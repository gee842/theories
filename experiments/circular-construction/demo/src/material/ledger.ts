import type {
  InspectionEvidence, MaterialAsset, MaterialBalance, MaterialEvent, MaterialId,
  MaterialLedgerState, MaterialLot, MaterialRole, PassportRecord, ProcessRecord,
  Provenanced,
} from './types';

const MATERIALS: MaterialId[] = ['steel', 'polymer'];
const EPSILON_KG = 1e-8;

function requireState(condition: unknown, message: string): asserts condition {
  if (!condition) throw new Error(message);
}

function positive(value: number, name: string): void {
  requireState(Number.isFinite(value) && value > 0, `${name} must be positive and finite`);
}

function nonnegative(value: number, name: string): void {
  requireState(Number.isFinite(value) && value >= 0, `${name} must be nonnegative and finite`);
}

function named(value: string, name: string): void {
  requireState(value.trim().length > 0, `${name} is required`);
}

function provenance<T>(value: Provenanced<T>, name: string): void {
  requireState(['measured', 'catalogue', 'assumed'].includes(value.basis), `${name} has invalid basis`);
  named(value.reference, `${name} reference`);
}

function activeAsset(state: MaterialLedgerState, id: string): MaterialAsset {
  const asset = state.assets[id];
  requireState(asset && asset.location !== 'consumed', `Unknown or consumed asset: ${id}`);
  return asset;
}

function availableLot(state: MaterialLedgerState, id: string): MaterialLot {
  const lot = state.lots[id];
  requireState(lot && lot.status === 'available', `Unknown or consumed lot: ${id}`);
  return lot;
}

function unusedId(state: MaterialLedgerState, id: string): void {
  named(id, 'new identity');
  requireState(!state.assets[id] && !state.lots[id], `Identity already exists: ${id}`);
}

function record(asset: MaterialAsset, event: MaterialEvent, detail: string, evidenceId?: string): void {
  const entry: PassportRecord = { eventId: event.id, atS: event.atS, action: event.action, detail };
  if (evidenceId) entry.evidenceId = evidenceId;
  asset.passport.records.push(entry);
}

function roleMatches(asset: MaterialAsset, role: MaterialRole): void {
  named(role.id, 'role ID');
  requireState(asset.kind === role.kind && asset.partTypeId === role.partTypeId && asset.material === role.material,
    `Asset ${asset.id} is incompatible with role ${role.id}`);
  nonnegative(role.minScreeningCapacityKN, 'screening capacity threshold');
  const qualified = asset.qualification;
  requireState(asset.condition === 'qualified' && qualified !== null &&
    qualified.basis === 'measured' && qualified.integrityRevision === asset.integrityRevision,
  `Asset ${asset.id} lacks current measured qualification`);
  requireState(qualified.interfaceRevision === role.interfaceRevision &&
    asset.passport.interfaceRevision.value === role.interfaceRevision,
  `Asset ${asset.id} has incompatible interface revision`);
  requireState(qualified.materialGrade === role.requiredMaterialGrade &&
    asset.passport.grade.value === role.requiredMaterialGrade,
  `Asset ${asset.id} has incompatible material grade`);
  requireState(qualified.screeningCapacityKN >= role.minScreeningCapacityKN,
    `Asset ${asset.id} lacks screening capacity for ${role.id}`);
}

function checkObservation(asset: MaterialAsset, evidence: InspectionEvidence): void {
  named(evidence.id, 'inspection evidence ID');
  named(evidence.reference, 'inspection reference');
  named(evidence.notes, 'inspection notes');
  requireState(evidence.observedIntegrityRevision === asset.integrityRevision,
    `Stale inspection evidence for ${asset.id}`);
}

function processMass(inputMassKg: number, outputMassKg: number, yieldFraction: number, energyKWh: number): number {
  positive(inputMassKg, 'process input mass');
  positive(outputMassKg, 'process output mass');
  requireState(Number.isFinite(yieldFraction) && yieldFraction > 0 && yieldFraction <= 1,
    'Process yield must be in (0, 1]');
  nonnegative(energyKWh, 'process energy');
  requireState(outputMassKg <= inputMassKg + EPSILON_KG,
    'Process would create material mass');
  requireState(Math.abs(outputMassKg - inputMassKg * yieldFraction) <= EPSILON_KG * Math.max(1, inputMassKg),
    'Process output does not match declared yield');
  return Math.max(0, inputMassKg - outputMassKg);
}

function addProcess(state: MaterialLedgerState, event: Extract<MaterialEvent, { action: 'recycle' | 'reforge' }>,
  input: MaterialLot, outputId: string, outputMassKg: number): void {
  const unrecoveredMassKg = processMass(input.massKg, outputMassKg, event.yieldFraction, event.energyKWh);
  provenance(event.provenance, 'process provenance');
  const process: ProcessRecord = {
    eventId: event.id, operation: event.action, inputId: input.id, outputId,
    material: input.material, inputMassKg: input.massKg, outputMassKg, unrecoveredMassKg,
    yieldFraction: event.yieldFraction, energyKWh: event.energyKWh,
    provenance: structuredClone(event.provenance),
  };
  state.processes.push(process);
  if (unrecoveredMassKg > EPSILON_KG) {
    state.losses.push({ eventId: event.id, material: input.material, massKg: unrecoveredMassKg,
      disposition: 'unrecovered-process-output' });
  }
}

/** Opens a finite, explicit inventory. Callers remain responsible for the truth of opening measurements. */
export function createMaterialLedger(openingAssets: MaterialAsset[], openingLots: MaterialLot[] = []): MaterialLedgerState {
  const state: MaterialLedgerState = {
    schemaVersion: 1, revision: 0, lastAtS: 0,
    assets: {}, lots: {},
    openingMassKg: { steel: 0, polymer: 0 },
    receivedMassKg: { steel: 0, polymer: 0 },
    losses: [], processes: [], events: [],
  };
  for (const asset of openingAssets) {
    unusedId(state, asset.id);
    state.assets[asset.id] = structuredClone(asset);
    state.openingMassKg[asset.material] += asset.massKg;
  }
  for (const lot of openingLots) {
    unusedId(state, lot.id);
    state.lots[lot.id] = structuredClone(lot);
    state.openingMassKg[lot.material] += lot.massKg;
  }
  assertMaterialLedger(state);
  return state;
}

/** Atomic, deterministic transition. The input state is never modified. */
export function applyMaterialEvent(current: MaterialLedgerState, event: MaterialEvent): MaterialLedgerState {
  assertMaterialLedger(current);
  requireState(event.schemaVersion === 1, 'Unsupported material event version');
  named(event.id, 'event ID');
  requireState(event.expectedRevision === current.revision,
    `Stale material event ${event.id}: expected revision ${event.expectedRevision}, current ${current.revision}`);
  requireState(Number.isFinite(event.atS) && event.atS >= current.lastAtS, 'Material event time moved backwards');
  requireState(!current.events.some(previous => previous.id === event.id), `Duplicate material event: ${event.id}`);
  if (event.source) {
    named(event.source.executionEventId, 'execution event ID');
    nonnegative(event.source.worldRevision, 'world revision');
  }
  const state = structuredClone(current);
  switch (event.action) {
    case 'reserve': {
      const asset = activeAsset(state, event.assetId);
      requireState(asset.location === 'stock', `Asset ${asset.id} is not in stock`);
      roleMatches(asset, event.role);
      asset.location = 'reserved';
      asset.reservedRole = structuredClone(event.role);
      record(asset, event, `Reserved for ${event.role.id}`);
      break;
    }
    case 'move': {
      const asset = activeAsset(state, event.assetId);
      const allowed = (asset.location === 'reserved' && event.to === 'carrier') ||
        (asset.location === 'carrier' && event.to === 'hoist') ||
        (asset.location === 'hoist' && event.to === 'workfront');
      requireState(allowed, `Invalid custody move for ${asset.id}: ${asset.location} -> ${event.to}`);
      named(event.custodianId, 'custodian ID');
      asset.location = event.to;
      asset.custodianId = event.custodianId;
      record(asset, event, `Custody to ${event.to}:${event.custodianId}`);
      break;
    }
    case 'install': {
      const asset = activeAsset(state, event.assetId);
      requireState(asset.location === 'workfront' && asset.reservedRole?.id === event.roleId,
        `Asset ${asset.id} is not prepared for role ${event.roleId}`);
      roleMatches(asset, asset.reservedRole);
      asset.location = 'installed';
      asset.custodianId = event.roleId;
      asset.installedRoleId = event.roleId;
      asset.reservedRole = null;
      asset.useCount += 1;
      asset.integrityRevision += 1;
      asset.qualification = null;
      record(asset, event, `Installed for use ${asset.useCount} at ${event.roleId}`);
      break;
    }
    case 'damage': {
      const asset = activeAsset(state, event.assetId);
      requireState(asset.location === 'installed', `Damage event requires installed asset: ${asset.id}`);
      named(event.description, 'damage description');
      asset.condition = 'damaged';
      asset.integrityRevision += 1;
      asset.qualification = null;
      record(asset, event, `Damage observed: ${event.description}`);
      break;
    }
    case 'remove': {
      const asset = activeAsset(state, event.assetId);
      requireState(asset.location === 'installed', `Asset ${asset.id} is not installed`);
      named(event.inspectionCustodianId, 'inspection custodian ID');
      asset.location = 'inspection';
      asset.custodianId = event.inspectionCustodianId;
      asset.installedRoleId = null;
      asset.condition = asset.condition === 'damaged' ? 'damaged' : 'inspection-required';
      asset.integrityRevision += 1;
      asset.qualification = null;
      record(asset, event, 'Removed for condition inspection');
      break;
    }
    case 'inspect': {
      const asset = activeAsset(state, event.assetId);
      requireState(asset.location === 'inspection' || asset.location === 'quarantine',
        `Asset ${asset.id} is not awaiting inspection`);
      checkObservation(asset, event.evidence);
      requireState(!state.events.some(previous => previous.action === 'inspect' && previous.evidence.id === event.evidence.id),
        `Duplicate inspection evidence: ${event.evidence.id}`);
      if (event.outcome === 'qualified') {
        requireState(event.evidence.basis === 'measured', 'Qualification requires measured inspection evidence');
        requireState(event.evidence.observedInterfaceRevision === asset.passport.interfaceRevision.value,
          `Inspection found incompatible interface on ${asset.id}`);
        named(event.evidence.observedMaterialGrade ?? '', 'observed material grade');
        positive(event.evidence.screeningCapacityKN ?? NaN, 'measured screening capacity');
        named(event.stockCustodianId ?? '', 'stock custodian ID');
        asset.passport.grade = { value: event.evidence.observedMaterialGrade!, basis: 'measured',
          reference: event.evidence.reference };
        asset.passport.interfaceRevision = { value: event.evidence.observedInterfaceRevision!, basis: 'measured',
          reference: event.evidence.reference };
        asset.condition = 'qualified';
        asset.location = 'stock';
        asset.custodianId = event.stockCustodianId!;
        asset.qualification = {
          evidenceId: event.evidence.id, basis: 'measured', integrityRevision: asset.integrityRevision,
          screeningCapacityKN: event.evidence.screeningCapacityKN!,
          interfaceRevision: event.evidence.observedInterfaceRevision!,
          materialGrade: event.evidence.observedMaterialGrade!,
        };
      } else if (event.outcome === 'repairable') {
        requireState(event.evidence.basis === 'measured', 'Repair disposition requires measured inspection evidence');
        asset.location = 'repair';
        asset.condition = 'repairable';
        asset.qualification = null;
      } else if (event.outcome === 'quarantine') {
        asset.location = 'quarantine';
        asset.condition = 'quarantined';
        asset.qualification = null;
      } else {
        requireState(event.evidence.basis === 'measured', 'Feedstock disposition requires measured inspection evidence');
        unusedId(state, event.feedstockLotId ?? '');
        const lot: MaterialLot = {
          id: event.feedstockLotId!, material: asset.material, stage: 'feedstock', massKg: asset.massKg,
          source: { value: `Recovered ${asset.id}`, basis: event.evidence.basis, reference: event.evidence.reference },
          parentAssetIds: [...new Set([...asset.passport.parentAssetIds, asset.id])], status: 'available',
        };
        state.lots[lot.id] = lot;
        asset.location = 'consumed';
        asset.custodianId = lot.id;
        asset.condition = 'quarantined';
        asset.qualification = null;
      }
      record(asset, event, `Inspection outcome: ${event.outcome}; ${event.evidence.notes}`, event.evidence.id);
      break;
    }
    case 'repair': {
      const asset = activeAsset(state, event.assetId);
      requireState(asset.location === 'repair' && asset.condition === 'repairable',
        `Asset ${asset.id} is not in repair`);
      named(event.evidence.id, 'repair evidence ID');
      named(event.evidence.reference, 'repair reference');
      named(event.evidence.method, 'repair method');
      nonnegative(event.evidence.energyKWh, 'repair energy');
      requireState(event.evidence.observedIntegrityRevision === asset.integrityRevision,
        `Stale repair evidence for ${asset.id}`);
      named(event.inspectionCustodianId, 'inspection custodian ID');
      asset.location = 'inspection';
      asset.custodianId = event.inspectionCustodianId;
      asset.condition = 'inspection-required';
      asset.integrityRevision += 1;
      asset.qualification = null;
      record(asset, event, `Mass-neutral repair: ${event.evidence.method}; ${event.evidence.energyKWh} kWh`, event.evidence.id);
      break;
    }
    case 'receive-lot': {
      unusedId(state, event.lot.id);
      requireState(event.lot.status === 'available', 'Received lot must be available');
      requireState(event.lot.stage === 'virgin' || event.lot.stage === 'feedstock',
        'External receipt must be virgin or feedstock');
      positive(event.lot.massKg, 'received lot mass');
      provenance(event.lot.source, 'received lot source');
      state.lots[event.lot.id] = structuredClone(event.lot);
      state.receivedMassKg[event.lot.material] += event.lot.massKg;
      break;
    }
    case 'recycle': {
      const input = availableLot(state, event.inputLotId);
      requireState(input.material === 'steel' && input.stage === 'feedstock',
        'Steel recycling requires a steel feedstock lot');
      unusedId(state, event.outputLotId);
      addProcess(state, event, input, event.outputLotId, event.outputMassKg);
      input.status = 'consumed';
      state.lots[event.outputLotId] = {
        id: event.outputLotId, material: input.material, stage: 'recycled', massKg: event.outputMassKg,
        source: structuredClone(event.provenance), parentAssetIds: [...input.parentAssetIds], status: 'available',
      };
      break;
    }
    case 'reforge': {
      const input = availableLot(state, event.inputLotId);
      requireState(input.material === 'steel' && input.stage === 'recycled',
        'Reforging requires a recycled steel lot');
      const output = event.outputAsset;
      unusedId(state, output.id);
      requireState(output.material === input.material && output.location === 'inspection' &&
        output.condition === 'inspection-required' && output.qualification === null &&
        output.reservedRole === null && output.installedRoleId === null && output.useCount === 0 &&
        output.integrityRevision === 0,
      'Reforged asset must start unqualified in inspection');
      requireState(output.passport.parentAssetIds.length === input.parentAssetIds.length &&
        output.passport.parentAssetIds.every((id, index) => id === input.parentAssetIds[index]),
      'Reforged passport must preserve input asset lineage');
      addProcess(state, event, input, output.id, output.massKg);
      input.status = 'consumed';
      state.assets[output.id] = structuredClone(output);
      record(state.assets[output.id], event, `Reforged from ${input.id}; pending qualification`);
      break;
    }
    default: {
      const unsupported: never = event;
      throw new Error(`Unsupported material action: ${String(unsupported)}`);
    }
  }
  state.revision += 1;
  state.lastAtS = event.atS;
  state.events.push(structuredClone(event));
  assertMaterialLedger(state);
  return state;
}

export function materialBalances(state: MaterialLedgerState): Record<MaterialId, MaterialBalance> {
  const balances = {} as Record<MaterialId, MaterialBalance>;
  for (const material of MATERIALS) {
    const activeAssetMassKg = Object.values(state.assets)
      .filter(asset => asset.material === material && asset.location !== 'consumed')
      .reduce((mass, asset) => mass + asset.massKg, 0);
    const availableLotMassKg = Object.values(state.lots)
      .filter(lot => lot.material === material && lot.status === 'available')
      .reduce((mass, lot) => mass + lot.massKg, 0);
    const unrecoveredMassKg = state.losses.filter(loss => loss.material === material)
      .reduce((mass, loss) => mass + loss.massKg, 0);
    const openingMassKg = state.openingMassKg[material];
    const receivedMassKg = state.receivedMassKg[material];
    balances[material] = { material, openingMassKg, receivedMassKg, activeAssetMassKg,
      availableLotMassKg, unrecoveredMassKg,
      residualKg: openingMassKg + receivedMassKg - activeAssetMassKg - availableLotMassKg - unrecoveredMassKg };
  }
  return balances;
}

/** Structural bookkeeping checks, not a validation of physical yield or mechanical safety. */
export function assertMaterialLedger(state: MaterialLedgerState): void {
  requireState(state.schemaVersion === 1, 'Unsupported material ledger version');
  requireState(Number.isInteger(state.revision) && state.revision >= 0, 'Invalid material ledger revision');
  requireState(state.events.length === state.revision, 'Material ledger event count differs from revision');
  nonnegative(state.lastAtS, 'last material event time');
  requireState(new Set(state.events.map(event => event.id)).size === state.events.length, 'Duplicate material event ID');
  state.events.forEach((event, index) => {
    requireState(event.schemaVersion === 1 && event.expectedRevision === index,
      `Invalid recorded event revision: ${event.id}`);
    requireState(event.atS >= (index === 0 ? 0 : state.events[index - 1].atS),
      `Recorded event time moved backwards: ${event.id}`);
  });
  if (state.events.length) {
    requireState(state.lastAtS === state.events[state.events.length - 1].atS,
      'Last material time differs from event log');
  }
  for (const material of MATERIALS) {
    nonnegative(state.openingMassKg[material], `opening ${material} mass`);
    nonnegative(state.receivedMassKg[material], `received ${material} mass`);
  }
  for (const [id, asset] of Object.entries(state.assets)) {
    requireState(id === asset.id, `Asset identity mismatch: ${id}`);
    positive(asset.massKg, `asset ${id} mass`);
    named(asset.partTypeId, `asset ${id} part type`);
    named(asset.custodianId, `asset ${id} custodian`);
    named(asset.passport.manufactureBatchId, `asset ${id} manufacture batch`);
    requireState(asset.passport.schemaVersion === 1, `Unsupported passport version: ${id}`);
    provenance(asset.passport.grade, `asset ${id} grade`);
    provenance(asset.passport.interfaceRevision, `asset ${id} interface`);
    if (asset.passport.dimensionsM) {
      provenance(asset.passport.dimensionsM, `asset ${id} dimensions`);
      asset.passport.dimensionsM.value.forEach(value => positive(value, `asset ${id} dimension`));
    }
    requireState(Number.isInteger(asset.integrityRevision) && asset.integrityRevision >= 0,
      `Invalid integrity revision: ${id}`);
    requireState(Number.isInteger(asset.useCount) && asset.useCount >= 0, `Invalid use count: ${id}`);
    requireState(new Set(asset.passport.parentAssetIds).size === asset.passport.parentAssetIds.length,
      `Duplicate lineage in ${id}`);
    requireState(!asset.passport.parentAssetIds.includes(id), `Self-parent lineage in ${id}`);
    if (asset.location === 'stock' || asset.location === 'reserved' || asset.location === 'carrier' ||
      asset.location === 'hoist' || asset.location === 'workfront') {
      requireState(asset.condition === 'qualified' && asset.qualification?.basis === 'measured' &&
        asset.qualification.integrityRevision === asset.integrityRevision,
      `Unqualified asset in available custody: ${id}`);
      named(asset.qualification.evidenceId, `asset ${id} qualification evidence ID`);
      positive(asset.qualification.screeningCapacityKN, `asset ${id} screening capacity`);
      requireState(asset.qualification.interfaceRevision === asset.passport.interfaceRevision.value &&
        asset.qualification.materialGrade === asset.passport.grade.value,
      `Qualification and passport conflict: ${id}`);
    }
    if (asset.location === 'stock') requireState(asset.reservedRole === null, `Stock asset remains reserved: ${id}`);
    if (asset.location === 'installed') requireState(asset.installedRoleId !== null, `Installed asset lacks role: ${id}`);
    if (asset.location === 'repair') requireState(asset.condition === 'repairable', `Repair asset is not repairable: ${id}`);
    if (asset.location === 'quarantine') requireState(asset.condition === 'quarantined', `Quarantine condition mismatch: ${id}`);
    if (asset.location === 'consumed') requireState(asset.qualification === null, `Consumed asset remains qualified: ${id}`);
  }
  for (const [id, lot] of Object.entries(state.lots)) {
    requireState(id === lot.id && !state.assets[id], `Lot identity collision: ${id}`);
    positive(lot.massKg, `lot ${id} mass`);
    provenance(lot.source, `lot ${id} source`);
    requireState(new Set(lot.parentAssetIds).size === lot.parentAssetIds.length, `Duplicate lineage in lot ${id}`);
  }
  for (const loss of state.losses) {
    positive(loss.massKg, 'unrecovered mass');
    requireState(loss.disposition === 'unrecovered-process-output', 'Invalid loss disposition');
  }
  for (const balance of Object.values(materialBalances(state))) {
    requireState(Math.abs(balance.residualKg) <= EPSILON_KG * Math.max(1, balance.openingMassKg + balance.receivedMassKg),
      `${balance.material} material account does not reconcile: ${balance.residualKg} kg`);
  }
}
