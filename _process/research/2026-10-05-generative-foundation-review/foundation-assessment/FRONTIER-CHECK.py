"""Check document/source integrity; this is not scientific validation.

Run from any directory with Python 3. Writes FRONTIER-INTEGRATION.json.
Shared index whole-file hashes are historical snapshots. Their exact owned
insertions must survive, while concurrent edits elsewhere are recorded.
"""
from pathlib import Path
import hashlib
import json
import re
import subprocess
import urllib.parse

A = Path(__file__).resolve().parent
R = A.parents[3]
C = R / 'theories/shengsheng-buxi-generative-existence/unified-2026-10-05'
OUT = A / 'FRONTIER-INTEGRATION.json'


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def binding(path, scope='owned_or_fixed_source'):
    raw = path.read_bytes()
    return dict(path=str(path.relative_to(R)), bytes=len(raw),
                sha256=digest(raw), scope=scope)


ed = json.loads((A / 'FRONTIER-COMPLETION-EDITS.json').read_text())
before = (R / ed['before_path']).read_text()
current = (R / ed['path']).read_text()
replay = before
for op in ed['replacements']:
    assert replay.count(op['old']) == 1
    replay = replay.replace(op['old'], op['new'], 1)
replay += ed['appended_references']
assert replay == current
assert digest(before.encode()) == ed['before_sha256']
assert digest(current.encode()) == ed['after_sha256']
names = ['Explain the common foundation', 'Ground and revise concern',
         'Compose actual mechanisms', 'Protect futures under changing circumstances',
         'Handle plural agency and authority', 'Work in learned AI and social arrangements',
         'Establish explanatory and empirical reach']


def criteria(text):
    rows = [line.split('|') for line in text.splitlines()]
    return {v[1].strip(): v[1:3] for v in rows
            if len(v) == 5 and v[1].strip() in names}


assert len(criteria(current)) == 7 and criteria(current) == criteria(before)
idx = json.loads((A / 'FRONTIER-INDEX-EDITS.json').read_text())
index_checks = []
for op in idx['edits']:
    text = (R / op['path']).read_text()
    assert text.count(op['insert']) == 1, op['path']
    whole_match = digest(text.encode()) == op['after_sha256']
    if whole_match:
        assert digest(text.replace(op['insert'], '', 1).encode()) == op['before_sha256']
    index_checks.append(dict(path=op['path'], owned_insertion_present_once=True,
                             insertion_sha256=digest(op['insert'].encode()),
                             whole_file_matches_insertion_snapshot=whole_match,
                             current_context_sha256=digest(text.encode()),
                             subsequent_context_changes_preserved=not whole_match))

files = [A / 'ALIGNMENT-FRONTIER-ASSESSMENT.md'] + sorted(A.glob('FRONTIER-*.md'))
files += [C / 'ALIGNMENT-COMPLETION.md',
          R / 'sources/36-alignment-frontier-comparators-2026-10-06/README.md',
          R / 'sources/36-relational-alignment-comparators-2026-10-06/README.md']


def anchors(path):
    found, counts = set(), {}
    for line in path.read_text().splitlines():
        match = re.match(r'^#{1,6} +(.+?)(?: +#+)?$', line)
        if not match:
            continue
        value = re.sub(r'<[^>]+>', '', match[1]).lower()
        value = re.sub(r'[^\w\- ]', '', value).replace(' ', '-')
        n = counts.get(value, 0)
        counts[value] = n + 1
        found.add(value if n == 0 else f'{value}-{n}')
    return found


seen, links, external = set(), [], set()


def check_links(text, base, origin):
    targets = re.findall(r'\]\(([^\s)]+)(?:\s+[^)]*)?\)', text)
    targets += re.findall(r'^\[[^\]]+\]:\s*(\S+)', text, re.M)
    for target in targets:
        if target.startswith(('http:', 'https:', 'mailto:', 'app:', 'codex:')):
            external.add(target)
            continue
        name, _, anchor = urllib.parse.unquote(target.strip('<>')).partition('#')
        if not name:
            continue
        path = (base / name).resolve()
        key = (str(path), anchor)
        if key in seen:
            continue
        seen.add(key)
        assert path.exists() or path == OUT, (origin, target)
        if anchor and path.suffix == '.md':
            assert anchor in anchors(path), (origin, target)
        links.append(dict(origin=origin, target=str(path.relative_to(R)), anchor=anchor or None))


for path in files:
    check_links(path.read_text(), path.parent, str(path.relative_to(R)))
for op in idx['edits']:
    check_links(op['insert'], (R / op['path']).parent, op['path'] + ' [owned insertion]')

review = (A / 'FRONTIER-INTEGRATION-REVIEW.md').read_text()
special = {
    'Sibling `root-foundation/FOUNDATION-ROOT-ACCEPTANCE.md`': A.parent / 'root-foundation/FOUNDATION-ROOT-ACCEPTANCE.md',
    'Canonical `ALIGNMENT-COMPLETION.md`': C / 'ALIGNMENT-COMPLETION.md',
}
review_count = 0
for label, sha in re.findall(r'^\| (.+?) \| `([0-9a-f]{64})` \|$', review, re.M):
    path = special.get(label, A / label.strip('`'))
    assert digest(path.read_bytes()) == sha, label
    review_count += 1
assert review_count == 10
source = R / 'sources/36-relational-alignment-comparators-2026-10-06'
manifest = json.loads((source / 'manifest.json').read_text())
for row in manifest['files']:
    raw = (source / row['path']).read_bytes()
    assert len(raw) == row['bytes'] and digest(raw) == row['sha256']
root_receipt = A.parent / 'root-foundation/FOUNDATION-ROOT-ACCEPTANCE.json'
accepted = json.loads(root_receipt.read_text())
for row in accepted['sources']:
    raw = subprocess.run(['git', 'show', row['commit'] + ':' + row['path']],
                         cwd=R, capture_output=True, check=True).stdout
    assert digest(raw) == row['sha256']
assert digest((R / accepted['root_acceptance']['path']).read_bytes()) == accepted['root_acceptance']['sha256']
subprocess.run(['git', 'diff', '--check'], cwd=R, capture_output=True, check=True)

paths = set(files + [Path(__file__), A / 'FRONTIER-COMPLETION-EDITS.json',
                    A / 'FRONTIER-INDEX-EDITS.json', A / 'FRONTIER-RELATIONAL-SOURCES.json',
                    R / ed['before_path'], root_receipt,
                    R / accepted['root_acceptance']['path'], source / 'manifest.json',
                    R / 'sources/15-codex-theory-conversations/2026-10-06-alignment-frontier-question.md',
                    R / 'sources/36-alignment-frontier-comparators-2026-10-06/READING-RECORD.json'])
paths.update(source / row['path'] for row in manifest['files'])
shared = {R / op['path'] for op in idx['edits']}
paths.update(shared)
result = dict(
    date='2026-10-06', status='targeted_comparative_checkpoint_complete',
    scientific_scope='No scientific run; checks establish document/source integrity, not novelty or alignment reliability.',
    goal_status='full_alignment_and_governance_goal_remains_active',
    named_connection='formed evaluative influence to warranted selective revision to authorized verified effects',
    previous_goal_turn='progress: inspected prior-art evidence narrowed the next research question',
    checks=dict(completion_edit_exact_reconstruction=True, unchanged_requirement_rows=7,
                unchanged_requirement_and_evidence_cells=14, owned_index_insertions=len(index_checks),
                index_contexts_changed_since_insertion=sum(not x['whole_file_matches_insertion_snapshot'] for x in index_checks),
                independent_review_bindings=review_count, local_file_anchor_pairs=len(links),
                preserved_source_package_files=len(manifest['files']),
                committed_foundation_source_bindings=len(accepted['sources']), git_diff_check='passed'),
    scope_exclusions=['No dispatch-ready trial protocol', 'No external peer review',
                      'No exhaustive priority certification', 'Goal/authority readings are link-only'],
    shared_index_checks=index_checks,
    artifacts=[binding(p, 'shared_context_snapshot_owned_fragment_checked_separately' if p in shared else 'owned_or_fixed_source') for p in sorted(paths)],
    local_links=links, foundation_accepted_committed_sources=accepted['sources'],
    external_urls_in_checked_fragments=sorted(external))
OUT.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
assert all((R / x['target']).exists() for x in links)
print(json.dumps(dict(receipt=str(OUT.relative_to(R)), sha256=digest(OUT.read_bytes()),
                      artifact_count=len(paths), checks=result['checks']), indent=2))
