# R1-R4 Glyph Test Ledger

> Status: first falsification pass, not a proof.
> Companion: [`r1-r4-glyph-rationale.md`](./r1-r4-glyph-rationale.md).
> Question: are we merely fitting Chinese glyphs onto R1-R4, or is there a
> real structural affinity that constrains the mapping?

This document tests the proposed R1-R4 glyph table against external classical
usage and internal operator constraints.  The aim is not to prove that Chinese
characters historically derive from the R-tower.  That claim would be too
strong.  The aim is weaker and falsifiable:

> A candidate glyph is good only if its `#` cell reading, its `@` operator
> reading, its R-layer position, and its compound behaviour all point in the
> same direction.

If a word sounds good but fails the operator law, the table is fitting words to
math.  If a word appears in classical compounds that already express the same
cell/operator relation, the table has real evidence.

## Fixed Rules Before Testing

The rules frozen for this pass:

1. R1 is the primitive visibility distinction: `o = 隱`, `x = 見`.
2. R2 has two axes: relation/interval and activity/manifestation.
3. R2 has body readings `物 / 動 / 間 / 事` and process readings `幾 / 勢 / 機 / 時`.
4. R3 is phase/aspect under reversal `swap02`.
5. R4 is `R2(body) × R2(process)` for `#` readings.
6. R4 is `End(R2)` for `@` readings.
7. A glyph may be both `#word` and `@word`, but the role must be chosen by
   grammar or explicit marker.

## Verdict Scale

| mark | meaning |
|---|---|
| strong | source usage and operator law both support the placement |
| moderate | source usage supports the semantic field, but operator support is indirect |
| weak | plausible semantics, but current evidence is mostly our construction |
| red flag | source usage or operator law pushes against the placement |

## Test 1 — `生`

Candidate:

```text
#oooo 生 = 物 × 幾
@oooo 生 = R4 zero map / reset-to-origin
```

Evidence:

- The `#` reading is strong.  The *Xici* line "天地之大德曰生" makes `生` a
  generative cosmological value, and "生生之謂易" makes repeated generation
  central to the 易 reading.
- The phrase `生生` supports role flexibility: one `生` can naturally act as
  process/operator and the next as generated value.

Problem:

- The raw R4 matrix `@oooo` is the zero map `(a, b) ↦ (0, 0)`.  Calling this
  "generation" is only acceptable if we read it as reset-to-seed.  It does not
  itself generate visible output.

Verdict: `#生` strong; `@生` red-flag unless explicitly defined as
reset-to-source or backed by a richer native generator.

## Test 2 — `幾`

Candidate:

```text
#oo 幾 = subtle beginning before relation/activity
@oo 幾 = identity/keep-both mask at R2
```

Evidence:

- The *Xici* tradition has "幾者動之微": 幾 is the subtle trace of motion before
  manifest action.  This directly supports `幾` as pre-activity rather than as
  ordinary motion.

Operator check:

- `@oo` as identity is quiet but not contradictory.  It says the subtle
  condition is not yet an intervention.

Verdict: strong for `#幾`; moderate for `@幾`.

## Test 3 — `物 / 事`

Candidate:

```text
#oo 物 = no relation, no activity
#xx 事 = relation + activity
```

Evidence:

- The *Daxue* phrase "物有本末，事有終始" cleanly separates `物` as thing with
  structure and `事` as affair with temporal/event structure.
- This agrees with the R2 axis split: `物` can have parts without yet being an
  event; `事` has activated relation and therefore beginning/end.

Operator check:

- `@xx` toggles both axes.  As `事`, it eventuates: it turns relation and action
  on/off together.

Verdict: strong for the R2 `物/事` split.

## Test 4 — `化 / 變 / 行 / 通 / 事`

Candidate cluster:

```text
#ooxo 化 = 物 × 機
#xxxo 變 = 事 × 機
#ooox 行 = 物 × 勢
#xoox 通 = 間 × 勢
#xx   事 = relation + activity
```

Evidence:

- The *Xici* formula "化而裁之謂之變，推而行之謂之通" is a direct stress test.
  It links `化` to `變`, and `行` to `通`.
- The related line "通變之謂事" links `通 + 變` to `事`.

Operator check:

- `@化 = (a, b) ↦ (0, a)` moves one channel into another: form changes place.
- `@變 = (a, b) ↦ (a + b, a)` is an invertible 3-cycle on nonzero R2 states:
  this is a real change operator.
- `@行 = (a, b) ↦ (0, b)` selects a directed channel.
- `@通 = identity`, pass-through.

Verdict: strong.  This is the best evidence so far that the table is not just
arbitrary fitting.  The classical formula already relates these glyphs in a
way close to the R4 operator reading.

## Test 5 — `變 → 通 → 久/續`

Candidate:

```text
#xxxo 變
#xoox 通
#oxxx 續
```

Evidence:

- The *Xici* pattern "窮則變，變則通，通則久" says extremity leads to change,
  change leads to passage, passage leads to endurance.

Operator check:

- `@變` is an invertible nontrivial cycle.
- `@通` is identity/pass-through.
- `@續` is the opposite cyclic continuation through nonzero states.

Verdict: strong for `變/通`; moderate for `續`, because the text says `久`
rather than `續`.  `續` remains plausible but not directly forced.

## Test 6 — `通`

Candidate:

```text
#xoox 通 = 間 × 勢
@xoox 通 = identity
```

Evidence:

- `通` is repeatedly paired with `變` in the *Xici* tradition.
- Its operator law is exactly pass-through: `(a, b) ↦ (a, b)`.

Negative control:

- If `通` were assigned to `@oooo`, the operator would collapse all inputs,
  contradicting通 as passage.
- If `通` were assigned to a non-invertible projection, it would lose one
  channel rather than keep passage open.

Verdict: strong.  `通 = @xoox` is one of the most constrained placements.

## Test 7 — R3 Phase Words

Candidate:

```text
藏 呈 蘊 起 歸 定 斂 成
```

Evidence:

- `定` has strong general classical support as stabilization: "知止而后有定"
  places 定 after finding the stopping point.
- `幾者動之微` indirectly supports the R3 need for a middle/pivot notion, but
  not the eight chosen glyphs.
- `起/歸/斂/成` are semantically plausible as phase words, but this pass has
  not found a compact classical formula that forces exactly these eight slots.

Operator check:

- The mask-action interpretations are coherent, but that proves only internal
  consistency, not external attestation.

Verdict: mostly weak, with `定` moderate.  R3 is still a designed phase
lexicon, not yet a discovered classical system.

## Test 8 — R4 Weak Cells

The following placements are coherent but not yet externally forced:

| glyph | placement | current status |
|---|---|---|
| 萌 | 動 × 幾 | plausible: incipient motion, but needs textual support |
| 長 | 動 × 勢 | plausible: motion under tendency grows, but needs corpus support |
| 緣 | 間 × 幾 | plausible and later strong in Buddhist `緣起`, but not yet classical-core evidence |
| 會 | 間 × 機 | plausible: meeting at a pivot, but needs source support |
| 繫 | 間 × 時 | plausible: relation over time, but source support pending |
| 兆 | 事 × 幾 | plausible: event-sign, but source support pending |
| 趨 | 事 × 勢 | plausible: trend/tendency, but source support pending |
| 史 | 事 × 時 | conceptually strong, but not yet backed by a classical formula in this pass |

Verdict: weak-to-moderate.  These are candidates, not closed choices.

## Current Result

The table is not uniformly validated.

Strong cluster:

```text
生 (# only so far), 幾, 物, 事, 化, 行, 通, 變
```

Moderate cluster:

```text
勢, 機, 時, 定, 續
```

Weak / needs testing:

```text
藏, 呈, 蘊, 起, 歸, 斂, 成,
萌, 長, 緣, 會, 繫, 兆, 趨, 史
```

Red flag:

```text
@生 = @oooo
```

If `生` is allowed as an operator, the matrix law alone gives reset-to-origin,
not visible generation.  That may be philosophically acceptable, but it is not
the same as ordinary generative action.  This needs either a narrower gloss
("return to generative seed") or a richer native operator.

## Conclusion

The evidence does not support the strong claim "Chinese characters are the
R-tower."  It does support a narrower claim:

> A classical Chinese process cluster around 生 / 幾 / 化 / 行 / 通 / 變 / 事
> aligns unusually well with the R2/R4 cell/operator distinction.

That is enough to continue, but not enough to freeze the whole R1-R4 lexicon.
The next tests should target the weak cells with corpus evidence and negative
controls before we put them into an active default-like lexicon.

## Sources Checked

- [Chinese Text Project, *Zhouyi / Xici Xia* parallel passages](https://ctext.org/text.pl?if=gb&node=46943&show=parallel)
  for "天地之大德曰生".
- [Chinese Text Project dictionary entry for 裁](https://ctext.org/dictionary.pl?char=%E8%A3%81&if=gb),
  containing "化而裁之謂之變，推而行之謂之通，舉而錯之天下之民，謂之事業".
- [Chinese Text Project, *Book of Changes: Xi Ci II* parallel passage](https://ctext.org/text.pl?if=en&node=46969&show=parallel)
  for "幾者動之微".
- [Chinese Thought terminology note](https://www.chinesethought.cn/shuyu_show.aspx?shuyu_id=3688)
  for "窮則變，變則通，通則久".
- [Shidian classical-text entry](https://www.shidianguji.com/mid-page/7352264678808207398)
  for "物有本末，事有終始".
