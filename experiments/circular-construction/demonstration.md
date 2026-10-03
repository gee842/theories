# Three.js demonstration specification

30 September 2026 · Historical specification derived from the [research brief](README.md).

**Superseded for product scope and implementation order on 1 October 2026 by the [current implementation plan](demo/IMPLEMENTATION-PLAN.md) and [architecture](demo/ARCHITECTURE.md).** The current plan requires Blender assets and detailed robotics dynamics within one continuous empty-site-to-complete-building demonstration. Climbing carriers are the preferred material route; any lifting equipment must itself be assembled and removed visibly. The connection-first order, optional Blender wording and default hoist route below describe the earlier proposal. Retain the mechanics requirements as background where consistent with the controlling plan.

## What the viewer should be able to establish

The demonstration should answer a concrete question: can the proposed machines transform a finite inventory into a useful building, and return its components to further use through a physically coherent sequence?

Keep three kinds of evidence visible: observed capabilities in external experiments, constraints checked by this simulation, and assumed future capabilities. A cinematic playback may compress time, but the construction clock, queues, failures, and material ledger must still come from the same execution record.

The ultimate scene is an entire lifecycle. The first engineering milestone is a single connection operation. Scaling up before that operation is coherent would multiply the same untested assumption.

## Visual sequence for the complete lifecycle

| Stage | Visible actions | What must be represented |
|---|---|---|
| Prepare | Survey, establish working access, foundations and material yard | Site boundary, soil assumptions, equipment, disturbance, stock origins, preparation duration |
| Bootstrap | Ground machine places and braces the first stable frame | Foundation reactions, temporary fixtures, real lifting support, initial robot access |
| Build frame | Carriers supply the hoist; climbers extend approved workfronts | Grips, bodies, members, slings, latch motion, tool changes, connections, loads, queues |
| Close and service | Lift floor cassettes, install roof/facade, connect accessible services | Added weights, diaphragm status, changed wind area, retained tool and transport access |
| Commission and use | Inspect and test; occupy the completed space | Which checks are modeled, commissioning duration, occupancy readiness distinguished from frame completion |
| Maintain | Support and replace a selected damaged part | Temporary load path, access, isolation of affected space, quarantined part |
| Dismantle | Isolate services, add necessary restraint, recover modules and members | Checked removal sequence, supported releases, robot retreat, final ground-machine recovery |
| Inspect and recompose | Sort, repair or reprocess; build a different arrangement | Persistent part IDs, condition changes, stocks, process yield assumptions, losses and new inputs |

For the first complete building, foundations, services and material reprocessing may be explicit schematic subprocesses. Give each an input, duration, output, and unverified-status label. Do not imply that detailed autonomous machinery exists for a stage merely because a progress bar advances. Subsequent milestones replace these abstractions with engineering models.

## The component contract

Every part type needs units and structured metadata independent of the rendered mesh:

- Geometry, mass, center of mass, section or layer properties, connection locations and permitted variants.
- Structural capacities and stiffness model, including where these are measured, calculated, assumed, or absent.
- Lifting points and gripper sites with admissible forces and moments.
- Connection insertion trajectories, lead-in region, adjustment range, tool approach envelope and removal clearance.
- Compatibility: member family, fastener type, version, required access, permitted reuse history.
- Inspection evidence and condition state for the actual serialized part.

A rendering mesh is not automatically a collision mesh, and a collision mesh is not a structural model. Derive all three from the same dimensions but keep their functions separate.

A structural adapter may have several ports, but their occupancy can conflict. The contract must express exclusions: a diagonal or collar may obstruct a wrench, gripper, cable, or member insertion. Place a member only if the complete approach and future required operations remain feasible.

Reusable joints need physical assembly allowance. Two close-fitting sockets fixed at the ends of a rigid beam may make insertion impossible. Investigate a seated connection with an accessible removable closure or connector plate, rather than assuming a beam can slide axially into two closed pockets simultaneously. Whatever accommodates installation must have a defined final restraint and stiffness.

## Robot mechanics

Begin with a parametric four-limb robot and simple collision geometry. Include the mass of motors, tools, batteries, clamps, and carried items. Do not present a payload rating until pose-dependent forces and actuator limits have been modeled.

Each limb has modes `free`, `approaching`, `captured`, `locked`, `load_verified`, `tooling`, and `fault`. Contact detection alone does not imply a locked grip. A grip becomes an eligible support only after its modeled verification.

Use one-limb-at-a-time travel as the initial policy. Working and traveling are different state transitions:

`three anchors + tool → park tool → fourth grip verified → unload one anchor → release → move → recapture → verify`

Tool exchange is a physical operation. The tool dock occupies space, the tool has mass, and exchange takes time. A two-ended beam may require two climbers, each with three anchors and one guiding limb. The lifting cradle continues carrying the assigned weight during alignment. Where one climber services both ends sequentially, show the parked beam and verified support before that robot moves.

### Kinematic checks

For a chosen set of anchors, solve body pose and limb inverse kinematics together. Enforce joint limits, reach, self-collision, environmental collision, and useful clearance from singular configurations. Locked grippers remain at fixed world poses unless compliance is explicitly modeled; they must not slide along beams to make an animation fit.

A candidate step comprises release, collision-free swing, capture, verification, and load transfer. Check intermediate poses, not only endpoints. An interpolated endpoint-to-endpoint animation can pass through a diagonal or pull a locked foot off its anchor.

Planning should initially use discrete known docking sites and a library of parameterized, validated motion primitives. Global path search finds a route through these sites; local optimization resolves actual motion. This is simpler to debug than training an unconstrained end-to-end policy before the kit or success conditions exist. Learned perception or local controllers can be compared later without replacing the physical contract.

### Contact and load checks

For each quasi-static stance, solve a bounded contact-wrench problem:

`G(q) × w + w_external = 0`

Here `w` contains the allowed forces and moments at the active grips. `w_external` includes robot weight, any carried or guided load share, and tool reactions. Include joint torque constraints through the contact Jacobians and gravity terms. Each grip has a declared admissible wrench set; a point contact cannot be silently given the moment capacity of a keyed fixture.

Also apply the opposite grip and hoist reactions to the current frame. Local flange bending, tube-wall loading, collar attachment, torsion, and deformation may govern before the overall building load capacity is reached.

A solution under assumed limits means only that those assumptions admit equilibrium. It does not validate clamp hardware, stiffness, slip behavior, fatigue, collision tolerances, or dynamic motion. Missing capacities produce `unverified`, never a default green pass. Speed limits must remain tied to the quasi-static assumption until a dynamic study justifies faster motion.

Use dynamics software for difficult handoffs and contact transitions. MuJoCo is a candidate for robot and contact experiments, with measured or explicitly assumed parameters; it cannot substitute for structural assessment of the building. [MuJoCo computation documentation](https://mujoco.readthedocs.io/en/stable/computation/index.html)

## Connection transaction

For each beam, preserve one visible support history:

1. Reserve the correct inspected part, assembly workers, hoist, anchors, insertion corridor, tool access and retreat path.
2. Transport the serialized beam from stock to a defined lifting point.
3. Attach the sling or cradle, verify capture, and move the supported beam to the workfront.
4. Guide its ends into designed capture seats without collision or impossible deformation.
5. Verify temporary support before changing tools or reducing lifting support.
6. Assemble and verify the final structural joints at both ends. The verification method depends on the selected fastener; a generic torque value alone is not universal proof of correct pretension.
7. Evaluate the resulting construction stage with the actual robot, beam, temporary-support and hoist loads.
8. Transfer load incrementally, verify the supported state, detach the lifting device, and release reserved resources.
9. Mark approved robot docking points as available only when their supporting load path is accepted.

Before final verification, the beam can be physically present while remaining unavailable to support future work. This distinction is essential.

If a latch mis-seats, preserve the hoist support and either retry through a feasible path or return the part to a buffer. Failure cannot be solved by marking the task successful after a fixed number of animation loops. Every recovery action requires the same reach, load, inventory and access checks as ordinary work.

## Construction planning

Maintain related models with different meanings:

| Model | Meaning |
|---|---|
| Structural model | Members, joints, restraints, current loads, stiffness, and qualified capacities |
| Access graph | Available grips, robot stance transitions, corridors, and retreat routes |
| Task dependency graph | Necessary predecessor operations and alternative methods for the current plan |
| Resource reservations | Time occupancy of robots, hoists, staging buffers, tools, docks and swept volumes |
| Inventory ledger | Identity, custody, condition and material state of parts and process streams |

A connected structural graph is not a stability calculation. A route through an access graph is not automatically collision-free. Neither is a guarantee of contact force feasibility.

A practical initial scheduler repeatedly:

1. Finds eligible operations from dependencies and current evidence.
2. Rejects operations with unavailable stock or unreachable work locations.
3. Constructs candidate supports, robot stances and material approach paths.
4. Checks the staged structure, robot loads and local connection conditions.
5. Reserves shared resources and robot escape routes.
6. Executes the chosen operation with sensor-state transitions and logged outcomes.
7. Updates models only after the relevant verifications succeed; replans after delays or faults.

Use a deterministic seeded planner with inspectable priorities before a sophisticated global optimizer. It should seek throughput within hard constraints, with penalties for extra transport, temporary works and trapped access. State the objective rather than assuming every fastest solution is materially best.

Assembly sequence and robot motion must be planned together; published construction research provides a relevant precedent. [Huang et al., 2021](https://arxiv.org/abs/2105.11438). NASA's assembly-order work addresses robots traveling over the structure they build and provides another useful planning baseline. [Peters et al., 2025](https://ntrs.nasa.gov/citations/20250002467)

### Structural validation

Use a suitable frame model or an externally checked stage library. A first-order axial truss solver is acceptable only for states whose actual joints and load transfer match that abstraction. Beam bending, connection stiffness, instability, second-order behavior, local effects, foundations and construction loads cannot be dismissed because the final geometry resembles a truss.

OpenSees is a candidate for external frame analysis, including appropriate beam-column elements and geometric transformations. Choosing it does not validate the model; section definitions, restraints, loading, convergence and applicable capacity checks still need engineering review. [OpenSees modeling capabilities](https://opensees.berkeley.edu/OpenSees/user/modellingCapabilities.php)

Cache a checked stage only for the exact support, load and geometry assumptions it represents. Robot movement, hoist reactions, wind or missing bracing can invalidate that cache. In the UI, describe the scope of a passed check, such as “linear stiffness check passed for listed loads,” rather than “building safe.”

### Deconstruction is a new plan

First isolate services, clear the affected space, and inspect the actual structure. Restore temporary supports where needed. Hold a member before releasing its fasteners. Keep the last machine's exit and the last support's removal feasible. Finish with ground equipment retrieving the seed and lifting infrastructure.

Use reverse assembly order as a candidate, not a proof. Occupancy changes, damage, grip accessibility, corrosion, enclosure, cable routes and available inventory can make the correct removal sequence different.

## Three.js and Blender implementation

Proposed local project structure:

```text
src/domain/          component contracts, units, condition and inventory
src/planning/        tasks, access graph, reservations, recovery
src/robotics/        kinematics, motion primitives, contact checks
src/structure/       solver adapters, stage validation, load cases
src/simulation/      event clock, deterministic state, execution log
src/view/            Three.js scene, controls, inspection overlays
assets/              optional Blender sources and exported GLB assets
scenarios/           kit, site, target structure and test cases
```

Simulation state owns the world. Three.js renders that state and may interpolate only approved motion segments. Camera playback speed changes presentation time, not construction duration. A paused scene should expose the part's custody and why each robot is waiting.

Use `InstancedMesh` for repeated installed members where appropriate; retain a stable mapping from domain part IDs to render instances. Use separate articulated transforms for active robot limbs and handled parts. Three.js documents instancing as a way to reduce draw calls for repeated geometry. [InstancedMesh](https://threejs.org/docs/pages/InstancedMesh.html)

Create robots and connection mechanisms procedurally while geometry is changing. Later, use Blender for readable machine bodies, joints, latches and surrounding architecture, retaining correct pivots, dimensions and component names. Import GLB assets using the documented glTF loader. Baked decorative animation may improve presentation, but support feet and load-bearing motion remain driven by the simulation. [GLTFLoader](https://threejs.org/docs/pages/GLTFLoader.html)

Run planning and appropriate numerical work outside the rendering loop, using workers or a backend where needed. Export reproducible event logs and snapshots so the same sequence can be replayed, inspected and compared across model revisions. Pin dependencies when implementation starts; this research does not select an unverified “latest” version.

The essential view has the construction site, material yard, lifting route and working robots. Offer close inspection of one robot, joint or part, plus time controls and overlays for active grips, loads, verified supports, reserved paths and material state. A large field of decorative robot activity should never stand in for simulated work.

## Experiments in dependency order

| Milestone | Pass evidence | Failure that must be visible |
|---|---|---|
| Detailed node and insertion | Beam can enter, latch, fasten and leave under declared tolerances; both-end access shown | Connector clashes, inadequate tool space or geometrically impossible insertion |
| One robot around a corner | All intermediate poses satisfy declared reach, collision, grip and actuator limits | Infeasible three-anchor stance or blocked swing |
| One beam transaction | Supply, lift, guide, capture, fasten, verify, release, remove and return with a complete support history | Mis-seated latch holds the hoist and triggers recovery |
| One braced bay grows | Every intermediate state passes the stated structural model | Removing a required brace prevents advancement |
| Small building lifecycle | All lifecycle stages represented with maturity labels; identified components enter a second layout | Unknown service or foundation behavior remains explicitly schematic |
| Multiple workfronts | Computed schedule includes delivery, motion, tools, inspection, queues and recovery | More robots stop improving throughput at a real shared constraint |
| Physical prototype program | Measured grip, connector and integrated-cycle behavior reconciled against simulation | Tolerance, wear or force mismatch requires model revision |

Negative cases are part of the demonstration, not incidental debugging: missing material, blocked insertion, a failed grip, seized hardware, robot outage, delayed delivery and an inadmissible removal should produce intelligible holds or replans.

Track time to completed frame separately from time to commissioned building. Track useful component output separately from recyclable feedstock. Track successful recovery separately from zero-fault execution. These distinctions make the demonstration useful for research as well as communication.
