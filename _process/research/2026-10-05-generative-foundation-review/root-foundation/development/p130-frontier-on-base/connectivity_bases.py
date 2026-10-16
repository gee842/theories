"""THEOREM-CONNECTIVITY.py under a chosen base set, writing only into OUTDIR (P130, 16 October 2026).

usage (from the repository root):
  python3 -B _process/research/2026-10-05-generative-foundation-review/root-foundation/development/p130-frontier-on-base/connectivity_bases.py \
      _process/research/2026-10-05-generative-foundation-review/root-foundation/THEOREM-CONNECTIVITY.py OUTDIR original|extended [without-new]

It imports the measure, changes only its PROCESS/WORLD lists (`extended` adds Becoming.Law.orbit to
the Process family and Becoming.ExchangeLaw and Becoming.carried to the World family, the readings
Becoming.Runs proves), and writes the JSON into OUTDIR instead of the study. With `without-new`, the
constants of the six P130 modules are removed from the dump and from the spine list before the
analysis: no existing module imports a new one, so this is the state before P130 measured on the
same compiled environment. Like the measure, it needs the checker cache to hold the current sources.
"""
import importlib.util
import sys
from pathlib import Path

NEW = ['Becoming.Runs', 'Becoming.CourseWorlds', 'Becoming.LearnableRuns', 'Becoming.ParityReadings',
       'Becoming.FinerTraces', 'Becoming.FormedLoops']

script = Path(sys.argv[1]).resolve()
out = Path(sys.argv[2]).resolve()
out.mkdir(parents=True, exist_ok=True)
spec = importlib.util.spec_from_file_location('tc', script)
tc = importlib.util.module_from_spec(spec)
spec.loader.exec_module(tc)
if sys.argv[3] == 'extended':
    tc.PROCESS = tc.PROCESS + ['Becoming.Law.orbit']
    tc.WORLD = tc.WORLD + ['Becoming.ExchangeLaw', 'Becoming.carried']
if len(sys.argv) > 4 and sys.argv[4] == 'without-new':
    dump = tc.dump_constants

    def filtered():
        constants, registry, modules, version, clean = dump()
        kept = {n: x for n, x in constants.items() if x['m'] not in NEW}
        for x in kept.values():
            assert not any(constants[d]['m'] in NEW for d in x['t'] + x['v'] if d in constants), x['n']
        return kept, {m: r for m, r in registry.items() if m not in NEW}, modules - len(NEW), version, clean

    tc.dump_constants = filtered
    tc.cb.SPINE = [m for m in tc.cb.SPINE if m not in NEW]
tc.HERE = out
sys.argv = [str(script), '--write']
tc.main()
