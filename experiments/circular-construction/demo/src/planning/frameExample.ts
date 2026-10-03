import { scheduleTasks } from './scheduler';
import type {
  PartRequirement, PlanningPart, PlanningTask, ResourceLease, ResourceRequirement,
  ScheduleResult, TaskGraph,
} from './types';

const defaultRecoveryBay = 's1-x0-y0';

export interface FrameExampleOptions {
  /** Set null for an uninterrupted planning case. Default injects one reseat path. */
  injectedRecoveryBay?: string | null;
  /** Number of interchangeable hoists at the site; defaults to one. */
  hoistCount?: number;
}

/**
 * A 2 × 2 bay, two-storey scheduling fixture. Durations and equipment are assumed
 * for comparison; no operation has a linked motion or structural validator.
 */
export function createTwoByTwoFrameGraph(options: FrameExampleOptions = {}): TaskGraph {
  const recoveryBay = options.injectedRecoveryBay === undefined
    ? defaultRecoveryBay : options.injectedRecoveryBay;
  const hoistCount = options.hoistCount ?? 1;
  if (!Number.isSafeInteger(hoistCount) || hoistCount < 1)
    throw new Error('hoistCount must be a positive integer.');
  const validBayIds = new Set<string>();
  for (let storey = 1; storey <= 2; storey++) {
    for (let x = 0; x < 2; x++) {
      for (let y = 0; y < 2; y++) validBayIds.add(`s${storey}-x${x}-y${y}`);
    }
  }
  if (recoveryBay !== null && !validBayIds.has(recoveryBay))
    throw new Error(`Unknown recovery bay ${recoveryBay}.`);

  const tasks: PlanningTask[] = [];
  const parts: PlanningPart[] = [];
  const leases: ResourceLease[] = [];
  const need = (kind: ResourceRequirement['kind'], resourceId?: string,
    count?: number): ResourceRequirement => ({ kind, resourceId, count });
  const part = (partId: string, typeId: string,
    mode: PartRequirement['mode']): PartRequirement => ({ partId, typeId, mode });
  const task = (entry: Omit<PlanningTask, 'mechanicalStatus'>) =>
    tasks.push({ ...entry, mechanicalStatus: 'unverified' });

  for (const side of ['west', 'east'] as const) {
    parts.push({ id: `seed-kit-${side}`, typeId: 'seed-kit', initialState: 'stock' });
    task({
      id: `seed-${side}`, kind: 'ground-seed', workfrontId: side,
      predecessors: [], durationS: 600,
      parts: [part(`seed-kit-${side}`, 'seed-kit', 'allocate')],
      resources: [need('carrier'), need('robot'), need('tool', 'tool-brace'),
        need('approach-zone', `zone-${side}`)],
      description: `Propose a ground-anchored braced seed at the ${side} workfront.`,
    });
  }

  for (let storey = 1; storey <= 2; storey++) {
    for (let x = 0; x < 2; x++) {
      for (let y = 0; y < 2; y++) {
        const bay = `s${storey}-x${x}-y${y}`;
        const side = x === 0 ? 'west' : 'east';
        const zone = `zone-${side}`;
        const braceId = `brace-${bay}`;
        const railId = `rail-${bay}`;
        const placementId = `place-${bay}`;
        const captureId = `capture-${bay}`;
        const verificationId = `verify-${bay}`;
        const releaseId = `release-${bay}`;
        const leaseId = `lift-${bay}`;
        const bracePartId = `part-brace-${bay}`;
        const railPartId = `part-rail-${bay}`;
        const memberPartId = `part-member-${bay}`;
        parts.push(
          { id: bracePartId, typeId: 'temporary-brace', initialState: 'stock' },
          { id: railPartId, typeId: 'rail-extension', initialState: 'stock' },
          { id: memberPartId, typeId: 'frame-member', initialState: 'stock' },
        );
        const basePredecessor = storey === 1
          ? `seed-${side}` : `release-s${storey - 1}-x${x}-y${y}`;
        task({
          id: braceId, kind: 'brace', workfrontId: side,
          predecessors: [basePredecessor], safetyGateIds: [basePredecessor],
          durationS: 420,
          parts: [part(bracePartId, 'temporary-brace', 'allocate')],
          resources: [need('carrier'), need('robot'), need('tool', 'tool-brace'),
            need('approach-zone', zone)],
          description: `Propose temporary bracing for ${bay}.`,
        });
        task({
          id: railId, kind: 'rail-extension', workfrontId: side,
          predecessors: [basePredecessor], safetyGateIds: [basePredecessor],
          durationS: 300,
          parts: [part(railPartId, 'rail-extension', 'allocate')],
          resources: [need('robot'), need('tool', 'tool-rail'), need('approach-zone', zone)],
          description: `Propose a climbing rail extension for ${bay}.`,
        });
        task({
          id: placementId, kind: 'member-placement', workfrontId: side,
          predecessors: [braceId, railId], safetyGateIds: [braceId, railId],
          durationS: 900,
          parts: [part(memberPartId, 'frame-member', 'allocate')],
          resources: [need('carrier'), need('robot', undefined, 2), need('tool', 'tool-guide')],
          description: `Propose delivery, lift and guided placement of ${memberPartId}.`,
        });
        leases.push({
          id: leaseId, startTaskId: placementId, endTaskId: releaseId,
          resources: [need('hoist'), need('approach-zone', zone)],
        });
        task({
          id: captureId, kind: 'capture', workfrontId: side,
          predecessors: [placementId], leaseIds: [leaseId], durationS: 420,
          parts: [part(memberPartId, 'frame-member', 'reference')],
          resources: [need('robot'), need('tool', 'tool-guide')],
          description: `Propose seat capture and reversible fastening for ${memberPartId}.`,
        });
        task({
          id: verificationId, kind: 'verification', workfrontId: side,
          predecessors: [captureId], leaseIds: [leaseId], durationS: 300,
          parts: [part(memberPartId, 'frame-member', 'reference')],
          resources: [need('robot'), need('tool', 'tool-inspect')],
          description: `Reserve time for geometric and mechanical verification of ${memberPartId}; validator absent.`,
        });
        let releasePredecessor = verificationId;
        if (bay === recoveryBay) {
          const recoveryId = `recover-${bay}`;
          const reverifyId = `reverify-${bay}`;
          task({
            id: recoveryId, kind: 'recovery', workfrontId: side,
            predecessors: [verificationId], leaseIds: [leaseId], durationS: 360,
            parts: [part(memberPartId, 'frame-member', 'reference')],
            resources: [need('robot', undefined, 2), need('tool', 'tool-guide')],
            description: `Injected reseat/regrasp recovery for ${memberPartId}; support lease remains held.`,
          });
          task({
            id: reverifyId, kind: 'verification', workfrontId: side,
            predecessors: [recoveryId], leaseIds: [leaseId], durationS: 300,
            parts: [part(memberPartId, 'frame-member', 'reference')],
            resources: [need('robot'), need('tool', 'tool-inspect')],
            description: `Reserve a repeat verification after recovery for ${memberPartId}; validator absent.`,
          });
          releasePredecessor = reverifyId;
        }
        task({
          id: releaseId, kind: 'release', workfrontId: side,
          predecessors: [releasePredecessor], leaseIds: [leaseId], durationS: 180,
          parts: [part(memberPartId, 'frame-member', 'reference')],
          resources: [need('robot'), need('tool', 'tool-guide')],
          description: `Propose a checked load transfer and hoist/zone release for ${memberPartId}.`,
        });
      }
    }
  }

  return {
    id: `two-by-two-frame-${recoveryBay ?? 'nominal'}-hoists-${hoistCount}`,
    workfronts: [{ id: 'east', capacity: 1 }, { id: 'west', capacity: 1 }],
    resources: [
      ...Array.from({ length: hoistCount }, (_, index) =>
        ({ id: `hoist-${index + 1}`, kind: 'hoist' as const })),
      { id: 'carrier-1', kind: 'carrier' },
      { id: 'robot-1', kind: 'robot' }, { id: 'robot-2', kind: 'robot' },
      { id: 'tool-brace', kind: 'tool' }, { id: 'tool-rail', kind: 'tool' },
      { id: 'tool-guide', kind: 'tool' }, { id: 'tool-inspect', kind: 'tool' },
      { id: 'zone-east', kind: 'approach-zone', workfrontIds: ['east'] },
      { id: 'zone-west', kind: 'approach-zone', workfrontIds: ['west'] },
    ],
    parts, tasks, leases,
    assumptions: [
      'Planning fixture only: all ground, brace, rail, lift, capture, verification, release and recovery operations are mechanically unverified.',
      `Task durations and the ${hoistCount}-hoist, one-carrier, two-robot fleet are assumed scheduling inputs, not measured production rates.`,
      'A workfront and approach zone each admit one operation; the hoist and zone remain reserved from placement through release.',
      'Dependencies express a proposed sequence. Structural stability, robot reach, collision, support transfer and part qualification require linked validators.',
      ...(recoveryBay ? [`An injected capture fault at ${recoveryBay} adds reseating and repeat verification.`] : []),
    ],
  };
}

export function runTwoByTwoFrameExample(options: FrameExampleOptions = {}):
  { graph: TaskGraph; schedule: ScheduleResult } {
  const graph = createTwoByTwoFrameGraph(options);
  return { graph, schedule: scheduleTasks(graph) };
}
