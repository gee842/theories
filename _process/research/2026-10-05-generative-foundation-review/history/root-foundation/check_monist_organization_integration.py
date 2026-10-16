#!/usr/bin/env python3
"""Owned document/record checks, separate from the saved Lean kernel receipt."""
from pathlib import Path
import hashlib
import importlib.util
import json
import re
import subprocess

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
sha = lambda b: hashlib.sha256(b).hexdigest()
receipt = json.loads((HERE / 'MONIST-ORGANIZATION-INDEX-EDITS.json').read_text())
report_path = HERE / 'MONIST-ORGANIZATION-CHECKS.json'
if not report_path.exists():
    report_path.write_text('{}\n')
spec = importlib.util.spec_from_file_location('chain', HERE / 'build_generative_chain.py')
chain = importlib.util.module_from_spec(spec)
spec.loader.exec_module(chain)
errors, concurrent, checks = [], [], []
links = 0
for edit in receipt['documents']:
    path = ROOT / edit['path']
    current = path.read_text()
    if current.count(edit['new']) != 1:
        errors.append('Owned passage missing or ambiguous: ' + edit['path'])
        continue
    reversed_text = current.replace(edit['new'], edit['old'], 1)
    same = sha(reversed_text.encode()) == edit['before_sha256']
    checks.append({'path': edit['path'], 'owned_passage_present': True, 'reversible_to_baseline': same})
    if not same:
        concurrent.append(edit['path'])
    previous = set(re.findall(r'\]\(([^)]+)\)', edit['old']))
    for link in set(re.findall(r'\]\(([^)]+)\)', edit['new'])) - previous:
        if re.match(r'\w+://', link):
            continue
        name, _, fragment = link.partition('#')
        target = (path.parent / name).resolve() if name else path
        links += 1
        if not target.exists():
            errors.append('Missing new target: ' + link)
        elif fragment and target.suffix == '.md' and fragment not in chain.heading_ids(target):
            errors.append('Missing new anchor: ' + link)

data = chain.read_data()
entry = next(e for s in data['sections'] for e in s['entries'] if e['id'] == 'M20')
for key, addition in receipt['entry_additions'].items():
    if addition not in entry[key]:
        errors.append('Missing paired M20 addition: ' + key)
row = lambda text: next(x for x in text.splitlines() if x.startswith('| M20 |'))
if row(chain.OUTPUT.read_text()) != row(chain.render(data)):
    errors.append('M20 rendering differs')
for link in receipt['entry_after']['links'][len(receipt['entry_before']['links']):]:
    links += 1
    target, fragment = chain.local_target(link['path'])
    if link not in entry['links'] or not target.exists() or (fragment and fragment not in chain.heading_ids(target)):
        errors.append('M20 link missing: ' + link['path'])
for path in receipt['reviewed_owned_sources']:
    if sha((ROOT / path).read_bytes()) != data['reviewed_sources'][path]:
        concurrent.append(path + ' (later version needs review)')
for key in ['other_entries_preserved_at_write','other_rendered_lines_preserved_at_write','discovery_inventory_preserved']:
    if receipt[key] is not True:
        errors.append('Preservation failure: ' + key)
record = json.loads((ROOT / receipt['record']).read_text())
for ref in record['references']:
    if sha((ROOT / ref['path']).read_bytes()) != ref['sha256']:
        errors.append('Owned result source drift: ' + ref['path'])
proof = ROOT / 'experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity'
lean = json.loads((proof / 'relational-organization-verification.json').read_text())
for module, fingerprint in lean['source_sha256'].items():
    if sha((proof / (module + '.lean')).read_bytes()) != fingerprint:
        errors.append('Lean receipt source mismatch: ' + module)
if lean['status'] != 'passed':
    errors.append('Lean run not successful')
new = next(x for x in lean['modules'] if x['module'] == 'RelationalOrganization')
if new['theorems'] != 13 or len(new['declarations']) != 29:
    errors.append('Wrong recorded declaration counts')
direction = ROOT / 'theories/becoming/chapters/ALIGNMENT-DIRECTION.md'
if sha(direction.read_bytes()) != receipt['accepted_alignment_direction_sha256']:
    errors.append('Accepted alignment direction fingerprint changed')
source = ROOT / 'sources/15-codex-theory-conversations/2026-10-08-generative-alignment-priority.md'
if '\n> 请从一元角度切入，证明，直到你hit a wall\n' not in source.read_text():
    errors.append('Exact source instruction missing')
registry = subprocess.run(['python3',str(HERE/'build_result_registry.py'),'--ids',record['id'],'--check'],cwd=ROOT,capture_output=True,text=True)
if registry.returncode:
    errors.append('Scoped registry check failed: ' + registry.stdout + registry.stderr)
report = {'scope':'Owned integration and current result only; no full-table freshness, new empirical validation or independent acceptance. Lean checking is separately source-bound.', 'passed':not errors,'new_local_links_checked':links,'documents':checks,'concurrent_changes_not_certified':concurrent,'scoped_registry':json.loads(registry.stdout),'pending_shared_reviews_not_certified':chain.changes(data),'new_lean_theorems':13,'new_lean_declaration_audits':29,'inherited_theorems':30,'inherited_audits':46,'errors':errors}
report_path.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'passed':not errors,'new_local_links_checked':links,'document_count':len(checks),'concurrent_changes':concurrent,'errors':errors},ensure_ascii=False))
raise SystemExit(bool(errors))
