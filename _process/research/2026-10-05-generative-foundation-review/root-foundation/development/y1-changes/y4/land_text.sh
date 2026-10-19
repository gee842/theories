#!/bin/bash
# Y4: replay the landing text on a checkout whose branch holds the package commit on main: the text, the record, the
# re-pointing, the board move, the render and the gates. Run from the checkout's root on a clean tree.
# usage: bash land_text.sh RECEIPT CHECKER_MAIN BASE
#   RECEIPT       the core receipt (its run's main is CHECKER_MAIN)
#   BASE          the main commit the branch is rebased on (records that matched it are re-pointed)
set -euo pipefail
R=$1; CHECKER_MAIN=$2; BASE=$3
K=_process/research/2026-10-05-generative-foundation-review/root-foundation/development/y1-changes/y4
python3 -B $K/apply_text.py "$R" "$(git rev-parse "$CHECKER_MAIN")" $K/conn-1.log $K/checker-y4.log > $K/apply_text.log
read -r N DN < $K/apply_text.log
echo "section $N, decision $DN"
python3 -B $K/make_record.py "$R" "$N" "$DN" > $K/make_record.log
python3 -B $K/rehash_refs.py "$(git rev-parse "$BASE")" > $K/rehash.log
python3 -B $K/repoint_y3.py >> $K/rehash.log
D_ID="d${DN#D}-初上无位与独应之读--the-readings-of-the-fixed-places-and-the-sole-line"
RF=research/2026-10-05-generative-foundation-review/root-foundation
STATE="claimed 2026-10-19; **landed** 2026-10-19: \`Becoming.HexagramSites\`, 103 theorems, 142 declarations, empty axiom reports, core receipt \`$R\` on \`$(git rev-parse --short=9 "$CHECKER_MAIN")\` (after Z1, while T1 and X1b ran no core checker; rule 5); connectivity 464 apart of 10,847, 23 of them in the module, its 21 roots registered as model witnesses (what the 彖, the 小象, the 文言, the line texts and 王弼's 略例下 say of named configurations, the censuses, 王弼's dilemma, the twelve configurations with a sole line) and 2 lemmas only they use; record [fixed-places-and-sole-lines](../theories/becoming/results/records/fixed-places-and-sole-lines.md), [study §$N]($RF/BECOMING-RENEWAL-READING.md#$N-王弼s-readings-of-the-places-on-the-spine-y4), decision [$DN]($RF/DELEGATED-CHOICES.md#$D_ID) with a revision note on D50 (3); the 《周易略例》 preserved (the index and seven pages, revision ids, timestamps and SHA-256); 需上六 an agreement under the second relation, its divergence from the parity of six places kept; passage map 88 (19 added, 5 of Y2's revised), eight new censuses, each of nine mutations caught; render, check, strict check, links, test and secrets pass"
python3 -B $K/board_move.py "$STATE"
for g in research-render research-check research-check-strict research-links research-test research-secrets; do
  touch $K/gate-$g.log
done
status=0
for g in research-render research-check research-check-strict research-links research-test research-secrets; do
  if make $g > $K/gate-$g.log 2>&1; then echo "$g ok"; else echo "$g FAILED"; status=1; fi
done
exit $status
