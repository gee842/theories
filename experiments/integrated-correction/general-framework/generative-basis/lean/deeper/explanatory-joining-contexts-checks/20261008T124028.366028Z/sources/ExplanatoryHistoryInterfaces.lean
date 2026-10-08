import ExplanatoryContextualStructure

/-! Instantiate on admitted histories of one process. Histories and probes
share one joining law; no determinism of the underlying process is assumed.
The retained scope is continuation compatibility, not every historical fact. -/
namespace Generative.ExplanatoryHistoryInterfaces
open ExplanatoryJoining ExplanatoryLocalUnits ExplanatoryJoiningContexts
open ExplanatoryUniqueness ExplanatoryContextualStructure
universe u v w
variable {S : Type u} {A : Type v}

def Boundaries {P : Process S A} (x y : Admitted P) : Prop :=
  x.val.start = y.val.start ∧ x.val.finish = y.val.finish

theorem boundary_join_replacement {P : Process S A} {a b c a' b' : Admitted P}
    (ha : Boundaries a a') (hb : Boundaries b b') (hc : traceJoin P a b c) :
    ∃ d, traceJoin P a' b' d ∧ Boundaries c d := by
  have joint : Joint P a'.val b'.val :=
    ⟨a'.property, b'.property, ha.2.symm.trans (hc.1.2.2.trans hb.1)⟩
  let d : Admitted P := ⟨merge a'.val b'.val, joint_merge_valid joint⟩
  refine ⟨d, ⟨joint, rfl⟩, ?_, ?_⟩
  · exact (congrArg Fragment.start hc.2).symm.trans ha.1
  · exact (congrArg Fragment.finish hc.2).symm.trans hb.2

theorem boundaries_compatible (P : Process S A) : Compatible (traceJoin P) (@Boundaries S A P) := by
  intro x y h a
  have rev : Boundaries y x := ⟨h.1.symm, h.2.symm⟩
  have refl : Boundaries a a := ⟨rfl, rfl⟩
  refine ⟨?_, ?_, ?_, ?_⟩
  · intro z hz
    exact boundary_join_replacement refl h hz
  · intro w hw
    obtain ⟨z, hz, he⟩ := boundary_join_replacement refl rev hw
    exact ⟨z, hz, he.1.symm, he.2.symm⟩
  · intro z hz
    exact boundary_join_replacement h refl hz
  · intro w hw
    obtain ⟨z, hz, he⟩ := boundary_join_replacement rev refl hw
    exact ⟨z, hz, he.1.symm, he.2.symm⟩

theorem all_joining_contexts_iff_boundaries (P : Process S A) (x y : Admitted P) :
    Same (traceJoin P) x y ↔ Boundaries x y := by
  constructor
  · intro h
    have left : Composable (traceJoin P) (traceIdle P x.val.start) x :=
      ⟨x, joined_idle_left x.property⟩
    have right : Composable (traceJoin P) x (traceIdle P x.val.finish) :=
      ⟨x, joined_idle_right x.property⟩
    obtain ⟨_, hl⟩ := (same_preserves_joinability (same_refl _ _) h).mp left
    obtain ⟨_, hr⟩ := (same_preserves_joinability h (same_refl _ _)).mp right
    exact ⟨hl.1.2.2, hr.1.2.2.symm⟩
  · exact compatible_refines_same (boundaries_compatible P)

/-- Earlier local probes generate the same distinctions as every nested
joining arrangement; a specified small interface is proved complete here. -/
theorem local_probes_complete_for_all_contexts (P : Process S A) (x y : Admitted P) :
    SameAnswers (probeTarget P) x.val y.val ↔ Same (traceJoin P) x y :=
  (same_probes_iff_boundaries x.property y.property).trans
    (all_joining_contexts_iff_boundaries P x y).symm

theorem every_exact_joining_account_retains_interfaces {P : Process S A} {C : Type w}
    {p : Account (Admitted P) C} (hp : Exact (target (traceJoin P)) p)
    {x y : Admitted P} (h : p.encode x = p.encode y) : Boundaries x y :=
  (all_joining_contexts_iff_boundaries P x y).mp (exact_same_code hp h)

def interfaceAccount (P : Process S A) : Account (Admitted P) (S × S) where
  encode x := (x.val.start, x.val.finish)
  read code c := ∃ x : Admitted P, (x.val.start, x.val.finish) = code ∧ Possible (traceJoin P) c x

theorem interface_account_exact (P : Process S A) : Exact (target (traceJoin P)) (interfaceAccount P) := by
  intro x c
  constructor
  · rintro ⟨y, eq, hy⟩
    have hb : Boundaries y x := ⟨congrArg Prod.fst eq, congrArg Prod.snd eq⟩
    exact ((all_joining_contexts_iff_boundaries P y x).mpr hb c).mp hy
  · intro hx
    exact ⟨x, rfl, hx⟩

theorem interface_account_reduced (P : Process S A) : Reduced (target (traceJoin P)) (interfaceAccount P) := by
  intro x y h
  obtain ⟨hs, ht⟩ := (all_joining_contexts_iff_boundaries P x y).mp h
  exact Prod.ext hs ht

/-- Different realized activities can have the same required interface. This
is a positive nonidentity witness, not a counterexample to common necessity. -/
def loopHistory (a : Bool) : Admitted loopProcess := ⟨loop a, loop_valid a⟩

theorem different_histories_same_required_interface :
    loopHistory false ≠ loopHistory true ∧
    Same (traceJoin loopProcess) (loopHistory false) (loopHistory true) := by
  constructor
  · intro eq
    have bad := congrArg (fun x : Admitted loopProcess => x.val.word) eq
    cases bad
  · exact (all_joining_contexts_iff_boundaries _ _ _).mpr ⟨rfl, rfl⟩

theorem all_exact_accounts_factor_through_interfaces {P : Process S A} {C : Type w}
    {p : Account (Admitted P) C} (hp : Exact (target (traceJoin P)) p) :
    ∀ c, Used p c → ∃ d, Matches p (interfaceAccount P) c d ∧
      ∀ e, Matches p (interfaceAccount P) c e → e = d := by
  intro c hc
  obtain ⟨d, _, hd⟩ := matches_total_on_used p (interfaceAccount P) hc
  exact ⟨d, hd, fun e he => matches_functional hp (interface_account_reduced P) he hd⟩

/-- Retaining the full history is also exact. Minimality of an account is
not a requirement for preserving the common interface. -/
def historyAccount (P : Process S A) : Account (Admitted P) (Admitted P) where
  encode x := x
  read x c := Possible (traceJoin P) c x

theorem history_account_exact (P : Process S A) :
    Exact (target (traceJoin P)) (historyAccount P) := fun _ _ => Iff.rfl

theorem history_account_need_not_be_reduced :
    ¬ Reduced (target (traceJoin loopProcess)) (historyAccount loopProcess) := by
  intro h
  exact different_histories_same_required_interface.1
    (h _ _ different_histories_same_required_interface.2)

end Generative.ExplanatoryHistoryInterfaces

#print axioms Generative.ExplanatoryHistoryInterfaces.boundary_join_replacement
#print axioms Generative.ExplanatoryHistoryInterfaces.boundaries_compatible
#print axioms Generative.ExplanatoryHistoryInterfaces.all_joining_contexts_iff_boundaries
#print axioms Generative.ExplanatoryHistoryInterfaces.local_probes_complete_for_all_contexts
#print axioms Generative.ExplanatoryHistoryInterfaces.every_exact_joining_account_retains_interfaces
#print axioms Generative.ExplanatoryHistoryInterfaces.interface_account_exact
#print axioms Generative.ExplanatoryHistoryInterfaces.interface_account_reduced
#print axioms Generative.ExplanatoryHistoryInterfaces.different_histories_same_required_interface
#print axioms Generative.ExplanatoryHistoryInterfaces.all_exact_accounts_factor_through_interfaces
#print axioms Generative.ExplanatoryHistoryInterfaces.history_account_exact
#print axioms Generative.ExplanatoryHistoryInterfaces.history_account_need_not_be_reduced
