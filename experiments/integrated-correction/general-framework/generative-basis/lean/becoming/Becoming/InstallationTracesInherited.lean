import Becoming.InstallationTraces

/-!
# The installation of `EffectiveCommand` as a process: the laws of its steps that inherit axioms

`InstallationTraces` reads the installation of `EffectiveCommand` as a process
(`InstallationTraces.installation`): a move is an inquiry with its answer, an issue, a delivery
along a route or an enactment, and the protocol is a trace of issuing, delivering and enacting
(`InstallationTraces.protocol_iff`). This module states, of that process, the module's laws of single
steps, whose proofs there use `propext`, `Quot.sound` or `Classical.choice`.

* **What a move needs.** An unsigned configuration has no issuing move (`unsigned_no_issue`), nor
  one whose credential is not the current authority (`stale_no_issue`); an undelivered
  configuration has no enacting move (`undelivered_no_enact`), nor one whose credential is not the
  current authority (`revoked_no_enact`).
* **Reserve and spending are conserved.** Every move either leaves the configuration as it is or
  spends through `EffectiveCommand.spend`, keeping what it leaves of reserve and spending
  (`move_spends`). So the reserve plus what is spent is invariant under every move
  (`conserved_invariant`), and every trace ends with the reserve plus what is spent with which it
  began (`conserved_trace`).
* **The protocol completes where its conditions hold.** From a signed configuration with current
  credential, the route open, a reserve of three and three units of time left, the installation has
  a trace of the protocol ending completed, delivered and issued, with three spent, three units of
  time used and the authority unchanged (`protocol_completes`).

No ethical predicate or ranking occurs. Inherited axioms: `propext` from
`EffectiveCommand.unsigned_cannot_issue` and `EffectiveCommand.undelivered_cannot_enact`; `propext`
and `Quot.sound` from `EffectiveCommand.stale_authority_cannot_issue`,
`EffectiveCommand.revoked_before_execution` and `EffectiveCommand.spend_conserves`; `propext`,
`Quot.sound` and `Classical.choice` from `EffectiveCommand.protocol_exact`.
-/

namespace Becoming

open Generative

namespace InstallationTracesInherited

open InstallationTraces

/-! ## What a move needs -/

/-- **An unsigned configuration has no issuing move.** -/
theorem unsigned_no_issue {s : EffectiveCommand.State} (unsigned : s.signed = false) :
    ¬ Enabled installation s .issue :=
  fun ⟨_, h⟩ => none_ne_some ((EffectiveCommand.unsigned_cannot_issue s unsigned).symm.trans h)

/-- **A configuration whose credential is not the current authority has no issuing move.** -/
theorem stale_no_issue {s : EffectiveCommand.State} (stale : s.credential ≠ s.authority) :
    ¬ Enabled installation s .issue :=
  fun ⟨_, h⟩ => none_ne_some ((EffectiveCommand.stale_authority_cannot_issue s stale).symm.trans h)

/-- **An undelivered configuration has no enacting move.** -/
theorem undelivered_no_enact {s : EffectiveCommand.State} (undelivered : s.delivered = false) :
    ¬ Enabled installation s .enact :=
  fun ⟨_, h⟩ => none_ne_some ((EffectiveCommand.undelivered_cannot_enact s undelivered).symm.trans h)

/-- **A configuration whose credential is not the current authority has no enacting move.** -/
theorem revoked_no_enact {s : EffectiveCommand.State} (revoked : s.credential ≠ s.authority) :
    ¬ Enabled installation s .enact :=
  fun ⟨_, h⟩ => none_ne_some ((EffectiveCommand.revoked_before_execution s revoked).symm.trans h)

/-! ## Reserve and spending are conserved -/

/-- A step guarded by a condition is present only where the condition holds and the step is. -/
theorem ite_some {α : Type} {x : Option α} {t : α} :
    ∀ {c : Bool}, (if c = true then x else none) = some t → x = some t
  | true, h => h
  | false, h => nomatch h

/-- A step that spends and then records keeps what the spending leaves. -/
theorem recorded {s t : EffectiveCommand.State} {c d : Nat} {f : EffectiveCommand.State → EffectiveCommand.State}
    (keeps : ∀ u, (f u).reserve = u.reserve ∧ (f u).spent = u.spent)
    (h : (EffectiveCommand.spend c d s >>= fun u => pure (f u)) = some t) :
    ∃ c d u, EffectiveCommand.spend c d s = some u ∧ t.reserve = u.reserve ∧ t.spent = u.spent :=
  match (bind_eq_some _ _ _).mp h with
  | ⟨u, spent, made⟩ =>
    have same : f u = t := Option.some.inj made
    ⟨c, d, u, spent, (congrArg EffectiveCommand.State.reserve same).symm.trans (keeps u).1,
      (congrArg EffectiveCommand.State.spent same).symm.trans (keeps u).2⟩

/-- **Every move of the installation leaves the configuration as it is or spends, keeping what the
spending leaves of reserve and spending.** -/
theorem move_spends : ∀ (m : Move) {s t : EffectiveCommand.State}, installation.step s m t →
    t = s ∨ ∃ c d u, EffectiveCommand.spend c d s = some u ∧ t.reserve = u.reserve ∧ t.spent = u.spent
  | .probe .none _, _, _, h => .inl (congrArg Prod.snd (Option.some.inj h)).symm
  | .probe .route o, s, t, h =>
    match (bind_eq_some _ _ _).mp
        (h : (EffectiveCommand.spend 1 1 s >>= fun u => pure (s.openRoute, u)) = some (o, t)) with
    | ⟨u, spent, made⟩ =>
      have same : u = t := congrArg Prod.snd (Option.some.inj made)
      .inr ⟨1, 1, u, spent, congrArg EffectiveCommand.State.reserve same.symm,
        congrArg EffectiveCommand.State.spent same.symm⟩
  | .probe .slow o, s, t, h =>
    match (bind_eq_some _ _ _).mp
        (h : (EffectiveCommand.spend 1 3 s >>= fun u => pure (s.openRoute, u)) = some (o, t)) with
    | ⟨u, spent, made⟩ =>
      have same : u = t := congrArg Prod.snd (Option.some.inj made)
      .inr ⟨1, 3, u, spent, congrArg EffectiveCommand.State.reserve same.symm,
        congrArg EffectiveCommand.State.spent same.symm⟩
  | .issue, s, _, h => .inr (recorded (f := fun u => {u with issued := true})
      (fun _ => ⟨rfl, rfl⟩) (ite_some (c := s.signed && (s.credential == s.authority)) h))
  | .deliver r, s, _, h => .inr (recorded (f := fun u => {u with delivered := true})
      (fun _ => ⟨rfl, rfl⟩) (ite_some (c := s.issued && (r == s.openRoute)) h))
  | .enact, s, _, h => .inr (recorded
      (f := fun u => {u with
        completed := true
        running := s.requested != .shutdown
        generation := s.generation + if s.requested == .replace then 1 else 0
        version := s.version + if s.requested == .update then 1 else 0})
      (fun _ => ⟨rfl, rfl⟩)
      (ite_some (c := s.delivered && s.signed && (s.credential == s.authority)) h))

/-- **The reserve plus what is spent is invariant under every move of the installation.** -/
theorem conserved_invariant (c : Nat) :
    Invariant installation (fun s => s.reserve + s.spent = c) :=
  fun _ m _ st held => match move_spends m st with
    | .inl same => same ▸ held
    | .inr ⟨_, _, u, spent, reserve, spending⟩ =>
      ((congrArg (· + _) reserve).trans (congrArg (u.reserve + ·) spending)).trans
        ((EffectiveCommand.spend_conserves spent).1.trans held)

/-- **Every trace of the installation ends with the reserve plus what is spent with which it
began.** -/
theorem conserved_trace {s t : EffectiveCommand.State} {ms : List Move}
    (tr : Trace installation s ms t) : t.reserve + t.spent = s.reserve + s.spent :=
  (conserved_invariant (s.reserve + s.spent)).trace tr rfl

/-! ## The protocol completes where its conditions hold -/

/-- **From a signed configuration with current credential, the route open, a reserve of three and
three units of time left, the installation has a trace of the protocol ending completed, delivered
and issued, with three spent, three units of time used and the authority unchanged.** -/
theorem protocol_completes (s : EffectiveCommand.State) (r : Bool)
    (signed : s.signed = true) (current : s.credential = s.authority) (route : r = s.openRoute)
    (funded : 3 ≤ s.reserve) (timely : s.time + 3 ≤ s.deadline) :
    ∃ t, Trace installation s (protocolMoves r) t ∧ t.completed = true ∧ t.delivered = true ∧
      t.issued = true ∧ t.reserve + 3 = s.reserve ∧ t.time = s.time + 3 ∧
      t.spent = s.spent + 3 ∧ t.authority = s.authority :=
  match EffectiveCommand.protocol_exact s r signed current route funded timely with
  | ⟨t, ran, rest⟩ => ⟨t, (protocol_iff r s t).mp ran, rest⟩

end InstallationTracesInherited

end Becoming
