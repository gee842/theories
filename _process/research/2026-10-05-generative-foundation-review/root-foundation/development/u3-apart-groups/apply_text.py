#!/usr/bin/env python3
"""U3/U4 (19 October 2026): chapter (English and Chinese) and study text. Each edit must match exactly once.
Every count is read from the checker log and the connectivity output, so the edit holds on whatever main it relands on.
usage (from the checkout root): python3 -B apply_text.py SECTION MAIN_COMMIT RECEIPT CONNECTIVITY_JSON"""
import json
import re
import sys
from pathlib import Path

section, main_commit, RECEIPT, conn_path = sys.argv[1:5]
HERE = Path(__file__).resolve().parent
log = (HERE / 'checker-u3.log').read_text()
chk = json.loads(log[log.index('{'):log.rindex('}') + 1])
assert chk['status'] == 'passed'
conn = json.loads(Path(conn_path).read_text())
n_mod = len(chk['spine_theorems'])
n_thm = sum(chk['spine_theorems'].values())
n_closure = len(chk['core_closure'])
APART = conn['classes']['apart: own vocabulary'] + conn['classes']['apart: prelude-only statement']
TOTAL = conn['spine_theorems']
assert TOTAL == n_thm, (TOTAL, n_thm)
REMOVED = len(conn['register_entries_not_apart_roots'])
COMPONENTS = conn['components']['count']
OUTSIDE = len(conn['components']['theorems_outside_the_main_component'])
BOTH = conn['classes']['statement on both families']
fmt = '{:,}'.format
C = Path('theories/becoming/chapters/THE-THEORY-OF-BECOMING.md')
CZ = Path('theories/becoming/chapters/THE-THEORY-OF-BECOMING.zh.md')
STUDY = Path('_process/research/2026-10-05-generative-foundation-review/root-foundation/BECOMING-RENEWAL-READING.md')
SLUG = f'{section}-theorems-apart-from-the-base-largest-groups-first-the-practical-commitments-in-the-core-u3-u4'
STUDY_LINK = f'../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/BECOMING-RENEWAL-READING.md#{SLUG}'
PKG_LINK = '../../../experiments/integrated-correction/general-framework/generative-basis/lean/becoming'


def once(text, old, new):
    assert text.count(old) == 1, ('edit does not match once', old[:90], text.count(old))
    return text.replace(old, new)


t = C.read_text()
t = once(t, '| `PracticalJudgment`, `BetterAt` (periphery; standard Lean axioms) | further commitments proposed by the AI, '
            'disclosed as conditions of the practical laws |',
         '| `Lexical.BasicPriority`, `Lexical.Frame.Above` (J1/J2), `Requirement.Frontier`, `Required` (J3/J4); read on a '
         'frame by `FrontierFrames.Priority` and `FrontierFrames.Options` (core; empty axiom reports) | further commitments '
         'proposed by the AI, disclosed as conditions of the practical laws. Where they need a classical principle it is a '
         'hypothesis with its calibration: a choice at every step needs weak excluded middle '
         '(`FrontierFrames.choice_exists_iff_weakly`, §8.6) |')
t = once(t, 'are stated by `Lexical.Frame.Above` (the bridge\'s `BetterAt` until the F3 sweep; [practical-judgment-g0-j]',
         'are stated by `Lexical.Frame.Above` (the bridge\'s `BetterAt` until the F3 sweep), and on a frame\'s steps by '
         '`FrontierFrames.Priority`, the options at a configuration being what one move reaches (`FrontierFrames.Options`): '
         'where one option keeps every basic claim any option realizes, keeping them is required of the choice where '
         'decided (`FrontierFrames.Priority.kept_required`) ([practical-judgment-g0-j]')
t = once(t, 'That is exactly weak excluded middle, ¬P ∨ ¬¬P for every P (`exists_undominated_iff_weakly`).',
         'That is exactly weak excluded middle, ¬P ∨ ¬¬P for every P (`exists_undominated_iff_weakly`). Read on frames, '
         'the options at a configuration being what one move reaches, it is the choice at every step: every comparison '
         'irreflexive and transitive on listed options leaves some option chosen exactly where every proposition is '
         'weakly decided (`FrontierFrames.choice_exists_iff_weakly`). What the need says about the unfolding: where '
         'whether one move betters another is open, a step need leave no move known to be chosen; the choice is found by '
         'settling, up to double negation, how the moves compare. This is the one classical step of the practical '
         'commitments as `PracticalJudgment` first proved them (`finite_frontier`).')
m = re.search(r'There are (\d+) dependency components, with (\d+) spine theorems outside the main one; (\d+) statements use both families\.', t)
assert m and t.count(m.group(0)) == 1
t = t.replace(m.group(0),
         'Rerun with U3 (receipt ' + RECEIPT + f'), it counts {APART} of {fmt(TOTAL)}, none in the four modules '
         '`Becoming.FrontierFrames`, `Becoming.FrontierWorlds`, `Becoming.AcceptanceFrames` and '
         '`Becoming.PresentationFrames`: the largest groups apart, taken by module, are read on the base, the practical '
         'commitments with the options of a step as what one move reaches, presentations with the questions as a frame\'s '
         'branching tests, listing with the list as what takes part in a step, and the received pairing of the hexagrams '
         f'through the law of waxing and waning; {REMOVED} apart roots are now used on the base and left the register. The '
         'rest stand apart as model witnesses, support lemmas, or general structure whose base reading is the next step, '
         f'each group\'s disposition in [study section {section}]({STUDY_LINK}). There are {COMPONENTS} dependency '
         f'components, with {OUTSIDE} spine theorems outside the main one; {BOTH} statements use both families.')
m = re.search(r'The \[current receipt\]\([^)]*becoming-verification\.json\) is run `[^`]+`.*? in the working tree\.', t)
assert m and t.count(m.group(0)) == 1
t = t.replace(m.group(0),
              f'The [current receipt]({PKG_LINK}/becoming-verification.json) is run `{RECEIPT}`, frozen in '
              f'[`becoming-checks/{RECEIPT}/`]({PKG_LINK}/becoming-checks/{RECEIPT}/verification.json). It was checked '
              f'with Lean 4.29.1 on main {main_commit} with U3 (`Becoming.FrontierFrames`, `Becoming.FrontierWorlds`, '
              '`Becoming.AcceptanceFrames`, `Becoming.PresentationFrames`, and new theorems in `Becoming.Hexagrams` and '
              f'`Becoming.Listing`, [study §{section}]({STUDY_LINK})) in the working tree.')
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
for old, new in [
                 ('| J1–J4 | the practical commitments | `PracticalJudgment`, `BetterAt` |',
                  '| J1–J4 | the practical commitments | `PracticalJudgment`, `BetterAt` (periphery, superseded); now '
                  '`Lexical.BasicPriority` and `Requirement.Frontier`, on frames `FrontierFrames.Priority` |')]:
    t = once(t, old, new)
C.write_text(t)

z = CZ.read_text()
z = once(z, '| `PracticalJudgment`、`BetterAt` | AI 提出的附加承诺，作为实践规律的条件公开 |',
         '| `Lexical.BasicPriority`、`Lexical.Frame.Above`（J1/J2），`Requirement.Frontier`、`Required`（J3/J4）；'
         '在框架上由 `FrontierFrames.Priority` 与 `FrontierFrames.Options` 读出（核心；公理报告为空） | AI 提出的附加承诺，'
         '作为实践规律的条件公开。需要经典原则之处，它是假设并附校准：每一步都有被选者需要弱排中律'
         '（`FrontierFrames.choice_exists_iff_weakly`，§8.6） |')
z = once(z, '| J1–J4 | 实践承诺 | `PracticalJudgment`、`BetterAt` |',
         '| J1–J4 | 实践承诺 | `PracticalJudgment`、`BetterAt`（外围，已被取代）；现为 `Lexical.BasicPriority` 与 '
         '`Requirement.Frontier`，在框架上为 `FrontierFrames.Priority` |')
CZ.write_text(z)

s = STUDY.read_text()
body = (HERE / 'study_u3.txt').read_text().replace('## 194.', f'## {section}.', 1)
for key, value in (('{RECEIPT}', RECEIPT), ('{APART}', str(APART)), ('{TOTAL}', fmt(TOTAL)),
                   ('{ROOTS_REMOVED}', str(REMOVED))):
    assert key in body, key
    body = body.replace(key, value)
assert not s.rstrip('\n').endswith(body.rstrip('\n'))
STUDY.write_text(s.rstrip('\n') + '\n\n' + body.rstrip('\n') + '\n')
print('applied')
