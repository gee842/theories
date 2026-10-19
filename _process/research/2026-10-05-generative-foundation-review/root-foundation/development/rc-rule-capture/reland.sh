#!/bin/zsh
# RC landing on a fresh main (19 October 2026). From the checkout root of a branch at main's head with the kit checked
# out from the RC branch: join the module, register its apart root, run the core checker, check connectivity, apply the
# text, patch RO's passage map and chapter, write the record, verify RO's map, re-point references that matched at
# BASE, render, re-point the records linked from the collective continuation row RC rewrites (repoint_drift.py checks
# that the row is the only change bearing on them), render again. The gates, the board move, the commit and the connectivity measure (--write) are run after, by hand.
# usage: zsh reland.sh BASE MODULE_SOURCE SCRATCH_DIR   (BASE: the main commit the branch starts from;
#        MODULE_SOURCE: RuleCapture.lean, e.g. from `git show claude/keen-jemison-dd6641:<package>/Becoming/RuleCapture.lean`)
set -e
BASE=$1; SRC=$2; L=$3
RF=_process/research/2026-10-05-generative-foundation-review/root-foundation
K=$RF/development/rc-rule-capture
PKG=experiments/integrated-correction/general-framework/generative-basis/lean/becoming
ROOT=$PWD
[[ "$(git rev-parse HEAD)" == "$(git rev-parse $BASE)" ]] || { echo 'HEAD is not BASE'; exit 1 }
if pgrep -f "check_becoming.py" > /dev/null; then echo 'another checker run is going; wait for it'; exit 1; fi
RC_ROOT=$PWD python3 -B $K/integrate.py $SRC
python3 -B $K/register_apart.py
(cd $PKG && python3 -B check_becoming.py > $ROOT/$K/checker-rc.log 2>&1)
R=$(python3 -c "import json; d=json.load(open('$PKG/becoming-verification.json')); assert d['status']=='passed', d['status']; print(d['utc'])")
echo "receipt $R"
python3 -B $RF/THEOREM-CONNECTIVITY.py --check > $K/connectivity-rc.log 2> $L/connectivity-rc.err
NUMS=$(python3 -B $K/apply_text.py $R $(git rev-parse --short $BASE) $K/connectivity-rc.log)
N=${NUMS% *}; D=${NUMS#* }
echo "study section $N, decision D$D"
python3 -B $K/patch_ro.py $N $D $BASE
python3 -B $K/make_record.py $R $N $D
python3 -B $K/update_goal.py
python3 -B $RF/development/ro-relational-sources/verify_ro.py > $K/verify-ro.log 2>&1
tail -3 $K/verify-ro.log
python3 -B $K/rehash_refs.py $BASE $N $D | tail -1
make research-render > $L/render-rc.log 2>&1 || true
python3 -B $K/repoint_drift.py $L/render-rc.log $BASE | tail -1
make research-render > $L/render-rc2.log 2>&1 || true
python3 - $L <<'PY'
import json, sys
L = sys.argv[1]
t = open(f'{L}/render-rc2.log').read(); d = json.loads(t[t.index('{'):t.rindex('}') + 1])
print('errors', d.get('errors'))
print('drift', json.dumps(d.get('source_drift'), ensure_ascii=False)[:3000])
PY
echo "done, receipt $R, section $N, D$D"
