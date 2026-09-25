# Federation recovery boundary

Recovery is Identity-owned principal evolution authorized by a declared
workflow and Authority policy. It is not a special Kind category or an
application handler bypass.

A recovery workflow validates its evidence, advances the Identity principal
revision, records any Authority issuer-epoch/revocation effects, updates the Yi
root's actual Occasion head, and commits once. Failed or concurrent recovery
attempts leave no partial key or certificate state.

The public SDK does not currently promise a stock recovery-policy catalog.
Future social, threshold, grace-period, or hardware-backed policies must ship
as installed workflow artifacts with exact schemas and handler provenance.
Remote execution must use the same typed transport and protocol `162` as local
execution.
