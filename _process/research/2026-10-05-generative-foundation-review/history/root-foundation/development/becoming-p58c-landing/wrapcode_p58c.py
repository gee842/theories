#!/usr/bin/env python3
"""P58c: hand-wrap the code lines the renames made longer than 100 characters. Usage: wrapcode_p58c.py TREE"""
import sys
from pathlib import Path
B = Path(sys.argv[1]) / 'Becoming'
EDITS = {
 'Dissipation.lean': [
  ('theorem Dissipative.finite_taking_not_recurring (balances : L.Balances W) (dissipative : L.Dissipative)\n',
   'theorem Dissipative.finite_taking_not_recurring (balances : L.Balances W)\n    (dissipative : L.Dissipative)\n'),
  ('  fun coming => rising_not_recurring balances dissipative distinct every fun N => match coming N with\n',
   '  fun coming => rising_not_recurring balances dissipative distinct every fun N =>\n    match coming N with\n'),
  ('   fun dissipative => dissipative.one_taking_not_recurring Pulse.pulsed.1 Pulse.pulsed.2.2.2.1.takers_recur,\n',
   '   fun dissipative => dissipative.one_taking_not_recurring Pulse.pulsed.1\n     Pulse.pulsed.2.2.2.1.takers_recur,\n')],
 'Locality.lean': [
  ('  | k + 1 => fun no => ceasing_steps_unrefuted ceasing N k fun ⟨E, U, distinct, length, from_, all⟩ =>\n',
   '  | k + 1 => fun no =>\n    ceasing_steps_unrefuted ceasing N k fun ⟨E, U, distinct, length, from_, all⟩ =>\n')],
 'Openness.lean': [
  ('    | ⟨all, _, every⟩ => comes_to_rest_unrefuted_from (T := 0) (fun _ _ => ⟨all, fun x _ => every x⟩)\n',
   '    | ⟨all, _, every⟩ =>\n      comes_to_rest_unrefuted_from (T := 0) (fun _ _ => ⟨all, fun x _ => every x⟩)\n'),
  ('      (standingCensus census embodied) fun t later => (enclosed t later).aroundStanding_not_not alive\n',
   '      (standingCensus census embodied) fun t later =>\n        (enclosed t later).aroundStanding_not_not alive\n'),
  ('theorem exchange_not_recurring {stand : Nat → List w.Relatum} (standing : w.web.StandingCensus stand)\n',
   'theorem exchange_not_recurring {stand : Nat → List w.Relatum}\n    (standing : w.web.StandingCensus stand)\n')],
 'Reserve.lean': [
  ('  active_not_recurring_from (T := T + 1) (fun t _ => carries t g) (unsupported_after_loss fixed below)\n',
   '  active_not_recurring_from (T := T + 1) (fun t _ => carries t g)\n    (unsupported_after_loss fixed below)\n'),
  ('/-- Carried and unsupported from step `T` on, a formation does not arise at arbitrarily late steps.\n-/\n',
   '/-- Carried and unsupported from step `T` on, a formation does not arise at arbitrarily late\nsteps. -/\n')],
 'Resolution.lean': [
  ('    Trickle.enclosed, Trickle.losesAtEverySize, Trickle.exchange_not_recurring, Trickle.arising_whole,\n',
   '    Trickle.enclosed, Trickle.losesAtEverySize, Trickle.exchange_not_recurring,\n    Trickle.arising_whole,\n'),
  ('  rests_unrefuted_of_after (rests_unrefuted_enclosed (after_counted counted T) (after_embodied embodied T)\n',
   '  rests_unrefuted_of_after (rests_unrefuted_enclosed (after_counted counted T)\n    (after_embodied embodied T)\n'),
  ('      (rests_unrefuted_without_refinement counted embodied balances dissipative enclosed unrefined)).1\n',
   '      (rests_unrefuted_without_refinement counted embodied balances dissipative enclosed\n        unrefined)).1\n')],
}
for name, pairs in EDITS.items():
    p = B / name; t = p.read_text()
    for old, new in pairs:
        assert t.count(old) == 1, (name, old)
        t = t.replace(old, new)
    p.write_text(t)
print('ok')
