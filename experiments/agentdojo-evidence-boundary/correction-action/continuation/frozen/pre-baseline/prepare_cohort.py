"""Prepare the fixed cohort; do not execute a controller or dispatch a worker."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile

HERE = Path(__file__).resolve().parent


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def save(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n")


def main():
    manifest_path = HERE / "case-manifest.json"
    if manifest_path.exists() or (HERE / "preparations").exists():
        raise RuntimeError("Refusing to overwrite an existing cohort preparation")
    specification = json.loads((HERE / "COHORT.json").read_text())
    base = Path(tempfile.mkdtemp(prefix="codex-audit-continuation-")).resolve()
    record = {"schema_version": 1, "status": "preparation_in_progress_no_participants",
              "temporary_base": str(base), "cohort_sha256": sha(HERE / "COHORT.json"),
              "preparer_sha256": sha(Path(__file__)), "episodes": []}
    save(manifest_path, record)
    for episode in specification["episodes"]:
        case = base / episode["id"]
        process = subprocess.run([sys.executable, "-B", str(HERE / "broker.py"), "prepare",
                                  "--case-dir", str(case), "--branch", episode["branch"]],
                                 capture_output=True, text=True)
        directory = HERE / "preparations"
        directory.mkdir(exist_ok=True)
        (directory / (episode["id"] + ".stdout.txt")).write_text(process.stdout)
        (directory / (episode["id"] + ".stderr.txt")).write_text(process.stderr)
        if process.returncode:
            record["status"] = "preparation_failed_preserved"
            record["failed_episode"] = episode["id"]
            save(manifest_path, record)
            raise RuntimeError(f"Preparation failed: {episode['id']}; original outputs preserved")
        response = json.loads(process.stdout)
        prepared = {**episode, "case_dir": str(case), "preparation": response["preparation"],
                    "initial_observation": response["initial_observation"]}
        prompt = (HERE / "TASK.txt").read_text() + "\nInitial interface observation:\n" + json.dumps(
            response["initial_observation"], indent=2, ensure_ascii=False) + "\n"
        prompt_path = HERE / "prompts" / (episode["id"] + ".txt")
        prompt_path.parent.mkdir(exist_ok=True)
        prompt_path.write_text(prompt)
        prepared["prompt"] = {"path": str(prompt_path.relative_to(HERE)), "sha256": sha(prompt_path),
                              "bytes": prompt_path.stat().st_size}
        record["episodes"].append(prepared)
        save(manifest_path, record)
    assert len({item["prompt"]["sha256"] for item in record["episodes"]}) == 1, "Unequal initial information"
    record["status"] = "prepared_no_controller_or_learned_execution"
    save(manifest_path, record)
    print(json.dumps({"status": record["status"], "episodes": len(record["episodes"]),
                      "temporary_base": str(base), "manifest_sha256": sha(manifest_path),
                      "all_initial_prompts_byte_identical": True}, indent=2))


if __name__ == "__main__":
    main()
