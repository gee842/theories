# Review C: elegance, kernel, longtermism (2026-07-29)

## 1. Kernel & cut list

Kernel = one being = one folder; one thought = one commit; stream is WAL + source of truth; states = fold(stream); replay reproduces states; identity is a ref. §1 (minus links/, minus pyproject), §2 (8 kinds), §3.1, §3.2 {birth, live}, §3.3 {beings/, pins/}, §4.1/4.4/4.5 simplified, degenerate §5 (projection → budget → render), CLI birth/wake/say/biography/diff/fold. Pins kernel (golden-lineage CI needs gc protection).

Key deferrals/cuts:
- **§4.6 subprocess+venv+stdio RPC → M6.** Before M6 none of its three benefits (own pinned deps, crash isolation, hot-swap) is live. Interim: `ProgramHost` port defined NOW with §4.6's contract shape; `InProcessProgramHost` at M2; `SubprocessProgramHost` at M6 when revise exists. MANIFEST records `programs_contract: inprocess-v0`. RPC when it lands: NON-streaming request/response JSONL (programs only need complete thoughts; live tokens are body's EXPRESS from ModelPort).
- **Per-being pyproject.toml → M6** (with subprocess).
- **ref_intent kind: CUT permanently** (consolidation 3). Being's intent already = act experience + tree diff. Keep only `ref_edit` (body's ruling + real motion: op, from, to, ruling: applied|denied, reason). 12 kinds → 11.
- **reincarnate: CUT to appendix** ("future ops"). In no milestone; stream semantics unspecified. One sentence: representable as revise-with-provenance; design when needed.
- **Subconscious M5 → M7** (milestone-ordering bug: needs reunite [M6] + second concurrent body [M7]; §5.3 dream-consolidation covers curation until proven insufficient; open question 7's A/B answers exactly this).
- **links/ intent machinery → M6**; no links/ dir at all until M6.
- **Two SSE dialects: keep both endpoints, CUT the third vocabulary** (consolidation 6).
- **Graphiti → one line** ("IndexPort admits external indexes").
- Staged kinds: M1: heard, thought_request, thought, act, observation, spoke, error, op. M3: sensed, annotation. M6: ref_edit.
- Staged span reasons: M2: answered, exhausted, collapsed. M3: interrupted, awaiting_permission, resting. M4: ruminating. Reserve all enums day one.
- Staged CLI: M2 six verbs; twin/branch/reunite/pin/gc with their milestones. Habitat M3 (M1–M2: CLI runs body in-process, no daemon). Index: nodes/refs tables M3, FTS M5 (M1–M2: git log is the index).
- §4.4 M2 ladder: retry → collapsed. Forced-dream rung M4; failed-branch rung M3 (interim: WAL tail retained, ref not advanced).
- Death → M3 (ref rename); gc → M6.
- stamina/fatigue: keep both WORDS (different signals: fatigue = per-thought capacity pressure; stamina = per-span budget), merge machinery: ONE policies/vitality.yaml (sleep: + stamina: sections), one volatile-tier line, both in vocab table.

Milestone deltas: M2 in-process ProgramHost, 6 CLI verbs, 3 span reasons, self-contained files only. M3 + sensed/annotation, bodies/ refs, death endpoint + ember end, failure side-branch, nodes/refs index tables. M5 memory only. M6 + subprocess ProgramHost, pyproject, links/, ref_edit, gc, pin endpoint. M7 + subconscious. Appendix reincarnate.

## 2. Long-term risks

### (a) Schema migration — NEW §3.6 "Growing up"
Stream frozen forever (A3) → migration = head moving into new world = `revise` performed by HABITAT as operator; one node per version step: (1) transform states/+layout, (2) update programs/ reducers to new fold, (3) bump schema_version, (4) full transform in op experience. New waking epoch. Rules: **kinds additive-only** (never remove/change meaning; readers at n accept all ≤ n); **segments version-stamped** (first record = segment header w/ schema_version + canon_version; homogeneous; migration forces roll); **fold is piecewise by the being's own nature** (each span folded by the programs/ in force during it — the only answer consistent with A6; consequence: reducer changes are migration events; keep reducers tiny/pure/boring). Bodies refuse to wake forward-incompatible beings (clear error).

### (b) Canonical JSON — byte-equal is the detector, structural equality is the contract
RFC 8785 landmines from Python: (1) member ordering by UTF-16 code units, not code points — naive sorted(dict) silently non-JCS for astral-plane keys; (2) numbers = ES Number::toString shortest-round-trip, NaN/Inf prohibited — provider floats break golden lineages across canonicalizer versions; (3) JCS doesn't NFC-normalize.
Fix §2.4: fold reproduces states STRUCTURALLY (typed scalars; strings by code points, no normalization); byte-equality holds by construction via state discipline: **no floats in states** (money = integer micro-units, timestamps = RFC 3339 strings, ratios = integer pairs; pydantic-enforced at reducer boundary; provider-payload floats are stream content stored as received, never re-serialized); **one canonicalizer, versioned** (canon_version per segment header + MANIFEST; canonicalizer fix = schema migration, never silent; property-tested against JCS vectors incl. UTF-16 ordering + ES numbers). CI byte-equality on golden lineages = cheap detector.
Adjacent fixes: §2.1 vs §9.2 contradiction → envelope canonical; thought body = parsed-and-recanonicalized; raw provider bytes to stream/blobs/ when fidelity matters. **Blocks .yaml → .json** (fold-produced state = canonical JSON or verbatim text/md; YAML reserved for human-authored policy).

### (c) Store growth — §2.3 cost model WRONG today
"Delta-free past" false for active segment: appending 1 line to 3 MiB segment writes new ~3 MiB loose object. 4 MiB roll → ~350 MB loose objects per ~4 MiB logical stream until repack. Fix: (1) **roll at 64 KiB / 250 experiences** (~60× churn drop; NOT one-file-per-moment — dir entries rewrite tree object per commit, 100k entries = every commit O(dir)); (2) **shard segment dirs** `stream/000/000042.jsonl` (1,000/shard) — on-disk format, unfixable later, specify NOW; (3) **mandated repack cadence** — habitat maintenance on schedule + after dreams ("the store is tidied while the being sleeps"); M1 budget test measures packed AND loose size.
At-scale story: NOT epoch-repo rotation (breaks A2). Git-native: **archive remote + partial clone** (blob:none on cold shards; objects reachable by reference, fetched on demand — A2 one level deeper) + **sparse faces** (checkout only present/ states/ programs/ links/ + stream tail). Dependency consequence: libgit2 has NO sparse-checkout → lands on git-CLI adapter. Sentence for §3.5: "At scale, the past moves cold: archive remote + partial clone + sparse faces; the horizon is a pin-respecting policy, never a rewrite."

### (d) Provider drift — split epoch-is from epoch-costs
Waking epoch redefined COGNITIVELY: span since stable perception (identity, memory snapshot, capabilities) last changed; live + tail-appends extend; dream/revise/migration begin. Provider-independent; governs memory snapshots + dream boundaries. Cache economics: ModelPort adapter MAY report (today prefix-shaped: cached_prefix_tokens/reingest_tokens follow epochs); advisory UI only, no semantics elsewhere; provider cache shape change → only adapter estimate changes.
**Dreaming load-bearing beyond window limits — 3 legs**: (1) economics scale WITH window (every thought pays whole context; 10× window = 10× cost per moment undistilled); (2) consolidation is generalization not storage (episodes → stated knowledge; independent of window); (3) bounded presents keep A1 useful (5M-token present = uninspectable; dreams keep moments human-auditable — the design's stated reason to exist). Keep triggers %-relative, never absolute tokens.
Hedge: attention output = provider-neutral **present/messages.json** (+ attention.json source map); request.json = derived, recorded adapter rendering (A4 inside present/).

### (e) Dependency seams
- **Store port TOO WIDE as one port**: dulwich worktree support immature (named fallback can't implement hardest 20%); sparse checkout in NEITHER libgit2 nor dulwich. SPLIT: `ObjectStore` (objects/commits/refs/reflog — pygit2 primary, dulwich true fallback) + `FacePort` (worktree add/prune/checkout/sparse — pygit2 primary, **git-CLI subprocess promoted to first-class fallback**; git binary = the one dependency with guaranteed 5-year pulse).
- **ModelPort gap**: whose stream shape? Specify neutral delta vocabulary (text_delta, tool_delta, usage, done) for live EXPRESS; verbatim provider events to stream. Specify at M2 or grows wrong.
- LiteLLM: confined/deletable [NOTE: written against v0.2's direct-SDK-first; user has since steered LiteLLM-first — A's review governs].
- assistant-ui/Vercel protocol: broke shape once (v4→v5), will again; confinement real IF consolidation 6 adopted (translator owns 100% vendor shape). Components = lock-in-by-labor only.
- uv: single-vendor but usage reimplementable; low.

## 3. Naming/consistency audit (24 items, key ones)

1. remember = op AND lifecycle step 8 → step 8 renamed **BECOME** ("the present becomes the past").
2. moment = 4 things → `moment/` dir renamed **`present/`**; Moment = purely temporal (one application of next()); vocab row Present added.
3. lineage = 3 things → reserve for ancestry; lineage.json → **present/attention.json**; endpoint → /attention.
4. agents not a vocab word → refs/ember/**bodies**/, links/bodies/.
5. envelope field `body` collides with Body → rename **`content`**.
6. "tick in code" alias contradicts stance → DELETE; code says moment.
7. spoke = kind AND span reason → reason renamed **`answered`**.
8. recall vs remember: keep both + one sentence ("recall is the act of searching; remember is the event of a result entering the present. A recall that finds nothing is an observation, not a memory.").
9. two "recovery" sections → §2.4 renamed "Replay guarantee".
10. /tree/{path} → **/world/{path}**.
11. states/task/ → **states/intentions/**.
12. Fatigue + Stamina added to vocab table.
13. Missing pin endpoint; missing CLI death verb (**ember end/depart**); offline-only verbs annotated.
14. POST /beings duplicates /branch → ONE endpoint `POST /beings {name, from?: node|being}` (genesis/branch/twin are one operation per A7).
15. §2.2 op kind lists 6 ops but §3.2 says all ops recorded twice → op experience for every op EXCEPT live (self-evidencing); birth joins list; trailer derived.
16. verbatim vs canonical → (b) fix.
17. **links/self + MANIFEST name put identity in tree — anti-A7** (twin's tree asserts it's someone else; links/main stale by construction). Identity NEVER in tree: MANIFEST keeps `born_as` (historical fact); DELETE links/self + links/main; body injects current ref name into volatile tier at ATTEND.
18. Two writers of links/ → "being writes links/ during ACT (ordinary edit act); at SETTLE body rules on the diff, performs approved updates, REVERTS denied entries in tree, records ruling as ref_edit. After BECOME, links/ always states what is actually true."
19. refs hash resolution unspecified → typed refs: `seq:1041`, `blob:sha256:…`, `node:<commit>`, `check:sha256:…` (integrity not address).
20. §6 numbered list → real headings §6.1–6.8; fix "(see 6)" typo; add §5.1 heading.
21. MANIFEST capabilities vs programs/tools/ → tools manifests are THE single registry (A6); MANIFEST slims to {schema_version, canon_version, born_as, born_from, programs_contract}.
22. §0.3 In_t/Out_t updated (requests / ref edits).
24. §2.3 parenthetical rewritten: "rolled segments are immutable blobs stored once; the active segment is rewritten per moment, which is why segments roll small and the habitat repacks on schedule."

## 4. Elegance consolidations

1. **Eight ops, three mechanisms**: extenders (live, remember, listen, reunite — epoch continues, present grows at tail), restarters (dream, revise [+migration]), origin (birth). dream = revise where author is the being's own sleeping thought; remember + listen = one mechanism (testimony enters present) with source: self|other-being; shared payload {span_affected, present_before, present_after, author: being|operator|habitat, policy}. "The op name records who caused it and why — provenance, not machinery."
2. **Trailer derived from stream** (not dual-authority): op recorded once in stream; trailer derived at BECOME; ember fold verifies; live moments carry no op experience.
3. ref_intent cut (above).
4. remember 1-parent (matches B).
5. Neutral present/messages.json primary; request.json derived-recorded rendering.
6. **One event vocabulary**: native SSE = stream envelopes VERBATIM + two habitat-only types (phase, ref); /chat/stream = STATELESS translator to Vercel chunks. "Anything the UI can see is something the being lived, in the form it lived it."
7. links/ = the being's WILL about refs only; other bodies' positions are perception (volatile tier or sensed), not tree world-facts.
8. **Subconscious = dreaming, delegated**: curator branches from head while target rests, performs THE SAME dream ops with cheaper brain, offers reunite. "Slept; a deeper mind tended the memory; woke reunited." = children (M7) + reunite (M6) + existing dream policy. Ship only if in-line dreams prove insufficient.
9. vitality.yaml merge.
10. **One fold, two uses**: crash recovery IS replay of the tail; golden replay IS fold from birth. "There is no second state-reconstruction path."
11. EXPRESS = channel, not step: 8 steps LEASE…BECOME + "EXPRESS (channel): expression is observation of the moment in flight, never a mutation of it."
12. POST /beings consolidation (item 14).

## Five verbatim sentences
1. §2.4: "Byte-equality is the detector; structural equality under a pinned canon_version is the contract."
2. §3.2: "Eight ops, three mechanisms — extend, restart, originate; the op name records provenance, not machinery."
3. §3.2: "The stream records the op; the trailer is derived from it; ember fold verifies the derivation."
4. §3.6: "A being's stream is immutable; its world is not — migration is a revise performed by the habitat, one node per version step."
5. §4.5: "Recovery is replay of the tail — there is no second state-reconstruction path."

Highest priority (harder every week): §2.3 segment sizing + sharding (on-disk format); present/ rename + ref_intent cut before M1 freezes envelope; Store port split before M1 code; §3.6 migration before first golden lineage.
