# User prompts from Claude Code project -Users-ren-repos-runtime

sessions: 12  long prompts (>=200 chars): 47  chars: 292370

---
[2026-08-07T09:21] session 0d12c725

<task-notification>
<task-id>ac91bd4cedfd558b2</task-id>
<tool-use-id>toolu_011paToaqqWhhg9oukVaVwsp</tool-use-id>
<output-file>/private/tmp/claude-501/-Users-ren-repos-runtime/0d12c725-8d2a-4f05-9b71-22745c997f04/tasks/ac91bd4cedfd558b2.output</output-file>
<status>completed</status>
<summary>Agent "Review CLAUDE.md accuracy/fitness" finished</summary>
<note>A task-notification fires each time this agent stops with no live background children of its own. The user can send it another message and resume it, so the same task-id may notify more than once.</note>
<result>All three documents read in full (CLAUDE.md 64 lines; plan lines 1–1465; decisions.md 76 lines), and the repo root inspected. Report follows.

---

# Review: `files/CLAUDE.md` for Context Runtime

**Files reviewed**
- Under review: `/Users/ren/repos/runtime/files/CLAUDE.md`
- Spec: `/Users/ren/repos/runtime/Context_Runtime_v0.3.md` (read in full)
- Decisions: `/Users/ren/repos/runtime/files/decisions.md`
- Repo reality: root contains only `Context_Runtime_v0.3.md`, `files/CLAUDE.md`, `files/decisions.md`, `.git`, `.DS_Store`. No `specs/`, no `packages/`, no `bench/`, no code.

## 1. Reference accuracy

### Section citations: all correct

Every §-citation was checked against the plan. All match:

| CLAUDE.md claim | Plan section | Verdict |
|---|---|---|
| Twenty Laws §35 | §35 "Twenty laws" — "function as project law and gate every review" | ✓ |
| nine objects / three worlds §2 | §2 "Nine objects, three worlds" | ✓ |
| adoption levels §3 | §3 "Hosts and adoption levels" | ✓ |
| Node ≠ State §7 | §7 "Node and State" | ✓ |
| identity scheme §8 | §8 "Identity" | ✓ |
| layout law §9 | §9 "The layout law" | ✓ |
| canonical bytes §10 | §10 "Canonical bytes" | ✓ |
| effect bracket §15 | §15 "Effects" | ✓ |
| realm rule §16 | §16 "Realms" | ✓ |
| attenuation algebra §17 | §17 "Authority and the kernel" (contains "The attenuation algebra") | ✓ |
| stage discipline §32 | §32 "Implementation sequence" | ✓ |
| not-yet list §34 | §34 "Things we explicitly should not build yet" | ✓ |

The error-class list (CLAUDE.md line 36: `validation | authorization | race | transient | capacity | policy`) matches §26 exactly: "`RuntimeFailed` carries a structured class — `validation | authorization | race | transient | capacity | policy`". Same six, same order.

### CRITICAL — Phantom paths, no "future layout" disclaimer

**CLAUDE.md lines 4–5:**
&gt; "The spec is `specs/plan.md` (v0.3). It is the source of truth. … Rationale lives in `specs/decisions.md`."

**Reality:** `specs/` does not exist. The plan is at `/Users/ren/repos/runtime/Context_Runtime_v0.3.md`; decisions at `/Users/ren/repos/runtime/files/decisions.md`. Worse, the plan's own repo layout (§31) enumerates the intended `specs/` contents — `ontology.md`, `canonical-encoding.md`, `layout.md`, `transitions.md`, `effects.md`, `authority.md`, `merging.md`, `sessions.md`, `wire-protocol.md`, `failure.md`, `security.md` — and **`plan.md`, `decisions.md`, `adr/`, and `acceptance/` appear nowhere in that list**. So these paths are neither current reality nor the plan's stated future layout; they are the previous agent's unstated invention. A fresh session told "the source of truth is `specs/plan.md`" will fail to find the source of truth on its first action, and may conclude the spec is missing or (worse) reconstruct it. This is exactly the trap the file must not contain.

Compounding it: **CLAUDE.md sits at `files/CLAUDE.md`, not the repo root**, so Claude Code will not auto-load it at all.

**Fix (exact text for lines 4–5):**
&gt; The spec is `Context_Runtime_v0.3.md` at the repo root (v0.3). It is the source of truth. Rationale lives in `files/decisions.md`. When the §31 workspace is scaffolded (Stage 0), these move to `specs/plan.md` and `specs/decisions.md`; update this file in the same commit.

And move `files/CLAUDE.md` → `/Users/ren/repos/runtime/CLAUDE.md`.

### Same class of problem, referenced paths (major)

- **Line 13:** "`specs/acceptance/stage-N.md`" — the plan says probe numbers are "written into the Stage 1 acceptance record" (§12, §32 Stage 1) but never names a path. Invented convention, doesn't exist, not labeled as future.
- **Lines 21, 63:** "`specs/adr/`" / "`specs/adr/NNN-title.md`" — the plan never mentions ADRs anywhere. Invented convention (a reasonable one), doesn't exist, not labeled as future.
- **Line 53:** "The Stage 1 load probe lives in `bench/`" — §31's tree has only `apps/`, `packages/`, `specs/`. `bench/` is invented and doesn't exist.

Inventing these conventions is fine; presenting them as if they exist is not. Fix: one line, e.g. "Directories named here that don't exist yet (`specs/`, `specs/adr/`, `specs/acceptance/`, `bench/`, `packages/`) are created as their stage begins — creating them is part of the work, not a prerequisite."

## 2. Consistency with the plan

### MAJOR — Git ≥ 2.44 contradicts the plan's stated floor, with no recorded justification

**CLAUDE.md line 42:** "Git ≥ 2.44 verified at kernel boot · bare repos · SHA-256 object format"
**Plan §12:** "worktree-free three-way merge (`merge-tree --write-tree`, Git ≥ 2.38)"

2.38 is the only version requirement the plan states (and it is factually correct — `merge-tree --write-tree` landed in Git 2.38). decisions.md contains no Git-version entry at all. So 2.44 is a stricter pin with zero recorded rationale, in a file that claims its pins' rationale lives in decisions.md. A future agent cannot tell whether 2.44 is load-bearing (some SHA-256 or fast-import fix?) or arbitrary — and either relaxing it or cargo-culting it is a coin flip. **Fix:** either change to "Git ≥ 2.38 (merge-tree --write-tree, per plan §12)" or keep 2.44 and add one line to decisions.md stating why (e.g., "2.44 floor: comfortably post-merge-tree, mature SHA-256 support; 2.38 is the hard minimum per §12").

### MAJOR — "Pins (rationale in specs/decisions.md)" is false for most of the pins

**CLAUDE.md line 38** header claims decisions.md holds the rationale. Checked pin by pin against decisions.md:

| Pin (CLAUDE.md lines 40–45) | Rationale in decisions.md? |
|---|---|
| pnpm workspaces | ✓ "pnpm not bun (Temporal TS SDK native module compatibility…)" |
| `pg` + hand-written SQL, no ORM | ✓ "plain SQL not ORM (the control plane is small; SQL *is* its spec)" — though `pg`/node-pg-migrate specifically are not named |
| fast-import writer + cat-file --batch readers | ✓ "`fast-import` + `cat-file --batch` workers — rejected isomorphic-git…" |
| SHA-256, bare repos | ✓ (SHA-256 entry; bare repos via plan §12) |
| Node ≥ 22 | ✗ nothing |
| Git ≥ 2.44 | ✗ nothing |
| TypeScript strict, vitest, fast-check, biome | ✗ nothing |
| zod v4, ulidx | ✗ nothing |
| node-pg-migrate | ✗ nothing |
| `canonicalize` package | ✗ nothing (RFC 8785 itself is plan §10) |
| Blob CAS layout `data/blobs/sha256/ab/cd/…`, `BlobStore` interface | ✗ nothing — plan mentions a blob store but never a v1 filesystem layout or an interface name |
| Postgres ≥ 16 (line 58) | ✗ nothing — plan names PostgreSQL, no version |

Roughly two-thirds of the pins have no rationale where the file says rationale lives. The pins themselves are all reasonable; the false pointer is the bug — it trains agents to trust a cross-reference that dead-ends. **Fix (either):** (a) add a "Toolchain pins" entry to decisions.md covering the invented ones, or (b) change the header to "Pins (Git/store/SQL/pnpm rationale in decisions.md; the rest are conventional defaults — challenge via ADR, don't churn silently)".

### MAJOR — Frozen tier vs. Stage 0 drafts: overlapping and ambiguous

**CLAUDE.md lines 10–11** freeze "layout law (§9), canonical bytes (§10), effect bracket (§15)… attenuation algebra (§17)". **Lines 22–23** make Draft-for-review "everything §32 Stage 0 assigns (encoding, layout, authority matrix, effect protocol, merge structures, failure model)". But Stage 0's assignment list (plan §32) *includes* "canonical-encoding.md", the "layout law", the "effect protocol", the "attenuation algebra" — i.e., the same items appear in both tiers. An agent doing Stage 0 work on `canonical-encoding.md` cannot tell from this file whether it's touching a Frozen item (stop, get Ren's approval) or a Draft item (write it, mark `OPEN:`, ask). The intended reading is almost certainly "the architectural commitment is frozen; the Stage 0 document elaborating it is draft" — but the file never says so.

Also omitted: the plan explicitly reserves a revision window — §32 Stage 0: "**version** (not freeze — the ontology is revised once against reality after Stage 2, then held under conformance tests)" and Stage 2: "*Then the ontology is revised once, and held.*" CLAUDE.md's unconditional "Frozen" hides this scheduled revision.

**Fix (insert after line 23):**
&gt; Frozen and Stage 0 overlap on purpose: the *commitment* (e.g. "JSON per RFC 8785", "two commits bracket every effect") is frozen; the Stage 0 *document elaborating it* is draft-for-review. Elaborate freely; contradicting the commitment needs Ren. Per §32, the ontology gets one deliberate revision after Stage 2, then is held under conformance tests.

### MINOR — Draft-for-review parenthetical under-quotes Stage 0

Stage 0 assigns (plan §32): "the nine objects · five data classes · authority matrix · canonical-encoding.md / layout law … / transition &amp; patch format · effect protocol · realm rules · attenuation algebra / merge data structures + the worked memory policy · failure model · threat model". CLAUDE.md's parenthetical omits the transition &amp; patch format, realm rules, the worked memory policy, and the **threat model**. "Everything §32 Stage 0 assigns" technically governs, but the parenthetical is what gets read. Fix: append "…, threat model — the full list is §32 Stage 0" or trim the parenthetical to "(see §32 Stage 0 for the full list)".

### Verified consistent (no findings)

- Merge-bomb rejection (line 16) matches decisions.md ("Rejected: single-file JSON collections… merge bombs") and plan §9.
- "domain has zero runtime dependencies", "kernel small enough to audit" — plan §31 verbatim in spirit.
- Purity/injection rules — plan §13 ("pure and deterministic over a `StateView`") and §20 (deterministic memo key).
- Testing bullets — plan §32 Stage 2 ("every commit's patch re-applies to hash equality"), Stage 4 ("crash drills, not happy paths… `kill -9` between intent and receipt"), Stage 9 ("property tests hold… invariants after reconciliation"). The kill-9-a-real-child-process stance is a faithful strengthening.
- "Model provider keys arrive at Stage 3" — correct: Stage 1 is "No LLM", Stage 2 has no invocations, Stage 3 has "one model invocation".
- "Never implement ahead… create the interface where a future thing belongs" — §34 verbatim in spirit ("Create interfaces where these may someday belong").

## 3. Fitness as a CLAUDE.md

### MAJOR — No statement of the current stage

The file legislates stage discipline but never says which stage the project is in, and the repo (zero code) offers no signal a fresh agent is instructed to read. The implicit rule "current stage = first N with no acceptance record" fails at bootstrap because `specs/acceptance/` doesn't exist, and fails for Stage 0 anyway — Stage 0 is spec-writing and the plan defines no acceptance *tests* for it, so line 12's "done when its acceptance tests pass" has no meaning for the very first stage. **Fix:** add near the top: "Current stage: **0** (specification; nothing is built). Stage 0 is done when Ren signs off on the §32 Stage 0 document set — record the sign-off as `specs/acceptance/stage-0.md`. Thereafter, current stage = first N with no acceptance record."

### MINOR — "Environment (Ren fills in)" blanks

The pattern is legitimate (clearly human-owned placeholders, honestly labeled), but blanks in an instruction file invite two failure modes: an agent "helpfully" filling them, or silently assuming a value. One clause fixes it: "If a blank is still blank, ask Ren; never assume a value and never fill these in yourself." Also note "Postgres ≥16" inside this section is a pin hiding in the environment block (see pins table above).

### MINOR — Missing "how to run things"

No test/build commands. Currently defensible — there is no code and no scaffold — but the file should say so ("Commands land in package.json scripts as Stage 1 scaffolds; until then there is nothing to run"), otherwise an agent may burn time hunting for a harness.

### Fitness positives

Under 100 lines as promised (64). The Frozen / Draft-for-review / Free tiering is a genuinely good construct (modulo the overlap ambiguity above). "When unsure → write the ADR, stop and ask" matches decisions.md's own "draft at Stage 0, mark OPEN, then ask." The "do not re-propose rejected designs" instruction plus a concrete example is exactly what prevents re-litigation. The style section is actionable, not vibes.

## 4. Technical claims spot-check

- **`canonicalize` package for RFC 8785** — accurate; the npm package `canonicalize` implements the JSON Canonicalization Scheme, and since JCS number serialization is defined by ECMAScript's, a hand-rolled JS implementation genuinely is small. ✓
- **"pnpm not bun (Temporal TS SDK native module compatibility)"** — accurate and honestly hedged in decisions.md ("revisit when Temporal lands, not before"); the Temporal TS SDK's native Rust core has historically not supported Bun. ✓
- **Git ≥ 2.38 for `merge-tree --write-tree`** (plan) — correct. The 2.44 pin is the unexplained delta (see above).
- **SHA-256 bare repos** — supported and appropriate here. One flag, in decisions.md not CLAUDE.md: "acceptable to add later as a bridged second remote" understates the difficulty — Git's SHA-1↔SHA-256 interoperability layer remains largely unimplemented, so a SHA-1 mirror would in practice mean a re-imported bridge repo, not a plain second remote. Not a blocker (the decision itself is sound), but the recorded rationale is optimistic.
- **zod v4, ulidx, node-pg-migrate, Node ≥ 22, Postgres ≥ 16** — all real/current and reasonable in 2026; only their absent rationale is the issue.

---

## Verdict: **Ready with fixes** — not a rewrite

The skeleton is strong: every section citation is correct, the error taxonomy is exact, the tier concept is right, and nothing in it contradicts the plan's *substance* except the Git version. But as shipped it would misdirect a fresh session on its first action (phantom `specs/plan.md`), and it wouldn't even load from `files/`.

**Fixes in priority order:**

1. **(Critical)** Fix the source-of-truth paths — point at `Context_Runtime_v0.3.md` and `files/decisions.md` as they exist today, state the intended §31 migration explicitly, and move CLAUDE.md to the repo root.
2. **(Major)** Add a "Current stage: 0" line plus a Stage 0 completion criterion and the first-N-without-acceptance-record rule.
3. **(Major)** Resolve Git 2.44 vs the plan's 2.38 — align down or record the reason in decisions.md.
4. **(Major)** Make the pins header honest: add a toolchain entry to decisions.md for the invented pins, or relabel which pins have recorded rationale.
5. **(Major)** Add the one-sentence Frozen-commitment-vs-Stage-0-draft clarification, plus the plan's "revised once after Stage 2" provision.
6. **(Minor)** Label `specs/adr/`, `specs/acceptance/`, `bench/` as conventions to be created, not existing paths; complete or trim the Stage 0 parenthetical; add "if blank, ask — never fill in" to the Environment section; note that run/test commands arrive with the Stage 1 scaffold.</result>
<usage><subagent_tokens>61248</subagent_tokens><tool_uses>7</tool_uses><duration_ms>221620</duration_ms></usage>
</task-notification>

---
[2026-08-07T09:24] session 0d12c725

<task-notification>
<task-id>ac3a4d6f4a7cdb9c6</task-id>
<tool-use-id>toolu_0119GjhQPmMpVTFgGPQZSANR</tool-use-id>
<output-file>/private/tmp/claude-501/-Users-ren-repos-runtime/0d12c725-8d2a-4f05-9b71-22745c997f04/tasks/ac3a4d6f4a7cdb9c6.output</output-file>
<status>completed</status>
<summary>Agent "Cross-doc consistency and feasibility review" finished</summary>
<note>A task-notification fires each time this agent stops with no live background children of its own. The user can send it another message and resume it, so the same task-id may notify more than once.</note>
<result># Cross-Document Consistency &amp; Feasibility Review — Context Runtime v0.3

Documents reviewed in full: `/Users/ren/repos/runtime/Context_Runtime_v0.3.md` (1465 lines), `/Users/ren/repos/runtime/files/decisions.md`, `/Users/ren/repos/runtime/files/CLAUDE.md`, plus the actual repo state.

---

## 1. Three-way consistency

### C1 — MAJOR — SHA-256: the plan is conditional, the other two docs are unconditional
Docs: plan §12 · decisions.md "SHA-256 object format" · CLAUDE.md Pins.
**Claim:** decisions.md and CLAUDE.md have hardened a decision the plan (the declared source of truth) still leaves open.
- Plan §12: "**SHA-256 repositories** unless a SHA-1-only mirror (e.g. GitHub) is required for backup. The NodeId brand makes this a config choice."
- decisions.md: "SHA-256 object format. Self-hosted mirrors for backup. A GitHub mirror would force SHA-1; acceptable to add later as a bridged second remote… Rejected: SHA-1 default."
- CLAUDE.md: "SHA-256 object format" — no condition.

These are not the same decision. The plan permits creating SHA-1 universes if GitHub backup is wanted; decisions.md forecloses that (SHA-256 always, GitHub only via a future bridge). A contributor following "the spec is the source of truth" (CLAUDE.md line 4) could legitimately create a SHA-1 universe. Fix: amend plan §12 to the settled form. Feasibility footnote: Git's SHA-1/SHA-256 interop is still incomplete upstream, so "bridged second remote" is aspirational — fine, but decisions.md states it as if routine.

### C2 — MAJOR — CLAUDE.md's "Frozen" and "Draft-for-review" tiers claim the same territory, and neither acknowledges the plan's "version, not freeze" stance
Docs: CLAUDE.md Non-negotiables + Decision authority · plan §32 Stage 0.
- CLAUDE.md Frozen: "layout law (§9), canonical bytes (§10), … effect bracket (§15), … attenuation algebra (§17)".
- CLAUDE.md Draft-for-review: "everything §32 Stage 0 assigns (encoding, layout, authority matrix, effect protocol, merge structures, failure model)".
- Plan §32 Stage 0: "Write and **version** (not freeze — the ontology is revised once against reality after Stage 2, then held under conformance tests)".

Encoding, layout, the effect protocol, and the authority material appear in *both* tiers, and the frozen list omits the plan's sanctioned one-time post-Stage-2 revision. An agent literally cannot tell whether editing `specs/canonical-encoding.md` needs Ren's ADR-recorded approval or is the expected Stage 0 work. Fix: one sentence in CLAUDE.md — "Frozen = the invariants as stated in the plan; Stage 0 drafts elaborate them and may not contradict them; the single post-Stage-2 ontology revision (§32) is the sanctioned exception."

### C3 — MINOR — Three non-identical settledness registries
decisions.md settles items that CLAUDE.md's frozen list never mentions: turns/sequencer (§14, "Fine-grained nodes, grouped into turns"), memory-as-claims (§21), first-class conflicts (§24), Git-as-first-store (§11–12). Most are recoverable through the Twenty Laws (Laws 5, 11, 12), but the coverage is not identical and no doc says which registry wins. A one-line precedence rule (plan &gt; decisions.md &gt; CLAUDE.md, or the reverse) would close it.

### C4 — MINOR — Stale stage reference in plan §15
Plan §15: "This protocol exists **before Stage 6** — before the first external tool, not after the first incident." But §32 builds the bracket at Stage 4 and gates tools there: "**No external tool exists before this stage passes review.**" "Stage 6" is a leftover from an earlier numbering; as written it implies external tools arrive two stages later than they do.

### C5 — MINOR — An OPEN item second-guesses a normative sketch
decisions.md OPEN: "Renames in `PatchOp`? Proposal: no rename op." But the plan's §13 `PatchOp` union already contains only `put | delete | link`, and CLAUDE.md declares "The TS sketches in the plan are normative in shape." Either the sketch is normative (item is settled, not open) or it isn't. Cheap fix: move to Settled.

### C6 — MINOR — OPEN list vs Stage 0 scope mismatch
The OPEN list header says "draft at Stage 0," but: "Postgres DDL drafts for §28" and "Turn boundary heuristics for Level 0 hosts" are absent from §32 Stage 0's write list (they serve Stages 2–3), and "Sidecar auth model" simultaneously says "defer detail until a Python host actually exists" — an item that is both draft-at-Stage-0 and explicitly deferred. Also, §31's `specs/` tree includes `sessions.md` and `wire-protocol.md`, which no stage assigns for writing.

### C7 — MINOR — CLAUDE.md references paths the plan's layout doesn't contain
CLAUDE.md: "The Stage 1 load probe lives in `bench/`", acceptance records in `specs/acceptance/stage-N.md`, ADRs in `specs/adr/`. §31's monorepo tree has none of these (no `bench/`, and `specs/` shows 11 flat files, no subdirectories). Harmless, but §31 is the layout law's home ground — it should show them.

**Verified consistent (no findings):** NodeId/StateId/GitOid scheme (§8 vs decisions.md), record-per-file (§9), blob tiers + ingest gate (§9), effect bracket rationale (§15), realm rule (§16), attestation (§17), compiler-as-battery (§3/§20), memory claims (§21), conflicts-as-values (§24), Temporal-not-day-one, TypeScript/no-Rust, fast-import/cat-file pins (§12), §28 rebuild-at-Stage-2 vs Stage 2 acceptance, §29 tape-harness-at-Stage-5 vs Stage 5 acceptance, §3's Stage-3 LangGraph adapter vs §32.

---

## 2. Stage-sequence feasibility (§32, stages 0–11)

### S1 — MAJOR — Stage 2's "a self-grant proposal fails" is underspecified against an "authorization stub"
Stage 2 lists "authorization stub"; kernel attestation is Stage 4. The self-grant test is only non-vacuous if the stub (a) denies by default and (b) authorizes against something *outside* the proposal and outside the tree being written — i.e., a static out-of-tree grant table. An always-allow stub fails the test; a stub that reads capabilities from state reintroduces exactly the §17 hole. The plan never says what the stub checks, so Stage 2 either ships a vacuous test or quietly pulls Stage 4 attestation forward. One sentence fixes it; it belongs on the OPEN list (see §5 below).

### S2 — OK — Stage 3 model invocation vs provider keys
CLAUDE.md: "Model provider keys arrive at Stage 3, not before. Stages 0–2 run with zero providers." Stage 3 is the first stage needing an invocation. Consistent; no finding.

### S3 — OK — Tape harness sequencing
"Tape recording of invocations begins here" (Stage 3) → §29/Stage 5 "the deterministic tape harness drives the full loop with zero providers." Record-then-replay ordering is sound, and the one-time ontology revision lands after Stage 2, before any tapes exist. No finding.

### S4 — MINOR — Stage 3 `summarize-epoch` vs Stage 8 compaction records
Stage 3: "manual compaction exists from here on"; Stage 8: "Full compaction records, frontiers, retention classes." §22 requires a compaction record (source frontier, digests, omitted information, retention class) and Law 8 forbids destructive summarization — but the plan never says what the Stage 3 manual version records. Under CLAUDE.md's "never implement ahead of the current stage," an agent needs the minimal Stage 3 record shape stated, or it must guess.

### S5 — MINOR — Dialog records are needed by Stage 6 but their production is only implied at Stage 3
Stage 6 acceptance: "a thread reconstructs from the repository with no session store present" — requiring `state/dialog/&lt;shard&gt;/&lt;ulid&gt;.json` records to have accumulated since Stage 3's `chat` command. But the observation-transition convention is defined in §25 (Session territory, Stage 5), and Stage 3's scope never says its `chat` writes dialog records; only "dialog location" is in Stage 0's layout scope. It works, but only if Stage 3 implements §25's dialog convention — make that an explicit Stage 3 deliverable.

### S6 — OK, with a caveat — Realm enforcement at Stage 4 vs forks from Stage 1
The question "what stops a simulation from touching the world in Stages 1–3" is answered by the plan: nothing world-touching exists. Stage 3 has "one read-only tool" and Stage 4 states "**No external tool exists before this stage passes review.**" So it is moot by construction, and the plan does say so. Caveat (minor): the Stage 3 tool's read-only-ness is asserted, not enforced — the capability machinery that would enforce `effects: "none"` arrives at Stage 4 — and model invocations from any branch ship state to a provider by design. Worth one honest sentence in Stage 3.

### S7 — MINOR — Stage 4 approvals bind a "projection hash" before any surface exists
§17: an approval records "the payload hash, the node, **and the projection hash** — the exact bytes the human saw." Stage 4's acceptance includes "approval replay fails," but surfaces arrive at Stage 5–6. Feasible if the Stage 3–4 terminal rendering counts as the projection, but the plan doesn't say what the projection is pre-UI.

### S8 — MAJOR — Stage 8 crypto-shredding is a write-path property scheduled as a late feature
Stage 8: "tombstones with crypto-shredding"; §22: "the payload is crypto-shredded (per-subject keys)." You can only crypto-shred what was encrypted under per-subject keys **when it was written**. Evidence blobs start accumulating at Stage 1–3 (CLAUDE.md pins "Blob store v1: filesystem CAS `data/blobs/sha256/…`" — plaintext CAS). As sequenced, Stage 8 begins with a full blob-store re-encryption migration, or crypto-shredding silently degrades to "delete the file." Either decide envelope-encryption-at-ingest at Stage 0, or descope v1 tombstones to exclusion-flags + physical blob deletion and say so.

### S9 — MINOR — Two specified capabilities are assigned to no stage
§30's upgrade-on-touch (`schema_upgrade` children, the bounded support window) and §29's observability acceptance test ("from any trace span, navigate to the exact node") appear in no stage's scope or acceptance list. Both are cheap to slot (§29 fits Stage 5; §30 fits wherever the first schema bump happens) but currently float.

Otherwise the dependency graph is sound: Stage 1 needs only Stage 0's encoding/layout; Stage 2's Postgres rebuild matches §28; Stage 5's SSE resume needs the Stage 2 event log; Stage 6's approvals need Stage 4; Stage 7's ACL acceptance needs only §17 path scopes (Stage 4), not Stage 10 multi-agent; Stage 9 needs Stage 7's claims; the §33 drill "two agents commit disjoint paths → linearized" needs only Stage 2 commutation, not Stage 10.

---

## 3. Scope realism (solo maintainer)

**Where the plan already hedges well:** the Stage 1 load probe with named fallbacks; terminal-first Stage 3 ("months before our own frontend exists"); the §34 not-yet list, which is binding per CLAUDE.md; pgvector gated on measurement (§21); Temporal last, behind an unchanged interface (§32 Stage 11); the AssistantTransport two-day spike (§27); the honest "ugly conflict-reconciliation surface… research-grade" warning (Stage 9). This is unusually disciplined hedging.

**Where it commits to breadth prematurely:**

1. **Four host adapters + sidecar (§3, §31) vs the one-host rule (§34).** §34 says "adapters for every framework at once — one host proves the seam" is a not-yet, and decisions.md agrees ("adapters beyond LangGraph until that one seam is proven"). Yet §3 markets all four with per-framework integration detail and §31 scaffolds `adapters/mastra/`, `adapters/openai-agents/`, `adapters/sidecar/` as package directories. Keep `langgraph/` only in the tree; mark the rest as future.
2. **Stage 4 is the heaviest single stage:** bracket + reconciliation + attestation + path scopes + attenuation + approvals-with-projection-hashes + realm enforcement + **signed runtime bundles + sandbox** + Level 2 host middleware. Signed bundles and sandboxed historical compilers exist to bound runtime self-modification — which §34 defers anyway. A kernel that loads only its built-in runtime needs no signature verification yet. Sever bundles/sandbox from Stage 4's gate; keep the bracket, realms, attestation, approvals.
3. **Crypto-shredding** — cut from v1 per S8.
4. **Stages 5–6 are a full product frontend** (SSE-with-resume, React Flow DAG, node inspector, Assistant UI adapter, streaming, attachments) for one person. The plan's own mitigation (minimal web, spike first) is right; the risk is that "minimal" grows. The tape harness and Postgres-rebuild drills are the parts that earn their keep; the DAG explorer can stay crude much longer than demo pressure will suggest.
5. **Temporal (Stage 11)** is correctly last, but it already taxes the present: decisions.md picks pnpm over bun for Temporal SDK compatibility "— revisit when Temporal lands, not before." Fine, but notice this is the plan's only day-one cost paid for a stage that may never arrive.

**Minimal path to the §33 demo:** Stages 0–7 plus 9. Stage 8 (compaction records/retention — Stage 3's manual `summarize-epoch` suffices for the demo), Stage 10 (multi-agent), and Stage 11 (Temporal) are not exercised by any line of §33. Within that path, the severable items are Stage 4's bundles/sandbox and Stage 6's attachment polish. The plan never states this critical path; §32 reads as strictly linear. Stating it would let schedule pressure cut the right things.

**Highest schedule risk, ranked:** Stage 4 (breadth), Stage 9 (research-grade UX, merge fuzzing), Stage 6 (frontend integration), Stage 5 (SSE/resume infra).

---

## 4. Repo state vs documents

### R1 — CRITICAL — CLAUDE.md is not where it must be to function
Reality at `/Users/ren/repos/runtime`: a git repo with **zero commits** (empty object store, no refs), containing `Context_Runtime_v0.3.md` at the root, `files/CLAUDE.md`, `files/decisions.md`, and an untracked `.DS_Store`. No `specs/`, no `packages/`, no `bench/`, no code.

CLAUDE.md says "This file is loaded every session" — but at `files/CLAUDE.md` it is not auto-loaded by Claude Code, so every discipline it encodes (stage gating, frozen list, ADR protocol, pins) is currently inert. Every self-reference in the doc set is false today: "The spec is `specs/plan.md`" (it's `/Context_Runtime_v0.3.md`), "Rationale lives in `specs/decisions.md`" (it's `files/decisions.md`), acceptance records in `specs/acceptance/`, ADRs in `specs/adr/` (neither exists). Also: §31 names the monorepo `context-runtime/`; the actual directory is `runtime/` — decide whether this repo *is* the monorepo. Finally, CLAUDE.md's Environment section is unfilled blanks ("Deploy target: ____ · data dir: ____ · Postgres: ____"), which blocks Stage 1–2 acceptance work (the load probe needs a data dir; Stage 2's rebuild test needs Postgres).

One clarification worth a line somewhere: the SHA-256 pin applies to *universe* repos, not this source repo — the source repo will want SHA-1 if it is ever pushed to GitHub. CLAUDE.md's "Commit messages in this repo" phrasing already implies the distinction; make it explicit before someone applies the pin to the wrong repo.

---

## 5. Open-questions completeness

decisions.md's existing item 1 already covers the footprint/cap-scope selector grammar jointly — good. But §24's merge "strategy dispatch per path-pattern" is a **third** consumer of the same grammar and isn't named in that item. Missing from the OPEN list entirely:

1. **Dialog record schema.** §25 gives only "(`role`, content or blob ref, `at`, `via`)" in passing; needed concretely by Stage 3's `chat` and Stage 6's ThreadProjection. Stage 0's layout scope covers dialog *location* only.
2. **Turn-boundary rules for the runtime's own loop (Level 3).** §14 defines turn mechanics (detached chain, shared ULID) but never what opens/closes a turn in §13's `step()`. The OPEN list covers only Level 0 host heuristics.
3. **`SimulationId` semantics.** §16's `{ kind: "simulation"; world?: SimulationId }` is the only occurrence of the concept in all three documents. What a simulation "world" is — whether branches can share one, whether simulated receipts are visible within it — is undefined.
4. **Stage 2 authorization-stub semantics** (per S1): deny-by-default, static out-of-tree grant table, never reads the proposal's or written tree's capability JSON.
5. **Evidence redaction rules.** §18: "Redacted at ingest… scrubbed for credentials" — no ruleset, no owner; belongs with Stage 0's threat model.
6. **Blob encryption-at-ingest** (forced by S8): decide now whether evidence blobs are envelope-encrypted per subject from day one, or crypto-shredding is descoped.
7. **Minimal Stage 3 compaction-record shape** (per S4).
8. (Lesser) The `Commit` / `MergeRequest` / `Diff` shapes in §11's Store interface are unsketched — arguably covered by CLAUDE.md's "finalized in `packages/domain`," but the Store is Stage 1, before most spec drafting pressure hits; and §28's "budgets, enforced as policy in the tree" names a policy schema that exists nowhere.

---

## (a) Prioritized fixes

1. **[R1]** Fix repo reality first (checklist below) — nothing else in the docs is operative until CLAUDE.md loads and the paths resolve.
2. **[C1]** Amend plan §12 to the settled unconditional SHA-256 form (delete "unless a SHA-1-only mirror… is required").
3. **[C2]** Add the frozen-vs-draft precedence sentence to CLAUDE.md, acknowledging the §32 post-Stage-2 revision window.
4. **[S1 + item 4]** Specify the Stage 2 authorization stub in one paragraph so "self-grant fails" is meaningful.
5. **[S8 + item 6]** Decide encryption-at-ingest now, or descope crypto-shredding from v1 and edit §22/Stage 8 accordingly.
6. **[§5 additions]** Add OPEN items 1–3, 5, 7 to decisions.md; move the rename question to Settled (C5); name §24 dispatch patterns as a selector-grammar consumer.
7. **[Scope]** Add a "critical path to §33" note to §32 (stages 0–7 + 9; 8/10/11 post-demo; bundles/sandbox severable from Stage 4); trim §31's adapter tree to `langgraph/` (+ future markers).
8. **[C4, C7, S5, S9]** Sweep the small stale references: §15 "before Stage 6" → "before Stage 4's gate"; add `bench/`, `specs/adr/`, `specs/acceptance/` to §31; make dialog-record production an explicit Stage 3 deliverable; assign §29's trace-to-node test and §30's upgrade-on-touch to stages.

## (b) First-commit checklist

1. `git mv` equivalents (these are the first adds, since there are no commits yet):
   - `Context_Runtime_v0.3.md` → `specs/plan.md`
   - `files/decisions.md` → `specs/decisions.md`
   - `files/CLAUDE.md` → `CLAUDE.md` (repo root — this is what makes "loaded every session" true)
2. `.gitignore` with `.DS_Store`, `node_modules/`, `data/`; remove `files/` and the stray `.DS_Store`.
3. Create `specs/adr/` (with a `000-template.md`) and `specs/acceptance/` (empty, `.gitkeep`).
4. Fill CLAUDE.md's Environment blanks (deploy target, data dir, Postgres) — prerequisite for Stage 1–2 acceptance.
5. Decide the monorepo question: if this repo is §31's `context-runtime/`, add `pnpm-workspace.yaml` + root `package.json` stubs now (or record an ADR that the monorepo lives elsewhere and fix §31's root name).
6. Apply fixes 2–3 above (the two source-of-truth edits) in the same or next commit, so the first committed state is internally consistent.
7. Seed Stage 0 spec stubs (`specs/ontology.md`, `canonical-encoding.md`, `layout.md`, `transitions.md`, `effects.md`, `authority.md`, `merging.md`, `sessions.md`, `wire-protocol.md`, `failure.md`, `security.md`) each carrying its `OPEN:` markers from the expanded decisions.md list.
8. Commit under the pinned convention, e.g. `stage-0(§31): establish spec tree and working instructions` — making the repo's very first commit an instance of its own rules.</result>
<usage><subagent_tokens>62095</subagent_tokens><tool_uses>6</tool_uses><duration_ms>353373</duration_ms></usage>
</task-notification>

---
[2026-08-07T09:27] session 0d12c725

<task-notification>
<task-id>a6950fe09479bae6c</task-id>
<tool-use-id>toolu_01PEkXsdw2i45gvCbDqM3q1D</tool-use-id>
<output-file>/private/tmp/claude-501/-Users-ren-repos-runtime/0d12c725-8d2a-4f05-9b71-22745c997f04/tasks/a6950fe09479bae6c.output</output-file>
<status>completed</status>
<summary>Agent "Review plan architecture soundness" finished</summary>
<note>A task-notification fires each time this agent stops with no live background children of its own. The user can send it another message and resume it, so the same task-id may notify more than once.</note>
<result># Technical Review — Context Runtime v0.3

## Verdict

The ontology is genuinely strong — Node/State separation, the five data classes, the effect bracket, realm-by-ref, and the attenuation algebra are the right shapes, and the staging discipline (load probe first, crash drills as acceptance) is unusually honest. But the document has two places where frozen mechanisms contradict each other outright (turn atomicity vs. the effect bracket; tombstones vs. the Git object model), and a cluster of load-bearing mechanisms — the sequencer's commutation rule, the fast-import write path, no-op suppression, blob GC, promotion — that are treated as solved while hiding real correctness problems. None of these are fatal to the architecture; most are fixable with explicit design work. But several would surface as data-loss or double-execution incidents if implementation proceeded from the text as written, and two of them ("the demo works" and "GDPR erasure works") cannot both be true under the current design.

---

## Critical findings

### C1. The effect bracket and turn atomicity are mutually exclusive as specified
**Sections:** §5, §13, §14, §15.
**Claim:** An effect's intent commit must be real before dispatch, but a turn's commits are unreachable until the turn-ending CAS move — so mid-turn effects dispatch against commits the system itself defines as "not real."

§15 requires the intent be "committed BEFORE dispatch," and its recovery story is "On recovery the intent is visible in state." §14 says a turn — explicitly including "tool calls" — "is built as a **detached chain** and applied with **one CAS ref move**," and "Recovery of a half-built chain is trivial: it was never reachable." §5 states "Nothing before step 3 [the CAS move] is real." Failure scenario: mid-turn, the agent sends an email; the intent commit sits in a detached, unreachable chain; the process dies before the turn's CAS move. The chain is discarded per §14's recovery rule ("it was never reachable"), the intent is *not* visible from any ref, and §22's GC (and `git gc`) will eventually delete it — yet the email was sent. The double-send the bracket exists to prevent is back, now with the evidence erased. The §13 pseudocode makes the tension visible: `kernel.bracket(head, admitted.effects)` ("two commits") runs *before* `store.chain(...)` and `sequencer.advance(...)` — either the bracket's commits are inside the detached chain (unreachable at dispatch) or they are separate reachable commits (breaking "one CAS ref move" per turn and "Races happen once per turn"). The plan must choose: split turns at effect boundaries, or anchor intents on a durable side-ref, or move the pre-dispatch guarantee entirely into the Postgres journal — each option sacrifices something the text currently claims.

### C2. Tombstones/crypto-shredding are incompatible with inline state, patch-embedding, and Git object integrity
**Sections:** §22 vs. §7, §9, §10, §12, §13.
**Claim:** "The hash chain survives; the bytes are gone" is not achievable for the data most likely to need erasure, because those bytes live inline in Git objects and are duplicated into `record/transition.json`.

§9 puts every value ≤ 64 KiB "inline in `state/`" — which is where dialog messages and memory claims (the PII-dense records) live. §7's layout notes `transition.json ← includes the patch itself`, and `PatchOp` carries the literal `value: CanonicalValue` — so every inline write exists in *at least two* Git objects (the state blob and the transition record). Now apply §22: "the payload is crypto-shredded (per-subject keys) or physically redacted... the hash chain survives; the bytes are gone."

- *Physical redaction* of a Git blob referenced by immutable trees breaks the ODB: `fsck` fails, `git push` to the mirror (§12: "replicates the agent's entire existence") fails on the missing object, and `Store.view` on every historical StateId containing that blob errors. Redacting the value inside `transition.json` is worse: the file contains other fields, so its bytes must be rewritten, its OID changes, and either the trees/commits above it are rewritten (the hash chain does **not** survive) or the repo contains objects that don't hash-verify.
- *Crypto-shredding* requires ciphertext at rest, which destroys §10's contract that "equal meaning yields equal bytes yields equal StateId," breaks §13's third-party verify (patch-apply-to-hash-equality), and collides with dedup: per-subject keys make identical content hash differently per subject, while conversely Git's dedup means one plaintext blob may be reachable from multiple subjects' records — shredding subject A's key deletes nothing if the same bytes serve subject B, and physical deletion destroys B's data.

Stage 8's acceptance test ("a tombstoned payload is gone physically, honest logically") cannot pass against this design without violating Stage 1's integrity invariants. This needs a real design (e.g., envelope-encrypting *all* erasure-eligible record classes from day one, with StateId computed over plaintext and a keyed indirection layer), not a paragraph.

---

## Major findings

### M1. The sequencer's commutation check ignores read footprints
**Sections:** §13, §14.
**Claim:** Linearization as specified checks only write-disjointness plus explicit preconditions, which admits write-skew — the classic snapshot-isolation anomaly.

§14: "If a queued proposal's writes are disjoint from the interleaved history and its preconditions still hold against the new head, it is reapplied in arrival order." Proposals declare `reads`, but the rule never consults them. Scenario: two proposals each read a shared budget record and write disjoint expense records; both validate against the old head; both writes are disjoint from the interleaved history; both linearize; the budget invariant is violated with no branch and no conflict. "Reapplied" is also ambiguous: re-applying the old patch executes a decision made against a state that no longer holds; re-running the reducer produces an outcome that was never validated or authorized. Preconditions could plug the hole only if every read were mirrored into a `hashEquals` precondition — which the plan neither requires nor mentions.

### M2. Model-derived pinning contradicts the multi-agent parallelism claims
**Sections:** §14, §12, §32 Stage 10.
**Claim:** §14 simultaneously promises that disjoint agents "never branch" and that any model-derived proposal whose head has moved lands on a branch "never silently rebased" — and agent proposals are model-derived.

§14: "Agent 17 writing `agents/17/**` and agent 841 writing `agents/841/**` never branch." Same section: "a model-derived proposal is pinned to its input node: if the head has moved, the result lands as a child of the node it was compiled from, on a branch." If 841 commits first, 17's model-derived proposal meets a moved head and, by the pinning rule as written (conditioned only on "the head has moved," not on overlap), branches. Stage 10's acceptance — "N agents on one universe under footprint parallelism produce zero accidental branches" — requires the opposite reading. Worse, the pin's own rationale (the compiled context's meaning depends on the state it was compiled from) implies the *true* read footprint of a model-derived proposal is the compile's input — which spans shared dialog, memory, and tasks — so honest read-footprints intersect nearly every interleaved write and everything branches. The plan needs an explicit rule for when a moved head invalidates a model-derived proposal (e.g., only when the interleave intersects the compiled context's source paths) and it does not have one.

### M3. The no-op rule suppresses record-only commits and strands evidence for GC to eat
**Sections:** §7, §13, §18, §19, §22.
**Claim:** "If the resulting StateId equals the parent's, nothing commits" conflicts with commits whose entire payload is `record/`, and leaves invocation evidence with no committed node unreachable — and therefore sweepable.

An effect intent, per §7's layout, lives under `record/effects/`; if it writes nothing under `state/`, the no-op rule as literally stated ("A reducer whose output state equals the parent state commits nothing") suppresses the very commit §15 requires before dispatch. (§15's "the intent is visible in state" suggests intents *do* write state — but then §7's layout is wrong, and effect bookkeeping churns StateId, so two branches identical except for their effect journals no longer share a StateId, weakening §7's convergence and memoization claims.) Separately, §19 explicitly allows `resultNodes: ∅ if none committed` — an invocation that led to a no-op. Its evidence blobs are "referenced from `record/`" (§18) of no commit; §22's blob GC is "mark-and-sweep from reachable `state/` and `record/` roots"; the sweep collects the evidence of a real, paid, possibly-important model call — directly contradicting §4/§18's "evidence survives everything."

### M4. The fast-import write path's visibility, durability, and CAS semantics are unexamined — and the load probe as specified won't catch them
**Sections:** §5, §11, §12, Stage 1; decisions.md pins.
**Claim:** The hot write path assumes properties `git fast-import` does not have, and the probe measures throughput, not the production commit shape or crash durability.

§12 pins "a long-lived `git fast-import` stream — blobs, trees, commits, and atomic ref updates through one process," and §11's `move` is CAS. But fast-import's ref updates are not compare-and-swap, and objects written into its stream are invisible to the `cat-file --batch` readers (and to `update-ref`) until a `checkpoint`, which finalizes a packfile. The production shape is therefore *chain → checkpoint → external CAS `update-ref` → read-back* — one small packfile per turn, i.e., the loose-object-churn problem reborn as small-pack churn. The probe ("100k commits at 100× expected rate; p50/p99 commit latency via fast-import") will, if implemented as one continuous stream, measure a workload production never runs. Durability is worse: §5 declares the CAS ref move "the semantic commit point," yet nothing specifies fsync ordering — Git does not fsync ref updates by default, so a power loss after step 3 can silently regress the head below commits the runtime already reported as real, and a crash between fast-import buffering and pack finalization can leave a CAS'd ref pointing at objects that never hit disk. The crash drills (§32) all target the effect bracket and SSE, never the store. Finally, "one fast-import writer per universe" plus "one sequencer per ref" plus "CAS mediates between runtime processes" leaves writer ownership and failover (who holds the stream when the worker dies?) unassigned.

### M5. StateId is not the durable content identity the plan leans on — it is a Git-encoding artifact
**Sections:** §8, §9, §11, §12, §13.
**Claim:** StateId (v1: "the Git tree OID of `state/`") is bound to hash algorithm, Git tree encoding, file modes, and the shard layout, which undercuts the "Store interface is the firewall" fallback and Law 3.

If the Stage 1 probe fails and the fallback store (all-Postgres CAS, or Dolt — §12) replaces Git, every recorded StateId — in every Node, every transition verify, every memoization key — changes; the swap the firewall promises is actually the "importing into a new universe" migration §8 admits only for hash-algorithm changes. §13's "Replication can ship transitions instead of trees" similarly requires the replica to reproduce Git's exact tree encoding and the exact shard layout: change the shard fan-out (a "config" decision) and byte-identical semantic content yields a different StateId — Law 3 ("same content, same identity") silently becomes "same content *under one layout version*." And §8's "GitOid never leaves the store" is contradicted in substance: StateId *is* a GitOid wearing a brand. One factual note on the escape hatch: decisions.md's "bridged second remote" to a SHA-1 GitHub mirror does not exist — Git's SHA-1/SHA-256 interop remains incomplete; a SHA-256 repo cannot push to a SHA-1 remote today, so the backup fallback is currently fiction.

### M6. Evidence retention contradicts the GC rule, and evidence volume is the unbounded cost nobody prices
**Sections:** §4, §18, §19, §20, §22.
**Claim:** "Retained by policy, independently of state retention" (§18) is impossible under §22's reachability-based mark-and-sweep, and per-invocation evidence is the system's dominant, effectively permanent storage cost.

§22 defines exactly two blob fates: reachable (kept) or unreachable (swept), and names "vanish while referenced" as the failure mode — yet policy-expiring an evidence blob referenced from a reachable `record/` is precisely that. Meanwhile every invocation stores the compiled context, the full request (which *contains* the compiled prompt again — near-total duplication the item-tree sharing does not touch), the response, provider-opaque reasoning state, and a "full selection process" compile record (§20). For an agent running "continuously for months" (§1) at tens of invocations per hour, evidence — not state — dominates disk, backup ("git bundle... alongside a blob-store manifest," §12), and export, and the ingest gate (§9) protects only `state/`. The plan needs either evidence-class retention tiers with tombstone-grade redaction, or an honest admission that evidence is append-forever and priced accordingly.

### M7. Blob-store GC and `git gc` race in-flight commits and detached chains
**Sections:** §5, §14, §22, Stage 1.
**Claim:** Mark-and-sweep from reachable roots, run against a protocol whose first step uploads blobs *before* anything references them and whose turns are unreachable until they end, deletes live data absent a grace/pinning mechanism the plan never mentions.

§5 step 1 uploads evidence blobs; the CAS move (step 3) may be minutes later — a turn spans model invocations and tool calls. A sweep in that window sees unreferenced blobs and collects them; the turn then commits with dangling `BlobRef`s. The same applies to Git objects in detached chains ("it was never reachable," §14) versus scheduled `gc` with pruning — and Stage 1's "orphan cleanup" acceptance institutionalizes exactly the dangerous operation. The standard fixes (grace periods keyed to upload time, pin sets for open turns) are easy but must be specified, because the failure is silent corruption discovered much later.

### M8. The "kernel as TCB" is a library in a monolith; the sandbox and Level-2 claims outrun the actual trust boundary
**Sections:** §3, §17, §31.
**Claim:** Every security "cannot" in the document is enforced by a package boundary inside one Node process, which is not a privilege boundary.

§31 makes `packages/kernel` a library linked into `apps/worker` alongside the sequencer, compiler, reducers, effect executors, and — at Levels 0–2 — the host framework itself. Credential resolution (§17) therefore happens in the same address space as arbitrary host and tool code; "self-grant is impossible by construction" holds at the API surface, not the process. §17's "Historical or branch compilers execute sandboxed with their own budgets" names an unsolved problem as a feature: there is no credible in-process TypeScript sandbox (vm2 is abandoned; worker threads do not confine), and no process-isolation design is given. §3's footnote ("at the levels that route through it") concedes the bypass problem, but the Level 2 bullet still claims "simulations cannot email, crashes cannot double-charge, approvals bind to what was seen" — for an embedded library, each "cannot" is "will not, provided the host voluntarily routes every call through the wrapper." Relatedly, §17's approval binding ("the projection hash — the exact bytes the human saw... closing both approval-replay and TOCTOU") closes TOCTOU only if the projection function is deterministic, versioned, and computed by trusted code; the surfaces that render approvals live outside the TCB (§27, or outside the codebase entirely at Level 2), so the kernel is attesting a hash supplied by the very layer it should distrust.

### M9. Promotion is a named ceremony with unspecified semantics
**Sections:** §16, §17, §26.
**Claim:** "Its pending effects are re-authorized and re-executed" leaves undefined what happens to the DAG, to `Node.realm` stamps, to state derived from simulated observations, and to approvals bound to simulation nodes.

Does `PromoteBranch` fast-forward `refs/live` to the simulated tip (leaving `realm: simulation` permanently stamped in live ancestry, contradicting §7's per-node `realm` field and the `Realm: live` trailer semantics) or re-commit the branch (new NodeIds, breaking session pins and cross-references)? "Pending" effects re-execute — but what of effects the simulation recorded as *succeeded* against a simulated world, and of every memory claim and decision downstream of those fake observations, which promotion adopts wholesale as live state? And §17's approvals are "checked at execution time against the executing node" — under re-execution the executing node is by definition not the approved node, so either every promotion invalidates all approvals (probably intended, never stated) or the check is loosened (dangerous, also never stated). This is the single bridge between the safe world and the real one, and it is the least specified mechanism in the document.

---

## Minor findings

- **ULID-prefix sharding is time-bucketing, not load-spreading (§9).** ULIDs are timestamp-prefixed; a 4-char shard (`01J9/`) covers roughly a 2^30 ms ≈ 12-day window, so *all* concurrent writes land in one hot shard whose tree grows for days — "tree objects stay small and appends stay O(1)" is false at fixed granularity under real write rates. Relatedly, §9's packfile rationale ("each path's history is a sequence of similar small objects") is wrong for a layout whose files are write-once by design; delta wins come from cross-file similarity and tree-version deltas instead.
- **Canonical JSON defeats the default merge strategy (§10, §24).** RFC 8785 output is a single line, so Git's line-based three-way merge can never merge two edits to one record; §24's `default: three-way` and `workspace/** three-way` rows degenerate to per-file conflicts, and the JSON-structural merge that would fix this is assigned to no component (Store.merge is "structural only" at tree level).
- **Read-your-writes is unaddressed (§5, §21, §26, §28).** Projection is "asynchronous" (step 4), yet the next turn's compile retrieves from Postgres FTS/pgvector — a claim asserted this turn can be invisible to retrieval next turn, and session event emission relative to step 4 is unspecified. Solvable (await projection per ref; read-through), but the core loop depends on it.
- **Ref proliferation is unmeasured (§14, §22, §23, Stage 1).** Every divergence mints a namespaced ref, and "deleting a branch means archiving its head under `refs/archive/`" makes ref count monotonic — but the load probe measures commits, diff, merge, gc, and bundle size, never ref cardinality.
- **The LangGraph Level 0 mapping recreates a rejected design (§3 vs. §9).** "Channel values → one record per channel" puts the dominant LangGraph pattern — an accumulating `messages` channel — into exactly the single-file collection §9 rejected as a merge bomb, giving whole-array diffs and guaranteed conflicts on concurrent checkpoint forks.
- **Compile determinism rests on an optional, unspecified field (§19, §20, §29).** `retrievalSnapshot?` is optional and framed as pinning *evals*; live invocations without it make the memoization key `(StateId, agent, requestHash, compilerDigest, retrievalSnapshot)` incomplete as the index drifts, and no mechanism is given for snapshotting a live FTS/pgvector index cheaply per invocation.
- **Reconciliation-by-query is the exception, not the rule (§15).** Most non-idempotent APIs (email sends prominently) offer no query-by-idempotency-key; the honest `unknown`-and-escalate path exists in the text but will be the *common* path, which changes the operational load the design implies.

---

## Strengths

The core corrections from v0.1 are real improvements, not churn: the Node/State split with the no-op rule (once repaired per M3) is elegant and earns its keep; the five-data-class taxonomy with a single authority per record resolves a contradiction most systems never even notice; the effect bracket is the correct shape and correctly scheduled before the first tool rather than after the first incident; realm-as-ref-rule is enforceable where branch metadata never is; the attenuation algebra (fork ⊆, merge ∩, expansion-by-recorded-grant) is the right lattice; record-per-file with union merges genuinely does convert most merges into tree operations; the reproducibility ladder (§19) is refreshingly honest; conflicts-as-values with Jujutsu as prior art is the right call; and the staging plan — probe before dependence, `kill -9` drills as acceptance tests, delete-and-rebuild-the-index as a standing test, one host adapter as an API forcing function — is better engineering discipline than most shipped systems ever apply. The decisions.md ledger preventing re-litigation is itself good architecture. The problems above are concentrated where mechanisms *interact* — bracket × turns, GC × in-flight writes, pinning × parallelism, erasure × content-addressing — which is exactly where a v0.4 pass should aim.</result>
<usage><subagent_tokens>59914</subagent_tokens><tool_uses>4</tool_uses><duration_ms>571544</duration_ms></usage>
</task-notification>

---
[2026-08-07T09:56] session 0d12c725

<task-notification>
<task-id>whus1j5fb</task-id>
<tool-use-id>toolu_01UGy2s3s88cx74yki98gkkz</tool-use-id>
<output-file>/private/tmp/claude-501/-Users-ren-repos-runtime/0d12c725-8d2a-4f05-9b71-22745c997f04/tasks/whus1j5fb.output</output-file>
<status>completed</status>
<summary>Dynamic workflow "Verify plan v0.4 + CLAUDE.md + decisions.md address the three review reports without new contradictions" completed</summary>
<result>{"summaries":["v0.4 genuinely resolves both criticals and most of Report 1's majors with real, mutually consistent mechanisms rather than patched prose: turn anchoring (C1), residence-split erasure with the false claim withdrawn (C2), read-consulting commutation with enforced footprint-scoped views (M1), the compile-source invalidation rule for pinning (M2), encoding-versioned StateId with Law 3 rescoped (M5), per-class evidence retention priced in print (M6), GC grace windows and anchor roots (M7), TCB honesty plus registered approval projections (M8), and re-execution promotion (M9's semantics). Five of seven minors are fully fixed. Three repairs left verifiable defects. (1) M3 is only partially propagated: §13's commit step still reads \"if the resulting StateId equals the parent's, nothing commits\" (line 626), flatly contradicting §7's record-only nodes at the exact site of the original bug. (2) M4's durability fix overclaims: Git's `core.fsync=committed` aggregate equals `objects` and excludes the `reference` component, so ref updates — the §5 semantic commit point and ADR-002's \"fsynced\" turn anchors — are still not fsynced; §5's \"objects and ref are fsynced\" is not delivered by the pinned config, and the review's power-loss head-regression scenario survives (fix: `core.fsync=committed,reference`). (3) M9's crossover labeling cites \"§20's authority labels\" for a `simulation` label that §20's authority union does not contain. Additionally, the read-your-writes minor fixed the compile barrier but left session-event-emission ordering unspecified, and the §13 loop sketch still shows bracket-before-chain from head.id (cosmetic given §14's explicit prose). Net: 15 of 18 items addressed, 3 partial, 0 missed; the partials are each one-sentence-to-one-line fixes but two of them (M3, M4) sit exactly where the original data-loss findings lived.","All six Report 2 fixes verified against the new root CLAUDE.md and the repo's actual state; all are addressed, with one name-level residual under fix 4. Specifics: (1) CLAUDE.md now lives at the repo root and its source-of-truth paths resolve — specs/plan.md is v0.4, specs/decisions.md exists, the old Context_Runtime_v0.3.md/files/ layout is gone, and plan §31's tree now legitimizes plan.md/decisions.md/adr/acceptance/bench. (2) Current-stage section present and coherent: Stage 0 declared, sign-off criterion defined (stage-0.md record), lowest-N-without-record rule works against the empty acceptance/ dir. (3) Git pin fully reconciled at &gt;= 2.45 across CLAUDE.md, plan §12, decisions.md Toolchain pins, and ADR-006, with reftable as the recorded rationale and 2.38 kept as the merge-tree hard minimum; no 2.44 remains. (4) Pins header pointer is now honest — the decisions.md 'Toolchain pins' entry plus dedicated entries cover every substantive pin; only the literal tokens `pg` and `BlobStore` appear nowhere in decisions.md/plan (implied, not enumerated). (5) Frozen-commitment-vs-Stage-0-draft clarification present with the post-Stage-2 revision window, matching plan §32's language. (6) Future dirs labeled truthfully, Stage 0 parenthetical trimmed, environment blanks guarded, nothing-to-run note present. File is 81 lines, under its promised 100. Section citations were re-verified against v0.4's numbering (unchanged §1-§36; error-class sextet matches §26 line 1139 exactly). No new inconsistencies introduced by the fixes were found in CLAUDE.md.","Verified all Report 3 findings against the v0.4 doc set (specs/plan.md, CLAUDE.md, specs/decisions.md, specs/adr/000-009) and repo reality. 17 of 18 tracked items are fully addressed with exact, mutually consistent text: SHA-256 is unconditional in all three docs (C1); the frozen-vs-draft commitment/elaboration rule and the plan&gt;decisions&gt;CLAUDE.md precedence rule are in CLAUDE.md (C2, C3); §15's stale stage reference now points at Stage 4's gate (C4); the PatchOp rename question moved to Settled (C5); §31's tree gained bench/, adr/, acceptance/ and was trimmed to the LangGraph adapter (C7, scope); the Stage 2 auth stub, Stage 3 dialog-record and minimal-compaction-record deliverables, registered terminal projection, and Stage 5/first-breaking-change assignments for the §29 trace test and §30 upgrade-on-touch are all specified (S1, S4, S5, S7, S9); crypto-shredding is honestly descoped via ADR-003's blob-deletion + rewrite-ceremony redesign with per-subject encryption recorded as deferred (S8); the critical path to §33 is stated in §32; CLAUDE.md sits at the repo root with two convention-following commits and a clean tree (R1, with Environment blanks left for Ren by explicit design); and every requested OPEN-list addition landed, three of them resolved outright instead of left open. The single partial is C6: the OPEN-list header mismatches are fixed via per-item stage annotations, but §31's specs/ tree still lists sessions.md and wire-protocol.md that no stage assigns for writing, and the Level-0 turn-boundary OPEN item lacks a stage annotation. No fix was found to introduce a new cross-document inconsistency (checked §5 commit protocol vs turn anchors, §22 GC roots vs §14/§23, Git-version pins, blob-store pin vs Stage 8, and residual SHA-1/stage-number references by grep).","Fresh-eyes regression hunt over plan.md v0.4, decisions.md, CLAUDE.md, and ADRs 000–009 (all read in full). The v0.4 edits are largely sound: all 12 changelog claims are present in the body; no surviving text assumes optional retrievalSnapshot, time-prefix sharding, fast-import ref updates, v1 crypto-shredding, v1 sandboxed compilers (the §31/§36 kernel 'bundles·sandbox' labels read as end-state diagrams), or a four-adapter tree; cross-references (§ numbers, ADR pointers, §15's Stage-4 gate, §31's specs tree) all resolve; CLAUDE.md paths match repo reality and its Git 2.45/reftable pin now has recorded rationale. Eight NEW problems found, four major: (R-1) §13's commit bullet still states the v0.3 no-op rule (\\\"StateId equals parent's → nothing commits\\\") that edited §7/ADR-005 corrected — reintroducing the stranded-evidence bug in the normative pipeline; (R-2) turn anchoring (ADR-002) and the checkpointed write path (ADR-006) don't compose — nothing requires a checkpoint before the mid-turn anchor ref move, yet §12 says uncheckpointed fast-import objects are invisible, so recovery can find an anchor pointing at unreadable objects, or else per-turn-checkpoint cost claims are wrong; (R-3) §13's step() references an unbound `turn` variable and its comment claims intent anchoring that the code's ordering (bracket before any chain exists) cannot perform — the v0.3 C1 shape survives under a new comment; (R-4) §16/ADR-008's \\\"labeled `simulation` (§20's authority labels)\\\" cites an enum member §20's closed union does not contain. Four minors: stale \\\"beyond signed-bundle configuration\\\" phrasing in binding lists §34 and decisions.md contradicting ADR-009 (R-5); Stage 10 acceptance and the §33 drill still promise linearization from path-disjointness alone, missing ADR-004's compile-source/profile-scoping qualifier (R-6); Law 11 arrives at both Level 1 and Level 2 (R-7); §9's \\\"small trees, O(1) appends\\\" overclaims for unboundedly growing entropy shards whose fan-out ADR-007 now makes migration-expensive to change (R-8)."],"problems":[{"id":"M3","status":"partial","severity":"major","detail":"The mechanism is right: §7 redefines no-op as \"changes neither state nor record\" and introduces record-only nodes for effect intents and paid invocations (line 434), keeping StateId/memoization untouched; ADR-005 requires Store.commit to accept them; blob-GC gains the permanent-class root so §19's resultNodes-∅ invocations no longer strand evidence. BUT the fix was not propagated to §13's pipeline, which still states the v0.3 rule verbatim in effect: \"**commit**: if the resulting StateId equals the parent's, nothing commits. The no-op rule.\" (line 626). Read literally — and the pipeline 
... (truncated 59202 chars, full result in /private/tmp/claude-501/-Users-ren-repos-runtime/0d12c725-8d2a-4f05-9b71-22745c997f04/tasks/whus1j5fb.output)</result>
<diagnostics>Per-agent results: /Users/ren/.claude/projects/-Users-ren-repos-runtime/0d12c725-8d2a-4f05-9b71-22745c997f04/subagents/workflows/wf_6897c3ce-acf/journal.jsonl — one {"type":"result",...} line per completed agent with its full return value.
If the result above is empty or unexpected, Read this file BEFORE diagnosing — do not assume agents returned non-empty results.
To re-run with edited post-processing: Workflow({scriptPath: '/Users/ren/.claude/projects/-Users-ren-repos-runtime/0d12c725-8d2a-4f05-9b71-22745c997f04/workflows/scripts/verify-v04-absorption-wf_6897c3ce-acf.js', resumeFromRunId: 'wf_6897c3ce-acf'}) — agents whose (prompt, opts) are unchanged replay from cache.</diagnostics>
<usage><agent_count>4</agent_count><agents_done>4</agents_done><agents_error>0</agents_error><agents_skipped>0</agents_skipped><agents_empty_result>0</agents_empty_result><subagent_tokens>412989</subagent_tokens><tool_uses>69</tool_uses><duration_ms>549175</duration_ms></usage>
</task-notification>

---
[2026-08-07T10:34] session 0d12c725

"Follow the plan; don't outsmart it."

interesting, i think before we do this, we should spawn a few agents to try to outsmart it, find better ways to build it, or improve the structure and elegance, or whatever

how can we make our plan better or make a better plan?

---
[2026-08-07T10:37] session 0d12c725

review from gpt: Yes. This is substantially better. v0.1 had a powerful ontology with several distributed-systems holes; v0.4 feels like an actual runtime specification. The important thing is that most of the previous problems have not been patched locally—they have been absorbed into the model: Node ≠ State, Evidence as a fifth class, effect bracketing, realms, attested authority, transition footprints, explicit retention, and the component/host distinction now reinforce one another.
I would build from this. But I would make one more v0.5 pass before treating the ontology as stable after Stage 2. I see four genuine correctness issues and several smaller specification mismatches remaining.
Overall judgment
The strongest improvement is that the architecture now has a coherent causal decomposition:
[
\text{Being}
\rightarrow
\text{Compilation}
\rightarrow
\text{Computation}
\rightarrow
\text{Proposal}
\rightarrow
\text{Transition}
\rightarrow
\text{Being}
]
with external reality deliberately outside that closure:
[
\text{Transition}
\rightarrow
\text{EffectIntent}
\rightarrow
\text{World}
\rightarrow
\text{Observation}
\rightarrow
\text{Transition}
]
That is much cleaner than v0.1. The Being / Becoming / Encounter split is especially good, as is the decision to make the runtime an embeddable component rather than insisting that it own the agent loop.
The contemporary integration assumptions also check out: LangGraph JS currently exposes the `BaseCheckpointSaver`/`BaseStore` seam you intend to target, Google now has an official TypeScript ADK, and Assistant UI's current `AssistantTransport` is explicitly layered on `ExternalStoreRuntime`. So the adapter strategy is not based on imaginary seams. ([Docs by LangChain](https://docs.langchain.com/oss/javascript/langgraph/persistence?utm_source=chatgpt.com))
The remaining issues are these, in order of importance:

1. Realm belongs to an execution/binding, not intrinsically to a Node. The document simultaneously says `Node { realm: Realm }` and that only `refs/live` is live while every other ref is simulation. Those two statements cannot both define the same thing. A single historical node may be reachable from `refs/live`, forked under `refs/sim/foo`, and pinned by a replay session simultaneously. The node should instead record something like `originRealm` or `createdUnderRealm` as provenance. The effective `ExecutionRealm` must be resolved from `(universe, ref/binding, current operation)` by the kernel. Otherwise a historical node carrying `realm: live` becomes semantically confusing precisely where the realm mechanism is intended to protect you.
2. You now need to distinguish durability from publication. §5 says the visible ref CAS is “the semantic commit point” and “nothing before step 3 is real,” while §14 deliberately creates durable internal turn refs before the visible ref advances. The latter is correct; the former vocabulary is now obsolete. There are really two events:
[
\text{durable fact}
\neq
\text{published continuation}
]
An anchored effect intent is already canonical fact—it must be, because the world is about to be touched—but it has not yet become the visible continuation of `refs/live`. I would name these durability/recording and publication/advancement explicitly. Once you do, the cross-store protocol becomes much easier to reason about.
3. Turn anchoring must protect more than external effects. The document says a paid invocation with unchanged State creates a record-only node whose evidence “outlives everything,” but effect-free turns are not checkpointed/anchored until the final ref move. A crash after receiving a paid model response but before that checkpoint can therefore lose the record-only node. Likewise, an accepted user input or approval can exist operationally without yet being reachable semantically.
I would generalize the idea from an effect anchor to a turn journal anchor. Advance the private turn ref whenever an irrecoverable/non-regenerable fact has entered the runtime: accepted external input if acknowledged, completed model response, human approval, effect intent, effect receipt. The public ref still advances once, so turns remain atomic to normal observers. Internally, however, you stop pretending that nondeterministic evidence can be safely left in an uncheckpointed stream.
This would make the model beautifully regular:

```text
refs/live
    H
    │
    │     private durable journal
    │        ↓
    └──── input → invocation → intent → receipt → final
                                               │
                                               │ publish
                                               ▼
                                          refs/live

```

4. An anchored live effectful turn must become a hard sequencer barrier. This is the most dangerous remaining crash/concurrency case. Suppose T1 starts from live H, anchors an email intent, sends the email, and its worker dies. A replacement worker sees `refs/live = H` and advances a different turn T2 to B. T1 is later recovered—but its world effect has already happened and its final CAS `H → T1` can no longer succeed. You cannot simply send it to a simulation branch, because the physical world did not branch. The plan says recovery scans unfinished turn anchors before “completing or shelving” them, but I would turn that into an explicit invariant:
Once a live turn has crossed its first irreversible effect-intent boundary, that ref is fenced until the turn is resolved and published or a reconciliation transition explicitly absorbs it.
In other words, an unresolved live-world effect is a serialization barrier. Lease failover must recover it before the next live turn is admitted. This belongs in §14/§15 and in the Stage 4 kill drills.
5. Compilation invalidation is still too weak. v0.4 correctly repaired write-skew and now checks a model proposal against “what the model actually saw,” but checking only selected source paths is insufficient. Imagine retrieval returned memories A, B, and C; another turn adds memory X under the same searchable namespace. X may now rank above A and change the compiled projection even though none of A/B/C's paths changed. Likewise `list("tasks/**")` depends on the set of children, not merely the paths returned.
The compiler needs a CompilationFootprint, not merely a source list:

```ts
interface CompilationFootprint {
  stateReads: Selector[];       // prefixes/queries included
  selectedSources: SourceRef[];
  retrievalGeneration: RetrievalGeneration;
  authoritySnapshot: Digest;
  toolSetDigest: Digest;
}

```

Then your pinning rule becomes: an old model proposal can linearize only when the intervening history cannot have changed the compiled projection, not merely when it did not mutate selected items.
This also reveals that the current memoization key

```text
StateId × agent × requestHash × compilerDigest × retrievalSnapshot

```

is incomplete if effective grants/tool availability come from the kernel. Revoking a capability can change the tool context without changing `StateId`. Include the complete external compilation-input digest.
6. `retrievalSnapshot` is currently named more strongly than it is implemented. You define it as “a monotone index watermark plus config digest, a watermark, not a copy,” yet later evaluation relies on pinning it to make comparisons reproducible. A watermark only works as a snapshot if the retrieval system can actually query the historical generation. Otherwise it tells you which index produced the result without letting you reproduce that result.
I see two clean approaches. Either keep immutable/versioned index generations that are queryable by generation ID, or rename it `RetrievalGeneration` and rely on the compile evidence—which already stores the candidate/selected/rejected set—for exact replay. For model-A-vs-model-B evaluation, the simplest and strongest approach is often to reuse the exact same `CompiledContext` evidence rather than rerunning retrieval at all.
7. Some immutable evidence structures still contain backward references that cannot be immutable. `InvocationRecord.resultNodes` is the clearest example. The invocation has to exist before the resulting transition nodes can reference it; but if the immutable invocation blob already includes the node IDs produced afterward, you have a circular creation dependency.
Remove `resultNodes` from `InvocationRecord`. Let resulting transition records refer to `InvocationId`; the reverse relation is a derived index. Then:

```text
Invocation I
    ↓ referenced by
Transition T1
Transition T2

```

gives you `resultNodes(I)` by projection.
I would make the same correction to `Effect`. `phase: intended | dispatched | succeeded...` looks like mutable aggregate state. Prefer immutable facts:

```text
EffectIntent
DispatchAttempt      // operational
EffectObservation    // succeeded | failed | unknown

```

and derive the current Effect projection from them. That aligns perfectly with the rest of your ontology.
8. Conflict-bearing nodes need to appear in the core value type. §24 now allows unresolved conflicts to inhabit State, which I like. But `StateView.read()` still returns only `CanonicalValue | null`. That means your own Store API says contested values cannot exist while your Merge model says they can.
Decide now between:

```ts
type StateValue =
  | { kind: "resolved"; value: CanonicalValue }
  | { kind: "conflict"; conflict: ConflictRef };

```

and a separate canonical `state/conflicts/**` namespace with explicit behavior for the contested original path.
I prefer the first if “conflict is information” is truly a project law. It is more invasive, but honest: compiler, reducer, validator, projection, and index code must then consciously handle uncertainty instead of accidentally treating one side as truth.
9. `StateId` is still content identity, not semantic equivalence. This is mostly a wording correction, but an important one. “Equal meaning yields equal bytes” is stronger than canonical encoding can guarantee. Two semantically equivalent states may have different claim IDs, timestamps, provenance paths, or logically redundant records. What you genuinely have is:
Equal canonical structural content under the same encoding profile → equal StateId.
That is plenty. I would stop using “equal meaning” or calling byte-identical convergence semantic convergence. Call it structural convergence. Semantic equivalence can someday be a separate relation.
There is also one real cache issue here: the v1 `StateId` is just the `state/` tree OID, while schema/encoding version lives beside it in the Node. If identical bytes can ever be interpreted under two schema versions, the same `StateId` may mean two things. Either put a canonical state-format header inside the `state/` subtree or define StateId as something like:
[
H(\text{encodingVersion}\parallel\text{schemaVersion}\parallel\text{treeOid})
]
rather than the raw tree OID.
10. The Git write-path section has two concrete implementation mistakes worth fixing now. `git fast-import` cannot literally be used for “object creation only” when creating commits: its `commit` command requires a ref and creates/updates that branch, and `checkpoint` writes the current refs as well as finalizing the pack. Git's own documentation is explicit about both behaviors. ([Git](https://git-scm.com/docs/git-fast-import))

The architecture is still fine; just describe the implementation truthfully:

```text
fast-import
    → writer-private refs/internal/import/<writer>
    → checkpoint
    → objects + private staging ref durable
    → update-ref <public-ref> <new> <expected-old>  // semantic/public CAS

```

Hide those refs from advertisement and treat them as operational/recovery roots. `update-ref` does indeed provide the expected-old-value CAS semantics you want. ([Git](https://git-scm.com/docs/git-update-ref.html?utm_source=chatgpt.com))
More importantly, `core.fsync=committed,reference` does not by itself guarantee the power-loss semantics the prose claims on every platform. Git documents that `committed` covers objects and `reference` covers refs, but also documents that the default `core.fsyncMethod` on macOS is `writeout-only`, which may not survive a system crash. If the invariant is “an acknowledged head cannot disappear after power loss,” explicitly configure/test `core.fsyncMethod=fsync` or a proven equivalent on the deployment filesystem. ([Git](https://git-scm.com/docs/git-config))
Your SHA-256 caution is otherwise justified: current Git documents `compatObjectFormat` interoperability as still incomplete. ([Git](https://git-scm.com/docs/git-config))

11. Your canonical-JSON profile is not literally RFC 8785. This is easy to fix in wording. RFC 8785 deliberately says Unicode strings are preserved as-is and does not perform Unicode normalization; JCS also emits the canonical JSON representation without formatting whitespace. Your additional NFC normalization and trailing LF are perfectly reasonable choices, but they make this a Context Runtime canonical JSON profile built on JCS, rather than raw RFC-8785 bytes. ([RFC Editor](https://www.rfc-editor.org/rfc/rfc8785.html?utm_source=chatgpt.com))

I would specify:

```text
CR-CJSON/1:
  input strings NFC-normalized at ingestion
  then RFC 8785 serialization
  then LF framing for repository files

```

Now encoding versioning has a concrete name and future migration target.

12. Level 0 still overclaims the laws it satisfies. This is perhaps the main conceptual weakness introduced by the “component before application” move. A LangGraph checkpointer can give a host immutable snapshots, forks, diffs and history. It cannot guarantee Law 1—“if it determines continuation, it lives in State”—because the host may assemble prompts from arbitrary state outside Context Runtime. Nor can it guarantee complete Evidence if model calls are performed outside the runtime. The document already says the compiler is optional and tools are host-owned, so the law table contradicts that honesty.

I would define adoption guarantees as scoped guarantees:

```text
L0  versioned persistence for runtime-managed snapshots
L1  transactional semantics for runtime-managed mutations
L2  world/authority guarantees for runtime-routed effects
L3  complete continuation semantics

```

Only Level 3 can plausibly assert the full “complete state over what determines this agent's continuation” claim.

13. Promotion says “re-execution” but still partly describes adoption. Applying a simulated branch's “net state change” directly onto live is essentially state adoption. Consider a simulation where a mock purchase succeeded and caused tasks, beliefs, and plans downstream to change. The net diff cannot simply be applied and then the purchase re-executed. Promotion must be more like transition-aware replay/reconciliation:


```text
simulation intent/history
        │
        ▼
derive promotion proposal
        │
reconcile with current live head
        │
revalidate pure transitions
re-observe simulation-derived claims
re-authorize/reapprove effects
execute effects
        │
        ▼
fresh live trajectory

```

Some pure artifacts may copy directly. Some claims remain `simulation`. Some transitions must rerun. Some should disappear. I would give promotion a policy registry just as you did merge.

14. Evidence has two small internal contradictions. You correctly say evidence is the actual provider response/exact bytes seen, but also say it is “redacted at ingest.” Once scrubbed, it is no longer the actual payload. And you say reconstructable/auditable/replayable are guaranteed “always,” while invocation responses are `standard` evidence that may later be physically deleted. After deletion, replay is no longer possible.

I'd say:
Evidence records are canonical; evidence payload availability is retention-scoped.
And choose explicitly between exact sealed raw evidence and sanitized evidence. A good design may retain a sanitized canonical representation plus an optionally encrypted raw payload under a stricter retention/access class. Don't call scrubbed bytes exact.

15. Read authority should appear in the API, not just the prose. You say another agent's private memory is unreadable “at the `StateView`,” but the current Store exposes `view(state): StateView` without a principal or read scope. A caller holding it can seemingly read any path. Likewise `Claim.sources` appears able to carry authority labels, which would let an untrusted writer claim `"operator"` provenance unless those labels are derived rather than trusted.

I would have a trusted raw store view and a runtime-issued scoped view:

```ts
RawStateView       // Store/kernel internals
ScopedStateView    // principal + read capability + realm

```

Reducers and compilers receive only the latter. Provenance records store origins; the runtime derives authority from authenticated provenance, just as it derives effective capability instead of trusting state to self-grant it.

16. The one-page loop needs the first transition moved forward. Right now it compiles `head.state` with an ephemeral `input`, while §25 says accepted user content becomes a canonical dialog observation. The causal chain should really be:


```text
H
↓ accept(input)
I                   ← input is now canonical
↓ compile(I.state)
invocation
↓ proposal
...

```

In a detached turn this does not make the user message publicly visible prematurely. It simply means the model is genuinely continuing from a State that contains the observation it is responding to. Combined with the generalized private turn anchor above, this produces a very clean causal model.
There are a few smaller things I would fix while touching these sections. The claim that “records are write-once by design” does not fit mutable per-task files under `tasks/**`; claims/dialog records are write-once, but entities such as tasks clearly have new versions at stable paths. `git push` does not replicate the agent's “entire existence” because evidence payloads live in the blob store—the triple export does. A bounded schema-reader horizon still needs permanently retained migration readers or proactive migration before an old parser is removed. And exact budget enforcement should not depend solely on a disposable Postgres rollup: if remaining budget controls whether the agent is permitted to act, the authoritative consumption counter belongs either in State or in the external authority/kernel plane.
What I would change architecturally
I don't think you need a tenth fundamental object. That is actually a good sign.
I think v0.4 has discovered almost all of the correct primitives. The remaining work is mostly sharpening relations between them. The architecture I now see is:

```text
                         UNIVERSE

              materialized causal trajectory graph
                              │
                              ▼
                        ┌───────────┐
                        │   NODE    │
                        │ StateId   │
                        │ Record    │
                        │ Parents   │
                        └─────┬─────┘
                              │
                ┌─────────────┴─────────────┐
                ▼                           ▼
              STATE                       RECORD
          "what continues"             "what happened"
                │                           │
                │                     evidence refs
                ▼                           │
          COMPILATION                       │
                │                           │
                ▼                           │
          COMPILED VIEW                     │
                │                           │
                ▼                           │
           INVOCATION ──────────────────────┘
                │
                ▼
             PROPOSAL
                │
                ▼
           TRANSITION
                │
          ┌─────┴──────┐
          │            │
       pure state    effect intent
          │            │
          │            ▼
          │          KERNEL
          │            │
          │            ▼
          │           WORLD
          │            │
          │      effect observation
          └────────────┴───────► NODE

```

And surrounding it:

```text
ExecutionBinding =
    Universe
  + Ref/Node
  + EffectiveRealm
  + Principal
  + AttestedCapabilities

```

I think that last equation is the missing abstraction that resolves several remaining ambiguities without needing to become another fundamental domain object.
Where I think the plan is now
v0.1 was: “this is a compelling architecture.”
v0.4 is: “this is probably buildable.”
With the corrections above, I would be comfortable treating v0.5 as the architecture to execute rather than continuing to redesign it abstractly. In particular, I would not reopen Git-vs-database, TypeScript-vs-Rust, Session-vs-State, canonical-memory-vs-index, or framework-ownership questions unless Stage 1/2 measurements actually falsify them. Those decisions now fit together.
The highest-priority v0.5 ADRs, in my view, are execution realm vs origin realm; durable journal vs public publication; live-effect fencing; compilation dependency footprints; immutable invocation/effect records; and conflict-valued State. After those, I think the remaining uncertainty belongs where it should belong: in implementation measurements and experience, not in the ontology.

---
[2026-08-07T10:48] session 0d12c725

<task-notification>
<task-id>wdn37oq3z</task-id>
<tool-use-id>toolu_01FhqzpVpaXaziSMSvyhmu2c</tool-use-id>
<output-file>/private/tmp/claude-501/-Users-ren-repos-runtime/0d12c725-8d2a-4f05-9b71-22745c997f04/tasks/wdn37oq3z.output</output-file>
<status>completed</status>
<summary>Dynamic workflow "Design competition: six challengers attack the plan’s foundational bets, six judges score their proposals" completed</summary>
<result>{"domains":[{"domain":"substrate","challenge":{"proposals":[{"title":"Own the Merkle store: a ~1,000-line content-addressed DAG on SQLite per universe; Git demoted to an export format","targets":"plan §5 (commit protocol), §11–12, §14 (turn-anchor mechanics), §22 (erasure, GC), §32 Stages 1 and 8, §34 item 1; specs/adr/002, 003, 006; decisions.md 'Git as the first Store implementation' and the Git/reftable/SHA-256 pins (/Users/ren/repos/runtime/specs/plan.md, /Users/ren/repos/runtime/specs/decisions.md, /Users/ren/repos/runtime/specs/adr/006-store-write-path.md)","change":"Rewrite §12: one SQLite file per universe (WAL mode) is the Store. Tables: objects(hash PRIMARY KEY, kind, size, data — zstd-compressed, content-addressed by the runtime's canonical Merkle encoding), refs(name, head) where move() is `UPDATE refs SET head=:to WHERE name=:ref AND head=:expected` inside a transaction, turn_anchors(turn_ulid, tip) written in the same transaction as the intent commit. PatchOp values are stored as leaf objects and referenced by hash from the transition record, never embedded twice. packages/store implements tree codec, recursive diff, structural three-way merge, and LCA/bases as pure functions (~800–1,000 lines, fast-check property-tested; verify-by-hash in §13 cross-checks every commit forever). The filesystem blob CAS stays for &gt;64 KiB payloads; one mark-and-sweep collector covers db objects and fs blobs. Erasure of inline canonical bytes becomes the same operation as blob erasure: replace the value object's payload with a typed `redacted` placeholder keyed by the original hash — the hash chain survives, reads resolve typed-absent, and because patches reference values by hash, an erasure touches exactly one object; ADR-003's successor-universe rewrite ceremony is deleted. Add `runtime export --git &lt;dir&gt;`: stream any universe (or ref subset) into a real Git repo via fast-import with the same commit topology and §8 trailers — fast-import's non-CAS refs and visibility semantics are harmless in an exporter. Stage 3 / Level 0 acceptance 'readable with plain git log' runs against the export. Stage 1's probe shrinks to: SQLite commit-transaction latency at production shape, diff/merge/LCA at 100k commits, the same two writer crash drills, GC sweep correctness.","rationale":"Engaging decisions.md's rationale item by item. (1) 'Immutable Merkle DAG, structural sharing, ancestry, CAS refs': the plan uses perhaps 5% of Git and v0.4 had to patch every one of these — CAS refs needed ADR-006 (fast-import refs aren't CAS, refs aren't fsynced by default), visibility needed checkpoint-per-turn and turn-anchor refs (ADR-002), immutability needed the rewrite ceremony carve-out (ADR-003), and identity needed encoding-versioning (ADR-007). Four of the eight substantive v0.4 ADRs are Git-impedance repairs; that is the signal, priced. (2) 'Worktree-free merge-tree': the only Git algorithm genuinely reused — and only its tree-structural layer, because the plan itself concedes RFC 8785 makes line merge useless (§24) and reimplements semantic merge in the runtime; the residual is ~300 lines of recursive map three-way, covered by Stage 9's already-planned merge fuzzing. (3) 'Universal tooling': already half-surrendered — SHA-256 repos can't push to GitHub (decisions.md accepts this), bare repos of sharded canonical-JSON ULIDs aren't browsable, and every tool that matters (node inspector, why-compiled, ThreadProjection) is custom regardless; the export preserves `git log` on demand. (4) 'Clone-based replication': the plan's own export format is already a triple (bundle + blob manifest + pg dump) because Git alone was never sufficient; `VACUUM INTO`/file copy/Litestream on one file per universe is strictly simpler. (5) 'Validated by the Stage 1 load probe, not assumed': the probe gates on performance, but the real cost of Git is standing choreography — subprocess protocol client, stream lifecycle and failover, checkpoint/repack/gc/reftable/fsync configuration — which the probe cannot fail on; Git will likely pass the probe and the ceremony is then kept forever. (6) §34's 'no custom Git implementation': this builds a content-addressed map plus a DAG, not Git — no packfiles, no wire protocol, no index, no line merge — and the plan already commits to a custom CAS blob store with its own GC, a custom structural merge, a custom canonical encoding, and a NodeId system; the genuinely new surface is the tree codec and LCA. Finally, the embeddable-library positioning (§3) currently requires every Level 0 host to carry a Git ≥2.45 binary with reftable and fsync configuration; `npm install` plus one .db file is a categorically better adoption story.","simplifies":"Deletes: the fast-import client and stream lifecycle, checkpoint choreography and small-pack repack scheduling, commit-graph/bitmap/multi-pack-index operations, core.fsync and reftable and Git-version pins, the SHA-256-repo decision and its GitHub-mirror concession, turn-anchor ref mechanics (ADR-002's mechanism becomes one row in the intent's transaction), ADR-003's rewrite ceremony and the erasure `subject` blob-tier workaround, the grace-window GC root class for db-resident payloads (blob upload and reference become one transaction), and the leased writer's stream-failover dance (the lease stays; the stream doesn't exist). Stage 1 shrinks; Stage 8's hardest acceptance item disappears.","costs":"Ren owns data-integrity risk that Git's decades-hardened ODB currently absorbs — a store bug corrupts an agent's life; mitigated but not eliminated by the §13 verify-by-hash law on every commit, SQLite as the durability substrate (the fsync/atomicity part is delegated, and it is better-tested than the v0.4 fast-import/update-ref composition, which is itself novel), and the Git export as an independent integrity cross-check. Loses packfile delta compression across similar records (zstd with trained dictionaries recovers much; §18 says evidence, outside Git, dominates storage anyway). 'git log on your agent's life' becomes on-demand rather than ambient — a real demo/positioning loss. Spec rework at Stage 0: rewrite §12, amend §5/§14/§22, supersede ADR-006, amend ADR-002/003; new pin (better-sqlite3 or node:sqlite). Zero code exists, so no migration — this is the last cheap moment to decide.","confidence":"high"},{"title":"StateId is a runtime-computed canonical Merkle hash from v1 — promote ADR-007's 'natural v2' and un-qualify Law 3","targets":"plan §8, §10, §13 (verify), §35 Law 3; specs/adr/007; Stage 0's canonical-encoding.md scope (/Users/ren/repos/runtime/specs/plan.md, /Users/ren/repos/runtime/specs/adr/007-stateid-encoding-versioned.md)","change":"canonical-encoding.md defines a store-independent Merkle: leaf hash = SHA-256 over the record's RFC 8785 bytes; interior hash = SHA-256 over the sorted (logical path segment, child hash, kind) list; StateId = the root hash of the *logical* tree — shard fan-out is declared a physical-layout concern excluded from identity. Computed incrementally during §13's verify (rehash only the changed paths' ancestor chains, O(changed × depth)). Recorded in transition.json and the commit trailer; the map to the store's native id (Git tree OID today) becomes a rebuildable projection, cross-checked as a Stage 1–2 acceptance assertion.","rationale":"ADR-007 rejected this for v1 as 'a second full hash pass' — that objection is overstated: verify already re-applies every patch, and the rehash is incremental over the patch, not the tree. What v1-adoption buys is that the 'Store interface is the firewall' claim becomes fact instead of aspiration: ADR-007's own consequence today is that a store swap 'preserves the ontology and the API, not recorded ids' — i.e., the firewall does not protect the thing users accumulate. With a runtime hash, a store swap or a shard-fan-out change is a data move, not an identity migration, and Law 3 loses its 'within a store encoding' asterisk. If proposal 1 is adopted, 
... (truncated 147815 chars, full result in /private/tmp/claude-501/-Users-ren-repos-runtime/0d12c725-8d2a-4f05-9b71-22745c997f04/tasks/wdn37oq3z.output)</result>
<diagnostics>Per-agent results: /Users/ren/.claude/projects/-Users-ren-repos-runtime/0d12c725-8d2a-4f05-9b71-22745c997f04/subagents/workflows/wf_514a6d02-4ef/journal.jsonl — one {"type":"result",...} line per completed agent with its full return value.
If the result above is empty or unexpected, Read this file BEFORE diagnosing — do not assume agents returned non-empty results.
To re-run with edited post-processing: Workflow({scriptPath: '/Users/ren/.claude/projects/-Users-ren-repos-runtime/0d12c725-8d2a-4f05-9b71-22745c997f04/workflows/scripts/outsmart-the-plan-wf_514a6d02-4ef.js', resumeFromRunId: 'wf_514a6d02-4ef'}) — agents whose (prompt, opts) are unchanged replay from cache.</diagnostics>
<usage><agent_count>12</agent_count><agents_done>12</agents_done><agents_error>0</agents_error><agents_skipped>0</agents_skipped><agents_empty_result>0</agents_empty_result><subagent_tokens>938878</subagent_tokens><tool_uses>121</tool_uses><duration_ms>724092</duration_ms></usage>
</task-notification>

---
[2026-08-08T08:04] session 0d12c725

still not sure about the git choice, but agree with demotion

I need you to think about this more, and why use sqlite instead of postgres since we are already using it? and if we use database, git export and related functions can delay.  Also, after we build this, provide a claude web like interface that just works, allow multi user use with assistant ui as frontend, is still within the future roadmap

---
[2026-08-08T08:25] session 0d12c725

<task-notification>
<task-id>wfvdy18ni</task-id>
<tool-use-id>toolu_01NssomQ64qX7XjZQih3MBdR</tool-use-id>
<output-file>/private/tmp/claude-501/-Users-ren-repos-runtime/0d12c725-8d2a-4f05-9b71-22745c997f04/tasks/wfvdy18ni.output</output-file>
<status>completed</status>
<summary>Dynamic workflow "Adversarial analysis: Postgres vs SQLite vs Git as the canonical Merkle store, under the new multi-user roadmap constraint" completed</summary>
<result>{"positions":{"all-postgres":{"position_summary":"Canonical storage lives in Postgres. The v1 stack is Node + one Postgres 16 + the filesystem blob CAS — nothing else, no Git binary, no SQLite. This is not a third novel design: it is the plan's own recorded fallback-of-record (\"all-Postgres content-addressed store\", decisions.md/§12), promoted on exactly the evidence the competition used to demote Git, plus the constraints that postdate the SQLite verdict. Everything the competition proved collapses under a transactional store — intent + outbox + projection + event append in one commit, erasure as one audited placeholder write, ADR-002 anchoring as a row, the §28 barrier deleted — collapses identically under Postgres, with one decisive difference: sessions, events, jobs, leases, FTS, and pgvector were ALWAYS going to live in Postgres (§5 authority matrix, §26, §28), and the firm multi-user hosted roadmap guarantees Postgres arrives regardless. SQLite-per-universe therefore buys its one-transaction elegance only until the second user exists, then reopens every seam it deleted — the competition's own P4 text concedes \"the multi-process server eventually reintroduces Postgres.\" Choosing Postgres now means the semantic commit transaction spans the ENTIRE system with zero cross-store seams, at solo scale and at hosted scale, forever. The store-agnostic Merkle codec and runtime-computed StateId (v0.5 Tier 1 #4) make the engine's only job durability + transactions + refs — precisely the surface where Postgres WAL recovery is the most battle-tested option on the table. Git export is deferred per Ren's constraint (2), same work item under every database option. The embedding loss is real but overstated: LangGraph's own production checkpointer is PostgresSaver and LangGraph Platform runs on Postgres — \"bring a connection string\" is the incumbent norm for exactly the hosts the plan targets — and PGlite is the credible future zero-server adapter sharing the same SQL dialect.","key_arguments":["SEAM COUNTING, END-STATE HONEST. Under all-Postgres, one BEGIN...COMMIT spans chain objects + effect-outbox row + turn-open row + node-index projection + claim projections + session-event append + ref CAS. GPT-2's invariant 'durable before acknowledged' becomes a transaction property across the WHOLE system, not just the store. Under SQLite-per-universe, v1 already needs a second database (competition P4: sessions/jobs/event log in an app-level SQLite 'until a second process exists') and the multi-user milestone — which Ren has declared a firm roadmap item, not a hypothetical — reintroduces Postgres, splitting the event log, sessions, and projections back out of the commit transaction. The seams the SQLite verdict celebrated deleting return at exactly the moment the product becomes real. Count them: SQLite end-state = SQLite fleet + Postgres + blob CAS (two engines forever, cross-engine event/commit ordering discipline back); Postgres end-state = Postgres + blob CAS, zero returning seams.","THIS IS THE PLAN'S OWN FALLBACK, NOT A REOPENING. decisions.md and §12 name 'an all-Postgres content-addressed store' as the fallback-of-record behind the Store firewall; WF effects P1 — independently adopted by the judges — is the Postgres transactional outbox. The competition established that Git's price is standing choreography and that a transactional store collapses four ADRs into one mechanism; nothing in that argument is SQLite-specific. Promoting the recorded fallback on the competition's own evidence is the conservative move; introducing a second database engine the stack never contained is the radical one.","THE CODEC MAKES THE ENGINE'S JOB SMALL, AND POSTGRES IS BEST AT EXACTLY THAT JOB. With v0.5 Tier 1 #4 (runtime-computed StateId over the logical tree) and the pure-TS Merkle codec (hash, diff, LCA, structural merge) identical under every option, the store supplies only durability, atomicity, CAS refs, and queries. The kill -9 drills then land on Postgres WAL crash recovery — the most exercised recovery path in the industry — versus better-sqlite3 WAL discipline inside a Node process, versus the v0.4 fast-import/update-ref/fsync composition that the v0.3 review found bugs in before code existed. Integrity ownership of the codec is Ren's under all three options; durability ownership is most delegated under Postgres.","THE MULTI-USER ROADMAP IS SERVED NATIVELY, NOT EVENTUALLY. Concurrent sequencers across universes are MVCC row traffic in one engine (one writer per ref remains a lease discipline, now enforceable atomically: the ref-CAS UPDATE carries the fencing token in the same transaction as the lease check — Tier 1 #3's fencing stops being cross-system choreography). Row-level security keyed on universe_id gives the hosted product tenant isolation the engine enforces. LISTEN/NOTIFY wakes SSE fan-out for §26's event log, which the plan already specifies as Postgres-resident with Last-Event-ID resume. FTS and pgvector sit beside canonical tables, so Tier 1 #11's retrieval basis watermark is a same-engine, same-snapshot comparison instead of a cross-store wait. Nobody ships a Claude-web-like hosted product on a fleet of SQLite files without building a database on top of them; Postgres IS that database, available from Stage 1.","LEVEL 0 REALITY CHECK (VERIFIED): the flagship host already demands Postgres in production. LangGraph's production-grade checkpointer is PostgresSaver/AsyncPostgresSaver (langgraph-checkpoint-postgres on PyPI, @langchain/langgraph-checkpoint-postgres on npm), and self-hosted LangGraph Platform requires DATABASE_URI (Postgres) for checkpoints/threads plus Redis for streaming. 'Point the adapter at the Postgres you already run for PostgresSaver' is a BETTER adoption pitch than 'adopt my bespoke .db file format'. The npm-install-only story SQLite wins is the casual-trial tier — which Tier 4's own resequencing demotes to post-demo ('web when a second user exists').","OPS IS ONE STORY, WORKED CONCRETELY. Solo v1: nightly pg_dump (the whole cluster is small) plus optional WAL archiving; one daemon, one data directory, one thing to monitor. Hosted: pg_basebackup + WAL archiving = point-in-time recovery for every universe at once, or a managed Postgres and the problem is outsourced. Per-universe export is a runtime command COPYing canon.* rows where universe_id=$u plus the blob manifest — the export 'triple' becomes a pair. Contrast: Git needed bundle + blob manifest + pg dump (three artifacts, §12); SQLite-per-universe needs N files × (WAL checkpoint schedule, integrity check, backup job) PLUS the app database PLUS later Postgres. Also: §28's cost rollups and any ops dashboard span universes — plain SQL in one engine, a bespoke aggregation layer over a file fleet.","SOLO-V1 COST IS A BREW-INSTALL SWAP, NOT AN ADDITION. The Git plan already put Postgres on the Stage 1 write path — §12: 'One writer, leased. The sequencer worker holds a Postgres lease per universe', and the probe 'runs the production shape' — while CLAUDE.md schedules postgresql@16 at Stage 2; that is a latent inconsistency in the current plan. All-Postgres resolves it: brew install postgresql@16 at Stage 1 (fresh initdb; Stage-1 data is disposable, no pg_upgrade from 14), and DELETE the Homebrew git ≥ 2.45 pin, the reftable pin, the SHA-256-repo decision, and the fast-import lifecycle. Net pins decrease.","EVERY WIN THE SQLITE VERDICT CLAIMED SURVIVES INTACT. Erasure of inline canonical bytes = one audited UPDATE swapping a value object's bytes for a typed placeholder, transition-recorded per the judges' condition (d) — ADR-003's rewrite ceremony stays deleted. Turn anchoring = a turn_open row in the intent's transaction — ADR-002's mechanism stays deleted. The §28 projection barrier and the acknowledged-commit/unlanded-projection crash class stay deleted (projection is in-transaction). The dual-write ordering gap between anchor and operational journal stays deleted. The composition co
... (truncated 89425 chars, full result in /private/tmp/claude-501/-Users-ren-repos-runtime/0d12c725-8d2a-4f05-9b71-22745c997f04/tasks/wfvdy18ni.output)</result>
<diagnostics>Per-agent results: /Users/ren/.claude/projects/-Users-ren-repos-runtime/0d12c725-8d2a-4f05-9b71-22745c997f04/subagents/workflows/wf_b4f48399-4ff/journal.jsonl — one {"type":"result",...} line per completed agent with its full return value.
If the result above is empty or unexpected, Read this file BEFORE diagnosing — do not assume agents returned non-empty results.
To re-run with edited post-processing: Workflow({scriptPath: '/Users/ren/.claude/projects/-Users-ren-repos-runtime/0d12c725-8d2a-4f05-9b71-22745c997f04/workflows/scripts/substrate-postgres-vs-sqlite-wf_b4f48399-4ff.js', resumeFromRunId: 'wf_b4f48399-4ff'}) — agents whose (prompt, opts) are unchanged replay from cache.</diagnostics>
<usage><agent_count>5</agent_count><agents_done>5</agents_done><agents_error>0</agents_error><agents_skipped>0</agents_skipped><agents_empty_result>0</agents_empty_result><subagent_tokens>403134</subagent_tokens><tool_uses>104</tool_uses><duration_ms>892632</duration_ms></usage>
</task-notification>

---
[2026-08-08T08:56] session 0d12c725

<task-notification>
<task-id>w9chxq6xs</task-id>
<tool-use-id>toolu_01DJ5t8EtsE6taepwDR4aYwo</tool-use-id>
<output-file>/private/tmp/claude-501/-Users-ren-repos-runtime/0d12c725-8d2a-4f05-9b71-22745c997f04/tasks/w9chxq6xs.output</output-file>
<status>completed</status>
<summary>Dynamic workflow "Verify plan v0.5 + decisions.md + CLAUDE.md + ADRs: coverage of the approved package, internal consistency, cross-doc agreement" completed</summary>
<result>{"summaries":["COVERAGE CHECK of plan v0.5 + decisions.md + CLAUDE.md + ADRs against the approved package (specs/reviews/v0.5-proposals.md and the judge's 9 spec_implications in substrate-analysis.json). Verdict: the package landed essentially intact — 37 of 43 checked items fully covered, 5 partial, 1 missed, none above minor severity. Every structural commitment is present and quotable: all Tier-2 all-Postgres mechanics (canon/proj/ops split, fenced CAS and outbox and event log in one transaction, turn-journal row, append-only trigger with audited gc_sweep/redact, basis watermark, re-based probe with both kill -9 drills and targets bound to specs/acceptance/stage-1.md, SQLite fallback with flip condition, Git exporter deferred with verify-by-hash + golden-vector compensation, postgresql@16 at Stage 1 in both CLAUDE.md and §32), all of Tier 3, the Tier-4 resequencing with all three judge amendments, both rejects in decisions.md, and 16 of 19 Tier-1 invariants verbatim-or-stronger. The six gaps, all minor spec-text omissions rather than design drift: (1) T1-17 — \\\"CapScope gains `models?` + budget\\\" lost its landing spot because v0.5 dropped the CapScope sketch entirely; (2) T1-10 — the Python-sidecar bet is not re-priced; §3 and decisions.md retain the v0.4 \\\"the protocol exists for them\\\" framing without the adopted \\\"later format/spec play, not a near-term sidecar play\\\" concession; (3) T1-05 — \\\"auxiliary shapes encoding-versioned\\\" (encoding-version field on Commit/Diff) is unstated; (4) T4-05 — the observation-class-effect measurement (the one spike-first item) is neither a probe line item nor recorded as mooted; (5) T2-07 — the LISTEN/NOTIFY commit-serialization caveat is only half-noted (escape named, caveat and polling omitted); (6) SAL-01 — the approved salvage of the rejected laws-compression (derivation annotations on Laws 8 and 18) is missing. All six are one-to-three-line fixes in plan.md/decisions.md.","Internal-consistency audit of specs/plan.md v0.5 (all 1404 lines read; every §-reference, every Stage-N mention, and the loop/schema/fence mechanics cross-checked; two suspected stale references verified against the v0.4 text in git history). The document is internally coherent on everything load-bearing: the old substrate is genuinely gone (no checkpoints, fsync choreography, declared footprints, Node.realm, nine objects, optional retrievalSnapshot, projection barrier, or rewrite ceremony — each is either absent or present only as an explicit deletion), §-cross-references all resolve correctly including reciprocal pairs, the §5/§11/§13/§14/§15 commit-outbox-fence-publish protocol composes against the §12 schema, the §31 tree matches every package named in prose, and the three renumbering decisions (demo at end of Stage 6, sessions Stage 8, thread Stage 9) hold at every mention. Ten defects found, all minor wording-level, none architectural. The two worth fixing first: (1) the changelog and §13 date observed-footprint OCC to Stage 10 while §14/§32/§33 activate it at the end-of-Stage-6 demo; (2) changelog item 1 claims the semantic commit is 'one transaction' spanning outbox through ref CAS, which §5's own two-transaction protocol — the premise of the fence — contradicts. The rest: a stale v0.4 'Stage 5' reference in §29, a dangling 'trailer conventions' reference in the Git exporter line, sim/ missing from the canon.refs schema comment, an ambiguous turn-journal write placement (§11 open vs §5 mid-turn step), Law 1 retaining pre-Frame wording that §19's headline contradicts, the §13 loop leaving the pre-compile observation commit implicit against §25's requirement, a §30 conformance-window claim absent from Stage 0's deliverables, and the v0.4 term 'footprint selectors' surviving in §9.","CHECK 3 (cross-document agreement): the document set is in strong agreement — CLAUDE.md's every claim (sections, stage definition, pins, environment, testing) matches plan v0.5 and decisions.md; 15+ decisions.md settled entries match their cited sections including all-Postgres/§12, serial-per-ref/§14, CR-CJSON/§10, coverage-contracts/§3; ADR-002..010 status lines match the plan (no internal-ref anchoring survives; §8 is ADR-007's promoted form); all 15 ADR-010 points are realized; OPEN-list owners match §32; git grep finds zero stale paths. Four defects: (major) ADR-001, marked plain \\\"accepted\\\", still says workspace scaffolding lands at Stage 1 \\\"not before\\\", contradicting §32 Stage 0 (\\\"Workspace tooling ... arrives here\\\") and CLAUDE.md — misleading for the current stage; (minor) ADR-001's SHA-256-universe-repo consequence references a pin ADR-010 deleted, with no status flag; (minor) plan §3 line 153 uses bare `StateView`, a type v0.5 no longer defines (§11 has only ScopedStateView); (minor) decisions.md's deferred section cites \\\"(plan §34)\\\" for per-subject envelope encryption, which is deferred only in §22.","Fresh-eyes distributed-systems review of plan.md v0.5's new mechanisms (§5, §8, §12–16, §22, §26, §28) found 1 critical, 7 major, and 4 minor defects, all grounded in exact text; 4 pressed mechanisms held. The critical finding: the fence is checked only at the publication CAS while the law it implements regulates dispatch — a stalled worker can dispatch a durable intent after failover reconciliation has absorbed its turn (email double-send via the plan's own unknown-and-escalate path), and a turn admitted during occupation dispatches before its CAS can discover the conflict. Supporting majors: the fence token's minting/increment discipline is unspecified and the sketched `fence &lt; $token` predicate wedges consecutive publications under one lease (or stops identifying stale holders); the occupation predicate is unimplementable because canon.turns has no ref binding and open() takes a NodeId; erasure-by-object-replacement collaterally redacts other subjects' identical bytes since inline values dedup on (universe_id, hash) with no subject namespace — §18's never-delete-another's-bytes guarantee covers only blobs; crashed-turn 'paid evidence survives' has no GC root once the turn closes; §26's publication-only event append deadlocks or contradicts the approval/EffectIntended bracket-visibility claim; the proj event log is claimed rebuildable yet holds canon-less events and authoritative Last-Event-ID sequences; and the incremental re-hash leaves delete/empty-node pruning and shard/un-shard thresholds undefined — StateId divergence across conforming implementations. Minors: the append-only-canon trigger contradicts the protocol's own refs/turns UPDATEs; the 'one transaction' headline overstates (any effectful turn spans two-plus transactions per §5's own protocol); basis ≥ requested is undefined on a DAG with basis collapsed to a single NodeId; and the LISTEN/NOTIFY commit-serialization caveat the judge required is only half-recorded."],"problems":[{"id":"T1-05","status":"partial","severity":"minor","detail":"Logical paths everywhere (\"Paths are logical — consumers ... never see physical storage\") and durability as interface obligation (\"`commit` returns only after the transaction is durable\") both landed. But the third sub-item, \"auxiliary shapes encoding-versioned\" (substrate P3: \"adding an encoding version field to Commit and Diff is a one-line hardening\"), is nowhere stated — §11 says only \"`Commit`, `MergeRequest`, `Diff`, and friends are finalized as zod schemas in `packages/domain` at Stage 0\", with no encoding-version requirement, and the old decisions.md 'Store auxiliary shapes' OPEN item was dropped rather than closed with this condition.","location":"specs/plan.md §9 (line 327), §11 (lines 414-419)"},{"id":"T1-10","status":"partial","severity":"minor","detail":"AdoptionManifest, the real BaseCheckpointSaver contract (getTuple/list/put/put_writes/channel_versions/versions_seen/get_next_version/delete_thread), superstep→turn \"(settled)\", and the partial-superstep resume drill in Stage 3 
... (truncated 34372 chars, full result in /private/tmp/claude-501/-Users-ren-repos-runtime/0d12c725-8d2a-4f05-9b71-22745c997f04/tasks/w9chxq6xs.output)</result>
<diagnostics>Per-agent results: /Users/ren/.claude/projects/-Users-ren-repos-runtime/0d12c725-8d2a-4f05-9b71-22745c997f04/subagents/workflows/wf_47d446b6-6c3/journal.jsonl — one {"type":"result",...} line per completed agent with its full return value.
If the result above is empty or unexpected, Read this file BEFORE diagnosing — do not assume agents returned non-empty results.
To re-run with edited post-processing: Workflow({scriptPath: '/Users/ren/.claude/projects/-Users-ren-repos-runtime/0d12c725-8d2a-4f05-9b71-22745c997f04/workflows/scripts/verify-v05-wf_47d446b6-6c3.js', resumeFromRunId: 'wf_47d446b6-6c3'}) — agents whose (prompt, opts) are unchanged replay from cache.</diagnostics>
<usage><agent_count>4</agent_count><agents_done>4</agents_done><agents_error>0</agents_error><agents_skipped>0</agents_skipped><agents_empty_result>0</agents_empty_result><subagent_tokens>444452</subagent_tokens><tool_uses>63</tool_uses><duration_ms>586992</duration_ms></usage>
</task-notification>

---
[2026-08-08T09:43] session 0d12c725

I asked gpt 5.6 to do a deep review over this plan, wdyt:
## Verdict
No—not yet the most elegant architecture for a framework-neutral context engine. But the foundation is unusually strong, and I would preserve roughly 80% of it.
The right move is a targeted v0.6 correction before Stage 0/1, not a rewrite:
- Keep the Node/State split, immutable causal history, Continuation Frame, Postgres substrate, effect bracket, binding-derived realms, attested authority, replay, and conflict-as-data.
- Rework the engine boundary, exact invariants, redaction model, concurrency scope, portability contracts, and stage ordering.
- Remove the assertion that all ontology uncertainty is resolved; several remaining issues are contract-level, not implementation-level ([plan.md:8](/Users/ren/repos/runtime/specs/plan.md:8)).
| Question | Assessment |
|---|---|
| Elegant conceptual model? | Yes—very strong. |
| Most elegant implementation boundary? | Not yet. It mixes causal substrate, agent cognition, safety, and product assumptions. |
| Context engine for other frameworks? | Yes, conditionally. The adapter/protocol contract needs strengthening first. |
| Robust today? | Good failure philosophy, but several P0 invariant gaps remain. |
| Can grow 5–10 years without a rewrite? | Yes if corrected before the Store/public schemas freeze; otherwise boundary and migration rewrites are likely. |
## What is already excellent
The most durable decisions are:
- Being versus Becoming and Node versus State. These are clean, general abstractions with real operational value ([plan.md:70](/Users/ren/repos/runtime/specs/plan.md:70), [plan.md:246](/Users/ren/repos/runtime/specs/plan.md:246)).
- State versus Continuation Frame. This correctly distinguishes persisted being from current authority, realm, tools, retrieval, and execution conditions ([plan.md:745](/Users/ren/repos/runtime/specs/plan.md:745)).
- Postgres as the first canonical substrate. One transactional engine is the correct decision for the hosted roadmap; I would not reopen Git or SQLite as primary storage ([plan.md:430](/Users/ren/repos/runtime/specs/plan.md:430)).
- Canonical/evidential/operational/derived separation ([plan.md:161](/Users/ren/repos/runtime/specs/plan.md:161)).
- Effects modeled as intent → world → observation, with uncertainty represented honestly ([plan.md:588](/Users/ren/repos/runtime/specs/plan.md:588)).
- Realm on the execution binding rather than the historical node ([plan.md:622](/Users/ren/repos/runtime/specs/plan.md:622)).
- Authority attested outside the mutable state tree ([plan.md:664](/Users/ren/repos/runtime/specs/plan.md:664)).
- Replay-first development, projection rebuild drills, property tests, and explicit deferrals ([plan.md:1113](/Users/ren/repos/runtime/specs/plan.md:1113), [plan.md:1302](/Users/ren/repos/runtime/specs/plan.md:1302)).
- Structural merge below domain merge, with disagreement preserved as data ([plan.md:931](/Users/ren/repos/runtime/specs/plan.md:931)).
These are not the likely sources of a future rewrite.
## P0 issues to fix before freezing Stage 0/1
### 1. Frame staleness is internally contradictory
The frame digest includes the entire `StateId` ([plan.md:751](/Users/ren/repos/runtime/specs/plan.md:751)), but admission says a ref may advance while the frame digest remains unchanged when the model’s projection is unaffected ([plan.md:550](/Users/ren/repos/runtime/specs/plan.md:550)). Any state-changing advancement changes `StateId`, so that fast path cannot work.
There is also a second hole: authority, tools, retrieval, or realm can change while the ref does not. Admission currently receives the original frame, so revocation does not necessarily invalidate an in-flight state proposal.
Use three separate identities:
- `FrameDigest`: exact provenance/evidence identity.
- `CompilationDependencyWitness`: selectors read, prefix memberships, retrieval revision, authority epoch, realm, tools, runtime and availability epoch.
- `CompiledContextDigest`: exact bytes supplied to the model.
Validate current external dependencies on every admission, not only when the ref moved. Validate state dependencies against an advanced head using the witness. Keep reducer read traces as a separate OCC check.
### 2. Authorization happens before the actual write set exists
The pipeline is `authorize → reduce → verify`, but the reducer creates the patch after authorization ([plan.md:496](/Users/ren/repos/runtime/specs/plan.md:496), [plan.md:515](/Users/ren/repos/runtime/specs/plan.md:515)). Since declared write footprints were removed, authorization cannot yet know the exact paths or blob namespaces being modified. Hash verification does not close that gap.
Change it to:
```text
validate proposal
→ pre-authorize kind/input
→ reduce through scoped reads
→ authorize exact patch + effect plan
→ verify invariants/hash
→ re-attest at commit
→ commit
```
The Stage 2 self-grant test should include a reducer that attempts to write outside its authorized prefix.
### 3. Inline redaction breaks content addressing
`canon.objects` maps a hash to the bytes identified by that hash ([plan.md:438](/Users/ren/repos/runtime/specs/plan.md:438)). Redaction later replaces those bytes beneath the original hash ([plan.md:903](/Users/ren/repos/runtime/specs/plan.md:903)). That is no longer a content-addressed store.
It also creates a cognition bug: StateId and FrameDigest stay unchanged, so a compiled-context cache may still return erased data.
For v1, the simplest robust rule is:
- Never mutate bytes underneath a content hash.
- Make erasable/subject-tagged payloads indirect from admission—preferably mandatory BlobRefs or encrypted payload envelopes.
- Keep availability/redaction in a separate authenticated ledger.
- Add an availability/redaction epoch to compilation dependencies.
- Redact derived compiled contexts and other evidence containing the subject.
- Make `ErasureNamespaceId` independent. “One universe → one namespace” conflicts with later subject-specific erasure ([plan.md:224](/Users/ren/repos/runtime/specs/plan.md:224)).
Backup/WAL restore must also be tested for redaction resurrection.
### 4. Effect guarantees exceed what external APIs can prove
The plan correctly admits that many providers cannot query by idempotency key and recovery commonly ends in `unknown` ([plan.md:611](/Users/ren/repos/runtime/specs/plan.md:611)). But Level 2 and the demo promise no double charge and “the world is touched once” ([plan.md:147](/Users/ren/repos/runtime/specs/plan.md:147), [plan.md:1289](/Users/ren/repos/runtime/specs/plan.md:1289)).
Acceptance must be executor-class-specific:
| Executor class | Honest guarantee |
|---|---|
| Provider-enforced idempotency | Same key cannot cause a second effect. |
| Queryable outcome | Reconcile before retry. |
| Non-idempotent, non-queryable | Never retry automatically; record `unknown` and escalate. |
| Reversible | Record compensation semantics, not transactional rollback. |
Also, `Proposal` currently has no proposal ID even though deduplication and effect keys depend on it ([plan.md:280](/Users/ren/repos/runtime/specs/plan.md:280), [plan.md:496](/Users/ren/repos/runtime/specs/plan.md:496)).
### 5. Live-effect reservation needs one atomic invariant
Before an intent is recorded, the transaction must assert:
```text
ref.head == turn.base
AND ref.fence == lease.token
AND no incompatible open/reserved turn exists
```
Then the intent, outbox row, and reservation must be inserted atomically. The schema sketch currently does not express one-open-turn-per-ref, intent uniqueness, legal effect-fact transitions, or proposal deduplication ([plan.md:438](/Users/ren/repos/runtime/specs/plan.md:438)).
Approval should not create an effect intent before approval exists. Otherwise a human approval delay can occupy the live ref indefinitely. Publish an approval-request fact/node, allow cancellation or expiry, and revalidate head, authority, payload, and projection after approval.
### 6. The hash and value ABI is not fully specified
The StateId formula leaves `H`, tuple framing, segment encoding, sort collation, and algorithm tagging unspecified ([plan.md:301](/Users/ren/repos/runtime/specs/plan.md:301)). Plain concatenation without length framing can be ambiguous across implementations. Typed numeric objects also need a reserved namespace so normal user JSON cannot accidentally impersonate `$dec` or `$int`.
Stage 0 must freeze:
- algorithm-tagged digests;
- exact length-prefixed hash preimages;
- path segment encoding, normalization, limits and ordering;
- typed-tag reservation/rejection rules;
- Unicode runtime/version conformance;
- required `ProposalId`/`OperationId`;
- language-neutral golden fixtures and JSON Schema.
There is also an internal type gap: `StateValue` can be contested, but `PatchOp.put` accepts only `CanonicalValue`; the merge engine therefore cannot materialize the contested state it promises ([plan.md:407](/Users/ren/repos/runtime/specs/plan.md:407), [plan.md:496](/Users/ren/repos/runtime/specs/plan.md:496), [plan.md:952](/Users/ren/repos/runtime/specs/plan.md:952)).
## Architectural reframe for framework neutrality
The six-object ontology can remain, but it should not all be one frozen package boundary.
```text
Public surfaces
  domain ABI · adapter SPI · ContextEngine SDK
Cognition profile
  ModelInvocation · ContinuationFrame · compiler · memory · domain merge
Safety profile
  Effect · ExecutionBinding · capabilities · approvals · reconciliation
Causal kernel
  Universe · Node · State · Transition/commit records
  durable publication batches · refs · structural diff/merge · replay
Ports
  RuntimeStore · BlobStore · EffectDriver · ExecutionDriver
```
The key change is to make a core “turn” a generic durable publication batch. A resident agent turn and a framework superstep become profiles over that batch rather than storage primitives.
This avoids forcing every framework to adopt the reference runtime’s notions of chat, compiler categories, memory, or orchestration.
### Portability contracts currently missing
- The Store must be explicitly universe-scoped. Its methods omit `UniverseId` even though storage identity is composite ([plan.md:392](/Users/ren/repos/runtime/specs/plan.md:392), [plan.md:438](/Users/ren/repos/runtime/specs/plan.md:438)).
- The Store transaction port must cover the actual semantic transaction: objects, node/record facts, turn state, effect facts, durable core events, transactional projections and fenced ref CAS.
- Separate the Engine Protocol from the Encounter/session protocol. The only proposed wire envelopes require `sessionId`, despite Encounter being outside the core ([plan.md:101](/Users/ren/repos/runtime/specs/plan.md:101), [plan.md:1058](/Users/ren/repos/runtime/specs/plan.md:1058)).
- Add `HostCheckpointCodec` for exact opaque round-tripping. Semantic decomposition should be an optional adapter lens; otherwise Level 0 cannot safely promise edit/diff/merge for arbitrary host checkpoints ([plan.md:135](/Users/ren/repos/runtime/specs/plan.md:135)).
- Make `AdoptionManifest` a versioned capability matrix rather than assuming every integration is a monotonic Level 0→3 progression.
- Add a static `DomainModule` registry for namespaced schemas, reducers, migrations, merge policies and compiler sources. This is ordinary application composition, not the deferred dynamic plugin/self-modification system.
- Define `EffectDriver` and `ExecutionDriver`. The plan says the host owns tool execution while the kernel dispatches effects, and promises a future `LocalExecutionEngine` swap without defining the interface ([plan.md:115](/Users/ren/repos/runtime/specs/plan.md:115), [plan.md:1261](/Users/ren/repos/runtime/specs/plan.md:1261)).
- Prove the seam with two contrasting micro-hosts: one checkpoint-shaped and one loop/event-shaped. This is more valuable than building many full adapters.
With those changes, it can genuinely be the context engine beneath other frameworks. Without them, it will likely be an excellent TypeScript resident runtime with a LangGraph adapter.
## Long-term growth issues
These should be addressed in the contracts now, while implementation remains deferred:
- Hide Merkle sharding from semantic paths. `memory/claims/<id>` should be public; shard/trie structure should be encoding-internal. Current sharding leaks storage into capability paths and identity ([plan.md:319](/Users/ren/repos/runtime/specs/plan.md:319)).
- Use per-ref leases/fences. One writer per universe contradicts the serial-per-ref model and the thousands-of-agents north star ([plan.md:474](/Users/ren/repos/runtime/specs/plan.md:474)).
- Separate Universe from tenant ownership, erasure namespace, export policy and lease scope. They may default 1:1 in v1.
- Replace retrieval’s bare `NodeId` basis with `(ref, refEpoch, publicationRevision, nodeId)` or a source frontier. A NodeId does not support the promised `basis ≥ requested` comparison ([plan.md:791](/Users/ren/repos/runtime/specs/plan.md:791), [plan.md:1105](/Users/ren/repos/runtime/specs/plan.md:1105)).
- Split encoding, state schema, record schema, protocol, projector schema and bundle/runtime versions. One upgrade-on-touch paragraph is not enough ([plan.md:1127](/Users/ren/repos/runtime/specs/plan.md:1127)).
- Put destructive branch TTLs and session pins in durable authoritative records, not disposable `proj`; otherwise GC policy cannot be reconstructed safely ([plan.md:893](/Users/ren/repos/runtime/specs/plan.md:893), [plan.md:925](/Users/ren/repos/runtime/specs/plan.md:925)).
- Replay should compare record hashes, topology, frames, compiled bytes, authorization decisions, effect plans, read traces and exact tape consumption—not only StateIds ([plan.md:1119](/Users/ren/repos/runtime/specs/plan.md:1119)).
- Keep most internal packages private initially. “Everything under packages ships as libraries” creates unnecessary compatibility obligations for a solo project ([plan.md:1169](/Users/ren/repos/runtime/specs/plan.md:1169)).
## Rework the implementation sequence
The current sequence contains hard dependency and scope problems:
- Stage 1 claims a production-shape probe involving components not implemented until later stages ([plan.md:1185](/Users/ren/repos/runtime/specs/plan.md:1185)).
- Stage 3 introduces the compiler, provider integration, evidence, dialog, compaction, terminal host, DAG rendering and LangGraph together ([plan.md:1197](/Users/ren/repos/runtime/specs/plan.md:1197)).
- Real provider keys arrive before the model-egress authority gate ([plan.md:1211](/Users/ren/repos/runtime/specs/plan.md:1211), [plan.md:1219](/Users/ren/repos/runtime/specs/plan.md:1219)).
- Stage 4 implements promotion using three-way domain reconciliation, but that merge machinery is not built until Stage 6 ([plan.md:1217](/Users/ren/repos/runtime/specs/plan.md:1217), [plan.md:1229](/Users/ren/repos/runtime/specs/plan.md:1229)).
- GC is introduced in Stage 1 and again in Stage 7.
- Stage 11 has no acceptance criteria.
A leaner sequence is:
1. Exact portable ABI: paths, codec/hash, IDs, values/conflicts, version axes, manifests and conformance vectors.
2. Thin end-to-end causal slice: Postgres objects/nodes/refs, one atomic publication, traced reducer, replay, deterministic fake model, fork/diff.
3. Portability gate: adapter SPI, opaque checkpoint codec, LangGraph plus one contrasting micro-host.
4. Context usefulness: compiler/evidence/memory with a minimal real-model egress capability.
5. Branch semantics: domain merge, contested values and OCC.
6. Safety in three gates: bindings/authority; effect fencing/reconciliation matrix; approvals and promotion after merge.
7. Retention, GC, export, disaster recovery and capacity work on real traces.
8. Encounter/web/multi-user when product demand exists; Temporal only after an executable engine conformance suite exists.
## Current repository status
The repository is clean and the tooling passes:
- `pnpm test`
- `pnpm typecheck`
- `pnpm check`
But the implementation remains a scaffold: [packages/domain/src/index.ts](/Users/ren/repos/runtime/packages/domain/src/index.ts:1) exports nothing, and [harness.test.ts](/Users/ren/repos/runtime/packages/domain/test/harness.test.ts:1) only verifies the test libraries work. None of the architectural guarantees has executable evidence yet.
My recommendation is to write one focused boundary/correctness ADR and revise the Stage 0 acceptance criteria before implementing the domain model. That should be a v0.6 refinement, not a reset.

---
[2026-08-08T10:15] session 0d12c725

<task-notification>
<task-id>wiigbkx12</task-id>
<tool-use-id>toolu_0164tnMQAyjLejac1kxa1Xxb</tool-use-id>
<output-file>/private/tmp/claude-501/-Users-ren-repos-runtime/0d12c725-8d2a-4f05-9b71-22745c997f04/tasks/wiigbkx12.output</output-file>
<status>completed</status>
<summary>Dynamic workflow "Verify plan v0.6 absorbed the deep review without new incoherence" completed</summary>
<result>{"summaries":["CHECK A coverage verdict on plan v0.6 (/Users/ren/repos/runtime/specs/plan.md) against specs/reviews/v0.5-gpt3.md: 25 of 29 checked review items are fully absorbed with exact textual anchors; every P0's substantive fix is present, correctly cross-referenced (§5/§12/§13/§14/§15/§20/§22), and wired into stage acceptance. Four defects, all residue rather than substance: (1) MAJOR — the clean-paths fix is contradicted by stale shard-bearing paths in the very sections implementers will read: §21 'memory/claims/&lt;shard&gt;/&lt;ulid&gt;' (l.930) and §25 'dialog/&lt;shard&gt;/&lt;ulid&gt;' (l.1078), against §9's 'never shard segments' and decisions.md's own 'Rejected: shard segments in public paths'; (2) minor — §33's replay drill (l.1350) still says 'identical StateIds, zero providers', the exact weakened comparison §29 now rejects; (3) minor — subject-tag blob-indirection is 'mandatory routing, not advice' in §22 but §9 (l.362) and decisions.md (l.45) still say 'may be blob-stored'; (4) minor — the review's 'OperationId' (v0.5-gpt3.md l.38) appears nowhere and its disposition is unrecorded in ADR-011. One new issue: stale v0.5 'footprint' wording for the compiler's output at l.905 and l.1258 collides with v0.6's OCC sense of the word. All four ADR-011 declines (profile reframe, capability matrices, 8-stage resequence) are properly recorded in ADR-011 and decisions.md. Fixes are line-level edits; no structural rework needed.","CHECK B on specs/plan.md v0.6 (read in full, 1489 lines): the correction landed cleanly in its primary sections (§5, §12, §14, §15, §19-20, §22 all agree on the witness, the ledger, per-ref leases, (ref,position) basis, approvals-before-intents, and promotion-at-Stage-6), but 13 grounded inconsistencies survive. Three are contract-level (major): the §13 one-page loop still authorizes before reduce with a 'staleness' comment and no authorize-patch/verify step, contradicting the corrected pipeline directly above it (line 571); §28 still lists 'branch metadata &amp; TTLs' in proj, contradicting §23's destructive-inputs-are-durable rule (line 1152); and §9 says subject-tagged records 'may' be blob-stored while §22 declares that rule 'mandatory routing, not advice' (362 vs 955). Two more majors are missed shard-segment scrubs: `memory/claims/&lt;shard&gt;/&lt;ulid&gt;` in §21 (930) and `dialog/&lt;shard&gt;/&lt;ulid&gt;` in §25 (1078), plus §20's algorithm still says 'emit footprint and record' (905). Minor stragglers: the v0.5 changelog's present-tense 'frame staleness is the only admission check' (51), §2's 'validated, authorized, reduced' ordering (106), Stage 3's 'from the footprint' (1258), §33's StateId-only replay assertion (1350), an epoch type split (bigint in canon.availability vs Digest in the witness, 493 vs 879), the open()-refusal predicate qualified by effect-intent in §14 but unconditional in §12/§5's schema (610 vs 487/221), and the SchemaVersion-includes-encoding phrasing blurring §30's axes split. Eleven checked areas came back clean, including witness field agreement (§14↔§20), ApprovalRequested's home (§5↔§15↔§26), trie vocabulary (§8↔§9↔Stage 0), promotion staging, and all cross-references.","CHECK C on the v0.6 revision: the cross-doc skeleton is sound (amended decisions.md entries match plan v0.6; the settled block matches ADR-011; CLAUDE.md's v0.6 reference and Stage 0 definition hold; ADR-010/011 precedence is stated; the availability ledger composes with GC; approval revalidation catches a moved head; recovery's record-only publication is consistent with the reservation predicate). Four major defects survive adversarial reading: (1) the approval-before-intent claim (\\\"occupies nothing\\\") contradicts the one-open-turn-per-ref partial UNIQUE plus §26's mid-turn ApprovalRequested — an overnight approval does block the live ref unless the requesting turn closes first, which no text says; (2) §21/§25 still write `&lt;shard&gt;` into public paths, contradicting v0.6 change #8, §9, and decisions.md; (3) CLAUDE.md's Testing section still mandates the StateId-only replay assertion that §29/ADR-011 explicitly rejected; (4) the `contest` op writes contested values into hashed state but the Stage-0-frozen ABI defines no canonical encoding or fixture for them, making a later addition an encodingVersion migration. Five minors: §9/decisions.md's permissive \\\"may be blob-stored\\\" vs §22's mandatory blob-indirect rule; ledger epoch bigint vs witness availabilityEpoch Digest; the unstated universe-wide invalidation blast radius of an epoch bump; decisions.md omitting ADR-011 item 5's atomic reservation predicate; §33's leftover \\\"identical StateIds\\\" drill line."],"problems":[{"id":"P0-3-subject-tag-mandatory","status":"partial","severity":"minor","detail":"§22 states the upgrade — 'data whose subjects must be independently erasable is blob-indirect from admission — the §9 subject-tag rule is mandatory routing, not advice' — but the two texts it points at were never updated: §9 (l.362) still reads 'A record tagged with an erasure subject MAY be blob-stored regardless of size', and decisions.md l.45 still reads 'a subject-tagged record may be blob-stored regardless of size'. A reader of §9 or the older settled block sees permission where §22 declares obligation; the mandatory rule exists only where §22 asserts it about §9.","location":"/Users/ren/repos/runtime/specs/plan.md l.362 vs l.955; /Users/ren/repos/runtime/specs/decisions.md l.45"},{"id":"P0-6-operationid","status":"missed","severity":"minor","detail":"The review names two ids: 'typed-tag ($-key) reservation, ProposalId/OperationId, language-neutral fixtures' (v0.5-gpt3.md l.38). ProposalId landed; 'OperationId' appears nowhere in plan v0.6, decisions.md, or ADR-011 — grep confirms zero hits. effect_id/InvocationId plausibly subsume it, but no document records that disposition, so it is silently dropped rather than absorbed or declined.","location":"/Users/ren/repos/runtime/specs/reviews/v0.5-gpt3.md l.38; absent from /Users/ren/repos/runtime/specs/plan.md and specs/adr/011-v06-correction.md"},{"id":"LT-clean-paths-trie","status":"partial","severity":"major","detail":"The normative fix landed (§9: consumers 'see memory/claims/&lt;ulid&gt;, never physical storage and never shard segments'; trie 'never appears in a path, a scope, or a merge pattern'; decisions.md even records 'Rejected: shard segments in public paths') — but two normative sections still state the rejected layout: §21 l.930 'Claims live at memory/claims/&lt;shard&gt;/&lt;ulid&gt; and never change' and §25 l.1078 'an observation transition writing dialog/&lt;shard&gt;/&lt;ulid&gt;'. These are the definitive location statements an implementer of Stages 5 and 3 will read, and they directly contradict v0.6 change #8.","location":"/Users/ren/repos/runtime/specs/plan.md l.930 and l.1078 vs l.350; /Users/ren/repos/runtime/specs/decisions.md l.40-41"},{"id":"LT-replay-comparisons","status":"partial","severity":"minor","detail":"§29 is fully fixed ('asserting identical record hashes, topology, frame digests, compiled bytes, authorization decisions, effect plans, and read traces, with exact tape consumption; StateId equality alone would let divergence hide in the records') — but the §33 demo drill l.1350 still carries the pre-fix claim the review attacked: 'replay the whole demo from the tape → identical StateIds, zero providers'. The demo line asserts exactly the weakened comparison §29 now forbids treating as sufficient.","location":"/Users/ren/repos/runtime/specs/plan.md l.1350 vs §29 (l.1170)"},{"id":"NEW-footprint-terminology","status":"new-issue","severity":"minor","detail":"The P0-1 rename left two compile-side uses of the old word: §20's v1 algorithm step 5 'redact at the boundary; label authority; emit footprint and record' (l.905) and Stage 3's 'why N57 (compiled context: selected &amp; rejected, from the footprint)' (l.1258). Everywhere else v0.6 deliberately reserves 'footprint
... (truncated 17155 chars, full result in /private/tmp/claude-501/-Users-ren-repos-runtime/0d12c725-8d2a-4f05-9b71-22745c997f04/tasks/wiigbkx12.output)</result>
<diagnostics>Per-agent results: /Users/ren/.claude/projects/-Users-ren-repos-runtime/0d12c725-8d2a-4f05-9b71-22745c997f04/subagents/workflows/wf_0125cbf1-0e3/journal.jsonl — one {"type":"result",...} line per completed agent with its full return value.
If the result above is empty or unexpected, Read this file BEFORE diagnosing — do not assume agents returned non-empty results.
To re-run with edited post-processing: Workflow({scriptPath: '/Users/ren/.claude/projects/-Users-ren-repos-runtime/0d12c725-8d2a-4f05-9b71-22745c997f04/workflows/scripts/verify-v06-wf_0125cbf1-0e3.js', resumeFromRunId: 'wf_0125cbf1-0e3'}) — agents whose (prompt, opts) are unchanged replay from cache.</diagnostics>
<usage><agent_count>3</agent_count><agents_done>3</agents_done><agents_error>0</agents_error><agents_skipped>0</agents_skipped><agents_empty_result>0</agents_empty_result><subagent_tokens>311620</subagent_tokens><tool_uses>29</tool_uses><duration_ms>426438</duration_ms></usage>
</task-notification>

---
[2026-08-08T11:08] session 0d12c725

<task-notification>
<task-id>woq5y3xv3</task-id>
<tool-use-id>toolu_014Eqzbu4rX8rUUV6FCVe6uN</tool-use-id>
<output-file>/private/tmp/claude-501/-Users-ren-repos-runtime/0d12c725-8d2a-4f05-9b71-22745c997f04/tasks/woq5y3xv3.output</output-file>
<status>completed</status>
<summary>Dynamic workflow "Adversarial review of the Stage 0 executable domain spec: ABI soundness, plan fidelity, RFC conformance" completed</summary>
<result>{"confirmed":[{"title":"Sparse arrays pass admission and serialize to invalid JSON that gets hashed","severity":"major","file":"/Users/ren/repos/runtime/packages/domain/src/value.ts","claim":"admitAt's array branch (value.ts:71) uses Array.prototype.map, which skips holes, so a sparse array's holes never reach the 'unsupported type' check (value.ts:86) and admission succeeds; jcs's `value.map(jcs).join(\",\")` (cjson.ts:17) then converts each hole to an empty string, emitting bytes that are not JSON at all, and leafHash/frame happily hash and frame them. This violates the CR-CJSON/1 contract (§10: canonical bytes are RFC 8785 JSON) and makes decodeFramed(frame(v)) partial for admitted v.","failure":"Verified by execution: admit([1,,3]) succeeds; jcs of the result is the string \"[1,,3]\" (invalid JSON); leafHash computes a valid digest over it; decodeFramed(frame(admit([1,,3]))) throws SyntaxError. A reducer that ever produces a sparse array (e.g. `const a = []; a[2] = x`) commits a leaf with a valid StateId whose stored bytes can never be decoded — verify passes, the object is permanently unreadable. JSON.parse can never produce a hole, so no golden vector or JSON-sourced test can catch it.","verdict":{"real":true,"reasoning":"Reproduced every step of the claim by executing the package's own compiled code (node --input-type=module against packages/domain/dist/src): admit([1,,3]) succeeds because value.ts:71 uses Array.prototype.map, which never visits holes, so the hole bypasses the 'unsupported type' check at value.ts:86 and the admitted value remains sparse; jcs(admitted) returns the literal string \"[1,,3]\" because cjson.ts:17's value.map(jcs).join(\",\") renders the hole as an empty string, and JSON.parse rejects that string; leafHash (tree.ts:28) computes a valid sha256 digest over the non-JSON framed bytes with no guard; decodeFramed(frame(admitted)) throws SyntaxError, so frame/decodeFramed fails to round-trip an admitted value. No caller applies the Zod CanonicalValue schema on this path (grep confirms zero parse/safeParse usages), and no test mentions sparse arrays — and since JSON.parse cannot produce array holes, the golden ABI vectors and all JSON-sourced tests structurally cannot catch it. Spec contradiction is exact: plan.md §10 defines CR-CJSON/1 serialization as RFC 8785 (JCS), whose output is by definition valid JSON, and states representation is part of the content-addressed identity contract. Severity major is justified: a reducer producing a sparse array commits a leaf with a valid StateId whose bytes are permanently undecodable in an ABI frozen at Stage 0."}},{"title":"Structural CanonicalValue lets unadmitted values into the hashed tree — StateId splits on identical canonical content","severity":"major","file":"/Users/ren/repos/runtime/packages/domain/src/patch.ts","claim":"The zod CanonicalValue schema (value.ts:25-34) is purely structural — no NFC, no well-formedness, no $-key reservation, no -0 folding — and PatchOp (patch.ts:21,26) uses it directly, so PatchOp.parse/applyPatch/rootHash accept and hash values that admission would reject or rewrite. CanonicalValue is also unbranded, so nothing in the type system records whether a value passed admit(). This contradicts §10 exactly: 'Same canonical content, same identity' and 'keys beginning $ are reserved... rejected at admission'. The exported PatchOp/StateValue JSON Schemas (part of the frozen ABI per §8) codify the structural-only definition for second implementations.","failure":"Verified by execution: PatchOp.parse({op:'put',path:'a',value:{'$evil':1}}) succeeds; PatchOp.parse accepts the non-NFC string 'é', the lone surrogate '\\ud800', and -0. Applying put of 'é' vs the NFC-equal 'é' through applyPatch and rootHash yields two DIFFERENT StateIds for the same canonical content — the exact identity split §10 exists to forbid. (zod v4 does reject NaN/Infinity, so only the string/-0/$-key axes are open.)","verdict":{"real":true,"reasoning":"Confirmed by execution via a scratch vitest run against /Users/ren/repos/runtime/packages/domain (deleted after; tree clean). Reproduced: (1) PatchOp.parse accepts {$evil:1}, non-NFC strings, lone surrogate \"\\ud800\", and -0, all of which admit() rejects or rewrites; (2) the decisive §10 violation — NFC-equivalent values pushed through Patch.parse → applyPatch → stateId produce two different StateIds (sha256:ae13c7… vs sha256:67a7ac…) for the same canonical content; (3) zod v4 does reject NaN/Infinity, matching the finding's caveat. Refutation attempts failed: the \"admission is a separate layer\" defense collapses because (a) the exported schemas/PatchOp.schema.json — part of the frozen ABI per §8 — codifies the structural-only value definition; (b) patch.test.ts itself hashes Patch.parse output without admit(), freezing that pattern; (c) path.ts enforces the identical §10 constraints in-schema (branded), so the value-side gap is an asymmetry, not intended layering; (d) NFC is not closed under concatenation, so even honest reducers can emit non-NFC patch values, and no check exists anywhere in parse/apply/hash (grep confirms admission logic lives only in value.ts/path.ts). One precision note: the -0 axis is acceptance-only — JCS serializes -0 as \"0\", so StateIds for -0 vs 0 are equal; identity does not split on that axis (the finding only claimed acceptance there, so it stands as written). Verification also surfaced two corroborating holes: a malformed $contested ({alternatives:[]}) passes the contest op's key-presence-only isContested gate into the hashed tree (contradicting §8's canonical-contested rule), and lone surrogates hash via U+FFFD replacement, aliasing \"\\ud800\" with \"�\" under one StateId while decodeFramed round-trips to a different value. Severity \"major\" is warranted: the identity invariant §10 exists to guarantee is violated through the only state-mutation door the spec defines, and the defect is codified in the frozen ABI artifacts a second implementation would build from."}},{"title":"Prototype-chain `in` check falsely rejects any key that exists on Object.prototype","severity":"major","file":"/Users/ren/repos/runtime/packages/domain/src/value.ts","claim":"The post-NFC duplicate-key check `if (key in out)` (value.ts:80) tests the prototype chain of a plain `{}`, so every key that names an Object.prototype member — toString, constructor, valueOf, hasOwnProperty, isPrototypeOf, propertyIsEnumerable, toLocaleString, __proto__, __defineGetter__, etc. — is reported as 'duplicate key after NFC' and admission throws. §10 reserves only '$'-prefixed keys, so these are admissible; a conforming second implementation (the ABI's stated goal, §8) admits and hashes {\"toString\":1} while this one rejects it — a frozen cross-implementation divergence on the admissible domain. Note for the fix: switching to Object.hasOwn alone is insufficient, because the assignment `out[key] = ...` (value.ts:81) hits the Object.prototype __proto__ setter — verified: it silently drops the key and rewrites the output object's prototype — so the accumulator must be Object.create(null) or a Map.","failure":"Verified by execution: admit({toString:1}), admit({constructor:'Acme'}), admit({hasOwnProperty:true}), and admit(JSON.parse('{\"__proto__\":1}')) all throw AdmissionError('duplicate key after NFC: ...'). Real-world JSON with a 'constructor' field (common in code-analysis or serialized-class payloads) fails admission for no spec reason.","verdict":{"real":true,"reasoning":"Reproduced by executing the package's own compiled code: admit({toString:1}), admit({constructor:'Acme'}), admit({hasOwnProperty:true}), admit(JSON.parse('{\"__proto__\":1}')), and a nested {a:{valueOf:2}} all throw AdmissionError('duplicate key after NFC: ...'), while a control plain key admits. Root cause is value.ts:77-80: the accumulator is a plain {} and the check uses `key in out`, which consults Object.prototype. specs/plan.md (§10, line 400) reserves only '$'-pre
... (truncated 80861 chars, full result in /private/tmp/claude-501/-Users-ren-repos-runtime/0d12c725-8d2a-4f05-9b71-22745c997f04/tasks/woq5y3xv3.output)</result>
<diagnostics>Per-agent results: /Users/ren/.claude/projects/-Users-ren-repos-runtime/0d12c725-8d2a-4f05-9b71-22745c997f04/subagents/workflows/wf_b294cbfc-60c/journal.jsonl — one {"type":"result",...} line per completed agent with its full return value.
If the result above is empty or unexpected, Read this file BEFORE diagnosing — do not assume agents returned non-empty results.
To re-run with edited post-processing: Workflow({scriptPath: '/Users/ren/.claude/projects/-Users-ren-repos-runtime/0d12c725-8d2a-4f05-9b71-22745c997f04/workflows/scripts/review-domain-abi-wf_b294cbfc-60c.js', resumeFromRunId: 'wf_b294cbfc-60c'}) — agents whose (prompt, opts) are unchanged replay from cache.</diagnostics>
<usage><agent_count>31</agent_count><agents_done>31</agents_done><agents_error>0</agents_error><agents_skipped>0</agents_skipped><agents_empty_result>0</agents_empty_result><subagent_tokens>1729975</subagent_tokens><tool_uses>571</tool_uses><duration_ms>1285028</duration_ms></usage>
</task-notification>

---
[2026-08-08T19:06] session 197b5d73

right - you see, the runtime as engine, we can design complex context systems like GTC. their focus are different, one is how to build a world, one is how to build a mind, coming from different aspects 
这两个其实可以整合在一起，“GTC 是可以跑在 Context Runtime 上的一个 domain + compiler 策略；runtime 是 GTC 缺的那半边（Becoming）。”你的这个理解很对
从这个角度来看呢？如果runtime可以有各种各样可编程的“context compiler”可以自己编程或者加载形成不同的“性/人格”呢？

---
[2026-08-08T19:06] session aaab8ad8

right - you see, the runtime as engine, we can design complex context systems like GTC. their focus are different, one is how to build a world, one is how to build a mind, coming from different aspects 
这两个其实可以整合在一起，“GTC 是可以跑在 Context Runtime 上的一个 domain + compiler 策略；runtime 是 GTC 缺的那半边（Becoming）。”你的这个理解很对
从这个角度来看呢？如果runtime可以有各种各样可编程的“context compiler”可以自己编程或者加载形成不同的“性/人格”呢？

---
[2026-08-09T03:24] session 197b5d73

请review一下：
首个完整演示已完成，Stages 0–6 全部验收。

* §33 已覆盖 N0→N5、A/B 合并、M1 continuation、回到 N5 探索 C 并对比 M1，以及显式 realm prompt。
* Promotion、OCC、冲突策略、projection 重建、SIGKILL 恢复和 tape replay 均通过。
* 全套门禁：23 个测试文件、102 项测试全部通过；TypeScript、Biome、生产形态探针全部绿色。
* 验收记录已更新：[stage-6.md](/Users/ren/repos/runtime/specs/acceptance/stage-6.md)
* 完成提交：`8f62373 stage-6(§33): complete the terminal demonstration`
* `main` 工作树干净。

---
[2026-08-09T03:30] session 197b5d73

<task-notification>
<task-id>a5ada151df8554d4d</task-id>
<tool-use-id>toolu_01E1JkoTsbj12zKEfDWEg2RN</tool-use-id>
<output-file>/private/tmp/claude-501/-Users-ren-repos-runtime/197b5d73-e1db-4b8b-97b2-8c8b5b17cbdf/tasks/a5ada151df8554d4d.output</output-file>
<status>completed</status>
<summary>Agent "Audit acceptance records vs §32" finished</summary>
<note>A task-notification fires each time this agent stops with no live background children of its own. The user can send it another message and resume it, so the same task-id may notify more than once.</note>
<result>## 1. §32 verdict tables

plan.md has **not** been touched since `9407fbf` (Stage 0), so §32's text is the frozen original for all of this.

### Stage 1 — §32 + §12 probe
| Criterion (§32/§12) | Verdict | Evidence |
|---|---|---|
| Graph test: fork, merge, checkout, diff every node | evidenced | stage-1.md:27–33 (all four checkouts, every ordered node-pair diff, best common base, clean multi-parent merge) |
| p50/p99 commit-transaction latency | evidenced | stage-1.md:44–45 — 5.215 / 8.660 ms |
| Diff + merge at 100k nodes | evidenced | :46–47 — 41.958 ms / 2,453.223 ms |
| Interior hashing at target cardinalities | evidenced | :48–49 — 100k and 1M |
| CAS contention across universes | evidenced | :50 — 160 ops / 8 universes |
| GC sweep under open turns + blob grace window | evidenced | :51, :58–64 (60 s grace, then zero-grace delete) |
| Per-universe export size | evidenced | :68 — 424,965,071 bytes |
| **drop-`proj` rebuild at 10⁶ objects** | **evidenced but weak (self-disclosed)** | :52, :66 — 1,050,551 objects present, but the rebuild reconstructed only **110** `proj.node_index` rows. 23.760 ms measures a near-empty projector, not a 10⁶-scale rebuild. The record admits it: "The projector is intentionally small at Stage 1" |
| Observation-class bracket overhead | evidenced | :53 — 3.387 ms p99 |
| Crash drill 1: `kill -9` mid-transaction | evidenced | :73–76, isolated postmaster port 55432 |
| Crash drill 2: `kill -9` intent-durable → pre-receipt | evidenced | :77–79 |
| Fallback named | evidenced | :94–96 — SQLite-per-universe |

### Stage 2
| Criterion | Verdict | Evidence |
|---|---|---|
| Invalid transitions cannot commit | evidenced | stage-2.md:36 |
| Self-grant proposal fails | evidenced | :37 (`authority/grants/fake`) |
| Write outside authorized prefix refused at patch authorization | evidenced | :38 |
| Patch re-applies to hash equality | evidenced | :45–46, :23–25 |
| Race branches, never silently rebases | evidenced | :42–43 |
| Read-traces recorded + replay-audited | evidenced | :39 |
| Unchanged subtrees structurally share | evidenced | :44 |
| drop-`proj` rebuild drill, standing | evidenced | :45–46, :86 |
| **"the ontology is revised once"** | **not evidenced as a revision** | :77–84 — the checkpoint ran and concluded **no** revision was required ("required no correction… remain at schema 1"). §32's phrasing presumes an actual revision; a no-op checkpoint is a defensible reading but is not what §32 says |

### Stage 3
| Criterion | Verdict | Evidence |
|---|---|---|
| §33 core feels natural in text | **unevidenced (subjective, no human judgment recorded)** | stage-3.md:40–46 describes mechanical execution; no named person attests "feels natural". No sign-off section exists |
| LangGraph adapter vs. **real** `BaseCheckpointSaver` contract | evidenced | :31–36, pinned LangGraph 1.4.9 / checkpoint 1.1.3 |
| "an **off-the-shelf** LangGraph example runs unmodified" | **partial** | :58 downgrades this to "an ordinary, unmodified `StateGraph`". `packages/langgraph-adapter/test/adapter.test.ts:159–176` hand-constructs the graph in-test (thread id literally `"off-the-shelf"`). No upstream example is executed |
| Partially failed superstep resumes without re-running completed tasks | evidenced | :59–60 (completed once, failed twice); test at adapter.test.ts:199 |
| Checkpoint round-trips byte-exact | evidenced | :61; adapter.test.ts:140 |
| Contrasting micro-host publishes batches, no session/compiler/chat | evidenced | :29–30, :65; `packages/host/test/micro-host.test.ts:98` asserts `hosts/micro-loop/batches/batch-1|2` |
| Adapter index rebuilds from `canon`, nothing lost | evidenced | :35–36, :64 |
| Each AdoptionManifest matches observed coverage | evidenced | :65 |

### Stage 4
| Criterion | Verdict | Evidence |
|---|---|---|
| **`kill -9` intent→receipt reconciles _per executor class_** | **partial** | Only the provider-idempotent class gets a real SIGKILL (`packages/tools/test/world-gate.test.ts:375`, `child.kill("SIGKILL")` at :432). The other three classes are covered by a synthetic "crash residue" test (:508) — queryable, non-idempotent, reversible. stage-4.md:53 is honest: "proves the contract without overstating it". §32 asks for the kill drill per class |
| Non-queryable records `unknown`, escalates, never auto-retries | evidenced | stage-4.md:59; world-gate.test.ts:686 `["succeeded","unknown","unknown"]` |
| Fencing drill (A stalls, B reconciles before advancing) | evidenced | stage-4.md:45–51 |
| Pending approval does not occupy the ref; stale approval needs fresh request | evidenced | :39–41 |
| Simulation binding refused external effect by construction | evidenced | :41–42 |
| Revoked grant fails on a historical branch | evidenced | :42 |
| Approval replay fails | evidenced | :40 ("two effects cannot consume one approval"), :20 single-use canonical facts |
| Orphaned outcome surfaces for reconciliation | evidenced | :50–51 `orphanedEffects()` |
| Level 2 middleware ships | evidenced | :21–25 |
| **"No external tool exists before this stage passes review"** | **unevidenced** | `specs/reviews/` contains only plan-level artifacts (v0.3–v0.5, design-competition.json, substrate-analysis.json). No Stage 4 review record exists |

### Stage 5
| Criterion | Verdict | Evidence |
|---|---|---|
| Index deleted + reconstructed **at corpus scale** without semantic loss | evidenced (scale is self-chosen) | stage-5.md:56–59; `packages/memory/test/stage-5.test.ts:341` — 10,000 claims, complete manifest compared byte-for-byte. §32 never defines "corpus scale" |
| Rebuild mints a new epoch; compile cache does not conflate | evidenced | :30–31, :52–54 |
| Private claims invisible across agent scopes | evidenced | :26–29, :49–52 (partner identifier not leaked; compilation rejects the one-sided dispute) |

### Stage 6
| Criterion | Verdict | Evidence |
|---|---|---|
| Two substantially diverged branches merge without silent discard | evidenced | stage-6.md:49–56 (A×5, B×7; both artifacts preserved) |
| Contradictions land as contested pairs | evidenced | :53–56, :27–30 |
| Reducer meeting a contested value behaves per policy | evidenced | :62–65 — all three of `continue`/`policy`/`never` exercised |
| Promoted branch re-runs effects through full pipeline; report matches | evidenced | :73–78 (refused plan, crossed claim, one fresh `booking.reserve` succeeded; provider applied once) |
| Property tests hold | evidenced | :66; `packages/runtime/test/merge.test.ts` `numRuns: 500` ×2 = the claimed 1,000 |
| §33 demo runs at end of stage | evidenced with a caveat | Demo covers time-travel to N5 / approach C, realm refusal, drop-`proj`, "why not claim X", tape replay. But §33 says the failure drills run "**live, in the same demo**" — stage-6.md:86–88 places the `kill -9` and fence-takeover drills in the Stage 4 suite instead ("The full suite also reruns Stage 4's real worker-death drills") |
| Two-agent OCC drill, first activation | evidenced | :68–71 (disjoint linearizes, no race ref; overlap branches) |

**Cross-cutting gap:** stages 1–6 all say `Status: **accepted**` in passive voice with **no named signer**. Only stage-0.md names Ren. §32 only demands Ren's signature at Stage 0, so this is not a literal violation — but Stage 3's subjective criterion and Stage 4's "passes review" gate both depend on a human, and no human is recorded.

## 2. Stage-0 sign-off

Yes — recorded twice. `/Users/ren/repos/runtime/specs/acceptance/stage-0.md:48`:

&gt; "- [x] Ren — signed on 2026-08-09. Stage 0 is accepted; the encoding, hash preimages, and fixture vectors are frozen; any future change to them is an encoding migration (§8, §30)."

And line 3: "Status: **accepted and signed by Ren**". The `9aca99c` commit subject was "draft the Stage 0 acceptance record — awaiting Ren"; the signature landed later.

## 3. specs/ diff classification

**Neither commit touched `specs/plan.md`. No normative plan text changed — there is nothing to quote.** `git log -- specs/plan.md` ends at `9407fbf` (Stage 0). Both commits changed only `specs/decisions.md` plus a new acceptance record.

**`5043030` (Stage 5)** — `specs/decisions.md` +6/−2, one hunk, in the OPEN-items list:
- Expands the "Domain comparator interface" OPEN item with what Stage 5 actually shipped and adds two explicit `OPEN:` markers. **Legitimate: recording a decision + narrowing an OPEN item.** Notably conservative — it books a *candidate*, not a truth judgment, and hands two questions forward: "`OPEN:` Stage 6 must define reference equivalence and register per-domain object incompatibility semantics."

**`6c4872c` (Stage 6)** — `specs/decisions.md` +25/−6, two hunks:

- *Hunk A (new decision blocks, legitimate with one flag):* adds "**Stage 6 domain merge and promotion.**" and "**Structured-claim equivalence v1.**". Recording decisions in the decisions register is the right venue. One clause deserves Ren's eyes because it scopes a §14 mechanism: "Observed-footprint OCC activates here only for pure, single-parent state transitions; disjoint work linearizes and overlap preserves a branch. General multi-agent scheduling remains Stage 10." That is *consistent* with §32 ("the first activation" at Stage 6, "generalized" at Stage 10), so I read it as legitimate — but it is a scope narrowing recorded by the implementer, not by the plan.

- *Hunk B (OPEN item rewritten — flag for Ren):* the OPEN item added one commit earlier is deleted and replaced by a narrower one. Removed: "`OPEN:` Stage 6 must define reference equivalence and **register per-domain object incompatibility semantics**." Retained, as a standalone item: "**Omitted structured-claim scope semantics.** Claims lacking the comparator's roles remain `unknown`…". The reference-equivalence half was closed by decision in Hunk A ("Reference roles compare by exact canonical identity; the runtime does not invent alias equivalence") — fine. But the **per-domain object incompatibility registry** obligation was dropped from the OPEN list without being closed anywhere. That is an obligation retired by deletion, one commit after it was written. Not a plan rewrite, but it is the one hunk I would not merge without Ren.

## 4. Test-count check: "23 test files, 102 tests" — **verified**

Method: `find packages -name "*.test.ts" -not -path "*/node_modules/*"` → **23** files. Case count: `grep -cE "^[[:space:]]*(test|it)(\.[a-z]+)?[[:space:]]*\("` summed across those files → **102**. Exact match on both numbers.

Caveats on what 102 means: it counts declaration sites only. `packages/runtime/test/merge.test.ts` contributes 3 cases but executes 1,000 fast-check runs; several "cases" are very large scenarios (`stage-6-demo.test.ts` is a single `it` covering the entire §33 demo; `stage-3.test.ts` likewise is 1). So 102 is an accurate file/declaration count and a poor proxy for assertion breadth — 5 packages contribute exactly 1–2 cases each while `packages/domain` contributes 63.</result>
<usage><subagent_tokens>67745</subagent_tokens><tool_uses>24</tool_uses><duration_ms>204767</duration_ms></usage>
</task-notification>

---
[2026-08-09T03:32] session 197b5d73

<task-notification>
<task-id>a4b68890d0e36b95d</task-id>
<tool-use-id>toolu_012YCXCVcg7pnzLmNiYMPfcX</tool-use-id>
<output-file>/private/tmp/claude-501/-Users-ren-repos-runtime/197b5d73-e1db-4b8b-97b2-8c8b5b17cbdf/tasks/a4b68890d0e36b95d.output</output-file>
<status>completed</status>
<summary>Agent "Check boundary notes + build-ahead" finished</summary>
<note>A task-notification fires each time this agent stops with no live background children of its own. The user can send it another message and resume it, so the same task-id may notify more than once.</note>
<result>Both audits complete. Full findings:

---

# Audit 1 — Boundary-notes compliance

## (a) Compiler — Stage 3 items

**1. Explicit pipeline stages, typed candidate between them — APPLIED**
- Five pure exported stages: `gather` `/Users/ren/repos/runtime/packages/compiler/src/pipeline.ts:135`, `score` `:158`, `select` `:179`, `order` `:311`, `render` `:328`; composed at `/Users/ren/repos/runtime/packages/compiler/src/index.ts:76-84`.
- The candidate object is not just typed, it is stage-tagged: `Candidate` `pipeline.ts:62`, then `GatheredCandidate` `:82`, `ScoredCandidate` `:83`, `SelectedCandidate` `:87`, `OrderedCandidate` `:91` — each stage strips the prior tag and adds its own, so a stage cannot be skipped or reordered at the type level. Stronger than the note asked for.
- Covered by `packages/compiler/test/compiler.test.ts:69`.

**2. Constants lifted into one data object — APPLIED**
- `COMPILER_POLICY_V1`, frozen, `pipeline.ts:23-49`. Shares are identity 2 / policy 5 / tasks 8 / dialog 30 / memory 35 / artifacts 12 / tools 8 (`:25-33`) — exact match to `specs/plan.md:911`. Priority weights at `:35-48`, spill order at `:34`.
- No inline literals survive in the algorithm: `score` reads `.priorityWeights` `:159`, `select` reads `.categoryShares` `:185` and `.spillOrder` `:213`.
- One residue: `stabilityRank` `pipeline.ts:308` is an inline ordering constant outside the policy object, so it is not digest-bound. Outside the note's literal wording ("budget shares, priority weights"), but it is the last free constant in the compiler.

**3. Policy digest folded into compilerDigest — APPLIED**
- `compilerPolicyDigest = recordDigest(admit(COMPILER_POLICY_V1))` `pipeline.ts:51`; `compilerDigest` `:52-58` carries `policy: compilerPolicyDigest`.
- Memoization discipline unchanged: `compileCacheKey` is `frameDigest:compilerDigest` `index.ts:49-51`, matching `plan.md:917`. Both digests also land in the record `pipeline.ts:346-347`. Tests `compiler.test.ts:63-65,127`.

**4. No plugin points / dynamic loading — HONORED**
- `index.ts:70-73` states the stages stay an implementation detail "until a second compiler proves an interface (§20 boundary note)". No `import()`, no registry, no plugin surface in `packages/compiler/src`.
- Nearest repo-wide analogue is `DomainRegistry` `packages/runtime/src/registry.ts:71`, labelled "Static build-time composition only; dynamic loading is deliberately deferred" `:70` — that is `plan.md:1231`'s sanctioned static composition, not a compiler seam.

*Deviation worth naming, and it is a correct one:* the pipeline has six stages, not five — `completeEpistemically` `pipeline.ts:229` sits between select and order. The implementation string is honest about it: `"gather-score-select-epistemic-complete-order-render/v2"` `:55`, format `"context-compiler/v2"` `:54`. That is the notes' Stage 5 epistemic-completion item landing inside the Stage 3 shape.

## (b) Memory — Stage 5 items

**1. Structured statement form on `Claim.content` — APPLIED**
- `StructuredClaimStatement` `/Users/ren/repos/runtime/packages/domain/src/objects.ts:277-282` is `{ predicate, args: Record&lt;role, arg&gt; }`; `StructuredClaimArgument` `:270-273` is exactly the `{ref} | {value}` union.
- `ClaimContent = BlobRef | string | StructuredClaimStatement` `:285` — prose and blob preserved beside it, as instructed.
- Vocabulary is data, not schema: `:276` "The predicate vocabulary is data. No per-predicate schema is admitted here." Predicate and role are regex-bounded strings (`:279`, `:269`); no per-predicate zod kinds exist. Test `packages/domain/test/schemas.test.ts:185`.

**2. Structured claim-to-claim references on contest/supersede — APPLIED**
- `MemoryContestRecord` `packages/memory/src/domain.ts:32-39` (`left`/`right` as `ClaimId`), `MemorySupersedeRecord` `:42-50` (`prior`/`successor`), `MemoryRetireRecord` `:52-59`. Prose `reason` is optional and sits *beside* the typed edge.
- Both endpoints are resolved against real claims before the record is written (`:118`, `:142`, via `requiredClaim` `:87`).
- Genuinely queryable, not just typed: `projectMemoryState` `:246-288` folds lifecycle into status + adjacency, and the index materializes `contested_with` as a SQL array column `packages/memory/src/indexer.ts:47,216-223`.

**3. Bitemporality explicit — APPLIED (two clocks, two homes)**
- `observedAt: Time` on the claim schema `objects.ts:293`.
- Record/topological time is deliberately *not* a second claim field — it is the node that recorded the claim, materialized as `recorded_at` / `recorded_node` on the projection `indexer.ts:49-50,60-61,211-212`. That matches `plan.md:939` ("current status is a projection of ancestry, never mutated in place... observation time and validity time are distinct") and Law 5. If you expected both fields on the schema itself, read this as partial; measured against the plan it is the right split.

**4. Compiler epistemic completion — APPLIED, end to end**
- Compiler side: `completeEpistemically` `pipeline.ts:229-306` builds the contested graph, takes connected components, and for any component containing a selected member either admits the whole component `:286-291` or drops all of it with a recorded reason `:276-284` — "contested partner unavailable at compilation boundary" / "complete contested group exceeds token budget". Never one side silently.
- Retrieval side closes the loop: the indexer fetches partners absent from the primary result `indexer.ts:333-345`, sets `withheldContestedPartner` when ACL scope hides one `:366`, and `toCandidates` emits a deliberately unresolvable id `memory:&lt;id&gt;:withheld-contested-partner` `:404-409` — forcing the compiler to drop the group rather than show a one-sided claim. The failure direction is correct.
- `contestedWith` survives into the compilation record `pipeline.ts:358-360`. Test `compiler.test.ts:169`.

**5. Domain comparator sketched — APPLIED, both places**
- `specs/decisions.md:113-118` "Structured-claim equivalence v1" settles the computable part; `specs/decisions.md:217-219` leaves the genuine fork open ("Omitted structured-claim scope semantics").
- Code: `DomainComparator` `packages/memory/src/domain.ts:297` with the `OPEN:` marker at `:294-295`; `StructuredStatementComparator` `:306-327` is the conservative seed (same predicate/subject/scope, unequal object ⇒ `contradiction-candidate`; missing roles ⇒ `unknown`).
- Wired to Stage 6: the merge `after` hook auto-emits contest records for cross-branch contradiction candidates `:209-225`, reason "automatic contradiction candidate from domain merge" `:222`.

*Housekeeping item from the notes is closed:* `specs/acceptance/stage-0.md:3` now reads "accepted and signed by Ren", signed `:48` on 2026-08-09.

---

# Audit 2 — Build-ahead check against §34

| Item | Verdict | Evidence |
|---|---|---|
| Sessions / web packages | **Clean** | No `apps/`; no `packages/session`. Stages 8–9 untouched. |
| `packages/host` scope | **Legitimate** | 3 files / 328 lines. `MicroHost` `packages/host/src/micro-host.ts:25-52` publishes one opaque event batch as blob + link. Comment `:24` "batches opaque loop events without sessions, prompts, or chat semantics" mirrors `plan.md:1279`'s gate criterion. `MICRO_HOST_MANIFEST` `:9-22` declares level 0 with all captures false. `publisher.ts` / `codec.ts` are the named Stage 3 portability deliverables (`plan.md:1277`). |
| `packages/terminal` scope | **Legitimate** | `Stage3Terminal` `packages/terminal/src/terminal.ts:92` plus `merge-surface.ts` (35 lines) and `svg.ts` (70 lines) — the §33 command list at `plan.md:1263-1271`. No server, no stream, no session. |
| Temporal | **Clean** | Zero deps. One forward-looking comment, `packages/tools/src/index.ts:90`, on the `ExecutionDriver` port — precisely §34's "create interfaces where these may someday belong". |
| CRDTs / custom vector DB / pgvector | **Clean** | No CRDT libs anywhere. Retrieval is Postgres FTS: `websearch_to_tsquery('simple',…)` + `ts_rank_cd` `packages/memory/src/indexer.ts:310,313`, policy recorded as data `:38-40`. Notably, the *absence* of embeddings is itself recorded and verified: `MEMORY_EMBEDDING_MODEL = …{format:"embedding-model/none"}` `:37`, carried in the epoch snapshot `:234`, checked on read `:257`. Matches `plan.md:942,1289`. |
| Self-modification / signed bundles / sandboxing | **Clean** | Zero hits in `packages/*/src` and in `pnpm-lock.yaml`. |
| Git exporter | **Clean** | No `isomorphic-git`/`nodegit`; no exporter code. |
| Second store backend | **Clean** | Postgres only (`packages/store/src/postgres-store.ts`); no sqlite/pglite in sources or lockfile. |
| Stage 7 policy machinery | **Clean — line respected exactly** | `canon.availability` is **read-only** in the codebase: `availabilityEpoch()` `packages/store/src/postgres-store.ts:1665-1672` and a status lookup `:1969-1975`. No INSERT/UPDATE/DELETE against it anywhere. Both reads are forced by earlier-stage contracts, not by retention policy: `availabilityEpoch` is a required `ContinuationFrame` field `packages/domain/src/frame.ts:59` populated at compile time `packages/terminal/src/terminal.ts:227`, and `redacted`/`expired` are §22 typed-absence members of the value union `packages/domain/src/objects.ts:238` that the terminal must handle `terminal.ts:158`. No tombstone writer, no retention enforcement, no export. |
| All packages private | **Clean** | All 12 `packages/*/package.json` carry `"private": true`; root `package.json:3` likewise. Matches `plan.md:39` item 7. |

**One thing that looks like a §34 violation and is not.** `universeExportBytes()` `packages/store/src/postgres-store.ts:2171-2200` is not a per-universe exporter — it is `SUM(pg_column_size(...))` across the schema, and its only callers are the Stage 1 load probe `bench/stage-1.ts:398` and its store test `packages/store/test/store.test.ts:286`. `plan.md:520` names "per-universe export size" as a Stage 1 *measurement*. The name invites the misread; the code does not earn it.

---

# Over-built / under-built

**Over-built: nothing.** Four candidates surfaced and all four clear:
- Compiler v2 / six stages — the notes' own Stage 5 epistemic-completion item, honestly named in the digest string `pipeline.ts:55`.
- `CompactionRecord.retention` enum `packages/terminal/src/domain.ts:24` — the closest call. It clears because `plan.md:1268-1269` makes `summarize-epoch` with a minimal record an explicit Stage 3 deliverable, and the field is inert: written once as the constant `"reversible"` `terminal.ts:355`, never read or enforced anywhere. It is a record label, not Stage 7's retention-class machinery. Slightly beyond the literal "frontier, digests, retained/omitted" list, worth a glance but not a build-ahead.
- Temporal comment `tools/src/index.ts:90` — a comment.
- `universeExportBytes` — Stage 1 probe measurement, as above.

**Under-built, all minor and none blocking:**
- `packages/observability` appears in the §31 layout (`plan.md:1211` region) and does not exist. No Stage 0–6 acceptance requires it — tracing acceptance is Stage 8 `plan.md:1307` — so this is a layout gap, not a violation.
- §31 shows `packages/adapters/langgraph`; the repo has flat `packages/langgraph-adapter`. Cosmetic naming deviation from the layout diagram.
- `stabilityRank` `pipeline.ts:308` is the one compiler constant left outside `COMPILER_POLICY_V1` and therefore outside `compilerPolicyDigest`. Ordering rank is not literally a "budget share" or "priority weight", so the note's letter is met — but folding it in is a one-line change that would make the policy object genuinely total.

Overall: the boundary notes were applied faithfully and in a couple of places (stage-tagged candidate types, the recorded `embedding-model/none`, the withheld-partner poison id) more rigorously than asked. No Stage 7–11 machinery exists.</result>
<usage><subagent_tokens>72780</subagent_tokens><tool_uses>44</tool_uses><duration_ms>293226</duration_ms></usage>
</task-notification>

---
[2026-08-09T03:35] session 197b5d73

<task-notification>
<task-id>a062bf250099d4750</task-id>
<tool-use-id>toolu_01MhCD61dG1hrVYL5x52oFsS</tool-use-id>
<output-file>/private/tmp/claude-501/-Users-ren-repos-runtime/197b5d73-e1db-4b8b-97b2-8c8b5b17cbdf/tasks/a062bf250099d4750.output</output-file>
<status>completed</status>
<summary>Agent "Verify drills, replay, OCC realness" finished</summary>
<note>A task-notification fires each time this agent stops with no live background children of its own. The user can send it another message and resume it, so the same task-id may notify more than once.</note>
<result>I have complete evidence. Here are the verdicts.

## 1. SIGKILL crash drills — **REAL** (one drill), with scope gaps

**The drill:** `packages/tools/test/world-gate.test.ts:375` — `it("survives SIGKILL between intent and receipt, fences failover, and surfaces the orphan")`.

- Real child: `world-gate.test.ts:416` `spawn(process.execPath, ["--import", "tsx", fixture], …)`; real kill at `:432` `child.kill("SIGKILL")` then `await once(child, "exit")`.
- The child genuinely touches the world before dying: `packages/tools/test/fixtures/crash-between-intent-and-receipt.ts:90-99` inserts into `ops.stage4_world_effects`, prints `WORLD_TOUCHED`, then `await new Promise&lt;void&gt;(() =&gt; {})` — hangs forever with no receipt. The parent waits for that exact marker (`:431`).
- **Both crash windows in one drill.** The fixture runs inside `engine.transact` (`fixture:107`), and `transact`'s `context.step` performs a *durable mid-turn commit* (`packages/runtime/src/engine.ts:622-628`) while publication happens once at the end (`engine.ts:781`). So the SIGKILL lands after intent + mid-turn commit and before both receipt and publication.

**Reconciliation assertions (all load-bearing):**
- Outbox found: `world-gate.test.ts:443-445` `const pending = await recovered.pendingEffectEntries(LIVE); expect(pending).toHaveLength(1)`
- Cannot advance before reconciling: `:446` `await expect(recovered.open(root.id, LIVE)).rejects.toMatchObject({ category: "race" })`
- Idempotent re-dispatch dedupes at the world: `:493` `expect(counts.rows[0]).toEqual({ calls: "2", effects: "1" })` — two driver attempts, one world application.
- Orphan surfaced, not dropped: `:497-498` `expect(orphaned.map(({ intent }) =&gt; intent.effect)).toEqual([effect])` + `expect(orphaned[0]?.observation?.outcome).toBe("succeeded")`.

**Per-executor-class behavior — REAL contract, SIMULATED crash.** `world-gate.test.ts:508` `it("reconciles queryable, non-idempotent, and reversible crash residue by class")` induces residue with an in-process `throw new Error("induced pre-receipt crash residue")` (`:643`), not a process death. Assertions are strong — `:686` `.toEqual(["succeeded", "unknown", "unknown"])`, `:696-697` `queryableReconciliations: 1, nonIdempotentDispatches: 0` (never auto-dispatch or auto-query the non-queryable class), `:708` `escalated: true` with declared compensation. **Flag:** only the `provider-idempotent` class is proven under a real `kill -9`; the other three classes are proven against a simulated crash.

**Second gap:** `bench/stage-1.ts` holds two more real drills — durable-intent (`:111` `child.kill("SIGKILL")`) and a genuine postmaster kill (`:232` `process.kill(postmasterPid, "SIGKILL")` + WAL recovery). Neither is in the standing suite: `vitest.config.ts:5` includes only `packages/*/test/**/*.test.ts`; bench runs manually via `pnpm probe:stage-1`.

## 2. Fencing drill — **REAL, but split across two tests**

- **Fence-equality CAS is real, not advisory.** `packages/store/src/postgres-store.ts:1513` `AND turn_row.fence=$3 AND ref.fence=$3 AND lease.token=$3 AND lease.holder=$4` (dispatch); `:1541` `AND turn_row.fence &lt; $3 AND ref.fence=$3 …` (recovery — the recoverer must hold a strictly higher fence). `beginEffectAbsorption` (`:1548`) additionally requires the prior lease expired past the safety margin and an unresolved intent to exist (`:1573`).
- **A's late publish is fenced out:** `packages/store/test/store.test.ts:341-343` — two live store handles (`worker-a`, `worker-b`); B calls `acquireLease`, then `expect(fenced).toEqual({ kind: "fenced", expected: occupied.fence, actual: newFence })`. Worker A is *alive* here.
- **B must reconcile before advancing live:** `world-gate.test.ts:446` (open rejects `race`), absorb retry loop `:473-484`, then `:494` `const next = await recovered.open(root.id, LIVE)` succeeds. Enforcement is structural — the occupied turn cannot be abandoned while an intent is unresolved: `store.test.ts:380` `await expectStoreError(first.abandon(effectTurn), "policy")`.

**Weakened only in composition:** no single test has A *alive and stalled mid-effect* while B reconciles that same effect and A's late publish is then rejected. The stall+takeover half kills A (so A can never publish late); the late-publish-fenced half has no effect in flight.

## 3. Tape replay — **REAL, and the strongest thing here**

Harness: `packages/replay/src/index.ts:122` `liveThenReplay`.

```
129: const replay = clone(await scenario(replayer, "replay"));
130: replayer.assertConsumed();
131: if (JSON.stringify(live) !== JSON.stringify(replay)) throw new Error("live/replay result divergence");
```

**Exact consumption is asserted in all three directions:** leftover → `:115-119` `assertConsumed()` throws `replay left N tape entries unconsumed`; short tape → `:83` `replay tape exhausted at ${kind}:${label}`; wrong order/label → `:84-88` `replay mismatch at ${cursor}`. Directly unit-tested at `packages/replay/test/replay.test.ts:29-35`.

**Not StateId-only.** Every suite calls `resetDatabase()` as the *first* line inside the scenario, so replay is a full re-execution against an empty database. What's compared:
- **Record hashes + topology + runtime/kernel digests:** every payload returns `graph`, and `graph()` selects `record_hash` per node (`postgres-store.ts:2103`), mapped to `record: digest(row.record_hash)` at `:164`.
- **Read traces:** `store.test.ts:282-283` `paths: [...view.trace.paths].sort(), prefixes: […].sort()`; `runtime.test.ts:332` `acceptedReads: acceptedTransition.reads` → asserted `:375` `{ paths: ["tasks/seed"], prefixes: ["tasks/**"] }`.
- **Authorization decisions:** `runtime.test.ts:333-336` `authorizationBound` (checks the persisted `authority.static/v1` evidence + realm), plus four error categories compared (`invalidCategory`/`selfGrantCategory`/`escapeCategory` = `validation`/`authorization`/`authorization`).
- **Frames &amp; compiler evidence:** `memory/test/stage-5.test.ts:331` `compile: [firstCompile.frameDigest, secondCompile.frameDigest]`; the full compilation record is compared as `why` (`terminal/test/stage-3.test.ts:235`, `stage-6-demo.test.ts:806`).
- **Effect plans/receipts:** `world-gate.test.ts:361-364` returns `effect`, `observation`, and `approvals`.
- **Zero providers on replay:** `world-gate.test.ts:371` `expect(providerCalls).toBe(1)`; `stage-3.test.ts:242` `expect(providerCalls).toBe(2)`; `stage-6-demo.test.ts:836` `expect(worldApplications).toBe(1)` across live + replay.

**Scope gaps (not theater, but "every acceptance run" is overstated):** 8 of 23 test files use `liveThenReplay`. Notably **`packages/langgraph-adapter/test/adapter.test.ts` (4 acceptance tests) never replays at all**, and within `world-gate.test.ts` only 1 of 3 tests replays — the two crash/recovery tests do not. **One item on the CLAUDE.md list is indirect:** the `compiler.context` blob hash (`compiled.hash`) never appears in a compared payload — it's only asserted `.not.toBe(...)` inside the scenario (`stage-5.test.ts:319`). Frame digest and compilation-record content are compared; rendered item *content* strings are not (`packages/compiler/src/pipeline.ts:343-373` — the record carries candidate identity/authority/tokens, not content).

## 4. OCC two-agent drill — **REAL OCC, in-process concurrency**

`packages/terminal/test/stage-6-demo.test.ts:576-577` and `:600-601`, both `await Promise.all([occ.submit(…), occ.submit(…)])`.

- Disjoint: `:581` `expect(occB.linearizedFrom).toBe(designBase.id)` and `:871` `branchesAfterDisjoint: []` — B rebased onto A's new head, no race ref created.
- Overlapping: `:604` `expect(overlapB.result.kind).toBe("branched")`.

**Not a serial simulation of staleness.** `packages/runtime/src/sequencer.ts:82` launches `this.#engine.observe(request)` for *both* agents before either enters the arrival queue, and `observe` does real work — real reducer against a real `ScopedStateView` at the request's base, with re-authorization (`packages/runtime/src/engine.ts:723-734`). B's base is genuinely stale by the time it is admitted; the footprint check at `sequencer.ts:65-73` decides linearize vs. branch.

**Honest limitation, disclosed in the source:** admission is serialized by an in-process per-ref queue — `sequencer.ts:5` `/** One in-process arrival queue per ref; the Store fence remains the cross-process authority. */`. Cross-process concurrency is proven separately (item 1's spawned child, item 2's two store handles), not in the OCC test itself.

## 5. Promotion (§16) — **REAL**

`packages/tools/src/index.ts:481` `/** Promotion is reconciliation plus fresh live effect proposals, in one fenced publication batch. */`

- Simulated receipts cannot be imported — the merger refuses them structurally: `packages/runtime/src/merge.ts:385` `refused.push({ path, reason: "simulated effect plans are re-proposed, never imported" })`.
- Promotion effects must be exactly those refused paths, with a matching real driver: `tools/src/index.ts:571` `throw new Error(\`promotion effect ${effect.source} is not a refused simulated plan\`)`.
- Re-proposed through the full pipeline under a live binding: `:540` `throw new Error("promotion requires the designated live binding")`, `:545` candidate must be simulation-derived, then `turn.step({...effect.step, effects:[effect.plan]})` → engine authorization → `:599` `const observation = await this.#bracket.dispatch(effect.plan.effect, effect.driver)` — a fresh receipt, not an imported one.
- **Promotion report vs. what actually happened:** `stage-6-demo.test.ts:686` `expect(promoted.report.reran).toMatchObject([{ outcome: "succeeded" }])`, cross-checked against canon at `:691` `expect(promotedEffect.observation?.outcome).toBe(promoted.report.reran[0]?.outcome)`; `:880` `liveImportedSimulatedPlan: false`; ancestry check `:695` `expect(liveAncestry.has(approachB.id)).toBe(false)`.
- **Simulation-derived claims cross labeled:** `:687` `expect(promoted.report.crossedAsSimulation).toContain(claimPath(steel.id))` and `:756` `expect(promotedCandidates).toMatchObject([{ authority: "simulation" }])` — the label is re-derived from the claim's authenticated source transition (`tools/src/index.ts:517-521`), not copied.

## 6. Drop-proj drill — **REAL for the rebuild; ops event-log half ABSENT (not yet built)**

- It literally drops the schema: `packages/store/src/projection.ts:63` `await client.query("DROP SCHEMA IF EXISTS proj CASCADE")`, then rebuilds every table from `canon.nodes` / `canon.host_checkpoints` / `canon.host_thread_events`.
- Standing equivalence assertions in 7 suites: `store.test.ts:266` `expect(afterRebuild).toEqual(beforeRebuild)`; `runtime.test.ts:307` `if (jcs(beforeRebuild) !== jcs(afterRebuild)) throw new Error("projection rebuild drift")`; `langgraph-adapter/test/adapter.test.ts:181` `expect(after).toEqual(before)` (checkpoint tuple identity across the drop).
- "Degrades loudly, never wrongly": `stage-6-demo.test.ts:762-765` `await rebuildAllProjections(…)` then `.rejects.toThrow("does not name this memory index materialization")`, followed by a fresh epoch returning the same claim.
- **Ops event-log sequences unrenumbered: ABSENT, legitimately.** That requirement is `specs/plan.md:1126` (`a client's Last-Event-ID must survive the drop-proj drill unrenumbered`) and belongs to the **Stage 8** session event log (`plan.md:1307`, `packages/session` + `apps/server`), which does not exist. Grepping the migrations, no `ops` event-log table or sequence exists today; the only `bigserial` generation counter is `canon.host_thread_events.event_id` (`migrations/007_host_checkpoints.cjs:4`), which lives in `canon` and is therefore untouched by the drop by construction. CLAUDE.md's stage discipline covers this; no test claims it.

## 7. The §33 demo — **REAL, executed by a test**

`packages/terminal/test/stage-6-demo.test.ts:189` `it("merges divergent simulations, enforces contested policy, linearizes OCC, and promotes through the world gate")` — a vitest test, not a script, wrapped in `liveThenReplay` at `:191`, closing with `:835` `expect(execution.replay).toEqual(execution.live)`.

It executes the §33 script beat for beat: N0–N5 design loop (`:266-278`, asserted `expect(designNodes).toHaveLength(6)`); fork `exp/approach-A`/`exp/approach-B` with realm-labeled prompts (`:288-303`, `:855-858` `approachA: "[simulation:exp/approach-A] &gt;"`); merge with contested claims (`:849` `merge: { kind: "conflicts", parents: […] }`); time-travel to N5 → approach C → compare to M1 (`:479-481` `store.diff(approachC.state, mergeNode.state)`); promote B4's booking (item 5 above). Plus in-demo: historical fork's effect refused (`:879` `simulationEffectRefused: "authorization"`), the "why didn't the model see claim X" answer (`:745-747` `expect(why.rejected).toMatchObject([{ reason: "contested partner unavailable at compilation boundary" }])`), DAG render, drop-proj, and full-tape replay.

**One §33 line does not live in the demo:** the `kill -9` drill. The demo has no child process — that drill lives in `world-gate.test.ts:375` and is rerun by the same suite. `specs/acceptance/stage-6.md:86` states this accurately ("The full suite also reruns Stage 4's real worker-death drills"), so it's disclosed, not concealed.

---

## Theater flags

1. **`bench/stage-1.ts:450-454` is green-by-default when skipped.** `const intentCrash = skipCrashDrills ? true : await runIntentCrashDrill();` and the WAL equivalent hardcode `{ acknowledgedSurvived: true, unacknowledgedRolledBack: true }`. Those values flow straight into `checks.walCrash` / `checks.intentCrash` (`:521-522`) and into `passed: Object.values(checks).every(Boolean)` (`:539`). Only `shape.crashDrillsExecuted` (`:535`) distinguishes a smoke run from a real one. The signed record `bench/results/stage-1.json` does say `crashDrillsExecuted: true`, so the record of truth is sound — but a reader trusting `passed: true` alone can be misled. A skipped drill should report `false`/`null`, not `true`.
2. **Crash recovery is never replayed.** The two crash/reconciliation tests in `world-gate.test.ts` (`:375`, `:508`) use a bare `TapeRecorder` with no replay pass, unlike every other acceptance scenario in the file.
3. **`packages/langgraph-adapter/test/adapter.test.ts` — 4 acceptance tests, zero `liveThenReplay`.** It is the one acceptance surface fully outside the replay spine.
4. **Three of four executor classes are proven against a simulated crash**, not a real one (`world-gate.test.ts:643` `throw new Error("induced pre-receipt crash residue")`).

## Counter-flags (things that pattern-match to rigor)

- **Zero mocking anywhere.** `vi.mock`, `vi.fn`, `vi.spyOn`, `mockImplementation` return no hits across `packages/`. No `process.kill` is stubbed; the only kills are real.
- `store.verify()` (`postgres-store.ts:2360-2404`) re-derives every StateId, re-applies every stored patch and re-checks it reproduces the StateId, and walks every effect's action hash — and it is called inside both the live and replay passes.
- The bench WAL drill refuses to run against the wrong cluster (`bench/stage-1.ts:213`), i.e. it declines to fake a pass.</result>
<usage><subagent_tokens>121249</subagent_tokens><tool_uses>72</tool_uses><duration_ms>473302</duration_ms></usage>
</task-notification>

---
[2026-08-09T03:41] session 197b5d73

① 需要你裁决的（唯一一处）：6c4872c 在 decisions.md 里删掉了一条前一个 commit 刚写下的 OPEN 义务——"register per-domain object incompatibility semantics"。reference-equivalence 那一半被正式决议关闭（合法），但这一半是被删除而非被关闭的。代码里留了保守的 comparator 种子和 OPEN: 标记，所以精神部分存活，但账本上的义务消失了。建议：要么恢复该 OPEN 项，要么由你明示批准其退役。

not totally sure about this, and other things looks ok, if there is a clear elegant choice, choose that

如果没有问题，请起草

---
[2026-08-09T03:48] session 197b5d73

你只剩三个小动作：满意的话把 ADR-012 的 proposed 翻成 accepted（一个词）；亲手跑一遍 demo 感受它（pnpm vitest run packages/terminal/test/stage-6-demo.test.ts）；如认可就在 stage-4/stage-6 记录里补个签名行。提交讯息建议 adr-012(§20,§21,§31): composable context systems — how the mind layer arrives，或按你的习惯来。

accepted, 你可以自己翻一下
然后，告诉我离开始stage 8，frontend之前，我们还差什么

---
[2026-08-09T05:09] session aaab8ad8

@"/Users/ren/Downloads/GTC_Generative_Topological_Context_v0.2.md"
now v0.2 is also out. please note this plan is from a research branch, lack some contexts of our current progress
please think deeply, what from this inspires us? what should be absorbed? combining with the current codebase, what is the most elegant, clever, unified direction we should be taking?

---
[2026-08-09T05:13] session 197b5d73

* 签字：`stage-{3,4,6,7}.md` 各加了一行未勾选的 sign-off，只针对人才能判断的准则（stage-3 的 "feels natural"、stage-4 的 review gate）。stage-4 那条我写明了诚实残留：四个 executor class 里只有 provider-idempotent 经过真 `kill -9`。
* 亲手跑一次 demo（如果还没）


edit them, all done and commit

---
[2026-08-09T05:19] session aaab8ad8

"现在的状态：引擎从 domain spec 一路到 retention/erasure 全部落地并签收，账本干净，ADR-012 把心智层的入场规则立好了。下次开工时有两条互不阻塞的路——Stage 8（等你的宣告）和 ADR-012 下的心智层模块（随时可以开始，与 Stage 8 平行）。"
这是目前最新的repo状态

我们先不动stage 8，而是update我们现在的plan和repo，确保我们接下来的方向是这个unified，合流的版本

---
[2026-08-09T07:21] session 67f705b7

让我们思考一下stage 8，我们的frontend该怎么设计
我在考虑的assistant ui和CopilotKit， 是我知道的比较popular的，我希望尽可能“不要自己造轮子，但是支持优雅的造轮子”
就是说，我希望有一个open source solution，优雅，可扩展，有足够多的组件，例如render artifacts，可以自定义ui，同时interface设计的很优雅的

我们的前端应该用什么stack？ 沟通用什么协议？如何edit/update context并与server的保持同步？有很多事情需要思考，确保longtermism， 优雅，架构合理

---
[2026-08-09T17:41] session 67f705b7

<task-notification>
<task-id>a9ce2b7258a840654</task-id>
<tool-use-id>toolu_012abra64iwURLUfop1dVth5</tool-use-id>
<output-file>/private/tmp/claude-501/-Users-ren-repos-runtime/67f705b7-bf84-4a27-826f-9576a2a82ee2/tasks/a9ce2b7258a840654.output</output-file>
<status>completed</status>
<summary>Agent "Deep-dive AI Elements internals" finished</summary>
<note>A task-notification fires each time this agent stops with no live background children of its own. The user can send it another message and resume it, so the same task-id may notify more than once.</note>
<result>All research complete. Here is the report.

---

# Due-Diligence Report: Vercel AI Elements as a Thread-Surface Layer for a Non-AI-SDK Runtime

**Audit basis:** full source read of a fresh clone of [github.com/vercel/ai-elements](https://github.com/vercel/ai-elements) at HEAD `0c1f5e8` (2026-07-09), plus Vercel changelogs, docs at [elements.ai-sdk.dev](https://elements.ai-sdk.dev/), npm registry metadata (retrieved 2026-08-10), and the GitHub issue tracker.

**Correction to the brief's premise:** there was no "May 2026 update." The Voice components shipped in the [AI Voice Elements changelog of January 14, 2026](https://vercel.com/changelog/ai-voice-elements); Code components + the Attachments extraction in the [AI Code Elements changelog of January 21, 2026](https://vercel.com/changelog/ai-code-elements); and the latest release, 1.9.0, on [March 12, 2026](https://vercel.com/changelog/ai-elements-1-9). Some aggregators show a May 11, 2026 date, and the npm package metadata was last touched 2026-05-18 ([npmjs.com/package/ai-elements](https://www.npmjs.com/package/ai-elements)), but git history and the changelog posts put the component wave in January–March. There have been **zero releases since March 12, 2026**.

---

## 1. Component inventory (Aug 2026)

48 source files in [`packages/elements/src`](https://github.com/vercel/ai-elements/tree/main/packages/elements/src), grouped in docs as Chatbot / Code / Voice / Workflow / Utilities ([elements.ai-sdk.dev](https://elements.ai-sdk.dev/)).

**Structural change vs. 2025:** the standalone `Branch`, `Response`, `Actions`, `Loader` components no longer exist. `branch.tsx`, `response.tsx`, `actions.tsx` were deleted on 2025-11-06 (commit `64e9143`, "Delete unused components"); their functionality lives inside [`message.tsx`](https://github.com/vercel/ai-elements/blob/main/packages/elements/src/message.tsx) as `MessageBranch*`, `MessageResponse`, `MessageActions`, and `Loader` was replaced by `Shimmer` ([shimmer.tsx](https://github.com/vercel/ai-elements/blob/main/packages/elements/src/shimmer.tsx)).

Thread-relevant components:

| Component | File | What it does |
|---|---|---|
| **Conversation** (+Content, ScrollButton, EmptyState, Download) | [conversation.tsx](https://github.com/vercel/ai-elements/blob/main/packages/elements/src/conversation.tsx) | Scroll container: thin wrapper over `StickToBottom` from [use-stick-to-bottom](https://www.npmjs.com/package/use-stick-to-bottom) with `initial="smooth" resize="smooth" role="log"` |
| **Message** (+Content, Actions/Action, Branch\*, Response, Toolbar) | [message.tsx](https://github.com/vercel/ai-elements/blob/main/packages/elements/src/message.tsx) | Role-styled message frame, action buttons, branch pager, Streamdown markdown renderer |
| **Tool** (+Header, Content, Input, Output) | [tool.tsx](https://github.com/vercel/ai-elements/blob/main/packages/elements/src/tool.tsx) | Collapsible tool-call display: status badge, JSON params/result |
| **Confirmation** (+Title, Request, Accepted, Rejected, Actions/Action) | [confirmation.tsx](https://github.com/vercel/ai-elements/blob/main/packages/elements/src/confirmation.tsx) | Tool-approval UI (approve/deny), state-gated slots |
| **Reasoning** (+Trigger, Content) | [reasoning.tsx](https://github.com/vercel/ai-elements/blob/main/packages/elements/src/reasoning.tsx) | Collapsible thinking block; auto-open/auto-close on streaming, duration timer |
| **PromptInput** (~20 subcomponents: Textarea, Submit, Tools, ActionMenu, Select, AddAttachments, AddScreenshot, …) | [prompt-input.tsx](https://github.com/vercel/ai-elements/blob/main/packages/elements/src/prompt-input.tsx) (1,463 lines) | Composer form: text, attachments (picker/drop/paste), model select, submit/stop button |
| **Attachments** (+Attachment, Preview, Info, Remove, HoverCard, Empty) | [attachments.tsx](https://github.com/vercel/ai-elements/blob/main/packages/elements/src/attachments.tsx) | Display of file/source attachments; grid/inline/list variants (extracted Jan 2026) |
| **Sources**, **InlineCitation** | [sources.tsx](https://github.com/vercel/ai-elements/blob/main/packages/elements/src/sources.tsx), [inline-citation.tsx](https://github.com/vercel/ai-elements/blob/main/packages/elements/src/inline-citation.tsx) | Citation collapsible / hover-card carousel |
| **Artifact**, **CodeBlock**, **Snippet** | [artifact.tsx](https://github.com/vercel/ai-elements/blob/main/packages/elements/src/artifact.tsx), [code-block.tsx](https://github.com/vercel/ai-elements/blob/main/packages/elements/src/code-block.tsx) | Artifact panel chrome; Shiki-highlighted code with copy/language selector |
| **ChainOfThought, Plan, Task, Queue, Checkpoint, Context, Shimmer, Suggestion, ModelSelector** | same dir | Agent-progress and metadata displays (Context = token usage via `tokenlens`) |
| Code group: **Agent, Sandbox, Terminal, FileTree, Commit, StackTrace, TestResults, WebPreview, JSXPreview**, … | same dir | IDE/agent surfaces ([Jan 21, 2026 changelog](https://vercel.com/changelog/ai-code-elements)) |
| Voice group: **Persona, SpeechInput, Transcription, AudioPlayer, MicSelector, VoiceSelector** | same dir | Voice UIs ([Jan 14, 2026 changelog](https://vercel.com/changelog/ai-voice-elements)) |
| Workflow group: **Canvas, Node, Edge, Connection, Controls, Panel, Toolbar** | same dir | React Flow (`@xyflow/react`) wrappers |

"Slots" = `data-slot` attributes for CSS targeting of internal parts, present only on newer components (e.g., [transcription docs](https://elements.ai-sdk.dev/components/transcription): `data-slot="transcription"`); rollout incomplete.

**There is no edit-message component, no compare/side-by-side component, and no diff view for branches anywhere in the library** (verified by grep over all sources and docs).

---

## 2. Coupling audit (from source)

**Global finding:** every import from `ai` in all 48 files is `import type` — there are **zero runtime imports and zero hook calls** (`useChat`/`useCompletion` appear nowhere in `packages/elements/src`; verified by grep). `@ai-sdk/react` is only a devDependency of the workspace ([package.json](https://github.com/vercel/ai-elements/blob/main/packages/elements/package.json)). Components are props-in, state-out leaves; the app owns the render loop. However, the **registry install force-adds `ai`, `@ai-sdk/react`, and `zod` to your package.json** regardless of source usage (see §4).

Per component:

### MessageBranch — the crux, and the weakest fit
Source: [message.tsx#L116-L320](https://github.com/vercel/ai-elements/blob/main/packages/elements/src/message.tsx).
- Props: `MessageBranchProps = HTMLAttributes&lt;HTMLDivElement&gt; &amp; { defaultBranch?: number; onBranchChange?: (branchIndex: number) =&gt; void }`.
- State: **internal `useState(defaultBranch)` — uncontrolled only.** There is **no controlled `branch`/`index` prop**; `defaultBranch` is read once at mount. Ironically, `Reasoning` uses Radix `useControllableState` for its open state, but `MessageBranch` does not.
- Branch discovery: `MessageBranchContent` turns `children` into an array and registers it into context via `useEffect` (guarded by `branches.length !== childrenArray.length`), then renders **all branches simultaneously**, toggling `block`/`hidden` CSS classes on `index === currentBranch`.
- Navigation: `goToPrevious`/`goToNext` wrap around; `MessageBranchSelector` returns `null` when `totalBranches &lt;= 1`; `MessageBranchPage` renders `"{n} of {total}"`.
- **Verdict: purely client-side pager over already-materialized sibling subtrees.** It matches the "regenerate-siblings" model, not your universe-DAG. For an async re-bind that re-derives the message list: (a) you can't set the active index externally except by remounting with a changed `key`; (b) it requires all sibling branch contents mounted in the DOM; (c) `onBranchChange` fires synchronously before any data exists. Usable only as dumb pager chrome (`Selector`/`Previous`/`Next`/`Page` are trivial buttons); the state machine must be yours — or you fork the file, which the distribution model expects.

### Message / MessageContent — usable standalone
- `MessageProps = HTMLAttributes&lt;HTMLDivElement&gt; &amp; { from: UIMessage["role"] }` — `UIMessage` is a type-only import used solely to derive the role union (`"system" | "user" | "assistant"`); rendering is `is-user`/`is-assistant` class switching. `MessageContent` is `HTMLAttributes&lt;HTMLDivElement&gt;` — pure children. **No message object is ever passed; there is no UIMessage prop anywhere in the render path.** ([message.tsx#L33-L66](https://github.com/vercel/ai-elements/blob/main/packages/elements/src/message.tsx))

### MessageResponse (the former Response) — usable standalone
- `MessageResponseProps = ComponentProps&lt;typeof Streamdown&gt;`; wraps the [streamdown](https://streamdown.ai/) package (v2.x) with plugins `{cjk, code, math, mermaid}`, memoized on `children` and `isAnimating` ([message.tsx#L322-L342](https://github.com/vercel/ai-elements/blob/main/packages/elements/src/message.tsx)). Streamdown is Vercel-maintained but AI-SDK-independent: it renders **any incrementally growing markdown string**, repairing incomplete blocks during streaming ([streamdown.ai](https://streamdown.ai/)). Caveat: requires `@source "../node_modules/streamdown/dist/*.js"` in `globals.css` or styles silently break ([message docs](https://elements.ai-sdk.dev/components/message)).

### Tool — adaptable with thin mapping
- `ToolHeader` props are a discriminated union: `{ type: ToolUIPart["type"]; state: ToolUIPart["state"]; toolName?: never }` | `{ type: "dynamic-tool"; state; toolName: string }`, plus optional `title` ([tool.tsx#L35-L45](https://github.com/vercel/ai-elements/blob/main/packages/elements/src/tool.tsx)). `type` is expected to be `` `tool-${name}` `` (the name is derived by stripping the `tool-` prefix) unless you pass `title`.
- `state` must be one of the **seven AI SDK v6 tool-part states**, hard-coded in label/icon maps: `input-streaming` ("Pending"), `input-available` ("Running"), `output-available` ("Completed"), `output-error`, `approval-requested` ("Awaiting Approval"), `approval-responded`, `output-denied` ([tool.tsx#L47-L65](https://github.com/vercel/ai-elements/blob/main/packages/elements/src/tool.tsx)).
- `ToolInput` takes `input: unknown` (rendered as JSON CodeBlock); `ToolOutput` takes `output` + `errorText` (ReactNode passthrough, or JSON/string in CodeBlock). No callbacks, no execution, no hooks. **Verdict:** stateless display; map your runtime's tool lifecycle onto those seven strings (or edit the copied file's maps).

### Confirmation (approval UI) — adaptable with thin mapping
- `ConfirmationProps = ComponentProps&lt;typeof Alert&gt; &amp; { approval?: { id: string; approved?: boolean; reason?: string }; state: ToolUIPart["state"] }`; renders `null` unless `approval` exists and state is past the input phases. `ConfirmationRequest` children show only at `approval-requested`; `ConfirmationAccepted`/`ConfirmationRejected` gate on `approval.approved` in response states; `ConfirmationAction` is a **plain Button — you wire `onClick` to your own server command** ([confirmation.tsx](https://github.com/vercel/ai-elements/blob/main/packages/elements/src/confirmation.tsx)). Fits a "server command that forks the universe" flow with a ~10-line adapter.

### Conversation — usable standalone
- Pure wrapper over `use-stick-to-bottom` (all props pass through: `ComponentProps&lt;typeof StickToBottom&gt;`); `ConversationScrollButton` consumes `useStickToBottomContext` ([conversation.tsx](https://github.com/vercel/ai-elements/blob/main/packages/elements/src/conversation.tsx)). The only structural AI SDK dependence in the file is the optional `ConversationDownload`, which takes `messages: UIMessage[]` and reads `message.parts[].type === "text"` — skip it or feed a compatible shape.

### PromptInput — usable standalone (fully controllable without useChat)
- `PromptInputProps` is a form: `onSubmit: (message: PromptInputMessage, event) =&gt; void | Promise&lt;void&gt;` with `PromptInputMessage = { text: string; files: FileUIPart[] }`, plus `accept`, `multiple`, `globalDrop`, `syncHiddenInput`, `maxFiles`, `maxFileSize`, `onError({code: "max_files" | "max_file_size" | "accept"})` ([prompt-input.tsx#L484-L512](https://github.com/vercel/ai-elements/blob/main/packages/elements/src/prompt-input.tsx)).
- On submit it converts blob: URLs to **data: URLs in memory** and passes them to your callback; clears on success, preserves input on error/rejection. Text state is uncontrolled (FormData) by default, controllable via optional `PromptInputProvider`.
- `PromptInputTextarea`: Enter submits (IME-composition-safe, Shift+Enter newline, respects disabled submit button), Backspace on empty removes last attachment, paste adds files.
- `PromptInputSubmit`: `status?: ChatStatus` (type-only import; union `"submitted" | "streaming" | "ready" | "error"` per [useChat reference](https://ai-sdk.dev/docs/reference/ai-sdk-ui/use-chat)) + `onStop?: () =&gt; void`. Behavior: `submitted`→spinner, `streaming`→stop square and the button becomes `type="button"` calling `onStop`, `error`→X, otherwise submit icon ([prompt-input.tsx#L1211-L1263](https://github.com/vercel/ai-elements/blob/main/packages/elements/src/prompt-input.tsx)). Trivial to feed from any status source.

### Attachments — usable standalone
- `AttachmentData = (FileUIPart | SourceDocumentUIPart) &amp; { id: string }` — i.e., plain `{ type, url, mediaType, filename }`-shaped objects; `Attachment` takes `data` + `onRemove?: () =&gt; void` (`AttachmentRemove` renders only when `onRemove` provided); variants `"grid" | "inline" | "list"` ([attachments.tsx](https://github.com/vercel/ai-elements/blob/main/packages/elements/src/attachments.tsx)). Display-only; **no upload logic exists**.

### Reasoning — usable standalone (the best-behaved one)
- Controlled or uncontrolled via Radix `useControllableState`: `open`, `defaultOpen`, `onOpenChange`, plus `isStreaming` and controllable `duration`. Auto-opens when streaming starts (unless `defaultOpen === false`), auto-closes 1s after streaming ends (once), measures thinking duration via `Date.now()` ([reasoning.tsx](https://github.com/vercel/ai-elements/blob/main/packages/elements/src/reasoning.tsx)). `ReasoningContent` takes `children: string` → Streamdown.

### Everything else in the thread set
`MessageActions`/`MessageAction` (Button + tooltip), `Sources`, `InlineCitation`, `Task`, `ChainOfThought`, `Plan`, `Queue`, `Checkpoint`, `Suggestion`, `Shimmer`, `CodeBlock`, `Artifact`: purely presentational, props/children only (verified by export-surface read of each file). `Context` needs `{ usedTokens, maxTokens, usage?, modelId? }` and uses `tokenlens` for cost display ([context.tsx](https://github.com/vercel/ai-elements/blob/main/packages/elements/src/context.tsx)).

**Summary verdicts:** usable standalone — Conversation, Message, MessageContent, MessageResponse, MessageActions, Reasoning, PromptInput suite, Attachments, Sources, CodeBlock, Artifact, and the rest of the display set. Adaptable with thin mapping — Tool (seven state strings, `tool-` prefix), Confirmation (state+approval shape), PromptInputSubmit (four status strings), ConversationDownload (UIMessage[]). Hard-wired to AI SDK — **none at runtime**; the only hard-wiring is distribution-level (§4) and type-level. Wrong state model for your architecture — MessageBranch (uncontrolled, client-side, all-branches-mounted).

---

## 3. The DIY gap without AI SDK

The docs' canonical pattern is: `useChat()` returns `messages`/`status`/`sendMessage`/`regenerate`, and **you** write the `messages.map(...parts.map(switch part.type))` render loop feeding Elements ([message docs usage](https://elements.ai-sdk.dev/components/message)). Elements never subscribe to anything. What [useChat](https://ai-sdk.dev/docs/reference/ai-sdk-ui/use-chat) normally supplies that your Session Runtime must replace:

1. **Streaming accumulation &amp; message projection** — useChat folds the SSE/UI-message-stream into `UIMessage[]` with typed parts (text/reasoning/tool/file/source). Your runtime already owns this; you only need a mapping from your projection to per-component props (strings, state enums, part objects).
2. **Status machine** — `"submitted" | "streaming" | "ready" | "error"` feeding `PromptInputSubmit`; plus `stop()` → `onStop`, `clearError()`.
3. **Tool lifecycle + approvals** — useChat's `addToolApprovalResponse()`/`addToolOutput()` and the seven part states; you must emit equivalent states from your event stream and wire `ConfirmationAction` buttons to your fork-command.
4. **Branch state machine — DIY even with AI SDK.** The docs state: "the AI SDK does not provide built-in branching support, you have full flexibility to design and manage multiple response paths" ([message docs](https://elements.ai-sdk.dev/components/message)). For your async re-bind you additionally bypass `MessageBranch`'s internal index (own selector state; reuse only the button chrome, or fork the file).
5. **Edit flows — no component exists.** No edit-in-place UI, no "edit → fork" affordance anywhere; build textarea swap + submit-to-command yourself.
6. **Regenerate** — `MessageAction` is a bare button; useChat's `regenerate()` must become your fork/re-run command.
7. **Attachment upload state** — Elements hold picked files in memory as blob URLs and hand you data URLs on submit ([prompt-input.tsx#L862-L876](https://github.com/vercel/ai-elements/blob/main/packages/elements/src/prompt-input.tsx)); real upload (presigned URLs, progress, retry, CAS ingestion) is entirely yours, as is any per-attachment progress UI.
8. **Autoscroll edge cases** — largely covered: `use-stick-to-bottom` handles resize-driven growth, user-scroll cancellation, and smooth animation without `overflow-anchor` ([npm](https://www.npmjs.com/package/use-stick-to-bottom)). You still handle: scroll position across branch re-binds (a re-derived list will animate from `initial`; remount vs. preserve is your call), and any two-pane synchronized scrolling for compare views (nothing exists for this).
9. **Keyboard shortcuts** — only Enter/Shift+Enter/Backspace-attachment/paste ship in `PromptInputTextarea`; everything else (Cmd+K, arrow-to-edit, branch hotkeys) is yours.
10. **A11y** — leaf-level is decent (`role="log"` on Conversation, `aria-label`s, `sr-only` labels, ARIA on collapsibles via Radix); thread-level live-region announcements, focus management after re-bind, and skip navigation are yours.
11. **Persistence, resume, error recovery** — useChat's `resumeStream()`/transport layer has no Elements counterpart; your runtime owns it (which is the point).
12. **Side-by-side branch compare** — no component; compose two `Conversation` columns yourself (each `StickToBottom` instance is independent, so this works mechanically).

Net: for a runtime that already owns projection/status/commands, the gap is a **props-mapping layer plus branch/edit UI you were going to build anyway**. What you get is polished chrome: markdown streaming, collapsibles, composer ergonomics, scroll handling.

---

## 4. Distribution &amp; churn

**Distribution — shadcn-registry copy-in, no component npm package.**
- The npm package [`ai-elements`](https://www.npmjs.com/package/ai-elements) (v1.9.0, Apache-2.0) is a ~60-line CLI shim that detects your package manager and execs `npx shadcn@latest add https://elements.ai-sdk.dev/api/registry/&lt;component&gt;.json` ([cli/index.js](https://github.com/vercel/ai-elements/blob/main/packages/cli/index.js)). No args = install all.
- The registry is generated server-side from the monorepo sources by [apps/docs/app/api/registry/[component]/route.ts](https://github.com/vercel/ai-elements/blob/main/apps/docs/app/api/registry/%5Bcomponent%5D/route.ts): files land at `components/ai-elements/&lt;name&gt;.tsx` in your repo, with imports rewritten (`@repo/shadcn-ui/...` → your shadcn paths, `@repo/elements/...` → `@/components/ai-elements/...`), and inter-component deps resolved to `registryDependencies`.
- **The registry route unconditionally injects `ai`, `@ai-sdk/react`, and `zod` into every item's npm dependencies** (code comment: "Registry should auto-add ai sdk v5 as a dependency" — stale comment, live behavior), so installing even the purely presentational components adds the AI SDK to your package.json unless you prune it afterward. Since the dependency is unversioned, shadcn will install whatever `ai@latest` is — **currently v7** — while the copied sources were written against v6 types (untested combination; see unknowns).
- **Updates: overwrite, no merge.** The shadcn CLI has `--overwrite` (default false) and `--diff`, nothing else; docs don't address updating locally modified components at all ([ui.shadcn.com/docs/cli](https://ui.shadcn.com/docs/cli); [elements.ai-sdk.dev/docs](https://elements.ai-sdk.dev/docs) is silent on updates). Once you edit a copied file, upstream updates are a manual diff exercise. Corollary: forking `MessageBranch` is a sanctioned workflow, not a hack.
- **License: Apache-2.0** ([LICENSE](https://github.com/vercel/ai-elements/blob/main/LICENSE), [cli/package.json](https://github.com/vercel/ai-elements/blob/main/packages/cli/package.json)).
- **Platform assumptions:** React 19 (no forwardRef), Tailwind CSS 4 CSS-variables mode, Next.js + AI SDK listed as prerequisites ([docs](https://elements.ai-sdk.dev/docs), [README](https://github.com/vercel/ai-elements)). React-only — no Svelte/Vue ([#66](https://github.com/vercel/ai-elements/issues/66), [#70](https://github.com/vercel/ai-elements/issues/70), both open, unplanned).

**AI SDK version state (Aug 2026):**
- `ai` npm dist-tags: `latest: 7.0.58`, `ai-v6: 6.0.246`, `ai-v5: 5.0.228`. **AI SDK 7 GA'd June 25, 2026** ([changelog](https://vercel.com/changelog/ai-sdk-7); [migration guide](https://ai-sdk.dev/docs/migration-guides/migration-guide-7-0) — Node 22+, ESM-only, prompt/system-message and prepareStep breaking changes). AI SDK 6 GA'd December 22, 2025 ([blog](https://vercel.com/blog/ai-sdk-6)) — it introduced the tool-approval states Elements' Tool/Confirmation render.
- AI Elements 1.9.0 (March 12, 2026) pins `ai: ^6.0.105` ([package.json](https://github.com/vercel/ai-elements/blob/main/packages/elements/package.json)) and **has not shipped a v7-aligned release in the ~7 weeks since v7 GA**. I found no v7-compatibility issue in the tracker as of 2026-08-10 (searched via GitHub API) — plausibly because type-only usage keeps most things compiling, but it's unverified.

**Cadence (last ~12 months, npm publish dates + git):** roughly monthly-or-faster through early 2026 — 1.7.0 (2026-01-16, Voice), 1.8.0 (2026-01-21, Code + Attachments), 1.8.1–1.8.4 (Jan 26–Feb 5), 1.9.0 (2026-03-12) — **then nothing for 5 months**. Repo commits continue at low intensity (last component-source change 2026-05-27, last commit 2026-07-09, mostly docs/skills/CI; open July PRs are mic-selector fixes). One breaking rename wave in ~15 months (Branch/Response/Actions/Loader → Message\*/Shimmer, Nov 2025) with no published migration guide — copy-in users found out by re-pulling.

---

## 5. Signals of intent

- **Positioning is AI-SDK-first, not AI-SDK-only-by-mechanism.** Launch post: "customizable React components for building interfaces with the Vercel AI SDK … you can use `useChat` from the AI SDK to manage state and streaming, and render responses using AI Elements" ([Aug 6, 2025](https://vercel.com/changelog/introducing-ai-elements)). Docs live on the AI SDK's own domain (`elements.ai-sdk.dev`), list "a Next.js project with the AI SDK installed" as a prerequisite, and every canonical example (14 files across docs and examples, plus the agent [SKILL.md](https://github.com/vercel/ai-elements/blob/main/skills/ai-elements/SKILL.md)) wires `useChat`. The registry force-adds the SDK. **There is no official statement anywhere about using Elements without the AI SDK** — neither endorsement nor discouragement ([docs](https://elements.ai-sdk.dev/docs) verified silent).
- **But the architecture contradicts lock-in:** all-presentational components, type-only imports, and the docs' own branching callout ("the AI SDK does not provide built-in branching support; you have full flexibility") show the team deliberately keeps state out of the components. `Streamdown` and `use-stick-to-bottom` — the two load-bearing behaviors — are separate, SDK-independent packages.
- **Community:** tutorials pair Elements with the AI SDK (e.g., [LogRocket](https://blog.logrocket.com/vercel-ai-elements/)); I found no substantial public writeup of Elements atop a non-AI-SDK runtime, and no issue asking for one — the tracker's themes are new features, framework ports ([#66](https://github.com/vercel/ai-elements/issues/66)/[#70](https://github.com/vercel/ai-elements/issues/70)), and composer extensions ([#448](https://github.com/vercel/ai-elements/issues/448), mentions/slash-commands). Closed issue [#378](https://github.com/vercel/ai-elements/issues/378) shows even AI-SDK users hit type drift between Elements and `useChat` shapes.

---

## Hard facts vs. unknowns

**Hard facts**
1. Zero runtime AI SDK coupling in all 48 component sources; `ai` imports are type-only; no hooks ([src tree](https://github.com/vercel/ai-elements/tree/main/packages/elements/src), verified by grep at `0c1f5e8`).
2. `MessageBranch` is uncontrolled: `defaultBranch`/`onBranchChange` only, internal `useState`, all branches mounted and CSS-toggled; no external index control ([message.tsx](https://github.com/vercel/ai-elements/blob/main/packages/elements/src/message.tsx)).
3. `MessageResponse` = memoized [Streamdown](https://streamdown.ai/); works on arbitrary incremental markdown strings; needs a `globals.css` `@source` line.
4. `Tool`/`Confirmation` are stateless renderers of the seven AI SDK v6 tool states including `approval-requested`; approve/deny buttons are unwired ([tool.tsx](https://github.com/vercel/ai-elements/blob/main/packages/elements/src/tool.tsx), [confirmation.tsx](https://github.com/vercel/ai-elements/blob/main/packages/elements/src/confirmation.tsx)).
5. `PromptInput` is a self-contained form emitting `{ text, files: FileUIPart[] }` with files as data URLs; `PromptInputSubmit` maps `"submitted" | "streaming" | "ready" | "error"` + `onStop` ([prompt-input.tsx](https://github.com/vercel/ai-elements/blob/main/packages/elements/src/prompt-input.tsx)).
6. `Conversation` = [use-stick-to-bottom](https://www.npmjs.com/package/use-stick-to-bottom) wrapper.
7. Distribution is shadcn-registry copy-in (`components/ai-elements/*.tsx`); the CLI shells to `shadcn add`; updates overwrite, no merge ([cli/index.js](https://github.com/vercel/ai-elements/blob/main/packages/cli/index.js), [shadcn CLI docs](https://ui.shadcn.com/docs/cli)); registry force-adds `ai`, `@ai-sdk/react`, `zod` ([registry route](https://github.com/vercel/ai-elements/blob/main/apps/docs/app/api/registry/%5Bcomponent%5D/route.ts)).
8. License Apache-2.0; latest release 1.9.0 (2026-03-12); AI SDK latest major is v7 (GA 2026-06-25) while Elements pins `ai ^6`; old Branch/Response/Actions components were deleted 2025-11-06 in favor of Message-scoped versions.
9. No edit-message, no branch-compare, no upload machinery exists in the library.

**Unknowns / risks**
1. Whether the copied v6-typed sources typecheck cleanly against `ai@7` (registry installs unversioned `ai` → v7 today); no issue reports either way as of 2026-08-10.
2. Whether the 5-month release gap is a pause or a pre-v7-rework lull — no public roadmap statement found; repo commit activity suggests maintenance mode since March.
3. Whether Vercel will ever support controlled `MessageBranch` state — no open issue requests it; nothing planned publicly.
4. The "May 11, 2026" update date circulating in aggregators has no primary source; Vercel's own changelog dates are Jan 14, Jan 21, and Mar 12, 2026.
5. Slots (`data-slot`) coverage across older components — announced as incomplete; no published completion timeline.

**Bottom line for the architecture decision:** AI Elements is safe to adopt as owned, forkable chrome — every thread-surface component you need is presentational and feeds cleanly from a Session Runtime projection via a thin mapping (tool states, chat status, part shapes). The two places you'd fight it are exactly the two you already own: branch state (`MessageBranch` is a client-side sibling pager; keep only its buttons or fork it) and anything involving commands (edit, regenerate, approve — all bare buttons awaiting your wiring). The real coupling is operational, not architectural: an unwanted `ai`/`@ai-sdk/react` dependency injected at install (prunable), overwrite-only updates, one historical rename wave, and a library currently one major behind its own SDK with a 5-month release gap.</result>
<usage><subagent_tokens>111493</subagent_tokens><tool_uses>54</tool_uses><duration_ms>819026</duration_ms></usage>
</task-notification>

---
[2026-08-09T17:43] session 67f705b7

<task-notification>
<task-id>aa1a4bcfac66da48b</task-id>
<tool-use-id>toolu_01AvJnRPzdMWiMYd9fgdsFSm</tool-use-id>
<output-file>/private/tmp/claude-501/-Users-ren-repos-runtime/67f705b7-bf84-4a27-826f-9576a2a82ee2/tasks/aa1a4bcfac66da48b.output</output-file>
<status>completed</status>
<summary>Agent "Deep-dive assistant-ui internals" finished</summary>
<note>A task-notification fires each time this agent stops with no live background children of its own. The user can send it another message and resume it, so the same task-id may notify more than once.</note>
<result>All research is complete. Here is the report.

---

# assistant-ui — Technical Due Diligence (as of 2026-08-10)

**Snapshot:** `@assistant-ui/react` **0.15.12** (published 2026-08-09, per [npm](https://www.npmjs.com/package/@assistant-ui/react)); repo [assistant-ui/assistant-ui](https://github.com/assistant-ui/assistant-ui): 11,519 stars, 1,123 forks, 91 open issues, MIT, last push 2026-08-09 (GitHub API). Downloads: **6,193,033/month** for `@assistant-ui/react` ([npm API, 2026-07-10→08-08](https://api.npmjs.org/downloads/point/last-month/@assistant-ui/react)).

---

## 1. ExternalStoreRuntime: adapter API and branching

### 1.1 Exact adapter surface (verified against source, not docs)

Source of truth: [`packages/core/src/runtimes/external-store/external-store-adapter.ts`](https://github.com/assistant-ui/assistant-ui/blob/main/packages/core/src/runtimes/external-store/external-store-adapter.ts). `ExternalStoreAdapter&lt;T&gt;` fields as of 0.15.12:

| Field | Signature | Notes |
|---|---|---|
| `messages` | `readonly T[]` | Visible list; parent inferred as previous array element |
| `messageRepository` | `ExportedMessageRepository` | Alternative to `messages`: full branch tree `{ headId?, messages: [{ message, parentId, runConfig? }] }` |
| `onNew` (required) | `(message: AppendMessage) =&gt; Promise&lt;void&gt;` | |
| `setMessages` | `(messages: readonly T[]) =&gt; void` | Required for branch switching and fallback delete |
| `onEdit` | `(message: AppendMessage) =&gt; Promise&lt;void&gt;` | `AppendMessage` carries `parentId` and `sourceId`; the core routes to `onEdit` when `sourceId != null` or `parentId !== head` ([runtime core `append()`](https://github.com/assistant-ui/assistant-ui/blob/main/packages/core/src/runtimes/external-store/external-store-thread-runtime-core.ts)) |
| `onReload` | `(parentId: string \| null, config: StartRunConfig) =&gt; Promise&lt;void&gt;` | Inline comment: `// TODO: remove parentId in 0.12.0` (stale) |
| `onDelete` | `(messageId: string) =&gt; Promise&lt;void&gt; \| void` | Falls back to `setMessages` filtering if absent |
| `onCancel` | `() =&gt; Promise&lt;void&gt;` | |
| `onResume` | `(config: ResumeRunConfig) =&gt; Promise&lt;void&gt;` | Resume interrupted runs |
| `onResumeToolCall` | `({ toolCallId, payload }) =&gt; void` | Human-in-the-loop resume |
| `onRespondToToolApproval` | `(options: RespondToToolApprovalOptions) =&gt; Promise&lt;void&gt; \| void` | Tool-approval decision handoff |
| `onAddToolResult` | `(options: AddToolResultOptions) =&gt; Promise&lt;void&gt; \| void` | |
| `onRefetchThread` | `() =&gt; Promise&lt;void&gt;` | In-place refetch, drives `threads.reloadMainThread()` |
| `isRunning`, `isDisabled`, `isSendDisabled`, `isLoading` | `boolean` | |
| `convertMessage` | `(message: T, idx: number) =&gt; ThreadMessageLike` | Identity-cached per object reference |
| `queue` | `ExternalThreadQueueAdapter` | Message queueing/steering |
| `suggestions`, `extras`, `state` | | `state` is opaque JSON for export/import |
| `onImport`, `onExportExternalState`, `onLoadExternalState` | | Thread snapshot round-trip |
| `unstable_onBranchChange` | `(e: { headId: string \| null; visibleMessageIds: readonly string[] }) =&gt; void` | Added June 2026 in [PR #4543](https://github.com/assistant-ui/assistant-ui/pull/4543); fires only on explicit switches, de-duped, canonical (non-optimistic) head |
| `unstable_enableToolInvocations` / `setToolStatuses` | | Opt-in client-side tool execution pipeline |
| `unstable_capabilities` | `{ copy?: boolean }` | |
| `adapters` | `{ attachments?, speech?, dictation?, voice?, feedback?, threadList? }` | `threadList` (with `onSwitchToThread`, `onSwitchToNewThread`, `threads`, `archivedThreads`, `onRename/onArchive/onDelete/...`) is tagged `@deprecated ... under active development` |

Docs page: [/docs/runtimes/custom/external-store](https://www.assistant-ui.com/docs/runtimes/custom/external-store).

### 1.2 Who owns branch bookkeeping — the internal MessageRepository

assistant-ui's internal [`MessageRepository`](https://github.com/assistant-ui/assistant-ui/blob/main/packages/core/src/runtime/utils/message-repository.ts) **does own branch topology** in the legacy runtime. It is a linked tree (`Map&lt;id, {prev, children[], next, current, level}&gt;`); the visible thread is the path from root along `next` pointers to `head`; siblings = multiple `children` of one parent. Key mechanics, all from that file and [`external-store-thread-runtime-core.ts`](https://github.com/assistant-ui/assistant-ui/blob/main/packages/core/src/runtimes/external-store/external-store-thread-runtime-core.ts):

- **Flat `messages` mode:** each snapshot is ingested linearly (`parent = previous array element`). Branches exist only because earlier-seen siblings persist in the in-memory tree across renders. The docs confirm: "Branches are automatically tracked by assistant-ui by observing changes to the `messages` array" ([branching guide](https://www.assistant-ui.com/docs/guides/branching)). This is session-local; a reload loses branch structure.
- **`messageRepository` mode:** the app supplies the full tree (every branch's messages materialized) with explicit `parentId`s and a `headId`; the core diffs it into the internal tree (add/update, delete-missing, `resetHead`). Constructed via `ExportedMessageRepository.fromBranchableArray()`.
- **`switchToBranch(branchId)` is synchronous and in-memory only.** It throws `"Branch not found"` if the target id is not already in the internal tree, walks `next` pointers to that subtree's **leaf** (`findHead`), then calls your `setMessages` with the new visible path (mapped back to your original `T` objects via a WeakMap binding — only if they went through `convertMessage`). Return type is `void`; there is no async hook in the switch path.
- **Branch switches while `isRunning` are silently ignored** (`// Silently ignore branch switches while running`), and the capability `switchBranchDuringRun` is hard-coded `false`.
- **Branch counts cannot be supplied externally in the legacy runtime.** `getBranches(messageId)` returns `message.prev.children` — sibling ids of materialized tree nodes. There is no "branch count per message" input.
- **`resetHead` deletes descendant subtrees** when the head moves to an interior node (behavior introduced as "MessageRepository should delete dangling messages on resetHead", [CHANGELOG 0.10.46](https://github.com/assistant-ui/assistant-ui/blob/main/packages/react/CHANGELOG.md)). For your model (re-bind to an ancestor of a previously-seen node), the internal bookkeeping for everything below that node is destroyed and must be re-supplied.

**Answer for the legacy `useExternalStoreRuntime`:** the app can own branch topology *data* (via `messageRepository`) but not branch *behavior* — selection is resolved inside the internal tree, synchronously, against fully materialized in-memory messages. **Async on-demand branch fetch is not supported in this path.** `unstable_onBranchChange` only notifies after the fact for persistence ([external-store docs](https://www.assistant-ui.com/docs/runtimes/custom/external-store)).

### 1.3 The new answer: `ExternalThread` + `ExternalThreadBranchAdapter`

The repo is mid-migration to a new client architecture (`@assistant-ui/core` + `@assistant-ui/store` + `@assistant-ui/tap`; the old runtime layer literally lives in [`packages/react/src/legacy-runtime/`](https://github.com/assistant-ui/assistant-ui/tree/main/packages/react/src/legacy-runtime)). The new externally-owned-state surface is [`ExternalThread`](https://github.com/assistant-ui/assistant-ui/blob/main/packages/react/src/client/ExternalThread.ts), publicly exported from `@assistant-ui/react` and documented in the [External Store API reference](https://www.assistant-ui.com/docs/api-reference/external-store/runtime). Its props: `messages` (flat visible list), `isRunning`, `onNew/onEdit/onReload/onStartRun/onCancel/onResume`, tool callbacks, attachment/feedback/speech adapters, `queue`, and — decisive for you — `branches`:

```ts
// packages/core/src/runtime/branch/external-thread-branch-adapter.ts
export type ExternalThreadBranchAdapter = {
  /** Sibling branch ids for a message in display order, including the message's own id. */
  getBranches: (messageId: string) =&gt; readonly string[];
  /** Makes the given branch the visible one. The runtime is expected to swap
   *  the `messages` array to the selected branch. May be invoked
   *  programmatically while a run is in progress... */
  switchToBranch: (branchId: string) =&gt; void;
};
```

([source](https://github.com/assistant-ui/assistant-ui/blob/main/packages/core/src/runtime/branch/external-thread-branch-adapter.ts)). Here **the app fully owns branch topology**: `branchNumber`/`branchCount` are derived from `getBranches` (ids only — sibling *messages* need not be in memory), and `switchToBranch` is a fire-and-forget command — your Session Runtime can fetch the target path asynchronously and then swap the `messages` prop. The [test suite](https://github.com/assistant-ui/assistant-ui/blob/main/packages/react/src/tests/external-thread-branches.test.tsx) confirms: mounting via `useAui({ thread: ExternalThread(props) })` + `&lt;AuiProvider&gt;`, explicit `branchId` is "forwarded unvalidated", edges no-op, and without the adapter branching is off. Branch switching for ExternalThread landed 2026-06-11 ([PR #4359](https://github.com/assistant-ui/assistant-ui/pull/4359)); feature parity work (feedback, speech, attachments, transport props) was still landing through July–August 2026 ([CHANGELOG 0.14.29–0.15.11](https://github.com/assistant-ui/assistant-ui/blob/main/packages/react/CHANGELOG.md)). Caveat: `ExternalThread`'s edit payload "carries the edited message's own id as both `parentId` and `sourceId`" (adapter source comment), and there is no `docs/` guide for it yet beyond the auto-generated reference.

### 1.4 Community evidence on the legacy path's limits

- ["ExternalStoreRuntime seems incompatible with branching"](https://github.com/assistant-ui/assistant-ui/issues/3161) (Jan–Apr 2026): user discovers flat-mode parent inference; maintainer points to `messageRepository`, user then hits `setMessages` receiving internal `ThreadMessage[]` instead of their own type, broken WeakMap mapping, and identity-based caching stalling streaming. Maintainer (Yonom): "We check for message equality based on the identity of the object you pass us... **Sorry, this is still too complicated. We'll work on simplifying it much further**", and notes the AI SDK integration does *not* use `messageRepository` but `runtime.thread.import()` + `onImport`.
- ["Thread Branching for Server Fetched Threads"](https://github.com/assistant-ui/assistant-ui/issues/2047) (2025): answer is "pass pairs of `{ message, parentId }`" — i.e., materialize the whole tree client-side.
- Optimistic-id-swap phantom siblings required repeated fixes/reverts ([#4148](https://github.com/assistant-ui/assistant-ui/pull/4148), [#4149](https://github.com/assistant-ui/assistant-ui/pull/4149), [#4162](https://github.com/assistant-ui/assistant-ui/pull/4162), May 2026).

---

## 2. AssistantTransport

**What it is:** "a state-streaming protocol layered on `ExternalStoreRuntime`" — the backend streams snapshots of full agent state (any JSON), the frontend `converter` turns state into `{ messages, isRunning, state? }`; user actions flow back as **commands** (`add-message`, `add-tool-result`, plus custom) with `state`, `system`, `tools`, `threadId`, `parentId` in the POST body. Wire format is `aui-state:` prefixed ops (`set`, `append-text`) ([docs](https://www.assistant-ui.com/docs/runtimes/custom/assistant-transport)). Client hook `useAssistantTransportRuntime({ initialState, api, resumeApi?, resumeStateApi?, converter, headers?, body?, prepareSendCommandsRequest?, capabilities?: { edit?: boolean }, adapters?, onResponse?, onFinish?, onError?, onCancel? })`; server uses the `assistant-stream` package (npm + PyPI) ([same docs page](https://www.assistant-ui.com/docs/runtimes/custom/assistant-transport)).

**Maturity (Aug 2026):** first-class documented option, not labeled experimental, but: the docs state "**The wire format will migrate to Server-Sent Events (SSE) in a future release**" (line 277 of [assistant-transport.mdx](https://github.com/assistant-ui/assistant-ui/blob/main/apps/docs/content/docs/runtimes/custom/assistant-transport.mdx)); the message converter is still `unstable_createMessageConverter`; and a burst of queue/run-lifecycle bugfixes landed as recently as 0.14.29 (Jul 2026) — dropped commands, starved queues, leaked fetches ([CHANGELOG](https://github.com/assistant-ui/assistant-ui/blob/main/packages/react/CHANGELOG.md)). Editing is **disabled by default** (`capabilities: { edit: true }` to enable), and branching guidance is "truncate after parent, append, stream state back" — i.e., regenerate-style, server-truncating, not DAG-forking.

**Is ExternalStore being deprecated for it?** No. The ["Picking a runtime"](https://www.assistant-ui.com/docs/runtimes/pick-a-runtime) decision table keeps them as siblings: ExternalStoreRuntime = "Keep messages in redux, zustand, tanstack-query", AssistantTransport = "Stream full agent state snapshots (not just messages)", DataStream = "Backend that already speaks the data stream protocol". AssistantTransport is *itself built on* ExternalStoreRuntime ([architecture statement in docs](https://www.assistant-ui.com/docs/runtimes/custom/assistant-transport)), as are the AG-UI and AI-SDK integrations — so ExternalStore is load-bearing infrastructure. The real successor pressure is the internal **legacy-runtime → store/client (`ExternalThread`) migration** described in §1.3, which has no announced timeline.

---

## 3. Tool UI / generative UI

**The API churned in 2026.** `makeAssistantToolUI`, `useAssistantToolUI`, `makeAssistantTool`, `useAssistantTool` are all **officially deprecated**: "The component and hook based tool APIs are deprecated... Use a toolkit registered with `Tools({ toolkit })` instead" ([toolkit migration guide](https://www.assistant-ui.com/docs/migrations/toolkit-tools)); the API reference stamps `makeAssistantToolUI` with a Deprecated warning ([tools/rendering reference](https://www.assistant-ui.com/docs/api-reference/tools/rendering)). The old guide URLs (`/docs/guides/ToolUI`, `/docs/copilots/make-assistant-tool-ui`) now 404.

**Current API:** `defineToolkit` in a `"use generative"` file (a compiler plugin — `@assistant-ui/x-generative-compiler`, with `@assistant-ui/vite` — splits schema/executor/renderer across client/server), registered via `AuiConfig({ tools: Tools({ toolkit }) })` on `AssistantRuntimeProvider` ([Tool UI docs](https://www.assistant-ui.com/docs/tools/tool-ui), [Defining Tools](https://www.assistant-ui.com/docs/tools/defining-tools)). Five tool kinds: **backend** (server `execute`, client `render` only — your case for server-executed effects), **frontend** (`"use client"` execute), **human** (`execute: humanTool()` + `render` with `addResult` — explicit HITL primitive), **provider**, **external** (`execute: externalTool()`, renderer-only). Render props: `args, argsText, result, status, addResult, toolCallId, artifact` plus `renderText` shorthand; streaming-arg awareness via `useToolArgsStatus` ([status reference](https://www.assistant-ui.com/docs/api-reference/tools/status)).

**Approval flows are supported patterns:** server-side approval gates surface as `approval` + `respondToApproval({ approved, reason? })` on the renderer (added for AI SDK v6 `needsApproval` in [commit 32ae846 / #4107](https://github.com/assistant-ui/assistant-ui/commit/32ae846a91b61eccd01330693868a48f2f3bb0c4)); the ExternalStore adapter exposes the matching `onRespondToToolApproval` and `onResumeToolCall` callbacks (see §1.1 source); LangGraph has a dedicated [approval-UI tutorial](https://www.assistant-ui.com/docs/runtimes/langgraph/tutorial/part-3) and a [Mastra HITL example repo](https://github.com/assistant-ui/mastra-hitl). Beyond tool UIs there are `unstable_` **Interactables** — model-and-user co-edited stateful components with versioning ([docs](https://www.assistant-ui.com/docs/tools/interactables)). Attachments (adapter-based) and streaming markdown (`@assistant-ui/react-markdown`, or `@assistant-ui/react-streamdown` wrapping Vercel Streamdown with Shiki/KaTeX/Mermaid) are first-class ([streamdown docs](https://www.assistant-ui.com/docs/ui/streamdown)).

---

## 4. Friction and weaknesses (with evidence)

**Breaking-change cadence — high, no v1.** Still 0.x after 2.5 years. Breaking minors in the last 12 months: **0.11** 2025-09-08 ("runtime rearchitecture (unified state API)"), **0.12** 2026-01-24 ("use @assistant-ui/store to power state management" — "complete rewrite of the state management system", [v0.12 guide](https://www.assistant-ui.com/docs/migrations/v0-12)), **0.14** 2026-05-07 (drops v0.11/v0.12-deprecated APIs; `components` prop → children render functions, [v0.14 guide](https://www.assistant-ui.com/docs/migrations/v0-14)), **0.15** 2026-07-28 (drops the classic context hooks `useThread`, `useMessage`, `useComposer`, `useAssistantRuntime` etc. in favor of `useAui`/`useAuiState`; `AuiProvider` requires `AuiConfig(...)`; [v0.15 guide](https://www.assistant-ui.com/docs/migrations/v0-15), [CHANGELOG 0.15.0](https://github.com/assistant-ui/assistant-ui/blob/main/packages/react/CHANGELOG.md)). That's **four breaking minors in 12 months, ~one per quarter**, with codemods (`npx assistant-ui upgrade`) provided. The stated [deprecation policy](https://www.assistant-ui.com/docs/migrations/deprecation-policy) is blunt: **only "Primitives (except AttachmentPrimitive)" are Stable** (&gt;3-month notice); the **Runtime API, Context API, Message types, styled components, and shadcn styles are all "Beta"** (&lt;1-month notice); anything `unstable_` and the `RuntimeCore` API "may be removed at any time".

**ExternalStore pain points:** the whole §1.4 saga ([#3161](https://github.com/assistant-ui/assistant-ui/issues/3161) with the maintainer's "still too complicated" admission); `setMessages` type confusion in `messageRepository` mode; object-identity-based render caching that stalls naive streaming updates (same issue); phantom-sibling bugs from optimistic id swaps ([#4148](https://github.com/assistant-ui/assistant-ui/pull/4148)/[#4149](https://github.com/assistant-ui/assistant-ui/pull/4149)); duplicate-id handling churn ([#5262](https://github.com/assistant-ui/assistant-ui/pull/5262)); React **StrictMode** breakages as recently as July 2026 — "useAuiState/useExternalStoreRuntime never notify under React StrictMode (Next.js 16, React 19.2.4)" ([#5502](https://github.com/assistant-ui/assistant-ui/issues/5502), closed) and composer input dropped in the with-external-store example ([#5422](https://github.com/assistant-ui/assistant-ui/issues/5422)); a v0.15 regression where `useChatRuntime({ messages })` mounts an empty thread ([#5529](https://github.com/assistant-ui/assistant-ui/issues/5529), open).

**Provider/context complexity:** three architectural generations coexist (legacy runtime-core hooks → v0.12 unified state API → v0.15 `aui` property accessors + `AuiConfig` scopes like `Tools(...)`, `unstable_Interactables()`); the interactables docs even warn that legacy and new interactables scopes "are mutually exclusive" ([interactables docs](https://www.assistant-ui.com/docs/tools/interactables)).

**Styling:** still the shadcn copy-in model — components install from a registry (`https://r.assistant-ui.com/...`) into `components/assistant-ui/`, headless primitives stay in the package. Since July 2026 the registry serves **two flavors, Radix and Base UI** (shadcn's new default), selected by style name ([installation](https://www.assistant-ui.com/docs/installation), [base-ui page](https://www.assistant-ui.com/docs/base-ui)). Examples run **Tailwind v4** (`tailwindcss ^4.3.3` in [with-external-store/package.json](https://github.com/assistant-ui/assistant-ui/blob/main/examples/with-external-store/package.json)).

**Bundle:** `@assistant-ui/react@0.15.12` is **171.7 kB min+gzip (576.7 kB min)**, 18 dependencies including `zustand`, the full `radix-ui` package, and notably the `assistant-cloud` client as a hard dependency ([bundlephobia](https://bundlephobia.com/package/@assistant-ui/react), [npm](https://www.npmjs.com/package/@assistant-ui/react)); 2.5 MB unpacked.

**Docs quality:** breadth is good (an `llms.txt`/`llm.mdx` exists, auto-generated API reference), but URLs move without redirects (two former tool-UI URLs 404 today), the reference is typedoc-generated with thin prose, `ExternalThread` has no narrative guide, and the branching/external-store interplay was documented mostly *after* users fought it (user in [#3161](https://github.com/assistant-ui/assistant-ui/issues/3161): "there is few documentation about it, and even less complete examples").

**A11y:** actively worked but not settled — thread-list keyboard navigation added June 2026 ([#4627](https://github.com/assistant-ui/assistant-ui/pull/4627)), model-selector a11y fixes July 2026 ([#4682](https://github.com/assistant-ui/assistant-ui/pull/4682)), accessible names for icon-only controls ([#4564](https://github.com/assistant-ui/assistant-ui/pull/4564)), and an **open** "accessibility, overflow, and prop-range pass across all 100 elements" filed 2026-08-09 ([#5743](https://github.com/assistant-ui/assistant-ui/issues/5743)). RTL is documented ([rtl.mdx](https://github.com/assistant-ui/assistant-ui/blob/main/apps/docs/content/docs/(docs)/rtl.mdx)).

---

## 5. Project health

- **Velocity:** 1,963 GitHub release tags total (per-package); `@assistant-ui/react` shipped 6–11 npm releases/month over the last year (npm `time` data); commits daily, last push 2026-08-09 (GitHub API).
- **Bus factor:** 130 contributors, but founder **Yonom (Simon Farshid) has 2,215 commits vs 592 for the next human** (okisdev), and essentially every core-runtime changelog entry is his ([contributors API](https://api.github.com/repos/assistant-ui/assistant-ui/contributors), [CHANGELOG](https://github.com/assistant-ui/assistant-ui/blob/main/packages/react/CHANGELOG.md)). YC lists 3 employees ([YC profile](https://www.ycombinator.com/companies/assistant-ui)).
- **Adoption:** 11,519 stars; **6.19M monthly npm downloads** for the core package, `@assistant-ui/react-markdown` 712k/week, `@assistant-ui/react-ai-sdk` 387k/week ([npm API](https://api.npmjs.org/downloads/point/last-week/@assistant-ui/react-markdown)); README lists Mastra, LangChain, Browser Use as production users; LangChain's own docs carry an [assistant-ui integration page](https://docs.langchain.com/oss/python/langchain/frontend/integrations/assistant-ui).
- **Commercial layer:** [Assistant Cloud](https://www.assistant-ui.com/docs/cloud) is a hosted persistence service (thread history, thread list, auto-titles, per-user authorization). The OSS library is fully MIT and not feature-gated — persistence is DIY via adapters — but the cloud is promoted in docs/README, a `cloud` template ships in the CLI, and the `assistant-cloud` client is a dependency of the core npm package ([npm](https://www.npmjs.com/package/@assistant-ui/react)).
- **Funding:** YC **W25**; $500K pre-seed announced 2025-02-17 (YC; Tracxn also lists Eight Capital Management). **No subsequent round is publicly recorded** as of Aug 2026 ([Crunchbase](https://www.crunchbase.com/funding_round/assistant-ui-pre-seed--f2a73bf0), [Tracxn 2026 profile](https://tracxn.com/d/companies/assistantui/__q4UNwMXTw-rHBgY8XWPwHIWPXEAmoJffOxq1IdByDgQ), [PitchBook](https://pitchbook.com/profiles/company/756676-90)).
- **AG-UI relationship:** `@assistant-ui/react-ag-ui` is an official adapter for the AG-UI protocol (CopilotKit ecosystem) and **is layered on ExternalStoreRuntime** — stated in the [docs](https://www.assistant-ui.com/docs/runtimes/ag-ui/overview) and verified in [source](https://github.com/assistant-ui/assistant-ui/blob/main/packages/react-ag-ui/src/useAgUiRuntime.ts) (`useExternalStoreRuntime` from `@assistant-ui/core/react`); backed by MessageRepository since [PR #4938](https://github.com/assistant-ui/assistant-ui/pull/4938) after it was found to [flatten branch structure on load (#4774)](https://github.com/assistant-ui/assistant-ui/issues/4774).

---

## Hard facts vs unknowns

**Hard facts (source/API-verified):**
1. Legacy `useExternalStoreRuntime` branch switching is synchronous, in-memory, requires the target branch's messages to already be in the internal `MessageRepository`, throws on unknown ids, is silently ignored mid-run, and lands on the subtree's leaf — no async fetch seam ([runtime core](https://github.com/assistant-ui/assistant-ui/blob/main/packages/core/src/runtimes/external-store/external-store-thread-runtime-core.ts), [message-repository.ts](https://github.com/assistant-ui/assistant-ui/blob/main/packages/core/src/runtime/utils/message-repository.ts)).
2. `resetHead` to an interior node deletes all descendant bookkeeping — hostile to ancestor re-binding ([message-repository.ts](https://github.com/assistant-ui/assistant-ui/blob/main/packages/core/src/runtime/utils/message-repository.ts)).
3. The new `ExternalThread` client + `ExternalThreadBranchAdapter` (`getBranches(id) =&gt; ids`, `switchToBranch(id) =&gt; void`) gives the app full ownership of branch topology and makes async branch switching structurally possible (ids without materialized messages; switch is a command; app swaps `messages`) ([adapter type](https://github.com/assistant-ui/assistant-ui/blob/main/packages/core/src/runtime/branch/external-thread-branch-adapter.ts), [tests](https://github.com/assistant-ui/assistant-ui/blob/main/packages/react/src/tests/external-thread-branches.test.tsx)). This is the shape that fits your universe-DAG/fold model; the legacy adapter is not.
4. Editing routes to your `onEdit` with `parentId` + `sourceId` and the library waits for your state to resync — compatible with "edit = server fork command" ([runtime core `append()`](https://github.com/assistant-ui/assistant-ui/blob/main/packages/core/src/runtimes/external-store/external-store-thread-runtime-core.ts)).
5. Four breaking minors in 12 months; only Primitives have a &gt;3-month stability guarantee; the Runtime API tier you'd integrate against is officially "Beta" ([deprecation policy](https://www.assistant-ui.com/docs/migrations/deprecation-policy)).
6. `makeAssistantToolUI` is deprecated; toolkits (`defineToolkit` + compiler directive) are the current tool/HITL surface, with `humanTool()`, `addResult`, `approval`/`respondToApproval`, `onRespondToToolApproval` ([migration guide](https://www.assistant-ui.com/docs/migrations/toolkit-tools), [adapter source](https://github.com/assistant-ui/assistant-ui/blob/main/packages/core/src/runtimes/external-store/external-store-adapter.ts)).
7. AssistantTransport assumes server-truncation branching and snapshot-state streaming; its wire format has an announced future breaking migration to SSE ([docs line 277](https://github.com/assistant-ui/assistant-ui/blob/main/apps/docs/content/docs/runtimes/custom/assistant-transport.mdx)).

**Unknowns / risks:**
1. **Timeline and end-state of the legacy-runtime → store/client migration** — `ExternalThread` reached branch/attachment/feedback parity only in June–August 2026, has no narrative docs, and nothing states when (or whether) `useExternalStoreRuntime` will be deprecated. Betting on either surface means betting on an unannounced roadmap.
2. Whether `ExternalThreadBranchAdapter` semantics (e.g. unvalidated `branchId` forwarding, mid-run invocation) are stable — the type carries no `unstable_` prefix, but the Runtime API tier is Beta.
3. Runway: $500K pre-seed (Feb 2025) with no publicly recorded follow-on and ~3 employees, against 6M monthly downloads of support surface; sustainability depends on unannounced revenue/funding.
4. No formal a11y audit or conformance statement exists; the 100-element a11y pass is open ([#5743](https://github.com/assistant-ui/assistant-ui/issues/5743)).
5. Real-world `messageRepository`-mode correctness under heavy async resync (your SSE-fold case) is under-tested publicly — the maintainer's own integrations avoid that mode in favor of `thread.import()` ([#3161 comment](https://github.com/assistant-ui/assistant-ui/issues/3161)).</result>
<usage><subagent_tokens>144552</subagent_tokens><tool_uses>72</tool_uses><duration_ms>950908</duration_ms></usage>
</task-notification>

---
[2026-08-10T11:20] session f8eb4bad

<task-notification>
<task-id>b2yoi0dru</task-id>
<tool-use-id>toolu_01NqobTtacuirczDRK71irfS</tool-use-id>
<output-file>/private/tmp/claude-501/-Users-ren-repos-runtime/f8eb4bad-17c8-421c-ad65-6bdfc527cdf8/tasks/b2yoi0dru.output</output-file>
<status>completed</status>
<summary>Background command "Full suite run for accurate status" completed (exit code 0)</summary>
</task-notification>

---
[2026-08-11T15:19] session f8eb4bad

<task-notification>
<task-id>w83f4gg0g</task-id>
<tool-use-id>toolu_01W9buPbR6G7mFXrTjqm3aL5</tool-use-id>
<output-file>/private/tmp/claude-501/-Users-ren-repos-runtime/f8eb4bad-17c8-421c-ad65-6bdfc527cdf8/tasks/w83f4gg0g.output</output-file>
<status>completed</status>
<summary>Dynamic workflow "Design and build legible branch context, sibling navigation, and reversal in Encounter" completed</summary>
<result>{"spec":"# Encounter branch navigation — implementation spec\n\nSpine: a **persistent in-flow path bar** (replaces the fork success toast) + an **always-visible fork-point row** at the divergence message. Nothing here needs a new command, store op, or migration.\n\n## 1. Component inventory\n\n**`PathBar`** — new, `apps/web/src/components/path-bar.tsx`. Props: `{ binding: ContextBinding; head: string; ref?: string; emptyPath: boolean; liveExists: boolean; onReturnToLive: () =&gt; void; disabled: boolean }`. Full-width in-flow strip under `.topbar`, above the conversation; sticky at the scroller top on mobile; borrows `.edit-banner` (globals.css:831-843) as `.path-bar`. No close button. States: `live` (renders `null`), `side-path`, `pinned`, `compare`. `disabled` = streaming; buttons get `title=\"Wait for the reply to finish.\"`\n\n**`ForkPointRow`** — new, same file. Props: `{ message: ThreadMessage; siblings: readonly string[]; index: number; liveSiblingIndex: number; onSelect: (node: string) =&gt; void; disabled: boolean }`. Renders in flow *above* the divergence bubble, never hover-gated: hairline rule, count line, `&lt;fieldset className=\"branch-pager\" aria-label=\"Paths from this point\"&gt;` with `‹ ›`, caption, and a `.live-dot` marker.\n\n**`BranchPager`** (encounter-app.tsx:103-140) — deleted from `MessageActions` (:209) along with the `onSelectBranch`/`canSelectBranch` props threaded at :879/:882; its `.branch-pager` CSS (globals.css:513-524) is re-scoped under `.fork-point-row`.\n\n**Realm pill** (encounter-app.tsx:783-808) — text becomes `Live` (Radio) or `Not live` (GitFork). No raw ULID; the ref string moves into the bar body as selectable text.\n\n**`session-runtime.tsx`** — delete the success `setNotice` at :617 (keep every error notice). `updateBinding(node)` → `selectSibling(node)`: pin `branchTip(dag, node)` unless it equals `dag.refs.live`, in which case send `follow`/`live`. New `returnToLive()` gated on `canRead` only (never `canEdit` — compare zeroes it, `runtime.ts:803-811`). On leaving, store the departed ref in `ui-store` as `lastLeftRef` (per session; survives `resetConversationEphemera`).\n\n## 2. Exact copy\n\nPill: `Live` · `Not live`.\n\n**Side path** — title `Side path`.\nLine 1: `Replies here are real and recorded, and the model is still called as usual. What a side path cannot do is change anything in the outside world — no sending, no purchases, no tool actions.`\nLine 2: `Nothing you do here changes the main line, and the main line never picks up work from here on its own.`\nLine 3 (when `emptyPath`): `Nothing has been added here yet.`\nRef line: `Path: {binding.ref}`\nButton: `Back to the main line` · `title=\"This path stays exactly as it is.\"`\nHelper: `Leaving doesn't erase this path. Nothing here is overwritten — you just stop adding to it.`\n\n**Pinned** — title `Pinned to a fixed point`.\nLine 1: `You're viewing a fixed point instead of following the main line. Sending from here starts a new side path.`\nLine 2 as above. Same button and helper.\n\n**Compare** — title `Comparing points`. Line 1: `You're comparing two points. You can't send while comparing.` Same button.\n\n**On live, with `lastLeftRef`**: chip in the bar slot — `Return to the path you left` (selects that ref via `CheckoutContext`).\n\n**Return notice**: `Back on the main line. The path you left is still there.`\n\n**Fork-point row**: `{n} paths from this point` · caption `Path {i+1} of {n}` and, when that sibling reaches live, ` · continues on the main line` with `.live-dot`.\n\n## 3. Sibling model\n\nExtend `apps/web/src/lib/runtime-fold.ts` (keep `branchTip`):\n\n- `divergenceMessage(messages: readonly ThreadMessage[]): ThreadMessage | undefined` — the **last** message with `branches.length &gt; 1`, deduped by `message.node` (one node can emit several `dialog/` paths). Redacted rows carry `branches: []` (projection.ts:272) and are skipped.\n- `siblingReachesLive(dag, node, liveHead): boolean` — map `node` to its turn, BFS the inverted `turn.parents` edges, test whether the turn containing `liveHead` is reached. Never rank by `turn.generation` (unreliable, projection.ts:339).\n- `boundRealm(binding): \"live\" | \"side-path\" | \"pinned\" | \"compare\"` — `live` iff `mode===\"follow\" &amp;&amp; ref===\"live\"`.\n- `pathIsEmpty(dag, binding, head): boolean` — `mode===\"follow\" &amp;&amp; dag.refs[binding.ref] === head` and no ancestry message forks.\n\nSiblings are `message.branches` (universe-wide first-parent children, projection.ts:281-296); the main line's own version is in the set. No turn-summary labels — `turn.summary` is the assistant reply and falls back to `kind` (projection.ts:343-355).\n\n## 4. Reversal\n\nReturn to live: `UpdateBinding`, `payload: { surfaceId, binding: { mode: \"follow\", universe: snapshot.thread.universe, ref: \"live\" } }`. Render the button only when `dag.refs.live` exists. Re-entering a left path: `CheckoutContext`, `payload: { surfaceId, target: { mode: \"follow\", universe, ref: lastLeftRef } }`.\n\n**Discard does not exist and is never named.** `canon.refs` forbids deletion (`refs_guard`, 004_gc_role.cjs:59-81); the only affordance is leaving, and the helper copy says exactly that. No Promote button either — `runtime.ts:1901` drops `payload.effects`.\n\n## 5. Keyboard / a11y\n\nArrows are normal tab stops, **never disabled at the ends** (no-op instead, so focus is not dropped). `ArrowLeft`/`ArrowRight`/`Home`/`End` on the fieldset. One `.sr-only` `aria-live=\"polite\"` span, owned by `ForkPointRow` only, announcing `Now showing path 2 of 3` — **not** `role=\"status\"` (keeps `getByRole(\"status\")` unambiguous). Global Escape handler untouched. Every icon-only control keeps `aria-label`.\n\n## 6. Tests\n\n`apps/web/test/runtime-fold.test.ts`: `divergenceMessage` picks the deepest fork, dedupes duplicate nodes, ignores redacted `branches: []`; `siblingReachesLive` true on live's ancestry, false on a branch-of-a-branch, terminates on cycles; `boundRealm` across all four modes; `pathIsEmpty` true right after a fork.\n\n`apps/web/e2e/encounter.spec.ts`: retarget :219-224 from `.realm-pill.simulation` containing `exp/branch/` to the pill reading `Not live` **and** `.path-bar` containing `exp/branch/`; add — fork renders the bar immediately (no toast); `Back to the main line` restores `Live` and hides the bar; the fork-point row is visible without hover after an edit; arrow keys page siblings; axe passes with the bar mounted.\n\n## 7. Non-goals\n\nBranch rename or friendly names (ref origin is written, never read back); \"N ahead of live\" (`dag.refs` drops `position`); off-path sibling text (unreachable); a branch tree (`context-graph.tsx` exists); Promote; discard/delete; TTL or expiry wording; `compare` redesign; dropdown/popover primitives (none vendored).","implementation":"**Files changed**\n\n- `apps/web/src/components/path-bar.tsx` (new) — `PathBar` + `ForkPointRow`.\n- `apps/web/src/lib/runtime-fold.ts` — added `divergenceMessage`, `siblingReachesLive`, `boundRealm` (+ exported `BoundRealm`), `pathIsEmpty`; `branchTip` now shares the `turnOf`/`childTurns` helpers.\n- `apps/web/src/components/encounter-app.tsx` — deleted `BranchPager` and the `onSelectBranch`/`canSelectBranch` props; mounts `PathBar` in `.conversation-pane` above the scroller; renders `ForkPointRow` in flow above the divergence bubble (via `flatMap` with a constant `key=\"fork-point\"` so paging never remounts the pager and drops focus); realm pill now reads `Live`/`Not live`.\n- `apps/web/src/runtime/session-runtime.tsx` — fork success toast deleted (errors kept); `updateBinding` → `selectSibling` (pins `branchTip`, sends `follow`/`live` when the tip *is* live); new `returnToLive` (gated on `canRead`, records the departed ref) and `returnToPath` (`CheckoutContext`).\n- `apps/web/src/lib/ui-store.ts` — `lastLeftRef: Record&lt;sessionId, ref&gt;` + `rememberLeftRef`, outside `resetConversationEphemera`.\n- `apps/web/src/app/globals
... (truncated 10313 chars, full result in /private/tmp/claude-501/-Users-ren-repos-runtime/f8eb4bad-17c8-421c-ad65-6bdfc527cdf8/tasks/w83f4gg0g.output)</result>
<diagnostics>Per-agent results: /Users/ren/.claude/projects/-Users-ren-repos-runtime/f8eb4bad-17c8-421c-ad65-6bdfc527cdf8/subagents/workflows/wf_139ca43c-4cd/journal.jsonl — one {"type":"result",...} line per completed agent with its full return value.
If the result above is empty or unexpected, Read this file BEFORE diagnosing — do not assume agents returned non-empty results.
To re-run with edited post-processing: Workflow({scriptPath: '/Users/ren/.claude/projects/-Users-ren-repos-runtime/f8eb4bad-17c8-421c-ad65-6bdfc527cdf8/workflows/scripts/branch-navigation-ux-wf_139ca43c-4cd.js', resumeFromRunId: 'wf_139ca43c-4cd'}) — agents whose (prompt, opts) are unchanged replay from cache.</diagnostics>
<usage><agent_count>22</agent_count><agents_done>22</agents_done><agents_error>0</agents_error><agents_skipped>0</agents_skipped><agents_empty_result>0</agents_empty_result><subagent_tokens>1872678</subagent_tokens><tool_uses>547</tool_uses><duration_ms>3831419</duration_ms></usage>
</task-notification>

---
[2026-08-13T08:24] session 971c6429

<!-- attach -->
> B. 一个真实的哲学分歧
> 它主张 schema-on-read：写入时不分类，"系统提示词"不是存储类型而是 compile 时的一次角色分配。我们是写入时分类（§4 五类数据 review 强制、§9 路径布局法）。
> 
> 这个美学在我们的架构里买不起：per-path merge strategy、capability path scope、ScopedStateView 三堵承重墙全都建立在"路径即分类"上。反过来说，它没有这三样，所以它付得起。这是架构后果，不是品味之争。

仔细说

---
[2026-08-13T08:28] session 971c6429

真正被推迟的只有一个维度：WindowItem.region: 'instruction' | 'history' | 'workingset'。而且这个维度也不自由——§6.1 规定 instruction 区的门槛是 authority ≥ 3，即区域由写入时那个整数决定。那不是一次决策，是一次查表。

所以它做的事，准确讲是：把 role 维度换成了 authority 维度，并把"什么能进指令位"这个问题从 role 改绑到 authority 上。§7 的"双点执行"里，位置权限承担的正是 role 原来承担的活。

它对 chat API 的诊断是对的（"user role 名存实亡"、tool_result 塞进 user message 是历史包袱，§1）。但诊断被推广成了"一切写入时分类都是坏的"——这一步推广不成立，因为它把两种性质完全不同的分类混成了一件事：

详细说

---
[2026-08-13T08:49] session 971c6429

我认为这些可以直接变成compile流水线的一部分，然后又一个最小的，逻辑上最易懂的，新版本作为框架，这个流水线写入
你不觉得DAG作为“宇宙时空”和authority应该是分开的吗？authority是在moment中的一部分，它返回的error和handler是独立于agent的


这部分仔细说：它主张 schema-on-read：写入时不分类，"系统提示词"不是存储类型而是 compile 时的一次角色分配。我们是写入时分类（§4 五类数据 review 强制、§9 路径布局法）。

这个美学在我们的架构里买不起：per-path merge strategy、capability path scope、ScopedStateView 三堵承重墙全都建立在"路径即分类"上。反过来说，它没有这三样，所以它付得起。这是架构后果，不是品味之争。

---
[2026-08-13T18:37] session 30cb7da2

last agent completed phase 0, but overdid Phase 0 due to optimization target drift, should we undo some, if not all? or shall we leave it and start phase 1? I don't want too much verification and testing slow down us too much
the plan also has been updated, please trying to understand current codebase and the new direction, a lot of your memory needs to be adjusted

context:

```

- specs/history-kernel-mediated-runtime.md
- specs/history-core-execution-plan.md 的 Phase 1
- specs/acceptance/history-core/phase-0.md
- specs/history-core/schema-ownership.json
- specs/history-core/package-boundaries.json
- bench/results/history-core/phase-0.json

```

---
[2026-08-13T18:37] session 3a41ba34

last agent completed phase 0, but overdid Phase 0 due to optimization target drift, should we undo some, if not all? or shall we leave it and start phase 1? I don't want too much verification and testing slow down us too much
the plan also has been updated, please trying to understand current codebase and the new direction, a lot of your memory needs to be adjusted

context:

```

- specs/history-kernel-mediated-runtime.md
- specs/history-core-execution-plan.md 的 Phase 1
- specs/acceptance/history-core/phase-0.md
- specs/history-core/schema-ownership.json
- specs/history-core/package-boundaries.json
- bench/results/history-core/phase-0.json

```

---
[2026-08-13T18:37] session 5b71429d

last agent completed phase 0, but overdid Phase 0 due to optimization target drift, should we undo some, if not all? or shall we leave it and start phase 1? I don't want too much verification and testing slow down us too much
the plan also has been updated, please trying to understand current codebase and the new direction, a lot of your memory needs to be adjusted

context:

```

- specs/history-kernel-mediated-runtime.md
- specs/history-core-execution-plan.md 的 Phase 1
- specs/acceptance/history-core/phase-0.md
- specs/history-core/schema-ownership.json
- specs/history-core/package-boundaries.json
- bench/results/history-core/phase-0.json

```

---
[2026-08-13T18:52] session 30cb7da2

please update CLAUDE.md

"1.4k lines of self-tests for the verification harness itself" so you are basically saying the agent used for phase 0 behavior indicates it is gaming training? and wrote a bunch stuff, merge them, just for getting scores? did this do any damage to our codebase? or over complicating it? slowing it?

---
[2026-08-13T18:58] session 3a41ba34

Where the drift actually is (so we contain the pattern, not the code)
You're right that the target drifted from "establish the baseline" to "maximize acceptance-evidence strength": ~7.8k lines of harness including ~1.4k lines of self-tests for the verification harness itself, a 405-line process-group supervisor, a disposable-cluster manager whose internal contracts reached "v3", per-symbol repo inventories (package-boundaries.json is ~40k lines where the plan asked for an allowed-edge matrix + import-graph generator), and a 10k-line committed evidence file. The plan itself already forbids repeating this — §2.1 says the runner grows "只在出现真实 gate 时增量扩展", no pre-built generic sandbox/database-ownership/lineage systems, and §14.4's stop rules apply. So the containment is behavioral: future phases reuse this machinery as-is, add no harness self-tests, run only the suites each phase's gate section names, and accept that the inventories regenerate as big mechanical diffs per candidate.

could this be a big problem? another project of mine also used this agent, and its codebase also has gates like structure - and since then, progress got a lot slower and the work just becomes more complex with a lot comments that seems to be written to just "game training rewards"

---
[2026-08-14T15:54] session 30cb7da2

no need to put it in your memory, this is irrelevant. Instead, write a long prompt with all context and what you'd change, I think all that mentioned to be changed should - if not more, and edit its own claude.md and memory

it should also speed up the future development speed, by a lot

please write this prompt for me to copy, it can be as long as it needed, put details in

---
[2026-08-15T05:26] session 6c2b4950

<task-notification>
<task-id>a9dd145d52ef1e936</task-id>
<output-file>/private/tmp/claude-501/-Users-ren-repos-runtime/6c2b4950-c688-4929-9036-358b51b5eb95/tasks/a9dd145d52ef1e936.output</output-file>
<status>stopped</status>
<summary>No completion record was found for background agent "Map Invocation v1 and ingress" after it was re-dispatched via SendMessage in the previous session. It may have been stopped (via the UI, an SDK interrupt, or agent teardown — these leave no transcript marker), or it may have been running when the previous Claude Code process exited. Check its worktree/output for partial work before assuming the task landed.</summary>
</task-notification>

---
[2026-08-15T05:26] session 6c2b4950

<task-notification>
<task-id>a97c09b19a7d47915</task-id>
<task-id>a1cedf36f83ba5b94</task-id>
<task-id>abf81711e15a34fd5</task-id>
<task-id>a3ec7dd6c23561d72</task-id>
<task-id>a1c5851a040601a16</task-id>
<status>stopped</status>
<summary>No completion record was found for 5 background agents from the previous session: "Map Store publication semantics" (a97c09b19a7d47915), "Map Authority Kernel and budgets" (a1cedf36f83ba5b94), "Architecture delta review 0–2A" (abf81711e15a34fd5), "Map compiler pipeline for Phase 3" (a3ec7dd6c23561d72), "Map contact paths for Phase 4" (a1c5851a040601a16). They may have been stopped, or they may have been running when the previous Claude Code process exited — either way their transcripts are saved on disk, so their progress is not lost. Resume any of them by sending a message to its id with SendMessage, or check its worktree/output for partial work before assuming the task landed.</summary>
</task-notification>

---
[2026-08-15T05:26] session 6c2b4950

<task-notification>
<task-id>bhpznunes</task-id>
<tool-use-id>toolu_01RhoZJgMWq5h5q4RWgVg8qM</tool-use-id>
<status>stopped</status>
<summary>No completion record was found for this background shell command from the previous session. It may have been stopped (via the UI, Monitor timeout, or agent teardown — these leave no transcript marker), or it may have been running when the previous Claude Code process exited. Check the output file for partial results before assuming it completed.</summary>
</task-notification>

---
[2026-08-18T08:51] session 985b84e3

<!-- attach -->
> "Live" is a property of your binding, not of the path
> The pill reads off boundRealm() in runtime-fold.ts:127, which only looks at how your surface is attached to the graph:
> 
> {mode: "follow", ref: "live"} → Live
> {mode: "pinned", node} → Not live
> compare / none → Not live

explain in depth

---
[2026-08-18T11:44] session 985b84e3

let's consider more - what if the agent branched into 2-3 agents to deal with different tasks, while sharing the same context and workspace? codex does this
what if agent spawn a few sub agents, with new context but share workspace, or start new work tree?
what if we don't have workspace?
what if I switch to another branch, and keep context and workspace shared?

---
[2026-08-18T11:56] session 985b84e3

i know we have some constrains on claude.md, but they can, and should change according to situation
I know some operations may mess up, or create conflict, but they should still be allowed - dag, context, refs - but if their operation makes them lose pureness, it is ok, but it should be detected

and for workspace - we should allow a new branch to own its work tree, and merge back, wdyt?

and also think about the sdk surface of our context runtime - what operations should be allowed on history, context, ref, session? we should allow them to be edited by code

---
[2026-08-22T07:22] session e1235178

<task-notification>
<task-type>artifact-watch-lifecycle</task-type>
<summary>Stopped watching Artifact: "Everything Is a Plugin" (connection lost)</summary>
<event>Watch on https://claude.ai/code/artifact/7bd7db06-4f02-4485-9169-651b3ec8b115 ended — the live connection kept failing and reconnecting has stopped. This session will no longer hear when it is republished; watch it again if you still need that.</event>
</task-notification>

---
[2026-08-22T07:25] session e1235178

This session is being continued from a previous conversation that ran out of context. The summary below covers the earlier portion of the conversation.

Summary:
1. **Primary Request and Intent:**

   Four user turns drove this session, each escalating scope:

   a. **"agree with you, please finish R0"** — complete ADR-030's R0 pre-launch reset, continuing from parts 1–3a which had already landed.

   b. **"Deleting migration-era readers keeps unfreezing families / show me what are they, and why"** — a request to substantiate a claim I had made in a prior report. This turned into a verification exercise that found I had *overstated* the claim and had *accidentally deleted* a valid registry contract.

   c. **"no legacy should exist, and in general, I don't think we should have these gates, it is over done. so if any frozen gates is interfering, especially when we update our architecture, reason, then unfreeze or remove the gate"** — the pivotal standing directive. It (i) resolved a blocker I had stopped on (the mind-01 dependency), and (ii) authorized changing the freeze *rules themselves*, not merely reclassifying candidates.

   d. **"explain things you flagged"** — the current turn. Explain the two items I surfaced in my last report: the version-guard inversion bug I made and caught, and the `TransitionEngine`/enum-members finding I deliberately left as Ren's call.

2. **Key Technical Concepts:**
   - **context-runtime**: branchable persistent agent-state runtime on one Postgres; canon (append-only) / proj (disposable) / ops schemas; CR-CJSON/1 canonical encoding; OCC via read-trace witnesses; per-lease fencing; effect intent/observation bracket; replay seam (`liveThenReplay`); RLS tenancy.
   - **ADR-030 R0**: the pre-launch reset — one genesis migration (soft, re-editable until the first uncontrolled consumer), byte pins disarmed, no legacy, one version per family, every family tag renumbered to `/1`.
   - **The realm re-carve (decision 8)**: `live | simulation{world?} | replay` → `anchored | world{W} | detached`; `replay` leaves the axis (it is a `ReplayMode`); `anchored(realm) ⇔ class(ref) = anchor` as a biconditional.
   - **The Ref grammar**: `<class>/<name>(/<name>)*` with classes `anchor | branch | session | agents | eval | archive`; `exp/` and `sim/` merge into `branch/`; `anchor/main` is the genesis anchor.
   - **Freeze registry / rule of two**: a `freeze` requires two independent consumers, golden vectors, shared conformance, a compatibility reader, schema owners, a version rule, and a security gate. Decisions: `freeze | frozen-legacy-read-only | experimental | private-versioned`.
   - **Vector coherence vs. byte pins**: pins assert "these bytes"; *coherence* means the corpus must not contradict itself (derived digests, cross-references, canonical encodings). Pins are disarmed; coherence is recomputed.
   - **The probe method**: when unsure whether a branch is reachable, make it `throw` and run the whole suite rather than reasoning from the schema.

3. **Files and Code Sections:**

   - **`packages/domain/src/ids.ts`** — the root of the re-carve. `SimulationId` → `WorldId`; new `REF_CLASSES`, `refClass`, `ANCHOR_REF`, `isAnchorRef`; the three-arm realm; and the one derivation:
     ```ts
     export function bindingRealm(ref: Ref, world?: WorldId): ExecutionRealm {
       if (isAnchorRef(ref)) return { kind: "anchored" };
       return world === undefined ? { kind: "detached" } : { kind: "world", world };
     }
     ```
     `world` is passed rather than read because `workspace/world` has no bytes yet (D3 owns it) — "create the interface and stop".

   - **`packages/domain/src/authority/ids.ts`** — `refRealmClass` replaced by the biconditional:
     ```ts
     export function refAdmitsRealm(ref: Ref, realm: ExecutionRealm): boolean {
       return isAnchorRef(ref) === (realm.kind === "anchored");
     }
     ```
     The old namespace→class table could only state one direction; the direction it could not state ("this ref must not be anchored") is the one that gates effects.

   - **`packages/kernel/src/index.ts`** — the effect gate, previously spelled twice:
     ```ts
     function assertAnchoredEffectBinding(request: EffectAuthorityRequest): void {
       if (request.realm.kind !== "anchored" || !isAnchorRef(RefSchema.parse(request.ref))) {
         throw new KernelError("external effects require an anchored binding");
       }
     }
     ```
     Also: `StaticGrantTable` (lines 306-428) and `legacyDecision` (194-216) deleted; manifests now advertise `authority-port/1` only.

   - **`packages/tools/src/runtime-effect-adapter/index.ts:145-159`** — the site of the bug I flagged. Original:
     ```ts
     const actionFinalization =
       request.action.format === "effect-action/v1" ? "absorb" : request.action.finalization;
     ```
     My sweep produced `=== "effect-action/v2" ? "absorb" : …`. Current (correct):
     ```ts
     // One shape since R0: the action states its own policy, so there is no
     // version to branch on (ADR-030).
     const actionFinalization = request.action.finalization;
     ```

   - **`packages/tools/src/execution.ts`** — `EffectActionRecord` collapsed from a discriminated union to one strict object with `finalization` required; `effectActionFinalization` now `return action.finalization;`.

   - **`bench/scripts/history-core/vector-coherence.ts`** — grew from ~95 lines to a multi-pass tool. Ordered passes: (1) source-run digests + provenance recitation + `runManifest`, (2) cross-references, (2b) sibling citations, (2c) normalizer outputs + sensitivity, (2d) attestation→evidence citations, (2e) history-address corpus, (2f) evidence-anchor corpus, (2g) lease-binding→catalogue, (2h) transition preimages, (2i) variant mutation literals, (3) `derived` blocks, (4) canonical encodings last. Header states: *"Order matters and is not arbitrary… Running the passes in the other order needs a second run to settle, which would make 'did this converge?' a question rather than a fact."*

   - **`bench/mind/selection.ts`** (new) — the mind layer's five selection stages moved out of `@context-runtime/compiler`, with ties breaking by `codePointOrdering`.

   - **`packages/store/migrations/001_genesis.cjs`** — edited in place several times (soft genesis): promotion guards use `LIKE 'anchor/%'` with `COALESCE`, the permit realm-key CHECK re-carved, `canon.invocations` removed entirely, `history_nodes_transition_profile_check` narrowed to `envelope-v1`, family tags renumbered. `frozen-migrations.json` and `packages/store/src/migration-manifest.ts`'s `trustedManifestSha256`/`trustedManifestByteLength` re-pinned each time.

   - **`packages/product/src/mediation.ts`** — `MEDIATION_MATRIX` cardinalities corrected 2→1 for `chat-turn.ts#dispatch` and `#submit` after the dead path was deleted.

   - **`specs/acceptance/mind-01.md`** — status changed to **"stale — needs re-measuring"** with the two reasons (comparator changed; stages moved).

4. **Errors and fixes:**

   - **The guard inversion (the flagged bug).** A sweep rewriting `"effect-action/v1"` → `"effect-action/v2"` hit two ternaries whose *left operand was the version test*, inverting their polarity. Typechecks cleanly; `"absorb"` is a valid policy. Effect: `actionFinalization` pinned to `"absorb"` regardless of the record. Caught by `gateway-active-effect.test.ts` asserting `durableCalls === 1` and getting `0`. **I have now confirmed the full causal chain in this turn** by reintroducing the bug and instrumenting the mismatch branch:
     `MISMATCH {"tool":[...same...],"cls":[...same...],"fin":["absorb","publish-or-branch"],"format":"effect-action/1"}` — the request carries `publish-or-branch`; the pinned `"absorb"` made `actionFinalization !== request.finalization` true → `policy-refused` → the driver was never called. Restored and re-verified 5/5.

   - **Overstated claim, corrected (`32d8854`).** I had reported "two families lost their freeze". Checking the registry showed only `continuation-resolution` did. `context-materialization-vocabulary` remains frozen on the materializer + compiler core; `context-ir` was *already* `private-versioned` carrying "there is no second renderer". What was actually lost on the render side is untracked test evidence: `renderer.test.ts`'s cross-renderer comparison, which the registry never cited (0 citations, before and after).

   - **Accidental contract deletion (`32d8854`).** A line-range delete of `compilation-record-v1-v5` took `invocation-record-v1` with it. Its reader, consumer, and gate test all still existed. Restored verbatim from `pre-r0-baseline`. Root cause worth keeping: the registry's `--check` validates that *cited files exist*, not that every real contract is *listed*.

   - **Wrong rule implementation.** Scoping the compatibility-reader requirement, I first counted `schema.versions.length` — but `versions` is a list of format *tags*, not versions of one family (six `activation` tags at v1 are six families). Rewrote to group tags by family stem and count only stems with >1 version.

   - **`git checkout` reverting unrelated work** — twice: `vector-coherence.ts` (lost all extensions; rewrote via `Write`) and `postgres-store.ts` (lost three edits; re-applied).

   - **Brace-matching deletions overshooting** — removed a blob branch and a class declaration in `postgres/reader.ts`; restored and redid with exact string replacement. Similar issue removed the wrong registry candidate; switched to line-range cuts anchored on `id:` lines.

   - **`*/` inside a doc comment** (`activation.*/v1`) closed the block early → esbuild "Expected ; but found the".

   - **NUL-terminated domain tag** omitted from `payloadDigest`; found by comparing against a `derived` value computed by a real domain function.

   - **Session schema over-reach** — regenerating `packages/session/schemas/*.json` folded in pre-existing unrelated drift. Restored and applied only the ref-pattern change; spawned background task `task_721cccb1` for the drift.

   - **Renumber fallout, each fixed:** SQL `'/v' || version` expression; `apps/web/src/lib/conversation-creation.ts` namespace regex; negative test fixtures that became *valid* after renumbering; `EnvelopeSchema` numeric `version: 2` not covered by the tag sweep; duplicate `versions` entries after collapse; the supersession ledger's `history-core-source-provenance/v1`.

5. **Problem Solving:**

   - **Established the probe method**: when unsure whether a branch is reachable, make it throw and run the whole suite. Used to confirm three dead paths: the `legacy-record-v1` address synthesis (never fired), the null-history-row branch, and the Phase-4 chat turn path.
   - **Distinguished "our legacy" from "a vocabulary for classifying others"**: kept `authority.attested/v1` (live, phase-based decisions, four readers) while deleting `authority.static/v1`; kept `AuthorityProtocolVersion` as an open declared string so `protocol-not-served` stays reachable.
   - **Recognised the recurring unfreeze pattern**: the rule of two's *second* consumer was usually the migration-era reader being deleted. Reported it as a change to the accepted frozen surface every time rather than absorbing it.
   - **Made the coherence pass converge in one run** by ordering values → citations → encodings, so "did this converge?" is a fact rather than a question.

6. **All user messages:**
   - "agree with you, please finish R0"
   - "Deleting migration-era readers keeps unfreezing families / show me what are they, and why"
   - "no legacy should exist, and in general, I don't think we should have these gates, it is over done. so if any frozen gates is interfering, especially when we update our architecture, reason, then unfreeze or remove the gate"
   - "explain things you flagged"

   (Prior-session standing constraints that remain in force, from CLAUDE.md: never weaken a frozen *correctness* semantic — canonical bytes, OCC, fencing, the effect bracket, erasure, replay, tenancy — to make an abstraction fit; one active writer per semantic; rule of two; never build ahead; when unsure, ask. Ren's freeze lift applies to *representational* constraints only. No credential/secret-handling instructions were given this session.)

7. **Pending Tasks:**
   - Finish answering "explain things you flagged" (the current turn).
   - **Awaiting Ren's decision**: whether to retire `TransitionEngine` (and with it the `legacy`/`legacy-engine`/`legacy-kernel` enum members and one two-driver conformance kit).

8. **Current Work:**

   Answering "explain things you flagged". I gathered hard evidence for both, and had *just* begun the final comparison for the second when the turn ended.

   **Flag 1 — the guard inversion.** Fully traced and confirmed this turn. Original code at `pre-r0-baseline:packages/tools/src/runtime-effect-adapter/index.ts:147-148`:
   ```ts
   const actionFinalization =
     request.action.format === "effect-action/v1" ? "absorb" : request.action.finalization;
   ```
   The sweep flipped `v1`→`v2`, pinning the value. Reintroducing the bug reproduced `durableCalls: 0`; instrumenting produced the decisive line `"fin":["absorb","publish-or-branch"]`. Fix restored; `gateway-active-effect.test.ts` 5/5; tree clean.

   **Flag 2 — `TransitionEngine`.** Verified every reference in `packages/product/src`, `packages/terminal/src`, `packages/agents/src/reference-driver/driver.ts`, `packages/tools/src/index.ts`, `packages/host/src/publication-adapter/ports.ts`, and `packages/runtime/src/{engine,merge,rollout/actors,ports/index}.ts` is a **comment**. Only importers: `packages/runtime/src/index.ts` (barrel) and four test files totalling 1173 lines (`transition-engine-conformance.ts` at 998 lines with 12 `it` blocks). The enum members `legacy`/`legacy-engine`/`legacy-kernel` **are** produced — `specs/history-core/integrations/product-chat-scoped-active.json` classifies `TransitionEngine#execute` and `#transact` as `legacy` ("still on the pre-Phase-4 path pending an adopter reducer"), so deleting the members would make that profile lie.

   I had just retrieved both behaviour lists to determine whether retiring the engine loses coverage or duplicates it. Overlapping: lost-race refusal, deterministic branch publication, resubmission from durable settlement. Unique to the engine kit and *not* in the coordinator suite: "admits a concurrent write that is disjoint from what it read", "observes the exact reads and writes without committing anything", "refuses a generalized observation whose declared compilation read has moved", "recovers a lost acknowledgement by operation key", "makes a step adjunct durable with the write and leaves none behind on refusal".

   Final state: **13 commits since `pre-r0-baseline`; 560 files; ~475k lines deleted.** Registry at 11 contracts — 8 freeze, 2 experimental, 1 private-versioned, **zero `frozen-legacy-read-only`**. Suite 171/171 files, 1695 passed, 6 skipped; tsc clean; biome at its two pre-existing warnings; all five inventories green. HEAD is `2e2997c`.

9. **Optional Next Step:**

   Write the plain-text explanation of both flags — no further code changes. The evidence is gathered; what remains is presenting it.

   For flag 1: the guard's polarity inverted, it typechecked, and only a behavioural test caught it — with the confirmed mechanism (`"fin":["absorb","publish-or-branch"]` → `policy-refused` → driver never invoked).

   For flag 2: present the trade honestly as stated in commit `2e2997c` — *"Retiring the engine would also retire one of the two-driver conformance kits CLAUDE.md names as the real verification, which is a call I am not making unasked."* — and add the coverage comparison now in hand: five engine-kit behaviours (disjoint concurrent write, non-committing observation, moved compilation read, lost-ack recovery by operation key, step-adjunct durability) have no counterpart in `publication-conformance-suite.ts`, so retirement would lose them unless they are ported to the coordinator kit first.

If you need specific details from before compaction (like exact code snippets, error messages, or content you generated), read the full transcript at: /Users/ren/.claude/projects/-Users-ren-repos-context-runtime/c38e6a04-6315-4ec0-8cef-ba400c4b5d94.jsonl
Continue the conversation from where it left off without asking the user any further questions. Resume directly — do not acknowledge the summary, do not recap what was happening, do not preface with "I'll continue" or similar. Pick up the last task as if the break never happened.

---
[2026-08-22T08:13] session e1235178

embody the wisdom of software architect, let's find a elegant way that is both structurally elegant but smoothly adopt dsh plugin, we should loose/remove some guard.
the reason for that the old guard guards the old architecture, but we need architecture upgrade. I think many places compromised design due to gate, and we are still experimenting, so v1/v2 won't even make sense, and these gates won't either, they maybe useful locally but negative globally
