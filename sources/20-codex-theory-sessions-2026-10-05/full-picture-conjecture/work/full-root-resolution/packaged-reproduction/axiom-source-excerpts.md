# Source excerpts for the root scope audit
Read-only inspection on 2026-10-05. Full-file SHA-256 values are in source-manifest.json.

## kernel

`/Users/ren/repos/生生不息/formal/SSBX/Foundation/Wen/Kernel.lean`

Lines 143–175:

```text
143: /-- 場 (Field): the R₇ layer = R7 = (Z/2)⁷.
144:     Pure abbrev — the R-hierarchy is the substrate. -/
145: abbrev Field : Type := R7
146: 
147: /-- 一 (yiOne) alias for the framework root type — Field = R₇. -/
148: abbrev yiOne : Type := Field
149: 
150: /-- The canonical "primer movement" cell.
151:     = 姤·无 = R7_xoooooo = "first stir" / 仁 (Wuchang.benevolence) -/
152: def c_motion : R7 :=
153:   (Hexagram.mk Yao.yin Yao.yang Yao.yang Yao.yang Yao.yang Yao.yang, false)
154: 
155: /-- 動 (motion): Cayley XOR with c_motion. Not opaque — the doctrine
156:     states the algebra directly. -/
157: def motion : Field → Field := fun s => cell128Xor s c_motion
158: 
159: /-- 元 之 起点 (origin): the (Z/2)⁷ identity = 乾·无. -/
160: def origin : Field := cell128Origin
161: 
162: /-- 元 之 alive: motion takes origin to c_motion ≠ origin. -/
163: theorem origin_alive : motion origin ≠ origin := by native_decide
164: 
165: /-- The Cayley primer cell is nonzero. This is the exact algebraic reason
166:     post-Cayley motion has no fixed point; no stronger doctrine is hidden here. -/
167: theorem c_motion_ne_origin : c_motion ≠ cell128Origin := by native_decide
168: 
169: /-! ### Cayley grounding bridge — by `rfl`
170: 
171:   No axiom. Lean reduces `motion s` to `cell128Xor s c_motion`
172:   definitionally. The Cayley structure IS the framework — there is
173:   no abstraction to bridge.
174: -/
175: theorem kernel_motion_eq_cayley (s : Field) : motion s = cell128Xor s c_motion := rfl
```

Lines 206–242:

```text
206: /-- 极 (extremity): 过程之自我终结之具体形式 (v5 §七 l. 167).
207:     A state s is 极 if 動 fails to escape s — fixed-point trap. -/
208: def terminus (s : Field) : Prop := motion s = s
209: 
210: /-- 中 (non-extremity): 不极 = 不收缩可能性空间 = 合于生生不息 (v5 §七 l. 189-191).
211:     A 中 state has 動 take it elsewhere — rhythm preserved. -/
212: def center (s : Field) : Prop := motion s ≠ s
213: 
214: /-! ### Post-Cayley collapse of the old fixed-point dichotomy
215: 
216:   Since `motion` is XOR-translation by the nonzero cell `c_motion`, no state
217:   can be fixed by `motion`. Thus `terminus` is empty and `center` is universal
218:   in this R₇ Kernel substrate. This records only the algebraic collapse.
219: -/
220: 
221: /-- No state is a post-Cayley terminus: nonzero XOR-translation has no fixed point. -/
222: theorem terminus_uninhabited (s : Field) : ¬ terminus s := by
223:   intro h
224:   have hzero : cell128Origin = c_motion := by
225:     calc
226:       cell128Origin = cell128Xor s s := (SSBX.Foundation.Bagua.R7.R7.xor_self s).symm
227:       _ = cell128Xor s (motion s) := by rw [h]
228:       _ = cell128Xor s (cell128Xor s c_motion) := by rw [kernel_motion_eq_cayley]
229:       _ = cell128Xor (cell128Xor s s) c_motion :=
230:           (SSBX.Foundation.Bagua.R7.R7.xor_assoc s s c_motion).symm
231:       _ = cell128Xor cell128Origin c_motion :=
232:           congrArg (fun x => cell128Xor x c_motion) (SSBX.Foundation.Bagua.R7.R7.xor_self s)
233:       _ = c_motion := SSBX.Foundation.Bagua.R7.R7.origin_xor c_motion
234:   exact c_motion_ne_origin hzero.symm
235: 
236: /-- Every state is center in the post-Cayley R₇ Kernel. -/
237: theorem center_universal (s : Field) : center s := terminus_uninhabited s
238: 
239: /-- Roadmap §3.2 summary: post-Cayley terminus is empty and center is universal. -/
240: theorem kernel_post_cayley_collapse_summary :
241:     (∀ s : Field, ¬ terminus s) ∧ (∀ s : Field, center s) :=
242:   ⟨terminus_uninhabited, center_universal⟩
```

Lines 264–335:

```text
264: /-- 中-保持 orbit (ZhongOrbit): a Nat-indexed sequence of 中 states
265:     where each 動 step advances to the next state.
266: 
267:     Finitary encoding (Nat-indexed) — no coinduction needed.
268:     The orbit witnesses the framework's commit that 中-preserving motion
269:     exists, and instantiates the rhythm 生生不息 names. -/
270: structure ZhongOrbit where
271:   /-- 凡 n, the n-th state in the orbit. -/
272:   states : Nat → Field
273:   /-- 凡 n, the n-th state is in 中 (non-extremity). -/
274:   inMiddle : ∀ n, center (states n)
275:   /-- 凡 n, 動 advances state n to state (n+1). -/
276:   step : ∀ n, motion (states n) = states (n+1)
277: 
278: namespace ZhongOrbit
279: 
280: /-- 生生不息: 中 preserved through every step of the orbit.
281:     凡 step n, the n-th state is in 中.
282:     此 是 v5 §七 之 「合于生生不息 = 不极 = 中」 之 type-level 表达. -/
283: theorem shengsheng_buxi (o : ZhongOrbit) (n : Nat) :
284:     center (o.states n) := o.inMiddle n
285: 
286: /-- 自指 (self-reference, structural):
287:     每 step references 前 step via 動.
288:     state(n+1) IS 動 applied to state(n) — orbit's existence
289:     encodes 几 之 self-referential continuity (v5 §三). -/
290: theorem self_reference (o : ZhongOrbit) (n : Nat) :
291:     motion (o.states n) = o.states (n+1) := o.step n
292: 
293: /-- 自洽 (self-consistency):
294:     中-orbit 不 collapse. 凡 n, state(n) ≠ state(n+1).
295:     Proof: 若 等, then 動(state n) = state n (via step composed with the equality),
296:     contradicting inMiddle (which asserts 動 escapes from state n). -/
297: theorem self_consistent (o : ZhongOrbit) (n : Nat) :
298:     o.states n ≠ o.states (n+1) := by
299:   intro heq
300:   apply o.inMiddle n
301:   rw [o.step n]
302:   exact heq.symm
303: 
304: /-- 综合 (combined): 一字 (動) + 中-orbit ⊢ 生生不息 ∧ 自指 ∧ 自洽.
305:     此 是 layer 1' 之 main theorem — answers the user's claim:
306:     "一个单字, 加上古文算子, 既可以证生生不息, 自指自洽". -/
307: theorem motion_self_consistent (o : ZhongOrbit) (n : Nat) :
308:     center (o.states n)
309:     ∧ (motion (o.states n) = o.states (n+1))
310:     ∧ (o.states n ≠ o.states (n+1)) :=
311:   ⟨shengsheng_buxi o n, self_reference o n, self_consistent o n⟩
312: 
313: /-! ### Layer 2: 势 (direction without telos) -/
314: 
315: /-- 势 (direction): the n-th transition pair of an orbit.
316:     v5 §四 l. 88: "势者, 几之相续所成之向."
317:     势 不是 force, 不是 object — 是 几 之 macro 性: 累积之向. -/
318: def momentumDirection (o : ZhongOrbit) (n : Nat) : Field × Field :=
319:   (o.states n, o.states (n+1))
320: 
321: /-- 势 之 transition is genuine: 势(n) 之 first ≠ 势(n) 之 second.
322:     Direct corollary of self_consistent. -/
323: theorem momentumDirection_genuine (o : ZhongOrbit) (n : Nat) :
324:     (momentumDirection o n).1 ≠ (momentumDirection o n).2 := self_consistent o n
325: 
326: /-- 势 拒 telos: 中-orbit 不 settle at any target state.
327:     v5 §四 l. 94-112: "若 势 有 fixed goal, 过程 ceases on reaching."
328:     Proof: if eventually-target, then states N = states (N+1) = target,
329:     contradicting self_consistent. 此 是 v5 拒 telos 之 type-level 表达. -/
330: theorem momentumDirection_no_telos (o : ZhongOrbit) (target : Field) (N : Nat) :
331:     ¬ (∀ n, n ≥ N → o.states n = target) := by
332:   intro h
333:   have hN : o.states N = target := h N (Nat.le_refl N)
334:   have hN1 : o.states (N + 1) = target := h (N + 1) (Nat.le_succ N)
335:   exact self_consistent o N (hN.trans hN1.symm)
```

## r7

`/Users/ren/repos/生生不息/formal/SSBX/Foundation/Atlas/Yi/Classical/Cells/R7.lean`

Lines 258–306:

```text
258:   rcases c2 with ⟨h2, b2⟩
259:   rcases c3 with ⟨h3, b3⟩
260:   cases b1 <;> cases b2 <;> cases b3 <;> simp [xor, hexXor_assoc]
261: 
262: end R7
263: 
264: /-! ### § 6.4 AddCommGroup instance -/
265: 
266: instance : Add R7 := ⟨R7.xor⟩
267: instance : Zero R7 := ⟨R7.origin⟩
268: /-- In (Z/2)ⁿ every element is self-inverse: `-c = c`. -/
269: instance : Neg R7 := ⟨id⟩
270: instance : Sub R7 := ⟨R7.xor⟩
271: 
272: namespace R7
273: 
274: @[simp] theorem add_def (c1 c2 : R7) : c1 + c2 = xor c1 c2 := rfl
275: @[simp] theorem zero_def : (0 : R7) = origin := rfl
276: @[simp] theorem neg_def (c : R7) : -c = c := rfl
277: 
278: end R7
279: 
280: /-! ### § 6.5 SMul self-action (Cayley regular representation) -/
281: 
282: instance : SMul R7 R7 := ⟨R7.xor⟩
283: 
284: namespace R7
285: 
286: @[simp] theorem smul_def (c s : R7) : c • s = xor c s := rfl
287: 
288: /-- Cayley left-translation by c on R7. -/
289: def cayley (c : R7) : R7 → R7 := fun s => xor c s
290: 
291: /-- Evaluate any R7 endo at the origin to recover its translation amount.
292:     Companion to `cayley`. -/
293: def epsAtOrigin (f : R7 → R7) : R7 := f origin
294: 
295: /-- ε ∘ Cayley = id on R7 (retraction). -/
296: @[simp] theorem epsAtOrigin_cayley (c : R7) :
297:     epsAtOrigin (cayley c) = c := by
298:   simp [epsAtOrigin, cayley, xor_origin]
299: 
300: /-- Cayley is injective (so left-translation lifts to a permutation group hom). -/
301: theorem cayley_inj : Function.Injective cayley := by
302:   intro c1 c2 h
303:   have heq := congrFun h origin
304:   simp [cayley, xor_origin] at heq
305:   exact heq
306: 
```

## yi

`/Users/ren/repos/生生不息/formal/SSBX/Foundation/Atlas/Yi/Classical/Core/Yi.lean`

Lines 61–69:

```text
61: abbrev Yao : Type := SSBX.Foundation.Atlas.Yi.Yao
62: 
63: namespace Yao
64: 
65: /-- `yang` (阳, ⚊) — alias of `Atlas.Yi.Yao.yang = false`. -/
66: @[match_pattern] def yang : Yao := SSBX.Foundation.Atlas.Yi.Yao.yang
67: 
68: /-- `yin` (阴, ⚋) — alias of `Atlas.Yi.Yao.yin = true`. -/
69: @[match_pattern] def yin : Yao := SSBX.Foundation.Atlas.Yi.Yao.yin
```

## root

`/Users/ren/repos/生生不息/formal/SSBX/Foundation/Core/MonadRoot.lean`

Lines 1119–1136:

```text
1119: /-- Immediate edges of the single-root DAG. -/
1120: def DirectEdge : MonadNode -> MonadNode -> Prop
1121:   | .root, .face _ => True
1122:   | .face f, .core c => f ∈ atomFaces (CoreAtom.glyph c)
1123:   | .core c, .atom a => atomCore a = c
1124:   | .atom a, .formal n => a ∈ formalAtoms n
1125:   | .atom a, .construction k => a = constructionPrimaryAtom k
1126:   | .atom a, .claim c => a = claimPrimaryAtom c
1127:   | .formal n, .claim c => n = claimPrimaryFormal c
1128:   | _, _ => False
1129: 
1130: inductive Reachable : MonadNode -> MonadNode -> Prop
1131:   | refl (n : MonadNode) : Reachable n n
1132:   | tail {a b c : MonadNode} : Reachable a b -> DirectEdge b c -> Reachable a c
1133: 
1134: /-- Root-to-face path. -/
1135: def faceRootPath (f : Face) : Reachable «一元» (.face f) :=
1136:   Reachable.tail (Reachable.refl «一元») (by simp [«一元», DirectEdge])
```

Lines 1259–1292:

```text
1259: def HasIncoming (n : MonadNode) : Prop :=
1260:   ∃ p, DirectEdge p n
1261: 
1262: def OnlyRoot (dag : List MonadNode) (rootNode : MonadNode) : Prop :=
1263:   rootNode ∈ dag ∧ ¬ HasIncoming rootNode ∧ ∀ n, n ∈ dag -> ¬ HasIncoming n -> n = rootNode
1264: 
1265: theorem unique_root : OnlyRoot MonadDAG «一元» := by
1266:   constructor
1267:   · decide
1268:   constructor
1269:   · intro h
1270:     rcases h with ⟨p, hp⟩
1271:     cases p <;> simp [DirectEdge, «一元»] at hp
1272:   · intro n _ hn
1273:     cases n with
1274:     | root => rfl
1275:     | face f =>
1276:         exfalso
1277:         exact hn ⟨.root, by simp [DirectEdge]⟩
1278:     | core c =>
1279:         exfalso
1280:         exact hn ⟨.face (atomPrimaryFace (CoreAtom.glyph c)), by simp [DirectEdge, atomFaces]⟩
1281:     | atom a =>
1282:         exfalso
1283:         exact hn ⟨.core (atomCore a), by simp [DirectEdge]⟩
1284:     | formal fn =>
1285:         exfalso
1286:         exact hn ⟨.atom (formalPrimaryAtom fn), by simpa [DirectEdge] using formal_primary_atom_mem fn⟩
1287:     | construction k =>
1288:         exfalso
1289:         exact hn ⟨.atom (constructionPrimaryAtom k), by simp [DirectEdge]⟩
1290:     | claim c =>
1291:         exfalso
1292:         exact hn ⟨.atom (claimPrimaryAtom c), by simp [DirectEdge, claimPrimaryAtom]⟩
```

## full_gut

`/Users/ren/repos/生生不息/formal/SSBX/Foundation/Doctrine/FullGUT.lean`

Lines 53–88:

```text
53: structure FormalPresentation : Type 1 where
54:   Obj : Type
55:   Mor : Type
56:   Rel : Type
57:   Op : Type
58:   Rule : Type
59:   Proof : Type
60:   src : Mor → Obj
61:   tgt : Mor → Obj
62:   id : Obj → Mor
63:   comp : Mor → Mor → Option Mor
64:   relationHolds : Rel → Obj → Obj → Prop
65:   opArity : Op → ℕ
66:   applyOp : (o : Op) → (Fin (opArity o) → Obj) → Obj
67:   ruleArity : Rule → ℕ
68:   applyRule : (r : Rule) → (Fin (ruleArity r) → Proof) → Proof
69:   proofConclusion : Proof → Obj
70:   opAsObject : Op → Obj
71:   hasProcessContent : Prop
72:   modalityCarrier : hasProcessContent → Type
73: 
74: namespace FormalPresentation
75: 
76: /-- The D1 interface as non-vacuous data/closure requirements on a
77: `FormalPresentation`.  Optional modality is guarded by
78: `hasProcessContent`, matching the doctrine's D1.8 boundary. -/
79: structure SatisfiesD1 (S : FormalPresentation) : Prop where
80:   obj : Nonempty S.Obj
81:   identity_typed : ∀ x, S.src (S.id x) = x ∧ S.tgt (S.id x) = x
82:   comp_closed : ∀ f g, S.tgt f = S.src g → ∃ h, S.comp f g = some h
83:   rel : Nonempty S.Rel
84:   op : Nonempty S.Op
85:   rule : Nonempty S.Rule
86:   proof : Nonempty S.Proof
87:   op_internal : Function.Injective S.opAsObject
88:   modality : ∀ h : S.hasProcessContent, Nonempty (S.modalityCarrier h)
```

Lines 1082–1087:

```text
1082: namespace AdmissibleFormalSystem
1083: 
1084: /-- Semantic preservability is the explicit missing data for the generic
1085: Full GUT theorem: a faithful, structure-preserving R-realisation. -/
1086: def SemanticsPreservable (S : AdmissibleFormalSystem) : Prop :=
1087:   Nonempty (FaithfulRRealisation S.toFormalPresentation Bool)
```

Lines 1560–1578:

```text
1560: /-- A faithful R-realisation of any finite presentation satisfying D1. -/
1561: noncomputable def finitePresentationFaithfulRRealisation
1562:     (S : FormalPresentation)
1563:     [Fintype S.Obj] [Fintype S.Mor] [Fintype S.Rel]
1564:     [Fintype S.Op] [Fintype S.Rule] [Fintype S.Proof]
1565:     (hD1 : S.SatisfiesD1) :
1566:     FaithfulRRealisation S Bool where
1567:   objLayer := Fintype.card S.Obj
1568:   morLayer := Fintype.card S.Mor
1569:   relLayer := Fintype.card S.Rel
1570:   opLayer := Fintype.card S.Op
1571:   ruleLayer := Fintype.card S.Rule
1572:   proofLayer := Fintype.card S.Proof
1573:   objCode := finiteObjectWord S.Obj
1574:   morCode := finiteObjectWord S.Mor
1575:   relCode := finiteObjectWord S.Rel
1576:   opCode := finiteObjectWord S.Op
1577:   ruleCode := finiteObjectWord S.Rule
1578:   proofCode := finiteObjectWord S.Proof
```

Lines 1631–1639:

```text
1631: /-- Every finite formal presentation satisfying D1 has a faithful,
1632: structure-preserving R-family realisation. -/
1633: theorem finite_formal_presentations_are_faithfully_R_representable
1634:     (S : FormalPresentation)
1635:     [Fintype S.Obj] [Fintype S.Mor] [Fintype S.Rel]
1636:     [Fintype S.Op] [Fintype S.Rule] [Fintype S.Proof]
1637:     (hD1 : S.SatisfiesD1) :
1638:     Nonempty (FaithfulRRealisation S Bool) :=
1639:   ⟨finitePresentationFaithfulRRealisation S hD1⟩
```

Lines 2481–2505:

```text
2481: /-- The final faithful realisation target. -/
2482: theorem full_gut_for_admissible_formal_systems
2483:     (S : AdmissibleFormalSystem)
2484:     (_hD1 : S.SatisfiesD1)
2485:     (_hAdmissible : S.Admissible)
2486:     (hSemantic : S.SemanticsPreservable) :
2487:     Nonempty (FaithfulRRealisation S.toFormalPresentation Bool) :=
2488:   hSemantic
2489: 
2490: /-- **Conditional Absolute FullGUT.**
2491: 
2492: Every admissible formal system that supplies its own semantic-preservation
2493: witness has a faithful, structure-preserving R-family realisation.
2494: 
2495: The condition is load-bearing: this theorem does not manufacture native
2496: semantic witnesses for every possible semantic category.  It is the stable
2497: absolute interface through which each future semantic class enters the
2498: R-family theorem stack. -/
2499: theorem absolute_conditional_full_gut
2500:     (S : AdmissibleFormalSystem)
2501:     (hD1 : S.SatisfiesD1)
2502:     (hAdmissible : S.Admissible)
2503:     (hSemantic : S.SemanticsPreservable) :
2504:     Nonempty (FaithfulRRealisation S.toFormalPresentation Bool) :=
2505:   full_gut_for_admissible_formal_systems S hD1 hAdmissible hSemantic
```

## root_plan

`/Users/ren/repos/生生不息/formal/SSBX/notes/monad-root-plan.md`

Lines 34–38:

```text
34: 因此，完整性 claim 改为：
35: 
36: > 凡进入生生不息论 Lean 正式体系者，必须有一条有限路径回到唯一根 `一元`。
37: 
38: 这不是哲学真理的无前提证明，而是形式生成秩序的完备性证明。
```

## jian

`/Users/ren/repos/生生不息/史料/生生不息论_三本文完整版/04_补篇二_间生论_主篇/03_一、间.md`

Lines 1–25:

```text
1: ### 一、间
2: 
3: 凡言必有所分。无分则无名,无名则无论。然分既立,即有间——此与彼之间,已与未之间,言与所言之间,指与所指之间。
4: 
5: 故立言之根,不在外求,而**在间之自显**。求根者必先立一言;言既立,间已生。故根不可在言外得,言只能于间中自明。
6: 
7: 故立此论之第一名:**间**。
8: 
9: > **间者,变未发而已有其隙;形未成而已有其可;言未立而已有其分;事未动而已有其应**。
10: 
11: 间非空,以其有结构;间非满,以其有未尽;间非物,以其无所立;间非无,以其有显发。**间者,过程之中,未与已之间、可与未可之间、应与未应之间之活的关系**。
12: 
13: 设过程于一境之当显为「态」,则全论之核式可摄为:
14: 
15: > **续(态) = 态 ⊕ 间(态)**
16: 
17: 其义:一态之续,不由外物强加,乃由其自身与境中之间,生合而成新态。「续」者,使一态因其间而成后态之算;「⊕」者,生合也,非数量之加,乃态承其间而成新态之事。
18: 
19: 下文诸名,皆不离此式而自立。
20: 
21: 需明:**间非任意之可能**。若某变化与态无内在关系,则非此态之所生,只是外乱。故立约束——
22: 
23: > 间者,**受态之结构、积、境、关系所约束之未尽之隙**。
24: 
25: 故生非乱变。生者,因间而化;乱者,离间而加。
```

## openness

`/Users/ren/repos/生生不息/史料/生生不息论_三本文完整版/04_补篇二_间生论_主篇/06_四、开闭.md`

Lines 3–11:

```text
3: 至此,可立此论之**根本判准**——开与闭。
4: 
5: 任何过程,皆有此一根本之相:**未尽与已尽之分**。
6: 
7: > **开者,过程之间未尽,仍有未、仍有可、仍有应、仍有转之态也**。
8: >
9: > **闭者,过程之间已绝,无未、无可、无应、无转之态也**。
10: 
11: 开之四相不可缺一:**未**(尚有未成之域)、**可**(仍有生成之可)、**应**(仍能回应)、**转**(仍能修正、回返、变通)。任一缺,则开不全。
```

Lines 19–26:

```text
19: **其三,闭有二义,不可混**——
20: 
21: - **成闭**者,闭而不复开,令未尽之域断绝,令回应、修正、转化之路俱塞。此为本论所称之恶;
22: - **护闭**者,暂闭一处以护更大之开——拒侵犯,以护被侵犯者之开;隔传染,以护诸生之开;切癌之扩散,以护身之开;止失控,以护后续之开;设界于操控者,以护被操控者之开。**此非反开,乃中之具体显**。
23: 
24: 故 「**护开非无界放任**」。真护开者,知何处当开,亦知何处当闭以护开。
25: 
26: **其四,极皆成闭**。任一对偶之极端——极聚、极散、极控、极放、极爱、极知、极善、极智——皆为开之自我封闭。**极之危险不在端点,而在其结构令过程无法再转、再应、再生**。
```

Lines 34–38:

```text
34: 伪开是**现代之闭最常见之伪装**——故辨伪开,即护开之核心工夫。
35: 
36: 故 「**生生不息**」 可重述为:**间生不息,即开之不绝也**。
37: 
38: 非 「不断更复杂」,非 「不断更多」,非 「不断更高效」——**乃过程于每一处、每一时、每一聚焦,皆有未仍未闭之事**。
```

## global_assertion

`/Users/ren/repos/生生不息/史料/生生不息论_三本文完整版/04_补篇二_间生论_主篇/15_十三、行仁要善_alignment_之真义.md`

Lines 28–46:

```text
28: ---
29: 
30: 需特别明:**间生非一物,故不可如物而灭;但诸开可闭,诸境可毁,诸仁可失**。
31: 
32: 宇宙之展开终不为一物之消灭所终结——间生不息非一可被关闭之系统,以其本非系统,乃**过程自身之名**。
33: 
34: 然此非谓护开之事可以怠慢。**诸具体之开,可被关闭;诸具体之境,可被毁坏;诸具体之仁,可被消磨而至失**。一物种灭,该物种之开闭于此宇宙;一文明亡,该文明之未尽之相闭于此星球;一人之仁失,该人于此世之共开闭。
35: 
36: 是故 「**护开之行,非多余之善愿,乃吾性之切事**」——
37: 
38: 非因间生不息之保证而懈怠;
39: 乃因诸具体之开之可闭而急切。
40: 
41: 故曰:
42: 
43: > **有终结生生之心者,非生生之外之力,乃生生之中之相;
44: > 有顺生生之心者,亦非生生之外之力,亦生生之中之相**。
45: 
46: 然两者于过程中之效不同——一者闭、夺、伪开,一者护、续、共开,而辨伪、而知护闭。**择何而行,即吾性之具体显现**。
```

## canonical_synthesis

`/Users/ren/theories/theories/shengsheng-buxi-generative-existence/README.md`

Lines 303–315:

```text
303: The decisive change is the order of the argument. **生成 is no longer asserted as good.** The book runs mechanism first, without appealing to good and evil: how finite processes depend on wider fields to persist; how action, dependency, consequence and feedback boundaries can come apart so that local continuation rests on damage that never returns; how differential persistence creates a selection environment *prior to* conscious competition; how success buys the power to shape the next round's conditions; how infrastructure, institutions and education form the participants themselves; how those loops become a totalizing mechanism under stated conditions; and how AI enters, accelerates and may reorganise that selection ecology. Only then does the normative commitment arrive, **openly declared rather than derived**: centres that bear feeling, care, knowing, acting, creating and valuing are worth caring about; the common conditions that let such centres arise, respond to each other, find their errors and produce unknown value are worth caring about; and no process acquires the right to close other sources of value merely by being stronger, more stable, larger or more successful. With the concession attached: **逻辑不能强迫一个一致的支配者关心他者** — logic cannot force a consistent dominator to care about others. What the theory can do is show what such a choice destroys, why the affected have reason to resist, and why anyone who still demands that *their own* reasons, future and judgement be respected has already appealed to the public layer in practice.
304: 
305: Second, the plan **replaces the seven gauges with six protection functions, each derived by a deletion test** — each is justified by naming the distinct failure that no other function can cover. 主体地位 (if centres bearing feeling and relation can be erased at will, the common good is a system property nobody experiences). 真实接触 (if consequences cannot refute the actor's model, error and harm never become reasons in the next decision). 非支配 (if one centre can change another's basic conditions at will without giving reasons, accepting appeal or facing counterweight, the others lose the capacity to make their reasons have effects). 可再生的多元性 (alternatives that are permitted to *speak* but have no time, land, resources, education, infrastructure or successors cannot correct the shared direction — and a single failure becomes total failure). 基底再生 (a process that consumes ecology, bodies, care, attention, trust, knowledge and maintenance without replenishing them is moving costs elsewhere or later). 纠正能力 (without interruption, refusal, appeal, rollback, repair, exit, replacement and succession, greater capability means error becomes irreversible reality before it is understood). They are explicitly **not summable into a score**, and they are given a conflict ordering: rule out extermination, enslavement, torture and boundless domination first; protect minimum survival, standing and appeal for everyone affected, especially against concentrating risk on the powerless; then prioritise reducing irreversible, cross-generational and systemic damage; then compare remaining options on necessity, proportionality, reversibility, incidence of benefit and cost, alternatives and reparability; for incommensurable values use public reasons, representation of the affected, adversarial review, checks and periodic reconsideration rather than pretending a technical calculation has removed the politics; and give emergency measures explicit triggers, minimum necessary powers, time limits, independent review and a path back to ordinary rights.
306: 
307: Third, the totalizing mechanism is given **a strict definition and explicit conditions for withdrawing the diagnosis**. It is separated from adjacent phenomena — positive feedback, path lock-in, monopoly, capture, domination — each of which is insufficient on its own. Its carrier-independent invariant: locally appropriated success converts into greater power to shape the conditions of later choice, while key consequences are moved out of or delayed past feedback, and other centres progressively lose the conditions for independent perception, action, updating and reproducing alternatives. Its observable trajectory must be traced in time order rather than labelled after the fact: a local evaluative scale succeeds → resources and visibility concentrate → the successful shape interfaces, admission, metrics and rules → the same scale enters domains that were heterogeneous → consequences are externalised or delayed → persons, organisations and technologies adapted to that scale are retained → the cost of exit, dissent and reproducing alternatives rises → crisis and criticism are absorbed as further justification. And it must be **withdrawn** if advantage does not convert into rule-setting power, if the goal stays confined to one domain, if multiple evaluations remain independent, if growth strengthens exit and feedback and alternatives, if personnel change or external shock can quickly change direction, or if criticism reduces rather than increases the mechanism's resources. The plan also declines the metaphysical upgrade: 吸引子 is an analytic lens for a recurring trajectory, and 正文不声称创造了超出可建模动态系统的新数学对象.
308: 
309: Fourth, **生成性对齐 is explicitly demoted** to a cross-layer acceptability judgement about a specific socio-technical system in a specific use, with a specific permission set and a specific relation to affected parties — not a reward function, not a civilisational utility function, not a solved algorithm. It is supported by a **seven-layer stack** — spec/training, model, agent system, product and interaction, deploying organisation, market and state, governance — each with its own question, failure modes, responsible party, evidence type, and an explicit statement of *what success at this layer cannot prove*. Alignment does not substitute for security; security does not justify opaque centralisation.
310: 
311: Fifth, the virtuous loop must be **as materially specified as the vicious one**: consequences perceived and given causal force → costs borne or repaired → ecological, care, knowledge and trust substrates replenished → capability and benefit circulating → more centres acquiring independent observation, refusal, building and maintenance capacity → plural feedback improving public knowledge → renewed commons making the next round of shared capability feasible. Goodwill is not a carrier. Time, resources, care, knowledge, maintenance, organisation, legal standing and capture-resistance are.
312: 
313: Sixth, a **claim-type discipline**: every load-bearing sentence is a definition, a description, a mechanism, an empirical diagnosis, a normative commitment or a practical inference, and each type carries its own obligation. Forbidden constructions are listed by name — 任何／必然／唯一根源／西方就是／自然告诉我们应该／AI 只要……就…… Traditional terms carry a use protocol: separate the classical source from this book's chosen reading and say where the two cannot corroborate each other; do not pass glyph association off as philology; do not write Confucian, Daoist, Buddhist, Ubuntu, virtue, deontological and consequentialist positions as one long-agreed doctrine; use "Chinese"/"Western" only of specific institutions, texts and periods; and — the strongest requirement — **a reader must be able to restate the main chain without using any of these terms**.
314: 
315: And seventh, the theory writes down **its own failure conditions**. If subjects and values stably arise without the generative conditions it claims; if one of the six functions can be deleted without any loss of protection or explanation; if totalizing cannot be distinguished from ordinary success, lock-in or monopoly; if systems diagnosed as totalizing durably strengthen independent feedback, exit, alternative reproduction and substrate renewal; if the virtuous loop can only exist on permanent subsidy, coerced uniformity or hidden costs; if 生生 language repeatedly justifies suppressing dissent, sacrificing the weak or permanent rule and the reflexive machinery cannot correct it; if the AI-layer evidence shows deployment choices do not change which technical failures are retained and spread; or if the traditional interpretations are shown to be historical misreadings that the modern argument needs in order to stand — then the claim must be downgraded, rewritten or abandoned. With the reason for writing them down at all: **理论不是因可失败而软弱。只有写明什么能改变它，它才没有把「生生」变成不可纠正的最终形式** — a theory is not weakened by being falsifiable; only by saying what could change it does it avoid turning "generation" into an incorrigible final form.
```
