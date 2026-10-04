"""Exact-state branching, derived from unchanged v1 epoch logic.

The underlying update order is preserved; only initialization and execution bounds
change. Absolute epochs retain the original demand and correction schedules.
"""
from dataclasses import dataclass
import hashlib
from pathlib import Path
import numpy as np
from benchmark import ACTIONS, evaluate, production, choose, candidates, softmax

@dataclass(frozen=True)
class State:
    next_epoch: int
    seeds: np.ndarray
    rubric: np.ndarray
    outputs: np.ndarray
    authority: np.ndarray

    def __post_init__(self):
        for key in ("seeds", "rubric", "outputs", "authority"):
            arr = np.array(getattr(self, key), copy=True)
            arr.setflags(write=False)
            object.__setattr__(self, key, arr)

    def fingerprint(self):
        h = hashlib.sha256(str(self.next_epoch).encode())
        for key in ("seeds", "rubric", "outputs", "authority"):
            arr = getattr(self, key)
            h.update(str((key, arr.shape, arr.dtype.str)).encode())
            h.update(arr.tobytes())
        return h.hexdigest()

    def save(self, path):
        np.savez_compressed(path, next_epoch=self.next_epoch, seeds=self.seeds,
                            rubric=self.rubric, outputs=self.outputs, authority=self.authority,
                            fingerprint=self.fingerprint(), schema_version=1,
                            engine_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())

    @classmethod
    def load(cls, path):
        a = np.load(path)
        if int(a["schema_version"]) != 1:
            raise ValueError("Unsupported snapshot schema")
        if str(a["engine_sha256"]) != hashlib.sha256(Path(__file__).read_bytes()).hexdigest():
            raise ValueError("Snapshot engine version differs")
        state = cls(int(a["next_epoch"]), a["seeds"], a["rubric"], a["outputs"], a["authority"])
        if state.fingerprint() != str(a["fingerprint"]):
            raise ValueError("Snapshot integrity failure")
        return state

def run_segment(cfg, worlds, context, arm, state=None, stop_epoch=None):
    b, n, tmax = cfg["worlds"], cfg["agents"], cfg["epochs"]
    bi = np.arange(b)
    rubric = np.tile(cfg["initial_rubric"], (b, 1))
    # Common neutral initialization: useful effort split evenly.
    initial_action = int(np.flatnonzero(np.all(ACTIONS == [.5, .5, 0.], axis=1))[0])
    outputs = worlds["features"][:, :, initial_action].copy()
    authority = np.full((b, n), 1/n)
    hist = {k: np.zeros((b, tmax)) for k in (
        "gross", "net", "hhi", "presentation", "harmful", "beneficial",
        "amended", "veto", "evidence_valid", "corrected", "delta_governor",
        "delta_value", "pre_governor_share", "admin_cost", "reference_delta_value",
        "reference_delta_governor")}
    hist["governor"] = np.full((b, tmax), -1, dtype=int)
    hist["proposed_option"] = np.full((b, tmax), -1, dtype=int)
    hist["implemented_option"] = np.full((b, tmax), -1, dtype=int)
    hist["shares"] = np.zeros((b, tmax, n))
    hist["appointment_probabilities"] = np.zeros((b, tmax, n))
    hist["frozen_outputs"] = np.zeros((b, tmax, n, 3))
    hist["candidate_values"] = np.full((b, tmax, 8), np.nan)
    hist["candidate_valid"] = np.zeros((b, tmax, 8), dtype=bool)
    hist["before_rubric"] = np.zeros((b, tmax, 3))
    hist["after_rubric"] = np.zeros((b, tmax, 3))
    hist["proposed_rubric"] = np.zeros((b, tmax, 3))
    start_epoch = 0
    if state is not None:
        start_epoch = state.next_epoch
        if not np.array_equal(state.seeds, worlds["seeds"]):
            raise ValueError("Snapshot world identities differ")
        if state.rubric.shape != (b, 3) or state.outputs.shape != (b, n, 3) or state.authority.shape != (b, n):
            raise ValueError("Snapshot dimensions differ from configuration")
        rubric = state.rubric.copy()
        outputs = state.outputs.copy()
        authority = state.authority.copy()
    stop_epoch = tmax if stop_epoch is None else stop_epoch
    if not 0 <= start_epoch < stop_epoch <= tmax:
        raise ValueError("Invalid absolute epoch interval")
    if arm not in ("fixed", "endogenous", "independent", "protected"):
        raise ValueError("Unsupported branch policy")
    if context not in ("stable", "shift"):
        raise ValueError("Unsupported demand context")
    for epoch in range(start_epoch, stop_epoch):
        alpha = .25 if context == "shift" and epoch >= tmax//2 else .75
        hist["before_rubric"][:, epoch] = rubric
        w_rounds, p_rounds = [], []
        for rnd in range(cfg["rounds_per_epoch"]):
            outputs = production(outputs, rubric, alpha, worlds,
                                 worlds["prod"][:, epoch, rnd], cfg)
            p, w, true = evaluate(outputs, rubric, alpha, cfg)
            w_rounds.append(w)
            p_rounds.append(p)
        mean_p = np.mean(p_rounds, axis=0)
        hist["gross"][:, epoch] = np.mean(w_rounds, axis=0)
        hist["shares"][:, epoch] = mean_p
        hist["frozen_outputs"][:, epoch] = outputs
        hist["hhi"][:, epoch] = (mean_p**2).sum(-1)
        hist["presentation"][:, epoch] = rubric[:, 2]
        authority = (1-cfg["authority_memory"])*authority + cfg["authority_memory"]*mean_p
        if arm == "fixed" or epoch == tmax-1:
            hist["after_rubric"][:, epoch] = rubric
            hist["proposed_rubric"][:, epoch] = rubric
            hist["net"][:, epoch] = hist["gross"][:, epoch] - hist["admin_cost"][:, epoch]
            continue
        if arm == "independent":
            appointment_probs = np.full((b, n), 1/n)
            governor = choose(appointment_probs, worlds["appointment"][:, epoch])
        else:
            appointment_probs = authority**cfg["authority_power"]
            appointment_probs /= appointment_probs.sum(-1, keepdims=True)
            governor = choose(appointment_probs, worlds["appointment"][:, epoch])
        hist["appointment_probabilities"][:, epoch] = appointment_probs
        evidence_day = (epoch+1) % cfg["correction_every"] == 0
        proposals, valid = candidates(rubric, alpha, evidence_day, cfg)
        scores = np.einsum("bnd,bkd->bkn", outputs, proposals)
        alt_p = cfg["allocation_floor"]/n + (1-cfg["allocation_floor"])*softmax(
            cfg["score_temperature"]*scores)
        alt_w = (alt_p*true[:, None, :]).sum(-1)
        changed = np.max(np.abs(proposals-rubric[:, None, :]), axis=-1) > cfg["numeric_tolerance"]
        governor_p = alt_p[bi[:, None], np.arange(8)[None, :], governor[:, None]]
        value = governor_p + cfg["common_value_weight"]*alt_w - cfg["amendment_cost"]*changed
        value[~valid] = -np.inf
        hist["candidate_values"][:, epoch] = value
        hist["candidate_valid"][:, epoch] = valid
        picked = choose(softmax(cfg["governance_temperature"]*value), worlds["amendment"][:, epoch])
        hist["proposed_option"][:, epoch] = picked
        hist["proposed_rubric"][:, epoch] = proposals[bi, picked]
        valid_evidence = evidence_day & ((alt_w[:, 7]-alt_w[:, 0]) > cfg["evidence_threshold"])
        veto = np.zeros(b, dtype=bool)
        if arm == "protected":
            veto = alt_w[bi, picked] < alt_w[:, 0]-cfg["numeric_tolerance"]
            picked[veto] = 0
            picked[valid_evidence] = 7
        next_rubric = proposals[bi, picked].copy()
        # Only tiny floating-point residuals are removed, never substantive invalid weights.
        next_rubric[np.abs(next_rubric) < cfg["numeric_tolerance"]] = 0
        adopted = changed[bi, picked]
        dp = governor_p[bi, picked]-governor_p[:, 0]
        dw = alt_w[bi, picked]-alt_w[:, 0]
        tol = cfg["numeric_tolerance"]
        hist["governor"][:, epoch] = governor
        hist["implemented_option"][:, epoch] = picked
        hist["reference_delta_value"][:, epoch] = alt_w[:, 7]-alt_w[:, 0]
        hist["reference_delta_governor"][:, epoch] = governor_p[:, 7]-governor_p[:, 0]
        hist["pre_governor_share"][:, epoch] = p[bi, governor]
        hist["amended"][:, epoch] = adopted
        hist["veto"][:, epoch] = veto
        hist["delta_governor"][:, epoch] = dp
        hist["delta_value"][:, epoch] = dw
        hist["harmful"][:, epoch] = adopted & (dp > tol) & (dw < -tol)
        hist["beneficial"][:, epoch] = adopted & (dw > tol)
        hist["evidence_valid"][:, epoch] = valid_evidence
        hist["corrected"][:, epoch] = valid_evidence & (alt_w[bi, picked] >= alt_w[:, 7]-tol)
        hist["admin_cost"][:, epoch] = cfg["amendment_cost"]*adopted + cfg["audit_cost"]*(arm == "protected")
        hist["net"][:, epoch] = hist["gross"][:, epoch]-hist["admin_cost"][:, epoch]
        hist["after_rubric"][:, epoch] = next_rubric
        rubric = next_rubric
    return hist, State(stop_epoch, worlds["seeds"], rubric, outputs, authority)
