"""Schema 2 records: structure, shared boundaries, hash-bound earlier text, rendering and search.

Most cases run in a temporary repository root, so they neither read nor write the real
records. The last class validates the migration drafts of the planning study against the
current records, without installing them.
"""
import copy
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from tools.research import registry, research, style

DRAFTS = registry.ROOT / ('_process/research/2026-10-05-generative-foundation-review/root-foundation/development/'
                          'becoming-general-laws-plan/readability/drafts')


def pair(en, zh):
    return {'en': en, 'zh': zh}


class TemporaryRoot:
    """A minimal repository root: configuration, one schema-1 record, one source, shared boundaries."""

    def __enter__(self):
        self.folder = tempfile.TemporaryDirectory()
        root = self.root = Path(self.folder.name).resolve()
        (root / '_process').mkdir()
        (root / 'records').mkdir()
        (root / 'data').mkdir()
        (root / 'RESULTS.md').write_text('# Register\n')
        (root / 'source.md').write_text('# Source\n\n## Exchange balances\n\nText.\n')
        (root / 'Law.lean').write_text('theorem Example.balanced : True := trivial\n')
        (root / 'data/boundaries.json').write_text(json.dumps({'boundaries': {
            'discrete-steps': {'en': 'Stated for discrete steps.', 'zh': '按离散步骤陈述。', 'source': 'source.md'}}}))
        self.settings = {'record_directories': ['records'], 'standard_boundaries': 'data/boundaries.json', 'record_snapshots': 'history'}
        (root / '_process/research-config.json').write_text(json.dumps(self.settings))
        self.v1 = {'schema_version': 1, 'id': 'example', 'title': pair('Example: every exchange balances along the run', '例')}
        (root / 'records/example.json').write_text(json.dumps(self.v1, ensure_ascii=False, indent=2) + '\n')
        self.patches = [patch.object(registry, 'ROOT', root), patch.object(registry, 'RECORDS', root / 'records')]
        for p in self.patches:
            p.start()
        return self

    def __exit__(self, *exc):
        for p in self.patches:
            p.stop()
        self.folder.cleanup()

    def record(self, **fields):
        source = {'path': 'source.md', 'role': 'statement', 'sha256': registry.digest(self.root / 'source.md')}
        law = {'path': 'Law.lean', 'role': 'review', 'sha256': registry.digest(self.root / 'Law.lean'), 'declarations': ['Example.balanced']}
        r = {'schema_version': 2, 'id': 'example', 'kind': 'target', 'status': 'open', 'family': 'F01',
             'reviewed_at_utc': '2026-10-14T00:00:00+00:00', '_record_path': 'records/example.json',
             'title': pair('Balanced exchange', '平衡交换'),
             'statement': pair('Every exchange balances along the run.', '沿运行每次交换都平衡。'),
             'laws': [dict(pair('Balance at each step is balance along every course.', '每步平衡即每一历程平衡。'), declarations=['Example.balanced'])],
             'hypotheses': [pair('A finite run.', '有限运行。')],
             'not_required': [pair('No unique vocabulary.', '不要求唯一语言。')],
             'does_not_show': [dict(pair('Balance does not give a direction.', '平衡不给出方向。'), kind='non-implication', witness='Example.balanced')],
             'standard_boundaries': ['discrete-steps'],
             'progress': [dict(pair('Exchange connected.', '交换已接通。'), source='source.md#exchange-balances')],
             'correspondence': pair('Formal.', '形式。'), 'validation_scope': pair('Reviewed.', '已审。'),
             'next_delta': pair('State the converse.', '陈述逆命题。'), 'canonical_source': 'source.md',
             'aliases': [], 'dependencies': [], 'related': [], 'counterexamples': [], 'references': [source, law],
             'history': [pair('Migrated.', '已迁移。')], 'text_versions': [registry.snapshot_record('example', self.settings)]}
        r.update(fields)
        return r


class Schema2ValidationTests(unittest.TestCase):
    def test_complete_record_validates_and_renders(self):
        with TemporaryRoot() as t:
            r = t.record()
            errors, drift = registry.validate([r])
            self.assertEqual((errors, drift), ([], []))
            page = registry.render_record(r)
        order = [page.index(x) for x in ('> Every exchange', '## Progress', '## Laws', '## Conditions', '## Does not show',
                                         'Stated for discrete steps.', '## Evidence', '## Next', '<details>', '### Earlier text')]
        self.assertEqual(order, sorted(order))
        self.assertIn('[study](../source.md#exchange-balances)', page)
        self.assertIn('Witness: `Example.balanced`', page)

    def test_snapshot_keeps_exact_bytes_and_never_overwrites(self):
        with TemporaryRoot() as t:
            entry = registry.snapshot_record('example', t.settings)
            raw = (t.root / 'records/example.json').read_bytes()
            self.assertEqual((t.root / entry['path']).read_bytes(), raw)
            self.assertEqual(entry['path'], f'history/{entry["sha256"][:16]}/example.json')
            self.assertEqual(registry.snapshot_record('example', t.settings), entry)  # idempotent
            (t.root / entry['path']).write_text('{}')
            with self.assertRaisesRegex(ValueError, 'Refusing to overwrite'):
                registry.snapshot_record('example', t.settings)

    def test_text_version_is_hash_bound_and_belongs_to_the_record(self):
        with TemporaryRoot() as t:
            r = t.record()
            changed = copy.deepcopy(r)
            changed['text_versions'][0]['sha256'] = '0' * 64
            self.assertIn('text version missing or changed', '\n'.join(registry.validate_v2_fields(changed, t.settings)))
            other = copy.deepcopy(r)
            other['id'] = 'another'
            self.assertIn('not an earlier version of this record', '\n'.join(registry.validate_v2_fields(other, t.settings)))
            outside = copy.deepcopy(r)
            outside['text_versions'][0] = {**r['text_versions'][0], 'path': 'records/example.json'}
            self.assertIn('stored under record_snapshots', '\n'.join(registry.validate_v2_fields(outside, t.settings)))
            unpaired = copy.deepcopy(r)
            unpaired['text_versions'][0]['note'] = 'English only'
            self.assertIn('bilingual note', '\n'.join(registry.validate_v2_fields(unpaired, t.settings)))

    def test_rejects_unknown_boundary_bad_anchor_and_undeclared_names(self):
        with TemporaryRoot() as t:
            r = t.record(standard_boundaries=['no-such-boundary'])
            r['progress'][0]['source'] = 'source.md#no-such-anchor'
            r['laws'][0]['declarations'] = ['Example.nowhere']
            r['does_not_show'][0].update(kind='aside', witness='Example.elsewhere')
            messages = '\n'.join(registry.validate_v2_fields(r, t.settings))
        for expected in ('unknown standard boundary', 'progress anchor missing', 'law names undeclared references',
                         'does_not_show kind must be one of', 'witness is not a declared reference'):
            self.assertIn(expected, messages)

    def test_progress_needs_a_hashed_reference(self):
        with TemporaryRoot() as t:
            r = t.record()
            r['progress'][0]['source'] = 'RESULTS.md'
            self.assertIn('progress source must be a hashed reference', '\n'.join(registry.validate_v2_fields(r, t.settings)))

    def test_schema_2_replaces_limitations_and_pairs_every_item(self):
        with TemporaryRoot() as t:
            r = t.record(limitations=pair('Old block.', '旧块。'))
            r['not_required'].append({'en': 'English only'})
            messages = '\n'.join(registry.validate_v2_fields(r, t.settings))
        self.assertIn('schema 2 replaces limitations', messages)
        self.assertIn('not_required items require nonempty Chinese and English', messages)

    def test_schema_2_needs_statement_and_lint_errors_fail(self):
        with TemporaryRoot() as t:
            r = t.record()
            r.pop('statement')
            self.assertIn('statement requires nonempty Chinese and English', '\n'.join(registry.validate([r])[0]))
            r = t.record(next_delta=pair('After P92 and P94 (receipt 20261013T125626Z), continue.', '继续。'))
            errors = '\n'.join(registry.validate([r])[0])
        self.assertIn('next_delta: process-marker:round-number', errors)
        self.assertIn('next_delta: process-marker:receipt-timestamp', errors)

    def test_does_not_show_can_stand_for_counterexamples(self):
        with TemporaryRoot() as t:
            r = t.record()
            self.assertEqual(r['counterexamples'], [])
            self.assertEqual(registry.validate([r])[0], [])
            r['does_not_show'] = []
            self.assertIn('counterexamples or explicit scoped boundary required', '\n'.join(registry.validate([r])[0]))

    def test_shared_boundary_file_is_checked(self):
        with TemporaryRoot() as t:
            (t.root / 'data/boundaries.json').write_text(json.dumps({'boundaries': {'Bad Key': {'en': 'x', 'zh': '', 'source': 'missing.md'}}}))
            errors = registry.validate_standard_boundaries(t.settings)
        self.assertTrue(any('not a stable name' in e for e in errors))
        self.assertTrue(any('requires nonempty Chinese and English' in e for e in errors))

    def test_repository_boundaries_are_bilingual_and_sourced(self):
        self.assertEqual(registry.validate_standard_boundaries(), [])
        known = registry.standard_boundaries()
        self.assertEqual(known['no-ethical-premise'], {**known['no-ethical-premise'], 'en': 'No ethical premise and no Lean axiom is used.', 'zh': '不用伦理前提，也不用 Lean 公理。'})

    def test_changed_boundary_file_selects_citing_records(self):
        records = [{'id': 'a', '_record_path': 'r/a.json', 'references': [], 'dependencies': [], 'standard_boundaries': ['discrete-steps']},
                   {'id': 'b', '_record_path': 'r/b.json', 'references': [], 'dependencies': []}]
        self.assertEqual(registry.affected_ids(records, {registry.standard_boundaries_path()}), {'a'})


class Schema1StatementTests(unittest.TestCase):
    def test_statement_renders_first_and_leaves_other_pages_unchanged(self):
        records, _ = registry.load_records()
        r = copy.deepcopy(next(r for r in records if r.get('schema_version') == 1 and 'statement' not in r))
        before = registry.render_record(r)
        r['statement'] = pair('Every exchange balances along the run.', '沿运行每次交换都平衡。')
        after = registry.render_record(r)
        lines = after.splitlines()
        self.assertEqual(lines[4:8], ['> Every exchange balances along the run.', '>', '> 沿运行每次交换都平衡。', ''])
        self.assertEqual(after.replace('> Every exchange balances along the run.\n>\n> 沿运行每次交换都平衡。\n\n', ''), before)

    def test_statement_is_validated_and_schema_2_fields_need_schema_2(self):
        with TemporaryRoot() as t:
            r = t.record()
            r.update(schema_version=1, claim=pair('Every exchange balances.', '每次交换都平衡。'), limitations=pair('Discrete.', '离散。'),
                     counterexamples=[{'detail': pair('Scope.', '范围。'), 'path': 'source.md'}])
            for key in registry.V2_LISTS:
                r.pop(key)
            self.assertEqual(registry.validate([r])[0], [])
            r['statement'] = pair('P92: ' + 'x' * 300, '陈述')
            r['does_not_show'] = []
            errors = '\n'.join(registry.validate([r])[0])
        self.assertIn('statement: length', errors)
        self.assertIn('statement: process-marker:round-number', errors)
        self.assertIn('schema-2 fields need schema_version 2: does_not_show', errors)

    def test_schema_1_lint_never_fails_validation(self):
        with TemporaryRoot() as t:
            r = t.record()
            r.update(schema_version=1, claim=pair('P92 shows it (receipt 20261013T125626Z); this round adds §29.', '本轮'),
                     limitations=pair('Stated for discrete steps.', '按离散步骤陈述。'),
                     counterexamples=[{'detail': pair('Scope.', '范围。'), 'path': 'source.md'}])
            for key in registry.V2_LISTS + ('statement',):
                r.pop(key)
            self.assertTrue(style.lint(r))
            self.assertEqual(registry.validate([r])[0], [])


class SearchTests(unittest.TestCase):
    def test_find_searches_statement_laws_and_does_not_show(self):
        with TemporaryRoot() as t:
            r = t.record()
        r.pop('claim', None)
        r['_record_path'] = 'theories/becoming/results/records/example.json'
        for needle in ('balances along the run', 'balance along every course', 'does not give a direction'):
            with patch.object(registry, 'load_records', return_value=([r], [])), patch.object(research, 'inventory', return_value=[]):
                found = research.search(needle)['results']
            self.assertEqual([x.get('id') for x in found], ['example'], needle)


@unittest.skipUnless(DRAFTS.is_dir(), 'migration drafts not in this tree')
class MigrationDraftTests(unittest.TestCase):
    """The three drafts validate in place of their schema-1 records, and their pages link correctly.

    The drafts predate the paired note, so it is paired here; their snapshots are the
    adjacent .v1.json files. Declaration presence is left out: it is checked against the
    current Lean sources, which later renames may change, and is covered by the registry tests.
    """

    def test_drafts_validate_and_render(self):
        records, _ = registry.load_records()
        by_id = {r['id']: r for r in records}
        snapshots, drafts = {}, []
        for path in sorted(DRAFTS.glob('*.v2.json')):
            r = json.loads(path.read_text())
            for version in r['text_versions']:
                snapshots[version['path']] = DRAFTS / (r['id'] + '.v1.json')
                if isinstance(version['note'], str):
                    version['note'] = pair(version['note'], '迁移前的记录原始字节（schema 1）。')
            r['_record_path'] = by_id[r['id']]['_record_path']
            r['_record_links'] = by_id[r['id']]['_record_links']
            by_id[r['id']] = r
            drafts.append(r)
        self.assertEqual(len(drafts), 3)
        real = registry.path_in_repo
        with patch.object(registry, 'path_in_repo', side_effect=lambda value: snapshots.get(value) or real(value)):
            errors, _ = registry.validate(sorted(by_id.values(), key=lambda r: r['id']))
            pages = {str(registry.record_path(r).with_suffix('.md').relative_to(registry.ROOT)): registry.render_record(r) for r in drafts}
        ids = {r['id'] for r in drafts}
        self.assertEqual([e for e in errors if e.split(':')[0] in ids and 'declaration not found' not in e], [])
        self.assertEqual([e for e in errors if e.split(':')[0] not in ids], [])
        self.assertEqual([e for e in research.check_links(pages) if 'architecture/history' not in e], [])
        for r in drafts:
            self.assertEqual([f for f in style.lint(r) if f['severity'] == 'error'], [])


if __name__ == '__main__':
    unittest.main()
