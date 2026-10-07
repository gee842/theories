#!/bin/sh
set -eu
study_dir=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
build_dir=$(mktemp -d "${TMPDIR:-/tmp}/perspectival-lean.XXXXXX")
trap 'rm -rf "$build_dir"' EXIT HUP INT TERM
cd "$study_dir"
lean --version
lean -o "$build_dir/TrajectoryFidelity.olean" TrajectoryFidelity.lean
LEAN_PATH="$build_dir" lean Audit.lean
shasum -a 256 TrajectoryFidelity.lean Audit.lean
