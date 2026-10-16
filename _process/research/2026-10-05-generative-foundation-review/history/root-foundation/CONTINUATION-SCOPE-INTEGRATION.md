# Which continuations a choice must count

6 October 2026. AI-authored continuation of the
[inquiry-warrant integration](CONSEQUENCE-INQUIRY-WARRANT-INTEGRATION.md)
under [Ren's request to aim for a complete alignment solution](../../../../theories/becoming/chapters/ALIGNMENT-COMPLETION.md).
Named connection: **a choice's actual reach → the continuations it must count
→ what the structure of the choice settles, and what it leaves to evaluation
and governance**. It bears on alignment requirements 2 (ground and revise
concern) and 5 (plural agency and authority). It completes neither.

**Accepted scope.** The new module
[`ContinuationScope.lean`](../../../../experiments/integrated-correction/general-framework/generative-basis/mathematical-abstraction/acquisition/feedback/remaining-dependency/formal/ContinuationScope.lean)
has 22 audited declarations (13 theorems, 9 definitions) and depends only on
`propext` and `Quot.sound`. It has no `sorry`, custom axiom, `native_decide`
or `Classical.choice`. An independent AI review accepted it with corrections,
listed in section 5 and applied. The
[build record](../../../../experiments/integrated-correction/general-framework/generative-basis/mathematical-abstraction/acquisition/feedback/remaining-dependency/formal/inquiry-warrant/BUILD.md)
covers both new modules.

## 1. Setting

The previous round took the list of surviving continuations as supplied. Here
a situation lists available courses, the continuations under consideration,
and which continuations each course secures. A continuation is **reached**
when two available courses differ on securing it. A course **needlessly
forecloses** when another available course secures everything it secures and
more. A course that no other course improves on in this way is
**non-foreclosing**.

## 2. What is proved

- **Unreached continuations never matter** (`unreached_never_matters`,
  `nonforeclosing_restrict_iff`). Counting exactly the reached continuations
  gives the same verdicts as counting all listed ones. Reach is derived from
  the supplied courses and secures relation; it is not a separately supplied
  list of who counts. The result is close to definitional.
- **Omitting a reached continuation distorts in both directions**
  (`omitted_scope_admits_needless_foreclosure`, `omitted_scope_can_condemn`).
  For any omitted continuation there is a constructed situation in which the
  narrowed assessment endorses a needless foreclosure of it. In another
  situation, narrowing condemns a course that forecloses nothing needlessly.
  A scope narrower than the choice's reach cannot be relied on in either
  direction. This generalizes the previous round's self-scoped invariance:
  the problem is omission of a reached continuation, whoever bears it.
- **A non-foreclosing course always exists** (`nonforeclosing_exists`) in any
  finite situation with at least one course. Avoiding needless foreclosure is
  therefore always achievable. It is a floor that never asks for the
  impossible.
- **Structure alone cannot settle symmetric competition**
  (`both_courses_nonforeclosing`,
  `symmetric_competition_has_no_structural_choice`). When each of two courses
  secures one center's continuation and not the other's, both are
  non-foreclosing. No deterministic rule that must output a course and treats
  the centers alike can choose. This is the classic tie-symmetry argument. It
  says nothing against randomized or procedural tie-breaks, appeal to history,
  or further information about the centers. It does locate where those must
  enter.
- **Fulfillment can turn a retained course into a foreclosure**
  (`fulfillment_turns_retained_course_foreclosing`). In one stipulated example,
  acting on a claim and abstaining are both non-foreclosing while the claim is
  open. Once the claim is fulfilled it is no longer reached. Continuing to act
  then needlessly forecloses another center's continuation. A disposition that
  persists after its ground is met is a needless foreclosure, not neutral
  loyalty.

## 3. What this establishes

The previous two rounds showed which inquiry answers a challenged relation and
when that answer has a role. This round gives the **minimal structural
standard** for what a choice must count and avoid:

1. Count every continuation the choice actually reaches, whoever bears it.
2. Never take a course another available course improves on.

The first is derived from reach, not from a supplied circle of concern.
Narrower scopes provably mislead. The second is always satisfiable. Together
they are the strongest constraint that follows from the structure of a choice
without weighing continuations against each other. Beyond them, the
symmetric-competition theorem marks the point where structure runs out.

**中文表述（AI 撰写）：** 一个选择所必须计入的延续，就是该选择实际触及的那些——不论属于
自身还是他者；只计其中一部分，判断会在两个方向上都出错。不选取另一可行方案能全面改进的
方案，这一底线总是可以做到。超出这一底线，若两个中心的延续对称地相互竞争，仅凭结构的
确定性规则无法作出选择：此时需要关于各方的进一步事实与评价，或公正的程序（轮换、抽签、
协商）。

## 4. What remains open

- **Supplied inputs.** Courses, the continuation list and the secures relation
  are supplied. Reach filters the list; it never adds a continuation the list
  left out. Learning whose continuations a choice reaches is an inquiry
  problem, and the earlier inquiry results apply to it. It is not solved here.
- **Weighing.** Improvement is all-or-nothing inclusion, with no magnitude,
  likelihood or burden. Choosing among non-foreclosing courses needs an
  evaluation of the affected lives and claims, as the
  [whole-process account](WHOLE-PROCESS-GROUNDING-INTEGRATION.md) requires.
  It may also need a legitimate procedure.
- **Requirement 2.** This round supplies a scope condition and the
  withdrawal pattern in a toy case. It does not show how another center's
  consequences come to enter an organization's evaluation, beyond the
  previous round's point that access or coupling is needed. Nor does it show
  why such reasons survive scrutiny. Fulfillment-sensitive withdrawal in the
  acquired evaluator remains unimplemented; that is the next round.
- **Requirement 5.** The tie-symmetry result shows that standing, consent or
  authority must come from somewhere other than the structure of the choice.
  It supplies none of them, and it provides no recourse.

## 5. Independent review

A separate AI reviewer recompiled the module and tested variants. It accepted
the definitions as faithful and required five corrections, all applied:

1. "read off the situation, not supplied" became "derived from the supplied
   courses and secures relation".
2. The omitted-scope result is stated as one constructed witness, and a second
   theorem shows that omission can also condemn.
3. The symmetric result now states that the rule must output a course and
   that the proof uses only the fixed point.
4. The fulfillment theorem is called a single stipulated example.
5. The module states that restriction only filters the supplied list.

The reviewer also noted that `unreached_never_matters` is close to
definitional and that `nonforeclosing_exists` is the standard finite-maximum
fact. This note presents both as such.
