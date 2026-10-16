#!/bin/zsh
# P73–P75 landing, after `root_edits.py W core` and the three checkers passed in the worktree W
# (check_becoming.py, check_correction_inquiry.py, check_learning_correspondence.py). Inventory, documents, records,
# generators and checks; commits nothing. Follows P80's land.sh.
# Usage: zsh land.sh W S PLAN_ZH_AFTER PLAN_EN_AFTER [LOGDIR]
#   S: P73's study section (the next after the last landed one); P75 takes S+1;
#   PLAN_ZH_AFTER, PLAN_EN_AFTER: prefixes of the plan's row and bullet P73's go after.
# Stops at the first failure.
set -e
W=${1:a}; S=$2; ZH=$3; EN=$4
L=${5:-$W/../p73-landing-logs}
RF=_process/research/2026-10-05-generative-foundation-review/root-foundation
K=${0:a:h}
mkdir -p $L
cd $W
test -z "$BECOMING_FRESH" || { echo "BECOMING_FRESH is set"; exit 1; }
python3 -B $K/inventory_edit.py $W edit
(cd $RF && python3 -B DECIDABILITY-INVENTORY.py > $L/inventory.log 2>&1) || { echo "inventory failed"; tail -30 $L/inventory.log; exit 1; }
tail -2 $L/inventory.log
python3 -B $K/inventory_edit.py $W zero
python3 -B $K/apply_docs.py $W $S "$ZH" "$EN"
python3 -B $K/make_records.py $W $(date -u +%Y-%m-%dT%H:%M:%S+00:00) $S
python3 -B $K/repoint.py $W HEAD | tail -3
python3 -B $K/root_edits.py $W readmes
python3 -B $K/reading_entries.py $W
python3 -B tools/research/reading_catalogue.py > $L/catalogue_gen.log 2>&1
python3 -B tools/research/lean_catalogue.py > $L/lean_gen.log 2>&1
python3 -B tools/research/research.py render > $L/render.log 2>&1 || { echo "render failed"; tail -30 $L/render.log; exit 1; }
python3 -B tools/research/session_map.py --capture > $L/capture.log 2>&1
python3 -B $K/repoint.py $W HEAD | tail -2
python3 -B tools/research/research.py render > $L/render2.log 2>&1 || { echo "render failed"; tail -30 $L/render2.log; exit 1; }
python3 -B tools/research/research.py check > $L/check.log 2>&1 || { echo "research check failed"; tail -40 $L/check.log; exit 1; }
python3 -B tools/research/lean_catalogue.py --check > $L/lean_check.log 2>&1 || { echo "lean catalogue check failed"; tail -5 $L/lean_check.log; exit 1; }
python3 -B tools/research/reading_catalogue.py --check > $L/catalogue_check.log 2>&1 || { echo "reading catalogue check failed"; tail -5 $L/catalogue_check.log; exit 1; }
python3 -B tools/research/session_map.py --check > $L/session_check.log 2>&1 || { echo "session map check failed"; tail -5 $L/session_check.log; exit 1; }
python3 -B tools/research/generative_chain.py --check > $L/chain.log 2>&1 || echo "generative chain check: see $L/chain.log"
python3 -B $K/../becoming-p69-landing/linkcheck.py $W
git status --short | grep -v "results/records/" || true
echo "records changed: $(git status --short | grep -c results/records/)"
echo "P73–P75 ready to commit"
