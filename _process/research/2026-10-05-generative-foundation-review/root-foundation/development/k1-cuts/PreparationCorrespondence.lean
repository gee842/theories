import Becoming.Copying
import Becoming.Cuts
import Becoming.Feedback
import Becoming.Readout
import GrownFragmentation

/-!
# Preparation and fragmentation as instances of the core

`MaterialMaturation` routes a recipe from a pool of material, one unit of support per placed slot,
and `GrownFragmentation` cuts actually grown graphs and certifies the components left. This
periphery module reads both on the core's general laws.

* **Preparation is copying with a unit draw.** `route` completes with `rest` left in the pool and
  `left` support free exactly when copying the recipe from the pool, each attachment drawing one
  unit, does (`route_some_iff`). So by `Copying.empties_iff`, preparation completes with an empty
  residual pool exactly when the pool is a permutation of the recipe and the recipe is no longer
  than the support, the support left being the support less the recipe's length
  (`preparation_empties_iff`, `preparation_leaves`).
* **A cut's components are certified closures.** Being connected by the bonds is lying within the
  closure under the bonds read symmetrically (`connected_iff_within`). A component that holds its
  root and is closed on every remaining bond is that closure, by `closure_iff_certified`
  (`component_is_closure`), so `certificate_exact_split` holds from the core law
  (`certificate_exact_split_by_core`), and a certified cut leaves its two ends apart, by
  `not_within_of_closed` (`cut_separates`).
* **Every bond grown by division is needed; a joined bond is bypassed where it crosses.** The
  bonds read both ways are the listed links of `Cuts.Links` (`adjacent_iff_links`,
  `connected_iff_links`). Division attaches a new position by at most one bond, so whatever the
  division word, the bonds stay grown by attachment (`divide_attached`, `develop_attached`), and by
  `Cuts.attached_link_separates` every bond of every body grown by division separates its ends
  when cut (`bond_cut_separates`, `every_grown_bond_separates`); the example's certified cuts are
  cases. After one aggregation, by `Cuts.joined_cut_unchanged_iff`, cutting a grown bond changes
  no connection exactly where the aggregated bond's ends lie on its two sides
  (`aggregate_cut_unchanged_iff`); the reinforced chain's bypass is a case
  (`reinforced_cut_unchanged`).
* **Matched composition does not predict the cut return.** The two grown graphs have the same
  parent summary and different mean cut returns, so by `Readout.no_judge_of_merged` no function of
  the summary gives both (`no_parent_summary_predictor_by_core`).

The local production law, sampling, recipe, stocks and growth histories keep the earlier modules'
scope. The core does not import this module.
-/

namespace Becoming.PreparationCorrespondence

open MaterialMaturation GrownFragmentation

/-! ## Preparation is copying with a unit draw -/

/-- Each attachment draws one unit of support. -/
def unit : Option Bool → Bool → Nat := fun _ _ => 1

theorem use_unit : ∀ (prev : Option Bool) (word : List Bool), Copying.use unit prev word = word.length
  | _, [] => rfl
  | _, x :: xs => by
    show 1 + Copying.use unit (some x) xs = xs.length + 1
    rw [use_unit, Nat.add_comm]

theorem countOf_eq_count (a : Bool) : ∀ l : List Bool, Copying.countOf a l = l.count a
  | [] => rfl
  | x :: xs => by
    rw [List.count_cons, ← countOf_eq_count a xs]
    by_cases h : x = a
    · subst h; simp [Copying.countOf]
    · simp [Copying.countOf, h]

theorem mem_iff_countOf_pos (x : Bool) (pool : List Bool) : x ∈ pool ↔ 0 < Copying.countOf x pool := by
  rw [countOf_eq_count, List.count_pos_iff]

theorem erase_eq_remove (x : Bool) : ∀ pool : List Bool, pool.erase x = Copying.remove x pool
  | [] => rfl
  | y :: ys => by
    rw [List.erase_cons]
    by_cases h : y = x
    · subst h; simp [Copying.remove]
    · simp [Copying.remove, h, erase_eq_remove x ys]

/-- **Preparation is copying with a unit draw.** `route` completes with `rest` left in the pool
and `left` support free exactly when copying the recipe from the pool does. -/
theorem route_some_iff : ∀ (target pool : List Bool) (fuel : Nat) (rest : List Bool) (left : Nat)
    (prev : Option Bool) (built : List Bool) (used : Nat),
    route target pool fuel = some (rest, left) ↔
      (Copying.steps unit target.length ⟨prev, target, built, pool, fuel, used⟩).pending = [] ∧
      (Copying.steps unit target.length ⟨prev, target, built, pool, fuel, used⟩).pool = rest ∧
      (Copying.steps unit target.length ⟨prev, target, built, pool, fuel, used⟩).free = left
  | [], pool, fuel, rest, left, prev, built, used => by
    simp [route, Copying.steps]
  | x :: xs, pool, fuel, rest, left, prev, built, used => by
    have unfold_steps : ∀ s, Copying.steps unit (x :: xs).length s =
        Copying.steps unit xs.length (Copying.tick unit s) := fun _ => rfl
    rw [unfold_steps, Copying.tick_cons]
    by_cases h : x ∈ pool ∧ 0 < fuel
    · have hc : 0 < Copying.countOf x pool ∧ unit prev x ≤ fuel :=
        ⟨(mem_iff_countOf_pos x pool).mp h.1, h.2⟩
      rw [if_pos hc]
      simp only [route, if_pos h, erase_eq_remove]
      exact route_some_iff xs (Copying.remove x pool) (fuel - 1) rest left (some x) (built ++ [x])
        (used + 1)
    · have hc : ¬ (0 < Copying.countOf x pool ∧ unit prev x ≤ fuel) :=
        fun ⟨p, f⟩ => h ⟨(mem_iff_countOf_pos x pool).mpr p, f⟩
      have fixed : Copying.tick unit ⟨prev, x :: xs, built, pool, fuel, used⟩ =
          ⟨prev, x :: xs, built, pool, fuel, used⟩ :=
        (Copying.tick_cons unit prev x xs built pool fuel used).trans (if_neg hc)
      rw [if_neg hc, Copying.steps_fixed unit fixed]
      simp [route, h]

/-- **Whole-pool preparation is copying that empties the pool** (`Copying.empties_iff`): `route`
completes with an empty residual pool exactly when the pool is a permutation of the recipe and the
recipe is no longer than the support. -/
theorem preparation_empties_iff (target pool : List Bool) (fuel : Nat) :
    (∃ left, route target pool fuel = some ([], left)) ↔ pool.Perm target ∧ target.length ≤ fuel := by
  have core := Copying.empties_iff unit none [] target pool fuel 0
  rw [use_unit] at core
  constructor
  · rintro ⟨left, h⟩
    have ⟨done, empty, _⟩ := (route_some_iff target pool fuel [] left none [] 0).mp h
    have ⟨same, covered⟩ := core.mp ⟨done, empty⟩
    refine ⟨List.perm_iff_count.mpr fun a => ?_, covered⟩
    rw [← countOf_eq_count, ← countOf_eq_count]
    exact (same a).symm
  · rintro ⟨perm, covered⟩
    have ⟨done, empty⟩ := core.mpr ⟨fun a => by
      rw [countOf_eq_count, countOf_eq_count]
      exact (List.perm_iff_count.mp perm a).symm, covered⟩
    exact ⟨_, (route_some_iff target pool fuel [] _ none [] 0).mpr ⟨done, empty, rfl⟩⟩

/-- The support left by whole-pool preparation is the support less the recipe's length
(`Copying.copies`). -/
theorem preparation_leaves (target pool : List Bool) (fuel : Nat) (perm : pool.Perm target)
    (covered : target.length ≤ fuel) : route target pool fuel = some ([], fuel - target.length) := by
  have supplies : Copying.Supplies target pool := fun a => by
    rw [countOf_eq_count, countOf_eq_count]
    exact Nat.le_of_eq (List.perm_iff_count.mp perm a).symm
  have within : Copying.use unit none target ≤ fuel := by rw [use_unit]; exact covered
  have done := Copying.copies unit none [] target pool fuel 0 supplies within
  have ⟨_, empty⟩ := (Copying.empties_iff unit none [] target pool fuel 0).mpr
    ⟨fun a => by
      rw [countOf_eq_count, countOf_eq_count]
      exact (List.perm_iff_count.mp perm a).symm, within⟩
  refine (route_some_iff target pool fuel [] _ none [] 0).mpr ⟨?_, empty, ?_⟩
  · rw [done]
  · rw [done, use_unit]

/-! ## A cut's components are certified closures -/

/-- The bonds read as a symmetric relation. -/
def adjacent (bonds : List Edge) (a b : Nat) : Prop := (a, b) ∈ bonds ∨ (b, a) ∈ bonds

theorem connected_of_adjacent {bonds : List Edge} {a b : Nat} (related : adjacent bonds a b) :
    DevelopmentalAssociation.Connected bonds a b :=
  related.elim (fun e => .bond e) (fun e => .symm (.bond e))

/-- **Being connected by the bonds is lying within the closure under them.** -/
theorem connected_iff_within (bonds : List Edge) (a b : Nat) :
    DevelopmentalAssociation.Connected bonds a b ↔ WithinClosure (adjacent bonds) a b := by
  constructor
  · intro h
    induction h with
    | refl a => exact WithinClosure.refl a
    | bond he => exact WithinClosure.of_rel (Or.inl he)
    | symm _ ih => exact WithinClosure.symm (fun _ _ r => r.symm) ih
    | trans _ _ ih1 ih2 => exact ih1.trans ih2
  · intro within
    exact within (DevelopmentalAssociation.Connected bonds a)
      (fun _ _ joined related => joined.trans (connected_of_adjacent related)) (.refl a)

/-- **A component holding its root and closed on every remaining bond is the root's closure**
(`closure_iff_certified`). -/
theorem component_is_closure {count : Nat} {es : List Edge} {r : Nat}
    (hr : r ∈ component count es r) (hc : closed es (component count es r) = true) :
    ∀ v, v ∈ component count es r ↔ WithinClosure (adjacent es) r v :=
  closure_iff_certified.mpr
    ⟨hr, fun _ _ inside related => (connected_same_side hc (connected_of_adjacent related)).mp inside,
     fun g inside => (connected_iff_within es r g).mp (component_sound inside)⟩

/-- **`certificate_exact_split` from the core law.** -/
theorem certificate_exact_split_by_core {s : Growing} {e : Edge} (h : cutCertificate s e = true) :
    (∀ v, v ∈ component s.body.count (cutEdges s.body.bonds e) e.1 ↔
      DevelopmentalAssociation.Connected (cutEdges s.body.bonds e) e.1 v) ∧
    (∀ v, v ∈ component s.body.count (cutEdges s.body.bonds e) e.2 ↔
      DevelopmentalAssociation.Connected (cutEdges s.body.bonds e) e.2 v) ∧
    (∀ v < s.body.count,
      (v ∈ component s.body.count (cutEdges s.body.bonds e) e.1 ↔
       v ∉ component s.body.count (cutEdges s.body.bonds e) e.2)) := by
  have split := certificate_exact_split h
  simp only [cutCertificate, Bool.and_eq_true, List.contains_iff_mem] at h
  obtain ⟨⟨⟨⟨ha, hb⟩, ca⟩, cb⟩, _⟩ := h
  exact ⟨fun v => (component_is_closure ha ca v).trans (connected_iff_within _ _ _).symm,
    fun v => (component_is_closure hb cb v).trans (connected_iff_within _ _ _).symm, split.2.2⟩

/-- **A certified cut leaves its two ends apart** (`not_within_of_closed`): the second end is not
within the first end's closure under the remaining bonds. -/
theorem cut_separates {s : Growing} {e : Edge} (h : cutCertificate s e = true) :
    ¬ WithinClosure (adjacent (cutEdges s.body.bonds e)) e.1 e.2 := by
  have split := certificate_exact_split h
  simp only [cutCertificate, Bool.and_eq_true, List.contains_iff_mem] at h
  obtain ⟨⟨⟨⟨ha, hb⟩, ca⟩, _⟩, _⟩ := h
  have below : e.2 < s.body.count := List.mem_range.mp (List.mem_filter.mp hb).1
  have outside := fun inside => (split.2.2 e.2 below).mp inside hb
  exact not_within_of_closed
    (fun _ _ inside related => (connected_same_side ca (connected_of_adjacent related)).mp inside)
    ha outside

/-! ## Matched composition does not predict the cut return -/

theorem returns_differ : meanCutReturn chain ≠ meanCutReturn branched := by
  rw [uniform_cut_returns.1, uniform_cut_returns.2]
  decide +kernel

/-- **No function of the parent summary gives both mean cut returns** (`Readout.no_judge_of_merged`). -/
theorem no_parent_summary_predictor_by_core :
    ¬∃ f : (Nat × Nat × Nat × Nat) → Rat,
      meanCutReturn chain = f (parentSummary chain) ∧
      meanCutReturn branched = f (parentSummary branched) :=
  fun ⟨f, at_chain, at_branched⟩ =>
    Readout.no_judge_of_merged (family := [chain, branched]) (π := parentSummary) (f := meanCutReturn)
      (.head _) (.tail _ (.head _))
      (matched_parent_summaries.1.trans matched_parent_summaries.2.symm) returns_differ
      ⟨f, fun g mem => by
        cases mem with
        | head => exact at_chain.symm
        | tail _ later =>
          cases later with
          | head => exact at_branched.symm
          | tail _ none => exact nomatch none⟩

/-! ## Every bond grown by division is needed; a joined bond is bypassed where it crosses -/

/-- **The bonds read both ways are the listed links** of `Cuts.Links`. -/
theorem adjacent_iff_links : ∀ (bonds : List Edge) (a b : Nat),
    adjacent bonds a b ↔ Cuts.Links bonds a b
  | [], _, _ => ⟨fun h => h.elim (fun m => nomatch m) (fun m => nomatch m), fun h => nomatch h⟩
  | (x, y) :: rest, a, b => by
    have ih := adjacent_iff_links rest a b
    simp only [adjacent] at ih
    show ((a, b) ∈ (x, y) :: rest ∨ (b, a) ∈ (x, y) :: rest) ↔
      Cuts.Links rest a b ∨ ((a = x ∧ b = y) ∨ (a = y ∧ b = x))
    simp only [List.mem_cons, Prod.mk.injEq]
    constructor
    · rintro ((⟨rfl, rfl⟩ | m) | (⟨rfl, rfl⟩ | m))
      · exact Or.inr (Or.inl ⟨rfl, rfl⟩)
      · exact Or.inl (ih.mp (Or.inl m))
      · exact Or.inr (Or.inr ⟨rfl, rfl⟩)
      · exact Or.inl (ih.mp (Or.inr m))
    · rintro (l | (⟨rfl, rfl⟩ | ⟨rfl, rfl⟩))
      · rcases ih.mpr l with m | m
        · exact Or.inl (Or.inr m)
        · exact Or.inr (Or.inr m)
      · exact Or.inl (Or.inl ⟨rfl, rfl⟩)
      · exact Or.inr (Or.inl ⟨rfl, rfl⟩)

/-- Being connected by the bonds is lying within the closure under the listed links. -/
theorem connected_iff_links (bonds : List Edge) (a b : Nat) :
    DevelopmentalAssociation.Connected bonds a b ↔ WithinClosure (Cuts.Links bonds) a b :=
  (connected_iff_within bonds a b).trans (Cuts.within_congr (adjacent_iff_links bonds))

/-- The bonds grow by attachment, and every bond joins positions below the count. -/
def AttachedBelow (s : DevelopmentalAssociation.State) : Prop :=
  Cuts.Attaches s.bonds ∧ ∀ e ∈ s.bonds, e.1 < s.count ∧ e.2 < s.count

/-- **A division attaches the new position.** -/
theorem divide_attached {s t : DevelopmentalAssociation.State} {p : Nat} (grown : AttachedBelow s)
    (divided : DevelopmentalAssociation.divide s p = some t) : AttachedBelow t := by
  unfold DevelopmentalAssociation.divide at divided
  split at divided
  · rename_i enabled
    cases divided
    obtain ⟨attaches, below⟩ := grown
    have fresh : Cuts.Unlinked (Cuts.Links s.bonds) s.count := fun g => by
      constructor <;> intro linked <;>
        rcases (adjacent_iff_links _ _ _).mpr linked with m | m <;>
        have := below _ m <;> simp at this <;> omega
    by_cases retained : s.retains p = true
    · simp only [retained, if_true]
      refine ⟨.cons attaches fresh (by omega), ?_⟩
      intro e m
      dsimp only
      rcases List.mem_cons.mp m with rfl | m
      · exact ⟨by omega, by omega⟩
      · have := below e m; omega
    · simp only [retained]
      refine ⟨attaches, fun e m => ?_⟩
      dsimp only
      have := below e m; omega
  · cases divided

/-- **Growth by division keeps the bonds grown by attachment**, whatever the word. -/
theorem develop_attached : ∀ (ps : List Nat) {s : Growing}, AttachedBelow s.body →
    AttachedBelow (develop ps s).body
  | [], _, grown => grown
  | p :: ps, s, grown => by
    apply develop_attached ps
    show AttachedBelow (birth s p).body
    unfold birth
    split
    · exact grown
    · rename_i t divided
      exact divide_attached grown divided

theorem initial_attached : AttachedBelow initial.body :=
  ⟨.nil, fun _ m => nomatch m⟩

/-- Cutting a bond grown by attachment removes exactly that bond. -/
theorem cut_attached {newer older : List Edge} {p n : Nat}
    (grown : Cuts.Attaches (newer ++ (p, n) :: older)) :
    cutEdges (newer ++ (p, n) :: older) (p, n) = newer ++ older := by
  obtain ⟨notNewer, notOlder⟩ := grown.listed_once
  have keep : ∀ l : List Edge, ¬ (p, n) ∈ l → l.filter (fun f => f != (p, n)) = l := fun l absent =>
    List.filter_eq_self.mpr fun x m => by
      simp only [bne_iff_ne, ne_eq]
      intro same
      exact absent (same ▸ m)
  simp only [cutEdges, List.filter_append, List.filter_cons, bne_self_eq_false, Bool.false_eq_true,
    if_false]
  rw [keep newer notNewer, keep older notOlder]

/-- **Every bond of a body grown by division separates its ends when cut** (`Cuts.attached_link_separates`). -/
theorem bond_cut_separates {s : DevelopmentalAssociation.State} (grown : AttachedBelow s) {e : Edge}
    (listed : e ∈ s.bonds) :
    ¬ DevelopmentalAssociation.Connected (cutEdges s.bonds e) e.1 e.2 := by
  obtain ⟨newer, older, split⟩ := List.append_of_mem listed
  obtain ⟨p, n⟩ := e
  have attaches : Cuts.Attaches (newer ++ (p, n) :: older) := split ▸ grown.1
  rw [split, cut_attached attaches, connected_iff_links]
  exact Cuts.attached_link_separates attaches

/-- **Every bond of every body grown by division from one position is needed**: cutting it leaves
its ends apart, whatever the division word. -/
theorem every_grown_bond_separates (ps : List Nat) {e : Edge}
    (listed : e ∈ (develop ps initial).body.bonds) :
    ¬ DevelopmentalAssociation.Connected (cutEdges (develop ps initial).body.bonds e) e.1 e.2 :=
  bond_cut_separates (develop_attached ps initial_attached) listed

/-- **After one aggregation, cutting a grown bond changes no connection exactly where the aggregated
bond crosses it** (`Cuts.joined_cut_unchanged_iff`). -/
theorem aggregate_cut_unchanged_iff {s t : DevelopmentalAssociation.State} (grown : AttachedBelow s)
    {a b p n : Nat} (listed : (p, n) ∈ s.bonds) (other : (a, b) ≠ (p, n))
    (joined : DevelopmentalAssociation.aggregate s a b = some t) :
    (∀ f g, DevelopmentalAssociation.Connected t.bonds f g ↔
        DevelopmentalAssociation.Connected (cutEdges t.bonds (p, n)) f g) ↔
      (DevelopmentalAssociation.Connected (cutEdges s.bonds (p, n)) p a ∧
        DevelopmentalAssociation.Connected (cutEdges s.bonds (p, n)) b n) ∨
      (DevelopmentalAssociation.Connected (cutEdges s.bonds (p, n)) p b ∧
        DevelopmentalAssociation.Connected (cutEdges s.bonds (p, n)) a n) := by
  have bonds : t.bonds = (a, b) :: s.bonds := by
    unfold DevelopmentalAssociation.aggregate at joined
    split at joined
    · cases joined; rfl
    · cases joined
  obtain ⟨newer, older, split⟩ := List.append_of_mem listed
  have attaches : Cuts.Attaches (newer ++ (p, n) :: older) := split ▸ grown.1
  have cutT : cutEdges t.bonds (p, n) = (a, b) :: (newer ++ older) := by
    rw [bonds, split, cutEdges, List.filter_cons]
    simp only [bne_iff_ne, ne_eq, other, not_false_eq_true, if_true]
    rw [← cutEdges, cut_attached attaches]
  rw [cutT, bonds, split, cut_attached attaches]
  simp only [connected_iff_links]
  exact Cuts.joined_cut_unchanged_iff attaches

/-- **The reinforced chain's bypass is an instance**: cutting bond `(3,4)` after the join `(0,7)`
changes no connection, since the join's ends lie on the bond's two sides. -/
theorem reinforced_cut_unchanged : ∀ f g,
    DevelopmentalAssociation.Connected reinforced.body.bonds f g ↔
      DevelopmentalAssociation.Connected (cutEdges reinforced.body.bonds (3, 4)) f g :=
  (aggregate_cut_unchanged_iff (develop_attached chainWord initial_attached)
    (by decide +kernel) (by decide) reinforcement_is_actual).mpr
    (Or.inl ⟨component_sound (count := 8) (by decide +kernel),
      component_sound (count := 8) (by decide +kernel)⟩)

end Becoming.PreparationCorrespondence
