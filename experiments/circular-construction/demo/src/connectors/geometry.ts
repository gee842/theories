import type {
  Box, ClearanceEnvelope, ConnectorMotionInput, ConnectorMotionScreen, Obstacle,
  OpenSeat, PathCheckInput, PathScreen, RigidPart, ScreeningIssue, Vec3,
} from './types';

const EPS = 1e-9;

function validNumber(value: number): boolean { return Number.isFinite(value); }
function validVec(v: Vec3): boolean { return v.length === 3 && v.every(validNumber); }
function isSegment(value: Obstacle): value is Extract<Obstacle, { start: Vec3 }> {
  return 'start' in value;
}
function validBox(box: Box): boolean {
  return validVec(box.min) && validVec(box.max) && box.min.every((v, i) => v < box.max[i]);
}
function validObstacle(item: Obstacle): boolean {
  return isSegment(item)
    ? validVec(item.start) && validVec(item.end) && validNumber(item.radius) && item.radius >= 0
    : validBox(item);
}
function validEnvelope(e: ClearanceEnvelope): boolean {
  return validVec(e.poseError) && validVec(e.partError)
    && e.poseError.every(v => v >= 0) && e.partError.every(v => v >= 0)
    && [e.obstacleClearance, e.seatClearance, e.floorContactError].every(v => validNumber(v) && v >= 0);
}

function translate(box: Box, p: Vec3): Box {
  return { id: box.id, min: [box.min[0] + p[0], box.min[1] + p[1], box.min[2] + p[2]],
    max: [box.max[0] + p[0], box.max[1] + p[1], box.max[2] + p[2]] };
}

function expanded(box: Box, e: Vec3): Box {
  return { id: box.id, min: [box.min[0] - e[0], box.min[1] - e[1], box.min[2] - e[2]],
    max: [box.max[0] + e[0], box.max[1] + e[1], box.max[2] + e[2]] };
}

function boxesOverlap(a: Box, b: Box): boolean {
  return a.min.every((v, i) => v < b.max[i] - EPS && a.max[i] > b.min[i] + EPS);
}

/** Slab intersection of a centreline with an AABB expanded by tube radius. */
function segmentHitsBox(start: Vec3, end: Vec3, box: Box, radius: number): boolean {
  const bounds = expanded(box, [radius, radius, radius]);
  let enter = 0, exit = 1;
  for (let axis = 0; axis < 3; axis += 1) {
    const delta = end[axis] - start[axis];
    if (Math.abs(delta) < EPS) {
      if (start[axis] <= bounds.min[axis] + EPS || start[axis] >= bounds.max[axis] - EPS) return false;
      continue;
    }
    const a = (bounds.min[axis] - start[axis]) / delta;
    const b = (bounds.max[axis] - start[axis]) / delta;
    enter = Math.max(enter, Math.min(a, b));
    exit = Math.min(exit, Math.max(a, b));
    if (enter >= exit - EPS) return false;
  }
  return true;
}

function pathSamples(path: readonly Vec3[], maxStep: number): Vec3[] {
  const poses: Vec3[] = [path[0]];
  for (let i = 1; i < path.length; i += 1) {
    const a = path[i - 1], b = path[i];
    const length = Math.hypot(b[0] - a[0], b[1] - a[1], b[2] - a[2]);
    const steps = Math.max(1, Math.ceil(length / maxStep));
    for (let j = 1; j <= steps; j += 1) {
      const t = j / steps;
      poses.push([a[0] + (b[0] - a[0]) * t, a[1] + (b[1] - a[1]) * t,
        a[2] + (b[2] - a[2]) * t]);
    }
  }
  return poses;
}

function invalidInput(path: readonly Vec3[], moving: RigidPart, obstacles: readonly Obstacle[],
  envelope: ClearanceEnvelope, maxSampleStep: number): string | null {
  if (path.length < 2 || !path.every(validVec)) return 'Path requires at least two finite three-axis poses.';
  if (!validNumber(maxSampleStep) || maxSampleStep <= 0) return 'Sample step must be positive and finite.';
  if (!validEnvelope(envelope)) return 'Clearance envelope must be finite and nonnegative.';
  if (moving.solids.length === 0 || moving.solids.some(s => !validBox(s))) return 'Moving solids must be nonempty valid boxes.';
  if (obstacles.some(o => !validObstacle(o))) return 'Obstacles must be valid boxes or line segments.';
  return null;
}

export function screenRigidPath(input: PathCheckInput): PathScreen {
  const error = invalidInput(input.path, input.moving, input.obstacles, input.envelope, input.maxSampleStep);
  if (error) return { status: 'failed', sampleCount: 0, issues: [{ code: 'invalid-input', detail: error }] };
  const poses = pathSamples(input.path, input.maxSampleStep);
  const expansion: Vec3 = [0, 1, 2].map(i => input.envelope.poseError[i]
    + input.envelope.partError[i] + input.envelope.obstacleClearance) as unknown as Vec3;
  const issues: ScreeningIssue[] = [];
  for (let sample = 0; sample < poses.length; sample += 1) {
    for (const solid of input.moving.solids) {
      const world = expanded(translate(solid, poses[sample]), expansion);
      for (const obstacle of input.obstacles) {
        const hit = isSegment(obstacle)
          ? segmentHitsBox(obstacle.start, obstacle.end, world, obstacle.radius)
          : boxesOverlap(world, obstacle);
        if (hit) issues.push({ code: 'collision', detail: `${solid.id} intersects the reserved clearance of ${obstacle.id}.`,
          sample, movingSolidId: solid.id, obstacleId: obstacle.id });
      }
    }
  }
  return { status: issues.length ? 'failed' : 'passed', sampleCount: poses.length, issues };
}

function validSeat(seat: OpenSeat): boolean {
  return validVec(seat.center) && [seat.floorZ, seat.insideLength, seat.throatWidth, seat.mouthWidth,
    seat.leadInHeight, seat.openingError].every(validNumber)
    && seat.insideLength > 0 && seat.throatWidth > 0 && seat.mouthWidth >= seat.throatWidth
    && seat.leadInHeight > 0 && seat.openingError >= 0
    && Math.abs(seat.center[2] - seat.floorZ) < EPS;
}

function seatIssues(poses: readonly Vec3[], input: ConnectorMotionInput):
  { issues: ScreeningIssue[]; minimumMargin: number | null } {
  const issues: ScreeningIssue[] = [];
  let minimumMargin: number | null = null;
  const seatedPose = input.operation === 'guide' ? poses[poses.length - 1] : poses[0];
  for (const seat of input.seats) {
    const shoe = input.member.solids.find(s => s.id === seat.shoeId);
    if (!shoe) {
      issues.push({ code: 'invalid-input', detail: `Seat ${seat.id} references missing shoe ${seat.shoeId}.`, seatId: seat.id });
      continue;
    }
    const seatedBottom = seatedPose[2] + shoe.min[2];
    if (Math.abs(seatedBottom - seat.floorZ) > input.envelope.floorContactError + EPS) {
      issues.push({ code: 'seat-contact', detail: `${seat.id} shoe bottom is not at its seat floor.`, seatId: seat.id });
    }
    for (let sample = 0; sample < poses.length; sample += 1) {
      const pose = poses[sample];
      const bottom = pose[2] + shoe.min[2];
      if (bottom > seat.floorZ + seat.leadInHeight + EPS) continue;
      if (bottom < seat.floorZ - input.envelope.floorContactError - EPS) {
        issues.push({ code: 'seat-fit', detail: `${seat.id} shoe penetrates the seat floor.`, sample, seatId: seat.id });
        continue;
      }
      const rise = Math.max(0, Math.min(1, (bottom - seat.floorZ) / seat.leadInHeight));
      const openingWidth = seat.throatWidth + (seat.mouthWidth - seat.throatWidth) * rise - 2 * seat.openingError;
      const openingLength = seat.insideLength - 2 * seat.openingError;
      const shoeWidth = shoe.max[1] - shoe.min[1] + 2 * input.envelope.partError[1];
      const shoeLength = shoe.max[0] - shoe.min[0] + 2 * input.envelope.partError[0];
      const shoeX = pose[0] + (shoe.min[0] + shoe.max[0]) / 2;
      const shoeY = pose[1] + (shoe.min[1] + shoe.max[1]) / 2;
      const xMargin = (openingLength - shoeLength) / 2
        - Math.abs(shoeX - seat.center[0]) - input.envelope.poseError[0];
      const yMargin = (openingWidth - shoeWidth) / 2
        - Math.abs(shoeY - seat.center[1]) - input.envelope.poseError[1];
      const margin = Math.min(xMargin, yMargin);
      minimumMargin = minimumMargin === null ? margin : Math.min(minimumMargin, margin);
      if (margin + EPS < input.envelope.seatClearance) {
        issues.push({ code: 'seat-fit', detail: `${seat.id} worst-case shoe margin ${margin.toFixed(4)} m is below required ${input.envelope.seatClearance.toFixed(4)} m.`,
          sample, seatId: seat.id });
      }
      // The full-depth member overlaps the inner part of both seats. Its X span
      // is not constrained to a single seat, but it must clear each cheek pair.
      for (const solid of input.member.solids) {
        if (solid.id === shoe.id) continue;
        const minX = pose[0] + solid.min[0], maxX = pose[0] + solid.max[0];
        const minZ = pose[2] + solid.min[2], maxZ = pose[2] + solid.max[2];
        const minY = pose[1] + solid.min[1], maxY = pose[1] + solid.max[1];
        const insideFloorFootprint = minX < seat.center[0] + seat.insideLength / 2
          && maxX > seat.center[0] - seat.insideLength / 2
          && minY < seat.center[1] + seat.mouthWidth / 2
          && maxY > seat.center[1] - seat.mouthWidth / 2;
        if (insideFloorFootprint && minZ < seat.floorZ - input.envelope.floorContactError - EPS) {
          issues.push({ code: 'seat-fit', detail: `${solid.id} penetrates the floor of ${seat.id}.`,
            sample, movingSolidId: solid.id, seatId: seat.id });
        }
        if (minX >= seat.center[0] + seat.insideLength / 2
          || maxX <= seat.center[0] - seat.insideLength / 2
          || minZ >= seat.floorZ + seat.leadInHeight || maxZ <= seat.floorZ) continue;
        const lowest = Math.max(minZ, seat.floorZ);
        const sideRise = Math.min(1, (lowest - seat.floorZ) / seat.leadInHeight);
        const sideOpening = seat.throatWidth + (seat.mouthWidth - seat.throatWidth) * sideRise
          - 2 * seat.openingError;
        const sideWidth = solid.max[1] - solid.min[1] + 2 * input.envelope.partError[1];
        const sideCenter = pose[1] + (solid.min[1] + solid.max[1]) / 2;
        const sideMargin = (sideOpening - sideWidth) / 2
          - Math.abs(sideCenter - seat.center[1]) - input.envelope.poseError[1];
        minimumMargin = Math.min(minimumMargin, sideMargin);
        if (sideMargin + EPS < input.envelope.seatClearance) {
          issues.push({ code: 'seat-fit', detail: `${solid.id} side margin in ${seat.id} is ${sideMargin.toFixed(4)} m.`,
            sample, movingSolidId: solid.id, seatId: seat.id });
        }
      }
    }
  }
  return { issues, minimumMargin };
}

/** Screen a specified path only. A pass does not infer an alternate path or joint capacity. */
export function screenConnectorMotion(input: ConnectorMotionInput): ConnectorMotionScreen {
  const base = screenRigidPath({ moving: input.member, path: input.path, obstacles: input.obstacles,
    envelope: input.envelope, maxSampleStep: input.maxSampleStep });
  const issues: ScreeningIssue[] = [...base.issues];
  if (input.closureState !== 'removed') {
    issues.push({ code: 'closure-present', detail: 'Closure must be removed before beam guidance or extraction.' });
  }
  if (input.seats.length !== 2 || input.seats.some(s => !validSeat(s))
    || new Set(input.seats.map(s => s.shoeId)).size !== 2) {
    issues.push({ code: 'invalid-input', detail: 'Exactly two valid seats with distinct shoes are required.' });
  }
  const fit = base.sampleCount && !issues.some(i => i.code === 'invalid-input')
    ? seatIssues(pathSamples(input.path, input.maxSampleStep), input)
    : { issues: [], minimumMargin: null };
  issues.push(...fit.issues);
  return { operation: input.operation, status: issues.length ? 'failed' : 'passed',
    sampleCount: base.sampleCount, minimumSeatMargin: fit.minimumMargin, issues };
}
