# 道德经第一章 formalization spec

> Status: first adapter slice live; still not a completed formalization.
> Date: 2026-05-19.
> Scope: first chapter only.  This document replaces the earlier
> `daodejing-01.wen` interpretation as the canonical direction.  The runnable
> file `formal/SSBX/Foundation/Wen/samples/daodejing-01-scope-demo.wen` is only
> a scope/report demo.  The stricter first attempt is
> `formal/SSBX/Foundation/Wen/samples/daodejing-01-formal.wen`.
> Implementation must follow
> `docs-next/10_formal_形式/wen-to-r-code-frontend-plan.md`,
> not by adding more token-pattern cases to the current prototype.

## Why the previous sample was not real

The previous runnable example assigned:

```text
妙 := #oxox
徼 := #oooooooo
玄 := #oooooooooxox
```

and then judged:

```text
判 (eq (dsum 徼 妙) 玄)
```

That checks the interpreter, but it does not check the text.  The conclusion
was already embedded in the lexicon.  A real formalization must not put
`玄 = 徼 + 妙` into the dictionary.  It must make the sentence structure produce
the claim.

The stricter rule is:

```text
lexicon gives atoms;
syntax gives claim shape;
laws give admissible inference;
R judgment reports truth, descent, loss, overclaiming, or needs-law.
```

## Kernel shape

The target is not tied to `R8` or `R4`.  Use parameters:

```text
V : visible rank
K : residual rank
D : R (V + K)
observe_V(D) = visible D : R V
residual_K(D) = residual D : R K
```

The relevant kernel facts are already R-native:

- `R (V + K) ≃ R V × R K` by direct-sum/scope splitting.
- If `0 < K`, visible scope alone cannot recover the residual:
  `not_carrierRecoversResidual_of_pos`.
- A predicate descends through a scope exactly when it is constant on every
  observation fiber: `RJudgment.descends_iff_fiber_constant`.
- Visible-only predicates descend: `RJudgment.visibleOnly_descends`.
- Residual-dependent predicates overclaim when residual rank is positive:
  `RJudgment.residualDependent_overclaims`.
- A law may recover residual information only when it explicitly determines
  residuals: `LawDeterminesResidual`.

Thus the real Daodejing question is not whether `8 + 4` is special.  The
question is whether the text consistently distinguishes:

```text
visible saying       : claims over R V
constant/full saying : claims over R (V + K)
subtle/residual      : claims over R K
law-mediated recovery: extra assumptions that determine R K
```

## Source text

```text
道可道，非常道。
名可名，非常名。
無名天地之始；有名萬物之母。
故常無欲，以觀其妙；常有欲，以觀其徼。
此兩者，同出而異名，同謂之玄。
玄之又玄，眾妙之門。
```

## Formal roles

These are roles, not final word assignments.

| Surface | Role | R-level target |
|---|---|---|
| 道 | object variable / source object | `D : R (V + K)` |
| 名 | naming operation or naming object | `Name : R (V + K)` or an operation over objects |
| 可 | sayability modality | asks whether a claim descends to a stated scope |
| 常 | full/invariant claim | asks for full-scope truth or law-backed invariance |
| 非 | separation / non-implication | not ordinary lexical negation only |
| 無名 | no-name mode | residual / pre-name side, not directly visible |
| 有名 | name-present mode | visible naming side |
| 妙 | subtle aspect | residual observation target |
| 徼 | boundary aspect | visible observation target |
| 同出 | common-source relation | two observations arise from one full object |
| 異名 | distinct labels | names differ even if source is common |
| 謂之 | naming assertion | bind a derived claim label, not a primitive equality |
| 玄 | result of common-source + distinct-name reading | derived object/claim, not lexicon primitive |
| 之又 | iteration / lift | apply the same pattern at the next scope |
| 門 | access/boundary operation | a higher object whose visible part is the prior result |

## Sentence-level readings

### 1. 道可道，非常道

Do not parse this as simple equality.  The first and third `道` have different
roles.

Target grammar:

```text
道 可 道，非 常 道
```

Target formal shape:

```text
object D : R (V + K)
visible claim S(D) : Pred (R V)
full claim C(D) : Pred (R (V + K))

claim A: S descends through visible scope
claim B: C does not follow from visible scope unless a law is supplied
```

R judgment output should be one of:

```text
descent: descends          -- for the visible/sayable claim
descent: overclaims        -- for full claim asserted at visible scope
descent: descends          -- only at full scope or under a named law
descent: unknown/needs-law -- if the formalization supplies no law
```

This is the real form of "可道 is not 常道": visible saying is not full recovery.

### 2. 名可名，非常名

Same grammar as line 1, but over naming:

```text
名 可 名，非 常 名
```

Target:

```text
NameObj : R (V + K)
visible naming claim descends
full naming claim overclaims from visible scope unless law-backed
```

This should share the same generic theorem as line 1; it should not require a
new hardcoded `R8` case.

### 3. 無名天地之始；有名萬物之母

This line should not define `無名` as a particular suffix by fiat.  It should
introduce two modes of observation:

```text
NoName(D) : residual-side reading
HasName(D) : visible-side reading
```

Target:

```text
NoName depends on residual_K(D)
HasName depends on visible_V(D)
```

Expected R judgment:

```text
NoName at visible scope     -> overclaims or needs-law
HasName at visible scope    -> descends
NoName at full/residual scope -> descends
```

The words `天地之始` and `萬物之母` are not yet executable claims.  They should
be represented later as generative roles:

```text
始 : source/origin relation
母 : generating/nurturing relation
```

and only judged once those relations have R-dynamic semantics.

### 4. 常無欲，以觀其妙；常有欲，以觀其徼

This line distinguishes two observation policies.

Target:

```text
觀妙 : observe residual/subtle side
觀徼 : observe visible/boundary side
```

Expected R judgment:

```text
觀徼 through visible scope -> descends
觀妙 through visible scope -> overclaims or needs-law
觀妙 through residual/full scope -> descends
```

`欲` is not yet formalized.  The minimal safe reading is:

```text
無欲 / 有欲 are observation policies, not moral truth values.
```

Future dynamic reading:

```text
無欲 : operation that does not force residual into visible naming
有欲 : operation that selects visible boundary
```

That dynamic version belongs in `RDynamic`, not in the lexicon.

### 5. 此兩者，同出而異名，同謂之玄

This is where the previous demo cheated by assigning `玄` directly.

Real target:

```text
Two readings A and B share one full source D.
They have distinct names.
The pair/common-source structure receives the label 玄.
```

Formal shape:

```text
CommonSource(D, A, B)
DistinctName(name(A), name(B))
NameAs(玄, CommonSource(D, A, B) + DistinctName(...))
```

Executable first approximation:

```text
given A : R V and B : R K,
derive Pair(A,B) : R (V+K) by direct sum;
do not bind 玄 to Pair(A,B) in the lexicon;
instead, a `謂之 玄` clause creates the alias/certificate.
```

Needed implementation:

```text
句 同出 A B 謂之 X
```

should lower to a derived binding/certificate, not an ordinary `名 #word X`.

### 6. 玄之又玄，眾妙之門

This is iteration/lift.

Target:

```text
if X is a full object at rank V+K,
then X之又X lifts to a new object at rank (V+K)+K'
or to an iterated scope package.
```

The exact rank is not fixed.  The earlier demo used `R16 = R12 + R4`; that is
only an instance.  The general target is:

```text
R (V + K) -> R ((V + K) + K')
```

Expected R judgment:

```text
visible prior玄 at prefix V+K -> descends
new residual玄標 at prefix V+K -> overclaims unless law-backed
```

## Proposed `.wen` source grammar

This is the next implementation target.

```text
原 道可道非常道
句 可非常 道

原 名可名非常名
句 可非常 名

原 無名天地之始 有名萬物之母
句 無有名 道 始 母

原 常無欲以觀其妙 常有欲以觀其徼
句 觀 妙 徼

原 此兩者同出而異名同謂之玄
句 同出 妙 徼 謂之 玄

原 玄之又玄眾妙之門
句 又玄 玄 謂之 眾妙門
```

The first slice of this now exists in
`formal/SSBX/Foundation/Wen/ClassicalJudgment.lean`.  The dictionary supplies
primitive atoms and optional model witnesses; `句 同出 ... 謂之 ...` and
`句 又玄 ... 謂之 ...` derive new bindings during file execution instead of
requiring them in the initial lexicon.

## Acceptance criteria for the first real example

The first real example is accepted only when all of these are true:

1. The runnable `.wen` file does not bind `玄` directly to `dsum 徼 妙`.
2. `同出 ... 謂之 玄` is represented as a sentence-derived claim or certificate.
3. `可...非常...` lowers from grammar into visible/full scope contrast.
4. At least one reading returns `overclaims` with a witness.
5. At least one reading returns `descends`.
6. At least one reading returns `needs-law` or `unknown` when the grammar asks
   for a relation whose R semantics has not yet been supplied.
7. The output wording says "bounded finite runtime enumeration" unless a named
   Lean theorem is attached.

## Immediate next code slice

The first small active adapter exists:

```text
Foundation/Wen/ClassicalJudgment.lean
```

Responsibilities:

- parse `句` lines;
- elaborate each supported classical sentence form to one or more existing
  `Wen.SourceJudgment` requests;
- keep unsupported semantic relations as `needs-law`, not false;
- avoid imports from `WenDef`, `WenSurface`, Yi, Hex, Bagua, or Atlas.

The R kernel remains unchanged: it already owns the mathematics of scope,
loss, overclaiming, and law-mediated recovery.

Next slices:

- replace the still-explicit `句 可非常 所道 可道 道體 前 8` shape with a
  parser closer to the original text;
- attach `needs-law` reports to `天地之始`, `萬物之母`, and `欲` instead of
  leaving them as comments;
- move repeated scope/report wording behind named theorem-backed certificates
  where the Lean theorem already exists.
