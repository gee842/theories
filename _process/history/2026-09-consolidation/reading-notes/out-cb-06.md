# Ideas from cb-06 (2026-08-31 – 2026-09-02)

**Read this caveat first.** cb-06 is 2496 lines and 34 of its 35 entries are `<task-notification>` blocks — reports written *by* background agents and delivered *into* Ren's message stream. Only one entry (2026-09-01T07:24) contains prose that is not agent output: a context-compaction summary, whose section 6 ("All user messages") preserves roughly two dozen of Ren's directives verbatim, in English and Chinese. So the batch's Ren-voice yield is thin but unusually concentrated: a single window onto how he commissions, constrains, rules on, and interrogates a large build. The subject is **manifold** — the personal web environment he split out of the DeepSeek Harness on 2026-08-30/31, renamed, rescoped to `@manifold/*`, self-hosted at `git.datong.to`, brought level with 1,313 upstream commits in five waves, and then extended into an authenticated multi-user control plane with per-user isolated runners, hosted execution, and shared Notes. Below, tier A is verbatim Ren; tier B is Ren's rulings as his agents report them back to him in the second person; tier C is the design of the thing he commissioned, agent-worded but owned by his decisions.

## Ideas

### A. Ren's own words (verbatim; all quoted inside the 2026-09-01T07:24 compaction summary, `manifold · session 4a7bdca0`)

1. **A dirty working tree is a stop condition, not something an agent tidies up.** He forbids the agent from resolving the precondition itself.
   > "If the dsh working tree is still dirty with phase-5 changes, stop and tell me — do not commit or stash it yourself."
   2026-09-01 · manifold · session 4a7bdca0 (compaction summary, §1) — `memories-and-working-style`

2. **The default environment of a machine is not the environment of a project; the project pins its own.**
   > "use Node via nvm (v22.22.2 — the default system Node is unsupported)."
   2026-09-01 · manifold · session 4a7bdca0 — `context-as-existence-runtimes`

3. **A new product starts as local git only — no remote, no push, no publish without explicit permission.** Existence before exposure.
   > "Create the new repository at /Users/ren/repos/manifold, local git only — no GitHub remote, no push, no npm publish without asking me."
   2026-09-01 · manifold · session 4a7bdca0 — `the-fork-and-cooperative-infrastructure`

4. **Do not translate docs.** A standing instruction that later hardens into the English-only rule for this repository.
   > "Do not translate docs."
   2026-09-01 · manifold · session 4a7bdca0 — `memories-and-working-style`

5. **The upstream is read-only: never modify tracked files under it.** The boundary between what you own and what you consume is enforced, not remembered.
   > "never modify tracked files under dsh/ (builds may emit into gitignored dsh/**/lib/)"
   2026-09-01 · manifold · session 4a7bdca0 — `context-as-existence-runtimes`

6. **Dependency direction is one-way and stated as a hard rule.**
   > "dependency direction is manifold→dsh only"
   2026-09-01 · manifold · session 4a7bdca0 — `context-as-existence-runtimes`

7. **Renaming has a boundary: identity strings that are shared vocabulary do not get renamed.** ctx keys, events, slots, the session event map and the vendored framework's names are the shared language between the two trees; the package scope is not.
   > "ctx keys, events, slots, SessionEventMap, and @deepseek-ai/cordis* vendor names do not rename"
   2026-09-01 · manifold · session 4a7bdca0 — `jian-and-wenyan-as-formal-language`

8. **The product must add no new session-level events and merge nothing into the shared event map.** A refusal to extend a shared namespace from a downstream position — later enforced as its own gate (`check:no-session-events`).
   > "no manifold-owned SessionEventMap merges or scoped events"
   2026-09-01 · manifold · session 4a7bdca0 — `context-as-existence-runtimes`

9. **Commits should be small and mechanical so a human can review them as a sequence.**
   > "Commit locally in small mechanical commits…"
   2026-09-01 · manifold · session 4a7bdca0 — `memories-and-working-style`

10. **When the tree contradicts the plan, stop and report — do not improvise a reconciliation.**
    > "stop at any blocking discrepancy with the plan and summarize what you found."
    2026-09-01 · manifold · session 4a7bdca0 — `memories-and-working-style`

11. **Pin the derivative to the exact commit of the parent at the moment of separation.** Identity of a fork is a coordinate, not a description.
    > "Pin manifold at the phase-5 commit once it exists."
    2026-09-01 · manifold · session 4a7bdca0 — `context-as-existence-runtimes`

12. **Delegate implementation to a stronger model in its own lane; keep the coordinator for judgment.**
    > "spawn opus for implementation, commit phase 5 first"
    2026-09-01 · manifold · session 4a7bdca0 — `memories-and-working-style`

13. **Coherence is not negotiable, and coherence includes surface strings.** The single most quotable line in the batch: no half-rebrands, no vestigial vendor prefix anywhere the product speaks as itself.
    > "no compromise on coherence, no DSH_, please continue"
    2026-09-01 · manifold · session 4a7bdca0 — `context-as-existence-runtimes`

14. **Own your framework: maintain your own copy of the substrate rather than tracking someone else's.**
    > "we should maintain our own cordis, we should maintain our own version of it"
    2026-09-01 · manifold · session 4a7bdca0 — `the-fork-and-cooperative-infrastructure`

15. **A live, evolving artifact should be treated as absent-and-changing, not as a contract.** He explicitly derates his own home directory as a stable surface.
    > "~/.manifold is not very important at this moment, it is still evolving, expect absence and change"
    2026-09-01 · manifold · session 4a7bdca0 — `keep-the-possibility-space-open`

16. **A constraint that serves the finished thing can be suspended during the phase that is making it.** Bilingual documentation parity is right for a shipped repo, wrong for a repo in motion.
    > "disable bilingual constrain for docs, at least during this dev cycle"
    2026-09-01 · manifold · session 4a7bdca0 — `memories-and-working-style`

17. **Generalize from one instance to its class.** He answers a single reported string with a rule for "this kind of situation".
    > "\"consumed web strings still print dsh web:/harness\" for this kind of situations, please change to manifold"
    2026-09-01 · manifold · session 4a7bdca0 — `memories-and-working-style`

18. **Aim for full completion of a plan, not a partial landing.**
    > "and also complete step 4, then 5... aim for full completion of the current plan"
    2026-09-01 · manifold · session 4a7bdca0 — `memories-and-working-style`

19. **A plan that has been executed changes status: proposed → implemented → approved.** Design documents have a lifecycle and the lifecycle is recorded.
    > "plan should move to implemented approved"
    2026-09-01 · manifold · session 4a7bdca0 — `memories-and-working-style`

20. **Self-host the code, under a name of one's own, on a domain named 大同.** The hosting decision, the naming decision and the disavowal of the vendor arrive in a single sentence — his personal infrastructure runs on `datong.to`.
    > "I want to host this repos at git.datong.to and its name should be manifold, no deepseek-ai or dsh"
    2026-09-01 · manifold · session 4a7bdca0 — `the-fork-and-cooperative-infrastructure`

21. **The mark is his to make; the placeholder stays until it exists.** He will not let an agent invent the product's logo.
    > "still working on logo, will update once i have it"
    2026-09-01 · manifold · session 4a7bdca0 — `memories-and-working-style`

22. **A suspension stays in force while the reason for it stays in force.**
    > "leave BILINGUAL_DOC_GATES_SUSPENDED we have more dev works coming"
    2026-09-01 · manifold · session 4a7bdca0 — `memories-and-working-style`

23. **He asks for an explanation of a residual gap rather than accepting it silently.** Item 7 of a completion report — the missing generated API regions — gets its own follow-up question.
    > "and after you are done, explain 7 No generated cordis-surface regions on manifold's subsystem pages"
    2026-09-01 · manifold · session 4a7bdca0 — `memories-and-working-style`

24. **Identity decisions answered in four words: owner, scope, sibling repo, timing.** He hosts the upstream fork under the same owner as the product.
    > owner "ren"; npm scope "@manifold/<x>"; host dsh "Yes, same owner"; "Configure + push now"
    2026-09-01 · manifold · session 4a7bdca0 (§1, §6) — `the-fork-and-cooperative-infrastructure`

25. **When the repository changes, does memory survive?** [zh] The first question he asks after the split is about continuity of the working self across a change of substrate — sessions, memory, history.
    > "现在我有几个问题想要清晰的理解：我们的repo换了，现在有了manifold的session - 记忆，历史记录还会载入吗？我现在直接换到manifold继续就可以了么"
    2026-09-01 · manifold · session 4a7bdca0 (§6) — `context-as-existence-runtimes`

26. **Ask for the shape of the whole before continuing.** [zh] He interrupts execution to demand an architectural account: what are these two repos now, and how are so many packages organized?
    > "现在这两个repo都是什么样的？manifest的codebase architecture是什么样的，这么多packages是如何组织的？"
    2026-09-01 · manifold · session 4a7bdca0 (§6) — `memories-and-working-style`

27. **Where are we and where are we going.** [zh] Progress and roadmap requested as one question.
    > "我们现在都完成了什么 roadmap是什么样的"
    2026-09-01 · manifold · session 4a7bdca0 (§6) — `memories-and-working-style`

28. **The governing statement of the whole batch** [zh]: manifold is a fork of dsh with no relationship to the vendor; leverage upstream's updates as far as possible while keeping one's own structure complete and elegant and the codebase sustainable. Independence, borrowing, integrity and sustainability held together as four simultaneous constraints.
    > "manifold是fork的dsh，和deepseekai没有关系，但想尽可能的leverage dsh的updates，同时保证自身结构的完整优雅，保证codebase的可持续性"
    2026-09-01 · manifold · session 4a7bdca0 (§6) — `the-fork-and-cooperative-infrastructure`

29. **Approve the direction, defer the pacing until the inventory is counted, and freeze the old branch as an archive.** [zh] Three moves in eleven characters: approval, deferral pending measurement, and preservation of the superseded state rather than deletion.
    > "批准，上有追赶清点结果出来再定，worktree/agentic-web-desktop 冻结存档"
    2026-09-01 · manifold · session 4a7bdca0 (§6) — `memories-and-working-style`

30. **Endorsement as a full speech act.** [zh] [endorsement]
    > "OK就按照这个方向继续"
    2026-09-01 · manifold · session 4a7bdca0 (§6) — `memories-and-working-style`

31. **Why staged absorption rather than one merge with the newest?** [zh] He challenges the wave method itself — the sharpest methodological question he asks in this batch — and pairs it with "where are we".
    > "解释下w3和之后的都是什么，为什么要w1 w2 w3而不是直接与最新的进行merge？我们现在的进度和roadmap在哪里"
    2026-09-01 · manifold · session 4a7bdca0 (§6) — `memories-and-working-style`

32. **Minimal continuation tokens once the method is agreed.** [zh] After the shape is settled he spends single words: "继续w3", "继续", "继续W5".
    > "继续w3" / "继续" / "继续W5"
    2026-09-01 · manifold · session 4a7bdca0 (§6) — `memories-and-working-style`

33. **Infrastructure choices are deliberate, not accidental** — he corrects the agent's model of his own host: Git-over-SSH is deliberately disabled on his Forgejo per his invariants, the CLI must use HTTPS plus an access token, and the token lives in the macOS Keychain through Xcode's system osxkeychain helper. (Reported as a user message with a Chinese explanation.)
    > "(User message reporting local commands + Chinese explanation) — Forgejo Git-over-SSH deliberately disabled per invariants.md; git.md mandates HTTPS + Forgejo access token"
    2026-09-01 · manifold · session 4a7bdca0 (§6) — `the-fork-and-cooperative-infrastructure`

34. **The milestone is named by its plan, not by its diff.** He opens by naming the note that governs the work, not the changes he wants.
    > "Implement the first milestone of the manifold product split: steps 1–3 of the plan…"
    2026-09-01 · manifold · session 4a7bdca0 (§6) — `memories-and-working-style`

### B. Ren's rulings, reported back to him in the second person by his own agents (paraphrase in the source, not verbatim Ren)

35. **He decides commit boundaries down to which file lands in which commit.**
    > "`built-boot.snapshot.ts` is in commit 2 by your instruction"
    2026-08-31T01:06 · manifold · session 4a7bdca0 — `memories-and-working-style`

36. **A branch may be deliberately red under its parent's gates.** He briefed that the fork-base branch is never validated by the upstream's own checks, so the agent refuses to "fix" a failure that is by design.
    > "Per your brief this branch is never validated by dsh's gates, so I did not improvise a fix"
    2026-08-31T10:07 · manifold · session 4a7bdca0 — `context-as-existence-runtimes`

37. **He chose the larger, more faithful inventory over the optimized one.** Offered a trim from 139 paths to 132 that would cut future conflicts, he first took the complete form.
    > "The A2 trim was not applied — you asked for the 139-path form"
    2026-08-31T10:07 · manifold · session 4a7bdca0 — `memories-and-working-style`

38. **A ruling can be right in intent and wrong in fact, and the agent must reconcile the two.** His ruling to keep "the headless-example row" named something that had never been in the inventory; the agent added it mechanically rather than authoring it.
    > "Your ruling said to keep \"the headless-example row\"; it could not survive a trim because it was never present, so I added it."
    2026-08-31T10:14 · manifold · session 4a7bdca0 — `memories-and-working-style`

39. **He reverses cleanly when the measurement contradicts him.** Both offered amendments were accepted in one turn.
    > "Both rulings applied. No ninth commit; the A2 trim is in and the branch is rebuilt."
    2026-08-31T10:14 · manifold · session 4a7bdca0 — `memories-and-working-style`

40. **Standing ruling: the fork base carries no documentation.** Seams are documented in the product's own notes, so package READMEs stay out of the delta and are not prose-merged every wave.
    > "Standing rulings: fork base carries no documentation"
    2026-09-01 · manifold · session 4a7bdca0 (§5) — `context-as-existence-runtimes`

41. **Standing ruling: a symbol the upstream deletes is not revived in the base — it moves into a package you own.** Do not keep a dead thing alive in the borrowed layer; adopt it into your own.
    > "symbols upstream deletes are not revived in the base but moved into manifold-owned packages"
    2026-09-01 · manifold · session 4a7bdca0 (§5) — `context-as-existence-runtimes`

42. **Standing ruling: the vendored framework directory is the project's own maintained fork**, not a tracking copy of anyone's upstream.
    > "`dsh/vendor` is the project's maintained Cordis fork"
    2026-09-01 · manifold · session 4a7bdca0 (§5) — `the-fork-and-cooperative-infrastructure`

43. **He prefers not to widen a stored contract when the consuming side can carry the concern.** Asked how to expire login attempts, he chose consuming-side sweeps over a new store method.
    > "the store lacks `sweepLoginAttempts`, so per your preference I used consuming-side expiry with **no new store method**"
    2026-09-02T08:07 · manifold · session 0edeb674 — `context-as-existence-runtimes`

44. **When a specified mechanism is proven not to achieve its purpose, he rules on the replacement himself.** Told that bubblewrap's launcher cannot forward SIGTERM, he decided to signal the sandboxed processes through the scope's cgroup directly.
    > "Graceful stop (coordinator's decision, implemented)"
    2026-09-02T06:11 · manifold · session 0edeb674 — `context-as-existence-runtimes`

45. **Agents must not build past the boundary of a decision.** The lane implemented the specified mechanism, stated the caveat honestly, and refused to build the working variant unasked.
    > "I implemented the mechanism as specified … and stated the caveat accurately in the README rather than claiming a graceful stop … I did not build that without approval."
    2026-09-02T06:03 · manifold · session 0edeb674 — `memories-and-working-style`

46. **Pushing is a decision he retains.** The permission classifier's refusal is escalated to him, not routed around.
    > "The permission classifier denied `git push origin main` twice. … This needs your approval or a Bash permission rule."
    2026-08-31T12:54 · manifold · session 4a7bdca0 — `memories-and-working-style`

47. **Some questions are the owner's, not the rebase's.** When absorption hit a design fork, the agent named the choice as his rather than resolving it.
    > "W2 itself is now blocked on one decision that is yours, not a rebase's: what happens to A5."
    2026-08-31T12:54 · manifold · session 4a7bdca0 — `memories-and-working-style`

48. **Adding a runtime row to a shipped profile is a product decision, not wave mechanics.** The agent recorded a standing obligation rather than changing composition unilaterally.
    > "adding runtime plugin rows is a product decision, not wave mechanics, and it should get its own review"
    2026-08-31T11:59 · manifold · session 4a7bdca0 — `memories-and-working-style`

49. **A repository URL cannot be invented.** With the hosting question open, 82 stale manifest URLs were left as an owner decision rather than guessed.
    > "Deliberately not touched, needs an owner decision … so I did not invent a URL."
    2026-08-31T01:06 · manifold · session 4a7bdca0 — `memories-and-working-style`

50. **Edit scope is stated per lane and honoured even when the fix is obvious.** Repeatedly: "outside my edit scope", "the edit limit named only the id/capabilities wiring", "runner-manager src is frozen".
    > "**Source change needed (NOT made — runner-manager src is frozen)**"
    2026-09-02T09:19 · manifold · session 0edeb674 — `memories-and-working-style`

51. **Prose amendments to design notes are drafted for him and applied by him.** Ten of the eleven lanes end with a section titled for his hand.
    > "### Text for you to apply" / "Note and doc amendments (for you to apply)" / "Text for the owner to apply"
    2026-09-02T07:46, 07:49, 08:56 · manifold · session 0edeb674 — `memories-and-working-style`

### C. The design of the environment he commissioned (agent-worded reports of Ren-owned decisions)

52. **manifold is the personal web environment that hosts applications; the agent harness is merely its first application.** The product identity is the environment, not the agent.
    > "the Manifold Web GUI serving this session" / brand pass renaming `HARNESS` → `MANIFOLD`
    2026-08-31T01:06 · manifold · session 4a7bdca0 — `context-as-existence-runtimes`

53. **Total identity means the whole surface, not the visible one**: banner text, CLI usage, manifest, storage keys, DOM markers, CSS custom properties, globals, symbols, probe routes, model-visible prompt descriptions. 3,903 rename sites across 1,126 files.
    > "Globals `__MANIFOLD_BOOT__`, `__MANIFOLD_TRANSPORT__`, `ManifoldWindow`; DOM markers `data-manifold-boot[-spinner]`; `--manifold-*` CSS custom properties (234 sites, 54 files)"
    2026-08-31T01:06 · manifold · session 4a7bdca0 — `context-as-existence-runtimes`

54. **The exception to total rebranding: a component keeps its own name where it speaks as itself.** The harness's self-description, its persona, its own skill docs stay in its voice.
    > "**`cordis` preset persona** … — the agent's own self-description."
    2026-08-31T01:06 · manifold · session 4a7bdca0 — `jian-and-wenyan-as-formal-language`

55. **A fork's relationship to its parent is an inventory, not a diff.** The "slim fork base" = one upstream SHA plus 8–11 named delta commits, each with an id, a purpose, a proving call site, a retirement condition and an exact path list; a gate proves the branch is exactly base + inventoried paths.
    > "`626e14b158 is b150a551b8 plus 138 inventoried path(s).`"
    2026-08-31T11:30 · manifold · session 4a7bdca0 — `context-as-existence-runtimes`

56. **Every delta must be justified by a call site you own, and must state the condition under which it dies.** Concerns carry `retirement` and `upstreamReference` fields; two retired by convergence when upstream adopted the same shape.
    > "each with `id`, `concern`, `owner: runtime`, `purpose`, `callSite`, `retirement`, `upstreamReference: null`"
    2026-08-31T10:32 · manifold · session 4a7bdca0 — `context-as-existence-runtimes`

57. **The answer to his own question about waves (idea 31), stated as a measured principle: the rebase is cheap; the product-side following is where the time goes.**
    > "Nothing in W1 suggests the transaction is fragile — it suggests the transaction is cheap and the *product-side following* is where the time goes."
    2026-08-31T11:59 · manifold · session 4a7bdca0 — `context-as-existence-runtimes`

58. **Drift is commit-rate-paced, not calendar-paced — there is no quiet period to wait for.** 1,313 upstream commits in nine calendar days.
    > "Drift is commit-rate-paced, not calendar-paced. 1,313 commits in 9 days (100–225/day). There is no quiet period to wait for."
    2026-08-31T09:57 · manifold · session 4a7bdca0 — `context-as-existence-runtimes`

59. **The recurring failure pattern of maintaining a derivative: "upstream moved a layer, the product must follow all the way."** Not a merge conflict — a companion that has to be adopted too.
    > "all the same family (upstream moved a layer, the product must follow all the way)"
    (corpus corroboration: `sources/13-claude-memories/claude-code-manifold/manifold-project-state.md`) — `context-as-existence-runtimes`

60. **A seam can be dissolved rather than grown.** When the coupling to be abstracted kept widening every wave, the answer was to alias the upstream names onto his own forks in the type facade, shrinking a 8-path concern to 2.
    > "**Dissolve the concern** — alias … onto manifold's own copies, keeping the packages withdrawn."
    2026-08-31T12:54 · manifold · session 4a7bdca0 — `context-as-existence-runtimes`

61. **Gates are the product's constitution.** Thirteen (later fourteen) named checks run as one command: typecheck, test, build, snapshot, cordis-config, paths-coverage, doc, rescope, no-session-events, submodule-clean, dsh-resolutions, fork-base, web, hosted.
    > "gates: typecheck, test, build, snapshot, cordis-config, paths-coverage, doc, rescope, no-session-events, submodule-clean, dsh-resolutions, fork-base, web — all passed"
    2026-08-31T11:30 · manifold · session 4a7bdca0 — `context-as-existence-runtimes`

62. **Every gate must be proved by a planted violation, then reverted.** A check nobody has seen fail is not evidence.
    > "Three planted violations, each failing on its own assertion, all reverted"
    2026-08-31T11:30 · manifold · session 4a7bdca0 — `memories-and-working-style`

63. **A gate matches the *shape* of a declaration, not the module it came from**, so an equivalent violation through another route is still caught.
    > "It matches the declaration *shape*, not the module specifier, so an equivalent merge through another route is caught"
    2026-08-31T04:25 · manifold · session 4a7bdca0 — `jian-and-wenyan-as-formal-language`

64. **A gate should state the condition under which it retires.** The no-session-events check carries a header saying when the bar lifts.
    > "Header states the bar lifts when dsh lands the out-of-repo event registration surface."
    2026-08-31T04:25 · manifold · session 4a7bdca0 — `keep-the-possibility-space-open`

65. **Verification must be byte-level, not descriptive.** Repeatedly: byte-identical config dumps across a pin bump, byte-identical Typert artifacts, mechanical substitution proofs that a re-recorded golden equals the substituted original.
    > "**Dump diff**: `manifold --dump-config --profile web` — 572 lines, **byte-identical** pre- vs post-bump."
    2026-08-31T01:40 · manifold · session 4a7bdca0 — `memories-and-working-style`

66. **Verification must not require a secret.** Every lane replays keylessly; the machine has no API key and keyed lanes self-skip.
    > "keyless; memory store by default" / "No item required a live API."
    2026-09-02T08:56, 2026-08-31T01:13 · manifold — `context-as-existence-runtimes`

67. **A claim in a design note without a corresponding test is itself a defect.** Two review sections are devoted entirely to "verification claims without tests".
    > "The note's \"control-store suite proves stale lease updates fail…\" is a statement about the fake."
    2026-09-02T05:01 · manifold · session 0edeb674 — `memories-and-working-style`

68. **A sentence in the docs that has become false is a change to make, not a nuance to tolerate.**
    > "that sentence is now false; suggest replacing it with …"
    2026-09-02T09:19 · manifold · session 0edeb674 — `memories-and-working-style`

69. **"Refusal is a value."** A named principle of the domain: a refused operation returns a typed rejection through the normal channel, it does not throw. The review's finding is that the principle was *broken* for ids the authority rejects.
    > "### 9. \"Refusal is a value\" broken for ids the authority rejects"
    2026-09-02T04:59 · manifold · session 0edeb674 — `jian-and-wenyan-as-formal-language`

70. **A protocol needs a name for every real outcome, or it lies.** Two lanes widen unions precisely because reality had a case the vocabulary could not say: `timeout` added to outcome reasons; `invalid-note-id` identified as the missing rejection code.
    > "`ExecutionProcessSnapshot['outcome'].reason` has no `timeout`, so a `RuntimeMaxSec` kill is reported as `killed`; widening the protocol union would let the wall-clock case be named."
    2026-09-02T09:20 · manifold · session 0edeb674 — `jian-and-wenyan-as-formal-language`

71. **The hard isolation invariant of a multi-user personal environment: nothing is shared between users except through a declared authority.**
    > "No event bus, object reference, Cordis service, or process is shared between users."
    2026-09-02T07:53 · manifold · session 0edeb674 — `relational-self-and-datong`

72. **One user gets one runner, and that runner is a whole environment, not a request handler.** A per-user `manifold web` process, leased, generation-fenced, spawned inside bubblewrap and a systemd user scope.
    > "each gets its own runner process and generation-1 lease"
    2026-09-02T08:56 · manifold · session 0edeb674 — `context-as-existence-runtimes`

73. **Durable identity must survive upgrade and rollback of the software that reads it.** The review's finding — homes keyed by profile *version* — was fixed to key homes by `(user, profile name)` and version only the runtime overlay.
    > "a promotion keeps Sessions, Spaces, settings, credentials, and plugins and a rollback returns to them"
    2026-09-02T07:49 · manifold · session 0edeb674 — `context-as-existence-runtimes`

74. **Placement is a property of durable state, not of a machine.** A stopped runtime must be reconstructible on another node from externally resolved state — proven by writing sessions and plugins on node A and reading them back on node B.
    > "`reconstructs a stopped runtime on another node from externally resolved durable state`"
    2026-09-02T07:49 · manifold · session 0edeb674 — `context-as-existence-runtimes`

75. **The arbiter of exclusivity must be the store, in one statement — not a read followed by an act.** Four separate findings collapse into this: refusal has to be atomic with acquisition.
    > "The generation bump is atomic; the refusal is not." → "The acquire statement itself refuses an active lease owned by another node"
    2026-09-02T04:59, 07:49 · manifold · session 0edeb674 — `context-as-existence-runtimes`

76. **A personal environment gives every chat the user's one tree.** The design rule chosen for workspaces, and the clearest statement in the batch of what "personal" means computationally.
    > "which is the hosted deployment and is also what a personal environment should do (every chat works in the user's one tree)"
    2026-09-02T10:44 · manifold · session 0edeb674 — `context-as-existence-runtimes`

77. **A workspace belongs to a session lineage, not to a session**, so a child agent edits the tree its parent can see.
    > "**One workspace per lineage, and the runner's own workspace directory is that volume.**"
    2026-09-02T10:44 · manifold · session 0edeb674 — `context-as-existence-runtimes`

78. **Nothing the plane reads is chosen by a link.** Canonicalizing a path proves only where it pointed a moment ago; content is read through a handle whose inode must still match.
    > "**Nothing the plane reads is chosen by a link.** Canonicalizing a path proves only where it pointed a moment ago"
    2026-09-02T10:44 · manifold · session 0edeb674 — `context-as-existence-runtimes`

79. **Caches of shared state must be monotonic**: an install takes only a higher revision, and a poll commits deltas against the listing it actually took.
    > "the cache is monotonic: an install takes only a higher revision"
    2026-09-02T07:53 · manifold · session 0edeb674 — `context-as-existence-runtimes`

80. **Announce after you commit, never before.** The first-ranked review finding: events were emitted before the cache held what they announced.
    > "a changed Note must already be readable at ≥ the announced revision; a deleted one must be gone"
    2026-09-02T04:59 · manifold · session 0edeb674 — `context-as-existence-runtimes`

81. **An outage posture must be stated, and it must be time-bounded.** Serve the last listing for thirty seconds, then fail closed for reads while writes keep crossing the authority — neither fail-at-boot-forever nor serve-stale-forever.
    > "after `staleAfterMs` (default thirty seconds) without a listing, reads fail closed … while writes keep crossing it"
    2026-09-02T07:53 · manifold · session 0edeb674 — `context-as-existence-runtimes`

82. **A protocol refusal and an infrastructure failure are different answers.** 400 with a stable code for what the authority will not consider; 503 `authority-unavailable` for a store that could not answer.
    > "a store or authority failure … answers 503 `authority-unavailable`"
    2026-09-02T07:53 · manifold · session 0edeb674 — `jian-and-wenyan-as-formal-language`

83. **Registries must not inherit.** Looking a kind up on a plain object let `constructor` name a validator; the fix — own keys only — is a general rule about namespaces that leak their substrate.
    > "Validators register by their own keys, so an inherited name such as `constructor` names no kind."
    2026-09-02T07:53 · manifold · session 0edeb674 — `jian-and-wenyan-as-formal-language`

84. **Authority is a stored row that an operator can narrow, not a constant in code.** The credential carries the account's stored root capability grant; narrowing the row narrows both sides at once.
    > "so narrowing the row narrows both sides"
    2026-09-02T08:07 · manifold · session 0edeb674 — `alignment-selection-on-cognition`

85. **Every audited action names a grant that exists.** Attribution is to a real authority row, not to a derived label.
    > "every audit `authorizedBy` names a row that exists"
    2026-09-02T08:07 · manifold · session 0edeb674 — `alignment-selection-on-cognition`

86. **Attribution must survive the long-lived stream.** Work started by a message on an open socket must be checked and audited under the identity that opened it, not against a fallback baseline.
    > "so stream-started Agent work is checked against the intersection and audited with its AuthSession rather than the baseline alone"
    2026-09-02T07:46 · manifold · session 0edeb674 — `alignment-selection-on-cognition`

87. **A tool the model can reach must not be able to change who may reach it.** The note tool touches content only; membership is out of its reach.
    > "the model cannot change membership"
    2026-09-02T04:59 · manifold · session 0edeb674 — `alignment-selection-on-cognition`

88. **Enforcement that is claimed but not measured is not enforcement.** systemd's `IPAddressDeny` on a user unit was measured unenforced; the plane now runs a real probe job and refuses to mint network grants while the probe says unenforced.
    > "`IPAddressDeny=` on a `systemd-run --user` unit is measured not to be enforced … so the properties stay only as defence in depth"
    2026-09-02T09:47 · manifold · session 0edeb674 — `alignment-selection-on-cognition`

89. **A probe that cannot answer counts as unenforced — fail closed.**
    > "a reached listener *or* a probe that cannot answer is `unenforced` (fail closed)"
    2026-09-02T09:47 · manifold · session 0edeb674 — `alignment-selection-on-cognition`

90. **A stronger check beats the specified check when the specified one can pass falsely.** The plan asked whether the firewall chain exists; the lane proved refusal instead, because a stale chain would pass an existence test.
    > "I implemented the stronger check (a real probe job proving refusal), since a loaded chain whose cgroup id went stale would still pass an existence check"
    2026-09-02T09:47 · manifold · session 0edeb674 — `memories-and-working-style`

91. **The enforcement boundary is its own gate on its own host.** `gates:linux` is not a row in the everyday roster; it is what a deployment passes before it ships.
    > "`gates:linux` remains the enforcement boundary."
    2026-09-02T08:56 · manifold · session 0edeb674 — `context-as-existence-runtimes`

92. **A negative control proves the test is not vacuous.** Assertions were deliberately flipped on the VM to confirm they could fail.
    > "Negative control run: flipping three assertions on the VM copy produced exactly the three expected failures … so the probes are not vacuous."
    2026-09-02T09:19 · manifold · session 0edeb674 — `memories-and-working-style`

93. **The environment a process runs in is not the environment a sandbox inherits.** Two blocking defects came from this gap; the fix clears everything and sets back exactly what was built.
    > "the sandbox clears it with `--clearenv` and sets back exactly the entries the manager scrubbed and built"
    2026-09-02T09:47 · manifold · session 0edeb674 — `context-as-existence-runtimes`

94. **What the runtime carries must be exactly what it needs and nothing of its host.** The env allowlist is five names; a sentinel exported into the host session provably does not reach the job.
    > "the job's `env` is exactly `HOME, L9_REQUEST_ENV, LANG, PATH, PWD, TMPDIR`"
    2026-09-02T09:47 · manifold · session 0edeb674 — `context-as-existence-runtimes`

95. **Repository metadata is masked from the sandbox** — the runtime a user's agent runs in must not be able to read the project's own git history.
    > "`.git` masked — a `.git/HEAD` sentinel in the runtime root lists as `[]` inside the sandbox"
    2026-09-02T09:19 · manifold · session 0edeb674 — `context-as-existence-runtimes`

96. **Sharing is opt-in per object with named members, and refusals distinguish "I cannot see it" from "I see it but do not own it" from "who is that".** Three answers where a lesser design would give one.
    > "distinguish a resource the caller cannot read (`unavailable`), one it reads but does not own (`forbidden`), and an unknown member or the owner itself (`invalid`)"
    2026-09-02T07:53 · manifold · session 0edeb674 — `relational-self-and-datong`

97. **Collaboration is proved end-to-end between two real people's runtimes** — an owner creates a Note, a second account cannot read it until granted editor, a third gets `missing-note`, and the Note survives the owner's runner restarting at a new generation.
    > "a third logged-in identity gets `missing-note` and an empty listing, and after the owner's runner restarts at generation 2 the Note is still read from the authority"
    2026-09-02T08:56 · manifold · session 0edeb674 — `relational-self-and-datong`

98. **The whole hosted composition must boot as a product at least once, on a developer's own machine, before it is believed.** That first boot found three defects that no unit test had.
    > "the first boot of this composition as a product"
    2026-09-02T08:56 · manifold · session 0edeb674 — `memories-and-working-style`

99. **A deployment recipe is a deliverable, and a preflight is what an operator runs before the services start.** One-node recipe, systemd user units, commented env examples, and a check-by-check preflight that skips cleanly off Linux.
    > "one line per check and non-zero on any failure. Every Linux-only check reports `skip` off Linux, so the same command is safe on a developer host."
    2026-09-02T10:29 · manifold · session 0edeb674 — `human-solutions-museum`

100. **Frozen archives are kept, not deleted, and every historical pin must stay fetchable.** Tags before every rebase exist so that an old commit can still initialize its own submodule.
     > "every base a live manifold commit pins stays fetchable"
     2026-08-31T13:32 · manifold · session 4a7bdca0 — `keep-the-possibility-space-open`

101. **A pre-release product discards existing local state rather than carrying migrations it has not earned.**
     > "Pre-release, no migration — any existing browser state is discarded."
     2026-08-31T01:06 · manifold · session 4a7bdca0 — `context-as-existence-runtimes`

102. **Fidelity to a mirror loses to correctness.** Where the upstream's own type facade carried dead targets, the fork dropped them and recorded the divergence.
     > "Mirror fidelity lost to correctness"
     2026-08-31T04:25 · manifold · session 4a7bdca0 — `memories-and-working-style`

103. **Two lockfiles written at different times resolve a range differently by construction** — so drift is a warning, and only a name someone pinned or patched on purpose is a failure.
     > "the version was chosen on purpose … and a **listed warning** otherwise"
     2026-08-31T04:25 · manifold · session 4a7bdca0 — `context-as-existence-runtimes`

104. **Fix the upstream option rather than the downstream workaround, and reject a workaround that couples to a private cache format across a repository boundary.**
     > "I rejected the one workaround that would have run … it couples to a private cache-key format across the repository boundary."
     2026-08-31T02:36 · manifold · session 4a7bdca0 — `memories-and-working-style`

105. **A cost that is real should be recorded with its price rather than left as an open question.**
     > "Recorded in the note with that cost stated, rather than left as an open question."
     2026-08-31T03:56 · manifold · session 4a7bdca0 — `memories-and-working-style`

106. **Names are load-bearing infrastructure**: a package whose name carries its group as a stem breaks every wildcard mapping and needs a literal entry.
     > "the group-glob assumption breaks whenever a package name carries its group as a stem"
     2026-08-31T11:59 · manifold · session 4a7bdca0 — `jian-and-wenyan-as-formal-language`

107. **A finding can be isolated or a class; audit for the class.** Having found one omitted load-bearing path, the agent cross-referenced all 431 consumed files to see whether the defect had siblings.
     > "**I audited for other instances of this defect class** and it is isolated."
     2026-08-31T10:14 · manifold · session 4a7bdca0 — `memories-and-working-style`

108. **Measure before you rebase.** The roster diff — which packages upstream added and removed — is a five-minute gate that tells you the shape of the whole wave.
     > "**Do the roster diff first, as a gate.**"
     2026-08-31T11:59 · manifold · session 4a7bdca0 — `memories-and-working-style`

109. **Do not extrapolate from the cheap case.** W1 cost 27 minutes and gave zero information about re-record cost, because no lane moved.
     > "**W1 cost 27 minutes; do not extrapolate.**"
     2026-08-31T11:59 · manifold · session 4a7bdca0 — `memories-and-working-style`

110. **When a delta and an upstream rewrite overlap heavily, do not blind-union the conflict** — take upstream's file and re-author your additions against precise anchors.
     > "**W4: A6 preset merge broke syntax twice** (naive \"keep both sides\" spliced mid-class)"
     2026-09-01 · manifold · session 4a7bdca0 (§4) — `memories-and-working-style`

111. **When the delegated channel keeps failing, take the work back into the loop that is stable.**
     > "8+ consecutive `Connection lost mid-response` errors across 5 agents; after backoffs failed, I took over all work in the main loop"
     2026-09-01 · manifold · session 4a7bdca0 (§4) — `memories-and-working-style`

112. **A defect that only the deployed shape exposes will not be found by unit tests mounted on a permissive root.** The hosted client read a sibling's service without declaring `inject`, and the lax composition path hid it.
     > "A Loader-mounted row reaches a sibling's service only through injection (the existing integration spec mounted on a root Context, where the lax path hid it)."
     2026-09-02T08:56 · manifold · session 0edeb674 — `context-as-existence-runtimes`

113. **Two behaviours that cannot both hold get named, not merged.** Lineage keying is the default and what the tests prove; a runner naming its own key overrides it — and which applies is made explicit rather than reconciled away.
     > "I kept both behaviours and made which one applies explicit"
     2026-09-02T10:44 · manifold · session 0edeb674 — `keep-the-possibility-space-open`

114. **A contradiction in the plan is recorded, not improvised around.**
     > "## Contradiction to record (nothing was improvised around it)"
     2026-09-02T10:44 · manifold · session 0edeb674 — `memories-and-working-style`

## Recurring preoccupations

**Coherence of a whole product surface (2026-08-30 → 08-31).** The thread that starts with "no compromise on coherence, no DSH_" (idea 13) runs through a 3,903-site rename (53), a named list of exceptions where a component still speaks as itself (54), and the refusal to let an agent invent the logo (21). He wants the thing to be one thing, all the way down to CSS custom property prefixes and model-visible prompt text — and he wants the exceptions *named*, not tolerated.

**Independence without isolation (2026-08-31).** "manifold是fork的dsh，和deepseekai没有关系，但想尽可能的leverage dsh的updates" (28) is the axis: take everything useful from a stream you did not author, owe it nothing, and keep your own structure "完整优雅" and "可持续". The whole slim-fork-base apparatus (55, 56, 60) is machinery for holding that contradiction open. His hosting choice — `git.datong.to`, under his own name, with the upstream fork mirrored under the same owner (20, 24) — is the same commitment expressed as infrastructure.

**Method as the object of scrutiny (2026-08-31 → 09-01).** He interrupts execution three times to ask for the shape rather than the next step: what are these repos now (26), what have we finished and where is the roadmap (27), and above all *why waves instead of one merge* (31). His agents then answer him in measured form — the rebase is cheap, the following is expensive (57); drift is commit-rate-paced (58); don't extrapolate from the cheap wave (109).

**Continuity of the working self across a change of substrate (2026-09-01).** "我们的repo换了…记忆，历史记录还会载入吗？" (25) is asked about a code repository, but it is the same question the corpus asks everywhere about context and existence. The 09-02 work answers it in the machine: homes keyed by identity not by build (73), runtimes reconstructible on another node (74), a Note still readable after its owner's runner restarts at a new generation (97).

**What "personal" means computationally (2026-09-02).** The whole second session is one long elaboration: one user, one runner, one home, one tree (72, 76, 77); nothing shared between users except through a declared authority (71); sharing as an explicit per-object membership with three distinct refusals (96). And, unavoidably, containment — because a personal environment that hosts other people's runtimes has to be able to prove what it prevents (88, 89, 94, 95).

**Evidence over assertion (throughout).** Byte-identical dumps (65), planted-then-reverted gate violations (62), negative controls (92), keyless replay (66), "a claim in the note without a corresponding test" as a first-class defect (67), "that sentence is now false" (68). The most characteristic sentence in the whole batch is a price tag followed by "Everything below is measured, not projected."

## Ideas that appear nowhere else in the corpus

- **The verbatim directives themselves.** `sources/13-claude-memories/claude-code-manifold/ren-working-style.md` and `manifold-project-state.md` carry the *substance* of nearly all of tier A in paraphrase; what only cb-06 preserves is Ren's own wording — "no compromise on coherence, no DSH_", "we should maintain our own cordis", "~/.manifold is not very important at this moment, it is still evolving, expect absence and change", "aim for full completion of the current plan", and the Chinese governing sentence (28). For a book, the wording is the artifact.
- **"~/.manifold is not very important at this moment, it is still evolving, expect absence and change" (15).** A first-person statement about treating one's own home directory as provisional. Nothing else in the corpus states this posture toward one's own persistent state.
- **The datong.to hosting decision as a single sentence pairing self-hosting, naming and disavowal (20).** The domain appears in memories and in `theories/context-as-existence-runtimes/synthesis-b-ember-fnar-and-other-runtimes.md`, but the moment of decision — and that the domain is 大同 — is only here.
- **"a personal environment should do (every chat works in the user's one tree)" (76).** The most explicit definition of personal computing anywhere in this batch's reach; the drafts describe multi-user runtimes but not this criterion.
- **"Refusal is a value" as a named domain principle (69),** and the connected discipline that a protocol must have a name for every real outcome or it lies (70, 82). This is the same instinct as the `jian`/`wenyan` work applied to an ordinary API surface, and it is not carried in the language drafts.
- **"Nothing the plane reads is chosen by a link" (78)** and **"Enforcement that is claimed but not measured is not enforcement" (88).** Two aphorism-quality formulations of epistemic discipline that emerged from systems work, not from the philosophical drafts.
- **The A2 episode (37–39)** — he chooses the complete inventory over the optimized one, is shown the ruling names something that never existed, and reverses in one turn. A rare recorded instance of the correction loop working in both directions.
- **The standing ruling that a symbol upstream deletes is not revived in the base but adopted into your own package (41).** A precise rule about how a dependent keeps something the source abandoned, which has obvious resonance with `human-solutions-museum` and is stated nowhere else.

## Ren's questions

All of these are verbatim, from §6 of the 2026-09-01T07:24 compaction summary.

- "现在我有几个问题想要清晰的理解：我们的repo换了，现在有了manifold的session - 记忆，历史记录还会载入吗？我现在直接换到manifold继续就可以了么" [zh]
- "现在这两个repo都是什么样的？manifest的codebase architecture是什么样的，这么多packages是如何组织的？" [zh]
- "我们现在都完成了什么 roadmap是什么样的" [zh]
- "解释下w3和之后的都是什么，为什么要w1 w2 w3而不是直接与最新的进行merge？我们现在的进度和roadmap在哪里" [zh]
- "and after you are done, explain 7 No generated cordis-surface regions on manifold's subsystem pages" [en]

Note the pattern: four of the five ask for the shape or the reason, not for the next action; only the fifth is about a specific gap, and even that is a demand for an explanation rather than a fix.

## Style and method notes

**He states preconditions and refuses to let them be resolved for him.** "If the dsh working tree is still dirty with phase-5 changes, stop and tell me — do not commit or stash it yourself." Then, in a later message, he authorizes exactly the act he had forbidden: "spawn opus for implementation, commit phase 5 first". The permission is separate from the work.

**He generalizes a report into a rule.** Given one example of a leaked string, he answers for the class: "\"consumed web strings still print dsh web:/harness\" for this kind of situations, please change to manifold". One instance in, one policy out.

**He corrects the model of the situation, not the output.** After the agent has been operating on the assumption that manifold is a downstream of a vendor it belongs to, he restates the whole relation in one sentence — "manifold是fork的dsh，和deepseekai没有关系，但想尽可能的leverage dsh的updates，同时保证自身结构的完整优雅，保证codebase的可持续性" — and the entire fork-base architecture follows from that correction rather than from any instruction about files.

**He approves, defers and preserves in the same breath.** "批准，上有追赶清点结果出来再定，worktree/agentic-web-desktop 冻结存档": approve the direction, hold the pacing until the count is in, and freeze the superseded branch rather than delete it. Deferral pending measurement, and preservation of what is being replaced, are both habitual.

**He compresses once the method is agreed.** After the wave method is explained he spends single tokens — "OK就按照这个方向继续", "继续w3", "继续", "继续W5". The verbosity is front-loaded into the framing; execution gets almost nothing.

**He keeps three classes of decision to himself**: what gets pushed ("This needs your approval or a Bash permission rule"), what the product's composition is ("adding runtime plugin rows is a product decision, not wave mechanics"), and what the product looks like ("still working on logo, will update once i have it"). His agents recognise these and route them back — "One thing left for you to decide", "needs an owner decision", "that is a different ruling".

**He wants the prose written for him but applied by him.** Every lane in the 09-02 session ends with a section addressed to his hand — "Text for you to apply", "Note and doc amendments (for you to apply)", "Text for the owner to apply". Design notes are amended by the owner; only code is delegated.

**He suspends rules with a stated scope and a stated reason.** "disable bilingual constrain for docs, at least during this dev cycle" and "leave BILINGUAL_DOC_GATES_SUSPENDED we have more dev works coming". A suspension has an expiry condition, which is the same discipline his gates carry ("Header states the bar lifts when…").

**A note on this batch's provenance.** Because 34 of 35 entries are agent reports pasted into his message stream, the *style* visible here is largely the style he has trained into his agents: price tag first, measured not projected, contradictions recorded rather than improvised around, edit scope honoured even when the fix is obvious, planted violations and negative controls, and a closing section of text for the owner. That house style is itself evidence about him — it is what he asked for and kept.
