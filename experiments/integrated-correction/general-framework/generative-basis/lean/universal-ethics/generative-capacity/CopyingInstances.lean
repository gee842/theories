import Becoming.Copying
import CopyingCorrection

/-!
# Constructed copy machines as instances of the copying laws (periphery)

The four constructed copy machines (`RecurrentAssembly`, `StructuralCopying`,
`CopyingRegistration`, `CopyingCorrection`) use library membership, erasure and `simp`, so their
instances of the core's laws (`Becoming.Copying`, `Becoming.Gated`) are stated here rather than in
the pure core. Each machine's state is read as a copy in progress (`view`); one move of the
machine is one move of the core copy, so the general laws hold of every machine state, and the
old examples are instances.

* **Exact copying and release.** Copying a template strand reproduces its tokens exactly when
  the pool holds each token at least as often as the strand uses it and the support covers the
  local charges (`copy_cells_iff`); it is released exactly when the support also covers one
  more unit (`reproduce_iff`), for every pool. The old law of the support needed, with the
  template's own tokens in the pool, is the instance (`template_pool_reproduce_iff`).
* **One shared pool.** Reproducing strands in turn from one pool and support, every strand is
  released exactly when the pool supplies all their tokens together and the support covers
  all their charges and releases (`batch_all_released_iff`); exchanging adjacent strands keeps
  this (`batch_all_released_swap`).
* **Local charges.** The machine's charges are the core's local charges with first charge 1
  (`charge_eq`), so the ranking of the alternating and clustered strands
  (`local_ranking_from_law`) and the constraint on the mixed strand
  (`third_structure_from_law`) are instances of `cost_lt_iff` and `cost_midpoint`.
* **Chain growth and doubling rounds.** End attachment grows a chain by the alternating word
  exactly when the pool supplies that word and the support covers one unit per token
  (`grow_iff`); from the empty chain, the mature chain forms exactly when the pool holds at
  least four of each kind and at least eight units are free (`mature_forms_iff`). `n` rounds from `k` mature
  chains with the needed material reach `k * 2 ^ n` mature chains exactly when the support
  covers `9 * required n k` (`rounds_mature_iff`), that is, exactly when the core's doubling
  process with draw 9 runs `n` rounds (`rounds_follow_doubling`).
* **Reading through contacts.** For every registration state, operating as many copy moves as
  a word has tokens extends the product by that word exactly when each site reads the word's
  token through the actual contacts, the pool supplies the word and the support covers its
  charges (`operate_copies_iff`); complete registration is the instance
  (`registered_copy_cells`). Every course keeps the built product as a prefix
  (`product_extends_along`); only copy moves change the product (`product_gated`,
  `contact_course_keeps_product`), and every course keeps the totals of connectors, material
  and support (`totals_along`).
* **Inspection.** For every correction state, inspecting a site never increases the defects
  for any product exactly when the reference agrees with the template there
  (`inspect_le_iff_instance`); a scan of such sites never increases them (`scan_le_from_law`),
  of which the old faithful-scan theorem is the instance (`scan_faithful_instance`); the
  single-site criterion is an instance (`matches_reference_from_law`), and the wrong reference
  of the old witness is unfaithful at the damaged site (`wrong_reference_unfaithful`).
-/

namespace Becoming.CopyingInstances

open Generative

/-! ## Lists of tokens -/

theorem mem_iff_pos (x : Bool) : ∀ l : List Bool, x ∈ l ↔ 0 < Copying.countOf x l
  | [] => by simp [Copying.countOf]
  | y :: ys => by
    have ih := mem_iff_pos x ys
    by_cases h : y = x
    · subst h
      simp [Copying.countOf]
    · have h' : x ≠ y := fun e => h e.symm
      simp [Copying.countOf, h, h', ih]

theorem erase_eq (x : Bool) : ∀ l : List Bool, l.erase x = Copying.remove x l
  | [] => rfl
  | y :: ys => by
    by_cases h : y = x
    · subst h
      simp [Copying.remove]
    · simp [Copying.remove, h, erase_eq x ys]

theorem nth_eq {β : Type} : ∀ (l : List β) (i : Nat), Copying.nth l i = l[i]?
  | [], _ => rfl
  | _ :: _, 0 => rfl
  | _ :: xs, i + 1 => by simp [Copying.nth, nth_eq xs i]

theorem setAt_eq {β : Type} : ∀ (l : List β) (i : Nat) (x : β), Copying.setAt l i x = l.set i x
  | [], _, _ => rfl
  | _ :: _, 0, _ => rfl
  | y :: xs, i + 1, x => by simp [Copying.setAt, setAt_eq xs i x]

theorem final_eq {β : Type} : ∀ l : List β, Copying.final l = l.getLast?
  | [] => rfl
  | [_] => rfl
  | _ :: y :: rest => by simp [Copying.final, final_eq (y :: rest)]

theorem supplies_prefix (w tail : List Bool) : Copying.Supplies w (w ++ tail) := fun a => by
  rw [Copying.countOf_append]
  exact Nat.le_add_right _ _

/-! ## Structural copying -/

section Structural

open RecurrentAssembly

/-- A machine copy read as a core copy in progress. -/
def view (w : StructuralCopying.CopyState) : Copying.Scan Bool :=
  ⟨w.previous, w.pending, w.built.cells, w.supply.pool, w.supply.free, w.supply.spent⟩

/-- The machine's charges are the core's local charges with first charge 1. -/
theorem charge_eq (law : StructuralCopying.Law) :
    StructuralCopying.charge law = Copying.pairCharge 1 law.equal law.unequal := by
  funext p x
  cases p <;> rfl

theorem cost_eq (law : StructuralCopying.Law) : ∀ (p : Option Bool) (w : List Bool),
    StructuralCopying.cost law p w = Copying.cost (StructuralCopying.charge law) p w
  | _, [] => rfl
  | p, x :: xs => congrArg (StructuralCopying.charge law p x + ·) (cost_eq law (some x) xs)

theorem cost_pair_eq (law : StructuralCopying.Law) (p : Option Bool) (w : List Bool) :
    StructuralCopying.cost law p w = Copying.cost (Copying.pairCharge 1 law.equal law.unequal) p w := by
  rw [cost_eq, charge_eq]

/-- One machine move is one core move. -/
theorem view_tick (law : StructuralCopying.Law) (w : StructuralCopying.CopyState) :
    view (StructuralCopying.tick law w) = Copying.tick (StructuralCopying.charge law) (view w) := by
  rcases w with ⟨prev, pending, built, ⟨pool, free, spent⟩⟩
  cases pending with
  | nil => rfl
  | cons x xs =>
    show view (if x ∈ pool ∧ StructuralCopying.charge law prev x ≤ free then _ else _) =
      if 0 < Copying.countOf x pool ∧ StructuralCopying.charge law prev x ≤ free then _ else _
    by_cases hc : x ∈ pool ∧ StructuralCopying.charge law prev x ≤ free
    · rw [if_pos hc, if_pos ⟨(mem_iff_pos x pool).mp hc.1, hc.2⟩]
      simp [view, StructuralCopying.extend, erase_eq]
    · rw [if_neg hc, if_neg fun h => hc ⟨(mem_iff_pos x pool).mpr h.1, h.2⟩]

theorem view_steps (law : StructuralCopying.Law) : ∀ (n : Nat) (w : StructuralCopying.CopyState),
    view (StructuralCopying.steps law n w) = Copying.steps (StructuralCopying.charge law) n (view w)
  | 0, _ => rfl
  | n + 1, w => (view_steps law n _).trans
      (congrArg (Copying.steps (StructuralCopying.charge law) n) (view_tick law w))

theorem view_copy (law : StructuralCopying.Law) (parent : Strand)
    (hp : parent.bonds = path parent.cells.length) (hn : parent.cells ≠ []) (r : Supply) :
    view (StructuralCopying.copy law parent r) =
      Copying.steps (StructuralCopying.charge law) parent.cells.length
        ⟨none, parent.cells, [], r.pool, r.free, r.spent⟩ := by
  simp only [StructuralCopying.copy, if_pos (And.intro hp hn)]
  exact view_steps law _ _

/-- **Exact copying.** Copying a template strand reproduces its tokens exactly when the pool
supplies them and the support covers the local charges, for every pool (from
`Copying.built_iff`). -/
theorem copy_cells_iff (law : StructuralCopying.Law) (parent : Strand)
    (hp : parent.bonds = path parent.cells.length) (hn : parent.cells ≠ []) (r : Supply) :
    (StructuralCopying.copy law parent r).built.cells = parent.cells ↔
      Copying.Supplies parent.cells r.pool ∧ StructuralCopying.cost law none parent.cells ≤ r.free := by
  have h := Copying.built_iff (StructuralCopying.charge law) none [] parent.cells r.pool r.free r.spent
  rw [← view_copy law parent hp hn r, ← cost_eq] at h
  exact h

theorem copy_tracks (law : StructuralCopying.Law) (parent : Strand)
    (hp : parent.bonds = path parent.cells.length) (hn : parent.cells ≠ []) (r : Supply) :
    (StructuralCopying.copy law parent r).built.cells ++ (StructuralCopying.copy law parent r).pending =
      parent.cells := by
  have h := (StructuralCopying.steps_invariants law parent.cells.length
    (StructuralCopying.start parent r)).2.2
  simp only [StructuralCopying.copy, if_pos (And.intro hp hn)]
  simpa [StructuralCopying.start] using h

/-- **Exact reproduction.** A template strand is copied and released exactly when the pool
supplies its tokens and the support covers its charges and the release, for every pool (from
`Copying.releases_iff`). -/
theorem reproduce_iff (law : StructuralCopying.Law) (parent : Strand)
    (hp : parent.bonds = path parent.cells.length) (hn : parent.cells ≠ []) (r : Supply) :
    (StructuralCopying.reproduce law parent r).1 = true ↔
      Copying.Supplies parent.cells r.pool ∧ StructuralCopying.cost law none parent.cells + 1 ≤ r.free := by
  have h := Copying.releases_iff (StructuralCopying.charge law) 1 none [] parent.cells r.pool r.free
    r.spent
  rw [← view_copy law parent hp hn r, ← cost_eq] at h
  unfold StructuralCopying.reproduce StructuralCopying.release
  constructor
  · intro hr
    split at hr
    · rename_i c
      exact h.mp ⟨c.1, c.2.2⟩
    · exact nomatch hr
  · intro hs
    have ⟨done, left⟩ := h.mpr hs
    have cells := (copy_cells_iff law parent hp hn r).mpr
      ⟨hs.1, Nat.le_trans (Nat.le_add_right _ 1) hs.2⟩
    have filled : (StructuralCopying.copy law parent r).built.cells ≠ [] := by
      rw [cells]
      exact hn
    rw [if_pos ⟨done, filled, left⟩]

/-- The old law of the support needed is the instance with the template's own tokens in the
pool. -/
theorem template_pool_reproduce_iff (law : StructuralCopying.Law) (parent : Strand)
    (hp : parent.bonds = path parent.cells.length) (hn : parent.cells ≠ [])
    (tail : List Bool) (free spent : Nat) :
    (StructuralCopying.reproduce law parent ⟨parent.cells ++ tail, free, spent⟩).1 = true ↔
      StructuralCopying.cost law none parent.cells + 1 ≤ free :=
  (reproduce_iff law parent hp hn _).trans
    ⟨fun h => h.2, fun h => ⟨supplies_prefix _ _, h⟩⟩

theorem release_view (w : StructuralCopying.CopyState) (filled : w.pending = [] → w.built.cells ≠ []) :
    (StructuralCopying.release w).1 = Copying.released 1 (view w) ∧
    (StructuralCopying.release w).2.supply =
      ⟨w.supply.pool, cond (Copying.released 1 (view w)) (w.supply.free - 1) w.supply.free,
        cond (Copying.released 1 (view w)) (w.supply.spent + 1) w.supply.spent⟩ := by
  rcases w with ⟨prev, pending, built, ⟨pool, free, spent⟩⟩
  cases pending with
  | nil =>
    have ne := filled rfl
    by_cases hf : 0 < free
    · have h1 : 1 ≤ free := hf
      simp [StructuralCopying.release, Copying.released, view, ne, hf, h1]
    · have h1 : ¬ 1 ≤ free := hf
      simp [StructuralCopying.release, Copying.released, view, ne, hf, h1]
  | cons x xs => simp [StructuralCopying.release, Copying.released, view]

/-- The core copy a machine copy of `p` from `r` runs. -/
def copied (law : StructuralCopying.Law) (p : Strand) (r : Supply) : Copying.Scan Bool :=
  Copying.steps (StructuralCopying.charge law) p.cells.length ⟨none, p.cells, [], r.pool, r.free, r.spent⟩

/-- Reproducing strands in turn from one shared pool is the core's batch, flag for flag and
supply for supply. -/
theorem batch_view (law : StructuralCopying.Law) : ∀ (ps : List Strand) (r : Supply),
    (∀ p, p ∈ ps → p.bonds = path p.cells.length ∧ p.cells ≠ []) →
      (StructuralCopying.batch law ps r).1.map Prod.fst =
          (Copying.batch (StructuralCopying.charge law) 1 (ps.map Strand.cells) r.pool r.free r.spent).1 ∧
        (StructuralCopying.batch law ps r).2 =
          ⟨(Copying.batch (StructuralCopying.charge law) 1 (ps.map Strand.cells) r.pool r.free r.spent).2.1,
           (Copying.batch (StructuralCopying.charge law) 1 (ps.map Strand.cells) r.pool r.free r.spent).2.2.1,
           (Copying.batch (StructuralCopying.charge law) 1 (ps.map Strand.cells) r.pool r.free r.spent).2.2.2⟩
  | [], _, _ => ⟨rfl, rfl⟩
  | p :: ps, r, shaped => by
    have ⟨hp, hn⟩ := shaped p (.head _)
    have filled : (StructuralCopying.copy law p r).pending = [] →
        (StructuralCopying.copy law p r).built.cells ≠ [] := fun done => by
      have tr := copy_tracks law p hp hn r
      rw [done, List.append_nil] at tr
      rw [tr]
      exact hn
    have ⟨flag, supply⟩ := release_view (StructuralCopying.copy law p r) filled
    have e : view (StructuralCopying.copy law p r) = copied law p r := view_copy law p hp hn r
    have flag' : (StructuralCopying.reproduce law p r).1 = Copying.released 1 (copied law p r) := by
      rw [← e]
      exact flag
    have supply' : (StructuralCopying.reproduce law p r).2.supply =
        ⟨(copied law p r).pool, cond (Copying.released 1 (copied law p r)) ((copied law p r).free - 1)
          (copied law p r).free,
         cond (Copying.released 1 (copied law p r)) ((copied law p r).spent + 1)
          (copied law p r).spent⟩ := by
      rw [← e]
      exact supply
    have ih := batch_view law ps (StructuralCopying.reproduce law p r).2.supply
      fun q m => shaped q (.tail p m)
    rw [supply'] at ih
    refine ⟨?_, ?_⟩
    · show (StructuralCopying.reproduce law p r).1 ::
          List.map Prod.fst (StructuralCopying.batch law ps (StructuralCopying.reproduce law p r).2.supply).1 =
        Copying.released 1 (copied law p r) ::
          (Copying.batch (StructuralCopying.charge law) 1 (ps.map Strand.cells) (copied law p r).pool
            (cond (Copying.released 1 (copied law p r)) ((copied law p r).free - 1) (copied law p r).free)
            (cond (Copying.released 1 (copied law p r)) ((copied law p r).spent + 1)
              (copied law p r).spent)).1
      rw [flag', supply']
      exact congrArg _ ih.1
    · show (StructuralCopying.batch law ps (StructuralCopying.reproduce law p r).2.supply).2 =
        ⟨(Copying.batch (StructuralCopying.charge law) 1 (ps.map Strand.cells) (copied law p r).pool
            (cond (Copying.released 1 (copied law p r)) ((copied law p r).free - 1) (copied law p r).free)
            (cond (Copying.released 1 (copied law p r)) ((copied law p r).spent + 1)
              (copied law p r).spent)).2.1,
         (Copying.batch (StructuralCopying.charge law) 1 (ps.map Strand.cells) (copied law p r).pool
            (cond (Copying.released 1 (copied law p r)) ((copied law p r).free - 1) (copied law p r).free)
            (cond (Copying.released 1 (copied law p r)) ((copied law p r).spent + 1)
              (copied law p r).spent)).2.2.1,
         (Copying.batch (StructuralCopying.charge law) 1 (ps.map Strand.cells) (copied law p r).pool
            (cond (Copying.released 1 (copied law p r)) ((copied law p r).free - 1) (copied law p r).free)
            (cond (Copying.released 1 (copied law p r)) ((copied law p r).spent + 1)
              (copied law p r).spent)).2.2.2⟩
      rw [supply']
      exact ih.2

/-- **One shared pool.** Every strand of a batch is released exactly when the pool supplies all
their tokens together and the support covers all their charges and releases. -/
theorem batch_all_released_iff (law : StructuralCopying.Law) (ps : List Strand) (r : Supply)
    (shaped : ∀ p, p ∈ ps → p.bonds = path p.cells.length ∧ p.cells ≠ []) :
    Copying.Every ((StructuralCopying.batch law ps r).1.map Prod.fst) ↔
      Copying.Supplies (Copying.joinAll (ps.map Strand.cells)) r.pool ∧
        Copying.totalOf (fun w => StructuralCopying.cost law none w + 1) (ps.map Strand.cells) ≤
          r.free := by
  rw [(batch_view law ps r shaped).1]
  have fe : (fun w => StructuralCopying.cost law none w + 1) =
      (fun w => Copying.cost (StructuralCopying.charge law) none w + 1) :=
    funext fun w => congrArg (· + 1) (cost_eq law none w)
  rw [fe]
  exact Copying.batch_all_iff (StructuralCopying.charge law) 1 _ r.pool r.free r.spent

/-- Exchanging two adjacent strands of a batch keeps whether all are released. -/
theorem batch_all_released_swap (law : StructuralCopying.Law) (pre post : List Strand)
    (p q : Strand) (r : Supply)
    (shaped : ∀ s, s ∈ pre ++ p :: q :: post → s.bonds = path s.cells.length ∧ s.cells ≠ []) :
    Copying.Every ((StructuralCopying.batch law (pre ++ p :: q :: post) r).1.map Prod.fst) ↔
      Copying.Every ((StructuralCopying.batch law (pre ++ q :: p :: post) r).1.map Prod.fst) := by
  have shaped' : ∀ s, s ∈ pre ++ q :: p :: post → s.bonds = path s.cells.length ∧ s.cells ≠ [] :=
    fun s m => shaped s (by
      simp only [List.mem_append, List.mem_cons] at m ⊢
      rcases m with m | m | m | m
      · exact Or.inl m
      · exact Or.inr (Or.inr (Or.inl m))
      · exact Or.inr (Or.inl m)
      · exact Or.inr (Or.inr (Or.inr m)))
  rw [(batch_view law _ r shaped).1, (batch_view law _ r shaped').1]
  simp only [List.map_append, List.map_cons]
  exact Copying.batch_all_swap (StructuralCopying.charge law) 1 _ _ _ _ r.pool r.free r.spent

/-- **Local ranking** of the alternating and clustered strands, an instance of
`Copying.cost_lt_iff`. -/
theorem local_ranking_from_law (law : StructuralCopying.Law) :
    StructuralCopying.cost law none StructuralCopying.alternating.cells <
        StructuralCopying.cost law none StructuralCopying.clustered.cells ↔
      law.unequal < law.equal := by
  rw [cost_pair_eq, cost_pair_eq]
  exact Copying.cost_lt_iff 1 law.equal law.unequal (x := false) (y := false)
    (l := [false, true, true]) (m := [true, false, true]) rfl (d := 2) rfl (by decide)

/-- **The third arrangement**, an instance of `Copying.cost_midpoint`. -/
theorem third_structure_from_law (law : StructuralCopying.Law) :
    2 * (StructuralCopying.cost law none StructuralCopying.mixed.cells + 1) =
      (StructuralCopying.cost law none StructuralCopying.alternating.cells + 1) +
        (StructuralCopying.cost law none StructuralCopying.clustered.cells + 1) := by
  have h := Copying.cost_midpoint 1 law.equal law.unequal (x := false) (y := false) (z := false)
    (l := [true, false, true]) (m := [true, true, false]) (k := [false, true, true]) rfl rfl rfl
  rw [cost_pair_eq, cost_pair_eq, cost_pair_eq]
  show 2 * (Copying.cost (Copying.pairCharge 1 law.equal law.unequal) none
        (false :: [true, true, false]) + 1) =
      (Copying.cost (Copying.pairCharge 1 law.equal law.unequal) none
        (false :: [true, false, true]) + 1) +
      (Copying.cost (Copying.pairCharge 1 law.equal law.unequal) none
        (false :: [false, true, true]) + 1)
  omega

end Structural

/-! ## Chain growth and doubling rounds -/

section Assembly

open RecurrentAssembly

/-- The alternating word of `n` tokens beginning with `b`. -/
def alternatingFrom : Bool → Nat → List Bool
  | _, 0 => []
  | b, n + 1 => b :: alternatingFrom (!b) n

theorem length_alternatingFrom : ∀ (b : Bool) (n : Nat), (alternatingFrom b n).length = n
  | _, 0 => rfl
  | b, n + 1 => congrArg (· + 1) (length_alternatingFrom (!b) n)

/-- Every attachment draws one unit. -/
def unit : Option Bool → Bool → Nat := fun _ _ => 1

theorem cost_unit : ∀ (p : Option Bool) (w : List Bool), Copying.cost unit p w = w.length
  | _, [] => rfl
  | _, _ :: xs => (Nat.add_comm 1 _).trans (congrArg (· + 1) (cost_unit _ xs))

theorem grow_fixed (s : Strand) (r : Supply) (fixed : attach s r = (s, r)) :
    ∀ n, grow n s r = (s, r)
  | 0 => rfl
  | n + 1 => by
    show grow n (attach s r).1 (attach s r).2 = (s, r)
    rw [fixed]
    exact grow_fixed s r fixed n

/-- The product and supply of a growing chain. -/
def ofGrow (t : Strand × Supply) : List Bool × List Bool × Nat × Nat :=
  (t.1.cells, t.2.pool, t.2.free, t.2.spent)

/-- The product and supply of a core copy. -/
def ofScan (c : Copying.Scan Bool) : List Bool × List Bool × Nat × Nat :=
  (c.built, c.pool, c.free, c.spent)

/-- End attachment is the core copy of the alternating word with unit charges. -/
theorem grow_view : ∀ (n : Nat) (s : Strand) (r : Supply) (prev : Option Bool),
    s.cells.length + n ≤ 8 →
      ofGrow (grow n s r) =
        ofScan (Copying.steps unit n ⟨prev, alternatingFrom (wanted s) n, s.cells, r.pool, r.free, r.spent⟩)
  | 0, _, _, _, _ => rfl
  | n + 1, s, r, prev, room => by
    have short : s.cells.length < 8 := by omega
    show ofGrow (grow n (attach s r).1 (attach s r).2) =
        ofScan (Copying.steps unit n (Copying.tick unit
          ⟨prev, wanted s :: alternatingFrom (!wanted s) n, s.cells, r.pool, r.free, r.spent⟩))
    by_cases go : wanted s ∈ r.pool ∧ 0 < r.free
    · have tk : Copying.tick unit
          ⟨prev, wanted s :: alternatingFrom (!wanted s) n, s.cells, r.pool, r.free, r.spent⟩ =
          ⟨some (wanted s), alternatingFrom (!wanted s) n, s.cells ++ [wanted s],
            Copying.remove (wanted s) r.pool, r.free - 1, r.spent + 1⟩ :=
        if_pos ⟨(mem_iff_pos _ _).mp go.1, go.2⟩
      have cells : (attach s r).1.cells = s.cells ++ [wanted s] := by
        simp [attach, short, go]
      have supply : (attach s r).2 = ⟨Copying.remove (wanted s) r.pool, r.free - 1, r.spent + 1⟩ := by
        simp [attach, short, go, erase_eq]
      have next : wanted (attach s r).1 = !wanted s := by
        simp [wanted, cells]
      have core_eq : (⟨some (wanted s), alternatingFrom (wanted (attach s r).1) n, (attach s r).1.cells,
          (attach s r).2.pool, (attach s r).2.free, (attach s r).2.spent⟩ : Copying.Scan Bool) =
          ⟨some (wanted s), alternatingFrom (!wanted s) n, s.cells ++ [wanted s],
            Copying.remove (wanted s) r.pool, r.free - 1, r.spent + 1⟩ := by
        rw [next, cells, supply]
      rw [tk, ← core_eq]
      exact grow_view n (attach s r).1 (attach s r).2 (some (wanted s))
        (by rw [cells, List.length_append]; simp; omega)
    · have att : attach s r = (s, r) := by
        simp only [attach]
        rw [if_neg fun h => go ⟨h.2.1, h.2.2⟩]
      have tk : Copying.tick unit
          ⟨prev, wanted s :: alternatingFrom (!wanted s) n, s.cells, r.pool, r.free, r.spent⟩ =
          ⟨prev, wanted s :: alternatingFrom (!wanted s) n, s.cells, r.pool, r.free, r.spent⟩ :=
        if_neg fun h => go ⟨(mem_iff_pos _ _).mpr h.1, h.2⟩
      rw [att, tk, grow_fixed s r att n, Copying.steps_fixed unit tk n]
      rfl

/-- **Chain growth.** Within the size limit, end attachment grows a chain by the alternating word
exactly when the pool supplies that word and the support covers one unit per token. -/
theorem grow_iff (n : Nat) (s : Strand) (r : Supply) (room : s.cells.length + n ≤ 8) :
    (grow n s r).1.cells = s.cells ++ alternatingFrom (wanted s) n ↔
      Copying.Supplies (alternatingFrom (wanted s) n) r.pool ∧ n ≤ r.free := by
  rw [show (grow n s r).1.cells = _ from congrArg Prod.fst (grow_view n s r none room)]
  have h := Copying.built_iff unit none s.cells (alternatingFrom (wanted s) n) r.pool r.free r.spent
  rw [cost_unit, length_alternatingFrom] at h
  exact h

/-- From the empty chain, the mature chain forms exactly when the pool holds at least four of
each kind and at least eight units are free. -/
theorem mature_forms_iff (r : Supply) :
    (grow 8 ⟨[], []⟩ r).1.cells = mature.cells ↔
      Copying.Supplies mature.cells r.pool ∧ 8 ≤ r.free :=
  grow_iff 8 ⟨[], []⟩ r (by decide)

theorem required_eq : ∀ n k : Nat, Copying.required n k = RecurrentAssembly.required n k
  | 0, _ => rfl
  | n + 1, k => congrArg (k + ·) (required_eq n (2 * k))

theorem attach_spent (s : Strand) (r : Supply) :
    (attach s r).2.spent + s.cells.length = r.spent + (attach s r).1.cells.length := by
  unfold attach
  split <;> simp <;> omega

theorem grow_spent : ∀ (n : Nat) (s : Strand) (r : Supply),
    (grow n s r).2.spent + s.cells.length = r.spent + (grow n s r).1.cells.length
  | 0, _, _ => rfl
  | n + 1, s, r => by
    have a := attach_spent s r
    have g := grow_spent n (attach s r).1 (attach s r).2
    show (grow n (attach s r).1 (attach s r).2).2.spent + s.cells.length =
      r.spent + (grow n (attach s r).1 (attach s r).2).1.cells.length
    omega

/-- Each attachment and each cleavage draws one unit: support spent grows with size plus
number of chains. -/
theorem reproduce_spent (s : Strand) (r : Supply) :
    (reproduce s r).2.spent + s.cells.length + 1 =
      r.spent + size (reproduce s r).1 + (reproduce s r).1.length := by
  unfold reproduce
  split
  · rename_i h
    have ha := grow_spent 4 (fragment s 0 4) ⟨r.pool, r.free - 1, r.spent + 1⟩
    have hb := grow_spent 4 (fragment s 4 4) (grow 4 (fragment s 0 4) ⟨r.pool, r.free - 1, r.spent + 1⟩).2
    simp only [size, fragment, List.drop_zero, List.length_take, List.length_drop, h.1] at *
    simp only [List.length_cons, List.length_nil]
    omega
  · simp [size]

theorem generation_spent : ∀ (ss : List Strand) (r : Supply),
    (generation ss r).2.spent + size ss + ss.length =
      r.spent + size (generation ss r).1 + (generation ss r).1.length
  | [], _ => rfl
  | s :: ss, r => by
    have h := reproduce_spent s r
    have hi := generation_spent ss (reproduce s r).2
    simp only [generation, size_append, size, List.length_append, List.length_cons]
    omega

theorem rounds_spent : ∀ (n : Nat) (ss : List Strand) (r : Supply),
    (rounds n ss r).2.spent + size ss + ss.length =
      r.spent + size (rounds n ss r).1 + (rounds n ss r).1.length
  | 0, _, _ => rfl
  | n + 1, ss, r => by
    have h := generation_spent ss r
    have hi := rounds_spent n (generation ss r).1 (generation ss r).2
    show (rounds n (generation ss r).1 (generation ss r).2).2.spent + size ss + ss.length =
      r.spent + size (rounds n (generation ss r).1 (generation ss r).2).1 +
        (rounds n (generation ss r).1 (generation ss r).2).1.length
    omega

/-- **Doubling rounds.** From `k` mature chains with the material for `n` rounds, the rounds
reach `k * 2 ^ n` mature chains exactly when the support covers `9 * required n k`. -/
theorem rounds_mature_iff (n k : Nat) (tail : List Bool) (free spent : Nat) :
    (rounds n (List.replicate k mature) ⟨blocks (RecurrentAssembly.required n k) ++ tail, free, spent⟩).1 =
        List.replicate (k * 2 ^ n) mature ↔
      9 * RecurrentAssembly.required n k ≤ free := by
  constructor
  · intro h
    have hs := rounds_spent n (List.replicate k mature)
      ⟨blocks (RecurrentAssembly.required n k) ++ tail, free, spent⟩
    have ha := (rounds_accounts n (List.replicate k mature)
      ⟨blocks (RecurrentAssembly.required n k) ++ tail, free, spent⟩).2
    rw [h, size_replicate, size_replicate, List.length_replicate, List.length_replicate] at hs
    have g := required_as_growth n k
    dsimp only at ha hs
    revert hs ha g
    generalize (rounds n (List.replicate k mature)
      ⟨blocks (RecurrentAssembly.required n k) ++ tail, free, spent⟩).2 = r'
    generalize k * 2 ^ n = K
    generalize RecurrentAssembly.required n k = R
    intro hs ha g
    omega
  · intro h
    have e := supported_rounds n k tail (free - 9 * RecurrentAssembly.required n k) spent
    rw [Nat.sub_add_cancel h] at e
    rw [e]

/-- **The rounds follow the core's doubling.** The machine reaches `k * 2 ^ n` mature chains
exactly when the doubling process with draw 9 runs `n` rounds from `k` units and the free
support. -/
theorem rounds_follow_doubling (n k : Nat) (tail : List Bool) (free spent : Nat) :
    (rounds n (List.replicate k mature) ⟨blocks (RecurrentAssembly.required n k) ++ tail, free, spent⟩).1 =
        List.replicate (k * 2 ^ n) mature ↔
      ∃ t, Trace (Copying.doubling 9) (k, free) (Copying.rounds n) t :=
  (rounds_mature_iff n k tail free spent).trans
    ⟨fun h => ⟨_, Copying.doubling_runs 9 n k free (by rw [required_eq]; exact h)⟩,
     fun ⟨t, path⟩ => by
      have h := ((Copying.doubling_iff 9 n k free t).mp path).1
      rw [required_eq] at h
      exact h⟩

end Assembly

/-! ## Reading through contacts -/

section Registration

open RecurrentAssembly

theorem tick_template (law : StructuralCopying.Law) (s : CopyingRegistration.State) :
    (CopyingRegistration.tick law s).template = s.template := by
  unfold CopyingRegistration.tick
  split
  · dsimp only
    split <;> rfl
  · rfl

theorem readAt_tick (law : StructuralCopying.Law) (s : CopyingRegistration.State) :
    CopyingRegistration.readAt (CopyingRegistration.tick law s) = CopyingRegistration.readAt s := by
  funext i
  unfold CopyingRegistration.readAt
  rw [(CopyingRegistration.tick_accounts law s).1, tick_template]

/-- One copy move of the registration machine is one move of the core copy reading through the
actual contacts. -/
theorem tick_work_view (law : StructuralCopying.Law) (s : CopyingRegistration.State) :
    view (CopyingRegistration.tick law s).work =
      Copying.readTick (StructuralCopying.charge law) (CopyingRegistration.readAt s) (view s.work) := by
  rcases s with ⟨template, ⟨prev, pending, built, ⟨pool, free, spent⟩⟩, contacts, spare⟩
  show view (CopyingRegistration.tick law ⟨template, ⟨prev, pending, built, ⟨pool, free, spent⟩⟩,
      contacts, spare⟩).work =
    Copying.readStep (StructuralCopying.charge law) ⟨prev, pending, built.cells, pool, free, spent⟩
      (CopyingRegistration.readAt ⟨template, ⟨prev, pending, built, ⟨pool, free, spent⟩⟩,
        contacts, spare⟩ built.cells.length)
  unfold CopyingRegistration.tick
  generalize CopyingRegistration.readAt _ built.cells.length = o
  cases pending with
  | nil => cases o <;> rfl
  | cons p xs =>
    cases o with
    | none => rfl
    | some x =>
      show view (if x ∈ pool ∧ StructuralCopying.charge law prev x ≤ free then
          (_ : CopyingRegistration.State) else _).work =
        if 0 < Copying.countOf x pool ∧ StructuralCopying.charge law prev x ≤ free then
          (_ : Copying.Scan Bool) else _
      by_cases hc : x ∈ pool ∧ StructuralCopying.charge law prev x ≤ free
      · rw [if_pos hc, if_pos ⟨(mem_iff_pos x pool).mp hc.1, hc.2⟩]
        simp [view, StructuralCopying.extend, erase_eq]
      · rw [if_neg hc, if_neg fun h => hc ⟨(mem_iff_pos x pool).mpr h.1, h.2⟩]
        rfl

theorem operate_view (law : StructuralCopying.Law) : ∀ (n : Nat) (s : CopyingRegistration.State),
    view (CopyingRegistration.operate law n s).work =
      Copying.readSteps (StructuralCopying.charge law) (CopyingRegistration.readAt s) n (view s.work)
  | 0, _ => rfl
  | n + 1, s => by
    show view (CopyingRegistration.operate law n (CopyingRegistration.tick law s)).work =
      Copying.readSteps (StructuralCopying.charge law) (CopyingRegistration.readAt s) n
        (Copying.readTick (StructuralCopying.charge law) (CopyingRegistration.readAt s) (view s.work))
    rw [operate_view law n (CopyingRegistration.tick law s), readAt_tick, tick_work_view]

/-- **Reading through contacts.** For every registration state, as many copy moves as a word has
tokens extend the product by that word exactly when each site reads the word's token through
the actual contacts, the pool supplies the word and the support covers its charges (from
`Copying.reading_iff`). -/
theorem operate_copies_iff (law : StructuralCopying.Law) (s : CopyingRegistration.State)
    (word : List Bool) (len : s.work.pending.length = word.length) :
    (CopyingRegistration.operate law word.length s).work.built.cells = s.work.built.cells ++ word ↔
      Copying.Reads (CopyingRegistration.readAt s) s.work.built.cells.length word ∧
        Copying.Supplies word s.work.supply.pool ∧
        StructuralCopying.cost law s.work.previous word ≤ s.work.supply.free := by
  have h := Copying.reading_iff (StructuralCopying.charge law) (CopyingRegistration.readAt s) word
    s.work.pending s.work.previous s.work.built.cells s.work.supply.pool s.work.supply.free
    s.work.supply.spent len
  rw [← cost_eq] at h
  have h' : (view (CopyingRegistration.operate law word.length s).work).built =
      s.work.built.cells ++ word ↔
        Copying.Reads (CopyingRegistration.readAt s) s.work.built.cells.length word ∧
          Copying.Supplies word s.work.supply.pool ∧
          StructuralCopying.cost law s.work.previous word ≤ s.work.supply.free := by
    rw [operate_view]
    exact h
  exact h'

theorem reads_of_getElem (read : Nat → Option Bool) : ∀ (word : List Bool) (k : Nat),
    (∀ i, i < word.length → read (k + i) = word[i]?) → Copying.Reads read k word
  | [], _, _ => trivial
  | x :: xs, k, h =>
    ⟨by simpa using h 0 (by simp),
     reads_of_getElem read xs (k + 1) fun i hi => by
      have e : k + 1 + i = k + (i + 1) := by omega
      rw [e]
      simpa using h (i + 1) (by simp; omega)⟩

/-- Complete registration is the instance: the product is the template's tokens, for every
template (the old inheritance theorem adds the template's bonds). -/
theorem registered_copy_cells (law : StructuralCopying.Law) (p : Strand) (tail : List Bool)
    (free spent : Nat) (contacts : List (Nat × Nat)) (spare : Nat)
    (hreg : CopyingRegistration.Registered ⟨p, StructuralCopying.start p
      ⟨p.cells ++ tail, free + StructuralCopying.cost law none p.cells, spent⟩, contacts, spare⟩) :
    (CopyingRegistration.operate law p.cells.length ⟨p, StructuralCopying.start p
      ⟨p.cells ++ tail, free + StructuralCopying.cost law none p.cells, spent⟩, contacts, spare⟩).work.built.cells =
      p.cells :=
  (operate_copies_iff law _ p.cells rfl).mpr
    ⟨reads_of_getElem _ p.cells 0 fun i hi => by rw [Nat.zero_add]; exact hreg i hi,
     supplies_prefix _ _, Nat.le_add_left _ _⟩

theorem product_extends (law : StructuralCopying.Law) :
    Copying.Extends (CopyingRegistration.process law) (fun s => s.work.built.cells) :=
  fun s e t step => by
    subst step
    exact CopyingRegistration.step_retains_built_prefix law s e

/-- **The product only grows** along every course of the registration machine (from
`Copying.extends_along_iff`). -/
theorem product_extends_along (law : StructuralCopying.Law) :
    ∀ s plan t, Trace (CopyingRegistration.process law) s plan t →
      ∃ tail, t.work.built.cells = s.work.built.cells ++ tail :=
  Copying.extends_along_iff.mpr (product_extends law)

/-- The copy moves. -/
def copyGate : CopyingRegistration.Event → Bool
  | .copy => true
  | .dock _ _ => false
  | .lose _ => false
  | .slip _ _ => false

/-- **Only copy moves change the product.** Docking, loss and slip keep it. -/
theorem product_gated (law : StructuralCopying.Law) :
    Gated.KeptBy (CopyingRegistration.process law) copyGate (fun s => s.work.built) := by
  intro s e t step ungated
  subst step
  cases e with
  | dock i j =>
    show (CopyingRegistration.dock i j s).work.built = s.work.built
    unfold CopyingRegistration.dock
    split <;> rfl
  | lose i => rfl
  | slip i j =>
    show (CopyingRegistration.slip i j s).work.built = s.work.built
    unfold CopyingRegistration.slip
    split <;> rfl
  | copy => exact nomatch ungated

/-- A course of contact moves keeps the product (from `Gated.kept_along_iff`). -/
theorem contact_course_keeps_product (law : StructuralCopying.Law) {s t : CopyingRegistration.State}
    {plan : List CopyingRegistration.Event} (path : Trace (CopyingRegistration.process law) s plan t)
    (ungated : ∀ e, e ∈ plan → copyGate e = false) : t.work.built = s.work.built :=
  Gated.kept_along_iff.mpr (product_gated law) s plan t path ungated

/-- A course that changes the product contains a copy move (from `Gated.change_passes_gate`). -/
theorem product_change_passes_copy (law : StructuralCopying.Law) {s t : CopyingRegistration.State}
    {plan : List CopyingRegistration.Event} (path : Trace (CopyingRegistration.process law) s plan t)
    (changed : t.work.built ≠ s.work.built) : ∃ e, e ∈ plan ∧ copyGate e = true :=
  Gated.change_passes_gate (product_gated law) path changed

/-- Connectors with spare ones, material in product and pool, support free and spent. -/
def totals (s : CopyingRegistration.State) : Nat × Nat × Nat :=
  (s.contacts.length + s.spare, s.work.built.cells.length + s.work.supply.pool.length,
    s.work.supply.free + s.work.supply.spent)

theorem totals_kept (law : StructuralCopying.Law) :
    Gated.KeptBy (CopyingRegistration.process law) (fun _ => false) totals := by
  intro s e t step _
  subst step
  have ⟨a, b, c⟩ := CopyingRegistration.step_accounts law s e
  simp only [totals, a, b, c]

/-- **The totals are kept along every course** (the old `history_accounts`, from
`Gated.kept_along_iff` with no move gated). -/
theorem totals_along (law : StructuralCopying.Law) :
    ∀ s plan t, Trace (CopyingRegistration.process law) s plan t → totals t = totals s :=
  fun s plan t path => Gated.kept_along_iff.mpr (totals_kept law) s plan t path fun _ _ => rfl

end Registration

/-! ## Inspection against a reference -/

section Correction

theorem defects_eq : ∀ t b : List Bool, CopyingCorrection.defects t b = Copying.defects t b
  | [], [] => rfl
  | [], _ :: _ => rfl
  | _ :: _, [] => rfl
  | a :: as, b :: bs => by
    show (if a = b then 0 else 1) + CopyingCorrection.defects as bs =
      (if a = b then 0 else 1) + Copying.defects as bs
    rw [defects_eq as bs]

theorem exchange_view (i : Nat) (x : Bool) (w : StructuralCopying.CopyState) :
    view (CopyingCorrection.exchange i x w) = Copying.exchange 1 i x (view w) := by
  unfold CopyingCorrection.exchange Copying.exchange
  rw [show Copying.nth (view w).built i = w.built.cells[i]? from nth_eq _ _]
  cases h : w.built.cells[i]? with
  | none => rfl
  | some old =>
    show view (if old ≠ x ∧ x ∈ w.supply.pool ∧ 0 < w.supply.free then _ else _) =
      if ¬ old = x ∧ 0 < Copying.countOf x w.supply.pool ∧ 1 ≤ w.supply.free then _ else _
    by_cases c : old ≠ x ∧ x ∈ w.supply.pool ∧ 0 < w.supply.free
    · rw [if_pos c, if_pos ⟨c.1, (mem_iff_pos _ _).mp c.2.1, c.2.2⟩]
      simp [view, setAt_eq, final_eq, erase_eq]
    · rw [if_neg c, if_neg fun d => c ⟨d.1, (mem_iff_pos _ _).mpr d.2.1, d.2.2⟩]

/-- One inspection of the correction machine is one core inspection against its reference with
unit charges. -/
theorem inspect_view (i : Nat) (s : CopyingCorrection.State) :
    view (CopyingCorrection.inspect i s).assembly.work =
      Copying.inspect 1 1 (CopyingCorrection.reference s) i (view s.assembly.work) := by
  unfold CopyingCorrection.inspect Copying.inspect
  rw [show Copying.nth (view s.assembly.work).built i = s.assembly.work.built.cells[i]? from
    nth_eq _ _]
  cases hr : CopyingCorrection.reference s i with
  | none => rfl
  | some x =>
    cases hb : s.assembly.work.built.cells[i]? with
    | none => rfl
    | some old =>
      show view (if 0 < s.assembly.work.supply.free then _ else s).assembly.work =
        if 1 ≤ s.assembly.work.supply.free then _ else _
      by_cases f : 0 < s.assembly.work.supply.free
      · rw [if_pos f, if_pos (show 1 ≤ s.assembly.work.supply.free from f)]
        exact exchange_view i x _
      · rw [if_neg f, if_neg (show ¬ 1 ≤ s.assembly.work.supply.free from f)]

theorem inspect_keeps_reference (i : Nat) (s : CopyingCorrection.State) :
    CopyingCorrection.reference (CopyingCorrection.inspect i s) = CopyingCorrection.reference s := by
  have h := CopyingCorrection.inspection_preserves_organization s i
  funext j
  simp only [CopyingCorrection.reference, h.2.2.2, h.1]

theorem scan_template : ∀ (is : List Nat) (s : CopyingCorrection.State),
    (CopyingCorrection.scan is s).assembly.template = s.assembly.template
  | [], _ => rfl
  | i :: is, s => (scan_template is _).trans (CopyingCorrection.inspection_preserves_organization s i).1

theorem scan_view : ∀ (is : List Nat) (s : CopyingCorrection.State),
    view (CopyingCorrection.scan is s).assembly.work =
      Copying.scanSites 1 1 (CopyingCorrection.reference s) is (view s.assembly.work)
  | [], _ => rfl
  | i :: is, s => by
    show view (CopyingCorrection.scan is (CopyingCorrection.inspect i s)).assembly.work =
      Copying.scanSites 1 1 (CopyingCorrection.reference s) is
        (Copying.inspect 1 1 (CopyingCorrection.reference s) i (view s.assembly.work))
    rw [scan_view is (CopyingCorrection.inspect i s), inspect_keeps_reference, inspect_view]

/-- The state with another copy in progress. -/
def withWork (s : CopyingCorrection.State) (w : StructuralCopying.CopyState) : CopyingCorrection.State :=
  ⟨{ s.assembly with work := w }, s.routes⟩

/-- A core copy as a machine copy with an unbonded product. -/
def ofCopy (c : Copying.Scan Bool) : StructuralCopying.CopyState :=
  ⟨c.previous, c.pending, ⟨c.built, []⟩, ⟨c.pool, c.free, c.spent⟩⟩

/-- **Inspection never increases the defects exactly where the reference is faithful.** For
every correction state and site, inspecting the site never increases the defects against the
template for any copy in progress exactly when the reference agrees with the template there
(from `Copying.inspect_le_iff`). -/
theorem inspect_le_iff_instance (s : CopyingCorrection.State) (i : Nat) :
    (∀ w : StructuralCopying.CopyState,
      CopyingCorrection.defects s.assembly.template.cells
          (CopyingCorrection.inspect i (withWork s w)).assembly.work.built.cells ≤
        CopyingCorrection.defects s.assembly.template.cells w.built.cells) ↔
      Copying.FaithfulAt (CopyingCorrection.reference s) s.assembly.template.cells i := by
  have key : ∀ w, (CopyingCorrection.inspect i (withWork s w)).assembly.work.built.cells =
      (Copying.inspect 1 1 (CopyingCorrection.reference s) i (view w)).built :=
    fun w => congrArg Copying.Scan.built (inspect_view i (withWork s w))
  constructor
  · intro never
    apply (Copying.inspect_le_iff 1 1 _ _ i).mp
    intro c
    have h := never (ofCopy c)
    rw [key, defects_eq, defects_eq] at h
    exact h
  · intro faithful w
    rw [key, defects_eq, defects_eq]
    exact Copying.inspect_le faithful 1 1 (view w)

/-- **A scan of faithful sites never increases the defects** (from `Copying.scan_le`). -/
theorem scan_le_from_law (is : List Nat) (s : CopyingCorrection.State)
    (faithful : ∀ i, i ∈ is →
      Copying.FaithfulAt (CopyingCorrection.reference s) s.assembly.template.cells i) :
    CopyingCorrection.defects (CopyingCorrection.scan is s).assembly.template.cells
        (CopyingCorrection.scan is s).assembly.work.built.cells ≤
      CopyingCorrection.defects s.assembly.template.cells s.assembly.work.built.cells := by
  rw [scan_template, defects_eq, defects_eq]
  have h := Copying.scan_le 1 1 is (view s.assembly.work) faithful
  rw [← scan_view] at h
  exact h

theorem faithfulAt_of_faithful (s : CopyingCorrection.State) (h : CopyingCorrection.Faithful s)
    (i : Nat) : Copying.FaithfulAt (CopyingCorrection.reference s) s.assembly.template.cells i :=
  fun x y hr ht => by
    have hx := h i x hr
    rw [nth_eq] at ht
    rw [ht] at hx
    exact (Option.some.inj hx).symm

/-- The old faithful-scan theorem is the instance where the reference is faithful everywhere. -/
theorem scan_faithful_instance (s : CopyingCorrection.State) (is : List Nat)
    (h : CopyingCorrection.Faithful s) :
    CopyingCorrection.defects (CopyingCorrection.scan is s).assembly.template.cells
        (CopyingCorrection.scan is s).assembly.work.built.cells ≤
      CopyingCorrection.defects s.assembly.template.cells s.assembly.work.built.cells :=
  scan_le_from_law is s fun i _ => faithfulAt_of_faithful s h i

/-- The single-site criterion is an instance of `Copying.inspect_matches_iff` with unit
charges. -/
theorem matches_reference_from_law (s : CopyingCorrection.State) (i : Nat) (x old : Bool)
    (hr : CopyingCorrection.reference s i = some x)
    (hb : s.assembly.work.built.cells[i]? = some old) (ne : old ≠ x) :
    (CopyingCorrection.inspect i s).assembly.work.built.cells[i]? = some x ↔
      2 ≤ s.assembly.work.supply.free ∧ x ∈ s.assembly.work.supply.pool := by
  have h := Copying.inspect_matches_iff 1 1 (view s.assembly.work) hr
    (show Copying.nth (view s.assembly.work).built i = some old by rw [nth_eq]; exact hb) ne
  rw [← inspect_view, nth_eq, ← mem_iff_pos] at h
  exact h

/-- A product of the template's length has no defect exactly when it is the template. -/
theorem product_is_template_iff (t b : List Bool) (len : b.length = t.length) :
    CopyingCorrection.defects t b = 0 ↔ b = t := by
  rw [defects_eq]
  exact Copying.defects_zero_iff t b len

/-- The old witness of a damaged correct product: its reference is unfaithful at the inspected
site, the case the law excludes. -/
theorem wrong_reference_unfaithful :
    let good : CopyingCorrection.State := ⟨CopyingRegistration.run StructuralCopying.alternatingEasy
      CopyingRegistration.copying (CopyingRegistration.prepared 15), []⟩
    let s := CopyingCorrection.run StructuralCopying.alternatingEasy
      [.assembly (.lose 1), .connect 1 0] good
    ¬ Copying.FaithfulAt (CopyingCorrection.reference s) s.assembly.template.cells 1 := by
  intro good s f
  have hr : CopyingCorrection.reference s 1 = some false := by decide
  have ht : Copying.nth s.assembly.template.cells 1 = some true := by rw [nth_eq]; decide
  exact absurd (f false true hr ht) (by decide)

end Correction

end Becoming.CopyingInstances
