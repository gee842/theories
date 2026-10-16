# Prompt for the outside-family review of V6.1 (Codex)

Run from `/Users/ren/theories/drafts/2026-10-02-iaseai-selecting-the-selectors/`: `sed '1,/^---$/d' v6.1/reviews/CODEX-PROMPT.md | codex exec -s workspace-write -`. The prompt is everything below the rule. It was written on 4 October 2026 for the V6.1 snapshot with THEORY.md SHA-256 beginning `242a61240d810e51`.

---

You are reviewing V6.1 of Ren's theory paper "Changing the AI Trajectory: The Meta-Attractor of Winning and the Generative Alternative". It is in `v6.1/`. You reviewed v6.0 on 3 October 2026; your review is `v6/reviews/REVIEW-v6-codex.md`, with calculations in `v6/reviews/counterexamples_codex.py`. V6.1 restructures the paper and repairs the mathematics in response to that review and six others (`v6/reviews/SYNTHESIS-v6.0.md`). The drafting model and its other reviewers belong to one model family. You are the review from outside that family, so independence is the point: derive, do not trust.

**Files.**
- `v6.1/THEORY.md` is the core. Results are stated there, not proved.
- `v6.1/SUPPLEMENT.md` has the proofs, chapter by chapter: S2 for Section 2, and so on.
- `v6.1/DISCUSSION.md` holds lineage, alternatives, the full design and the transition.
- `v6.1/CLAIMS.md` lists every result by stable key.
- `v6.1/LEDGER.md` maps v6.0 results to V6.1.
- `v6.1/checks_v61.py` holds the drafters' numerical checks.
- `V6.1-PLAN.md` and `v6/v61-planning/Q2-math-repairs.md` show what the repairs were meant to do.

**Scope: a targeted audit of the new and repaired mathematics, and of the argument that rests on it.** In order of priority:

1. **Prop 5.4, the enforcement condition, and its corollaries 5.5 and 5.6.**
   - Prop 5.4 replaces v6.0's Prop 5.7 along the lines of your repair: (1−δ)g+δp_d(D−C) ≤ δ(1−p_d)(C−v).
   - It adds a punishment value with breakouts, v=[(1−δ)P+δq(D+U)]/(1−δ+2δq).
   - Cor 5.5 claims that reversion to a race can fail to punish. Cor 5.6 states what restraint needs.
   - Check the continuation assumptions and the observability assumptions.
   - Check whether 5.5 rests on a weak or knife-edge equilibrium.
   - Check whether Cor 7.3 ("what the premise of the race cannot justify") claims more than 5.4–5.6 give.
2. **Prop 2.2 (loop gain) and Prop 3.9 (price of standing).**
   - The loop gain is Γ=(1−β)Σ_j r_j ω_j d_j/(d_j+δ_f,j), with ω_j=κ_jΩ/(κ_jΩ+n k_0j).
   - The price of standing is λ=Γ_δ/(1−Γ_δ), with threshold θ_Γ=(nθ0−(n−1)(1+θ0)Γ_δ)/(n−(1+θ0)Γ_δ).
   - The text claims the interconnected conditions "combine near equal standing into one loop gain", and that the loop gain "prices standing and so manufactures the relative objective".
   - Is that a theorem of the stated model, or does it depend on linearization, symmetry or the quasi-static reduction?
   - Does it survive away from equal standing?
3. **Lemma 3.3 (blindness, with incidence and evasion) and Lemma 3.10 (one group: every partition, transmission term).**
4. **Section 4's cost structure, Assumption 4.2: C(q;p)=f p^{ξ_f} q + γ p^{ξ_v} q^{1+η}/(1+η).** Check the results that follow from it:
   - the rate law α_cor ≥ α_ctl/(1+η);
   - the size threshold exponent 1/(2−ξ_f);
   - the splitting factor k^{(2−ξ_v)/η};
   - concentration via Σp^{1+(2−ξ_v)/η}, a third moment of shares rather than a Herfindahl index;
   - Thm 4.12 (the slow route);
   - Prop 4.11 (the pause field). It also appears in the author's paper of 28 September 2026; say whether the two statements agree.
5. **Prop 5.15(2), Prop 9.1, Prop 10.3, and the margin in Thm 10.5.**
   - Prop 5.15(2) says talk among three or more forms blocs.
   - Prop 9.1 gives requirements by kind of support.
   - Prop 10.3 is about sharing.
   - Is the margin in Thm 10.5 necessary, sufficient, or neither, as stated?
6. **The quasi-static assumption.** It couples human capacity ℳ (decay δ_h, recovery ϱ_h) with the field in §4, §6 and §11.
   - What in the core depends on it?
   - Is that dependence stated wherever it is used?
   - If you can, run a joint simulation without timescale separation and report where the conclusions change. This is TESTS Study 2, not yet done.
7. **Your v6.0 findings.** For each, say whether V6.1 fixed it, or whether the fix introduced a new error.

**Also check.**
- Does each core statement carry every premise its proof uses?
- Is each claim tag right? The tags are [def] [val] [thm] [thm∣prem] [prem] [obs] [num] [conj] [rec].
- Does `checks_v61.py` test what CLAIMS says it tests, and is any check circular?

**Constraints.**
- Do not edit any manuscript, register or existing script. Do not commit.
- Write your calculations to `v6.1/reviews/counterexamples_codex_v61.py`, using the standard library only.
- Write your review to `v6.1/reviews/REVIEW-v6.1-codex.md`, in English, in the shape of your v6.0 review:
  - an assessment first;
  - then findings by priority, each with its location (file:line in the snapshot), the problem, a derivation or counterexample, and a repair;
  - then what is sound and should be kept;
  - then what you did and did not check.
- Record the SHA-256 of the THEORY.md you reviewed.
- The author's standing rules bind any text you suggest:
  - name no particular states or firms; use roles;
  - do not elevate race-camp arguments beyond what they earn;
  - keep stopping (E2) distinct from slowing (E3);
  - judge the game, not the act.
