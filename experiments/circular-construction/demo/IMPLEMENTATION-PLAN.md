# Implementation plan: empty land to a complete building

Revised 1 October 2026 following Ren's explicit correction. This is the controlling plan for the Blender, MuJoCo, OpenSeesPy and Three.js demonstration. It replaces the previous connector-first implementation order and the mandatory crane logistics concept. The [earlier research plan](../build-plan.md) and existing mechanism studies remain background material.

**Classification:** an applied experiment under `experiments/circular-construction/`. The theories guide its values and design questions; the implementation, engineering hypotheses and findings do not constitute theory or modify the canonical theory documents.

## The demonstration we are building

One continuous, realistic, inspectable 3D scene begins with **empty flat land**. A group of autonomous robots arrives carrying construction materials and tools. They prepare the ground, establish foundations, assemble the first stable frame from ground level, climb what they have built and extend it. Material-carrying robots travel up the growing frame and hand components to construction robots. Several robots work concurrently across the structure. Floors, circulation, roof, enclosure and the specified building systems follow. Temporary equipment is recovered, the robots descend and depart, and a complete building remains.

The full demonstration target remains **20 storeys**. The current carrier-oriented candidate is an 18 × 12 m footprint, 3 m bays and 3.2 m storeys, with an initial fleet of eight carriers, four assemblers, two ground builders and four cargo rovers. These are design variables, not qualified capacities or a fixed fleet requirement. The earlier 36 × 24 m crane/workcell design is a separate study. The kit, spans, robot geometry and payloads must be designed together around material transport by climbing robots. The intended architecture remains a desirable inhabited building with pale expressed framing, recessed glazing, shaded terraces, warm soffits and planting.

Success is judged first by watching an empty site become a finished building and being able to follow how the robots did it. An already erected tower containing a beam-placement experiment does not meet that requirement. Separate connector and climbing experiments are supporting engineering work, not the main deliverable.

## What the viewer must show

| Sequence | Visible action | State that permits the next action |
|---|---|---|
| 1. Empty site and arrival | Bare terrain; mobile robots and secured cargo enter from a visible site boundary. No installed foundations, racks, rails, crane or tower exist at time zero. | Arriving machines park, identify their cargo and establish working space. |
| 2. Deploy and prepare | Robots unload their own tools and temporary supplies, survey the site, prepare access and deploy service equipment. | Ground and access assumptions are declared; bootstrap machines have support and energy. |
| 3. Foundations | Ground machines visibly install the selected foundation and base-connection system, handle material and account for spoil or residual work. | Each required base and anchor is accepted for its next construction load. Flat terrain does not imply adequate soil. |
| 4. First stable structure | Ground manipulators hold and join the first columns, beams and braces, using reachable poses and visible temporary restraints. | A stable initial bay and usable climbing interfaces exist before a robot mounts them. |
| 5. First loaded climb | A carrier receives and secures a component, approaches the frame, engages its grips and climbs the structure that was just assembled. | The route exists, remains stable under the robot and payload, and has an available delivery position. |
| 6. Handoff and installation | A construction robot receives the component while the carrier retains support; robots orient, seat, connect and verify it before the carrier releases. | A measured receiving load path permits custody transfer. The carrier can return or take another task. |
| 7. Swarm growth | Multiple carriers travel, wait, hand off and return while assemblers add members, braces and access interfaces at several eligible work locations. | Dependencies, route reservations, temporary stability and combined robot loads permit parallel work. |
| 8. Complete the building | Robots install floor and roof cassettes, core/circulation components, facade, terraces and specified services and finish modules. | Installation and inspection tasks complete without closing remaining material or robot access routes prematurely. |
| 9. Clear the site | Robots inspect, remove temporary braces where permitted, descend, recover rails and tools, pack service equipment and leave. Final closures, removed supports and ground finishes are inspected before the last inspection/service equipment and ground machine depart. | No machine is stranded; no temporary structure or unexplained construction prop remains. |

Every installed component must have a visible origin, carrying or lifting action, handoff and installation. Whole floors must not appear by visibility switches. Fast playback advances the same event history; it must not skip the work that creates the building.

At representative working moments, the whole-site camera must show different concurrent jobs: incoming transport, loaded ascent, assembly, empty return and supported waiting. Follow one persistent beam and one carrier through their complete histories, then return to the whole-site view without changing the world or its clock. This is the visual acceptance review for every milestone, including milestones focused on a local mechanism.

The incoming supply boundary represents factory-produced robots and qualified material. Factory manufacture can be inspected as an upstream process but is not the opening scene. Mobile robots may arrive assembled and charged. Any site-specific infrastructure they need must be brought, deployed, assembled and recovered visibly.

## Carrier robots are the default material route

Use ground carriers for incoming cargo and four-limb climbing carriers for vertical delivery. Construction robots visibly attach from the ground, climb into supported assembly positions, reposition as work advances and receive parts. Their routes, carried tools and eventual descent are part of the same fleet history. A common robot chassis with interchangeable payload cradle and assembly tooling is worth evaluating, but the roles may require different machines. Four limbs are the starting concept; useful payload, reach, grip capacity and access decide the final mechanism.

The defining repeated cycle is:

**retrieve → secure payload → approach frame → attach → climb → traverse → rendezvous → overlap support → install and verify → release carrier → return or accept another task.**

A carrier must actually carry its cargo through this path. The assembler does not summon a beam from the supply yard. A loaded carrier is a new dynamics problem; the existing unloaded climb does not establish payload capacity. Check payload mass and center of mass, torque and grip forces, collision clearance, wind exposure, acceleration, braking, passage around joints, floor transitions and return energy.

Start by defining a material and handling catalogue. Each component needs its mass, dimensions, grip/lift interfaces, installation orientation, robot or team assignment, temporary supports, connection actions and reverse handling route. Smaller steel members, reusable truss subassemblies and lighter floor/enclosure cassettes may be necessary. Existing 638.6 kg beams and roughly 8–10 tonne core-panel concepts are not automatically assigned to climbing robots. If multiple robots share a payload, model their coupling and coordination rather than dividing the mass arithmetically.

A lift, hoist or crane is an **optional engineered branch**, used only where the selected kit and carrier approach require it. Its cargo arrival, unloading, foundation or support, robot assembly, commissioning, extension, material transfers, dismantling and departure all belong in the same scene and schedule. Equipment cannot depend on itself to erect its own first support. No permanently pre-positioned tower crane is assumed.

## First implementation milestone: the complete construction sequence

The next main deliverable is a runnable end-to-end site demonstration that starts with empty terrain and ends with the completed building and departed fleet. Develop its full sequence immediately. Do not postpone arrival, foundations, fleet behavior, enclosure or egress until a standalone fastener benchmark is finished.

This milestone combines four coordinated workstreams:

1. **Site state and task execution.** Generate the complete building bill of materials and tasks, including arrival, bootstrap, temporary works, repeated material trips, installation, enclosure and departure. Give each part, robot, tool and support a persistent identity. Tasks consume actual inventory and update the erected structure; they cannot install an object merely because a timer expired.
2. **Robot and building assets.** Use editable Blender models for the transport robots, climbing carriers, assemblers, payload attachments, interchangeable tools, foundation equipment and modular building kit. Local joints, pivots and contact interfaces come from shared dimensional data used by the physics models. Show actual grasping and articulation rather than rigid bodies sliding along arbitrary splines.
3. **Loaded climbing and handoff mechanics.** Make a representative ground pickup, payload climb, transfer, installation and empty return work in one compatible robot/part model. Apply the existing climbing and connector research to these actions. Resolve support and reach problems where the full process exposes them; do not make a second disconnected mechanism viewer the delivery milestone.
4. **Continuous Three.js experience.** Render the same site state and task history from first arrival to final departure. Provide whole-site, follow-carrier, follow-assembler and connection cameras, pause, scrub and playback speed. Begin with the empty site; a planned final model is an optional reference overlay, never an erected load path.

Early development runs may contain explicitly provisional motion and engineering assumptions. They still need coherent part ownership, reachable assembly order and visible material paths. Label such runs as planned construction sequences, not solved dynamics. The physics, contact and structural evidence is progressively attached to the corresponding actions in this same scene. Increasing engineering fidelity must not replace the whole process with isolated experiments.

**Milestone acceptance:** replay from time zero reaches the complete defined building with every required installation and departure accounted for; several robots work concurrently; a selected part can be followed from arrival to installation; a selected carrier completes a loaded ascent, handoff and return; no visible result is created by teleportation, untracked inventory or an unexplained prebuilt support.

## Engineering hardening of the same demonstration

These are parallel improvements to the end-to-end deliverable, not a return to the old connector-first product order.

### Bootstrap and access

Select and model a foundation method appropriate to the stated site assumptions. Reversible piles, anchors or reusable foundation modules are candidates requiring ground and capacity analysis, not established solutions for this tower. Give arriving ground machines the reach and support needed to build the first bay. Temporary braces and fixtures must be installed before they are needed.

Design how a robot transfers from ground travel to frame attachment, how the first climbing interfaces are attached, and how each new receiver or rail is delivered and fitted from already supported geometry. Prefer usable interfaces integrated into reusable structural members where feasible. If separate rails are necessary, include their mass, installation, obstruction and recovery. Preserve a route for the last robot to get down.

### Loaded climbing, traffic and handoffs

Unify the robot geometry across carrying, climbing and assembly. Simulate joint limits, masses, actuators, payload restraints, finite grip geometry, contact and interference with adjacent steel and installed panels. A three-grip stance is not automatically stable; solve the required forces and moments.

Reserve routes and staging positions. Loaded ascent, empty descent, passing or waiting positions, delivery docks and recovery routes share finite space. The scheduler must resolve opposing traffic and blocked workfronts without deadlock. Fleet size follows useful concurrency and congestion measurements, not visual multiplication.

At a handoff, both machines may support the component. The receiving robot, temporary fixture or completed connection must carry the required load before the sender releases. Failed capture, missing latch or occupied destination keeps the part supported and triggers a retry, return or supported stop. Visible waiting and recovery are part of the swarm behavior.

### Structural assembly and enclosure

Analyze the structure at meaningful erection stages, including partial bays, temporary restraints, robot and payload loads and simultaneous work. Only accepted connections and effective bracing contribute the claimed stiffness. Frame deformation must be checked against gripping and mating tolerances.

Use reversible structural connections with reachable tooling and a removal path. Investigate insertion, retention, slip, preload where relevant, load reversal and extraction as part of installation tasks. Existing one-pin axial evidence does not qualify a whole joint. Keep unsupported physical claims out of the structural results.

The complete-building catalogue includes foundations, frame, braces, floors, roof, circulation/core, enclosure, facade weather closure, terraces, declared service and interior modules, and ground restoration/landscape. Define this bill before completion logic. Omitted fit-out or system performance must remain explicitly outside the claimed completed scope; a finished-looking facade alone is not commissioning. Cladding and interior closure must preserve carrier, tool and machine escape access until those tasks are done.

Resolve circulation as actual geometry and construction tasks: ground-floor deck, entrance, continuous stairs, floor openings, landings, edge framing, guards and unobstructed headroom. Placing a stair mesh through a solid floor does not satisfy circulation. Reserve the stair bay before generating floor cassettes and beams; include every replacement header and landing support in the material catalogue, delivery history and structural model. Coordinate the access plan with doors, facade closure, service routes and maintenance access.

Bracing must work in both principal directions and under load reversal, including incomplete erection stages. If structural analysis requires additional braces, larger members or revised connections, those changes must appear in Blender, the inventory and installation sequence before their stiffness is credited. Solver convergence alone does not establish member, connection or foundation capacity.

### Service, faults and completion

Robots arrive with enough energy for bootstrap and deploy mobile service before recurring work. Model charging or battery exchange, tool exchange, consumables, equipment downtime and inspection as scheduled actions. Cheap energy does not imply unlimited battery storage, motor power or zero service time.

Removed temporary parts remain visible inventory through packing and departure. A part must move from its installed location to a supported receiver, a transport restraint and an outgoing vehicle; hiding it after removal is not recovery. Permanent maintenance rails may remain only when they are explicitly part of the finished building and counted as such.

Exercise a delayed delivery, blocked climbing route, failed grasp and failed connection within the same site run. Check that the visible fleet replans or remains supported. Completion requires the roof and declared building systems, inspection tasks, temporary-work removal, all machines' descent and packed departure. Construction-machine egress and later building deconstruction are separate phases.

## Simulation and rendering architecture

The site model owns the persistent bill of materials, component condition, robot state, custody, accepted structure, workfronts, traffic reservations and task dependencies. The planner selects possible work from that current state.

Blender supplies editable geometry, materials, rigged joints and named interfaces. MuJoCo supplies detailed articulated/contact dynamics for loaded locomotion, handoffs and assembly; Mink may generate targets where useful, with success decided by actuator and contact results. OpenSeesPy evaluates growing structural stages and loads. Three.js shows the resulting site, robot poses and task history with continuous camera movement.

Use a shared SI geometry contract and stable body/component names across engines. Record the model and load revision behind each physical result. A completed task commits inventory and structure changes only against its appropriate execution evidence. Clearly distinguish a task executed by the current planning/motion model from an action physically verified within a stated load and geometry envelope.

Detailed contact simulation can focus on active work areas. The rest of the site still has explicit robot tasks, trajectories, payloads, supports and occupancy. Reusable solved motions require matching geometry, payload, support and boundary conditions; changing scale, route, orientation or load requires renewed analysis. Camera selection must not change the simulated history or upgrade an assumption into evidence.

The interface should emphasize the construction itself. Concise state cues explain what a selected robot is carrying, where it is going, why it is waiting and who currently supports a part. Engineering detail is inspectable without covering the main view in diagnostics. Show task progress and material movements instead of a decorative building-growth percentage.

## Throughput and regenerative values

The site clock includes arrival, foundations, bootstrap, every carrier trip, assembly, rails, temporary works, service stops, enclosure, inspection and departure. Report simulated duration and playback speed separately. Compare fleet size, payload, member size and route capacity through reproducible runs. Construction in days remains a hypothesis until the full scope fits the measured clock.

The earlier one-crane estimate of roughly 32–53 days for assumed lifts is background evidence about that earlier architecture, not a forecast for climbing-carrier construction. Recompute the handling catalogue and schedule for the selected new kit. Do not reuse the old lift count as carrier-trip count.

Design disassembly and reuse into the part kit from the start: accessible reversible connections, persistent material identity, recoverable temporary equipment and explicit site residuals. After the continuous build demonstration works, add its second act: inspection, supported dismantling, sorting, repair where needed and a different composition from recovered components. Prefer direct qualified reuse before remanufacture or remelt; account for losses and site restoration. Recycling statistics must not substitute for watching robots carry out construction or recovery.

## Delivery milestones and acceptance

These milestones are an integration order. Asset work, robotics and structure proceed in parallel and feed the same demonstration. A narrow numerical success does not complete a milestone whose visible construction actions are missing.

| Milestone | Concrete deliverable | Acceptance before it is called complete |
|---|---|---|
| A. Coherent whole-site construction | The main entry shows the full 20-storey planned sequence using editable Blender assets, persistent parts and a concurrent fleet. | Empty first frame; visible arrivals and ground bootstrap; no carried-part jumps; repeated loaded delivery and empty return; roof, enclosure and usable circulation; packed temporary equipment and last-machine departure. Follow cameras and seeking preserve identity and state. This establishes a planning demonstration, not physical feasibility. |
| B. One integrated carrier transaction | A compatible machine and real kit member execute pickup, payload restraint, ground-to-frame attachment, loaded ascent, supported delivery, installation and empty return inside the main sequence. | Finite grip geometry and actuator limits, actual payload inertia, collision clearance, continuous support and explicit receiving loads. A failed grip or capture retains support. Any remaining authored segment is identified and prevents a claim that the whole transaction is physically solved. |
| C. Complete kit and architectural access | Every required component has geometry, mass, interfaces, an assembly/removal method and a robot or team that can handle it. | Actual columns, beams, braces, floor/roof panels, stairs, facade and service modules each have a supported route. Heavy parts are redesigned or assigned a demonstrated team/device; no assumed 350 kg rating. Stair openings, entrance, landings, guards, headroom and robot escape routes exist in the assembled geometry. |
| D. Stable growth and adaptive swarm | The runtime dispatches eligible work from the current structure, inventory and reservations; structural checks cover concurrent loads and partial stages. | Routes and grips only use installed, accepted geometry. Opposing traffic, occupied receivers, delayed cargo, a blocked route and failed connection cause waiting, recovery or replanning. Bracing, joints and foundations support the claimed stages; stale results cannot authorize changed geometry. A precomputed successful timeline alone does not establish autonomy. |
| E. Whole-building completion and throughput | Construction, service stops, inspection, closures, equipment recovery and departure form one measured schedule. | Declared building systems have actual installation and inspection tasks. Remaining performance/commissioning exclusions are explicit. No construction equipment is stranded or disappears; finite transport, energy and workfront capacity explain the duration. Report frame time and finished-scope time separately. |
| F. Recovery and second composition | Extend the same world history through supported dismantling, inspection, sorting and a visibly different building made from recovered parts. | Reverse operations preserve stability and last-robot escape. Direct reuse retains component identity; repair, reprocessing, new inputs, losses and residual site work are accounted for. Recycling feedstock is not counted as qualified recovered output. |

The full-site experience remains available throughout B–F. Every review starts with the whole process, then follows the action improved in that iteration. Milestone F is part of the intended regenerative demonstration; it is sequenced after a coherent construction run, not removed from scope.

## Current baseline and next work

As of this revision, `index.html` opens the new [construction runtime and viewer](src/construction/runtime.ts). It contains an end-to-end authored task/motion sequence and the carrier-oriented [Blender libraries](production/blender/CARRIER-ASSETS.md). The earlier level-12 experiment is retained at `workcell.html`. This is progress toward milestone A, not acceptance of all its criteria or a solved autonomous construction system.

The current planned sequence includes loaded arrivals, persistent cargo through transfers, a slower guided beam-delivery cycle, actual stair openings and delivered supports, a ground entrance, and visible packing and outgoing transport of temporary equipment. These are implemented planning and geometric results. They do not establish autonomous dispatch, physical handling or acceptance of milestone A as a whole.

The [loaded-carrier experiment](production/physics/carrier/README.md) raises a 92.928 kg beam through one 3.2 m storey under bounded motor torques, using ideal grip constraints. A separate [finite-jaw experiment](production/physics/carrier/FINITE-GRIP.md) sustains a loaded hold; a complete accepted loaded climbing, ground transition and handoff cycle remains outstanding. The column-mass ballast case fails the first capture; the proposed 350 kg envelope therefore remains a design target. New contact work must retain both successful and failed runs rather than replace a failing physical model with prescribed motion.

The structural model now derives its members from the visible inventory, including the stair openings and support members. Its current lateral probes expose inadequate baseline bracing under load reversal. Revised bracing must be delivered and installed in the scene before it can be counted in the accepted structural model.

Immediate integrated work, in priority order:

1. **Make the bootstrap mechanically coherent.** Follow the arriving equipment through unloading, foundation installation, temporary restraint and the first stable bay. Correct pile driving so joined segments advance together, rather than placing separate segments directly at final depth. Resolve ground-builder reach, supported first-column placement and the first ground-to-frame attachment. Preserve and inspect the implemented cargo continuity, stairs, entrance and packed recovery throughout this work.
2. **Resolve finite-contact loaded travel and receiving.** Extend the loaded hold to controlled unloading of one grip, clearance around the real rail brackets, advance, recapture and measured load acceptance. Then establish repeated ascent, horizontal access and descent with the actual jaw geometry. Join pickup, payload restraint, ground attachment and receiving actions to the same machine. Rework payload size and cradle geometry when torque, grip or clearance results require it; a closed jaw alone does not prove a load-bearing capture.
3. **Make kit changes propagate everywhere.** Reconcile bracing in both axes, member/connection demands and partial-stage support with the visible components. Evaluate smaller or split heavy members together with their added splices, robot access and delivery cost. Do not claim the lighter part works until its actual geometry is evaluated.
4. **Replace assumed dispatch and support with runtime decisions.** Add payload-specific traversals, reservations for shared interior paths and docks, supported handoff/fastening, service actions and fault recovery. The scene remains the delivery target; local benches produce evidence for these named actions.
5. **Re-run the full construction and recovery scope.** Recompute the bill and schedule after design changes, inspect the complete guided replay and freely selectable views, then extend to dismantling and recomposition. The current slow loaded-travel assumption produces a schedule on the order of 100 days; that is a planning diagnostic, not a forecast or a days-scale success.

### Next visible review

Review the main scene from empty terrain through the first two storeys at normal inspection speed, then continue the same history to the twentieth storey, finishing and departure. The close-up must show arriving cargo being unloaded, the ground-built stable bay, a carrier mounting it with a secured member, assembly robots taking supported positions, a loaded delivery and receiving operation, and the carrier returning. The whole-site view must show concurrent useful work during this sequence.

This review is a concrete implementation checkpoint within milestone A and the start of B, not a smaller replacement for the full building. Any action still driven by authored motion remains identified as such. Acceptance depends on the visible process and the engineering evidence for each claimed physical action; additional dashboards, mechanism-only scenes or regression counts cannot substitute for either.

Use GPT-6.1 Sol for most implementation and integration; retain Astra for architecture, complex robotics, key 3D modeling and modular design as directed. Keep module ownership explicit so the shared contract, physics, assets and runtime cannot quietly diverge.

The [architecture](ARCHITECTURE.md) and [autonomous process specification](production/autonomy/README.md) support this plan; [STATUS.md](STATUS.md) records the narrower evidence that actually exists. The previous tower, pin and crane studies remain supporting references and do not determine the main experience or completion criteria.
