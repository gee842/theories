import type { ConstructionStage, TrussModel } from './types';

/** Small research example: three pin-ended legs brace one loaded node in 3D. */
export function createBracedTripodExample(): { model: TrussModel; stages: ConstructionStage[] } {
  const model: TrussModel = {
    nodes: [
      { id: 'base-a', positionM: [1, 0, 0] },
      { id: 'base-b', positionM: [-0.5, Math.sqrt(3) / 2, 0] },
      { id: 'base-c', positionM: [-0.5, -Math.sqrt(3) / 2, 0] },
      { id: 'peak', positionM: [0, 0, 1] },
    ],
    members: ['a', 'b', 'c'].map(letter => ({
      id: `leg-${letter}`, nodeA: `base-${letter}`, nodeB: 'peak',
      areaM2: 1e-4, elasticModulusPa: 200e9,
      tensionCapacityN: 600, compressionCapacityN: 600,
    })),
    supports: [
      ...['a', 'b', 'c'].map(letter => ({
        id: `ground-${letter}`, nodeId: `base-${letter}`,
        restrained: [true, true, true] as const, kind: 'permanent' as const,
      })),
      { id: 'temporary-x', nodeId: 'peak',
        restrained: [true, false, false], kind: 'temporary' },
    ],
  };
  const ground = ['ground-a', 'ground-b', 'ground-c'];
  const load = (forceN: number) => [{ nodeId: 'peak', forceN: [0, 0, -forceN] as const }];
  const stages: ConstructionStage[] = [
    {
      id: 'two-legs-temporarily-held', activeMemberIds: ['leg-a', 'leg-b'],
      activeSupportIds: [...ground, 'temporary-x'], loads: load(100),
    },
    {
      id: 'premature-temporary-release', activeMemberIds: ['leg-a', 'leg-b'],
      activeSupportIds: ground, loads: load(100),
    },
    {
      id: 'third-leg-braced', activeMemberIds: ['leg-a', 'leg-b', 'leg-c'],
      activeSupportIds: ground, loads: load(900),
    },
    {
      id: 'braced-overload', activeMemberIds: ['leg-a', 'leg-b', 'leg-c'],
      activeSupportIds: ground, loads: load(1500),
    },
  ];
  return { model, stages };
}
