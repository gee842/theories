# Odd/Even Two-Step Band — n=2 Inner/Outer Overlay

> Status: paired-layer candidate, not kernel semantics.
> Scope: this document refines [`r5-glyph-rationale.md`](./r5-glyph-rationale.md):
> the old R5/R6 `內/外` reading is the `n = 2` example of an all-scale
> odd/even band.
> The formal core remains `R N := Fin N -> Bool`; glyphs enter only through
> explicit `.wen` lexicon bindings.

## Finding

The kernel statement is all-scale.  For every `n`, an odd rank is an even
prefix plus one residual bit:

```text
R (2*n + 1) ~= R (2*n) x R 1
```

and the next even rank closes that residual into a two-bit label space:

```text
R (2*n + 2) ~= R (2*n) x R 2
```

So the structural pattern is:

| rank shape | structure | role |
|---|---|---|
| `R (2*n+1)` | `R (2*n) x Bool` | one residual bit above an even prefix |
| `R (2*n+2)` | `R (2*n) x Bool x Bool` | two residual labels above the same prefix |

The `內/外` language is one lexicon choice for the `n = 2` overlay.  It should
not be read as kernel structure.  At the kernel level, the only facts are
projection, residual fiber, labeled slices, and coverage.

## Review Status

The 2026-05-19 review separates three questions:

| question | status | note |
|---|---|---|
| all-scale coordinate theorem | OK | Lean proves the generic `R (N+K)` slice/fiber/coverage facts and the `2*n+1` / `2*n+2` residual splits. |
| n=2 coordinate listing | OK | The tables below list the 32 one-bit and 64 two-bit addresses for the `n = 2` overlay. |
| parser feasibility | OK, with boundary | The candidate `.wen` files are valid flat lexicons; current lookup expands a whole input token, not aliases inside compound forms. |
| glyph reasonableness | candidate | The structural names are justified by coordinates.  Single glyphs and hexagram names remain proposed readings, not proof that Chinese characters are uniquely determined by the R tower. |

The strongest part is the all-scale coordinate grammar:

```text
R (2*n) word -> one residual bit -> two residual bits
```

The weakest part is also explicit: a traditional R6 hexagram name is a useful
rank-6 address alias, but it does not by itself prove that the new
`本本 / 本征 / 征本 / 征征 + even-prefix face` reading is philologically canonical.  The
candidate lexicon is therefore data to test, not compiler semantics.

For the general theory of why `R (N+K) -> R N` loses the residual `R K`, why a
claim must descend through a scope before it is valid there, and how
chart/focus forgetting differs from coordinate projection, see
[`r-scope-information-flow.md`](./r-scope-information-flow.md).

## Coordinates

Let `w : R (2*n)` be an even-prefix word.

The odd rank appends one residual bit:

```text
w ++ o
w ++ x
```

The next even rank appends two residual bits:

```text
w ++ oo
w ++ ox
w ++ xo
w ++ xx
```

In the `n = 2` overlay, these four labels are read as:

```text
oo = 本本
ox = 本征
xo = 征本
xx = 征征
```

That gives the two overlay operator names:

| operator | mask | effect |
|---|---|---|
| `易內` | toggles the first residual bit | changes `內本 <-> 內征` |
| `易外` | toggles the second residual bit | changes `外本 <-> 外征` |

They should be read as a pair.  `易內` without `易外` is an inward turn; `易外`
without `易內` is external re-presentation.  Together they generate the
two-bit residual square above every even-prefix face.

## Complete Listing

This section lists the `n = 2` overlay for the current low-rank candidate
table.  The list is structural first, but it also records actual glyph
candidates.  The 32 one-bit names are proposed; the 64 two-bit names have an
existing historical glyph set.  Those names should enter through an explicit
lexicon overlay, not compiler knowledge.

### R5 Inner Pair

| prefix face (`n = 2`) | `內本` | `內征` |
|---|---|---|
| `#oooo` 生 | `#ooooo` 種 = `內本·生` | `#oooox` 育 = `內征·生` |
| `#ooox` 行 | `#oooxo` 徑 = `內本·行` | `#oooxx` 履 = `內征·行` |
| `#ooxo` 化 | `#ooxoo` 質 = `內本·化` | `#ooxox` 革 = `內征·化` |
| `#ooxx` 流 | `#ooxxo` 源 = `內本·流` | `#ooxxx` 衍 = `內征·流` |
| `#oxoo` 萌 | `#oxooo` 芽 = `內本·萌` | `#oxoox` 茁 = `內征·萌` |
| `#oxox` 長 | `#oxoxo` 根 = `內本·長` | `#oxoxx` 滋 = `內征·長` |
| `#oxxo` 轉 | `#oxxoo` 軸 = `內本·轉` | `#oxxox` 旋 = `內征·轉` |
| `#oxxx` 續 | `#oxxxo` 緒 = `內本·續` | `#oxxxx` 繼 = `內征·續` |
| `#xooo` 緣 | `#xoooo` 由 = `內本·緣` | `#xooox` 牽 = `內征·緣` |
| `#xoox` 通 | `#xooxo` 渠 = `內本·通` | `#xooxx` 達 = `內征·通` |
| `#xoxo` 會 | `#xoxoo` 契 = `內本·會` | `#xoxox` 合 = `內征·會` |
| `#xoxx` 繫 | `#xoxxo` 綱 = `內本·繫` | `#xoxxx` 維 = `內征·繫` |
| `#xxoo` 兆 | `#xxooo` 象 = `內本·兆` | `#xxoox` 占 = `內征·兆` |
| `#xxox` 趨 | `#xxoxo` 向 = `內本·趨` | `#xxoxx` 赴 = `內征·趨` |
| `#xxxo` 變 | `#xxxoo` 故 = `內本·變` | `#xxxox` 更 = `內征·變` |
| `#xxxx` 史 | `#xxxxo` 記 = `內本·史` | `#xxxxx` 述 = `內征·史` |

### R6 Inner/Outer Square

| prefix face (`n = 2`) | `本本` | `本征` | `征本` | `征征` |
|---|---|---|---|---|
| `#oooo` 生 | `#oooooo` 本本·生 | `#ooooox` 本征·生 | `#ooooxo` 征本·生 | `#ooooxx` 征征·生 |
| `#ooox` 行 | `#oooxoo` 本本·行 | `#oooxox` 本征·行 | `#oooxxo` 征本·行 | `#oooxxx` 征征·行 |
| `#ooxo` 化 | `#ooxooo` 本本·化 | `#ooxoox` 本征·化 | `#ooxoxo` 征本·化 | `#ooxoxx` 征征·化 |
| `#ooxx` 流 | `#ooxxoo` 本本·流 | `#ooxxox` 本征·流 | `#ooxxxo` 征本·流 | `#ooxxxx` 征征·流 |
| `#oxoo` 萌 | `#oxoooo` 本本·萌 | `#oxooox` 本征·萌 | `#oxooxo` 征本·萌 | `#oxooxx` 征征·萌 |
| `#oxox` 長 | `#oxoxoo` 本本·長 | `#oxoxox` 本征·長 | `#oxoxxo` 征本·長 | `#oxoxxx` 征征·長 |
| `#oxxo` 轉 | `#oxxooo` 本本·轉 | `#oxxoox` 本征·轉 | `#oxxoxo` 征本·轉 | `#oxxoxx` 征征·轉 |
| `#oxxx` 續 | `#oxxxoo` 本本·續 | `#oxxxox` 本征·續 | `#oxxxxo` 征本·續 | `#oxxxxx` 征征·續 |
| `#xooo` 緣 | `#xooooo` 本本·緣 | `#xoooox` 本征·緣 | `#xoooxo` 征本·緣 | `#xoooxx` 征征·緣 |
| `#xoox` 通 | `#xooxoo` 本本·通 | `#xooxox` 本征·通 | `#xooxxo` 征本·通 | `#xooxxx` 征征·通 |
| `#xoxo` 會 | `#xoxooo` 本本·會 | `#xoxoox` 本征·會 | `#xoxoxo` 征本·會 | `#xoxoxx` 征征·會 |
| `#xoxx` 繫 | `#xoxxoo` 本本·繫 | `#xoxxox` 本征·繫 | `#xoxxxo` 征本·繫 | `#xoxxxx` 征征·繫 |
| `#xxoo` 兆 | `#xxoooo` 本本·兆 | `#xxooox` 本征·兆 | `#xxooxo` 征本·兆 | `#xxooxx` 征征·兆 |
| `#xxox` 趨 | `#xxoxoo` 本本·趨 | `#xxoxox` 本征·趨 | `#xxoxxo` 征本·趨 | `#xxoxxx` 征征·趨 |
| `#xxxo` 變 | `#xxxooo` 本本·變 | `#xxxoox` 本征·變 | `#xxxoxo` 征本·變 | `#xxxoxx` 征征·變 |
| `#xxxx` 史 | `#xxxxoo` 本本·史 | `#xxxxox` 本征·史 | `#xxxxxo` 征本·史 | `#xxxxxx` 征征·史 |

This completes the active structural list.  The actual R6 glyph overlay is:

| prefix face (`n = 2`) | `本本` | `本征` | `征本` | `征征` |
|---|---|---|---|---|
| `#oooo` 生 | `#oooooo` 乾 | `#ooooox` 夬 | `#ooooxo` 大有 | `#ooooxx` 大壯 |
| `#ooox` 行 | `#oooxoo` 小畜 | `#oooxox` 需 | `#oooxxo` 大畜 | `#oooxxx` 泰 |
| `#ooxo` 化 | `#ooxooo` 履 | `#ooxoox` 兌 | `#ooxoxo` 睽 | `#ooxoxx` 歸妹 |
| `#ooxx` 流 | `#ooxxoo` 中孚 | `#ooxxox` 節 | `#ooxxxo` 損 | `#ooxxxx` 臨 |
| `#oxoo` 萌 | `#oxoooo` 同人 | `#oxooox` 革 | `#oxooxo` 離 | `#oxooxx` 豐 |
| `#oxox` 長 | `#oxoxoo` 家人 | `#oxoxox` 既濟 | `#oxoxxo` 賁 | `#oxoxxx` 明夷 |
| `#oxxo` 轉 | `#oxxooo` 無妄 | `#oxxoox` 隨 | `#oxxoxo` 噬嗑 | `#oxxoxx` 震 |
| `#oxxx` 續 | `#oxxxoo` 益 | `#oxxxox` 屯 | `#oxxxxo` 頤 | `#oxxxxx` 復 |
| `#xooo` 緣 | `#xooooo` 姤 | `#xoooox` 大過 | `#xoooxo` 鼎 | `#xoooxx` 恒 |
| `#xoox` 通 | `#xooxoo` 巽 | `#xooxox` 井 | `#xooxxo` 蠱 | `#xooxxx` 升 |
| `#xoxo` 會 | `#xoxooo` 訟 | `#xoxoox` 困 | `#xoxoxo` 未濟 | `#xoxoxx` 解 |
| `#xoxx` 繫 | `#xoxxoo` 渙 | `#xoxxox` 坎 | `#xoxxxo` 蒙 | `#xoxxxx` 師 |
| `#xxoo` 兆 | `#xxoooo` 遁 | `#xxooox` 咸 | `#xxooxo` 旅 | `#xxooxx` 小過 |
| `#xxox` 趨 | `#xxoxoo` 漸 | `#xxoxox` 蹇 | `#xxoxxo` 艮 | `#xxoxxx` 謙 |
| `#xxxo` 變 | `#xxxooo` 否 | `#xxxoox` 萃 | `#xxxoxo` 晉 | `#xxxoxx` 豫 |
| `#xxxx` 史 | `#xxxxoo` 觀 | `#xxxxox` 比 | `#xxxxxo` 剝 | `#xxxxxx` 坤 |

This is the point I missed in the previous pass: the structural names close the
coordinate system, but the R6 glyphs are not blank.  They are exactly this
historical 64-name overlay.  The active-source rule is only that these names
must be loaded as data, not baked into the kernel.

Machine-readable candidate lexicons are provided as separate files:

| file | content | reason for separation |
|---|---|---|
| `formal/SSBX/Foundation/Wen/lexicons/r5-candidate.wen` | R5 `內本/內征` glyphs | R5 has candidate 32-cell names. |
| `formal/SSBX/Foundation/Wen/lexicons/r6-candidate.wen` | R6 structural names plus hexagram glyphs | R6 has historical 64-name glyphs. |

They are separated because the current `SourceLexicon` lookup is flat.  Some
glyphs naturally collide across ranks, for example `履` and `革`; a future
rank-aware resolver can load both together, but today's flat lookup should not
pretend that collision is solved.

There is also a current interpreter boundary: the CLI/REPL lexicon lookup is a
whole-line glyph lookup before native evaluation.  So `本本·生` can lower to
`#oooooo` when it is the whole input, but aliases are not yet expanded inside
compound native forms such as `(pair 本本·生 本征·生)`.

## Why R5 Alone Felt Awkward

The earlier one-bit overlay table looked plausible because many pairs have a real
noun/action shape:

```text
徑/履, 質/革, 源/衍, 緒/繼, 由/牽,
渠/達, 契/合, 綱/維, 象/占, 故/更, 記/述
```

But those pairs are not a complete world.  They are one residual split above
an even-prefix face.  Once the second residual bit is added, each pair becomes
a square:

```text
          外本      外征
內本      本本      本征
內征      征本      征征
```

That is the all-scale odd/even structure.  The one-bit rank is the interface
where a residual distinction first appears; the next even rank is the closure
where two residual coordinates can vary independently.

## R6 Is Not Just Hex Again

The `n = 2` two-bit overlay has a traditional Hexagram anchor, but active Wen
should not make Hex/Yi the default semantics again.  The active structural
name is:

```text
TwoBitLabel · EvenPrefixFace
```

where the `n = 2` label lexicon may read:

```text
Quadrant ::= 本本 | 本征 | 征本 | 征征
```

The traditional hexagram names above are the strongest actual R6 glyph
candidates.  The rank-polymorphic source path should still be able to
understand the rank-6 overlay structurally, without importing Yi/Hex doctrine:

```text
本本·生
本征·生
征本·生
征征·生
```

This keeps the interpreter line clean:

```text
glyph -> #ox... / @ox... -> Wen.Native.Expr n
```

and avoids restoring `Hexagram` as a privileged active source type.

## Example: `生`

Using the current R4 candidate:

```text
#oooo = 生
```

R5 gives the inner pair:

| word | structural reading | candidate glyph |
|---|---|---|
| `#ooooo` | `內本·生` | 種 |
| `#oooox` | `內征·生` | 育 |

R6 closes the square:

| word | structural reading | possible prose reading |
|---|---|---|
| `#oooooo` | `本本·生` | generation held inwardly and outwardly as basis |
| `#ooooox` | `本征·生` | generation whose inner basis is outwardly expressed |
| `#ooooxo` | `征本·生` | generation inwardly active while outwardly grounded |
| `#ooooxx` | `征征·生` | generation active both inwardly and outwardly |

The R6 structural names are enough for the active kernel path.  The actual
human glyph overlay may also bind the four words above to `乾 / 夬 / 大有 /
大壯`.

## Operator Consequence

A low-rank even prefix can have extra operator audits, for example:

```text
R4 = End(R2)
```

But the all-scale odd/even band does not inherit that exact privilege.  Its
honest default operator reading is mask translation:

```text
@m(s) = m xor s
```

Therefore overlay operator names should be generated from coordinate atoms:

| rank | atoms |
|---|---|
| `R (2*n+1)` | inherited even-prefix toggles + one residual toggle |
| `R (2*n+2)` | inherited even-prefix toggles + two residual toggles |

For the `n = 2` overlay, the two residual toggles are named `易內` and `易外`.

Composite names should remain explicit unless the compound is stable:

```text
變化
改變
臨+易內
易內+易外
改+變化+臨+易內+易外
```

This separates cell glyphs from operator glyphs more sharply than the low-rank
matrix audit does.  That separation is not a defect.  It is exactly what the
odd/even band shows: residual-coordinate extensions are not automatically new
endomorphism algebras.

## Lexicon Direction

An experimental active lexicon for the `n = 2` overlay should probably use
four layers:

1. even-prefix cell glyphs: `生 / 行 / 化 / ...`.
2. one-bit residual aliases where they are strong: `徑 / 履`, `質 / 革`, etc.
3. two-bit structural aliases generated from label + even-prefix face.
4. historical rank-6 glyph aliases: the sixty-four hexagram names listed above.

For the two-bit overlay, structure should come before traditional names:

```wen
名
  #oooooo 本本·生
  #ooooox 本征·生
  #ooooxo 征本·生
  #ooooxx 征征·生
```

Hexagram names can be added in the same non-default candidate lexicon:

```wen
名 #oooooo 乾
```

The key boundary is that this is an explicit lexicon choice, not compiler
knowledge.

## Current Result

The better all-scale statement is:

```text
R (2*n+1) / R (2*n+2) = one-bit residual / two-bit residual completion
```

The `n = 2` one-bit layer is useful, but it is not the natural stopping point.
The next even layer is where the pair closes.  This also explains why the
rank-6 overlay has much stronger traditional pressure than the rank-5 overlay:
the former is a complete two-bit field, while the latter is a half-step
internalization.
