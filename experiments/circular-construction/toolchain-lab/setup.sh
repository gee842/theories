#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"

for executable in uv blender node npm; do
  if ! command -v "$executable" >/dev/null 2>&1; then
    echo "Required executable is missing: $executable" >&2
    exit 1
  fi
done

# This lock is verified on this project's Apple Silicon macOS host.
# A different platform needs a separately resolved and verified OpenSees wheel.
if [[ "$(uname -s)" != "Darwin" || "$(uname -m)" != "arm64" ]]; then
  echo "This environment lock targets macOS arm64." >&2
  exit 1
fi
if [[ ! -x .venv/bin/python ]]; then
  uv venv --python 3.11.2 .venv
fi
uv pip sync requirements.lock --python .venv/bin/python --require-hashes
npm ci --ignore-scripts --no-audit --no-fund
.venv/bin/python verify_toolchain.py
