# Ideas from cb-04 (2026-08-27 – 2026-08-29)

**Provenance warning, read this first.** This batch contains **no messages written by Ren**. All 38 entries in `/Users/ren/theories/_process/reading-notes/cb-04.md` are `<task-notification>` blocks — subagent completion reports that arrive in the user turn of a Claude Code transcript and were therefore mis-classified as "Ren's own messages" by the extraction pipeline. Of 360,570 characters, 357,710 sit inside those blocks; stripping them leaves only 38 date headers and nothing else. There are zero `· · ·` separators, because there are zero Ren messages to separate. **Nothing below is Ren's voice.** What the batch does contain, densely, is the interior of `deepseek-harness` during Phases 3–7 (multi-window desktop, notes application, durable personal plugins): doc-comments, README rules, invariants, naming laws and refusal texts from a codebase Ren directs. Those are quoted here with their provenance marked, because the design philosophy is real and traceable even though the wording is not his.

Provenance markers used throughout: **[repo-doc]** = a comment, README, spec or config sentence from Ren's repository, quoted verbatim inside an agent report; **[agent]** = a subagent's own prose describing a rule that governs the repo; **[repo-rule]** = a named gate or standing order (`AGENTS.md`, `docs/AGENTS.md`, `docs/testing.md`, `packages/CLAUDE.md`). Everything is in English unless marked zh.

---

## Ideas

### A. Ontology of the runtime — windows, sessions, existence

1. **A window's existence is the session's staging: the two are biconditional.** The runtime's own module doc states the equivalence rather than a mechanism.
   > "the window opens ⟺ the session is on stage (today the stage is `current`; the staged state can widen to a multi-pane list later)" [repo-doc, `session-runtime/src/client/service.ts:1-16`]
   2026-08-27T22:22 · "Map phase-3 verification surfaces" · `context-as-existence-runtimes`

2. **A session's live runtime exists exactly as long as someone is holding a viewing lease on it — refcounted existence, not a global selection.** Global "current session" is deleted and replaced by `acquireView`.
   > "one `viewHolds: Map<SessionId, number>` where *an entry exists ⟺ the session is STAGED*, and the value counts live holds. A **zero value is the release grace**." [agent]
   2026-08-28T00:21 · "P3-W3: session viewing leases" · `context-as-existence-runtimes`

3. **Ceasing to exist gets a grace period, so that a handover between viewers never tears the world down.** Release parks the count at zero and schedules a macrotask sweep; re-acquire inside the grace cancels it.
   > "This is what makes StrictMode acquire/release/acquire and A-closes-while-B-opens handoffs leave the scope untouched." [agent]
   2026-08-28T00:21 · "P3-W3: session viewing leases" · `context-as-existence-runtimes`

4. **A session that leaves the world while still being watched keeps its scope frozen until the last watcher lets go.**
   > "a session that leaves the list while staged keeps its scope frozen until its last lease releases" [agent]
   2026-08-28T00:21 · "P3-W3: session viewing leases" · `context-as-existence-runtimes`

5. **Writing the binding *is* the navigation — there is no separate act of "going somewhere".** State is written to the durable record; the mirror republishes; the frame re-renders. Navigation is a consequence of a fact changing, not a command.
   > "Writing the binding IS the navigation: the Host stores the launch state, the mirror republishes it, and this frame re-renders against the new `launchState`" [repo-doc, `ChatSurface.tsx:172-175`]
   2026-08-28T08:19 · "Map second-app + profile surfaces" · `context-as-existence-runtimes`

6. **A window is identified by what it shows, never by a hidden id — identity is content, and a test may not ask for a convenience handle.**
   > "the wrapper records the Surface, never the Session, and the doc at `:134-136` says adding an id attribute for a test's convenience is not on offer" [agent quoting repo-doc, `desktop-windows.ts`]
   2026-08-28T08:19 · "Map second-app + profile surfaces" · `context-as-existence-runtimes`

7. **Two windows on one surface were forbidden only because browser state was keyed by surface identity — a scoping accident, recorded as such and later lifted.**
   > "One Window per Surface while a Surface's browser state is keyed by Surface id alone: a second Window would draw the first one's state." [repo-doc, `desktop-domain/src/index.ts:222-230`]
   2026-08-27T22:22 · "Map windowing UX substrate" · `context-as-existence-runtimes`

8. **Per-instance state is a genuine axis of existence: the same registration renders many times, each with its own store.** `instanceKey: record.id` plus `pruneStoreInstance` retire a window's private world when the window closes.
   > "`instanceKey: record.id` on the window dispatch; `DesktopRoot` diffs the id set and prunes, gated on a `ready` view so a failed baseline never wipes live windows' state." [agent]
   2026-08-28T05:41 · "P3 fixer round 1" · `context-as-existence-runtimes`

9. **A mechanism that exists but that nothing invokes is a lie in the codebase, and gets called out as such.** The reviewer's blocker was not a bug but dead machinery.
   > "**D3 is dead code in production.** The whole per-window `instanceKey` pipeline exists … but no production dispatch site passes `instanceKey` and nothing calls `pruneStoreInstance`." [agent]
   2026-08-28T03:55 · "P3-W7: adversarial review" · `memories-and-working-style`

10. **Crash containment is scoped wrongly when identity is registration-wide but rendering is per-instance — and the rule is worth a recorded decision rather than a rushed patch.**
    > "One `register()` call backs the `chat` Surface, so any single Window's ChatSurface crash retires the registration for *all* Windows … the rule outlives its fix and deserves a recorded decision rather than a code change now." [agent]
    2026-08-28T05:48 · "P3-W7: adversarial review" · `keep-the-possibility-space-open`

11. **Narrowing the view is presentation only; the records must be byte-identical across the narrowing.** The world does not shrink because the window did.
    > "the records are byte-compared across the resize to show narrowing is presentation only, and widening restores both Windows" [agent]
    2026-08-28T03:39 · "P3-W6: e2e lanes + goldens" · `context-as-existence-runtimes`

12. **Hiding a window unmounts it and releases its lease, but the session keeps living — visibility and existence are decoupled.**
    > "`chrome.ts:127-136` unmounts it and releases the lease, but the Session stays list-eligible so its scope and stream survive." [agent]
    2026-08-28T05:48 · "P3-W7: adversarial review" · `context-as-existence-runtimes`

13. **Reconnection must merge, never clear — a transient loss of contact must not transiently unbind everything.**
    > "merges rather than clears and holds `listPhase` at `ready`, so `boundListed` never transiently drops" [agent]
    2026-08-28T05:48 · "P3-W7: adversarial review" · `context-as-existence-runtimes`

14. **A deleted thing is marked missing, never pruned — because something may still be watching that exact cell, and the same name may come back.**
    > "**Detail cells are marked `missing`, never pruned** — an open editor is subscribed to that exact store, and a Note recreated under the same id must be able to come back." [agent]
    2026-08-28T09:41 · "P4-N3: Notes application client" · `keep-the-possibility-space-open`

15. **Ordering after a death cannot be revision-based, because a deleted thing has no revision and a recreated one restarts at zero — so use a generation counter.**
    > "Install ordering is guarded by a per-cell generation counter rather than revision comparison, because a deleted Note has no revision and a recreated one restarts at 0." [agent]
    2026-08-28T09:41 · "P4-N3: Notes application client" · `shengsheng-buxi-generative-existence`

### B. Interfaces as commitments — the discipline of widening

16. **Widening an interface is not a code change but a constitutional act, and the doc says so at the interface itself.**
    > "widening this interface is the explicit act of widening what a browser package may do" [repo-doc, `desktop-runtime/contract/desktop.ts:41-46`]
    2026-08-27T22:22 · "Map windowing UX substrate" · `keep-the-possibility-space-open`

17. **The wire surface is enumerable and small; everything else is in-process.** Six `@Remote` methods, and the one remaining exposure is written down rather than hidden.
    > "the wire surface is exactly six `@Remote` methods … The remaining exposure — `resolve` serving any id to any caller — is already recorded at `packages/desktop/desktop/README.md:29`." [agent]
    2026-08-28T05:48 · "P3-W7: adversarial review" · `keep-the-possibility-space-open`

18. **The bundle that owns the shell owns exactly the shell.**
    > shell "owns the frame, the window records, and the overlay layer, nothing else" [repo-doc, `bundle/desktop-shell/cordis.patch.yml`]
    2026-08-27T22:22 · "Map windowing UX substrate" · `keep-the-possibility-space-open`

19. **A union member that nothing can ever produce is fiction, and is deleted rather than documented.**
    > "A code nothing can produce would be dead, so I dropped it from the union and stated the governing rule instead" [agent]
    2026-08-28T08:57 · "P4-N1: note seam host" · `memories-and-working-style`

20. **A parameter whose guard can only fire when a caller misuses it is dead and gets removed.**
    > "`configureSubagentView`'s first parameter is dead … the guard can only fire if a caller passes something other than `address.parentSessionId`" [agent]
    2026-08-28T05:48 · "P3-W7: adversarial review" · `memories-and-working-style`

21. **An optional arm with no expressible target is "uncovered fiction" — a memorable coinage for a common design failure.**
    > "the `| undefined` arm has no expressible target (there is no child id to clear) and no caller, so it would be uncovered fiction" [agent]
    2026-08-28T00:21 · "P3-W3: session viewing leases" · `memories-and-working-style`

22. **A nullable field that no state produces is refused: nullability must be earned by a reachable state.**
    > "**`lastMutationId` is `string`, never `null`** … every create carries a mutation id, so a nullable would be a state nothing produces" [agent]
    2026-08-28T08:57 · "P4-N1: note seam host" · `memories-and-working-style`

23. **Discriminated unions over optional fields, because an optional field forces readers into branches nothing can reach.**
    > "With `record?` every reader needs a narrowing check that nothing can make fail — unreachable branches that the 100% per-file gate cannot pass." [agent]
    2026-08-28T09:41 · "P4-N3: Notes application client" · `jian-and-wenyan-as-formal-language`

24. **Client-side outcome types alias the host's own unions so they cannot drift, and the one arm added is epistemically honest.**
    > "a carrier failure reached *no* Host verdict, so the caller says 'not saved' rather than naming a refusal the Host never made" [agent]
    2026-08-28T09:41 · "P4-N3: Notes application client" · `jian-and-wenyan-as-formal-language`

25. **Explicit over implicit, with no hidden default filled in behind the caller's back.**
    > "`DynamicCordisRunnerEnv` gained a **required** field (explicit-over-implicit; no hidden `?? 'dyn'`)" [agent]
    2026-08-28T14:32 · "Export draft-runtime execution seam" · `jian-and-wenyan-as-formal-language`

26. **A no-op change is not a change, and is refused at parse.**
    > "`updateWindow` with an empty `set` is refused at parse (a revision that changed nothing is not a change)." [agent]
    2026-08-27T23:08 · "P3-W2: desktop host geometry+focus" · `jian-and-wenyan-as-formal-language`

### C. The no-silent-loss principle

27. **Never re-derive the caller's expected revision at send time — re-reading it *is* the silent overwrite the conflict rule exists to prevent.** Named "the crux".
    > "**`expectedRevision` is the caller's and is never re-derived at send time.** This is the crux: re-reading the held revision when the write leaves *is* the silent overwrite the no-retry rule exists to prevent." [agent]
    2026-08-28T09:41 · "P4-N3: Notes application client" · `keep-the-possibility-space-open`

28. **Treating a conflict like a commit is the archetypal silent loss: the mutation is dropped and nobody hears.**
    > "**Concurrent Window mutations are silently discarded.** … treats `conflict` exactly like `committed` — installs the snapshot, no retry, no warning. Callers … are fire-and-forget, so the loss is invisible." [agent]
    2026-08-28T03:39 · "P3-W6: e2e lanes + goldens" · `keep-the-possibility-space-open`

29. **Latch on success, never on attempt — a latch on attempt makes one transient failure permanent and silent.**
    > "*Remedy:* latch on success, not on attempt; log where the rejection is swallowed." [agent]
    2026-08-28T05:48 · "P3-W7: adversarial review" · `keep-the-possibility-space-open`

30. **A conflict banner must disable plain Save, or Save carries the stale draft onto the very revision the banner warns about.**
    > "While it stands, plain Save is disabled — otherwise Save would carry the draft onto the very revision the banner warns about." [agent]
    2026-08-28T09:41 · "P4-N3: Notes application client" · `keep-the-possibility-space-open`

31. **Drafts are tagged with their subject, so a window changing subject can never leak one draft onto another.**
    > "The per-Window draft is tagged with its Note (`subject`), so a Window switching notes can never leak one draft onto another." [agent]
    2026-08-28T09:41 · "P4-N3: Notes application client" · `keep-the-possibility-space-open`

32. **A limit that fails silently is a dead end; refusals must reach the person through the layer that already carries notices.**
    > "**The Window limit fails silently.** … At the cap, 'Open in new window', modifier-click, and the taskbar launcher all do nothing with no feedback." [agent]
    2026-08-28T05:48 · "P3-W7: adversarial review" · `keep-the-possibility-space-open`

33. **Collapsing a refusal into `undefined` is a design failure: the person presses a button and nothing explains itself.**
    > "Collapsing `note-limit` into `undefined` means pressing New note does nothing with no explanation; the list pane now shows the Host's own message." [agent]
    2026-08-28T09:41 · "P4-N3: Notes application client" · `keep-the-possibility-space-open`

34. **A listener fan-out must contain each listener, or one throwing subscriber starves the rest.**
    > "There is now one listener per mounted Chat Window, and `provide()` runs during plugin apply, so a throwing subscriber starves the rest and propagates into a registering plugin. *Remedy:* restore per-listener containment." [agent]
    2026-08-28T05:48 · "P3-W7: adversarial review" · `keep-the-possibility-space-open`

35. **A publish that fails must never fail the mutation — publication is contained by construction.**
    > "`publish` … and `publishSurfaceChange` … (both `try/catch` → `logger.warn`, so a throwing listener cannot fail the mutation)" [agent]
    2026-08-28T08:19 · "Map second-app + profile surfaces" · `keep-the-possibility-space-open`

36. **Fail loud where the failure is real; fall back only where the contract says fallback.** The two are separated deliberately at the same seam.
    > "session-maybe outside a boundary fails loud (F2) while strict slots still fall back (spec D2, which root chrome depends on)" [agent]
    2026-08-28T05:41 · "P3 fixer round 1" · `keep-the-possibility-space-open`

37. **Deletion is the one operation that cannot be made idempotent by replay, and the reason is stated rather than papered over.**
    > "Any record still present whose `lastMutationId` matches is one this delete did *not* remove; answering `committed` for it would announce a deletion that never happened" [agent]
    2026-08-28T08:57 · "P4-N1: note seam host" · `jian-and-wenyan-as-formal-language`

38. **A prototype-named key must round-trip as data — `z.record` silently drops `__proto__`, so the schema is hand-built over a null-prototype container.**
    > "zod's `z.record` silently **drops** `__proto__`" ; test: "replays a key named after a prototype member as the data it is" [agent]
    2026-08-28T19:40 · "Fix registry review findings" · `keep-the-possibility-space-open`

### D. Durability, records and commit points

39. **One record, one put, is the commit point — because the domain form offers no cross-table transaction.**
    > "the domain form has no cross-table transaction, so one record + one `put` is the commit point" [repo-doc, `desktop-domain/src/spec.ts:12-15`]
    2026-08-28T08:19 · "Map second-app + profile surfaces" · `context-as-existence-runtimes`

40. **A schema version stamped differently rejects the whole medium at open — versioning is a hard gate, not a migration hint.**
    > "a medium stamped with a different version rejects at open." [repo-doc, `DomainSpec.version` JSDoc]
    2026-08-28T08:19 · "Map second-app + profile surfaces" · `jian-and-wenyan-as-formal-language`

41. **Old records must stay valid: a required field would fail the whole domain open for every record written before it existed.**
    > "Domain records are zod-parsed at load, so a required field would fail the whole domain open for any phase-2 record — D4 forbids a version bump and wants old records valid." [agent]
    2026-08-27T23:08 · "P3-W2: desktop host geometry+focus" · `context-as-existence-runtimes`

42. **Every write rides one per-key queue — mutations, the creating put, and the stamping alike.**
    > "*every* write — mutations, the creating put, and the `lastOpenedAt` stamp — rides the same queue" [repo-doc, `desktop-domain/src/index.ts:151-156`]
    2026-08-28T08:19 · "Map second-app + profile surfaces" · `context-as-existence-runtimes`

43. **Ordering ties must be broken by identity, because sort stability does not survive a restart.**
    > "Sort stability alone does not survive a restart, since the tie order would then be the medium's serialization order." [agent]
    2026-08-28T08:57 · "P4-N1: note seam host" · `context-as-existence-runtimes`

44. **Fixed contract bounds refuse at validation; deployment bounds refuse as result values.** Two kinds of "no", kept apart.
    > "fixed contract bounds (title ≤512, an update naming no field) are refused at validation; deployment bounds (`maxNotes`, `maxBodyBytes`) are refused as result values" [agent]
    2026-08-28T08:57 · "P4-N1: note seam host" · `jian-and-wenyan-as-formal-language`

45. **Request-validity is checked before deployment bounds — identity, then size, then retention.**
    > "Create checks in the order: identity → body size → retention bound" [agent]
    2026-08-28T08:57 · "P4-N1: note seam host" · `jian-and-wenyan-as-formal-language`

46. **A publish-at-commit invariant lives on the *definition* package so it binds every provider, not on any one implementation.**
    > "It lives on the **Definition** package so it covers every provider; `desktop-domain/src/invariant.ts` is the justified empty one that points at it." [agent]
    2026-08-28T08:19 · "Map second-app + profile surfaces" · `keep-the-possibility-space-open`

47. **Notify-then-pull: an event carries only an identity and a revision; the reader pulls.** A burst during an in-flight resolve is served by exactly one follow-up read.
    > "the retained-snapshot slot is deleted outright; the 'pending need' is the existing `needsRefresh` flag, so a burst of announcements during an in-flight resolve is served by exactly one follow-up read" [agent]
    2026-08-27T23:08 · "P3-W2: desktop host geometry+focus" · `context-as-existence-runtimes`

48. **The record *is* the wire value — so a field added to the record lands on the wire for free.**
    > "deliberately record = wire value" [agent, on `DesktopSnapshot`]
    2026-08-29T08:58 · "Review plan: codebase grounding" · `spirit-space-token-and-yi-substrate`

49. **Identity is content-addressed: a package is the digest of exactly the bytes that were written.**
    > "the `sha256:` package digest is deliberately left literal because it is the content address of exactly the bytes the script wrote." [agent]
    2026-08-28T18:19 · "Build Phase 7 test lanes" · `spirit-space-token-and-yi-substrate`

50. **Canonical serialization by construction, so that a schema field cannot silently drop out of identity.**
    > "This makes 'recursively sorted keys, no whitespace' exact and branch-free, and a field added to a schema cannot silently drop out of the digest." [agent]
    2026-08-28T14:38 · "Build plugin-package-store package" · `spirit-space-token-and-yi-substrate`

51. **Identity is minted when the request is *armed*, not at commit — so the thing runs under the name it will eventually be committed under.**
    > "The registry mints the id when it *arms* a request — even for a first install — so a candidate mounts under the id it will commit under and the post-commit reconcile is a no-op" [agent]
    2026-08-28T16:21 · "Build personal-client-runner package" · `spirit-space-token-and-yi-substrate`

52. **Id minting must survive collision by asking the caller, not by trusting randomness.**
    > "`mintRunId`/`mintPromotionRequestId`/`mintPersonalPluginId` … take an `IdTaken` predicate and loop via `untilFree`" [agent]
    2026-08-28T19:40 · "Fix registry review findings" · `spirit-space-token-and-yi-substrate`

### E. Model-facing context as a first-class, documented resource

53. **Every package must declare, in its README, what the model sees, its token effect, and its KV-cache effect — a gate enforces the exact three headings.** This makes the model's context a governed budget of the whole system, not an afterthought.
    > required structure: "`## Model Experience`, then one H3 per model-context entry, each with the three ordered H4s `#### What the model sees`, `#### Token effect`, `#### KV Cache effect`" [repo-rule, `scripts/verify-package-readme-model-experience.ts`]
    2026-08-28T08:22 · "Map tool-authoring surfaces" · `alignment-selection-on-cognition`

54. **A package with no model-facing contribution must say so explicitly, in a fixed sentence.**
    > "None, as the bundle composes …; nothing it inserts registers a tool, a prompt section, or any other model-visible contribution." and "None; this package neither assembles nor sends a provider request." [repo-doc, bundle README template]
    2026-08-28T08:19 · "Map second-app + profile surfaces" · `alignment-selection-on-cognition`

55. **Cache-prefix stability is reasoned about explicitly as a property of appended content.**
    > "Append-only; newly visible content follows the reusable request prefix and does not invalidate existing KV-cache entries." [repo-doc, `tool-automation/README.md`]
    2026-08-28T08:22 · "Map tool-authoring surfaces" · `alignment-selection-on-cognition`

56. **A listing bound is justified in prose by what the model can actually act on within one turn's context.**
    > "Twenty rules fit a listing the model can act on without spending a turn's context on inventory" [repo-doc, `tool-automation/src/index.ts` Config JSDoc]
    2026-08-28T08:22 · "Map tool-authoring surfaces" · `alignment-selection-on-cognition`

57. **A caller must not be able to widen a listing past its configured cap — the bound is applied to the emitted array, not delegated to the service.**
    > "a registry that ignores `limit` cannot widen a listing past its configured cap" [repo-doc, `tool-automation/src/index.ts:495,501`]
    2026-08-28T08:22 · "Map tool-authoring surfaces" · `alignment-selection-on-cognition`

58. **Truncation must leave a character whole or absent — bounds are measured at their exact encoded cost.**
    > "Truncation walks code points at their exact JSON-encoded cost, so a character is whole or absent." [agent]
    2026-08-28T16:01 · "Build tool-plugin-development package" · `jian-and-wenyan-as-formal-language`

59. **Timestamps were removed from rendered model-facing listings because they made every transcript differ and moved the request prefix for no action.** Context churn is treated as a cost.
    > "Rendered listings carried raw epoch-ms stamps, making every transcript differ per run (and moving the request prefix for no action)." [agent]
    2026-08-28T09:34 · "P4-N2: tools + snapshots" · `alignment-selection-on-cognition`

60. **The prompt text a model reads cannot drift from the validator, because the description interpolates the validator's own pattern.**
    > "`CREATE_DESCRIPTION` interpolates `AUTOMATION_EVENT_NAME_PATTERN.source` … so the prompt cannot drift from the validator" [agent]
    2026-08-28T08:22 · "Map tool-authoring surfaces" · `alignment-selection-on-cognition`

61. **Model-visible description text is pinned verbatim by tests — the prompt is a contract, not copy.**
    > "model-visible description text pinned verbatim (`:213-218`)" [agent]
    2026-08-28T08:22 · "Map tool-authoring surfaces" · `alignment-selection-on-cognition`

62. **A refusal should teach the model what to do instead, naming the legal alternatives.**
    > "desktop.window.surface only accepts a Surface this Plugin declared, and \"wallet\" is not one of them. Register under one of: \"clock\", \"timer\"." and "This Plugin declared no Surface, so it has no window to render into." [repo-doc, guard teaching text]
    2026-08-28T14:32 · "Export draft-runtime execution seam" · `alignment-selection-on-cognition`

63. **Presenters must be pure, because they run both on live streaming and on session-log replay.** The rendered past must be reconstructible from the log alone.
    > "**purity** (presenters run on live streaming *and* session-log replay — no I/O, no session state, no clock/random)" [repo-doc, `docs/cookbook/adding-a-tool.md:86-88`]
    2026-08-28T08:22 · "Map tool-authoring surfaces" · `context-as-existence-runtimes`

64. **Malformed older logged arguments degrade to a generic card rather than crashing replay — the past must stay readable as the schema moves.**
    > "`defineTool` soft-validates the display path so malformed older logged args return `undefined` (generic fallback) instead of crashing replay" [agent]
    2026-08-28T08:22 · "Map tool-authoring surfaces" · `context-as-existence-runtimes`

65. **The model result and the UI formatting are separate concerns; UI-only formatting stays out of what the model reads.**
    > "**UI-only formatting stays out of the model result**" [repo-doc, `docs/cookbook/adding-a-tool.md`]
    2026-08-28T08:22 · "Map tool-authoring surfaces" · `alignment-selection-on-cognition`

66. **Bounded output has three named layers, and a new tool must pick from them consciously.** Config caps on the emitted array; byte trimming in `finalizeContent`; a spill store with a follow-up-readable locator.
    > "Apply bounds to the complete result… test tiny and exact limits, oversized single chunks, and multibyte byte limits." [repo-rule, `packages/CLAUDE.md`]
    2026-08-28T08:22 · "Map tool-authoring surfaces" · `alignment-selection-on-cognition`

### F. Naming discipline and formal vocabulary

67. **Tool names are `<singular_subsystem>_<verb>`, and plural prefixes are never used** — even where the package and the service are plural (`tool-jobs`, `ctx.jobs`, but `job_kill`).
    > "**Plural prefixes are never used.**" [agent, inventorying `docs/tool-catalog.md:18-44`]
    2026-08-28T08:22 · "Map tool-authoring surfaces" · `jian-and-wenyan-as-formal-language`

68. **Two case regimes coexist deliberately: model-facing top-level parameters are `snake_case`, nested objects mirroring a durable record keep the record's `camelCase`** — so a rejection quotes the exact path the model supplied.
    > "mirrors the `AutomationRuleInput` record field-for-field (camelCase), so a zod rejection quotes the exact parameter path the model supplied." [repo-doc, `tool-automation/README.md:9`]
    2026-08-28T08:22 · "Map tool-authoring surfaces" · `jian-and-wenyan-as-formal-language`

69. **Multi-action modelling has two shapes, chosen by whether the actions share a subject and an argument shape**: one tool with an action enum, or many tools; plus a hybrid with a boolean discriminator and a `oneOf` output.
    > "*Single tool + action enum*: `lsp` with `operation: enum[…]` over one identical `(file_path, line, character)` cursor … *Many tools*: `terminal_*` (six, distinct arguments and lifecycles)" [agent]
    2026-08-28T08:22 · "Map tool-authoring surfaces" · `jian-and-wenyan-as-formal-language`

70. **A vocabulary has exactly one home; enums are sourced from the record schema rather than restated.**
    > "the outcome vocabulary has one home" [repo-doc, `tool-automation/src/index.ts:91`]
    2026-08-28T08:22 · "Map tool-authoring surfaces" · `jian-and-wenyan-as-formal-language`

71. **Descriptions are module constants, never inline literals** — text that the model reads is a named thing.
    > "**Descriptions** are module constants, not inline: `:98-113 CREATE_DESCRIPTION`, `:115-122 LIST_DESCRIPTION`, `:124-129 SET_ENABLED_DESCRIPTION`." [agent]
    2026-08-28T08:22 · "Map tool-authoring surfaces" · `jian-and-wenyan-as-formal-language`

72. **A verb is reserved: "mint" is the id-creation verb of this vocabulary, and using it for anything else is flagged as a term collision.**
    > "'mint' is this note's id-creation verb — 'page-minted Desktops', the Window-id mint" [agent, prose review]
    2026-08-29T08:59 · "Review plan: scope and prose" · `jian-and-wenyan-as-formal-language`

73. **One exact term per subject; a nominalized word that competes with an existing one is a defect.** "Plane" overloaded against "control plane" is rejected, and "installation target" is prescribed instead.
    > "prose standard — one exact term per subject; 'application plane' reads as a deployment tier beside the control plane, which it is not." [agent, prose review]
    2026-08-29T08:59 · "Review plan: scope and prose" · `jian-and-wenyan-as-formal-language`

74. **Metaphors are banned in the repo's prose, and the ban names the specific metaphors to avoid.**
    > root `AGENTS.md`: "Do not use metaphors"; `docs/AGENTS.md`: "Name the exact check… instead of metaphorical 'gate', 'vocabulary', or 'surface'" [repo-rule]
    2026-08-29T08:59 · "Review plan: scope and prose" · `jian-and-wenyan-as-formal-language`

75. **A lowercase generic use of a word that is elsewhere a branded object is a defect, and the fix names the mechanism.**
    > "'no surface added by this phase accepts a caller-supplied identity' — lowercase generic 'surface' in a note where `Surface` is a branded object … Replace: 'and no Remote method or tool added by this phase accepts a caller-supplied user identity.'" [agent]
    2026-08-29T08:59 · "Review plan: scope and prose" · `jian-and-wenyan-as-formal-language`

76. **Registration keys must be literals because the catalog generator reads registration text from source and resolves no constants** — a case where the formal language of the system forbids abstraction at one exact site, and the comment says why.
    > "child-slot keys **must be literals**, the client-catalog generator resolves no constants" [repo-doc, `ui-desktop/src/client/index.ts:114-115`]
    2026-08-27T22:22 · "Map windowing UX substrate" · `jian-and-wenyan-as-formal-language`

77. **Constants shared across compiler aggregates are mirrored, never imported — and each mirror names its source.**
    > "the file's own rule (`:5-8`) is that constants are **mirrored, never imported**, because these specs live in the Host compiler aggregate" [repo-doc, `apps/web/tests/desktop-windows.ts`]
    2026-08-28T08:19 · "Map second-app + profile surfaces" · `jian-and-wenyan-as-formal-language`

78. **Brand factories may not live in a types-only module — a repo rule that agents are told to follow even against local precedent.**
    > "`note/types.ts` and `desktop/types.ts` put factories in `types.ts`, which `packages/AGENTS.md` forbids; the instruction was explicit, so I did not copy them." [agent]
    2026-08-28T14:38 · "Build plugin-package-store package" · `jian-and-wenyan-as-formal-language`

79. **A boundary type must be exported from a public non-root subpath — the generator refuses a root import.**
    > "`PluginPackageId must be exported from a public non-root type subpath`" [repo-doc, Typert generator refusal]
    2026-08-28T15:33 · "Build plugin-registry core package" · `jian-and-wenyan-as-formal-language`

80. **A description of a version field states the condition for raising it, not what it is.**
    > "`launch_schema_version` description → 'Raise it whenever the layout of that state changes'" [agent]
    2026-08-28T19:24 · "Fix periphery review findings" · `jian-and-wenyan-as-formal-language`

### G. Bilingual discipline — zh/en as one document

81. **Every doc exists as a pair with a recorded blob-hash sidecar; a gate counts them and demands consistency.** The corpus reaches 1,051 pairs.
    > "`verify-translation-pairing`: `1051 pair(s) checked across all in-scope documentation, all consistent.`" [agent]
    2026-08-28T19:40 · "Fix registry review findings" · `jian-and-wenyan-as-formal-language`

82. **"Pairs update together" is a standing order, and a one-sided amendment is a red gate, not a to-do.**
    > `docs/AGENTS.md` — "Pairs update together"; "until translated the pair is two contradictory plans" [repo-rule + agent]
    2026-08-29T08:59 · "Review plan: scope and prose" · `jian-and-wenyan-as-formal-language`

83. **Some technical terms are translated and some deliberately are not — a mixed kernel.** (zh)
    > "hand-translated style-matched to the Phase 2 note (seam stays `seam`, 组合包, 座位, 租约, 视口, 任务栏, 启动器)" [agent] — zh: 组合包 (bundle), 座位 (seat), 租约 (lease), 视口 (viewport), 任务栏 (taskbar), 启动器 (launcher)
    2026-08-28T08:02 · "P3-W8: docs + bilingual close" · `jian-and-wenyan-as-formal-language`

84. **Window chrome is named 窗饰 in Chinese** — an invented compound for a concept English calls "chrome". (zh)
    > "the whole new **Window 窗饰** section: title bar, taskbar, launcher, narrow viewport, completion notices, `document.title`" [agent]
    2026-08-28T08:02 · "P3-W8: docs + bilingual close" · `jian-and-wenyan-as-formal-language`

85. **Terminology conflicts are resolved by family coherence over global frequency — and the choice is surfaced for the owner to overrule.** (zh)
    > "I used 契约 for 'contract' … `docs/i18n/terminology.md` prescribes 约定 (which dominates repo-wide 73:13), but the phase-3 desktop family … is uniformly 契约 … say the word and I will switch the family to 约定." [agent]
    2026-08-28T12:45 · "P4-N6: docs + bilingual close" · `jian-and-wenyan-as-formal-language`

86. **Cross-locale anchors must be byte-identical, so a Chinese heading carries an explicit English anchor id.** (zh/en)
    > "**Cross-locale anchors must be byte-identical.** … the repo's mechanism … is an explicit `<a id>` on the Chinese page, so `desktop.zh.md` now carries `<a id=\"surfaces-and-the-window-slot\">`." [agent]
    2026-08-28T12:45 · "P4-N6: docs + bilingual close" · `jian-and-wenyan-as-formal-language`

87. **Chinese word order reversing a link sequence is fixed by reordering the sentence, not by relinking.**
    > "Two other failures were Chinese word order reversing link sequence — reordered rather than relinked." [agent]
    2026-08-28T12:45 · "P4-N6: docs + bilingual close" · `jian-and-wenyan-as-formal-language`

88. **A README shipping without a language switcher is a latent defect that the pairing gate would only catch later — so it is caught by reading.**
    > "**Six English READMEs shipped without a language switcher** … the pairing gate would have rejected them the moment a counterpart existed." [agent]
    2026-08-28T12:45 · "P4-N6: docs + bilingual close" · `jian-and-wenyan-as-formal-language`

### H. Documents as governed artifacts

89. **Documents carry word budgets with frozen ceilings; when a doc is above target, you condense rather than raise the ceiling.**
    > "`packages/README.md` is at exactly 994/994 words. Its ceiling is *frozen* (docs/AGENTS.md: above the 600-word target, no raise), so I condensed instead of raising" [agent]
    2026-08-28T12:45 · "P4-N6: docs + bilingual close" · `human-solutions-museum`

90. **A fact belongs in exactly one document; a restatement is replaced by a link to its owner.**
    > "replaced a 26-word restatement of package-README requirements with a one-line link, since packages/AGENTS.md:26-27 already owns that fact" [agent]
    2026-08-28T12:45 · "P4-N6: docs + bilingual close" · `human-solutions-museum`

91. **Links must be machine-checkable, never free prose naming a thing.**
    > `docs/AGENTS.md` — "machine-checkable links, never free prose" [repo-rule]
    2026-08-29T08:59 · "Review plan: scope and prose" · `jian-and-wenyan-as-formal-language`

92. **Docs describe the current state, never narrate the change** — "it is now X rather than Y" is rewritten to "it is X".
    > "rewrote the three change-narration sentences (studio README ×2, ui-cordis 'it is now … rather than a popover', plus the two 'no longer' clauses …) to current state" [agent]
    2026-08-28T19:24 · "Fix periphery review findings" · `human-solutions-museum`

93. **A factually wrong paragraph about a rule the code has lifted is an obligation to fix, not a nicety** — because docs accompany code.
    > "a factually wrong English paragraph about a rule this phase lifted, which the docs-accompany-code rule makes an obligation, not a nicety" [agent]
    2026-08-28T05:48 · "P3-W7: adversarial review" · `human-solutions-museum`

94. **Documented behavior that is not yet true is called "aspirational" and fixed in the code so the doc becomes true.**
    > "The documented behavior … is now true rather than aspirational." [agent]
    2026-08-28T19:24 · "Fix periphery review findings" · `human-solutions-museum`

95. **An architecture table maps generic mechanisms, not applications — a `ctx.notes` row is refused on that ground alone.**
    > "The extension table maps generic *mechanisms*; 'Add a launchable desktop Surface' already covers how a second application attaches, and a `ctx.notes` row would put one application into a mechanism table." [agent]
    2026-08-28T12:45 · "P4-N6: docs + bilingual close" · `human-solutions-museum`

96. **Decisions are recorded as "Agent Notes" with a fixed anatomy — Problem, Decision, Alternatives considered, Consequences — and land in `proposed/` then `implemented/`, with an `Implemented by …` exit line back into the plan.**
    > sections: "`## Problem`, `## Decision` (9 bold-led paragraphs …), `## Alternatives considered` (6, all from the spec/wave record), `## Consequences`" [agent]
    2026-08-28T18:26 · "Docs, catalogs, and Agent Note" · `human-solutions-museum`

97. **Stale alternatives in living notes are a named hazard with a dedicated remedy skill; leaving settled decisions contradicted for a whole phase is a defect.**
    > "two active proposed notes carry alternatives the user has already settled against — the exact condition `dsh-archive-agent-notes` exists to prevent" [agent]
    2026-08-29T08:59 · "Review plan: scope and prose" · `human-solutions-museum`

98. **Every non-trivial model-, protocol- or human-visible change carries its keyless scenario in the same PR, and a plan must name every coverage tier at plan time.**
    > `docs/testing.md`: "Every non-trivial model-, protocol-, or human-visible change adds or updates a keyless scenario in the same PR" and "New capability seams … name every coverage tier at plan time." [repo-rule]
    2026-08-29T08:59 · "Review plan: scope and prose" · `memories-and-working-style`

99. **PR history is chosen deliberately; independent changes are split.**
    > "Choose PR history deliberately. Split independent changes." [repo-rule, quoted by reviewer]
    2026-08-29T08:59 · "Review plan: scope and prose" · `memories-and-working-style`

### I. Composition, planes and where a thing belongs

100. **A later layer disables a row rather than dropping the bundle, and a patch replaces the whole config so each row states every key it owns.**
     > "A surface that composes its agent per session (the Web bundles) **disables these rows from a later layer rather than dropping this bundle**… A patch replaces the targeted row's whole `config`, so each row states every key it owns." [repo-doc, `bundle/agent-standard/cordis.patch.yml:1-13`]
     2026-08-28T08:22 · "Map tool-authoring surfaces" · `context-as-existence-runtimes`

101. **A service row in an agent preset must sit inside an isolate realm, or it publishes into the process-global root and is refused at mount.**
     > "*'A service row here MUST sit inside a group carrying an `isolate` realm'* — otherwise it publishes into the process-global root realm and `dsh-agent-presets` rejects it at mount." [repo-doc, `agent-presets/standard/agent.cordis.yml:1-19`]
     2026-08-28T08:22 · "Map tool-authoring surfaces" · `keep-the-possibility-space-open`

102. **A tool row never names its backing service; it declares `inject` and resolves whatever its scope sees.** Placement — host plane vs. preset — follows from who else must read the service.
     > "it does not, by name. It declares `inject` and resolves whatever `ctx.<key>` its scope sees." [agent]
     2026-08-28T08:22 · "Map tool-authoring surfaces" · `context-as-existence-runtimes`

103. **One row, one plane: a row active in the host composition may not also be a preset row.**
     > "verify-cordis-config's one-row-one-plane rule rejected it the moment the bundle ships the toolset host-plane: `row \"tool-cordis\" is also active in the host composition`" [agent]
     2026-08-28T17:52 · "Wire personal-plugin-runtime bundle" · `keep-the-possibility-space-open`

104. **Bundle rows are ordered host-first, then client** — a stated composition grammar.
     > "Row order (host first, then client)" [agent]
     2026-08-28T17:52 · "Wire personal-plugin-runtime bundle" · `context-as-existence-runtimes`

105. **The set of "seven bundles" is enumerated in ten independent places, and adding an eighth is a survey problem, not an edit.** The batch documents both the enumeration and the migration table that rewrites old installation-owned tuples to the new template.
     > "**The seven-bundle lists (all of them — I found three you did not name)**" [agent]
     2026-08-28T08:19 · "Map second-app + profile surfaces" · `human-solutions-museum`

106. **A capability that exists in only one plane must announce itself: authoring is mode-work, the OS side is host-plane.**
     > "header rewritten to state the OS-side/authoring split" [agent]
     2026-08-29T08:17 · "Scope plugin authoring to cordis mode" · `the-fork-and-cooperative-infrastructure`

107. **A capability withheld from a mode is replaced by a redirect that tells the model, in one pinned sentence, what the person must do.**
     > "Building or changing a personal plugin needs the Plugins mode, which this session is not in: if the user asks you to build or change one, tell them to switch this session's mode to Plugins." [repo-doc, pinned verbatim in three test files]
     2026-08-29T08:17 · "Scope plugin authoring to cordis mode" · `alignment-selection-on-cognition`

108. **Suppression is achieved by shadowing: a scoped section registered under the same name and order shadows the global one — no duplication.**
     > "it registers under the *same* section name `tool:plugin-development` at order 116 as the full toolset, and a scoped section shadows a global one of the same name" [agent]
     2026-08-29T08:17 · "Scope plugin authoring to cordis mode" · `context-as-existence-runtimes`

109. **A new surface appears in the launcher purely by registering with the host — there is no client-side list.**
     > "So a Host `registerSurface` call is all it takes for a new entry to appear in the launcher — no client-side list." [agent]
     2026-08-28T08:19 · "Map second-app + profile surfaces" · `keep-the-possibility-space-open`

110. **A configuration whose intended target does not yet exist must fail loud rather than fall back to a default.**
     > "a stored Desktop bound to a preset id the current config no longer declares must refuse resolve loudly rather than fall back" [agent, plan review]
     2026-08-29T08:58 · "Review plan: codebase grounding" · `keep-the-possibility-space-open`

111. **An enforcement claimed as "one host check" is falsified by a second creation path that bypasses it — a review finding about the difference between a rule and its coverage.**
     > "**(Contradiction) 'Enforcement is one host check: launch resolution' — but Desktop creation seeds a Window through a second path that bypasses it.**" [agent]
     2026-08-29T08:58 · "Review plan: codebase grounding" · `meta-attractor`

112. **A widening that happens silently is the named failure mode the acceptance criterion exists to forbid.**
     > "exactly the 'silently widening' the new acceptance bullet forbids" [agent]
     2026-08-29T08:58 · "Review plan: codebase grounding" · `keep-the-possibility-space-open`

### J. Human authority over what runs

113. **Enable, disable and uninstall are the user's — stated in the system prompt the model reads.**
     > "draft → promote → approval → survives restarts; revise via `target_plugin_id`; rollback; `harness.storage` + schema-version rule; a rejection is not re-requested; enable/disable/uninstall are the user's" [repo-doc, `PLUGIN_DEVELOPMENT_SYSTEM_PROMPT`]
     2026-08-28T16:01 · "Build tool-plugin-development package" · `the-fork-and-cooperative-infrastructure`

114. **A rejection is not re-requested** — a norm written into the agent's prompt, forbidding the retry-until-yes pattern.
     > "a rejection is not re-requested" [repo-doc, same prompt]
     2026-08-28T16:01 · "Build tool-plugin-development package" · `alignment-selection-on-cognition`

115. **Approval is per-promotion, contrasted with the draft's two-button standing grant** — a deliberate distinction between one-off consent and a standing grant.
     > "per-promotion approval vs. the draft's two-button standing grant" [repo-doc, Agent Note decision heading]
     2026-08-28T18:26 · "Docs, catalogs, and Agent Note" · `the-fork-and-cooperative-infrastructure`

116. **The approving page proves the client half** — human approval is not a rubber stamp; the act of approving is what demonstrates the code actually runs.
     > "the approving page proves the client half" [repo-doc, Agent Note decision heading]
     2026-08-28T18:26 · "Docs, catalogs, and Agent Note" · `the-fork-and-cooperative-infrastructure`

117. **A candidate may read but may not write until the person approves it.**
     > "`assertWritable` refuses `set`/`delete` for an unadopted run with a message naming the approval state; reads stay open." [agent]
     2026-08-28T19:40 · "Fix registry review findings" · `the-fork-and-cooperative-infrastructure`

118. **A plugin disabled during an approval must not be adopted by the commit** — a plugin the person switched off must not come up live.
     > "commitPromotion never re-reads or honors record.enabled … leaves a disabled plugin with a live run, registered Surfaces, and answering handlers." [agent, adversarial review]
     2026-08-28T18:54 · "Adversarial multi-agent review of the Phase 7 durable personal plugins working tree" · `the-fork-and-cooperative-infrastructure`

119. **A delete-confirm uses a plain modal, not the heavy risk confirmation** — proportionality of friction is a design decision with a stated reason.
     > "delete confirm via `Modal` (not `RiskConfirmation`, which demands an acknowledgement checkbox — over-heavy for deleting your own note)" [agent]
     2026-08-28T09:41 · "P4-N3: Notes application client" · `human-solutions-museum`

120. **Uninstalling must settle the pending promotions of the thing it removes, and only those.**
     > "`uninstall` now calls `dropPromotionsOf(pluginId)` first: disposes candidates, disarms, publishes `settled`, and steers the requesting Agent" [agent]
     2026-08-28T19:40 · "Fix registry review findings" · `the-fork-and-cooperative-infrastructure`

121. **Activation is bounded by a configured timeout so an unresponsive half cannot hang boot, approval, rollback or enable.**
     > "New validated config `activationTimeoutMs` … drives one shared helper `boundActivation` … so boot, approval, rollback, and enable are all bounded." [agent]
     2026-08-28T19:40 · "Fix registry review findings" · `keep-the-possibility-space-open`

122. **A concurrent gesture on the same subject must not be declared settled by another gesture's failure.**
     > "a concurrent gesture on the same subject must not be declared settled" [agent]
     2026-08-28T19:24 · "Fix periphery review findings" · `keep-the-possibility-space-open`

123. **A community-plugin taxonomy fixes what installs where: agent capabilities go to the runtime plane or a preset; application contributions target their Application.**
     > "agent capabilities — tools, providers, agent behavior — target `runtime` or a preset" ; "application contributions target their Application" [repo-doc + reviewer's prescribed fix]
     2026-08-29T08:59 · "Review plan: scope and prose" · `the-fork-and-cooperative-infrastructure`

124. **Sharing a desktop shares everything its applications expose — an allowlist reads as privacy but is not resource narrowing.** The reviewer insists this be stated with the actor and the error named.
     > "An owner can mistake an Application allowlist for resource narrowing: sharing a Desktop shares every list its Applications expose…" [agent, prescribed replacement]
     2026-08-29T08:59 · "Review plan: scope and prose" · `relational-self-and-datong`

125. **No method or tool added by a pre-auth phase may accept a caller-supplied user identity** — identity is not a parameter until there is an authenticated control plane.
     > "and no Remote method or tool added by this phase accepts a caller-supplied user identity." [agent, prescribed exit criterion]
     2026-08-29T08:59 · "Review plan: scope and prose" · `the-fork-and-cooperative-infrastructure`

### K. Testing as evidence, not ceremony

126. **The fixture pins only what the model said; the tools execute for real.** A replay is not a mock of the world.
     > "the fixture pins only what the MODEL said; the tools execute for real" [repo-doc, `cordis-tool-round.e2e.ts:1-10`]
     2026-08-28T08:22 · "Map tool-authoring surfaces" · `context-as-existence-runtimes`

127. **A side effect is proved by probing the world, not by trusting the transcript.**
     > "the DOM probe `[data-snapshot-probe]` is asserted absent before and present after … proving the side effect really happened" [agent]
     2026-08-28T08:22 · "Map tool-authoring surfaces" · `memories-and-working-style`

128. **A latch must be non-vacuous: the test proves the condition it claims to catch was actually live at that instant.**
     > "**both** latches assert non-vacuity" ; "a non-vacuous `finished === false` check at the moment of closing" [agent]
     2026-08-28T06:11 / 2026-08-28T03:39 · "P3 fixer round 2" / "P3-W6" · `memories-and-working-style`

129. **A test's own claim is falsified by breaking it deliberately** — evidence over assertion.
     > "I proved the anchors are load-bearing by breaking one: the run stops after `note_list`." [agent]
     2026-08-28T12:03 · "P4 fixer: review verdicts" · `memories-and-working-style`

130. **A prescribed fix is disproved by experiment rather than argued about.**
     > "**Deviation, with evidence:** the prescribed `<Fragment key={id}>{children(id)}</Fragment>` defeats its own goal — I ran the experiment, and undefined→id remounts under it (mount counter #1→#2) while the unkeyed form preserves." [agent]
     2026-08-28T05:41 · "P3 fixer round 1" · `memories-and-working-style`

131. **Timing margins are computed arithmetically, not tuned by feel.**
     > "**Two-ongoing window (remedy 4):** A's turn runs 46 × 300 ms = 13.8 s; B's runs 32 × 300 ms = 9.6 s from its own start … Overlap = B's full 9.6 s — **≥ 8 s**." [agent]
     2026-08-28T06:28 · "P3 fixer round 2: e2e hardening" · `memories-and-working-style`

132. **Bracketing a capture inside a lifetime is proof, not margin.**
     > "dismissal is one-way, so bracketing is proof, not just margin." [agent]
     2026-08-28T06:28 · "P3 fixer round 2: e2e hardening" · `memories-and-working-style`

133. **A locator derived by index across an interaction is unsound; every handle must re-derive.**
     > "every `windowAtOrigin` result is now a live selector, so nothing in the lane is index-derived across a click" [agent]
     2026-08-28T12:03 · "P4 fixer: review verdicts" · `memories-and-working-style`

134. **A vacuously-passing test is a worse defect than a failing one, and is hunted specifically.**
     > "the propagation test's `other` was also stale (it had been reading the *first* window and passing vacuously)" [agent]
     2026-08-28T12:03 · "P4 fixer: review verdicts" · `memories-and-working-style`

135. **A stale-green incremental typecheck is caught by forcing a full rebuild** — the tooling itself is distrusted where it can lie.
     > "an earlier incremental run had gone stale-green and hidden a real break" [agent]
     2026-08-27T23:08 · "P3-W2: desktop host geometry+focus" · `memories-and-working-style`

136. **A "known reds" list (§G) names the failures never chased, so that a red is either on the list or is real.**
     > "Known-red per §G: `rescope-vendor` (environmental) and `verify-translation-pairing` (17 packages incl. ui-desktop await zh mirrors in W8)." [agent]
     2026-08-28T02:25 · "P3-W5: window manager chrome" · `memories-and-working-style`

137. **A pre-existing failure is proved pre-existing by removing one's own change and re-running.**
     > "**Verified pre-existing**: I temporarily removed my one `knip.json` line and re-ran `rescope-vendor --check` — identical two failures." [agent]
     2026-08-28T18:19 · "Build Phase 7 test lanes" · `memories-and-working-style`

138. **A production bug found in test triage is left red with file:line evidence rather than papered over.**
     > "## Production bugs (left red, not papered over)" [agent]
     2026-08-28T03:39 · "P3-W6: e2e lanes + goldens" · `memories-and-working-style`

139. **A seeded state may be written by driving the real host service in-process — "a write no browser made at all".**
     > "the precedent that *does* hold in this lane is `notes-window.e2e.ts` driving the Host service directly from the spec ('a write no browser made at all')" [agent quoting repo-doc]
     2026-08-28T18:19 · "Build Phase 7 test lanes" · `context-as-existence-runtimes`

140. **A scenario with no single session to harvest is hand-written in the recorded shape, and the module doc says so** — fabrication is bounded and declared.
     > "a scenario driving two Sessions at once has no single session to harvest; the lane skips record mode and the module doc says so." [agent]
     2026-08-28T03:39 · "P3-W6: e2e lanes + goldens" · `memories-and-working-style`

141. **A golden's blast radius is surveyed before the change, selector by selector, and "no existing golden touched" is reported as a result.**
     > "Added 6, changed 0. All existing goldens — desktop-recovery's included — are byte-identical." [agent]
     2026-08-28T03:39 · "P3-W6: e2e lanes + goldens" · `memories-and-working-style`

142. **Byte-identity of a fixture is proved by hash before and after.**
     > "**Fixture hash proof:** `7b93522c…` before and after — byte-identical." [agent]
     2026-08-29T08:17 · "Scope plugin authoring to cordis mode" · `memories-and-working-style`

143. **The real hazard in a concurrency change is named as a class, not a case.**
     > "**The real hazard is a second window, not the taskbar.** `.first()` makes all 40 `centerCol` captures … silently bind to the DOM-first ChatSurface." [agent]
     2026-08-27T22:24 · "Map phase-3 verification surfaces" · `memories-and-working-style`

144. **A test double that records but never moves the mirror is a stated limitation, so a spec needing motion must write it.**
     > "**inert recording** `openWindow`/`closeWindow` … — a spec that needs the mirror to move must write it with `set()`." [agent]
     2026-08-27T22:24 · "Map phase-3 verification surfaces" · `memories-and-working-style`

145. **A double that silently does less than the definition promises makes a test unreal, and is fixed before the test is trusted.**
     > "The stub's `_focusWindow` was silently not raising zOrder or the window revision (the Definition documents both), so I fixed the double — without it the test could not be real." [agent]
     2026-08-28T12:03 · "P4 fixer: review verdicts" · `memories-and-working-style`

146. **Concurrency ordering that depends on which call arrives first is marked in the source as an open problem, in the code, at the site.**
     > "`// XXX(concurrent-subagents): concurrent children need an explicit first-call ordinal.`" [repo-doc, `llm-replay/src/index.ts:578`]
     2026-08-27T22:24 · "Map phase-3 verification surfaces" · `memories-and-working-style`

### L. Method: how work is organized and how deviation is handled

147. **Work is organized into numbered parallel workstreams (W1–W8, N1–N6), then an adversarial review, then numbered fixer rounds (F1–F14, R1–R11, P1–P9), then a bilingual docs close.** The phase shape is itself a designed artifact.
     [agent, structure visible across all 38 entries]
     2026-08-27 – 2026-08-29 · whole batch · `memories-and-working-style`

148. **Every deviation from the brief is reported with a stated reason, under its own heading.** This appears in essentially every report: "Deviations, with rationale", "Two judgment calls you should know about", "Three deviations from the brief, each for a stated reason".
     > "**Two judgment calls you should know about**" ; "**Deviations from the spec, with rationale**" [agent]
     2026-08-27T23:00 · "P3-W1: slots/renderer substrate" · `memories-and-working-style`

149. **Scope is respected even at the cost of leaving a tree red: another workstream's file is not edited concurrently.**
     > "I left it for W4's owner rather than editing another workstream's package concurrently." [agent]
     2026-08-28T02:25 · "P3-W5: window manager chrome" · `memories-and-working-style`

150. **A finding is "reinterpreted honestly" when the diagnosis turns out to be wrong, and fixed at its true origin.**
     > "**F10 — reinterpreted honestly.** F5 removed the mutation collision, so the rename leg was never a collision cause. The real defect: a refused title bump made `fork()` reject … Fixed at the origin" [agent]
     2026-08-28T05:41 · "P3 fixer round 1" · `memories-and-working-style`

151. **A reviewer confirms every reported bug and reports where each is *wider* than reported.**
     > "**All four reported bugs verified, three of them wider than reported.**" [agent]
     2026-08-28T03:55 · "P3-W7: adversarial review" · `memories-and-working-style`

152. **The review ends with an explicit "candidate areas that came up clean" list** — negative results are reported, not discarded.
     > "# Candidate areas that came up clean" [agent]
     2026-08-28T05:48 · "P3-W7: adversarial review" · `memories-and-working-style`

153. **A reviewer states what it did *not* verify, so the evidence has known limits.**
     > "I did not run an official build or the three e2e lanes in replay — I skipped the build deliberately, so the e2e evidence in this review is static only." [agent]
     2026-08-28T05:48 · "P3-W7: adversarial review" · `memories-and-working-style`

154. **The verdict names must-fix, should-fix, and follow-up, and one item "wants a recorded decision rather than code".**
     > "The rest are follow-ups; **#13** wants a recorded decision rather than code." [agent]
     2026-08-28T05:48 · "P3-W7: adversarial review" · `memories-and-working-style`

155. **A defect found in one's own work during self-review is reported as such.**
     > "**Two defects I found and fixed in my own work**, both surfaced by recording the goldens and self-review" ; "**I caught a regression in my own first cut during e2e triage**" [agent]
     2026-08-28T09:34 / 2026-08-28T05:41 · "P4-N2" / "P3 fixer round 1" · `memories-and-working-style`

156. **Duplication is fenced with a written justification rather than silently tolerated, and the eventual extraction is named and assigned.**
     > "two `jscpd:ignore` regions with a written justification … Extracting a shared owner into `dsh-storage-domain` is the right eventual move but touches a committed phase-2 package beyond N1's scope — **flagging it for N5.**" [agent]
     2026-08-28T08:57 · "P4-N1: note seam host" · `memories-and-working-style`

157. **Every package carries an invariant companion, and an empty one must begin with a fixed phrase and give a package-specific reason.**
     > "an empty installer whose JSDoc **must** start with `No runtime invariant:` and give a package-specific reason" [repo-rule, `packages/CLAUDE.md`]
     2026-08-28T08:22 · "Map tool-authoring surfaces" · `keep-the-possibility-space-open`

158. **Rules are not duplicated across layers, because duplication lets the two drift.**
     > "Duplicating those rules would let the two drift." [agent]
     2026-08-28T16:01 · "Build tool-plugin-development package" · `human-solutions-museum`

159. **A shared counter is deliberately made page-wide rather than per-instance, because two private counters would collide at an occupied cell.**
     > "made page-wide deliberately, because the registry refuses a second entry at an occupied cell's exact priority, so two engines with private counters would collide" [agent]
     2026-08-28T14:32 · "Export draft-runtime execution seam" · `context-as-existence-runtimes`

160. **A stale ordered list is flagged as itself needing cleanup rather than quietly extended.**
     > "that list is substantially stale … the new group now sorts ahead of long-standing unordered groups. … the list is a candidate for its own cleanup." [agent]
     2026-08-28T18:26 · "Docs, catalogs, and Agent Note" · `memories-and-working-style`

161. **Honesty about mount placement in a generated catalog: what is not yet shipped is written as not yet shipped.**
     > "I recorded honestly: *'Not in any shipped tree yet: the `personal-plugin-runtime` bundle … arrives with the rest of the durable plugin runtime.'* **The bundle is still pending** — update that sentence when it lands." [agent]
     2026-08-28T16:01 · "Build tool-plugin-development package" · `memories-and-working-style`

162. **A rule found contradicted by a later decision is qualified in both languages rather than left self-contradictory.**
     > "`docs/subsystems/note.md` asserted a categorical rule this decision contradicts … I qualified it in both languages rather than leave the docs self-contradictory." [agent]
     2026-08-29T08:17 · "Scope plugin authoring to cordis mode" · `human-solutions-museum`

163. **A design is judged by what it earns at this version: a duplicate affordance "earns nothing at v1".**
     > "a rail duplicating a list the Back button already reaches earns nothing at v1" [agent]
     2026-08-28T09:41 · "P4-N3: Notes application client" · `memories-and-working-style`

164. **A widening of a shared primitive for one consumer is refused; a local component is built instead, with the divergence documented.**
     > "widening a statically-linked primitive for one consumer was outside W5. … hold 8s (documented as deliberately longer than Toast's 3s, since it must be reachable)" [agent]
     2026-08-28T02:25 · "P3-W5: window manager chrome" · `keep-the-possibility-space-open`

165. **Coverage is not a number but a gate: 100% per-file, with unreachable branches treated as a design smell rather than an exemption.**
     > "`test:coverage` **exit 0** (905 files, 15104 tests, 100% per-file …)" [agent]
     2026-08-28T05:41 · "P3 fixer round 1" · `memories-and-working-style`

166. **Every rule is written as a pure function so it can be tested and reused** — the window-manager chrome is "every rule as a pure function".
     > "`chrome.ts` — every rule as a pure function: `showsTitlebar`, `drawnWindows`, `windowStyle`, `restorePlacement`, `cascadeBounds`, …" [agent]
     2026-08-28T02:25 · "P3-W5: window manager chrome" · `jian-and-wenyan-as-formal-language`

167. **Placement is decided with the record, by the host — the client asks, the host places.**
     > "the launcher asks, the Host places" [repo-doc, `ui-desktop/README.md` pair title] ; "placement is decided with the record" [repo-doc, `desktop-domain/README.md`]
     2026-08-28T12:03 · "P4 fixer: review verdicts" · `context-as-existence-runtimes`

168. **A stale-because-derived comparison must be by value, not identity, when the source mints fresh objects on every pull.**
     > "`DesktopWindow` drops the preview on a placement **value** change, not `record.revision` (mirror pulls mint fresh objects, so identity comparison would not do)" [agent]
     2026-08-28T07:35 · "P3 fixer round 3: verdict items" · `context-as-existence-runtimes`

169. **A local optimistic preview is dropped only when the host confirms a change to *that* thing — and "focus is not one".**
     > module doc: the preview drops when the Host confirms "a change to this Window" — "focus is not one" [repo-doc + agent]
     2026-08-28T05:48 · "P3-W7: adversarial review" · `context-as-existence-runtimes`

170. **Convergence is by activation, serialized on one lane, so a roster refresh arriving mid-approval can never unload an unsettled candidate.**
     > "a roster pull arriving mid-approval runs *after* it, so no reconcile can unload an unsettled candidate." [agent]
     2026-08-28T16:21 · "Build personal-client-runner package" · `context-as-existence-runtimes`

171. **Failure unwinding rides the same convergence loop rather than being a separate rollback path.**
     > "**Failure unwinding rides convergence**: after `resolvePromotion(ok:false)` … the final reconcile sees a runId mismatch and re-mounts whatever the host still runs." [agent]
     2026-08-28T16:21 · "Build personal-client-runner package" · `shengsheng-buxi-generative-existence`

172. **A page that goes away mid-approval leaves the request armed, rather than resolving on behalf of an absent witness.**
     > "so an unproven candidate is never resolved for a page that is gone — matching the README's existing 'a page that goes away mid-approval leaves the request armed' contract" [agent]
     2026-08-28T19:24 · "Fix periphery review findings" · `the-fork-and-cooperative-infrastructure`

173. **A crash report names the slot, not a surface, because the supervision seam carries no registration key — and the limitation is documented rather than faked.**
     > "`surfaceId` on a render report is the crashed entry's **slot**, because the supervision seam carries no registration key — documented in Known Limitations" [agent]
     2026-08-28T16:21 · "Build personal-client-runner package" · `memories-and-working-style`

174. **An error state that a retry could clear must be deletable on rejection, not latched forever.**
     > "New `ui-plugin-studio/src/client/reads.ts` (`readOnce`) owns the ask-once latch and deletes the key on rejection" [agent]
     2026-08-28T19:24 · "Fix periphery review findings" · `keep-the-possibility-space-open`

175. **A pointer into a collection must be schema-checked against the collection, so a "cannot happen" throw stays honest.**
     > "`personalPluginRecord` gained a `.check()` requiring `currentPackageId ∈ packages[].packageId` … the defensive throw and its `v8 ignore` stay honest." [agent]
     2026-08-28T19:40 · "Fix registry review findings" · `jian-and-wenyan-as-formal-language`

176. **A serialization lane must be split by purpose or the system deadlocks against itself.**
     > "A host half that `await`s `harness.storage.get(...)` during activation would then deadlock against the transaction activating it. I kept one `operationTails` map and one `enqueue`, keyed by lane" [agent]
     2026-08-28T15:33 · "Build plugin-registry core package" · `context-as-existence-runtimes`

177. **An id-mismatch guard is preferable to a mocked randomness source, because randomness has other consumers.**
     > "rather than mocking `node:crypto` (brittle — the package store also consumes randomness), the collision is injected through the predicate, which is the exact signal the loop reacts to" [agent]
     2026-08-28T19:40 · "Fix registry review findings" · `memories-and-working-style`

178. **A browser-serialization surprise is probed against a real browser and then written into the comment.**
     > "Chromium re-serializes `inset: auto` + `left`/`top` back into the `inset` shorthand. I probed a real Chromium to confirm the exact attribute text … and the selector now matches … documented with that reasoning." [agent]
     2026-08-28T12:03 · "P4 fixer: review verdicts" · `memories-and-working-style`

---

## Recurring preoccupations

These are the preoccupations of the *codebase and its standing orders* over three days (2026-08-27 → 2026-08-29), not of Ren's prose in this batch.

- **Nothing may be lost silently.** From the phase-3 conflict-as-commit defect (08-27 → 08-28 review) through the note editor's `expectedRevision`-is-the-caller's rule (08-28 09:41) to the phase-7 registry findings about a disabled plugin adopted at commit and a leaked live candidate (08-28 18:54, 19:40), the same law recurs: a refusal must be visible, a conflict must not install as a commit, a latch must latch on success. Items 27–38, 118, 122.
- **Existence is scoped and refcounted, not global.** The global "current session" is deleted on 08-28 00:21 and replaced by leases; per-window store instances arrive 08-28 05:41; per-plugin activation lanes arrive 08-28 15:33 and 16:21. The unifying claim: a thing is alive exactly while something holds it. Items 1–15, 170–172, 176.
- **Widening is an act.** Recorded at the interface itself on 08-27 22:22, restated on 08-28 08:19, and applied on 08-29 08:58/08:59 to Application allowlists and preset bindings, where "silently widening" is the named failure the acceptance criterion forbids. Items 16–18, 110–112, 124–125.
- **The model's context is a documented, budgeted resource.** The `## Model Experience` / token effect / KV-cache effect triple is enforced on every package README across the whole batch (08-28 08:19 through 08-29 08:17), and it repeatedly drives concrete code decisions: epoch timestamps removed from listings, caps applied to emitted arrays, prompt text pinned by test. Items 53–66, 107.
- **Bilingual doc pairing intensifies.** 1,031 pairs on 08-28 08:02 → 1,041 on 08-28 12:45 → 1,048 on 08-28 17:52 → 1,051 on 08-28 19:24/19:40. The character of the discipline deepens too: from mechanical mirroring to terminology arbitration (契约 vs 约定, 08-28 12:45) and byte-identical cross-locale anchors. Items 81–88.
- **Documents govern code and are governed in turn.** Frozen word ceilings, one-owner-per-fact, no change narration, machine-checkable links, Agent Notes with a fixed anatomy, and the rule that a factually wrong paragraph is an obligation. Items 89–99, 160–162.
- **The phase shape repeats.** Map → parallel workstreams → adversarial review → numbered fixer rounds → docs/bilingual close, three times over (Phase 3 on 08-27/28, Phase 4 on 08-28, Phase 7 on 08-28/29). Item 147.
- **Human authority is designed in.** Enable/disable/uninstall are the user's; a rejection is not re-requested; the approving page proves the client half; a candidate may read but not write. This cluster appears only in Phase 7 (08-28 16:01 → 08-29 08:17) and is the batch's most theory-bearing material. Items 113–125.

---

## Ideas that appear nowhere else in the corpus

Candidates the written drafts likely do not carry, all from the engineering register:

1. **The window/session biconditional as a stated ontological commitment** — "the window opens ⟺ the session is on stage" — a formal biconditional written into a module doc, and the refcounted lease that replaces global selection. This is `context-as-existence-runtimes` implemented and named, not theorized. (Items 1–4.)
2. **"Writing the binding IS the navigation."** Navigation as an epiphenomenon of a durable fact changing. A crisp, quotable formulation of "context is existence" in operational terms. (Item 5.)
3. **The `## Model Experience` README section as a mandatory, gate-enforced declaration** that every package state what the model sees, its token effect, and its KV-cache effect. A governance idea about machine cognition as a shared, budgeted commons — no draft in the corpus is likely to carry this. (Items 53–55.)
4. **"Uncovered fiction"** as a term of art for an interface arm nothing can reach. (Item 21.)
5. **The bilingual technical kernel with a declared untranslated core** — `seam` stays `seam` while bundle/seat/lease/viewport/taskbar/launcher become 组合包/座位/租约/视口/任务栏/启动器, and window chrome becomes 窗饰. A worked example of Ren's `jian-and-wenyan` programme applied to a live engineering vocabulary. (Items 83–84.)
6. **Terminology arbitration by family coherence over corpus frequency** (契约 chosen against a 73:13 prescription for 约定, and the choice surfaced for overrule). A method for how a formal vocabulary evolves without central fiat. (Item 85.)
7. **"A rejection is not re-requested"** written into an agent's system prompt — a norm against the retry-until-yes pattern, stated as agent policy rather than as a guardrail. (Item 114.)
8. **"The approving page proves the client half."** Human consent doubles as the proof-of-execution. (Item 116.)
9. **The refusal-as-teaching-text pattern**: a guard's error names the legal alternatives back to the model. (Item 62.)
10. **"Constants are mirrored, never imported"** across compiler aggregates, with each mirror naming its source — deliberate, documented duplication as a boundary discipline. (Item 77.)
11. **A rule that a mechanism must not exist without a caller** — "D3 is dead code in production" filed as a blocker-class review finding. (Item 9.)
12. **Content-addressed package identity plus canonical-by-construction serialization**, so that "a field added to a schema cannot silently drop out of the digest". (Items 49–50.)

---

## Ren's questions

**None.** This batch contains no messages from Ren, and therefore no questions of his. The interrogatives present in the file are agents' own framings and reviewers' prompts — they are not Ren's and must not be quoted as such.

Two questions are put *to* Ren by agents, which is the closest this batch comes; they are worth recording only as evidence of what the workflow escalates:

- "**Terminology call worth a reviewer's eye:** … say the word and I will switch the family to 约定." — 2026-08-28T12:45, "P4-N6: docs + bilingual close"
- "If you want a green tree before then, the fix is to demote those four link sites … to plain code-font package names — tell me and I'll do it." — 2026-08-28T14:41, "Build surface-plugin-studio package"

For genuine Ren questions in the deepseek-harness period, the parent agent should look to a batch that actually contains his turns; cb-04 cannot supply them.

---

## Style and method notes

**The batch cannot tell us how Ren writes — only what his agents write back to him, and what his repository's standing orders require.** With that caveat, several method signatures are visible and are almost certainly his, because they are consistent across 38 independent agents, three phases, and two sessions:

1. **Deviation must be declared and justified, never absorbed.** Every single report has a section for it: "Two judgment calls you should know about", "Three deviations from the brief, each for a stated reason", "Deviations / things you need to know", "**Deviation, with evidence**". The template is: what the brief said, what was done instead, why, and what it costs.

2. **Evidence over argument.** A prescribed fix is disproved by running the experiment ("I ran the experiment, and undefined→id remounts under it (mount counter #1→#2)"); a load-bearing assertion is proved by deliberately breaking it ("I proved the anchors are load-bearing by breaking one: the run stops after `note_list`"); a pre-existing failure is proved by removing one's own change and re-running.

3. **Report what was *not* done, and what came up clean.** "I did not run an official build or the three e2e lanes in replay — I skipped the build deliberately, so the e2e evidence in this review is static only." And a whole section headed "# Candidate areas that came up clean".

4. **Honest recording over convenient wording.** "**F10 — reinterpreted honestly.**" ; "I recorded honestly: *'Not in any shipped tree yet…'*" ; "the defensive throw and its `v8 ignore` stay honest."

5. **Scope is a boundary, not a suggestion** — even when respecting it leaves the tree red. "I left it for W4's owner rather than editing another workstream's package concurrently." ; "it is a peer phase's note and outside my brief, so I flagged it as a follow-up task rather than rewriting it."

6. **Some findings want a recorded decision rather than a code change.** "**#13** wants a recorded decision rather than code." The corollary appears in the doc register too: a rule that outlives its fix deserves a note.

7. **Correction is stated as a rule, not as a patch.** Reviewers repeatedly generalize: "latch on success, not on attempt"; "the predicate now asks the entries, not the pull state"; "drop the preview on a bounds/mode change" ; "the intersect requires both (a) … and (b) …".

8. **Prose is corrected with exact replacement text, not with a complaint.** The prose reviewer supplies verbatim substitutes for every violation it names — "Replace: 'and no Remote method or tool added by this phase accepts a caller-supplied user identity.'" — which is a distinctive review style, and one that only works where a house prose standard already exists.

9. **Bilingual completion is treated as part of the deliverable, not as follow-up** — but it is systematically deferred to a named workstream (W8, N6) rather than done badly in-flight. "READMEs edited **English-only** (§G): … zh mirrors + i18n sidecars are W8's."

10. **A methodological caution for whoever reads this batch next.** These reports are extremely fluent and extremely confident. Their fluency is not evidence about Ren. Any sentence in cb-04 attributed to Ren would be an invention; the design philosophy above is his only in the weaker sense that he directs the repository these agents were mapping.
