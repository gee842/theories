import assert from 'node:assert/strict';
import { createHash } from 'node:crypto';
import { readFileSync } from 'node:fs';
import { join } from 'node:path';

const root = new URL('../', import.meta.url).pathname;
const json = path => JSON.parse(readFileSync(join(root, path), 'utf8'));
const near = (a, b, tolerance, label) => assert.ok(Number.isFinite(a) && Math.abs(a - b) <= tolerance, `${label}: ${a} vs ${b}`);

function glbDocument(path) {
  const file = readFileSync(join(root, path));
  assert.equal(file.toString('ascii', 0, 4), 'glTF');
  assert.equal(file.readUInt32LE(4), 2);
  const jsonLength = file.readUInt32LE(12);
  assert.equal(file.toString('ascii', 16, 20), 'JSON');
  return JSON.parse(file.toString('utf8', 20, 20 + jsonLength));
}
function glbNodes(data) {
  const names = new Map();
  for (const node of data.nodes) names.set(node.name, [...(names.get(node.name) ?? []), node]);
  return names;
}
function one(nodes, name) {
  const matches = nodes.get(name) ?? [];
  assert.equal(matches.length, 1, `${name} must be a unique glTF node`);
  return matches[0];
}

function levelSteelVertices(data, level) {
  const levelNode = data.nodes.find(node => node.name === `Level_${String(level).padStart(2, '0')}`);
  assert.ok(levelNode, `Level ${level} exists`);
  const steel = levelNode.children.map(index => data.nodes[index]).find(node => node.name.startsWith('StructuralSteel'));
  assert.ok(steel, `Level ${level} steel group exists`);
  return steel.children.flatMap(index => data.meshes[data.nodes[index].mesh].primitives)
    .reduce((sum, primitive) => sum + data.accessors[primitive.attributes.POSITION].count, 0);
}

const siteDocument = glbDocument('public/assets/tower-site.glb');
const plannedDocument = glbDocument('public/assets/planned-architecture.glb');
const site = glbNodes(siteDocument);
const planned = glbNodes(plannedDocument);
const robot = glbNodes(glbDocument('public/assets/climber-robot.glb'));
const trace = json('public/assets/workcell-trace.json');
const structure = json('public/assets/tower-structure.json');
const nominal = json('production/physics/mujoco/nominal-validation.json');
const missed = json('production/physics/mujoco/missed-seat-validation.json');
const beam = one(site, 'lifted_beam');
const hoist = one(site, 'ActiveHoist');

assert.equal(beam.extras.length, 5.6);
assert.match(beam.extras.section, /450 x 300 x 9 \/ 18mm/);
near(beam.extras.mass_kg, nominal.beamMassKg, .001, 'Blender/MuJoCo beam mass kg');
near(structure.activeBeam.massKg, nominal.beamMassKg, 1e-7, 'OpenSees/MuJoCo beam mass kg');
near(structure.loads.activeBeamMassKg, nominal.beamMassKg, 1e-7, 'Imported structural beam load kg');
for (let level = 1; level <= 20; level++) one(site, `Level_${String(level).padStart(2, '0')}`);
for (let level = 1; level <= 20; level++) one(planned, `Level_${String(level).padStart(2, '0')}`);
assert.match(one(planned, 'ConstructionSite').extras.stage, /design study/i);
assert.equal(one(planned, 'ConstructionSite').extras.finish_levels, 20);
one(planned, 'FinishModule_20');
one(planned, 'CoreModule_20');
assert.equal(planned.has('TowerCrane'), false);
assert.equal(planned.has('lifted_beam'), false);
assert.equal(planned.has('ActiveHoist'), false);
assert.equal(levelSteelVertices(plannedDocument, 12) - levelSteelVertices(siteDocument, 12), 72, 'The planned design closes the active I-beam gap');
one(site, 'RobotGripRails');
one(site, 'TemporaryYBraces');
for (const binding of trace.bindings) one(binding.assetId === 'robot' ? robot : site, binding.node);
assert.equal(trace.bindings.length, 16);
assert.deepEqual(trace.units, { length: 'm', time: 's', force: 'N' });
assert.equal(trace.coordinates, 'gltf-y-up');
assert.equal(trace.frames.length, 601);
const initial = trace.frames[0].bodies;
for (let i = 0; i < 3; i++) {
  near(beam.translation[i], initial.lifted_beam.position[i], 1e-4, `Initial beam origin ${i}`);
  near(hoist.translation[i], initial.hoist_carrier.position[i], 1e-4, `Initial carrier origin ${i}`);
}
assert.equal(trace.frames.at(-1).state.support, 'two seats');
assert.equal(trace.frames.at(-1).state.connection, 'seated, unfastened');
assert.equal(nominal.hoistReleased, true);
assert.equal(missed.hoistReleased, false);
near(nominal.finalSeatLoadsN.seat_left + nominal.finalSeatLoadsN.seat_right, nominal.beamMassKg * 9.81, 1, 'Final seat weight N');
assert.equal(structure.negativeSeatCase.status, 'unstable-mechanism');
const digest = createHash('sha256').update(readFileSync(join(root, 'production/physics/mujoco/nominal-validation.json'))).digest('hex');
assert.equal(structure.source.sha256, digest, 'Structural export must identify current physics result');
console.log('Production integrity verified: 20 levels, closed planned beam gap, 16 bindings, aligned origins and section mass, positive/negative support, structural source hash.');
