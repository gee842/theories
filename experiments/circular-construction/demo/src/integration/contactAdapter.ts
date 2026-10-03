/**
 * Fixed-pose bridge from RobotState to numerical/contact_solver.py contract v1.
 * The result is local contact equilibrium evidence, never a beam transaction or
 * supporting-frame approval. Joint resultant moments are conservatively bounded
 * for self-weight only; wrist transmission/orientation and dynamics are unverified.
 */
import { solveRobotPose, TOOL_DOCK_OFFSET } from '../robotics/kinematics';
import { add, cross, mix, rotateZ, sub } from '../robotics/math';
import type { CheckResult, RobotState, Vec3 } from '../robotics/types';

export type ContactKind = 'point' | 'keyed';
export type ContactSolverStatus = 'passed' | 'failed' | 'unverified';

export interface ContactLoad {
  id: string;
  mass_kg?: number;
  position_m: Vec3;
  force_N?: Vec3;
  moment_Nm?: Vec3;
}

export interface ContactBounds {
  lower: [number | null, number | null, number | null];
  upper: [number | null, number | null, number | null];
}

export interface ActuatorConstraint {
  id: string;
  gravity_torque_Nm: number;
  wrench_coefficients: { contact_id: string; force_to_torque_m: Vec3; moment_to_torque: Vec3 }[];
  lower_Nm: number | null;
  upper_Nm: number | null;
}

export interface ContactRequest {
  schema_version: 1;
  request_id: string;
  world_revision: number;
  input_fingerprint: string;
  gravity_m_s2: Vec3;
  loads: ContactLoad[];
  contacts: {
    id: string;
    position_m: Vec3;
    kind: ContactKind;
    force_bounds_N: ContactBounds;
    moment_bounds_Nm?: ContactBounds;
  }[];
  require_actuator_limits: true;
  actuator_constraints: ActuatorConstraint[];
  adapter_context: {
    version: 'robot-fixed-pose/2';
    robot_id: string;
    body_position_m: Vec3;
    yaw_rad: number;
    limbs: { index: number; wrist_position_m: Vec3; mode: string; anchor_id: string | null; tool: boolean }[];
    contact_kind: ContactKind;
    capacity_source: 'assumed' | 'measured';
    declared_grip_force_limit_N: number | null;
    declared_grip_moment_limit_Nm: number | null;
    declared_shoulder_torque_limit_Nm: number | null;
    declared_elbow_torque_limit_Nm: number | null;
    actuator_rows: 'self-weight-resultant-box' | 'missing-external-load-attachment';
    external_loads_complete: boolean;
    load_scope: string;
    pose_geometry: CheckResult;
    source_geometry: CheckResult | null;
  };
}

export interface ContactRequestOptions {
  requestId: string;
  worldRevision: number;
  /** Point contacts prove geometric mechanisms; keyed contacts use declared couple boxes. */
  contactKind?: ContactKind;
  /** Additional known fixed-pose forces/couples. Weight belongs in mass_kg, not force_N. */
  externalLoads?: ContactLoad[];
  /** True only when all external loads relevant to this isolated robot pose are supplied. */
  externalLoadsComplete: boolean;
  /** For example, "robot self-weight at beam-end standoff, no beam contact". */
  loadScope: string;
  /** Earlier sampled collision/stance evidence, when this pose came from a task trace. */
  sourceGeometry?: CheckResult;
}

export interface ContactSolverResult {
  schema_version?: unknown;
  request_id?: unknown;
  world_revision?: unknown;
  input_fingerprint?: unknown;
  request_sha256?: unknown;
  model_version?: unknown;
  status?: unknown;
  reason?: unknown;
  solver?: { status?: unknown };
  actuator_status?: unknown;
  missing_capacities?: unknown;
  equilibrium_residual?: { max_abs?: unknown } | null;
  max_bound_violation?: unknown;
}

export interface ContactAssessment extends CheckResult {
  stale: boolean;
  solverStatus: ContactSolverStatus | 'invalid';
  worldRevision: number;
  inputFingerprint: string;
}

const cloneVec = (point: Vec3): Vec3 => [...point];
const finiteVec = (point: readonly number[]): boolean => point.length === 3 && point.every(Number.isFinite);
const validMass = (mass: number): boolean => Number.isFinite(mass) && mass >= 0;
const LIMIT_DIVISOR = Math.sqrt(3);

function boundsFromMagnitude(limit: number | null): ContactBounds {
  // An axis-aligned box of ±L/sqrt(3) stays inside an assumed Euclidean L ball.
  // This is conservative; the solver does not model the actual coupled ball.
  if (limit !== null && (!Number.isFinite(limit) || limit < 0))
    throw new Error('Declared capacity must be finite and nonnegative or null');
  const axis = limit === null ? null : limit / LIMIT_DIVISOR;
  return { lower: axis === null ? [null, null, null] : [-axis, -axis, -axis], upper: [axis, axis, axis] };
}

/** Resultant moment on the distal free body. The motor reaction has the opposite
 * sign, immaterial for symmetric limits. Cartesian rows conservatively bound the
 * full moment norm; for the elbow this also bounds its hinge-axis projection.
 * Body/docked-tool weight acts upstream and enters through contact equilibrium.
 */
function selfWeightActuatorRows(state: RobotState, pose: ReturnType<typeof solveRobotPose>,
  contacts: ContactRequest['contacts']): ActuatorConstraint[] {
  const c = state.config;
  const rows: ActuatorConstraint[] = [];
  for (const limb of state.limbs) {
    const p = pose.limbs[limb.index];
    const contact = limb.mode === 'load_verified' && limb.anchor
      ? contacts.find(item => item.id === `${state.id}:${limb.anchor!.id}`) : undefined;
    const upperCenter = mix(p.shoulder, p.elbow, 0.5);
    const foreCenter = mix(p.elbow, p.wrist, 0.5);
    const tipMass = c.clampMass + (limb.tool ? c.toolMass : 0);
    for (const joint of ['shoulder', 'elbow'] as const) {
      const origin = p[joint];
      let gravity = add(cross(sub(foreCenter, origin), [0, 0, -9.81 * c.foreMass]),
        cross(sub(p.wrist, origin), [0, 0, -9.81 * tipMass]));
      if (joint === 'shoulder') gravity = add(gravity,
        cross(sub(upperCenter, origin), [0, 0, -9.81 * c.upperMass]));
      const limit = joint === 'shoulder' ? c.shoulderTorqueLimit : c.elbowTorqueLimit;
      const bounds = boundsFromMagnitude(limit);
      for (let axis = 0; axis < 3; axis++) {
        const unit: Vec3 = [0, 0, 0];
        unit[axis] = 1;
        // e · (r × F) = (e × r) · F. Empty coefficients are a free-arm constant row.
        rows.push({ id: `${state.id}:limb-${limb.index}:${joint}:${'xyz'[axis]}`,
          gravity_torque_Nm: gravity[axis],
          wrench_coefficients: contact ? [{ contact_id: contact.id,
            force_to_torque_m: cross(unit, sub(p.wrist, origin)), moment_to_torque: unit }] : [],
          lower_Nm: bounds.lower[axis], upper_Nm: bounds.upper[axis] });
      }
    }
  }
  return rows;
}

function sorted(value: unknown): unknown {
  if (Array.isArray(value)) return value.map(sorted);
  if (value !== null && typeof value === 'object')
    return Object.fromEntries(Object.entries(value).sort(([a], [b]) => a < b ? -1 : a > b ? 1 : 0).map(([key, item]) => [key, sorted(item)]));
  return value;
}

async function sha256Text(serialized: string): Promise<string> {
  const bytes = new TextEncoder().encode(serialized);
  const digest = await globalThis.crypto.subtle.digest('SHA-256', bytes);
  return Array.from(new Uint8Array(digest), byte => byte.toString(16).padStart(2, '0')).join('');
}

const sha256 = (value: unknown): Promise<string> => sha256Text(JSON.stringify(sorted(value)));

/** Match Python json.dumps(sort_keys=True, separators=(',', ':'), ensure_ascii=True).
 * JSON from this adapter is passed through JS JSON.stringify before Python
 * loads it. Python therefore reads integer tokens as ints and decimal/exponent
 * tokens as floats; small floats need Python's exponent spelling for its hash. */
function pythonCanonical(value: unknown): string {
  if (value === null) return 'null';
  if (typeof value === 'number') {
    if (!Number.isFinite(value)) throw new Error('Contact request contains a nonfinite number');
    const token = JSON.stringify(value);
    if (!/[.eE]/.test(token) || value === 0 || Math.abs(value) >= 1e-4 && Math.abs(value) < 1e16) return token;
    return value.toExponential().replace(/e([+-]?)(\d+)$/, (_match, sign: string, digits: string) =>
      `e${sign || '+'}${digits.padStart(2, '0')}`);
  }
  if (typeof value === 'string') return JSON.stringify(value).replace(/[\u007f-\uffff]/g,
    character => `\\u${character.charCodeAt(0).toString(16).padStart(4, '0')}`);
  if (typeof value === 'boolean') return value ? 'true' : 'false';
  if (Array.isArray(value)) return `[${value.map(item => pythonCanonical(item ?? null)).join(',')}]`;
  if (typeof value === 'object') return `{${Object.entries(value).filter(([, item]) => item !== undefined)
    .sort(([a], [b]) => a < b ? -1 : a > b ? 1 : 0)
    .map(([key, item]) => `${pythonCanonical(key)}:${pythonCanonical(item)}`).join(',')}}`;
  throw new Error('Contact request contains unsupported JSON data');
}

function withoutFingerprint(request: ContactRequest): Omit<ContactRequest, 'input_fingerprint'> {
  const { input_fingerprint: _fingerprint, ...body } = request;
  return body;
}

function checkLoad(load: ContactLoad): void {
  if (!load.id || !finiteVec(load.position_m) || (load.mass_kg !== undefined && !validMass(load.mass_kg)) ||
    (load.force_N !== undefined && !finiteVec(load.force_N)) || (load.moment_Nm !== undefined && !finiteVec(load.moment_Nm)))
    throw new Error(`Invalid fixed-pose load ${load.id || '(unnamed)'}`);
}

/** Build a self-contained, versioned solver request from one immutable fixed pose. */
export async function createContactRequest(state: RobotState, options: ContactRequestOptions): Promise<ContactRequest> {
  if (!options.requestId || !Number.isInteger(options.worldRevision) || options.worldRevision < 0 || !options.loadScope)
    throw new Error('Contact request needs a nonempty ID, world revision, and load scope');
  if (typeof options.externalLoadsComplete !== 'boolean')
    throw new Error('External-load completeness must be declared');
  if (state.motion || !finiteVec(state.position) || !Number.isFinite(state.yaw) || state.limbs.length !== 4)
    throw new Error('Contact request requires a fixed four-limb RobotState pose');
  if (new Set(state.limbs.map(limb => limb.index)).size !== 4 ||
    state.limbs.some((limb, index) => limb.index !== index))
    throw new Error('Contact request requires limb indices 0–3 in array order');
  if (state.limbs.some(limb => limb.mode === 'load_verified' && !limb.anchor))
    throw new Error('Every load-verified limb needs a fixed anchor');
  const c = state.config;
  for (const mass of [c.bodyMass, c.upperMass, c.foreMass, c.clampMass, c.toolMass])
    if (!validMass(mass)) throw new Error('Robot mass distribution must be finite and nonnegative');
  const pose = solveRobotPose(state);
  if (pose.check.status !== 'pass') throw new Error(`Robot pose geometry is not checked: ${pose.check.reasons.join('; ')}`);
  const loads: ContactLoad[] = [{ id: `${state.id}:body`, mass_kg: c.bodyMass, position_m: cloneVec(state.position) }];
  for (const limb of state.limbs) {
    const p = pose.limbs[limb.index];
    if (!p || !finiteVec(limb.position)) throw new Error(`Invalid limb ${limb.index}`);
    loads.push({ id: `${state.id}:upper-${limb.index}`, mass_kg: c.upperMass, position_m: mix(p.shoulder, p.elbow, 0.5) });
    loads.push({ id: `${state.id}:fore-${limb.index}`, mass_kg: c.foreMass, position_m: mix(p.elbow, p.wrist, 0.5) });
    loads.push({ id: `${state.id}:clamp-${limb.index}`, mass_kg: c.clampMass, position_m: cloneVec(p.wrist) });
  }
  const toolLimbs = state.limbs.filter(limb => limb.tool);
  if (toolLimbs.length > 1 || (state.toolDocked && toolLimbs.length) || (!state.toolDocked && !toolLimbs.length))
    throw new Error('Tool custody must identify exactly one carried tool or the body dock');
  const toolPosition = toolLimbs[0]?.position ?? add(state.position, rotateZ(TOOL_DOCK_OFFSET, state.yaw));
  loads.push({ id: `${state.id}:tool`, mass_kg: c.toolMass, position_m: cloneVec(toolPosition) });
  for (const load of options.externalLoads ?? []) checkLoad(load);
  loads.push(...structuredClone(options.externalLoads ?? []));
  if (new Set(loads.map(load => load.id)).size !== loads.length) throw new Error('Fixed-pose load IDs must be unique');

  const kind = options.contactKind ?? 'keyed';
  if (kind !== 'point' && kind !== 'keyed') throw new Error('Contact kind must be point or keyed');
  const contacts = state.limbs.filter(limb => limb.mode === 'load_verified' && limb.anchor).map(limb => {
    const anchor = limb.anchor!;
    if (!anchor.available || !finiteVec(anchor.position) ||
      anchor.position.some((coordinate, axis) => Math.abs(coordinate - limb.position[axis]) > 1e-8))
      throw new Error(`Grip ${limb.index} has no fixed, available anchor at its wrist`);
    return {
      id: `${state.id}:${anchor.id}`,
      position_m: cloneVec(anchor.position),
      kind,
      force_bounds_N: boundsFromMagnitude(c.gripForceLimit),
      ...(kind === 'keyed' ? { moment_bounds_Nm: boundsFromMagnitude(c.gripMomentLimit) } : {}),
    };
  });
  if (!contacts.length || new Set(contacts.map(contact => contact.id)).size !== contacts.length)
    throw new Error('Contact request needs unique, verified fixed anchors');
  // External-load positions alone do not identify the affected link/joint chain.
  // Do not apply self-weight-only joint rows when omitted loads could aid or oppose them.
  const actuatorRows = options.externalLoads?.length ? [] : selfWeightActuatorRows(state, pose, contacts);
  const request: ContactRequest = {
    schema_version: 1, request_id: options.requestId, world_revision: options.worldRevision, input_fingerprint: '',
    gravity_m_s2: [0, 0, -9.81], loads, contacts, require_actuator_limits: true, actuator_constraints: actuatorRows,
    adapter_context: {
      version: 'robot-fixed-pose/2', robot_id: state.id, body_position_m: cloneVec(state.position), yaw_rad: state.yaw,
      limbs: state.limbs.map(limb => ({ index: limb.index, wrist_position_m: cloneVec(limb.position), mode: limb.mode,
        anchor_id: limb.anchor?.id ?? null, tool: limb.tool })),
      contact_kind: kind, capacity_source: c.capacitySource,
      declared_grip_force_limit_N: c.gripForceLimit, declared_grip_moment_limit_Nm: c.gripMomentLimit,
      declared_shoulder_torque_limit_Nm: c.shoulderTorqueLimit, declared_elbow_torque_limit_Nm: c.elbowTorqueLimit,
      actuator_rows: actuatorRows.length ? 'self-weight-resultant-box' : 'missing-external-load-attachment', external_loads_complete: options.externalLoadsComplete, load_scope: options.loadScope,
      pose_geometry: pose.check, source_geometry: options.sourceGeometry ? structuredClone(options.sourceGeometry) : null,
    },
  };
  request.input_fingerprint = `sha256:${await sha256(withoutFingerprint(request))}`;
  return request;
}

/** Rebuild currentRequest from the current pose/world before accepting an asynchronous result. */
export async function assessContactResult(issuedRequest: ContactRequest, result: ContactSolverResult | null,
  currentRequest: ContactRequest): Promise<ContactAssessment> {
  const base = { scope: 'conditional fixed-pose declared-load contact/actuator box model; assumed capacities; wrist, dynamics and host rail unverified',
    worldRevision: currentRequest.world_revision, inputFingerprint: currentRequest.input_fingerprint };
  const unverified = (reason: string, stale = false): ContactAssessment => ({ ...base, status: 'unverified',
    reasons: [reason], stale, solverStatus: 'invalid' });
  if (issuedRequest.input_fingerprint !== `sha256:${await sha256(withoutFingerprint(issuedRequest))}` ||
    currentRequest.input_fingerprint !== `sha256:${await sha256(withoutFingerprint(currentRequest))}`)
    return unverified('Request fingerprint no longer matches its fixed-pose inputs', true);
  if (issuedRequest.world_revision !== currentRequest.world_revision ||
    issuedRequest.input_fingerprint !== currentRequest.input_fingerprint)
    return unverified('Solver result is stale for the current world revision or pose inputs', true);
  if (!result || result.schema_version !== 1 || result.model_version !== 'contact-box-static/1.0.0' ||
    result.request_id !== issuedRequest.request_id || result.world_revision !== issuedRequest.world_revision ||
    result.input_fingerprint !== issuedRequest.input_fingerprint ||
    result.request_sha256 !== await sha256Text(pythonCanonical(issuedRequest)))
    return unverified('Solver result identity or canonical request hash does not match the issued request', true);
  if (!['passed', 'failed', 'unverified'].includes(String(result.status))) return unverified('Solver returned no recognized status');
  const solverStatus = result.status as ContactSolverStatus;
  if (solverStatus === 'failed' && result.solver?.status === 'infeasible' && issuedRequest.adapter_context.external_loads_complete)
    return { ...base, status: 'fail', reasons: [String(result.reason ?? 'Declared contact model is infeasible'),
      'Infeasible under conservative boxes; this alone does not prove physical infeasibility under the original norm limits'], stale: false, solverStatus };
  if (solverStatus === 'passed' && issuedRequest.adapter_context.external_loads_complete &&
    issuedRequest.adapter_context.actuator_rows === 'self-weight-resultant-box' &&
    result.solver?.status === 'feasible' && result.actuator_status === 'included' &&
    Array.isArray(result.missing_capacities) && result.missing_capacities.length === 0 &&
    typeof result.equilibrium_residual?.max_abs === 'number' && Number.isFinite(result.equilibrium_residual.max_abs) &&
    result.equilibrium_residual.max_abs >= 0 && result.equilibrium_residual.max_abs <= 1e-7 &&
    typeof result.max_bound_violation === 'number' && Number.isFinite(result.max_bound_violation) &&
    result.max_bound_violation >= 0 && result.max_bound_violation <= 1e-7)
    return { ...base, status: 'pass', reasons: ['Conditional self-weight witness satisfies conservative contact and shoulder/elbow bounds; no beam-guiding or hardware approval'],
      stale: false, solverStatus };
  const reasons = [String(result.reason ?? 'Contact solver could not verify the fixed pose')];
  if (!issuedRequest.adapter_context.external_loads_complete) reasons.push('Relevant external loads are not fully specified');
  if (issuedRequest.adapter_context.actuator_rows === 'missing-external-load-attachment')
    reasons.push('External loads lack link attachment information; actuator effects are unverified');
  if (solverStatus === 'passed') reasons.push('A passed solver label alone does not establish the complete scoped fixed-pose check');
  return { ...base, status: 'unverified', reasons, stale: false, solverStatus };
}
