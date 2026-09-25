# Wen to R.Code frontend plan

> Status: canonical implementation plan.
> Date: 2026-05-19.
> Supersedes: `wen-classical-judgment-implementation-plan.md`.

> Implementation note: Stage 1 first slice is live in
> `formal/SSBX/Foundation/R/Code*.lean`; Stage 3/4 first slice is live in
> `formal/SSBX/Foundation/Wen/{ElabToRCode,Analysis,Runner}.lean`.
> Generic `判` sentences are now lowered to recursive `R.Code.Predicate`
> values; they are not evaluated by a Wen-side Boolean interpreter.
> Operator declarations now consult the R registry for both canonical ids and
> aliases such as `dsum -> append`.  Indexed projections are represented by
> `R.Code.Term.appAt`, so the rank parameter belongs to the R.Code term rather
> than to a Wen-side special case.
> The active frontend now uses `Wen.Binding`: source tokens first resolve as
> typed bindings (`term`, `op`, `predicate`, `predicateOp`, `logicOp`, `scope`,
> `law`, `dynamic`), then lower to `R.Code`.  Unknown terms are no longer
> silently accepted as variables.
> Architecture wording: Wen compiles to `R.Code` and renders `R.Awareness`.
> `Judgment` is the claim sublayer inside `R.Awareness`, not the whole report
> boundary.
> Core Closure boundary: supported executable operations lower to R.Code-side
> operator declarations/registry entries.  Wen performs supported source syntax
> parsing, typed binding, command lowering, and rendering only.  Trace closure
> records theorem-backed builtin structural effects for registry builtins and
> leaves opaque dynamic boundaries as `unknown` / `needs-law`.
> Active AST boundary: `.wen` source is parsed into
> `Wen.Classical.Module` / `Wen.Classical.Item`, then bridged through the
> `Wen.SourceModule` compatibility shape while the existing R.Code elaborator
> is reused.  The semantic boundary remains `R.Code` / `R.Awareness`; Classical
> owns only source structure, reading evidence, and provenance.

## Goal

`R` core is language-independent.  Wen is only the first frontend.  In this
Core Closure slice, Wen does not own active operations: it resolves surface
syntax through typed bindings, emits `R.Code` commands, and asks the R.Code
checker/registry for operator identity, rank behavior, finite normalization,
trace effects, and judgment status.

The target architecture is:

```text
Wen source line
-> Wen.Classical.Module / Item               -- active source AST
-> Wen.SourceModule / SourceCommand          -- compatibility lowering shim
-> Wen.Binding typed binding context
-> R.Code command(s)
-> R.Code checker / runtime / operator registry
-> R.Awareness
   -> Judgment claim sublayer + R.Scope loss/descent accounting
-> per-statement analysis ledger
```

Wen, future controlled English, mathematical notation, JSON/sexp tools, or any
other frontend must all compile to the same `R.Code`.  No source language owns
truth, scope, operator semantics, or descent.  Those belong to `Foundation/R`.
The rendered result is an `R.Awareness` report: a scope/loss/evidence account
with a `Judgment` claim state when the statement is a claim.

The practical finish line is a `.wen` file that behaves like a small formal
theory: definitions extend a context, operators compile to R-core operations,
claims compile to R-core predicates, and every statement receives a judgment
state:

```text
proven | refuted | overclaims | underdetermined | needs-law | unknown |
non-denoting | rank-conflict | parse-error | elaboration-error
```

## Concrete Pipeline

The first implemented slice uses this path:

```text
1. Source text
   句 同出 顯 妙 謂之 道體

2. Wen.Classical.Item
   Classify the line as a Classical AST item while preserving source span and
   textual provenance.  For executable command-style lines such as `句`, the
   item records the supported sentence shape without assigning operator
   semantics.

2b. Wen.SourceModule / SourceCommand
   The current elaborator still accepts a line-command normal form.  Classical
   lowering converts the item into that compatibility shape; new parsing work
   should target `Wen.Classical`, not grow `SourceModule`.

3. Wen typed binding context
   同出 -> OperatorId.append
   顯   -> R.Code.Name 顯
   妙   -> R.Code.Name 妙

4. Emit R.Code
   def 道體 := (append 顯 妙)

5. R.Code checker
   Look up append in the R-core operator registry:
   append : R N -> R K -> R (N + K)

6. Closed finite normalization
   If 顯 = #oooo and 妙 = #ox,
   道體 normalizes to #ooooox : R 6.

7. Claims lower to R.Code predicates
   判於 顯域 所道 顯 顯
   判於 顯域 所道 等 偽體
   emit visible/full-at-scope claims without phrase-specific macros.

8. Generic judgments lower the same way
   判 所道 等 道體
   判 非 所道 等 偽體
   判 所道 顯 顯 且 所道 餘 妙
   emit `eq`, `not`, `partEq`, and `and` predicates.

9. Projection definitions lower through R-core projection operators
   句 取前 4 所道 謂之 顯部
   句 取後 4 所道 謂之 餘部
   emit indexed `Term.appAt` projection applications.  `takeLeft 4` keeps the
   first four bits; `takeRight 4` drops the first four bits and keeps the
   residual suffix.

10. R.Awareness report
   The R-side scope solver and finite request evaluator produce
   proven/refuted/overclaims/etc. as the `Judgment` claim sublayer, together
   with scope, residual loss, and evidence metadata.

11. Statement ledger
   The whole file reports one judgment state per supported line.
```

The first CLI entry for this path is:

```bash
wen --analyze-file formal/SSBX/Foundation/Wen/samples/r-code-demo.wen
```

This is why operator aliases are separated from operator semantics.  Wen
surface tokens such as `同出` may point to `OperatorId.append`; alternate core
spellings such as `dsum` or `⊕` are aliases on the R registry declaration
rather than canonicalisation rules in the Wen adapter.  The rank rule,
normalizer, and descent facts stay in one R-core declaration.

## Non-Negotiable Boundary

Do not implement:

```text
Wen sentence -> hand-built native string
Wen glyph    -> mandatory RWord
Wen operator -> Wen-side evaluator
Wen phrase   -> phrase-specific Lean constructor
```

Implement:

```text
Wen sentence -> supported source item / future Wen AST -> R.Code command(s)
Wen glyph    -> source binding -> R.Code name / term / op / law
Wen operator -> alias of R-core OperatorId
Wen phrase   -> generic R.Code claim / definition / assumption shape
```

Closed finite cells may normalise to `RWord`, but `RWord` is not the only
meaning target.  A source name may denote a term, operator, predicate, dynamic,
scope, or law.

The active AST slice is now `Wen.Classical`: it preserves source spans, raw
text items, selected readings, role annotations, and the existing executable
declaration/judgment forms.  `Wen.SourceModule` remains a compatibility shim so
the R.Code elaborator does not need to be rewritten in one step.  Future work
can enrich `Wen.Classical.Clause` and sentence grouping without moving truth,
dynamic, operator, descent, or loss semantics out of `R.Code`.

## R.Code

Add `formal/SSBX/Foundation/R/Code.lean`.

The first version should be small but explicit:

```lean
namespace SSBX.Foundation.R.Code

structure Name where
  id : String

structure OperatorId where
  id : String

inductive Part where
  | visible
  | residual
  | full

inductive Observation where
  | infer
  | full
  | prefix (visibleRank : Nat)
  | sameAs (claim : Name)

inductive Term where
  | cell (word : String)        -- checked finite o/x word
  | input (word : String)       -- named full input, represented by o/x shape
  | var (name : Name)
  | app (op : OperatorId) (args : List Term)
  | appAt (op : OperatorId) (rankParam : Nat) (args : List Term)

inductive Predicate where
  | eq (left right : Term)
  | partEq (subject : Term) (part : Part) (target : Term)
  | app (op : OperatorId) (args : List Term)
  | not (p : Predicate)
  | and (p q : Predicate)
  | or (p q : Predicate)
  | implies (p q : Predicate)

structure Claim where
  label : Option Name
  predicate : Predicate
  observe : Observation := .infer

inductive Command where
  | defTerm (name : Name) (term : Term)
  | defPredicate (name : Name) (pred : Predicate)
  | assert (claim : Claim)
  | assumeLaw (name : Name) (pred : Predicate)

structure Module where
  commands : List Command

end SSBX.Foundation.R.Code
```

This is not the evaluator.  It is the shared core syntax that frontends emit.
The evaluator/checker is a separate layer over this syntax.

## Operator Relation To Core

Operators are not frontend functions.  They are R-core declarations.

Add `formal/SSBX/Foundation/R/Code/Operator.lean` or keep this namespace inside
`R.Code` for the first slice.

An operator declaration should have four pieces:

```lean
structure OperatorDecl where
  id : OperatorId
  kind : OperatorKind
  signature : RankSignature
  compile? : List CheckedTerm -> Except CompileError CheckedTerm
  judgmentLaws : List JudgmentLawRef
```

Where:

- `OperatorId` is language-independent, for example `append`, `takeLeft`,
  `takeRight`, `compose`, `eq`, or a namespaced theorem-backed operator.
- `OperatorKind` distinguishes term operator, predicate operator, dynamic, and
  scope transformer.
- `RankSignature` states rank constraints.  Examples:
  - `append : R N -> R K -> R (N + K)`
  - `takeLeft : R (N + K) -> R N`
  - `takeRight : R (N + K) -> R K`
  - `partEq visible : R (N + K) -> R N -> Prop`
  - `partEq residual : R (N + K) -> R K -> Prop`
- `compile?` performs executable lowering for the finite fragment.
- `judgmentLaws` records theorem handles such as descent, preservation, or
  information-use facts.

The source language only aliases tokens to `OperatorId`:

```text
Wen token 同出 -> OperatorId.append
registered ASCII token dsum -> OperatorId.append
registered math token ⊕ -> OperatorId.append
```

The signature, rank solving, evaluator, and descent facts remain exactly once
in `Foundation/R`.  If a source adapter needs to know operator semantics, it
should ask the R-core operator registry.

## Checking And Judgment

`R.Code` should have two stages:

```text
Raw R.Code
-> Checked R.Code
-> JudgmentRequest / theorem obligation / diagnostic
```

The checker owns:

- RWord validation for finite cells;
- rank inference and rank constraints;
- operator signature checking;
- normalization of closed finite cells;
- conversion of supported predicates into `R.JudgmentRequest`;
- emission of theorem obligations or `needs-law` when executable judgment is
  not available.

The judgment layer owns:

- truth and falsehood for denoting predicates;
- non-denoting versus false;
- scope and residual information;
- descent and overclaiming;
- underdetermination;
- authority labels such as `finite-enumeration`, `theorem`, `law`, `fuelled`,
  or `unknown`.

In the current architecture this is the `Judgment` claim sublayer of
`R.Awareness`.  The umbrella report also carries non-claim information such as
lossless direct-sum decomposition, projected residuals, and evidence labels.

The evidence boundary is intentionally strict:

| source of result | report status |
|---|---|
| named R/Lean theorem or registry effect marked `theoremBacked` | theorem-backed |
| registered law or operator effect recorded but not discharged | obligation / `needs-law` |
| bounded finite runtime check without a named soundness theorem | diagnostic |
| opaque dynamic, unsupported fragment, unbounded request, fuel/rank refusal | `unknown` |

Dynamic operators are R.Code/R.Awareness boundaries.  A Wen dynamic binding can
name a registry dynamic, but it does not simulate total behavior, prove
termination, or solve halting.  No frontend report should be read as a general
halting claim.

## Wen Frontend

Wen needs its own small stack, but it must stop before semantics:

```text
Wen.Classical.Module / Item
Wen.SourceModule / SourceCommand compatibility shim
Wen.Binding
Wen.ElabToRCode
Wen.AnalysisRunner
```

The current source compiler is `Wen.Classical`.  It gives each source item an
AST shape and source position sufficient for reading evidence, lowering, and
ledger reporting.  `Wen.SourceModule` is retained only as a compatibility shim
for the existing `ElabToRCode` adapter.  Neither layer is a Wen-side evaluator;
the semantics boundary remains `R.Code` and `R.Awareness`.

### Source Context

The Wen context maps surface tokens to typed source bindings.  The same
surface token may be reused across different kinds, but same-kind conflicts
are rejected:

```lean
inductive BindingTarget where
  | term (name : R.Code.Name)
  | op (id : R.Code.OperatorId)
  | predicate (name : R.Code.Name)
  | predicateOp (id : R.Code.OperatorId)
  | logicOp (id : R.Code.OperatorId)
  | scope (observe : R.Code.Observation)
  | law (name : R.Code.Name)
  | dynamic (id : R.Code.OperatorId)
```

For convenience, a finite cell binding may immediately emit a core term:

```text
名 #ox 妙 妙名
```

lowers to:

```text
R.Code.Command.defTerm 妙 (R.Code.Term.cell "ox")
R.Code.Command.defTerm 妙名 (R.Code.Term.cell "ox")
```

But that is only one binding form.  It must not become the model for all
meaning.

Current declaration forms:

```text
名 #word alias...          -- bind source terms and emit finite term defs
算 surface coreToken       -- bind a term operator alias via R registry
謂 surface P               -- bind a named predicate and emit defPredicate
域 surface 全              -- bind a full observation scope
域 surface 前 n            -- bind a prefix observation scope
域 surface 同 claim        -- bind a scope same as a prior labeled claim
律 surface P               -- record a law assumption
動 surface coreToken       -- reserved dynamic binding; requires dynamic operator
判於 surface P             -- judge P at a named scope
```

Dynamic bindings are boundary markers, not a runtime debugger.  A dynamic or
opaque operator may be named only if the R.Code registry accepts it; without a
law/theorem-backed structural effect it must render as `unknown` or
`needs-law`, not as a simulated halting or total-behavior fact.

Predicate relation words such as `等/同/異/顯/見/餘/隱/全` are default
`predicateOp` bindings to R-core predicate operators.  `異` is the derived
R-core predicate operator `ne := not (eq ...)`; it is not special-cased by the
Wen parser.  Logical words such as `非/且/或/則` are default `logicOp`
bindings to R-core logical combinators.  The parser only recognises prefix,
infix, and relation positions; operator identity and semantics come from
`Foundation/R/Code`.

### Operator Aliases

Wen must be able to bind operators as data:

```text
算 同出 dsum
算 取前 takeLeft
算 取後 takeRight
```

The exact surface keyword can change, but the semantics cannot: this creates a
source alias to an R-core `OperatorId`.  It does not define the operator.
The Wen adapter must resolve the core token by asking the R registry.  It must
not maintain a second canonicalisation table for spellings such as `dsum`.

A sentence using that operator:

```text
句 同出 顯 妙 謂之 道體
```

lowers to:

```text
R.Code.Command.defTerm
  道體
  (R.Code.Term.app OperatorId.append [顯, 妙])
```

Then the R.Code checker verifies `append`'s rank signature and normalises if
`顯` and `妙` are closed finite cells.

Projection sentence forms are reserved source syntax over the R-core
projection operators:

```text
句 取前 4 所道 謂之 顯部
句 取後 4 所道 謂之 餘部
```

The intended target is:

```text
R.Code.Command.defTerm 顯部 (R.Code.Term.appAt OperatorId.takeLeft 4 所道)
R.Code.Command.defTerm 餘部 (R.Code.Term.appAt OperatorId.takeRight 4 所道)
```

The implementation uses `Term.appAt` for indexed operators, so checker
diagnostics and normal forms are derived from the same R registry declaration.

### Claims

The old phrase-specific sketch:

```text
句 可非常 所道 可道 道體
```

is no longer active syntax.  It should be written as generic claims:

```text
assert visible:
  partEq 所道 visible 可道

assert overclaim-test:
  eq 所道 道體 observed at same scope as visible

assert full:
  eq 所道 道體 observed at full scope
```

The shared observation is a core scope relation, not a hardcoded `前 8`.
If ranks determine a unique scope, infer it.  If not, report
`ambiguous-scope` and let the source add an explicit scope hint.

The generic judgment sentence is the regular path for direct assertions:

```text
判 A 等 B          -- full equality, natural scope inferred
判 A 同 B          -- synonym for equality
判 A 異 B          -- negated equality
判 A 顯 B          -- visible/prefix equality
判 A 見 B          -- synonym for visible equality
判 A 餘 B          -- residual/suffix equality
判 A 隱 B          -- synonym for residual equality
判 A 全 B          -- explicit full-part equality
判 非 P
判 P 且 Q
判 P 或 Q
判 P 則 Q
判全 P
判前 N P
```

These forms lower through typed bindings: relation words become
`R.Code.Predicate.app` over registry-backed predicate operators, while logic
words are applied by R.Code helpers for `not`, `and`, `or`, and `implies`.
`判前`, `判全`, and `判於` only select the observation scope; they do not
change the predicate itself.  The R side still owns operator identity, rank
checking, natural scope inference, overclaim detection, and finite truth
evaluation.  A future Wen AST should preserve sentence structure, but it
should not own judgment semantics.

## Whole-File Compilation

The compiler should process a `.wen` file as a module:

```text
empty Wen.Context
empty R.Code.Module
empty StatementAnalysis ledger

for each source item:
  parse Wen source line as Wen.Classical.Item
  bridge to Wen.SourceModule / SourceCommand while ElabToRCode is reused
  update Wen.Context if it is a declaration
  emit R.Code.Command(s)
  check new commands against R.Code context
  run available R.Awareness / Judgment analyses
  append StatementAnalysis
```

Output is not one Boolean.  It is a ledger:

```text
line:
source:
emitted R.Code:
checked rank:
operator signatures used:
scope:
state:
authority:
diagnostics:
witnesses:
```

This is how an entire Wen text can be analyzed statement by statement without
pretending every line is decidable.

## Implementation Stages

### Stage 1: R.Code Core

Files:

```text
formal/SSBX/Foundation/R/Code.lean
formal/SSBX/Foundation/R/Code/Operator.lean
formal/SSBX/Foundation/R/Code/Check.lean
```

Build:

```text
lake build SSBX.Foundation.R.Code
```

Acceptance:

- no Wen, Atlas, Yi, Hex, Bagua imports;
- `Term`, `Predicate`, `Command`, `Module` exist;
- operator registry contains at least `append`, `takeLeft`, `takeRight`,
  `eq`, `visible`, `residual`, `full`;
- rank signatures are represented explicitly.

### Stage 2: R.Code Awareness / Judgment Bridge

Files:

```text
formal/SSBX/Foundation/R/JudgmentRequest.lean
formal/SSBX/Foundation/R/Code/Judgment.lean
```

Acceptance:

- checked finite predicates lower to `R.JudgmentRequest`, the current claim
  request surface inside `R.Awareness`;
- unsupported predicates become theorem obligations or `unknown`;
- false is distinct from non-denoting;
- scope inference and ambiguity are R-side diagnostics.

### Stage 3: Wen To R.Code

Files:

```text
formal/SSBX/Foundation/Wen/Source.lean
formal/SSBX/Foundation/Wen/Binding.lean
formal/SSBX/Foundation/Wen/ElabToRCode.lean
```

Acceptance:

- `.wen` declarations bind terms, operators, predicates, scopes, laws, and
  reserved dynamics into a typed Wen binding context;
- Wen emits `R.Code.Command`, not native strings;
- source operator aliases point to R-core `OperatorId`;
- unknown ordinary source terms are rejected instead of guessed as variables;
- no operator semantics are implemented in Wen.

### Stage 4: Whole-File Analysis

Files:

```text
formal/SSBX/Foundation/Wen/Analysis.lean
formal/SSBX/Foundation/Wen/Runner.lean
```

Acceptance:

- every supported statement produces `StatementAnalysis`;
- a `.wen` file produces a ledger and summary;
- `needs-law` and `unknown` are successful diagnostics;
- no Daodejing-specific execution mode exists.

## First Demonstration Target

Use a tiny `.wen` file that exercises definitions, operator aliasing, rank
checking, scope inference, full-scope awareness, projection loss, and
overclaim detection:

```text
算 同出 dsum
算 取前 takeLeft
算 取後 takeRight

名 #oooo 顯
名 #ox 妙
名 #oooooo 偽體

句 同出 顯 妙 謂之 道體
句 指 道體 謂之 所道
謂 同體 所道 等 道體
域 顯域 前 4
域 全域 全
句 取前 4 所道 謂之 顯部
句 取後 4 所道 謂之 餘部
判 同體
判於 全域 所道 等 道體
判於 顯域 所道 顯 顯
判於 顯域 所道 等 偽體
律 保顯 所道 顯 顯
判 顯部 等 顯
判 餘部 等 妙
```

Expected analysis:

- `同出` resolves to `OperatorId.append`;
- `道體` is emitted as `app append [顯, 妙]`;
- closed finite normalization derives the full word;
- `顯部` and `餘部` are emitted through the R projection operators
  `takeLeft` and `takeRight`, with their registry signatures surfaced in
  diagnostics;
- nested term construction is rendered as an R.Code term trace, so a chain like
  direct-sum followed by projection reports the first operation that discards a
  residual block;
- `同體` demonstrates named predicate binding and later `判` expansion;
- `全域` demonstrates lossless full-scope awareness, while `顯域` demonstrates
  a named prefix scope used by `判於`;
- `保顯` demonstrates law recording without claiming executable proof;
- `可非常` produces visible/full/overclaim claims;
- visible scope is inferred from `顯`'s rank;
- overclaim is reported at visible scope if residual rank is positive.
- generic `判` examples report true, false, negation, visible/residual
  matching, conjunction, disjunction, and implication through R.Code.
- direct sum itself is reported as lossless; residual loss appears when the
  analysis projects or restricts `所道` to `顯域` / prefix scope.  The trace
  distinguishes operation loss from mere scope focus: `dsum` preserves both
  components, while `takeLeft` / `takeRight` discard the complement unless an
  external law later supplies recovery.
- opaque dynamic boundaries are successful diagnostics only as `unknown` or
  `needs-law` until an R.Code registry declaration is backed by an explicit
  law/theorem.

This example is not the doctrine.  It is a compiler test.

## Stop Conditions

Stop and redesign if implementation does any of these:

- adds more sentence-string pattern matching;
- builds native source strings as the main target;
- puts operator evaluator logic in Wen;
- treats every source name as direct RWord;
- hardcodes Daodejing phrase constructors;
- requires explicit prefix when ranks determine a unique scope;
- guesses a scope when ranks do not determine one;
- imports Wen/Yi/Atlas into `Foundation/R`;
- reports timeout or unsupported recursion as false.
- presents the supported line parser as a complete Wen AST;
- presents trace closure as a runtime debugger, halting solution, or universal
  truth-decision procedure.
