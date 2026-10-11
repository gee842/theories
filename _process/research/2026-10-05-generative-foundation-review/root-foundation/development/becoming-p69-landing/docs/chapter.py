"""Chapter edits for P69, as (kind, anchor, text) edits applied by apply_docs.py.

kind: 'before' inserts text before the line starting with anchor (a blank line after a paragraph,
none after a list item or table row); 'after_line' inserts text as new lines after the line starting
with anchor; 'replace' replaces the exact substring anchor with text. Every anchor must occur once.
Several anchors are lines the P64–P68 package adds, so these edits apply after it.
Placeholders {LEAN}, {STUDY_UNFOLDING}, {S_UNFOLDING} and {N_UNFOLDING} are filled by apply_docs.py.
"""

SOURCE = '../../../sources/15-codex-theory-conversations/2026-10-12-relational-starting-point.md'
AGREED = '../../../sources/15-codex-theory-conversations/2026-10-12-no-two-realities.md'
REC_A = '../results/records/process-and-frame-as-readings.md'
REC_B = '../results/records/configurations-alike-by-relation.md'

OPEN_ZH_OLD = '**机制。** 起点是过程：一个配置经一次可容许的变化成为另一个配置。'
OPEN_ZH_NEW = ('**起点。** 起点是一个展开：一类读法的关系项，每一步各自取、给、立于、需要与汲取什么（`World`，见下文“整体与其部分”）。'
               '过程是它的一种读法：一个配置经一次可容许的变化成为另一个配置；动作可以读入配置，律所留开的就是下一个动作。'
               '框架是另一种读法：每个配置上实现哪些主张。两种读法都回到同一展开：这是 P69 的结果，不是 Ren 的措辞（见下）。')
OPEN_EN_OLD = '**Mechanism.** The starting point is the process: a configuration becomes another through an admissible change.'
OPEN_EN_NEW = ('**Starting point.** The starting point is one unfolding: relata read with one kind, with what each takes, gives, '
               'stands at, needs and draws at each step (`World`, below under the whole and its parts). The process is one '
               'reading of it: a configuration becomes another through an admissible change; the move can be read within the '
               'configuration, and what the law leaves open is the next move. The frame is another: which claims are realized '
               "at each configuration. Both readings return to the one unfolding: this is P69's result, not Ren's wording (below).")

UNF_ZH = (
    '**一个展开与它的读法（第一部分，P69）。** Ren 问核心的前两层“is this dualistic?”（[来源](' + SOURCE + ')）。'
    '它们不设主体与客体，但其形式把四种分割当作给定：配置与取自另一字母表的动作、先于所支配历史的律、从配置读出的主张、先于其间关系的配置。'
    '`World` 不取其中任何一个；这里从世界一侧陈述这四种分割，不加前提（[Becoming.Unfolding]({LEAN}/Unfolding.lean)）。'
    '**动作是展开的一部分。** 动作读入配置时运行不变，律留开下一个动作，恰当原来确定且每步只有一个动作时确定（`withMove_determined_iff`）；'
    '动作由配置的策略在内形成时，确定的律仍确定，从同一配置出发的运行每一步都相同（`closedBy_runs_agree`）；'
    '部分之间，共享的动作是一种关系：各自先忘掉动作，两个分岔的部分就能同时走不同的路（`Fork.label_couples`）。'
    '世界的动作是关系项的交换：世界平衡，恰当其水平以交换为动作按交换之律运行（`World.balances_iff_exchange`）；'
    '交换从一个起点固定所立，所立不固定交换（`exchange_runs_agree`、`Circulation`）。'
    '**历史固定它所显示的律。** 每段历史是它所显示之律的运行，是它为其运行的最小的律，恰在历史从不以同一动作把同一配置带到两处时确定，'
    '恰在这时有确定的律容许它（`shown_le_iff`、`shown_determined_iff`、`exists_law_iff`）；先于历史给出的律所多出的，是未取的动作，记录不固定它们。'
    '对应不是同一：律可以有一步而没有历史（`DeadEnd.no_history`）；历史重访之处，它所显示的律容许它没有走过的历史（`Splice.spliced`）；'
    '保留历史时只容许它（`Run.keepHistory_shown`），代价是从不返回（`Becoming.Recurrence`）。'
    '**主张是关系项。** 沿运行的框架是一个世界，关系项是主张，恰在实现处活跃；新实现就是生起，所以活动的规律对主张成立；'
    '以配置为主张，每个运行是一个固定它的世界（`Frame.world`、`Frame.novel_iff_arises`、`Frame.claims_recur_iff`、`Frame.world_fixes_run`）。'
    '**配置由它怎样关系而定。** 互模拟所联系的配置相同：实现同样的主张，以同样的动作到相同的配置；相同是等价关系，'
    '相同的配置通过同样的检验（`Alike`、`Alike.tests`）；描述有意义，恰当它恰把相同者等同，这时它在等同什么上唯一，框架相同之下确定时承载规律（`makesSense_iff`、`MakesSense.unique`、`MakesSense.carries`）。外围的关系的同一（`RelationalDynamics`，2026-10-06；`ExplanatoryBranching` 的分支检验）'
    '由桥接证明就是这一个。作为相等的确定性依赖于命名：双胞胎的两个后继在每个关系上相同，与一个确定的框架相同，而自身不确定（`Twins.alike_one`）；'
    '相同之下的确定性沿相同传递（`DeterminedAt.transfer`）；交换之律下，水平相同恰当在每个关系项上相等（`exchange_alike_iff`）。'
    '读法：律与历史是同一展开的两种读法，律从展开读出，不是置于其上；对这一读法 Ren 写道“yes, i do agree with your reading, there are no two realities”'
    '（[来源](' + AGREED + ')）。其余读法是 AI 的，待 Ren：起点是 `World`，带标签的过程与框架是它的读法，两个方向都已证明；'
    '行动不是展开之外的第二种原因；律与历史之间的差别是记忆；认识在展开之内；配置的名字不承载任何东西。'
    '不推出：共同的步序；动作在展开之内形成与否、由什么形成；一个形成把它的历史读作哪条律；经同样检验的配置相同；'
    '第一部分以 `Determined` 陈述的定理在相同之下成立。`GenerativeCore` 不变，这是读法、两个方向的定理与桥接，不是另一个基础。'
    '见[研究 §{S_UNFOLDING}]({STUDY_UNFOLDING})与 [process-and-frame-as-readings](' + REC_A + ')、'
    '[configurations-alike-by-relation](' + REC_B + ')。')

UNF_EN = (
    '**One unfolding and its readings (Part I, P69).** Ren asked of the core\'s first two layers “is this dualistic?”. '
    'They posit no subject and object, but their form takes four splits as given: a configuration and a move drawn from '
    'an alphabet of its own, a law prior to the history it governs, claims read off a configuration, and configurations '
    'prior to their relation. `World` takes none of them, and the four splits are stated here from the world\'s side, '
    'with no premise. The move is part of what the unfolding is: read within the configuration it changes no run, and '
    'what the law leaves open is the next move; formed within by a policy, runs from one configuration agree at every '
    'step; between parts, a shared move is a relation; a world\'s move is its relata\'s exchange, balance is running by '
    'the law of exchange, and the exchange fixes the standings from a beginning while the standings do not fix the '
    'exchange. A history fixes the law it shows, the least law it is a run of, determined exactly where the history is '
    'consistent; the correspondence is not an identity, a law having a step and no history and a revisiting history '
    'showing a law that admits a history it never took, and it closes where the history is kept, at the price that a '
    'kept history never returns. A claim is a relatum, and novelty is arising. A configuration is how it relates: '
    'configurations related by a bisimulation are alike and pass the same tests, and a description makes sense where it identifies exactly the alike ones, carrying a law where the frame is determined up to likeness; the bridge identifies the periphery\'s '
    'relational identity with this one; determinacy as equality depends on names, and determinacy up to likeness passes '
    'along likeness. Ren confirmed the reading that law and history are one unfolding read two ways, the law read off '
    'the unfolding rather than set over it: “yes, i do agree with your reading, there are no two realities”. The rest '
    'are the AI\'s readings, pending Ren. Not derived: the shared index of steps; that a move is formed within, or by '
    'what; which law a formation takes its history to show; that configurations passing the same tests are alike; that '
    'Part I\'s theorems stated with `Determined` hold up to likeness. `GenerativeCore` is unchanged: this is a reading '
    'with theorems in both directions and a bridge, not another foundation.')

FULL_ZH_OLD = '哪个条件就是哪个关系项，由表示的共同索引给出。〔表示〕'
FULL_ZH_NEW = ('哪个条件就是哪个关系项，由表示的共同索引给出。带标签的过程与框架是这一整体的读法，不是它的根据：动作读入配置而不失去什么，'
               '世界的动作是关系项的交换；每段历史是它所显示之律的运行，律与历史的对应不是同一，差别是记忆；主张是关系项；'
               '配置的相同由互模拟刻画（`Becoming.Unfolding`，P69，定理；律与历史是同一展开的两种读法经 Ren 确认，其余读法待 Ren）。〔表示〕')
FULL_EN_OLD = "Which condition is which relatum is supplied by the representation's shared index. [representation]"
FULL_EN_NEW = ("Which condition is which relatum is supplied by the representation's shared index. The labelled process "
               "and the frame are readings of this whole, not its ground: the move is read within the configuration with "
               "nothing lost, and a world's move is its relata's exchange; every history is a run of the law it shows, the "
               "correspondence of law and history not being an identity, the gap being memory; a claim is a relatum; "
               "configurations are alike by bisimulation (`Becoming.Unfolding`, P69, theorems; that law and history are one "
               "unfolding read two ways Ren confirmed, the other readings pending Ren). [representation]")

WHOLE_I_ZH = ('- 过程与框架是同一展开的读法：动作读入配置时运行不变，律留开下一个动作；世界的动作是关系项的交换，平衡恰是按交换之律运行；'
              '每段历史是它所显示之律的运行，那是最小的律，恰在历史一致处确定；律可以有一步而没有历史，历史重访处它所显示的律容许它没有走过的历史，'
              '保留历史时只容许它；主张是关系项，新实现就是生起；互模拟所联系的配置相同，通过同样的检验（`withMove_determined_iff`、'
              '`World.balances_iff_exchange`、`shown_le_iff`、`exists_law_iff`、`DeadEnd.no_history`、`Splice.spliced`、'
              '`Run.keepHistory_shown`、`Frame.novel_iff_arises`、`Alike.tests`，P69）。')
WHOLE_I_EN = ('- The process and the frame are readings of one unfolding: read within the configuration the move changes no '
              'run, and the law leaves the next move open; a world\'s move is its relata\'s exchange, and balance is running '
              'by the law of exchange; every history is a run of the law it shows, the least one, determined exactly where '
              'the history is consistent; a law can have a step and no history, a revisiting history shows a law admitting '
              'a history it never took, and a kept history only itself; a claim is a relatum and novelty is arising; '
              'configurations related by a bisimulation are alike and pass the same tests (`withMove_determined_iff`, '
              '`World.balances_iff_exchange`, `shown_le_iff`, `exists_law_iff`, `DeadEnd.no_history`, `Splice.spliced`, '
              '`Run.keepHistory_shown`, `Frame.novel_iff_arises`, `Alike.tests`, P69).')

WHOLE_III_ZH = ('- **动作与律从哪里来。** 动作在展开之内形成与否、由什么形成，不由动力学决定：律只留开下一个动作（`withMove_open`）。'
                '一个形成把它的历史读作显示哪条律，也不由它决定：历史重访之处，所显示的律容许它没有走过的历史（`Splice.spliced`）。'
                '作为相等的确定性依赖于配置怎样命名（`Twins.alike_one`）。')
WHOLE_III_EN = ('- **Where moves and laws come from.** Whether a move is formed within the unfolding, and by what, is not '
                'decided by the dynamics: the law only leaves the next move open (`withMove_open`). Nor is which law a '
                'formation takes its history to show: where a history revisits, the law it shows admits a history it never '
                'took (`Splice.spliced`). Determinacy as equality depends on how configurations are named (`Twins.alike_one`).')

STATUS_ROW = ('| 一个关系的起点（P69） | 已陈述并检查，不加前提：过程与框架是同一展开的读法，动作读入配置，世界的动作是关系项的交换，'
              '每段历史是它所显示之律的运行，对应不是同一而在保留历史时合上，主张是关系项（[process-and-frame-as-readings](' + REC_A + ')）；'
              '配置由互模拟定为相同，作为相等的确定性依赖于命名，桥接把外围的关系的同一认同为核心的'
              '（[configurations-alike-by-relation](' + REC_B + ')）；律与历史的读法经 Ren 确认，其余读法待 Ren；共同的步序仍是表示的承诺 |')

CHOICE_ZH = ('- 一个关系的起点（P69）：起点是否读作 `World`，带标签的过程与框架是否读作它的读法；“行动不是展开之外的第二种原因”是否是 Ren 的读法；'
             '主张作为关系项的读法；配置的同一是否读作相同（互模拟）。律与历史是同一展开的两种读法已由 Ren 确认（“there are no two realities”）。')
CHOICE_EN = ('- One relational starting point (P69): whether the starting point reads as `World`, with the labelled process and '
             'the frame as its readings; whether “an agent\'s choice is not a second kind of cause beside the unfolding” is '
             'Ren\'s reading; the reading of claims as relata; whether the identity of configurations reads as likeness '
             '(bisimulation). That law and history are one unfolding read two ways Ren has confirmed (“there are no two realities”).')

FURTHER_ZH = ('- 一个关系的起点：第一部分以 `Determined`（相等）陈述的定理在相同之下重述（`DeterminedAt`），或说明何处需要相等'
              '（例如合并）；核心中经同样检验推出相同的构造性条件；动作在展开之内形成的条件；从关系推出共同的步序；主张之间的关系作为 '
              '`Frame.world` 的流与依存。')
FURTHER_EN = ('- One relational starting point: restating the Part I theorems stated with `Determined` (equality) up to '
              'likeness (`DeterminedAt`), or saying where equality is needed (merging, for one); a constructive condition in '
              'the core under which passing the same tests makes configurations alike; when a move is formed within the '
              'unfolding; deriving the shared index of steps from relations; relations among claims as the flow and web of '
              '`Frame.world`.')

SPINE_L3 = ('| L3 | [Becoming.Unfolding]({LEAN}/Unfolding.lean) | 一个展开与它的读法（不加前提，P69）：动作读入配置时运行不变，律留开下一个动作，'
            '由策略在内形成时运行处处相同，部分之间共享的动作是关系；世界的动作是关系项的交换，平衡恰是按交换之律运行，交换从起点固定所立，'
            '所立不固定交换；每段历史是它所显示之律的运行，最小的律，恰在历史一致处确定；死路与拼接，保留历史时对应合上；主张是关系项，'
            '新实现就是生起；互模拟的相同是等价关系，相同的配置通过同样的检验，有意义的描述恰把相同者等同并承载规律，作为相等的确定性依赖于命名，相同之下的确定性沿相同传递；'
            '水平相同恰当逐点相等 | {N_UNFOLDING} |')

GLOSS_PROCESS_OLD = '| 过程 | process | 声明可容许的变化 | `Generative.Process` |'
GLOSS_PROCESS_NEW = ('| 过程 | process | 声明可容许的变化；同一展开把配置分为律所固定者与所留开者（动作）的读法，动作可以读入配置（P69） | '
                     '`Generative.Process`、`withMove` |')
GLOSS_FRAME_OLD = '| 框架 | frame | 过程加上每个配置实现的主张 | `Frame` |'
GLOSS_FRAME_NEW = '| 框架 | frame | 过程加上每个配置实现的主张；沿运行读作以主张为关系项的世界（P69） | `Frame`、`Frame.world` |'
GLOSS_NEW = '\n'.join([
    '| 交换 | exchange | 世界跨一步的动作：在场的关系项取与给什么；交换之律说每个关系项一步之后的水平连同被取的等于之前的连同被给的，世界平衡恰是按它运行 | '
    '`Exchange`、`exchange`、`World.move`、`World.balances_iff_exchange` |',
    '| 所显示的律 | law shown | 一段历史所走过的各步；历史为其运行的最小的律，恰在历史一致处确定；对应不是同一，保留历史时合上 | '
    '`Shown`、`shown_le_iff`、`exists_law_iff`、`Run.keepHistory_shown` |',
    '| 相同／互模拟 | alike / bisimulation | 互模拟所联系的配置：实现同样的主张，以同样的动作到相同的配置；等价关系，相同的配置通过同样的检验 | '
    '`Bisimulation`、`Alike`、`Alike.tests` |',
    '| 相同之下确定 | determined up to likeness | 同一动作的任何两个结果相同；沿相同传递；作为相等的确定性依赖于命名 | '
    '`DeterminedAt`、`DeterminedAt.transfer`、`Twins.alike_one` |',
    '| 有意义的描述 | description that makes sense | 恰把相同的配置等同的描述；在等同什么上唯一，框架相同之下确定时承载规律；不分任何东西的描述总承载规律，却只在一切都相同时有意义 | '
    '`MakesSense`、`makesSense_iff`、`MakesSense.carries` |',
])

EDITS = [
    ('replace', OPEN_ZH_OLD, OPEN_ZH_NEW),
    ('replace', OPEN_EN_OLD, OPEN_EN_NEW),
    ('before', '**形成、维持、转化、退化与消解都是沿运行的关系变化，不是五个阶段。**', UNF_ZH + '\n\n' + UNF_EN),
    ('replace', FULL_ZH_OLD, FULL_ZH_NEW),
    ('replace', FULL_EN_OLD, FULL_EN_NEW),
    ('after_line', '- 每个确定的律恰吸入不返回者', WHOLE_I_ZH),
    ('after_line', '- Every determined law draws exactly what does not return', WHOLE_I_EN),
    ('before', '- **意义。** 规律与定理不给任何部分以意义', WHOLE_III_ZH),
    ('before', '- **Significance.** The laws and theorems give no part significance', WHOLE_III_EN),
    ('after_line', '| 与一般因果系统的比较（P64–P68） |', STATUS_ROW),
    ('before', '- 名称：本理论中由 AI 拟定的用语', CHOICE_ZH),
    ('before', '- Names: the terms the AI has proposed', CHOICE_EN),
    ('after_line', '- 反馈与所及：他者有回应的比较', FURTHER_ZH),
    ('after_line', '- Feedback and reach: a comparison in which others respond', FURTHER_EN),
    ('after_line', '| L3 | [Becoming.Space]', SPINE_L3),
    ('replace', GLOSS_PROCESS_OLD, GLOSS_PROCESS_NEW),
    ('replace', GLOSS_FRAME_OLD, GLOSS_FRAME_NEW),
    ('after_line', '| 世界 | world |', GLOSS_NEW),
]
