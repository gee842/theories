# Repeated four-limb rail climb — isolated MuJoCo prototype

**A 137 kg free-base robot ascends one 3.6 m storey through 48 sequential physical grip advances and 12 body-raising strokes.** This prototype is isolated from the canonical workcell and public assets. It demonstrates an ideal-clamp climbing mechanism, not a fabricated robot or complete construction cycle.

## Reproduce

From `experiments/circular-construction/demo`:

```sh
numerical/.venv/bin/python production/physics/climb-prototype/prototype.py
numerical/.venv/bin/python production/physics/climb-prototype/prototype.py --scenario missed-grip
numerical/.venv/bin/python production/physics/climb-prototype/test_prototype.py
numerical/.venv/bin/python production/physics/climb-prototype/geometry_sweep.py
numerical/.venv/bin/python production/physics/climb-prototype/render_evidence.py
```

Requires MuJoCo 3.14.0 and NumPy in the existing numerical environment. Rendering uses MuJoCo's OpenGL renderer and a standard-library PNG writer. Six tests pass, covering a complete storey, stepwise positive support, bounded dynamics, motor energy, failed receiver recovery, trace poses and deterministic first-cycle reproduction. Metrics aggregate **every 2 ms integration step**, not just exported frames.

## Measured outcome

| Metric | Nominal | Missed receiver |
|---|---:|---:|
| Integrated time | 199.396 s | 9.504 s |
| Forward recaptures | 48 | 0 |
| Completed 0.3 m strokes | 12 | 0 |
| Chassis rise from initial unloaded pose | 3.599931971 m | −0.000068159 m |
| Rise from initial settled pose | 3.599999994 m | −0.000000136 m |
| Minimum positive upward supports | 3 | 3 |
| Minimum vertical reaction of any engaged support | 328.907 N | 333.838 N |
| Peak support reaction magnitude | 994.545 N | 961.787 N |
| Peak motor torque | 450.000 Nm | 403.281 Nm |
| Maximum joint limit violation | 0 | 0 |
| Maximum supported tip drift | 0.065694 mm | 0.063413 mm |
| Maximum successful capture error | 0.042188 mm | 0.022733 mm, recovery |
| Maximum successful capture speed | 0.005680 m/s | 0.005088 m/s |
| Simulator warnings | 0 | 0 |

The nominal chassis ends at MuJoCo Z-up `[0.000000728, 0, 4.799931971]` m. Gravity is 9.81 m/s². Motor mechanical work is **4933.817 J**; potential energy increases **4838.218 J**. Integrated ideal-constraint work is **−1.742 J**, so the clamps do not provide the lifting energy. These are numerical power integrals, not actuator electrical-energy or efficiency estimates.

`nominal-metrics.json` and `missed-grip-metrics.json` contain exact events, stepwise extrema, final reactions and solver diagnostics. `nominal-trace.json` and `missed-grip-trace.json` contain measured states sampled at 10 Hz. `climb-start.png`, `climb-mid.png` and `climb-end.png` are MuJoCo-rendered recorded poses at 0.002, 99.702 and 199.302 s. The renderer restores recorded state solely to draw these stills; it performs no simulation steps.

## Mechanism and transition gates

The baseline supplies the 137 kg total mass, four 8/6/3 kg articulated limbs, a free chassis and ±450 Nm motors. This isolated redesign merges the baseline 4 kg tool into the chassis (69 kg), uses 0.45 m links, changes the rest angles and joint ranges, and omits the beam, hoist and tool motion.

Each cycle holds the chassis while front-left, front-right, rear-left and rear-right advance in order by 0.30 m. A released grip retracts 70 mm away from the rail during its 2.5 s smooth swing. Each receiver is an immutable world site. A `connect` equality implements a force-transmitting point clamp with free rotation; it does not transmit a weld moment.

Before release, all three continuing supports must have measured upward reaction above 5 N. The new clamp can activate only when actual tip distance is below 4 mm and actual tip speed below 0.025 m/s, after at least 2.5 s. The new support must then develop a reaction above 5 N and remain engaged during a 0.6 s loading interval before another limb can release. Once all four have advanced, bounded joint motors raise the chassis 0.30 m over a 3 s smooth stroke with 1 s of settling. The sequence repeats twelve times.

All movement during integration results from **joint motor torques and gravity**. No robot/grip qpos, qvel, body positions, mocap positions, receiver positions or equality target coordinates are assigned. Only actuator inputs and equality activation change. Inverse kinematics gives joint targets; a least-squares static grasp solution balances the six unactuated chassis DOFs and supplies motor gravity feedforward. PD gains are 12000 Nm/rad and 220 Nms/rad, clipped to ±450 Nm. The static grasp solution never applies an external force to the chassis. Fixed anchor arrays are checked for exact immutability.

In the negative case the first front-left receiver is displaced 80 mm laterally, outside the planar limb's reachable plane. The actual capture error remains 80.012 mm. After the 4.5 s timeout the controller rejects that receiver, never activates its equality, never releases another support, and drives the foot back to its original receiver. That return is subject to the same distance and speed gates. All four original supports are restored; the climb remains aborted.

## Geometry and smallest tested design

`geometry-contract.json` is the authoritative asset-building contract. SI, MuJoCo Z-up:

- Chassis starts at `(0, 0, 1.2)`; hips are `(0, ±0.25, ±0.32)` m.
- Rails lie at `x=0.55`, `y=±0.25` m; lateral spacing is 0.50 m.
- Upper/lower links extend along their own local +X by 0.45 m. Initial shoulder angle is `−acos(0.55/0.90)`; initial elbow angle is twice its magnitude. Joint axes are local +Y.
- Shoulder limits are `[−1.7, 0.3]` rad and elbow limits `[0.4, 2.5]` rad. There is no joint-position servo that bypasses the torque cap.
- Receiver heights are `1.2 + hipZ + 0.30*k`, `k=0..12`. Front/rear receiver families on each rail are offset by 0.64 m: they are two interleaved families, **not one uniform 0.30 m rung lattice**. A continuous gripping rail is assumed. Tooth pitch and latch hardware are not modeled.
- Clamp solver parameters are `solref=".008 1"`, `solimp=".99 .99 .001"`; tiny measured compliance prevents severe redundant planar-constraint force amplification.

The original 0.32 m workcell links, initial rail offset of about 0.6206 m and initial tip rise of 0.1097 m cannot execute this gait's first 0.30 m fixed-body grip advance: the required hip-tip distance is about 0.7437 m, exceeding their 0.64 m total reach. This does not prove that every possible smaller-stroke gait is impossible with the original robot.

For the redesigned 0.55 m rail offset and tip-height interval 0..0.30 m, the purely geometric equal-link lower bound is `sqrt(0.55²+0.30²)/2 = 0.31325 m`; with the 0.4 rad minimum elbow bend it is approximately 0.31962 m. These are reach bounds, not dynamic guarantees. The declared 0.32/0.34/0.36/0.40/0.45 m sweep finds **0.36 m to be the smallest tested successful link length**. It is not a globally optimized minimum. At 0.32 m, first-capture error/speed are 10.794 mm / 0.237 m/s; at 0.34 m they are 4.131 mm / 0.265 m/s. Both fail the actual capture gate under this controller and deadline. The 0.32 m recovery also fails, leaving three supports retained. The 0.36 m design additionally completes a separately validated full storey, with 48 captures, 440.576 Nm peak torque and 971.807 N peak support reaction (`minimum-tested-metrics.json`). The exported viewer demonstration remains the declared 0.45 m design.

## Integrating a separate climb mode into the 20-storey scene

The trace conforms to `src/experience/types.ts`: schemaVersion 1, glTF Y-up, 13 explicit `robot` body/node bindings, phases, actuator values, support forces, empty collision contacts and discrete support state. Additional diagnostic fields retain Z-up qpos, grip positions, rung indices and exact events. Conversion is `p=(x,z,−y)`, `Rg=C Rm Cᵀ`, quaternion order xyzw. All trace body poses are world poses; avoid double-applying their parent transforms in an asset.

Build a separate matching long-link robot asset from the geometry contract; the canonical 0.32 m robot does not match. Place this local simulation beside a tower rail by applying one rigid transform to every recorded body pose and every receiver/rail. Translate/rotate the robot and rails together; do not stretch the recorded trajectory or individually offset limbs. Keep this as a distinct one-storey climb mode and preserve the canonical beam-placement trace. Reaching another floor requires more fixed receivers and a rerun; concatenating this clip cannot establish 20-storey endurance, payload carriage or obstruction clearance.

## Remaining fidelity gaps

Clamps are ideal point constraints: no pad contact, tooth engagement, capture orientation, latch closure, pullout, finite holding strength or mechanical interlock is simulated. The 995 N peak is a demanded reaction, not a tested clamp rating. Links, grips and rails have collision disabled; their inertial dynamics are active, but self-collision, snagging, member crossing, floor-edge obstruction and finite-body clearance are unvalidated. The stills show this abstract mechanism, not a fabrication-ready layout. Rails are rigid world supports, not elastically coupled to the tower. No beam payload, tool load, lateral gait, sensor error, motor thermal limit or fault detection beyond the declared receiver gate is included.

[MuJoCo equality-constraint reference](https://mujoco.readthedocs.io/en/stable/XMLreference.html#equality-connect) documents the point-clamp/site semantics used here.
