#!/usr/bin/env python3
"""R35 batch B1, before the move: what stays live of the two chapters that move is stated in the canonical chapter
(EN and ZH), with links to them at their present paths, which the move rewrites to their history paths.

* G0-WARRANT §2-§3 (what each kind of support for living significance contributes) -> one item of §8.5.
* PLURAL-SYSTEMS-AND-CORRECTION §15 (responsive transformation) -> one paragraph closing §4.

usage (from the checkout root): python3 -B folds_b1.py
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[6]
EN = ROOT / 'theories/becoming/chapters/THE-THEORY-OF-BECOMING.md'
ZH = ROOT / 'theories/becoming/chapters/THE-THEORY-OF-BECOMING.zh.md'
G0 = 'G0-WARRANT.md#2-支持的四种方式--four-kinds-of-support'
PL = 'PLURAL-SYSTEMS-AND-CORRECTION.md#15-responsive-transformation'
REC = '../results/records/'

SUPPORT_EN = (
    '- **What the support for living significance contributes.** Four kinds of support count for it comparatively, '
    'none as a proof: explanatory unification (care, repair, creation, learning, renewal, rest, finite fulfilment and '
    'constructive ending explained from one ground, without a separate value for each); discriminating content '
    '(renewing and consuming formation separated by descriptive content in one law class, where a one-step count '
    'ranks them the other way); discrimination against rivals (the minimality of each premise, and rival orderings '
    'shown independent of C or bounded); and fruitfulness for alignment (instructions, institutional aims and an AI\'s '
    'present purposes open to evaluation). The formal checks contribute inference, premise footprint, descriptive '
    'dynamical distinctions and independence. None verifies the starting commitment, and the dynamical theorems are '
    'sign-neutral, so whether their readings capture 生生 is a question of reading and correspondence. The account of '
    f'9 October 2026, written when living significance was an adopted axiom, with its table of checks: [history]({G0}).\n')
SUPPORT_ZH = (
    '- 对生命意义的支持各承担什么：四种支持都只作比较的理由，不作证明。解释的统一（照料、修复、创造、学习、更新、休息、有限的成全与有建设性的结束，'
    '由同一根据解释，不为每一项另设价值）；区分的内容（在一个规律类中以可描述的内容分开更新的形成与消耗的形成，而一步的计数把二者排反）；'
    '对竞争者的区分（每个前提的极小性，竞争的排序示为独立于 C 或有界）；对对齐的成果（指令、制度目标与 AI 当下的目的都可受评价）。'
    '形式检查承担推理、前提足迹、描述性的动力学区分与独立性；没有一项验证起点承诺，动力学定理按构造不带正负，所以其读法是否把握生生是读法与对应的问题。'
    f'2026 年 10 月 9 日（生命意义还是采用的公理时）的说明及其检查表见[历史]({G0})。\n')

RESPONSIVE_EN = (
    '**Responsive transformation** (因应转化). Understanding, purposes and action are reorganized through changing '
    'relations and consequences: activity alters the conditions of further activity, some effects become available to '
    'discernment and memory, and acquired understanding enters evaluation and changed practice. A warranted direction '
    'is not an assured outcome: a local mechanism can guarantee an effect within an established range without '
    'guaranteeing that the range, its interpretation or the reasons for the effect persist through every later change. '
    'The relations to examine are consequences becoming discernible, acquired grounds staying applicable to present '
    'circumstances, understanding changing operative purposes and practice, support continuing through a transition, '
    'and evaluation staying answerable to living consequences. Each has its own standing, and together they are not a '
    f'proved checklist (the pending-task composition, [acquired-revision-of-pending-task]({REC}acquired-revision-of-pending-task.md); '
    f'the retained routes, [versioned-request-completion]({REC}versioned-request-completion.md)). The direction is not the '
    'maximization of change, flexibility, information or compliance: constant revision can destroy the continuity '
    'learning needs, and persistence can sustain care or entrench a mistake. Revising an interpretation of the good '
    'gives no AI authority to exempt itself from warranted oversight; the bridge to *corrigibility* is the relational '
    'capacity for such transformation, including the forming and revising of the judgment about what should change. '
    f'The statement of 9 October 2026, with its table of conditions and their status: [history]({PL}).\n\n')
RESPONSIVE_ZH = (
    '**因应转化。** 理解、目的与行动经由变化着的关系与后果而重组：活动改变后续活动的条件，一些效果成为可辨识、可记忆的，'
    '取得的理解进入评价与改变了的实践。有根据的方向不是有保证的结果：局部机制可在已建立的范围内保证某一效果，'
    '却不保证这一范围、它的解释或效果的理由在之后的每次变化中都持续。要考察的关系是：后果变得可辨识，取得的根据对当下的情形仍适用，'
    '理解改变起作用的目的与实践，支持在过渡中延续，评价对活的后果仍可问责。各项有各自的地位，合起来不是已证明的清单'
    f'（待办任务的组合，[acquired-revision-of-pending-task]({REC}acquired-revision-of-pending-task.md)；保留的路径，'
    f'[versioned-request-completion]({REC}versioned-request-completion.md)）。这一方向不是使变化、灵活、信息或服从最大：'
    '不断的修订会毁掉学习所需的连续，持续可以维系照料也可以固化错误。修订对善的解释，不给 AI 免于有根据的监督的权限；'
    '与 *corrigibility* 的连接是这种转化的关系能力，包括形成并修订“什么该改变”的判断。'
    f'2026 年 10 月 9 日的陈述及其条件表见[历史]({PL})。\n\n')


def insert_before(text, marker, block):
    assert text.count(marker) == 1, marker[:50]
    assert block not in text
    return text.replace(marker, block + marker)


en = EN.read_text()
en = insert_before(en, '- **Calling the generative space good.** Two questions of warrant', SUPPORT_EN)
en = insert_before(en, '<a id="5-评价的形成--how-evaluation-forms"></a>\n## 5. How evaluation forms', RESPONSIVE_EN) \
    if '<a id="5-评价的形成--how-evaluation-forms"></a>\n## 5. How evaluation forms' in en \
    else insert_before(en, '## 5. How evaluation forms', RESPONSIVE_EN)
EN.write_text(en)
zh = ZH.read_text()
zh = insert_before(zh, '- 称生成的空间为好：两个根据问题', SUPPORT_ZH)
zh = insert_before(zh, '<a id="5-评价的形成--how-evaluation-forms"></a>\n## 5. 评价的形成', RESPONSIVE_ZH)
ZH.write_text(zh)
print('folded')
