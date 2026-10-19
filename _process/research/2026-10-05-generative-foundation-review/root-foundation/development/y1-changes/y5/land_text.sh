#!/bin/bash
# Y5: replay the landing text on a checkout whose branch holds the package commit on main: the apart register, the
# text, the record, the re-pointing, the board move, the render and the gates. Run from the checkout's root on a tree
# where the core checker (checker-y5.log) and the connectivity check after register_apart.py (conn-1.log) have run.
# usage: bash land_text.sh RECEIPT CHECKER_MAIN BASE
#   RECEIPT       the core receipt (its run's main is CHECKER_MAIN)
#   BASE          the main commit the branch is rebased on (records that matched it are re-pointed)
set -euo pipefail
R=$1; CHECKER_MAIN=$2; BASE=$3
K=_process/research/2026-10-05-generative-foundation-review/root-foundation/development/y1-changes/y5
python3 -B $K/apply_text.py "$R" "$(git rev-parse "$CHECKER_MAIN")" $K/conn-1.log $K/checker-y5.log > $K/apply_text.log
read -r N DN < $K/apply_text.log
echo "section $N, decision $DN"
python3 -B $K/make_record.py "$R" "$N" "$DN" > $K/make_record.log
python3 -B $K/rehash_refs.py "$(git rev-parse "$BASE")" > $K/rehash.log
python3 -B $K/board_move.py "$R" "$(git rev-parse --short=9 "$CHECKER_MAIN")" $K/conn-1.log "$N" "$DN"
status=0
for g in research-render research-check research-check-strict research-links research-test research-secrets; do
  if make $g > $K/gate-$g.log 2>&1; then echo "$g ok"; else echo "$g FAILED"; status=1; fi
done
exit $status
