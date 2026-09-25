---
name: named_spirit_storage_shape_drift
description: "Resolved named-spirit storage drift — current readers use referent-linked Yi children and owned-Kind dimensions"
metadata: 
  node_type: memory
  type: project
  originSessionId: bef148ee-33f5-48c3-9494-b89a6ca24e88
---

All six named community spirits now read the Yi substrate. Collection members
are referent-linked child holdings queried with `rt.yi.children` or
`rt.yi.where`; kit data lives in each row's owned-Kind `dimensions[...]`, not
`items`, root `contents` arrays, or child `payload`.

`heron.ts` derives the installed roster-presence Kind and scans it by referent.
`owl.ts` reads the Ritual dimension's nested `config` and traverses Occurrence
and Attendance children. Their tests use the real Roster and Ritual writers.

Prefer `rt.as(caller).read` / `where` or handler `ctx.find` / `where` for
product reads. `rawYiGet` in `packages/std/src/raw-yi.ts` is the marked std
bootstrap/system escape hatch. The old synthetic-fixture false-green and
`unifiedHoldings.update` recipe are superseded.
