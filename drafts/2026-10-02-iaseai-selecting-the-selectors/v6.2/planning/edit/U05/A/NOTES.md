# U05 elegance pass, editor A: Section 5 (core `50_s5.md`) and S5 (`05_S5.md`)

4 October 2026. Start point: the current `src/` files (identical to `planning/snapshots/draftA/src/`). The directory held an interrupted earlier attempt (a core file with the box, `enforce`(5), the Scopes of `enforce`, `detectlink`, `relpunish`, `restraint`, `enough`, `talk` and `scissors` compressed; S5 untouched; no notes). I checked it sentence by sentence, kept what was sound, reversed three slips and finished the pass:

- restored the dissipative-limit clause of `join`(3) in §5.1, which the attempt had dropped and which §7.2's Branch I leans on ("joining buys nothing materially in the fully dissipative limit");
- restored the explicit payoff mapping in `detectlink` ($R$, $T$, $P-F$), without which "read as continuation values" does not say which reading makes the two thresholds coincide;
- kept the closed form of `enforce`(5) in the core (the result; only its numerical instance moves), and fixed a misplaced "where Section 8.3 ..." after C13.

Files written (only these three):
- `planning/edit/U05/A/core/50_s5.md`
- `planning/edit/U05/A/supp/05_S5.md`
- `planning/edit/U05/A/NOTES.md`

## 1. Word counts

| | Snapshot (draftA) | Edited | Change |
|---|---|---|---|
| core §5, assembler count | 5,579 | 5,167 | −412 (−7.4%) |
| core `50_s5.md`, raw words | 5,516 | 5,106 | −410 |
| of which: claim box (Claim + Why) | 297 (216 + 81) | 219 (165 + 54) | −78 |
| result statements (heads, numbered parts, displays, pivot) | 1,952 | 1,924 | −28 |
| Scope paragraphs | 791 | 598 | −193 |
| prose, definitions, premises, hand-offs | 2,463 | 2,348 | −115 |
| by subsection (raw): head / 5.1 / 5.2 / 5.3 / 5.4 / 5.5 | 303 / 589 / 1,825 / 1,276 / 652 / 874 | 225 / 583 / 1,646 / 1,244 / 616 / 791 | |
| supp `05_S5.md`, raw words | 6,304 | 6,335 | +31 |

**On the target (about 3,700).** The section lands at 5,167, and I stopped there deliberately. §5 declares 17 keyed results (more than any other section), and every one of them is cited by Parts II–IV in the core or is on the spine (plan §1: `enforce`, `detectlink`, `scissors`; `join`, `dissipate`, `relpunish`, `restraint`, `wingives`, `preventattack`, `racehazard`, `nonsum`, `tempo`, `coverage`, `freeze`, `enough`, `talk` are each cited from §6–§12), so under plan §2 none may move to S-numbering; `frontier` is cited only from the registers and S14 but the plan (§4, §5) places it in the core as a two-sentence Remark, which it already is. Their statements with the conditions their proofs use are 1,924 words; the definitions the statements need (the §5.2 setup, the race channel, $Y_t$, $U_t$, the four conditions of contestable correction, the three premises, E2 and E3) about 575; the Scopes, each now holding only what the result does not cover and what would make it fail, 598. That is about 3,100 words before any mechanism, consequence, Ren line or hand-off. The remaining 2,000 carry: the Claim and Why (219); the mechanisms in prose before each result; Ren's lines with the mechanisms they compress (the anaesthetic, 讲理/讲赢 by reference, Ψ2, "growth is not the danger; the mind is", 癌亦增长); the consequences the plan asks for (C11, C13, E2≠E3 with the `masked` pointer, the certified-corrector requirement, Kuran, the counter-performativity pointer, the Test G and Test E hooks, trees); and the hand-offs. Reaching 3,700 would require thinning statements (V6.1's error) or moving cited results, so I judge 5,167 to be the frontier for this unit as the plan constrains it. If the integration pass wants §5 shorter, the uniform options are in §5 below.

**Claim box.** 219 words against the brief's 90–140. The box states five results and the conjecture; each sentence keeps its antecedent and its tag. The glosses of the three means and the second gloss of $n/(n-2)$ are gone; what remains I could not cut without dropping an antecedent.

## 2. Moves (core → companion), with the pointer left in the core

| # | What left the core | Where it now lives | Pointer in the core |
|---|---|---|---|
| M1 | `enforce`(5)'s numerical instance: $C_i=1$, $P_i=0$, $D_i=4$, $V^{\rm sub}_i=0$, $g_i=2$, $\delta=0.9$; fails on $(0.0354,0.0556)$; $v_i=0.895$ at $q_b=0.045$ | S5, proof of `enforce`, new sentence "*The instance of (5).*" (the proof computed the window but never stated the parameters; now it does) [num: ES] | "S5 gives an instance that fails over a window of $q_b$ [num: ES]" |
| M2 | `enforce` Scope: valuation check of part (1); the 19,965 settings of the best-response-over-plans check; the 35 settings in which the punisher quits | S5 "Numerics (ES; EC)", bullets *Best response over plans* and *Valuation check* (already there, verbatim) | Scope keeps the condition ("Part (5) gives the credible punishment value only where racing on, not quitting the race, is the punisher's best response"); Proof line names both checks |
| M3 | Folk-theorem paragraph: $C_i=3$, $D_i=6$, $v_i=1$, $\delta=0.9$; gain 1 at $p_d=0.1$ deterred, gain 0.2 at $p_d=0.6$ not | S5 bullet *Per deviation* (already there) | "in S5's instance the deviation with the larger gain is deterred and the quieter one with the higher chance of breakout is not [num: ES]" |
| M4 | `detectlink` Scope, second sentence (the verification threshold compares cooperating with defecting against a cooperator, $F$ given, trust deciding; the equilibrium-path reading with the decisive position carrying its own stakes) | S5 "Derivation of `detectlink`", paragraph *Where they differ* (already there) | Scope's one sentence plus "(S5)" |
| M5 | After `detectlink`: "$p_d$ to detection set against the time a breakout needs to become decisive … $\bar p_d$ to the value of winning set against the sanction that remains" | restates the Remark's own statement and `enforce`(2); the Remark is the home | "Both sides of (eq) are thereby tied to what can be measured." kept as the consequence |
| M6 | `relpunish` Scope: the three-player example at $\delta\ge0.706$; weak as printed; strict under any small difference between the roles' prizes once assigned to match; strict in nearly every perturbed game; both punishers prefer the same role; indifference between hurting the deviator and the fellow punisher | S5 "Proof of `relpunish`", paragraphs *The role-differentiated counterexample*, *Strictness*, *Indifference* (already there, with the counts) | Scope: "punishers in different roles, a punishment that is weak as printed, strict under small asymmetries between the roles, and needs the roles coordinated, a problem of equilibrium selection (S5) [num: ES; CR]" |
| M7 | `restraint` Scope: $C_i=1$, $D_i=0.9$, $v_i=0$, $g_i=2$, $\delta=0.9$, $\bar p_{d,i}=0.864$ | S5 "Proof of `restraint`", last sentence (already there, 0.8642) | Scope states the condition instead of the number: "with $D_i<C_i$ but $(1-\delta)g_i>\delta(C_i-D_i)$, restraint still fails above $\bar p_{d,i}$ (S5 gives an instance)" |
| M8 | `enough` Proof line: 0.717 frozen at need; $1.8\times10^{-9}$ by period 400 | S5 "Proof of `enough`" (already there) | "S5, with the frozen and the compounding case in numbers [num: PE]" |
| M9 | `talk` Scope: the quadratic third-party variant as a number sentence | S5 "Proof of `talk`" (2), the $-ky^2$ sentence (already there) | Scope keeps the condition it establishes: "Linear third-party payoffs are not load-bearing: quadratic ones leave the effective bias unchanged (S5) [num: TK]" |
| M10 | `scissors` Scope numbers: 0.924 → 0.387; thresholds 0.551 and 0.542; crossing at period 31.8; 12 of 96 settings | S5 *The reduced form (JX)* and Remark `jointscissors` (already there) | Scope keeps the shape of both results and the one number the argument uses (none enforceable above $p_d=0.9495$ for $\theta_0=0$); the box's "[num]" is carried by the `jointscissors` sentence |
| M11 | `scissors` Scope: "in the contests computed exceeds the structural gain where a lead discourages the follower and can fall below it where a laggard tries harder" | kept, shortened, now citing `eqgain` (S2), the home of the numbers | "which exceeds the structural gain where a lead discourages the follower and can fall below it where a laggard tries harder ({{eqgain}})" |
| M12 | Test G paragraph: the mechanism of the hump and "this theory and structural realism agree" | §7.4 Test G row (same wording) and S5 *Test G* (registered wording) | one sentence: "at intermediate $p_d$, since … (Section 7.4; S5) [num: JX]" |

Nothing moved to a Discussion chapter (the unit has none). No key changed kind or numbering; declarations are the same 18 in the same order; `{{eqgain}}` is the one new citation (an S2 Remark, resolves).

## 3. Duplicates removed (true duplicates of text elsewhere in the paper)

| Sentence removed | Where the point lives |
|---|---|
| "as nuclear advantage saturated at a secure second strike [obs]" (§5.1) | §7.2, after `branches`: "Branch I′ is how nuclear rivalry stabilized once a survivable second strike was secure … [obs]"; §5.1 now points "(Section 7.2)" |
| "though the longest-horizon series is at the limit of its task suite" (§5.3, EV5 caveat) | §7.3 (line "Capability growth is measured, with the longest-horizon series at the limit of its instrument …") and EVIDENCE EV5; §5.3 now points "(Section 7.3)" |
| Claim box glosses "which makes restraint pay through the future; … which makes costs return in time; … which lets the parties see the same danger and believe one another" | the Why's first sentence, and the openings of §5.2, §5.3 and §5.4 |
| Claim box "The first two arms turn on one pivot, the won share" and "a factor that falls toward one as actors multiply" and "which the diagnosis tests" | the `scissors` pivot paragraph; the `talk` headline; the `scissors` Scope ("Test E examines, Section 7.4") |
| Why "captured correctors weaken the sanction, and the objectives that compounding narrows drain talk" | `scissors` arms 2–3 and the sentence after `talk` ("the loop that narrows working objectives drains talk with them") |
| Why "so nothing in it stops growth where need is met" | merged into the `enough` paragraph: "what decides whether growth stops where need is met" |
| `talk`(2) "three times the material bias among three, falling toward it as $n$ grows" | the `talk` headline ("a factor that falls toward one as actors multiply") |
| "as optimizing a learned reward past a point lowers the quality it measured (Gao et al. 2023)" | §6.4 ("Reward hacking is Goodhart's law inside training (Gao et al. 2023)"); §5.4 keeps the citation in four words |
| "The amplification at $\theta=-1$ is greatest among three" | `talk`(2) |
| After `relpunish`: "roles that need coordinating, which is a problem of equilibrium selection, or a continuation that carries a label" | the Corollary's own Scope, which now lists the two escapes once |
| §5.5 closing: "the pivot does not turn" | the pivot paragraph ("provision that grows with the stakes holds both still"); the closing keeps V6.1's "growth moves temptation up and restraint down at once", conditional, which the merge notes placed here |
| §5.1 "and in the fully dissipative limit joining buys nothing over staying out" | not removed: the attempt had dropped it; restored as a clause, since §7.2 cites `join` for it |

## 4. Preservation check (sentcheck, snapshot core against new core + new S5 + all other current src files, --min 0.5)

181 sentences checked, 10 below 0.5, each adjudicated:

1. Claim box first sentence (0.49): kept in shorter words; the glosses are duplicates (§3).
2. "The first two arms turn on one pivot … blades close together [num]" (0.44): merged into the arms sentence of the Claim ("and in one reduced model the two arms on that pivot close together [num]").
3. "Each erosion then feeds the others: captured correctors weaken the sanction …" (0.24): kept as "each erosion feeds the others [thm]"; the concretization is a duplicate (§3).
4. "A valuation check confirms the algebra of part (1) [identity: EC]" (0.25): moved, M2; the Proof line names it.
5. "With $n\ge3$, punishers in different roles can hold a relative deviator below zero" (0.30): merged into the `relpunish` Scope's second escape, M6.
6. "In a three-player example such a punishment sustains cooperation for $\delta\ge0.706$ …" (0.16): moved, M6 (S5 holds it verbatim).
7. "Both punishers prefer the same role … equilibrium selection" (0.34): moved, M6; "a problem of equilibrium selection" kept in the Scope.
8. "PE: frozen at need, survival … 0.717; compounding at 10% … $1.8\times10^{-9}$" (0.39): moved, M8.
9. "With third-party payoffs quadratic … unchanged [num: TK]" (0.35): kept as a condition in other words, M9.
10. "Measures become targets … (Gao et al. 2023)" (0.39): kept in shorter words; the Gao clause is a duplicate (§3).

Snapshot S5 against new S5 (+ core + others): 190 sentences checked, 0 below 0.5. S5 was not rewritten; one sentence was added (M1).

## 5. Verification

- Test assembly in `/private/tmp/claude-501/u05A-scratch` (a copy of v6.2 with the two edited files in `src/`): `python3 src/assemble_v62.py` → "no problems"; §5 = 5,167; 95 core and 33 supplement declarations unchanged.
- `xref_v62.py` in the scratch copy reports two guide-against-§1.2 items below 60% (items 1 and 9). They fail identically on an untouched copy of the current `src/`, so they are front-matter work (plan §10, phase 2), not this unit's.
- Keys: same 18 declarations, same order; every `{{key}}` the snapshot cited is still cited; `{{eqgain}}` added. Corpus tags 4 → 4; [conj] 6 → 6; "prem" 18 → 18; [num] tags 17 → 15 because two pairs merged into one bracket each ("[identity: EC; num: ES]", "[num: ES; CR]"); no claim lost its tag.
- Mathematics unchanged. M1's closed form was re-derived: $v_i(q_b)=3.6q_b/(0.1+1.8q_b)$; enforceable at $p_d=0$ iff $v_i\le0.7778$ iff $q_b\le0.0354$; $v_i<1$ iff $q_b<0.0556$; $v_i(0.045)=0.895$.
- Ren rulings and merge-note "For Ren" items all present: the anaesthetic sentence with its corpus tag (§5.1); Ψ2 keyed to `psi`; "changing the premise itself" (`restraint`); "AI-assisted correction can keep pace"; "They are different arrangements" and the `masked` pointer; "growth is not the danger; the mind is" [corpus: meta-attractor; Ren, 2026-09-25]; 癌亦增长 [corpus: shengsheng, 2026-07-14]; 讲理/讲赢 by reference to `psi` (one home, §3.8); Kuran 1995; the §11.2 counter-performativity pointer; C0 named in the box; 0.9495; the hand-off sentence.
- Standing rules: no named states or firms (xref confirms); E2 and E3 as before; "stopping is not slowing" kept.

## 6. Open issues for the integration editor

1. **Length.** If §5 must come down further without loss, the only uniform routes are (a) S-numbering `frontier` (not cited from Parts II–IV; the plan placed it in the core, so this is a plan decision) and (b) the merge notes' suggestion that the definitions of $Y_t$ and $U_t$ and the four conditions of contestable correction move to S5 with one clause left; §6.4, S0 and S7 use "overrulable" as a defined term, so the definition must then be pointed to from §6.4.
2. **Claim-box length** (219) exceeds the brief; §6's box is longer still. A uniform box pass across sections would be the place to decide.
3. **Snidal 1991** is now in `refs_v62.py` (merge-notes item 2 is closed). Abreu 1988 and Kuran 1995 resolve.
4. **Test G** is now stated once in full in §7.4 and in S5's registered wording; §5.5 carries one sentence pointing to both. TESTS should follow S5's registered wording (merge notes, item 3).
5. Merge-notes items 3–8 (other files; corpus keys for X1; fidelity marks D; legacy numbers; two joint models) are untouched by this pass and still open.
