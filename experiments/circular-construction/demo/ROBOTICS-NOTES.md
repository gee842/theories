# Robot mechanism: implemented scope

The prototype uses metres, seconds and kilograms with **Z up**. The default robot faces local +Y toward two prepared docking rails. Its body is 0.68 m behind their plane. Yaw rotates around Z. Four shoulder offsets, 0.73 m upper links, 0.68 m forearms, clamp jaw geometry and a physical tool parking dock are generated parametrically. The 102 kg mass assumption includes links, clamps, chassis and a 6 kg tool.

The limbs use geometric two-link position IK with a spherical shoulder, elbow hinge, and visual wrist orientation. The solver enforces reach, elbow flexion and a shoulder cone, keeping distance from full-extension and folded singularities. Numerical shoulder/elbow/wrist positions drive nested Three.js pivots; a test confirms rendered wrists equal numerical targets even after body translation and yaw.

`createRailClimber` implements four individually checked grip steps followed by a body shift with four fixed world contacts. `planStep` samples the complete swing and verifies the three remaining anchors. Release, swing, capture, locking and load verification are distinct states. A failed verification retains three supports and can be retried. `planToolExchange` reaches the outboard upper-right tool dock; tools must be parked and the fourth grip recaptured before travel. The dock location and elbow spread were revised because the first geometry collided or exceeded the limb envelope.

`assessStance` computes the full model centre of mass, including tool custody, and an explicit quasi-static load allocation: equal upward forces at the supporting clamps, with equal keyed-clamp moments balancing the residual external moment. It checks assumed force/moment limits and shoulder/elbow torque norms, including link gravity and free-arm tool mass. Force and moment residuals are returned. A passing allocation is evidence that this particular assumed allocation balances; a failing allocation does not prove that no other allocation could work. Missing capacity inputs return `unverified` and prohibit new primitives.

Collision checks cover capsule links against each other and the torso, plus conservative expanded-box tests for caller-supplied obstacles. Motion is sampled with at least 40 intervals and a target spatial increment of 20 mm. These are sampled checks, not a proof of continuous swept-volume separation. No site obstacles are implicitly inferred: callers must provide them.

Still unverified or unimplemented:

- A physical grip design, clamp stiffness/compliance and measured capacities; all supplied capacity values are assumptions.
- Wrist joint limits/torques, mechanical shoulder axis limits, actuator selection, batteries, dynamics and grip impact.
- Clamp, parked-tool bracket, cable and detailed hardware collision envelopes. Current collision primitives represent links and torso.
- Frame attachment reactions, local rail and member stresses, wind and externally applied task forces. This load allocation includes gravity only.
- Changing rail faces around a structural corner, arbitrary body orientation optimization, and a global access-graph route planner. The checked locomotion controller currently follows one planar pair of prepared rails.
- Installation/removal of those rails, rail discontinuities, and transfers from ground equipment to the seed frame.
- Real fastener/tool operation and a coupled member-handling controller. The tool exchange primitive establishes access and custody only.

The initial four-grip stance is a commissioned initial condition, not an automatically verified bootstrap operation. Callers should retain this scope when showing robot check results and should not reposition the visual independently of `RobotState` while calling that motion checked.

Run the numerical and transform tests with `npx vitest run src/robotics/robotics.test.ts`.
