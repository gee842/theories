"""Readability lint and schema-2 prototype: form only, never the substance of a boundary."""
import copy
import json
import unittest

from tools.research import registry, style


def v1_record(**fields):
    base = {'id': 'example', 'schema_version': 1, 'title': {'en': 'Example', 'zh': '例'},
            'claim': {'en': 'Every step keeps the balance.', 'zh': '每一步保持平衡。'},
            'limitations': {'en': 'Stated for discrete steps.', 'zh': '按离散步骤陈述。'},
            'validation_scope': {'en': 'Checked.', 'zh': '已查。'}, 'correspondence': {'en': 'Formal.', 'zh': '形式。'},
            'next_delta': {'en': 'None.', 'zh': '无。'}, 'hypotheses': [], 'counterexamples': []}
    base.update(fields)
    return base


class StyleTests(unittest.TestCase):
    def rules(self, record):
        return {f['rule'] for f in style.lint(record)}

    def test_process_markers_in_claim(self):
        r = v1_record(claim={'en': 'P92 shows the bound (receipt 20261013T125626.097616Z); this round adds §29.', 'zh': '本轮'})
        found = self.rules(r)
        for rule in ('process-marker:round-number', 'process-marker:receipt-timestamp', 'process-marker:round-narration', 'process-marker:section-reference'):
            self.assertIn(rule, found)

    def test_lean_names_and_letters_are_not_round_numbers(self):
        r = v1_record(claim={'en': 'Uses World.P2 and P(x), J1–J4, BC1 and G0.', 'zh': '使用 G0。'})
        self.assertNotIn('process-marker:round-number', self.rules(r))

    def test_stock_boundary_is_suggested_as_key(self):
        r = v1_record(limitations={'en': 'Stated for discrete steps; evaluates neither arising nor ceasing.', 'zh': '…'})
        keys = {f['detail'] for f in style.lint(r) if f['rule'] == 'stock-boundary'}
        self.assertTrue(any('discrete-steps' in k for k in keys) and any('no-evaluation' in k for k in keys))

    def test_v1_findings_are_warnings_only(self):
        r = v1_record(claim={'en': 'P92 ' * 600, 'zh': 'x'})
        self.assertTrue(style.lint(r))
        self.assertEqual({f['severity'] for f in style.lint(r)}, {'warning'})

    def test_v2_findings_are_errors(self):
        r = v1_record(schema_version=2, statement={'en': 'Target: P90 shows it.', 'zh': '目标'})
        r.pop('limitations')
        self.assertIn('error', {f['severity'] for f in style.lint(r)})

    def test_round_accretion(self):
        r = v1_record(validation_scope={'en': 'P90 ok. P92 ok. P94 ok. P97 ok.', 'zh': '…'})
        self.assertIn('round-accretion', self.rules(r))

    def test_ratchet_blocks_growth_of_v1_boundaries(self):
        old = v1_record()
        new = copy.deepcopy(old)
        new['limitations']['en'] += ' This round adds no new theorem.'
        self.assertEqual([f['rule'] for f in style.growth(old, new)], ['v1-growth'])
        new['schema_version'] = 2
        self.assertEqual(style.growth(old, new), [])

    def test_current_records_still_pass_structural_validation(self):
        records = [json.loads(p.read_text()) for p in sorted(registry.RECORDS.glob('*.json'))]
        errors, _ = registry.validate(records)
        self.assertEqual(errors, [])

    def test_schema2_rejects_unknown_standard_boundary_and_bad_anchor(self):
        records = [json.loads(p.read_text()) for p in sorted(registry.RECORDS.glob('*.json'))]
        r = next((x for x in records if x.get('schema_version') == 2 and x.get('progress')), None)
        if r is None:
            self.skipTest('no schema-2 record with progress in this tree')
        r = copy.deepcopy(r)
        r['standard_boundaries'] = ['no-such-boundary']
        r['progress'][0]['source'] = r['progress'][0]['source'].split('#')[0] + '#no-such-anchor'
        messages = '\n'.join(registry.validate_v2(r))
        self.assertIn('unknown standard boundary', messages)
        self.assertIn('progress anchor missing', messages)

    def test_schema2_text_version_is_hash_bound(self):
        records = [json.loads(p.read_text()) for p in sorted(registry.RECORDS.glob('*.json'))]
        r = next((x for x in records if x.get('text_versions')), None)
        if r is None:
            self.skipTest('no migrated record in this tree')
        r = copy.deepcopy(r)
        r['text_versions'][0]['sha256'] = '0' * 64
        self.assertIn('text version missing or changed', '\n'.join(registry.validate_v2(r)))


if __name__ == '__main__':
    unittest.main()
