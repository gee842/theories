import Becoming.Horizon
import PrefixSafety

/-!
# Prefix safety as an instance of what a finite history refutes

`PrefixSafety` classifies properties of infinite traces by their finite prefixes. A trace is the
run of `Becoming.Sequences.process`, the process whose runs are all sequences, and the prefix
order is the core's `Run.AgreeUpTo` there (`samePrefix_iff_agree`). Then:
* finite refutability is the core's `Refutable` (`finiteRefutable_iff_refutable`), and the prefix
  closure is adherence (`prefixClosure_iff_adheres`);
* with Lean's classical reasoning supplying stability, the core's `Refutable.not_not` gives that
  a finitely refutable property holds wherever its prefix closure does
  (`holds_of_prefixClosure_by_core`), and `Refutable.adheres_least` that the prefix closure is
  below every finitely refutable superset (`prefixClosure_least_by_core`); the core states these
  up to double negation, which is what holds with no classical step;
* recurrence and the termination event are not finitely refutable by the core's
  `Sequences.recurs_not_refutable` and `Sequences.eventually_not_refutable`
  (`recurrence_not_finiteRefutable_by_core`, `terminationEvent_not_finiteRefutable_by_core`);
* classical reasoning gives the core's `Markov`, so a property given by prefix tests is
  finitely refutable by the core's `refutable_passes` (`boundary_closed_by_core`); the core shows
  that asked of every process this needs exactly Markov's principle.

`PrefixSafety`'s definitions and statements are unchanged.
-/

namespace Becoming.PrefixSafetyCorrespondence

open CompletionWarrant.PrefixSafety

universe u

variable {A : Type u}

theorem samePrefix_iff_agree {n : Nat} {a b : Trace A} :
    SamePrefix n a b ↔ (Sequences.run a).AgreeUpTo n (Sequences.run b) :=
  (Sequences.agree_iff (h := n) (r := Sequences.run a) (r' := Sequences.run b)).symm

/-- **Finite refutability is the core's refutability on the runs of the sequences.** -/
theorem finiteRefutable_iff_refutable {K : Property A} :
    FiniteRefutable K ↔ Refutable (fun r : Run (Sequences.process A) => K r.act) :=
  ⟨fun refutable r outside => match refutable r.act outside with
    | ⟨n, blocked⟩ => ⟨n, fun r' agree => blocked r'.act (Sequences.agree_iff.mp agree)⟩,
   fun refutable a outside => match refutable (Sequences.run a) outside with
    | ⟨n, blocked⟩ => ⟨n, fun b same => blocked (Sequences.run b) (samePrefix_iff_agree.mp same)⟩⟩

/-- **The prefix closure is adherence.** -/
theorem prefixClosure_iff_adheres {K : Property A} {a : Trace A} :
    PrefixClosure K a ↔ Adheres (fun r : Run (Sequences.process A) => K r.act) (Sequences.run a) :=
  ⟨fun closure n => match closure n with
    | ⟨b, inside, same⟩ => ⟨Sequences.run b, inside, samePrefix_iff_agree.mp same⟩,
   fun adheres n => match adheres n with
    | ⟨r', inside, agree⟩ => ⟨r'.act, inside, Sequences.agree_iff.mp agree⟩⟩

/-- A finitely refutable property holds wherever its prefix closure does: the core gives it up to
double negation, classical reasoning removes the double negation. -/
theorem holds_of_prefixClosure_by_core {K : Property A} (refutable : FiniteRefutable K)
    {a : Trace A} (closure : PrefixClosure K a) : K a :=
  Classical.byContradiction
    ((finiteRefutable_iff_refutable.mp refutable).not_not (prefixClosure_iff_adheres.mp closure))

/-- The prefix closure is below every finitely refutable superset. -/
theorem prefixClosure_least_by_core {K L : Property A} (refutable : FiniteRefutable L)
    (sub : ∀ a, K a → L a) {a : Trace A} (closure : PrefixClosure K a) : L a :=
  Classical.byContradiction
    ((finiteRefutable_iff_refutable.mp refutable).adheres_least (fun r => sub r.act)
      (prefixClosure_iff_adheres.mp closure))

theorem recurrence_not_finiteRefutable_by_core : ¬ FiniteRefutable Recurs :=
  fun refutable => Sequences.recurs_not_refutable (finiteRefutable_iff_refutable.mp refutable)

theorem terminationEvent_not_finiteRefutable_by_core : ¬ FiniteRefutable EventuallyTrue :=
  fun refutable => Sequences.eventually_not_refutable (finiteRefutable_iff_refutable.mp refutable)

/-- Classical reasoning gives the core's Markov principle. -/
theorem markov_classical : Markov :=
  fun s notFalse => Classical.byContradiction fun none =>
    notFalse fun n => match e : s n with
      | true => absurd ⟨n, e⟩ none
      | false => rfl

/-- **`boundary_closed` from the core.** A property given by prefix tests is finitely refutable:
the core's `refutable_passes`, with the tests decided classically and Markov's principle from
classical reasoning. -/
theorem boundary_closed_by_core (H : Nat → Trace A → Prop)
    (hlocal : ∀ n a b, SamePrefix n a b → H n a → H n b) : FiniteRefutable (AllPrefixesIn H) := by
  classical
  let fails : Nat → Run (Sequences.process A) → Bool := fun n r => decide (¬ H n r.act)
  have byPrefixes : ByPrefixes fails := fun n r r' agree => by
    have same : SamePrefix n r.act r'.act :=
      fun i before => Sequences.agree_iff.mp agree i (Nat.lt_trans before (Nat.lt_succ_self n))
    have forth := hlocal n r.act r'.act same
    have back := hlocal n r'.act r.act (fun i before => (same i before).symm)
    by_cases holds : H n r.act
    · simp [fails, holds, forth holds]
    · have fails' : ¬ H n r'.act := fun h' => holds (back h')
      simp [fails, holds, fails']
  have passes_iff : ∀ r, Passes fails r ↔ AllPrefixesIn H r.act := fun r =>
    ⟨fun passes n => by simpa [fails] using passes n, fun all n => by simpa [fails] using all n⟩
  refine finiteRefutable_iff_refutable.mpr fun r outside => ?_
  obtain ⟨h, blocked⟩ := refutable_passes markov_classical byPrefixes r
    (fun passes => outside ((passes_iff r).mp passes))
  exact ⟨h, fun r' agree inside => blocked r' agree ((passes_iff r').mpr inside)⟩

end Becoming.PrefixSafetyCorrespondence
