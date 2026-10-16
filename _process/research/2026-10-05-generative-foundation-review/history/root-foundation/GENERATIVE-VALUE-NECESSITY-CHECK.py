"""Check the continued necessity argument, owned index and actual Lean-run bindings."""
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
output = HERE / 'GENERATIVE-VALUE-NECESSITY-CHECKS.json'
source_record = ROOT / 'sources/15-codex-theory-conversations/2026-10-08-knowledge-content-continuation.md'
documents = [HERE / 'GENERATIVE-VALUE-NECESSITY.md',
             HERE / 'SCIENTIFIC-COMPATIBILITY-NECESSITY.md',
             CAN / 'KNOWLEDGE.md', CAN / 'PHILOSOPHICAL-ACCOUNT.md', INQ / 'README.md', source_record]
errors = []
links = 0
for document in documents:
    for target in re.findall(r'\[[^\]]*\]\(([^\s)]+)\)', document.read_text()):
        if target.startswith(('https:', 'http:', 'mailto:')):
            continue
        name, _, fragment = target.partition('#')
        path = (document.parent / unquote(name)).resolve() if name else document
        links += 1
        if not path.exists() and path != output:
            errors.append(f'{document.name}: missing {target}')
        elif fragment and path.suffix == '.md' and unquote(fragment) not in chain.heading_ids(path):
            errors.append(f'{document.name}: missing heading {target}')
# Shared indices contain unrelated research. Check this task's inserted links only.
indices = [ROOT / 'RESEARCH.md', CAN.parent / 'README.md', HERE / 'README.md',
           HERE / 'GENERATIVITY-CHAIN-INDEX-RECORD.md']
for document in indices:
    for line in document.read_text().splitlines():
        if 'GENERATIVE-VALUE-NECESSITY' not in line:
            continue
        for target in re.findall(r'\[[^\]]*\]\(([^\s)]+)\)', line):
            if target.startswith(('http:', 'https:')):
                continue
            links += 1
            if not (document.parent / unquote(target.split('#')[0])).exists() and not target.endswith(output.name):
                errors.append(f'{document.name}: missing owned link {target}')

receipt_path = INQ / 'observational-compatibility-verification.json'
proof = json.loads(receipt_path.read_text())
frozen = INQ / proof['retained_run']
bindings = {'passed': proof['status'] == 'passed', 'kernel_checked': proof['kernel_checked'],
            'unchanged_during_compilation': proof['source_unchanged_during_check'],
            'frozen_receipt': sha(frozen / 'verification.json') == sha(receipt_path)}
for name, digest in proof['source_sha256'].items():
    bindings['source:' + name] = sha(INQ / (name + '.lean')) == digest
    bindings['frozen_source:' + name] = sha(frozen / (name + '.lean')) == digest
for name, digest in proof['checker_sha256'].items():
    bindings['checker:' + name] = sha((GROUND if name == 'check.py' else INQ) / name) == digest
    bindings['frozen_checker:' + name] = sha(frozen / name) == digest
for name, digest in proof['artifact_sha256'].items():
    bindings['artifact:' + name] = sha(frozen / name) == digest
if not all(bindings.values()):
    errors.append('Proof-source or execution binding failed')
if (proof['theorems'], len(proof['declarations']), len(proof['axiom_dependencies'])) != (8, 11, 11):
    errors.append('Declared proof inventory mismatch')
if any(proof['axiom_dependencies'].values()):
    errors.append('Claimed empty proof dependency audit is not empty')
if '\n> please try to push as far as possible\n' not in source_record.read_text():
    errors.append('Exact continuation instruction missing')

data = chain.read_data()
entry = next(e for section in data['sections'] for e in section['entries'] if e['id'] == 'M21')
expected_row = next(line for line in chain.render(data).splitlines() if line.startswith('| M21 |'))
actual_row = next(line for line in chain.OUTPUT.read_text().splitlines() if line.startswith('| M21 |'))
versions = {}
for link in entry['links']:
    path, _ = chain.local_target(link['path'])
    name = str(path.relative_to(ROOT))
    versions[name] = data['reviewed_sources'].get(name) == sha(path)
edits = json.loads((HERE / 'GENERATIVE-VALUE-NECESSITY-INDEX-EDITS.json').read_text())
if expected_row != actual_row or not all(versions.values()):
    errors.append('Owned bilingual row or its source versions mismatch')
if edits['entry_after'] != entry or not edits['other_generated_lines_preserved']:
    errors.append('Owned index edit receipt mismatch')
if any(sha(ROOT / name) != digest for name, digest in edits['reviewed_sources'].items()):
    errors.append('Owned source review receipt mismatch')
changes, validation = chain.changes(data), chain.validate(data)
result = {
    'status': 'passed_scoped_documentary_and_proof_bindings' if not errors else 'failed',
    'checked_at_utc': datetime.now(timezone.utc).isoformat(), 'errors': errors,
    'local_links_checked': links, 'checker_sha256': sha(Path(__file__)),
    'document_sha256': {str(p.relative_to(ROOT)): sha(p) for p in documents},
    'proof_receipt': str(receipt_path.relative_to(ROOT)), 'proof_receipt_sha256': sha(receipt_path),
    'execution_bindings': bindings, 'new_theorems': 8, 'explicit_declaration_audits': 11,
    'empty_dependency_audits': 11, 'new_empirical_experiments': 0,
    'independent_agent_acceptance': False, 'lean_rerun_by_documentary_checker': False,
    'chain': {'owned_entry': 'M21', 'paired_row_matches': expected_row == actual_row,
              'source_versions': versions, 'other_entries_preserved_at_edit': edits['other_entries_preserved'],
              'remaining_changes': changes, 'validation_errors': validation,
              'full_table_current': not any(changes.values()) and not validation and chain.OUTPUT.read_text() == chain.render(data)},
    'scope': 'Restricted-profile compatibility and its full-package limitations are kernel checked. Basic value is distinguished from exclusive grounding; primary comparisons and the whole helping case are assessed. No proof of G0, whole-theory necessity, empirical experiment or independent-agent acceptance. Prior results retain their scopes.'}
output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({k: result[k] for k in ['status', 'local_links_checked', 'new_theorems', 'errors']}, indent=2))
if errors:
    raise SystemExit(1)
