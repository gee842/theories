#!/bin/zsh
# P59 + P58 landing in the session's worktree: the Lean, both checkers, the inventory page, the docs and records,
# generators, the hash refresh and the checks.
# Usage: zsh land_p5859.sh <main-head-commit> [--no-check]
#   --no-check skips the patches and the two checkers (for a rerun against receipts already in the tree).
# Stops at the first failure. Commits nothing: the commit and fast-forward follow by hand.
set -e
S=/private/tmp/claude-501/-Users-ren-theories/dfe4a1b1-3a34-40ef-86a7-d1c09e897f30/scratchpad
W=${LAND_WT:-$S/p58/wt}
P=$S/p58
Q=$S/p54
L=${LAND_LOGS:-$P/landing-5859}
RF=_process/research/2026-10-05-generative-foundation-review/root-foundation
LB=experiments/integrated-correction/general-framework/generative-basis/lean
mkdir -p $L
cd $W
if [[ "$2" != "--no-check" ]]; then
  git switch -q --detach "$1"
  # untracked retained runs of earlier checks of this landing stay and are committed with it
  test -z "$(git status --short --untracked-files=no)" || { echo "worktree not clean"; exit 1; }
  test -z "$BECOMING_FRESH" || { echo "BECOMING_FRESH is set"; exit 1; }
  python3 -B $P/p58_lean.py $W
  python3 -B $Q/p59_lean.py $W
  python3 -B $LB/becoming/check_becoming.py > $L/core.log 2>&1 || { echo "core check failed"; tail -30 $L/core.log; exit 1; }
  LEAN_TIMEOUT=${LEAN_TIMEOUT:-3600} python3 -B $LB/universal-ethics/generative-capacity/check_correction_inquiry.py > $L/peri.log 2>&1 \
    || { echo "periphery check failed"; tail -30 $L/peri.log; exit 1; }
fi
python3 -c "import json,sys; r=json.load(open('$LB/becoming/becoming-verification.json')); assert r['status']=='passed'; print('core receipt', r['utc'])"
python3 -c "import json,sys; r=json.load(open('$LB/universal-ethics/generative-capacity/correction-inquiry-verification.json')); assert r['status']=='passed'; print('periphery receipt', r['utc'])"
# the inventory page, read by Lean from the checked core (modules restored from the checker's cache)
cp $P/repo/DECIDABILITY-INVENTORY.py $P/repo/DECIDABILITY-INVENTORY.lean $RF/
if [[ -n "$INV_MOCK" ]]; then
  cp "$INV_MOCK" $RF/DECIDABILITY-INVENTORY.md   # dry run only: a page generated earlier, no Lean run
else
  python3 -B $RF/DECIDABILITY-INVENTORY.py > $L/inventory.log 2>&1 || { echo "inventory failed"; tail -30 $L/inventory.log; exit 1; }
  tail -3 $L/inventory.log
fi
# spec and documents
python3 -B $P/p5859_spec.py $W $L
python3 -B $P/p5859_docs.py $W $L/values.json $RF/DECIDABILITY-INVENTORY.md
# records
P45ROOT=$W python3 -B $Q/shared/repoint.py $L/spec.json > $L/repoint.log
echo "re-pointed $(grep -c '^re-pointed' $L/repoint.log) records"
python3 -B $Q/shared/modcounts.py $L/counts.json $W > $L/modcounts.log
S58=$(grep -o '^## [0-9]*\. 可判定性局部化（P58）' $RF/BECOMING-RENEWAL-READING.md | grep -o '^## [0-9]*' | grep -o '[0-9]*')
S59=$(grep -o '^## [0-9]*\. 不平衡作为关系项：先证等价（P59）' $RF/BECOMING-RENEWAL-READING.md | grep -o '^## [0-9]*' | grep -o '[0-9]*')
python3 -B $P/p58_records.py $W $S58 $S59
# references to files this landing changed, where the record was current at HEAD (the p54 rule), before the generators
python3 -B $P/p5859_refresh.py $W > $L/refresh.log
cat $L/refresh.log
# the landing kit, kept as provenance beside the other landings' kits, before the generators capture the tree
K=$RF/development/becoming-p58-p59-landing
mkdir -p $K
cp $P/kit/README.md $P/land_p5859.sh $P/p58_lean.py $Q/p59_lean.py $P/p5859_spec.py $P/p5859_docs.py $P/p58_records.py \
  $P/p5859_refresh.py $Q/shared/repoint.py $Q/shared/modcounts.py $P/board_p5859.py $P/mock_receipts_5859.py $K/
# generators
python3 -B tools/research/reading_catalogue.py > $L/catalogue_gen.log 2>&1
python3 -B tools/research/lean_catalogue.py > $L/lean_gen.log 2>&1
python3 -B tools/research/research.py render > $L/render.log 2>&1 || { echo "render failed"; tail -30 $L/render.log; exit 1; }
python3 -B tools/research/session_map.py --capture > $L/capture.log 2>&1
python3 -B tools/research/research.py render > $L/render2.log 2>&1 || { echo "render failed"; tail -30 $L/render2.log; exit 1; }
# checks
python3 -B tools/research/research.py check > $L/check.log 2>&1 || { echo "research check failed"; tail -40 $L/check.log; exit 1; }
python3 -B tools/research/lean_catalogue.py --check > $L/lean_check.log 2>&1 || { echo "lean catalogue check failed"; tail -5 $L/lean_check.log; exit 1; }
python3 -B tools/research/reading_catalogue.py --check > $L/catalogue_check.log 2>&1 || { echo "reading catalogue check failed"; tail -5 $L/catalogue_check.log; exit 1; }
python3 -B tools/research/session_map.py --check > $L/session_check.log 2>&1 || { echo "session map check failed"; tail -5 $L/session_check.log; exit 1; }
python3 -B tools/research/generative_chain.py --check > $L/chain.log 2>&1 || echo "generative chain check: see $L/chain.log"
# no research tests: this landing changes no infrastructure (AGENTS.md: run them after infrastructure changes)
grep -o '"errors": \[[^]]*\]' $L/check.log | head -2 || true
git status --short | grep -v "results/records/" | grep -v "becoming-checks/\|correction-inquiry-checks/" || true
echo "records changed: $(git status --short | grep -c results/records/)"
echo "study sections: P58 $S58, P59 $S59"
echo "P59 + P58 ready to commit"
