#!/bin/zsh
# G4 landing on a fresh main (18 October 2026): from a branch at main's head with the module untracked in this
# folder, integrate, run the core checker, measure connectivity, apply the text and records, re-point references
# that matched at BASE, render and restore the environment-dependent Lean index pair. The gates (check, links, test)
# and the board move are run after, by hand. usage (from the checkout root): zsh reland.sh BASE_SHA SCRATCH_DIR
set -e
BASE=$1; L=$2
G=_process/research/2026-10-05-generative-foundation-review/root-foundation/development/g4-law-through-coupling
PKG=experiments/integrated-correction/general-framework/generative-basis/lean/becoming
python3 -B $G/integrate.py
(cd $PKG && LEAN_TIMEOUT=1800 BECOMING_JOBS=3 python3 -B check_becoming.py > $OLDPWD/$G/checker-g4.log 2>&1)
R=$(ls -t $PKG/becoming-checks | head -1)
python3 -c "import json;assert json.load(open('$PKG/becoming-checks/$R/verification.json'))['status']=='passed'"
echo receipt=$R
python3 -B _process/research/2026-10-05-generative-foundation-review/root-foundation/THEOREM-CONNECTIVITY.py --check > $L/conn-g4r.log 2>&1
APART=$(python3 -c "
import json;t=open('$L/conn-g4r.log').read();d=json.loads(t[t.index('{'):t.rindex('}')+1]);c=d['classes']
assert 'Becoming.LawThroughCoupling' not in d['apart_by_module']
print(sum(v for k,v in c.items() if k.startswith('apart')))")
echo apart=$APART
N=$(python3 -B $G/apply_text.py $R $APART $(git rev-parse --short=9 HEAD))
echo section=$N
python3 -B $G/make_record.py $R $N
python3 -B $G/rehash_refs.py $BASE | tail -1
echo '.build/' > $L/g4-excludes
GIT_CONFIG_COUNT=1 GIT_CONFIG_KEY_0=core.excludesFile GIT_CONFIG_VALUE_0=$L/g4-excludes make research-render > $L/render-g4r.log 2>&1
python3 -c "
import json;t=open('$L/render-g4r.log').read();d=json.loads(t[t.index('{'):t.rindex('}')+1]);print('errors',d.get('errors'),'drift',d.get('source_drift'))"
git checkout HEAD -- theories/becoming/results/data/lean-index.json theories/becoming/results/LEAN-INDEX.md
python3 - <<'EOF'
import json,subprocess
M='_process/architecture/generated-manifest.json'
new=json.load(open(M)); old=json.loads(subprocess.run(['git','show','HEAD:'+M],capture_output=True,text=True).stdout)
for p in ['theories/becoming/results/data/lean-index.json','theories/becoming/results/LEAN-INDEX.md']:
    new['files'][p]=old['files'][p]
open(M,'w').write(json.dumps(new,ensure_ascii=False,indent=2)+'\n')
EOF
echo done
