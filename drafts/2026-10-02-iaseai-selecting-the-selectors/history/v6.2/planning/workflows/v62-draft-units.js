export const meta = {
  name: 'v62-draft-units',
  description: 'Draft V6.2 sections 2-12 (core + Supplement + Discussion) as Fable/Opus pairs, merge blind, extend checks, assemble',
  phases: [
    { title: 'Draft', detail: 'Fable and Opus draft each unit independently' },
    { title: 'Merge', detail: 'blind comparison and merge into src/' },
    { title: 'Checks', detail: 'extend checks_v62.py with new independent blocks' },
    { title: 'Build', detail: 'assemble, fix mechanical issues, report' },
  ],
}

const ROOT = '/Users/ren/theories/drafts/2026-10-02-iaseai-selecting-the-selectors'
const V61 = ROOT + '/v6.1'
const V62 = ROOT + '/v6.2'
const MEM = '/Users/ren/.claude/projects/-Users-ren-theories/memory'

const UNITS = [
  { id: 'U02', sec: '§2', core: ['20_s2.md'], supp: ['02_S2.md'], disc: [], focus: 'loopgain (2.2 with part (4) rivals who respond), tdec (S2.1), compound (2.3), channel signs (chansign, S2), meta, bench, pathgen; the corrected lever sentence in the box; carriers glossed; Ren sentence completed; S2 remarks eqgain, delayosc, illustrative Γ ranges' },
  { id: 'U03', sec: '§3', core: ['30_s3.md'], supp: ['03_S3.md'], disc: [], focus: 'blind (3.3 incidence: neutrality vs compliance), boundary (κ divisible), standprice (3.9 general form), twoerrors (new remark), onegroup (3.10), club, psi; §3.6–3.8 tightened in Ren\'s words; §3.8 opening ruling; corpus keys fixed; S3 growprize' },
  { id: 'U04', sec: '§4', core: ['40_s4.md'], supp: ['04_S4.md'], disc: [], focus: 'capture (two directions), costq (per-unit floor), corrrate (4.5 halves, [H_f] three cases + transient, lump sum, Ŷ), humancorr (new prop), alarm (4.8 evidence the model does not control), pausefield scope, slowroute (renamed, re-premised), line-363 repair; S4 capdyn joint simulation results' },
  { id: 'U05', sec: '§5', core: ['50_s5.md'], supp: ['05_S5.md'], disc: [], focus: 'enforce (per-deviation, (5) constraints, new example), detectlink (new), relpunish, restraint, wingives (κ_W), coverage, enough (sharpened rule), talk (unified bias), frontier (two sentences + Ren sentence), Kuran; scissors (new prop) closing the section; S5 jointscissors and the toy' },
  { id: 'U06', sec: '§6', core: ['60_s6.md'], supp: ['06_S6.md'], disc: [], focus: 'subsections 6.1–6.6 per D1-opus; delegatelock p=1; nested (matched variant, tax from a lead); masked (new); internal deployment; tax not fixed (three points); two joints of "our aligned AI is us"; AI mind (bounded objective not enough); topology (sufficient; adversarial independence); 6.8/6.10/6.11 compression or move; inner level rewritten; broad E1 in Ren\'s words; N4; incarnation gloss' },
  { id: 'U07', sec: '§7', core: ['70_s7.md'], supp: ['07_S7.md'], disc: [], focus: 'Table 7.1 thresholds (new, corrected by channel); four loops in Ren\'s words with formal correspondence; "the drive"; branches (Proposition, I′ analogy to prose); raceselects; racepremise ([thm∣prem] + [val]); evidence fixes (EV5 leads by measure; near parity is where standing is priced highest); T-table status repairs; Test Γ re-signed; S7 matrix with four entries per cell; mechanism index updated' },
  { id: 'U08', sec: '§8', core: ['80_s8.md'], supp: ['08_S8.md'], disc: ['08_X8.md'], focus: 'Jones fix; kernel, fallback, survassure; profile, durability; G1–G7 canonical; 8.3(a)–(g) per plan (Bueno de Mesquita reading, persuades-by-promising tone + κ_W, sprint by mechanism, insurance accepts the frame, detectlink reference); 8.4 table; X8 Fudenberg–Koh paragraph, Abecassis moved, failure-mode table for every path (base of tier 3), equal evidence standard for own design' },
  { id: 'U09', sec: '§9', core: ['90_s9.md'], supp: ['09_S9.md'], disc: [], focus: 'Table 9.1 require (R1 limsup, R3a halves, R4 exception, R8 split + liability route, limits incl. internal deployment and open weights, masked classes); nounilateral; coverage can unravel; S9 row-by-row and the crosswalk R ↔ threshold ↔ G-mark ↔ D-test ↔ readiness Q' },
  { id: 'U10', sec: '§10', core: ['a0_s10.md'], supp: ['10_S10.md'], disc: ['10_X10.md'], focus: '10.1 mechanism first + "who builds and funds"; 10.2 share (n vs n−1), levers by channel, positional part (κ_s≤0), what should diffuse; 10.3 safeguards margin condition; 10.4 two loops in Ren\'s words with institutional forms and "fear deepens", fifth strand pace, third strand dual of the drive, guardian with rejected-guardians list; 10.5 six new rows, separation rule plus chamber, monocentric-per-function, DP3, coercive fallback pointing to tier 3; X10 all gameable clauses repaired (Sys I6), nesting option, minimum-tax correction' },
  { id: 'U11', sec: '§11', core: ['b0_s11.md'], supp: ['11_S11.md'], disc: ['11_X11.md'], focus: 'relaxtrust, signal (+ MacKenzie counter-performativity home); E1 narrow/broad, E2 "can be large (C10)", E3; pausevalue; readiness with residence and decision rule; parallel tracks slowest first; dwell depth and recruitable lineage (10.45→3.81); ratchet; Table 11.5 reachable; precedents with limiting conditions; saturation conditional; where things stand per D4 (roles only); X11 corrected' },
  { id: 'U12', sec: '§12', core: ['c0_s12.md'], supp: [], disc: [], focus: 'the judgment merged per plan §4 (tier 1(a)/(b), tier 2 pre-committed mechanism with certified estimator and release rule, tier 3 with coercion under three conditions, reversibility reasons (i)(ii), closing broad-E1 line); 12.2 Meadows beside thresholds, understanding without executive authority, delays/buffers, theory of change; 12.3 cruxes C3a/b, C9a–d, C12, C13, N4; 12.4 conclusion with G1–G7 and Ren\'s meaning' },
]

const COMMON = `
You are working on Ren's theory paper "Changing the AI Trajectory: The Meta-Attractor of Winning and the Generative Alternative", moving it from V6.1 to V6.2. Ren is the author; Claude drafts.

AUTHORITATIVE PLAN: ${V62}/V6.2-PLAN.md. Read it first, in full. Where design memos differ, the plan decides; where the plan is silent, follow the memo it names; failing that, use the judgment of a great paper.
DESIGN MEMOS: ${V62}/planning/D1-architecture-fable.md, ${V62}/planning/D1-architecture-opus.md (section specs: D1-opus §3.3, D1-fable §3; fidelity tables §5.1 in both; judgment §6 in both; coherence rules §7), ${V62}/planning/D2-math-fable.md and ${V62}/planning/D2-math-opus.md (exact statements, proofs, tags and checks by key; scripts and logs in ${V62}/planning/math-fable/ and math-opus/), ${V62}/planning/D4-evidence-notes.md (verified evidence text changes by location, bibliography entries; its "## Verification" section corrects earlier items — the verified version wins).
REVIEWS of V6.1: ${V61}/reviews/ (R-v6.1-*.md in Chinese, REVIEW-v6.1-codex.md, SYNTHESIS-v6.1.md). V6.1 sources: ${V61}/src/{core,supp,disc,reg}/ and assembled ${V61}/THEORY.md, SUPPLEMENT.md, DISCUSSION.md.
REN'S GUIDANCE: ${MEM}/feedback_ren_writing_discipline.md, ${MEM}/feedback_ren_why_and_meaning.md. Corpus: /Users/ren/theories/theories/<slug>/README.md.

REN'S DIRECTION: "no length limit (still want it elegantly short, but let's get the best outcome first) … write v6.2 elegantly, with great coherence and 'is a great paper', not hard rules, … go for the pareto frontier."
STANDING RULES: never name particular states or firms in the body (roles only); do not elevate race-camp arguments beyond what they earn, but meet them at their strongest; E2 (stop) ≠ E3 (slow); judge the game, not the act; growth is not the danger, the mind is; affirmative meaning; NO LOSSY CONSOLIDATION (every V6.1 point in your unit must survive somewhere findable: in your files, or explicitly moved with a note); mechanism first; statements own their conditions (delete the Scope paragraph and the statement must still be true — V6.1's error was compressing premises away).

MARKUP (keyed sources): declare a result with {{!Kind:key}} (Kinds: Definition, Proposition, Theorem, Lemma, Corollary, Remark, Assumption, Table — Table is being added to the assembler); cite as {{key}} (prints "Kind N.k"), {{#key}} (number only), {{>key}} (forward pointer; prints the kind — NEVER write a kind word before {{key}} or {{>key}}); equations {{!eq:key}} and {{eq:key}}; literal braces escaped {{{{ }}}}. Claim tags [def] [val] [thm] [thm∣prem] [prem] [obs] [num] [conj] [rec]. Keys are stable: keep every existing key of your unit (see ${V61}/src/keymap.json) unless the plan retires it; new core keys only those the plan names for your unit; Supplement-only keys may be added with unique names (grep keymap.json and the plan to avoid clashes). Results declared in the Supplement chapter files are numbered S N.k. No result may be used in the core before it is stated, except via {{>key}}.
STYLE: English, plain and precise, Ren's register (mechanism before conclusion; Ren's lines quoted after the mechanism they compress, with [corpus: key]); claim boxes = "> **Claim.** … >\\n> **Why.** …" with conditions as antecedents and tags per sentence, no hedging adverbs; one home per point; hand-off sentence at the end of each section.
`

const DRAFT_SCHEMA = {
  type: 'object',
  properties: {
    files_written: { type: 'array', items: { type: 'string' } },
    items_addressed: { type: 'array', items: { type: 'string' }, description: 'plan/synthesis/review items handled, one line each, e.g. "A2 standprice general form: done in 3.9"' },
    moved_or_dropped: { type: 'array', items: { type: 'string' }, description: 'every V6.1 point of this unit that moved elsewhere (with destination) or was deliberately not carried (with reason)' },
    open_issues: { type: 'array', items: { type: 'string' } },
    word_counts: { type: 'string' },
  },
  required: ['files_written', 'items_addressed', 'moved_or_dropped'],
}

const draftPrompt = (u, tag, dir) => `${COMMON}
YOUR TASK: write the complete V6.2 draft of one unit: Section ${u.sec} of the core, with its Supplement chapter${u.supp.length ? '' : ' (none for this unit)'}${u.disc.length ? ' and its Discussion chapter' : ''}.
Source files to rewrite (start from the V6.1 versions in ${V61}/src/): core ${u.core.map(f => 'core/' + f).join(', ')}; supplement ${u.supp.map(f => 'supp/' + f).join(', ') || '—'}; discussion ${u.disc.map(f => 'disc/' + f).join(', ') || '—'}.
Focus for this unit (the plan has the decisions): ${u.focus}.
Write your draft files ONLY into ${dir}/ using the same relative paths (e.g. ${dir}/core/${u.core[0]}${u.supp[0] ? ', ' + dir + '/supp/' + u.supp[0] : ''}). Do not edit anything in ${V62}/src or elsewhere. You are one of two independent drafters given this identical task; do not look at ${V62}/planning/drafts/ other than your own directory.
Method: (0) your directory may already contain files from an interrupted earlier attempt at this same task (the run stopped on a usage limit): if so, read them, check them against the task, and complete or rewrite them rather than starting blind; (1) read the plan in full; from the four memos read only the parts relevant to your unit (grep them for your section number and your keys, e.g. 'grep -n "§${u.sec.slice(1)}\\|<key>"', and read those passages), the V6.1 files of your unit in full, the review items that touch your unit, and D4's items for your locations; (2) list every V6.1 paragraph/result of your unit and decide where its substance lives in V6.2; (3) write the files whole — not a diff — as a great section of a great paper: the strongest true statements with their conditions inside them, the mechanism first, no repetition of what other sections own, hand-off at the end; (4) every number you state must come from a memo/reviewer script log or a check block named in the plan §7 (cite the block in [num: …]); (5) test-assemble: copy ${V62} to a scratch directory (e.g. /private/tmp/claude-501/v62scratch-${u.id}-${tag}), put your files into its src/, run "python3 src/assemble_v62.py" there, and fix every problem in YOUR files (unknown keys that belong to other units' new keys — twoerrors, humancorr, detectlink, scissors, masked, thresholds — are expected and acceptable; report them).
Return the structured summary.`

const mergePrompt = (u, dirA, dirB) => `${COMMON}
YOUR TASK: produce the final V6.2 version of one unit — Section ${u.sec} (core ${u.core.join(', ')}; supplement ${u.supp.join(', ') || '—'}; discussion ${u.disc.join(', ') || '—'}) — by comparing two independent complete drafts and merging them.
Draft A: ${dirA}/ ; Draft B: ${dirB}/ (same relative paths: core/, supp/, disc/). Their authors' summaries are in ${dirA}/SUMMARY.json and ${dirB}/SUMMARY.json if present. The drafts are anonymized; judge them on the page.
Focus for this unit: ${u.focus}.
Method:
1. Read the plan, both drafts in full, and the V6.1 files of the unit (${V61}/src/...). (If ${V62}/planning/merge-notes/${u.id}.md or this unit's files in ${V62}/src already show partial work from an interrupted earlier merge, check it and continue.)
2. Compare part by part (claim box; each result statement, scope, proof; each paragraph group; each table): for each, take the better version, or graft the best of both, judged by: correctness and completeness of conditions (statements own their conditions), fidelity to the plan and to Ren's words, elegance and economy (Pareto: no point said twice, nothing without its condition), coherence with the rest of the paper (hand-offs, vocabulary of plan §8), and loss (every V6.1 point survives somewhere findable).
3. Verify the mathematics you keep against the D2 memos and their logs; where the two drafts disagree on a statement, decide by derivation, not by vote, and note it.
4. Write the final files to ${V62}/src/core/, ${V62}/src/supp/, ${V62}/src/disc/ (only this unit's files: ${[...u.core.map(f => 'core/' + f), ...u.supp.map(f => 'supp/' + f), ...u.disc.map(f => 'disc/' + f)].join(', ')}).
5. Test-assemble in a scratch copy of ${V62} (e.g. /private/tmp/claude-501/v62merge-${u.id}); fix problems in your files; unknown keys from other units' new keys are acceptable (report them).
6. Write ${V62}/planning/merge-notes/${u.id}.md: for each part, A / B / graft and why (one line each); disagreements resolved by derivation; every V6.1 point moved or not carried and where; open issues for the integration editor; word counts.
Return a summary (300–500 words) of the merge, including which draft contributed more and why, and any issue that needs Ren or the integration editor.`

const checksPrompt = `${COMMON}
YOUR TASK: extend ${V62}/checks_v62.py (the only file you edit, plus its log ${V62}/checks_v62.log and a notes file ${V62}/planning/checks-notes.md) per plan §7.
- The file may already contain substantial partial work from an interrupted earlier attempt at this same task (the run stopped on a usage limit): read the current file first, keep what is sound, and complete it.
- Keep every V6.1 block; relabel EC as a valuation check and LG(C)/(C′) and RH as identities (their printed labels and the S15-style descriptions in comments).
- Port, do not rewrite, the scripts in ${V62}/planning/math-fable/ (f1–f7), ${V62}/planning/math-opus/ (m01–m10) and ${V61}/reviews/scripts-v6.1-*/ into the new independent blocks named in plan §7 (SP, PD, MP, CE, CH, TD, CI ext, PR ext, QS, FF, ES, CR ext, JX, TK, DL ext, HO ext, SH ext, SR, SM, CS ext), each printing the numbers the text will cite and asserting the claimed relations (with tolerances). Codex's eight boundary cases must each appear. Use the same block registration mechanism as the existing file (read it first). Keep total runtime reasonable (target < 10 minutes; heavy MPE grids may use smaller sizes with a flag for the full run, documented).
- Pure Python standard library only (numpy is not installed).
- Run python3 checks_v62.py > checks_v62.log from ${V62}; all blocks must pass. If a ported claim fails, do not loosen it silently: record it in the notes as a finding.
- Write ${V62}/planning/checks-notes.md: each block, its keys, kind (independent/identity/derived), what it asserts, and the key numbers it prints (so text can cite them), and any failures or discrepancies between the two memos' numbers.
Return a summary.`

const buildPrompt = (mergeSummaries) => `${COMMON}
YOUR TASK: integrate the merged units into a building V6.2 and fix mechanical problems. All eleven units (§2–§12 with their Supplement and Discussion chapters) have just been merged into ${V62}/src by separate agents; summaries follow. The front matter (00_head, 10_s01, d0_symbols, supp 00_S0, 13–15, disc X1/X2, registers other than EVIDENCE) has NOT been rewritten yet; it is V6.1's and will be rewritten next — do not rewrite it now, but you may make minimal edits there to keep the build passing (e.g. a reference to a renamed or moved key).
1. Add the Table kind to ${V62}/src/assemble_v62.py if no unit did (numbered in the section counter, printed "Table N.k"); make sure the assembler handles any other kind changes the plan names.
2. Run cd ${V62} && python3 src/assemble_v62.py. Fix: unknown keys (a key renamed in one unit but cited by another; a new key cited with a different name), forward uses in the core (reorder or use {{>key}}), duplicate keys, doubled kind words, leftover markup. Make the smallest correct edit, in src only, preserving each unit's text otherwise.
3. Run python3 src/refs_v62.py from ${V62}/src (it rebuilds the reference lists; read its docstring), add any bibliography entries the units cite that are missing — take complete verified entries from ${V62}/planning/D4-evidence-notes.md (bibliography section, as corrected in its Verification section) or, if absent there, mark them † with the best entry you can verify — then assemble again and run python3 xref_v62.py. Report every remaining failure.
4. Run python3 checks_v62.py > checks_v62.log if the checks agent has finished (it runs in parallel and may still be working — if the file is mid-edit, skip) and report.
5. Cross-unit consistency: grep the assembled THEORY.md for the vocabulary rules of plan §8 (banned: "every forward-looking actor", "manufactures the relative objective", "on any reading of the cruxes", "win this race", "shared flourishing", "systemically false", "decides whether leads compound", "four conditions"), for named states or firms in core prose, for "Proposition Proposition"-type doubles; fix mechanical ones, list judgment ones.
6. Write ${V62}/planning/build-notes.md: what you fixed (file:line, before → after), what remains for the integration editor, per-section word counts, total core words, and the list of keys added/removed vs V6.1's keymap.
Merge summaries:
${mergeSummaries}
Return a summary.`

phase('Draft')
const checksP = agent(checksPrompt, { label: 'checks', phase: 'Checks', effort: 'xhigh' })

const draftStage = async (u) => {
    const i = UNITS.indexOf(u)
    const fableIsA = (i % 2 === 0)
    const dirA = `${V62}/planning/drafts/${u.id}/A`
    const dirB = `${V62}/planning/drafts/${u.id}/B`
    const dirF = fableIsA ? dirA : dirB
    const dirO = fableIsA ? dirB : dirA
    const [f, o] = await Promise.all([
      agent(draftPrompt(u, 'f', dirF) + `\nAlso write your structured summary as JSON to ${dirF}/SUMMARY.json.`, { label: `draft:${u.id}:fable`, phase: 'Draft', model: 'fable', effort: 'xhigh', schema: DRAFT_SCHEMA }),
      agent(draftPrompt(u, 'o', dirO) + `\nAlso write your structured summary as JSON to ${dirO}/SUMMARY.json.`, { label: `draft:${u.id}:opus`, phase: 'Draft', model: 'opus', effort: 'xhigh', schema: DRAFT_SCHEMA }),
    ])
    if (!f || !o) throw new Error(`draft missing for ${u.id}`)
    return { u, dirA, dirB, fableIsA, fable: f, opus: o }
}
const mergeStage = async (d) => {
    const m = await agent(mergePrompt(d.u, d.dirA, d.dirB), { label: `merge:${d.u.id}`, phase: 'Merge', effort: 'xhigh' })
    if (!m) throw new Error(`merge missing for ${d.u.id}`)
    return { id: d.u.id, fableIsA: d.fableIsA, merge: m, fableDraft: d.fable, opusDraft: d.opus }
}
const results = []
for (let b = 0; b < UNITS.length; b += 3) {
  const batch = UNITS.slice(b, b + 3)
  log(`batch ${b / 3 + 1}: ${batch.map(u => u.id).join(', ')}`)
  const r = await pipeline(batch, draftStage, mergeStage)
  results.push(...r)
}

const checks = await checksP
const ok = results.filter(Boolean)
log(`merged ${ok.length}/${UNITS.length} units`)
if (ok.length < UNITS.length) { return { units: ok.map(r => ({ id: r.id, fableIsA: r.fableIsA, merge: r.merge })), checks, build: null, incomplete: true } }
const mergeSummaries = ok.map(r => `--- ${r.id} (Fable was ${r.fableIsA ? 'A' : 'B'}):\n${typeof r.merge === 'string' ? r.merge.slice(0, 3000) : JSON.stringify(r.merge).slice(0, 3000)}`).join('\n')

phase('Build')
const build = await agent(buildPrompt(mergeSummaries) + `\nChecks agent summary:\n${typeof checks === 'string' ? checks.slice(0, 4000) : JSON.stringify(checks).slice(0, 4000)}`, { label: 'build', phase: 'Build', effort: 'xhigh' })

return { units: ok.map(r => ({ id: r.id, fableIsA: r.fableIsA, merge: r.merge })), checks, build }
