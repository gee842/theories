# Selected formal-source excerpts

Read-only source snapshots, 5 October 2026. These are the inspected statement/definition boundaries, not a verified rebuild. SHA-256 values identify the complete source files at capture.

## /Users/ren/repos/生生不息/formal/SSBX/Foundation/Core/MonadRoot.lean

SHA-256: `7625468f3fb76c5193a81696b9657c984ed82046dfb21ecf8068321137cd326e`

Lines 947–961:

```text

947: inductive MonadNode where

948:   | root : MonadNode

949:   | face : Face -> MonadNode

950:   | core : CoreAtom -> MonadNode

951:   | atom : AtomName -> MonadNode

952:   | formal : FormalNode -> MonadNode

953:   | construction : ConstructionId -> MonadNode

954:   | claim : ClaimId -> MonadNode

955:   deriving DecidableEq, Repr

956: 

957: /-- The unique root.  This is not `一` or `一元论`; it is the source node itself. -/

958: def «一元» : MonadNode := .root

959: 

960: /-- The whole theory as a generated formal node. -/

961: def «生生不息论» : MonadNode := .formal (.generated .«生生不息»)

```

Lines 1021–1027:

```text

1021: theorem formal_primary_atom_mem (n : FormalNode) :

1022:     formalPrimaryAtom n ∈ formalAtoms n := by

1023:   cases n with

1024:   | generated g => cases g <;> native_decide

1025:   | primitive p => cases p <;> native_decide

1026:   | recursive r => cases r <;> native_decide

1027:   | pending u => cases u <;> native_decide

```

Lines 1120–1128:

```text

1120: def DirectEdge : MonadNode -> MonadNode -> Prop

1121:   | .root, .face _ => True

1122:   | .face f, .core c => f ∈ atomFaces (CoreAtom.glyph c)

1123:   | .core c, .atom a => atomCore a = c

1124:   | .atom a, .formal n => a ∈ formalAtoms n

1125:   | .atom a, .construction k => a = constructionPrimaryAtom k

1126:   | .atom a, .claim c => a = claimPrimaryAtom c

1127:   | .formal n, .claim c => n = claimPrimaryFormal c

1128:   | _, _ => False

```

Lines 1259–1266:

```text

1259: def HasIncoming (n : MonadNode) : Prop :=

1260:   ∃ p, DirectEdge p n

1261: 

1262: def OnlyRoot (dag : List MonadNode) (rootNode : MonadNode) : Prop :=

1263:   rootNode ∈ dag ∧ ¬ HasIncoming rootNode ∧ ∀ n, n ∈ dag -> ¬ HasIncoming n -> n = rootNode

1264: 

1265: theorem unique_root : OnlyRoot MonadDAG «一元» := by

1266:   constructor

```

Lines 1294–1301:

```text

1294: def distance : MonadNode -> Nat

1295:   | .root => 0

1296:   | .face _ => 1

1297:   | .core _ => 2

1298:   | .atom _ => 3

1299:   | .formal _ => 4

1300:   | .construction _ => 4

1301:   | .claim _ => 5

```

Lines 1315–1329:

```text

1315: theorem near_root_constraint (x : MonadNode) :

1316:     distance x ≤ 2 -> x = «一元» ∨ IsFace x ∨ IsCoreAtom x := by

1317:   intro h

1318:   cases x <;> simp [distance, IsFace, IsCoreAtom, «一元»] at h ⊢

1319: 

1320: /-- Acyclicity witness: every direct edge strictly increases monadic distance. -/

1321: def AcyclicByRank (_dag : List MonadNode) : Prop :=

1322:   ∀ {a b : MonadNode}, DirectEdge a b -> distance a < distance b

1323: 

1324: theorem direct_edge_rank_lt {a b : MonadNode} (h : DirectEdge a b) :

1325:     distance a < distance b := by

1326:   cases a <;> cases b <;> simp [DirectEdge, distance] at h ⊢

1327: 

1328: theorem monad_dag_acyclic : AcyclicByRank MonadDAG :=

1329:   fun h => direct_edge_rank_lt h

```

## /Users/ren/repos/生生不息/formal/SSBX/Foundation/Doctrine/FullGUT.lean

SHA-256: `246a9c74ae0c0f6af8c7c664ceda86277b2d09351ff5112adf015408b5ee5825`

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

Lines 833–875:

```text

833: preservation equations. -/

834: structure StructurePreservingRMap

835:     (S : FormalPresentation) (δ : Type := Bool) :

836:     Type extends REncoding S δ where

837:   idCode : R objLayer δ → R morLayer δ

838:   compCode : R morLayer δ → R morLayer δ → Option (R morLayer δ)

839:   relationCodeHolds : R relLayer δ → R objLayer δ → R objLayer δ → Prop

840:   opCodeApply : (o : S.Op) → R opLayer δ →

841:     (Fin (S.opArity o) → R objLayer δ) → R objLayer δ

842:   ruleCodeApply : (r : S.Rule) → R ruleLayer δ →

843:     (Fin (S.ruleArity r) → R proofLayer δ) → R proofLayer δ

844:   proofConclusionCode : R proofLayer δ → R objLayer δ

845:   opAsObjectCode : R opLayer δ → R objLayer δ

846:   id_preserved : ∀ x, morCode (S.id x) = idCode (objCode x)

847:   comp_preserved : ∀ f g h,

848:     S.comp f g = some h →

849:       compCode (morCode f) (morCode g) = some (morCode h)

850:   rel_preserved : ∀ r x y,

851:     S.relationHolds r x y ↔

852:       relationCodeHolds (relCode r) (objCode x) (objCode y)

853:   op_preserved : ∀ o xs,

854:     objCode (S.applyOp o xs) =

855:       opCodeApply o (opCode o) (fun i => objCode (xs i))

856:   rule_preserved : ∀ r ps,

857:     proofCode (S.applyRule r ps) =

858:       ruleCodeApply r (ruleCode r) (fun i => proofCode (ps i))

859:   proofConclusion_preserved : ∀ p,

860:     objCode (S.proofConclusion p) = proofConclusionCode (proofCode p)

861:   opAsObject_preserved : ∀ o,

862:     objCode (S.opAsObject o) = opAsObjectCode (opCode o)

863: 

864: /-- A faithful realisation is a structure-preserving R map that is injective

865: on the syntactic carriers it claims to represent. -/

866: structure FaithfulRRealisation

867:     (S : FormalPresentation) (δ : Type := Bool) :

868:     Type extends StructurePreservingRMap S δ where

869:   obj_injective : Function.Injective objCode

870:   mor_injective : Function.Injective morCode

871:   rel_injective : Function.Injective relCode

872:   op_injective : Function.Injective opCode

873:   rule_injective : Function.Injective ruleCode

874:   proof_injective : Function.Injective proofCode

875: 

```

Lines 1082–1089:

```text

1082: namespace AdmissibleFormalSystem

1083: 

1084: /-- Semantic preservability is the explicit missing data for the generic

1085: Full GUT theorem: a faithful, structure-preserving R-realisation. -/

1086: def SemanticsPreservable (S : AdmissibleFormalSystem) : Prop :=

1087:   Nonempty (FaithfulRRealisation S.toFormalPresentation Bool)

1088: 

1089: end AdmissibleFormalSystem

```

Lines 1561–1603:

```text

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

1579:   idCode := fun xCode =>

1580:     finiteObjectWord S.Mor

1581:       (S.id (finiteObjectWordDecodeD S.Obj (Classical.choice hD1.obj) xCode))

1582:   compCode := finitePresentationCompCode S

1583:   relationCodeHolds :=

1584:     finitePresentationRelationCodeHolds S (Classical.choice hD1.obj)

1585:   opCodeApply := fun o _ xs =>

1586:     finiteObjectWord S.Obj

1587:       (S.applyOp o

1588:         (fun i => finiteObjectWordDecodeD S.Obj (Classical.choice hD1.obj) (xs i)))

1589:   ruleCodeApply := fun r _ ps =>

1590:     finiteObjectWord S.Proof

1591:       (S.applyRule r

1592:         (fun i => finiteObjectWordDecodeD S.Proof (Classical.choice hD1.proof) (ps i)))

1593:   proofConclusionCode := fun pCode =>

1594:     finiteObjectWord S.Obj

1595:       (S.proofConclusion

1596:         (finiteObjectWordDecodeD S.Proof (Classical.choice hD1.proof) pCode))

1597:   opAsObjectCode := fun oCode =>

1598:     finiteObjectWord S.Obj

1599:       (S.opAsObject

1600:         (finiteObjectWordDecodeD S.Op (Classical.choice hD1.op) oCode))

1601:   id_preserved := by

1602:     intro x

1603:     simp [finiteObjectWordDecodeD_finiteObjectWord]

```

Lines 1633–1639:

```text

1633: theorem finite_formal_presentations_are_faithfully_R_representable

1634:     (S : FormalPresentation)

1635:     [Fintype S.Obj] [Fintype S.Mor] [Fintype S.Rel]

1636:     [Fintype S.Op] [Fintype S.Rule] [Fintype S.Proof]

1637:     (hD1 : S.SatisfiesD1) :

1638:     Nonempty (FaithfulRRealisation S Bool) :=

1639:   ⟨finitePresentationFaithfulRRealisation S hD1⟩

```

Lines 2169–2177:

```text

2169: noncomputable def encodablePresentationFaithfulRStreamRealisation

2170:     (S : FormalPresentation)

2171:     [Encodable S.Obj] [Encodable S.Mor] [Encodable S.Rel]

2172:     [Encodable S.Op] [Encodable S.Rule] [Encodable S.Proof]

2173:     (hD1 : S.SatisfiesD1) :

2174:     FaithfulRStreamRealisation S where

2175:   objCode := encodableStreamCode S.Obj

2176:   morCode := encodableStreamCode S.Mor

2177:   relCode := encodableStreamCode S.Rel

```

Lines 2233–2241:

```text

2233: /-- Every encodable presentation satisfying D1 has a faithful,

2234: structure-preserving stream R-realisation. -/

2235: theorem encodable_formal_presentations_are_faithfully_RStream_representable

2236:     (S : FormalPresentation)

2237:     [Encodable S.Obj] [Encodable S.Mor] [Encodable S.Rel]

2238:     [Encodable S.Op] [Encodable S.Rule] [Encodable S.Proof]

2239:     (hD1 : S.SatisfiesD1) :

2240:     Nonempty (FaithfulRStreamRealisation S) :=

2241:   ⟨encodablePresentationFaithfulRStreamRealisation S hD1⟩

```

Lines 2482–2505:

```text

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

## /Users/ren/repos/生生不息/docs-next/10_formal_形式/claim-status-ledger.md

SHA-256: `6a7b33a057497afcba31533693a3e775efae594b2e39968112975325c954b200`

Lines 1–17:

```text

1: # Claim Status Ledger — R-Family / Claim Z / GUT

2: 

3: > v0.8 · 2026-05-21. This page is the human status ledger for the current `wen-substrate` / GUT line. It does not replace Lean source. It prevents over-reading headline names such as `T5_general`, `universal_sayability`, `scoped_gut_a_closed`, `scoped_coordinate_full_gut`, or `conditional_absolute_full_gut` as stronger than their theorem statements.

4: 

5: ## Reading Rule

6: 

7: Use the strongest claim allowed by the theorem type, not by the file title or surrounding doctrine prose.

8: 

9: - **closed** means there is a non-placeholder Lean theorem/definition whose statement carries the claimed content.

10: - **scoped** means the theorem is real but restricted by base, carrier level, or supplied structure fields.

11: - **schema** means the Lean object fixes the shape of a claim while leaving fields or hypotheses to instantiation sites.

12: - **external route** means a standard mathematical theorem suggests a reduction, but this repository has not stated and proved the exact bridge theorem.

13: - **sketch** means the document names a plausible research direction without a theorem-grade reduction.

14: - **placeholder** means the statement is intentionally `True`, `coherent := True`, or otherwise vacuous at the load-bearing point.

15: - **open** means the repository states the obligation but does not provide the proof.

16: 

17: ## Current Status

```
