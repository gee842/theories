---
name: examples-test-leg-masked-by-build-bail
description: "check:release runs example build before example tests; a build failure prevents the runtime leg from starting"
metadata:
  node_type: memory
  type: project
  originSessionId: 70c08fc7-6dcc-4191-9cb3-cd72cb328ec2
  modified: 2026-08-15T01:07:22.798Z
---

The live `check:release` script ends with:

`pnpm -r --filter './docs/examples/*' run build && pnpm -r --filter './docs/examples/*' run test`

Recursive pnpm execution bails on the first failing task by default, and `&&`
skips the test leg when the build leg fails. A reported example build failure
therefore says nothing about later build packages or runtime example tests.

For diagnosis, enumerate both surfaces independently:

`pnpm -r --filter './docs/examples/*' --no-bail run build`

`pnpm -r --filter './docs/examples/*' --no-bail run test`

The old dated failure counts are not a standing red-suite inventory; this note
pins only the current command behavior and operator action under
[[verification-regime-2026-08-14]].
