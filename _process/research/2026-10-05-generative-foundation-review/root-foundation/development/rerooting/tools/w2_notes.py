"""W2: say in each module's docstring where its moved declarations now are, and where a module's
received declarations came from.

usage: w2_notes.py PACKAGE

Each note is a paragraph added at the end of the module docstring (before its closing `-/`). Run
after move_decls.py; a module whose docstring already holds its note is left unchanged.
"""
import sys
from pathlib import Path

FRAME = "so this module does not import the frame (board item W)."
NOTES = {
    # Modules whose readings of the labelled process moved out.
    "Becoming.Recurrence": "The laws of a determined law as a process and of reach along runs (`Law.process`, "
    "`Law.run`, `Run.revisits_from`, `keeps_reach_iff_returns`, `not_returns_iff_loses`, `WithinMoves` and "
    "what follows from it) are in `Becoming.Labelled`, " + FRAME + " `Law.SameFuture`, from "
    "`Becoming.Unfolding`, and `trajectory`, from `Becoming.Mechanism`, are stated here (see the sections so headed).",
    "Becoming.Metaethics": "The valuations read on frames (`Valuation.relations`, `G0`, `universal_reason`, "
    "`Comparison`, `Extension`, `LiftBetter`, the `Conditions`, `Separate` and `Model` instances) are in "
    "`Becoming.ValuationFrames`, " + FRAME,
    "Becoming.Significance": "`Conditions.significant_of_unrestricted` and the paths of a web (`Web.paths` and "
    "its comparison theorems) are in `Becoming.ValuationFrames`, " + FRAME,
    "Becoming.Diagonal": "`Frame.self_incomplete` is in `Becoming.DiagonalRuns`, " + FRAME,
    "Becoming.Context": "Contexts read as laws on configurations (`Contextual.indexed`, `Contextual.no_free_frame`, "
    "`pooledLaw`, `retainedLaw`, `evolvingLaw`, `erasedLaw`, `Arrives` and the witnesses `CrossingContexts` and "
    "`ChangingContext`) are in `Becoming.ContextArrivalTraces`, " + FRAME,
    "Becoming.Testing": "Judging a class along runs (`Web.class_judge_iff`, `Web.class_judge_later`, "
    "`Web.class_judge_widen`, `Flow.class_judge_beyond`) and the finite readings of renewal "
    "(`Renewable.finite_reading_withholds_renewal`, `Renewable.no_exact_finite_reading`), with "
    "`sees_narrow`, which only they use, are in `Becoming.LabelledRoles`, " + FRAME,
    "Becoming.Weighted": "`counting_transfer_iff` and `possibility_transfer_iff` are in `Becoming.WeightedTraces`, "
    + FRAME,
    "Becoming.Capture": "`Law.perturbation_reabsorbed` is in `Becoming.SeekingRuns`, " + FRAME,
    "Becoming.Counterfactual": "The laws of exchange along runs (`ExchangeLaw.worldRun`, "
    "`ExchangeLaw.world_exchange_iff`, `ExchangeLaw.act_not_taken`, `Run.beyond_shown_iff`, "
    "`ExchangeLaw.counterfactual_beyond_shown`, `ExchangeLaw.closedBy_course`) are in "
    "`Becoming.CounterfactualRuns`, " + FRAME + " `trajectory` is stated in `Becoming.Recurrence`.",
    "Becoming.Learning": "`Learning.GoAlikeAt`, `Learning.goAlike_iff_at`, `Learning.transfer_right_iff` and "
    "`Learning.goAlike_iff_lumped` are in `Becoming.LearningRuns`, " + FRAME,
    "Becoming.Description": "The laws that identify alike configurations (`Law.identifiesAlike_of_law` and the "
    "other `Law` theorems on identifying alike, `Law.kernel_bisimulation`, `Law.sameFuture_of_law`, the "
    "`Motion` witnesses and `alike_moments_iff`) are in `Becoming.IdentificationRuns`, " + FRAME,
    "Becoming.Identification": "`Law.name_identifiesAlike`, `Law.name_carries` and `Law.decideAlike` are in "
    "`Becoming.IdentificationRuns`, " + FRAME,
    "Becoming.Lexical": "The two tiers on a frame (`Lexical.Frame.Above` and its laws, `Lexical.tierFrame`, "
    "`Lexical.above_iff_frame`, `Lexical.included_basicSide_iff`, `Lexical.included_gainSide_iff`) are in "
    "`Becoming.FrontierFrames`, which states the commitments on a frame, " + FRAME,
    "Becoming.Frontier": "The formation witness as steps of a process and on its frame (`Requirement.Formation.draw`, "
    "`Requirement.Formation.frame` and their laws) and `Requirement.Required.through_summary` are in "
    "`Becoming.FrontierFrames`, which states the commitments on a frame, " + FRAME,
    # Modules that keep their readings and gave a few declarations to a module free of the frame.
    "Becoming.Composition": "Joint plans and exclusive footprints for any ternary relation (`JointPlan`, "
    "`JointPlan.Realizes`, `JointPlan.draws`, `PartsWithin`, `PartsApart`, `Supports`, "
    "`JointPlan.within_of_realizes`, `JointPlan.nodup_of_realizes`, `JointPlan.supports_of_realizes`, "
    "`mem_appended_split`, `nodup_append_of_apart`) are in `Becoming.JointPlans`, so the modules using them "
    "do not import the frame (board item W).",
    "Becoming.Joining": "`Joining.appended_assoc` is in `Becoming.Decidedness`, so the modules using it do not "
    "import the frame (board item W).",
    "Becoming.Coverage": "`Coverage.Perm.mem` is in `Becoming.Decidedness`, so `Becoming.ListFootprints` does "
    "not import the frame (board item W).",
    "Becoming.Horizon": "The support-gated law (`Feedback`) is in `Becoming.HorizonWebs`, which states the "
    "horizon on its webs, so that module does not import the frame (board item W).",
    "Becoming.Mechanism": "`trajectory` is stated in `Becoming.Recurrence`, beside `Law.orbit`, so "
    "`Becoming.Counterfactual` does not import the frame (board item W).",
    "Becoming.Unfolding": "`Law.SameFuture` is stated in `Becoming.Recurrence`, so the modules using it do not "
    "import the frame (board item W).",
    "Becoming.Likeness": "`Decided.exists_listed` and `Decided.exists_not_in` are in `Becoming.Decidedness`, so "
    "the modules using them do not import the frame (board item W).",
    "Becoming.Readings": "`presupposition_iff_all_of_invariant` and `bounded_invariant_iff` are in "
    "`Becoming.BoundaryWorlds`, so that module does not import the frame (board item W).",
    "Becoming.Standpoints": "`Flow.FedBy` and `Clearing.fedBy_source` are in `Becoming.Continuation`, so the "
    "modules using them do not import the frame (board item W).",
    "Becoming.Runs": "`ExchangeLaw.courseWorld`, `ExchangeLaw.courseWorld_balanced_iff` and `carriedWorld` with "
    "its laws are in `Becoming.Propagation`, so the modules using them do not import the frame (board item W).",
    # Modules that received declarations.
    "Becoming.Labelled": "A third part holds the readings of `Becoming.Recurrence` on runs (a determined "
    "law as a process, reach along runs), moved here unchanged with their names (board item W, second batch).",
    "Becoming.LabelledRoles": "It also holds the readings along runs of `Becoming.Testing` (judging a class, "
    "the finite readings of renewal, and `sees_narrow`, which only they use), moved here unchanged with their names (board item W, second batch).",
}
RECEIVED = "Declarations moved here unchanged, with their names, from {} (board item W): see the sections so headed."
SOURCES = {
    "Becoming.ContextArrivalTraces": "`Becoming.Context`", "Becoming.CounterfactualRuns": "`Becoming.Counterfactual`",
    "Becoming.IdentificationRuns": "`Becoming.Description` and `Becoming.Identification`",
    "Becoming.DiagonalRuns": "`Becoming.Diagonal`", "Becoming.LearningRuns": "`Becoming.Learning`",
    "Becoming.WeightedTraces": "`Becoming.Weighted`", "Becoming.SeekingRuns": "`Becoming.Capture`",
    "Becoming.HorizonWebs": "`Becoming.Horizon`",
    "Becoming.Decidedness": "`Becoming.Likeness`, `Becoming.Joining` and `Becoming.Coverage`",
    "Becoming.FrontierFrames": "`Becoming.Lexical` and `Becoming.Frontier`", "Becoming.BoundaryWorlds": "`Becoming.Readings`",
    "Becoming.Continuation": "`Becoming.Standpoints`", "Becoming.Propagation": "`Becoming.Runs`",
}
for m, s in SOURCES.items():
    NOTES[m] = NOTES.get(m, "") and NOTES[m] + " "
    NOTES[m] += RECEIVED.format(s)


def wrap(text, width=100):
    out, line = [], ""
    for word in text.split():
        if line and len(line) + 1 + len(word) > width:
            out.append(line)
            line = word
        else:
            line = (line + " " + word) if line else word
    out.append(line)
    return "\n".join(out)


package = Path(sys.argv[1])
for m, note in NOTES.items():
    path = package / (m.replace(".", "/") + ".lean")
    text = path.read_text()
    i = text.index("/-!")
    depth, j = 0, i
    while True:
        if text.startswith("/-", j):
            depth += 1
            j += 2
        elif text.startswith("-/", j):
            depth -= 1
            j += 2
            if depth == 0:
                break
        else:
            j += 1
    close = j - 2
    body = text[:close].rstrip()
    para = wrap(note)
    if para in text:
        continue
    path.write_text(body + "\n\n" + para + "\n" + text[close:])
print("notes:", len(NOTES))
