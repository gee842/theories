#!/usr/bin/env python3
"""P107: documentary and registration edits in a checkout (run with the checkout root as argument).

usage: apply_docs.py ROOT
Every edit is anchored on text that must occur exactly once, so a concurrent change stops the script.
Edits: study §124 and its English paragraph; chapter (theory stated in full items 1 and 3, Part I stated
whole, §8, §9 rows, glossary); ZERO-PREMISE-PLAN §1.4; Becoming.lean imports and module notes;
check_becoming.py's core list. §9 totals are written at landing from the receipt.
"""
import sys
from pathlib import Path

ROOT = Path(sys.argv[1]).resolve()
HERE = Path(__file__).resolve().parent
LEANDIR = 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming'
LINK = '../../../' + LEANDIR + '/Becoming/'
REC = '../results/records/'


def edit(path, pairs):
    p = ROOT / path
    s = p.read_text()
    for old, new in pairs:
        assert s.count(old) == 1, (path, s.count(old), old[:90])
        s = s.replace(old, new)
    p.write_text(s)


def study():
    path = '_process/research/2026-10-05-generative-foundation-review/root-foundation/BECOMING-RENEWAL-READING.md'
    p = ROOT / path
    s = p.read_text()
    anchor = '\n## English summary\n'
    assert s.count(anchor) == 1
    section = (HERE / 'study-124.md').read_text().rstrip('\n') + '\n'
    s = s.replace(anchor, '\n' + section + anchor)
    s = s.rstrip('\n') + '\n' + (HERE / 'study-124-en.md').read_text().rstrip('\n') + '\n'
    p.write_text(s)


CH = 'theories/becoming/chapters/THE-THEORY-OF-BECOMING.md'


def chapter():
    src = '../../../sources/15-codex-theory-conversations/2026-10-14-relation-first-refounding.md'
    item1_zh_old = '律与历史是同一展开的两种读法经 Ren 确认，其余读法待 Ren）。〔表示〕'
    item1_zh_new = ('律与历史是同一展开的两种读法经 Ren 确认，其余读法待 Ren）。Ren 问“why do we need "World"?”'
                    f'（2026-10-14，[来源]({src})）。`World` 不是起点：读一个展开的都是语境中的读法，一个展开在语境中的诸读法总是一个世界'
                    '（其关系项是被索引的主张，被识即活跃，其中没有什么立着或被交换），不用粘合，量子的识亦然（`Contextual.world`）；'
                    '不依语境的描述恰在诸读法处处粘合时存在（`Contextual.fitsFree_iff`），`World` 是这样的描述，它的平衡就是所立与交换两种变化'
                    '读法的粘合（`Flow.changeReadings_glue_everywhere_iff`）；把整体的其余算作关系项（Ren 同日采用），每个世界都平衡，是交换之律'
                    f'的一次运行，原来的平衡恰是其余从不活跃（`World.unity`，`Becoming.Readings`，[unity-of-readings]({REC}unity-of-readings.md)）。〔表示，定理〕')
    item1_en_old = 'that law and history are one unfolding read two ways Ren confirmed, the other readings pending Ren). [representation]'
    item1_en_new = ('that law and history are one unfolding read two ways Ren confirmed, the other readings pending Ren). Ren asked '
                    f'“why do we need "World"?” (14 October 2026, [source]({src})). `World` is not the start: whatever reads an '
                    'unfolding is a reading in context, and the readings in context of one unfolding are always one world (its '
                    'relata the indexed claims, active where registered, nothing standing or exchanged in it), with no gluing, '
                    'quantum registrations included (`Contextual.world`); a description free of context exists exactly where the '
                    'readings glue everywhere (`Contextual.fitsFree_iff`), and `World` is such a description, its balance being the '
                    'gluing of the two readings of change, by standing and by exchange (`Flow.changeReadings_glue_everywhere_iff`); '
                    'with the rest of the whole counted as a relatum (adopted by Ren the same day), every world balances and is one '
                    'run of the law of exchange, its former balance being exactly the rest never active (`World.unity`, '
                    f'`Becoming.Readings`, [unity-of-readings]({REC}unity-of-readings.md)). [representation, theorems]')
    item3_zh_old = '它们是前提，不是规律；以下定理在它们划出的部分上成立。〔定理〕'
    item3_zh_new = ('这种独立度量的是 `World` 分别选取的八个字段的自由，不是生成的偶然：从一次交换读出活跃与汲取、算入整体的其余时，平衡、只有活跃者'
                    '给予与只有活跃者取用其所汲取的由读法成立，对一条交换之律把要求读作交换所回应的，活动需要支持也由读法成立（`World.withRest`、'
                    f'`ExchangeLaw.readWorld_glue`，[premises-read-off-the-exchange]({REC}premises-read-off-the-exchange.md)）；余下的是部分的'
                    '状态：其余是否闲置（封闭，对一条律即可行）、耗散、体现、有界传递，以及列出活跃者所需的判定（Ren 2026-10-14 采用把其余算作关系项）。'
                    '它们是前提，不是规律；以下定理在它们划出的部分上成立。〔定理〕')
    item3_en_old = 'They are premises, not laws; the theorems below hold on the parts they carve. [theorem]'
    item3_en_new = ('The independence measures the freedom of `World`\'s eight separately chosen fields, not contingency in '
                    'becoming: with activity and drawing read off one exchange and the rest of the whole counted, balance, only '
                    'active relata giving and only active relata taking what they draw on hold by reading, and for a law of '
                    'exchange, with requirement read as what the exchange responds to, so does activity needing support '
                    f'(`World.withRest`, `ExchangeLaw.readWorld_glue`, [premises-read-off-the-exchange]({REC}premises-read-off-the-exchange.md)); '
                    'what remains are states of parts: whether the rest is idle (closure, for a law feasibility), dissipation, '
                    'embodiment, bounded transmission and the decision needed to list what is active (Ren adopted counting the '
                    'rest as a relatum on 14 October 2026). They are premises, not laws; the theorems below hold on the parts they '
                    'carve. [theorem]')
    each_zh_old = '**二、每个前提加了什么。** 前提是条件定理的假设，不是规律。八个前提彼此独立，每个都划出一个真部分（`World.contingent`、`World.independent`）。'
    each_zh_new = each_zh_old + ('这种独立是 `World` 分别选取的读法之间的：从一次交换读出、算入整体的其余时，平衡、只有活跃者给予、只有活跃者取用其所汲取的'
                                 '与对交换之律的活动需要支持由读法成立（`World.withRest_balanced`、`ExchangeLaw.readWorld_glue`，'
                                 f'[premises-read-off-the-exchange]({REC}premises-read-off-the-exchange.md)）；余下的是部分的状态。')
    each_en_old = ('**II. What each premise adds.** Premises are hypotheses of conditional theorems, not laws. The eight premises '
                   'are independent, and each carves a proper part (`World.contingent`, `World.independent`).')
    each_en_new = each_en_old + (' This independence is among `World`\'s separately chosen readings: read off one exchange with '
                                 'the rest of the whole counted, balance, only active relata giving, only active relata taking what '
                                 'they draw on, and activity needing support under a law of exchange hold by reading '
                                 '(`World.withRest_balanced`, `ExchangeLaw.readWorld_glue`, '
                                 f'[premises-read-off-the-exchange]({REC}premises-read-off-the-exchange.md)); what remains are '
                                 'states of parts.')
    s = (ROOT / CH).read_text()
    zh_learn = next(l for l in s.split('\n') if l.startswith('- 所识的未来相同的配置给每个学习者同样的记录'))
    en_learn = next(l for l in s.split('\n') if l.startswith('- Configurations with the same registered future give every learner'))
    zh_bullets = '\n'.join([
        '- 只用水平，不用流、平衡、损失或世界的有限，部分的状态写在规律之内：家族的存量从某步起在一个界内，其构型从每一步起有两步相同，'
        '不断变化时它在一次变化之后回返；在不多于界内构型数的各步都新的家族在其中某步超出界，逐步核对即得，所以每步都新的家族在任意晚处超出每个界；'
        '在界内的家族，其构型读不出不重复的记录或无界的计数，所以在界内、交换不止的家族不承载其交换的历史，有限的整体亦然；存量不升、每次变化都下降时，'
        '变化的次数不多于起点的存量，变化不无尽复现；熵在第一律之下的形式是其情形（`Web.revisits_of_bounded`、`Web.returns_of_bounded`、'
        '`Web.exceeds_of_new`、`Web.unread_of_unbounded`、`Flow.uncarried_of_bounded`、`World.forgets_of_bounded`、`Web.changes_le_stock`、'
        f'`first_law_cases`，`Becoming.Novelty`，[returning-novelty-forgetting-on-levels]({REC}returning-novelty-forgetting-on-levels.md)）。',
        '- 从一次交换读出活跃（即交换）与汲取（即所取），只有活跃者给予、只有活跃者取用其所汲取的对每个流成立；算入整体的其余，每个世界都平衡，'
        '平衡恰是其余从不活跃；交换之律下，把要求读作交换对条件低于所需的回应，活动需要支持对每个所需成立，四个联结前提都不用前提；要求是律的反事实，'
        '同一历程可以由要求不同的律生成（`Flow.readOff_acting`、`Flow.readOff_taking`、`World.withRest_balanced`、`World.withRest_closed_iff`、'
        '`ExchangeLaw.readWorld_glue`、`ExchangeLaw.requirement_beyond_course`，`Becoming.Reading`）。',
        '- 读一个展开的都是语境中的读法：一个运行上语境系统的诸识总是一个世界的关系项，不用粘合，量子的识亦然；所立与交换两种读法跨一步把变化读得一样，'
        '恰当流在那里平衡，所以 `World` 的平衡是两种读法的粘合；算入其余，每个世界的两种读法处处粘合，是交换之律的一次运行（`Contextual.world`、'
        '`Flow.changeReadings_glue_iff`、`Flow.changeReadings_free_iff`、`World.unity`，`Becoming.Readings`）。'])
    en_bullets = '\n'.join([
        '- On the levels alone, with no flow, balance, loss or finiteness of the world, each law\'s condition a state of the part '
        'written into it: a family whose stock stays within a bound from some step on has two equal configurations from every step '
        'on, and changing without end it returns after a change; a family new at each of as many steps as there are configurations '
        'within a bound exceeds the bound at one of them, found by checking step by step, so a family new at every step exceeds every '
        'bound at arbitrarily late steps; no reading of a bounded family\'s configuration gives a record that never repeats or a count '
        'without bound, so a bounded family exchanged with without end does not carry the history of its exchanges, nor does a finite '
        'whole; with the stock never rising and falling at each change, the changes number at most the stock at the start, and change '
        'does not recur without end; Entropy\'s forms under the first law are cases (`Web.revisits_of_bounded`, '
        '`Web.returns_of_bounded`, `Web.exceeds_of_new`, `Web.unread_of_unbounded`, `Flow.uncarried_of_bounded`, '
        '`World.forgets_of_bounded`, `Web.changes_le_stock`, `first_law_cases`, `Becoming.Novelty`, '
        f'[returning-novelty-forgetting-on-levels]({REC}returning-novelty-forgetting-on-levels.md)).',
        '- Activity read off one exchange as exchanging and drawing as taking, only active relata give and only active relata take '
        'what they draw on, for every flow; with the rest of the whole counted every world balances, balance being exactly the rest '
        'never active; under a law of exchange, with requirement read as what the exchange responds to when a condition falls below a '
        'need, activity needs support for every need, so the four tying premises hold with no premise; requirement is a counterfactual '
        'of the law, one course being generated by laws differing in requirement (`Flow.readOff_acting`, `Flow.readOff_taking`, '
        '`World.withRest_balanced`, `World.withRest_closed_iff`, `ExchangeLaw.readWorld_glue`, '
        '`ExchangeLaw.requirement_beyond_course`, `Becoming.Reading`).',
        '- Whatever reads an unfolding is a reading in context: the registrations of a contextual system along a run are always the '
        'relata of one world, with no gluing, quantum registrations included; the standing and the exchange read a change across a step '
        'alike exactly where the flow balances there, so `World`\'s balance is the gluing of two readings; with the rest counted the '
        'two readings of every world glue at every step, and it is one run of the law of exchange (`Contextual.world`, '
        '`Flow.changeReadings_glue_iff`, `Flow.changeReadings_free_iff`, `World.unity`, `Becoming.Readings`).'])
    row_anchor = next(l for l in s.split('\n') if l.startswith('| 一个关系的起点 |'))
    row_new = ('| 不以 `World` 为起点 | 已陈述并检查，不加前提（Ren 2026-10-14 批准从关系开始的重建，'
               f'[来源]({src})）：回返、新与遗忘只用水平陈述，部分的状态写在规律之内'
               f'（[returning-novelty-forgetting-on-levels]({REC}returning-novelty-forgetting-on-levels.md)）；从交换读出、算入整体的其余，'
               f'四个联结前提由读法成立，余下的是部分的状态（[premises-read-off-the-exchange]({REC}premises-read-off-the-exchange.md)）；'
               '读一个展开的都是语境中的读法，`World` 是粘合的读法，算入其余时每个世界都是交换之律的一次运行'
               f'（[unity-of-readings]({REC}unity-of-readings.md)）。开放：其余在实际展开中是什么；已落地规律的陈述是否改写为其余闲置；'
               '连续时间与实数的量 |')
    choice_zh_old = ('- 一个关系的起点：起点是否读作 `World`，带标签的过程与框架是否读作它的读法；“行动不是展开之外的第二种原因”是否是 Ren 的读法；')
    choice_zh_new = ('- 一个关系的起点：起点不读作 `World`：Ren 2026-10-14 问“why do we need "World"?”，并批准以语境中的读法为一般情形、'
                     f'`World` 为诸读法粘合的情形（[unity-of-readings]({REC}unity-of-readings.md)），带标签的过程与框架和 `World` 同是一个展开的'
                     '读法；仍待 Ren：“行动不是展开之外的第二种原因”是否是 Ren 的读法；')
    choice_en_old = ('- One relational starting point: whether the starting point reads as `World`, with the labelled process and '
                     'the frame as its readings; whether “an agent\'s choice is not a second kind of cause beside the unfolding” is '
                     'Ren\'s reading;')
    choice_en_new = ('- One relational starting point: the starting point does not read as `World`: on 14 October 2026 Ren asked '
                     '“why do we need "World"?” and approved the readings in context as the general case, with `World` the case '
                     f'where they glue ([unity-of-readings]({REC}unity-of-readings.md)), the labelled process and the frame being '
                     'readings of one unfolding as `World` is; pending Ren: whether “an agent\'s choice is not a second kind of cause '
                     'beside the unfolding” is Ren\'s reading;')
    zh_choice_line = next(l for l in s.split('\n') if l.startswith('- 一个关系的起点：起点是否读作'))
    en_choice_line = next(l for l in s.split('\n') if l.startswith('- One relational starting point: whether the starting point'))
    refound_zh = ('- 从关系开始的重建：部分的状态是否读作像曲率那样是一个区域的状态；新而不止是否读作来自部分之外的无界增益；有界的当下是否读作不能承载'
                  '自身的历史；其余的交换是否读作所立与交换两种读法之差；在同样的不变标准下意义不停在边界上，公理归于预设（读法是 AI 的）。')
    refound_en = ('- The relation-first re-founding: whether a state of a part reads as curvature is a state of a region; novelty without '
                  'end as gain without bound from beyond the part; a bounded present as unable to hold its own history; the rest\'s '
                  'exchange as the difference between the standing\'s and the exchange\'s readings of change; and significance, under '
                  'the same standard of invariance, as stopping at no boundary, the axiom coming to the presupposition (the AI\'s '
                  'readings).')
    scope_zh_old = '（离散的步、自然数的量、把条件与关系项对应起来的共同索引）；不能这样表示的部分'
    scope_zh_new = ('（离散的步、自然数的量；把条件与关系项对应起来的共同索引只在诸读法粘合成 `World` 时需要：语境中的读法总是一个世界，'
                    '`Contextual.world`，研究 §124）；不能这样表示的部分')
    scope_en_old = '(discrete steps, natural-number amounts, a shared index identifying conditions with relata); where it cannot'
    scope_en_new = ('(discrete steps, natural-number amounts; a shared index identifying conditions with relata is needed only where '
                    'the readings glue into `World`, the readings in context always being one world, `Contextual.world`, study '
                    'section 124); where it cannot')
    imb_row_old = '不平衡作为关系项，先证等价（Ren 2026-10-11：“please”；是否采用由 Ren 定）：'
    imb_row_new = '不平衡作为关系项，先证等价（Ren 2026-10-11：“please”；Ren 2026-10-14 采用，见 `Becoming.Reading`）：'
    imb_row_end_old = '恰当它们在原流上成立且流在那里平衡；不采用 | 15 |'
    imb_row_end_new = '恰当它们在原流上成立且流在那里平衡；采用之后已落地的规律保留其陈述 | 15 |'
    post_row = next(l for l in s.split('\n') if l.startswith('| L3 | [Becoming.Postponement]'))
    rows = '\n'.join([
        f'| L3 | [Becoming.Novelty]({LINK}Novelty.lean) | 只用水平的回返、新与遗忘（不加前提，部分的状态写在规律之内）：存量在界内的家族回返；'
        '在不多于界内构型数的各步都新的家族在其中某步超出界，每步都新的家族超出每个界；在界内的家族与有限的整体不承载其交换的历史；每次变化都下降时'
        '变化不无尽复现；熵在第一律之下的形式是其情形。/ Returning, novelty and forgetting on the levels alone, with no premise, each '
        'law\'s condition a state of the part: a family whose stock stays within a bound returns; a family new at each of as many '
        'steps as there are configurations within a bound exceeds it at one of them, and one new at every step exceeds every bound; '
        'a bounded family and a finite whole do not carry the history of their exchanges; with loss at each change, change does not '
        'recur without end; Entropy\'s forms under the first law are cases. | 19 |',
        f'| L4 | [Becoming.Reading]({LINK}Reading.lean) | 从交换读出（不加前提；Ren 2026-10-14 采用其余作为关系项）：把活跃读作交换、汲取读作所取，'
        '只有活跃者给与取对每个流成立；每个世界算入其余都平衡，平衡恰是其余从不活跃；交换之律下把要求读作交换所回应的，活动需要支持，四个联结前提都不用'
        '前提；要求是律的反事实，同一历程可由要求不同的律生成。/ Read off the exchange, with no premise (the rest adopted as a relatum by '
        'Ren, 14 October 2026): with activity read as exchanging and drawing as taking, only active relata give and take, for every '
        'flow; every world with its rest counted balances, balance being exactly the rest never active; under a law of exchange, with '
        'requirement read as what the exchange responds to, activity needs support, so the four tying premises hold with no premise; '
        'requirement is a counterfactual of the law, one course being generated by laws differing in requirement. | 34 |',
        f'| L4 | [Becoming.Readings]({LINK}Readings.lean) | 一个展开在语境中的读法（不加前提）：一个运行在语境中的诸读法总是一个世界的被索引的主张，'
        '不用粘合；平衡是所立与交换两种变化读法的粘合；算入其余，每个世界都是交换之律的一次运行；在同样的不变标准下意义不停在边界上（Boundaries 的重述）。'
        '/ One unfolding read in context, with no premise: the readings in context of a run are always one world of indexed claims, '
        'with no gluing; balance is the gluing of the standing\'s and the exchange\'s readings of change; with the rest counted every '
        'world is one run of the law of exchange; under the same standard of invariance no significance stops at a boundary (a '
        'restatement of Boundaries). | 13 |'])
    gloss_old = '两种表示逐步等价；是否采用由 Ren 定（`Becoming.Imbalance`） |'
    gloss_new = '两种表示逐步等价；Ren 2026-10-14 采用（`Becoming.Imbalance`、`Becoming.Reading`） |'
    gloss_row = next(l for l in s.split('\n') if l.startswith('| 不平衡关系项 | imbalance relatum |'))
    gloss_rest = ('| 整体的其余 | rest of the whole | 算作关系项 `none` 的不平衡：它给每个条件其水平超出流的净交换而升的部分，取其超出而降的部分，从不要求什么；'
                  '算入它，每个流都平衡，平衡恰是它闲置；它的交换由水平与形成的交换之差读出，不是观察；Ren 2026-10-14 采用（`Becoming.Reading`） | '
                  '`Flow.withImbalance`、`World.withRest`、`World.withRest_closed_iff` |')
    edit(CH, [(item1_zh_old, item1_zh_new), (item1_en_old, item1_en_new), (item3_zh_old, item3_zh_new),
              (item3_en_old, item3_en_new), (each_zh_old, each_zh_new), (each_en_old, each_en_new),
              (zh_learn + '\n', zh_learn + '\n' + zh_bullets + '\n'), (en_learn + '\n', en_learn + '\n' + en_bullets + '\n'),
              (row_anchor + '\n', row_anchor + '\n' + row_new + '\n'),
              (choice_zh_old, choice_zh_new), (choice_en_old, choice_en_new),
              (scope_zh_old, scope_zh_new), (scope_en_old, scope_en_new),
              (imb_row_old, imb_row_new), (imb_row_end_old, imb_row_end_new),
              (post_row + '\n', post_row + '\n' + rows + '\n'),
              (gloss_old, gloss_new)])
    # the two new choice bullets follow the starting-point bullets, which the edit above has just rewritten
    s = (ROOT / CH).read_text()
    zh_line = next(l for l in s.split('\n') if l.startswith('- 一个关系的起点：起点不读作 `World`'))
    en_line = next(l for l in s.split('\n') if l.startswith('- One relational starting point: the starting point does not read as'))
    gl = next(l for l in s.split('\n') if l.startswith('| 不平衡关系项 | imbalance relatum |'))
    edit(CH, [(zh_line + '\n', zh_line + '\n' + refound_zh + '\n'), (en_line + '\n', en_line + '\n' + refound_en + '\n'),
              (gl + '\n', gl + '\n' + gloss_rest + '\n')])
    del zh_choice_line, en_choice_line, gloss_row


def plan():
    path = '_process/research/2026-10-05-generative-foundation-review/root-foundation/ZERO-PREMISE-PLAN.md'
    src = '../../../../sources/15-codex-theory-conversations/2026-10-14-relation-first-refounding.md'
    edit(path, [
        ('每个流都平衡，平衡恰是新增关系项的闲置，活动的前提逐步等价；是否采用由 Ren 定。',
         '每个流都平衡，平衡恰是新增关系项的闲置，活动的前提逐步等价；是否采用由 Ren 定。已决定（Ren 2026-10-14：“please, finish all”，'
         f'[原话]({src})）：采用。`Becoming.Reading` 在每个世界中算入其余（`World.withRest`），从交换读出活跃与汲取：平衡、只有活跃者给与取、'
         '对交换之律的活动需要支持由读法成立，封闭读作其余闲置；已落地的规律保留其陈述（P107，研究 §124）。'),
        ('两者都属于重新奠定表示；Ren 2026-10-11 的决定见上，是否采用不平衡关系项仍由 Ren 定。',
         '两者都属于重新奠定表示；Ren 2026-10-11 的决定见上；不平衡关系项已由 Ren 2026-10-14 采用（见上）。'),
        ('and the activity premises are equivalent step by step; whether to adopt it is Ren\'s.',
         'and the activity premises are equivalent step by step; whether to adopt it is Ren\'s. Decided (Ren, 14 October 2026: '
         f'“please, finish all”, [words]({src})): adopted. `Becoming.Reading` counts the rest in every world (`World.withRest`) and '
         'reads activity and drawing off the exchange: balance, only active relata giving and taking, and activity needing support '
         'under a law of exchange hold by reading, and closure reads as the rest idle; the landed laws keep their statements (P107, '
         'study section 124).'),
        ('Both re-found the representation; Ren\'s decisions of 11 October 2026 are above, and whether to adopt the imbalance '
         'relatum is still Ren\'s.',
         'Both re-found the representation; Ren\'s decisions of 11 October 2026 are above, and the imbalance relatum was adopted '
         'by Ren on 14 October 2026 (above).'),
    ])


IMBALANCE_OLD = """* `Becoming.Imbalance` (L3): imbalance counted as a relatum, proved equivalent first (Ren,
  11 October 2026: "please"; adoption is Ren's). Wherever the flow does not balance, the
  difference is counted as the exchange of one more relatum, never active and requiring
  nothing; then every flow balances, the flow balances on a family across a step exactly where
  that relatum is idle there, and on a family across a step the activity premises hold of the
  extended flow exactly where they hold of the flow and it balances there. Nothing is adopted:
  the laws of the core keep balance as a local condition. The readings are the AI's, pending
  Ren.
"""
IMBALANCE_NEW = """* `Becoming.Imbalance` (L3): imbalance counted as a relatum, proved equivalent first (Ren,
  11 October 2026: "please"), adopted by Ren on 14 October 2026 (`Becoming.Reading`). Wherever
  the flow does not balance, the difference is counted as the exchange of one more relatum,
  never active and requiring nothing; then every flow balances, the flow balances on a family
  across a step exactly where that relatum is idle there, and on a family across a step the
  activity premises hold of the extended flow exactly where they hold of the flow and it
  balances there. Adopted, the landed laws keep their statements, with balance a local
  condition read as the rest idle. The readings are the AI's, pending Ren.
"""


def root_module():
    path = LEANDIR + '/Becoming.lean'
    s = (ROOT / path).read_text()
    last_import = [l for l in s.split('\n') if l.startswith('import ')][-1]
    notes = '\n'.join([
        '* `Becoming.Novelty` (L3): returning, novelty and forgetting on the levels alone, with no premise.',
        '  Each law\'s condition is a state of the part written into it: a family whose stock stays within a',
        '  bound returns; a family new at each of as many steps as there are configurations within a bound',
        '  exceeds the bound at one of them, so what is new at every step exceeds every bound; no reading of a',
        '  bounded configuration gives a record that never repeats or a count without bound, so a bounded',
        '  family exchanged with without end, and a finite whole, forget; with loss at each change, change does',
        '  not recur without end. Entropy\'s forms under the first law are cases.',
        '* `Becoming.Reading` (L4): activity, drawing and requirement read off the exchange, with no premise',
        '  (Ren, 14 October 2026: "please, finish all", adopting the rest of the whole as a relatum). With',
        '  activity read as exchanging and drawing as taking, only active relata give and take, for every flow;',
        '  with the rest counted, every world balances and its balance is exactly the rest never active; under',
        '  a law of exchange, with requirement read as what the exchange responds to, activity needs support,',
        '  so the four premises tying readings of one exchange hold with no premise, and requirement is a',
        '  counterfactual of the law that no course fixes. The readings are the AI\'s, pending Ren.',
        '* `Becoming.Readings` (L4): one unfolding, read in context, with no premise. The readings in context',
        '  of a run are always one world of indexed claims, with no gluing; a description free of context is a',
        '  gluing; balance is the gluing of the standing\'s and the exchange\'s readings of change, and with the',
        '  rest counted every world is one run of the law of exchange. Under the same standard of invariance,',
        '  significance from a standpoint holds within a boundary only by holding for everything, a',
        '  restatement of `Becoming.Boundaries`. The readings are the AI\'s, pending Ren.'])
    tail = '\nThe core imports nothing else, every source declaration has an empty axiom report, and'
    edit(path, [
        (last_import + '\n', last_import + '\nimport Becoming.Novelty\nimport Becoming.Reading\nimport Becoming.Readings\n'),
        (tail, '\n' + notes + '\n' + tail),
        (IMBALANCE_OLD, IMBALANCE_NEW),
    ])


def checker():
    path = LEANDIR + '/check_becoming.py'
    edit(path, [('"Becoming.Boundaries", "Becoming.Relevance", "Becoming"',
                 '"Becoming.Boundaries", "Becoming.Novelty", "Becoming.Reading", "Becoming.Readings", "Becoming.Relevance", "Becoming"')])


if __name__ == '__main__':
    study()
    chapter()
    plan()
    root_module()
    checker()
    print('documents and registration edited')
