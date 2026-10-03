import { applyMaterialEvent, createMaterialLedger } from './ledger';
import type { MaterialAsset, MaterialEvent, MaterialLedgerState, MaterialRole } from './types';

export const ORIGINAL_BEAM_ID = 'steel-beam-001';
export const REFORGED_BEAM_ID = 'steel-beam-002';
export const FASTENER_SET_ID = 'fastener-set-001';
export const TEMPORARY_BRACE_ID = 'temporary-brace-001';

function openingAsset(id: string, kind: MaterialAsset['kind'], partTypeId: string,
  massKg: number, dimensionsM: readonly [number, number, number]): MaterialAsset {
  return {
    id, kind, partTypeId, material: 'steel', massKg,
    passport: {
      schemaVersion: 1, manufactureBatchId: 'synthetic-opening-batch', parentAssetIds: [],
      grade: { value: 'S355-demo', basis: 'measured', reference: 'synthetic-opening-inspection' },
      interfaceRevision: { value: 'capture-bolt-v1', basis: 'measured', reference: 'synthetic-opening-inspection' },
      dimensionsM: { value: dimensionsM, basis: 'measured', reference: 'synthetic-opening-inspection' },
      records: [{ eventId: 'opening', atS: 0, action: 'opening', detail: 'Synthetic qualified opening stock' }],
    },
    location: 'stock', custodianId: 'yard-rack', condition: 'qualified', integrityRevision: 0,
    qualification: { evidenceId: `opening-inspection:${id}`, basis: 'measured', integrityRevision: 0,
      screeningCapacityKN: 50, interfaceRevision: 'capture-bolt-v1', materialGrade: 'S355-demo' },
    reservedRole: null, installedRoleId: null, useCount: 0,
  };
}

export function createBeamMaterialOpening(): MaterialLedgerState {
  return createMaterialLedger([
    openingAsset(ORIGINAL_BEAM_ID, 'member', 'beam-3m', 93.3, [3, 0.146, 0.254]),
    openingAsset(FASTENER_SET_ID, 'fastener-set', 'bolt-set', 2, [0.15, 0.08, 0.04]),
    openingAsset(TEMPORARY_BRACE_ID, 'temporary-work', 'brace-2m', 20, [2, 0.07, 0.07]),
  ]);
}

/**
 * Synthetic, deterministic accounting example: install A, inspect and directly reuse
 * the same identified beam at B, then quarantine and reforge it into a new ID for C.
 * Recorded "measured" inspections are fixture inputs, not real test data.
 */
export function runBeamMaterialLifecycle(): MaterialLedgerState {
  let state = createBeamMaterialOpening();
  let sequence = 0;
  const base = (): Pick<MaterialEvent, 'schemaVersion' | 'id' | 'expectedRevision' | 'atS'> => {
    sequence += 1;
    return { schemaVersion: 1, id: `material-${String(sequence).padStart(3, '0')}`,
      expectedRevision: state.revision, atS: sequence };
  };
  const commit = (event: MaterialEvent): void => { state = applyMaterialEvent(state, event); };
  const role = (configuration: string, kind: MaterialRole['kind'], partTypeId: string,
    minScreeningCapacityKN: number): MaterialRole => ({
    id: `${configuration}:${kind}`, kind, partTypeId, material: 'steel',
    requiredMaterialGrade: 'S355-demo', interfaceRevision: 'capture-bolt-v1', minScreeningCapacityKN,
  });
  const install = (assetId: string, target: MaterialRole): void => {
    commit({ ...base(), action: 'reserve', assetId, role: target });
    commit({ ...base(), action: 'move', assetId, to: 'carrier', custodianId: 'carrier-1' });
    commit({ ...base(), action: 'move', assetId, to: 'hoist', custodianId: 'hoist-1' });
    commit({ ...base(), action: 'move', assetId, to: 'workfront', custodianId: target.id });
    commit({ ...base(), action: 'install', assetId, roleId: target.id });
  };
  const remove = (assetId: string): void => {
    commit({ ...base(), action: 'remove', assetId, inspectionCustodianId: 'inspection-yard' });
  };
  const inspect = (assetId: string, outcome: 'qualified' | 'quarantine' | 'feedstock',
    feedstockLotId?: string): void => {
    const asset = state.assets[assetId];
    commit({ ...base(), action: 'inspect', assetId, outcome, stockCustodianId: 'yard-rack', feedstockLotId,
      evidence: {
        id: `synthetic-inspection-${sequence}`, basis: 'measured',
        reference: `synthetic-demonstration-observation-${sequence}`,
        observedIntegrityRevision: asset.integrityRevision,
        notes: outcome === 'qualified' ? 'Synthetic dimensional and capacity screen passed' :
          'Synthetic damage disposition',
        screeningCapacityKN: 50, observedInterfaceRevision: 'capture-bolt-v1',
        observedMaterialGrade: 'S355-demo',
      },
    });
  };
  const installConfiguration = (configuration: string, beamId: string, beamType: string): void => {
    install(TEMPORARY_BRACE_ID, role(configuration, 'temporary-work', 'brace-2m', 15));
    install(beamId, role(configuration, 'member', beamType, 25));
    install(FASTENER_SET_ID, role(configuration, 'fastener-set', 'bolt-set', 10));
  };
  const removeConfiguration = (beamId: string): void => {
    remove(FASTENER_SET_ID);
    remove(beamId);
    remove(TEMPORARY_BRACE_ID);
  };

  installConfiguration('configuration-A', ORIGINAL_BEAM_ID, 'beam-3m');
  removeConfiguration(ORIGINAL_BEAM_ID);
  inspect(ORIGINAL_BEAM_ID, 'qualified');
  inspect(FASTENER_SET_ID, 'qualified');
  inspect(TEMPORARY_BRACE_ID, 'qualified');

  installConfiguration('configuration-B', ORIGINAL_BEAM_ID, 'beam-3m');
  commit({ ...base(), action: 'damage', assetId: ORIGINAL_BEAM_ID,
    description: 'Synthetic permanent bend after second use' });
  removeConfiguration(ORIGINAL_BEAM_ID);
  inspect(ORIGINAL_BEAM_ID, 'quarantine');
  inspect(ORIGINAL_BEAM_ID, 'feedstock', 'beam-scrap-001');
  inspect(FASTENER_SET_ID, 'qualified');
  inspect(TEMPORARY_BRACE_ID, 'qualified');

  commit({ ...base(), action: 'recycle', inputLotId: 'beam-scrap-001', outputLotId: 'recycled-steel-001',
    outputMassKg: 90, yieldFraction: 90 / 93.3, energyKWh: 40,
    provenance: { value: 'Illustrative recycling balance', basis: 'assumed',
      reference: 'synthetic-demonstration-process-assumption' } });
  const reforged: MaterialAsset = {
    id: REFORGED_BEAM_ID, kind: 'member', partTypeId: 'beam-2.8m', material: 'steel', massKg: 88,
    passport: {
      schemaVersion: 1, manufactureBatchId: 'synthetic-reforging-batch',
      parentAssetIds: [ORIGINAL_BEAM_ID],
      grade: { value: 'S355-demo', basis: 'assumed', reference: 'synthetic-reforging-assumption' },
      interfaceRevision: { value: 'capture-bolt-v1', basis: 'assumed',
        reference: 'synthetic-reforging-assumption' },
      dimensionsM: { value: [2.8, 0.146, 0.254], basis: 'assumed',
        reference: 'synthetic-reforging-assumption' },
      records: [],
    },
    location: 'inspection', custodianId: 'inspection-yard', condition: 'inspection-required',
    integrityRevision: 0, qualification: null, reservedRole: null, installedRoleId: null, useCount: 0,
  };
  commit({ ...base(), action: 'reforge', inputLotId: 'recycled-steel-001', outputAsset: reforged,
    yieldFraction: 88 / 90, energyKWh: 24,
    provenance: { value: 'Illustrative forging balance', basis: 'assumed',
      reference: 'synthetic-demonstration-process-assumption' } });
  inspect(REFORGED_BEAM_ID, 'qualified');
  installConfiguration('configuration-C', REFORGED_BEAM_ID, 'beam-2.8m');
  return state;
}
