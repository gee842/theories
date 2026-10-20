#!/usr/bin/env python3
"""R25 replayed onto a main that moved while it waited (20 October 2026: R26, then R27 landed, each re-pointing
records, taking a study section and changing the board). Usage, from the checkout root on a clean tree at main:
python3 -B replay.py WORK BASE SECTION

WORK is the commit holding R25 on BASE (the main it was last replayed on). It applies R25's hand edits
(chapter en/zh, AGENTS.md, README lead, OPENING's footnote, DELEGATED-CHOICES, THEOREM-CONNECTIVITY.md, the Lean
README, research config, the history excerpt, the kit and the AGENTS before-copy) with a three-way merge; appends
R25's study section to main's study as SECTION, renumbering its anchor and every link to it; applies the three
records' corrected text (refs/salvage/r25-wip-records-text); and replays the board edits on main's board.
Records are then re-pointed by repoint_drift.py against main, after `make research-render`."""
import re, subprocess, sys
WORK, BASE, SEC = sys.argv[1], sys.argv[2], sys.argv[3]
RF = '_process/research/2026-10-05-generative-foundation-review/root-foundation/'
KIT = RF + 'development/r25-docs-now/'
S = RF + 'BECOMING-RENEWAL-READING.md'
B = '_process/BECOMING-WORKBOARD.md'
HB = '_process/history/workboard/BECOMING-WORKBOARD-2026-10-11_to_2026-10-17.md'
HAND = ['AGENTS.md', '_process/history/2026-10-20-instructions', '_process/navigation/README-LEAD.md',
        RF + 'DELEGATED-CHOICES.md', RF + 'DELEGATED-CHOICES.zh.md', RF + 'THEOREM-CONNECTIVITY.md', KIT,
        'experiments/integrated-correction/general-framework/generative-basis/lean/becoming/README.md',
        'theories/becoming/OPENING.md', 'theories/becoming/chapters/THE-THEORY-OF-BECOMING.md',
        'theories/becoming/chapters/THE-THEORY-OF-BECOMING.zh.md',
        'theories/becoming/history/THE-THEORY-OF-BECOMING-open-programme-2026-10-20.md', '_process/research-config.json']
REC = ['theories/becoming/results/records/' + r + '.json' for r in ('one-axiom-yields-g0', 'own-count-misses-joint-excess', 'reserve-defers-ending')]
def run(*a, inp=None):
    return subprocess.run(a, input=inp, capture_output=True, text=True, check=True).stdout
def show(rev, p):
    return run('git', 'show', f'{rev}:{p}')
patch = run('git', 'diff', '--binary', BASE, WORK, '--', *HAND)
subprocess.run(['git', 'apply', '-3', '--index'], input=patch, text=True, check=True)
rp = run('git', 'diff', 'refs/salvage/r25-wip-records-text~1', 'refs/salvage/r25-wip-records-text', '--', *REC)
subprocess.run(['git', 'apply', '-3', '--index'], input=rp, text=True, check=True)
run('git', 'reset', '-q')
# the study section
w = show(WORK, S)
m = re.search(r'<a id="(\d+)-r25-the-twentieth-reviews-step-1-docs-now"></a>\n## \d+\. R25', w)
old = m.group(1); sec = w[m.start():]
sec = sec.replace(f'<a id="{old}-r25-', f'<a id="{SEC}-r25-', 1).replace(f'## {old}. R25', f'## {SEC}. R25', 1)
s = open(S, encoding='utf-8').read()
assert f'## {SEC}.' not in s and 'R25: the twentieth review' not in s
open(S, 'w', encoding='utf-8').write(s.rstrip('\n') + '\n\n' + sec)
for p in ('theories/becoming/chapters/THE-THEORY-OF-BECOMING.md', 'theories/becoming/chapters/THE-THEORY-OF-BECOMING.zh.md'):
    t = open(p, encoding='utf-8').read()
    t, n = re.subn(r'(§|section )' + old + r'(\]\([^)]*#)' + old + '-r25-the-twentieth-reviews-step-1-docs-now',
                   r'\g<1>' + SEC + r'\g<2>' + SEC + '-r25-the-twentieth-reviews-step-1-docs-now', t)
    assert n == 3, (p, n); open(p, 'w', encoding='utf-8').write(t)
k = open(KIT + 'repoint_drift.py', encoding='utf-8').read()
k, n = re.subn(r"\('section \d+ added \(R25\); earlier sections unchanged', '新增第 \d+ 节（R25）；前面各节不变'\)",
              f"('section {SEC} added (R25); earlier sections unchanged', '新增第 {SEC} 节（R25）；前面各节不变')", k)
assert n == 1; open(KIT + 'repoint_drift.py', 'w', encoding='utf-8').write(k)
# the board: R25's row out of the open claims; its landed row (from WORK's history file) into main's history file
b = open(B, encoding='utf-8').read().split('\n')
i = [j for j, l in enumerate(b) if l.startswith("| **R25: the twentieth review's step 1, docs now**")]
assert len(i) == 1; b.pop(i[0]); b = '\n'.join(b)
wrow = [l for l in show(WORK, HB).split('\n') if l.startswith("| **R25: the twentieth review's step 1")]
assert len(wrow) == 1
row = re.sub(r'BECOMING-RENEWAL-READING\.md#\d+-r25-', f'BECOMING-RENEWAL-READING.md#{SEC}-r25-', wrow[0]).replace('[study §' + old + ']', '[study §' + SEC + ']')
row = row.replace("replayed on R23's and R26's landings", "replayed on R23's, R26's and R27's landings")
hl = open(HB, encoding='utf-8').read().split('\n')
j = [x for x, l in enumerate(hl) if l.startswith('| **R2') and 'landed' in l]
hl.insert(j[-1] + 1, row); open(HB, 'w', encoding='utf-8').write('\n'.join(hl))
# queue line, landing paragraph and the proposals, from WORK's board
wb = show(WORK, B)
q = re.search(r"- \*\*Queue:\*\* [^\n]*", b).group(0)
b = b.replace(q, "- **Queue:** empty; R25 landed (docs only; see the landing queue below).")
land = re.search(r"\): nothing is queued\.", b)
assert land
b = b[:land.start()] + "; R25, the twentieth review's step 1, landed, docs and records with no checker run, its row moved likewise" + b[land.start():]
props = re.search(r"Two proposals, from R25 .*?\n\nReadings: none since 19 October 2026\. ", wb, flags=re.S).group(0)
props = re.sub(r'BECOMING-RENEWAL-READING\.md#\d+-r25-', f'BECOMING-RENEWAL-READING.md#{SEC}-r25-', props).replace('[study §' + old + ']', '[study §' + SEC + ']')
o = "## Decisions pending Ren\n\nNone since 19 October 2026. "
assert b.count(o) == 1
b = b.replace(o, "## Decisions pending Ren\n\n" + props)
open(B, 'w', encoding='utf-8').write(b)
print('replayed', WORK, 'as section', SEC)
