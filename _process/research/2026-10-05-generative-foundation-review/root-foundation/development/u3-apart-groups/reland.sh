#!/bin/zsh
# U3/U4 relanding on a fresh main (19 October 2026): from a checkout at main's head with this kit in place,
# join the modules (integrate.py), run the core checker, the connectivity check with the register update, the
# text and records, the re-pointing of references that matched at BASE, and render. The gates (check, links, test),
# the board move and the commit are run after, by hand.
# usage (from the checkout root): zsh reland.sh SCRATCH_DIR BASE SECTION
set -e
L=$1; BASE=$2; SECTION=$3   # BASE: the main commit the checkout starts from; SECTION: the next study section
K=_process/research/2026-10-05-generative-foundation-review/root-foundation/development/u3-apart-groups
PKG=experiments/integrated-correction/general-framework/generative-basis/lean/becoming
CONN=_process/research/2026-10-05-generative-foundation-review/root-foundation
TOP=$PWD
[[ -d $K/.build ]] && mv $K/.build $L/u3-build-aside   # the catalogue reads ignored files; keep build output out of it
for m in Hexagrams Listing; do git diff --quiet 19185cc8c HEAD -- $PKG/Becoming/$m.lean || { echo "$m.lean changed on main since 19185cc8c: merge the kit copy first"; exit 1; }; done
U3_ROOT=$PWD python3 -B $K/integrate.py
(cd $PKG && python3 -B check_becoming.py > $TOP/$K/checker-u3.log 2>&1)
R=$(ls $PKG/becoming-checks | sort | tail -1)
echo receipt $R
(cd $CONN && python3 -B THEOREM-CONNECTIVITY.py > $L/conn-u3.json 2> $L/conn-u3.err) || true
python3 - <<PY
import json
d = json.load(open('$L/conn-u3.json'))
assert not d['apart_roots_unclassified'], d['apart_roots_unclassified']
reg = json.load(open('$CONN/THEOREM-CONNECTIVITY-APART.json'))
for s in d['register_entries_not_apart_roots']:
    del reg['roots'][s]
open('$CONN/THEOREM-CONNECTIVITY-APART.json', 'w').write(json.dumps(reg, ensure_ascii=False, indent=1) + '\n')
c = d['classes']
print('apart', c['apart: own vocabulary'] + c['apart: prelude-only statement'], 'of', d['spine_theorems'],
      'removed', len(d['register_entries_not_apart_roots']), 'components', d['components']['count'],
      'outside', len(d['components']['theorems_outside_the_main_component']))
PY
python3 -B $K/apply_text.py $SECTION $BASE $R $L/conn-u3.json
python3 -B $K/make_records.py $R $SECTION
python3 -B $K/rehash_refs.py $BASE $SECTION | tail -1
python3 -B $K/rebind.py $R
echo '.build/' > $L/u3-excludes
GIT_CONFIG_COUNT=1 GIT_CONFIG_KEY_0=core.excludesFile GIT_CONFIG_VALUE_0=$L/u3-excludes make research-render > $K/render-u3.log 2>&1 || true
python3 -c "
import json;t=open('$K/render-u3.log').read();d=json.loads(t[t.index('{'):t.rindex('}')+1]);print('errors',d.get('errors'),'drift',d.get('source_drift'))"
echo done
