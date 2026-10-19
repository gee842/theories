#!/bin/bash
# Dry run of Y3's landing on the worktree's current tree, with a stand-in receipt (20991231T000000.000000Z) built
# from the latest real one plus the scratch module's declarations, and stand-in connectivity and checker logs.
# Nothing is committed; revert afterwards with: git checkout HEAD -- <changed files> and remove the untracked outputs
# (the package copy of HexagramLaws.lean, the stand-in receipt, the new record). usage: bash dry_run.sh OUT_DIR
set -euo pipefail
OUT=$1
ROOT=$(git rev-parse --show-toplevel)
cd "$ROOT"
K=_process/research/2026-10-05-generative-foundation-review/root-foundation/development/y1-changes/y3
Y2K=_process/research/2026-10-05-generative-foundation-review/root-foundation/development/y1-changes/y2
PKG=experiments/integrated-correction/general-framework/generative-basis/lean/becoming
mkdir -p "$OUT"
python3 -B $K/integrate.py
if [ -f $PKG/Becoming/Commuting.lean ]; then python3 -B $K/cite_commuting.py $PKG/Becoming/HexagramLaws.lean; fi
python3 -B $K/add_passages.py > "$OUT/add_passages.log"
python3 -B $K/register_apart.py > "$OUT/register_apart.log"
PKG=$PKG python3 - <<'EOF'
import copy, hashlib, json, os, sys
from pathlib import Path
pkg = Path(os.environ['PKG'])
sys.path.insert(0, str(pkg))
import check_becoming as cb
real = sorted((pkg / 'becoming-checks').glob('2026*/verification.json'))[-1]
r = json.loads(real.read_text())
src = (pkg / 'Becoming/HexagramLaws.lean').read_bytes()
ds = cb.declarations(src)
m = copy.deepcopy(next(x for x in r['modules'] if x['module'] == 'Becoming.HexagramPlaces'))
m.update(module='Becoming.HexagramLaws', declarations=[{'name': d['name'], 'kind': d['kind']} for d in ds],
         theorems=sum(d['kind'] == 'theorem' for d in ds), axiom_dependencies={d['name']: [] for d in ds})
r['modules'].append(m)
for key in ('core_modules', 'spine_modules', 'core_closure', 'compile_order'):
    r[key].append('Becoming.HexagramLaws')
for p in pkg.glob('Becoming/*.lean'):
    if f'Becoming.{p.stem}' in r['source_sha256']:
        r['source_sha256'][f'Becoming.{p.stem}'] = hashlib.sha256(p.read_bytes()).hexdigest()
r['source_sha256']['Becoming.HexagramLaws'] = hashlib.sha256(src).hexdigest()
out = pkg / 'becoming-checks/20991231T000000.000000Z'
out.mkdir()
(out / 'verification.json').write_text(json.dumps(r))
print('stand-in receipt from', real, m['theorems'], len(ds))
EOF
python3 -c "
import json
t = open('$Y2K/conn-3.log').read(); c = json.loads(t[t.index('{'):t.rindex('}') + 1])
c['apart_by_module']['Becoming.HexagramLaws'] = [13, 132]
open('$OUT/fake-conn.log', 'w').write(json.dumps(c))
"
cp $Y2K/checker-y2b.log "$OUT/fake-check.log"
python3 -B $K/apply_text.py 20991231T000000.000000Z "$(git rev-parse HEAD)" "$OUT/fake-conn.log" "$OUT/fake-check.log" \
  > "$OUT/apply_text.log"
read -r N DN < <(tail -1 "$OUT/apply_text.log")
python3 -B $K/make_record.py 20991231T000000.000000Z "$N" "$DN" > "$OUT/make_record.log"
python3 -B $K/rehash_refs.py HEAD > "$OUT/rehash.log"
for gate in research-render research-check research-check-strict research-links research-test research-secrets; do
  if make $gate > "$OUT/$gate.log" 2>&1; then echo "$gate ok"; else echo "$gate FAILED"; fi
done
