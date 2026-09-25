# R.Awareness / Judgment / Wen Adapter Plan

> Status: first implementation slice is live. The runtime adapter and R-core
> vocabulary exist; theorem-backed checker soundness remains a later proof
> target and is not a ledgered doctrine claim.
> Scope: R-native awareness reporting and judgment accounting plus the active
> `Wen.Source -> Wen.Native.Expr n` adapter path and `.wen`
> `Wen.Classical` AST / `Wen.SourceModule` compatibility command path. No WenDef,
> WenSurface, Yi, Hex, Bagua, or rank-8 fallback is part of this plan.
> Core Closure boundary: `R.Awareness` is the report umbrella, `Judgment` is
> its claim sublayer, supported executable operations lower through typed
> bindings to R.Code operator declarations, and Wen only performs source
> structure recognition, syntax/binding/command lowering plus rendering.  The
> active `.wen` path is:
> `Wen source line -> Wen.Classical.Module / Item -> SourceCommand shim -> Wen.Binding ->
> R.Code command -> R.Code checker/runtime -> R.Awareness`.  A full Wen AST is
> now starting as the Classical AST; it does not move semantics into Wen.

## Goal

The next interpreter milestone is an awareness report boundary with three
pieces:

1. **R.Awareness umbrella**: owns the report shape for denotation, scope,
   residual loss, claim state, and evidence labels.
2. **Judgment claim sublayer**: owns held/failed propositions, predicates over
   R words, closed finite Bool answers, and descent/overclaim accounting.
3. **Wen Adapter**: lowers active Wen source into native finite R requests and
   renders the user-facing report.

This is not a Wen-owned truth oracle. Wen supplies source-command recognition,
syntax, lexicon bindings, source locations, command lowering, and display
authority labels; the awareness content is either closed finite native
evaluation, R-scope evidence, or a `Judgment` claim-state report over that
scope.  Operator signatures, judgment semantics, dynamic descent, scope loss,
overclaiming, and underdetermination are R.Code/R.Awareness responsibilities.

```text
Wen source line
-> Wen.Classical.Module / Item               -- active source AST
-> Wen.SourceModule / SourceCommand          -- compatibility command layer
-> Wen.Binding typed binding
-> R.Code command(s)
-> R.Code checker / runtime / operator registry
-> R.Awareness report
   -> Judgment claim sublayer where a claim/predicate is present
-> standardized report:
   source, lowered source, rank, truth/answer, scope, loss, descent status,
   authority/evidence
```

The important distinction is:

- closed judgment: a closed source expression evaluates to `Bool` at a concrete
  inferred or supplied finite rank;
- scoped judgment: a predicate is checked against an observation/scope, so the
  system can say whether the truth is well-defined after information is
  forgotten.

Both are needed. The first gives a finite closed Bool report. The second
connects the source-level request to the R-kernel theory in
`Foundation/R/Scope.lean`. Neither gives a universal truth oracle for arbitrary
programs, arbitrary prose, or unbounded formal systems.

Universal sayability is likewise not universal truth decidability.  It says an
adequate realisation can be expressed through the R substrate and supplied law
packages; it does not decide every claim expressible in that substrate.

## Current Baseline

Already implemented:

- `wen` evaluates active source through `Wen.Source -> Wen.Native`.
- `wen-kernel` evaluates direct native R-word/S-expression forms.
- `#ox...` and `@ox...` infer arbitrary rank from word length.
- `(dsum ...)` builds direct-sum R-words without compression to R8.
- `wen --scope <expr>` and REPL `:scope <expr>` display rank, direct-sum
  block chart, residual rank, and fiber size.
- Supported executable command items lower through typed bindings to R.Code
  operator ids/declarations; Wen aliases source tokens but does not implement
  operator semantics.
- R.Code term tracing reports builtin structural effects: direct-sum/append is
  operation-lossless, while `takeLeft` / `takeRight` projections create
  residual loss by discarding the complementary block.
- Opaque dynamic boundaries, predicate definitions, and law assumptions render
  as `unknown` / `needs-law` until a named R theorem or law discharges them.
- `Foundation/R/Scope.lean` defines and proves observations, observation
  equality, predicate descent, represented scoped predicates, scope
  refinement, operation descent, block-scope descent criteria, and exact
  residual/fiber loss for `R (N + K) -> R N`.

Missing:

- no ledgered theorem-backed checker soundness for runtime descent reports;
- no claim-status row marking any new universal judgment theorem as closed;
- no accepted path from arbitrary Wen/prose to R truth beyond the active source
  adapter;
- no user-facing wording that should be read as a universal truth oracle.

## Design Rules

1. `Wen.Native.Expr n` remains the only active runtime kernel for Wen source.
2. `R.Awareness` owns the abstract report boundary; its `Judgment` sublayer
   owns claim-state accounting. The Wen adapter owns parsing, lowering, source
   text, lowered text, lexicon use, and display.
3. Judgment is a claim sublayer over active source evaluation and R-scope
   theory, not a second evaluator and not the whole awareness layer.
4. Supported executable operations are R.Code-side declarations. Wen may bind
   syntax to operator ids and emit commands, but rank signatures, finite
   normalization, operation-loss traces, and judgment laws remain R-side.
5. `Wen.SourceJudgment` may import `Wen.Source`, `Wen.SourceScope`,
   `Foundation/R/Scope`, and `Foundation/R/Judgment`; it must not import
   legacy surface or Atlas modules.
6. A closed judgment is accepted only when evaluation returns `.bool b`.
7. A non-Bool result is not false; it is a type/shape error.
8. Scope descent is only claimed when there is an explicit predicate and an
   explicit observation. A closed Bool result by itself is not a descent
   certificate.
9. Runtime enumeration is bounded finite checking: explicit rank, explicit
   scope, supported predicate fragment, fuel/rank limits, and finite residual
   fibers. Unless a named Lean theorem connects the checker result to
   `R.Scope`, it is diagnostic evidence, not theorem status.
10. Trace closure is not a runtime debugger. It only records known builtin
   structural effects; opaque or dynamic boundaries remain `.unknown` /
   `.needs-law`.
11. Ancient-Chinese judgment syntax lowers into the same Wen adapter; it does
   not define kernel semantics.
12. Glyph meanings still enter only through `.wen` lexicon bindings.
13. No output should imply a universal truth oracle. Unsupported, unbounded, or
   theorem-unbacked cases must render as `.unknown`, diagnostic, or error.

## Implemented Lean Modules

```text
formal/SSBX/Foundation/R/Judgment.lean
formal/SSBX/Foundation/Wen/SourceJudgment.lean
formal/SSBX/Foundation/Wen/JudgmentSyntax.lean
```

`R/Judgment.lean` is the current `Judgment` claim sublayer. It packages
language-independent denotation, held propositions, scope-relative
necessity/possibility, predicate descent, and operation descent without knowing
Wen syntax.  The wider `R.Awareness` boundary is the architectural/report layer
that also includes scope, residual loss, and evidence labels.

`SourceJudgment.lean` is the Wen Adapter. It provides the source-native API,
uses active source evaluation, and renders `R.Awareness` reports with
source/lowered text, rank, answer, scope/loss, descent status, witness data,
and authority labels.

`JudgmentSyntax.lean` provides the first minimal ancient-Chinese judgment
lowerer. It is deliberately a source adapter, not a kernel semantics module.

## Core Data Model

```lean
namespace SSBX.Foundation.R.R

structure Denotation (Expr α : Type) where
  denote? : Expr -> Option α

def Sayable (D : Denotation Expr α) (e : Expr) : Prop :=
  ∃ a, D.denote? e = some a

def NonDenoting (D : Denotation Expr α) (e : Expr) : Prop :=
  D.denote? e = none

structure RJudgment (M V : Nat) where
  scope : RScope M V
  pred : R M -> Prop

namespace RJudgment

def TruthAt {M V : Nat} (J : RJudgment M V) (x : R M) : Prop :=
  J.pred x

def NecessaryAt {M V : Nat} (J : RJudgment M V) (y : R V) : Prop :=
  ∀ x, J.scope.observe x = y -> J.pred x

def PossibleAt {M V : Nat} (J : RJudgment M V) (y : R V) : Prop :=
  ∃ x, J.scope.observe x = y ∧ J.pred x

def Descends {M V : Nat} (J : RJudgment M V) : Prop :=
  J.scope.DescendsPred J.pred

end RJudgment
end SSBX.Foundation.R.R
```

The Wen adapter owns the runtime report:

```lean
namespace SSBX.Foundation.Wen.SourceJudgment

inductive Answer where
  | bool (value : Bool)
  | unknown (reason : String)
  | notApplicable

inductive Authority where
  | theorem
  | totalFragment
  | finiteEnumeration
  | fuelledRuntime
  | unknown

structure Report where
  source : String
  lowered : String
  rank : Nat
  answer : Answer
  scope : ScopeReport
  descent : DescentStatus
  authority : Authority
  witness? : Option Witness
  deriving DecidableEq, Repr

end SSBX.Foundation.Wen.SourceJudgment
```

The public report should separate answer text from display text. In this
discipline, `.finiteEnumeration` means bounded finite runtime enumeration. It is
diagnostic unless backed by named Lean theorem; only `.theorem` should be read
as theorem-backed.  A true closed answer is a claim result, not a certificate
that the same claim descends through a smaller scope.

## Public API

Closed judgment API:

```lean
def judgeClosedString :
  Nat -> String -> Except JudgmentError Report

def judgeClosedStringWithLexicon :
  Nat -> Lexicon -> String -> Except JudgmentError Report

def renderReport (report : Report) : String
def renderError (err : JudgmentError) : String
```

Behavior:

- `judgeClosedString fuel "(eq #ox #ox)"` succeeds with rank `2`, answer `true`.
- `judgeClosedString fuel "(eq #ox #xo)"` succeeds with rank `2`, answer `false`.
- `judgeClosedString fuel "#ox"` fails with `nonBoolResult`, because a cell is not
  a judgment.
- pure rankless Bool expressions should remain rejected in the inferred source
  path unless the API explicitly supplies a rank. This keeps rank inference
  honest.

Scoped judgment API:

```lean
inductive ScopeSpec where
  | full
  | prefix (visibleRank : Nat)

def judgeScopedString :
  Nat -> ScopeSpec -> String -> Except JudgmentError Report

def judgeScopedStringWithLexicon :
  Nat -> Lexicon -> ScopeSpec -> String -> Except JudgmentError Report
```

The first scoped implementation supports full scope and prefix/block residual
scope. Predicate descent is handled for the explicit `judge-over` predicate
fragment below. Evidence produced by enumeration remains diagnostic unless a
named Lean theorem later connects the executable checker to the denoted R
predicate.

## Predicate Descent Shape

For real descent, the judgment must be a predicate over a full R word:

```text
P : R (N + K) -> Bool
visible : R (N + K) -> R N
```

The R-kernel theorem says:

```text
DescendsPred visible P
iff
forall x y, visible x = visible y -> (P x <-> P y)
```

At the source level, v1 should support only explicit finite predicate forms,
not arbitrary higher-order native programs. This is the Wen adapter syntax for
constructing a `Judgment` request inside the `R.Awareness` boundary. A
practical first syntax is:

```text
(judge-over @input <bool-expr>)
```

where `@input` is a distinguished native name of rank `N + K`. In concrete
source this is usually an `@ox...` name whose word length fixes the full rank.
A scope request then specifies the visible projection.

Supported predicate forms in the current adapter:

```text
(native <Bool Native expr>)
(full-eq @name #word)
(visible-eq @name #word)
(residual-eq @name #word)
(not P)
(and P Q)
(or P Q)
```

The semantics should stay this simple:

1. bind a single full-rank input variable;
2. evaluate the Bool expression for every completion in each visible fiber;
3. if all completions agree, report `.descends`;
4. if two completions disagree, report `.overclaims` / `.underdetermined`
   with witnesses;
5. if the program cannot be enumerated within the supported fragment/fuel/rank
   bound, report `.unknown`.

This separation prevents a common mistake: a closed expression has a truth
value, but it is not automatically a theorem about all residual completions.

## Runtime Descent Checker

The finite runtime checker should be deliberately narrow and bounded. It is
currently exposed through `judgeScopedString` / `judgeScopedStringWithLexicon`,
not as a standalone theorem-producing checker:

```lean
def judgeScopedString :
  Nat -> ScopeSpec -> String -> Except JudgmentError Report
```

For `R (N + K) -> R N`, it enumerates:

```text
for every a : R N:
  evaluate P(slice a q) for every q : R K
  require all answers equal
```

The first version limits ranks for CLI responsiveness. If it refuses to
enumerate, it returns `.unknown`, not `.descends`. A successful enumeration may
justify a diagnostic report. It becomes theorem-backed only after a named Lean
theorem connects the checker to the denoted R predicate.

Lean soundness target:

```lean
theorem checkedBlockDescends_sound
  (h : executable scoped report says descends for P through blockScope N K) :
  (R.blockScope N K).DescendsPred (denote P)
```

This theorem may be a later proof target if the first implementation keeps the
checker as diagnostic. The document/status ledger must mark which state we are
in, and runtime output must not present diagnostic enumeration as theorem
status.

## CLI and REPL

Add to `formal/SSBX/Foundation/Wen/REPL.lean`:

```text
:judge <expr>
:j <expr>
wen --judge <expr>
```

Basic output:

```text
source: (eq #ox #ox)
rank: R 2
truth: true
scope: full, residual R 0, lossless
descent: not requested
```

Non-Bool output:

```text
wen judgment failed: expression evaluated to Cell 2, not Bool
```

Scoped output:

```text
source: ...
rank: R 12
answer: true
scope: visible R 8, residual R 4, fiber 2^4 = 16
descent: unknown, no predicate-over-input form supplied
```

After predicate descent is implemented:

```text
descent: descends through block 0
```

or:

```text
descent: depends on residual
witness A: #oooooooooooo -> true
witness B: #oooooooooxox -> false
```

CLI flags:

```text
wen --judge <expr>
wen --judge --full <expr>
wen --judge --prefix 8 <expr>
wen --lexicon path.wen --judge <expr>
wen --no-default-lexicon --judge <expr>
```

`--scope` remains a value/scope report. `--judge` is stricter: it requires a
Bool-valued result for closed reports, and an explicit predicate-over-input
form for scoped descent reports.

## Ancient-Chinese Judgment Grammar

This grammar should be active source syntax, not legacy WenSurface fallback.
It can be implemented in `Wen.JudgmentSyntax`.

Minimal v1 forms:

```text
判 <judgment>
判曰 <judgment>
<term> 等 <term>
<term> 同 <term>
非 <judgment>
<judgment> 且 <judgment>
<judgment> 或 <judgment>
若 <judgment> 则 <judgment>
```

Lowering:

```text
判 P              -> P
判曰 P            -> P
A 等 B            -> (eq A B)
A 同 B            -> (eq A B)
非 P              -> (if P false true)
P 且 Q            -> (if P Q false)
P 或 Q            -> (if P true Q)
若 P 则 Q          -> (if P Q true)
```

Important constraints:

- `A` and `B` must lower to same-rank native terms.
- `P` and `Q` must lower to Bool-valued judgments at the same inferred rank,
  unless an explicit fixed-rank API is used.
- The grammar keywords are logical syntax. They do not assign doctrine
  meanings to arbitrary glyphs.
- Terms such as `阳`, `阴`, `生`, `成`, or operator aliases come only from the
  active `.wen` lexicon.

Examples after this slice:

```text
wen --judge '#ox 等 #ox'
wen --judge '若 #ox 等 #ox 则 #xo 等 #xo'
wen --lexicon examples/r1.wen --judge '阳 等 阴'
```

## Relation to `R.Scope`

`R.Scope` is the formal mathematical layer:

```text
Observation X Y
ObsEq q x y
DescendsPred q P
ScopedPred q P
DescendsOp q r f
RScope.Finer fine coarse
```

`R.Judgment` is the claim sublayer:

```text
rank + predicate/closed Bool + observation
-> denotation / held proposition / descent question
```

`R.Awareness` is the wider report boundary that pairs that claim state with
scope, residual loss, and evidence:

```text
rank + denotation + observation + optional claim
-> answer / scope / loss / descent / evidence
```

`Wen.SourceJudgment` is the runtime/user adapter:

```text
source judgment
-> active source lowering/evaluation
-> R.Awareness request/report
-> rendered awareness report
```

The report must make the distinction visible:

| report field | meaning |
|---|---|
| `truth` | the closed judgment's current Bool result |
| `scope` | what visible part is being discussed and what residual exists |
| `descent` | whether the judgment is well-defined after forgetting residual data |
| `loss` | fiber size / residual rank / chart metadata loss |
| `authority` / `evidence` | theorem-backed, diagnostic enumeration, fuelled runtime, absent, or unknown |

Thus:

```text
truth = true
```

does not imply:

```text
descends through a smaller scope
```

That second claim requires a predicate-over-input check and, for theorem
status, a named Lean theorem. Runtime enumeration without that theorem remains
diagnostic.

## Relation to Universal Sayability

Universal sayability answers:

```text
Can this adequate realisation say the same R-core?
```

Awareness, via its Judgment sublayer and scope accounting, answers:

```text
When this realisation says a particular judgment,
which scope is it using,
what information is lost,
and does the truth descend through that loss?
```

Universal sayability is not universal truth decidability: an adequate
realisation may be able to say a claim in R without there being a total
decision procedure for that claim.  So `R.Awareness` plus the Wen Adapter should
sit between:

```text
Wen.Source / Wen.Native
```

and:

```text
R.Scope / T_GUT scope-aware boundary
```

It should not add new doctrine axioms. It exposes and audits the R-kernel
facts already present.

## Implementation Phases

### Phase 1 — Closed Bool Judgment

Files:

```text
formal/SSBX/Foundation/Wen/SourceJudgment.lean
formal/SSBX/Foundation/Wen/Interpreter.lean
formal/SSBX/Foundation/Wen/REPL.lean
docs-next/10_formal_形式/wen-judgment-system-plan.md
```

Deliver:

- `R.Awareness` report vocabulary, with `Judgment` denotation/descent vocabulary
  as the claim sublayer;
- Wen Adapter `Report`, `Answer`, `JudgmentError`, `DescentStatus`, and
  `Authority`.
- `judgeClosedString`.
- `judgeClosedStringWithLexicon`.
- `renderReport`.
- `wen --judge`.
- REPL `:judge` / `:j`.
- Non-Bool results rejected with clear diagnostics.

Targeted checks:

```text
lake build SSBX.Foundation.Wen.SourceJudgment
lake build SSBX.Foundation.Wen.REPL
lake build wen
```

Acceptance:

```text
lake exe wen --judge '(eq #ox #ox)'
lake exe wen --judge '(eq #ox #xo)'
lake exe wen --judge '#ox'       # clear non-Bool error
```

### Phase 2 — Scope-Aware Judgment Report

Deliver:

- integrate `Wen.SourceScope.Report`;
- add full/prefix scope request;
- display residual rank and fiber size in judgment output;
- keep descent `.notRequested` or `.unknown` unless a predicate form is
  supplied;
- mark runtime enumeration as diagnostic unless a named soundness theorem is
  attached.

Acceptance:

```text
lake exe wen --judge --prefix 8 '(judge-over @oooooooooooo (visible-eq @oooooooooooo #oooooooo))'
```

The output should say rank `R 12`, visible `R 8`, residual `R 4`, fiber size
`16`, and descent status for the explicit predicate request.

### Phase 3 — Predicate-Over-Input Descent

Deliver:

- `(judge-over @name P)` as a supported source form for one distinguished input
  cell;
- bounded enumeration over finite residual fibers;
- `.descends` / `.overclaims` / `.underdetermined` / `.unknown`;
- witness rendering for residual-dependent judgments.

Acceptance:

```text
wen --judge --prefix 8 '(judge-over @oooooooooooo (visible-eq @oooooooooooo #oooooooo))'
wen --judge --prefix 8 '(judge-over @oooooooooooo (residual-eq @oooooooooooo #oxox))'
```

The first examples should include:

- a predicate depending only on the visible prefix, which descends;
- a predicate depending on the residual suffix, which does not descend and
  returns witnesses.

### Phase 4 — Soundness Anchors

Deliver Lean statements connecting checked reports to `R.Scope`:

```lean
theorem closed_judgment_report_bool_sound ...
theorem checked_block_descends_sound ...
theorem checked_block_counterexample_sound ...
```

The exact theorem shape depends on how Native predicates are denoted. If the
runtime checker remains diagnostic, these theorem names must stay out of the
claim ledger until they are real; the ledger may mention the diagnostic feature
only as non-theorem runtime evidence.

### Phase 5 — Ancient-Chinese Judgment Syntax

Deliver:

- `Wen.JudgmentSyntax` parser/lowerer;
- `判`, `判曰`, `等`, `同`, `非`, `且`, `或`, `若...则...`;
- CLI and REPL route this syntax through `SourceJudgment`;
- no fallback to legacy WenSurface.

Acceptance:

```text
lake exe wen --judge '#ox 等 #ox'
lake exe wen --judge '若 #ox 等 #ox 则 #xo 等 #xo'
```

With custom lexicon:

```text
名 #o 阳 #x 阴
```

then:

```text
lake exe wen --lexicon path/to/lexicon.wen --judge '阳 等 阴'
```

must evaluate as a normal source judgment after lexicon lowering.

### Phase 6 — Documentation and Status Ledger

Deliver:

- update `v4-kernel-interpreter-architecture.md`;
- update `wen-language-roadmap.md`;
- update `r-scope-information-flow.md` if the implemented report changes the
  runtime boundary;
- update `claim-status-ledger.md` only for genuinely formalized theorem
  status, not for diagnostic CLI features. Diagnostic runtime features may be
  listed only as such.

## Non-Goals

- No full Wen AST in this slice.
- No WenDef fallback.
- No rank-8 default.
- No Yi/Hex/Bagua semantics.
- No automatic Chinese doctrine mapping.
- No claim that closed truth implies scoped descent.
- No universal truth oracle.
- No universal truth decidability.
- No runtime debugger.
- No halting solution.
- No unbounded runtime enumeration.
- No theorem status for diagnostic enumeration unless backed by a named Lean
  soundness theorem.
- No implicit mixed-rank promotion.
- No broad natural-language understanding. The ancient grammar slice is a
  small logical grammar, not a prose parser.

## Final Target

The intended user experience is:

```text
≫ :judge #ox 等 #ox
truth: true
rank: R 2
scope: full, residual R 0, lossless
descent: lossless

≫ :judge --prefix N <predicate-over-R(N+K)>
answer: true
scope: visible R N, residual R K, fiber 2^K
descent: descends / overclaims / underdetermined / unknown
```

At that point Wen will not merely evaluate expressions. It will adapt them into
`R.Code` and render an `R.Awareness` report for the exact R-scope in which the
judgment is complete, or state that the evidence is only diagnostic/unknown.
