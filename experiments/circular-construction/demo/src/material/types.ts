/** Material ledger contract. All masses are kg, energy is kWh, and time is seconds. */
export type MaterialId = 'steel' | 'polymer';
export type ProvenanceBasis = 'measured' | 'catalogue' | 'assumed';
export type AssetKind = 'member' | 'fastener-set' | 'temporary-work' | 'module';
export type AssetLocation =
  | 'stock' | 'reserved' | 'carrier' | 'hoist' | 'workfront' | 'installed'
  | 'inspection' | 'repair' | 'quarantine' | 'consumed';
export type AssetCondition = 'qualified' | 'inspection-required' | 'repairable' | 'damaged' | 'quarantined';

export interface Provenanced<T> {
  value: T;
  basis: ProvenanceBasis;
  reference: string;
}

export interface MaterialRole {
  id: string;
  kind: AssetKind;
  partTypeId: string;
  material: MaterialId;
  requiredMaterialGrade: string;
  interfaceRevision: string;
  /** Illustrative screening threshold; it is not a structural stage check. */
  minScreeningCapacityKN: number;
}

export interface InspectionEvidence {
  id: string;
  basis: ProvenanceBasis;
  reference: string;
  /** Must match the asset when the observation is committed. */
  observedIntegrityRevision: number;
  notes: string;
  /** Required for a qualified outcome. */
  screeningCapacityKN?: number;
  observedInterfaceRevision?: string;
  observedMaterialGrade?: string;
}

export interface RepairEvidence {
  id: string;
  basis: ProvenanceBasis;
  reference: string;
  observedIntegrityRevision: number;
  method: string;
  /** This first ledger supports mass-neutral repair only. */
  energyKWh: number;
}

export interface Qualification {
  evidenceId: string;
  basis: 'measured';
  integrityRevision: number;
  screeningCapacityKN: number;
  interfaceRevision: string;
  materialGrade: string;
}

export interface PassportRecord {
  eventId: string;
  atS: number;
  action: MaterialEvent['action'] | 'opening';
  detail: string;
  evidenceId?: string;
}

export interface MaterialPassport {
  schemaVersion: 1;
  manufactureBatchId: string;
  /** Empty for original stock; new IDs retain all input asset IDs. */
  parentAssetIds: string[];
  grade: Provenanced<string>;
  interfaceRevision: Provenanced<string>;
  dimensionsM?: Provenanced<readonly [number, number, number]>;
  records: PassportRecord[];
}

export interface MaterialAsset {
  id: string;
  kind: AssetKind;
  partTypeId: string;
  material: MaterialId;
  massKg: number;
  passport: MaterialPassport;
  location: AssetLocation;
  custodianId: string;
  condition: AssetCondition;
  integrityRevision: number;
  qualification: Qualification | null;
  reservedRole: MaterialRole | null;
  installedRoleId: string | null;
  useCount: number;
}

export interface MaterialLot {
  id: string;
  material: MaterialId;
  stage: 'virgin' | 'feedstock' | 'recycled';
  massKg: number;
  source: Provenanced<string>;
  parentAssetIds: string[];
  status: 'available' | 'consumed';
}

export interface ProcessRecord {
  eventId: string;
  operation: 'recycle' | 'reforge';
  inputId: string;
  outputId: string;
  material: MaterialId;
  inputMassKg: number;
  outputMassKg: number;
  unrecoveredMassKg: number;
  yieldFraction: number;
  energyKWh: number;
  provenance: Provenanced<string>;
}

export interface MaterialLoss {
  eventId: string;
  material: MaterialId;
  massKg: number;
  /** A tracked disposition, not an assertion that the material disappeared. */
  disposition: 'unrecovered-process-output';
}

export interface MaterialEventLink {
  /** Optional link to the authoritative simulation event and its pre-commit world revision. */
  executionEventId: string;
  worldRevision: number;
}

interface BaseEvent {
  schemaVersion: 1;
  id: string;
  expectedRevision: number;
  atS: number;
  source?: MaterialEventLink;
}

export type MaterialEvent = BaseEvent & (
  | { action: 'reserve'; assetId: string; role: MaterialRole }
  | { action: 'move'; assetId: string; to: 'carrier' | 'hoist' | 'workfront'; custodianId: string }
  | { action: 'install'; assetId: string; roleId: string }
  | { action: 'damage'; assetId: string; description: string }
  | { action: 'remove'; assetId: string; inspectionCustodianId: string }
  | {
      action: 'inspect'; assetId: string; evidence: InspectionEvidence;
      outcome: 'qualified' | 'repairable' | 'quarantine' | 'feedstock';
      stockCustodianId?: string; feedstockLotId?: string;
    }
  | { action: 'repair'; assetId: string; evidence: RepairEvidence; inspectionCustodianId: string }
  | { action: 'receive-lot'; lot: MaterialLot }
  | {
      action: 'recycle'; inputLotId: string; outputLotId: string;
      outputMassKg: number; yieldFraction: number; energyKWh: number;
      provenance: Provenanced<string>;
    }
  | {
      action: 'reforge'; inputLotId: string; outputAsset: MaterialAsset;
      yieldFraction: number; energyKWh: number;
      provenance: Provenanced<string>;
    }
);

export interface MaterialLedgerState {
  schemaVersion: 1;
  revision: number;
  lastAtS: number;
  assets: Record<string, MaterialAsset>;
  lots: Record<string, MaterialLot>;
  openingMassKg: Record<MaterialId, number>;
  receivedMassKg: Record<MaterialId, number>;
  losses: MaterialLoss[];
  processes: ProcessRecord[];
  events: MaterialEvent[];
}

export interface MaterialBalance {
  material: MaterialId;
  openingMassKg: number;
  receivedMassKg: number;
  activeAssetMassKg: number;
  availableLotMassKg: number;
  unrecoveredMassKg: number;
  residualKg: number;
}
