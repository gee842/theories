#!/bin/zsh
# E1 relanding on a fresh main (19 October 2026), from the checkout root on a branch at main's head:
# take the module and the kit from SOURCE (the E1 branch), join the module, run the core checker and connectivity,
# apply the text and records, re-point references that matched at BASE, render, re-point section 0/8 drift, render.
# The gates (check, links, test) and the commits are run after, by hand.
# usage: zsh reland.sh SOURCE_REF
set -e
SRC=$1
BASE=$(git rev-parse HEAD)
K=_process/research/2026-10-05-generative-foundation-review/root-foundation/development/e1-exchange-premises
PKG=experiments/integrated-correction/general-framework/generative-basis/lean/becoming
git checkout $SRC -- $K/lean $K/integrate.py $K/apply_text.py $K/make_records.py $K/rehash_refs.py $K/repoint_drift.py $K/study_e1.txt $K/reland.sh
E1_ROOT=$PWD python3 -B $K/integrate.py
(cd $PKG && python3 -B check_becoming.py > $OLDPWD/$K/checker-e1.log 2>&1)
python3 -c "import json;t=open('$K/checker-e1.log').read();d=json.loads(t[t.index('{'):t.rindex('}')+1]);assert d['status']=='passed'"
R=$(python3 -c "import json;print(json.load(open('$PKG/becoming-verification.json'))['retained_run'].split('/')[-1])")
MAIN=$(python3 -c "import json;print(json.load(open('$PKG/becoming-checks/$R/verification.json'))['source_commit']['main'][:9])")
echo receipt $R main $MAIN
python3 -B _process/research/2026-10-05-generative-foundation-review/root-foundation/THEOREM-CONNECTIVITY.py --check > $K/connectivity-e1.log 2>&1
python3 -B $K/apply_text.py $R $MAIN $K/connectivity-e1.log
python3 -B $K/make_records.py $R
python3 -B $K/rehash_refs.py $BASE | tail -1
python3 -B _process/research/2026-10-05-generative-foundation-review/root-foundation/THEOREM-CONNECTIVITY.py --write --check > /dev/null
render() { make research-render > $K/render-e1.log 2>&1 || true }
render
IDS=$(python3 -c "
import json;t=open('$K/render-e1.log').read();d=json.loads(t[t.index('{'):t.rindex('}')+1])
assert not d.get('errors'), d['errors']
assert all(set(x['changed_sections'])<={'## 8. Open programme','## 0. Premise card'} for x in d.get('source_drift',[])), d['source_drift']
print(' '.join(sorted({x['id'] for x in d.get('source_drift',[])})))")
[[ -n "$IDS" ]] && python3 -B $K/repoint_drift.py ${=IDS} | wc -l && render
python3 -c "
import json;t=open('$K/render-e1.log').read();d=json.loads(t[t.index('{'):t.rindex('}')+1]);print('errors',d.get('errors'),'drift',d.get('source_drift'))"
echo done
