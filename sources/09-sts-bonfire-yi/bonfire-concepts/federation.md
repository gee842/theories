# Federation

Federation remains a bounded integration layer over Bonfire's normalized
runtime. It does not alter context ownership or introduce a second install,
handler, event, or migration plane.

## Current invariants

- Yi `uid` and Kind family identity remain stable across hosts.
- Semantic cross-host coordinates remain strings where a local foreign key is
  impossible.
- Imported packages use `PortableKitInstallSourceV3` and the ordinary package
  workflow.
- Import authorization uses the same Authority/workflow envelope as local
  installation.
- Export policy is privileged operation metadata stored with installation
  provenance; it is not a semantic Kind facet.
- Local and connected Worlds expose the same typed transport contract.

Import never reinterprets schema ids, reconstructs detached declarations, or
falls back to an older wire decoder. Protocol `162` is exact.

## Trust and causality

Identity owns principal keys and revisions. Authority owns certificates and
revocation consistency. Occasion commits provide causal positions for imported
effects and server-side watch order. Federation code must not manufacture
ambient authority or bypass installed workflows.

## Deferred work

Peer discovery, replication topology, offline conflict policy, archive proofs,
and multi-host recovery policy are not promised by the current SDK. New work in
those areas must preserve the fifteen-context owner graph and the Occasion
spine rather than adding compatibility storage or dual writes.
