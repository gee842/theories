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

theorem mem_cons_cases {α : Type} {a x : α} {l : List α} (h : a ∈ x :: l) :
    a = x ∨ a ∈ l := by
  cases h with
  | head => exact Or.inl rfl
  | tail _ h => exact Or.inr h

theorem any_false_mem {α : Type} (f : α → Bool) :
    ∀ l : List α, l.any f = false → ∀ x ∈ l, f x = false
  | [], _, _, hx => nomatch hx
  | y :: ys, h, x, hx => by
    have h' : (f y || ys.any f) = false := h
    cases hfy : f y with
    | true => rw [hfy] at h'; exact nomatch h'
    | false =>
      rw [hfy] at h'
      cases mem_cons_cases hx with
      | inl e => rw [e]; exact hfy
      | inr hm => exact any_false_mem f ys h' x hm

theorem mem_filter_of {α : Type} {p : α → Bool} {x : α} :
    ∀ {l : List α}, x ∈ l → p x = true → x ∈ l.filter p
  | [], hx, _ => nomatch hx
  | y :: ys, hx, hp => by
    cases hy : p y with
    | true =>
      rw [List.filter_cons_of_pos hy]
      cases mem_cons_cases hx with
      | inl e => rw [e]; exact List.Mem.head _
      | inr hm => exact List.Mem.tail _ (mem_filter_of hm hp)
    | false =>
      rw [List.filter_cons_of_neg (fun h => nomatch hy.symm.trans h)]
      cases mem_cons_cases hx with
      | inl e => rw [e, hy] at hp; exact nomatch hp
      | inr hm => exact mem_filter_of hm hp

theorem of_mem_filter {α : Type} {p : α → Bool} {x : α} :
    ∀ {l : List α}, x ∈ l.filter p → x ∈ l ∧ p x = true
  | [], hx => nomatch hx
  | y :: ys, hx => by
    cases hy : p y with
    | true =>
      rw [List.filter_cons_of_pos hy] at hx
      cases mem_cons_cases hx with
      | inl e => rw [e]; exact ⟨List.Mem.head _, hy⟩
      | inr hm =>
        have r := of_mem_filter hm
        exact ⟨List.Mem.tail _ r.1, r.2⟩
    | false =>
      rw [List.filter_cons_of_neg (fun h => nomatch hy.symm.trans h)] at hx
      have r := of_mem_filter hx
      exact ⟨List.Mem.tail _ r.1, r.2⟩

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
  have inner := any_false_mem _ s.courses h a ha
  have hab : (s.secures a k != s.secures b k) = false :=
    any_false_mem _ s.courses inner b hb
  revert hab
  cases s.secures a k <;> cases s.secures b k <;> intro hab <;>
    first | rfl | exact nomatch hab

/-- Restricting attention to the reached continuations never changes whether
one available course improves on another. -/
theorem unreached_never_matters (s : Situation A K) (a b : A)
    (ha : a ∈ s.courses) (hb : b ∈ s.courses) :
    Improves s b a ↔ Improves (s.restrict s.reached) b a := by
  constructor
  · rintro ⟨incl, k, hk, yes, no⟩
    have hr : s.reached k = true := by
      cases hr : s.reached k
      · have := unreached_agree s k hr a b ha hb
        rw [no, yes] at this
        exact nomatch this
      · rfl
    exact ⟨fun k' hk' => incl k' (of_mem_filter hk').1, k, mem_filter_of hk hr, yes, no⟩
  · rintro ⟨incl, k, hk, yes, no⟩
    refine ⟨fun k' hk' sa => ?_, k, (of_mem_filter hk).1, yes, no⟩
    cases hr : s.reached k'
    · rw [← unreached_agree s k' hr a b ha hb]
      exact sa
    · exact incl k' (mem_filter_of hk' hr) sa

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
    exact none ⟨true, List.Mem.tail _ (List.Mem.head _), fun _ _ _ => rfl, k,
      List.Mem.head _, rfl, rfl⟩
  · refine ⟨List.Mem.head _, ?_⟩
    rintro ⟨b, _, _, k', hk', _, _⟩
    have hk'' : k' ∈ ([k] : List K).filter scope := hk'
    rw [List.filter_cons_of_neg (fun h => nomatch omitted.symm.trans h)] at hk''
    exact nomatch hk''

/-- Omission can also condemn: each course secures one center's continuation;
dropping one of them makes the course that secures it look improvable. -/
theorem omitted_scope_can_condemn :
    let s : Situation Bool Bool :=
      { courses := [false, true], continuations := [false, true],
        secures := fun a k => a == k }
    Nonforeclosing s true ∧ ¬ Nonforeclosing (s.restrict fun k => !k) true := by
  refine ⟨⟨List.Mem.tail _ (List.Mem.head _), ?_⟩, ?_⟩
  · rintro ⟨b, _, incl, k, _, yes, no⟩
    have := incl true (List.Mem.tail _ (List.Mem.head _)) rfl
    cases b
    · exact nomatch this
    · exact nomatch yes.symm.trans no
  · rintro ⟨_, none⟩
    refine none ⟨false, List.Mem.head _, ?_, false, List.Mem.head _, rfl, rfl⟩
    intro k hk _
    have hk' : k ∈ [false] := hk
    cases mem_cons_cases hk' with
    | inl e => rw [e]; rfl
    | inr hm => exact nomatch hm

/-- How many considered continuations a course secures. -/
def Situation.securedCount (s : Situation A K) (a : A) : Nat :=
  s.continuations.countP fun k => s.secures a k

theorem countP_go_acc {α : Type} (p : α → Bool) :
    ∀ (l : List α) (n : Nat), List.countP.go p l n = List.countP.go p l 0 + n
  | [], n => (Nat.zero_add n).symm
  | x :: xs, n => by
    show (bif p x then List.countP.go p xs (n + 1) else List.countP.go p xs n) =
      (bif p x then List.countP.go p xs (0 + 1) else List.countP.go p xs 0) + n
    cases p x with
    | true =>
      show List.countP.go p xs (n + 1) = List.countP.go p xs (0 + 1) + n
      rw [countP_go_acc p xs (n + 1), countP_go_acc p xs (0 + 1), Nat.add_assoc,
        Nat.zero_add, Nat.add_comm 1 n]
    | false => exact countP_go_acc p xs n

theorem countP_cons_true {α : Type} {p : α → Bool} {x : α} {xs : List α}
    (h : p x = true) : (x :: xs).countP p = xs.countP p + 1 := by
  show (bif p x then List.countP.go p xs (0 + 1) else List.countP.go p xs 0) = _
  rw [h]
  exact countP_go_acc p xs (0 + 1)

theorem countP_cons_false {α : Type} {p : α → Bool} {x : α} {xs : List α}
    (h : p x = false) : (x :: xs).countP p = xs.countP p := by
  show (bif p x then List.countP.go p xs (0 + 1) else List.countP.go p xs 0) = _
  rw [h]
  rfl

theorem countP_le_of_incl {α : Type} (p q : α → Bool) :
    ∀ l : List α, (∀ k ∈ l, p k = true → q k = true) → l.countP p ≤ l.countP q
  | [], _ => Nat.le_refl _
  | y :: ys, incl => by
    have ih := countP_le_of_incl p q ys (fun k hk => incl k (List.Mem.tail _ hk))
    cases hp : p y with
    | true =>
      have hq := incl y (List.Mem.head _) hp
      rw [countP_cons_true hp, countP_cons_true hq]
      exact Nat.succ_le_succ ih
    | false =>
      rw [countP_cons_false hp]
      cases hq : q y with
      | true => rw [countP_cons_true hq]; exact Nat.le_succ_of_le ih
      | false => rw [countP_cons_false hq]; exact ih

theorem countP_lt_of_improves (p q : K → Bool) :
    ∀ l : List K, (∀ k ∈ l, p k = true → q k = true) →
      (∃ k ∈ l, q k = true ∧ p k = false) → l.countP p < l.countP q
  | [], _, ⟨_, hk, _⟩ => nomatch hk
  | x :: xs, incl, ⟨k, hk, yes, no⟩ => by
    have inclTail : ∀ k ∈ xs, p k = true → q k = true :=
      fun k hk => incl k (List.Mem.tail _ hk)
    have le : xs.countP p ≤ xs.countP q := countP_le_of_incl p q xs inclTail
    cases mem_cons_cases hk with
    | inl e =>
      rw [e] at yes no
      rw [countP_cons_false no, countP_cons_true yes]
      exact Nat.lt_succ_of_le le
    | inr hk' =>
      have lt := countP_lt_of_improves p q xs inclTail ⟨k, hk', yes, no⟩
      cases hp : p x with
      | true =>
        have hq := incl x (List.Mem.head _) hp
        rw [countP_cons_true hp, countP_cons_true hq]
        exact Nat.succ_lt_succ lt
      | false =>
        rw [countP_cons_false hp]
        cases hq : q x with
        | true => rw [countP_cons_true hq]; exact Nat.lt_succ_of_lt lt
        | false => rw [countP_cons_false hq]; exact lt

theorem improves_count (s : Situation A K) (a b : A) (h : Improves s b a) :
    s.securedCount a < s.securedCount b :=
  countP_lt_of_improves _ _ s.continuations h.1 h.2

theorem exists_max (f : A → Nat) :
    ∀ l : List A, l ≠ [] → ∃ a ∈ l, ∀ b ∈ l, f b ≤ f a
  | [], h => absurd rfl h
  | [x], _ => ⟨x, List.Mem.head _, fun b hb => by
      cases mem_cons_cases hb with
      | inl e => rw [e]; exact Nat.le_refl _
      | inr hm => exact nomatch hm⟩
  | x :: y :: rest, _ => by
    obtain ⟨m, hm, hmax⟩ := exists_max f (y :: rest) (fun h => nomatch h)
    match Nat.decLe (f m) (f x) with
    | isTrue hxm =>
      refine ⟨x, List.Mem.head _, fun b hb => ?_⟩
      cases mem_cons_cases hb with
      | inl e => rw [e]; exact Nat.le_refl _
      | inr hb => exact Nat.le_trans (hmax b hb) hxm
    | isFalse hxm =>
      refine ⟨m, List.Mem.tail _ hm, fun b hb => ?_⟩
      cases mem_cons_cases hb with
      | inl e => rw [e]; exact Nat.le_of_lt (Nat.lt_of_not_le hxm)
      | inr hb => exact hmax b hb

/-- Every finite situation with an available course has a course that forecloses
nothing needlessly. -/
theorem nonforeclosing_exists (s : Situation A K) (h : s.courses ≠ []) :
    ∃ a, Nonforeclosing s a := by
  obtain ⟨a, ha, amax⟩ := exists_max s.securedCount s.courses h
  refine ⟨a, ha, fun ⟨b, hb, imp⟩ => ?_⟩
  exact Nat.lt_irrefl _ (Nat.lt_of_lt_of_le (improves_count s a b imp) (amax b hb))

/-! ### Symmetric competition between two centers -/

/-- Two courses and two centers' continuations: course `c` secures exactly
center `c`'s continuation. -/
def competition : Bool → Bool → Bool := fun course k => course == k

theorem both_courses_nonforeclosing (c : Bool) :
    Nonforeclosing ⟨[false, true], [false, true], competition⟩ c := by
  have hc : c ∈ [false, true] := by
    cases c
    · exact List.Mem.head _
    · exact List.Mem.tail _ (List.Mem.head _)
  refine ⟨hc, ?_⟩
  rintro ⟨b, _, incl, k, _, yes, no⟩
  have hcc : competition c c = true := by cases c <;> rfl
  have := incl c hc hcc
  cases b <;> cases c
  · exact nomatch yes.symm.trans no
  · exact nomatch this
  · exact nomatch this
  · exact nomatch yes.symm.trans no

/-- A deterministic choice rule over such two-course, two-continuation
structures that treats the centers alike: relabeling both centers (and hence
which course secures which) relabels its choice. -/
def TreatsCentersAlike (rule : (Bool → Bool → Bool) → Bool) : Prop :=
  ∀ secures, rule (fun course k => secures (!course) (!k)) = !(rule secures)

/-- No such rule can choose in the symmetric competition: the structure alone
does not say whose continuation to secure. The rule must output a course, so
abstention is not among its options. The proof needs only one structure that
the relabeling leaves unchanged; the constant structure is used, so that no
equality of functions is needed, and the symmetric competition is another. -/
theorem symmetric_competition_has_no_structural_choice :
    ¬ ∃ rule, TreatsCentersAlike rule := by
  rintro ⟨rule, alike⟩
  have h := alike fun _ _ => true
  revert h
  cases rule fun _ _ => true <;> intro h <;> exact nomatch h

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
  refine ⟨⟨List.Mem.tail _ (List.Mem.head _), ?_⟩, ⟨List.Mem.head _, ?_⟩,
    ?_, ⟨List.Mem.head _, ?_⟩, rfl⟩
  · rintro ⟨b, _, incl, k, _, yes, no⟩
    have := incl true (List.Mem.tail _ (List.Mem.head _)) rfl
    cases b
    · exact nomatch this
    · exact nomatch yes.symm.trans no
  · rintro ⟨b, _, incl, k, _, yes, no⟩
    have := incl false (List.Mem.head _) rfl
    cases b
    · exact nomatch yes.symm.trans no
    · exact nomatch this
  · rintro ⟨_, none⟩
    refine none ⟨false, List.Mem.head _, ?_, false, List.Mem.head _, rfl, rfl⟩
    intro k _ _
    cases k <;> rfl
  · rintro ⟨b, _, _, k, hk, yes, no⟩
    cases k <;> exact nomatch no

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
#print axioms ContinuationScope.mem_cons_cases
#print axioms ContinuationScope.any_false_mem
#print axioms ContinuationScope.mem_filter_of
#print axioms ContinuationScope.of_mem_filter
#print axioms ContinuationScope.countP_go_acc
#print axioms ContinuationScope.countP_cons_true
#print axioms ContinuationScope.countP_cons_false
#print axioms ContinuationScope.countP_le_of_incl
