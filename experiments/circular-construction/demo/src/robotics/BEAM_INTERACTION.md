# Beam-side guide contact: active-floor interface candidate

`beamInteraction.ts` is a transferable local geometry screen, independent of
animation, scenario approval, force allocation and the building model. The
waypoints contain explicit beam-centre and robot-wrist positions. The body and
three supporting wrists/anchors remain fixed. Every sampled tool tip comes
from the wrist plus a finite tool axis, shaft and spherical pad. A nominated
contact must coincide with a real face of a named beam solid, with a pad-radius
margin from its edges. A gap cannot generate a contact wrench.

## Candidate geometry

The existing member is 3.0 m overall, including its end shoes. Its central
2.86 × 0.146 × 0.254 m solid has a +20 mm local Z offset. The 180 × 130 × 90 mm
shoes enter upward-open seats, whose floors are at Z=3.20 m and whose cheeks
reach Z=3.31 m. This is the existing box member, **not a rolled I-section**;
an I-section redesign must nominate an actual flange/web face and update its
collision solids. Do not apply a box-face contact to the empty space between
flanges.

For a beam centre at [1.5,0,3.327] m, use the near side of the central body at
[0.25,-0.073,3.360] and [2.75,-0.073,3.360] m. These points lie inboard of the
seat cheeks and 50 mm above them. The tool is a 12 mm-radius shaft extending
130 mm from wrist to a 25 mm-radius spherical guide pad. Its axis points +Y.
The corresponding wrists are [0.25,-0.228,3.360] and
[2.75,-0.228,3.360] m. A freely rotating spherical/roller head could reduce
scrubbing during lowering; its bearing, compliance, sensing and fabrication
are design requirements, not modeled hardware qualification.

The tests validate each end independently, including a straight 222 mm wrist
approach from Y=-0.45 m and a coupled side-contact follow over the final
120 mm of vertical lowering. The low robot body is at Z=2.25 m and
Y=-0.68 m. A rigid translation to an active floor 54 m higher preserves these
local geometric results; it does not qualify that floor or its rail supports.
Independent end checks do not establish inter-robot clearance or synchronized
control. Neither robot can pull the beam toward itself with this pad.

## Concrete conflicts and co-design changes

- The old wrist [0,-0.25,3.0] does not reach this physical contact. It is a
  standoff pose and must not receive a beam load in a force model.
- Moving the same pad to a shoe side at Z=3.245 m drives it through the front
  seat cheek. Use the higher, inboard body-side contact; keep the cheek in
  the collision model.
- Following the entire 450 mm descent from the clear beam height exceeds the
  current robot reach envelope. Have the hoist place the beam into the final
  120 mm local guide region before the robot establishes contact, or design
  and validate a higher stance/longer robot. No body climb under contact is
  inferred here.
- Keeping the +Y tool orientation while departing the generic body dock
  produces tool/forearm collision. The passing short approach starts at an
  explicit precontact pose; a path from that dock to the precontact pose is
  **not verified**. Design a rotating wrist and tool-orientation trajectory,
  or a forward-facing exchange station. Do not move the tool directly from
  dock to the passing pose in a viewer and label it validated.

## Geometry and wrench contract

`screenBeamInteraction()` checks at a default maximum 10 mm translational
step, including both beam and wrist movement. It tests robot IK/joint limits,
robot self collision, supplied boxes, beam versus robot, shaft/pad versus beam,
tool versus fixtures and other limbs, and tool versus torso. A short portion
of the tool's own forearm adjoining the wrist is excluded from tool/forearm
collision: 1.05 × (link radius + shaft radius), 60.9 mm with default values.
This represents an intentional wrist coupling, not a general self-collision
exemption. The current robot model does not solve wrist orientation limits.
The sphere/box penetration check uses closest-point distance; capsule/box
checks are conservative expanded-box tests. These are sampled checks, not a
continuous collision proof. There is no allowance for deflection or
manufacturing/placement uncertainty beyond the explicit contact tolerance.

The positive tests supply posts, heads, longitudinal members and both open-seat
floor/cheek pairs. They do not claim comprehensive active-floor geometry:
rail/anchor mating interfaces, braces, hoist, slings, nearby robots, decking,
workers, and placed closures must be added with their real contact/collision
semantics in the detailed scene. Beam/seat insertion clearance remains the
separate connector screen; this module does not test beam against fixtures.

Only a successful complete path returns a `contactWrenches` record. Forces on
beam and tool are equal and opposite **at the same physical surface point**,
with zero free couple. `atWrist` transfers the on-tool wrench with
`(contactPoint - wrist) × force`. The test's 80 N is a prescribed compression
demand, not an optimized, capacity-approved or observed force. The module
always returns `forceAndHost.status = 'unverified'`. A frictionless side pad
has one force direction; it supplies neither vertical lift nor arbitrary
six-axis restraint. Two same-side pads still need hoist/connection reactions
to balance lateral demands.

For a detailed MuJoCo trajectory, instantiate finite shaft/pad and member
collision geometry, model the actual wrist orientation and coupler, and
export contact point, force, body references and time. Carry the equal and
opposite robot reactions through explicitly modeled rail anchors into the
OpenSeesPy active-stage model. Rendering the contact points or applying
numerical forces alone is not evidence that the mechanism reached them.

Run `npx vitest run src/robotics/beamInteraction.test.ts`.
