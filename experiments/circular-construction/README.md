# Autonomous circular construction experiment

Opened 30 September 2026; classified as an experiment on 1 October 2026. This is a speculative engineering experiment that applies Ren's theories and values. It is not a theory, a canonical formulation, or an extension of the theory corpus. Its design choices, assumptions, simulations and results belong to this experiment. Findings may inform later theoretical discussion, but must not be incorporated into canonical theory without a separate explicit decision.

The linked theories remain the intellectual foundation. This folder contains an assistant-authored engineering proposal, evidence review and working demonstration; it is not Ren's verbatim writing or a validated building design.

**The promising route is to design the steel kit, climbing robots, and construction process together.** The frame can provide the robots with access, known grasp locations, positioning references, and temporary fixtures. Climbing material carriers deliver components up the growing frame to four-limbed assemblers; optional lifting equipment must be assembled and recovered by robots if the selected kit needs it. Reversible connections and a return-and-inspection yard make the same system capable of maintaining, dismantling, and recomposing what it builds.

The literature establishes important pieces of this architecture. It does not yet establish the proposed integration: a large inhabited steel building erected autonomously in days and recovered almost completely. The purpose of the demonstration is to expose and test the missing links.

## Research record

| File | Purpose |
|---|---|
| [Evidence](evidence.md) | Primary sources, what each establishes, and limits on transferring its result |
| [Earlier demonstration specification](demonstration.md) | Original lifecycle and mechanics requirements; its product order and default hoist route are superseded |
| [Current implementation plan](demo/IMPLEMENTATION-PLAN.md) | Controlling plan: empty land, arriving robots, loaded climbing carriers, swarm construction, complete building and fleet departure |
| [Original build plan](build-plan.md) | Earlier exploratory plan, retained for research history; its mechanism-first sequence, mandatory hoist, provisional geometry and tools are superseded |
| [Calculation script](feasibility.py) | Reproducible mass, handling moment, throughput, reliability, and material-retention sensitivities |
| [Calculated results](results.json) | Inputs, provenance, computed bounds, and limitations |

Current status: a [20-storey 3D demonstrator](demo/README.md) now combines editable Blender site and robot models, MuJoCo workcell dynamics, OpenSeesPy construction-stage frame studies, and a Three.js viewer. It demonstrates a seated beam and guarded hoist release; the joint remains unfastened. A separate full-storey climb with 48 measured grip advances and an isolated one-ended mounted-pin proof exist, but neither is integrated into a complete beam transaction. A [planned architectural model](demo/architecture.html) shows the future completed appearance without claiming it was physically built. A [29-task autonomy specification](demo/production/autonomy/README.md) names the machines and custody needed from fabrication through recovery; it is not an execution trace. A [geometry-derived throughput screen](demo/production/planning/README.md) finds that the earlier one-crane concept does not substantiate a days-scale whole-building schedule. The calculation script below remains a sensitivity model, not a construction simulation.

**Current direction — 1 October 2026:** the next main deliverable is the entire continuous construction process. Begin on empty flat land, show robots arriving with tools and materials, build foundations and the first stable frame, then show a swarm of climbing carriers and construction robots completing the 20-storey building. Include roof, enclosure, specified systems, temporary-equipment recovery and the last machine’s departure. Develop detailed dynamics within that same scene. The existing local experiments support it; they do not replace it.

## The values become engineering requirements

Ren's [original material direction](../../worldbuilding/archive/004-ren-regenerative-materials.txt) already connects public knowledge, robot-assembled steel buildings, reuse, and freedom to transform resources across successive uses. The [material foundation](../../worldbuilding/foundations/regenerative-material-civilization.md) develops that direction; the [architecture exploration](../../theories/architecture-for-a-living-earth/README.md) supplies an earlier lifecycle proposal. These establish intellectual provenance, not technical proof. This independent study inherits neither a particular city nor an architectural aesthetic.

| Commitment | Consequence for the demonstration |
|---|---|
| Generativity preserves the means for further life and change | Assemble one useful configuration, dismantle it, inspect the parts, and construct a different configuration from identified recovered members |
| Resources retain value across uses | Preserve complete members first; distinguish repair, qualified reuse, remanufacturing, stored rejects, and actual losses |
| Public knowledge supports shared capability | Keep geometry, interfaces, assumptions, constraints, and failure records in readable, portable data |
| Freedom includes continuity | Allow maintenance and selective replacement as well as complete transformation; repeated rebuilding is not the objective |
| Powerful automation can meet a finite need | Give the planner a requested program and stock budget, then stop when it is complete; speed is a legitimate hypothesis, not a value violation |
| Regeneration concerns living systems too | Account for construction disturbance and site recovery separately from metal recovery; neither metric substitutes for the other |

**Scenario assumptions:** abundant inexpensive energy, expensive material resources, automated manufacturing and transport available to support the site. Energy availability does not set robot torque, payload, reliability, wind tolerance, logistics capacity, or recovery yield. Those remain explicit engineering inputs. Low energy price also does not by itself establish low environmental impact; lifecycle accounting needs the energy source and process inputs.

## What existing work makes credible

NASA's ARMADAS demonstrated three robots assembling a shed-scale lattice from hundreds of composite modules in slightly over 100 operating hours. This supports the strategy of co-designing components and specialized robotic roles. It is a controlled lightweight assembly result. [NASA demonstration](https://www.nasa.gov/general/robot-team-builds-high-performance-digital-structure-for-nasa/)

Four-limb climbing is physically demonstrated. SCALER's loaded vertical trial carried 3.4 kg at 0.16 m/min on a prepared rail. That is useful evidence for locomotion and grasping, and also illustrates why climbing payload and speed cannot be inferred from a robot's ground performance. [SCALER, section VI B2](https://arxiv.org/html/2312.04856v2)

Designing steelwork for reuse has a substantial engineering basis: accessible bolted joints, compatible component families, identification, and planning for separation. The missing contribution is to turn those requirements into a robot-compatible building system with verified temporary states. [SCI P449](https://www.steelconstruction.info/images/0/0d/SCI_P449.pdf), [ECCS PROGRESS](https://www.steelconstruct.com/wp-content/uploads/PROGRESS-D3.1-Design-for-reuse.pdf)

## Proposed construction system

### A family of structural parts with common interfaces

Use beams or hollow sections, columns, removable braces, and floor cassettes with accessible connection adapters. Steel need not be solid bar: section shape matters for mass and stiffness. Common interfaces should accommodate different member capacities; a lower-storey column and a roof brace cannot be assumed interchangeable merely because their endpoints fit.

Start with ordinary inspectable structural fasteners and purpose-designed capture hardware. Factory-welded end fittings can remain part of a reusable member. Repeated destructive welding between site modules would obstruct the intended reuse cycle.

Three functions must remain distinct:

1. **Alignment:** lead-in surfaces and controlled adjustment help a delivered member reach the connection geometry.
2. **Capture:** a positive temporary seat or latch carries defined loads while alignment and fastening proceed.
3. **Final connection:** the verified structural joint carries its intended forces with the required stiffness.

A captured beam is not automatically a completed beam. A latch cannot be rendered as load-bearing unless its load path and capacity exist in the model. One-sided tool access or captive nuts reduce the need for an extra manipulator, but the chosen details need connection testing; a convenient invented connector is not already qualified structural hardware.

Add replaceable robot docking collars or rails. Their attachment loads still enter the steel frame. Keep them accessible after services, fire protection, and enclosure are installed, or deliberately retain another maintenance route.

### Four interchangeable limbs with explicit work and travel modes

The preferred research robot has four articulated arm/legs, positive locking grippers, force sensing, joint brakes, and a tool interface. Its body and limb proportions remain parameters until reach and loads are tested. A six-degree-of-freedom limb is a useful starting kinematic hypothesis, not a selected actuator design.

During a conservative climbing gait, one limb moves while three remain attached. During work, three anchor the robot while the fourth guides a supported member or operates a tool. To walk again, the free limb must put away its tool, attach, and let another limb move. The simulation must show this transition.

**Three contacts are not a stability proof.** Their geometry, force and moment limits, joint torques, load offsets, and the unfinished frame's deformation matter. Three force-only grasps along one line cannot resist every applied moment. Keyed clamps may transmit moments, but several rigidly fixed limbs can also fight one another when geometry is imperfect. Force sensing and controlled compliance belong in the design.

Structural bays and climbing strides are different scales. A 3–6 m bay needs intermediate grips, rails, or truss geometry within limb reach. Rail installation and removal are construction tasks with their own mass, time, and access needs.

### Carry material up the growing frame

The preferred route uses arriving ground carriers, climbing material carriers and construction robots. Ground manipulators establish the first stable frame. Assemblers climb to supported work positions; carriers secure a part, climb and traverse to a reserved delivery point, overlap support with the receiver, retain the part through connection and stage acceptance, then release and return. This complete cycle must be visible for repeated material deliveries.

Choose component size, payload cradles, rail/grip interfaces and robot capacities together. Smaller reusable members or team carrying may be needed. A lift, hoist or crane is a conditional alternative for a selected load, with its own visible arrival, robot assembly, support verification, extension, operation, dismantling and departure. There is no assumed prebuilt lifting plant.

Payload moments remain a design constraint. British Steel lists UB 254 × 146 × 31 at 31.1 kg/m. A 6 m piece weighs **186.6 kg** before fittings. Holding it horizontally at one end requires about **5.49 kN·m** of gravitational moment at that support, before dynamics. This is a handling example, not a section sized for our building. Carrier cradles, load orientation, member subdivision and shared support need analysis against the actual robot model. [Manufacturer table](https://www.britishsteel.co.uk/wp-content/uploads/2025/07/british-steel-product-brochure-14012025-compressed-1.pdf); calculations in [feasibility.py](feasibility.py).

### Grow from a stable and reachable frontier

The first robot cannot climb a frame that does not exist. Ground machinery establishes foundations, anchors, temporary works, and a braced seed. The climbing team extends this structure through checked intermediate states.

A connected rectangular frame can still sway as a mechanism. The erection sequence needs appropriate bracing and restraint before robots or new members load it. Floors count as diaphragms only when their designed connections are effective. Cladding changes temporary wind loading. Existing steel practice explicitly recognizes the need to retain erection supports until replacement restraint is established. [AISC 303-22, section 7.10](https://www.aisc.org/globalassets/aisc/publications/standards/a303-22w.pdf)

Construction decisions must preserve all three: structural adequacy, a route for incoming components, and a route out for the machines. The planner is allowed to reject an attractive geometry that cannot be assembled or dismantled.

## Alternatives to compare

Climbing delivery is the preferred concept. Compare these kit choices against its payload, reach, access and joint requirements; any required lifting plant adds its entire assembly and recovery process:

| Architecture | Advantage to investigate | Cost that the model must expose |
|---|---|---|
| Many short bars forming larger trusses | Lower handling mass per piece; potentially more work done entirely by climbers | More joints, inspections and robot moves; accumulated tolerances; truss depth and access |
| Larger frame members with lifting support | Fewer major placements; climbers concentrate on connections | Hoist capacity, reactions, wind sensitivity, shared delivery paths and handoffs |
| Large prefabricated cassettes or modules | Fewer site operations; controlled factory assembly | Heavier lifts, transport envelope, factory work, and potentially less fine-grained recomposition |

Compare these for the same useful space and load requirements, including component and temporary-work mass. A small repeated voxel may simplify robotics while using too many joints or too much material at building scale. A large module may shorten the site clock by moving work upstream. The study should count both effects.

## Can it build a large structure in days

**Possibly within a defined scope and sufficiently capable system; current evidence does not establish the proposed rate.** The meaningful question is what a specified building requires, where the bottleneck lies, and which assumptions must improve to meet a target.

Separate manufacturing, site preparation, structural erection, enclosure, services, commissioning, and occupancy readiness. A frame erection clock cannot silently stand for the whole building process.

For an illustrative batch of member placements, let:

- `N` be placements, with both end connections included in each complete operation;
- `t` be minutes per operation for one assembly cell;
- `C` be independent assembly cells, each with its required robots;
- `u` be their effective utilization;
- `m` be average member mass;
- `Qparts` and `Qmass` be delivery capacities;
- `Tcritical` be the duration forced by dependencies.

Then a resource lower bound in hours is:

`T ≥ max(N × t / (60 × C × u), N / Qparts, N × m / Qmass, Tcritical)`

This is not a schedule. Capacity can remain idle because the right workfront is unavailable; queueing, shared hoist occupancy, precedence, and startup/tail effects can make completion longer. A detailed model must count node preparation, braces, rail extension, tool changes, inspection, temporary works, panel handling, and recovery. If utilization already absorbs a class of delays, do not also add the same delays separately.

The included sensitivity assumes **10,000 placements**, **12 minutes each**, **two climbers per cell**, **65% utilization**, **100 kg average member mass**, **100 members/hour delivery**, **5 tonnes/hour mass delivery**, and an assumed **72-hour critical path**. None of these operational assumptions is a measured future-robot specification or a bill of materials for a real building.

| Assembly cells | Climbing robots | Work capacity bound | Overall resource bound |
|---:|---:|---:|---:|
| 10 | 20 | 307.7 hours | 307.7 hours, 12.8 continuous days |
| 20 | 40 | 153.8 hours | 200 hours, 8.3 continuous days |
| 40 | 80 | 76.9 hours | 200 hours, 8.3 continuous days |

The 1,000-tonne assumed material batch takes at least 200 hours through the 5 t/h supply route. Doubling the fleet no longer helps. With delivery increased to 20 t/h and 200 members/h, 40 cells have a 76.9-hour bound; 48 cells reach the assumed 72-hour critical-path floor. Those results identify demands on the infrastructure. They do not demonstrate three-day construction.

Reliability also scales with operation count. If each of 10,000 operations independently has a 0.1% chance of an unresolved event, the expected count is ten and the probability of none is about 0.0045%. At 0.01%, the expected count is one and the probability of none is about 36.8%. These are mathematical sensitivities, not measured failure rates; correlated failures may be worse. Recovery must be a core autonomous capability, and the event definition must distinguish automatically resolved retries from failures requiring outside help.

## Circularity must include the whole building

The demonstration should trace each component through `stock → transport → installed → removed → inspected → qualified reuse / repair / reprocessing / quarantine`. Keep material in the stock ledger even while it is waiting for a next use. Being placed in a recycling bin is not the same as returning qualified material to production.

| Layer | Research direction | Remaining issue |
|---|---|---|
| Steel frame | Reversible member connections, accessible inspection, qualified second use | Fatigue, corrosion, connection wear, dimensional changes, and the demands of the next structure |
| Floors | Mechanically connected replaceable cassettes with separate diaphragm ties | Strength, vibration, acoustics, fire performance, lifting weight, and separability of layers |
| Facade and roof | Mechanically retained panels with replaceable seals | Weathering, damaged glass, coatings, insulation, and seal consumption |
| Services | Accessible detachable routes and replaceable modules | Commissioning, leakage, electrical testing, electronics, and compatibility |
| Foundations | Site-specific removable or reusable systems where feasible | Soil, installation disturbance, load capacity, corrosion, and incomplete removal |
| Hardware and temporary works | Captive parts, counted inventories, replaceable wear components | Fastener reuse restrictions, damaged tools, slings, grip pads, batteries, and rail recovery |

Full-scale demountable floor experiments show this layer is a real research subject, including assembly tolerances; their particular connections cannot be assumed to be a universal dry solution. [Delft floor study](https://research.tudelft.nl/files/110957617/G_rbacea_et_al_2019_ce_papers.pdf)

Steel can return to structural use through an appropriate recovery and qualification route. Damage does not imply that reheating or forging alone restores a certified member. Sorting, chemistry, refining, forming, heat treatment where required, and testing determine what comes back. Copper contamination is one reason remelting is not equivalent to perfect purification. [JRC circularity briefing](https://publications.jrc.ec.europa.eu/repository/bitstream/JRC142660/JRC142660_01.pdf)

Show direct reuse, qualified repaired output, recycling feedstock, actual recycled output, retained inventory, new inputs, and losses separately. Do not choose a near-100% recovery number to fit the premise. Even a hypothetical 99% retention per complete cycle leaves only 36.6% of the original stock after 100 cycles without replenishment; 99.9% leaves 90.5%. This simple sensitivity explains why small losses matter over the long horizon.

Material continuity and ecological regeneration need separate evidence. A steel recovery ledger cannot establish restored soil, habitat, hydrology, or biodiversity. Include the footprint and final site state in the visual lifecycle, and describe ecological outcomes as unmeasured until a site model exists.

## The next implementation milestone

**Show the whole empty-site-to-completed-building sequence**, with concurrent robots and materials that can be followed from arrival through loaded climbing, supported handoff, installation and carrier return. Include ground bootstrap, roof and specified systems, temporary-work recovery, final inspection and fleet departure. Use the [controlling plan](demo/IMPLEMENTATION-PLAN.md) for implementation order and acceptance.

Develop the site task runner, Blender assets, loaded carrying and assembly mechanics, and continuous Three.js experience together. Clearly distinguish provisional planning motion from physically verified actions. Existing beam and connector benches help improve actions within this same sequence; they are no longer prerequisites to developing the whole demonstration. Once construction works end to end, extend the same history through inspection, supported dismantling, recovery and recomposition.

The central invention is a **reversible construction system whose material interfaces make robotic action easier and whose planning preserves the ability to change it again**. Three.js can make its operation intelligible. The engineering case comes from the constraints, tests, and evidence behind what it displays.
