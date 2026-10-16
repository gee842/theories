#!/usr/bin/env python3
"""Scoped documentary checks; no philosophical or mathematical certification."""
from pathlib import Path
import copy
import hashlib
import importlib.util
import json
import re

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
RECEIPT = HERE / 'GENERATIVE-FIRST-CORRECTION-EDITS.json'
REPORT = HERE / 'GENERATIVE-FIRST-CORRECTION-CHECKS.json'
sha = lambda s: hashlib.sha256(s.encode()).hexdigest()
receipt = json.loads(RECEIPT.read_text())
spec = importlib.util.spec_from_file_location('chain', HERE / 'build_generative_chain.py')
chain = importlib.util.module_from_spec(spec)
spec.loader.exec_module(chain)
errors, concurrent, checks = [], [], []
# Make the future report's local link resolvable before checking it.
if not REPORT.exists():
    REPORT.write_text('{}\n')
checked_links = 0
for record in receipt['document_edits']:
    p = ROOT / record['path']
    current = p.read_text()
    reconstructed = current
    for edit in reversed(record['edits']):
        if reconstructed.count(edit['new']) != 1:
            errors.append('Owned replacement missing or ambiguous: ' + record['path'])
            break
        reconstructed = reconstructed.replace(edit['new'], edit['old'], 1)
    else:
        if sha(reconstructed) == record['before_sha256']:
            checks.append({'path': record['path'], 'reversible_to_baseline': True})
        else:
            concurrent.append({'path': record['path'], 'note': 'Owned edits present; additional concurrent content differs from captured baseline.'})
    for edit in record['edits']:
        old_links = set(re.findall(r'\]\(([^)]+)\)', edit['old']))
        new_links = set(re.findall(r'\]\(([^)]+)\)', edit['new'])) - old_links
        for link in new_links:
            if re.match(r'\w+://', link):
                continue
            name, _, anchor = link.partition('#')
            target = (p.parent / name).resolve() if name else p
            checked_links += 1
            if not target.exists():
                errors.append(f'Missing new target: {p.relative_to(ROOT)} -> {link}')
            elif anchor and target.suffix == '.md' and anchor not in chain.heading_ids(target):
                errors.append(f'Missing new anchor: {p.relative_to(ROOT)} -> {link}')

data = chain.read_data()
entry = next(e for s in data['sections'] for e in s['entries'] if e['id'] == 'M20')
prior = json.loads((HERE / receipt['previous_wall_receipt']).read_text())
for key in ['claim_zh', 'claim_en', 'scope_zh', 'scope_en', 'connection_zh', 'connection_en']:
    old = prior['entry_after'][key][len(prior['entry_before'][key]):]
    before = receipt['entry_before'][key]
    after = receipt['entry_after'][key]
    start = before.index(old)
    suffix = before[start + len(old):]
    replacement = after[start:len(after)-len(suffix)] if suffix else after[start:]
    if replacement not in entry[key] or old in entry[key]:
        errors.append('M20 correction missing or withdrawn wall remains in ' + key)
for link in receipt['entry_after']['links'][len(receipt['entry_before']['links']):]:
    if link not in entry['links']:
        errors.append('M20 correction link missing: ' + link['path'])
    target, anchor = chain.local_target(link['path'])
    checked_links += 1
    if not target.exists() or (anchor and anchor not in chain.heading_ids(target)):
        errors.append('M20 target missing: ' + link['path'])
row = lambda text: next(l for l in text.splitlines() if l.startswith('| M20 |'))
if row(chain.OUTPUT.read_text()) != row(chain.render(data)):
    errors.append('M20 is not canonically rendered')
for path in receipt['reviewed_owned_sources']:
    if chain.digest(ROOT / path) != data['reviewed_sources'][path]:
        concurrent.append({'path': path, 'note': 'Later source version requires separate review; not refreshed by this check.'})
others = [e for s in data['sections'] for e in s['entries'] if e['id'] != 'M20']
other_rows = '\n'.join(l for l in chain.OUTPUT.read_text().splitlines() if not l.startswith('| M20 |'))
checks.append({'other_entries_match_mutation_snapshot': sha(json.dumps(others, ensure_ascii=False, sort_keys=True)) == receipt['other_entries_sha256'], 'other_rendered_lines_match_mutation_snapshot': sha(other_rows) == receipt['other_rendered_lines_sha256'], 'note': 'Differences after this mutation can be concurrent work; no other entry or rendered line was edited by this correction.'})
direction = ROOT / 'theories/becoming/chapters/ALIGNMENT-DIRECTION.md'
if chain.digest(direction) != receipt['accepted_alignment_direction_sha256']:
    errors.append('Accepted alignment direction differs from fixed fingerprint')
source = ROOT / 'sources/15-codex-theory-conversations/2026-10-08-generative-alignment-priority.md'
quote = '“认识范围扩大，不必导致机构权力扩大；它也可能要求机构收缩权力” 为什么机构必须收缩权力？你认知是不是有问题？首先考虑的是这个事情是不是好，是不是generative，不要进入西方陷阱'
if '\n> ' + quote + '\n' not in source.read_text():
    errors.append('Exact user correction missing')
report = {'scope': 'Owned documentary corrections only. Historical paragraphs explicitly superseded; no new Lean result, empirical validation, independent review or full-table freshness claim.', 'passed': not errors, 'new_local_links_checked': checked_links, 'checks': checks, 'concurrent_changes_not_certified': concurrent, 'pending_shared_reviews_not_certified': chain.changes(data), 'errors': errors}
REPORT.write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({'passed': not errors, 'new_local_links_checked': checked_links, 'document_checks': len(checks), 'concurrent_differences': len(concurrent), 'errors': errors}, ensure_ascii=False))
raise SystemExit(bool(errors))
