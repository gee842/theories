#!/usr/bin/env python3
"""Check P80's source identity and recorded counts before writing landing documents.

Usage: python3 -B verify_sources.py ROOT [--dry-run]
This verifies the actual checker evidence already present; it does not run Lean.
Marked stand-in receipts are rejected unless explicitly rehearsing with --dry-run.
"""
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import sys

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('root', type=Path)
parser.add_argument('--dry-run', action='store_true')
args = parser.parse_args()
ROOT = args.root.resolve()
HERE = Path(__file__).resolve().parent
LEAN = ROOT / 'experiments/integrated-correction/general-framework/generative-basis/lean'
CORE = LEAN / 'becoming'
source = CORE / 'Becoming/Counterfactual.lean'
packaged = HERE / 'lean/Becoming/Counterfactual.lean'
assert source.read_bytes() == packaged.read_bytes(), 'P80 source differs from the preserved package'
receipt = json.loads((CORE / 'becoming-verification.json').read_text())
periphery = json.loads((LEAN / 'universal-ethics/generative-capacity/correction-inquiry-verification.json').read_text())
assert receipt['status'] == periphery['status'] == 'passed'
for evidence in (receipt, periphery):
    synthetic = any('dry' in key.lower() or 'synthetic' in key.lower() for key in evidence)
    assert args.dry_run or not synthetic, 'stand-in receipt rejected: actual checks are required for landing'
digest = hashlib.sha256(source.read_bytes()).hexdigest()
assert digest == receipt['source_sha256']['Becoming.Counterfactual'], 'P80 core receipt is stale'
assert digest == periphery['source_sha256']['Becoming.Counterfactual'], 'P80 periphery receipt is stale'
assert receipt['core_compiles_from_prelude'], 'core prelude-only check is missing'
for evidence in (receipt, periphery):
    for module, path in evidence['source_paths'].items():
        assert hashlib.sha256((LEAN / path).read_bytes()).hexdigest() == evidence['source_sha256'][module], (
            'checked source has changed', module)
spec = importlib.util.spec_from_file_location('p80_checker', CORE / 'check_becoming.py')
checker = importlib.util.module_from_spec(spec)
spec.loader.exec_module(checker)
declarations = checker.declarations(source.read_bytes())
module = next(m for m in receipt['modules'] if m['module'] == 'Becoming.Counterfactual')
assert module['declarations'] == declarations, 'P80 recorded declarations differ from its exact source'
theorems = sum(d['kind'] == 'theorem' for d in declarations)
assert module['theorems'] == theorems == 46
assert len(declarations) == 72
assert all(not dependencies for dependencies in module['axiom_dependencies'].values())
label = 'structural dry rehearsal only; no proof evidence' if args.dry_run else 'both actual receipts current'
print(f'P80 source {digest}: {theorems} theorems, {len(declarations)} declarations; {label}')
