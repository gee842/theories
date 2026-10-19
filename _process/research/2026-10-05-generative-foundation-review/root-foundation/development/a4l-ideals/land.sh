#!/bin/zsh
# A4-L landing on a fresh main (19 October 2026): from the branch rebased on main's head, with the two modules in this
# folder, integrate them into the core, register their apart roots, run the core checker, check connectivity, run the
# correspondence checker, apply the text and the records, re-point references that matched at BASE, render and restore
# the environment-dependent Lean index pair. The gates (check, links, test, lint) and the board move are run after, by
# hand. usage (from the checkout root): zsh land.sh BASE_SHA SCRATCH_DIR "AFTER"
# AFTER is what BASE adds to the last landing, for the receipt sentence (for example "after N7's landing and its board
# move").
set -e
BASE=$1; L=$2; AFTER=$3
K=_process/research/2026-10-05-generative-foundation-review/root-foundation/development/a4l-ideals
PKG=experiments/integrated-correction/general-framework/generative-basis/lean/becoming
FORMAL=experiments/integrated-correction/general-framework/generative-basis/mathematical-abstraction/completion/formal
mkdir -p $L
python3 -B $K/integrate.py
python3 -B $K/register_apart.py
(cd $PKG && LEAN_TIMEOUT=1800 BECOMING_JOBS=3 python3 -B check_becoming.py > $OLDPWD/$K/checker-a4l.log 2>&1)
R=$(ls -t $PKG/becoming-checks | head -1)
python3 -c "import json;assert json.load(open('$PKG/becoming-checks/$R/verification.json'))['status']=='passed'"
echo receipt=$R
python3 -B _process/research/2026-10-05-generative-foundation-review/root-foundation/THEOREM-CONNECTIVITY.py --check > $L/conn-a4l.log 2>&1
python3 -c "
import json;t=open('$L/conn-a4l.log').read();d=json.loads(t[t.index('{'):t.rindex('}')+1]);c=d['classes']
print('apart', sum(v for k,v in c.items() if k.startswith('apart')), 'of', sum(c.values()),
      {m: d['apart_by_module'].get(m) for m in ('Becoming.Ideals', 'Becoming.HistoryIdeals')})"
(LEAN_TIMEOUT=1800 python3 -B $FORMAL/check_ideals_correspondence.py > $K/checker-corr.log 2>&1)
C=$(ls -t $FORMAL/ideals-correspondence-checks | head -1)
python3 -c "import json;assert json.load(open('$FORMAL/ideals-correspondence-checks/$C/verification.json'))['status']=='passed'"
echo correspondence=$C
N=$(python3 -B $K/apply_text.py $R $BASE "$AFTER" $L/conn-a4l.log $C)
echo section=$N
python3 -B $K/make_record.py $R $N $C
python3 -B $K/rehash_refs.py $BASE | tail -1
echo '.build/' > $L/a4l-excludes
GIT_CONFIG_COUNT=1 GIT_CONFIG_KEY_0=core.excludesFile GIT_CONFIG_VALUE_0=$L/a4l-excludes make research-render > $L/render-a4l.log 2>&1
python3 -c "
import json;t=open('$L/render-a4l.log').read();d=json.loads(t[t.index('{'):t.rindex('}')+1]);print('errors',d.get('errors'),'drift',d.get('source_drift'))"
git checkout HEAD -- theories/becoming/results/data/lean-index.json theories/becoming/results/LEAN-INDEX.md
python3 - <<'EOF'
import json,subprocess
M='_process/architecture/generated-manifest.json'
new=json.load(open(M)); old=json.loads(subprocess.run(['git','show','HEAD:'+M],capture_output=True,text=True).stdout)
for p in ['theories/becoming/results/data/lean-index.json','theories/becoming/results/LEAN-INDEX.md']:
    new['files'][p]=old['files'][p]
open(M,'w').write(json.dumps(new,ensure_ascii=False,indent=2)+'\n')
EOF
echo done receipt=$R correspondence=$C section=$N
