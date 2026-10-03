import { readFile, access } from 'node:fs/promises';

const spec = JSON.parse(await readFile(new URL('./process-spec.json', import.meta.url), 'utf8'));
const errors = [];
const ids = new Set(spec.tasks.map(task => task.id));
const statuses = new Set(['planned', 'software-only', 'analysis-only', 'partial-local-simulation']);
if (ids.size !== spec.tasks.length) errors.push('Task IDs must be unique.');
if (spec.overallStatus !== 'specified-not-implemented-or-simulated') errors.push('Whole-process status must remain explicitly unimplemented.');
if (spec.executionPolicy.humanPhysicalTasksAllowed !== false || spec.executionPolicy.remoteDrivingCountsAsAutonomous !== false) errors.push('Human-free execution policy is missing.');
for (const task of spec.tasks) {
  for (const field of ['id', 'name', 'machine', 'loadCustody', 'failureHold', 'acceptanceGate', 'statusDetail']) {
    if (typeof task[field] !== 'string' || !task[field].trim()) errors.push(`${task.id}: missing ${field}.`);
  }
  if (!statuses.has(task.status)) errors.push(`${task.id}: unrecognized or overclaimed status.`);
  if (!Array.isArray(task.requiredEvidence) || !task.requiredEvidence.length) errors.push(`${task.id}: missing future evidence requirements.`);
  for (const id of task.prerequisites) if (!ids.has(id)) errors.push(`${task.id}: unknown prerequisite ${id}.`);
  for (const id of task.evidence) if (!spec.evidence[id]) errors.push(`${task.id}: unknown evidence ${id}.`);
  if (task.status !== 'planned' && !task.evidence.length) errors.push(`${task.id}: credited status has no evidence.`);
}
for (const [id, evidence] of Object.entries(spec.evidence)) {
  if (!evidence.scope?.trim()) errors.push(`${id}: evidence scope is missing.`);
  try { await access(new URL(`../../${evidence.path}`, import.meta.url)); }
  catch { errors.push(`${id}: evidence file absent: ${evidence.path}.`); }
}
const done = new Set();
while (done.size < ids.size) {
  const ready = spec.tasks.filter(task => !done.has(task.id) && task.prerequisites.every(id => done.has(id)));
  if (!ready.length) { errors.push('Prerequisite graph has a cycle or unresolved dependency.'); break; }
  ready.forEach(task => done.add(task.id));
}
for (const group of ['ongoingRequirements', 'repeatableStageTasks']) {
  for (const id of spec[group]) if (!ids.has(id)) errors.push(`${group}: unknown task ${id}.`);
}
if (errors.length) { console.error(errors.join('\n')); process.exitCode = 1; }
else console.log(`Specification structure valid: ${spec.tasks.length} proposed tasks, ${Object.keys(spec.evidence).length} scoped evidence references, acyclic precedence graph. No physics or autonomous execution was validated.`);
