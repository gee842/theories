# Regenerative construction: 20-storey engineering demonstrator

**Current direction — 1 October 2026:** the [implementation plan](IMPLEMENTATION-PLAN.md) calls for one continuous demonstration from empty flat land to a complete 20-storey building and a departed fleet. Robots arrive with materials, build the first frame from the ground, then carry parts up the frame to a visible construction swarm. Any selected lifting equipment must itself be assembled and removed. The plan defines six delivery milestones, from a coherent whole-site sequence through physical carrier handling, adaptive construction, full completion and regenerative second use.

The main page now opens the **whole-site planned construction sequence**, using the carrier-oriented Blender kit and an initial 18-machine fleet. Its current candidate is 18 × 12 m with twenty 3.2 m storeys. The viewer supports guided playback, phase selection, scrubbing and following a carrier, assembler or part. Its routes, installation actions and support assumptions remain planned motion; the current sequence does not establish solved autonomous construction or the physics of every visible action. Circulation, physical transfers, traffic, service and recovery details are active work under the plan's acceptance criteria.

The earlier level-12 tower experiment remains at `workcell.html`. It replays a MuJoCo workcell simulation with a 638.563 kg beam and OpenSeesPy snapshots of that separate tower. Its beam ends **seated and unfastened**. The newer [loaded carrier study](production/physics/carrier/README.md) uses the current kit but still has ideal grip constraints and is not a verified end-to-end pickup/climb/handoff cycle. The planned architecture page and older mechanism studies remain supporting references.

## Run and inspect

Node 22 and Python 3.11 are used for the current reproducible build:

```sh
npm ci
npm run dev
```

Open the URL printed by Vite. The default page begins on empty terrain; use Play, the phase buttons, timeline and follow cameras to inspect the planned construction. The guided tour slows down and follows one beam carrier through pickup, loaded travel, installation and return; manual camera/selection input takes over. Cargo arrives with the opening fleet, and temporary equipment leaves in tracked rover trips. `workcell.html` preserves the earlier tower experiment; `climb.html` shows its separate one-storey dynamics study; `architecture.html` shows the earlier architectural design; `lab.html` preserves the small mechanism and circularity laboratory. The workcell and climb pages replay saved physics traces. The main construction page currently uses its own planned site history; these evidence scopes must not be conflated.

Reproduce the earlier workcell assets and engineering studies from this directory (the current carrier kit has its own [asset instructions](production/blender/CARRIER-ASSETS.md) and [dynamics instructions](production/physics/carrier/README.md)):

```sh
python3 -m venv numerical/.venv
numerical/.venv/bin/python -m pip install -r numerical/requirements.txt
blender --background --python production/blender/build_assets.py
blender --background --python production/blender/build_climb_assets.py
numerical/.venv/bin/python production/physics/mujoco/simulate.py
numerical/.venv/bin/python production/physics/climb-prototype/prototype.py
node scripts/exportClimbTrace.mjs
numerical/.venv/bin/python production/structure/opensees/analyze.py --public
python3 production/planning/study.py
npm run build
```

Blender 5.2.1 created the editable `.blend` sources and glTF browser assets. The physics and structure source models, exported traces, validation logs, images, and interface code are all in this repository. Rendering the Blender previews can take a few minutes. The installed Blender executable may need an absolute path if `blender` is not on `PATH`.

Run regression checks:

```sh
npm test
npm run verify:production
numerical/.venv/bin/python production/physics/mujoco/test_workcell.py
numerical/.venv/bin/python production/physics/climb-prototype/test_prototype.py
numerical/.venv/bin/python production/physics/connector-prototype/test_prototype.py
numerical/.venv/bin/python -m unittest discover -s production/structure/opensees -p 'test_*.py' -v
python3 production/planning/study.py
node production/autonomy/validate-spec.mjs
numerical/.venv/bin/python production/physics/integrated-fastener/check_mounted.py
```

## Source map

| Source | Role |
|---|---|
| [Construction runtime](src/construction/runtime.ts) and [viewer](src/construction/view.ts) | Current main experience: persistent component missions and fleet tracks from empty site through planned completion and departure. Authored task/motion evidence, not whole-site solved dynamics. |
| [Carrier kit and machines](production/blender/CARRIER-ASSETS.md) | Current 3 m modular kit, editable Blender libraries, articulated carrier/assembler/ground-builder/cargo-rover assets and shared dimensional contract. |
| [Loaded carrier experiment](production/physics/carrier/README.md) | Bounded-torque beam-carrying ascent, missed-grip recovery and payload sensitivities with ideal grip constraints; physical jaw contact and complete transfer remain separate work. |
| [Finite-contact experiment](production/physics/carrier/FINITE-GRIP.md) | Actual opposed-jaw loaded hold; rejected capture/climbing attempts and controller/design revisions remain explicit. No full loaded contact-safe step is claimed. |
| [Carrier-kit structural study](production/structure/carrier/README.md) | Member graph from the main scene's parts, including stair openings and headers. Conditional stage responses expose unresolved brace and connection demands. |
| [Blender generator](production/blender/build_assets.py), [climb generator](production/blender/build_climb_assets.py) and [asset contract](production/blender/ASSETS.txt) | 36 × 24 m, 20-storey site; steel sections, seats, crane, demountable core and floor cassettes, facade, grip rails and robots. The generator also produces the planned 20-storey architectural GLB and editable [Blender design source](production/blender/planned-architecture.blend), with pale framing, planted garden terraces and a landscaped forecourt. These finish parts have no engineering credit or validated lifting inventory. |
| [MuJoCo workcell](production/physics/mujoco/README.md) | Articulated robot, bounded actuators, grip constraints, free I-beam, contact seats, controlled hoist and failure gate. The nominal trace is `public/assets/workcell-trace.json`. |
| [Connector contact prototype](production/physics/connector-prototype/README.md) | Separate physically simulated pin-and-dog insertion, retention, misalignment and pullout study. Its fixed guide and revised tool approach have not been integrated into the active-floor robot. |
| [Fastening integration gate](production/physics/integrated-fastener/README.md) | Finds the original tool misses by 93.4 mm. An isolated revised tool, pin magazine and temporary receiving stop then insert a six-DOF free pin and withdraw before a 2 kN axial proof load. Final dog/head reactions agree across two timesteps; a 7.7–9.1 kN slack-take-up impact, large joint play and single-end scope prevent a completed structural-connection claim. |
| [Full-storey climb prototype](production/physics/climb-prototype/README.md) | Separate 137 kg free-base robot with 0.45 m links makes 48 actual grip advances over 3.6 m under bounded torques; the viewer uses matching Blender assets and its measured trace. Ideal point clamps and collision-disabled links/rails limit the result. |
| [OpenSees stage study](production/structure/opensees/README.md) | 3D elastic beam-column frame snapshots, temporary braces, active beam/robot loads and support sensitivity. Browser export is `public/assets/tower-structure.json`. |
| [Throughput and logistics screen](production/planning/README.md) | Extracts actual Blender part counts and tests explicit full-20-storey lift assumptions against crane time, reach, payload and robot-climb evidence. This is analytical planning, not a simulated schedule. |
| [Autonomous process specification](production/autonomy/README.md) | Defines 29 required machine task families from driverless delivery and foundations to robot assembly, egress and material recovery, with custody and failure holds. The complete chain is specified, not implemented. |
| [Verified toolchain lab](../toolchain-lab/README.md) | Independently checks Blender export, Three.js loading, MuJoCo/Mink bounded-torque dynamics, OpenSeesPy reference behavior and the current production regressions; it does not replace the construction simulations. |
| [Three.js experience](src/experience/README.md) | Loads named glTF assemblies, applies recorded body poses, shows stages and evidence, and moves continuously between site and workcell. |
| [Planned design viewer](architecture.html) | Inspect the modeled future facade, terraces, full-height core and entrance. Its source is `public/assets/planned-architecture.glb`; the page is explicitly separate from physical construction playback. |
| [Earlier mechanism lab](lab.html) | Schematic beam transaction, material ledger, connector and planning studies retained as a separate research tool. |

The beam section, 5.6 m length and density are shared dimensions. OpenSees derives section mass and blocks export if it differs from MuJoCo. The OpenSees model imports measured final MuJoCo seat reactions with a recorded source hash. Blender and MuJoCo are Z-up; glTF and Three.js use `(x, z, −y)` with explicit quaternion conversion.

[STATUS.md](STATUS.md) separates demonstrated behavior from unproven claims. The [current implementation plan](IMPLEMENTATION-PLAN.md) defines the complete construction sequence and acceptance criteria; [ARCHITECTURE.md](ARCHITECTURE.md) explains the simulation and lifecycle design. The broader [research record](../README.md) explains the regenerative values and evidence base.
