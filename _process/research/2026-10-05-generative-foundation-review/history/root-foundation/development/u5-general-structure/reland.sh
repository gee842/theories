#!/bin/zsh
# U5 landing on a fresh main (19 October 2026). From the checkout root of a branch at main's head with the kit commit
# cherry-picked: measure connectivity on main's tree (the count before), join the modules, run the core checker, measure
# connectivity and update the register, apply the text, write the records, re-point references that matched at BASE,
# render, re-point the chapter drift U5 made, render again, write the measure. The gates, the board move and the commit
# are run after, by hand.
# usage: zsh reland.sh SCRATCH_DIR BASE SECTION     (BASE: the main commit the branch starts from)
set -e
L=$1; BASE=$2; SECTION=$3
K=_process/research/2026-10-05-generative-foundation-review/root-foundation/development/u5-general-structure
PKG=experiments/integrated-correction/general-framework/generative-basis/lean/becoming
CONN=_process/research/2026-10-05-generative-foundation-review/root-foundation
ROOT=$PWD
[[ -d $K/.build ]] && mv $K/.build $L/u5-build-aside   # the catalogue reads ignored files; keep build output out of it
if pgrep -f "check_becoming.py" > /dev/null; then echo 'another checker run is going; wait for it'; exit 1; fi
(cd $CONN && python3 -B THEOREM-CONNECTIVITY.py > $L/conn-before.json 2> $L/conn-before.err)
U5_ROOT=$PWD python3 -B $K/integrate.py
(cd $PKG && python3 -B check_becoming.py > $ROOT/$K/checker-u5.log 2>&1)
R=$(python3 -c "import json; d=json.load(open('$PKG/becoming-verification.json')); assert d['status']=='passed', d['status']; print(d['utc'])")
echo "receipt $R"
(cd $CONN && python3 -B THEOREM-CONNECTIVITY.py > $L/conn-u5.json 2> $L/conn-u5.err) || true
python3 - <<PY
import json
d = json.load(open('$L/conn-u5.json'))
assert not d['apart_roots_unclassified'], d['apart_roots_unclassified']
reg = json.load(open('$CONN/THEOREM-CONNECTIVITY-APART.json'))
for s in d['register_entries_not_apart_roots']:
    del reg['roots'][s]
open('$CONN/THEOREM-CONNECTIVITY-APART.json', 'w').write(json.dumps(reg, ensure_ascii=False, indent=1) + '\n')
c = d['classes']
print('apart', c['apart: own vocabulary'] + c['apart: prelude-only statement'], 'of', d['spine_theorems'],
      'removed', len(d['register_entries_not_apart_roots']))
PY
(cd $CONN && python3 -B THEOREM-CONNECTIVITY.py --check > $L/conn-check.json 2> $L/conn-check.err)
python3 -B $K/apply_text.py $SECTION $BASE $R $L/conn-u5.json $L/conn-before.json
python3 -B $K/make_records.py $R $SECTION
python3 -B $K/rehash_refs.py $BASE $SECTION | tail -1
echo '.build/' > $L/u5-excludes
render() { GIT_CONFIG_COUNT=1 GIT_CONFIG_KEY_0=core.excludesFile GIT_CONFIG_VALUE_0=$L/u5-excludes make research-render > $L/render-u5.log 2>&1 || true }
render
python3 - $L <<'PY'
import json, sys
L = sys.argv[1]
t = open(f'{L}/render-u5.log').read(); d = json.loads(t[t.index('{'):t.rindex('}') + 1])
assert not d.get('errors'), d['errors']
m = {x['id']: x['changed_sections'] for x in d.get('source_drift', [])
     if x['path'] == 'theories/becoming/chapters/THE-THEORY-OF-BECOMING.md'}
assert len(m) == len(d.get('source_drift', [])), d['source_drift']
json.dump(m, open(f'{L}/u5-drift.json', 'w'))
open(f'{L}/u5-drift-ids.txt', 'w').write(' '.join(sorted(m)))
print('drifting', len(m))
PY
IDS=$(cat $L/u5-drift-ids.txt)
[[ -n "$IDS" ]] && python3 -B $K/repoint_drift.py $L/u5-drift.json ${=IDS} | wc -l && render
python3 -c "
import json;t=open('$L/render-u5.log').read();d=json.loads(t[t.index('{'):t.rindex('}')+1]);print('errors',d.get('errors'),'drift',d.get('source_drift'))"
echo "done, receipt $R"
