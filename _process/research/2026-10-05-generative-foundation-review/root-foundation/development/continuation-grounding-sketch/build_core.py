"""Compile the committed Becoming core in a scratch directory, for the continuation-grounding sketch.

Uses the bytes of commit CORE_COMMIT only, so uncommitted edits in the working tree are not compiled.
Usage: python3 -I build_core.py <empty work dir>; then copy Continuation.lean to <work>/Sketch/ and
compile it with LEAN_PATH=<work> lean -o Sketch/Continuation.olean Sketch/Continuation.lean.
"""
import os, subprocess, sys, time
from pathlib import Path

REPO = Path("/Users/ren/theories")
CORE_COMMIT = "e448c56b180a62e51c35cd5cc1e42deb5b455377"
LEAN_REL = "experiments/integrated-correction/general-framework/generative-basis/lean"
ORDER = [l.split() for l in """GenerativeCore GenerativeCore.lean
InquirySufficiency inquiry-root/sufficiency/InquirySufficiency.lean
RelationalRenewal deeper/RelationalRenewal.lean
Becoming.Frame becoming/Becoming/Frame.lean
Becoming.Inquiry becoming/Becoming/Inquiry.lean
Becoming.Renewal becoming/Becoming/Renewal.lean
Becoming.Dependence becoming/Becoming/Dependence.lean
Becoming.Return becoming/Becoming/Return.lean
Becoming.Horizon becoming/Becoming/Horizon.lean
Becoming.Joint becoming/Becoming/Joint.lean
Becoming.Substitution becoming/Becoming/Substitution.lean
Becoming.Generation becoming/Becoming/Generation.lean
Becoming.Flow becoming/Becoming/Flow.lean
Becoming.Change becoming/Becoming/Change.lean
Becoming.Population becoming/Becoming/Population.lean
Becoming.Identity becoming/Becoming/Identity.lean
Becoming.Wholes becoming/Becoming/Wholes.lean
Becoming.Dissipation becoming/Becoming/Dissipation.lean
Becoming.Roles becoming/Becoming/Roles.lean
Becoming.Reserve becoming/Becoming/Reserve.lean
Becoming.Evolution becoming/Becoming/Evolution.lean
Becoming.Space becoming/Becoming/Space.lean
Becoming.Premises becoming/Becoming/Premises.lean
Becoming.Openness becoming/Becoming/Openness.lean
Becoming.Metaethics becoming/Becoming/Metaethics.lean
Becoming.Ranking becoming/Becoming/Ranking.lean
Becoming.Correspondence becoming/Becoming/Correspondence.lean
Becoming.Descent becoming/Becoming/Descent.lean""".splitlines()]
LEAN = Path.home() / ".elan/toolchains/leanprover--lean4---v4.29.1/bin/lean"
work = Path(sys.argv[1]).resolve()
work.mkdir(parents=True, exist_ok=True)
logs = work / "logs"; logs.mkdir(exist_ok=True)
env = {**os.environ, "LEAN_PATH": str(work)}
for name, rel in ORDER:
    data = subprocess.run(["git", "show", f"{CORE_COMMIT}:{LEAN_REL}/{rel}"], cwd=REPO, capture_output=True, check=True).stdout
    target = work / (name.replace(".", "/") + ".lean")
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_bytes(data)
for name, _ in ORDER:
    src = name.replace(".", "/") + ".lean"
    start = time.time()
    p = subprocess.run([str(LEAN), "-o", src[:-5] + ".olean", src], cwd=work, env=env, text=True,
                       stdout=subprocess.PIPE, stderr=subprocess.STDOUT, timeout=900)
    (logs / (name + ".log")).write_text(p.stdout)
    print(f"{name}: rc={p.returncode} {time.time()-start:.1f}s", flush=True)
    if p.returncode != 0:
        print(p.stdout[-3000:]); sys.exit(1)
print("CORE BUILT")
