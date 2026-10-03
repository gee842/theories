/** Construction planning coordinates: SI metres, Three.js Y-up; Euler XYZ radians. */
export type Vec3 = [number, number, number];
export interface Pose { position: Vec3; rotation: Vec3 }
export type PartKind = 'pile' | 'foundation' | 'column' | 'beam' | 'brace' | 'floor' | 'roof' | 'facade' | 'core' | 'stair' | 'landing' | 'service' | 'terrace' | 'planter' | 'temp_brace' | 'temp_service';
export type RobotKind = 'carrier' | 'assembler' | 'ground_builder' | 'cargo_rover';
export type ConstructionPhase = 'empty' | 'arrival' | 'bootstrap' | 'foundations' | 'first-frame' | 'climbing' | 'swarm' | 'completion' | 'inspection' | 'recovery' | 'departure' | 'complete';
export type CatalogueId = 'column' | 'beam' | 'beam_half' | 'brace' | 'floor' | 'roof' | 'terrace' | 'facade' | 'core' | 'core_half' | 'entry' | 'stair' | 'landing' | 'service' | 'pile' | 'foundation' | 'planter' | 'temporary_brace';
export interface PartDefinition { id: string; kind: PartKind; catalogueId: CatalogueId; asset: string; assetScale?: Vec3; dimensions: Vec3; massKg: number; finalPose: Pose; floor: number; temporary: boolean; lane: number }
export interface RobotDefinition { id: string; kind: RobotKind; lane: number; home: Vec3 }
export interface TimedPose { time: number; pose: Pose }
export interface RobotTrack { robotId: string; start: number; end: number; action: string; partId?: string; lane: number; waypoints: TimedPose[]; supportIds: string[] }
export interface ConstructionMission { id: string; partId: string; carrierId: string; assemblerId: string; lane: number; arrivalStart: number; arrived: number; pickup: number; secured: number; attached: number; rendezvous: number; captured: number; installed: number; returned: number; prerequisites: string[]; routeSupportIds: string[]; waypoints: TimedPose[]; removalStart?: number; removed?: number; removalWaypoints?: TimedPose[]; recoveryLoadStart?: number; recoveryLoaded?: number; recoveryRoverId?: string; outgoingWaypoints?: TimedPose[] }
export interface Stage { phase: ConstructionPhase; start: number; end: number; label: string }
export interface ConstructionPlan { schemaVersion: 1; evidence: 'planned-motion'; catalogueRevision: string; dimensions: { width: number; depth: number; floors: number; storeyHeight: number; bay: number }; parts: PartDefinition[]; robots: RobotDefinition[]; missions: ConstructionMission[]; tracks: RobotTrack[]; stages: Stage[]; duration: number; notes: string[] }
export type PartStatus = 'incoming' | 'cargo' | 'stored' | 'carried' | 'handoff' | 'installing' | 'installed' | 'recovering' | 'packing' | 'outgoing' | 'removed';
export interface PartState { id: string; kind: PartKind; status: PartStatus; pose: Pose; custodian: string; supports: string[]; progress: number; visible: boolean }
export interface RobotState { id: string; kind: RobotKind; pose: Pose; action: string; payloadId: string | null; supports: string[]; lane: number; progress: number; visible: boolean; /** Cyclic articulation targets, authored motion rather than solved contact. */ locomotion?: 'vertical-climb' | 'ground-travel' | 'frame-traverse' | 'hold'; climbDirection?: 1 | -1; climbStartHeight?: number; gait: number; gripCount: number }
export interface ConstructionSnapshot { time: number; phase: ConstructionPhase; label: string; parts: PartState[]; robots: RobotState[]; installedCount: number; totalCount: number; activeTasks: string[]; complete: boolean; evidence: 'planned-motion' }
