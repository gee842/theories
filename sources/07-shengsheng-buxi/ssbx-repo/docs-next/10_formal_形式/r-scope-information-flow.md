# R Scope Information Flow

> Status: R-kernel theory layer, with Lean anchors
> [`Foundation/R/Scope.lean`](../../formal/SSBX/Foundation/R/Scope.lean)
> and
> [`Foundation/Doctrine/T_GUT.lean`](../../formal/SSBX/Foundation/Doctrine/T_GUT.lean).
> Scope: all-scale account of projection, slice coverage, information loss,
> predicate descent, operation descent, R.Code trace closure, scope order,
> law-mediated recovery,
> the `R.Awareness` umbrella boundary, its `Judgment` claim sublayer, evidence
> labels, and scope-relative truth.
> Glyphs and Chinese phrase readings enter only after these R facts are fixed.

## Claim

The R tower does not merely store `o/x` words.  It also tells us what a
chosen observation keeps, what it forgets, and which judgments remain valid
after that forgetting.

The kernel pattern is:

```text
full R word -> scoped observation -> fiber / residual
```

The direct-sum word is the full object.  Direct-sum/append is
operation-lossless: it puts both components into the full word rather than
discarding either component.  Loss begins only when an observation projects or
restricts that full object to a smaller scope.

For the canonical Bool/F2 realisation:

```text
R N := Fin N -> Bool
```

an element of `R N` is an `N`-bit information state.  A scope is an
observation of that state.  The first formal layer uses block projections:

```text
R (N + K)  ~=  R N x R K

visible  : R (N + K) -> R N
residual : R (N + K) -> R K
```

`visible` is what remains in the chosen scope.  `residual` is the information
that scope has not observed.

## Split, Slice, Fiber

The direct-sum equivalence gives the exact decomposition:

```text
R (N + K) ~= R N x R K
```

This equivalence is lossless: both components are still present, and changing
charts across the equivalence changes coordinates rather than discarding data.
Projection to either component is the lossy step, because the unobserved
component becomes residual fiber data.

For every residual label `q : R K`, there is a section:

```text
s_q : R N -> R (N + K)
s_q(a) = (a, q)
```

and a labeled slice:

```text
Slice(q) := image(s_q)
```

All labeled slices together are the full space:

```text
R (N + K) = disjoint_union_{q : R K} Slice(q)
```

Lean packages this as:

```text
R.slicesEquiv : R K x R N ~= R (N + K)
R.exists_slice_eq : forall w, exists q a, R.slice a q = w
```

The fiber over a visible value `a : R N` is:

```text
fiber(visible, a) := { w : R (N + K) | visible w = a }
```

and the kernel-level fact is:

```text
fiber(visible, a) ~= R K
|fiber(visible, a)| = 2^K
```

So the loss is not metaphorical.  It is exactly the residual component.

## Loss

If `K > 0`, the map:

```text
visible : R (N + K) -> R N
```

is not injective.  There are distinct full words with the same visible part.
Lean records this as:

```text
R.not_carrierRecoversResidual_of_pos
```

This is the formal reason that “只看一部分” lowers the valid scope of a
judgment.  The smaller view may be useful, but it does not contain the whole
state unless a separate law determines the residual.

The safe rule is:

```text
visible equality is not full equality
unless the residual rank is zero or a law determines the residual
```

## Coverage Versus Recovery

Keeping all labels is lossless.  Forgetting labels is projection loss.  Keeping
only some labels is incomplete coverage.

For `Q : Set (R K)`, define the covered subset:

```text
coveredBy(Q) := { w : R (N + K) | residual w in Q }
```

The exact coverage theorem is:

```text
coveredBy(Q) = univ  iff  Q = univ
```

Thus a missing label is addressable as a missing region, but the bare R carrier
does not invent the missing data.

The distinction is:

| situation | formal object | result |
|---|---|---|
| all labeled slices kept | all `q : R K` | full coverage |
| labels forgotten | `visible : R (N+K) -> R N` | fiber loss `R K` |
| some labels missing | `Q < univ` | partial coverage |
| missing label recovered | partial cover + extra law | law-mediated completion |

Recovery is stronger than coverage.  A law can recover the residual only if it
proves that equal visible observations force equal residual labels inside that
law.  Lean names this interface:

```text
R.LawDeterminesResidual P
R.full_eq_of_lawDeterminesResidual
```

Without such a law, recovery is not a theorem of the R carrier.

## Scope Objects and Order

The generic notion is an observation:

```text
Observation X Y := X -> Y
```

and an R-scope is the R-family instance:

```text
RScope N K := R N -> R K
```

Two full states are equal at a scope when the observation cannot distinguish
them:

```text
ObsEq q x y := q.observe x = q.observe y
```

Scopes are ordered by factorisation.  A scope `fine` is finer than `coarse`
when `coarse` can be computed from `fine`:

```text
RScope.Finer fine coarse :=
  exists h, forall x, coarse.observe x = h (fine.observe x)
```

Lean records reflexivity, transitivity, and the monotonicity of predicate
descent:

```text
RScope.finer_refl
RScope.finer_trans
RScope.descendsPred_of_finer
```

Thus "more complete scope" is not a metaphor.  It is the factorisation order
on observations.

## Odd and Even Boundaries

The same split explains every odd/even transition.

Even rank:

```text
R (2*n) ~= R n x R n
```

Odd rank:

```text
R (2*n + 1) ~= R (2*n) x R 1
```

The next even rank:

```text
R (2*n + 2) ~= R (2*n) x R 2
```

So an odd boundary is an even prefix plus one residual bit.  The following
even boundary is the same prefix plus a two-bit residual square.  Nothing in
this statement depends on a privileged small rank.

Lean anchors:

```text
R.evenSplitEquiv
R.oddResidualEquiv
R.nextEvenResidualEquiv
R.oddResidualFiber_card
R.nextEvenResidualFiber_card
```

This is the all-scale version of the intuition that a half-step can be useful
but is not naturally closed: its visible projection has a residual bit, and the
next even step lets that residual join a full two-bit label space.

## Completeness of a Judgment

A judgment is a predicate:

```text
P : R (N + K) -> Prop
```

It is valid at the visible scope only when it does not change inside visible
fibers:

```text
DescendsPred visible P :=
  forall x y,
    visible x = visible y ->
    (P x <-> P y)
```

Equivalently, `P` is saturated by the fiber relation.  If this fails, then the
judgment uses hidden information.  It may be true for one residual completion
and false for another.

For the canonical block scope, Lean proves the exact criterion:

```text
(blockScope N K).DescendsPred P
  iff
forall a q1 q2, P (slice a q1) <-> P (slice a q2)
```

So a judgment descends exactly when changing the residual label cannot change
the answer.

Scope-relative truth therefore has three readings:

| reading | definition | meaning |
|---|---|---|
| necessary at scope | all residual completions satisfy `P` | forced by visible data |
| possible at scope | some residual completion satisfies `P` | compatible with visible data |
| well-defined at scope | `P` descends through `visible` | residual cannot change the answer |

Proof and deterministic language should use the third reading.

## R.Awareness and Judgment

`R.Awareness` is the umbrella report/accounting layer.  It keeps together:

```text
denotation
scope / observation
visible and residual information
loss / fiber size
judgment state for claims
evidence / authority
```

`Judgment` is the claim sublayer inside that umbrella.  It handles predicates,
closed Bool values, truth/refutation, descent, overclaiming, and
underdetermination.  Scope and loss are not owned by `Judgment`; they come from
the R-scope theory and are rendered by the wider awareness report.

The claim sublayer is R-native.  Its inputs are:

```text
rank
closed Bool value or predicate over an R word
observation / scope
evidence source
```

and its outputs are:

```text
truth
scope / residual / fiber loss
descent status
evidence status
```

This keeps the ownership clean.  R scope theory owns descent, loss, and
well-definedness after projection; the `Judgment` sublayer owns claim-state
accounting over those scopes; `R.Awareness` is the report boundary that carries
both together.  A language adapter such as Wen may lower surface syntax into a
closed Bool report or a predicate-over-input request, but it does not create a
new truth semantics.

Evidence has to be explicit:

| evidence | status |
|---|---|
| named Lean theorem over `R.Scope` | theorem-backed |
| registry builtin with a named R structural theorem/law handle and `theoremBacked` effect status | theorem-backed structural effect for that builtin only |
| registered law/effect with no discharge theorem yet | obligation / `needs-law` |
| bounded finite runtime enumeration | diagnostic unless backed by named Lean theorem |
| unsupported fragment, fuel/rank refusal, or unbounded request | unknown |

Thus the active Wen `:judge` / `wen --judge` layer is an adapter to
`R.Awareness` through its `Judgment` sublayer.  It can report closed finite Bool
evaluation, exact residual/fiber loss, and bounded finite descent diagnostics.
It must not render an unbounded program check or arbitrary prose reading as a
universal truth oracle.  Dynamic reports follow the same rule: they can expose
whether a registered dynamic descends through a scope or remains
underdetermined/opaque, but they do not assert a general halting theorem.

## Operations and Descent

Operations must also respect scope.  An operation:

```text
f : R (N + K) -> R (N + K)
```

descends to the visible scope if there exists:

```text
g : R N -> R N
```

such that:

```text
visible (f x) = g (visible x)
```

for every `x`.  Equivalently:

```text
visible x = visible y -> visible (f x) = visible (f y)
```

If this fails, `f` uses residual information and cannot honestly be run at the
smaller scope.

For mask actions:

```text
T_m(x) = x + m
```

block projections behave cleanly:

```text
visible(T_m x) = T_(visible m)(visible x)
```

The residual part of `m` is not false; it is simply invisible at the chosen
scope.

Lean names the operation interface:

```text
DescendsOp q r f
RespectsScope q r f
```

and proves that descended operations respect fibers.  For surjective
observations, respecting fibers constructs the descended operation.  In the
block case, mask translation always descends:

```text
R.blockScope_mask_descends
```

## Charts Are Not Projection

A chart is a reversible way to read the same full R word:

```text
R (A + B) ~= R A x R B
R (B + A) ~= R B x R A
```

Changing chart preserves information.  It only changes coordinates.  The
formal map is an equivalence, not a projection.

Forgetting the chart is different.  A phrase-level object may carry:

```text
ChartExpr N := Sigma chart, chart.domain
address : ChartExpr N -> R N
```

The map `address` can forget chart, order, head/modifier focus, or other
metadata even when it preserves the full R address.  This is still an
observation theory:

```text
e1 ~=_address e2  iff  address e1 = address e2
```

but its fibers are phrase-structure fibers rather than vector-space cosets.

Thus there are two kinds of loss:

| loss kind | map | measurement |
|---|---|---|
| coordinate loss | `R (N+K) -> R N` | residual rank / fiber `R K` |
| chart/focus loss | `ChartExpr N -> R N` | chart metadata in the fiber |

Both are exact.  Neither should be inferred from glyphs.

## Language Alignment Layer

Glyphs enter after the R theory:

```text
glyph -> R word
phrase grammar -> charted R expression
chart transition -> R theorem
scope map -> information loss theorem
```

The lexicon never creates the law.  It only aligns a surface token with an R
word, R operation, or charted expression already defined elsewhere.

The first runtime boundary is now:

```text
Wen.Source -> Wen.SourceScope.Report
```

It is a report layer, not a second evaluator.  It runs through the same
rank-polymorphic `Wen.Source -> Wen.Native` path as `wen`, then records the
rank, rendered native value, and the direct-sum block chart that can be read
from explicit source syntax.  The CLI and REPL expose this as:

```text
wen --scope <expr>
:scope <expr>
```

For a phrase, the eventual full report should include:

```text
surface
chart
components
full address
chosen visible scope
lost residual / forgotten chart fields
equivalence level
```

The current Core Closure slice is intentionally narrower.  For direct R-source
forms it reports the full rank, whether the final scoped view is lossless at
full scope, and for the R.Code structural fragment it emits a bottom-up term
trace.  The active `.wen` analysis path is:

```text
Wen source line
-> Wen.Classical.Module / Item
-> Wen.SourceModule / SourceCommand compatibility shim
-> Wen.Binding typed binding
-> R.Code command(s)
-> R.Code checker / runtime / operator registry
-> R.Awareness report
```

`Wen.Classical` is the current source AST boundary.  `Wen.SourceModule` /
`SourceCommand` remains as a compatibility lowering shape for the existing
R.Code elaborator; it no longer owns parsing authority.  The AST remains above
the same lowering boundary and does not own judgment, dynamic, operator,
descent, or loss semantics.

Trace closure is limited to registry-backed R.Code builtins: it records
theorem-backed structural effects for the builtin direct-sum/projection
operators, reports `append` / `dsum` as operation-lossless, reports
`takeLeft` / `takeRight` as discarding the complementary residual block, and
keeps opaque dynamic or non-builtin boundaries as `unknown` / `needs-law`
until an explicit R law or theorem is supplied.  For each direct-sum or
projection block it reports:

```text
visible block rank
residual rank
fiber size 2^residual
operation-loss trace step
```

This makes the R-kernel loss facts visible at runtime without placing glyph or
phrase semantics in the kernel.

The awareness boundary extends this as:

```text
Wen.Source
-> Wen.SourceJudgment adapter
-> R.Awareness report with a Judgment claim state
```

Closed Bool results remain finite source evaluation.  Scoped descent remains an
R-scope claim.  Runtime enumeration over finite residual fibers is useful as a
diagnostic, but theorem status requires a named soundness theorem connecting
the checker result to the denoted R predicate.

Then two phrases can be compared without guessing:

```text
same full expression
same after chart equivalence
same after projection
same only after forgetting chart/focus
not same
```

## Relation to Universal Sayability

Universal sayability proves that formal realisations can be transported into
the canonical R substrate at the appropriate carrier and law-package level.
The scope/loss theory answers a different question:

```text
when a realisation is expressed in R,
which observation is being used,
which residual data is hidden,
and which claims still descend through that observation?
```

So scope/loss is not an extra semantic overlay and not a replacement for
`T_GUT`.  It is the boundary accounting layer that makes “can say” precise
with respect to “what was kept” and “what was forgotten.”

In particular, universal sayability is not universal truth decidability.  It
says that an adequate realisation can be expressed/transported into the R-core
boundary with its supplied laws.  It does not decide every R-coded claim, every
Wen sentence, arbitrary prose, or unbounded program behavior.

The formal bridge is conservative.  `T_GUT` does not get new generators from
scope/loss.  Instead it exposes the R-kernel facts as a boundary package:

```text
TGUTRealisation.RScopeBoundary
TGUTRealisation.HasScopeCoherence
TGUTRealisation.ScopeAwareUniversalSayability
TGUTRealisation.universal_sayability_scope_aware_of_law_packages
```

The meaning is:

```text
CompleteUniversalSayability
  = the realisation can say the represented R-core and its supplied laws

ScopeAwareUniversalSayability
  = CompleteUniversalSayability plus exact accounting of scoped loss,
    coverage, descent, and law-mediated recovery
```

This is the intended boundary: universal sayability states adequacy of saying;
R-scope theory states whether a particular scoped saying is lossless, complete,
or dependent on hidden residual information; `R.Awareness` renders that
accounting, with `Judgment` only as the claim sublayer.

## Summary

```text
R tower tracks information at every rank.
Scopes are observations.
Scopes are ordered by observation factorisation.
Block projection creates residual fibers.
The lost information in R (N+K) -> R N is exactly R K.
All labeled slices preserve the full space.
Forgetting labels is projection loss.
Partial labels are incomplete coverage, not automatic recovery.
Recovery requires an additional law.
Odd rank R (2*n+1) has a one-bit residual.
The next even rank R (2*n+2) has a two-bit residual square.
Judgments and operations are valid at a scope only when they descend.
R.Awareness owns the report boundary; Judgment is its claim sublayer.
Wen source lines pass through SourceCommand, typed binding, and R.Code before
R.Awareness; Wen does not own truth, dynamics, or operator semantics.
Trace closure is builtin structural tracing, not a runtime debugger.
Opaque dynamics and missing laws remain unknown / needs-law.
T_GUT exposes these facts as the scope-aware boundary of universal sayability,
not as universal truth decidability.
Charts preserve information; forgetting charts can still lose phrase metadata.
Glyphs align to R facts; they do not create those facts.
```
