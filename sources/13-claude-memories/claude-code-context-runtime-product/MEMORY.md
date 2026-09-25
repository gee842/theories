# Memory index

- [Principal ticket lifetime](principal-ticket-lifetime.md) — stale runtimes lose the DB; RLS errors that look like provisioning bugs are usually ticket expiry
- [Live deployment layout](live-deployment-layout.md) — live DB `context_runtime_product` at :55432, runtime homes under `data/runtimes/`, forensics via `cp.audit` + `SET context_runtime.internal=on`
