#!/usr/bin/env python3
"""Check owned integration links and preserve the core/tree proof provenance."""

from datetime import datetime, timezone
from hashlib import sha256
import json
from pathlib import Path
import re
import subprocess
from urllib.parse import unquote, urlsplit

HERE = Path(__file__).resolve().parent
CORE = HERE.parent
ROOT = CORE.parents[4]
REVIEW = ROOT / '_process/research/2026-10-05-generative-foundation-review/root-foundation'
ARCHIVE = HERE / 'verification-history/2026-10-06-before-core-tree-continuation'
MANIFEST_SHA = '3f1cb5f088cfc9cdb7b92668e986a016d2bc321e9af33874fc5573fe655450ca'
SOURCE = ROOT / 'sources/15-codex-theory-conversations/2026-10-06-core-tree-nondual-continuation.md'
DESTINATION = REVIEW / 'CORE-TREE-CONTINUATION-CHECKS.json'
NEW_NAMES = {'CoreTreeRearticulation', 'GenerativeEpisode', 'GenerativeCoreTreeModel'}


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


def load(path):
    return json.loads(path.read_text())


def anchors(path):
    source = re.sub(r'```.*?```', '', path.read_text(), flags=re.S)
    result, counts = set(), {}
    for heading in re.findall(r'^#{1,6}\s+(.+?)\s*#*$', source, re.M):
        heading = re.sub(r'\[([^\]]+)\]\([^)]*\)', r'\1', heading)
        slug = re.sub(r'[^\w\- ]', '', heading.lower()).replace(' ', '-')
        count = counts.get(slug, 0)
        counts[slug] = count + 1
        result.add(slug if not count else f'{slug}-{count}')
    result.update(re.findall(r'(?:id|name)=[\"\x27]([^\"\x27]+)', source))
    return result


def main():
    errors = []
    def check(condition, message):
        if not condition:
            errors.append(message)

    if not DESTINATION.exists():
        DESTINATION.write_text('{"passed": false, "status": "pending"}\n')
    changes = load(REVIEW / 'CORE-TREE-CONTINUATION-DOC-EDITS.json')['files']
    full_docs = [SOURCE] + [REVIEW / name for name in (
        'CORE-TREE-CONTINUATION.md', 'CORE-TREE-CONTINUATION-REVIEW.md', 'CORE-TREE-SOURCE-READING.md')]
    blocks = [(ROOT / row['path'], row['inserted_markdown']) for row in changes]
    blocks += [(path, path.read_text()) for path in full_docs]
    sources_index = ROOT / 'sources/SOURCES.md'
    source_entry = next(line for line in sources_index.read_text().splitlines()
                        if line.startswith('**6 October 2026 — core/tree continuation correction:'))
    blocks.append((sources_index, source_entry))
    links = fragments = 0
    reading_sources = {}
    for path, block in blocks:
        check(block in path.read_text(), f'Owned insertion missing: {path.relative_to(ROOT)}')
        for raw in re.findall(r'\[[^\]\n]*\]\(([^)\n]+)\)', block):
            ref = urlsplit(raw.strip().strip('<>'))
            if ref.scheme or raw.startswith('//'):
                continue
            target = (path.parent / unquote(ref.path)).resolve() if ref.path else path
            links += 1
            check(target.exists(), f'Missing link: {path.relative_to(ROOT)} -> {raw}')
            if ref.fragment and target.is_file() and target.suffix == '.md':
                fragments += 1
                check(unquote(ref.fragment) in anchors(target),
                      f'Missing fragment: {path.relative_to(ROOT)} -> {raw}')
            if path.name == 'CORE-TREE-SOURCE-READING.md' and target.is_file() and (ROOT / 'sources') in target.parents:
                reading_sources[str(target.relative_to(ROOT))] = digest(target)

    exact = ('> generative core and the generative tree are non dual. a lot of your attempts are '
             'from western practices are western, which leads to wrong trajectory\n>\n'
             '> please keep this in mind, and continue')
    check(exact in SOURCE.read_text(), 'Current directive is not preserved exactly')
    # Recheck two key earlier HUMAN passages against the preserved primary chat.
    original = ROOT / 'sources/12-claude-ai-chats/2026-05-02_生生不息的出处_1bd809e5.md'
    for quote in ('结构的出现给了新的结构出现的可能性',
                  '没有其中一个是本体 - 并且这个递归，都是整体的一部分，互相交织的'):
        check(quote in original.read_text(), 'Earlier source quotation mismatch: ' + quote)

    manifest = load(ARCHIVE / 'manifest.json')
    check(digest(ARCHIVE / 'manifest.json') == MANIFEST_SHA, 'Baseline manifest changed')
    for row in manifest['files']:
        for kind in ('source', 'snapshot'):
            check(digest(ROOT / row[kind]) == row['sha256'], f'Ancestor {kind} changed: {row[kind]}')
    ancestors = {m['module']: m for m in manifest['modules']}
    receipt = load(HERE / 'core-tree-verification.json')
    check(receipt['status'] == 'passed', 'Combined Lean build did not pass')
    check(digest(HERE / 'check_core_tree.py') == receipt['checker_sha256'], 'Lean checker changed')
    check(digest(CORE / 'lean-toolchain') == receipt['toolchain_sha256'], 'Lean toolchain changed')
    check(receipt['baseline_manifest_sha256'] == MANIFEST_SHA, 'Receipt baseline mismatch')
    new_audits = {}
    for module in receipt['modules']:
        name = module['module']
        check(digest(ROOT / module['source']) == module['source_sha256'], f'Lean source changed: {name}')
        check(digest(HERE / module['output']) == module['output_sha256'], f'Lean output changed: {name}')
        check(module['passed'] and module['exit_code'] == 0, f'Lean module failed: {name}')
        if name in NEW_NAMES:
            new_audits.update(module['audits'])
            check(all(not deps for deps in module['audits'].values()), f'New dependency: {name}')
        else:
            check(module['audits'] == ancestors[name]['audits'], f'Ancestor audit changed: {name}')
    check(len(receipt['modules']) == 31 and receipt['audits'] == 400, 'Combined count mismatch')
    check(len(ancestors) == 28 and len(new_audits) == 11, 'New/ancestor count mismatch')
    check(receipt['new_axiom_dependencies'] == [], 'New axiom summary mismatch')

    v73 = load(REVIEW / 'V73-INTEGRATION-CHECKS.json')['source_sha256']
    for path, expected in v73.items():
        check(digest(ROOT / path) == expected, f'Preserved V7.3 source changed: {path}')
    files = {path for path, _ in blocks}
    diff = subprocess.run(['git', 'diff', '--check', '--', *[str(p.relative_to(ROOT)) for p in files]],
                          cwd=ROOT, text=True, capture_output=True)
    check(diff.returncode == 0, 'Whitespace check failed: ' + diff.stdout + diff.stderr)
    result = dict(checked_at_utc=datetime.now(timezone.utc).isoformat(),
                  scope='Owned document insertions and four full new documents; current proof/source/archive reconciliation. No scientific or Lean rerun and no claim to audit unrelated concurrent edits.',
                  documents_touched=len(files), owned_blocks_checked=len(blocks),
                  local_links_checked=links, fragments_checked=fragments,
                  exact_user_directive_preserved=True, prior_primary_quote_fragments_checked=2,
                  reading_source_sha256=reading_sources,
                  archived_and_current_ancestor_files=len(manifest['files']),
                  inherited_modules_checked=len(ancestors), combined_modules=31,
                  combined_audits=400, new_empty_dependency_audits=len(new_audits),
                  v73_original_hashes_checked=len(v73),
                  proof_receipt_sha256=digest(HERE / 'core-tree-verification.json'),
                  checker_sha256=digest(Path(__file__)),
                  documents_sha256={str(p.relative_to(ROOT)): digest(p) for p in sorted(files)},
                  errors=errors, passed=not errors)
    DESTINATION.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({k: result[k] for k in ('documents_touched', 'owned_blocks_checked',
                                           'local_links_checked', 'fragments_checked',
                                           'new_empty_dependency_audits', 'errors', 'passed')}, indent=2))
    if errors:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
