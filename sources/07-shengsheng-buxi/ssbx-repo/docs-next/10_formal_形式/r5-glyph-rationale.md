# R5 Glyph Rationale — n=2 Odd-Band Candidate

> Status: next-layer candidate, not kernel semantics.
> Scope: this document adapts the old R5 `內` layer as the `n = 2`
> specialization of the all-scale odd-band shape `R (2*n+1)`.
> The formal core remains `R N := Fin N -> Bool`; glyphs enter only through
> explicit `.wen` lexicon bindings.
> Paired-layer refinement: [`r5-r6-inner-outer-rationale.md`](./r5-r6-inner-outer-rationale.md).

## Finding

The kernel statement is all-scale:

```text
R (2*n + 1) ~= R (2*n) x Bool
```

This document is only the `n = 2` glyph candidate for that pattern:

```text
R (2*2 + 1) ~= R (2*2) x Bool
```

The appended bit is read as `內` in this candidate overlay:

| bit | reading | role |
|---|---|---|
| `o` | `內本` | the inner basis, root, vessel, trace, or condition of the even-prefix face |
| `x` | `內征` | the inner expression, use, tendency, or enactment of the even-prefix face |

So a one-bit odd-band word is obtained by appending one bit to an even-prefix
word:

```text
w ++ o = 內本·w
w ++ x = 內征·w
```

This means the table is constrained by the prefix table.  If a prefix cell
changes, the two cells above it must be re-audited.  The older R5 table in
[`r4-r8-character-ladder.md`](./r4-r8-character-ladder.md) and
`root-language-tree/glyph-inventory/R5.md` used the older R4 line where
`#oooo = 動`, `#oxxo = 發`, and `#xoxx = 系`.  The current active R1-R4
candidate changed these to:

```text
#oooo = 生
#oxxo = 轉
#xoxx = 繫
```

Therefore this `n = 2` odd-band overlay needs a new pass before it becomes a
`.wen` lexicon.  The paired next-even layer is audited in
[`r5-r6-inner-outer-rationale.md`](./r5-r6-inner-outer-rationale.md).

## Cell Table

The table below keeps the old R5 principle where it still fits, but repairs
the rows affected by the current prefix table.  The canonical fallback remains
structural: `內本·prefix` and `內征·prefix`.

| prefix word | prefix glyph | 內本 word | 內本 glyph | why | 內征 word | 內征 glyph | why | status |
|---|---|---|---|---|---|---|---|---|
| `#oooo` | 生 | `#ooooo` | 種 | generation as seed or planted source | `#oooox` | 育 | generation as nurture and bringing forth | provisional |
| `#ooox` | 行 | `#oooxo` | 徑 | path as the inner basis of going | `#oooxx` | 履 | treading as the enacted use of a path | strong |
| `#ooxo` | 化 | `#ooxoo` | 質 | the substance that can be transformed | `#ooxox` | 革 | the enacted alteration of that substance | strong |
| `#ooxx` | 流 | `#ooxxo` | 源 | the source from which flow proceeds | `#ooxxx` | 衍 | the extension or overflowing of flow | strong |
| `#oxoo` | 萌 | `#oxooo` | 芽 | sprout as the inner body of incipient motion | `#oxoox` | 茁 | vigorous sprouting as its visible enactment | moderate |
| `#oxox` | 長 | `#oxoxo` | 根 | root as the inner support of growth | `#oxoxx` | 滋 | nourishing increase as growth in action | moderate |
| `#oxxo` | 轉 | `#oxxoo` | 軸 | axis as the inner condition of turning | `#oxxox` | 旋 | rotation as turning made active | provisional |
| `#oxxx` | 續 | `#oxxxo` | 緒 | thread-end or beginning as the basis of continuation | `#oxxxx` | 繼 | succession as continuation performed | strong |
| `#xooo` | 緣 | `#xoooo` | 由 | the cause-path or source of relation | `#xooox` | 牽 | relation as active pulling or linkage | strong |
| `#xoox` | 通 | `#xooxo` | 渠 | channel as the inner basis of passage | `#xooxx` | 達 | arrival or reaching-through as passage enacted | strong |
| `#xoxo` | 會 | `#xoxoo` | 契 | tally or accord as the inner basis of meeting | `#xoxox` | 合 | joining as meeting enacted | strong |
| `#xoxx` | 繫 | `#xoxxo` | 綱 | main cord or governing thread of linkage | `#xoxxx` | 維 | sustaining tie as linkage held active | strong |
| `#xxoo` | 兆 | `#xxooo` | 象 | visible image as the basis of an omen | `#xxoox` | 占 | divination as reading the omen | strong |
| `#xxox` | 趨 | `#xxoxo` | 向 | direction as the inner orientation of tendency | `#xxoxx` | 赴 | going toward as tendency enacted | moderate |
| `#xxxo` | 變 | `#xxxoo` | 故 | prior condition as what change departs from | `#xxxox` | 更 | renewal or replacement as change enacted | strong |
| `#xxxx` | 史 | `#xxxxo` | 記 | record as the inner substrate of history | `#xxxxx` | 述 | narration as history transmitted | strong |

This table should be read as a hypothesis, not as a closed doctrine.  The
strong rows reuse pairs that already survived the older R5 readability audit
and still fit the current prefix face.  The provisional rows are where the
current prefix table changed the base face and the old one-bit pair no longer
followed.

## Why These Repairs

`生` replaces old `動` at `#oooo`, so the old R5 pair `力 / 作` is no longer the
best default.  `力 / 作` says power and enactment of motion.  The current face
is earlier: `物 x 幾`, birth or generation before organized motion.  `種 / 育`
therefore fits better:

```text
種 = generation held as seed/source
育 = generation carried forward as nurture
```

`轉` replaces old `發` at `#oxxo`, so the old pair `蓄 / 啟` also shifts.  It
fits `發`: reserve and opening.  It does not directly fit the current matrix
law of `轉` as swap/turn.  `軸 / 旋` is more exact:

```text
軸 = the axis or pivot that makes turning possible
旋 = turning as active rotation
```

`繫` replaces old `系` only orthographically.  The pair `綱 / 維` remains good:
both are cord/system words, and `維` is already close to sustaining and
holding-together.

## Operator Side

An odd-band overlay should not repeat a prefix-specific operator rule blindly.

The `n = 2` prefix has a special operator audit because:

```text
R4 = End(R2)
```

So a prefix word can be read as both a cell and a 2 x 2 matrix.  The one-bit
odd-band extension does not have that same canonical endomorphism reading.  Its
honest default operator reading is the same-rank mask action:

```text
@m(s) = m xor s
```

The canonical operator vocabulary should therefore be generated from coordinate
atoms, not from the 32 cell glyphs above:

| mask | operator | reading |
|---|---|---|
| `@ooooo` | 恒 | identity mask |
| `@xoooo` | 改 | toggle the first inherited prefix bit |
| `@oxooo` | 化 | toggle the second inherited prefix bit |
| `@ooxoo` | 變 | toggle the third inherited prefix bit |
| `@oooxo` | 臨 | toggle the fourth inherited prefix bit |
| `@oooox` | 易內 | toggle the appended residual bit |

Composite masks should stay explicit unless a compound is genuinely stable:

```text
@oxxoo = 變化
@xoxoo = 改變
@oooxx = 臨+易內
@xxxxx = 改+變化+臨+易內
```

This is the main structural difference from the prefix matrix audit.  There,
the same glyph can often carry the `#` and `@` reading because the matrix law is
visible.  In the odd-band extension, cell glyphs such as `種 / 育 / 徑 / 履`
name states.  Operator glyphs such as `改 / 化 / 變 / 臨 / 易內` name mask
actions.  A future environment may still define `@育` or `@履`, but that would
be an additional named operation, not the default consequence of the address.

## Lexicon Sketch

An experimental `n = 2` odd-band cell lexicon could be written as data.  The
actual candidate file also includes structural aliases such as `內本·生`, so
both the coordinate and the proposed single glyph are available:

```wen
名
  #ooooo 內本·生 種
  #oooox 內征·生 育
  #oooxo 內本·行 徑
  #oooxx 內征·行 履
  #ooxoo 內本·化 質
  #ooxox 內征·化 革
  #ooxxo 內本·流 源
  #ooxxx 內征·流 衍
  #oxooo 內本·萌 芽
  #oxoox 內征·萌 茁
  #oxoxo 內本·長 根
  #oxoxx 內征·長 滋
  #oxxoo 內本·轉 軸
  #oxxox 內征·轉 旋
  #oxxxo 內本·續 緒
  #oxxxx 內征·續 繼
  #xoooo 內本·緣 由
  #xooox 內征·緣 牽
  #xooxo 內本·通 渠
  #xooxx 內征·通 達
  #xoxoo 內本·會 契
  #xoxox 內征·會 合
  #xoxxo 內本·繫 綱
  #xoxxx 內征·繫 維
  #xxooo 內本·兆 象
  #xxoox 內征·兆 占
  #xxoxo 內本·趨 向
  #xxoxx 內征·趨 赴
  #xxxoo 內本·變 故
  #xxxox 內征·變 更
  #xxxxo 內本·史 記
  #xxxxx 內征·史 述
```

The matching operator lexicon is a generated mask vocabulary:

```wen
名
  @ooooo 恒
  @xoooo 改
  @oxooo 化
  @ooxoo 變
  @oooxo 臨
  @oooox 易內
```

Composite operator names can be added as aliases, but the atom list above is
the important part.

## Test Result

The `n = 2` odd-band overlay appears to be useful only if we treat it as a
one-bit residual split:

```text
even-prefix face -> inner basis / inner expression
```

That is not a proof that Chinese characters are secretly an R-tower.  It is a
more disciplined test: the table is constrained by one new binary axis, and
bad pairs become visible quickly.  The strongest evidence is not the existence
of 32 nice words; it is the repeated noun/action pairing:

```text
徑/履, 質/革, 源/衍, 緒/繼, 由/牽,
渠/達, 契/合, 綱/維, 象/占, 故/更, 記/述
```

The weak points are also clear:

```text
種/育, 軸/旋, 芽/茁, 根/滋, 向/赴
```

Those need corpus checks before becoming a default CJK lexicon.  For now the
formal result is only the all-scale split, specialized at `n = 2`:

```text
R (2*n + 1) ~= R (2*n) x Bool
```

where the extra `Bool` is read as `內` in this overlay.  The lexicon result is
a candidate half-layer, not active semantics.  The paired closure is the next
even rank, where the second residual bit is added; see
[`r5-r6-inner-outer-rationale.md`](./r5-r6-inner-outer-rationale.md).
