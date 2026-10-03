/** Authored geometric contact targets. These do not establish forces, friction or grip capacity. */
export type ClimbingLimb = 'fl' | 'fr' | 'rl' | 'rr';
export interface PlannedGrip {
  limb: ClimbingLimb;
  shoulder: number;
  elbow: number;
  wrist: number;
  contactX: number;
  worldHeight: number;
  lateral: number;
  anchorIndex: number;
  planted: boolean;
  jawCenter: number;
  reachable: boolean;
}
export interface PlantedClimb { grips: PlannedGrip[]; plantedCount: number; phase: number; cycle: number; evidence: 'planned-ik' }
const PITCH = .32;
const LINK = .65;
const THROAT = .135;
const BODY_REFERENCE = 1.44;
const order: ClimbingLimb[] = ['fl', 'rr', 'fr', 'rl'];
const smooth = (u: number) => u * u * (3 - 2 * u);

/**
 * Three jaw throats stay at fixed world lattice positions while the fourth moves.
 * Body motion is the site's actual root pose; anchors never inherit body translation.
 * The mapping is reversible for descent and reconstructs identically after a seek.
 */
export function solvePlantedClimb(rootHeight: number, forwardDistance = .75, saddlePhase = 0): PlantedClimb {
  const travel = (rootHeight - BODY_REFERENCE) / PITCH;
  const cycle = Math.floor(travel + 1e-10);
  const phase = Math.max(0, Math.min(1, travel - cycle));
  const grips = (['fl', 'fr', 'rl', 'rr'] as ClimbingLimb[]).map((limb): PlannedGrip => {
    const row = limb[0] === 'f' ? 3 : 0;
    const step = order.indexOf(limb);
    const swingProgress = Math.max(0, Math.min(1, phase * 4 - step));
    const planted = swingProgress <= 0 || swingProgress >= 1;
    const advance = smooth(swingProgress);
    const retract = planted ? 0 : .10 * Math.sin(Math.PI * swingProgress);
    const contactX = forwardDistance - retract;
    const anchorIndex = 3 + cycle + row + (swingProgress >= 1 ? 1 : 0);
    const worldHeight = saddlePhase + (3 + cycle + row + advance) * PITCH;
    const hipHeight = rootHeight + (row ? .48 : -.48);
    const x = contactX - THROAT, y = worldHeight - hipHeight;
    const radius2 = x * x + y * y;
    const reachable = x > 0 && radius2 <= (2 * LINK) ** 2 && radius2 > 1e-8;
    const cosine = Math.max(-1, Math.min(1, (radius2 - 2 * LINK * LINK) / (2 * LINK * LINK)));
    // Angles are absolute glTF +Z hinge rotations; source physics +Y angles have opposite sign.
    const elbow = -Math.acos(cosine);
    const shoulder = Math.atan2(y, x) - Math.atan2(LINK * Math.sin(elbow), LINK + LINK * Math.cos(elbow));
    const wrist = -(shoulder + elbow);
    const aperture = planted ? .045 : .045 + .105 * Math.sin(Math.PI * swingProgress);
    return { limb, shoulder, elbow, wrist, contactX, worldHeight, lateral: limb[1] === 'l' ? .32 : -.32, anchorIndex, planted, jawCenter: aperture, reachable };
  });
  return { grips, plantedCount: grips.filter((g) => g.planted && g.reachable).length, phase, cycle, evidence: 'planned-ik' };
}

/** Forward geometry useful for checking the actual exported throat against the target. */
export function gripForward(grip: PlannedGrip, hipWorldHeight: number) {
  return {
    x: LINK * Math.cos(grip.shoulder) + LINK * Math.cos(grip.shoulder + grip.elbow) + THROAT * Math.cos(grip.shoulder + grip.elbow + grip.wrist),
    y: hipWorldHeight + LINK * Math.sin(grip.shoulder) + LINK * Math.sin(grip.shoulder + grip.elbow) + THROAT * Math.sin(grip.shoulder + grip.elbow + grip.wrist),
  };
}
