---
name: 生生不息 / 道理 project framing
description: Foundational framing of the 生生不息 (SSBX) / 道理 (Daoli) corpus at /Users/ren/repos/生生不息/ — required to interpret the user's terse instructions correctly
type: project
originSessionId: 7ac48d64-9a82-4a7e-8052-ee6ef59f8d2c
---
The 生生不息 project at /Users/ren/repos/生生不息/ is a philosophical-computational framework where **classical Chinese (文言/wenyan) is treated as a computational kernel ≈ λ-calculus + temporal composition + aspect monad + effect**, with **名实合一 (name-reality unity) as architectural default** (no syntax/semantics 分立 presupposed).

Key correspondences:
- 之/其/所 = variables; 者 = λ-binder; juxtaposition + 之 = application
- 而 = sequential composition WITH time grain (not pure ∘); non-commutative by default
- 也/矣/既/方/将 = aspect monad markers (state collapse, perfective, past/now/future)
- 令…则… = monadic bind with effect (world-changing implication)
- 凡/必/若/故/即/是/為 = proof-syntax particles
- 易传 卦爻 = symbols-AND-categorical-objects (Curry-Howard-Lambek as default, not discovery)

**Why:** The user explicitly said "古文 ≈ λ-calc + temporal + aspect + effect" and "选 wenyan-operators 作 kernel 是 principled". Without this framing, the markdown looks like just philosophy; with it, the project is a Lean-verified, type-theoretic kernel construction with single-character expansion protocols.

**How to apply:**
- Treat .md files in 真理/ and root as formal specifications, not casual essays
- "证 X" usually means "manifest/exhibit X structurally", not "prove X via derivation"
- "常识" is ONE of three faces of 道理 (per 法则 60: 道理 ≡ 普通 ≡ 常识 ≡ 真理), specifically 知行合一
- Yesterday's work is 生生不息/*.md root files; today's distill is 生生不息/真理/daoli-v12-*.md
- Never propose verification-list documents when the user wants kernel-architecture work — listen for "核" / "kernel" / "完备" / "自指" / "expansion path" cues
- Single-character (字元) economy is enforced via T1-T6 metatheorems in v14; new terms must register, have roots, preserve type
