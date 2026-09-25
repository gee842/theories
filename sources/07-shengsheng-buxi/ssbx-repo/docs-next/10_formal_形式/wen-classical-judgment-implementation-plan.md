# Wen Classical Judgment implementation plan

> Status: superseded implementation plan.
> Date: 2026-05-19.
> Superseded: use `wen-to-r-code-frontend-plan.md` as the canonical plan.
> Scope: replace the current `ClassicalJudgment.lean` prototype with a real
> typed classical-judgment adapter for active Wen, plus a language-independent
> R judgment request layer.  This is not a legacy WenSurface/WenDef revival.
> Terminology update: read "R judgment request layer" below as the `Judgment`
> claim sublayer inside the wider `R.Awareness` report boundary. Wen compiles
> to `R.Code` and renders `R.Awareness`; it does not own truth semantics.

## Problem

The current `formal/SSBX/Foundation/Wen/ClassicalJudgment.lean` is not a real
implementation.  It is a token-pattern dispatcher:

```text
tokens -> match a few strings -> concatenate "(judge-over ...)" text
```

That is useful only as a smoke harness.  It repeats the same mistake as the
first Daodejing demo: structure is being smuggled into ad hoc surface
conventions instead of represented as typed syntax, typed context, and typed
elaboration.

The next implementation must not add more string-pattern cases.  It must
replace that layer.

## Final Goal

The goal is an ordinary `.wen` file that behaves like a small formal theory:
definitions extend a typed context, statements are elaborated against that
context, and every statement receives a judgment state.

```text
.wen document
-> language-specific source context
-> language-independent R.Code module
-> statement analyses
-> proof / refutation / overclaim / underdetermination / needs-law / unknown
```

This is not a special Daodejing mode.  A Daodejing chapter is just a demanding
test case because it mixes names, scope shifts, derivations, and claims that
require extra laws.  The same runner should also analyze any other Wen text
using the same statement ledger.

It is also not the final exclusive language.  Wen/Classical is the first
frontend.  Future frontends may be mathematical notation, English-ish
controlled prose, JSON/sexp tooling, or another historical language.  They
should all compile into the same R-core code layer:

```text
Wen / Classical source
Other controlled language source
Machine-facing source
-> R.Code
-> R.Judgment / R.Scope
-> statement analysis
```

The practical finish line is not "the machine understands all prose."  It is:
for every supported statement form, the system can say exactly what formal
content was obtained, what authority judged it, what scope it used, and what is
missing if judgment cannot be completed.

## Design Rule

The adapter boundary is document-level, not a special judgment mode:

```text
Wen document
-> Classical.Syntax commands
-> Classical source context
-> language-independent R.Code terms/claims/dynamics/laws
-> R.Judgment / R.Scope execution where possible
-> per-statement analysis ledger
```

The forbidden shortcut is:

```text
classical source line
-> hand-built native source string
```

Native source strings may still be produced at the final execution boundary,
but only after the sentence has been parsed into an AST and elaborated into an
explicit request.

The important direction is inward:

```text
Classical syntax is not the judge.
Wen is not the judge.
R tower judgment is the judge.
```

The Classical layer may introduce source names, derived terms, operators,
claims, and law assumptions, but every truth/scope/descent question must become
a language-independent R judgment request before it is evaluated.

The evaluator never judges Chinese words directly.  It judges typed R-core
content.  A closed finite cell may normalise to a strict RWord, but that is not
the same as saying every glyph maps directly to an RWord:

```text
surface syntax
-> Context lookup / definitions / derivations
-> R.Code term, predicate, dynamic, scope, or law
-> judgment request
-> R judgment state
```

Direct `glyph -> RWord` as a default semantics is not the active design.  The
active design is `Wen document -> R.Code theory`; RWord is the normal
form for closed finite cells inside that theory.

If a surface term cannot be resolved to a typed R-core object, a law, or a
supported derivation, the result is `needs-law` or an elaboration error, not
false.

The normal runner should analyze every statement in a `.wen` file and produce
a judgment state.  It should not require a one-off Daodejing mode, and it
should not stop at the first unsupported line unless the caller asks for strict
failure.

## Non-Goals

- Do not change the `R` carrier, scope, or theorem semantics.  Planned
  `Foundation/R` additions are a language-independent `R.Code` surface for
  terms/operations/claims and a judgment request wrapper over existing
  R-word/scope machinery.
- Do not import `WenDef`, `WenSurface`, Yi, Hex, Bagua, or Atlas.
- Do not claim raw Classical Chinese understanding.
- Do not make `wen` a universal truth oracle.
- Do not add a broad grammar for the whole Daodejing.
- Do not make lexicons a mandatory direct glyph-to-RWord table.  Lexicons and
  document definitions bind source names into the typed context; closed finite
  cell bindings are only one binding kind.
- Do not bind derived claims such as `玄 = dsum 徼 妙` directly in the initial
  lexicon.
- Do not encode Daodejing sentence names as Lean constructor names such as
  `keFeiChang` or `wuYouMing`.  Constructors must name generic semantic
  roles, not text-specific phrases.

## File Plan

Replace the single prototype file with small modules:

```text
formal/SSBX/Foundation/R/Code.lean
formal/SSBX/Foundation/R/JudgmentRequest.lean
formal/SSBX/Foundation/Wen/Classical/Syntax.lean
formal/SSBX/Foundation/Wen/Classical/Context.lean
formal/SSBX/Foundation/Wen/Classical/Elab.lean
formal/SSBX/Foundation/Wen/Classical/Analysis.lean
formal/SSBX/Foundation/Wen/Classical/Runner.lean
```

`R/Code.lean` and `R/JudgmentRequest.lean` must remain language-independent:
no Chinese names, no Wen imports, no lexicon dependency.  `R.Code` is the
shared target for every source language.  `R.JudgmentRequest` is the executable
request surface for the existing `R.Judgment` / `R.Scope` theory.

Then keep:

```text
formal/SSBX/Foundation/Wen/ClassicalJudgment.lean
```

as a compatibility re-export or thin deprecated wrapper while callers move to
the new modules.

## Core Types

### R Code

`R.Code` is the language-independent "R(ox) code" layer.  Wen should compile
to it; future languages should compile to the same layer.

```lean
namespace SSBX.Foundation.R.Code

inductive Name where
  | anonymous
  | named (id : String)

inductive CoreOp where
  | append
  | takeLeft
  | takeRight
  | visible
  | residual
  | full
  | eq
  | not
  | and
  | or
  | compose
  | named (id : String)

inductive Part where
  | visible
  | residual
  | full

inductive Term where
  | cell (word : String)               -- checked finite RWord normal form
  | ref (word : String)                -- named full input, serialized as RWord
  | var (name : Name)
  | app (op : CoreOp) (args : List Term)

inductive Predicate where
  | eq (left right : Term)
  | scopedEq (subject : Term) (side : Part) (target : Term)
  | app (name : Name) (args : List Term)

inductive Command where
  | defTerm (name : Name) (term : Term)
  | defPredicate (name : Name) (pred : Predicate)
  | assert (claim : Predicate)
  | assumeLaw (name : Name) (claim : Predicate)

structure Module where
  commands : List Command

end SSBX.Foundation.R.Code
```

This sketch should be refined during implementation, but the boundary is not
optional: source languages compile to `R.Code`; `R.Code` compiles to
`R.JudgmentRequest` or a theorem obligation where executable judgment is not
yet available.

Operations are part of this same core layer.  A source token such as a Wen
glyph, an ASCII operator, or a future mathematical symbol may alias
`R.Code.CoreOp.append`, `takeLeft`, a named dynamic, or a theorem-backed law.
The operator's rank signature, scope behavior, and descent facts belong to R
core, not to the source language.

### Atoms

Atoms are names from `.wen` lexicon or derived names in the context.

```lean
structure Atom where
  surface : String
```

Atoms do not by themselves imply a cell, reference, predicate, dynamic, scope,
or law.  That information lives in `Context`.

### Binding Targets

The context must be wider than a glyph-to-RWord map:

```lean
inductive BindingTarget where
  | cell (word : String)               -- closed finite RWord normal form
  | ref (word : String)                -- named full input, serialized as RWord
  | term (name : R.Code.Name)          -- elaborated R.Code term
  | predicate (name : R.Code.Name)     -- elaborated R.Code predicate
  | dynamic (name : R.Code.Name)       -- elaborated R dynamic/op handle
  | scope (name : R.Code.Name)         -- named observation/scope
  | law (name : R.Code.Name)           -- assumption or theorem handle
  | op (op : R.Code.CoreOp)            -- source operator alias
```

The first implementation may only execute the finite `.cell` / `.ref`
fragment, but the shape must leave room for ordinary Wen definitions,
operators, predicates, scopes, and laws.  Otherwise the architecture collapses
back to a static dictionary.

### Source Objects

```lean
inductive ObjRef where
  | surface (name : String)
  | cell (word : String)
  | ref (word : String)
```

Validation of `#word` / `@word` happens at parsing or context insertion.

### Classical AST

The Classical AST must be generic.  It should not contain constructors named
after Daodejing phrases.  Surface forms such as `句 可非常 ...` may parse into
the AST, but the AST names should describe reusable semantic roles.

```lean
inductive ScopeSide where
  | visible
  | residual
  | full

inductive ObservationHint where
  | infer
  | prefix (visibleRank : Nat)
  | full
  | sameAs (claimName : String)

inductive Predicate where
  | partEq
      (subject : ObjRef)
      (side : ScopeSide)
      (target : ObjRef)
  | dsumEq
      (left right result : ObjRef)
  | distinct
      (left right : ObjRef)
  | needsLaw
      (lawName : String)
      (about : List ObjRef)

structure Claim where
  name : Option String
  predicate : Predicate
  observe : ObservationHint := .infer

inductive Derivation where
  | bindDsum
      (left right : ObjRef)
      (result : Atom)
  | bindRef
      (target : ObjRef)
      (result : Atom)

inductive Sentence where
  | assert
      (claim : Claim)
  | contrast
      (available unavailable : Claim)
  | derive
      (derivation : Derivation)
      (checks : List Claim)
  | sequence
      (parts : List Sentence)
  | unsupported
      (raw : String)
```

This AST is still small, but it is real: downstream code pattern matches
semantic constructors, not arbitrary token sequences.

Examples:

```text
句 可非常 所道 可道 道體
```

parses to a `Sentence.sequence` containing generic `Claim` values with
inferred observation hints:

```text
visible equality: 所道 visible= 可道, infer scope from rank 可道
full equality:    所道 full= 道體, observed at the same visible scope
full equality:    所道 full= 道體 at full scope
```

It does not parse to a constructor named after the phrase `可非常`.

### Context

There are two contexts:

```text
Classical.Context
  source names, local notation, line origins, and frontend diagnostics

R.Code.Module / R.Code context
  language-independent terms, predicates, operations, scopes, laws, and claims
```

`Classical.Context` is an adapter-side overlay.  It may remember that a Wen
surface token came from `名`, `謂之`, or a source line, but it should not be the
semantic home of a term.  The semantic home is the emitted `R.Code` command.

```lean
structure Binding where
  surface : String
  target : BindingTarget
  origin : Origin

inductive Origin where
  | lexicon
  | derivedBySentence (lineNo : Nat) (rule : RuleName)
  | lawAssumption (name : String)

structure Context where
  bindings : List Binding
  laws : List LawDecl
```

Rules:

- Initial `名` lines create `.lexicon` bindings only.
- `謂之` creates `.derivedBySentence` bindings.
- A later sentence may use a derived binding.
- Rebinding an existing surface name is an error unless the target is
  definitionally identical and the file explicitly marks it as repeated.

### R-kernel Requests

Elaboration must not return raw strings.  It returns language-independent
R-kernel request values plus context updates.  These request values belong in
`Foundation/R`, not in Wen.

```lean
namespace SSBX.Foundation.R

inductive ScopeRequest where
  | full
  | prefix (visibleRank : Nat)

inductive PredicateRequest where
  | fullEq
      (subject target : String)       -- checked strict RWord strings
  | visibleEq
      (subject target : String)
      (visibleRank : Nat)
  | residualEq
      (subject target : String)
      (visibleRank : Nat)
  | dsumEq
      (left right result : String)
  | distinct
      (left right : String)

structure JudgmentRequest where
  scope : ScopeRequest
  predicate : PredicateRequest

end SSBX.Foundation.R
```

Context updates are separate:

```lean
inductive ContextUpdate where
  | deriveCell
      (surface : String)
      (word : String)
      (origin : Origin)
  | deriveRef
      (surface : String)
      (word : String)
      (origin : Origin)
  | needsLaw
      (message : String)
```

Only the R request runner evaluates `JudgmentRequest`.  Wen may render the
result, but Wen should not decide the judgment.

The R request runner must validate every `String` payload through `RWord` before
execution.  These are strings only as a concrete serialization of `ox` words;
they are not surface-language tokens.

This finite request surface is the first executable fragment, not the whole
future R-core IR.  As more Wen definitions become active, `JudgmentRequest`
should grow by adding typed R-core term/predicate/dynamic references, not by
adding new glyph-specific cases.

### Statement Analysis

The document runner should treat every judgment-bearing sentence as producing a
statement record:

```lean
inductive JudgmentState where
  | proven
  | refuted
  | overclaims
  | underdetermined
  | needsLaw
  | unknown
  | nonDenoting
  | rankConflict
  | parseError
  | elaborationError

structure StatementAnalysis where
  lineNo : Nat
  source : String
  command : Sentence
  contextUpdates : List ContextUpdate
  requests : List SSBX.Foundation.R.JudgmentRequest
  state : JudgmentState
  diagnostics : List Diagnostic
```

`proven` here means "proved by the available R executable/theorem authority for
this statement", not "the prose text is philosophically proven."  `unknown` is
an honest successful diagnostic when the current fragment lacks a decision
procedure, fuel, or law.

## Parsing Plan

Keep the first grammar whitespace-based.  Do not pretend it parses raw
punctuated classical prose yet.

Accepted first-slice forms:

```text
原 <raw-text>

句 可非常 <object> <visibleClaim> <fullClaim> [前 <N>]
句 無有名 <object> <noName> <hasName> [前 <N>]
句 觀 <object> <subtle> <boundary> [前 <N>]
句 同出 <left> <right> 異名 <leftName> <rightName> 謂之 <result>
句 又玄 <base> <mark> 謂之 <result>
句 門 <object> <visible> <residual> [前 <N>]
```

`前 <N>` is an explicit disambiguation hint, not the normal path.  The
default elaboration path must infer the visible scope from resolved finite
cell ranks whenever there is a unique solution.

Parsing failures must produce structured errors:

```lean
inductive ParseError where
  | unknownForm
  | missingToken
  | invalidNat
  | invalidMarkedWord
```

No parser branch should execute a judgment or mutate the context.

## Elaboration Plan

Elaboration consumes:

```text
Context × Sentence
-> Context
   × List ContextUpdate
   × List SSBX.Foundation.R.JudgmentRequest
   × List Diagnostic
```

The clean design has three phases:

```text
Sentence
-> SemanticClaim graph
-> solved R requests
```

It must not do this:

```text
resolve surface token
-> immediately emit hand-selected R.visibleEq / R.fullEq calls
```

That shape is too local.  It makes every sentence constructor responsible for
scope arithmetic, and it forces phrases such as `可非常` to duplicate the same
prefix/full/residual logic.  The sentence layer should say what relation is
being claimed; the R request layer should decide how that relation is observed.

### Resolved Objects

All judgment-bearing objects are resolved before any judgment executes.  The
generic resolved object is typed; it is not always a cell:

```lean
structure Resolved where
  source : ObjRef
  target : BindingTarget
  origin : Origin
```

Closed finite cells then have a checked RWord view:

```lean
structure ResolvedCell where
  source : ObjRef
  word : String       -- checked strict RWord serialization
  rank : Nat
  origin : Origin
```

Resolution rules:

- `#word` resolves to a cell value at `word.length`;
- `@word` resolves to a named full input at `word.length`;
- surface atoms resolve through `Context`;
- operators, predicates, dynamics, scopes, and laws resolve to their typed
  binding targets, not to fake cells;
- unresolved atoms produce an elaboration error or `needs-law`;
- no Classical constructor may inspect Chinese names after this phase.

`#` and `@` are source roles, not kernel semantics.  After resolution the R
request layer receives only checked R-word payloads plus the predicate role
(`visible`, `residual`, `full`, `dsum`, `distinct`).  The final judgment runs
on `ox`; it does not run on glyphs, `#`, or `@`.

### Semantic Claim Graph

Claims should carry two independent pieces of intent:

1. the predicate being tested;
2. the observation scope at which that predicate is tested.

This separation matters.  A full equality predicate can be tested at full
scope, or it can be tested through a visible scope to detect overclaiming.
Those are different judgments over the same predicate.

The concrete syntax can reuse the `Predicate`, `ObservationHint`, and `Claim`
types from the AST.  If implementation needs a separate elaborated type, it
should be isomorphic to that triple: optional claim name, predicate, observation
hint.

The `ObservationHint.infer` default is important.  Most Classical lines should
not say `前 8`.  They should resolve their atoms to typed context objects,
then let the solver infer the only scope compatible with the executable finite
fragment.  `sameAs` is the generic way to express "test this second predicate
under the same observation as that first predicate"; it is not special to the
Daodejing.

### Scope Solver

The scope solver owns all rank and prefix reasoning.  It receives resolved
objects, predicate shape, and observation hints.  It returns either a solved
request or a diagnostic:

```lean
inductive SolvedScope where
  | full
  | prefix (visibleRank residualRank : Nat)
  | ambiguous (choices : List ScopeCandidate)
  | impossible (reason : String)
```

Inference policy:

- `Predicate.partEq subject .full target` requires
  `rank subject = rank target`.
- `Predicate.partEq subject .visible target` requires
  `rank target <= rank subject`; its natural inferred observation is prefix
  `rank target`.
- `Predicate.partEq subject .residual target` requires
  `rank target <= rank subject`; its natural inferred observation is prefix
  `rank subject - rank target`, because the target names the residual part.
- `ObservationHint.full` forces full observation after predicate ranks are
  valid.
- `ObservationHint.sameAs name` reuses the solved scope of a previous named
  claim; if that claim has not solved uniquely, this claim is also blocked.
- explicit `前 N` must agree with the ranks required by the predicate side and
  target; disagreement is a rank/scope error, not false.
- if multiple scopes are valid because the target is not rank-informative
  enough, report `ambiguous-scope` and ask for `前 N`.
- if no scope is valid, report `impossible-scope`.

This is where the design stays honest: the system tries automatic judgment
first, but it does not guess when the R tower does not determine a unique
scope.

### R Request Compilation

Only after scope solving may the elaborator produce R-kernel requests:

```text
Predicate.partEq subject visible target, observe infer
-> resolved subject : R M
-> resolved target  : R V
-> solved prefix V
-> R.visibleEq subject-word target-word prefix V

Predicate.partEq subject residual target, observe infer
-> resolved subject : R M
-> resolved target  : R K
-> solved prefix (M - K)
-> R.residualEq subject-word target-word prefix (M - K)

Predicate.partEq subject full target, observe full
-> resolved subject : R M
-> resolved target  : R M
-> solved full
-> R.fullEq subject-word target-word

Predicate.partEq subject full target, observe sameAs visible-claim
-> resolved subject : R M
-> resolved target  : R M
-> solved prefix V from visible-claim
-> R.fullEq subject-word target-word prefix V
```

Sentence elaborators must not emit `R.visibleEq` or `R.fullEq` directly.  They
emit `SemanticClaim`s, then the shared compiler produces R requests.  That is
the difference between an adapter and another string macro.

### `可非常`

Input:

```text
句 可非常 所道 可道 道體
```

Semantic claims:

```text
claim visible:
  predicate = 所道 visible= 可道
  observe   = infer

claim overclaim-test:
  predicate = 所道 full= 道體
  observe   = sameAs visible

claim full:
  predicate = 所道 full= 道體
  observe   = full
```

If `rank 所道 = M`, `rank 可道 = V`, and `rank 道體 = M`, the solver derives:

```text
R.visibleEq 所道-word 可道-word prefix V
R.fullEq    所道-word 道體-word prefix V
R.fullEq    所道-word 道體-word full
```

The shared visible scope comes from `可道`'s rank, not from a hardcoded `前 8`.
An explicit form remains valid when disambiguation is needed:

```text
句 可非常 所道 可道 道體 前 8
```

but then `8` is checked against the resolved ranks.

Expected reports:

- visible claim descends;
- full claim overclaims at visible scope when residual rank is positive;
- full claim descends at full scope.

### `無有名`

Input:

```text
句 無有名 所道 無名 有名
```

Semantic claims:

```text
claim no-name:
  predicate = 所道 residual= 無名
  observe   = infer

claim has-name:
  predicate = 所道 visible= 有名
  observe   = infer

needsLaw 天地之始 / 萬物之母 relation if present
```

If `rank 所道 = M`, `rank 無名 = K`, and `rank 有名 = V`, the solver checks
`V + K = M` when both sides are meant to partition the same subject.  If that
partition does not hold, the sentence is a scope error or `needs-law`, not a
forced projection.

The first slice may ignore `始/母` in source, but the plan requires the next
slice to represent them as `needsLaw`, not comments.

### `觀`

Input:

```text
句 觀 所道 妙 徼
```

Semantic claims:

```text
claim subtle:
  predicate = 所道 residual= 妙
  observe   = infer

claim boundary:
  predicate = 所道 visible= 徼
  observe   = infer

needsLaw 欲 semantics
```

`欲` must not become a hardcoded moral truth value.  It is an observation
policy until an R-dynamic law is supplied.

### `同出 ... 謂之 ...`

Input:

```text
句 同出 徼 妙 異名 妙名 徼名 謂之 玄
```

Elaboration:

1. Resolve `徼` and `妙` to checked R-word cells.
2. Derive `玄` as `append 徼 妙`.
3. Insert derived binding:

   ```text
   玄 -> #<append word>
   origin := derivedBySentence lineNo 同出
   ```

4. Emit:

   ```text
   R.dsumEq   boundary-word subtle-word derived-word
   R.distinct subtle-name-word boundary-name-word
   ```

Important: `玄` must not exist in the initial `名` block.

### `又玄 ... 謂之 ...`

Same structure as `同出`, but the rule name is `又玄` and the result is the
next-layer derived cell.

### `門`

After `眾妙門` is derived:

```text
句 門 眾妙門 玄 玄標
```

Semantic claims:

```text
claim prior:
  predicate = 眾妙門 visible= 玄
  observe   = infer

claim marker:
  predicate = 眾妙門 residual= 玄標
  observe   = infer
```

Expected reports:

- visible prior layer descends;
- residual new layer overclaims at prefix scope.

## Runner Plan

Runner should process `.wen` files sequentially:

```text
initial empty Context
initial empty analysis ledger
for each line:
  comment/blank -> skip
  名 line       -> parse lexicon binding into Context
  原 line       -> store/display source reference only
  句 line       -> parse Sentence, elaborate, run R judgment where possible,
                  append StatementAnalysis
  判 line       -> parse explicit judgment, elaborate, run R judgment where
                  possible, append StatementAnalysis
```

The runner may temporarily reuse current `Wen.SourceJudgment` rendering helpers
while the R request runner is being introduced, but the target architecture is:

```text
Classical.Runner -> R.JudgmentRequest runner -> report
```

No new code should route a Classical sentence directly to a hand-built native
source string.

The whole-file output should be a ledger, not a single answer:

```text
file:
statements:
  line:
  source:
  context updates:
  resolved core:
  requests:
  state:
  diagnostics:
summary:
  proven:
  refuted:
  overclaims:
  underdetermined:
  needs-law:
  unknown:
  errors:
```

This is the path toward "a Wen text whose every statement has a judgment
state."  Some statements may be `needs-law` or `unknown`; that is still useful
analysis because it identifies exactly what is missing instead of pretending
the text has been judged.

## Output Requirements

Every emitted report should expose:

```text
line:
rule:
source sentence:
derived binding, if any:
request:
resolved ox:
rank:
scope: inferred | explicit | full | ambiguous | impossible
descent:
authority:
witness, if overclaims:
```

If a sentence is unsupported or needs a law:

```text
line:
rule:
status: needs-law
missing: <law name / relation>
```

This is a successful diagnostic, not false.

## First Real `.wen` Target

Replace:

```text
名
  #oooooooo 可道 可名 有名 徼
  #oxox 無名 妙
  #oooooooooxox 道體
```

with a staged file that has fewer initial whole-word claims.  The exact
surface notation below is illustrative; the implementation must route it
through AST, Context, and R requests:

```text
名
  #oooo 顯
  #oooo 界
  #ox 妙核
  #ox 名核
  #xo 徼名
  #xoxo 玄標

句 同出 顯 界 謂之 可道
句 同出 顯 界 謂之 可名
句 同出 顯 界 謂之 有名
句 同出 妙核 名核 謂之 無名
句 同出 妙核 名核 謂之 妙
句 同出 可道 妙 謂之 道體
句 指 道體 謂之 所道
```

Follow-on judgment lines should normally omit `前 N`:

```text
句 可非常 所道 可道 道體
句 無有名 所道 無名 有名
句 觀 所道 妙 徼
```

If the words in context do not determine a unique scope, the runner should
report `ambiguous-scope`; the user may then add `前 N` as a checked
disambiguation.  Explicit scope is a repair for ambiguity, not the default
language.

This syntax is illustrative.  Do not implement it as another string macro.
Implement it only after `Syntax`, `Context`, `Elab`, and `Runner` exist.

## Verification Plan

No full build.

Targeted Lean:

```text
lake build SSBX.Foundation.R.Code
lake build SSBX.Foundation.Wen.Classical.Syntax
lake build SSBX.Foundation.Wen.Classical.Context
lake build SSBX.Foundation.Wen.Classical.Elab
lake build SSBX.Foundation.Wen.Classical.Analysis
lake build SSBX.Foundation.Wen.Classical.Runner
lake build SSBX.Foundation.Wen.REPL wen
```

CLI smoke:

```text
wen --analyze-file formal/SSBX/Foundation/Wen/samples/daodejing-01-formal.wen
```

Static checks:

```text
rg "WenDef|WenSurface|Atlas|Bagua|Hex" formal/SSBX/Foundation/Wen/Classical -g '*.lean'
```

Expected: no matches.

## Acceptance Criteria

The next implementation is accepted only if:

1. `R.Code` exists as the language-independent target for Wen and future
   frontends.
2. `Classical.Syntax` defines an AST.
3. `Classical.Context` records initial versus derived bindings and supports
   typed targets beyond direct cell words.
4. `Classical.Elab` returns structured `R.Code` / request values, not native
   source strings.
5. `Classical.Elab` resolves surface atoms to typed R-core bindings before any
   judgment execution, and only demands checked RWords when compiling finite
   cell/ref requests.
6. Source operators resolve to `R.Code.CoreOp` / R-core dynamic handles; their
   rank and descent behavior is not implemented in the Wen layer.
7. Judgment execution happens through a language-independent R request runner.
8. `Classical.Runner` renders R reports; it does not decide truth itself.
9. `ObservationHint.infer` is attempted before requiring explicit `前 N`.
10. `ObservationHint.sameAs` lets one claim reuse another solved scope without
   hardcoding a number.
11. Ambiguous scope reports `ambiguous-scope`, not false and not a guessed
   prefix.
12. `Classical.Analysis` produces a per-statement ledger for a whole `.wen`
    document.
13. `玄` and `眾妙門` are derived by sentence execution, not initial lexicon.
14. At least one Daodejing line emits `needs-law`.
15. At least one Daodejing line emits `descends`.
16. At least one Daodejing line emits `overclaims` with witness.
17. The old `ClassicalJudgment.lean` prototype is either deleted or reduced to
   a compatibility re-export with a deprecation note.

## Stop Conditions

Stop and revise the plan if implementation starts doing any of these:

- matching entire sentence strings and concatenating report strings;
- adding more special cases directly to `REPL.lean`;
- putting derived conclusions into `名` bindings;
- forcing every source name to be a direct RWord binding;
- implementing operator rank/signature/descent behavior in the Wen adapter
  instead of R core;
- creating a Daodejing-only judgment mode instead of whole-Wen statement
  analysis;
- requiring `前 N` where ranks determine a unique scope;
- guessing a prefix when scope inference is ambiguous;
- treating `unknown` or `needs-law` as false;
- importing legacy language layers;
- claiming the Daodejing text itself has been proven.
