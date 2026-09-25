---
name: Phase A — Algebraic spine on R₇/R₈ (2026-05-10)
description: Cell128/Cell256 now carry full Add/Zero/Neg/Sub/SMul + Cayley ι/ε + 印/投 as XOR masks; origin=道=identity
type: project
originSessionId: dc179491-4360-455e-b86e-f377b6bf4de4
---
Phase A of the doctrine-alignment refactor (plan: crystalline-sprouting-cocoa.md) landed on 2026-05-10.

**What was added** in `formal/SSBX/Foundation/Bagua/Cell128.lean` (§ 6/7/8) and `Cell256.lean` (§ 7/8/9):
- `yaoXor` / `hexXor` / `Cell{128,256}.xor` componentwise XOR + 5 group laws each
- `origin = (qian, false)` for Cell128 and `(qian, dao)` for Cell256 — the V₄ identity / 道 / (Z/2)ⁿ zero
- `Add / Zero / Neg / Sub / SMul Cell{n} Cell{n}` instances (no Mathlib AddCommGroup typeclass; explicit lemmas)
- `cayley : Cell{n} → (Cell{n} → Cell{n})` regular representation + `epsAtOrigin` evaluation at origin
- Theorems: `cayley_inj`, `epsAtOrigin_cayley` (= retract law), `cayley_hom` (homomorphism)
- 印/投 rewritten as XOR masks: `yin_mask = (qian, ji)`, `tou_mask = (qian, wei)`; `yin = (· ⊕ yin_mask)`, `tou = (· ⊕ tou_mask)`
- Old `Shi.yin / Shi.tou` (V₄ wrap form) preserved in `Cell256.Shi` namespace for backward compat — new mask form lives at top-level `Cell256.yin/tou`

**Why:** doctrine yi-RO-hierarchy-v2.md treats every R-layer as a (Z/2)ⁿ abelian group with 道 as origin and Cayley fusion (R ≅ XOR(R)) as the central self-similarity. Phase A made this structure explicit in Lean rather than only documenting it.

**How to apply:** when extending downstream code (lift/project, operator semantics, R₅ Wuyao), use `(c ⊕ mask)` form for atomic operators rather than ad-hoc `(c.1, !c.2)` — it composes via the abelian group laws and lines up with Cayley `ι(mask)`.

**Status:** 0 sorry, full `lake build` clean. Phase B (YinBit dedup, Shi → abbrev) and Phase F (Cell192 deletion) still pending.
