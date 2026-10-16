#!/usr/bin/env python3
"""Read-only source/receipt and owned-document validation. Does not run Lean."""
from pathlib import Path
from urllib.parse import unquote
import hashlib
import json
import re
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
LEDGER = HERE / 'LIANGZHI-PRACTICAL-EDITS.json'
OUTPUT = HERE / 'LIANGZHI-PRACTICAL-CHECKS.json'
checks = []
link_count = 0

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def check(name, ok, detail=None):
    checks.append({'name': name, 'passed': bool(ok), 'detail': detail})

def slug(text):
    text = re.sub(r'[`*_]', '', text.lower())
    text = re.sub(r'[^\w\s-]', '', text)
    return re.sub(r'\s', '-', text.strip())

def links(path, content):
    global link_count
    for target in re.findall(r'\[[^\]\n]*\]\(([^)\n]+)\)', content):
        target = target.strip('<>')
        if re.match(r'^[a-zA-Z][\w+.-]*:', target):
            continue
        link_count += 1
        raw, _, fragment = target.partition('#')
        dest = (path.parent / unquote(raw)).resolve() if raw else path
        ok = dest.exists()
        if ok and fragment and dest.suffix == '.md':
            txt = dest.read_text()
            anchors = {slug(h) for h in re.findall(r'^#{1,6}\s+(.+)$', txt, re.M)}
            anchors.update(re.findall(r'<a\s+(?:id|name)=["\x27]([^"\x27]+)', txt))
            ok = unquote(fragment) in anchors
        check('local_link', ok, {'from': str(path.relative_to(ROOT)), 'target': target})

ledger = json.loads(LEDGER.read_text())
for row in ledger['insertions']:
    p = ROOT / row['path']
    check('owned_shared_fragment', p.read_text().count(row['text']) == 1, row['path'])
    links(p, row['text'])
for row in ledger['owned_files']:
    p = ROOT / row['path']
    check('owned_file_hash', p.exists() and sha(p) == row['sha256'], row['path'])
    if p.suffix == '.md':
        links(p, p.read_text())

p = ROOT / ledger['proof_receipt']
r = json.loads(p.read_text())
check('proof_receipt_binding', sha(p) == ledger['proof_receipt_sha256'])
check('proof_status', r['status'] == 'passed' and r['fresh_temporary_build'] and r['inputs_unchanged'])
check('compiler_binding', sha(Path(r['compiler'])) == r['compiler_sha256'])
check('proof_checker_binding', sha(p.parent / 'check.py') == r['checker_sha256'])
check('semantic_contract_binding', sha(p.parent / 'SEMANTICS.md') == r['semantic_contract_sha256'])
inherited = ROOT / 'experiments/integrated-correction/general-framework/generative-basis/noninstrumental-concern/purpose-verification.json'
check('inherited_receipt_binding', sha(inherited) == r['inherited_receipt_sha256'])
total = 0
new = {}
for m in r['modules']:
    check('module_status', m['passed'] and m['exit_code'] == 0, m['module'])
    check('source_binding', sha(ROOT / m['source']) == m['sha256'], m['source'])
    check('log_binding', sha(p.parent / m['log']) == m['log_sha256'], m['log'])
    total += len(m['axioms_by_declaration'])
    if m['new']:
        new.update(m['axioms_by_declaration'])
check('audit_count', total == 65 and len(new) == 20 and r['new_audits'] == 20)
source = (p.parent / 'SupportHandoff.lean').read_text()
declared = {'SupportHandoff.' + n for n in re.findall(r'^theorem\s+(\w+)', source, re.M)}
check('all_new_theorems_audited', declared == set(new))
check('only_reported_standard_dependencies', all(set(a) <= {'propext','Quot.sound'} for a in new.values()))
check('new_dependency_distribution', sum(not a for a in new.values()) == 10 and sum(set(a)=={'propext'} for a in new.values()) == 2 and sum(set(a)=={'propext','Quot.sound'} for a in new.values()) == 8)
result = {'status': 'passed' if all(c['passed'] for c in checks) else 'failed',
          'scope': 'Owned text and links; independent source/log/compiler/checker/contract bindings of the new passed Lean receipt. No second compilation or empirical run.',
          'ledger_sha256': sha(LEDGER), 'checker_sha256': sha(Path(__file__)),
          'local_links_checked': link_count, 'checks': checks}
OUTPUT.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'status':result['status'],'checks':len(checks),'local_links_checked':link_count,
                  'failures':[c for c in checks if not c['passed']]},ensure_ascii=False))
sys.exit(result['status'] != 'passed')
