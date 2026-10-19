import Becoming.Counting

/-!
# Tally worlds: the counts a world's census can have

`Becoming.Population` states that the counts some listing has are exactly the tallies
(`tally_iff_counted`), that a tally is the census balance with no more ceasing across a step
than were counted before it (`tally_iff`), that the balance alone is no tally
(`balance_not_tally`), and that a step after which nothing changes, asked of every tally with a
change bound, is the limited principle of omniscience (`ChangeBound.lpo_of_ends`). A census of a
world lists its active relata at each step (`Web.Census`), and `Becoming.Counting` reads every
tally as the census of a queue world (`World.queue`). This module states those laws of the
censuses of worlds and proves them through the laws of listings.

* **The counts of a world's census are exactly the tallies.** Some world's census counts `n`
  active at each step, `c` ceasing and `a` arising across it (`Shown`), exactly when `n`, `c`, `a`
  are a tally (`shown_iff_tally`); so exactly when they balance and no more cease across a step
  than were active before it (`shown_iff_balance`). The balance alone is not enough: none active,
  one ceasing and one arising across every step balance, and no world's census counts them
  (`balance_not_shown`).
* **The end of change asks for omniscience.** If every world's census whose change is bounded from
  the first step, with nothing arising across a step at which nothing is active, had a step after
  which nothing ceases or arises, `LPO` would hold (`lpo_of_census_ends`).

`World.counting_free` states that a property of the counts holds of every world's census exactly
when it holds of every tally. No ethical predicate, ranking or axiom occurs.
-/

namespace Becoming

namespace TallyWorlds

/-- Some world's census counts `n` active relata at each step, `c` ceasing and `a` arising across
the step from it. -/
def Shown (n c a : Nat → Nat) : Prop :=
  ∃ (w : World) (_ : ∀ t x, Decidable (w.web.active t x)) (alive : Nat → List w.Relatum),
    w.web.Census alive ∧ ∀ t, (alive t).length = n t ∧
      ceasings (alive t) (fun x s => w.web.active s x) t = c t ∧
      comings (alive (t + 1)) (fun x s => w.web.active s x) t = a t

/-- **The counts of a world's census are exactly the tallies.** Some world's census has the counts
`n`, `c`, `a` exactly when they are a tally; the queue world counts every tally. -/
theorem shown_iff_tally (n c a : Nat → Nat) : Shown n c a ↔ Tally n c a :=
  ⟨fun ⟨w, _, alive, census, same⟩ =>
     (tally_iff_counted n c a).mpr ⟨w.Relatum, fun x s => w.web.active s x, inferInstance, alive,
       census, same⟩,
   fun tally => ⟨World.queue n c, World.queue_decided n c, Queue.line n c, Queue.listed,
     Queue.counts tally⟩⟩

/-- **A world's census counts exactly what balances with ceasing within the count.** Some world's
census has the counts `n`, `c`, `a` exactly when, across each step, those active after it with
those ceasing are those active before it with those arising, and no more cease than were active
before it. -/
theorem shown_iff_balance (n c a : Nat → Nat) :
    Shown n c a ↔ Balance n c a ∧ ∀ t, c t ≤ n t :=
  (shown_iff_tally n c a).trans tally_iff

/-- **The balance alone is not a census.** With none active, one ceasing and one arising across
every step, the census balance holds and no world's census has these counts. -/
theorem balance_not_shown :
    Balance (fun _ => 0) (fun _ => 1) (fun _ => 1) ∧
      ¬ Shown (fun _ => 0) (fun _ => 1) (fun _ => 1) :=
  ⟨balance_not_tally.1, fun shown => balance_not_tally.2 ((shown_iff_tally _ _ _).mp shown)⟩

/-- Counting the steps at which a quantity is positive respects its values at each step. -/
theorem occurrences_congr {T : Nat} {q q' : Nat → Nat} (same : ∀ s, q s = q' s) :
    ∀ t, occurrences T q t = occurrences T q' t
  | 0 => rfl
  | t + 1 => (congr (congrArg (· + ·) (occurrences_congr same t))
      (mark_iff (p := T ≤ t ∧ 0 < q t) (q := T ≤ t ∧ 0 < q' t)
        ⟨fun ⟨later, pos⟩ => ⟨later, Eq.subst (motive := fun x => 0 < x) (same t) pos⟩,
         fun ⟨later, pos⟩ => ⟨later, Eq.subst (motive := fun x => 0 < x) (same t).symm pos⟩⟩) :
      occurrences T q t + mark (T ≤ t ∧ 0 < q t) = occurrences T q' t + mark (T ≤ t ∧ 0 < q' t))

/-- **The end of change in every world asks for omniscience.** If every census of every world
whose activity is decided, with change bounded from the first step and nothing arising across a
step at which nothing is active, had a step after which nothing ceases or arises, the limited
principle of omniscience would hold. -/
theorem lpo_of_census_ends
    (ends : ∀ (w : World) [∀ t x, Decidable (w.web.active t x)] (alive : Nat → List w.Relatum),
      w.web.Census alive →
      (∀ t, 0 < comings (alive (t + 1)) (fun x s => w.web.active s x) t → 0 < (alive t).length) →
      (∃ B, ChangeBound 0 B (fun t => (alive t).length)
        (fun t => ceasings (alive t) (fun x s => w.web.active s x) t)
        (fun t => comings (alive (t + 1)) (fun x s => w.web.active s x) t)) →
      ∃ E, ∀ t, E ≤ t → ceasings (alive t) (fun x s => w.web.active s x) t +
        comings (alive (t + 1)) (fun x s => w.web.active s x) t = 0) : LPO :=
  ChangeBound.lpo_of_ends fun n c _ tally company ⟨B, bound⟩ =>
    have counts := Queue.counts tally
    match ends (World.queue n c) (Queue.line n c) Queue.listed
        (fun t pos => Eq.subst (motive := fun x => 0 < x) (counts t).1.symm
          (company t (Eq.subst (motive := fun x => 0 < x) (counts t).2.2 pos)))
        ⟨B, fun t later => Nat.le_trans (Nat.le_of_eq (congr (congrArg (· + ·) (counts t).1)
            (occurrences_congr
              (fun s => congr (congrArg (· + ·) (counts s).2.1) (counts s).2.2) t)))
          (bound t later)⟩ with
    | ⟨E, quiet⟩ => ⟨E, fun t later =>
        (congr (congrArg (· + ·) (counts t).2.1) (counts t).2.2).symm.trans (quiet t later)⟩

end TallyWorlds

end Becoming
