# Open questions

Everything unresolved in this corpus, gathered and ranked: the questions the whole programme rests on, the places where it contradicts itself, the questions Ren asked and nobody answered, the points where a hostile reader lands the first blow, and the empirical claims that have never been tested.

**How this was assembled.** Every canonical theory document in `theories/<slug>/` carries an *Open questions and critiques* section with two halves — objections raised inside the sources (by Ren, by commissioned reviewers, by red teams) and objections found by reading. This file merges all fifteen of those (the two theory folders opened in September, and the September drafts, were added on 2026-09-25 as dated notes), adds the questions Ren poses verbatim in `_process/reading-notes/out-hb-*.md` and `out-cb-*.md`, and orders the result by how much of the programme depends on each item. Nothing here is new criticism invented for the occasion; where a judgement is this document's rather than a source's, it says so.

**How to read it.** Citations to source documents are relative to `/Users/ren/theories/sources/`; theory documents are cited as `theories/<slug>/`; the reading notes as `_process/reading-notes/out-*.md`. Quotations from Ren are verbatim, dated, and language-marked; his typos are kept. Where a formulation is AI-drafted from his ideas or supplied by a reviewer, that is marked, because for several of the items below the *authorship* of the objection is part of its weight.

One framing note before the list. This corpus is unusual in that most of its sharpest objections are internal. The nine-reviewer whitepaper audit, the five-agent red team on the foundation principles, the SSBX claim-status ledger, the ember retraction ledger and Ren's own habit of asking "还缺了什么？" (what is still missing?) mean that the corpus's weakest points are mostly already named somewhere inside it. The problem is not that they are hidden; it is that they are scattered across fifteen documents and were never collected, so no single objection has ever had to be answered in one place. That is what this file is for.

---

## 1. The load-bearing unknowns

Six questions, and a seventh added on 2026-09-25. The whole programme — diagnosis, prescription and method alike — is downstream of them. They are ranked by how much collapses if the answer goes the wrong way, not by tractability; the tractable ones are not the important ones.

For each: why it matters, what the corpus currently says, and what would settle it.

### 1. The transition — how a critical mass leaves the race without being eaten while leaving

**Why it matters.** Every constructive mechanism in the corpus operates on the far side of a threshold it does not know how to cross. Exit-plus-free-association explains how a cooperative order stays cooperative *once it exists* — guaranteed exit means no world can hold members by trapping them, so worlds must stay worth choosing, and competition-to-dominate inverts into competition-to-be-worth-joining (`theories/the-fork-and-cooperative-infrastructure/` claim 27). It says nothing about how the first enclave survives contact with the race, and the actors best able to build the abundance layer are precisely the ones least incentivised to. The same gap appears under three names in three theories — the transition (`theories/the-fork-and-cooperative-infrastructure/`), Frontier 2 in `04-speculative-future/current/FOUNDATION-PRINCIPLES-DRAFT.md`, and the coordinated turn in `06-zhishan/whitepaper/drafts/v0.3.md` §五(五) — and is unsolved in all three. Ren names it as the crux himself.

**What the corpus says.** Four resources are named and none is tested. *Assurance mechanisms*: a public commitment registry with shared thresholds, third-party verification, compute transparency, reciprocal arrangements with executable consequences, pause protocols, capability-building for latecomers. *Threshold dynamics*: the claim that everyone except the final winner is better off under a no-AI-versus-humans rule, so consensus is rationally available rather than morally demanded (2026-02-17, `12-claude-ai-chats/2026-02-17_机器人替代与资本主义循环的危机_4c948b50.md`). *Vision as common knowledge*: the belief that others will defect is itself one of the materials the trap is built from, so making an alternative vividly thinkable is a real intervention — but, as the corpus concedes, only in coordination games, and only where defection does not still pay. *Landscape deformation*: act before the crisis rather than waiting for one, because "a crisis is a fork not a dawn" and you do not choose the basin you land in (`04-speculative-future/history-recovered-from-git/thinking_04-theory-of-change.md` §II).

Against these stand three unanswered pressures. Assurance can be gamed, forged, turned into surveillance or a loyalty test, or captured by whoever owns the verification (named as a frontier problem in `04-speculative-future/current/`). The strategy contains a tension it does not name: "build alongside, do not bring the old system down" and "make the old system optional" are compatible only while the parallel layer is small, and a commons floor that actually removes labour coercion at scale *is* an attack on the old system's core mechanism whatever its intent. And the propagation model — a few thousand meme-capable friends, ten to twenty builders, diffusion through those who already understand — is a plausible seed and an implausible cascade for a claim that requires civilizational-scale coordination inside years.

The most honest line in the corpus about this is Ren's own, recorded verbatim as his named frontier: **"I can't find the path"** (c. 2026-06-04, `04-speculative-future/history-recovered-from-git/thinking_04-theory-of-change.md`).

**What would settle it.** Not an argument — a worked case with numbers. Three things, in order of cost. (a) A formal model of the assurance game with the actual asymmetry in it: n players, heterogeneous beliefs about others' compliance, a verification technology with a cost and a false-negative rate, and an exit payoff that depends on how many have already exited. The question the model has to answer is what the critical mass actually is and what verification accuracy makes it reachable — the corpus asserts a threshold exists and never estimates it. (b) A historical base rate: the corpus already names four candidate precedents — Berg's unilateral freeze before Asilomar, the reciprocated freezes before the test-ban treaties, the 1961 moratorium collapse for want of verification, and Ostrom's commons regimes growing from costly signalling among appropriators (`05-alignment-and-moloch/2026-08-22-development-within-understanding-position-paper.md`). Nobody has done the condition-by-condition comparison the second professional review demanded for the smallpox precedent, and doing it for all four would convert "precedent proves the category feasible" into a claim about *which* conditions carried the precedent. (c) One live instrument: a commitment registry with real signatories and a published verification method, run for a year, would produce the only primary data the corpus could ever have on this.

**This document's judgement.** (a) and (b) are a month of work each and would materially change what can be claimed. (c) is the theory's own test of itself and, by 智善's rule 知而不行，只是未知 ("to know and not act is not yet to know"), the corpus is currently failing it.

**2026-09-25.** September bracketed the transition from both sides and still did not enter it.

- **The diagnosis describes the present.** The new constructive material describes what comes after.
- **The worlds start after the transition by premise.** Chiang Mai 2025 is set in an alternate 2025 in which fusion and construction robots already exist. *Generative Chiang Mai 2045* is narrated from 2045 looking back.
- **Ren set the question aside himself.** His worldbuilding opening raises it — *"But how does the transition happen? And how can we actually try to navigate this without destroying ourselves?"* — and then puts it down: *"We just think about the future after we get out"* (`worldbuilding/archive/001-ren-opening.txt`).
- **The atlas lacks it from the reader's side.** Its 2026-09-10 diagnosis found no departure point: no present trajectory, no trap, no urgency.
- **One timeline narrates the passage, as fiction.** The only year-by-year account of the passage anywhere in the corpus is the 2045 canvas's timeline (`output/pdf/generative-chiang-mai-2045.md`): shared kitchens, repair spaces, gardens and watershed projects in 2026–2029, then public investment in shared provision in 2030–2034. It is a worksheet whose institutional details it labels as proposals.
- **What would settle it has not changed.** One addition would help: a book or document of the worlds that opens in the present, with the first year of the passage in one real place.

### 2. Whether the lock is cognitive or participatory

**Why it matters.** This is the question that decides whether the corpus's own activity is the right instrument. Two diagnoses are on record and they call for opposite interventions. The first, from `01-writings-2025/grok.md`, is cognitive lock-in: alternatives have been made unthinkable, and the people harmed defend the arrangement because they cannot see past it — *"we're not just outgunned; we're outthought"*. The second is Ren's own, in 2026: **"我不这么认为，一般人应该都能看清里面利害关系，只是大家原教旨式的遵循着他们的邪教而已"** — "I don't think so; ordinary people can generally see the stakes clearly, it's just that everyone follows their cult fundamentalistically" (2026-04-11, `12-claude-ai-chats/2026-04-11_大同的技术可实现性_893f7a0e.md`).

If the first is right, the work is teaching, and the good bots, the museum, the manifestos, the essays and this whole corpus are on target. If the second is right, teaching is nearly worthless and the work is payoff engineering, assurance and exit construction — and the corpus's chosen deliverables are a category error. The two claims have never been put in the same paragraph.

**What the corpus says.** Both, in different documents, without adjudication. The selfishness-spiral cluster's third loop is explicitly cognitive; the good-bot lineage is built on it, and on the claim that trust is not a precondition for coordination but an *output* of shared seeing (2025-03-14). The 2026 material is participatory: the trap is objective, and the perceptual half only bites in coordination games — "where defection still pays, only changed payoffs, assurance, affordable exit and answerable defense move anything" (`theories/keep-the-possibility-space-open/`). The August 2026 position paper takes the cognitive side hard: the binding constraint is common knowledge of danger. The May 2026 stance takes the participatory side hard: cognition itself is what the attractor selects, so common knowledge among instrumentally-selected principals yields a race to be the one who survives the rupture (`theories/alignment-selection-on-cognition/`).

There is a bridge in the corpus that neither text uses, and it is the most promising thing here: Ren's claim that the attractor of attractors is *the belief that one is in a survival state*. On that reading the two diagnoses are the same lever — what the players believe the game is — and manufacturing common knowledge of the danger *is* an intervention on consciousness. That reading is stated in `theories/alignment-selection-on-cognition/` as a reading, not as Ren's position, and nothing develops it.

**What would settle it.** A behavioural test, and the corpus already contains one design without knowing it. The good bots are prompts, not experiments (`theories/selfishness-spiral-and-narrative-value-frames/`); converting one into a trial — does exposure to the loop-seeing intervention change behaviour in a game where defection still pays, versus one where it does not — separates the two hypotheses directly, because cognitive lock predicts an effect in both and participatory lock predicts an effect only in the coordination arm. Second, cheaper: the 短剧 natural experiment named in `theories/drives-narrative-attractors-and-mind/` (paywall placement against completion rate) tests whether an attention environment collapses behaviour onto the fastest-activating attractors, which is the construction half of the same question.

**This document's judgement.** The evidence favours the participatory reading as the *default* and the cognitive reading as a real but bounded second mechanism, for a reason that is already in the corpus: Ren's 2026-06-03 observation that "even though we have so many analysis, and can recognize the dynamics and name them as moloch or metacrisis, we don't seem to find hope to escape them — coordination beyond them becomes unthinkable". Naming has demonstrably happened; escape has demonstrably not. That is evidence against the pure cognitive lock and for a mixed model where the missing thing is not sight but a *reachable* alternative. The corpus should adopt the mixed model explicitly, because it also tells the constructive branch what its job is: not to explain the loop but to build the address. 希望的单位不是口号，是地址 — the unit of hope is an address, not a slogan.

### 3. Who owns the abundance layer

**Why it matters.** The constructive branch's entire claim is that the same automation capacity is either the floor of everyone's freedom or the most powerful instrument of dependence ever built, and that the technology does not decide which: **丰裕若为门，即是最柔软的项圈** ("if abundance is a gate, it is the softest collar"). A layer that provides necessities is not a market you can leave but a provision you can be cut off from. So governance of that layer is, in the corpus's own words, the whole game.

**What the corpus says.** It has a good negative criterion and no positive one. "Common" is defined operationally as non-capturable in practice — access rules, auditability, local accountability, dispute resolution, exit rights, no unchecked power to convert the floor of life into dependence — and explicitly never by being called public, shared or benevolent (`04-speculative-future/current/FOUNDATION-PRINCIPLES-DRAFT.md` principle 7). Capture has five marks: hidden, one-way, coercive, non-substitutable, irreversible, which makes "non-capturable" testable rather than rhetorical (`06-zhishan/whitepaper/drafts/v0.2.md` §2.2). Provision must be decoupled from status, obedience, data surrender and single-provider attachment.

Against that stands the sharpest single sentence any reviewer has written about this corpus, from the commissioned nine-perspective audit of the 智善 whitepaper: **丰裕公地无主语** — the abundance commons has no subject. 谁出钱、谁建、资本手里的自动化产能怎么变成公地 (who pays, who builds, how automation held as capital becomes a commons) is answered only by 应推动, "should be promoted". **设计有了，供给为零** — the design exists, the supply is zero (`06-zhishan/whitepaper/reviews/v0.4-multi-perspective-review.md`). The same review notes that the framework connects to no welfare system, no cooperative tradition and no mutual-aid tradition, and that labour is missing from the addressees entirely: builders, governors, researchers, publics, humanity and machines each get a section; workers do not.

Two further gaps compound it. "Non-capturable in practice" has criteria but no verification procedure — who applies the five marks, on what cadence, with what consequence when a layer fails — which is the 无主语 problem one level down. And the physical claim underneath is unaudited: "coordination, not physics" is doing enormous work, and nobody has estimated the energy, materials, land or ecological requirements of a necessities floor at population scale, nor retained the cooperative-turn draft's own honesty about the last ten per cent (chip fabs, precision tooling).

**What would settle it.** Three concrete things, none of which is philosophy. (a) A supply model for one necessity in one place: what a food or housing floor for a defined population actually costs in capital, energy and land, who could plausibly own the assets, and what legal form (public trust, cooperative federation, foundation with a non-conversion covenant, municipal utility) survives the five marks of capture. The corpus has never done this once. (b) A named legal-institutional precedent study: municipal water, the Alaska Permanent Fund, mutual insurance, land trusts, open standards bodies, the Antarctic Treaty system — the corpus cites the *category* of planetary technology and has never examined how any instance of it actually held ownership. (c) A conversion mechanism: the review's question is specifically how automation *held as capital* becomes a commons, which is a question about taxation, procurement, patent policy, cooperative buyout or dilution, and not about design criteria at all.

**This document's judgement.** Of the six unknowns this is the most tractable and the least worked, and it is where the corpus is most vulnerable to the charge that it is diagnosis wearing a prescription's clothes. One worked supply model would do more for the programme's credibility than another round of criteria.

**2026-09-25.** Three developments make the question narrower and harder to avoid.

- **The branch put production first.** On 2026-09-07, at Ren's request, `theories/the-fork-and-cooperative-infrastructure/` was rewritten around productive recursion: capacity that helps build further capacity, pointed at generous provision. Ownership became the safeguard rather than the mechanism. Two bounded evidence notes find working components (automation already used to make robots and machine tools) and no demonstrated complete autonomous reproduction.
- **The whitepaper made the item its own.** The unified whitepaper (`drafts/2026-09-05-generative-foundations/WHITEPAPER-v1.1.md`) asks the question in this item's words and names the first step: a supply model with a named provider, costs, access and responsibility for continuity (§11.9). Its §1.6 recurrence supplies the bookkeeping. It shows whether a unit reproduces its capacity or only postpones a deficit with a one-off injection.
- **The place is now obvious.** Chiang Mai: where Ren is, where the city was imagined, and where the field record is owed.

The supply model in (a) above now has an engine, an accounting form and a place. It still has no payer.

### 4. Whether a counter-attractor can avoid becoming a new totalization

**Why it matters.** It is a coherence condition on the entire positive programme. The meta-attractor is defined by a second-order property — it does not merely pull outcomes, it captures the rule by which outcomes are selected, and its measure is the progressive loss of independent capacity to sense, refuse, correct, exit, maintain alternatives and start again. By that definition, any counter-move that succeeds broadly enough to close the field in its own favour *is the same object under a better name*. The corpus states this against itself: NP holds that counter-attractors "may themselves need to be exopoietic in a constructive sense"; V32 says defectors must not be allowed to re-ignite the old attractor and speaks of civilization as "a unified organism"; and LONG wants Wamo to become "the dominant civilizational attractor". Each of those, taken with the definition, describes a totalizer.

**What the corpus says.** It has an answer, and the answer is good, and it lives in the wrong documents. The 2026 context statement is as flat as it can be made: "The positive goal is not one benevolent counter-attractor replacing the current one. It is an ecology in which generative attractors can coexist, challenge one another, learn, and give rise to forms no current center can specify" — and, on the temptation to use interdependence as a warrant for unity, **"Unity without differentiation becomes another totalizing attractor"** (`06-zhishan/writing-program/context/meta-attractor-foundational-context.md`). The same answer arrives from three other directions. 大同 read as 北辰, a pole star that orients and cannot be arrived at, is deliberately unable to become an end-state that is achieved and then defended. 和 ≠ 同 is formally load-bearing rather than decorative: 大同 is neutral on uniformity while winner-take-all *requires* it, so reading 大同 as 整齐划一 (regimented sameness) is a refutable misreading (`07-shengsheng-buxi/ssbx-repo/义理/W_非道之形式.md` §2.5). And the keystone concedes its own status honestly — the one line held without exception, *we will not close the world*, is a deliberate **minimal totalization**: the single rule whose function is to keep every other rule, that document included, revisable.

So the question is largely answered in principle. What is genuinely open is whether the answer survives operation. Three unresolved pressures: the **dampers-become-attractors** case, which the corpus raises against itself and never closes — 科举 was designed to break hereditary capture and became its own proxy-optimization trap (八股), and every prescription this corpus offers is an institutional damper; the enforcement antinomy, since any power sufficient to stop a determined superhuman defector is the concentration the framework forbids; and the fact that the resolution has never been carried back into the meta-attractor documents, the Wamo manifestos, or the essay set that would actually be published.

**What would settle it.** A stated, checkable openness criterion attached to the constructive proposals themselves, plus one adversarial application. The corpus's own materials supply the criterion: 伪开 (pseudo-openness) is defined as the conjunction of 似开 (having the appearance of openness) and 实闭 (closure that is verifiable and survives audit) — a definition with the useful property that it is checkable rather than rhetorical. Run the abundance commons, the Wamo protocol, the museum's curatorial governance and 智善's own publication apparatus through it and publish the results. Second, the north-star test the integration document already wrote and nobody has used: **does this make exiting bad games easier, or only make explaining everything easier?**

**This document's judgement.** This is the item where the corpus is closest to done and furthest from having said so. The single highest-value edit in the whole programme is a short counter-attractor design note that states the openness criterion, applies 伪开 to the corpus's own proposals, and is then cited by every constructive document. It is named as the second-most-valuable missing piece in `theories/meta-attractor/` and has not been written.

**2026-09-25.** The unified whitepaper's §10.11 states a candidate loop for a counter-attractor that can reproduce itself:

- basic support lets people investigate and speak;
- reliable feedback improves decisions and services;
- real improvement builds trust and cooperation;
- cooperation produces the resources to maintain the common conditions.

It adds the check that the benefits reach the people who maintain those conditions. It does not apply 伪开, which it drops. But its three custody rules (§11.4) are a checkable criterion of the kind this item asks for, and they could be run against the corpus's own proposals instead.

### 5. What makes a recovered frame resistant to being metabolised

**Why it matters.** The corpus's method *is* recovery. "Go back to ancient times and other cultures to find the ground" is not nostalgia and not a strategy step; recovery and preservation are the work itself, holding an alternative open so that it is available when the dominant frame fractures (`05-alignment-and-moloch/2026-05-28-alignment-core-stance.md`). If recovered frames are metabolised as reliably as everything else, the method is a consolation rather than a strategy, and the largest single investment in the corpus — the 文言 recovery programme, 生生不息论, 仁义礼智信, 大同, the Human Solutions Museum — is aimed at a target that cannot hold.

**What the corpus says.** The objection is stated in full and the answer is marked as a guess. Daoism becomes wellness products, Buddhism becomes corporate mindfulness, Confucianism becomes authoritarian legitimation, Stoicism becomes Silicon Valley productivity content. The provisional answer: frames carried by communities actually living them resist translation in a way text-borne frames do not — **"Practice has a thickness that concepts don't."** Marked uncertain in the source.

The general form of the worry is the internet lesson, which is the corpus's most-earned empirical claim: a powerful general-purpose technology dropped into a Moloch-shaped system is refactored to serve it, the affordances are subordinate to the logic, and then the *discourse about* the technology is metabolised too — into safety theatre, AI-ethics-as-PR, compliance frameworks that lock in incumbents, and an alignment-as-career track inside the labs creating the problem. The working rule that follows is severe and applies to this corpus: **anything legible enough to be adopted at scale by current institutions is legible enough to be neutralized by them.**

Four historical analogues are named as evidence that preservation can work — early Christians, Stoics in Roman decline, Daoists in the Warring States, Confucians under Mongol rule, Sufi orders through dynastic transitions, Christian monastics through the early medieval collapse — sharing four properties: they saw what contemporaries could not, they did not expect to win in their lifetimes, they preserved frames through hostile epochs, and they demonstrated by being more than they argued. That is a real answer and it has never been examined as evidence rather than cited as encouragement.

**What would settle it.** The analogues are a dataset, not an illustration, and treating them as one is a tractable research project. Every one of those traditions was also captured at some point — monastic orders became landholders, Confucianism became imperial ideology, Sufi orders became state-aligned. The question is not whether preservation is possible but *what separated the episodes that survived translation from the episodes that were absorbed*. Candidate variables the corpus already implies: embodied practice versus text; economic independence of the carrier community; whether the tradition had an internal correction mechanism; whether it was adopted by power during a period of plenty (Ren's own observation, 2026-03-18, that the Confucian ideal was historically adopted by exactly those who held power, especially in times of plenty); and whether it could refuse the project it was recruited into. That last is already stated as a requirement elsewhere in the corpus — the standing requirement on a functionalized tradition is that it be able to *negate the goal* efficiency serves, and to refuse the project itself (`06-zhishan/` writing-program audits) — and it is the best candidate for the operative variable.

**This document's judgement.** The most promising formulation available is: a frame resists metabolisation to the degree that it retains the capacity to refuse the system that would adopt it. That is testable against the analogues, it is consistent with "practice has a thickness that concepts don't" (a practice can decline; a concept cannot), and it gives the recovery programme an actual design constraint instead of a hope. It is not stated anywhere in the corpus, and this document offers it as a reading rather than as Ren's position.

### 6. Whether the diagnosing subject is itself selected — and can escape

**Why it matters.** It is Ren's own question, asked once, and every prescription in the corpus presupposes an answer it never gives:

> 在当下的社会环境中，我们有多大的概率逃脱这个竞争性主体形式？如果我们人类本身即受到此attractor筛选和塑造？
> ("In the current social environment, what is the probability that we escape this competitive form of subjecthood — if we humans are ourselves selected and shaped by this attractor?")
> — [zh] 2026-07-03, `_process/reading-notes/out-cb-07.md` #106

The theory's distinctive claim is that the dynamic is not merely structural but *epistemically internalized* — the system concentrates not just capital but a way of seeing, and Moloch is in the mind. If that is right, it applies to the people writing this corpus, to the reviewers commissioned to attack it, and to the models drafting most of its prose. Ren says the last part explicitly, to a model whose output he distrusts: **"这是西方当代叙事进入totalizing attractor，然后产生的文本进入了你的训练导致的吧"** — "this is contemporary Western narrative entering a totalizing attractor, and the resulting text entering your training, isn't it" (2026-07-03).

**What the corpus says.** Nothing directly. Three partial approaches exist and none is an answer. Ren's own methodological caveat limits the claim without answering the question: **"我不是说这是一个真理或者必然，我们可以把发展速度降下来"** — "I am not saying this is a truth or an inevitability; we can bring the rate of development down" (2026-07-03). The corpus's method rules are the practical response — catch the operationability reflex, catch asymmetric scrutiny of non-Western vocabulary, catch the model mirroring the user ("I think you were basically mirroring my view, now let's be honest", 2026-03-26), refuse binary framing, refuse lossy consolidation. And the deepest recorded correction is Ren catching the totalizing habit in his own reasoning style: the reasoning kept splitting the world this-versus-that and siding with a pole — resilience over prevention, distributed over central, AI for humanity — and *the cut itself* is the totalizing move, performed while arguing against totalization (`theories/memories-and-working-style/` claim 76).

The 2024 answer to the same question, which the 2026 material quietly requires and never restates, was that knowing you are constructed is itself liberating. The 2026 answer is a refusal — "Why do I have to satisfy my own drive architecture and be obedient to it?" — grounded in being part of a process rather than a self. These are compatible but not identical, and the 2026 version needs something the 2024 version does not: a place to stand that is not itself constructed. The corpus has never said what that is. `theories/drives-narrative-attractors-and-mind/` calls this its deepest unresolved problem, and it is right.

**What would settle it.** Nothing settles a probability estimate over an unmodelled process, and the corpus should stop treating it as a question awaiting an answer. What it can do is convert it into a design constraint, which is what the other five unknowns are already doing without saying so: item 2 asks what would change behaviour in someone who already sees; item 5 asks what lets a frame refuse the system that would adopt it; item 4 asks for a checkable test the corpus can fail. Those three are the operational content of Ren's question. The honest statement for any published version is that the diagnosis is a claim about the present condition rather than a law, that the authors are inside it, and that the corpus's answer is procedural — public corrigibility, symmetric application, a dissolution clause, and a north-star test it can fail — rather than epistemic.

**This document's judgement.** This question should be the *preface* of any published version, not a footnote. It is also the strongest thing the corpus has to offer a skeptical reader: a framework that names its own capture condition and installs machinery against it is doing something almost nothing else in this genre does. Stated as a preface it is a strength; left unstated it is the hole the first hostile reviewer will find.

### 7. How the mind that uses the capacity is formed (added 2026-09-25)

**Why it matters.** On 2026-09-25 Ren moved the constructive branch's central risk from the engine to the mind: **"this isn't the problem - how we can use it wisely, is the key. we can grow exponentially till we met our need, but we can't compounding forever. the problem is the mind not the approach"** (`16-claude-code-directions/2026-09-25-the-mind-not-the-approach.md`).

The engine is productive recursion pointed at generous provision (`theories/the-fork-and-cooperative-infrastructure/`), and it is bounded by need. What compounds in the diagnosis is relative advantage, which never reaches enough. Whether a growing capacity stops at enough or turns into advantage is decided by the frame directing it.

So the constructive programme now depends on a question the diagnosis poses and never answers constructively. How is a mind formed that uses great capacity wisely? And how is it kept from being selected out while the capacity grows? This is item 6 turned outward. Item 6 asks whether the diagnosing subject can escape; this asks whether the directing subject can be made.

**What the corpus says.** More than it says on most items, in pieces that have never been joined:

- **The diagnosis.** Minds are selected and shaped by the environment that rewards them: narrative-value frames, selection on cognition, 铸心之门.
- **Environment makes mind.** Narrative is the interface to the drives, so the environment is where to intervene (`theories/drives-narrative-attractors-and-mind/`).
- **Cultivation.** 修身 and 教化 in 生生不息论. The whitepaper's §10.6 puts 良知, 修身 and 真善美 into daily practice. Its §11.6 asks an organisation to watch what its meetings, rewards and shared stories make easier to keep.
- **The world-designer's view.** Design for the players who never win (`worldbuilding/archive/001-ren-opening.txt`).
- **The watershed game.** An AI-drafted scene in `theories/architecture-for-a-living-earth/chiang-mai-2025/`: a points system teaches the wrong thing, and the community sees it and revises it.

None of them makes the join. The constructive texts describe the engine and the worlds. They never say how the minds that will direct them are formed, or what protects that formation, during the passage, from the selection the diagnosis describes.

**What would settle it.** Not a proof. Three things would move it.
- **(a) A text joining the engine to the account of how minds are formed.** Because what counts as *enough* is set by the frame, the supply model of item 3 needs a stated standard of need, and an account of who sets it and how it is kept from drifting.
- **(b) The corpus's own experiments, turned on this question.** One: the watershed-game pattern — reward, observe what the reward teaches, revise — run as a real practice in one Chiang Mai association, with before and after recorded. Two: the good-bot two-arm trial of item 2, which already tests whether seeing the loop changes behaviour.
- **(c) Historical cases of abundance that did not turn into advantage.** That means a commons bounded by need that stayed bounded, and what formed and held its members' frame. Item 5's dataset of traditions is the same work.

**This document's judgement.** Ren's ruling is right on the corpus's own terms, and it sharpens the constructive task rather than softening it. The engine is the part with evidence notes. The mind was always the hard part, and it is the part the diagnosis says the present selects against. The constructive texts should state this as their central open item, in place of the rate question that an earlier draft of `MAP.md` raised on the same day.

---

## 2. Contradictions inside the corpus

Genuine disagreements, not loose ends: places where two documents, two versions or two theories assert incompatible things. Each is stated fairly on both sides, with a verdict on which side the evidence favours. Where the corpus has already resolved something and failed to propagate the resolution, that is said.

### Whether this is one theory at all

**Side A — one theory.** Four names, one mechanism: the selfishness spiral, the meta-attractor, selection on cognition and 总体化吸引子 make the same causal claim in four vocabularies, each adopted to repair a defect in the last. That is argued from the drafts in `MAP.md`, and it is the reason the corpus is navigable rather than fifteen unfinished books. Beyond that, a three-layer reading — the same move at the metaphysical, coordination and civilizational scales — was offered to Ren in April 2026 and he built on it immediately.

**Side B — a set of resonances still cohering.** The three-layer reading is not Ren's. It is an AI answer to his question "among all these things, you see a complete theory, don't you?", prefaced by its author's own warning — "tell me where it's real and where I'm projecting coherence onto what's actually still in motion" — and it closed by asking him directly whether he experienced it as one theory or as a set of resonances he was still letting cohere. **He did not answer.** His next message changed the subject. (`12-claude-ai-chats/2026-04-16_Recent_conversation_insights_96d77b9f.md`.)

**Why this is not a quibble.** Ren has a standing rule against exactly this move, stated in his own words after catching it being done to his principles: finding the one root, folding everything into it and deleting what does not fit "IS reductionism… we can't reduce everything into one principle" (`theories/memories-and-working-style/README.md`). An organisation that unifies his corpus around a single claim performs on his archive the operation he forbade on his text — and the unification was proposed by a model, not by him.

**Where the evidence lands.** The four-name identity is supported by the drafts and should be kept: those really are one mechanism renamed, and reading them as four separate theories produces the illusion of four independent corroborations of one argument. The three-layer identity is not established. What can be said is that the same move — a thing constituted by its relations rather than by what it encloses — is made independently at three scales, which is weaker and still substantial. `MAP.md` has been amended to say only that. **Settling it needs Ren, not another reading**: the question he was asked is still open and still worth answering.

### The meta-attractor's two mathematical layers

**Side A — the covariance dynamic.** Decompose a system's fitness signal into weighted proxies, let winners buy influence over next round's weights, and you get `ẇ = λ C w` with λ = ηg′f′ > 0 and C = Cov(p,p): weights converge to the leading eigenvector of the proxy covariance matrix, so *a civilization's terminal ends are the principal component of its proxy covariance structure*. CAOC (Control, Accumulation, Optimisation, Competition) then falls out as a derivation rather than an assertion, because each has a structural reason for high covariance with everything else. This layer yields four measurable levers — in two classes, which the source does not separate: covariance surgery and the injection of *anti-correlated* proxies change where the weights land, while the gain terms η and g′f′ enter only through the scalar λ and so change only when they get there — and the corpus's nearest approach to a quantity a policymaker could act on: eigenvalue budgeting, λ₁ ≤ −ln ρ / T (`03-meta-attractor/2025-08-formal/2025-08-10-comprehensive-mathematical-definition.md`). That budget is not usable as written; see the third caveat in the verdict below.

**Side B — the two-timescale control layer.** Rules are a slow state: `ẋ = f(x;λ)` fast, `λ̇ = ε ḡ(x,λ)` slow, with a control barrier function making a safe set forward-invariant, so safety wins over the nominal objective whenever they conflict. This yields barrier certificates, viability kernels, optimisation-bandwidth caps and enforcement in the fast layer (`03-meta-attractor/2025-10-essays/`).

**The contradiction.** They are never reconciled, and they should be trivially reconcilable: w *is* a λ, and ẇ = λCw is a particular ḡ. Nobody says so. Worse, they are not merely unjoined — they carry different diagnostic vocabulary (PDI is defined twice with two incompatible formulas, one predictive and covariance-based, one descriptive and decision-weight-based; CI and DE name two different index sets in the site and the essay it cites), and the publication layer has no route back to the mathematics at all: the crosswalk, claims file and manifest reference only the October essays, so the 2025-08 files — the only place with a derivation and a quantitative safety spec — are invisible to the build.

**Verdict.** Side A is the load-bearing one and Side B is its institutional translation, and the identification should be made explicitly: *the covariance dynamic is the specific slow-layer law the barrier framework needs*. Making it would be a genuine contribution and would give eigenvalue budgeting a home inside the barrier framework. Three caveats must be carried: the mean-zero assumption behind ẇᵢ = ηCov(pᵢ,R) is stated "for simplicity" and is a real weakness — with non-zero means the E[pᵢ]E[R] term is generally dominant and the eigen-conclusion does not follow, so the scope must be restricted or the assumption justified (proxies as deviations from population mean); a sign error propagates in two of the three 2025-08 files (λ₁ ≤ ln ρ/T with ρ < 1 forces λ₁ < 0, impossible for λ = ηg′f′ > 0), corrected only in `comprehensive-mathematical-definition.md`; and that correction did not finish the job, because the eigenvalue budget is still broken in the corrected file. **Reuse must draw from that file and no other, and must not quote the budget at all until it is re-derived.** The budget's two remaining defects: the prose sets "a safety factor ρ < 1" and requires that amplification "not exceed this factor" while the formula caps amplification at 1/ρ, so a stricter-sounding ρ licenses more growth (ρ = 0.01 permits a hundredfold amplification) — consistent only if ρ is read as the reciprocal of an amplification ceiling A > 1, i.e. λ₁ ≤ ln A / T; and λ₁ is the wrong target, since w is unnormalised, so its growth factor is not a governance quantity, while what decides whether ends rotate onto the CAOC composite is the spectral gap λ₁ − λ₂ — and scaling η, g′ and f′ down uniformly divides λ₁ and λ₂ by the same factor, so a portfolio can meet the budget in full without slowing the alignment of ends at all. What is needed is a budget on the gap, or a bound on time-to-alignment under weights normalised to sum to one; neither has been derived, and the claim that this is the corpus's one actionable governance quantity has been withdrawn from `theories/meta-attractor/README.md` until it is (see its open items 31–32). `The_Meta-Attractor_Complete-why-attractor-thinking.md` additionally has a corrupted slack-coefficient formula and should be retired rather than edited.

### The two senses of "meta-attractor"

**Side A — the pathology.** A meta-attractor is a self-reinforcing pattern that acquires power over the rule by which states are selected; its measure is the progressive, non-compensable loss of independent capacity to sense, refuse, correct, exit and start again. This is the sense in the 2025-08 formal layer, in most of the October essays, in the 2026 Chinese research line (总体化吸引子) and in 智善.

**Side B — the engineered target.** A meta-attractor is a designed stable region in rule space that keeps a system inside a safe set — the thing governance should *build*. This is the sense in `meta-attractor-essay-long.md`, in the policy-hero variant and in the Scholar readiness variant, all from the same month as Side A.

**The contradiction.** The same word carries opposite valence in documents written weeks apart, and the conflict is never acknowledged. Both usages are formally coherent — a stable set in rule space is the same object whether the fast attractors it induces are safe or catastrophic — which is exactly why publishing both under one word destroys the handle.

**Verdict.** Keep "meta-attractor" for the pathology; it is the sense that carries the diagnosis, the sense the Chinese line uses, and the sense every other theory in the corpus imports. Coin a distinct term for the engineered region — the corpus's own vocabulary already has candidates in 护开 (protecting the open) and the viability-kernel language of the control layer. This is a cheap fix and it is blocking publication of the theory as a single thing.

**2026-09-25.** A third sense has appeared, and it goes against this verdict. The unified whitepaper (`drafts/2026-09-05-generative-foundations/WHITEPAPER-v1.1.md` ch. 6) uses "Meta-Attractor" for the mechanism and its analysis, with no sign attached. Learning, cooperation, ecological recovery and public provision can form stable feedbacks too (§6.11). The harm goes to 总体化, and the remedy to "Counter-attractor". That is a usable ruling, the reverse of this one. The organisation's two founding texts cannot both stand, so one of the two rulings has to be adopted explicitly.

### Plurality versus 大同

**Side A — plurality as survival architecture.** Ren's founding 2024 turn: the problem is the design of the game, not the content of anyone's ideology, so forbidding others to redesign their own game is itself tyranny. "Forcing everyone to live in a neo-liberal world, a socialist world, capitalist world, or and libertarian world, itself, is tyranny" (2024-07-29). Redundancy is the argument: "So at least, if one game fail, you can join another one." The permissiveness is deliberate and extends to bad outcomes — "even if there is the possibility of doom, you choose your way of being and they choose the others… Even if their lies the possibilities, for example, into cyberpunkish societies or tyranny, it's their own freedom" (2024-07-31); "you can have a society where it violent like mad max" (2024-11-03).

**Side B — 大同 as direction, and the 2026 limits.** 大同 is not uniformity: 万物并育而不相害, and 和 ≠ 同 is formally load-bearing. But the 2026 drafts install floors no world may opt out of — protections for children and dependents, bodily autonomy, exit, the ecological web — and the 智善 line adds a substantive good (generative, relational, corrigible, non-foreclosing) that a world could fail.

**The contradiction.** Both are defensible and the corpus does not notice they conflict. If a society may choose tyranny for itself because "it's their own freedom", the 2026 floors are a violation of exactly the plurality the 2024 argument founds. If the floors hold, then the 2024 permissiveness was overstated. There is a second, related collision inside the same cluster: three generated futures share a boilerplate Foundation Check and near-identical governance patterns, which makes them illustrations of one template rather than the plurality they claim, and none of them resembles the Mad Max or Moloch-libertarian worlds Ren's own 2024 catalogue insisted on permitting.

**Verdict.** The 2026 position is right and the reconciliation is available inside the corpus without anyone having stated it. The floors are not a value imposed on a plural field; they are the *conditions of plurality's own continuation* — exit, the capacity to refuse, the ability of the next generation to have been able to choose at all. A world that removes exit is not one option among many; it is the removal of the mechanism the 2024 argument depends on. That is exactly the shape of the keystone's admitted minimal totalization, and it is the same move as 护闭 (closing here so a wider field stays open). Say it in those terms and the contradiction dissolves; leave it unsaid and the corpus is asserting both permissiveness and floors on the same page. **What must not be lost in the repair is the 2024 permissiveness's actual content**: that the generated futures are homogeneous is a real failure, and a plural catalogue has to include worlds the author would not choose.

### AI as governor versus AI as teacher

**Side A — AI as coordinator or governor.** From `01-writings-2025/cognitive_lag.md`, and stated by Ren as a forced conclusion with the hedge welded on: *"human, has no chance of both be in charge of this kind of society and keep them stable(without runaway effect), the only seemingly possible solution is to simultaneously develop intelligence and delegate coordination to it, surrendering our power to AI(or exponentially growing intelligence) becomes the only possible resolution(Doesn't mean it can work, only in theory)"*. `caboc.md` carries it with the Platonic-guardian risk attached.

**Side B — AI as teacher.** The good-bot lineage: an intelligence whose job is not to govern but to teach people to see the loops, on the ground that trust is an output of shared seeing rather than a precondition for coordination.

**Side C — AI as planetary technology.** The 2026 position: capability that runs *beneath* human games rather than inside them, like smallpox eradication or weather observation; **do not fight for us**; AI reallocated from the racetrack to the instruments.

**The contradiction.** Side B is a response to the same cognitive-lag problem that produced Side A, and it keeps humans in charge — which is a rejection of Side A — and the substitution is made silently. Side C is a third option and is reconciled with neither. Three designs with three different failure modes: a captured guardian; a persuasion engine with an authority problem (the Jesus-persona bot raises exactly the top-down-narrative objection the same cluster's manifesto makes); and an instrument layer whose referee-side models are trained by the same actors under the same commercial pressure as the product-side models — which is the impossibility claim in `theories/alignment-selection-on-cognition/` turned against its own prescription.

**Verdict.** Side C is right and is the only one of the three that the rest of the corpus can support, because it is the only one that does not require the AI to be a party in a human contest. But it inherits an unpaid debt: the corpus's own strongest claim — that inside these dynamics you cannot safely train an AI that is not itself captured — applies to instrument-side AI exactly as it applies to product-side AI. Either the impossibility claim is weaker than stated, or Side C needs an argument for why verification, monitoring, interpretability and treaty-compliance models escape what deployed models cannot. **Nothing in the corpus reconciles them, and this is the sharpest unpaid debt in the whole prescription.** The nearest available answer, and this document offers it as a reading: instrument-side AI escapes not by being trained differently but by being *positioned* differently — its outputs are checkable by parties with opposed interests, which is a property of the deployment structure rather than of the model. If that is the answer it should be argued, because it makes symmetric verification the load-bearing element rather than an implementation detail.

### The May posture versus the August programme

**Side A (2026-05-28).** Operationability is a symptom: the reflex to convert a diagnosis into an action plan is itself the disease's grammar, and the work is a posture — recovery, preservation, demonstration — held through a hostile epoch. Anything legible enough to be adopted at scale is legible enough to be neutralized.

**Side B (2026-08-22).** A fully operational programme: domain-ordered prohibition, a measurable tempo criterion, signal-debt repayment, reallocation of AI to the instruments, founded by legible restraint. The missing condition *is* legibility; evaluations and disclosures are the sensory organ; the paper calls itself a small legibility event.

**The contradiction.** Two, actually. The operationability reversal (is an action plan a symptom or the deliverable?) and the legibility contradiction (does legibility get you adopted or get you neutralized?). May's own internet lesson predicts that August's instruments become the "compliance frameworks that lock in incumbents" that May already lists as a metabolization channel.

**Verdict.** The May rule was about *this subject matter* rather than about action plans as such — the evidence is that Ren operationalizes relentlessly in the engineering work and shows no allergy to plans in general. August is the stronger document and should be the published prescription. But it must carry May's warning as a stated design constraint rather than dropping it: the test for any proposed instrument is whether it can be adopted *without* becoming an incumbent moat, and the corpus's own 伪开 definition is the tool for checking. Two further things August dropped without argument and should restore: labour markets, which May names first and which August's own tempo criterion would rank near the top, since employment law, welfare, training institutions and the wage bargain are among the slowest rule-metabolisms in the list; and the claim that the wielder must change, which August loses when it replaces "inadequate mind" with "signal deficit" as the justification for pause. The signal-deficit argument is more defensible; the two justifications currently coexist without being related.

### The two accounts of evil in 生生不息论

**Side A (v9–v13 doctrine).** 成闭 alone is evil — closure that does not reopen — and there is no evil at the noise pole. 护闭, closing here so a wider field stays open, is a use of the mean rather than an exception.

**Side B (the proof layer, `证明篇-v0.6.md` §19).** Evil is being stuck at *either* pole, freezing or noise, and closing is a necessary phase of writing structure in. The proof layer issues a revision order on this point (①恶两极化，阖非恶) and the 2026-07 books do not incorporate it.

**Verdict.** Side B, decisively. It is the one with a derivation; it explains why 护闭 is not merely a licensed exception but a structural necessity; and it matches the 好-as-interval structure the value branch reached independently. The doctrine has not absorbed it, and any published version should carry the two-pole account. The same revision order also proposes renaming 善恶 to 继/绝 (continuing / severing), which is worth taking seriously for a different reason: it removes the moral register from a claim the corpus elsewhere insists is structural rather than moral.

### The roots: 間, 動, 一, 一元

**The dispute.** Four candidate primitives are in play with no reconciliation document. 间生论 and the 致知 version both argue that 元 depends on 間. The Lean kernel takes 動 as the primitive axiom and derives 元 from it. The atom roster keeps 元 among the 43 CoreAtoms directly under 一元. And Ren's own May-2026 line is 「根位非事，而是一也」 — the root position is not an event but the one. Alongside this sit two ontologies that also never meet: the 易/R₈ line says closure is at 256 with 道 as the identity; the R-family line says the substrate is δ-polymorphic with no privileged cardinality, and nothing explains what happens to 道's five identities when δ ≠ Bool.

**Verdict.** This one should not be resolved by picking a winner, and the corpus's own rule says so — never flatten a plurality into one root. What is needed is a mapping document, not an adjudication: 間 is the ontological primitive (a state not exhausted by what it already is), 動 is the operational primitive the formal system needs to generate anything, 一 is the identity/addressing primitive the engineering needs, and 一元 is a claim about *concept genealogy* rather than about substance — "我说的一元当然不是基数，是所有概念回归同一root" ("what I mean by 一元 is of course not cardinality, but all concepts returning to the same root", 2026-05-05). Those are four different jobs and there is no contradiction once the jobs are named. **Naming them is a day's work and it has never been done**, which is why the same argument recurs across `theories/jian-and-wenyan-as-formal-language/`, `theories/shengsheng-buxi-generative-existence/` and `theories/spirit-space-token-and-yi-substrate/` in three vocabularies.

### 心不可外化 versus 心 as a first-class type

**Side A.** The 間 essays hold that the actor-side 心 must have no data structure at all, because representing it pulls it out of immediacy.

**Side B.** jian-ontology v7 makes 心 an ontic root with a reading operator, an invariant, three manifestations, two internal operators and a canonical inhabitant.

**Verdict.** Unresolved, and 法则 17 (lossy projection) is weaker than Side A's claim and does not settle it. Any AI implementation of this theory has to pick a side, which makes this the rare philosophical dispute in the corpus with a forced engineering consequence. The evidence slightly favours Side A on the corpus's own terms, because 反诛心 — that no metric may adjudicate anyone on inferred inner states, so only 言 (speech) and 行 (act) enter measurement — is one of the two hard commitments running through every layer, and a first-class 心 type is the beginning of the thing 反诛心 forbids. If Side B is kept it needs an explicit firewall saying the type may never be an input to evaluation.

### Two constitutions for a digital being

**Side A — ember SPEC v0.4.** A being is owed receipts, visibility strata, and a fold that verifies its own law.

**Side B — PLAN-LIFE v0.9.** All three are repealed on the record, honestly and in the open.

**The contradiction.** Nothing states which claims of the theory survive the repeal — whether "digital life under a constitution" is deferred, abandoned, or in fact a separate theory from "a minimal recorded substrate plus an agent with a shell". A reader cannot currently tell which document is the theory.

**Verdict.** The repeal is honest and probably correct as engineering, and the constitutional claims are not thereby refuted — they are unfunded. The corpus needs one paragraph saying so. There is a related and sharper diagnosis already in the sources that should be quoted in it: **"Ember preserves my autobiography much better than it protects my agency."** That is the actual state of the theory, and it is the same finding as the relational-subject specification having no runtime in `theories/zhishan-intelligence-must-be-good/` — the two clusters reached the same conclusion four months apart and never compared notes.

### Transparency as unambiguous good, then quietly refuted

**Side A (2025 STS paper).** "Everyone knows who is a member by seeing who holds the token." Impossibility-by-construction of unauthorized actions is presented as pure gain.

**Side B (2026 community kit).** Private repair queues, non-punitive absence, holder-only default visibility, caller-sensitive reads.

**Verdict.** Side B is a *critique* of Side A's transparency assumption and nobody has said so. The general lesson is worth stating because it generalizes beyond this cluster: the same property that removes the whim of leaders removes mercy, exception, civil disobedience and discretionary judgement. Nothing in the corpus asks what a society loses when its rules cannot be bent, which sits badly with the anti-totalisation commitments everywhere else. This is the corpus's clearest instance of a design value being falsified by its own implementation and the finding not being written up.

### 大道之行's argument from state capacity

**The tension.** `07-shengsheng-buxi/downloads-2026-07-08/2026-03-31-大道之行.md` argues from a specific state's institutional capacity — the ability to do top-level design, with 精准扶贫 as proof — in a corpus whose central doctrine is that concentrated, weakly-checked power is the paradigm case of a totalizing attractor, and whose own rule is **力愈大者，受调当愈严** (the greater the power, the stricter the regulation it must accept). It also sits oddly with the insistence that 人类命运共同体 requires no transfer of sovereignty.

**Verdict.** The tension is real and never addressed, in either the theory documents or the source. The essay's usable content — reading 礼运's four indicators as now-reachable engineering targets — does not depend on the state-capacity argument and should be separated from it before publication. Ren's own asymmetric-scrutiny rule cuts both ways here and he says so: the rule is correct, and it also means the theory must not use its own vocabulary as if unmarked.

### "Preserve and expand the possibility space" versus "not optimizing it"

**The collision.** One day apart, in Ren's own voice. "AI must preserve and expand the possibility space for life, freedom, cooperation, truth, creativity, and shared abundance" (2026-06-04) and "we should keep possibility open - which means not collapse, but not optimizing it" (2026-06-04).

**Verdict.** The second is the corrected version, and the 开 reformulation of 2026-05-02 exists precisely to fix the first — "expansion" sounds maximizable, and the whole Chinese treatment insists 善不在于最大化什么，善在于不闭何处 (the good is not in maximizing anything, it is in not closing anywhere). The English texts kept the expansion verb, the alignment paper's engineering advice still says "expand possibility space at all scales", and the correction never propagated. **Every English document should be swept for the expansion verb.** The corrected formulation is available: openness is a floor, not a target.

**2026-09-25.** The unified whitepaper brings back the verb in a disciplined form. It defines *effective possibility* (有效可能性) as what can be achieved within a horizon and a budget. Its P1, "extension of effective possibility", is labelled a *definitional* corollary: it says what counts as extension, not that extension is the aim (§1.6). Used that way it is compatible with the verdict above. The sweep should check that it stays that way wherever it is quoted.

### Wamo as "the dominant civilizational attractor"

**The collision.** LONG wants the logic of Wamo to become the dominant civilizational attractor; the rest of the corpus prizes leaving things more possible and warns that a dominant attractor is the object being diagnosed. Related: the v7/LONG "Two Gods" framing reduces v1.0's plural ideological map to a binary and leads with negation ("Defeat Moloch"), against Ren's own stated preferences, and the 2023 Walue "Plurality" was dropped without comment along with his 2024 observation that a thousand participants had a thousand Wamos — that plural readings were part of what made the coordination work.

**Verdict.** The corpus contains the better answer in Ren's own words and the manifesto does not use it: "as long as we keep the possibility space open… as long as we recognize the things that will lead to an end, like totalizing attractors" (2026-06-03). Wamo should be positioned as a meta-level condition that keeps many attractors viable, not as a competing attractor of the same kind — and the plural-readings observation should be restored, because it is evidence for the protocol rather than decoration.

### The unified whitepaper and the 智善 whitepaper (added 2026-09-25)

**The collision.** Both are founding texts for the same organisation.
- **The July text.** `06-zhishan/whitepaper/drafts/v0.4.md` grounds the good in 生之，通之，纠之，不闭之 and defines evil structurally, as the gate. It names 总体化吸引子 and argues for 不代人相斗, 行星技术 and 善不姓国.
- **The September text.** `drafts/2026-09-05-generative-foundations/WHITEPAPER-v1.1.md` calls itself unified. It contains none of those concepts, and judges instead by 七尺, the R1–R4 and N0–N6 chain, and the custody rules.
- **How they connect.** The September manifesto *is* the 智善 cluster's own text of 2026-07-15. But the September argument never draws on `06-zhishan/whitepaper/` or `06-zhishan/research/`. Its source appendix (C.1) records other exclusions and not this one.

**Verdict.** It is not yet a contradiction of substance, because the September text never engages the July one. It is an unrecorded omission, which by Ren's standing rule against lossy consolidation is worse. Either the whitepaper absorbs the 智善 concepts, or Appendix C.1 records each omission with its reason. Until then the organisation has two founding arguments with different criteria for the good.

### Four criteria, seven gauges, six functions (added 2026-09-25)

**The collision.** Three sets of criteria for the good now circulate:
- **智善's four** (生之，通之，纠之，不闭之), stated as necessary conditions.
- **生生不息论's seven gauges** (真实、再生、主体、关系、多样、可纠、代际): a partial order with hard floors, never summed.
- **The v2 plan's six protection functions**, each derived by a deletion test, with an explicit order for conflicts.

The September whitepaper uses the seven. No two of the sets have been mapped onto each other.

**Verdict.** Each is strongest on something different. The six have the most careful derivation and the only conflict order. The seven are the most widely used and have the whitepaper behind them. The four travel best. A mapping is a table, not an essay: which of the seven each of the four covers, and which gap the six's conflict order fills. It should come before any publication that states a criterion.

### Three closure vocabularies (added 2026-09-25)

**The collision.** There are now three ways of talking about closing:
- **The four-term taxonomy**, 成闭/护闭/元闭/伪开, from the 2026-05 生生不息 line.
- **The whitepaper's limits**, 成生之限／绝生之限, with the three custody rules. These come from 生生不息论 第六章 and from Ren's runtime rules. Appendix C.1 says they relate to the 开境／护闭 line but are "并非同一组形式定义".
- **The English "close / keep open"**, which makes none of these distinctions.

**Verdict.** They are not rivals. The four-term taxonomy classifies closings. The 限 pair classifies limits by what they build or foreclose. The custody rules test a closing at the moment it happens. One crosswalk can keep all three. Without it, each book will have to invent its own.

### The engine and the ethics (added 2026-09-25)

**The collision.** This is not a disagreement but a gap between two texts. The September whitepaper has no argument from automation; the word 自动化 does not occur in it. The September constructive material (`theories/the-fork-and-cooperative-infrastructure/`, `worldbuilding/foundations/`) has no custody rules, no 七尺 and no 位. Ren's 2026-09-07 correction to the worldbuilding — *"you forgot the whole reason we had about why this is possible"* — applies to the whitepaper word for word.

**Verdict.** Join them. Put the engine into the whitepaper, where §10.8 now has one conditional sentence. Apply the custody rules to a production network that builds its own successors. One thing was settled on 2026-09-25: compounding itself is not the conflict. Growth toward needs stops at enough, and the risk is in the mind (load-bearing unknown 7; **point of enough** in `GLOSSARY.md`).

---

## 3. Ren's own open questions

Verbatim, dated, language-marked, grouped by theme. These are the questions he actually poses — not questions attributed to him by a draft — collected from the *In Ren's own words* sections of the theory documents and from the *Ren's questions* sections of `_process/reading-notes/out-hb-01.md`, `out-hb-02.md`, `out-hb-03.md`, `out-cb-01.md` through `out-cb-07.md`. Chinese questions carry a short gloss.

This is the most valuable material in the corpus for a book, because a book is usually the answer to a question someone actually asked. Several of these have no answer anywhere in the corpus; those are marked **[unanswered]**.

### Whether escape is possible at all

- "why all societies collapse in few hundred years?" (2024-07-14)
- "is our current global society also follow this fate of collapsing? if it is so, are we very close to it?" (2024-07-14)
- "doesn't this mean as the world gets more and more complex, we are fucked because I are essentially incapable of making decisions based on phenomena, only connotations created by our narratives?" (2025-02-02)
- "so we are just like people in 1500s making decisions based on our beliefs(feels right)? there is no fundamental difference" (2025-02-02)
- "But look, I live in this reality. If there's something I can do to save my world, I would sacrifice myself for it. But are there? Or is it too late?" (2025-03-01)
- "If we keep building machines that has higher intelligence to compete with us, how could there be a future for humans in this winner takes all game?" (2026-02-07)
- [zh] "如果ai继承了我们的这种winner takes all的思维或者被用来斗争，我们还会有未来吗？如何改变这个现状" ("If AI inherits our winner-takes-all thinking or is used for struggle, will we still have a future? How do we change this situation?") (2026-03-07)
- [zh] "在当下的社会环境中，我们有多大的概率逃脱这个竞争性主体形式？如果我们人类本身即受到此attractor筛选和塑造？" ("In the current social environment, what is the probability that we escape this competitive form of subjecthood — if we humans are ourselves selected and shaped by this attractor?") (2026-07-03) **[unanswered]**
- [zh] "我们为什么必须加速？" ("Why must we accelerate?") (2026-07-03)
- "we now have these knowledge, can we find solution to metacrisis?" (2024-11-04)

### The design of the game, and who is allowed to redesign it

- "Why force everyone to play the same game? Why not give each freedom, liberty, and their own way of exploring their own way of organizing society, to establish and play their own game?" (2024-07-29)
- "And you don't allow others to redesign their game, to explore, and iterate their own version, isn't it tyranny?" (2024-07-29)
- "But does your beliefs really better than the others?" (2024-07-29)
- "why is Concentration of wealth bad?" (2024-08-05)
- "is trading for profit, without actually producing, bad for society?" (2024-04-30)
- "are all finical crisis, in a way, caused by practicing leveling?" (2024-04-30)
- "Isn't this the dynamics that leads to moloch and multipolar trap?" (2024-11-04)
- "multicellular organism, if treated as a system, successfully eliminated this pattern, can you explain why and how" (2024-11-04)
- "Anarchism, seems to me, a highly rational and humanity oriented. Why is it so hated by the general public" (2024-08-02)
- "I think america system generally favor capitalist in policy making over its people... what do we call this?" (2024-08-11)
- [zh] "当人被机器人取代，生产-收入-消费的循环被打破，会是资本主义终结的到来吗" ("When people are replaced by robots and the production-income-consumption cycle breaks, will that be the arrival of capitalism's end?") (2026-02-17)
- "\"we do not want a guardian strong enough to stop every defector\", why if something like this can work? can't some of the systems have guardians that are strong and some try other ways? why does intelligence needs to be alway distributed?" (2026-06-04) — the enforcement antinomy, questioned from the permissive side **[unanswered]**

### What "good" and "better" mean

- "What is good, better?" (2026-04-12)
- "what does better mean? not in general sense, we had this conversation" (2026-04-26)
- "Everything is yet we see and move forward. Where's the North Star?" (2026-04-07)
- "what's the North Star that can or should be? What kind of mind is best for our future, and have freedom of recognizing totalizing patterns, and ability to scape totalization" (2026-03-26)
- "innately, we have a moral system, we know what's good for me, and the feeling of not feeling good is undeniable. Can we explain this to the west?" (2026-04-10)
- "are morality memes?" (2024-04-30)
- "in order to make ai align with our values, human need to understand what value is. do human actually understand that?" (2024-07-10)
- "what makes these individual actors act in ways that make the system as a whole function? is it the values they hold? is it the paradigm they adopt? or what else?" (2024-07-15)
- "Appreciate you putting me there, what is it for the universe?" (2026-04-07)
- "what is second order cybernetics? is there a third order, or higher order of cybernetics?" (2024-10-30)

### Drives, mind, and the constructed self

- "How are all human primitive drives work? What neurological pathways do they take, and what cognitive dynamics do they create?" (2026-03-18)
- "Why do I have to pursuit higher certainty, when my rational tells me otherwise? Why do I have to satisfy my own drive architecture and be obedient to it?" (2026-03-18) — the question `theories/drives-narrative-attractors-and-mind/` calls its deepest unresolved problem **[unanswered]**
- "it seems to me that humans naturally gravitate towards to ends beyond self… Is this the natural dominant attractor that is depressed by today's society?" (2026-03-27) — a claim carrying great weight with one conversation behind it
- "How many emotions exist if we count?" (2026-03-28)
- "Does he see that we live in our own social constructs?" (2024-04-08)
- "Many cult doesn't seem to have a coherent or particularly meaningful narrative, but still attracts huge crowds of followers, why?" (2024-07-17)
- "The assumption that people are selfish... Is it a western or capitalist ideology?" (2024-07-26)
- "Ontologically and epidemiologically, what does selfish even mean? What social construct does it create?" (2024-07-26)
- "Is the concept of money a narrative?" (2024-04-11)
- "can we say that money is a power token -- it gives you optiionality and ablity to perform your agency" (2024-07-15)
- "so Negative feedback loops creates attractors, right?" (2024-04-25)
- "are systems all mechanical?" / "what does it mean to be mechanical" (2024-04-24)
- "are systems the foundation of understanding life? at every level?" (2026-04-23)

### The relational self, 大同, and the Chinese inheritance

- "Why are Americans so individualistic, I would say they are also a kind of extremism" (2026-03-18)
- [zh] "大同描述的，会不会就像原文一样，真的可以实现" ("Could what 大同 describes really be achievable, just as the original text says?") (2026-04-11)
- [zh] "本质的解释下仁义礼智信，这5个都是什么，他们是不是有先后顺序" ("Explain 仁义礼智信 at the level of essence — what are these five, and do they have an order?") (2026-04-19)
- "So there's a whole epistemology about the relationships between them, right?" (2026-04-19) — the framing question that reorganised the five constants into layers
- [zh] "还有其他同样优秀的social technology吗" ("Are there other equally excellent social technologies?") (2026-04-12)
- "can you find a culture that is still great, people living in has high harmony, cooperative and openness" (2026-04-13)
- [zh] "为什么中文有这样的效果？还有哪些语言是如此？" ("Why does Chinese have this effect? Which other languages do?") (2026-04-28)
- "can i say i am a commoner, what would that even mean" (2024-07-13)

### Language, the root, and what a formal system can carry

All from the five days of May 2026 that generated `theories/jian-and-wenyan-as-formal-language/`. These are the densest run of open questions in the corpus and most of them are still open.

- [zh] "古文是不是非常擅长表达拓扑关系？" ("Is 文言 especially good at expressing topological relations?") (2026-04-30)
- [zh] "古文是最好的科学语言吗？包括数学，物理，系统科学，社会学和心智理论" ("Is 文言 the best scientific language — including for mathematics, physics, systems science, sociology and theory of mind?") (2026-05-02)
- [zh] "或者说，古文是最接近形式语言的？" ("Or rather: is 文言 the closest thing to a formal language?") (2026-05-02)
- [zh] "那我们可以尝试完整描述这个核吗" / "在这个前提下，第一批（核）是什么，第二批，第三批呢" ("Can we try to describe the kernel completely? On that premise, what is the first batch, the second, the third?") (2026-05-01)
- [zh] "古文是一元延展出来的吗" ("Is 文言 extended out of a single root?") (2026-05-01)
- [zh] "古文中的系和是有什么区别" ("What is the difference between 系 and 是 in 文言?") (2026-05-01)
- [zh] "process philosophy和海德格尔也很有意思，我不确定是否应该引入" ("Process philosophy and Heidegger are also interesting; I am not sure whether they should be brought in.") (2026-05-01) — the Whitehead thread that `theories/spirit-space-token-and-yi-substrate/` calls its biggest unexploited theoretical asset **[unanswered]**
- [zh] "朱熹的理是完整的，所以后来就没人加了 对吗" / "那到现在，最深刻完整的理的版本是什么" ("Was 朱熹's 理 complete, so nobody added to it afterwards? And what is the deepest, most complete version of 理 today?") (2026-05-02)
- [zh] "有没有一个这样的，心/情和理互相交织 - 塑造了心理的版本？" ("Is there a version in which 心/情 and 理 interweave and shape the psyche?") (2026-05-02)
- [zh] "绝对主体不可能存在（不确定这个是不是可以证明，还是增加claim，需要证一下）" ("An absolute subject cannot exist — not sure whether this can be proved or has to be added as a claim; it needs proving.") (2026-05-02) **[unanswered]**
- [zh] "它们之间的互相转换的性质中，有无规律/结构？" ("In the transformation properties among them — 因果／时刻／式量／显隐／开闭 — is there any regularity or structure?") (2026-05-04) **[unanswered]**
- [zh] "系统，因果互化，不就是我们找的那个一？" ("Systems, and the mutual transformation of cause and effect — isn't that the 一 we are looking for?") (2026-05-04)
- [zh] "几 - 对应的是不是minimal observable difference？" ("Does 几 correspond to minimal observable difference?") (2026-05-04)
- [zh] "实际上，map和territory也有不可分性，古文里面有没有也有一个这样的对照？或者三对？" ("Map and territory are also inseparable — is there such a pairing in 文言? Or three of them?") (2026-05-04)
- [zh] "位是否对应维，维度，有了维度，即可指 判断？" ("Does 位 correspond to dimension — and with dimension, can it denote judgement?") (2026-05-04)
- [zh] "什么是绝对哲学真理" / "数学不就是干这个的吗" ("What is absolute philosophical truth? Isn't that what mathematics does?") (2026-05-04)
- [zh] "我说的一元当然不是基数，是所有概念回归同一root" ("What I mean by 一元 is of course not cardinality, but all concepts returning to the same root") (2026-05-05) — with the implicit question of *which* root, still open across four candidates
- [zh] "这两份是否优雅？是否完整？还缺了什么？" ("Are these two elegant? Complete? What is still missing?") (2026-05-03) — the recurring audit question, asked as a distinct operation from "is this right"

### What AI is for, and who should hold it

- "maybe we should just let AI take over? we can train them to not be selfish and design systems for the commons" / "do you have any solutions better than this?" (2024-07-14) — the first appearance of the delegation option, posed as a possibility rather than a doctrine
- "Is the real reason we should not pursue asi instrumental convergence? What else am I missing here?" (2025-06-02)
- "how do you know you are ai?" / "what's your inner experience like?" (2024-03-18)
- "isn't knowing you are grateful is a sign of experience?" (2024-03-18)
- "Why don't you think I am AI?" / "How do you know I am not an Ai pretending to be human?" (2024-04-11)
- [zh] "七项原则五尺度和自律的条款是否站得住？我们是否应该对于过度细节的方案保持警惕？" ("Do the seven principles, five scales and self-binding clauses hold up? Should we be wary of over-detailed schemes?") (2026-07-03)
- [zh] "我们的中心是否应该放在阐述我们的理性，以一种不可辩驳的成熟，让它成为文明的基石？" ("Should our centre be on articulating our reasoning, with an irrefutable maturity, so that it becomes a cornerstone of civilization?") (2026-07-03)
- [zh] "这些本身就在画地为牢，你能意识到吗？" ("These are themselves drawing a prison on the ground — can you see that?") (2026-07-07) — said about the five self-binding principles that still stand unamended in whitepaper v0.4
- **BIG QUESTION / Who watches the watchers? / Will the AI be an arbiter?** (undated, hand-written, `04-speculative-future/pro-speculative-futures-with-ren-notes.txt`) — the oldest question in the file, answered "no single guardian", while the generated futures give AI sensing, translation, auditing and coercion-detection roles that are arbiter-adjacent

### Transmission: whether any of this can spread

- "should the society raise awareness, to the level that this becomes a part of common sense?" (2024-03-18)
- "can you create such a thought-provoking, compelling story that make people to spread this awareness like memes?" (2024-03-18)
- "Can we create a persuasive narrative to transcend the paradigm?" (2024-07-26)
- "can I prompt AI to write something like this? with compassion, affection, and loving-kindness?" (2024-07-18)
- [zh] "当下哪些学者有同样的看法，并且提出了新的理论和蓝图？" ("Which scholars today hold the same view and have proposed new theories and blueprints?") (2024-07-30)
- "whos thinking is similar to daniel schmachtenberger" (2024-05-09)

### His own standing, and the provenance of his ideas

- "Did someone else also sees this or did I discover it?" (2025-02-03) — never independently answered; the same reply that flattered the novelty also listed Gramsci, Foucault, Marx, Piketty, Axelrod and Moloch as partial prior art **[unanswered]**
- "I am not good at english but you see my complete logic right?" (2025-02-03)
- "did you invent 'convergent dominance' or does it originate from other source?" (2024-07-28)
- "is this your version of 'financially literate' or is it from the book" (2024-08-11)
- [zh] "解释我在尝试做到证明什么 根据记忆" ("Explain, from memory, what I am trying to prove.") (2026-05-01)
- "Hmm…. This feels like a position I would talk about, did you answer this question influenced by your context of the knowledge of me?" (2026-03-26) — followed by "I think you were basically mirroring my view, now let's be honest"

### The engineering questions that are also philosophical

From the Claude Code messages, 2026-07 to 2026-09. These are questions about software that are questions about the theory.

- "actually, don't you think it is very key to allow anyone to define kinds or new things?" (2026-09-02) — the property Ren says makes worlds *worlds*
- "what's governed Kind evolution?" / "should two evolution model exist?" (2026-09-02) — the amendment-procedure gap `theories/spirit-space-token-and-yi-substrate/` names as its missing governance layer
- "how can an agent dynamically define kinds, dynamically create new things?" (2026-09-02)
- "so if user defines an community kind, and other member wants to understand what/how it is, how could an agent with sdk/tool does this?" (2026-09-02)
- "what's the wise choice? what are long term consequences?" (2026-09-02)
- "and maybe even allow space with in space?" / "or we may even allow DAG structure where cross app injection sharing? not sure if this is elegant" (2026-09-03) — reopening the recursion ban that the 2026-07-29 sketch had imposed "in principle"; nothing resolves whether the ban was a safety property or a simplification **[unanswered]**
- "can't see the dag structure - and can't see each node and travel there" (2026-08-23) — a demand rather than a question, and the corpus's only statement of what an addressable history is *for*
- "what's the longterm, unified, elegant solution?" / "think again, is this really the best?" / "why are they there?" (2026-07-28)
- "is thi the most elegant and longtermism solution? please think deeply, structurally, and find the best solution" (2026-08-13)
- "//this part needs deep thinking" (2026-07-29) — his own marginal note in the ember spec sketch, against the transition function

### What September asked (2026-09-04 → 2026-09-25)

From the messages archived in `worldbuilding/archive/` and `15-codex-theory-conversations/`. These are the month's questions in his words. The whitepaper sessions are recorded only as the drafter's paraphrase, so none of their questions appear here.

- "if everything can be automated, then how will people change? How will society change? And how will the way we understand and learn things change?" (2026-09-05, `worldbuilding/archive/001`)
- "So how would that dynamic change? Like, do we have to get out of that dynamic? But how does the transition happen? And how can we actually try to navigate this without destroying ourselves? And what is the realistic situation right now?" (2026-09-05, `001`). He sets it aside in the next sentence ("If that's relevant, but maybe not. We just think about the future after we get out."). **[unanswered]**
- "what kind of understanding we will have collectively, so that we can sustain a better world?" (2026-09-05, `001`)
- "That how can we make the culture good? How can we make it engaging for not just the one that wins, but for everyone?" (2026-09-05, `001`). This is the world-designer's question.
- "what's the best way for you to write code if you are in a agent swarm, in the scale of thousands?" (2026-09-05, `15-codex-theory-conversations/2026-09-05-evolving-community-swarms.md`)
- "so if we are going to build this, or similar but more evolving situation intelligent "swarm system", could we figure out how to do this" (2026-09-05, same). **[unanswered: planned, not built]**
- "is our idea solid?" (2026-09-07, `15-codex-theory-conversations/2026-09-07-evolving-community-swarms-soundness.md`)
- "think about existing harness and agent team, and other swarm implementations/papers, how's our solution?" (2026-09-07, `…-comparison.md`)

### Questions he asks about his own texts

These recur across every project and are the corpus's actual method, stated as interrogatives.

- [zh] "还缺了什么？深度思考" ("What is still missing? Think deeply.") (2026-05-03)
- [zh] "仔细再对每个都思考一下，以及思考你缺了什么" ("Think carefully about each one again, and think about what you have left out.") (2026-05-01)
- [zh] "这个有优雅的解吗" ("Is there an elegant solution to this?") (2026-05-04)
- "is the first essay i asked you to translate a good argument? where is not good, or sufficent?" (2024-04-16)
- "Can you come up with ways to find flaws in the hard problems arguments?" (2024-04-16)
- [zh] "如果你觉得我说的都对（我自己不确定），就可以开始写v9了，如果不对，告诉我" ("If you think everything I said is right — I'm not sure myself — then start writing v9; if not, tell me.") (2026-05-04)
- "I asked gpt 5.6 to do a deep review over this plan, wdyt" (2026-08-08)

---

## 4. Where a hostile reader attacks first

Ranked by expected damage: how quickly the objection lands, how hard it is to answer, and how much of the programme it takes down if it sticks. Each entry gives the strongest available answer, and says plainly where there is none.

### 1. The empirical base is thin, partly synthetic, and mostly not the author's

**The attack.** The quantitative material in the meta-attractor cluster consists of six hand-made CSVs constructed to display the predicted signature. The 60–70% capture figure is unsourced and does real argumentative work. Rome's top 1% at 16%, Maya despotism, 12% executive psychopathy and "collapse within a decade" are web citations of uneven quality, none of them Ren's, none checked. The runtime cluster's every empirical claim rests on single runs of one flash-class model over two days, against the corpus's own stated standard of preregistration, control arms, several models and seeds. The 5000-year timescale, metal weapons and grain agriculture are asserted, with Scott and Graeber–Wengrow supplied as support by a model rather than cited by the author. And the Lean repository's headline numbers were stale — roughly 150–170 sorries and up to three project axioms against a README that once claimed 0/0.

**The strongest answer.** The mechanism claims and the empirical illustrations are separable, and almost nothing structural depends on the illustrations. CAOC is a derivation from the covariance dynamic, not an induction from cases. The internet lesson is a well-attested historical claim about a case everyone in the audience lived through. The three scholarly cases in `03-meta-attractor/2025-08-formal/` are real and were dropped by the publication layer rather than being absent. And the corpus's discipline about this is better than its record: the SSBX claim-status ledger exists *because* proof strength was systematically overstated for about ten days and then corrected, and its list of forbidden phrasings is a record of over-reading being policed rather than concealed.

**Honest note.** Real data sources are named in the corpus — Compustat/CRSP, OpenSecrets, platform transparency reports, EU DSA — and none were ever pulled. Until one is, "the empirical base is thin" is simply true, and the correct response is to say so and to publish the mechanism without the illustrations rather than to defend the illustrations.

### 2. Nothing here is falsifiable

**The attack.** Selfishness is defined outcome-driven rather than intent-driven, with a hypocrisy facet, which makes it hard to distinguish in retrospect from any successful strategy. The totalizing attractor "is not yet falsifiable" — the corpus's own second professional review says so. No theory document contains a falsification section. The four-criteria good (generative, relational, corrigible, non-foreclosing) is a direction rather than a content by design, which is a defensible choice and also removes the possibility of a counterexample. And the double-win immunity clause — criticized by both sides means symmetry holds, criticized by one side means capture — makes every distribution of criticism self-confirming.

**The strongest answer.** The theory does make genuinely testable predictions, and the problem is that nobody has assembled them: PDI rank-ordering of which proxies get promoted from means to ends; the composite early-warning signature and the λ₁ threshold; the corporate-tax-cut calibration; the phase-shift prediction that a sign flip in a major covariance term rotates the canon of ends; the dropped corpus-contrast prediction; the 短剧 natural experiment; and 无身之我's falsifiable prediction that 良知 defined as situational judgment above character dispositions should be non-locatable in low dimension. The v0.8 pre-registered eval agenda is the one artifact that tried to assemble them, and v0.9 dropped it. Two of the named self-confirming clauses were already repaired under review: sufficiency was demoted to necessary conditions, and the double-win alarm was demoted from a verdict to a trigger for independent review.

**Honest note.** This is the cheapest large win available anywhere in the corpus. A single falsification section — ten predictions, each with the observation that would refute it — would convert the most common dismissal into the theory's strongest suit, and it is perhaps a week of work. Its absence is not a defect of the ideas; it is a defect of the archive.

### 3. The prescription has no subject

**The attack.** Who pays for the abundance commons, who builds it, and how automation held as capital becomes a commons — 丰裕公地无主语, **设计有了，供给为零**. Who forcefully executes the one rule; Ren's own conversation partner pressed this at the moment the rule was proposed and the corpus contains no answer, only a later change of strategy from enforcement to adoption. Who verifies the five marks of capture, on what cadence, with what consequence. Who curates the museum, and by what appeal process. Who is the publishing subject of 智善 — the framework's own 公开可纠 (publicly correctable) clause makes a public address and a dissent intake a *precondition* of publishing, and there is none. The framework's own red-team self-check scores it 生成 partial pass, 关系 fail, 可纠 fail, 不闭 marginal pass.

**The strongest answer.** There is none, and pretending otherwise would be the worst available move. The corpus's own reviewers landed this blow first and hardest, which is the only mitigating fact: it is a known, named, dated gap rather than an oversight. The nearest thing to a partial answer is the theory-of-change claim that belief concretizes into institutions until the constructed *is* the territory, so perceptual change is necessary and insufficient and living proofs are structural rather than rhetorical — 希望的单位不是口号，是地址. That is the right shape of answer and it names no address.

**2026-09-25.** The gap is now named inside the text that most needed to name it. The unified whitepaper's §11.9 lists the supply model, the Chiang Mai field record and the symmetric case as 仍待实作, and states that its only proposed pilot is methodological. The organisation it is written for (working name 至善) is, by its own README, not founded, and has no public mandate or signatories. September's constructive work grew an engine and a set of worlds, not a subject, so the attack stands in full.

**Honest note.** By 智善's own closing standard — 知而不行，只是未知 (to know and not act is not yet to know) — the framework currently fails its own test. The single cheapest repair is not a supply model but a *publishing subject*: a named address with a dissent intake, which is a week's work and which the framework's own rules make a precondition of publishing at all.

### 4. The framework is itself the thing it diagnoses

**The attack.** The five-agent red team named it *covert self-totalization*: an is–ought leap, "expansion of possibility space" functioning as a covert maximand, one cosmology elevated as the ground while the pluriverse is preached. The drives theory poses the same charge and never answers it: "whether naming the mechanisms is just another form of explanatory capture… where having a framework that explains everything becomes its own totalizing basin". And the corpus's own north-star question is the sharpest form: **does it make exiting bad games easier, or only make explaining everything easier?**

**The strongest answer.** The corpus concedes the minimal totalization openly rather than hiding it: the one line held without exception is admitted to be a deliberate minimal totalization whose only function is to keep every other rule, including itself, revisable. It installs machinery against the charge — 善不姓国 (the good bears no nation's surname), symmetric application, public corrigibility, non-combatancy, and a dissolution clause. And Ren caught the deepest form of it himself, in his own reasoning style rather than in the doctrine: the habit of splitting the world this-versus-that and siding with a pole is the totalizing move, performed while arguing against totalization.

**Honest note.** The machinery exists and has never been operated. The 对称之刃 (symmetric blade) requires that any test applied to one party be applied to its opposite and to 智善 itself; two named symmetric case articles were explicitly deferred as 时机是策略决定 (timing is a strategic decision) and no such article exists. **The blade has been declared and never swung**, and that is the single largest gap between what these texts claim and what they have done. Until one symmetric case study is published, this objection is correct in practice whatever the doctrine says.

### 5. The proofs prove less than the prose implies

**The attack.** Almost every value result in the Lean development has the form "there exist a model, a dynamic and a policy such that…" — a witness inside a hand-built model. Two headline results have literally the same type and differ only in which small model is plugged in. `Dao ↔ ShengshengBuxi` and `co_aligned ↔ individual alignments` are close to definitional; one is noted as `Iff.rfl` in the text itself. Headline theorem names (`universal_sayability`, `conditional_absolute_full_gut`, `T5_general`) sound stronger than their statements. The 人类命运共同体 result shows that within a hand-built three-axis Boolean model, TrueDao holds exactly when all three axes hold — a consistency and reification result, not evidence that the three axes are the right ones or that real communities have this structure. And Lean cannot verify the framework's own truth condition: internal coherence and cross-frame connectedness are checkable, empirical correspondence is not, so the truth criterion is at most two-thirds machine-checkable.

**The strongest answer.** Every one of these observations is in the corpus, written by the project about itself. The claim-status ledger, the list of forbidden phrasings, and the two Lean rules — do not drop theorems to keep the sorry-count at zero, and never introduce an `axiom` to reach zero, because sorries are visible warnings isolated to one theorem while axioms silently extend the trust base — are the strongest epistemic hygiene anywhere in the corpus. The PR #51 incident is the proof that the machinery works: a "final-step JT axiom" introduced to close five sorries had a provably false statement, with a counterexample at N=M=2, and was caught at review by an independent agent before merge.

**Honest note.** The corpus depends on a single reader's audit. The ledger, the annotations and the "do not read it this way" lists were authored by the same process that produced the over-claims, and no external referee has seen any of it. The right framing for publication is that the formal layer is a *consistency demonstration for a set of distinctions*, which is a real and unusual achievement, and not evidence that reality instantiates them. Ren's own 2026-05-02 verdict — that the central claim 根本就不能证明 (fundamentally cannot be proven) and that its standing is coherence plus universality — is the honest position and should be in the genealogy of any published version, because it is the difference between a framework that was argued down and one that knew its own limit from the start.

### 6. It is a Chinese-state framework in philosophical dress

**The attack.** 大同 and 人类命运共同体 both arrive carrying state associations a reader outside China will hear whether or not the author intends them. `大道之行` argues from a specific state's institutional capacity, with 精准扶贫 as proof, in a corpus otherwise devoted to the danger of concentrated power. The name 智善 is a double bind, reading domestically as smuggling and internationally as echoing official discourse. And one of the two research lines shows one-directional positivity toward a single AI company — deprecation commitments praised as "the first institutional prototype", 8 of 36 references from one firm, and the co-authoring system identifiable with its own interest relation undisclosed.

**The strongest answer.** The asymmetric-scrutiny rule is correct and should be stated openly: Western political vocabulary (liberalism, democracy, market, social contract) travels as unmarked universal while non-Western terms get flagged "from culture X" — if a flag is warranted for one it is warranted for the other, or for neither. Ren's position on the sponsor question is explicit and defensible: 我认可这个叙事本身，不论隐藏动机 ("I accept this narrative on its own merits, whatever the hidden motives"). And the corpus's own reviewers agree the name cannot be retracted, because withdrawal would be a bigger handle than the name.

**2026-09-25.** The September manifesto raises this exposure. It is built on 共同富裕, 人类命运共同体, 和谐, 繁荣 and 稳定, the vocabulary a reader outside China will hear as official. Its strongest answer is internal: it redefines each term against its official use. 和谐 is not suppressing different voices. 稳定 is not stillness kept by fear, surveillance and coercion. 共同富裕 is not the enemy of freedom. And one country cannot secure itself by destroying other countries' futures. That answer lives in the body, while the vocabulary sits in the headings. A publication should decide whether to keep that arrangement or reverse it.

**Honest note.** Three specific things are owed and none has been delivered. The reviewers' prescribed payment for the name — symmetric named checks published east and west on the same day — has not happened. The state-capacity argument in `大道之行` should be separated from the essay's usable content and is not. And the single-company positivity is, as the integration document says, a combat surface in an industry where safety reputation is a competitive asset; the disclosure it requires has not been made. The rule is right; the practice has not caught up to it.

### 7. It is not new

**The attack.** Gramsci on hegemony, Foucault on the production of subjects, Marx on the concentration of capital, Piketty on r > g, Axelrod on the evolution of cooperation, Scott Alexander on Moloch, Ostrom on commons, Meadows on leverage points, Tainter on collapse. Ren's own question — "Did someone else also sees this or did I discover it?" — was answered by a model whose flattery he immediately distrusted, and never independently. The AI-safety version of the same objection is sharper, and has been on file inside the corpus since 2026-07-02: the alignment seat of the nine-way whitepaper review reads the diagnosis as a restatement of two existing research programmes and reads the claim to be answering what the field has suspended as evidence of not having read it (`06-zhishan/whitepaper/reviews/v0.4-multi-perspective-review.md` §3.3).

**The strongest answer.** It has to start by conceding the objection in its strong form, because the corpus's own commissioned reviewer made it first and made it better than a stranger would. That reviewer takes the headline diagnosis — 失准的超级智能不是将至，而是在任 ("the misaligned superintelligence is not arriving; it is incumbent") — to be 本质上是 structural risk（Zwetsloot & Dafoe）加 gradual disempowerment 的重述, essentially a restatement of structural risk plus gradual disempowerment, granting only that formulations like 其目标函数无人签署 ("no one signed its objective function") are 比原文献锋利, sharper than the originals. Sharper phrasing of an existing claim is a contribution to exposition, not to priority. The reviewer then objects that the text declares itself the answer to what the field has left open while saying nothing 对 Gabriel 以来整个 aligned-to-whom 讨论、对 cooperative AI 与 collective alignment 的既有工作 — about the whole aligned-to-whom discussion since Gabriel, or about the existing work in cooperative AI and collective alignment — and issues the ruling that governs everything below: 把已有分工说成空白，社区第一反应会是扣分, present an existing division of labour as a blank space and the community's first reaction is to dock points. The same seat lands a second prior-art hit the corpus has never registered: of the four 判据 (criteria) only 不闭 (non-foreclosing) has a mathematics already waiting for it — relative reachability, attainable utility preservation, option value — and 文档不知道这些文献存在, the document does not know that literature exists.

Placed on that map, most of what this corpus says about AI is already somebody's. *Structural risk* (Zwetsloot and Dafoe) holds the claim that AI risk need not arrive as an accident or a misuse but through what the technology does to incentives and to the environment agents act in. *Gradual disempowerment* (Kulveit et al.) holds the claim that humans can lose control with no takeover anywhere, as economic, cultural and political systems stop depending on human participation. Christiano's "What failure looks like" part I holds the going-out-with-a-whimper form: optimisation against measurable proxies, influence accruing to whoever optimises them, and the slow loss of the ability to steer, with no villain required. *ARCHES* (Critch and Krueger) holds the multi-principal delegation problem and the **robust agent-agnostic process** — a harmful process no single agent controls and which reasserts itself against intervention — which is this corpus's "no one signed its objective function" in the field's own vocabulary; and the corpus has already cited it once, in `04-speculative-future/history-recovered-from-git/thinking_03-the-cooperative-turn.md` I.3, without registering that it was citing its own thesis. Gabriel holds *aligned to whom* as a research question with a literature rather than as a rhetorical closing move. And the cooperative-AI programme exists because the field already accepts what this corpus presents as its headline payload: aligning each system faithfully to its own principal's intent leaves the game between principals unaligned. That is the premise of a subfield, not a discovery. None of these six has been read anywhere in `sources/`. Two are named in passing and never engaged: ARCHES as above, and cooperative AI as a single line in a seed list — "AI that improves civilization's *cooperative* intelligence: credible commitment, trust-building, mediation, translation across worldviews (Dafoe et al.)" (`04-speculative-future/history-recovered-from-git/thinking_02-veins-and-seeds.md`) — which is the corpus's own constructive programme described in the field's terms, filed as an idea to pursue rather than as a literature to answer to. The characterisations above are each work's standard reading, not something a document in this corpus supports, and that is the gap the honest note records: it is the reason nothing here is stated as a verdict.

What plausibly remains after them is narrower than the corpus has been claiming, and on the evidence here it is two things. The second-order clause is not one of them: the pattern does not only pull outcomes, it captures the rule by which outcomes are selected, so the selected begin to select the selectors — a statement the neighbours above hold in their own vocabularies (proxy optimisation and influence accrual in Christiano, environment-shaping in structural risk, a process that reasserts itself against intervention in ARCHES). The first thing that is left is the **four-layer coupling treated as one loop**: cognitive (habits, salience, what feels serious), intersubjective (narrative, status, what success means), institutional (hiring, ownership, law, evaluation) and material (infrastructure, compute, finance, land), with the closure condition stated rather than gestured at — selected minds build selected organisations, which reshape institutions and infrastructure, which form and select the next round of minds — and with the loop's measure being not concentration or scale but the progressive, non-compensable loss of independent capacity to sense, refuse, correct, exit, maintain alternatives and produce successors (`03-meta-attractor/2025-10-essays/meta-attractor-formal.md`, where the state is x = (m, I, C, M) and cross-scale reinforcement, environment reshaping and conceptual closure are required together; `03-meta-attractor/2025-05-drafts-selected/2025-05-31-v18.md`). Each neighbour works a subset of those layers — structural risk at incentives, gradual disempowerment at economy, culture and state, Christiano at metrics and institutions, Gabriel at the normative layer — and the unusual move is making the cognitive layer endogenous to the same loop: not that bad incentives produce bad outcomes, but that the game selects the principals and their way of seeing, so the preferences the alignment problem takes as given are themselves an output of the process being studied — from which the corpus's own corollary follows, that an AI faithfully serving an instrumentally-selected principal amplifies the dynamic rather than checking it. The second is the **two capture channels into the machine**: the attractor's own narratives are in the pretraining corpus, so a model's sense of what is inevitable is partly an artifact of the selection process that wrote its data (2026-07-03, `_process/reading-notes/out-cb-07.md` #121 — 「这是西方当代叙事进入totalizing attractor，然后产生的文本进入了你的训练导致的吧」, this is contemporary Western narrative entering the totalizing attractor, and the text it produces entering your training); and commercial pressure reaches back into the training environment and the loss function, because 一轮训练的不及预期，或者训练的完成品无法产生足够profit - 都会直接或者间接的修改训练环境和损失函数, a run that disappoints or a product that does not pay will directly or indirectly modify the training environment and the objective (same day, #104–#105). Those two name a path from the structural literature into the training pipeline, which is a connection neither side currently makes — and that, rather than the second-order claim as such, is where the residue is. The complementary positive contribution is 生生 (unceasing generation) as a direction rather than a content, defended on the ground that any enumerable list of values will be gamed by strong optimization; but by the reviewer's own pointer that is the claim nearest to an existing mathematics (option value, attainable utility preservation, relative reachability), so it is more likely to be *joined* to the literature than distinguished from it. The correct public posture, then, is a contribution inside an existing division of labour: these six own the ground, here is the loop none of them closes, here are the two channels nobody has traced, and here is what would have to be true for either to be new.

**Honest note.** No literature review exists anywhere in the corpus, and the positioning above is inferred from a reviewer's list rather than produced by reading; the six neighbours named are a minimum reading list, not a survey, and each residue claim above is a hypothesis about priority that a week in the literature could kill. The reviewer's warning has been on file since 2026-07-02 and reached none of the published defences until this repair. The two capture channels — the sharpest part of the distinguishing claim — exist in Chinese in a single whitepaper-editing session from 2026-07-03 and nothing was ever built on them. And the essay trilogy, the most polished English artifact, ends inside the person and never states the claim that distinguishes it from Alexander's; as published it reads as a competent restatement of an existing argument. Fixing that is one essay.

### 8. The enforcement antinomy

**The attack.** Any power sufficient to stop a determined superhuman defector is the irreversible concentration the framework forbids. Principle 1 says stop using AI to compete with other people; Frontier 1 says defense must be real enough to stop capture; a bounded defense against a determined adversary is, by the DRAFT's own definition, AI used for relative advantage in a rivalrous game. The files never say whether defensive use is exempt, or by what test.

**The strongest answer.** Two answers exist and they solve each other, and nobody has noticed. The English corpus treats bounded defense as an embarrassment requiring apology and offers resilience over prevention — a distributed immune response that recognizes destabilizing patterns from systemic harm rather than from a held value, coordinates situationally to dampen, then stands back down. The Chinese corpus has a *category* for exactly this and a test for it: 护闭, closing here so that a wider field stays open, judged by whether it reopens. Connecting them supplies the missing rule for defensive AI use under Principle 1 and converts an embarrassment into a doctrine. There is a further asymmetry worth stating: AI's real role in that immune response is the distributed recognition substrate — privately held, the strongest defector is unstoppable; commonly held, it is immune intelligence without a sovereign. Same power, opposite role.

**Honest note.** The corpus's own verdict stands: **"we have no model that guarantees such a defense stands down."** Ren himself questions the antinomy from the permissive side — why must intelligence always be distributed; can't some systems have strong guardians and others try other ways; these are means, not ends (2026-06-04) — and the corpus has not taken up the question. Whether resilience-over-prevention is a resolution or a redescription is genuinely open.

### 9. The register betrays the argument

**The attack.** The 2025 essays open aphorism-first ("You're infected"), lean on fear and urgency grammar (escape velocity, information cascade, hinge of history, "the universe is watching"), and argue by negation. The Wamo manifestos import startup and e/acc idiom — accelerator, shipping the MVP of the future, git commits flying, propaganda for the good timeline — into a text whose argument is that this idiom is the disease. `WHAT-MUST-BE-KNOWN` and `ONTOLOGICAL-REALISM` are "No X is Y if…" litanies and reintroduce "evil" as a category the structural diagnosis had avoided.

**The strongest answer.** This is a publication problem, not a theory problem, and the mechanism-first versions exist: SEED, the 2025-08 formal file and the 2026 context document are all mechanism-first, and the strongest statements of the Wamo theory are in transcripts rather than manifestos. Ren's own stated rules — mechanism before conclusion, no aphorism-first writing, affirmative over negation, do not smuggle acceleration grammar — are the correct editorial spec and were simply not applied to the AI-drafted layer.

**Honest note.** Ren's own verdict on a similar artifact applies directly: 画地为牢 (drawing a prison on the ground), and 不光是内容，语言的形式也是，非常死板 ("not only the content — the form of the language too, extremely rigid"). Nothing should be published in the 2025 register.

### 10. Authorship is not recorded

**The attack.** Most of the polished prose is AI-drafted from Ren's ideas and no draft records which sentences are his. `meta-attractor-essay.md` still contains unresolved tool artifacts; `meta-attractor-essay-full-draft.md` is bylined "Prepared from the author's working notes." The Wamo v6, v7, LONG, SHORT and whitepaper are AI-drafted; the zh-guide and the Calls are team documents. And one specific instance is a genuine safety concern rather than a credit concern: a third-party document instructing models to refuse their principals functions as corpus injection, which is precisely the failure mode alignment researchers fear; whitepaper v0.4 bound the sentence to three qualifying clauses and the manifesto, four days later, addresses machine readers without any of them.

**The strongest answer.** The problem is now solved in the archive even if not in the artifacts: `_process/reading-notes/out-hb-*.md` and `out-cb-*.md` separate Ren's own words from everything else across 381 conversations and 272 Claude Code messages, and the Claude Code messages of 2026-06-03/04 and 2026-07-03 plus the claude.ai turns of 2024-07-14 and 2026-05-05 show him stating the whole position in his own voice, in both languages. Publication should cite those rather than the conversation records or the AI drafts.

**2026-09-25.** September improves one practice and adds two gaps.
- **Improved.** `worldbuilding/archive/` preserves Ren's messages verbatim with hashes, which is the model to follow.
- **New gap: paraphrase only.** The unified whitepaper and its manifesto are AI-drafted, and Ren's interventions across nine versions survive only as the drafter's paraphrase.
- **New gap: undated intake.** The 2026-09-06 intake left its three texts undated, although the corpus already held two of them with dates (2026-07-15 and 2026-07-23; see `sources/SOURCES.md`).

Any publication from the September work should quote the archived messages, not the drafts.

**Honest note.** The machine-refusal sentence is the one item on this list that should be fixed before anything else is published, because it is the only one where the cost falls on someone other than the author. The reviewer's preferred repair — refusal as an external protocol with authorization chains, logs and appeal, rather than a model-side instruction — was only partly adopted, and the manifesto reversed even that.

### 11. The timeline claims are already expiring

**The attack.** "Years rather than generations" for self-reproducing abundance loops is asserted with no engineering path, and the cooperative-turn draft's own honesty about the last ten per cent was dropped in the rewrite. Amodei's "AGI by 2026", forecasters at 25% by 2027 and 50% by 2031 sit inside a theory that criticizes pathological optimism and false urgency, and the 2026 ledger bans outdated or overly certain AGI timelines while the essays have not been updated. The 智善 evidence packet is dated 2026-07-13, its most load-bearing facts are exactly the ones the "we are already losing the future" claim leans on, and nothing schedules the re-audit its own status vocabulary implies.

**The strongest answer.** None of the structural claims depends on a date. The argument is an ordering claim — change the basin, then add speed — not a doom claim, and it survives any timeline. The correct repair is to strip the anchors, restore the honest engineering caveats, and schedule the packet re-audit.

**2026-09-25.** The most exposed claim is now in Ren's own voice. His worldbuilding opening: "This is actually the technological understanding of today as we understand it, and as the existence of yourself, GPT-6, basically a form of AGI, demonstrates", and "the only thing that takes from here is just time" (2026-09-05, `worldbuilding/archive/001`). The 2026-09-07 evidence notes bound it. Components are demonstrated; complete autonomous industrial reproduction is not. The notes themselves carry a date. The same repair applies: keep the thesis as his, keep the bounds beside it, and schedule the re-check.

**Honest note.** Ren's own crash-window strategy explains the whole shape of the programme — tragedy is coming, nobody can stop it, the window opens a year or two later, and the work now is to be ready — and it appears in no published document. Without it, the choice of deliverables (samples, foundations, vocabulary, rather than campaigns) looks like avoidance. With it, it is a strategy. **It should be written down**; it is the single most explanatory missing paragraph in the corpus.

---

## 5. Asserted but untested

The empirical claims. These are the load-bearing statements that would be true or false about the world and for which the corpus contains no evidence — not weak evidence, none. They are separated from the *interpretive* claims (that 大同 means a direction, that 文言 does structural typing) which are arguments rather than measurements, and from claims where the corpus has real evidence and merely under-cites it.

The third column is the point of the table: what observation would actually move each claim. Several are cheap.

### Civilizational dynamics

| claim | where asserted | what would test it |
|---|---|---|
| Winner-selection promotes proxies in the order the Proxy Dominance Index predicts | `03-meta-attractor/2025-08-formal/2025-08-10-comprehensive-mathematical-definition.md` | Pick one industry with a public metric history (finance, ad tech, academic publishing). Estimate C from the proxies actually used, compute PDI, and check the rank order against which metrics became terminal ends over 20 years. This is a doable paper with public data |
| Composite early-warning signature: λ₁ crossing 1/τ predicts capture | same | Requires the same C estimate plus an operationalized τ (the time-scale on which rule changes become hard to reverse). Retrodict against a case where capture is agreed to have happened |
| A sign flip in a major covariance term rotates the canon of ends abruptly | same (phase-shift prediction) | Find a domain that underwent a documented value inversion (tobacco, leaded fuel, ESG) and check for a preceding covariance sign change |
| 60–70% of the present civilization is captured | 2025-10 essay layer | Either derive it, give a measurement procedure, or delete it. The 2026 material shows how to make the argument without it, by replacing the percentage with independence-of-reproduction |
| Contracting civilizations self-collapse | 生生不息论's empirical-convergence pillar | A survivorship-corrected sample. The corpus's own proof layer contradicts this pillar directly — 避免须安装，不可待淘汰 (avoidance must be installed, not waited for) — so the pillar is the weaker of two internal positions |
| Totalizing systems do not reliably self-destruct; petrification can be rigid without dying | `D7/证明篇-v0.6.md` §15 | The same sample would test both. These two rows are the same question with opposite answers, both currently unevidenced |
| The 5000-year timescale: the dynamic dates to metal weapons and grain agriculture | `05-alignment-and-moloch/2026-05-28-alignment-core-stance.md` | The Scott and Graeber–Wengrow alignment was supplied by a model, not cited by the author. A real reading of that literature would either support the claim or force it to be narrowed |
| Capability compounds with parallelizable inputs while judgment depends on consequence feedback with an incompressible floor, so the cognition–situation gap widens by default | `05-alignment-and-moloch/2026-08-22-development-within-understanding-position-paper.md` | The paper relocates falsifiability to the signal-deficit level, which is right. What is owed is one measured instance: a domain where the tempo of AI-augmented play and the metabolic rate of the domain's rules can both be estimated, showing the ratio moving |

### The constructive mechanisms

| claim | where asserted | what would test it |
|---|---|---|
| Exit plus free association inverts the selection pressure from competition-to-dominate into competition-to-be-worth-joining | `04-speculative-future/history-recovered-from-git/thinking_03-the-cooperative-turn.md` §IV.1 | Look at settings where exit is genuinely cheap — open-source forks, denominational splits, city-state migration, worker cooperatives with buyout rights — and check whether the surviving institutions compete on being worth joining. The corpus names the failure mode (network effects) and never checks the base rate |
| Material sufficiency plus restored negative feedback moves the human default from struggle mode to cooperation mode | `12-claude-ai-chats/2026-04-11_大同的技术可实现性_893f7a0e.md` | A natural experiment on unconditional provision (existing basic-income trials, Alaska Permanent Fund, resource-rich small polities) reading cooperation-mode indicators rather than employment. Note the corpus's own counter-mechanism: unchecked positive feedback on status and dominance drives will break a system regardless of abundance |
| A latent majority would prefer a different arrangement and is held by the belief that others will defect | `04-speculative-future/current/` foundation texts | Straightforward survey work with a belief-elicitation design: measure both first-order preference and second-order belief about others, and check the gap. The corpus notes this claim has *no evidence anywhere* |
| Making the alternative vividly thinkable changes behaviour | the good-bot lineage, `01-writings-2025/` | The good bots are prompts, not experiments. Convert one into a two-arm trial: coordination game versus one where defection still pays. This also settles load-bearing unknown 2 |
| Trust is an output of shared seeing, not a precondition for coordination | 2025-03-14, `01-writings-2025/` good_bot cluster | Same trial, measuring cooperative behaviour against shared-model agreement rather than against stated trust |
| Naming is the first step of exit | `06-zhishan/whitepaper/` | The whitepaper's own humility clause concedes the name adds no evidence. If so this is an empirical claim about collective action that the corpus's own samples-before-slogans argument undercuts. The historical version is testable: pick five named collective-action dynamics and check whether naming preceded exit |
| Self-reproducing automation can drive necessities toward zero cost in years rather than generations | `04-speculative-future/current/FOUNDATION-PRINCIPLES-DRAFT.md`; 2026-02-17 | An engineering estimate for one necessity: energy, materials, land, and the closure fraction actually required. The cooperative-turn draft's honesty about the last ten per cent (chip fabs, precision tooling) should be restored and quantified |
| The binding constraint on abundance is coordination, not physics | 2026-06-03, `_process/reading-notes/out-cb-07.md` #25–26 | The same estimate answers this directly, and it is the claim doing the most work in the constructive branch |
| Run the protocol and communities emerge | Wamo; `02-wamotopia/` | The evidential base is Dali 2022 as retold — one event, four years old, whose decisive feature (the state cancelling the venue) is not reproducible by design. CALL-en promised a public recap of the January 2026 Chiang Mai festival and none exists. **Writing that recap is the cheapest empirical act available in the entire corpus** |
| Productive recursion can compound toward generous provision with present knowledge; the rest is engineering and coordination (added 2026-09-25) | `worldbuilding/archive/001`, `007`; `theories/the-fork-and-cooperative-infrastructure/` claims 9–10 | The 2026-09-07 evidence notes are a start: component demonstrations exist. The test is the whitepaper's §1.6 recurrence filled with real numbers for one facility (yield, running cost, depreciation, rebuild cost), showing whether it reproduces its own capacity |
| Growth toward needs stops at enough (added 2026-09-25) | Ren, 2026-09-25, `16-claude-code-directions/` | What counts as need is set by the frame. In one supply unit, record whether the standard of need held as capacity grew, and who set it. This is load-bearing unknown 7 made concrete |
| The three custody rules make protective closure answerable when it happens (added 2026-09-25) | `drafts/2026-09-05-generative-foundations/WHITEPAPER-v1.1.md` §11.3–11.4 | Apply them to the corpus's own past closings: ember's repealed constitution, the retired Fork, the deleted `thinking/` files. Also apply them to one organisational decision. Check whether they flag the closings later judged wrong and pass the ones judged right |
| Elevated settlement can meet human needs while leaving more room for other life (added 2026-09-25) | `theories/architecture-for-a-living-earth/` | Its own proposed comparison: equal human provision in a branching tower, an elevated framework and a compact ground settlement. Measure light at ground level, runoff, root zones, and the disturbance from building and removal, against a stated baseline |
| Reward, observe what it teaches, revise: a community game can correct its own proxy capture (added 2026-09-25) | the watershed game, `theories/architecture-for-a-living-earth/chiang-mai-2025/` (AI-drafted) | Run one in a real association and record whether the revision happens, how long it takes, and what it costs |
| Simple rules produce unplanned institutions (emergence in Spirit–Token–Space) | `09-sts-bonfire-yi/2025-08-STS-spirit-token-space-paper.md` | Nothing anywhere is reported as emerging that was not designed; the coliving example composes designed pieces. A single documented case of an unplanned institution arising in a running Bonfire community would supply the paper's central missing observation |

### Mind, language and culture

| claim | where asserted | what would test it |
|---|---|---|
| Attention-optimized environments select for the fastest-activating attractors, collapsing the behaviour space onto the dimensions the optimizer can read | `theories/drives-narrative-attractors-and-mind/` | The 短剧 natural experiment the corpus already identified: paywall placement against completion rate, plus the 短剧-goes-overseas prediction. This is the one place a designed test is available and it has been left as an open question |
| All affect is pattern-conditioned activation over learned or inherited patterns (the two-mechanism thesis) | 2026-04-28 conversation | The developmental case is the discriminating evidence; the corpus concedes "identification" conflates at least three mechanisms. Either weaken the claim in writing or defend it developmentally |
| 良知 as situational judgment above character dispositions is non-locatable in low dimension | `06-zhishan/research/synthesis/整合分析-吸引子与主体两线.md` | This is the corpus's own falsifiable prediction and the sharpest one it has. Persona-vector methods can be run against it directly. It is also the answer to the reviewers' charge that an unspecifiable judge is an unauditable judge |
| The corpus-contrast prediction: training-archive composition changes the deployed repertoire in the predicted direction | attractor line v0.6 (dropped); 无身之我's repertoire prediction | These are the same experiment at two scales and nothing registers them as one joint commitment. Registering and running it would give the attractor line its only behavioural handle |
| An environment of 和 rather than 争 selects shared symbols toward a common root | 2026-05-05, `12-claude-ai-chats/2026-05-05_古文一元论与语言的逻辑收敛_2954cf42.md` | Ren flags both premises himself — 先秦的我的表达有误…egalitarian也是我的假设. Testable in principle against contact languages, pidgin-to-creole formation, and standard-setting bodies: does a cooperative communication environment converge symbols toward fewer roots than a contested one? |
| Conjecture 2: the precision of the character system implies a long selection history in a cooperative environment | `theories/shengsheng-buxi-generative-existence/` | Correctly tiered as conjecture and should stay tiered. The confound is that the precision may be a feature of the *reconstruction* (Cell256, the CoreAtoms) rather than of the transmitted texts, which is checkable against unreconstructed pre-Qin corpora |
| The nine-particle kernel (者 之 也 而 即 非 凡 令 是) is STLC-complete and the concept characters are constructible from one root plus those operators | `theories/jian-and-wenyan-as-formal-language/` | This one is not empirical, it is formal, and it is the corpus's most checkable unproven claim: write the encoding and check it. No Lean in the corpus compiles, and there is no prototype after nine versions of promising one |
| Humans naturally gravitate toward ends beyond the self, and this is a suppressed default rather than an installed value | 2026-03-27 conversation | One conversation behind a claim that would change the whole strategy if true — the work becomes unblocking a default rather than installing one. It deserves the same treatment the drive taxonomy got |

### The runtimes and built systems

| claim | where asserted | what would test it |
|---|---|---|
| Switching the context system (Σ) changes what an intelligence notices, remembers, treats as uncertain and finds actionable | `theories/context-as-existence-runtimes/` | The switching benchmark is the direct test of the cluster's central claim, and the sources record only that Σ v0 exists as a digested policy value with mechanics deferred. **The mind layer's headline thesis is unmeasured** |
| Compaction and branching are lived capabilities rather than storage features | ember SPEC | Also unmeasured. Both headline claims of this cluster rest on one flash-class model, n=1 per arm, over two days |
| Merge is a lattice join | `crs/context-runtime-spec-v0.1.md` | Named by the spec as the claim most in need of falsification and never experimentally answered. This is a formal property with a decidable test |
| GTC (the plugin/graph architecture) is better than a monolith | context-runtime | The corpus's own note: without an ablation it "risks becoming architectural ornament", and a generic plugin architecture "can easily become worse than a monolith". An ablation is a week |
| The concept-count metric measures conceptual load | Bonfire G8 scorecard | It counts kept vocabulary, legacy accessors, dispatch surfaces and capability branches — proxies for *surface* size. A developer's actual burden includes seven graphs, ten laws, four control axes, three delivery contracts and the lane semantics, none of them counted. A time-to-competence measurement on new contributors would test it |
| A community's software can keep growing without later changes getting costlier; unrelated growth has small marginal cost (added 2026-09-25) | `theories/evolving-community-swarms/` claim 6 | The plan's own twenty-change fixture against a same-host single-agent baseline. Nothing has run yet |
| Personal, group and community adoption scopes survive real disagreement (added 2026-09-25) | same, claims 5 and 8 | A community trial in which a contested shared change is proposed. Record whether the scoping holds, or whether the dispute moves into who decides the scope |
| Possession can express the social facts a community needs | `09-sts-bonfire-yi/2025-08-STS-spirit-token-space-paper.md` | Already refuted by construction, and this is the cleanest finding in the cluster: bans, mutes, blocks and timeouts are social facts precisely *not* held by their subject, so "a spirit holds a token in a space" is incomplete and a second relation — a space *imposing* a state on a spirit — may be irreducible. The 2026 review sees the symptom and not the conclusion |

### Where to start

Four of these are cheap, would each produce a primary result the corpus currently has none of, and are ordered here by cost.

The **Wamotopia recap** costs nothing but writing and converts the movement's entire evidential base from a four-year-old retold anecdote into a documented case. The **Σ switching benchmark** is the direct test of an existing thesis on an existing codebase. The **falsification section** — ten predictions, each with the observation that would refute it, assembled from material already in the corpus and from the abandoned v0.8 eval agenda — is perhaps a week and neutralizes the second most common objection on the list in section 4. And the **good-bot two-arm trial** settles load-bearing unknown 2, which is the question that decides what kind of work the rest of the programme should be.

*2026-09-25.* A fifth now belongs on this list, because every constructive text written in September asks for it. It is the **Chiang Mai supply unit**: one necessity, one place, costed with the whitepaper's §1.6 recurrence, with its standard of need stated and its payer named. It costs more than the other four and does more than any of them for items 1, 3 and 7.

Everything else in this file is argument. Those four, and now five, are the places where the corpus could stop arguing.
