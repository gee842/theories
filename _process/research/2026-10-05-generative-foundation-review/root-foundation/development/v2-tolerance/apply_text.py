#!/usr/bin/env python3
"""V2 landing text: study section 194, chapter §4 (en, zh), §8.2 row, §9 receipt and connectivity, the board row moved
to the history file, and the queue sentence. Every edit must match exactly once.

usage (from the checkout root to edit): python3 -B apply_text.py RECEIPT BASE CONNECTIVITY_LOG
RECEIPT is the core checker run, BASE the main commit it ran on, CONNECTIVITY_LOG the --check output on the
landing tree. The §9 counts are read from the receipt."""
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = Path.cwd()
PKG = 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming'
STUDY = '_process/research/2026-10-05-generative-foundation-review/root-foundation/BECOMING-RENEWAL-READING.md'
CH = 'theories/becoming/chapters/THE-THEORY-OF-BECOMING.md'
CHZ = 'theories/becoming/chapters/THE-THEORY-OF-BECOMING.zh.md'
BOARD = '_process/BECOMING-WORKBOARD.md'
HISTORY = '_process/history/workboard/BECOMING-WORKBOARD-2026-10-11_to_2026-10-17.md'
MOD = 'Becoming.Tolerance'
receipt_id, base, conn_log = sys.argv[1], sys.argv[2], sys.argv[3]


def edit(path, pairs):
    p = ROOT / path
    text = p.read_text(encoding='utf-8')
    for old, new in pairs:
        k = text.count(old)
        if k != 1:
            sys.exit(f'{path}: expected one match, found {k}: {old[:100]!r}')
        text = text.replace(old, new)
    p.write_text(text, encoding='utf-8')
    print('edited', path, len(pairs))


rec = json.loads((ROOT / PKG / 'becoming-checks' / receipt_id / 'verification.json').read_text())
core = [m for m in rec['modules'] if m['layer'] == 'core']
assert rec['status'] == 'passed' and rec['core_compiles_from_prelude'] and rec['source_unchanged_during_check']
assert not any(v for m in core for v in m['axiom_dependencies'].values())
spine = {m['module']: m['theorems'] for m in core}
mod = next(m for m in core if m['module'] == MOD)
n_mod_thm, n_mod_decl = mod['theorems'], len(mod['declarations'])
n_mod = len(rec['core_modules'])
n_thm = sum(spine.values())
closure = len(rec['core_closure'])
assert closure == len(rec['compile_order'])
audits = sum(len(m['declarations']) for m in rec['modules'] if m['spine'])
inj = len(rec['generated_axiom_dependencies'])
ran, reused = len(rec['lean_steps']['ran']), len(rec['lean_steps']['reused'])
t = (ROOT / conn_log).read_text() if not conn_log.startswith('/') else Path(conn_log).read_text()
conn = json.loads(t[t.index('{'):t.rindex('}') + 1])
apart = sum(v for k, v in conn['classes'].items() if k.startswith('apart'))
assert conn['spine_theorems'] == n_thm, (conn['spine_theorems'], n_thm)
assert MOD not in conn['apart_by_module']
comps = conn['components']['count']
outside = len(conn['components']['theorems_outside_the_main_component'])
both = conn['classes']['statement on both families']
fmt = lambda n: f'{n:,}'

# Study section 194.
study = (HERE / 'study_v2.txt').read_text(encoding='utf-8')
study = (study.replace('{RECEIPT}', receipt_id).replace('{THEOREMS}', str(n_mod_thm)).replace('{DECLS}', str(n_mod_decl))
         .replace('{APART}', f'{apart} apart of {fmt(n_thm)}, none in the module;\n'
                             '          FaultEnvelopes.availability_iff_separated and correlated_three_blocks, registered\n'
                             '          apart, are now used on the base and leave the register'))
stext = (ROOT / STUDY).read_text(encoding='utf-8')
assert re.search(r'^## 193\. ', stext, re.M) and not re.search(r'^## 194\. ', stext, re.M)
(ROOT / STUDY).write_text(stext.rstrip('\n') + '\n\n' + study.rstrip('\n') + '\n', encoding='utf-8')
print('appended', STUDY)

# Chapter, English.
sec4 = (HERE / 'chapter_section4.txt').read_text(encoding='utf-8').strip('\n')
ANCHOR4 = ('no course of the law with memory regains giving (`waitsAll_gives_earlier`).\n')
OLDROW4 = ('| 4. Cooperation among strangers | Giving that waits on giving (`Becoming.Withholding`, below). | '
           'Amounts of giving and thresholds of waiting are open. |')
NEWROW4 = ('| 4. Cooperation among strangers | Giving that waits on giving (`Becoming.Withholding`, below); thresholds of '
           'waiting and the laws that restore giving (`Becoming.Tolerance`, below). | Amounts of giving, thresholds with '
           'memory, and how a restoring law forms are open. |')
OLDCOOP = ('Kept promises, enforced contracts and institutions that act whatever was last received are read as such laws. '
           'The law changes; the state alone does not.')
NEWCOOP = (OLDCOOP + ' Tolerance absorbs a scattered withholding and restores none that is total; a restoring law '
           'restores exactly where every long enough chain of reliance passes a formation giving first '
           '(`Becoming.Tolerance`, below).')
OLD82 = ('| Collective continuation | (Stated: giving that waits on giving, `Becoming.Withholding`; whether a loop closes, '
         'keeps or widens a difference, `Becoming.Widening`; how fast a rule may change, `Becoming.Pace`; a pattern lasting '
         'through passing, `Becoming.Passing`; conditions kept together and keeping a part, `Becoming.JointKeeping`; §4.) '
         'Amounts of giving and thresholds of waiting (a formation giving where at least `k` of what it waits on gave); '
         'which laws that give first restore giving in a general family, and how such a law forms; a loop with real '
         'strengths, where a multiplication below one closes gradually; many levels of rule and rules that change by '
         'chance; passing derived from descent (`Flow.DescendsAt`) rather than supplied; joint keeping over a horizon with '
         'the choices given by a law of exchange; homeostasis, carrying capacity and fault tolerance stated as instances '
         '(the last joined to `Becoming.FaultEnvelopes`). | ')
NEW82 = ('| Collective continuation | (Stated: giving that waits on giving, `Becoming.Withholding`; thresholds of waiting, '
         'the worst start for restoring and restoring under a law giving first, with fault tolerance as the tolerating '
         'law and as the certificate law of `Becoming.FaultEnvelopes`, `Becoming.Tolerance`; whether a loop closes, '
         'keeps or widens a difference, `Becoming.Widening`; how fast a rule may change, `Becoming.Pace`; a pattern lasting '
         'through passing, `Becoming.Passing`; conditions kept together and keeping a part, `Becoming.JointKeeping`; §4.) '
         'Amounts of giving and thresholds with memory; how a law that tolerates or gives first forms; a loop with real '
         'strengths, where a multiplication below one closes gradually; many levels of rule and rules that change by '
         'chance; passing derived from descent (`Flow.DescendsAt`) rather than supplied; joint keeping over a horizon with '
         'the choices given by a law of exchange; homeostasis and carrying capacity stated as instances. | ')
OLD82R = '[giving-that-waits-on-giving](../results/records/giving-that-waits-on-giving.md), [whether-a-loop'
NEW82R = ('[giving-that-waits-on-giving](../results/records/giving-that-waits-on-giving.md), '
          '[restoring-giving-from-the-worst-start](../results/records/restoring-giving-from-the-worst-start.md), '
          '[thresholds-of-waiting](../results/records/thresholds-of-waiting.md), [whether-a-loop')
ch = (ROOT / CH).read_text(encoding='utf-8')
m = re.search(r' There are (\d+) dependency components, with (\d+) spine theorems outside the main one; (\d+) statements use both families\.', ch)
assert m, 'components sentence'
OLDINT = m.group(0)
NEWINT = (f' Rerun with V2 (receipt {receipt_id}), it counts {apart} of {fmt(n_thm)}, none in `Becoming.Tolerance`, whose '
          'main laws are stated on runs of the spine (`Law.run`); `FaultEnvelopes.availability_iff_separated` and '
          '`FaultEnvelopes.correlated_three_blocks`, registered apart, are now used on the base by `Becoming.Tolerance` '
          f'and leave the register. There are {comps} dependency components, with {outside} spine theorems outside the '
          f'main one; {both} statements use both families.')
m = re.search(r'\*\*The current receipt\.\*\* The \[current receipt\]\([^)]*\) is run `([^`]+)`, frozen in .*?It passed\. Its counts:', ch, re.S)
assert m and '\n' not in m.group(0), 'receipt sentence'
NEWREC = (f'**The current receipt.** The [current receipt](../../../{PKG}/becoming-verification.json) is run '
          f'`{receipt_id}`, frozen in [`becoming-checks/{receipt_id}/`](../../../{PKG}/becoming-checks/{receipt_id}/'
          f'verification.json). It was checked with Lean 4.29.1 on main {base} (after V2\'s board claim) with V2 '
          '(`Becoming.Tolerance`, [study §194](../../../_process/research/2026-10-05-generative-foundation-review/'
          'root-foundation/BECOMING-RENEWAL-READING.md#194-thresholds-of-waiting-and-the-laws-that-restore-giving-v2)) in '
          'the working tree. It passed. Its counts:')
table = re.search(r'\| Core modules \(with the root `Becoming`, 0 theorems\) \| (\d+) modules, ([\d,]+) theorems \|\n'
                  r'\| Foundation modules \| 3 modules, 74 theorems \|\n'
                  r'\| Core closure \| (\d+) modules, ([\d,]+) theorems \|\n'
                  r'\| Spine \(the core; no bridge since the F3 sweep\) \| ([\d,]+) theorems \|\n'
                  r'\| Audited spine declarations \| ([\d,]+) \|\n', ch)
assert table, 'counts table'
NEWTABLE = (f'| Core modules (with the root `Becoming`, 0 theorems) | {n_mod} modules, {fmt(n_thm)} theorems |\n'
            '| Foundation modules | 3 modules, 74 theorems |\n'
            f'| Core closure | {closure} modules, {fmt(n_thm + 74)} theorems |\n'
            f'| Spine (the core; no bridge since the F3 sweep) | {fmt(n_thm)} theorems |\n'
            f'| Audited spine declarations | {fmt(audits)} |\n')
mo = re.search(r'\| Modules in the compile order \| (\d+) \|\n\| Generated `injEq` lemmas on `propext` \| (\d+) in the core closure \|', ch)
assert mo, 'compile order'
NEWMO = f'| Modules in the compile order | {closure} |\n| Generated `injEq` lemmas on `propext` | {inj} in the core closure |'
mr = re.search(r'That run reused ([\d,]+) cached Lean steps from `~/.cache/becoming-lean` and ran (\d+)\.', ch)
assert mr, 'reuse sentence'
NEWR = f'That run reused {fmt(reused)} cached Lean steps from `~/.cache/becoming-lean` and ran {ran}.'
edit(CH, [(ANCHOR4, ANCHOR4 + '\n' + sec4 + '\n'), (OLDROW4, NEWROW4), (OLDCOOP, NEWCOOP), (OLD82, NEW82),
          (OLD82R, NEW82R), (OLDINT, NEWINT), (m.group(0), NEWREC), (table.group(0), NEWTABLE), (mo.group(0), NEWMO),
          (mr.group(0), NEWR)])

# Chapter, Chinese edition: a bullet after the bullet of the four gaps.
secz = (HERE / 'chapter_section4.zh.txt').read_text(encoding='utf-8').strip('\n')
ANCHORZ = '一步无承载者即此后再无，传递停止则在一个跨度内结束（`Web.ByPassing.ends_within`）。\n'
edit(CHZ, [(ANCHORZ, ANCHORZ + secz + '\n')])

# Board: the row moves to the history file; the queue sentence names the landing.
board = (ROOT / BOARD).read_text(encoding='utf-8')
history = (ROOT / HISTORY).read_text(encoding='utf-8')
lines = board.split('\n')
rows = [i for i, line in enumerate(lines) if line.startswith('| **V2: thresholds of waiting and the laws that restore giving**')]
assert len(rows) == 1, rows
row = lines.pop(rows[0])
cells = row.split(' | ')
assert len(cells) == 5, len(cells)
cells[2] = (f'landed 2026-10-19, core receipt `{receipt_id}`; {n_mod_thm} theorems in one core module, empty axiom '
            'reports; records restoring-giving-from-the-worst-start, thresholds-of-waiting; study §194')
row = ' | '.join(cells).replace('](../', '](../../../').replace('](research/', '](../../research/')
hist = history.split('\n')
stop = next((i for i, line in enumerate(hist) if line.startswith('## Lapsed claims')), len(hist))
last = max(i for i, line in enumerate(hist[:stop]) if line.startswith('| **'))
hist.insert(last + 1, row)
board = '\n'.join(lines)
OLDQ = 'V landed, core receipt `20261019T064004.300228Z`, ahead of W2): W2 ('
assert board.count(OLDQ) == 1, 'queue sentence'
board = board.replace(OLDQ, 'V landed, core receipt `20261019T064004.300228Z`, ahead of W2; '
                      f'V2 landed, core receipt `{receipt_id}`, ahead of W2): W2 (')
(ROOT / BOARD).write_text(board, encoding='utf-8')
(ROOT / HISTORY).write_text('\n'.join(hist), encoding='utf-8')
print('board row moved; receipt', receipt_id, 'apart', apart, 'theorems', n_thm, 'modules', n_mod, 'closure', closure)
