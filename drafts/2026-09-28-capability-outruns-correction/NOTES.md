# When Capability Outruns Correction — v2 (2026-09-29)

*These notes were written by Claude Opus 5.5, which drafted v2. Ren has not yet reviewed v2.*

## Files

- `When_Capability_Outruns_Correction_v2.tex` is the single-file source, with the figures inline as pgfplots code. It builds with any TeX Live that includes pgfplots (1.18 or later). It was tested with Tectonic 0.17.0.
- `When_Capability_Outruns_Correction_v2.pdf` is the compiled paper: 26 pages, about 13,500 words including the appendix and references.
- `build/` is the working source:
  - `main.tex` is the same text, with `\input` for the figures;
  - `figures.py`, in pure Python, regenerates `fig-*.tex` and prints every number quoted in the paper;
  - `checks.log` is that printout.

  To rebuild after changing the figures, run `python3 figures.py` in `build/` and then re-flatten; the flattening is a one-line `re.sub` over `\input{fig-*.tex}`.

## Provenance

- **v1:** `sources/05-alignment-and-moloch/2026-09-28-When_Capability_Outruns_Correction.tex`. An unnamed AI tool drafted it at Ren's request.
- **The two reviews of v1:** `theories/alignment-selection-on-cognition/review-2026-09-28-capability-outruns-correction/REVIEW.md`, by Claude Opus 5.5 and Claude Fable 5.1.
- **Ren's direction for v2:** `sources/16-claude-code-directions/2026-09-28-capability-outruns-correction-v2-request.md`. It holds the three decisions below and "Pursue academic excellence, please write the next version".
- **Authorship:** v2 is AI-drafted from Ren's ideas, v1 and the corpus. None of its sentences are Ren's verbatim.

## Ren's three decisions, and where they are carried

1. **The frontier-only scope is deliberate: the paper is for academia and intellectuals.** The "Scope and status" paragraph in §1 says so. It adds that the restriction of scope "implies no judgement about other uses". The mechanisms bear on the wider question of AI in competitive, concentrating activities, but the paper does not argue it. It concedes nothing on the 2026-09-26 game-level ruling.
2. **Reconcile unilateral restraint where it strengthens the paper.** §7 does this through basin geometry.
   - **Prop. 9 (the restraint window).** Restraint by a coalition with share *s* unwinds capture without any agreement if *x₀ − s < σ(r₀)*. The required coalition grows with inherited rule support, so the window for founding acts closes.
   - **Prop. 10 (a pause resets rule support).** A pause moves rule support to the level the frozen shares justify under whatever rule-making runs during it. With ordinary rule-making, it completes capture by a practice above the saddle share. With rule-making insulated from shares, it unwinds capture up to σ(0).
   - **Corollary 2.** From near-full capture in the running example, the required coalition is 0.86 for restraint alone, 0.55 with an ordinary pause, and 0.27 with an insulated pause (Fig. 4).
   - **History.** The Berg letter preceded Asilomar. The 1958–61 test moratorium collapsed when negotiations over inspection stalled. The 1963 treaty covered only what could be detected without inspection.

   The 08-22 "founding act" and the 09-28 "strategically weak" now appear as two regimes of one result: weak for small actors, strong for actors whose share is comparable to *s\**, and strongest combined with an insulated pause and verification.
3. **Restore the incompressible floor, with stronger reasons.** §5 does this in four steps.
   - **Four sources of incompressibility:** manifestation, reflexivity, irreducibility and novelty, with citations.
   - **Assumption 1:** a manifestation window *m_k* and an extrapolation reach *λ_k*.
   - **Prop. 5, the speed limit:** γ ≤ ln(λ_k q_max)/m_k, independent of any investment in assurance, and attained by paced advancement. This is a precise form of "development within understanding".
   - **Prop. 6, the correction window:** m_k + τ_d + τ_r < T_k. It sorts hazard classes into compressible, incompressible-but-correctable and uncorrectable.

   The v1 sentence "if tests and interventions scale sufficiently fast… acceleration need not create this lag" survives. It is now true exactly for compressible classes.

## What changed from v1, by review finding

| Review finding (both reviews unless marked) | v2 |
|---|---|
| The "explicit chain" is claimed but not built | One coupled model. Prop. 7: capture lowers the effective alarm. Prop. 8: capture consumes the correction budget from both ends. Fig. 3 shows masking acting as delay. |
| The pause follows from the rate model, not from the capture model | Prop. 4: reversal latency depends on the lever. Prop. 10: a pause resets rule support. Prop. 11: accumulation. The regime is derived in §10 and Table 2, with the regime's own R_cap < 1. |
| The transition-path claim is asserted | Prop. 4 (i)–(iii), including the slow-institutions result, and Fig. 2: same destination, different paths. |
| Triggers wait for hazard (Fable) | §8: the trigger is the absence of a passing independent safety case, derived from Assumption 1 and Prop. 7. |
| Is it licensing? (Fable) | §10: yes in part. Analogues from pharmaceuticals, nuclear safeguards, biosafety and aviation. The 737 MAX recertification kept compliance findings at the FAA (DOT OIG 2023), which is b lowered. |
| Accumulation and overhang | Prop. 11: a pause helps only through governed inputs and reallocation to assurance. |
| Prior work | §2 is rewritten. References grow from 10 to 85. |
| Mathematical presentation | Propositions with proofs in App. A. New results: the gradient structure, invariant quadrants, the separatrix as a nonincreasing σ(r), R_cap > 2 as the risk-dominance threshold, the M-matrix lemma without irreducibility, the integrability step for h = ρ, a parameter-level viability condition, and a Le Cam bound for the probabilistic version of the lemma. |
| Notation clashes and `\qquad` | Resolved: C is now E′, g is now γ or θ, B is now G, L is now Λ, and S_i is now 𝒮_i. The Φ display is gone. Unused packages were removed. Epistemic lag gets a definition (Def. 2). |
| Defensive register | Disclaimers are folded into one "Scope and status" paragraph and §12. The formal results no longer carry trailing "not X" sentences. |
| Paired domains (智善 plan v6) | §9 and Table 1: biological misuse, agents with infrastructure access, the information ecosystem. |
| Corpus: conceptual capture | §6.2: capture of the evidence channel, the formal counterpart of "what you can't count stops counting". |
| Corpus: the stag hunt | Remark 2 and §7.1: rule memory creates the coordination structure. |
| Corpus: the agent-fleet case | §3.2, "A small observed case", labelled as anecdotal. |

## Verification done

- **Numbers.** Every number in the text comes from `build/figures.py`; see `checks.log`. The claims in the propositions were checked numerically in this session, including the pause reset in both directions and the combined restraint-and-pause coalitions.
- **References checked against the web on 2026-09-28/29.**
  - The ten v1 references, by the Fable reviewer.
  - Thirteen arXiv IDs: Alaga and Schuett; Buhl et al.; Critch and Russell; Kasirzadeh; Sastry et al.; Hooker; Anderljung et al.; Shavit; Shevlane et al.; Taleb et al.; Clymer et al.; Kulveit et al.; Kwa et al.
  - The IDAIS statements, the FAA 737 MAX summary, and DOT OIG report AV2023025.

  The remaining classic books and journal articles are cited from knowledge and should be spot-checked before submission. They include Collingridge, Stigler, Pierson, Weitz et al., Arrow and Fisher, Henry, Kandori et al., Young, Kydd, Seaborg and Divine.
- **Build.** The flattened file compiles standalone, with no undefined references and no overfull lines.

## Open for Ren

- **The anecdote in §3.2.** It is your own engineering, the Bonfire agent fleet, described generically. Keep it or cut it.
- **The author note** names Claude Opus 5.5 and the two AI reviews. Adjust it to the venue's disclosure norms.
- **No parameter is calibrated.** If a venue wants empirics, the next step is the sandbox design and the data streams in §11.
- **Length.** For a conference version, move Appendix A and §9 to supplementary material.
- **Venue.** arXiv (cs.CY) first. Then a journal such as *Philosophy & Technology*, *AI & Society* or *Risk Analysis*, or AIES as a conference.
