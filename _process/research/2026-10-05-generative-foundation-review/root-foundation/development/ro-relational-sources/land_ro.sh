#!/bin/zsh
# RO landing (docs and records, no checker run) on a branch at main's head with RO's kit, chapter and sources in place:
# apply the text, write the record, re-point references that matched at BASE, render. The gates (check, links, test),
# the board move and the commit are run after, by hand.
# usage (from the checkout root): zsh land_ro.sh SCRATCH_DIR BASE
set -e
L=$1; BASE=$2
K=_process/research/2026-10-05-generative-foundation-review/root-foundation/development/ro-relational-sources
ND=($(python3 -B $K/apply_text.py))
echo study $ND[1] decision D$ND[2]
python3 -B $K/make_record.py $ND[1] $ND[2]
python3 -B $K/rehash_refs.py $BASE | tail -1
echo '.build/' > $L/ro-excludes
GIT_CONFIG_COUNT=1 GIT_CONFIG_KEY_0=core.excludesFile GIT_CONFIG_VALUE_0=$L/ro-excludes make research-render > $L/render-ro.log 2>&1 || true
python3 -c "
import json;t=open('$L/render-ro.log').read();d=json.loads(t[t.index('{'):t.rindex('}')+1]);print('errors',d.get('errors'),'drift',d.get('source_drift'))"
echo done
