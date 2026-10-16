"""Bind the completed model-revision study to its checked sources and executions.

This verifies documentary and execution bindings; it does not rerun Lean or
establish the philosophical adequacy of the declared measurement premises.
"""
from collections import Counter
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
CAN = ROOT / 'theories/becoming/chapters'
INQ = ROOT / 'experiments/integrated-correction/general-framework/generative-basis/lean/inquiry-root'
GROUND = INQ.parent / 'universal-ethics/generative-capacity'
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
spec = importlib.util.spec_from_file_location('chain', HERE / 'build_generative_chain.py')
chain = importlib.util.module_from_spec(spec)
spec.loader.exec_module(chain)
output = HERE / 'MODEL-REVISION-CHECKS.json'
documents = [HERE / 'MODEL-REVISION-INTEGRATION.md', HERE / 'SOURCE-RELIANCE-INTEGRATION.md',
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
        # The output is created below on the initial execution, then checked on reruns.
        if not p.exists() and p != output:
            errors.append(f'{document.name}: missing {target}')
        elif fragment and p.suffix == '.md' and unquote(fragment) not in chain.heading_ids(p):
            errors.append(f'{document.name}: missing heading {target}')

receipt_path = INQ / 'model-revision-verification.json'
proof = json.loads(receipt_path.read_text())
frozen = INQ / proof['retained_run']
bindings = {'passed': proof['status'] == 'passed',
            'sources_unchanged_during_compilation': proof['source_unchanged_during_check'],
            'frozen_receipt': sha(frozen / 'verification.json') == sha(receipt_path)}
inquiry_modules = {'KnowledgeCorrespondence', 'SelectiveRevision', 'SourceReliance', 'ModelRevision'}
for name, digest in proof['source_sha256'].items():
    current = (INQ if name in inquiry_modules else GROUND) / (name + '.lean')
    bindings['source:' + name] = sha(current) == digest
    bindings['frozen_source:' + name] = sha(frozen / (name + '.lean')) == digest
for name, digest in proof['checker_sha256'].items():
    current = (GROUND if name == 'check.py' else INQ) / name
    bindings['checker:' + name] = sha(current) == digest
for name, digest in proof['artifact_sha256'].items():
    bindings['artifact:' + name] = sha(frozen / name) == digest
if not all(bindings.values()):
    errors.append('Current or retained proof/execution binding failed')
new = next(m for m in proof['modules'] if m['module'] == 'ModelRevision')
if new['theorems'] != 30 or len(new['declarations']) != 72:
    errors.append('New proof count mismatch')
if not all(m['kernel_checked'] for m in proof['modules']):
    errors.append('Module not checked')
if not all(set(xs) <= {'propext', 'Quot.sound'} for xs in new['axiom_dependencies'].values()):
    errors.append('Unexpected new dependency')
empty_audits = sum(not xs for xs in new['axiom_dependencies'].values())
if len(new['axiom_dependencies']) != 72 or empty_audits != 63:
    errors.append('Dependency audit inventory mismatch')

with (frozen / 'revision-runs.csv').open() as f:
    rows = list(csv.DictReader(f))
grammar = [r for r in rows if r['kind'] == 'generated_grammar']
covered = [r for r in grammar if int(r['budget']) > 0]
inadequate = [r for r in rows if r['kind'] == 'inadequate_grammar']
restricted = [r for r in rows if r['kind'] == 'restricted_probe_scope']
if (len(rows), len(grammar), len(covered), len(inadequate), len(restricted)) != (76, 72, 48, 3, 1):
    errors.append('Executable run inventory mismatch')
inventory = Counter((r['mechanism'], int(r['budget'])) for r in grammar)
if inventory != Counter({(str(i), b): 1 for i in range(24) for b in range(3)}):
    errors.append('Mechanism/budget grid mismatch')
if any(r['all_eight_predictions_correct'] != 'true' or r['all_eight_observed'] != 'true'
       or r['final_candidates'] != '1' or r['status'] != 'settled_on_available' for r in covered):
    errors.append('Completed covered-domain correctness failed')
if any(r['history_retained'] != 'true' for r in rows):
    errors.append('Lost earlier history')
if any(r['status'] != 'needs_probe' for r in grammar if r['budget'] == '0'):
    errors.append('Zero-budget incompletion was hidden')
if any(r['status'] != 'inadequate' or r['final_candidates'] != '0'
       for r in inadequate if int(r['budget']) > 0):
    errors.append('Insufficient-grammar rejection failed')
if any(r['status'] != 'settled_on_available' or r['all_eight_observed'] != 'false'
       or r['all_eight_predictions_correct'] != 'false' for r in restricted):
    errors.append('Restricted-scope limit was lost')
expected_cases = {'revision_runs': 76, 'generated_mechanisms': 24, 'budget_values': [0, 1, 2],
                  'completed_covered_runs': 48, 'covered_wrong_predictions': 0,
                  'inadequate_grammar_runs': 3, 'restricted_scope_runs': 1}
if any(proof['executable_cases'].get(k) != v for k, v in expected_cases.items()):
    errors.append('Compiler-run receipt disagrees with declared case counts')
if '\n> finish The next frontier\n' not in documents[-1].read_text():
    errors.append('Exact completion request missing')

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
edits = json.loads((HERE / 'MODEL-REVISION-INDEX-EDITS.json').read_text())
if edits['entry_after'] != entry or not edits['other_generated_lines_preserved']:
    errors.append('Index edit receipt mismatch')
if any(sha(ROOT / name) != digest for name, digest in edits['reviewed_sources'].items()):
    errors.append('Owned reviewed-source receipt mismatch')
changes = chain.changes(data)
validation = chain.validate(data)
result = {
    'status': 'passed_scoped_documentary_and_execution_bindings' if not errors else 'failed',
    'checked_at_utc': datetime.now(timezone.utc).isoformat(), 'errors': errors,
    'local_links_checked': links,
    'document_sha256': {str(p.relative_to(ROOT)): sha(p) for p in documents},
    'checker_sha256': sha(Path(__file__)),
    'proof_receipt': str(receipt_path.relative_to(ROOT)), 'proof_receipt_sha256': sha(receipt_path),
    'execution_bindings': bindings, 'new_theorems': 30, 'new_explicit_declaration_audits': 72,
    'empty_new_dependency_audits': empty_audits,
    'executed_revision_runs': len(rows), 'completed_covered_runs': len(covered),
    'status_counts': dict(Counter(r['status'] for r in rows)), 'all_histories_retained': True,
    'checked_lean_run_recorded': True, 'lean_rerun_by_this_documentary_check': False,
    'new_human_or_animal_experiments': 0, 'independent_agent_acceptance': False,
    'chain': {'owned_entry': 'M21', 'paired_row_matches': row == actual,
              'source_versions': versions, 'other_entries_preserved_at_edit': edits['other_entries_preserved'],
              'remaining_changes': changes, 'validation_errors': validation,
              'full_table_current': not any(changes.values()) and not validation and chain.OUTPUT.read_text() == chain.render(data)},
    'scope': 'Named model-revision frontier completed as a defended method and finite checked realization. Candidate construction, retained-history and common-omission checks, exhaustive finite correspondence and bounded renewed use are connected. Measurement, causal location, grammar, support and transfer retain explicit premises and counterexamples. No universal semantic, consciousness or whole-theory necessity completion claimed.'}
output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({k: result[k] for k in ['status', 'local_links_checked', 'new_theorems', 'executed_revision_runs', 'errors']}, indent=2))
if errors:
    raise SystemExit(1)
