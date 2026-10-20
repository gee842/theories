#!/bin/zsh
# Z1 relanding on a fresh main (19 October 2026): from a branch at main's head with the package commit cherry-picked
# (and, if main changed the package, the core checker rerun and its receipt committed), check that the receipt binds
# the tree, run connectivity, apply the text and the record, render, re-point section 8/9 drift, render again. The
# gates (check, links, test, secrets), the board move and the commit are run after, by hand.
# usage (from the checkout root): zsh reland.sh RECEIPT BASE
set -e
R=$1; BASE=$2
K=_process/research/2026-10-05-generative-foundation-review/root-foundation/development/z1-relative-position
C=_process/research/2026-10-05-generative-foundation-review/root-foundation
PKG=experiments/integrated-correction/general-framework/generative-basis/lean/becoming
python3 - <<PY
import hashlib, json
r = json.load(open('$PKG/becoming-checks/$R/verification.json'))
bad = [m for m, p in r['source_paths'].items() if hashlib.sha256(open('$PKG/../' + p, 'rb').read()).hexdigest() != r['source_sha256'][m]]
assert not bad, bad
print('receipt binds the tree:', len(r['source_paths']), 'sources')
PY
python3 -B $C/THEOREM-CONNECTIVITY.py --check > $K/connectivity-z1.log 2>&1
N=$(python3 -B $K/apply_text.py $R $BASE $K/connectivity-z1.log)
echo "study section $N"
python3 -B $K/apply_opening.py
python3 -B $K/make_record.py $R $N
make research-render > $K/render-z1.log 2>&1 || true
IDS=$(python3 -c "
import json;t=open('$K/render-z1.log').read();d=json.loads(t[t.index('{'):t.rindex('}')+1])
assert not d.get('errors'), d['errors']
assert all(set(x['changed_sections']) <= {'## 8. Open programme', '## 9. The formal spine'} for x in d.get('source_drift',[])), d['source_drift']
print(' '.join(sorted({x['id'] for x in d.get('source_drift',[])})))")
[[ -n "$IDS" ]] && python3 -B $K/repoint_drift.py ${=IDS} && make research-render > $K/render-z1.log 2>&1
python3 -c "
import json;t=open('$K/render-z1.log').read();d=json.loads(t[t.index('{'):t.rindex('}')+1]);print('errors',d.get('errors'),'drift',d.get('source_drift'))"
echo done
