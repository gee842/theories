import Becoming.RuleNarrowingProcesses

/-!
# Learning a rule as narrowed belief: laws through `StandardsBridge`'s list facts

`Becoming.RuleNarrowingProcesses` reads `StandardsBridge`'s learning as a belief over rules narrowed
by `After` on the pure observation process (`narrowed`, `mem_learn_iff`) and states its concrete
results there with empty axiom reports. `StandardsBridge`'s general laws of filtering are proved with
`simp` and classical reasoning; this module states them of the narrowed belief and proves them
through those theorems.

* **One narrowing.** After observing `b` at `q`, the belief holds exactly the rules it held that give
  `b` at `q` (`narrow_once_iff`).
* **Narrowing by a list.** The narrowed belief holds exactly the rules the belief held that fit every
  observation (`narrowed_iff_fits`); a rule the belief held and the narrowing dropped has an
  observation it contradicts (`dropped_has_counterevidence`); observing the same thing twice narrows
  as observing it once (`repeated_observation_idle`).
* **Faithful re-encoding.** Narrowing re-encoded rules by re-encoded observations holds exactly the
  re-encodings of what the original narrowing holds (`narrowing_transport`).
* **Faithful observation of the actual rule.** From the four rules on two cases, whatever the belief
  narrowed by observations of the actual rule settles is the actual rule's value
  (`full_repertoire_settles_actual`).

No ethical predicate or ranking occurs. The axioms are inherited from the periphery theorems used:
`propext` from `StandardsBridge.mem_revise`; `propext` and `Quot.sound` from
`StandardsBridge.mem_learn`, `StandardsBridge.repetition_does_not_change_candidates` and
`StandardsBridge.learning_transport`; `propext`, `Classical.choice` and `Quot.sound` from
`StandardsBridge.eliminated_rule_has_counterevidence` and
`StandardsBridge.full_bool_repertoire_correct`. No axiom is added here.
-/

namespace Becoming

open Generative Generative.InquirySufficiency

namespace RuleNarrowingProcessesInherited

open RuleNarrowingProcesses

variable {Q : Type}

/-- **One narrowing.** After observing `b` at `q`, the belief in a list holds exactly the rules of the
list that give `b` at `q`. -/
theorem narrow_once_iff (hs : List (StandardsBridge.Rule Q)) (q : Q) (b : Bool)
    (h : StandardsBridge.Rule Q) :
    After observe sense (· ∈ hs) q (encode b) h ↔ h ∈ hs ∧ h q = b :=
  (revise_is_after hs q b h).symm.trans (StandardsBridge.mem_revise h hs (q, b))

/-- **The narrowed belief holds exactly the rules the belief held that fit every observation.** -/
theorem narrowed_iff_fits (hs : List (StandardsBridge.Rule Q))
    (e : List (StandardsBridge.Observation Q)) (h : StandardsBridge.Rule Q) :
    narrowed (· ∈ hs) e h ↔ h ∈ hs ∧ StandardsBridge.Fits h e :=
  (mem_learn_iff e hs h).symm.trans (StandardsBridge.mem_learn h hs e)

/-- **A rule the belief held and the narrowing dropped contradicts some observation.** -/
theorem dropped_has_counterevidence {hs : List (StandardsBridge.Rule Q)}
    {e : List (StandardsBridge.Observation Q)} {h : StandardsBridge.Rule Q} (held : h ∈ hs)
    (dropped : ¬ narrowed (· ∈ hs) e h) : ∃ o, o ∈ e ∧ h o.1 ≠ o.2 :=
  match StandardsBridge.eliminated_rule_has_counterevidence h hs e held
      (fun m => dropped ((mem_learn_iff e hs h).mp m)) with
  | ⟨o, m, ne⟩ => ⟨o, m, ne⟩

/-- **Observing the same thing twice narrows as observing it once.** -/
theorem repeated_observation_idle (hs : List (StandardsBridge.Rule Q))
    (o : StandardsBridge.Observation Q) (h : StandardsBridge.Rule Q) :
    narrowed (· ∈ hs) [o, o] h ↔ narrowed (· ∈ hs) [o] h :=
  (mem_learn_iff [o, o] hs h).symm.trans
    ((Iff.of_eq (congrArg (h ∈ ·)
        (StandardsBridge.repetition_does_not_change_candidates hs o))).trans
      (mem_learn_iff [o] hs h))

/-- **Narrowing re-encoded rules by re-encoded observations holds exactly the re-encodings of what
the original narrowing holds**, where decoding inverts encoding. -/
theorem narrowing_transport {R : Type} (hs : List (StandardsBridge.Rule Q))
    (e : List (StandardsBridge.Observation Q)) (enc : Q → R) (dec : R → Q)
    (faithful : ∀ q, dec (enc q) = q) (g : StandardsBridge.Rule R) :
    narrowed (· ∈ hs.map (StandardsBridge.transport dec)) (e.map (fun o => (enc o.1, o.2))) g ↔
      g ∈ (StandardsBridge.learn hs e).map (StandardsBridge.transport dec) :=
  (mem_learn_iff _ _ g).symm.trans
    (Iff.of_eq (congrArg (g ∈ ·) (StandardsBridge.learning_transport hs e enc dec faithful)))

/-- **What faithful observation of the actual rule settles is the actual rule's value.** From the
four rules on two cases, whatever the belief narrowed by observations of `actual` settles at a
question is `actual`'s value there. -/
theorem full_repertoire_settles_actual (actual : StandardsBridge.Rule Bool) (fuel : Nat)
    (qs : List Bool) {q b : Bool}
    (settled : Settles (narrowed (· ∈ StandardsBridge.repertoire)
      (StandardsBridge.acquire actual fuel qs)) q b) : b = actual q :=
  StandardsBridge.full_bool_repertoire_correct actual fuel qs q b
    (answer_of_settles (settles_learn_iff.mpr settled))

end RuleNarrowingProcessesInherited

end Becoming
