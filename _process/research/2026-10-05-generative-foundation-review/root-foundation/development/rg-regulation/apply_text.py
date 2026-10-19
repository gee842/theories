#!/usr/bin/env python3
"""RG (19 October 2026): canonical chapter (English and Chinese) and study text. Each edit must match exactly once;
every count is read from the checker log and the connectivity outputs, so the edit holds on whatever main it relands on.
usage (from the checkout root): python3 -B apply_text.py MAIN_COMMIT RECEIPT CONNECTIVITY_JSON BEFORE_JSON
The study section takes the next free number, counting the numbers board items have claimed; it is printed."""
import json
import re
import subprocess
import sys
from pathlib import Path

main_commit, RECEIPT, conn_path, before_path = sys.argv[1:5]
HERE = Path(__file__).resolve().parent
log = (HERE / 'checker-rg.log').read_text()
chk = json.loads(log[log.index('{'):log.rindex('}') + 1])
assert chk['status'] == 'passed'
conn = json.loads(Path(conn_path).read_text())
before = json.loads(Path(before_path).read_text())
n_mod = len(chk['spine_theorems'])
n_thm = sum(chk['spine_theorems'].values())
n_closure = len(chk['core_closure'])
apart = lambda c: c['classes']['apart: own vocabulary'] + c['classes']['apart: prelude-only statement']
APART, TOTAL = apart(conn), conn['spine_theorems']
B_APART, B_TOTAL = apart(before), before['spine_theorems']
assert TOTAL == n_thm, (TOTAL, n_thm)
assert not conn['apart_roots_unclassified'], conn['apart_roots_unclassified']
assert 'Becoming.Regulation' not in conn['apart_by_module'], conn['apart_by_module'].get('Becoming.Regulation')
COMPONENTS = conn['components']['count']
OUTSIDE = len(conn['components']['theorems_outside_the_main_component'])
BOTH = conn['classes']['statement on both families']
# Register entries that left: those at the base commit no longer in the register.
REG = '_process/research/2026-10-05-generative-foundation-review/root-foundation/THEOREM-CONNECTIVITY-APART.json'
base_reg = json.loads(subprocess.run(['git', 'show', f'{main_commit}:{REG}'], capture_output=True, text=True,
                                     check=True).stdout)['roots']
LEFT = sorted(set(base_reg) - set(json.loads(Path(REG).read_text())['roots']))
fmt = '{:,}'.format
C = Path('theories/becoming/chapters/THE-THEORY-OF-BECOMING.md')
CZ = Path('theories/becoming/chapters/THE-THEORY-OF-BECOMING.zh.md')
STUDY = Path('_process/research/2026-10-05-generative-foundation-review/root-foundation/BECOMING-RENEWAL-READING.md')
BOARD = Path('_process/BECOMING-WORKBOARD.md')
PKG_LINK = '../../../experiments/integrated-correction/general-framework/generative-basis/lean/becoming'

s = STUDY.read_text()
assert '(RG)\n' not in s, 'study section exists'
claimed = [int(x) for x in re.findall(r'study §(\d+)', BOARD.read_text())]
section = max([int(m.group(1)) for m in re.finditer(r'^## (\d+)\. ', s, re.M)] + claimed) + 1
SLUG = f'{section}-a-level-held-from-both-sides-and-a-level-read-late-rg'
STUDY_LINK = f'../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/BECOMING-RENEWAL-READING.md#{SLUG}'


def once(text, old, new):
    assert text.count(old) == 1, ('edit does not match once', old[:90], text.count(old))
    return text.replace(old, new)


t = C.read_text()
# Section 4: the paragraph after Pace's.
pace = [l for l in t.split('\n') if l.startswith('**How fast a rule may change** ([Becoming.Pace]')]
assert len(pace) == 1
t = once(t, pace[0] + '\n', pace[0] + '\n\n' + (HERE / 'chapter_section4.txt').read_text().rstrip('\n') + '\n')
# Section 4: constraint 7 of the account of social viability.
t = once(t, '| 7. Stability with adaptability | How fast a rule may change (`Becoming.Pace`, below). | Many levels and noisy '
            'rules are open. |',
         '| 7. Stability with adaptability | How fast a rule may change (`Becoming.Pace`, below); a level held from both '
         'sides settles where the response does not overshoot, and a rule reading `ℓ` steps late needs a band at least '
         '`2 (ℓ + 1) d` wide (`Becoming.Regulation`, below). | Many levels and noisy rules are open; so is one policy keeping '
         'a band from every start under late reading. |')
# Section 8.2: the collective-continuation row.
old = 'a pattern lasting through passing, `Becoming.Passing`;'
t = once(t, old, old + ' a level held from both sides and a level read late, `Becoming.Regulation`;')
t = once(t, 'homeostasis and carrying capacity stated as instances',
         'one policy keeping a band from every start under late reading, and several regulated levels lumped as one; '
         'homeostasis and carrying capacity stated as instances')
row = [l for l in t.split('\n') if l.startswith('| Collective continuation | ')]
assert len(row) == 1 and row[0].endswith(' |'), row
t = once(t, row[0] + '\n', row[0][:-2] + ', [two-sided-regulation-and-late-reading](../results/records/'
                            'two-sided-regulation-and-late-reading.md) |\n')
# Section 8.2: the integration row.
old = ' The two course worlds are two readings of one flow and one web, defined once.'
left = ('; ' + ', '.join(f'`{x.removeprefix("Becoming.")}`' for x in LEFT) + (' is' if len(LEFT) == 1 else ' are')
        + ' now used on the base and left the register') if LEFT else ''
t = once(t, old, f' Rerun with RG (receipt {RECEIPT}), it counts {APART} of {fmt(TOTAL)} ({B_APART} of '
         f'{fmt(B_TOTAL)} before), none in `Becoming.Regulation`, whose laws are stated on a flow and a web'
         f'{left} ([study section {section}]({STUDY_LINK})); {COMPONENTS} dependency components, {OUTSIDE} spine '
         f'theorems outside the main one, {BOTH} statements on both families.' + old)
# Section 9: the receipt and the counts.
m = re.search(r'The \[current receipt\]\([^)]*becoming-verification\.json\) is run `[^`]+`.*? in the working tree\.', t)
assert m and t.count(m.group(0)) == 1
t = t.replace(m.group(0),
              f'The [current receipt]({PKG_LINK}/becoming-verification.json) is run `{RECEIPT}`, frozen in '
              f'[`becoming-checks/{RECEIPT}/`]({PKG_LINK}/becoming-checks/{RECEIPT}/verification.json). It was checked '
              f'with Lean 4.29.1 on main {main_commit[:9]} with RG (`Becoming.Regulation`, '
              f'[study §{section}]({STUDY_LINK})) in the working tree.')
for pattern, new in [
        (r'\| Core modules \(with the root `Becoming`, 0 theorems\) \| [\d,]+ modules, [\d,]+ theorems \|',
         f'| Core modules (with the root `Becoming`, 0 theorems) | {n_mod} modules, {fmt(n_thm)} theorems |'),
        (r'\| Core closure \| [\d,]+ modules, [\d,]+ theorems \|',
         f'| Core closure | {n_closure} modules, {fmt(n_thm + 74)} theorems |'),
        (r'\| Spine \(the core; no bridge since the F3 sweep\) \| [\d,]+ theorems \|',
         f'| Spine (the core; no bridge since the F3 sweep) | {fmt(n_thm)} theorems |'),
        (r'\| Audited spine declarations \| [\d,]+ \|', f'| Audited spine declarations | {fmt(chk["spine_declaration_audits"])} |'),
        (r'\| Modules in the compile order \| [\d,]+ \|', f'| Modules in the compile order | {n_closure} |'),
        (r'- That run reused [\d,]+ cached Lean steps from `~/\.cache/becoming-lean` and ran \d+\.',
         f'- That run reused {fmt(chk["lean_steps_reused"])} cached Lean steps from `~/.cache/becoming-lean` and ran '
         f'{chk["lean_steps_run"]}.')]:
    found = re.findall(pattern, t)
    assert len(found) == 1, (pattern, found)
    t = re.sub(pattern, lambda _: new, t)
assert '| Foundation modules | 3 modules, 74 theorems |' in t
C.write_text(t)

z = CZ.read_text()
tol = [l for l in z.split('\n') if l.startswith('- **等待的阈值与恢复给出的律**（`Becoming.Tolerance`）')]
assert len(tol) == 1
z = once(z, tol[0] + '\n', tol[0] + '\n' + (HERE / 'chapter_section4.zh.txt').read_text().rstrip('\n') + '\n')
CZ.write_text(z)

body = (HERE / 'study_rg.txt').read_text()
receipt = json.loads(Path(f'experiments/integrated-correction/general-framework/generative-basis/lean/becoming/'
                          f'becoming-checks/{RECEIPT}/verification.json').read_text())
assert receipt['status'] == 'passed'
mod = next(m for m in receipt['modules'] if m['module'] == 'Becoming.Regulation')
assert not any(mod['axiom_dependencies'].values())
for key, value in (('{N}', str(section)), ('{RECEIPT}', RECEIPT), ('{APART}', str(APART)), ('{TOTAL}', fmt(TOTAL)),
                   ('{THMS}', str(chk['spine_theorems']['Becoming.Regulation'])),
                   ('{DECLS}', str(len(mod['declarations'])))):
    assert key in body, key
    body = body.replace(key, value)
assert not re.search(r'\{[A-Z_]+\}', body), 'placeholder left'
STUDY.write_text(s.rstrip('\n') + '\n\n' + body.rstrip('\n') + '\n')
print('section', section, 'apart', APART, 'of', TOTAL, 'before', B_APART, 'of', B_TOTAL, 'left the register', LEFT)
