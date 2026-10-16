# P84 landing package: transmission, derived or bounded

Under Ren's "move towards 100%" (12 October 2026, [source](../../../../../../sources/15-codex-theory-conversations/2026-10-12-move-towards-100.md)), the session "Current math core" [1c3084] claimed P84 on the [work board](../../../../../BECOMING-WORKBOARD.md). It answers the chapter's §8 further proof, "deriving transmission from how dependence forms (`TransmitsWithin` is now a premise)", and the matching item in the next delta of `evolution-on-descent`. An Opus subagent of the session built the module, and the session checked it.

| Item | Module | Layer | Imports | Records |
|---|---|---|---|---|
| P84 transmission | `Becoming.Transmission` | L3 | `Premises` | transmission-is-inheritance-and-need, transmission-independent-where-it-binds (F01); a delta to evolution-on-descent |

No existing module changes. `REGISTRATION.md` (the subagent's landing notes) gives:
- the root import;
- the docstring bullet;
- the `CORE` entry;
- an optional wording pointer in `Evolution`'s docstring.

## What it contains

`lean/Becoming/Transmission.lean`: 64 theorems and 83 declarations by the checker's parser (168 constants with compiler auxiliaries). It is all term-mode.

- **Exact form.** Transmission is inheritance with the need within a bound (`Flow.transmitsWithin_iff`). Where the descendant held no dependence before it stood, inheritance is the law of forming at coming to stand (`Web.inheritsAt_iff_forming`). The split into forming and holding is exact where the earlier holding is decided; asked of every descent, it is excluded middle (`split_iff_em`).
- **What it carries.** Under balance, descent forms no new dependence (`Flow.no_new_dependence`). The evolution bounds need it only at the descent they use, and there only from some supported giver (`Flow.fromSome_supported`). That form is strictly weaker (`TwoGivers.twofold`).
- **Independent wherever it binds.** Dropping one dependence of the giver keeps every other premise and finiteness, and breaks transmission (`World.drop_but`). So no law kept by dropping a dependence derives it (`World.vacuous_of_drop_invariant`, `World.drawn_not_enough`).
- **What derives it.**
  - The reading of drawing, together with drawing being depending, derives it (`World.transmitting_of_drawn`).
  - The derivation is not vacuous (`World.bearingHatch_derived`).
  - Each of the two is needed (`World.drawn_and_link_needed`).

## Verified in scratch

- **Against main.** `scratch_build.py` against main `66dc4450`: no error or warning. The audit of `Becoming.Transmission` reports 64 theorems and 83 declarations, none using an axiom.
- **The subagent's own build.** Its `mk.sh` build reported 168 constants and no forbidden token.
- **Name clashes.** A text scan found none against the core, P69's `Unfolding` or the queued packages (P70–P73, P76–P82, P85).

## Docs

- `docs/records/`: the two record drafts.
- `docs/records/record_delta.py`: points evolution-on-descent's next delta and limitation to the new records, adds a related entry and a history line. A dry run on a copy applies cleanly.
- `docs/study/`: the study section, zh and en.

## Not achieved

- No derivation from the core alone; this is proved impossible.
- The link (drawing is depending) is sufficient, not necessary.
- The need bound is coarse.
- No census law is stated.
- Weakening `World.Transmitting` to `TransmitsFromSome` would change the map of premises and is Ren's call.
- No independent review yet.
