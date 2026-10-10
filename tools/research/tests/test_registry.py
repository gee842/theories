"""Check registry failure modes without changing sources or scientific receipts."""
import copy
import json
import unittest
from unittest.mock import patch

from tools.research import registry


class RegistryTests(unittest.TestCase):
    def setUp(self):
        self.records = [json.loads(p.read_text()) for p in sorted(registry.RECORDS.glob('*.json'))]
        self.proved = next(r for r in self.records if r['status'] == 'recorded-checked')

    def errors(self):
        return '\n'.join(registry.validate(self.records)[0])

    def test_current_records_are_structurally_valid(self):
        self.assertEqual(self.errors(), '')

    def test_case_insensitive_alias_collision(self):
        self.records[0]['aliases'].append(self.records[1]['id'].upper())
        self.assertIn('duplicate alias', self.errors())

    def test_missing_dependency(self):
        self.records[0]['dependencies'].append({'id': 'missing-result', 'relation': 'formal-reuse', 'detail': {'zh': '测试', 'en': 'test'}})
        self.assertIn('missing or self result link', self.errors())

    def test_dependency_cycle(self):
        a, b = self.records[:2]
        for x, y in [(a, b), (b, a)]:
            x['dependencies'].append({'id': y['id'], 'relation': 'application', 'detail': {'zh': '测试', 'en': 'test'}})
        self.assertIn('circular result dependency', self.errors())

    def test_checked_without_receipt_is_rejected(self):
        self.proved['references'] = [r for r in self.proved['references'] if r['role'] != 'receipt']
        self.assertIn('needs proof source and existing receipt', self.errors())

    def test_wrong_receipt_binding_is_rejected(self):
        self.proved['proof_bindings'][0]['sha256_pointer'] = '/no-such-source'
        self.assertIn('invalid proof receipt binding', self.errors())

    def test_unelaborated_declaration_name_is_rejected(self):
        for r in self.records:
            refs = {x['path']: x for x in r.get('references', [])}
            for binding in r.get('proof_bindings', []):
                data = json.loads((registry.ROOT / binding['receipt']).read_text())
                module = binding['sha256_pointer'].rsplit('/', 1)[-1]
                names = refs[binding['source']].get('declarations', [])
                if names and any(m.get('module') == module for m in data.get('modules', [])):
                    names.append('Nowhere.' + names[0].split('.')[-1])
                    self.assertIn('declarations not elaborated', self.errors())
                    return
        self.skipTest('no receipt lists elaborated declarations')

    def test_unelaborated_alias_is_rejected(self):
        for r in self.records:
            for alias in r.get('aliases', []):
                if alias.startswith('Becoming.') and r.get('proof_bindings'):
                    r['aliases'].append(alias + '_nowhere')
                    self.assertIn('alias not elaborated', self.errors())
                    return
        self.skipTest('no record has a Lean alias and a receipt binding')

    def test_open_target_cannot_be_claimed_complete(self):
        next(r for r in self.records if r['kind'] == 'target')['status'] = 'reviewed-scoped'
        self.assertIn('a target cannot be marked completed', self.errors())

    def test_source_drift_is_reported_without_rewriting_hash(self):
        original = copy.deepcopy(self.records)
        path = registry.ROOT / self.proved['canonical_source']
        real_digest = registry.digest
        with patch.object(registry, 'digest', side_effect=lambda p: '0' * 64 if p == path else real_digest(p)):
            _, drift = registry.validate(self.records)
        self.assertTrue(any(d['path'] == self.proved['canonical_source'] for d in drift))
        self.assertEqual(original, self.records)

    def test_outside_reference_rejected(self):
        self.records[0]['references'][0]['path'] = '../../outside-the-repository'
        self.assertIn('missing or unsafe reference', self.errors())


if __name__ == '__main__':
    unittest.main()
