#!/usr/bin/env python3
"""Landing edits for P80 in a checkout W: copy `Becoming.Counterfactual`, and edit the root module, the
checker's CORE and scope, and the Lean README. Usage: python3 -B land_edits.py W

Every anchor must occur exactly once; rerunning on an applied checkout fails."""
import re
import shutil
import sys
from pathlib import Path

W = Path(sys.argv[1]).resolve()
PKG = Path(__file__).resolve().parent
B = W / 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming'

assert not (B / 'Becoming/Counterfactual.lean').exists(), 'already landed'
shutil.copyfile(PKG / 'lean/Becoming/Counterfactual.lean', B / 'Becoming/Counterfactual.lean')


def edit(path, pairs):
    s = path.read_text()
    for a, b in pairs:
        assert s.count(a) == 1, (path.name, a[:80], s.count(a))
        s = s.replace(a, b)
    path.write_text(s)
    print('edited', path.relative_to(W))


def declared(names):
    text = (B / 'Becoming/Counterfactual.lean').read_text()
    for n in names:
        last = n.split('.')[-1]
        assert (re.search(rf'^(theorem|def|structure|inductive|abbrev)\s+\S*{re.escape(last)}\b', text, re.M)
                or re.search(rf'^namespace {re.escape(n)}$', text, re.M)), n


BULLET = """* `Becoming.Counterfactual` (L4): the rest's exchange given by a law of what has stood, the
  counterfactual of an act is the course the law gives: fixed by the act, existing exactly where
  feasible. Where the law reads only what each formation registers, P65's response premise is a
  theorem, and with finitely many conditions the registration is what the law is sensitive to;
  the comparison is then decided within the responsive reach with neither the second flow nor
  the response supplied. An act not taken is an intervention of the standard causal model. The
  readings are the AI's, pending Ren.
"""
root = B / 'Becoming.lean'
edit(root, [
    ('import Becoming.Response\n', 'import Becoming.Response\nimport Becoming.Counterfactual\n'),
    ('* `Becoming.Selection` (L4):', BULLET + '* `Becoming.Selection` (L4):'),
])

SCOPE = (
    '    "Counterfactual: where the rest exchanges by a law reading what has stood, two balanced flows in "\n'
    '    "which the part acts alike, starting alike, are one flow; the law generates a course, the orbit "\n'
    '    "of one determined law on the stage and the history so far, which balances exactly where the law "\n'
    '    "never takes more than stands and is given; the counterfactual of an act is the course it "\n'
    '    "generates; where the law reads only what each formation registers, the rest responds through its "\n'
    '    "registration in any two courses, and with finitely many conditions every law of what has stood "\n'
    '    "reads through what it is sensitive to, the least registration; the comparison is then decided "\n'
    '    "within the responsive reach with neither the second flow nor the response supplied; the course is "\n'
    '    "a trajectory of the standard model whose input is the part\'s move, an act not taken an "\n'
    '    "intervention. "\n')
edit(B / 'check_becoming.py', [
    ('"Becoming.Response",', '"Becoming.Response", "Becoming.Counterfactual",'),
    ('    "Selection: two histories are selected alike', SCOPE + '    "Selection: two histories are selected alike'),
])

NAMES = ['counterfactual_fixed', 'ExchangeLaw.course_balances_iff', 'counterfactual_is_course',
         'ExchangeLaw.course_unique', 'ExchangeLaw.Through.responds', 'ExchangeLaw.Nonanticipating.through_sensitive',
         'ExchangeLaw.Through.registers_of_sensitive', 'comparison_with_act', 'ExchangeLaw.course_trajectory',
         'ExchangeLaw.act_not_taken', 'Loop.responds_by_law', 'Loop.courses_fixed']
declared(NAMES)
ROW = ('| L4 | [`Becoming.Counterfactual`](Becoming/Counterfactual.lean) | '
       '回应由动力学给出（不用公理；交换律、它读已立者与进程可行是各定理的假设）：其余遵从一个读已立者的交换律时，部分动作相同、'
       '起始相同的两个平衡的流是一个流（`counterfactual_fixed`）；律生成的进程平衡恰当可行（`ExchangeLaw.course_balances_iff`），'
       '动作的反事实就是它生成的进程，每个形成都遵从一个律时平衡的流就是律的进程（`counterfactual_is_course`、'
       '`ExchangeLaw.course_unique`）；律只读各形成所识时，P65 的经识回应是定理（`ExchangeLaw.Through.responds`），条件有限时'
       '读已立者的律经其敏感而读，敏感是最小的识（`ExchangeLaw.Nonanticipating.through_sensitive`、'
       '`ExchangeLaw.Through.registers_of_sensitive`）；比较在动作与另一动作生成的进程之间、在回应所及之内决定，不另给第二个流与'
       '回应（`comparison_with_act`）；进程是以部分的动作为输入的标准因果模型的轨道，未取的动作是干预（'
       '`ExchangeLaw.course_trajectory`、`ExchangeLaw.act_not_taken`）；`Loop` 的回应是律（`Loop.responds_by_law`、'
       '`Loop.courses_fixed`）；读法是 AI 的，待 Ren / '
       "the response as the dynamics give (no axiom; the law of exchange, that it reads what has stood, and feasibility "
       "are hypotheses of the theorems that use them): where the rest follows one law reading what has stood, two "
       "balanced flows in which the part acts alike, starting alike, are one flow (`counterfactual_fixed`); the course "
       "the law generates balances exactly where it is feasible (`ExchangeLaw.course_balances_iff`), the "
       "counterfactual of an act is the course it generates, and where every formation follows one law a balanced "
       "flow is the law's course (`counterfactual_is_course`, `ExchangeLaw.course_unique`); where the law reads only "
       "what each formation registers, P65's response premise is a theorem (`ExchangeLaw.Through.responds`), and with "
       "finitely many conditions a law of what has stood reads through what it is sensitive to, the least "
       "registration (`ExchangeLaw.Nonanticipating.through_sensitive`, `ExchangeLaw.Through.registers_of_sensitive`); "
       "the comparison of an act with the course another act generates is decided within the responsive reach with "
       "neither the second flow nor the response supplied (`comparison_with_act`); the course is a trajectory of the "
       "standard causal model whose input is the part's move, and an act not taken is an intervention "
       "(`ExchangeLaw.course_trajectory`, `ExchangeLaw.act_not_taken`); `Loop`'s reply is a law "
       "(`Loop.responds_by_law`, `Loop.courses_fixed`); the readings are the AI's, pending Ren |\n")

readme = B / 'README.md'
s = readme.read_text()
i = s.index('| [`Becoming.Response`](Becoming/Response.lean) |')
i = s.rindex('\n', 0, i) + 1
j = s.index('\n', i) + 1
assert '`Becoming.Counterfactual`' not in s
s = s[:j] + ROW + s[j:]
readme.write_text(s)
edit(readme, [
    ('`Response` 导入 `Testing`；', '`Response` 导入 `Testing`；`Counterfactual` 导入 `Response` 与 `Mechanism`；'),
    ('`Response` imports `Testing`;', '`Response` imports `Testing`; `Counterfactual` imports `Response` and `Mechanism`;'),
])
