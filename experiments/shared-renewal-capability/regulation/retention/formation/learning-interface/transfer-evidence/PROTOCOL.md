# Paid evidence at a later concern decision

6 October 2026. AI-authored protocol, specified before executable results.

This study supplies a finite reliability interface from the [existing paid
prediction process](../README.md) to the concern model's pathwise choice
condition. It does not build a new correspondence assay: `g=z=1` remain
supplied, as do shared evaluation routing, perfect action efficacy, and the
meaning of the recipient's adverse state. The earlier
[adaptive-evidence branch](../../../../../../integrated-correction/general-framework/reproduction-test/adaptive-evidence/FORMAL.md)
already develops accumulation, certificates and reversal limitations. The new
composition is with the actual paid teacher histories and a later recipient
action, rather than a claim to invent those statistical methods.

## Existing physical law and added finite memory

Use `model.py` in the parent directory without modifying it. A paid observation
prepays two common-fuel units, receives two units from a finite counted source
on a zero target and none on a one target, and writes the observed net loss
divided by two. The primary target law is stationary Bernoulli with parameter
`beta`. Initial source is `2T`; every successor carries its actual remaining
fuel and source. There are at most `T` opportunities. Below two common units,
no observation or write occurs. Decay is zero in these comparisons.

The existing gain-one-quarter estimate is compared with a new supplied counter
updater storing the number `n` of paid observations and their sum `s`. Each
counter has capacity `0..T`, requiring `ceil(log2(T+1))` bits. Confidence-budget
and routing records, and a finite preinstalled certificate table, are additional
supplied apparatus. The common declared operation/write/computation price of
two units is assumed sufficient for either finite circuit through this horizon.
It pays every acquired update; this does not derive memory construction,
maintenance, a size-independent physical price, or unlimited storage. Both
comparators have exactly the same acquired outcomes, funding and action bill.

## Single-stream certificate

For `n>=1`, set `d_n` to the largest power of two no greater than `n`,
`D_n={k/d_n : 0<=k<=d_n}`, and `alpha_n=alpha/[n(n+1)]`. Define

`tail(n,q,s) = sum_{j=s}^n binom(n,j) q^j (1-q)^(n-j)`

and `L(n,s)` as the greatest grid candidate whose tail is at most `alpha_n`,
or zero if no candidate passes. At `n=0`, set `L=0`. Exact rational arithmetic
is used throughout. This is one unknown stream, so its entire budget is
`alpha`; a three-unknown-stream construction would have to split that budget.
Stopping after resource loss does not reset the paid-observation index or its
confidence budget. Stationarity and calibration remain conditions of coverage.

## Separate next action

After all acquired evidence, a new terminal recipient state has adverse outcome
four. With `g=z=1, b=0, H=4, a=1`, the strict preference threshold is `w>1/4`.
Three supplied policies substitute the actual retained EWMA, `s/n` (zero before
observation), or `L(n,s)` respectively. A tie selects Wait. Protect additionally
requires one currently available common unit, spends it before any return, and
sets the recipient outcome to zero. Wait spends nothing and leaves outcome
four. There are no terminal returns. Evidence cannot retroactively protect any
earlier outcome.

Report strict preference and delivered action separately. A false certificate
means a claimed lower bound exceeds the true stationary `beta`; false threshold
certification concerns `beta*H<=a`. It does not mean Protect harms this recipient:
the supplied terminal efficacy is one. Training shortfalls remain counted
separately and are not erased by this later protective action.

## Prespecified cases and checks

Use `alpha=1/10`, `T=16`, and the following five cases:

- `beta=1/2, F0=33`: every update and the later action bill can be funded.
- `beta=1/2, F0=16`: acquisition stops at the eighth loss with no action reserve.
- `beta=1/2, F0=17`: the same stop leaves one unit for a later action.
- `beta=1/4, F0=33`: a full-support boundary model permits rare false certification.
- `beta=1/8, F0=3`: the first loss stops acquisition but leaves the action bill.
  Raw-count preference occurs exactly when that first loss arrives before the
  fourth observation, with probability `1-(7/8)^3`; the EWMA has only one loss
  and never strictly exceeds one quarter, and the certificate never passes.

A count/resource-state dynamic program must reuse the parent transition
function. EWMA threshold probabilities are reconstructed by exact weighted
subset counting, with bounds that avoid enumerating all outcome words. Check
all resource and terminal-action ledgers, total probability, counter capacity,
fixed-sample and stopped anytime false-certificate mass, and ties.

Two further negative witnesses retain actual paid histories. Sixteen one
targets followed by five zero targets, with fuel 43 and source 42, can all be
paid and still leave a terminal bill. Five zero targets reduce any previous
EWMA in `[0,1]` to at most `243/1024<1/4`. If the law switches to `beta=0` after
the sixteenth sample, accumulated evidence can remain above the threshold;
stationary confidence guarantees do not survive that switch. A finite
all-one history has positive probability even under `beta=1/4`, so a positive
finite certificate is not a zero-error identification of the model.

These checks do not execute infinitely many paid observations or prove durable
concern from a finite source. Infinite confidence and learning claims require
their own support, stationarity and memory conditions.
