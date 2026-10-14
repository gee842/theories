import Becoming.Copying
import Becoming.Countdown
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
  local draws (`copy_cells_iff`); it is released exactly when the support also covers one
  more unit (`reproduce_iff`), for every pool. The old law of the support needed, with the
  template's own tokens in the pool, is the instance (`template_pool_reproduce_iff`).
* **One shared pool.** Reproducing strands in turn from one pool and support, every strand is
  released exactly when the pool supplies all their tokens together and the support covers
  all their draws and releases (`batch_all_released_iff`); exchanging adjacent strands keeps
  this (`batch_all_released_swap`).
* **A lineage.** For every pool and support, every reproduction of a lineage of `n` from a
  path-shaped strand is released exactly when the pool holds each token at least `n` times as
  often as the strand uses it and the free support covers `n` times its draws and release
  (`lineage_released_iff`, from `Copying.lineage_all_iff`); a released lineage holds `n + 1`
  copies of the parent and has used `n` times the draws and release (`lineage_of_released`).
  The support used is `n` times the draws and release exactly when every reproduction is
  released (`lineage_used_iff`): this is the converse of `finite_lineage_inherits`, whose
  premises are the sufficient side (`finite_lineage_instance`). Read on the strands alone the
  converse is false: a lineage of one can hold two copies of the parent with its reproduction
  not released (`strands_do_not_show_release`).
* **Local draws.** The machine's draws are the core's local draws with first draw 1
  (`draw_eq`), so the ranking of the alternating and clustered strands
  (`local_ranking_from_law`) and the constraint on the mixed strand
  (`third_structure_from_law`) are instances of `use_lt_iff` and `use_midpoint`.
* **Chain growth and doubling rounds.** End attachment grows a chain by the alternating word
  exactly when the pool supplies that word and the support covers one unit per token
  (`grow_iff`); from the empty chain, the mature chain forms exactly when the pool holds at
  least four of each kind and at least eight units are free (`mature_forms_iff`). Attachment
  keeps the bonds the path on the tokens, so both hold bonds included (`grow_strand_iff`,
  `mature_strand_iff`). `n` rounds from `k` mature
  chains with the needed material reach `k * 2 ^ n` mature chains exactly when the support
  covers `9 * required n k` (`rounds_mature_iff`), that is, exactly when the core's doubling
  process with draw 9 runs `n` rounds (`rounds_follow_doubling`).
* **Reading through contacts.** For every registration state, operating as many copy moves as
  a word has tokens extends the product by that word exactly when each site reads the word's
  token through the actual contacts, the pool supplies the word and the support covers what it
  draws (`operate_copies_iff`); complete registration is the instance
  (`registered_copy_cells`). The chain's bonds need nothing beyond the tokens: every course
  keeps the product's bonds the path on its tokens (`path_shaped_along`, from
  `Countdown.invariant_iff_reach`), so the same condition makes the product the strand, bonds
  included (`operate_strand_iff`), and complete registration copies the template exactly when
  its bonds are the path on its tokens (`registered_copy_iff`); the old
  `registered_inheritance` is the instance without its non-empty premise
  (`registered_inheritance_instance`). Every course keeps the built product as a prefix
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

/-- The machine's draws are the core's local draws with first draw 1. -/
theorem draw_eq (law : StructuralCopying.Law) :
    StructuralCopying.charge law = Copying.pairDraw 1 law.equal law.unequal := by
  funext p x
  cases p <;> rfl

theorem use_eq (law : StructuralCopying.Law) : ∀ (p : Option Bool) (w : List Bool),
    StructuralCopying.cost law p w = Copying.use (StructuralCopying.charge law) p w
  | _, [] => rfl
  | p, x :: xs => congrArg (StructuralCopying.charge law p x + ·) (use_eq law (some x) xs)

theorem use_pair_eq (law : StructuralCopying.Law) (p : Option Bool) (w : List Bool) :
    StructuralCopying.cost law p w = Copying.use (Copying.pairDraw 1 law.equal law.unequal) p w := by
  rw [use_eq, draw_eq]

/-- One machine move is one core move. -/
theorem view_tick (law : StructuralCopying.Law) (w : StructuralCopying.CopyState) :
    view (StructuralCopying.tick law w) = Copying.tick (StructuralCopying.charge law) (view w) := by
  rcases w with ⟨prev, pending, built, ⟨pool, free, used⟩⟩
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
supplies them and the support covers the local draws, for every pool (from
`Copying.built_iff`). -/
theorem copy_cells_iff (law : StructuralCopying.Law) (parent : Strand)
    (hp : parent.bonds = path parent.cells.length) (hn : parent.cells ≠ []) (r : Supply) :
    (StructuralCopying.copy law parent r).built.cells = parent.cells ↔
      Copying.Supplies parent.cells r.pool ∧ StructuralCopying.cost law none parent.cells ≤ r.free := by
  have h := Copying.built_iff (StructuralCopying.charge law) none [] parent.cells r.pool r.free r.spent
  rw [← view_copy law parent hp hn r, ← use_eq] at h
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
supplies its tokens and the support covers its draws and the release, for every pool (from
`Copying.releases_iff`). -/
theorem reproduce_iff (law : StructuralCopying.Law) (parent : Strand)
    (hp : parent.bonds = path parent.cells.length) (hn : parent.cells ≠ []) (r : Supply) :
    (StructuralCopying.reproduce law parent r).1 = true ↔
      Copying.Supplies parent.cells r.pool ∧ StructuralCopying.cost law none parent.cells + 1 ≤ r.free := by
  have h := Copying.releases_iff (StructuralCopying.charge law) 1 none [] parent.cells r.pool r.free
    r.spent
  rw [← view_copy law parent hp hn r, ← use_eq] at h
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
    (tail : List Bool) (free used : Nat) :
    (StructuralCopying.reproduce law parent ⟨parent.cells ++ tail, free, used⟩).1 = true ↔
      StructuralCopying.cost law none parent.cells + 1 ≤ free :=
  (reproduce_iff law parent hp hn _).trans
    ⟨fun h => h.2, fun h => ⟨supplies_prefix _ _, h⟩⟩

theorem release_view (w : StructuralCopying.CopyState) (filled : w.pending = [] → w.built.cells ≠ []) :
    (StructuralCopying.release w).1 = Copying.released 1 (view w) ∧
    (StructuralCopying.release w).2.supply =
      ⟨w.supply.pool, cond (Copying.released 1 (view w)) (w.supply.free - 1) w.supply.free,
        cond (Copying.released 1 (view w)) (w.supply.spent + 1) w.supply.spent⟩ := by
  rcases w with ⟨prev, pending, built, ⟨pool, free, used⟩⟩
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
         cond (Copying.released 1 (copied law p r)) ((copied law p r).used + 1)
          (copied law p r).used⟩ := by
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
            (cond (Copying.released 1 (copied law p r)) ((copied law p r).used + 1)
              (copied law p r).used)).1
      rw [flag', supply']
      exact congrArg _ ih.1
    · show (StructuralCopying.batch law ps (StructuralCopying.reproduce law p r).2.supply).2 =
        ⟨(Copying.batch (StructuralCopying.charge law) 1 (ps.map Strand.cells) (copied law p r).pool
            (cond (Copying.released 1 (copied law p r)) ((copied law p r).free - 1) (copied law p r).free)
            (cond (Copying.released 1 (copied law p r)) ((copied law p r).used + 1)
              (copied law p r).used)).2.1,
         (Copying.batch (StructuralCopying.charge law) 1 (ps.map Strand.cells) (copied law p r).pool
            (cond (Copying.released 1 (copied law p r)) ((copied law p r).free - 1) (copied law p r).free)
            (cond (Copying.released 1 (copied law p r)) ((copied law p r).used + 1)
              (copied law p r).used)).2.2.1,
         (Copying.batch (StructuralCopying.charge law) 1 (ps.map Strand.cells) (copied law p r).pool
            (cond (Copying.released 1 (copied law p r)) ((copied law p r).free - 1) (copied law p r).free)
            (cond (Copying.released 1 (copied law p r)) ((copied law p r).used + 1)
              (copied law p r).used)).2.2.2⟩
      rw [supply']
      exact ih.2

/-- **One shared pool.** Every strand of a batch is released exactly when the pool supplies all
their tokens together and the support covers all their draws and releases. -/
theorem batch_all_released_iff (law : StructuralCopying.Law) (ps : List Strand) (r : Supply)
    (shaped : ∀ p, p ∈ ps → p.bonds = path p.cells.length ∧ p.cells ≠ []) :
    Copying.Every ((StructuralCopying.batch law ps r).1.map Prod.fst) ↔
      Copying.Supplies (Copying.joinAll (ps.map Strand.cells)) r.pool ∧
        Copying.totalOf (fun w => StructuralCopying.cost law none w + 1) (ps.map Strand.cells) ≤
          r.free := by
  rw [(batch_view law ps r shaped).1]
  have fe : (fun w => StructuralCopying.cost law none w + 1) =
      (fun w => Copying.use (StructuralCopying.charge law) none w + 1) :=
    funext fun w => congrArg (· + 1) (use_eq law none w)
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
`Copying.use_lt_iff`. -/
theorem local_ranking_from_law (law : StructuralCopying.Law) :
    StructuralCopying.cost law none StructuralCopying.alternating.cells <
        StructuralCopying.cost law none StructuralCopying.clustered.cells ↔
      law.unequal < law.equal := by
  rw [use_pair_eq, use_pair_eq]
  exact Copying.use_lt_iff 1 law.equal law.unequal (x := false) (y := false)
    (l := [false, true, true]) (m := [true, false, true]) rfl (d := 2) rfl (by decide)

/-- **The third arrangement**, an instance of `Copying.use_midpoint`. -/
theorem third_structure_from_law (law : StructuralCopying.Law) :
    2 * (StructuralCopying.cost law none StructuralCopying.mixed.cells + 1) =
      (StructuralCopying.cost law none StructuralCopying.alternating.cells + 1) +
        (StructuralCopying.cost law none StructuralCopying.clustered.cells + 1) := by
  have h := Copying.use_midpoint 1 law.equal law.unequal (x := false) (y := false) (z := false)
    (l := [true, false, true]) (m := [true, true, false]) (k := [false, true, true]) rfl rfl rfl
  rw [use_pair_eq, use_pair_eq, use_pair_eq]
  show 2 * (Copying.use (Copying.pairDraw 1 law.equal law.unequal) none
        (false :: [true, true, false]) + 1) =
      (Copying.use (Copying.pairDraw 1 law.equal law.unequal) none
        (false :: [true, false, true]) + 1) +
      (Copying.use (Copying.pairDraw 1 law.equal law.unequal) none
        (false :: [false, true, true]) + 1)
  omega

/-! ### A lineage -/

theorem strand_eq {s p : Strand} (cells : s.cells = p.cells) (bonds : s.bonds = p.bonds) :
    s = p := by
  cases s
  cases p
  simp_all

/-- Every reproduction of a lineage of `n` is released. -/
def AllReleased (law : StructuralCopying.Law) : Nat → Strand → Supply → Prop
  | 0, _, _ => True
  | n + 1, p, r => (StructuralCopying.reproduce law p r).1 = true ∧
      AllReleased law n (StructuralCopying.reproduce law p r).2.built
        (StructuralCopying.reproduce law p r).2.supply

theorem reproduce_built_eq (law : StructuralCopying.Law) (p : Strand) (r : Supply) :
    (StructuralCopying.reproduce law p r).2.built = (StructuralCopying.copy law p r).built := by
  unfold StructuralCopying.reproduce StructuralCopying.release
  split <;> rfl

/-- A released reproduction of a path-shaped strand is the strand, bonds included. -/
theorem reproduce_built (law : StructuralCopying.Law) (p : Strand)
    (hp : p.bonds = path p.cells.length) (hn : p.cells ≠ []) (r : Supply)
    (h : (StructuralCopying.reproduce law p r).1 = true) :
    (StructuralCopying.reproduce law p r).2.built = p := by
  have ⟨hs, hc⟩ := (reproduce_iff law p hp hn r).mp h
  have cells := (copy_cells_iff law p hp hn r).mpr ⟨hs, Nat.le_trans (Nat.le_add_right _ 1) hc⟩
  have bonds := StructuralCopying.steps_preserve_path law p.cells.length
    (StructuralCopying.start p r) rfl
  have e : StructuralCopying.copy law p r =
      StructuralCopying.steps law p.cells.length (StructuralCopying.start p r) := by
    simp only [StructuralCopying.copy, if_pos (And.intro hp hn)]
  rw [reproduce_built_eq, e]
  rw [e] at cells
  exact strand_eq cells (by rw [bonds, cells, hp])

/-- What a copy uses is at most the draws of its strand. -/
theorem copy_used_le (law : StructuralCopying.Law) (p : Strand)
    (hp : p.bonds = path p.cells.length) (hn : p.cells ≠ []) (r : Supply) :
    (StructuralCopying.copy law p r).supply.spent ≤ r.spent + StructuralCopying.cost law none p.cells := by
  have hc : (StructuralCopying.steps law p.cells.length (StructuralCopying.start p r)).supply.spent +
      StructuralCopying.cost law
        (StructuralCopying.steps law p.cells.length (StructuralCopying.start p r)).previous
        (StructuralCopying.steps law p.cells.length (StructuralCopying.start p r)).pending =
      r.spent + StructuralCopying.cost law none p.cells :=
    StructuralCopying.steps_cost_balance law p.cells.length (StructuralCopying.start p r)
  simp only [StructuralCopying.copy, if_pos (And.intro hp hn)]
  omega

/-- A released reproduction uses the draws and the release; one not released uses at most the
draws. -/
theorem reproduce_strand_used (law : StructuralCopying.Law) (p : Strand)
    (hp : p.bonds = path p.cells.length) (hn : p.cells ≠ []) (r : Supply) :
    ((StructuralCopying.reproduce law p r).1 = true →
        (StructuralCopying.reproduce law p r).2.supply.spent =
          r.spent + (StructuralCopying.cost law none p.cells + 1)) ∧
      ((StructuralCopying.reproduce law p r).1 = false →
        (StructuralCopying.reproduce law p r).2.supply.spent ≤
          r.spent + StructuralCopying.cost law none p.cells) := by
  have le := copy_used_le law p hp hn r
  unfold StructuralCopying.reproduce StructuralCopying.release
  split
  · rename_i c
    have e := StructuralCopying.completed_copy_requires_cost law p r c.1
    refine ⟨fun _ => ?_, fun h => by simp at h⟩
    simp only
    omega
  · exact ⟨fun h => by simp at h, fun _ => le⟩

/-- A lineage is released copy by copy exactly when the batch of `n` copies of its parent is. -/
theorem all_released_iff_batch (law : StructuralCopying.Law) (p : Strand)
    (hp : p.bonds = path p.cells.length) (hn : p.cells ≠ []) : ∀ (n : Nat) (r : Supply),
    AllReleased law n p r ↔
      Copying.Every ((StructuralCopying.batch law (List.replicate n p) r).1.map Prod.fst)
  | 0, _ => Iff.rfl
  | n + 1, r => by
    show ((StructuralCopying.reproduce law p r).1 = true ∧
        AllReleased law n (StructuralCopying.reproduce law p r).2.built
          (StructuralCopying.reproduce law p r).2.supply) ↔
      ((StructuralCopying.reproduce law p r).1 = true ∧
        Copying.Every ((StructuralCopying.batch law (List.replicate n p)
          (StructuralCopying.reproduce law p r).2.supply).1.map Prod.fst))
    constructor
    · intro ⟨h, rest⟩
      rw [reproduce_built law p hp hn r h] at rest
      exact ⟨h, (all_released_iff_batch law p hp hn n _).mp rest⟩
    · intro ⟨h, rest⟩
      refine ⟨h, ?_⟩
      rw [reproduce_built law p hp hn r h]
      exact (all_released_iff_batch law p hp hn n _).mpr rest

/-- **The lineage law** (from `Copying.lineage_all_iff`). For every pool and support, every
reproduction of a lineage of `n` from a path-shaped strand is released exactly when the pool
holds each token at least `n` times as often as the strand uses it and the free support covers
`n` times its draws and release. -/
theorem lineage_released_iff (law : StructuralCopying.Law) (p : Strand)
    (hp : p.bonds = path p.cells.length) (hn : p.cells ≠ []) (n : Nat) (r : Supply) :
    AllReleased law n p r ↔
      (∀ a, n * Copying.countOf a p.cells ≤ Copying.countOf a r.pool) ∧
        n * (StructuralCopying.cost law none p.cells + 1) ≤ r.free := by
  rw [all_released_iff_batch law p hp hn n r,
    (batch_view law (List.replicate n p) r fun q m => by
      rw [List.eq_of_mem_replicate m]
      exact ⟨hp, hn⟩).1,
    List.map_replicate, use_eq]
  exact Copying.lineage_all_iff (StructuralCopying.charge law) 1 p.cells r.pool r.free r.spent n

/-- **A released lineage reproduces its parent**: `n + 1` copies of it, with the support used
grown by `n` times the draws and release. -/
theorem lineage_of_released (law : StructuralCopying.Law) (p : Strand)
    (hp : p.bonds = path p.cells.length) (hn : p.cells ≠ []) : ∀ (n : Nat) (r : Supply),
    AllReleased law n p r →
      (StructuralCopying.descendants law n p r).1 = List.replicate (n + 1) p ∧
        (StructuralCopying.descendants law n p r).2.spent =
          r.spent + n * (StructuralCopying.cost law none p.cells + 1)
  | 0, r, _ => ⟨rfl, by simp [StructuralCopying.descendants]⟩
  | n + 1, r, ⟨h, rest⟩ => by
    have built := reproduce_built law p hp hn r h
    rw [built] at rest
    have ih := lineage_of_released law p hp hn n _ rest
    have used := (reproduce_strand_used law p hp hn r).1 h
    simp only [StructuralCopying.descendants, h, if_true, built]
    refine ⟨by rw [ih.1]; rfl, ?_⟩
    rw [ih.2, used, Nat.succ_mul]
    omega

/-- **The converse of `finite_lineage_inherits`, read on the support used.** A lineage of `n`
from a path-shaped strand uses `n` times the draws and release exactly when every reproduction
is released, so exactly when the pool and support satisfy the lineage law. -/
theorem lineage_used_iff (law : StructuralCopying.Law) (p : Strand)
    (hp : p.bonds = path p.cells.length) (hn : p.cells ≠ []) : ∀ (n : Nat) (r : Supply),
    (StructuralCopying.descendants law n p r).2.spent =
        r.spent + n * (StructuralCopying.cost law none p.cells + 1) ↔ AllReleased law n p r
  | 0, r => ⟨fun _ => trivial, fun _ => by simp [StructuralCopying.descendants]⟩
  | n + 1, r => by
    cases h : (StructuralCopying.reproduce law p r).1 with
    | true =>
      have built := reproduce_built law p hp hn r h
      have used := (reproduce_strand_used law p hp hn r).1 h
      have ih := lineage_used_iff law p hp hn n (StructuralCopying.reproduce law p r).2.supply
      simp only [StructuralCopying.descendants, h, if_true, AllReleased, true_and, built]
      rw [← ih, used, Nat.succ_mul]
      constructor <;> intro e <;> omega
    | false =>
      have used := (reproduce_strand_used law p hp hn r).2 h
      simp only [StructuralCopying.descendants, h, AllReleased]
      simp only [Bool.false_eq_true, if_false, false_and, iff_false]
      rw [Nat.succ_mul]
      omega

/-- The old feed of `n` copies is the core's `n` copies joined. -/
theorem repeatedFeed_eq (w : List Bool) : ∀ n : Nat,
    StructuralCopying.repeatedFeed w n = Copying.joinAll (List.replicate n w)
  | 0 => rfl
  | n + 1 => congrArg (w ++ ·) (repeatedFeed_eq w n)

/-- `finite_lineage_inherits`'s pool and support satisfy the lineage law: the old theorem is its
sufficient side. -/
theorem finite_lineage_instance (law : StructuralCopying.Law) (p : Strand)
    (hp : p.bonds = path p.cells.length) (hn : p.cells ≠ []) (n : Nat) (tail : List Bool)
    (free spent : Nat) :
    AllReleased law n p ⟨StructuralCopying.repeatedFeed p.cells n ++ tail,
      free + n * (StructuralCopying.cost law none p.cells + 1), spent⟩ :=
  (lineage_released_iff law p hp hn n _).mpr
    ⟨fun a => by
      show n * Copying.countOf a p.cells ≤
        Copying.countOf a (StructuralCopying.repeatedFeed p.cells n ++ tail)
      rw [Copying.countOf_append, repeatedFeed_eq, Copying.countOf_joinAll_replicate]
      exact Nat.le_add_right _ _,
     Nat.le_add_left _ _⟩

/-- **The strands alone do not show release.** With support for the copy but not for its
release, a lineage of one holds two copies of the parent, yet its reproduction is not released:
the converse of `finite_lineage_inherits` read on the strands alone is false. -/
theorem strands_do_not_show_release :
    (StructuralCopying.descendants StructuralCopying.alternatingEasy 1 StructuralCopying.alternating
        ⟨StructuralCopying.feed, 4, 0⟩).1 = List.replicate 2 StructuralCopying.alternating ∧
      ¬ AllReleased StructuralCopying.alternatingEasy 1 StructuralCopying.alternating
        ⟨StructuralCopying.feed, 4, 0⟩ := by
  refine ⟨by decide, fun ⟨h, _⟩ => ?_⟩
  rw [StructuralCopying.full_copy_need_not_be_released.2] at h
  exact Bool.noConfusion h

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

theorem use_unit : ∀ (p : Option Bool) (w : List Bool), Copying.use unit p w = w.length
  | _, [] => rfl
  | _, _ :: xs => (Nat.add_comm 1 _).trans (congrArg (· + 1) (use_unit _ xs))

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
  (c.built, c.pool, c.free, c.used)

/-- End attachment is the core copy of the alternating word with unit draws. -/
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
  rw [use_unit, length_alternatingFrom] at h
  exact h

/-- From the empty chain, the mature chain forms exactly when the pool holds at least four of
each kind and at least eight units are free. -/
theorem mature_forms_iff (r : Supply) :
    (grow 8 ⟨[], []⟩ r).1.cells = mature.cells ↔
      Copying.Supplies mature.cells r.pool ∧ 8 ≤ r.free :=
  grow_iff 8 ⟨[], []⟩ r (by decide)

/-- Attachment keeps the chain's bonds the path on its tokens. -/
theorem attach_path_shaped (s : Strand) (r : Supply) (h : s.bonds = path s.cells.length) :
    (attach s r).1.bonds = path (attach s r).1.cells.length := by
  unfold attach
  split
  · simp only [List.length_append, List.length_singleton, path]
    cases hs : s.cells <;> simp_all [path]
  · exact h

theorem grow_path_shaped : ∀ (n : Nat) (s : Strand) (r : Supply),
    s.bonds = path s.cells.length → (grow n s r).1.bonds = path (grow n s r).1.cells.length
  | 0, _, _, h => h
  | n + 1, s, r, h => grow_path_shaped n _ _ (attach_path_shaped s r h)

/-- **Chain growth, bonds included.** Within the size limit, a chain whose bonds are the path on
its tokens grows by the alternating word, bonds included, exactly when the pool supplies that
word and the support covers one unit per token: the bonds need nothing beyond the tokens. -/
theorem grow_strand_iff (n : Nat) (s : Strand) (r : Supply) (room : s.cells.length + n ≤ 8)
    (shaped : s.bonds = path s.cells.length) :
    (grow n s r).1 = ⟨s.cells ++ alternatingFrom (wanted s) n,
        path (s.cells ++ alternatingFrom (wanted s) n).length⟩ ↔
      Copying.Supplies (alternatingFrom (wanted s) n) r.pool ∧ n ≤ r.free := by
  rw [← grow_iff n s r room]
  have hb := grow_path_shaped n s r shaped
  constructor
  · intro h
    rw [h]
  · intro h
    exact strand_eq h (by rw [hb, h])

/-- From the empty chain the mature chain forms, bonds included, exactly when the pool holds at
least four of each kind and at least eight units are free. -/
theorem mature_strand_iff (r : Supply) :
    (grow 8 ⟨[], []⟩ r).1 = mature ↔ Copying.Supplies mature.cells r.pool ∧ 8 ≤ r.free :=
  grow_strand_iff 8 ⟨[], []⟩ r (by decide) rfl

theorem required_eq : ∀ n k : Nat, Copying.required n k = RecurrentAssembly.required n k
  | 0, _ => rfl
  | n + 1, k => congrArg (k + ·) (required_eq n (2 * k))

theorem attach_used (s : Strand) (r : Supply) :
    (attach s r).2.spent + s.cells.length = r.spent + (attach s r).1.cells.length := by
  unfold attach
  split <;> simp <;> omega

theorem grow_used : ∀ (n : Nat) (s : Strand) (r : Supply),
    (grow n s r).2.spent + s.cells.length = r.spent + (grow n s r).1.cells.length
  | 0, _, _ => rfl
  | n + 1, s, r => by
    have a := attach_used s r
    have g := grow_used n (attach s r).1 (attach s r).2
    show (grow n (attach s r).1 (attach s r).2).2.spent + s.cells.length =
      r.spent + (grow n (attach s r).1 (attach s r).2).1.cells.length
    omega

/-- Each attachment and each cleavage draws one unit: support used grows with size plus
number of chains. -/
theorem reproduce_used (s : Strand) (r : Supply) :
    (reproduce s r).2.spent + s.cells.length + 1 =
      r.spent + size (reproduce s r).1 + (reproduce s r).1.length := by
  unfold reproduce
  split
  · rename_i h
    have ha := grow_used 4 (fragment s 0 4) ⟨r.pool, r.free - 1, r.spent + 1⟩
    have hb := grow_used 4 (fragment s 4 4) (grow 4 (fragment s 0 4) ⟨r.pool, r.free - 1, r.spent + 1⟩).2
    simp only [size, fragment, List.drop_zero, List.length_take, List.length_drop, h.1] at *
    simp only [List.length_cons, List.length_nil]
    omega
  · simp [size]

theorem generation_used : ∀ (ss : List Strand) (r : Supply),
    (generation ss r).2.spent + size ss + ss.length =
      r.spent + size (generation ss r).1 + (generation ss r).1.length
  | [], _ => rfl
  | s :: ss, r => by
    have h := reproduce_used s r
    have hi := generation_used ss (reproduce s r).2
    simp only [generation, size_append, size, List.length_append, List.length_cons]
    omega

theorem rounds_used : ∀ (n : Nat) (ss : List Strand) (r : Supply),
    (rounds n ss r).2.spent + size ss + ss.length =
      r.spent + size (rounds n ss r).1 + (rounds n ss r).1.length
  | 0, _, _ => rfl
  | n + 1, ss, r => by
    have h := generation_used ss r
    have hi := rounds_used n (generation ss r).1 (generation ss r).2
    show (rounds n (generation ss r).1 (generation ss r).2).2.spent + size ss + ss.length =
      r.spent + size (rounds n (generation ss r).1 (generation ss r).2).1 +
        (rounds n (generation ss r).1 (generation ss r).2).1.length
    omega

/-- **Doubling rounds.** From `k` mature chains with the material for `n` rounds, the rounds
reach `k * 2 ^ n` mature chains exactly when the support covers `9 * required n k`. -/
theorem rounds_mature_iff (n k : Nat) (tail : List Bool) (free used : Nat) :
    (rounds n (List.replicate k mature) ⟨blocks (RecurrentAssembly.required n k) ++ tail, free, used⟩).1 =
        List.replicate (k * 2 ^ n) mature ↔
      9 * RecurrentAssembly.required n k ≤ free := by
  constructor
  · intro h
    have hs := rounds_used n (List.replicate k mature)
      ⟨blocks (RecurrentAssembly.required n k) ++ tail, free, used⟩
    have ha := (rounds_accounts n (List.replicate k mature)
      ⟨blocks (RecurrentAssembly.required n k) ++ tail, free, used⟩).2
    rw [h, size_replicate, size_replicate, List.length_replicate, List.length_replicate] at hs
    have g := required_as_growth n k
    dsimp only at ha hs
    revert hs ha g
    generalize (rounds n (List.replicate k mature)
      ⟨blocks (RecurrentAssembly.required n k) ++ tail, free, used⟩).2 = r'
    generalize k * 2 ^ n = K
    generalize RecurrentAssembly.required n k = R
    intro hs ha g
    omega
  · intro h
    have e := supported_rounds n k tail (free - 9 * RecurrentAssembly.required n k) used
    rw [Nat.sub_add_cancel h] at e
    rw [e]

/-- **The rounds follow the core's doubling.** The machine reaches `k * 2 ^ n` mature chains
exactly when the doubling process with draw 9 runs `n` rounds from `k` units and the free
support. -/
theorem rounds_follow_doubling (n k : Nat) (tail : List Bool) (free used : Nat) :
    (rounds n (List.replicate k mature) ⟨blocks (RecurrentAssembly.required n k) ++ tail, free, used⟩).1 =
        List.replicate (k * 2 ^ n) mature ↔
      ∃ t, Trace (Copying.doubling 9) (k, free) (Copying.rounds n) t :=
  (rounds_mature_iff n k tail free used).trans
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
  rcases s with ⟨template, ⟨prev, pending, built, ⟨pool, free, used⟩⟩, contacts, spare⟩
  show view (CopyingRegistration.tick law ⟨template, ⟨prev, pending, built, ⟨pool, free, used⟩⟩,
      contacts, spare⟩).work =
    Copying.readStep (StructuralCopying.charge law) ⟨prev, pending, built.cells, pool, free, used⟩
      (CopyingRegistration.readAt ⟨template, ⟨prev, pending, built, ⟨pool, free, used⟩⟩,
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
the actual contacts, the pool supplies the word and the support covers what it draws (from
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
  rw [← use_eq] at h
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
    (free used : Nat) (contacts : List (Nat × Nat)) (spare : Nat)
    (hreg : CopyingRegistration.Registered ⟨p, StructuralCopying.start p
      ⟨p.cells ++ tail, free + StructuralCopying.cost law none p.cells, used⟩, contacts, spare⟩) :
    (CopyingRegistration.operate law p.cells.length ⟨p, StructuralCopying.start p
      ⟨p.cells ++ tail, free + StructuralCopying.cost law none p.cells, used⟩, contacts, spare⟩).work.built.cells =
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

/-- Connectors with spare ones, material in product and pool, support free and used. -/
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

/-! ### The chain's bonds -/

/-- The product's bonds are the path on its tokens. -/
def PathShaped (s : CopyingRegistration.State) : Prop :=
  s.work.built.bonds = path s.work.built.cells.length

theorem extend_path (s : Strand) (x : Bool) (h : s.bonds = path s.cells.length) :
    (StructuralCopying.extend s x).bonds = path (StructuralCopying.extend s x).cells.length := by
  simp only [StructuralCopying.extend, List.length_append, List.length_singleton, path]
  cases hs : s.cells <;> simp_all [path]

theorem tick_path_shaped (law : StructuralCopying.Law) (s : CopyingRegistration.State)
    (h : PathShaped s) : PathShaped (CopyingRegistration.tick law s) := by
  unfold PathShaped CopyingRegistration.tick at *
  split
  · dsimp only
    split
    · exact extend_path _ _ h
    · exact h
  · exact h

/-- **The bonds need nothing beyond the tokens.** Every course of the registration machine keeps
the product's bonds the path on its tokens (an instance of `Countdown.invariant_iff_reach`:
copy moves extend the path, the other moves keep the product). -/
theorem path_shaped_along (law : StructuralCopying.Law) :
    ∀ s t, Reach (CopyingRegistration.process law) s t → PathShaped s → PathShaped t :=
  Countdown.invariant_iff_reach.mp fun s e t step held => by
    cases e with
    | copy =>
      subst step
      exact tick_path_shaped law s held
    | dock i j =>
      have same : t.work.built = s.work.built := product_gated law s _ t step rfl
      unfold PathShaped
      rw [same]
      exact held
    | lose i =>
      have same : t.work.built = s.work.built := product_gated law s _ t step rfl
      unfold PathShaped
      rw [same]
      exact held
    | slip i j =>
      have same : t.work.built = s.work.built := product_gated law s _ t step rfl
      unfold PathShaped
      rw [same]
      exact held

theorem operate_path_shaped (law : StructuralCopying.Law) : ∀ (n : Nat) (s : CopyingRegistration.State),
    PathShaped s → PathShaped (CopyingRegistration.operate law n s)
  | 0, _, h => h
  | n + 1, s, h => operate_path_shaped law n _ (tick_path_shaped law s h)

/-- **Reading through contacts, bonds included.** For every registration state whose product is
path-shaped, as many copy moves as a word has tokens make the product the strand of its tokens
followed by the word, bonds included, exactly when each site reads the word's token through the
actual contacts, the pool supplies the word and the support covers what it draws. -/
theorem operate_strand_iff (law : StructuralCopying.Law) (s : CopyingRegistration.State)
    (word : List Bool) (len : s.work.pending.length = word.length) (shaped : PathShaped s) :
    (CopyingRegistration.operate law word.length s).work.built =
        ⟨s.work.built.cells ++ word, path (s.work.built.cells ++ word).length⟩ ↔
      Copying.Reads (CopyingRegistration.readAt s) s.work.built.cells.length word ∧
        Copying.Supplies word s.work.supply.pool ∧
        StructuralCopying.cost law s.work.previous word ≤ s.work.supply.free := by
  rw [← operate_copies_iff law s word len]
  have hb := operate_path_shaped law word.length s shaped
  unfold PathShaped at hb
  constructor
  · intro h
    rw [h]
  · intro h
    exact strand_eq h (by rw [hb, h])

/-- **Complete registration copies the template, bonds included, exactly when the template's
bonds are the path on its tokens.** The tokens need the pool and support
(`registered_copy_cells`); the bonds need nothing more. -/
theorem registered_copy_iff (law : StructuralCopying.Law) (p : Strand) (tail : List Bool)
    (free used : Nat) (contacts : List (Nat × Nat)) (spare : Nat)
    (hreg : CopyingRegistration.Registered ⟨p, StructuralCopying.start p
      ⟨p.cells ++ tail, free + StructuralCopying.cost law none p.cells, used⟩, contacts, spare⟩) :
    (CopyingRegistration.operate law p.cells.length ⟨p, StructuralCopying.start p
      ⟨p.cells ++ tail, free + StructuralCopying.cost law none p.cells, used⟩, contacts, spare⟩).work.built =
      p ↔ p.bonds = path p.cells.length := by
  have cells := registered_copy_cells law p tail free used contacts spare hreg
  have shaped := operate_path_shaped law p.cells.length ⟨p, StructuralCopying.start p
    ⟨p.cells ++ tail, free + StructuralCopying.cost law none p.cells, used⟩, contacts, spare⟩ rfl
  unfold PathShaped at shaped
  constructor
  · intro h
    rw [h] at shaped
    exact shaped
  · intro hp
    exact strand_eq cells (by rw [shaped, cells, hp])

/-- The old `registered_inheritance` is the instance, without its non-empty premise. -/
theorem registered_inheritance_instance (law : StructuralCopying.Law) (p : Strand)
    (hp : p.bonds = path p.cells.length) (tail : List Bool) (free used : Nat)
    (contacts : List (Nat × Nat)) (spare : Nat)
    (hreg : CopyingRegistration.Registered ⟨p, StructuralCopying.start p
      ⟨p.cells ++ tail, free + StructuralCopying.cost law none p.cells, used⟩, contacts, spare⟩) :
    (CopyingRegistration.operate law p.cells.length ⟨p, StructuralCopying.start p
      ⟨p.cells ++ tail, free + StructuralCopying.cost law none p.cells, used⟩, contacts, spare⟩).work.built =
      p :=
  (registered_copy_iff law p tail free used contacts spare hreg).mpr hp

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
unit draws. -/
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
  ⟨c.previous, c.pending, ⟨c.built, []⟩, ⟨c.pool, c.free, c.used⟩⟩

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
draws. -/
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
