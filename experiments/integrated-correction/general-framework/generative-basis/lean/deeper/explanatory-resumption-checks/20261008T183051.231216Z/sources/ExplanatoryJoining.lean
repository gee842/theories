import ExplanatoryUniqueness

/-! Boundary-sensitive finite joining and recovery by empty-history probes.
The process and the scope of its recorded conditions are supplied. Probes are
mathematical candidates, not a claim that every probe is physically available. -/
namespace Generative.ExplanatoryJoining
open ExplanatoryUniqueness
universe u v w
variable {S : Type u} {A : Type v} {C : Type w}

structure Fragment (S : Type u) (A : Type v) where
  start : S
  word : List A
  finish : S
  deriving DecidableEq

def Valid (P : Process S A) (f : Fragment S A) : Prop := Trace P f.start f.word f.finish

def idle (s : S) : Fragment S A := ⟨s, [], s⟩

def merge (f g : Fragment S A) : Fragment S A := ⟨f.start, f.word ++ g.word, g.finish⟩

def Joint (P : Process S A) (f g : Fragment S A) : Prop :=
  Valid P f ∧ Valid P g ∧ f.finish = g.start

def Joined (P : Process S A) (f g h : Fragment S A) : Prop := Joint P f g ∧ merge f g = h

theorem idle_valid (P : Process S A) (s : S) : Valid P (idle s) := .nil s

theorem joint_iff_joined (P : Process S A) (f g : Fragment S A) :
    Joint P f g ↔ ∃ h, Joined P f g h :=
  ⟨fun h => ⟨merge f g, h, rfl⟩, fun ⟨_, h, _⟩ => h⟩

theorem joined_functional {P : Process S A} {f g h k : Fragment S A}
    (hh : Joined P f g h) (hk : Joined P f g k) : h = k := hh.2.symm.trans hk.2

theorem joint_merge_valid {P : Process S A} {f g : Fragment S A} (h : Joint P f g) :
    Valid P (merge f g) := by
  apply trace_append_iff.mpr
  exact ⟨f.finish, h.1, h.2.2 ▸ h.2.1⟩

theorem joined_valid {P : Process S A} {f g h : Fragment S A} (hh : Joined P f g h) :
    Valid P h := hh.2 ▸ joint_merge_valid hh.1

theorem merge_associative (f g h : Fragment S A) : merge (merge f g) h = merge f (merge g h) := by
  cases f; cases g; cases h
  simp only [merge, List.append_assoc]

theorem joint_chain_left {P : Process S A} {f g h : Fragment S A}
    (hfg : Joint P f g) (hgh : Joint P g h) : Joint P (merge f g) h :=
  ⟨joint_merge_valid hfg, hgh.2.1, hgh.2.2⟩

theorem joint_chain_right {P : Process S A} {f g h : Fragment S A}
    (hfg : Joint P f g) (hgh : Joint P g h) : Joint P f (merge g h) :=
  ⟨hfg.1, joint_merge_valid hgh, hfg.2.2⟩

theorem joined_associative (P : Process S A) (f g h k : Fragment S A) :
    (∃ m, Joined P f g m ∧ Joined P m h k) ↔
    (∃ n, Joined P g h n ∧ Joined P f n k) := by
  constructor
  · rintro ⟨m, ⟨hfg, rfl⟩, ⟨hmh, he⟩⟩
    have hgh : Joint P g h := ⟨hfg.2.1, hmh.2.1, hmh.2.2⟩
    exact ⟨merge g h, ⟨hgh, rfl⟩, joint_chain_right hfg hgh, (merge_associative f g h).symm.trans he⟩
  · rintro ⟨n, ⟨hgh, rfl⟩, ⟨hfn, he⟩⟩
    have hfg : Joint P f g := ⟨hfn.1, hgh.1, hfn.2.2⟩
    exact ⟨merge f g, ⟨hfg, rfl⟩, joint_chain_left hfg hgh, (merge_associative f g h).trans he⟩

theorem idle_left_probe (P : Process S A) (f : Fragment S A) (s : S) :
    Joint P (idle s) f ↔ Valid P f ∧ s = f.start :=
  ⟨fun h => ⟨h.2.1, h.2.2⟩, fun h => ⟨idle_valid P s, h.1, h.2⟩⟩

theorem idle_right_probe (P : Process S A) (f : Fragment S A) (s : S) :
    Joint P f (idle s) ↔ Valid P f ∧ f.finish = s :=
  ⟨fun h => ⟨h.1, h.2.2⟩, fun h => ⟨h.1, idle_valid P s, h.2⟩⟩

theorem joined_idle_left {P : Process S A} {f : Fragment S A} (h : Valid P f) :
    Joined P (idle f.start) f f := by
  refine ⟨⟨idle_valid P _, h, rfl⟩, ?_⟩
  cases f; rfl

theorem joined_idle_right {P : Process S A} {f : Fragment S A} (h : Valid P f) :
    Joined P f (idle f.finish) f := by
  refine ⟨⟨h, idle_valid P _, rfl⟩, ?_⟩
  cases f
  simp only [merge, idle, List.append_nil]

inductive Probe (S : Type u) where
  | before : S → Probe S
  | after : S → Probe S

def probeTarget (P : Process S A) (f : Fragment S A) : Probe S → Prop
  | .before s => Joint P (idle s) f
  | .after s => Joint P f (idle s)

theorem same_probes_iff_boundaries {P : Process S A} {f g : Fragment S A}
    (hf : Valid P f) (hg : Valid P g) :
    SameAnswers (probeTarget P) f g ↔ f.start = g.start ∧ f.finish = g.finish := by
  constructor
  · intro h
    have hs := (h (.before f.start)).mp ((idle_left_probe P f f.start).mpr ⟨hf, rfl⟩)
    have ht := (h (.after f.finish)).mp ((idle_right_probe P f f.finish).mpr ⟨hf, rfl⟩)
    exact ⟨((idle_left_probe P g f.start).mp hs).2, ((idle_right_probe P g f.finish).mp ht).2.symm⟩
  · rintro ⟨hs, ht⟩ q
    cases q with
    | before s =>
      constructor
      · intro h
        exact (idle_left_probe P g s).mpr ⟨hg, h.2.2.trans hs⟩
      · intro h
        exact (idle_left_probe P f s).mpr ⟨hf, h.2.2.trans hs.symm⟩
    | after s =>
      constructor
      · intro h
        exact (idle_right_probe P g s).mpr ⟨hg, ht.symm.trans h.2.2⟩
      · intro h
        exact (idle_right_probe P f s).mpr ⟨hf, ht.trans h.2.2⟩

theorem probes_recover_joint (P : Process S A) (f g : Fragment S A) :
    Joint P f g ↔ ∃ s, probeTarget P f (.after s) ∧ probeTarget P g (.before s) := by
  constructor
  · intro h
    exact ⟨f.finish, (idle_right_probe P f _).mpr ⟨h.1, rfl⟩,
      (idle_left_probe P g _).mpr ⟨h.2.1, h.2.2⟩⟩
  · rintro ⟨s, hf, hg⟩
    exact ⟨hf.1, hg.2.1, hf.2.2.trans hg.2.2⟩

theorem exact_codes_retain_boundaries {P : Process S A}
    {p : Presentation (Fragment S A) (Probe S) C} (hp : Exact (probeTarget P) p)
    {f g : Fragment S A} (hf : Valid P f) (hg : Valid P g) (h : p.encode f = p.encode g) :
    f.start = g.start ∧ f.finish = g.finish :=
  (same_probes_iff_boundaries hf hg).mp (equal_codes_same_answers hp h)

def RecoveredJoint (p : Presentation (Fragment S A) (Probe S) C) (a b : C) : Prop :=
  ∃ s, p.read a (.after s) ∧ p.read b (.before s)

theorem exact_reads_recover_joint {P : Process S A}
    {p : Presentation (Fragment S A) (Probe S) C} (hp : Exact (probeTarget P) p)
    (f g : Fragment S A) : RecoveredJoint p (p.encode f) (p.encode g) ↔ Joint P f g := by
  constructor
  · rintro ⟨s, hf, hg⟩
    exact (probes_recover_joint P f g).mpr ⟨s, (hp f _).mp hf, (hp g _).mp hg⟩
  · intro h
    obtain ⟨s, hf, hg⟩ := (probes_recover_joint P f g).mp h
    exact ⟨s, (hp f _).mpr hf, (hp g _).mpr hg⟩

theorem boundary_replacement_preserves_joint {P : Process S A} {f f' g g' : Fragment S A}
    (hf : Valid P f) (hf' : Valid P f') (hg : Valid P g) (hg' : Valid P g')
    (ef : SameAnswers (probeTarget P) f f') (eg : SameAnswers (probeTarget P) g g') :
    Joint P f g ↔ Joint P f' g' := by
  obtain ⟨_, efinish⟩ := (same_probes_iff_boundaries hf hf').mp ef
  obtain ⟨estart, _⟩ := (same_probes_iff_boundaries hg hg').mp eg
  exact ⟨fun h => ⟨hf', hg', efinish.symm.trans (h.2.2.trans estart)⟩,
    fun h => ⟨hf, hg, efinish.trans (h.2.2.trans estart.symm)⟩⟩

/-- A concrete budget transition records remaining capacity in its boundary. -/
def budgetProcess : Process Bool Unit where
  step s _ t := s = false ∧ t = true

def spend : Fragment Bool Unit := ⟨false, [()], true⟩

theorem spend_valid : Valid budgetProcess spend :=
  trace_singleton_iff.mpr ⟨rfl, rfl⟩

theorem spend_cannot_self_join : ¬ Joint budgetProcess spend spend := by
  intro h
  cases h.2.2

theorem boundary_idles_distinguished :
    ¬ SameAnswers (probeTarget budgetProcess) (idle false) (idle true) := by
  intro h
  have bad := (same_probes_iff_boundaries (idle_valid budgetProcess false)
    (idle_valid budgetProcess true)).mp h
  cases bad.1

/-- Joinability probes preserve interfaces but need not preserve path content. -/
def loopProcess : Process Unit Bool where
  step _ _ _ := True

def loop (a : Bool) : Fragment Unit Bool := ⟨(), [a], ()⟩

theorem loop_valid (a : Bool) : Valid loopProcess (loop a) := trace_singleton_iff.mpr True.intro

theorem probes_miss_internal_word :
    SameAnswers (probeTarget loopProcess) (loop false) (loop true) ∧
    (loop false).word ≠ (loop true).word := by
  refine ⟨(same_probes_iff_boundaries (loop_valid false) (loop_valid true)).mpr ⟨rfl, rfl⟩, ?_⟩
  intro h
  cases h

end Generative.ExplanatoryJoining

#print axioms Generative.ExplanatoryJoining.idle_valid
#print axioms Generative.ExplanatoryJoining.joint_iff_joined
#print axioms Generative.ExplanatoryJoining.joined_functional
#print axioms Generative.ExplanatoryJoining.joint_merge_valid
#print axioms Generative.ExplanatoryJoining.joined_valid
#print axioms Generative.ExplanatoryJoining.merge_associative
#print axioms Generative.ExplanatoryJoining.joint_chain_left
#print axioms Generative.ExplanatoryJoining.joint_chain_right
#print axioms Generative.ExplanatoryJoining.joined_associative
#print axioms Generative.ExplanatoryJoining.idle_left_probe
#print axioms Generative.ExplanatoryJoining.idle_right_probe
#print axioms Generative.ExplanatoryJoining.joined_idle_left
#print axioms Generative.ExplanatoryJoining.joined_idle_right
#print axioms Generative.ExplanatoryJoining.same_probes_iff_boundaries
#print axioms Generative.ExplanatoryJoining.probes_recover_joint
#print axioms Generative.ExplanatoryJoining.exact_codes_retain_boundaries
#print axioms Generative.ExplanatoryJoining.exact_reads_recover_joint
#print axioms Generative.ExplanatoryJoining.boundary_replacement_preserves_joint
#print axioms Generative.ExplanatoryJoining.spend_valid
#print axioms Generative.ExplanatoryJoining.spend_cannot_self_join
#print axioms Generative.ExplanatoryJoining.boundary_idles_distinguished
#print axioms Generative.ExplanatoryJoining.loop_valid
#print axioms Generative.ExplanatoryJoining.probes_miss_internal_word
