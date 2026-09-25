# Native Wen Interpreter Architecture

> Status: supersedes the old V4 kernel interpreter draft (2026-05-13)
> Lean anchor: `SSBX.Foundation.Wen.Interpreter`
> Core anchor: `SSBX.Foundation.Wen.Native`
> Scope: one public interpreter entrypoint over the rank-polymorphic native
> kernel `Layered.Vn/Rn`.

> 2026-05-18 update: this is now the **single-kernel policy**.  The project
> should not grow new interpreter strata.  `WenSurface`, `WenDef`, `RKernel`,
> `YiInstr`, `Bagua`, and `MetaInterp` are legacy adapters, historical
> compatibility lines, or proof targets; they are not peer kernels and not
> optional active semantics.  The direct runtime CLI is
> now `wen-kernel`; pure native `#ox...` / top-level `ox...` words infer
> their rank from word length and run as `Wen.Native.Expr n`.  `wen` is now
> the active `Wen.Source -> Wen.Native` CLI and deliberately has no automatic
> WenSurface / WenDef / Hex fallback.
>
> Current migration slice: `Wen.Interpreter` is the public import boundary,
> and `Wen.Native` carries only language-independent kernel data, including
> first-class `fix`, cell-tagged values, and native nominal tagged-data
> hosting (`Wen.Native.Nominal`).  WenSurface namespaces, classes, and typed
> unquote remain source adapters/lowering conveniences.

## Decision

The active Wen interpreter kernel is no longer rooted in the old V4 interpreter
spine.  It is a native, arbitrary-rank kernel.  `Expr n` is the kernel shape;
`Expr 8` is only a legacy compatibility target for old Hex/R8-shaped source
IR.  It is not the default kernel rank and not the default `wen` runtime path.

```text
SSBX.Foundation.Wen.Interpreter
-> Kernel facade / NativeReader / LegacyBoundary
-> Wen.Native.Expr n / Value n / Env n / GlobalEnv n / TopForm n
Layered.Rn n / Layered.Vn n
-> evalFuel / quote / universal eval
-> native nominal tagged-data hosting
-> backend contract
-> surface reader and program runner
-> Kleene target interfaces
```

The old V4 kernel modules remain available as compatibility and research
history, but they are not the active public interpreter API.  The same applies
to the older `WenDef` / `WenSurface` execution spine: it is now a legacy
adapter/proof line, not an automatic `wen` fallback.  Chinese glyph meanings
enter the active path through explicit `Wen.SourceLexicon` bindings over
R-words, not through implicit Hex/R8 projection.

## Native Kernel Modules

These are modules of one kernel, not doctrine strata.

| Module | Lean anchor | Role |
|---|---|---|
| public interpreter entry | `Wen.Interpreter` | canonical import for runtime work |
| kernel facade | `Wen.Interpreter.Kernel` | thin aliases and laws over `Wen.Native` |
| native text boundary | `Wen.Interpreter.NativeReader` | direct S-expression runner for `wen-kernel` |
| source scope report | `Wen.SourceScope` | runtime report of rank, direct-sum chart, residual rank, and fiber size |
| legacy ledger | `Wen.Interpreter.LegacyBoundary` | labels old lines as non-kernel adapters/proof targets |
| rank carrier | `Wen.Layered.VnRn` | `Rn n := BitSpace n`, `Vn n := BitSpace n` |
| syntax and values | `Wen.Native.Syntax` | `Expr n`, `Value n`, `Env n`, `GlobalEnv n`, `TopForm n` |
| evaluator | `Wen.Native.Eval` | fuelled eval with globals, closures, quote values, and `.eval` |
| nominal hosting | `Wen.Native.Nominal` | language-independent tagged records, constructor/catalogue/set shapes, and pattern-test lowering |
| code trees | `Wen.Native.Quote` | reference `CodeTree n`, encode/decode, value-level quote round trip |
| universal eval | `Wen.Native.Universal` | evaluates encoded native expressions and top forms |
| backend contract | `Wen.Native.Backend` | abstract representation contract plus `treeBackend` |
| surface | `Wen.Native.Surface` | cell-named surface forms to de Bruijn core expressions |
| reader | `Wen.Native.Reader` | S-expression boundary over native cells, with no YiInstr import |
| programs | `Wen.Native.Program` | top-form lists, surface programs, reader-backed programs |
| Kleene targets | `Wen.Native.Kleene` | `Halts`, `Computable`, universal/s-m-n/fixed-point/inverter targets |

## Design Rules

- Atomic program values are `Rn n` cells.
- Primitive layer operations are `Vn n`: `zero`, `xor`, `act`, cell `eq`, and
  slot `flip`; structural helpers include list primitives, Boolean equality,
  and safe data-tag tests.
- There is exactly one interpreter entrypoint: `Wen.Interpreter`; its executable
  core is `Wen.Native`.
- Direct R-tower words enter through `RWord` into `Sigma fun n => Expr n` /
  `Sigma fun n => Value n`; they do not pass through Hex, Bagua, Yi, or rank-8
  coercion.
- Surface languages lower into the kernel; they do not define semantics.
- `Wen.Native` includes first-class `fix`, cell-tagged data, and nominal
  tagged-data hosting because all three are language-independent kernel
  constructs.  Source adapters still own symbol interning: user constructor
  names, catalogue ids, and set/quote wrapper names must be assigned finite
  cell tags before entering Native.
- `Wen.Native` must not grow WenSurface-only conveniences.  Namespaces,
  classes, typed unquote, prose names, and glyph-specific behavior lower
  through adapters before entering the native kernel.
- `V4`, `Word64/R6`, `R8/Cell256`, and `RootCell256` are deprecated bridge
  adapters.  They live behind explicit imports such as `Wen.Native.Bridges`,
  not behind the active `Wen.Native` or `Wen.Interpreter` entrypoint.
- Core binding remains de Bruijn; surface names are cells that elaborate either
  to local variables or immutable global references.
- `define` is immutable at the Lean level: evaluation returns an extended
  `GlobalEnv`.
- Backend modules prove representation round trips; they do not redefine
  evaluation.
- Concrete carrier bridges are adapters only: they map existing carriers to
  native cells and prove native `.xor` agrees with the old carrier operation.
- Public witness names are semantic: `originCell`, `slotXorExpr`,
  `lambdaAddExpr`, `defineChain`, and module-level `*_laws` theorems state the
  small API contracts.

## Reader Surface

The direct `wen-kernel` reader accepts one S-expression top form:

```text
top     ::= (define name expr) | expr
expr    ::= nil | true | false | nat | prim | name | #bits
          | ()
          | (cell bits)
          | (dsum cell-part+)
          | (quote expr) | 'expr
          | (lambda param expr)
          | (fix name expr)
          | (if expr expr expr)
          | (data tag expr)
          | (flip nat expr)
          | (expr expr*)
name    ::= @bits | bits
param   ::= name | (name)
bits    ::= exactly n chars, each one of o x 0 1
cell-part ::= #bits | (cell bits) | @bits | bits
            | (xor cell-part cell-part)
            | (act cell-part cell-part)
            | (flip nat cell-part)
            | (dsum cell-part+)
prim    ::= zero | xor | act | eq | cell-eq | bool-eq | cons | car | cdr
          | null | null? | atom | atom? | bool? | number? | num?
          | data? | data-tag | data-fields | data-tag-eq
          | numEq | num-eq | num-le | <= | num-lt | <
          | succ | pred | add | + | eval
```

`#bits` is reserved for cell literals.  `@bits` is the explicit name spelling;
bare `bits` remains a compact name spelling inside compound forms.  In the
inferred-rank CLI/API, a whole input consisting of one bare `ox...` word is
treated as a cell literal.  Outside explicit `(dsum ...)`, all explicit word
tokens in one inferred-rank form must have the same length; mixed-rank compounds
fail instead of being promoted or squeezed into `R8`.  The reader does not
import YiInstr or the old V4 Lisp reader.

`(dsum ...)` is a static direct-sum lowering form.  Each cell-valued component
is parsed at its own rank, lifted into a disjoint slice of one total rank, and
lowered to an ordinary `Expr N`; `Expr`, `Value`, environments, quote/eval, and
the evaluator remain homogeneous.  For example, `(dsum #oooooooo #oxox)` lowers
to rank 12 with word `oooooooooxox`, and `(dsum #oooo #oooo #oxox)` is the same
total word.  In v1, `dsum` accepts only cell blocks (`#bits`, `(cell bits)`,
`@bits`/bare word refs, `xor`, `act`, `flip`, nested `dsum`).  Bool-valued `eq`
and rankless forms such as numbers, `cons`, `quote`, `eval`, lambdas, and
arbitrary apps are rejected as components.  Runtime heterogeneous expressions
are explicitly deferred.

The active `wen` CLI also exposes a scope report:

```text
wen --scope <expr>
```

and the REPL accepts `:scope <expr>`.  This report is implemented in
`Wen.SourceScope`, after ordinary source evaluation.  It does not define new
semantics; it displays the R-kernel accounting already proved in
`Foundation/R/Scope.lean`: full rank, explicit direct-sum blocks, residual
rank for each block projection, and the corresponding fiber size.

The active user-facing awareness layer is the Wen adapter for `R.Awareness`,
specified in [`wen-judgment-system-plan.md`](wen-judgment-system-plan.md).
It promotes Bool-valued source evaluation to `judgeClosedString`,
`wen --judge`, and REPL `:judge`, then connects scoped predicate requests to
the `Judgment` claim sublayer and `R.Scope.DescendsPred` without reintroducing
WenDef/WenSurface fallback or rank-8 defaults.  Wen owns syntax, lexicon
lowering, and rendering; it compiles to `R.Code` and renders `R.Awareness`.
R owns truth/descent/loss evidence.  Direct sum is lossless as a full R object;
projection or scope restriction is where residual loss appears.  Bounded
finite runtime enumeration is diagnostic unless a named Lean theorem backs the
checker, and no CLI path is a universal truth oracle.

The active `.wen` analysis path is now a Classical AST pipeline:

```text
Wen source line
-> Wen.Classical.Module / Item
-> Wen.SourceModule / SourceCommand compatibility shim
-> Wen.Binding typed binding
-> R.Code command(s)
-> R.Code checker / runtime / operator registry
-> R.Awareness report
```

`Wen.Classical` owns source structure, raw text, selected readings, role
annotations, and executable command items.  `Wen.SourceModule` / `SourceCommand`
is only a compatibility lowering shape for the existing elaborator.  The AST
must still lower to `R.Code`; judgment semantics, dynamic semantics, operator
signatures, operation-loss traces, descent, and overclaim/underdetermination
remain R.Code/R.Awareness responsibilities, not Wen responsibilities.

The certificate boundary is likewise R-side.  A registry effect or checker
result is theorem-backed only when it points to a named Lean/R theorem or a
registry effect marked `theoremBacked`.  Registered but undischarged effects
remain obligations and render as `needs-law`; opaque dynamics, unsupported
fragments, unbounded requests, or fuel/rank refusals render as `unknown`.
Dynamic runtime reports are scope/descent reports, not a general halting
claim.

## Suspended Lines

The old `Foundation/Wen/V4Kernel` and its Lisp-named modules are compatibility
and research material.  YiInstr and restored `MetaInterp` also remain separate
backend/proof lines.  `Wen.Interpreter` intentionally does not import heavy
legacy adapters; `Wen.Native` intentionally does not import those modules at
all.

The cleanup target is:

```text
external syntax / prose / S-expression
-> source adapter
-> namespace/class/type elaboration and typed-unquote lowering
-> Wen.Interpreter.Expr n / TopForm n
-> Wen.Native.evalFuelG
```

Anything that currently evaluates through `WenDefEval`, `RKernel.LispEval`,
`YiState.runFuel`, or `MetaInterp` should either lower to `Wen.Native`, become
a backend/proof target for `Wen.Native`, or move to a clearly labelled legacy
namespace.  WenDef's user constructors, catalogue wrappers, first-class
predicate sets, and flat match tests now have a native host shape in
`Wen.Native.Nominal`, and `Wen.Interpreter.Adapters.WenDef` contains the first
checked lowering pass for the low-risk subset: literals, named lambda/app,
Bool logic, cell equality, quote/eval, function-shaped fix, nominal
constructors, catalogue records, predicate sets, and flat matches.  The
adapter can derive a finite symbol table from one closed `WenDef.Tm`.  The
public `wen` path no longer calls this adapter automatically; the remaining
work is to give source-level glyph definitions and full WenSurface lowering a
rank-polymorphic path into `Wen.Source`, not to restore a WenDef fallback.

## Current Completion Boundary

This phase completes the public native spine:

```text
Expr n
-> evalFuel
-> Nominal tagged-data hosting
-> CodeTree n
-> universalEvalExpr
-> Backend n
-> SurfaceTopForm n / Reader
```

Deprecated concrete bridges still exist under `Wen.Native.Bridges.*` for
compatibility checks and historical proof targets, but they are outside this
completion boundary.

Native Kleene currently stops at target interfaces and target assembly:

```text
FixedPointExists n
-> BoolInverterCompilerExists n
-> NativeKleeneInverter n
```

It does not yet supply hard witnesses for the universal interpreter,
s-m-n compiler, fixed-point compiler, or Boolean inverter compiler.  Those are
future proof/implementation obligations, not axioms added to this phase.
