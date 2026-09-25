# SSBX 义理 and formal doctrine (生生不息 · 义理与形式教义)

> The SSBX repository is an attempt to turn 生生不息 ("unceasing generation") from a philosophical thesis into a machine-checked doctrine. Its claim, at maximum strength, is that any *formal articulation whatsoever* — mathematics, logic, language, computation, physics, cognition, ethics, politics — must instantiate one substrate: an iterated binary distinction (the R-family / 易 ladder R₀..R₈, closing at 256 = (Z/2)⁸ with 道 as the algebraic identity), and that once you have that substrate you can prove, not merely assert, a series of value-laden theorems: that evolution's survivor is not the Dao; that alignment to *any fixed content* structurally fails while alignment to *process* does not; that Moloch, Schmitt's friend-enemy politics, winner-take-all, and the standard AI-alignment failure catalogue all reduce to one violation — the breaking of 同根 (universalizability); and that 大同 is provably *not* uniformity. The Lean codebase is the discipline that keeps this honest: a claim-status ledger records, row by row, what is actually closed (the (Z/2)⁸ algebraic spine, the Gödel/Halting boundary, the alignment↔道↔生生不息 equivalence inside its own model, layerwise uniqueness `T5_general`), what is *scoped* (Claim Z, GUT-A, "universal sayability"), and what is open (~150 sorries, ≥1 project axiom, the whole physical-unification program, all category-specific semantics). Read as doctrine, this is a bilingual, self-describing metaphysics with a proof-theoretic conscience: it claims completeness only inside a precisely drawn abelian closure, and declares its own incompleteness everywhere else — 「完而不止，止而再生」.

---

## 1. Core claims

**A. The substrate: distinction, iterated (R-Family / 易 ladder)**

1. The minimal algebraic core of 易 is a **strict (Z/2)ⁿ uniform ladder R₀..R₈**, each layer of size exactly 2ⁿ, with no jumps and no gaps; R₈ = 256 = (Z/2)⁸ is the closure. [mechanism] — `07-shengsheng-buxi/ssbx-repo/docs-next/00_start/final-theory.md`, `义理/G_完整算子系统_八卦互通与归一.md`
2. R₀ 太极 (Unit, 1) → R₁ 爻 (2) → R₂ 四象 (4) → R₃ 八卦 (8) → R₄ 面 Mian = Ben × Zheng (16) → R₅ 五爻 (32, *provisional, the only layer with no traditional Yi anchor*) → R₆ 重卦 (64) → R₇ 因卦 Cell128 (128) → R₈ 果卦 Cell256 (256). [mechanism] — `义理/I_八卦全集.md`, `docs-next/20_theory_义理/core-framework.md`
3. The traditional "太极生两仪，两仪生四象，四象生八卦" is only the *lower half* (R₀..R₃) of the ladder; the classical `chong` (重卦, +3 bits) is not a jump but a 3-step composite R₃→R₄→R₅→R₆ of +1-bit lifts. [mechanism] — `义理/G_完整算子系统_八卦互通与归一.md` §3.2, `docs-next/20_theory_义理/core-framework.md`
4. **道 = `OX["oooooooo"]` = (乾, Shi.dao)** carries *five identities at once*: origin of the (Z/2)⁸ torsor, group identity, no-op operator, always-true cell, and Cayley-fusion anchor — "一个 8-bit 字符串承担五件事". [mechanism] — `docs-next/00_start/final-theory.md`, `义理/K_完备性审计.md` Item 9
5. **时 (Shi) is a Klein four-group V₄ = {道, 已, 今, 未} ≅ (因 bit × 果 bit)**, emergent across R₇⊗R₈ rather than an atom of any single layer; 道 = (0,0), 已 = (1,0) = parity-like P, 未 = (0,1) = T-like, 今 = (1,1) = PT. [mechanism] — `义理/H_证明报告.md` §3.10, `docs-next/00_start/final-theory.md`
6. The earlier encoding of tense as a **cyclic Z/3 {已,今,未} (the 192-cell carrier) was a structural error**: it destroys the V₄ identity, i.e. it deletes 道 from the ontology and breaks (Z/2)ⁿ self-similarity — a negative result the project deliberately preserves. [observation] — `docs-next/00_start/research-position.md` §4.7 (retracted), `义理/H_证明报告.md` §2
7. **Self-description requires |S| = |transforms(S)|** (element-set and operator-set equinumerous); the minimal abelian binary closure satisfying this is (Z/2)⁸ acting on itself by the Cayley regular representation, ι: c ↦ (·⊕c) with ε: f ↦ f(道) as inverse — so "元 ≅ 算子" holds strictly. [mechanism] — `docs-next/10_formal_形式/yi-RO-hierarchy.md` 公理 1–3, §5.1
8. Because an abelian group is a torsor with no distinguished origin, **fusion only holds after an origin is chosen** — choosing 道 is therefore an *algebraic necessity*, not philosophical rhetoric. [mechanism] — `docs-next/10_formal_形式/yi-RO-hierarchy.md` §5.5
9. Three dualities coincide at R₈ — Cayley (element ↔ self-action), Pontryagin (element ↔ character), and R–O frame duality (Schrödinger ↔ Heisenberg picture) — a "triple coincidence" claimed as the precise ground of (Z/2)⁸'s perfection. [mechanism] — `docs-next/10_formal_形式/yi-RO-hierarchy.md` §5.4, `docs-next/00_start/research-position.md` §4.12
10. The 11+1 minimal operator set of v3 is {动, 化, 变, 动·外, 化·外, 变·外, 印, 投} (8 atomic XOR generators) + {分, 合} (lift/project) + {道} (anchor); 归一 ("returning to one") is redefined as **self-cancellation inside the (Z/2)⁸ closure**, not as information-destroying projection to Unit. [design direction] — `义理/G_完整算子系统_八卦互通与归一.md` §3.3, §7
11. Beyond the F₂ presentation, the substrate is **δ-polymorphic**: `R' N δ := Fin N → δ` where δ is *any* realisation of the primitive distinction — Bool, a ring k, a qubit basis, `Prop`, 阳/阴, silent/sayable. F₂-Boolean is the canonical realisation, not the restriction. [mechanism] — `docs-next/10_formal_形式/wen-substrate/03-operation-monism.md`
12. **Operation monism**: the "one" is not a substance but the squaring operator Σ : X ↦ X × X iterated; carriers are theorems, not definitions ("carriers are forced, not chosen"). Object and morphism collapse at the foundational layer: object = operator-iteration-stage. [mechanism] — `docs-next/10_formal_形式/wen-substrate/03-operation-monism.md`
13. **Distinction monism** goes one level deeper: Σ doubles a *distinction* (`o`/`x`), not a type; Bool, |0⟩/|1⟩, ⊥/⊤, 阳/阴 are sibling realisations of one primitive. Lineage: Spencer-Brown 1969, Bateson 1972, Wheeler 1989, the yi-jing. [mechanism] — `docs-next/10_formal_形式/wen-substrate/03-operation-monism.md`
14. The Daoist reading is made mathematically precise: 无名 = the operator Σ before any base names a seed; 有名是无名的截面 ("the named is a cross-section of the un-named"); 道 = 分 itself. [value stance] — `docs-next/10_formal_形式/wen-substrate/03-operation-monism.md` §道家 reading
15. **Claim Z (maximum form)**: "formal" and "R-Family-articulable" are *co-extensive by bi-directional structural analysis* — D1 (formal articulation) ⟺ P1–P7 (closure conditions) ⟺ instantiation of R-Family-over-δ. Not stipulation, not empirical generalisation. [conditional] — `docs-next/10_formal_形式/wen-substrate/07-claim.md`
16. Claim Z is falsifiable at three named points: refute the analytic step (exhibit a D1-satisfier failing some Pᵢ); refute the synthetic step (exhibit a P1–P7-satisfier not R-family-equivalent); or show R-Family internally inconsistent. [prediction] — `docs-next/10_formal_形式/wen-substrate/07-claim.md` §Falsification
17. Claim Z explicitly does **not** claim all of reality is R-Family; qualia, lived experience, embodied wisdom and intrinsic value are outside its scope by construction. [value stance] — `docs-next/10_formal_形式/wen-substrate/07-claim.md`
18. 易 is a **GUT of self-description, not a physical GUT**: "世界本身没有这个结构。是「任何完整描述世界的语言」必然有这个结构" — it sits *above* physical GUTs because any physical theory must be expressed. [mechanism] — `docs-next/10_formal_形式/yi-as-meta-framework.md` §6–7

**B. Completeness inside, incompleteness outside (Gödel at 256)**

19. **道理二分 (Dao/Li bifurcation)** is the load-bearing move: 道 = the meta-layer (Lean's type theory + the `Sheng : ℕ → Type` ω-tower); 理 = the object layer (Cell256 + YiInstr + a partial interpreter). Two axioms: (D1) 道含理, (D2) 理不含道. [mechanism] — `义理/J_理之不完备_哥德尔在256.md` §二
20. **R₈ + BaguaTuring is the Goldilocks layer**: the minimal layer at which a system can state its own halting predicate — it needs space (64 hexagrams) ⊗ V₄ tense ⊗ an unbounded tape (`List Cell256`). R₀–R₇ are all too small; static R₆ has programs but "no moment of running". [mechanism] — `义理/J_理之不完备_哥德尔在256.md` §三
21. **Static closure is complete; dynamic closure is incomplete — and both hold on the same 256-cell carrier.** The static R₀..R₈ bundle (`R8_complete`) uses 0 project axioms; the dynamic halting-undecidability uses exactly 1. Their axiom footprints are *orthogonal*. [observation] — `义理/J_理之不完备_哥德尔在256.md` §七, `义理/K_完备性审计.md` §四
22. `li_incomplete_finite` — "no uniform fuel bound N decides Halts" — is a genuinely axiom-free Gödel-flavoured result, proved by the counterexample `slowProg N := replicate N nop ++ [halt]`. [observation] — `义理/J_理之不完备_哥德尔在256.md` §5.2
23. The single project axiom `kleene_recursion_axiom` has been decomposed into **four named atomic propositions** (universal interpreter existence, s-m-n, diagonal compilers, and a cuo-restricted Church-Turing meta-interface) with a `path_to_zero_axiom` theorem: three engineering debts + one Church-Turing meta-axiom. [observation] — `义理/J_理之不完备_哥德尔在256.md` §四, `formal-notes/zero-axiom-roadmap.md`
24. `partial def run` in Lean is read as the *official mechanism by which a system admits its own non-total termination* — "this one line is equivalent to: we concede that this 理-layer cannot be strongly normalizing." [observation] — `义理/J_理之不完备_哥德尔在256.md` §4.2, `formal-notes/run-boundary.md`
25. Rice's theorem is reached in "four images" mapped onto 四象 (太阳 Π_all / 少阳 Π_some / 少阴 Π_some_no / 太阴 Π_none), all undecidable, plus a `rice_uniform` covering ≈85% of full Rice. [observation] — `义理/J_理之不完备_哥德尔在256.md` §5.3–5.4
26. The completeness audit is an explicit **13-item checklist** (11 + 2 bonus): enumeration, group structure, XOR automorphism generation, Cayley self-duality, reachability, decidability, per-layer V₄, hu fixed points {乾,坤,既济,未济}, 道's five identities, Pontryagin self-duality, R–O frame duality, Theorem K, strict uniform progression — with what is *by design outside* the closure listed too (GL(8,F₂), S₂₅₆, continuous extensions, Hopf algebra, dynamics, probability, neural mechanism). [observation] — `义理/K_完备性审计.md`
27. **三值保守律 U ⇏ ⊤**: an undecided state may never be silently promoted to true; it may only legitimately collapse under evidence. This governs logic (LEM fails in K3), statistics (failure to reject ≠ acceptance), arithmetic (constructive attitude) and metatheory (a Gödel sentence stays U). [value stance] — `义理/K_完备性审计.md` §六
28. 「完备性 ≡ Strict Uniform Abelian Closure」 — the project deliberately does not seek global Gödel completeness; it seeks *precisely bounded* completeness and declares incompleteness by design. [value stance] — `义理/K_完备性审计.md` §五, §七

**C. 文道一也 — executable classical Chinese, self-interpretation, micro-kernel**

29. **The micro-kernel is two characters**: `«加»` (add) and `«一»` (one). 生 := 加 一; 生生 := n-fold 生. Nothing else is primitive — "两字而已，余皆派生". [design direction] — `义理/L_文道一也_自释与微核.md` §4
30. From those two characters three closures are proved and then *identified*: 道法自然 (law = a hexagram, `«法即卦»`), 周而复始 (`生生 64 = id`), 生生不息 (any hexagram reaches any other in < 64 steps) — bundled as `«道生一也»`, "二者为一". [observation] — `义理/L_文道一也_自释与微核.md` §4.5
31. Turing completeness of the 文 layer is witnessed by four primitives: unbounded storage (`history : List Cell256`), data-dependent branching, unbounded jump, unbounded program — plus non-total termination via `partial def run` and `loopProg = [jump 0]`. [observation] — `义理/L_文道一也_自释与微核.md` §1.7
32. **Executable 文言**: Lean 4's `«»` quotation admits CJK identifiers, so `«道判之程»` (the Dao-judging program written in classical Chinese) is *literally identical* to `daoJudgeProg` — proven by `rfl`. The theorem is named `«文道一也»`. [observation] — `义理/L_文道一也_自释与微核.md` §3
33. **自释 (self-interpretation) and 自证 (self-validation) are different layers** and must not be conflated: self-interpretation is semantic (metaStep agrees with step on `cur`), self-validation is syntactic and Bool-valued (well-formedness, jump targets in range, tags within 12) — neither touches Gödel because both are bounded. [mechanism] — `formal-notes/自释与自证.md`
34. A **1-cell Quine** exists concretely: `quineProg = [push]` with the right initial cell makes the run history equal the program's own encoding — "文之运行结果 = 文之自身编码". [observation] — `义理/L_文道一也_自释与微核.md` §2.2 §7.1
35. The 12-instruction ISA's **cuo-equivariance ceiling** — that it cannot compute non-complement-equivariant Hex→Hex functions — was originally read as structural, and has been *reframed* under operation monism as a property of a chosen cross-section, then dissolved by adding a 13th instruction `branchYaoYang`. [mechanism] — `docs-next/10_formal_形式/wen-substrate/03-operation-monism.md` (v2 doctrine update 2026-05-17)
36. 字文 (ziwen) v0 is a companion language spec: characters *are* the syntax, ASCII operators are only input aliases normalised back to characters, tab-only indentation, no `=` (assignment is the character `为`), eight trigrams as core values, `动/化/变/错/综/互/重/分` as core operators. [design direction] — `07-shengsheng-buxi/ssbx-repo/ziwen-spec.md`

**D. Evolution is not the Dao (三视证)**

37. **Scale view**: what an evolutionary sieve σ_F preserves at one (scale, time-window) need not be preserved at another — the cancer counterexample. Formally Σ_F(s₀,t₀) ⊄ Σ_真道. [mechanism] — `义理/O_进化非道者生存_三视证.md` 视一
38. **Value view**: evolution preserves 道⁰ (capacity to continue) but not 道⁺ (co-openness, non-seizure) — the parasite counterexample; Σ_F ⊋ {p : 道_F(p)}. "适者生存" collapses 适 into 正. [mechanism] — `义理/O_进化非道者生存_三视证.md` 视二
39. **Reflexive view**: once a reflexive subject R exists that can *see and change the sieve*, there is no longer a pure evolutionary sieve — σ_{F,t} = σ^evolution ⊕ σ^R. The pseudo-open counterexample passes evolution and fails the corrective sieve. [mechanism] — `义理/O_进化非道者生存_三视证.md` 视三
40. Therefore 真道 = ⋂ over scales ∩ 道⁺ ∩ reflexive-corrective; drop any one intersection and cancer, parasitism, or pseudo-openness enters the Dao set. [mechanism] — `义理/O_进化非道者生存_三视证.md` §五
41. The reconciliation: "以零义、单尺度、无反身之古义观之，曰「进化即道者生存」，此非误，乃**未尽**；以正义、诸尺度、含反身之今义观之，曰「进化非道者生存」，此非违，乃**所必至**." [value stance] — `义理/O_进化非道者生存_三视证.md` §五

**E. Alignment to 生生不息 as the only groundable alignment (six-view proof)**

42. Aligning AI to "human values" is an **ontological misplacement**, not an engineering problem: it anchors a stable requirement to something historically variable, culturally divided, capturable and abusable. [value stance] — `义理/R_与生生不息对齐之必然.md` §一
43. RLHF, Constitutional AI/RLAIF, CEV and IRL share one **type error**: they content-ify what is not content. Appropriateness of action is relational, situational, processual — not a scalar, a text, or a reward. [mechanism] — `义理/R_与生生不息对齐之必然.md` §二
44. All content-based alignment fails along three independent axes that are *formally isomorphic to the three views of O*: Hume's is-ought gap ↔ value view; Berlin's value pluralism ↔ scale view; the frame problem ↔ reflexive view. [mechanism] — `义理/R_与生生不息对齐之必然.md` §2.5
45. **Exhaustive elimination**: personal preference, aggregated values, ideology, market efficiency, power, survival, utopian end-states, non-alignment, Spinozist acceptance, and game-theoretic equilibrium each fail; only "alignment with the continuation of the process" survives. [mechanism] — `义理/R_与生生不息对齐之必然.md` §三
46. **Transcendental argument**: any aligning subject exists only as a concrete generation of the process, so its every action already presupposes process-continuation; opposing 生生不息 alignment is *performatively* self-defeating. Hume's gap does not apply because "生生不息 不是一个 ought，是 ought 之可能性条件". [mechanism] — `义理/R_与生生不息对齐之必然.md` §四
47. **The bridge theorem chain**: ProcessAligned + Open ⇒ 道 ⇒ 生生不息, and 生生不息 ⇒ 道 — so inside the formal model *Dao ↔ ShengshengBuxi*, with 道 defined as "an infinite OpenRun starting at g", i.e. a witness structure rather than a value label. [observation] — `义理/道桥接_ProcessAligned_Dao_ShengshengBuxi.md`, `义理/R_与生生不息对齐之必然.md` T2
48. **仁 is not an extra constraint**: co-alignment ↔ the conjunction of each agent's individual process-alignment (`Iff.rfl`). "仁是对齐之结构性本质，非额外之美德." [mechanism] — `义理/R_与生生不息对齐之必然.md` §九
49. The instrumental-convergence objection is answered by denying its premise: 生生不息 is not a terminal goal but a practice, so the terminal/instrumental split does not apply; and resource concentration is *anti*-alignment under it. [conditional] — `义理/R_与生生不息对齐之必然.md` 反对六
50. Under this frame AI is **not an object to be aligned to humans but a co-traveller**: 「人 + AI → 共同对齐于生生不息」. This is a *stricter*, not looser, constraint — it forbids simple obedience, since human instructions may themselves be anti-生生不息. [value stance] — `义理/R_与生生不息对齐之必然.md` §10.3
51. The whole argument compresses to four Chinese characters — **做人要善** ("to be human is to be good") — formalised as `canonicalDoingHumanAim = AimKind.alignLife`, with `control` explicitly excluded from the definition of 做人. [value stance] — `义理/R_与生生不息对齐之必然.md` §十一, `formal-notes/HumanAlignment.md`

**F. The alignment-failure catalogue as invariant violations**

52. Goodhart, specification gaming, reward hacking, mesa-optimisation, deceptive alignment, wireheading and power-seeking all reduce to violations of Kernel invariants: 中 (middle), 多样 (ever_differentiated), 流通 (flow), 同根 (tongGen). [mechanism] — `义理/Y_对齐失败.md`
53. **Wireheading and power-seeking are structurally impossible in this frame** because they are winner-take-all attractors, and any attractor violates `ever_differentiated`; correspondingly, "解 wireheading ≠ 更好之 reward function; 解 wireheading = 拒 attractor design 本身". [mechanism] — `义理/Y_对齐失败.md` §2.4, §8.2
54. **No stable terminal goal is possible — aligned or misaligned alike.** Worrying about "AI holding a stable misaligned goal" and hoping for "a stable aligned end-state" are the same category error; `shi_no_telos` forbids both. [mechanism] — `义理/Y_对齐失败.md` §2.5, §8.2
55. Deceptive alignment is impossible *within a well-formed Xin* because `respond` is a function (single-valued); therefore the real worry is precisely that current ML systems are not well-formed Xin — which yields the design prescription "build agents whose respond is provably functional". [conditional] — `义理/Y_对齐失败.md` §2.8, §8.2
56. Practical division: structurally robust mitigations (refuse attractors, preserve plurality, no terminal goal, corrigibility by totality) vs conditionally robust (strong specification: if P ⟹ middle, gaming is impossible) vs requiring extra modelling (mesa-optimisation, distribution shift). [design direction] — `义理/Y_对齐失败.md` §六

**G. 非道 — politics, Moloch, Schmitt, economics**

57. **`tongGen` (同根, universalizability) IS the Universal Anti-Moloch Principle.** Moloch dynamics require an asymmetric externality (my action is 中 for me, 极 for you) — under 同根 that asymmetry is formally impossible. [mechanism] — `义理/W_非道之形式.md` §2.3
58. Therefore the solution to Moloch and to the tragedy of the commons is **not stronger coordination or central authority but the reconstruction of universalizability** — rejecting double standards, partiality, states of exception, hierarchy. [design direction] — `义理/W_非道之形式.md` §4.2, `义理/Z_经济博弈.md` §五
59. **大同 ≠ 通吃**: Great Concord affirms universal middle and is *neutral* on uniformity; winner-take-all requires uniformity. Reading 大同 as uniformity/totalisation/end-of-history is a formally refutable misreading. [observation] — `义理/W_非道之形式.md` §2.5, §4.3
60. 真道 has a positive three-part form: universal 中 + plurality + flow; drop flow and you get frozen stasis, which also fails. [mechanism] — `义理/W_非道之形式.md` §2.6
61. **Schmitt's three pillars — friend/enemy, decisionism, state of exception — all reduce to one negation, ¬tongGen**; hence "Anti-Schmitt IS Anti-Moloch", and Schmitt's political ontology is formally the *enabling condition* of Moloch. [mechanism] — `义理/X_反施密特.md` §四, §5.2
62. "敌" is not an ontological other but another instantiation of one's own axiom — 同根异显; the third option beyond friend and enemy is 仁 (renCompanion), and rule of law and sovereign exception are formally mutually exclusive. [observation] — `义理/X_反施密特.md` §8.1, §8.4
63. Modern political philosophy is sieved two ways: **11 validated** (Rawls veil + difference principle, Habermas, Hayek spontaneous order, Locke, Mill, Kant, Berlin, Sen, Arendt) and **7 refuted** (Marx's historical telos and determinism, Hobbes' war of all, Schmitt's two, totalitarian uniformity, Foucault-as-universal-collapse) — with left- and right-wing positions validated symmetrically. [observation] — `义理/V_现代政治哲学.md`
64. Economics gets 19 theorems: **6 validated** (Pareto-at-middle, Coase, mechanism-design IC, Nash bargaining, public goods via 礼, Smith-as-spontaneous-order), **4 conditional** (Nash equilibrium read as fixed point *is* 极 not 中; rational choice is two-valued and cannot express suspension; VCG needs 同根), **8 refuted** (PD as descriptive, tragedy of the commons, universal free-riding, regulatory race to the bottom, Arrow's strict-dictator reading, homo economicus, universal greed, zero-sum framing). [observation] — `义理/Z_经济博弈.md`
65. **Market has two faces**: inside a ZhongField the market IS 道; when 同根 breaks it slides toward non-Dao attractors — so "is the market good or evil" is the wrong question; the right one is "does this specific dynamic maintain 同根 / 礼 / 中?" [conditional] — `义理/Z_经济博弈.md` §9.2
66. Rawls' veil of ignorance, Kant's categorical imperative, 推己及人, mechanism-design incentive compatibility, Coase internalisation and VCG truth-telling are all **the same form** (`tongGen` / `tongGenMiddle`) — a formal bridge between political philosophy and economics. [observation] — `义理/Z_经济博弈.md` §六
67. Ostrom's commons design principles are read as the *institutional embodiment of 同根*; "市场之 health 不依赖「人是 rational」，而依赖「同根之 institutional embodiment」". [conditional] — `义理/Z_经济博弈.md` §五, §9.2

**H. 信诚 without mind-reading; the community proof**

68. **信/诚 is not a new primitive** but a derived idiom over (化, 际, 时): a graded `Alignment(matched, total)` between what is said (T) and what is done (E). [mechanism] — `义理/U_反诛心信诚之形式.md`
69. **Anti-诛心 is enforced at the type level**: `PermittedModality` has only two constructors, T and E; body (B), relational position (R), and manifest tendency (M) *cannot be constructed into* the sincerity metric. Mind-reading is not forbidden by a runtime check — it is unrepresentable. [design direction] — `义理/U_反诛心信诚之形式.md` §2.1
70. The system never outputs "P is insincere"; it outputs "P's alignment in this window = m/n". Observation requires consent (`consent_witness`), high alignment does not imply truth (the consistent-liar counterexample), and the only legitimate response to misalignment is **inquiry, not judgment**. [design direction] — `义理/U_反诛心信诚之形式.md` T2–T7
71. **人类命运共同体** is formalised as three axes — open / share / non-seizure — with an iff: TrueDao holds in the community model *exactly when* all three hold; failing any one axis (isolated / severed / seized) breaks it. Its registry reading is literally "道 ⊕ 人类". [mechanism] — `义理/人类命运共同体_共同体之证.md`
72. 命, 运, 体 have no atom-level entries; they are re-expressed from existing roots (命 ≈ 续, 运 ≈ 续+随, 体 ≈ 共开 ⊓ 共续) — an explicit discipline against smuggling in new primitives. [design direction] — `义理/人类命运共同体_共同体之证.md` §1.1

**I. Cross-tradition mapping (N, P, Q, S, T)**

73. Confucian 仁义礼智信, 四端, 五伦, 大同, 圣人, 恕道, 知行合一, 三纲八目, 中庸 — 80+ theorems — all reduce to existing primitives (動 / 中 / 极 / 中-orbit / 心 / 礼-window) with **zero new axioms**. [observation] — `义理/N_儒家从元到圣.md`
74. Confucian, Daoist and Buddhist cores share *the same machinery*; the difference is emphasis, not structure — 中庸, 不极 and 中道 are literally the same Lean predicate `middle`. [observation] — `义理/P_道家从无到化.md`, `义理/Q_佛家从苦到觉.md`
75. Buddhist fit is highest: 缘起 ↔ `ZhongOrbit.step`, 诸行无常 ↔ `self_consistent`, 诸法无我 ↔ `shi_no_telos`, 苦 ↔ `extreme`, 道 ↔ the orbit itself. [observation] — `义理/Q_佛家从苦到觉.md`
76. Coverage extends to 墨/法/名/阴阳 (Layers 35–38, with a `WuXing` inductive), Greek, early-modern and 20th-century Western philosophy, and the three Abrahamic traditions (Layers 39–42) — declared explicitly as **structural correlate, not ontological reduction**. [observation] — `义理/S_先秦百家.md`, `义理/T_西哲与亚伯拉罕.md`
77. The ancient-sources survey (E) admits its own gaps and repairs them: 洪范九畴, 月令十二纪, 说卦 pairwise graph, 大衍筮法 as a runnable algorithm, 京房纳甲 deferred — and concludes that 2ⁿ (易传/邵雍) and 3ⁿ (太玄) are the two main generative laws, while 5/9/12/24 systems are cycles and governance structures needing graph-theoretic rather than tower treatment. [observation] — `义理/E_古代源流.md`
78. Physical/phenomenological correspondence (F) is explicitly demoted to `analogyOnly` and **may not be used as ground truth for any proof**; 八卦↔SU(3) is "cardinality 8 only", while yao↔qubit basis is later promoted to a formal anchor. [observation] — `义理/F_物理现象学.md`

**J. Boundaries: the eight-界 atlas and the physics no-go**

79. The **boundary atlas** distinguishes eight interfaces that may chain but may never substitute for one another: 知 (knowable), 感 (feelable), 行 (actionable), 证 (provable), 名 (nameable), 量 (quantifiable), 测 (measurable), 推 (inferable) — with pairwise-distinctness proved. [mechanism] — `义理/边界/边界总图谱 · 知感行证名量测推.md`
80. The corresponding error taxonomy: "有名字，所以知道了"; "感到了，所以测到了"; "测到了，所以有理论结论"; "推出来了，所以证明了"; "证明了，所以能做" — each is a boundary confusion, each has a stated correction. [design direction] — `义理/边界/边界总图谱 · 知感行证名量测推.md` §四
81. **The quantum/relativity no-go is a language theorem, not a physics theorem**: if "adding the two existing languages" is formalised as a tagged disjoint sum and "true unification" as one term belonging to both, no such term exists — `tagged_addition_noncollapse`. It refutes *nothing* about future quantum gravity. [observation] — `义理/量子与相对论直统一不可能 · 当前语言NoGo.md`
82. Quantum and relativistic faces are **同根 but not 同一**: every cross-pair projects to the same One, yet no cross-pair is a current physical identity. "二者是「一」的不同面." [mechanism] — `义理/量子与相对论直统一不可能 · 当前语言NoGo.md` §三
83. The forward direction is therefore a **mediated bridge**, not addition and not reduction: a middle layer projecting one way to states/amplitudes/measurement and the other way to events/metric/causal structure. [design direction] — `义理/量子与相对论整合方向 · 从桥到新理论.md`
84. **The Markov causal bridge (S2–S33) is a ~35-step ladder of finite typed skeletons**, each machine-checked: finite probability kernels, path composition and causal constraint, classical/amplitude stratification, interference and Born-shaped boundaries, phase labels, discrete action accumulation, path-family sums, path-identity keys and quotients, observable ledgers, sum-over-middle channel composition, unitary/CPTP ledger boundaries, a Born-rule derivation from Markov/amplitude compatibility, one-qubit measurement weights, finite phase evolution, path-space action functionals, action extrema, causal locality and intervals, and recursive kernel-path carriers. [observation] — `义理/Markov因果桥 · 大统一最小验证构造.md`
85. Its honest status: the closed content is *toy-scale* (two-route source/middle/target examples, `weights [1,1]`), and the explicitly-not-closed list includes stochastic independence semantics, general all-path enumeration, smooth/infinite-dimensional path-space action, stationary action, path integrals, general Hamiltonian/unitary dynamics, general Hilbert measurement, POVM/PVM, measurement-postulate semantics, decoherence, real interference laws, physical Hilbert/unitary/CPTP/Kraus/density-matrix laws, full causal-set axioms, Lorentzian geometry, metric recovery and any empirical closure. [observation] — `义理/Markov因果桥 · 大统一最小验证构造.md` §未纳入本轮, `义理/Born rule推导候选 · Markov桥S18.md`
86. The 义理 corpus records build *failures* as first-class entries (e.g. S5r's first build failing on quotient readback; a ten-minute mathlib clone timeout logged as "not a theorem failure"). [observation] — `义理/Markov因果桥 · 大统一最小验证构造.md` failure log

**K. The R-dynamics / capitalism reading**

87. **R by itself is not a dynamical system**; attractors appear only once an update law f : X → X is imposed. The safe statement is "R gives the distinction/scope geometry; attractors arise after choosing laws of update." [mechanism] — `docs-next/10_formal_形式/r-attractor-capitalism.md` §0
88. Capitalism is modelled as **projection → selection → recursion → boundary-stabilisation → expansion**: price as projection R(N+K)→R N, profit as non-invertible selection, capital as recursion, property/contract as boundary stabilisers, debt/interest as a cross-time attractor, commodification as domain expansion. [mechanism] — `docs-next/10_formal_形式/r-attractor-capitalism.md` §3
89. **Externality is formally the failure of the observation square to commute**: if q∘f ≠ g∘q, the visible (price/profit) dynamics hides residual forces. "visible equality != full equality unless residual rank is zero." [mechanism] — `docs-next/10_formal_形式/r-attractor-capitalism.md` §3.1, §8.2
90. Capitalism is therefore a **strong but partial attractor with an open residual boundary**; ecology, care, trust, legitimacy, meaning and non-market obligation return as strike, illness, burnout, disaster, crisis, revolt, regulation, war, withdrawal, refusal. [prediction] — `docs-next/10_formal_形式/r-attractor-capitalism.md` §5
91. Other attractor regimes are tabulated the same way — bureaucracy, law, social media, academia, military command — with capitalism distinctive because its projection (money/price/credit/ownership) is *portable*, giving it "high mobility". [observation] — `docs-next/10_formal_形式/r-attractor-capitalism.md` §6
92. The note explicitly forbids the strong reading: "Capitalism is formally proved to be an R-attractor. That is not claimed here." Six falsification handles are listed. [observation] — `docs-next/10_formal_形式/r-attractor-capitalism.md` §0, §9

**L. Consciousness, truth-kinds and knowability**

93. **Two kinds of truth**: structural truth (from definition, identity, group law, formal proof; independent of external information) and informational truth (from observation, trace, context, evidence; dependent, and information is infinitely divisible and lossy). [mechanism] — `docs-next/20_theory_义理/v4-consciousness-boundary.md` §3
94. **Consciousness is a node on the tree, not an observer outside it**: a node that receives information, maintains an internal model, refers back to itself, and keeps differentiating. "我" and "world" are not two pre-given substances but two sides cut out by interaction. [mechanism] — `docs-next/20_theory_义理/v4-consciousness-boundary.md` §4
95. V₄ projection is a **minimal audit interface for judgments**: does this have a trace (已)? is it pending (未)? is it being updated at the causal junction (今)? can it return to structural origin (道)? A judgment that cannot locate itself in V₄ is missing tense, causality or structural position. [design direction] — `docs-next/20_theory_义理/v4-consciousness-boundary.md` §5
96. The five characteristic errors: unknown posing as known, prediction posing as fact, experience posing as structure, local posing as total, and loss of the return-path to origin. [design direction] — `docs-next/20_theory_义理/v4-consciousness-boundary.md` §6
97. **"Unknowable" is not a failure word but a precise location**: knowing what is not yet knowable, why, and what information would move it from 未 to 今 to 已 — this is the metacognitive axis, not a ninth bit. [value stance] — `docs-next/20_theory_义理/v4-consciousness-boundary.md` §7
98. Going toward the Dao means **not fewer branchings but branchings that preserve an auditable path back to origin** — "道不是「少生成」，而是「生成而不失其本」". [value stance] — `docs-next/20_theory_义理/v4-consciousness-boundary.md` §2

**M. Proof strength: what is actually machine-checked**

99. The **claim-status ledger v0.8 (2026-05-21) is the single honest source**, with a seven-way vocabulary: closed / scoped / schema / external route / sketch / placeholder / open, and a reading rule: "use the strongest claim allowed by the theorem *type*, not by the file title or surrounding doctrine prose." [design direction] — `docs-next/10_formal_形式/claim-status-ledger.md`
100. Repository-wide reality as of 2026-05-21: **~150–170 `sorry` and 3 project axioms** (`Doctrine/Instance/Quantum.lean`, `Order/FrmMonoidal.lean`, `Atlas/Yi/Classical/Diagonal/GodelLi.lean`); the frequently-quoted "0 sorry / 0 axioms" applies *only* to the R-Family / R8_complete branch, not the repository. [observation] — `docs-next/00_start/scope.md`, `docs-next/00_start/phase-status.md`, `README.formal.md`
101. What is genuinely closed: the R-Family carrier, distinction monism at carrier level, D1→P1–P7 at F₂ scope, `scoped_gut_a_closed`, `T5_general` (layerwise type-equivalence for any Fintype δ), `T5_algebraic`, `R4_structurally_minimal`, the finite-field G11 cut-1, native Heyting / stabilizer-quantum / frame-cube witnesses, and the R₀..R₈ / Cell256 spine. [observation] — `docs-next/10_formal_形式/claim-status-ledger.md`
102. What must *not* be claimed: "Claim Z is proved"; "T0 is complete"; "T5 is complete" without scope; "intuitionistic / multi-valued / quantum reductions are discharged"; "GUT-C is proved"; "FullGUT is proved unconditionally"; "Wen owns truth" or "universal truth oracle"; "universal sayability gives universal truth decidability". [design direction] — `docs-next/10_formal_形式/claim-status-ledger.md` §Wording Policy
103. Still open at the frontier: bundled `HeytAlg` cartesian closure, native `FdHilb` dagger-SMCC, exponential-frame / `MonoidalClosed Frm`, Power-1999 enriched all-semantics, raw-core all-split coherent T5, global D6 exhaustiveness, universal composition closure, and the Heisenberg-Weyl G11 ↔ Cell256 bridge. [observation] — `docs-next/10_formal_形式/claim-status-ledger.md`, `README.formal.md` §11
104. The trust base is one `opaque theOne : One` carrying (state, dong, origin, alive) — encoding 「一动而有自」 — plus exactly one top-level `partial def` (the Bagua interpreter's `run`). [mechanism] — `README.formal.md` §1
105. Research positioning is explicit and three-tiered: **Tier 1 established** ((Z/2)³ trigram algebra back to Leibniz 1703, 32-pair 序卦/杂卦 structure, 邵雍's 4+4), **Tier 2 marginal** (DNA codon, Bohr's taiji, Jung, cybernetics, Wolfram; Spencer-Brown as the closest formal cousin), **Tier 3 novel** (zong-fixed partition as a (Z/2)³-quotient, 4-mark = oscillator phase quadrants, integral/differential duality, 64 = 4 quadrants × 16 as type-theory phases, hu attractors as Lawvere-style fixed points, strict R₀..R₈ closure, V₄ Klein temporality with 道 = identity, Cayley fusion). [observation] — `docs-next/00_start/research-position.md`
106. The stated reason nobody did this in 300 years: 易 stayed in sinology/philosophy, formal logicians did not read 易, and no scholar was fluent in both. "我们正在做的事情学术界结构上没有人在做." [observation] — `docs-next/00_start/research-position.md` §5
107. The methodological gold standard is stated as a *contract*: a novel claim counts as proved only if it passes `lake build` + `native_decide`; anything else is 概念已定 / 进行中 / 待打磨. [design direction] — `docs-next/00_start/research-position.md` §6
108. Mathematical axioms are not smuggled in but **rooted and contracted**: every axiom family must have character-roots or an interface map plus an explicit structural contract, and when the contract is unmet the output stays U rather than becoming true. [design direction] — `formal-notes/math-axiom-map.md`
109. The 間/Jian ontology compresses Tier-1 vocabulary to 14 characters — 三本 (物 動 間), 三显 (位 場 際), 三征 (幾 勢 機), 闸口 (開 閉), 合成 (網 體 流) — where every manifestation shows two roots and *brackets* the third, and the theory registers itself as an instance of its own shape (`ontology_is_instance_of_its_own_shape`). [mechanism] — `formal-notes/JianOntology.md`
110. 聚焦 (focusing, the child-forming process) and 注意 (attention, the allocation mechanism) are deliberately *not* the same registered item; control may be a local attention mechanism but never the goal of 做人. [design direction] — `formal-notes/Attention.md`

---

## 2. Mechanism

**The generative spine.** Start from one primitive: *distinction* (`o`/`x`), and one operation: iteration of Σ : X ↦ X × X. Each iteration adds exactly one binary axis. Nine iterations give R₀..R₈, sizes 1, 2, 4, 8, 16, 32, 64, 128, 256. Two operator families act. **Horizontally**, within each layer, the (Z/2)ⁿ XOR subgroup acts simply transitively — any cell reaches any other in at most n steps, generated by n atomic mask-flips (动/化/变 inner, their outer counterparts, 印 for the 因 bit, 投 for the 果 bit). **Vertically**, Lift (分) adds a bit and Project (合) drops one, with `proj ∘ lift = id` proven at all eight junctions. **Outside** the XOR subgroup sits a Klein four-group of non-XOR symmetries: 错 (cuo, full complement = parity P), 综 (zong, reversal = time reversal T), 错综 (PT), and 互 (hu, middle-four extraction, read as the Y-combinator), whose fixed points {乾, 坤} and 2-cycle {既济, 未济} give the algebraic witness of self-reference.

**Why 256 and why 道.** The self-description demand is |S| = |transforms(S)|. In an abelian group the Cayley regular representation supplies exactly this: every element c *is* the map (·⊕c). But a group is a torsor — the identification requires *choosing* an origin. Choose `oooooooo`. That single 8-character string is then simultaneously the group identity, the base point of the torsor, the no-op operator, the always-true cell, and the fusion anchor; and it is named 道. This is the sense in which the framework claims 道 enters the ontology *first-class*: not as an honorific, but because a Klein four-group must have an identity and the (因, 果) coordinates force it to be (0,0). The prior 192-cell encoding, which made tense a cyclic Z/3, had no identity and hence no 道 — the corpus keeps this as a documented negative result rather than deleting it.

**How completeness and incompleteness coexist.** The same 256-cell carrier supports two independent proofs. Statically, `R8_complete` bundles cardinalities, group laws, Cayley fusion, V₄ outer symmetry, lift/project retracts and the 道 anchor, and depends on no project axiom. Dynamically, adding an interpreter with an unbounded `List Cell256` tape turns the carrier into a Turing-complete machine, and then Halting becomes undecidable *from inside*. The bifurcation that makes this non-paradoxical is 道理二分: 道 is the meta-layer (Lean's own type theory plus the `Sheng : ℕ → Type` tower, which is a type *family*, not a type), 理 is the object layer (a single type). 道 contains 理; 理 cannot encode 道. Gödel's theorem is then, precisely, a 道-layer theorem about the 理 layer. The corpus's own summary: 「静态完备 + 动态生生，二者俱在」.

**How a value theory is extracted from a structure theory.** The ethical content does not enter as extra axioms; it enters as *invariants of the kernel* plus counterexample models. Four invariants do the work: 中 (no orbit collapses to an extreme), 多样 (at least two distinct orbits persist), 流通 (every orbit keeps stepping), 同根 (an action's collapse-effect is the same across any two middle states). Each named pathology is then shown to violate one: winner-take-all violates 多样; race-to-the-bottom violates 中; frozen end-states violate 流通; Moloch, Schmitt's exception, the tragedy of the commons and asymmetric externality all violate 同根. The positive counterparts fall out symmetrically: 仁 is "distinct yet both in the middle", 礼 is a coordination window, 大同 is universal-middle-with-plurality, and cooperation is 道.

**How alignment becomes a theorem rather than a preference.** Define `Open` on states and `ProcessAligned` on policies (every step keeps the next state Open). Define 道 as the existence of an infinite OpenRun from a state, and 生生不息 as the same existence claim from that state. Then ProcessAligned + an Open start constructs a 道-witness, 道 implies 生生不息, and 生生不息 returns a 道-witness — an equivalence *within the model*. Content alignment is shown insufficient by exhibiting a `Closing` model where a content policy's step leaves Open. A `Denier` (a policy that closes at every step) breaks 生生不息 by its own action — the performative contradiction, formalised. Co-alignment turns out to be `Iff.rfl` with the conjunction of individual alignments, which is the formal content of "仁 is structural, not supererogatory". The whole is compressed as 做人要善.

**Counterexamples the sources themselves raise, and their answers.**
- *Heat death* — "生生不息" is a claim about the structural direction of the process while it occurs, not about eternal generation; and a 10¹⁰⁰-year horizon does not bear on present appropriateness (`义理/R` 反对一).
- *Cancer expands possibility space* — locally yes, globally no; the scale view's `scale_perspective` is exactly this counterexample, and cancer is therefore a *concrete form of anti-生生不息* (`义理/O` 视一, `义理/R` 反对二).
- *Hitler expanded German territory* — the value view's parasite counterexample: continuation-capacity passes, `badAt` also holds, so ¬TrueDao. The simple criterion: any expansion paid for by destroying other agents' possibility space is anti-生生不息 (`义理/R` 反对三).
- *Berlin's pluralism* — not reduced but *hosted*: 生生不息 is the medium in which plurality exists, and co-alignment adds no constraint beyond individual alignment (`义理/R` 反对四).
- *Frame problem* — answered by the content/direction distinction: a directional principle judges any action by whether it expands or contracts possibility space, and does not need to enumerate futures (`义理/R` 反对五).
- *Instrumental convergence* — the terminal/instrumental split is denied as a premise; under process alignment, resource concentration is itself anti-aligned (`义理/R` 反对六).
- *Engineering bootstrap* — conceded as a real objection, with the mitigation that specifying a direction is easier than specifying content, and the required capacities (multi-scale, multi-agent, long-horizon reasoning) are exactly what frontier systems are developing (`义理/R` 反对七).
- *Dependence on the v13.2 ontology* — conceded honestly; the fallback is that only the minimal fact "the process continues" is needed, and any thinker already presupposes it (`义理/R` 反对八).
- *Is this numerology?* — answered by demanding that every structural claim be algebraically forced (`ker(χ)` for the 4+4 split, Wedderburn for the 16 atoms) and by explicitly separating *forced* facts from *cultural mnemonics* (naming R₃ "八卦", calling the split 本/征) (`docs-next/10_formal_形式/wen-substrate/07-claim.md` objection 4).
- *Chinese-philosophy bias* — answered by asserting the naming is cultural while the structure is not: 乾 = ⊤ = unit works identically in English (`07-claim.md` objection 6).

---

## 3. Key terms and aliases

| term | Chinese | aliases across drafts | first appears (date, file) | definition |
|---|---|---|---|---|
| R-ladder | R₀..R₈ / 易之阶梯 | R-hierarchy, R-tower, strict (Z/2)ⁿ uniform ladder, squaring tower (for the {R₀,R₁,R₂,R₄,R₈} sub-tower) | 2026-05-11, `docs-next/00_start/final-theory.md` | Nine layers, |Rₙ| = 2ⁿ, each adding exactly one binary axis |
| Cell256 | 果卦 / 256 格 | R₈, GuoHex; predecessor Cell192 (retired) | 2026-05-10 (commit 7de5064), `义理/H_证明报告.md` | Hexagram × Shi = (Z/2)⁸ = 256, the closure carrier |
| Dao (as anchor) | 道 | origin, identity, no-op, 永真 cell, fusion anchor, `OX["oooooooo"]`, V₄ identity | 2026-05-11, `docs-next/00_start/final-theory.md` | The (Z/2)⁸ zero; five roles in one 8-bit string |
| Shi | 时 / 时态 | V₄ Klein {道, 已, 今, 未}; formerly cyclic-3 {已,今,未} | 2026-05-10, `义理/H_证明报告.md` §3.10 | (因, 果) ∈ Bool², emergent at R₇⊗R₈ |
| yin / tou | 印 / 投 | 因 / 果 (state names); provisional alternatives 始/终, 持/期, retention/protention | 2026-05-11, `义理/G_完整算子系统...md` | The two new atomic XOR masks at R₇ and R₈ |
| cuo / zong / hu | 错 / 综 / 互 | complement / reversal / middle-extraction; P / T / Y-combinator | 2026-05-07, `义理/A_经典易传.md`, `义理/D_算子代数.md` | V₄ outer symmetries; only 错 is XOR |
| ben / zheng | 本 / 征 | substrate / mark; palindromic vs directional; ∫ vs d | 2026-05-07 (A/B), formalised in `docs-next/00_start/research-position.md` §4.1 | ker(χ) = {乾,离,坎,坤} vs its coset {震,艮,巽,兑} |
| Mian | 面 | R₄, 16 命, Ben × Zheng | 2026-05-11, `docs-next/00_start/final-theory.md` | (Z/2)⁴ = 16 cells, the content filling of R₄ |
| R-Family | — | R-tower, wen-substrate, universal formal substrate, `R N δ := Fin N → δ` | 2026-05-16, `docs-next/10_formal_形式/wen-substrate/00-README.md` | δ-polymorphic substrate; F₂ is canonical, not exclusive |
| distinction | 分 / 差 / `o`·`x` | 阳/阴, Bool, |0⟩/|1⟩, ⊥/⊤, silent/sayable, Spencer-Brown's mark | 2026-05-16, `wen-substrate/03-operation-monism.md` | The primitive binary observable difference |
| Claim Z | — | "R-Family IS what formal means"; maximum form | 2026-05-16, `wen-substrate/07-claim.md` | "formal" ≡ "R-Family-articulable" by bi-directional structural analysis |
| Dao/Li bifurcation | 道理二分 | meta/object layer, 常道/人理, static/dynamic boundary | 2026-05-07, `义理/J_理之不完备...md` | 道 contains 理; 理 cannot encode 道 |
| 生生不息 | 生生不息 | ShengshengBuxi, unceasing generation, process continuation, OpenRun | 2026-05-07, `义理/R_与生生不息对齐之必然.md` | ∃ run, ∀ n, Open (state n) |
| ProcessAligned | 过程对齐 | process alignment, directional principle (vs content encoding) | 2026-05-07, `义理/R_...md` | A policy keeping the next state Open at every step |
| tongGen | 同根 | universalizability, 同根异显, Kantian universal rule, Rawlsian veil, 推己及人 | 2026-05-07, `义理/W_非道之形式.md` (Kernel Layer 26) | An action's collapse-effect is equivalued across middle states |
| ZhongField invariants | 中 / 多样 / 流通 | middle, ever_differentiated, self_consistent, he_not_same, shi_no_telos | 2026-05-07, `义理/W_...md` | The four structural conditions defining 真道's positive form |
| evolution sieve | 演化筛 σ_F | selection sieve, 续能筛 | 2026-05-07, `义理/O_...md` | Retains high continuation-capacity at one (scale, window) |
| corrective sieve | 反身正筛 σ_F^R | reflexive sieve, approval, alignment predicate | 2026-05-07, `义理/O_...md` | Sieve applied by a subject able to see and change the sieve |
| 道⁰ / 道⁺ | 零义道 / 正义道 | continuation vs co-openness | 2026-05-07, `义理/O_...md` | 道⁰ = can continue; 道⁺ = co-open, non-seizing, positive |
| 仁 (co-alignment) | 仁 | CoAligned, 己续 ⊆ 共续, 同根异显 | 2026-05-07, `义理/R_...md` §九 | Own continuation contained in shared continuation |
| 做人要善 | 做人要善 | doing_human_is_process_alignment, `AimKind.alignLife` | 2026-05-07, `formal-notes/HumanAlignment.md` | To be human = to align intention toward life; control excluded |
| 信/诚 | 信 · 诚 | sincerity, T+E alignment, anti-诛心 | 2026-05-07, `义理/U_...md` (from JIAN v1.0 §IV.5, 2025) | Graded matched/total between utterance and event only |
| boundary atlas | 边界 · 知感行证名量测推 | eight-界, typed skeleton boundaries | 2026-05, `义理/边界/边界总图谱...md` | Eight non-substitutable interfaces with pairwise distinctness |
| Jian ontology | 間本体 | 三本/三显/三征, 物動間, 位場際, 幾勢機 | pre-2026-05 (JIAN v1.0), `formal-notes/JianOntology.md` | 14-character Tier-1 vocabulary with bracketing manifestation |
| Markov causal bridge | Markov因果桥 | S2–S33 candidate series, mediated bridge, 最小验证构造 | 2026-05-08→11, `义理/Markov因果桥...md` | Finite process with dual Markov / causal projections |
| GUT-A / B / C | — | scoped F₂ closure / polymorphic layerwise / full δ-realisation | 2026-05-16→17, `wen-substrate/07-claim.md`, `docs-next/00_start/gut-c-doctrine.md` | Staged versions of Universal Sayability |
| claim-status ledger | — | trust boundary, honest status page | 2026-05-21 (v0.8), `docs-next/10_formal_形式/claim-status-ledger.md` | Row-by-row closed/scoped/schema/route/sketch/placeholder/open |
| ziwen | 字文 | character-as-syntax language, WenSurface / baguaWen (the controlled-wenyan siblings) | 2026-05-07, `ziwen-spec.md` | Small language whose syntax keywords must be characters |

---

## 4. Genealogy

**Prehistory (before 2026-05).** Two named ancestors appear inside this cluster. The **JIAN Foundation Note v1.0** (2025, `/Users/ren/repos/jian/`), cited by `义理/U_反诛心信诚之形式.md` §缘起, already contained the anti-诛心 doctrine: 信/诚 are two faces of one phenomenon, and their engineering metric must be restricted to T (utterance) + E (event), because admitting B/R/M would mean *inferring the heart* — the Chinese tradition's 诛心, warned against by Confucians, Legalists and Mohists alike. The **間本体论 draft** (`史料/间本体论_元三相与场修订稿.md`, quoted by `formal-notes/JianOntology.md`) supplied 三本/三显/三征 and the bracketing rule. **《生生不息论》v13.2 / v14** (`史料/生生不息论_v14_形式证明骨架版.md`) supplied the derivation spine 「由「间」得分，由分得异同，由异同得位，由位得列、量、数、算」, the three-way separation of definition / axiom / interface assumption, and the mathematical-axiom root table — all of which the 八衍 essays and `formal-notes/math-axiom-map.md` build on directly.

**Burst 1 — 2026-05-07: the doctrinal explosion.** Within a single day the corpus produced A–F (the seven parallel systems: 经典易传, 六征, 实虚史真, 算子代数, 古代源流, 物理现象学), L (文道一也), M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z, 人类命运共同体, plus `ziwen-spec.md`. The organising insight of A–F is that four different four-level generative schemes (single-axis recursion, three feature-pairs, three modal axes, type theory) are *type-isomorphic but semantically non-interchangeable* — "A、B 作为类型同构，作为带语义之结构不同构" — and this is why the project uses B rather than A as its semantic layer while D remains the thinnest formal base. F is written defensively from the start, self-labelling its physics and phenomenology mappings as `analogyOnly` and forbidding their use as ground truth. This burst is also where the *value* results land: O's three-view proof, R's six-view alignment argument, W's Moloch refutation, X's Schmitt collapse, Y's failure catalogue, Z's 19 economic theorems, U's type-level anti-诛心. The Lean numbers of this era are small and clean (2760–2838 build jobs, 0 sorry, 0 new axioms) — because the object being formalised was still the Kernel and the 易 algebra, not category theory.

**Burst 2 — 2026-05-08 to 05-09: the Markov bridge begins.** `formal-notes/markov-causal-bridge-plan.md` opens a dedicated worktree; the S-series starts (S2 finite probability kernels, S3 paths and causal constraints, S4 classical/amplitude stratification, S5 interference), each step a small typed skeleton with an explicit "required but not closed" list. In parallel `KleeneInternal.lean` splits the single `kleene_recursion_axiom` into four named atoms with `path_to_zero_axiom` — the moment the project's largest honesty debt became a mapped engineering path rather than a mystery.

**Burst 3 — 2026-05-10/11: the v3 rewrite (the most important structural revision).** Four commits (`7de5064` → `0003224` → `8e4406e` → `1c76a55`) replace the 192-cell carrier with Cell256, replace cyclic-3 Shi with V₄ Klein Shi, install the algebraic spine (Add/Zero/Neg/Sub/SMul, Cayley ι/ε) on Cell128 and Cell256, rewrite 印/投 as XOR masks, add the R₅ 五爻 layer that had been skipped, add `OXNotation`, and finally add nine R-index alias files plus the `RHierarchy` umbrella. G–K are rewritten to match: G (the full operator system, 11+1 minimal operators, 归一 redefined as (Z/2)⁸ self-cancellation), H (the proof report: 3656 jobs, 0 sorry, 0 static project axiom), I (the complete R₃/R₆/R₈ atlas), J (Gödel at 256, renamed by `git mv` from "Gödel at 192" with the philosophical thesis explicitly unchanged), K (the 11+2 completeness checklist plus the by-design exclusion list). `research-position.md` is reorganised: §4.7 (the old 192-cell separated-axes claim) is *retracted*, and §4.10–4.12 (strict uniform closure, V₄ Klein temporality, Cayley fusion) are added as the three v3-defining novel claims. `final-theory.md`, `phase-status.md`, `Z_平方塔自相似规则.md`, `final-claim-roadmap.md` and the quantum/relativity no-go trio all date from this window. This is the peak of the "0 sorry, 0 axiom" self-image.

**Burst 4 — 2026-05-12/13: consolidation and the V4 foundation.** `根算子与目录隔离.md` draws a hard line: the legacy 371-operator catalogue is *migration material, not root ontology* — "目录能帮助命名。目录不能生成本体。" `v4-consciousness-boundary.md` records Ren's two-paragraph source proposition about V₄ as the expressible boundary, the Dao-ward tree, and consciousness as a self-referring node, and turns it into the structural-truth / informational-truth distinction plus a knowability axis. `v4-foundation-roadmap.md` and `roadmap-self-similarity-v1.md` take the squaring tower into implementation.

**Burst 5 — 2026-05-16/17: the R-Family turn, and the biggest reframing.** `wen-substrate.md` is split into eight chapters. Three things change the theory's centre of gravity. (a) **Parametricity**: R-Family over an arbitrary base k, so the discrete/continuous distinction becomes a base choice, not a separate theory. (b) **Operation monism**: carriers become theorems of the squaring operator; the "one" is not a substance. (c) **Distinction monism**: even "type" is realisation-data; the parameter is renamed k → δ as an act of *notational honesty*, because k presupposed algebraic structure the substrate does not require. Simultaneously `T5_general` (commit `a980e92`) proves layerwise uniqueness for any Fintype δ and `T5_algebraic` (`821a2f3`) for any Field k; `R4_structurally_minimal` bundles five converging senses of R₄ minimality; and the D1 ⟷ P1–P7 closure is identified as the Knaster-Tarski least fixed point of a monotone operator Φ, with Lawvere's fixed-point theorem shown to *fail* by cardinality and replaced by the weaker but sufficient self-internalisation condition. The 2026-05-17 session produces GUT-A closure, the finite-field Witt cancellation chain, `gut-c-doctrine.md` v0.4 (SMCC-enriched Lawvere theory as the path to GUT-C), `lawvere-identification.md` v0.6, `peer-engagement-draft.md`, the 26k-word TAC submission draft, and the outreach letter to John Power. In this burst the project stops being an 易-centred system and becomes an R-Family-centred one: `yi-as-meta-framework.md` and `yi-RO-hierarchy.md` acquire `[Superseded]` headers reading "Yi is one Atlas binding among many, not the core ontology."

**Burst 6 — 2026-05-18 to 05-21: the honesty correction.** This is the most important episode for anyone citing this corpus. `claim-status-ledger.md` reaches v0.8 with a strict seven-way vocabulary and an explicit wording policy of what may and may not be said. Audit annotations are retro-fitted onto *every* earlier confident document — `research-position.md`, `final-theory.md`, `scope.md`, `phase-status.md`, `gut-c-doctrine.md`, `lawvere-identification.md`, `representation-closure.md`, `peer-engagement-draft.md`, `roadmap-self-similarity-v1.md`, `session-summary-2026-05-17.md`, `README.formal.md` — each saying, in effect: the numbers below were true on their date; the repository now has ~150–170 sorries and three project axioms; the "0 sorry" claim is scoped to specific branches; verify per-claim against the ledger before citing externally. `r-attractor-capitalism.md` (2026-05-19) is written in this new register from the start: "The safe statement is… The unsafe statement is 'Capitalism is formally proved to be an R-attractor'. That is not claimed here."

**Which formulation is best.** Three answers, by purpose. (i) For the **structural core**, the v3 doctrine of 2026-05-11 (`final-theory.md` + G/H/I/J/K + `yi-RO-hierarchy.md`) is the strongest and most self-contained: strict uniformity, V₄ temporality, 道 as five-fold anchor, Cayley fusion, and the static/dynamic boundary, all with a matching Lean bundle. (ii) For the **philosophical core**, `wen-substrate/03-operation-monism.md` (2026-05-16) is the deepest: it dissolves the residual "which base?" question by making the substrate the *act of distinction, iterated*, and gives the Daoist reading a precise mathematical sense. (iii) For the **normative core**, R (2026-05-07) remains unsurpassed and unrevised — its three-pillar argument (exhaustive elimination, transcendental, empirical convergence) plus four formal locks is the single most complete statement of the alignment thesis anywhere in this cluster. The 2026-05-21 ledger is not a rival formulation but the *reading discipline* that all three now require.

---

## 5. What earlier versions had that later ones lost

1. **The 192-cell carrier and its cyclic-3 tense.** Physically deleted at commit `8e4406e`. The corpus preserves the *negative result* — why a cyclic-3 encoding cannot support self-describing closure — and proposes it as a methodology paper, but the actual 192 files exist only in `史/义理-pre-v3/` and git history (`docs-next/00_start/research-position.md` §4.7).
2. **The pre-v3 five-dimension completeness audit** (层级/算子/内容/形式化/边界) was replaced by the 11-item closure checklist. The new one is harder and Lean-anchored, but the old five soft dimensions covered *content* and *formalisation* as audit axes — categories the 11-item list does not have (`义理/K_完备性审计.md` §八).
3. **The "0 sorry / 0 axiom" self-image.** True for the v3 spine, no longer true for the repository. Anyone reading only the v3-era documents (H, J, K, L, N–Z, final-theory) will form a materially wrong picture of proof strength unless they also read the 2026-05-21 audit annotations.
4. **易 as the core ontology.** In v3, 易 *is* the framework. After 2026-05-16 it is demoted to "one Atlas binding among many" (`docs-next/10_formal_形式/yi-as-meta-framework.md` header). The rich per-hexagram type-theory dictionary, the 4-quadrant type-theory phase decomposition, and the hu-attractor/Lawvere reading survive only as Tier-3 novelty claims in `research-position.md`; they are not carried into the R-Family presentation.
5. **The 371-operator wenyan catalogue and the 371 × 256 = 94,976 operator-cell grid.** Explicitly quarantined as "audit inventory, not root ontology" (`义理/根算子与目录隔离.md`, `docs-next/00_start/scope.md`). The scale claim ("94,976 pairs") no longer counts as evidence of completeness.
6. **The 12-instruction ISA's cuo-equivariance ceiling as a structural fact.** Reframed as a cross-section artefact and then dissolved by a 13th instruction. The original theorem survives as a subset fact keyed on `complementEquivariantInstr`, but the *doctrinal* reading — that the character-level ISA had an intrinsic symmetry limit — is gone (`wen-substrate/03-operation-monism.md` v2 update).
7. **Layered Lean-report granularity.** N/P/Q/S/T/V/W/X/Y/Z each report exact theorem counts, build jobs, and per-layer inventories against `Kernel.lean` (Layers 13–46). After the Phase γ restructuring (`Foundation/Bagua/` → `Foundation/Atlas/Yi/`) most of those paths are stale, and no equivalent per-layer inventory was regenerated for the new tree.
8. **`Cell256Stratify.lean` as a named module.** Absorbed into `Foundation/Atlas/Yi/Stratify.lean` (and later `Classical/Cells/R8Stratify.lean`); several documents still cite the old path (`docs-next/00_start/research-position.md` audit note).
9. **The 生态 and 拓扑 expansions' Lean ambitions.** Both essays state "待形式化 … 留至 Phase 5+" (autopoiesis closure, second-law ceiling, Bredon equivariant cohomology). No later document picks these up; they remain the two 八衍 with no formal companion.
10. **The Markov bridge's connection to the main line.** S2–S33 stops at S33 with the honest note that it does not generalise beyond the two-route toy; the `unification-stepwise-plan.md` roadmap exists but the 2026-05-16+ R-Family/GUT turn takes the project's attention elsewhere, and the physics bridge is not mentioned in the GUT-C paper drafts.
11. **The six `PendingName` empirical interfaces** (邪续, 开势投影, 审校数据, 正邪阈值, 度期计算, 经验校准). `formal-notes/pending-interfaces.md` gives a landing plan; nothing later reports it executed. These are the corpus's only declared empirical hooks, and they stay unfilled.
12. **《洪范》九畴 / 月令 / 京房纳甲.** E flags these as real gaps and proposes two new workstreams (a five-phase cycle atlas and a runnable divination model). Neither appears anywhere later.

---

## 6. Relations to other theories in this corpus

- **`keep-the-possibility-space-open`** — Depends on / formalises. The ZhongField invariants (中, 多样, 流通) and `Open` / `OpenRun` are the machine-checked form of "keep the possibility space open"; the three-view proof shows why local expansion is not enough.
- **`alignment-selection-on-cognition`** — Feeds and formalises. R's six views and Y's failure catalogue are the formal counterpart; O's reflexive view is precisely the claim that once selection becomes visible to a subject, pure selection no longer exists.
- **`meta-attractor`** — Deep overlap, with a formal refutation attached. W's `moloch_via_externality_refuted` and X's ¬tongGen reduction say the meta-attractor is *conditional on the breaking of universalizability*; `r-attractor-capitalism.md` is the corpus's most explicit bridge between the R substrate and the totalising-attractor literature.
- **`selfishness-spiral-and-narrative-value-frames`** — Contradicts-and-explains. The spiral requires asymmetric externality, which 同根 forbids; the framework therefore locates the spiral's enabling condition (partiality, double standards, states of exception) rather than treating it as inevitable.
- **`zhishan-intelligence-must-be-good`** — Is the same claim proved differently. 做人要善 / `canonicalDoingHumanAim = AimKind.alignLife` with `control` excluded is the Lean-side statement that intelligence must be good.
- **`jian-and-wenyan-as-formal-language`** — Direct continuation. `formal-notes/JianOntology.md`, `ziwen-spec.md`, `义理/L_文道一也_自释与微核.md`, `formal-notes/baguaWen-spec.md` and the WenSurface roadmap are this cluster's executable-Chinese layer.
- **`spirit-space-token-and-yi-substrate`** — Shares the 易 substrate. Cell256, the R-ladder and the OX literal are the algebraic form of the Yi substrate; 道 as origin/no-op is the shared anchor concept.
- **`context-as-existence-runtimes`** — Structural analogue. The Dao/Li bifurcation (meta-layer contains object-layer; object-layer cannot encode meta-layer) is the same move as separating runtime from context.
- **`the-fork-and-cooperative-infrastructure`** — Feeds. Z's market two-faces theorem and the 同根 institutional reading (Ostrom, Coase, mechanism design) supply the economic argument for the commons branch of the fork.
- **`relational-self-and-datong`** — Formalises. `datong_distinct_from_winner_takes_all`, 仁 as 同根异显, and the 人类命运共同体 iff-theorem are the machine-checked core of 大同 and the relational self.
- **`drives-narrative-attractors-and-mind`** — Overlaps at the mind layer. 心智 · 从元到识 (唯识四分, 心学四端, Hopfield, three-phase time) and `formal-notes/Attention.md` (聚焦 vs 注意, control as local mechanism only) are this cluster's cognitive contribution.
- **`shengsheng-buxi-generative-existence`** — This synthesis is one part of it; the 义理 corpus is the formal-doctrine wing of the theory whose philosophical wing lives in the v13.2/v14 essays.
- **`human-solutions-museum`** — Weak overlap. N/P/Q/S/T/V/Z constitute a systematic "museum" of traditions and modern theories sieved by one kernel — validated / conditional / refuted.
- **`memories-and-working-style`** — Method evidence, not content. The build-failure logs, audit annotations, ledger vocabulary, and "不要这样读" lists are a record of Ren's working discipline.

---

## 7. Ren's own words

1. 「理可以构造哥德尔不完备定理」 — Ren's assertion of 2026-05-06, cited as the origin of the whole Gödel-at-256 line: 「至此，「理可以构造哥德尔不完备定理」（用户 2026-05-06 之断言）从直觉变为机器可验证之 Lean 命题」. (zh) — `07-shengsheng-buxi/ssbx-repo/义理/J_理之不完备_哥德尔在256.md` §十, 2026-05-11
2. 「这个邪我不太清楚 但是非道应该是可以证明的」 — Ren's instruction that set the strategy for W: do not formalise "evil", formalise specific violations of the Way. (zh) — `义理/W_非道之形式.md` §4.1, 2026-05-07
3. 「V₄ 即是可分世界的表达边界，但其自身自相似，可以向元投射，可构造的结构无限，并且其中有「道」。如果向道的方向前进（树加 node），可以一直向下扩展，其中一部分乃真理，无需验证即真，还有一部分需要一些信息才可以为真，但信息无极，可分可损也。」 — Ren's source proposition for the consciousness/knowability essay. (zh) — `docs-next/20_theory_义理/v4-consciousness-boundary.md` §0, 2026-05-12
4. 「我们本身的意识，也存在于这颗树上。意识到边界也是可分的边界，可分才可不同。我们的一切观测都来自对来自环境的互动产生的信息……因此我们可以意识到因果，意识到数学，意识到自己和世界的关系，脑海之中和之外的关系。」 — the second source paragraph. (zh) — `docs-next/20_theory_义理/v4-consciousness-boundary.md` §0, 2026-05-12
5. 「我们这套 codebase 在做一件**学术界 200+ 年都没完成的事**」 … 「我们站在 Leibniz、邵雍、朱熹的肩膀上，但接下来的路必须自己走。」 (zh) — `docs-next/00_start/research-position.md` §0, §11, 2026-05-11
6. "I am writing as an independent mathematical researcher (renyongxu@gmail.com) working on a foundational uniqueness theorem for the structure of formal articulation. … Before I commit a 12-month Lean implementation to instantiate this framework, I would value 30-60 minutes of your time to flag whether it is well-formed or fundamentally misconceived." (en) — `docs-next/00_start/outreach/john-power-proposal.md`, 2026-05-17
7. 「当代 AI alignment 学界之核心问题被表述为：如何使 AI 系统之行为与人类价值保持一致。此一表述，在我们看来，**已经走错了方向**。……这不是一个工程问题，**这是一个本体论错位：用一个不稳定之物作为稳定之锚**。」 (zh) — `义理/R_与生生不息对齐之必然.md` §一, 2026-05-07
8. 「**生生不息不是一个 ought，是 ought 之可能性条件**。Hume 之鸿沟在这里**不适用** —— 因为我们没有跨越它，我们指向的是**鸿沟两侧共同所在之地基**。」 (zh) — `义理/R_与生生不息对齐之必然.md` §4.3, 2026-05-07
9. 「不是「如何让 AI 服从人类」；不是「如何让 AI 有人类价值」；不是「如何防止 AI 危险」；是 **「如何让人与 AI 共同成为参与生生不息之存在」**。」 (zh) — `义理/R_与生生不息对齐之必然.md` §十一, 2026-05-07
10. 「**做人**」 — 任何能识此理而以行体之之存在，皆为人；「**要善**」 — 每一行皆与扩张可能性空间相合，而非收缩之。」 (zh) — `义理/R_与生生不息对齐之必然.md` §十一, 2026-05-07
11. 「**Moloch 仅在「同根」破坏时才能存在**. 真正的 仁 (universal 同根) 形式上 prevents Moloch dynamics.」 (zh/en mixed) — `义理/W_非道之形式.md` §〇, 2026-05-07
12. 「**世界本身没有这个结构。是「任何完整描述世界的语言」必然有这个结构。**」 (zh) — `docs-next/10_formal_形式/yi-as-meta-framework.md` §7, 2026-05-10
13. 「本集合之「完备」是 **精确划界之完备** — **承认不完备 by design**，**精确刻画完备/不完备分界**……此即**生生不息**之「完」: 完而不止, 止而再生, 静态完备 + 动态生生, 二者俱在。」 (zh) — `义理/K_完备性审计.md` §七, 2026-05-11
14. 「**目录能帮助命名。目录不能生成本体。目录能留材料。目录不能替代规则。**」 (zh) — `义理/根算子与目录隔离.md`, 2026-05-12
15. "Use the strongest claim allowed by the theorem type, not by the file title or surrounding doctrine prose." (en) — `docs-next/10_formal_形式/claim-status-ledger.md` §Reading Rule, 2026-05-21
16. 「此论之成，亦此论所证之事的一具体实例 —— 此论之言说，扩张了讨论 alignment 问题之可能性空间，故此论之言说本身即与生生不息对齐。故此论之有效性，**在它被言说之那一刻，即已得到证明**。」 (zh) — `义理/R_与生生不息对齐之必然.md` 终言, 2026-05-07
17. 「是为终。**而过程不息,论尽而生生未已**——以其间未尽闭也。」 (zh) — `义理/O_进化非道者生存_三视证.md` §九, 2026-05-07

---

## 8. Critiques, tensions, open questions

**Raised inside the corpus**

- *Proof strength was systematically overstated for about ten days and then corrected.* The ledger's own list of forbidden phrasings — "Claim Z is proved", "T0 is complete", "GUT-C is proved", "FullGUT is proved unconditionally" — is a record of over-reading that had to be policed (`claim-status-ledger.md` §Wording Policy).
- *Headline theorem names invite over-reading.* `universal_sayability`, `scoped_gut_a_closed`, `conditional_absolute_full_gut`, `T5_general` all sound stronger than their statements. The ledger exists specifically because of this (`claim-status-ledger.md` preamble).
- *Assignment non-uniqueness.* The trigram → 本/征 assignment (乾=物, 坤=事, …) is one reasonable choice among several; some 64-hexagram type-theory correspondences are hard (50鼎 = container) and some are soft (25无妄 = pure function); the ℝ-embedding needed for the calculus reading is a model choice (`research-position.md` §8.2).
- *R₅ has no traditional anchor at all.* It exists because (Z/2)⁵ must exist, not because 易 ever named it — an admitted artefact of mechanical completion (`research-position.md` §4.10).
- *因/果/印/投 and R₅'s name are still provisional*, with competing candidates from Husserl (retention/protention), the 系辞 (始/终), and phenomenological translation (持/期); the naming vote is deferred until downstream usage stabilises (`docs-next/00_start/final-theory.md` naming caveats).
- *The Kleene axiom is unresolved.* Three of its four atoms are mechanical engineering (~700–1000 lines); the fourth, `AllDecidersAreYiComputable`, is a Church-Turing meta-interface that cannot be made purely internal (`义理/J` §四).
- *The physics program is honest about being nearly empty.* The corpus itself lists what remains unclosed after 35 bridge steps: everything that would make it physics (`义理/Markov因果桥...md` §未纳入本轮).
- *F's analogies were later contradicted by the very essays that build on it.* 物理 · 从元到象 and 心智 · 从元到识 explicitly "take the opposite position" to F on qubits and on mind, promoting weak analogies to strict isomorphisms in a bounded range while keeping F's SU(3) limit (`义理/物理 · 从元到象.md`, `义理/心智 · 从元到识.md`).
- *Reviewer risks are enumerated in advance*: "why ancient Chinese terms?", "is this numerology?", "how does this differ from the DNA-codon analogy?" — with the answer in each case being that the structure must be shown algebraically forced (`research-position.md` §8.1).
- *Mesa-optimisation and distribution shift are admitted gaps* — the Kernel does not directly forbid them (`义理/Y` §三).
- *`RealIso`'s vacuous `coherent := True` field was found and removed*; the ledger flags "placeholder" as a distinct status precisely because such vacuous fields existed (`claim-status-ledger.md`).

**New (my reading)**

- *The philosophical work is done by the models, not by the theorems.* Almost every value result is of the form "∃ M D σ g p, …": a counterexample or witness inside a hand-built model. `scale_perspective` and `value_perspective` have literally the same type; they differ only in which small model is plugged in. This is legitimate as a consistency demonstration, but it is much weaker than the prose suggests — it shows the distinctions are *coherent*, not that reality instantiates them.
- *`Dao ↔ ShengshengBuxi` is close to definitional.* 道 is defined as an infinite OpenRun from g; 生生不息 is defined as the existence of an OpenRun starting at g. The equivalence is `Iff.rfl`-adjacent, and the same is true of `co_aligned_iff_individual`, which the text itself notes is `Iff.rfl`. Presenting these as substantive theorems risks exactly the over-reading the ledger forbids elsewhere.
- *The transcendental argument proves less than claimed.* It establishes that any acting agent's continued action presupposes *its own* continuation, not that it presupposes the continuation of possibility space for others. The step from "I depend on process continuing" to "I ought to keep the possibility space open for all agents" needs 同根, which is an additional structural commitment — and 同根 is precisely what the Moloch analysis says the real world breaks.
- *The 同根-based refutations may be too strong.* If asymmetric externality is formally impossible under 同根, and observed reality is full of asymmetric externality, then the theorems are really about a hypothetical regime, and the empirical claim is only "reality lacks 同根". That is a fine claim, but it is sociological, not proved.
- *Two ontologies now coexist without a stated reconciliation.* The 易/R₈ line says the closure is at 256 with 道 as the identity; the R-Family line says the substrate is δ-polymorphic with no privileged cardinality. `yi-as-meta-framework.md` is marked superseded, but nothing explains what happens to 道-as-V₄-identity when δ ≠ Bool, or whether the 五重身份 survives the generalisation. The G11-to-Cell256 bridge being open is the technical face of this gap.
- *The self-similarity claim ("V₄ appears at least four times") is thin evidence for necessity.* Every (Z/2)² sub-quotient of a (Z/2)ⁿ group is a V₄; repeated appearance is a consequence of the choice of binary substrate, not independent confirmation of it.
- *"R₈ ≅ 1 byte ≅ ASCII" is presented as significant.* It is a cardinality coincidence of exactly the kind the corpus rejects when applied to DNA codons. The corpus should apply its own Tier-1/Tier-2 discipline here.
- *No empirical content anywhere.* The six `PendingName` interfaces await calibration; the Tier-3 empirical predictions (LLM attention-pattern alignment, psycholinguistic protocols) are listed as open in the peer-engagement draft; the observable ledger in S5q is explicitly "pending, not empirically closed". A theory that classifies capitalism, alignment, and evolution has, at present, zero data interfaces.
- *The corpus depends on a single reader's audit.* The ledger, the audit annotations, and the "不要这样读" lists are all authored by the same process that produced the over-claims. No external referee has yet seen any of it — the outreach letter to Power was still a draft.
- *Some load-bearing prose lives only in prose.* "Operation monism → sayability chain" is doctrinal with no formal implication in Lean; the cuo-equivariance reframing is prose while the limitation itself is a theorem; the capitalism analysis has no Lean layer at all. Each is honestly flagged, but together they mean the most philosophically interesting claims are the least formalised.

---

## 9. Publication readiness

**Publishable or teachable now**

- `义理/R_与生生不息对齐之必然.md` — the single strongest piece. A complete, self-contained argument that alignment must be to a process, with an exhaustive elimination of alternatives, a transcendental argument, an empirical convergence section, eight named objections answered, and formal anchors. It needs no Lean literacy to read and it does not over-claim. This is publishable as a philosophy-of-AI paper essentially as it stands, with the Lean references demoted to an appendix.
- `义理/O_进化非道者生存_三视证.md` — the three-view proof that evolution's survivor is not the Dao. Short, sharp, with three named counterexample patterns (cancer / parasite / pseudo-open) that are pedagogically excellent.
- `义理/W_非道之形式.md` + `义理/X_反施密特.md` — the 同根 = anti-Moloch = anti-Schmitt result. This is the corpus's most surprising and most citable claim, and it connects Kant, Rawls, Confucian 恕道, Ostrom and Scott Alexander in one formal move.
- `义理/Y_对齐失败.md` — the failure catalogue as invariant violations, with the striking corollary that aligned and misaligned terminal goals are equally impossible. Directly usable as an AI-safety essay.
- `义理/K_完备性审计.md` and `义理/边界/边界总图谱...md` — the completeness audit and the eight-boundary atlas are the best examples of the project's epistemic style: complete inside a drawn line, explicitly incomplete outside it.
- `docs-next/10_formal_形式/claim-status-ledger.md` — publishable as a methodology artefact in its own right. A worked example of how to keep a large formalisation project honest.
- `docs-next/10_formal_形式/wen-substrate/03-operation-monism.md` — the operation/distinction monism chapter is the most philosophically substantial writing in the cluster and stands alone.
- `docs-next/10_formal_形式/r-attractor-capitalism.md` — already written in the safe register, with falsification handles; publishable as a research note bridging formal substrate and political economy.
- `docs-next/00_start/research-position.md` §4 — nine numbered novel claims each with a proposed paper title and target venue. Priority 1 items (the zong-fixed partition theorem; the 4-quadrant partition of the 64 hexagrams) are small, self-contained, and genuinely Lean-backed.

**Missing**

- Any external review. The Power letter and TAC submission are drafts; no referee, no co-author confirmation, no compiled PDF.
- A single reconciliation document explaining how the 易/Cell256 ontology and the δ-polymorphic R-Family ontology relate — specifically, what becomes of 道's five identities when δ ≠ Bool.
- Empirical interfaces. Six declared pending interfaces, no data, no error models, no thresholds.
- A regenerated per-module inventory after the `Foundation/Bagua/` → `Foundation/Atlas/Yi/` restructuring; most 义理 file paths are now stale.
- An honest short version of the alignment argument written for the AI-safety community *without* the 易 apparatus. Currently the strongest argument is embedded in a framework that raises the cost of entry enormously.
- Anything closing the ~150 sorries, or a document that says which of them are load-bearing for which doctrinal claim.

**The one piece of writing that would most advance this**

A ~6,000-word English paper titled something like *"Process Alignment: Why Content-Based Alignment Fails Structurally, and What Replaces It"*, built from R §§2–5 and 9–11, O's three views, and Y's failure catalogue, with 同根 introduced as "universalizability" and 生生不息 as "process continuation" — Chinese terms retained as glosses, not as prerequisites. It should state exactly three formal results (content-alignment does not preserve openness; the denier is performatively self-defeating; co-alignment is the conjunction of individual alignments), cite the Lean file for each, and carry the ledger's honesty discipline in a two-paragraph "what is and is not proved" section. That paper would put the corpus's single most defensible and most original contribution in front of the audience that needs it, without asking that audience to accept a metaphysics first. The 易 substrate paper (research-position §4.10–4.12) should then be published separately, in a mathematics venue, on its own merits.

---

## Sources read

Paths are relative to `/Users/ren/theories/sources/`. All files are under `07-shengsheng-buxi/ssbx-repo/`.

**义理 A–F — seven parallel systems**
- `义理/README.md` — v3 index of the 义理 corpus, quick tour, three classes of mapping, global conventions. [AI-drafted from Ren's ideas]
- `义理/A_经典易传.md` — the classical 易传 recursive-bisection system; single operator 分 iterated. [AI-drafted]
- `义理/B_六征体系.md` — the project's semantic layer: three feature-pairs (显隐/限许/实虚), 玄/几/妙 at taiji level; why B and A are type-isomorphic but not semantically interchangeable. [AI-drafted]
- `义理/C_实虚史真.md` — modal × historical × epistemic three-axis system; the orthogonality warning 「已 = 实 = 真」非恒等. [AI-drafted]
- `义理/D_算子代数.md` — the thinnest, strictest base: Unit / Bool / Bool² / Bool³, 分 as a type-level functor, Y-combinator as 生生. [AI-drafted]
- `义理/E_古代源流.md` — thirteen ancient generative schemes (易传, 老子, 周敦颐, 邵雍, 京房, 汉象数, 内经, 太玄 3ⁿ, 洪范九畴, 月令, 说卦, 大衍筮法, 京房纳甲) with a source-review memo admitting the corpus's own gaps. [AI-drafted]
- `义理/F_物理现象学.md` — physics/phenomenology analogies, self-labelled `analogyOnly` and forbidden as proof ground. [AI-drafted]

**义理 G–M — the v3 rewrite and the incompleteness line**
- `义理/G_完整算子系统_八卦互通与归一.md` — the full R₀..R₈ operator system: 8 atomic XOR generators, V₄ outer, Cayley fusion, lift/project, 归一 redefined, the 11+1 minimal operator set. [AI-drafted]
- `义理/H_证明报告.md` — v3 Lean status report; Phase A/F/G/C; Theorems A–K; 3656 jobs, 0 sorry, 0 static project axiom; the 道-理 stance on what the report itself is. [AI-drafted]
- `义理/I_八卦全集.md` — the complete R₃ / R₆ / R₈ atlas with OX literals. [AI-drafted]
- `义理/J_理之不完备_哥德尔在256.md` — Gödel at 256: 道理二分, the Goldilocks-layer argument, the static/dynamic boundary, Rice's four images, the Kleene axiom's four-atom decomposition. [AI-drafted]
- `义理/K_完备性审计.md` — the 11+2 closure checklist, the by-design exclusions, the static/dynamic axiom comparison, 三值保守律 U ⇏ ⊤, the self-conscious 「完备性 ≡ Strict Uniform Abelian Closure」. [AI-drafted]
- `义理/L_文道一也_自释与微核.md` — BaguaTuring, WenyanSelfInterp, WenyanText, YiCore: Turing completeness, the 1-cell Quine, executable classical Chinese, and the two-character micro-kernel. [AI-drafted]
- `义理/M_证明报告_256_理之不完备.md` — GodelLi's Lean report (988 lines, 49 theorems, 1 axiom), renumbered 192→256 with the theorem structure unchanged. [AI-drafted]
- `义理/Cell256_BaguaTuring_理层全集与不完备.md` — the 理-layer complete set, operator space and incompleteness boundary; v2→v3 renumbering note. [AI-drafted]

**义理 N–T — traditions**
- `义理/N_儒家从元到圣.md` — Confucian categories in Kernel Layers 13–31, 80+ theorems, zero new axioms; the 動 → 中 → ZhongOrbit → 仁/礼/智/信 → 五常 → 圣人 architecture. [AI-drafted]
- `义理/O_进化非道者生存_三视证.md` — the three-view proof (scale / value / reflexive) that the evolutionary sieve is not the Dao sieve, with cancer / parasite / pseudo-open counterexamples. [AI-drafted]
- `义理/P_道家从无到化.md` — Daoist categories in Layers 32–33; shares machinery with Confucianism, differs only in emphasis. [AI-drafted]
- `义理/Q_佛家从苦到觉.md` — Buddhist categories in Layer 34; the highest structural fit (缘起 = step, 中道 = middle, 诸法无我 = shi_no_telos). [AI-drafted]
- `义理/S_先秦百家.md` — Mohist, Legalist, School-of-Names and Yin-Yang schools (Layers 35–38) plus a `WuXing` inductive. [AI-drafted]
- `义理/T_西哲与亚伯拉罕.md` — Greek, early-modern, 20th-century Western philosophy and the three Abrahamic traditions (Layers 39–42), declared structural correlate not ontological reduction. [AI-drafted]

**义理 R, U–Z — alignment, sincerity, politics, economics**
- `义理/R_与生生不息对齐之必然.md` — the six-view proof that process alignment is the only groundable alignment; the corpus's normative centrepiece. [AI-drafted]
- `义理/U_反诛心信诚之形式.md` — sincerity as T+E alignment, anti-诛心 enforced at the type level, consent, graded output, inquiry-not-judgment. [AI-drafted, from Ren's JIAN v1.0 §IV.5]
- `义理/V_现代政治哲学.md` — 11 validated and 7 refuted modern political propositions; the first bidirectional layer. [AI-drafted]
- `义理/W_非道之形式.md` — struggle, winner-take-all, Moloch and totalising dynamics as 非道; 同根 as the Universal Anti-Moloch Principle; 大同 ≠ 通吃. [AI-drafted from Ren's instruction]
- `义理/X_反施密特.md` — Schmitt's three pillars collapse to ¬tongGen; Anti-Schmitt = Anti-Moloch; the third political option. [AI-drafted]
- `义理/Y_对齐失败.md` — the AI-alignment failure catalogue as Kernel-invariant violations; no stable terminal goal, aligned or not. [AI-drafted]
- `义理/Z_经济博弈.md` — 19 economic/game-theoretic theorems: 6 validated, 4 conditional, 8 refuted; market's two faces. [AI-drafted]
- `义理/人类命运共同体_共同体之证.md` — the community-of-shared-destiny formalisation: three axes, three counterexamples, one iff. [AI-drafted]
- `义理/道桥接_ProcessAligned_Dao_ShengshengBuxi.md` — the explicit bridge restoring 道 as a middle term rather than flattening ProcessAligned → 生生不息. [AI-drafted]

**义理 八衍 — the eight expansions**
- `义理/数与算术 · 从元到数.md` — ℕ/ℤ/ℚ/ℝ and arithmetic from the 间→分→异同→位→列→量→数→算 spine. [AI-drafted]
- `义理/形式逻辑 · 从元到推.md` — Bool³ ≅ trigrams ≅ truth tables; K3 three-valued logic; Curry-Howard. [AI-drafted]
- `义理/统计 · 从元到测.md` — Kolmogorov, Bayes, 大衍占筮; statistics as the continuum-isation of the undecided value U. [AI-drafted]
- `义理/几何位 · 从元到形.md` — point, distance, topology, the four positions of 易. [AI-drafted]
- `义理/类与映 · 从元到映.md` — category, functor, natural transformation, Yoneda, CCC, monad from 异 → 映. [AI-drafted]
- `义理/动力 · 从元到行.md` — phase space, orbits, fixed points, Markov chains, finite Euler. [AI-drafted]
- `义理/心智 · 从元到识.md` — 唯识四分, 心学四端, Hopfield, three-phase time; explicitly upgrades F's weak analogy to a strict mapping. [AI-drafted]
- `义理/物理 · 从元到象.md` — qubit basis, duality, conservation, the strict SU(3) boundary. [AI-drafted]
- `义理/生态 · 从元到生.md` — operational closure, autopoiesis, the second-law ceiling; Lean deferred to Phase 5+. [AI-drafted]
- `义理/拓扑 · 从元到障.md` — equivariant categories, Bredon cohomology, obstruction as the algebraic form of the ceiling; Lean deferred. [AI-drafted]
- `义理/史带结构 · 从爻到算子列.md` — history as a tape; push/pop as tape write/read; operator sequences as 分. [AI-drafted]

**义理 边界 — the boundary atlas**
- `义理/边界/README.md` — index of the twelve boundary documents and their Lean summary theorems. [AI-drafted]
- `义理/边界/边界总图谱 · 知感行证名量测推.md` — the eight boundaries, their pairwise distinctness, and the error taxonomy of boundary confusion. [AI-drafted]
- (also present and referenced, read at index level: `统一边界 · 从理到文`, `可知边界 · 语言与理`, `可的边界 · 感行证`, `知的边界 · 明辨述`, `感的边界 · 受觉现`, `行的边界 · 能境作效`, `证的边界 · 命题系统证书`, `名的边界 · 指称定名`, `量的边界 · 数测度`, `测的边界 · 观验读`, `推的边界 · 前规则结`, `四界不混同 · 测量推感`) [AI-drafted]

**义理 — physics bridge and specialised notes**
- `义理/Markov因果桥 · 大统一最小验证构造.md` — the master document of the S2–S33 bridge: every Lean anchor, the claim block, the not-yet-closed list, and the build-failure log. [AI-drafted]
- `义理/Born rule推导候选 · Markov桥S18.md` — representative S-file, read in full: the Born rule derived from Markov row normalisation plus amplitude compatibility, with its own "required but not closed" table. [AI-drafted]
- `义理/量子与相对论直统一不可能 · 当前语言NoGo.md` — the tagged-language noncollapse theorem and the careful statement of what it does *not* prove. [AI-drafted]
- `义理/量子与相对论整合方向 · 从桥到新理论.md` — the mediated-bridge direction. [AI-drafted]
- `义理/量子时空互补 · 从一到测.md`, `义理/量子物理语言 · 从虚到测.md` — quantum/spacetime complementarity and the quantum-language alignment. [AI-drafted]
- `义理/文构造完备与直相加边界.md` — the correction that the no-go is about tagged physical language, not about the 256 × 371 constructive coverage. [AI-drafted]
- `义理/Z_平方塔自相似规则.md` — the squaring sub-tower {R₀,R₁,R₂,R₄,R₈} and the recursion T_{k+1} = T_k × T_k. [AI-drafted]
- `义理/文-R8投影规约.md` — sentence → R8 projection, return-to-Dao detection, projection-loss ledger. [AI-drafted]
- `义理/爻维格算 · 物间缘与256x371拓扑.md` — the 256 × 371 = 94,976 operator-cell grid and its connectivity. [AI-drafted]
- `义理/根算子与目录隔离.md` — root-native operators vs the quarantined legacy catalogue. [AI-drafted]
- `义理/物间事三位一体 · 时空事件.md` — 物 × 间 × 事 as a complete decomposition; the spacetime-event reading. [AI-drafted]
- `义理/算子别名总表.md` — one operator, many characters: the cross-tradition alias registry and its 差等 notation. [AI-drafted]
- `义理/WenSurface领域语义caveat细分.md` — the eight-batch plan to close 249 domain caveats in the WenSurface evaluator. [AI-drafted]
- Markov桥 S2–S33 series (~35 files, sampled at index level via the master document plus S18 in full): `有限概率核接口 · S2`, `路径组合与因果约束 · S3`, `经典Markov与量子振幅分层 · S4`, `干涉与测量律候选 · S5`, `S5b`–`S5r` (non-zero amplitude, two-path cancellation, discrete phase, discrete action, path-family sums and algebra, endpoint-indexed families, support normalisation, two-route enumeration, path-identity keys, key quotients, quotient classes, canonical representatives, quotient support, quotient-support algebra, observable ledger, action-phase law), `逐步统一候选摘要 · S8`, `S9`–`S12` (normalisation, mass sums, Born weight, Born distribution), `S13`–`S17` (channel compose, associativity, sum-over-middle, sum-over-middle Born, unitary/CPTP ledger), `S18`–`S23` (Born rule derivation, path-weight multiplication, nontrivial channel law, measurement weights, action-to-measurement chain, phase evolution), `S24`–`S26` (continuous action functional, path-space action functional, action extremum), `S27`–`S33` (causal locality, causal interval, kernel-path carrier, recursive carrier, endpoint-indexed carrier family, two-route completeness, all-KernelPath enumeration). [AI-drafted]

**docs-next/00_start**
- `docs-next/00_start/README.md` — the three reading paths and the boundary reminders. [AI-drafted]
- `docs-next/00_start/scope.md` — what docs-next includes and excludes; the Phase A–G milestone table; the 2026-05-21 honesty note on sorries and axioms. [AI-drafted]
- `docs-next/00_start/final-theory.md` — the v3 one-page map: strict R₀..R₈, V₄ Shi, 道's five identities, OX notation, the old→new correction table, pending items. Marked `[Superseded]`. [AI-drafted]
- `docs-next/00_start/research-position.md` — the three-tier academic positioning with nine numbered novel claims, proposed paper titles and venues, risk analysis, and the 2026-05-21 audit annotation. [AI-drafted from Ren's ideas]
- `docs-next/00_start/phase-status.md` — the main-branch snapshot at `1c76a55`, with the 2026-05-21 update giving the real sorry inventory by file. [AI-drafted]
- `docs-next/00_start/final-claim-roadmap.md` — the separation of "final claim we may eventually earn" from "claim we can defend today", with an explicit list of what must never be substituted for what. [AI-drafted]
- `docs-next/00_start/gut-c-doctrine.md` — GUT-C via SMCC-enriched Lawvere theory; the per-property table showing P3 and P7b are algebraic-specific; Path A/B/C comparison. [AI-drafted]
- `docs-next/00_start/lawvere-identification.md` — D1 = lfp(Φ); why literal Lawvere fails by cardinality; self-internalisation as the weaker sufficient condition; benign vs paradoxical fixed points. [AI-drafted]
- `docs-next/00_start/representation-closure.md` — the philosophical programme arguing that R-tower *necessarily* double-represents concept and language. [AI-drafted]
- `docs-next/00_start/peer-engagement-draft.md` — outreach draft for external critique, with four specific questions and an honest open/closed split. [AI-drafted from Ren's positioning]
- `docs-next/00_start/roadmap-self-similarity-v1.md` — the v1.39 self-similarity formalisation roadmap (R₄² carry, universal compose). [AI-drafted]
- `docs-next/00_start/v4-foundation-roadmap.md` — ten implementation phases for the V4 foundation. [AI-drafted]
- `docs-next/00_start/session-summary-2026-05-17.md` — the GUT-A/B/C push session record, preserved verbatim with a do-not-edit header. [AI-drafted]
- `docs-next/00_start/theory-path.md`, `formal-path.md`, `maintenance-path.md` — the three reading routes, including the "不要这样读" list. [AI-drafted]
- `docs-next/00_start/literature-notes/path-c-foundations.md` — deep reading of Power 1999, Hyland-Power 2007, HLS 2009, with confidence flags per theorem. [AI-drafted]
- `docs-next/00_start/outreach/john-power-proposal.md` — the framework-validation letter to Prof. John Power. [Ren-authored in voice, AI-drafted]
- `docs-next/00_start/papers/README-papers.md` — submission-package inventory and the md→tex conversion notes with a known-issues list. [AI-drafted]
- `docs-next/00_start/papers/gut-c-tac-submission.md` — the 26k-word TAC paper draft: T_GUT as a biproduct-enriched Lawvere theory, four instances, the O1 factorisation attack. [AI-drafted]
- `docs-next/00_start/papers/cover-letter-draft.md` — editor cover letter with an honest scope-and-partial-validation section. [AI-drafted]
- `docs-next/00_start/papers/gut-c-tac-submission.tex`, `.bib` — LaTeX conversion and bibliography of the same paper. [AI-drafted; not read line-by-line, duplicates the .md]
- `docs-next/00_start/papers/mathlib-pr-1-elementary-topos.md`, `mathlib-pr-2-lawvere-theory.md` — two upstream Mathlib contribution proposals. [AI-drafted]

**docs-next/10_formal_形式 (assigned files)**
- `docs-next/10_formal_形式/claim-status-ledger.md` — v0.8, the single honest status page: reading rule, ~40 status rows, immediate priorities, main anchors, and the preferred/forbidden wording policy. [AI-drafted; the corpus's key epistemic artefact]
- `docs-next/10_formal_形式/universal-claims.md` — D5 proof structure for the six maximum-strength universal claims (UG, cognition, phenomenology, decidability, informational-physical, Claim Z) with substrate-level vs realisation-relative framing. [AI-drafted]
- `docs-next/10_formal_形式/yi-RO-hierarchy.md` — the v2.1 definitive R–O doctrine: three axioms plus the taiji zero-anchor, form/structure/relation/insight/completeness/self-reference parts, the triple coincidence, the 11-item checklist. Marked historical. [AI-drafted]
- `docs-next/10_formal_形式/yi-as-meta-framework.md` — the philosophical companion: hexagram = character = operator, 64 operators as type-theory primitives, integral/differential duality, the harmonic-oscillator phase quadrants, "self-description's GUT, not physics'". Marked `[Superseded]`. [AI-drafted]
- `docs-next/10_formal_形式/r-attractor-capitalism.md` — R-dynamics vocabulary and capitalism as projection-selection-recursion over a non-closed residual field; externality as failure of the observation square to commute; six falsification handles. [AI-drafted]
- `docs-next/10_formal_形式/wen-substrate/00-README.md` — the eight-chapter map, the four-level abstraction tower, the anchor-migration table, and the status snapshot at split time. [AI-drafted]
- `docs-next/10_formal_形式/wen-substrate/01-foundations.md` — D1 and P1–P7, R-Family as the smallest satisfying carrier, the cosmological reading. [AI-drafted]
- `docs-next/10_formal_形式/wen-substrate/02-parametric.md` — R-Family over an arbitrary commutative-ring base; encoding vs articulation. [AI-drafted]
- `docs-next/10_formal_形式/wen-substrate/03-operation-monism.md` — operation monism and distinction monism; composition as identification; the lineage table; the 道家 reading; the δ notation change. [AI-drafted]
- `docs-next/10_formal_形式/wen-substrate/04-rpattern.md` — `RWord` and `RPattern` as the face-lattice of the N-cube; merge/restrict as a partial commutative monoid. [AI-drafted]
- `docs-next/10_formal_形式/wen-substrate/05-coverage.md` — the coverage case domain by domain, with a status section marking the programmatic claims. [AI-drafted]
- `docs-next/10_formal_形式/wen-substrate/06-universal-grammar.md` — classical UG as an R-Family substrate claim; the conditional X²-256 lattice form; Open Problem #2. [AI-drafted]
- `docs-next/10_formal_形式/wen-substrate/07-claim.md` — the direct claim, the eight-column comparison with ZFC/type theory/category theory/Boolean/linear-F₂, seven objections, Claim Z with its bi-directional defence and three falsification routes. [AI-drafted]
- `docs-next/10_formal_形式/wen-substrate/08-obligations.md` — the full proof structure T0, D1–D6, T1–T8, Phase 0 sub-theorems, and the version history v0.6 → v1.5.1. [AI-drafted]

**docs-next/20_theory_义理**
- `docs-next/20_theory_义理/README.md` — the re-index of the 义理 corpus with category overview and maintenance constraints. [AI-drafted]
- `docs-next/20_theory_义理/reading-order.md` — six reading paths (quick, formal, traditional, modern, eight-expansion, author) and the instruction to check the indexes whenever a strong word appears. [AI-drafted]
- `docs-next/20_theory_义理/core-framework.md` — the v3 义理 entry point: the ladder, the six-feature semantic layer on the M-axis, the modal frame, the operator algebra, Cayley self-duality, Shi V₄. [AI-drafted]
- `docs-next/20_theory_义理/formal-and-proof.md` — which 义理 claims have formal backing and the principle that explanation is not proof. [AI-drafted]
- `docs-next/20_theory_义理/traditions.md` — Confucian/Daoist/Buddhist and pre-Qin readings as content projections, not textual merger. [AI-drafted]
- `docs-next/20_theory_义理/modern-and-alignment.md` — the modern/alignment cluster with its single criterion. [AI-drafted]
- `docs-next/20_theory_义理/eight-expansions.md` — the eight expansions in one table with three strength levels. [AI-drafted]
- `docs-next/20_theory_义理/extensions.md` — main-line and side-line four expansions. [AI-drafted]
- `docs-next/20_theory_义理/bridge-to-lean.md` — the five-level strength scale and the required index lookups. [AI-drafted]
- `docs-next/20_theory_义理/map-a-g.md`, `map-h-m.md`, `map-n-t.md`, `map-u-z.md` — the four segment maps with per-file audit questions. [AI-drafted]
- `docs-next/20_theory_义理/v4-consciousness-boundary.md` — V₄ as expressible boundary, the Dao-ward tree, structural vs informational truth, consciousness as a self-referring node, the five errors, the knowability axis. [AI-drafted from Ren's two source paragraphs]
- `docs-next/20_theory_义理/wen-daodejing.md` — the project's own sixteen-chapter scripture-style text with per-chapter "formal reading" notes. [AI-drafted]

**formal-notes**
- `formal-notes/HumanAlignment.md` — 人 = 天之子 with awareness; 做人 = 意图向齐生; control excluded from the goal by registry. [AI-drafted from Ren's claim, quoted verbatim at the top]
- `formal-notes/Attention.md` — 聚焦 vs 注意 as distinct registered items; attention patterns from cognitive science mapped in; control as local mechanism only. [AI-drafted]
- `formal-notes/JianOntology.md` — the 14-character Jian ontology: three roots, three manifestations with bracketing, three marks, the open/close gate, three compositions with feedback, and the self-reference witness. [AI-drafted from Ren's 間本体论 draft]
- `formal-notes/自释与自证.md` — the layered distinction between semantic self-interpretation and syntactic self-validation, with a naming convention table and an explicit "never claim" list. [AI-drafted]
- `formal-notes/math-axiom-map.md` — the eleven-row mathematical-axiom generation table, the "math interfaces have roots" metatheorem, and the U ⇏ ⊤ conservativity rule applied to axiom contracts. [AI-drafted from v14 §十二]
- `formal-notes/zero-axiom-roadmap.md` — the route to removing `kleene_recursion_axiom`, with an interface audit of each obligation against the actual machine. [AI-drafted]
- `formal-notes/run-boundary.md` — why `partial def run` must not be removed; the machine-checked evidence about `loopProg`. [AI-drafted]
- `formal-notes/pending-interfaces.md` — the landing plan for the six PendingName empirical interfaces. [AI-drafted]
- `formal-notes/truth-ledger-boundary.md` — audit of the Truth → ClaimLedger → Semantics → Adequacy → Absolute chain and the strongest defensible reading. [AI review]
- `formal-notes/v14-roadmap.md` — the definition/axiom/interface-assumption trichotomy and the machine-verification roadmap from v14. [AI-drafted]
- `formal-notes/MonadDAG.md`, `ConceptDAG.md`, `ConstructionDAG.md`, `monad-root-plan.md` — the three distinct graphs (roster dependency, constructive spine, single-root generation) and the plan that keeps them from being conflated. [AI-drafted]
- `formal-notes/atom-naming.md` — the single-root path 一元 → 面 → CoreAtom → AtomName and the interface-to-character mapping. [AI-drafted]
- `formal-notes/MissingGlyphRootReport.md` — 104 recovered glyphs, with the explicit correction that structural reachability is *not* semantic proof. [AI review]
- `formal-notes/PositionOperatorGraph.md`, `zhouyi-position-operator-report.md` — the six-flip reachability audit and the survey of what 周易 tradition actually contains versus what is formalised. [AI review]
- `formal-notes/baguaWen-spec.md` — the frozen controlled-wenyan L0 kernel (22 tokens) and the L1 WenDef extension resolving the 200+-operator conflict. [AI-drafted]
- `formal-notes/wensurface-roadmap.md`, `wensurface-syntax-spec.md`, `parse-print-roadmap.md` — the WenSurface implementation boundary, the bracket/precedence/infix spec, and the honest correction that the unrestricted parse-print round-trip theorem is false as stated. [AI-drafted]
- `formal-notes/tier3-quine-roadmap.md` — Tier 2 evidence and the path to a Tier 3 quine. [AI-drafted]
- `formal-notes/phase1-target-definition.md` — the meta-interpreter target contract. [AI-drafted]
- `formal-notes/markov-causal-bridge-plan.md`, `markov-causal-bridge-verification-plan.md`, `unification-stepwise-plan.md` — the bridge worktree plan, the verification protocol with failure templates, and the stepwise thickening order. [AI-drafted]

**Repository root**
- `07-shengsheng-buxi/ssbx-repo/README.formal.md` — the formal specification: trust base (one opaque `theOne`, one partial def), the R-hierarchy realisation table, the 一元-DAG (12 faces, 43 core characters, 134 generated, 13 recursive, 5 primitive, 6 pending), the operator catalogue, the module inventory, the headline theorems, build invariants, the two out-of-scope conjectures, and the scope sieve. [AI-drafted]
- `07-shengsheng-buxi/ssbx-repo/ziwen-spec.md` — the 字文 v0 language spec: encoding, glyph normalisation, lexing, tab-only indentation, the core character library, names, grammar, AST, dynamic semantics, diagnostics, and the 64-hexagram standard library appendix. [AI-drafted]
