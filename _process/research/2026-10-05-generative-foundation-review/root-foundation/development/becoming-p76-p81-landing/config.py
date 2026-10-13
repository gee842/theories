"""Run (a) of the landing queue (integrator's order, 10-12): P76 and P81 in one checker run, with the shared kit in
`../becoming-landing-kit/`. P76 lands first (study section S), P81 second (S + 1).

Anchors are lines of main after P69 (da8f75a7); P73 and P70–P72 land before this run, so the run is dry-run
against the main it lands on, and an anchor that has moved fails loudly rather than landing twice.
"""

LABEL = 'P76 + P81'

MOVE = '../../../sources/15-codex-theory-conversations/2026-10-12-move-towards-100.md'
SOURCE = 'sources/15-codex-theory-conversations/2026-10-12-move-towards-100.md'
REC = '../results/records/'

PACKAGES = [
    dict(
        module='Histories', package='becoming-p76-landing', key='HISTORIES', prefix='p76', after='Unfolding',
        scope_before='Attraction: for every determined law,',
        bullet="""* `Becoming.Histories` (L3): what histories fix (P76). A family of histories is the family of
  some law's histories exactly where it holds every sequence made of its own steps, and of a
  determined law's exactly where it is also consistent; two laws admit the same histories exactly
  where they have the same live steps, so laws up to their dead ends and families holding their
  splices correspond one to one, and with histories that stop no dead end remains. Where both
  frames are determined up to likeness, configurations are alike exactly where they pass the same
  tests; with branching they need not (`Choosing`). The readings are the AI's, pending Ren.""",
        scope=("Histories: the law a family of histories shows is the least law admitting each of them; a family "
               "is the family of some law's histories exactly where it holds every sequence made of its own steps, "
               "and of a determined law's exactly where it is also consistent; two laws admit the same histories "
               "exactly where they have the same live steps, the dead end's step not being live, and have the same "
               "finite histories exactly where they have the same steps; where both frames are determined up to "
               "likeness, configurations are alike exactly where they pass the same tests, the same courses open "
               "and the same claims realizable after each, while a frame choosing after its first move and one "
               "choosing at it pass the same tests and are not alike."),
        readme_zh=('历史固定什么（不加前提，P76）：一族历史恰在含有它的拼接时是某个律的历史族，还一致时是确定的律的；两个律恰在活的步相同时'
                   '容许同样的历史，所以不计死路的律与含有拼接的历史族一一对应；会停止的历史下没有死路；两个框架在相同之下确定时，'
                   '配置恰在通过同样的检验时相同，有分支时不然（`Choosing`）'),
        readme_en=("what histories fix (no premise, P76): a family of histories is a law's exactly where it holds its "
                   "splices, a determined law's where it is also consistent; two laws admit the same histories exactly "
                   "where they have the same live steps, so laws up to dead ends and families holding their splices "
                   "correspond one to one; with histories that stop no dead end remains; where both frames are "
                   "determined up to likeness, configurations are alike exactly where they pass the same tests, and not "
                   "with branching (`Choosing`)"),
        imports_zh=('`Unfolding` 导入 `Mechanism` 与 `Space`；', '`Unfolding` 导入 `Mechanism` 与 `Space`；`Histories` 导入 `Unfolding`；'),
        imports_en=('`Unfolding` imports `Mechanism` and `Space`;', '`Unfolding` imports `Mechanism` and `Space`; `Histories` imports `Unfolding`;'),
    ),
    dict(
        module='Branching', package='becoming-p81-landing', key='BRANCHING', prefix='p81', after='Histories',
        scope_before='Attraction: for every determined law,',
        bullet="""* `Becoming.Branching` (L3): R6's and P67's laws for every process, whose course branches
  (P81). A configuration that returns can be had at every step, and every configuration
  returns exactly where every region the process never leaves keeps every possibility of
  its own; keeping every possibility does not give returning, merging nothing gives it along
  runs, and a merge need not lose a possibility. Every process necessarily draws exactly
  what does not return; possibly drawn is losing oneself on some course and allows return.
  Determinacy is determinacy up to likeness with configurations named; the main theorems of
  `Experiment` and `Mechanism` stated with `Determined` are restated up to likeness, and
  those needing equality are named with witnesses. Capture's rule region is absorbing and a
  reform of the state alone is drawn into what the rule holds. The readings are the AI's,
  pending Ren.""",
        scope=("Branching: for every process, a configuration returns exactly where its own course can have it "
               "at the next step, and every configuration returns exactly where every region the process never "
               "leaves keeps every possibility of its own; a configuration that returns can be had at every step "
               "and has a run that never loses it; keeping every possibility does not give returning, merging "
               "nothing gives it along a run listed within finitely many configurations, and a merge need not lose "
               "a possibility; every process necessarily draws exactly what does not return, and possibly drawn is "
               "losing oneself on some course, which allows return on another; under a determined law each notion "
               "is R6's or P67's; determinacy is determinacy up to likeness where the claims name the "
               "configurations, theorems on how configurations relate hold up to likeness, and retargeting one of "
               "two alike configurations, an unregistered past and an unregistered description need equality; "
               "where a rule keeps itself its region is absorbing, and where the next configuration depends on the "
               "rule alone a reformed state is drawn into what the rule holds."),
        readme_zh=('路径分支时（不加前提，P81）：配置恰在它自己的路径下一步能再得到它时返回，处处返回恰是过程不离开的每个区域都保留它自己的'
                   '每个可能；保留每个可能不给返回，不合并沿运行给返回，合并不必失去可能；每个过程必然吸入的恰是不返回者，可能被吸入'
                   '允许在另一路径中返回；确定是相同之下确定的命名情形，需要相等之处有见证；Capture 的规则区域是吸收区域'),
        readme_en=("when the course branches (no premise, P81): a configuration returns exactly where its own course can "
                   "have it at the next step, and every configuration returns exactly where every region the process "
                   "never leaves keeps every possibility of its own; keeping every possibility does not give returning, "
                   "merging nothing gives it along runs, a merge need not lose a possibility; every process necessarily "
                   "draws exactly what does not return, and possibly drawn allows return on another course; "
                   "determinacy is the named case of determinacy up to likeness, with witnesses where equality is "
                   "needed; Capture's rule region is absorbing"),
        imports_zh=('`Histories` 导入 `Unfolding`；', '`Histories` 导入 `Unfolding`；`Branching` 导入 `Unfolding`、`Attraction` 与 `Capture`；'),
        imports_en=('`Histories` imports `Unfolding`;', '`Histories` imports `Unfolding`; `Branching` imports `Unfolding`, `Attraction` and `Capture`;'),
    ),
]

PLAN_ZH = '\n'.join([
    ('| P76 律与历史、检验与相同的完备 ✓ | 按 Ren 2026-10-12 的“move towards 100%”（[来源](../../../../' + SOURCE + ')）：强意义上的完备，'
     '此前只对计数成立。完成：新模块 `Becoming.Histories`（{N_HISTORIES} 项定理，L3，只导入 Unfolding（P69），不改已有模块），不加前提。'
     '一族历史恰在含有它的拼接时是某个律的历史族，还一致时是确定的律的（`family_iff`、`determined_family_iff`）；两个律恰在活的步相同时'
     '容许同样的历史（`same_histories_iff`），所以不计死路的律与含有拼接的历史族一一对应，P69 的死路与拼接就是律与历史之间的全部规律；'
     '会停止的历史下没有死路（`same_finite_histories_iff`）。两个框架在相同之下确定时，配置恰在通过同样的检验时相同'
     '（`alike_iff_sameTests`），有分支时不然（`Choosing.not_alike`）。记录 histories-fix-law-up-to-dead-ends、'
     'tests-fix-likeness-where-determined（F01）；研究 §{S_HISTORIES}。核心中分支检验固定相同的构造性证明开放。 |'),
    ('| P81 路径分支时 ✓ | 同一来源；R6 的三方等价对不确定的律不成立。完成：新模块 `Becoming.Branching`（{N_BRANCHING} 项定理，L3，'
     '导入 Unfolding、Attraction 与 Capture，不改已有模块），不加前提。返回的精确条件（`returns_iff_fed_ahead`、`returns_iff_keepsWithin`）；'
     '保留每个可能不给返回，合并不必失去可能，不合并沿运行给返回（`Transit.keeps_not_returns`、`OneWay.merge_keeps`、'
     '`Branching.Lossless.returns`）；每个过程必然吸入的恰是不返回者，可能被吸入允许返回（`necessarilyDrawn_iff_not_returns`、'
     '`OneWay.possibly_not_necessarily`）；确定是相同之下确定的命名情形，`Experiment` 与 `Mechanism` 的主要定理在相同之下重述，需要相等之处有见证'
     '（`determined_iff_named`、`Twins.retarget_breaks`）；Capture 的规则区域是吸收区域（`Law.rule_absorbing`）。记录 '
     'returning-where-the-course-branches、necessarily-drawn-is-not-returning、determinacy-up-to-likeness（F01）；研究 §{S_BRANCHING}。 |'),
])

PLAN_EN = '\n'.join([
    ("- **P76:** law and history, and likeness, complete, under Ren's \"move towards 100%\" of 12 October 2026 "
     '([source](../../../../' + SOURCE + ')): completeness in the strong sense, which had held for counting only. '
     'Done: `Becoming.Histories` ({N_HISTORIES} theorems, L3, importing Unfolding (P69) only, changing no existing '
     "module), with no premise. A family of histories is a law's exactly where it holds its splices, a determined law's "
     'where it is also consistent (`family_iff`, `determined_family_iff`); two laws admit the same histories exactly '
     "where they have the same live steps (`same_histories_iff`), so P69's dead ends and splices are the whole law of "
     'law and history; with histories that stop no dead end remains (`same_finite_histories_iff`). Where both frames '
     'are determined up to likeness, configurations are alike exactly where they pass the same tests '
     '(`alike_iff_sameTests`), not with branching (`Choosing.not_alike`). Records histories-fix-law-up-to-dead-ends '
     'and tests-fix-likeness-where-determined (F01); study §{S_HISTORIES}. A constructive proof that branching tests fix '
     'likeness in the core is open.'),
    ("- **P81:** when the course branches, from the same source, after R6's three-way equivalence was found to fail for "
     'laws that are not determined. Done: `Becoming.Branching` ({N_BRANCHING} theorems, L3, importing Unfolding, '
     'Attraction and Capture, changing no existing module), with no premise. The exact condition for returning '
     "(`returns_iff_fed_ahead`, `returns_iff_keepsWithin`); keeping every possibility does not give returning, a merge "
     'need not lose a possibility, merging nothing gives returning along runs (`Transit.keeps_not_returns`, '
     '`OneWay.merge_keeps`, `Branching.Lossless.returns`); every process necessarily draws exactly what does not return, '
     'and possibly drawn allows return (`necessarilyDrawn_iff_not_returns`, `OneWay.possibly_not_necessarily`); '
     'determinacy is the named case of determinacy up to likeness, the main theorems of Experiment and Mechanism are '
     'restated up to likeness, with witnesses where equality is needed (`determined_iff_named`, '
     "`Twins.retarget_breaks`); Capture's rule region is absorbing (`Law.rule_absorbing`). Records "
     'returning-where-the-course-branches, necessarily-drawn-is-not-returning and determinacy-up-to-likeness (F01); '
     'study §{S_BRANCHING}.'),
])

R76A = f'[histories-fix-law-up-to-dead-ends]({REC}histories-fix-law-up-to-dead-ends.md)'
R76B = f'[tests-fix-likeness-where-determined]({REC}tests-fix-likeness-where-determined.md)'
R81A = f'[returning-where-the-course-branches]({REC}returning-where-the-course-branches.md)'
R81B = f'[necessarily-drawn-is-not-returning]({REC}necessarily-drawn-is-not-returning.md)'
R81C = f'[determinacy-up-to-likeness]({REC}determinacy-up-to-likeness.md)'

P76_ZH = (
    '**历史固定什么（第一部分，P76）。** 按 Ren 的“move towards 100%”（[来源](' + MOVE + ')），P69 的死路与拼接就是律与历史之间的全部规律，'
    '不加前提（[Becoming.Histories]({LEAN}/Histories.lean)）。一族历史所显示的律以其中历史所走的步为步，是容许每段历史的最小的律；'
    '一族历史恰在含有它的拼接（由它自己的步组成的每个序列都在族中）时是某个律的历史族，恰在还一致时是某个确定的律的'
    '（`family_iff`、`determined_family_iff`）。两个律恰在活的步（某段历史所走的步）相同时容许同样的历史（`same_histories_iff`），'
    '所以不计死路的律与含有拼接的历史族一一对应。会停止的历史下死路消失：两个律恰在步相同时有同样的有限历史（`same_finite_histories_iff`）。'
    '两个框架处处在相同之下确定时，配置恰在通过同样的检验时相同（`alike_iff_sameTests`）；有分支时不然：在第一步之后选择与在第一步选择的'
    '两个框架通过同样的检验而不相同（`Choosing.not_alike`）。读法是 AI 的，待 Ren：从历史读出的律就是含有拼接的历史族，'
    '置于展开之上的律所能多出的只是没有历史显示的死路；拼接是记忆的缺席。不推出：实际展开的历史是否终止；核心中分支检验固定相同。'
    '见[研究 §{S_HISTORIES}]({STUDY_HISTORIES})与 ' + R76A + '、' + R76B + '。')
P76_EN = (
    "**What histories fix (Part I, P76).** Under Ren's “move towards 100%”, P69's dead ends and splices are the whole law "
    'of law and history, with no premise. The law a family of histories shows is the least law admitting each of them; a '
    "family is the family of some law's histories exactly where it holds every sequence made of its own steps, and of a "
    "determined law's exactly where it is also consistent. Two laws admit the same histories exactly where they have the "
    'same live steps, those some history takes, so laws up to their dead ends and families holding their splices '
    'correspond one to one; with histories that stop the dead end disappears. Where both frames are determined up to '
    'likeness, configurations are alike exactly where they pass the same tests; with branching they need not, a frame '
    "choosing after its first move and one choosing at it passing the same tests. The readings are the AI's, pending Ren: "
    'a law read off histories is a family holding its splices, and what a law set over the unfolding can add are dead '
    "ends no history shows; the splice is memory's absence. Not derived: whether an actual unfolding's histories stop; "
    'branching tests fixing likeness in the core.')

P81_ZH = (
    '**路径分支时（第一部分，P81）。** R6 与 P67 的规律对确定的律陈述；脊柱的过程只固定哪些步可容许，路径可以分支。这里对每个过程陈述它们，'
    '不加前提（[Becoming.Branching]({LEAN}/Branching.lean)）。配置恰在它自己的路径下一步能再得到它时返回；每个配置都返回，恰在过程从不离开的'
    '每个区域都保留它自己的每个可能时（`returns_iff_fed_ahead`、`returns_iff_keepsWithin`）。R6 的三方等价在分支时分开：保留每个可能不给返回'
    '（`Transit.keeps_not_returns`），合并不必失去可能（`OneWay.merge_keeps`），不合并在有限多配置之内沿每个运行给返回'
    '（`Branching.Lossless.returns`）。每个过程必然吸入的恰是不返回者（`necessarilyDrawn_iff_not_returns`）；可能被吸入是在某一路径中失去自身，'
    '可能被吸入者可以在另一路径中返回（`possiblyDrawn_iff`、`OneWay.possibly_not_necessarily`）。确定是相同之下确定的命名情形'
    '（`determined_iff_named`）；`Experiment` 与 `Mechanism` 中关于配置怎样相关的主要定理在相同之下成立，需要相等的是对相同者之一的干预、'
    '没有登记的过去与没有登记的描述（`Twins.retarget_breaks`、`keepHistory_new_named`、`carries_unregistered`）。Capture 的规则区域是吸收区域，'
    '只改状态会被吸回规则所持之处（`Law.rule_absorbing`、`Captured.state_reform_drawn`）。读法是 AI 的，待 Ren。不推出：从每个能动的配置出发的'
    '运行（选择）；在界内被吸入；分支路径上的度量。见[研究 §{S_BRANCHING}]({STUDY_BRANCHING})与 ' + R81A + '、' + R81B + '、' + R81C + '。')
P81_EN = (
    "**When the course branches (Part I, P81).** R6's and P67's laws are stated for determined laws; a process of the "
    'spine fixes only which steps are admissible, and its course can branch. They are stated here for every process, '
    'with no premise. A configuration returns exactly where its own course can have it at the next step, and every '
    'configuration returns exactly where every region the process never leaves keeps every possibility of its own. '
    "R6's three-way equivalence comes apart under branching: keeping every possibility does not give returning, a merge "
    'need not lose a possibility, and merging nothing gives returning along each run within finitely many '
    'configurations. Every process necessarily draws exactly what does not return; possibly drawn is losing oneself on '
    'some course, and a configuration possibly drawn can return on another. Determinacy is the named case of '
    'determinacy up to likeness; the main theorems of Experiment and Mechanism on how configurations relate hold up to '
    'likeness, while an intervention on one of two alike configurations, an unregistered past and an unregistered '
    "description need equality. Capture's rule region is absorbing, and reforming the state alone is drawn back into "
    "what the rule holds. The readings are the AI's, pending Ren. Not derived: a run from every configuration that can "
    'move (a choice); being drawn in within a bound; a measure on branching courses.')

WHOLE_I_76_ZH = ('- 一族历史恰在含有它的拼接时是某个律的历史族，恰在还一致时是确定的律的；两个律恰在活的步相同时容许同样的历史，恰在步相同时有同样的'
                 '有限历史；两个框架在相同之下确定时，配置恰在通过同样的检验时相同（`family_iff`、`determined_family_iff`、`same_histories_iff`、'
                 '`same_finite_histories_iff`、`alike_iff_sameTests`，P76）。')
WHOLE_I_76_EN = ("- A family of histories is a law's exactly where it holds its splices, a determined law's exactly where it is "
                 'also consistent; two laws admit the same histories exactly where they have the same live steps, and have '
                 'the same finite histories exactly where they have the same steps; where both frames are determined up to '
                 'likeness, configurations are alike exactly where they pass the same tests (`family_iff`, '
                 '`determined_family_iff`, `same_histories_iff`, `same_finite_histories_iff`, `alike_iff_sameTests`, P76).')
WHOLE_I_81_ZH = ('- 每个过程必然吸入的恰是不返回者，可能被吸入是在某一路径中失去自身；配置恰在它自己的路径下一步能再得到它时返回，处处返回恰是'
                 '过程不离开的每个区域都保留它自己的每个可能；保留每个可能不给返回，合并不必失去可能；确定是相同之下确定的命名情形'
                 '（`necessarilyDrawn_iff_not_returns`、`possiblyDrawn_iff`、`returns_iff_fed_ahead`、`returns_iff_keepsWithin`、'
                 '`Transit.keeps_not_returns`、`OneWay.merge_keeps`、`determined_iff_named`，P81）。')
WHOLE_I_81_EN = ('- Every process necessarily draws exactly what does not return, and possibly drawn is losing oneself on some '
                 'course; a configuration returns exactly where its own course can have it at the next step, and every one '
                 'returns exactly where every region the process never leaves keeps every possibility of its own; keeping '
                 'every possibility does not give returning, and a merge need not lose a possibility; determinacy is the '
                 'named case of determinacy up to likeness (`necessarilyDrawn_iff_not_returns`, `possiblyDrawn_iff`, '
                 '`returns_iff_fed_ahead`, `returns_iff_keepsWithin`, `Transit.keeps_not_returns`, `OneWay.merge_keeps`, '
                 '`determined_iff_named`, P81).')

STATUS = '\n'.join([
    ('| 历史固定什么（P76） | 已陈述并检查，不加前提：一族历史恰在含有拼接时是某个律的历史族，律与历史一一对应到死路为止，会停止的历史下没有死路'
     '（' + R76A + '）；两个框架在相同之下确定时检验固定相同，有分支时不然（' + R76B + '）；读法待 Ren；核心中分支检验固定相同开放 |'),
    ('| 路径分支时（P81） | 已陈述并检查，不加前提：分支过程中返回的精确条件，R6 的三方等价分开之处（' + R81A + '）；每个过程必然吸入的恰是'
     '不返回者，可能被吸入允许返回，Capture 的规则区域是吸收区域（' + R81B + '）；确定是相同之下确定的命名情形，需要相等之处有见证'
     '（' + R81C + '）；读法待 Ren；在界内被吸入与分支路径上的度量开放 |'),
])

CHOICE_ZH = ('- 历史与分支（P76、P81）：律是否读作含有拼接的历史族，展开的历史是否读作不终止；“拼接是记忆的缺席”；返回读作自己的路径能再得到，'
             '可能与必然被吸入的分开读作路径的开放；需要相等的定理读作取决于登记了什么。')
CHOICE_EN = ('- Histories and branching (P76, P81): whether a law reads as a family of histories holding its splices, and an '
             "unfolding's histories as unending; “the splice is memory's absence”; returning read as one's own course "
             'having one again, possibly and necessarily drawn coming apart as the course being open; the theorems needing '
             'equality read as depending on what is registered.')

FURTHER_ZH_OLD = ('- 一个关系的起点：第一部分以 `Determined`（相等）陈述的定理在相同之下重述（`DeterminedAt`），或说明何处需要相等'
                  '（例如合并）；核心中经同样检验推出相同的构造性条件；')
FURTHER_ZH_NEW = ('- 一个关系的起点：第一部分以 `Determined`（相等）陈述的定理中尚未在相同之下重述的（`Mechanism` 的 `Image`／`FactorsThrough` '
                  '刻画、`not_fixes_other_of_new`、`Joint` 的 `determined_dichotomy`、`carries_law_iff` 的双向形式；其余主要定理 P81 已重述或给出'
                  '需要相等的见证）；核心中分支检验固定相同的构造性证明（线性检验在相同之下确定时固定相同，P76）；')
FURTHER_EN_OLD = ('- One relational starting point: restating the Part I theorems stated with `Determined` (equality) up to '
                  'likeness (`DeterminedAt`), or saying where equality is needed (merging, for one); a constructive condition '
                  'in the core under which passing the same tests makes configurations alike;')
FURTHER_EN_NEW = ('- One relational starting point: restating up to likeness the Part I theorems stated with `Determined` '
                  "(equality) that P81 did not (Mechanism's characterization through `Image` and `FactorsThrough`, "
                  "`not_fixes_other_of_new`, Joint's `determined_dichotomy`, the two-way form of `carries_law_iff`); a "
                  'constructive proof in the core that branching tests fix likeness (linear tests fix it where both frames '
                  'are determined up to likeness, P76);')
FURTHER_ADD_ZH = '- 路径分支时：在界内被吸入；从每个能动的配置出发的运行是否需要选择之外的条件；分支路径上的度量（P82）。'
FURTHER_ADD_EN = ('- When the course branches: being drawn in within a bound; whether a run from every configuration that can '
                  'move needs more than a choice; a measure on branching courses (P82).')

SPINE = '\n'.join([
    ('| L3 | [Becoming.Histories]({LEAN}/Histories.lean) | 历史固定什么（不加前提，P76）：一族历史恰在含有它的拼接时是某个律的历史族，还一致时是确定的律的；'
     '两个律恰在活的步相同时容许同样的历史，不计死路的律与含有拼接的历史族一一对应；会停止的历史下没有死路；两个框架在相同之下确定时，'
     '配置恰在通过同样的检验时相同，有分支时不然 | {N_HISTORIES} |'),
    ('| L3 | [Becoming.Branching]({LEAN}/Branching.lean) | 路径分支时（不加前提，P81）：返回的精确条件，处处返回恰是过程不离开的每个区域都保留它自己的'
     '每个可能；保留每个可能不给返回，不合并沿运行给返回，合并不必失去可能；每个过程必然吸入的恰是不返回者，可能被吸入允许返回；确定是相同之下'
     '确定的命名情形，需要相等之处有见证；Capture 的规则区域是吸收区域 | {N_BRANCHING} |'),
])

GLOSS = '\n'.join([
    ('| 含有拼接／活的步 | holds its splices / live steps | 一族历史含有由它自己的步组成的每个序列；律的活的步是它的某段历史所走的步；'
     '一族历史恰在含有拼接时是某个律的历史族，两个律恰在活的步相同时容许同样的历史 | `SpliceClosed`、`family_iff`、`live`、`same_histories_iff` |'),
    ('| 可能／必然被吸入 | possibly / necessarily drawn | 从配置出发的某条路径／每个运行进入一个过程从不离开的区域；每个过程必然吸入的恰是'
     '不返回者，可能被吸入者可以在另一路径中返回 | `PossiblyDrawnInto`、`NecessarilyDrawnInto`、`necessarilyDrawn_iff_not_returns`、'
     '`possiblyDrawn_iff` |'),
])

CHAPTER_EDITS = [
    ('before', '**形成、维持、转化、退化与消解都是沿运行的关系变化，不是五个阶段。**', P76_ZH + '\n\n' + P76_EN),
    ('before', '**整体与 manifold。**', P81_ZH + '\n\n' + P81_EN),
    ('after_line', '- 每个确定的律恰吸入不返回者', WHOLE_I_81_ZH),
    ('after_line', '- Every determined law draws exactly what does not return', WHOLE_I_81_EN),
    ('after_line', '- 过程与框架是同一展开的读法', WHOLE_I_76_ZH),
    ('after_line', '- The process and the frame are readings of one unfolding', WHOLE_I_76_EN),
    ('after_line', '| 一个关系的起点（P69） |', STATUS),
    ('after_line', '- 一个关系的起点（P69）：', CHOICE_ZH),
    ('after_line', '- One relational starting point (P69):', CHOICE_EN),
    ('replace', FURTHER_ZH_OLD, FURTHER_ZH_NEW),
    ('replace', FURTHER_EN_OLD, FURTHER_EN_NEW),
    ('after_line', '- 一个关系的起点：第一部分以', FURTHER_ADD_ZH),
    ('after_line', '- One relational starting point: restating', FURTHER_ADD_EN),
    ('after_line', '| L3 | [Becoming.Unfolding]', SPINE),
    ('after_line', '| 相同之下确定 | determined up to likeness |', GLOSS),
]

READING = dict(
    after_en=("(P69; Ren agreed that law and history are one unfolding read two ways, “there are no two realities”; the "
              "other readings are the AI's, pending Ren). "),
    after_zh='（P69；Ren 同意律与历史是同一展开的两种读法，“there are no two realities”；其余读法是 AI 的，待 Ren）。',
    en=("Dead ends and splices are the whole law of law and history: a family of histories is a law's exactly where it "
        'holds its splices, two laws admit the same histories exactly where they have the same live steps, and where both '
        'frames are determined up to likeness tests fix likeness (P76). Where the course branches, every process '
        'necessarily draws exactly what does not return, possibly drawn allows return on another course, keeping every '
        "possibility does not give returning, and determinacy is the named case of determinacy up to likeness (P81; the "
        "readings are the AI's, pending Ren). "),
    zh=('死路与拼接就是律与历史之间的全部规律：一族历史恰在含有拼接时是某个律的历史族，两个律恰在活的步相同时容许同样的历史，'
        '两个框架在相同之下确定时检验固定相同（P76）。路径分支时，每个过程必然吸入的恰是不返回者，可能被吸入允许在另一路径中返回，'
        '保留每个可能不给返回，确定是相同之下确定的命名情形（P81；读法是 AI 的，待 Ren）。'),
    lean_after='Unfolding.lean',
)

HISTORY = {
    'HISTORIES': ('2026-10-12 P76：新增，按 Ren“move towards 100%”；见整合文档 §{S}。',
                  "2026-10-12 P76: added, following Ren's ‘move towards 100%’; see §{S} of the integration note."),
    'BRANCHING': ('2026-10-12 P81：新增，按 Ren“move towards 100%”；见整合文档 §{S}。',
                  "2026-10-12 P81: added, following Ren's ‘move towards 100%’; see §{S} of the integration note."),
}

RECORDS = {
    'histories-fix-law-up-to-dead-ends': dict(
        package='HISTORIES',
        sections=['A family of histories and its law', 'The live steps of a law', 'Histories that stop'],
        named=['shownBy_le_iff', 'family_iff', 'shownBy_determined_iff', 'determined_family_iff', 'admits_live_iff',
               'same_histories_iff', 'DeadEnd.not_live', 'same_finite_histories_iff', 'finite_family_iff'],
        builds_on=['Shown', 'Consistent', 'Run.keepHistory_shown', 'exists_law_iff', 'DeadEnd.no_history',
                   'Splice.spliced', 'Determined', 'Run', 'Generative.Trace', 'Generative.trace_nil_iff',
                   'Generative.trace_cons_iff'],
        provenance=[SOURCE],
    ),
    'tests-fix-likeness-where-determined': dict(
        package='HISTORIES',
        sections=['What tests fix', 'Where tests do not fix likeness'],
        named=['Alike.sameTests', 'SameTests.after', 'sameTests_bisimulation', 'alike_iff_sameTests',
               'Determined.alike_iff_sameTests', 'Choosing.sameTests', 'Choosing.not_alike',
               'Choosing.early_not_determined'],
        builds_on=['Bisimulation', 'Alike', 'Alike.trace', 'Alike.tests', 'DeterminedAt', 'Determined.at', 'Frame',
                   'Generative.Trace'],
        provenance=[SOURCE],
    ),
    'returning-where-the-course-branches': dict(
        package='BRANCHING',
        sections=['Courses of a given length', 'Within finitely many configurations',
                  'A configuration that returns has a run that never loses it', 'Under a determined process, the moves decide',
                  'A passage', 'The fork merges nothing and does not return', 'Runs that meet and part'],
        named=['Branching.lost_stays', 'Branching.Returns.reachable', 'Branching.keeps_iff_fed',
               'Branching.returns_iff_fed_ahead', 'Branching.returns_iff_keepsWithin', 'Branching.Lossless.returns', 'Branching.rise_not_lossless',
               'Branching.Returns.run', 'Branching.Transit.keeps_not_returns', 'Branching.fork_lossless_not_returns',
               'Branching.Determined.stays_merged', 'Coarse.meet_and_part'],
        builds_on=['Law.Returns', 'Law.Lossless', 'Law.KeepsPossibilities', 'Law.process', 'Law.orbit', 'Run', 'Reach',
                   'Fork.law', 'Determined', 'Invariant', 'Generative.Trace'],
        provenance=[SOURCE],
    ),
    'necessarily-drawn-is-not-returning': dict(
        package='BRANCHING',
        sections=['Possibly and necessarily drawn', 'The future narrows', 'Determined laws are the instance',
                  'A one-way passage', "Capture's rule region"],
        named=['Branching.necessarilyDrawn_iff_not_returns', 'Branching.NecessarilyDrawnInto.not_returns',
               'Branching.necessarilyDrawnInto_ahead', 'Branching.possiblyDrawn_iff',
               'Branching.PossiblyDrawnInto.never_back', 'Branching.OneWay.possibly_not_necessarily',
               'Branching.reachable_invariant', 'Branching.lost_necessarily_drawn', 'Run.enters_returning',
               'Law.rule_absorbing', 'Law.reform_drawnInto', 'Captured.state_reform_drawn'],
        builds_on=['Law.Absorbing', 'Law.DrawnInto', 'Law.drawn_iff_not_returns', 'Law.Returns', 'Invariant',
                   'Law.reform_reabsorbed', 'Run'],
        provenance=[SOURCE],
    ),
    'determinacy-up-to-likeness': dict(
        package='BRANCHING',
        sections=['Determinacy up to likeness', 'What the record fixes, up to likeness', 'A kept history, up to likeness',
                  'What nothing registers is not refuted', 'The twins: retargeting one of two alike configurations',
                  'A confound not registered is not refuted'],
        named=['determined_iff_named', 'goesAlike_iff', 'DeterminedAt.stays_alike', 'DependsOnlyOnAlike.reabsorbed',
               'forget_inputs_determinedAt_iff', 'Run.fixesAlike_of_takes', 'Run.generalizesAlike',
               'Run.not_fixesAlike_of_untaken', 'keepHistory_new_named', 'carries_unregistered',
               'Twins.retarget_breaks', 'Confound.refutes_registered'],
        builds_on=['DeterminedAt', 'Alike', 'Bisimulation', 'Determined', 'goAlike_id_iff', 'GoAlike.runs_agree',
                   'DependsOnlyOn.reabsorbed', 'forget_inputs_determined_iff', 'Run.fixes_of_takes',
                   'Run.not_fixes_of_untaken', 'Run.generalizes', 'retarget', 'retarget_determined', 'keepHistory',
                   'keepHistory_new', 'carries_law_iff', 'Confound.varied_refutes'],
        provenance=[SOURCE],
    ),
}

DELTAS = ['record_delta.py']
