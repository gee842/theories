import type { GateDefinition, GateRequirement, ModelIdentity } from './evidence';

export interface VersionedModel { readonly id: string; readonly version: string; }

export interface BeamHandoffModels {
  readonly connectorMotion: VersionedModel;
  readonly robotBeamContact: VersionedModel;
  readonly hoistLoad: VersionedModel;
  readonly beamFrame: VersionedModel;
  readonly jointStrength: VersionedModel;
  readonly hostFrame: VersionedModel;
}

function model(versioned: VersionedModel, scope: string): ModelIdentity {
  return { id: versioned.id, version: versioned.version, scope };
}

function requirement(id: string, checkId: string, connection: GateRequirement['connection'],
  checkModel: ModelIdentity, capacityBasis: 'none' | 'measured'): GateRequirement {
  return {
    id, checkId, connection, model: checkModel,
    acceptedBases: ['measured', 'calculated'],
    acceptedCapacityBases: [capacityBasis],
  };
}

/**
 * Default strict policy for the one-beam experiment. Each scope is a separate
 * physical question. In particular, axial-truss and connector-path screens
 * cannot stand in for beam bending/frame response or joint strength.
 */
export function createBeamHandoffGates(models: BeamHandoffModels): Readonly<{
  guide: GateDefinition;
  transferLoad: GateDefinition;
  detachHoist: GateDefinition;
}> {
  const jointTransfer = model(models.jointStrength, 'installed-end-joint-strength');
  const jointReleased = model(models.jointStrength, 'end-joint-after-hoist-release');
  return {
    guide: {
      id: 'beam-guide', version: '1', action: 'guide', requirements: [
        requirement('connector-path', 'connector-motion', 'part',
          model(models.connectorMotion, 'beam-end-guide-path'), 'none'),
        requirement('beam-contact', 'robot-beam-contact', 'part',
          model(models.robotBeamContact, 'beam-end-guidance-load'), 'measured'),
        requirement('hoist-supported-guide', 'hoist-load', 'part',
          model(models.hoistLoad, 'suspended-beam-guide'), 'measured'),
      ],
    },
    transferLoad: {
      id: 'beam-transfer-load', version: '1', action: 'transfer-load', requirements: [
        requirement('beam-frame', 'beam-frame', 'part',
          model(models.beamFrame, 'installed-beam-frame'), 'measured'),
        requirement('joint-A', 'joint-strength', 'A', jointTransfer, 'measured'),
        requirement('joint-B', 'joint-strength', 'B', jointTransfer, 'measured'),
        requirement('host-frame', 'host-frame', 'part',
          model(models.hostFrame, 'supporting-frame-response'), 'measured'),
      ],
    },
    detachHoist: {
      id: 'beam-detach-hoist', version: '1', action: 'detach-hoist', requirements: [
        requirement('unassisted-beam-frame', 'beam-frame', 'part',
          model(models.beamFrame, 'beam-frame-after-hoist-release'), 'measured'),
        requirement('released-joint-A', 'joint-strength', 'A', jointReleased, 'measured'),
        requirement('released-joint-B', 'joint-strength', 'B', jointReleased, 'measured'),
        requirement('released-host-frame', 'host-frame', 'part',
          model(models.hostFrame, 'host-frame-after-hoist-release'), 'measured'),
      ],
    },
  };
}
