#!/usr/bin/env python3
"""I4b-3: the documents naming Becoming.Horizon and its PrefixSafety instance (run from the repository root).

* the theory chapter's §9 row for Becoming.Horizon (what it states, now bilingual, and its theorem count);
* a §9 periphery row for PrefixSafetyCorrespondence, and its name in the chapter's lists of peripheral instance
  modules, zh and en;
* the module bullet in Becoming.lean;
* a paragraph under the completion package README's table.
Each edit asserts the text it replaces, so a second run fails."""
import re
from pathlib import Path

LEAN = 'experiments/integrated-correction/general-framework/generative-basis/lean/'
FORMAL = 'experiments/integrated-correction/general-framework/generative-basis/mathematical-abstraction/completion/formal/'
HORIZON = Path(LEAN + 'becoming/Becoming/Horizon.lean')
INSTANCE = Path(FORMAL + 'PrefixSafetyCorrespondence.lean')


def count(path):
    return sum(1 for line in path.read_text().splitlines() if re.match(r'^theorem ', line))


def change(s, old, new, what):
    assert s.count(old) == 1, what
    return s.replace(old, new)


chapter = Path('theories/becoming/chapters/THE-THEORY-OF-BECOMING.md')
s = chapter.read_text()
s = change(s, '| 有限前缀不决定分类，有反馈时也如此；按数量的读法 | 12 |',
           '| 有限前缀不决定分类，有反馈时也如此；按数量的读法。'
           '有限历史所否证者（不加前提）：读法可否证，当其外每个运行有一界，过此界与它一致的运行都不在其内；'
           '可否证的读法在每个附着于它的运行上于双重否定下成立，稳定的读法附着即成立；'
           '其外有附着运行的读法既不可否证也不可证实（复现与终于发生皆然）；'
           '由测试构成的读法在附着处成立，对每个过程要求其可否证恰是 Markov 原则。'
           '/ No finite prefix decides the classification, with feedback too; a reading of amounts. '
           'What a finite history refutes (no premise): a reading is refutable where every run outside it has a '
           'horizon past which no agreeing run is inside; a refutable reading holds up to double negation at every run '
           'adhering to it, and for a stable reading adhering is holding; a reading with an adhering run outside it is '
           'neither refutable nor verifiable (so recurrence and eventual occurrence); a reading made of tests holds '
           'where it adheres, and asked of every process its refutability is exactly Markov\'s principle. '
           f'| {count(HORIZON)} |', 'chapter Horizon row')
living = s[s.index('| 外围实例 / Peripheral instances | [LivingOrganizationCorrespondence]'):]
living = living[:living.index('\n') + 1]
s = change(s, living, living +
           '| 外围实例 / Peripheral instances | [PrefixSafetyCorrespondence](../../../' + FORMAL +
           'PrefixSafetyCorrespondence.lean) | 无穷迹前缀序中的实例，用 Lean 4.30.0-rc2，由 check_prefix_safety_correspondence.py '
           '另行检查，只用标准公理：迹即核心 `Sequences.process` 的运行，同前缀即核心的 `Run.AgreeUpTo`（`samePrefix_iff_agree`），'
           '有限可否证即核心的 `Refutable`，前缀闭包即附着（`finiteRefutable_iff_refutable`、`prefixClosure_iff_adheres`），'
           '复现与终止事件不可有限否证由核心的 `Sequences` 律给出，这五项公理报告为空；以 Lean 的经典推理，核心的 '
           '`Refutable.not_not`、`Refutable.adheres_least` 给出 `holds_of_prefixClosure_by_core`、`prefixClosure_least_by_core`，'
           '核心的 `Markov` 与 `refutable_passes` 给出 `boundary_closed_by_core`。'
           '/ The instance in the prefix order of infinite traces, with Lean 4.30.0-rc2, checked separately by '
           'check_prefix_safety_correspondence.py with standard axioms only: traces are the runs of the core\'s '
           '`Sequences.process`, a shared prefix is the core\'s `Run.AgreeUpTo` (`samePrefix_iff_agree`), finite '
           'refutability is the core\'s `Refutable` and the prefix closure is adherence (`finiteRefutable_iff_refutable`, '
           '`prefixClosure_iff_adheres`), and recurrence and the termination event are not finitely refutable by the '
           'core\'s `Sequences` laws, these five with empty axiom reports; with Lean\'s classical reasoning the core\'s '
           '`Refutable.not_not` and `Refutable.adheres_least` give `holds_of_prefixClosure_by_core` and '
           '`prefixClosure_least_by_core`, and the core\'s `Markov` and `refutable_passes` give `boundary_closed_by_core`. '
           f'| {count(INSTANCE)} |\n', 'chapter periphery row')
s = change(s, '关系的组织形成及组织中池的起源同样经', '关系的组织形成、组织中池的起源及无穷迹的前缀序同样经', 'zh list words')
s = change(s, 'OrganizationCorrespondence、LivingOrganizationCorrespondence）', 
           'OrganizationCorrespondence、LivingOrganizationCorrespondence、PrefixSafetyCorrespondence）', 'zh list')
s = change(s, "organizational formation and the origin of an organization's pools connect",
           "organizational formation, the origin of an organization's pools and the prefix order of infinite traces "
           "connect", 'en list words')
s = change(s, 'OrganizationCorrespondence, LivingOrganizationCorrespondence)',
           'OrganizationCorrespondence, LivingOrganizationCorrespondence, PrefixSafetyCorrespondence)', 'en list')
chapter.write_text(s)

package = Path(LEAN + 'becoming/Becoming.lean')
s = package.read_text()
s = change(s, """* `Becoming.Horizon` (L3): no finite stretch of a run decides whether its drawing
  renews or consumes in the whole-run sense, with or without feedback; a reading of
  amounts is decided step by step.
""", """* `Becoming.Horizon` (L3): no finite stretch of a run decides whether its drawing
  renews or consumes in the whole-run sense, with or without feedback; a reading of
  amounts is decided step by step. What a finite history refutes, with no premise: a
  refutable reading holds, up to double negation, at every run adhering to it; a reading
  with an adhering run outside it is neither refutable nor verifiable; a reading made of
  tests holds where it adheres, and asked of every process its refutability is exactly
  Markov's principle.
""", 'package bullet')
package.write_text(s)

readme = Path(FORMAL + 'README.md')
s = readme.read_text()
s = change(s, """| [CompletionBoundaries.lean](CompletionBoundaries.lean) | Why compactness and generation cannot be dropped from the completion role. |
""", """| [CompletionBoundaries.lean](CompletionBoundaries.lean) | Why compactness and generation cannot be dropped from the completion role. |

16 October 2026: [PrefixSafetyCorrespondence.lean](PrefixSafetyCorrespondence.lean) reads `PrefixSafety` as an instance of the Becoming core's laws of what a finite history refutes (`Becoming.Horizon`): traces are the runs of the core's process of all sequences, finite refutability is its `Refutable`, the prefix closure is adherence, and the classical theorems follow from the core's laws up to double negation and Markov's principle. It imports the core, so `check.py` does not compile it; [check_prefix_safety_correspondence.py](check_prefix_safety_correspondence.py) checks it with Lean 4.30.0-rc2, and `PrefixSafety` must match this package's receipt. `PrefixSafety` and the package receipt are unchanged.
""", 'completion README')
readme.write_text(s)
print('Horizon row (', count(HORIZON), 'theorems), periphery row (', count(INSTANCE), '), lists, bullet, README')
