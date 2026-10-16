#!/usr/bin/env python3
"""Rewrap the docstring lines P58b lengthened. Usage: python3 -B wrap_p58b.py WT"""
import sys
from pathlib import Path
B = Path(sys.argv[1]) / 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming'
FIX = {
 'Decidedness.lean': [(
'''  then on a later fall stays unrefuted (`falls_stop_unrefuted`, `stop_unrefuted_iff`), and that refutes the arising which ceasing recurring under a covering list
''',
'''  then on a later fall stays unrefuted (`falls_stop_unrefuted`, `stop_unrefuted_iff`), and that
  refutes the arising which ceasing recurring under a covering list
''')],
 'Openness.lean': [
('''  unrefuted (`World.arising_stops_unrefuted_from`, from `Flow.change_stops_unrefuted`). With a census of what is active
  as well,''',
'''  unrefuted (`World.arising_stops_unrefuted_from`, from `Flow.change_stops_unrefuted`). With a
  census of what is active as well,'''),
('''  decision procedure where that coming to be stops cannot be refuted (`Listed.few_of_stop_unrefuted`). So in every world
''',
'''  decision procedure where that coming to be stops cannot be refuted
  (`Listed.few_of_stop_unrefuted`). So in every world
'''),
('''every step from `T` on a later arising stays unrefuted (`stop_unrefuted_iff`). No premise on the flow and no decision procedure (`Flow.change_stops_unrefuted`). -/''',
'''every step from `T` on a later arising stays unrefuted (`stop_unrefuted_iff`). No premise on the
flow and no decision procedure (`Flow.change_stops_unrefuted`). -/'''),
('''that arising stops cannot be refuted (`arising_stops_unrefuted_from`), and ceasing recurring would leave a later arising
unrefuted after every step''',
'''that arising stops cannot be refuted (`arising_stops_unrefuted_from`), and ceasing recurring
would leave a later arising unrefuted after every step'''),
('''refuted (`Flow.change_stops_unrefuted`), nor with it that coming to be stops (`Listed.few_of_stop_unrefuted`). So the worlds it
covers''',
'''refuted (`Flow.change_stops_unrefuted`), nor with it that coming to be stops
(`Listed.few_of_stop_unrefuted`). So the worlds it covers'''),
('''theorem arising_stops_unrefuted_from {stand : Nat → List w.Relatum} (standing : w.web.StandingCensus stand)
    (embodied''',
'''theorem arising_stops_unrefuted_from {stand : Nat → List w.Relatum}
    (standing : w.web.StandingCensus stand) (embodied'''),
('''theorem Listed.few_of_stop_unrefuted {p : α → Nat → Prop} {l : Nat → List α} (listed : Listed p l)
''',
'''theorem Listed.few_of_stop_unrefuted {p : α → Nat → Prop} {l : Nat → List α}
    (listed : Listed p l)
'''),
 ],
 'Space.lean': [
('''theorem Web.generation_stops_unrefuted {X : Type} {W : Web X X} {L : Flow X X} {ds : List X} {T : Nat}
''',
'''theorem Web.generation_stops_unrefuted {X : Type} {W : Web X X} {L : Flow X X} {ds : List X}
    {T : Nat}
'''),
 ],
}
for f, pairs in FIX.items():
    p = B / f; t = p.read_text()
    for old, new in pairs:
        assert t.count(old) == 1, (f, old[:60]); t = t.replace(old, new)
    p.write_text(t)
print('ok')
