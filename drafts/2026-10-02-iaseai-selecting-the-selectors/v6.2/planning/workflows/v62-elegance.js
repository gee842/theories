export const meta = {
  name: 'v62-elegance',
  description: 'Elegance pass on V6.2 sections 2-12: Fable/Opus edit each section toward the Pareto frontier by moving (not deleting) detail to the companions, blind merge, then a whole-core preservation check and build',
  phases: [
    { title: 'Edit', detail: 'Fable and Opus edit each unit independently' },
    { title: 'Merge', detail: 'blind comparison and merge into src/' },
    { title: 'Preserve', detail: 'sentence-level check against the snapshot; restore losses; build' },
  ],
}

const ROOT = '/Users/ren/theories/drafts/2026-10-02-iaseai-selecting-the-selectors'
const V61 = ROOT + '/v6.1'
const V62 = ROOT + '/v6.2'
const SNAP = V62 + '/planning/snapshots/draftA'
const MEM = '/Users/ren/.claude/projects/-Users-ren-theories/memory'

const UNITS = [
  { id: 'U02', sec: '§2', core: ['20_s2.md'], supp: ['02_S2.md'], disc: [], now: 4007, target: 2700 },
  { id: 'U03', sec: '§3', core: ['30_s3.md'], supp: ['03_S3.md'], disc: [], now: 5452, target: 3700 },
  { id: 'U04', sec: '§4', core: ['40_s4.md'], supp: ['04_S4.md'], disc: [], now: 4473, target: 3000 },
  { id: 'U05', sec: '§5', core: ['50_s5.md'], supp: ['05_S5.md'], disc: [], now: 5579, target: 3700 },
  { id: 'U06', sec: '§6', core: ['60_s6.md'], supp: ['06_S6.md'], disc: [], now: 6015, target: 3800 },
  { id: 'U07', sec: '§7', core: ['70_s7.md'], supp: ['07_S7.md'], disc: [], now: 5563, target: 3200 },
  { id: 'U08', sec: '§8', core: ['80_s8.md'], supp: ['08_S8.md'], disc: ['08_X8.md'], now: 5388, target: 3300 },
  { id: 'U09', sec: '§9', core: ['90_s9.md'], supp: ['09_S9.md'], disc: [], now: 3089, target: 1600 },
  { id: 'U10', sec: '§10', core: ['a0_s10.md'], supp: ['10_S10.md'], disc: ['10_X10.md'], now: 6520, target: 3800 },
  { id: 'U11', sec: '§11', core: ['b0_s11.md'], supp: ['11_S11.md'], disc: ['11_X11.md'], now: 5921, target: 3200 },
  { id: 'U12', sec: '§12', core: ['c0_s12.md'], supp: [], disc: [], now: 5321, target: 3000 },
]

const BRIEF = `
CONTEXT. Ren's theory paper "Changing the AI Trajectory: The Meta-Attractor of Winning and the Generative Alternative" is being revised to V6.2 in ${V62}/ (keyed sources in src/{core,supp,disc,reg}; build: python3 src/assemble_v62.py from ${V62}). The plan is ${V62}/V6.2-PLAN.md. Sections 2–12 were just rewritten by Fable/Opus pairs and merged (merge notes: ${V62}/planning/merge-notes/Uxx.md). The result is correct, complete and well conditioned, but the merges took the union of two drafts and the core doubled, from 30.5k words (V6.1) to 59.5k. The full merged version is preserved as a snapshot in ${SNAP}/ (src/ and assembled documents).

REN'S DIRECTION: "no length limit (still want it elegantly short, but let's get the best outcome first) … write v6.2 elegantly, with great coherence and 'is a great paper', not hard rules, … go for the pareto frontier." The best outcome now exists; this pass makes it elegant. A point on the frontier is one where nothing can be cut from the core without making it less correct, less complete in its conditions, or less useful to a reader, and nothing the reader of the core needs is only in the companions.

WHAT THE CORE IS FOR. The core argues: claim boxes, definitions, result statements with every condition their proofs use, the mechanism in prose, Ren's own lines after the mechanisms they compress, the consequences, hand-offs. The SUPPLEMENT proves and computes: proofs, derivations, numerical illustrations, extended scope details, secondary results, robustness tables. The DISCUSSION holds lineage, alternatives in full, design in full, transition in full, worked instances.

HOW TO GET THERE (judgment, not procedure):
- MOVE, never delete. Any sentence that leaves the core goes to the unit's Supplement chapter (or Discussion chapter, where named), next to the result or topic it serves, with a pointer from the core where a reader would want it ("S5 gives the numbers"). The only text that may disappear is a true duplicate of something said elsewhere in the paper — then note where.
- STATEMENTS OWN THEIR CONDITIONS. Never shorten a result statement by dropping a premise (V6.1's error). Shorten by moving illustrations and number tables out of statements and Scope paragraphs. A Scope paragraph in the core says, in two or three sentences, what the result does not cover and what would make it fail; the numbers that illustrate it go to the Supplement. A [num] claim stays in the core only where the argument needs the number.
- Side results not cited by Parts II–IV and not on the spine (plan §1) may move to the Supplement, keeping their keys (they become S-numbered; check every {{key}} citing them still reads correctly), with one core sentence that carries their conditions.
- Claim boxes: Claim and Why, conditions as antecedents, tags per sentence, about 90–140 words in all.
- Prose: one home per point (plan §8); no sentence whose only job is to restate; tighter sentences; mechanism first; Ren's quoted lines stay in the core, verbatim with their corpus keys (bracketed repairs as they stand).
- Keep every key, every claim tag, every Ren ruling restored in this round (plan §5; merge notes "For Ren"), every condition the reviews asked for, and the vocabulary of plan §8.
- Do not change the mathematics. If you find an error, fix it minimally and record it.

TARGET for this unit's core: about the figure given below (a guide, not a cap; justify any large deviation in your notes by naming what the extra words carry). The companion chapters may grow by what they receive.

VERIFY before finishing:
1. Test-assemble in a scratch copy (cp -R ${V62} /private/tmp/claude-501/<unique>; put your files into its src/; python3 src/assemble_v62.py there): no problems from your files.
2. Run the sentence-level preservation check on your unit against the snapshot: python3 src/sentcheck.py ${SNAP}/src/core/<file> <your new core file> <your new supp/disc files> <the other current src core/supp/disc files> --min 0.5 (run it from a directory where src/sentcheck.py exists, e.g. the scratch copy). Every sentence listed must be accounted for in your notes: moved (where), merged into another sentence (which), duplicate of (where), or restored. Do the same for the unit's Supplement/Discussion chapters if you rewrote any of their existing text.
3. Count words: python3 src/assemble_v62.py prints per-section counts.

STANDING RULES: no named states or firms in the body (roles only); do not elevate race-camp arguments beyond what they earn; E2 ≠ E3; judge the game, not the act; growth is not the danger, the mind is; affirmative meaning; no lossy consolidation; mechanism first.
MARKUP: {{!Kind:key}} declares; {{key}} cites (prints "Kind N.k"); {{#key}} number; {{>key}} forward pointer (prints the kind; never write a kind word before {{key}} or {{>key}}); {{!eq:key}}/{{eq:key}}; {{{{ }}}} escapes. Declarations in supp/ files are S-numbered.
`

const EDIT_SCHEMA = {
  type: 'object',
  properties: {
    files_written: { type: 'array', items: { type: 'string' } },
    core_words_before_after: { type: 'string' },
    moved: { type: 'array', items: { type: 'string' }, description: 'what moved from core to which companion location, one line each' },
    duplicates_removed: { type: 'array', items: { type: 'string' }, description: 'sentence removed as a duplicate, with where the point lives' },
    other_changes: { type: 'array', items: { type: 'string' } },
    open_issues: { type: 'array', items: { type: 'string' } },
  },
  required: ['files_written', 'core_words_before_after', 'moved'],
}

const filesOf = (u) => [...u.core.map(f => 'core/' + f), ...u.supp.map(f => 'supp/' + f), ...u.disc.map(f => 'disc/' + f)]

const editPrompt = (u, dir) => `${BRIEF}
YOUR TASK: the elegance pass for Section ${u.sec}: core ${u.core.join(', ')} (now about ${u.now} words; target about ${u.target}); companions ${[...u.supp, ...u.disc].join(', ') || '— (none: anything leaving this section goes to the chapter of the section it serves, or to a Supplement chapter named in a note; prefer keeping §12 whole if it is already tight)'}.
Start from the CURRENT files in ${V62}/src/ (identical to the snapshot). Read the plan, the unit's merge notes (${V62}/planning/merge-notes/${u.id}.md), the current files of the unit in full, and enough of the neighbouring sections to keep hand-offs right. Your directory may already contain files from an interrupted earlier attempt at this same task: check and complete them.
Write your edited files ONLY into ${dir}/ with the same relative paths (${filesOf(u).map(f => dir + '/' + f).join(', ')}). Do not edit ${V62}/src. You are one of two independent editors given this identical task; do not look at the other's directory.
Also write ${dir}/NOTES.md (moves, duplicates removed, preservation-check adjudication, word counts, open issues) and return the structured summary.`

const mergePrompt = (u, dirA, dirB) => `${BRIEF}
YOUR TASK: produce the final elegant version of Section ${u.sec} (files: ${filesOf(u).join(', ')}) by comparing two independent edits of the same current text and merging them.
Edit A: ${dirA}/ ; Edit B: ${dirB}/ (same relative paths; each has NOTES.md). Anonymized: judge on the page. The current (pre-edit) files are in ${V62}/src/ and the snapshot ${SNAP}/src/.
Judge part by part by: (1) nothing the core reader needs went missing, and every statement still owns its conditions; (2) elegance and economy; (3) coherence and voice; (4) fidelity to Ren's words; (5) the moved material is well placed and findable. Take the better edit of each part, or graft. Where one editor cut something the other kept and the core reader needs it, keep it. Do not exceed the target by much unless the extra words carry conditions or Ren's words; do not go far below it if that loses what a reader needs.
Write the final files to ${V62}/src/ (only: ${filesOf(u).join(', ')}). Test-assemble in a scratch copy; run the sentence-level preservation check of the snapshot's unit files against the final ${V62}/src (all core/supp/disc files) and adjudicate every listed sentence (restore anything substantive that was lost from both edits).
Write ${V62}/planning/elegance-notes/${u.id}.md: per part A / B / graft and why; the preservation adjudication; word counts before/after (core and companions); open issues for the integration editor or Ren.
Return a 200–400 word summary.`

const buildPrompt = (summaries) => `${BRIEF}
YOUR TASK: after the elegance pass of all eleven units, make the whole build pass and check preservation across units.
1. cd ${V62} && python3 src/assemble_v62.py ; fix any cross-unit problem (a key moved to the Supplement now cited in the core before its statement, kind words, forward uses) with the smallest edit in src.
2. Run python3 src/refs_v62.py from ${V62}/src, then assemble again, then python3 xref_v62.py. The guide/§1.2 mismatch is expected (front matter is rewritten next); report anything else.
3. Whole-core preservation: python3 src/sentcheck.py ${SNAP}/THEORY.md THEORY.md SUPPLEMENT.md DISCUSSION.md --min 0.5 (after assembling). Adjudicate every listed sentence: if its substance is now elsewhere, note where; if it was lost, restore it to the right place in src (core if the core reader needs it, else the companion) and record it. Also run python3 src/sentcheck.py ${V61}/THEORY.md THEORY.md SUPPLEMENT.md DISCUSSION.md --min 0.4 to confirm no V6.1 point was lost across the two passes; adjudicate the same way.
4. python3 checks_v62.py > checks_v62.log (about five minutes); report failures.
5. Write ${V62}/planning/elegance-build-notes.md: fixes, the two preservation adjudications (every listed sentence with its disposition), per-section word counts (core, supplement, discussion), open issues.
Unit summaries:
${summaries}
Return a summary.`

const editStage = async (u) => {
  const i = UNITS.indexOf(u)
  const fableIsA = (i % 2 === 1)
  const dirA = `${V62}/planning/edit/${u.id}/A`
  const dirB = `${V62}/planning/edit/${u.id}/B`
  const dirF = fableIsA ? dirA : dirB
  const dirO = fableIsA ? dirB : dirA
  const [f, o] = await Promise.all([
    agent(editPrompt(u, dirF), { label: `edit:${u.id}:fable`, phase: 'Edit', model: 'fable', effort: 'xhigh', schema: EDIT_SCHEMA }),
    agent(editPrompt(u, dirO), { label: `edit:${u.id}:opus`, phase: 'Edit', model: 'opus', effort: 'xhigh', schema: EDIT_SCHEMA }),
  ])
  if (!f || !o) throw new Error(`edit missing for ${u.id}`)
  return { u, dirA, dirB, fableIsA, f, o }
}
const mergeStage = async (d) => {
  const m = await agent(mergePrompt(d.u, d.dirA, d.dirB), { label: `merge:${d.u.id}`, phase: 'Merge', effort: 'xhigh' })
  if (!m) throw new Error(`merge missing for ${d.u.id}`)
  return { id: d.u.id, fableIsA: d.fableIsA, merge: m, fable: d.f, opus: d.o }
}

const results = []
for (let b = 0; b < UNITS.length; b += 4) {
  const batch = UNITS.slice(b, b + 4)
  log(`batch ${b / 4 + 1}: ${batch.map(u => u.id).join(', ')}`)
  const r = await pipeline(batch, editStage, mergeStage)
  results.push(...r)
}
const ok = results.filter(Boolean)
log(`merged ${ok.length}/${UNITS.length}`)
if (ok.length < UNITS.length) return { units: ok.map(r => ({ id: r.id, merge: r.merge })), build: null, incomplete: true }

phase('Preserve')
const summaries = ok.map(r => `--- ${r.id} (Fable was ${r.fableIsA ? 'A' : 'B'}):\n${String(r.merge).slice(0, 2500)}`).join('\n')
const build = await agent(buildPrompt(summaries), { label: 'build+preserve', phase: 'Preserve', effort: 'xhigh' })
return { units: ok.map(r => ({ id: r.id, fableIsA: r.fableIsA, merge: r.merge })), build }
