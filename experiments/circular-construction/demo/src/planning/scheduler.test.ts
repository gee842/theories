import { describe, expect, it } from 'vitest';
import { createTwoByTwoFrameGraph } from './frameExample';
import { scheduleTasks } from './scheduler';
import type { PlanningTask, TaskGraph } from './types';

function cloneGraph(graph: TaskGraph): TaskGraph {
  return structuredClone(graph);
}

function smallTask(id: string, workfrontId: string,
  predecessors: string[] = [], leaseIds: string[] = []): PlanningTask {
  return {
    id, workfrontId, kind: 'ground-seed', predecessors, leaseIds, durationS: 1,
    parts: [], resources: [], mechanicalStatus: 'unverified', description: id,
  };
}

describe('deterministic construction task scheduler', () => {
  it('plans the two-storey frame and accounts for held lifting resources and throughput', () => {
    const graph = createTwoByTwoFrameGraph();
    const result = scheduleTasks(graph);
    expect(result.status).toBe('complete');
    expect(result.diagnostics).toEqual([]);
    expect(result.tasks).toHaveLength(graph.tasks.length);
    expect(result.tasks.filter(row => row.taskId.startsWith('place-'))).toHaveLength(8);
    expect(result.tasks.filter(row => row.taskId.startsWith('brace-'))).toHaveLength(8);
    expect(result.tasks.filter(row => row.taskId.startsWith('rail-'))).toHaveLength(8);
    expect(result.tasks.filter(row => row.taskId.startsWith('recover-'))).toHaveLength(1);
    expect(result.tasks.every(row => row.status === 'planned'
      && row.mechanicalStatus === 'unverified')).toBe(true);
    for (const row of result.tasks) {
      expect(Object.values(row.waitByReasonS).reduce((sum, value) => sum + value, 0))
        .toBe(row.queueWaitS);
    }

    const place = result.tasks.find(row => row.taskId === 'place-s1-x0-y0')!;
    const release = result.tasks.find(row => row.taskId === 'release-s1-x0-y0')!;
    const hoistLease = result.reservations.find(interval => interval.ownerId === 'lift-s1-x0-y0'
      && interval.resourceId === 'hoist-1')!;
    expect(hoistLease.startS).toBe(place.startS);
    expect(hoistLease.endS).toBe(release.endS);
    for (const resourceId of new Set(result.reservations.map(interval => interval.resourceId))) {
      const intervals = result.reservations.filter(interval => interval.resourceId === resourceId)
        .sort((a, b) => a.startS - b.startS);
      for (let i = 1; i < intervals.length; i++)
        expect(intervals[i].startS).toBeGreaterThanOrEqual(intervals[i - 1].endS);
    }

    const report = result.report!;
    expect(report.precedenceCriticalPathS).toBeLessThanOrEqual(report.resourceLimitedMakespanS);
    expect(report.resourceLimitedMakespanS).toBeLessThan(report.serialDurationS);
    expect(report.resourcePenaltyOverPrecedenceS).toBeGreaterThan(0);
    expect(report.totalReadyQueueWaitS).toBeGreaterThan(0);
    expect(report.peakReadyQueue).toBeGreaterThan(0);
    expect(report.peakParallelTasks).toBe(2);
    for (const front of report.workfronts) {
      expect(front.busySlotS + front.idleSlotS)
        .toBe(report.resourceLimitedMakespanS * front.capacity);
      expect(Object.values(front.idleByReasonS).reduce((sum, value) => sum + value, 0))
        .toBe(front.idleSlotS);
    }
    for (const resource of report.resources) {
      expect(resource.busyUnitS + resource.idleUnitS)
        .toBe(report.resourceLimitedMakespanS * resource.units);
    }
  });

  it('has identical results when input arrays are reordered', () => {
    const graph = createTwoByTwoFrameGraph();
    const reordered = {
      ...graph,
      tasks: [...graph.tasks].reverse(),
      resources: [...graph.resources].reverse(),
      parts: [...graph.parts].reverse(),
      leases: [...graph.leases].reverse(),
      workfronts: [...graph.workfronts].reverse(),
    };
    expect(scheduleTasks(reordered)).toEqual(scheduleTasks(graph));
  });

  it('rejects an unavailable hoist before scheduling', () => {
    const graph = cloneGraph(createTwoByTwoFrameGraph());
    graph.resources = graph.resources.filter(unit => unit.kind !== 'hoist');
    const result = scheduleTasks(graph);
    expect(result.status).toBe('impossible');
    expect(result.report).toBeNull();
    expect(result.diagnostics).toContainEqual(expect.objectContaining({
      code: 'unavailable-resource', referenceId: 'hoist',
    }));
  });

  it('assigns interchangeable hoist leases concurrently when two fronts can use them', () => {
    const graph: TaskGraph = {
      id: 'parallel-lifts', assumptions: ['Synthetic resource capacity comparison.'],
      workfronts: [{ id: 'a', capacity: 1 }, { id: 'b', capacity: 1 }],
      resources: [{ id: 'hoist-1', kind: 'hoist' }], parts: [],
      tasks: [
        { ...smallTask('a-start', 'a'), durationS: 10 },
        smallTask('a-end', 'a', ['a-start'], ['a-lift']),
        { ...smallTask('b-start', 'b'), durationS: 10 },
        smallTask('b-end', 'b', ['b-start'], ['b-lift']),
      ],
      leases: [
        { id: 'a-lift', startTaskId: 'a-start', endTaskId: 'a-end',
          resources: [{ kind: 'hoist' }] },
        { id: 'b-lift', startTaskId: 'b-start', endTaskId: 'b-end',
          resources: [{ kind: 'hoist' }] },
      ],
    };
    const one = scheduleTasks(graph);
    const two = scheduleTasks({ ...graph, resources: [...graph.resources,
      { id: 'hoist-2', kind: 'hoist' }] });
    expect(one.status).toBe('complete');
    expect(two.status).toBe('complete');
    expect(one.report?.resourceLimitedMakespanS).toBe(22);
    expect(two.report?.resourceLimitedMakespanS).toBe(11);
    expect(two.reservations.filter(item => item.ownerKind === 'lease')
      .map(item => item.resourceId).sort()).toEqual(['hoist-1', 'hoist-2']);
  });

  it('shows the frame fixture sensitivity to a second interchangeable hoist', () => {
    const one = scheduleTasks(createTwoByTwoFrameGraph({ hoistCount: 1 }));
    const two = scheduleTasks(createTwoByTwoFrameGraph({ hoistCount: 2 }));
    expect(one.status).toBe('complete');
    expect(two.status).toBe('complete');
    expect(one.report?.resourceLimitedMakespanS).toBe(19_080);
    expect(two.report?.resourceLimitedMakespanS).toBe(17_520);
    expect(two.report!.resources.find(row => row.kind === 'hoist')?.units).toBe(2);
  });

  it('rejects a member placement whose brace predecessor is missing', () => {
    const graph = cloneGraph(createTwoByTwoFrameGraph());
    graph.tasks = graph.tasks.map(task => task.id === 'place-s1-x0-y0'
      ? { ...task, predecessors: task.predecessors.filter(id => id !== 'brace-s1-x0-y0') }
      : task);
    const result = scheduleTasks(graph);
    expect(result.status).toBe('impossible');
    expect(result.diagnostics).toContainEqual(expect.objectContaining({
      code: 'missing-safety-gate', taskId: 'place-s1-x0-y0',
      referenceId: 'brace-s1-x0-y0',
    }));
  });

  it('reports a bounded resource deadlock between two held leases', () => {
    const graph: TaskGraph = {
      id: 'lease-deadlock', assumptions: ['Synthetic resource deadlock.'],
      workfronts: [{ id: 'a', capacity: 1 }, { id: 'b', capacity: 1 }],
      resources: [
        { id: 'hoist', kind: 'hoist' },
        { id: 'zone', kind: 'approach-zone' },
      ],
      parts: [],
      tasks: [
        smallTask('a-start', 'a'),
        smallTask('b-start', 'b'),
        { ...smallTask('a-end', 'a', ['a-start'], ['a-lease']),
          resources: [{ kind: 'approach-zone' }] },
        { ...smallTask('b-end', 'b', ['b-start'], ['b-lease']),
          resources: [{ kind: 'hoist' }] },
      ],
      leases: [
        { id: 'a-lease', startTaskId: 'a-start', endTaskId: 'a-end',
          resources: [{ kind: 'hoist' }] },
        { id: 'b-lease', startTaskId: 'b-start', endTaskId: 'b-end',
          resources: [{ kind: 'approach-zone' }] },
      ],
    };
    const result = scheduleTasks(graph);
    expect(result.status).toBe('blocked');
    expect(result.diagnostics.filter(item => item.code === 'deadlock')).toHaveLength(2);
    expect(result.tasks.filter(row => row.status === 'blocked')).toHaveLength(2);
    expect(result.report).toBeNull();
  });

  it('enforces a caller-supplied event bound', () => {
    const result = scheduleTasks(createTwoByTwoFrameGraph(), { maxTransitions: 1 });
    expect(result.status).toBe('blocked');
    expect(result.diagnostics).toContainEqual(expect.objectContaining({ code: 'transition-limit' }));
  });
});
