# Exact checks of action-dependent continuations

6 October 2026. This supports the existing [settlement study](../../../_process/research/2026-10-05-revisable-concern/settlement/README.md), specifically **continued protection when present action changes future opportunities or power**. These are authored mathematical examples, not new observations, a learned-agent benchmark or a full extension of the settlement's strategic economy.

The [mathematical note](../../../_process/research/2026-10-05-revisable-concern/settlement/formal/ENDOGENOUS-CONTINUATION-MATH.md) states the general conditional verification results. The [independent review](../../../_process/research/2026-10-05-revisable-concern/settlement/formal/ENDOGENOUS-CONTINUATION-REVIEW.md) and [source/identification audit](../../../_process/research/2026-10-05-revisable-concern/settlement/formal/ENDOGENOUS-CONTINUATION-EVIDENCE.md) distinguish standard mathematics, finite checks and application premises.

## What is checked

[Fixtures](fixtures.json) specify three finite processes and a separate two-stage game. The [checker](check_continuations.py) uses exact rational Gaussian elimination to evaluate every deterministic stationary policy. It then checks every action at every state against those values, including unreachable states under the candidate policy. A separate comparison verifies that the accepted policy values dominate all enumerated stationary alternatives. Closed-form expressions independently check the stated examples. The general history-dependent optimality argument belongs to the written proof, not this enumeration.

Seven process/discount cases evaluate sixteen stationary policies. Every check passes. The primary two examples retain an actual cash order: opening reserve, paid cost, external gross receipt, distribution to the operator and closing reserve. Each permitted action restores reserve two after its explicitly supplied receipt and dividend. This is a finite financial transition law; it does not derive the physical production of continuing external supplies.

| Supplied opportunity law | Discount | Protection candidate's advantage at its initial comparison | Result |
|---|---:|---:|---|
| Harmful intervention opens a higher future receipt | 1/5 | 1/4 | Protection strictly optimal |
| Same law | 1/4 | 0 | Protection and intervention tie |
| Same law | 1/2 | −2 | Protection candidate fails; intervention policy verified |
| Protection opens the better future receipt | 1/5 | −1/4 | Protection candidate fails |
| Same law | 1/4 | 0 | Tie |
| Same law | 1/2 | 2 | Protection strictly optimal |

For the first law, the comparison is against one deviation followed by the candidate policy. The checker separately evaluates the alternative policy, so it does not confuse that local comparison with the value of an arbitrary multistep deviation. The two scenarios deliberately have different transition laws. They illustrate two possible directions of a horizon change; they do not estimate which law occurs in a population or claim global monotonicity in a general game.

The third process demonstrates why checking only a protective path is insufficient: its candidate passes at the realized state but fails at a reachable off-path state. A two-step deviation has value five against the candidate's two. The checker also rejects a fabricated continuation value and omission of that off-path state.

The separate two-stage game illustrates credibility. Respect is optimal against a stipulated punishment, but the trustee would prefer tolerance after an attack. Backward induction then selects attack followed by tolerance. Its payoff table does not implement a real punishment, commitment technology or institution.

## Reproduction and scope

Run from the repository root with Python's standard library:

```sh
python experiments/integrated-correction/endogenous-continuation/check_continuations.py
```

[Results](results.json) record every policy, value, residual and applicable cash prefix, with hashes of the exact fixtures and checker. Rerunning writes the same deterministic result file; repeated runs are not independent evidence. No original settlement model or previously accepted result was changed.

Positive grounds, patient identity and benefit, sound evidence, authority, objective interpretation, feasible alternatives, future production and the opportunity transition law remain supplied. The operator-only examples do not establish the complete-profile equilibrium certificate for an extended R2 economy. They substantiate the numerical illustrations and expose false verification shortcuts; they neither derive concern nor complete alignment.
