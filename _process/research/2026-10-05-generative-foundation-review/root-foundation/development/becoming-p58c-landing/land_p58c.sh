#!/bin/zsh
# P58c landing in the worktree W, after both checkers passed on the patched tree (the tree's modules copied over
# Becoming/, then check_becoming.py and check_correction_inquiry.py with LEAN_TIMEOUT=3600).
# Usage: LAND_WT=W zsh land_p58c.sh. Stops at the first failure. Commits nothing.
set -e
S=/private/tmp/claude-501/-Users-ren-theories/dfe4a1b1-3a34-40ef-86a7-d1c09e897f30/scratchpad
W=${LAND_WT:?set LAND_WT}
P=$S/p58c
Q=$S/p54
L=${LAND_LOGS:-$P/landing}
RF=_process/research/2026-10-05-generative-foundation-review/root-foundation
mkdir -p $L
cd $W
test -z "$BECOMING_FRESH" || { echo "BECOMING_FRESH is set"; exit 1; }
python3 -B $P/p58c_spec.py $W $L
python3 -B $P/p58c_docs.py $W | tee $L/docs.log
SEC=$(grep '^SECTION ' $L/docs.log | cut -d' ' -f2)
python3 -B $P/p58c_records.py $W $SEC
if [ -z "$DRY" ]; then   # DRY=1 for a dry run with stand-in receipts: the inventory reads the checked core
  python3 -B $RF/DECIDABILITY-INVENTORY.py > $L/inventory.log 2>&1 || { echo "inventory failed"; tail -30 $L/inventory.log; exit 1; }
  tail -3 $L/inventory.log
fi
P45ROOT=$W python3 -B $Q/shared/repoint.py $L/spec.json > $L/repoint.log
echo "re-pointed $(grep -c '^re-pointed' $L/repoint.log) records"
python3 -B $Q/shared/modcounts.py $L/counts.json $W > $L/modcounts.log
cat $L/modcounts.log
python3 -B $P/p58c_refresh.py $W > $L/refresh.log
cat $L/refresh.log
K=$RF/development/becoming-p58c-landing
mkdir -p $K/lean/Becoming
cp $P/kit/README.md $P/land_p58c.sh $P/p58c_names.py $P/namemap.json $P/namemap_p58c.py $P/p58c_spec.py $P/p58c_docs.py \
  $P/p58c_records.py $P/p58c_refresh.py $P/hand_p58c.py $P/tokens_p58c.py $P/tokens2_p58c.py $P/openness_p58c.py \
  $P/openness2_p58c.py $P/openness3_p58c.py $P/docs_lean_p58c.py $P/resolution2_p58c.py $P/wrap_p58c.py $P/wrapcode_p58c.py \
  $Q/shared/repoint.py $Q/shared/modcounts.py $K/
python3 -B tools/research/reading_catalogue.py > $L/catalogue_gen.log 2>&1
python3 -B tools/research/lean_catalogue.py > $L/lean_gen.log 2>&1
python3 -B tools/research/research.py render > $L/render.log 2>&1 || { echo "render failed"; tail -30 $L/render.log; exit 1; }
python3 -B tools/research/session_map.py --capture > $L/capture.log 2>&1
python3 -B tools/research/research.py render > $L/render2.log 2>&1 || { echo "render failed"; tail -30 $L/render2.log; exit 1; }
python3 -B tools/research/research.py check > $L/check.log 2>&1 || { echo "research check failed"; tail -40 $L/check.log; exit 1; }
python3 -B tools/research/lean_catalogue.py --check > $L/lean_check.log 2>&1 || { echo "lean catalogue check failed"; tail -5 $L/lean_check.log; exit 1; }
python3 -B tools/research/reading_catalogue.py --check > $L/catalogue_check.log 2>&1 || { echo "reading catalogue check failed"; tail -5 $L/catalogue_check.log; exit 1; }
python3 -B tools/research/session_map.py --check > $L/session_check.log 2>&1 || { echo "session map check failed"; tail -5 $L/session_check.log; exit 1; }
python3 -B tools/research/generative_chain.py --check > $L/chain.log 2>&1 || echo "generative chain check: see $L/chain.log"
git status --short | grep -v "results/records/" || true
echo "records changed: $(git status --short | grep -c results/records/)"
echo "P58c ready to commit"
