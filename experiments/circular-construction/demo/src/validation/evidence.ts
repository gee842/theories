import type { EventAction, ExecutionEvent, WorldState } from '../domain/types';

export type CheckStatus = 'passed' | 'failed' | 'unverified';
export type EvidenceBasis = 'measured' | 'calculated' | 'assumed';
export type CapacityBasis = 'measured' | 'assumed' | 'none';
export type ConnectionSelector = 'part' | 'A' | 'B';

/** Every external input to a check belongs in one of these four domains. */
export interface EngineeringInputs {
  readonly geometry: Readonly<Record<string, unknown>>;
  readonly supports: Readonly<Record<string, unknown>>;
  readonly loads: Readonly<Record<string, unknown>>;
  readonly capacities: Readonly<Record<string, {
    readonly value: unknown;
    readonly units: string;
    readonly basis: 'measured' | 'assumed';
    readonly reference: string;
  }>>;
}

export interface ModelIdentity {
  readonly id: string;
  readonly version: string;
  /** Exact physical question answered by this model; a truss screen is not a beam-frame check. */
  readonly scope: string;
}

export interface EvidenceSubmission {
  readonly id: string;
  readonly checkId: string;
  readonly connectionId: string | null;
  readonly model: ModelIdentity;
  readonly status: CheckStatus;
  readonly provenance: {
    readonly basis: EvidenceBasis;
    readonly reference: string;
    readonly assumptions?: readonly string[];
  };
  /** Only the named capacity inputs may be claimed as measured or assumed by this result. */
  readonly capacityIds: readonly string[];
  readonly dependencies: readonly string[];
  readonly detail: string;
}

export interface EngineeringEvidence extends Omit<EvidenceSubmission, 'provenance'> {
  readonly schemaVersion: 1;
  readonly worldRevision: number;
  readonly eventId: string;
  readonly action: EventAction;
  readonly partId: string;
  readonly inputFingerprint: string;
  readonly provenance: {
    readonly basis: EvidenceBasis;
    readonly capacityBasis: CapacityBasis;
    readonly reference: string;
    readonly assumptions: readonly string[];
  };
}

export interface GateRequirement {
  readonly id: string;
  readonly checkId: string;
  readonly connection: ConnectionSelector;
  readonly model: ModelIdentity;
  readonly acceptedBases: readonly EvidenceBasis[];
  readonly acceptedCapacityBases: readonly CapacityBasis[];
}

export interface GateDefinition {
  readonly id: string;
  readonly version: string;
  readonly action: EventAction;
  readonly requirements: readonly GateRequirement[];
}

export type HoldCode =
  | 'missing' | 'stale-revision' | 'fingerprint-mismatch' | 'event-mismatch'
  | 'action-mismatch' | 'part-mismatch' | 'connection-mismatch'
  | 'model-mismatch' | 'scope-mismatch' | 'basis-mismatch'
  | 'capacity-basis-mismatch' | 'failed' | 'unverified'
  | 'dependency-missing' | 'dependency-invalid' | 'dependency-cycle';

export interface GateHold {
  readonly requirementId: string;
  readonly code: HoldCode;
  readonly message: string;
  readonly evidenceId?: string;
}

export interface GateDecision {
  readonly gateId: string;
  readonly gateVersion: string;
  readonly eventId: string;
  readonly worldRevision: number;
  readonly inputFingerprint: string;
  readonly allowed: boolean;
  readonly holds: readonly GateHold[];
  readonly acceptedEvidenceIds: readonly string[];
}

function named(value: string, label: string): void {
  if (typeof value !== 'string' || !value.trim()) throw new Error(`${label} needs a nonempty value`);
}

function record(value: unknown, label: string, allowEmpty = false): asserts value is Record<string, unknown> {
  if (value === null || typeof value !== 'object' || Array.isArray(value) ||
      (Object.getPrototypeOf(value) !== Object.prototype && Object.getPrototypeOf(value) !== null) ||
      (!allowEmpty && !Object.keys(value).length)) {
    throw new Error(`${label} needs a ${allowEmpty ? '' : 'nonempty '}plain object`);
  }
}

/** Exact canonical JSON is used as the fingerprint, so no hash collision can release a gate. */
function canonical(value: unknown, path: string, active = new Set<object>()): string {
  if (value === null || typeof value === 'boolean' || typeof value === 'string') return JSON.stringify(value);
  if (typeof value === 'number') {
    if (!Number.isFinite(value)) throw new Error(`${path} must be finite`);
    return JSON.stringify(value);
  }
  if (typeof value !== 'object') throw new Error(`${path} is not JSON data`);
  if (active.has(value)) throw new Error(`${path} contains a cycle`);
  active.add(value);
  try {
    if (Array.isArray(value)) {
      if (Reflect.ownKeys(value).length !== value.length + 1) throw new Error(`${path} is a sparse or decorated array`);
      const items: string[] = [];
      for (let index = 0; index < value.length; index++) {
        const field = Object.getOwnPropertyDescriptor(value, String(index));
        if (!field || !field.enumerable || !('value' in field))
          throw new Error(`${path}[${index}] is not plain data`);
        items.push(canonical(field.value, `${path}[${index}]`, active));
      }
      return `[${items.join(',')}]`;
    }
    record(value, path, true);
    if (Reflect.ownKeys(value).some(key => typeof key === 'symbol'))
      throw new Error(`${path} has a symbol property`);
    const fields = Object.getOwnPropertyDescriptors(value);
    const keys = Object.keys(fields).sort();
    const body = keys.map(key => {
      const field = fields[key];
      if (!field.enumerable || !('value' in field)) throw new Error(`${path}.${key} is not plain data`);
      return `${JSON.stringify(key)}:${canonical(field.value, `${path}.${key}`, active)}`;
    });
    return `{${body.join(',')}}`;
  } finally {
    active.delete(value);
  }
}

function validateInputs(inputs: EngineeringInputs): void {
  record(inputs, 'engineering inputs');
  record(inputs.geometry, 'geometry');
  record(inputs.supports, 'supports');
  record(inputs.loads, 'loads');
  record(inputs.capacities, 'capacities', true);
  for (const [id, capacity] of Object.entries(inputs.capacities)) {
    named(id, 'capacity ID');
    record(capacity, `capacity ${id}`);
    named(capacity.units, `capacity ${id} units`);
    named(capacity.reference, `capacity ${id} reference`);
    if (capacity.basis !== 'measured' && capacity.basis !== 'assumed')
      throw new Error(`capacity ${id} needs measured or assumed basis`);
    if (!Object.hasOwn(capacity, 'value')) throw new Error(`capacity ${id} needs a value`);
    if (capacity.value === null || capacity.value === undefined ||
        (typeof capacity.value === 'object' && !Object.keys(capacity.value).length))
      throw new Error(`capacity ${id} needs a nonempty value`);
  }
  canonical(inputs, 'engineering inputs');
}

function eventContext(world: WorldState, event: ExecutionEvent, inputs: EngineeringInputs) {
  if (!Number.isSafeInteger(world.revision) || world.revision < 0) throw new Error('Invalid world revision');
  if (event.sequence !== world.revision + 1) throw new Error('Gate event sequence is not contiguous');
  named(event.id, 'event ID');
  named(event.partId, 'part ID');
  if (!world.parts[event.partId]) throw new Error(`Unknown gate part: ${event.partId}`);
  validateInputs(inputs);
  return {
    worldRevision: world.revision,
    eventId: event.id,
    action: event.action,
    partId: event.partId,
    inputFingerprint: `engineering-inputs/v1:${canonical({ world, inputs }, 'fingerprint')}`,
  };
}

function freezeDeep<T>(value: T): T {
  if (value !== null && typeof value === 'object' && !Object.isFrozen(value)) {
    for (const item of Object.values(value)) freezeDeep(item);
    Object.freeze(value);
  }
  return value;
}

function uniqueNames(values: readonly string[], label: string): string[] {
  if (!Array.isArray(values)) throw new Error(`${label} must be an array`);
  const sorted = [...values].sort();
  for (let i = 0; i < sorted.length; i++) {
    named(sorted[i], label);
    if (i && sorted[i] === sorted[i - 1]) throw new Error(`Duplicate ${label}: ${sorted[i]}`);
  }
  return sorted;
}

function modelIdentity(model: ModelIdentity): void {
  if (!model) throw new Error('Missing model identity');
  named(model.id, 'model ID');
  named(model.version, 'model version');
  named(model.scope, 'model scope');
}

function capacityBasis(inputs: EngineeringInputs, ids: readonly string[]): CapacityBasis {
  if (!ids.length) return 'none';
  return ids.some(id => inputs.capacities[id].basis === 'assumed') ? 'assumed' : 'measured';
}

export class EvidenceRegistry {
  private readonly byId = new Map<string, EngineeringEvidence>();

  /** Copies and freezes a result. A late async result retains the revision at which it was computed. */
  register(world: WorldState, event: ExecutionEvent, inputs: EngineeringInputs,
    submission: EvidenceSubmission): EngineeringEvidence {
    const context = eventContext(world, event, inputs);
    named(submission.id, 'evidence ID');
    if (this.byId.has(submission.id)) throw new Error(`Evidence ID already registered: ${submission.id}`);
    named(submission.checkId, 'check ID');
    modelIdentity(submission.model);
    if (!['passed', 'failed', 'unverified'].includes(submission.status)) throw new Error('Invalid evidence status');
    if (!['measured', 'calculated', 'assumed'].includes(submission.provenance?.basis))
      throw new Error('Invalid evidence basis');
    named(submission.provenance.reference, 'provenance reference');
    named(submission.detail, 'evidence detail');
    if (submission.connectionId !== null &&
        !Object.values(world.parts[event.partId].connections).some(connection => connection.id === submission.connectionId))
      throw new Error(`Evidence connection does not belong to ${event.partId}: ${submission.connectionId}`);
    const capacityIds = uniqueNames(submission.capacityIds, 'capacity ID');
    for (const id of capacityIds) {
      if (!Object.hasOwn(inputs.capacities, id)) throw new Error(`Undeclared capacity: ${id}`);
    }
    const dependencies = uniqueNames(submission.dependencies, 'dependency ID');
    if (dependencies.includes(submission.id)) throw new Error(`Self-dependent evidence: ${submission.id}`);
    const assumptions = submission.provenance.assumptions ?? [];
    if (!Array.isArray(assumptions) || assumptions.some(value => typeof value !== 'string' || !value.trim()))
      throw new Error('Evidence assumptions must be nonempty strings');
    if ((submission.provenance.basis === 'assumed' || capacityBasis(inputs, capacityIds) === 'assumed') &&
        assumptions.length === 0) throw new Error('Assumed evidence needs an explicit assumption');
    const saved: EngineeringEvidence = freezeDeep(structuredClone({
      schemaVersion: 1 as const, ...context,
      id: submission.id, checkId: submission.checkId, connectionId: submission.connectionId,
      model: submission.model, status: submission.status,
      provenance: { basis: submission.provenance.basis,
        capacityBasis: capacityBasis(inputs, capacityIds), reference: submission.provenance.reference,
        assumptions: [...assumptions] },
      capacityIds, dependencies, detail: submission.detail,
    }));
    this.byId.set(saved.id, saved);
    return saved;
  }

  get(id: string): EngineeringEvidence | undefined { return this.byId.get(id); }
  list(): readonly EngineeringEvidence[] { return Object.freeze([...this.byId.values()]); }
}

function hold(requirementId: string, code: HoldCode, message: string, evidenceId?: string): GateHold {
  return evidenceId ? { requirementId, code, message, evidenceId } : { requirementId, code, message };
}

function connectionId(world: WorldState, event: ExecutionEvent, selector: ConnectionSelector): string | null {
  return selector === 'part' ? null : world.parts[event.partId].connections[selector].id;
}

function validateGate(gate: GateDefinition): void {
  named(gate.id, 'gate ID');
  named(gate.version, 'gate version');
  if (!Array.isArray(gate.requirements) || !gate.requirements.length)
    throw new Error(`Gate ${gate.id} needs requirements`);
  const ids = new Set<string>();
  for (const requirement of gate.requirements) {
    named(requirement.id, 'requirement ID');
    if (ids.has(requirement.id)) throw new Error(`Duplicate requirement ID: ${requirement.id}`);
    ids.add(requirement.id);
    named(requirement.checkId, 'requirement check ID');
    if (!['part', 'A', 'B'].includes(requirement.connection)) throw new Error('Invalid connection selector');
    modelIdentity(requirement.model);
    if (!Array.isArray(requirement.acceptedBases) || !requirement.acceptedBases.length ||
        requirement.acceptedBases.some((basis: EvidenceBasis) => !['measured', 'calculated', 'assumed'].includes(basis)))
      throw new Error(`Requirement ${requirement.id} needs accepted evidence bases`);
    if (!Array.isArray(requirement.acceptedCapacityBases) || !requirement.acceptedCapacityBases.length ||
        requirement.acceptedCapacityBases.some((basis: CapacityBasis) => !['measured', 'assumed', 'none'].includes(basis)))
      throw new Error(`Requirement ${requirement.id} needs accepted capacity bases`);
  }
}

function mismatches(evidence: EngineeringEvidence, context: ReturnType<typeof eventContext>,
  requiredConnectionId: string | null, requirement: GateRequirement): GateHold[] {
  const issue = (code: HoldCode, message: string) => hold(requirement.id, code, message, evidence.id);
  const holds: GateHold[] = [];
  if (evidence.worldRevision !== context.worldRevision)
    holds.push(issue('stale-revision', `world revision ${evidence.worldRevision}; need ${context.worldRevision}`));
  if (evidence.inputFingerprint !== context.inputFingerprint)
    holds.push(issue('fingerprint-mismatch', 'geometry, supports, loads, or capacities differ from the current world and inputs'));
  if (evidence.eventId !== context.eventId)
    holds.push(issue('event-mismatch', `event ${evidence.eventId}; need ${context.eventId}`));
  if (evidence.action !== context.action)
    holds.push(issue('action-mismatch', `action ${evidence.action}; need ${context.action}`));
  if (evidence.partId !== context.partId)
    holds.push(issue('part-mismatch', `part ${evidence.partId}; need ${context.partId}`));
  if (evidence.connectionId !== requiredConnectionId)
    holds.push(issue('connection-mismatch', `connection ${evidence.connectionId ?? 'part'}; need ${requiredConnectionId ?? 'part'}`));
  if (evidence.model.id !== requirement.model.id || evidence.model.version !== requirement.model.version)
    holds.push(issue('model-mismatch', `model ${evidence.model.id}@${evidence.model.version}; need ${requirement.model.id}@${requirement.model.version}`));
  if (evidence.model.scope !== requirement.model.scope)
    holds.push(issue('scope-mismatch', `scope ${evidence.model.scope}; need ${requirement.model.scope}`));
  if (!requirement.acceptedBases.includes(evidence.provenance.basis))
    holds.push(issue('basis-mismatch', `source basis ${evidence.provenance.basis} is not accepted`));
  if (!requirement.acceptedCapacityBases.includes(evidence.provenance.capacityBasis))
    holds.push(issue('capacity-basis-mismatch', `capacity basis ${evidence.provenance.capacityBasis} is not accepted`));
  return holds;
}

function dependencyHolds(registry: EvidenceRegistry, evidence: EngineeringEvidence,
  context: ReturnType<typeof eventContext>, requirement: GateRequirement,
  path = new Set<string>()): GateHold[] {
  if (path.has(evidence.id))
    return [hold(requirement.id, 'dependency-cycle', `dependency cycle at ${evidence.id}`, evidence.id)];
  path.add(evidence.id);
  const holds: GateHold[] = [];
  for (const id of evidence.dependencies) {
    const dependency = registry.get(id);
    if (!dependency) {
      holds.push(hold(requirement.id, 'dependency-missing', `missing dependency ${id}`, evidence.id));
      continue;
    }
    const sameContext = dependency.worldRevision === context.worldRevision &&
      dependency.inputFingerprint === context.inputFingerprint && dependency.eventId === context.eventId &&
      dependency.action === context.action && dependency.partId === context.partId;
    if (!sameContext || dependency.status !== 'passed' ||
        (dependency.provenance.capacityBasis === 'assumed' &&
          !requirement.acceptedCapacityBases.includes('assumed'))) {
      holds.push(hold(requirement.id, 'dependency-invalid',
        `dependency ${id} is ${dependency.status} or belongs to a different event, revision, fingerprint, part, or capacity basis`, id));
      continue;
    }
    holds.push(...dependencyHolds(registry, dependency, context, requirement, path));
  }
  path.delete(evidence.id);
  return holds;
}

/** Evaluate against the world before the event. Every named requirement must pass. */
export function evaluateEventGate(registry: EvidenceRegistry, world: WorldState, event: ExecutionEvent,
  inputs: EngineeringInputs, gate: GateDefinition): GateDecision {
  validateGate(gate);
  if (gate.action !== event.action) throw new Error(`Gate ${gate.id} does not apply to ${event.action}`);
  const context = eventContext(world, event, inputs);
  const holds: GateHold[] = [];
  const acceptedEvidenceIds: string[] = [];
  for (const requirement of gate.requirements) {
    const candidates = registry.list().filter(item => item.checkId === requirement.checkId);
    if (!candidates.length) {
      holds.push(hold(requirement.id, 'missing', `missing ${requirement.checkId} evidence for ${requirement.connection}`));
      continue;
    }
    const expectedConnection = connectionId(world, event, requirement.connection);
    const ranked = candidates.map(evidence => ({ evidence,
      issues: mismatches(evidence, context, expectedConnection, requirement) }));
    const exact = ranked.filter(candidate => candidate.issues.length === 0);
    if (!exact.length) {
      ranked.sort((a, b) => a.issues.length - b.issues.length || a.evidence.id.localeCompare(b.evidence.id));
      holds.push(...ranked[0].issues);
      continue;
    }
    for (const { evidence } of exact) {
      if (evidence.status !== 'passed') {
        holds.push(hold(requirement.id, evidence.status,
          `${requirement.checkId} evidence ${evidence.id} is ${evidence.status}: ${evidence.detail}`, evidence.id));
        continue;
      }
      const dependencyIssues = dependencyHolds(registry, evidence, context, requirement);
      holds.push(...dependencyIssues);
      if (!dependencyIssues.length) acceptedEvidenceIds.push(evidence.id);
    }
  }
  return freezeDeep({ gateId: gate.id, gateVersion: gate.version,
    eventId: context.eventId, worldRevision: context.worldRevision,
    inputFingerprint: context.inputFingerprint,
    allowed: holds.length === 0, holds, acceptedEvidenceIds });
}

export function formatGateHolds(decision: GateDecision): string {
  if (decision.allowed) return `${decision.gateId}@${decision.gateVersion}: allowed`;
  return `${decision.gateId}@${decision.gateVersion}: hold ${decision.holds
    .map(item => `${item.requirementId} [${item.code}] ${item.message}`).join('; ')}`;
}
