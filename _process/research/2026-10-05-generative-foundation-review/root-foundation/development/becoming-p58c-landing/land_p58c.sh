#!/bin/zsh
# P58c landing in W, after apply_latest.py and both checkers passed on that exact tree.
# Usage: LAND_WT=W zsh land_p58c.sh. Stops at the first failure. Commits nothing.
set -e
set -o pipefail
W=${LAND_WT:?set LAND_WT}
P=${0:A:h}
Q=$P/../becoming-p58b-landing
L=${LAND_LOGS:-$W/../p58c-landing-logs}
RF=_process/research/2026-10-05-generative-foundation-review/root-foundation
mkdir -p $L
cd $W
test -z "$BECOMING_FRESH" || { echo "BECOMING_FRESH is set"; exit 1; }
python3 -B $P/p58c_spec.py $W $L
python3 -B $P/p58c_docs.py $W | tee $L/docs.log
SEC=$(grep '^SECTION ' $L/docs.log | cut -d' ' -f2)
python3 -B $P/p58c_records.py $W $SEC
python3 -B $P/inventory_names.py $W
if [ -z "$DRY" ]; then   # DRY=1 for a dry run with stand-in receipts: the inventory reads the checked core
  python3 -B $RF/DECIDABILITY-INVENTORY.py > $L/inventory.log 2>&1 || { echo "inventory failed"; tail -30 $L/inventory.log; exit 1; }
  tail -3 $L/inventory.log
  python3 -B $P/../becoming-landing-kit/zero_count.py $W
fi
P45ROOT=$W python3 -B $Q/repoint.py $L/spec.json > $L/repoint.log
echo "re-pointed $(grep -c '^re-pointed' $L/repoint.log) records"
python3 -B $Q/modcounts.py $L/counts.json $W > $L/modcounts.log
cat $L/modcounts.log
python3 -B $P/p58c_refresh.py $W > $L/refresh.log
cat $L/refresh.log
python3 -B tools/research/reading_catalogue.py > $L/catalogue_gen.log 2>&1
python3 -B tools/research/lean_catalogue.py > $L/lean_gen.log 2>&1
python3 -B $P/p58c_refresh.py $W >> $L/refresh.log
python3 -B tools/research/research.py render > $L/render.log 2>&1 || { echo "render failed"; tail -30 $L/render.log; exit 1; }
python3 -B tools/research/session_map.py --capture > $L/capture.log 2>&1
python3 -B $P/p58c_refresh.py $W >> $L/refresh.log
python3 -B tools/research/research.py render > $L/render2.log 2>&1 || { echo "render failed"; tail -30 $L/render2.log; exit 1; }
python3 -B tools/research/research.py check > $L/check.log 2>&1 || { echo "research check failed"; tail -40 $L/check.log; exit 1; }
python3 -B tools/research/lean_catalogue.py --check > $L/lean_check.log 2>&1 || { echo "lean catalogue check failed"; tail -5 $L/lean_check.log; exit 1; }
python3 -B tools/research/reading_catalogue.py --check > $L/catalogue_check.log 2>&1 || { echo "reading catalogue check failed"; tail -5 $L/catalogue_check.log; exit 1; }
python3 -B tools/research/session_map.py --check > $L/session_check.log 2>&1 || { echo "session map check failed"; tail -5 $L/session_check.log; exit 1; }
python3 -B tools/research/generative_chain.py --check > $L/chain.log 2>&1 || echo "generative chain check: see $L/chain.log"
git status --short | grep -v "results/records/" || true
echo "records changed: $(git status --short | grep -c results/records/)"
echo "P58c ready to commit"
