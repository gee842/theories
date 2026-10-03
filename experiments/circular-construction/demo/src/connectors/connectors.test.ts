import { describe, expect, it } from 'vitest';
import { BEAM, CLEAR_CENTER, ENVELOPE, fixtureObstacles, INSTALLED_CENTER,
  runOpenSeatBench, SAMPLE_STEP, screenDualClosedSockets, SEATS } from './bench';
import { screenConnectorMotion, screenRigidPath } from './geometry';
import { screenScenarioConnectorMotions } from './scenario';

describe('two-ended reversible connector geometry screen', () => {
  it('guides both shoes into open seats, places caps, reaches both screws, and extracts', () => {
    const result = runOpenSeatBench();
    expect(result.status).toBe('passed');
    expect(result.guide.sampleCount).toBeGreaterThan(40);
    expect(result.lower.sampleCount).toBe(result.guide.sampleCount);
    expect(result.guide.minimumSeatMargin).toBeGreaterThan(ENVELOPE.seatClearance);
    expect(result.closurePlacement.map(r => r.status)).toEqual(['passed', 'passed']);
    expect(result.closureRemoval.map(r => r.status)).toEqual(['passed', 'passed']);
    expect(result.driverAccess.map(r => r.status)).toEqual(['passed', 'passed']);
  });

  it('blocks a guide if the removable caps remain installed', () => {
    const result = screenConnectorMotion({ operation: 'guide', member: BEAM,
      path: [CLEAR_CENTER, INSTALLED_CENTER], seats: SEATS, obstacles: fixtureObstacles(),
      closureState: 'installed', envelope: ENVELOPE, maxSampleStep: SAMPLE_STEP });
    expect(result.status).toBe('failed');
    expect(result.issues.some(i => i.code === 'closure-present')).toBe(true);
  });

  it('shows why two fixed closed lips block the vertical two-end insertion', () => {
    const result = screenDualClosedSockets();
    expect(result.status).toBe('failed');
    expect(result.issues.some(i => i.code === 'collision' && i.obstacleId?.includes('cap'))).toBe(true);
  });

  it('rejects a lateral alignment error outside the tolerance envelope', () => {
    const start: readonly [number, number, number] = [CLEAR_CENTER[0], 0.05, CLEAR_CENTER[2]];
    const finish: readonly [number, number, number] = [INSTALLED_CENTER[0], 0.05, INSTALLED_CENTER[2]];
    const result = screenConnectorMotion({ operation: 'guide', member: BEAM,
      path: [start, finish], seats: SEATS, obstacles: fixtureObstacles(),
      closureState: 'removed', envelope: ENVELOPE, maxSampleStep: SAMPLE_STEP });
    expect(result.status).toBe('failed');
    expect(result.issues.some(i => i.code === 'seat-fit')).toBe(true);
  });

  it('rejects an enlarged beam body even when the narrower shoes fit', () => {
    const wider = { ...BEAM, solids: BEAM.solids.map(s => s.id === 'beam-body'
      ? { ...s, min: [-1.43, -0.105, -0.107] as const,
        max: [1.43, 0.105, 0.147] as const } : s) };
    const result = screenConnectorMotion({ operation: 'guide', member: wider,
      path: [CLEAR_CENTER, INSTALLED_CENTER], seats: SEATS, obstacles: fixtureObstacles(),
      closureState: 'removed', envelope: ENVELOPE, maxSampleStep: SAMPLE_STEP });
    expect(result.status).toBe('failed');
    expect(result.issues.some(i => i.code === 'seat-fit' && i.movingSolidId === 'beam-body')).toBe(true);
  });

  it('fails when the declared placement error consumes the seat clearance', () => {
    const result = screenConnectorMotion({ operation: 'guide', member: BEAM,
      path: [CLEAR_CENTER, INSTALLED_CENTER], seats: SEATS, obstacles: fixtureObstacles(),
      closureState: 'removed', envelope: { ...ENVELOPE, poseError: [0.03, 0.03, 0.004] },
      maxSampleStep: SAMPLE_STEP });
    expect(result.status).toBe('failed');
    expect(result.issues.some(i => i.code === 'seat-fit')).toBe(true);
  });

  it('checks tool access against an added workfront obstruction', () => {
    const blocked = screenRigidPath({ moving: { id: 'driver', solids: [
      { id: 'driver-envelope', min: [-0.03, -0.03, -0.10], max: [0.03, 0.03, 0.10] }] },
      path: [[0.01, 0, 3.78], [0.01, 0, 3.48]],
      obstacles: [{ id: 'parked-tool-blocks-driver', min: [-0.05, -0.05, 3.48], max: [0.05, 0.05, 3.65] }],
      envelope: ENVELOPE, maxSampleStep: SAMPLE_STEP });
    expect(blocked.status).toBe('failed');
    expect(blocked.issues[0]?.obstacleId).toBe('parked-tool-blocks-driver');
  });

  it('rejects the historical 3.25-to-3.00 m move against solid heads', () => {
    const result = screenConnectorMotion({ operation: 'guide', member: BEAM,
      path: [[1.5, 0, 3.25], [1.5, 0, 3.00]], seats: SEATS,
      obstacles: fixtureObstacles(), closureState: 'removed', envelope: ENVELOPE,
      maxSampleStep: SAMPLE_STEP });
    expect(result.status).toBe('failed');
    expect(result.issues.some(i => i.code === 'collision' && i.obstacleId?.startsWith('head-'))).toBe(true);
    expect(result.issues.some(i => i.code === 'seat-contact')).toBe(true);
  });

  it('screens recorded A/B guides, recorded A removal, and the reversible B path', () => {
    const checks = screenScenarioConnectorMotions();
    expect(checks.map(c => [c.fixture, c.operation, c.source])).toEqual([
      ['A', 'guide', 'recorded-event'],
      ['A', 'lower', 'recorded-event'],
      ['B', 'guide', 'recorded-event'],
      ['B', 'lower', 'reverse-of-recorded-guide'],
    ]);
    for (const check of checks) {
      expect(check.result.status, `${check.fixture} ${check.operation}: ${check.result.issues[0]?.detail}`)
        .toBe('passed');
    }
  });
});
