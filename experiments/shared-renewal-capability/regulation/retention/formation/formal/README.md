# Checked formation and localized copying of competing variants

6 October 2026. [FormedSelection.lean](FormedSelection.lean) and [FormationRoot.lean](FormationRoot.lean) contain **53 checked theorem declarations** for the discrete formation law and its exact connection to the repository's existing causal root. They use Lean 4.29.1 and `Std`. The previous root is compiled from its original source as a dependency; its existing declarations are counted separately in the [verification record](verification.json).

The governing scope is in [FORMED-VARIANT-SELECTION-LEAN.md](../../../../../../_process/research/2026-10-05-support-and-shared-generativity/completion/FORMED-VARIANT-SELECTION-LEAN.md). These are event-law, accounting and reachability proofs. Expected selective advantage belongs to the separate analytical and computational work; it is not certified here.

## State and transition interface

The state fields, in order, are

`(aFree, hFree, resident, intact, localFuel, fuel, source)`.

`resident` is `empty`, `active` or `alternative`; the two site fields are Boolean. There is one site. Material M is a natural-number parameter; precursor is derived as M minus the count of all free and resident variants. Every step requires that count to be at most M and preserves the bound. The corresponding Python convention uses resident codes 0, 1 and 2 and Boolean site flags 0 and 1. This mapping is documented for review, not machine-proved as a Python refinement.

The sixteen event labels are two formation events, two paid association events, repair, capture, two local-copy events, two bulk-copy events, two free-variant wear events, resident wear, site damage and two leakage events. Formation requires a damaged site, available precursor and common fuel. Both types have that same enabling condition. Only an active resident can repair; any resident can copy using local fuel. Bulk copying requires an existing template of the corresponding type. Wear returns precursor; resident wear preserves the site's condition and local fuel.

`Enabled` and `advance` state every guard and update explicitly. Stochastic rate coefficients, negative controls and optional catalytic-consumption channels are outside this formal relation. Turning off a channel restricts its paths and preserves the universal path constraints; changing an update requires a separate check.

## Results that constrain the mechanism

- **Material and energy accounting:** every finite valid path preserves total precursor plus variants. Final common fuel, local fuel, incident support and all spent units equal their initial total. A separate ledger records common-fuel spending; source capture never silently refills the common pool. Copy count cannot exceed the initial total fuel.
- **Finite event bound:** `4E + 2F + 2L + C + population` decreases by one or two on every event. No infinite event sequence exists in this finite-stock law. This does not limit elapsed waiting time or imply a universal value measure.
- **Paid bootstrap:** from an absent, vacant, damaged preparation, restoring an intact site needs at least three initial common-fuel units. If an alternative variant is present with that restored site, at least four initial common units were necessary. The second result explicitly charges the competing variant's origin.
- **Type ancestry:** a previously absent type cannot appear along a trace containing none of its own formation events. Every copy requires an existing template and increases only that template's type. This checks type-level ancestry, not an individually tagged molecular genealogy.
- **Local access before resident wear:** on every history from the initial preparation without resident wear, an alternative resident never has an intact site or local fuel. Therefore no H local copy occurs. Free wear, additional formation and other enabled events are allowed by this invariant.
- **An actual counterpath:** when resident wear is allowed, an H variant can inherit the site repaired by A and then produce an H copy. The useful contributor's disappearance and the alternative's growth occur under the same supplied law.

The four-unit result uses a history-independent bound on common fuel plus paid progress. The progress term is three when the site is intact, two when an A resident is installed at a damaged site, and otherwise at most one for an existing A; a separate unit records whether H exists. Every event preserves or decreases their sum with common fuel. This avoids assuming that the second variant or the contest preparation is supplied for free.

## Mixed witness from complete variant absence

With M=3, initial F=4 and E=1, the checked path is

**form H → form A → associate A → repair → capture → copy A**.

Both variants begin absent and the site begins damaged, vacant and without local fuel. The final state contains A=2 and H=1. Four common units pay both formations, association and repair. The newly captured source packet pays copying. All intermediate states are carried through the same law; the proof does not restart at a favorable mixed preparation.

This proves an admissible mixed formation-to-copy path. It does not claim that every history follows it, that the path is likely, or that its population ratio establishes an expected selection effect. Those questions require the actual event rates and all competing histories.

The separate counterpath starts with M=2, F=5 and E=1:

**form A → form H → associate A → repair → resident wear → associate H → capture → copy H**.

It ends with A=0 and H=2. That witness makes the no-resident-wear premise of the access invariant explicit and rules out treating private access as an unconditional reward for useful contribution.

## Reproduce

Run `python3 check.py` from this directory. The checker explicitly selects `lean +leanprover/lean4:v4.29.1`, records the compiler hash, freezes all source bytes, and compiles in a fresh temporary build. Its original-root dependency is [GenerativeCore.lean](../../../../../integrated-correction/general-framework/generative-basis/lean/GenerativeCore.lean). No previously compiled project object is reused.

Every new theorem must have an axiom audit. The script rejects proof placeholders, custom axioms, unsafe declarations, native decision shortcuts, warnings and unexpected axiom dependencies. [verification.json](verification.json) and [verification/](verification/) preserve source, checker, compiler and log hashes. Only the disclosed standard Lean foundations are accepted. The command replaces only this directory's verification artifacts.

`FormationRoot.lean` proves exact equivalence with `Generative.Trace`, transports the ledger, bootstrap bounds, mixed witness and inheritance counterpath, and obtains actual-state concatenation directly from the earlier root. This establishes formal compatibility with the root, while the chemistry, type repertoire, local-access architecture and copying specificity remain supplied premises.
