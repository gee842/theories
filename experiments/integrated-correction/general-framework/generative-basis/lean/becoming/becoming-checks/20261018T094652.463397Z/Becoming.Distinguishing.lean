import Becoming.Identification
import Becoming.Likeness

/-!
# Distinguishing: what tells configurations apart, and how deep

`Becoming.Histories` shows that tests fix likeness where branching is determined up to likeness
(`alike_iff_sameTests`); `Becoming.Identification` shows that a bounded prefix fixes the future
through a map (`bounded_agree`, `Law.sameFuture_iff_within`); `Becoming.Likeness` bounds the depth of
likeness by classes (`alike_iff_alikeTo_classes`, `alike_iff_alikeTo_across`). This module joins
them, with no premise:

* **The tests are a bounded prefix.** Under a determined law read through a map, in a
  world a list of `N` configurations holds, two configurations pass the same tests exactly where
  their futures through the map agree for `N - 1` steps (`Law.sameTests_iff_within`); across two
  such worlds of `N` and `N'` configurations, exactly where they agree for `N + N' - 1` steps
  (`Law.sameTests_iff_below_across`). Infinitely many tests, each a course of moves and a claim,
  are fixed by finitely many values through the map. Two laws read through maps are alike
  exactly where their futures through the maps agree at every step (`Law.alike_iff_agree`).
* **Moves that carry the map's value.** A law whose single move at each configuration is named
  by the map's value there, with nothing claimed (`Law.labelled`), is alike to depth `k`
  exactly where the futures through the map agree for `k` steps (`Law.alikeTo_labelled_iff`): one
  step fewer than when the map's value is claimed (`alikeTo_frameBy_iff` of `Becoming.Likeness`).
  Every history with at most `N` states is the course of a law on `N` configurations
  (`Law.realized_within`), so of such a frame, finite and decided (`Law.labelled_finite`).
* **The depths are exact for every pair.** For every `N` and `N'` there are such frames of `N`
  and `N'` configurations, held by lists of `N` and `N'` members, with configurations alike to
  depth `N + N' - 2` and not alike (`labelled_across_exact`): the depth `N + N' - 1` of
  `alike_iff_alikeTo_across` is exact, as `N - 1` within one frame is (`EndOfPath.classes_exact`).
  Read through maps, two worlds of `N` and `N'` configurations have configurations whose
  futures through the maps agree for `N + N' - 2` steps and which do not pass the same tests
  (`frameBy_across_exact`): `N + N' - 1` of `Law.sameTests_iff_below_across` is exact too. Both
  come from the histories of `Identification.bounded_agree_exact`. Within one world `N - 1` is
  exact too: on the path of `N` places to a last one that stays, read through a map that takes
  only whether the last is reached, the first two places agree for `N - 2` steps and do not pass
  the same tests
  (`frameBy_within_exact`).

The readings are the AI's, adopted on Ren's delegation of 15 October 2026 (DELEGATED-CHOICES D34):
what tells configurations apart within a bounded world is a finite prefix, and its length is set by
the number of configurations, exactly.
-/

namespace Becoming

open Generative

universe u u' v w

/-! ## The tests are a bounded prefix -/

namespace Law

variable {S : Type u} {S' : Type u'} {R : Type w}

/-- Agreeing at every step is a bisimulation between two laws read through maps. -/
theorem agree_bisimulation {next : S → S} {next' : S' → S'} {o : S → R} {o' : S' → R} :
    Bisimulation (Law.frameBy next o) (Law.frameBy next' o')
      (fun t t' => ∀ n, o (Law.orbit next t n) = o' (Law.orbit next' t' n)) :=
  fun s s' same =>
    have ahead : ∀ n, o (Law.orbit next (next s) n) = o' (Law.orbit next' (next' s') n) := fun n =>
      (congrArg o (Law.orbit_shift next s n)).symm.trans
        ((same (n + 1)).trans (congrArg o' (Law.orbit_shift next' s' n)))
    ⟨fun _ => ⟨fun at_s => (same 0).symm.trans at_s, fun at_s' => (same 0).trans at_s'⟩,
     fun _ t to => ⟨next' s', rfl, Eq.subst
        (motive := fun v => ∀ n, o (Law.orbit next v n) = o' (Law.orbit next' (next' s') n))
        (to : t = next s).symm ahead⟩,
     fun _ t' to => ⟨next s, rfl, Eq.subst
        (motive := fun v => ∀ n, o (Law.orbit next (next s) n) = o' (Law.orbit next' v n))
        (to : t' = next' s').symm ahead⟩⟩

/-- **Two laws read through maps are alike exactly where their futures through the maps agree
at every step.** -/
theorem alike_iff_agree {next : S → S} {next' : S' → S'} {o : S → R} {o' : S' → R} {s : S}
    {s' : S'} :
    Alike (Law.frameBy next o) (Law.frameBy next' o') s s' ↔
      ∀ n, o (Law.orbit next s n) = o' (Law.orbit next' s' n) :=
  ⟨fun alike n => alikeTo_frameBy_iff.mp (alike.alikeTo n) n (Nat.le_refl n),
   fun agree => ⟨_, agree_bisimulation, agree⟩⟩

/-- **The tests are a bounded prefix.** Under a determined law read through a map, in a
world a list of `N` configurations holds, two configurations pass the same tests exactly where
their futures through the map agree for `N - 1` steps. Tests fix likeness (`Determined.alike_iff_sameTests`
of `Becoming.Histories`), likeness is the same future through the map (`Law.alike_iff_sameFuture`), and
that is agreement for `N - 1` steps (`Law.sameFuture_iff_within`). -/
theorem sameTests_iff_within {next : S → S} {o : S → R} {l : List S} (world : ∀ s, s ∈ l)
    {s s' : S} :
    SameTests (Law.frameBy next o) (Law.frameBy next o) s s' ↔
      ∀ n, n < l.length - 1 → o (Law.orbit next s n) = o (Law.orbit next s' n) :=
  (Determined.alike_iff_sameTests (Law.frameBy_determined next o)).symm.trans
    (Law.alike_iff_sameFuture.trans
      (Law.sameFuture_iff_within (fun s _ => world (next s)) (world s) (world s')))

/-- **Across two worlds, the tests are a prefix of `N + N' - 1` steps.** Under two determined
laws read through maps, in worlds lists of `N` and `N'` configurations hold, two
configurations pass the same tests exactly where their futures through the maps agree for
`N + N' - 1` steps (`Identification.bounded_agree`). -/
theorem sameTests_iff_below_across {next : S → S} {next' : S' → S'} {o : S → R} {o' : S' → R}
    {l : List S} {l' : List S'} (world : ∀ s, s ∈ l) (world' : ∀ s', s' ∈ l') {s : S} {s' : S'} :
    SameTests (Law.frameBy next o) (Law.frameBy next' o') s s' ↔
      ∀ n, n < l.length + l'.length - 1 → o (Law.orbit next s n) = o' (Law.orbit next' s' n) :=
  (alike_iff_sameTests (Determined.at (Law.frameBy_determined next o))
    (Determined.at (Law.frameBy_determined next' o'))).symm.trans
    (alike_iff_agree.trans
      ⟨fun agree n _ => agree n, fun agree =>
        Identification.bounded_agree (statesBelow_held (fun s _ => world (next s)) (world s) o)
          (statesBelow_held (fun s _ => world' (next' s)) (world' s') o') agree⟩)

end Law

/-! ## Moves that carry the map's value -/

namespace Law

variable {S : Type u} {S' : Type u'} {A : Type v}

/-- A law whose single move at each configuration is named by the map's value there, with
nothing claimed. -/
def labelled (next : S → S) (o : S → A) : Frame S A Empty :=
  ⟨⟨fun s a t => t = next s ∧ a = o s⟩, fun _ c => nomatch c⟩

/-- **Where the moves carry the map's value, likeness to depth `k` is agreement for `k`
steps.** -/
theorem alikeTo_labelled_iff {next : S → S} {next' : S' → S'} {o : S → A} {o' : S' → A} :
    ∀ {k : Nat} {s : S} {s' : S'},
    AlikeTo (Law.labelled next o) (Law.labelled next' o') k s s' ↔
      ∀ n, n < k → o (Law.orbit next s n) = o' (Law.orbit next' s' n)
  | 0, _, _ => ⟨fun _ n lt => absurd lt (Nat.not_lt_zero n), fun _ c => nomatch c⟩
  | k + 1, s, s' =>
    ⟨fun ⟨_, forth, _⟩ n lt => match forth (o s) (next s) ⟨rfl, rfl⟩ with
      | ⟨_, ⟨to', named⟩, joined⟩ => match n, lt with
        | 0, _ => named
        | m + 1, lt =>
          (congrArg o (Law.orbit_shift next s m)).trans
            ((alikeTo_labelled_iff.mp
                (Eq.subst (motive := fun v => AlikeTo (Law.labelled next o) (Law.labelled next' o')
                  k (next s) v) to' joined) m (Nat.lt_of_succ_lt_succ lt)).trans
              (congrArg o' (Law.orbit_shift next' s' m)).symm),
     fun agree =>
      have ahead : AlikeTo (Law.labelled next o) (Law.labelled next' o') k (next s) (next' s') :=
        alikeTo_labelled_iff.mpr fun m lt =>
          (congrArg o (Law.orbit_shift next s m)).symm.trans
            ((agree (m + 1) (Nat.succ_lt_succ lt)).trans (congrArg o' (Law.orbit_shift next' s' m)))
      ⟨fun c => (nomatch c),
       fun _ _ ⟨to, named⟩ => ⟨next' s', ⟨rfl, named.trans (agree 0 (Nat.zero_lt_succ k))⟩,
         Eq.subst (motive := fun v => AlikeTo (Law.labelled next o) (Law.labelled next' o') k v
           (next' s')) (Eq.symm to) ahead⟩,
       fun _ _ ⟨to', named'⟩ => ⟨next s, ⟨rfl, named'.trans (agree 0 (Nat.zero_lt_succ k)).symm⟩,
         Eq.subst (motive := fun v => AlikeTo (Law.labelled next o) (Law.labelled next' o') k
           (next s) v) (Eq.symm to') ahead⟩⟩⟩

/-- Where the configurations are listed and their equality and the names are decided, the frame
is finite and decided. -/
theorem labelled_finite [DecidableEq S] [DecidableEq A] {next : S → S} {o : S → A}
    (listed : ∃ l : List S, ∀ s, s ∈ l) : FiniteDecided (Law.labelled next o) :=
  ⟨listed,
   fun s a t => if same : t = next s ∧ a = o s then .inl same else .inr same,
   fun _ c => nomatch c⟩

/-- A law on positions that stays below `N` is a law on `N` configurations, with the same
orbits. -/
theorem orbit_fin {N : Nat} {f : Nat → Nat} (stays : ∀ p, f p < N) (start : Fin N) :
    ∀ n, (Law.orbit (fun p : Fin N => (⟨f p.val, stays p.val⟩ : Fin N)) start n).val =
      Law.orbit f start.val n
  | 0 => rfl
  | n + 1 => congrArg f (orbit_fin stays start n)

/-- **Every history with at most `N` states is the course of a law on `N` configurations.** The
law is the history's lasso world on positions below `N` (`Learning.lassoNext`). -/
theorem realized_within {O : Type w} {x : Nat → O} {N : Nat} (bound : StatesBelow x N) :
    ∃ (next : Fin N → Fin N) (o : Fin N → O) (s : Fin N), ∀ n, o (Law.orbit next s n) = x n :=
  match Identification.statesBelow_iff_lasso.mp bound with
  | ⟨i, q, within, lasso⟩ =>
    have stays : ∀ p, Learning.lassoNext i q p < N := fun p =>
      match Nat.lt_or_ge p (i + q) with
      | .inl inside => Eq.subst (motive := fun v => v < N)
          (if_pos inside : Learning.lassoNext i q p = p + 1).symm
          (Nat.lt_of_lt_of_le (Nat.succ_lt_succ inside) within)
      | .inr last => Eq.subst (motive := fun v => v < N)
          (if_neg (fun inside => Nat.lt_irrefl _ (Nat.lt_of_lt_of_le inside last)) :
            Learning.lassoNext i q p = i).symm
          (Nat.lt_of_lt_of_le (Nat.lt_succ_of_le (Nat.le_add_right i q)) within)
    let start : Fin N := ⟨0, Nat.lt_of_lt_of_le (Nat.zero_lt_succ _) within⟩
    ⟨fun p => ⟨Learning.lassoNext i q p.val, stays p.val⟩, fun p => x p.val, start, fun n =>
      (congrArg x (orbit_fin stays start n)).trans ((Learning.lasso_realized lasso).2 n)⟩

end Law

/-! ## The depths are exact for every pair -/

/-- **Across two branching frames, the depth `N + N' - 1` is exact.** For every `N = M + 1` and
`N' = M' + 1` there are frames whose moves carry a map's value, of `N` and `N'` configurations,
finite and decided, with configurations alike to depth `N + N' - 2` and not alike. With the moves
and claims listed, they are alike exactly where alike to depth `N + N' - 1`
(`alike_iff_alikeTo_across`), and no lower depth will do. -/
theorem labelled_across_exact (M M' : Nat) :
    ∃ (F : Frame (Fin (M + 1)) Bool Empty) (G : Frame (Fin (M' + 1)) Bool Empty)
      (s : Fin (M + 1)) (s' : Fin (M' + 1)),
      FiniteDecided F ∧ FiniteDecided G ∧
      (finBelow (M + 1) (M + 1) (Nat.le_refl _)).length = M + 1 ∧
      (finBelow (M' + 1) (M' + 1) (Nat.le_refl _)).length = M' + 1 ∧
      AlikeTo F G (M + M') s s' ∧ ¬ Alike F G s s' :=
  match Identification.bounded_agree_exact (x := true) (y := false) (fun same => Bool.noConfusion same) M M' with
  | ⟨_, _, bound, bound', shared, differ⟩ =>
    match Law.realized_within bound, Law.realized_within bound' with
    | ⟨next, o, s, course⟩, ⟨next', o', s', course'⟩ =>
      ⟨Law.labelled next o, Law.labelled next' o', s, s',
       Law.labelled_finite ⟨_, fun t => mem_finBelow t (M + 1) (Nat.le_refl _) t.isLt⟩,
       Law.labelled_finite ⟨_, fun t => mem_finBelow t (M' + 1) (Nat.le_refl _) t.isLt⟩,
       length_finBelow (M + 1) (M + 1) (Nat.le_refl _),
       length_finBelow (M' + 1) (M' + 1) (Nat.le_refl _),
       Law.alikeTo_labelled_iff.mpr fun n early =>
         (course n).trans ((Identification.prefix_eq_iff.mp shared n early).trans (course' n).symm),
       fun alike => differ ((course (M + M')).symm.trans
         ((Law.alikeTo_labelled_iff.mp (alike.alikeTo (M + M' + 1)) (M + M')
           (Nat.lt_succ_self _)).trans (course' (M + M'))))⟩

/-- **Across two worlds read through maps, `N + N' - 1` is exact.** For every
`N = M + 1` and `N' = M' + 1` there are laws on `N` and `N'` configurations, read through
maps, with configurations whose futures through the maps agree for `N + N' - 2` steps and which
do not pass the same tests: the length of `Law.sameTests_iff_below_across` is exact. -/
theorem frameBy_across_exact (M M' : Nat) :
    ∃ (next : Fin (M + 1) → Fin (M + 1)) (o : Fin (M + 1) → Bool)
      (next' : Fin (M' + 1) → Fin (M' + 1)) (o' : Fin (M' + 1) → Bool)
      (s : Fin (M + 1)) (s' : Fin (M' + 1)),
      (∀ n, n < M + M' → o (Law.orbit next s n) = o' (Law.orbit next' s' n)) ∧
      ¬ SameTests (Law.frameBy next o) (Law.frameBy next' o') s s' :=
  match Identification.bounded_agree_exact (x := true) (y := false) (fun same => Bool.noConfusion same) M M' with
  | ⟨_, _, bound, bound', shared, differ⟩ =>
    match Law.realized_within bound, Law.realized_within bound' with
    | ⟨next, o, s, course⟩, ⟨next', o', s', course'⟩ =>
      ⟨next, o, next', o', s, s', fun n early =>
         (course n).trans ((Identification.prefix_eq_iff.mp shared n early).trans (course' n).symm),
       fun same => differ ((course (M + M')).symm.trans
         ((Law.alike_iff_agree.mp ((alike_iff_sameTests
            (Determined.at (Law.frameBy_determined next o))
            (Determined.at (Law.frameBy_determined next' o'))).mpr same) (M + M')).trans
           (course' (M + M'))))⟩

/-- **Within one world, `N - 1` is exact for the tests.** For every `N = M + 2` there is a law on
`N` configurations, read through a map, in a world a list of `N` members holds, with two
configurations whose futures through the map agree for `N - 2` steps and which do not pass the same
tests: the length `N - 1` of `Law.sameTests_iff_within` is exact. The law is the path of `N`
places to a last one that stays, read through a map that takes only whether the last is reached. -/
theorem frameBy_within_exact (M : Nat) :
    ∃ (next : Fin (M + 2) → Fin (M + 2)) (o : Fin (M + 2) → Bool) (s s' : Fin (M + 2)),
      (finBelow (M + 2) (M + 2) (Nat.le_refl _)).length = M + 2 ∧
      (∀ t, t ∈ finBelow (M + 2) (M + 2) (Nat.le_refl _)) ∧
      (∀ n, n < M → o (Law.orbit next s n) = o (Law.orbit next s' n)) ∧
      ¬ SameTests (Law.frameBy next o) (Law.frameBy next o) s s' :=
  have stays : ∀ p, Learning.lassoNext (M + 1) 0 p < M + 2 := fun p =>
    match Nat.lt_or_ge p (M + 1) with
    | .inl inside => Eq.subst (motive := fun v => v < M + 2)
        (if_pos inside : Learning.lassoNext (M + 1) 0 p = p + 1).symm (Nat.succ_lt_succ inside)
    | .inr last => Eq.subst (motive := fun v => v < M + 2)
        (if_neg (fun inside => Nat.lt_irrefl _ (Nat.lt_of_lt_of_le inside last)) :
          Learning.lassoNext (M + 1) 0 p = M + 1).symm (Nat.lt_succ_self _)
  let next : Fin (M + 2) → Fin (M + 2) := fun p => ⟨Learning.lassoNext (M + 1) 0 p.val, stays p.val⟩
  let o : Fin (M + 2) → Bool := fun p => if p.val < M + 1 then true else false
  let s : Fin (M + 2) := ⟨0, Nat.zero_lt_succ _⟩
  let s' : Fin (M + 2) := ⟨1, Nat.succ_lt_succ (Nat.zero_lt_succ M)⟩
  have reads : ∀ (x : Fin (M + 2)) (v : Nat), x.val = v → o x = if v < M + 1 then true else false :=
    fun _ _ at_v => congrArg (fun w => if w < M + 1 then true else false) at_v
  have from0 : ∀ n, n ≤ M + 1 → (Law.orbit next s n).val = n := fun n le =>
    (Law.orbit_fin stays s n).trans (Identification.lassoPos_early (i := M + 1) (q := 0) n le)
  have from1 : ∀ n, n ≤ M → (Law.orbit next s' n).val = n + 1 := fun n le =>
    (Law.orbit_fin stays s' n).trans
      ((congrArg (fun v => Law.orbit (Learning.lassoNext (M + 1) 0) v n)
        (if_pos (Nat.zero_lt_succ M) : Learning.lassoNext (M + 1) 0 0 = 1).symm).trans
        ((Law.orbit_shift _ 0 n).symm.trans
          (Identification.lassoPos_early (i := M + 1) (q := 0) (n + 1) (Nat.succ_le_succ le))))
  have world : ∀ t, t ∈ finBelow (M + 2) (M + 2) (Nat.le_refl _) := fun t =>
    mem_finBelow t (M + 2) (Nat.le_refl _) t.isLt
  ⟨next, o, s, s', length_finBelow (M + 2) (M + 2) (Nat.le_refl _), world,
   fun n early =>
    ((reads _ n (from0 n (Nat.le_trans (Nat.le_of_lt early) (Nat.le_succ M)))).trans
      (if_pos (Nat.lt_succ_of_lt early))).trans
      ((reads _ (n + 1) (from1 n (Nat.le_of_lt early))).trans
        (if_pos (Nat.succ_lt_succ early))).symm,
   fun same =>
    have agree := (Law.sameTests_iff_within world).mp same M
      (Eq.subst (motive := fun L => M < L - 1)
        (length_finBelow (M + 2) (M + 2) (Nat.le_refl _)).symm (Nat.lt_succ_self M))
    nomatch (((reads _ M (from0 M (Nat.le_succ M))).trans (if_pos (Nat.lt_succ_self M))).symm.trans
      (agree.trans ((reads _ (M + 1) (from1 M (Nat.le_refl M))).trans
        (if_neg (Nat.lt_irrefl (M + 1))))) : true = false)⟩

end Becoming
