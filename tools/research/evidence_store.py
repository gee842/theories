#!/usr/bin/env python3
"""Content-addressed store for checker run folders (RESTRUCTURE-PLAN 4.3).

A checker run folder (`<root>/<UTC stamp>/`) holds copies of sources, logs and drivers, and one
`verification.json` receipt. Most copies repeat byte for byte across runs. This tool keeps every
receipt, and every file something cites, where it is, and replaces the other files of a run by
entries in a store of byte-identical blobs:

    <root>/_objects/<sha[0:2]>/<sha256>      one file per distinct content (no suffix)
    <root>/<run>/RUN-INDEX.json              relative path -> sha256, size, mode, where it is kept

Nothing is lost: every byte stays in `_objects` (or in place), and `restore` rebuilds a run folder
exactly, checking each sha256. In a git checkout the tracked set changes only by renames into
`_objects` (the first copy of each blob, via `git mv`), by deletions of working copies that are
byte-identical to a blob already in the store, by deletions of zero-byte files (recorded in the
index only), and by one new `RUN-INDEX.json` per packed run. No command here runs `git rm`,
commits or adds anything beyond what `git mv` stages.

Retention (kept in place, whole or by file):
  * every `*.json` in a run (receipts: `verification.json`);
  * the latest run whose receipt passed, and runs named with `--keep-run` (stamp prefixes);
  * a run named by a bare stamp in a tracked file outside the root (Markdown, record, receipt,
    plain text), when `--bare whole` (default); with `--bare receipt` only a bare stamp inside a
    record's `references`, `proof_bindings` or `counterexamples` keeps the run whole, and the
    other bare stamps (history notes, validation prose) only name the receipt, which is kept;
  * a file named by path (`<stamp>/<name>`, any Markdown link or text) anywhere tracked outside
    the root, except for the receipt itself.

Readers of old run folders (checked 17 Oct 2026): `check_becoming.py` and the correspondence
checkers (`passed_receipts`) read every `*.json` under the Lean root, which are the receipts and
`RUN-INDEX.json` (never has `status: passed`); `check_becoming.py` and `scratch_build.py` skip
`*-checks` directories when indexing `.lean` modules; `lean_catalogue.py` classifies the folders
as saved copies; `research.py find` lists files that exist. None reads the other files of an old run.

Commands: plan, pack [--apply], restore, verify. See --help of each.
"""
import argparse
import hashlib
import json
import os
import re
import shutil
import stat
import subprocess
import sys
import tempfile
from pathlib import Path

STORE = '_objects'
INDEX = 'RUN-INDEX.json'
FORMAT = 'becoming-evidence-run-index/1'
RUN_RE = re.compile(r'^\d{8}T\d{6}\.\d+Z$')
STAMP = r'[0-9]{8}T[0-9]{6}(\.[0-9]+Z?)?(/[A-Za-z0-9_.+-]*[A-Za-z0-9_+-])?'
STAMP_RE = re.compile(STAMP)
NAMED_FIELDS = ('references', 'proof_bindings', 'counterexamples')
DEFAULT_KEEP = ('20261016T121942', '20261016T124157')  # the two newest becoming runs, 17 Oct 2026
EMPTY = hashlib.sha256(b'').hexdigest()


class StoreError(Exception):
    pass


# ---------------------------------------------------------------- basics

def sha256_file(path):
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        for chunk in iter(lambda: f.read(1 << 20), b''):
            h.update(chunk)
    return h.hexdigest()


def object_path(root, sha):
    return Path(root) / STORE / sha[:2] / sha


def list_runs(root):
    root = Path(root)
    return sorted(p.name for p in root.iterdir() if p.is_dir() and RUN_RE.match(p.name))


def run_files(run_dir):
    """Relative posix paths of every file of a run (INDEX excluded), sorted. Symlinks are refused."""
    run_dir = Path(run_dir)
    found = []
    for dirpath, dirnames, names in os.walk(run_dir):
        dirnames.sort()
        for name in names:
            path = Path(dirpath) / name
            if path.is_symlink():
                raise StoreError(f'symlink in run folder: {path}')
            rel = path.relative_to(run_dir).as_posix()
            if rel != INDEX:
                found.append(rel)
    return sorted(found)


def is_receipt(rel):
    return rel.endswith('.json')


def receipt_passed(path):
    try:
        data = json.loads(Path(path).read_text(errors='replace'))
    except (OSError, ValueError):
        return False
    return isinstance(data, dict) and (data.get('status') == 'passed' or data.get('passed') is True)


def mode_of(path):
    return format(stat.S_IMODE(os.stat(path).st_mode), '04o')


def dump_index(index):
    """One entry per line, so git diffs and reading stay manageable."""
    head = json.dumps({k: v for k, v in index.items() if k != 'files'}, ensure_ascii=False, sort_keys=True)
    rows = ',\n'.join(f' {json.dumps(name, ensure_ascii=False)}: {json.dumps(entry, sort_keys=True)}'
                      for name, entry in sorted(index['files'].items()))
    return head[:-1] + ',\n"files": {\n' + rows + '\n}}\n'


def read_index(run_dir):
    path = Path(run_dir) / INDEX
    if not path.is_file():
        return None
    index = json.loads(path.read_text())
    if index.get('format') != FORMAT:
        raise StoreError(f'{path}: unknown format {index.get("format")!r}')
    return index


# ---------------------------------------------------------------- git

def git_top(path):
    try:
        out = subprocess.run(['git', '-C', str(path), 'rev-parse', '--show-toplevel'], text=True,
                             stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
    except OSError:
        return None
    return Path(out.stdout.strip()).resolve() if out.returncode == 0 and out.stdout.strip() else None


def tracked_files(root):
    out = subprocess.run(['git', '-C', str(root), 'ls-files', '-z', '--', '.'], stdout=subprocess.PIPE, check=True)
    return {(Path(root).resolve() / p.decode()) for p in out.stdout.split(b'\0') if p}


def git_mv(root, src, dst, tries=5):
    import time
    for attempt in range(tries):
        out = subprocess.run(['git', '-C', str(root), 'mv', '--', str(src), str(dst)], text=True,
                             stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if out.returncode == 0:
            return
        if 'index.lock' in out.stderr and attempt + 1 < tries:
            time.sleep(1 + attempt)
            continue
        raise StoreError(f'git mv {src} {dst}: {out.stderr.strip()}')


# ---------------------------------------------------------------- mentions

def scan_mentions(root, runs, repo=None, exclude=(), no_git=False):
    """Stamps named in tracked text files outside `root`, as {run: {"bare": [files], "named": bool,
    "paths": {name: [files]}, "receipt": n}}. A stamp of 15 characters (no fraction) names every run
    with that prefix. `repo` is searched with `git grep` if it is a git checkout, else walked."""
    repo = Path(repo).resolve()
    root = Path(root).resolve()
    exclude = [str(Path(e)).strip('/') for e in exclude]
    if repo in root.parents:
        exclude.append(root.relative_to(repo).as_posix())
    hits = []  # (file, match)
    if not no_git and git_top(repo) == repo:
        cmd = ['git', '-C', str(repo), 'grep', '-I', '-o', '-n', '-z', '-E', STAMP, '--', '.']
        cmd += [f':(exclude){e}' for e in exclude]
        out = subprocess.run(cmd, stdout=subprocess.PIPE)
        if out.returncode not in (0, 1):
            raise StoreError('git grep failed')
        for line in out.stdout.split(b'\n'):
            parts = line.split(b'\0', 2)
            if len(parts) == 3:
                hits.append((parts[0].decode(errors='replace'), parts[2].decode(errors='replace')))
    else:
        for dirpath, dirnames, names in os.walk(repo):
            rel_dir = Path(dirpath).relative_to(repo).as_posix()
            dirnames[:] = [d for d in sorted(dirnames) if d != '.git' and
                           not any(((rel_dir + '/' + d) if rel_dir != '.' else d).startswith(e) for e in exclude)]
            for name in sorted(names):
                path = Path(dirpath) / name
                rel = path.relative_to(repo).as_posix()
                if path.is_symlink() or any(rel.startswith(e + '/') or rel == e for e in exclude):
                    continue
                data = path.read_bytes()
                if b'\0' in data[:8192]:
                    continue
                for m in STAMP_RE.finditer(data.decode(errors='replace')):
                    hits.append((rel, m.group(0)))
    by_run = {}
    record_bare = {}  # record file -> bare stamps inside its named fields
    named_by = {}

    def naming(stamp):
        # a stamp without the closing Z (including the 15-character form) names every run it prefixes
        if stamp not in named_by:
            named_by[stamp] = [r for r in runs if r == stamp or (not stamp.endswith('Z') and r.startswith(stamp))]
        return named_by[stamp]

    for file, match in hits:
        stamp, _, name = match.partition('/')
        for run in naming(stamp):
            entry = by_run.setdefault(run, {'bare': [], 'named': False, 'paths': {}, 'receipt': 0})
            if not name:
                if file not in entry['bare']:
                    entry['bare'].append(file)
            elif name == 'verification.json':
                entry['receipt'] += 1
            else:
                files = entry['paths'].setdefault(name, [])
                if file not in files and len(files) < 5:
                    files.append(file)
    for run, entry in by_run.items():
        for file in entry['bare']:
            if '/results/records/' in '/' + file and file.endswith('.json') and file not in record_bare:
                try:
                    data = json.loads((repo / file).read_text())
                except (OSError, ValueError):
                    data = {}
                text = ' '.join(json.dumps(data.get(k, '')) for k in NAMED_FIELDS) if isinstance(data, dict) else ''
                record_bare[file] = {m.group(0) for m in STAMP_RE.finditer(text) if not m.group(2)}
        for file in entry['bare']:
            stamps = record_bare.get(file, set())
            if any(run in naming(s.split('/')[0]) for s in stamps):
                entry['named'] = True
    return by_run


def load_mentions(args, root, runs):
    if args.mentions_file and Path(args.mentions_file).is_file():
        return json.loads(Path(args.mentions_file).read_text())
    if args.no_mentions:
        return {}
    repo = args.repo or git_top(root)
    if not repo:
        raise StoreError('no repository to search for mentions: pass --repo DIR, --mentions-file FILE or --no-mentions')
    mentions = scan_mentions(root, runs, repo, args.exclude or (), no_git=getattr(args, 'no_git', False))
    if args.mentions_file:
        Path(args.mentions_file).write_text(json.dumps(mentions, indent=1, sort_keys=True))
    return mentions


# ---------------------------------------------------------------- retention

def retention(root, runs, mentions, keep_runs=DEFAULT_KEEP, bare='whole'):
    """{run: {"whole": [reasons], "files": {rel: [reasons]}}} for every run."""
    root = Path(root)
    result = {r: {'whole': [], 'files': {}} for r in runs}
    for run in sorted(runs, reverse=True):
        if receipt_passed(root / run / 'verification.json'):
            result[run]['whole'].append('latest passed run')
            break
    for run in runs:
        for prefix in keep_runs:
            if run.startswith(prefix):
                result[run]['whole'].append(f'kept run {prefix}')
        m = mentions.get(run)
        if m:
            if m['bare'] and (bare == 'whole' or m['named']):
                why = 'named in a record reference' if m['named'] else 'bare stamp mentioned in ' + m['bare'][0]
                result[run]['whole'].append(why)
            for name, files in m['paths'].items():
                result[run]['files'].setdefault(name, []).append('path cited in ' + files[0])
        for rel in run_files(root / run):
            if is_receipt(rel):
                result[run]['files'].setdefault(rel, []).append('receipt')
    return result


# ---------------------------------------------------------------- plan / pack

def plan_run(root, run, keep):
    """Entries for a run: rel -> (sha, size, mode, where) with where in object | empty | run."""
    entries = {}
    run_dir = Path(root) / run
    for rel in run_files(run_dir):
        path = run_dir / rel
        sha = sha256_file(path)
        size = path.stat().st_size
        kept = keep['whole'] or rel in keep['files']
        where = 'run' if kept else ('empty' if size == 0 else 'object')
        entries[rel] = (sha, size, mode_of(path), where)
    return entries


def build(root, args):
    root = Path(root).resolve()
    runs = list_runs(root)
    mentions = load_mentions(args, root, runs)
    keep = retention(root, runs, mentions, tuple(args.keep_run) if args.keep_run else DEFAULT_KEEP, args.bare)
    work = {}
    for run in runs:
        index = read_index(root / run)
        if index:  # a packed or half-packed run: the index is the truth
            work[run] = {rel: (e['sha256'], e['size'], e['mode'], e['store']) for rel, e in index['files'].items()}
        else:
            work[run] = plan_run(root, run, keep[run])
    return root, runs, keep, work


def summary(root, runs, keep, work):
    files = bytes_ = 0
    blobs = {}
    kept_files = kept_bytes = empty = packed_files = dup_files = 0
    packed_runs = 0
    reasons = {}
    whole_runs = []
    for run in runs:
        if keep[run]['whole']:
            whole_runs.append(run)
        packed = False
        for rel, (sha, size, mode, where) in work[run].items():
            files += 1
            bytes_ += size
            if where == 'run':
                kept_files += 1
                kept_bytes += size
                why = keep[run]['whole'][0].split(' in ')[0] if keep[run]['whole'] else keep[run]['files'].get(rel, ['?'])[0].split(' in ')[0]
                reasons[why] = reasons.get(why, 0) + 1
            elif where == 'empty':
                empty += 1
                packed = True
            else:
                packed = True
                packed_files += 1
                if sha in blobs:
                    dup_files += 1
                else:
                    blobs[sha] = size
        packed_runs += packed
    blob_bytes = sum(blobs.values())
    after = kept_files + len(blobs) + packed_runs
    return {
        'runs': len(runs), 'files': files, 'bytes': bytes_,
        'runs_kept_whole': len(whole_runs), 'runs_packed': packed_runs,
        'files_kept_in_place': kept_files, 'bytes_kept_in_place': kept_bytes,
        'files_to_pack': packed_files + empty, 'zero_byte_files': empty,
        'unique_blobs': len(blobs), 'blob_bytes': blob_bytes,
        'duplicate_files_removed': dup_files + empty,
        'files_renamed_into_store': len(blobs),
        'run_indexes_added': packed_runs,
        'files_after': after, 'bytes_after': kept_bytes + blob_bytes,
        'tracked_change': {'renamed': len(blobs), 'deleted': dup_files + empty, 'added': packed_runs},
        'kept_reasons': reasons, 'runs_kept_whole_list': whole_runs,
    }


def ops_for(root, runs, work):
    """The operations still to do, in order. A file already moved or removed (a resumed pack) needs none."""
    ops = []
    first = {}
    root = Path(root)
    for run in runs:
        files = work[run]
        if not any(w in ('object', 'empty') for (_, _, _, w) in files.values()):
            continue
        if not (root / run / INDEX).is_file():
            ops.append({'op': 'write_index', 'run': run})
        for rel, (sha, size, mode, where) in sorted(files.items()):
            src = f'{run}/{rel}'
            if where not in ('empty', 'object') or not (root / src).exists():
                continue
            if where == 'empty':
                ops.append({'op': 'remove_empty', 'path': src})
                continue
            dst = f'{STORE}/{sha[:2]}/{sha}'
            if sha in first or object_path(root, sha).exists():
                ops.append({'op': 'remove_duplicate', 'path': src, 'object': dst, 'sha256': sha, 'size': size})
            else:
                first[sha] = src
                ops.append({'op': 'move', 'path': src, 'object': dst, 'sha256': sha, 'size': size})
    return ops


def write_index(root, run, files):
    index = {'format': FORMAT, 'run': run,
             'note': 'store: object = bytes in _objects/<sha[0:2]>/<sha256>; empty = zero bytes, nowhere stored; '
                     'run = kept in this folder. Rebuild with evidence_store.py restore.',
             'files': {rel: {'sha256': sha, 'size': size, 'mode': mode, 'store': where}
                       for rel, (sha, size, mode, where) in sorted(files.items())}}
    path = Path(root) / run / INDEX
    text = dump_index(index)
    json.loads(text)
    tmp = path.with_suffix('.tmp')
    tmp.write_text(text)
    os.replace(tmp, path)


def apply_ops(root, runs, work, ops, use_git):
    root = Path(root)
    tracked = tracked_files(root) if use_git else set()
    verified = {}

    def blob_ok(sha, size):
        if sha not in verified:
            p = object_path(root, sha)
            verified[sha] = p.is_file() and p.stat().st_size == size and sha256_file(p) == sha
        return verified[sha]

    for op in ops:
        kind = op['op']
        if kind == 'write_index':
            write_index(root, op['run'], work[op['run']])
            continue
        src = root / op['path']
        if kind == 'remove_empty':
            if src.exists():
                if src.stat().st_size != 0:
                    raise StoreError(f'not empty: {src}')
                os.remove(src)
            continue
        sha, size = op['sha256'], op['size']
        if kind == 'move':
            dst = root / op['object']
            if src.exists():
                if sha256_file(src) != sha:
                    raise StoreError(f'changed since planning: {src}')
                if dst.exists():
                    verified.pop(sha, None)
                    if not blob_ok(sha, size):
                        raise StoreError(f'blob differs from its name: {dst}')
                    os.remove(src)  # a duplicate after all (resumed run)
                else:
                    dst.parent.mkdir(parents=True, exist_ok=True)
                    if use_git and src.resolve() in tracked:
                        git_mv(root, src, dst)
                    else:
                        os.rename(src, dst)
                    verified[sha] = True
            elif not blob_ok(sha, size):
                raise StoreError(f'moved earlier but blob missing or wrong: {dst}')
        else:  # remove_duplicate
            if src.exists():
                if not blob_ok(sha, size):
                    raise StoreError(f'blob missing or wrong, not removing {src}: {op["object"]}')
                if sha256_file(src) != sha:
                    raise StoreError(f'changed since planning: {src}')
                os.remove(src)


def cmd_plan(args):
    root, runs, keep, work = build(args.root, args)
    result = summary(root, runs, keep, work)
    if args.json:
        print(json.dumps(result, indent=1))
    else:
        for k, v in result.items():
            if k == 'runs_kept_whole_list':
                print(f'{k}: ' + ', '.join(v))
            elif isinstance(v, dict):
                print(f'{k}:')
                for a, b in v.items():
                    print(f'    {a}: {b}')
            else:
                print(f'{k}: {v:,}' if isinstance(v, int) else f'{k}: {v}')
    return 0


def cmd_pack(args):
    root, runs, keep, work = build(args.root, args)
    use_git = not args.no_git and git_top(root) is not None
    ops = ops_for(root, runs, work)
    result = summary(root, runs, keep, work)
    counts = {}
    for op in ops:
        counts[op['op']] = counts.get(op['op'], 0) + 1
    if args.ops_out:
        Path(args.ops_out).write_text(json.dumps({'root': str(root), 'git': use_git, 'operations': ops}, indent=0))
    print(json.dumps({'mode': 'apply' if args.apply else 'dry run', 'git': use_git, 'operations': counts,
                      'expected': {k: result[k] for k in ('files', 'files_after', 'bytes', 'bytes_after', 'tracked_change')}}, indent=1))
    if not args.apply:
        print('dry run: nothing changed; add --apply to carry it out')
        return 0
    apply_ops(root, runs, work, ops, use_git)
    errors = verify(root)
    print(json.dumps({'applied': True, 'verify_errors': errors[:20], 'error_count': len(errors)}, indent=1))
    return 1 if errors else 0


# ---------------------------------------------------------------- restore / verify

def resolve_run(arg, root=None):
    path = Path(arg)
    if path.is_dir():
        return path.resolve()
    if root and (Path(root) / arg).is_dir():
        return (Path(root) / arg).resolve()
    raise StoreError(f'no such run folder: {arg}')


def restore(run_dir, to=None):
    run_dir = Path(run_dir)
    root = run_dir.parent
    index = read_index(run_dir)
    if index is None:
        raise StoreError(f'{run_dir} has no {INDEX}: nothing to restore')
    dest = Path(to) if to else run_dir
    if to:
        if dest.exists() and any(dest.iterdir()):
            raise StoreError(f'{dest} is not empty')
        dest.mkdir(parents=True, exist_ok=True)
    made = checked = 0
    for rel, e in sorted(index['files'].items()):
        sha, size, mode, where = e['sha256'], e['size'], e['mode'], e['store']
        target = dest / rel
        here = run_dir / rel
        if where == 'object':
            source = object_path(root, sha)
        else:
            source = here
        if target.exists():
            if sha256_file(target) != sha:
                raise StoreError(f'{target} differs from the index (sha256)')
            checked += 1
            continue
        target.parent.mkdir(parents=True, exist_ok=True)
        if where == 'empty':
            target.write_bytes(b'')
        else:
            if not source.is_file():
                raise StoreError(f'missing {source} for {rel}')
            shutil.copyfile(source, target)
        if sha256_file(target) != sha or target.stat().st_size != size:
            target.unlink()
            raise StoreError(f'{rel}: bytes differ from the index')
        os.chmod(target, int(mode, 8))
        made += 1
    return {'run': index['run'], 'restored': made, 'already_there': checked, 'to': str(dest)}


def verify(root):
    """Every index entry resolves, every receipt's artifact_sha256 resolves, objects match their names."""
    root = Path(root)
    errors = []
    store = root / STORE
    checked = {}
    names = set()

    def blob(sha, size=None):
        if sha not in checked:
            p = object_path(root, sha)
            if not p.is_file():
                checked[sha] = 'missing object ' + sha
            elif sha256_file(p) != sha:
                checked[sha] = 'object bytes do not match their name ' + sha
            else:
                checked[sha] = None
        if checked[sha] is None and size is not None and object_path(root, sha).stat().st_size != size:
            return 'object size differs from the index ' + sha
        return checked[sha]

    for run in list_runs(root):
        run_dir = root / run
        index = read_index(run_dir)
        present = set(run_files(run_dir))
        if index:
            if index.get('run') != run:
                errors.append(f'{run}: index names run {index.get("run")}')
            for rel, e in index['files'].items():
                sha, size, where = e['sha256'], e['size'], e['store']
                if where == 'object':
                    bad = blob(sha, size)
                    if bad:
                        errors.append(f'{run}/{rel}: {bad}')
                elif where == 'empty':
                    if size != 0 or sha != EMPTY:
                        errors.append(f'{run}/{rel}: marked empty but is not')
                elif where == 'run':
                    path = run_dir / rel
                    if not path.is_file():
                        errors.append(f'{run}/{rel}: kept in place but missing')
                    elif sha256_file(path) != sha:
                        errors.append(f'{run}/{rel}: kept file differs from the index')
                else:
                    errors.append(f'{run}/{rel}: unknown store {where!r}')
                if rel in present and where != 'run':
                    path = run_dir / rel
                    if sha256_file(path) != sha:
                        errors.append(f'{run}/{rel}: working copy differs from the index')
                if where == 'object':
                    names.add(sha)
            for rel in sorted(present - set(index['files'])):
                errors.append(f'{run}/{rel}: file not in the index')
        receipt = run_dir / 'verification.json'
        if receipt.is_file():
            try:
                data = json.loads(receipt.read_text())
            except ValueError:
                errors.append(f'{run}: verification.json does not parse')
                continue
            for name, sha in (data.get('artifact_sha256') or {}).items():
                if name == 'verification.json':
                    continue
                if index:
                    e = index['files'].get(name)
                    if not e:
                        errors.append(f'{run}: receipt cites {name}, not in the index')
                    elif e['sha256'] != sha:
                        errors.append(f'{run}: receipt sha256 of {name} differs from the index')
                else:
                    path = run_dir / name
                    if not path.is_file():
                        errors.append(f'{run}: receipt cites {name}, which is not there')
                    elif sha256_file(path) != sha:
                        errors.append(f'{run}: receipt sha256 of {name} differs from the file')
    if store.is_dir():
        for p in store.rglob('*'):
            if p.is_file() and p.name not in checked and p.name not in names:
                errors.append(f'orphan object (not named by any index): {p.relative_to(root)}')
    return errors


def cmd_restore(args):
    run = resolve_run(args.run, args.root)
    print(json.dumps(restore(run, args.to), indent=1))
    return 0


def cmd_verify(args):
    root = Path(args.root)
    errors = verify(root)
    runs = list_runs(root)
    indexed = sum(1 for r in runs if (root / r / INDEX).is_file())
    blobs = sum(1 for p in (root / STORE).rglob('*') if p.is_file()) if (root / STORE).is_dir() else 0
    print(json.dumps({'runs': len(runs), 'runs_indexed': indexed, 'objects': blobs,
                      'errors': errors[:50], 'error_count': len(errors)}, indent=1))
    return 1 if errors else 0


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest='command', required=True)

    def common(p):
        p.add_argument('root', help='the folder holding the run folders, e.g. .../becoming/becoming-checks')
        p.add_argument('--repo', help='checkout searched for mentions of runs (default: the git top level of ROOT)')
        p.add_argument('--exclude', action='append', help='repo-relative prefix left out of the mention search (ROOT itself always is)')
        p.add_argument('--keep-run', action='append', help='stamp prefix of a run kept whole (default: the two newest becoming runs)')
        p.add_argument('--bare', choices=('whole', 'receipt'), default='whole',
                       help='whole: a bare stamp in any tracked file keeps the run whole (default); '
                            'receipt: only a bare stamp in a record references/proof_bindings/counterexamples does')
        p.add_argument('--mentions-file', help='read the mention scan from this JSON file, or write it there if absent (the scan takes about a minute)')
        p.add_argument('--no-mentions', action='store_true', help='do not search for mentions (unsafe except in tests)')
        p.add_argument('--no-git', action='store_true', help='plain files: rename and delete without git')

    p = sub.add_parser('plan', help='counts and what is retained, changing nothing')
    common(p)
    p.add_argument('--json', action='store_true')
    p.set_defaults(fn=cmd_plan)
    p = sub.add_parser('pack', help='dry run by default; --apply moves the first copy of each blob into _objects and removes byte-identical duplicates')
    common(p)
    p.add_argument('--apply', action='store_true', help='carry the operations out')
    p.add_argument('--ops-out', help='write the operations list (JSON) here')
    p.set_defaults(fn=cmd_pack)
    p = sub.add_parser('restore', help='rebuild a run folder exactly from its RUN-INDEX.json, checking sha256')
    p.add_argument('run', help='run folder, or a stamp with --root')
    p.add_argument('--root')
    p.add_argument('--to', help='write the rebuilt folder here (a new or empty directory); default: fill in place')
    p.set_defaults(fn=cmd_restore)
    p = sub.add_parser('verify', help='every index entry and every receipt artifact resolves')
    p.add_argument('root')
    p.set_defaults(fn=cmd_verify)
    args = parser.parse_args(argv)
    try:
        return args.fn(args)
    except StoreError as e:
        print(f'error: {e}', file=sys.stderr)
        return 2


if __name__ == '__main__':
    sys.exit(main())
