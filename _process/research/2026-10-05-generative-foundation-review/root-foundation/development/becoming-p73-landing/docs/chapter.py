"""Chapter edits for P73–P75, as (kind, anchor, text) edits applied by apply_docs.py.

kind: 'before' inserts text before the line starting with anchor (a blank line after a paragraph,
none after a list item or table row); 'after_line' inserts text as new lines after the line starting
with anchor; 'replace' replaces the exact substring anchor with text. Every anchor must occur once.
Placeholders {LEAN}, {PERI}, {STUDY_LEARNING}, {STUDY_WISDOM}, {S_LEARNING}, {S_WISDOM} and
{N_LEARNING} are filled by apply_docs.py.
"""

LEARN_ZH = '**学习：归纳、推广、训练与元层次（第一部分，P73）。** Ren 问对元层次、人工神经网络、认知与关于学习的智慧解释得多完整，随后写道：“please, fully complete, 我觉得理更像是对结构和变化的规律的建模 finish wisdom root, and resolve the undissolved”（[来源](../../../sources/15-codex-theory-conversations/2026-10-12-learning-wisdom-root-and-induction.md)；[Becoming.Learning]({LEAN}/Learning.lean)）。一个被识的序列是被识的值的序列，例如确定律之轨道的识；学习者是任何从第 t 步之前的记录作出的主张。不加前提：无记录固定下一个，即使在有限的世界中（`no_record_fixes_next`、`no_record_fixes_next_finite`）；对每个学习者，都有一个序列在每一步回答它、否证它的每个主张，它保留记录，所以开放（`diagonal_refutes`、`diagonal_unrested`、`diagonal_open`）。按否证学习（假设依次排列，恰在所持者被否证时移向下一个）从不越过成立的假设（`index_le_of_holds`）。确定律的轨道被列表所持时，其识从某步起周期重复（`lasso_of_held`）；不知配置也不知其数目、只读能分辨值之识的学习者，被否证少于 `tri N` 次（N 为配置数），从第 N 步起每步主张，不在任意晚处被否证（`held_learner_bounded`）；它静止这一点不能被否证（`held_rest_unrefuted`，双重否定），它只在这样的序列上静止（`lasso_of_rest`），它的记录从不表明它已静止（`no_record_fixes_next_finite`）。对类的学习是合并枚举上的同一学习，每种合并都有其对角序列（`merged_bound`、`merged_unrested`）。理依 Ren 读作对结构与变化之规律的建模：对结构的建模是一个归并（`Lumped`），对变化的建模是步骤经它同去的归并，两者是同一个概念（`goAlike_iff_lumped`）。在经归并同去的函数之中，有限数据固定未试之值，恰当它与某个观察输入被归并（`determines_lumped_iff`）；推广正确，恰当世界在两者取同一值（`lumped_right_iff`）；变化之律的结果转移，恰当两个配置以该动作同去（`transfer_right_iff`）；一切函数之类在未试之处自由，数据单独不固定任何东西（`every_determines_nothing`）。训练是经数据的选择（`Training.loss_through`，P64 的经识选择是其实例），在数据之外自由的类中使未试之值与类同样自由（`Training.unselected_beyond_data`）；拟合在数据之外正确，恰当类在那里由数据决定（`Training.fit_right_iff`）。外围桥接 [LearningCorrespondence]({PERI}/LearningCorrespondence.lean)（P74）：习得链的推广是经律的归并的推广（`uniform_determines`、`nonuniform_not_determined`），Hebb 式发展与更新路线是 P66 的 `adaptive` 系统，活动或网络单独没有律之处恰是权重或路线造成差别之处（`hebbian_no_activity_law`、`updating_no_network_law`）。读法（AI 的，待 Ren）：归纳被消解为规律而不是被保证；自然的一致性不是前提，而是世界经模型所归并者同去这一局部条件；对受训网络，类是训练所能达到的，推广来自结构与更新所施加的归并，不来自损失；元层次是再学习，没有顶层。见[研究 §{S_LEARNING}]({STUDY_LEARNING})、[learning-by-refutation](../results/records/learning-by-refutation.md) 与 [generalization-through-lumping](../results/records/generalization-through-lumping.md)。'

LEARN_EN = '**Learning: induction, generalization, training and the meta level (Part I, P73).** Ren asked how completely the meta level, artificial neural networks, cognition and the wisdom about learning are explained, then wrote "please, fully complete, 我觉得理更像是对结构和变化的规律的建模 finish wisdom root, and resolve the undissolved" (`Becoming.Learning`). A course is a sequence of registered values, such as the registration of a determined law\'s orbit; a learner is any claim made from the record before a step. With no premise: no record fixes the next value, even among finite worlds; for every learner a course answers and refutes each of its claims, and that course keeps its record, so it is open. Learning by refutation, holding hypotheses in order and moving on exactly where the one held is refuted, never passes a hypothesis that holds. Where a determined law\'s orbit is held by a list, its registration repeats from some step; a learner reading only a registration it can tell apart, knowing neither the configurations nor how many there are, is refuted fewer than `tri N` times for `N` configurations, claims at every step from step `N` on and is not refuted at arbitrarily late steps. That it comes to rest is unrefuted, a double negation; it rests only on such courses, and its record never shows that it has come to rest. Learning over classes is the same learning over a merged enumeration, and every merging has its diagonal course. 理 is read as Ren reads it, the modeling of the laws of structure and of change: a model of structure is a lumping, a model of change a lumping the step goes alike across, and the two are one notion. Within the functions going alike across a lumping, finite data fix an untried value exactly where it is lumped with an observed one, and the generalization is right exactly where the world takes one value at the two; an outcome of a law of change transfers exactly where the two configurations go alike by the move; the class of every function is free at every untried input, so data alone fix nothing there. Training is a selection through the data, P64\'s selection through registration being an instance; within a class free beyond the data it leaves the untried value as free as the class, and a fit is right beyond the data exactly where the class determines it. The periphery bridge (P74) reads the acquisition chain\'s transfer as generalization through a lumping of laws, and Hebbian development and the route of updating as P66\'s adaptive systems, activity or the network alone having no law exactly where the weights or the route make a difference. On the AI\'s readings, pending Ren, induction is resolved into laws rather than certified; the uniformity of nature is no premise but the local condition that the world goes alike across what the model lumps; for a trained network the class is what training can reach, and generalization comes from the lumping that architecture and updates impose, not from the loss; the meta level is learning again, with no top.'

THEORY_ZH_OLD = '失控读作在其一之中运行的回路，是启发，不是陈述；理 读作对识负责的模型。'

THEORY_ZH_NEW = '失控读作在其一之中运行的回路，是启发，不是陈述。理 依 Ren 读作对结构与变化之规律的建模（P73，见下文“学习”），取代 AI 先前的读法“对识负责的模型”；模型仍只经识被检验。'

WHOLE_ZH = '- **学习。** 无记录固定下一个（`no_record_fixes_next`）；每个学习者都有否证它每个主张的开放的序列（`diagonal_refutes`、`diagonal_open`）；被列表所持的世界中，按否证学习的否证有界、从某步起每步主张，它静止不能被否证，只在这样的世界中静止（`held_learner_bounded`、`held_rest_unrefuted`、`lasso_of_rest`）；推广恰在归并之处，正确恰在世界经归并同去之处，结构与变化是同一个归并（`determines_lumped_iff`、`lumped_right_iff`、`goAlike_iff_lumped`）；训练经数据选择，拟合在数据之外正确恰当类在那里决定（`Training.loss_through`、`Training.fit_right_iff`）；对类的学习是合并枚举上的同一学习（`merged_bound`、`merged_unrested`）。'

WHOLE_EN = '- **Learning.** No record fixes the next value (`no_record_fixes_next`); every learner has an open course refuting each of its claims (`diagonal_refutes`, `diagonal_open`); in a world held by a list, learning by refutation is refuted a bounded number of times and claims at every step from some step on, its coming to rest is unrefuted, and it rests only in such worlds (`held_learner_bounded`, `held_rest_unrefuted`, `lasso_of_rest`); generalization reaches exactly what a lumping lumps and is right exactly where the world goes alike across it, structure and change being one lumping (`determines_lumped_iff`, `lumped_right_iff`, `goAlike_iff_lumped`); training selects through the data, and a fit is right beyond the data exactly where the class determines it (`Training.loss_through`, `Training.fit_right_iff`); learning over classes is the same learning over a merged enumeration (`merged_bound`, `merged_unrested`).'

HYP_ZH = '- **假设与类。** 一个形成持有或能达到哪些假设、类或归并，它的识是否分辨值，它的世界是否被列表所持，不由动力学决定；数据单独不固定任何未试之值（`every_determines_nothing`），推广的正确以世界经归并同去为条件（`lumped_right_iff`），学习者的记录从不表明它已静止（`no_record_fixes_next_finite`）。'

HYP_EN = '- **Hypotheses and classes.** Which hypotheses, classes or lumpings a formation holds or can reach, whether its registration tells values apart and whether its world is held by a list are not decided by the dynamics; data alone fix no untried value (`every_determines_nothing`), a generalization is right on condition that the world goes alike across the lumping (`lumped_right_iff`), and a learner\'s record never shows that it has come to rest (`no_record_fixes_next_finite`).'

WISDOM_ROW_OLD = '| 核心作为智慧之根（[wisdom-root](../results/records/wisdom-root.md)） | 开放 |'

WISDOM_ROW_NEW = '| 核心作为智慧之根（[wisdom-root](../results/records/wisdom-root.md)） | 开放；形式部分在第一部分所及范围内完成（P75，[wisdom-root-part-one](../results/records/wisdom-root-part-one.md)）：识、理、检验、学习与推广、经识的选择与训练、够、失控与元层次的规律对每个学习者、每个表示成立，不用公理；仍开放的是实际形成的对应、关切与情感的形成，以及这组关系对全部智慧的充分性 |'

STATUS_ROW = '| 学习（P73、P74） | 已陈述并检查，不用公理：无记录固定下一个，每个学习者都有否证它每个主张的开放的序列，被列表所持的世界中按否证学习的否证有界、静止不能被否证且只在那里静止，何时静止不被识（[learning-by-refutation](../results/records/learning-by-refutation.md)）；推广恰在归并之处、正确恰在世界经归并同去之处，结构与变化是同一个归并，训练经数据选择，拟合在数据之外正确恰当类在那里决定；习得链与连接主义模型是脊柱上的实例（[generalization-through-lumping](../results/records/generalization-through-lumping.md)）。开放：概率的或近似的学习、可数类的一般界、优化的动力学与隐式偏置；实际网络施加哪个归并；读法待 Ren |'

EMP_ZH_OLD = '- 智慧的实际形成：说明智慧怎样实际形成（[wisdom-root](../results/records/wisdom-root.md)）；这是解释与经验的任务，不是进一步的证明。'

EMP_ZH_NEW = '- 智慧的实际形成：说明智慧怎样实际形成（[wisdom-root](../results/records/wisdom-root.md)）；其形式部分已在第一部分完成（[wisdom-root-part-one](../results/records/wisdom-root-part-one.md)），实际的人与 AI 是否经这些路线形成其理解与修正，是解释与经验的任务，不是进一步的证明。\n- 实际学习者与网络持有或能达到的类：一个实际网络的结构、起点与更新施加哪个归并，其与世界的对应（[generalization-through-lumping](../results/records/generalization-through-lumping.md)）。'

EMP_EN_OLD = '- How wisdom actually forms: an explanatory and empirical task, not a further proof.'

EMP_EN_NEW = '- How wisdom actually forms: its formal part is complete in Part I (wisdom-root-part-one); whether actual humans and AI form understanding and correction along these routes is an explanatory and empirical task, not a further proof.\n- The classes actual learners and networks hold or can reach: which lumping an actual network\'s architecture, starting points and updates impose, and its correspondence to the world.'

SPINE_L4 = '| L4 | [Becoming.Learning]({LEAN}/Learning.lean) | 学习（不加前提）：无记录固定下一个，有限世界中亦然；每个学习者都有否证它每个主张的序列，那是保留记录之律的识，开放；按否证学习从不越过成立的假设；被列表所持的世界中套索学习者否证少于 `tri N` 次、从第 N 步起每步主张、静止不能被否证，只在套索上静止，何时静止不被识；对类的学习是合并枚举上的同一学习；归并恰在它归并之处推广，正确恰在世界经归并同去之处，结构与变化是同一个归并；一切函数之类不固定任何未试之值；训练经数据选择，拟合在数据之外正确恰当类在那里决定 | {N_LEARNING} |'

GLOSS_LUMP = '| 理 | 理 (modeling of laws) | Ren 的读法（2026-10-12）：对结构与变化之规律的建模；形式上，对结构的建模是一个归并，对变化的建模是步骤经它同去的归并，两者是同一个概念（AI 对形式项的读法）；模型只经识被检验 | `Lumped`、`goAlike_iff_lumped`、`carries_law_iff` |\n| 归并／推广 | lumping / generalization | 输入的一个函数 π；经 π 同去的函数在 π 相同的输入取同一值；其中数据固定未试之值，恰当它与某个观察输入被归并；推广正确，恰当世界经归并同去 | `Lumped`、`Determines`、`determines_lumped_iff`、`lumped_right_iff` |\n| 自由（数据之外） | free (beyond the data) | 类的每个成员在数据上的值都能与每个成员在 x 的值组合；自由处数据只决定成员共有的；一切函数之类在每个未试之处自由 | `Free`、`free_determines_iff`、`every_determines_nothing` |\n| 训练 | training | 经数据的选择：在数据上一致的函数被选得相同；拟合在数据之外正确，恰当类在那里由数据决定；推广来自训练所能达到的类，不来自损失（后半是 AI 的读法） | `Training.Through`、`Training.loss_through`、`Training.fit_right_iff` |'

GLOSS_LEARN = '| 被识的序列／记录 | course / record | 被识的值的序列，例如确定律之轨道的识；第 t 步之前的值，最新在前 | `record`、`back_record` |\n| 按否证学习 | learning by refutation | 假设依次排列，恰在所持者被否证时移向下一个；从不越过成立的假设，越过的每个都在记录中被否证 | `indexOn`、`learner`、`index_le_of_holds`、`refuted_before` |\n| 套索 | lasso | 从某步起周期重复的序列；恰是被列表所持之世界的识；套索学习者在其上否证有界，静止不能被否证 | `Lasso`、`lasso_of_held`、`lasso_realized`、`lasso_learner_bounded`、`rest_unrefuted` |\n| 对角序列 | diagonal course | 在每一步回答学习者之主张、把它否证的序列；它是保留记录之律的识，所以开放 | `diagonal`、`diagonal_refutes`、`diagonal_open` |\n| 合并枚举（元层次） | merged enumeration (meta level) | 假设的类沿对合并为一个枚举；对类的学习是其上的同一学习，界复合；每种合并都有其对角序列 | `merged`、`merged_bound`、`merged_unrested` |'

EDITS = [
    # Section 3: learning after selection through registration, before knowledge.
    ('before', '**知识。** [知识一章]', LEARN_ZH + '\n\n' + LEARN_EN),
    # Section 3: Ren's reading of 理 in the P49 paragraph.
    ('replace', THEORY_ZH_OLD, THEORY_ZH_NEW),
    # Part I stated whole.
    ('before', '- **其余。** 运行上的端点丧失', WHOLE_ZH),
    ('before', '- **The rest.** The theorems on endpoint loss', WHOLE_EN),
    ('before', '- **意义。** 规律与定理不给任何部分以意义', HYP_ZH),
    ('before', '- **Significance.** The laws and theorems give no part significance', HYP_EN),
    # Section 8.
    ('replace', WISDOM_ROW_OLD, WISDOM_ROW_NEW),
    ('after_line', '| 与一般因果系统的比较（P64–P68） |', STATUS_ROW),
    ('replace', EMP_ZH_OLD, EMP_ZH_NEW),
    ('replace', EMP_EN_OLD, EMP_EN_NEW),
    # Section 9: the spine table.
    ('after_line', '| L4 | [Becoming.Selection]', SPINE_L4),
    # Section 10: the glossary.
    ('after_line', '| 描述／承载规律 | description / carries a law |', GLOSS_LUMP),
    ('after_line', '| 否证 | refutation |', GLOSS_LEARN),
]
