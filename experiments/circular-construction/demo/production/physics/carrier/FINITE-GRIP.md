# Actual-jaw local contact experiment

`finite_grip.py` is separate from the unchanged `simulate.py` ideal-point runner. It uses the same 320 kg carrier, 92.928 kg beam and 0.65 m links. There are **zero equality restraints**, mocap bodies, live qpos rewrites or applied body forces. Motor forces and collision/contact forces advance the state. The payload is already rigidly locked to its cradle; pickup and cradle retention contacts are not solved.

The physical jaw throat is 0.135 m ahead of the wrist pivot, so the wrist lies 0.615 m from the initial chassis while the rail capture line is 0.75 m away. A third actuated wrist maintains jaw orientation at the existing Blender pivot; its proposed bound is 400 Nm. Each opposed sliding jaw is force limited to 8 kN, with nominal 4 kN closing force supplied by a bounded position servo. The grip's total nominal normal load is approximately 8 kN, rather than an unexplained point reaction. Open centers are ±0.15 m and closed centers are ±0.045 m.

The column is at source X=0.93 m and faces toward the carrier; its near rails are at X=0.75 m, Y=±0.32 m. Actual 0.10 m-wide receiver plates obstruct a rail-width jaw centered directly on a receiver. The finite fixture therefore starts the chassis at Z=1.44 m, putting jaw centers midway between plates at Z=0.96 and 1.92 m. This differs intentionally from the old ideal fixture. Column, rail, bracket, receiver and robot-to-environment collision primitives are active. Robot self-collision is still omitted, and rigid frame compliance is not solved.

The nominal contact model assumes pad/steel friction 0.65. Elliptic friction with impedance ratio 20 and a stiff normal response limits regularization creep. This follows [MuJoCo's contact modeling guidance](https://mujoco.readthedocs.io/en/stable/modeling.html); it does not constitute measured pad friction or hardware compliance. No NoSlip post-solver is used. The source and XML record every solver/control parameter.

Run from the demo directory:

```sh
numerical/.venv/bin/python production/physics/carrier/finite_grip.py --mode hold
numerical/.venv/bin/python production/physics/carrier/finite_grip.py --mode recapture --shift-x .12
numerical/.venv/bin/python production/physics/carrier/finite_grip.py --mode step --shift-x .12
numerical/.venv/bin/python production/physics/carrier/finite_grip.py --mode hold --mu .2
```

The accepted result is the **five-second nominal four-grip contact hold**, with all four upward supports, approximately 0.045 mm maximum body drift, approximately 0.002 mm maximum contact penetration, no non-grip environment collision, and bounded actuator effort (about 645 Nm shoulder, 1413 Nm elbow, 134 Nm wrist). The exact current metrics and model hash are stored beside the XML and trace.

A 0.12 m motor-driven shift toward the rails lowers the gravity moment before releasing a front grip. Release/return/recapture can finish its state sequence, but roughly 5.35 mm transient penetration, jaw-limit violation and saturated elbow/wrist control reject its contact-quality gate. **It is not an accepted capture result.** A 0.32 m climb attempt loses the three-retained-upward-support gate and stops; no physical loaded step is claimed. At friction 0.2 the initial hold also fails, showing that the measured hold depends materially on the assumed surface friction.

`sequenceComplete` means the requested phase sequence ended. `complete` additionally requires the contact-quality gate; rejected attempts must not be published as nominal physical motion. Their traces remain useful diagnostics. The next work is a force-aware unloading/distribution controller, collision-safe jaw capture and revised support geometry/actuation if the measured torque bounds continue to govern. Raising actuator bounds to force a passing result is not assumed.
