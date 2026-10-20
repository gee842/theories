#!/usr/bin/env python3
"""R37c: state the tally-level agreement of enclosed and finite worlds once
(`World.enclosed_iff_finite_tally`, in Becoming/Counting.lean) and read the decided
`enclosed_iff_finite_counting_under` and the counted `enclosed_iff_finite_counting_under_counted`
from it, statements unchanged.

usage: python3 -B tally_lemma.py PACKAGE_DIR
"""
import sys
from pathlib import Path

LEMMA = '''/-- **The tally conditions of worlds enclosed from some step on and of finite worlds agree under
a selection exactly when it bounds change and binds counting**, over any class of properties of
the counts that holds the pointwise ones: there a change bound from some step is one from the
first step (`ChangeBound.from_zero`) and bounds the count. Where the selection does not bound
change, a count growing without end meets the enclosed condition and not the finite one; where it
bounds change without binding counting, one relatum arising from none meets the enclosed
condition and not that nothing arises across a step at which nothing is active. -/
theorem enclosed_iff_finite_tally (S : Premise → Bool)
    {Props : ((Nat → Nat) → (Nat → Nat) → (Nat → Nat) → Prop) → Prop}
    (pointwise : ∀ Q, Pointwise Q → Props Q) :
    (∀ Q, Props Q →
      ((∀ n c a, Tally n c a → (BindsCounting S → ∀ t, 0 < a t → 0 < n t) →
          (BoundsChange S → ∃ T B, ChangeBound T B n c a ∧
            ∀ t, T ≤ t → 0 < a t → 0 < n t) → Q n c a) ↔
        ∀ n c a, Tally n c a → (∃ M, ∀ t, n t ≤ M) →
          (BindsCounting S ∨ BoundsChange S → ∀ t, 0 < a t → 0 < n t) →
          (BoundsChange S → ∃ B, ChangeBound 0 B n c a) → Q n c a)) ↔
      BoundsChange S ∧ BindsCounting S :=
  ⟨fun law =>
    have growing : ¬ ¬ BoundsChange S := fun free =>
      match (law _ (pointwise (fun n (_ _ : Nat → Nat) => ∃ M, ∀ t, n t ≤ M)
          fun same ⟨M, bounded⟩ => ⟨M, fun t => Nat.le_trans (Nat.le_of_eq (same t).1.symm)
            (bounded t)⟩)).mpr (fun _ _ _ _ bounded _ _ => bounded)
          (fun t => t + 1) (fun _ => 0) (fun _ => 1) (fun t => ⟨t + 1, rfl, rfl⟩)
          (fun _ _ _ => Nat.succ_pos _) (fun bounds => absurd bounds free) with
      | ⟨M, bounded⟩ => Nat.lt_irrefl M (bounded M)
    have arising : BoundsChange S → ¬ ¬ BindsCounting S := fun bounds free =>
      Nat.lt_irrefl 0 ((law _ (pointwise (fun n (_ : Nat → Nat) a => ∀ t, 0 < a t → 0 < n t)
          fun same law t pos => Nat.lt_of_lt_of_le (law t (Nat.lt_of_lt_of_le pos
            (Nat.le_of_eq (same t).2.2.symm))) (Nat.le_of_eq (same t).1))).mpr
          (fun _ _ _ _ _ quiet _ => quiet (.inr bounds)) _ _ _ Queue.lone_tally
        (fun binds => absurd binds free)
        (fun _ => ⟨1, 1, Queue.lone_settles, fun t later pos => match t, later, pos with
          | 0, later, _ => absurd later (Nat.not_succ_le_zero 0)
          | _ + 1, _, pos => absurd pos (Nat.lt_irrefl 0)⟩)
        0 Nat.zero_lt_one)
    match hb : S .balanced, he : S .embodied, hd : S .dissipative, ha : S .acting,
      ht : S .taking with
    | true, true, true, true, _ => ⟨⟨hb, he, hd⟩, ⟨hb, he, .inl ha⟩⟩
    | true, true, true, false, true => ⟨⟨hb, he, hd⟩, ⟨hb, he, .inr ⟨ht, hd⟩⟩⟩
    | true, true, true, false, false => (arising ⟨hb, he, hd⟩ fun
        | ⟨_, _, .inl acting⟩ => nomatch ha.symm.trans acting
        | ⟨_, _, .inr ⟨taking, _⟩⟩ => nomatch ht.symm.trans taking).elim
    | false, _, _, _, _ => (growing fun bounds => nomatch hb.symm.trans bounds.1).elim
    | true, false, _, _, _ => (growing fun bounds => nomatch he.symm.trans bounds.2.1).elim
    | true, true, false, _, _ => (growing fun bounds => nomatch hd.symm.trans bounds.2.2).elim,
   fun ⟨bounds, binds⟩ _ _ =>
    ⟨fun law n c a tally _ quiet bounded => law n c a tally (fun _ => quiet (.inl binds))
        fun _ => match bounded bounds with
          | ⟨_, bound⟩ => ⟨0, _, bound, fun t _ => quiet (.inl binds) t⟩,
      fun law n c a tally quiet bounded => match bounded bounds with
        | ⟨_, _, bound, _⟩ => law n c a tally ⟨_, fun t => Nat.le_trans (Nat.le_add_right _ _)
            (bound.from_zero t (Nat.zero_le t))⟩ (fun _ => quiet binds)
            (fun _ => ⟨_, bound.from_zero⟩)⟩⟩

'''

DECIDED_BODY = '''  Iff.trans ⟨fun law Q pointwise => (enclosed_counting_under S pointwise).trans
      ((law Q pointwise).trans (finite_counting_under S pointwise).symm),
    fun law Q pointwise => (enclosed_counting_under S pointwise).symm.trans
      ((law Q pointwise).trans (finite_counting_under S pointwise))⟩
    (enclosed_iff_finite_tally S fun _ => id)
'''

COUNTED_BODY = '''  Iff.trans ⟨fun law Q _ => (enclosed_counting_under_counted S (Q := Q)).trans
      ((law Q).trans (finite_counting_under_counted S).symm),
    fun law Q => (enclosed_counting_under_counted S (Q := Q)).symm.trans
      ((law Q trivial).trans (finite_counting_under_counted S))⟩
    (enclosed_iff_finite_tally S (Props := fun _ => True) fun _ _ => trivial)
'''


def replace_body(text, name, body, before=""):
    start = text.index(f"theorem {name} ")
    head = text.rindex("/--", 0, start)
    stop = text.index(":=\n", start) + 3
    end = text.index("\n\n", stop) + 1
    return text[:head] + before + text[head:stop] + body + text[end:]


package = Path(sys.argv[1]) / "Becoming"
counting = package / "Counting.lean"
counting.write_text(replace_body(counting.read_text(), "enclosed_iff_finite_counting_under",
                                 DECIDED_BODY, LEMMA))
binding = package / "CensusBinding.lean"
binding.write_text(replace_body(binding.read_text(), "enclosed_iff_finite_counting_under_counted",
                                COUNTED_BODY))
