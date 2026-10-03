# Construction modeling and dynamics toolchain

An isolated, executable toolchain set up on 30 September 2026. The existing
`../demo` is read only during verification. This lab has its own Python virtual
environment, JavaScript dependency lock, scripts, and generated outputs.

## Run

On the verified Apple Silicon macOS host, with Blender, Node, npm and uv available:

```sh
cd /Users/ren/theories/experiments/circular-construction/toolchain-lab
bash setup.sh
```

The setup installs only into this lab. Python packages are version-locked with
distribution hashes; JavaScript dependencies use `package-lock.json`. Rerun the
checks without installing anything:

```sh
.venv/bin/python verify_toolchain.py
```

## Verified tools

| Tool | Version | Executed verification |
|---|---|---|
| Blender | 5.2.1 LTS | Open the existing editable climber asset and export a separate GLB |
| Three.js | 0.180.0 | Parse that exported GLB using the real GLTFLoader and check geometry |
| MuJoCo | 3.14.0 | Bounded actuator dynamics, overload failure, gravity and physical contacts |
| Mink | 1.1.0 | Differential inverse kinematics with joint-position and reference-velocity limits |
| DAQP / OSQP | 0.10.2 / 1.1.3 | Both optimization backends execute the IK trajectory |
| OpenSeesPy | 3.8.0.0 | 3D elastic cantilever agrees with analytical deflection and reactions |
| Python | 3.11.2 | Isolated interpreter and locked dependencies |

The verification also runs the existing four workcell tests, eight structural
tests, and production asset integrity check without regenerating their outputs.

## What the new dynamics check establishes

`verify_dynamics.py` models a fixed-base, three-joint arm with explicit body mass,
gravity, joint limits, and 120/120/80 Nm motor limits. Mink updates a separate
reference configuration at 100 Hz. A bounded torque controller drives the actual
MuJoCo state at 1 kHz. After initialization, simulated positions are advanced only
by integration. No reference pose is copied into the simulated robot.

The 3 kg attached tool fixture reaches a changing Cartesian target within the
3 mm acceptance tolerance and stays below the motor limits. A 40 kg overload
saturates the motors and misses the target by over 0.8 m; the physical failure is
retained in the output. The overload is an adverse numerical experiment, not a
demonstrated safe recovery procedure. The attached tool mass is an ideal rigid
fixture, not a validated gripper.

Checks also cover exact repeatability, final-position agreement after halving the
timestep, nominal joint limits and speed, and the alternative IK solver. A
separate free-body drop/contact fixture settles under 25 kg of gravity with a
245.25 N total support reaction. Its measured peak penetration is approximately
1.13 mm at the tested 1 ms timestep and contact parameters.

These are toolchain integration checks with idealized geometry and parameters.
They do not validate a climbing robot, assembly connection, material strength,
perception system, autonomous construction process, or physical hardware.

## Outputs

- `output/toolchain-report.json`: aggregate results and installed versions.
- `output/dynamics-report.json`: physical measurements and pass/fail gates.
- `output/nominal-trace.json`, `output/overload-trace.json`: integrated poses,
  commands and actual actuator forces.
- `output/nominal.xml`, `output/overload.xml`: editable physics fixtures.
- `output/climber-roundtrip.glb`: newly exported existing Blender robot asset.
- `output/blender-report.json`, `output/three-report.json`: asset checks.
- `output/*.log`: captured verification logs.

Generated outputs and environments are ignored locally. Reproduction scripts and
dependency locks are the source artifacts. The Blender input's hash is recorded,
and the export check verifies that the source file remains unchanged.

## Next integration requirements

The existing production workcell still uses ideal clamp equality constraints,
prescribed crane motion, and a fastening tool with collision disabled. Its report
correctly ends at a seated, unfastened beam. Passing this toolchain's checks does
not remove those limitations.

The next mechanism work needs shared Blender/MJCF geometry, reachable tool poses,
physical mating contacts, finite clamp capacities, force-aware insertion,
load-transfer verification, and autonomous retreat or recovery. Use Mink for
reference generation; assess success from the integrated dynamic state. Evaluate
collision-avoidance planning separately from actual collision response.

Implementation policy: GPT-6.1 Sol at low/medium effort for bounded implementation,
high for difficult implementation bugs; retain architecture, mechanism/control
design, structural coupling and consequential reviews with the lead model. This
records the requested policy, not an assertion that another thread's model was
changed or a worker launched.

References: [Mink installation](https://kevinzakka.github.io/mink/installation.html),
[MuJoCo model reference](https://mujoco.readthedocs.io/en/stable/XMLreference.html),
[OpenSeesPy beam-column element](https://openseespydoc.readthedocs.io/en/latest/src/elasticBeamColumn.html),
[Three.js GLTFLoader](https://threejs.org/docs/pages/GLTFLoader.html).
