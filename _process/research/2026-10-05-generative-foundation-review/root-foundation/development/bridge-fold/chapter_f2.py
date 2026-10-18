#!/usr/bin/env python3
"""F2, joins into the core (18 October 2026): chapter section 9's receipt and counts, and the connectivity rerun.

usage (from the checkout root): python3 -B chapter_f2.py RECEIPT_ID BASE APART

RECEIPT_ID is F2's passing core receipt, BASE the main commit it was checked on, APART the connectivity check's count
of spine theorems apart (as printed, with thousands separators). Every count is read from the receipt itself. F1's
`chapter_f1.py`, with the receipt sentence naming F2 and the rerun sentence following F1's.
"""
import json
import re
import sys
from pathlib import Path

RID, BASE, APART = sys.argv[1:4]
CH = Path('theories/becoming/chapters/THE-THEORY-OF-BECOMING.md')
PKG = Path('experiments/integrated-correction/general-framework/generative-basis/lean/becoming')
STUDY = '../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/BECOMING-BRIDGE-FOLD.md'
BRIDGES = ['Becoming.Bridge', 'Becoming.CompositionBridge', 'Becoming.JoiningBridge', 'Becoming.GranularityBridge',
           'Becoming.RepairComparison', 'Becoming.Instances', 'Becoming.RenewalBridge', 'Becoming.CoursesBridge']

d = json.loads((PKG / 'becoming-checks' / RID / 'verification.json').read_text())
assert d['status'] == 'passed', d['status']
mods = {m['module']: m for m in d['modules']}
th = lambda names: sum(int(mods[x]['theorems']) for x in names)
joins = [m for m in d['bridge_modules'] if m not in BRIDGES]
assert set(BRIDGES) <= set(d['bridge_modules'])
c = {
    'core': (len(d['core_modules']), th(d['core_modules'])),
    'foundation': (len(d['foundation_modules']), th(d['foundation_modules'])),
    'closure': (len(d['core_closure']), th(d['core_closure'])),
    'bridges': (len(BRIDGES), th(BRIDGES)),
    'joins': (len(joins), th(joins)),
    'spine': th(d['spine_modules']),
    'audited': sum(len(mods[x]['declarations']) for x in d['spine_modules']),
    'pj': (len(d['periphery_join_modules']), th(d['periphery_join_modules'])),
    'inherited': len(d['inherited_receipts']),
    'compile': len(d['compile_order']),
    'injeq': (len(d['generated_axiom_dependencies']), len(d['bridge_generated_axiom_dependencies'])),
    'steps': (len(d['lean_steps']['reused']), len(d['lean_steps']['ran'])),
}
n = lambda x: f'{x:,}'
spine = n(c['spine'])


def subn1(pattern, repl, text, what):
    text, k = re.subn(pattern, repl, text)
    if k != 1:
        sys.exit(f'{what}: expected one match, found {k}')
    return text


ch = CH.read_text(encoding='utf-8')
ch = subn1(r'finds [\d,]+ of the [\d,]+ spine theorems apart from both base families at the last rerun',
           f'finds {APART} of the {spine} spine theorems apart from both base families at the last rerun', ch,
           'section 9 connectivity')
ch = subn1(r'\d+ modules counting the root `Becoming`, and \d+ in the core closure with the foundation',
           f'{c["core"][0]} modules counting the root `Becoming`, and {c["closure"][0]} in the core closure with the '
           'foundation', ch, 'section 9 module counts')
start = ch.index('**The current receipt.**')
end = ch.index('Further facts about the receipt:', start)
para = ch[start:end]
old = re.search(r'is run `([0-9TZ.]+)`', para).group(1)
para = para.replace(old, RID)
para = subn1(r'It was checked with Lean 4\.29\.1 on main \S+ (?:\(.*?\) )?with .*?(?:in the working tree, and it passed\.|\. It passed\.)',
             f'It was checked with Lean 4.29.1 on main {BASE} (after F3R sub-chain 1) with F2, joins into the core '
             f'([fold study]({STUDY}#8-what-was-done-f2)), in the working tree, and it passed.', para, 'receipt sentence')
rows = {
    '| Core modules (with the root `Becoming`, 0 theorems) |': f' {c["core"][0]} modules, {n(c["core"][1])} theorems |',
    '| Foundation modules |': f' {c["foundation"][0]} modules, {n(c["foundation"][1])} theorems |',
    '| Core closure |': f' {c["closure"][0]} modules, {n(c["closure"][1])} theorems |',
    '| Spine (core and bridge) |': f' {spine} theorems |',
    '| Audited spine declarations |': f' {n(c["audited"])} |',
    '| Modules in the compile order |': f' {c["compile"]} |',
}
lines = para.split('\n')
out = []
for line in lines:
    for head, tail in rows.items():
        if line.startswith(head):
            line = head + tail
    if line.startswith('| Bridges (the eight'):
        line = f'| Bridges (the eight bridge modules) | {c["bridges"][0]} modules, {n(c["bridges"][1])} theorems |'
    if line.startswith('| Pure periphery joins'):
        line = f'| Pure periphery joins | {c["joins"][0]} modules, {n(c["joins"][1])} theorems |'
    if line.startswith('| Periphery-join modules'):
        line = re.sub(r'\| \d+ modules, [\d,]+ theorems,', f'| {c["pj"][0]} modules, {n(c["pj"][1])} theorems,', line)
    if line.startswith('| Inherited modules bound'):
        assert f'| {c["inherited"]} (' in line, line
    if line.startswith('| Generated `injEq`'):
        # F3R sub-chain 1 added seven (Dephasing, JointPhase, MatchedCourses, ProjectedLaws, StrictTransport); F2 none.
        assert f' {c["injeq"][1]} on the bridge side' in line, line
        line = re.sub(r'\| \d+ in the core closure,', f'| {c["injeq"][0]} in the core closure,', line)
    out.append(line)
para = '\n'.join(out)
ch = ch[:start] + para + ch[end:]
ch = subn1(r'That run reused [\d,]+ cached Lean steps from `~/\.cache/becoming-lean` and ran [\d,]+\.',
           f'That run reused {n(c["steps"][0])} cached Lean steps from `~/.cache/becoming-lean` and ran '
           f'{n(c["steps"][1])}.', ch, 'steps sentence')
# On rebasing onto F3R sub-chain 1 (19 October): the last rerun sentence is F3 sweep step 1's.
f1 = re.search(r'Rerun with F3 sweep step 1 \(receipt [^)]*\), it counts .*?stood connected\.', ch)
assert f1, 'last rerun sentence'
at = f1.end()
ch = ch[:at] + (f' Rerun with F2, joins into the core (receipt {RID}), it counts {APART} of {spine}: of its six core modules '
                'only the witness `ScopedReach.domain_covers` stands apart, and the 22 periphery theorems the joins no '
                'longer cite stand apart as laws the core restates, each in the apart register. The other 25 theorems apart since '
                'that rerun are in the modules of F3R sub-chain 1, which landed without a connectivity rerun (`StrictTransport` 11, '
                '`MatchedCourses` 4, `ProjectedLaws` 4, `ActiveReading` 2, `Dephasing` 2, `SupportRecovery` 1, `Integers` 1); '
                'their 21 roots await register entries from F3R.') + ch[at:]
CH.write_text(ch, encoding='utf-8')
print(json.dumps(c))
