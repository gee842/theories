import Becoming.Readout
import Becoming.LearnableRuns

/-!
# Partial readout: reading a feature through a map on a domain, or staying silent

`Becoming.Readout` asks when a feature `f : S → V` is read off a map `π : S → K` everywhere
(`Readout.Decodes`). Here a reading may stay silent: a partial decoder `answer : K → Option V`
proposes a value or none, and is judged only on a domain `D` of configurations. It is **sound
within `D`** when every value it proposes there is the feature's (`SoundWithin`), **exact within
`D`** when it proposes the feature's value at every configuration of `D` (`ExactWithin`), and the
feature is **lumped within `D`** when configurations of `D` merged by the map have one feature
value (`LumpedWithin`). On the whole domain with a decoder that never stays silent, exactness is
the core's `Readout.Decodes` and lumping is `Learning.Lumped` (`exactWithin_univ_iff`,
`lumpedWithin_univ_iff`). This module states the laws of such readings, with no premise beyond
what each theorem names, and reads them on the prefixes of runs (board item F3Q, 18 October 2026:
the content of `KnowledgeCorrespondence`, 6 October, and of the joins `ExactRecordRuns` and
`ExactRecordRunsInherited`, 17 October).

* **Exact is sound, and exact needs lumping** (`ExactWithin.sound`, `ExactWithin.lumped`). With a
  supplied section of the map over the domain (`SectionWithin`: a configuration of the domain for
  each value the map takes on it, and for no other value), some exact reading exists exactly where
  the feature is lumped (`exact_exists_iff`), the reading being the feature at the section
  (`ExactWithin.ofSection`). No choice is used: the section is the datum that finds a
  configuration behind a value, which a decoder needs in general.
* **A sound reading stays silent where the map merges two feature values** (`SoundWithin.silent`),
  soundness holds on every smaller domain (`SoundWithin.mono`), lumping survives a finer map
  (`LumpedWithin.finer`), and exactness survives a faithfully read-back retention
  (`ExactWithin.retained`). Staying silent everywhere is sound and, on an inhabited domain, not
  exact (`silent_sound`, `silent_not_exact`). A claim that holds is safe whatever asserts it
  (`safe_of_holds`): safety of a fixed true claim does not tell a derivation from a guess.
* **A reference reading fixes orientation.** In the channel model a bit passes through an
  orientation that may reverse it (`Channel`, `signal`). The signal alone does not lump the bit
  (`signal_not_lumped`), so no reading of it is exact (`signal_no_exact`) and every sound reading
  of it stays silent on both values (`signal_sound_silent`); paired with a reference reading of the
  orientation it is read exactly (`paired_exact`), also when only their parity is kept
  (`parity_exact`). The direct reading is exact on the unreversed channels and not sound on all
  (`direct_exact_unreversed`, `direct_not_sound`), though right on one of them
  (`direct_right_once`); reading a negated copy back is exact (`negated_exact`).
* **On runs.** The prefix a map leaves along a run before step `t` (`prefixBefore`) is read for
  the feature at `t` (`featureAt`); every law above holds of these readings (`Runs.exact_sound`,
  `Runs.exact_lumped`, `Runs.sound_silent`, `Runs.sound_mono`, `Runs.finer_lumped`,
  `Runs.retained_exact`, `Runs.silent_sound`, `Runs.silent_not_exact`, `Runs.exact_exists_iff`),
  and, along the runs of a determined law, an extrapolation rests on the feature from `T` exactly
  where it reads the prefix exactly at every step from `T` (`Runs.exact_iff_predictsFrom`, through
  `LearnableRuns.PredictsFrom`).

The channel is a supplied countermodel, not a definition of knowledge; domain adequacy and uptake
are not claimed. No ethical predicate or ranking occurs, and every declaration has an empty axiom
report.
-/

namespace Becoming

open Generative

universe u v w x

namespace PartialReadout

section Laws

variable {S : Type u} {K : Type v} {V : Type w}

/-- Every value `answer` proposes at a configuration of `D` is the feature's. -/
def SoundWithin (D : S → Prop) (π : S → K) (f : S → V) (answer : K → Option V) : Prop :=
  ∀ s, D s → ∀ v, answer (π s) = some v → v = f s

/-- `answer` proposes the feature's value at every configuration of `D`. -/
def ExactWithin (D : S → Prop) (π : S → K) (f : S → V) (answer : K → Option V) : Prop :=
  ∀ s, D s → answer (π s) = some (f s)

/-- Configurations of `D` the map merges have one feature value. -/
def LumpedWithin (D : S → Prop) (π : S → K) (f : S → V) : Prop :=
  ∀ s s', D s → D s' → π s = π s' → f s = f s'

/-- **Exact is sound.** -/
theorem ExactWithin.sound {D : S → Prop} {π : S → K} {f : S → V} {answer : K → Option V}
    (exact : ExactWithin D π f answer) : SoundWithin D π f answer :=
  fun s inD _ proposed => Option.some.inj (proposed.symm.trans (exact s inD))

/-- **An exact reading needs the feature lumped by the map.** -/
theorem ExactWithin.lumped {D : S → Prop} {π : S → K} {f : S → V} {answer : K → Option V}
    (exact : ExactWithin D π f answer) : LumpedWithin D π f :=
  fun s s' inD inD' same =>
    Option.some.inj ((exact s inD).symm.trans ((congrArg answer same).trans (exact s' inD')))

/-- On the whole domain, a reading that never stays silent is exact exactly where it decodes. -/
theorem exactWithin_univ_iff {π : S → K} {f : S → V} {g : K → V} :
    ExactWithin (fun _ => True) π f (fun k => some (g k)) ↔ Readout.Decodes π f g :=
  ⟨fun exact s => (Option.some.inj (exact s trivial)).symm,
   fun decodes s _ => congrArg some (decodes s).symm⟩

/-- On the whole domain, lumping within it is the core's lumping. -/
theorem lumpedWithin_univ_iff {π : S → K} {f : S → V} :
    LumpedWithin (fun _ => True) π f ↔ Learning.Lumped π f :=
  ⟨fun lumped s s' same => lumped s s' trivial trivial same,
   fun lumped s s' _ _ same => lumped s s' same⟩

/-- A section of the map over `D`: for a value the map takes on `D`, a configuration of `D` with
that value; for no other value, any configuration. -/
def SectionWithin (D : S → Prop) (π : S → K) (pick : K → Option S) : Prop :=
  (∀ k s, pick k = some s → D s ∧ π s = k) ∧ ∀ s, D s → ∃ s', pick (π s) = some s'

/-- The reading through a section: the feature at the configuration it picks. -/
def throughSection (pick : K → Option S) (f : S → V) (k : K) : Option V :=
  match pick k with
  | none => none
  | some s => some (f s)

/-- **With a section, the reading through it is exact where the feature is lumped.** -/
theorem ExactWithin.ofSection {D : S → Prop} {π : S → K} {f : S → V} {pick : K → Option S}
    (sec : SectionWithin D π pick) (lumped : LumpedWithin D π f) :
    ExactWithin D π f (throughSection pick f) :=
  fun s inD =>
    match sec.2 s inD with
    | ⟨s', picked⟩ =>
      have back := sec.1 (π s) s' picked
      have value : throughSection pick f (π s) = some (f s') := by
        unfold throughSection
        rw [picked]
      value.trans (congrArg some (lumped s' s back.1 inD back.2))

/-- **With a section of the map over the domain, some exact reading exists exactly where the
feature is lumped within it.** -/
theorem exact_exists_iff {D : S → Prop} {π : S → K} {f : S → V} {pick : K → Option S}
    (sec : SectionWithin D π pick) :
    (∃ answer, ExactWithin D π f answer) ↔ LumpedWithin D π f :=
  ⟨fun ⟨_, exact⟩ => exact.lumped, fun lumped => ⟨_, ExactWithin.ofSection sec lumped⟩⟩

/-- **A sound reading stays silent where the map merges two configurations of the domain with
different feature values.** -/
theorem SoundWithin.silent {D : S → Prop} {π : S → K} {f : S → V} {answer : K → Option V}
    (sound : SoundWithin D π f answer) {s s' : S} (inD : D s) (inD' : D s') (same : π s = π s')
    (different : f s ≠ f s') : answer (π s) = none :=
  match proposed : answer (π s) with
  | none => rfl
  | some v =>
    absurd ((sound s inD v proposed).symm.trans
      (sound s' inD' v ((congrArg answer same).symm.trans proposed))) different

/-- **Soundness holds on every smaller domain.** -/
theorem SoundWithin.mono {D D' : S → Prop} {π : S → K} {f : S → V} {answer : K → Option V}
    (sound : SoundWithin D π f answer) (within : ∀ s, D' s → D s) :
    SoundWithin D' π f answer :=
  fun s inD' v proposed => sound s (within s inD') v proposed

/-- **Lumping survives a finer map**, the map read beside a second one. -/
theorem LumpedWithin.finer {K' : Type x} {D : S → Prop} {π : S → K} {f : S → V}
    (lumped : LumpedWithin D π f) (π' : S → K') :
    LumpedWithin D (fun s => (π s, π' s)) f :=
  fun s s' inD inD' same => lumped s s' inD inD' (congrArg Prod.fst same)

/-- **Exactness survives a retention read back faithfully on the domain.** -/
theorem ExactWithin.retained {M : Type x} {D : S → Prop} {π : S → K} {f : S → V}
    {answer : K → Option V} (exact : ExactWithin D π f answer) (retain : K → M) (read : M → K)
    (faithful : ∀ s, D s → read (retain (π s)) = π s) :
    ExactWithin D (fun s => retain (π s)) f (fun m => answer (read m)) :=
  fun s inD => (congrArg answer (faithful s inD)).trans (exact s inD)

/-- **Staying silent is sound.** -/
theorem silent_sound (D : S → Prop) (π : S → K) (f : S → V) :
    SoundWithin D π f (fun _ => none) :=
  fun _ _ _ proposed => nomatch proposed

/-- **Staying silent is not exact on a domain holding a configuration.** -/
theorem silent_not_exact {D : S → Prop} (π : S → K) (f : S → V) {s : S} (inD : D s) :
    ¬ ExactWithin D π f (fun _ => none) :=
  fun exact => nomatch exact s inD

/-- A claim `p` is safe on `D` where every configuration of `D` asserting it has `p`. -/
def SafeWithin (D : S → Prop) (p : Prop) (asserts : S → Prop) : Prop := ∀ s, D s → asserts s → p

/-- **A claim that holds is safe whatever asserts it**: safety of a fixed true claim does not tell
a derivation from a guess. -/
theorem safe_of_holds (D asserts : S → Prop) {p : Prop} (holds : p) : SafeWithin D p asserts :=
  fun _ _ _ => holds

end Laws

/-! ## The channel model -/

/-- A bit passing through an orientation that may reverse it. -/
structure Channel where
  value : Bool
  reversed : Bool

/-- What passes: the bit, reversed where the orientation reverses it. -/
def signal (h : Channel) : Bool := Bool.xor h.value h.reversed

/-- The bit. -/
def bit (h : Channel) : Bool := h.value

/-- Every channel. -/
def every (_ : Channel) : Prop := True

/-- The unreversed channels. -/
def unreversed (h : Channel) : Prop := h.reversed = false

/-- A reference bit, `false`, sent through the same orientation. -/
def reference (h : Channel) : Bool := Bool.xor false h.reversed

/-- The signal with the reference. -/
def paired (h : Channel) : Bool × Bool := (signal h, reference h)

/-- Read the bit as the parity of the pair. -/
def decodePair (e : Bool × Bool) : Option Bool := some (Bool.xor e.1 e.2)

/-- Read the signal as the bit. -/
def direct (b : Bool) : Option Bool := some b

/-- **Paired with the reference, the signal is read exactly.** -/
theorem paired_exact : ExactWithin every paired bit decodePair
  | ⟨false, false⟩, _ => rfl
  | ⟨false, true⟩, _ => rfl
  | ⟨true, false⟩, _ => rfl
  | ⟨true, true⟩, _ => rfl

/-- **The signal alone does not lump the bit.** -/
theorem signal_not_lumped : ¬ LumpedWithin every signal bit :=
  fun lumped => Bool.noConfusion (lumped ⟨false, false⟩ ⟨true, true⟩ trivial trivial rfl)

/-- **No reading of the signal alone is exact.** -/
theorem signal_no_exact : ¬ ∃ answer, ExactWithin every signal bit answer :=
  fun ⟨_, exact⟩ => signal_not_lumped exact.lumped

/-- **Every sound reading of the signal alone stays silent on both values.** -/
theorem signal_sound_silent (answer : Bool → Option Bool) (sound : SoundWithin every signal bit answer) :
    ∀ e, answer e = none
  | false => SoundWithin.silent sound (s := ⟨false, false⟩) (s' := ⟨true, true⟩) trivial trivial rfl
      Bool.noConfusion
  | true => SoundWithin.silent sound (s := ⟨true, false⟩) (s' := ⟨false, true⟩) trivial trivial rfl
      Bool.noConfusion

/-- **The direct reading is exact on the unreversed channels.** -/
theorem direct_exact_unreversed : ExactWithin unreversed signal bit direct
  | ⟨false, false⟩, _ => rfl
  | ⟨true, false⟩, _ => rfl
  | ⟨_, true⟩, reversed => Bool.noConfusion reversed

/-- **The direct reading is not sound on every channel.** -/
theorem direct_not_sound : ¬ SoundWithin every signal bit direct :=
  fun sound => Bool.noConfusion (sound ⟨false, true⟩ trivial true rfl)

/-- The direct reading is right on the unreversed `false` channel. -/
theorem direct_right_once : direct (signal ⟨false, false⟩) = some (bit ⟨false, false⟩) := rfl

/-- **Keeping only the parity of the pair keeps exactness**: retaining every datum is not
needed. -/
theorem parity_exact :
    ExactWithin every (fun h => Bool.xor (paired h).1 (paired h).2) bit direct :=
  paired_exact

/-- **A negated copy read back by negation is exact.** -/
theorem negated_exact : ExactWithin every (fun h => !h.value) bit (fun b => some (!b))
  | ⟨false, _⟩, _ => rfl
  | ⟨true, _⟩, _ => rfl

/-! ## Readings of the prefix along runs -/

namespace Runs

section AnyProcess

variable {S : Type u} {A : Type v} {R : Type w} {V : Type x} {P : Process S A}

/-- The prefix the map `g` leaves along a run before step `t`, latest first. -/
def prefixBefore (g : S → R) (t : Nat) (r : Run P) : List R :=
  Learning.prefixOf (Parting.course g r) t

/-- The feature `f` of a run's configuration at step `t`. -/
def featureAt (f : S → V) (t : Nat) (r : Run P) : V := f (r.state t)

/-- **A reading of the prefix exact on a domain of runs is sound there.** -/
theorem exact_sound {D : Run P → Prop} {g : S → R} {f : S → V} {t : Nat}
    {answer : List R → Option V} (exact : ExactWithin D (prefixBefore g t) (featureAt f t) answer) :
    SoundWithin D (prefixBefore g t) (featureAt f t) answer :=
  exact.sound

/-- **An exact reading of the prefix needs lumping**: runs of the domain with one prefix before
`t` have one feature value at `t`. -/
theorem exact_lumped {D : Run P → Prop} {g : S → R} {f : S → V} {t : Nat}
    {answer : List R → Option V} (exact : ExactWithin D (prefixBefore g t) (featureAt f t) answer) :
    LumpedWithin D (prefixBefore g t) (featureAt f t) :=
  exact.lumped

/-- **A sound reading stays silent where the prefix leaves the feature open**. -/
theorem sound_silent {D : Run P → Prop} {g : S → R} {f : S → V} {t : Nat}
    {answer : List R → Option V} (sound : SoundWithin D (prefixBefore g t) (featureAt f t) answer)
    {r r' : Run P} (inD : D r) (inD' : D r') (same : prefixBefore g t r = prefixBefore g t r')
    (different : f (r.state t) ≠ f (r'.state t)) : answer (prefixBefore g t r) = none :=
  sound.silent inD inD' same different

/-- **Soundness on a domain of runs holds on every smaller one.** -/
theorem sound_mono {D D' : Run P → Prop} {g : S → R} {f : S → V} {t : Nat}
    {answer : List R → Option V} (sound : SoundWithin D (prefixBefore g t) (featureAt f t) answer)
    (within : ∀ r, D' r → D r) : SoundWithin D' (prefixBefore g t) (featureAt f t) answer :=
  sound.mono within

/-- **Lumping survives reading a second map's prefix beside the first.** -/
theorem finer_lumped {R' : Type w} {D : Run P → Prop} {g : S → R} {f : S → V} {t : Nat}
    (lumped : LumpedWithin D (prefixBefore g t) (featureAt f t)) (g' : S → R') :
    LumpedWithin D (fun r => (prefixBefore g t r, prefixBefore g' t r)) (featureAt f t) :=
  lumped.finer (prefixBefore g' t)

/-- **A faithfully retained prefix keeps exactness.** -/
theorem retained_exact {M : Type w} {D : Run P → Prop} {g : S → R} {f : S → V} {t : Nat}
    {answer : List R → Option V} (exact : ExactWithin D (prefixBefore g t) (featureAt f t) answer)
    (retain : List R → M) (read : M → List R)
    (faithful : ∀ r, D r → read (retain (prefixBefore g t r)) = prefixBefore g t r) :
    ExactWithin D (fun r => retain (prefixBefore g t r)) (featureAt f t)
      (fun m => answer (read m)) :=
  exact.retained retain read faithful

/-- **Staying silent on every prefix is sound** on every domain of runs. -/
theorem silent_sound (D : Run P → Prop) (g : S → R) (f : S → V) (t : Nat) :
    SoundWithin D (prefixBefore g t) (featureAt f t) (fun _ => none) :=
  PartialReadout.silent_sound D (prefixBefore g t) (featureAt f t)

/-- **Staying silent is not exact on a domain holding a run.** -/
theorem silent_not_exact {D : Run P → Prop} (g : S → R) (f : S → V) (t : Nat) {r : Run P}
    (inD : D r) : ¬ ExactWithin D (prefixBefore g t) (featureAt f t) (fun _ => none) :=
  PartialReadout.silent_not_exact (prefixBefore g t) (featureAt f t) inD

/-- **With a section of the prefix over a domain of runs, some reading of the prefix is exact at
`t` exactly where runs of the domain with one prefix before `t` have one feature value at `t`.** -/
theorem exact_exists_iff {D : Run P → Prop} {g : S → R} {f : S → V} {t : Nat}
    {pick : List R → Option (Run P)} (sec : SectionWithin D (prefixBefore g t) pick) :
    (∃ answer, ExactWithin D (prefixBefore g t) (featureAt f t) answer) ↔
      LumpedWithin D (prefixBefore g t) (featureAt f t) :=
  PartialReadout.exact_exists_iff sec

end AnyProcess

section Law

variable {S : Type u} {R : Type v} {V : Type w} {next : S → S}

/-- **Along the runs of a determined law, an extrapolation rests on the feature from `T` exactly
where, at every step from `T` on, it reads the prefix exactly on all runs.** -/
theorem exact_iff_predictsFrom {g : S → R} {f : S → V} {pred : List R → Option V} {T : Nat} :
    (∀ t, T ≤ t → ExactWithin (fun _ : Run (Law.process next) => True) (prefixBefore g t)
        (featureAt f t) pred) ↔
      ∀ r : Run (Law.process next), LearnableRuns.PredictsFrom g f pred r T :=
  ⟨fun exact r t late => exact t late r trivial, fun rests t late r _ => rests r t late⟩

end Law

end Runs

end PartialReadout

end Becoming
