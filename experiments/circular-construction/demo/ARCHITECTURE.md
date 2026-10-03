# Architecture for continuous robotic construction

Revised 1 October 2026. The [implementation plan](IMPLEMENTATION-PLAN.md) controls the product and development order: **empty land → arriving robots and cargo → foundations and first frame → loaded climbing and swarm assembly → complete building → machine departure**. This document describes how to support that sequence. The earlier isolated workcell studies supply bounded evidence, not the main experience.

## One site state from arrival to departure

The site starts with terrain and declared ground/environment conditions. No installed frame, foundation, rail, rack, charging station or lifting equipment exists. Factory-built mobile robots and restrained cargo can enter at a visible site boundary. Site-specific facilities become available only after robots deploy them.

One persistent world state owns:

- Parts, tools and machines, with identity, geometry revision, material, mass, condition, current pose and custody.
- Erected structure, actual connection states, temporary supports, accepted stage loads and usable climbing interfaces.
- Robot attachments, carried loads, tools, energy, current action and reachable departure path.
- Inventory, storage supports, delivery vehicles and payload-specific transport assignments.
- Task dependencies, workfronts, route reservations, docking positions and shared-resource occupancy.
- Execution records, measured/assumed motion evidence, failures and recovery actions.

Building geometry is generated from installed parts in this state. A future-design overlay may show the intended result, but cannot supply collision supports, grasp points or stiffness to the executed sequence.

## Robots, material routes and bootstrap

The default supply system is ground transport plus climbing material carriers. Assemblers visibly attach from the ground, ascend and occupy supported work positions on accepted structure before deliveries begin; carriers deliver parts and overlap support during handoff. Assembler repositioning and descent use the same route and support model. Machines can share a platform where its geometry and capacities allow, but task roles remain explicit.

The first foundations, frame and climbing interfaces must be installed by mobile ground machines within their actual reach. Arriving equipment has bootstrap energy and self-unloading capability. A mobile service unit supports later missions. No permanent site plant is a hidden prerequisite.

The part catalogue links every component to a complete handling method. The previous 638.6 kg beam and heavy core-panel geometry are candidate designs, not an approved climbing payload. Redesign parts, subassemblies, payload cradles and robot teams together. Cooperative handling requires coupled motion and force analysis.

If an engineered lifting device is selected for a particular payload, instantiate a conditional equipment task branch: deliver components, unload, create support, robotically assemble, inspect, use/extend, dismantle, pack and remove. The device cannot be assumed erected. Its assembly dependencies must be satisfiable by arriving equipment and previously accepted structure.

The route graph grows only when robots install usable structure and interfaces. Installation of a next rail section or receiver is itself a delivery and connection task. The planner also preserves descent, equipment removal and last-machine escape before facade or floor closure blocks access.

## Site execution and concurrency

Each task follows a state machine:

**available → reserved → approach → capture → carry/traverse → rendezvous → place/connect → verify transfer → release → depart → complete**

Not every task uses every phase, but every payload handoff has explicit retained supports and overlapping custody. A pose target or elapsed timer alone does not prove a physical load transfer. A failure enters a supported hold and triggers a bounded retry, an alternate route, return-to-storage or a stopped incomplete run.

The planner maintains five related graphs:

| Graph | Information it contributes |
|---|---|
| Structure | Installed members, effective joints, temporary restraints and allowable next loads |
| Access | Robot/payload-specific grips, traversable routes, transitions and escape paths |
| Logistics | Cargo, racks, cradles, carrier missions, handoffs and return trips |
| Task dependencies | Ground work, first frame, extensions, bracing, floors, roof, enclosure, services and cleanup |
| Resource reservations | Robots, tools, climbing lanes, delivery positions, staging space, energy/service and simultaneous structural loads |

Parallelism comes from independent eligible tasks. Carriers cannot pass through each other or enter occupied docks. The controller must expose waiting, return traffic, workfront supply and blocked routes. Several robots should perform different tasks at once, rather than replay identical decorative motions. Faults can change dispatch and the construction schedule.

Completion is derived from the declared building bill and task record, including roof and specified systems, inspections, temporary-work recovery, descent and departure. Final closures, temporary-support removal and ground finishes receive their own acceptance before the last inspection/service machines leave. A completed planned sequence and an engineering-verified sequence are separate evidence claims. Missing engineering evidence remains visible even when the planning model can show the whole intended process.

## Geometry, dynamics, structure and display

**Blender** supplies editable building and machine models, deliberate materials and real articulated mechanisms. A shared dimensional contract supplies robot joints, mass/inertia, payload grips, rail interfaces, connector geometry and stable names to the render and physics models.

**MuJoCo** supplies articulated motion under actuator limits, payload and contact behavior, clamps, restraint forces, transfers and installation mechanics. Mink may propose target joint configurations; solver convergence alone does not establish a physically successful task. Loaded ascent, cooperative carriage, mating, departure and fault holds need their own valid operating envelopes.

**OpenSeesPy** supplies structural response at meaningful construction stages. Stage loads include robots, carried parts and concurrent work. Temporary restraints and actual connection assumptions are explicit. Deflected anchors and tolerances must be checked against robot reach and contact clearances before claiming coupled feasibility.

**Three.js** renders site state, recorded trajectories, task events and the evolving building in one scene. Cameras follow the whole site, one carrier, an assembler or a connection without substituting another world. Scrubbing reconstructs the same state and identities. Playback speed does not change engineering time.

Detailed physics can be solved offline for active work areas and then replayed alongside the site task history. Distant work still needs explicit part identity, motion, support and traffic occupancy. Reusing a solved action is allowed only within its stated geometry, payload, gravity, support and boundary conditions; geometry or load changes invalidate prior evidence. Copying a trajectory to arbitrary floors is not a verified construction method.

Use SI units. The existing bridge maps Blender/MuJoCo Z-up coordinates to glTF/Three.js as (x, z, −y), with a corresponding quaternion basis conversion. Record model, load and geometry revisions with exports. Named body bindings and matching origins prevent a visually plausible but physically different machine.

## Development order and engineering evidence

Build the complete continuous site sequence now, while advancing the loaded carrying and assembly mechanics alongside it. The first integrated demonstration must cover the whole construction story; local experiments support specific actions within it.

Distinguish three kinds of evidence:

1. **Authored design:** geometry, component catalogue and proposed actions.
2. **Executed planning/motion sequence:** tracked materials, concurrent tasks, routes, custody assumptions and completion at the stated modelling fidelity.
3. **Verified physical action or structural stage:** a result tied to the current inputs, bounded criteria, supporting reactions and relevant failure tests.

Do not promote one class into another through rendering. Conversely, unfinished hardware qualification must not prevent development of the complete, clearly identified planning sequence. The user-visible progression remains the empty-site-to-building demonstration throughout.

The current main application has an authored whole-site planning/motion sequence and a carrier-oriented Blender kit. Its new loaded one-storey experiment uses ideal grip constraints; finite-jaw locomotion and an integrated pickup/handoff cycle remain work in progress. Earlier studies retain useful but narrow scope: an unfastened seated beam, an unloaded climb, isolated pin retention and independent elastic tower snapshots. The old one-crane throughput screen applies to that earlier lifting architecture. It is not the schedule or payload evidence for the climbing-carrier fleet. The [delivery milestones](IMPLEMENTATION-PLAN.md#delivery-milestones-and-acceptance) distinguish coherent planning playback, qualified local actions, adaptive swarm behavior and regenerative recovery.

## Time, recovery and the second use

Measure arrival, bootstrap, material trips, assembly, service stops, waiting, inspection, enclosure, cleanup and departure separately. Frame erection and completed-building time are different outputs. The full schedule must emerge from tasks and finite resources before a construction-in-days claim.

Reversible connections, identifiable parts and recovery paths belong in the initial kit. Once the continuous build works, extend the same site history through inspection, supported dismantling, sorting, qualified direct reuse, repair and remanufacture. Preserve access and temporary stability during removal. Count processing loss and site residuals; abundant inexpensive energy is a scenario assumption, not a recovery yield.

The [process specification](production/autonomy/README.md) names the required machine responsibilities and custody boundaries. The [status record](STATUS.md) remains the record of demonstrated evidence. Neither a task graph nor an architectural render alone establishes real autonomous construction feasibility.
