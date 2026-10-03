# Isolated positive connector feasibility prototype

**Result:** a contact-based headed pin with two spring-deployed radial dogs can retain a seated 5.6 m beam under a 2 kN axial proof load in this isolated MuJoCo fixture. Actual dog/beam and head/bracket contacts carry the load with every actuator off. The current robot cannot perform this operation without reach/alignment and tool changes. This is not an integrated robot fastening cycle, threaded bolt, preload model, or certified connection design. Canonical physics, Blender assets, and the public viewer trace are untouched.

## Run and inspect

From `experiments/circular-construction/demo`:

```sh
numerical/.venv/bin/python production/physics/connector-prototype/prototype.py
numerical/.venv/bin/python production/physics/connector-prototype/prototype.py --scenario misaligned
numerical/.venv/bin/python production/physics/connector-prototype/test_prototype.py
numerical/.venv/bin/python production/physics/connector-prototype/prototype.py --render
```

MuJoCo 3.14.0 and NumPy are already installed in that environment. The test writes four editable MJCF models, four actual dynamic traces, validation reports, and `test-results.json` into this directory. Tests need no rendering dependency; optional `--render` uses MuJoCo's OpenGL renderer and writes `nominal-final.png` directly from the integrated final state. All frames use local **Z-up metres**, not the production glTF convention. Translate by `(6.2, -12, 43.2)` to place this fixture in the active workcell.

## Geometry and mechanism

The 450 × 300 mm I-section, 9 mm web, 18 mm flanges, 5.6 m length, and two seat-top heights match the canonical physics. Beam mass is 638.563 kg plus a 2.180 kg representative annular end lug, totaling 640.743 kg. The beam has all six free-body degrees of freedom. No equality constraints exist. Both seats are frictionless so axial retention cannot be attributed to friction.

The lug is centered at local `(0.015, 0.085, 0.3375)`, matching the location and 24 mm hole radius of the upper positive-Y hole on the Blender left endplate. A proposed fixed support lug is centered at `(-0.03, 0.085, 0.3375)` with 20 mm thickness; the beam lug is 30 mm thick. Each annulus uses sixteen **separate convex sectors**, leaving a genuine open polygonal bore. A single concave mesh would be convex-hulled and would not provide this passage. The polygonal bore has 23.539 mm minimum radius; a 12 mm-radius pin has 11.539 mm nominal radial clearance. This generous clearance is an explicit concept assumption, not a fitted structural fastener specification.

The headed pin has 114 mm insertion travel. A cutout near its nose accommodates opposed 12 × 14 × 10 mm sliding dogs. Each dog has 30 mm available outward travel, a 1 kN/m spring, and a bounded retracting actuator. They stay retracted until their actual rear faces clear the actual beam-lug rear face by 2 mm. They then deploy under spring force; their ideal internal slide joints and travel stops stand in for machined guides. The insertion motor is limited to 500 N and switched off at 2 s. The paired dog retractors also remain off during retention.

A 2 kN axial load ramps on from 2.5–3 s and remains through 5 s. Its line of action passes through the bore center; this isolates axial retention rather than claiming multi-axis restraint. The load path is beam lug → dog faces → pin assembly → pin head → fixed support lug. Approximately 14 mm axial clearance is taken up before retention. The dog springs only deploy the dogs; they do not supply the 2 kN axial retaining force. Contact reactions and the internal dog guide reactions supply that force.

## Measured checks

| Case | Measured behavior |
|---|---|
| Nominal insertion + axial proof load | Dogs release at 1.286 s. Final axial beam displacement 14.03 mm; final-quarter-second dog/beam and head/bracket axial contact reactions each approximately 2000.50 N. Insertion and dog motor forces are zero. |
| Beam hole offset by 25 mm | Real interference peaks at approximately 48.53 N. More than 25 N sustained for 30 ms triggers retraction at 0.843 s. Dogs remain retracted; proof load is inhibited. The frictionless beam is disturbed by approximately 10.23 mm axially; this is a failed insertion, not a harmless alignment correction. |
| Dogs held retracted | Same insertion and proof-load command; beam escapes axially. No dog/beam retaining reaction. Continued intentionally unrestrained load eventually pushes it off the seats, so later motion is outside the useful connection test. |
| Pin extraction challenge | After engagement, a −250 N pin motor force replaces the external proof load. Dog/beam contact carries approximately 250 N; the beam lug reaches the fixed bracket and closes that reaction path. Pin remains inserted about 80 mm. |

All four cases have finite states, no MuJoCo warnings, bounded actuator forces, and maximum contact penetration below 0.23 mm. Regression tests require an exact deterministic nominal repeat, compare the 0.5 ms baseline to 0.25 ms integration, inspect both physical retaining interfaces, ensure motors are off during nominal retention, and require the misalignment and no-latch controls to fail appropriately. The timestep comparison is in `test-results.json`. These checks establish behavior in this rigid model; they do not establish material strength or machine reliability.

Traces include joint positions, actual body positions, applied load, actuator forces, named contact pairs, contact normal magnitudes, signed world-space force on contact geom B, and penetration. Validation summaries aggregate final-quarter-second **axial** retaining forces rather than incorrectly treating every normal as axial.

## Current robot feasibility

The canonical final trace puts the robot chassis at Z-up `(5.397012, -12, 44.110894)` and tool origin at `(5.887012, -12, 43.560894)`. The 120 mm tool tip is therefore at x=6.007012. Raising tool extension from its commanded 240 mm to the current 350 mm maximum reaches only x=6.117012; the beam front face is x=6.2. The tool also has no lateral or vertical alignment axes. The nearest visible hole is at y=−11.915 and z=43.5375: **85 mm lateral and −23.394 mm vertical correction** are needed. The canonical tool's collision is disabled.

For this cartridge, the final accessible rear pin-head face is at x≈6.148. A tip-extension setting of approximately **381 mm** would be required at the measured chassis pose, exceeding the existing 350 mm travel. A proposed 450–500 mm stroke and fixed 85 mm lateral / −23.4 mm vertical offset could access this one hole; a real reusable tool needs bounded lateral/vertical alignment axes, approach clearance, and collision checks. The current chassis raising trajectory does not itself establish this access. The support lug and cartridge are new components absent from both canonical MJCF and Blender geometry.

## Exact integration work still required

1. Use shared dimensions to replace the relevant Blender visual hole and MJCF lug with the same full endplate, bolt/pin cartridge, and support bracket. Resolve support-to-column attachment and the other three holes. Preserve the real bore using convex decomposition; do not model a bore as one concave collision mesh. Update beam mass/inertia consistently with complete plates and hardware.
2. Mount a cartridge on an extended robot tool, adding lateral and vertical adjustment joints or a precisely designed offset fixture. Replace the isolated world-anchored pin slide with a captive cartridge and an independently moving pusher contacting the pin head. Enable actual tool, chassis, bracket, pin, and beam collision; evaluate full reachable approach and retreat poses.
3. Start insertion only after the existing two-seat load/velocity gate, with the crane retained as appropriate for the assembly sequence. Drive bounded motors; use actual bore clearance and force thresholds to abort and retract. Do not overwrite pin/beam poses, turn off collision to pass through a plate, or add a fastening weld.
4. Require both dogs to deploy, remove pusher force, demonstrate a bounded proof load with dog/beam and head/bracket reactions and limited displacement, then withdraw/release the cartridge. Model how the loose pin remains supported after the cartridge leaves; the current fixture still supplies non-axial pin guidance.
5. Export actual pin, dog, pusher, and beam transforms and reaction metrics with the existing Z-up→glTF conversion. Add matching Blender nodes and explicit viewer labels separating “pin retained in isolated axial test” from “completed robot fastening.” Extend production tests with misalignment, one-dog failure, no-latch, failed withdrawal, and finite multi-axis loads before changing the canonical completion claim.

## Boundaries

The pin has one world-guided axial degree of freedom; its other five motions are constrained by an ideal cartridge fixture. That fixture can carry non-axial reactions. It cannot directly carry axial load because the insertion slide is unlimited, has no axial stop, and the motor is off; the measured head/bracket contact is the axial support. Nevertheless, this fixture remains present throughout the run, so autonomous fastening and tool departure are not demonstrated. The paired dog slides/stops are ideal internal mechanisms, not contact-resolved miniature guideways. Only one representative end lug is included; its union with the beam and the bracket's fixed foundation are ideal rigid attachments. Far-end fastening, angular alignment errors, realistic close-fit tolerances, wear, fatigue, dog strength, pin shear/bending, preload, threads, removal tooling, and coupled tower dynamics remain unmodeled. The connector has large slack and must not be presented as a final building connection.

MuJoCo implementation references: [MJCF geometry and joints](https://mujoco.readthedocs.io/en/stable/XMLreference.html) and [contact-force API](https://mujoco.readthedocs.io/en/stable/APIreference/APIfunctions.html#mj-contactforce).
