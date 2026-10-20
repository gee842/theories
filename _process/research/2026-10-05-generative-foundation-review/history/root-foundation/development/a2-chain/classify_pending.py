#!/usr/bin/env python3
"""A2: classify the generativity chain's pending sources (fingerprint no longer matching) by
what changed since the version each fingerprint records. Read-only on the repository.

For each modified source the version its fingerprint records is found in git history
(walking `git log --follow` from the newest commit), and the net change from that version to
the working tree is classified:

- links-only: the two texts are equal once every Markdown link target `](...)` and
  `<a href="...">` target is blanked. Moves rewrite only link targets, so the change is the
  rewrite and the document's text is unchanged.
- split+links: equal, after the same blanking, to the English output of
  tools/research/split_languages.py run on the recorded version: the language separation of
  17 October 2026 with nothing else changed.
- record-bindings: a result record (JSON) whose changed top-level fields are only bindings,
  references, history, aliases, related records or text versions.
- generated: a page generated from records or data (record pages, registers); classified by
  the records it is generated from, and read through them. For a record page the changed fields
  of its record JSON since the same commit are listed (`record_fields`), and the diff is taken
  against the language separation's English output of the recorded page.
- other: anything else; the diff is written out to be read.

For every source the commits that changed it since the recorded version are listed (`commits`),
and `move_rewrites` names the move batches (_process/architecture/moves/*.json) whose recorded
rewrites take the fingerprint to the current sha256, when they do: then the whole change is the
move tool's rewriting of links and path mentions.

Usage (from the repository root):
  python3 -B classify_pending.py OUT_DIR [--matches FILE] [--only PATH ...]
writes OUT_DIR/classification.json and OUT_DIR/diffs/<n>.diff for every source not
links-only, and prints a summary. --matches reuses a file mapping each source to
{"matched": {"commit": ..., "path": ...}} (as written by a previous walk), checking each
recorded version's sha256 again before using it.
"""
import difflib
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path.cwd()
sys.path.insert(0, str(ROOT))
from tools.research import generative_chain  # noqa: E402
from tools.research.split_languages import split  # noqa: E402

LINK_TARGET = re.compile(r'\]\(([^)\n]*)\)')
HREF = re.compile(r'(<a\s[^>]*?href=)("[^"]*"|\'[^\']*\')')
RECORD_ONLY = {'references', 'proof_bindings', 'history', 'aliases', 'related', 'text_versions',
               'dependencies', 'reviewed_at_utc'}


def git(*args):
    return subprocess.run(['git', *args], capture_output=True, check=True, cwd=ROOT).stdout


def recorded_version(name, fingerprint):
    """(commit, path, bytes) of the newest version of `name` whose sha256 is `fingerprint`."""
    log = git('log', '--follow', '--name-status', '--format=@@%H', '--', name).decode()
    entries, current = [], None
    for line in log.splitlines():
        if line.startswith('@@'):
            current = {'commit': line[2:]}
            entries.append(current)
        elif line.strip() and current is not None and 'path' not in current:
            parts = line.split('\t')
            current['status'], current['path'] = parts[0], parts[-1]
    for e in entries:
        if 'path' not in e or e['status'].startswith('D'):
            continue
        try:
            blob = git('show', f"{e['commit']}:{e['path']}")
        except subprocess.CalledProcessError:
            continue
        if hashlib.sha256(blob).hexdigest() == fingerprint:
            return e['commit'], e['path'], blob
    return None, None, None


def blank_links(text):
    return HREF.sub(r'\1""', LINK_TARGET.sub('](·)', text))


def classify(name, old, new):
    if name.endswith('.json') and '/results/records/' in name:
        a, b = json.loads(old), json.loads(new)
        changed = sorted(k for k in set(a) | set(b) if a.get(k) != b.get(k))
        return ('record-bindings' if set(changed) <= RECORD_ONLY else 'other'), changed
    if not name.endswith('.md'):
        return 'other', []
    if '/results/records/' in name or name in GENERATED:
        kind = 'generated'
    else:
        kind = None
    if blank_links(old) == blank_links(new):
        return 'links-only', []
    if kind:
        return kind, []
    english = '\n'.join(split(old, Path(name).name).en)
    if blank_links(english).rstrip('\n') == blank_links(new).rstrip('\n'):
        return 'split+links', []
    zh = (ROOT / name).with_suffix('.zh.md')
    if zh.exists() and not (ROOT / name).name.endswith('.zh.md'):
        return 'split+edits', english
    return 'other', []


GENERATED = {'RESEARCH.md', 'theories/becoming/README.md', 'theories/becoming/chapters/CLAIMS.md',
             'theories/becoming/results/ROADMAP.md'}


def move_rewrites():
    """sha256 -> [(new sha256, batch)] from the rewrites every move manifest records."""
    edges = {}
    for manifest in sorted((ROOT / '_process/architecture/moves').glob('*.json')):
        data = json.loads(manifest.read_text())
        for item in data.get('rewritten', []):
            edges.setdefault(item['old_sha256'], []).append((item['new_sha256'], data['batch']))
    return edges


def rewrite_path(edges, start, goal):
    """The batches whose rewrites lead from `start` to `goal`, or None."""
    frontier, seen = [(start, [])], {start}
    while frontier:
        sha, batches = frontier.pop()
        if sha == goal:
            return batches
        for new, batch in edges.get(sha, ()):
            if new not in seen:
                seen.add(new)
                frontier.append((new, batches + [batch]))
    return None


def commits_since(commit, name):
    log = git('log', '--follow', '--format=%h %s', f'{commit}..HEAD', '--', name).decode()
    return [line[:160] for line in log.splitlines()]


def record_fields(commit, name):
    """Changed top-level fields of a record page's JSON since `commit`, or None."""
    source = name[:-3] + '.json'
    try:
        old = json.loads(git('show', f'{commit}:{source}'))
    except subprocess.CalledProcessError:
        return None
    new = json.loads((ROOT / source).read_text())
    return sorted(k for k in set(old) | set(new) if old.get(k) != new.get(k))


def main():
    out = Path(sys.argv[1])
    only = sys.argv[sys.argv.index('--only') + 1:] if '--only' in sys.argv else None
    known = json.loads(Path(sys.argv[sys.argv.index('--matches') + 1]).read_text()) if '--matches' in sys.argv else {}
    (out / 'diffs').mkdir(parents=True, exist_ok=True)
    data = generative_chain.read_data()
    pending = generative_chain.changes(data)['modified_sources']
    if only:
        pending = [p for p in pending if p in only]
    entries = {}
    for section in data['sections']:
        for entry in section['entries']:
            for link in entry['links']:
                path, _ = generative_chain.local_target(link['path'])
                entries.setdefault(str(path.relative_to(ROOT)), set()).add(entry['id'])
    edges = move_rewrites()
    result = {}
    for n, name in enumerate(pending):
        fingerprint = data['reviewed_sources'][name]
        commit = old_path = blob = None
        match = (known.get(name) or {}).get('matched')
        if match:
            blob = git('show', f"{match['commit']}:{match['path']}")
            if hashlib.sha256(blob).hexdigest() == fingerprint:
                commit, old_path = match['commit'], match['path']
            else:
                blob = None
        if blob is None:
            commit, old_path, blob = recorded_version(name, fingerprint)
        if blob is None:
            result[name] = {'kind': 'version-not-found', 'entries': sorted(entries.get(name, ()))}
            continue
        old, new = blob.decode(), (ROOT / name).read_text()
        kind, fields = classify(name, old, new)
        base, label = old, 'links blanked'
        if kind == 'split+edits':
            # What the language separation's English output does not account for: translations of
            # Chinese-only passages, pointers to the Chinese edition, relabels and other edits.
            base, fields, label = fields, [], 'split English output, links blanked'
        current = hashlib.sha256((ROOT / name).read_bytes()).hexdigest()
        item = {'kind': kind, 'recorded_commit': commit, 'recorded_path': old_path,
                'entries': sorted(entries.get(name, ())), 'changed_fields': fields,
                'move_rewrites': rewrite_path(edges, fingerprint, current),
                'commits': commits_since(commit, name)}
        if kind == 'generated' and '/results/records/' in name:
            item['record_fields'] = record_fields(commit, name)
            base = '\n'.join(split(old, Path(name).name).en) + '\n'
            label = 'split English output, links blanked'
        if kind != 'links-only':
            if kind in ('split+edits', 'other', 'generated') and name.endswith('.md'):
                a, b = blank_links(base), blank_links(new)
            else:
                a, b, label = old, new, 'raw'
            item['diff_basis'] = label
            diff = ''.join(difflib.unified_diff(a.splitlines(True), b.splitlines(True),
                                                f'{commit[:9]}:{old_path}', name, n=1))
            target = out / 'diffs' / f'{n:03d}.diff'
            target.write_text(diff)
            item['diff'] = str(target)
            item['diff_lines'] = sum(1 for line in diff.splitlines() if line[:1] in '+-')
        result[name] = item
        print(f'{n:3d} {kind:16s} {",".join(item["entries"])[:30]:30s} {name}', flush=True)
    (out / 'classification.json').write_text(json.dumps(result, ensure_ascii=False, indent=1) + '\n')
    kinds = {}
    for item in result.values():
        kinds[item['kind']] = kinds.get(item['kind'], 0) + 1
    print(json.dumps(kinds, indent=1))


if __name__ == '__main__':
    main()
