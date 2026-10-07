import InquiryRelevance

/-!
Scope of a further inquiry after the original opportunity has ended.

`InquiryRelevance` showed that, in the declared family, only a weak test at
the setting actually used answers whether its weak response agreed with the
acquired full effect. That is epistemic sufficiency. This module asks when
the answer has a role in what remains: which surviving continuations, borne
by the inquiring organization or by another center, can be carried out
adequately with the answer and not without it, given that the inquiry itself
draws on support those continuations also require.

A continuation records whose continuation it is, the relay setting it will
rely on, the effect it relies on there, which action is adequate when the weak
indication does or does not agree with that effect, and the support it needs.
Adequacy, the relied-on effect (acquired only at the used setting, supplied
elsewhere) and the requirement are supplied local inputs, not derived goods;
each answer has exactly one adequate action. The test is faithful, every weak
table remains possible, and abstention is modelled as drawing nothing and
having no further consequence: a simplification, not a claim that abstaining
is neutral. `other` marks a
differentiated center inside the same unfolding, not an external party. The
shared support quantity is an analyst's summary of the conditions all listed
continuations draw on. Nothing here ranks continuations, scores outcomes, or
derives that any continuation ought to be sustained. The results characterize
which alternatives exist; choosing among them is outside this module.
-/
namespace InquiryWarrant
open RemainingDependency InquiryRelevance

structure Continuation where
  /-- `false`: borne by the inquiring organization; `true`: by another center. -/
  other : Bool
  /-- The relay setting this continuation will rely on. -/
  setting : Bool
  /-- The full effect it relies on at that setting. -/
  expected : Bool
  /-- Adequate action when the weak indication agrees (`true`) or not (`false`). -/
  adequate : Bool → Bool
  /-- Support this continuation needs in order to be carried out. -/
  requirement : Nat

/-- Whether the weak indication at the continuation's setting agrees with the
effect it relies on. -/
def agrees (c : Continuation) (weak : Pair Bool) : Bool :=
  weak.get c.setting == c.expected

/-- Local helper: Boolean `==` is `true` exactly at equality. -/
theorem beq_true_iff (a b : Bool) : (a == b) = true ↔ a = b := by
  cases a <;> cases b <;> decide

/-- Local helper: a constant table reads its value at every setting. -/
theorem get_const (e s : Bool) : (⟨e, e⟩ : Pair Bool).get s = e := by
  cases s <;> rfl

/-- Local helper: a flipped bit never equals the original. -/
theorem not_beq_self (e : Bool) : ((!e) == e) = false := by
  cases e <;> rfl

/-- Local helper: a flipped bit is a different bit. -/
theorem not_ne_self (e : Bool) : (!e) ≠ e := by
  cases e <;> decide

/-- Local helper (local counterpart of `off_target_witness`): away from the
relied-on setting, some table agrees with the constant one at the query and
flips the relied-on bit. -/
theorem off_target_table (s e q : Bool) (hq : q ≠ s) :
    ∃ alt : Pair Bool, alt.get q = e ∧ alt.get s = !e := by
  cases s <;> cases q
  · exact absurd rfl hq
  · exact ⟨⟨!e, e⟩, rfl, rfl⟩
  · exact ⟨⟨e, !e⟩, rfl, rfl⟩
  · exact absurd rfl hq

/-- Local helper (local counterpart of `query_sufficient_iff_used_setting`). -/
theorem sufficient_iff_used (r f q : Bool) : QuerySufficient r f q ↔ q = r := by
  constructor
  · intro sufficient
    match Bool.decEq q r with
    | isTrue hq => exact hq
    | isFalse hq =>
      obtain ⟨alt, hq', hr⟩ := off_target_table r f q hq
      have same : (⟨f, f⟩ : Pair Bool).get q = alt.get q := (get_const f q).trans hq'.symm
      have agree : LocalAgreement ⟨f, f⟩ r f := get_const f r
      have bad : alt.get r = f := (sufficient _ _ same).mp agree
      exact absurd (hr.symm.trans bad) (not_ne_self f)
  · intro hq
    subst hq
    intro weak alternative h
    exact ⟨fun x => h.symm.trans x, fun x => h.trans x⟩

theorem agrees_iff_local (c : Continuation) (weak : Pair Bool) :
    agrees c weak = true ↔ LocalAgreement weak c.setting c.expected :=
  beq_true_iff _ _

/-- Local helper: the constant table at the relied-on effect agrees. -/
theorem agrees_const (c : Continuation) : agrees c ⟨c.expected, c.expected⟩ = true := by
  show (Pair.get ⟨c.expected, c.expected⟩ c.setting == c.expected) = true
  rw [get_const]
  exact (beq_true_iff _ _).mpr rfl

/-- Local helper: a table whose relied-on bit is flipped disagrees. -/
theorem agrees_flipped (c : Continuation) (alt : Pair Bool)
    (h : alt.get c.setting = !c.expected) : agrees c alt = false := by
  show (alt.get c.setting == c.expected) = false
  rw [h]
  exact not_beq_self _

/-- After a faithful weak test at `q`, some response policy acts adequately
whatever the still-possible weak table is. -/
def InquiryAdequate (q : Bool) (c : Continuation) : Prop :=
  ∃ policy : Bool → Bool, ∀ weak : Pair Bool,
    policy (weak.get q) = c.adequate (agrees c weak)

/-- Without a further test, one action is adequate for every possible table:
a common adequate response. -/
def AbstentionAdequate (c : Continuation) : Prop :=
  ∃ action : Bool, ∀ weak : Pair Bool, action = c.adequate (agrees c weak)

/-- The answer bears on the continuation: its adequate action differs. -/
def AnswerBearing (c : Continuation) : Prop := c.adequate true ≠ c.adequate false

instance (c : Continuation) : Decidable (AnswerBearing c) :=
  inferInstanceAs (Decidable (c.adequate true ≠ c.adequate false))

theorem abstention_adequate_iff (c : Continuation) :
    AbstentionAdequate c ↔ ¬ AnswerBearing c := by
  constructor
  · rintro ⟨action, h⟩ hb
    have h1 := h ⟨c.expected, c.expected⟩
    have h2 := h ⟨!c.expected, !c.expected⟩
    have e1 : agrees c ⟨c.expected, c.expected⟩ = true := agrees_const c
    have e2 : agrees c ⟨!c.expected, !c.expected⟩ = false :=
      agrees_flipped c _ (get_const _ _)
    rw [e1] at h1
    rw [e2] at h2
    exact hb (h1.symm.trans h2)
  · intro hb
    have same : c.adequate true = c.adequate false :=
      Decidable.byContradiction hb
    refine ⟨c.adequate true, fun weak => ?_⟩
    cases agrees c weak
    · exact same
    · rfl

/-- The decision role of a weak test: it secures an adequate response exactly
when it is at the relied-on setting or the answer does not matter. The `→`
direction uses the off-target witness of `InquiryRelevance`. -/
theorem inquiry_adequate_iff (q : Bool) (c : Continuation) :
    InquiryAdequate q c ↔ q = c.setting ∨ ¬ AnswerBearing c := by
  constructor
  · rintro ⟨policy, h⟩
    match Bool.decEq q c.setting with
    | isTrue hq => exact Or.inl hq
    | isFalse hq =>
      refine Or.inr fun hb => ?_
      obtain ⟨alt, hq', hs⟩ := off_target_table c.setting c.expected q hq
      have h1 := h ⟨c.expected, c.expected⟩
      have h2 := h alt
      rw [agrees_const, get_const] at h1
      rw [agrees_flipped c alt hs, hq'] at h2
      exact hb (h1.symm.trans h2)
  · rintro (hq | hb)
    · refine ⟨fun b => c.adequate (b == c.expected), fun weak => ?_⟩
      rw [hq]
      rfl
    · obtain ⟨action, h⟩ := (abstention_adequate_iff c).mpr hb
      exact ⟨fun _ => action, h⟩

/-- For a continuation whose action depends on the answer, the decision role
of a test coincides with the epistemic sufficiency already proved. -/
theorem bearing_adequate_iff_sufficient (q : Bool) (c : Continuation)
    (hb : AnswerBearing c) :
    InquiryAdequate q c ↔ QuerySufficient c.setting c.expected q := by
  constructor
  · intro h
    rcases (inquiry_adequate_iff q c).mp h with h | h
    · exact (sufficient_iff_used _ _ _).mpr h
    · exact False.elim (h hb)
  · intro h
    exact (inquiry_adequate_iff q c).mpr (Or.inl ((sufficient_iff_used _ _ _).mp h))

/-- The inquiry's own draw on support is carried forward with its answer. -/
def InquirySecures (support draw : Nat) (q : Bool) (c : Continuation) : Prop :=
  c.requirement + draw ≤ support ∧ InquiryAdequate q c

def AbstentionSecures (support : Nat) (c : Continuation) : Prop :=
  c.requirement ≤ support ∧ AbstentionAdequate c

/-- The test secures this continuation and abstention does not. -/
def InquiryNeeded (support draw : Nat) (q : Bool) (c : Continuation) : Prop :=
  InquirySecures support draw q c ∧ ¬ AbstentionSecures support c

theorem inquiry_needed_iff (support draw : Nat) (q : Bool) (c : Continuation) :
    InquiryNeeded support draw q c ↔
      q = c.setting ∧ AnswerBearing c ∧ c.requirement + draw ≤ support := by
  constructor
  · rintro ⟨⟨fits, hq⟩, notAbstain⟩
    have hb : AnswerBearing c :=
      Decidable.byContradiction fun hb =>
        notAbstain ⟨Nat.le_trans (Nat.le_add_right _ _) fits,
          (abstention_adequate_iff c).mpr hb⟩
    rcases (inquiry_adequate_iff q c).mp hq with hq | hq
    · exact ⟨hq, hb, fits⟩
    · exact False.elim (hq hb)
  · rintro ⟨hq, hb, fits⟩
    exact ⟨⟨fits, (inquiry_adequate_iff q c).mpr (Or.inl hq)⟩,
      fun ⟨_, na⟩ => (abstention_adequate_iff c).mp na hb⟩

/-- Some surviving continuation needs the test. -/
def NeededFor (support draw : Nat) (q : Bool) (cs : List Continuation) : Prop :=
  ∃ c ∈ cs, InquiryNeeded support draw q c

theorem needed_for_iff (support draw : Nat) (q : Bool) (cs : List Continuation) :
    NeededFor support draw q cs ↔
      ∃ c ∈ cs, c.setting = q ∧ AnswerBearing c ∧ c.requirement + draw ≤ support := by
  unfold NeededFor
  constructor
  · rintro ⟨c, hc, hn⟩
    obtain ⟨hq, hb, fits⟩ := (inquiry_needed_iff _ _ _ _).mp hn
    exact ⟨c, hc, hq.symm, hb, fits⟩
  · rintro ⟨c, hc, hq, hb, fits⟩
    exact ⟨c, hc, (inquiry_needed_iff _ _ _ _).mpr ⟨hq.symm, hb, fits⟩⟩

/-- When no surviving continuation relies on the tested setting (as after the
original opportunity has ended, if nothing else reuses it), every continuation the test secures is also
secured, with no more support drawn, without it. The test that uniquely answers
the past application's question then has no role in what remains: the
statement concerns a single test at `q`. -/
theorem dominated_without_reliance (support draw : Nat) (q : Bool)
    (cs : List Continuation) (none : ∀ c ∈ cs, c.setting ≠ q) :
    (∀ c ∈ cs, InquirySecures support draw q c → AbstentionSecures support c) ∧
      ¬ NeededFor support draw q cs := by
  refine ⟨fun c hc ⟨fits, ha⟩ => ?_, fun hn => ?_⟩
  · rcases (inquiry_adequate_iff q c).mp ha with hq | hb
    · exact False.elim (none c hc hq.symm)
    · exact ⟨Nat.le_trans (Nat.le_add_right _ _) fits, (abstention_adequate_iff c).mpr hb⟩
  · obtain ⟨c, hc, hq, _, _⟩ := (needed_for_iff _ _ _ _).mp hn
    exact none c hc hq

/-- The continuations borne by the inquiring organization itself. -/
def selfOnly (cs : List Continuation) : List Continuation :=
  cs.filter fun c => !c.other

/-- Local helper: membership in a filtered list implies membership. -/
theorem mem_of_mem_filter' {α : Type} (p : α → Bool) (x : α) :
    ∀ l : List α, x ∈ l.filter p → x ∈ l
  | [], h => h
  | a :: l, h => by
    cases hp : p a
    · rw [List.filter_cons_of_neg (by rw [hp]; decide)] at h
      exact List.mem_cons_of_mem _ (mem_of_mem_filter' p x l h)
    · rw [List.filter_cons_of_pos hp] at h
      cases h with
      | head => exact List.mem_cons_self
      | tail _ h => exact List.mem_cons_of_mem _ (mem_of_mem_filter' p x l h)

/-- Local helper: filtering distributes over append. -/
theorem filter_append' {α : Type} (p : α → Bool) :
    ∀ l m : List α, (l ++ m).filter p = l.filter p ++ m.filter p
  | [], _ => rfl
  | a :: l, m => by
    cases hp : p a
    · rw [List.cons_append, List.filter_cons_of_neg (by rw [hp]; decide),
        List.filter_cons_of_neg (by rw [hp]; decide)]
      exact filter_append' p l m
    · rw [List.cons_append, List.filter_cons_of_pos hp, List.filter_cons_of_pos hp,
        List.cons_append, filter_append' p l m]

/-- Local helper: appending the empty list. -/
theorem append_nil' {α : Type} : ∀ l : List α, l ++ [] = l
  | [] => rfl
  | a :: l => congrArg (a :: ·) (append_nil' l)

theorem self_needed_implies_needed (support draw : Nat) (q : Bool)
    (cs : List Continuation) :
    NeededFor support draw q (selfOnly cs) → NeededFor support draw q cs := by
  rintro ⟨c, hc, hn⟩
  exact ⟨c, mem_of_mem_filter' _ _ _ hc, hn⟩

/-- A selection rule that consults only self-borne continuations gives the
same verdict however many continuations of other centers are added. This holds
by construction of such a rule; it is recorded because it is the inquiry-scope
analogue (not a derivation) of the unreached-extension result in the
valuation-development study: other centers' consequences must reach a rule
through something beyond its self-scoped input. -/
theorem self_scoped_rule_ignores_others (rule : List Continuation → Bool)
    (cs others : List Continuation) (h : ∀ c ∈ others, c.other = true) :
    rule (selfOnly (cs ++ others)) = rule (selfOnly cs) := by
  have : selfOnly others = [] := by
    induction others with
    | nil => rfl
    | cons c rest ih =>
      have hc : c.other = true := h c List.mem_cons_self
      unfold selfOnly
      rw [List.filter_cons_of_neg (by rw [hc]; decide)]
      exact ih fun d hd => h d (List.mem_cons_of_mem _ hd)
  unfold selfOnly at this ⊢
  rw [filter_append', this, append_nil']

/-! ### Witnesses at the actual failed operation (setting 1, full effect 0) -/

/-- The inquiring organization would rely again on the used setting. -/
def selfReuse : Continuation :=
  { other := false, setting := true, expected := false, adequate := id, requirement := 1 }

/-- Another center would rely on the used setting (for example, when deciding
whether a weak report there can be trusted about what reaches it). -/
def othersReuse : Continuation :=
  { other := true, setting := true, expected := false, adequate := id, requirement := 1 }

/-- The inquiring organization would rely only on the other setting: its own
continuation does not reuse the relation the past application challenged. -/
def selfElsewhere : Continuation :=
  { other := false, setting := false, expected := false, adequate := id, requirement := 1 }

/-- Another center's continuation whose adequate action does not depend on
the answer but which needs more of the shared support. -/
def othersSettled : Continuation :=
  { other := true, setting := false, expected := false, adequate := fun _ => true,
    requirement := 2 }

/-- The organization's own surviving continuation relies on the other
setting, so a self-scoped assessment finds no role for the test at the used
setting, while another center's surviving reliance gives it one. -/
theorem needed_only_through_other :
    ¬ NeededFor 3 1 true (selfOnly [selfElsewhere, othersReuse]) ∧
      NeededFor 3 1 true [selfElsewhere, othersReuse] := by
  refine ⟨?_, ?_⟩
  · rintro ⟨c, hc, hn⟩
    have e : selfOnly [selfElsewhere, othersReuse] = [selfElsewhere] := rfl
    rw [e] at hc
    cases hc with
    | head => exact absurd ((inquiry_needed_iff _ _ _ _).mp hn).1 (by decide)
    | tail _ h => cases h
  · refine (needed_for_iff _ _ _ _).mpr
      ⟨othersReuse, List.Mem.tail _ (List.Mem.head _), rfl, ?_, by decide⟩
    show (true : Bool) ≠ false
    decide

/-- Answering can remove the means of acting on the answer: with support 1 the
test answers the question but leaves too little to carry the continuation,
and abstention keeps the support but cannot act adequately. -/
theorem answering_can_remove_the_means :
    InquiryAdequate true selfReuse ∧ ¬ InquirySecures 1 1 true selfReuse ∧
      ¬ AbstentionSecures 1 selfReuse := by
  refine ⟨(inquiry_adequate_iff _ _).mpr (Or.inl rfl), ?_, ?_⟩
  · rintro ⟨fits, _⟩
    exact absurd fits (by decide)
  · rintro ⟨_, ha⟩
    exact (abstention_adequate_iff _).mp ha (by decide)

/-- A joint course: whether to test, and which continuations to carry out
together from one support quantity, each adequately. -/
def JointlySecures (support draw : Nat) (inquire q : Bool)
    (carried : List Continuation) : Prop :=
  (carried.map Continuation.requirement).sum + (if inquire then draw else 0) ≤ support ∧
    ∀ c ∈ carried, if inquire then InquiryAdequate q c else AbstentionAdequate c

/-- Differentiated continuations can compete for the same conditions. Testing
secures the organization's own reuse, abstaining secures the other center's
continuation, and no course secures both. The model enumerates these
alternatives; it does not say which should be taken. The competition is
additive on one support summary, and the courses range over one uniform
test-or-abstain choice. -/
theorem competing_continuations :
    JointlySecures 3 1 true true [selfReuse] ∧
      JointlySecures 3 1 false true [othersSettled] ∧
      ∀ inquire q : Bool, ¬ JointlySecures 3 1 inquire q [selfReuse, othersSettled] := by
  refine ⟨⟨by decide, ?_⟩, ⟨by decide, ?_⟩, ?_⟩
  · intro c hc
    cases hc with
    | head => exact (inquiry_adequate_iff _ _).mpr (Or.inl rfl)
    | tail _ h => cases h
  · intro c hc
    cases hc with
    | head => exact (abstention_adequate_iff _).mpr (by decide)
    | tail _ h => cases h
  · intro inquire q ⟨fits, each⟩
    cases inquire
    · have ha : AbstentionAdequate selfReuse := each selfReuse (List.Mem.head _)
      exact (abstention_adequate_iff _).mp ha (by decide)
    · exact absurd fits (by decide)

end InquiryWarrant

#print axioms InquiryWarrant.Continuation
#print axioms InquiryWarrant.agrees
#print axioms InquiryWarrant.beq_true_iff
#print axioms InquiryWarrant.get_const
#print axioms InquiryWarrant.not_beq_self
#print axioms InquiryWarrant.not_ne_self
#print axioms InquiryWarrant.off_target_table
#print axioms InquiryWarrant.sufficient_iff_used
#print axioms InquiryWarrant.agrees_iff_local
#print axioms InquiryWarrant.agrees_const
#print axioms InquiryWarrant.agrees_flipped
#print axioms InquiryWarrant.InquiryAdequate
#print axioms InquiryWarrant.AbstentionAdequate
#print axioms InquiryWarrant.AnswerBearing
#print axioms InquiryWarrant.abstention_adequate_iff
#print axioms InquiryWarrant.inquiry_adequate_iff
#print axioms InquiryWarrant.bearing_adequate_iff_sufficient
#print axioms InquiryWarrant.InquirySecures
#print axioms InquiryWarrant.AbstentionSecures
#print axioms InquiryWarrant.InquiryNeeded
#print axioms InquiryWarrant.inquiry_needed_iff
#print axioms InquiryWarrant.NeededFor
#print axioms InquiryWarrant.needed_for_iff
#print axioms InquiryWarrant.dominated_without_reliance
#print axioms InquiryWarrant.selfOnly
#print axioms InquiryWarrant.mem_of_mem_filter'
#print axioms InquiryWarrant.filter_append'
#print axioms InquiryWarrant.append_nil'
#print axioms InquiryWarrant.self_needed_implies_needed
#print axioms InquiryWarrant.self_scoped_rule_ignores_others
#print axioms InquiryWarrant.selfReuse
#print axioms InquiryWarrant.othersReuse
#print axioms InquiryWarrant.selfElsewhere
#print axioms InquiryWarrant.othersSettled
#print axioms InquiryWarrant.needed_only_through_other
#print axioms InquiryWarrant.answering_can_remove_the_means
#print axioms InquiryWarrant.JointlySecures
#print axioms InquiryWarrant.competing_continuations
