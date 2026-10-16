import CalibratedUpdater

noncomputable section

namespace CalibrationRenewal
open ConnectionistRecovery DevelopmentalMemory UpdaterConsequences CalibratedUpdater

theorem two_references_complete (old current : Channel) :
    (raw old 0 = raw current 0 ∧ raw old 1 = raw current 1) ↔
      ∀ p, raw old p = raw current p := by
  constructor
  · rintro ⟨h0,h1⟩ p
    have hb : old.bias = current.bias := by simpa [raw] using h0
    have hg : old.gain = current.gain := by dsimp [raw] at h1; linarith
    simp [raw,hb,hg]
  · intro h; exact ⟨h 0,h 1⟩

def signal (old current : Channel) (p s : ℝ) : ℝ :=
  s*(raw old 1-raw old 0)*(raw current p-raw old 0)

theorem signal_expansion (old current : Channel) (p s : ℝ) :
    signal old current p s = (old.gain*current.gain)*(s*p) +
      old.gain*(current.bias-old.bias)*s := by
  dsimp [signal,raw]; ring

theorem all_signs_transfer_iff (old current : Channel) (hg : old.gain ≠ 0) :
    (∀ p s, (0 < signal old current p s ↔ 0 < s*p)) ↔
      current.bias = old.bias ∧ 0 < old.gain*current.gain := by
  constructor
  · intro h
    have h0 := h 0 1
    have hn := h 0 (-1)
    rw [signal_expansion] at h0 hn
    have hz : old.gain*(current.bias-old.bias) = 0 := by
      norm_num at h0 hn
      linarith
    have hb : current.bias = old.bias := by
      have := (mul_eq_zero.mp hz).resolve_left hg
      linarith
    refine ⟨hb,?_⟩
    have hp := (h 1 1).2 (by norm_num)
    simpa [signal_expansion,hb] using hp
  · rintro ⟨hb,hp⟩ p s
    rw [signal_expansion]
    simp only [hb,sub_self,mul_zero,zero_mul,add_zero]
    exact mul_pos_iff_of_pos_left hp

theorem zero_reference_blind :
    raw (⟨1,0⟩ : Channel) 0 = raw (⟨-1,0⟩ : Channel) 0 ∧
    raw (⟨1,0⟩ : Channel) 1 ≠ raw (⟨-1,0⟩ : Channel) 1 := by
  norm_num [raw]

theorem positive_gain_change_preserves_signs :
    ∀ p s, (0 < signal (⟨1,0⟩ : Channel) (⟨2,0⟩ : Channel) p s ↔ 0 < s*p) := by
  exact (all_signs_transfer_iff _ _ (by norm_num)).2 (by norm_num)

structure Sample where
  zero : Fin 3 → ℝ
  one : Fin 3 → ℝ

def acquireSample (channels : Fin 3 → Channel) : Sample :=
  ⟨fun i => raw (channels i) 0, fun i => raw (channels i) 1⟩

def agrees (h : Apparatus) (sample : Sample) : Prop :=
  ∀ i, h.zero i = some (sample.zero i) ∧ h.one i = some (sample.one i)

def revise (h : Apparatus) (sample : Sample) : Apparatus :=
  { h with zero := fun i => some (sample.zero i)
           one := fun i => some (sample.one i) }

def connected (h : Apparatus) : Prop := (∀ i, h.wired i = true) ∧ h.inhibit = true

theorem revised_matches (h : Apparatus) (sample : Sample) : agrees (revise h sample) sample := by
  intro i; exact ⟨rfl,rfl⟩

theorem ready_matches_iff (old current : Fin 3 → Channel) :
    agrees (ready old) (acquireSample current) ↔ ∀ i p, raw (old i) p = raw (current i) p := by
  simp only [agrees,ready,acquireSample,Option.some.injEq]
  exact forall_congr' (fun i => two_references_complete (old i) (current i))

theorem matching_report (h : Apparatus) (channels : Fin 3 → Channel)
    (hc : connected h) (hm : agrees h (acquireSample channels))
    (hg : ∀ i, (channels i).gain ≠ 0) (p s : Profile 3) :
    report h (readings channels p) s = some (@decide (recalls s p) (Classical.propDecidable _)) := by
  classical
  have hlocal : ∀ i, localRead h (readings channels p) s i = some (decide (0 < s i*p i)) := by
    intro i
    rw [localRead, hc.1 i]
    simp only [↓reduceIte, readings]
    rw [(hm i).1,(hm i).2]
    exact acquired_local_exact (channels i) (p i) (s i) (hg i)
  simp only [report, hlocal, join_some]
  congr 1
  simp [recalls,Fin.forall_fin_succ]

theorem matching_usable (h : Apparatus) (channels : Fin 3 → Channel)
    (hc : connected h) (hm : agrees h (acquireSample channels))
    (hg : ∀ i, (channels i).gain ≠ 0) : usable h := by
  refine ⟨hc.2,?_⟩
  intro i
  refine ⟨hc.1 i,raw (channels i) 0,raw (channels i) 1,(hm i).1,(hm i).2,?_⟩
  simp [raw,hg i]

theorem matching_update (h : Apparatus) (channels : Fin 3 → Channel)
    (hc : connected h) (hm : agrees h (acquireSample channels))
    (hg : ∀ i, (channels i).gain ≠ 0) (B : Network 3) (task : Task) :
    nativeUpdate h channels B task = update .responsive B task := by
  classical
  unfold nativeUpdate
  dsimp only
  rw [matching_report h channels hc hm hg]
  simp [hc.2,update,UpdaterConsequences.succeeds]

theorem matching_run (h : Apparatus) (channels : Fin 3 → Channel)
    (hc : connected h) (hm : agrees h (acquireSample channels))
    (hg : ∀ i, (channels i).gain ≠ 0) (B : Network 3) (tasks : List Task) :
    nativeRun h channels B tasks = run .responsive B tasks := by
  induction tasks generalizing B with
  | nil => rfl
  | cons task rest ih => simp [nativeRun,run,matching_update h channels hc hm hg,ih]

structure Renewal where
  apparatus : Apparatus
  fuel : Nat
  spent : Nat
  admitted : Bool
  revisions : Nat

def inspect (channels : Fin 3 → Channel) (x : Renewal) : Renewal := by
  classical
  exact if (∀ i, x.apparatus.wired i = true) ∧ 6 ≤ x.fuel then
    let sample := acquireSample channels
    if agrees x.apparatus sample then
      { x with fuel := x.fuel-6, spent := x.spent+6, admitted := true }
    else if 7 ≤ x.fuel then
      { x with apparatus := revise x.apparatus sample
               fuel := x.fuel-7, spent := x.spent+7, admitted := true
               revisions := x.revisions+1 }
    else { x with fuel := x.fuel-6, spent := x.spent+6, admitted := false }
  else { x with admitted := false }

theorem inspection_conserves (channels : Fin 3 → Channel) (x : Renewal) :
    (inspect channels x).fuel+(inspect channels x).spent = x.fuel+x.spent := by
  classical
  unfold inspect
  dsimp only
  split_ifs <;> dsimp <;> omega

theorem inspection_fuel_bound (channels : Fin 3 → Channel) (x : Renewal) :
    x.fuel ≤ (inspect channels x).fuel+7 := by
  classical
  unfold inspect
  dsimp only
  split_ifs <;> dsimp <;> omega

theorem inspection_connected (channels : Fin 3 → Channel) (x : Renewal)
    (hc : connected x.apparatus) : connected (inspect channels x).apparatus := by
  classical
  unfold inspect
  dsimp only
  split_ifs <;> simpa only [connected,revise] using hc

theorem inspection_matches (channels : Fin 3 → Channel) (x : Renewal)
    (hc : connected x.apparatus) (hf : 7 ≤ x.fuel) :
    agrees (inspect channels x).apparatus (acquireSample channels) := by
  classical
  have h6 : 6 ≤ x.fuel := by omega
  unfold inspect
  rw [if_pos ⟨hc.1,h6⟩]
  dsimp only
  simp only [if_pos hf]
  split_ifs with hm
  · exact hm
  · exact revised_matches _ _

theorem inspection_admitted (channels : Fin 3 → Channel) (x : Renewal)
    (hc : connected x.apparatus) (hf : 7 ≤ x.fuel) : (inspect channels x).admitted = true := by
  classical
  have h6 : 6 ≤ x.fuel := by omega
  unfold inspect
  rw [if_pos ⟨hc.1,h6⟩]
  dsimp only
  split_ifs <;> simp_all

theorem uninspectable_not_admitted (channels : Fin 3 → Channel) (x : Renewal)
    (hf : x.fuel < 6) : (inspect channels x).admitted = false := by
  simp [inspect,show ¬ 6 ≤ x.fuel by omega]

theorem unfunded_revision_not_admitted (channels : Fin 3 → Channel) (x : Renewal)
    (hc : connected x.apparatus) (hf : x.fuel = 6)
    (hm : ¬ agrees x.apparatus (acquireSample channels)) :
    (inspect channels x).apparatus = x.apparatus ∧
    (inspect channels x).admitted = false ∧ (inspect channels x).spent = x.spent+6 := by
  simp [inspect,hc.1,hf,hm]

def runAdmitted (x : Renewal) (channels : Fin 3 → Channel) (B : Network 3)
    (tasks : List Task) : Network 3 × Nat := by
  classical
  exact if x.admitted = true ∧ usable x.apparatus
    then nativeRun x.apparatus channels B tasks else (B,0)

theorem unadmitted_holds (x : Renewal) (channels : Fin 3 → Channel) (B : Network 3)
    (tasks : List Task) (hn : x.admitted = false) : runAdmitted x channels B tasks = (B,0) := by
  simp [runAdmitted,hn]

theorem renewed_run (channels : Fin 3 → Channel) (x : Renewal)
    (hc : connected x.apparatus) (hf : 7 ≤ x.fuel)
    (hg : ∀ i, (channels i).gain ≠ 0) (B : Network 3) (tasks : List Task) :
    runAdmitted (inspect channels x) channels B tasks = run .responsive B tasks := by
  have hc' := inspection_connected channels x hc
  have hm := inspection_matches channels x hc hf
  have hu := matching_usable _ channels hc' hm hg
  simp only [runAdmitted,inspection_admitted channels x hc hf,hu,and_self,↓reduceIte]
  exact matching_run _ channels hc' hm hg B tasks

theorem renewed_cycle (channels : Fin 3 → Channel) (x : Renewal)
    (hc : connected x.apparatus) (hf : 7 ≤ x.fuel)
    (hg : ∀ i, (channels i).gain ≠ 0) (carrier : NativeState) :
    project .responsive (nativeCycle (inspect channels x).apparatus channels carrier) =
      cycleStep (project .responsive carrier) := by
  exact native_cycle_projection _ _ _
    (matching_run _ channels (inspection_connected channels x hc)
      (inspection_matches channels x hc hf) hg) carrier

structure Block where
  channels : Fin 3 → Channel
  tasks : List Task

def runBlocks (x : Renewal) (B : Network 3) : List Block → Renewal × (Network 3 × Nat)
  | [] => (x,(B,0))
  | block :: rest =>
    let next := inspect block.channels x
    let result := runAdmitted next block.channels B block.tasks
    let later := runBlocks next result.1 rest
    (later.1,(later.2.1,result.2+later.2.2))

def idealBlocks (B : Network 3) : List Block → Network 3 × Nat
  | [] => (B,0)
  | block :: rest =>
    let result := run .responsive B block.tasks
    let later := idealBlocks result.1 rest
    (later.1,result.2+later.2)

theorem finite_blocks_correspond (blocks : List Block) (x : Renewal) (B : Network 3)
    (hc : connected x.apparatus) (hf : 7*blocks.length ≤ x.fuel)
    (hg : ∀ block ∈ blocks, ∀ i, (block.channels i).gain ≠ 0) :
    (runBlocks x B blocks).2 = idealBlocks B blocks := by
  induction blocks generalizing x B with
  | nil => rfl
  | cons block rest ih =>
    have h7 : 7 ≤ x.fuel := by simp only [List.length_cons] at hf; omega
    have hb := inspection_fuel_bound block.channels x
    have hr : 7*rest.length ≤ (inspect block.channels x).fuel := by
      simp only [List.length_cons] at hf
      omega
    have hgain := hg block (by simp)
    have hrest : ∀ b ∈ rest, ∀ i, (b.channels i).gain ≠ 0 := by
      intro b h; exact hg b (by simp [h])
    simp only [runBlocks,idealBlocks,renewed_run block.channels x hc h7 hgain]
    rw [ih _ _ (inspection_connected block.channels x hc) hr hrest]

theorem finite_blocks_conserve (blocks : List Block) (x : Renewal) (B : Network 3) :
    (runBlocks x B blocks).1.fuel+(runBlocks x B blocks).1.spent = x.fuel+x.spent := by
  induction blocks generalizing x B with
  | nil => rfl
  | cons block rest ih =>
    simp only [runBlocks]
    rw [ih]
    exact inspection_conserves block.channels x

def oldReader (fuel : Nat) : Renewal := ⟨ready identityChannels,fuel,0,false,0⟩

def changedReader : Renewal := ⟨ready changedChannels,0,7,true,1⟩

theorem unchanged_inspection (fuel : Nat) (hf : 6 ≤ fuel) :
    inspect identityChannels (oldReader fuel) =
      ⟨ready identityChannels,fuel-6,6,true,0⟩ := by
  have hm : agrees (ready identityChannels) (acquireSample identityChannels) := by
    intro i; exact ⟨rfl,rfl⟩
  unfold inspect
  rw [if_pos ⟨fun _ => rfl,hf⟩]
  dsimp only [oldReader]
  rw [if_pos hm]

theorem actual_changed_inspection : inspect changedChannels (oldReader 7) = changedReader := by
  have hm : ¬ agrees (ready identityChannels) (acquireSample changedChannels) := by
    intro h
    have := (h 2).2
    have he : second (2:Fin 3) = -1 := rfl
    norm_num [oldReader,ready,acquireSample,raw,identityChannels,changedChannels,he] at this
  unfold inspect
  rw [if_pos ⟨fun _ => rfl,by norm_num [oldReader]⟩]
  dsimp only [oldReader]
  rw [if_neg hm,if_pos (by omega)]
  rfl

theorem changed_channels_nonzero (i : Fin 3) : (changedChannels i).gain ≠ 0 := by
  fin_cases i <;> norm_num [changedChannels,second]

theorem actual_repair_after_inspection :
    (runAdmitted (inspect changedChannels (oldReader 7)) changedChannels
      (weighted 1 4) [.a,.a]).1 = weighted 2 4 ∧
    (runAdmitted (inspect changedChannels (oldReader 7)) changedChannels
      (weighted 1 4) [.a,.a]).2 = 1 := by
  have hc : connected (oldReader 7).apparatus := ⟨fun _ => rfl,rfl⟩
  rw [renewed_run changedChannels (oldReader 7) hc (by norm_num [oldReader]) changed_channels_nonzero]
  rw [run, repaired_by_responsive]
  norm_num [run,update,succeeds_first_iff]

theorem six_units_cannot_revise :
    runAdmitted (inspect changedChannels (oldReader 6)) changedChannels
      (weighted 1 4) [.a] = (weighted 1 4,0) := by
  apply unadmitted_holds
  have hm : ¬ agrees (oldReader 6).apparatus (acquireSample changedChannels) := by
    intro h
    have := (h 2).2
    have he : second (2:Fin 3) = -1 := rfl
    norm_num [oldReader,ready,acquireSample,raw,identityChannels,changedChannels,he] at this
  exact (unfunded_revision_not_admitted _ _ ⟨fun _ => rfl,rfl⟩ rfl hm).2.1

theorem late_change_still_fails :
    nativeUpdate (inspect identityChannels (oldReader 6)).apparatus changedChannels
      (weighted 1 4) .a = weighted 1 4 ∧ ¬ succeeds (weighted 1 4) .a := by
  rw [unchanged_inspection 6 (by omega)]
  exact stale_channel_blocks_actual_repair

theorem mixed_epoch_false_success :
    localReport (some (raw (⟨1,0⟩ : Channel) 0))
      (some (raw (⟨1,2⟩ : Channel) 1)) (raw (⟨1,2⟩ : Channel) (-1)) 1 = some true ∧
      ¬ (0 < (1:ℝ)*(-1)) := by
  norm_num [localReport,raw]

theorem constant_channel_unusable (h : Apparatus) (channels : Fin 3 → Channel)
    (hm : agrees h (acquireSample channels)) (i : Fin 3) (hg : (channels i).gain = 0) :
    ¬ usable h := by
  intro hu
  obtain ⟨z,o,hz,ho,hne⟩ := (hu.2 i).2
  have hz' : z = raw (channels i) 0 := Option.some.inj (hz.symm.trans (hm i).1)
  have ho' : o = raw (channels i) 1 := Option.some.inj (ho.symm.trans (hm i).2)
  apply hne
  rw [hz',ho']
  simp [raw,hg]

theorem constant_channel_holds (channels : Fin 3 → Channel) (x : Renewal)
    (hc : connected x.apparatus) (hf : 7 ≤ x.fuel) (i : Fin 3)
    (hg : (channels i).gain = 0) (B : Network 3) (tasks : List Task) :
    runAdmitted (inspect channels x) channels B tasks = (B,0) := by
  have hn := constant_channel_unusable _ channels (inspection_matches channels x hc hf) i hg
  simp [runAdmitted,hn]

def withoutReferenceRenewal : Nat → Network 3
  | 0 => weighted 1 4
  | n+1 => nativeUpdate (ready identityChannels) changedChannels (withoutReferenceRenewal n) .a

theorem false_success_stalls (n : Nat) : withoutReferenceRenewal n = weighted 1 4 := by
  induction n with
  | zero => rfl
  | succ n ih =>
    rw [withoutReferenceRenewal,ih]
    exact stale_channel_blocks_actual_repair.1

def curvedReading (p : ℝ) : ℝ := p*(2*p-1)

theorem nonaffine_reference_alias :
    curvedReading 0 = raw (⟨1,0⟩ : Channel) 0 ∧
    curvedReading 1 = raw (⟨1,0⟩ : Channel) 1 ∧
    localReport (some (curvedReading 0)) (some (curvedReading 1))
      (curvedReading (-1)) 1 = some true ∧ ¬ (0 < (1:ℝ)*(-1)) := by
  norm_num [curvedReading,raw,localReport]

end CalibrationRenewal
