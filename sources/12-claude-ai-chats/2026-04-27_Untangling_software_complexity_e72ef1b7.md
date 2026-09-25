# Untangling software complexity

created: 2026-04-27T13:20:16.789830Z  uuid: e72ef1b7-32d2-4dfc-abbf-7b1cba147bf0  export: new
messages: 2  total_chars: 6885  human_chars: 60


---
**HUMAN** (2026-04-27T13:20):

explain and summarize https://www.inkandswitch.com/untangle/

---
**ASSISTANT** (2026-04-27T13:21):

  The user has provided a URL and wants me to explain and summarize it, so I'll need to fetch the content from that link to see what information it contains.
```
This block is not supported on your current device yet.
```

 I'm thinking through how to present this Ink & Switch research on Untangle in a way that resonates with Ren's interests—their background in agent architectures and programmable interfaces makes this particularly relevant, especially given the spatial and graphical computation aspects they've been exploring.# Untangle (Ink & Switch, 2023)

Untangle is a research prototype from Ink & Switch (Szymon Kaliski, Marcel Goethals, Mike Kluev) that asks: what would a theorem prover feel like if it met you where you actually think — sketching with a stylus, fuzzy, reactive, willing to give you a "good enough" answer instead of an error?

## The core gambit

Formal constraint solvers (Prolog, Z3, Alloy, ASP) are powerful but demand that you fully understand and formalize the problem before they help. In practice, we usually understand a problem *by* working through it on paper — wedding seating, scheduling, assigning graders. The hard part isn't the search; it's the formalization. Untangle tries to collapse that gap by letting you sketch the problem and have the machine continuously propose solutions while you sketch.

It uses Z3 underneath, but exposes none of Z3's surface area. The interface is hand-drawn ink, spatial queries, and arrows.

## The three primitives

The whole system is built from three things that compose into a "ladder of abstraction":

**Symbols** are anything on the canvas — strokes grouped into a unit ("Bob", a box, a tally mark).

**Arrows** assign one symbol into another (drag "Bob" into a box). The solver fills the assignment; if multiple assignments satisfy, dots appear at the bottom and you scroll through alternatives.

**Spatial queries** are reified selections. Select a column of names and Untangle offers a query template like "vertical column starting with Bob." Drop that query on the canvas and now the arrow operates over *all* matching symbols, not just one. Queries include things like "box with something to its left," wildcards (`?`), `count` modifiers, and a `lookup` query for table-like layouts. Crucially, spatial matching is *fuzzy* — "roughly to the left," not "exactly 137px."

The reification idea is the key pedagogical move: each primitive is a generalized version of something you could already do manually one step earlier. Manual drag → arrow → spatial-query-driven arrow.

## The examples

They walk through five problems that get progressively weirder:

1. **Peer grading assignment** — six students, a box next to each name, a wildcard rule that nobody grades themselves, plus pinning Bob↔Claire because they wrote on similar topics. Add a seventh student and the whole thing reflows.

2. **5G spectrum auction** — telcos bidding on bands. Introduces `count` (Verizon wants 4 bands), spatial preference (specific bands), and *over-constraint relaxation*: when bids exceed slots, instead of erroring, Untangle drops some constraints and colors the violated arrows red. The framing they like: "no, but what if…" beats "no."

3. **Coffee shop schedule** — two-dimensional. Availability table in one corner (X marks), empty week schedule in another, `lookup` query bridges them, plus a "no two consecutive days the same person" constraint.

4. **Generative art (10 PRINT)** — flips the usage from collapsing the solution space to *expanding* it. Same primitives, opposite intent.

5. **Recursive rewrites** — flatten pink (computed) results back into black ink, the queries re-fire, and you get cellular automata or logic gate networks. This is the most interesting move — it's the same trick as graphical production systems / Wave Function Collapse.

## Findings worth holding onto

- There's a **sweet spot** of problem size: small enough to draw by hand, complex enough that you can't keep it in working memory. Above that, hand-drawing is too tedious; below it, you'd just solve it directly.
- Problem representations **drift toward tables** — but starting freeform and arriving at a table feels different (better) than being forced into one upfront.
- **Fuzziness is conversational.** Spatial queries that match "roughly," arrows that don't snap to ports, solvers that relax rather than refuse — together they produce a feel of dialogue rather than specification.
- **Fidelity should match maturity of the idea.** Ink for early-stage thinking; vector/crisp for mature representations. They tried vector early and it created cognitive dissonance.

## Honest shortcomings

The team is unusually candid about what doesn't work:

- **No clear semantics.** The query primitives are ad-hoc — added per example. They don't compose. You can't combine "to the left" + "to the top" to build the lookup query; lookup is its own primitive. Pure example-based query construction is also tedious.
- **Stroke→symbol grouping is a crutch.** Users have to manually group strokes into a "symbol" via a magic wand. Reliable automatic grouping is a long-standing unsolved problem (going back to Palm Graffiti).
- **Visibility gaps.** Arrows can dangle without valid sources/targets and you only know via the absence of solution updates.
- **Computer voice is under-designed.** Pink-for-computed works in a one-color system but doesn't generalize.
- **Small canvas, no pan/zoom**, so problem scale is artificially capped. They flag "Untangle with external data" as future work.
- **No solution-space visualization.** You scrub through one result at a time; can't see clusters, branches, or how a constraint cuts the space.

## What it's part of

Untangle sits in Ink & Switch's "programmable ink" track alongside [Inkbase](https://www.inkandswitch.com/inkbase/) and [Crosscut](https://www.inkandswitch.com/crosscut/). The throughline is: directly manipulable representations that stay alive and reactive, so you can improvise and stay in intuitive (System 1) mode rather than switching to effortful (System 2) symbolic computation.

The thesis they end on: this is a glimpse of *conversation with a dynamic medium* — sketching at the speed of thought, collaborating with the machine, with fuzziness as a feature of the interface rather than a bug to be eliminated.

---

Given the SST work and OpenClaw's emphasis on minimal-intervention delegation, the bit I'd flag as most relevant is the relaxation behavior — the system's choice to return a partially-correct solution with red-tagged violations rather than erroring. That's a different posture toward "incorrectness" than most agent harnesses take, and it pairs interestingly with how you've been thinking about agent loops that stream incremental output rather than blocking on full satisfaction.
