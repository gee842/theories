# MuJoCo active-floor workcell

This is a physically simulated **partial placement cycle**, replayed in the browser from actual MuJoCo states. It ends with a 5.6 m I-section beam supported on two seats and a tool approaching the connection. It does **not** end with a fastened connection.

From `experiments/circular-construction/demo`:

```sh
numerical/.venv/bin/python production/physics/mujoco/simulate.py
numerical/.venv/bin/python production/physics/mujoco/simulate.py --scenario missed-seat --output production/physics/mujoco/missed-seat-trace.json
numerical/.venv/bin/python production/physics/mujoco/test_workcell.py
```

Requires Python 3.11, MuJoCo 3.14.0 and NumPy. `workcell.xml` is the editable MJCF source read by the simulator. `build_model.py` regenerates that source; running it replaces manual MJCF edits. The standard output is `public/assets/workcell-trace.json`, plus `nominal-validation.json` beside the source. Negative-case output and `missed-seat-validation.json` are separate.

## Physical model and control

- Gravity is 9.81 m/s²; timestep 2 ms; `implicitfast` integration; Newton constraint solver, up to 80 iterations. Positions are never overwritten during simulation. Only the external crane carrier has a prescribed motion.
- The 137 kg concept climbing robot has a free chassis, four two-joint limbs with mass/inertia, bounded joints, 450 Nm bounded torque motors, and a 500 N bounded prismatic tool motor. The PD joint controller includes joint gravity/bias feedforward.
- Eight limb torques raise the chassis about 0.211 m against four rail grips. Front-left support releases at 5.502 s, articulates under torque, then reacquires its original rail capture point at 9.502 s. The other three supports remain engaged. This demonstrates one body-raising stroke and a grip cycle, not a complete storey-to-storey gait.
- Each rail clamp is an ideal MuJoCo weld to a local fixed rail anchor, gated on an 18 mm translational capture envelope. Geometry, pad compression, clamp closure, load limits and a full mechanical latch are not resolved. The viewer receives actual constraint force magnitudes and active-lock counts.
- The free 638.563 kg beam uses three collision boxes representing a 300 × 450 mm I-section (18 mm flanges, 9 mm web, density 7850 kg/m³). Length is 5.6 m between the 6 m column grid, allowing column clearance; the geometry matches the modeled beam asset.
- A prescribed crane carrier descends from z=46.45 m to 45.05 m. Two **unilateral** sling forces are calculated from real beam attachment positions and velocities: `max(0, k*extension + c*extensionRate)` while taut, with k=30 kN/m, c=1.2 kNs/m and free length 1.4 m. They are applied to the beam through `mj_applyFT`; no compressive rope force is allowed. Native spatial tendons retain attachment geometry but have zero native stiffness/damping to avoid double counting. The carrier is an imposed input, not an autonomous crane controller.
- Physical seat collision reactions at both ends must each exceed 35% of beam weight and beam translational speed must remain below 0.03 m/s for 0.4 s before sling forces are disabled. The nominal run releases support at 15.828 s, with final seat reactions about 3132 N each and beam center z=43.4249965 m.
- The tool actuator then extends toward the connection. Its collision is disabled; it ends short of the member and applies no bolt torque or pin contact. A full connection requires a revised tool reach, actual mating pin/bolt collision geometry and clearance, contact-driven insertion, a verified latch or preload model, and an appropriate load-transfer gate. Merely adding a beam weld would not establish that behavior.

## Negative case and verification

`missed-seat` shifts the beam and crane by 0.8 m laterally. Neither seat takes load, so the release gate remains false and the crane retains support and the tool approach remains inhibited. The result is an explicit abort, not a successful construction event.

Integration tests check physical weight transfer, support retention in the negative case, actual body raise, actuator limits, no simulator warnings, maximum penetration under 2 mm, normalized output quaternions and exact deterministic repeatability. Logs report solver iterations, finite state, contact penetration, forces and events. These are simulation regression tests, not experimental validation or engineering certification.

## Trace and modeling boundaries

The trace implements `src/experience/types.ts`. Frames contain MuJoCo world poses, individual seat contact normals, motor forces/positions, grip reaction magnitudes, contact and solver metrics, plus support/connection state. Viewer coordinates are glTF Y-up: `(x,z,-y)`, `R_g = C R_m C^T`, and quaternion order xyzw. Physics origin is the actual Blender site origin, with active seat elevation 43.2 m. Every node binds by explicit asset/node name; no frame-to-frame scripted limb placement is used.

`robot` nodes are `robot_chassis`, `limb_{fl,fr,rl,rr}_{upper,lower,grip}`, and `robot_tool`. `site` nodes are `lifted_beam` and `ActiveHoist`. Both limb links extend along local +X by 0.32 m; rest upper rotation is −0.35 rad about Blender Y and lower relative rotation +0.35 rad. Blade/tool/robot decorative geometry does not substitute for collision geometry.

Tower flexibility is not coupled back into this rigid workcell. Mass properties, friction, grip strength assumptions and controller gains describe an unvalidated concept machine. There is no sensor noise, perception, autonomous route planning, fault-tolerant controller, thread mechanics, bolt preload, plastic deformation or certified connection design.

API references: [MuJoCo MJCF reference](https://mujoco.readthedocs.io/en/stable/XMLreference.html), [MuJoCo API functions](https://mujoco.readthedocs.io/en/stable/APIreference/APIfunctions.html).
