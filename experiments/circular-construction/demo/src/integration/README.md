# Beam task robot projection

`robotTask.ts` compiles the existing beam `SimulationTrace` into deterministic,
time-indexed four-limb poses. It calls the robotics controller for each regrip,
fixed-contact body shift and tool pick/park. A sampled three-grip IK and stance
check covers the tool arm's approach to a point **0.25 m short of each beam end**.
No event's `transaction` check passes: the domain reducer does not store the
mechanical state/check IDs, and beam contact, tool identities, connector stages
and frame reactions have not been coupled.

```ts
import { createRobotTaskTrace, robotTaskAtTime } from './integration/robotTask';

const robotTask = createRobotTaskTrace(trace, { deployment: 'four-robot-bench' });
const frame = robotTaskAtTime(robotTask, clock);
visualA.update(frame.states['climber-1']);
visualB.update(frame.states['climber-2']);
// Add visuals for climber-3 and climber-4 when using the four-robot bench.
// Show frame.activeEvent.localGeometry and .transaction as separate evidence.
```

The default `two-robot` projection deliberately uses only the two robots at A
to test the proposed transfer route; the current `WorldState` also inventories
the pair stationed at B.
Their source positions are exactly the initial domain positions. During the
first 18-second `deliver` interval, each controller makes four 3.6-second grip
steps to new sockets, then a 3.15-second body shift to a work pose. Both robots
move in parallel. Later, a five-second `park-tools` event fits the 3.4-second
parking primitive; the following `retreat` performs the 3.6-second fourth-grip
recapture. At B the original two robots hold at A and every B event's local
geometry is `unverified`, because no A-to-B route exists in the access model.

`four-robot-bench` uses the inventoried robots at fixture B, facing back
toward the fixture from y=3.68 m. Their local grip and tool motion can be
checked through the B task. The coarse domain reducer updates only the pair
assigned to the active fixture, but it does not persist the detailed mechanical
limb states or their check IDs. `supplementalRobotIds` remains available for
scenarios that omit the B pair.

## Required bench geometry

`requiredRobotRails()` gives every assumed rail centerline and z range. Each
fixture end at x=0 and x=3 needs paired keyed socket rails at x=end±0.58 m.
Fixture A needs staging rails at y=0.23 m for the domain seed and work rails at
y=0 m; B needs work rails at y=3 m. The initial A contacts are at z=2.01 and
3.09 m; the checked work contacts are at z=1.71 and 2.79 m. The current site's
small pads have been replaced with paired rails that illustrate these paths.
Rail bracket capacity, clamp orientation, socket tolerance and
reactions into the fixture remain unqualified.

A candidate two-robot transfer would add paired continuous travel rails along
the outboard sides of the x=0 and x=3 longitudinal top members, from y=0 to
y=3, plus a checked corner transfer at each end: front-face work rails to the
outboard travel rails, then travel rails to rear-face B work rails. The transfer
must keep at least three verified grips while changing the body orientation
from yaw 0 to yaw π, clear the diagonal braces and crossmember, and retain a
retreat route. The current controller has no corner/yaw primitive and the
required rail/anchor geometry is not present. Even ignoring both corners,
3 m at the controller's maximum 0.26 m body advance needs 12 cycles: 48 grip
steps × 3.6 s plus 12 body shifts × (0.26/0.12) s ≈ 199 s per robot. The
scenario allows only 130 s from the end of A removal retreat (t=314 s) to the
start of B guide (t=444 s). A two-robot version needs a longer event schedule
or a faster measured mechanism before either corner can be attempted.

The fixture-box collision model includes the visible posts, heads and top
longitudinal members. It omits diagonal braces, the moving beam, sling/cable,
tool body and allowed contact volumes. Those gaps are part of the explicit
`transaction` reasons, not implicit approvals.
