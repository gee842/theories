# U2: joining the periphery to the base (brief for one batch)

17 October 2026. Ren, on U's open items: "let's fix all these" ([source](../../../../../../../sources/15-codex-theory-conversations/2026-10-17-unification-follow-through.md)); one of them is that the periphery is not measured or joined. Ren chose eight Opus batches. The integrator (the session "Repository completion review and restructure") holds board item **U2** and lands everything. You write join modules for one batch of periphery modules, verify them in scratch, and report. You do not land, commit, run `check_becoming.py`, edit records, or edit any existing file.

Read [the U brief](../U-BRIEF.md) first: the meaning of apart, roots and joins, the standard, the categories and the tools all carry over. This brief gives only what differs.

## What differs from U

1. **The periphery.** The core checker's run compiles 78 inherited modules besides the spine: the foundation (`GenerativeCore`, `InquirySufficiency`, `RelationalRenewal`) and 75 earlier modules (ethics, correction, inquiry, explanation, composition) in `experiments/integrated-correction/general-framework/generative-basis/lean/`, `.../lean/universal-ethics/` and `.../lean/inquiry-root/`. The bridge modules (`Becoming.Bridge`, `Becoming.Instances`, `Becoming.RenewalBridge`, `Becoming.CoursesBridge`, …) import some of them and prove that their interfaces are the core's concepts. On main, 814 of the 1,282 theorems of these modules stand apart from the base, and 527 of those are roots. Find a module's file with `python3 -B -c "import check_becoming as cb; print(cb.module_index()['NAME'])"` from the package folder.
2. **Join modules are bridge modules.** They import the periphery module(s) of your batch and the core modules they need (`Becoming.Runs`, `Becoming.Frame`, `Becoming.Space`, `Becoming.Flow`, …, or the root `Becoming`). The core never imports them, and they are registered on the bridge side. They live at `Becoming/<Name>.lean` in your batch folder, namespace `Becoming.<Name>`. Templates: `Becoming/RenewalBridge.lean` (a periphery family shown to be a balanced flow, with its results derived from the spine's laws), `Becoming/Instances.lean`, `Becoming/CoursesBridge.lean`, and U's pilot `../pilot/Becoming/SeekingRuns.lean`.
3. **What a periphery join is.** Prefer, in this order:
   - **Instance.** The periphery structure *is* a base object: its states and steps are a `Process`, its histories `Run`s or traces, its quantities a `Flow` and `Web`, its situation a `World`. State that reading with the theorem that makes it exact. Then state the periphery theorem's law of that base object, proved through the periphery theorem. Where the spine already has the general law, prefer deriving the periphery's law from it (as `RenewalBridge` does).
   - **Reading off a base object.** The periphery's vocabulary is read off a run, process, frame, world, flow or web. This is U's standard join.
   - **Classification.** Classify it, using U's categories (support, logical-strength, model-witness, restates, general-structure, bridge-interface). Two categories are added:
     - `axiom-dependent`: the root's own axiom report is not empty (it uses `propext`, `Classical.choice`, `Quot.sound` or `funext`). A join on the bridge must have an empty report, so it cannot use the root. Check this with the audit before you classify.
     - `periphery-scope`: the root is a statement about the periphery's own abstract interface (an evaluator, a standard, a priority, a policy space) that has no evident reading as a process, run or world, and the bridge already identifies that interface with a core concept where one exists. Name the core concept or say there is none.
4. **Names and prose.** Use structural names in the core's vocabulary, not the periphery's social or evaluative words, wherever a structural word exists (AGENTS.md, board rule 8). A module name ends in a structural word (`Runs`, `Worlds`, `Traces`, `Flows`, `Webs`, `Frames`, `Processes`). Do not reuse the periphery's dualist or limited-scope names (Warrant, Permitted, Admits, Command, Priority, Rival) in new names. Use the current labels: "living significance", not G0; "the continuation condition", not "the axiom" or "the one axiom"; "the theory without axiom", not Part I. Docstrings are in English and claims say exactly what the Lean proves.
5. **Do not edit any periphery or spine file.** If a periphery theorem looks wrong or misplaced, report it.

## Tools (as in U, from the package folder unless stated)

- Build and audit: `BECOMING_JOBS=2 python3 -B scratch_build.py TREE` (TREE = your batch folder). Each of your modules must show `"unclean": []` and `"with_axioms": {}`. To audit a periphery module's own declarations, name it: `python3 -B scratch_build.py TREE NAME`.
- Measure (from the repository root): `python3 -B _process/research/2026-10-05-generative-foundation-review/root-foundation/development/u-unification/apart_roots.py TREE/apart.json TREE`. Since U2 it measures spine and periphery together. The starting list is `u2/periphery-before.json`.

## Deliverables in your batch folder

1. `Becoming/<Name>.lean`: one or more join modules, building clean.
2. `classification.json`: `{"<theorem>": {"module": "...", "category": "...", "reason": "..."}}` for every root of your periphery modules still apart at the end.
3. The report, as your final message (subagents may not write report files; the integrator saves it as `REPORT.md`). Keep it short and in English: the modules written; the roots covered and the readings used; the apart count and root count for your periphery modules, before and after; anything wrong or misplaced in a periphery module; anything the integrator must decide.

Work through your periphery modules in the order given. Aim to join every root that has a meaningful reading on the base, and classify the rest. Keep proofs short and route them through the roots.
