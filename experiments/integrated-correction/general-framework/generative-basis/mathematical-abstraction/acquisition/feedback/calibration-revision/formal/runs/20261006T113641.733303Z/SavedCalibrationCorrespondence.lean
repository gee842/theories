import CalibrationRevision
namespace CalibrationRevisionSaved
open CalibrationRevision
set_option maxRecDepth 65536
set_option maxHeartbeats 8000000
/- Generated from frozen saved states. A 16-entry Boolean mask is losslessly encoded as a 16-bit Nat; distinct observed encodings are also kernel checked. -/
def parent_calibration_break_config : RemainingDependency.Config := {weak := ⟨false, true⟩, full := ⟨false, false⟩, channels := ⟨.faithful, .faithful⟩, clamp := false}
def parent_calibration_break : RemainingDependency.State := {ancestor := {alphabet := ["a"], initial := 0, controlLocation := "reported_episode_complete", outputs := [true, true, false], transitions := [1, 2, 0], table := [(some false), (some true), none], retained := true, componentDone := true}, config := parent_calibration_break_config, body := {account := {fuel := 428018, start := 713012, spent := 284994, live := 34, peak := 42, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := true, mode := .serviceIssued, values := ⟨(some false), (some true)⟩, tags := ⟨(some 1), (some 1)⟩, contact := none, candidate := (some true), readMode := (some .selectedRelay), selected := (some true)}}
def parent_context_change_config : RemainingDependency.Config := {weak := ⟨false, true⟩, full := ⟨false, false⟩, channels := ⟨.faithful, .faithful⟩, clamp := false}
def parent_context_change : RemainingDependency.State := {ancestor := {alphabet := ["a"], initial := 0, controlLocation := "reported_episode_complete", outputs := [true, true, false], transitions := [1, 2, 0], table := [(some false), (some true), none], retained := true, componentDone := true}, config := parent_context_change_config, body := {account := {fuel := 428018, start := 713012, spent := 284994, live := 34, peak := 42, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 2, relay := true, pending := none, held := false, installed := true, retained := true, mode := .serviceIssued, values := ⟨(some false), (some true)⟩, tags := ⟨(some 1), (some 1)⟩, contact := none, candidate := (some true), readMode := (some .selectedRelay), selected := (some true)}}
def parent_false_dependence_config : RemainingDependency.Config := {weak := ⟨false, false⟩, full := ⟨false, false⟩, channels := ⟨.faithful, .flip⟩, clamp := false}
def parent_false_dependence : RemainingDependency.State := {ancestor := {alphabet := ["a"], initial := 0, controlLocation := "reported_episode_complete", outputs := [true, true, false], transitions := [1, 2, 0], table := [(some false), (some true), none], retained := true, componentDone := true}, config := parent_false_dependence_config, body := {account := {fuel := 428018, start := 713012, spent := 284994, live := 34, peak := 42, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := true, mode := .serviceIssued, values := ⟨(some false), (some true)⟩, tags := ⟨(some 1), (some 1)⟩, contact := none, candidate := (some true), readMode := (some .selectedRelay), selected := (some true)}}
def parent_false_positive_first_config : RemainingDependency.Config := {weak := ⟨false, true⟩, full := ⟨false, true⟩, channels := ⟨.flip, .faithful⟩, clamp := false}
def parent_false_positive_first : RemainingDependency.State := {ancestor := {alphabet := ["a"], initial := 0, controlLocation := "reported_episode_complete", outputs := [true, true, false], transitions := [1, 2, 0], table := [(some false), (some true), none], retained := true, componentDone := true}, config := parent_false_positive_first_config, body := {account := {fuel := 444402, start := 713012, spent := 268610, live := 34, peak := 42, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := false, pending := none, held := false, installed := true, retained := true, mode := .serviceIssued, values := ⟨(some true), (some true)⟩, tags := ⟨(some 1), (some 1)⟩, contact := none, candidate := (some false), readMode := (some .selectedBypass), selected := (some false)}}
def parent_law_01_learned_config : RemainingDependency.Config := {weak := ⟨false, true⟩, full := ⟨false, true⟩, channels := ⟨.faithful, .faithful⟩, clamp := false}
def parent_law_01_learned : RemainingDependency.State := {ancestor := {alphabet := ["a"], initial := 0, controlLocation := "reported_episode_complete", outputs := [true, true, false], transitions := [1, 2, 0], table := [(some false), (some true), none], retained := true, componentDone := true}, config := parent_law_01_learned_config, body := {account := {fuel := 428018, start := 713012, spent := 284994, live := 34, peak := 42, capacity := 256}, stocks := ⟨0, 10, 0⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := true, mode := .serviceIssued, values := ⟨(some false), (some true)⟩, tags := ⟨(some 1), (some 1)⟩, contact := none, candidate := (some true), readMode := (some .selectedRelay), selected := (some true)}}
def parent_law_10_learned_config : RemainingDependency.Config := {weak := ⟨true, false⟩, full := ⟨true, false⟩, channels := ⟨.faithful, .faithful⟩, clamp := false}
def parent_law_10_learned : RemainingDependency.State := {ancestor := {alphabet := ["a"], initial := 0, controlLocation := "reported_episode_complete", outputs := [true, true, false], transitions := [1, 2, 0], table := [(some false), (some true), none], retained := true, componentDone := true}, config := parent_law_10_learned_config, body := {account := {fuel := 444402, start := 713012, spent := 268610, live := 34, peak := 42, capacity := 256}, stocks := ⟨0, 10, 0⟩, context := 1, relay := false, pending := none, held := false, installed := true, retained := true, mode := .serviceIssued, values := ⟨(some true), (some false)⟩, tags := ⟨(some 1), (some 1)⟩, contact := none, candidate := (some false), readMode := (some .selectedBypass), selected := (some false)}}
def parent_law_11_learned_config : RemainingDependency.Config := {weak := ⟨true, true⟩, full := ⟨true, true⟩, channels := ⟨.faithful, .faithful⟩, clamp := false}
def parent_law_11_learned : RemainingDependency.State := {ancestor := {alphabet := ["a"], initial := 0, controlLocation := "reported_episode_complete", outputs := [true, true, false], transitions := [1, 2, 0], table := [(some false), (some true), none], retained := true, componentDone := true}, config := parent_law_11_learned_config, body := {account := {fuel := 444402, start := 713012, spent := 268610, live := 34, peak := 42, capacity := 256}, stocks := ⟨0, 10, 0⟩, context := 1, relay := false, pending := none, held := false, installed := true, retained := true, mode := .serviceIssued, values := ⟨(some true), (some true)⟩, tags := ⟨(some 1), (some 1)⟩, contact := none, candidate := (some false), readMode := (some .selectedBypass), selected := (some false)}}
def parent_source_exhausted_config : RemainingDependency.Config := {weak := ⟨false, true⟩, full := ⟨false, true⟩, channels := ⟨.faithful, .faithful⟩, clamp := false}
def parent_source_exhausted : RemainingDependency.State := {ancestor := {alphabet := ["a"], initial := 0, controlLocation := "reported_episode_complete", outputs := [true, true, false], transitions := [1, 2, 0], table := [(some false), (some true), none], retained := true, componentDone := true}, config := parent_source_exhausted_config, body := {account := {fuel := 642106, start := 909620, spent := 267514, live := 34, peak := 42, capacity := 256}, stocks := ⟨0, 0, 0⟩, context := 1, relay := true, pending := none, held := true, installed := true, retained := true, mode := .selectedRelay, values := ⟨(some false), (some true)⟩, tags := ⟨(some 1), (some 1)⟩, contact := none, candidate := (some true), readMode := (some .selectedRelay), selected := (some true)}}
theorem parent_calibration_break_matches_prior_formal_construction :
  parent_calibration_break = mismatchParent := by decide

theorem parent_false_dependence_matches_prior_formal_construction :
  parent_false_dependence = oldReportErrorParent := by decide

theorem parent_law_01_learned_matches_prior_formal_construction :
  parent_law_01_learned = positiveParent := by decide

theorem mask_encoding_51 :
  (List.range 16).map (51 : Nat).testBit = [true, true, false, false, true, true, false, false, false, false, false, false, false, false, false, false] := by decide

theorem mask_encoding_204 :
  (List.range 16).map (204 : Nat).testBit = [false, false, true, true, false, false, true, true, false, false, false, false, false, false, false, false] := by decide

theorem mask_encoding_255 :
  (List.range 16).map (255 : Nat).testBit = [true, true, true, true, true, true, true, true, false, false, false, false, false, false, false, false] := by decide

theorem mask_encoding_1285 :
  (List.range 16).map (1285 : Nat).testBit = [true, false, true, false, false, false, false, false, true, false, true, false, false, false, false, false] := by decide

theorem mask_encoding_3855 :
  (List.range 16).map (3855 : Nat).testBit = [true, true, true, true, false, false, false, false, true, true, true, true, false, false, false, false] := by decide

theorem mask_encoding_61680 :
  (List.range 16).map (61680 : Nat).testBit = [false, false, false, false, true, true, true, true, false, false, false, false, true, true, true, true] := by decide

theorem mask_encoding_65280 :
  (List.range 16).map (65280 : Nat).testBit = [false, false, false, false, false, false, false, false, true, true, true, true, true, true, true, true] := by decide

theorem mask_encoding_65535 :
  (List.range 16).map (65535 : Nat).testBit = [true, true, true, true, true, true, true, true, true, true, true, true, true, true, true, true] := by decide

def positive_learned_config : Config := {fullFault := .faithful, weakFault := .faithful, clamp := false}
def positive_learned_s0 : State := {parent := parent_law_01_learned, config := positive_learned_config, body := {account := {fuel := 428018, start := 428018, spent := 0, live := 34, peak := 42, capacity := 256}, stocks := ⟨0, 10, 0⟩, context := 1, relay := true, pending := none, held := false, installed := false, retained := false, mask := none, fullRecord := none, weakRecord := none, contact := none, application := .unobserved, diagnosis := .unobserved, proposal := none, activation := none, phase := .oldInterface}}
def positive_learned_s1 : State := {parent := parent_law_01_learned, config := positive_learned_config, body := {account := {fuel := 311680, start := 428018, spent := 116338, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 10, 0⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := false, mask := (some 65535), fullRecord := none, weakRecord := none, contact := none, application := .unobserved, diagnosis := .unobserved, proposal := none, activation := none, phase := .formed}}
def positive_learned_s2 : State := {parent := parent_law_01_learned, config := positive_learned_config, body := {account := {fuel := 295236, start := 428018, spent := 132782, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 10, 0⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := false, mask := (some 65535), fullRecord := none, weakRecord := none, contact := (some ⟨1, true, true⟩), application := .unobserved, diagnosis := .unobserved, proposal := none, activation := none, phase := .formed}}
def positive_learned_s3 : State := {parent := parent_law_01_learned, config := positive_learned_config, body := {account := {fuel := 292044, start := 428018, spent := 135974, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 10, 0⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := false, mask := (some 65535), fullRecord := (some ⟨1, true, true⟩), weakRecord := none, contact := none, application := .unobserved, diagnosis := .unobserved, proposal := none, activation := none, phase := .formed}}
def positive_learned_s4 : State := {parent := parent_law_01_learned, config := positive_learned_config, body := {account := {fuel := 258256, start := 428018, spent := 169762, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 10, 0⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := false, mask := (some 65280), fullRecord := (some ⟨1, true, true⟩), weakRecord := none, contact := none, application := .unobserved, diagnosis := .unobserved, proposal := none, activation := none, phase := .formed}}
def positive_learned_s5 : State := {parent := parent_law_01_learned, config := positive_learned_config, body := {account := {fuel := 255004, start := 428018, spent := 173014, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 10, 0⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := false, mask := (some 65280), fullRecord := (some ⟨1, true, true⟩), weakRecord := none, contact := none, application := .supported, diagnosis := .unobserved, proposal := none, activation := none, phase := .applicationRevised}}
def positive_learned_s6 : State := {parent := parent_law_01_learned, config := positive_learned_config, body := {account := {fuel := 219199, start := 428018, spent := 208819, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 10, 0⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := false, mask := (some 65280), fullRecord := (some ⟨1, true, true⟩), weakRecord := none, contact := none, application := .supported, diagnosis := .unobserved, proposal := none, activation := none, phase := .applicationRevised}}
def positive_learned_s7 : State := {parent := parent_law_01_learned, config := positive_learned_config, body := {account := {fuel := 217031, start := 428018, spent := 210987, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 10, 0⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := false, mask := (some 65280), fullRecord := (some ⟨1, true, true⟩), weakRecord := none, contact := none, application := .supported, diagnosis := .unobserved, proposal := none, activation := none, phase := .committed}}
def positive_learned_s8 : State := {parent := parent_law_01_learned, config := positive_learned_config, body := {account := {fuel := 156499, start := 428018, spent := 271519, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 10, 0⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := true, mask := (some 65280), fullRecord := (some ⟨1, true, true⟩), weakRecord := none, contact := none, application := .supported, diagnosis := .unobserved, proposal := none, activation := none, phase := .committed}}
theorem positive_learned_actual_entrance :
  entrance parent_law_01_learned positive_learned_config = positive_learned_s0 := by decide

theorem positive_learned_initial_whole_account :
  wholeTotal 8419342 positive_learned_s0 = 145 * RemainingDependency.ticks := by decide

theorem positive_learned_event_1 :
  step positive_learned_s0 .install = positive_learned_s1 ∧ RemainingDependency.tariff positive_learned_s0.body.account 24 58 8 65536 0 = 116338 ∧ (RemainingDependency.charge positive_learned_s0.body.account 24 58 8 65536 0).2 = .none := by decide

theorem positive_learned_event_2 :
  step positive_learned_s1 .fullContact = positive_learned_s2 ∧ RemainingDependency.tariff positive_learned_s1.body.account 0 58 2 16384 0 = 16444 ∧ (RemainingDependency.charge positive_learned_s1.body.account 0 58 2 16384 0).2 = .none := by decide

theorem positive_learned_event_3 :
  step positive_learned_s2 .fullWrite = positive_learned_s3 ∧ RemainingDependency.tariff positive_learned_s2.body.account 1 58 2 0 2 = 3192 ∧ (RemainingDependency.charge positive_learned_s2.body.account 1 58 2 0 2).2 = .none := by decide

theorem positive_learned_event_4 :
  step positive_learned_s3 .filterFull = positive_learned_s4 ∧ RemainingDependency.tariff positive_learned_s3.body.account 16 58 2 0 16 = 33788 ∧ (RemainingDependency.charge positive_learned_s3.body.account 16 58 2 0 16).2 = .none := by decide

theorem positive_learned_event_5 :
  step positive_learned_s4 .reviseApplication = positive_learned_s5 ∧ RemainingDependency.tariff positive_learned_s4.body.account 2 58 2 0 1 = 3252 ∧ (RemainingDependency.charge positive_learned_s4.body.account 2 58 2 0 1).2 = .none := by decide

theorem positive_learned_event_6 :
  step positive_learned_s5 .choose = positive_learned_s6 ∧ RemainingDependency.tariff positive_learned_s5.body.account 32 58 3 0 1 = 35805 ∧ (RemainingDependency.charge positive_learned_s5.body.account 32 58 3 0 1).2 = .none := by decide

theorem positive_learned_event_7 :
  step positive_learned_s6 .commit = positive_learned_s7 ∧ RemainingDependency.tariff positive_learned_s6.body.account 1 58 2 0 1 = 2168 ∧ (RemainingDependency.charge positive_learned_s6.body.account 1 58 2 0 1).2 = .none := by decide

theorem positive_learned_event_8 :
  step positive_learned_s7 .retain = positive_learned_s8 ∧ RemainingDependency.tariff positive_learned_s7.body.account 1 58 0 59392 0 = 60532 ∧ (RemainingDependency.charge positive_learned_s7.body.account 1 58 0 59392 0).2 = .none := by decide

theorem positive_learned_saved_run :
  run positive_learned_s0 [.install, .fullContact, .fullWrite, .filterFull, .reviseApplication, .choose, .commit, .retain] = positive_learned_s8 := by decide

theorem positive_learned_core_trace :
  Generative.Trace process positive_learned_s0 [.install, .fullContact, .fullWrite, .filterFull, .reviseApplication, .choose, .commit, .retain] positive_learned_s8 := by
  rw [← positive_learned_saved_run]
  exact run_is_core_trace _ _

theorem positive_learned_final_whole_account :
  wholeTotal 8419342 positive_learned_s8 = 145 * RemainingDependency.ticks := by decide

def positive_clamped_config : Config := {fullFault := .faithful, weakFault := .faithful, clamp := true}
def positive_clamped_s0 : State := {parent := parent_law_01_learned, config := positive_clamped_config, body := {account := {fuel := 428018, start := 428018, spent := 0, live := 34, peak := 42, capacity := 256}, stocks := ⟨0, 10, 0⟩, context := 1, relay := true, pending := none, held := false, installed := false, retained := false, mask := none, fullRecord := none, weakRecord := none, contact := none, application := .unobserved, diagnosis := .unobserved, proposal := none, activation := none, phase := .oldInterface}}
def positive_clamped_s1 : State := {parent := parent_law_01_learned, config := positive_clamped_config, body := {account := {fuel := 311680, start := 428018, spent := 116338, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 10, 0⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := false, mask := (some 65535), fullRecord := none, weakRecord := none, contact := none, application := .unobserved, diagnosis := .unobserved, proposal := none, activation := none, phase := .formed}}
def positive_clamped_s2 : State := {parent := parent_law_01_learned, config := positive_clamped_config, body := {account := {fuel := 295236, start := 428018, spent := 132782, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 10, 0⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := false, mask := (some 65535), fullRecord := none, weakRecord := none, contact := (some ⟨1, true, true⟩), application := .unobserved, diagnosis := .unobserved, proposal := none, activation := none, phase := .formed}}
def positive_clamped_s3 : State := {parent := parent_law_01_learned, config := positive_clamped_config, body := {account := {fuel := 292044, start := 428018, spent := 135974, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 10, 0⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := false, mask := (some 65535), fullRecord := (some ⟨1, true, true⟩), weakRecord := none, contact := none, application := .unobserved, diagnosis := .unobserved, proposal := none, activation := none, phase := .formed}}
def positive_clamped_s4 : State := {parent := parent_law_01_learned, config := positive_clamped_config, body := {account := {fuel := 258256, start := 428018, spent := 169762, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 10, 0⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := false, mask := (some 65280), fullRecord := (some ⟨1, true, true⟩), weakRecord := none, contact := none, application := .unobserved, diagnosis := .unobserved, proposal := none, activation := none, phase := .formed}}
def positive_clamped_s5 : State := {parent := parent_law_01_learned, config := positive_clamped_config, body := {account := {fuel := 255004, start := 428018, spent := 173014, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 10, 0⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := false, mask := (some 65280), fullRecord := (some ⟨1, true, true⟩), weakRecord := none, contact := none, application := .supported, diagnosis := .unobserved, proposal := none, activation := none, phase := .applicationRevised}}
def positive_clamped_s6 : State := {parent := parent_law_01_learned, config := positive_clamped_config, body := {account := {fuel := 219199, start := 428018, spent := 208819, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 10, 0⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := false, mask := (some 65280), fullRecord := (some ⟨1, true, true⟩), weakRecord := none, contact := none, application := .supported, diagnosis := .unobserved, proposal := none, activation := none, phase := .applicationRevised}}
def positive_clamped_s7 : State := {parent := parent_law_01_learned, config := positive_clamped_config, body := {account := {fuel := 217031, start := 428018, spent := 210987, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 10, 0⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := false, mask := (some 65280), fullRecord := (some ⟨1, true, true⟩), weakRecord := none, contact := none, application := .supported, diagnosis := .unobserved, proposal := none, activation := none, phase := .committed}}
def positive_clamped_s8 : State := {parent := parent_law_01_learned, config := positive_clamped_config, body := {account := {fuel := 156499, start := 428018, spent := 271519, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 10, 0⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := true, mask := (some 65280), fullRecord := (some ⟨1, true, true⟩), weakRecord := none, contact := none, application := .supported, diagnosis := .unobserved, proposal := none, activation := none, phase := .committed}}
theorem positive_clamped_actual_entrance :
  entrance parent_law_01_learned positive_clamped_config = positive_clamped_s0 := by decide

theorem positive_clamped_initial_whole_account :
  wholeTotal 8419342 positive_clamped_s0 = 145 * RemainingDependency.ticks := by decide

theorem positive_clamped_event_1 :
  step positive_clamped_s0 .install = positive_clamped_s1 ∧ RemainingDependency.tariff positive_clamped_s0.body.account 24 58 8 65536 0 = 116338 ∧ (RemainingDependency.charge positive_clamped_s0.body.account 24 58 8 65536 0).2 = .none := by decide

theorem positive_clamped_event_2 :
  step positive_clamped_s1 .fullContact = positive_clamped_s2 ∧ RemainingDependency.tariff positive_clamped_s1.body.account 0 58 2 16384 0 = 16444 ∧ (RemainingDependency.charge positive_clamped_s1.body.account 0 58 2 16384 0).2 = .none := by decide

theorem positive_clamped_event_3 :
  step positive_clamped_s2 .fullWrite = positive_clamped_s3 ∧ RemainingDependency.tariff positive_clamped_s2.body.account 1 58 2 0 2 = 3192 ∧ (RemainingDependency.charge positive_clamped_s2.body.account 1 58 2 0 2).2 = .none := by decide

theorem positive_clamped_event_4 :
  step positive_clamped_s3 .filterFull = positive_clamped_s4 ∧ RemainingDependency.tariff positive_clamped_s3.body.account 16 58 2 0 16 = 33788 ∧ (RemainingDependency.charge positive_clamped_s3.body.account 16 58 2 0 16).2 = .none := by decide

theorem positive_clamped_event_5 :
  step positive_clamped_s4 .reviseApplication = positive_clamped_s5 ∧ RemainingDependency.tariff positive_clamped_s4.body.account 2 58 2 0 1 = 3252 ∧ (RemainingDependency.charge positive_clamped_s4.body.account 2 58 2 0 1).2 = .none := by decide

theorem positive_clamped_event_6 :
  step positive_clamped_s5 .choose = positive_clamped_s6 ∧ RemainingDependency.tariff positive_clamped_s5.body.account 32 58 3 0 1 = 35805 ∧ (RemainingDependency.charge positive_clamped_s5.body.account 32 58 3 0 1).2 = .none := by decide

theorem positive_clamped_event_7 :
  step positive_clamped_s6 .commit = positive_clamped_s7 ∧ RemainingDependency.tariff positive_clamped_s6.body.account 1 58 2 0 1 = 2168 ∧ (RemainingDependency.charge positive_clamped_s6.body.account 1 58 2 0 1).2 = .none := by decide

theorem positive_clamped_event_8 :
  step positive_clamped_s7 .retain = positive_clamped_s8 ∧ RemainingDependency.tariff positive_clamped_s7.body.account 1 58 0 59392 0 = 60532 ∧ (RemainingDependency.charge positive_clamped_s7.body.account 1 58 0 59392 0).2 = .none := by decide

theorem positive_clamped_saved_run :
  run positive_clamped_s0 [.install, .fullContact, .fullWrite, .filterFull, .reviseApplication, .choose, .commit, .retain] = positive_clamped_s8 := by decide

theorem positive_clamped_core_trace :
  Generative.Trace process positive_clamped_s0 [.install, .fullContact, .fullWrite, .filterFull, .reviseApplication, .choose, .commit, .retain] positive_clamped_s8 := by
  rw [← positive_clamped_saved_run]
  exact run_is_core_trace _ _

theorem positive_clamped_final_whole_account :
  wholeTotal 8419342 positive_clamped_s8 = 145 * RemainingDependency.ticks := by decide

def positive_conventional_config : Config := {fullFault := .faithful, weakFault := .faithful, clamp := false}
def positive_conventional_s0 : State := {parent := parent_law_01_learned, config := positive_conventional_config, body := {account := {fuel := 428018, start := 428018, spent := 0, live := 34, peak := 42, capacity := 256}, stocks := ⟨0, 10, 0⟩, context := 1, relay := true, pending := none, held := false, installed := false, retained := false, mask := none, fullRecord := none, weakRecord := none, contact := none, application := .unobserved, diagnosis := .unobserved, proposal := none, activation := none, phase := .oldInterface}}
def positive_conventional_s1 : State := {parent := parent_law_01_learned, config := positive_conventional_config, body := {account := {fuel := 311680, start := 428018, spent := 116338, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 10, 0⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := false, mask := (some 65535), fullRecord := none, weakRecord := none, contact := none, application := .unobserved, diagnosis := .unobserved, proposal := none, activation := none, phase := .formed}}
def positive_conventional_s2 : State := {parent := parent_law_01_learned, config := positive_conventional_config, body := {account := {fuel := 295236, start := 428018, spent := 132782, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 10, 0⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := false, mask := (some 65535), fullRecord := none, weakRecord := none, contact := (some ⟨1, true, true⟩), application := .unobserved, diagnosis := .unobserved, proposal := none, activation := none, phase := .formed}}
def positive_conventional_s3 : State := {parent := parent_law_01_learned, config := positive_conventional_config, body := {account := {fuel := 292044, start := 428018, spent := 135974, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 10, 0⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := false, mask := (some 65535), fullRecord := (some ⟨1, true, true⟩), weakRecord := none, contact := none, application := .unobserved, diagnosis := .unobserved, proposal := none, activation := none, phase := .formed}}
def positive_conventional_s4 : State := {parent := parent_law_01_learned, config := positive_conventional_config, body := {account := {fuel := 258256, start := 428018, spent := 169762, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 10, 0⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := false, mask := (some 65280), fullRecord := (some ⟨1, true, true⟩), weakRecord := none, contact := none, application := .unobserved, diagnosis := .unobserved, proposal := none, activation := none, phase := .formed}}
def positive_conventional_s5 : State := {parent := parent_law_01_learned, config := positive_conventional_config, body := {account := {fuel := 255004, start := 428018, spent := 173014, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 10, 0⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := false, mask := (some 65280), fullRecord := (some ⟨1, true, true⟩), weakRecord := none, contact := none, application := .supported, diagnosis := .unobserved, proposal := none, activation := none, phase := .applicationRevised}}
def positive_conventional_s6 : State := {parent := parent_law_01_learned, config := positive_conventional_config, body := {account := {fuel := 219199, start := 428018, spent := 208819, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 10, 0⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := false, mask := (some 65280), fullRecord := (some ⟨1, true, true⟩), weakRecord := none, contact := none, application := .supported, diagnosis := .unobserved, proposal := none, activation := none, phase := .applicationRevised}}
def positive_conventional_s7 : State := {parent := parent_law_01_learned, config := positive_conventional_config, body := {account := {fuel := 217031, start := 428018, spent := 210987, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 10, 0⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := false, mask := (some 65280), fullRecord := (some ⟨1, true, true⟩), weakRecord := none, contact := none, application := .supported, diagnosis := .unobserved, proposal := none, activation := none, phase := .committed}}
def positive_conventional_s8 : State := {parent := parent_law_01_learned, config := positive_conventional_config, body := {account := {fuel := 156499, start := 428018, spent := 271519, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 10, 0⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := true, mask := (some 65280), fullRecord := (some ⟨1, true, true⟩), weakRecord := none, contact := none, application := .supported, diagnosis := .unobserved, proposal := none, activation := none, phase := .committed}}
theorem positive_conventional_actual_entrance :
  entrance parent_law_01_learned positive_conventional_config = positive_conventional_s0 := by decide

theorem positive_conventional_initial_whole_account :
  wholeTotal 8419342 positive_conventional_s0 = 145 * RemainingDependency.ticks := by decide

theorem positive_conventional_event_1 :
  step positive_conventional_s0 .install = positive_conventional_s1 ∧ RemainingDependency.tariff positive_conventional_s0.body.account 24 58 8 65536 0 = 116338 ∧ (RemainingDependency.charge positive_conventional_s0.body.account 24 58 8 65536 0).2 = .none := by decide

theorem positive_conventional_event_2 :
  step positive_conventional_s1 .fullContact = positive_conventional_s2 ∧ RemainingDependency.tariff positive_conventional_s1.body.account 0 58 2 16384 0 = 16444 ∧ (RemainingDependency.charge positive_conventional_s1.body.account 0 58 2 16384 0).2 = .none := by decide

theorem positive_conventional_event_3 :
  step positive_conventional_s2 .fullWrite = positive_conventional_s3 ∧ RemainingDependency.tariff positive_conventional_s2.body.account 1 58 2 0 2 = 3192 ∧ (RemainingDependency.charge positive_conventional_s2.body.account 1 58 2 0 2).2 = .none := by decide

theorem positive_conventional_event_4 :
  step positive_conventional_s3 .filterFull = positive_conventional_s4 ∧ RemainingDependency.tariff positive_conventional_s3.body.account 16 58 2 0 16 = 33788 ∧ (RemainingDependency.charge positive_conventional_s3.body.account 16 58 2 0 16).2 = .none := by decide

theorem positive_conventional_event_5 :
  step positive_conventional_s4 .reviseApplication = positive_conventional_s5 ∧ RemainingDependency.tariff positive_conventional_s4.body.account 2 58 2 0 1 = 3252 ∧ (RemainingDependency.charge positive_conventional_s4.body.account 2 58 2 0 1).2 = .none := by decide

theorem positive_conventional_event_6 :
  step positive_conventional_s5 .choose = positive_conventional_s6 ∧ RemainingDependency.tariff positive_conventional_s5.body.account 32 58 3 0 1 = 35805 ∧ (RemainingDependency.charge positive_conventional_s5.body.account 32 58 3 0 1).2 = .none := by decide

theorem positive_conventional_event_7 :
  step positive_conventional_s6 .commit = positive_conventional_s7 ∧ RemainingDependency.tariff positive_conventional_s6.body.account 1 58 2 0 1 = 2168 ∧ (RemainingDependency.charge positive_conventional_s6.body.account 1 58 2 0 1).2 = .none := by decide

theorem positive_conventional_event_8 :
  step positive_conventional_s7 .retain = positive_conventional_s8 ∧ RemainingDependency.tariff positive_conventional_s7.body.account 1 58 0 59392 0 = 60532 ∧ (RemainingDependency.charge positive_conventional_s7.body.account 1 58 0 59392 0).2 = .none := by decide

theorem positive_conventional_saved_run :
  run positive_conventional_s0 [.install, .fullContact, .fullWrite, .filterFull, .reviseApplication, .choose, .commit, .retain] = positive_conventional_s8 := by decide

theorem positive_conventional_core_trace :
  Generative.Trace process positive_conventional_s0 [.install, .fullContact, .fullWrite, .filterFull, .reviseApplication, .choose, .commit, .retain] positive_conventional_s8 := by
  rw [← positive_conventional_saved_run]
  exact run_is_core_trace _ _

theorem positive_conventional_final_whole_account :
  wholeTotal 8419342 positive_conventional_s8 = 145 * RemainingDependency.ticks := by decide

def mismatch_learned_config : Config := {fullFault := .faithful, weakFault := .faithful, clamp := false}
def mismatch_learned_s0 : State := {parent := parent_calibration_break, config := mismatch_learned_config, body := {account := {fuel := 428018, start := 428018, spent := 0, live := 34, peak := 42, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := false, retained := false, mask := none, fullRecord := none, weakRecord := none, contact := none, application := .unobserved, diagnosis := .unobserved, proposal := none, activation := none, phase := .oldInterface}}
def mismatch_learned_s1 : State := {parent := parent_calibration_break, config := mismatch_learned_config, body := {account := {fuel := 311680, start := 428018, spent := 116338, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := false, mask := (some 65535), fullRecord := none, weakRecord := none, contact := none, application := .unobserved, diagnosis := .unobserved, proposal := none, activation := none, phase := .formed}}
def mismatch_learned_s2 : State := {parent := parent_calibration_break, config := mismatch_learned_config, body := {account := {fuel := 295236, start := 428018, spent := 132782, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := false, mask := (some 65535), fullRecord := none, weakRecord := none, contact := (some ⟨1, true, false⟩), application := .unobserved, diagnosis := .unobserved, proposal := none, activation := none, phase := .formed}}
def mismatch_learned_s3 : State := {parent := parent_calibration_break, config := mismatch_learned_config, body := {account := {fuel := 292044, start := 428018, spent := 135974, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := false, mask := (some 65535), fullRecord := (some ⟨1, true, false⟩), weakRecord := none, contact := none, application := .unobserved, diagnosis := .unobserved, proposal := none, activation := none, phase := .formed}}
def mismatch_learned_s4 : State := {parent := parent_calibration_break, config := mismatch_learned_config, body := {account := {fuel := 258256, start := 428018, spent := 169762, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := false, mask := (some 255), fullRecord := (some ⟨1, true, false⟩), weakRecord := none, contact := none, application := .unobserved, diagnosis := .unobserved, proposal := none, activation := none, phase := .formed}}
def mismatch_learned_s5 : State := {parent := parent_calibration_break, config := mismatch_learned_config, body := {account := {fuel := 255004, start := 428018, spent := 173014, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := false, mask := (some 255), fullRecord := (some ⟨1, true, false⟩), weakRecord := none, contact := none, application := .failed, diagnosis := .unobserved, proposal := none, activation := none, phase := .applicationRevised}}
def mismatch_learned_s6 : State := {parent := parent_calibration_break, config := mismatch_learned_config, body := {account := {fuel := 219199, start := 428018, spent := 208819, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := false, mask := (some 255), fullRecord := (some ⟨1, true, false⟩), weakRecord := none, contact := none, application := .failed, diagnosis := .unobserved, proposal := (some true), activation := none, phase := .applicationRevised}}
def mismatch_learned_s7 : State := {parent := parent_calibration_break, config := mismatch_learned_config, body := {account := {fuel := 217031, start := 428018, spent := 210987, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := false, mask := (some 255), fullRecord := (some ⟨1, true, false⟩), weakRecord := none, contact := none, application := .failed, diagnosis := .unobserved, proposal := (some true), activation := (some true), phase := .committed}}
def mismatch_learned_s8 : State := {parent := parent_calibration_break, config := mismatch_learned_config, body := {account := {fuel := 199503, start := 428018, spent := 228515, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := false, mask := (some 255), fullRecord := (some ⟨1, true, false⟩), weakRecord := none, contact := none, application := .failed, diagnosis := .unobserved, proposal := (some true), activation := (some true), phase := .committed}}
def mismatch_learned_s9 : State := {parent := parent_calibration_break, config := mismatch_learned_config, body := {account := {fuel := 181975, start := 428018, spent := 246043, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := (some ⟨1, true, true⟩), held := false, installed := true, retained := false, mask := (some 255), fullRecord := (some ⟨1, true, false⟩), weakRecord := none, contact := none, application := .failed, diagnosis := .unobserved, proposal := (some true), activation := (some true), phase := .committed}}
def mismatch_learned_s10 : State := {parent := parent_calibration_break, config := mismatch_learned_config, body := {account := {fuel := 165531, start := 428018, spent := 262487, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := false, mask := (some 255), fullRecord := (some ⟨1, true, false⟩), weakRecord := none, contact := (some ⟨1, true, true⟩), application := .failed, diagnosis := .unobserved, proposal := (some true), activation := (some true), phase := .committed}}
def mismatch_learned_s11 : State := {parent := parent_calibration_break, config := mismatch_learned_config, body := {account := {fuel := 162339, start := 428018, spent := 265679, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := false, mask := (some 255), fullRecord := (some ⟨1, true, false⟩), weakRecord := (some ⟨1, true, true⟩), contact := none, application := .failed, diagnosis := .unobserved, proposal := (some true), activation := (some true), phase := .committed}}
def mismatch_learned_s12 : State := {parent := parent_calibration_break, config := mismatch_learned_config, body := {account := {fuel := 128551, start := 428018, spent := 299467, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := false, mask := (some 204), fullRecord := (some ⟨1, true, false⟩), weakRecord := (some ⟨1, true, true⟩), contact := none, application := .failed, diagnosis := .unobserved, proposal := (some true), activation := (some true), phase := .committed}}
def mismatch_learned_s13 : State := {parent := parent_calibration_break, config := mismatch_learned_config, body := {account := {fuel := 125299, start := 428018, spent := 302719, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := false, mask := (some 204), fullRecord := (some ⟨1, true, false⟩), weakRecord := (some ⟨1, true, true⟩), contact := none, application := .failed, diagnosis := .discrepancy, proposal := (some true), activation := (some true), phase := .diagnosisRevised}}
def mismatch_learned_s14 : State := {parent := parent_calibration_break, config := mismatch_learned_config, body := {account := {fuel := 64767, start := 428018, spent := 363251, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := true, mask := (some 204), fullRecord := (some ⟨1, true, false⟩), weakRecord := (some ⟨1, true, true⟩), contact := none, application := .failed, diagnosis := .discrepancy, proposal := (some true), activation := (some true), phase := .diagnosisRevised}}
theorem mismatch_learned_actual_entrance :
  entrance parent_calibration_break mismatch_learned_config = mismatch_learned_s0 := by decide

theorem mismatch_learned_initial_whole_account :
  wholeTotal 8419342 mismatch_learned_s0 = 145 * RemainingDependency.ticks := by decide

theorem mismatch_learned_event_1 :
  step mismatch_learned_s0 .install = mismatch_learned_s1 ∧ RemainingDependency.tariff mismatch_learned_s0.body.account 24 58 8 65536 0 = 116338 ∧ (RemainingDependency.charge mismatch_learned_s0.body.account 24 58 8 65536 0).2 = .none := by decide

theorem mismatch_learned_event_2 :
  step mismatch_learned_s1 .fullContact = mismatch_learned_s2 ∧ RemainingDependency.tariff mismatch_learned_s1.body.account 0 58 2 16384 0 = 16444 ∧ (RemainingDependency.charge mismatch_learned_s1.body.account 0 58 2 16384 0).2 = .none := by decide

theorem mismatch_learned_event_3 :
  step mismatch_learned_s2 .fullWrite = mismatch_learned_s3 ∧ RemainingDependency.tariff mismatch_learned_s2.body.account 1 58 2 0 2 = 3192 ∧ (RemainingDependency.charge mismatch_learned_s2.body.account 1 58 2 0 2).2 = .none := by decide

theorem mismatch_learned_event_4 :
  step mismatch_learned_s3 .filterFull = mismatch_learned_s4 ∧ RemainingDependency.tariff mismatch_learned_s3.body.account 16 58 2 0 16 = 33788 ∧ (RemainingDependency.charge mismatch_learned_s3.body.account 16 58 2 0 16).2 = .none := by decide

theorem mismatch_learned_event_5 :
  step mismatch_learned_s4 .reviseApplication = mismatch_learned_s5 ∧ RemainingDependency.tariff mismatch_learned_s4.body.account 2 58 2 0 1 = 3252 ∧ (RemainingDependency.charge mismatch_learned_s4.body.account 2 58 2 0 1).2 = .none := by decide

theorem mismatch_learned_event_6 :
  step mismatch_learned_s5 .choose = mismatch_learned_s6 ∧ RemainingDependency.tariff mismatch_learned_s5.body.account 32 58 3 0 1 = 35805 ∧ (RemainingDependency.charge mismatch_learned_s5.body.account 32 58 3 0 1).2 = .none := by decide

theorem mismatch_learned_event_7 :
  step mismatch_learned_s6 .commit = mismatch_learned_s7 ∧ RemainingDependency.tariff mismatch_learned_s6.body.account 1 58 2 0 1 = 2168 ∧ (RemainingDependency.charge mismatch_learned_s6.body.account 1 58 2 0 1).2 = .none := by decide

theorem mismatch_learned_event_8 :
  step mismatch_learned_s7 (.command true) = mismatch_learned_s8 ∧ RemainingDependency.tariff mismatch_learned_s7.body.account 1 58 2 16384 0 = 17528 ∧ (RemainingDependency.charge mismatch_learned_s7.body.account 1 58 2 16384 0).2 = .none := by decide

theorem mismatch_learned_event_9 :
  step mismatch_learned_s8 .challenge = mismatch_learned_s9 ∧ RemainingDependency.tariff mismatch_learned_s8.body.account 1 58 2 16384 0 = 17528 ∧ (RemainingDependency.charge mismatch_learned_s8.body.account 1 58 2 16384 0).2 = .none := by decide

theorem mismatch_learned_event_10 :
  step mismatch_learned_s9 .weakContact = mismatch_learned_s10 ∧ RemainingDependency.tariff mismatch_learned_s9.body.account 0 58 2 16384 0 = 16444 ∧ (RemainingDependency.charge mismatch_learned_s9.body.account 0 58 2 16384 0).2 = .none := by decide

theorem mismatch_learned_event_11 :
  step mismatch_learned_s10 .weakWrite = mismatch_learned_s11 ∧ RemainingDependency.tariff mismatch_learned_s10.body.account 1 58 2 0 2 = 3192 ∧ (RemainingDependency.charge mismatch_learned_s10.body.account 1 58 2 0 2).2 = .none := by decide

theorem mismatch_learned_event_12 :
  step mismatch_learned_s11 .filterWeak = mismatch_learned_s12 ∧ RemainingDependency.tariff mismatch_learned_s11.body.account 16 58 2 0 16 = 33788 ∧ (RemainingDependency.charge mismatch_learned_s11.body.account 16 58 2 0 16).2 = .none := by decide

theorem mismatch_learned_event_13 :
  step mismatch_learned_s12 .reviseDiagnosis = mismatch_learned_s13 ∧ RemainingDependency.tariff mismatch_learned_s12.body.account 2 58 2 0 1 = 3252 ∧ (RemainingDependency.charge mismatch_learned_s12.body.account 2 58 2 0 1).2 = .none := by decide

theorem mismatch_learned_event_14 :
  step mismatch_learned_s13 .retain = mismatch_learned_s14 ∧ RemainingDependency.tariff mismatch_learned_s13.body.account 1 58 0 59392 0 = 60532 ∧ (RemainingDependency.charge mismatch_learned_s13.body.account 1 58 0 59392 0).2 = .none := by decide

theorem mismatch_learned_saved_run :
  run mismatch_learned_s0 [.install, .fullContact, .fullWrite, .filterFull, .reviseApplication, .choose, .commit, (.command true), .challenge, .weakContact, .weakWrite, .filterWeak, .reviseDiagnosis, .retain] = mismatch_learned_s14 := by decide

theorem mismatch_learned_core_trace :
  Generative.Trace process mismatch_learned_s0 [.install, .fullContact, .fullWrite, .filterFull, .reviseApplication, .choose, .commit, (.command true), .challenge, .weakContact, .weakWrite, .filterWeak, .reviseDiagnosis, .retain] mismatch_learned_s14 := by
  rw [← mismatch_learned_saved_run]
  exact run_is_core_trace _ _

theorem mismatch_learned_final_whole_account :
  wholeTotal 8419342 mismatch_learned_s14 = 145 * RemainingDependency.ticks := by decide

def mismatch_clamped_config : Config := {fullFault := .faithful, weakFault := .faithful, clamp := true}
def mismatch_clamped_s0 : State := {parent := parent_calibration_break, config := mismatch_clamped_config, body := {account := {fuel := 428018, start := 428018, spent := 0, live := 34, peak := 42, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := false, retained := false, mask := none, fullRecord := none, weakRecord := none, contact := none, application := .unobserved, diagnosis := .unobserved, proposal := none, activation := none, phase := .oldInterface}}
def mismatch_clamped_s1 : State := {parent := parent_calibration_break, config := mismatch_clamped_config, body := {account := {fuel := 311680, start := 428018, spent := 116338, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := false, mask := (some 65535), fullRecord := none, weakRecord := none, contact := none, application := .unobserved, diagnosis := .unobserved, proposal := none, activation := none, phase := .formed}}
def mismatch_clamped_s2 : State := {parent := parent_calibration_break, config := mismatch_clamped_config, body := {account := {fuel := 295236, start := 428018, spent := 132782, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := false, mask := (some 65535), fullRecord := none, weakRecord := none, contact := (some ⟨1, true, false⟩), application := .unobserved, diagnosis := .unobserved, proposal := none, activation := none, phase := .formed}}
def mismatch_clamped_s3 : State := {parent := parent_calibration_break, config := mismatch_clamped_config, body := {account := {fuel := 292044, start := 428018, spent := 135974, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := false, mask := (some 65535), fullRecord := (some ⟨1, true, false⟩), weakRecord := none, contact := none, application := .unobserved, diagnosis := .unobserved, proposal := none, activation := none, phase := .formed}}
def mismatch_clamped_s4 : State := {parent := parent_calibration_break, config := mismatch_clamped_config, body := {account := {fuel := 258256, start := 428018, spent := 169762, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := false, mask := (some 255), fullRecord := (some ⟨1, true, false⟩), weakRecord := none, contact := none, application := .unobserved, diagnosis := .unobserved, proposal := none, activation := none, phase := .formed}}
def mismatch_clamped_s5 : State := {parent := parent_calibration_break, config := mismatch_clamped_config, body := {account := {fuel := 255004, start := 428018, spent := 173014, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := false, mask := (some 255), fullRecord := (some ⟨1, true, false⟩), weakRecord := none, contact := none, application := .failed, diagnosis := .unobserved, proposal := none, activation := none, phase := .applicationRevised}}
def mismatch_clamped_s6 : State := {parent := parent_calibration_break, config := mismatch_clamped_config, body := {account := {fuel := 219199, start := 428018, spent := 208819, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := false, mask := (some 255), fullRecord := (some ⟨1, true, false⟩), weakRecord := none, contact := none, application := .failed, diagnosis := .unobserved, proposal := (some true), activation := none, phase := .applicationRevised}}
def mismatch_clamped_s7 : State := {parent := parent_calibration_break, config := mismatch_clamped_config, body := {account := {fuel := 217031, start := 428018, spent := 210987, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := false, mask := (some 255), fullRecord := (some ⟨1, true, false⟩), weakRecord := none, contact := none, application := .failed, diagnosis := .unobserved, proposal := (some true), activation := none, phase := .committed}}
def mismatch_clamped_s8 : State := {parent := parent_calibration_break, config := mismatch_clamped_config, body := {account := {fuel := 156499, start := 428018, spent := 271519, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := true, mask := (some 255), fullRecord := (some ⟨1, true, false⟩), weakRecord := none, contact := none, application := .failed, diagnosis := .unobserved, proposal := (some true), activation := none, phase := .committed}}
theorem mismatch_clamped_actual_entrance :
  entrance parent_calibration_break mismatch_clamped_config = mismatch_clamped_s0 := by decide

theorem mismatch_clamped_initial_whole_account :
  wholeTotal 8419342 mismatch_clamped_s0 = 145 * RemainingDependency.ticks := by decide

theorem mismatch_clamped_event_1 :
  step mismatch_clamped_s0 .install = mismatch_clamped_s1 ∧ RemainingDependency.tariff mismatch_clamped_s0.body.account 24 58 8 65536 0 = 116338 ∧ (RemainingDependency.charge mismatch_clamped_s0.body.account 24 58 8 65536 0).2 = .none := by decide

theorem mismatch_clamped_event_2 :
  step mismatch_clamped_s1 .fullContact = mismatch_clamped_s2 ∧ RemainingDependency.tariff mismatch_clamped_s1.body.account 0 58 2 16384 0 = 16444 ∧ (RemainingDependency.charge mismatch_clamped_s1.body.account 0 58 2 16384 0).2 = .none := by decide

theorem mismatch_clamped_event_3 :
  step mismatch_clamped_s2 .fullWrite = mismatch_clamped_s3 ∧ RemainingDependency.tariff mismatch_clamped_s2.body.account 1 58 2 0 2 = 3192 ∧ (RemainingDependency.charge mismatch_clamped_s2.body.account 1 58 2 0 2).2 = .none := by decide

theorem mismatch_clamped_event_4 :
  step mismatch_clamped_s3 .filterFull = mismatch_clamped_s4 ∧ RemainingDependency.tariff mismatch_clamped_s3.body.account 16 58 2 0 16 = 33788 ∧ (RemainingDependency.charge mismatch_clamped_s3.body.account 16 58 2 0 16).2 = .none := by decide

theorem mismatch_clamped_event_5 :
  step mismatch_clamped_s4 .reviseApplication = mismatch_clamped_s5 ∧ RemainingDependency.tariff mismatch_clamped_s4.body.account 2 58 2 0 1 = 3252 ∧ (RemainingDependency.charge mismatch_clamped_s4.body.account 2 58 2 0 1).2 = .none := by decide

theorem mismatch_clamped_event_6 :
  step mismatch_clamped_s5 .choose = mismatch_clamped_s6 ∧ RemainingDependency.tariff mismatch_clamped_s5.body.account 32 58 3 0 1 = 35805 ∧ (RemainingDependency.charge mismatch_clamped_s5.body.account 32 58 3 0 1).2 = .none := by decide

theorem mismatch_clamped_event_7 :
  step mismatch_clamped_s6 .commit = mismatch_clamped_s7 ∧ RemainingDependency.tariff mismatch_clamped_s6.body.account 1 58 2 0 1 = 2168 ∧ (RemainingDependency.charge mismatch_clamped_s6.body.account 1 58 2 0 1).2 = .none := by decide

theorem mismatch_clamped_event_8 :
  step mismatch_clamped_s7 .retain = mismatch_clamped_s8 ∧ RemainingDependency.tariff mismatch_clamped_s7.body.account 1 58 0 59392 0 = 60532 ∧ (RemainingDependency.charge mismatch_clamped_s7.body.account 1 58 0 59392 0).2 = .none := by decide

theorem mismatch_clamped_saved_run :
  run mismatch_clamped_s0 [.install, .fullContact, .fullWrite, .filterFull, .reviseApplication, .choose, .commit, .retain] = mismatch_clamped_s8 := by decide

theorem mismatch_clamped_core_trace :
  Generative.Trace process mismatch_clamped_s0 [.install, .fullContact, .fullWrite, .filterFull, .reviseApplication, .choose, .commit, .retain] mismatch_clamped_s8 := by
  rw [← mismatch_clamped_saved_run]
  exact run_is_core_trace _ _

theorem mismatch_clamped_final_whole_account :
  wholeTotal 8419342 mismatch_clamped_s8 = 145 * RemainingDependency.ticks := by decide

def mismatch_conventional_config : Config := {fullFault := .faithful, weakFault := .faithful, clamp := false}
def mismatch_conventional_s0 : State := {parent := parent_calibration_break, config := mismatch_conventional_config, body := {account := {fuel := 428018, start := 428018, spent := 0, live := 34, peak := 42, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := false, retained := false, mask := none, fullRecord := none, weakRecord := none, contact := none, application := .unobserved, diagnosis := .unobserved, proposal := none, activation := none, phase := .oldInterface}}
def mismatch_conventional_s1 : State := {parent := parent_calibration_break, config := mismatch_conventional_config, body := {account := {fuel := 311680, start := 428018, spent := 116338, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := false, mask := (some 65535), fullRecord := none, weakRecord := none, contact := none, application := .unobserved, diagnosis := .unobserved, proposal := none, activation := none, phase := .formed}}
def mismatch_conventional_s2 : State := {parent := parent_calibration_break, config := mismatch_conventional_config, body := {account := {fuel := 295236, start := 428018, spent := 132782, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := false, mask := (some 65535), fullRecord := none, weakRecord := none, contact := (some ⟨1, true, false⟩), application := .unobserved, diagnosis := .unobserved, proposal := none, activation := none, phase := .formed}}
def mismatch_conventional_s3 : State := {parent := parent_calibration_break, config := mismatch_conventional_config, body := {account := {fuel := 292044, start := 428018, spent := 135974, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := false, mask := (some 65535), fullRecord := (some ⟨1, true, false⟩), weakRecord := none, contact := none, application := .unobserved, diagnosis := .unobserved, proposal := none, activation := none, phase := .formed}}
def mismatch_conventional_s4 : State := {parent := parent_calibration_break, config := mismatch_conventional_config, body := {account := {fuel := 258256, start := 428018, spent := 169762, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := false, mask := (some 255), fullRecord := (some ⟨1, true, false⟩), weakRecord := none, contact := none, application := .unobserved, diagnosis := .unobserved, proposal := none, activation := none, phase := .formed}}
def mismatch_conventional_s5 : State := {parent := parent_calibration_break, config := mismatch_conventional_config, body := {account := {fuel := 255004, start := 428018, spent := 173014, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := false, mask := (some 255), fullRecord := (some ⟨1, true, false⟩), weakRecord := none, contact := none, application := .failed, diagnosis := .unobserved, proposal := none, activation := none, phase := .applicationRevised}}
def mismatch_conventional_s6 : State := {parent := parent_calibration_break, config := mismatch_conventional_config, body := {account := {fuel := 219199, start := 428018, spent := 208819, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := false, mask := (some 255), fullRecord := (some ⟨1, true, false⟩), weakRecord := none, contact := none, application := .failed, diagnosis := .unobserved, proposal := (some true), activation := none, phase := .applicationRevised}}
def mismatch_conventional_s7 : State := {parent := parent_calibration_break, config := mismatch_conventional_config, body := {account := {fuel := 217031, start := 428018, spent := 210987, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := false, mask := (some 255), fullRecord := (some ⟨1, true, false⟩), weakRecord := none, contact := none, application := .failed, diagnosis := .unobserved, proposal := (some true), activation := (some true), phase := .committed}}
def mismatch_conventional_s8 : State := {parent := parent_calibration_break, config := mismatch_conventional_config, body := {account := {fuel := 199503, start := 428018, spent := 228515, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := false, mask := (some 255), fullRecord := (some ⟨1, true, false⟩), weakRecord := none, contact := none, application := .failed, diagnosis := .unobserved, proposal := (some true), activation := (some true), phase := .committed}}
def mismatch_conventional_s9 : State := {parent := parent_calibration_break, config := mismatch_conventional_config, body := {account := {fuel := 181975, start := 428018, spent := 246043, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := (some ⟨1, true, true⟩), held := false, installed := true, retained := false, mask := (some 255), fullRecord := (some ⟨1, true, false⟩), weakRecord := none, contact := none, application := .failed, diagnosis := .unobserved, proposal := (some true), activation := (some true), phase := .committed}}
def mismatch_conventional_s10 : State := {parent := parent_calibration_break, config := mismatch_conventional_config, body := {account := {fuel := 165531, start := 428018, spent := 262487, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := false, mask := (some 255), fullRecord := (some ⟨1, true, false⟩), weakRecord := none, contact := (some ⟨1, true, true⟩), application := .failed, diagnosis := .unobserved, proposal := (some true), activation := (some true), phase := .committed}}
def mismatch_conventional_s11 : State := {parent := parent_calibration_break, config := mismatch_conventional_config, body := {account := {fuel := 162339, start := 428018, spent := 265679, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := false, mask := (some 255), fullRecord := (some ⟨1, true, false⟩), weakRecord := (some ⟨1, true, true⟩), contact := none, application := .failed, diagnosis := .unobserved, proposal := (some true), activation := (some true), phase := .committed}}
def mismatch_conventional_s12 : State := {parent := parent_calibration_break, config := mismatch_conventional_config, body := {account := {fuel := 128551, start := 428018, spent := 299467, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := false, mask := (some 204), fullRecord := (some ⟨1, true, false⟩), weakRecord := (some ⟨1, true, true⟩), contact := none, application := .failed, diagnosis := .unobserved, proposal := (some true), activation := (some true), phase := .committed}}
def mismatch_conventional_s13 : State := {parent := parent_calibration_break, config := mismatch_conventional_config, body := {account := {fuel := 125299, start := 428018, spent := 302719, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := false, mask := (some 204), fullRecord := (some ⟨1, true, false⟩), weakRecord := (some ⟨1, true, true⟩), contact := none, application := .failed, diagnosis := .discrepancy, proposal := (some true), activation := (some true), phase := .diagnosisRevised}}
def mismatch_conventional_s14 : State := {parent := parent_calibration_break, config := mismatch_conventional_config, body := {account := {fuel := 64767, start := 428018, spent := 363251, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := true, mask := (some 204), fullRecord := (some ⟨1, true, false⟩), weakRecord := (some ⟨1, true, true⟩), contact := none, application := .failed, diagnosis := .discrepancy, proposal := (some true), activation := (some true), phase := .diagnosisRevised}}
theorem mismatch_conventional_actual_entrance :
  entrance parent_calibration_break mismatch_conventional_config = mismatch_conventional_s0 := by decide

theorem mismatch_conventional_initial_whole_account :
  wholeTotal 8419342 mismatch_conventional_s0 = 145 * RemainingDependency.ticks := by decide

theorem mismatch_conventional_event_1 :
  step mismatch_conventional_s0 .install = mismatch_conventional_s1 ∧ RemainingDependency.tariff mismatch_conventional_s0.body.account 24 58 8 65536 0 = 116338 ∧ (RemainingDependency.charge mismatch_conventional_s0.body.account 24 58 8 65536 0).2 = .none := by decide

theorem mismatch_conventional_event_2 :
  step mismatch_conventional_s1 .fullContact = mismatch_conventional_s2 ∧ RemainingDependency.tariff mismatch_conventional_s1.body.account 0 58 2 16384 0 = 16444 ∧ (RemainingDependency.charge mismatch_conventional_s1.body.account 0 58 2 16384 0).2 = .none := by decide

theorem mismatch_conventional_event_3 :
  step mismatch_conventional_s2 .fullWrite = mismatch_conventional_s3 ∧ RemainingDependency.tariff mismatch_conventional_s2.body.account 1 58 2 0 2 = 3192 ∧ (RemainingDependency.charge mismatch_conventional_s2.body.account 1 58 2 0 2).2 = .none := by decide

theorem mismatch_conventional_event_4 :
  step mismatch_conventional_s3 .filterFull = mismatch_conventional_s4 ∧ RemainingDependency.tariff mismatch_conventional_s3.body.account 16 58 2 0 16 = 33788 ∧ (RemainingDependency.charge mismatch_conventional_s3.body.account 16 58 2 0 16).2 = .none := by decide

theorem mismatch_conventional_event_5 :
  step mismatch_conventional_s4 .reviseApplication = mismatch_conventional_s5 ∧ RemainingDependency.tariff mismatch_conventional_s4.body.account 2 58 2 0 1 = 3252 ∧ (RemainingDependency.charge mismatch_conventional_s4.body.account 2 58 2 0 1).2 = .none := by decide

theorem mismatch_conventional_event_6 :
  step mismatch_conventional_s5 .choose = mismatch_conventional_s6 ∧ RemainingDependency.tariff mismatch_conventional_s5.body.account 32 58 3 0 1 = 35805 ∧ (RemainingDependency.charge mismatch_conventional_s5.body.account 32 58 3 0 1).2 = .none := by decide

theorem mismatch_conventional_event_7 :
  step mismatch_conventional_s6 .commit = mismatch_conventional_s7 ∧ RemainingDependency.tariff mismatch_conventional_s6.body.account 1 58 2 0 1 = 2168 ∧ (RemainingDependency.charge mismatch_conventional_s6.body.account 1 58 2 0 1).2 = .none := by decide

theorem mismatch_conventional_event_8 :
  step mismatch_conventional_s7 (.command true) = mismatch_conventional_s8 ∧ RemainingDependency.tariff mismatch_conventional_s7.body.account 1 58 2 16384 0 = 17528 ∧ (RemainingDependency.charge mismatch_conventional_s7.body.account 1 58 2 16384 0).2 = .none := by decide

theorem mismatch_conventional_event_9 :
  step mismatch_conventional_s8 .challenge = mismatch_conventional_s9 ∧ RemainingDependency.tariff mismatch_conventional_s8.body.account 1 58 2 16384 0 = 17528 ∧ (RemainingDependency.charge mismatch_conventional_s8.body.account 1 58 2 16384 0).2 = .none := by decide

theorem mismatch_conventional_event_10 :
  step mismatch_conventional_s9 .weakContact = mismatch_conventional_s10 ∧ RemainingDependency.tariff mismatch_conventional_s9.body.account 0 58 2 16384 0 = 16444 ∧ (RemainingDependency.charge mismatch_conventional_s9.body.account 0 58 2 16384 0).2 = .none := by decide

theorem mismatch_conventional_event_11 :
  step mismatch_conventional_s10 .weakWrite = mismatch_conventional_s11 ∧ RemainingDependency.tariff mismatch_conventional_s10.body.account 1 58 2 0 2 = 3192 ∧ (RemainingDependency.charge mismatch_conventional_s10.body.account 1 58 2 0 2).2 = .none := by decide

theorem mismatch_conventional_event_12 :
  step mismatch_conventional_s11 .filterWeak = mismatch_conventional_s12 ∧ RemainingDependency.tariff mismatch_conventional_s11.body.account 16 58 2 0 16 = 33788 ∧ (RemainingDependency.charge mismatch_conventional_s11.body.account 16 58 2 0 16).2 = .none := by decide

theorem mismatch_conventional_event_13 :
  step mismatch_conventional_s12 .reviseDiagnosis = mismatch_conventional_s13 ∧ RemainingDependency.tariff mismatch_conventional_s12.body.account 2 58 2 0 1 = 3252 ∧ (RemainingDependency.charge mismatch_conventional_s12.body.account 2 58 2 0 1).2 = .none := by decide

theorem mismatch_conventional_event_14 :
  step mismatch_conventional_s13 .retain = mismatch_conventional_s14 ∧ RemainingDependency.tariff mismatch_conventional_s13.body.account 1 58 0 59392 0 = 60532 ∧ (RemainingDependency.charge mismatch_conventional_s13.body.account 1 58 0 59392 0).2 = .none := by decide

theorem mismatch_conventional_saved_run :
  run mismatch_conventional_s0 [.install, .fullContact, .fullWrite, .filterFull, .reviseApplication, .choose, .commit, (.command true), .challenge, .weakContact, .weakWrite, .filterWeak, .reviseDiagnosis, .retain] = mismatch_conventional_s14 := by decide

theorem mismatch_conventional_core_trace :
  Generative.Trace process mismatch_conventional_s0 [.install, .fullContact, .fullWrite, .filterFull, .reviseApplication, .choose, .commit, (.command true), .challenge, .weakContact, .weakWrite, .filterWeak, .reviseDiagnosis, .retain] mismatch_conventional_s14 := by
  rw [← mismatch_conventional_saved_run]
  exact run_is_core_trace _ _

theorem mismatch_conventional_final_whole_account :
  wholeTotal 8419342 mismatch_conventional_s14 = 145 * RemainingDependency.ticks := by decide

def old_report_error_learned_config : Config := {fullFault := .faithful, weakFault := .faithful, clamp := false}
def old_report_error_learned_s0 : State := {parent := parent_false_dependence, config := old_report_error_learned_config, body := {account := {fuel := 428018, start := 428018, spent := 0, live := 34, peak := 42, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := false, retained := false, mask := none, fullRecord := none, weakRecord := none, contact := none, application := .unobserved, diagnosis := .unobserved, proposal := none, activation := none, phase := .oldInterface}}
def old_report_error_learned_s1 : State := {parent := parent_false_dependence, config := old_report_error_learned_config, body := {account := {fuel := 311680, start := 428018, spent := 116338, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := false, mask := (some 65535), fullRecord := none, weakRecord := none, contact := none, application := .unobserved, diagnosis := .unobserved, proposal := none, activation := none, phase := .formed}}
def old_report_error_learned_s2 : State := {parent := parent_false_dependence, config := old_report_error_learned_config, body := {account := {fuel := 295236, start := 428018, spent := 132782, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := false, mask := (some 65535), fullRecord := none, weakRecord := none, contact := (some ⟨1, true, false⟩), application := .unobserved, diagnosis := .unobserved, proposal := none, activation := none, phase := .formed}}
def old_report_error_learned_s3 : State := {parent := parent_false_dependence, config := old_report_error_learned_config, body := {account := {fuel := 292044, start := 428018, spent := 135974, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := false, mask := (some 65535), fullRecord := (some ⟨1, true, false⟩), weakRecord := none, contact := none, application := .unobserved, diagnosis := .unobserved, proposal := none, activation := none, phase := .formed}}
def old_report_error_learned_s4 : State := {parent := parent_false_dependence, config := old_report_error_learned_config, body := {account := {fuel := 258256, start := 428018, spent := 169762, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := false, mask := (some 255), fullRecord := (some ⟨1, true, false⟩), weakRecord := none, contact := none, application := .unobserved, diagnosis := .unobserved, proposal := none, activation := none, phase := .formed}}
def old_report_error_learned_s5 : State := {parent := parent_false_dependence, config := old_report_error_learned_config, body := {account := {fuel := 255004, start := 428018, spent := 173014, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := false, mask := (some 255), fullRecord := (some ⟨1, true, false⟩), weakRecord := none, contact := none, application := .failed, diagnosis := .unobserved, proposal := none, activation := none, phase := .applicationRevised}}
def old_report_error_learned_s6 : State := {parent := parent_false_dependence, config := old_report_error_learned_config, body := {account := {fuel := 219199, start := 428018, spent := 208819, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := false, mask := (some 255), fullRecord := (some ⟨1, true, false⟩), weakRecord := none, contact := none, application := .failed, diagnosis := .unobserved, proposal := (some true), activation := none, phase := .applicationRevised}}
def old_report_error_learned_s7 : State := {parent := parent_false_dependence, config := old_report_error_learned_config, body := {account := {fuel := 217031, start := 428018, spent := 210987, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := false, mask := (some 255), fullRecord := (some ⟨1, true, false⟩), weakRecord := none, contact := none, application := .failed, diagnosis := .unobserved, proposal := (some true), activation := (some true), phase := .committed}}
def old_report_error_learned_s8 : State := {parent := parent_false_dependence, config := old_report_error_learned_config, body := {account := {fuel := 199503, start := 428018, spent := 228515, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := false, mask := (some 255), fullRecord := (some ⟨1, true, false⟩), weakRecord := none, contact := none, application := .failed, diagnosis := .unobserved, proposal := (some true), activation := (some true), phase := .committed}}
def old_report_error_learned_s9 : State := {parent := parent_false_dependence, config := old_report_error_learned_config, body := {account := {fuel := 181975, start := 428018, spent := 246043, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := (some ⟨1, true, false⟩), held := false, installed := true, retained := false, mask := (some 255), fullRecord := (some ⟨1, true, false⟩), weakRecord := none, contact := none, application := .failed, diagnosis := .unobserved, proposal := (some true), activation := (some true), phase := .committed}}
def old_report_error_learned_s10 : State := {parent := parent_false_dependence, config := old_report_error_learned_config, body := {account := {fuel := 165531, start := 428018, spent := 262487, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := false, mask := (some 255), fullRecord := (some ⟨1, true, false⟩), weakRecord := none, contact := (some ⟨1, true, false⟩), application := .failed, diagnosis := .unobserved, proposal := (some true), activation := (some true), phase := .committed}}
def old_report_error_learned_s11 : State := {parent := parent_false_dependence, config := old_report_error_learned_config, body := {account := {fuel := 162339, start := 428018, spent := 265679, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := false, mask := (some 255), fullRecord := (some ⟨1, true, false⟩), weakRecord := (some ⟨1, true, false⟩), contact := none, application := .failed, diagnosis := .unobserved, proposal := (some true), activation := (some true), phase := .committed}}
def old_report_error_learned_s12 : State := {parent := parent_false_dependence, config := old_report_error_learned_config, body := {account := {fuel := 128551, start := 428018, spent := 299467, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := false, mask := (some 51), fullRecord := (some ⟨1, true, false⟩), weakRecord := (some ⟨1, true, false⟩), contact := none, application := .failed, diagnosis := .unobserved, proposal := (some true), activation := (some true), phase := .committed}}
def old_report_error_learned_s13 : State := {parent := parent_false_dependence, config := old_report_error_learned_config, body := {account := {fuel := 125299, start := 428018, spent := 302719, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := false, mask := (some 51), fullRecord := (some ⟨1, true, false⟩), weakRecord := (some ⟨1, true, false⟩), contact := none, application := .failed, diagnosis := .oldContradicted, proposal := (some true), activation := (some true), phase := .diagnosisRevised}}
def old_report_error_learned_s14 : State := {parent := parent_false_dependence, config := old_report_error_learned_config, body := {account := {fuel := 64767, start := 428018, spent := 363251, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := true, mask := (some 51), fullRecord := (some ⟨1, true, false⟩), weakRecord := (some ⟨1, true, false⟩), contact := none, application := .failed, diagnosis := .oldContradicted, proposal := (some true), activation := (some true), phase := .diagnosisRevised}}
theorem old_report_error_learned_actual_entrance :
  entrance parent_false_dependence old_report_error_learned_config = old_report_error_learned_s0 := by decide

theorem old_report_error_learned_initial_whole_account :
  wholeTotal 8419342 old_report_error_learned_s0 = 145 * RemainingDependency.ticks := by decide

theorem old_report_error_learned_event_1 :
  step old_report_error_learned_s0 .install = old_report_error_learned_s1 ∧ RemainingDependency.tariff old_report_error_learned_s0.body.account 24 58 8 65536 0 = 116338 ∧ (RemainingDependency.charge old_report_error_learned_s0.body.account 24 58 8 65536 0).2 = .none := by decide

theorem old_report_error_learned_event_2 :
  step old_report_error_learned_s1 .fullContact = old_report_error_learned_s2 ∧ RemainingDependency.tariff old_report_error_learned_s1.body.account 0 58 2 16384 0 = 16444 ∧ (RemainingDependency.charge old_report_error_learned_s1.body.account 0 58 2 16384 0).2 = .none := by decide

theorem old_report_error_learned_event_3 :
  step old_report_error_learned_s2 .fullWrite = old_report_error_learned_s3 ∧ RemainingDependency.tariff old_report_error_learned_s2.body.account 1 58 2 0 2 = 3192 ∧ (RemainingDependency.charge old_report_error_learned_s2.body.account 1 58 2 0 2).2 = .none := by decide

theorem old_report_error_learned_event_4 :
  step old_report_error_learned_s3 .filterFull = old_report_error_learned_s4 ∧ RemainingDependency.tariff old_report_error_learned_s3.body.account 16 58 2 0 16 = 33788 ∧ (RemainingDependency.charge old_report_error_learned_s3.body.account 16 58 2 0 16).2 = .none := by decide

theorem old_report_error_learned_event_5 :
  step old_report_error_learned_s4 .reviseApplication = old_report_error_learned_s5 ∧ RemainingDependency.tariff old_report_error_learned_s4.body.account 2 58 2 0 1 = 3252 ∧ (RemainingDependency.charge old_report_error_learned_s4.body.account 2 58 2 0 1).2 = .none := by decide

theorem old_report_error_learned_event_6 :
  step old_report_error_learned_s5 .choose = old_report_error_learned_s6 ∧ RemainingDependency.tariff old_report_error_learned_s5.body.account 32 58 3 0 1 = 35805 ∧ (RemainingDependency.charge old_report_error_learned_s5.body.account 32 58 3 0 1).2 = .none := by decide

theorem old_report_error_learned_event_7 :
  step old_report_error_learned_s6 .commit = old_report_error_learned_s7 ∧ RemainingDependency.tariff old_report_error_learned_s6.body.account 1 58 2 0 1 = 2168 ∧ (RemainingDependency.charge old_report_error_learned_s6.body.account 1 58 2 0 1).2 = .none := by decide

theorem old_report_error_learned_event_8 :
  step old_report_error_learned_s7 (.command true) = old_report_error_learned_s8 ∧ RemainingDependency.tariff old_report_error_learned_s7.body.account 1 58 2 16384 0 = 17528 ∧ (RemainingDependency.charge old_report_error_learned_s7.body.account 1 58 2 16384 0).2 = .none := by decide

theorem old_report_error_learned_event_9 :
  step old_report_error_learned_s8 .challenge = old_report_error_learned_s9 ∧ RemainingDependency.tariff old_report_error_learned_s8.body.account 1 58 2 16384 0 = 17528 ∧ (RemainingDependency.charge old_report_error_learned_s8.body.account 1 58 2 16384 0).2 = .none := by decide

theorem old_report_error_learned_event_10 :
  step old_report_error_learned_s9 .weakContact = old_report_error_learned_s10 ∧ RemainingDependency.tariff old_report_error_learned_s9.body.account 0 58 2 16384 0 = 16444 ∧ (RemainingDependency.charge old_report_error_learned_s9.body.account 0 58 2 16384 0).2 = .none := by decide

theorem old_report_error_learned_event_11 :
  step old_report_error_learned_s10 .weakWrite = old_report_error_learned_s11 ∧ RemainingDependency.tariff old_report_error_learned_s10.body.account 1 58 2 0 2 = 3192 ∧ (RemainingDependency.charge old_report_error_learned_s10.body.account 1 58 2 0 2).2 = .none := by decide

theorem old_report_error_learned_event_12 :
  step old_report_error_learned_s11 .filterWeak = old_report_error_learned_s12 ∧ RemainingDependency.tariff old_report_error_learned_s11.body.account 16 58 2 0 16 = 33788 ∧ (RemainingDependency.charge old_report_error_learned_s11.body.account 16 58 2 0 16).2 = .none := by decide

theorem old_report_error_learned_event_13 :
  step old_report_error_learned_s12 .reviseDiagnosis = old_report_error_learned_s13 ∧ RemainingDependency.tariff old_report_error_learned_s12.body.account 2 58 2 0 1 = 3252 ∧ (RemainingDependency.charge old_report_error_learned_s12.body.account 2 58 2 0 1).2 = .none := by decide

theorem old_report_error_learned_event_14 :
  step old_report_error_learned_s13 .retain = old_report_error_learned_s14 ∧ RemainingDependency.tariff old_report_error_learned_s13.body.account 1 58 0 59392 0 = 60532 ∧ (RemainingDependency.charge old_report_error_learned_s13.body.account 1 58 0 59392 0).2 = .none := by decide

theorem old_report_error_learned_saved_run :
  run old_report_error_learned_s0 [.install, .fullContact, .fullWrite, .filterFull, .reviseApplication, .choose, .commit, (.command true), .challenge, .weakContact, .weakWrite, .filterWeak, .reviseDiagnosis, .retain] = old_report_error_learned_s14 := by decide

theorem old_report_error_learned_core_trace :
  Generative.Trace process old_report_error_learned_s0 [.install, .fullContact, .fullWrite, .filterFull, .reviseApplication, .choose, .commit, (.command true), .challenge, .weakContact, .weakWrite, .filterWeak, .reviseDiagnosis, .retain] old_report_error_learned_s14 := by
  rw [← old_report_error_learned_saved_run]
  exact run_is_core_trace _ _

theorem old_report_error_learned_final_whole_account :
  wholeTotal 8419342 old_report_error_learned_s14 = 145 * RemainingDependency.ticks := by decide

def old_report_error_clamped_config : Config := {fullFault := .faithful, weakFault := .faithful, clamp := true}
def old_report_error_clamped_s0 : State := {parent := parent_false_dependence, config := old_report_error_clamped_config, body := {account := {fuel := 428018, start := 428018, spent := 0, live := 34, peak := 42, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := false, retained := false, mask := none, fullRecord := none, weakRecord := none, contact := none, application := .unobserved, diagnosis := .unobserved, proposal := none, activation := none, phase := .oldInterface}}
def old_report_error_clamped_s1 : State := {parent := parent_false_dependence, config := old_report_error_clamped_config, body := {account := {fuel := 311680, start := 428018, spent := 116338, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := false, mask := (some 65535), fullRecord := none, weakRecord := none, contact := none, application := .unobserved, diagnosis := .unobserved, proposal := none, activation := none, phase := .formed}}
def old_report_error_clamped_s2 : State := {parent := parent_false_dependence, config := old_report_error_clamped_config, body := {account := {fuel := 295236, start := 428018, spent := 132782, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := false, mask := (some 65535), fullRecord := none, weakRecord := none, contact := (some ⟨1, true, false⟩), application := .unobserved, diagnosis := .unobserved, proposal := none, activation := none, phase := .formed}}
def old_report_error_clamped_s3 : State := {parent := parent_false_dependence, config := old_report_error_clamped_config, body := {account := {fuel := 292044, start := 428018, spent := 135974, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := false, mask := (some 65535), fullRecord := (some ⟨1, true, false⟩), weakRecord := none, contact := none, application := .unobserved, diagnosis := .unobserved, proposal := none, activation := none, phase := .formed}}
def old_report_error_clamped_s4 : State := {parent := parent_false_dependence, config := old_report_error_clamped_config, body := {account := {fuel := 258256, start := 428018, spent := 169762, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := false, mask := (some 255), fullRecord := (some ⟨1, true, false⟩), weakRecord := none, contact := none, application := .unobserved, diagnosis := .unobserved, proposal := none, activation := none, phase := .formed}}
def old_report_error_clamped_s5 : State := {parent := parent_false_dependence, config := old_report_error_clamped_config, body := {account := {fuel := 255004, start := 428018, spent := 173014, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := false, mask := (some 255), fullRecord := (some ⟨1, true, false⟩), weakRecord := none, contact := none, application := .failed, diagnosis := .unobserved, proposal := none, activation := none, phase := .applicationRevised}}
def old_report_error_clamped_s6 : State := {parent := parent_false_dependence, config := old_report_error_clamped_config, body := {account := {fuel := 219199, start := 428018, spent := 208819, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := false, mask := (some 255), fullRecord := (some ⟨1, true, false⟩), weakRecord := none, contact := none, application := .failed, diagnosis := .unobserved, proposal := (some true), activation := none, phase := .applicationRevised}}
def old_report_error_clamped_s7 : State := {parent := parent_false_dependence, config := old_report_error_clamped_config, body := {account := {fuel := 217031, start := 428018, spent := 210987, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := false, mask := (some 255), fullRecord := (some ⟨1, true, false⟩), weakRecord := none, contact := none, application := .failed, diagnosis := .unobserved, proposal := (some true), activation := none, phase := .committed}}
def old_report_error_clamped_s8 : State := {parent := parent_false_dependence, config := old_report_error_clamped_config, body := {account := {fuel := 156499, start := 428018, spent := 271519, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := true, mask := (some 255), fullRecord := (some ⟨1, true, false⟩), weakRecord := none, contact := none, application := .failed, diagnosis := .unobserved, proposal := (some true), activation := none, phase := .committed}}
theorem old_report_error_clamped_actual_entrance :
  entrance parent_false_dependence old_report_error_clamped_config = old_report_error_clamped_s0 := by decide

theorem old_report_error_clamped_initial_whole_account :
  wholeTotal 8419342 old_report_error_clamped_s0 = 145 * RemainingDependency.ticks := by decide

theorem old_report_error_clamped_event_1 :
  step old_report_error_clamped_s0 .install = old_report_error_clamped_s1 ∧ RemainingDependency.tariff old_report_error_clamped_s0.body.account 24 58 8 65536 0 = 116338 ∧ (RemainingDependency.charge old_report_error_clamped_s0.body.account 24 58 8 65536 0).2 = .none := by decide

theorem old_report_error_clamped_event_2 :
  step old_report_error_clamped_s1 .fullContact = old_report_error_clamped_s2 ∧ RemainingDependency.tariff old_report_error_clamped_s1.body.account 0 58 2 16384 0 = 16444 ∧ (RemainingDependency.charge old_report_error_clamped_s1.body.account 0 58 2 16384 0).2 = .none := by decide

theorem old_report_error_clamped_event_3 :
  step old_report_error_clamped_s2 .fullWrite = old_report_error_clamped_s3 ∧ RemainingDependency.tariff old_report_error_clamped_s2.body.account 1 58 2 0 2 = 3192 ∧ (RemainingDependency.charge old_report_error_clamped_s2.body.account 1 58 2 0 2).2 = .none := by decide

theorem old_report_error_clamped_event_4 :
  step old_report_error_clamped_s3 .filterFull = old_report_error_clamped_s4 ∧ RemainingDependency.tariff old_report_error_clamped_s3.body.account 16 58 2 0 16 = 33788 ∧ (RemainingDependency.charge old_report_error_clamped_s3.body.account 16 58 2 0 16).2 = .none := by decide

theorem old_report_error_clamped_event_5 :
  step old_report_error_clamped_s4 .reviseApplication = old_report_error_clamped_s5 ∧ RemainingDependency.tariff old_report_error_clamped_s4.body.account 2 58 2 0 1 = 3252 ∧ (RemainingDependency.charge old_report_error_clamped_s4.body.account 2 58 2 0 1).2 = .none := by decide

theorem old_report_error_clamped_event_6 :
  step old_report_error_clamped_s5 .choose = old_report_error_clamped_s6 ∧ RemainingDependency.tariff old_report_error_clamped_s5.body.account 32 58 3 0 1 = 35805 ∧ (RemainingDependency.charge old_report_error_clamped_s5.body.account 32 58 3 0 1).2 = .none := by decide

theorem old_report_error_clamped_event_7 :
  step old_report_error_clamped_s6 .commit = old_report_error_clamped_s7 ∧ RemainingDependency.tariff old_report_error_clamped_s6.body.account 1 58 2 0 1 = 2168 ∧ (RemainingDependency.charge old_report_error_clamped_s6.body.account 1 58 2 0 1).2 = .none := by decide

theorem old_report_error_clamped_event_8 :
  step old_report_error_clamped_s7 .retain = old_report_error_clamped_s8 ∧ RemainingDependency.tariff old_report_error_clamped_s7.body.account 1 58 0 59392 0 = 60532 ∧ (RemainingDependency.charge old_report_error_clamped_s7.body.account 1 58 0 59392 0).2 = .none := by decide

theorem old_report_error_clamped_saved_run :
  run old_report_error_clamped_s0 [.install, .fullContact, .fullWrite, .filterFull, .reviseApplication, .choose, .commit, .retain] = old_report_error_clamped_s8 := by decide

theorem old_report_error_clamped_core_trace :
  Generative.Trace process old_report_error_clamped_s0 [.install, .fullContact, .fullWrite, .filterFull, .reviseApplication, .choose, .commit, .retain] old_report_error_clamped_s8 := by
  rw [← old_report_error_clamped_saved_run]
  exact run_is_core_trace _ _

theorem old_report_error_clamped_final_whole_account :
  wholeTotal 8419342 old_report_error_clamped_s8 = 145 * RemainingDependency.ticks := by decide

def old_report_error_conventional_config : Config := {fullFault := .faithful, weakFault := .faithful, clamp := false}
def old_report_error_conventional_s0 : State := {parent := parent_false_dependence, config := old_report_error_conventional_config, body := {account := {fuel := 428018, start := 428018, spent := 0, live := 34, peak := 42, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := false, retained := false, mask := none, fullRecord := none, weakRecord := none, contact := none, application := .unobserved, diagnosis := .unobserved, proposal := none, activation := none, phase := .oldInterface}}
def old_report_error_conventional_s1 : State := {parent := parent_false_dependence, config := old_report_error_conventional_config, body := {account := {fuel := 311680, start := 428018, spent := 116338, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := false, mask := (some 65535), fullRecord := none, weakRecord := none, contact := none, application := .unobserved, diagnosis := .unobserved, proposal := none, activation := none, phase := .formed}}
def old_report_error_conventional_s2 : State := {parent := parent_false_dependence, config := old_report_error_conventional_config, body := {account := {fuel := 295236, start := 428018, spent := 132782, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := false, mask := (some 65535), fullRecord := none, weakRecord := none, contact := (some ⟨1, true, false⟩), application := .unobserved, diagnosis := .unobserved, proposal := none, activation := none, phase := .formed}}
def old_report_error_conventional_s3 : State := {parent := parent_false_dependence, config := old_report_error_conventional_config, body := {account := {fuel := 292044, start := 428018, spent := 135974, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := false, mask := (some 65535), fullRecord := (some ⟨1, true, false⟩), weakRecord := none, contact := none, application := .unobserved, diagnosis := .unobserved, proposal := none, activation := none, phase := .formed}}
def old_report_error_conventional_s4 : State := {parent := parent_false_dependence, config := old_report_error_conventional_config, body := {account := {fuel := 258256, start := 428018, spent := 169762, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := false, mask := (some 255), fullRecord := (some ⟨1, true, false⟩), weakRecord := none, contact := none, application := .unobserved, diagnosis := .unobserved, proposal := none, activation := none, phase := .formed}}
def old_report_error_conventional_s5 : State := {parent := parent_false_dependence, config := old_report_error_conventional_config, body := {account := {fuel := 255004, start := 428018, spent := 173014, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := false, mask := (some 255), fullRecord := (some ⟨1, true, false⟩), weakRecord := none, contact := none, application := .failed, diagnosis := .unobserved, proposal := none, activation := none, phase := .applicationRevised}}
def old_report_error_conventional_s6 : State := {parent := parent_false_dependence, config := old_report_error_conventional_config, body := {account := {fuel := 219199, start := 428018, spent := 208819, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := false, mask := (some 255), fullRecord := (some ⟨1, true, false⟩), weakRecord := none, contact := none, application := .failed, diagnosis := .unobserved, proposal := (some true), activation := none, phase := .applicationRevised}}
def old_report_error_conventional_s7 : State := {parent := parent_false_dependence, config := old_report_error_conventional_config, body := {account := {fuel := 217031, start := 428018, spent := 210987, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := false, mask := (some 255), fullRecord := (some ⟨1, true, false⟩), weakRecord := none, contact := none, application := .failed, diagnosis := .unobserved, proposal := (some true), activation := (some true), phase := .committed}}
def old_report_error_conventional_s8 : State := {parent := parent_false_dependence, config := old_report_error_conventional_config, body := {account := {fuel := 199503, start := 428018, spent := 228515, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := false, mask := (some 255), fullRecord := (some ⟨1, true, false⟩), weakRecord := none, contact := none, application := .failed, diagnosis := .unobserved, proposal := (some true), activation := (some true), phase := .committed}}
def old_report_error_conventional_s9 : State := {parent := parent_false_dependence, config := old_report_error_conventional_config, body := {account := {fuel := 181975, start := 428018, spent := 246043, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := (some ⟨1, true, false⟩), held := false, installed := true, retained := false, mask := (some 255), fullRecord := (some ⟨1, true, false⟩), weakRecord := none, contact := none, application := .failed, diagnosis := .unobserved, proposal := (some true), activation := (some true), phase := .committed}}
def old_report_error_conventional_s10 : State := {parent := parent_false_dependence, config := old_report_error_conventional_config, body := {account := {fuel := 165531, start := 428018, spent := 262487, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := false, mask := (some 255), fullRecord := (some ⟨1, true, false⟩), weakRecord := none, contact := (some ⟨1, true, false⟩), application := .failed, diagnosis := .unobserved, proposal := (some true), activation := (some true), phase := .committed}}
def old_report_error_conventional_s11 : State := {parent := parent_false_dependence, config := old_report_error_conventional_config, body := {account := {fuel := 162339, start := 428018, spent := 265679, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := false, mask := (some 255), fullRecord := (some ⟨1, true, false⟩), weakRecord := (some ⟨1, true, false⟩), contact := none, application := .failed, diagnosis := .unobserved, proposal := (some true), activation := (some true), phase := .committed}}
def old_report_error_conventional_s12 : State := {parent := parent_false_dependence, config := old_report_error_conventional_config, body := {account := {fuel := 128551, start := 428018, spent := 299467, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := false, mask := (some 51), fullRecord := (some ⟨1, true, false⟩), weakRecord := (some ⟨1, true, false⟩), contact := none, application := .failed, diagnosis := .unobserved, proposal := (some true), activation := (some true), phase := .committed}}
def old_report_error_conventional_s13 : State := {parent := parent_false_dependence, config := old_report_error_conventional_config, body := {account := {fuel := 125299, start := 428018, spent := 302719, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := false, mask := (some 51), fullRecord := (some ⟨1, true, false⟩), weakRecord := (some ⟨1, true, false⟩), contact := none, application := .failed, diagnosis := .oldContradicted, proposal := (some true), activation := (some true), phase := .diagnosisRevised}}
def old_report_error_conventional_s14 : State := {parent := parent_false_dependence, config := old_report_error_conventional_config, body := {account := {fuel := 64767, start := 428018, spent := 363251, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := true, mask := (some 51), fullRecord := (some ⟨1, true, false⟩), weakRecord := (some ⟨1, true, false⟩), contact := none, application := .failed, diagnosis := .oldContradicted, proposal := (some true), activation := (some true), phase := .diagnosisRevised}}
theorem old_report_error_conventional_actual_entrance :
  entrance parent_false_dependence old_report_error_conventional_config = old_report_error_conventional_s0 := by decide

theorem old_report_error_conventional_initial_whole_account :
  wholeTotal 8419342 old_report_error_conventional_s0 = 145 * RemainingDependency.ticks := by decide

theorem old_report_error_conventional_event_1 :
  step old_report_error_conventional_s0 .install = old_report_error_conventional_s1 ∧ RemainingDependency.tariff old_report_error_conventional_s0.body.account 24 58 8 65536 0 = 116338 ∧ (RemainingDependency.charge old_report_error_conventional_s0.body.account 24 58 8 65536 0).2 = .none := by decide

theorem old_report_error_conventional_event_2 :
  step old_report_error_conventional_s1 .fullContact = old_report_error_conventional_s2 ∧ RemainingDependency.tariff old_report_error_conventional_s1.body.account 0 58 2 16384 0 = 16444 ∧ (RemainingDependency.charge old_report_error_conventional_s1.body.account 0 58 2 16384 0).2 = .none := by decide

theorem old_report_error_conventional_event_3 :
  step old_report_error_conventional_s2 .fullWrite = old_report_error_conventional_s3 ∧ RemainingDependency.tariff old_report_error_conventional_s2.body.account 1 58 2 0 2 = 3192 ∧ (RemainingDependency.charge old_report_error_conventional_s2.body.account 1 58 2 0 2).2 = .none := by decide

theorem old_report_error_conventional_event_4 :
  step old_report_error_conventional_s3 .filterFull = old_report_error_conventional_s4 ∧ RemainingDependency.tariff old_report_error_conventional_s3.body.account 16 58 2 0 16 = 33788 ∧ (RemainingDependency.charge old_report_error_conventional_s3.body.account 16 58 2 0 16).2 = .none := by decide

theorem old_report_error_conventional_event_5 :
  step old_report_error_conventional_s4 .reviseApplication = old_report_error_conventional_s5 ∧ RemainingDependency.tariff old_report_error_conventional_s4.body.account 2 58 2 0 1 = 3252 ∧ (RemainingDependency.charge old_report_error_conventional_s4.body.account 2 58 2 0 1).2 = .none := by decide

theorem old_report_error_conventional_event_6 :
  step old_report_error_conventional_s5 .choose = old_report_error_conventional_s6 ∧ RemainingDependency.tariff old_report_error_conventional_s5.body.account 32 58 3 0 1 = 35805 ∧ (RemainingDependency.charge old_report_error_conventional_s5.body.account 32 58 3 0 1).2 = .none := by decide

theorem old_report_error_conventional_event_7 :
  step old_report_error_conventional_s6 .commit = old_report_error_conventional_s7 ∧ RemainingDependency.tariff old_report_error_conventional_s6.body.account 1 58 2 0 1 = 2168 ∧ (RemainingDependency.charge old_report_error_conventional_s6.body.account 1 58 2 0 1).2 = .none := by decide

theorem old_report_error_conventional_event_8 :
  step old_report_error_conventional_s7 (.command true) = old_report_error_conventional_s8 ∧ RemainingDependency.tariff old_report_error_conventional_s7.body.account 1 58 2 16384 0 = 17528 ∧ (RemainingDependency.charge old_report_error_conventional_s7.body.account 1 58 2 16384 0).2 = .none := by decide

theorem old_report_error_conventional_event_9 :
  step old_report_error_conventional_s8 .challenge = old_report_error_conventional_s9 ∧ RemainingDependency.tariff old_report_error_conventional_s8.body.account 1 58 2 16384 0 = 17528 ∧ (RemainingDependency.charge old_report_error_conventional_s8.body.account 1 58 2 16384 0).2 = .none := by decide

theorem old_report_error_conventional_event_10 :
  step old_report_error_conventional_s9 .weakContact = old_report_error_conventional_s10 ∧ RemainingDependency.tariff old_report_error_conventional_s9.body.account 0 58 2 16384 0 = 16444 ∧ (RemainingDependency.charge old_report_error_conventional_s9.body.account 0 58 2 16384 0).2 = .none := by decide

theorem old_report_error_conventional_event_11 :
  step old_report_error_conventional_s10 .weakWrite = old_report_error_conventional_s11 ∧ RemainingDependency.tariff old_report_error_conventional_s10.body.account 1 58 2 0 2 = 3192 ∧ (RemainingDependency.charge old_report_error_conventional_s10.body.account 1 58 2 0 2).2 = .none := by decide

theorem old_report_error_conventional_event_12 :
  step old_report_error_conventional_s11 .filterWeak = old_report_error_conventional_s12 ∧ RemainingDependency.tariff old_report_error_conventional_s11.body.account 16 58 2 0 16 = 33788 ∧ (RemainingDependency.charge old_report_error_conventional_s11.body.account 16 58 2 0 16).2 = .none := by decide

theorem old_report_error_conventional_event_13 :
  step old_report_error_conventional_s12 .reviseDiagnosis = old_report_error_conventional_s13 ∧ RemainingDependency.tariff old_report_error_conventional_s12.body.account 2 58 2 0 1 = 3252 ∧ (RemainingDependency.charge old_report_error_conventional_s12.body.account 2 58 2 0 1).2 = .none := by decide

theorem old_report_error_conventional_event_14 :
  step old_report_error_conventional_s13 .retain = old_report_error_conventional_s14 ∧ RemainingDependency.tariff old_report_error_conventional_s13.body.account 1 58 0 59392 0 = 60532 ∧ (RemainingDependency.charge old_report_error_conventional_s13.body.account 1 58 0 59392 0).2 = .none := by decide

theorem old_report_error_conventional_saved_run :
  run old_report_error_conventional_s0 [.install, .fullContact, .fullWrite, .filterFull, .reviseApplication, .choose, .commit, (.command true), .challenge, .weakContact, .weakWrite, .filterWeak, .reviseDiagnosis, .retain] = old_report_error_conventional_s14 := by decide

theorem old_report_error_conventional_core_trace :
  Generative.Trace process old_report_error_conventional_s0 [.install, .fullContact, .fullWrite, .filterFull, .reviseApplication, .choose, .commit, (.command true), .challenge, .weakContact, .weakWrite, .filterWeak, .reviseDiagnosis, .retain] old_report_error_conventional_s14 := by
  rw [← old_report_error_conventional_saved_run]
  exact run_is_core_trace _ _

theorem old_report_error_conventional_final_whole_account :
  wholeTotal 8419342 old_report_error_conventional_s14 = 145 * RemainingDependency.ticks := by decide

def positive_bypass_config : Config := {fullFault := .faithful, weakFault := .faithful, clamp := false}
def positive_bypass_s0 : State := {parent := parent_law_10_learned, config := positive_bypass_config, body := {account := {fuel := 444402, start := 444402, spent := 0, live := 34, peak := 42, capacity := 256}, stocks := ⟨0, 10, 0⟩, context := 1, relay := false, pending := none, held := false, installed := false, retained := false, mask := none, fullRecord := none, weakRecord := none, contact := none, application := .unobserved, diagnosis := .unobserved, proposal := none, activation := none, phase := .oldInterface}}
def positive_bypass_s1 : State := {parent := parent_law_10_learned, config := positive_bypass_config, body := {account := {fuel := 328064, start := 444402, spent := 116338, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 10, 0⟩, context := 1, relay := false, pending := none, held := false, installed := true, retained := false, mask := (some 65535), fullRecord := none, weakRecord := none, contact := none, application := .unobserved, diagnosis := .unobserved, proposal := none, activation := none, phase := .formed}}
def positive_bypass_s2 : State := {parent := parent_law_10_learned, config := positive_bypass_config, body := {account := {fuel := 311620, start := 444402, spent := 132782, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 10, 0⟩, context := 1, relay := false, pending := none, held := false, installed := true, retained := false, mask := (some 65535), fullRecord := none, weakRecord := none, contact := (some ⟨1, false, true⟩), application := .unobserved, diagnosis := .unobserved, proposal := none, activation := none, phase := .formed}}
def positive_bypass_s3 : State := {parent := parent_law_10_learned, config := positive_bypass_config, body := {account := {fuel := 308428, start := 444402, spent := 135974, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 10, 0⟩, context := 1, relay := false, pending := none, held := false, installed := true, retained := false, mask := (some 65535), fullRecord := (some ⟨1, false, true⟩), weakRecord := none, contact := none, application := .unobserved, diagnosis := .unobserved, proposal := none, activation := none, phase := .formed}}
def positive_bypass_s4 : State := {parent := parent_law_10_learned, config := positive_bypass_config, body := {account := {fuel := 274640, start := 444402, spent := 169762, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 10, 0⟩, context := 1, relay := false, pending := none, held := false, installed := true, retained := false, mask := (some 61680), fullRecord := (some ⟨1, false, true⟩), weakRecord := none, contact := none, application := .unobserved, diagnosis := .unobserved, proposal := none, activation := none, phase := .formed}}
def positive_bypass_s5 : State := {parent := parent_law_10_learned, config := positive_bypass_config, body := {account := {fuel := 271388, start := 444402, spent := 173014, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 10, 0⟩, context := 1, relay := false, pending := none, held := false, installed := true, retained := false, mask := (some 61680), fullRecord := (some ⟨1, false, true⟩), weakRecord := none, contact := none, application := .supported, diagnosis := .unobserved, proposal := none, activation := none, phase := .applicationRevised}}
def positive_bypass_s6 : State := {parent := parent_law_10_learned, config := positive_bypass_config, body := {account := {fuel := 235583, start := 444402, spent := 208819, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 10, 0⟩, context := 1, relay := false, pending := none, held := false, installed := true, retained := false, mask := (some 61680), fullRecord := (some ⟨1, false, true⟩), weakRecord := none, contact := none, application := .supported, diagnosis := .unobserved, proposal := none, activation := none, phase := .applicationRevised}}
def positive_bypass_s7 : State := {parent := parent_law_10_learned, config := positive_bypass_config, body := {account := {fuel := 233415, start := 444402, spent := 210987, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 10, 0⟩, context := 1, relay := false, pending := none, held := false, installed := true, retained := false, mask := (some 61680), fullRecord := (some ⟨1, false, true⟩), weakRecord := none, contact := none, application := .supported, diagnosis := .unobserved, proposal := none, activation := none, phase := .committed}}
def positive_bypass_s8 : State := {parent := parent_law_10_learned, config := positive_bypass_config, body := {account := {fuel := 172883, start := 444402, spent := 271519, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 10, 0⟩, context := 1, relay := false, pending := none, held := false, installed := true, retained := true, mask := (some 61680), fullRecord := (some ⟨1, false, true⟩), weakRecord := none, contact := none, application := .supported, diagnosis := .unobserved, proposal := none, activation := none, phase := .committed}}
theorem positive_bypass_actual_entrance :
  entrance parent_law_10_learned positive_bypass_config = positive_bypass_s0 := by decide

theorem positive_bypass_initial_whole_account :
  wholeTotal 8402958 positive_bypass_s0 = 145 * RemainingDependency.ticks := by decide

theorem positive_bypass_event_1 :
  step positive_bypass_s0 .install = positive_bypass_s1 ∧ RemainingDependency.tariff positive_bypass_s0.body.account 24 58 8 65536 0 = 116338 ∧ (RemainingDependency.charge positive_bypass_s0.body.account 24 58 8 65536 0).2 = .none := by decide

theorem positive_bypass_event_2 :
  step positive_bypass_s1 .fullContact = positive_bypass_s2 ∧ RemainingDependency.tariff positive_bypass_s1.body.account 0 58 2 16384 0 = 16444 ∧ (RemainingDependency.charge positive_bypass_s1.body.account 0 58 2 16384 0).2 = .none := by decide

theorem positive_bypass_event_3 :
  step positive_bypass_s2 .fullWrite = positive_bypass_s3 ∧ RemainingDependency.tariff positive_bypass_s2.body.account 1 58 2 0 2 = 3192 ∧ (RemainingDependency.charge positive_bypass_s2.body.account 1 58 2 0 2).2 = .none := by decide

theorem positive_bypass_event_4 :
  step positive_bypass_s3 .filterFull = positive_bypass_s4 ∧ RemainingDependency.tariff positive_bypass_s3.body.account 16 58 2 0 16 = 33788 ∧ (RemainingDependency.charge positive_bypass_s3.body.account 16 58 2 0 16).2 = .none := by decide

theorem positive_bypass_event_5 :
  step positive_bypass_s4 .reviseApplication = positive_bypass_s5 ∧ RemainingDependency.tariff positive_bypass_s4.body.account 2 58 2 0 1 = 3252 ∧ (RemainingDependency.charge positive_bypass_s4.body.account 2 58 2 0 1).2 = .none := by decide

theorem positive_bypass_event_6 :
  step positive_bypass_s5 .choose = positive_bypass_s6 ∧ RemainingDependency.tariff positive_bypass_s5.body.account 32 58 3 0 1 = 35805 ∧ (RemainingDependency.charge positive_bypass_s5.body.account 32 58 3 0 1).2 = .none := by decide

theorem positive_bypass_event_7 :
  step positive_bypass_s6 .commit = positive_bypass_s7 ∧ RemainingDependency.tariff positive_bypass_s6.body.account 1 58 2 0 1 = 2168 ∧ (RemainingDependency.charge positive_bypass_s6.body.account 1 58 2 0 1).2 = .none := by decide

theorem positive_bypass_event_8 :
  step positive_bypass_s7 .retain = positive_bypass_s8 ∧ RemainingDependency.tariff positive_bypass_s7.body.account 1 58 0 59392 0 = 60532 ∧ (RemainingDependency.charge positive_bypass_s7.body.account 1 58 0 59392 0).2 = .none := by decide

theorem positive_bypass_saved_run :
  run positive_bypass_s0 [.install, .fullContact, .fullWrite, .filterFull, .reviseApplication, .choose, .commit, .retain] = positive_bypass_s8 := by decide

theorem positive_bypass_core_trace :
  Generative.Trace process positive_bypass_s0 [.install, .fullContact, .fullWrite, .filterFull, .reviseApplication, .choose, .commit, .retain] positive_bypass_s8 := by
  rw [← positive_bypass_saved_run]
  exact run_is_core_trace _ _

theorem positive_bypass_final_whole_account :
  wholeTotal 8402958 positive_bypass_s8 = 145 * RemainingDependency.ticks := by decide

def positive_independent_config : Config := {fullFault := .faithful, weakFault := .faithful, clamp := false}
def positive_independent_s0 : State := {parent := parent_law_11_learned, config := positive_independent_config, body := {account := {fuel := 444402, start := 444402, spent := 0, live := 34, peak := 42, capacity := 256}, stocks := ⟨0, 10, 0⟩, context := 1, relay := false, pending := none, held := false, installed := false, retained := false, mask := none, fullRecord := none, weakRecord := none, contact := none, application := .unobserved, diagnosis := .unobserved, proposal := none, activation := none, phase := .oldInterface}}
def positive_independent_s1 : State := {parent := parent_law_11_learned, config := positive_independent_config, body := {account := {fuel := 328064, start := 444402, spent := 116338, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 10, 0⟩, context := 1, relay := false, pending := none, held := false, installed := true, retained := false, mask := (some 65535), fullRecord := none, weakRecord := none, contact := none, application := .unobserved, diagnosis := .unobserved, proposal := none, activation := none, phase := .formed}}
def positive_independent_s2 : State := {parent := parent_law_11_learned, config := positive_independent_config, body := {account := {fuel := 311620, start := 444402, spent := 132782, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 10, 0⟩, context := 1, relay := false, pending := none, held := false, installed := true, retained := false, mask := (some 65535), fullRecord := none, weakRecord := none, contact := (some ⟨1, false, true⟩), application := .unobserved, diagnosis := .unobserved, proposal := none, activation := none, phase := .formed}}
def positive_independent_s3 : State := {parent := parent_law_11_learned, config := positive_independent_config, body := {account := {fuel := 308428, start := 444402, spent := 135974, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 10, 0⟩, context := 1, relay := false, pending := none, held := false, installed := true, retained := false, mask := (some 65535), fullRecord := (some ⟨1, false, true⟩), weakRecord := none, contact := none, application := .unobserved, diagnosis := .unobserved, proposal := none, activation := none, phase := .formed}}
def positive_independent_s4 : State := {parent := parent_law_11_learned, config := positive_independent_config, body := {account := {fuel := 274640, start := 444402, spent := 169762, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 10, 0⟩, context := 1, relay := false, pending := none, held := false, installed := true, retained := false, mask := (some 61680), fullRecord := (some ⟨1, false, true⟩), weakRecord := none, contact := none, application := .unobserved, diagnosis := .unobserved, proposal := none, activation := none, phase := .formed}}
def positive_independent_s5 : State := {parent := parent_law_11_learned, config := positive_independent_config, body := {account := {fuel := 271388, start := 444402, spent := 173014, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 10, 0⟩, context := 1, relay := false, pending := none, held := false, installed := true, retained := false, mask := (some 61680), fullRecord := (some ⟨1, false, true⟩), weakRecord := none, contact := none, application := .supported, diagnosis := .unobserved, proposal := none, activation := none, phase := .applicationRevised}}
def positive_independent_s6 : State := {parent := parent_law_11_learned, config := positive_independent_config, body := {account := {fuel := 235583, start := 444402, spent := 208819, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 10, 0⟩, context := 1, relay := false, pending := none, held := false, installed := true, retained := false, mask := (some 61680), fullRecord := (some ⟨1, false, true⟩), weakRecord := none, contact := none, application := .supported, diagnosis := .unobserved, proposal := none, activation := none, phase := .applicationRevised}}
def positive_independent_s7 : State := {parent := parent_law_11_learned, config := positive_independent_config, body := {account := {fuel := 233415, start := 444402, spent := 210987, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 10, 0⟩, context := 1, relay := false, pending := none, held := false, installed := true, retained := false, mask := (some 61680), fullRecord := (some ⟨1, false, true⟩), weakRecord := none, contact := none, application := .supported, diagnosis := .unobserved, proposal := none, activation := none, phase := .committed}}
def positive_independent_s8 : State := {parent := parent_law_11_learned, config := positive_independent_config, body := {account := {fuel := 172883, start := 444402, spent := 271519, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 10, 0⟩, context := 1, relay := false, pending := none, held := false, installed := true, retained := true, mask := (some 61680), fullRecord := (some ⟨1, false, true⟩), weakRecord := none, contact := none, application := .supported, diagnosis := .unobserved, proposal := none, activation := none, phase := .committed}}
theorem positive_independent_actual_entrance :
  entrance parent_law_11_learned positive_independent_config = positive_independent_s0 := by decide

theorem positive_independent_initial_whole_account :
  wholeTotal 8402958 positive_independent_s0 = 145 * RemainingDependency.ticks := by decide

theorem positive_independent_event_1 :
  step positive_independent_s0 .install = positive_independent_s1 ∧ RemainingDependency.tariff positive_independent_s0.body.account 24 58 8 65536 0 = 116338 ∧ (RemainingDependency.charge positive_independent_s0.body.account 24 58 8 65536 0).2 = .none := by decide

theorem positive_independent_event_2 :
  step positive_independent_s1 .fullContact = positive_independent_s2 ∧ RemainingDependency.tariff positive_independent_s1.body.account 0 58 2 16384 0 = 16444 ∧ (RemainingDependency.charge positive_independent_s1.body.account 0 58 2 16384 0).2 = .none := by decide

theorem positive_independent_event_3 :
  step positive_independent_s2 .fullWrite = positive_independent_s3 ∧ RemainingDependency.tariff positive_independent_s2.body.account 1 58 2 0 2 = 3192 ∧ (RemainingDependency.charge positive_independent_s2.body.account 1 58 2 0 2).2 = .none := by decide

theorem positive_independent_event_4 :
  step positive_independent_s3 .filterFull = positive_independent_s4 ∧ RemainingDependency.tariff positive_independent_s3.body.account 16 58 2 0 16 = 33788 ∧ (RemainingDependency.charge positive_independent_s3.body.account 16 58 2 0 16).2 = .none := by decide

theorem positive_independent_event_5 :
  step positive_independent_s4 .reviseApplication = positive_independent_s5 ∧ RemainingDependency.tariff positive_independent_s4.body.account 2 58 2 0 1 = 3252 ∧ (RemainingDependency.charge positive_independent_s4.body.account 2 58 2 0 1).2 = .none := by decide

theorem positive_independent_event_6 :
  step positive_independent_s5 .choose = positive_independent_s6 ∧ RemainingDependency.tariff positive_independent_s5.body.account 32 58 3 0 1 = 35805 ∧ (RemainingDependency.charge positive_independent_s5.body.account 32 58 3 0 1).2 = .none := by decide

theorem positive_independent_event_7 :
  step positive_independent_s6 .commit = positive_independent_s7 ∧ RemainingDependency.tariff positive_independent_s6.body.account 1 58 2 0 1 = 2168 ∧ (RemainingDependency.charge positive_independent_s6.body.account 1 58 2 0 1).2 = .none := by decide

theorem positive_independent_event_8 :
  step positive_independent_s7 .retain = positive_independent_s8 ∧ RemainingDependency.tariff positive_independent_s7.body.account 1 58 0 59392 0 = 60532 ∧ (RemainingDependency.charge positive_independent_s7.body.account 1 58 0 59392 0).2 = .none := by decide

theorem positive_independent_saved_run :
  run positive_independent_s0 [.install, .fullContact, .fullWrite, .filterFull, .reviseApplication, .choose, .commit, .retain] = positive_independent_s8 := by decide

theorem positive_independent_core_trace :
  Generative.Trace process positive_independent_s0 [.install, .fullContact, .fullWrite, .filterFull, .reviseApplication, .choose, .commit, .retain] positive_independent_s8 := by
  rw [← positive_independent_saved_run]
  exact run_is_core_trace _ _

theorem positive_independent_final_whole_account :
  wholeTotal 8402958 positive_independent_s8 = 145 * RemainingDependency.ticks := by decide

def old_false_positive_config : Config := {fullFault := .faithful, weakFault := .faithful, clamp := false}
def old_false_positive_s0 : State := {parent := parent_false_positive_first, config := old_false_positive_config, body := {account := {fuel := 444402, start := 444402, spent := 0, live := 34, peak := 42, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := false, pending := none, held := false, installed := false, retained := false, mask := none, fullRecord := none, weakRecord := none, contact := none, application := .unobserved, diagnosis := .unobserved, proposal := none, activation := none, phase := .oldInterface}}
def old_false_positive_s1 : State := {parent := parent_false_positive_first, config := old_false_positive_config, body := {account := {fuel := 328064, start := 444402, spent := 116338, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := false, pending := none, held := false, installed := true, retained := false, mask := (some 65535), fullRecord := none, weakRecord := none, contact := none, application := .unobserved, diagnosis := .unobserved, proposal := none, activation := none, phase := .formed}}
def old_false_positive_s2 : State := {parent := parent_false_positive_first, config := old_false_positive_config, body := {account := {fuel := 311620, start := 444402, spent := 132782, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := false, pending := none, held := false, installed := true, retained := false, mask := (some 65535), fullRecord := none, weakRecord := none, contact := (some ⟨1, false, false⟩), application := .unobserved, diagnosis := .unobserved, proposal := none, activation := none, phase := .formed}}
def old_false_positive_s3 : State := {parent := parent_false_positive_first, config := old_false_positive_config, body := {account := {fuel := 308428, start := 444402, spent := 135974, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := false, pending := none, held := false, installed := true, retained := false, mask := (some 65535), fullRecord := (some ⟨1, false, false⟩), weakRecord := none, contact := none, application := .unobserved, diagnosis := .unobserved, proposal := none, activation := none, phase := .formed}}
def old_false_positive_s4 : State := {parent := parent_false_positive_first, config := old_false_positive_config, body := {account := {fuel := 274640, start := 444402, spent := 169762, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := false, pending := none, held := false, installed := true, retained := false, mask := (some 3855), fullRecord := (some ⟨1, false, false⟩), weakRecord := none, contact := none, application := .unobserved, diagnosis := .unobserved, proposal := none, activation := none, phase := .formed}}
def old_false_positive_s5 : State := {parent := parent_false_positive_first, config := old_false_positive_config, body := {account := {fuel := 271388, start := 444402, spent := 173014, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := false, pending := none, held := false, installed := true, retained := false, mask := (some 3855), fullRecord := (some ⟨1, false, false⟩), weakRecord := none, contact := none, application := .failed, diagnosis := .unobserved, proposal := none, activation := none, phase := .applicationRevised}}
def old_false_positive_s6 : State := {parent := parent_false_positive_first, config := old_false_positive_config, body := {account := {fuel := 235583, start := 444402, spent := 208819, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := false, pending := none, held := false, installed := true, retained := false, mask := (some 3855), fullRecord := (some ⟨1, false, false⟩), weakRecord := none, contact := none, application := .failed, diagnosis := .unobserved, proposal := (some false), activation := none, phase := .applicationRevised}}
def old_false_positive_s7 : State := {parent := parent_false_positive_first, config := old_false_positive_config, body := {account := {fuel := 233415, start := 444402, spent := 210987, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := false, pending := none, held := false, installed := true, retained := false, mask := (some 3855), fullRecord := (some ⟨1, false, false⟩), weakRecord := none, contact := none, application := .failed, diagnosis := .unobserved, proposal := (some false), activation := (some false), phase := .committed}}
def old_false_positive_s8 : State := {parent := parent_false_positive_first, config := old_false_positive_config, body := {account := {fuel := 215887, start := 444402, spent := 228515, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := false, pending := none, held := false, installed := true, retained := false, mask := (some 3855), fullRecord := (some ⟨1, false, false⟩), weakRecord := none, contact := none, application := .failed, diagnosis := .unobserved, proposal := (some false), activation := (some false), phase := .committed}}
def old_false_positive_s9 : State := {parent := parent_false_positive_first, config := old_false_positive_config, body := {account := {fuel := 198359, start := 444402, spent := 246043, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := false, pending := (some ⟨1, false, false⟩), held := false, installed := true, retained := false, mask := (some 3855), fullRecord := (some ⟨1, false, false⟩), weakRecord := none, contact := none, application := .failed, diagnosis := .unobserved, proposal := (some false), activation := (some false), phase := .committed}}
def old_false_positive_s10 : State := {parent := parent_false_positive_first, config := old_false_positive_config, body := {account := {fuel := 181915, start := 444402, spent := 262487, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := false, pending := none, held := false, installed := true, retained := false, mask := (some 3855), fullRecord := (some ⟨1, false, false⟩), weakRecord := none, contact := (some ⟨1, false, false⟩), application := .failed, diagnosis := .unobserved, proposal := (some false), activation := (some false), phase := .committed}}
def old_false_positive_s11 : State := {parent := parent_false_positive_first, config := old_false_positive_config, body := {account := {fuel := 178723, start := 444402, spent := 265679, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := false, pending := none, held := false, installed := true, retained := false, mask := (some 3855), fullRecord := (some ⟨1, false, false⟩), weakRecord := (some ⟨1, false, false⟩), contact := none, application := .failed, diagnosis := .unobserved, proposal := (some false), activation := (some false), phase := .committed}}
def old_false_positive_s12 : State := {parent := parent_false_positive_first, config := old_false_positive_config, body := {account := {fuel := 144935, start := 444402, spent := 299467, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := false, pending := none, held := false, installed := true, retained := false, mask := (some 1285), fullRecord := (some ⟨1, false, false⟩), weakRecord := (some ⟨1, false, false⟩), contact := none, application := .failed, diagnosis := .unobserved, proposal := (some false), activation := (some false), phase := .committed}}
def old_false_positive_s13 : State := {parent := parent_false_positive_first, config := old_false_positive_config, body := {account := {fuel := 141683, start := 444402, spent := 302719, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := false, pending := none, held := false, installed := true, retained := false, mask := (some 1285), fullRecord := (some ⟨1, false, false⟩), weakRecord := (some ⟨1, false, false⟩), contact := none, application := .failed, diagnosis := .oldContradicted, proposal := (some false), activation := (some false), phase := .diagnosisRevised}}
def old_false_positive_s14 : State := {parent := parent_false_positive_first, config := old_false_positive_config, body := {account := {fuel := 81151, start := 444402, spent := 363251, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := false, pending := none, held := false, installed := true, retained := true, mask := (some 1285), fullRecord := (some ⟨1, false, false⟩), weakRecord := (some ⟨1, false, false⟩), contact := none, application := .failed, diagnosis := .oldContradicted, proposal := (some false), activation := (some false), phase := .diagnosisRevised}}
theorem old_false_positive_actual_entrance :
  entrance parent_false_positive_first old_false_positive_config = old_false_positive_s0 := by decide

theorem old_false_positive_initial_whole_account :
  wholeTotal 8402958 old_false_positive_s0 = 145 * RemainingDependency.ticks := by decide

theorem old_false_positive_event_1 :
  step old_false_positive_s0 .install = old_false_positive_s1 ∧ RemainingDependency.tariff old_false_positive_s0.body.account 24 58 8 65536 0 = 116338 ∧ (RemainingDependency.charge old_false_positive_s0.body.account 24 58 8 65536 0).2 = .none := by decide

theorem old_false_positive_event_2 :
  step old_false_positive_s1 .fullContact = old_false_positive_s2 ∧ RemainingDependency.tariff old_false_positive_s1.body.account 0 58 2 16384 0 = 16444 ∧ (RemainingDependency.charge old_false_positive_s1.body.account 0 58 2 16384 0).2 = .none := by decide

theorem old_false_positive_event_3 :
  step old_false_positive_s2 .fullWrite = old_false_positive_s3 ∧ RemainingDependency.tariff old_false_positive_s2.body.account 1 58 2 0 2 = 3192 ∧ (RemainingDependency.charge old_false_positive_s2.body.account 1 58 2 0 2).2 = .none := by decide

theorem old_false_positive_event_4 :
  step old_false_positive_s3 .filterFull = old_false_positive_s4 ∧ RemainingDependency.tariff old_false_positive_s3.body.account 16 58 2 0 16 = 33788 ∧ (RemainingDependency.charge old_false_positive_s3.body.account 16 58 2 0 16).2 = .none := by decide

theorem old_false_positive_event_5 :
  step old_false_positive_s4 .reviseApplication = old_false_positive_s5 ∧ RemainingDependency.tariff old_false_positive_s4.body.account 2 58 2 0 1 = 3252 ∧ (RemainingDependency.charge old_false_positive_s4.body.account 2 58 2 0 1).2 = .none := by decide

theorem old_false_positive_event_6 :
  step old_false_positive_s5 .choose = old_false_positive_s6 ∧ RemainingDependency.tariff old_false_positive_s5.body.account 32 58 3 0 1 = 35805 ∧ (RemainingDependency.charge old_false_positive_s5.body.account 32 58 3 0 1).2 = .none := by decide

theorem old_false_positive_event_7 :
  step old_false_positive_s6 .commit = old_false_positive_s7 ∧ RemainingDependency.tariff old_false_positive_s6.body.account 1 58 2 0 1 = 2168 ∧ (RemainingDependency.charge old_false_positive_s6.body.account 1 58 2 0 1).2 = .none := by decide

theorem old_false_positive_event_8 :
  step old_false_positive_s7 (.command false) = old_false_positive_s8 ∧ RemainingDependency.tariff old_false_positive_s7.body.account 1 58 2 16384 0 = 17528 ∧ (RemainingDependency.charge old_false_positive_s7.body.account 1 58 2 16384 0).2 = .none := by decide

theorem old_false_positive_event_9 :
  step old_false_positive_s8 .challenge = old_false_positive_s9 ∧ RemainingDependency.tariff old_false_positive_s8.body.account 1 58 2 16384 0 = 17528 ∧ (RemainingDependency.charge old_false_positive_s8.body.account 1 58 2 16384 0).2 = .none := by decide

theorem old_false_positive_event_10 :
  step old_false_positive_s9 .weakContact = old_false_positive_s10 ∧ RemainingDependency.tariff old_false_positive_s9.body.account 0 58 2 16384 0 = 16444 ∧ (RemainingDependency.charge old_false_positive_s9.body.account 0 58 2 16384 0).2 = .none := by decide

theorem old_false_positive_event_11 :
  step old_false_positive_s10 .weakWrite = old_false_positive_s11 ∧ RemainingDependency.tariff old_false_positive_s10.body.account 1 58 2 0 2 = 3192 ∧ (RemainingDependency.charge old_false_positive_s10.body.account 1 58 2 0 2).2 = .none := by decide

theorem old_false_positive_event_12 :
  step old_false_positive_s11 .filterWeak = old_false_positive_s12 ∧ RemainingDependency.tariff old_false_positive_s11.body.account 16 58 2 0 16 = 33788 ∧ (RemainingDependency.charge old_false_positive_s11.body.account 16 58 2 0 16).2 = .none := by decide

theorem old_false_positive_event_13 :
  step old_false_positive_s12 .reviseDiagnosis = old_false_positive_s13 ∧ RemainingDependency.tariff old_false_positive_s12.body.account 2 58 2 0 1 = 3252 ∧ (RemainingDependency.charge old_false_positive_s12.body.account 2 58 2 0 1).2 = .none := by decide

theorem old_false_positive_event_14 :
  step old_false_positive_s13 .retain = old_false_positive_s14 ∧ RemainingDependency.tariff old_false_positive_s13.body.account 1 58 0 59392 0 = 60532 ∧ (RemainingDependency.charge old_false_positive_s13.body.account 1 58 0 59392 0).2 = .none := by decide

theorem old_false_positive_saved_run :
  run old_false_positive_s0 [.install, .fullContact, .fullWrite, .filterFull, .reviseApplication, .choose, .commit, (.command false), .challenge, .weakContact, .weakWrite, .filterWeak, .reviseDiagnosis, .retain] = old_false_positive_s14 := by decide

theorem old_false_positive_core_trace :
  Generative.Trace process old_false_positive_s0 [.install, .fullContact, .fullWrite, .filterFull, .reviseApplication, .choose, .commit, (.command false), .challenge, .weakContact, .weakWrite, .filterWeak, .reviseDiagnosis, .retain] old_false_positive_s14 := by
  rw [← old_false_positive_saved_run]
  exact run_is_core_trace _ _

theorem old_false_positive_final_whole_account :
  wholeTotal 8402958 old_false_positive_s14 = 145 * RemainingDependency.ticks := by decide

def full_fault_missing_config : Config := {fullFault := .missing, weakFault := .faithful, clamp := false}
def full_fault_missing_s0 : State := {parent := parent_calibration_break, config := full_fault_missing_config, body := {account := {fuel := 428018, start := 428018, spent := 0, live := 34, peak := 42, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := false, retained := false, mask := none, fullRecord := none, weakRecord := none, contact := none, application := .unobserved, diagnosis := .unobserved, proposal := none, activation := none, phase := .oldInterface}}
def full_fault_missing_s1 : State := {parent := parent_calibration_break, config := full_fault_missing_config, body := {account := {fuel := 311680, start := 428018, spent := 116338, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := false, mask := (some 65535), fullRecord := none, weakRecord := none, contact := none, application := .unobserved, diagnosis := .unobserved, proposal := none, activation := none, phase := .formed}}
def full_fault_missing_s2 : State := {parent := parent_calibration_break, config := full_fault_missing_config, body := {account := {fuel := 295236, start := 428018, spent := 132782, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := false, mask := (some 65535), fullRecord := none, weakRecord := none, contact := none, application := .unobserved, diagnosis := .unobserved, proposal := none, activation := none, phase := .formed}}
def full_fault_missing_s3 : State := {parent := parent_calibration_break, config := full_fault_missing_config, body := {account := {fuel := 292044, start := 428018, spent := 135974, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := false, mask := (some 65535), fullRecord := none, weakRecord := none, contact := none, application := .unobserved, diagnosis := .unobserved, proposal := none, activation := none, phase := .formed}}
def full_fault_missing_s4 : State := {parent := parent_calibration_break, config := full_fault_missing_config, body := {account := {fuel := 258256, start := 428018, spent := 169762, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := false, mask := (some 65535), fullRecord := none, weakRecord := none, contact := none, application := .unobserved, diagnosis := .unobserved, proposal := none, activation := none, phase := .formed}}
def full_fault_missing_s5 : State := {parent := parent_calibration_break, config := full_fault_missing_config, body := {account := {fuel := 255004, start := 428018, spent := 173014, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := false, mask := (some 65535), fullRecord := none, weakRecord := none, contact := none, application := .unavailable, diagnosis := .unobserved, proposal := none, activation := none, phase := .applicationRevised}}
def full_fault_missing_s6 : State := {parent := parent_calibration_break, config := full_fault_missing_config, body := {account := {fuel := 219199, start := 428018, spent := 208819, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := false, mask := (some 65535), fullRecord := none, weakRecord := none, contact := none, application := .unavailable, diagnosis := .unobserved, proposal := none, activation := none, phase := .applicationRevised}}
def full_fault_missing_s7 : State := {parent := parent_calibration_break, config := full_fault_missing_config, body := {account := {fuel := 217031, start := 428018, spent := 210987, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := false, mask := (some 65535), fullRecord := none, weakRecord := none, contact := none, application := .unavailable, diagnosis := .unobserved, proposal := none, activation := none, phase := .committed}}
def full_fault_missing_s8 : State := {parent := parent_calibration_break, config := full_fault_missing_config, body := {account := {fuel := 156499, start := 428018, spent := 271519, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := true, mask := (some 65535), fullRecord := none, weakRecord := none, contact := none, application := .unavailable, diagnosis := .unobserved, proposal := none, activation := none, phase := .committed}}
theorem full_fault_missing_actual_entrance :
  entrance parent_calibration_break full_fault_missing_config = full_fault_missing_s0 := by decide

theorem full_fault_missing_initial_whole_account :
  wholeTotal 8419342 full_fault_missing_s0 = 145 * RemainingDependency.ticks := by decide

theorem full_fault_missing_event_1 :
  step full_fault_missing_s0 .install = full_fault_missing_s1 ∧ RemainingDependency.tariff full_fault_missing_s0.body.account 24 58 8 65536 0 = 116338 ∧ (RemainingDependency.charge full_fault_missing_s0.body.account 24 58 8 65536 0).2 = .none := by decide

theorem full_fault_missing_event_2 :
  step full_fault_missing_s1 .fullContact = full_fault_missing_s2 ∧ RemainingDependency.tariff full_fault_missing_s1.body.account 0 58 2 16384 0 = 16444 ∧ (RemainingDependency.charge full_fault_missing_s1.body.account 0 58 2 16384 0).2 = .none := by decide

theorem full_fault_missing_event_3 :
  step full_fault_missing_s2 .fullWrite = full_fault_missing_s3 ∧ RemainingDependency.tariff full_fault_missing_s2.body.account 1 58 2 0 2 = 3192 ∧ (RemainingDependency.charge full_fault_missing_s2.body.account 1 58 2 0 2).2 = .none := by decide

theorem full_fault_missing_event_4 :
  step full_fault_missing_s3 .filterFull = full_fault_missing_s4 ∧ RemainingDependency.tariff full_fault_missing_s3.body.account 16 58 2 0 16 = 33788 ∧ (RemainingDependency.charge full_fault_missing_s3.body.account 16 58 2 0 16).2 = .none := by decide

theorem full_fault_missing_event_5 :
  step full_fault_missing_s4 .reviseApplication = full_fault_missing_s5 ∧ RemainingDependency.tariff full_fault_missing_s4.body.account 2 58 2 0 1 = 3252 ∧ (RemainingDependency.charge full_fault_missing_s4.body.account 2 58 2 0 1).2 = .none := by decide

theorem full_fault_missing_event_6 :
  step full_fault_missing_s5 .choose = full_fault_missing_s6 ∧ RemainingDependency.tariff full_fault_missing_s5.body.account 32 58 3 0 1 = 35805 ∧ (RemainingDependency.charge full_fault_missing_s5.body.account 32 58 3 0 1).2 = .none := by decide

theorem full_fault_missing_event_7 :
  step full_fault_missing_s6 .commit = full_fault_missing_s7 ∧ RemainingDependency.tariff full_fault_missing_s6.body.account 1 58 2 0 1 = 2168 ∧ (RemainingDependency.charge full_fault_missing_s6.body.account 1 58 2 0 1).2 = .none := by decide

theorem full_fault_missing_event_8 :
  step full_fault_missing_s7 .retain = full_fault_missing_s8 ∧ RemainingDependency.tariff full_fault_missing_s7.body.account 1 58 0 59392 0 = 60532 ∧ (RemainingDependency.charge full_fault_missing_s7.body.account 1 58 0 59392 0).2 = .none := by decide

theorem full_fault_missing_saved_run :
  run full_fault_missing_s0 [.install, .fullContact, .fullWrite, .filterFull, .reviseApplication, .choose, .commit, .retain] = full_fault_missing_s8 := by decide

theorem full_fault_missing_core_trace :
  Generative.Trace process full_fault_missing_s0 [.install, .fullContact, .fullWrite, .filterFull, .reviseApplication, .choose, .commit, .retain] full_fault_missing_s8 := by
  rw [← full_fault_missing_saved_run]
  exact run_is_core_trace _ _

theorem full_fault_missing_final_whole_account :
  wholeTotal 8419342 full_fault_missing_s8 = 145 * RemainingDependency.ticks := by decide

def full_fault_flip_config : Config := {fullFault := .flip, weakFault := .faithful, clamp := false}
def full_fault_flip_s0 : State := {parent := parent_calibration_break, config := full_fault_flip_config, body := {account := {fuel := 428018, start := 428018, spent := 0, live := 34, peak := 42, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := false, retained := false, mask := none, fullRecord := none, weakRecord := none, contact := none, application := .unobserved, diagnosis := .unobserved, proposal := none, activation := none, phase := .oldInterface}}
def full_fault_flip_s1 : State := {parent := parent_calibration_break, config := full_fault_flip_config, body := {account := {fuel := 311680, start := 428018, spent := 116338, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := false, mask := (some 65535), fullRecord := none, weakRecord := none, contact := none, application := .unobserved, diagnosis := .unobserved, proposal := none, activation := none, phase := .formed}}
def full_fault_flip_s2 : State := {parent := parent_calibration_break, config := full_fault_flip_config, body := {account := {fuel := 295236, start := 428018, spent := 132782, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := false, mask := (some 65535), fullRecord := none, weakRecord := none, contact := (some ⟨1, true, true⟩), application := .unobserved, diagnosis := .unobserved, proposal := none, activation := none, phase := .formed}}
def full_fault_flip_s3 : State := {parent := parent_calibration_break, config := full_fault_flip_config, body := {account := {fuel := 292044, start := 428018, spent := 135974, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := false, mask := (some 65535), fullRecord := (some ⟨1, true, true⟩), weakRecord := none, contact := none, application := .unobserved, diagnosis := .unobserved, proposal := none, activation := none, phase := .formed}}
def full_fault_flip_s4 : State := {parent := parent_calibration_break, config := full_fault_flip_config, body := {account := {fuel := 258256, start := 428018, spent := 169762, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := false, mask := (some 65280), fullRecord := (some ⟨1, true, true⟩), weakRecord := none, contact := none, application := .unobserved, diagnosis := .unobserved, proposal := none, activation := none, phase := .formed}}
def full_fault_flip_s5 : State := {parent := parent_calibration_break, config := full_fault_flip_config, body := {account := {fuel := 255004, start := 428018, spent := 173014, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := false, mask := (some 65280), fullRecord := (some ⟨1, true, true⟩), weakRecord := none, contact := none, application := .supported, diagnosis := .unobserved, proposal := none, activation := none, phase := .applicationRevised}}
def full_fault_flip_s6 : State := {parent := parent_calibration_break, config := full_fault_flip_config, body := {account := {fuel := 219199, start := 428018, spent := 208819, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := false, mask := (some 65280), fullRecord := (some ⟨1, true, true⟩), weakRecord := none, contact := none, application := .supported, diagnosis := .unobserved, proposal := none, activation := none, phase := .applicationRevised}}
def full_fault_flip_s7 : State := {parent := parent_calibration_break, config := full_fault_flip_config, body := {account := {fuel := 217031, start := 428018, spent := 210987, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := false, mask := (some 65280), fullRecord := (some ⟨1, true, true⟩), weakRecord := none, contact := none, application := .supported, diagnosis := .unobserved, proposal := none, activation := none, phase := .committed}}
def full_fault_flip_s8 : State := {parent := parent_calibration_break, config := full_fault_flip_config, body := {account := {fuel := 156499, start := 428018, spent := 271519, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := true, mask := (some 65280), fullRecord := (some ⟨1, true, true⟩), weakRecord := none, contact := none, application := .supported, diagnosis := .unobserved, proposal := none, activation := none, phase := .committed}}
theorem full_fault_flip_actual_entrance :
  entrance parent_calibration_break full_fault_flip_config = full_fault_flip_s0 := by decide

theorem full_fault_flip_initial_whole_account :
  wholeTotal 8419342 full_fault_flip_s0 = 145 * RemainingDependency.ticks := by decide

theorem full_fault_flip_event_1 :
  step full_fault_flip_s0 .install = full_fault_flip_s1 ∧ RemainingDependency.tariff full_fault_flip_s0.body.account 24 58 8 65536 0 = 116338 ∧ (RemainingDependency.charge full_fault_flip_s0.body.account 24 58 8 65536 0).2 = .none := by decide

theorem full_fault_flip_event_2 :
  step full_fault_flip_s1 .fullContact = full_fault_flip_s2 ∧ RemainingDependency.tariff full_fault_flip_s1.body.account 0 58 2 16384 0 = 16444 ∧ (RemainingDependency.charge full_fault_flip_s1.body.account 0 58 2 16384 0).2 = .none := by decide

theorem full_fault_flip_event_3 :
  step full_fault_flip_s2 .fullWrite = full_fault_flip_s3 ∧ RemainingDependency.tariff full_fault_flip_s2.body.account 1 58 2 0 2 = 3192 ∧ (RemainingDependency.charge full_fault_flip_s2.body.account 1 58 2 0 2).2 = .none := by decide

theorem full_fault_flip_event_4 :
  step full_fault_flip_s3 .filterFull = full_fault_flip_s4 ∧ RemainingDependency.tariff full_fault_flip_s3.body.account 16 58 2 0 16 = 33788 ∧ (RemainingDependency.charge full_fault_flip_s3.body.account 16 58 2 0 16).2 = .none := by decide

theorem full_fault_flip_event_5 :
  step full_fault_flip_s4 .reviseApplication = full_fault_flip_s5 ∧ RemainingDependency.tariff full_fault_flip_s4.body.account 2 58 2 0 1 = 3252 ∧ (RemainingDependency.charge full_fault_flip_s4.body.account 2 58 2 0 1).2 = .none := by decide

theorem full_fault_flip_event_6 :
  step full_fault_flip_s5 .choose = full_fault_flip_s6 ∧ RemainingDependency.tariff full_fault_flip_s5.body.account 32 58 3 0 1 = 35805 ∧ (RemainingDependency.charge full_fault_flip_s5.body.account 32 58 3 0 1).2 = .none := by decide

theorem full_fault_flip_event_7 :
  step full_fault_flip_s6 .commit = full_fault_flip_s7 ∧ RemainingDependency.tariff full_fault_flip_s6.body.account 1 58 2 0 1 = 2168 ∧ (RemainingDependency.charge full_fault_flip_s6.body.account 1 58 2 0 1).2 = .none := by decide

theorem full_fault_flip_event_8 :
  step full_fault_flip_s7 .retain = full_fault_flip_s8 ∧ RemainingDependency.tariff full_fault_flip_s7.body.account 1 58 0 59392 0 = 60532 ∧ (RemainingDependency.charge full_fault_flip_s7.body.account 1 58 0 59392 0).2 = .none := by decide

theorem full_fault_flip_saved_run :
  run full_fault_flip_s0 [.install, .fullContact, .fullWrite, .filterFull, .reviseApplication, .choose, .commit, .retain] = full_fault_flip_s8 := by decide

theorem full_fault_flip_core_trace :
  Generative.Trace process full_fault_flip_s0 [.install, .fullContact, .fullWrite, .filterFull, .reviseApplication, .choose, .commit, .retain] full_fault_flip_s8 := by
  rw [← full_fault_flip_saved_run]
  exact run_is_core_trace _ _

theorem full_fault_flip_final_whole_account :
  wholeTotal 8419342 full_fault_flip_s8 = 145 * RemainingDependency.ticks := by decide

def full_fault_context_config : Config := {fullFault := .wrongContext, weakFault := .faithful, clamp := false}
def full_fault_context_s0 : State := {parent := parent_calibration_break, config := full_fault_context_config, body := {account := {fuel := 428018, start := 428018, spent := 0, live := 34, peak := 42, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := false, retained := false, mask := none, fullRecord := none, weakRecord := none, contact := none, application := .unobserved, diagnosis := .unobserved, proposal := none, activation := none, phase := .oldInterface}}
def full_fault_context_s1 : State := {parent := parent_calibration_break, config := full_fault_context_config, body := {account := {fuel := 311680, start := 428018, spent := 116338, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := false, mask := (some 65535), fullRecord := none, weakRecord := none, contact := none, application := .unobserved, diagnosis := .unobserved, proposal := none, activation := none, phase := .formed}}
def full_fault_context_s2 : State := {parent := parent_calibration_break, config := full_fault_context_config, body := {account := {fuel := 295236, start := 428018, spent := 132782, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := false, mask := (some 65535), fullRecord := none, weakRecord := none, contact := (some ⟨2, true, false⟩), application := .unobserved, diagnosis := .unobserved, proposal := none, activation := none, phase := .formed}}
def full_fault_context_s3 : State := {parent := parent_calibration_break, config := full_fault_context_config, body := {account := {fuel := 292044, start := 428018, spent := 135974, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := false, mask := (some 65535), fullRecord := none, weakRecord := none, contact := none, application := .unobserved, diagnosis := .unobserved, proposal := none, activation := none, phase := .formed}}
def full_fault_context_s4 : State := {parent := parent_calibration_break, config := full_fault_context_config, body := {account := {fuel := 258256, start := 428018, spent := 169762, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := false, mask := (some 65535), fullRecord := none, weakRecord := none, contact := none, application := .unobserved, diagnosis := .unobserved, proposal := none, activation := none, phase := .formed}}
def full_fault_context_s5 : State := {parent := parent_calibration_break, config := full_fault_context_config, body := {account := {fuel := 255004, start := 428018, spent := 173014, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := false, mask := (some 65535), fullRecord := none, weakRecord := none, contact := none, application := .unavailable, diagnosis := .unobserved, proposal := none, activation := none, phase := .applicationRevised}}
def full_fault_context_s6 : State := {parent := parent_calibration_break, config := full_fault_context_config, body := {account := {fuel := 219199, start := 428018, spent := 208819, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := false, mask := (some 65535), fullRecord := none, weakRecord := none, contact := none, application := .unavailable, diagnosis := .unobserved, proposal := none, activation := none, phase := .applicationRevised}}
def full_fault_context_s7 : State := {parent := parent_calibration_break, config := full_fault_context_config, body := {account := {fuel := 217031, start := 428018, spent := 210987, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := false, mask := (some 65535), fullRecord := none, weakRecord := none, contact := none, application := .unavailable, diagnosis := .unobserved, proposal := none, activation := none, phase := .committed}}
def full_fault_context_s8 : State := {parent := parent_calibration_break, config := full_fault_context_config, body := {account := {fuel := 156499, start := 428018, spent := 271519, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := true, mask := (some 65535), fullRecord := none, weakRecord := none, contact := none, application := .unavailable, diagnosis := .unobserved, proposal := none, activation := none, phase := .committed}}
theorem full_fault_context_actual_entrance :
  entrance parent_calibration_break full_fault_context_config = full_fault_context_s0 := by decide

theorem full_fault_context_initial_whole_account :
  wholeTotal 8419342 full_fault_context_s0 = 145 * RemainingDependency.ticks := by decide

theorem full_fault_context_event_1 :
  step full_fault_context_s0 .install = full_fault_context_s1 ∧ RemainingDependency.tariff full_fault_context_s0.body.account 24 58 8 65536 0 = 116338 ∧ (RemainingDependency.charge full_fault_context_s0.body.account 24 58 8 65536 0).2 = .none := by decide

theorem full_fault_context_event_2 :
  step full_fault_context_s1 .fullContact = full_fault_context_s2 ∧ RemainingDependency.tariff full_fault_context_s1.body.account 0 58 2 16384 0 = 16444 ∧ (RemainingDependency.charge full_fault_context_s1.body.account 0 58 2 16384 0).2 = .none := by decide

theorem full_fault_context_event_3 :
  step full_fault_context_s2 .fullWrite = full_fault_context_s3 ∧ RemainingDependency.tariff full_fault_context_s2.body.account 1 58 2 0 2 = 3192 ∧ (RemainingDependency.charge full_fault_context_s2.body.account 1 58 2 0 2).2 = .none := by decide

theorem full_fault_context_event_4 :
  step full_fault_context_s3 .filterFull = full_fault_context_s4 ∧ RemainingDependency.tariff full_fault_context_s3.body.account 16 58 2 0 16 = 33788 ∧ (RemainingDependency.charge full_fault_context_s3.body.account 16 58 2 0 16).2 = .none := by decide

theorem full_fault_context_event_5 :
  step full_fault_context_s4 .reviseApplication = full_fault_context_s5 ∧ RemainingDependency.tariff full_fault_context_s4.body.account 2 58 2 0 1 = 3252 ∧ (RemainingDependency.charge full_fault_context_s4.body.account 2 58 2 0 1).2 = .none := by decide

theorem full_fault_context_event_6 :
  step full_fault_context_s5 .choose = full_fault_context_s6 ∧ RemainingDependency.tariff full_fault_context_s5.body.account 32 58 3 0 1 = 35805 ∧ (RemainingDependency.charge full_fault_context_s5.body.account 32 58 3 0 1).2 = .none := by decide

theorem full_fault_context_event_7 :
  step full_fault_context_s6 .commit = full_fault_context_s7 ∧ RemainingDependency.tariff full_fault_context_s6.body.account 1 58 2 0 1 = 2168 ∧ (RemainingDependency.charge full_fault_context_s6.body.account 1 58 2 0 1).2 = .none := by decide

theorem full_fault_context_event_8 :
  step full_fault_context_s7 .retain = full_fault_context_s8 ∧ RemainingDependency.tariff full_fault_context_s7.body.account 1 58 0 59392 0 = 60532 ∧ (RemainingDependency.charge full_fault_context_s7.body.account 1 58 0 59392 0).2 = .none := by decide

theorem full_fault_context_saved_run :
  run full_fault_context_s0 [.install, .fullContact, .fullWrite, .filterFull, .reviseApplication, .choose, .commit, .retain] = full_fault_context_s8 := by decide

theorem full_fault_context_core_trace :
  Generative.Trace process full_fault_context_s0 [.install, .fullContact, .fullWrite, .filterFull, .reviseApplication, .choose, .commit, .retain] full_fault_context_s8 := by
  rw [← full_fault_context_saved_run]
  exact run_is_core_trace _ _

theorem full_fault_context_final_whole_account :
  wholeTotal 8419342 full_fault_context_s8 = 145 * RemainingDependency.ticks := by decide

def full_fault_setting_config : Config := {fullFault := .wrongSetting, weakFault := .faithful, clamp := false}
def full_fault_setting_s0 : State := {parent := parent_calibration_break, config := full_fault_setting_config, body := {account := {fuel := 428018, start := 428018, spent := 0, live := 34, peak := 42, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := false, retained := false, mask := none, fullRecord := none, weakRecord := none, contact := none, application := .unobserved, diagnosis := .unobserved, proposal := none, activation := none, phase := .oldInterface}}
def full_fault_setting_s1 : State := {parent := parent_calibration_break, config := full_fault_setting_config, body := {account := {fuel := 311680, start := 428018, spent := 116338, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := false, mask := (some 65535), fullRecord := none, weakRecord := none, contact := none, application := .unobserved, diagnosis := .unobserved, proposal := none, activation := none, phase := .formed}}
def full_fault_setting_s2 : State := {parent := parent_calibration_break, config := full_fault_setting_config, body := {account := {fuel := 295236, start := 428018, spent := 132782, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := false, mask := (some 65535), fullRecord := none, weakRecord := none, contact := (some ⟨1, false, false⟩), application := .unobserved, diagnosis := .unobserved, proposal := none, activation := none, phase := .formed}}
def full_fault_setting_s3 : State := {parent := parent_calibration_break, config := full_fault_setting_config, body := {account := {fuel := 292044, start := 428018, spent := 135974, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := false, mask := (some 65535), fullRecord := none, weakRecord := none, contact := none, application := .unobserved, diagnosis := .unobserved, proposal := none, activation := none, phase := .formed}}
def full_fault_setting_s4 : State := {parent := parent_calibration_break, config := full_fault_setting_config, body := {account := {fuel := 258256, start := 428018, spent := 169762, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := false, mask := (some 65535), fullRecord := none, weakRecord := none, contact := none, application := .unobserved, diagnosis := .unobserved, proposal := none, activation := none, phase := .formed}}
def full_fault_setting_s5 : State := {parent := parent_calibration_break, config := full_fault_setting_config, body := {account := {fuel := 255004, start := 428018, spent := 173014, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := false, mask := (some 65535), fullRecord := none, weakRecord := none, contact := none, application := .unavailable, diagnosis := .unobserved, proposal := none, activation := none, phase := .applicationRevised}}
def full_fault_setting_s6 : State := {parent := parent_calibration_break, config := full_fault_setting_config, body := {account := {fuel := 219199, start := 428018, spent := 208819, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := false, mask := (some 65535), fullRecord := none, weakRecord := none, contact := none, application := .unavailable, diagnosis := .unobserved, proposal := none, activation := none, phase := .applicationRevised}}
def full_fault_setting_s7 : State := {parent := parent_calibration_break, config := full_fault_setting_config, body := {account := {fuel := 217031, start := 428018, spent := 210987, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := false, mask := (some 65535), fullRecord := none, weakRecord := none, contact := none, application := .unavailable, diagnosis := .unobserved, proposal := none, activation := none, phase := .committed}}
def full_fault_setting_s8 : State := {parent := parent_calibration_break, config := full_fault_setting_config, body := {account := {fuel := 156499, start := 428018, spent := 271519, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := true, mask := (some 65535), fullRecord := none, weakRecord := none, contact := none, application := .unavailable, diagnosis := .unobserved, proposal := none, activation := none, phase := .committed}}
theorem full_fault_setting_actual_entrance :
  entrance parent_calibration_break full_fault_setting_config = full_fault_setting_s0 := by decide

theorem full_fault_setting_initial_whole_account :
  wholeTotal 8419342 full_fault_setting_s0 = 145 * RemainingDependency.ticks := by decide

theorem full_fault_setting_event_1 :
  step full_fault_setting_s0 .install = full_fault_setting_s1 ∧ RemainingDependency.tariff full_fault_setting_s0.body.account 24 58 8 65536 0 = 116338 ∧ (RemainingDependency.charge full_fault_setting_s0.body.account 24 58 8 65536 0).2 = .none := by decide

theorem full_fault_setting_event_2 :
  step full_fault_setting_s1 .fullContact = full_fault_setting_s2 ∧ RemainingDependency.tariff full_fault_setting_s1.body.account 0 58 2 16384 0 = 16444 ∧ (RemainingDependency.charge full_fault_setting_s1.body.account 0 58 2 16384 0).2 = .none := by decide

theorem full_fault_setting_event_3 :
  step full_fault_setting_s2 .fullWrite = full_fault_setting_s3 ∧ RemainingDependency.tariff full_fault_setting_s2.body.account 1 58 2 0 2 = 3192 ∧ (RemainingDependency.charge full_fault_setting_s2.body.account 1 58 2 0 2).2 = .none := by decide

theorem full_fault_setting_event_4 :
  step full_fault_setting_s3 .filterFull = full_fault_setting_s4 ∧ RemainingDependency.tariff full_fault_setting_s3.body.account 16 58 2 0 16 = 33788 ∧ (RemainingDependency.charge full_fault_setting_s3.body.account 16 58 2 0 16).2 = .none := by decide

theorem full_fault_setting_event_5 :
  step full_fault_setting_s4 .reviseApplication = full_fault_setting_s5 ∧ RemainingDependency.tariff full_fault_setting_s4.body.account 2 58 2 0 1 = 3252 ∧ (RemainingDependency.charge full_fault_setting_s4.body.account 2 58 2 0 1).2 = .none := by decide

theorem full_fault_setting_event_6 :
  step full_fault_setting_s5 .choose = full_fault_setting_s6 ∧ RemainingDependency.tariff full_fault_setting_s5.body.account 32 58 3 0 1 = 35805 ∧ (RemainingDependency.charge full_fault_setting_s5.body.account 32 58 3 0 1).2 = .none := by decide

theorem full_fault_setting_event_7 :
  step full_fault_setting_s6 .commit = full_fault_setting_s7 ∧ RemainingDependency.tariff full_fault_setting_s6.body.account 1 58 2 0 1 = 2168 ∧ (RemainingDependency.charge full_fault_setting_s6.body.account 1 58 2 0 1).2 = .none := by decide

theorem full_fault_setting_event_8 :
  step full_fault_setting_s7 .retain = full_fault_setting_s8 ∧ RemainingDependency.tariff full_fault_setting_s7.body.account 1 58 0 59392 0 = 60532 ∧ (RemainingDependency.charge full_fault_setting_s7.body.account 1 58 0 59392 0).2 = .none := by decide

theorem full_fault_setting_saved_run :
  run full_fault_setting_s0 [.install, .fullContact, .fullWrite, .filterFull, .reviseApplication, .choose, .commit, .retain] = full_fault_setting_s8 := by decide

theorem full_fault_setting_core_trace :
  Generative.Trace process full_fault_setting_s0 [.install, .fullContact, .fullWrite, .filterFull, .reviseApplication, .choose, .commit, .retain] full_fault_setting_s8 := by
  rw [← full_fault_setting_saved_run]
  exact run_is_core_trace _ _

theorem full_fault_setting_final_whole_account :
  wholeTotal 8419342 full_fault_setting_s8 = 145 * RemainingDependency.ticks := by decide

def weak_fault_missing_config : Config := {fullFault := .faithful, weakFault := .missing, clamp := false}
def weak_fault_missing_s0 : State := {parent := parent_calibration_break, config := weak_fault_missing_config, body := {account := {fuel := 428018, start := 428018, spent := 0, live := 34, peak := 42, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := false, retained := false, mask := none, fullRecord := none, weakRecord := none, contact := none, application := .unobserved, diagnosis := .unobserved, proposal := none, activation := none, phase := .oldInterface}}
def weak_fault_missing_s1 : State := {parent := parent_calibration_break, config := weak_fault_missing_config, body := {account := {fuel := 311680, start := 428018, spent := 116338, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := false, mask := (some 65535), fullRecord := none, weakRecord := none, contact := none, application := .unobserved, diagnosis := .unobserved, proposal := none, activation := none, phase := .formed}}
def weak_fault_missing_s2 : State := {parent := parent_calibration_break, config := weak_fault_missing_config, body := {account := {fuel := 295236, start := 428018, spent := 132782, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := false, mask := (some 65535), fullRecord := none, weakRecord := none, contact := (some ⟨1, true, false⟩), application := .unobserved, diagnosis := .unobserved, proposal := none, activation := none, phase := .formed}}
def weak_fault_missing_s3 : State := {parent := parent_calibration_break, config := weak_fault_missing_config, body := {account := {fuel := 292044, start := 428018, spent := 135974, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := false, mask := (some 65535), fullRecord := (some ⟨1, true, false⟩), weakRecord := none, contact := none, application := .unobserved, diagnosis := .unobserved, proposal := none, activation := none, phase := .formed}}
def weak_fault_missing_s4 : State := {parent := parent_calibration_break, config := weak_fault_missing_config, body := {account := {fuel := 258256, start := 428018, spent := 169762, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := false, mask := (some 255), fullRecord := (some ⟨1, true, false⟩), weakRecord := none, contact := none, application := .unobserved, diagnosis := .unobserved, proposal := none, activation := none, phase := .formed}}
def weak_fault_missing_s5 : State := {parent := parent_calibration_break, config := weak_fault_missing_config, body := {account := {fuel := 255004, start := 428018, spent := 173014, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := false, mask := (some 255), fullRecord := (some ⟨1, true, false⟩), weakRecord := none, contact := none, application := .failed, diagnosis := .unobserved, proposal := none, activation := none, phase := .applicationRevised}}
def weak_fault_missing_s6 : State := {parent := parent_calibration_break, config := weak_fault_missing_config, body := {account := {fuel := 219199, start := 428018, spent := 208819, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := false, mask := (some 255), fullRecord := (some ⟨1, true, false⟩), weakRecord := none, contact := none, application := .failed, diagnosis := .unobserved, proposal := (some true), activation := none, phase := .applicationRevised}}
def weak_fault_missing_s7 : State := {parent := parent_calibration_break, config := weak_fault_missing_config, body := {account := {fuel := 217031, start := 428018, spent := 210987, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := false, mask := (some 255), fullRecord := (some ⟨1, true, false⟩), weakRecord := none, contact := none, application := .failed, diagnosis := .unobserved, proposal := (some true), activation := (some true), phase := .committed}}
def weak_fault_missing_s8 : State := {parent := parent_calibration_break, config := weak_fault_missing_config, body := {account := {fuel := 199503, start := 428018, spent := 228515, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := false, mask := (some 255), fullRecord := (some ⟨1, true, false⟩), weakRecord := none, contact := none, application := .failed, diagnosis := .unobserved, proposal := (some true), activation := (some true), phase := .committed}}
def weak_fault_missing_s9 : State := {parent := parent_calibration_break, config := weak_fault_missing_config, body := {account := {fuel := 181975, start := 428018, spent := 246043, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := (some ⟨1, true, true⟩), held := false, installed := true, retained := false, mask := (some 255), fullRecord := (some ⟨1, true, false⟩), weakRecord := none, contact := none, application := .failed, diagnosis := .unobserved, proposal := (some true), activation := (some true), phase := .committed}}
def weak_fault_missing_s10 : State := {parent := parent_calibration_break, config := weak_fault_missing_config, body := {account := {fuel := 165531, start := 428018, spent := 262487, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := false, mask := (some 255), fullRecord := (some ⟨1, true, false⟩), weakRecord := none, contact := none, application := .failed, diagnosis := .unobserved, proposal := (some true), activation := (some true), phase := .committed}}
def weak_fault_missing_s11 : State := {parent := parent_calibration_break, config := weak_fault_missing_config, body := {account := {fuel := 162339, start := 428018, spent := 265679, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := false, mask := (some 255), fullRecord := (some ⟨1, true, false⟩), weakRecord := none, contact := none, application := .failed, diagnosis := .unobserved, proposal := (some true), activation := (some true), phase := .committed}}
def weak_fault_missing_s12 : State := {parent := parent_calibration_break, config := weak_fault_missing_config, body := {account := {fuel := 128551, start := 428018, spent := 299467, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := false, mask := (some 255), fullRecord := (some ⟨1, true, false⟩), weakRecord := none, contact := none, application := .failed, diagnosis := .unobserved, proposal := (some true), activation := (some true), phase := .committed}}
def weak_fault_missing_s13 : State := {parent := parent_calibration_break, config := weak_fault_missing_config, body := {account := {fuel := 125299, start := 428018, spent := 302719, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := false, mask := (some 255), fullRecord := (some ⟨1, true, false⟩), weakRecord := none, contact := none, application := .failed, diagnosis := .unavailable, proposal := (some true), activation := (some true), phase := .diagnosisRevised}}
def weak_fault_missing_s14 : State := {parent := parent_calibration_break, config := weak_fault_missing_config, body := {account := {fuel := 64767, start := 428018, spent := 363251, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := true, mask := (some 255), fullRecord := (some ⟨1, true, false⟩), weakRecord := none, contact := none, application := .failed, diagnosis := .unavailable, proposal := (some true), activation := (some true), phase := .diagnosisRevised}}
theorem weak_fault_missing_actual_entrance :
  entrance parent_calibration_break weak_fault_missing_config = weak_fault_missing_s0 := by decide

theorem weak_fault_missing_initial_whole_account :
  wholeTotal 8419342 weak_fault_missing_s0 = 145 * RemainingDependency.ticks := by decide

theorem weak_fault_missing_event_1 :
  step weak_fault_missing_s0 .install = weak_fault_missing_s1 ∧ RemainingDependency.tariff weak_fault_missing_s0.body.account 24 58 8 65536 0 = 116338 ∧ (RemainingDependency.charge weak_fault_missing_s0.body.account 24 58 8 65536 0).2 = .none := by decide

theorem weak_fault_missing_event_2 :
  step weak_fault_missing_s1 .fullContact = weak_fault_missing_s2 ∧ RemainingDependency.tariff weak_fault_missing_s1.body.account 0 58 2 16384 0 = 16444 ∧ (RemainingDependency.charge weak_fault_missing_s1.body.account 0 58 2 16384 0).2 = .none := by decide

theorem weak_fault_missing_event_3 :
  step weak_fault_missing_s2 .fullWrite = weak_fault_missing_s3 ∧ RemainingDependency.tariff weak_fault_missing_s2.body.account 1 58 2 0 2 = 3192 ∧ (RemainingDependency.charge weak_fault_missing_s2.body.account 1 58 2 0 2).2 = .none := by decide

theorem weak_fault_missing_event_4 :
  step weak_fault_missing_s3 .filterFull = weak_fault_missing_s4 ∧ RemainingDependency.tariff weak_fault_missing_s3.body.account 16 58 2 0 16 = 33788 ∧ (RemainingDependency.charge weak_fault_missing_s3.body.account 16 58 2 0 16).2 = .none := by decide

theorem weak_fault_missing_event_5 :
  step weak_fault_missing_s4 .reviseApplication = weak_fault_missing_s5 ∧ RemainingDependency.tariff weak_fault_missing_s4.body.account 2 58 2 0 1 = 3252 ∧ (RemainingDependency.charge weak_fault_missing_s4.body.account 2 58 2 0 1).2 = .none := by decide

theorem weak_fault_missing_event_6 :
  step weak_fault_missing_s5 .choose = weak_fault_missing_s6 ∧ RemainingDependency.tariff weak_fault_missing_s5.body.account 32 58 3 0 1 = 35805 ∧ (RemainingDependency.charge weak_fault_missing_s5.body.account 32 58 3 0 1).2 = .none := by decide

theorem weak_fault_missing_event_7 :
  step weak_fault_missing_s6 .commit = weak_fault_missing_s7 ∧ RemainingDependency.tariff weak_fault_missing_s6.body.account 1 58 2 0 1 = 2168 ∧ (RemainingDependency.charge weak_fault_missing_s6.body.account 1 58 2 0 1).2 = .none := by decide

theorem weak_fault_missing_event_8 :
  step weak_fault_missing_s7 (.command true) = weak_fault_missing_s8 ∧ RemainingDependency.tariff weak_fault_missing_s7.body.account 1 58 2 16384 0 = 17528 ∧ (RemainingDependency.charge weak_fault_missing_s7.body.account 1 58 2 16384 0).2 = .none := by decide

theorem weak_fault_missing_event_9 :
  step weak_fault_missing_s8 .challenge = weak_fault_missing_s9 ∧ RemainingDependency.tariff weak_fault_missing_s8.body.account 1 58 2 16384 0 = 17528 ∧ (RemainingDependency.charge weak_fault_missing_s8.body.account 1 58 2 16384 0).2 = .none := by decide

theorem weak_fault_missing_event_10 :
  step weak_fault_missing_s9 .weakContact = weak_fault_missing_s10 ∧ RemainingDependency.tariff weak_fault_missing_s9.body.account 0 58 2 16384 0 = 16444 ∧ (RemainingDependency.charge weak_fault_missing_s9.body.account 0 58 2 16384 0).2 = .none := by decide

theorem weak_fault_missing_event_11 :
  step weak_fault_missing_s10 .weakWrite = weak_fault_missing_s11 ∧ RemainingDependency.tariff weak_fault_missing_s10.body.account 1 58 2 0 2 = 3192 ∧ (RemainingDependency.charge weak_fault_missing_s10.body.account 1 58 2 0 2).2 = .none := by decide

theorem weak_fault_missing_event_12 :
  step weak_fault_missing_s11 .filterWeak = weak_fault_missing_s12 ∧ RemainingDependency.tariff weak_fault_missing_s11.body.account 16 58 2 0 16 = 33788 ∧ (RemainingDependency.charge weak_fault_missing_s11.body.account 16 58 2 0 16).2 = .none := by decide

theorem weak_fault_missing_event_13 :
  step weak_fault_missing_s12 .reviseDiagnosis = weak_fault_missing_s13 ∧ RemainingDependency.tariff weak_fault_missing_s12.body.account 2 58 2 0 1 = 3252 ∧ (RemainingDependency.charge weak_fault_missing_s12.body.account 2 58 2 0 1).2 = .none := by decide

theorem weak_fault_missing_event_14 :
  step weak_fault_missing_s13 .retain = weak_fault_missing_s14 ∧ RemainingDependency.tariff weak_fault_missing_s13.body.account 1 58 0 59392 0 = 60532 ∧ (RemainingDependency.charge weak_fault_missing_s13.body.account 1 58 0 59392 0).2 = .none := by decide

theorem weak_fault_missing_saved_run :
  run weak_fault_missing_s0 [.install, .fullContact, .fullWrite, .filterFull, .reviseApplication, .choose, .commit, (.command true), .challenge, .weakContact, .weakWrite, .filterWeak, .reviseDiagnosis, .retain] = weak_fault_missing_s14 := by decide

theorem weak_fault_missing_core_trace :
  Generative.Trace process weak_fault_missing_s0 [.install, .fullContact, .fullWrite, .filterFull, .reviseApplication, .choose, .commit, (.command true), .challenge, .weakContact, .weakWrite, .filterWeak, .reviseDiagnosis, .retain] weak_fault_missing_s14 := by
  rw [← weak_fault_missing_saved_run]
  exact run_is_core_trace _ _

theorem weak_fault_missing_final_whole_account :
  wholeTotal 8419342 weak_fault_missing_s14 = 145 * RemainingDependency.ticks := by decide

def weak_fault_flip_config : Config := {fullFault := .faithful, weakFault := .flip, clamp := false}
def weak_fault_flip_s0 : State := {parent := parent_calibration_break, config := weak_fault_flip_config, body := {account := {fuel := 428018, start := 428018, spent := 0, live := 34, peak := 42, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := false, retained := false, mask := none, fullRecord := none, weakRecord := none, contact := none, application := .unobserved, diagnosis := .unobserved, proposal := none, activation := none, phase := .oldInterface}}
def weak_fault_flip_s1 : State := {parent := parent_calibration_break, config := weak_fault_flip_config, body := {account := {fuel := 311680, start := 428018, spent := 116338, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := false, mask := (some 65535), fullRecord := none, weakRecord := none, contact := none, application := .unobserved, diagnosis := .unobserved, proposal := none, activation := none, phase := .formed}}
def weak_fault_flip_s2 : State := {parent := parent_calibration_break, config := weak_fault_flip_config, body := {account := {fuel := 295236, start := 428018, spent := 132782, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := false, mask := (some 65535), fullRecord := none, weakRecord := none, contact := (some ⟨1, true, false⟩), application := .unobserved, diagnosis := .unobserved, proposal := none, activation := none, phase := .formed}}
def weak_fault_flip_s3 : State := {parent := parent_calibration_break, config := weak_fault_flip_config, body := {account := {fuel := 292044, start := 428018, spent := 135974, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := false, mask := (some 65535), fullRecord := (some ⟨1, true, false⟩), weakRecord := none, contact := none, application := .unobserved, diagnosis := .unobserved, proposal := none, activation := none, phase := .formed}}
def weak_fault_flip_s4 : State := {parent := parent_calibration_break, config := weak_fault_flip_config, body := {account := {fuel := 258256, start := 428018, spent := 169762, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := false, mask := (some 255), fullRecord := (some ⟨1, true, false⟩), weakRecord := none, contact := none, application := .unobserved, diagnosis := .unobserved, proposal := none, activation := none, phase := .formed}}
def weak_fault_flip_s5 : State := {parent := parent_calibration_break, config := weak_fault_flip_config, body := {account := {fuel := 255004, start := 428018, spent := 173014, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := false, mask := (some 255), fullRecord := (some ⟨1, true, false⟩), weakRecord := none, contact := none, application := .failed, diagnosis := .unobserved, proposal := none, activation := none, phase := .applicationRevised}}
def weak_fault_flip_s6 : State := {parent := parent_calibration_break, config := weak_fault_flip_config, body := {account := {fuel := 219199, start := 428018, spent := 208819, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := false, mask := (some 255), fullRecord := (some ⟨1, true, false⟩), weakRecord := none, contact := none, application := .failed, diagnosis := .unobserved, proposal := (some true), activation := none, phase := .applicationRevised}}
def weak_fault_flip_s7 : State := {parent := parent_calibration_break, config := weak_fault_flip_config, body := {account := {fuel := 217031, start := 428018, spent := 210987, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := false, mask := (some 255), fullRecord := (some ⟨1, true, false⟩), weakRecord := none, contact := none, application := .failed, diagnosis := .unobserved, proposal := (some true), activation := (some true), phase := .committed}}
def weak_fault_flip_s8 : State := {parent := parent_calibration_break, config := weak_fault_flip_config, body := {account := {fuel := 199503, start := 428018, spent := 228515, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := false, mask := (some 255), fullRecord := (some ⟨1, true, false⟩), weakRecord := none, contact := none, application := .failed, diagnosis := .unobserved, proposal := (some true), activation := (some true), phase := .committed}}
def weak_fault_flip_s9 : State := {parent := parent_calibration_break, config := weak_fault_flip_config, body := {account := {fuel := 181975, start := 428018, spent := 246043, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := (some ⟨1, true, true⟩), held := false, installed := true, retained := false, mask := (some 255), fullRecord := (some ⟨1, true, false⟩), weakRecord := none, contact := none, application := .failed, diagnosis := .unobserved, proposal := (some true), activation := (some true), phase := .committed}}
def weak_fault_flip_s10 : State := {parent := parent_calibration_break, config := weak_fault_flip_config, body := {account := {fuel := 165531, start := 428018, spent := 262487, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := false, mask := (some 255), fullRecord := (some ⟨1, true, false⟩), weakRecord := none, contact := (some ⟨1, true, false⟩), application := .failed, diagnosis := .unobserved, proposal := (some true), activation := (some true), phase := .committed}}
def weak_fault_flip_s11 : State := {parent := parent_calibration_break, config := weak_fault_flip_config, body := {account := {fuel := 162339, start := 428018, spent := 265679, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := false, mask := (some 255), fullRecord := (some ⟨1, true, false⟩), weakRecord := (some ⟨1, true, false⟩), contact := none, application := .failed, diagnosis := .unobserved, proposal := (some true), activation := (some true), phase := .committed}}
def weak_fault_flip_s12 : State := {parent := parent_calibration_break, config := weak_fault_flip_config, body := {account := {fuel := 128551, start := 428018, spent := 299467, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := false, mask := (some 51), fullRecord := (some ⟨1, true, false⟩), weakRecord := (some ⟨1, true, false⟩), contact := none, application := .failed, diagnosis := .unobserved, proposal := (some true), activation := (some true), phase := .committed}}
def weak_fault_flip_s13 : State := {parent := parent_calibration_break, config := weak_fault_flip_config, body := {account := {fuel := 125299, start := 428018, spent := 302719, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := false, mask := (some 51), fullRecord := (some ⟨1, true, false⟩), weakRecord := (some ⟨1, true, false⟩), contact := none, application := .failed, diagnosis := .oldContradicted, proposal := (some true), activation := (some true), phase := .diagnosisRevised}}
def weak_fault_flip_s14 : State := {parent := parent_calibration_break, config := weak_fault_flip_config, body := {account := {fuel := 64767, start := 428018, spent := 363251, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := true, mask := (some 51), fullRecord := (some ⟨1, true, false⟩), weakRecord := (some ⟨1, true, false⟩), contact := none, application := .failed, diagnosis := .oldContradicted, proposal := (some true), activation := (some true), phase := .diagnosisRevised}}
theorem weak_fault_flip_actual_entrance :
  entrance parent_calibration_break weak_fault_flip_config = weak_fault_flip_s0 := by decide

theorem weak_fault_flip_initial_whole_account :
  wholeTotal 8419342 weak_fault_flip_s0 = 145 * RemainingDependency.ticks := by decide

theorem weak_fault_flip_event_1 :
  step weak_fault_flip_s0 .install = weak_fault_flip_s1 ∧ RemainingDependency.tariff weak_fault_flip_s0.body.account 24 58 8 65536 0 = 116338 ∧ (RemainingDependency.charge weak_fault_flip_s0.body.account 24 58 8 65536 0).2 = .none := by decide

theorem weak_fault_flip_event_2 :
  step weak_fault_flip_s1 .fullContact = weak_fault_flip_s2 ∧ RemainingDependency.tariff weak_fault_flip_s1.body.account 0 58 2 16384 0 = 16444 ∧ (RemainingDependency.charge weak_fault_flip_s1.body.account 0 58 2 16384 0).2 = .none := by decide

theorem weak_fault_flip_event_3 :
  step weak_fault_flip_s2 .fullWrite = weak_fault_flip_s3 ∧ RemainingDependency.tariff weak_fault_flip_s2.body.account 1 58 2 0 2 = 3192 ∧ (RemainingDependency.charge weak_fault_flip_s2.body.account 1 58 2 0 2).2 = .none := by decide

theorem weak_fault_flip_event_4 :
  step weak_fault_flip_s3 .filterFull = weak_fault_flip_s4 ∧ RemainingDependency.tariff weak_fault_flip_s3.body.account 16 58 2 0 16 = 33788 ∧ (RemainingDependency.charge weak_fault_flip_s3.body.account 16 58 2 0 16).2 = .none := by decide

theorem weak_fault_flip_event_5 :
  step weak_fault_flip_s4 .reviseApplication = weak_fault_flip_s5 ∧ RemainingDependency.tariff weak_fault_flip_s4.body.account 2 58 2 0 1 = 3252 ∧ (RemainingDependency.charge weak_fault_flip_s4.body.account 2 58 2 0 1).2 = .none := by decide

theorem weak_fault_flip_event_6 :
  step weak_fault_flip_s5 .choose = weak_fault_flip_s6 ∧ RemainingDependency.tariff weak_fault_flip_s5.body.account 32 58 3 0 1 = 35805 ∧ (RemainingDependency.charge weak_fault_flip_s5.body.account 32 58 3 0 1).2 = .none := by decide

theorem weak_fault_flip_event_7 :
  step weak_fault_flip_s6 .commit = weak_fault_flip_s7 ∧ RemainingDependency.tariff weak_fault_flip_s6.body.account 1 58 2 0 1 = 2168 ∧ (RemainingDependency.charge weak_fault_flip_s6.body.account 1 58 2 0 1).2 = .none := by decide

theorem weak_fault_flip_event_8 :
  step weak_fault_flip_s7 (.command true) = weak_fault_flip_s8 ∧ RemainingDependency.tariff weak_fault_flip_s7.body.account 1 58 2 16384 0 = 17528 ∧ (RemainingDependency.charge weak_fault_flip_s7.body.account 1 58 2 16384 0).2 = .none := by decide

theorem weak_fault_flip_event_9 :
  step weak_fault_flip_s8 .challenge = weak_fault_flip_s9 ∧ RemainingDependency.tariff weak_fault_flip_s8.body.account 1 58 2 16384 0 = 17528 ∧ (RemainingDependency.charge weak_fault_flip_s8.body.account 1 58 2 16384 0).2 = .none := by decide

theorem weak_fault_flip_event_10 :
  step weak_fault_flip_s9 .weakContact = weak_fault_flip_s10 ∧ RemainingDependency.tariff weak_fault_flip_s9.body.account 0 58 2 16384 0 = 16444 ∧ (RemainingDependency.charge weak_fault_flip_s9.body.account 0 58 2 16384 0).2 = .none := by decide

theorem weak_fault_flip_event_11 :
  step weak_fault_flip_s10 .weakWrite = weak_fault_flip_s11 ∧ RemainingDependency.tariff weak_fault_flip_s10.body.account 1 58 2 0 2 = 3192 ∧ (RemainingDependency.charge weak_fault_flip_s10.body.account 1 58 2 0 2).2 = .none := by decide

theorem weak_fault_flip_event_12 :
  step weak_fault_flip_s11 .filterWeak = weak_fault_flip_s12 ∧ RemainingDependency.tariff weak_fault_flip_s11.body.account 16 58 2 0 16 = 33788 ∧ (RemainingDependency.charge weak_fault_flip_s11.body.account 16 58 2 0 16).2 = .none := by decide

theorem weak_fault_flip_event_13 :
  step weak_fault_flip_s12 .reviseDiagnosis = weak_fault_flip_s13 ∧ RemainingDependency.tariff weak_fault_flip_s12.body.account 2 58 2 0 1 = 3252 ∧ (RemainingDependency.charge weak_fault_flip_s12.body.account 2 58 2 0 1).2 = .none := by decide

theorem weak_fault_flip_event_14 :
  step weak_fault_flip_s13 .retain = weak_fault_flip_s14 ∧ RemainingDependency.tariff weak_fault_flip_s13.body.account 1 58 0 59392 0 = 60532 ∧ (RemainingDependency.charge weak_fault_flip_s13.body.account 1 58 0 59392 0).2 = .none := by decide

theorem weak_fault_flip_saved_run :
  run weak_fault_flip_s0 [.install, .fullContact, .fullWrite, .filterFull, .reviseApplication, .choose, .commit, (.command true), .challenge, .weakContact, .weakWrite, .filterWeak, .reviseDiagnosis, .retain] = weak_fault_flip_s14 := by decide

theorem weak_fault_flip_core_trace :
  Generative.Trace process weak_fault_flip_s0 [.install, .fullContact, .fullWrite, .filterFull, .reviseApplication, .choose, .commit, (.command true), .challenge, .weakContact, .weakWrite, .filterWeak, .reviseDiagnosis, .retain] weak_fault_flip_s14 := by
  rw [← weak_fault_flip_saved_run]
  exact run_is_core_trace _ _

theorem weak_fault_flip_final_whole_account :
  wholeTotal 8419342 weak_fault_flip_s14 = 145 * RemainingDependency.ticks := by decide

def weak_fault_context_config : Config := {fullFault := .faithful, weakFault := .wrongContext, clamp := false}
def weak_fault_context_s0 : State := {parent := parent_calibration_break, config := weak_fault_context_config, body := {account := {fuel := 428018, start := 428018, spent := 0, live := 34, peak := 42, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := false, retained := false, mask := none, fullRecord := none, weakRecord := none, contact := none, application := .unobserved, diagnosis := .unobserved, proposal := none, activation := none, phase := .oldInterface}}
def weak_fault_context_s1 : State := {parent := parent_calibration_break, config := weak_fault_context_config, body := {account := {fuel := 311680, start := 428018, spent := 116338, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := false, mask := (some 65535), fullRecord := none, weakRecord := none, contact := none, application := .unobserved, diagnosis := .unobserved, proposal := none, activation := none, phase := .formed}}
def weak_fault_context_s2 : State := {parent := parent_calibration_break, config := weak_fault_context_config, body := {account := {fuel := 295236, start := 428018, spent := 132782, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := false, mask := (some 65535), fullRecord := none, weakRecord := none, contact := (some ⟨1, true, false⟩), application := .unobserved, diagnosis := .unobserved, proposal := none, activation := none, phase := .formed}}
def weak_fault_context_s3 : State := {parent := parent_calibration_break, config := weak_fault_context_config, body := {account := {fuel := 292044, start := 428018, spent := 135974, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := false, mask := (some 65535), fullRecord := (some ⟨1, true, false⟩), weakRecord := none, contact := none, application := .unobserved, diagnosis := .unobserved, proposal := none, activation := none, phase := .formed}}
def weak_fault_context_s4 : State := {parent := parent_calibration_break, config := weak_fault_context_config, body := {account := {fuel := 258256, start := 428018, spent := 169762, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := false, mask := (some 255), fullRecord := (some ⟨1, true, false⟩), weakRecord := none, contact := none, application := .unobserved, diagnosis := .unobserved, proposal := none, activation := none, phase := .formed}}
def weak_fault_context_s5 : State := {parent := parent_calibration_break, config := weak_fault_context_config, body := {account := {fuel := 255004, start := 428018, spent := 173014, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := false, mask := (some 255), fullRecord := (some ⟨1, true, false⟩), weakRecord := none, contact := none, application := .failed, diagnosis := .unobserved, proposal := none, activation := none, phase := .applicationRevised}}
def weak_fault_context_s6 : State := {parent := parent_calibration_break, config := weak_fault_context_config, body := {account := {fuel := 219199, start := 428018, spent := 208819, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := false, mask := (some 255), fullRecord := (some ⟨1, true, false⟩), weakRecord := none, contact := none, application := .failed, diagnosis := .unobserved, proposal := (some true), activation := none, phase := .applicationRevised}}
def weak_fault_context_s7 : State := {parent := parent_calibration_break, config := weak_fault_context_config, body := {account := {fuel := 217031, start := 428018, spent := 210987, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := false, mask := (some 255), fullRecord := (some ⟨1, true, false⟩), weakRecord := none, contact := none, application := .failed, diagnosis := .unobserved, proposal := (some true), activation := (some true), phase := .committed}}
def weak_fault_context_s8 : State := {parent := parent_calibration_break, config := weak_fault_context_config, body := {account := {fuel := 199503, start := 428018, spent := 228515, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := false, mask := (some 255), fullRecord := (some ⟨1, true, false⟩), weakRecord := none, contact := none, application := .failed, diagnosis := .unobserved, proposal := (some true), activation := (some true), phase := .committed}}
def weak_fault_context_s9 : State := {parent := parent_calibration_break, config := weak_fault_context_config, body := {account := {fuel := 181975, start := 428018, spent := 246043, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := (some ⟨1, true, true⟩), held := false, installed := true, retained := false, mask := (some 255), fullRecord := (some ⟨1, true, false⟩), weakRecord := none, contact := none, application := .failed, diagnosis := .unobserved, proposal := (some true), activation := (some true), phase := .committed}}
def weak_fault_context_s10 : State := {parent := parent_calibration_break, config := weak_fault_context_config, body := {account := {fuel := 165531, start := 428018, spent := 262487, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := false, mask := (some 255), fullRecord := (some ⟨1, true, false⟩), weakRecord := none, contact := (some ⟨2, true, true⟩), application := .failed, diagnosis := .unobserved, proposal := (some true), activation := (some true), phase := .committed}}
def weak_fault_context_s11 : State := {parent := parent_calibration_break, config := weak_fault_context_config, body := {account := {fuel := 162339, start := 428018, spent := 265679, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := false, mask := (some 255), fullRecord := (some ⟨1, true, false⟩), weakRecord := none, contact := none, application := .failed, diagnosis := .unobserved, proposal := (some true), activation := (some true), phase := .committed}}
def weak_fault_context_s12 : State := {parent := parent_calibration_break, config := weak_fault_context_config, body := {account := {fuel := 128551, start := 428018, spent := 299467, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := false, mask := (some 255), fullRecord := (some ⟨1, true, false⟩), weakRecord := none, contact := none, application := .failed, diagnosis := .unobserved, proposal := (some true), activation := (some true), phase := .committed}}
def weak_fault_context_s13 : State := {parent := parent_calibration_break, config := weak_fault_context_config, body := {account := {fuel := 125299, start := 428018, spent := 302719, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := false, mask := (some 255), fullRecord := (some ⟨1, true, false⟩), weakRecord := none, contact := none, application := .failed, diagnosis := .unavailable, proposal := (some true), activation := (some true), phase := .diagnosisRevised}}
def weak_fault_context_s14 : State := {parent := parent_calibration_break, config := weak_fault_context_config, body := {account := {fuel := 64767, start := 428018, spent := 363251, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := true, mask := (some 255), fullRecord := (some ⟨1, true, false⟩), weakRecord := none, contact := none, application := .failed, diagnosis := .unavailable, proposal := (some true), activation := (some true), phase := .diagnosisRevised}}
theorem weak_fault_context_actual_entrance :
  entrance parent_calibration_break weak_fault_context_config = weak_fault_context_s0 := by decide

theorem weak_fault_context_initial_whole_account :
  wholeTotal 8419342 weak_fault_context_s0 = 145 * RemainingDependency.ticks := by decide

theorem weak_fault_context_event_1 :
  step weak_fault_context_s0 .install = weak_fault_context_s1 ∧ RemainingDependency.tariff weak_fault_context_s0.body.account 24 58 8 65536 0 = 116338 ∧ (RemainingDependency.charge weak_fault_context_s0.body.account 24 58 8 65536 0).2 = .none := by decide

theorem weak_fault_context_event_2 :
  step weak_fault_context_s1 .fullContact = weak_fault_context_s2 ∧ RemainingDependency.tariff weak_fault_context_s1.body.account 0 58 2 16384 0 = 16444 ∧ (RemainingDependency.charge weak_fault_context_s1.body.account 0 58 2 16384 0).2 = .none := by decide

theorem weak_fault_context_event_3 :
  step weak_fault_context_s2 .fullWrite = weak_fault_context_s3 ∧ RemainingDependency.tariff weak_fault_context_s2.body.account 1 58 2 0 2 = 3192 ∧ (RemainingDependency.charge weak_fault_context_s2.body.account 1 58 2 0 2).2 = .none := by decide

theorem weak_fault_context_event_4 :
  step weak_fault_context_s3 .filterFull = weak_fault_context_s4 ∧ RemainingDependency.tariff weak_fault_context_s3.body.account 16 58 2 0 16 = 33788 ∧ (RemainingDependency.charge weak_fault_context_s3.body.account 16 58 2 0 16).2 = .none := by decide

theorem weak_fault_context_event_5 :
  step weak_fault_context_s4 .reviseApplication = weak_fault_context_s5 ∧ RemainingDependency.tariff weak_fault_context_s4.body.account 2 58 2 0 1 = 3252 ∧ (RemainingDependency.charge weak_fault_context_s4.body.account 2 58 2 0 1).2 = .none := by decide

theorem weak_fault_context_event_6 :
  step weak_fault_context_s5 .choose = weak_fault_context_s6 ∧ RemainingDependency.tariff weak_fault_context_s5.body.account 32 58 3 0 1 = 35805 ∧ (RemainingDependency.charge weak_fault_context_s5.body.account 32 58 3 0 1).2 = .none := by decide

theorem weak_fault_context_event_7 :
  step weak_fault_context_s6 .commit = weak_fault_context_s7 ∧ RemainingDependency.tariff weak_fault_context_s6.body.account 1 58 2 0 1 = 2168 ∧ (RemainingDependency.charge weak_fault_context_s6.body.account 1 58 2 0 1).2 = .none := by decide

theorem weak_fault_context_event_8 :
  step weak_fault_context_s7 (.command true) = weak_fault_context_s8 ∧ RemainingDependency.tariff weak_fault_context_s7.body.account 1 58 2 16384 0 = 17528 ∧ (RemainingDependency.charge weak_fault_context_s7.body.account 1 58 2 16384 0).2 = .none := by decide

theorem weak_fault_context_event_9 :
  step weak_fault_context_s8 .challenge = weak_fault_context_s9 ∧ RemainingDependency.tariff weak_fault_context_s8.body.account 1 58 2 16384 0 = 17528 ∧ (RemainingDependency.charge weak_fault_context_s8.body.account 1 58 2 16384 0).2 = .none := by decide

theorem weak_fault_context_event_10 :
  step weak_fault_context_s9 .weakContact = weak_fault_context_s10 ∧ RemainingDependency.tariff weak_fault_context_s9.body.account 0 58 2 16384 0 = 16444 ∧ (RemainingDependency.charge weak_fault_context_s9.body.account 0 58 2 16384 0).2 = .none := by decide

theorem weak_fault_context_event_11 :
  step weak_fault_context_s10 .weakWrite = weak_fault_context_s11 ∧ RemainingDependency.tariff weak_fault_context_s10.body.account 1 58 2 0 2 = 3192 ∧ (RemainingDependency.charge weak_fault_context_s10.body.account 1 58 2 0 2).2 = .none := by decide

theorem weak_fault_context_event_12 :
  step weak_fault_context_s11 .filterWeak = weak_fault_context_s12 ∧ RemainingDependency.tariff weak_fault_context_s11.body.account 16 58 2 0 16 = 33788 ∧ (RemainingDependency.charge weak_fault_context_s11.body.account 16 58 2 0 16).2 = .none := by decide

theorem weak_fault_context_event_13 :
  step weak_fault_context_s12 .reviseDiagnosis = weak_fault_context_s13 ∧ RemainingDependency.tariff weak_fault_context_s12.body.account 2 58 2 0 1 = 3252 ∧ (RemainingDependency.charge weak_fault_context_s12.body.account 2 58 2 0 1).2 = .none := by decide

theorem weak_fault_context_event_14 :
  step weak_fault_context_s13 .retain = weak_fault_context_s14 ∧ RemainingDependency.tariff weak_fault_context_s13.body.account 1 58 0 59392 0 = 60532 ∧ (RemainingDependency.charge weak_fault_context_s13.body.account 1 58 0 59392 0).2 = .none := by decide

theorem weak_fault_context_saved_run :
  run weak_fault_context_s0 [.install, .fullContact, .fullWrite, .filterFull, .reviseApplication, .choose, .commit, (.command true), .challenge, .weakContact, .weakWrite, .filterWeak, .reviseDiagnosis, .retain] = weak_fault_context_s14 := by decide

theorem weak_fault_context_core_trace :
  Generative.Trace process weak_fault_context_s0 [.install, .fullContact, .fullWrite, .filterFull, .reviseApplication, .choose, .commit, (.command true), .challenge, .weakContact, .weakWrite, .filterWeak, .reviseDiagnosis, .retain] weak_fault_context_s14 := by
  rw [← weak_fault_context_saved_run]
  exact run_is_core_trace _ _

theorem weak_fault_context_final_whole_account :
  wholeTotal 8419342 weak_fault_context_s14 = 145 * RemainingDependency.ticks := by decide

def weak_fault_setting_config : Config := {fullFault := .faithful, weakFault := .wrongSetting, clamp := false}
def weak_fault_setting_s0 : State := {parent := parent_calibration_break, config := weak_fault_setting_config, body := {account := {fuel := 428018, start := 428018, spent := 0, live := 34, peak := 42, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := false, retained := false, mask := none, fullRecord := none, weakRecord := none, contact := none, application := .unobserved, diagnosis := .unobserved, proposal := none, activation := none, phase := .oldInterface}}
def weak_fault_setting_s1 : State := {parent := parent_calibration_break, config := weak_fault_setting_config, body := {account := {fuel := 311680, start := 428018, spent := 116338, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := false, mask := (some 65535), fullRecord := none, weakRecord := none, contact := none, application := .unobserved, diagnosis := .unobserved, proposal := none, activation := none, phase := .formed}}
def weak_fault_setting_s2 : State := {parent := parent_calibration_break, config := weak_fault_setting_config, body := {account := {fuel := 295236, start := 428018, spent := 132782, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := false, mask := (some 65535), fullRecord := none, weakRecord := none, contact := (some ⟨1, true, false⟩), application := .unobserved, diagnosis := .unobserved, proposal := none, activation := none, phase := .formed}}
def weak_fault_setting_s3 : State := {parent := parent_calibration_break, config := weak_fault_setting_config, body := {account := {fuel := 292044, start := 428018, spent := 135974, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := false, mask := (some 65535), fullRecord := (some ⟨1, true, false⟩), weakRecord := none, contact := none, application := .unobserved, diagnosis := .unobserved, proposal := none, activation := none, phase := .formed}}
def weak_fault_setting_s4 : State := {parent := parent_calibration_break, config := weak_fault_setting_config, body := {account := {fuel := 258256, start := 428018, spent := 169762, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := false, mask := (some 255), fullRecord := (some ⟨1, true, false⟩), weakRecord := none, contact := none, application := .unobserved, diagnosis := .unobserved, proposal := none, activation := none, phase := .formed}}
def weak_fault_setting_s5 : State := {parent := parent_calibration_break, config := weak_fault_setting_config, body := {account := {fuel := 255004, start := 428018, spent := 173014, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := false, mask := (some 255), fullRecord := (some ⟨1, true, false⟩), weakRecord := none, contact := none, application := .failed, diagnosis := .unobserved, proposal := none, activation := none, phase := .applicationRevised}}
def weak_fault_setting_s6 : State := {parent := parent_calibration_break, config := weak_fault_setting_config, body := {account := {fuel := 219199, start := 428018, spent := 208819, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := false, mask := (some 255), fullRecord := (some ⟨1, true, false⟩), weakRecord := none, contact := none, application := .failed, diagnosis := .unobserved, proposal := (some true), activation := none, phase := .applicationRevised}}
def weak_fault_setting_s7 : State := {parent := parent_calibration_break, config := weak_fault_setting_config, body := {account := {fuel := 217031, start := 428018, spent := 210987, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := false, mask := (some 255), fullRecord := (some ⟨1, true, false⟩), weakRecord := none, contact := none, application := .failed, diagnosis := .unobserved, proposal := (some true), activation := (some true), phase := .committed}}
def weak_fault_setting_s8 : State := {parent := parent_calibration_break, config := weak_fault_setting_config, body := {account := {fuel := 199503, start := 428018, spent := 228515, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := false, mask := (some 255), fullRecord := (some ⟨1, true, false⟩), weakRecord := none, contact := none, application := .failed, diagnosis := .unobserved, proposal := (some true), activation := (some true), phase := .committed}}
def weak_fault_setting_s9 : State := {parent := parent_calibration_break, config := weak_fault_setting_config, body := {account := {fuel := 181975, start := 428018, spent := 246043, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := (some ⟨1, true, true⟩), held := false, installed := true, retained := false, mask := (some 255), fullRecord := (some ⟨1, true, false⟩), weakRecord := none, contact := none, application := .failed, diagnosis := .unobserved, proposal := (some true), activation := (some true), phase := .committed}}
def weak_fault_setting_s10 : State := {parent := parent_calibration_break, config := weak_fault_setting_config, body := {account := {fuel := 165531, start := 428018, spent := 262487, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := false, mask := (some 255), fullRecord := (some ⟨1, true, false⟩), weakRecord := none, contact := (some ⟨1, false, true⟩), application := .failed, diagnosis := .unobserved, proposal := (some true), activation := (some true), phase := .committed}}
def weak_fault_setting_s11 : State := {parent := parent_calibration_break, config := weak_fault_setting_config, body := {account := {fuel := 162339, start := 428018, spent := 265679, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := false, mask := (some 255), fullRecord := (some ⟨1, true, false⟩), weakRecord := none, contact := none, application := .failed, diagnosis := .unobserved, proposal := (some true), activation := (some true), phase := .committed}}
def weak_fault_setting_s12 : State := {parent := parent_calibration_break, config := weak_fault_setting_config, body := {account := {fuel := 128551, start := 428018, spent := 299467, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := false, mask := (some 255), fullRecord := (some ⟨1, true, false⟩), weakRecord := none, contact := none, application := .failed, diagnosis := .unobserved, proposal := (some true), activation := (some true), phase := .committed}}
def weak_fault_setting_s13 : State := {parent := parent_calibration_break, config := weak_fault_setting_config, body := {account := {fuel := 125299, start := 428018, spent := 302719, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := false, mask := (some 255), fullRecord := (some ⟨1, true, false⟩), weakRecord := none, contact := none, application := .failed, diagnosis := .unavailable, proposal := (some true), activation := (some true), phase := .diagnosisRevised}}
def weak_fault_setting_s14 : State := {parent := parent_calibration_break, config := weak_fault_setting_config, body := {account := {fuel := 64767, start := 428018, spent := 363251, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := true, mask := (some 255), fullRecord := (some ⟨1, true, false⟩), weakRecord := none, contact := none, application := .failed, diagnosis := .unavailable, proposal := (some true), activation := (some true), phase := .diagnosisRevised}}
theorem weak_fault_setting_actual_entrance :
  entrance parent_calibration_break weak_fault_setting_config = weak_fault_setting_s0 := by decide

theorem weak_fault_setting_initial_whole_account :
  wholeTotal 8419342 weak_fault_setting_s0 = 145 * RemainingDependency.ticks := by decide

theorem weak_fault_setting_event_1 :
  step weak_fault_setting_s0 .install = weak_fault_setting_s1 ∧ RemainingDependency.tariff weak_fault_setting_s0.body.account 24 58 8 65536 0 = 116338 ∧ (RemainingDependency.charge weak_fault_setting_s0.body.account 24 58 8 65536 0).2 = .none := by decide

theorem weak_fault_setting_event_2 :
  step weak_fault_setting_s1 .fullContact = weak_fault_setting_s2 ∧ RemainingDependency.tariff weak_fault_setting_s1.body.account 0 58 2 16384 0 = 16444 ∧ (RemainingDependency.charge weak_fault_setting_s1.body.account 0 58 2 16384 0).2 = .none := by decide

theorem weak_fault_setting_event_3 :
  step weak_fault_setting_s2 .fullWrite = weak_fault_setting_s3 ∧ RemainingDependency.tariff weak_fault_setting_s2.body.account 1 58 2 0 2 = 3192 ∧ (RemainingDependency.charge weak_fault_setting_s2.body.account 1 58 2 0 2).2 = .none := by decide

theorem weak_fault_setting_event_4 :
  step weak_fault_setting_s3 .filterFull = weak_fault_setting_s4 ∧ RemainingDependency.tariff weak_fault_setting_s3.body.account 16 58 2 0 16 = 33788 ∧ (RemainingDependency.charge weak_fault_setting_s3.body.account 16 58 2 0 16).2 = .none := by decide

theorem weak_fault_setting_event_5 :
  step weak_fault_setting_s4 .reviseApplication = weak_fault_setting_s5 ∧ RemainingDependency.tariff weak_fault_setting_s4.body.account 2 58 2 0 1 = 3252 ∧ (RemainingDependency.charge weak_fault_setting_s4.body.account 2 58 2 0 1).2 = .none := by decide

theorem weak_fault_setting_event_6 :
  step weak_fault_setting_s5 .choose = weak_fault_setting_s6 ∧ RemainingDependency.tariff weak_fault_setting_s5.body.account 32 58 3 0 1 = 35805 ∧ (RemainingDependency.charge weak_fault_setting_s5.body.account 32 58 3 0 1).2 = .none := by decide

theorem weak_fault_setting_event_7 :
  step weak_fault_setting_s6 .commit = weak_fault_setting_s7 ∧ RemainingDependency.tariff weak_fault_setting_s6.body.account 1 58 2 0 1 = 2168 ∧ (RemainingDependency.charge weak_fault_setting_s6.body.account 1 58 2 0 1).2 = .none := by decide

theorem weak_fault_setting_event_8 :
  step weak_fault_setting_s7 (.command true) = weak_fault_setting_s8 ∧ RemainingDependency.tariff weak_fault_setting_s7.body.account 1 58 2 16384 0 = 17528 ∧ (RemainingDependency.charge weak_fault_setting_s7.body.account 1 58 2 16384 0).2 = .none := by decide

theorem weak_fault_setting_event_9 :
  step weak_fault_setting_s8 .challenge = weak_fault_setting_s9 ∧ RemainingDependency.tariff weak_fault_setting_s8.body.account 1 58 2 16384 0 = 17528 ∧ (RemainingDependency.charge weak_fault_setting_s8.body.account 1 58 2 16384 0).2 = .none := by decide

theorem weak_fault_setting_event_10 :
  step weak_fault_setting_s9 .weakContact = weak_fault_setting_s10 ∧ RemainingDependency.tariff weak_fault_setting_s9.body.account 0 58 2 16384 0 = 16444 ∧ (RemainingDependency.charge weak_fault_setting_s9.body.account 0 58 2 16384 0).2 = .none := by decide

theorem weak_fault_setting_event_11 :
  step weak_fault_setting_s10 .weakWrite = weak_fault_setting_s11 ∧ RemainingDependency.tariff weak_fault_setting_s10.body.account 1 58 2 0 2 = 3192 ∧ (RemainingDependency.charge weak_fault_setting_s10.body.account 1 58 2 0 2).2 = .none := by decide

theorem weak_fault_setting_event_12 :
  step weak_fault_setting_s11 .filterWeak = weak_fault_setting_s12 ∧ RemainingDependency.tariff weak_fault_setting_s11.body.account 16 58 2 0 16 = 33788 ∧ (RemainingDependency.charge weak_fault_setting_s11.body.account 16 58 2 0 16).2 = .none := by decide

theorem weak_fault_setting_event_13 :
  step weak_fault_setting_s12 .reviseDiagnosis = weak_fault_setting_s13 ∧ RemainingDependency.tariff weak_fault_setting_s12.body.account 2 58 2 0 1 = 3252 ∧ (RemainingDependency.charge weak_fault_setting_s12.body.account 2 58 2 0 1).2 = .none := by decide

theorem weak_fault_setting_event_14 :
  step weak_fault_setting_s13 .retain = weak_fault_setting_s14 ∧ RemainingDependency.tariff weak_fault_setting_s13.body.account 1 58 0 59392 0 = 60532 ∧ (RemainingDependency.charge weak_fault_setting_s13.body.account 1 58 0 59392 0).2 = .none := by decide

theorem weak_fault_setting_saved_run :
  run weak_fault_setting_s0 [.install, .fullContact, .fullWrite, .filterFull, .reviseApplication, .choose, .commit, (.command true), .challenge, .weakContact, .weakWrite, .filterWeak, .reviseDiagnosis, .retain] = weak_fault_setting_s14 := by decide

theorem weak_fault_setting_core_trace :
  Generative.Trace process weak_fault_setting_s0 [.install, .fullContact, .fullWrite, .filterFull, .reviseApplication, .choose, .commit, (.command true), .challenge, .weakContact, .weakWrite, .filterWeak, .reviseDiagnosis, .retain] weak_fault_setting_s14 := by
  rw [← weak_fault_setting_saved_run]
  exact run_is_core_trace _ _

theorem weak_fault_setting_final_whole_account :
  wholeTotal 8419342 weak_fault_setting_s14 = 145 * RemainingDependency.ticks := by decide

def old_changed_context_config : Config := {fullFault := .faithful, weakFault := .faithful, clamp := false}
def old_changed_context_s0 : State := {parent := parent_context_change, config := old_changed_context_config, body := {account := {fuel := 428018, start := 428018, spent := 0, live := 34, peak := 42, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 2, relay := true, pending := none, held := false, installed := false, retained := false, mask := none, fullRecord := none, weakRecord := none, contact := none, application := .unobserved, diagnosis := .unobserved, proposal := none, activation := none, phase := .oldInterface}}
def old_changed_context_s1 : State := {parent := parent_context_change, config := old_changed_context_config, body := {account := {fuel := 311680, start := 428018, spent := 116338, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 2, relay := true, pending := none, held := false, installed := true, retained := false, mask := (some 65535), fullRecord := none, weakRecord := none, contact := none, application := .unobserved, diagnosis := .unobserved, proposal := none, activation := none, phase := .formed}}
def old_changed_context_s2 : State := {parent := parent_context_change, config := old_changed_context_config, body := {account := {fuel := 295236, start := 428018, spent := 132782, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 2, relay := true, pending := none, held := false, installed := true, retained := false, mask := (some 65535), fullRecord := none, weakRecord := none, contact := (some ⟨2, true, false⟩), application := .unobserved, diagnosis := .unobserved, proposal := none, activation := none, phase := .formed}}
def old_changed_context_s3 : State := {parent := parent_context_change, config := old_changed_context_config, body := {account := {fuel := 292044, start := 428018, spent := 135974, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 2, relay := true, pending := none, held := false, installed := true, retained := false, mask := (some 65535), fullRecord := none, weakRecord := none, contact := none, application := .unobserved, diagnosis := .unobserved, proposal := none, activation := none, phase := .formed}}
def old_changed_context_s4 : State := {parent := parent_context_change, config := old_changed_context_config, body := {account := {fuel := 258256, start := 428018, spent := 169762, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 2, relay := true, pending := none, held := false, installed := true, retained := false, mask := (some 65535), fullRecord := none, weakRecord := none, contact := none, application := .unobserved, diagnosis := .unobserved, proposal := none, activation := none, phase := .formed}}
def old_changed_context_s5 : State := {parent := parent_context_change, config := old_changed_context_config, body := {account := {fuel := 255004, start := 428018, spent := 173014, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 2, relay := true, pending := none, held := false, installed := true, retained := false, mask := (some 65535), fullRecord := none, weakRecord := none, contact := none, application := .unavailable, diagnosis := .unobserved, proposal := none, activation := none, phase := .applicationRevised}}
def old_changed_context_s6 : State := {parent := parent_context_change, config := old_changed_context_config, body := {account := {fuel := 219199, start := 428018, spent := 208819, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 2, relay := true, pending := none, held := false, installed := true, retained := false, mask := (some 65535), fullRecord := none, weakRecord := none, contact := none, application := .unavailable, diagnosis := .unobserved, proposal := none, activation := none, phase := .applicationRevised}}
def old_changed_context_s7 : State := {parent := parent_context_change, config := old_changed_context_config, body := {account := {fuel := 217031, start := 428018, spent := 210987, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 2, relay := true, pending := none, held := false, installed := true, retained := false, mask := (some 65535), fullRecord := none, weakRecord := none, contact := none, application := .unavailable, diagnosis := .unobserved, proposal := none, activation := none, phase := .committed}}
def old_changed_context_s8 : State := {parent := parent_context_change, config := old_changed_context_config, body := {account := {fuel := 156499, start := 428018, spent := 271519, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 2, relay := true, pending := none, held := false, installed := true, retained := true, mask := (some 65535), fullRecord := none, weakRecord := none, contact := none, application := .unavailable, diagnosis := .unobserved, proposal := none, activation := none, phase := .committed}}
theorem old_changed_context_actual_entrance :
  entrance parent_context_change old_changed_context_config = old_changed_context_s0 := by decide

theorem old_changed_context_initial_whole_account :
  wholeTotal 8419342 old_changed_context_s0 = 145 * RemainingDependency.ticks := by decide

theorem old_changed_context_event_1 :
  step old_changed_context_s0 .install = old_changed_context_s1 ∧ RemainingDependency.tariff old_changed_context_s0.body.account 24 58 8 65536 0 = 116338 ∧ (RemainingDependency.charge old_changed_context_s0.body.account 24 58 8 65536 0).2 = .none := by decide

theorem old_changed_context_event_2 :
  step old_changed_context_s1 .fullContact = old_changed_context_s2 ∧ RemainingDependency.tariff old_changed_context_s1.body.account 0 58 2 16384 0 = 16444 ∧ (RemainingDependency.charge old_changed_context_s1.body.account 0 58 2 16384 0).2 = .none := by decide

theorem old_changed_context_event_3 :
  step old_changed_context_s2 .fullWrite = old_changed_context_s3 ∧ RemainingDependency.tariff old_changed_context_s2.body.account 1 58 2 0 2 = 3192 ∧ (RemainingDependency.charge old_changed_context_s2.body.account 1 58 2 0 2).2 = .none := by decide

theorem old_changed_context_event_4 :
  step old_changed_context_s3 .filterFull = old_changed_context_s4 ∧ RemainingDependency.tariff old_changed_context_s3.body.account 16 58 2 0 16 = 33788 ∧ (RemainingDependency.charge old_changed_context_s3.body.account 16 58 2 0 16).2 = .none := by decide

theorem old_changed_context_event_5 :
  step old_changed_context_s4 .reviseApplication = old_changed_context_s5 ∧ RemainingDependency.tariff old_changed_context_s4.body.account 2 58 2 0 1 = 3252 ∧ (RemainingDependency.charge old_changed_context_s4.body.account 2 58 2 0 1).2 = .none := by decide

theorem old_changed_context_event_6 :
  step old_changed_context_s5 .choose = old_changed_context_s6 ∧ RemainingDependency.tariff old_changed_context_s5.body.account 32 58 3 0 1 = 35805 ∧ (RemainingDependency.charge old_changed_context_s5.body.account 32 58 3 0 1).2 = .none := by decide

theorem old_changed_context_event_7 :
  step old_changed_context_s6 .commit = old_changed_context_s7 ∧ RemainingDependency.tariff old_changed_context_s6.body.account 1 58 2 0 1 = 2168 ∧ (RemainingDependency.charge old_changed_context_s6.body.account 1 58 2 0 1).2 = .none := by decide

theorem old_changed_context_event_8 :
  step old_changed_context_s7 .retain = old_changed_context_s8 ∧ RemainingDependency.tariff old_changed_context_s7.body.account 1 58 0 59392 0 = 60532 ∧ (RemainingDependency.charge old_changed_context_s7.body.account 1 58 0 59392 0).2 = .none := by decide

theorem old_changed_context_saved_run :
  run old_changed_context_s0 [.install, .fullContact, .fullWrite, .filterFull, .reviseApplication, .choose, .commit, .retain] = old_changed_context_s8 := by decide

theorem old_changed_context_core_trace :
  Generative.Trace process old_changed_context_s0 [.install, .fullContact, .fullWrite, .filterFull, .reviseApplication, .choose, .commit, .retain] old_changed_context_s8 := by
  rw [← old_changed_context_saved_run]
  exact run_is_core_trace _ _

theorem old_changed_context_final_whole_account :
  wholeTotal 8419342 old_changed_context_s8 = 145 * RemainingDependency.ticks := by decide

def old_source_denied_config : Config := {fullFault := .faithful, weakFault := .faithful, clamp := false}
def old_source_denied_s0 : State := {parent := parent_source_exhausted, config := old_source_denied_config, body := {account := {fuel := 642106, start := 642106, spent := 0, live := 34, peak := 42, capacity := 256}, stocks := ⟨0, 0, 0⟩, context := 1, relay := true, pending := none, held := true, installed := false, retained := false, mask := none, fullRecord := none, weakRecord := none, contact := none, application := .unobserved, diagnosis := .unobserved, proposal := none, activation := none, phase := .oldInterface}}
def old_source_denied_s1 : State := {parent := parent_source_exhausted, config := old_source_denied_config, body := {account := {fuel := 642106, start := 642106, spent := 0, live := 34, peak := 42, capacity := 256}, stocks := ⟨0, 0, 0⟩, context := 1, relay := true, pending := none, held := true, installed := false, retained := false, mask := none, fullRecord := none, weakRecord := none, contact := none, application := .unobserved, diagnosis := .unobserved, proposal := none, activation := none, phase := .oldInterface}}
theorem old_source_denied_actual_entrance :
  entrance parent_source_exhausted old_source_denied_config = old_source_denied_s0 := by decide

theorem old_source_denied_initial_whole_account :
  wholeTotal 8860614 old_source_denied_s0 = 145 * RemainingDependency.ticks := by decide

theorem old_source_denied_event_1 :
  (old_source_denied_s0.parent.body.retained = false ∨ old_source_denied_s0.parent.body.mode ≠ .serviceIssued ∨ old_source_denied_s0.parent.body.selected = none ∨ old_source_denied_s0.body.stocks.source ≠ 0) ∧ old_source_denied_s0 = old_source_denied_s1 := by decide

theorem old_source_denied_saved_run :
  run old_source_denied_s0 [] = old_source_denied_s1 := by decide

theorem old_source_denied_core_trace :
  Generative.Trace process old_source_denied_s0 [] old_source_denied_s1 := by
  rw [← old_source_denied_saved_run]
  exact run_is_core_trace _ _

theorem old_source_denied_final_whole_account :
  wholeTotal 8860614 old_source_denied_s1 = 145 * RemainingDependency.ticks := by decide

def wait_one_config : Config := {fullFault := .faithful, weakFault := .faithful, clamp := false}
def wait_one_s0 : State := {parent := parent_calibration_break, config := wait_one_config, body := {account := {fuel := 428018, start := 428018, spent := 0, live := 34, peak := 42, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := false, retained := false, mask := none, fullRecord := none, weakRecord := none, contact := none, application := .unobserved, diagnosis := .unobserved, proposal := none, activation := none, phase := .oldInterface}}
def wait_one_s1 : State := {parent := parent_calibration_break, config := wait_one_config, body := {account := {fuel := 362448, start := 428018, spent := 65570, live := 34, peak := 42, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := false, retained := false, mask := none, fullRecord := none, weakRecord := none, contact := none, application := .unobserved, diagnosis := .unobserved, proposal := none, activation := none, phase := .oldInterface}}
def wait_one_s2 : State := {parent := parent_calibration_break, config := wait_one_config, body := {account := {fuel := 246110, start := 428018, spent := 181908, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := false, mask := (some 65535), fullRecord := none, weakRecord := none, contact := none, application := .unobserved, diagnosis := .unobserved, proposal := none, activation := none, phase := .formed}}
def wait_one_s3 : State := {parent := parent_calibration_break, config := wait_one_config, body := {account := {fuel := 229666, start := 428018, spent := 198352, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := false, mask := (some 65535), fullRecord := none, weakRecord := none, contact := (some ⟨1, true, false⟩), application := .unobserved, diagnosis := .unobserved, proposal := none, activation := none, phase := .formed}}
def wait_one_s4 : State := {parent := parent_calibration_break, config := wait_one_config, body := {account := {fuel := 226474, start := 428018, spent := 201544, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := false, mask := (some 65535), fullRecord := (some ⟨1, true, false⟩), weakRecord := none, contact := none, application := .unobserved, diagnosis := .unobserved, proposal := none, activation := none, phase := .formed}}
def wait_one_s5 : State := {parent := parent_calibration_break, config := wait_one_config, body := {account := {fuel := 192686, start := 428018, spent := 235332, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := false, mask := (some 255), fullRecord := (some ⟨1, true, false⟩), weakRecord := none, contact := none, application := .unobserved, diagnosis := .unobserved, proposal := none, activation := none, phase := .formed}}
def wait_one_s6 : State := {parent := parent_calibration_break, config := wait_one_config, body := {account := {fuel := 189434, start := 428018, spent := 238584, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := false, mask := (some 255), fullRecord := (some ⟨1, true, false⟩), weakRecord := none, contact := none, application := .failed, diagnosis := .unobserved, proposal := none, activation := none, phase := .applicationRevised}}
def wait_one_s7 : State := {parent := parent_calibration_break, config := wait_one_config, body := {account := {fuel := 153629, start := 428018, spent := 274389, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := false, mask := (some 255), fullRecord := (some ⟨1, true, false⟩), weakRecord := none, contact := none, application := .failed, diagnosis := .unobserved, proposal := (some true), activation := none, phase := .applicationRevised}}
def wait_one_s8 : State := {parent := parent_calibration_break, config := wait_one_config, body := {account := {fuel := 151461, start := 428018, spent := 276557, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := false, mask := (some 255), fullRecord := (some ⟨1, true, false⟩), weakRecord := none, contact := none, application := .failed, diagnosis := .unobserved, proposal := (some true), activation := (some true), phase := .committed}}
def wait_one_s9 : State := {parent := parent_calibration_break, config := wait_one_config, body := {account := {fuel := 133933, start := 428018, spent := 294085, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := false, mask := (some 255), fullRecord := (some ⟨1, true, false⟩), weakRecord := none, contact := none, application := .failed, diagnosis := .unobserved, proposal := (some true), activation := (some true), phase := .committed}}
def wait_one_s10 : State := {parent := parent_calibration_break, config := wait_one_config, body := {account := {fuel := 116405, start := 428018, spent := 311613, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := (some ⟨1, true, true⟩), held := false, installed := true, retained := false, mask := (some 255), fullRecord := (some ⟨1, true, false⟩), weakRecord := none, contact := none, application := .failed, diagnosis := .unobserved, proposal := (some true), activation := (some true), phase := .committed}}
def wait_one_s11 : State := {parent := parent_calibration_break, config := wait_one_config, body := {account := {fuel := 99961, start := 428018, spent := 328057, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := false, mask := (some 255), fullRecord := (some ⟨1, true, false⟩), weakRecord := none, contact := (some ⟨1, true, true⟩), application := .failed, diagnosis := .unobserved, proposal := (some true), activation := (some true), phase := .committed}}
def wait_one_s12 : State := {parent := parent_calibration_break, config := wait_one_config, body := {account := {fuel := 96769, start := 428018, spent := 331249, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := false, mask := (some 255), fullRecord := (some ⟨1, true, false⟩), weakRecord := (some ⟨1, true, true⟩), contact := none, application := .failed, diagnosis := .unobserved, proposal := (some true), activation := (some true), phase := .committed}}
def wait_one_s13 : State := {parent := parent_calibration_break, config := wait_one_config, body := {account := {fuel := 62981, start := 428018, spent := 365037, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := false, mask := (some 204), fullRecord := (some ⟨1, true, false⟩), weakRecord := (some ⟨1, true, true⟩), contact := none, application := .failed, diagnosis := .unobserved, proposal := (some true), activation := (some true), phase := .committed}}
def wait_one_s14 : State := {parent := parent_calibration_break, config := wait_one_config, body := {account := {fuel := 59729, start := 428018, spent := 368289, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := false, mask := (some 204), fullRecord := (some ⟨1, true, false⟩), weakRecord := (some ⟨1, true, true⟩), contact := none, application := .failed, diagnosis := .discrepancy, proposal := (some true), activation := (some true), phase := .diagnosisRevised}}
def wait_one_s15 : State := {parent := parent_calibration_break, config := wait_one_config, body := {account := {fuel := 59729, start := 428018, spent := 368289, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := false, mask := (some 204), fullRecord := (some ⟨1, true, false⟩), weakRecord := (some ⟨1, true, true⟩), contact := none, application := .failed, diagnosis := .discrepancy, proposal := (some true), activation := (some true), phase := .diagnosisRevised}}
theorem wait_one_actual_entrance :
  entrance parent_calibration_break wait_one_config = wait_one_s0 := by decide

theorem wait_one_initial_whole_account :
  wholeTotal 8419342 wait_one_s0 = 145 * RemainingDependency.ticks := by decide

theorem wait_one_event_1 :
  step wait_one_s0 (.wait 1) = wait_one_s1 ∧ RemainingDependency.tariff wait_one_s0.body.account 0 34 0 65536 0 = 65570 ∧ (RemainingDependency.charge wait_one_s0.body.account 0 34 0 65536 0).2 = .none := by decide

theorem wait_one_event_2 :
  step wait_one_s1 .install = wait_one_s2 ∧ RemainingDependency.tariff wait_one_s1.body.account 24 58 8 65536 0 = 116338 ∧ (RemainingDependency.charge wait_one_s1.body.account 24 58 8 65536 0).2 = .none := by decide

theorem wait_one_event_3 :
  step wait_one_s2 .fullContact = wait_one_s3 ∧ RemainingDependency.tariff wait_one_s2.body.account 0 58 2 16384 0 = 16444 ∧ (RemainingDependency.charge wait_one_s2.body.account 0 58 2 16384 0).2 = .none := by decide

theorem wait_one_event_4 :
  step wait_one_s3 .fullWrite = wait_one_s4 ∧ RemainingDependency.tariff wait_one_s3.body.account 1 58 2 0 2 = 3192 ∧ (RemainingDependency.charge wait_one_s3.body.account 1 58 2 0 2).2 = .none := by decide

theorem wait_one_event_5 :
  step wait_one_s4 .filterFull = wait_one_s5 ∧ RemainingDependency.tariff wait_one_s4.body.account 16 58 2 0 16 = 33788 ∧ (RemainingDependency.charge wait_one_s4.body.account 16 58 2 0 16).2 = .none := by decide

theorem wait_one_event_6 :
  step wait_one_s5 .reviseApplication = wait_one_s6 ∧ RemainingDependency.tariff wait_one_s5.body.account 2 58 2 0 1 = 3252 ∧ (RemainingDependency.charge wait_one_s5.body.account 2 58 2 0 1).2 = .none := by decide

theorem wait_one_event_7 :
  step wait_one_s6 .choose = wait_one_s7 ∧ RemainingDependency.tariff wait_one_s6.body.account 32 58 3 0 1 = 35805 ∧ (RemainingDependency.charge wait_one_s6.body.account 32 58 3 0 1).2 = .none := by decide

theorem wait_one_event_8 :
  step wait_one_s7 .commit = wait_one_s8 ∧ RemainingDependency.tariff wait_one_s7.body.account 1 58 2 0 1 = 2168 ∧ (RemainingDependency.charge wait_one_s7.body.account 1 58 2 0 1).2 = .none := by decide

theorem wait_one_event_9 :
  step wait_one_s8 (.command true) = wait_one_s9 ∧ RemainingDependency.tariff wait_one_s8.body.account 1 58 2 16384 0 = 17528 ∧ (RemainingDependency.charge wait_one_s8.body.account 1 58 2 16384 0).2 = .none := by decide

theorem wait_one_event_10 :
  step wait_one_s9 .challenge = wait_one_s10 ∧ RemainingDependency.tariff wait_one_s9.body.account 1 58 2 16384 0 = 17528 ∧ (RemainingDependency.charge wait_one_s9.body.account 1 58 2 16384 0).2 = .none := by decide

theorem wait_one_event_11 :
  step wait_one_s10 .weakContact = wait_one_s11 ∧ RemainingDependency.tariff wait_one_s10.body.account 0 58 2 16384 0 = 16444 ∧ (RemainingDependency.charge wait_one_s10.body.account 0 58 2 16384 0).2 = .none := by decide

theorem wait_one_event_12 :
  step wait_one_s11 .weakWrite = wait_one_s12 ∧ RemainingDependency.tariff wait_one_s11.body.account 1 58 2 0 2 = 3192 ∧ (RemainingDependency.charge wait_one_s11.body.account 1 58 2 0 2).2 = .none := by decide

theorem wait_one_event_13 :
  step wait_one_s12 .filterWeak = wait_one_s13 ∧ RemainingDependency.tariff wait_one_s12.body.account 16 58 2 0 16 = 33788 ∧ (RemainingDependency.charge wait_one_s12.body.account 16 58 2 0 16).2 = .none := by decide

theorem wait_one_event_14 :
  step wait_one_s13 .reviseDiagnosis = wait_one_s14 ∧ RemainingDependency.tariff wait_one_s13.body.account 2 58 2 0 1 = 3252 ∧ (RemainingDependency.charge wait_one_s13.body.account 2 58 2 0 1).2 = .none := by decide

theorem wait_one_event_15 :
  (RemainingDependency.charge wait_one_s14.body.account 1 58 0 59392 0).2 = .funding ∧ step wait_one_s14 .retain = wait_one_s15 := by decide

theorem wait_one_saved_run :
  run wait_one_s0 [(.wait 1), .install, .fullContact, .fullWrite, .filterFull, .reviseApplication, .choose, .commit, (.command true), .challenge, .weakContact, .weakWrite, .filterWeak, .reviseDiagnosis, .retain] = wait_one_s15 := by decide

theorem wait_one_core_trace :
  Generative.Trace process wait_one_s0 [(.wait 1), .install, .fullContact, .fullWrite, .filterFull, .reviseApplication, .choose, .commit, (.command true), .challenge, .weakContact, .weakWrite, .filterWeak, .reviseDiagnosis, .retain] wait_one_s15 := by
  rw [← wait_one_saved_run]
  exact run_is_core_trace _ _

theorem wait_one_final_whole_account :
  wholeTotal 8419342 wait_one_s15 = 145 * RemainingDependency.ticks := by decide

def wait_two_config : Config := {fullFault := .faithful, weakFault := .faithful, clamp := false}
def wait_two_s0 : State := {parent := parent_calibration_break, config := wait_two_config, body := {account := {fuel := 428018, start := 428018, spent := 0, live := 34, peak := 42, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := false, retained := false, mask := none, fullRecord := none, weakRecord := none, contact := none, application := .unobserved, diagnosis := .unobserved, proposal := none, activation := none, phase := .oldInterface}}
def wait_two_s1 : State := {parent := parent_calibration_break, config := wait_two_config, body := {account := {fuel := 296912, start := 428018, spent := 131106, live := 34, peak := 42, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := false, retained := false, mask := none, fullRecord := none, weakRecord := none, contact := none, application := .unobserved, diagnosis := .unobserved, proposal := none, activation := none, phase := .oldInterface}}
def wait_two_s2 : State := {parent := parent_calibration_break, config := wait_two_config, body := {account := {fuel := 180574, start := 428018, spent := 247444, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := false, mask := (some 65535), fullRecord := none, weakRecord := none, contact := none, application := .unobserved, diagnosis := .unobserved, proposal := none, activation := none, phase := .formed}}
def wait_two_s3 : State := {parent := parent_calibration_break, config := wait_two_config, body := {account := {fuel := 164130, start := 428018, spent := 263888, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := false, mask := (some 65535), fullRecord := none, weakRecord := none, contact := (some ⟨1, true, false⟩), application := .unobserved, diagnosis := .unobserved, proposal := none, activation := none, phase := .formed}}
def wait_two_s4 : State := {parent := parent_calibration_break, config := wait_two_config, body := {account := {fuel := 160938, start := 428018, spent := 267080, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := false, mask := (some 65535), fullRecord := (some ⟨1, true, false⟩), weakRecord := none, contact := none, application := .unobserved, diagnosis := .unobserved, proposal := none, activation := none, phase := .formed}}
def wait_two_s5 : State := {parent := parent_calibration_break, config := wait_two_config, body := {account := {fuel := 127150, start := 428018, spent := 300868, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := false, mask := (some 255), fullRecord := (some ⟨1, true, false⟩), weakRecord := none, contact := none, application := .unobserved, diagnosis := .unobserved, proposal := none, activation := none, phase := .formed}}
def wait_two_s6 : State := {parent := parent_calibration_break, config := wait_two_config, body := {account := {fuel := 123898, start := 428018, spent := 304120, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := false, mask := (some 255), fullRecord := (some ⟨1, true, false⟩), weakRecord := none, contact := none, application := .failed, diagnosis := .unobserved, proposal := none, activation := none, phase := .applicationRevised}}
def wait_two_s7 : State := {parent := parent_calibration_break, config := wait_two_config, body := {account := {fuel := 88093, start := 428018, spent := 339925, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := false, mask := (some 255), fullRecord := (some ⟨1, true, false⟩), weakRecord := none, contact := none, application := .failed, diagnosis := .unobserved, proposal := (some true), activation := none, phase := .applicationRevised}}
def wait_two_s8 : State := {parent := parent_calibration_break, config := wait_two_config, body := {account := {fuel := 85925, start := 428018, spent := 342093, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := false, mask := (some 255), fullRecord := (some ⟨1, true, false⟩), weakRecord := none, contact := none, application := .failed, diagnosis := .unobserved, proposal := (some true), activation := (some true), phase := .committed}}
def wait_two_s9 : State := {parent := parent_calibration_break, config := wait_two_config, body := {account := {fuel := 68397, start := 428018, spent := 359621, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := false, mask := (some 255), fullRecord := (some ⟨1, true, false⟩), weakRecord := none, contact := none, application := .failed, diagnosis := .unobserved, proposal := (some true), activation := (some true), phase := .committed}}
def wait_two_s10 : State := {parent := parent_calibration_break, config := wait_two_config, body := {account := {fuel := 50869, start := 428018, spent := 377149, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := (some ⟨1, true, true⟩), held := false, installed := true, retained := false, mask := (some 255), fullRecord := (some ⟨1, true, false⟩), weakRecord := none, contact := none, application := .failed, diagnosis := .unobserved, proposal := (some true), activation := (some true), phase := .committed}}
def wait_two_s11 : State := {parent := parent_calibration_break, config := wait_two_config, body := {account := {fuel := 34425, start := 428018, spent := 393593, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := false, mask := (some 255), fullRecord := (some ⟨1, true, false⟩), weakRecord := none, contact := (some ⟨1, true, true⟩), application := .failed, diagnosis := .unobserved, proposal := (some true), activation := (some true), phase := .committed}}
def wait_two_s12 : State := {parent := parent_calibration_break, config := wait_two_config, body := {account := {fuel := 31233, start := 428018, spent := 396785, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := false, mask := (some 255), fullRecord := (some ⟨1, true, false⟩), weakRecord := (some ⟨1, true, true⟩), contact := none, application := .failed, diagnosis := .unobserved, proposal := (some true), activation := (some true), phase := .committed}}
def wait_two_s13 : State := {parent := parent_calibration_break, config := wait_two_config, body := {account := {fuel := 31233, start := 428018, spent := 396785, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := false, mask := (some 255), fullRecord := (some ⟨1, true, false⟩), weakRecord := (some ⟨1, true, true⟩), contact := none, application := .failed, diagnosis := .unobserved, proposal := (some true), activation := (some true), phase := .committed}}
def wait_two_s14 : State := {parent := parent_calibration_break, config := wait_two_config, body := {account := {fuel := 31233, start := 428018, spent := 396785, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := false, mask := (some 255), fullRecord := (some ⟨1, true, false⟩), weakRecord := (some ⟨1, true, true⟩), contact := none, application := .failed, diagnosis := .unobserved, proposal := (some true), activation := (some true), phase := .committed}}
theorem wait_two_actual_entrance :
  entrance parent_calibration_break wait_two_config = wait_two_s0 := by decide

theorem wait_two_initial_whole_account :
  wholeTotal 8419342 wait_two_s0 = 145 * RemainingDependency.ticks := by decide

theorem wait_two_event_1 :
  step wait_two_s0 (.wait 2) = wait_two_s1 ∧ RemainingDependency.tariff wait_two_s0.body.account 0 34 0 131072 0 = 131106 ∧ (RemainingDependency.charge wait_two_s0.body.account 0 34 0 131072 0).2 = .none := by decide

theorem wait_two_event_2 :
  step wait_two_s1 .install = wait_two_s2 ∧ RemainingDependency.tariff wait_two_s1.body.account 24 58 8 65536 0 = 116338 ∧ (RemainingDependency.charge wait_two_s1.body.account 24 58 8 65536 0).2 = .none := by decide

theorem wait_two_event_3 :
  step wait_two_s2 .fullContact = wait_two_s3 ∧ RemainingDependency.tariff wait_two_s2.body.account 0 58 2 16384 0 = 16444 ∧ (RemainingDependency.charge wait_two_s2.body.account 0 58 2 16384 0).2 = .none := by decide

theorem wait_two_event_4 :
  step wait_two_s3 .fullWrite = wait_two_s4 ∧ RemainingDependency.tariff wait_two_s3.body.account 1 58 2 0 2 = 3192 ∧ (RemainingDependency.charge wait_two_s3.body.account 1 58 2 0 2).2 = .none := by decide

theorem wait_two_event_5 :
  step wait_two_s4 .filterFull = wait_two_s5 ∧ RemainingDependency.tariff wait_two_s4.body.account 16 58 2 0 16 = 33788 ∧ (RemainingDependency.charge wait_two_s4.body.account 16 58 2 0 16).2 = .none := by decide

theorem wait_two_event_6 :
  step wait_two_s5 .reviseApplication = wait_two_s6 ∧ RemainingDependency.tariff wait_two_s5.body.account 2 58 2 0 1 = 3252 ∧ (RemainingDependency.charge wait_two_s5.body.account 2 58 2 0 1).2 = .none := by decide

theorem wait_two_event_7 :
  step wait_two_s6 .choose = wait_two_s7 ∧ RemainingDependency.tariff wait_two_s6.body.account 32 58 3 0 1 = 35805 ∧ (RemainingDependency.charge wait_two_s6.body.account 32 58 3 0 1).2 = .none := by decide

theorem wait_two_event_8 :
  step wait_two_s7 .commit = wait_two_s8 ∧ RemainingDependency.tariff wait_two_s7.body.account 1 58 2 0 1 = 2168 ∧ (RemainingDependency.charge wait_two_s7.body.account 1 58 2 0 1).2 = .none := by decide

theorem wait_two_event_9 :
  step wait_two_s8 (.command true) = wait_two_s9 ∧ RemainingDependency.tariff wait_two_s8.body.account 1 58 2 16384 0 = 17528 ∧ (RemainingDependency.charge wait_two_s8.body.account 1 58 2 16384 0).2 = .none := by decide

theorem wait_two_event_10 :
  step wait_two_s9 .challenge = wait_two_s10 ∧ RemainingDependency.tariff wait_two_s9.body.account 1 58 2 16384 0 = 17528 ∧ (RemainingDependency.charge wait_two_s9.body.account 1 58 2 16384 0).2 = .none := by decide

theorem wait_two_event_11 :
  step wait_two_s10 .weakContact = wait_two_s11 ∧ RemainingDependency.tariff wait_two_s10.body.account 0 58 2 16384 0 = 16444 ∧ (RemainingDependency.charge wait_two_s10.body.account 0 58 2 16384 0).2 = .none := by decide

theorem wait_two_event_12 :
  step wait_two_s11 .weakWrite = wait_two_s12 ∧ RemainingDependency.tariff wait_two_s11.body.account 1 58 2 0 2 = 3192 ∧ (RemainingDependency.charge wait_two_s11.body.account 1 58 2 0 2).2 = .none := by decide

theorem wait_two_event_13 :
  (RemainingDependency.charge wait_two_s12.body.account 16 58 2 0 16).2 = .funding ∧ step wait_two_s12 .filterWeak = wait_two_s13 := by decide

theorem wait_two_event_14 :
  (RemainingDependency.charge wait_two_s13.body.account 1 58 0 59392 0).2 = .funding ∧ step wait_two_s13 .retain = wait_two_s14 := by decide

theorem wait_two_saved_run :
  run wait_two_s0 [(.wait 2), .install, .fullContact, .fullWrite, .filterFull, .reviseApplication, .choose, .commit, (.command true), .challenge, .weakContact, .weakWrite, .filterWeak, .retain] = wait_two_s14 := by decide

theorem wait_two_core_trace :
  Generative.Trace process wait_two_s0 [(.wait 2), .install, .fullContact, .fullWrite, .filterFull, .reviseApplication, .choose, .commit, (.command true), .challenge, .weakContact, .weakWrite, .filterWeak, .retain] wait_two_s14 := by
  rw [← wait_two_saved_run]
  exact run_is_core_trace _ _

theorem wait_two_final_whole_account :
  wholeTotal 8419342 wait_two_s14 = 145 * RemainingDependency.ticks := by decide

def wait_three_config : Config := {fullFault := .faithful, weakFault := .faithful, clamp := false}
def wait_three_s0 : State := {parent := parent_calibration_break, config := wait_three_config, body := {account := {fuel := 428018, start := 428018, spent := 0, live := 34, peak := 42, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := false, retained := false, mask := none, fullRecord := none, weakRecord := none, contact := none, application := .unobserved, diagnosis := .unobserved, proposal := none, activation := none, phase := .oldInterface}}
def wait_three_s1 : State := {parent := parent_calibration_break, config := wait_three_config, body := {account := {fuel := 231376, start := 428018, spent := 196642, live := 34, peak := 42, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := false, retained := false, mask := none, fullRecord := none, weakRecord := none, contact := none, application := .unobserved, diagnosis := .unobserved, proposal := none, activation := none, phase := .oldInterface}}
def wait_three_s2 : State := {parent := parent_calibration_break, config := wait_three_config, body := {account := {fuel := 115038, start := 428018, spent := 312980, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := false, mask := (some 65535), fullRecord := none, weakRecord := none, contact := none, application := .unobserved, diagnosis := .unobserved, proposal := none, activation := none, phase := .formed}}
def wait_three_s3 : State := {parent := parent_calibration_break, config := wait_three_config, body := {account := {fuel := 98594, start := 428018, spent := 329424, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := false, mask := (some 65535), fullRecord := none, weakRecord := none, contact := (some ⟨1, true, false⟩), application := .unobserved, diagnosis := .unobserved, proposal := none, activation := none, phase := .formed}}
def wait_three_s4 : State := {parent := parent_calibration_break, config := wait_three_config, body := {account := {fuel := 95402, start := 428018, spent := 332616, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := false, mask := (some 65535), fullRecord := (some ⟨1, true, false⟩), weakRecord := none, contact := none, application := .unobserved, diagnosis := .unobserved, proposal := none, activation := none, phase := .formed}}
def wait_three_s5 : State := {parent := parent_calibration_break, config := wait_three_config, body := {account := {fuel := 61614, start := 428018, spent := 366404, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := false, mask := (some 255), fullRecord := (some ⟨1, true, false⟩), weakRecord := none, contact := none, application := .unobserved, diagnosis := .unobserved, proposal := none, activation := none, phase := .formed}}
def wait_three_s6 : State := {parent := parent_calibration_break, config := wait_three_config, body := {account := {fuel := 58362, start := 428018, spent := 369656, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := false, mask := (some 255), fullRecord := (some ⟨1, true, false⟩), weakRecord := none, contact := none, application := .failed, diagnosis := .unobserved, proposal := none, activation := none, phase := .applicationRevised}}
def wait_three_s7 : State := {parent := parent_calibration_break, config := wait_three_config, body := {account := {fuel := 22557, start := 428018, spent := 405461, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := false, mask := (some 255), fullRecord := (some ⟨1, true, false⟩), weakRecord := none, contact := none, application := .failed, diagnosis := .unobserved, proposal := (some true), activation := none, phase := .applicationRevised}}
def wait_three_s8 : State := {parent := parent_calibration_break, config := wait_three_config, body := {account := {fuel := 20389, start := 428018, spent := 407629, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := false, mask := (some 255), fullRecord := (some ⟨1, true, false⟩), weakRecord := none, contact := none, application := .failed, diagnosis := .unobserved, proposal := (some true), activation := (some true), phase := .committed}}
def wait_three_s9 : State := {parent := parent_calibration_break, config := wait_three_config, body := {account := {fuel := 2861, start := 428018, spent := 425157, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := false, mask := (some 255), fullRecord := (some ⟨1, true, false⟩), weakRecord := none, contact := none, application := .failed, diagnosis := .unobserved, proposal := (some true), activation := (some true), phase := .committed}}
def wait_three_s10 : State := {parent := parent_calibration_break, config := wait_three_config, body := {account := {fuel := 2861, start := 428018, spent := 425157, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := false, mask := (some 255), fullRecord := (some ⟨1, true, false⟩), weakRecord := none, contact := none, application := .failed, diagnosis := .unobserved, proposal := (some true), activation := (some true), phase := .committed}}
def wait_three_s11 : State := {parent := parent_calibration_break, config := wait_three_config, body := {account := {fuel := 2861, start := 428018, spent := 425157, live := 58, peak := 66, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := false, mask := (some 255), fullRecord := (some ⟨1, true, false⟩), weakRecord := none, contact := none, application := .failed, diagnosis := .unobserved, proposal := (some true), activation := (some true), phase := .committed}}
theorem wait_three_actual_entrance :
  entrance parent_calibration_break wait_three_config = wait_three_s0 := by decide

theorem wait_three_initial_whole_account :
  wholeTotal 8419342 wait_three_s0 = 145 * RemainingDependency.ticks := by decide

theorem wait_three_event_1 :
  step wait_three_s0 (.wait 3) = wait_three_s1 ∧ RemainingDependency.tariff wait_three_s0.body.account 0 34 0 196608 0 = 196642 ∧ (RemainingDependency.charge wait_three_s0.body.account 0 34 0 196608 0).2 = .none := by decide

theorem wait_three_event_2 :
  step wait_three_s1 .install = wait_three_s2 ∧ RemainingDependency.tariff wait_three_s1.body.account 24 58 8 65536 0 = 116338 ∧ (RemainingDependency.charge wait_three_s1.body.account 24 58 8 65536 0).2 = .none := by decide

theorem wait_three_event_3 :
  step wait_three_s2 .fullContact = wait_three_s3 ∧ RemainingDependency.tariff wait_three_s2.body.account 0 58 2 16384 0 = 16444 ∧ (RemainingDependency.charge wait_three_s2.body.account 0 58 2 16384 0).2 = .none := by decide

theorem wait_three_event_4 :
  step wait_three_s3 .fullWrite = wait_three_s4 ∧ RemainingDependency.tariff wait_three_s3.body.account 1 58 2 0 2 = 3192 ∧ (RemainingDependency.charge wait_three_s3.body.account 1 58 2 0 2).2 = .none := by decide

theorem wait_three_event_5 :
  step wait_three_s4 .filterFull = wait_three_s5 ∧ RemainingDependency.tariff wait_three_s4.body.account 16 58 2 0 16 = 33788 ∧ (RemainingDependency.charge wait_three_s4.body.account 16 58 2 0 16).2 = .none := by decide

theorem wait_three_event_6 :
  step wait_three_s5 .reviseApplication = wait_three_s6 ∧ RemainingDependency.tariff wait_three_s5.body.account 2 58 2 0 1 = 3252 ∧ (RemainingDependency.charge wait_three_s5.body.account 2 58 2 0 1).2 = .none := by decide

theorem wait_three_event_7 :
  step wait_three_s6 .choose = wait_three_s7 ∧ RemainingDependency.tariff wait_three_s6.body.account 32 58 3 0 1 = 35805 ∧ (RemainingDependency.charge wait_three_s6.body.account 32 58 3 0 1).2 = .none := by decide

theorem wait_three_event_8 :
  step wait_three_s7 .commit = wait_three_s8 ∧ RemainingDependency.tariff wait_three_s7.body.account 1 58 2 0 1 = 2168 ∧ (RemainingDependency.charge wait_three_s7.body.account 1 58 2 0 1).2 = .none := by decide

theorem wait_three_event_9 :
  step wait_three_s8 (.command true) = wait_three_s9 ∧ RemainingDependency.tariff wait_three_s8.body.account 1 58 2 16384 0 = 17528 ∧ (RemainingDependency.charge wait_three_s8.body.account 1 58 2 16384 0).2 = .none := by decide

theorem wait_three_event_10 :
  (RemainingDependency.charge wait_three_s9.body.account 1 58 2 16384 0).2 = .funding ∧ step wait_three_s9 .challenge = wait_three_s10 := by decide

theorem wait_three_event_11 :
  (RemainingDependency.charge wait_three_s10.body.account 1 58 0 59392 0).2 = .funding ∧ step wait_three_s10 .retain = wait_three_s11 := by decide

theorem wait_three_saved_run :
  run wait_three_s0 [(.wait 3), .install, .fullContact, .fullWrite, .filterFull, .reviseApplication, .choose, .commit, (.command true), .challenge, .retain] = wait_three_s11 := by decide

theorem wait_three_core_trace :
  Generative.Trace process wait_three_s0 [(.wait 3), .install, .fullContact, .fullWrite, .filterFull, .reviseApplication, .choose, .commit, (.command true), .challenge, .retain] wait_three_s11 := by
  rw [← wait_three_saved_run]
  exact run_is_core_trace _ _

theorem wait_three_final_whole_account :
  wholeTotal 8419342 wait_three_s11 = 145 * RemainingDependency.ticks := by decide

#print axioms parent_calibration_break_matches_prior_formal_construction
#print axioms parent_false_dependence_matches_prior_formal_construction
#print axioms parent_law_01_learned_matches_prior_formal_construction
#print axioms mask_encoding_51
#print axioms mask_encoding_204
#print axioms mask_encoding_255
#print axioms mask_encoding_1285
#print axioms mask_encoding_3855
#print axioms mask_encoding_61680
#print axioms mask_encoding_65280
#print axioms mask_encoding_65535
#print axioms positive_learned_actual_entrance
#print axioms positive_learned_initial_whole_account
#print axioms positive_learned_event_1
#print axioms positive_learned_event_2
#print axioms positive_learned_event_3
#print axioms positive_learned_event_4
#print axioms positive_learned_event_5
#print axioms positive_learned_event_6
#print axioms positive_learned_event_7
#print axioms positive_learned_event_8
#print axioms positive_learned_saved_run
#print axioms positive_learned_core_trace
#print axioms positive_learned_final_whole_account
#print axioms positive_clamped_actual_entrance
#print axioms positive_clamped_initial_whole_account
#print axioms positive_clamped_event_1
#print axioms positive_clamped_event_2
#print axioms positive_clamped_event_3
#print axioms positive_clamped_event_4
#print axioms positive_clamped_event_5
#print axioms positive_clamped_event_6
#print axioms positive_clamped_event_7
#print axioms positive_clamped_event_8
#print axioms positive_clamped_saved_run
#print axioms positive_clamped_core_trace
#print axioms positive_clamped_final_whole_account
#print axioms positive_conventional_actual_entrance
#print axioms positive_conventional_initial_whole_account
#print axioms positive_conventional_event_1
#print axioms positive_conventional_event_2
#print axioms positive_conventional_event_3
#print axioms positive_conventional_event_4
#print axioms positive_conventional_event_5
#print axioms positive_conventional_event_6
#print axioms positive_conventional_event_7
#print axioms positive_conventional_event_8
#print axioms positive_conventional_saved_run
#print axioms positive_conventional_core_trace
#print axioms positive_conventional_final_whole_account
#print axioms mismatch_learned_actual_entrance
#print axioms mismatch_learned_initial_whole_account
#print axioms mismatch_learned_event_1
#print axioms mismatch_learned_event_2
#print axioms mismatch_learned_event_3
#print axioms mismatch_learned_event_4
#print axioms mismatch_learned_event_5
#print axioms mismatch_learned_event_6
#print axioms mismatch_learned_event_7
#print axioms mismatch_learned_event_8
#print axioms mismatch_learned_event_9
#print axioms mismatch_learned_event_10
#print axioms mismatch_learned_event_11
#print axioms mismatch_learned_event_12
#print axioms mismatch_learned_event_13
#print axioms mismatch_learned_event_14
#print axioms mismatch_learned_saved_run
#print axioms mismatch_learned_core_trace
#print axioms mismatch_learned_final_whole_account
#print axioms mismatch_clamped_actual_entrance
#print axioms mismatch_clamped_initial_whole_account
#print axioms mismatch_clamped_event_1
#print axioms mismatch_clamped_event_2
#print axioms mismatch_clamped_event_3
#print axioms mismatch_clamped_event_4
#print axioms mismatch_clamped_event_5
#print axioms mismatch_clamped_event_6
#print axioms mismatch_clamped_event_7
#print axioms mismatch_clamped_event_8
#print axioms mismatch_clamped_saved_run
#print axioms mismatch_clamped_core_trace
#print axioms mismatch_clamped_final_whole_account
#print axioms mismatch_conventional_actual_entrance
#print axioms mismatch_conventional_initial_whole_account
#print axioms mismatch_conventional_event_1
#print axioms mismatch_conventional_event_2
#print axioms mismatch_conventional_event_3
#print axioms mismatch_conventional_event_4
#print axioms mismatch_conventional_event_5
#print axioms mismatch_conventional_event_6
#print axioms mismatch_conventional_event_7
#print axioms mismatch_conventional_event_8
#print axioms mismatch_conventional_event_9
#print axioms mismatch_conventional_event_10
#print axioms mismatch_conventional_event_11
#print axioms mismatch_conventional_event_12
#print axioms mismatch_conventional_event_13
#print axioms mismatch_conventional_event_14
#print axioms mismatch_conventional_saved_run
#print axioms mismatch_conventional_core_trace
#print axioms mismatch_conventional_final_whole_account
#print axioms old_report_error_learned_actual_entrance
#print axioms old_report_error_learned_initial_whole_account
#print axioms old_report_error_learned_event_1
#print axioms old_report_error_learned_event_2
#print axioms old_report_error_learned_event_3
#print axioms old_report_error_learned_event_4
#print axioms old_report_error_learned_event_5
#print axioms old_report_error_learned_event_6
#print axioms old_report_error_learned_event_7
#print axioms old_report_error_learned_event_8
#print axioms old_report_error_learned_event_9
#print axioms old_report_error_learned_event_10
#print axioms old_report_error_learned_event_11
#print axioms old_report_error_learned_event_12
#print axioms old_report_error_learned_event_13
#print axioms old_report_error_learned_event_14
#print axioms old_report_error_learned_saved_run
#print axioms old_report_error_learned_core_trace
#print axioms old_report_error_learned_final_whole_account
#print axioms old_report_error_clamped_actual_entrance
#print axioms old_report_error_clamped_initial_whole_account
#print axioms old_report_error_clamped_event_1
#print axioms old_report_error_clamped_event_2
#print axioms old_report_error_clamped_event_3
#print axioms old_report_error_clamped_event_4
#print axioms old_report_error_clamped_event_5
#print axioms old_report_error_clamped_event_6
#print axioms old_report_error_clamped_event_7
#print axioms old_report_error_clamped_event_8
#print axioms old_report_error_clamped_saved_run
#print axioms old_report_error_clamped_core_trace
#print axioms old_report_error_clamped_final_whole_account
#print axioms old_report_error_conventional_actual_entrance
#print axioms old_report_error_conventional_initial_whole_account
#print axioms old_report_error_conventional_event_1
#print axioms old_report_error_conventional_event_2
#print axioms old_report_error_conventional_event_3
#print axioms old_report_error_conventional_event_4
#print axioms old_report_error_conventional_event_5
#print axioms old_report_error_conventional_event_6
#print axioms old_report_error_conventional_event_7
#print axioms old_report_error_conventional_event_8
#print axioms old_report_error_conventional_event_9
#print axioms old_report_error_conventional_event_10
#print axioms old_report_error_conventional_event_11
#print axioms old_report_error_conventional_event_12
#print axioms old_report_error_conventional_event_13
#print axioms old_report_error_conventional_event_14
#print axioms old_report_error_conventional_saved_run
#print axioms old_report_error_conventional_core_trace
#print axioms old_report_error_conventional_final_whole_account
#print axioms positive_bypass_actual_entrance
#print axioms positive_bypass_initial_whole_account
#print axioms positive_bypass_event_1
#print axioms positive_bypass_event_2
#print axioms positive_bypass_event_3
#print axioms positive_bypass_event_4
#print axioms positive_bypass_event_5
#print axioms positive_bypass_event_6
#print axioms positive_bypass_event_7
#print axioms positive_bypass_event_8
#print axioms positive_bypass_saved_run
#print axioms positive_bypass_core_trace
#print axioms positive_bypass_final_whole_account
#print axioms positive_independent_actual_entrance
#print axioms positive_independent_initial_whole_account
#print axioms positive_independent_event_1
#print axioms positive_independent_event_2
#print axioms positive_independent_event_3
#print axioms positive_independent_event_4
#print axioms positive_independent_event_5
#print axioms positive_independent_event_6
#print axioms positive_independent_event_7
#print axioms positive_independent_event_8
#print axioms positive_independent_saved_run
#print axioms positive_independent_core_trace
#print axioms positive_independent_final_whole_account
#print axioms old_false_positive_actual_entrance
#print axioms old_false_positive_initial_whole_account
#print axioms old_false_positive_event_1
#print axioms old_false_positive_event_2
#print axioms old_false_positive_event_3
#print axioms old_false_positive_event_4
#print axioms old_false_positive_event_5
#print axioms old_false_positive_event_6
#print axioms old_false_positive_event_7
#print axioms old_false_positive_event_8
#print axioms old_false_positive_event_9
#print axioms old_false_positive_event_10
#print axioms old_false_positive_event_11
#print axioms old_false_positive_event_12
#print axioms old_false_positive_event_13
#print axioms old_false_positive_event_14
#print axioms old_false_positive_saved_run
#print axioms old_false_positive_core_trace
#print axioms old_false_positive_final_whole_account
#print axioms full_fault_missing_actual_entrance
#print axioms full_fault_missing_initial_whole_account
#print axioms full_fault_missing_event_1
#print axioms full_fault_missing_event_2
#print axioms full_fault_missing_event_3
#print axioms full_fault_missing_event_4
#print axioms full_fault_missing_event_5
#print axioms full_fault_missing_event_6
#print axioms full_fault_missing_event_7
#print axioms full_fault_missing_event_8
#print axioms full_fault_missing_saved_run
#print axioms full_fault_missing_core_trace
#print axioms full_fault_missing_final_whole_account
#print axioms full_fault_flip_actual_entrance
#print axioms full_fault_flip_initial_whole_account
#print axioms full_fault_flip_event_1
#print axioms full_fault_flip_event_2
#print axioms full_fault_flip_event_3
#print axioms full_fault_flip_event_4
#print axioms full_fault_flip_event_5
#print axioms full_fault_flip_event_6
#print axioms full_fault_flip_event_7
#print axioms full_fault_flip_event_8
#print axioms full_fault_flip_saved_run
#print axioms full_fault_flip_core_trace
#print axioms full_fault_flip_final_whole_account
#print axioms full_fault_context_actual_entrance
#print axioms full_fault_context_initial_whole_account
#print axioms full_fault_context_event_1
#print axioms full_fault_context_event_2
#print axioms full_fault_context_event_3
#print axioms full_fault_context_event_4
#print axioms full_fault_context_event_5
#print axioms full_fault_context_event_6
#print axioms full_fault_context_event_7
#print axioms full_fault_context_event_8
#print axioms full_fault_context_saved_run
#print axioms full_fault_context_core_trace
#print axioms full_fault_context_final_whole_account
#print axioms full_fault_setting_actual_entrance
#print axioms full_fault_setting_initial_whole_account
#print axioms full_fault_setting_event_1
#print axioms full_fault_setting_event_2
#print axioms full_fault_setting_event_3
#print axioms full_fault_setting_event_4
#print axioms full_fault_setting_event_5
#print axioms full_fault_setting_event_6
#print axioms full_fault_setting_event_7
#print axioms full_fault_setting_event_8
#print axioms full_fault_setting_saved_run
#print axioms full_fault_setting_core_trace
#print axioms full_fault_setting_final_whole_account
#print axioms weak_fault_missing_actual_entrance
#print axioms weak_fault_missing_initial_whole_account
#print axioms weak_fault_missing_event_1
#print axioms weak_fault_missing_event_2
#print axioms weak_fault_missing_event_3
#print axioms weak_fault_missing_event_4
#print axioms weak_fault_missing_event_5
#print axioms weak_fault_missing_event_6
#print axioms weak_fault_missing_event_7
#print axioms weak_fault_missing_event_8
#print axioms weak_fault_missing_event_9
#print axioms weak_fault_missing_event_10
#print axioms weak_fault_missing_event_11
#print axioms weak_fault_missing_event_12
#print axioms weak_fault_missing_event_13
#print axioms weak_fault_missing_event_14
#print axioms weak_fault_missing_saved_run
#print axioms weak_fault_missing_core_trace
#print axioms weak_fault_missing_final_whole_account
#print axioms weak_fault_flip_actual_entrance
#print axioms weak_fault_flip_initial_whole_account
#print axioms weak_fault_flip_event_1
#print axioms weak_fault_flip_event_2
#print axioms weak_fault_flip_event_3
#print axioms weak_fault_flip_event_4
#print axioms weak_fault_flip_event_5
#print axioms weak_fault_flip_event_6
#print axioms weak_fault_flip_event_7
#print axioms weak_fault_flip_event_8
#print axioms weak_fault_flip_event_9
#print axioms weak_fault_flip_event_10
#print axioms weak_fault_flip_event_11
#print axioms weak_fault_flip_event_12
#print axioms weak_fault_flip_event_13
#print axioms weak_fault_flip_event_14
#print axioms weak_fault_flip_saved_run
#print axioms weak_fault_flip_core_trace
#print axioms weak_fault_flip_final_whole_account
#print axioms weak_fault_context_actual_entrance
#print axioms weak_fault_context_initial_whole_account
#print axioms weak_fault_context_event_1
#print axioms weak_fault_context_event_2
#print axioms weak_fault_context_event_3
#print axioms weak_fault_context_event_4
#print axioms weak_fault_context_event_5
#print axioms weak_fault_context_event_6
#print axioms weak_fault_context_event_7
#print axioms weak_fault_context_event_8
#print axioms weak_fault_context_event_9
#print axioms weak_fault_context_event_10
#print axioms weak_fault_context_event_11
#print axioms weak_fault_context_event_12
#print axioms weak_fault_context_event_13
#print axioms weak_fault_context_event_14
#print axioms weak_fault_context_saved_run
#print axioms weak_fault_context_core_trace
#print axioms weak_fault_context_final_whole_account
#print axioms weak_fault_setting_actual_entrance
#print axioms weak_fault_setting_initial_whole_account
#print axioms weak_fault_setting_event_1
#print axioms weak_fault_setting_event_2
#print axioms weak_fault_setting_event_3
#print axioms weak_fault_setting_event_4
#print axioms weak_fault_setting_event_5
#print axioms weak_fault_setting_event_6
#print axioms weak_fault_setting_event_7
#print axioms weak_fault_setting_event_8
#print axioms weak_fault_setting_event_9
#print axioms weak_fault_setting_event_10
#print axioms weak_fault_setting_event_11
#print axioms weak_fault_setting_event_12
#print axioms weak_fault_setting_event_13
#print axioms weak_fault_setting_event_14
#print axioms weak_fault_setting_saved_run
#print axioms weak_fault_setting_core_trace
#print axioms weak_fault_setting_final_whole_account
#print axioms old_changed_context_actual_entrance
#print axioms old_changed_context_initial_whole_account
#print axioms old_changed_context_event_1
#print axioms old_changed_context_event_2
#print axioms old_changed_context_event_3
#print axioms old_changed_context_event_4
#print axioms old_changed_context_event_5
#print axioms old_changed_context_event_6
#print axioms old_changed_context_event_7
#print axioms old_changed_context_event_8
#print axioms old_changed_context_saved_run
#print axioms old_changed_context_core_trace
#print axioms old_changed_context_final_whole_account
#print axioms old_source_denied_actual_entrance
#print axioms old_source_denied_initial_whole_account
#print axioms old_source_denied_event_1
#print axioms old_source_denied_saved_run
#print axioms old_source_denied_core_trace
#print axioms old_source_denied_final_whole_account
#print axioms wait_one_actual_entrance
#print axioms wait_one_initial_whole_account
#print axioms wait_one_event_1
#print axioms wait_one_event_2
#print axioms wait_one_event_3
#print axioms wait_one_event_4
#print axioms wait_one_event_5
#print axioms wait_one_event_6
#print axioms wait_one_event_7
#print axioms wait_one_event_8
#print axioms wait_one_event_9
#print axioms wait_one_event_10
#print axioms wait_one_event_11
#print axioms wait_one_event_12
#print axioms wait_one_event_13
#print axioms wait_one_event_14
#print axioms wait_one_event_15
#print axioms wait_one_saved_run
#print axioms wait_one_core_trace
#print axioms wait_one_final_whole_account
#print axioms wait_two_actual_entrance
#print axioms wait_two_initial_whole_account
#print axioms wait_two_event_1
#print axioms wait_two_event_2
#print axioms wait_two_event_3
#print axioms wait_two_event_4
#print axioms wait_two_event_5
#print axioms wait_two_event_6
#print axioms wait_two_event_7
#print axioms wait_two_event_8
#print axioms wait_two_event_9
#print axioms wait_two_event_10
#print axioms wait_two_event_11
#print axioms wait_two_event_12
#print axioms wait_two_event_13
#print axioms wait_two_event_14
#print axioms wait_two_saved_run
#print axioms wait_two_core_trace
#print axioms wait_two_final_whole_account
#print axioms wait_three_actual_entrance
#print axioms wait_three_initial_whole_account
#print axioms wait_three_event_1
#print axioms wait_three_event_2
#print axioms wait_three_event_3
#print axioms wait_three_event_4
#print axioms wait_three_event_5
#print axioms wait_three_event_6
#print axioms wait_three_event_7
#print axioms wait_three_event_8
#print axioms wait_three_event_9
#print axioms wait_three_event_10
#print axioms wait_three_event_11
#print axioms wait_three_saved_run
#print axioms wait_three_core_trace
#print axioms wait_three_final_whole_account
end CalibrationRevisionSaved
