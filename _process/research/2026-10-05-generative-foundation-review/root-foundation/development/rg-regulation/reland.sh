#!/bin/zsh
# RG landing on a fresh main (19 October 2026). From the checkout root of a branch at main's head with the module and
# the kit taken from the RG branch (Becoming/Regulation.lean at its package path, development/rg-regulation/): measure
# connectivity on main's tree (the count before), join the module, run the core checker, measure connectivity and update
# the register, apply the text, re-point RO's map and chapter, write the record and bring RO's record up, re-point
# references that matched at BASE, render, re-point the chapter drift RG made, render again, run verify_ro.py.
# The gates, the board move and the commit are run after, by hand.
# usage: zsh reland.sh SCRATCH_DIR BASE     (BASE: the main commit the branch starts from)
set -e
L=$1; BASE=$2
K=_process/research/2026-10-05-generative-foundation-review/root-foundation/development/rg-regulation
PKG=experiments/integrated-correction/general-framework/generative-basis/lean/becoming
CONN=_process/research/2026-10-05-generative-foundation-review/root-foundation
STUDY=$CONN/BECOMING-RENEWAL-READING.md
ROOT=$PWD
if pgrep -f "check_becoming.py" > /dev/null; then echo 'another checker run is going; wait for it'; exit 1; fi
mkdir -p $L
mv $PKG/Becoming/Regulation.lean $L/Regulation.lean.aside   # the count before is measured without the module
(cd $CONN && python3 -B THEOREM-CONNECTIVITY.py > $L/conn-before.json 2> $L/conn-before.err) || true
mv $L/Regulation.lean.aside $PKG/Becoming/Regulation.lean
RG_ROOT=$PWD python3 -B $K/integrate.py
(cd $PKG && LEAN_TIMEOUT=3600 python3 -B check_becoming.py > $ROOT/$K/checker-rg.log 2>&1)
R=$(python3 -c "import json; d=json.load(open('$PKG/becoming-verification.json')); assert d['status']=='passed', d['status']; print(d['utc'])")
echo "receipt $R"
(cd $CONN && python3 -B THEOREM-CONNECTIVITY.py > $L/conn-rg.json 2> $L/conn-rg.err) || true
python3 - <<PY
import json
d = json.load(open('$L/conn-rg.json'))
assert not d['apart_roots_unclassified'], d['apart_roots_unclassified']
reg = json.load(open('$CONN/THEOREM-CONNECTIVITY-APART.json'))
for s in d['register_entries_not_apart_roots']:
    del reg['roots'][s]
open('$CONN/THEOREM-CONNECTIVITY-APART.json', 'w').write(json.dumps(reg, ensure_ascii=False, indent=1) + '\n')
c = d['classes']
print('apart', c['apart: own vocabulary'] + c['apart: prelude-only statement'], 'of', d['spine_theorems'],
      'removed', d['register_entries_not_apart_roots'])
PY
(cd $CONN && python3 -B THEOREM-CONNECTIVITY.py --check > $L/conn-check.json 2> $L/conn-check.err)
python3 -B $K/apply_text.py $BASE $R $L/conn-rg.json $L/conn-before.json
SECTION=$(python3 -c "import re; print(re.search(r'^## (\d+)\. A level held from both sides, and a level read late \(RG\)$', open('$STUDY').read(), re.M).group(1))")
echo "study section $SECTION"
python3 -B $K/ro_points.py
python3 -B $K/make_record.py $R
python3 -B $K/update_ro_record.py $BASE
python3 -B $K/rehash_refs.py $BASE $SECTION | tail -1
python3 -B $K/update_goal.py
echo '.build/' > $L/rg-excludes
render() { GIT_CONFIG_COUNT=1 GIT_CONFIG_KEY_0=core.excludesFile GIT_CONFIG_VALUE_0=$L/rg-excludes make research-render > $L/render-rg.log 2>&1 || true }
render
python3 - $L <<'PY'
import json, sys
L = sys.argv[1]
t = open(f'{L}/render-rg.log').read(); d = json.loads(t[t.index('{'):t.rindex('}') + 1])
assert not d.get('errors'), d['errors']
m = {x['id']: x['changed_sections'] for x in d.get('source_drift', [])
     if x['path'] == 'theories/becoming/chapters/THE-THEORY-OF-BECOMING.md'}
assert len(m) == len(d.get('source_drift', [])), d['source_drift']
json.dump(m, open(f'{L}/rg-drift.json', 'w'))
open(f'{L}/rg-drift-ids.txt', 'w').write(' '.join(sorted(m)))
print('drifting', len(m))
PY
IDS=$(cat $L/rg-drift-ids.txt)
[[ -n "$IDS" ]] && python3 -B $K/repoint_drift.py $L/rg-drift.json ${=IDS} | wc -l && render
python3 -c "
import json;t=open('$L/render-rg.log').read();d=json.loads(t[t.index('{'):t.rindex('}')+1]);print('errors',d.get('errors'),'drift',d.get('source_drift'))"
python3 -B $K/../ro-relational-sources/verify_ro.py > $L/verify-ro.log 2>&1 || echo 'verify_ro.py failed'
head -3 $L/verify-ro.log
echo "done, receipt $R, study section $SECTION"
