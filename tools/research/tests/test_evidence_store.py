"""The content-addressed evidence store: plan, pack (dry run, apply, resume), restore, verify.
Runs in scratch git repositories; nothing in this checkout is changed."""
import hashlib
import json
import os
from pathlib import Path
import subprocess
import tempfile
import unittest

from tools.research import evidence_store as ev

RUNS = ['20261001T000001.000001Z', '20261001T000002.000002Z', '20261001T000003.000003Z',
        '20261001T000004.000004Z', '20261001T000005.000005Z']
LEAN = 'import Std\ntheorem t : True := trivial\n'


def sha(data):
    return hashlib.sha256(data).hexdigest()


class Args:
    def __init__(self, **kw):
        self.repo = None
        self.exclude = None
        self.keep_run = None
        self.bare = 'whole'
        self.mentions_file = None
        self.no_mentions = False
        self.no_git = False
        self.__dict__.update(kw)


class StoreTests(unittest.TestCase):
    def setUp(self):
        self.dir = tempfile.TemporaryDirectory()
        self.repo = Path(self.dir.name).resolve()
        self.root = self.repo / 'lean' / 'becoming-checks'
        self.git('init', '-q')
        self.git('config', 'user.email', 't@t')
        self.git('config', 'user.name', 't')
        # runs 1-2 pass, run 3 fails, run 4 passes, run 5 (latest) passes
        statuses = ['passed', 'passed', 'failed', 'passed', 'passed']
        self.contents = {}
        for i, (run, status) in enumerate(zip(RUNS, statuses)):
            files = {'Becoming.A.lean': LEAN.encode(), 'Becoming.B.lean': f'-- run {i // 2}\n'.encode(),
                     'Becoming.A.log': b'', 'Becoming.B.log': b'', 'check.py': b'print(1)\n',
                     'unique.log': f'only in {run}\n'.encode()}
            if i == 3:
                files['Becoming.C.lean'] = b'-- cited\n'
            artifact = {n: sha(d) for n, d in files.items() if n.endswith('.lean')}
            receipt = {'status': status, 'retained_run': f'becoming-checks/{run}', 'artifact_sha256': artifact}
            run_dir = self.root / run
            run_dir.mkdir(parents=True)
            for name, data in files.items():
                (run_dir / name).write_bytes(data)
            (run_dir / 'check.py').chmod(0o755)
            (run_dir / 'verification.json').write_text(json.dumps(receipt))
            self.contents[run] = {**files, 'verification.json': json.dumps(receipt).encode()}
        (self.repo / 'README.md').write_text('See becoming-checks/%s/Becoming.C.lean and the receipt %s/verification.json.\n'
                                              % (RUNS[3], RUNS[0]))
        (self.repo / 'NOTES.md').write_text('Rebound at run %s.\n' % RUNS[1])
        (self.repo / 'records').mkdir()
        self.git('add', '.')
        self.git('commit', '-qm', 'runs')

    def tearDown(self):
        self.dir.cleanup()

    def git(self, *args):
        return subprocess.run(['git', *args], cwd=self.repo, check=True, capture_output=True, text=True).stdout

    def tracked(self):
        return set(self.git('ls-files').split('\n')) - {''}

    def args(self, **kw):
        return Args(root=str(self.root), repo=str(self.repo), **kw)

    def snapshot(self, base):
        return {p.relative_to(base).as_posix(): p.read_bytes() for p in sorted(Path(base).rglob('*')) if p.is_file()}

    def pack(self, **kw):
        args = self.args(apply=True, ops_out=None, **kw)
        import io
        import contextlib
        with contextlib.redirect_stdout(io.StringIO()):
            return ev.cmd_pack(args)

    # -------------------------------------------------------------- retention

    def test_retention_reasons(self):
        runs = ev.list_runs(self.root)
        mentions = ev.scan_mentions(self.root, runs, self.repo)
        keep = ev.retention(self.root, runs, mentions, keep_runs=(), bare='whole')
        self.assertEqual(keep[RUNS[4]]['whole'], ['latest passed run'])
        self.assertTrue(keep[RUNS[1]]['whole'])  # bare stamp in NOTES.md
        self.assertFalse(keep[RUNS[2]]['whole'])
        self.assertEqual(list(keep[RUNS[3]]['files']), ['Becoming.C.lean', 'verification.json'])
        keep = ev.retention(self.root, runs, mentions, keep_runs=(), bare='receipt')
        self.assertFalse(keep[RUNS[1]]['whole'])
        keep = ev.retention(self.root, runs, mentions, keep_runs=(RUNS[0][:15],), bare='receipt')
        self.assertTrue(keep[RUNS[0]]['whole'])

    def test_record_reference_keeps_the_run_whole_in_receipt_mode(self):
        (self.repo / 'records' / 'x.json').write_text('{}')  # not under results/records: prose only
        rec = self.repo / 'theories' / 'results' / 'records'
        rec.mkdir(parents=True)
        (rec / 'r.json').write_text(json.dumps({'references': [f'run {RUNS[2]}'], 'history': [RUNS[0]]}))
        self.git('add', '.')
        runs = ev.list_runs(self.root)
        mentions = ev.scan_mentions(self.root, runs, self.repo)
        keep = ev.retention(self.root, runs, mentions, keep_runs=(), bare='receipt')
        self.assertTrue(keep[RUNS[2]]['whole'])
        self.assertFalse(keep[RUNS[0]]['whole'])

    def test_stamp_prefix_names_runs(self):
        (self.repo / 'P.md').write_text('seconds only: 20261001T000002\n')
        runs = ev.list_runs(self.root)
        mentions = ev.scan_mentions(self.root, runs, self.repo, no_git=True)
        self.assertIn('P.md', mentions[RUNS[1]]['bare'])
        self.assertNotIn(RUNS[0], [r for r, m in mentions.items() if 'P.md' in m['bare']])

    # -------------------------------------------------------------- plan and pack

    def test_plan_counts(self):
        root, runs, keep, work = ev.build(self.root, self.args(bare='receipt', keep_run=['none']))
        s = ev.summary(root, runs, keep, work)
        self.assertEqual(s['files'], 5 * 7 + 1)
        self.assertEqual(s['runs_kept_whole'], 1)  # the latest passed run
        self.assertEqual(s['zero_byte_files'], 8)
        # A.lean and check.py once, B.lean twice (runs 0-1 and 2-3), unique.log four times; C.lean is cited and stays
        self.assertEqual(s['unique_blobs'], 1 + 1 + 2 + 4)
        self.assertEqual(s['files_after'], s['files_kept_in_place'] + s['unique_blobs'] + s['run_indexes_added'])

    def test_dry_run_changes_nothing(self):
        before = self.snapshot(self.repo)
        import io
        import contextlib
        with contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(ev.cmd_pack(self.args(apply=False, ops_out=None)), 0)
        self.assertEqual(self.snapshot(self.repo), before)
        self.assertEqual(self.git('status', '--porcelain'), '')

    def test_pack_git_roundtrip(self):
        original = {r: self.snapshot(self.root / r) for r in RUNS}
        before = self.tracked()
        self.assertEqual(self.pack(bare='receipt', keep_run=['none']), 0)
        # tracked set: renames into _objects, deletions of duplicates, one index per packed run
        self.git('add', '-A')
        status = [l.split('\t') for l in self.git('diff', '--cached', '-M', '--name-status').split('\n') if l]
        kinds = {}
        for s in status:
            kinds[s[0][0]] = kinds.get(s[0][0], 0) + 1
        self.assertGreater(kinds.get('R', 0), 0)
        self.assertGreater(kinds.get('D', 0), 0)
        after = self.tracked()
        self.assertTrue(all(p.startswith('lean/becoming-checks/_objects/') or p.endswith('RUN-INDEX.json') for p in after - before))
        self.assertTrue(all(p.startswith('lean/becoming-checks/') for p in before - after))
        self.assertEqual(ev.verify(self.root), [])
        # receipts and the latest passed run stay whole
        for run in RUNS:
            self.assertTrue((self.root / run / 'verification.json').is_file())
        self.assertEqual(sorted(p.name for p in (self.root / RUNS[4]).iterdir()), sorted(original[RUNS[4]]))
        # every run restores byte for byte, with modes
        for run in RUNS:
            out = Path(self.dir.name) / 'restored' / run
            if (self.root / run / ev.INDEX).is_file():
                ev.restore(self.root / run, out)
                self.assertEqual(self.snapshot(out), original[run])
                self.assertEqual(oct(os.stat(out / 'check.py').st_mode & 0o777), '0o755')
        self.assertFalse((self.root / RUNS[4] / ev.INDEX).exists())

    def test_cited_file_stays_and_the_rest_packs(self):
        self.pack(bare='receipt', keep_run=['none'])
        run = self.root / RUNS[3]
        self.assertTrue((run / 'Becoming.C.lean').is_file())
        self.assertFalse((run / 'Becoming.A.lean').exists())
        index = ev.read_index(run)
        self.assertEqual(index['files']['Becoming.C.lean']['store'], 'run')
        self.assertEqual(index['files']['Becoming.A.log']['store'], 'empty')
        self.assertEqual(index['files']['Becoming.A.lean']['store'], 'object')
        self.assertTrue(ev.object_path(self.root, sha(LEAN.encode())).is_file())

    def test_blob_written_once(self):
        self.pack(bare='receipt', keep_run=['none'])
        blobs = [p for p in (self.root / ev.STORE).rglob('*') if p.is_file()]
        self.assertEqual(len(blobs), len({p.name for p in blobs}))
        self.assertIn(sha(LEAN.encode()), {p.name for p in blobs})
        for p in blobs:
            self.assertEqual(sha(p.read_bytes()), p.name)

    def test_pack_is_idempotent_and_resumes(self):
        original = {r: self.snapshot(self.root / r) for r in RUNS}
        root, runs, keep, work = ev.build(self.root, self.args(bare='receipt', keep_run=['none']))
        ops = ev.ops_for(root, runs, work)
        ev.apply_ops(root, runs, work, ops[:len(ops) // 2], use_git=True)  # interrupted half way
        self.assertEqual(self.pack(bare='receipt', keep_run=['none']), 0)
        self.assertEqual(self.pack(bare='receipt', keep_run=['none']), 0)  # nothing left to do
        self.assertEqual(ev.verify(self.root), [])
        root, runs, keep, work = ev.build(self.root, self.args(bare='receipt', keep_run=['none']))
        self.assertEqual(ev.ops_for(root, runs, work), [])
        for run in RUNS:
            if (self.root / run / ev.INDEX).is_file():
                out = Path(self.dir.name) / 'again' / run
                ev.restore(self.root / run, out)
                self.assertEqual(self.snapshot(out), original[run])

    def test_non_git_mode(self):
        plain = Path(tempfile.mkdtemp(dir=self.dir.name))
        copy = plain / 'checks'
        subprocess.run(['cp', '-Rp', str(self.root), str(copy)], check=True)
        original = {r: self.snapshot(copy / r) for r in RUNS}
        args = Args(root=str(copy), repo=str(self.repo), no_git=True, apply=True, ops_out=None, bare='receipt', keep_run=['none'])
        import io
        import contextlib
        with contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(ev.cmd_pack(args), 0)
        self.assertEqual(ev.verify(copy), [])
        out = plain / 'out'
        ev.restore(copy / RUNS[0], out / RUNS[0])
        self.assertEqual(self.snapshot(out / RUNS[0]), original[RUNS[0]])
        # restore in place after deleting a working file that is kept in place
        ev.restore(copy / RUNS[0])

    # -------------------------------------------------------------- restore and verify

    def test_verify_finds_damage(self):
        self.pack(bare='receipt', keep_run=['none'])
        blob = ev.object_path(self.root, sha(LEAN.encode()))
        blob.write_text('tampered')
        errors = ev.verify(self.root)
        self.assertTrue(any('do not match their name' in e or 'size differs' in e for e in errors))
        blob.write_text(LEAN)
        self.assertEqual(ev.verify(self.root), [])
        blob.unlink()
        self.assertTrue(any('missing object' in e for e in ev.verify(self.root)))

    def test_verify_checks_receipt_artifacts(self):
        self.pack(bare='receipt', keep_run=['none'])
        path = self.root / RUNS[0] / 'verification.json'
        data = json.loads(path.read_text())
        data['artifact_sha256']['Becoming.A.lean'] = sha(b'other')
        path.write_text(json.dumps(data))
        self.assertTrue(any('receipt sha256 of Becoming.A.lean differs' in e for e in ev.verify(self.root)))

    def test_verify_flags_unindexed_and_orphans(self):
        self.pack(bare='receipt', keep_run=['none'])
        (self.root / RUNS[0] / 'stray.txt').write_text('x')
        extra = self.root / ev.STORE / 'ab'
        extra.mkdir(exist_ok=True)
        (extra / ('ab' + '0' * 62)).write_text('x')
        errors = ev.verify(self.root)
        self.assertTrue(any('not in the index' in e for e in errors))
        self.assertTrue(any('orphan object' in e for e in errors))

    def test_restore_refuses_bad_input(self):
        self.pack(bare='receipt', keep_run=['none'])
        out = Path(self.dir.name) / 'full'
        out.mkdir()
        (out / 'x').write_text('x')
        with self.assertRaises(ev.StoreError):
            ev.restore(self.root / RUNS[0], out)
        ev.object_path(self.root, sha(LEAN.encode())).write_text('tampered')
        with self.assertRaises(ev.StoreError):
            ev.restore(self.root / RUNS[0], Path(self.dir.name) / 'bad')
        with self.assertRaises(ev.StoreError):
            ev.restore(self.root / RUNS[4], Path(self.dir.name) / 'nothing')  # no index

    def test_changed_file_is_not_removed(self):
        root, runs, keep, work = ev.build(self.root, self.args(bare='receipt', keep_run=['none']))
        ops = ev.ops_for(root, runs, work)
        (self.root / RUNS[0] / 'Becoming.B.lean').write_text('edited after planning')
        with self.assertRaises(ev.StoreError):
            ev.apply_ops(root, runs, work, ops, use_git=True)
        self.assertEqual((self.root / RUNS[0] / 'Becoming.B.lean').read_text(), 'edited after planning')

    def test_mentions_file_is_written_and_reused(self):
        cache = Path(self.dir.name) / 'mentions.json'
        args = self.args(mentions_file=str(cache))
        runs = ev.list_runs(self.root)
        first = ev.load_mentions(args, self.root, runs)
        self.assertTrue(cache.is_file())
        (self.repo / 'NOTES.md').write_text('nothing\n')
        self.assertEqual(ev.load_mentions(args, self.root, runs), first)


if __name__ == '__main__':
    unittest.main()
