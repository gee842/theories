import type { Vec3 } from '../domain/types';
import type {
  Axis, ConditioningDiagnostics, ConstructionStage, FreeDof, LoadPathResult,
  MemberResult, NodalLoad, StageResult, SupportPath, TrussMember, TrussModel,
  TrussNode, TrussSupport,
} from './types';

const AXES: readonly Axis[] = ['x', 'y', 'z'];
const RELATIVE_RANK_TOLERANCE = 1e-11;
const CONDITION_WARNING = 1e7;
const CONDITION_LIMIT = 1e9;
const compareId = (a: string, b: string): number => a < b ? -1 : a > b ? 1 : 0;

interface Geometry { member: TrussMember; lengthM: number; direction: Vec3; axialStiffnessNPerM: number; }
interface ModelIndex {
  nodes: Map<string, TrussNode>;
  members: Map<string, Geometry>;
  supports: Map<string, TrussSupport>;
}
interface EigenResult { values: number[]; vectors: number[][]; converged: boolean; }

function checkId(id: string, label: string): void {
  if (typeof id !== 'string' || !id.trim()) throw new Error(`${label} needs a nonempty id`);
}
function checkPositive(value: number, label: string): void {
  if (!Number.isFinite(value) || value <= 0) throw new Error(`${label} must be finite and positive`);
}
function checkVector(vector: Vec3, label: string): void {
  if (!Array.isArray(vector) || vector.length !== 3 || !vector.every(Number.isFinite)) {
    throw new Error(`${label} must be a finite 3-vector`);
  }
}
function uniqueIds(ids: readonly string[], label: string): string[] {
  const sorted = [...ids].sort();
  for (let i = 0; i < sorted.length; i++) {
    checkId(sorted[i], label);
    if (i && sorted[i] === sorted[i - 1]) throw new Error(`Duplicate ${label}: ${sorted[i]}`);
  }
  return sorted;
}

function indexModel(model: TrussModel): ModelIndex {
  const nodes = new Map<string, TrussNode>();
  const members = new Map<string, Geometry>();
  const supports = new Map<string, TrussSupport>();
  for (const node of model.nodes) {
    checkId(node.id, 'node');
    checkVector(node.positionM, `node ${node.id} positionM`);
    if (nodes.has(node.id)) throw new Error(`Duplicate node: ${node.id}`);
    nodes.set(node.id, node);
  }
  for (const member of model.members) {
    checkId(member.id, 'member');
    if (members.has(member.id)) throw new Error(`Duplicate member: ${member.id}`);
    const a = nodes.get(member.nodeA)?.positionM;
    const b = nodes.get(member.nodeB)?.positionM;
    if (!a || !b) throw new Error(`Member ${member.id} references an unknown node`);
    const delta: Vec3 = [b[0] - a[0], b[1] - a[1], b[2] - a[2]];
    const lengthM = Math.hypot(...delta);
    if (!(lengthM > 1e-9)) throw new Error(`Member ${member.id} has zero or negligible length`);
    checkPositive(member.areaM2, `member ${member.id} areaM2`);
    checkPositive(member.elasticModulusPa, `member ${member.id} elasticModulusPa`);
    checkPositive(member.tensionCapacityN, `member ${member.id} tensionCapacityN`);
    checkPositive(member.compressionCapacityN, `member ${member.id} compressionCapacityN`);
    members.set(member.id, {
      member, lengthM,
      direction: [delta[0] / lengthM, delta[1] / lengthM, delta[2] / lengthM],
      axialStiffnessNPerM: member.elasticModulusPa * member.areaM2 / lengthM,
    });
    checkPositive(members.get(member.id)!.axialStiffnessNPerM, `member ${member.id} axial stiffness`);
  }
  for (const support of model.supports) {
    checkId(support.id, 'support');
    if (supports.has(support.id)) throw new Error(`Duplicate support: ${support.id}`);
    if (!nodes.has(support.nodeId)) throw new Error(`Support ${support.id} references an unknown node`);
    if (!Array.isArray(support.restrained) || support.restrained.length !== 3 ||
        !support.restrained.every(value => typeof value === 'boolean') ||
        !support.restrained.some(Boolean)) {
      throw new Error(`Support ${support.id} needs three Boolean restraint flags and at least one restraint`);
    }
    if (support.kind !== 'permanent' && support.kind !== 'temporary') {
      throw new Error(`Support ${support.id} needs a permanent or temporary kind`);
    }
    supports.set(support.id, support);
  }
  return { nodes, members, supports };
}

function sortLoads(loads: readonly NodalLoad[]): NodalLoad[] {
  return [...loads].sort((a, b) => compareId(a.nodeId, b.nodeId) ||
    a.forceN[0] - b.forceN[0] || a.forceN[1] - b.forceN[1] || a.forceN[2] - b.forceN[2]);
}

/** Cyclic Jacobi diagonalization of the symmetric free-DOF stiffness matrix. */
function eigenSymmetric(matrix: number[][]): EigenResult {
  const n = matrix.length;
  const a = matrix.map(row => [...row]);
  const v = Array.from({ length: n }, (_, i) =>
    Array.from({ length: n }, (_, j) => Number(i === j)));
  const scale = Math.max(0, ...a.map((row, i) => Math.abs(row[i])));
  if (!scale) return { values: Array(n).fill(0), vectors: v, converged: true };
  let converged = false;
  for (let sweep = 0; sweep < 40; sweep++) {
    let largestOffDiagonal = 0;
    for (let p = 0; p < n - 1; p++) {
      for (let q = p + 1; q < n; q++) {
        const apq = a[p][q];
        largestOffDiagonal = Math.max(largestOffDiagonal, Math.abs(apq));
        if (Math.abs(apq) <= scale * 1e-14) continue;
        const tau = (a[q][q] - a[p][p]) / (2 * apq);
        const t = (tau >= 0 ? 1 : -1) / (Math.abs(tau) + Math.hypot(1, tau));
        const c = 1 / Math.hypot(1, t);
        const s = t * c;
        const app = a[p][p];
        const aqq = a[q][q];
        a[p][p] = app - t * apq;
        a[q][q] = aqq + t * apq;
        a[p][q] = a[q][p] = 0;
        for (let k = 0; k < n; k++) {
          if (k !== p && k !== q) {
            const akp = a[k][p];
            const akq = a[k][q];
            a[k][p] = a[p][k] = c * akp - s * akq;
            a[k][q] = a[q][k] = s * akp + c * akq;
          }
          const vkp = v[k][p];
          const vkq = v[k][q];
          v[k][p] = c * vkp - s * vkq;
          v[k][q] = s * vkp + c * vkq;
        }
      }
    }
    if (largestOffDiagonal <= scale * 1e-13) {
      converged = true;
      break;
    }
  }
  return { values: a.map((row, i) => row[i]), vectors: v, converged };
}

/** Solve a positive definite system without changing the supplied matrix. */
function choleskySolve(matrix: number[][], force: number[]): number[] | null {
  const n = matrix.length;
  const l = Array.from({ length: n }, () => Array<number>(n).fill(0));
  for (let i = 0; i < n; i++) {
    for (let j = 0; j <= i; j++) {
      let value = matrix[i][j];
      for (let k = 0; k < j; k++) value -= l[i][k] * l[j][k];
      if (i === j) {
        if (!(value > 0) || !Number.isFinite(value)) return null;
        l[i][j] = Math.sqrt(value);
      } else l[i][j] = value / l[j][j];
    }
  }
  const y = Array<number>(n).fill(0);
  for (let i = 0; i < n; i++) {
    let value = force[i];
    for (let k = 0; k < i; k++) value -= l[i][k] * y[k];
    y[i] = value / l[i][i];
  }
  const x = Array<number>(n).fill(0);
  for (let i = n - 1; i >= 0; i--) {
    let value = y[i];
    for (let k = i + 1; k < n; k++) value -= l[k][i] * x[k];
    x[i] = value / l[i][i];
  }
  return x.every(Number.isFinite) ? x : null;
}

function adjacency(geometries: readonly Geometry[], carryingIds?: ReadonlySet<string>): Map<string, { nodeId: string; memberId: string }[]> {
  const links = new Map<string, { nodeId: string; memberId: string }[]>();
  for (const { member } of geometries) {
    if (carryingIds && !carryingIds.has(member.id)) continue;
    for (const [from, to] of [[member.nodeA, member.nodeB], [member.nodeB, member.nodeA]]) {
      const edges = links.get(from) ?? [];
      edges.push({ nodeId: to, memberId: member.id });
      links.set(from, edges);
    }
  }
  for (const edges of links.values()) edges.sort((a, b) => compareId(a.memberId, b.memberId) || compareId(a.nodeId, b.nodeId));
  return links;
}

function pathsToSupports(start: string, links: Map<string, { nodeId: string; memberId: string }[]>,
  supports: readonly TrussSupport[]): SupportPath[] {
  const parent = new Map<string, { nodeId: string; memberId: string } | null>([[start, null]]);
  const queue = [start];
  for (let i = 0; i < queue.length; i++) {
    for (const edge of links.get(queue[i]) ?? []) {
      if (parent.has(edge.nodeId)) continue;
      parent.set(edge.nodeId, { nodeId: queue[i], memberId: edge.memberId });
      queue.push(edge.nodeId);
    }
  }
  return supports.filter(support => parent.has(support.nodeId)).map(support => {
    const memberIds: string[] = [];
    let node = support.nodeId;
    while (node !== start) {
      const step = parent.get(node)!;
      if (!step) break;
      memberIds.unshift(step.memberId);
      node = step.nodeId;
    }
    return { supportId: support.id, memberIds };
  });
}

function unresolvedMembers(geometries: readonly Geometry[]): MemberResult[] {
  return geometries.map(({ member, lengthM }) => ({
    id: member.id, lengthM, axialForceN: null, stressPa: null,
    mode: 'unresolved', tensionCapacityN: member.tensionCapacityN,
    compressionCapacityN: member.compressionCapacityN, capacityN: null, utilization: null,
  }));
}

function assessIndexedStage(index: ModelIndex, stage: ConstructionStage): StageResult {
  checkId(stage.id, 'stage');
  const memberIds = uniqueIds(stage.activeMemberIds, `active member in stage ${stage.id}`);
  const supportIds = uniqueIds(stage.activeSupportIds, `active support in stage ${stage.id}`);
  const geometries = memberIds.map(id => {
    const geometry = index.members.get(id);
    if (!geometry) throw new Error(`Stage ${stage.id} references unknown member ${id}`);
    return geometry;
  });
  const supports = supportIds.map(id => {
    const support = index.supports.get(id);
    if (!support) throw new Error(`Stage ${stage.id} references unknown support ${id}`);
    return support;
  });
  const external = new Map<string, number[]>();
  for (const load of stage.loads) {
    if (!index.nodes.has(load.nodeId)) throw new Error(`Stage ${stage.id} load references unknown node ${load.nodeId}`);
    checkVector(load.forceN, `stage ${stage.id} load at ${load.nodeId}`);
  }
  for (const load of sortLoads(stage.loads)) {
    const total = external.get(load.nodeId) ?? [0, 0, 0];
    for (let axis = 0; axis < 3; axis++) total[axis] += load.forceN[axis];
    external.set(load.nodeId, total);
  }
  const activeNodeIds = new Set<string>();
  for (const { member } of geometries) { activeNodeIds.add(member.nodeA); activeNodeIds.add(member.nodeB); }
  for (const support of supports) activeNodeIds.add(support.nodeId);
  for (const [nodeId, force] of external) if (Math.hypot(...force) > 0) activeNodeIds.add(nodeId);
  const nodes = [...activeNodeIds].sort();
  const restrained = new Map(nodes.map(id => [id, [false, false, false]]));
  for (const support of supports) {
    const axes = restrained.get(support.nodeId)!;
    for (let axis = 0; axis < 3; axis++) {
      if (!support.restrained[axis]) continue;
      if (axes[axis]) throw new Error(`Stage ${stage.id} has overlapping restraints at node ${support.nodeId}, ${AXES[axis]}`);
      axes[axis] = true;
    }
  }
  const free: { nodeId: string; axis: Axis; axisIndex: number }[] = [];
  const freeIndex = new Map<string, number[]>();
  for (const nodeId of nodes) {
    const indices = [-1, -1, -1];
    for (let axis = 0; axis < 3; axis++) {
      if (!restrained.get(nodeId)![axis]) {
        indices[axis] = free.length;
        free.push({ nodeId, axis: AXES[axis], axisIndex: axis });
      }
    }
    freeIndex.set(nodeId, indices);
  }
  const n = free.length;
  const stiffness = Array.from({ length: n }, () => Array<number>(n).fill(0));
  const force = Array<number>(n).fill(0);
  for (const [nodeId, applied] of external) {
    const indices = freeIndex.get(nodeId);
    if (!indices) continue;
    for (let axis = 0; axis < 3; axis++) if (indices[axis] >= 0) force[indices[axis]] += applied[axis];
  }
  for (const { member, direction, axialStiffnessNPerM } of geometries) {
    const indices = [...freeIndex.get(member.nodeA)!, ...freeIndex.get(member.nodeB)!];
    const coefficients = [-direction[0], -direction[1], -direction[2], ...direction];
    for (let a = 0; a < 6; a++) {
      if (indices[a] < 0) continue;
      for (let b = 0; b < 6; b++) {
        if (indices[b] < 0) continue;
        stiffness[indices[a]][indices[b]] += axialStiffnessNPerM * coefficients[a] * coefficients[b];
      }
    }
  }
  const eigen = eigenSymmetric(stiffness);
  const largest = n ? Math.max(0, ...eigen.values) : null;
  const smallest = n ? Math.min(...eigen.values) : null;
  const rankThreshold = (largest ?? 0) * RELATIVE_RANK_TOLERANCE;
  const rank = eigen.values.filter(value => value > rankThreshold).length;
  const conditionNumber = n && rank === n && smallest! > 0 ? largest! / smallest! : null;
  const mechanismModes = eigen.values.flatMap((value, column) => {
    if (value > rankThreshold) return [];
    const amplitudes = free.map((dof, row) => ({ ...dof, amplitude: eigen.vectors[row][column] }));
    const maximum = Math.max(0, ...amplitudes.map(dof => Math.abs(dof.amplitude)));
    const dominantDofs: FreeDof[] = amplitudes
      .filter(dof => Math.abs(dof.amplitude) >= maximum * 0.35)
      .sort((a, b) => Math.abs(b.amplitude) - Math.abs(a.amplitude) ||
        compareId(a.nodeId, b.nodeId) || compareId(a.axis, b.axis));
    return [{ eigenvalueNPerM: value, dominantDofs }];
  });
  const messages: string[] = [];
  if (rank < n) messages.push(`Free stiffness rank ${rank}/${n}: a mechanism or disconnected free degree of freedom is present.`);
  if (!eigen.converged) messages.push('Stiffness eigenvalue calculation did not converge.');
  if (conditionNumber !== null && conditionNumber > CONDITION_WARNING) {
    messages.push(`Stiffness condition number ${conditionNumber.toExponential(2)} exceeds the ${CONDITION_WARNING.toExponential(0)} warning level.`);
  }
  if (conditionNumber !== null && conditionNumber > CONDITION_LIMIT) {
    messages.push('Stiffness solution withheld because its condition number exceeds the reliability limit.');
  }
  let stability: StageResult['stability'] = rank < n ? 'mechanism' :
    !eigen.converged || (conditionNumber !== null && conditionNumber > CONDITION_LIMIT) ? 'ill-conditioned' : 'stable';
  let solution = stability === 'stable' ? choleskySolve(stiffness, force) : null;
  if (stability === 'stable' && !solution) {
    stability = 'ill-conditioned';
    messages.push('Positive-definite stiffness solve failed.');
  }
  if (stability === 'stable' && solution) {
    const residual = stiffness.reduce((max, row, i) => {
      const computed = row.reduce((sum, value, j) => sum + value * solution![j], 0);
      return Math.max(max, Math.abs(computed - force[i]));
    }, 0);
    const forceScale = Math.max(1, ...force.map(Math.abs));
    if (residual > forceScale * 1e-6) {
      stability = 'ill-conditioned';
      solution = null;
      messages.push(`Equilibrium residual ${residual.toExponential(2)} N exceeds the solve tolerance.`);
    }
  }
  const diagnostics: ConditioningDiagnostics = {
    freeDofCount: n, stiffnessRank: rank,
    smallestEigenvalueNPerM: smallest, largestEigenvalueNPerM: largest,
    conditionNumber, relativeRankTolerance: RELATIVE_RANK_TOLERANCE,
    conditionWarning: conditionNumber !== null && conditionNumber > CONDITION_WARNING,
    eigenSolverConverged: eigen.converged,
    equilibriumResidualN: null, globalForceResidualN: null,
    mechanismModes, messages,
  };
  const allLinks = adjacency(geometries);
  const loadedNodes = [...external.entries()]
    .filter(([, applied]) => Math.hypot(...applied) > 0)
    .sort(([a], [b]) => compareId(a, b));
  const loadPaths = (carryingLinks?: Map<string, { nodeId: string; memberId: string }[]>,
    reactingSupports: readonly TrussSupport[] = []): LoadPathResult[] => loadedNodes.map(([nodeId, applied]) => {
    const connected = pathsToSupports(nodeId, allLinks, supports).length > 0;
    const supportPaths = carryingLinks ? pathsToSupports(nodeId, carryingLinks, reactingSupports) : [];
    const status: LoadPathResult['status'] = !connected ? 'disconnected' : !carryingLinks ? 'unresolved' :
      supportPaths.some(path => path.memberIds.length === 0) ? 'direct' :
      supportPaths.length ? 'transmitted' : 'self-equilibrated';
    return {
      nodeId, appliedForceN: [applied[0], applied[1], applied[2]] as Vec3,
      topologicallyConnectedToRestraint: connected, status, supportPaths,
    };
  });
  if (!solution || stability !== 'stable') {
    return {
      scope: 'axial-truss-screening-only', stageId: stage.id,
      stability, capacity: 'unverified', canTransferLoad: false,
      diagnostics, displacements: [], members: unresolvedMembers(geometries),
      reactions: [], loadPaths: loadPaths(),
    };
  }
  const displacement = new Map<string, number[]>();
  for (const nodeId of nodes) {
    const indices = freeIndex.get(nodeId)!;
    displacement.set(nodeId, indices.map(index => index < 0 ? 0 : solution[index]));
  }
  const internal = new Map(nodes.map(id => [id, [0, 0, 0]]));
  const forceThreshold = Math.max(1e-8, ...loadedNodes.map(([, applied]) => Math.hypot(...applied) * 1e-9));
  const carryingIds = new Set<string>();
  const memberResults: MemberResult[] = geometries.map(({ member, lengthM, direction, axialStiffnessNPerM }) => {
    const a = displacement.get(member.nodeA)!;
    const b = displacement.get(member.nodeB)!;
    const extension = direction.reduce((sum, component, axis) => sum + component * (b[axis] - a[axis]), 0);
    const axialForceN = axialStiffnessNPerM * extension;
    for (let axis = 0; axis < 3; axis++) {
      internal.get(member.nodeA)![axis] -= axialForceN * direction[axis];
      internal.get(member.nodeB)![axis] += axialForceN * direction[axis];
    }
    if (Math.abs(axialForceN) > forceThreshold) carryingIds.add(member.id);
    const mode = axialForceN === 0 ? 'zero' : axialForceN > 0 ? 'tension' : 'compression';
    const capacityN = mode === 'tension' ? member.tensionCapacityN :
      mode === 'compression' ? member.compressionCapacityN : null;
    return {
      id: member.id, lengthM, axialForceN, stressPa: axialForceN / member.areaM2,
      mode, tensionCapacityN: member.tensionCapacityN,
      compressionCapacityN: member.compressionCapacityN,
      capacityN, utilization: capacityN ? Math.abs(axialForceN) / capacityN : 0,
    };
  });
  const reactions = supports.map(support => {
    const memberForce = internal.get(support.nodeId)!;
    const applied = external.get(support.nodeId) ?? [0, 0, 0];
    return {
      supportId: support.id, nodeId: support.nodeId,
      forceN: support.restrained.map((fixed, axis) => fixed ? memberForce[axis] - applied[axis] : 0) as unknown as Vec3,
    };
  });
  let freeResidual = 0;
  for (const dof of free) {
    const memberForce = internal.get(dof.nodeId)![dof.axisIndex];
    const applied = external.get(dof.nodeId)?.[dof.axisIndex] ?? 0;
    freeResidual = Math.max(freeResidual, Math.abs(memberForce - applied));
  }
  const globalBalance = [0, 1, 2].map(axis =>
    [...external.values()].reduce((sum, applied) => sum + applied[axis], 0) +
    reactions.reduce((sum, reaction) => sum + reaction.forceN[axis], 0));
  diagnostics.equilibriumResidualN = freeResidual;
  diagnostics.globalForceResidualN = Math.hypot(...globalBalance);
  const capacity = memberResults.some(member => member.utilization !== null && member.utilization > 1 + 1e-9) ? 'fail' : 'pass';
  const reactingSupports = supports.filter(support => {
    const reaction = reactions.find(item => item.supportId === support.id)!;
    return Math.hypot(...reaction.forceN) > forceThreshold;
  });
  return {
    scope: 'axial-truss-screening-only', stageId: stage.id,
    stability, capacity, canTransferLoad: capacity === 'pass',
    diagnostics,
    displacements: nodes.map(nodeId => ({
      nodeId, displacementM: displacement.get(nodeId)! as unknown as Vec3,
    })),
    members: memberResults, reactions,
    loadPaths: loadPaths(adjacency(geometries, carryingIds), reactingSupports),
  };
}

/** Assess one construction stage using a 3D pin-jointed, linear-elastic axial truss. */
export function assessTrussStage(model: TrussModel, stage: ConstructionStage): StageResult {
  return assessIndexedStage(indexModel(model), stage);
}

/** Assess stages in the caller's order, with a fresh equilibrium solution at each stage. */
export function assessConstructionStages(model: TrussModel, stages: readonly ConstructionStage[]): StageResult[] {
  const index = indexModel(model);
  uniqueIds(stages.map(stage => stage.id), 'stage');
  return stages.map(stage => assessIndexedStage(index, stage));
}
