import FormationRoutes

/-!
# Reclaiming a formed coupling into a third actual formation

This adds real, work-consuming transitions to FormationRoutes while preserving
its state, constituent accounting and existing recipes. Releasing a spanning bar
returns its one material part to raw stock; no historical work is refunded.
The new AC dyad and Z=((a,c),b) use the ordinary two-joint assembly law. Earlier
products persist through release and later completion. The original two ports,
recipes, contact law and recovery of an intact bar part remain local premises.

Old steps/histories embed forward. Old negative reachability results do not
automatically transfer to this enlarged event repertoire. No ethical predicate
or unconditional preference for retention, transformation or Z is supplied.
-/

namespace ReconfigurableRoutes

open FormationRoutes

def dyadAC : Tree := .join (.atom .a) (.atom .c)
def zForm : Tree := .join dyadAC (.atom .b)

theorem z_common_address :
    inspect zForm [.left,.right] = some .c ∧
    inspect leftForm [.left,.right] = some .b ∧
    inspect rightForm [.left,.right] = none := by
  exact ⟨rfl,rfl,rfl⟩

theorem z_distinct : zForm ≠ leftForm ∧ zForm ≠ rightForm := by decide

inductive Event where
  | old (event : FormationRoutes.Event)
  | release | startAC | finishZ
  deriving DecidableEq, Repr

def advance (s : State) : Event → State
  | .old e => FormationRoutes.advance s e
  | .release => {s with raw := s.raw+1, work := s.work-1, spent := s.spent+1, bar := .absent}
  | .startAC => {s with raw := s.raw-2, work := s.work-1, spent := s.spent+1, pending := some dyadAC}
  | .finishZ => {s with raw := s.raw-1, work := s.work-1, spent := s.spent+1,
                        pending := none, products := zForm :: s.products}

def Enabled (s : State) : Event → Prop
  | .old e => FormationRoutes.Enabled s e
  | .release => Spans s.bar ∧ 1 ≤ s.work
  | .startAC => s.pending = none ∧ 2 ≤ s.raw ∧ 1 ≤ s.work
  | .finishZ => s.pending = some dyadAC ∧ 1 ≤ s.raw ∧ 1 ≤ s.work

instance enabledDecidable (s : State) (e : Event) : Decidable (Enabled s e) := by
  cases e <;> unfold Enabled <;> infer_instance

def Step (s : State) (e : Event) (t : State) : Prop := Enabled s e ∧ t = advance s e
def process : Generative.Process State Event := ⟨Step⟩

def oldEvents : List FormationRoutes.Event :=
  [.receive,.attach,.repair,.startAB,.startBC,.finishLeft,.finishRight,.syncLeft,.syncRight]

def events : List Event := oldEvents.map Event.old ++ [.release,.startAC,.finishZ]
def children (s : State) : List State := (events.filter (fun e => decide (Enabled s e))).map (advance s)

theorem finite_branching (s t : State) : (∃ e, Step s e t) ↔ t ∈ children s := by
  constructor
  · rintro ⟨e,enabled,rfl⟩
    apply List.mem_map.mpr
    refine ⟨e,List.mem_filter.mpr ⟨?_,by simpa using enabled⟩,rfl⟩
    cases e with
    | old e => cases e <;> simp [events,oldEvents]
    | release | startAC | finishZ => simp [events]
  · intro ht
    obtain ⟨e,he,rfl⟩ := List.mem_map.mp ht
    exact ⟨e,of_decide_eq_true (List.mem_filter.mp he).2,rfl⟩

theorem old_step {s t : State} {e : FormationRoutes.Event}
    (h : FormationRoutes.Step s e t) : Step s (.old e) t := h

theorem old_trace {s t : State} {es : List FormationRoutes.Event}
    (h : Generative.Trace FormationRoutes.process s es t) :
    Generative.Trace process s (es.map Event.old) t := by
  induction h with
  | nil => exact .nil _
  | cons hs _ ih => exact .cons (old_step hs) ih

def Synchronized : Event → Prop
  | .old e => FormationRoutes.Synchronized e
  | _ => False

def bypassProcess : Generative.Process State Event := ⟨fun s e t => Step s e t ∧ ¬ Synchronized e⟩
def retainingProcess : Generative.Process State Event := ⟨fun s e t => Step s e t ∧ e ≠ .release⟩

theorem step_accounts {s t : State} {e : Event} (h : Step s e t) :
    material t = material s ∧ workAccount t = workAccount s := by
  cases e with
  | old e => exact FormationRoutes.step_accounts h
  | release =>
    obtain ⟨he,rfl⟩ := h
    cases hb : s.bar with
    | absent | loose => simp [Enabled,Spans,hb] at he
    | span p q =>
      simp only [Enabled] at he
      simp [advance,material,workAccount,sourceRaw,sourceWork,partialParts,hb,barParts]
      exact ⟨by omega,by omega⟩
  | startAC | finishZ =>
    obtain ⟨he,rfl⟩ := h
    simp_all [Enabled,advance,material,workAccount,sourceRaw,sourceWork,partialParts,
      productParts,parts,dyadAC,zForm]
    all_goals (first | exact ⟨by omega,by omega⟩ | omega)

theorem trace_accounts {s t : State} {es : List Event}
    (h : Generative.Trace process s es t) : material t = material s ∧ workAccount t = workAccount s := by
  induction h with
  | nil => exact ⟨rfl,rfl⟩
  | cons hs _ ih =>
    have one := step_accounts hs
    exact ⟨ih.1.trans one.1,ih.2.trans one.2⟩

theorem release_preserves_products_and_history {s t : State} (h : Step s .release t) :
    t.products = s.products ∧ t.pending = s.pending ∧ t.raw = s.raw+1 ∧
    t.work+1 = s.work ∧ t.spent = s.spent+1 ∧ t.bar = .absent := by
  obtain ⟨he,rfl⟩ := h
  simp only [Enabled] at he
  refine ⟨rfl,rfl,rfl,?_,rfl,rfl⟩
  simp only [advance]
  omega

theorem bypass_step_progress {s t : State} {e : Event}
    (h : Step s e t) (bypass : ¬ Synchronized e)
    (bound : manualProgress s ≤ s.spent) : manualProgress t ≤ t.spent := by
  cases e with
  | old e => exact FormationRoutes.bypass_step_progress h bypass bound
  | release =>
    rw [h.2]
    exact Nat.le_trans bound (Nat.le_succ s.spent)
  | startAC | finishZ =>
    obtain ⟨he,rfl⟩ := h
    simp_all [Enabled,advance,manualProgress]
    all_goals omega

theorem bypass_trace_progress {s t : State} {es : List Event}
    (h : Generative.Trace bypassProcess s es t)
    (bound : manualProgress s ≤ s.spent) : manualProgress t ≤ t.spent := by
  induction h with
  | nil => exact bound
  | cons hs _ ih => exact ih (bypass_step_progress hs.1 hs.2 bound)

theorem forget_bypass {s t : State} {es : List Event}
    (h : Generative.Trace bypassProcess s es t) : Generative.Trace process s es t := by
  induction h with
  | nil => exact .nil _
  | cons hs _ ih => exact .cons hs.1 ih

theorem old_bypass_trace {s t : State} {es : List FormationRoutes.Event}
    (h : Generative.Trace FormationRoutes.bypassProcess s es t) :
    Generative.Trace bypassProcess s (es.map Event.old) t := by
  induction h with
  | nil => exact .nil _
  | cons hs _ ih => exact .cons ⟨old_step hs.1,hs.2⟩ ih

theorem bypass_output_bound (raw work : Nat) {t : State} {es : List Event}
    (h : Generative.Trace bypassProcess (initial raw work) es t) : 2*t.products.length ≤ work := by
  have progress := bypass_trace_progress h (by simp [initial,manualProgress])
  have account := (trace_accounts (forget_bypass h)).2
  simp only [initial,workAccount,sourceWork,Option.getD_some,Nat.add_zero] at account
  unfold manualProgress at progress
  omega

def ThreePartProducts (s : State) : Prop := productParts s.products = 3*s.products.length

theorem step_three_part_products {s t : State} {e : Event}
    (h : Step s e t) (shapes : ThreePartProducts s) : ThreePartProducts t := by
  obtain ⟨he,rfl⟩ := h
  cases e with
  | old e =>
    cases e with
    | receive =>
      cases hs : s.source <;> simpa [advance,FormationRoutes.advance,hs,ThreePartProducts] using shapes
    | attach | repair | startAB | startBC => exact shapes
    | finishLeft | finishRight | syncLeft | syncRight =>
      simp_all [advance,FormationRoutes.advance,ThreePartProducts,productParts,parts,
        leftForm,rightForm,dyadAB,dyadBC]
      all_goals omega
  | release | startAC => exact shapes
  | finishZ =>
    simp_all [advance,ThreePartProducts,productParts,parts,zForm,dyadAC]
    omega

theorem trace_three_part_products {s t : State} {es : List Event}
    (h : Generative.Trace process s es t) (shapes : ThreePartProducts s) : ThreePartProducts t := by
  induction h with
  | nil => exact shapes
  | cons hs _ ih => exact ih (step_three_part_products hs shapes)

theorem trace_product_material_bound {s t : State} {es : List Event}
    (h : Generative.Trace process s es t) (shapes : ThreePartProducts s) :
    2+3*t.products.length ≤ material s := by
  have shape := trace_three_part_products h shapes
  have account := (trace_accounts h).1
  unfold ThreePartProducts at shape
  unfold material at account ⊢
  omega

theorem retaining_starved_step {s t : State} {e : Event}
    (h : Step s e t) (retain : e ≠ .release) (unfed : s.source = none)
    (short : s.raw + partialParts s ≤ 2) :
    t.source = none ∧ t.raw + partialParts t ≤ 2 ∧ t.products = s.products := by
  obtain ⟨he,rfl⟩ := h
  cases e with
  | old e =>
    cases e <;> simp_all [Enabled,FormationRoutes.Enabled,advance,FormationRoutes.advance,
      partialParts,parts,dyadAB,dyadBC]
    all_goals omega
  | release => exact False.elim (retain rfl)
  | startAC | finishZ =>
    simp_all [Enabled,advance,partialParts,parts,dyadAC]
    all_goals omega

theorem retaining_starved_trace {s t : State} {es : List Event}
    (h : Generative.Trace retainingProcess s es t) (unfed : s.source = none)
    (short : s.raw+partialParts s ≤ 2) :
    t.source = none ∧ t.raw+partialParts t ≤ 2 ∧ t.products = s.products := by
  induction h with
  | nil => exact ⟨unfed,short,rfl⟩
  | cons hs _ ih =>
    have one := retaining_starved_step hs.1 hs.2 unfed short
    have tail := ih one.1 one.2.1
    exact ⟨tail.1,tail.2.1,tail.2.2.trans one.2.2⟩

theorem unfed_step_spends {s t : State} {e : Event}
    (h : Step s e t) (unfed : s.source = none) : t.source = none ∧ t.work+1 = s.work := by
  cases e with
  | old e => exact FormationRoutes.unfed_step_spends h unfed
  | release | startAC | finishZ =>
    obtain ⟨he,rfl⟩ := h
    simp_all [Enabled,advance]
    all_goals omega

theorem zero_work_trace_constant {s t : State} {es : List Event}
    (h : Generative.Trace process s es t) (unfed : s.source = none) (empty : s.work = 0) : t=s := by
  cases h with
  | nil => rfl
  | cons hs _ => have spent := (unfed_step_spends hs unfed).2; omega

theorem small_fresh_step_no_product {s t : State} {e : Event}
    (h : Step s e t) (unfed : s.source = none) (fresh : s.pending = none)
    (short : s.raw ≤ 2) : t.products = s.products := by
  obtain ⟨he,rfl⟩ := h
  cases e with
  | old e =>
    cases e <;> simp_all [Enabled,FormationRoutes.Enabled,advance,FormationRoutes.advance]
    all_goals omega
  | release | startAC | finishZ => simp_all [Enabled,advance]

theorem small_one_work_no_product {s t : State} {es : List Event}
    (h : Generative.Trace process s es t) (unfed : s.source = none)
    (fresh : s.pending = none) (short : s.raw ≤ 2) (budget : s.work ≤ 1) :
    t.products = s.products := by
  cases h with
  | nil => rfl
  | cons hs tail =>
    have first := small_fresh_step_no_product hs unfed fresh short
    have next := unfed_step_spends hs unfed
    have empty := zero_work_trace_constant tail next.1 (by omega)
    rw [empty]
    exact first

/-- The L/R prefix retains exactly the parts and work needed for release and Z. -/
def coupled (remaining : Nat) (products : List Tree) : State :=
  ⟨none,3*remaining+2,remaining+3,1+products.length,.span .left .right,none,products⟩

theorem coupled_prefix (n : Nat) :
    Generative.Trace process (initial (3*n+3) (n+4)) [.old .receive,.old .attach] (coupled n []) := by
  refine .cons (old_step (receive_step _ _)) (.cons ?_ (.nil _))
  constructor
  · simp [Enabled,FormationRoutes.Enabled,stocked]
  · simp [coupled,advance,FormationRoutes.advance,stocked]

theorem coupled_step (f : Form) (n : Nat) (products : List Tree) :
    Step (coupled (n+1) products) (.old (syncEvent f)) (coupled n (treeOf f :: products)) := by
  cases f <;> constructor
  all_goals simp [Enabled,FormationRoutes.Enabled,coupled,syncEvent,treeOf,Spans,
    advance,FormationRoutes.advance,Nat.mul_add]
  all_goals omega

theorem coupled_list (forms : List Form) (products : List Tree) :
    Generative.Trace process (coupled forms.length products)
      (forms.map (fun f => Event.old (syncEvent f))) (coupled 0 (pushed forms products)) := by
  induction forms generalizing products with
  | nil => exact .nil _
  | cons f fs ih => exact .cons (coupled_step f fs.length products) (ih (treeOf f :: products))

def zPending (bar : Bar) (surplus work spent : Nat) (products : List Tree) : State :=
  ⟨none,surplus+1,work+1,spent+1,bar,some dyadAC,products⟩

def zResult (bar : Bar) (surplus work spent : Nat) (products : List Tree) : State :=
  ⟨none,surplus,work,spent+2,bar,none,zForm::products⟩

theorem manual_z (bar : Bar) (surplus work spent : Nat) (products : List Tree) :
    Generative.Trace bypassProcess ⟨none,surplus+3,work+2,spent,bar,none,products⟩
      [.startAC,.finishZ] (zResult bar surplus work spent products) := by
  refine .cons (m := zPending bar surplus work spent products) ?_ ?_
  · simp [bypassProcess,Step,Enabled,advance,zPending,Synchronized]
  · refine .cons (m := zResult bar surplus work spent products) ?_ (.nil _)
    simp [bypassProcess,Step,Enabled,advance,zPending,zResult,Synchronized]

theorem reclaim_then_z (products : List Tree) :
    Generative.Trace process (coupled 0 products) [.release,.startAC,.finishZ]
      (zResult .absent 0 0 (2+products.length) products) := by
  refine .cons (m := ⟨none,3,2,2+products.length,.absent,none,products⟩) ?_ ?_
  · constructor
    · simp [Enabled,coupled,Spans]
    · simp [coupled,advance]; omega
  · exact forget_bypass (manual_z .absent 0 0 (2+products.length) products)

theorem formed_then_reconfigured_history (forms : List Form) :
    Generative.Trace process (initial (3*forms.length+3) (forms.length+4))
      ([.old .receive,.old .attach] ++ forms.map (fun f => Event.old (syncEvent f)) ++
        [.release,.startAC,.finishZ])
      (zResult .absent 0 0 (2+(pushed forms []).length) (pushed forms [])) := by
  apply Generative.trace_append_iff.mpr
  refine ⟨coupled 0 (pushed forms []),?_,reclaim_then_z _⟩
  exact Generative.trace_append_iff.mpr ⟨coupled forms.length [],coupled_prefix _,coupled_list forms []⟩

theorem final_reconfigured_costs (forms : List Form) :
    let final := zResult .absent 0 0 (2+(pushed forms []).length) (pushed forms [])
    final.products.length = forms.length+1 ∧ final.spent = forms.length+4 ∧
    final.raw = 0 ∧ final.work = 0 ∧ final.bar = .absent := by
  simp [zResult,pushed_length,Nat.add_comm]
  omega

theorem repeated_use_strict_threshold (k : Nat) (many : 3 ≤ k)
    {es : List Event} {t : State}
    (h : Generative.Trace bypassProcess (initial (3*k+3) (k+4)) es t) :
    t.products.length < k+1 := by
  have bound := bypass_output_bound (3*k+3) (k+4) h
  omega

theorem retained_material_cannot_complete {t : State} {es : List Event} (products : List Tree)
    (h : Generative.Trace retainingProcess (coupled 0 products) es t) : t.products = products := by
  exact (retaining_starved_trace h rfl (by simp [coupled,partialParts])).2.2

def allThree : State := zResult .absent 0 0 4 [rightForm,leftForm]

theorem two_uses_then_reclaim :
    Generative.Trace process (initial 9 6)
      [.old .receive,.old .attach,.old .syncLeft,.old .syncRight,.release,.startAC,.finishZ]
      allThree := by
  exact formed_then_reconfigured_history [.left,.right]

/-- The same source, completed products, stores and spent work are possible manually. -/
theorem two_use_ordinary_tie :
    Generative.Trace bypassProcess (initial 9 6)
      [.old .receive,.old .startAB,.old .finishLeft,.old .startBC,.old .finishRight,.startAC,.finishZ]
      allThree := by
  refine .cons ⟨old_step (receive_step 9 6),by simp [Synchronized,FormationRoutes.Synchronized]⟩ ?_
  apply Generative.trace_append_iff.mpr
  refine ⟨manualResult .left .absent 6 4 0 [],old_bypass_trace (manual_two_steps .left .absent 6 4 0 []),?_⟩
  apply Generative.trace_append_iff.mpr
  exact ⟨manualResult .right .absent 3 2 2 [leftForm],
    old_bypass_trace (manual_two_steps .right .absent 3 2 2 [leftForm]),
    manual_z .absent 0 0 4 [rightForm,leftForm]⟩

theorem direct_z_from_small_source :
    Generative.Trace bypassProcess (initial 3 2) [.old .receive,.startAC,.finishZ]
      (zResult .absent 0 0 0 []) := by
  exact .cons ⟨old_step (receive_step 3 2),by simp [Synchronized,FormationRoutes.Synchronized]⟩
    (manual_z .absent 0 0 0 [])

def prematurelyCoupled : State := ⟨none,2,1,1,.span .left .right,none,[]⟩

theorem premature_coupling_history :
    Generative.Trace process (initial 3 2) [.old .receive,.old .attach] prematurelyCoupled := by
  exact .cons (old_step (receive_step 3 2)) (.cons ⟨by decide,rfl⟩ (.nil _))

theorem premature_coupling_loses_completion {t : State} {es : List Event}
    (h : Generative.Trace process prematurelyCoupled es t) : t.products = [] := by
  exact small_one_work_no_product h rfl rfl (by decide) (by decide)

theorem premature_release_exhausts_work :
    Step prematurelyCoupled .release ⟨none,3,0,2,.absent,none,[]⟩ := by
  exact ⟨by decide,rfl⟩

/-- Both further L/R and Z are supported here; Z no longer requires release. -/
def commonChoice : State := ⟨none,3,3,3,.span .left .right,none,[rightForm,leftForm]⟩

theorem common_choice_actual_history :
    Generative.Trace process (initial 10 6)
      [.old .receive,.old .attach,.old .syncLeft,.old .syncRight] commonChoice := by
  refine .cons (old_step (receive_step 10 6)) ?_
  refine .cons (m := ⟨none,9,5,1,.span .left .right,none,[]⟩) ⟨by decide,rfl⟩ ?_
  refine .cons (m := ⟨none,6,4,2,.span .left .right,none,[leftForm]⟩) ⟨by decide,rfl⟩ ?_
  exact .cons ⟨by decide,rfl⟩ (.nil _)

theorem common_can_reuse_coupling :
    Generative.Trace process commonChoice [.old .syncLeft]
      ⟨none,0,2,4,.span .left .right,none,[leftForm,rightForm,leftForm]⟩ := by
  exact .cons ⟨by decide,rfl⟩ (.nil _)

theorem common_can_form_z_without_release :
    Generative.Trace process commonChoice [.startAC,.finishZ]
      (zResult (.span .left .right) 0 1 3 [rightForm,leftForm]) := by
  exact forget_bypass (manual_z (.span .left .right) 0 1 3 [rightForm,leftForm])

theorem common_can_release_then_z :
    Generative.Trace process commonChoice [.release,.startAC,.finishZ]
      (zResult .absent 1 0 4 [rightForm,leftForm]) := by
  refine .cons (m := ⟨none,4,2,4,.absent,none,[rightForm,leftForm]⟩) ⟨by decide,rfl⟩ ?_
  exact forget_bypass (manual_z .absent 1 0 4 [rightForm,leftForm])

theorem common_cannot_add_two_completions {t : State} {es : List Event}
    (h : Generative.Trace process commonChoice es t) : t.products.length ≤ 3 := by
  have bound := trace_product_material_bound h (by decide)
  have fixed : material commonChoice = 12 := rfl
  rw [fixed] at bound
  omega

theorem ordinary_z_keeps_more_work_and_bar :
    let direct := zResult (.span .left .right) 0 1 3 [rightForm,leftForm]
    let released := zResult .absent 1 0 4 [rightForm,leftForm]
    direct.products = released.products ∧ direct.work = released.work+1 ∧
    direct.spent+1 = released.spent ∧ direct.bar = .span .left .right ∧
    released.bar = .absent ∧ released.raw = direct.raw+1 := by
  decide

end ReconfigurableRoutes
