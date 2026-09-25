# R1-R4 Glyph Rationale

> Status: draft candidate lexicon rationale, not kernel semantics.
> Scope: this document explains a possible human glyph table for R1-R4.
> The formal core remains `R N := Fin N → Bool`; `o/x` words are canonical.
> Chinese glyphs enter only through explicit `.wen` lexicon bindings.
> First falsification pass: [`r1-r4-glyph-test.md`](./r1-r4-glyph-test.md).
> Next layer candidate: [`r5-glyph-rationale.md`](./r5-glyph-rationale.md).

This document gives a disciplined way to read the first four R layers as words.
It is not a theorem and it is not a default doctrine table.  Its purpose is to
make every proposed glyph auditable: for each word we should be able to say why
it belongs at that exact `o/x` address, how it relates to the previous layer,
and how it can later support both cell and operator readings without putting
Chinese meaning into the kernel.

This low-rank audit is not the base of the scope/loss theory.  The all-scale
kernel theory is stated over `R (N+K)`, `R (2*n+1)`, and `R (2*n+2)` in
[`r-scope-information-flow.md`](./r-scope-information-flow.md).  The present
document is only a candidate lexicon for small ranks.

The guiding convention is:

```text
o = 隱: unmarked, latent, not yet manifest
x = 見: marked, manifest, visible as a distinction
```

`隱/見` are chosen instead of `陰/陽`, `無/有`, or `0/1` because they are close
to the substrate-level distinction while avoiding a premature Yi, ontology, or
numeric reading.  They say only whether a distinction has come into visibility.

## Role Rule

A glyph may later have both readings:

```wen
名 #oooo 生
名 @oooo 生
```

This means:

| form | reading | responsibility |
|---|---|---|
| `#word` | cell / value | names an R-cell at that exact address |
| `@word` | reference / operator | names a value in the native environment at that exact address |

The kernel must not guess between the two.  A future role-aware resolver should
choose by syntactic position:

| context | glyph role |
|---|---|
| value / object position | `#word` |
| function / operator position | `@word` |
| no deciding context | report ambiguity or require explicit `#` / `@` |

So `生生不息` can be read without special-casing the phrase:

```text
生 生 不息
@生 #生 ...
```

The first `生` is the operation named by the glyph; the second `生` is the cell
named by the same glyph.  The lexicon records that both readings are allowed;
the grammar decides which reading is active.

For R4 there is one extra audit condition: `R 4` has both pair-state and
matrix-operator views.  A glyph may name the pair-state directly.  If the same
glyph is enabled as an operator, the operator implementation must either be the
corresponding `R 4 = End(R 2)` matrix action or an explicitly defined native
operation whose law matches the same semantic pattern.  The glyph table alone
does not prove the operator law.

## Operator Schemas

The same surface glyph can be a cell and an operator, but the operator side has
to say which law it means.  The useful schemas in R1-R4 are:

| layer | canonical `#` reading | canonical `@` reading |
|---|---|---|
| R1 | one-bit visibility state | one-dimensional linear endomap: hide/preserve |
| R2 | body/process cell | same-rank mask action: toggle relation/activity axes |
| R3 | phase profile | same-rank mask action: toggle source/pivot/outcome axes |
| R4 | R2-body × R2-process cell | matrix action `R 2 → R 2` via `R 4 = End(R 2)` |

The R2/R3 operator readings are intentionally weaker than R4.  R2 and R3 are
not endomorphism algebras of the previous displayed layer.  Their most honest
native operator is therefore the additive mask action on the same rank:

```text
@w(v) = v xor w
```

R4 is different: it is formally `End(R 2)`, so `@w` has a stronger matrix
reading:

```text
@w(a, b) = M_w · (a, b)
```

If a future environment defines a richer named operation for a glyph, that
operation should be recorded as an additional law.  It should not silently
replace the basic audit law.

This `R 4 = End(R 2)` privilege is a low-rank algebraic audit, not a general
rule for all later ranks.  Later odd/even bands should default to coordinate
mask actions unless an explicit endomorphism law is supplied.

## R1

R1 has exactly one distinction.  It should not yet say object, motion, relation,
or event.  It only says whether the mark is latent or manifest.

| word | glyph | reason |
|---|---|---|
| `#o` | 隱 | The distinction is present only as unmarked potential.  `隱` says "not yet visible" without saying non-being. |
| `#x` | 見 | The distinction has become visible.  `見` says "manifest" rather than "true", "one", or "being". |

This is the smallest reading that can support all later readings.  `隱` can
later realise as absence, silence, potential, unmarked, or false; `見` can later
realise as presence, sayability, actuality, markedness, or true.  The words do
not force one realisation.

Operator reading:

| ref | glyph | operation | reason |
|---|---|---|---|
| `@o` | 隱 | `t ↦ o` | As an operator, hiding collapses either input to the unmarked state. |
| `@x` | 見 | `t ↦ t` | As an operator, seeing preserves what is present so it can remain visible. |

This uses the one-dimensional linear endomorphism reading of R1: `o` is the
zero map and `x` is the identity map.  This is stronger than a mere mnemonic.
It is the smallest possible operator pair.

## R2

R2 is the first square of the distinction.  It has two independent axes.  We
read the first coordinate as whether relation / interval has appeared, and the
second coordinate as whether activity / manifestation has appeared.

```text
first bit  = interval / relation axis
second bit = activity / manifestation axis
```

That gives a body reading:

| word | glyph | construction | reason |
|---|---|---|---|
| `#oo` | 物 | no interval, no activity | A thing as a bare locus: not yet relational, not yet active. |
| `#ox` | 動 | no interval, active | Motion as activity before it is organized into relation. |
| `#xo` | 間 | interval, not active | Interval, spacing, relation, or between-ness before event. |
| `#xx` | 事 | interval and activity | An affair/event: relation activated into something that happens. |

The same four cells also have a process reading:

| word | glyph | construction | reason |
|---|---|---|---|
| `#oo` | 幾 | no interval, no activity | The subtle beginning before visible action or relation. |
| `#ox` | 勢 | no interval, active | Tendency or force: activity already has direction, even before relation is articulated. |
| `#xo` | 機 | interval, not active | A pivot or trigger point: relation exists, but action has not yet fired. |
| `#xx` | 時 | interval and activity | Time is activated relation: before/after becomes real through happening. |

The two readings are not contradictory.  They are two projections of the same
R2 cells:

| word | body | process |
|---|---|---|
| `#oo` | 物 | 幾 |
| `#ox` | 動 | 勢 |
| `#xo` | 間 | 機 |
| `#xx` | 事 | 時 |

This gives R4 its row/column grammar: rows use the body reading; columns use the
process reading.

Operator reading uses the same-rank mask action on R2.  The two glyphs attached
to the same word share the same formal action; their difference is a surface
gloss.

| ref | glyphs | mask action on `(relation, activity)` | reason |
|---|---|---|---|
| `@oo` | 物 / 幾 | keep both axes | `物` lets the object stand; `幾` keeps the subtle condition unforced. |
| `@ox` | 動 / 勢 | toggle activity | `動` activates/deactivates; `勢` adds/removes directed tendency. |
| `@xo` | 間 / 機 | toggle relation | `間` opens/closes interval; `機` engages/disengages the pivot. |
| `@xx` | 事 / 時 | toggle relation and activity together | `事` eventuates by making relation active; `時` advances the relational activity as one pulse. |

The `@oo` case is deliberately quiet: as a mask operator it is identity.  If a
later language wants `物` or `幾` to mean a nontrivial operation, that operation
must be defined separately.  The basic R2 operator law is only the mask action.

## R3

R3 should not be forced into the R4 row-column table.  Its natural structure is
phase / aspect.  The proved R3 structure in the formal layer is coordinate
reversal:

```text
swap02(b0, b1, b2) = (b2, b1, b0)
```

So R3 should be read as:

```text
b0 = source / before
b1 = middle / pivot
b2 = outcome / after
```

The first and third coordinates form the reversal pair; the middle coordinate
is the pivot.  The table below is chosen so that the four palindromes are
self-reversal phases, and the four non-palindromes form two meaningful pairs.

| word | glyph | reversal | reason |
|---|---|---|---|
| `#ooo` | 藏 | self | Hidden before, hidden through the middle, hidden after.  This is concealment, not absence. |
| `#oox` | 呈 | pairs with `#xoo` | Hidden source becomes visible outcome while the middle remains unmarked: presentation / appearing. |
| `#oxo` | 蘊 | self | Hidden ends with a visible middle: something is held inside, active in the centre but not yet exposed. |
| `#oxx` | 起 | pairs with `#xxo` | Hidden source, active middle, visible outcome: arising or beginning to stand forth. |
| `#xoo` | 歸 | pairs with `#oox` | Visible source returns to hidden outcome: reversion / return. |
| `#xox` | 定 | self | Visible source and outcome with a hidden middle: the same manifest form holds across the pivot, hence stability. |
| `#xxo` | 斂 | pairs with `#oxx` | Visible source and active middle close into hidden outcome: gathering inward / contraction. |
| `#xxx` | 成 | self | Visible throughout source, pivot, and outcome: completion / formed actuality. |

The pair structure is:

| relation | words | reading |
|---|---|---|
| self-reversal | `#ooo 藏` | hidden remains hidden |
| self-reversal | `#oxo 蘊` | interior activity held within hidden ends |
| self-reversal | `#xox 定` | manifest form remains itself through the middle |
| self-reversal | `#xxx 成` | manifest process completed throughout |
| reversal pair | `#oox 呈` / `#xoo 歸` | appearing / returning |
| reversal pair | `#oxx 起` / `#xxo 斂` | arising / gathering back |

This keeps R3 distinct from R2 and R4.  R2 says "what kind of cell"; R3 says
"what phase profile"; R4 says "how a body cell meets a process cell".

Operator reading again uses same-rank mask action, now on the phase profile
`(source, pivot, outcome)`.

| ref | glyph | mask action | reason |
|---|---|---|---|
| `@ooo` | 藏 | keep the phase profile | Concealment here is non-exposure: no forced phase change. |
| `@oox` | 呈 | toggle outcome | Presentation acts at the end: it makes the outcome appear or withdraw. |
| `@oxo` | 蘊 | toggle pivot | What is contained acts in the middle while the ends remain untouched. |
| `@oxx` | 起 | toggle pivot and outcome | Arising starts inside and reaches the outcome. |
| `@xoo` | 歸 | toggle source | Returning changes the source side: the process is read back from where it began. |
| `@xox` | 定 | toggle source and outcome together | Stability preserves the relation between the two ends by moving them together. |
| `@xxo` | 斂 | toggle source and pivot | Gathering back acts from the source through the middle, closing before the outcome. |
| `@xxx` | 成 | toggle all three axes | Completion closes the whole phase profile as one total passage. |

These are phase actions, not matrix actions.  The formal invariant is that the
same word used as `#word` names the phase profile, while `@word` applies that
profile as a mask.  The reversal pairs still matter: `呈/歸` and `起/斂` are
opposite profiles under `swap02`, so their operator readings are paired too.

## R4

R4 is read as `R2 × R2`, equivalently the `n = 2` even split
`R (2*n) ~= R n × R n`:

```text
word = rowbits ++ columnbits
row    = body reading of R2:    物 / 動 / 間 / 事
column = process reading of R2: 幾 / 勢 / 機 / 時
```

This uses the same bit split as the formal pair view:

```text
#w0w1w2w3 = (#w0w1, #w2w3)
```

It also matches the row-major matrix view of `R 4 = End(R 2)`, but the table
below is primarily the pair-state reading.  Operator readings must be audited
separately as described in the Role Rule.  This is a useful low-rank example,
not the source of the all-scale projection theory.

|  | 幾 `#oo` | 勢 `#ox` | 機 `#xo` | 時 `#xx` |
|---|---|---|---|---|
| 物 `#oo` | 生 `#oooo` | 行 `#ooox` | 化 `#ooxo` | 流 `#ooxx` |
| 動 `#ox` | 萌 `#oxoo` | 長 `#oxox` | 轉 `#oxxo` | 續 `#oxxx` |
| 間 `#xo` | 緣 `#xooo` | 通 `#xoox` | 會 `#xoxo` | 繫 `#xoxx` |
| 事 `#xx` | 兆 `#xxoo` | 趨 `#xxox` | 變 `#xxxo` | 史 `#xxxx` |

### Row 物

| word | glyph | construction | reason |
|---|---|---|---|
| `#oooo` | 生 | 物 × 幾 | A thing touched by the subtle beginning becomes birth/generation.  `生` is better than `動` here because this cell is pre-motion: it is the arising of a thing, not motion itself. |
| `#ooox` | 行 | 物 × 勢 | A thing under tendency gains path and direction.  `行` is directed going, not raw activity. |
| `#ooxo` | 化 | 物 × 機 | A thing meeting a pivot changes form.  `化` is the transformation of a body through mechanism. |
| `#ooxx` | 流 | 物 × 時 | A thing under time is no longer fixed substance; it becomes flow. |

### Row 動

| word | glyph | construction | reason |
|---|---|---|---|
| `#oxoo` | 萌 | 動 × 幾 | Activity at its subtle beginning is sprouting.  `萌` keeps the movement incipient. |
| `#oxox` | 長 | 動 × 勢 | Activity reinforced by tendency becomes extension/growth.  `長` is motion that accumulates. |
| `#oxxo` | 轉 | 動 × 機 | Activity meeting a pivot turns.  `轉` also aligns better with the matrix-operator reading of `oxxo` as the swap pattern than `發` would. |
| `#oxxx` | 續 | 動 × 時 | Activity under time becomes continuation.  `續` is movement sustained across time. |

### Row 間

| word | glyph | construction | reason |
|---|---|---|---|
| `#xooo` | 緣 | 間 × 幾 | Relation at its subtle beginning is condition or affinity.  `緣` is relation before explicit connection. |
| `#xoox` | 通 | 間 × 勢 | Relation with tendency becomes passage.  `通` also fits the operator audit of `xoox` as identity/pass-through in the matrix view. |
| `#xoxo` | 會 | 間 × 機 | Relations meeting at a pivot become convergence or assembly. |
| `#xoxx` | 繫 | 間 × 時 | Relation sustained through time becomes binding, linkage, or system. |

### Row 事

| word | glyph | construction | reason |
|---|---|---|---|
| `#xxoo` | 兆 | 事 × 幾 | An event at its subtle beginning is a sign or omen.  `兆` is event before full occurrence. |
| `#xxox` | 趨 | 事 × 勢 | An event under tendency becomes a trend.  `趨` is the directional drift of affairs. |
| `#xxxo` | 變 | 事 × 機 | An event meeting a pivot becomes change.  `變` is not mere flow; it is event-level transformation at a critical point. |
| `#xxxx` | 史 | 事 × 時 | Events under time become history.  `史` is the temporal inscription of affairs. |

### Why `轉` replaces `發`

`動 × 機` could be read as `發`: motion triggered by a mechanism.  But R4 also
has an operator audit through the matrix view.  The word `#oxxo` is the swap
matrix:

```text
[[0, 1],
 [1, 0]]
```

As an operator, it exchanges the two basis directions of R2.  `轉` therefore
has a stronger double reading: as a cell it is motion encountering a pivot; as
an operator it is the turning/exchange pattern.  `發` remains a possible alias,
but `轉` is the better canonical glyph.

## R4 Operator Audit Notes

R4 has a formally important matrix view:

```text
#w0w1w2w3 = [[w0, w1],
             [w2, w3]]
```

This does not mean every R4 glyph automatically has a good primitive operator
reading.  It means every proposed `@glyph` has a concrete matrix law.  Write an
input R2 vector as `(a, b)`.

| ref | glyph | matrix action | reason |
|---|---|---|---|
| `@oooo` | 生 | `(a, b) ↦ (0, 0)` | Returns any input to the seed point.  As an operator, `生` is not "create from nothing"; it is reset-to-origin, the condition from which generation begins. |
| `@ooox` | 行 | `(a, b) ↦ (0, b)` | Keeps the second channel and erases the first: one directed path is selected. |
| `@ooxo` | 化 | `(a, b) ↦ (0, a)` | Moves the first channel into the second output: the form changes place. |
| `@ooxx` | 流 | `(a, b) ↦ (0, a + b)` | Merges both inputs downstream into one channel: flow as carried sum. |
| `@oxoo` | 萌 | `(a, b) ↦ (b, 0)` | Pulls the second channel forward into the first: sprouting from latent support. |
| `@oxox` | 長 | `(a, b) ↦ (b, b)` | Copies one channel into both outputs: extension and growth. |
| `@oxxo` | 轉 | `(a, b) ↦ (b, a)` | Swaps the two basis directions: turning/exchange. |
| `@oxxx` | 續 | `(a, b) ↦ (b, a + b)` | A rank-2 3-cycle on nonzero states: continuation through a cycle. |
| `@xooo` | 緣 | `(a, b) ↦ (a, 0)` | Preserves the first condition and drops the second: relation as initial condition. |
| `@xoox` | 通 | `(a, b) ↦ (a, b)` | Identity/pass-through: letting relation hold without obstruction. |
| `@xoxo` | 會 | `(a, b) ↦ (a, a)` | Copies the first channel into both outputs: convergence into a shared meeting point. |
| `@xoxx` | 繫 | `(a, b) ↦ (a, a + b)` | Keeps the first channel and binds the second to it: linkage. |
| `@xxoo` | 兆 | `(a, b) ↦ (a + b, 0)` | Compresses both inputs into a first signal: omen/sign as reduced trace. |
| `@xxox` | 趨 | `(a, b) ↦ (a + b, b)` | Keeps the second channel while bending the first by it: trend or tendency. |
| `@xxxo` | 變 | `(a, b) ↦ (a + b, a)` | The opposite rank-2 3-cycle: change through the nonzero states. |
| `@xxxx` | 史 | `(a, b) ↦ (a + b, a + b)` | Records one parity into both outputs: history as inscription of what the pair summed to. |

This fills the operator side for all sixteen R4 glyphs.  The six rank-2 words
are invertible operators; the rank-0 and rank-1 words are collapse/projection
operators.  Those collapse maps are not second-class.  They are precisely why
the R4 operator table can speak not only of reversible symmetry but also of
birth, path, trace, record, and binding.

The audit stops here.  Higher ranks do not inherit a matrix interpretation just
because their cells have glyphs; they need either the generic mask-action law
or an explicitly supplied native operation.

This also prevents semantic leakage.  The lexicon may say that `生` has both
`#oooo` and `@oooo` readings, but the operator reading is honest because its
matrix law is explicit.  If a later runtime wants `生` to mean a richer
recursive/generative function, that should be a named operation whose relation
to `@oooo` is stated, not silently assumed.

## Lexicon Sketch

The default lexicon should remain doctrine-free.  A separate experimental file
could contain:

```wen
名
  #o 隱
  #x 見

  #oo 物 幾
  #ox 動 勢
  #xo 間 機
  #xx 事 時

  #ooo 藏
  #oox 呈
  #oxo 蘊
  #oxx 起
  #xoo 歸
  #xox 定
  #xxo 斂
  #xxx 成

  #oooo 生
  #ooox 行
  #ooxo 化
  #ooxx 流
  #oxoo 萌
  #oxox 長
  #oxxo 轉
  #oxxx 續
  #xooo 緣
  #xoox 通
  #xoxo 會
  #xoxx 繫
  #xxoo 兆
  #xxox 趨
  #xxxo 變
  #xxxx 史
```

Operator aliases should be added only when the operator side has an explicit
definition or accepted matrix/mask reading.  A full experimental role-aware
lexicon would add the `@` side too:

```wen
名
  @o 隱
  @x 見

  @oo 物 幾
  @ox 動 勢
  @xo 間 機
  @xx 事 時

  @ooo 藏
  @oox 呈
  @oxo 蘊
  @oxx 起
  @xoo 歸
  @xox 定
  @xxo 斂
  @xxx 成

  @oooo 生
  @ooox 行
  @ooxo 化
  @ooxx 流
  @oxoo 萌
  @oxox 長
  @oxxo 轉
  @oxxx 續
  @xooo 緣
  @xoox 通
  @xoxo 會
  @xoxx 繫
  @xxoo 兆
  @xxox 趨
  @xxxo 變
  @xxxx 史
```

Eventually, role-aware lexicon loading can allow both lines for the same glyph:

```wen
名 #xoox 通
名 @xoox 通
```

At that point `通` in value position lowers to `#xoox`, while `通` in operator
position lowers to `@xoox`.

## Summary

The proposed progression is:

```text
R1: 隱 / 見
R2: 物 動 間 事     and     幾 勢 機 時
R3: 藏 呈 蘊 起 歸 定 斂 成
R4: 生 行 化 流 / 萌 長 轉 續 / 緣 通 會 繫 / 兆 趨 變 史
```

The logic is:

1. R1 names the primitive visibility distinction.
2. R2 names the first square as body cells and process cells.
3. R3 names phase profiles governed by reversal.
4. R4 names the interaction of an R2 body row with an R2 process column.
5. Cell/operator ambiguity is allowed as lexicon data, but resolved by syntax
   and audited by operator laws.
6. The all-scale R-scope theory does not depend on these small-rank names; it
   uses generic projection and residual theorems over `R (N+K)`.
