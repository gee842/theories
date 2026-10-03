import { describe, expect, it } from 'vitest';
import { applyMaterialEvent, materialBalances } from './ledger';
import {
  createBeamMaterialOpening, FASTENER_SET_ID, ORIGINAL_BEAM_ID,
  REFORGED_BEAM_ID, runBeamMaterialLifecycle, TEMPORARY_BRACE_ID,
} from './demo';
import type { MaterialEvent, MaterialLedgerState, MaterialRole } from './types';

type EventDetails = MaterialEvent extends infer E
  ? E extends unknown ? Omit<E, 'schemaVersion' | 'id' | 'expectedRevision' | 'atS'> : never
  : never;

const beamRole: MaterialRole = {
  id: 'test-bay:member', kind: 'member', partTypeId: 'beam-3m', material: 'steel',
  requiredMaterialGrade: 'S355-demo', interfaceRevision: 'capture-bolt-v1', minScreeningCapacityKN: 25,
};

function event(state: MaterialLedgerState, sequence: number,
  details: EventDetails): MaterialEvent {
  return { schemaVersion: 1, id: `test-${sequence}`, expectedRevision: state.revision,
    atS: sequence, ...details } as MaterialEvent;
}

function installedBeam(): { state: MaterialLedgerState; sequence: number } {
  let state = createBeamMaterialOpening();
  let sequence = 0;
  const commit = (details: Parameters<typeof event>[2]) => {
    state = applyMaterialEvent(state, event(state, ++sequence, details));
  };
  commit({ action: 'reserve', assetId: ORIGINAL_BEAM_ID, role: beamRole });
  commit({ action: 'move', assetId: ORIGINAL_BEAM_ID, to: 'carrier', custodianId: 'carrier' });
  commit({ action: 'move', assetId: ORIGINAL_BEAM_ID, to: 'hoist', custodianId: 'hoist' });
  commit({ action: 'move', assetId: ORIGINAL_BEAM_ID, to: 'workfront', custodianId: 'bay' });
  commit({ action: 'install', assetId: ORIGINAL_BEAM_ID, roleId: beamRole.id });
  return { state, sequence };
}

describe('material passports and lifecycle ledger', () => {
  it('tracks direct reuse, quarantine, steel recycling and a newly identified reforged beam', () => {
    const state = runBeamMaterialLifecycle();
    const original = state.assets[ORIGINAL_BEAM_ID];
    const reforged = state.assets[REFORGED_BEAM_ID];
    const steel = materialBalances(state).steel;

    expect(original.useCount).toBe(2);
    expect(original.location).toBe('consumed');
    expect(original.passport.records.some(record => record.action === 'damage')).toBe(true);
    expect(original.passport.records.some(record => record.detail.includes('quarantine'))).toBe(true);
    expect(reforged.id).not.toBe(original.id);
    expect(reforged.passport.parentAssetIds).toEqual([ORIGINAL_BEAM_ID]);
    expect(reforged.useCount).toBe(1);
    expect(reforged.location).toBe('installed');
    expect(state.assets[FASTENER_SET_ID].useCount).toBe(3);
    expect(state.assets[TEMPORARY_BRACE_ID].useCount).toBe(3);
    expect(state.processes.map(process => process.operation)).toEqual(['recycle', 'reforge']);
    expect(state.processes.map(process => process.provenance.basis)).toEqual(['assumed', 'assumed']);
    expect(state.processes.map(process => process.energyKWh)).toEqual([40, 24]);
    expect(steel.openingMassKg).toBeCloseTo(115.3);
    expect(steel.activeAssetMassKg).toBeCloseTo(110);
    expect(steel.unrecoveredMassKg).toBeCloseTo(5.3);
    expect(steel.residualKg).toBeCloseTo(0, 10);
    expect(materialBalances(state).polymer.residualKg).toBe(0);
  });

  it('blocks reuse after removal until a current measured inspection qualifies the same ID', () => {
    let { state, sequence } = installedBeam();
    state = applyMaterialEvent(state, event(state, ++sequence,
      { action: 'remove', assetId: ORIGINAL_BEAM_ID, inspectionCustodianId: 'inspection-yard' }));
    expect(() => applyMaterialEvent(state, event(state, sequence + 1,
      { action: 'reserve', assetId: ORIGINAL_BEAM_ID, role: beamRole }))).toThrow(/not in stock/);
    const obsoleteRevision = state.assets[ORIGINAL_BEAM_ID].integrityRevision - 1;
    const inspection = {
      id: 'test-inspection', basis: 'measured' as const, reference: 'synthetic-test-observation',
      observedIntegrityRevision: obsoleteRevision, notes: 'Passed fixture screen',
      screeningCapacityKN: 50, observedInterfaceRevision: 'capture-bolt-v1',
      observedMaterialGrade: 'S355-demo',
    };
    expect(() => applyMaterialEvent(state, event(state, sequence + 1,
      { action: 'inspect', assetId: ORIGINAL_BEAM_ID, outcome: 'qualified',
        stockCustodianId: 'yard-rack', evidence: inspection }))).toThrow(/Stale inspection evidence/);
    state = applyMaterialEvent(state, event(state, ++sequence,
      { action: 'inspect', assetId: ORIGINAL_BEAM_ID, outcome: 'qualified',
        stockCustodianId: 'yard-rack', evidence: {
          ...inspection, observedIntegrityRevision: state.assets[ORIGINAL_BEAM_ID].integrityRevision,
        } }));
    state = applyMaterialEvent(state, event(state, ++sequence,
      { action: 'reserve', assetId: ORIGINAL_BEAM_ID, role: beamRole }));
    expect(state.assets[ORIGINAL_BEAM_ID].id).toBe(ORIGINAL_BEAM_ID);
    expect(state.assets[ORIGINAL_BEAM_ID].location).toBe('reserved');
  });

  it('returns a mass-neutral repair to inspection and requires a new qualification', () => {
    let { state, sequence } = installedBeam();
    state = applyMaterialEvent(state, event(state, ++sequence,
      { action: 'damage', assetId: ORIGINAL_BEAM_ID, description: 'Bent flange' }));
    state = applyMaterialEvent(state, event(state, ++sequence,
      { action: 'remove', assetId: ORIGINAL_BEAM_ID, inspectionCustodianId: 'inspection-yard' }));
    state = applyMaterialEvent(state, event(state, ++sequence,
      { action: 'inspect', assetId: ORIGINAL_BEAM_ID, outcome: 'repairable',
        evidence: { id: 'repair-assessment', basis: 'measured', reference: 'synthetic-test-observation',
          observedIntegrityRevision: state.assets[ORIGINAL_BEAM_ID].integrityRevision,
          notes: 'Cold straightening candidate' } }));
    state = applyMaterialEvent(state, event(state, ++sequence,
      { action: 'repair', assetId: ORIGINAL_BEAM_ID, inspectionCustodianId: 'inspection-yard',
        evidence: { id: 'straightening-record', basis: 'assumed', reference: 'synthetic-repair-assumption',
          observedIntegrityRevision: state.assets[ORIGINAL_BEAM_ID].integrityRevision,
          method: 'Mass-neutral cold straightening', energyKWh: 3 } }));
    expect(state.assets[ORIGINAL_BEAM_ID].location).toBe('inspection');
    expect(state.assets[ORIGINAL_BEAM_ID].qualification).toBeNull();
    expect(materialBalances(state).steel.residualKg).toBeCloseTo(0, 10);
    expect(() => applyMaterialEvent(state, event(state, sequence + 1,
      { action: 'inspect', assetId: ORIGINAL_BEAM_ID, outcome: 'qualified',
        stockCustodianId: 'yard-rack', evidence: {
          id: 'assumed-pass', basis: 'assumed', reference: 'synthetic-test-assumption',
          observedIntegrityRevision: state.assets[ORIGINAL_BEAM_ID].integrityRevision,
          notes: 'Assumed pass', screeningCapacityKN: 50,
          observedInterfaceRevision: 'capture-bolt-v1', observedMaterialGrade: 'S355-demo',
        } }))).toThrow(/measured inspection/);
  });

  it('rejects process mass creation, inconsistent yield and stale ledger revision', () => {
    const complete = runBeamMaterialLifecycle();
    let state = createBeamMaterialOpening();
    for (const recorded of complete.events) {
      if (recorded.action === 'recycle') break;
      state = applyMaterialEvent(state, recorded);
    }
    const inputMass = state.lots['beam-scrap-001'].massKg;
    expect(() => applyMaterialEvent(state, event(state, state.revision + 1,
      { action: 'recycle', inputLotId: 'beam-scrap-001', outputLotId: 'impossible-steel',
        outputMassKg: inputMass + 1, yieldFraction: 1, energyKWh: 40,
        provenance: { value: 'Bad yield', basis: 'assumed', reference: 'test' } })))
      .toThrow(/create material mass/);
    expect(() => applyMaterialEvent(state, event(state, state.revision + 1,
      { action: 'recycle', inputLotId: 'beam-scrap-001', outputLotId: 'wrong-yield',
        outputMassKg: 90, yieldFraction: 0.5, energyKWh: 40,
        provenance: { value: 'Bad yield', basis: 'assumed', reference: 'test' } })))
      .toThrow(/declared yield/);
    const valid = complete.events.find(recorded => recorded.action === 'recycle')!;
    expect(() => applyMaterialEvent(state, { ...valid, expectedRevision: state.revision - 1 }))
      .toThrow(/Stale material event/);
  });
});
