# When a further inquiry has a role in what remains

6 October 2026. AI-authored continuation of the
[consequence → inquiry integration](CONSEQUENCE-INQUIRY-SELECTION-INTEGRATION.md),
taking up its stated next transition under the
[shared method](../../../../theories/shengsheng-buxi-generative-existence/unified-2026-10-05/NONDUAL-METHOD.md).
Named connection: **acquired consequence → answer to the challenged
application → role of that answer in surviving continuations, including
those of other centers**.

**Accepted scope.** One new Lean module,
[`InquiryWarrant.lean`](../../../../experiments/integrated-correction/general-framework/generative-basis/mathematical-abstraction/acquisition/feedback/remaining-dependency/formal/InquiryWarrant.lean),
imports the unchanged `InquiryRelevance` and its prerequisites. It adds 11
theorems and 16 definitions (27 audited declarations). No declaration uses
`sorry`, a custom axiom, `native_decide` or `Classical.choice`; the reported
dependencies are `propext` and `Quot.sound` only. The
[build record](../../../../experiments/integrated-correction/general-framework/generative-basis/mathematical-abstraction/acquisition/feedback/remaining-dependency/formal/inquiry-warrant/BUILD.md)
lists source hashes and the full audit output. No verified source was changed.
An [independent review](#7-independent-review) accepted the module with
corrections, which have been applied.

## 1. The question this round can and cannot answer

The prior round established that only a weak test at the setting actually
used answers whether that application's weak indication agreed with its
acquired full effect. It then observed that the packet is already gone:
answering the question does not show that anything remaining depends on the
answer, nor that the support the test consumes should be consumed on it.

That leaves two different questions:

1. **Role.** Given what survives the original opportunity, does the answer
   change what can adequately be done, and can it still be used once the
   test's own draw on shared conditions is carried forward?
2. **Warrant.** Given every continuation the test enables or forecloses,
   for this organization and for others, ought it to be done?

The first is a question about the structure of the unfolding and can be
settled by derivation and counterexample. The second is an evaluative question.
Lean can delimit it by showing which alternatives exist and what each
preserves or forecloses. It cannot supply the evaluation. This note
keeps the two apart throughout.

## 2. What is proved

A *continuation* records whose continuation it is (the inquiring organization's
or another center's), the relay setting it will rely on, the effect it relies
on there, which action is adequate when the weak indication agrees or does
not, and how much of the shared support it needs. The weak table remains
open over all four possibilities, as in the prior round.

**Decision role of a test (`inquiry_adequate_iff`).** After a faithful weak
test at `q`, some response policy acts adequately for every still-possible
table **exactly when** `q` is the setting the continuation relies on, or the
continuation's adequate action does not depend on the answer. The `→`
direction reuses the earlier off-target witness. For continuations whose
action depends on the answer, this decision role coincides with the earlier
epistemic sufficiency (`bearing_adequate_iff_sufficient`). The prior
relevance theorem is now joined to what is done next. It is no longer only a
fact about which test discriminates.

**Common adequate response (`abstention_adequate_iff`).** One action serves
without testing exactly when the answer does not bear on the continuation.

**When the test is needed (`inquiry_needed_iff`).** The test secures a
continuation that abstention cannot secure **exactly when** three conditions
hold: the continuation relies on the tested setting, its adequate action
depends on the answer, and its support requirement plus the test's own draw
fit within what is available. Each condition is derived from the semantic
definitions, rather than stipulated as the definition of need.

**After the original opportunity ends (`dominated_without_reliance`).** If no
surviving continuation relies on the tested setting, every continuation the
test secures is also secured without it, with no more support drawn. Under that
condition the test that uniquely answers the past application's question has
no role in what remains. Diagnosis of a completed operation acquires practical
standing only through a surviving reliance on the relation it diagnoses.

**Others' continuations (`needed_only_through_other`,
`self_needed_implies_needed`, `self_scoped_rule_ignores_others`).** In the
explicit witness, the organization's only surviving continuation relies on the
other setting. A self-scoped assessment therefore finds no role for the test
at the used setting. Another center's reliance on
the same setting gives the test a role. Restricting attention to self-borne
continuations can only remove roles, never add them. Any selection rule that
consults only self-borne continuations gives the same verdict however many
continuations of other centers are added. Others' consequences therefore
must reach such a rule through something beyond its self-scoped input:
further access, a coupling in its law, or an inherited link. The invariance
holds by construction; it is recorded as the inquiry-scope analogue, not a
derivation, of the unreached-extension result in the valuation-development study (on its own
branch, not imported here).

**Answering can remove the means (`answering_can_remove_the_means`).** With
one unit of support and a test drawing one, the test answers the question
but leaves too little to carry out the continuation. Abstention keeps the
support but cannot act adequately. Nothing secures that continuation. This
formalizes, for the present model, the earlier sufficiency account's warning
that informativeness is not adequacy.

**Differentiated continuations compete (`competing_continuations`).** With
three units, testing secures the organization's own reuse of the setting, and
abstaining secures another center's continuation that needs no answer but
more support. No joint course secures both. The model lists both courses and
what each forecloses. It does not rank them.

## 3. What this establishes for the foundation

The prior round showed that an actual consequence determines **which**
inquiry answers the challenged relation. This round shows **when** that
answer has a role in the unfolding after the original opportunity ends. The
answer has a role exactly where some surviving continuation, borne by this
organization or another, relies on the same relation, depends on the answer,
and can still be carried once the inquiry's own draw is counted. Inquiry,
continuation and consequence for others are related within one history. None
is added from outside through a scalar score. A selector's scope is also a
fact about that history: a self-scoped selector is invariant to others'
consequences by construction, not by any discovery about their importance.

**中文表述（AI 撰写）：** 先前的结果说明，后果决定了“问哪一个问题”才能回答被质疑的关系。
本轮说明的是：原先的机会结束之后，这个回答何时还在后续展开中起作用。只有当某个延续——
无论属于自身还是属于他者——仍然依赖同一关系，其恰当行动取决于这个回答，并且在计入追问
本身所耗的共同条件之后仍可实现，追问才有作用。只看自身延续的选择规则，对他者的后果
在结构上是不敏感的；他者的后果只能经由进一步的接触、耦合或继承而进入。至于在相互竞争的
延续之间“应当”如何取舍，这里只列出各自保全与排除了什么，并不作出判断。

## 4. What remains philosophical

The following are **not** established, and no Lean result here bears on them:

- **Which continuations count.** The list of surviving continuations, the
  marking of a center as "other", and the adequacy relation are supplied
  local inputs. The theorems hold for any such list; they do not derive the
  list from the generative account.
- **How to weigh competing continuations.** `competing_continuations` exhibits
  a choice where securing one center's continuation forecloses another's.
  Choosing between them needs an evaluation of the whole history's
  affected conditions and lives, as the
  [whole-process account](WHOLE-PROCESS-GROUNDING-INTEGRATION.md) requires.
  Persistence, successful correction or an organization's own preference does
  not supply it.
- **Why concern should extend to others at all.** The invariance theorem says
  how others' consequences can enter a selection rule. It does not say that
  they ought to. That they matter is a substantive ethical claim of the
  [unified ethical account](../../../../theories/shengsheng-buxi-generative-existence/unified-2026-10-05/UNIFIED-ETHICAL-GROUNDING.md).
  It is not proved here.
- **Whether the activity itself is worth continuing.** A role for inquiry is
  relative to continuations that are taken as given. A continuation whose
  worth is in question cannot confer warrant on the inquiry that serves it.

## 5. Scope conditions and revision conditions

- The test is faithful, and the weak table remains fully open for every
  continuation, including other centers', as in the prior round. Reliable weak
  facts or correlated tables could give an off-target test a role through
  inference. Such a family would change `inquiry_adequate_iff`.
- A continuation relies on one setting and one Boolean answer. Continuations
  whose adequate action depends on several relations need a product version.
  The single-relation result is the base case.
- Support is one shared natural-number summary of the conditions every listed
  continuation draws on, with additive draws. Separately renewed or
  non-rival conditions would remove the competition in
  `competing_continuations`. Renewal of support is the subject of the renewal
  roadmap and the three-phase-cycle work, not of this module.
- The relied-on effect is acquired only at the used setting. For a
  continuation at the other setting it is a supplied input. Each answer has
  exactly one adequate action; sets of adequate actions are not modelled.
- Abstention is modelled as drawing nothing and having no consequence of its
  own. This is a simplification, not a claim that abstaining is neutral; the
  [identification note](CONSEQUENCE-INQUIRY-SELECTION-IDENTIFICATION.md)
  rightly denies that any response is automatically neutral. Timing and order
  of use are not modelled.
- `other` is a label used only to filter. It carries no access, coupling or
  internal structure of the other center.
- "Adequate" is supplied per continuation. A continuation that is adequately
  carried out may still be harmful; the module does not say otherwise.

**Would change the account:** a surviving continuation that uses an answer
without relying on its relation, through some channel not represented here,
would defeat `dominated_without_reliance` for that history. A selection rule
that tracks others' consequences without any access or coupling would refute
the invariance reading. A further account showing that some continuations are
not worth sustaining would remove the warrant that their reliance gives the
inquiry.

## 6. Next transition

The open bridge is now narrower. It is no longer why inquiry is warranted
in general. It is how the list of continuations that count, and their
competing claims on shared conditions, are formed within the generative
history rather than supplied. Two existing lines bear directly on it. The
renewal roadmap, if it shows that a continuation renews rather than only
draws on its conditions, would relax competition in this model. The
valuation-development line, through access and coupling, explains how
others' continuations come to enter selection. Ethical warrant for a
particular choice among competing continuations remains a separate,
unfinished question. This round does not move it.

## 7. Independent review

A separate AI reviewer recompiled the module and audited it adversarially. It
judged the definitions faithful and non-vacuous: need cannot arise from support
failure alone, and the adequacy characterizations use real witnesses. It
required these corrections, all applied before this record:
"less support" became "no more support", since the draw may be zero; the
invariance docstring now says the result holds by construction and is an
analogue; the other-center witness now includes a surviving self-borne
continuation instead of an empty self list; and section 5 now states the
abstention, faithfulness, supplied-effect and labelling caveats. The parameter
`demand` was renamed `draw`. The reviewer also noted that the answer's role
comes from the supplied adequacy relation, which `AnswerBearing` restates
rather than derives; section 4 records this as a supplied input.
