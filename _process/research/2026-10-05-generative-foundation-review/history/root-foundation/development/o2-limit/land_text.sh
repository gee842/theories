#!/bin/sh
# O1 and O2 landing text and records, in order (run from the checkout root to edit):
#   sh land_text.sh RECEIPT BASE CONNECTIVITY_LOG SCRATCH
# Both texts first, then both records, then the re-pointing of records whose cited files the landing changed; then
# a render with build output excluded, its log in SCRATCH/render.log. Stops at the first failure.
set -e
R=$1; B=$2; C=$3; S=$4
D=_process/research/2026-10-05-generative-foundation-review/root-foundation/development
N1=$(python3 -B $D/o1-verification/apply_text.py "$R" "$B" "$C" | tee /dev/stderr | sed -n 's/^STUDY_SECTION //p')
N2=$(python3 -B $D/o2-limit/apply_text.py "$R" "$C" "$N1" | tee /dev/stderr | sed -n 's/^STUDY_SECTION //p')
python3 -B $D/o1-verification/make_record.py "$R" "$N1"
python3 -B $D/o2-limit/make_record.py "$R" "$N2"
python3 -B $D/o2-limit/rehash_refs.py "$B"
printf '.build/\n.lake/\n' > "$S/excl"
GIT_CONFIG_COUNT=1 GIT_CONFIG_KEY_0=core.excludesFile GIT_CONFIG_VALUE_0="$S/excl" make research-render > "$S/render.log" 2>&1 || echo "render reported errors or drift: $S/render.log"
echo "N1=$N1 N2=$N2"
