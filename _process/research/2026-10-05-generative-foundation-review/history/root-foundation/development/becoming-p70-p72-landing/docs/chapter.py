"""Chapter edits for P70–P72 (with P72q), as (kind, anchor, text) edits applied by apply_docs.py.

kind: 'before' inserts text before the line starting with anchor (a blank line after a paragraph,
none after a list item or table row); 'after_line' inserts text as new lines after the line starting
with anchor; 'replace' replaces the exact substring anchor with text. Every anchor must occur once.
Several anchors are lines the P69 package adds, so these edits apply after it.
Placeholders {LEAN}, {STUDY_KEY}, {S_KEY} and {N_KEY} (KEY = DESCRIPTION, DIAGONAL, CONTEXT, and
{N_QUANTUM}) are filled by apply_docs.py.
"""

SOURCE = '../../../sources/15-codex-theory-conversations/2026-10-12-framing-and-pairs.md'
REC_SEP = '../results/records/separation-loses-the-relation.md'
REC_SPLIT = '../results/records/the-split-that-makes-sense.md'
REC_DIAG = '../results/records/registration-within-what-it-registers.md'
REC_CTX = '../results/records/contextual-registration.md'

# Section 1: what makes a pair a pair, after P69's paragraph on the one unfolding.
PAIR_ZH = (
    '**一对怎样成为一对（第一部分，P70）。** Ren 问“what makes a pair, a pair?”（[来源](' + SOURCE + ')）。'
    '两个部分的整体（哪些组合出现）是矩形的，指与一个部分同在的，与另一部分的每一项同在；这时分别描述两部分恰给回整体（`separation_faithful_iff`，'
    '[Becoming.Description]({LEAN}/Description.lean)）。整体不是矩形，就是两部分之间有关系：分别描述失去的恰是它，失去的关系作为多余重现'
    '（`separation_surplus`）；三个部分可以作为整体相关而任意两个都自由，描述每一对仍失去它（`whole_not_in_pairs`）。'
    '关系在展开中形成、持续与结束，都在共同的律中：各自移动每个部分的律，不论有损与否，从不使无关的部分相关（`Rectangular.image_of_separate`），'
    '把一个部分复制进另一部分的律使它们相关（`copy_relates`）；关系形成之后，在各自移动每个部分、在出现者上不合并的每条律下持续（`relation_persists`），'
    '所以它只由出现者之内的失去（如忘掉一个部分，`forgetting_unrelates`）或对两部分的共同作用结束：例如一次耦合使两个部分相关，再作用一次使它们不再相关，'
    '两次都不失去什么（`coupling_relates_and_unrelates`），耦合本身是双射，结束关系的是它共同作用于两部分。'
    '在律之下，一对是有意义的切分：位置按速度变化而只识位置时，有意义的切分是位置与速度这一对，两者单独都没有意义（`Motion.neither_alone`）；'
    '没有什么经过时，位置单独有意义，一对是一（`Motion.still_makes_sense`）。'
    '读法（AI 的，待 Ren；Ren 要求就“What makes two a pair, then, is relation”往深处挖，并同意了其后的回答）：两个之所以是一对，在于关系，'
    '在于能一起是什么或怎样一起继续；成员从一对中读出，不是一对由成员拼成；一对是最小的切分，不是最小的关系。'
    '见[研究 §{S_DESCRIPTION}]({STUDY_DESCRIPTION})与 [separation-loses-the-relation](' + REC_SEP + ')。')

PAIR_EN = (
    '**What makes a pair a pair (Part I, P70).** Ren asked “what makes a pair, a pair?”. A whole of two parts, the '
    'combinations that occur, is rectangular when what occurs with one part occurs with every item of the other; then '
    'describing the parts separately gives the whole back exactly. A whole that is not rectangular is a relation between '
    'the parts: it is exactly what describing them separately loses, and the lost relation reappears as surplus; three '
    'parts can be related as a whole while every two are free, and describing every pair still loses it. A relation forms, '
    'lasts and ends in the joint law: a law moving each part by itself, lossy or not, never relates unrelated parts, and a '
    'law copying one part into the other relates them; once formed, a relation lasts under every law that moves each part '
    'by itself and merges nothing that occurs, so it ends only by loss within what occurs, as by forgetting a part, or by '
    'acting on both parts together: for example, a coupling relates two parts and, acting again, unrelates them, losing '
    'nothing either way; the coupling is a bijection, and what ends the relation is its acting on both. Under a law a pair '
    'is a split that makes sense: where position changes by velocity and only position is registered, the split that makes '
    'sense is the pair, and neither alone makes sense; where nothing passes, position alone makes sense, and the pair is '
    'one. Readings (the AI\'s, pending Ren; Ren asked for “What makes two a pair, then, is relation” to be dug deeper and '
    'agreed with the reply that followed): two are a pair by relation, in what they can be together or how they go on '
    'together; the members are read off the pair, not the pair assembled from them; a pair is the least split, not the '
    'least relation.')

# Section 3: the split that makes sense, a registration within what it registers, contextual registration.
SPLIT_ZH = (
    '**有意义的切分与从历史读出的状态（第一部分，P70）。** Ren 问切分的“make sense”本身是什么。以 P69 的定义，描述有意义，指它恰把相同的配置等同；'
    '确定的律经识读时，相同就是所识的未来相同（`Law.alike_iff_sameFuture`）。保留所识并承载规律的最粗切分有意义，不失去所识的任何东西'
    '（`Law.makesSense_of_law`、`Law.sameFuture_of_law`，[Becoming.Description]({LEAN}/Description.lean)）；承载规律不够：什么都不分的切分总承载规律，'
    '只在所识从不不同时有意义（`Law.const_makesSense_iff`）。现在所识者自身有意义，恰当它承载规律，这是一步上的条件（`Law.now_makesSense_iff_goAlike`）；'
    '所识的部分单独有意义，恰当其余对它的下一值不造成差别（`Law.part_makesSense_iff_step`）；控制者的规则随之改变时，恰当规则对它不造成差别'
    '（`Law.adaptive_makesSense_iff`，P66 的 `adaptive_state_law_iff` 的条件）：认知或控制者在有意义的切分之内，恰在它造成所识的差别之处。'
    '状态不给配置，从一段所识的历史读出：两个时刻是同一状态，指其后所识的一切相同（`SameAhead`）；每段所识的历史都是一条确定的律（时刻之律，只用步的相继，即表示的共同步序）经所识而读，'
    '它的相同的时刻恰是同一状态的时刻（`alike_moments_iff`）。所以除了步的相继，展开有律不是前提，律的内容是它的压缩：状态有限恰当所识从某一刻起重复'
    '（`finitely_many_states_iff`，经不加判定的按关系的鸽笼 `shared_below`），返回的构型在每个识读之下状态有限（`Law.Returns.states`）；'
    '二值否定的所识恰有两个状态，每个经另一个定义（`Denial.two_states`、`Denial.each_through_other`）。'
    '见[研究 §{S_DESCRIPTION}]({STUDY_DESCRIPTION})与 [the-split-that-makes-sense](' + REC_SPLIT + ')。')

SPLIT_EN = (
    '**The split that makes sense, and states read off a history (Part I, P70).** Ren asked what the “make sense” of a '
    'split itself is. With P69\'s definition a description makes sense when it identifies exactly the alike configurations; '
    'for a determined law read through a registration, alike is the same registered future. The coarsest split keeping '
    'what is registered and carrying a law makes sense and loses nothing registered; carrying a law is not enough, since '
    'the split lumping everything always carries one and makes sense only where nothing registered ever differs. What is '
    'registered now makes sense by itself exactly where it carries a law, a condition on one step; a registered part alone '
    'makes sense exactly where the rest makes no difference to its next value; where a controller\'s rule changes with it, '
    'exactly where the rule makes no difference to it, the condition of P66\'s `adaptive_state_law_iff`: cognition or a '
    'controller is inside the split that makes sense exactly where it makes a registered difference. States are not given '
    'with configurations but read off a registered history: two moments are one state when everything registered after '
    'them is alike; every registered history is a determined law, the law of moments, which uses only the succession of '
    'steps, the representation\'s shared index, read through what is registered, and its alike moments are exactly its '
    'states. So beyond the succession of steps, that an unfolding has a law is not a premise, and a law\'s content is its '
    'compression: there are finitely many states exactly where the registration repeats from some moment on (by a pigeonhole up to a '
    'relation with no decision), a returning configuration has finitely many states under every registration, and the '
    'two-valued denial has exactly two states, each defined through the other.')

DIAG_ZH = (
    '**在所识之中的识（第一部分，P71）。** 世界对自身的识由它的部分作出，部分在所识者之中（[来源](' + SOURCE + ')）。'
    '以所读者为索引的识，对移动每个值的映射漏掉一个确定的读法（`Diagonal.gap_unsaid`，Lawvere 的对角线，[Becoming.Diagonal]({LEAN}/Diagonal.lean)；'
    '外围的 `RootCoverageBoundary` 有同一对角线）；主张从不与它的否定相同，所以没有主张族说出每个读法，框架不能以自己的配置实现关于配置的每种主张'
    '（`Diagonal.claims_incomplete`、`Frame.self_incomplete`）。限制恰在有差别处：以相等比较的值，在所识之中的识说出每个读法，恰当值之间没有什么可分'
    '（`Diagonal.complete_iff_alike`）；说出每个读法的识给每个映射一个不动点（`Diagonal.fixed_of_complete`），所以包含自身是可以的，'
    '不可以的是把每个读法同时持有在一个内部的描述中。补全是展开：保留所识、下一步识得所漏者的识在每一步都不完备，每个缺口都是新的，从不返回，'
    '没有有限储存持有所漏的，这样的展开存在（`Diagonal.Unfolds.incomplete`、`Diagonal.Unfolds.never_returns`、`Diagonal.Unfolds.unheld`、'
    '`Diagonal.unfolding_open`）。说谎者读作修正：从不静止，二值时每两步返回，是没有静值的节律，不是矛盾（`Diagonal.revision_never_rests`、'
    '`Diagonal.denial_returns`）。读法（AI 的，待 Ren；Ren 同意了包含它们的回答）：对 Ren 的推测“完整的真可按情境推出”，从内部，任何给定的真'
    '可在下一步说出，不能从一个情境全部说出；限制在投影，即试图把整体持有在它之中的一个描述里，不在真之外还有什么。'
    '见[研究 §{S_DIAGONAL}]({STUDY_DIAGONAL})与 [registration-within-what-it-registers](' + REC_DIAG + ')。')

DIAG_EN = (
    '**A registration within what it registers (Part I, P71).** A world\'s registration of itself is made by its parts, '
    'which are within what is registered. A registration indexed by what it reads misses a definite reading for any map '
    'moving every value (Lawvere\'s diagonal; the periphery\'s `RootCoverageBoundary` has the same diagonal); a claim is '
    'never alike with its negation, so no family of claims says every reading, and no frame realizes with its own '
    'configurations every claim about them. The limit lies exactly where there is something to tell apart: for values '
    'compared by equality, a registration within what it registers says every reading exactly where nothing differs, and '
    'one that does gives every map a fixed point, so containing itself is possible; what is not is holding every reading '
    'at once in one description inside. Completing is an unfolding: a registration keeping what it registered and next '
    'registering what it missed is incomplete at every step, each gap new, never returning, its gaps held by no finite '
    'stock, and such an unfolding exists. The liar read as revision never rests and, two-valued, returns every two steps: a '
    'rhythm with no still value, not a contradiction. Readings (the AI\'s, pending Ren; Ren agreed with the reply '
    'containing them): of Ren\'s speculation that the full truth can be derived situationally, from within any given truth '
    'can be said at the next step and not all from one situation; the limit is the projection\'s, holding the whole in one '
    'description inside it, not something beyond the truth.')

CTX_ZH = (
    '**语境中的识（第一部分，P72）。** Ren 问框架所失去的是否像“wave/particle”（[来源](' + SOURCE + ')）。框架在类型上把主张读作不依语境：'
    '一个主张被识得什么，不取决于与它一起被识的是什么。这里把它定为表示的承诺，并给出它何时合（[Becoming.Context]({LEAN}/Context.lean)）。'
    '主张在语境中被识；诸识粘合，恰当识同一主张的任意两个语境识得相同（`Contextual.glues_iff_agree`）；不依语境的主张的框架合，恰当诸识在每个配置粘合'
    '（`Contextual.fitsFree_iff`）；以语境为索引的框架总合（`Contextual.indexed_fits`）。有的世界在任何配置都不粘合：Specker 的三个盒子与 '
    'Mermin–Peres 方阵，每个语境内一致，没有语境强制任何主张，没有不依语境的读法（`Specker.noGlobal`、`Square.noGlobal`）；两个量子比特上的九个'
    '可观测量实现这个方阵，没有赋值在每条线上被量子态共同显示（[Becoming.Quantum]({LEAN}/Quantum.lean)，`no_context_free_values`；P72q，'
    '由 P64–P68 的所有者写成并检查），所以量子的识属于这一类。部分失去整体有两种方式，在同样的三对上：不给回整体（P70 的奇偶，'
    '`evenBoxes_not_determined`），与允许没有整体有的（`Specker.no_whole`）。读法（AI 的，待 Ren；Ren 同意了包含它们的回答）：'
    '波与粒子都是向不依语境的值的投影；值是在语境中的识，即关系；Ren 推测的真是关系的。'
    '见[研究 §{S_CONTEXT}]({STUDY_CONTEXT})与 [contextual-registration](' + REC_CTX + ')。')

CTX_EN = (
    '**Contextual registration (Part I, P72).** Ren asked whether what the framing loses is like “wave/particle”. The frame '
    'reads claims as context-free by type: what a claim registers does not depend on what is registered with it. This is '
    'named here a commitment of the representation, with the condition under which it fits. Claims are registered in '
    'contexts; the registrations glue exactly where any two contexts registering a claim register it alike; a frame of '
    'context-free claims fits exactly where they glue at every configuration, and the frame indexed by context always fits. '
    'Some worlds glue at no configuration: Specker\'s three boxes and the Mermin–Peres square, consistent within each '
    'context, no context forcing a claim, with no context-free reading; the nine two-qubit observables realize the square, '
    'and no assignment is shown jointly on every line by quantum states (`Becoming.Quantum`, P72q, written and checked by '
    'the owner of P64–P68), so quantum registration is of this kind. Parts fail a whole in two ways, on the same three '
    'pairs: by not giving it back (P70\'s parity) and by allowing what no whole has (`Specker.no_whole`). Readings (the '
    'AI\'s, pending Ren; Ren agreed with the reply containing them): wave and particle are both projections onto '
    'context-free values; a value is a registration in context, a relation; the truth of Ren\'s speculation is relational.')

# Item 9 of the theory stated in full.
KNOW_ZH_OLD = '知识的完整说明见第 3 节。〔定理〕'
KNOW_ZH_NEW = ('确定的律下，描述有意义，恰当它恰把所识的未来相同者等同；部分单独有意义，恰当其余对它不造成差别；状态从所识的历史读出（`Becoming.Description`）。'
               '在所识之中的识不能同时持有每个读法，补全它是从不返回的展开（`Becoming.Diagonal`）。不依语境的主张是表示的承诺，量子的识不满足它'
               '（`Becoming.Context`、`Becoming.Quantum`）。知识的完整说明见第 3 节。〔定理〕')
KNOW_EN_OLD = '; section 3 gives the account of knowledge. [theorem]'
KNOW_EN_NEW = ('; under a determined law, a description makes sense exactly where it identifies what has the same registered future, a part alone '
               'exactly where the rest makes no difference to it, and states are read off a registered history '
               '(`Becoming.Description`); a registration within what it registers cannot hold every reading at once, and '
               'completing it is an unfolding that never returns (`Becoming.Diagonal`); context-free claims are a commitment '
               'of the representation, which quantum registration does not meet (`Becoming.Context`, `Becoming.Quantum`); '
               'section 3 gives the account of knowledge. [theorem]')

# Part I stated whole, I: after P69's bullet.
WHOLE_I_ZH = '\n'.join([
    '- 分别描述各部分恰在整体为矩形处给回整体，失去的恰是关系；关系只由共同作用形成，在各自移动每个部分、在出现者上不合并的律下持续，'
    '只由出现者之内的失去或共同作用结束；三个部分可以作为整体相关而任意两个都自由（`separation_faithful_iff`、`copy_relates`、`relation_persists`、'
    '`forgetting_unrelates`、`whole_not_in_pairs`，P70）。确定的律下，保留所识并承载规律的最粗切分有意义，所识的部分单独有意义恰当其余对它的下一值'
    '不造成差别；每段所识的历史是一条确定的律（只用步的相继），状态有限恰当所识从某一刻起重复（`Law.makesSense_of_law`、`Law.part_makesSense_iff_step`、`alike_moments_iff`、'
    '`finitely_many_states_iff`，P70）。',
    '- 以所读者为索引的识，对移动每个值的映射漏掉其缺口，主张的识从不完备；以相等比较的值，它恰在值之间没有什么可分处完备；补全它的展开每一步都不完备，'
    '从不返回，没有有限储存持有所漏的；以否定修正主张从不静止（`Diagonal.gap_unsaid`、`Diagonal.claims_incomplete`、`Diagonal.complete_iff_alike`、'
    '`Diagonal.Unfolds.never_returns`、`Diagonal.Unfolds.unheld`、`Diagonal.revision_never_rests`，P71）。',
    '- 不依语境的主张的框架合于语境中的诸识，恰当它们在每个配置粘合，以语境为索引的框架总合；可能性局部而没有不依语境的读法时，没有尊重它们的配置粘合；'
    '没有不依语境的读法而某个语境允许某物时，它们不是任何整体的部分；Specker 的盒子与 Mermin–Peres 方阵是这样的世界，量子比特实现方阵（`Contextual.fitsFree_iff`、`Contextual.indexed_fits`、'
    '`Contextual.no_free_frame`、`no_whole`、`Square.noGlobal`、`no_context_free_values`，P72）。',
])
WHOLE_I_EN = '\n'.join([
    '- Describing the parts separately gives back the whole exactly where it is rectangular, and what is lost is exactly '
    'the relation; a relation forms only by joint action, lasts under laws that move each part by itself and merge nothing '
    'that occurs, and ends only by loss within what occurs or by joint action; three parts can be related as a whole while '
    'every two are free (`separation_faithful_iff`, `copy_relates`, `relation_persists`, `forgetting_unrelates`, '
    '`whole_not_in_pairs`, P70). Under a determined law the coarsest split keeping what is registered and carrying a law '
    'makes sense, and a registered part alone makes sense exactly where the rest makes no difference to its next value; '
    'every registered history is a determined law, using only the succession of steps, with finitely many states exactly '
    'where its registration repeats from some moment on '
    '(`Law.makesSense_of_law`, `Law.part_makesSense_iff_step`, `alike_moments_iff`, `finitely_many_states_iff`, P70).',
    '- A registration indexed by what it reads misses the gap of any map moving every value, and a registration of claims '
    'is never complete; for values compared by equality it is complete exactly where nothing differs; the unfolding that '
    'completes it is incomplete at every step, never returns, and no finite stock holds what it misses; revising a claim '
    'by negation never rests (`Diagonal.gap_unsaid`, `Diagonal.claims_incomplete`, `Diagonal.complete_iff_alike`, '
    '`Diagonal.Unfolds.never_returns`, `Diagonal.Unfolds.unheld`, `Diagonal.revision_never_rests`, P71).',
    '- A frame of context-free claims fits registrations in context exactly where they glue at every configuration, and '
    'the frame indexed by context always fits; with local possibilities and no context-free reading no configuration '
    'respecting them glues, and with no context-free reading, where some context allows something, they are the parts of '
    'no whole; Specker\'s boxes and the Mermin–Peres square are such '
    'worlds, and qubits realize the square (`Contextual.fitsFree_iff`, `Contextual.indexed_fits`, '
    '`Contextual.no_free_frame`, `no_whole`, `Square.noGlobal`, `no_context_free_values`, P72).',
])

# Part I stated whole, III: before Significance, after P69's bullet on moves and laws.
WHOLE_III_ZH = ('- **所识与语境。** 一个形成识什么，从而哪个切分对它有意义，不由动力学决定；给定所识，有意义的切分在它等同什么上唯一（P69、P70）。'
                '主张是否不依语境，是表示的承诺，不由动力学决定：以语境为索引的框架总合，不依语境的只在诸识粘合处合，量子的识不粘合'
                '（`Contextual.indexed_fits`、`Contextual.fitsFree_iff`、`no_context_free_values`）。从内部，没有一个识同时持有关于自身的每个读法'
                '（`Frame.self_incomplete`）；任何给定的读法可以在下一步识得（`Diagonal.Unfolds`）。')
WHOLE_III_EN = ('- **Registration and context.** What a formation registers, and so which split makes sense for it, is not '
                'decided by the dynamics; given what is registered, the split that makes sense is unique in what it '
                'identifies (P69, P70). Whether claims are context-free is a commitment of the representation, not decided '
                'by the dynamics: the frame indexed by context always fits, a context-free one only where the registrations '
                'glue, and quantum registrations do not glue (`Contextual.indexed_fits`, `Contextual.fitsFree_iff`, '
                '`no_context_free_values`). From within, no registration holds every reading about itself at once '
                '(`Frame.self_incomplete`); any given reading can be registered at the next step (`Diagonal.Unfolds`).')

STATUS_ROW = ('| 描述保留什么、失去什么（P70–P72） | 已陈述并检查，不加前提：分离恰失去关系，关系只由共同作用形成，在各自不合并的律下持续，'
              '只由失去或共同作用结束（[separation-loses-the-relation](' + REC_SEP + ')）；确定的律下有意义的切分，所识的部分单独有意义的条件，'
              '状态从所识的历史读出，状态有限恰当所识从某一刻起重复（[the-split-that-makes-sense](' + REC_SPLIT + ')）；在所识之中的识恰在没有差别处完备，'
              '补全它是从不返回的展开，说谎者是节律（[registration-within-what-it-registers](' + REC_DIAG + ')）；不依语境的主张是表示的承诺，'
              '恰在诸识粘合处合，量子的识不粘合（[contextual-registration](' + REC_CTX + ')）。开放：有分支的框架下有意义的切分；概率的语境性；'
              '奇偶障碍的一般定理；读法待 Ren |')

CHOICE_ZH = ('- 描述保留什么、失去什么（P70–P72）：“两个之所以是一对，在于关系”与“成员从一对中读出”是否是 Ren 的读法；值是否读作在语境中的识'
             '（波与粒子都是投影）；Ren 推测的“真”是否读作关系的、按情境可推出而不能从一个情境全部说出；不依语境的主张是否列为表示的承诺'
             '（零前提计划由整合者提议）。')
CHOICE_EN = ('- What a description keeps and loses (P70–P72): whether “two are a pair by relation” and “the members are read '
             'off the pair” are Ren\'s readings; whether a value reads as a registration in context (wave and particle both '
             'projections); whether the “truth” of Ren\'s speculation reads as relational, derivable situationally and not '
             'all sayable from one situation; whether context-free claims are listed as a commitment of the representation '
             '(the integrator proposes it for the zero-premise plan).')

FURTHER_ZH = ('- 描述保留什么、失去什么：有分支的框架下有意义的切分（以 P69 的 `Alike` 重述确定的律的情形）；{FURTHER_LASSO_ZH}'
              '与外围 `RootCoverageBoundary` 的实例定理；奇偶障碍的一般定理；概率的语境性'
              '（Bell 型不等式）；多于两个部分的关系的生灭。')
FURTHER_EN = ('- What a description keeps and loses: the split that makes sense for branching frames (restating the determined '
              'case with P69\'s `Alike`); {FURTHER_LASSO_EN}'
              'the instance theorem to the periphery\'s `RootCoverageBoundary`; the general '
              'parity obstruction; probabilistic contextuality (Bell-type inequalities); how relations among more than two '
              'parts form and end.')

SPINE_L2 = '\n'.join([
    '| L2 | [Becoming.Diagonal]({LEAN}/Diagonal.lean) | 在所识之中的识（不加前提，P71）：以所读者为索引的族漏掉移动每个值之映射的缺口（Lawvere 的对角线），'
    '主张族从不完备，框架不以自己的配置实现每种关于配置的主张；以相等比较的值，完备恰在没有差别处，完备时有不动点；补全的展开每一步不完备，'
    '缺口两两不同，从不返回，没有有限储存持有，这样的展开存在；修正从不静止，二值的否定每两步返回 | {N_DIAGONAL} |',
    '| L2 | [Becoming.Context]({LEAN}/Context.lean) | 语境中的识（不加前提，P72）：诸识粘合恰当语境在相交处一致，不依语境的主张的框架恰在处处粘合时合，'
    '以语境为索引的框架总合；可能性局部而没有不依语境的读法时没有尊重它们的配置粘合；整体在其部分粘合成者之内，没有不依语境的读法、某个语境允许某物的可能性不是任何整体的部分；'
    'Specker 的三个盒子与 Mermin–Peres 方阵 | {N_CONTEXT} |',
    '| L2 | [Becoming.Quantum]({LEAN}/Quantum.lean) | Mermin–Peres 方阵的量子实现（P72q，由 P64–P68 的所有者写成）：两个量子比特上九个可观测量作为整数矩阵，'
    '平方为 I，每条线两两对易，线的乘积在第三列为 −I、否则为 I；态在一条线上共同显示的值是该线的一个可能，每个可能都被显示；所以没有不依语境的值 | {N_QUANTUM} |',
])
SPINE_L3 = ('| {LAYER} | [Becoming.Description]({LEAN}/Description.lean) | 描述保留什么、失去什么（不加前提，P70）：分离恰在整体为矩形处给回整体，失去的是关系，'
            '三个部分可以作为整体相关而任意两个自由，在 Specker 的三对上诸对不给回奇偶；关系只由共同作用形成，在各自不合并的律下持续，只由失去或共同作用结束；'
            '确定的律下保留所识并承载规律的最粗切分有意义，现在所识者有意义恰当它承载规律，部分单独有意义恰当其余对它的下一值不造成差别（控制者的规则在内）；'
            '位置与速度一对；状态从所识的历史读出，每段所识的历史是一条确定的律，状态有限恰当所识从某一刻起重复，返回的构型状态有限；二值否定恰有两个状态 | {N_DESCRIPTION} |')

GLOSS_NEW = '\n'.join([
    '| 矩形的整体／分离 | rectangular whole / separated description | 与一个部分同在的，与另一部分的每一项同在；分离的描述只说每个部分能是什么，'
    '恰在整体为矩形时给回整体；整体不是矩形，就是部分之间有关系 | `Rectangular`、`Separated`、`separation_faithful_iff` |',
    '| 同一状态 | one state (same ahead) | 一段所识的历史中，其后所识的一切相同的两个时刻；状态从历史读出，不给配置；状态有限恰当所识从某一刻起重复 | '
    '`SameAhead`、`alike_moments_iff`、`finitely_many_states_iff` |',
    '| 缺口／补全的展开 | gap / completing unfolding | 以所读者为索引的识把每个成员对自身之识经一个映射移动所得的读法，不被任何成员说出；'
    '保留所识、下一步识得缺口的识，每一步都不完备，从不返回 | `Diagonal.gap`、`Diagonal.gap_unsaid`、`Diagonal.Unfolds` |',
    '| 语境中的识／粘合 | contextual registration / gluing | 主张在语境中被识；诸识粘合，指有一个不依语境的读法与每个语境一致，恰当识同一主张的语境识得相同；'
    '不依语境的主张是表示的承诺 | `Contextual`、`Contextual.Glues`、`Contextual.glues_iff_agree`、`Contextual.fitsFree_iff` |',
])

EDITS = [
    ('before', '**形成、维持、转化、退化与消解都是沿运行的关系变化，不是五个阶段。**', PAIR_ZH + '\n\n' + PAIR_EN),
    ('before', '**知识。** [知识一章]', '\n\n'.join([SPLIT_ZH, SPLIT_EN, DIAG_ZH, DIAG_EN, CTX_ZH, CTX_EN])),
    ('replace', KNOW_ZH_OLD, KNOW_ZH_NEW),
    ('replace', KNOW_EN_OLD, KNOW_EN_NEW),
    ('after_line', '- 过程与框架是同一展开的读法', WHOLE_I_ZH),
    ('after_line', '- The process and the frame are readings of one unfolding', WHOLE_I_EN),
    ('before', '- **意义。** 规律与定理不给任何部分以意义', WHOLE_III_ZH),
    ('before', '- **Significance.** The laws and theorems give no part significance', WHOLE_III_EN),
    ('after_line', '| 一个关系的起点（P69） |', STATUS_ROW),
    ('before', '- 名称：本理论中由 AI 拟定的用语', CHOICE_ZH),
    ('before', '- Names: the terms the AI has proposed', CHOICE_EN),
    ('after_line', '- 一个关系的起点：第一部分以', FURTHER_ZH),
    ('after_line', '- One relational starting point: restating', FURTHER_EN),
    ('after_line', '| L2 | [Becoming.Recurrence]', SPINE_L2),
    ('after_line', '{SPINE_AFTER}', SPINE_L3),
    ('after_line', '| 有意义的描述 |', GLOSS_NEW),
]
