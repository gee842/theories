# Reversible beam connector geometry bench

This is a **geometric screening example**, in metres with Z up. It does not
qualify a connection, latch, fastener, robot, hoist, frame or transfer of load.
`runOpenSeatBench()` screens one 3.0 m overall member with two narrowed end
shoes and two open seats. The shoe/floor contact is intentional; both shoes and
the adjacent beam body are checked against declared manufacturing, alignment and obstacle
allowances. The open seats have 240 mm inside length, 190 mm throat width,
240 mm lead-in mouth and 110 mm lead-in rise. Seat floors are at Z = 3.20 m,
above the declared 3.15 m fixture head tops. The candidate beam centre is
Z = 3.327 m at seating and Z = 3.777 m when clear. Each 80 mm outer-end cap
is placed after seating, with a nominal 20 mm gap above its shoe and an
overhead driver approach. Cap holes, bolt preload and capture strength have
no model here.

`fixtureObstacles()` declares four posts, four solid heads, both longitudinal
rails, four diagonal brace tubes, both bays' work rails and A staging rails,
including their brackets and sockets.
The swept beam, cap-placement, cap-removal and driver-access paths are sampled at no more
than 10 mm pose increments, with fixed beam yaw and translation-only paths.
Non-contact solids use conservative expanded AABB
tests. Brace tubes use centreline intersection against expanded AABBs, which
can reject near-corner paths conservatively. The seat floor and cheeks are
treated as specified contact hardware, screened by their dimensions rather
than as ordinary obstacles. Cap bearing area and bolt geometry are conceptual.
These samples do not prove continuous motion,
robot reach, sling clearance, deflection, forces, fatigue or field tolerance.

The comparison `screenDualClosedSockets()` installs fixed overhead lips before
the same vertical guide. Both shoes collide with those lips. This disproves
that specific straight vertical insertion, not every imaginable assembly
method. A 50 mm Y misalignment and a blocked driver path also fail.

`screenScenarioConnectorMotions()` reads the recorded scenario guide and A
removal waypoints and screens them against both fixture bays. The trace ends
with the beam installed at B, so its B extraction screen reverses the recorded
B guide; that fourth path is a candidate, not a recorded event. The historical
Z = 3.25 m to Z = 3.00 m guide remains as an explicit negative regression test:
it intersects the solid fixture heads. Before committing a `guide` event, pass its
actual beam-centre waypoints, current obstacles, two seat records and
`closureState: 'removed'` to `screenConnectorMotion`. For `lower`, first record
that caps were removed under hoist support and screen the actual extraction
waypoints. Save the result with a geometry/input fingerprint and world revision;
invalidate it when a rail, brace, tool, fixture or pose changes. Keep capture,
fastener inspection and structural stage checks as separate gates.

Run `npx vitest run src/connectors/connectors.test.ts` from `demo/`.
