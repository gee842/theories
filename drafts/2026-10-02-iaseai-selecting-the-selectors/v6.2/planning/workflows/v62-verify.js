export const meta = {
  name: 'v62-verify',
  description: 'Verify V6.2 with single Opus agents: five reviews, adversarial confirmation of each finding, one fixer, rebuild',
  phases: [
    { title: 'Review', detail: 'math (two halves), loss and fidelity, cold read, evidence' },
    { title: 'Confirm', detail: 'try to refute each review\'s findings' },
    { title: 'Fix', detail: 'apply confirmed findings; rebuild; checks' },
  ],
}

const ROOT = '/Users/ren/theories/drafts/2026-10-02-iaseai-selecting-the-selectors'
const V61 = ROOT + '/v6.1'
const V62 = ROOT + '/v6.2'
const MEM = '/Users/ren/.claude/projects/-Users-ren-theories/memory'

const BASE = `
You are reviewing V6.2 of Ren's theory paper "Changing the AI Trajectory: The Meta-Attractor of Winning and the Generative Alternative", in ${V62}/ : THEORY.md (core, ~56k words, Parts I–IV, English abstract and Chinese guide at top), SUPPLEMENT.md (proofs, ~59k), DISCUSSION.md (~21k), registers CLAIMS, EVIDENCE, TESTS, LEDGER (+ LEDGER-v62-sentences.tsv), CHANGELOG, README; checks_v62.py with checks_v62.log (188 assertions); keyed sources in src/. The plan: ${V62}/V6.2-PLAN.md. The review round on V6.1 and its synthesis: ${V61}/reviews/ (SYNTHESIS-v6.1.md). Process notes: ${V62}/planning/ (merge-notes, elegance-notes, front-notes, coherence-notes, registers-notes, x1-notes, s13-notes, checks-notes, final-build-notes).
Ren's decisions (4 Oct 2026): V6.2 is the complete theory of record (length is accepted; a separate short paper will be written later); Definition 2.1 is three conditions plus the reflexive closure; coercive restriction of inputs sits in the compared tier with three conditions; R9 kept; "if growth and change are favoured" (his word).
Standing rules: never name particular states or firms in the body (roles only); do not elevate race-camp arguments beyond what they earn; E2 ≠ E3; judge the game, not the act; growth is not the danger, the mind is; affirmative meaning; no lossy consolidation; mechanism first; statements own their conditions.
Rules for you: do not edit any project file; write only your report (path below) and scripts in your scratch folder (pure Python standard library; numpy is not installed). Derive and compute independently; do not trust the draft, its notes or the checks. You are the same model family as the drafter; say where that bias could matter. Write the report in 简体中文 (findings may quote English): 总判断 (3–6 sentences); findings by severity 致命/重要/次要, each with an id (e.g. M1), location (file and section/result number), problem, evidence (derivation, counterexample, source), and a concrete fix; what is good and should not change; what you checked and did not. Then return the structured findings.
`

const FINDINGS = {
  type: 'object',
  properties: {
    report_path: { type: 'string' },
    findings: {
      type: 'array',
      items: {
        type: 'object',
        properties: {
          id: { type: 'string' },
          severity: { type: 'string', enum: ['fatal', 'important', 'minor'] },
          location: { type: 'string' },
          problem: { type: 'string' },
          evidence: { type: 'string' },
          fix: { type: 'string' },
        },
        required: ['id', 'severity', 'location', 'problem', 'fix'],
      },
    },
  },
  required: ['report_path', 'findings'],
}

const VERDICTS = {
  type: 'object',
  properties: {
    verdicts: {
      type: 'array',
      items: {
        type: 'object',
        properties: {
          id: { type: 'string' },
          verdict: { type: 'string', enum: ['confirmed', 'partly', 'refuted'] },
          reason: { type: 'string' },
          fix: { type: 'string', description: 'the fix to apply if confirmed or partly (corrected where needed)' },
        },
        required: ['id', 'verdict', 'reason'],
      },
    },
  },
  required: ['verdicts'],
}

const REVIEWS = [
  { dim: 'math-I', scratch: 'v62verify/math1', prompt: `DIMENSION: mathematics, first half. Results of Sections 2–5 and their Supplement chapters S2–S5, with priority to what is new or repaired in V6.2: Prop 2.2 incl. part (4) (rivals who respond: r^eq for stability, r^pr for the price; the cusp beyond Γ_δ≥1), Remark S2.1 (Λ*), the channel-sign proposition in S2 ("at least in proportion" for correction, "less than in proportion" for provision), Prop 2.3 (strict cap, the local condition at K̄=K*, diffusion), Lemma 3.3 (neutrality vs compliance; s(0)>c>s(1)), Prop 3.6 (κ divisible), Prop 3.9 in its general form (λ_rel vs λ_com; fixed prize "wherever Γ_δ>0"; proportional prize iff (1−β)r>1 at every horizon; diffusion separating the thresholds), Remark 3.10 (two errors), Lemma 3.11 (total and within-group terms under every monotone fitness; between-group under affine), Prop 4.5 (sufficient half at any adaptation speed; necessary half when capacity tracks; the three floor cases plus transient; per-unit floor vs lump sum), Prop 4.6 (human capacity: +wδ_h; recovery; hysteresis), Prop 4.13 (silent crossing; premises), S4.2 (capacity dynamics, incl. the merge's claim that variance growing slower than q² keeps capacity bounded), Prop 5.4 (per-deviation p_d; (5) exclusive/independent breakouts; the q=0.045 example), Remark 5.5 (detect link: p_d = 1−υ(T_dec), (14) as υ ≥ 1−p̄_d, and its relation to Prop 8.x verification threshold), Cor 5.6 (exchangeable continuation; strict variants), Prop 5.12/Thm 5.13 (tempo, coverage), Prop 5.16 (talk: effective bias b0(n−1−θ)/(n−1+θ), informative iff <1/4), Prop 5.17 (scissors: arms, pivot ω, stakes arm condition) and the joint model in S5. For each: are all premises in the core statement; is the proof right; check numerically with your own scripts; is the tag right. Report: ${V62}/reviews/R-v6.2-math-I.md.` },
  { dim: 'math-II', scratch: 'v62verify/math2', prompt: `DIMENSION: mathematics, second half. Results of Sections 6–11 and S6–S11, with priority to what is new or repaired in V6.2: Prop 6.1, 6.2, Lemma 6.3, Prop 6.4 (p=1; q_L; the near-lock bound Remark S6.1), Lemma 6.5, Prop 6.7 (matched unsafe variant; tax paid from a lead), Remark 6.8 (masked divergences), Prop 6.9 (topology: sufficient certificate; budgets: three checks per layer 0.994 vs six across the gap 0.989; adversarial blind spot), the S6 results moved from the core (opaquecorr, lyapunov, homeostasis, boundedopt), Table 7.1 (each inequality against the result it cites), Prop 7.2 (branches), Prop 7.3 (raceselects, with the premise that winning depends on X only through E), Cor 7.4, §8 results (kernel Def, fallback Lemma 8.2, assure needs T−P+F>0, verify, preventown), Table 9.1 rows (R1 limsup; R3a halves; R4 exception (1−δ)g ≤ δ(C−D); R5 necessity from residual floor and nonsum; R8a/R8b; R9), §10 results (commonfront, commonfrontn, share with n vs n−1, twoorders, safeguards margin on both hosts, participate), §11 (signal: U11 found V6.1's signal(2) false and corrected it with a mixed equilibrium — verify; dwell monotonic in depth and unbounded as capture ages [thm]; readrule (Wald) conditions; Table 11.5). For each: premises, proofs, numerics with your own scripts, tags. Report: ${V62}/reviews/R-v6.2-math-II.md.` },
  { dim: 'fidelity', scratch: 'v62verify/fidelity', prompt: `DIMENSION: loss and fidelity to Ren. (1) Loss: V6.1 → V6.2 using ${V62}/LEDGER-v62-sentences.tsv and src/sentcheck.py (python3 src/sentcheck.py ${V61}/THEORY.md THEORY.md SUPPLEMENT.md DISCUSSION.md --min 0.4 from ${V62}); sample at least 60 dispositions (weighted to "reworded", "moved", "merged", "withdrawn") and check each against the text; check the 14 losses of R-v6.1-fidelity 重要5 are restored where LEDGER §6 says. (2) Ren's words: read ${MEM}/feedback_ren_writing_discipline.md, ${MEM}/feedback_ren_why_and_meaning.md, ${MEM}/user_ren_profile.md; sample the corpus (/Users/ren/theories/theories/*/README.md, X1's table); check every [corpus: …] quotation in the core is verbatim and correctly attributed (no AI-drafted line presented as Ren's — see x1-notes Verification); check CLAIMS' D list is complete. (3) Direction: does V6.2 say what Ren's theory says — predict → align understanding → coordinate; affirmative meaning; "we are one"; no better guardian; broad E1 as scope; judge the game, not the act; growth is not the danger, the mind is — and does any passage drift toward race-camp framing or generic AI-safety prose? (4) The Chinese guide: natural, faithful to §1.2 and §12.1, Ren's register, no translationese; quote and rewrite any bad sentence. Report: ${V62}/reviews/R-v6.2-fidelity.md.` },
  { dim: 'coldread', scratch: 'v62verify/coldread', prompt: `DIMENSION: cold read by a hostile but fair senior referee drawing on structural realism, industrial organization and arms control, who has not seen earlier versions. Read THEORY.md cold (abstract, guide skipped, §0–§12), then check objections against SUPPLEMENT/DISCUSSION. Questions: Does every headline claim (abstract, §1.2, claim boxes, §12.4) follow from the results with their conditions — any overclaim or underclaim? Is the argument coherent across sections (contradictions, repetitions, terms used two ways, numbers that differ between places)? Are the strongest counter-positions met at their strongest without being elevated? Is the judgment (§12) derived where it says derived and stated as judgment where it is judgment? Is it a great paper — what most limits it now, and what single change would most raise it? Since a short (~12–15k) paper will be written from this spine later, name what that short paper must contain and what it can leave to V6.2. Report: ${V62}/reviews/R-v6.2-coldread.md.` },
  { dim: 'evidence', scratch: 'v62verify/evidence', prompt: `DIMENSION: evidence and citations. You have WebSearch and WebFetch (load via ToolSearch "select:WebSearch,WebFetch" if deferred). Today is 4 October 2026. (1) Every work cited in V6.2 that was not in V6.1's reference lists (diff the three reference lists of V6.2 against V6.1's): verify existence, authors, year, venue, and that the sentence citing it says what the work says; prioritise the 2024–2026 alignment literature (alignment faking, sleeper agents, in-context scheming, MacDiarmid et al., monitorability, shutdown resistance, control evaluations, gradual disempowerment, hidden loyalties, internal deployment) and the IR/IO/arms-control works added to X1 (Grieco, Snidal, Powell 1999, Gilbert–Newbery, Budd–Harris–Vickers, Athey–Schmutzler, Aghion et al. 2001, Avenhaus et al., Schelling–Halperin, Kydd 2000, Shavell, Grossman–Helpman). (2) EVIDENCE register: check the rows the core leans on (EV1, EV2, EV4, EV5, EV6, EV8, EV11) against their sources, with the symmetric standard, and that the core states their strength correctly (no "shows" where "is consistent with"). (3) Precedents in §11 and X11. (4) No state or firm named in the core body. Mark each source 已核实 / 有误 (with correction) / 无法核实. Report: ${V62}/reviews/R-v6.2-evidence.md.` },
]

const confirmPrompt = (dim, res) => `${BASE}
YOUR TASK: adversarially verify the findings of the ${dim} review of V6.2 (report: ${res.report_path}). For EACH finding below, try to REFUTE it: re-derive, recompute (scripts in /private/tmp/claude-501/v62verify/confirm-${dim}/), re-read the cited text and sources. Default to "refuted" only if you show it is wrong; "partly" if the problem is real but the fix is wrong or overstated (then give the corrected fix); "confirmed" if it holds (keep or sharpen the fix). Do not edit project files. Findings:
${JSON.stringify(res.findings, null, 1).slice(0, 60000)}
Write ${V62}/reviews/C-v6.2-${dim}.md (one line per finding: verdict and reason, in 简体中文) and return the structured verdicts.`

const fixPrompt = (bundle) => `${BASE}
OVERRIDE of the rule above: you ARE the fixer and may edit ${V62}/src/ (core, supp, disc, reg) and ${V62}/checks_v62.py. Never edit assembled documents directly.
YOUR TASK: apply the confirmed findings of the V6.2 verification round. Below are the findings with their confirmation verdicts. Apply every finding with verdict "confirmed" or "partly" (using the verifier's fix where given), in order of severity, with the smallest correct change in src: keep keys, tags, Ren's words and every condition; if a fix changes a statement, update its proof in the Supplement, its check block if it has one (assertions must still pass; add one if the finding exposed an unchecked number), and every place that cites it (grep the key). Where a fix would need Ren's decision (his words, a value judgment, the length), do not apply it: list it. Do not apply refuted findings.
Then from ${V62}: python3 src/assemble_v62.py; (cd src && python3 refs_v62.py); python3 src/assemble_v62.py; python3 xref_v62.py; python3 checks_v62.py > checks_v62.log — all must pass.
Write ${V62}/reviews/FIXES-v6.2-verify.md: every finding id with its verdict and what you did (file:line, before → after) or why not; the "needs Ren" list; build and check status. Return a summary.
FINDINGS AND VERDICTS:
${bundle}`

phase('Review')
const reviewed = await pipeline(REVIEWS,
  (r) => agent(BASE + `\nScratch folder: /private/tmp/claude-501/${r.scratch}/\n` + r.prompt, { label: `review:${r.dim}`, phase: 'Review', effort: 'xhigh', schema: FINDINGS }).then(res => {
    if (!res) throw new Error('review failed ' + r.dim)
    return { dim: r.dim, res }
  }),
  (x) => {
    const serious = x.res.findings.filter(f => f.severity !== 'minor' || true)
    if (!serious.length) return { ...x, verdicts: { verdicts: [] } }
    return agent(confirmPrompt(x.dim, x.res), { label: `confirm:${x.dim}`, phase: 'Confirm', effort: 'xhigh', schema: VERDICTS }).then(v => ({ ...x, verdicts: v || { verdicts: [] } }))
  },
)
const ok = reviewed.filter(Boolean)
log(`reviews completed: ${ok.map(x => x.dim).join(', ')}`)
if (ok.length < REVIEWS.length) return { reviews: ok, incomplete: true }

const bundle = ok.map(x => {
  const vmap = Object.fromEntries((x.verdicts.verdicts || []).map(v => [v.id, v]))
  return `### ${x.dim} (${x.res.report_path})\n` + x.res.findings.map(f => {
    const v = vmap[f.id] || { verdict: 'unverified', reason: '' }
    return `- [${f.id}] (${f.severity}; verdict: ${v.verdict}) ${f.location}: ${f.problem}\n  fix: ${v.fix || f.fix}\n  verifier: ${v.reason}`
  }).join('\n')
}).join('\n\n')

phase('Fix')
const fix = await agent(fixPrompt(bundle.slice(0, 150000)), { label: 'fix', phase: 'Fix', effort: 'xhigh' })
const counts = ok.map(x => {
  const vs = x.verdicts.verdicts || []
  return `${x.dim}: ${x.res.findings.length} findings (${x.res.findings.filter(f => f.severity === 'fatal').length} fatal, ${x.res.findings.filter(f => f.severity === 'important').length} important); confirmed ${vs.filter(v => v.verdict === 'confirmed').length}, partly ${vs.filter(v => v.verdict === 'partly').length}, refuted ${vs.filter(v => v.verdict === 'refuted').length}`
})
return { counts, fix }
