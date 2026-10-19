#!/bin/zsh
# V2 landing on a fresh main (19 October 2026): from a branch at main's head with the package commit cherry-picked,
# check that the receipt still binds the tree, apply the text and records, re-point references that matched at BASE,
# render, re-point section-8 drift, render again. The gates (check, links, test) and the commit are run after, by hand.
# usage (from the checkout root): zsh reland.sh SCRATCH_DIR BASE [RECEIPT [TEXT_BASE]]
set -e
L=$1; BASE=$2   # BASE: the main commit the branch starts from
K=_process/research/2026-10-05-generative-foundation-review/root-foundation/development/v2-tolerance
PKG=experiments/integrated-correction/general-framework/generative-basis/lean/becoming
R=${3:-20261019T073658.056526Z}; TEXTBASE=${4:-$BASE}
python3 - <<PY
import hashlib, json
r = json.load(open('$PKG/becoming-checks/$R/verification.json'))
bad = [m for m, p in r['source_paths'].items() if hashlib.sha256(open('$PKG/../' + p, 'rb').read()).hexdigest() != r['source_sha256'][m]]
assert not bad, bad
print('receipt binds the tree:', len(r['source_paths']), 'sources')
PY
python3 -B $K/apply_text.py $R $TEXTBASE $K/connectivity-v2.log
python3 -B $K/make_records.py $R
python3 -B $K/rehash_refs.py $BASE | tail -1
echo '.build/' > $L/v2-excludes
render() { GIT_CONFIG_COUNT=1 GIT_CONFIG_KEY_0=core.excludesFile GIT_CONFIG_VALUE_0=$L/v2-excludes make research-render > $L/render-v2.log 2>&1 || true }
render
IDS=$(python3 -c "
import json;t=open('$L/render-v2.log').read();d=json.loads(t[t.index('{'):t.rindex('}')+1])
assert not d.get('errors'), d['errors']
assert all(x['changed_sections']==['## 8. Open programme'] for x in d.get('source_drift',[])), d['source_drift']
print(' '.join(sorted({x['id'] for x in d.get('source_drift',[])})))")
[[ -n "$IDS" ]] && python3 -B $K/repoint_drift.py ${=IDS} | wc -l && render
python3 -c "
import json;t=open('$L/render-v2.log').read();d=json.loads(t[t.index('{'):t.rindex('}')+1]);print('errors',d.get('errors'),'drift',d.get('source_drift'))"
echo done
