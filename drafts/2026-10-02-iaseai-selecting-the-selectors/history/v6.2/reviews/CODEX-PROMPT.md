# Prompt for the outside-family review of V6.2 (Codex)

Run from `/Users/ren/theories/drafts/2026-10-02-iaseai-selecting-the-selectors/`:

```
sed '1,/^---$/d' v6.2/reviews/CODEX-PROMPT.md | codex exec -s workspace-write -
```

The prompt is everything below the rule. It was written on 4 October 2026. Record the SHA-256 of the THEORY.md you review.

---

You are reviewing V6.2 of Ren's theory paper "Changing the AI Trajectory: The Meta-Attractor of Winning and the Generative Alternative", in `v6.2/`. You reviewed V6.1 on 4 October 2026:
- the review is `v6.1/reviews/REVIEW-v6.1-codex.md`;
- the calculations are in `v6.1/reviews/counterexamples_v61_codex.py`.

V6.2 answers that review and eight others, which are summarised in `v6.1/reviews/SYNTHESIS-v6.1.md`. It was drafted, merged and verified entirely by one model family, and its verification round is in `v6.2/reviews/`. You are the review from outside that family, so independence is the point: derive, do not trust.

Ren has decided that V6.2 is the complete theory of record, at its length. A short paper will be written from it later. Length is not in scope, except where length hides an error.

**Files**
- `v6.2/THEORY.md`: the core, with an English abstract and a Chinese guide at the top.
- `v6.2/SUPPLEMENT.md`: proofs, by chapter.
- `v6.2/DISCUSSION.md`.
- The registers: `CLAIMS.md` (the inventory by stable key, with a V6.1→V6.2 column), `LEDGER.md` (the crosswalk), `TESTS.md`, `EVIDENCE.md` and `CHANGELOG.md`.
- `v6.2/checks_v62.py`, with 40 blocks and 188 assertions. Its map is SUPPLEMENT S15.
- `v6.2/V6.2-PLAN.md`: what the repairs were meant to do.

**Scope, in priority order**

1. **Your V6.1 findings.** For each of your six central findings and the "other definite corrections", say whether V6.2 fixed it, fixed it differently, or introduced a new error in fixing it. They were:
   - the domain of the price of standing;
   - the sign of correction;
   - the cap at equality and diffusion;
   - the falling linear cost;
   - equal incidence in R8;
   - stochastic punishment;
   - and among the other corrections: $p=1$ in delegation, affine fitness in Lemma 3.10, row sums called necessary, line 363, $s(0)>c>s(1)$, and Test M.
2. **The new or rewritten results that carry the argument:**
   - **Proposition 3.9 in general form**, relative against common return of reinvestment. Is the claim right that with a prize proportional to total capacity the narrowing condition is $(1-\beta)r>1$ at every horizon, so that compounding narrows the working objective exactly where leads compound? Is "wherever the discounted loop gain is positive" right for the fixed prize?
   - **Proposition 2.2(4)**, rivals who respond: the form survives with $r^{\rm eq}$ for stability and $r^{\rm pr}$ for the price, in symmetric Markov equilibria differentiable at equal standing. Check also the Markov computations, the "winner-take-all equilibrium coexisting with the smooth one", and what happens in catch-up contests. The drafting family flagged all three for you.
   - **The channel-sign proposition in S2.** Correction lowers the gain where decisiveness rises at least in proportion to the stock; provision lowers it where decisiveness rises less than in proportion; sharing and diffusion lower it in every channel.
   - **Proposition 4.5's two halves and the floor cases.** Proposition 4.6, human capacity, threshold raised by $w\delta_h$. S4.2's claim that gradual selection with variance growing more slowly than $q^2$ keeps capacity bounded.
   - **Remark 5.5 (detect link) and Proposition 5.17 (the scissors).** The arms, the pivot $\omega$, the stakes-arm condition, and the joint reduced model in S5.
   - **Proposition 5.16**, talk under one effective bias $b_0(n-1-\theta)/(n-1+\theta)$.
   - **The §11 corrections.** V6.1's `signal`(2) was false and is replaced by a mixed equilibrium. Dwell is now a theorem: monotone in the depth of lock-in and unbounded as capture ages.
   - **Table 7.1.** Is every inequality the one its cited result proves, and does every "lever" reverse what it claims?
3. **The checks.** Which of the 188 assertions are independent, and which hold by construction? Are any numbers in the text not backed by a block (S15 maps them)? Are the "outside review" cases (S14, marked (O)) right?
4. **The judgment (§12).**
   - Tier 1(a) claims to hold "on every reading of the cruxes". Check that against the robustness matrix in TESTS.
   - Tier 1(b) places the burden of proof on withdrawal. Is that consistent with the protection standard of §8.1?
   - Tier 2's activation is committed in advance and executed by mechanism.
   - Tier 3 argues reversibility over every failure mode. Does it treat the designed path's own failure modes as it treats continuation's?

**Also check**
- Every core statement carries every premise its proof uses.
- The claim tags ([def] [val] [thm] [thm∣prem] [prem] [obs] [num] [conj] [rec]) are right.

**Constraints**
- Do not edit any manuscript, register or existing script. Do not commit.
- Write calculations to `v6.2/reviews/counterexamples_v62_codex.py`, standard library only.
- Write the review to `v6.2/reviews/REVIEW-v6.2-codex.md`, in English, in the shape of your V6.1 review:
  - assessment first;
  - what the previous review can now close;
  - findings by priority, each with location (file:line in the snapshot), problem, derivation or counterexample, and repair;
  - what is sound;
  - what you did and did not check.
- The author's standing rules bind any text you suggest:
  - name no particular states or firms; use roles;
  - do not elevate race-camp arguments beyond what they earn;
  - keep stopping (E2) distinct from slowing (E3);
  - judge the game, not the act.
