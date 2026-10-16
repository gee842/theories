import hashlib
import json
from pathlib import Path
import subprocess
import tempfile
import unittest

from tools.research import moves, paths, research


def git(root, *args):
    return subprocess.run(['git', '-c', 'user.name=Test', '-c', 'user.email=test@example.invalid', *args], cwd=root,
                          check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout.decode()


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


CONFIG = {
    'record_directories': ['theories/becoming/results/records'],
    'goal_directory': '_process/goals',
    'move_receipts': '_process/architecture/moves',
    'move_pinned': ['theories/becoming/OPENING.md', 'sources/**'],
    'move_rewrite_extra': ['tools/paths.txt'],
}


class Fixture:
    """A small git repository with live, generated-free, history and evidence referrers."""

    def __init__(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        files = {
            '_process/research-config.json': json.dumps(CONFIG, indent=2) + '\n',
            '_process/DIGEST.md': '# Scope / 范围\n\nBody. [Back](../docs/A.md)\n',
            '_process/old-study/NOTE.md': '# Note\n',
            '_process/old-study/deep/PART.md': '# Part\n',
            'docs/A.md': ('# A\n\n[Digest](../_process/DIGEST.md#scope--范围) and [study](../_process/old-study/deep/PART.md)'
                          ' and [dir](../_process/old-study/).\n\n`[code](../_process/DIGEST.md)` stays.\n'),
            'README.md': 'See [digest](_process/DIGEST.md) and [opening](theories/becoming/OPENING.md).\n',
            'theories/becoming/OPENING.md': '# Opening\n',
            'theories/becoming/results/records/r.json': None,
            'archive/history/H.md': '[old](../../_process/DIGEST.md)\n',
            'runs/20261016T121942.123456Z/R.md': '[old](../../_process/DIGEST.md)\n',
            'experiments/x/data.txt': 'frozen data\n',
            'tools/paths.txt': 'reads _process/DIGEST.md and _process/old-study/NOTE.md.\n',
            'sources/original.md': '[old](../_process/DIGEST.md)\n',
        }
        for name, body in files.items():
            if body is None:
                continue
            p = self.root / name
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_text(body)
        freeze = {'files': {'experiments/x/data.txt': sha(self.root / 'experiments/x/data.txt')}}
        (self.root / 'experiments/x/FREEZE.json').write_text(json.dumps(freeze, indent=2) + '\n')
        record = {
            'id': 'r', 'canonical_source': '_process/DIGEST.md#scope',
            'references': [{'path': '_process/DIGEST.md', 'role': 'reading', 'sha256': sha(self.root / '_process/DIGEST.md')},
                           {'path': 'theories/becoming/OPENING.md', 'role': 'reading'}],
            'counterexamples': [{'path': '_process/old-study/NOTE.md'}],
            'history': [{'en': 'Reviewed _process/DIGEST.md in prose.'}],
            'pointer': '/artifacts/_process/DIGEST.md',
        }
        p = self.root / 'theories/becoming/results/records/r.json'
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(json.dumps(record, ensure_ascii=False, indent=2) + '\n')
        git(self.root, 'init', '-q')
        git(self.root, 'add', '-A')
        git(self.root, 'commit', '-q', '-m', 'fixture')

    def plan(self, rows):
        path = self.root / 'plan.tsv'
        path.write_text(''.join('\t'.join(r) + '\n' for r in rows))
        return moves.Plan(moves.Plan.read(path), root=self.root, batch='test-batch').analyse()

    def close(self):
        self.tmp.cleanup()


class MoveTests(unittest.TestCase):
    def setUp(self):
        self.f = Fixture()
        self.root = self.f.root
        (self.root / 'plan.tsv').unlink(missing_ok=True)

    def tearDown(self):
        self.f.close()

    def test_dry_run_reports_without_changing_anything(self):
        before = {p: sha(self.root / p) for p in ('docs/A.md', 'theories/becoming/results/records/r.json')}
        plan = self.f.plan([('_process/DIGEST.md', '_process/history/2026-09/DIGEST.md', 'superseded')])
        report = plan.report()
        self.assertEqual(report['conflicts'], [])
        self.assertEqual(report['summary']['files_moved'], 1)
        rewritten = {r['path'] for r in report['rewrites']}
        self.assertEqual(rewritten, {'docs/A.md', 'README.md', 'theories/becoming/results/records/r.json', 'tools/paths.txt'})
        self.assertEqual({p: sha(self.root / p) for p in before}, before)
        self.assertTrue((self.root / '_process/DIGEST.md').exists())
        # The moved file's own link breaks at the new depth; it is reported, not edited.
        self.assertEqual(len(report['moved_markdown_links_broken_by_move']), 1)
        # The prose mention inside the record is reported, not rewritten.
        self.assertTrue(any(m['file'].endswith('r.json') for m in report['unrewritten_live_mentions']))

    def test_apply_moves_bytes_rewrites_live_references_and_writes_receipts(self):
        digest = sha(self.root / '_process/DIGEST.md')
        frozen = {p: sha(self.root / p) for p in ('archive/history/H.md', 'runs/20261016T121942.123456Z/R.md', 'sources/original.md')}
        plan = self.f.plan([('_process/DIGEST.md', '_process/history/2026-09/DIGEST.md', 'superseded'),
                            ('_process/old-study', '_process/history/old-study', 'retired study')])
        result = plan.apply()
        self.assertEqual(result['verification_errors'], [])
        new = self.root / '_process/history/2026-09/DIGEST.md'
        self.assertEqual(sha(new), digest)
        self.assertFalse((self.root / '_process/DIGEST.md').exists())
        self.assertIn('R  _process/DIGEST.md -> _process/history/2026-09/DIGEST.md', git(self.root, 'status', '--porcelain'))
        a = (self.root / 'docs/A.md').read_text()
        self.assertIn('](../_process/history/2026-09/DIGEST.md#scope--范围)', a)
        self.assertIn('](../_process/history/old-study/deep/PART.md)', a)
        self.assertIn('](../_process/history/old-study/)', a)
        self.assertIn('`[code](../_process/DIGEST.md)`', a)  # code is not a link
        self.assertIn('[digest](_process/history/2026-09/DIGEST.md)', (self.root / 'README.md').read_text())
        self.assertEqual((self.root / 'tools/paths.txt').read_text(),
                         'reads _process/history/2026-09/DIGEST.md and _process/history/old-study/NOTE.md.\n')
        record = json.loads((self.root / 'theories/becoming/results/records/r.json').read_text())
        self.assertEqual(record['canonical_source'], '_process/history/2026-09/DIGEST.md#scope')
        self.assertEqual(record['references'][0]['path'], '_process/history/2026-09/DIGEST.md')
        self.assertEqual(record['references'][0]['sha256'], digest)
        self.assertEqual(record['counterexamples'][0]['path'], '_process/history/old-study/NOTE.md')
        self.assertEqual(record['history'][0]['en'], 'Reviewed _process/DIGEST.md in prose.')
        self.assertEqual(record['pointer'], '/artifacts/_process/DIGEST.md')
        for p, digest_before in frozen.items():
            self.assertEqual(sha(self.root / p), digest_before, p)
        receipt = json.loads((self.root / '_process/architecture/moves/test-batch.json').read_text())
        self.assertEqual(receipt['batch'], 'test-batch')
        self.assertEqual(receipt['base_commit'], git(self.root, 'rev-parse', 'HEAD').strip())
        files = {f['old_path']: f for f in receipt['files']}
        self.assertEqual(files['_process/DIGEST.md']['new_path'], '_process/history/2026-09/DIGEST.md')
        self.assertEqual(files['_process/DIGEST.md']['sha256'], digest)
        self.assertEqual(files['_process/DIGEST.md']['blob'], git(self.root, 'hash-object', str(new)).strip())
        self.assertEqual(files['_process/old-study/deep/PART.md']['reason'], 'retired study')
        rewritten = {r['path']: r for r in receipt['rewritten']}
        self.assertEqual(rewritten['docs/A.md']['new_sha256'], sha(self.root / 'docs/A.md'))
        manifest = json.loads((self.root / '_process/history/MANIFEST.json').read_text())
        self.assertEqual(len(manifest['entries']), 3)
        self.assertEqual({e['batch'] for e in manifest['entries']}, {'test-batch'})
        index = (self.root / '_process/history/INDEX.md').read_text()
        self.assertIn('`_process/old-study`', index)
        self.assertIn('| 2 | retired study |', index)
        self.assertEqual(moves.former_paths('_process/history/2026-09/DIGEST.md', root=self.root, settings=CONFIG),
                         ['_process/DIGEST.md'])

    def test_pinned_paths_are_refused(self):
        plan = self.f.plan([('theories/becoming/OPENING.md', 'theories/becoming/history/OPENING.md', 'no'),
                            ('experiments/x/data.txt', 'experiments/history/data.txt', 'no'),
                            ('experiments/x/FREEZE.json', 'experiments/history/FREEZE.json', 'no'),
                            ('sources/original.md', 'history/original.md', 'no')])
        problems = [p for c in plan.conflicts for p in c['problems']]
        self.assertEqual(len(plan.conflicts), 4)
        self.assertTrue(all(p.startswith('pinned') for p in problems), problems)
        with self.assertRaises(ValueError):
            plan.apply()
        self.assertTrue((self.root / 'theories/becoming/OPENING.md').exists())
        self.assertFalse((self.root / '_process/architecture/moves/test-batch.json').exists())

    def test_missing_source_and_existing_target_are_conflicts(self):
        plan = self.f.plan([('_process/NOPE.md', '_process/history/NOPE.md', 'x'),
                            ('_process/DIGEST.md', 'docs/A.md', 'x')])
        problems = {c['old']: c['problems'] for c in plan.conflicts}
        self.assertTrue(any('missing' in p for p in problems['_process/NOPE.md']))
        self.assertTrue(any('target exists' in p for p in problems['_process/DIGEST.md']))

    def test_history_component_is_history(self):
        c = paths.Classifier(settings={}, root=self.root, generated=set())
        self.assertEqual(c.role('a/history/b.md'), 'history')
        self.assertEqual(c.role('experiments/lean/history/Becoming/X.lean'), 'history')
        self.assertEqual(c.role('_process/architecture/history/abc/x.md'), 'history')
        self.assertEqual(c.role('x/becoming-checks/20261016T121942.917817Z/a.lean'), 'evidence')
        self.assertEqual(c.role('x/verification-history/a.md'), 'evidence')
        self.assertEqual(c.role('x/legacy-replays/a.md'), 'evidence')
        self.assertEqual(c.role('x/README-BEFORE-RESULTS.md'), 'evidence')
        self.assertEqual(c.role('sources/a/history/b.md'), 'source')
        self.assertEqual(c.role('.claude/worktrees/x/a.md'), 'scratch')
        self.assertEqual(c.role('docs/historyless/a.md'), 'live')
        self.assertEqual(c.role('docs/history.md'), 'live')
        self.assertEqual(paths.Classifier(settings=CONFIG, root=self.root, generated=set()).role('_process/architecture/moves/b.json'), 'evidence')
        self.assertFalse(research.working('experiments/a/history/Current.lean'))
        self.assertFalse(research.working('theories/becoming/history/OLD.md'))
        self.assertTrue(research.working('theories/becoming/chapters/THE-THEORY-OF-BECOMING.md'))

    def commit(self, message='step'):
        git(self.root, 'add', '-A')
        git(self.root, 'commit', '-q', '-m', message)

    def test_markdown_path_mentions_are_rewritten_outside_link_targets(self):
        (self.root / 'docs/B.md').write_text('Read `_process/DIGEST.md` and _process/old-study/NOTE.md.\n\n'
                                              '```sh\ncat _process/DIGEST.md\n```\n[x](theories/becoming/OPENING.md)\n')
        self.commit()
        plan = self.f.plan([('_process/DIGEST.md', '_process/history/2026-09/DIGEST.md', 'superseded'),
                            ('_process/old-study', '_process/history/old-study', 'retired study')])
        changes = {r['path']: r for r in plan.rewrites}['docs/B.md']['changes']
        self.assertEqual(sorted((c['kind'], c['old']) for c in changes),
                         [('path-mention', '_process/DIGEST.md'), ('path-mention', '_process/DIGEST.md'),
                          ('path-mention', '_process/old-study/NOTE.md')])
        text = {r['path']: r for r in plan.rewrites}['docs/B.md']['_text']
        self.assertIn('`_process/history/2026-09/DIGEST.md`', text)
        self.assertIn('cat _process/history/2026-09/DIGEST.md', text)
        # Mentions are off where the config says so.
        settings = dict(CONFIG, move_mentions_exclude=['docs/B.md'])
        off = moves.Plan(moves.Plan.read(self.root / 'plan.tsv'), root=self.root, settings=settings, batch='b').analyse()
        self.assertNotIn('docs/B.md', {r['path'] for r in off.rewrites})

    def test_keep_references_moves_without_rewriting(self):
        before = sha(self.root / 'docs/A.md')
        path = self.root / 'plan.tsv'
        path.write_text('_process/DIGEST.md\t_process/history/2026-09/DIGEST.md\treplaced afterwards\n')
        plan = moves.Plan(moves.Plan.read(path), root=self.root, batch='keep', keep_references=True).analyse()
        report = plan.report()
        self.assertEqual(report['rewrites'], [])
        self.assertTrue(report['summary']['live_references_kept_for_replacement'] > 0)
        result = plan.apply()
        self.assertEqual(sha(self.root / 'docs/A.md'), before)
        receipt = json.loads((self.root / result['receipt']).read_text())
        self.assertTrue(receipt['keep_references'])
        # Until the replacement is written, the check reports the dangling references.
        self.assertTrue(moves.check_receipt(result['receipt'], root=self.root, settings=CONFIG)['errors'])
        (self.root / '_process/DIGEST.md').write_text('# Scope / 范围\n\nNew short page.\n')
        check = moves.check_receipt(result['receipt'], root=self.root, settings=CONFIG)
        self.assertEqual(check['errors'], [])
        self.assertEqual(check['replaced_at_old_path'], 1)

    def test_check_receipt_and_receipt_lookups(self):
        plan = self.f.plan([('_process/DIGEST.md', '_process/history/2026-09/DIGEST.md', 'superseded'),
                            ('_process/old-study', '_process/history/old-study', 'retired study')])
        result = plan.apply()
        check = moves.check_receipt(result['receipt'], root=self.root, settings=CONFIG)
        self.assertEqual(check['errors'], [], check)
        self.assertTrue(any('r.json' in w for w in check['warnings']))  # record prose keeps its words
        self.assertEqual(moves.later_path('_process/old-study/deep/PART.md', self.root, CONFIG),
                         '_process/history/old-study/deep/PART.md')
        self.assertEqual(moves.later_path('_process/old-study/deep/', self.root, CONFIG), '_process/history/old-study/deep/')
        self.assertIsNone(moves.later_path('docs/A.md', self.root, CONFIG))
        self.assertEqual(moves.current_path('_process/DIGEST.md#scope', self.root, CONFIG), '_process/history/2026-09/DIGEST.md#scope')
        self.assertEqual(moves.current_path('docs/A.md', self.root, CONFIG), 'docs/A.md')
        self.assertEqual(moves.historical_paths(['_process/*.md'], self.root, CONFIG), {'_process/history/2026-09/DIGEST.md'})
        # A live link left at an old path, or changed bytes, fail the check.
        (self.root / 'docs/C.md').write_text('[stale](../_process/old-study/NOTE.md) and `_process/DIGEST.md`\n')
        (self.root / '_process/history/old-study/deep/PART.md').write_text('changed\n')
        errors = moves.check_receipt(result['receipt'], root=self.root, settings=CONFIG)['errors']
        self.assertTrue(any('docs/C.md' in e and 'markdown-link' in e for e in errors), errors)
        self.assertTrue(any('docs/C.md' in e and 'path-mention' in e for e in errors), errors)
        self.assertTrue(any('sha256 differs' in e for e in errors), errors)

    def test_reviewed_version_follows_moves(self):
        from tools.research import registry
        original = (self.root / '_process/DIGEST.md').read_text()
        digest = sha(self.root / '_process/DIGEST.md')
        self.f.plan([('_process/DIGEST.md', '_process/history/2026-09/DIGEST.md', 'superseded')]).apply()
        self.commit('move')
        (self.root / '_process/history/2026-09/DIGEST.md').write_text(original + '\nAdded later.\n')
        self.commit('edit')
        saved = registry.ROOT, registry.VERSION_CACHE, dict(registry._versions)
        try:
            registry.ROOT = self.root
            registry.VERSION_CACHE = self.root / '.cache-versions.json'
            registry._versions.clear()
            self.assertEqual(registry.reviewed_version('_process/history/2026-09/DIGEST.md', digest), original)
        finally:
            registry.ROOT, registry.VERSION_CACHE = saved[0], saved[1]
            registry._versions.clear()
            registry._versions.update(saved[2])

    def test_lean_history_is_a_saved_copy(self):
        from tools.research import lean_catalogue
        self.assertEqual(lean_catalogue.path_role('experiments/x/lean/history/connected/A.lean'), 'saved-copy')
        self.assertIsNone(lean_catalogue.path_role('experiments/x/lean/historyless/A.lean'))

    def test_evidence_command_passes_through(self):
        out = subprocess.run(['python3', '-B', str(paths.ROOT / 'tools/research/research.py'), 'evidence', '--help'],
                             stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        self.assertEqual(out.returncode, 0, out.stderr)
        self.assertIn('restore', out.stdout)

    def test_glob_matching(self):
        self.assertTrue(paths.matches('a/b/becoming-verification.json', ['**/becoming-verification.json']))
        self.assertTrue(paths.matches('becoming-verification.json', ['**/becoming-verification.json']))
        self.assertTrue(paths.matches('lean/becoming/Becoming/A/B.lean', ['lean/becoming/Becoming/**']))
        self.assertFalse(paths.matches('lean/becoming/BecomingX.lean', ['lean/becoming/Becoming/**']))
        self.assertTrue(paths.matches('x/Protocol-FREEZE.json', ['**/*freeze*.json'], 2))


if __name__ == '__main__':
    unittest.main()
