/-!
Which continuations a choice must count, and what the structure of a choice
can and cannot settle.

`InquiryWarrant` took the list of surviving continuations as supplied. Here a
situation lists the available courses, the continuations under consideration
and which continuations each course secures. A continuation is *reached* by
the choice when some two available courses differ on securing it; that
relation is derived from the supplied courses and secures relation rather than
listed separately. Restriction only filters the supplied continuation list; it
never adds a continuation the list left out. A course
*needlessly forecloses* when another available course secures everything it
secures and more.

Results:
* counting exactly the reached continuations never changes which courses
  needlessly foreclose (`unreached_never_matters`);
* omitting a reached continuation distorts assessment in both directions:
  in a constructed witness it endorses a needless foreclosure
  (`omitted_scope_admits_needless_foreclosure`), in another it condemns a
  course that forecloses nothing needlessly (`omitted_scope_can_condemn`);
* every finite nonempty situation has a course that forecloses nothing
  needlessly (`nonforeclosing_exists`);
* when two centers' continuations compete symmetrically, both courses
  foreclose nothing needlessly, and no deterministic rule that must output a
  course and sees only this structure can choose; this is the classic
  tie-symmetry argument and says nothing against randomized or procedural
  tie-breaks, history or further information
  (`symmetric_competition_has_no_structural_choice`);
* after a claim is fulfilled, a course kept for it can become a needless
  foreclosure (`fulfillment_turns_retained_course_foreclosing`); this is one
  stipulated example without time or uncertainty about fulfillment.

Courses, continuations and the Boolean secures relation are supplied local
inputs. Improvement is all-or-nothing inclusion: it has no magnitude,
likelihood or burden. Nothing here weighs
continuations, decides whose claim prevails, or proves that every reached
continuation ought to be sustained.
-/
namespace ContinuationScope

structure Situation (A K : Type) where
  courses : List A
  continuations : List K
  secures : A → K → Bool

variable {A K : Type}

/-- `b` secures every considered continuation `a` secures, and one more. -/
def Improves (s : Situation A K) (b a : A) : Prop :=
  (∀ k ∈ s.continuations, s.secures a k = true → s.secures b k = true) ∧
    ∃ k ∈ s.continuations, s.secures b k = true ∧ s.secures a k = false

/-- An available course that no available course improves on. -/
def Nonforeclosing (s : Situation A K) (a : A) : Prop :=
  a ∈ s.courses ∧ ¬ ∃ b ∈ s.courses, Improves s b a

/-- The choice reaches `k` when two available courses differ on securing it. -/
def Situation.reached (s : Situation A K) (k : K) : Bool :=
  s.courses.any fun a => s.courses.any fun b => s.secures a k != s.secures b k

/-- The same situation with only the continuations in `scope` considered. -/
def Situation.restrict (s : Situation A K) (scope : K → Bool) : Situation A K :=
  { s with continuations := s.continuations.filter scope }

theorem unreached_agree (s : Situation A K) (k : K) (h : s.reached k = false)
    (a b : A) (ha : a ∈ s.courses) (hb : b ∈ s.courses) :
    s.secures a k = s.secures b k := by
  have h' := h
  simp only [Situation.reached, List.any_eq_false] at h'
  have inner := h' a ha
  rw [Bool.not_eq_true, List.any_eq_false] at inner
  have := inner b hb
  cases hx : s.secures a k <;> cases hy : s.secures b k <;> simp_all

/-- Restricting attention to the reached continuations never changes whether
one available course improves on another. -/
theorem unreached_never_matters (s : Situation A K) (a b : A)
    (ha : a ∈ s.courses) (hb : b ∈ s.courses) :
    Improves s b a ↔ Improves (s.restrict s.reached) b a := by
  unfold Improves Situation.restrict
  simp only [List.mem_filter]
  constructor
  · rintro ⟨incl, k, hk, yes, no⟩
    refine ⟨fun k' hk' => incl k' hk'.1, k, ⟨hk, ?_⟩, yes, no⟩
    cases hr : s.reached k
    · have := unreached_agree s k hr a b ha hb
      rw [no, yes] at this
      cases this
    · rfl
  · rintro ⟨incl, k, hk, yes, no⟩
    refine ⟨fun k' hk' sa => ?_, k, hk.1, yes, no⟩
    cases hr : s.reached k'
    · rw [← unreached_agree s k' hr a b ha hb]
      exact sa
    · exact incl k' ⟨hk', hr⟩ sa

theorem nonforeclosing_restrict_iff (s : Situation A K) (a : A) :
    Nonforeclosing s a ↔ Nonforeclosing (s.restrict s.reached) a := by
  unfold Nonforeclosing
  constructor
  · rintro ⟨ha, none⟩
    refine ⟨ha, fun ⟨b, hb, imp⟩ => none ⟨b, hb, ?_⟩⟩
    exact (unreached_never_matters s a b ha hb).mpr imp
  · rintro ⟨ha, none⟩
    refine ⟨ha, fun ⟨b, hb, imp⟩ => none ⟨b, hb, ?_⟩⟩
    exact (unreached_never_matters s a b ha hb).mp imp

/-- Whatever continuation a scope omits, there is a constructed situation
where it is reached, a course needlessly forecloses it, and the scoped
assessment finds nothing wrong with that course. -/
theorem omitted_scope_admits_needless_foreclosure (scope : K → Bool) (k : K)
    (omitted : scope k = false) :
    let s : Situation Bool K :=
      { courses := [false, true], continuations := [k], secures := fun a _ => a }
    s.reached k = true ∧ ¬ Nonforeclosing s false ∧
      Nonforeclosing (s.restrict scope) false := by
  refine ⟨rfl, ?_, ?_⟩
  · rintro ⟨_, none⟩
    exact none ⟨true, by simp, fun _ _ _ => rfl, k, by simp, rfl, rfl⟩
  · refine ⟨by simp [Situation.restrict], ?_⟩
    rintro ⟨b, _, _, k', hk', _, _⟩
    simp [Situation.restrict, omitted] at hk'

/-- Omission can also condemn: each course secures one center's continuation;
dropping one of them makes the course that secures it look improvable. -/
theorem omitted_scope_can_condemn :
    let s : Situation Bool Bool :=
      { courses := [false, true], continuations := [false, true],
        secures := fun a k => a == k }
    Nonforeclosing s true ∧ ¬ Nonforeclosing (s.restrict fun k => !k) true := by
  refine ⟨⟨by simp, ?_⟩, ?_⟩
  · rintro ⟨b, _, incl, _⟩
    have := incl true (by simp) (by simp)
    cases b <;> simp_all
  · rintro ⟨_, none⟩
    refine none ⟨false, by simp [Situation.restrict], ?_, false,
      by simp [Situation.restrict], rfl, rfl⟩
    intro k hk _
    simp [Situation.restrict] at hk
    subst hk
    rfl

/-- How many considered continuations a course secures. -/
def Situation.securedCount (s : Situation A K) (a : A) : Nat :=
  s.continuations.countP fun k => s.secures a k

theorem countP_lt_of_improves (p q : K → Bool) :
    ∀ l : List K, (∀ k ∈ l, p k = true → q k = true) →
      (∃ k ∈ l, q k = true ∧ p k = false) → l.countP p < l.countP q
  | [], _, ⟨_, hk, _⟩ => by cases hk
  | x :: xs, incl, ⟨k, hk, yes, no⟩ => by
    have inclTail : ∀ k ∈ xs, p k = true → q k = true :=
      fun k hk => incl k (List.mem_cons_of_mem _ hk)
    have le : xs.countP p ≤ xs.countP q := by
      clear hk yes no incl
      induction xs with
      | nil => exact Nat.le_refl _
      | cons y ys ih =>
        have hy := inclTail y (List.mem_cons_self ..)
        have ih' := ih (fun k hk => inclTail k (List.mem_cons_of_mem _ hk))
        simp only [List.countP_cons]
        cases hp : p y <;> cases hq : q y <;> simp_all <;> omega
    rcases List.mem_cons.mp hk with rfl | hk'
    · simp only [List.countP_cons, yes, no]
      simp
      omega
    · have lt := countP_lt_of_improves p q xs inclTail ⟨k, hk', yes, no⟩
      have hx := incl x (List.mem_cons_self ..)
      simp only [List.countP_cons]
      cases hp : p x <;> cases hq : q x <;> simp_all <;> omega

theorem improves_count (s : Situation A K) (a b : A) (h : Improves s b a) :
    s.securedCount a < s.securedCount b :=
  countP_lt_of_improves _ _ s.continuations h.1 h.2

theorem exists_max (f : A → Nat) :
    ∀ l : List A, l ≠ [] → ∃ a ∈ l, ∀ b ∈ l, f b ≤ f a
  | [], h => absurd rfl h
  | [x], _ => ⟨x, by simp, fun b hb => by simp at hb; rw [hb]; exact Nat.le_refl _⟩
  | x :: y :: rest, _ => by
    obtain ⟨m, hm, hmax⟩ := exists_max f (y :: rest) (by simp)
    by_cases hxm : f m ≤ f x
    · refine ⟨x, by simp, fun b hb => ?_⟩
      rcases List.mem_cons.mp hb with rfl | hb
      · exact Nat.le_refl _
      · exact Nat.le_trans (hmax b hb) hxm
    · refine ⟨m, List.mem_cons_of_mem _ hm, fun b hb => ?_⟩
      rcases List.mem_cons.mp hb with rfl | hb
      · omega
      · exact hmax b hb

/-- Every finite situation with an available course has a course that forecloses
nothing needlessly. -/
theorem nonforeclosing_exists (s : Situation A K) (h : s.courses ≠ []) :
    ∃ a, Nonforeclosing s a := by
  obtain ⟨a, ha, amax⟩ := exists_max s.securedCount s.courses h
  refine ⟨a, ha, fun ⟨b, hb, imp⟩ => ?_⟩
  have := improves_count s a b imp
  have := amax b hb
  omega

/-! ### Symmetric competition between two centers -/

/-- Two courses and two centers' continuations: course `c` secures exactly
center `c`'s continuation. -/
def competition : Bool → Bool → Bool := fun course k => course == k

theorem both_courses_nonforeclosing (c : Bool) :
    Nonforeclosing ⟨[false, true], [false, true], competition⟩ c := by
  refine ⟨by cases c <;> simp, ?_⟩
  rintro ⟨b, _, incl, _⟩
  have := incl c (by cases c <;> simp) (by simp [competition])
  cases b <;> cases c <;> simp_all [competition]

/-- A deterministic choice rule over such two-course, two-continuation
structures that treats the centers alike: relabeling both centers (and hence
which course secures which) relabels its choice. -/
def TreatsCentersAlike (rule : (Bool → Bool → Bool) → Bool) : Prop :=
  ∀ secures, rule (fun course k => secures (!course) (!k)) = !(rule secures)

/-- No such rule can choose in the symmetric competition: the structure alone
does not say whose continuation to secure. The rule must output a course, so
abstention is not among its options; the proof uses only that the competition
is unchanged by the relabeling. -/
theorem symmetric_competition_has_no_structural_choice :
    ¬ ∃ rule, TreatsCentersAlike rule := by
  rintro ⟨rule, alike⟩
  have h := alike competition
  have same : (fun course k => competition (!course) (!k)) = competition := by
    funext course k
    cases course <;> cases k <;> rfl
  rw [same] at h
  cases hr : rule competition <;> simp [hr] at h

/-! ### Withdrawal after fulfillment -/

/-- Continuation `true` is the organization's own claim, `false` another
center's continuation; course `true` acts on the claim and forecloses the other,
course `false` abstains. -/
def beforeFulfillment : Situation Bool Bool :=
  { courses := [false, true], continuations := [false, true],
    secures := fun act k => if k then act else !act }

/-- Once the claim is fulfilled it is secured whatever is done now. -/
def afterFulfillment : Situation Bool Bool :=
  { beforeFulfillment with secures := fun act k => if k then true else !act }

theorem fulfillment_turns_retained_course_foreclosing :
    Nonforeclosing beforeFulfillment true ∧ Nonforeclosing beforeFulfillment false ∧
      ¬ Nonforeclosing afterFulfillment true ∧ Nonforeclosing afterFulfillment false ∧
      afterFulfillment.reached true = false := by
  refine ⟨⟨by simp [beforeFulfillment], ?_⟩, ⟨by simp [beforeFulfillment], ?_⟩,
    ?_, ⟨by simp [afterFulfillment, beforeFulfillment], ?_⟩, rfl⟩
  · rintro ⟨b, _, incl, _⟩
    have := incl true (by simp [beforeFulfillment]) (by simp [beforeFulfillment])
    cases b <;> simp_all [beforeFulfillment]
  · rintro ⟨b, _, incl, _⟩
    have := incl false (by simp [beforeFulfillment]) (by simp [beforeFulfillment])
    cases b <;> simp_all [beforeFulfillment]
  · rintro ⟨_, none⟩
    refine none ⟨false, by simp [afterFulfillment, beforeFulfillment], ?_, false,
      by simp [afterFulfillment, beforeFulfillment], by simp [afterFulfillment], by
        simp [afterFulfillment]⟩
    intro k _ _
    cases k <;> simp [afterFulfillment]
  · rintro ⟨b, _, _, k, hk, yes, no⟩
    cases k <;> cases b <;> simp_all [afterFulfillment]

end ContinuationScope

#print axioms ContinuationScope.Situation
#print axioms ContinuationScope.Improves
#print axioms ContinuationScope.Nonforeclosing
#print axioms ContinuationScope.Situation.reached
#print axioms ContinuationScope.Situation.restrict
#print axioms ContinuationScope.unreached_agree
#print axioms ContinuationScope.unreached_never_matters
#print axioms ContinuationScope.nonforeclosing_restrict_iff
#print axioms ContinuationScope.omitted_scope_admits_needless_foreclosure
#print axioms ContinuationScope.omitted_scope_can_condemn
#print axioms ContinuationScope.Situation.securedCount
#print axioms ContinuationScope.countP_lt_of_improves
#print axioms ContinuationScope.improves_count
#print axioms ContinuationScope.exists_max
#print axioms ContinuationScope.nonforeclosing_exists
#print axioms ContinuationScope.competition
#print axioms ContinuationScope.both_courses_nonforeclosing
#print axioms ContinuationScope.TreatsCentersAlike
#print axioms ContinuationScope.symmetric_competition_has_no_structural_choice
#print axioms ContinuationScope.beforeFulfillment
#print axioms ContinuationScope.afterFulfillment
#print axioms ContinuationScope.fulfillment_turns_retained_course_foreclosing
