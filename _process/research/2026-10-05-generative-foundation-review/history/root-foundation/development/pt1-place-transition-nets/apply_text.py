#!/usr/bin/env python3
"""Apply PT1's text to the shared pages of a landing checkout, after the core checker and the connectivity check:
  python3 -B apply_text.py RECEIPT MAIN CONNECTIVITY_LOG CHECKER_LOG
RECEIPT is the core run, MAIN the main commit it ran on, the two logs the outputs of THEOREM-CONNECTIVITY.py --check
and check_becoming.py. Writes the study section (the next free number, counting those other board items have claimed;
printed), the canonical chapter's section 8.7 bullet, its section 8.2 integration sentence and counts, and its section 9
counts and receipt. Each edit must match exactly once; run on a checkout that has none of them."""
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[5]
R, MAIN, CONN, CHECK = sys.argv[1], sys.argv[2], Path(sys.argv[3]), Path(sys.argv[4])
RF = ROOT / '_process/research/2026-10-05-generative-foundation-review/root-foundation'
STUDY = RF / 'BECOMING-RENEWAL-READING.md'
BOARD = ROOT / '_process/BECOMING-WORKBOARD.md'
CANON = ROOT / 'theories/becoming/chapters/THE-THEORY-OF-BECOMING.md'
PKG = 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming'
LEAN = f'../../../{PKG}/Becoming/PlaceTransitionNets.lean'
MODULE = 'Becoming.PlaceTransitionNets'
RECORD = '[place-transition-nets-on-the-spine](../results/records/place-transition-nets-on-the-spine.md)'


def once(text, old, new):
    assert text.count(old) == 1, ('edit does not match once', old[:100], text.count(old))
    return text.replace(old, new)


def number(n):
    return f'{n:,}'


receipt = json.loads((ROOT / PKG / 'becoming-checks' / R / 'verification.json').read_text())
assert receipt['status'] == 'passed'
ms = {m['module']: m for m in receipt['modules']}
core, found = receipt['core_modules'], receipt['foundation_modules']
core_thms = sum(ms[m]['theorems'] for m in core)
found_thms = sum(ms[m]['theorems'] for m in found)
audited = sum(len(ms[m]['declarations']) for m in receipt['spine_modules'])
mod = ms[MODULE]
assert not any(mod['axiom_dependencies'].values())
thms, decls_n = mod['theorems'], len(mod['declarations'])
generated = len(receipt['generated_axiom_dependencies'])
log = CHECK.read_text()
run = json.loads(log[log.index('{'):log.rindex('}') + 1])
assert run['status'] == 'passed'
ran, reused = run['lean_steps_run'], run['lean_steps_reused']
conn_text = CONN.read_text()
conn = json.loads(conn_text[conn_text.index('{'):conn_text.rindex('}') + 1])
assert not conn['apart_roots_unclassified'] and not conn['register_entries_not_apart_roots']
classes = conn['classes']
apart = sum(v for k, v in classes.items() if k.startswith('apart'))
total = sum(classes.values())
mod_apart = conn['apart_by_module'].get(MODULE, [0])[0]
assert mod_apart == 0, mod_apart
components = conn['components']['count']
outside = len(conn['components']['theorems_outside_the_main_component'])
both = sum(conn['statements_on_both_by_module'].values())

# The next free section number, counting what other board items have claimed.
board = BOARD.read_text()
study = STUDY.read_text()
assert 'Place/transition nets on the spine (PT1)' not in study
claimed_sections = [int(x) for x in re.findall(r'study §(\d+)', board)]
N = max([int(m.group(1)) for m in re.finditer(r'^## (\d+)\. ', study, re.M)] + claimed_sections) + 1
ANCHOR = f'#{N}-placetransition-nets-on-the-spine-pt1'

section = (HERE / 'study_pt1.txt').read_text().format(
    N=N, R=R, THMS=thms, DECLS=decls_n, APART=number(apart), TOTAL=number(total), MOD_APART=mod_apart,
    COMPONENTS=components, OUTSIDE=outside, BOTH=both)
STUDY.write_text(study.rstrip('\n') + '\n\n' + section)

canon = CANON.read_text()
PREMISES = [l for l in canon.split('\n') if l.startswith('- Whether actual unfoldings meet the premises:')]
assert len(PREMISES) == 1, PREMISES
canon = once(
    canon,
    PREMISES[0] + '\n',
    PREMISES[0] + '\n'
    f'- One standard formalism defined outside the theory meets the premises by its own definitions ([{MODULE}]({LEAN}), '
    f'{RECORD}). In a place/transition net (a Petri net, or a reaction network with whole-number counts) with finitely '
    'many places, balance is the firing rule: the net\'s flow balances its markings exactly along firing sequences '
    '(`Net.balances_iff`); activity needing support and only active transitions giving and taking hold by the '
    'definitions; enclosure is the net\'s finiteness; and dissipation holds exactly where every fired transition loses '
    'weighted tokens, a strict P-subinvariant (`Net.dissipative_iff`). Rising with falling, the bound of the consuming '
    'firings by the initial weighted tokens, rest unrefuted (`Net.rests_unrefuted`) and joint excess, as the law that an '
    'emptied place every producer of which consumes it stays empty (`Net.siphon_empty`), are then theorems of every such '
    'net; a conservative cycle, which loses nothing, never rests (`Net.cycle_never_rests`). Which actual systems are '
    'such nets, with which weights, is the correspondence that remains.\n')
COUNTS = re.compile(r'There are \d+ dependency components, with \d+ spine theorems outside the main one; \d+ statements '
                    r'use both families\.')
assert len(COUNTS.findall(canon)) == 1
canon = COUNTS.sub(
    f'Rerun with PT1 (receipt {R}), it counts {number(apart)} of {number(total)}, none in `{MODULE}`, whose laws are '
    f'stated on a net\'s flow, web and world. There are {components} dependency components, with {outside} spine '
    f'theorems outside the main one; {both} statements use both families.', canon)
modules = len(core)
closure = len(receipt['core_closure'])
canon, n = re.subn(r'four layers: \d+ modules counting the root `Becoming`, and \d+ in the core closure',
                   f'four layers: {modules} modules counting the root `Becoming`, and {closure} in the core closure', canon)
assert n == 1
start = canon.index('**The current receipt.**')
end = canon.index('\n', start)
canon = canon[:start] + (
    f'**The current receipt.** The [current receipt](../../../{PKG}/becoming-verification.json) is run `{R}`, frozen in '
    f'[`becoming-checks/{R}/`](../../../{PKG}/becoming-checks/{R}/verification.json). It was checked with Lean 4.29.1 '
    f'on main {MAIN[:9]} with PT1 (`{MODULE}`, [study §{N}](../../../_process/'
    f'research/2026-10-05-generative-foundation-review/root-foundation/BECOMING-RENEWAL-READING.md{ANCHOR})) in the '
    f'working tree. It passed. Its counts:') + canon[end:]
for pattern, value in (
        (r'\| Core modules \(with the root `Becoming`, 0 theorems\) \| [\d,]+ modules, [\d,]+ theorems \|',
         f'| Core modules (with the root `Becoming`, 0 theorems) | {modules} modules, {number(core_thms)} theorems |'),
        (r'\| Foundation modules \| \d+ modules, [\d,]+ theorems \|',
         f'| Foundation modules | {len(found)} modules, {number(found_thms)} theorems |'),
        (r'\| Core closure \| \d+ modules, [\d,]+ theorems \|',
         f'| Core closure | {closure} modules, {number(core_thms + found_thms)} theorems |'),
        (r'\| Spine \(the core; no bridge since the F3 sweep\) \| [\d,]+ theorems \|',
         f'| Spine (the core; no bridge since the F3 sweep) | {number(core_thms)} theorems |'),
        (r'\| Audited spine declarations \| [\d,]+ \|', f'| Audited spine declarations | {number(audited)} |'),
        (r'\| Modules in the compile order \| \d+ \|', f'| Modules in the compile order | {len(receipt["compile_order"])} |'),
        (r'\| Generated `injEq` lemmas on `propext` \| \d+ in the core closure \|',
         f'| Generated `injEq` lemmas on `propext` | {generated} in the core closure |'),
        (r'That run reused [\d,]+ cached Lean steps from `~/.cache/becoming-lean` and ran \d+\.',
         f'That run reused {number(reused)} cached Lean steps from `~/.cache/becoming-lean` and ran {ran}.')):
    canon, n = re.subn(pattern, value, canon)
    assert n == 1, pattern
CANON.write_text(canon)
print('study section', N, 'apart', apart, 'of', total, 'module', thms, decls_n)
