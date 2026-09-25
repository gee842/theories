# Federation signing boundary

This page records the current boundary for signed federation data. It is not a
separate public authoring API.

Identity principal records own public keys, key history, and recovery
coordinates. Signed import/export operations resolve those records through the
Identity repository and authorize their workflow through Authority. Signature
verification does not infer a representation from identifier spelling or
authored fields.

Imported Kit data uses canonical `PortableKitInstallSourceV3` bytes. Imported
runtime effects name their Occasion causal position. Protocol `162` rejects
older wire shapes rather than lowering them through a compatibility decoder.

Hosted key custody, recovery ceremonies, replication transport, and archive
proofs remain separate follow-up work. Any implementation must use narrow
Identity/Authority/Occasion entrypoints and keep physical placement details out
of public Kind and SDK surfaces.
