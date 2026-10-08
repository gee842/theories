#!/usr/bin/env python3
"""Check this contribution's preservation, links and existing proof bindings."""
from datetime import datetime, timezone
import hashlib
import importlib.util
import json
from pathlib import Path
import re
import subprocess
import sys
from urllib.parse import unquote

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
sha = lambda b: hashlib.sha256(b).hexdigest()
pack = lambda x: json.dumps(x, ensure_ascii=False, sort_keys=True).encode()
edits = json.loads((HERE / 'SCIENTIFIC-INQUIRY-NECESSITY-EDITS.json').read_text())
errors = []
links = 0
spec = importlib.util.spec_from_file_location('chain', HERE / 'build_generative_chain.py')
chain = importlib.util.module_from_spec(spec)
spec.loader.exec_module(chain)
output = HERE / 'SCIENTIFIC-INQUIRY-NECESSITY-CHECKS.json'


def require(ok, message):
    if not ok:
        errors.append(message)


def check_links(path, text):
    global links
    for target in re.findall(r'\[[^\]]*\]\(([^\s)]+)\)', text):
        if target.startswith(('http:', 'https:', 'mailto:')):
            continue
        name, _, fragment = target.partition('#')
        destination = (path.parent / unquote(name)).resolve() if name else path
        links += 1
        require(destination.exists() or destination == output, 'Missing link: ' + target)
        if destination.exists() and fragment and destination.suffix == '.md':
            require(unquote(fragment) in chain.heading_ids(destination), 'Missing anchor: ' + target)


for name, evidence in edits['before_appends'].items():
    path = ROOT / name
    data = path.read_bytes()
    n = evidence['bytes']
    require(sha(data[:n]) == evidence['sha256'], 'Original prefix changed: ' + name)
    require(sha(data[n:]) == evidence['append_sha256'], 'Authored append changed: ' + name)
    require(sha(data) == evidence['after_sha256'], 'Reviewed version changed: ' + name)
    check_links(path, data[n:].decode())

for key, path in [('directive_register', ROOT / '_process/RESEARCH-DIRECTIVES.md'),
                  ('chain_maintenance', HERE / 'GENERATIVITY-CHAIN-INDEX-RECORD.md')]:
    e = edits[key]
    data = path.read_bytes()
    n = e.get('before_bytes', e.get('prior_bytes'))
    require(sha(data[:n]) == e.get('before_sha256', e.get('prior_sha256')),
            'Preserved prefix changed: ' + str(path))
    require(e['addition'].encode() in data[n:], 'Owned addition missing: ' + str(path))
    check_links(path, e['addition'])

receipt_path = ROOT / edits['proof_receipt']
receipt = json.loads(receipt_path.read_text())
run = ROOT / receipt['snapshot']
source = ROOT / receipt['source']
checker = source.parent / 'check_scientific_inquiry_necessity.py'
require(receipt['status'] == 'passed', 'Unsuccessful proof receipt')
require((receipt['theorems'], receipt['explicit_declaration_audits']) == (18, 27), 'Proof inventory mismatch')
require(sha(source.read_bytes()) == receipt['source_sha256'], 'Current proof drift')
require(sha((run / source.name).read_bytes()) == receipt['source_sha256'], 'Frozen proof drift')
require(sha(checker.read_bytes()) == receipt['checker_sha256'], 'Checker drift')
require(sha((run / checker.name).read_bytes()) == receipt['checker_sha256'], 'Frozen checker drift')
require((source.parent / 'scientific-inquiry-necessity-verification.json').read_bytes() == receipt_path.read_bytes(),
        'Latest receipt differs from owned frozen receipt')
for name, digest in receipt['log_sha256'].items():
    require(sha((run / name).read_bytes()) == digest, 'Proof log drift: ' + name)
require(len(receipt['dependencies']) == 27, 'Incomplete axiom inventory')
require(sum(not deps for deps in receipt['dependencies'].values()) == 11, 'Empty dependency count mismatch')
require(all(set(deps) <= {'propext', 'Quot.sound'} for deps in receipt['dependencies'].values()),
        'Unreported logical dependency')

data = chain.read_data()
entry = next(e for section in data['sections'] for e in section['entries'] if e['id'] == 'M21')
e = edits['chain']
require(sha(pack(entry)) == e['row_sha256'], 'Owned row changed after integration')
restored = json.loads(json.dumps(entry))
for key, suffix in e['append_fields'].items():
    require(restored[key].endswith(suffix), 'Missing bilingual suffix: ' + key)
    restored[key] = restored[key][:-len(suffix)]
for link in e['added_links']:
    require(link in restored['links'], 'Missing added chain link')
    if link in restored['links']:
        restored['links'].remove(link)
require(sha(pack(restored)) == e['prior_row_sha256'], 'Prior row not recoverable')
expected = next(line for line in chain.render(data).splitlines() if line.startswith('| M21 |'))
actual = next(line for line in chain.OUTPUT.read_text().splitlines() if line.startswith('| M21 |'))
require(expected == actual, 'Owned rendered row differs')
for name, digest in e['reviewed_sources'].items():
    require(sha((ROOT / name).read_bytes()) == digest, 'Owned reviewed source drift: ' + name)
    require(data['reviewed_sources'].get(name) == digest, 'Chain source binding differs: ' + name)
require(e['other_entries_preserved'] and e['other_rendered_lines_preserved'] and e['prior_discovery_preserved'],
        'Chain mutation preservation failed')

cmd = [sys.executable, '-B', 'tools/research/research.py', 'check', '--ids',
       'finite-fallible-inquiry-necessity', 'scientific-inquiry-foundation']
checked = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True, timeout=60)
registry = json.loads(checked.stdout)
require(checked.returncode == 0 and not registry['errors'] and not registry['source_drift'],
        'Scoped registry check failed')
changes, validation = chain.changes(data), chain.validate(data)
record = {
    'status': 'passed_scoped' if not errors else 'failed',
    'checked_at_utc': datetime.now(timezone.utc).isoformat(),
    'errors': errors, 'local_links_checked': links,
    'proof_receipt': edits['proof_receipt'], 'proof_receipt_sha256': sha(receipt_path.read_bytes()),
    'theorems': 18, 'declaration_audits': 27, 'empty_dependency_lists': 11,
    'standard_dependency_lists': 16, 'proof_rerun_by_this_checker': False,
    'registry': registry, 'owned_chain_row_matches': expected == actual,
    'chain_pending_changes': changes, 'chain_validation_errors': validation,
    'whole_chain_current': not any(changes.values()) and not validation,
    'new_empirical_runs': 0, 'independent_agent_review': False,
    'checker_sha256': sha(Path(__file__).read_bytes()),
    'scope': 'Own append preservation, links, canonical records and frozen Lean evidence only. '
             'The finite necessity theorem is checked; the scientific-foundation target remains open. '
             'Unrelated concurrent edits and whole-chain freshness are not certified.'
}
output.write_text(json.dumps(record, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({key: record[key] for key in ['status', 'errors', 'local_links_checked',
                                               'theorems', 'declaration_audits', 'whole_chain_current']}))
raise SystemExit(bool(errors))
