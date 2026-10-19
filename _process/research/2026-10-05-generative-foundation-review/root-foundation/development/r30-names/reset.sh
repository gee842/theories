#!/bin/sh
# R30 working tool: put the package's Lean files back to main before R30 (BASE; the four renamed modules
# removed), then reapply the checker's text change and the table. Run from the checkout root.
set -e
L=experiments/integrated-correction/general-framework/generative-basis/lean/becoming
K=_process/research/2026-10-05-generative-foundation-review/root-foundation/development/r30-names
git reset -q HEAD -- "$L"
git checkout 4cc010fb0 -- "$L"
git reset -q HEAD -- "$L"
for m in Arising MoveFormation Restoration SecuredContent; do
  if [ -f "$L/Becoming/$m.lean" ]; then rm "$L/Becoming/$m.lean"; fi
done
git apply "$K/check_becoming.patch"
python3 -B "$K/apply.py" .
python3 -B "$K/positive.py" .
python3 -B "$K/manual.py" .
