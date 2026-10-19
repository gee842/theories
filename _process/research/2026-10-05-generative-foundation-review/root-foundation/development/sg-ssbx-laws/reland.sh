#!/bin/zsh
# SG relanding on a fresh main (19 October 2026). From the checkout root of a branch at main's head with the modules
# and kit commit (e9d69be56) cherry-picked: join the modules, run the core checker, register the apart root, measure
# connectivity, apply the text, write the records, re-point references that matched at BASE, render, re-point the
# chapter drift SG made, render again. The gates and the commit are run after, by hand.
# usage: zsh reland.sh SCRATCH_DIR BASE      (BASE: the main commit the branch starts from)
set -e
L=$1; BASE=$2
K=_process/research/2026-10-05-generative-foundation-review/root-foundation/development/sg-ssbx-laws
PKG=experiments/integrated-correction/general-framework/generative-basis/lean/becoming
SG_ROOT=$PWD python3 -B $K/integrate.py
if pgrep -f "check_becoming.py" > /dev/null; then echo 'another checker run is going; wait for it'; exit 1; fi
ROOT=$PWD
(cd $PKG && python3 -B check_becoming.py > $ROOT/$K/checker-sg.log 2>&1)
R=$(python3 -c "import json; d=json.load(open('$PKG/becoming-verification.json')); assert d['status']=='passed', d['status']; print(d['utc'])")
echo "receipt $R"
python3 -B $K/register_apart.py
python3 -B _process/research/2026-10-05-generative-foundation-review/root-foundation/THEOREM-CONNECTIVITY.py --check > $K/connectivity-sg.log 2>&1
python3 -B $K/apply_text.py $R $BASE $K/connectivity-sg.log --board
python3 -B $K/make_records.py $R
python3 -B $K/rehash_refs.py $BASE | tail -1
echo '.build/' > $L/sg-excludes
render() { GIT_CONFIG_COUNT=1 GIT_CONFIG_KEY_0=core.excludesFile GIT_CONFIG_VALUE_0=$L/sg-excludes make research-render > $L/render-sg.log 2>&1 || true }
render
python3 - $L <<'PY'
import json, sys
L = sys.argv[1]
t = open(f'{L}/render-sg.log').read(); d = json.loads(t[t.index('{'):t.rindex('}') + 1])
assert not d.get('errors'), d['errors']
m = {x['id']: x['changed_sections'] for x in d.get('source_drift', [])
     if x['path'] == 'theories/becoming/chapters/THE-THEORY-OF-BECOMING.md'}
assert len(m) == len(d.get('source_drift', [])), d['source_drift']
json.dump(m, open(f'{L}/sg-drift.json', 'w'))
open(f'{L}/sg-drift-ids.txt', 'w').write(' '.join(sorted(m)))
print('drifting', len(m))
PY
IDS=$(cat $L/sg-drift-ids.txt)
[[ -n "$IDS" ]] && python3 -B $K/repoint_drift.py $L/sg-drift.json ${=IDS} | wc -l && render
python3 -c "
import json;t=open('$L/render-sg.log').read();d=json.loads(t[t.index('{'):t.rindex('}')+1]);print('errors',d.get('errors'),'drift',d.get('source_drift'))"
echo "done, receipt $R"
