#!/bin/zsh
# PT1 landing on a fresh main (19 October 2026): from a branch at main's head with the package commit's module
# cherry-picked (Becoming/PlaceTransitionNets.lean), integrate, run the core checker and the connectivity check, apply the
# text and the record, re-point references that matched at BASE, render, re-point section-8/9 drift, render again.
# The gates (check, links, test), the board move and the commit are run after, by hand.
# usage (from the checkout root): zsh reland.sh SCRATCH_DIR BASE
set -e
L=$1; BASE=$2   # BASE: the main commit the branch starts from
K=_process/research/2026-10-05-generative-foundation-review/root-foundation/development/pt1-place-transition-nets
PKG=experiments/integrated-correction/general-framework/generative-basis/lean/becoming
python3 -B $K/integrate.py
(cd $PKG && LEAN_TIMEOUT=3600 python3 -B check_becoming.py > $OLDPWD/$K/checker-pt1.log 2>&1)
R=$(python3 -c "
import json;t=open('$K/checker-pt1.log').read();d=json.loads(t[t.index('{'):t.rindex('}')+1]);assert d['status']=='passed'
print(json.load(open('$PKG/becoming-verification.json'))['retained_run'].rstrip('/').split('/')[-1])")
echo receipt $R
python3 -B _process/research/2026-10-05-generative-foundation-review/root-foundation/THEOREM-CONNECTIVITY.py --check > $K/connectivity-pt1.log 2>&1
python3 -B $K/apply_text.py $R $BASE $K/connectivity-pt1.log $K/checker-pt1.log
python3 -B $K/make_record.py $R
python3 -B $K/opening_note.py
python3 -B $K/rehash_refs.py $BASE | tail -1
echo '.build/' > $L/pt1-excludes
render() { GIT_CONFIG_COUNT=1 GIT_CONFIG_KEY_0=core.excludesFile GIT_CONFIG_VALUE_0=$L/pt1-excludes make research-render > $L/render-pt1.log 2>&1 || true }
render
IDS=$(python3 -c "
import json;t=open('$L/render-pt1.log').read();d=json.loads(t[t.index('{'):t.rindex('}')+1])
assert not d.get('errors'), d['errors']
bad=[x for x in d.get('source_drift',[]) if not set(x['changed_sections'])<={'## 8. Open programme','## 9. The formal spine'}]
assert not bad, bad
print(' '.join(sorted({x['id'] for x in d.get('source_drift',[])})))")
[[ -n "$IDS" ]] && python3 -B $K/repoint_drift.py ${=IDS} | wc -l && render
python3 -c "
import json;t=open('$L/render-pt1.log').read();d=json.loads(t[t.index('{'):t.rindex('}')+1]);print('errors',d.get('errors'),'drift',d.get('source_drift'))"
echo done $R
