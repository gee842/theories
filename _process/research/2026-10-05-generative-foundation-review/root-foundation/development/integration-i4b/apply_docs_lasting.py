#!/usr/bin/env python3
"""I4b-4: the documents naming Becoming.Lasting's lifting laws and the FiniteBranching instance (run from the
repository root).

* the module docstring of Lasting.lean: a bullet for the new section;
* the theory chapter's §9 row for Becoming.Lasting (what it states and its theorem count);
* a §9 periphery row for FiniteBranchingCorrespondence, and its name in the chapter's lists of peripheral instance
  modules, zh and en;
* the module bullet in Becoming.lean;
* a paragraph in the completion package README.
Each edit asserts the text it replaces, so a second run fails."""
import re
from pathlib import Path

LEAN = 'experiments/integrated-correction/general-framework/generative-basis/lean/'
FORMAL = 'experiments/integrated-correction/general-framework/generative-basis/mathematical-abstraction/completion/formal/'
LASTING = Path(LEAN + 'becoming/Becoming/Lasting.lean')
INSTANCE = Path(FORMAL + 'FiniteBranchingCorrespondence.lean')


def count(path):
    return sum(1 for line in path.read_text().splitlines() if re.match(r'^theorem ', line))


def change(s, old, new, what):
    assert s.count(old) == 1, what
    return s.replace(old, new)


s = LASTING.read_text()
s = change(s, """
Every condition named here is local: one step from each configuration.""", """* **Lasting some course.** `Lasts` asks every admissible course to stay; here some course goes
  on. `Continues P n s`: some course of `n` steps starts at `s`; `Unbounded P s`: courses of
  every length do. Where the process branches finitely (`FinitelyBranching`), the depth reached
  is decided (`Continues.decided`), and an unbounded configuration cannot fail to have an
  unbounded successor (`Unbounded.step_not_not`). That it has one follows from
  `EitherThroughout` (`Unbounded.step_of_either`), and asked of every finitely branching process
  it is exactly that principle (`step_iff_either`, witness the two chains of `Chains`). A
  selection of a successor staying in a family gives a run from each member (`runOf`), so
  `EitherThroughout` and a choice of an unbounded successor lift courses of every length to a run
  (`lifting`). Where the branching is infinite, courses of every length need not continue one
  another (`Fan.no_unbounded_step`).

Every condition named here is local: one step from each configuration.""", 'Lasting docstring')
LASTING.write_text(s)

chapter = Path('theories/becoming/chapters/THE-THEORY-OF-BECOMING.md')
s = chapter.read_text()
s = change(s, '历史形式、数值形式与对偶各需判定，各有见证。/ Lasting a number of steps',
           '历史形式、数值形式与对偶各需判定，各有见证。有限分支处持续某段进程（不加前提）：所达深度已定；有每个长度进程者不能没有同样的后继，'
           '有之由 EitherThroughout 给出，对每个有限分支进程要求时恰是此原则，选取给出运行；无限分支时不然（扇）。'
           '/ Lasting a number of steps', 'chapter Lasting row zh')
s = change(s, 'and witnesses show where each decision is needed. | 69 |',
           'and witnesses show where each decision is needed. Lasting some course where branching is finite (no premise): '
           'the depth reached is decided; a configuration with courses of every length cannot fail to have a successor '
           'with them, has one given EitherThroughout, exactly that principle asked of every finitely branching process, '
           f'and a selection gives a run; where branching is infinite it need not (the fan). | {count(LASTING)} |',
           'chapter Lasting row en')
prefix = s[s.index('| 外围实例 / Peripheral instances | [PrefixSafetyCorrespondence]'):]
prefix = prefix[:prefix.index('\n') + 1]
s = change(s, prefix, prefix +
           '| 外围实例 / Peripheral instances | [FiniteBranchingCorrespondence](../../../' + FORMAL +
           'FiniteBranchingCorrespondence.lean) | 有限分支提升中的实例，用 Lean 4.30.0-rc2，由 '
           'check_finite_branching_correspondence.py 另行检查，只用标准公理：关系即一个动作的过程，`Reach` 即核心的 '
           '`Lasting.Continues`，`Unbounded` 即 `Lasting.Unbounded`，列出的子节点使过程有限分支（`reach_iff_continues`、'
           '`unbounded_iff`、`finitelyBranching`），这几项公理报告为空；经典推理给出 `EitherThroughout`（`either_classical`），'
           'Lean 的选择选取无界后继，核心的 `EitherThroughout.list`、`Lasting.Unbounded.step_of_either`、`Lasting.lifting` 与 '
           '`Lasting.unbounded_start_of_either` 给出 `finite_unbounded`、`unbounded_child`、`infinite_from_unbounded`、'
           '`finite_initial_lifting` 与 `labelled_lifting`（各为 `_by_core`）。'
           '/ The instance in finite-branching lifting, with Lean 4.30.0-rc2, checked separately by '
           'check_finite_branching_correspondence.py with standard axioms only: a relation is the process with one move, '
           '`Reach` is the core\'s `Lasting.Continues` and `Unbounded` its `Lasting.Unbounded`, and listed children make '
           'the process finitely branching (`reach_iff_continues`, `unbounded_iff`, `finitelyBranching`), these with empty '
           'axiom reports; classical reasoning gives `EitherThroughout` (`either_classical`), Lean\'s choice selects an '
           'unbounded successor, and the core\'s `EitherThroughout.list`, `Lasting.Unbounded.step_of_either`, '
           '`Lasting.lifting` and `Lasting.unbounded_start_of_either` give `finite_unbounded`, `unbounded_child`, '
           '`infinite_from_unbounded`, `finite_initial_lifting` and `labelled_lifting` (each `_by_core`). '
           f'| {count(INSTANCE)} |\n', 'chapter periphery row')
s = change(s, '组织中池的起源及无穷迹的前缀序同样经', '组织中池的起源、无穷迹的前缀序及有限分支的提升同样经', 'zh list words')
s = change(s, 'LivingOrganizationCorrespondence、PrefixSafetyCorrespondence）',
           'LivingOrganizationCorrespondence、PrefixSafetyCorrespondence、FiniteBranchingCorrespondence）', 'zh list')
s = change(s, "the origin of an organization's pools and the prefix order of infinite traces connect",
           "the origin of an organization's pools, the prefix order of infinite traces and finite-branching lifting "
           "connect", 'en list words')
s = change(s, 'LivingOrganizationCorrespondence, PrefixSafetyCorrespondence)',
           'LivingOrganizationCorrespondence, PrefixSafetyCorrespondence, FiniteBranchingCorrespondence)', 'en list')
chapter.write_text(s)

package = Path(LEAN + 'becoming/Becoming.lean')
s = package.read_text()
s = change(s, """  is at most `n` at the start. Where the histories form, the numeric form and the duality with
  lasting need a decision, a theorem shows it.
""", """  is at most `n` at the start. Where the histories form, the numeric form and the duality with
  lasting need a decision, a theorem shows it. Some course lasting: where the process branches
  finitely, the depth reached is decided, and a configuration with courses of every length
  cannot fail to have a successor with them; it has one given `EitherThroughout`, exactly that
  principle asked of every finitely branching process, and a selection gives a run. Where the
  branching is infinite it need not.
""", 'package bullet')
package.write_text(s)

readme = Path(FORMAL + 'README.md')
s = readme.read_text()
anchor = s[s.index('16 October 2026: [PrefixSafetyCorrespondence.lean]'):]
anchor = anchor[:anchor.index('\n') + 1]
s = change(s, anchor, anchor + """
16 October 2026: [FiniteBranchingCorrespondence.lean](FiniteBranchingCorrespondence.lean) reads `FiniteBranching` as an instance of the Becoming core's laws of lasting some course (`Becoming.Lasting`): a relation is the process with one move, `Reach` is its `Continues` and `Unbounded` its `Unbounded`, and each theorem follows from the core's laws with the classical steps named (`EitherThroughout` from excluded middle, Lean's choice for the selection). It imports the core, so `check.py` does not compile it; [check_finite_branching_correspondence.py](check_finite_branching_correspondence.py) checks it with Lean 4.30.0-rc2, and `FiniteBranching` must match this package's receipt. `FiniteBranching` and the package receipt are unchanged.
""", 'completion README')
readme.write_text(s)
print('Lasting docstring; Lasting row (', count(LASTING), 'theorems), periphery row (', count(INSTANCE),
      '), lists, bullet, README')
