export const meta = {
  name: 'v62-codex-fix',
  description: 'Integrate the two Codex reviews of V6.2: verify each finding against current src, plan repairs, apply by area, add checks, rebuild and re-verify (single Opus agents)',
  phases: [
    { title: 'Verify', detail: 'one agent per Codex track: extract findings, test each against current src' },
    { title: 'Plan', detail: 'dedup and order repairs' },
    { title: 'Fix', detail: 'sequential fixers by area; checks' },
    { title: 'Recheck', detail: 'independent re-check of changed results; registers; build' },
  ],
}

const ROOT = '/Users/ren/theories/drafts/2026-10-02-iaseai-selecting-the-selectors'
const V61 = ROOT + '/v6.1'
const V62 = ROOT + '/v6.2'
const RV = V62 + '/reviews'

const BASE = `
CONTEXT. V6.2 of Ren's theory paper "Changing the AI Trajectory: The Meta-Attractor of Winning and the Generative Alternative" is in ${V62}/ (keyed sources in src/{core,supp,disc,reg}; build from ${V62}: python3 src/assemble_v62.py; (cd src && python3 refs_v62.py); python3 src/assemble_v62.py; python3 xref_v62.py; python3 checks_v62.py > checks_v62.log). Plan: ${V62}/V6.2-PLAN.md.
Two outside-family reviews by Codex were made on the snapshot with THEORY.md SHA-256 f50fb6a1…: ${RV}/REVIEW-v6.2-codex.md (comprehensive: formal F1–F6, F-C1/F-C2; systems and alignment SA-01–SA-09; evidence and governance EG1–EG10; integration I1–I4; with the specialist reports appended, and scripts/logs in ${RV}/formal-audit, systems-audit, harness-audit, counterexamples_v62_codex.py) and ${RV}/REVIEW-v6.2-codex-second.md (nine findings; scripts in ${RV}/codex-second/ and counterexamples_v62_codex_second.py). Line numbers in them refer to that snapshot; the current src may have moved since, because an internal verification round (${RV}/R-v6.2-*.md, C-v6.2-*.md, FIXES-v6.2-verify.md) applied its own confirmed fixes after the snapshot.
Ren's decisions: V6.2 is the complete theory of record (length accepted; a short paper later); Definition 2.1 three conditions plus closure; coercive restriction in the compared tier with three conditions; R9 kept; "if growth and change are favoured". Standing rules: no named states or firms in the body (roles); do not elevate race-camp arguments beyond what they earn; E2 ≠ E3; judge the game, not the act; growth is not the danger, the mind is; affirmative meaning; no lossy consolidation; mechanism first; statements own their conditions. Repairs keep what is correct (Codex says which sub-results survive) and narrow what is not; never weaken a check tolerance to keep a claim.
MARKUP: {{!Kind:key}} declares; {{key}} cites ("Kind N.k"); {{#key}}; {{>key}} forward pointer (never write a kind word before {{key}}/{{>key}}); {{!eq:key}}/{{eq:key}}; supp declarations are S-numbered. Edit src/ only; never assembled documents. Pure Python standard library for scripts (no numpy).
`

const VERDICTS = {
  type: 'object',
  properties: {
    track: { type: 'string' },
    findings: {
      type: 'array',
      items: {
        type: 'object',
        properties: {
          id: { type: 'string' },
          priority: { type: 'string' },
          keys: { type: 'array', items: { type: 'string' } },
          current_location: { type: 'string', description: 'file:line in CURRENT src' },
          status: { type: 'string', enum: ['holds', 'partly', 'already-fixed', 'refuted', 'needs-ren'] },
          reason: { type: 'string' },
          repair: { type: 'string', description: 'exact repair to make in current src: statement, proof, citations, checks' },
          check_to_add: { type: 'string', description: 'assertion(s) to add to checks_v62.py, if any' },
        },
        required: ['id', 'status', 'reason'],
      },
    },
  },
  required: ['track', 'findings'],
}

const TRACKS = [
  { id: 'formal', what: `the FORMAL track of ${RV}/REVIEW-v6.2-codex.md (synthesis items 1–2 and F1–F6, F-C1, F-C2 in the formal report section) AND the second review ${RV}/REVIEW-v6.2-codex-second.md findings that concern §§2–5 mathematics (balanced growth and the standing price; responsive-rival price; detection link; any others on §§2–5)` },
  { id: 'systems', what: `the SYSTEMS AND ALIGNMENT track of ${RV}/REVIEW-v6.2-codex.md (synthesis items 3–4 and SA-01–SA-09) AND the second review's findings that concern §§6, 9–11 and the readiness/transition results` },
  { id: 'governance', what: `the EVIDENCE AND GOVERNANCE track of ${RV}/REVIEW-v6.2-codex.md (synthesis item 5 and EG1–EG10, including the 18-entry source audit) AND the second review's findings that concern §§7–8, 12, the cruxes, activation/withdrawal rules, evidence and comparisons` },
  { id: 'integration', what: `the INTEGRATION track of ${RV}/REVIEW-v6.2-codex.md (I1–I4: test-runner exit status, preservation sample, research-outline operationalization, entry route) AND any remaining finding of either review not covered by the formal, systems or governance tracks (list them all; say which track owns them)` },
]

const verifyPrompt = (t) => `${BASE}
YOUR TASK: take ${t.what}. Extract EVERY finding (id, priority, keys). For each, test it against the CURRENT src (not the snapshot): locate the passage now (file:line), reproduce the demonstration or counterexample with your own script (scratch: /private/tmp/claude-501/v62codexfix/${t.id}/; you may run Codex's scripts too), decide: holds (the problem is present now), partly (present but the proposed repair is wrong or overstated — give the corrected repair), already-fixed (the internal round fixed it — say where), refuted (show why), or needs-ren (a value or wording choice that is Ren's). For each that holds or partly: write the exact repair (new statement wording with all its conditions, proof changes, every citing place to update by key, and the check assertion to add, with the numbers it must reproduce). Keep correct sub-results. Do not edit project files. Write ${RV}/CF-${t.id}.md (one entry per finding) and return the structured list.`

const planPrompt = (lists) => `${BASE}
YOUR TASK: build one repair plan from the verified Codex findings below (four tracks). Deduplicate (the two reviews overlap: e.g. the responsive-rival price, the detection link); where two repairs conflict, decide by derivation and say why; order the repairs by dependency (statements before the places that cite them; math before tables, boxes, abstract, §1.2, guide, registers). Assign each repair to exactly one of four areas: A = §§2–3 and S2–S3 (and their check blocks); B = §§4–6 and S4–S6, X2; C = §§7–12, S7–S11, S13–S14, X8, X10, X11, TESTS, EVIDENCE; D = front matter (00_head abstract and guide, 10_s01 §0–§1, symbols, S0), CLAIMS, LEDGER, CHANGELOG, README, checks_v62.py harness changes (exit status; new assertions for every counterexample). For each repair give: id(s), area, files and keys, the exact change, the citing places to update, the assertion to add. Cross-area propagation (a statement in A cited in C) is listed under the later area. Needs-Ren items are listed separately, not repaired. Do not edit project files. Write ${V62}/planning/codex-fix-plan.md and return it in full.
VERIFIED FINDINGS:
${lists}`

const fixPrompt = (area, scope) => `${BASE}
YOUR TASK: apply area ${area} of the repair plan ${V62}/planning/codex-fix-plan.md (read it in full, and the CF-*.md notes it cites). Area ${area} covers: ${scope}. Edit only the files of your area in src/ (and, for area D, checks_v62.py). Make each repair exactly as planned unless you find it wrong on the page (then fix it correctly and note why). Keep keys, tags, Ren's words and every condition; when a statement changes, update its proof, its check block, and every place in YOUR area that cites it; list citing places in other areas you could not reach. Test-assemble after your edits (no problems; refs and xref pass). Write ${V62}/planning/codex-fix-${area}.md: each repair applied (file, before → after) or not (why), and propagation left for later areas. Return a summary.`

const recheckPrompt = `${BASE}
YOUR TASK: independent re-check after the Codex repairs. Read ${V62}/planning/codex-fix-plan.md and codex-fix-{A,B,C,D}.md. For every statement that changed: re-derive it, run your own numerical check (scratch: /private/tmp/claude-501/v62codexfix/recheck/), and confirm (a) the Codex counterexample no longer applies, (b) the correct sub-results survive, (c) every place that cites it (abstract, §1.2, guide, claim boxes, Table 7.1, §12, registers) now says the same with the same conditions. Then run the full build: python3 src/assemble_v62.py; (cd src && python3 refs_v62.py); python3 src/assemble_v62.py; python3 xref_v62.py; python3 checks_v62.py > checks_v62.log; and python3 src/sentcheck.py ${V61}/THEORY.md THEORY.md SUPPLEMENT.md DISCUSSION.md --min 0.4 (report the count and adjudicate anything new). Fix only mechanical problems and propagation misses (smallest edits in src); report anything substantive. Write ${RV}/RECHECK-v6.2-codex-fixes.md (in English): per repaired finding: closed / partly / open, with evidence; build and check status; the needs-Ren list. Return a summary.`

phase('Verify')
const lists = await parallel(TRACKS.map(t => () => agent(verifyPrompt(t), { label: `verify:${t.id}`, phase: 'Verify', effort: 'xhigh', schema: VERDICTS })))
const got = lists.filter(Boolean)
if (got.length < TRACKS.length) return { incomplete: true, got }
const flat = got.map(l => `### ${l.track}\n` + l.findings.map(f => `- [${f.id}] ${f.priority || ''} status=${f.status} keys=${(f.keys || []).join(',')} at ${f.current_location || ''}\n  reason: ${f.reason}\n  repair: ${f.repair || ''}\n  check: ${f.check_to_add || ''}`).join('\n')).join('\n\n')

phase('Plan')
const plan = await agent(planPrompt(flat.slice(0, 180000)), { label: 'plan', phase: 'Plan', effort: 'xhigh' })
if (!plan) return { incomplete: true, stage: 'plan' }

phase('Fix')
const AREAS = [
  ['A', '§§2–3 (src/core/20_s2.md, 30_s3.md) and S2–S3 (src/supp/02_S2.md, 03_S3.md)'],
  ['B', '§§4–6 (src/core/40_s4.md, 50_s5.md, 60_s6.md), S4–S6 (src/supp/04_S4.md, 05_S5.md, 06_S6.md), X2 (src/disc/02_X2.md)'],
  ['C', '§§7–12 (src/core/70_s7.md … c0_s12.md), S7–S11 and S13–S14 (src/supp/07_S7.md … 11_S11.md, 13_S13.md, 14_S14.md), X8, X10, X11 (src/disc/08_X8.md, 10_X10.md, 11_X11.md), TESTS and EVIDENCE (src/reg/TESTS.md, EVIDENCE.md)'],
  ['D', 'front matter (src/core/00_head.md, 10_s01.md, d0_symbols.md; src/supp/00_S0.md, 15_S15.md), CLAIMS, LEDGER, CHANGELOG, README (src/reg/), X1 (src/disc/01_X1.md), and checks_v62.py (harness: intended failures affect exit status; an assertion for every Codex counterexample and every repaired statement; run it and log to checks_v62.log)'],
]
const fixes = []
for (const [a, scope] of AREAS) {
  const r = await agent(fixPrompt(a, scope), { label: `fix:${a}`, phase: 'Fix', effort: 'xhigh' })
  fixes.push(r)
}

phase('Recheck')
const recheck = await agent(recheckPrompt, { label: 'recheck', phase: 'Recheck', effort: 'xhigh' })
return { tracks: got.map(l => ({ track: l.track, n: l.findings.length, holds: l.findings.filter(f => f.status === 'holds' || f.status === 'partly').length })), plan: String(plan).slice(0, 4000), fixes, recheck }
