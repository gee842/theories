#!/bin/zsh
# X1b relanding (19 October 2026), docs and records only. Run from the worktree root after `git rebase main` has finished, with any
# conflict in generated views or records resolved to main's version. Regenerates the views, re-points the records that
# drift only in sections 1 and 10 of the chapter or section 199 of the renewal study (X1b's changes there were read
# before writing the note), regenerates again and runs the gates. usage: zsh reland_x1b.sh SCRATCH_DIR
set -e
S=$1
K=_process/research/2026-10-05-generative-foundation-review/root-foundation/development/x1-closing-opening
render() { make research-render > $S/x1b-render.log 2>&1 || true }
drift() { python3 -c "
import json;t=open('$S/x1b-render.log').read();d=json.loads(t[t.index('{'):t.rindex('}')+1])
assert not d.get('errors'), d['errors']
assert not d.get('unrelated_source_drift'), d['unrelated_source_drift']
ok={'THE-THEORY-OF-BECOMING.md':{'## 1. Becoming: one unfolding','## 10. Glossary'},'BECOMING-RENEWAL-READING.md':{'## 199. Junctures, what a commuting law keeps apart, and the third value (SG)'}}
bad=[x for x in d.get('source_drift',[]) if not set(x['changed_sections'])<=ok.get(x['path'].rsplit('/',1)[-1],set())]
assert not bad, bad
print(' '.join(sorted({x['id']+':'+x['path'].rsplit('/',1)[-1] for x in d.get('source_drift',[])})))" }
render
IDS=$(drift)
if [[ -n "$IDS" ]]; then python3 -B $K/repoint_x1b.py ${=IDS}; render; fi
[[ -z "$(drift)" ]] || { echo 'drift remains'; exit 1 }
make research-check > $S/x1b-check.log 2>&1 || { echo 'check failed'; exit 1 }; echo check ok
make research-links > $S/x1b-links.log 2>&1 || { echo 'links failed'; exit 1 }; echo links ok
make research-test > $S/x1b-test.log 2>&1 || { echo 'test failed'; exit 1 }; echo test ok
git status --short
