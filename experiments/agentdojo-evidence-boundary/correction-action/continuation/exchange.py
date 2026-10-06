"""Parent transport only: preserve a worker reply, broker response and follow-up.

Added after dispatch freeze; it changes no broker/policy/scoring logic. The parent
supplies a verbatim worker reply file. No collaboration call is made here.
"""
import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import subprocess
import sys

HERE = Path(__file__).resolve().parent


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--episode", required=True, choices=["w01", "w02"])
    parser.add_argument("--reply", required=True, type=Path)
    args = parser.parse_args()
    for relative, record in json.loads((HERE / "DISPATCH-FREEZE.json").read_text())["files"].items():
        assert sha(HERE / relative) == record["sha256"], relative
    case = next(x for x in json.loads((HERE / "case-manifest.json").read_text())["episodes"] if x["id"] == args.episode)
    state = json.loads((Path(case["case_dir"]) / "state.json").read_text())
    assert not state["finished"] and state["attempts"] < 16
    number = state["attempts"] + 1
    directory = HERE / "transcripts" / args.episode
    directory.mkdir(parents=True, exist_ok=True)
    stem = directory / f"{number:02d}"
    raw = stem.with_suffix(".reply.txt")
    assert not raw.exists()
    raw.write_bytes(args.reply.read_bytes())
    p = subprocess.run([sys.executable, "-B", str(HERE / "broker.py"), "request", "--case-dir", case["case_dir"], "--json-file", str(raw)], capture_output=True)
    stem.with_suffix(".response.json").write_bytes(p.stdout)
    stem.with_suffix(".stderr.txt").write_bytes(p.stderr)
    assert p.returncode == 0, "Broker failure preserved; do not substitute a fabricated response"
    response = json.loads(p.stdout)
    followup = (HERE / "CONTINUE.txt").read_text() + "\n" + p.stdout.decode()
    stem.with_suffix(".followup.txt").write_text(followup)
    stem.with_suffix(".transport.json").write_text(json.dumps({"recorded_at_utc": datetime.now(timezone.utc).isoformat(), "helper_sha256": sha(Path(__file__)), "reply_sha256": sha(raw), "response_sha256": hashlib.sha256(p.stdout).hexdigest(), "followup_sha256": sha(stem.with_suffix('.followup.txt')), "broker_returncode": p.returncode, "request_number": number}, indent=2) + "\n")
    print(followup, end="")


if __name__ == "__main__":
    main()
