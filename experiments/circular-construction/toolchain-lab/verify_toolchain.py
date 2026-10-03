"""One-command toolchain verification; outputs remain inside this lab."""
from __future__ import annotations

import importlib.metadata
import json
import os
from pathlib import Path
import platform
import shutil
import subprocess
import sys

HERE = Path(__file__).resolve().parent
DEMO = HERE.parent/"demo"
OUTPUT = HERE/"output"


def run(name: str, command: list[str], cwd: Path = HERE) -> dict:
    print(f"Checking {name}...", flush=True)
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1")
    result = subprocess.run(command, cwd=cwd, env=env, text=True,
                            stdout=subprocess.PIPE, stderr=subprocess.STDOUT, timeout=180)
    (OUTPUT/f"{name}.log").write_text(result.stdout)
    return {"status": "passed" if result.returncode == 0 else "failed",
            "returnCode": result.returncode, "log": f"{name}.log"}


def structure_check() -> dict:
    import openseespy.opensees as ops
    ops.wipe()
    ops.model("basic", "-ndm", 3, "-ndf", 6)
    length, young, inertia, force = 3., 2e11, 8e-5, 1000.
    ops.node(1, 0., 0., 0.)
    ops.node(2, length, 0., 0.)
    ops.fix(1, 1, 1, 1, 1, 1, 1)
    ops.geomTransf("Linear", 1, 0., 0., 1.)
    ops.element("elasticBeamColumn", 1, 1, 2, .008, young, young/2.6,
                1.2e-6, inertia, 4e-5, 1)
    ops.timeSeries("Linear", 1)
    ops.pattern("Plain", 1, 1)
    ops.load(2, 0., 0., -force, 0., 0., 0.)
    ops.constraints("Plain")
    ops.numberer("RCM")
    ops.system("BandGeneral")
    ops.algorithm("Linear")
    ops.integrator("LoadControl", 1.)
    ops.analysis("Static")
    code = ops.analyze(1)
    measured = abs(ops.nodeDisp(2, 3))
    expected = force*length**3/(3*young*inertia)
    ops.reactions()
    reaction = ops.nodeReaction(1, 3)
    passed = code == 0 and abs(measured-expected)/expected < 1e-8 and abs(reaction-force) < 1e-6
    report = {"status": "passed" if passed else "failed", "engineVersion": ops.version(),
              "computedDeflectionM": measured, "analyticalDeflectionM": expected,
              "supportReactionN": reaction, "appliedForceN": force}
    ops.wipe()
    return report


def main() -> int:
    OUTPUT.mkdir(exist_ok=True)
    versions = {name: importlib.metadata.version(name) for name in
                ("mujoco", "mink", "numpy", "scipy", "openseespy", "qpsolvers", "osqp", "daqp")}
    blender, node = shutil.which("blender"), shutil.which("node")
    if not blender or not node:
        raise RuntimeError("Blender and Node must be installed and on PATH")
    checks = {"structuralAnalyticalReference": structure_check()}
    checks["robotics"] = run("dynamics", [sys.executable, "verify_dynamics.py"])
    checks["blender"] = run("blender", [blender, "--background", "--factory-startup",
        "--disable-autoexec", "--python", str(HERE/"verify_blender.py"), "--",
        "--source", str(DEMO/"production/blender/climber-robot.blend"), "--output", str(OUTPUT)])
    checks["three"] = run("three", [node, "verify_three.mjs"])
    # These existing tests compute in memory. Bytecode output is disabled above.
    checks["existingWorkcellRegression"] = run("existing-workcell",
        [sys.executable, "test_workcell.py"], DEMO/"production/physics/mujoco")
    checks["existingTowerRegression"] = run("existing-tower",
        [sys.executable, "-m", "unittest", "discover", "-p", "test_*.py", "-v"],
        DEMO/"production/structure/opensees")
    checks["existingAssetIntegrity"] = run("existing-assets",
        [node, "scripts/verifyProduction.mjs"], DEMO)
    report = {"status": "passed" if all(x["status"] == "passed" for x in checks.values()) else "failed",
        "python": platform.python_version(), "platform": platform.platform(), "packages": versions,
        "executables": {"python": sys.executable, "blender": blender, "node": node}, "checks": checks,
        "limitations": ["Toolchain and bounded numerical verification, not validation against hardware.",
                        "Existing clamp, collision and fastening limitations remain unchanged."]}
    (OUTPUT/"toolchain-report.json").write_text(json.dumps(report, indent=2)+"\n")
    print(json.dumps(report, indent=2))
    return 0 if report["status"] == "passed" else 1


if __name__ == "__main__":
    raise SystemExit(main())
