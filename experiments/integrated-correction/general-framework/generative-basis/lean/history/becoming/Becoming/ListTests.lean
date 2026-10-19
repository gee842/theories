/-!
# Boolean tests over lists and options, constructively

The core's models of a requested change carried out (`Becoming.ContingentPlans` and the modules after it) decide
their conditions by Boolean tests over finite lists: every member passes (`List.all`), some
member passes (`List.any`), the first member that passes (`List.find?`), the members that pass
(`List.filter`), membership by equality (`List.contains`), and options that hold a value
(`Option.any`, `bind`, `map`). Lean's prelude proves what these tests say with `propext`, so
the core cannot cite those proofs. This module proves the facts the models use, each by
recursion on the list or by cases on the option, with empty axiom reports.

* **Truth values.** A conjunction is true exactly where both are (`and_true_iff`), a
  disjunction exactly where one is (`or_true_iff`), a negation exactly where the value is false
  (`not_true_iff`), and a value is false exactly where it is not true (`false_iff_not`).
* **Lists.** `all` and `any` say every and some member passes (`all_true_iff`,
  `any_true_iff`); `contains` is membership (`contains_true_iff`); a member of `filter`,
  `map`, `flatMap` and `++` is what the operation says (`mem_filter_iff`, `mem_map_iff`,
  `mem_flatMap_iff`, `mem_append_iff`); `find?` returns a member that passes, and returns nothing
  exactly where no member passes (`find_some`, `mem_of_find_some`, `find_isSome_iff`,
  `find_none_iff`).
* **Options.** A bound option holds a value exactly where both stages do (`bind_eq_some`), a
  mapped one where the option does (`map_eq_some`), and `Option.any` holds exactly where the
  value passes (`option_any_true_iff`).

No premise; every declaration has an empty axiom report.
-/

namespace Becoming

namespace ListTests

universe u v

variable {α : Type u} {β : Type v}

/-! ## Truth values -/

theorem and_true_iff : ∀ {a b : Bool}, (a && b) = true ↔ a = true ∧ b = true
  | true, true => ⟨fun _ => ⟨rfl, rfl⟩, fun _ => rfl⟩
  | true, false => ⟨fun h => Bool.noConfusion h, fun h => Bool.noConfusion h.2⟩
  | false, _ => ⟨fun h => Bool.noConfusion h, fun h => Bool.noConfusion h.1⟩

theorem or_true_iff : ∀ {a b : Bool}, (a || b) = true ↔ a = true ∨ b = true
  | true, _ => ⟨fun _ => .inl rfl, fun _ => rfl⟩
  | false, true => ⟨fun _ => .inr rfl, fun _ => rfl⟩
  | false, false => ⟨fun h => Bool.noConfusion h,
      fun h => h.elim (fun e => Bool.noConfusion e) (fun e => Bool.noConfusion e)⟩

theorem not_true_iff : ∀ {a : Bool}, (!a) = true ↔ a = false
  | true => ⟨fun h => Bool.noConfusion h, fun h => Bool.noConfusion h⟩
  | false => ⟨fun _ => rfl, fun _ => rfl⟩

theorem false_iff_not : ∀ {b : Bool}, b = false ↔ ¬ b = true
  | true => ⟨fun e => Bool.noConfusion e, fun n => absurd rfl n⟩
  | false => ⟨fun _ e => Bool.noConfusion e, fun _ => rfl⟩

theorem and_left {a b : Bool} (h : (a && b) = true) : a = true := (and_true_iff.mp h).1

theorem and_right {a b : Bool} (h : (a && b) = true) : b = true := (and_true_iff.mp h).2

/-- A decided proposition is true exactly where it holds. -/
theorem decide_true_iff {p : Prop} [Decidable p] : decide p = true ↔ p :=
  ⟨of_decide_eq_true, decide_eq_true⟩

/-- Equality tested by a decided equality is equality. -/
theorem beq_true_iff [DecidableEq α] {a b : α} : (a == b) = true ↔ a = b := decide_true_iff

theorem beq_false_iff [DecidableEq α] {a b : α} : (a == b) = false ↔ a ≠ b :=
  false_iff_not.trans ⟨fun n e => n (beq_true_iff.mpr e), fun n e => n (beq_true_iff.mp e)⟩

/-! ## Membership -/

theorem mem_cons_iff {a b : α} {l : List α} : a ∈ b :: l ↔ a = b ∨ a ∈ l :=
  ⟨fun m => match m with
    | .head _ => .inl rfl
    | .tail _ m => .inr m,
   fun h => h.elim (fun e => e ▸ .head l) (fun m => .tail b m)⟩

theorem not_mem_nil {a : α} : ¬ a ∈ ([] : List α) := fun m => nomatch m

theorem mem_singleton_iff {a b : α} : a ∈ [b] ↔ a = b :=
  mem_cons_iff.trans ⟨fun h => h.elim id (fun m => absurd m not_mem_nil), .inl⟩

theorem mem_append_iff {a : α} : ∀ {l m : List α}, a ∈ l ++ m ↔ a ∈ l ∨ a ∈ m
  | [], _ => ⟨.inr, fun h => h.elim (fun m => absurd m not_mem_nil) id⟩
  | _ :: _, _ =>
    mem_cons_iff.trans (Iff.trans (or_congr Iff.rfl mem_append_iff)
      ⟨fun h => h.elim (fun e => .inl (mem_cons_iff.mpr (.inl e)))
          (fun h => h.elim (fun x => .inl (mem_cons_iff.mpr (.inr x))) .inr),
       fun h => h.elim (fun x => (mem_cons_iff.mp x).elim .inl (fun y => .inr (.inl y)))
          (fun y => .inr (.inr y))⟩)

/-! ## `all`, `any` and `contains` -/

theorem all_true_iff {p : α → Bool} : ∀ {l : List α}, l.all p = true ↔ ∀ x, x ∈ l → p x = true
  | [] => ⟨fun _ _ m => absurd m not_mem_nil, fun _ => rfl⟩
  | a :: l =>
    and_true_iff.trans ⟨fun ⟨pa, rest⟩ x m => (mem_cons_iff.mp m).elim (fun e => e ▸ pa)
        (fun m => all_true_iff.mp rest x m),
      fun all => ⟨all a (.head l), all_true_iff.mpr fun x m => all x (.tail a m)⟩⟩

theorem any_true_iff {p : α → Bool} : ∀ {l : List α}, l.any p = true ↔ ∃ x, x ∈ l ∧ p x = true
  | [] => ⟨fun h => Bool.noConfusion h, fun ⟨_, m, _⟩ => absurd m not_mem_nil⟩
  | a :: l =>
    or_true_iff.trans ⟨fun h => h.elim (fun pa => ⟨a, .head l, pa⟩)
        (fun rest => match any_true_iff.mp rest with | ⟨x, m, px⟩ => ⟨x, .tail a m, px⟩),
      fun ⟨x, m, px⟩ => (mem_cons_iff.mp m).elim (fun e => .inl (e ▸ px))
        (fun m => .inr (any_true_iff.mpr ⟨x, m, px⟩))⟩

theorem all_mem {p : α → Bool} {l : List α} (h : l.all p = true) {x : α} (m : x ∈ l) :
    p x = true := all_true_iff.mp h x m

theorem contains_true_iff [DecidableEq α] {a : α} : ∀ {l : List α}, l.contains a = true ↔ a ∈ l
  | [] => ⟨fun h => Bool.noConfusion h, fun m => absurd m not_mem_nil⟩
  | b :: l => by
    show (match a == b with | true => true | false => List.elem a l) = true ↔ a ∈ b :: l
    cases h : (a == b) with
    | true => exact ⟨fun _ => mem_cons_iff.mpr (.inl (beq_true_iff.mp h)), fun _ => rfl⟩
    | false => exact ⟨fun e => .tail b (contains_true_iff.mp e),
        fun m => (mem_cons_iff.mp m).elim (fun e => absurd e (beq_false_iff.mp h))
          contains_true_iff.mpr⟩

theorem contains_false_iff [DecidableEq α] {a : α} {l : List α} :
    l.contains a = false ↔ ¬ a ∈ l :=
  false_iff_not.trans ⟨fun n m => n (contains_true_iff.mpr m), fun n e => n (contains_true_iff.mp e)⟩

theorem isEmpty_false_iff : ∀ {l : List α}, l.isEmpty = false ↔ l ≠ []
  | [] => ⟨fun h => Bool.noConfusion h, fun n => absurd rfl n⟩
  | _ :: _ => ⟨fun _ e => (nomatch e), fun _ => rfl⟩

theorem not_isEmpty_true_iff {l : List α} : (!l.isEmpty) = true ↔ l ≠ [] :=
  not_true_iff.trans isEmpty_false_iff

/-! ## `filter`, `map` and `flatMap` -/

theorem mem_filter_iff {p : α → Bool} {x : α} :
    ∀ {l : List α}, x ∈ l.filter p ↔ x ∈ l ∧ p x = true
  | [] => ⟨fun m => absurd m not_mem_nil, fun h => absurd h.1 not_mem_nil⟩
  | a :: l => by
    show x ∈ (match p a with | true => a :: l.filter p | false => l.filter p) ↔ _
    cases h : p a with
    | true => exact ⟨fun m => (mem_cons_iff.mp m).elim (fun e => ⟨e ▸ .head l, e ▸ h⟩)
          (fun m => ⟨.tail a (mem_filter_iff.mp m).1, (mem_filter_iff.mp m).2⟩),
        fun ⟨m, px⟩ => (mem_cons_iff.mp m).elim (fun e => e ▸ .head _)
          (fun m => .tail a (mem_filter_iff.mpr ⟨m, px⟩))⟩
    | false => exact ⟨fun m => ⟨.tail a (mem_filter_iff.mp m).1, (mem_filter_iff.mp m).2⟩,
        fun ⟨m, px⟩ => (mem_cons_iff.mp m).elim
          (fun e => Bool.noConfusion (h.symm.trans (e ▸ px)))
          (fun m => mem_filter_iff.mpr ⟨m, px⟩)⟩

/-- A filter every member of which passes keeps the list. -/
theorem filter_of_all {p : α → Bool} : ∀ {l : List α}, (∀ x, x ∈ l → p x = true) → l.filter p = l
  | [], _ => rfl
  | a :: l, all => by
    show (match p a with | true => a :: l.filter p | false => l.filter p) = a :: l
    rw [all a (.head l)]
    exact congrArg (a :: ·) (filter_of_all fun x m => all x (.tail a m))

theorem mem_map_iff {f : α → β} {y : β} : ∀ {l : List α}, y ∈ l.map f ↔ ∃ x, x ∈ l ∧ f x = y
  | [] => ⟨fun m => absurd m not_mem_nil, fun ⟨_, m, _⟩ => absurd m not_mem_nil⟩
  | a :: l => mem_cons_iff.trans ⟨fun h => h.elim (fun e => ⟨a, .head l, e.symm⟩)
      (fun m => match mem_map_iff.mp m with | ⟨x, m, e⟩ => ⟨x, .tail a m, e⟩),
    fun ⟨x, m, e⟩ => (mem_cons_iff.mp m).elim (fun same => .inl (e ▸ same ▸ rfl))
      (fun m => .inr (mem_map_iff.mpr ⟨x, m, e⟩))⟩

theorem mem_map_of {f : α → β} {x : α} {l : List α} (m : x ∈ l) : f x ∈ l.map f :=
  mem_map_iff.mpr ⟨x, m, rfl⟩

theorem mem_flatten_iff {y : β} : ∀ {ls : List (List β)}, y ∈ ls.flatten ↔ ∃ l, l ∈ ls ∧ y ∈ l
  | [] => ⟨fun m => absurd m not_mem_nil, fun ⟨_, m, _⟩ => absurd m not_mem_nil⟩
  | l :: ls => mem_append_iff.trans ⟨fun h => h.elim (fun m => ⟨l, .head ls, m⟩)
      (fun m => match mem_flatten_iff.mp m with | ⟨l', m', y'⟩ => ⟨l', .tail l m', y'⟩),
    fun ⟨l', m', y'⟩ => (mem_cons_iff.mp m').elim (fun e => .inl (e ▸ y'))
      (fun m' => .inr (mem_flatten_iff.mpr ⟨l', m', y'⟩))⟩

theorem mem_flatMap_iff {f : α → List β} {y : β} {l : List α} :
    y ∈ l.flatMap f ↔ ∃ x, x ∈ l ∧ y ∈ f x :=
  mem_flatten_iff.trans ⟨fun ⟨_, m, y'⟩ => match mem_map_iff.mp m with
      | ⟨x, mx, e⟩ => ⟨x, mx, e ▸ y'⟩,
    fun ⟨x, mx, y'⟩ => ⟨f x, mem_map_of mx, y'⟩⟩

theorem length_append : ∀ (l m : List α), (l ++ m).length = l.length + m.length
  | [], m => (Nat.zero_add m.length).symm
  | _ :: l, m => (congrArg (· + 1) (length_append l m)).trans (Nat.succ_add l.length m.length).symm

/-! ## `find?` -/

theorem find_some {p : α → Bool} : ∀ {l : List α} {a : α}, l.find? p = some a → p a = true
  | [], _, h => nomatch h
  | b :: l, _, h => by
    revert h
    show (match p b with | true => some b | false => l.find? p) = _ → _
    cases hb : p b with
    | true => exact fun h => (Option.some.inj h) ▸ hb
    | false => exact find_some

theorem mem_of_find_some {p : α → Bool} : ∀ {l : List α} {a : α}, l.find? p = some a → a ∈ l
  | [], _, h => nomatch h
  | b :: l, _, h => by
    revert h
    show (match p b with | true => some b | false => l.find? p) = _ → _
    cases p b with
    | true => exact fun h => (Option.some.inj h) ▸ .head l
    | false => exact fun h => .tail b (mem_of_find_some h)

theorem find_none_iff {p : α → Bool} : ∀ {l : List α}, l.find? p = none ↔ ∀ x, x ∈ l → p x = false
  | [] => ⟨fun _ _ m => absurd m not_mem_nil, fun _ => rfl⟩
  | b :: l => by
    show (match p b with | true => some b | false => l.find? p) = none ↔ _
    cases hb : p b with
    | true => exact ⟨fun h => (nomatch h), fun all => Bool.noConfusion (hb.symm.trans (all b (.head l)))⟩
    | false => exact ⟨fun h x m => (mem_cons_iff.mp m).elim (fun e => e ▸ hb)
          (fun m => find_none_iff.mp h x m),
        fun all => find_none_iff.mpr fun x m => all x (.tail b m)⟩

theorem find_isSome_iff {p : α → Bool} {l : List α} :
    (l.find? p).isSome = true ↔ ∃ x, x ∈ l ∧ p x = true :=
  match h : l.find? p with
  | some a => ⟨fun _ => ⟨a, mem_of_find_some h, find_some h⟩, fun _ => rfl⟩
  | none => ⟨fun e => Bool.noConfusion e, fun ⟨x, m, px⟩ =>
      Bool.noConfusion ((find_none_iff.mp h x m).symm.trans px)⟩

/-! ## Options -/

theorem bind_eq_some {γ δ : Type} {o : Option γ} {f : γ → Option δ} {b : δ} :
    (o >>= f) = some b ↔ ∃ a, o = some a ∧ f a = some b :=
  match o with
  | none => ⟨fun h => (nomatch h), fun ⟨_, h, _⟩ => nomatch h⟩
  | some a => ⟨fun h => ⟨a, rfl, h⟩, fun ⟨_, h, h'⟩ => (Option.some.inj h) ▸ h'⟩

theorem map_eq_some {f : α → β} {b : β} : ∀ {o : Option α}, o.map f = some b ↔ ∃ a, o = some a ∧ f a = b
  | none => ⟨fun h => (nomatch h), fun ⟨_, h, _⟩ => nomatch h⟩
  | some a => ⟨fun h => ⟨a, rfl, Option.some.inj h⟩,
      fun ⟨_, h, e⟩ => congrArg some ((Option.some.inj h) ▸ e)⟩

theorem option_any_true_iff {f : α → Bool} : ∀ {o : Option α}, o.any f = true ↔ ∃ a, o = some a ∧ f a = true
  | none => ⟨fun h => Bool.noConfusion h, fun ⟨_, h, _⟩ => nomatch h⟩
  | some a => ⟨fun h => ⟨a, rfl, h⟩, fun ⟨_, h, h'⟩ => (Option.some.inj h) ▸ h'⟩

theorem isSome_iff {o : Option α} : o.isSome = true ↔ ∃ a, o = some a :=
  match o with
  | some a => ⟨fun _ => ⟨a, rfl⟩, fun _ => rfl⟩
  | none => ⟨fun h => Bool.noConfusion h, fun ⟨_, h⟩ => nomatch h⟩

theorem none_ne_some {a : α} : (none : Option α) ≠ some a := fun e => nomatch e

end ListTests

end Becoming
