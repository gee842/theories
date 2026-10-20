#!/bin/zsh
# PE1 landing, from the worktree root, when PE1 is at the head of the queue:
#   cp land.sh <scratch>/ && zsh <scratch>/land.sh  (it resets the tree it lives in)
#            (steps 1-5: reset to main, apply the kit, checker, connectivity, text, record, render)
# Then read the render's source drift, re-point what drifts only in PE1's edits, run check/links/tests and commit.
set -e
K=_process/research/2026-10-05-generative-foundation-review/root-foundation/development/pe1-propext
P=experiments/integrated-correction/general-framework/generative-basis/lean/becoming
D=_process/research/2026-10-05-generative-foundation-review/root-foundation
WIP=pe1-wip
git reset -q --hard main
git checkout $WIP -- $K
BASE=$(git rev-parse HEAD)
python3 -B $K/integrate.py
python3 -B $K/apply_text.py
python3 -B $K/register_roots.py
(cd $P && python3 -B check_becoming.py) > $K/checker.log 2>&1
RECEIPT=$(python3 -c "import json;print(json.load(open('$P/becoming-verification.json'))['utc'])")
python3 -c "import json;d=json.load(open('$P/becoming-verification.json'));assert d['status']=='passed'"
python3 -B $D/THEOREM-CONNECTIVITY.py --check --write > $K/connectivity.log 2>&1
python3 -B $K/land_text.py $RECEIPT $K/connectivity.log $BASE | tee /dev/stderr | grep STUDY_SECTION | awk '{print $2}' > $K/.n
N=$(cat $K/.n); rm $K/.n
python3 -B $K/make_record.py $RECEIPT $N
rm -rf $P/.build   # build output; render would index it as sources
make research-render > $K/render.log 2>&1 || true
echo "receipt $RECEIPT base $BASE study $N"
