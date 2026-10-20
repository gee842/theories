#!/bin/zsh
# F3Q landing on a fresh main (18 October 2026), modelled on G3's reland.sh: from the branch rebased on main's head,
# register the six modules, run the core checker, register their apart roots (apart_q.py), measure connectivity
# (its --check must pass), rebind and re-point the records, render and restore the environment-dependent Lean index pair. The gates (check, links, test) and the board move are run after,
# by hand. usage (from the checkout root): zsh land_q.sh BASE_SHA LOG_DIR
set -e
BASE=$1; L=$2
Q=_process/research/2026-10-05-generative-foundation-review/root-foundation/development/bridge-fold
PKG=experiments/integrated-correction/general-framework/generative-basis/lean/becoming
mkdir -p $L
L=$(cd $L && pwd)
python3 -B $Q/land_q.py
(cd $PKG && LEAN_TIMEOUT=1800 BECOMING_JOBS=3 python3 -B check_becoming.py > $L/checker-q.log 2>&1)
R=$(ls -t $PKG/becoming-checks | head -1)
python3 -c "import json;assert json.load(open('$PKG/becoming-checks/$R/verification.json'))['status']=='passed'"
grep -q '"core_axioms": \[\]' $L/checker-q.log
echo receipt=$R
python3 -B $Q/apart_q.py
python3 -B _process/research/2026-10-05-generative-foundation-review/root-foundation/THEOREM-CONNECTIVITY.py --write --check > $L/conn-q.log 2>&1
python3 -c "
import json;t=open('$L/conn-q.log').read();d=json.loads(t[t.index('{'):t.rindex('}')+1])
assert not d['apart_roots_unclassified'] and not d['register_entries_not_apart_roots']
print('apart', sum(v for k,v in d['classes'].items() if k.startswith('apart')))"
python3 -B $Q/rebind_q.py $R | tail -1
python3 -B $Q/rehash_q.py $BASE | tail -1
echo '.build/' > $L/q-excludes
GIT_CONFIG_COUNT=1 GIT_CONFIG_KEY_0=core.excludesFile GIT_CONFIG_VALUE_0=$L/q-excludes make research-render > $L/render-q.log 2>&1
python3 -c "
import json;t=open('$L/render-q.log').read();d=json.loads(t[t.index('{'):t.rindex('}')+1]);print('errors',d.get('errors'),'drift',d.get('source_drift'))"
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
