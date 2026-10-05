# Joint capability from a physical event law

AI-assisted mathematical experiment, 5 October 2026. This evaluates the existing finite-material shared-renewal process, with all event rates and energy spending retained. It is a calculation for a stipulated model, not an empirical study.

**New extension:** the [constructed-regulation comparison](regulation/README.md) adds a fuel-responsive inhibitor and pays its formation, binding and wear costs. It starts with no regulator and uses stronger source conditions. Its negative outcomes are preserved separately; the earlier protocol and interval results below are unchanged.

Read the [mathematical bridge](../../_process/research/2026-10-05-support-and-shared-generativity/completion/JOINT-CAPABILITY-BRIDGE.md) for the proof, assumptions and interpretation. The [protocol](PROTOCOL.md) was recorded before results; [certify.py](certify.py) uses only the Python standard library and writes [results.json](results.json).

At the prespecified horizon H=0.25 and reliability 0.5, increasing the supplied Y recycling coefficient from zero to four produces incomparable installed capability sets:

| Test, jointly with continued activity | Coefficient 0 | Coefficient 4 |
|---|---:|---:|
| At least one recycling event | 0.210619412 | 0.659720172 |
| At least one reserve packet left | 0.646107828 | 0.344331591 |
| Recycling and resident assembly both occur | 0.024095030 | 0.086651916 |
| Both conversions occur and a packet remains | 0.006683438 | 0.021045556 |

The displayed decimals summarize enclosing intervals in the results. The first two rows cross the common reliability threshold in opposite directions. The second two retain a substantive positive joint-construction effect below that threshold. All declared horizons and all eight profiles are reported, not only these rows.

The calculation includes energy-overflow uncertainty and the uniformization remainder, using directed decimal arithmetic. It does not silently drop transitions at the truncation boundary. The maximum overflow bound across declared cases is below 1.7e-17; the omitted Poisson mass is at most 1e-22 in each case.

Run `python3 certify.py` in this directory to reproduce the primary calculation. The [independent checker](independent_check.py) reconstructs the generator without importing the producer; its [result](independent-check.json) compares all 48 probabilities and checks exact integer accounting across 1,000 physical states. It agrees to within 2.78e-15, under a disclosed 1e-11 comparison tolerance. Its floating calculation is a cross-check; the rigorous enclosure relies on the separate directed-arithmetic argument. Read the [review](../../_process/research/2026-10-05-support-and-shared-generativity/completion/ASSAY-REVIEW.md) for scope. Re-running either script overwrites its results and timing/provenance fields.

The primary interval implementation is certified for the six declared cases, whose uniformization-rate times horizon products are exactly representable. Generalizing to arbitrary inputs requires enclosing that product as well. Every assembly-required profile remains below reliability 0.5 at H=0.25; the crossing witness compares delivered recycling with retained reserve readiness, not two separately delivered productive functions.

The protocol class here contains the autonomous run only. Its region is exact for that installed process and an inner bound for a broader controller class. These results neither prove global physical impossibility nor explain the formation of the compared catalyst. They make the next question sharper: which funded physical regulation can manage the tradeoff, and under what conditions does that regulation actually arise?

The fixed numerical source g=1 gives reduced work-equivalent drift -F-Y, so this specimen does not test ample-support persistent operation. The mathematical report separately shows that the opposed leading short-time tails persist for any fixed finite capture coefficient. The computed alpha=0.5 crossing remains specific to the declared source and horizons.
