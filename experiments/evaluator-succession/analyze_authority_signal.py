"""Exploratory exact enumeration of governance at archived v2 states.

No new outcome worlds, parameter fits, or trajectory interventions. Evaluate
every possible governor's actual finite logit menu at epochs 80 and 99, using
states reached by the endogenous continuation from both source histories in
both demand contexts. The first date is the common branch boundary; the second
is the first postfork correction date. Outcomes are frozen-submission changes,
not future welfare. All analytic comparisons are conditional on the SAME state.
"""
from pathlib import Path
import hashlib
import json
import numpy as np
import benchmark as base

ROOT = Path(__file__).resolve().parent
ARCHIVE = ROOT / "results-v2"
OUT = ROOT / "diagnostics-authority-signal"


def compute(outputs, rubric, authority, alpha, epoch, cfg):
    b, n = authority.shape
    proposals, valid = base.candidates(
        rubric, alpha, (epoch + 1) % cfg["correction_every"] == 0, cfg)
    scores = np.einsum("bnd,bkd->bkn", outputs, proposals)
    shares = cfg["allocation_floor"] / n + (1-cfg["allocation_floor"]) * base.softmax(
        cfg["score_temperature"] * scores)
    useful = alpha * outputs[..., 0] + (1-alpha) * outputs[..., 1]
    welfare = (shares * useful[:, None, :]).sum(-1)
    changed = np.max(abs(proposals-rubric[:, None, :]), axis=-1) > cfg["numeric_tolerance"]
    costs = cfg["amendment_cost"] * changed
    values = shares.transpose(0, 2, 1) + (
        cfg["common_value_weight"] * welfare - costs)[:, None, :]
    values = np.where(valid[:, None, :], values, -np.inf)
    choices = base.softmax(cfg["governance_temperature"] * values)
    dw = welfare - welfare[:, :1]
    effects = (choices * dw[:, None, :]).sum(-1)
    beta = cfg["authority_power"]
    probabilities = base.softmax(beta * np.log(authority))
    endogenous = (probabilities * effects).sum(-1)
    uniform = effects.mean(-1)
    covariance = ((n * probabilities - 1) * (effects-uniform[:, None])).mean(-1)
    log_a = np.log(authority)
    derivative = (probabilities * (effects-endogenous[:, None]) * (
        log_a-(probabilities*log_a).sum(-1, keepdims=True))).sum(-1)
    eps = 1e-5
    numeric_derivative = (((base.softmax((beta+eps)*log_a) -
                           base.softmax((beta-eps)*log_a)) * effects).sum(-1)/(2*eps))
    dp = shares - shares[:, :1, :]
    avg_utility_change = (dp + (
        cfg["common_value_weight"] * dw - costs)[:, :, None]).mean(-1)
    expected_uniform_utility = cfg["common_value_weight"] * dw - costs
    # Removing private share ONLY from governance makes every governor identical.
    common_values = np.where(valid, cfg["common_value_weight"]*welfare-costs, -np.inf)
    common_choices = base.softmax(cfg["governance_temperature"]*common_values)
    common_effect = (common_choices*dw).sum(-1)
    common_weighted = (probabilities*common_effect[:, None]).sum(-1)
    # Average all n cyclic assignments of the exact same appointment weights.
    # This preserves the probability spectrum/HHI, averages each weight onto each identity.
    permuted = np.stack([(np.roll(probabilities, shift, axis=1)*effects).sum(-1)
                         for shift in range(n)]).mean(0)
    errors = {
        "mixture_covariance": float(abs(endogenous-uniform-covariance).max()),
        "concentration_derivative": float(abs(derivative-numeric_derivative).max()),
        "uniform_utility_cancellation": float(abs(avg_utility_change-expected_uniform_utility).max()),
        "common_interest_appointment_null": float(abs(common_weighted-common_effect).max()),
        "identity_permutation_mean": float(abs(permuted-uniform).max()),
    }
    for key, error in errors.items():
        assert error < (1e-8 if key == "concentration_derivative" else 1e-12), (key,error)
    qualifies = ((epoch+1) % cfg["correction_every"] == 0) & (dw[:,7] > cfg["evidence_threshold"])
    # 'corrected' matches the archive: qualifies AND chosen outcome at least reference W.
    corrective = (choices * (welfare[:,None,:] >=
                  welfare[:,None,7:8]-cfg["numeric_tolerance"])).sum(-1)
    reference_success = np.where(qualifies[:,None],corrective,0.)
    return dict(values=values, probabilities=probabilities, effects=effects,
                endogenous=endogenous, uniform=uniform, covariance=covariance,
                derivative=derivative, errors=errors, qualifies=qualifies,
                expected_correction_endogenous=(probabilities*reference_success).sum(-1),
                expected_correction_uniform=reference_success.mean(-1))


def main():
    manifest=json.loads((ARCHIVE/"input_manifest.json").read_text())
    cfg=manifest["effective_config"]
    for name,digest in manifest["inputs"].items():
        assert hashlib.sha256((ROOT/name).read_bytes()).hexdigest()==digest
    report=dict(kind="Exploratory frozen-state exact enumeration; no new outcome worlds",
                created_at=base.now(), input_manifest_sha256=base.digest(ARCHIVE/"input_manifest.json"),
                script_sha256=base.digest(Path(__file__)), samples={}, checks={})
    OUT.mkdir(exist_ok=True)
    for source in ("endogenous","independent"):
        snapshot=np.load(ARCHIVE/f"checkpoint-{source}.npz")
        for context in ("stable","shift"):
            history_path=ARCHIVE/f"branch-{source}-{context}-endogenous.npz"
            h=np.load(history_path)
            authority=snapshot["authority"].copy()
            for epoch in range(80,100):
                authority=(1-cfg["authority_memory"])*authority+cfg["authority_memory"]*h["shares"][:,epoch]
                if epoch not in (80,99):
                    continue
                result=compute(h["frozen_outputs"][:,epoch],h["before_rubric"][:,epoch],
                               authority,.25 if context=="shift" else .75,epoch,cfg)
                np.testing.assert_allclose(result["probabilities"],h["appointment_probabilities"][:,epoch],atol=1e-14,rtol=0)
                actual_values=result["values"][np.arange(cfg["worlds"]),h["governor"][:,epoch]]
                np.testing.assert_allclose(actual_values,h["candidate_values"][:,epoch],atol=1e-14,rtol=0)
                if epoch==80:
                    independent=np.load(ARCHIVE/f"branch-{source}-{context}-independent.npz")
                    for key in ("frozen_outputs","before_rubric","shares"):
                        np.testing.assert_array_equal(h[key][:,epoch],independent[key][:,epoch])
                key=f"{source}/{context}/{epoch}"
                report["checks"][key]=result["errors"]
                report["samples"][key]=dict(
                    history_sha256=base.digest(history_path),
                    endogenous_mean=float(result["endogenous"].mean()),
                    uniform_mean=float(result["uniform"].mean()),
                    endogenous_minus_uniform_mean=float(result["covariance"].mean()),
                    derivative_at_power2_mean=float(result["derivative"].mean()),
                    negative_covariance_worlds=int((result["covariance"]<0).sum()),
                    correction_opportunity_worlds=int(result["qualifies"].sum()),
                    expected_corrections_endogenous=float(result["expected_correction_endogenous"].sum()),
                    expected_corrections_uniform=float(result["expected_correction_uniform"].sum()))
                np.savez_compressed(OUT/f"{source}-{context}-{epoch}.npz",
                    **{k:v for k,v in result.items() if k not in ("values","errors")},
                    seeds=snapshot["seeds"])
    (OUT/"analysis.json").write_text(json.dumps(report,indent=2)+"\n")
    for key,row in report["samples"].items():
        print(key, {k:round(row[k],7) for k in (
            "endogenous_mean","uniform_mean","endogenous_minus_uniform_mean",
            "derivative_at_power2_mean")},"negative worlds",row["negative_covariance_worlds"])
    print("All identities and archived governor menus verified.")


if __name__=="__main__":
    main()
