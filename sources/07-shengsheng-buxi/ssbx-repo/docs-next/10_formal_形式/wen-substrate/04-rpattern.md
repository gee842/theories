# 04 — RPattern / RWord substrate

> Current Lean status: the R core stays semantic-free.  Total words live in
> `RWord`; partial faces live in `RPattern`.  Yi / Wen / Chinese readings are
> downstream overlays, not definitions imported by `Foundation/R`.

The kernel carrier is still

```lean
R N := Fin N -> Bool
```

Two small bridges now cover the surface cases that used to be mixed together.

- [`Foundation/R/RWord.lean`](../../../formal/SSBX/Foundation/R/RWord.lean)
  parses and renders arbitrary finite `o`/`x` words as elements of `R N`,
  where `N` is the word length.
- [`Foundation/R/RPattern.lean`](../../../formal/SSBX/Foundation/R/RPattern.lean)
  defines partial bit patterns
  `RPattern N := Fin N -> Option Bool`, the face lattice of the `N`-cube.

The important rule is negative as much as positive: there is no kernel name
for "道" here.  `RPattern.empty` is the empty partial assignment, i.e. the
merge identity.  Reading that identity as 道 belongs to Atlas or a Wen-facing
explanation layer.

---

## RWord — arbitrary o/x rank

`RWord` is the strict parser / renderer for concrete bit words:

```lean
RWord.parseAt? 10 "oxoxoxoxox" : Option (R 10)
RWord.fromString? "oxoxoxoxox" : Option (Sigma fun N => R N)
RWord.render : R N -> String
```

Characters `o` / `0` parse as `false`; `x` / `1` parse as `true`.  Other
characters are rejected by the strict parser.  The word length is the rank, so
the interpreter no longer needs to force every literal into `R 8`:

| word | rank |
|---|---|
| `ox` | `R 2` |
| `oxox` | `R 4` |
| `oxoxoxox` | `R 8` |
| `oxoxoxoxox` | `R 10` |
| `oxoxoxoxoxox` | `R 12` |

The tower decomposition is direct-sum structure, not semantic convention.
For example:

```lean
RWord.split8_2 : R 10 ≃ R 8 × R 2
RWord.split8_4 : R 12 ≃ R 8 × R 4
RWord.split8_8 : R 16 ≃ R 8 × R 8
RWord.split4_4_4 : R 12 -> (R 4 × R 4) × R 4
```

Thus `R 10` can be read as `R 8 + R 2`, `R 12` can be read as either
`R 8 + R 4` or `R 4 + R 4 + R 4`, and both readings are just canonical
splittings of the same total word.  No rank is pushed back into `R 8`.

The Native reader uses this path for inferred top-level cell literals:

```lean
Wen.Native.Reader.cellExprOfRWordString? "oxoxoxoxox"
  : Option (Sigma fun n => Wen.Native.Expr n)

Wen.Native.Reader.readEvalInferredCellString? 8 "#oxoxoxoxox"
  = some (10, "oxoxoxoxox")

Wen.Native.Reader.readEvalInferredCellString? 8 "oxoxoxoxox"
  = some (10, "oxoxoxoxox")
```

Inside compound Wen forms, bare `ox...` remains a name; `#ox...` is the
literal spelling.  The bare form is inferred only when the whole input is a
single top-level word.  Outside explicit direct sums, all explicit word tokens
in one inferred native form must have the same rank; mixed-rank compounds fail
in the reader instead of silently lifting, concatenating, or coercing to `R8`.

The native reader now exposes direct sum as a static lowering form:

```lean
Wen.Native.Reader.readEvalInferredCellString? 16 "(dsum #oooooooo #oxox)"
  = some (12, "oooooooooxox")

Wen.Native.Reader.readEvalInferredCellString? 24
  "(dsum (flip 0 #oooooooo) (xor #oxox #oooo))"
  = some (12, "xooooooooxox")

Wen.Native.Reader.readEvalInferredCellString? 16 "(dsum #oooo #oooo #oxox)"
  = Wen.Native.Reader.readEvalInferredCellString? 16 "(dsum #oooooooo #oxox)"
```

This is not runtime heterogeneity.  Each component is lowered to a slice of one
ordinary `Expr N`, so the evaluator and value model remain fixed-rank.  In this
first version, `dsum` components are cell-valued blocks only: literals,
`(cell bits)`, word refs, `xor`, `act`, `flip`, and nested `dsum`.  `eq` is
Bool-valued and is not a valid component; rankless forms such as `cons`, `quote`,
`eval`, numbers, lambdas, and arbitrary apps are also rejected.

---

## RPattern — partial faces

`RPattern N := Fin N -> Option Bool` is the kernel type for partial
assignments.  At each position:

- `none` means unspecified.
- `some false` pins that coordinate to `o`.
- `some true` pins that coordinate to `x`.

The main operations are:

```lean
RPattern.empty     : RPattern N
RPattern.support   : RPattern N -> Finset (Fin N)
RPattern.ofFull    : R N -> RPattern N
RPattern.toFull?   : RPattern N -> Option (R N)
RPattern.compatible : RPattern N -> RPattern N -> Prop
RPattern.merge     : RPattern N -> RPattern N -> Option (RPattern N)
RPattern.restrict  : Finset (Fin N) -> RPattern N -> RPattern N
RPattern.mergeAll  : List (RPattern N) -> Option (RPattern N)
```

Geometrically, a pattern with `k` specified positions selects a face of
dimension `N - k` in the `N`-cube.  `ofFull v` is a vertex; `empty` is the
whole cube.  `merge` lowers dimension by adding compatible commitments, while
`restrict` raises dimension by forgetting positions.

`merge` is the single operation behind the old heterogeneous-composition
intuition:

| support geometry | result |
|---|---|
| disjoint supports | parallel composition; supports union |
| one support contained in the other | refinement |
| overlapping supports with disagreement | `none` |

The support laws in Lean make this explicit:

```lean
support (mergeFn a b) = support a ∪ support b
support (restrict s c) = s ∩ support c
```

This is why the earlier cases `R4 * R4`, `R4 * R2`, `R8 * R2`, and arbitrary
legal combinations should not be implemented as special cases.  Total
concatenation belongs to `RWord` / direct sums; overlay, refinement, and
constraint belong to `RPattern.merge`.

---

## Wen.Core status

[`Foundation/Wen/Core`](../../../formal/SSBX/Foundation/Wen/Core/) is still the
rank-8 RPattern machine.  Its state is:

```lean
cur : RPattern 8
history : List (RPattern 8)
```

and `State.initial.cur = RPattern.empty`.  Its ISA is RPattern-aware:
`merge`, `restrict`, `mergePrior`, partial-aware branches, and total-input
lifting through `RPattern.ofFull`.

This is useful for constraint composition and old Wen.Core proofs, but it is
not the whole Native path.  The current Native reader can already parse
arbitrary-rank total `o`/`x` words through `RWord`; the old rank-8 machine is
one operational layer on top of the same R kernel, not the definition of the
kernel.

---

## Status

- `Foundation/R/RWord.lean`: arbitrary-rank strict parsing/rendering and direct
  `R (N+M) ≃ R N × R M` split helpers; 0 sorry in the targeted build.
- `Foundation/R/RPattern.lean`: partial face-lattice algebra with `empty`,
  `merge`, `restrict`, `mergeAll`, full/partial round trip, and support laws;
  0 sorry in the targeted build.
- `Foundation/Wen/Native/Reader.lean` and
  `Foundation/Wen/Interpreter/NativeReader.lean`: primary inferred-rank cell
  APIs for top-level `o`/`x` strings, static `(dsum ...)` lowering for
  mixed-rank total-word composition, plus direct `RWord -> Expr n` /
  `RWord -> Value n` helpers.

## Open / TODO

- Wen.Core remains rank-8.  A polymorphic `RPattern N` machine is clean but not
  required for the current Native reader.
- Runtime heterogeneous programs remain deferred.  The current native surface
  supports explicit static concatenation with `(dsum ...)`; overlay/refinement
  still belongs to `RPattern`, and the surface grammar should not blur them.
- `R8` remains a legacy compatibility target for old Hex/R8-shaped adapters;
  it is not the default destination for arbitrary native words.
- Semantic names such as Yi hexagrams, Shi states, Pauli labels, or Chinese
  explanations must stay in `Foundation/Atlas` or application-level docs.
