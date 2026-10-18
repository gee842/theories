#!/usr/bin/env python3
"""F3Q (19 October 2026): the chapter's section 8.2 connectivity sentence and section 9 receipt and counts for F3Q's
landing, read off the receipt and the connectivity summary.

usage (from the checkout root): python3 -B chapter_q.py RECEIPT_ID MAIN_SHA

Edits only text that the landing makes stale: the "Integration of the spine" row gains one rerun sentence; section 9's
pointer to the last rerun, the core ring's counts, the current receipt paragraph and its count table are restated.
"""
import json
import re
import sys

RID, MAIN = sys.argv[1:3]
C = 'theories/becoming/chapters/THE-THEORY-OF-BECOMING.md'
PKG = 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming/'
CONN = '_process/research/2026-10-05-generative-foundation-review/root-foundation/THEOREM-CONNECTIVITY.json'
NEW = ['PartialReadout', 'Derivation', 'CodeAcquisition', 'RouteFormation', 'ResponseLearning', 'LearnedGrouping']
B8 = ['Becoming.Bridge', 'Becoming.CompositionBridge', 'Becoming.JoiningBridge', 'Becoming.GranularityBridge',
      'Becoming.RepairComparison', 'Becoming.Instances', 'Becoming.RenewalBridge', 'Becoming.CoursesBridge']

d = json.load(open(f'{PKG}becoming-checks/{RID}/verification.json'))
assert d['status'] == 'passed'
mods = {x['module']: x for x in d['modules']}
T = lambda ms: sum(mods[x]['theorems'] for x in ms)
D = lambda ms: sum((v if isinstance(v, int) else len(v)) for v in (mods[x]['declarations'] for x in ms))
bridge8 = [m for m in d['bridge_modules'] if m in B8]
pure = [m for m in d['bridge_modules'] if m not in B8]
n = lambda x: f'{x:,}'
conn = json.load(open(CONN))
apart = sum(v for k, v in conn['classes'].items() if k.startswith('apart'))
spine = conn['spine_theorems']
assert spine == T(d['spine_modules']), (spine, T(d['spine_modules']))
mine = {m: conn['apart_by_module'].get('Becoming.' + m, [0, 0])[0] for m in NEW}
new_th = sum(mods['Becoming.' + m]['theorems'] for m in NEW)

ch = open(C, encoding='utf-8').read()


def sub(old, new, count=1):
    global ch
    assert ch.count(old) == count, (old[:80], ch.count(old))
    ch = ch.replace(old, new)


# section 8.2, Integration of the spine: one rerun sentence after F3R sub-chain 2's
anchor = ('Rerun with F3R sub-chain 2 (receipt 20261018T203356.753598Z), none of the seven theorems of '
          '`Becoming.ActivationCapacity` stands apart, and the apart count is unchanged.')
parts = ', '.join(f'`{m}` {k}' for m, k in mine.items() if k)
sub(anchor, anchor + f' Rerun with F3Q, the port of the inquiry and composition family (receipt {RID}), it counts '
    f'{n(apart)} of {n(spine)}: {sum(mine.values())} of the {new_th} theorems of its six core modules stand apart '
    f'({parts}), the facts of its constructed examples (the channel, the codes, the Bool countermodel, the supplied '
    f'logs), the evaluation lemmas of its own grammar, and the two whole-domain equivalences of `PartialReadout` with '
    f'`Readout` and `Learning`; their 32 roots are in the apart register under the categories of their periphery '
    f'counterparts.')

# section 9: the last rerun, the core ring, the current receipt and its counts
ch, k = re.subn(r'finds [0-9,]+ of the [0-9,]+ spine theorems apart from both base families at the last rerun',
                f'finds {n(apart)} of the {n(spine)} spine theorems apart from both base families at the last rerun', ch)
assert k == 1
ch, k = re.subn(r'(with the package\'s base and four layers: )[0-9,]+( modules counting the root `Becoming`, and )[0-9,]+'
                r'( in the core closure with the foundation\.)',
                lambda m: f'{m[1]}{len(d["core_modules"])}{m[2]}{len(d["core_closure"])}{m[3]}', ch)
assert k == 1
i = ch.index('**The current receipt.**')
j = ch.index('Its counts:', i)
ch = ch[:i] + (
    f'**The current receipt.** The [current receipt](../../../{PKG}becoming-verification.json) is run `{RID}`, frozen in '
    f'[`becoming-checks/{RID}/`](../../../{PKG}becoming-checks/{RID}/verification.json). It was checked with Lean 4.29.1 '
    f'on main {MAIN} (after F3R sub-chain 2, `Becoming.ActivationCapacity`) with F3Q, the inquiry and composition family '
    f'(`Becoming.PartialReadout`, `Derivation`, `CodeAcquisition`, `RouteFormation`, `ResponseLearning` and '
    f'`LearnedGrouping`, [verdicts](../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/'
    f'development/bridge-fold/port-q.md)) in the working tree, and it passed. ') + ch[j:]
rows = {
    'Core modules (with the root `Becoming`, 0 theorems)': f'{len(d["core_modules"])} modules, {n(T(d["core_modules"]))} theorems',
    'Core closure': f'{len(d["core_closure"])} modules, {n(T(d["core_closure"]))} theorems',
    'Bridges (the eight bridge modules)': f'{len(bridge8)} modules, {n(T(bridge8))} theorems',
    'Pure periphery joins': f'{len(pure)} modules, {n(T(pure))} theorems',
    'Spine (core and bridge)': f'{n(T(d["spine_modules"]))} theorems',
    'Audited spine declarations': n(D(d['spine_modules'])),
    'Modules in the compile order': str(len(d['compile_order'])),
}
for what, count in rows.items():
    ch, k = re.subn(r'^(\| ' + re.escape(what) + r' \| )[^|]+( \|)$', lambda m: m[1] + count + m[2], ch, flags=re.M)
    assert k == 1, what
ch, k = re.subn(r'(\| Generated `injEq` lemmas on `propext` \| )[0-9]+( in the core closure, )[0-9]+( on the bridge side)',
                lambda m: f'{m[1]}{len(d["generated_axiom_dependencies"])}{m[2]}{len(d["bridge_generated_axiom_dependencies"])}{m[3]}', ch)
assert k == 1
ls = d['lean_steps']
ch, k = re.subn(r'That run reused [0-9,]+ cached Lean steps from `~/.cache/becoming-lean` and ran [0-9,]+\.',
                f'That run reused {n(len(ls["reused"]))} cached Lean steps from `~/.cache/becoming-lean` and ran '
                f'{n(len(ls["ran"]))}.', ch)
assert k == 1
assert list(d['market_names']) == ['Becoming.Flow.Balances.rise_paid_from_beyond'], d['market_names']
assert len(d['not_audited_by_name']) == 9, list(d['not_audited_by_name'])
open(C, 'w', encoding='utf-8').write(ch)
print('apart', apart, 'of', spine, mine, 'core', len(d['core_modules']), T(d['core_modules']))
