"""Chapter edits for P83, as (kind, anchor, text) edits applied by apply_docs.py.

kind: 'before' inserts text before the line starting with anchor (a blank line after a paragraph,
none after a list item or table row); 'after_line' inserts text as new lines after the line starting
with anchor; 'replace' replaces the exact substring anchor with text. Every anchor must occur once.
The anchors are lines the P70–P72 package adds, so these edits apply after it. Placeholders {LEAN},
{STUDY}, {S}, {N_MODULE}, {LAYER} and {SPINE_AFTER} are filled by apply_docs.py.
"""

SOURCE = '../../../sources/15-codex-theory-conversations/2026-10-12-framing-and-pairs.md'
REC = '../results/records/identification-where-bounded.md'

# Section 3: after contextual registration, before knowledge.
IDENT_ZH = (
    '**辨识：有界的记录确定什么（第一部分，P83）。** Ren 推测“the full \"truth\" can be derived, situationally, including the '
    'cognition/controller part”（[来源](' + SOURCE + ')）。情境给出的是它的状态数的界。至多 N 与 N′ 个状态的两段所识的历史，'
    '在 N + N′ − 1 之前相同就处处相同，所以这一长度的记录确定历程（`Identification.bounded_agree`，经 Fine 与 Wilf 的两个周期定理 '
    '`Identification.period_extends`，[Becoming.Identification]({LEAN}/Identification.lean)）；在 N = 1 与 N = N′ 时更短的记录不够'
    '（`Identification.record_short`、`Identification.record_short_twice`）。界给定时归纳就是演绎：N 之内、在长 2N − 1 的记录上不被否证的'
    '套索假设，就是整个历程的律（`Identification.bounded_induction`）；知道界的学习者处处不被否证，从 2N − 1 起每步都对，没有学习者能更早地总作主张'
    '（`Identification.knowing_right`、`Identification.knowing_earliest`）。不知道界的学习者（P73 的按否证学习）也会静止，静止之步由界给出：从第 N + (2N − 1)·tri N 步起每步都对'
    '（`Identification.held_learner_rests`），但它的记录从不表明这一点；没有界时，没有记录确定下一个值。'
    '世界中的控制者在所识之内；回答知道界的学习者的世界有多于那个界的状态（`Identification.answer_exceeds_bound`），说谎者的节律则从第 3 步起被推出'
    '（`Identification.denial_derived`）。列表持有的世界中，以长 2N − 1 的所识的未来命名每个配置，这一命名有意义并承载规律，不用商公理'
    '（`Law.name_makesSense`、`Law.name_carries`）；以整个未来命名需要函数外延性。读法（AI 的，待 Ren）：“按情境”就是界；有限的记录是一个投影，'
    '界使它对历程不失去什么。见[研究 §{S}]({STUDY})与 [identification-where-bounded](' + REC + ')。')

IDENT_EN = (
    '**Identification: what a bounded record fixes (Part I, P83).** Ren speculated that “the full \"truth\" can be derived, '
    'situationally, including the cognition/controller part”. What the situation supplies is a bound on its states. Two '
    'registered histories with at most N and N′ states that agree before N + N′ − 1 agree everywhere, so the record of '
    'that length fixes the course (by Fine and Wilf\'s two periods); for N = 1 and N = N′ no shorter record does. Where the '
    'bound is given induction is deduction: a lasso hypothesis within N unrefuted on the record before 2N − 1 is the law '
    'of the whole course; the learner that knows the bound is refuted nowhere and right from 2N − 1 on, and no learner can '
    'always speak sooner. The learner that does not know the bound (P73\'s learning by refutation) still rests by a step the '
    'bound gives, right at every step from N + (2N − 1)·tri N on, though its record never shows it; where there is no bound, '
    'no record fixes the next value. A controller in the world is within what is registered; a world answering the learner that knows '
    'the bound has more states than the bound, while the liar\'s rhythm is derived from step 3. In a world a list holds, '
    'naming each configuration by its registered future for 2N − 1 steps makes sense and carries the law, with no '
    'quotient axiom; naming by the whole future would need function extensionality. Readings (the AI\'s, pending Ren): '
    '“situationally” is the bound; a finite record is a projection, which the bound makes lose nothing of the course.')

# Item 9 of the theory stated in full (as P70–P72 left it).
KNOW_ZH_OLD = '知识的完整说明见第 3 节。〔定理〕'
KNOW_ZH_NEW = ('状态数的界给定时，长 2N − 1 的记录确定所识的历程，归纳成为演绎，有意义的切分以有限的名命名（`Becoming.Identification`）。'
               '知识的完整说明见第 3 节。〔定理〕')
KNOW_EN_OLD = '; section 3 gives the account of knowledge. [theorem]'
KNOW_EN_NEW = ('; where a bound on the states is given, the record of 2N − 1 steps fixes the registered course, induction '
               'is deduction, and the split that makes sense is named with finite names (`Becoming.Identification`); '
               'section 3 gives the account of knowledge. [theorem]')

# Part I stated whole, I: after P72's bullet.
WHOLE_I_ZH = ('- 至多 N 与 N′ 个状态的两段所识的历史在 N + N′ − 1 之前相同就处处相同，在 N = 1 与 N = N′ 时更短的不够；N 之内、在长 2N − 1 的记录上'
              '不被否证的套索假设是整个历程的律，知道界的学习者从 2N − 1 起每步都对，不能更早，不知道界的学习者从 N + (2N − 1)·tri N 起每步都对；列表持有的世界中，以有限的所识的未来命名配置有意义'
              '（`Identification.bounded_agree`、`Identification.record_short_twice`、`Identification.bounded_induction`、'
              '`Identification.knowing_earliest`、`Identification.held_learner_rests`、`Law.name_makesSense`，P83）。')
WHOLE_I_EN = ('- Two registered histories with at most N and N′ states that agree before N + N′ − 1 agree everywhere, and for '
              'N = 1 and N = N′ no shorter agreement suffices; a lasso hypothesis within N unrefuted on the record before '
              '2N − 1 is the law of the whole course, the learner that knows the bound is right from 2N − 1 on and '
              'cannot be sooner, and the learner that does not know it is right from N + (2N − 1)·tri N on; in a world a list holds, naming configurations by their finite registered futures makes '
              'sense (`Identification.bounded_agree`, `Identification.record_short_twice`, '
              '`Identification.bounded_induction`, `Identification.knowing_earliest`, `Identification.held_learner_rests`, '
              '`Law.name_makesSense`, P83).')

# Part I stated whole, III: after P70–P72's bullet on registration and context.
WHOLE_III_ZH = ('- **界。** 一个情境有多少状态，不由动力学决定，是情境给出的；给出它，所识的一切从有限的记录推出，不知道它的学习者也从它给出的一步起每步都对，却不知道何时；'
                '不给出，没有有限的记录足够'
                '（P73、P83）。')
WHOLE_III_EN = ('- **The bound.** How many states a situation has is not decided by the dynamics; the situation supplies it. '
                'Given it, everything registered is derived from a finite record, and a learner that does not know it is right from a '
                'step it gives on, without knowing when; not given, no finite record suffices '
                '(P73, P83).')

STATUS_ROW = ('| 辨识（P83） | 已陈述并检查，除了界不加前提：有界的记录确定历程，长度 N + N′ − 1，在 N = 1 与 N = N′ 时恰好；界给定时归纳即演绎，'
              '知道界的学习者从 2N − 1 起每步都对，不能更早；不知道界的学习者从 N + (2N − 1)·tri N 起每步都对；回答知道界的学习者的世界超出界；有意义的切分以有限的名命名，不用商'
              '（[identification-where-bounded](' + REC + ')）。开放：一般 N、N′ 的恰好性；同一世界的 Moore 界；最优的静止之步；有分支的框架下的辨识；读法待 Ren |')

CHOICE_ZH = ('- 辨识（P83）：“完整的真按情境可推出”是否读作“给出状态数的界，所识的一切从长 2N − 1 的记录推出”；有界时类的名是否读作它的有限的未来'
             '（“名可名”的一个精确化）。')
CHOICE_EN = ('- Identification (P83): whether “the full truth can be derived situationally” reads as “given the bound on '
             'states, everything registered is derived from the record of 2N − 1 steps”; whether, with a bound, a class\'s '
             'name reads as its finite future (a precise form of 名可名).')

FURTHER_ZH = ('- 辨识：一般 N、N′ 的恰好性（Fine 与 Wilf 的极值构造）；同一世界的 Moore 界；不知道界的学习者的最优静止之步；有分支的框架下的辨识（以 P69 的 `Alike` 与 P76 的检验）；'
              '与 P76 的 `alike_iff_sameTests` 的实例定理（由后落地者写出）。')
FURTHER_EN = ('- Identification: exactness for general N, N′ (Fine and Wilf\'s extremal words); Moore\'s bound for one world; '
              'the optimal rest step of the learner that does not know the bound; '
              'identification for branching frames (with P69\'s `Alike` and P76\'s tests); the instance theorem to P76\'s '
              '`alike_iff_sameTests` (by whichever lands second).')

SPINE = ('| {LAYER} | [Becoming.Identification]({LEAN}/Identification.lean) | 辨识（除了界不加前提，P83）：两个周期（Fine–Wilf）；至多 N 与 N′ 个状态的'
         '历史由长 N + N′ − 1 的记录确定，在 N = 1 与 N = N′ 时恰好；界给定时归纳即演绎，知道界的学习者从 2N − 1 起每步都对，不能更早；'
         '说谎者的节律被推出；回答知道界的学习者的世界超出界；不知道界的学习者从 N + (2N − 1)·tri N 起每步都对；列表持有的世界中以有限的所识的未来命名配置有意义并承载规律，不用商 | {N_MODULE} |')

GLOSS_NEW = '\n'.join([
    '| 状态数的界 | bound on states | 一段所识的历史至多有 N 个状态，即每个时刻与前 N 个时刻之一同一状态；恰当它是 N 之内的套索 | '
    '`StatesBelow`、`Identification.statesBelow_iff_lasso` |',
    '| 辨识／知道界的学习者 | identification / learner that knows the bound | 由有限的记录确定整个历程；知道界 N 的学习者在 2N − 1 之前不说，之后以'
    '为记录所证实的 N 之内的套索假设主张，处处不被否证 | `Identification.record_fixes`、`Identification.knowing` |',
])

EDITS = [
    ('before', '**知识。** [知识一章]', IDENT_ZH + '\n\n' + IDENT_EN),
    ('replace', KNOW_ZH_OLD, KNOW_ZH_NEW),
    ('replace', KNOW_EN_OLD, KNOW_EN_NEW),
    ('after_line', '- 不依语境的主张的框架合于语境中的诸识', WHOLE_I_ZH),
    ('after_line', '- A frame of context-free claims fits registrations in context', WHOLE_I_EN),
    ('before', '- **意义。** 规律与定理不给任何部分以意义', WHOLE_III_ZH),
    ('before', '- **Significance.** The laws and theorems give no part significance', WHOLE_III_EN),
    ('after_line', '| 描述保留什么、失去什么（P70–P72） |', STATUS_ROW),
    ('before', '- 名称：本理论中由 AI 拟定的用语', CHOICE_ZH),
    ('before', '- Names: the terms the AI has proposed', CHOICE_EN),
    ('after_line', '- 描述保留什么、失去什么：有分支的框架下有意义的切分', FURTHER_ZH),
    ('after_line', '- What a description keeps and loses: the split that makes sense for branching frames', FURTHER_EN),
    ('after_line', '{SPINE_AFTER}', SPINE),
    ('after_line', '| 语境中的识／粘合 |', GLOSS_NEW),
]
