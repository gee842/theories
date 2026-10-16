# P81 registration (to apply after P69's `Becoming.Unfolding` lands)

No existing module's statements change. Registering the new core module touches two existing files:

1. `experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming.lean`
   - imports: add `import Becoming.Branching` after `import Becoming.Unfolding` (it imports
     `Becoming.Unfolding`, `Becoming.Attraction` and `Becoming.Capture`).
   - docstring bullet (after the `Becoming.Unfolding` bullet):

     * `Becoming.Branching` (L3): R6's and P67's laws for every process, whose course branches
       (P81). A configuration that returns can be had at every step, and every configuration
       returns exactly where every region the process never leaves keeps every possibility of
       its own; keeping every possibility does not give returning, merging nothing gives it along
       runs, and a merge need not lose a possibility. Every process necessarily draws exactly
       what does not return; possibly drawn is losing oneself on some course and allows return.
       Determinacy is determinacy up to likeness with configurations named; theorems of
       `Experiment` and `Mechanism` stated with `Determined` are restated up to likeness, and
       those needing equality are named with witnesses. Capture's rule region is absorbing and a
       reform of the state alone is drawn into what the rule holds.

2. `check_becoming.py`: add `"Becoming.Branching"` to `CORE` after `"Becoming.Unfolding"`.

The module also adds theorems to existing namespaces (no existing declaration changed):
`Becoming.Run.{onward, enters_returning, possiblyDrawnInto, window_length, FixesAlike,
fixesAlike_of_takes, TakesAlike, not_fixesAlike_of_untaken, FixesThroughAlike, generalizesAlike}`,
`Becoming.Reach.of_dead_end`, `Becoming.Law.{rule_absorbing, held_absorbing, reform_drawnInto}`,
`Becoming.Twins.{determinedAt, retargeted, retarget_breaks}`,
`Becoming.Coarse.{flips, still, turnedPart, turned, firstFrame, first_bisimulation,
first_determinedAt, meet_and_part}`, `Becoming.Confound.refutes_registered`,
`Becoming.Captured.{keeps, not_ne, rule_region_absorbing, held_absorbing, state_reform_drawn,
rule_reform_drawn}`.
