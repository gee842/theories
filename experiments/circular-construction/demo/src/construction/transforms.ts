import { Euler, Quaternion, Vector3 } from 'three';
import type { Pose, Vec3 } from './types';

function quaternion(pose: Pose): Quaternion {
  return new Quaternion().setFromEuler(new Euler(...pose.rotation, 'XYZ'));
}
function fromQuaternion(position: Vec3, orientation: Quaternion): Pose {
  const euler = new Euler().setFromQuaternion(orientation, 'XYZ');
  return { position, rotation: [euler.x, euler.y, euler.z] };
}
/** A rigid local pose follows the complete parent transform, including orientation. */
export function composePose(parent: Pose, local: Pose): Pose {
  const orientation = quaternion(parent);
  const position = new Vector3(...local.position).applyQuaternion(orientation).add(new Vector3(...parent.position));
  return fromQuaternion(position.toArray() as Vec3, orientation.multiply(quaternion(local)));
}
/** Supported transfer blends translation and shortest-path orientation together. */
export function interpolatePose(from: Pose, to: Pose, progress: number): Pose {
  const u = Math.max(0, Math.min(1, progress));
  if (u === 0) return structuredClone(from);
  if (u === 1) return structuredClone(to);
  const position = from.position.map((v, i) => v + (to.position[i] - v) * u) as Vec3;
  return fromQuaternion(position, quaternion(from).slerp(quaternion(to), u));
}
/** Utility for checking the represented rigid orientation rather than Euler branches. */
export function transformedAxis(pose: Pose, localAxis: Vec3): Vec3 {
  return new Vector3(...localAxis).applyQuaternion(quaternion(pose)).toArray() as Vec3;
}
