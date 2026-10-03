import type {
  PartRequirement, PlanDiagnostic, PlannedTask, PlanningTask, ReservationInterval,
  ResourceKind, ResourceLease, ResourceRequirement, ResourceUnit, ScheduleOptions,
  ScheduleResult, TaskGraph, ThroughputReport, WaitReason, WorkfrontReport,
} from './types';

type Demand = {
  requirement: ResourceRequirement;
  ownerId: string;
  ownerKind: 'task' | 'lease';
  ordinal: number;
};

type Assignment = { unit: ResourceUnit; demand: Demand };

interface ActiveTask {
  id: string;
  endS: number;
  resourceIds: string[];
  partIds: string[];
}

interface ActiveLease {
  lease: ResourceLease;
  startS: number;
  resourceIds: string[];
}

function byId<T extends { id: string }>(a: T, b: T): number {
  return compareIds(a.id, b.id);
}

/** Code-unit ordering is independent of host locale. */
function compareIds(a: string, b: string): number {
  return a < b ? -1 : a > b ? 1 : 0;
}

function unique(values: readonly string[]): boolean {
  return new Set(values).size === values.length;
}

function isPositiveInteger(value: number): boolean {
  return Number.isSafeInteger(value) && value > 0;
}

function demandSlots(requirements: readonly ResourceRequirement[], ownerId: string,
  ownerKind: 'task' | 'lease'): Demand[] {
  return requirements.flatMap((requirement, index) =>
    Array.from({ length: requirement.count ?? 1 }, (_, slot) => ({
      requirement, ownerId, ownerKind, ordinal: index * 1000 + slot,
    })));
}

/** Exact IDs go first, so a generic request does not consume a needed named unit. */
function assignResources(demands: readonly Demand[], units: readonly ResourceUnit[],
  unavailableIds: ReadonlySet<string>, workfrontId: string):
  { assignments: Assignment[]; missing: ResourceRequirement | null } {
  const sorted = [...demands].sort((a, b) =>
    Number(Boolean(b.requirement.resourceId)) - Number(Boolean(a.requirement.resourceId))
    || compareIds(a.requirement.kind, b.requirement.kind)
    || compareIds(a.requirement.resourceId ?? '', b.requirement.resourceId ?? '')
    || compareIds(a.ownerId, b.ownerId)
    || a.ordinal - b.ordinal);
  const taken = new Set(unavailableIds);
  const assignments: Assignment[] = [];
  for (const demand of sorted) {
    const unit = units.find(candidate => candidate.kind === demand.requirement.kind
      && (!demand.requirement.resourceId || candidate.id === demand.requirement.resourceId)
      && (!candidate.workfrontIds || candidate.workfrontIds.includes(workfrontId))
      && !taken.has(candidate.id));
    if (!unit) return { assignments: [], missing: demand.requirement };
    assignments.push({ unit, demand });
    taken.add(unit.id);
  }
  return { assignments, missing: null };
}

function ancestorsOf(id: string, tasks: ReadonlyMap<string, PlanningTask>,
  cache: Map<string, Set<string>>): Set<string> {
  const cached = cache.get(id);
  if (cached) return cached;
  const ancestors = new Set<string>();
  for (const predecessor of tasks.get(id)?.predecessors ?? []) {
    ancestors.add(predecessor);
    for (const prior of ancestorsOf(predecessor, tasks, cache)) ancestors.add(prior);
  }
  cache.set(id, ancestors);
  return ancestors;
}

function topologicalTasks(tasks: ReadonlyMap<string, PlanningTask>): string[] {
  const successors = new Map<string, string[]>();
  const indegree = new Map<string, number>();
  for (const task of tasks.values()) {
    indegree.set(task.id, task.predecessors.length);
    for (const predecessor of task.predecessors) {
      const next = successors.get(predecessor) ?? [];
      next.push(task.id);
      successors.set(predecessor, next);
    }
  }
  const ready = [...indegree].filter(([, count]) => count === 0).map(([id]) => id).sort();
  const ordered: string[] = [];
  while (ready.length) {
    const id = ready.shift()!;
    ordered.push(id);
    for (const successor of successors.get(id) ?? []) {
      const count = indegree.get(successor)! - 1;
      indegree.set(successor, count);
      if (count === 0) {
        ready.push(successor);
        ready.sort();
      }
    }
  }
  return ordered;
}

interface ValidatedGraph {
  tasks: Map<string, PlanningTask>;
  leases: Map<string, ResourceLease>;
  orderedTaskIds: string[];
  diagnostics: PlanDiagnostic[];
}

function validateGraph(graph: TaskGraph): ValidatedGraph {
  const diagnostics: PlanDiagnostic[] = [];
  const tasks = new Map(graph.tasks.map(task => [task.id, task]));
  const leases = new Map(graph.leases.map(lease => [lease.id, lease]));
  const workfronts = new Map(graph.workfronts.map(front => [front.id, front]));
  const resources = new Map(graph.resources.map(unit => [unit.id, unit]));
  const parts = new Map(graph.parts.map(part => [part.id, part]));
  const error = (code: PlanDiagnostic['code'], message: string,
    taskId?: string, referenceId?: string) => diagnostics.push({ code, message, taskId, referenceId });
  if (!graph.id.trim()) error('invalid-input', 'Graph ID is empty.');
  if (graph.workfronts.length === 0)
    error('invalid-input', 'At least one workfront is required.');
  if (graph.tasks.reduce((sum, task) => sum + task.durationS, 0) > Number.MAX_SAFE_INTEGER)
    error('invalid-input', 'Total task duration exceeds safe integer simulation time.');
  for (const [name, entries] of [
    ['task', graph.tasks], ['lease', graph.leases], ['workfront', graph.workfronts],
    ['resource', graph.resources], ['part', graph.parts],
  ] as const) {
    const ids = entries.map(entry => entry.id);
    if (!unique(ids)) error('duplicate-id', `Duplicate ${name} ID.`);
    if (ids.some(id => !id.trim())) error('invalid-input', `Empty ${name} ID.`);
  }
  for (const front of graph.workfronts) {
    if (!isPositiveInteger(front.capacity))
      error('invalid-input', `Workfront ${front.id} capacity must be a positive integer.`, undefined, front.id);
  }
  for (const unit of graph.resources) {
    for (const frontId of unit.workfrontIds ?? []) {
      if (!workfronts.has(frontId))
        error('unknown-reference', `Resource ${unit.id} names unknown workfront ${frontId}.`, undefined, frontId);
    }
  }
  const checkRequirements = (requirements: readonly ResourceRequirement[], ownerId: string) => {
    for (const requirement of requirements) {
      if (!isPositiveInteger(requirement.count ?? 1)
        || (requirement.resourceId && (requirement.count ?? 1) !== 1))
        error('invalid-input', `Invalid resource count for ${ownerId}.`, ownerId);
      if (requirement.resourceId && resources.get(requirement.resourceId)?.kind !== requirement.kind)
        error('unavailable-resource', `${ownerId} requires unavailable or mismatched ${requirement.resourceId}.`,
          ownerId, requirement.resourceId);
    }
  };
  for (const task of graph.tasks) {
    if (!workfronts.has(task.workfrontId))
      error('unknown-reference', `Task ${task.id} has unknown workfront ${task.workfrontId}.`, task.id, task.workfrontId);
    if (!isPositiveInteger(task.durationS))
      error('invalid-input', `Task ${task.id} duration must be a positive integer second.`, task.id);
    if (task.mechanicalStatus !== 'unverified')
      error('invalid-input', `Task ${task.id} has unsupported mechanical status.`, task.id);
    if (!unique(task.predecessors) || !unique(task.safetyGateIds ?? [])
      || !unique(task.leaseIds ?? []))
      error('duplicate-id', `Task ${task.id} has repeated dependencies, gates or leases.`, task.id);
    for (const predecessor of task.predecessors) {
      if (!tasks.has(predecessor))
        error('unknown-reference', `Task ${task.id} names unknown predecessor ${predecessor}.`, task.id, predecessor);
    }
    for (const need of task.parts) {
      const part = parts.get(need.partId);
      if (!part || part.typeId !== need.typeId)
        error('unknown-reference', `Task ${task.id} requires missing or mismatched part ${need.partId}.`,
          task.id, need.partId);
    }
    if (!unique(task.parts.map(need => need.partId)))
      error('duplicate-id', `Task ${task.id} repeats a part requirement.`, task.id);
    checkRequirements(task.resources, task.id);
  }
  for (const lease of graph.leases) {
    if (!tasks.has(lease.startTaskId) || !tasks.has(lease.endTaskId))
      error('unknown-reference', `Lease ${lease.id} names an unknown endpoint.`, undefined, lease.id);
    if (lease.startTaskId === lease.endTaskId)
      error('invalid-input', `Lease ${lease.id} must span distinct tasks.`, undefined, lease.id);
    if (lease.resources.length === 0)
      error('invalid-input', `Lease ${lease.id} has no resources.`, undefined, lease.id);
    checkRequirements(lease.resources, lease.id);
  }
  if (diagnostics.length) return { tasks, leases, orderedTaskIds: [], diagnostics };

  const orderedTaskIds = topologicalTasks(tasks);
  if (orderedTaskIds.length !== tasks.size) {
    error('dependency-cycle', 'Task predecessors contain a cycle.');
    return { tasks, leases, orderedTaskIds: [], diagnostics };
  }
  const ancestorCache = new Map<string, Set<string>>();
  const allocations = new Map<string, string[]>();
  for (const task of graph.tasks) {
    const ancestors = ancestorsOf(task.id, tasks, ancestorCache);
    for (const gateId of task.safetyGateIds ?? []) {
      if (!ancestors.has(gateId))
        error('missing-safety-gate', `Task ${task.id} lacks required predecessor gate ${gateId}.`, task.id, gateId);
    }
    for (const need of task.parts) {
      if (need.mode === 'allocate') {
        const owners = allocations.get(need.partId) ?? [];
        owners.push(task.id);
        allocations.set(need.partId, owners);
      }
    }
    for (const leaseId of task.leaseIds ?? []) {
      const lease = leases.get(leaseId);
      if (!lease) {
        error('unknown-reference', `Task ${task.id} names unknown lease ${leaseId}.`, task.id, leaseId);
      } else if (!ancestors.has(lease.startTaskId)
        || (task.id !== lease.endTaskId
          && !ancestorsOf(lease.endTaskId, tasks, ancestorCache).has(task.id))) {
        error('invalid-input', `Task ${task.id} uses lease ${leaseId} outside its dependency span.`,
          task.id, leaseId);
      }
    }
  }
  for (const lease of graph.leases) {
    if (!ancestorsOf(lease.endTaskId, tasks, ancestorCache).has(lease.startTaskId))
      error('invalid-input', `Lease ${lease.id} end is not downstream of its start.`,
        lease.endTaskId, lease.id);
    if (!tasks.get(lease.endTaskId)!.leaseIds?.includes(lease.id))
      error('invalid-input', `Lease ${lease.id} end task must name its lease.`, lease.endTaskId, lease.id);
  }
  for (const [partId, owners] of allocations) {
    if (owners.length > 1 || parts.get(partId)?.initialState !== 'stock')
      error('part-allocation', `Part ${partId} cannot be allocated by ${owners.join(', ')}.`,
        owners[0], partId);
  }
  for (const task of graph.tasks) {
    for (const need of task.parts) {
      if (need.mode !== 'reference') continue;
      const part = parts.get(need.partId)!;
      const allocators = allocations.get(need.partId) ?? [];
      if (part.initialState !== 'allocated'
        && !allocators.some(id => ancestorsOf(task.id, tasks, ancestorCache).has(id)))
        error('part-allocation', `Task ${task.id} references ${need.partId} without a prior allocation.`,
          task.id, need.partId);
    }
  }
  for (const task of graph.tasks) {
    const demands = demandSlots(task.resources, task.id, 'task');
    for (const lease of graph.leases.filter(item => item.startTaskId === task.id))
      demands.push(...demandSlots(lease.resources, lease.id, 'lease'));
    const missing = assignResources(demands, [...graph.resources].sort(byId), new Set(),
      task.workfrontId).missing;
    if (missing)
      error('unavailable-resource', `Task ${task.id} cannot obtain ${missing.resourceId ?? missing.kind}.`,
        task.id, missing.resourceId ?? missing.kind);
  }
  return { tasks, leases, orderedTaskIds, diagnostics };
}

function criticalPath(orderedTaskIds: readonly string[], tasks: ReadonlyMap<string, PlanningTask>):
  { durationS: number; taskIds: string[] } {
  const finish = new Map<string, number>();
  const parent = new Map<string, string>();
  for (const id of orderedTaskIds) {
    const task = tasks.get(id)!;
    const best = [...task.predecessors].sort((a, b) =>
      (finish.get(b)! - finish.get(a)!) || compareIds(a, b))[0];
    finish.set(id, task.durationS + (best ? finish.get(best)! : 0));
    if (best) parent.set(id, best);
  }
  const last = [...orderedTaskIds].sort((a, b) =>
    (finish.get(b)! - finish.get(a)!) || compareIds(a, b))[0];
  const path: string[] = [];
  for (let id = last; id; id = parent.get(id)!) path.unshift(id);
  return { durationS: last ? finish.get(last)! : 0, taskIds: path };
}

function createRows(graph: TaskGraph, status: PlannedTask['status']): Map<string, PlannedTask> {
  return new Map([...graph.tasks].sort(byId).map(task => [task.id, {
    taskId: task.id, status, mechanicalStatus: task.mechanicalStatus,
    resourceIds: [], queueWaitS: 0, waitByReasonS: {},
  }]));
}

function calculateReport(graph: TaskGraph, rows: ReadonlyMap<string, PlannedTask>,
  reservations: readonly ReservationInterval[], makespanS: number,
  peakReadyQueue: number, peakParallelTasks: number,
  frontBusy: ReadonlyMap<string, number>,
  frontIdleReasons: ReadonlyMap<string, Partial<Record<WaitReason, number>>>,
  orderedTaskIds: readonly string[]): ThroughputReport {
  const taskMap = new Map(graph.tasks.map(task => [task.id, task]));
  const path = criticalPath(orderedTaskIds, taskMap);
  const workfronts: WorkfrontReport[] = [...graph.workfronts].sort(byId).map(front => {
    const busySlotS = frontBusy.get(front.id) ?? 0;
    const idleSlotS = makespanS * front.capacity - busySlotS;
    return {
      workfrontId: front.id, capacity: front.capacity, busySlotS, idleSlotS,
      idleByReasonS: frontIdleReasons.get(front.id) ?? {},
      utilization: makespanS ? busySlotS / (makespanS * front.capacity) : 0,
    };
  });
  const resourceKinds: ResourceKind[] = ['hoist', 'carrier', 'robot', 'tool', 'approach-zone'];
  const resources = resourceKinds.map(kind => {
    const units = graph.resources.filter(unit => unit.kind === kind).length;
    const busyUnitS = reservations.filter(interval =>
      graph.resources.find(unit => unit.id === interval.resourceId)?.kind === kind)
      .reduce((sum, interval) => sum + interval.endS - interval.startS, 0);
    return { kind, units, busyUnitS, idleUnitS: makespanS * units - busyUnitS,
      utilization: makespanS && units ? busyUnitS / (makespanS * units) : 0 };
  });
  return {
    serialDurationS: graph.tasks.reduce((sum, task) => sum + task.durationS, 0),
    precedenceCriticalPathS: path.durationS,
    precedenceCriticalPathTaskIds: path.taskIds,
    resourceLimitedMakespanS: makespanS,
    resourcePenaltyOverPrecedenceS: makespanS - path.durationS,
    totalReadyQueueWaitS: [...rows.values()].reduce((sum, row) => sum + row.queueWaitS, 0),
    peakReadyQueue, peakParallelTasks, workfronts, resources,
  };
}

/** Stable list scheduling. Completion precedes new starts at the same simulation second. */
export function scheduleTasks(graph: TaskGraph, options: ScheduleOptions = {}): ScheduleResult {
  const validated = validateGraph(graph);
  const rows = createRows(graph, 'invalid');
  const orderedRows = () => [...rows.values()];
  const invalidLimit = options.maxTransitions !== undefined
    && !isPositiveInteger(options.maxTransitions);
  if (invalidLimit) validated.diagnostics.push({ code: 'invalid-input',
    message: 'maxTransitions must be a positive integer.' });
  if (validated.diagnostics.length)
    return { graphId: graph.id, status: 'impossible', tasks: orderedRows(),
      reservations: [], diagnostics: validated.diagnostics, report: null };

  for (const row of rows.values()) row.status = 'blocked';
  const resources = [...graph.resources].sort(byId);
  const leasesByStart = new Map<string, ResourceLease[]>();
  const leasesByEnd = new Map<string, ResourceLease[]>();
  for (const lease of graph.leases) {
    leasesByStart.set(lease.startTaskId, [...(leasesByStart.get(lease.startTaskId) ?? []), lease]);
    leasesByEnd.set(lease.endTaskId, [...(leasesByEnd.get(lease.endTaskId) ?? []), lease]);
  }
  const activeLeases = new Map<string, ActiveLease>();
  const active = new Map<string, ActiveTask>();
  const completed = new Set<string>();
  const busy = new Set<string>();
  const lockedParts = new Set<string>();
  const partStates = new Map(graph.parts.map(part => [part.id, part.initialState]));
  const reservations: ReservationInterval[] = [];
  const frontBusy = new Map<string, number>();
  const frontIdleReasons = new Map<string, Partial<Record<WaitReason, number>>>();
  const frontRunning = new Map<string, number>();
  let now = 0;
  let peakReadyQueue = 0;
  let peakParallelTasks = 0;
  let transitions = 0;
  const transitionLimit = options.maxTransitions ?? graph.tasks.length * 2 + 2;
  const diagnostics: PlanDiagnostic[] = [];
  const markBlocked = (reason: string): ScheduleResult => {
    for (const row of rows.values()) {
      if (row.status === 'blocked' && !row.blockedReason) row.blockedReason = reason;
    }
    for (const lease of activeLeases.values()) {
      for (const resourceId of lease.resourceIds)
        reservations.push({ resourceId, ownerId: lease.lease.id, ownerKind: 'lease',
          startS: lease.startS, endS: now });
    }
    return { graphId: graph.id, status: 'blocked', tasks: orderedRows(),
      reservations: reservations.sort((a, b) => a.startS - b.startS
        || compareIds(a.resourceId, b.resourceId) || compareIds(a.ownerId, b.ownerId)),
      diagnostics, report: null };
  };

  while (completed.size < graph.tasks.length) {
    if (++transitions > transitionLimit) {
      diagnostics.push({ code: 'transition-limit', message: `Exceeded ${transitionLimit} scheduler transitions.` });
      return markBlocked('Scheduler transition limit reached.');
    }
    const ready = validated.orderedTaskIds.filter(id => !completed.has(id) && !active.has(id)
      && validated.tasks.get(id)!.predecessors.every(predecessor => completed.has(predecessor)));
    for (const id of ready) {
      const row = rows.get(id)!;
      if (row.readyAtS === undefined) row.readyAtS = now;
    }
    const waitReason = new Map<string, WaitReason>();
    for (const id of ready) {
      const task = validated.tasks.get(id)!;
      const row = rows.get(id)!;
      const front = graph.workfronts.find(item => item.id === task.workfrontId)!;
      if ((frontRunning.get(front.id) ?? 0) >= front.capacity) {
        waitReason.set(id, 'workfront');
        continue;
      }
      if ((task.leaseIds ?? []).some(leaseId => !activeLeases.has(leaseId))) {
        waitReason.set(id, 'lease');
        continue;
      }
      if (task.parts.some(need => lockedParts.has(need.partId)
        || partStates.get(need.partId) !== (need.mode === 'allocate' ? 'stock' : 'allocated'))) {
        waitReason.set(id, 'part');
        continue;
      }
      const demands = demandSlots(task.resources, id, 'task');
      for (const lease of leasesByStart.get(id) ?? [])
        demands.push(...demandSlots(lease.resources, lease.id, 'lease'));
      const assignment = assignResources(demands, resources, busy, front.id);
      if (assignment.missing) {
        waitReason.set(id, `resource:${assignment.missing.kind}`);
        continue;
      }
      const directResourceIds: string[] = [];
      for (const { unit, demand } of assignment.assignments) {
        busy.add(unit.id);
        if (demand.ownerKind === 'task') directResourceIds.push(unit.id);
      }
      for (const lease of leasesByStart.get(id) ?? []) {
        activeLeases.set(lease.id, { lease, startS: now,
          resourceIds: assignment.assignments.filter(item => item.demand.ownerId === lease.id)
            .map(item => item.unit.id).sort(compareIds) });
      }
      const partIds = task.parts.map(need => need.partId);
      for (const partId of partIds) lockedParts.add(partId);
      const endS = now + task.durationS;
      active.set(id, { id, endS, resourceIds: directResourceIds, partIds });
      frontRunning.set(front.id, (frontRunning.get(front.id) ?? 0) + 1);
      row.status = 'planned';
      row.startS = now;
      row.endS = endS;
      row.queueWaitS = now - row.readyAtS!;
      row.resourceIds = directResourceIds.sort(compareIds);
    }
    peakParallelTasks = Math.max(peakParallelTasks, active.size);
    const queued = ready.filter(id => !active.has(id));
    peakReadyQueue = Math.max(peakReadyQueue, queued.length);
    if (active.size === 0) {
      for (const id of queued) {
        const reason = waitReason.get(id) ?? 'dependency-or-no-work';
        diagnostics.push({ code: 'deadlock', taskId: id,
          message: `Task ${id} is ready but blocked by ${reason}.` });
        rows.get(id)!.blockedReason = reason;
      }
      for (const id of validated.orderedTaskIds.filter(item => !completed.has(item) && !queued.includes(item))) {
        diagnostics.push({ code: 'deadlock', taskId: id,
          message: `Task ${id} still awaits a predecessor.` });
        rows.get(id)!.blockedReason = 'predecessor';
      }
      return markBlocked('No task can advance.');
    }
    const nextTime = Math.min(...[...active.values()].map(item => item.endS));
    const delta = nextTime - now;
    for (const id of queued) {
      const row = rows.get(id)!;
      const reason = waitReason.get(id) ?? 'dependency-or-no-work';
      row.waitByReasonS[reason] = (row.waitByReasonS[reason] ?? 0) + delta;
    }
    for (const front of graph.workfronts) {
      const running = frontRunning.get(front.id) ?? 0;
      frontBusy.set(front.id, (frontBusy.get(front.id) ?? 0) + running * delta);
      const idleSlots = front.capacity - running;
      if (idleSlots <= 0) continue;
      const firstQueued = queued.find(id => validated.tasks.get(id)!.workfrontId === front.id);
      const reason = firstQueued ? (waitReason.get(firstQueued) ?? 'dependency-or-no-work')
        : 'dependency-or-no-work';
      const reasons = frontIdleReasons.get(front.id) ?? {};
      reasons[reason] = (reasons[reason] ?? 0) + idleSlots * delta;
      frontIdleReasons.set(front.id, reasons);
    }
    now = nextTime;
    const ending = [...active.values()].filter(item => item.endS === now)
      .sort((a, b) => compareIds(a.id, b.id));
    for (const item of ending) {
      const task = validated.tasks.get(item.id)!;
      for (const resourceId of item.resourceIds) {
        busy.delete(resourceId);
        reservations.push({ resourceId, ownerId: item.id, ownerKind: 'task',
          startS: rows.get(item.id)!.startS!, endS: now });
      }
      for (const partId of item.partIds) lockedParts.delete(partId);
      for (const need of task.parts.filter((part): part is PartRequirement => part.mode === 'allocate'))
        partStates.set(need.partId, 'allocated');
      for (const lease of leasesByEnd.get(item.id) ?? []) {
        const held = activeLeases.get(lease.id)!;
        for (const resourceId of held.resourceIds) {
          busy.delete(resourceId);
          reservations.push({ resourceId, ownerId: lease.id, ownerKind: 'lease',
            startS: held.startS, endS: now });
        }
        activeLeases.delete(lease.id);
      }
      active.delete(item.id);
      completed.add(item.id);
      frontRunning.set(task.workfrontId, frontRunning.get(task.workfrontId)! - 1);
    }
  }
  reservations.sort((a, b) => a.startS - b.startS
    || compareIds(a.resourceId, b.resourceId) || compareIds(a.ownerId, b.ownerId));
  const report = calculateReport(graph, rows, reservations, now, peakReadyQueue,
    peakParallelTasks, frontBusy, frontIdleReasons, validated.orderedTaskIds);
  return { graphId: graph.id, status: 'complete', tasks: orderedRows(),
    reservations, diagnostics, report };
}
