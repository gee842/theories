#!/bin/bash
# Y2b (19 October 2026): re-land the earlier-work paragraph of study section 195 on the current main, when the item's
# turn in the landing queue comes. The ready commit is kept under refs/salvage/y2b-75b9ee747. Run with bash from the
# root of the Y2 worktree, whose tracked files must be clean. It resets the branch to main (keeping nothing uncommitted),
# applies the paragraph, re-points the records whose study reference matches main, moves the board row to the history
# file, renders, runs the gates and commits the listed paths. Landing on main is a separate fast-forward.
set -euo pipefail
READY=refs/salvage/y2b-75b9ee747
K=_process/research/2026-10-05-generative-foundation-review/root-foundation/development/y1-changes/y2
cd "$(git rev-parse --show-toplevel)"
test -z "$(git status --porcelain --untracked-files=no -- . ":(exclude)$K/board_move.py")" || { echo 'tracked changes present'; exit 1; }
cp "$K/board_move.py" "$K/apply_earlier.py" "$K/reland_y2b.sh" "${TMPDIR:-/tmp}/"
git reset -q --keep main
cp "${TMPDIR:-/tmp}/board_move.py" "${TMPDIR:-/tmp}/apply_earlier.py" "${TMPDIR:-/tmp}/reland_y2b.sh" "$K/"
BASE=$(git rev-parse --short HEAD)
git checkout "$READY" -- "$K/cite_earlier.py" "$K/render-5.log" "$K/render-6.log" "$K/render-7.log" "$K/gate-check-strict.log"
git reset -q -- "$K"
python3 -B "$K/apply_earlier.py" "$READY"
python3 -B "$K/cite_earlier.py" HEAD
python3 -B "$K/board_move.py" "landed (docs and records, no checker run): study §195 cites the earlier work on the places; record \`place-relations-in-context\` gains the provenance references; rendered on \`$BASE\`; \`research-check-strict\`, links, test and secrets pass" '| **Y2b: the earlier work on the places cited** '
EX=$(mktemp); echo '.build/' > "$EX"
export GIT_CONFIG_COUNT=1 GIT_CONFIG_KEY_0=core.excludesFile GIT_CONFIG_VALUE_0="$EX"
touch "$K/render-8.log"
make research-render > "$K/render-8.log" 2>&1
for g in check-strict links test secrets; do
  make "research-$g" > "$K/gate-$g.log" 2>&1 || { echo "gate $g failed: $K/gate-$g.log"; exit 1; }
done
LIST=$(mktemp)
git -c core.quotepath=false status --porcelain --untracked-files=all | grep -v 'becoming-checks/20261019T074455' | cut -c4- > "$LIST"
MSG=$(mktemp)
cat > "$MSG" <<EOF
Y2b landing: the earlier work on the places cited in study section 195

The earlier 生生不息 repository's HexagramPosition.lean (its commit efd892a5; its Lean is not
preserved here), its preserved report on places and operators and item H6 of the review of that
repository are cited in section 195: the definitions of 當位, 應, 中, 承 and 乘 agree; its 比
counts neighbours of one kind (亲比), while 比 here is the pair of two kinds; its commentary on
turning over is proved here (inPhase_reverse, phaseCount_reverse), as are the laws it lacks
(rises_reverse, rises_falls_ends); the review's H6 is revised: the count of 應 is not a lumping
of waxing and waning, its pattern is (opposition_goAlike). Nothing was ported as code.

Record place-relations-in-context gains the provenance references (the preserved report, the
review) and the census boundary; the records whose study reference matched main are re-pointed
after reading the change (cite_earlier.py). Docs and records, no checker run. Rendered on
$BASE; research-check-strict, links, test and secrets pass. Board row moved to the history file
(rule 4).
EOF
git add --pathspec-from-file="$LIST"
git commit -q --pathspec-from-file="$LIST" -F "$MSG"
git log --oneline -1
wc -l < "$LIST"
