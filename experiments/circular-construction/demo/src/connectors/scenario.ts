import type { ExecutionEvent } from '../domain/types';
import { createBeamScenario } from '../scenarios/beam';
import { BEAM, ENVELOPE, fixtureObstacles, SAMPLE_STEP, SEATS } from './bench';
import { screenConnectorMotion } from './geometry';
import type { ConnectorMotionScreen, OpenSeat, Vec3 } from './types';

export interface ScenarioConnectorCheck {
  readonly fixture: 'A' | 'B';
  readonly operation: 'guide' | 'lower';
  readonly sourceEventId: string;
  readonly source: 'recorded-event' | 'reverse-of-recorded-guide';
  readonly path: readonly Vec3[];
  readonly result: ConnectorMotionScreen;
}

function pathOf(event: ExecutionEvent): readonly [Vec3, Vec3] {
  if (!event.poseFrom || !event.poseTo) throw new Error(`${event.id} has no beam motion waypoints.`);
  return [event.poseFrom, event.poseTo];
}

function seatsAt(fixture: 'A' | 'B'): OpenSeat[] {
  const shiftY = fixture === 'A' ? 0 : 3;
  return SEATS.map(seat => ({ ...seat, id: `${fixture}:${seat.id}`,
    center: [seat.center[0], seat.center[1] + shiftY, seat.center[2]] }));
}

/** Uses recorded scenario poses. The current trace removes A but ends installed
 * at B, so B extraction is explicitly the reverse of its recorded guide. */
export function screenScenarioConnectorMotions(): readonly ScenarioConnectorCheck[] {
  const events = createBeamScenario().events;
  const guides = events.filter(e => e.action === 'guide');
  const lowerA = events.find(e => e.action === 'lower');
  if (guides.length !== 2 || !lowerA) {
    throw new Error('Expected one recorded guide at each fixture and one recorded A removal.');
  }
  const guideAPath = pathOf(guides[0]);
  const guideBPath = pathOf(guides[1]);
  const lowerAPath = pathOf(lowerA);
  const entries: readonly Omit<ScenarioConnectorCheck, 'result'>[] = [
    { fixture: 'A', operation: 'guide', sourceEventId: guides[0].id,
      source: 'recorded-event', path: guideAPath },
    { fixture: 'A', operation: 'lower', sourceEventId: lowerA.id,
      source: 'recorded-event', path: lowerAPath },
    { fixture: 'B', operation: 'guide', sourceEventId: guides[1].id,
      source: 'recorded-event', path: guideBPath },
    { fixture: 'B', operation: 'lower', sourceEventId: guides[1].id,
      source: 'reverse-of-recorded-guide', path: [guideBPath[1], guideBPath[0]] },
  ];
  const obstacles = fixtureObstacles();
  return entries.map(entry => ({ ...entry,
    result: screenConnectorMotion({ operation: entry.operation, member: BEAM,
      path: entry.path, seats: seatsAt(entry.fixture), obstacles,
      closureState: 'removed', envelope: ENVELOPE, maxSampleStep: SAMPLE_STEP }),
  }));
}
