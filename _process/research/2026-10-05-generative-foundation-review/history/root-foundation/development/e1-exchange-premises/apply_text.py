#!/usr/bin/env python3
"""E1 landing text: the next study section; chapter item 3, premise card C, §8.1 target row, §8.2 row and §9 receipt
(English); item 3, the stated-whole bullet and paragraph II, §8.1 and §8.2 rows (Chinese edition); the board row moved
to the history file, and the queue sentence. Every edit must match exactly once.

usage (from the checkout root to edit): python3 -B apply_text.py RECEIPT BASE CONNECTIVITY_LOG
BASE is the main commit the receipt sentence names: the one the receipt records (source_commit.main), short."""
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
MOD = 'ExchangePremises'
receipt_id, base, conn_log = sys.argv[1], sys.argv[2], sys.argv[3]
R = '../results/records/'


def link(i):
    return f'[{i}]({R}{i}.md)'


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
n_mod = len(rec['core_modules'])
n_thm = sum(spine.values())
mine = next(m for m in core if m['module'] == f'Becoming.{MOD}')
found, decls = mine['theorems'], len(mine['declarations'])
closure = len(rec['core_closure'])
assert closure == len(rec['compile_order'])
audits = sum(len(m['declarations']) for m in rec['modules'] if m['spine'])
inj = len(rec['generated_axiom_dependencies'])
ran, reused = len(rec['lean_steps']['ran']), len(rec['lean_steps']['reused'])
t = Path(conn_log).read_text()
conn = json.loads(t[t.index('{'):t.rindex('}') + 1])
apart = sum(v for k, v in conn['classes'].items() if k.startswith('apart'))
assert conn['spine_theorems'] == n_thm, (conn['spine_theorems'], n_thm)
assert f'Becoming.{MOD}' not in conn['apart_by_module']
comps = conn['components']['count']
outside = len(conn['components']['theorems_outside_the_main_component'])
both = conn['classes']['statement on both families']
fmt = lambda n: f'{n:,}'

# Study section: the number after the last.
st = (ROOT / STUDY).read_text(encoding='utf-8')
assert 'Which remaining premises a reading of the exchange settles (E1)' not in st, 'already applied'
SEC = max(int(n) for n in re.findall(r'^## (\d+)\. ', st, re.M)) + 1
SLUG = f'#{SEC}-which-remaining-premises-a-reading-of-the-exchange-settles-e1'
study = (HERE / 'study_e1.txt').read_text(encoding='utf-8')
study = (study.replace('{SEC}', str(SEC)).replace('{RECEIPT}', receipt_id).replace('{THEOREMS}', str(found))
         .replace('{DECLS}', str(decls))
         .replace('{APART}', f'connectivity check passes, {apart} apart of {fmt(n_thm)}, none in the module'))
(ROOT / STUDY).write_text(st.rstrip('\n') + '\n\n' + study.rstrip('\n') + '\n', encoding='utf-8')
print('appended', STUDY)

# Chapter, English.
OLD3 = ("This independence measures the freedom of `World`'s separately chosen fields, not contingency in becoming. "
        "Read off one exchange with the rest counted, balance, only active giving and only active taking hold by reading "
        "(`World.withRest`). [theorem]")
NEW3 = ("This independence measures the freedom of `World`'s separately chosen fields, not contingency in becoming. "
        "Read off one exchange with the rest counted, five of the eight are readings: balance, only active giving and "
        "only active taking hold by reading, activity needing support does for a law of exchange (`World.withRest`, "
        "`ExchangeLaw.readWorld_glue`), and a census does wherever a named family closes each step's exchange, with no "
        "decision procedure, while no world read off an exchange fails a census at any step (`World.withRest_counted`, "
        "`Flow.not_not_listed_at`). Three are states of the law of exchange: worlds read off laws, with the rest counted "
        "and idle and the four tying premises holding, meet and fail each of dissipation, embodiment and bounded "
        "transmission (`ExchangeLaw.contingent`), as closure is feasibility and enclosure is the law's reach "
        "(`ExchangeLaw.spreading_not_enclosed`). [theorem]")
BOOK = ("This is not bookkeeping that removes the premise: with the rest counted, balance holds exactly where the rest "
        "is never active (`World.withRest_closed_iff`), and under a law of what has stood the rest is idle exactly where "
        "the course is feasible, no exchange taking from a condition more than stands on it and is given to it "
        "(`ExchangeLaw.readWorld_closed_iff`, `ExchangeLaw.course_balances_iff`). Nothing comes from nothing is then a "
        "premise located in the law, feasibility, not an absence of premise.")
OLDC = ("- *What the independence measures.* It measures the freedom of `World`'s separately chosen fields, not "
        "contingency in becoming. With activity and drawing read off one exchange and the rest of the whole counted, "
        "balance, only active giving and only active taking hold by reading. For a law of exchange, so does activity "
        "needing support (`World.withRest`, `ExchangeLaw.readWorld_glue`). " + BOOK + " Records: "
        f"[map-of-premises]({R}map-of-premises.md), "
        f"[premises-read-off-the-exchange]({R}premises-read-off-the-exchange.md).")
NEWC = (
    "- *What the independence measures.* It measures the freedom of `World`'s separately chosen fields, not "
    "contingency in becoming. Read off one exchange, with the rest of the whole counted, the eight divide in two "
    "(`Becoming.Reading`, `Becoming.ExchangePremises`).\n"
    "  - *Five are readings.* Balance, only active giving and only active taking hold by reading; for a law of exchange, "
    "so does activity needing support (`World.withRest`, `ExchangeLaw.readWorld_glue`). " + BOOK + " A census holds wherever a named "
    "family closes each step's exchange: the relata that exchange are then listed with no decision procedure, so every "
    "finite world whose formations taking part are listed once has a census with its rest counted, where "
    "`World.Finite.counted` needed activity decided (`World.withRest_counted`, `World.Finite.withRest_counted`). "
    "Without enclosure no world read off an exchange fails a census at any step, but asking one at every step of every "
    "flow over `Nat` is exactly the limited principle of omniscience: listing what exchanges then decides whether a "
    "formation exchanges with any of unboundedly many relata (`Flow.not_not_listed_at`, `Flow.listed_iff_lpo`).\n"
    "  - *Three are states of the law.* Worlds read off laws of exchange, with the rest counted and idle and the four "
    "tying premises holding, meet and fail each (`ExchangeLaw.contingent`). Dissipation is loss: under `responsive` a "
    "relatum takes its condition's unit and gives it back. Embodiment is no dormancy: under `still` a relatum stands "
    "and does not exchange; with the rest counted, embodiment is exactly balance and each relatum exchanging exactly "
    "while it stands (`World.withRest_embodied_iff`). Bounded transmission is heredity of response: under `sprouting` "
    "a sprout's exchange responds to the ground and its source's giving does not. As closure is feasibility, "
    "enclosure is the law's reach: under `spreading` no step is "
    "enclosed and a census still exists (`ExchangeLaw.spreading_not_enclosed`, `ExchangeLaw.spreading_counted`).\n"
    "  - *Requirement over open exchanges.* Where a relation leaves several exchanges open, requirement read as "
    "necessary response (under every history lowering the condition, no open exchange has the formation exchange) gives "
    "activity needing support on every run, and the four tying premises hold (`ExchangeRelation.reading_glue`); read "
    "as possible response it does not (`ExchangeRelation.free_unsupported`). A law of exchange is the relation leaving "
    "one exchange open, and there the two readings are the law's (`ExchangeLaw.relation_readWeb_requires`, "
    "`ExchangeLaw.relation_readWeb_may`).\n"
    f"  Records: {link('map-of-premises')}, {link('premises-read-off-the-exchange')}, "
    f"{link('census-read-off-the-exchange')}, {link('premises-that-are-states-of-the-law')}, "
    f"{link('requirement-over-open-exchanges')}.")
OLD81 = ("The record shows no progress entry since the early spine; the wording of the target is a goal scope, which "
         "changes only with Ren. |")
NEW81 = ("Of the eight `World` premises, five are readings of one exchange, and three, dissipation, embodiment and bounded "
         "transmission, are states of the law of exchange, as closure (feasibility) and enclosure (the law's reach) are "
         f"(premise card C, {link('premises-that-are-states-of-the-law')}). The necessary content of the whole cannot "
         "include those three: what a reading of the exchange makes necessary is what holds of every law of exchange, "
         "and which law holds is where becoming is contingent. Open as formal work: the spine's laws stated over every "
         "law, or relation, of exchange rather than over separately chosen premises. The wording of the target is a goal "
         "scope, which changes only with Ren. |")
OLD82 = ("The novelty and forgetting laws rest on the unit and on discrete steps (pigeonhole on the natural numbers); open "
         "there: reaching the bound,")
NEW82 = ("Read off one exchange, the census is a reading under enclosure, dissipation, embodiment and bounded "
         "transmission are states of the law, and requirement read as necessary response stays a reading where several "
         "exchanges are open ([Becoming.ExchangePremises](../../../" + PKG + "/Becoming/ExchangePremises.lean)); open "
         "there: the relation of exchange joined to the branching processes of `Becoming.Branching`, and a census over "
         "every step without a named family. The novelty and forgetting laws rest on the unit and on discrete steps "
         "(pigeonhole on the natural numbers); open there: reaching the bound,")
OLD82L = (f"[premises-read-off-the-exchange]({R}premises-read-off-the-exchange.md), "
          f"[unity-of-readings]({R}unity-of-readings.md),")
NEW82L = (f"[premises-read-off-the-exchange]({R}premises-read-off-the-exchange.md), "
          f"{link('census-read-off-the-exchange')}, {link('premises-that-are-states-of-the-law')}, "
          f"{link('requirement-over-open-exchanges')}, [unity-of-readings]({R}unity-of-readings.md),")

ch = (ROOT / CH).read_text(encoding='utf-8')
OLDINT = ' The two course worlds are two readings of one flow and one web, defined once.'
NEWINT = (f' Rerun with E1 (receipt {receipt_id}), it counts {apart} of {fmt(n_thm)}, none in '
          '`Becoming.ExchangePremises`, whose laws are stated on flows, webs and worlds read off laws of '
          f'exchange; {comps} dependency components, {outside} spine theorems outside the main one, {both} '
          'statements on both families.' + OLDINT)
m = re.search(r'\*\*The current receipt\.\*\* The \[current receipt\]\([^)]*\) is run `([^`]+)`, frozen in .*?It passed\. '
              r'Its counts:', ch, re.S)
assert m and '\n' not in m.group(0), 'receipt sentence'
NEWREC = (f'**The current receipt.** The [current receipt](../../../{PKG}/becoming-verification.json) is run '
          f'`{receipt_id}`, frozen in [`becoming-checks/{receipt_id}/`](../../../{PKG}/becoming-checks/{receipt_id}/'
          f'verification.json). It was checked with Lean 4.29.1 on main {base} (after E1\'s board claim) with E1 '
          f'(`Becoming.ExchangePremises`, [study §{SEC}](../../../_process/research/2026-10-05-generative-foundation-review/'
          f'root-foundation/BECOMING-RENEWAL-READING.md{SLUG})) '
          'in the working tree. It passed. Its counts:')
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
mo = re.search(r'\| Modules in the compile order \| (\d+) \|\n\| Generated `injEq` lemmas on `propext` \| (\d+) in the core '
               r'closure \|', ch)
assert mo, 'compile order'
NEWMO = f'| Modules in the compile order | {closure} |\n| Generated `injEq` lemmas on `propext` | {inj} in the core closure |'
mr = re.search(r'That run reused ([\d,]+) cached Lean steps from `~/.cache/becoming-lean` and ran (\d+)\.', ch)
assert mr, 'reuse sentence'
NEWR = f'That run reused {fmt(reused)} cached Lean steps from `~/.cache/becoming-lean` and ran {ran}.'
edit(CH, [(OLD3, NEW3), (OLDC, NEWC), (OLD81, NEW81), (OLD82, NEW82), (OLD82L, NEW82L), (OLDINT, NEWINT),
          (m.group(0), NEWREC), (table.group(0), NEWTABLE), (mo.group(0), NEWMO), (mr.group(0), NEWR)])

# Chapter, Chinese edition.
OLDZ3 = ("余下的是部分的状态：其余是否闲置（封闭，对一条律即可行）、耗散、体现、有界传递，以及列出活跃者所需的判定（其余算作关系项，见第 1 条）。")
NEWZ3 = ("凡有一个具名的家族围住每一步的交换，普查也由读法成立，不需判定程序，所以形成参与者各列一次的每个有限世界算入其余都有普查；"
         "不被围住时，从交换读出的世界没有一个在任何一步缺普查，但对 `Nat` 上每个流的每一步要求普查恰是有限全知原则"
         f"（`World.withRest_counted`、`Flow.not_not_listed_at`、`Flow.listed_iff_lpo`，{link('census-read-off-the-exchange')}）。"
         "所以八个中五个是一次交换的读法。另三个是交换之律的状态：从交换之律读出、算入其余且其余闲置、四个联结前提成立的世界，"
         f"耗散、体现与有界传递各有满足与不满足者（`ExchangeLaw.contingent`，{link('premises-that-are-states-of-the-law')}）："
         "耗散是损失，体现是没有休眠（算入其余时，体现恰是平衡加上每个关系项恰在它立着时交换，`World.withRest_embodied_iff`），"
         "有界传递是回应的遗传；封闭（其余闲置）对一条律即可行，被围住是律所及的范围（`ExchangeLaw.spreading_not_enclosed`）。"
         "在留下多个交换开放的关系上，把要求读作必然的回应，每个运行上活动都需要支持；读作可能的回应则不然"
         f"（`ExchangeRelation.reading_glue`、`ExchangeRelation.free_unsupported`，{link('requirement-over-open-exchanges')}）。")
OLDZ795 = "而不是没有前提；余下的是部分的状态。"
NEWZ795 = ("而不是没有前提；普查在一个具名的家族围住每一步的交换之处也由读法成立（`World.withRest_counted`）；"
           "耗散、体现与有界传递是交换之律的状态，各有满足与不满足它的、从律读出的世界（`ExchangeLaw.contingent`）。")
zh = (ROOT / CHZ).read_text(encoding='utf-8')
mb = re.search(r'^- 从一次交换读出活跃（即交换）与汲取（即所取）.*`Becoming\.Reading`）。\n', zh, re.M)
assert mb, 'stated-whole bullet'
NEWZB = mb.group(0) + ("- 普查在一个具名的家族围住每一步的交换之处由读法成立，不需判定程序；从交换读出的世界在任何一步都不缺普查，"
                       "对每个流的每一步要求普查是有限全知原则；耗散、体现与有界传递是交换之律的状态，各有满足与不满足它的从律读出的世界；"
                       "在留下多个交换开放的关系上，把要求读作必然的回应，每个运行上活动都需要支持，读作可能的回应则不然"
                       "（`World.withRest_counted`、`Flow.listed_iff_lpo`、`ExchangeLaw.contingent`、`ExchangeRelation.reading_glue`，"
                       "`Becoming.ExchangePremises`）。\n")
OLDZ81 = ("| 开放；有限相容性、作用损失与依存变化方式的相互约束已在各自范围内建立 |")
NEWZ81 = ("| 开放；有限相容性、作用损失与依存变化方式的相互约束已在各自范围内建立；`World` 的八个前提中五个是一次交换的读法，"
          "耗散、体现与有界传递三个是交换之律的状态，与封闭（可行）和被围住（律所及的范围）一样"
          f"（{link('premises-that-are-states-of-the-law')}），所以整体的必然内容不能包括这三个：交换的读法使之必然的，"
          "是对每条交换之律都成立的，哪条律成立是生成偶然之处；仍开放的形式工作：在每条交换之律（或交换关系）之上、"
          "而不在分别选取的前提之上陈述脊柱的规律 |")
OLDZ82 = ("（[premises-read-off-the-exchange](../results/records/premises-read-off-the-exchange.md)）；读一个展开的都是语境中的读法")
NEWZ82 = ("（[premises-read-off-the-exchange](../results/records/premises-read-off-the-exchange.md)）；普查在每一步的交换被围住处"
          "由读法成立，耗散、体现与有界传递是律的状态，把要求读作必然的回应在多个交换开放时仍给出支持"
          f"（{link('census-read-off-the-exchange')}、{link('premises-that-are-states-of-the-law')}、"
          f"{link('requirement-over-open-exchanges')}）；读一个展开的都是语境中的读法")
edit(CHZ, [(OLDZ3, NEWZ3), (OLDZ795, NEWZ795), (mb.group(0), NEWZB), (OLDZ81, NEWZ81), (OLDZ82, NEWZ82)])

# Board: the row moves to the history file; the queue sentence names the landing.
board = (ROOT / BOARD).read_text(encoding='utf-8')
history = (ROOT / HISTORY).read_text(encoding='utf-8')
lines = board.split('\n')
rows = [i for i, line in enumerate(lines) if line.startswith('| **E1: the remaining premises read off one exchange**')]
assert len(rows) == 1, rows
row = lines.pop(rows[0])
cells = row.split(' | ')
assert len(cells) == 5, len(cells)
cells[2] = (f'landed 2026-10-19, core receipt `{receipt_id}`; {found} theorems in `Becoming.ExchangePremises`, empty axiom '
            'reports; records census-read-off-the-exchange, premises-that-are-states-of-the-law, '
            'requirement-over-open-exchanges; premises-read-off-the-exchange corrected; a progress entry in '
            f'theory-of-becoming-foundation; study §{SEC}')
row = ' | '.join(cells).replace('](../', '](../../../').replace('](research/', '](../../research/')
hist = history.split('\n')
stop = next((i for i, line in enumerate(hist) if line.startswith('## Lapsed claims')), len(hist))
last = max(i for i, line in enumerate(hist[:stop]) if line.startswith('| **'))
hist.insert(last + 1, row)
board = '\n'.join(lines)
OLDQ = "): W2 (this re-rooting's second batch"
assert board.count(OLDQ) == 1, 'queue sentence'
board = board.replace(OLDQ, f"; E1 landed, core receipt `{receipt_id}`, ahead of W2" + OLDQ)
(ROOT / BOARD).write_text(board, encoding='utf-8')
(ROOT / HISTORY).write_text('\n'.join(hist), encoding='utf-8')
print('study section', SEC)
print('board row moved; receipt', receipt_id, 'apart', apart, 'theorems', n_thm, 'modules', n_mod, 'closure', closure)
