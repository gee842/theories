---
name: 人类命运共同体 形式证完成 (2026-05-07)
description: Foundation/Core/Renlei.lean — 三轴 community model + iff 充要刻画 + 四相收口
type: project
originSessionId: 858e08c8-dc07-40e1-b988-8bda67574672
---
On 2026-05-07, `Foundation/Core/Renlei.lean` (~276 lines, 21 declarations) was added — the formal证 for 人类命运共同体. Companion .md report at `四级生成_太极两翼四象八卦/人类命运共同体_共同体之证.md`. Total project jobs: 2834 (was 2833).

**Why:** The phrase 人类命运共同体 has only 「人类」「共」「同」 as registry atoms (命/运/体 are NOT in the atom table). The证 reconstructs it via existing字根: 人类命运共同体 = 道 ⊕ 人类 = (共开 ∧ 共续 ∧ ¬夺共续) restricted to G «人». This is a first-light reification of `R «道»`'s sense formula「正续 + 非夺共续 + 共开」 (Roster.lean:440) from string annotation to Lean Prop.

**Structure (Bool³ community state):**
- aligned (1,1,1) → realizes TrueDao
- isolated (0,1,1) → fails (lost 共开)
- severed (1,0,1) → fails (lost 共续)
- seized (1,1,0) → fails (夺共续 holds)
- iff theorem: TrueDao ↔ g = aligned (8-state enumeration)

**Witnesses:** 0 sorry / 0 axiom; registry membership by native_decide; deps by rfl; failure modes by Bool.noConfusion / direct application; aligned by direct construction; iff by subst.

**How to apply:**
- This pairs with O_进化非道者生存_三视证 as a dual: EvolutionDao证 σ_F's insufficiency (演化 ⊉ 道); Renlei证 共同体 sufficiency (3 axes ⟺ 道).
- Future extension points listed in §7 of the .md: multi-Focus n-human community, shenghe dynamics for gfp closure (matches RecName.«道» = .gfp), cross-link to Sincerity (反诛心 constraint on noSeizure judgment), 做人注意 alignment.
- The 8字根 deps verified by rfl give a registry-level coherence certificate; if any of those deps changes in Roster.lean, this file will catch the regression.
- Imports: SSBX.Core + Foundation.Core.Monism + Foundation.Core.HumanAlignment. No Mathlib dep.
