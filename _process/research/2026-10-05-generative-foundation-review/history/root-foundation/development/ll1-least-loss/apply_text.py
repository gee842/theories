#!/usr/bin/env python3
"""LL1 landing text: the study section (numbered after the last one), the chapter (item 4, §0 premise card,
§1 limits of the rest theorem, §8.2 entropy row and integration row, §8.6, §8.7, §9 receipt) and its Chinese
edition (item 4, §2 rest and openness). Every edit must match exactly once.

usage (from the checkout root to edit): python3 -B apply_text.py RECEIPT BASE CONNECTIVITY_LOG
RECEIPT is the core checker run, BASE the main commit it ran on, CONNECTIVITY_LOG the --check output on the
landing tree. Prints the study section number. The board row is moved by hand at landing."""
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
LL = f'../../../{PKG}/Becoming/LeastLoss.lean'
REC = '../results/records/least-loss-rest.md'
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
    print('edited', path, len(pairs), file=sys.stderr)


rec = json.loads((ROOT / PKG / 'becoming-checks' / receipt_id / 'verification.json').read_text())
core = [m for m in rec['modules'] if m['layer'] == 'core']
assert rec['status'] == 'passed' and rec['core_compiles_from_prelude'] and rec['source_unchanged_during_check']
assert not any(v for m in core for v in m['axiom_dependencies'].values())
spine = {m['module']: m['theorems'] for m in core}
n_mod = len(rec['core_modules'])
n_thm = sum(spine.values())
ll = spine['Becoming.LeastLoss']
ll_decls = len(next(m for m in core if m['module'] == 'Becoming.LeastLoss')['declarations'])
closure = len(rec['core_closure'])
assert closure == len(rec['compile_order'])
audits = sum(len(m['declarations']) for m in rec['modules'] if m['spine'])
inj = len(rec['generated_axiom_dependencies'])
ran, reused = len(rec['lean_steps']['ran']), len(rec['lean_steps']['reused'])
t = Path(conn_log).read_text() if conn_log.startswith('/') else (ROOT / conn_log).read_text()
conn = json.loads(t[t.index('{'):t.rindex('}') + 1])
apart = sum(v for k, v in conn['classes'].items() if k.startswith('apart'))
assert conn['spine_theorems'] == n_thm, (conn['spine_theorems'], n_thm)
ll_apart = conn['apart_by_module']['Becoming.LeastLoss'][0]
comps = conn['components']['count']
outside = len(conn['components']['theorems_outside_the_main_component'])
both = conn['classes']['statement on both families']
fmt = lambda n: f'{n:,}'

# Study section, numbered after the last.
study_text = (ROOT / STUDY).read_text(encoding='utf-8')
last = max(int(n) for n in re.findall(r'^## (\d+)\. ', study_text, re.M))
N = last + 1
section = (HERE / 'study_ll1.txt').read_text(encoding='utf-8').replace('## NNN.', f'## {N}.')
section = section.replace('`RECEIPT`', f'`{receipt_id}`')
section = section.replace('CONNECTIVITY', f'connectivity check passes on the landing tree, {apart} apart of '
                          f'{fmt(n_thm)}, {ll_apart} of {ll} in Becoming.LeastLoss (the dyadic and layered\n'
                          '          models and their arithmetic; six roots registered)')
assert 'RECEIPT' not in section and 'NNN' not in section
(ROOT / STUDY).write_text(study_text.rstrip('\n') + '\n\n' + section.rstrip('\n') + '\n', encoding='utf-8')
anchor = f'{N}-the-least-loss-as-a-premise-of-rest-ll1'
STUDY_LINK = f'../../../{STUDY}#{anchor}'

# Chapter, English.
OLD4 = ('The rest theorem depends on that whole unit: with real-valued amounts, losses can shrink geometrically and '
        'a closed world need not come to rest, and the second law supplies no least loss per step. [theorem]')
NEW4 = ('The rest theorem depends on that whole unit, and exactly through two premises of one law over amounts that '
        'may be dense: a least loss at each change counted, and the stock lying within finitely many least losses. '
        'Whole numbers are its instance, and the rest theorem is proved again from it with its statement unchanged '
        '(`Amounts.rests`, `World.rests_unrefuted_enclosed_whole`). With no least loss, in Archimedean amounts, a '
        'closed amount still comes arbitrarily near rest: for every amount above nothing, fewer than some count of '
        'steps lose at least it (`Amounts.few_large_losses_of_archimedean`); rest itself needs the least loss. '
        'With dense amounts and no least loss, losses shrink geometrically, and a stock halving at every step '
        'approaches rest without reaching it (`Halving.approaches_without_reaching`); the second law supplies no '
        'least loss per step. Over finitely many configurations a loss above nothing needs a law that merges '
        '(`Law.loss_needs_merge`): rest belongs to descriptions that lump configurations and dissipate, and a '
        'finite law that merges nothing returns rather than rests (`Becoming.Recurrence`) '
        f'([Becoming.LeastLoss]({LL}), [least-loss-rest]({REC})). [theorem]')
OLDDIS = ('on which the rest theorems and feeding from beyond depend (block A, natural-number amounts) |')
NEWDIS = ('on which the rest theorems and feeding from beyond depend (block A, natural-number amounts); over amounts '
          'that may be dense the least loss is a premise of the rest law (`Becoming.LeastLoss`) |')
OLDCARD = ('The second law supplies no least loss per step. | `Web.level`, `Flow.take`, `Flow.give` | representation; finer units in `Becoming.Units`, '
           '`Becoming.Resolution` |')
NEWCARD = ('The second law supplies no least loss per step. | `Web.level`, `Flow.take`, `Flow.give` | representation; finer units in `Becoming.Units`, '
           '`Becoming.Resolution`; for the rest laws, amounts that may be dense in `Becoming.LeastLoss`, the least '
           'loss a premise |')
OLDLIM = ('At a refining unit, rest fails unless the refinement is counted (`Becoming.Resolution`). The rest theorem '
          'is a well-founded descent on natural numbers.')
NEWLIM = ('At a refining unit, rest fails unless the refinement is counted (`Becoming.Resolution`). Every rest law '
          'reaches its conclusion through one of two descents on natural numbers (`falls_not_recurring`, '
          '`falls_stop_unrefuted`). Stated over amounts that may be dense (an order that addition keeps and '
          'cancels, with nothing least), the descent needs exactly two premises, both of which whole numbers '
          'supply: a least loss `ε` at each change counted, and the stock lying within finitely many copies of `ε`. '
          'Archimedean amounts give the second for every `ε` above nothing (`Amounts.rests`, '
          '`Amounts.rests_unrefuted`, `Amounts.rests_of_archimedean`). A family balanced and dissipated on with a '
          'least loss comes to rest in any such amounts (`Amounts.family_rests`). Whole numbers are the instance, '
          'with `ε` one. From the law, the two descents, `Flow.taking_not_recurring_from`, '
          '`Flow.takers_within_on`, `Flow.change_stops_unrefuted` and the rest theorem '
          '`World.rests_unrefuted_enclosed` are proved again, their statements unchanged. Each premise is needed. '
          'In dyadic amounts, dense and Archimedean, a stock halving at every step loses at every step, has no '
          'least loss and never rests (`Halving.never_rests`). In layered amounts a stock falls by a least loss at '
          'every step, lies beyond every multiple of it and never rests (`Layered.never_rests`). In any amounts '
          'the losses of a falling stock are summable (`Amounts.losses_within`). Approach to rest needs no least '
          'loss. For any `k` steps each losing at least `ε`, `k` copies of `ε` are within the stock '
          '(`Amounts.large_losses_within`). So in Archimedean amounts, for every `ε` above nothing, fewer than some '
          'count of steps lose at least `ε`, and such steps do not recur (`Amounts.few_large_losses_of_archimedean`, '
          '`Amounts.approaches_rest`). The Archimedean property is the structural premise here; layered amounts '
          'lack it (`Layered.not_archimedean`). In whole numbers approach is rest: no more steps lose anything than '
          'the stock counts (`Amounts.whole_losing_steps`). The halving stock approaches rest and falls at every '
          'step (`Halving.approaches_without_reaching`), as exponential relaxation does. Rest itself needs the '
          'least loss. So the rest laws hold in a continuous reading exactly where change of the kind counted has a '
          'floor and the stock lies within finitely many floors. Over finitely many configurations, a law that '
          'merges nothing returns every configuration (`Becoming.Recurrence`), so along its orbits every loss is '
          'nothing (`Law.Lossless.loses_nothing`) and a loss above nothing needs a merge (`Law.loss_needs_merge`), '
          'as along a run of every process (`Branching.loss_needs_merge`). '
          'Rest is a law of descriptions that lump configurations and dissipate; a finite world that merges nothing '
          f'returns rather than rests ([Becoming.LeastLoss]({LL}), [least-loss-rest]({REC})).')
OLDENT = ('whether the least loss per exchange can be derived rather than supplied, and whether lossless exchanges '
          'exist. | [entropy-history-and-record](../results/records/entropy-history-and-record.md), '
          '[rest-with-refinement-counted](../results/records/rest-with-refinement-counted.md), '
          '[recurrence-without-premise](../results/records/recurrence-without-premise.md) |')
NEWENT = ('whether the least loss per exchange can be derived rather than supplied (over amounts that may be dense it '
          'is the premise of `Amounts.rests`), and whether lossless exchanges exist; the flow, web and world with '
          'levels in any amounts, and the rest family restated there; a least loss that holds only in expectation. '
          '| [entropy-history-and-record](../results/records/entropy-history-and-record.md), '
          '[rest-with-refinement-counted](../results/records/rest-with-refinement-counted.md), '
          '[recurrence-without-premise](../results/records/recurrence-without-premise.md), '
          f'[least-loss-rest]({REC}) |')
OLD86 = ('The rest theorems conclude only that coming to rest cannot be refuted, ¬¬∃ (`World.rests_unrefuted`, '
         '`World.comes_to_rest_unrefuted`, `World.rests_unrefuted_enclosed`).')
NEW86 = (OLD86 + ' Over amounts that may be dense, the least-loss law takes its premises in the same weak form and '
         'decides nothing. So its whole-number instance proves `Flow.change_stops_unrefuted` again without '
         'deciding the order, as the original does twice (`Amounts.rests_unrefuted`, '
         '`Flow.change_stops_unrefuted_whole`).')
OLD87 = ('Whether a given system\'s exchanges meet these premises stays empirical.')
NEW87 = (OLD87 + ' Read with amounts that may be dense, rest needs a least loss per change and the stock within finitely '
         'many least losses (`Amounts.rests`), while approach to rest needs only Archimedean amounts '
         '(`Amounts.approaches_rest`); without a floor a stock can fall for ever while approaching rest '
         '(`Halving.approaches_without_reaching`), as exponential relaxation does, and over finitely many '
         'configurations a loss needs a law that merges (`Law.loss_needs_merge`) '
         f'([least-loss-rest]({REC})).')
ch = (ROOT / CH).read_text(encoding='utf-8')
mi = re.search(r'There are (\d+) dependency components, with (\d+) spine theorems outside the main one; (\d+) '
               r'statements use both families\.', ch)
assert mi, 'components sentence'
NEWINT = (f'Rerun with LL1 (receipt {receipt_id}), it counts {apart} of {fmt(n_thm)}: {ll_apart} of the {ll} '
          'theorems of `Becoming.LeastLoss` stand apart, the dyadic and layered models and their arithmetic, while its '
          'laws are used on the base by its six whole-number restatements (`World.rests_unrefuted_enclosed_whole` '
          f'among them). There are {comps} dependency components, with {outside} spine theorems outside the main '
          f'one; {both} statements use both families.')
m = re.search(r'\*\*The current receipt\.\*\* The \[current receipt\]\([^)]*\) is run `([^`]+)`, frozen in .*?'
              r'It passed\. Its counts:', ch, re.S)
assert m and '\n' not in m.group(0), 'receipt sentence'
NEWREC = (f'**The current receipt.** The [current receipt](../../../{PKG}/becoming-verification.json) is run '
          f'`{receipt_id}`, frozen in [`becoming-checks/{receipt_id}/`](../../../{PKG}/becoming-checks/{receipt_id}/'
          f'verification.json). It was checked with Lean 4.29.1 on main {base} with LL1 (`Becoming.LeastLoss`, '
          f'[study §{N}]({STUDY_LINK})) in the working tree. It passed. Its counts:')
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
mo = re.search(r'\| Modules in the compile order \| (\d+) \|\n\| Generated `injEq` lemmas on `propext` \| (\d+) in the '
               r'core closure \|', ch)
assert mo, 'compile order'
NEWMO = f'| Modules in the compile order | {closure} |\n| Generated `injEq` lemmas on `propext` | {inj} in the core closure |'
mr = re.search(r'That run reused ([\d,]+) cached Lean steps from `~/.cache/becoming-lean` and ran (\d+)\.', ch)
assert mr, 'reuse sentence'
NEWR = f'That run reused {fmt(reused)} cached Lean steps from `~/.cache/becoming-lean` and ran {ran}.'
edit(CH, [(OLD4, NEW4), (OLDDIS, NEWDIS), (OLDCARD, NEWCARD), (OLDLIM, NEWLIM), (OLDENT, NEWENT), (OLD86, NEW86), (OLD87, NEW87),
          (mi.group(0), NEWINT), (m.group(0), NEWREC), (table.group(0), NEWTABLE), (mo.group(0), NEWMO),
          (mr.group(0), NEWR)])

# Chapter, Chinese edition.
OLDZ4 = ('量取实数时，损失可以几何地缩小，封闭的世界不必归于停息，而第二定律不给每步的最小损失。〔定理〕')
NEWZ4 = ('量取实数时，损失可以几何地缩小，封闭的世界不必归于停息，而第二定律不给每步的最小损失。'
         '整数所承载的，恰是一条对可稠密之量成立的规律的两个前提：每次被计的变化有最小损失，'
         '且存量在有限份最小损失之内；整数是它的实例，停息定理由它重新证明，陈述不变'
         '（`Amounts.rests`、`World.rests_unrefuted_enclosed_whole`）；没有最小损失时，在阿基米德的量中，封闭的量仍任意地趋近停息：'
         '对每个大于无的量，至少损失它的步少于某个数（`Amounts.few_large_losses_of_archimedean`），停息本身则需要最小损失；'
         '量稠密而无最小损失时，每步减半的存量趋近停息而达不到（`Halving.approaches_without_reaching`）。'
         '在有限多个构形上，大于无的损失需要一条有所合并的规律（`Law.loss_needs_merge`）：停息属于把构形归并而耗散的描述，'
         '不合并任何东西的有限规律回返而不停息（`Becoming.Recurrence`）'
         f'（[Becoming.LeastLoss]({LL})，[least-loss-rest]({REC})）。〔定理〕')
OLDZR = ('缺少比例、最小尺度或储备的最小下降中的任何一个，变化都可以无尽地继续（[Becoming.Resolution]'
         '(../../../experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming/'
         'Resolution.lean)，[rest-at-every-resolution](../results/records/rest-at-every-resolution.md)）。')
NEWZR = (OLDZR + '每条停息规律都经由整数上的两个下降之一得到结论（`falls_not_recurring`、`falls_stop_unrefuted`）。'
         '对可稠密的量（加法保持并可消去的序，无为最小）陈述，这一下降恰需要整数所供给的两个前提：'
         '每次被计的变化至少损失 `ε`，且存量在有限份 `ε` 之内；阿基米德的量对每个大于无的 `ε` 给出后者'
         '（`Amounts.rests`、`Amounts.rests_unrefuted`、`Amounts.rests_of_archimedean`）；'
         '平衡且被耗散、有最小损失的家族在任何这样的量中都停息（`Amounts.family_rests`）。整数是 `ε` 为一的实例：'
         '两个下降、`Flow.taking_not_recurring_from`、`Flow.takers_within_on`、`Flow.change_stops_unrefuted` '
         '与停息定理 `World.rests_unrefuted_enclosed` 都由此律重新证明，陈述不变。每个前提都不可少：'
         '在稠密且阿基米德的二进分数量中，每步减半的存量每步都有损失、没有最小损失、从不停息（`Halving.never_rests`）；'
         '在分层的量中，存量每步至少下降一个最小损失，处于其每一倍数之上，从不停息（`Layered.never_rests`）。'
         '在任何量中，下降的存量的损失之和都在存量之内（`Amounts.losses_within`）。趋近停息不需要最小损失：'
         '任意 `k` 步各至少损失 `ε` 时，`k` 份 `ε` 在存量之内（`Amounts.large_losses_within`）；所以在阿基米德的量中，'
         '对每个大于无的 `ε`，至少损失 `ε` 的步少于某个数，且不复现（`Amounts.few_large_losses_of_archimedean`、'
         '`Amounts.approaches_rest`）；阿基米德性是这里的结构前提，分层的量没有它（`Layered.not_archimedean`）。'
         '在整数中趋近即停息：有所损失的步不多于存量之数（`Amounts.whole_losing_steps`）。'
         '每步减半的存量趋近停息而每步都在下降（`Halving.approaches_without_reaching`），如指数弛豫。停息本身需要最小损失；'
         '所以停息的规律在连续的读法中成立，恰在被计的那种变化有下限、且存量只有有限个下限之深之处。'
         '在有限多个构形上，不合并任何东西的规律使每个构形回返（`Becoming.Recurrence`），沿其轨道每个损失都为无'
         '（`Law.Lossless.loses_nothing`），大于无的损失需要合并（`Law.loss_needs_merge`；每个过程的运行亦然，`Branching.loss_needs_merge`）：停息是归并构形而耗散的描述的规律，'
         '不合并任何东西的有限世界回返而不停息'
         f'（[Becoming.LeastLoss]({LL})，[least-loss-rest]({REC})）。')
edit(CHZ, [(OLDZ4, NEWZ4), (OLDZR, NEWZR)])
print(N)
