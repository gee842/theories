import { describe, expect, it } from 'vitest';
import { assessConstructionStages, assessTrussStage } from './solver';
import { createBracedTripodExample } from './example';
import type { ConstructionStage, TrussModel } from './types';

const EA = 200e9 * 1e-4;
const model: TrussModel = {
  nodes: [
    { id: 'base-a', positionM: [1, 0, 0] },
    { id: 'base-b', positionM: [-0.5, Math.sqrt(3) / 2, 0] },
    { id: 'base-c', positionM: [-0.5, -Math.sqrt(3) / 2, 0] },
    { id: 'peak', positionM: [0, 0, 1] },
    { id: 'unattached', positionM: [5, 5, 5] },
  ],
  members: ['a', 'b', 'c'].map((letter): TrussModel['members'][number] => ({
    id: `leg-${letter}`, nodeA: `base-${letter}`, nodeB: 'peak',
    areaM2: 1e-4, elasticModulusPa: 200e9,
    tensionCapacityN: 600, compressionCapacityN: 600,
  })),
  supports: [
    ...['a', 'b', 'c'].map((letter): TrussModel['supports'][number] => ({
      id: `ground-${letter}`, nodeId: `base-${letter}`,
      restrained: [true, true, true], kind: 'permanent',
    })),
    { id: 'temporary-x', nodeId: 'peak', restrained: [true, false, false], kind: 'temporary' },
  ],
};

const allMembers = ['leg-a', 'leg-b', 'leg-c'];
const allGround = ['ground-a', 'ground-b', 'ground-c'];
const verticalLoad = (newtons: number) => [{ nodeId: 'peak', forceN: [0, 0, -newtons] as const }];
const complete: ConstructionStage = {
  id: 'complete-braced-tripod', activeMemberIds: allMembers,
  activeSupportIds: allGround, loads: verticalLoad(900),
};

describe('3D staged pin-jointed truss screening', () => {
  it('keeps the exported example and input-order variants deterministic', () => {
    const example = createBracedTripodExample();
    expect(assessConstructionStages(example.model, example.stages).map(stage =>
      [stage.stability, stage.capacity])).toEqual([
      ['stable', 'pass'], ['mechanism', 'unverified'],
      ['stable', 'pass'], ['stable', 'fail'],
    ]);
    const reversed: TrussModel = {
      nodes: [...model.nodes].reverse(), members: [...model.members].reverse(),
      supports: [...model.supports].reverse(),
    };
    expect(assessTrussStage(reversed, {
      ...complete, activeMemberIds: [...allMembers].reverse(),
      activeSupportIds: [...allGround].reverse(),
    })).toEqual(assessTrussStage(model, complete));
  });

  it('balances a braced tripod and reports the expected compression, stress, reactions, and load paths', () => {
    const result = assessTrussStage(model, complete);
    expect(result.scope).toBe('axial-truss-screening-only');
    expect(result.stability).toBe('stable');
    expect(result.capacity).toBe('pass');
    expect(result.canTransferLoad).toBe(true);
    expect(result.diagnostics.stiffnessRank).toBe(3);
    expect(result.diagnostics.conditionNumber).toBeGreaterThan(1);
    expect(result.diagnostics.equilibriumResidualN).toBeLessThan(1e-8);
    expect(result.diagnostics.globalForceResidualN).toBeLessThan(1e-8);
    const expectedForceN = -900 * Math.SQRT2 / 3;
    for (const member of result.members) {
      expect(member.mode).toBe('compression');
      expect(member.axialForceN).toBeCloseTo(expectedForceN, 7);
      expect(member.stressPa).toBeCloseTo(expectedForceN / 1e-4, 3);
      expect(member.utilization).toBeCloseTo(Math.abs(expectedForceN) / 600, 10);
    }
    const peak = result.displacements.find(item => item.nodeId === 'peak')!;
    expect(peak.displacementM[2]).toBeCloseTo(-2 * Math.SQRT2 * 900 / (3 * EA), 12);
    expect(result.reactions.reduce((sum, support) => sum + support.forceN[2], 0)).toBeCloseTo(900, 8);
    expect(result.loadPaths).toHaveLength(1);
    expect(result.loadPaths[0].status).toBe('transmitted');
    expect(result.loadPaths[0].supportPaths.map(path => path.supportId)).toEqual(allGround);
    expect(result.loadPaths[0].supportPaths.every(path => path.memberIds.length === 1)).toBe(true);
  });

  it('detects the mechanism caused by omitting a brace, then resolves it with temporary restraint', () => {
    const stages: ConstructionStage[] = [
      { id: 'two-legs-with-temporary-support', activeMemberIds: ['leg-a', 'leg-b'],
        activeSupportIds: [...allGround, 'temporary-x'], loads: verticalLoad(100) },
      { id: 'temporary-support-released-too-early', activeMemberIds: ['leg-a', 'leg-b'],
        activeSupportIds: allGround, loads: verticalLoad(100) },
      { ...complete, id: 'third-leg-installed', loads: verticalLoad(100) },
    ];
    const [held, released, braced] = assessConstructionStages(model, stages);
    expect(held.stability).toBe('stable');
    expect(held.canTransferLoad).toBe(true);
    expect(released.stability).toBe('mechanism');
    expect(released.capacity).toBe('unverified');
    expect(released.canTransferLoad).toBe(false);
    expect(released.diagnostics.stiffnessRank).toBe(2);
    expect(released.diagnostics.mechanismModes).toHaveLength(1);
    expect(released.diagnostics.mechanismModes[0].dominantDofs.some(dof => dof.nodeId === 'peak')).toBe(true);
    expect(released.members.every(member => member.axialForceN === null)).toBe(true);
    expect(released.loadPaths[0].status).toBe('unresolved');
    expect(braced.stability).toBe('stable');
    expect(braced.canTransferLoad).toBe(true);
  });

  it('fails capacity for a stable but overloaded stage', () => {
    const result = assessTrussStage(model, { ...complete, id: 'overload', loads: verticalLoad(1500) });
    expect(result.stability).toBe('stable');
    expect(result.capacity).toBe('fail');
    expect(result.canTransferLoad).toBe(false);
    expect(result.members.every(member => (member.utilization ?? 0) > 1)).toBe(true);
  });

  it('identifies an isolated loaded node as disconnected and unstable', () => {
    const result = assessTrussStage(model, {
      id: 'floating-load', activeMemberIds: allMembers, activeSupportIds: allGround,
      loads: [...verticalLoad(100), { nodeId: 'unattached', forceN: [0, 0, -100] }],
    });
    expect(result.stability).toBe('mechanism');
    expect(result.loadPaths.find(path => path.nodeId === 'unattached')).toMatchObject({
      status: 'disconnected', topologicallyConnectedToRestraint: false,
    });
  });

  it('withholds a nearly singular solution and reports its condition number', () => {
    const nearCoplanar: TrussModel = {
      ...model,
      nodes: model.nodes.map(node => node.id === 'base-c' ?
        { ...node, positionM: [1, 5e-5, 0] as const } : node),
    };
    const result = assessTrussStage(nearCoplanar, complete);
    expect(result.stability).toBe('ill-conditioned');
    expect(result.canTransferLoad).toBe(false);
    expect(result.diagnostics.conditionNumber).toBeGreaterThan(1e9);
    expect(result.diagnostics.conditionWarning).toBe(true);
    expect(result.members.every(member => member.axialForceN === null)).toBe(true);
  });

  it('rejects overlapping restraints rather than inventing a reaction split', () => {
    const overlapping: TrussModel = {
      ...model,
      supports: [...model.supports, {
        id: 'duplicate-x', nodeId: 'peak', restrained: [true, false, false], kind: 'temporary',
      }],
    };
    expect(() => assessTrussStage(overlapping, {
      ...complete, activeSupportIds: [...allGround, 'temporary-x', 'duplicate-x'],
    })).toThrow(/overlapping restraints/);
  });
});
