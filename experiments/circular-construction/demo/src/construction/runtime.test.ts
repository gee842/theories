import { Euler, Quaternion } from 'three';
import { cataloguePart, constructionContract } from './catalogue';
import { composePose, interpolatePose, transformedAxis } from './transforms';
import type { Pose, Vec3 } from './types';
import { describe, expect, it } from 'vitest';
import { buildConstructionPlan, restrainedPayloadPose, sampleConstruction, sampleConstructionPart, sampleRoute } from './runtime';

const plan = buildConstructionPlan();
const missionById = new Map(plan.missions.map(m => [m.partId, m]));
function orientation(p: Pose) { return new Quaternion().setFromEuler(new Euler(...p.rotation, 'XYZ')); }
function positionGap(a: Pose, b: Pose) { return Math.hypot(...a.position.map((v, i) => v - b.position[i])); }
describe('continuous twenty-storey construction history', () => {
  it('starts with bare terrain and no visible machines or parts', () => {
    const first = sampleConstruction(plan, 0);
    expect(first.phase).toBe('empty');
    expect(first.parts.every(p => !p.visible)).toBe(true);
    expect(first.robots.every(r => !r.visible)).toBe(true);
    expect(first.installedCount).toBe(0);
  });
  it('brings restrained material with the opening fleet before site facilities exist', () => {
    const arrival = plan.stages.find(s => s.phase === 'arrival')!;
    for (const robot of plan.robots.filter(r => r.kind === 'cargo_rover')) {
      const first = plan.tracks.filter(t => t.robotId === robot.id).sort((a, b) => a.start - b.start)[0];
      expect(first.partId).toBeTruthy();
      expect(first.start).toBeLessThan(arrival.end);
      const state = sampleConstruction(plan, first.start + .1);
      const material = state.parts.find(p => p.id === first.partId)!;
      expect(material.visible).toBe(true);
      expect(material.status).toBe('cargo');
      expect(material.supports).toEqual([robot.id]);
      expect(state.robots.find(r => r.id === robot.id)!.payloadId).toBe(material.id);
      expect(state.installedCount).toBe(0);
    }
    for (const p of plan.parts.filter(p => p.id.startsWith('stair-trimmer'))) {
      expect(p.asset).toBe('kit_beam_half');
      expect(p.assetScale).toEqual([1, 1, 1]);
      expect(p.massKg).toBeGreaterThan(92.928 / 2); // Same complete end connections.
    }
  });
  it('delivers every part through a finite persistent fleet and installs accepted supports before loaded climbs', () => {
    expect(new Set(plan.parts.map(p => p.id)).size).toBe(plan.parts.length);
    expect(plan.missions.length).toBe(plan.parts.length);
    expect(plan.robots.filter(r => r.kind === 'carrier')).toHaveLength(8);
    for (const m of plan.missions) {
      expect(m.arrivalStart).toBeLessThan(m.arrived);
      expect(m.arrived).toBeLessThan(m.pickup);
      expect(m.pickup).toBeLessThan(m.installed);
      expect(m.installed).toBeLessThan(m.returned);
      for (const id of m.prerequisites) expect(missionById.get(id)?.installed, `${m.partId} requires ${id}`).toBeLessThanOrEqual(m.attached);
    }
    const firstClimb = plan.missions.find(m => m.carrierId.startsWith('carrier'))!;
    for (const p of plan.parts.filter(p => p.kind === 'foundation' && !p.temporary)) expect(missionById.get(p.id)!.installed).toBeLessThan(firstClimb.attached);
    expect(missionById.get('column-0-0-0')!.installed).toBeLessThan(firstClimb.attached);
  });
  it('retains both robot supports through fastening and releases only to the installed joint', () => {
    const m = plan.missions.find(m => m.carrierId.startsWith('carrier'))!;
    for (const t of [m.rendezvous + 1, m.captured + 1, m.installed - .01]) {
      const state = sampleConstruction(plan, t).parts.find(p => p.id === m.partId)!;
      expect(state.supports).toContain(m.carrierId);
      expect(state.supports).toContain(m.assemblerId);
      expect(state.visible).toBe(true);
    }
    const installed = sampleConstruction(plan, m.installed).parts.find(p => p.id === m.partId)!;
    expect(installed.status).toBe('installed');
    expect(installed.supports).toEqual([`installed-joint-${m.partId}`]);
  });
  it('keeps every grip route below the accepted column frontier and positions receivers before arrival', () => {
    for (const m of plan.missions.filter(m => m.carrierId.startsWith('carrier'))) {
      const highest = Math.max(...m.routeSupportIds.map(id => plan.parts.find(p => p.id === id)!.finalPose.position[1] + 1.6));
      expect(Math.max(...m.waypoints.map(w => w.pose.position[1])) + .48).toBeLessThanOrEqual(highest);
      const receiver = plan.tracks.find(t => t.robotId === m.assemblerId && t.partId === m.partId && t.action.startsWith('supported receiver'))!;
      expect(receiver.start).toBeLessThan(m.rendezvous);
    }
  });
  it('reserves each loaded lane until the empty robot returns and actually reuses carrier identities', () => {
    for (let lane = 0; lane < 4; lane++) {
      const jobs = plan.missions.filter(m => m.lane === lane && m.carrierId.startsWith('carrier')).sort((a, b) => a.pickup - b.pickup);
      expect(new Set(jobs.map(m => m.carrierId)).size).toBe(2);
      for (let i = 1; i < jobs.length; i++) expect(jobs[i].pickup).toBeGreaterThanOrEqual(jobs[i - 1].returned);
    }
  });
  it('tracks cargo, stocked, carried, handoff, installed states with continuous pickup and placement', () => {
    const m = plan.missions.find(m => m.carrierId.startsWith('carrier'))!;
    const select = (t: number) => sampleConstructionPart(plan, m.partId, t);
    expect(select((m.arrivalStart + m.arrived) / 2).status).toBe('cargo');
    expect(select(m.pickup - 1).status).toBe('stored');
    expect(select(m.secured + 1).status).toBe('carried');
    for (const t of [m.pickup, m.secured, m.rendezvous, m.captured, m.installed]) {
      const a = select(t - .001).pose.position, b = select(t + .001).pose.position;
      expect(Math.hypot(...a.map((v, i) => v - b[i])), `${m.partId} at ${t}`).toBeLessThan(.01);
    }
    expect(sampleRoute(m.waypoints, m.rendezvous).position[1]).toBeGreaterThan(0);
  });
  it('finishes every declared module, removes temporary equipment and leaves no stranded fleet', () => {
    const last = sampleConstruction(plan, plan.duration);
    expect(last.complete).toBe(true);
    expect(last.installedCount).toBe(last.totalCount);
    expect(last.robots.every(r => !r.visible)).toBe(true);
    expect(plan.parts.filter(p => p.kind === 'column')).toHaveLength(20 * 35);
    for (const kind of ['floor', 'roof', 'facade', 'core', 'stair', 'service', 'terrace', 'planter']) expect(last.parts.some(p => p.kind === kind && p.status === 'installed')).toBe(true);
    for (const p of plan.parts.filter(p => p.temporary)) expect(last.parts.find(s => s.id === p.id)?.status).toBe('removed');
  });
  it('keeps recovered equipment visible through a supported handoff and an actual loaded boundary exit', () => {
    for (const definition of plan.parts.filter(p => p.temporary)) {
      const m = missionById.get(definition.id)!;
      const stateAt = (t: number) => sampleConstruction(plan, t);
      const partAt = (t: number) => stateAt(t).parts.find(p => p.id === definition.id)!;
      const packing = partAt((m.recoveryLoadStart! + m.recoveryLoaded!) / 2);
      expect(packing.visible).toBe(true);
      expect(packing.status).toBe('packing');
      expect(packing.supports).toEqual([`builder-${definition.lane % 2}`, m.recoveryRoverId]);
      const t = (m.recoveryLoaded! + m.removed!) / 2;
      const outgoing = partAt(t);
      const rover = stateAt(t).robots.find(r => r.id === m.recoveryRoverId)!;
      expect(outgoing.status).toBe('outgoing');
      expect(outgoing.visible).toBe(true);
      expect(outgoing.supports).toEqual([rover.id]);
      expect(rover.payloadId).toBe(definition.id);
      expect(outgoing.pose.position).toEqual([rover.pose.position[0], rover.pose.position[1] + 1.1, rover.pose.position[2]]);
      for (const boundary of [m.removalStart!, m.removalStart! + 16, m.recoveryLoadStart!, m.recoveryLoaded!]) {
        const a = partAt(boundary - .001).pose.position, b = partAt(boundary + .001).pose.position;
        expect(Math.hypot(...a.map((v, i) => v - b[i])), `${definition.id} at ${boundary}`).toBeLessThan(.01);
      }
      expect(partAt(m.removed! - .001).visible).toBe(true);
      const removed = partAt(m.removed!);
      expect(removed.visible).toBe(false);
      expect(removed.status).toBe('removed');
      expect(removed.pose.position[0]).toBe(-50);
    }
    const lastRecovered = [...plan.missions].filter(m => m.removed !== undefined).sort((a, b) => b.removed! - a.removed!)[0];
    expect(lastRecovered.partId).toBe('mobile-service-skid');
  });
  it('builds a usable nineteen-transition stair shaft with real floor voids and a closed roof deck', () => {
    expect(plan.parts.filter(p => p.kind === 'stair')).toHaveLength(38);
    expect(plan.parts.filter(p => p.kind === 'landing')).toHaveLength(38);
    expect(plan.parts.filter(p => p.id.startsWith('ground-floor-'))).toHaveLength(72);
    for (let f = 0; f < 19; f++) {
      for (let z = 3; z <= 8; z++) expect(plan.parts.some(p => p.id === `floor-${f}-2-${z}`)).toBe(false);
      expect(plan.parts.some(p => p.id === `beam-x-${f}-2-2`)).toBe(false);
      expect(plan.parts.some(p => p.id === `beam-x-${f}-2-3`)).toBe(false);
      expect(plan.parts.find(p => p.id === `stair-${f}-1`)?.finalPose.rotation[1]).toBe(Math.PI);
      expect(plan.parts.find(p => p.id === `core-entry-${f}`)?.asset).toBe('kit_entry');
    }
    expect(plan.parts.filter(p => p.kind === 'floor' && p.floor === 19)).toHaveLength(72);
    expect(plan.parts.filter(p => p.kind === 'roof')).toHaveLength(72);
    expect(plan.parts.some(p => p.id === 'stair-19-0')).toBe(false);
  });
  it('keeps each machine route continuous between jobs instead of resetting to a floor or parking pose', () => {
    for (const robot of plan.robots) {
      const tracks = plan.tracks.filter(t => t.robotId === robot.id).sort((a, b) => a.start - b.start);
      for (let i = 1; i < tracks.length; i++) {
        const previous = tracks[i - 1], next = tracks[i];
        expect(next.start, `${robot.id}: overlapping ${previous.action} / ${next.action}`).toBeGreaterThanOrEqual(previous.end - .001);
        const a = previous.waypoints[previous.waypoints.length - 1].pose.position, b = next.waypoints[0].pose.position;
        expect(Math.hypot(...a.map((v, j) => v - b[j])), `${robot.id}: ${previous.action} -> ${next.action}`).toBeLessThan(.001);
      }
    }
  });
  it('binds physical assets, dimensions and masses to one shared catalogue revision without scaling connection hardware', () => {
    expect(plan.catalogueRevision).toBe(constructionContract.revision);
    for (const p of plan.parts) {
      const material = cataloguePart(p.catalogueId);
      expect(p.asset).toBe(material.asset);
      expect(p.massKg).toBe(material.massKg);
      expect(p.dimensions).toEqual(material.dimensionsM_YUp);
      expect(p.assetScale).toEqual([1, 1, 1]);
    }
    expect(plan.parts.find(p => p.id === 'stair-trimmer-mid-0--3')?.catalogueId).toBe('beam_half');
    expect(plan.parts.find(p => p.id === 'core-entry-0')?.kind).toBe('core');
    expect(plan.parts.find(p => p.id === 'core-entry-0')?.catalogueId).toBe('entry');
    expect(plan.parts.find(p => p.kind === 'temp_brace')?.catalogueId).toBe('temporary_brace');
  });
  it('preserves full part pose through every unload, pickup, capture, installation and outgoing transfer', () => {
    const epsilon = .00001;
    for (const m of plan.missions) {
      const boundaries = [m.arrived, m.arrived + 12, m.pickup, m.secured, m.rendezvous, m.captured, m.installed];
      if (m.removalStart !== undefined) boundaries.push(m.removalStart, m.removalStart + 16, m.recoveryLoadStart!, m.recoveryLoaded!);
      for (const time of boundaries) {
        const a = sampleConstructionPart(plan, m.partId, time - epsilon), b = sampleConstructionPart(plan, m.partId, time + epsilon);
        expect(positionGap(a.pose, b.pose), `${m.partId} position at ${time}`).toBeLessThan(.001);
        expect(orientation(a.pose).angleTo(orientation(b.pose)), `${m.partId} orientation at ${time}`).toBeLessThan(.001);
      }
    }
  });
  it('keeps restrained cargo and carrier loads rigid through turns, with beams transverse to robot forward', () => {
    const examples = [plan.missions.find(m => plan.parts.find(p => p.id === m.partId)?.catalogueId === 'beam' && m.carrierId.startsWith('carrier'))!, plan.missions.find(m => m.partId === 'mobile-service-skid')!];
    for (const m of examples) {
      const p = plan.parts.find(p => p.id === m.partId)!;
      const intervals = [{ id: `cargo-${m.lane}`, start: m.arrivalStart, end: m.arrived }, { id: m.carrierId, start: m.secured, end: m.rendezvous }];
      if (m.removed !== undefined) intervals.push({ id: m.recoveryRoverId!, start: m.recoveryLoaded!, end: m.removed });
      for (const interval of intervals) {
        const robotTracks = plan.tracks.filter(t => t.robotId === interval.id).sort((a, b) => a.start - b.start);
        const times: number[] = [];
        for (const track of robotTracks) for (let i = 1; i < track.waypoints.length; i++) {
          const a = track.waypoints[i - 1], b = track.waypoints[i];
          if (b.time <= a.time) continue;
          if (Math.abs(b.pose.rotation[1] - a.pose.rotation[1]) > .1) times.push((a.time + b.time) / 2);
        }
        times.push((interval.start + interval.end) / 2);
        for (const time of times.filter(t => t > interval.start && t < interval.end)) {
          const track = [...robotTracks].reverse().find(t => t.start <= time)!;
          const robotPose = sampleRoute(track.waypoints, time);
          const actual = sampleConstructionPart(plan, p.id, time).pose;
          const expected = restrainedPayloadPose(robotPose, p, interval.id);
          expect(positionGap(actual, expected)).toBeLessThan(.000001);
          expect(orientation(actual).angleTo(orientation(expected))).toBeLessThan(.000001);
          if (p.kind === 'beam') {
            const beamAxis = transformedAxis(actual, [1, 0, 0]), forward = transformedAxis(robotPose, [1, 0, 0]);
            expect(Math.abs(beamAxis.reduce((dot, value, i) => dot + value * forward[i], 0))).toBeLessThan(.000001);
          }
        }
      }
    }
  });
  it('connects a real exterior door to the core entrance across the uninterrupted ground deck', () => {
    const entry = plan.parts.find(p => p.id === 'building-entry')!;
    expect(entry.kind).toBe('facade'); expect(entry.catalogueId).toBe('entry');
    expect(entry.finalPose.position).toEqual([-1.5, 1.51, -6.12]);
    expect(plan.parts.some(p => p.id === 'facade-x-0-4--6.12' || p.id === 'facade-x-0-5--6.12')).toBe(false);
    const coreDoor = plan.parts.find(p => p.id === 'core-entry-0')!;
    expect(coreDoor.finalPose.position[0]).toBe(entry.finalPose.position[0]);
    const decks = plan.parts.filter(p => p.id.startsWith('ground-floor-'));
    for (let z = -5.9; z <= -1.5; z += .1) {
      expect(decks.some(p => Math.abs(-1.5 - p.finalPose.position[0]) <= p.dimensions[0] / 2 && Math.abs(z - p.finalPose.position[2]) <= p.dimensions[2] / 2)).toBe(true);
      expect(plan.parts.filter(p => p.floor === 0 && p.kind === 'column').some(p => Math.abs(p.finalPose.position[0] + 1.5) < .3 && Math.abs(p.finalPose.position[2] - z) < .3)).toBe(false);
    }
    expect(plan.parts.find(p => p.id === 'building-entry-surround-left')?.catalogueId).toBe('core_half');
    expect(plan.notes.some(note => note.includes('exterior weather qualification remains unverified'))).toBe(true);
  });
  it('reconstructs identical custody and poses after arbitrary backward and forward seeking', () => {
    const t = plan.missions[Math.floor(plan.missions.length / 2)].rendezvous + 5;
    const expected = sampleConstruction(plan, t);
    sampleConstruction(plan, plan.duration); sampleConstruction(plan, 0); sampleConstruction(plan, t * .3);
    expect(sampleConstruction(plan, t)).toEqual(expected);
    expect(sampleConstruction(plan, t).evidence).toBe('planned-motion');
  });
});


describe('rigid pose transforms', () => {
  it('turns the cradle offset and transverse beam together through a right-angle turn', () => {
    const root: Pose = { position: [10, 2, 3], rotation: [0, Math.PI / 2, 0] };
    const beam = plan.parts.find(p => p.catalogueId === 'beam')!;
    const mounted = restrainedPayloadPose(root, beam, 'carrier-0');
    expect(mounted.position[0]).toBeCloseTo(10);
    expect(mounted.position[1]).toBeCloseTo(2);
    expect(mounted.position[2]).toBeCloseTo(3.61);
    const axis = transformedAxis(mounted, [1, 0, 0]);
    expect(axis[0]).toBeCloseTo(-1); expect(axis[1]).toBeCloseTo(0); expect(axis[2]).toBeCloseTo(0);
  });
  it('composes a local mount through parent roll, yaw and pitch without losing relative orientation', () => {
    const parent: Pose = { position: [2, 3, 4], rotation: [.3, .7, -.2] };
    const local: Pose = { position: [-.61, .1, .2], rotation: [.4, -.2, .8] };
    const result = composePose(parent, local);
    const expectedOffset = transformedAxis(parent, local.position);
    expect(result.position).toEqual(expectedOffset.map((v, i) => v + parent.position[i]));
    expect(orientation(result).angleTo(orientation(parent).multiply(orientation(local)))).toBeLessThan(.000001);
  });
  it('interpolates equivalent yaw branches along a short continuous rotation', () => {
    const a: Pose = { position: [0, 0, 0], rotation: [0, Math.PI - .01, 0] };
    const b: Pose = { position: [1, 0, 0], rotation: [0, -Math.PI + .01, 0] };
    const middle = interpolatePose(a, b, .5);
    expect(orientation(a).angleTo(orientation(middle))).toBeCloseTo(.01);
    expect(middle.position).toEqual([.5, 0, 0] as Vec3);
  });
});
