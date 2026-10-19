#!/bin/zsh
# MD1 landing on a fresh main (19 October 2026): from a branch at main's head with the package commit (integrate.py)
# and the core receipt committed, check that the receipt binds the tree, run connectivity, apply the text, the opening
# note and the record, update how-much-difference-arrives, render, re-point drift, render again. The gates (check,
# links, test, secrets), the board move and the commit are run after, by hand.
# usage (from the checkout root): zsh reland.sh RECEIPT BASE
set -e
R=$1; BASE=$2
K=_process/research/2026-10-05-generative-foundation-review/root-foundation/development/md1-mutual-dependence
C=_process/research/2026-10-05-generative-foundation-review/root-foundation
PKG=experiments/integrated-correction/general-framework/generative-basis/lean/becoming
python3 - <<PY
import hashlib, json
r = json.load(open('$PKG/becoming-checks/$R/verification.json'))
bad = [m for m, p in r['source_paths'].items() if hashlib.sha256(open('$PKG/../' + p, 'rb').read()).hexdigest() != r['source_sha256'][m]]
assert not bad, bad
print('receipt binds the tree:', len(r['source_paths']), 'sources')
PY
python3 -B $C/THEOREM-CONNECTIVITY.py --check > $K/connectivity-md1.log 2>&1
N=$(python3 -B $K/apply_text.py $R $BASE $K/connectivity-md1.log)
echo "study section $N"
python3 -B $K/apply_opening.py
python3 -B $K/make_record.py $R $N
python3 -B $K/update_hmda.py
make research-render > $K/render-md1.log 2>&1 || true
python3 -c "
import json;t=open('$K/render-md1.log').read();d=json.loads(t[t.index('{'):t.rindex('}')+1])
assert not d.get('errors'), d['errors']
for x in d.get('source_drift',[]): print(x['id'], x['changed_sections'])"
echo done
