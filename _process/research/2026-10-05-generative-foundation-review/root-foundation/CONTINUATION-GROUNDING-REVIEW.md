# Independent review: continuation grounding W1–W5 (plan W8)

- **Reviewed:** commit `1f6f375f` ("Derive what a continuing formation must count, and state the center as one axiom (W1–W5)") against parent `7f69f455`: `Becoming/Continuation.lean`, `Becoming/Standpoints.lean`, root `Becoming.lean`, package README, `check_becoming.py` scope; records `continuing-self-fed-from-beyond`, `own-count-misses-joint-excess`, `held-lives-g0-is-centering`, `conveyance-crosses-the-boundary`, `derived-extent-limits` (spot-check: `living-on-and-descent`); chapter §6.7, premise card, full statement items 6 and 10, §8–§10 rows; study §47 and its English summary; unification-plan row; plan implementation status.
- **Date:** 2026-10-10. **Reviewer:** independent Claude Opus 5.5 agent (did not write the work).
- **Method:** read all of the above; recompiled probes against the committed bytes (source hashes match the receipt `20261009T222752.438253Z`). Probe files, not part of the package: `Review/Probe.lean`, `Review/ProbeAudit.lean`, `Review/Probe2.lean` in the scratch build `work_head/`; every probe declaration reports "does not depend on any axioms".

## Verdict

The Lean is correct and axiom-free, and the general theorems say what their docstrings say. G0 stays the adopted axiom everywhere, and Ren's open choices are listed. The problems lie in the interpretive layer behind the headline "the proofs now draw the line where it said":

1. The witness that "the center is not derived" has no derived requirement at the level of valuations. Its transmission conjunct follows from S0, so the plan's §9 test could not fail as posed.
2. N_std is one of two completions of S0. With a dependence relation, the derived extent itself yields claim-level G0 in fully interdependent wholes, so "not derived" needs a scope.
3. Several AI readings are attributed to Ren's proposal.
4. `Lone` does not witness "no particular source is needed".
5. The joint-count requirement is stated unconditionally, though `Mortal` shows it binds only wants that outlast the stock.

Nothing is blocking. Every point can be fixed by rewording, plus one or two added theorems.

## Findings

### C1. `center_not_derived` contains no derived requirement; the §9 test was vacuous as posed (substantive)

**Location:** `Standpoints.lean:342–355` (`Totalizer.center_not_derived`); `held-lives-g0-is-centering`, `derived-extent-limits` (correspondence: "Had the fourth witness been impossible … the witness exists"); study §47 interpretation and counterreview 3; plan §3.4 item 4 and §9.

**What is wrong:**

- The conjunct `Within (fun i => own i.1 i.2.2) valuation.transmits` ("transmission into each own region") follows from S0 at every position in **every** valuation. It is not special to `own = sig`.
- So the valuation content of the theorem is exactly `Apart`'s: Held, S0, ¬N_std. The careful-keeper dynamics (`careful`) is a separate conjunct-free fact about the same web.
- Flow and Web predicates never constrain `sig`. No dynamics-level requirement could force N_std, and the witness could not have failed to exist.
- The plan's own §3.4 asked for something stronger: "transmission along what each continuation requires".

**Evidence:**

- `Review.own_transmission_of_selfGood : (∀ p, V.SelfGood p) → Within (fun i => V.own i.1 i.2.2) V.transmits`, with the one-line proof `fun ⟨p,_,d⟩ own _ _ alive => self p d own alive`.
- `Review.Tot.stronger` builds the intended witness. `Feeds e e'` holds when `e'` gives, at the common step, to a condition `e`'s formation requires. The keeper values its own events and the sun's. On that valuation: Held, S0 everywhere, transmission along `Feeds` out of every own region, `other` living at step 0 yet not significant from the keeper, ¬N_std, ¬G0.
- `Review.Tot.out_of_own_fails`: transmission out of own regions along `Web.valuation`'s formed relations (co-participation) **fails** in the committed witness. The keeper's living event at step 0 and the other's share the habitat (`related_keeper_other`).

The conclusion therefore holds only because the derived extent is read as running along dependence, not along every formed relation.

**Correction:**

- Replace the redundant conjunct with dependence-directed transmission (as in `Review.Tot.stronger`), or drop it and say the valuation half is `Apart`'s.
- State in the records and study that the line holds for a dependence-directed derived extent and fails for a relation-directed one (`out_of_own_fails`).
- Withdraw "the witness exists" as a passed test. Rephrase the §9 criterion so that it constrains `sig`.
- Replace "every derived requirement" with "every requirement derived in this group" in the README, root, chapter, study and commit-style summaries; the record hypothesis already says this.

### C2. N_std is not the unique completion, and "not derived" needs a scope (substantive)

**Location:**

- held-lives record ("on held lives the axiom is exactly N_std; connection and N_rel keep a role only for lives no standpoint holds");
- `Becoming.lean:260` ("standpoint neutrality is the one premise that does");
- `Apart.standpoint_neutrality_is_needed`;
- chapter §6.7 and item 10;
- plan §0 and §4.2.

**What is wrong:**

- On a connected whole where every position holds a living claim, S0 with N_rel gives G0 with no N_std premise.
- `Apart` is connected (`related := True`) and fails N_rel as well as N_std. It therefore shows that Held and S0 do not suffice; it does not single out N_std.
- If `related` is read as dependence (`Feeds`, C1), then N_rel along it is precisely the valuation form of "count what your continuation depends on". In a fully interdependent whole, the derived extent with S0 then yields claim-level G0. This is the §9 "center follows from the dynamics" case, reached in some worlds.
- Claim-level `sig` cannot distinguish counting another as a condition from counting it as a being that wants. The analysis relies on exactly that distinction ("reaches others as conditions"), but the formal content does not contain it.

**Evidence:**

- `Review.significant_of_selfGood_transmits : V.Connected → (∀ p, ∃ c, V.own p c ∧ V.living c) → (∀ p, V.SelfGood p) → Neutral V.transmits → V.Significant` (no `shares` hypothesis).
- `Review.apart_fails_transmission : ¬ Neutral Apart.valuation.transmits`.
- Applying the general theorem with `related` read as dependence is a hand argument.

**Correction:**

- State both completions: on held lives, S0 with N_std; on connected wholes where every position holds a living claim, S0 with N_rel.
- Say that N_std is chosen because it needs no connection, not because it is the only completion.
- Scope "the center is not derived": it holds wherever some living claim lies outside some wanting position's dependence closure (`Totalizer`), not universally.
- Disclose that `sig` does not separate instrumental from final significance.
- Rename or redocument `Apart.standpoint_neutrality_is_needed` as "held lives and S0 do not suffice".

### C3. `Lone` does not witness "no particular source is needed" (substantive)

**Location:** `Continuation.lean:25–27, 257, 281–282`; `continuing-self-fed-from-beyond` (title, claim, counterexample "No particular source is needed"); `derived-extent-limits` (second limit); chapter §6.7 line 488 and the L3 module row ("而不必有特定来源"); study §47 table and interpretation ("特定的来源不是").

**What is wrong:**

- `Lone` shows that no fuel is conveyed from twice: no source condition recurs.
- Every conveyance in `Lone` is by the sun, one particular formation at every step. Within the model, each fuel is used at its own step.
- `Lone.web.requires` is `False` throughout, so the model says nothing about what a wanting formation's continuation requires.
- The plan's intended witness for "reaches others as supply, not as particular beings" (a family fed alternately by two removable sources) was replaced. The claim was not adjusted.
- Bilingual mismatch inside the study: the zh table says "必要的是得到供给，不是哪个特定来源", while the English summary, the root and the README say "no particular source need recur".

**Evidence:** `Review.lone_only_sun : 0 < Lone.flow.give t f d → f = .sun`.

**Correction:** Use "being fed is needed; no particular source condition need recur" (zh: "不必有哪个特定来源复现") everywhere. Either build the two-removable-sources witness, or remove "as supply, not as particular beings" from the second limit.

### C4. AI readings attributed to Ren's proposal (substantive)

**Location:**

- `Standpoints.lean:23–25` ("Read as Ren's proposal reads it, S0 is what wanting one's continuation is") and `:55–56` ("S0 read as what wanting is, and standpoint neutrality as the one axiom, are Ren's proposal");
- `Becoming.lean:261` and README L4 row ("Ren's proposal reads S0 as wanting … and standpoint neutrality as its one axiom");
- chapter premise card S0 row (l.142, "Ren 2026-10-10 的重述提议把它读作想要自身延续") and N_std row (l.144, "以它为唯一公理");
- glossary 持有 and 中心 rows (l.767–768);
- item 10 ("which the proposal reads as its one axiom");
- plan §0 ("Ren's one axiom is standpoint neutrality").

**What is wrong:** Ren's axiom is "for anything, its continuation into the future has significance". The factorization into S0 (moved into "what wanting is") plus N_std was written by the AI after "exactly". The plan's §2 table and the held-lives hypothesis correctly call it "the AI's proposed reading, for Ren to judge". The listed locations contradict them.

**Correction:** Replace each with "the AI's reading of Ren's proposal (pending Ren)".

### C5. "A center at every point" is glossed as N_std, but S0 is what places the centers (substantive)

**Location:** `Standpoints.lean:5, 23–25`; `Becoming.lean:250`; README and chapter L4 rows ("每一点都是中心"); glossary 中心; N_std row; draft restatement ("…from every standpoint, and every point is a center").

**What is wrong:**

- In the formal decomposition, S0 is "the seed at every wanting point". `Apart` has a center at every point and fails the axiom.
- N_std makes what is significant from one center significant from every standpoint. That is de-centering; the source record itself says "the axiom makes the whole centerless".
- The draft that Ren is asked to accept therefore pairs N_std with a gloss that fits S0.

**Correction:** Gloss N_std as "what has significance from any center has it from every standpoint; no center is privileged". Keep "a center at every point" for S0, or mark it explicitly as the AI's phrase that Ren affirmed.

### C6. The joint-count requirement holds only for wants outlasting the stock; "the takers included" is conditional (substantive)

**Location:**

- `own-count-misses-joint-excess` correspondence ("A formation that wants its continuation must count the joint draw…");
- plan §3.3;
- chapter draft restatement (l.505) and item 6;
- every "the takers included" / "取用者在内".

**What is wrong:**

- `excess_bounded` permits `n` steps of joint excess from a level of at least `n`. `Mortal` takes in joint excess at both of its living steps, and its want is fully met; that is the point of the third limit.
- So "keep the joint draw within renewal" is a derived requirement only for a want whose horizon exceeds what is held, not for "a formation that wants its continuation" in general.
- `joint_excess_ends` ends only formations that depend at need ≥ `m`. Takers that do not depend on the condition, or depend at a lower need, continue.

**Evidence:** `Review.mortal_joint_excess : ¬ Mortal.flow.WithinJoint 0 () ∧ ¬ Mortal.flow.WithinJoint 1 ()`.

**Correction:**

- Qualify the requirement: "a formation wanting its continuation beyond what the shared condition holds must count the joint draw".
- Qualify the takers: "the takers included where they depend on it at such a need".

### C7. The witnesses' endings are stipulated, not derived (minor)

**Location:** `Exceeding.all_end` (docstring "by the law of gated renewal"), `Mortal.after_its_end`, `Downstream.one_way`, the last conjunct of `Totalizer.careful`.

**What is wrong:** Inactivity is defined: `Exceeding.live`, `Mortal.live`, `downLive`, `otherLive`. The giver's withdrawal is likewise set through `present`. The conclusions hold by definition. The witnesses establish joint satisfiability with Balances, Acting and Dependent; the derivation lives in the general theorems.

**Evidence:** `Review.exceeding_by_definition` proves `all_end` without the law. The other three are already proved by `fun _ dead => dead` in the source.

**Correction:** Reword to "consistent with the laws: …". Optionally state the forced form, quantifying over `active`: any `Dependent` web with these levels and needs is inactive from step 2 on.

### C8. "The earlier readings do not cross" overstates `conveyance_only` (minor)

**Location:** `conveyance-crosses-the-boundary` counterexample 1; README and chapter rows ("使先前读法不相关的条件相关" is fine; "do not cross" is not).

**What is wrong:**

- Under living on, read with one kind of relatum, the supply's region is not a cut either, because the keeper lives on the supply.
- For any region on which an outside formation lives, the earlier readings already make it no cut, without dissipation.
- What is new is a relation between two **conditions**, in the inflow direction.

**Evidence:** `Review.Tot.supply_not_cut_living_on`.

**Correction:** "The earlier readings relate no two conditions; conveyance alone relates the step's fuel to the supply." Also note that `region_not_a_cut` is distinctive only in direction.

### C9. Terminology: 传 is used for both conveying and transmission (minor)

**Location:** chapter l.488 ("传到/传入/传出" for `Conveys`) and l.496 ("意义传入各自区域" for `transmits`); held-lives record zh; study §47 table; continuing-self zh throughout; derived-extent-limits ("太阳传入当步的燃料").

**What is wrong:** The glossary adopts 输送 precisely because 传递 means transmission. In the zh text, 传入 now names both the conveyance of `Conveys` and N_rel transmission, in adjacent bullets.

**Correction:**

- For `Conveys`, use 输送到 / 输送入 / 从…输送出.
- For `transmits`, keep 传递 ("向各自区域的传递成立").

### C10. Smaller overstatements and parity (minor)

1. The held-lives title says "On held lives G0 is standpoint neutrality" / "G0 就是立场中立"; G0 is S0 **with** N_std.
2. "Where the whole is connected and every life is held both are equivalent to G0" needs "with some living claim". With no living claim, `Grounds` fails its seed while G0 holds vacuously.
3. The continuing-self correspondence says "the conveyance form adds no premise". It adds decided equality: `taking_draws_in` has no `DecidableEq` and `fed_from_beyond` does. Say "adds only decided equality".
4. In `derived-extent-limits` the limitations differ across languages. zh "更强的推出要求…只是不由想要自身延续推出" says derived requirements are not derived; en has "stronger requirements". Align the zh with the en.
5. The continuing-self claim calls `Lone` "with an eater taking at every step", but `supply_not_source` does not state that; cite `Lone.lone`.

### C11. Record ownership and dependency direction for `center_not_derived` (minor)

**Location:** `held-lives-g0-is-centering` (alias; formal-reuse of `own-count-misses-joint-excess` "for WithinJoint"); `derived-extent-limits` (proof binding of the same declaration; dependency on held-lives).

**What is wrong:**

- `center_not_derived` uses neither `WithinJoint` nor `careful`. It uses `Totalizer.web`, whose producer is `derived-extent-limits`, while `derived-extent-limits` lists held-lives as its own producer.
- The declaration is claimed by two records, and the producer/consumer direction is inverted.

**Correction:** Assign the declaration to one record. Point held-lives' dependency at the producer of `Totalizer.web`, or keep the link as `related`.

### C12. Ren's words: an unmarked elision and an unlisted reading of the weak form (minor)

**Location:** chapter §6.7 quote (l.478–482); weak form in §6.7, plan §4.3, study §47.

**What is wrong:**

- The quote drops Ren's middle paragraph (perspective, the illusory pure self, the meta-attractor) without an ellipsis. "all above does not require any axiom" then appears to refer only to the first line.
- Ren's "(doesn't have to be positive, we could argue as long as not harm)" also admits a deontic reading: the significance is a not-harm claim on others toward each continuation. The AI reading instead makes only undamaging continuations count. The plan mentions a "compatible second reading", but the chapter lists one reading only, and Ren's choices omit the other.

**Correction:**

- Mark the elision with "…", or quote the whole message.
- Add the alternative reading of the weak form to Ren's choices.

### C13. S0 already contains the weak form's filter; the keeper is not shown totalizing (minor)

**Location:** plan §2 ("S0 read as what wanting is"); premise card S0 row; `Totalizer`.

**What is wrong:**

- `SelfGood` ranges over `living` claims, which in `Web.valuation` are active **and not undermining**. The keeper is active at step 1 and that event is its own, but it is not living, so S0 is silent about it. "S0 = wanting" therefore carries the normative 不损 filter inside the seed.
- In `Totalizer` the keeper's clearing serves nothing: the habitat is not required, and the taking feeds nothing.
- "Renewed" holds because the sun requires nothing by stipulation, while a fresh fuel is consumed at every step. A transitive reading of "what continuation depends on" would find consumption, not renewal.

**Evidence:** `Review.keeper_active_not_living` (Probe2).

**Correction:**

- Either read wanting over `own ∧ active` and place the 不损 filter in the weak form, or disclose that the `living` reading inside S0 is normative.
- Disclose the stipulated sun.
- Optionally add a witness in which ending the other serves the keeper's continuation, a stronger case of the meta-attractor.

## Checked and found sound

- **Build.** Hashes match the receipt and record references; theorem counts 40 and 17; the only new generated `propext` constant is `Totalizer.Place.fuel.injEq`.
- **Constructive forms.** `not_inward_of_fed` needs no decidability; `inward_of_not_fed` needs `DecidableEq` (disclosed). The `fed_from_beyond` family and `boundary_crossed` conclude negated universals, and all new text says so; "at arbitrarily late steps" occurs only for hypotheses. (The inherited docstrings of `taking_draws_in`, Dissipation.lean:461–464, and `generation_draws_in`, Roles.lean:651–654, and plan §3.1 still state the conclusion that way; this predates the commit.)
- **Joint excess.** `joint_keeps`, `excess_lowers`, `excess_bounded`, `Pair.no_web`, `stays_below`, `ends_below` and `joint_excess_ends` are correct, with honest hypotheses; the gate and the `WithinOwn` comparison are disclosed.
- **Center half.** `significant_iff_held`, `significant_iff_reached` and the three countermodels are correct; decided holding is disclosed; "neither implies the other in general" is correct.
- **Standing.** G0 is kept as the adopted axiom everywhere; Ren's choices are listed and none is decided; quoted Ren words match the source exactly.
- **Housekeeping.** The 31 re-pointed records (spot-checked `living-on-and-descent`) change only receipt and hash references, with a history entry; the W3 link is honestly reported as interpretive.
