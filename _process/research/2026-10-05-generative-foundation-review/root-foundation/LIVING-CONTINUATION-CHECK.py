"""Documentary checks for the continuation and new-living rival test.

No compiler rerun or new proof is claimed. The three credited predecessor runs
are checked against their retained bytes and actual compilation receipts.
"""
from datetime import datetime, timezone
import hashlib
import importlib.util
import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
CAN = ROOT / 'theories/becoming/chapters'
INQ = ROOT / 'experiments/integrated-correction/general-framework/generative-basis/lean/inquiry-root'
GROUND = INQ.parent / 'universal-ethics/generative-capacity'
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
spec = importlib.util.spec_from_file_location('chain', HERE / 'build_generative_chain.py')
chain = importlib.util.module_from_spec(spec)
spec.loader.exec_module(chain)
output = HERE / 'LIVING-CONTINUATION-CHECKS.json'
source_record = ROOT / 'sources/15-codex-theory-conversations/2026-10-08-knowledge-content-continuation.md'
documents = [HERE / 'LIVING-VALUE-SCOPE.md', HERE / 'GENERATIVE-VALUE-NECESSITY.md',
             CAN / 'KNOWLEDGE.md', CAN / 'PHILOSOPHICAL-ACCOUNT.md', source_record]
errors = []
links = 0


def check_links(document, text):
    global links
    for target in re.findall(r'\[[^\]]*\]\(([^\s)]+)\)', text):
        if target.startswith(('https:', 'http:', 'mailto:')):
            continue
        name, _, fragment = target.partition('#')
        path = (document.parent / unquote(name)).resolve() if name else document
        links += 1
        if not path.exists() and path != output:
            errors.append(f'{document.name}: missing {target}')
        elif fragment and path.suffix == '.md' and unquote(fragment) not in chain.heading_ids(path):
            errors.append(f'{document.name}: missing heading {target}')


for document in documents:
    check_links(document, document.read_text())
for document in [ROOT / 'RESEARCH.md', CAN.parent / 'README.md', HERE / 'README.md',
                 HERE / 'GENERATIVITY-CHAIN-INDEX-RECORD.md']:
    for line in document.read_text().splitlines():
        if 'LIVING-VALUE-SCOPE' in line or 'LIVING-CONTINUATION' in line:
            check_links(document, line)

inherited = {}
for name, counts in [('observational-compatibility', (8, 11)),
                     ('scientific-compatibility', (13, 18))]:
    receipt_path = INQ / (name + '-verification.json')
    proof = json.loads(receipt_path.read_text())
    frozen = INQ / proof['retained_run']
    bindings = {'passed': proof['status'] == 'passed', 'kernel_checked': proof['kernel_checked'],
                'unchanged_during_compilation': proof['source_unchanged_during_check'],
                'frozen_receipt': sha(frozen / 'verification.json') == sha(receipt_path)}
    for module, digest in proof['source_sha256'].items():
        bindings['source:' + module] = sha(INQ / (module + '.lean')) == digest
        bindings['frozen_source:' + module] = sha(frozen / (module + '.lean')) == digest
    for helper, digest in proof['checker_sha256'].items():
        bindings['checker:' + helper] = sha((GROUND if helper == 'check.py' else INQ) / helper) == digest
        bindings['frozen_checker:' + helper] = sha(frozen / helper) == digest
    for artifact, digest in proof['artifact_sha256'].items():
        bindings['artifact:' + artifact] = sha(frozen / artifact) == digest
    if not all(bindings.values()):
        errors.append(name + ': inherited byte bindings changed')
    if (proof['theorems'], len(proof['declarations'])) != counts:
        errors.append(name + ': inherited count mismatch')
    if len(proof['axiom_dependencies']) != counts[1] or any(proof['axiom_dependencies'].values()):
        errors.append(name + ': inherited dependency inventory mismatch')
    inherited[name] = {'receipt': str(receipt_path.relative_to(ROOT)),
                       'receipt_sha256': sha(receipt_path), 'bindings': bindings,
                       'theorems': counts[0], 'declaration_audits': counts[1],
                       'new_in_this_round': False, 'recompiled_in_this_round': False}

# Reuse the actually compiled practical package without claiming a new proof.
receipt_path = GROUND / 'practical-judgment-verification.json'
proof = json.loads(receipt_path.read_text())
frozen = GROUND / proof['retained_run']
module = proof['modules'][0]
bindings = {'passed': proof['status'] == 'passed',
            'kernel_checked': module['kernel_checked'],
            'unchanged_during_compilation': proof['source_unchanged_during_check'],
            'frozen_receipt': sha(frozen / 'verification.json') == sha(receipt_path)}
for name, digest in proof['source_sha256'].items():
    bindings['source:' + name] = sha(GROUND / (name + '.lean')) == digest
    bindings['frozen_source:' + name] = sha(frozen / (name + '.lean')) == digest
for helper, digest in proof['checker_sha256'].items():
    bindings['checker:' + helper] = sha(GROUND / helper) == digest
    bindings['frozen_checker:' + helper] = sha(frozen / helper) == digest
for artifact, digest in proof['artifact_sha256'].items():
    bindings['artifact:' + artifact] = sha(frozen / artifact) == digest
selected = ['no_protection_trade_by_count', 'alternative_defeats_specific_duty',
            'impossible_menu_no_duty', 'assignment_respects_capacity',
            'settlement_removes_residual']
selected_dependencies = {name: module['axiom_dependencies']['PracticalJudgment.' + name]
                         for name in selected}
if not all(bindings.values()):
    errors.append('practical-judgment: inherited byte bindings changed')
if (module['theorems'], len(module['declarations']), len(module['axiom_dependencies'])) != (30, 46, 46):
    errors.append('practical-judgment: inherited inventory mismatch')
if any(selected_dependencies.values()):
    errors.append('practical-judgment: selected dependencies changed')
inherited['practical-judgment'] = {
    'receipt': str(receipt_path.relative_to(ROOT)), 'receipt_sha256': sha(receipt_path),
    'bindings': bindings, 'package_theorems': module['theorems'],
    'package_declaration_audits': len(module['declarations']),
    'selected_prior_results': selected_dependencies,
    'complete_prior_dependency_inventory': module['axiom_dependencies'],
    'new_in_this_round': False, 'recompiled_in_this_round': False,
    'scope': 'Formal comparisons use supplied predicates and hypotheses; no proof of G0/J or life correspondence.'}

if '\n> keep pushing frontier, till you see you reach an end\n' not in source_record.read_text():
    errors.append('Exact continuation instruction missing')
text = documents[0].read_text()
for url in [
    'https://dash.harvard.edu/server/api/core/bitstreams/0328c714-7330-4a35-ab8c-d7397c3bb494/content',
    'https://dash.harvard.edu/server/api/core/bitstreams/7312037d-36cb-6bd4-e053-0100007fdf3b/content',
    'https://philosophyintrocourse.com/wp-content/uploads/2016/05/paul-taylor-the-ethics-of-respect-for-nature.pdf',
    'https://dash.harvard.edu/server/api/core/bitstreams/29042ed1-b2ef-4475-8404-a1a836a6e730/content',
    'https://academic.oup.com/monist/article/107/2/99/7629690']:
    if url not in text:
        errors.append('Primary reading locator missing: ' + url)

data = chain.read_data()
entry = next(e for section in data['sections'] for e in section['entries'] if e['id'] == 'M21')
expected = next(line for line in chain.render(data).splitlines() if line.startswith('| M21 |'))
actual = next(line for line in chain.OUTPUT.read_text().splitlines() if line.startswith('| M21 |'))
versions = {}
for link in entry['links']:
    path, _ = chain.local_target(link['path'])
    name = str(path.relative_to(ROOT))
    versions[name] = data['reviewed_sources'].get(name) == sha(path)
edits = json.loads((HERE / 'LIVING-CONTINUATION-INDEX-EDITS.json').read_text())
if expected != actual or not all(versions.values()):
    errors.append('Owned paired row or source-version mismatch')
if (edits['entry_after'] != entry or not edits['other_generated_lines_preserved']
        or not edits['discovery_inventory_preserved']
        or not all(edits['reviewed_baseline_matches'].values())):
    errors.append('Owned edit receipt mismatch')
if any(sha(ROOT / name) != digest for name, digest in edits['reviewed_sources'].items()):
    errors.append('Owned read-source receipt mismatch')
changes, validation = chain.changes(data), chain.validate(data)
result = {
    'status': 'passed_scoped_documentary_and_inherited_bindings' if not errors else 'failed',
    'checked_at_utc': datetime.now(timezone.utc).isoformat(), 'errors': errors,
    'local_links_checked': links, 'checker_sha256': sha(Path(__file__)),
    'document_sha256': {str(p.relative_to(ROOT)): sha(p) for p in documents},
    'inherited_proof_bindings': inherited, 'new_theorems': 0, 'new_empirical_experiments': 0,
    'independent_agent_acceptance': False,
    'source_assessment': 'Frick dissertation extended reading at declared pages; Finneron-Burns displayed main text I-IV; link-only access and no original-byte import. Frick 2017 body retrieval failed and is not claimed read. This checker verifies locators, not philosophical attribution or truth.',
    'chain': {'owned_entry': 'M21', 'paired_row_matches': expected == actual,
              'source_versions': versions, 'other_entries_preserved_at_edit': edits['other_entries_preserved'],
              'remaining_changes': changes, 'validation_errors': validation,
              'full_table_current': not any(changes.values()) and not validation and chain.OUTPUT.read_text() == chain.render(data)},
    'scope': 'Extended primary reading corrects the rival classification and distinguishes preservation, renewal, new living and replacement. Prior completed G0/J answers are retained. Universal necessity remains open; no new proof, empirical experiment or independent acceptance is claimed.'}
output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({k: result[k] for k in ['status', 'local_links_checked', 'new_theorems', 'errors']}, indent=2))
if errors:
    raise SystemExit(1)
