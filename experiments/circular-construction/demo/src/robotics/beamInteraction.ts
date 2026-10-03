/** Local guide-contact screen. SI, Z up, translation only; no structural/load approval. */
import type { RigidPart } from '../connectors/types';
import { capsuleIntersectsBox, add, sub, scale, dot, cross, length, mix, segmentDistance, rotateZ } from './math';
import { solveRobotPose } from './kinematics';
import type { CheckResult, Obstacle, RobotState, Vec3 } from './types';

export interface GuideTool {
  id: string;
  /** Fixed world direction from wrist to pad. Orientation is an input, not solved IK. */
  axis: Vec3;
  /** Wrist to spherical pad centre; sphere touches beam one radius farther forward. */
  extension: number;
  shaftRadius: number;
  padRadius: number;
}
export interface BeamSideContact {
  solidId: string;
  /** Coordinates on the named solid's +/-Y face, relative to beam centre. */
  point: Vec3;
  side: -1 | 1;
}
export interface InteractionWaypoint {
  wrist: Vec3;
  beamCenter: Vec3;
  /** Required throughout a segment when both endpoint flags are true. */
  contactRequired: boolean;
}
export interface BeamInteractionInput {
  robot: RobotState;
  limbIndex: number;
  beam: RigidPart;
  tool: GuideTool;
  contact: BeamSideContact;
  waypoints: InteractionWaypoint[];
  /** Explicit fixture/seat/closure solids. Do not omit a cheek to create access. */
  obstacles: Obstacle[];
  maxStep?: number;
  contactTolerance?: number;
  /** Nonnegative compression only. No suction, adhesion, friction or lifting inferred. */
  normalForceN: number;
}
export interface LocatedWrench { point: Vec3; force: Vec3; moment: Vec3; }
export interface ContactWrenchPair {
  onBeam: LocatedWrench;
  onTool: LocatedWrench;
  /** Same on-tool wrench transferred to wrist, including its lever arm. */
  atWrist: LocatedWrench;
}
export interface BeamInteractionResult {
  localGeometry: CheckResult;
  forceAndHost: CheckResult;
  sampleCount: number;
  finalGap: number | null;
  finalWrist: Vec3 | null;
  finalContact: Vec3 | null;
  /** Withheld whenever the specified geometric path fails. */
  contactWrenches: ContactWrenchPair | null;
}
const finiteVec = (p: readonly number[]): boolean => p.length === 3 && p.every(Number.isFinite);
const unique = (s: string[]): string[] => [...new Set(s)];
const placed = (beam: RigidPart, center: Vec3): Obstacle[] => beam.solids.map(s => ({
  id: s.id, min: add([...s.min], center), max: add([...s.max], center),
}));
const spherePenetrates = (center: Vec3, radius: number, box: Obstacle, tolerance: number): boolean => {
  const distance = Math.hypot(...center.map((v, i) => Math.max(box.min[i] - v, 0, v - box.max[i])));
  return distance < radius - tolerance;
};

/** A normal contact contributes zero free moment at its physical point. */
export function guideContactWrenches(point: Vec3, wrist: Vec3, outward: Vec3, forceN: number): ContactWrenchPair {
  if (![point, wrist, outward].every(finiteVec) || !Number.isFinite(forceN) || forceN < 0
    || Math.abs(length(outward) - 1) > 1e-8) throw new Error('Finite positions, unit normal and nonnegative compression required');
  const beamForce = scale(outward, -forceN), toolForce = scale(beamForce, -1);
  return {
    onBeam: { point: [...point], force: beamForce, moment: [0, 0, 0] },
    onTool: { point: [...point], force: toolForce, moment: [0, 0, 0] },
    atWrist: { point: [...wrist], force: toolForce, moment: cross(sub(point, wrist), toolForce) },
  };
}

/** Derive wrist from an actual named beam surface and finite tool; never use standoff as contact. */
export function wristForBeamContact(center: Vec3, contact: BeamSideContact, tool: GuideTool): Vec3 {
  return sub(add(center, contact.point), scale(tool.axis, tool.extension + tool.padRadius));
}

export function screenBeamInteraction(input: BeamInteractionInput): BeamInteractionResult {
  const { robot, beam, contact, tool, limbIndex } = input;
  const reasons: string[] = [];
  const step = input.maxStep ?? 0.01, tolerance = input.contactTolerance ?? 1e-6;
  const forceAndHost: CheckResult = { status: 'unverified', scope: 'contact forces, wrist orientation/actuation, grips, beam, connector and host structure', reasons: [
    'Specified normal force is a demand, not a solved reaction or measured capacity',
    'Frictionless side pad cannot pull, lift, restrain all six beam degrees of freedom, or replace hoist custody',
    'Robot support reactions, tool compliance, dynamics, frame and foundation response require independent coupled validation',
  ] };
  const finish = (count: number, gap: number | null, final: InteractionWaypoint | null): BeamInteractionResult => ({
    localGeometry: { status: reasons.length ? 'fail' : 'pass', scope: 'sampled fixed-body/fixed-support IK, specified boxes, tool solids and beam-side contact', reasons: unique(reasons) },
    forceAndHost, sampleCount: count, finalGap: gap, finalWrist: final ? [...final.wrist] : null,
    finalContact: final ? add(final.beamCenter, contact.point) : null,
    contactWrenches: !reasons.length && final ? guideContactWrenches(add(final.beamCenter, contact.point), final.wrist, [0, contact.side, 0], input.normalForceN) : null,
  });
  const surface = beam.solids.find(s => s.id === contact.solidId);
  if (!surface || !finiteVec(contact.point) || ![-1, 1].includes(contact.side)
    || !finiteVec(tool.axis) || Math.abs(length(tool.axis) - 1) > 1e-8
    || dot(tool.axis, [0, -contact.side, 0]) < 1 - 1e-8
    || ![tool.extension, tool.shaftRadius, tool.padRadius, step].every(v => Number.isFinite(v) && v > 0)
    || tool.shaftRadius > tool.padRadius || !Number.isFinite(tolerance) || tolerance < 0 || tolerance > 0.001
    || !Number.isFinite(input.normalForceN) || input.normalForceN < 0
    || beam.solids.length === 0 || beam.solids.some(s => !finiteVec(s.min) || !finiteVec(s.max) || s.min.some((v, i) => v >= s.max[i]))
    || input.obstacles.some(s => !finiteVec(s.min) || !finiteVec(s.max) || s.min.some((v, i) => v >= s.max[i]))
    || input.waypoints.length < 2 || input.waypoints.some(p => !finiteVec(p.wrist) || !finiteVec(p.beamCenter))) {
    reasons.push('Invalid finite beam/tool/surface/path geometry or compressive force demand');
    return finish(0, null, null);
  }
  const faceY = contact.side === -1 ? surface.min[1] : surface.max[1];
  if (Math.abs(contact.point[1] - faceY) > tolerance
    || [0, 2].some(i => contact.point[i] - tool.padRadius < surface.min[i] || contact.point[i] + tool.padRadius > surface.max[i]))
    reasons.push('Contact is not on the named beam face with a full pad-radius edge margin');
  const arm = robot.limbs[limbIndex];
  if (!arm || !arm.tool || arm.anchor || arm.mode !== 'tooling' || robot.motion)
    reasons.push('An idle robot with a detached tooling limb is required');
  const supports = robot.limbs.filter(l => l.index !== limbIndex);
  if (supports.length !== 3 || supports.some(l => l.mode !== 'load_verified' || !l.anchor?.available || length(sub(l.position, l.anchor.position)) > tolerance))
    reasons.push('Exactly three available verified anchors must coincide with fixed support wrists');
  if (arm && length(sub(input.waypoints[0].wrist, arm.position)) > tolerance)
    reasons.push('Approach must begin at the supplied robot wrist; no teleport to the contact');
  if (!input.waypoints.at(-1)!.contactRequired) reasons.push('The final waypoint must require physical contact');
  if (reasons.length) return finish(0, null, null);

  const candidate = structuredClone(robot);
  let count = 0, gap: number | null = null;
  for (let segment = 1; segment < input.waypoints.length; segment++) {
    const a = input.waypoints[segment - 1], b = input.waypoints[segment];
    const n = Math.max(1, Math.ceil(Math.max(length(sub(b.wrist, a.wrist)), length(sub(b.beamCenter, a.beamCenter))) / step));
    for (let i = segment === 1 ? 0 : 1; i <= n; i++) {
      const sample = { wrist: mix(a.wrist, b.wrist, i / n), beamCenter: mix(a.beamCenter, b.beamCenter, i / n),
        contactRequired: (a.contactRequired && b.contactRequired) || (i === n && b.contactRequired) };
      count++;
      candidate.limbs[limbIndex].position = sample.wrist;
      const solids = placed(beam, sample.beamCenter), pose = solveRobotPose(candidate, [...input.obstacles, ...solids]);
      reasons.push(...pose.check.reasons.map(r => `Sample ${count}: ${r}`));
      const pad = add(sample.wrist, scale(tool.axis, tool.extension));
      const physicalPoint = add(pad, scale(tool.axis, tool.padRadius));
      const desiredPoint = add(sample.beamCenter, contact.point);
      gap = dot(sub(physicalPoint, desiredPoint), [0, contact.side, 0]);
      if (sample.contactRequired && length(sub(physicalPoint, desiredPoint)) > tolerance)
        reasons.push(`Sample ${count}: pad misses the physical beam contact by ${length(sub(physicalPoint, desiredPoint)).toFixed(4)} m`);
      for (const box of input.obstacles) {
        if (capsuleIntersectsBox(sample.wrist, pad, tool.shaftRadius, box) || spherePenetrates(pad, tool.padRadius, box, 0))
          reasons.push(`Sample ${count}: tool intersects ${box.id}`);
      }
      for (const box of solids) {
        // Shaft ends at pad centre and stays behind the spherical contact surface.
        if (capsuleIntersectsBox(sample.wrist, pad, tool.shaftRadius, box) || spherePenetrates(pad, tool.padRadius, box, tolerance))
          reasons.push(`Sample ${count}: tool penetrates beam solid ${box.id}`);
      }
      const local = (p: Vec3): Vec3 => rotateZ(sub(p, candidate.position), -candidate.yaw);
      const c = candidate.config;
      if (capsuleIntersectsBox(local(sample.wrist), local(pad), tool.padRadius,
        { id: 'torso', min: [-c.bodyWidth / 2, -c.bodyDepth / 2, -c.bodyHeight / 2], max: [c.bodyWidth / 2, c.bodyDepth / 2, c.bodyHeight / 2] }))
        reasons.push(`Sample ${count}: tool intersects torso`);
      for (const [index, limb] of pose.limbs.entries()) {
        const foreEnd = index === limbIndex ? mix(limb.wrist, limb.elbow, Math.min(1, (c.linkRadius + tool.shaftRadius) * 1.05 / c.foreLength)) : limb.wrist;
        for (const [start, end] of [[limb.shoulder, limb.elbow], [limb.elbow, foreEnd]] as [Vec3, Vec3][])
          if (segmentDistance(sample.wrist, pad, start, end) < tool.shaftRadius + c.linkRadius
            || segmentDistance(pad, pad, start, end) < tool.padRadius + c.linkRadius)
            reasons.push(`Sample ${count}: tool intersects limb ${index + 1} outside wrist coupling`);
      }
    }
  }
  return finish(count, gap, input.waypoints.at(-1)!);
}
