# Replacement and recurrent correction research record

This cycle executes the next target requested after the first structural-foundations study. It tests replacement of a correction interface, scaling with shared diagnostic capacity, and recurrent paid repair whose success restores the production funding later repairs.

Start with the [synthesis](synthesis.md). The main exact findings are:

- Hiding a cheap diagnostic raises robust correction reserve from three to four while preserving the plant graph and current output. A known invertible recoding preserves capacity.
- `n` independent hidden-fault modules with `k` parallel diagnostic channels need `ceil(n/k)+2` slots under the supplied three-stage protocol.
- A recurring route must finance each repair, finish in time, survive long quiet intervals, and replenish repair expense before the earliest next fault.
- In the base adaptive game, ready apparatus needs six initial units; absent apparatus needs sixteen, because two repairs can occur before the first replenishment. Another parameter regime favors suspension and rebuilding over permanent standby.

The universality claim supported here is conditional: the same proved constraint applies throughout its specified model class and under transformations that preserve its relevant structure. Empirical universality across real domains remains a hypothesis with explicit transfer tests.

## Proofs and source record

- [Modular replacement](modular-replacement.md): interface equivalence, graph-matched counterexample, feedback timing, and unit changes.
- [Scale and deadlines](scale-and-deadline.md): exact scheduling frontier and scope.
- [Recurrent model and proofs](recurrent-repair.md) and [exact results](verification/recurrent-repair-results.json): parameters, minimum initial credits, fixed-point checks, traces, and witness locations.
- [Universality and primary sources](universality-and-sources.md): invariants, failed abstractions, empirical tests, and four new source groups.
- [Claim register](CLAIMS.md): evidential status and failure conditions.

## Reproducibility

The three verification programs use Python's standard library. From this directory:

```text
python3 verification/check_modular_replacement.py
python3 verification/check_scale_deadline.py
python3 verification/check_recurrent_repair.py
```

Each program writes its results beside itself. The recurrent checker additionally saves a tabular route frontier and complete winning-region policy witnesses. Its finite graph and safety fixed point give an infinite guarantee for the declared duty; illustrative traces are not the proof. Code cross-checks share parts of the model and therefore do not independently validate the supplied causal assumptions.

All three checkers passed the coordinator's final rerun. Coverage includes 105 modular capacity cases and 45,960 paired action words; 36 scale frontiers and 468 deadline comparisons; and 33 selected recurrent games, six cap-versus-credit cases, 40 route-frontier points under both prescribed routes, and 3,630 bounded policy-tree comparisons. General parameter claims rely on the written proofs, not on these finite counts alone.

Current output, physical reachability, full-information controllability, and observation-based controllability are separate comparisons. Apparatus readiness and storage cap are also distinct from initial cash. The reports keep these differences explicit.

## Continuity

The [first-cycle synthesis](../synthesis.md) and [original next-target protocol](../next-research-target.md) remain available. This cycle supplies controlled mathematical constructions and exact finite-game calculations, not empirical institutional or AI results. No parent research files were modified. The next unresolved target is paid evidence retention and controller succession within the recurrent loop; it is described at the end of the synthesis.
