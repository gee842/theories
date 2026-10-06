# Current-source revalidation of the original inquiry package

The [current receipt](verification.json) records a fresh Lean 4.29.1 build of exactly `GenerativeCore`, `Depletion`, `GenerativeClosure` and `InquiryFamilies`: 27 package declaration audits and 23 inherited declaration audits. The first run passed on 6 October 2026. This is a revalidation of existing results, not a new theorem or a validation of the later core/tree and sufficiency packages.

The [historical receipt](../verification.json) and its logs remain unchanged. Its `Depletion` source hash differs from the current source because that module's proof bodies changed; the five audited theorem statements and names were retained. The fresh build's five `Depletion` axiom reports are empty. The standard dependencies still reported elsewhere are recorded per declaration in the new logs.

Run `python3 -B check.py` from this directory. The wrapper freezes four source files, the original checker and its toolchain pin. It copies their parent/package layout to a temporary directory and executes the original checker unchanged there; that checker creates a second fresh temporary build. No shared compiled artifacts or historical receipts are overwritten. The installed compiler must match the historical pinned binary; no toolchain is installed. `Std` and its transitive dependencies come from that installed distribution and are not rebuilt here.

Each run saves its six snapshots, original checker receipt, original stdout, four compiler logs and an independent receipt under `runs/<UTC>/`. `verification.json` is a byte-identical copy of that run's receipt. The wrapper independently checks exact qualified audit names, counts, source and output hashes, axiom limits, warnings, and preservation of live inputs, historical files and compiler bytes. Failed runs are retained and exit nonzero.

Receipt `inputs`, `snapshots` keys and `preserved_historical` keys are repository-relative source paths. Snapshot values, artifact paths, module output paths and `run_record` are relative to this directory. Module source paths are repository-relative. `compiler_binary` is an absolute installed path. `fresh_build` preserves the original checker receipt; its paths refer to the copied original layout, and its exact saved bytes are at `runs/<UTC>/original-checker-verification.json`.

This run verifies the explicit conditional mathematical package. It does not prove empirical or ethical premises, necessary truth of the full philosophical basis, physical infinite computation or complete wisdom.
