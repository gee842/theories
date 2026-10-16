import GenerativeCore

/-! Formation beyond an installed construction repertoire, and accountable
description revision. This is a conditional relational assembly model, not
unlimited physical novelty or a biological mechanism. All events, including
constructor coupling, belong to one encompassing process. -/

namespace Generative.NewPossibilities

universe u v w x

/-- A description is sufficient for specified response questions on a domain. -/
def AdequateOn {S : Type u} {D : Type v} {Q : Type w} {Y : Type x}
    (domain : S → Prop) (describe : S → D) (response : S → Q → Y) : Prop :=
  ∀ s t, domain s → domain t → describe s = describe t →
    ∀ q, response s q = response t q

theorem collision_defeats_adequacy {S : Type u} {D : Type v} {Q : Type w} {Y : Type x}
    {domain : S → Prop} {describe : S → D} {response : S → Q → Y}
    {s t : S} {q : Q} (hs : domain s) (ht : domain t)
    (same : describe s = describe t) (different : response s q ≠ response t q) :
    ¬ AdequateOn domain describe response := by
  intro adequate
  exact different (adequate s t hs ht same q)

/-- Refinement must preserve old distinctions. It does not guarantee acquisition. -/
theorem refinement_preserves_adequacy
    {S : Type u} {D E : Type v} {Q : Type w} {Y : Type x}
    {domain : S → Prop} {describe : S → D} {refined : S → E}
    {response : S → Q → Y}
    (refines : ∀ s t, refined s = refined t → describe s = describe t)
    (adequate : AdequateOn domain describe response) :
    AdequateOn domain refined response := by
  intro s t hs ht same q
  exact adequate s t hs ht (refines s t same) q

/-- A sufficient extension exists as a semantic construction. Its full profile
may be unavailable or infinite; this is not an implemented learner. -/
theorem response_profile_is_sufficient
    {S : Type u} {D : Type v} {Q : Type w} {Y : Type x}
    (domain : S → Prop) (describe : S → D) (response : S → Q → Y) :
    AdequateOn domain (fun s => (describe s, response s)) response := by
  intro s t _ _ same q
  exact congrFun (congrArg Prod.snd same) q

theorem adequacy_restricts_domain
    {S : Type u} {D : Type v} {Q : Type w} {Y : Type x}
    {small large : S → Prop} {describe : S → D} {response : S → Q → Y}
    (included : ∀ s, small s → large s)
    (adequate : AdequateOn large describe response) :
    AdequateOn small describe response := by
  intro s t hs ht same q
  exact adequate s t (included s hs) (included t ht) same q

/-- New questions extend an old language without erasing its meanings. -/
def extendResponses {S : Type u} {Q R : Type v} {Y : Type w}
    (old : S → Q → Y) (new : S → R → Y) (s : S) : Sum Q R → Y
  | .inl q => old s q
  | .inr r => new s r

theorem old_response_preserved {S : Type u} {Q R : Type v} {Y : Type w}
    (old : S → Q → Y) (new : S → R → Y) (s : S) (q : Q) :
    extendResponses old new s (.inl q) = old s q := rfl

theorem extended_adequacy_iff {S : Type u} {D Q R : Type v} {Y : Type w}
    (domain : S → Prop) (describe : S → D)
    (old : S → Q → Y) (new : S → R → Y) :
    AdequateOn domain describe (extendResponses old new) ↔
      AdequateOn domain describe old ∧ AdequateOn domain describe new := by
  constructor
  · intro h
    exact ⟨fun s t hs ht e q => h s t hs ht e (.inl q),
      fun s t hs ht e r => h s t hs ht e (.inr r)⟩
  · rintro ⟨ho, hn⟩ s t hs ht e q
    cases q with
    | inl q => exact ho s t hs ht e q
    | inr r => exact hn s t hs ht e r

/-- Generic origin constraint: a closed region cannot be escaped by its law. -/
theorem closed_region_preserved {S : Type u} {A : Type v}
    (P : Process S A) (region : S → Prop)
    (closed : ∀ s a t, region s → P.step s a t → region t)
    {s t : S} {word : List A} (history : Trace P s word t)
    (initial : region s) : region t := by
  induction history with
  | nil => exact initial
  | cons step _ ih => exact ih (closed _ _ _ initial step)

structure Assembly where
  links : Nat
  loose : Nat
  work : Nat
  coupled : Bool
  deriving DecidableEq, Repr

/-- Coupling binds two pre-existing parts; each chain link binds one further
part. All stocks and relations are coordinates of the same assembly history. -/
def material (s : Assembly) : Nat :=
  s.links + s.loose + if s.coupled then 2 else 0

inductive Event where
  | couple
  | extend
  | wait
  deriving DecidableEq, Repr

def assembly : Process Assembly Event where
  step s event t := match event with
    | .couple => s.coupled = false ∧ 2 ≤ s.loose ∧ 0 < s.work ∧
        t = ⟨s.links, s.loose - 2, s.work - 1, true⟩
    | .extend => s.coupled = true ∧ 0 < s.loose ∧ 0 < s.work ∧
        t = ⟨s.links + 1, s.loose - 1, s.work - 1, true⟩
    | .wait => 0 < s.work ∧ t = ⟨s.links, s.loose, s.work - 1, s.coupled⟩

/-- A signal traverses physically present adjacent links. This idealized
assay omits duration, attenuation and expenditure of transmitting the signal. -/
inductive Reaches (s : Assembly) : Nat → Prop where
  | root : Reaches s 0
  | next {n : Nat} : Reaches s n → n < s.links → Reaches s (n + 1)

theorem reach_bound {s : Assembly} {n : Nat} (path : Reaches s n) : n ≤ s.links := by
  cases path with
  | root => omega
  | next _ h => omega

theorem reach_construct {s : Assembly} {n : Nat} (h : n ≤ s.links) : Reaches s n := by
  induction n with
  | zero => exact .root
  | succ n ih => exact .next (ih (by omega)) (by omega)

theorem reaches_iff (s : Assembly) (n : Nat) : Reaches s n ↔ n ≤ s.links :=
  ⟨reach_bound, reach_construct⟩

theorem extension_adds_actual_route {s t : Assembly}
    (h : assembly.step s .extend t) :
    Reaches t (s.links + 1) ∧ ¬ Reaches s (s.links + 1) := by
  obtain ⟨_, _, _, rfl⟩ := h
  exact ⟨reach_construct (by simp), fun h => by have := reach_bound h; omega⟩

theorem step_material_conserved {s t : Assembly} {e : Event}
    (h : assembly.step s e t) : material t = material s := by
  cases e with
  | couple =>
    obtain ⟨hc, hl, _, rfl⟩ := h
    simp [material, hc]
    omega
  | extend =>
    obtain ⟨hc, hl, _, rfl⟩ := h
    simp [material, hc]
    omega
  | wait =>
    obtain ⟨_, rfl⟩ := h
    rfl

theorem step_work_account {s t : Assembly} {e : Event}
    (h : assembly.step s e t) : t.work + 1 = s.work := by
  cases e <;> simp only [assembly] at h
  · obtain ⟨_, _, hw, rfl⟩ := h; simp; omega
  · obtain ⟨_, _, hw, rfl⟩ := h; simp; omega
  · obtain ⟨hw, rfl⟩ := h; simp; omega

theorem trace_material_conserved {s t : Assembly} {word : List Event}
    (h : Trace assembly s word t) : material t = material s := by
  induction h with
  | nil => rfl
  | cons step _ ih => exact ih.trans (step_material_conserved step)

theorem trace_work_account {s t : Assembly} {word : List Event}
    (h : Trace assembly s word t) : t.work + word.length = s.work := by
  induction h with
  | nil => simp
  | cons step _ ih =>
    have := step_work_account step
    simp only [List.length_cons]
    omega

theorem finite_work_bounds_history {s t : Assembly} {word : List Event}
    (h : Trace assembly s word t) : word.length ≤ s.work := by
  have := trace_work_account h
  omega

theorem no_infinite_closed_execution (states : Nat → Assembly) (events : Nat → Event)
    (actual : ∀ n, assembly.step (states n) (events n) (states (n + 1))) : False := by
  have balance : ∀ n, (states n).work + n = (states 0).work := by
    intro n
    induction n with
    | zero => simp
    | succ n ih => have := step_work_account (actual n); omega
  have := balance ((states 0).work + 1)
  omega

/-- This restriction holds the constructor-coupling relation fixed as absent.
It is not the full physical law. -/
def frozen : Process Assembly Event where
  step s e t := assembly.step s e t ∧ e ≠ .couple

theorem frozen_step {s t : Assembly} {e : Event}
    (h : frozen.step s e t) (absent : s.coupled = false) :
    t.coupled = false ∧ t.links = s.links := by
  obtain ⟨step, noCouple⟩ := h
  cases e with
  | couple => exact False.elim (noCouple rfl)
  | extend => have := step.1; simp [absent] at this
  | wait => obtain ⟨_, rfl⟩ := step; exact ⟨absent, rfl⟩

theorem frozen_trace {s t : Assembly} {word : List Event}
    (h : Trace frozen s word t) (absent : s.coupled = false) :
    t.coupled = false ∧ t.links = s.links := by
  induction h with
  | nil => exact ⟨absent, rfl⟩
  | cons step _ ih =>
    obtain ⟨hc, hl⟩ := frozen_step step absent
    obtain ⟨tc, tl⟩ := ih hc
    exact ⟨tc, tl.trans hl⟩

theorem frozen_cannot_make_route {s t : Assembly} {word : List Event} {n : Nat}
    (h : Trace frozen s word t) (absent : s.coupled = false)
    (outside : s.links < n) : ¬ Reaches t n := by
  have equal := (frozen_trace h absent).2
  intro path
  have bound := reach_bound path
  omega

/-- One fixed local schema, with a constructor already coupled, builds any
funded finite extension. It does not import a menu of complete endpoint tools. -/
theorem construct_chain (n base loose work : Nat) :
    Trace assembly ⟨base, loose + n, work + n, true⟩
      (List.replicate n .extend) ⟨base + n, loose, work, true⟩ := by
  induction n generalizing base with
  | zero => simp; exact .nil _
  | succ n ih =>
    have first : assembly.step
        ⟨base, loose + (n + 1), work + (n + 1), true⟩ .extend
        ⟨base + 1, loose + n, work + n, true⟩ := by
      simp [assembly]
      omega
    have rest := ih (base + 1)
    have same : base + 1 + n = base + (n + 1) := by omega
    rw [same] at rest
    exact .cons first rest

theorem form_constructor_then_chain (n : Nat) :
    Trace assembly ⟨0, n + 2, n + 1, false⟩
      (.couple :: List.replicate n .extend) ⟨n, 0, 0, true⟩ := by
  have first : assembly.step ⟨0, n + 2, n + 1, false⟩ .couple
      ⟨0, n, n, true⟩ := by simp [assembly]
  have rest := construct_chain n 0 0 0
  simp only [Nat.zero_add] at rest
  exact .cons first rest

def menuBound : List Nat → Nat
  | [] => 0
  | n :: ns => max n (menuBound ns)

theorem member_below_bound {n : Nat} {menu : List Nat} (h : n ∈ menu) :
    n ≤ menuBound menu := by
  induction menu with
  | nil => simp at h
  | cons a rest ih =>
    simp only [List.mem_cons] at h
    cases h with
    | inl h => subst n; exact Nat.le_max_left _ _
    | inr h => exact Nat.le_trans (ih h) (Nat.le_max_right _ _)

/-- Every finite advertised endpoint menu can be exceeded, given separately
specified finite resources. Quantifier order does not promise one inexhaustible run. -/
theorem beyond_every_finite_menu (menu : List Nat) :
    ∃ n, n ∉ menu ∧ Reaches (⟨n, 0, 0, true⟩ : Assembly) n ∧
      Trace assembly ⟨0, n + 2, n + 1, false⟩
        (.couple :: List.replicate n .extend) ⟨n, 0, 0, true⟩ := by
  refine ⟨menuBound menu + 1, ?_, reach_construct (by simp),
    form_constructor_then_chain _⟩
  intro member
  have := member_below_bound member
  omega

/-- Same parts and work, different binding relations and construction capacity. -/
def initial : Assembly := ⟨0, 3, 3, false⟩
def bound : Assembly := ⟨0, 1, 2, true⟩
def unbound : Assembly := ⟨0, 3, 2, false⟩
def oldDescription (s : Assembly) : Nat × Nat × Nat := (material s, s.work, s.links)
def newDescription (s : Assembly) : (Nat × Nat × Nat) × Bool :=
  (oldDescription s, s.coupled)
def canExtend (s : Assembly) : Bool := s.coupled && decide (0 < s.loose ∧ 0 < s.work)

theorem response_matches_operation (s : Assembly) :
    canExtend s = true ↔ Enabled assembly s .extend := by
  simp only [canExtend, Bool.and_eq_true, decide_eq_true_eq]
  constructor
  · rintro ⟨hc, hl, hw⟩
    exact ⟨_, hc, hl, hw, rfl⟩
  · rintro ⟨t, hc, hl, hw, _⟩
    exact ⟨hc, hl, hw⟩

theorem matched_histories :
    Trace assembly initial [.couple] bound ∧ Trace assembly initial [.wait] unbound := by
  constructor <;> apply trace_singleton_iff.mpr <;>
    simp [assembly, initial, bound, unbound]

theorem old_description_collides : oldDescription bound = oldDescription unbound := by decide
theorem construction_response_differs : canExtend bound ≠ canExtend unbound := by decide

theorem old_description_inadequate :
    ¬ AdequateOn (fun _ : Assembly => True) oldDescription
      (fun s (_ : Unit) => canExtend s) :=
  collision_defeats_adequacy trivial trivial old_description_collides
    (q := ()) construction_response_differs

theorem new_description_preserves_old (s : Assembly) :
    (newDescription s).1 = oldDescription s := rfl

theorem new_description_adequate :
    AdequateOn (fun _ : Assembly => True) newDescription
      (fun s (_ : Unit) => canExtend s) := by
  intro s t _ _ h _
  have hc : s.coupled = t.coupled := congrArg Prod.snd h
  have ho : oldDescription s = oldDescription t := congrArg Prod.fst h
  have hm : material s = material t := congrArg Prod.fst ho
  have hw : s.work = t.work := congrArg (fun x => x.2.1) ho
  have hl : s.links = t.links := congrArg (fun x => x.2.2) ho
  have hp : s.loose = t.loose := by
    simp only [material, hc, hl] at hm
    omega
  simp only [canExtend, hc, hw, hp]

/-- Relabeling adds no missing distinction. -/
theorem relabeling_cannot_repair {D : Type u} (f : (Nat × Nat × Nat) → D) :
    ¬ AdequateOn (fun _ : Assembly => True) (fun s => f (oldDescription s))
      (fun s (_ : Unit) => canExtend s) :=
  collision_defeats_adequacy trivial trivial (congrArg f old_description_collides)
    (q := ()) construction_response_differs

/-- Faithful finite evidence suffices for this one query, not for every future. -/
def Faithful (s : Assembly) (record : Bool) : Prop := record = canExtend s

theorem acquired_record_repairs_query {s t : Assembly} {rs rt : Bool}
    (hs : Faithful s rs) (ht : Faithful t rt) (same : rs = rt) :
    canExtend s = canExtend t := hs.symm.trans (same.trans ht)

theorem stale_record_counterexample :
    Faithful unbound false ∧ ¬ Faithful bound false := by
  simp [Faithful, canExtend, bound, unbound]

/-- Gaining a transport route can exhaust further construction capacity. -/
theorem novelty_with_loss :
    assembly.step bound .extend ⟨1, 0, 1, true⟩ ∧
    Reaches (⟨1, 0, 1, true⟩ : Assembly) 1 ∧
    canExtend bound = true ∧ canExtend ⟨1, 0, 1, true⟩ = false := by
  refine ⟨?_, reach_construct (by simp), ?_, ?_⟩ <;>
    simp [assembly, bound, canExtend]

/-- The finite semantic repair adds exactly the queried distinction. Any
other repair that retains the old description and answers this question must
also determine this pair, on the declared domain. -/
theorem query_pair_is_coarsest_sufficient_refinement
    {S : Type u} {D E : Type v} {Y : Type w}
    {domain : S → Prop} {old : S → D} {response : S → Y} {other : S → E}
    (retains : ∀ s t, domain s → domain t → other s = other t → old s = old t)
    (answers : ∀ s t, domain s → domain t → other s = other t → response s = response t)
    {s t : S} (hs : domain s) (ht : domain t) (same : other s = other t) :
    (old s, response s) = (old t, response t) := by
  exact Prod.ext (retains s t hs ht same) (answers s t hs ht same)

/-- A historical response is preserved as a dated fact; current validity
requires a response-stability premise, which formation can defeat. -/
theorem record_transports_only_with_stability {s t : Assembly} {r : Bool}
    (record : Faithful s r) (stable : canExtend s = canExtend t) : Faithful t r :=
  record.trans stable

end Generative.NewPossibilities
