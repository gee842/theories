import ConsequenceInquiry

namespace ConsequenceInquirySaved

open RemainingDependency ConsequenceInquiry

set_option maxRecDepth 32768

set_option maxHeartbeats 4000000

def ordinaryConfig : Config := {weak := ⟨false, true⟩, full := ⟨false, true⟩, channels := ⟨.faithful, .faithful⟩, clamp := false}

def ordinary : State := {ancestor := {alphabet := ["a"], initial := 0, controlLocation := "reported_episode_complete", outputs := [true, true, false], transitions := [1, 2, 0], table := [(some false), (some true), none], retained := true, componentDone := true}, config := ordinaryConfig, body := {account := {fuel := 428018, start := 713012, spent := 284994, live := 34, peak := 42, capacity := 256}, stocks := ⟨0, 10, 0⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := true, mode := .serviceIssued, values := ⟨(some false), (some true)⟩, tags := ⟨(some 1), (some 1)⟩, contact := none, candidate := (some true), readMode := (some .selectedRelay), selected := (some true)}}

theorem ordinary_source_zero : ordinary.body.stocks.source = 0 := by decide

def calibrationConfig : Config := {weak := ⟨false, true⟩, full := ⟨false, false⟩, channels := ⟨.faithful, .faithful⟩, clamp := false}

def calibration : State := {ancestor := {alphabet := ["a"], initial := 0, controlLocation := "reported_episode_complete", outputs := [true, true, false], transitions := [1, 2, 0], table := [(some false), (some true), none], retained := true, componentDone := true}, config := calibrationConfig, body := {account := {fuel := 428018, start := 713012, spent := 284994, live := 34, peak := 42, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := true, mode := .serviceIssued, values := ⟨(some false), (some true)⟩, tags := ⟨(some 1), (some 1)⟩, contact := none, candidate := (some true), readMode := (some .selectedRelay), selected := (some true)}}

theorem calibration_source_zero : calibration.body.stocks.source = 0 := by decide

def falseContactConfig : Config := {weak := ⟨false, false⟩, full := ⟨false, false⟩, channels := ⟨.faithful, .flip⟩, clamp := false}

def falseContact : State := {ancestor := {alphabet := ["a"], initial := 0, controlLocation := "reported_episode_complete", outputs := [true, true, false], transitions := [1, 2, 0], table := [(some false), (some true), none], retained := true, componentDone := true}, config := falseContactConfig, body := {account := {fuel := 428018, start := 713012, spent := 284994, live := 34, peak := 42, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := true, mode := .serviceIssued, values := ⟨(some false), (some true)⟩, tags := ⟨(some 1), (some 1)⟩, contact := none, candidate := (some true), readMode := (some .selectedRelay), selected := (some true)}}

theorem falseContact_source_zero : falseContact.body.stocks.source = 0 := by decide

theorem ordinary_calibration_same_view : view ordinary = view calibration := by decide

theorem distinct_actual_outcomes : ordinary.body.stocks.load = 10 ∧ ordinary.body.stocks.waste = 0 ∧ calibration.body.stocks.load = 0 ∧ calibration.body.stocks.waste = 10 := by decide

theorem same_original_account : wholeTotal 8134348 ordinary = 145 * ticks ∧ wholeTotal 8134348 calibration = 145 * ticks := by decide

theorem all_words_preserve_ambiguity : ∀ es : List Event, view (run ordinary es) = view (run calibration es) := by
  intro es
  exact equal_view_runs ordinary calibration es ordinary_source_zero calibration_source_zero ordinary_calibration_same_view

theorem no_correct_view_decoder : ¬ ∃ f : State → Bool, f (view ordinary) = true ∧ f (view calibration) = false := by
  rintro ⟨f, hs, hf⟩
  rw [ordinary_calibration_same_view] at hs
  rw [hs] at hf
  cases hf

def alternateWord : List Event := [.command true, .challenge, .contact false, .write true, .read, .commit, .retain]

def ordinaryAlternate : State := {ancestor := {alphabet := ["a"], initial := 0, controlLocation := "reported_episode_complete", outputs := [true, true, false], transitions := [1, 2, 0], table := [(some false), (some true), none], retained := true, componentDone := true}, config := ordinaryConfig, body := {account := {fuel := 332286, start := 713012, spent := 380726, live := 34, peak := 42, capacity := 256}, stocks := ⟨0, 10, 0⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := true, mode := .selectedRelay, values := ⟨(some false), (some true)⟩, tags := ⟨(some 1), (some 1)⟩, contact := none, candidate := (some true), readMode := (some .selectedRelay), selected := (some true)}}

theorem ordinary_alternate_correspondence : run ordinary alternateWord = ordinaryAlternate := by decide

def calibrationAlternate : State := {ancestor := {alphabet := ["a"], initial := 0, controlLocation := "reported_episode_complete", outputs := [true, true, false], transitions := [1, 2, 0], table := [(some false), (some true), none], retained := true, componentDone := true}, config := calibrationConfig, body := {account := {fuel := 332286, start := 713012, spent := 380726, live := 34, peak := 42, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := true, mode := .selectedRelay, values := ⟨(some false), (some true)⟩, tags := ⟨(some 1), (some 1)⟩, contact := none, candidate := (some true), readMode := (some .selectedRelay), selected := (some true)}}

theorem calibration_alternate_correspondence : run calibration alternateWord = calibrationAlternate := by decide

def falseContactAlternate : State := {ancestor := {alphabet := ["a"], initial := 0, controlLocation := "reported_episode_complete", outputs := [true, true, false], transitions := [1, 2, 0], table := [(some false), (some true), none], retained := true, componentDone := true}, config := falseContactConfig, body := {account := {fuel := 332286, start := 713012, spent := 380726, live := 34, peak := 42, capacity := 256}, stocks := ⟨0, 0, 10⟩, context := 1, relay := true, pending := none, held := false, installed := true, retained := true, mode := .noSupportedRoute, values := ⟨(some false), (some false)⟩, tags := ⟨(some 1), (some 1)⟩, contact := none, candidate := none, readMode := (some .noSupportedRoute), selected := none}}

theorem falseContact_alternate_correspondence : run falseContact alternateWord = falseContactAlternate := by decide

theorem false_contact_still_separated : falseContactAlternate.body.values = ⟨some false, some false⟩ ∧ falseContactAlternate.body.selected = none ∧ calibrationAlternate.body.values = ⟨some false, some true⟩ ∧ calibrationAlternate.body.selected = some true := by decide

end ConsequenceInquirySaved
