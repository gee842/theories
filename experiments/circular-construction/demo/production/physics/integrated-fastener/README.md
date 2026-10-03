# Isolated mounted-pin prototype: narrow sequence demonstrated

**A modified robot-mounted tool now inserts a free pin, departs, and leaves the pin retaining a 2 kN axial proof load in this isolated concept model.** This is not a complete building connection or a validated real machine. The original canonical tool still cannot reach the lug; the mounted experiment adds an offset/longer-stroke pusher, contact-supported magazine, and removable receiving stop. Canonical MJCF, connector prototype, Blender, and browser files are unchanged.

From `demo`:

```sh
numerical/.venv/bin/python production/physics/integrated-fastener/test_incremental.py
```

The test regenerates actual dynamics traces and validation reports. MuJoCo 3.14.0 is used. `approach.py` reuses the canonical simulator in memory, changing only tool target to its existing 350 mm limit, enabling its capsule collision, and accumulating signed actuator mechanical work each simulation step. It records the source SHA256. The existing rail-lock equalities, articulated raise, sling dynamics, and actual two-seat gate remain. `free_pin.py` imports connector geometry and replaces the pin's world axial slide with a free joint, removes its insertion actuator, and initializes it **already inserted**. Neither script overwrites moving poses during integration or adds a fastening equality. The canonical crane mocap remains prescribed in the approach experiment only.

## Access experiment

The real two-seat load/velocity dwell gate releases the hoist at 15.828 s. Final seat reactions are about 3132 N each. The bounded tool motor performs 3.571 J signed mechanical work during its approach; the tool capsule has collision enabled but reaches no fastening geometry. Its centerline endpoint at maximum 350 mm extension is `(6.117012, -12, 43.560894)` in Z-up metres. Proposed connector geometry from the isolated prototype implies:

| Target | Z-up location / correction |
|---|---|
| Beam lug center | `(6.215, -11.915, 43.5375)` |
| Accessible inserted pin-head rear-face center | `(6.148, -11.915, 43.5375)` |
| Endpoint to pin-head center | `(+30.988, +85, -23.394)` mm |
| Endpoint-to-head-center distance | 93.448 mm |

These are **centerline alignment requirements**, not a claim that the capsule's outer surface has the same separation. The capsule radius is 35 mm; the pin head has 36 mm lateral half-width. Even the lateral envelopes remain separated by 14 mm at this pose. The robot provides no Y/Z tool joints. A centerline pusher would require approximately 381 mm extension, 85 mm lateral travel/fixture offset, and −23.4 mm vertical correction at the measured pose. Changing extension alone cannot solve this.

The approach MJCF deliberately retains the canonical beam without the proposed lug: target positions are analytical references, not hidden physical fastening contacts. The prototype lug, full endplate, bracket, cartridge and pusher have not been integrated. Chassis/rail collision and ideal clamp-lock limitations remain canonical limitations. The missed-seat control retains hoist support, never approaches, and ends with zero seat load. Every approach report records `completeFastenedCycle: false`.

## Free-pin load-path increment

The pre-inserted pin now has all six rigid-body degrees of freedom. It has no world guide, axial actuator, cartridge, or equality constraint. Both spring-loaded dogs are real articulated children of the free pin. The beam is also a six-DOF free body, seats are frictionless, and the 2 kN axial load begins only after actual two-seat reactions and low velocity persist for 0.4 s. The external load is a proof-test fixture force, not robot work.

The first free-pin run exposed unintended slot-rail shoulders: the original rectangular rail corners protruded outside the 12 mm shaft envelope. The isolated redesign recesses rail centers from ±10 to ±7 mm and narrows their lateral half-width from 6 to 4 mm. Their maximum radius is now 9.85 mm. Mass remains the same explicit 10 g per rail; this is a geometric collision correction, not a strength design.

At 0.5 ms, the revised free pin retains 2 kN with 14.030 mm axial beam displacement. Dogs carry 1999.318 N and the head/bracket carries 1999.319 N; slot reaction is zero. At 0.25 ms, displacement is 14.117 mm, dogs carry 2000.507 N, and head/bracket carries 2000.508 N, again with zero slot reaction. Displacement differs by 0.0877 mm and dog reaction by 1.189 N. The limited two-step convergence criterion now passes. Pin sag remains about 11.7 mm under gravity until its shaft reaches the loose bore; it is physically supported by bore contacts. All nominal actuator work remains zero.

The no-latch control holds dogs retracted and loses retention. Its 5 s endpoint is runaway failure after leaving the seats, not a meaningful structural displacement prediction. Regression checks require finite states, zero warnings, nominal penetration below 1 mm, both intended ~2 kN reaction interfaces, zero slot bearing at both timesteps, dog-reaction difference below 2 N, displacement agreement within 1 mm, and no-latch escape. All measurements are stored in validation/trace JSON. `test-results.json` keeps integrated fastening false; only the pre-inserted free-pin load-path convergence is true.

## Mounted contact sequence

`mounted_attempt.py` combines canonical articulated raise, actual two-seat gating, copied connector lugs, and a six-DOF free pin. A robot-mounted channel physically supports the pin head through the raising and receiving phases. A 100 N bounded gate keeps the loose pin from escaping beforehand. The pusher has 500 mm available extension, +85 mm lateral and −23.394 mm vertical mounting offsets, and a 500 N force limit. It advances over 5 s after the measured seat gate. The magazine has its own bounded 500 N withdrawal motor. A 20 kg far-end receiving stop has 5 mm beam clearance, real collision reaction, and a bounded 2 kN lateral withdrawal motor. These are proposed mechanism components, absent from the canonical model.

The initial square cylindrical nose generated a 104.9 kN transient at the beam bore during insertion. The revised 6 mm spherical lead-in keeps the same forward extent and slower insertion removes that impact. Without a receiver, the now-smoother insertion instead pushes the frictionless beam 153–170 mm and never clears the dogs. A downward-retracting receiver was also rejected because it collided with the seat and continued carrying the proof load. The final receiver withdraws 600 mm sideways, clear of both beam and seat. None of these failures was removed by changing solver limits or prescribed pin poses.

At 0.5 / 0.25 ms timestep:

| Measurement | 0.5 ms | 0.25 ms |
|---|---:|---:|
| Actual two-seat release | 15.828 s | 15.827 s |
| Dog-clear event | 22.7485 s | 22.6960 s |
| Final beam axial slack | 14.0662 mm | 14.0686 mm |
| Dog/beam axial reaction | 2000.302 N | 1999.770 N |
| Head/bracket axial reaction | 2000.302 N | 1999.770 N |
| Receiver reaction during proof | 0 N | 0 N |
| Tool/pin contact during proof | 0 N | 0 N |
| Maximum penetration, any contact | 0.685 mm | 0.732 mm |
| Peak mechanism contact | 7.666 kN | 9.101 kN |

The final ~2 kN load path is beam lug → deployed dogs → free pin → head → fixed support lug. There is no pin world guide or fastening equality. Four ideal rail-clamp equalities remain for the articulated robot. Both seats are explicitly frictionless, preventing friction mixing from concealing retention. The magazine, pusher, and temporary stop are absent from the retained load path. Pusher signed motor work is 25.503 / 25.439 J; magazine work is 50.349 / 50.775 J; receiving-stop work is 8.313 / 8.320 J. Hoist carrier motion remains prescribed, as in canonical physics.

The largest remaining mechanism contact is a **proof-load slack-take-up impact at a dog**, not an insertion-nose jam. Its peak changes ~18.7% with timestep, while final beam displacement differs only 0.00243 mm and final dog reaction by 0.531 N. Thus final axial retention passes the limited comparison; transient peak forces are not fully converged or a strength assessment. The 10 kN test ceiling is a regression envelope, not an allowable load or safety rating.

The missing-latch fault injection holds dogs retracted, withdraws tooling and receiver, and demonstrates loss of retention. Its free pin falls and beam eventually leaves the seats under the proof challenge; later free-fall positions/penetrations are failure evidence only. It is deliberately not a safe production policy. The missing-stop control demonstrates that the dogs never clear and proof is inhibited. It does **not** detect the missing stop before beginning an insertion attempt; an active force/position abort gate remains required. The release condition currently checks one dog's rear face; both final deployed dog positions/contact behavior must be considered when hardening the controller.

Run the mounted cases and check their saved evidence:

```sh
numerical/.venv/bin/python production/physics/integrated-fastener/mounted_attempt.py
numerical/.venv/bin/python -c "import sys; sys.path.insert(0,'production/physics/integrated-fastener'); import mounted_attempt as m; m.run(timestep=.00025); m.run('missing-stop')"
numerical/.venv/bin/python production/physics/integrated-fastener/check_mounted.py
```

`mounted-test-results.json` marks only `integratedPrototypeSequencePassed`; complete construction certification remains false. Contact traces include named interfaces, signed world forces, motor work, pin/beam/tool/magazine/stop positions and proof load. Every per-run summary continues to mark `completeRobotFasteningCycle: false` to prevent conflation with a full reusable autonomous construction cycle. The model needs collision-complete chassis/rails, full endplates and bracket attachment geometry, active failed-insertion recovery, multi-axis loads, force-limited slack take-up, material strength, and physical validation before canonical/browser completion claims can change.
