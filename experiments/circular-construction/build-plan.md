# Build plan for the autonomous circular construction demonstration

30 September 2026 · Historical implementation proposal based on the [research brief](README.md), [evidence register](evidence.md) and [earlier demonstration specification](demonstration.md).

**Superseded on 1 October 2026 by the [current implementation plan](demo/IMPLEMENTATION-PLAN.md).** The current deliverable starts with empty land and arriving robots, uses climbing material carriers by default, shows the whole construction swarm completing a 20-storey building, and ends with all machines departing. Blender assets and robotics dynamics develop alongside that full sequence. The mechanism-first order, mandatory hoist, provisional six-to-eight-storey target and procedural-first assets below are retained only as research history.

The deliverable is an interactive Three.js demonstration in which an autonomous team constructs a building, maintains it, dismantles it, and uses recovered components in a different building. The machines operate through an inspectable simulation. Its engineering conclusions are conditional on declared geometry, loads, capacities, and process assumptions.

The implementation order is **reversible mechanism → growing structure → complete small lifecycle → large autonomous site**. Each stage produces something usable and visible. Rendering and numerical work proceed together, using one component model and execution record.

## Product scope and proposed showcase

Use one persistent site with a material yard, carriers, lifting equipment, four-limbed climbing assemblers, and a building that grows from the ground. Follow selected steel members through both configurations. The yard, temporary works and last robot's exit remain visible throughout.

The provisional final target is a large modular building of six to eight storeys. An initial composition study may use a 36 × 24 m footprint, 6 m bays and approximately 3.6 m storeys. These are adjustable visual and planning inputs, not a structurally selected building or a forecast of achievable size. Freeze dimensions only after the kit and climbing mechanism work. The final showcase type remains a preference the user can steer.

Configuration A should be a compact multilevel shared workshop and learning building. Configuration B should visibly change the organization of space, potentially into lower wings around a shared court. Generate both bills of materials from the same qualified kit. Additional roof, facade or foundation components enter the ledger explicitly; the second building need not consume every recovered member.

The first complete software release includes the full lifecycle. Structural erection, climbing, handling and reversible connections receive detailed mechanics. Site surveying, soil behavior, selected service installation and metallurgical reprocessing can initially be bounded schematic processes with explicit inputs, durations, outputs and uncertainty. The interface identifies those boundaries where relevant.

A physical robot or certified building is a later research outcome. Completing this digital demonstration does not require fabricating hardware, but it must expose the hardware capacities and tests still needed.

## Decisions to carry into implementation

| Decision | Starting choice | Reason and revision point |
|---|---|---|
| Construction system | Braced steel frame with reusable members and separate accessible layers | Permits staged support and meaningful reuse; compare short-member trusses if handling or connections govern |
| Robot team | Four-limbed assemblers, ground carriers and a bounded hoist/crane | Gives climbers local manipulation tasks and heavy loads an explicit support path |
| Connection | Compare an open seat with removable closure against an accessible adapter-plate concept | Both must solve two-ended insertion, capture, final restraint and later extraction before selection |
| Climbing environment | Known replaceable docking sites and rails attached to the kit | Enables explicit reach and load checks; their installation and recovery are real tasks |
| First autonomy | Dependency planning, resource reservations and parameterized motion primitives | Produces explainable runtime decisions in a deliberately structured environment |
| First mechanical model | Quasi-static robot contact checks plus appropriate frame analysis | Focuses on slow controlled manipulation; dynamic claims require a later model |
| Software | TypeScript, Three.js and Vite; local Python numerical runner | Keeps interaction and rendering accessible while using numerical tools outside the render loop |
| Assets | Procedural geometry initially; Blender after geometry stabilizes | Makes mechanical revisions inexpensive and preserves dimensions and pivots |
| Delivery | Local research application plus portable replay of recorded runs | Supports experiments locally and an inspectable browser presentation of exactly those results |

No deadline is assigned before the coupled mechanism experiment. Its result can change the joint, robot, rails and work method together. Progress is measured by executable milestones rather than the volume of scene content.

## Milestones and completion criteria

### 0. Establish the shared model and visible test site

Create the application under `experiments/circular-construction/demo/`, keeping the existing research files as its rationale. Set up the TypeScript application, headless simulation entry point, numerical runner, and a small test scene with orbit, pause, operation-step and object selection.

Define SI units, coordinate conventions, stable IDs, component variants, connector states, grip modes, tool custody, support relationships, and an event clock. Adopt a Z-up engineering world and convert Blender/glTF assets at a single documented boundary. A serialized part is distinct from its reusable type definition.

Each input records its basis: assumed, calculated, catalog data, or measured. Each check separately reports passed, failed or unverified **under its stated model**. A successful calculation does not convert an assumed clamp rating into a measured rating.

Include a deterministic replay fixture immediately. Schematic events can exercise the presentation, but must carry their schematic status and cannot generate mechanical validation results.

**Complete when:** the same fixture produces the same ordered events and final inventory headlessly and in the browser; replay speed changes only presentation; every visible part can be traced to a world-state ID.

### 1. Co-design the joint and the climbing robot

Develop two parameterized benches in parallel:

- A connector bench: one beam between two support nodes, surrounded by representative diagonals, rail collars and floor-edge geometry.
- A climbing bench: two perpendicular frame faces and a level change, with adjustable docking sites and a physical tool dock.

Start with a 3 m handled member for the bench and include the researched 6 m handling case as a sensitivity. Those lengths are test inputs. Vary bay dimensions, robot link lengths, docking pitch, clearances, offsets and tool orientation together rather than selecting a finished robot body first.

Implement joint-limited inverse kinematics, self/environment collision, fixed poses for locked grips, tool mass, and work-to-travel transitions. A geometric path must include approach and extraction at both beam ends.

For checked poses, solve static force and moment balance, allowable grip wrench directions and joint torque demands. First calculate required capacities; then test explicit candidate hardware envelopes. Unknown capacities remain conditional. Where three grips are collinear, test the actual moment constraint instead of allowing unlimited clamp torque. Include compliance assumptions and equal-and-opposite robot reactions in the support model.

Use conservative swept collision envelopes and adaptive intermediate checks for trajectories. Record sampling resolution and model scope; endpoint-only checks are insufficient. Numerical tolerances and physical fit tolerances are separate inputs.

**Complete when:** one geometry supports both insertion/removal and a full corner/level traversal, including tool parking. Nominal and perturbed cases run; impossible clearance or load cases are rejected. Freeze the first kit/robot baseline only here.

### 2. Complete one reversible beam transaction

Combine the benches into a visible work cell: braced supports, one carrier, finite lifting envelope, two climbers, one beam and its tools. The initial bench supports can be anchored test fixtures with explicit reactions; construction of those supports becomes part of the next milestone.

Execute:

`reserve → receive → lift → guide → capture → fasten → inspect → transfer load → detach lifting support → retreat`

Then execute a separately checked removal, return, inspection and reuse at another compatible position. The hoist, temporary seat and final connection must have distinct support responsibilities. Check the system throughout load transfer.

Add a misaligned latch, unavailable grip and delayed delivery. Recovery consists of real operations—hold, regrasp, retract, reseat or return. Failed verification must keep the beam unavailable to support new work.

**Complete when:** the operation runs from inventory to second use with a continuous support history, physical tool exchanges and checked motion. All injected cases either recover through modeled actions or stop in a supported state with a clear unresolved cause.

### 3. Grow and recover a small frame autonomously

Use a two-by-two-bay, two-storey benchmark generated from the selected kit. Ground equipment establishes the foundations/anchors, temporary works and braced seed before the climbers enter.

Implement assembly dependencies, qualified work locations, part allocation, a runtime scheduler and reservations for equipment, docks, buffer space, approach corridors and retreat paths. Start with one work cell, then allow two to operate concurrently. Reserve resources conservatively before optimizing concurrency.

Deliver the thin localhost numerical bridge in this milestone. A changed workfront must generate fresh requests to the numerical runner during execution, and the planner may commit the resulting action only after matching results return. Exercise this with an access change or injected fault, and deliberately return an obsolete response to verify that it is rejected. File-based fixtures remain useful for benchmarks and replay, but do not stand in for live replanning.

Evaluate construction stages with beam/column behavior and the declared connection model. Include gravity, robot and hoist reactions, temporary bracing, relevant lateral loads and support conditions. Combine concurrent load cases; separate passing checks for two robots do not establish that their simultaneous loading is acceptable. Linear analysis can support an initial bounded claim; instability, second-order effects and local attachments need the additional checks appropriate to the chosen frame.

Plan dismantling from the actual current structure. Recover the last climber, seed and temporary works through ground equipment.

**Complete when:** the scheduler builds and removes at least two target layouts; altered stock or access changes its decisions; a missing critical brace blocks progression; every accepted state identifies the structural checks actually performed.

### 4. Complete the building and material lifecycle at small scale

Add independently handled floor, roof and facade cassettes, accessible service modules, commissioning, a maintenance episode and inspection on return. The order must preserve lifting clearance, future tool access and effective restraints. A floor becomes a diaphragm only after its required ties are in place.

Track energy consumption or work requirements where the model supports them, alongside battery/charging, maintenance and consumable assumptions. Cheap energy does not erase equipment downtime. Detailed service or reprocessing machinery can remain schematic at this stage, with its input/output balance and duration visible.

Represent damage as a changed condition. A removed member can be qualified for reuse, repaired and reassessed, quarantined, or converted to a material batch. Remanufactured parts receive new identities linked to the source batch. Directly reused parts retain their original identities.

Generate and build configuration B from available suitable inventory. Reconcile material in both buildings, yard stock, repair, processing, new inputs and losses. Distinguish actual qualified recycled output from feedstock waiting to be processed.

**Complete when:** the viewer can follow the entire lifecycle and an identifiable member through both useful configurations. The ledger closes and the full process includes preparation, temporary works, commissioning, maintenance and final recovery.

### 5. Expand autonomous operation and failure handling

Add multiple work cells, lifting demand, delivery queues, tool availability, charging and recoverable equipment outages. Detection uncertainty should progress from an explicitly idealized state observer to selected delayed/noisy grip and connection observations. Ground truth and observed state remain distinct when uncertainty is enabled.

Use runtime task selection and routing. Hand-authored motion primitives are acceptable; target geometry and current conditions determine their placement and order. Introduce deadlock detection, bounded retries and compensating recovery tasks. Equipment replacement or rescue must involve an available modeled machine with a feasible route.

**Complete when:** delivery delays, blocked grips, failed verification and an unavailable robot produce different valid plans; unresolved failures are surfaced; repeated seeded runs can be compared without changing results through renderer frame rate or numerical response timing.

### 6. Scale to the large building and measure the result

Generate the final six-to-eight-storey showcase from the tested component family. Resolve its sections, bracing, lifting reach, robot access and component bill before running the full schedule. Enlarge lifting infrastructure through explicit added equipment or support/relocation tasks.

Run fleet and logistics sensitivities. Measure completed placements, workfront availability, hoist occupancy, delivery queues, idle reasons, retries, downtime and material use. Record separate clocks for frame completion and whole-building commissioning; distinguish supplied prefabricated stock from upstream manufacturing.

Use the same planning rules and motion/structure checks as the small scene. Cache by complete input/model fingerprints, and exploit repeated modules only where the load and boundary conditions justify reuse of a result. Rendering detail may decrease with distance while domain state stays intact.

**Complete when:** a full-scale run and its recovery/recomposition execute to completion under declared assumptions; bottlenecks explain the duration; adding robots stops helping when another capacity governs. If construction takes longer than days, the measured result remains the result and motivates a revised system.

### 7. Finish the experience and deliver reproducible scenarios

Refine settled robot and joint assets in Blender where this improves legibility. Preserve mechanics, collision geometry, pivots, dimensions and IDs. Add lighting, readable material treatments, camera choreography, enclosure cutaways and reduced-motion behavior.

Two presentations share the same world state:

- **Guided story:** stock, bootstrap, close connection, growing building, useful occupation, maintenance, dismantling and second use.
- **Engineering exploration:** free orbit, operation stepping, follow robot/part, joint inspection and focused load/access/material overlays.

Switching presentation preserves time and selection. A viewer can interrupt a close-up and inspect why a machine is waiting. Use short explanations near the relevant object rather than a permanent wall of metrics.

Deliver source, scenarios, locked dependencies, run commands, recorded traces, assumptions, check summaries and a portable browser build. Publication is a separate delivery choice. A reference-machine performance benchmark is set during implementation; desired large-scene target is smooth interaction at 1080p with a 30 fps minimum on the measured reference machine, with details recorded rather than claiming universal performance.

**Complete when:** the full story is watchable, every inspected operation corresponds to the same execution record, browser controls and replay work, source and traces reproduce the demonstrated outcomes, and unresolved engineering boundaries are legible.

## Software architecture

Keep one local application and one numerical runner. The application has a pure TypeScript domain/simulation core usable in a worker or headless process. Three.js owns presentation only. Begin with file-based numerical request/result fixtures; deliver the thin localhost bridge in milestone 3 for live replanning.

```text
Target layout + finite stock + equipment + assumptions
                         ↓
        Deterministic task and motion planner
                         ↕
  Kinematics / collision / contact / structural checks
                         ↓
       Execution events + trajectories + evidence
                  ↙                 ↘
         Three.js view       Replay and analysis
```

Proposed layout:

```text
demo/
  src/domain/        schemas, units, part identity, state transitions
  src/simulation/    event clock, execution, checkpoints, replay
  src/planning/      dependencies, routes, reservations, recovery
  src/robotics/      kinematics, contact requests, motion primitives
  src/structure/     load extraction and validator adapters
  src/view/          Three.js scene, cameras, inspection, controls
  numerical/         Python contact and structural adapters
  scenarios/         benches, bays, building layouts, faults, assumptions
  assets/            editable Blender files and exported models
  tests/             mechanical examples, invariants, scenario/browser checks
  runs/              exported manifests and reproducible execution records
```

The shared contract has six central records:

| Record | Owns |
|---|---|
| `PartType` and `PartInstance` | Geometry/capacity family; actual identity, condition and location |
| `RobotModel` and `RobotState` | Links, masses, limits, tools; joints, attachments and current task |
| `ConnectionState` | Alignment, capture, fastening, inspection and load eligibility |
| `Task` and `Reservation` | Preconditions, resources, motion, duration, outcomes and recovery |
| `ValidationResult` | Exact inputs/model version, scope, status, residuals, margins and evidence basis |
| `ExecutionEvent` | Simulation time, stable ordering, affected IDs and committed state change |

Version interchange schemas and validate the same fixtures on both sides. Give numerical requests a world revision and hashes of geometry, loads, supports, capacities and solver configuration. Reject stale results. A late solver response must not reorder simulated events or validate a changed workfront.

Use fixed simulation-time conventions and deterministic tie-breaking. Advance discrete tasks on the event clock; render approved trajectories at presentation rate. During interactive computation, the simulated decision waits for its required result while the UI remains responsive. Numerical wall-clock time is not silently added to modeled construction time; modeled controller latency, when studied, is an explicit input.

Recorded runs include the solver outputs used, so they can be replayed without numerical installation. A static replay supports inspection and recorded branches. Arbitrary edited layouts or new fault scenarios require a numerical rerun unless they lie within an explicitly validated parameter envelope; the UI must distinguish replay from a newly solved experiment.

Exact playback uses recorded events and trajectories. Fresh numerical solutions are compared within stated tolerances; bit-identical optimization results across different platforms are not a requirement.

## Numerical implementation and verification

Use NumPy/SciPy for the first numerical harness. At a fixed robot pose, bounded contact wrenches and torque inequalities can be formulated as a linear feasibility problem using an appropriate conservative polytope. Explicitly set signed force/moment bounds; SciPy's default nonnegative variable bounds would be wrong for some wrench components. [SciPy linprog documentation](https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.linprog.html)

Use an OpenSees/OpenSeesPy adapter as the preferred frame-analysis path, after a host/runtime smoke test and analytical benchmarks. Its installation documentation lists Windows, Linux and Mac, but the compatible architecture/Python combination still needs testing locally. If the native combination fails, use a reproducible supported runner and preserve the same request/result contract. This is a packaging fallback, not permission to substitute graph connectivity for structural analysis. [OpenSeesPy installation](https://openseespydoc.readthedocs.io/en/latest/src/installation.html)

MuJoCo remains a focused later tool for contact transitions, compliance, cradle handoffs or swing dynamics that the quasi-static model cannot justify. It is not required to run the entire site from the first build. The motion-speed and load assumptions must match whichever model actually supports them.

Choose and pin compatible tool versions during milestone 0. Vite supports a plain TypeScript application and static production output; a UI framework is unnecessary for the initial controls. [Vite guide](https://vite.dev/guide/). Use Three.js instancing for repeated geometry after profiling; preserve selection and per-part IDs independently of draw-call optimization. [Three.js InstancedMesh](https://threejs.org/docs/pages/InstancedMesh.html)

Tests should establish consequences, not mirror implementation:

| Check | Required evidence |
|---|---|
| Analytic mechanics | Beam reactions/moments and simple frame displacement agree with independently derived examples within stated numerical tolerances |
| Robot contact | Impossible moment balance and exceeded joint limits fail; adequate comparison cases pass under declared capacities |
| Motion | Locked feet stay attached; bodies, tools, slings and parts respect tested clearance; insertion and extraction remain possible with neighboring geometry |
| Structural staging | Required-brace removal and inadmissible concurrent loads are rejected by the intended model |
| Physical ownership | No unsupported handled member, duplicate part, invisible tool transfer or attachment without its verification |
| Planning | Delayed supply and blocked access alter task decisions; progress cannot be created by bypassing a failed check |
| Circularity | Component identities and material masses reconcile through damage, reuse, processing, losses and new input |
| Replay | Seed, event ordering, snapshots and recorded numerical results reproduce the same committed state |
| Browser operation | Pause, step, inspect, follow, change view and replay reach the same state; loading errors are visible |

## Work organization and dependency gates

After the shared contract is stable, three workstreams can run concurrently:

1. **Mechanics:** connector geometry, robot motion, contact solver and frame analysis.
2. **Simulation:** component ledger, event execution, dependencies, resource allocation and recovery.
3. **Experience:** site scene, cameras, controls, inspection, robot/part visual readability and replay.

Integrate at every milestone with one small canonical scenario. The scene may preview future scale while checks are in development, but only completed validation contributes engineering evidence. Asset polish follows mechanical decisions.

The critical dependency is milestone 1 → reversible transaction → staged frame. Scaling and detailed building assets depend on that chain. The ledger, replay, presentation and lifecycle schematic can develop in parallel from milestone 0.

| If this fails | Revise this before proceeding |
|---|---|
| Beam cannot enter and later leave with neighboring parts installed | Connector opening, adapter, insertion sequence or member subdivision |
| Robot has no feasible stance or plausible capacity envelope | Dock layout, limb/body proportions, load sharing or handling method |
| Workfront cannot carry construction loads | Bracing, temporary support, member capacity or growth sequence |
| Hoist reach or access blocks completion | Equipment placement, added lifting capacity, relocation sequence or building layout |
| Routine fault needs an unavailable rescue action | Recovery resources and their access, or the declared autonomy boundary |
| Recovered kit cannot form configuration B | Second layout, explicit supplemental stock or compatibility assumptions |
| More robots do not meet the target duration | Measured limiting process: delivery, lifting, connection cycle, workfront or reliability |

## First implementation batch

Begin with milestone 0 and the two milestone-1 benches. The first batch should deliver:

1. A runnable Three.js test site and headless scenario runner.
2. Shared schemas, component IDs, explicit support states and replay fixtures.
3. A procedural four-limbed robot, docking rail/corner and tool dock.
4. Two adjustable connector concepts with an incoming beam and visible lifting support.
5. Numerical harness smoke tests plus initial reach, collision and required-load results.
6. A short decision record selecting or rejecting the initial geometry, with the next constraint to solve.

At that point we will have a concrete mechanism to inspect and measured software bottlenecks from which to estimate subsequent effort. The final acceptance remains the large, autonomous, circular building demonstration; the small benches supply its repeatable foundation.
