"""Supporting boundary audit; not the route-revision implementation or its acceptance."""
from pathlib import Path
import hashlib
import importlib.util
import json
import sys
sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parents[4]
BASE = ROOT / "experiments/shared-renewal-capability/regulation/retention/formation/selectors/updaters/prediction/recipient-correction"
MON = BASE / "route-diagnostics/monitor"
REV = BASE / "route-diagnostics/revision"
HERE = Path(__file__).resolve().parent

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def payment_path(grant):
    """Independent prescribed TARGET011 cash path, no hidden state or policy claim."""
    stock = 11 + grant
    spent = lost = 0
    trace = []
    def pay(fee, tag):
        nonlocal stock, spent
        if stock < fee + 1:
            trace.append(dict(stage=tag, paid=False, stock=stock))
            return False
        stock -= fee
        spent += fee
        trace.append(dict(stage=tag, paid=True, stock=stock))
        return True
    for tag in ("head_assembly", "evidence_read", "swap"):
        if not pay(1, tag):
            return dict(completed=False, stopped=tag, stock=stock, trace=trace)
    for i, capture in enumerate((False, True, True)):
        for stage, fee in (("rent", 1), ("sense", 1), ("work", 3), ("acquire", 1), ("write", 1)):
            tag = f"probe{i+1}:{stage}"
            if not pay(fee, tag):
                return dict(completed=False, stopped=tag, stock=stock, trace=trace)
            if stage == "work":
                stock += 10 if capture else 0
                lost += 0 if capture else 10
                trace.append(dict(stage=f"probe{i+1}:return", capture=capture, stock=stock))
    # Seed is a transfer; the prescribed child spends all five at rent/sense/work.
    for tag, fee in (("donor", 1), ("own_use", 1), ("read", 1), ("assemble", 1), ("write", 1), ("seed", 5)):
        if not pay(fee, "copy:" + tag):
            return dict(completed=False, stopped="copy:"+tag, stock=stock, trace=trace)
    stock += 10
    assert pay(1, "copy:hold")
    assert 11 + grant + 40 == stock + spent + lost
    return dict(completed=True, stopped=None, stock=stock, spent=spent, lost=lost, trace=trace)

def main():
    accepted = json.loads((MON / "verification.json").read_text())
    assert accepted["status"] == "passed"
    for name, digest in accepted["source_sha256"].items():
        assert sha(ROOT / name) == digest, name
    paths = [MON/"verification.json", MON/"model.py", MON/"HANDOFF.md", REV/"PROTOCOL.md",
             REV/"PROSPECTIVE-CLARIFICATIONS.md", REV/"protocol-freeze.json", Path(__file__)]
    hashes = {str(p.relative_to(ROOT)): sha(p) for p in paths}
    spec = importlib.util.spec_from_file_location("_revision_boundary_monitor", MON/"model.py")
    monitor = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(monitor)
    witnesses = {}
    expected = {"target": (1, "unresolved"), "closed": (3, "nonwriter"),
                "frozen": (3, "nonwriter"), "controlled_proxy": (1, "private_zero")}
    for label, (code, diagnosis) in expected.items():
        ref = accepted["witnesses"][label]
        case_name, entry_id = ref.split("/")
        case = dict(accepted["cases"][case_name], frames=1)
        state = monitor.run(accepted["entries"][entry_id]["entry"], case)["state"]
        assert (state["recipient"], state["new_source"], state["child_cash"]) == (11, 10, 0)
        assert (state["q"], state["diagnosis"]) == (code, diagnosis)
        assert all(state[k] for k in ("binding", "post_read_done", "write_done"))
        assert state["stage"] == "episode_complete"
        fields = ("recipient", "q", "gamma", "new_source", "child_cash", "success_summary",
                  "failure_summary", "binding", "post_read_done", "write_done", "stage", "diagnosis")
        witnesses[label] = dict(accepted_two_frame_reference=ref,
            evaluated_intervention="same accepted entry and case with frames=1",
            projection={k: state[k] for k in fields})
    paths_checked = {str(g): payment_path(g) for g in range(21)}
    for g, state in paths_checked.items():
        assert state["completed"] == (int(g) >= 5)
    assert paths_checked["4"]["stopped"] == "probe2:work"
    assert paths_checked["4"]["stock"] == 3
    assert paths_checked["5"]["stock"] == 11
    assert paths_checked["5"]["spent"] == 35
    assert paths_checked["5"]["lost"] == 10
    for name, digest in hashes.items():
        assert sha(ROOT / name) == digest, name
    result = dict(status="passed", scope="Four representative prefix replays and 21 independently specified cash paths; no revision policy or full-mixture acceptance.",
                  source_sha256=hashes, accepted_monitor_hashes_checked=len(accepted["source_sha256"]),
                  representative_prefixes=witnesses, proposed_target_payment_paths=paths_checked,
                  caveat="First-frame replay is not a saved two-frame endpoint. The dedicated handoff export and revision implementation require their own checks.")
    (HERE / "SUCCESSOR-ROUTE-REVISION-BOUNDARY-CHECK.json").write_text(json.dumps(result, indent=2)+"\n")
    print("Passed: four actual-entry first-frame projections; 21 independent candidate payment paths; frozen source hashes unchanged.")

if __name__ == "__main__":
    main()
