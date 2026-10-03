import { build } from 'esbuild';
import { createHash } from 'node:crypto';
import { readFile, writeFile } from 'node:fs/promises';
const compiled = await build({ entryPoints: ['src/construction/runtime.ts'], bundle: true, write: false, metafile: true, platform: 'node', format: 'esm' });
const runtime = await import(`data:text/javascript;base64,${Buffer.from(compiled.outputFiles[0].text).toString('base64')}`);
const plan = runtime.buildConstructionPlan();
const state = runtime.sampleConstruction(plan, plan.duration);
const hash = (bytes) => createHash('sha256').update(bytes).digest('hex');
const missions = new Map(plan.missions.map(m => [m.partId, m]));
const sourceDependencies = {};
for (const path of Object.keys(compiled.metafile.inputs).filter(path => !path.includes('node_modules/'))) sourceDependencies[path] = hash(await readFile(path));
const result = {
  schemaVersion: 1, coordinates: 'Three.js Y-up', units: 'm, kg, s',
  evidence: plan.evidence, dimensions: plan.dimensions,
  sourceSha256: hash(await readFile('src/construction/runtime.ts')),
  compiledSha256: hash(compiled.outputFiles[0].text), sourceDependencies,
  contractSha256: hash(await readFile('production/contracts/carrier-construction.json')),
  durationSeconds: plan.duration, notes: plan.notes,
  parts: plan.parts.map(p => ({ ...p, installedAt: missions.get(p.id).installed })),
  stages: plan.stages,
  final: { installed: state.installedCount, required: state.totalCount, remainingRobots: state.robots.filter(r => r.visible).length, complete: state.complete },
};
await writeFile('production/structure/carrier/site-plan.json', JSON.stringify(result, null, 2)+'\n');
console.log(JSON.stringify({ parts: result.parts.length, final: result.final, hours: result.durationSeconds / 3600 }));
