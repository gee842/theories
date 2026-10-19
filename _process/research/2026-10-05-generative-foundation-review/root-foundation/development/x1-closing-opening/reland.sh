#!/bin/zsh
# X1 relanding (19 October 2026), docs only. Run from the worktree root after `git rebase main` has finished, with any
# conflict in generated views or records resolved to main's version. Regenerates the views, re-points the records that
# drift only in sections 8 and 10 of the chapter (X1's changes there were read before writing the note), regenerates
# again and runs the gates. usage: zsh reland.sh SCRATCH_DIR
set -e
S=$1
K=_process/research/2026-10-05-generative-foundation-review/root-foundation/development/x1-closing-opening
render() { make research-render > $S/x1-render.log 2>&1 || true }
drift() { python3 -c "
import json;t=open('$S/x1-render.log').read();d=json.loads(t[t.index('{'):t.rindex('}')+1])
assert not d.get('errors'), d['errors']
assert not d.get('unrelated_source_drift'), d['unrelated_source_drift']
ok={'## 8. Open programme','## 10. Glossary'}
bad=[x for x in d.get('source_drift',[]) if not set(x['changed_sections'])<=ok or not x['path'].endswith('THE-THEORY-OF-BECOMING.md')]
assert not bad, bad
print(' '.join(sorted({x['id'] for x in d.get('source_drift',[])})))" }
render
IDS=$(drift)
if [[ -n "$IDS" ]]; then python3 -B $K/repoint_drift.py ${=IDS}; render; fi
[[ -z "$(drift)" ]] || { echo 'drift remains'; exit 1 }
make research-check > $S/x1-check.log 2>&1 && echo check ok
make research-links > $S/x1-links.log 2>&1 && echo links ok
make research-test > $S/x1-test.log 2>&1 && echo test ok
git status --short
