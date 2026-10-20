#!/bin/zsh
# SC landing on a fresh main (19 October 2026): from a branch at main's head with the module (Becoming/SharedCodes.lean)
# and this kit checked out from the package commit, register the module, run the core checker and the connectivity
# check, apply the text, re-point RO's passages, write the record, check RO's map, update RO's record, re-point
# references that matched at BASE, render, re-point section-4/8/9 drift, render again. The gates (strict check, links,
# secrets), the board move and the commit are run after, by hand; research-test after the commit, since its ratchet test
# reads the first record (this one, by name) from HEAD.
# usage (from the checkout root): zsh reland.sh SCRATCH_DIR BASE
set -e
L=$1; BASE=$2   # BASE: the main commit the branch starts from
K=_process/research/2026-10-05-generative-foundation-review/root-foundation/development/sc-shared-codes
PKG=experiments/integrated-correction/general-framework/generative-basis/lean/becoming
python3 -B $K/register.py
(cd $PKG && LEAN_TIMEOUT=3600 python3 -B check_becoming.py > $OLDPWD/$K/checker-sc.log 2>&1)
R=$(python3 -c "
import json;t=open('$K/checker-sc.log').read();d=json.loads(t[t.index('{'):t.rindex('}')+1]);assert d['status']=='passed'
print(json.load(open('$PKG/becoming-verification.json'))['retained_run'].rstrip('/').split('/')[-1])")
echo receipt $R
python3 -B _process/research/2026-10-05-generative-foundation-review/root-foundation/THEOREM-CONNECTIVITY.py --check > $K/connectivity-sc.log 2>&1
python3 -B $K/apply_text.py $R $BASE $K/connectivity-sc.log $K/checker-sc.log
python3 -B $K/patch_ro.py
python3 -B $K/make_record.py $R
python3 -B $K/../ro-relational-sources/verify_ro.py > $L/verify-ro.log; head -1 $L/verify-ro.log
python3 -B $K/update_ro_record.py $BASE
python3 -B $K/rehash_refs.py $BASE | tail -1
echo '.build/' > $L/sc-excludes
render() { GIT_CONFIG_COUNT=1 GIT_CONFIG_KEY_0=core.excludesFile GIT_CONFIG_VALUE_0=$L/sc-excludes make research-render > $L/render-sc.log 2>&1 || true }
render
IDS=$(python3 -c "
import json;t=open('$L/render-sc.log').read();d=json.loads(t[t.index('{'):t.rindex('}')+1])
assert not d.get('errors'), d['errors']
ok={'## 4. Collective dynamics','## 8. Open programme','## 9. The formal spine'}
bad=[x for x in d.get('source_drift',[]) if not set(x['changed_sections'])<=ok]
assert not bad, bad
print(' '.join(sorted({x['id'] for x in d.get('source_drift',[])})))")
[[ -n "$IDS" ]] && python3 -B $K/repoint_drift.py ${=IDS} | wc -l && render
python3 -c "
import json;t=open('$L/render-sc.log').read();d=json.loads(t[t.index('{'):t.rindex('}')+1]);print('errors',d.get('errors'),'drift',d.get('source_drift'))"
echo done $R
