#!/usr/bin/env python3
"""Owned integrity checks; mathematical execution is recorded separately."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import subprocess
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
EXPERIMENT = ROOT/'experiments/market-generativity/meta-attractor'
OUTPUT = HERE/'META-ATTRACTOR-RECONCILIATION-CHECKS.json'


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def main():
    proof = json.loads((EXPERIMENT/'reconciliation-verification.json').read_text())
    assert proof['status'] == 'passed'
    assert {k:len(v) for k,v in proof['theorems'].items()} == {
        'LegacyReconciliation':14, 'CommonOrganization':27}
    assert len(proof['new_audits']) == 89
    assert len(proof['inherited_audits']) == 112
    for name, expected in proof['sources'].items():
        source = ROOT/proof['source_paths'][name]
        assert sha(source) == expected, source
        assert (EXPERIMENT/'reconciliation-verification'/name).read_bytes() == source.read_bytes()
    for name, expected in proof['log_hashes'].items():
        assert sha(EXPERIMENT/'reconciliation-verification'/(name+'.txt')) == expected
    assert sha(EXPERIMENT/'check_reconciliation.py') == proof['checker_sha256']
    assert sha(Path.home()/'.elan/toolchains/leanprover--lean4---v4.29.1/bin/lean') == proof['compiler_sha256']
    originals = [
        'sources/03-meta-attractor/2025-08-formal/2025-08-10-comprehensive-mathematical-definition.md',
        'sources/03-meta-attractor/2025-10-essays/meta-attractor-essay-long.md',
        'drafts/2026-10-02-iaseai-selecting-the-selectors/v7.3/THEORY.md']
    preservation = {}
    for rel in originals:
        current = (ROOT/rel).read_bytes()
        old = subprocess.run(['git','show','HEAD:'+rel],cwd=ROOT,capture_output=True)
        matches = old.stdout == current if old.returncode == 0 else None
        assert matches is not False, ('historical source differs from HEAD',rel)
        preservation[rel] = {'sha256':sha(ROOT/rel),'matches_git_head':matches,
                             'review_scope':'selected passages named in the study, not every assertion'}
    edits = json.loads((HERE/'META-ATTRACTOR-RECONCILIATION-INDEX-EDITS.json').read_text())
    for fragment in edits['shared_fragments']:
        assert fragment['insertion'] in (ROOT/fragment['path']).read_text(), fragment['path']
    result = {'status':'checking_links','checked_at_utc':datetime.now(timezone.utc).isoformat(),
              'new_theorems':41,'new_audits':89,'inherited_theorem_audits':112,
              'proof_receipt_sha256':sha(EXPERIMENT/'reconciliation-verification.json'),
              'historical_sources':preservation,'index_entry':'M24',
              'other_entries_preserved_at_edit':edits['other_entries_preserved'],
              'checker_sha256':sha(Path(__file__))}
    OUTPUT.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    subprocess.run([sys.executable,str(HERE/'META-ATTRACTOR-CHECK.py')],cwd=ROOT,check=True)
    shared = json.loads((HERE/'META-ATTRACTOR-CHECKS.json').read_text())
    result.update(status='passed',local_links=shared['local_links'],
                  pending_shared_source_reviews=shared['full_table_pending_sources'],
                  scope='Owned links, current proof/source bindings and M24 additions only; no full-table freshness, empirical validation or independent acceptance.')
    OUTPUT.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({k:result[k] for k in ['status','new_theorems','new_audits','inherited_theorem_audits','local_links']}))


if __name__ == '__main__':
    main()
