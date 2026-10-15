import Becoming.Selection
import TieBreaking

/-!
# Plural records and equal chances as instances of selection through a model of the options

`PluralRecords` asks which center a rule may serve when it treats the centers alike, and
`TieBreaking` which weights a lottery may give them. A record (`Record n`) is the core's model of
the options `Fin n`, an entry for each, and there:
* exchanging two centers is the core's `Relabel.swap` (`transpose_eq_swap`); a rule treats the
  centers alike exactly when it is a choice through the model (`treatsAlike_iff`), a lottery
  exactly when its weights are a valuation through the model and its withholding
  weight does not change (`lotteryAlike_iff`), and holding an entry alone is the core's
  `Relabel.Alone` (`alone_iff`);
* the core's `Relabel.EquivariantChoice.untied` gives `tied_not_served`
  (`tied_not_served_by_core`), and `Relabel.EquivariantChoice.withholds_of_full_tie` gives
  `all_tied_forces_withholding` (`all_tied_forces_withholding_by_core`);
* the core's `Relabel.alone_equivariant` and `Relabel.alone_single` make serving the center that
  holds an entry alone a rule treating the centers alike, the search over `Fin n` being
  `PluralRecords.pick`; with `Relabel.EquivariantChoice.untied` this gives `servable_iff_untied`
  (`servable_iff_untied_by_core`);
* the core's `Relabel.EquivariantValue.tied`, `full_tie` and `const` give `tied_equal_weight`,
  `full_tie_equal_weights` and `uniform_alike`, and `Relabel.EquivariantValue.level` with
  `Relabel.Equivariant.none_of_full_tie` gives `point_mass_not_alike_at_tie` (each `_by_core`).

The core states these for any options with decided equality and entries of any kind, as
relations: a selection through the model singles out exactly the options the model separates
(`Relabel.singled_iff_untied`), with no search. `PluralRecords`' and `TieBreaking`'s definitions
and statements are unchanged.
-/

namespace Becoming.SelectionRelabelCorrespondence

open PluralRecords TieBreaking

theorem transpose_eq_swap {n : Nat} (a b k : Fin n) : transpose a b k = Relabel.swap a b k := rfl

/-- A rule treats the centers alike exactly when it is a choice through the model. -/
theorem treatsAlike_iff {n : Nat} (rule : Rule n) :
    TreatsAlike rule ↔ Relabel.EquivariantChoice rule :=
  Iff.rfl

/-- A lottery treats the centers alike exactly when its weights are through the model and its
withholding weight does not change. -/
theorem lotteryAlike_iff {n : Nat} (lot : Lottery n) :
    LotteryAlike lot ↔ Relabel.EquivariantValue (fun r i => (lot r).serve i) ∧
      ∀ (r r' : Record n) (a b : Fin n), (∀ k, r' k = r (transpose a b k)) →
        (lot r').withhold = (lot r).withhold :=
  ⟨fun alike => ⟨fun r r' a b relabel => (alike r r' a b relabel).1,
     fun r r' a b relabel => (alike r r' a b relabel).2⟩,
   fun both r r' a b relabel => ⟨both.1 r r' a b relabel, both.2 r r' a b relabel⟩⟩

theorem alone_iff {n : Nat} (v : Nat) (r : Record n) (i : Fin n) :
    PluralRecords.Alone v r i ↔ Relabel.Alone v r i :=
  Iff.rfl

theorem tied_not_served_by_core {n : Nat} (rule : Rule n) (alike : TreatsAlike rule)
    (r : Record n) (k j : Fin n) (hjk : j ≠ k) (tie : r j = r k) : rule r ≠ some k :=
  fun served => Relabel.EquivariantChoice.untied alike served j hjk tie

theorem first_lt {n : Nat} (two : 2 ≤ n) : 0 < n :=
  Nat.lt_of_lt_of_le (Nat.zero_lt_succ 1) two

theorem all_tied_forces_withholding_by_core {n : Nat} (rule : Rule n) (alike : TreatsAlike rule)
    (r : Record n) (two : 2 ≤ n) (tied : ∀ i j, r i = r j) : rule r = none :=
  match fin_other two ⟨0, first_lt two⟩ with
  | ⟨_, differ⟩ => Relabel.EquivariantChoice.withholds_of_full_tie alike differ tied

/-- **`servable_iff_untied` from the core**: the core's laws of what is singled out, with
`PluralRecords.pick` finding the center that holds the entry alone. -/
theorem servable_iff_untied_by_core {n : Nat} (r : Record n) (k : Fin n) :
    (∃ rule : Rule n, TreatsAlike rule ∧ rule r = some k) ↔ ∀ j, j ≠ k → r j ≠ r k :=
  ⟨fun ⟨_, alike, served⟩ => Relabel.EquivariantChoice.untied alike served,
   fun untied => ⟨fun r' => pick (PluralRecords.Alone (r k) r'),
     pick_alike (PluralRecords.Alone (r k)) (fun _ _ _ first second => Relabel.alone_single first second)
       (Relabel.alone_equivariant (r k)),
     pick_unique (PluralRecords.Alone (r k) r) (fun _ _ first second => Relabel.alone_single first second)
       ⟨rfl, untied⟩⟩⟩

theorem tied_equal_weight_by_core {n : Nat} (lot : Lottery n) (alike : LotteryAlike lot)
    (r : Record n) (a b : Fin n) (tie : r a = r b) : (lot r).serve a = (lot r).serve b :=
  Relabel.EquivariantValue.tied ((lotteryAlike_iff lot).mp alike).1 tie

theorem full_tie_equal_weights_by_core {n : Nat} (lot : Lottery n) (alike : LotteryAlike lot)
    (r : Record n) (tied : ∀ i j, r i = r j) (i j : Fin n) :
    (lot r).serve i = (lot r).serve j :=
  Relabel.EquivariantValue.full_tie ((lotteryAlike_iff lot).mp alike).1 tied i j

theorem uniform_alike_by_core (n : Nat) : LotteryAlike (uniform n) :=
  (lotteryAlike_iff (uniform n)).mpr ⟨Relabel.EquivariantValue.const 1, fun _ _ _ _ _ => rfl⟩

/-- The point mass weighs a center one exactly where the rule chooses it. -/
theorem pointMass_one {n : Nat} {rule : Rule n} {r : Record n} {i : Fin n}
    (one : (pointMass rule r).serve i = 1) : rule r = some i :=
  match decEq (rule r) (some i) with
  | isTrue chosen => chosen
  | isFalse other => absurd ((if_neg other).symm.trans one) (fun zero => one_ne_zero' zero.symm)

/-- **`point_mass_not_alike_at_tie` from the core**: the centers weighted one form a selection
through the model that selects at most one, so at a full tie it selects none. -/
theorem point_mass_not_alike_at_tie_by_core {n : Nat} (rule : Rule n)
    (alike : LotteryAlike (pointMass rule)) (two : 2 ≤ n) (r : Record n)
    (tied : ∀ i j, r i = r j) : rule r = none :=
  match fin_other two ⟨0, first_lt two⟩, chosen : rule r with
  | _, none => rfl
  | ⟨_, differ⟩, some k =>
    absurd (show (pointMass rule r).serve k = 1 from if_pos chosen)
      (Relabel.Equivariant.none_of_full_tie
        (Relabel.EquivariantValue.level ((lotteryAlike_iff _).mp alike).1 1)
        (fun _ _ first second => Option.some.inj ((pointMass_one first).symm.trans
          (pointMass_one second)))
        differ tied k)

end Becoming.SelectionRelabelCorrespondence
