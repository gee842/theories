"""Edits to theories/becoming/chapters/COGNITION-LEARNING-AND-EVOLUTION.md for P73 and P74, as (kind, anchor, text),
applied by apply_docs.py like docs/chapter.py: 'before' inserts text before the line starting with the anchor,
'replace' replaces the anchor, which must occur once. Placeholders {LEAN}, {PERI} and {STUDY_LEARNING} are filled
there. The chapter is the AI's research account; Ren's words are quoted and marked."""

SECTION_2 = (
    '### Laws of learning on the Becoming spine (P73, P74)\n\n'
    'On 12 October 2026 Ren asked how completely the meta level, artificial neural networks, cognition and the '
    'wisdom about learning are explained, then wrote "please, fully complete, 我觉得理更像是对结构和变化的规律的建模 '
    'finish wisdom root, and resolve the undissolved". The core module [Becoming.Learning]({LEAN}/Learning.lean) '
    'states learning\'s general laws with no axiom ([study]({STUDY_LEARNING})). No record fixes the next value, also '
    'among worlds held by a list. For every learner a course refutes each of its claims; that course is the '
    'registration of a law keeping its record, so open. Learning by refutation never passes a hypothesis that holds. '
    'Where a list holds the world it is refuted a bounded number of times and its coming to rest is unrefuted, while '
    'when it rests is not registered. Learning how to learn is the same learning over a merged enumeration of '
    'classes, and every merging has its diagonal course. Transfer is generalization through a lumping: the data '
    'determine an untried case exactly where the class lumps it with an observed one. The transfer is right exactly '
    'where the world takes one value across the lumping. Without a class, data fix nothing.\n\n'
    'The periphery bridge [LearningCorrespondence]({PERI}/LearningCorrespondence.lean) reads this chapter\'s earlier '
    'constructions as instances. Under fixed weights, the network\'s development is the orbit of its step. Hebbian '
    'development and the network under a route of updating are one determined process on the joint configuration. '
    'Activity, or the network, has a law of its own exactly where the weights, or the route, make no difference. In the '
    'three-unit memory and at the starting network they do make a difference. The responsive route learns exactly '
    'where the task fails. These are laws of every learner at the stated scope. Which classes an actual learner holds '
    'or can reach, how its registration discriminates, and whether its world is finite are settled by correspondence, '
    'not by these theorems.\n\n'
    '**学习的规律（P73、P74）。** 核心模块不用公理陈述学习的一般规律：无记录固定下一个；每个学习者都有否证它每个主张的开放的序列；'
    '按否证学习从不越过成立的假设；被列表所持的世界中其否证有界，静止不能被否证，何时静止不被识；学会怎样学习是合并枚举上的同一学习。'
    '迁移是经归并的推广：数据恰在类把未试之例与已观察者归并之处决定它，正确恰在世界经归并取同一值之处。外围桥接把本章既有的构造读作实例：'
    'Hebb 式发展与更新路线下的网络是联合配置上的一个确定过程。实际学习者持有哪些类、怎样分辨、其世界是否有限，由对应决定，不由这些定理决定。'
)

ROW_SYSTEMATIC_READ = 'grammar formation, richer concepts, unrestricted counterfactual modeling and natural language remain open. |'
ROW_SYSTEMATIC = (
    'grammar formation, richer concepts, unrestricted counterfactual modeling and natural language remain open. On the '
    'Becoming spine (P73, P74) transfer to unencountered combinations is generalization through a lumping: the data '
    'determine an untried case exactly where the class lumps it with an observed one, the uniform-law premise is that '
    'lumping, and without a class data fix nothing. |')
ROW_LEARNING_READ = 'Their generality and psychological realization still require correspondence. |'
ROW_LEARNING = (
    'Their generality and psychological realization still require correspondence. The Becoming spine now states '
    'learning\'s general laws with no axiom (P73): no record fixes the next value; every learner has an open course '
    'refuting each of its claims; where a list holds the world, learning by refutation is refuted a bounded number of '
    'times, its coming to rest unrefuted and not registered. Learning how to learn is the same learning one level up, '
    'and a network changing its weights or its route of updating has its law on the joint configuration (P74). |')

SECTION_4 = (
    '**On the Becoming spine (P74).** The uniform-law premise is a lumping of laws. Within the uniform family with '
    'distinguishable primitive effects, the three encounters determine every expression (`uniform_determines`, '
    'Becoming.Learning\'s `Determines`). Admitting the nonuniform law, they determine nothing at the novel expression '
    '(`nonuniform_not_determined`). The limit above, "a nonuniform law can agree with all three training encounters", '
    'is the general law that the class of every function fixes no untried value (`every_determines_nothing`).\n\n'
    '**脊柱上（P74）。** 一致律前提是规律的一个归并：在原子效果可分辨的一致律族中，三次接触决定每个表达式；容许非一致律时，在新表达式处'
    '什么也不决定。上文“非一致律可与三次训练接触都一致”是一般规律“一切函数之类不固定任何未试之值”的情形。'
)

EDITS = [
    ('before', '## 3. From organization to cognitive activity', SECTION_2),
    ('replace', ROW_SYSTEMATIC_READ, ROW_SYSTEMATIC),
    ('replace', ROW_LEARNING_READ, ROW_LEARNING),
    ('before', '### Formation and repair of the operative connection', SECTION_4),
]
