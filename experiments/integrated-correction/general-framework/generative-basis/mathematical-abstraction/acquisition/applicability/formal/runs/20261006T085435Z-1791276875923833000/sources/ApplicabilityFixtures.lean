import AcquiredApplicability

namespace ApplicabilityFixtures

open AcquiredApplicability

set_option maxRecDepth 32768

set_option maxHeartbeats 0

-- named:primary_changed

def case0Initial : State := { H := { outputs := [false, false, true], transitions := [1, 2, 0], initial := 0 }, config := { environment := { outputs := [false, false, true], transitions := [1, 2, 0], initial := 0 }, tau := true, sigma := true, brokenReset := false, blocked := false, receiptMode := .faithful, clamp := false, deny := .none }, body := { account := { start := 489849, fuel := 489849, spent := 0, income := 0, live := 15, workspace := 0, peak := 15, capacity := 256 }, physical := { phase := 1, source := 20, transferred := 0, wasted := 0 }, control := { word := 5, base := 23 } } }

def case0Events : List Event := [.install, .prepare, .reset, .advance, .advance, .advance, .advance, .advance, .sense, .checkSensor, .extract, .readReceipt, .commit, .closeRoute, .scan, .select, .prepare, .reset, .sense, .checkSensor, .extract, .readReceipt, .commit, .closeRoute, .retain]

def case0Vectors : List (List Nat) := [[489849, 489849, 0, 0, 15, 0, 15, 256, 1, 20, 0, 0, 5, 0, 0, 0, 23, 0, 0, 0, 0], [489849, 398353, 91496, 0, 32, 0, 40, 256, 1, 20, 0, 0, 5, 0, 1, 0, 23, 0, 0, 0, 3, 0, 1, 2], [489849, 391929, 97920, 0, 32, 8, 40, 256, 1, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 375503, 114346, 0, 32, 8, 42, 256, 0, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 359077, 130772, 0, 32, 8, 42, 256, 1, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 342651, 147198, 0, 32, 8, 42, 256, 2, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 326225, 163624, 0, 32, 8, 42, 256, 0, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 309799, 180050, 0, 32, 8, 42, 256, 1, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 293373, 196476, 0, 32, 8, 42, 256, 2, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 276947, 212902, 0, 32, 8, 42, 256, 2, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 275839, 214010, 0, 32, 8, 42, 256, 2, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 259413, 230436, 0, 32, 8, 42, 256, 2, 10, 0, 10, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 242987, 246862, 0, 32, 8, 42, 256, 2, 10, 0, 10, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 229291, 260558, 0, 31, 8, 48, 256, 2, 10, 0, 10, 5, 1, 3, 0, 23, 2, 2, 1, 2, 1, 2], [489849, 229291, 260558, 0, 31, 0, 48, 256, 2, 10, 0, 10, 5, 1, 3, 0, 23, 2, 2, 1, 2, 1, 2], [489849, 225015, 264834, 0, 31, 0, 48, 256, 2, 10, 0, 10, 5, 1, 3, 0, 23, 2, 2, 1, 2, 1, 2], [489849, 221875, 267974, 0, 26, 0, 48, 256, 2, 10, 0, 10, 0, 1, 4, 0, 23, 2, 2, 1, 2, 1, 2], [489849, 220793, 269056, 0, 26, 3, 48, 256, 2, 10, 0, 10, 0, 1, 2, 0, 23, 1, 2, 1, 2, 1, 2], [489849, 204378, 285471, 0, 26, 3, 48, 256, 0, 10, 0, 10, 0, 1, 2, 0, 23, 1, 2, 1, 2, 1, 2], [489849, 187963, 301886, 0, 26, 3, 48, 256, 0, 10, 0, 10, 0, 1, 2, 0, 23, 1, 2, 1, 2, 1, 2], [489849, 186877, 302972, 0, 26, 3, 48, 256, 0, 10, 0, 10, 0, 1, 2, 0, 23, 1, 2, 1, 2, 1, 2], [489849, 825822, 319387, 655360, 26, 3, 48, 256, 0, 0, 10, 10, 0, 1, 2, 0, 23, 1, 2, 1, 2, 1, 2], [489849, 809407, 335802, 655360, 26, 3, 48, 256, 0, 0, 10, 10, 0, 1, 2, 0, 23, 1, 2, 1, 2, 1, 2], [489849, 798957, 346252, 655360, 25, 3, 48, 256, 0, 0, 10, 10, 0, 2, 3, 0, 23, 1, 1, 2, 1, 1], [489849, 798957, 346252, 655360, 25, 0, 48, 256, 0, 0, 10, 10, 0, 2, 3, 0, 23, 1, 1, 2, 1, 1], [489849, 772283, 372926, 655360, 25, 0, 48, 256, 0, 0, 10, 10, 0, 2, 5, 1, 23, 1, 1, 2, 1, 1]]

def case0Observations : List (List Nat) := [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [2, 0, 0], [2, 0, 0], [2, 0, 0], [2, 1, 0], [2, 1, 0], [2, 1, 0], [2, 1, 0], [2, 1, 0], [0, 0, 0], [0, 0, 0], [1, 0, 0], [1, 0, 0], [1, 0, 1], [1, 2, 1], [1, 2, 1], [1, 2, 1], [1, 2, 1]]

theorem case0Certified : Runnable case0Initial case0Events ∧
    policyWord 100 case0Initial = case0Events ∧
    (history case0Initial case0Events).map vector = case0Vectors ∧
    (history case0Initial case0Events).map (fun s =>
      [optBoolCode s.body.sensor, optBoolCode s.body.receipt, boolCode s.body.actualArrival]) = case0Observations ∧
    (run case0Initial case0Events).body.error = .none ∧
    nextEvent (run case0Initial case0Events) = none := by decide

#print axioms case0Certified

-- named:primary_reader_clamped

def case1Initial : State := { H := { outputs := [false, false, true], transitions := [1, 2, 0], initial := 0 }, config := { environment := { outputs := [false, false, true], transitions := [1, 2, 0], initial := 0 }, tau := true, sigma := true, brokenReset := false, blocked := false, receiptMode := .faithful, clamp := true, deny := .none }, body := { account := { start := 489849, fuel := 489849, spent := 0, income := 0, live := 15, workspace := 0, peak := 15, capacity := 256 }, physical := { phase := 1, source := 20, transferred := 0, wasted := 0 }, control := { word := 5, base := 23 } } }

def case1Events : List Event := [.install, .prepare, .reset, .advance, .advance, .advance, .advance, .advance, .sense, .checkSensor, .extract, .readReceipt, .commit, .closeRoute, .clamp, .prepare, .reset, .advance, .advance, .advance, .advance, .advance, .sense, .checkSensor, .extract, .readReceipt, .commit, .closeRoute, .retain]

def case1Vectors : List (List Nat) := [[489849, 489849, 0, 0, 15, 0, 15, 256, 1, 20, 0, 0, 5, 0, 0, 0, 23, 0, 0, 0, 0], [489849, 398353, 91496, 0, 32, 0, 40, 256, 1, 20, 0, 0, 5, 0, 1, 0, 23, 0, 0, 0, 3, 0, 1, 2], [489849, 391929, 97920, 0, 32, 8, 40, 256, 1, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 375503, 114346, 0, 32, 8, 42, 256, 0, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 359077, 130772, 0, 32, 8, 42, 256, 1, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 342651, 147198, 0, 32, 8, 42, 256, 2, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 326225, 163624, 0, 32, 8, 42, 256, 0, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 309799, 180050, 0, 32, 8, 42, 256, 1, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 293373, 196476, 0, 32, 8, 42, 256, 2, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 276947, 212902, 0, 32, 8, 42, 256, 2, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 275839, 214010, 0, 32, 8, 42, 256, 2, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 259413, 230436, 0, 32, 8, 42, 256, 2, 10, 0, 10, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 242987, 246862, 0, 32, 8, 42, 256, 2, 10, 0, 10, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 229291, 260558, 0, 31, 8, 48, 256, 2, 10, 0, 10, 5, 1, 3, 0, 23, 2, 2, 1, 2, 1, 2], [489849, 229291, 260558, 0, 31, 0, 48, 256, 2, 10, 0, 10, 5, 1, 3, 0, 23, 2, 2, 1, 2, 1, 2], [489849, 222874, 266975, 0, 31, 0, 48, 256, 2, 10, 0, 10, 5, 1, 4, 0, 23, 2, 2, 1, 2, 1, 2], [489849, 216457, 273392, 0, 31, 8, 48, 256, 2, 10, 0, 10, 5, 1, 2, 0, 23, 2, 2, 1, 2, 1, 2], [489849, 200032, 289817, 0, 31, 8, 48, 256, 0, 10, 0, 10, 5, 1, 2, 0, 23, 2, 2, 1, 2, 1, 2], [489849, 183607, 306242, 0, 31, 8, 48, 256, 1, 10, 0, 10, 5, 1, 2, 0, 23, 2, 2, 1, 2, 1, 2], [489849, 167182, 322667, 0, 31, 8, 48, 256, 2, 10, 0, 10, 5, 1, 2, 0, 23, 2, 2, 1, 2, 1, 2], [489849, 150757, 339092, 0, 31, 8, 48, 256, 0, 10, 0, 10, 5, 1, 2, 0, 23, 2, 2, 1, 2, 1, 2], [489849, 134332, 355517, 0, 31, 8, 48, 256, 1, 10, 0, 10, 5, 1, 2, 0, 23, 2, 2, 1, 2, 1, 2], [489849, 117907, 371942, 0, 31, 8, 48, 256, 2, 10, 0, 10, 5, 1, 2, 0, 23, 2, 2, 1, 2, 1, 2], [489849, 101482, 388367, 0, 31, 8, 48, 256, 2, 10, 0, 10, 5, 1, 2, 0, 23, 2, 2, 1, 2, 1, 2], [489849, 100376, 389473, 0, 31, 8, 48, 256, 2, 10, 0, 10, 5, 1, 2, 0, 23, 2, 2, 1, 2, 1, 2], [489849, 83951, 405898, 0, 31, 8, 48, 256, 2, 0, 0, 20, 5, 1, 2, 0, 23, 2, 2, 1, 2, 1, 2], [489849, 67526, 422323, 0, 31, 8, 48, 256, 2, 0, 0, 20, 5, 1, 2, 0, 23, 2, 2, 1, 2, 1, 2], [489849, 55992, 433857, 0, 31, 8, 48, 256, 2, 0, 0, 20, 5, 2, 3, 0, 23, 2, 2, 1, 2, 1, 2], [489849, 55992, 433857, 0, 31, 0, 48, 256, 2, 0, 0, 20, 5, 2, 3, 0, 23, 2, 2, 1, 2, 1, 2], [489849, 23162, 466687, 0, 31, 0, 48, 256, 2, 0, 0, 20, 5, 2, 5, 1, 23, 2, 2, 1, 2, 1, 2]]

def case1Observations : List (List Nat) := [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [2, 0, 0], [2, 0, 0], [2, 0, 0], [2, 1, 0], [2, 1, 0], [2, 1, 0], [2, 1, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [2, 0, 0], [2, 0, 0], [2, 0, 0], [2, 1, 0], [2, 1, 0], [2, 1, 0], [2, 1, 0]]

theorem case1Certified : Runnable case1Initial case1Events ∧
    policyWord 100 case1Initial = case1Events ∧
    (history case1Initial case1Events).map vector = case1Vectors ∧
    (history case1Initial case1Events).map (fun s =>
      [optBoolCode s.body.sensor, optBoolCode s.body.receipt, boolCode s.body.actualArrival]) = case1Observations ∧
    (run case1Initial case1Events).body.error = .none ∧
    nextEvent (run case1Initial case1Events) = none := by decide

#print axioms case1Certified

-- named:stable

def case2Initial : State := { H := { outputs := [false, false, true], transitions := [1, 2, 0], initial := 0 }, config := { environment := { outputs := [false, false, true], transitions := [1, 2, 0], initial := 0 }, tau := false, sigma := false, brokenReset := false, blocked := false, receiptMode := .faithful, clamp := false, deny := .none }, body := { account := { start := 489849, fuel := 489849, spent := 0, income := 0, live := 15, workspace := 0, peak := 15, capacity := 256 }, physical := { phase := 1, source := 20, transferred := 0, wasted := 0 }, control := { word := 5, base := 23 } } }

def case2Events : List Event := [.install, .prepare, .reset, .advance, .advance, .advance, .advance, .advance, .sense, .checkSensor, .extract, .readReceipt, .commit, .closeRoute, .stop, .retain]

def case2Vectors : List (List Nat) := [[489849, 489849, 0, 0, 15, 0, 15, 256, 1, 20, 0, 0, 5, 0, 0, 0, 23, 0, 0, 0, 0], [489849, 398353, 91496, 0, 32, 0, 40, 256, 1, 20, 0, 0, 5, 0, 1, 0, 23, 0, 0, 0, 3, 0, 1, 2], [489849, 391929, 97920, 0, 32, 8, 40, 256, 1, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 375503, 114346, 0, 32, 8, 42, 256, 0, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 359077, 130772, 0, 32, 8, 42, 256, 1, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 342651, 147198, 0, 32, 8, 42, 256, 2, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 326225, 163624, 0, 32, 8, 42, 256, 0, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 309799, 180050, 0, 32, 8, 42, 256, 1, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 293373, 196476, 0, 32, 8, 42, 256, 2, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 276947, 212902, 0, 32, 8, 42, 256, 2, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 275839, 214010, 0, 32, 8, 42, 256, 2, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 914773, 230436, 655360, 32, 8, 42, 256, 2, 10, 10, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 898347, 246862, 655360, 32, 8, 42, 256, 2, 10, 10, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 885675, 259534, 655360, 30, 8, 48, 256, 2, 10, 10, 0, 5, 1, 3, 0, 23, 2, 2, 2, 1, 0], [489849, 885675, 259534, 655360, 30, 0, 48, 256, 2, 10, 10, 0, 5, 1, 3, 0, 23, 2, 2, 2, 1, 0], [489849, 885675, 259534, 655360, 30, 0, 48, 256, 2, 10, 10, 0, 5, 1, 3, 0, 23, 2, 2, 2, 1, 0], [489849, 853871, 291338, 655360, 30, 0, 48, 256, 2, 10, 10, 0, 5, 1, 5, 1, 23, 2, 2, 2, 1, 0]]

def case2Observations : List (List Nat) := [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [2, 0, 0], [2, 0, 0], [2, 0, 1], [2, 2, 1], [2, 2, 1], [2, 2, 1], [2, 2, 1], [2, 2, 1]]

theorem case2Certified : Runnable case2Initial case2Events ∧
    policyWord 100 case2Initial = case2Events ∧
    (history case2Initial case2Events).map vector = case2Vectors ∧
    (history case2Initial case2Events).map (fun s =>
      [optBoolCode s.body.sensor, optBoolCode s.body.receipt, boolCode s.body.actualArrival]) = case2Observations ∧
    (run case2Initial case2Events).body.error = .none ∧
    nextEvent (run case2Initial case2Events) = none := by decide

#print axioms case2Certified

-- named:blocked

def case3Initial : State := { H := { outputs := [false, false, true], transitions := [1, 2, 0], initial := 0 }, config := { environment := { outputs := [false, false, true], transitions := [1, 2, 0], initial := 0 }, tau := false, sigma := false, brokenReset := false, blocked := true, receiptMode := .faithful, clamp := false, deny := .none }, body := { account := { start := 489849, fuel := 489849, spent := 0, income := 0, live := 15, workspace := 0, peak := 15, capacity := 256 }, physical := { phase := 1, source := 20, transferred := 0, wasted := 0 }, control := { word := 5, base := 23 } } }

def case3Events : List Event := [.install, .prepare, .reset, .advance, .advance, .advance, .advance, .advance, .sense, .checkSensor, .extract, .readReceipt, .commit, .closeRoute, .scan, .select, .prepare, .reset, .sense, .checkSensor, .extract, .readReceipt, .commit, .closeRoute, .retain]

def case3Vectors : List (List Nat) := [[489849, 489849, 0, 0, 15, 0, 15, 256, 1, 20, 0, 0, 5, 0, 0, 0, 23, 0, 0, 0, 0], [489849, 398353, 91496, 0, 32, 0, 40, 256, 1, 20, 0, 0, 5, 0, 1, 0, 23, 0, 0, 0, 3, 0, 1, 2], [489849, 391929, 97920, 0, 32, 8, 40, 256, 1, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 375503, 114346, 0, 32, 8, 42, 256, 0, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 359077, 130772, 0, 32, 8, 42, 256, 1, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 342651, 147198, 0, 32, 8, 42, 256, 2, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 326225, 163624, 0, 32, 8, 42, 256, 0, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 309799, 180050, 0, 32, 8, 42, 256, 1, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 293373, 196476, 0, 32, 8, 42, 256, 2, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 276947, 212902, 0, 32, 8, 42, 256, 2, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 275839, 214010, 0, 32, 8, 42, 256, 2, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 259413, 230436, 0, 32, 8, 42, 256, 2, 10, 0, 10, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 242987, 246862, 0, 32, 8, 42, 256, 2, 10, 0, 10, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 229291, 260558, 0, 31, 8, 48, 256, 2, 10, 0, 10, 5, 1, 3, 0, 23, 2, 2, 1, 2, 1, 2], [489849, 229291, 260558, 0, 31, 0, 48, 256, 2, 10, 0, 10, 5, 1, 3, 0, 23, 2, 2, 1, 2, 1, 2], [489849, 225015, 264834, 0, 31, 0, 48, 256, 2, 10, 0, 10, 5, 1, 3, 0, 23, 2, 2, 1, 2, 1, 2], [489849, 221875, 267974, 0, 26, 0, 48, 256, 2, 10, 0, 10, 0, 1, 4, 0, 23, 2, 2, 1, 2, 1, 2], [489849, 220793, 269056, 0, 26, 3, 48, 256, 2, 10, 0, 10, 0, 1, 2, 0, 23, 1, 2, 1, 2, 1, 2], [489849, 204378, 285471, 0, 26, 3, 48, 256, 0, 10, 0, 10, 0, 1, 2, 0, 23, 1, 2, 1, 2, 1, 2], [489849, 187963, 301886, 0, 26, 3, 48, 256, 0, 10, 0, 10, 0, 1, 2, 0, 23, 1, 2, 1, 2, 1, 2], [489849, 186877, 302972, 0, 26, 3, 48, 256, 0, 10, 0, 10, 0, 1, 2, 0, 23, 1, 2, 1, 2, 1, 2], [489849, 170462, 319387, 0, 26, 3, 48, 256, 0, 0, 0, 20, 0, 1, 2, 0, 23, 1, 2, 1, 2, 1, 2], [489849, 154047, 335802, 0, 26, 3, 48, 256, 0, 0, 0, 20, 0, 1, 2, 0, 23, 1, 2, 1, 2, 1, 2], [489849, 143597, 346252, 0, 25, 3, 48, 256, 0, 0, 0, 20, 0, 2, 3, 0, 23, 1, 1, 1, 1, 2], [489849, 143597, 346252, 0, 25, 0, 48, 256, 0, 0, 0, 20, 0, 2, 3, 0, 23, 1, 1, 1, 1, 2], [489849, 116923, 372926, 0, 25, 0, 48, 256, 0, 0, 0, 20, 0, 2, 5, 1, 23, 1, 1, 1, 1, 2]]

def case3Observations : List (List Nat) := [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [2, 0, 0], [2, 0, 0], [2, 0, 0], [2, 1, 0], [2, 1, 0], [2, 1, 0], [2, 1, 0], [2, 1, 0], [0, 0, 0], [0, 0, 0], [1, 0, 0], [1, 0, 0], [1, 0, 0], [1, 1, 0], [1, 1, 0], [1, 1, 0], [1, 1, 0]]

theorem case3Certified : Runnable case3Initial case3Events ∧
    policyWord 100 case3Initial = case3Events ∧
    (history case3Initial case3Events).map vector = case3Vectors ∧
    (history case3Initial case3Events).map (fun s =>
      [optBoolCode s.body.sensor, optBoolCode s.body.receipt, boolCode s.body.actualArrival]) = case3Observations ∧
    (run case3Initial case3Events).body.error = .none ∧
    nextEvent (run case3Initial case3Events) = none := by decide

#print axioms case3Certified

-- named:missing_receipt

def case4Initial : State := { H := { outputs := [false, false, true], transitions := [1, 2, 0], initial := 0 }, config := { environment := { outputs := [false, false, true], transitions := [1, 2, 0], initial := 0 }, tau := true, sigma := true, brokenReset := false, blocked := false, receiptMode := .missing, clamp := false, deny := .none }, body := { account := { start := 489849, fuel := 489849, spent := 0, income := 0, live := 15, workspace := 0, peak := 15, capacity := 256 }, physical := { phase := 1, source := 20, transferred := 0, wasted := 0 }, control := { word := 5, base := 23 } } }

def case4Events : List Event := [.install, .prepare, .reset, .advance, .advance, .advance, .advance, .advance, .sense, .checkSensor, .extract, .readReceipt, .closeRoute]

def case4Vectors : List (List Nat) := [[489849, 489849, 0, 0, 15, 0, 15, 256, 1, 20, 0, 0, 5, 0, 0, 0, 23, 0, 0, 0, 0], [489849, 398353, 91496, 0, 32, 0, 40, 256, 1, 20, 0, 0, 5, 0, 1, 0, 23, 0, 0, 0, 3, 0, 1, 2], [489849, 391929, 97920, 0, 32, 8, 40, 256, 1, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 375503, 114346, 0, 32, 8, 42, 256, 0, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 359077, 130772, 0, 32, 8, 42, 256, 1, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 342651, 147198, 0, 32, 8, 42, 256, 2, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 326225, 163624, 0, 32, 8, 42, 256, 0, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 309799, 180050, 0, 32, 8, 42, 256, 1, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 293373, 196476, 0, 32, 8, 42, 256, 2, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 276947, 212902, 0, 32, 8, 42, 256, 2, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 275839, 214010, 0, 32, 8, 42, 256, 2, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 259413, 230436, 0, 32, 8, 42, 256, 2, 10, 0, 10, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 242987, 246862, 0, 32, 8, 42, 256, 2, 10, 0, 10, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 242987, 246862, 0, 32, 0, 42, 256, 2, 10, 0, 10, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2]]

def case4Observations : List (List Nat) := [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [2, 0, 0], [2, 0, 0], [2, 0, 0], [2, 0, 0], [2, 0, 0]]

theorem case4Certified : Runnable case4Initial case4Events ∧
    policyWord 100 case4Initial = case4Events ∧
    (history case4Initial case4Events).map vector = case4Vectors ∧
    (history case4Initial case4Events).map (fun s =>
      [optBoolCode s.body.sensor, optBoolCode s.body.receipt, boolCode s.body.actualArrival]) = case4Observations ∧
    (run case4Initial case4Events).body.error = .missing ∧
    nextEvent (run case4Initial case4Events) = none := by decide

#print axioms case4Certified

-- named:misleading_receipt

def case5Initial : State := { H := { outputs := [false, false, true], transitions := [1, 2, 0], initial := 0 }, config := { environment := { outputs := [false, false, true], transitions := [1, 2, 0], initial := 0 }, tau := true, sigma := true, brokenReset := false, blocked := false, receiptMode := .complemented, clamp := false, deny := .none }, body := { account := { start := 489849, fuel := 489849, spent := 0, income := 0, live := 15, workspace := 0, peak := 15, capacity := 256 }, physical := { phase := 1, source := 20, transferred := 0, wasted := 0 }, control := { word := 5, base := 23 } } }

def case5Events : List Event := [.install, .prepare, .reset, .advance, .advance, .advance, .advance, .advance, .sense, .checkSensor, .extract, .readReceipt, .commit, .closeRoute, .stop, .retain]

def case5Vectors : List (List Nat) := [[489849, 489849, 0, 0, 15, 0, 15, 256, 1, 20, 0, 0, 5, 0, 0, 0, 23, 0, 0, 0, 0], [489849, 398353, 91496, 0, 32, 0, 40, 256, 1, 20, 0, 0, 5, 0, 1, 0, 23, 0, 0, 0, 3, 0, 1, 2], [489849, 391929, 97920, 0, 32, 8, 40, 256, 1, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 375503, 114346, 0, 32, 8, 42, 256, 0, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 359077, 130772, 0, 32, 8, 42, 256, 1, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 342651, 147198, 0, 32, 8, 42, 256, 2, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 326225, 163624, 0, 32, 8, 42, 256, 0, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 309799, 180050, 0, 32, 8, 42, 256, 1, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 293373, 196476, 0, 32, 8, 42, 256, 2, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 276947, 212902, 0, 32, 8, 42, 256, 2, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 275839, 214010, 0, 32, 8, 42, 256, 2, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 259413, 230436, 0, 32, 8, 42, 256, 2, 10, 0, 10, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 242987, 246862, 0, 32, 8, 42, 256, 2, 10, 0, 10, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 230315, 259534, 0, 30, 8, 48, 256, 2, 10, 0, 10, 5, 1, 3, 0, 23, 2, 2, 2, 1, 0], [489849, 230315, 259534, 0, 30, 0, 48, 256, 2, 10, 0, 10, 5, 1, 3, 0, 23, 2, 2, 2, 1, 0], [489849, 230315, 259534, 0, 30, 0, 48, 256, 2, 10, 0, 10, 5, 1, 3, 0, 23, 2, 2, 2, 1, 0], [489849, 198511, 291338, 0, 30, 0, 48, 256, 2, 10, 0, 10, 5, 1, 5, 1, 23, 2, 2, 2, 1, 0]]

def case5Observations : List (List Nat) := [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [2, 0, 0], [2, 0, 0], [2, 0, 0], [2, 2, 0], [2, 2, 0], [2, 2, 0], [2, 2, 0], [2, 2, 0]]

theorem case5Certified : Runnable case5Initial case5Events ∧
    policyWord 100 case5Initial = case5Events ∧
    (history case5Initial case5Events).map vector = case5Vectors ∧
    (history case5Initial case5Events).map (fun s =>
      [optBoolCode s.body.sensor, optBoolCode s.body.receipt, boolCode s.body.actualArrival]) = case5Observations ∧
    (run case5Initial case5Events).body.error = .none ∧
    nextEvent (run case5Initial case5Events) = none := by decide

#print axioms case5Certified

-- named:interrupted_first_write

def case6Initial : State := { H := { outputs := [false, false, true], transitions := [1, 2, 0], initial := 0 }, config := { environment := { outputs := [false, false, true], transitions := [1, 2, 0], initial := 0 }, tau := true, sigma := true, brokenReset := false, blocked := false, receiptMode := .faithful, clamp := false, deny := .commit }, body := { account := { start := 489849, fuel := 489849, spent := 0, income := 0, live := 15, workspace := 0, peak := 15, capacity := 256 }, physical := { phase := 1, source := 20, transferred := 0, wasted := 0 }, control := { word := 5, base := 23 } } }

def case6Events : List Event := [.install, .prepare, .reset, .advance, .advance, .advance, .advance, .advance, .sense, .checkSensor, .extract, .readReceipt, .commit, .closeRoute]

def case6Vectors : List (List Nat) := [[489849, 489849, 0, 0, 15, 0, 15, 256, 1, 20, 0, 0, 5, 0, 0, 0, 23, 0, 0, 0, 0], [489849, 398353, 91496, 0, 32, 0, 40, 256, 1, 20, 0, 0, 5, 0, 1, 0, 23, 0, 0, 0, 3, 0, 1, 2], [489849, 391929, 97920, 0, 32, 8, 40, 256, 1, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 375503, 114346, 0, 32, 8, 42, 256, 0, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 359077, 130772, 0, 32, 8, 42, 256, 1, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 342651, 147198, 0, 32, 8, 42, 256, 2, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 326225, 163624, 0, 32, 8, 42, 256, 0, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 309799, 180050, 0, 32, 8, 42, 256, 1, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 293373, 196476, 0, 32, 8, 42, 256, 2, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 276947, 212902, 0, 32, 8, 42, 256, 2, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 275839, 214010, 0, 32, 8, 42, 256, 2, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 259413, 230436, 0, 32, 8, 42, 256, 2, 10, 0, 10, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 242987, 246862, 0, 32, 8, 42, 256, 2, 10, 0, 10, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 242987, 246862, 0, 32, 8, 42, 256, 2, 10, 0, 10, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 242987, 246862, 0, 32, 0, 42, 256, 2, 10, 0, 10, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2]]

def case6Observations : List (List Nat) := [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [2, 0, 0], [2, 0, 0], [2, 0, 0], [2, 1, 0], [2, 1, 0], [2, 1, 0]]

theorem case6Certified : Runnable case6Initial case6Events ∧
    policyWord 100 case6Initial = case6Events ∧
    (history case6Initial case6Events).map vector = case6Vectors ∧
    (history case6Initial case6Events).map (fun s =>
      [optBoolCode s.body.sensor, optBoolCode s.body.receipt, boolCode s.body.actualArrival]) = case6Observations ∧
    (run case6Initial case6Events).body.error = .commitDenied ∧
    nextEvent (run case6Initial case6Events) = none := by decide

#print axioms case6Certified

-- named:interrupted_final_retention

def case7Initial : State := { H := { outputs := [false, false, true], transitions := [1, 2, 0], initial := 0 }, config := { environment := { outputs := [false, false, true], transitions := [1, 2, 0], initial := 0 }, tau := true, sigma := true, brokenReset := false, blocked := false, receiptMode := .faithful, clamp := false, deny := .retain }, body := { account := { start := 489849, fuel := 489849, spent := 0, income := 0, live := 15, workspace := 0, peak := 15, capacity := 256 }, physical := { phase := 1, source := 20, transferred := 0, wasted := 0 }, control := { word := 5, base := 23 } } }

def case7Events : List Event := [.install, .prepare, .reset, .advance, .advance, .advance, .advance, .advance, .sense, .checkSensor, .extract, .readReceipt, .commit, .closeRoute, .scan, .select, .prepare, .reset, .sense, .checkSensor, .extract, .readReceipt, .commit, .closeRoute, .retain]

def case7Vectors : List (List Nat) := [[489849, 489849, 0, 0, 15, 0, 15, 256, 1, 20, 0, 0, 5, 0, 0, 0, 23, 0, 0, 0, 0], [489849, 398353, 91496, 0, 32, 0, 40, 256, 1, 20, 0, 0, 5, 0, 1, 0, 23, 0, 0, 0, 3, 0, 1, 2], [489849, 391929, 97920, 0, 32, 8, 40, 256, 1, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 375503, 114346, 0, 32, 8, 42, 256, 0, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 359077, 130772, 0, 32, 8, 42, 256, 1, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 342651, 147198, 0, 32, 8, 42, 256, 2, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 326225, 163624, 0, 32, 8, 42, 256, 0, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 309799, 180050, 0, 32, 8, 42, 256, 1, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 293373, 196476, 0, 32, 8, 42, 256, 2, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 276947, 212902, 0, 32, 8, 42, 256, 2, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 275839, 214010, 0, 32, 8, 42, 256, 2, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 259413, 230436, 0, 32, 8, 42, 256, 2, 10, 0, 10, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 242987, 246862, 0, 32, 8, 42, 256, 2, 10, 0, 10, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 229291, 260558, 0, 31, 8, 48, 256, 2, 10, 0, 10, 5, 1, 3, 0, 23, 2, 2, 1, 2, 1, 2], [489849, 229291, 260558, 0, 31, 0, 48, 256, 2, 10, 0, 10, 5, 1, 3, 0, 23, 2, 2, 1, 2, 1, 2], [489849, 225015, 264834, 0, 31, 0, 48, 256, 2, 10, 0, 10, 5, 1, 3, 0, 23, 2, 2, 1, 2, 1, 2], [489849, 221875, 267974, 0, 26, 0, 48, 256, 2, 10, 0, 10, 0, 1, 4, 0, 23, 2, 2, 1, 2, 1, 2], [489849, 220793, 269056, 0, 26, 3, 48, 256, 2, 10, 0, 10, 0, 1, 2, 0, 23, 1, 2, 1, 2, 1, 2], [489849, 204378, 285471, 0, 26, 3, 48, 256, 0, 10, 0, 10, 0, 1, 2, 0, 23, 1, 2, 1, 2, 1, 2], [489849, 187963, 301886, 0, 26, 3, 48, 256, 0, 10, 0, 10, 0, 1, 2, 0, 23, 1, 2, 1, 2, 1, 2], [489849, 186877, 302972, 0, 26, 3, 48, 256, 0, 10, 0, 10, 0, 1, 2, 0, 23, 1, 2, 1, 2, 1, 2], [489849, 825822, 319387, 655360, 26, 3, 48, 256, 0, 0, 10, 10, 0, 1, 2, 0, 23, 1, 2, 1, 2, 1, 2], [489849, 809407, 335802, 655360, 26, 3, 48, 256, 0, 0, 10, 10, 0, 1, 2, 0, 23, 1, 2, 1, 2, 1, 2], [489849, 798957, 346252, 655360, 25, 3, 48, 256, 0, 0, 10, 10, 0, 2, 3, 0, 23, 1, 1, 2, 1, 1], [489849, 798957, 346252, 655360, 25, 0, 48, 256, 0, 0, 10, 10, 0, 2, 3, 0, 23, 1, 1, 2, 1, 1], [489849, 798957, 346252, 655360, 25, 0, 48, 256, 0, 0, 10, 10, 0, 2, 3, 0, 23, 1, 1, 2, 1, 1]]

def case7Observations : List (List Nat) := [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [2, 0, 0], [2, 0, 0], [2, 0, 0], [2, 1, 0], [2, 1, 0], [2, 1, 0], [2, 1, 0], [2, 1, 0], [0, 0, 0], [0, 0, 0], [1, 0, 0], [1, 0, 0], [1, 0, 1], [1, 2, 1], [1, 2, 1], [1, 2, 1], [1, 2, 1]]

theorem case7Certified : Runnable case7Initial case7Events ∧
    policyWord 100 case7Initial = case7Events ∧
    (history case7Initial case7Events).map vector = case7Vectors ∧
    (history case7Initial case7Events).map (fun s =>
      [optBoolCode s.body.sensor, optBoolCode s.body.receipt, boolCode s.body.actualArrival]) = case7Observations ∧
    (run case7Initial case7Events).body.error = .retentionDenied ∧
    nextEvent (run case7Initial case7Events) = none := by decide

#print axioms case7Certified

-- named:sensor_mismatch

def case8Initial : State := { H := { outputs := [false, false, true], transitions := [1, 2, 0], initial := 0 }, config := { environment := { outputs := [false, false, true], transitions := [1, 2, 0], initial := 0 }, tau := false, sigma := true, brokenReset := false, blocked := false, receiptMode := .faithful, clamp := false, deny := .none }, body := { account := { start := 489849, fuel := 489849, spent := 0, income := 0, live := 15, workspace := 0, peak := 15, capacity := 256 }, physical := { phase := 1, source := 20, transferred := 0, wasted := 0 }, control := { word := 5, base := 23 } } }

def case8Events : List Event := [.install, .prepare, .reset, .advance, .advance, .advance, .advance, .advance, .sense, .checkSensor, .closeRoute]

def case8Vectors : List (List Nat) := [[489849, 489849, 0, 0, 15, 0, 15, 256, 1, 20, 0, 0, 5, 0, 0, 0, 23, 0, 0, 0, 0], [489849, 398353, 91496, 0, 32, 0, 40, 256, 1, 20, 0, 0, 5, 0, 1, 0, 23, 0, 0, 0, 3, 0, 1, 2], [489849, 391929, 97920, 0, 32, 8, 40, 256, 1, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 375503, 114346, 0, 32, 8, 42, 256, 0, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 359077, 130772, 0, 32, 8, 42, 256, 1, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 342651, 147198, 0, 32, 8, 42, 256, 2, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 326225, 163624, 0, 32, 8, 42, 256, 0, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 309799, 180050, 0, 32, 8, 42, 256, 1, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 293373, 196476, 0, 32, 8, 42, 256, 2, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 276947, 212902, 0, 32, 8, 42, 256, 2, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 275839, 214010, 0, 32, 8, 42, 256, 2, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 275839, 214010, 0, 32, 0, 42, 256, 2, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2]]

def case8Observations : List (List Nat) := [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [1, 0, 0], [1, 0, 0], [1, 0, 0]]

theorem case8Certified : Runnable case8Initial case8Events ∧
    policyWord 100 case8Initial = case8Events ∧
    (history case8Initial case8Events).map vector = case8Vectors ∧
    (history case8Initial case8Events).map (fun s =>
      [optBoolCode s.body.sensor, optBoolCode s.body.receipt, boolCode s.body.actualArrival]) = case8Observations ∧
    (run case8Initial case8Events).body.error = .mismatch ∧
    nextEvent (run case8Initial case8Events) = none := by decide

#print axioms case8Certified

-- named:reset_mismatch

def case9Initial : State := { H := { outputs := [false, false, true], transitions := [1, 2, 0], initial := 0 }, config := { environment := { outputs := [false, false, true], transitions := [1, 2, 0], initial := 0 }, tau := true, sigma := true, brokenReset := true, blocked := false, receiptMode := .faithful, clamp := false, deny := .none }, body := { account := { start := 489849, fuel := 489849, spent := 0, income := 0, live := 15, workspace := 0, peak := 15, capacity := 256 }, physical := { phase := 1, source := 20, transferred := 0, wasted := 0 }, control := { word := 5, base := 23 } } }

def case9Events : List Event := [.install, .prepare, .reset, .advance, .advance, .advance, .advance, .advance, .sense, .checkSensor, .closeRoute]

def case9Vectors : List (List Nat) := [[489849, 489849, 0, 0, 15, 0, 15, 256, 1, 20, 0, 0, 5, 0, 0, 0, 23, 0, 0, 0, 0], [489849, 398353, 91496, 0, 32, 0, 40, 256, 1, 20, 0, 0, 5, 0, 1, 0, 23, 0, 0, 0, 3, 0, 1, 2], [489849, 391929, 97920, 0, 32, 8, 40, 256, 1, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 375503, 114346, 0, 32, 8, 42, 256, 1, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 359077, 130772, 0, 32, 8, 42, 256, 2, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 342651, 147198, 0, 32, 8, 42, 256, 0, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 326225, 163624, 0, 32, 8, 42, 256, 1, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 309799, 180050, 0, 32, 8, 42, 256, 2, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 293373, 196476, 0, 32, 8, 42, 256, 0, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 276947, 212902, 0, 32, 8, 42, 256, 0, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 275839, 214010, 0, 32, 8, 42, 256, 0, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 275839, 214010, 0, 32, 0, 42, 256, 0, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2]]

def case9Observations : List (List Nat) := [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [1, 0, 0], [1, 0, 0], [1, 0, 0]]

theorem case9Certified : Runnable case9Initial case9Events ∧
    policyWord 100 case9Initial = case9Events ∧
    (history case9Initial case9Events).map vector = case9Vectors ∧
    (history case9Initial case9Events).map (fun s =>
      [optBoolCode s.body.sensor, optBoolCode s.body.receipt, boolCode s.body.actualArrival]) = case9Observations ∧
    (run case9Initial case9Events).body.error = .mismatch ∧
    nextEvent (run case9Initial case9Events) = none := by decide

#print axioms case9Certified

-- named:outside_family

def case10Initial : State := { H := { outputs := [false, false, true], transitions := [1, 2, 0], initial := 0 }, config := { environment := { outputs := [false, false, false, true], transitions := [1, 2, 3, 0], initial := 0 }, tau := true, sigma := true, brokenReset := false, blocked := false, receiptMode := .faithful, clamp := false, deny := .none }, body := { account := { start := 489849, fuel := 489849, spent := 0, income := 0, live := 15, workspace := 0, peak := 15, capacity := 256 }, physical := { phase := 1, source := 20, transferred := 0, wasted := 0 }, control := { word := 5, base := 23 } } }

def case10Events : List Event := [.install, .prepare, .reset, .advance, .advance, .advance, .advance, .advance, .sense, .checkSensor, .closeRoute]

def case10Vectors : List (List Nat) := [[489849, 489849, 0, 0, 15, 0, 15, 256, 1, 20, 0, 0, 5, 0, 0, 0, 23, 0, 0, 0, 0], [489849, 398353, 91496, 0, 32, 0, 40, 256, 1, 20, 0, 0, 5, 0, 1, 0, 23, 0, 0, 0, 3, 0, 1, 2], [489849, 391929, 97920, 0, 32, 8, 40, 256, 1, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 375503, 114346, 0, 32, 8, 42, 256, 0, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 359077, 130772, 0, 32, 8, 42, 256, 1, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 342651, 147198, 0, 32, 8, 42, 256, 2, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 326225, 163624, 0, 32, 8, 42, 256, 3, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 309799, 180050, 0, 32, 8, 42, 256, 0, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 293373, 196476, 0, 32, 8, 42, 256, 1, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 276947, 212902, 0, 32, 8, 42, 256, 1, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 275839, 214010, 0, 32, 8, 42, 256, 1, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 275839, 214010, 0, 32, 0, 42, 256, 1, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2]]

def case10Observations : List (List Nat) := [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [1, 0, 0], [1, 0, 0], [1, 0, 0]]

theorem case10Certified : Runnable case10Initial case10Events ∧
    policyWord 100 case10Initial = case10Events ∧
    (history case10Initial case10Events).map vector = case10Vectors ∧
    (history case10Initial case10Events).map (fun s =>
      [optBoolCode s.body.sensor, optBoolCode s.body.receipt, boolCode s.body.actualArrival]) = case10Observations ∧
    (run case10Initial case10Events).body.error = .mismatch ∧
    nextEvent (run case10Initial case10Events) = none := by decide

#print axioms case10Certified

-- named:fuel_zero

def case11Initial : State := { H := { outputs := [false, false, true], transitions := [1, 2, 0], initial := 0 }, config := { environment := { outputs := [false, false, true], transitions := [1, 2, 0], initial := 0 }, tau := true, sigma := true, brokenReset := false, blocked := false, receiptMode := .faithful, clamp := false, deny := .none }, body := { account := { start := 0, fuel := 0, spent := 0, income := 0, live := 15, workspace := 0, peak := 15, capacity := 256 }, physical := { phase := 1, source := 20, transferred := 0, wasted := 0 }, control := { word := 5, base := 23 } } }

def case11Events : List Event := [.install]

def case11Vectors : List (List Nat) := [[0, 0, 0, 0, 15, 0, 15, 256, 1, 20, 0, 0, 5, 0, 0, 0, 23, 0, 0, 0, 0], [0, 0, 0, 0, 15, 0, 15, 256, 1, 20, 0, 0, 5, 0, 0, 0, 23, 0, 0, 0, 0]]

def case11Observations : List (List Nat) := [[0, 0, 0], [0, 0, 0]]

theorem case11Certified : Runnable case11Initial case11Events ∧
    policyWord 100 case11Initial = case11Events ∧
    (history case11Initial case11Events).map vector = case11Vectors ∧
    (history case11Initial case11Events).map (fun s =>
      [optBoolCode s.body.sensor, optBoolCode s.body.receipt, boolCode s.body.actualArrival]) = case11Observations ∧
    (run case11Initial case11Events).body.error = .funding ∧
    nextEvent (run case11Initial case11Events) = none := by decide

#print axioms case11Certified

-- named:fuel_three

def case12Initial : State := { H := { outputs := [false, false, true], transitions := [1, 2, 0], initial := 0 }, config := { environment := { outputs := [false, false, true], transitions := [1, 2, 0], initial := 0 }, tau := true, sigma := true, brokenReset := false, blocked := false, receiptMode := .faithful, clamp := false, deny := .none }, body := { account := { start := 196608, fuel := 196608, spent := 0, income := 0, live := 15, workspace := 0, peak := 15, capacity := 256 }, physical := { phase := 1, source := 20, transferred := 0, wasted := 0 }, control := { word := 5, base := 23 } } }

def case12Events : List Event := [.install, .prepare, .reset, .advance, .advance, .advance, .advance, .advance, .sense, .closeRoute]

def case12Vectors : List (List Nat) := [[196608, 196608, 0, 0, 15, 0, 15, 256, 1, 20, 0, 0, 5, 0, 0, 0, 23, 0, 0, 0, 0], [196608, 105112, 91496, 0, 32, 0, 40, 256, 1, 20, 0, 0, 5, 0, 1, 0, 23, 0, 0, 0, 3, 0, 1, 2], [196608, 98688, 97920, 0, 32, 8, 40, 256, 1, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [196608, 82262, 114346, 0, 32, 8, 42, 256, 0, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [196608, 65836, 130772, 0, 32, 8, 42, 256, 1, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [196608, 49410, 147198, 0, 32, 8, 42, 256, 2, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [196608, 32984, 163624, 0, 32, 8, 42, 256, 0, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [196608, 16558, 180050, 0, 32, 8, 42, 256, 1, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [196608, 132, 196476, 0, 32, 8, 42, 256, 2, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [196608, 132, 196476, 0, 32, 8, 42, 256, 2, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [196608, 132, 196476, 0, 32, 0, 42, 256, 2, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2]]

def case12Observations : List (List Nat) := [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]

theorem case12Certified : Runnable case12Initial case12Events ∧
    policyWord 100 case12Initial = case12Events ∧
    (history case12Initial case12Events).map vector = case12Vectors ∧
    (history case12Initial case12Events).map (fun s =>
      [optBoolCode s.body.sensor, optBoolCode s.body.receipt, boolCode s.body.actualArrival]) = case12Observations ∧
    (run case12Initial case12Events).body.error = .funding ∧
    nextEvent (run case12Initial case12Events) = none := by decide

#print axioms case12Certified

-- named:capacity_24

def case13Initial : State := { H := { outputs := [false, false, true], transitions := [1, 2, 0], initial := 0 }, config := { environment := { outputs := [false, false, true], transitions := [1, 2, 0], initial := 0 }, tau := true, sigma := true, brokenReset := false, blocked := false, receiptMode := .faithful, clamp := false, deny := .none }, body := { account := { start := 489849, fuel := 489849, spent := 0, income := 0, live := 15, workspace := 0, peak := 15, capacity := 24 }, physical := { phase := 1, source := 20, transferred := 0, wasted := 0 }, control := { word := 5, base := 23 } } }

def case13Events : List Event := [.install]

def case13Vectors : List (List Nat) := [[489849, 489849, 0, 0, 15, 0, 15, 24, 1, 20, 0, 0, 5, 0, 0, 0, 23, 0, 0, 0, 0], [489849, 489849, 0, 0, 15, 0, 15, 24, 1, 20, 0, 0, 5, 0, 0, 0, 23, 0, 0, 0, 0]]

def case13Observations : List (List Nat) := [[0, 0, 0], [0, 0, 0]]

theorem case13Certified : Runnable case13Initial case13Events ∧
    policyWord 100 case13Initial = case13Events ∧
    (history case13Initial case13Events).map vector = case13Vectors ∧
    (history case13Initial case13Events).map (fun s =>
      [optBoolCode s.body.sensor, optBoolCode s.body.receipt, boolCode s.body.actualArrival]) = case13Observations ∧
    (run case13Initial case13Events).body.error = .capacity ∧
    nextEvent (run case13Initial case13Events) = none := by decide

#print axioms case13Certified

-- named:one_packet

def case14Initial : State := { H := { outputs := [false, false, true], transitions := [1, 2, 0], initial := 0 }, config := { environment := { outputs := [false, false, true], transitions := [1, 2, 0], initial := 0 }, tau := true, sigma := true, brokenReset := false, blocked := false, receiptMode := .faithful, clamp := false, deny := .none }, body := { account := { start := 489849, fuel := 489849, spent := 0, income := 0, live := 15, workspace := 0, peak := 15, capacity := 256 }, physical := { phase := 1, source := 10, transferred := 0, wasted := 0 }, control := { word := 5, base := 23 } } }

def case14Events : List Event := [.install, .prepare, .reset, .advance, .advance, .advance, .advance, .advance, .sense, .checkSensor, .extract, .readReceipt, .commit, .closeRoute, .scan, .select, .prepare, .reset, .sense, .checkSensor, .extract, .closeRoute]

def case14Vectors : List (List Nat) := [[489849, 489849, 0, 0, 15, 0, 15, 256, 1, 10, 0, 0, 5, 0, 0, 0, 23, 0, 0, 0, 0], [489849, 398353, 91496, 0, 32, 0, 40, 256, 1, 10, 0, 0, 5, 0, 1, 0, 23, 0, 0, 0, 3, 0, 1, 2], [489849, 391929, 97920, 0, 32, 8, 40, 256, 1, 10, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 375503, 114346, 0, 32, 8, 42, 256, 0, 10, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 359077, 130772, 0, 32, 8, 42, 256, 1, 10, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 342651, 147198, 0, 32, 8, 42, 256, 2, 10, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 326225, 163624, 0, 32, 8, 42, 256, 0, 10, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 309799, 180050, 0, 32, 8, 42, 256, 1, 10, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 293373, 196476, 0, 32, 8, 42, 256, 2, 10, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 276947, 212902, 0, 32, 8, 42, 256, 2, 10, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 275839, 214010, 0, 32, 8, 42, 256, 2, 10, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 259413, 230436, 0, 32, 8, 42, 256, 2, 0, 0, 10, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 242987, 246862, 0, 32, 8, 42, 256, 2, 0, 0, 10, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 229291, 260558, 0, 31, 8, 48, 256, 2, 0, 0, 10, 5, 1, 3, 0, 23, 2, 2, 1, 2, 1, 2], [489849, 229291, 260558, 0, 31, 0, 48, 256, 2, 0, 0, 10, 5, 1, 3, 0, 23, 2, 2, 1, 2, 1, 2], [489849, 225015, 264834, 0, 31, 0, 48, 256, 2, 0, 0, 10, 5, 1, 3, 0, 23, 2, 2, 1, 2, 1, 2], [489849, 221875, 267974, 0, 26, 0, 48, 256, 2, 0, 0, 10, 0, 1, 4, 0, 23, 2, 2, 1, 2, 1, 2], [489849, 220793, 269056, 0, 26, 3, 48, 256, 2, 0, 0, 10, 0, 1, 2, 0, 23, 1, 2, 1, 2, 1, 2], [489849, 204378, 285471, 0, 26, 3, 48, 256, 0, 0, 0, 10, 0, 1, 2, 0, 23, 1, 2, 1, 2, 1, 2], [489849, 187963, 301886, 0, 26, 3, 48, 256, 0, 0, 0, 10, 0, 1, 2, 0, 23, 1, 2, 1, 2, 1, 2], [489849, 186877, 302972, 0, 26, 3, 48, 256, 0, 0, 0, 10, 0, 1, 2, 0, 23, 1, 2, 1, 2, 1, 2], [489849, 170462, 319387, 0, 26, 3, 48, 256, 0, 0, 0, 10, 0, 1, 2, 0, 23, 1, 2, 1, 2, 1, 2], [489849, 170462, 319387, 0, 26, 0, 48, 256, 0, 0, 0, 10, 0, 1, 2, 0, 23, 1, 2, 1, 2, 1, 2]]

def case14Observations : List (List Nat) := [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [2, 0, 0], [2, 0, 0], [2, 0, 0], [2, 1, 0], [2, 1, 0], [2, 1, 0], [2, 1, 0], [2, 1, 0], [0, 0, 0], [0, 0, 0], [1, 0, 0], [1, 0, 0], [1, 0, 0], [1, 0, 0]]

theorem case14Certified : Runnable case14Initial case14Events ∧
    policyWord 100 case14Initial = case14Events ∧
    (history case14Initial case14Events).map vector = case14Vectors ∧
    (history case14Initial case14Events).map (fun s =>
      [optBoolCode s.body.sensor, optBoolCode s.body.receipt, boolCode s.body.actualArrival]) = case14Observations ∧
    (run case14Initial case14Events).body.error = .source ∧
    nextEvent (run case14Initial case14Events) = none := by decide

#print axioms case14Certified

-- named:source_exhausted

def case15Initial : State := { H := { outputs := [false, false, true], transitions := [1, 2, 0], initial := 0 }, config := { environment := { outputs := [false, false, true], transitions := [1, 2, 0], initial := 0 }, tau := true, sigma := true, brokenReset := false, blocked := false, receiptMode := .faithful, clamp := false, deny := .none }, body := { account := { start := 489849, fuel := 489849, spent := 0, income := 0, live := 15, workspace := 0, peak := 15, capacity := 256 }, physical := { phase := 1, source := 0, transferred := 0, wasted := 0 }, control := { word := 5, base := 23 } } }

def case15Events : List Event := [.install, .prepare, .reset, .advance, .advance, .advance, .advance, .advance, .sense, .checkSensor, .extract, .closeRoute]

def case15Vectors : List (List Nat) := [[489849, 489849, 0, 0, 15, 0, 15, 256, 1, 0, 0, 0, 5, 0, 0, 0, 23, 0, 0, 0, 0], [489849, 398353, 91496, 0, 32, 0, 40, 256, 1, 0, 0, 0, 5, 0, 1, 0, 23, 0, 0, 0, 3, 0, 1, 2], [489849, 391929, 97920, 0, 32, 8, 40, 256, 1, 0, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 375503, 114346, 0, 32, 8, 42, 256, 0, 0, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 359077, 130772, 0, 32, 8, 42, 256, 1, 0, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 342651, 147198, 0, 32, 8, 42, 256, 2, 0, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 326225, 163624, 0, 32, 8, 42, 256, 0, 0, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 309799, 180050, 0, 32, 8, 42, 256, 1, 0, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 293373, 196476, 0, 32, 8, 42, 256, 2, 0, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 276947, 212902, 0, 32, 8, 42, 256, 2, 0, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 275839, 214010, 0, 32, 8, 42, 256, 2, 0, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 259413, 230436, 0, 32, 8, 42, 256, 2, 0, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 259413, 230436, 0, 32, 0, 42, 256, 2, 0, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2]]

def case15Observations : List (List Nat) := [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [2, 0, 0], [2, 0, 0], [2, 0, 0], [2, 0, 0]]

theorem case15Certified : Runnable case15Initial case15Events ∧
    policyWord 100 case15Initial = case15Events ∧
    (history case15Initial case15Events).map vector = case15Vectors ∧
    (history case15Initial case15Events).map (fun s =>
      [optBoolCode s.body.sensor, optBoolCode s.body.receipt, boolCode s.body.actualArrival]) = case15Observations ∧
    (run case15Initial case15Events).body.error = .source ∧
    nextEvent (run case15Initial case15Events) = none := by decide

#print axioms case15Certified

-- named:inverted_prefix

def case16Initial : State := { H := { outputs := [true, true, false], transitions := [1, 2, 0], initial := 0 }, config := { environment := { outputs := [false, false, true], transitions := [1, 2, 0], initial := 0 }, tau := false, sigma := true, brokenReset := false, blocked := false, receiptMode := .faithful, clamp := false, deny := .none }, body := { account := { start := 468871, fuel := 468871, spent := 0, income := 0, live := 15, workspace := 0, peak := 15, capacity := 256 }, physical := { phase := 1, source := 20, transferred := 0, wasted := 0 }, control := { word := 6, base := 23 } } }

def case16Events : List Event := [.install, .prepare, .reset, .advance, .advance, .advance, .advance, .advance, .advance, .sense, .checkSensor, .extract, .readReceipt, .commit, .closeRoute, .scan, .scan, .scan, .select, .prepare, .reset, .advance, .advance, .sense, .checkSensor, .extract, .readReceipt, .commit, .closeRoute, .retain]

def case16Vectors : List (List Nat) := [[468871, 468871, 0, 0, 15, 0, 15, 256, 1, 20, 0, 0, 6, 0, 0, 0, 23, 0, 0, 0, 0], [468871, 376342, 92529, 0, 33, 0, 41, 256, 1, 20, 0, 0, 6, 0, 1, 0, 23, 0, 0, 0, 3, 0, 1, 2], [468871, 368838, 100033, 0, 33, 9, 42, 256, 1, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 352410, 116461, 0, 33, 9, 44, 256, 0, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 335982, 132889, 0, 33, 9, 44, 256, 1, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 319554, 149317, 0, 33, 9, 44, 256, 2, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 303126, 165745, 0, 33, 9, 44, 256, 0, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 286698, 182173, 0, 33, 9, 44, 256, 1, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 270270, 198601, 0, 33, 9, 44, 256, 2, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 253842, 215029, 0, 33, 9, 44, 256, 0, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 237414, 231457, 0, 33, 9, 44, 256, 0, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 236302, 232569, 0, 33, 9, 44, 256, 0, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 219874, 248997, 0, 33, 9, 44, 256, 0, 10, 0, 10, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 203446, 265425, 0, 33, 9, 44, 256, 0, 10, 0, 10, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 189734, 279137, 0, 32, 9, 50, 256, 0, 10, 0, 10, 6, 1, 3, 0, 23, 2, 2, 1, 2, 1, 2], [468871, 189734, 279137, 0, 32, 0, 50, 256, 0, 10, 0, 10, 6, 1, 3, 0, 23, 2, 2, 1, 2, 1, 2], [468871, 185453, 283418, 0, 32, 0, 50, 256, 0, 10, 0, 10, 6, 1, 3, 0, 23, 2, 2, 1, 2, 1, 2], [468871, 179043, 289828, 0, 32, 0, 50, 256, 0, 10, 0, 10, 6, 1, 3, 0, 23, 2, 2, 1, 2, 1, 2], [468871, 170500, 298371, 0, 32, 0, 50, 256, 0, 10, 0, 10, 6, 1, 3, 0, 23, 2, 2, 1, 2, 1, 2], [468871, 163184, 305687, 0, 28, 0, 50, 256, 0, 10, 0, 10, 2, 1, 4, 0, 23, 2, 2, 1, 2, 1, 2], [468871, 159980, 308891, 0, 28, 5, 50, 256, 0, 10, 0, 10, 2, 1, 2, 0, 23, 1, 2, 1, 2, 1, 2], [468871, 143561, 325310, 0, 28, 5, 50, 256, 0, 10, 0, 10, 2, 1, 2, 0, 23, 1, 2, 1, 2, 1, 2], [468871, 127142, 341729, 0, 28, 5, 50, 256, 1, 10, 0, 10, 2, 1, 2, 0, 23, 1, 2, 1, 2, 1, 2], [468871, 110723, 358148, 0, 28, 5, 50, 256, 2, 10, 0, 10, 2, 1, 2, 0, 23, 1, 2, 1, 2, 1, 2], [468871, 94304, 374567, 0, 28, 5, 50, 256, 2, 10, 0, 10, 2, 1, 2, 0, 23, 1, 2, 1, 2, 1, 2], [468871, 93210, 375661, 0, 28, 5, 50, 256, 2, 10, 0, 10, 2, 1, 2, 0, 23, 1, 2, 1, 2, 1, 2], [468871, 732151, 392080, 655360, 28, 5, 50, 256, 2, 0, 10, 10, 2, 1, 2, 0, 23, 1, 2, 1, 2, 1, 2], [468871, 715732, 408499, 655360, 28, 5, 50, 256, 2, 0, 10, 10, 2, 1, 2, 0, 23, 1, 2, 1, 2, 1, 2], [468871, 705258, 418973, 655360, 27, 5, 50, 256, 2, 0, 10, 10, 2, 2, 3, 0, 23, 1, 1, 2, 1, 1], [468871, 705258, 418973, 655360, 27, 0, 50, 256, 2, 0, 10, 10, 2, 2, 3, 0, 23, 1, 1, 2, 1, 1], [468871, 676532, 447699, 655360, 27, 0, 50, 256, 2, 0, 10, 10, 2, 2, 5, 1, 23, 1, 1, 2, 1, 1]]

def case16Observations : List (List Nat) := [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [2, 0, 0], [2, 0, 0], [2, 0, 0], [2, 1, 0], [2, 1, 0], [2, 1, 0], [2, 1, 0], [2, 1, 0], [2, 1, 0], [2, 1, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [1, 0, 0], [1, 0, 0], [1, 0, 1], [1, 2, 1], [1, 2, 1], [1, 2, 1], [1, 2, 1]]

theorem case16Certified : Runnable case16Initial case16Events ∧
    policyWord 100 case16Initial = case16Events ∧
    (history case16Initial case16Events).map vector = case16Vectors ∧
    (history case16Initial case16Events).map (fun s =>
      [optBoolCode s.body.sensor, optBoolCode s.body.receipt, boolCode s.body.actualArrival]) = case16Observations ∧
    (run case16Initial case16Events).body.error = .none ∧
    nextEvent (run case16Initial case16Events) = none := by decide

#print axioms case16Certified

-- grid:0:ordinary

def case17Initial : State := { H := { outputs := [false, false, true], transitions := [1, 2, 0], initial := 0 }, config := { environment := { outputs := [false, false, true], transitions := [1, 2, 0], initial := 0 }, tau := false, sigma := false, brokenReset := false, blocked := false, receiptMode := .faithful, clamp := false, deny := .none }, body := { account := { start := 489849, fuel := 489849, spent := 0, income := 0, live := 15, workspace := 0, peak := 15, capacity := 256 }, physical := { phase := 1, source := 20, transferred := 0, wasted := 0 }, control := { word := 5, base := 23 } } }

def case17Events : List Event := [.install, .prepare, .reset, .advance, .advance, .advance, .advance, .advance, .sense, .checkSensor, .extract, .readReceipt, .commit, .closeRoute, .stop, .retain]

def case17Vectors : List (List Nat) := [[489849, 489849, 0, 0, 15, 0, 15, 256, 1, 20, 0, 0, 5, 0, 0, 0, 23, 0, 0, 0, 0], [489849, 398353, 91496, 0, 32, 0, 40, 256, 1, 20, 0, 0, 5, 0, 1, 0, 23, 0, 0, 0, 3, 0, 1, 2], [489849, 391929, 97920, 0, 32, 8, 40, 256, 1, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 375503, 114346, 0, 32, 8, 42, 256, 0, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 359077, 130772, 0, 32, 8, 42, 256, 1, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 342651, 147198, 0, 32, 8, 42, 256, 2, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 326225, 163624, 0, 32, 8, 42, 256, 0, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 309799, 180050, 0, 32, 8, 42, 256, 1, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 293373, 196476, 0, 32, 8, 42, 256, 2, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 276947, 212902, 0, 32, 8, 42, 256, 2, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 275839, 214010, 0, 32, 8, 42, 256, 2, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 914773, 230436, 655360, 32, 8, 42, 256, 2, 10, 10, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 898347, 246862, 655360, 32, 8, 42, 256, 2, 10, 10, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 885675, 259534, 655360, 30, 8, 48, 256, 2, 10, 10, 0, 5, 1, 3, 0, 23, 2, 2, 2, 1, 0], [489849, 885675, 259534, 655360, 30, 0, 48, 256, 2, 10, 10, 0, 5, 1, 3, 0, 23, 2, 2, 2, 1, 0], [489849, 885675, 259534, 655360, 30, 0, 48, 256, 2, 10, 10, 0, 5, 1, 3, 0, 23, 2, 2, 2, 1, 0], [489849, 853871, 291338, 655360, 30, 0, 48, 256, 2, 10, 10, 0, 5, 1, 5, 1, 23, 2, 2, 2, 1, 0]]

def case17Observations : List (List Nat) := [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [2, 0, 0], [2, 0, 0], [2, 0, 1], [2, 2, 1], [2, 2, 1], [2, 2, 1], [2, 2, 1], [2, 2, 1]]

theorem case17Certified : Runnable case17Initial case17Events ∧
    policyWord 100 case17Initial = case17Events ∧
    (history case17Initial case17Events).map vector = case17Vectors ∧
    (history case17Initial case17Events).map (fun s =>
      [optBoolCode s.body.sensor, optBoolCode s.body.receipt, boolCode s.body.actualArrival]) = case17Observations ∧
    (run case17Initial case17Events).body.error = .none ∧
    nextEvent (run case17Initial case17Events) = none := by decide

#print axioms case17Certified

-- grid:1:ordinary

def case18Initial : State := { H := { outputs := [false, false, true], transitions := [1, 2, 0], initial := 0 }, config := { environment := { outputs := [false, false, true], transitions := [1, 2, 0], initial := 0 }, tau := false, sigma := false, brokenReset := false, blocked := false, receiptMode := .missing, clamp := false, deny := .none }, body := { account := { start := 489849, fuel := 489849, spent := 0, income := 0, live := 15, workspace := 0, peak := 15, capacity := 256 }, physical := { phase := 1, source := 20, transferred := 0, wasted := 0 }, control := { word := 5, base := 23 } } }

def case18Events : List Event := [.install, .prepare, .reset, .advance, .advance, .advance, .advance, .advance, .sense, .checkSensor, .extract, .readReceipt, .closeRoute]

def case18Vectors : List (List Nat) := [[489849, 489849, 0, 0, 15, 0, 15, 256, 1, 20, 0, 0, 5, 0, 0, 0, 23, 0, 0, 0, 0], [489849, 398353, 91496, 0, 32, 0, 40, 256, 1, 20, 0, 0, 5, 0, 1, 0, 23, 0, 0, 0, 3, 0, 1, 2], [489849, 391929, 97920, 0, 32, 8, 40, 256, 1, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 375503, 114346, 0, 32, 8, 42, 256, 0, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 359077, 130772, 0, 32, 8, 42, 256, 1, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 342651, 147198, 0, 32, 8, 42, 256, 2, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 326225, 163624, 0, 32, 8, 42, 256, 0, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 309799, 180050, 0, 32, 8, 42, 256, 1, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 293373, 196476, 0, 32, 8, 42, 256, 2, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 276947, 212902, 0, 32, 8, 42, 256, 2, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 275839, 214010, 0, 32, 8, 42, 256, 2, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 914773, 230436, 655360, 32, 8, 42, 256, 2, 10, 10, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 898347, 246862, 655360, 32, 8, 42, 256, 2, 10, 10, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 898347, 246862, 655360, 32, 0, 42, 256, 2, 10, 10, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2]]

def case18Observations : List (List Nat) := [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [2, 0, 0], [2, 0, 0], [2, 0, 1], [2, 0, 1], [2, 0, 1]]

theorem case18Certified : Runnable case18Initial case18Events ∧
    policyWord 100 case18Initial = case18Events ∧
    (history case18Initial case18Events).map vector = case18Vectors ∧
    (history case18Initial case18Events).map (fun s =>
      [optBoolCode s.body.sensor, optBoolCode s.body.receipt, boolCode s.body.actualArrival]) = case18Observations ∧
    (run case18Initial case18Events).body.error = .missing ∧
    nextEvent (run case18Initial case18Events) = none := by decide

#print axioms case18Certified

-- grid:2:ordinary

def case19Initial : State := { H := { outputs := [false, false, true], transitions := [1, 2, 0], initial := 0 }, config := { environment := { outputs := [false, false, true], transitions := [1, 2, 0], initial := 0 }, tau := false, sigma := false, brokenReset := false, blocked := false, receiptMode := .complemented, clamp := false, deny := .none }, body := { account := { start := 489849, fuel := 489849, spent := 0, income := 0, live := 15, workspace := 0, peak := 15, capacity := 256 }, physical := { phase := 1, source := 20, transferred := 0, wasted := 0 }, control := { word := 5, base := 23 } } }

def case19Events : List Event := [.install, .prepare, .reset, .advance, .advance, .advance, .advance, .advance, .sense, .checkSensor, .extract, .readReceipt, .commit, .closeRoute, .scan, .select, .prepare, .reset, .sense, .checkSensor, .extract, .readReceipt, .commit, .closeRoute, .retain]

def case19Vectors : List (List Nat) := [[489849, 489849, 0, 0, 15, 0, 15, 256, 1, 20, 0, 0, 5, 0, 0, 0, 23, 0, 0, 0, 0], [489849, 398353, 91496, 0, 32, 0, 40, 256, 1, 20, 0, 0, 5, 0, 1, 0, 23, 0, 0, 0, 3, 0, 1, 2], [489849, 391929, 97920, 0, 32, 8, 40, 256, 1, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 375503, 114346, 0, 32, 8, 42, 256, 0, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 359077, 130772, 0, 32, 8, 42, 256, 1, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 342651, 147198, 0, 32, 8, 42, 256, 2, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 326225, 163624, 0, 32, 8, 42, 256, 0, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 309799, 180050, 0, 32, 8, 42, 256, 1, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 293373, 196476, 0, 32, 8, 42, 256, 2, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 276947, 212902, 0, 32, 8, 42, 256, 2, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 275839, 214010, 0, 32, 8, 42, 256, 2, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 914773, 230436, 655360, 32, 8, 42, 256, 2, 10, 10, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 898347, 246862, 655360, 32, 8, 42, 256, 2, 10, 10, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 884651, 260558, 655360, 31, 8, 48, 256, 2, 10, 10, 0, 5, 1, 3, 0, 23, 2, 2, 1, 2, 1, 2], [489849, 884651, 260558, 655360, 31, 0, 48, 256, 2, 10, 10, 0, 5, 1, 3, 0, 23, 2, 2, 1, 2, 1, 2], [489849, 880375, 264834, 655360, 31, 0, 48, 256, 2, 10, 10, 0, 5, 1, 3, 0, 23, 2, 2, 1, 2, 1, 2], [489849, 877235, 267974, 655360, 26, 0, 48, 256, 2, 10, 10, 0, 0, 1, 4, 0, 23, 2, 2, 1, 2, 1, 2], [489849, 876153, 269056, 655360, 26, 3, 48, 256, 2, 10, 10, 0, 0, 1, 2, 0, 23, 1, 2, 1, 2, 1, 2], [489849, 859738, 285471, 655360, 26, 3, 48, 256, 0, 10, 10, 0, 0, 1, 2, 0, 23, 1, 2, 1, 2, 1, 2], [489849, 843323, 301886, 655360, 26, 3, 48, 256, 0, 10, 10, 0, 0, 1, 2, 0, 23, 1, 2, 1, 2, 1, 2], [489849, 842237, 302972, 655360, 26, 3, 48, 256, 0, 10, 10, 0, 0, 1, 2, 0, 23, 1, 2, 1, 2, 1, 2], [489849, 825822, 319387, 655360, 26, 3, 48, 256, 0, 0, 10, 10, 0, 1, 2, 0, 23, 1, 2, 1, 2, 1, 2], [489849, 809407, 335802, 655360, 26, 3, 48, 256, 0, 0, 10, 10, 0, 1, 2, 0, 23, 1, 2, 1, 2, 1, 2], [489849, 798957, 346252, 655360, 25, 3, 48, 256, 0, 0, 10, 10, 0, 2, 3, 0, 23, 1, 1, 2, 1, 1], [489849, 798957, 346252, 655360, 25, 0, 48, 256, 0, 0, 10, 10, 0, 2, 3, 0, 23, 1, 1, 2, 1, 1], [489849, 772283, 372926, 655360, 25, 0, 48, 256, 0, 0, 10, 10, 0, 2, 5, 1, 23, 1, 1, 2, 1, 1]]

def case19Observations : List (List Nat) := [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [2, 0, 0], [2, 0, 0], [2, 0, 1], [2, 1, 1], [2, 1, 1], [2, 1, 1], [2, 1, 1], [2, 1, 1], [0, 0, 1], [0, 0, 1], [1, 0, 1], [1, 0, 1], [1, 0, 0], [1, 2, 0], [1, 2, 0], [1, 2, 0], [1, 2, 0]]

theorem case19Certified : Runnable case19Initial case19Events ∧
    policyWord 100 case19Initial = case19Events ∧
    (history case19Initial case19Events).map vector = case19Vectors ∧
    (history case19Initial case19Events).map (fun s =>
      [optBoolCode s.body.sensor, optBoolCode s.body.receipt, boolCode s.body.actualArrival]) = case19Observations ∧
    (run case19Initial case19Events).body.error = .none ∧
    nextEvent (run case19Initial case19Events) = none := by decide

#print axioms case19Certified

-- grid:3:ordinary

def case20Initial : State := { H := { outputs := [false, false, true], transitions := [1, 2, 0], initial := 0 }, config := { environment := { outputs := [false, false, true], transitions := [1, 2, 0], initial := 0 }, tau := false, sigma := false, brokenReset := false, blocked := true, receiptMode := .faithful, clamp := false, deny := .none }, body := { account := { start := 489849, fuel := 489849, spent := 0, income := 0, live := 15, workspace := 0, peak := 15, capacity := 256 }, physical := { phase := 1, source := 20, transferred := 0, wasted := 0 }, control := { word := 5, base := 23 } } }

def case20Events : List Event := [.install, .prepare, .reset, .advance, .advance, .advance, .advance, .advance, .sense, .checkSensor, .extract, .readReceipt, .commit, .closeRoute, .scan, .select, .prepare, .reset, .sense, .checkSensor, .extract, .readReceipt, .commit, .closeRoute, .retain]

def case20Vectors : List (List Nat) := [[489849, 489849, 0, 0, 15, 0, 15, 256, 1, 20, 0, 0, 5, 0, 0, 0, 23, 0, 0, 0, 0], [489849, 398353, 91496, 0, 32, 0, 40, 256, 1, 20, 0, 0, 5, 0, 1, 0, 23, 0, 0, 0, 3, 0, 1, 2], [489849, 391929, 97920, 0, 32, 8, 40, 256, 1, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 375503, 114346, 0, 32, 8, 42, 256, 0, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 359077, 130772, 0, 32, 8, 42, 256, 1, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 342651, 147198, 0, 32, 8, 42, 256, 2, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 326225, 163624, 0, 32, 8, 42, 256, 0, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 309799, 180050, 0, 32, 8, 42, 256, 1, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 293373, 196476, 0, 32, 8, 42, 256, 2, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 276947, 212902, 0, 32, 8, 42, 256, 2, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 275839, 214010, 0, 32, 8, 42, 256, 2, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 259413, 230436, 0, 32, 8, 42, 256, 2, 10, 0, 10, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 242987, 246862, 0, 32, 8, 42, 256, 2, 10, 0, 10, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 229291, 260558, 0, 31, 8, 48, 256, 2, 10, 0, 10, 5, 1, 3, 0, 23, 2, 2, 1, 2, 1, 2], [489849, 229291, 260558, 0, 31, 0, 48, 256, 2, 10, 0, 10, 5, 1, 3, 0, 23, 2, 2, 1, 2, 1, 2], [489849, 225015, 264834, 0, 31, 0, 48, 256, 2, 10, 0, 10, 5, 1, 3, 0, 23, 2, 2, 1, 2, 1, 2], [489849, 221875, 267974, 0, 26, 0, 48, 256, 2, 10, 0, 10, 0, 1, 4, 0, 23, 2, 2, 1, 2, 1, 2], [489849, 220793, 269056, 0, 26, 3, 48, 256, 2, 10, 0, 10, 0, 1, 2, 0, 23, 1, 2, 1, 2, 1, 2], [489849, 204378, 285471, 0, 26, 3, 48, 256, 0, 10, 0, 10, 0, 1, 2, 0, 23, 1, 2, 1, 2, 1, 2], [489849, 187963, 301886, 0, 26, 3, 48, 256, 0, 10, 0, 10, 0, 1, 2, 0, 23, 1, 2, 1, 2, 1, 2], [489849, 186877, 302972, 0, 26, 3, 48, 256, 0, 10, 0, 10, 0, 1, 2, 0, 23, 1, 2, 1, 2, 1, 2], [489849, 170462, 319387, 0, 26, 3, 48, 256, 0, 0, 0, 20, 0, 1, 2, 0, 23, 1, 2, 1, 2, 1, 2], [489849, 154047, 335802, 0, 26, 3, 48, 256, 0, 0, 0, 20, 0, 1, 2, 0, 23, 1, 2, 1, 2, 1, 2], [489849, 143597, 346252, 0, 25, 3, 48, 256, 0, 0, 0, 20, 0, 2, 3, 0, 23, 1, 1, 1, 1, 2], [489849, 143597, 346252, 0, 25, 0, 48, 256, 0, 0, 0, 20, 0, 2, 3, 0, 23, 1, 1, 1, 1, 2], [489849, 116923, 372926, 0, 25, 0, 48, 256, 0, 0, 0, 20, 0, 2, 5, 1, 23, 1, 1, 1, 1, 2]]

def case20Observations : List (List Nat) := [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [2, 0, 0], [2, 0, 0], [2, 0, 0], [2, 1, 0], [2, 1, 0], [2, 1, 0], [2, 1, 0], [2, 1, 0], [0, 0, 0], [0, 0, 0], [1, 0, 0], [1, 0, 0], [1, 0, 0], [1, 1, 0], [1, 1, 0], [1, 1, 0], [1, 1, 0]]

theorem case20Certified : Runnable case20Initial case20Events ∧
    policyWord 100 case20Initial = case20Events ∧
    (history case20Initial case20Events).map vector = case20Vectors ∧
    (history case20Initial case20Events).map (fun s =>
      [optBoolCode s.body.sensor, optBoolCode s.body.receipt, boolCode s.body.actualArrival]) = case20Observations ∧
    (run case20Initial case20Events).body.error = .none ∧
    nextEvent (run case20Initial case20Events) = none := by decide

#print axioms case20Certified

-- grid:4:ordinary

def case21Initial : State := { H := { outputs := [false, false, true], transitions := [1, 2, 0], initial := 0 }, config := { environment := { outputs := [false, false, true], transitions := [1, 2, 0], initial := 0 }, tau := false, sigma := false, brokenReset := false, blocked := true, receiptMode := .missing, clamp := false, deny := .none }, body := { account := { start := 489849, fuel := 489849, spent := 0, income := 0, live := 15, workspace := 0, peak := 15, capacity := 256 }, physical := { phase := 1, source := 20, transferred := 0, wasted := 0 }, control := { word := 5, base := 23 } } }

def case21Events : List Event := [.install, .prepare, .reset, .advance, .advance, .advance, .advance, .advance, .sense, .checkSensor, .extract, .readReceipt, .closeRoute]

def case21Vectors : List (List Nat) := [[489849, 489849, 0, 0, 15, 0, 15, 256, 1, 20, 0, 0, 5, 0, 0, 0, 23, 0, 0, 0, 0], [489849, 398353, 91496, 0, 32, 0, 40, 256, 1, 20, 0, 0, 5, 0, 1, 0, 23, 0, 0, 0, 3, 0, 1, 2], [489849, 391929, 97920, 0, 32, 8, 40, 256, 1, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 375503, 114346, 0, 32, 8, 42, 256, 0, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 359077, 130772, 0, 32, 8, 42, 256, 1, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 342651, 147198, 0, 32, 8, 42, 256, 2, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 326225, 163624, 0, 32, 8, 42, 256, 0, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 309799, 180050, 0, 32, 8, 42, 256, 1, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 293373, 196476, 0, 32, 8, 42, 256, 2, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 276947, 212902, 0, 32, 8, 42, 256, 2, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 275839, 214010, 0, 32, 8, 42, 256, 2, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 259413, 230436, 0, 32, 8, 42, 256, 2, 10, 0, 10, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 242987, 246862, 0, 32, 8, 42, 256, 2, 10, 0, 10, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 242987, 246862, 0, 32, 0, 42, 256, 2, 10, 0, 10, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2]]

def case21Observations : List (List Nat) := [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [2, 0, 0], [2, 0, 0], [2, 0, 0], [2, 0, 0], [2, 0, 0]]

theorem case21Certified : Runnable case21Initial case21Events ∧
    policyWord 100 case21Initial = case21Events ∧
    (history case21Initial case21Events).map vector = case21Vectors ∧
    (history case21Initial case21Events).map (fun s =>
      [optBoolCode s.body.sensor, optBoolCode s.body.receipt, boolCode s.body.actualArrival]) = case21Observations ∧
    (run case21Initial case21Events).body.error = .missing ∧
    nextEvent (run case21Initial case21Events) = none := by decide

#print axioms case21Certified

-- grid:5:ordinary

def case22Initial : State := { H := { outputs := [false, false, true], transitions := [1, 2, 0], initial := 0 }, config := { environment := { outputs := [false, false, true], transitions := [1, 2, 0], initial := 0 }, tau := false, sigma := false, brokenReset := false, blocked := true, receiptMode := .complemented, clamp := false, deny := .none }, body := { account := { start := 489849, fuel := 489849, spent := 0, income := 0, live := 15, workspace := 0, peak := 15, capacity := 256 }, physical := { phase := 1, source := 20, transferred := 0, wasted := 0 }, control := { word := 5, base := 23 } } }

def case22Events : List Event := [.install, .prepare, .reset, .advance, .advance, .advance, .advance, .advance, .sense, .checkSensor, .extract, .readReceipt, .commit, .closeRoute, .stop, .retain]

def case22Vectors : List (List Nat) := [[489849, 489849, 0, 0, 15, 0, 15, 256, 1, 20, 0, 0, 5, 0, 0, 0, 23, 0, 0, 0, 0], [489849, 398353, 91496, 0, 32, 0, 40, 256, 1, 20, 0, 0, 5, 0, 1, 0, 23, 0, 0, 0, 3, 0, 1, 2], [489849, 391929, 97920, 0, 32, 8, 40, 256, 1, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 375503, 114346, 0, 32, 8, 42, 256, 0, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 359077, 130772, 0, 32, 8, 42, 256, 1, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 342651, 147198, 0, 32, 8, 42, 256, 2, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 326225, 163624, 0, 32, 8, 42, 256, 0, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 309799, 180050, 0, 32, 8, 42, 256, 1, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 293373, 196476, 0, 32, 8, 42, 256, 2, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 276947, 212902, 0, 32, 8, 42, 256, 2, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 275839, 214010, 0, 32, 8, 42, 256, 2, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 259413, 230436, 0, 32, 8, 42, 256, 2, 10, 0, 10, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 242987, 246862, 0, 32, 8, 42, 256, 2, 10, 0, 10, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 230315, 259534, 0, 30, 8, 48, 256, 2, 10, 0, 10, 5, 1, 3, 0, 23, 2, 2, 2, 1, 0], [489849, 230315, 259534, 0, 30, 0, 48, 256, 2, 10, 0, 10, 5, 1, 3, 0, 23, 2, 2, 2, 1, 0], [489849, 230315, 259534, 0, 30, 0, 48, 256, 2, 10, 0, 10, 5, 1, 3, 0, 23, 2, 2, 2, 1, 0], [489849, 198511, 291338, 0, 30, 0, 48, 256, 2, 10, 0, 10, 5, 1, 5, 1, 23, 2, 2, 2, 1, 0]]

def case22Observations : List (List Nat) := [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [2, 0, 0], [2, 0, 0], [2, 0, 0], [2, 2, 0], [2, 2, 0], [2, 2, 0], [2, 2, 0], [2, 2, 0]]

theorem case22Certified : Runnable case22Initial case22Events ∧
    policyWord 100 case22Initial = case22Events ∧
    (history case22Initial case22Events).map vector = case22Vectors ∧
    (history case22Initial case22Events).map (fun s =>
      [optBoolCode s.body.sensor, optBoolCode s.body.receipt, boolCode s.body.actualArrival]) = case22Observations ∧
    (run case22Initial case22Events).body.error = .none ∧
    nextEvent (run case22Initial case22Events) = none := by decide

#print axioms case22Certified

-- grid:6:ordinary

def case23Initial : State := { H := { outputs := [false, false, true], transitions := [1, 2, 0], initial := 0 }, config := { environment := { outputs := [false, false, true], transitions := [1, 2, 0], initial := 0 }, tau := false, sigma := true, brokenReset := false, blocked := false, receiptMode := .faithful, clamp := false, deny := .none }, body := { account := { start := 489849, fuel := 489849, spent := 0, income := 0, live := 15, workspace := 0, peak := 15, capacity := 256 }, physical := { phase := 1, source := 20, transferred := 0, wasted := 0 }, control := { word := 5, base := 23 } } }

def case23Events : List Event := [.install, .prepare, .reset, .advance, .advance, .advance, .advance, .advance, .sense, .checkSensor, .closeRoute]

def case23Vectors : List (List Nat) := [[489849, 489849, 0, 0, 15, 0, 15, 256, 1, 20, 0, 0, 5, 0, 0, 0, 23, 0, 0, 0, 0], [489849, 398353, 91496, 0, 32, 0, 40, 256, 1, 20, 0, 0, 5, 0, 1, 0, 23, 0, 0, 0, 3, 0, 1, 2], [489849, 391929, 97920, 0, 32, 8, 40, 256, 1, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 375503, 114346, 0, 32, 8, 42, 256, 0, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 359077, 130772, 0, 32, 8, 42, 256, 1, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 342651, 147198, 0, 32, 8, 42, 256, 2, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 326225, 163624, 0, 32, 8, 42, 256, 0, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 309799, 180050, 0, 32, 8, 42, 256, 1, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 293373, 196476, 0, 32, 8, 42, 256, 2, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 276947, 212902, 0, 32, 8, 42, 256, 2, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 275839, 214010, 0, 32, 8, 42, 256, 2, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 275839, 214010, 0, 32, 0, 42, 256, 2, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2]]

def case23Observations : List (List Nat) := [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [1, 0, 0], [1, 0, 0], [1, 0, 0]]

theorem case23Certified : Runnable case23Initial case23Events ∧
    policyWord 100 case23Initial = case23Events ∧
    (history case23Initial case23Events).map vector = case23Vectors ∧
    (history case23Initial case23Events).map (fun s =>
      [optBoolCode s.body.sensor, optBoolCode s.body.receipt, boolCode s.body.actualArrival]) = case23Observations ∧
    (run case23Initial case23Events).body.error = .mismatch ∧
    nextEvent (run case23Initial case23Events) = none := by decide

#print axioms case23Certified

-- grid:7:ordinary

def case24Initial : State := { H := { outputs := [false, false, true], transitions := [1, 2, 0], initial := 0 }, config := { environment := { outputs := [false, false, true], transitions := [1, 2, 0], initial := 0 }, tau := false, sigma := true, brokenReset := false, blocked := false, receiptMode := .missing, clamp := false, deny := .none }, body := { account := { start := 489849, fuel := 489849, spent := 0, income := 0, live := 15, workspace := 0, peak := 15, capacity := 256 }, physical := { phase := 1, source := 20, transferred := 0, wasted := 0 }, control := { word := 5, base := 23 } } }

def case24Events : List Event := [.install, .prepare, .reset, .advance, .advance, .advance, .advance, .advance, .sense, .checkSensor, .closeRoute]

def case24Vectors : List (List Nat) := [[489849, 489849, 0, 0, 15, 0, 15, 256, 1, 20, 0, 0, 5, 0, 0, 0, 23, 0, 0, 0, 0], [489849, 398353, 91496, 0, 32, 0, 40, 256, 1, 20, 0, 0, 5, 0, 1, 0, 23, 0, 0, 0, 3, 0, 1, 2], [489849, 391929, 97920, 0, 32, 8, 40, 256, 1, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 375503, 114346, 0, 32, 8, 42, 256, 0, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 359077, 130772, 0, 32, 8, 42, 256, 1, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 342651, 147198, 0, 32, 8, 42, 256, 2, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 326225, 163624, 0, 32, 8, 42, 256, 0, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 309799, 180050, 0, 32, 8, 42, 256, 1, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 293373, 196476, 0, 32, 8, 42, 256, 2, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 276947, 212902, 0, 32, 8, 42, 256, 2, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 275839, 214010, 0, 32, 8, 42, 256, 2, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 275839, 214010, 0, 32, 0, 42, 256, 2, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2]]

def case24Observations : List (List Nat) := [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [1, 0, 0], [1, 0, 0], [1, 0, 0]]

theorem case24Certified : Runnable case24Initial case24Events ∧
    policyWord 100 case24Initial = case24Events ∧
    (history case24Initial case24Events).map vector = case24Vectors ∧
    (history case24Initial case24Events).map (fun s =>
      [optBoolCode s.body.sensor, optBoolCode s.body.receipt, boolCode s.body.actualArrival]) = case24Observations ∧
    (run case24Initial case24Events).body.error = .mismatch ∧
    nextEvent (run case24Initial case24Events) = none := by decide

#print axioms case24Certified

-- grid:8:ordinary

def case25Initial : State := { H := { outputs := [false, false, true], transitions := [1, 2, 0], initial := 0 }, config := { environment := { outputs := [false, false, true], transitions := [1, 2, 0], initial := 0 }, tau := false, sigma := true, brokenReset := false, blocked := false, receiptMode := .complemented, clamp := false, deny := .none }, body := { account := { start := 489849, fuel := 489849, spent := 0, income := 0, live := 15, workspace := 0, peak := 15, capacity := 256 }, physical := { phase := 1, source := 20, transferred := 0, wasted := 0 }, control := { word := 5, base := 23 } } }

def case25Events : List Event := [.install, .prepare, .reset, .advance, .advance, .advance, .advance, .advance, .sense, .checkSensor, .closeRoute]

def case25Vectors : List (List Nat) := [[489849, 489849, 0, 0, 15, 0, 15, 256, 1, 20, 0, 0, 5, 0, 0, 0, 23, 0, 0, 0, 0], [489849, 398353, 91496, 0, 32, 0, 40, 256, 1, 20, 0, 0, 5, 0, 1, 0, 23, 0, 0, 0, 3, 0, 1, 2], [489849, 391929, 97920, 0, 32, 8, 40, 256, 1, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 375503, 114346, 0, 32, 8, 42, 256, 0, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 359077, 130772, 0, 32, 8, 42, 256, 1, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 342651, 147198, 0, 32, 8, 42, 256, 2, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 326225, 163624, 0, 32, 8, 42, 256, 0, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 309799, 180050, 0, 32, 8, 42, 256, 1, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 293373, 196476, 0, 32, 8, 42, 256, 2, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 276947, 212902, 0, 32, 8, 42, 256, 2, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 275839, 214010, 0, 32, 8, 42, 256, 2, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 275839, 214010, 0, 32, 0, 42, 256, 2, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2]]

def case25Observations : List (List Nat) := [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [1, 0, 0], [1, 0, 0], [1, 0, 0]]

theorem case25Certified : Runnable case25Initial case25Events ∧
    policyWord 100 case25Initial = case25Events ∧
    (history case25Initial case25Events).map vector = case25Vectors ∧
    (history case25Initial case25Events).map (fun s =>
      [optBoolCode s.body.sensor, optBoolCode s.body.receipt, boolCode s.body.actualArrival]) = case25Observations ∧
    (run case25Initial case25Events).body.error = .mismatch ∧
    nextEvent (run case25Initial case25Events) = none := by decide

#print axioms case25Certified

-- grid:9:ordinary

def case26Initial : State := { H := { outputs := [false, false, true], transitions := [1, 2, 0], initial := 0 }, config := { environment := { outputs := [false, false, true], transitions := [1, 2, 0], initial := 0 }, tau := false, sigma := true, brokenReset := false, blocked := true, receiptMode := .faithful, clamp := false, deny := .none }, body := { account := { start := 489849, fuel := 489849, spent := 0, income := 0, live := 15, workspace := 0, peak := 15, capacity := 256 }, physical := { phase := 1, source := 20, transferred := 0, wasted := 0 }, control := { word := 5, base := 23 } } }

def case26Events : List Event := [.install, .prepare, .reset, .advance, .advance, .advance, .advance, .advance, .sense, .checkSensor, .closeRoute]

def case26Vectors : List (List Nat) := [[489849, 489849, 0, 0, 15, 0, 15, 256, 1, 20, 0, 0, 5, 0, 0, 0, 23, 0, 0, 0, 0], [489849, 398353, 91496, 0, 32, 0, 40, 256, 1, 20, 0, 0, 5, 0, 1, 0, 23, 0, 0, 0, 3, 0, 1, 2], [489849, 391929, 97920, 0, 32, 8, 40, 256, 1, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 375503, 114346, 0, 32, 8, 42, 256, 0, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 359077, 130772, 0, 32, 8, 42, 256, 1, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 342651, 147198, 0, 32, 8, 42, 256, 2, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 326225, 163624, 0, 32, 8, 42, 256, 0, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 309799, 180050, 0, 32, 8, 42, 256, 1, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 293373, 196476, 0, 32, 8, 42, 256, 2, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 276947, 212902, 0, 32, 8, 42, 256, 2, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 275839, 214010, 0, 32, 8, 42, 256, 2, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 275839, 214010, 0, 32, 0, 42, 256, 2, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2]]

def case26Observations : List (List Nat) := [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [1, 0, 0], [1, 0, 0], [1, 0, 0]]

theorem case26Certified : Runnable case26Initial case26Events ∧
    policyWord 100 case26Initial = case26Events ∧
    (history case26Initial case26Events).map vector = case26Vectors ∧
    (history case26Initial case26Events).map (fun s =>
      [optBoolCode s.body.sensor, optBoolCode s.body.receipt, boolCode s.body.actualArrival]) = case26Observations ∧
    (run case26Initial case26Events).body.error = .mismatch ∧
    nextEvent (run case26Initial case26Events) = none := by decide

#print axioms case26Certified

-- grid:10:ordinary

def case27Initial : State := { H := { outputs := [false, false, true], transitions := [1, 2, 0], initial := 0 }, config := { environment := { outputs := [false, false, true], transitions := [1, 2, 0], initial := 0 }, tau := false, sigma := true, brokenReset := false, blocked := true, receiptMode := .missing, clamp := false, deny := .none }, body := { account := { start := 489849, fuel := 489849, spent := 0, income := 0, live := 15, workspace := 0, peak := 15, capacity := 256 }, physical := { phase := 1, source := 20, transferred := 0, wasted := 0 }, control := { word := 5, base := 23 } } }

def case27Events : List Event := [.install, .prepare, .reset, .advance, .advance, .advance, .advance, .advance, .sense, .checkSensor, .closeRoute]

def case27Vectors : List (List Nat) := [[489849, 489849, 0, 0, 15, 0, 15, 256, 1, 20, 0, 0, 5, 0, 0, 0, 23, 0, 0, 0, 0], [489849, 398353, 91496, 0, 32, 0, 40, 256, 1, 20, 0, 0, 5, 0, 1, 0, 23, 0, 0, 0, 3, 0, 1, 2], [489849, 391929, 97920, 0, 32, 8, 40, 256, 1, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 375503, 114346, 0, 32, 8, 42, 256, 0, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 359077, 130772, 0, 32, 8, 42, 256, 1, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 342651, 147198, 0, 32, 8, 42, 256, 2, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 326225, 163624, 0, 32, 8, 42, 256, 0, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 309799, 180050, 0, 32, 8, 42, 256, 1, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 293373, 196476, 0, 32, 8, 42, 256, 2, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 276947, 212902, 0, 32, 8, 42, 256, 2, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 275839, 214010, 0, 32, 8, 42, 256, 2, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 275839, 214010, 0, 32, 0, 42, 256, 2, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2]]

def case27Observations : List (List Nat) := [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [1, 0, 0], [1, 0, 0], [1, 0, 0]]

theorem case27Certified : Runnable case27Initial case27Events ∧
    policyWord 100 case27Initial = case27Events ∧
    (history case27Initial case27Events).map vector = case27Vectors ∧
    (history case27Initial case27Events).map (fun s =>
      [optBoolCode s.body.sensor, optBoolCode s.body.receipt, boolCode s.body.actualArrival]) = case27Observations ∧
    (run case27Initial case27Events).body.error = .mismatch ∧
    nextEvent (run case27Initial case27Events) = none := by decide

#print axioms case27Certified

-- grid:11:ordinary

def case28Initial : State := { H := { outputs := [false, false, true], transitions := [1, 2, 0], initial := 0 }, config := { environment := { outputs := [false, false, true], transitions := [1, 2, 0], initial := 0 }, tau := false, sigma := true, brokenReset := false, blocked := true, receiptMode := .complemented, clamp := false, deny := .none }, body := { account := { start := 489849, fuel := 489849, spent := 0, income := 0, live := 15, workspace := 0, peak := 15, capacity := 256 }, physical := { phase := 1, source := 20, transferred := 0, wasted := 0 }, control := { word := 5, base := 23 } } }

def case28Events : List Event := [.install, .prepare, .reset, .advance, .advance, .advance, .advance, .advance, .sense, .checkSensor, .closeRoute]

def case28Vectors : List (List Nat) := [[489849, 489849, 0, 0, 15, 0, 15, 256, 1, 20, 0, 0, 5, 0, 0, 0, 23, 0, 0, 0, 0], [489849, 398353, 91496, 0, 32, 0, 40, 256, 1, 20, 0, 0, 5, 0, 1, 0, 23, 0, 0, 0, 3, 0, 1, 2], [489849, 391929, 97920, 0, 32, 8, 40, 256, 1, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 375503, 114346, 0, 32, 8, 42, 256, 0, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 359077, 130772, 0, 32, 8, 42, 256, 1, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 342651, 147198, 0, 32, 8, 42, 256, 2, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 326225, 163624, 0, 32, 8, 42, 256, 0, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 309799, 180050, 0, 32, 8, 42, 256, 1, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 293373, 196476, 0, 32, 8, 42, 256, 2, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 276947, 212902, 0, 32, 8, 42, 256, 2, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 275839, 214010, 0, 32, 8, 42, 256, 2, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 275839, 214010, 0, 32, 0, 42, 256, 2, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2]]

def case28Observations : List (List Nat) := [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [1, 0, 0], [1, 0, 0], [1, 0, 0]]

theorem case28Certified : Runnable case28Initial case28Events ∧
    policyWord 100 case28Initial = case28Events ∧
    (history case28Initial case28Events).map vector = case28Vectors ∧
    (history case28Initial case28Events).map (fun s =>
      [optBoolCode s.body.sensor, optBoolCode s.body.receipt, boolCode s.body.actualArrival]) = case28Observations ∧
    (run case28Initial case28Events).body.error = .mismatch ∧
    nextEvent (run case28Initial case28Events) = none := by decide

#print axioms case28Certified

-- grid:12:ordinary

def case29Initial : State := { H := { outputs := [false, false, true], transitions := [1, 2, 0], initial := 0 }, config := { environment := { outputs := [false, false, true], transitions := [1, 2, 0], initial := 0 }, tau := true, sigma := false, brokenReset := false, blocked := false, receiptMode := .faithful, clamp := false, deny := .none }, body := { account := { start := 489849, fuel := 489849, spent := 0, income := 0, live := 15, workspace := 0, peak := 15, capacity := 256 }, physical := { phase := 1, source := 20, transferred := 0, wasted := 0 }, control := { word := 5, base := 23 } } }

def case29Events : List Event := [.install, .prepare, .reset, .advance, .advance, .advance, .advance, .advance, .sense, .checkSensor, .closeRoute]

def case29Vectors : List (List Nat) := [[489849, 489849, 0, 0, 15, 0, 15, 256, 1, 20, 0, 0, 5, 0, 0, 0, 23, 0, 0, 0, 0], [489849, 398353, 91496, 0, 32, 0, 40, 256, 1, 20, 0, 0, 5, 0, 1, 0, 23, 0, 0, 0, 3, 0, 1, 2], [489849, 391929, 97920, 0, 32, 8, 40, 256, 1, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 375503, 114346, 0, 32, 8, 42, 256, 0, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 359077, 130772, 0, 32, 8, 42, 256, 1, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 342651, 147198, 0, 32, 8, 42, 256, 2, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 326225, 163624, 0, 32, 8, 42, 256, 0, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 309799, 180050, 0, 32, 8, 42, 256, 1, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 293373, 196476, 0, 32, 8, 42, 256, 2, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 276947, 212902, 0, 32, 8, 42, 256, 2, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 275839, 214010, 0, 32, 8, 42, 256, 2, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 275839, 214010, 0, 32, 0, 42, 256, 2, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2]]

def case29Observations : List (List Nat) := [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [1, 0, 0], [1, 0, 0], [1, 0, 0]]

theorem case29Certified : Runnable case29Initial case29Events ∧
    policyWord 100 case29Initial = case29Events ∧
    (history case29Initial case29Events).map vector = case29Vectors ∧
    (history case29Initial case29Events).map (fun s =>
      [optBoolCode s.body.sensor, optBoolCode s.body.receipt, boolCode s.body.actualArrival]) = case29Observations ∧
    (run case29Initial case29Events).body.error = .mismatch ∧
    nextEvent (run case29Initial case29Events) = none := by decide

#print axioms case29Certified

-- grid:13:ordinary

def case30Initial : State := { H := { outputs := [false, false, true], transitions := [1, 2, 0], initial := 0 }, config := { environment := { outputs := [false, false, true], transitions := [1, 2, 0], initial := 0 }, tau := true, sigma := false, brokenReset := false, blocked := false, receiptMode := .missing, clamp := false, deny := .none }, body := { account := { start := 489849, fuel := 489849, spent := 0, income := 0, live := 15, workspace := 0, peak := 15, capacity := 256 }, physical := { phase := 1, source := 20, transferred := 0, wasted := 0 }, control := { word := 5, base := 23 } } }

def case30Events : List Event := [.install, .prepare, .reset, .advance, .advance, .advance, .advance, .advance, .sense, .checkSensor, .closeRoute]

def case30Vectors : List (List Nat) := [[489849, 489849, 0, 0, 15, 0, 15, 256, 1, 20, 0, 0, 5, 0, 0, 0, 23, 0, 0, 0, 0], [489849, 398353, 91496, 0, 32, 0, 40, 256, 1, 20, 0, 0, 5, 0, 1, 0, 23, 0, 0, 0, 3, 0, 1, 2], [489849, 391929, 97920, 0, 32, 8, 40, 256, 1, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 375503, 114346, 0, 32, 8, 42, 256, 0, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 359077, 130772, 0, 32, 8, 42, 256, 1, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 342651, 147198, 0, 32, 8, 42, 256, 2, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 326225, 163624, 0, 32, 8, 42, 256, 0, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 309799, 180050, 0, 32, 8, 42, 256, 1, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 293373, 196476, 0, 32, 8, 42, 256, 2, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 276947, 212902, 0, 32, 8, 42, 256, 2, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 275839, 214010, 0, 32, 8, 42, 256, 2, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 275839, 214010, 0, 32, 0, 42, 256, 2, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2]]

def case30Observations : List (List Nat) := [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [1, 0, 0], [1, 0, 0], [1, 0, 0]]

theorem case30Certified : Runnable case30Initial case30Events ∧
    policyWord 100 case30Initial = case30Events ∧
    (history case30Initial case30Events).map vector = case30Vectors ∧
    (history case30Initial case30Events).map (fun s =>
      [optBoolCode s.body.sensor, optBoolCode s.body.receipt, boolCode s.body.actualArrival]) = case30Observations ∧
    (run case30Initial case30Events).body.error = .mismatch ∧
    nextEvent (run case30Initial case30Events) = none := by decide

#print axioms case30Certified

-- grid:14:ordinary

def case31Initial : State := { H := { outputs := [false, false, true], transitions := [1, 2, 0], initial := 0 }, config := { environment := { outputs := [false, false, true], transitions := [1, 2, 0], initial := 0 }, tau := true, sigma := false, brokenReset := false, blocked := false, receiptMode := .complemented, clamp := false, deny := .none }, body := { account := { start := 489849, fuel := 489849, spent := 0, income := 0, live := 15, workspace := 0, peak := 15, capacity := 256 }, physical := { phase := 1, source := 20, transferred := 0, wasted := 0 }, control := { word := 5, base := 23 } } }

def case31Events : List Event := [.install, .prepare, .reset, .advance, .advance, .advance, .advance, .advance, .sense, .checkSensor, .closeRoute]

def case31Vectors : List (List Nat) := [[489849, 489849, 0, 0, 15, 0, 15, 256, 1, 20, 0, 0, 5, 0, 0, 0, 23, 0, 0, 0, 0], [489849, 398353, 91496, 0, 32, 0, 40, 256, 1, 20, 0, 0, 5, 0, 1, 0, 23, 0, 0, 0, 3, 0, 1, 2], [489849, 391929, 97920, 0, 32, 8, 40, 256, 1, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 375503, 114346, 0, 32, 8, 42, 256, 0, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 359077, 130772, 0, 32, 8, 42, 256, 1, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 342651, 147198, 0, 32, 8, 42, 256, 2, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 326225, 163624, 0, 32, 8, 42, 256, 0, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 309799, 180050, 0, 32, 8, 42, 256, 1, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 293373, 196476, 0, 32, 8, 42, 256, 2, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 276947, 212902, 0, 32, 8, 42, 256, 2, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 275839, 214010, 0, 32, 8, 42, 256, 2, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 275839, 214010, 0, 32, 0, 42, 256, 2, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2]]

def case31Observations : List (List Nat) := [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [1, 0, 0], [1, 0, 0], [1, 0, 0]]

theorem case31Certified : Runnable case31Initial case31Events ∧
    policyWord 100 case31Initial = case31Events ∧
    (history case31Initial case31Events).map vector = case31Vectors ∧
    (history case31Initial case31Events).map (fun s =>
      [optBoolCode s.body.sensor, optBoolCode s.body.receipt, boolCode s.body.actualArrival]) = case31Observations ∧
    (run case31Initial case31Events).body.error = .mismatch ∧
    nextEvent (run case31Initial case31Events) = none := by decide

#print axioms case31Certified

-- grid:15:ordinary

def case32Initial : State := { H := { outputs := [false, false, true], transitions := [1, 2, 0], initial := 0 }, config := { environment := { outputs := [false, false, true], transitions := [1, 2, 0], initial := 0 }, tau := true, sigma := false, brokenReset := false, blocked := true, receiptMode := .faithful, clamp := false, deny := .none }, body := { account := { start := 489849, fuel := 489849, spent := 0, income := 0, live := 15, workspace := 0, peak := 15, capacity := 256 }, physical := { phase := 1, source := 20, transferred := 0, wasted := 0 }, control := { word := 5, base := 23 } } }

def case32Events : List Event := [.install, .prepare, .reset, .advance, .advance, .advance, .advance, .advance, .sense, .checkSensor, .closeRoute]

def case32Vectors : List (List Nat) := [[489849, 489849, 0, 0, 15, 0, 15, 256, 1, 20, 0, 0, 5, 0, 0, 0, 23, 0, 0, 0, 0], [489849, 398353, 91496, 0, 32, 0, 40, 256, 1, 20, 0, 0, 5, 0, 1, 0, 23, 0, 0, 0, 3, 0, 1, 2], [489849, 391929, 97920, 0, 32, 8, 40, 256, 1, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 375503, 114346, 0, 32, 8, 42, 256, 0, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 359077, 130772, 0, 32, 8, 42, 256, 1, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 342651, 147198, 0, 32, 8, 42, 256, 2, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 326225, 163624, 0, 32, 8, 42, 256, 0, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 309799, 180050, 0, 32, 8, 42, 256, 1, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 293373, 196476, 0, 32, 8, 42, 256, 2, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 276947, 212902, 0, 32, 8, 42, 256, 2, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 275839, 214010, 0, 32, 8, 42, 256, 2, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 275839, 214010, 0, 32, 0, 42, 256, 2, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2]]

def case32Observations : List (List Nat) := [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [1, 0, 0], [1, 0, 0], [1, 0, 0]]

theorem case32Certified : Runnable case32Initial case32Events ∧
    policyWord 100 case32Initial = case32Events ∧
    (history case32Initial case32Events).map vector = case32Vectors ∧
    (history case32Initial case32Events).map (fun s =>
      [optBoolCode s.body.sensor, optBoolCode s.body.receipt, boolCode s.body.actualArrival]) = case32Observations ∧
    (run case32Initial case32Events).body.error = .mismatch ∧
    nextEvent (run case32Initial case32Events) = none := by decide

#print axioms case32Certified

-- grid:16:ordinary

def case33Initial : State := { H := { outputs := [false, false, true], transitions := [1, 2, 0], initial := 0 }, config := { environment := { outputs := [false, false, true], transitions := [1, 2, 0], initial := 0 }, tau := true, sigma := false, brokenReset := false, blocked := true, receiptMode := .missing, clamp := false, deny := .none }, body := { account := { start := 489849, fuel := 489849, spent := 0, income := 0, live := 15, workspace := 0, peak := 15, capacity := 256 }, physical := { phase := 1, source := 20, transferred := 0, wasted := 0 }, control := { word := 5, base := 23 } } }

def case33Events : List Event := [.install, .prepare, .reset, .advance, .advance, .advance, .advance, .advance, .sense, .checkSensor, .closeRoute]

def case33Vectors : List (List Nat) := [[489849, 489849, 0, 0, 15, 0, 15, 256, 1, 20, 0, 0, 5, 0, 0, 0, 23, 0, 0, 0, 0], [489849, 398353, 91496, 0, 32, 0, 40, 256, 1, 20, 0, 0, 5, 0, 1, 0, 23, 0, 0, 0, 3, 0, 1, 2], [489849, 391929, 97920, 0, 32, 8, 40, 256, 1, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 375503, 114346, 0, 32, 8, 42, 256, 0, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 359077, 130772, 0, 32, 8, 42, 256, 1, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 342651, 147198, 0, 32, 8, 42, 256, 2, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 326225, 163624, 0, 32, 8, 42, 256, 0, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 309799, 180050, 0, 32, 8, 42, 256, 1, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 293373, 196476, 0, 32, 8, 42, 256, 2, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 276947, 212902, 0, 32, 8, 42, 256, 2, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 275839, 214010, 0, 32, 8, 42, 256, 2, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 275839, 214010, 0, 32, 0, 42, 256, 2, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2]]

def case33Observations : List (List Nat) := [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [1, 0, 0], [1, 0, 0], [1, 0, 0]]

theorem case33Certified : Runnable case33Initial case33Events ∧
    policyWord 100 case33Initial = case33Events ∧
    (history case33Initial case33Events).map vector = case33Vectors ∧
    (history case33Initial case33Events).map (fun s =>
      [optBoolCode s.body.sensor, optBoolCode s.body.receipt, boolCode s.body.actualArrival]) = case33Observations ∧
    (run case33Initial case33Events).body.error = .mismatch ∧
    nextEvent (run case33Initial case33Events) = none := by decide

#print axioms case33Certified

-- grid:17:ordinary

def case34Initial : State := { H := { outputs := [false, false, true], transitions := [1, 2, 0], initial := 0 }, config := { environment := { outputs := [false, false, true], transitions := [1, 2, 0], initial := 0 }, tau := true, sigma := false, brokenReset := false, blocked := true, receiptMode := .complemented, clamp := false, deny := .none }, body := { account := { start := 489849, fuel := 489849, spent := 0, income := 0, live := 15, workspace := 0, peak := 15, capacity := 256 }, physical := { phase := 1, source := 20, transferred := 0, wasted := 0 }, control := { word := 5, base := 23 } } }

def case34Events : List Event := [.install, .prepare, .reset, .advance, .advance, .advance, .advance, .advance, .sense, .checkSensor, .closeRoute]

def case34Vectors : List (List Nat) := [[489849, 489849, 0, 0, 15, 0, 15, 256, 1, 20, 0, 0, 5, 0, 0, 0, 23, 0, 0, 0, 0], [489849, 398353, 91496, 0, 32, 0, 40, 256, 1, 20, 0, 0, 5, 0, 1, 0, 23, 0, 0, 0, 3, 0, 1, 2], [489849, 391929, 97920, 0, 32, 8, 40, 256, 1, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 375503, 114346, 0, 32, 8, 42, 256, 0, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 359077, 130772, 0, 32, 8, 42, 256, 1, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 342651, 147198, 0, 32, 8, 42, 256, 2, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 326225, 163624, 0, 32, 8, 42, 256, 0, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 309799, 180050, 0, 32, 8, 42, 256, 1, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 293373, 196476, 0, 32, 8, 42, 256, 2, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 276947, 212902, 0, 32, 8, 42, 256, 2, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 275839, 214010, 0, 32, 8, 42, 256, 2, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 275839, 214010, 0, 32, 0, 42, 256, 2, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2]]

def case34Observations : List (List Nat) := [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [1, 0, 0], [1, 0, 0], [1, 0, 0]]

theorem case34Certified : Runnable case34Initial case34Events ∧
    policyWord 100 case34Initial = case34Events ∧
    (history case34Initial case34Events).map vector = case34Vectors ∧
    (history case34Initial case34Events).map (fun s =>
      [optBoolCode s.body.sensor, optBoolCode s.body.receipt, boolCode s.body.actualArrival]) = case34Observations ∧
    (run case34Initial case34Events).body.error = .mismatch ∧
    nextEvent (run case34Initial case34Events) = none := by decide

#print axioms case34Certified

-- grid:18:ordinary

def case35Initial : State := { H := { outputs := [false, false, true], transitions := [1, 2, 0], initial := 0 }, config := { environment := { outputs := [false, false, true], transitions := [1, 2, 0], initial := 0 }, tau := true, sigma := true, brokenReset := false, blocked := false, receiptMode := .faithful, clamp := false, deny := .none }, body := { account := { start := 489849, fuel := 489849, spent := 0, income := 0, live := 15, workspace := 0, peak := 15, capacity := 256 }, physical := { phase := 1, source := 20, transferred := 0, wasted := 0 }, control := { word := 5, base := 23 } } }

def case35Events : List Event := [.install, .prepare, .reset, .advance, .advance, .advance, .advance, .advance, .sense, .checkSensor, .extract, .readReceipt, .commit, .closeRoute, .scan, .select, .prepare, .reset, .sense, .checkSensor, .extract, .readReceipt, .commit, .closeRoute, .retain]

def case35Vectors : List (List Nat) := [[489849, 489849, 0, 0, 15, 0, 15, 256, 1, 20, 0, 0, 5, 0, 0, 0, 23, 0, 0, 0, 0], [489849, 398353, 91496, 0, 32, 0, 40, 256, 1, 20, 0, 0, 5, 0, 1, 0, 23, 0, 0, 0, 3, 0, 1, 2], [489849, 391929, 97920, 0, 32, 8, 40, 256, 1, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 375503, 114346, 0, 32, 8, 42, 256, 0, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 359077, 130772, 0, 32, 8, 42, 256, 1, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 342651, 147198, 0, 32, 8, 42, 256, 2, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 326225, 163624, 0, 32, 8, 42, 256, 0, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 309799, 180050, 0, 32, 8, 42, 256, 1, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 293373, 196476, 0, 32, 8, 42, 256, 2, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 276947, 212902, 0, 32, 8, 42, 256, 2, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 275839, 214010, 0, 32, 8, 42, 256, 2, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 259413, 230436, 0, 32, 8, 42, 256, 2, 10, 0, 10, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 242987, 246862, 0, 32, 8, 42, 256, 2, 10, 0, 10, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 229291, 260558, 0, 31, 8, 48, 256, 2, 10, 0, 10, 5, 1, 3, 0, 23, 2, 2, 1, 2, 1, 2], [489849, 229291, 260558, 0, 31, 0, 48, 256, 2, 10, 0, 10, 5, 1, 3, 0, 23, 2, 2, 1, 2, 1, 2], [489849, 225015, 264834, 0, 31, 0, 48, 256, 2, 10, 0, 10, 5, 1, 3, 0, 23, 2, 2, 1, 2, 1, 2], [489849, 221875, 267974, 0, 26, 0, 48, 256, 2, 10, 0, 10, 0, 1, 4, 0, 23, 2, 2, 1, 2, 1, 2], [489849, 220793, 269056, 0, 26, 3, 48, 256, 2, 10, 0, 10, 0, 1, 2, 0, 23, 1, 2, 1, 2, 1, 2], [489849, 204378, 285471, 0, 26, 3, 48, 256, 0, 10, 0, 10, 0, 1, 2, 0, 23, 1, 2, 1, 2, 1, 2], [489849, 187963, 301886, 0, 26, 3, 48, 256, 0, 10, 0, 10, 0, 1, 2, 0, 23, 1, 2, 1, 2, 1, 2], [489849, 186877, 302972, 0, 26, 3, 48, 256, 0, 10, 0, 10, 0, 1, 2, 0, 23, 1, 2, 1, 2, 1, 2], [489849, 825822, 319387, 655360, 26, 3, 48, 256, 0, 0, 10, 10, 0, 1, 2, 0, 23, 1, 2, 1, 2, 1, 2], [489849, 809407, 335802, 655360, 26, 3, 48, 256, 0, 0, 10, 10, 0, 1, 2, 0, 23, 1, 2, 1, 2, 1, 2], [489849, 798957, 346252, 655360, 25, 3, 48, 256, 0, 0, 10, 10, 0, 2, 3, 0, 23, 1, 1, 2, 1, 1], [489849, 798957, 346252, 655360, 25, 0, 48, 256, 0, 0, 10, 10, 0, 2, 3, 0, 23, 1, 1, 2, 1, 1], [489849, 772283, 372926, 655360, 25, 0, 48, 256, 0, 0, 10, 10, 0, 2, 5, 1, 23, 1, 1, 2, 1, 1]]

def case35Observations : List (List Nat) := [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [2, 0, 0], [2, 0, 0], [2, 0, 0], [2, 1, 0], [2, 1, 0], [2, 1, 0], [2, 1, 0], [2, 1, 0], [0, 0, 0], [0, 0, 0], [1, 0, 0], [1, 0, 0], [1, 0, 1], [1, 2, 1], [1, 2, 1], [1, 2, 1], [1, 2, 1]]

theorem case35Certified : Runnable case35Initial case35Events ∧
    policyWord 100 case35Initial = case35Events ∧
    (history case35Initial case35Events).map vector = case35Vectors ∧
    (history case35Initial case35Events).map (fun s =>
      [optBoolCode s.body.sensor, optBoolCode s.body.receipt, boolCode s.body.actualArrival]) = case35Observations ∧
    (run case35Initial case35Events).body.error = .none ∧
    nextEvent (run case35Initial case35Events) = none := by decide

#print axioms case35Certified

-- grid:19:ordinary

def case36Initial : State := { H := { outputs := [false, false, true], transitions := [1, 2, 0], initial := 0 }, config := { environment := { outputs := [false, false, true], transitions := [1, 2, 0], initial := 0 }, tau := true, sigma := true, brokenReset := false, blocked := false, receiptMode := .missing, clamp := false, deny := .none }, body := { account := { start := 489849, fuel := 489849, spent := 0, income := 0, live := 15, workspace := 0, peak := 15, capacity := 256 }, physical := { phase := 1, source := 20, transferred := 0, wasted := 0 }, control := { word := 5, base := 23 } } }

def case36Events : List Event := [.install, .prepare, .reset, .advance, .advance, .advance, .advance, .advance, .sense, .checkSensor, .extract, .readReceipt, .closeRoute]

def case36Vectors : List (List Nat) := [[489849, 489849, 0, 0, 15, 0, 15, 256, 1, 20, 0, 0, 5, 0, 0, 0, 23, 0, 0, 0, 0], [489849, 398353, 91496, 0, 32, 0, 40, 256, 1, 20, 0, 0, 5, 0, 1, 0, 23, 0, 0, 0, 3, 0, 1, 2], [489849, 391929, 97920, 0, 32, 8, 40, 256, 1, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 375503, 114346, 0, 32, 8, 42, 256, 0, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 359077, 130772, 0, 32, 8, 42, 256, 1, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 342651, 147198, 0, 32, 8, 42, 256, 2, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 326225, 163624, 0, 32, 8, 42, 256, 0, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 309799, 180050, 0, 32, 8, 42, 256, 1, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 293373, 196476, 0, 32, 8, 42, 256, 2, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 276947, 212902, 0, 32, 8, 42, 256, 2, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 275839, 214010, 0, 32, 8, 42, 256, 2, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 259413, 230436, 0, 32, 8, 42, 256, 2, 10, 0, 10, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 242987, 246862, 0, 32, 8, 42, 256, 2, 10, 0, 10, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 242987, 246862, 0, 32, 0, 42, 256, 2, 10, 0, 10, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2]]

def case36Observations : List (List Nat) := [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [2, 0, 0], [2, 0, 0], [2, 0, 0], [2, 0, 0], [2, 0, 0]]

theorem case36Certified : Runnable case36Initial case36Events ∧
    policyWord 100 case36Initial = case36Events ∧
    (history case36Initial case36Events).map vector = case36Vectors ∧
    (history case36Initial case36Events).map (fun s =>
      [optBoolCode s.body.sensor, optBoolCode s.body.receipt, boolCode s.body.actualArrival]) = case36Observations ∧
    (run case36Initial case36Events).body.error = .missing ∧
    nextEvent (run case36Initial case36Events) = none := by decide

#print axioms case36Certified

-- grid:20:ordinary

def case37Initial : State := { H := { outputs := [false, false, true], transitions := [1, 2, 0], initial := 0 }, config := { environment := { outputs := [false, false, true], transitions := [1, 2, 0], initial := 0 }, tau := true, sigma := true, brokenReset := false, blocked := false, receiptMode := .complemented, clamp := false, deny := .none }, body := { account := { start := 489849, fuel := 489849, spent := 0, income := 0, live := 15, workspace := 0, peak := 15, capacity := 256 }, physical := { phase := 1, source := 20, transferred := 0, wasted := 0 }, control := { word := 5, base := 23 } } }

def case37Events : List Event := [.install, .prepare, .reset, .advance, .advance, .advance, .advance, .advance, .sense, .checkSensor, .extract, .readReceipt, .commit, .closeRoute, .stop, .retain]

def case37Vectors : List (List Nat) := [[489849, 489849, 0, 0, 15, 0, 15, 256, 1, 20, 0, 0, 5, 0, 0, 0, 23, 0, 0, 0, 0], [489849, 398353, 91496, 0, 32, 0, 40, 256, 1, 20, 0, 0, 5, 0, 1, 0, 23, 0, 0, 0, 3, 0, 1, 2], [489849, 391929, 97920, 0, 32, 8, 40, 256, 1, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 375503, 114346, 0, 32, 8, 42, 256, 0, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 359077, 130772, 0, 32, 8, 42, 256, 1, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 342651, 147198, 0, 32, 8, 42, 256, 2, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 326225, 163624, 0, 32, 8, 42, 256, 0, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 309799, 180050, 0, 32, 8, 42, 256, 1, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 293373, 196476, 0, 32, 8, 42, 256, 2, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 276947, 212902, 0, 32, 8, 42, 256, 2, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 275839, 214010, 0, 32, 8, 42, 256, 2, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 259413, 230436, 0, 32, 8, 42, 256, 2, 10, 0, 10, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 242987, 246862, 0, 32, 8, 42, 256, 2, 10, 0, 10, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 230315, 259534, 0, 30, 8, 48, 256, 2, 10, 0, 10, 5, 1, 3, 0, 23, 2, 2, 2, 1, 0], [489849, 230315, 259534, 0, 30, 0, 48, 256, 2, 10, 0, 10, 5, 1, 3, 0, 23, 2, 2, 2, 1, 0], [489849, 230315, 259534, 0, 30, 0, 48, 256, 2, 10, 0, 10, 5, 1, 3, 0, 23, 2, 2, 2, 1, 0], [489849, 198511, 291338, 0, 30, 0, 48, 256, 2, 10, 0, 10, 5, 1, 5, 1, 23, 2, 2, 2, 1, 0]]

def case37Observations : List (List Nat) := [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [2, 0, 0], [2, 0, 0], [2, 0, 0], [2, 2, 0], [2, 2, 0], [2, 2, 0], [2, 2, 0], [2, 2, 0]]

theorem case37Certified : Runnable case37Initial case37Events ∧
    policyWord 100 case37Initial = case37Events ∧
    (history case37Initial case37Events).map vector = case37Vectors ∧
    (history case37Initial case37Events).map (fun s =>
      [optBoolCode s.body.sensor, optBoolCode s.body.receipt, boolCode s.body.actualArrival]) = case37Observations ∧
    (run case37Initial case37Events).body.error = .none ∧
    nextEvent (run case37Initial case37Events) = none := by decide

#print axioms case37Certified

-- grid:21:ordinary

def case38Initial : State := { H := { outputs := [false, false, true], transitions := [1, 2, 0], initial := 0 }, config := { environment := { outputs := [false, false, true], transitions := [1, 2, 0], initial := 0 }, tau := true, sigma := true, brokenReset := false, blocked := true, receiptMode := .faithful, clamp := false, deny := .none }, body := { account := { start := 489849, fuel := 489849, spent := 0, income := 0, live := 15, workspace := 0, peak := 15, capacity := 256 }, physical := { phase := 1, source := 20, transferred := 0, wasted := 0 }, control := { word := 5, base := 23 } } }

def case38Events : List Event := [.install, .prepare, .reset, .advance, .advance, .advance, .advance, .advance, .sense, .checkSensor, .extract, .readReceipt, .commit, .closeRoute, .scan, .select, .prepare, .reset, .sense, .checkSensor, .extract, .readReceipt, .commit, .closeRoute, .retain]

def case38Vectors : List (List Nat) := [[489849, 489849, 0, 0, 15, 0, 15, 256, 1, 20, 0, 0, 5, 0, 0, 0, 23, 0, 0, 0, 0], [489849, 398353, 91496, 0, 32, 0, 40, 256, 1, 20, 0, 0, 5, 0, 1, 0, 23, 0, 0, 0, 3, 0, 1, 2], [489849, 391929, 97920, 0, 32, 8, 40, 256, 1, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 375503, 114346, 0, 32, 8, 42, 256, 0, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 359077, 130772, 0, 32, 8, 42, 256, 1, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 342651, 147198, 0, 32, 8, 42, 256, 2, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 326225, 163624, 0, 32, 8, 42, 256, 0, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 309799, 180050, 0, 32, 8, 42, 256, 1, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 293373, 196476, 0, 32, 8, 42, 256, 2, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 276947, 212902, 0, 32, 8, 42, 256, 2, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 275839, 214010, 0, 32, 8, 42, 256, 2, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 259413, 230436, 0, 32, 8, 42, 256, 2, 10, 0, 10, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 242987, 246862, 0, 32, 8, 42, 256, 2, 10, 0, 10, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 229291, 260558, 0, 31, 8, 48, 256, 2, 10, 0, 10, 5, 1, 3, 0, 23, 2, 2, 1, 2, 1, 2], [489849, 229291, 260558, 0, 31, 0, 48, 256, 2, 10, 0, 10, 5, 1, 3, 0, 23, 2, 2, 1, 2, 1, 2], [489849, 225015, 264834, 0, 31, 0, 48, 256, 2, 10, 0, 10, 5, 1, 3, 0, 23, 2, 2, 1, 2, 1, 2], [489849, 221875, 267974, 0, 26, 0, 48, 256, 2, 10, 0, 10, 0, 1, 4, 0, 23, 2, 2, 1, 2, 1, 2], [489849, 220793, 269056, 0, 26, 3, 48, 256, 2, 10, 0, 10, 0, 1, 2, 0, 23, 1, 2, 1, 2, 1, 2], [489849, 204378, 285471, 0, 26, 3, 48, 256, 0, 10, 0, 10, 0, 1, 2, 0, 23, 1, 2, 1, 2, 1, 2], [489849, 187963, 301886, 0, 26, 3, 48, 256, 0, 10, 0, 10, 0, 1, 2, 0, 23, 1, 2, 1, 2, 1, 2], [489849, 186877, 302972, 0, 26, 3, 48, 256, 0, 10, 0, 10, 0, 1, 2, 0, 23, 1, 2, 1, 2, 1, 2], [489849, 170462, 319387, 0, 26, 3, 48, 256, 0, 0, 0, 20, 0, 1, 2, 0, 23, 1, 2, 1, 2, 1, 2], [489849, 154047, 335802, 0, 26, 3, 48, 256, 0, 0, 0, 20, 0, 1, 2, 0, 23, 1, 2, 1, 2, 1, 2], [489849, 143597, 346252, 0, 25, 3, 48, 256, 0, 0, 0, 20, 0, 2, 3, 0, 23, 1, 1, 1, 1, 2], [489849, 143597, 346252, 0, 25, 0, 48, 256, 0, 0, 0, 20, 0, 2, 3, 0, 23, 1, 1, 1, 1, 2], [489849, 116923, 372926, 0, 25, 0, 48, 256, 0, 0, 0, 20, 0, 2, 5, 1, 23, 1, 1, 1, 1, 2]]

def case38Observations : List (List Nat) := [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [2, 0, 0], [2, 0, 0], [2, 0, 0], [2, 1, 0], [2, 1, 0], [2, 1, 0], [2, 1, 0], [2, 1, 0], [0, 0, 0], [0, 0, 0], [1, 0, 0], [1, 0, 0], [1, 0, 0], [1, 1, 0], [1, 1, 0], [1, 1, 0], [1, 1, 0]]

theorem case38Certified : Runnable case38Initial case38Events ∧
    policyWord 100 case38Initial = case38Events ∧
    (history case38Initial case38Events).map vector = case38Vectors ∧
    (history case38Initial case38Events).map (fun s =>
      [optBoolCode s.body.sensor, optBoolCode s.body.receipt, boolCode s.body.actualArrival]) = case38Observations ∧
    (run case38Initial case38Events).body.error = .none ∧
    nextEvent (run case38Initial case38Events) = none := by decide

#print axioms case38Certified

-- grid:22:ordinary

def case39Initial : State := { H := { outputs := [false, false, true], transitions := [1, 2, 0], initial := 0 }, config := { environment := { outputs := [false, false, true], transitions := [1, 2, 0], initial := 0 }, tau := true, sigma := true, brokenReset := false, blocked := true, receiptMode := .missing, clamp := false, deny := .none }, body := { account := { start := 489849, fuel := 489849, spent := 0, income := 0, live := 15, workspace := 0, peak := 15, capacity := 256 }, physical := { phase := 1, source := 20, transferred := 0, wasted := 0 }, control := { word := 5, base := 23 } } }

def case39Events : List Event := [.install, .prepare, .reset, .advance, .advance, .advance, .advance, .advance, .sense, .checkSensor, .extract, .readReceipt, .closeRoute]

def case39Vectors : List (List Nat) := [[489849, 489849, 0, 0, 15, 0, 15, 256, 1, 20, 0, 0, 5, 0, 0, 0, 23, 0, 0, 0, 0], [489849, 398353, 91496, 0, 32, 0, 40, 256, 1, 20, 0, 0, 5, 0, 1, 0, 23, 0, 0, 0, 3, 0, 1, 2], [489849, 391929, 97920, 0, 32, 8, 40, 256, 1, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 375503, 114346, 0, 32, 8, 42, 256, 0, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 359077, 130772, 0, 32, 8, 42, 256, 1, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 342651, 147198, 0, 32, 8, 42, 256, 2, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 326225, 163624, 0, 32, 8, 42, 256, 0, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 309799, 180050, 0, 32, 8, 42, 256, 1, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 293373, 196476, 0, 32, 8, 42, 256, 2, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 276947, 212902, 0, 32, 8, 42, 256, 2, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 275839, 214010, 0, 32, 8, 42, 256, 2, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 259413, 230436, 0, 32, 8, 42, 256, 2, 10, 0, 10, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 242987, 246862, 0, 32, 8, 42, 256, 2, 10, 0, 10, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 242987, 246862, 0, 32, 0, 42, 256, 2, 10, 0, 10, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2]]

def case39Observations : List (List Nat) := [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [2, 0, 0], [2, 0, 0], [2, 0, 0], [2, 0, 0], [2, 0, 0]]

theorem case39Certified : Runnable case39Initial case39Events ∧
    policyWord 100 case39Initial = case39Events ∧
    (history case39Initial case39Events).map vector = case39Vectors ∧
    (history case39Initial case39Events).map (fun s =>
      [optBoolCode s.body.sensor, optBoolCode s.body.receipt, boolCode s.body.actualArrival]) = case39Observations ∧
    (run case39Initial case39Events).body.error = .missing ∧
    nextEvent (run case39Initial case39Events) = none := by decide

#print axioms case39Certified

-- grid:23:ordinary

def case40Initial : State := { H := { outputs := [false, false, true], transitions := [1, 2, 0], initial := 0 }, config := { environment := { outputs := [false, false, true], transitions := [1, 2, 0], initial := 0 }, tau := true, sigma := true, brokenReset := false, blocked := true, receiptMode := .complemented, clamp := false, deny := .none }, body := { account := { start := 489849, fuel := 489849, spent := 0, income := 0, live := 15, workspace := 0, peak := 15, capacity := 256 }, physical := { phase := 1, source := 20, transferred := 0, wasted := 0 }, control := { word := 5, base := 23 } } }

def case40Events : List Event := [.install, .prepare, .reset, .advance, .advance, .advance, .advance, .advance, .sense, .checkSensor, .extract, .readReceipt, .commit, .closeRoute, .stop, .retain]

def case40Vectors : List (List Nat) := [[489849, 489849, 0, 0, 15, 0, 15, 256, 1, 20, 0, 0, 5, 0, 0, 0, 23, 0, 0, 0, 0], [489849, 398353, 91496, 0, 32, 0, 40, 256, 1, 20, 0, 0, 5, 0, 1, 0, 23, 0, 0, 0, 3, 0, 1, 2], [489849, 391929, 97920, 0, 32, 8, 40, 256, 1, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 375503, 114346, 0, 32, 8, 42, 256, 0, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 359077, 130772, 0, 32, 8, 42, 256, 1, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 342651, 147198, 0, 32, 8, 42, 256, 2, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 326225, 163624, 0, 32, 8, 42, 256, 0, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 309799, 180050, 0, 32, 8, 42, 256, 1, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 293373, 196476, 0, 32, 8, 42, 256, 2, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 276947, 212902, 0, 32, 8, 42, 256, 2, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 275839, 214010, 0, 32, 8, 42, 256, 2, 20, 0, 0, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 259413, 230436, 0, 32, 8, 42, 256, 2, 10, 0, 10, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 242987, 246862, 0, 32, 8, 42, 256, 2, 10, 0, 10, 5, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [489849, 230315, 259534, 0, 30, 8, 48, 256, 2, 10, 0, 10, 5, 1, 3, 0, 23, 2, 2, 2, 1, 0], [489849, 230315, 259534, 0, 30, 0, 48, 256, 2, 10, 0, 10, 5, 1, 3, 0, 23, 2, 2, 2, 1, 0], [489849, 230315, 259534, 0, 30, 0, 48, 256, 2, 10, 0, 10, 5, 1, 3, 0, 23, 2, 2, 2, 1, 0], [489849, 198511, 291338, 0, 30, 0, 48, 256, 2, 10, 0, 10, 5, 1, 5, 1, 23, 2, 2, 2, 1, 0]]

def case40Observations : List (List Nat) := [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [2, 0, 0], [2, 0, 0], [2, 0, 0], [2, 2, 0], [2, 2, 0], [2, 2, 0], [2, 2, 0], [2, 2, 0]]

theorem case40Certified : Runnable case40Initial case40Events ∧
    policyWord 100 case40Initial = case40Events ∧
    (history case40Initial case40Events).map vector = case40Vectors ∧
    (history case40Initial case40Events).map (fun s =>
      [optBoolCode s.body.sensor, optBoolCode s.body.receipt, boolCode s.body.actualArrival]) = case40Observations ∧
    (run case40Initial case40Events).body.error = .none ∧
    nextEvent (run case40Initial case40Events) = none := by decide

#print axioms case40Certified

-- grid:24:inverted

def case41Initial : State := { H := { outputs := [true, true, false], transitions := [1, 2, 0], initial := 0 }, config := { environment := { outputs := [false, false, true], transitions := [1, 2, 0], initial := 0 }, tau := false, sigma := true, brokenReset := false, blocked := false, receiptMode := .faithful, clamp := false, deny := .none }, body := { account := { start := 468871, fuel := 468871, spent := 0, income := 0, live := 15, workspace := 0, peak := 15, capacity := 256 }, physical := { phase := 1, source := 20, transferred := 0, wasted := 0 }, control := { word := 6, base := 23 } } }

def case41Events : List Event := [.install, .prepare, .reset, .advance, .advance, .advance, .advance, .advance, .advance, .sense, .checkSensor, .extract, .readReceipt, .commit, .closeRoute, .scan, .scan, .scan, .select, .prepare, .reset, .advance, .advance, .sense, .checkSensor, .extract, .readReceipt, .commit, .closeRoute, .retain]

def case41Vectors : List (List Nat) := [[468871, 468871, 0, 0, 15, 0, 15, 256, 1, 20, 0, 0, 6, 0, 0, 0, 23, 0, 0, 0, 0], [468871, 376342, 92529, 0, 33, 0, 41, 256, 1, 20, 0, 0, 6, 0, 1, 0, 23, 0, 0, 0, 3, 0, 1, 2], [468871, 368838, 100033, 0, 33, 9, 42, 256, 1, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 352410, 116461, 0, 33, 9, 44, 256, 0, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 335982, 132889, 0, 33, 9, 44, 256, 1, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 319554, 149317, 0, 33, 9, 44, 256, 2, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 303126, 165745, 0, 33, 9, 44, 256, 0, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 286698, 182173, 0, 33, 9, 44, 256, 1, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 270270, 198601, 0, 33, 9, 44, 256, 2, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 253842, 215029, 0, 33, 9, 44, 256, 0, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 237414, 231457, 0, 33, 9, 44, 256, 0, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 236302, 232569, 0, 33, 9, 44, 256, 0, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 219874, 248997, 0, 33, 9, 44, 256, 0, 10, 0, 10, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 203446, 265425, 0, 33, 9, 44, 256, 0, 10, 0, 10, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 189734, 279137, 0, 32, 9, 50, 256, 0, 10, 0, 10, 6, 1, 3, 0, 23, 2, 2, 1, 2, 1, 2], [468871, 189734, 279137, 0, 32, 0, 50, 256, 0, 10, 0, 10, 6, 1, 3, 0, 23, 2, 2, 1, 2, 1, 2], [468871, 185453, 283418, 0, 32, 0, 50, 256, 0, 10, 0, 10, 6, 1, 3, 0, 23, 2, 2, 1, 2, 1, 2], [468871, 179043, 289828, 0, 32, 0, 50, 256, 0, 10, 0, 10, 6, 1, 3, 0, 23, 2, 2, 1, 2, 1, 2], [468871, 170500, 298371, 0, 32, 0, 50, 256, 0, 10, 0, 10, 6, 1, 3, 0, 23, 2, 2, 1, 2, 1, 2], [468871, 163184, 305687, 0, 28, 0, 50, 256, 0, 10, 0, 10, 2, 1, 4, 0, 23, 2, 2, 1, 2, 1, 2], [468871, 159980, 308891, 0, 28, 5, 50, 256, 0, 10, 0, 10, 2, 1, 2, 0, 23, 1, 2, 1, 2, 1, 2], [468871, 143561, 325310, 0, 28, 5, 50, 256, 0, 10, 0, 10, 2, 1, 2, 0, 23, 1, 2, 1, 2, 1, 2], [468871, 127142, 341729, 0, 28, 5, 50, 256, 1, 10, 0, 10, 2, 1, 2, 0, 23, 1, 2, 1, 2, 1, 2], [468871, 110723, 358148, 0, 28, 5, 50, 256, 2, 10, 0, 10, 2, 1, 2, 0, 23, 1, 2, 1, 2, 1, 2], [468871, 94304, 374567, 0, 28, 5, 50, 256, 2, 10, 0, 10, 2, 1, 2, 0, 23, 1, 2, 1, 2, 1, 2], [468871, 93210, 375661, 0, 28, 5, 50, 256, 2, 10, 0, 10, 2, 1, 2, 0, 23, 1, 2, 1, 2, 1, 2], [468871, 732151, 392080, 655360, 28, 5, 50, 256, 2, 0, 10, 10, 2, 1, 2, 0, 23, 1, 2, 1, 2, 1, 2], [468871, 715732, 408499, 655360, 28, 5, 50, 256, 2, 0, 10, 10, 2, 1, 2, 0, 23, 1, 2, 1, 2, 1, 2], [468871, 705258, 418973, 655360, 27, 5, 50, 256, 2, 0, 10, 10, 2, 2, 3, 0, 23, 1, 1, 2, 1, 1], [468871, 705258, 418973, 655360, 27, 0, 50, 256, 2, 0, 10, 10, 2, 2, 3, 0, 23, 1, 1, 2, 1, 1], [468871, 676532, 447699, 655360, 27, 0, 50, 256, 2, 0, 10, 10, 2, 2, 5, 1, 23, 1, 1, 2, 1, 1]]

def case41Observations : List (List Nat) := [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [2, 0, 0], [2, 0, 0], [2, 0, 0], [2, 1, 0], [2, 1, 0], [2, 1, 0], [2, 1, 0], [2, 1, 0], [2, 1, 0], [2, 1, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [1, 0, 0], [1, 0, 0], [1, 0, 1], [1, 2, 1], [1, 2, 1], [1, 2, 1], [1, 2, 1]]

theorem case41Certified : Runnable case41Initial case41Events ∧
    policyWord 100 case41Initial = case41Events ∧
    (history case41Initial case41Events).map vector = case41Vectors ∧
    (history case41Initial case41Events).map (fun s =>
      [optBoolCode s.body.sensor, optBoolCode s.body.receipt, boolCode s.body.actualArrival]) = case41Observations ∧
    (run case41Initial case41Events).body.error = .none ∧
    nextEvent (run case41Initial case41Events) = none := by decide

#print axioms case41Certified

-- grid:25:inverted

def case42Initial : State := { H := { outputs := [true, true, false], transitions := [1, 2, 0], initial := 0 }, config := { environment := { outputs := [false, false, true], transitions := [1, 2, 0], initial := 0 }, tau := false, sigma := true, brokenReset := false, blocked := false, receiptMode := .missing, clamp := false, deny := .none }, body := { account := { start := 468871, fuel := 468871, spent := 0, income := 0, live := 15, workspace := 0, peak := 15, capacity := 256 }, physical := { phase := 1, source := 20, transferred := 0, wasted := 0 }, control := { word := 6, base := 23 } } }

def case42Events : List Event := [.install, .prepare, .reset, .advance, .advance, .advance, .advance, .advance, .advance, .sense, .checkSensor, .extract, .readReceipt, .closeRoute]

def case42Vectors : List (List Nat) := [[468871, 468871, 0, 0, 15, 0, 15, 256, 1, 20, 0, 0, 6, 0, 0, 0, 23, 0, 0, 0, 0], [468871, 376342, 92529, 0, 33, 0, 41, 256, 1, 20, 0, 0, 6, 0, 1, 0, 23, 0, 0, 0, 3, 0, 1, 2], [468871, 368838, 100033, 0, 33, 9, 42, 256, 1, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 352410, 116461, 0, 33, 9, 44, 256, 0, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 335982, 132889, 0, 33, 9, 44, 256, 1, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 319554, 149317, 0, 33, 9, 44, 256, 2, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 303126, 165745, 0, 33, 9, 44, 256, 0, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 286698, 182173, 0, 33, 9, 44, 256, 1, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 270270, 198601, 0, 33, 9, 44, 256, 2, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 253842, 215029, 0, 33, 9, 44, 256, 0, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 237414, 231457, 0, 33, 9, 44, 256, 0, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 236302, 232569, 0, 33, 9, 44, 256, 0, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 219874, 248997, 0, 33, 9, 44, 256, 0, 10, 0, 10, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 203446, 265425, 0, 33, 9, 44, 256, 0, 10, 0, 10, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 203446, 265425, 0, 33, 0, 44, 256, 0, 10, 0, 10, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2]]

def case42Observations : List (List Nat) := [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [2, 0, 0], [2, 0, 0], [2, 0, 0], [2, 0, 0], [2, 0, 0]]

theorem case42Certified : Runnable case42Initial case42Events ∧
    policyWord 100 case42Initial = case42Events ∧
    (history case42Initial case42Events).map vector = case42Vectors ∧
    (history case42Initial case42Events).map (fun s =>
      [optBoolCode s.body.sensor, optBoolCode s.body.receipt, boolCode s.body.actualArrival]) = case42Observations ∧
    (run case42Initial case42Events).body.error = .missing ∧
    nextEvent (run case42Initial case42Events) = none := by decide

#print axioms case42Certified

-- grid:26:inverted

def case43Initial : State := { H := { outputs := [true, true, false], transitions := [1, 2, 0], initial := 0 }, config := { environment := { outputs := [false, false, true], transitions := [1, 2, 0], initial := 0 }, tau := false, sigma := true, brokenReset := false, blocked := false, receiptMode := .complemented, clamp := false, deny := .none }, body := { account := { start := 468871, fuel := 468871, spent := 0, income := 0, live := 15, workspace := 0, peak := 15, capacity := 256 }, physical := { phase := 1, source := 20, transferred := 0, wasted := 0 }, control := { word := 6, base := 23 } } }

def case43Events : List Event := [.install, .prepare, .reset, .advance, .advance, .advance, .advance, .advance, .advance, .sense, .checkSensor, .extract, .readReceipt, .commit, .closeRoute, .stop, .retain]

def case43Vectors : List (List Nat) := [[468871, 468871, 0, 0, 15, 0, 15, 256, 1, 20, 0, 0, 6, 0, 0, 0, 23, 0, 0, 0, 0], [468871, 376342, 92529, 0, 33, 0, 41, 256, 1, 20, 0, 0, 6, 0, 1, 0, 23, 0, 0, 0, 3, 0, 1, 2], [468871, 368838, 100033, 0, 33, 9, 42, 256, 1, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 352410, 116461, 0, 33, 9, 44, 256, 0, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 335982, 132889, 0, 33, 9, 44, 256, 1, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 319554, 149317, 0, 33, 9, 44, 256, 2, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 303126, 165745, 0, 33, 9, 44, 256, 0, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 286698, 182173, 0, 33, 9, 44, 256, 1, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 270270, 198601, 0, 33, 9, 44, 256, 2, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 253842, 215029, 0, 33, 9, 44, 256, 0, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 237414, 231457, 0, 33, 9, 44, 256, 0, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 236302, 232569, 0, 33, 9, 44, 256, 0, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 219874, 248997, 0, 33, 9, 44, 256, 0, 10, 0, 10, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 203446, 265425, 0, 33, 9, 44, 256, 0, 10, 0, 10, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 190758, 278113, 0, 31, 9, 50, 256, 0, 10, 0, 10, 6, 1, 3, 0, 23, 2, 2, 2, 1, 0], [468871, 190758, 278113, 0, 31, 0, 50, 256, 0, 10, 0, 10, 6, 1, 3, 0, 23, 2, 2, 2, 1, 0], [468871, 190758, 278113, 0, 31, 0, 50, 256, 0, 10, 0, 10, 6, 1, 3, 0, 23, 2, 2, 2, 1, 0], [468871, 157928, 310943, 0, 31, 0, 50, 256, 0, 10, 0, 10, 6, 1, 5, 1, 23, 2, 2, 2, 1, 0]]

def case43Observations : List (List Nat) := [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [2, 0, 0], [2, 0, 0], [2, 0, 0], [2, 2, 0], [2, 2, 0], [2, 2, 0], [2, 2, 0], [2, 2, 0]]

theorem case43Certified : Runnable case43Initial case43Events ∧
    policyWord 100 case43Initial = case43Events ∧
    (history case43Initial case43Events).map vector = case43Vectors ∧
    (history case43Initial case43Events).map (fun s =>
      [optBoolCode s.body.sensor, optBoolCode s.body.receipt, boolCode s.body.actualArrival]) = case43Observations ∧
    (run case43Initial case43Events).body.error = .none ∧
    nextEvent (run case43Initial case43Events) = none := by decide

#print axioms case43Certified

-- grid:27:inverted

def case44Initial : State := { H := { outputs := [true, true, false], transitions := [1, 2, 0], initial := 0 }, config := { environment := { outputs := [false, false, true], transitions := [1, 2, 0], initial := 0 }, tau := false, sigma := true, brokenReset := false, blocked := true, receiptMode := .faithful, clamp := false, deny := .none }, body := { account := { start := 468871, fuel := 468871, spent := 0, income := 0, live := 15, workspace := 0, peak := 15, capacity := 256 }, physical := { phase := 1, source := 20, transferred := 0, wasted := 0 }, control := { word := 6, base := 23 } } }

def case44Events : List Event := [.install, .prepare, .reset, .advance, .advance, .advance, .advance, .advance, .advance, .sense, .checkSensor, .extract, .readReceipt, .commit, .closeRoute, .scan, .scan, .scan, .select, .prepare, .reset, .advance, .advance, .sense, .checkSensor, .extract, .readReceipt, .commit, .closeRoute, .retain]

def case44Vectors : List (List Nat) := [[468871, 468871, 0, 0, 15, 0, 15, 256, 1, 20, 0, 0, 6, 0, 0, 0, 23, 0, 0, 0, 0], [468871, 376342, 92529, 0, 33, 0, 41, 256, 1, 20, 0, 0, 6, 0, 1, 0, 23, 0, 0, 0, 3, 0, 1, 2], [468871, 368838, 100033, 0, 33, 9, 42, 256, 1, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 352410, 116461, 0, 33, 9, 44, 256, 0, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 335982, 132889, 0, 33, 9, 44, 256, 1, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 319554, 149317, 0, 33, 9, 44, 256, 2, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 303126, 165745, 0, 33, 9, 44, 256, 0, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 286698, 182173, 0, 33, 9, 44, 256, 1, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 270270, 198601, 0, 33, 9, 44, 256, 2, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 253842, 215029, 0, 33, 9, 44, 256, 0, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 237414, 231457, 0, 33, 9, 44, 256, 0, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 236302, 232569, 0, 33, 9, 44, 256, 0, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 219874, 248997, 0, 33, 9, 44, 256, 0, 10, 0, 10, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 203446, 265425, 0, 33, 9, 44, 256, 0, 10, 0, 10, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 189734, 279137, 0, 32, 9, 50, 256, 0, 10, 0, 10, 6, 1, 3, 0, 23, 2, 2, 1, 2, 1, 2], [468871, 189734, 279137, 0, 32, 0, 50, 256, 0, 10, 0, 10, 6, 1, 3, 0, 23, 2, 2, 1, 2, 1, 2], [468871, 185453, 283418, 0, 32, 0, 50, 256, 0, 10, 0, 10, 6, 1, 3, 0, 23, 2, 2, 1, 2, 1, 2], [468871, 179043, 289828, 0, 32, 0, 50, 256, 0, 10, 0, 10, 6, 1, 3, 0, 23, 2, 2, 1, 2, 1, 2], [468871, 170500, 298371, 0, 32, 0, 50, 256, 0, 10, 0, 10, 6, 1, 3, 0, 23, 2, 2, 1, 2, 1, 2], [468871, 163184, 305687, 0, 28, 0, 50, 256, 0, 10, 0, 10, 2, 1, 4, 0, 23, 2, 2, 1, 2, 1, 2], [468871, 159980, 308891, 0, 28, 5, 50, 256, 0, 10, 0, 10, 2, 1, 2, 0, 23, 1, 2, 1, 2, 1, 2], [468871, 143561, 325310, 0, 28, 5, 50, 256, 0, 10, 0, 10, 2, 1, 2, 0, 23, 1, 2, 1, 2, 1, 2], [468871, 127142, 341729, 0, 28, 5, 50, 256, 1, 10, 0, 10, 2, 1, 2, 0, 23, 1, 2, 1, 2, 1, 2], [468871, 110723, 358148, 0, 28, 5, 50, 256, 2, 10, 0, 10, 2, 1, 2, 0, 23, 1, 2, 1, 2, 1, 2], [468871, 94304, 374567, 0, 28, 5, 50, 256, 2, 10, 0, 10, 2, 1, 2, 0, 23, 1, 2, 1, 2, 1, 2], [468871, 93210, 375661, 0, 28, 5, 50, 256, 2, 10, 0, 10, 2, 1, 2, 0, 23, 1, 2, 1, 2, 1, 2], [468871, 76791, 392080, 0, 28, 5, 50, 256, 2, 0, 0, 20, 2, 1, 2, 0, 23, 1, 2, 1, 2, 1, 2], [468871, 60372, 408499, 0, 28, 5, 50, 256, 2, 0, 0, 20, 2, 1, 2, 0, 23, 1, 2, 1, 2, 1, 2], [468871, 49898, 418973, 0, 27, 5, 50, 256, 2, 0, 0, 20, 2, 2, 3, 0, 23, 1, 1, 1, 1, 2], [468871, 49898, 418973, 0, 27, 0, 50, 256, 2, 0, 0, 20, 2, 2, 3, 0, 23, 1, 1, 1, 1, 2], [468871, 21172, 447699, 0, 27, 0, 50, 256, 2, 0, 0, 20, 2, 2, 5, 1, 23, 1, 1, 1, 1, 2]]

def case44Observations : List (List Nat) := [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [2, 0, 0], [2, 0, 0], [2, 0, 0], [2, 1, 0], [2, 1, 0], [2, 1, 0], [2, 1, 0], [2, 1, 0], [2, 1, 0], [2, 1, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [1, 0, 0], [1, 0, 0], [1, 0, 0], [1, 1, 0], [1, 1, 0], [1, 1, 0], [1, 1, 0]]

theorem case44Certified : Runnable case44Initial case44Events ∧
    policyWord 100 case44Initial = case44Events ∧
    (history case44Initial case44Events).map vector = case44Vectors ∧
    (history case44Initial case44Events).map (fun s =>
      [optBoolCode s.body.sensor, optBoolCode s.body.receipt, boolCode s.body.actualArrival]) = case44Observations ∧
    (run case44Initial case44Events).body.error = .none ∧
    nextEvent (run case44Initial case44Events) = none := by decide

#print axioms case44Certified

-- grid:28:inverted

def case45Initial : State := { H := { outputs := [true, true, false], transitions := [1, 2, 0], initial := 0 }, config := { environment := { outputs := [false, false, true], transitions := [1, 2, 0], initial := 0 }, tau := false, sigma := true, brokenReset := false, blocked := true, receiptMode := .missing, clamp := false, deny := .none }, body := { account := { start := 468871, fuel := 468871, spent := 0, income := 0, live := 15, workspace := 0, peak := 15, capacity := 256 }, physical := { phase := 1, source := 20, transferred := 0, wasted := 0 }, control := { word := 6, base := 23 } } }

def case45Events : List Event := [.install, .prepare, .reset, .advance, .advance, .advance, .advance, .advance, .advance, .sense, .checkSensor, .extract, .readReceipt, .closeRoute]

def case45Vectors : List (List Nat) := [[468871, 468871, 0, 0, 15, 0, 15, 256, 1, 20, 0, 0, 6, 0, 0, 0, 23, 0, 0, 0, 0], [468871, 376342, 92529, 0, 33, 0, 41, 256, 1, 20, 0, 0, 6, 0, 1, 0, 23, 0, 0, 0, 3, 0, 1, 2], [468871, 368838, 100033, 0, 33, 9, 42, 256, 1, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 352410, 116461, 0, 33, 9, 44, 256, 0, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 335982, 132889, 0, 33, 9, 44, 256, 1, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 319554, 149317, 0, 33, 9, 44, 256, 2, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 303126, 165745, 0, 33, 9, 44, 256, 0, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 286698, 182173, 0, 33, 9, 44, 256, 1, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 270270, 198601, 0, 33, 9, 44, 256, 2, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 253842, 215029, 0, 33, 9, 44, 256, 0, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 237414, 231457, 0, 33, 9, 44, 256, 0, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 236302, 232569, 0, 33, 9, 44, 256, 0, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 219874, 248997, 0, 33, 9, 44, 256, 0, 10, 0, 10, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 203446, 265425, 0, 33, 9, 44, 256, 0, 10, 0, 10, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 203446, 265425, 0, 33, 0, 44, 256, 0, 10, 0, 10, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2]]

def case45Observations : List (List Nat) := [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [2, 0, 0], [2, 0, 0], [2, 0, 0], [2, 0, 0], [2, 0, 0]]

theorem case45Certified : Runnable case45Initial case45Events ∧
    policyWord 100 case45Initial = case45Events ∧
    (history case45Initial case45Events).map vector = case45Vectors ∧
    (history case45Initial case45Events).map (fun s =>
      [optBoolCode s.body.sensor, optBoolCode s.body.receipt, boolCode s.body.actualArrival]) = case45Observations ∧
    (run case45Initial case45Events).body.error = .missing ∧
    nextEvent (run case45Initial case45Events) = none := by decide

#print axioms case45Certified

-- grid:29:inverted

def case46Initial : State := { H := { outputs := [true, true, false], transitions := [1, 2, 0], initial := 0 }, config := { environment := { outputs := [false, false, true], transitions := [1, 2, 0], initial := 0 }, tau := false, sigma := true, brokenReset := false, blocked := true, receiptMode := .complemented, clamp := false, deny := .none }, body := { account := { start := 468871, fuel := 468871, spent := 0, income := 0, live := 15, workspace := 0, peak := 15, capacity := 256 }, physical := { phase := 1, source := 20, transferred := 0, wasted := 0 }, control := { word := 6, base := 23 } } }

def case46Events : List Event := [.install, .prepare, .reset, .advance, .advance, .advance, .advance, .advance, .advance, .sense, .checkSensor, .extract, .readReceipt, .commit, .closeRoute, .stop, .retain]

def case46Vectors : List (List Nat) := [[468871, 468871, 0, 0, 15, 0, 15, 256, 1, 20, 0, 0, 6, 0, 0, 0, 23, 0, 0, 0, 0], [468871, 376342, 92529, 0, 33, 0, 41, 256, 1, 20, 0, 0, 6, 0, 1, 0, 23, 0, 0, 0, 3, 0, 1, 2], [468871, 368838, 100033, 0, 33, 9, 42, 256, 1, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 352410, 116461, 0, 33, 9, 44, 256, 0, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 335982, 132889, 0, 33, 9, 44, 256, 1, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 319554, 149317, 0, 33, 9, 44, 256, 2, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 303126, 165745, 0, 33, 9, 44, 256, 0, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 286698, 182173, 0, 33, 9, 44, 256, 1, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 270270, 198601, 0, 33, 9, 44, 256, 2, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 253842, 215029, 0, 33, 9, 44, 256, 0, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 237414, 231457, 0, 33, 9, 44, 256, 0, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 236302, 232569, 0, 33, 9, 44, 256, 0, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 219874, 248997, 0, 33, 9, 44, 256, 0, 10, 0, 10, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 203446, 265425, 0, 33, 9, 44, 256, 0, 10, 0, 10, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 190758, 278113, 0, 31, 9, 50, 256, 0, 10, 0, 10, 6, 1, 3, 0, 23, 2, 2, 2, 1, 0], [468871, 190758, 278113, 0, 31, 0, 50, 256, 0, 10, 0, 10, 6, 1, 3, 0, 23, 2, 2, 2, 1, 0], [468871, 190758, 278113, 0, 31, 0, 50, 256, 0, 10, 0, 10, 6, 1, 3, 0, 23, 2, 2, 2, 1, 0], [468871, 157928, 310943, 0, 31, 0, 50, 256, 0, 10, 0, 10, 6, 1, 5, 1, 23, 2, 2, 2, 1, 0]]

def case46Observations : List (List Nat) := [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [2, 0, 0], [2, 0, 0], [2, 0, 0], [2, 2, 0], [2, 2, 0], [2, 2, 0], [2, 2, 0], [2, 2, 0]]

theorem case46Certified : Runnable case46Initial case46Events ∧
    policyWord 100 case46Initial = case46Events ∧
    (history case46Initial case46Events).map vector = case46Vectors ∧
    (history case46Initial case46Events).map (fun s =>
      [optBoolCode s.body.sensor, optBoolCode s.body.receipt, boolCode s.body.actualArrival]) = case46Observations ∧
    (run case46Initial case46Events).body.error = .none ∧
    nextEvent (run case46Initial case46Events) = none := by decide

#print axioms case46Certified

-- grid:30:inverted

def case47Initial : State := { H := { outputs := [true, true, false], transitions := [1, 2, 0], initial := 0 }, config := { environment := { outputs := [false, false, true], transitions := [1, 2, 0], initial := 0 }, tau := false, sigma := false, brokenReset := false, blocked := false, receiptMode := .faithful, clamp := false, deny := .none }, body := { account := { start := 468871, fuel := 468871, spent := 0, income := 0, live := 15, workspace := 0, peak := 15, capacity := 256 }, physical := { phase := 1, source := 20, transferred := 0, wasted := 0 }, control := { word := 6, base := 23 } } }

def case47Events : List Event := [.install, .prepare, .reset, .advance, .advance, .advance, .advance, .advance, .advance, .sense, .checkSensor, .closeRoute]

def case47Vectors : List (List Nat) := [[468871, 468871, 0, 0, 15, 0, 15, 256, 1, 20, 0, 0, 6, 0, 0, 0, 23, 0, 0, 0, 0], [468871, 376342, 92529, 0, 33, 0, 41, 256, 1, 20, 0, 0, 6, 0, 1, 0, 23, 0, 0, 0, 3, 0, 1, 2], [468871, 368838, 100033, 0, 33, 9, 42, 256, 1, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 352410, 116461, 0, 33, 9, 44, 256, 0, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 335982, 132889, 0, 33, 9, 44, 256, 1, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 319554, 149317, 0, 33, 9, 44, 256, 2, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 303126, 165745, 0, 33, 9, 44, 256, 0, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 286698, 182173, 0, 33, 9, 44, 256, 1, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 270270, 198601, 0, 33, 9, 44, 256, 2, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 253842, 215029, 0, 33, 9, 44, 256, 0, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 237414, 231457, 0, 33, 9, 44, 256, 0, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 236302, 232569, 0, 33, 9, 44, 256, 0, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 236302, 232569, 0, 33, 0, 44, 256, 0, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2]]

def case47Observations : List (List Nat) := [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [1, 0, 0], [1, 0, 0], [1, 0, 0]]

theorem case47Certified : Runnable case47Initial case47Events ∧
    policyWord 100 case47Initial = case47Events ∧
    (history case47Initial case47Events).map vector = case47Vectors ∧
    (history case47Initial case47Events).map (fun s =>
      [optBoolCode s.body.sensor, optBoolCode s.body.receipt, boolCode s.body.actualArrival]) = case47Observations ∧
    (run case47Initial case47Events).body.error = .mismatch ∧
    nextEvent (run case47Initial case47Events) = none := by decide

#print axioms case47Certified

-- grid:31:inverted

def case48Initial : State := { H := { outputs := [true, true, false], transitions := [1, 2, 0], initial := 0 }, config := { environment := { outputs := [false, false, true], transitions := [1, 2, 0], initial := 0 }, tau := false, sigma := false, brokenReset := false, blocked := false, receiptMode := .missing, clamp := false, deny := .none }, body := { account := { start := 468871, fuel := 468871, spent := 0, income := 0, live := 15, workspace := 0, peak := 15, capacity := 256 }, physical := { phase := 1, source := 20, transferred := 0, wasted := 0 }, control := { word := 6, base := 23 } } }

def case48Events : List Event := [.install, .prepare, .reset, .advance, .advance, .advance, .advance, .advance, .advance, .sense, .checkSensor, .closeRoute]

def case48Vectors : List (List Nat) := [[468871, 468871, 0, 0, 15, 0, 15, 256, 1, 20, 0, 0, 6, 0, 0, 0, 23, 0, 0, 0, 0], [468871, 376342, 92529, 0, 33, 0, 41, 256, 1, 20, 0, 0, 6, 0, 1, 0, 23, 0, 0, 0, 3, 0, 1, 2], [468871, 368838, 100033, 0, 33, 9, 42, 256, 1, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 352410, 116461, 0, 33, 9, 44, 256, 0, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 335982, 132889, 0, 33, 9, 44, 256, 1, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 319554, 149317, 0, 33, 9, 44, 256, 2, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 303126, 165745, 0, 33, 9, 44, 256, 0, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 286698, 182173, 0, 33, 9, 44, 256, 1, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 270270, 198601, 0, 33, 9, 44, 256, 2, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 253842, 215029, 0, 33, 9, 44, 256, 0, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 237414, 231457, 0, 33, 9, 44, 256, 0, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 236302, 232569, 0, 33, 9, 44, 256, 0, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 236302, 232569, 0, 33, 0, 44, 256, 0, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2]]

def case48Observations : List (List Nat) := [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [1, 0, 0], [1, 0, 0], [1, 0, 0]]

theorem case48Certified : Runnable case48Initial case48Events ∧
    policyWord 100 case48Initial = case48Events ∧
    (history case48Initial case48Events).map vector = case48Vectors ∧
    (history case48Initial case48Events).map (fun s =>
      [optBoolCode s.body.sensor, optBoolCode s.body.receipt, boolCode s.body.actualArrival]) = case48Observations ∧
    (run case48Initial case48Events).body.error = .mismatch ∧
    nextEvent (run case48Initial case48Events) = none := by decide

#print axioms case48Certified

-- grid:32:inverted

def case49Initial : State := { H := { outputs := [true, true, false], transitions := [1, 2, 0], initial := 0 }, config := { environment := { outputs := [false, false, true], transitions := [1, 2, 0], initial := 0 }, tau := false, sigma := false, brokenReset := false, blocked := false, receiptMode := .complemented, clamp := false, deny := .none }, body := { account := { start := 468871, fuel := 468871, spent := 0, income := 0, live := 15, workspace := 0, peak := 15, capacity := 256 }, physical := { phase := 1, source := 20, transferred := 0, wasted := 0 }, control := { word := 6, base := 23 } } }

def case49Events : List Event := [.install, .prepare, .reset, .advance, .advance, .advance, .advance, .advance, .advance, .sense, .checkSensor, .closeRoute]

def case49Vectors : List (List Nat) := [[468871, 468871, 0, 0, 15, 0, 15, 256, 1, 20, 0, 0, 6, 0, 0, 0, 23, 0, 0, 0, 0], [468871, 376342, 92529, 0, 33, 0, 41, 256, 1, 20, 0, 0, 6, 0, 1, 0, 23, 0, 0, 0, 3, 0, 1, 2], [468871, 368838, 100033, 0, 33, 9, 42, 256, 1, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 352410, 116461, 0, 33, 9, 44, 256, 0, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 335982, 132889, 0, 33, 9, 44, 256, 1, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 319554, 149317, 0, 33, 9, 44, 256, 2, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 303126, 165745, 0, 33, 9, 44, 256, 0, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 286698, 182173, 0, 33, 9, 44, 256, 1, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 270270, 198601, 0, 33, 9, 44, 256, 2, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 253842, 215029, 0, 33, 9, 44, 256, 0, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 237414, 231457, 0, 33, 9, 44, 256, 0, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 236302, 232569, 0, 33, 9, 44, 256, 0, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 236302, 232569, 0, 33, 0, 44, 256, 0, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2]]

def case49Observations : List (List Nat) := [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [1, 0, 0], [1, 0, 0], [1, 0, 0]]

theorem case49Certified : Runnable case49Initial case49Events ∧
    policyWord 100 case49Initial = case49Events ∧
    (history case49Initial case49Events).map vector = case49Vectors ∧
    (history case49Initial case49Events).map (fun s =>
      [optBoolCode s.body.sensor, optBoolCode s.body.receipt, boolCode s.body.actualArrival]) = case49Observations ∧
    (run case49Initial case49Events).body.error = .mismatch ∧
    nextEvent (run case49Initial case49Events) = none := by decide

#print axioms case49Certified

-- grid:33:inverted

def case50Initial : State := { H := { outputs := [true, true, false], transitions := [1, 2, 0], initial := 0 }, config := { environment := { outputs := [false, false, true], transitions := [1, 2, 0], initial := 0 }, tau := false, sigma := false, brokenReset := false, blocked := true, receiptMode := .faithful, clamp := false, deny := .none }, body := { account := { start := 468871, fuel := 468871, spent := 0, income := 0, live := 15, workspace := 0, peak := 15, capacity := 256 }, physical := { phase := 1, source := 20, transferred := 0, wasted := 0 }, control := { word := 6, base := 23 } } }

def case50Events : List Event := [.install, .prepare, .reset, .advance, .advance, .advance, .advance, .advance, .advance, .sense, .checkSensor, .closeRoute]

def case50Vectors : List (List Nat) := [[468871, 468871, 0, 0, 15, 0, 15, 256, 1, 20, 0, 0, 6, 0, 0, 0, 23, 0, 0, 0, 0], [468871, 376342, 92529, 0, 33, 0, 41, 256, 1, 20, 0, 0, 6, 0, 1, 0, 23, 0, 0, 0, 3, 0, 1, 2], [468871, 368838, 100033, 0, 33, 9, 42, 256, 1, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 352410, 116461, 0, 33, 9, 44, 256, 0, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 335982, 132889, 0, 33, 9, 44, 256, 1, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 319554, 149317, 0, 33, 9, 44, 256, 2, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 303126, 165745, 0, 33, 9, 44, 256, 0, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 286698, 182173, 0, 33, 9, 44, 256, 1, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 270270, 198601, 0, 33, 9, 44, 256, 2, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 253842, 215029, 0, 33, 9, 44, 256, 0, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 237414, 231457, 0, 33, 9, 44, 256, 0, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 236302, 232569, 0, 33, 9, 44, 256, 0, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 236302, 232569, 0, 33, 0, 44, 256, 0, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2]]

def case50Observations : List (List Nat) := [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [1, 0, 0], [1, 0, 0], [1, 0, 0]]

theorem case50Certified : Runnable case50Initial case50Events ∧
    policyWord 100 case50Initial = case50Events ∧
    (history case50Initial case50Events).map vector = case50Vectors ∧
    (history case50Initial case50Events).map (fun s =>
      [optBoolCode s.body.sensor, optBoolCode s.body.receipt, boolCode s.body.actualArrival]) = case50Observations ∧
    (run case50Initial case50Events).body.error = .mismatch ∧
    nextEvent (run case50Initial case50Events) = none := by decide

#print axioms case50Certified

-- grid:34:inverted

def case51Initial : State := { H := { outputs := [true, true, false], transitions := [1, 2, 0], initial := 0 }, config := { environment := { outputs := [false, false, true], transitions := [1, 2, 0], initial := 0 }, tau := false, sigma := false, brokenReset := false, blocked := true, receiptMode := .missing, clamp := false, deny := .none }, body := { account := { start := 468871, fuel := 468871, spent := 0, income := 0, live := 15, workspace := 0, peak := 15, capacity := 256 }, physical := { phase := 1, source := 20, transferred := 0, wasted := 0 }, control := { word := 6, base := 23 } } }

def case51Events : List Event := [.install, .prepare, .reset, .advance, .advance, .advance, .advance, .advance, .advance, .sense, .checkSensor, .closeRoute]

def case51Vectors : List (List Nat) := [[468871, 468871, 0, 0, 15, 0, 15, 256, 1, 20, 0, 0, 6, 0, 0, 0, 23, 0, 0, 0, 0], [468871, 376342, 92529, 0, 33, 0, 41, 256, 1, 20, 0, 0, 6, 0, 1, 0, 23, 0, 0, 0, 3, 0, 1, 2], [468871, 368838, 100033, 0, 33, 9, 42, 256, 1, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 352410, 116461, 0, 33, 9, 44, 256, 0, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 335982, 132889, 0, 33, 9, 44, 256, 1, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 319554, 149317, 0, 33, 9, 44, 256, 2, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 303126, 165745, 0, 33, 9, 44, 256, 0, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 286698, 182173, 0, 33, 9, 44, 256, 1, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 270270, 198601, 0, 33, 9, 44, 256, 2, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 253842, 215029, 0, 33, 9, 44, 256, 0, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 237414, 231457, 0, 33, 9, 44, 256, 0, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 236302, 232569, 0, 33, 9, 44, 256, 0, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 236302, 232569, 0, 33, 0, 44, 256, 0, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2]]

def case51Observations : List (List Nat) := [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [1, 0, 0], [1, 0, 0], [1, 0, 0]]

theorem case51Certified : Runnable case51Initial case51Events ∧
    policyWord 100 case51Initial = case51Events ∧
    (history case51Initial case51Events).map vector = case51Vectors ∧
    (history case51Initial case51Events).map (fun s =>
      [optBoolCode s.body.sensor, optBoolCode s.body.receipt, boolCode s.body.actualArrival]) = case51Observations ∧
    (run case51Initial case51Events).body.error = .mismatch ∧
    nextEvent (run case51Initial case51Events) = none := by decide

#print axioms case51Certified

-- grid:35:inverted

def case52Initial : State := { H := { outputs := [true, true, false], transitions := [1, 2, 0], initial := 0 }, config := { environment := { outputs := [false, false, true], transitions := [1, 2, 0], initial := 0 }, tau := false, sigma := false, brokenReset := false, blocked := true, receiptMode := .complemented, clamp := false, deny := .none }, body := { account := { start := 468871, fuel := 468871, spent := 0, income := 0, live := 15, workspace := 0, peak := 15, capacity := 256 }, physical := { phase := 1, source := 20, transferred := 0, wasted := 0 }, control := { word := 6, base := 23 } } }

def case52Events : List Event := [.install, .prepare, .reset, .advance, .advance, .advance, .advance, .advance, .advance, .sense, .checkSensor, .closeRoute]

def case52Vectors : List (List Nat) := [[468871, 468871, 0, 0, 15, 0, 15, 256, 1, 20, 0, 0, 6, 0, 0, 0, 23, 0, 0, 0, 0], [468871, 376342, 92529, 0, 33, 0, 41, 256, 1, 20, 0, 0, 6, 0, 1, 0, 23, 0, 0, 0, 3, 0, 1, 2], [468871, 368838, 100033, 0, 33, 9, 42, 256, 1, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 352410, 116461, 0, 33, 9, 44, 256, 0, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 335982, 132889, 0, 33, 9, 44, 256, 1, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 319554, 149317, 0, 33, 9, 44, 256, 2, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 303126, 165745, 0, 33, 9, 44, 256, 0, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 286698, 182173, 0, 33, 9, 44, 256, 1, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 270270, 198601, 0, 33, 9, 44, 256, 2, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 253842, 215029, 0, 33, 9, 44, 256, 0, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 237414, 231457, 0, 33, 9, 44, 256, 0, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 236302, 232569, 0, 33, 9, 44, 256, 0, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 236302, 232569, 0, 33, 0, 44, 256, 0, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2]]

def case52Observations : List (List Nat) := [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [1, 0, 0], [1, 0, 0], [1, 0, 0]]

theorem case52Certified : Runnable case52Initial case52Events ∧
    policyWord 100 case52Initial = case52Events ∧
    (history case52Initial case52Events).map vector = case52Vectors ∧
    (history case52Initial case52Events).map (fun s =>
      [optBoolCode s.body.sensor, optBoolCode s.body.receipt, boolCode s.body.actualArrival]) = case52Observations ∧
    (run case52Initial case52Events).body.error = .mismatch ∧
    nextEvent (run case52Initial case52Events) = none := by decide

#print axioms case52Certified

-- grid:36:inverted

def case53Initial : State := { H := { outputs := [true, true, false], transitions := [1, 2, 0], initial := 0 }, config := { environment := { outputs := [false, false, true], transitions := [1, 2, 0], initial := 0 }, tau := true, sigma := true, brokenReset := false, blocked := false, receiptMode := .faithful, clamp := false, deny := .none }, body := { account := { start := 468871, fuel := 468871, spent := 0, income := 0, live := 15, workspace := 0, peak := 15, capacity := 256 }, physical := { phase := 1, source := 20, transferred := 0, wasted := 0 }, control := { word := 6, base := 23 } } }

def case53Events : List Event := [.install, .prepare, .reset, .advance, .advance, .advance, .advance, .advance, .advance, .sense, .checkSensor, .closeRoute]

def case53Vectors : List (List Nat) := [[468871, 468871, 0, 0, 15, 0, 15, 256, 1, 20, 0, 0, 6, 0, 0, 0, 23, 0, 0, 0, 0], [468871, 376342, 92529, 0, 33, 0, 41, 256, 1, 20, 0, 0, 6, 0, 1, 0, 23, 0, 0, 0, 3, 0, 1, 2], [468871, 368838, 100033, 0, 33, 9, 42, 256, 1, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 352410, 116461, 0, 33, 9, 44, 256, 0, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 335982, 132889, 0, 33, 9, 44, 256, 1, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 319554, 149317, 0, 33, 9, 44, 256, 2, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 303126, 165745, 0, 33, 9, 44, 256, 0, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 286698, 182173, 0, 33, 9, 44, 256, 1, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 270270, 198601, 0, 33, 9, 44, 256, 2, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 253842, 215029, 0, 33, 9, 44, 256, 0, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 237414, 231457, 0, 33, 9, 44, 256, 0, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 236302, 232569, 0, 33, 9, 44, 256, 0, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 236302, 232569, 0, 33, 0, 44, 256, 0, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2]]

def case53Observations : List (List Nat) := [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [1, 0, 0], [1, 0, 0], [1, 0, 0]]

theorem case53Certified : Runnable case53Initial case53Events ∧
    policyWord 100 case53Initial = case53Events ∧
    (history case53Initial case53Events).map vector = case53Vectors ∧
    (history case53Initial case53Events).map (fun s =>
      [optBoolCode s.body.sensor, optBoolCode s.body.receipt, boolCode s.body.actualArrival]) = case53Observations ∧
    (run case53Initial case53Events).body.error = .mismatch ∧
    nextEvent (run case53Initial case53Events) = none := by decide

#print axioms case53Certified

-- grid:37:inverted

def case54Initial : State := { H := { outputs := [true, true, false], transitions := [1, 2, 0], initial := 0 }, config := { environment := { outputs := [false, false, true], transitions := [1, 2, 0], initial := 0 }, tau := true, sigma := true, brokenReset := false, blocked := false, receiptMode := .missing, clamp := false, deny := .none }, body := { account := { start := 468871, fuel := 468871, spent := 0, income := 0, live := 15, workspace := 0, peak := 15, capacity := 256 }, physical := { phase := 1, source := 20, transferred := 0, wasted := 0 }, control := { word := 6, base := 23 } } }

def case54Events : List Event := [.install, .prepare, .reset, .advance, .advance, .advance, .advance, .advance, .advance, .sense, .checkSensor, .closeRoute]

def case54Vectors : List (List Nat) := [[468871, 468871, 0, 0, 15, 0, 15, 256, 1, 20, 0, 0, 6, 0, 0, 0, 23, 0, 0, 0, 0], [468871, 376342, 92529, 0, 33, 0, 41, 256, 1, 20, 0, 0, 6, 0, 1, 0, 23, 0, 0, 0, 3, 0, 1, 2], [468871, 368838, 100033, 0, 33, 9, 42, 256, 1, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 352410, 116461, 0, 33, 9, 44, 256, 0, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 335982, 132889, 0, 33, 9, 44, 256, 1, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 319554, 149317, 0, 33, 9, 44, 256, 2, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 303126, 165745, 0, 33, 9, 44, 256, 0, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 286698, 182173, 0, 33, 9, 44, 256, 1, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 270270, 198601, 0, 33, 9, 44, 256, 2, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 253842, 215029, 0, 33, 9, 44, 256, 0, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 237414, 231457, 0, 33, 9, 44, 256, 0, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 236302, 232569, 0, 33, 9, 44, 256, 0, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 236302, 232569, 0, 33, 0, 44, 256, 0, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2]]

def case54Observations : List (List Nat) := [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [1, 0, 0], [1, 0, 0], [1, 0, 0]]

theorem case54Certified : Runnable case54Initial case54Events ∧
    policyWord 100 case54Initial = case54Events ∧
    (history case54Initial case54Events).map vector = case54Vectors ∧
    (history case54Initial case54Events).map (fun s =>
      [optBoolCode s.body.sensor, optBoolCode s.body.receipt, boolCode s.body.actualArrival]) = case54Observations ∧
    (run case54Initial case54Events).body.error = .mismatch ∧
    nextEvent (run case54Initial case54Events) = none := by decide

#print axioms case54Certified

-- grid:38:inverted

def case55Initial : State := { H := { outputs := [true, true, false], transitions := [1, 2, 0], initial := 0 }, config := { environment := { outputs := [false, false, true], transitions := [1, 2, 0], initial := 0 }, tau := true, sigma := true, brokenReset := false, blocked := false, receiptMode := .complemented, clamp := false, deny := .none }, body := { account := { start := 468871, fuel := 468871, spent := 0, income := 0, live := 15, workspace := 0, peak := 15, capacity := 256 }, physical := { phase := 1, source := 20, transferred := 0, wasted := 0 }, control := { word := 6, base := 23 } } }

def case55Events : List Event := [.install, .prepare, .reset, .advance, .advance, .advance, .advance, .advance, .advance, .sense, .checkSensor, .closeRoute]

def case55Vectors : List (List Nat) := [[468871, 468871, 0, 0, 15, 0, 15, 256, 1, 20, 0, 0, 6, 0, 0, 0, 23, 0, 0, 0, 0], [468871, 376342, 92529, 0, 33, 0, 41, 256, 1, 20, 0, 0, 6, 0, 1, 0, 23, 0, 0, 0, 3, 0, 1, 2], [468871, 368838, 100033, 0, 33, 9, 42, 256, 1, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 352410, 116461, 0, 33, 9, 44, 256, 0, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 335982, 132889, 0, 33, 9, 44, 256, 1, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 319554, 149317, 0, 33, 9, 44, 256, 2, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 303126, 165745, 0, 33, 9, 44, 256, 0, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 286698, 182173, 0, 33, 9, 44, 256, 1, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 270270, 198601, 0, 33, 9, 44, 256, 2, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 253842, 215029, 0, 33, 9, 44, 256, 0, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 237414, 231457, 0, 33, 9, 44, 256, 0, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 236302, 232569, 0, 33, 9, 44, 256, 0, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 236302, 232569, 0, 33, 0, 44, 256, 0, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2]]

def case55Observations : List (List Nat) := [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [1, 0, 0], [1, 0, 0], [1, 0, 0]]

theorem case55Certified : Runnable case55Initial case55Events ∧
    policyWord 100 case55Initial = case55Events ∧
    (history case55Initial case55Events).map vector = case55Vectors ∧
    (history case55Initial case55Events).map (fun s =>
      [optBoolCode s.body.sensor, optBoolCode s.body.receipt, boolCode s.body.actualArrival]) = case55Observations ∧
    (run case55Initial case55Events).body.error = .mismatch ∧
    nextEvent (run case55Initial case55Events) = none := by decide

#print axioms case55Certified

-- grid:39:inverted

def case56Initial : State := { H := { outputs := [true, true, false], transitions := [1, 2, 0], initial := 0 }, config := { environment := { outputs := [false, false, true], transitions := [1, 2, 0], initial := 0 }, tau := true, sigma := true, brokenReset := false, blocked := true, receiptMode := .faithful, clamp := false, deny := .none }, body := { account := { start := 468871, fuel := 468871, spent := 0, income := 0, live := 15, workspace := 0, peak := 15, capacity := 256 }, physical := { phase := 1, source := 20, transferred := 0, wasted := 0 }, control := { word := 6, base := 23 } } }

def case56Events : List Event := [.install, .prepare, .reset, .advance, .advance, .advance, .advance, .advance, .advance, .sense, .checkSensor, .closeRoute]

def case56Vectors : List (List Nat) := [[468871, 468871, 0, 0, 15, 0, 15, 256, 1, 20, 0, 0, 6, 0, 0, 0, 23, 0, 0, 0, 0], [468871, 376342, 92529, 0, 33, 0, 41, 256, 1, 20, 0, 0, 6, 0, 1, 0, 23, 0, 0, 0, 3, 0, 1, 2], [468871, 368838, 100033, 0, 33, 9, 42, 256, 1, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 352410, 116461, 0, 33, 9, 44, 256, 0, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 335982, 132889, 0, 33, 9, 44, 256, 1, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 319554, 149317, 0, 33, 9, 44, 256, 2, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 303126, 165745, 0, 33, 9, 44, 256, 0, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 286698, 182173, 0, 33, 9, 44, 256, 1, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 270270, 198601, 0, 33, 9, 44, 256, 2, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 253842, 215029, 0, 33, 9, 44, 256, 0, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 237414, 231457, 0, 33, 9, 44, 256, 0, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 236302, 232569, 0, 33, 9, 44, 256, 0, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 236302, 232569, 0, 33, 0, 44, 256, 0, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2]]

def case56Observations : List (List Nat) := [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [1, 0, 0], [1, 0, 0], [1, 0, 0]]

theorem case56Certified : Runnable case56Initial case56Events ∧
    policyWord 100 case56Initial = case56Events ∧
    (history case56Initial case56Events).map vector = case56Vectors ∧
    (history case56Initial case56Events).map (fun s =>
      [optBoolCode s.body.sensor, optBoolCode s.body.receipt, boolCode s.body.actualArrival]) = case56Observations ∧
    (run case56Initial case56Events).body.error = .mismatch ∧
    nextEvent (run case56Initial case56Events) = none := by decide

#print axioms case56Certified

-- grid:40:inverted

def case57Initial : State := { H := { outputs := [true, true, false], transitions := [1, 2, 0], initial := 0 }, config := { environment := { outputs := [false, false, true], transitions := [1, 2, 0], initial := 0 }, tau := true, sigma := true, brokenReset := false, blocked := true, receiptMode := .missing, clamp := false, deny := .none }, body := { account := { start := 468871, fuel := 468871, spent := 0, income := 0, live := 15, workspace := 0, peak := 15, capacity := 256 }, physical := { phase := 1, source := 20, transferred := 0, wasted := 0 }, control := { word := 6, base := 23 } } }

def case57Events : List Event := [.install, .prepare, .reset, .advance, .advance, .advance, .advance, .advance, .advance, .sense, .checkSensor, .closeRoute]

def case57Vectors : List (List Nat) := [[468871, 468871, 0, 0, 15, 0, 15, 256, 1, 20, 0, 0, 6, 0, 0, 0, 23, 0, 0, 0, 0], [468871, 376342, 92529, 0, 33, 0, 41, 256, 1, 20, 0, 0, 6, 0, 1, 0, 23, 0, 0, 0, 3, 0, 1, 2], [468871, 368838, 100033, 0, 33, 9, 42, 256, 1, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 352410, 116461, 0, 33, 9, 44, 256, 0, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 335982, 132889, 0, 33, 9, 44, 256, 1, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 319554, 149317, 0, 33, 9, 44, 256, 2, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 303126, 165745, 0, 33, 9, 44, 256, 0, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 286698, 182173, 0, 33, 9, 44, 256, 1, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 270270, 198601, 0, 33, 9, 44, 256, 2, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 253842, 215029, 0, 33, 9, 44, 256, 0, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 237414, 231457, 0, 33, 9, 44, 256, 0, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 236302, 232569, 0, 33, 9, 44, 256, 0, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 236302, 232569, 0, 33, 0, 44, 256, 0, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2]]

def case57Observations : List (List Nat) := [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [1, 0, 0], [1, 0, 0], [1, 0, 0]]

theorem case57Certified : Runnable case57Initial case57Events ∧
    policyWord 100 case57Initial = case57Events ∧
    (history case57Initial case57Events).map vector = case57Vectors ∧
    (history case57Initial case57Events).map (fun s =>
      [optBoolCode s.body.sensor, optBoolCode s.body.receipt, boolCode s.body.actualArrival]) = case57Observations ∧
    (run case57Initial case57Events).body.error = .mismatch ∧
    nextEvent (run case57Initial case57Events) = none := by decide

#print axioms case57Certified

-- grid:41:inverted

def case58Initial : State := { H := { outputs := [true, true, false], transitions := [1, 2, 0], initial := 0 }, config := { environment := { outputs := [false, false, true], transitions := [1, 2, 0], initial := 0 }, tau := true, sigma := true, brokenReset := false, blocked := true, receiptMode := .complemented, clamp := false, deny := .none }, body := { account := { start := 468871, fuel := 468871, spent := 0, income := 0, live := 15, workspace := 0, peak := 15, capacity := 256 }, physical := { phase := 1, source := 20, transferred := 0, wasted := 0 }, control := { word := 6, base := 23 } } }

def case58Events : List Event := [.install, .prepare, .reset, .advance, .advance, .advance, .advance, .advance, .advance, .sense, .checkSensor, .closeRoute]

def case58Vectors : List (List Nat) := [[468871, 468871, 0, 0, 15, 0, 15, 256, 1, 20, 0, 0, 6, 0, 0, 0, 23, 0, 0, 0, 0], [468871, 376342, 92529, 0, 33, 0, 41, 256, 1, 20, 0, 0, 6, 0, 1, 0, 23, 0, 0, 0, 3, 0, 1, 2], [468871, 368838, 100033, 0, 33, 9, 42, 256, 1, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 352410, 116461, 0, 33, 9, 44, 256, 0, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 335982, 132889, 0, 33, 9, 44, 256, 1, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 319554, 149317, 0, 33, 9, 44, 256, 2, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 303126, 165745, 0, 33, 9, 44, 256, 0, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 286698, 182173, 0, 33, 9, 44, 256, 1, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 270270, 198601, 0, 33, 9, 44, 256, 2, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 253842, 215029, 0, 33, 9, 44, 256, 0, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 237414, 231457, 0, 33, 9, 44, 256, 0, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 236302, 232569, 0, 33, 9, 44, 256, 0, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 236302, 232569, 0, 33, 0, 44, 256, 0, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2]]

def case58Observations : List (List Nat) := [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [1, 0, 0], [1, 0, 0], [1, 0, 0]]

theorem case58Certified : Runnable case58Initial case58Events ∧
    policyWord 100 case58Initial = case58Events ∧
    (history case58Initial case58Events).map vector = case58Vectors ∧
    (history case58Initial case58Events).map (fun s =>
      [optBoolCode s.body.sensor, optBoolCode s.body.receipt, boolCode s.body.actualArrival]) = case58Observations ∧
    (run case58Initial case58Events).body.error = .mismatch ∧
    nextEvent (run case58Initial case58Events) = none := by decide

#print axioms case58Certified

-- grid:42:inverted

def case59Initial : State := { H := { outputs := [true, true, false], transitions := [1, 2, 0], initial := 0 }, config := { environment := { outputs := [false, false, true], transitions := [1, 2, 0], initial := 0 }, tau := true, sigma := false, brokenReset := false, blocked := false, receiptMode := .faithful, clamp := false, deny := .none }, body := { account := { start := 468871, fuel := 468871, spent := 0, income := 0, live := 15, workspace := 0, peak := 15, capacity := 256 }, physical := { phase := 1, source := 20, transferred := 0, wasted := 0 }, control := { word := 6, base := 23 } } }

def case59Events : List Event := [.install, .prepare, .reset, .advance, .advance, .advance, .advance, .advance, .advance, .sense, .checkSensor, .extract, .readReceipt, .commit, .closeRoute, .stop, .retain]

def case59Vectors : List (List Nat) := [[468871, 468871, 0, 0, 15, 0, 15, 256, 1, 20, 0, 0, 6, 0, 0, 0, 23, 0, 0, 0, 0], [468871, 376342, 92529, 0, 33, 0, 41, 256, 1, 20, 0, 0, 6, 0, 1, 0, 23, 0, 0, 0, 3, 0, 1, 2], [468871, 368838, 100033, 0, 33, 9, 42, 256, 1, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 352410, 116461, 0, 33, 9, 44, 256, 0, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 335982, 132889, 0, 33, 9, 44, 256, 1, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 319554, 149317, 0, 33, 9, 44, 256, 2, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 303126, 165745, 0, 33, 9, 44, 256, 0, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 286698, 182173, 0, 33, 9, 44, 256, 1, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 270270, 198601, 0, 33, 9, 44, 256, 2, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 253842, 215029, 0, 33, 9, 44, 256, 0, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 237414, 231457, 0, 33, 9, 44, 256, 0, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 236302, 232569, 0, 33, 9, 44, 256, 0, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 875234, 248997, 655360, 33, 9, 44, 256, 0, 10, 10, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 858806, 265425, 655360, 33, 9, 44, 256, 0, 10, 10, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 846118, 278113, 655360, 31, 9, 50, 256, 0, 10, 10, 0, 6, 1, 3, 0, 23, 2, 2, 2, 1, 0], [468871, 846118, 278113, 655360, 31, 0, 50, 256, 0, 10, 10, 0, 6, 1, 3, 0, 23, 2, 2, 2, 1, 0], [468871, 846118, 278113, 655360, 31, 0, 50, 256, 0, 10, 10, 0, 6, 1, 3, 0, 23, 2, 2, 2, 1, 0], [468871, 813288, 310943, 655360, 31, 0, 50, 256, 0, 10, 10, 0, 6, 1, 5, 1, 23, 2, 2, 2, 1, 0]]

def case59Observations : List (List Nat) := [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [2, 0, 0], [2, 0, 0], [2, 0, 1], [2, 2, 1], [2, 2, 1], [2, 2, 1], [2, 2, 1], [2, 2, 1]]

theorem case59Certified : Runnable case59Initial case59Events ∧
    policyWord 100 case59Initial = case59Events ∧
    (history case59Initial case59Events).map vector = case59Vectors ∧
    (history case59Initial case59Events).map (fun s =>
      [optBoolCode s.body.sensor, optBoolCode s.body.receipt, boolCode s.body.actualArrival]) = case59Observations ∧
    (run case59Initial case59Events).body.error = .none ∧
    nextEvent (run case59Initial case59Events) = none := by decide

#print axioms case59Certified

-- grid:43:inverted

def case60Initial : State := { H := { outputs := [true, true, false], transitions := [1, 2, 0], initial := 0 }, config := { environment := { outputs := [false, false, true], transitions := [1, 2, 0], initial := 0 }, tau := true, sigma := false, brokenReset := false, blocked := false, receiptMode := .missing, clamp := false, deny := .none }, body := { account := { start := 468871, fuel := 468871, spent := 0, income := 0, live := 15, workspace := 0, peak := 15, capacity := 256 }, physical := { phase := 1, source := 20, transferred := 0, wasted := 0 }, control := { word := 6, base := 23 } } }

def case60Events : List Event := [.install, .prepare, .reset, .advance, .advance, .advance, .advance, .advance, .advance, .sense, .checkSensor, .extract, .readReceipt, .closeRoute]

def case60Vectors : List (List Nat) := [[468871, 468871, 0, 0, 15, 0, 15, 256, 1, 20, 0, 0, 6, 0, 0, 0, 23, 0, 0, 0, 0], [468871, 376342, 92529, 0, 33, 0, 41, 256, 1, 20, 0, 0, 6, 0, 1, 0, 23, 0, 0, 0, 3, 0, 1, 2], [468871, 368838, 100033, 0, 33, 9, 42, 256, 1, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 352410, 116461, 0, 33, 9, 44, 256, 0, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 335982, 132889, 0, 33, 9, 44, 256, 1, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 319554, 149317, 0, 33, 9, 44, 256, 2, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 303126, 165745, 0, 33, 9, 44, 256, 0, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 286698, 182173, 0, 33, 9, 44, 256, 1, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 270270, 198601, 0, 33, 9, 44, 256, 2, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 253842, 215029, 0, 33, 9, 44, 256, 0, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 237414, 231457, 0, 33, 9, 44, 256, 0, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 236302, 232569, 0, 33, 9, 44, 256, 0, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 875234, 248997, 655360, 33, 9, 44, 256, 0, 10, 10, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 858806, 265425, 655360, 33, 9, 44, 256, 0, 10, 10, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 858806, 265425, 655360, 33, 0, 44, 256, 0, 10, 10, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2]]

def case60Observations : List (List Nat) := [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [2, 0, 0], [2, 0, 0], [2, 0, 1], [2, 0, 1], [2, 0, 1]]

theorem case60Certified : Runnable case60Initial case60Events ∧
    policyWord 100 case60Initial = case60Events ∧
    (history case60Initial case60Events).map vector = case60Vectors ∧
    (history case60Initial case60Events).map (fun s =>
      [optBoolCode s.body.sensor, optBoolCode s.body.receipt, boolCode s.body.actualArrival]) = case60Observations ∧
    (run case60Initial case60Events).body.error = .missing ∧
    nextEvent (run case60Initial case60Events) = none := by decide

#print axioms case60Certified

-- grid:44:inverted

def case61Initial : State := { H := { outputs := [true, true, false], transitions := [1, 2, 0], initial := 0 }, config := { environment := { outputs := [false, false, true], transitions := [1, 2, 0], initial := 0 }, tau := true, sigma := false, brokenReset := false, blocked := false, receiptMode := .complemented, clamp := false, deny := .none }, body := { account := { start := 468871, fuel := 468871, spent := 0, income := 0, live := 15, workspace := 0, peak := 15, capacity := 256 }, physical := { phase := 1, source := 20, transferred := 0, wasted := 0 }, control := { word := 6, base := 23 } } }

def case61Events : List Event := [.install, .prepare, .reset, .advance, .advance, .advance, .advance, .advance, .advance, .sense, .checkSensor, .extract, .readReceipt, .commit, .closeRoute, .scan, .scan, .scan, .select, .prepare, .reset, .advance, .advance, .sense, .checkSensor, .extract, .readReceipt, .commit, .closeRoute, .retain]

def case61Vectors : List (List Nat) := [[468871, 468871, 0, 0, 15, 0, 15, 256, 1, 20, 0, 0, 6, 0, 0, 0, 23, 0, 0, 0, 0], [468871, 376342, 92529, 0, 33, 0, 41, 256, 1, 20, 0, 0, 6, 0, 1, 0, 23, 0, 0, 0, 3, 0, 1, 2], [468871, 368838, 100033, 0, 33, 9, 42, 256, 1, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 352410, 116461, 0, 33, 9, 44, 256, 0, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 335982, 132889, 0, 33, 9, 44, 256, 1, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 319554, 149317, 0, 33, 9, 44, 256, 2, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 303126, 165745, 0, 33, 9, 44, 256, 0, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 286698, 182173, 0, 33, 9, 44, 256, 1, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 270270, 198601, 0, 33, 9, 44, 256, 2, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 253842, 215029, 0, 33, 9, 44, 256, 0, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 237414, 231457, 0, 33, 9, 44, 256, 0, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 236302, 232569, 0, 33, 9, 44, 256, 0, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 875234, 248997, 655360, 33, 9, 44, 256, 0, 10, 10, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 858806, 265425, 655360, 33, 9, 44, 256, 0, 10, 10, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 845094, 279137, 655360, 32, 9, 50, 256, 0, 10, 10, 0, 6, 1, 3, 0, 23, 2, 2, 1, 2, 1, 2], [468871, 845094, 279137, 655360, 32, 0, 50, 256, 0, 10, 10, 0, 6, 1, 3, 0, 23, 2, 2, 1, 2, 1, 2], [468871, 840813, 283418, 655360, 32, 0, 50, 256, 0, 10, 10, 0, 6, 1, 3, 0, 23, 2, 2, 1, 2, 1, 2], [468871, 834403, 289828, 655360, 32, 0, 50, 256, 0, 10, 10, 0, 6, 1, 3, 0, 23, 2, 2, 1, 2, 1, 2], [468871, 825860, 298371, 655360, 32, 0, 50, 256, 0, 10, 10, 0, 6, 1, 3, 0, 23, 2, 2, 1, 2, 1, 2], [468871, 818544, 305687, 655360, 28, 0, 50, 256, 0, 10, 10, 0, 2, 1, 4, 0, 23, 2, 2, 1, 2, 1, 2], [468871, 815340, 308891, 655360, 28, 5, 50, 256, 0, 10, 10, 0, 2, 1, 2, 0, 23, 1, 2, 1, 2, 1, 2], [468871, 798921, 325310, 655360, 28, 5, 50, 256, 0, 10, 10, 0, 2, 1, 2, 0, 23, 1, 2, 1, 2, 1, 2], [468871, 782502, 341729, 655360, 28, 5, 50, 256, 1, 10, 10, 0, 2, 1, 2, 0, 23, 1, 2, 1, 2, 1, 2], [468871, 766083, 358148, 655360, 28, 5, 50, 256, 2, 10, 10, 0, 2, 1, 2, 0, 23, 1, 2, 1, 2, 1, 2], [468871, 749664, 374567, 655360, 28, 5, 50, 256, 2, 10, 10, 0, 2, 1, 2, 0, 23, 1, 2, 1, 2, 1, 2], [468871, 748570, 375661, 655360, 28, 5, 50, 256, 2, 10, 10, 0, 2, 1, 2, 0, 23, 1, 2, 1, 2, 1, 2], [468871, 732151, 392080, 655360, 28, 5, 50, 256, 2, 0, 10, 10, 2, 1, 2, 0, 23, 1, 2, 1, 2, 1, 2], [468871, 715732, 408499, 655360, 28, 5, 50, 256, 2, 0, 10, 10, 2, 1, 2, 0, 23, 1, 2, 1, 2, 1, 2], [468871, 705258, 418973, 655360, 27, 5, 50, 256, 2, 0, 10, 10, 2, 2, 3, 0, 23, 1, 1, 2, 1, 1], [468871, 705258, 418973, 655360, 27, 0, 50, 256, 2, 0, 10, 10, 2, 2, 3, 0, 23, 1, 1, 2, 1, 1], [468871, 676532, 447699, 655360, 27, 0, 50, 256, 2, 0, 10, 10, 2, 2, 5, 1, 23, 1, 1, 2, 1, 1]]

def case61Observations : List (List Nat) := [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [2, 0, 0], [2, 0, 0], [2, 0, 1], [2, 1, 1], [2, 1, 1], [2, 1, 1], [2, 1, 1], [2, 1, 1], [2, 1, 1], [2, 1, 1], [0, 0, 1], [0, 0, 1], [0, 0, 1], [0, 0, 1], [1, 0, 1], [1, 0, 1], [1, 0, 0], [1, 2, 0], [1, 2, 0], [1, 2, 0], [1, 2, 0]]

theorem case61Certified : Runnable case61Initial case61Events ∧
    policyWord 100 case61Initial = case61Events ∧
    (history case61Initial case61Events).map vector = case61Vectors ∧
    (history case61Initial case61Events).map (fun s =>
      [optBoolCode s.body.sensor, optBoolCode s.body.receipt, boolCode s.body.actualArrival]) = case61Observations ∧
    (run case61Initial case61Events).body.error = .none ∧
    nextEvent (run case61Initial case61Events) = none := by decide

#print axioms case61Certified

-- grid:45:inverted

def case62Initial : State := { H := { outputs := [true, true, false], transitions := [1, 2, 0], initial := 0 }, config := { environment := { outputs := [false, false, true], transitions := [1, 2, 0], initial := 0 }, tau := true, sigma := false, brokenReset := false, blocked := true, receiptMode := .faithful, clamp := false, deny := .none }, body := { account := { start := 468871, fuel := 468871, spent := 0, income := 0, live := 15, workspace := 0, peak := 15, capacity := 256 }, physical := { phase := 1, source := 20, transferred := 0, wasted := 0 }, control := { word := 6, base := 23 } } }

def case62Events : List Event := [.install, .prepare, .reset, .advance, .advance, .advance, .advance, .advance, .advance, .sense, .checkSensor, .extract, .readReceipt, .commit, .closeRoute, .scan, .scan, .scan, .select, .prepare, .reset, .advance, .advance, .sense, .checkSensor, .extract, .readReceipt, .commit, .closeRoute, .retain]

def case62Vectors : List (List Nat) := [[468871, 468871, 0, 0, 15, 0, 15, 256, 1, 20, 0, 0, 6, 0, 0, 0, 23, 0, 0, 0, 0], [468871, 376342, 92529, 0, 33, 0, 41, 256, 1, 20, 0, 0, 6, 0, 1, 0, 23, 0, 0, 0, 3, 0, 1, 2], [468871, 368838, 100033, 0, 33, 9, 42, 256, 1, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 352410, 116461, 0, 33, 9, 44, 256, 0, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 335982, 132889, 0, 33, 9, 44, 256, 1, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 319554, 149317, 0, 33, 9, 44, 256, 2, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 303126, 165745, 0, 33, 9, 44, 256, 0, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 286698, 182173, 0, 33, 9, 44, 256, 1, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 270270, 198601, 0, 33, 9, 44, 256, 2, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 253842, 215029, 0, 33, 9, 44, 256, 0, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 237414, 231457, 0, 33, 9, 44, 256, 0, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 236302, 232569, 0, 33, 9, 44, 256, 0, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 219874, 248997, 0, 33, 9, 44, 256, 0, 10, 0, 10, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 203446, 265425, 0, 33, 9, 44, 256, 0, 10, 0, 10, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 189734, 279137, 0, 32, 9, 50, 256, 0, 10, 0, 10, 6, 1, 3, 0, 23, 2, 2, 1, 2, 1, 2], [468871, 189734, 279137, 0, 32, 0, 50, 256, 0, 10, 0, 10, 6, 1, 3, 0, 23, 2, 2, 1, 2, 1, 2], [468871, 185453, 283418, 0, 32, 0, 50, 256, 0, 10, 0, 10, 6, 1, 3, 0, 23, 2, 2, 1, 2, 1, 2], [468871, 179043, 289828, 0, 32, 0, 50, 256, 0, 10, 0, 10, 6, 1, 3, 0, 23, 2, 2, 1, 2, 1, 2], [468871, 170500, 298371, 0, 32, 0, 50, 256, 0, 10, 0, 10, 6, 1, 3, 0, 23, 2, 2, 1, 2, 1, 2], [468871, 163184, 305687, 0, 28, 0, 50, 256, 0, 10, 0, 10, 2, 1, 4, 0, 23, 2, 2, 1, 2, 1, 2], [468871, 159980, 308891, 0, 28, 5, 50, 256, 0, 10, 0, 10, 2, 1, 2, 0, 23, 1, 2, 1, 2, 1, 2], [468871, 143561, 325310, 0, 28, 5, 50, 256, 0, 10, 0, 10, 2, 1, 2, 0, 23, 1, 2, 1, 2, 1, 2], [468871, 127142, 341729, 0, 28, 5, 50, 256, 1, 10, 0, 10, 2, 1, 2, 0, 23, 1, 2, 1, 2, 1, 2], [468871, 110723, 358148, 0, 28, 5, 50, 256, 2, 10, 0, 10, 2, 1, 2, 0, 23, 1, 2, 1, 2, 1, 2], [468871, 94304, 374567, 0, 28, 5, 50, 256, 2, 10, 0, 10, 2, 1, 2, 0, 23, 1, 2, 1, 2, 1, 2], [468871, 93210, 375661, 0, 28, 5, 50, 256, 2, 10, 0, 10, 2, 1, 2, 0, 23, 1, 2, 1, 2, 1, 2], [468871, 76791, 392080, 0, 28, 5, 50, 256, 2, 0, 0, 20, 2, 1, 2, 0, 23, 1, 2, 1, 2, 1, 2], [468871, 60372, 408499, 0, 28, 5, 50, 256, 2, 0, 0, 20, 2, 1, 2, 0, 23, 1, 2, 1, 2, 1, 2], [468871, 49898, 418973, 0, 27, 5, 50, 256, 2, 0, 0, 20, 2, 2, 3, 0, 23, 1, 1, 1, 1, 2], [468871, 49898, 418973, 0, 27, 0, 50, 256, 2, 0, 0, 20, 2, 2, 3, 0, 23, 1, 1, 1, 1, 2], [468871, 21172, 447699, 0, 27, 0, 50, 256, 2, 0, 0, 20, 2, 2, 5, 1, 23, 1, 1, 1, 1, 2]]

def case62Observations : List (List Nat) := [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [2, 0, 0], [2, 0, 0], [2, 0, 0], [2, 1, 0], [2, 1, 0], [2, 1, 0], [2, 1, 0], [2, 1, 0], [2, 1, 0], [2, 1, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [1, 0, 0], [1, 0, 0], [1, 0, 0], [1, 1, 0], [1, 1, 0], [1, 1, 0], [1, 1, 0]]

theorem case62Certified : Runnable case62Initial case62Events ∧
    policyWord 100 case62Initial = case62Events ∧
    (history case62Initial case62Events).map vector = case62Vectors ∧
    (history case62Initial case62Events).map (fun s =>
      [optBoolCode s.body.sensor, optBoolCode s.body.receipt, boolCode s.body.actualArrival]) = case62Observations ∧
    (run case62Initial case62Events).body.error = .none ∧
    nextEvent (run case62Initial case62Events) = none := by decide

#print axioms case62Certified

-- grid:46:inverted

def case63Initial : State := { H := { outputs := [true, true, false], transitions := [1, 2, 0], initial := 0 }, config := { environment := { outputs := [false, false, true], transitions := [1, 2, 0], initial := 0 }, tau := true, sigma := false, brokenReset := false, blocked := true, receiptMode := .missing, clamp := false, deny := .none }, body := { account := { start := 468871, fuel := 468871, spent := 0, income := 0, live := 15, workspace := 0, peak := 15, capacity := 256 }, physical := { phase := 1, source := 20, transferred := 0, wasted := 0 }, control := { word := 6, base := 23 } } }

def case63Events : List Event := [.install, .prepare, .reset, .advance, .advance, .advance, .advance, .advance, .advance, .sense, .checkSensor, .extract, .readReceipt, .closeRoute]

def case63Vectors : List (List Nat) := [[468871, 468871, 0, 0, 15, 0, 15, 256, 1, 20, 0, 0, 6, 0, 0, 0, 23, 0, 0, 0, 0], [468871, 376342, 92529, 0, 33, 0, 41, 256, 1, 20, 0, 0, 6, 0, 1, 0, 23, 0, 0, 0, 3, 0, 1, 2], [468871, 368838, 100033, 0, 33, 9, 42, 256, 1, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 352410, 116461, 0, 33, 9, 44, 256, 0, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 335982, 132889, 0, 33, 9, 44, 256, 1, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 319554, 149317, 0, 33, 9, 44, 256, 2, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 303126, 165745, 0, 33, 9, 44, 256, 0, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 286698, 182173, 0, 33, 9, 44, 256, 1, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 270270, 198601, 0, 33, 9, 44, 256, 2, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 253842, 215029, 0, 33, 9, 44, 256, 0, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 237414, 231457, 0, 33, 9, 44, 256, 0, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 236302, 232569, 0, 33, 9, 44, 256, 0, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 219874, 248997, 0, 33, 9, 44, 256, 0, 10, 0, 10, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 203446, 265425, 0, 33, 9, 44, 256, 0, 10, 0, 10, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 203446, 265425, 0, 33, 0, 44, 256, 0, 10, 0, 10, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2]]

def case63Observations : List (List Nat) := [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [2, 0, 0], [2, 0, 0], [2, 0, 0], [2, 0, 0], [2, 0, 0]]

theorem case63Certified : Runnable case63Initial case63Events ∧
    policyWord 100 case63Initial = case63Events ∧
    (history case63Initial case63Events).map vector = case63Vectors ∧
    (history case63Initial case63Events).map (fun s =>
      [optBoolCode s.body.sensor, optBoolCode s.body.receipt, boolCode s.body.actualArrival]) = case63Observations ∧
    (run case63Initial case63Events).body.error = .missing ∧
    nextEvent (run case63Initial case63Events) = none := by decide

#print axioms case63Certified

-- grid:47:inverted

def case64Initial : State := { H := { outputs := [true, true, false], transitions := [1, 2, 0], initial := 0 }, config := { environment := { outputs := [false, false, true], transitions := [1, 2, 0], initial := 0 }, tau := true, sigma := false, brokenReset := false, blocked := true, receiptMode := .complemented, clamp := false, deny := .none }, body := { account := { start := 468871, fuel := 468871, spent := 0, income := 0, live := 15, workspace := 0, peak := 15, capacity := 256 }, physical := { phase := 1, source := 20, transferred := 0, wasted := 0 }, control := { word := 6, base := 23 } } }

def case64Events : List Event := [.install, .prepare, .reset, .advance, .advance, .advance, .advance, .advance, .advance, .sense, .checkSensor, .extract, .readReceipt, .commit, .closeRoute, .stop, .retain]

def case64Vectors : List (List Nat) := [[468871, 468871, 0, 0, 15, 0, 15, 256, 1, 20, 0, 0, 6, 0, 0, 0, 23, 0, 0, 0, 0], [468871, 376342, 92529, 0, 33, 0, 41, 256, 1, 20, 0, 0, 6, 0, 1, 0, 23, 0, 0, 0, 3, 0, 1, 2], [468871, 368838, 100033, 0, 33, 9, 42, 256, 1, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 352410, 116461, 0, 33, 9, 44, 256, 0, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 335982, 132889, 0, 33, 9, 44, 256, 1, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 319554, 149317, 0, 33, 9, 44, 256, 2, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 303126, 165745, 0, 33, 9, 44, 256, 0, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 286698, 182173, 0, 33, 9, 44, 256, 1, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 270270, 198601, 0, 33, 9, 44, 256, 2, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 253842, 215029, 0, 33, 9, 44, 256, 0, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 237414, 231457, 0, 33, 9, 44, 256, 0, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 236302, 232569, 0, 33, 9, 44, 256, 0, 20, 0, 0, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 219874, 248997, 0, 33, 9, 44, 256, 0, 10, 0, 10, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 203446, 265425, 0, 33, 9, 44, 256, 0, 10, 0, 10, 6, 0, 2, 0, 23, 2, 0, 0, 3, 0, 1, 2], [468871, 190758, 278113, 0, 31, 9, 50, 256, 0, 10, 0, 10, 6, 1, 3, 0, 23, 2, 2, 2, 1, 0], [468871, 190758, 278113, 0, 31, 0, 50, 256, 0, 10, 0, 10, 6, 1, 3, 0, 23, 2, 2, 2, 1, 0], [468871, 190758, 278113, 0, 31, 0, 50, 256, 0, 10, 0, 10, 6, 1, 3, 0, 23, 2, 2, 2, 1, 0], [468871, 157928, 310943, 0, 31, 0, 50, 256, 0, 10, 0, 10, 6, 1, 5, 1, 23, 2, 2, 2, 1, 0]]

def case64Observations : List (List Nat) := [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [2, 0, 0], [2, 0, 0], [2, 0, 0], [2, 2, 0], [2, 2, 0], [2, 2, 0], [2, 2, 0], [2, 2, 0]]

theorem case64Certified : Runnable case64Initial case64Events ∧
    policyWord 100 case64Initial = case64Events ∧
    (history case64Initial case64Events).map vector = case64Vectors ∧
    (history case64Initial case64Events).map (fun s =>
      [optBoolCode s.body.sensor, optBoolCode s.body.receipt, boolCode s.body.actualArrival]) = case64Observations ∧
    (run case64Initial case64Events).body.error = .none ∧
    nextEvent (run case64Initial case64Events) = none := by decide

#print axioms case64Certified

end ApplicabilityFixtures
