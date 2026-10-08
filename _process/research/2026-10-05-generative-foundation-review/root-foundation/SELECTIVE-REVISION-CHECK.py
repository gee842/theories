"""Bind the executed selective-revision test and its scoped research integration."""
from datetime import datetime, timezone
import csv
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
CAN = ROOT / 'theories/shengsheng-buxi-generative-existence/unified-2026-10-05'
INQ = ROOT / 'experiments/integrated-correction/general-framework/generative-basis/lean/inquiry-root'
GROUND = INQ.parent / 'universal-ethics/generative-capacity'
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
spec = importlib.util.spec_from_file_location('chain', HERE / 'build_generative_chain.py')
chain = importlib.util.module_from_spec(spec)
spec.loader.exec_module(chain)
documents = [HERE / 'SELECTIVE-REVISION-TEST.md', HERE / 'SEMANTIC-SUFFICIENCY-INTEGRATION.md',
             CAN / 'KNOWLEDGE.md', CAN / 'PHILOSOPHICAL-ACCOUNT.md', INQ / 'README.md',
             ROOT / 'sources/15-codex-theory-conversations/2026-10-08-knowledge-content-continuation.md']
errors = []
links = 0
for document in documents:
    for target in re.findall(r'\[[^\]]*\]\(([^\s)]+)\)', document.read_text()):
        if target.startswith(('https:', 'http:', 'mailto:')):
            continue
        name, _, fragment = target.partition('#')
        p = (document.parent / unquote(name)).resolve() if name else document
        links += 1
        if not p.exists():
            errors.append(f'{document.name}: missing {target}')
        elif fragment and p.suffix == '.md' and unquote(fragment) not in chain.heading_ids(p):
            errors.append(f'{document.name}: missing heading {target}')

receipt_path = INQ / 'selective-revision-verification.json'
proof = json.loads(receipt_path.read_text())
frozen = INQ / proof['retained_run']
bindings = {'passed': proof['status'] == 'passed',
            'frozen_receipt': sha(frozen / 'verification.json') == sha(receipt_path)}
for name, digest in proof['source_sha256'].items():
    current = (INQ if name in ['KnowledgeCorrespondence', 'SelectiveRevision'] else GROUND) / (name + '.lean')
    bindings['source:' + name] = sha(current) == digest
    bindings['frozen_source:' + name] = sha(frozen / (name + '.lean')) == digest
for name, digest in proof['checker_sha256'].items():
    current = (GROUND if name == 'check.py' else INQ) / name
    bindings['checker:' + name] = sha(current) == digest
for name, digest in proof['artifact_sha256'].items():
    bindings['artifact:' + name] = sha(frozen / name) == digest
if not all(bindings.values()):
    errors.append('Current or retained proof/execution binding failed')
new = next(m for m in proof['modules'] if m['module'] == 'SelectiveRevision')
if new['theorems'] != 16 or len(new['declarations']) != 32:
    errors.append('New proof count mismatch')
if not all(m['kernel_checked'] for m in proof['modules']):
    errors.append('Module not checked')
if not all(set(xs) <= {'propext'} for xs in new['axiom_dependencies'].values()):
    errors.append('Unexpected new dependency')
with (frozen / 'cases.csv').open() as f:
    rows = list(csv.DictReader(f))
contexts = {tuple(r[k] for k in ['reversed', 'first_content', 'second_content', 'first_usable', 'second_usable', 'purpose']) for r in rows}
interventions = {r['intervention'] for r in rows}
if len(rows) != 1296 or len(contexts) != 144 or len(interventions) != 9:
    errors.append('Executable case inventory mismatch')
if not all(r['conventional_equal'] == 'true' for r in rows):
    errors.append('Implementation disagreement')
if '\n> next test please\n' not in documents[-1].read_text():
    errors.append('Exact user request missing')

data = chain.read_data()
entry = next(e for s in data['sections'] for e in s['entries'] if e['id'] == 'M21')
row = next(x for x in chain.render(data).splitlines() if x.startswith('| M21 |'))
actual = next(x for x in chain.OUTPUT.read_text().splitlines() if x.startswith('| M21 |'))
versions = {}
for link in entry['links']:
    p, _ = chain.local_target(link['path'])
    name = str(p.relative_to(ROOT))
    versions[name] = data['reviewed_sources'].get(name) == sha(p)
if row != actual or not all(versions.values()):
    errors.append('Owned M21 row or reviewed versions mismatch')
edits = json.loads((HERE / 'SELECTIVE-REVISION-INDEX-EDITS.json').read_text())
if edits['entry_after'] != entry or not edits['other_generated_lines_preserved']:
    errors.append('Index edit receipt mismatch')
changes = chain.changes(data)
validation = chain.validate(data)
result = {
    'status': 'passed_scoped_documentary_and_execution_bindings' if not errors else 'failed',
    'checked_at_utc': datetime.now(timezone.utc).isoformat(), 'errors': errors,
    'local_links_checked': links,
    'document_sha256': {str(p.relative_to(ROOT)): sha(p) for p in documents},
    'checker_sha256': sha(Path(__file__)),
    'proof_receipt': str(receipt_path.relative_to(ROOT)), 'proof_receipt_sha256': sha(receipt_path),
    'execution_bindings': bindings, 'new_theorems': 16, 'new_explicit_declaration_audits': 32,
    'executed_model_cases': len(rows), 'prepared_contexts': len(contexts),
    'interventions_per_context': len(interventions), 'new_lean_compiler_run': True,
    'new_human_or_animal_experiments': 0, 'independent_agent_acceptance': False,
    'chain': {'owned_entry': 'M21', 'paired_row_matches': row == actual,
              'source_versions': versions, 'other_entries_preserved_at_edit': edits['other_entries_preserved'],
              'remaining_changes': changes, 'validation_errors': validation,
              'full_table_current': not any(changes.values()) and not validation and chain.OUTPUT.read_text() == chain.render(data)},
    'scope': 'Formal/computational realization and assessment-procedure equivalence at a common acquired-history interface. Selective revision does not uniquely identify the theory, certify warranted reliance, establish semantic sufficiency or consciousness. No wider goal completion claimed.'}
(HERE / 'SELECTIVE-REVISION-CHECKS.json').write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({k: result[k] for k in ['status', 'local_links_checked', 'new_theorems', 'executed_model_cases', 'errors']}, indent=2))
if errors:
    raise SystemExit(1)
