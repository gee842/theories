# Six-axis carrier candidate — separate from production assets

This branch evaluates a motor-driven loaded hand advance with finite sliding jaws. The production Blender assets and shared construction contract have **not** been changed to this mechanism. The previous ideal-grip and finite-grip baseline traces remain comparisons, including their failures.

Each limb adds a source-Z shoulder yaw, and source-Z yaw plus source-X roll at the wrist. Existing source-Y shoulder, elbow and wrist pitch remain. Joint order is shoulder yaw → shoulder pitch → elbow pitch → wrist yaw → wrist pitch → wrist roll. The yaw joints and wrist roll each range ±0.6 rad; the original shoulder range is ±2.4 rad and elbow/wrist pitch ±2.7 rad. The links stay 0.65 m, hips remain Y±0.32/Z±0.48 m, and the physical throat stays 0.135 m ahead of the wrist. Proposed motor bounds are 400 Nm shoulder yaw, 3000 Nm shoulder pitch, 2000 Nm elbow, 150 Nm wrist yaw, 400 Nm wrist pitch and 150 Nm wrist roll. These are engineering specifications under test, not qualified hardware ratings.

An explicit 3 kg shoulder-yaw assembly and 2 kg wrist-gimbal addition per limb increase dry mass from 320 to 340 kg. With the existing 92.928 kg beam the tested total is 432.928 kg. These inertia primitives account for the candidate mass but are not completed manufactured Blender housings. No additional support, equality lock, mocap object, applied body force or live state rewrite is present.

## Controller and diagnostic corrections

The original release state machine used the previous phase's elapsed time for one control frame after changing phases. It also compared a stepped capture with the old rail height. The synchronized candidate fixes both without changing the baseline artifacts.

A finite-contact load allocator balances the free-base wrench and minimizes the largest normalized motor demand. Its forces are only a plan used to calculate motor feedforward: MuJoCo's actual contacts decide the achieved loads. Stance arms use torque control; the swing arm uses position feedback. A released limb remains closed until its measured resultant falls below 200 N. The other jaws must retain measured normal force before opening begins.

The positive-vertical-reaction gate is preserved in the older candidates. It is a conservative stance requirement, not a general test of clamped retention: a clamp may carry a downward reaction. The separately named signed candidate permits signed vertical reactions and records their values. Both pads of every retained grip must independently have at least 1000 N normal force, alongside position, friction, penetration, joint-limit, collision, actuator and body-pose checks. A negative vertical force cannot by itself establish either stability or failure.

A 0.25 ms integration step removes the jaw chatter present in the 1 ms spatial candidate. This is a numerical sensitivity finding, not increased hardware capacity. No NoSlip post-solver is used. Forces must be sampled from the contact solve that actually advanced the state; a second forward evaluation at the next position is not that force sample.

The straight upward hand path is obstructed: an opened inner finger intersects a horizontal rail-to-column bracket. Classifying every jaw/environment contact as a grip concealed this collision. The clearance candidate counts only rail contacts as intended support, and independently records jaw/receiver/bracket collisions. Its swing path withdraws 0.12 m over 2 s, rises 0.32 m over 5 s, then approaches over 2 s. Nineteen kinematic route poses showed no environment penetration for the released hand; this is only a route-geometry check, not dynamic proof.

## Reproduction and limits

`finite_grip_clearance.py --mode limb --shift-x .16` is the current six-axis route evaluation. Results, exact XML and traces use the `candidate-clearance-` prefix. The earlier `candidate-bidirectional-` run loses physical retention, and `candidate-contact-convergence-` hits the bracket and exceeds the pose limit; neither is accepted climbing evidence.

Contact friction is assumed (nominal μ0.65); the frame is rigid; the payload is already locked to the cradle. Robot-to-environment collisions use simplified shapes. Self-collision, actual reducer/bearing design, restraint closure, compliant structural response, entry from the ground and arbitrary frame traversal remain unqualified. In particular, six axes make spatial positioning/orientation possible but do not demonstrate routes between columns or around beam joints.

## Evaluated packaging successor

`finite_grip_packaged.py` is now the evaluated successor; `six-axis-proposal.json` is its separate proposed integration contract. It narrows the central casing to 0.66 × 0.44 × 1.0 m, retaining its specified 160 kg mass, and reduces swing withdrawal to 0.055 m. Robot self-collision is active between distinct assemblies. Forty-eight named exclusions cover overlapping primitives in connected wrist bearings and jaw guides; they do not exempt the casing, different limbs, payload or frame. The narrower casing addresses an observed ~57 mm wrist/casing penetration in the earlier 0.12 m retreat; the older contact-only pass must not be treated as packaged clearance evidence. A mass-preserving physical arrangement of batteries, drives and structure still needs detailed engineering.

The packaged single-hand test passes: the hand advances 0.32 m, closes on the rail, accepts a measured approximately 1.88 kN resultant proof load and holds for three seconds. Minimum retained-pad normal force is 3.407 kN, maximum retained-throat drift 1.50 mm, maximum contact penetration 0.752 mm, unintended collision force zero, maximum body tilt 0.00359 rad and force-balance residual 0.463 N. Peak shoulder/elbow/wrist-pitch torques are 1340/1622/348 Nm; added hip-yaw/wrist-yaw/wrist-roll peaks are 324/100/104 Nm. Only two contacts are upward during part of the three-clamp stance; the downward reaction is measured and all three remain retained. The full four-hand/base-increment run is a separate result, not implied by this single-hand pass.

The accepted load transfer interpolates between feasible three- and four-contact plans over two seconds. The preceding abrupt-switch experiment attained the final loaded state but briefly lost one retained pad's normal contact and is rejected. Neither its gate nor the friction/torque bounds were weakened to make the successor pass.

The fixture and robot remain rigid collision approximations, pad friction is assumed and the payload is prelocked. The production Blender model still has the older casing and joints until this proposal is accepted and deliberately integrated.

## Complete local climb and ground-gear successor

`finite_grip_continuous.py` additionally gives the four ground-gear modules explicit 8 kg masses and wheel/fork collision shapes. The central chassis mass becomes 128 kg; total dry mass remains 340 kg. The climb pose has 120 mm unloaded suspension droop, moving wheel centres from source Z=−0.63 m to −0.75 m. Ground travel and the suspension transition are not simulated. Smooth two-second load redistribution now precedes every release as well as every recapture, with a measured unloading dwell before the jaws open.

The complete four-hand and chassis step passes: all hands advance 0.3198–0.3200 m and the chassis rises 0.32085 m over 90.002 s. Minimum retained-pad normal force is 3.720 kN, maximum retained-throat drift 1.41 mm, maximum contact penetration 0.724 mm and unintended collision force zero. Body tilt peaks at 0.00702 rad; the measured force-balance residual peaks at 0.00143 N. Maximum grip resultant is 4.721 kN. Peak shoulder/elbow/wrist-pitch torques are 1987/1626/325 Nm; hip-yaw/wrist-yaw/wrist-roll peaks are 325/52/15 Nm. This passes the original physical bounds and the explicit signed-retention checks; the count of upward reactions remains diagnostic and reaches two.

The predecessor `candidate-packaged-step` reached the final pose but briefly lost one pad during an abrupt later unloading transfer, so it remains rejected. Likewise the first explicit-wheel candidate failed with abrupt unloading. These results are retained, not replaced with the accepted trace.

A separate injected-closure-fault test rejects the climb and keeps the three retained clamps loaded for five seconds (`recoverySupported=true`, `complete=false`). It uses the earlier narrow-casing model without explicit wheel inertias, so it does not automatically qualify recovery for the later wheel model. The μ0.2 hold counterpart is rejected before a stable hold is established. Its one-second measurement window is never reached; sentinel minimum values are not valid retention evidence.

The editable manufactured successor is now separately saved as `production/blender/six-axis-carrier-candidate.blend` and `.glb`. It contains the specified six pivot axes, narrower serviceable casing, nested wrist bearings and guided jaws, and an unloaded suspension pose. It does not overwrite the production libraries. The candidate preview uses a recorded dynamics pose. Hip/knee reducer and wrist-gimbal envelope additions are being checked by `finite_grip_manufactured.py`; the preceding 1801-frame geometric audit found no penetration but is explicitly a sampled-state check, not a dynamics rerun.

## Final evaluated local candidate

The larger manufactured-envelope dynamics rerun **also passes**, with the same 0.32085 m chassis advance and unchanged numerical metrics; its added casing envelopes never touch the frame or other independent assemblies. The canonical runner is `finite_grip_manufactured.py`, the accepted controller is `finite_grip_continuous.py`, and the exact nominal output is `candidate-manufactured-step-92.928kg-mu0.65-sx0.16-*`. `candidate-evidence-index.json` names the current deliverables without hiding the preceding experiments.

The closure-fault test was repeated with this same wheel and manufactured-housing model in `finite_grip_continuous_fault.py`. It rejects completion while sustaining the three retained clamps through the five-second supported stop (`recoverySupported=true`). It does not claim that the disabled fourth gripper recovered, that friction loss is recoverable, or that indefinite suspension is safe. The accepted single-step, this fault response, the lower-friction rejection and the old baseline all retain separate traces.

`test_candidate_acceptance.py` checks the actual four proof-load events, chassis/hand displacement, retained normals, penetration, unintended collision, force balance, motor bounds, zero equality/mocap restraints and the corresponding editable GLB joint names. `test_finite_grip.py` still checks that the original baseline's negative results remain rejected.
