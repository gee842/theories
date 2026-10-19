#!/usr/bin/env python3
"""V landing text: study section 193, D48 (en, zh), chapter §4 (en, zh), §7.7, §8.2 rows, §9 receipt, the
board row moved to the history file, and the queue sentence. Every edit must match exactly once.

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
DC = '_process/research/2026-10-05-generative-foundation-review/root-foundation/DELEGATED-CHOICES.md'
DCZ = '_process/research/2026-10-05-generative-foundation-review/root-foundation/DELEGATED-CHOICES.zh.md'
CH = 'theories/becoming/chapters/THE-THEORY-OF-BECOMING.md'
CHZ = 'theories/becoming/chapters/THE-THEORY-OF-BECOMING.zh.md'
BOARD = '_process/BECOMING-WORKBOARD.md'
HISTORY = '_process/history/workboard/BECOMING-WORKBOARD-2026-10-11_to_2026-10-17.md'
MODS = ['Withholding', 'Widening', 'Pace', 'Passing', 'JointKeeping']
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


def append(path, addition):
    p = ROOT / path
    text = p.read_text(encoding='utf-8')
    assert addition.strip()[:60] not in text, ('already applied', path)
    p.write_text(text.rstrip('\n') + '\n' + addition.rstrip('\n') + '\n', encoding='utf-8')
    print('appended', path)


rec = json.loads((ROOT / PKG / 'becoming-checks' / receipt_id / 'verification.json').read_text())
core = [m for m in rec['modules'] if m['layer'] == 'core']
assert rec['status'] == 'passed' and rec['core_compiles_from_prelude'] and rec['source_unchanged_during_check']
assert not any(v for m in core for v in m['axiom_dependencies'].values())
spine = {m['module']: m['theorems'] for m in core}
n_mod = len(rec['core_modules'])         # core modules with the root
n_thm = sum(spine.values())
found = sum(spine[f'Becoming.{m}'] for m in MODS)
assert found == 157, found
closure = len(rec['core_closure'])
assert closure == len(rec['compile_order'])
audits = sum(len(m['declarations']) for m in rec['modules'] if m['spine'])
inj = len(rec['generated_axiom_dependencies'])
ran, reused = len(rec['lean_steps']['ran']), len(rec['lean_steps']['reused'])
t = (ROOT / conn_log).read_text() if not conn_log.startswith('/') else Path(conn_log).read_text()
conn = json.loads(t[t.index('{'):t.rindex('}') + 1])
apart = sum(v for k, v in conn['classes'].items() if k.startswith('apart'))
assert conn['spine_theorems'] == n_thm, (conn['spine_theorems'], n_thm)
assert not any(f'Becoming.{m}' in conn['apart_by_module'] for m in MODS)
comps = conn['components']['count']
outside = len(conn['components']['theorems_outside_the_main_component'])
both = conn['classes']['statement on both families']
fmt = lambda n: f'{n:,}'

# Study section 193.
study = (HERE / 'study_v.txt').read_text(encoding='utf-8')
study = study.replace('{RECEIPT}', receipt_id).replace(
    '{APART}', f'{apart} apart of {fmt(n_thm)}, none in the five modules; Law.lost_stays, registered\n'
               '          apart as restating, is now used on the base (Becoming.Pace) and leaves the register')
assert re.search(r'^## 192\. ', (ROOT / STUDY).read_text(), re.M)
append(STUDY, '\n' + study)

# D48.
append(DC, (HERE / 'd48.txt').read_text(encoding='utf-8'))
append(DCZ, (HERE / 'd48.zh.txt').read_text(encoding='utf-8'))

# Chapter, English.
sec4 = (HERE / 'chapter_section4.txt').read_text(encoding='utf-8').strip('\n')
ANCHOR4 = 'Under the relational reading, “my share makes no difference” does not remove a drawer from consumption either. None of this yields responsibility or duty.\n'
OLD77 = ("Which law closes rather than widens a difference, how a member's law comes to, differences at many conditions "
         "at once, and members that read one another's coupling directly are open (§8.2, “Selection, causes and experiment”).")
NEW77 = ("For a loop, which law closes rather than widens a difference is answered: closing needs a link that gives back "
         "less than it received, and with whole-number strengths a loop closes at the first turn, keeps the difference or "
         "runs away (`Becoming.Widening`, §4). How a member's law comes to, differences at many conditions at once, and "
         "members that read one another's coupling directly are open (§8.2, “Selection, causes and experiment”).")
OLD82S = ("where two courses rejoin: `Becoming.Rejoining`.) Which law closes rather than widens a difference a pool's acts "
          "separate, and how a member's law comes to;")
NEW82S = ("where two courses rejoin: `Becoming.Rejoining`; whether a loop closes, keeps or widens a difference: "
          "`Becoming.Widening`.) Which law closes rather than widens a difference a pool's acts separate beyond a single "
          "loop, and how a member's law comes to;")
SEEK_END = ('[runaway-distance-unregistered](../results/records/runaway-distance-unregistered.md), '
            '[subthreshold-registration](../results/records/subthreshold-registration.md) |\n')
ROW = (
    '| Collective continuation | (Stated: giving that waits on giving, `Becoming.Withholding`; whether a loop closes, '
    'keeps or widens a difference, `Becoming.Widening`; how fast a rule may change, `Becoming.Pace`; a pattern lasting '
    'through passing, `Becoming.Passing`; conditions kept together and keeping a part, `Becoming.JointKeeping`; §4.) '
    'Amounts of giving and thresholds of waiting (a formation giving where at least `k` of what it waits on gave); '
    'which laws that give first restore giving in a general family, and how such a law forms; a loop with real '
    'strengths, where a multiplication below one closes gradually; many levels of rule and rules that change by '
    'chance; passing derived from descent (`Flow.DescendsAt`) rather than supplied; joint keeping over a horizon with '
    'the choices given by a law of exchange; homeostasis, carrying capacity and fault tolerance stated as instances '
    '(the last joined to `Becoming.FaultEnvelopes`). | '
    '[giving-that-waits-on-giving](../results/records/giving-that-waits-on-giving.md), '
    '[whether-a-loop-closes-a-difference](../results/records/whether-a-loop-closes-a-difference.md), '
    '[how-fast-a-rule-may-change](../results/records/how-fast-a-rule-may-change.md), '
    '[a-pattern-lasts-through-passing](../results/records/a-pattern-lasts-through-passing.md), '
    '[conditions-kept-together](../results/records/conditions-kept-together.md) |\n')
ch = (ROOT / CH).read_text(encoding='utf-8')
m = re.search(r'There are (\d+) dependency components, with (\d+) spine theorems outside the main one; (\d+) statements use both families\.', ch)
assert m, 'components sentence'
OLDINT = m.group(0)
NEWINT = (f'Rerun with V (receipt {receipt_id}), it counts {apart} of {fmt(n_thm)}, none in the five modules '
          '`Becoming.Withholding`, `Becoming.Widening`, `Becoming.Pace`, `Becoming.Passing` and `Becoming.JointKeeping`: '
          'every main law is stated on a run of the spine (`Law.run`), a `Run`, a viability kernel or a web, and '
          '`Law.lost_stays`, registered apart as restating, is now used on the base by `Becoming.Pace` and leaves the '
          f'register. There are {comps} dependency components, with {outside} spine theorems outside the main one; '
          f'{both} statements use both families.')
m = re.search(r'\*\*The current receipt\.\*\* The \[current receipt\]\([^)]*\) is run `([^`]+)`, frozen in .*?It passed\. Its counts:', ch, re.S)
assert m and '\n' not in m.group(0), 'receipt sentence'
old_rid = m.group(1)
NEWREC = (f'**The current receipt.** The [current receipt](../../../{PKG}/becoming-verification.json) is run '
          f'`{receipt_id}`, frozen in [`becoming-checks/{receipt_id}/`](../../../{PKG}/becoming-checks/{receipt_id}/'
          f'verification.json). It was checked with Lean 4.29.1 on main {base} (after V\'s board note) with V '
          '(`Becoming.Withholding`, `Becoming.Widening`, `Becoming.Pace`, `Becoming.Passing`, `Becoming.JointKeeping`, '
          '[study §193](../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/'
          'BECOMING-RENEWAL-READING.md#193-what-a-collectives-continuation-needs-v)) in the working tree. It passed. '
          'Its counts:')
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
edit(CH, [(ANCHOR4, ANCHOR4 + '\n' + sec4 + '\n'), (OLD77, NEW77), (OLD82S, NEW82S), (SEEK_END, SEEK_END + ROW),
          (OLDINT, NEWINT), (m.group(0), NEWREC), (table.group(0), NEWTABLE), (mo.group(0), NEWMO), (mr.group(0), NEWR)])

# Chapter, Chinese edition.
secz = (HERE / 'chapter_section4.zh.txt').read_text(encoding='utf-8').strip('\n')
ANCHORZ = '在关系读法下，“我的一份不造成差别”也不把它移出消耗。这些都不推出责任或义务。\n'
edit(CHZ, [(ANCHORZ, ANCHORZ + '\n' + secz + '\n')])

# Board: the row moves to the history file; the queue sentence names the landing.
board = (ROOT / BOARD).read_text(encoding='utf-8')
history = (ROOT / HISTORY).read_text(encoding='utf-8')
lines = board.split('\n')
rows = [i for i, line in enumerate(lines) if line.startswith("| **V: what a collective's continuation needs**")]
assert len(rows) == 1, rows
row = lines.pop(rows[0])
cells = row.split(' | ')
assert len(cells) == 5, len(cells)
cells[2] = (f'landed 2026-10-19, core receipt `{receipt_id}`; 157 theorems in five core modules, empty axiom reports; '
            'records giving-that-waits-on-giving, whether-a-loop-closes-a-difference, how-fast-a-rule-may-change, '
            'a-pattern-lasts-through-passing, conditions-kept-together; study §193; readings D48')
row = ' | '.join(cells).replace('](../', '](../../../').replace('](research/', '](../../research/')
hist = history.split('\n')
stop = next((i for i, line in enumerate(hist) if line.startswith('## Lapsed claims')), len(hist))
last = max(i for i, line in enumerate(hist[:stop]) if line.startswith('| **'))
hist.insert(last + 1, row)
board = '\n'.join(lines)
old_q = re.search(r"then V \(what a collective's continuation needs: [^)]*\), then W2 \(", board)
assert old_q, 'queue sentence'
board = board.replace(old_q.group(0), 'then W2 (')
mq = re.search(r'Y1 landed as `928422fa2`, core receipt `20261019T060745\.666273Z`, ahead of W2\)', board)
assert mq, 'landed list'
board = board.replace(mq.group(0), mq.group(0)[:-1] + f'; V landed, core receipt `{receipt_id}`, ahead of W2)')
(ROOT / BOARD).write_text(board, encoding='utf-8')
(ROOT / HISTORY).write_text('\n'.join(hist), encoding='utf-8')
print('board row moved; receipt', receipt_id, 'apart', apart, 'theorems', n_thm, 'modules', n_mod, 'closure', closure)
