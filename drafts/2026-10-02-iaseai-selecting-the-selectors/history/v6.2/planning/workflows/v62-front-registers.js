export const meta = {
  name: 'v62-front-registers',
  description: 'V6.2 front matter (abstract, guide, §0–§1, symbols, S0) drafted and reviewed by single agents; companions X1/X2 and S13–S15; checks ports; registers; whole-core coherence read; build',
  phases: [
    { title: 'Front', detail: 'abstract, guide, §0–§1, symbols, S0: draft, then critical review' },
    { title: 'Companions', detail: 'X1/X2 with verification; S13–S15; check ports' },
    { title: 'Registers', detail: 'TESTS, CLAIMS; then LEDGER, CHANGELOG, README' },
    { title: 'Coherence', detail: 'one reader lists edits; one editor applies' },
    { title: 'Build', detail: 'assemble, refs, xref, checks' },
  ],
}

const ROOT = '/Users/ren/theories/drafts/2026-10-02-iaseai-selecting-the-selectors'
const V61 = ROOT + '/v6.1'
const V62 = ROOT + '/v6.2'
const SNAP = V62 + '/planning/snapshots/draftA'
const MEM = '/Users/ren/.claude/projects/-Users-ren-theories/memory'

const BASE = `
CONTEXT. Ren's theory paper "Changing the AI Trajectory: The Meta-Attractor of Winning and the Generative Alternative", V6.2, in ${V62}/ (keyed sources in src/{core,supp,disc,reg}; build from ${V62}: python3 src/assemble_v62.py; python3 src/refs_v62.py run from src/; python3 xref_v62.py; python3 checks_v62.py > checks_v62.log). Plan: ${V62}/V6.2-PLAN.md. Sections 2–12 with their Supplement and Discussion chapters are final for now (merged by Fable/Opus pairs, then an elegance pass; notes in ${V62}/planning/merge-notes/, ${V62}/planning/elegance-notes/, ${V62}/planning/elegance-build-notes.md, ${V62}/planning/build-notes.md). Design memos: ${V62}/planning/D1-architecture-{fable,opus}.md, D2-math-{fable,opus}.md, D4-evidence-notes.md (the verified bibliography and evidence wording; its Verification section wins). Reviews of V6.1: ${V61}/reviews/ (SYNTHESIS-v6.1.md first). V6.1 for comparison: ${V61}/. The pre-elegance snapshot of V6.2: ${SNAP}/. Ren's guidance: ${MEM}/feedback_ren_writing_discipline.md, ${MEM}/feedback_ren_why_and_meaning.md; corpus /Users/ren/theories/theories/<slug>/README.md.
REN'S DIRECTION: "no length limit (still want it elegantly short, but let's get the best outcome first) … write v6.2 elegantly, with great coherence and 'is a great paper', not hard rules, … go for the pareto frontier."
STANDING RULES: never name particular states or firms in the body (roles only); do not elevate race-camp arguments beyond what they earn; E2 ≠ E3; judge the game, not the act; growth is not the danger, the mind is; affirmative meaning; no lossy consolidation; mechanism first; statements own their conditions.
MARKUP: {{!Kind:key}} declares; {{key}} cites ("Kind N.k"); {{#key}} number; {{>key}} forward pointer (prints the kind; never write a kind word before {{key}}/{{>key}}); {{!eq:key}}/{{eq:key}}; {{{{ }}}} escapes; supp declarations are S-numbered. Edit src/ only, never assembled documents. Test-assemble in a scratch copy (cp -R ${V62} /private/tmp/claude-501/<unique>) before writing to ${V62}/src when other agents may be writing at the same time.
`

const FRONT_FILES = ['core/00_head.md', 'core/10_s01.md', 'core/d0_symbols.md', 'supp/00_S0.md']

const frontPrompt = (dir) => `${BASE}
YOUR TASK: write the V6.2 front matter from the FINAL sections: ${FRONT_FILES.join(', ')} (V6.1 versions in ${V61}/src/; current ones in ${V62}/src/ are still V6.1's with minimal build edits).
- 00_head.md: title (unchanged); status line (plan §2; D1-opus §3.2: drafted by Claude from Ren's direction; reviewed by one model outside the drafting family (Codex) at V6.1; not yet reviewed by outside readers); an ENGLISH ABSTRACT (new; D1-opus §1.2 draft, rewritten to match the final statements exactly — read §2–§12 first); the 中文导读 (plan §6: structure from D1-fable §5.3 — 用途与意义, 核心, 论证链 nine items mirroring §1.2 item by item, 判断 in the three tiers exactly as final §12.1 has them, including coercive restriction in the compared tier with its three conditions and broad E1 as scope, 怎样读 — plus D1-opus's short 不主张什么; natural modern Chinese in Ren's register; 母体 throughout; banned: 宿主, 签名, 闭合于自身, 这个过程是好的, 弱化身, 强化身; about 2,400 字 at most).
- 10_s01.md: §0 Why this theory (D1-opus §3.2 draft, adapted: the game-not-act paragraph with broad E1's aggregate mechanism; the affirmative meaning with Ren's identity wording "We are not only our separate lives: we are the larger process of becoming, going on through us, and that is good. Decay and renewal belong to its growth."; check final §12.4 so the two do not repeat each other's sentences); §1.1 with the puzzle and Codex's organizing question; §1.2 The argument in one page — nine items, each conditional, mirroring the final statements (compounding prices standing where the relative return exceeds the common return; levers by channel with "at least in proportion" (U02 merge note); the scissors' arms and pivot with co-movement C0; talk as amplification n/(n−2) fading with n, blocs not claimed; masked divergences; internal deployment; "each actor computes correctly; the game is wrong"; "we are one" as the long-term requirement; the three tiers); §1.3 values (V1 in Ren's planetary-technology wording; N4 sentence); §1.4 what is claimed and what is not (levels, tags, the not-claimed list including the name sentence, what is new positioned against the literature as D1-opus §3.2 says, review status, reading paths: thirty minutes = abstract or guide, §0, §1.2, §1.4, claim boxes, Table 7.1, §12).
- d0_symbols.md and supp/00_S0.md: the symbol table updated to every rename in the final sections (grep the merge and elegance notes for renames); restrict the "one meaning" claim to the table's symbols; S0's notation and premise list updated (keys, tags, premises in words, new premises).
Vocabulary: plan §8.3. Banned in English: "every forward-looking actor", "manufactures the relative objective", "on any reading of the cruxes", "win this race", "shared flourishing", "systemically false", "decides whether leads compound".
Write ONLY into ${dir}/ with the same relative paths (${FRONT_FILES.map(f => dir + '/' + f).join(', ')}) plus ${dir}/NOTES.md. Test-assemble with your files in a scratch copy; run python3 xref_v62.py there and make the guide/§1.2 term match pass. You are one of two independent drafters; do not look at the other's directory.
Return a summary (300 words).`

const frontMergePrompt = (dirA, dirB) => `${BASE}
YOUR TASK: produce the final V6.2 front matter (${FRONT_FILES.join(', ')}) by comparing two independent drafts and merging them. Draft A: ${dirA}/ ; Draft B: ${dirB}/ (each with NOTES.md); anonymized. Read the final §2–§12 first. Judge part by part: exact fidelity to the final statements (the abstract, §1.2 and the guide must say what the sections prove, with the same conditions, no more and no less); Ren's voice and register (the guide in natural Chinese, 母体, no banned terms); elegance; the guide mirroring §1.2 item by item and §12.1's tiers exactly. Graft freely. Write the final files to ${V62}/src/ (only those four files). Assemble, run refs and xref (all must pass, including the guide term match), and write ${V62}/planning/front-notes.md (A/B/graft per part; open issues; for Ren: every English rendering of his words and every model paraphrase to be marked D). Return a summary.`

const x1Prompt = `${BASE}
YOUR TASK: bring DISCUSSION X1 (lineage and literature, ${V62}/src/disc/01_X1.md) and X2 (substrates, ${V62}/src/disc/02_X2.md) to V6.2. Edit only these two files.
- X1: corpus keys corrected (R-v6.1-fidelity 重要6: 讲理／讲赢 → alignment-selection with jian-and-wenyan, 2026-05-05; five endgames → selfishness-spiral, prompt.md 2025-02-27; 力之所及，责之所在 → shengsheng, the book 2026-07-14 l.357; the reform dilemma marked "not verified against an original"); a date column, verified against each corpus README's source list; a jian-and-wenyan row; every corpus key the final core uses ([corpus: …]) present in the table with its source and date (grep the assembled THEORY.md/SUPPLEMENT.md for [corpus:); the lineage-gap works with one sentence each on what this paper absorbs and what it adds (D4-evidence-notes §(c); R-v6.1-adversarial-opus I7): Grieco 1988, Snidal 1991, Powell 1999, Gilbert–Newbery 1982, Budd–Harris–Vickers 1993, Athey–Schmutzler 2001, Aghion et al. 2001, Avenhaus–von Stengel–Zamir 2002, Schelling–Halperin 1961, Kydd 2000, Shavell 1986, Grossman–Helpman 1994, Askell–Brundage–Hadfield 2019, prover–estimator debate (Brown-Cohen, Irving and Piliouras 2025), Meadows 1999, Kuran 1995, MacKenzie 2006, Harris–Vickers 1987, Konrad–Kovenock 2009; "what is new" rewritten to match the final §1.4 (Γ as the organization of known instability results; the price of standing as Powell 1991 generalized by the common channel; selecting the selectors; the enforcement condition split into p_d and p̄_d with its comparative statics; the nested loop under the alignment-tax premise; where integration must be anticipated); the alignment-literature paragraph updated (masked divergences, control, gradual disempowerment, hidden loyalties, the tax literature of 2024–26) per R-v6.1-alignment and D4.
- X2: Caulin & Maley qualified with Butler et al. 2025 (D4 wording); other instances checked against the final §2.4.
Bibliography: every work you cite must be in the reference data (src/refs_v62.py reads D4's entries; read its docstring); use the verified entries from D4; for any you add beyond D4, verify on the web (WebSearch/WebFetch; load with ToolSearch "select:WebSearch,WebFetch" if deferred) and mark the status honestly.
Assemble in a scratch copy, run refs and xref there; then write your two files to ${V62}/src/disc/. Write ${V62}/planning/x1-notes.md. Return a summary.`

const x1VerifyPrompt = (prev) => `${BASE}
YOUR TASK: adversarially verify the new DISCUSSION X1 and X2 (${V62}/src/disc/01_X1.md, 02_X2.md). Another agent wrote them; summary: """${String(prev).slice(0, 2500)}"""
For every corpus key and date: open the corpus README (/Users/ren/theories/theories/<slug>/README.md) and the cited source, and try to refute the attribution (wrong folder, wrong date, a model's paraphrase presented as Ren's words). For every literature sentence ("absorbs … adds …"): check the work says what is attributed (web where needed; WebSearch/WebFetch via ToolSearch if deferred). Fix errors directly in those two files (only), assemble in a scratch copy to confirm, and append "## Verification" to ${V62}/planning/x1-notes.md listing each item as confirmed / corrected / unverifiable. Return a summary.`

const s13Prompt = `${BASE}
YOUR TASK: bring Supplement chapters S13 (interfaces between models), S14 (counterexamples) and S15 (map of numerical checks) to V6.2: ${V62}/src/supp/13_S13.md, 14_S14.md, 15_S15.md (edit only these).
- S13: every interface the final sections name (grep the assembled THEORY/SUPPLEMENT for "S13" and "interface"), including "Human capacity and correction", "stocks and stage payoffs", "T_dec set by Λ*", loop gain and breakout probability, capacity and the field ("partly run": the joint simulations), and the status of each (proved / numerical / open).
- S14: the counterexample table updated with every counterexample the final text uses or the reviews established (Codex's eight boundary cases with their blocks; the growing prize with r<1; the Markov laggard; unequal incidence; the strict role-differentiated punishment; the falling floor transient; the signal(2) correction of U11; the delegation interior equilibrium at p<1; nonlinear fitness), each with its key, what it refutes or bounds, and its check block.
- S15: the map of check blocks from ${V62}/checks_v62.py and ${V62}/planning/checks-notes.md: every block, its kind (independent / identity / valuation / derived), the keys it serves, what it asserts. Verify that every [num: X] tag in the assembled THEORY, SUPPLEMENT and DISCUSSION names a block that exists in checks_v62.py (or a legacy block named as such); list any that do not in ${V62}/planning/s13-notes.md for the checks agent.
Assemble in a scratch copy; write the three files; write ${V62}/planning/s13-notes.md. Return a summary.`

const checksPrompt = `${BASE}
YOUR TASK: complete ${V62}/checks_v62.py (edit only it, its log, and ${V62}/planning/checks-notes.md). Read ${V62}/planning/checks-notes.md, ${V62}/planning/build-notes.md and the merge/elegance notes for requested ports.
- Port planning/drafts/U11/A/checks/tr_transition.py as block TR (the text cites [num: TR]); port the U06 nearlock script into DL and the homeostasis two-root example into SM if not already present; port any other script the final text cites by block name that is missing (grep the assembled THEORY/SUPPLEMENT/DISCUSSION for "[num:" and list every block name; each must exist or be a documented legacy block).
- Keep every existing block and assertion; do not loosen tolerances; record any failure as a finding.
- Run python3 checks_v62.py > checks_v62.log from ${V62}; all must pass. Update checks-notes.md. Return a summary listing every [num:] block name used in the text and its status.`

const testsClaimsPrompt = `${BASE}
YOUR TASK: rewrite the registers TESTS and CLAIMS for V6.2: ${V62}/src/reg/TESTS.md and ${V62}/src/reg/CLAIMS.md (edit only these two).
TESTS: cruxes C0–C13 and N1–N4 exactly as final §12.3 defines them (C3a/C3b, C9a–d, C12 verifiability, C13 dependence on the governed, N4 standing of AI systems), each with what it would change and its next measurement; the robustness matrix (tier 1(a) items × C0–C13, each cell why it stands: information, lead time, equilibrium without trust, public good) and tier 1(b) items with the crux that would withdraw each; registered conditions; Tests A–M and Γ with rival predictions as the final text states them — Test Γ re-signed (observable 1+θ, rising with provision and diffusion relative to stakes), Test G discriminating at intermediate p_d (the hump when D>C), Test L redesigned by cost incidence with detectability held fixed (R-v6.1-alignment I7 table), Test M relabelled a remedy test (Codex), Test B with entry barriers as the discriminating contrary; the indicators of tier 2 with their estimators; Study 2 updated with what the joint simulations found (conservative under monotone cost decline, optimistic after reversals and where correction rests on eroded human capacity; the failure signature from the slow variable) and what remains; the research programme including the meta-loop toy as a suggestion (Sys m3), a Γ calibration template by channel (ranges, not estimates), one sentence on ASTRA (or state why not), catch-up contests, the multiplicity of Markov equilibria for outside review; "rates of human overrule" replaced by catch rates of planted errors; the readiness reading of today pointed to X11; independence of review (family bias, what Codex checked).
CLAIMS: the thesis in the abstract's conditional form; definitions fixed in advance; the inventory of every result by stable key with its V6.2 number (read src/keymap.json after assembling), tag and status; the dependency chain by threshold (Table 7.1); open interfaces (S13); the disposition of every V6.1 review item (SYNTHESIS §二 table and §四 A–H, and every important item of each review) as fixed / narrowed / declined (reason) / open, including v6.0 alignment B3/B4 and minors 3, 4, 6 that V6.1 never recorded; "Evidence asymmetries and citation errors" as partly repaired with I1–I6; a "D" list: every English rendering of Ren's words and every model paraphrase in the text that Ren has not confirmed (collect from merge-notes, elegance-notes and front-notes "For Ren" sections and by grepping [corpus: …] sentences), with location; R9 (human decision authority) flagged for Ren's confirmation; the Meadows reading flagged.
Assemble in a scratch copy; write both files; write ${V62}/planning/registers-notes.md. Return a summary.`

const ledgerPrompt = `${BASE}
YOUR TASK: rewrite LEDGER, CHANGELOG and README for V6.2: ${V62}/src/reg/LEDGER.md, CHANGELOG.md, README.md (edit only these, plus a new ${V62}/LEDGER-v62-sentences.tsv).
LEDGER: (1) crosswalk of every result V6.1 → V6.2 by key (number, kind, core or Supplement), generated from ${V61}/src/keymap.json and ${V62}/src/keymap.json; (2) a sentence-level preservation ledger V6.1 → V6.2: run python3 src/sentcheck.py ${V61}/THEORY.md THEORY.md SUPPLEMENT.md DISCUSSION.md --min 0.4 --all (from ${V62}, after assembling) and write every V6.1 core sentence with its containment and, for each below 0.4, a disposition (restated where, moved where, corrected why, withdrawn why) into LEDGER-v62-sentences.tsv; summarize in LEDGER; (3) restated / corrected / withdrawn / declined items of this round (plan §9; each withdrawal with a one-line reason; the nine V6.1 withdrawals given reasons, two reclassified as restated, per R-v6.1-fidelity 次要1); (4) the fidelity table of R-v6.1-fidelity 重要5 (14 losses) with each V6.2 home; (5) unledgered V6.1 changes now recorded (entry barriers; the hysteresis prediction; Meadows → threshold reading, flagged for Ren); (6) LEDGER §5's blanket sentence removed and §7's "S5" misrecord corrected; earlier versions kept.
CHANGELOG: V6.2 entry: Ren's direction and the decisions (Definition 2.1 three plus closure, departing from the plan's four; coercion moved to tier 3; no cap; Ultracode workflows with Fable/Opus pairs and blind merges); what changed in the argument (the tightenings of plan §1); the structure (abstract; thresholds table; new keys; kinds; results moved to the Supplement); length (V6.1 30.5k core; the merged draft 59.5k; after the elegance pass N); checks (blocks, assertions, Codex's boundary cases); deviations from the plan and from the synthesis (each with reason: e.g. "at least in proportion"; R9; admission burden of proof in tier 1(b); the name sentence in §1.4); not done (Codex review of V6.2; Ren's read; items held for outside review).
README: files; reading paths regenerated from the final structure (thirty minutes; policy; formal; alignment — adding §8.3(a), X8 technical alignment, X1 alignment literature, EV6; systems and design; evidence and IR; readers of V6.1 → LEDGER first); rebuilding instructions with the v62 scripts and src/sentcheck.py.
Assemble in a scratch copy; write the files. Return a summary.`

const coherencePrompt = (tag, dir) => `${BASE}
YOUR TASK: read the whole assembled V6.2 core (${V62}/THEORY.md, after running python3 src/assemble_v62.py in a scratch copy so it is current) as the integration editor, from the abstract to the conclusion, and judge it as a great paper: one voice; one home per point; conditions owned by statements; claim boxes that a thirty-minute reader can trust; hand-offs; vocabulary (plan §8.3); no repetition across sections; no contradiction between sections (e.g. §6.6 vs §12.1 on when admission applies; the "four conditions" of correction vs Definition 2.1; quotation conventions; numbers cited in two places that differ); Ren's voice; the standing rules.
Do NOT edit any file. Write ${dir}/COHERENCE-${tag}.md: a prioritized list of concrete edits, each with file (src path) and the exact current text and the exact replacement (or the exact move), and why. Keep to edits that make the paper better on the page; for each, say whether it is necessary (an error or contradiction) or improving. Also list anything that the core reader needs and cannot find. You are one of two independent readers; do not look at the other's file. Return the path and the top ten edits.`

const applyPrompt = (fpath, opath) => `${BASE}
YOUR TASK: apply the integration edits. Two independent readers (anonymized) wrote edit lists: ${fpath} and ${opath}. Read both and the assembled core. Apply every necessary edit (errors, contradictions) that you confirm on the page; apply improving edits where both agree or where you judge the improvement clear; where they conflict, decide and note why. Edit src/ only (core, supp, disc, reg as needed), smallest correct change, keeping the mathematics, keys, tags, Ren's words and conditions. Then assemble, run refs and xref (all must pass), and write ${V62}/planning/coherence-notes.md (every edit applied or declined, with reason). Return a summary.`

const finalBuildPrompt = `${BASE}
YOUR TASK: final build of V6.2. From ${V62}: python3 src/assemble_v62.py; (cd src && python3 refs_v62.py); python3 src/assemble_v62.py; python3 xref_v62.py; python3 checks_v62.py > checks_v62.log. Fix mechanical failures (smallest edits in src). Then report: per-section core words, supplement and discussion words, number of results, xref status, checks status (assertions passed), and run python3 src/sentcheck.py ${V61}/THEORY.md THEORY.md SUPPLEMENT.md DISCUSSION.md --min 0.4 and python3 src/sentcheck.py ${SNAP}/THEORY.md THEORY.md SUPPLEMENT.md DISCUSSION.md --min 0.5 and report the counts below threshold with a short adjudication of any that look substantive. Write ${V62}/planning/final-build-notes.md. Return a summary.`

// ---- run ----
phase('Front')
const dirF = `${V62}/planning/front/single`
const frontP = (async () => {
  const a = await agent(frontPrompt(dirF).replace('You are one of two independent drafters; do not look at the other\'s directory.', ''), { label: 'front:draft', phase: 'Front', effort: 'xhigh' })
  if (!a) throw new Error('front draft missing')
  return agent(frontMergePrompt(dirF, dirF).replace('by comparing two independent drafts and merging them. Draft A: ' + dirF + '/ ; Draft B: ' + dirF + '/ (each with NOTES.md); anonymized.', 'by reviewing the draft in ' + dirF + '/ (with NOTES.md) critically against the final sections and improving it.'), { label: 'front:review', phase: 'Front', effort: 'xhigh' })
})()

const x1P = (async () => {
  const w = await agent(x1Prompt, { label: 'X1/X2', phase: 'Companions', effort: 'high' })
  const v = await agent(x1VerifyPrompt(w), { label: 'X1/X2:verify', phase: 'Companions', effort: 'high' })
  return { w, v }
})()
const checksP = agent(checksPrompt, { label: 'checks', phase: 'Companions', effort: 'high' })

const [front, x1, checks] = await Promise.all([frontP.catch(e => null), x1P.catch(e => null), checksP])
const s13 = await agent(s13Prompt, { label: 'S13-S15', phase: 'Companions', effort: 'high' })

phase('Registers')
const tc = await agent(testsClaimsPrompt, { label: 'TESTS+CLAIMS', phase: 'Registers', effort: 'xhigh' })
const led = await agent(ledgerPrompt, { label: 'LEDGER+CHANGELOG+README', phase: 'Registers', effort: 'high' })

phase('Coherence')
const cdir = `${V62}/planning/coherence`
const cf = await agent(coherencePrompt('A', cdir).replace('You are one of two independent readers; do not look at the other\'s file.', ''), { label: 'read', phase: 'Coherence', effort: 'xhigh' })
const applied = await agent(applyPrompt(`${cdir}/COHERENCE-A.md`, `${cdir}/COHERENCE-A.md`).replace('Two independent readers (anonymized) wrote edit lists', 'An integration reader wrote an edit list (given twice below; it is one file)'), { label: 'apply', phase: 'Coherence', effort: 'xhigh' })

phase('Build')
const fin = await agent(finalBuildPrompt, { label: 'final build', phase: 'Build', effort: 'high' })
return { front, x1, checks, s13, tc, led, applied, fin }
