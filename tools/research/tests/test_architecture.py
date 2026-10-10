import copy
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from tools.research import registry, navigation, research


class ArchitectureTests(unittest.TestCase):
    def test_changed_source_selects_downstream_consumers(self):
        records = [{'id': 'a', '_record_path': 'r/a.json', 'references': [{'path': 'A.lean'}], 'dependencies': []},
                   {'id': 'b', '_record_path': 'r/b.json', 'references': [], 'dependencies': [{'id': 'a'}]},
                   {'id': 'c', '_record_path': 'r/c.json', 'references': [], 'dependencies': []}]
        self.assertEqual(registry.affected_ids(records, {'A.lean'}), {'a', 'b'})

    def test_stale_record_does_not_block_healthy_render(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            (root/'stale.md').write_text('previous checked page')
            with patch.object(registry, 'OUT', root), patch.object(registry, 'record_path', side_effect=lambda r: root/(r['id']+'.json')), patch.object(registry, 'render_index', return_value='index'), patch.object(registry, 'render_record', return_value='healthy page'):
                written = registry.write_views([{'id': 'stale'}, {'id': 'healthy'}], [{'id': 'stale'}])
            self.assertEqual(written, ['healthy'])
            self.assertEqual((root/'stale.md').read_text(), 'previous checked page')
            self.assertEqual((root/'healthy.md').read_text(), 'healthy page')

    def test_concurrent_prose_is_never_overwritten(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            (root/'README.md').write_text('another session added evidence')
            (root/'history.json').write_text(json.dumps({'documents': {'README.md': {'sha256': navigation.sha(b'old')}}}))
            with patch.object(navigation, 'ROOT', root), patch.object(navigation, 'HISTORY', root/'history.json'), patch.object(navigation, 'MANIFEST', root/'generated.json'):
                errors = navigation.write_views({'README.md': 'new generated view'})
            self.assertIn('Unincorporated concurrent edit', errors[0])
            self.assertEqual((root/'README.md').read_text(), 'another session added evidence')

    def test_preservation_keeps_original_bytes_and_adapts_only_links(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            raw = '# Example\n\n[Evidence](notes/proof.md#scope)\n'
            (root/'README.md').write_text(raw)
            with patch.object(navigation, 'ROOT', root):
                saved = navigation.preserve('README.md')
            self.assertEqual((root/saved['raw']).read_bytes(), raw.encode())
            self.assertIn('#scope)', (root/saved['reading']).read_text())
            self.assertNotEqual((root/saved['reading']).read_text(), raw)

    def test_default_discovery_excludes_frozen_copies(self):
        self.assertTrue(research.working('experiments/a/Current.lean'))
        self.assertFalse(research.working('experiments/a/checks/20261008T123456Z/Current.lean'))
        self.assertFalse(research.working('experiments/a/verification/sources/Current.lean'))
        self.assertFalse(research.working('_process/architecture/history/deadbeef/README.md'))
        self.assertFalse(research.working('sources/imported/Current.lean'))

    def test_planned_generated_links_can_be_rendered_together(self):
        self.assertEqual(research.check_links({'README.md': '[New](future-test-view.md)'}, ['future-test-view.md']), [])

    def test_generated_links_check_heading_fragments(self):
        views = {'one.md': '[Other](two.md#missing)', 'two.md': '# Present\n'}
        self.assertIn('missing anchor', research.check_links(views, views)[0])
        views['one.md'] = '[Other](two.md#present)'
        self.assertEqual(research.check_links(views, views), [])

    def test_orphan_pages_checked_across_all_record_directories(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            (root/'_process').mkdir()
            (root/'_process/research-config.json').write_text(json.dumps({'record_directories': ['branch-a', 'branch-b']}))
            (root/'branch-a').mkdir(); (root/'branch-b').mkdir()
            (root/'branch-b/orphan.md').write_text('retained evidence')
            with patch.object(registry, 'ROOT', root):
                errors = registry.orphan_pages([])
            self.assertIn('branch-b/orphan.md', errors[0])

    def test_malformed_record_reports_errors_without_crashing(self):
        records, _ = registry.load_records()
        records = copy.deepcopy(records)
        records[0]['dependencies'] = 'invalid'
        errors, _ = registry.validate(records)
        self.assertTrue(any('expected lists' in e for e in errors))

    def test_output_input_contract_must_have_reviewed_evidence(self):
        records, _ = registry.load_records()
        r = next(r for r in records if r['dependencies'])
        r['dependencies'][0]['interface'] = {'output': {'zh':'出','en':'output'}, 'input': {'zh':'入','en':'input'}, 'conditions': {'zh':'条件','en':'conditions'}, 'evidence': 'unreviewed.md'}
        errors, _ = registry.validate(records)
        self.assertTrue(any('evidence must be a reviewed reference' in e for e in errors))

    def test_cross_branch_result_links_resolve_from_consumer(self):
        records, _ = registry.load_records()
        r = copy.deepcopy(next(r for r in records if r['dependencies']))
        ident = r['dependencies'][0]['id']
        r['_record_path'] = 'theories/other/results/records/consumer.json'
        r['_record_links'][ident] = 'theories/first/results/records/producer.json'
        self.assertIn('../../../first/results/records/producer.md', registry.render_record(r))
        self.assertIn('../../../../RESULTS.md', registry.render_record(r))

    def test_source_change_invalidates_render_snapshot(self):
        with patch.object(research, 'input_snapshot', return_value={'source': 'new'}):
            self.assertFalse(research.unchanged_inputs({'source': 'old'}))

    def test_render_snapshot_includes_the_readme_opening(self):
        config = {'goal_directory': 'no-such-goal-directory', 'record_directories': [], 'readme_opening': 'no-such-opening.md'}
        with patch.object(navigation, 'read', return_value=config):
            snapshot = research.input_snapshot()
        self.assertIn(str(research.ROOT / 'no-such-opening.md'), snapshot)

    def test_reconciliation_preserves_all_prior_versions(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            (root/'README.md').write_text('# Earlier\n')
            with patch.object(navigation, 'ROOT', root), patch.object(navigation, 'HISTORY', root/'history.json'), patch.object(navigation, 'MANIFEST', root/'generated.json'):
                first = navigation.preserve('README.md')
                (root/'history.json').write_text(json.dumps({'documents': {'README.md': first}}))
                (root/'README.md').write_text('# Added by another session\n')
                latest = navigation.preserve_view('README.md', 'Reviewed and integrated in the existing study.')
                self.assertEqual(latest['prior_versions'][0], first)
                self.assertEqual(navigation.validate_history(), [])
                self.assertIn('earlier', '\n'.join(navigation.preserved_anchors('README.md', navigation.read(root/'history.json'))))

    def test_previous_stale_page_guard_is_kept_in_manifest(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            (root/'history.json').write_text('{"documents": {}}')
            (root/'generated.json').write_text(json.dumps({'files': {'stale.md': 'retained'}}))
            with patch.object(navigation, 'ROOT', root), patch.object(navigation, 'HISTORY', root/'history.json'), patch.object(navigation, 'MANIFEST', root/'generated.json'):
                self.assertEqual(navigation.write_views({'new.md': 'new'}), [])
            self.assertEqual(json.loads((root/'generated.json').read_text())['files']['stale.md'], 'retained')


if __name__ == '__main__':
    unittest.main()
