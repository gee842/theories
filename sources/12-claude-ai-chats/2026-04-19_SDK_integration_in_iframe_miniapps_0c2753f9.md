# SDK integration in iframe miniapps

created: 2026-04-19T13:51:31.823659Z  uuid: 0c2753f9-0a5d-4684-b0d6-134e51142615  export: new
messages: 4  total_chars: 18031  human_chars: 225


---
**HUMAN** (2026-04-19T13:51):

can i create a miniapp program by passing an sdk to iframe and allow it to use the sdk?

---
**ASSISTANT** (2026-04-19T13:52):

  I'm recognizing this as a question about iframe security and SDK access — the user wants to know if an SDK can be passed into an iframe so that embedded mini-apps can use it, which is a core architectural challenge for building something like a mini-app platform. The answer involves understanding cross-origin policies, postMessage communication, and whether direct SDK access is feasible or if you need to proxy calls through the parent window. epts:

1. **Same-origin policy**: If the iframe is same-origin, you can directly access `iframe.contentWindow` and assign things to it, or the iframe can access `window.parent`.

2. **Cross-origin**: If the iframe is cross-origin (which is usually what you want for mini-app isolation/security), you CANNOT directly pass JavaScript objects/functions. You must use `postMessage` for communication.

3. **The common pattern for mini-app platforms** (like WeChat, Alipay, Line mini-programs):
   - Host a JS SDK that the mini-app includes
   - The SDK wraps `postMessage` calls under a nicer API (e.g., `wx.pay()`, `wx.getUserInfo()`)
   - The parent window listens for messages and handles privileged operations
   - Results are posted back to the iframe

4. **Why you can't just "pass an SDK"**:
   - Functions cannot be serialized across origins
   - postMessage uses structured clone algorithm which doesn't support functions
   - Even same-origin, passing live objects creates tight coupling

5. **Modern approaches**: Libraries like `comlink`, `postmate`, and `penpal` abstract away the complexity of `postMessage` by creating proxy-based RPC systems, or you can use service workers for certain scenarios. Same-origin setups can use direct window property assignment, but that's less common for production mini-app platforms.

6. **Security considerations**: Always validate `event.origin` in message handlers, expose only what the mini-app needs through a capability-based approach, use sandbox attributes on the iframe, and remember that the SDK running in the iframe's context can be inspected by the mini-app author — so treat it as untrusted code.

Given the context here, this looks like it's about building a mini-app or super-app platform, so I should structure the response around the same-origin vs cross-origin distinction and explain why the standard pattern works the way it does. The actual pattern: SDK lives in the iframe, communicates via postMessage to host. Security model: if the iframe is cross-origin, you can't pass live JavaScript objects directly — structured clone drops functions. So what actually happens is the SDK script loads inside the iframe as a thin shim that wraps postMessage calls into a nice API (like `app.pay({...})`), while the parent window listens for those messages, validates the origin, runs the privileged operations, and posts results back. The SDK then resolves its promise with the response — so the "SDK in the iframe" and the "real implementation in the host" are two halves of the same operation.

Setting up the message bus... I'm considering a few libraries that handle the postMessage plumbing—`comlink` from the Chrome team gives the nicest ergonomics by turning it into Proxy-based RPC, while `penpal` and `postmate` are promise-based alternatives. For a Nomad OS-style platform, `comlink` maps naturally to the capability model since you just expose what the host needs via `Comlink.expose()`. If the iframe is same-origin, I could also directly assign the SDK object to `iframe.contentWindow`, though that's mainly useful for trusted sub-surfaces like design-system previews.

Now I'm thinking about whether this response is the right length—it's technical and Ren is building something platform-like, so the detail feels appropriate. I should tighten the formatting though, moving away from heavy headers and letting it flow more naturally as prose. The core point is that same-origin iframes give third-party authors full access to the host's DOM and auth state, which is a security problem.

Actually, the real issue is that you can't pass a live JavaScript object across the iframe boundary when it's cross-origin—the browser's same-origin policy blocks direct property access, and postMessage uses structured clone which strips out functions. So instead, the pattern used by WeChat and similar platforms is to have the mini-app load a host-provided SDK script that runs in its own context. This SDK is just a thin wrapper around postMessage calls, giving a nice API surface without any actual privileged logic. When the mini-app calls something like `app.pay()`, the SDK translates that into a postMessage call back to the host.

Writing the SDK implementation... I should limit each mini-app's access to only the methods it needs, and use the iframe sandbox attribute strategically—`sandbox="allow-scripts"` without `allow-same-origin"` gives strong isolation with a null origin. For the actual implementation, libraries like Comlink (which wraps postMessage into a clean RPC interface), Penpal, or Postmate can handle the messaging plumbing, with Comlink's `expose()` method mapping nicely onto a capability model. There's a caveat with same-origin iframes though—

while you can directly assign the SDK object to `iframe.contentWindow`, that only works safely for trusted surfaces you control; third-party mini-apps shouldn't be same-origin since they'd get unrestricted access to your DOM, cookies, and auth state.Yes — this is the standard mini-app pattern, but the way "passing the SDK" actually works is worth unpacking, since the naive mental model doesn't match what the browser allows.

If the iframe is cross-origin (which you want for isolation), you cannot hand it a live JavaScript object or function. Same-origin policy blocks direct property access, and `postMessage` uses structured clone, which drops functions. So you can't literally pass an SDK instance across.

What actually happens in WeChat / Line / Alipay-style mini-programs: the mini-app loads a host-provided SDK script (`<script src="https://host.com/sdk.js">`) that runs inside the iframe's own context. The SDK is a thin shim — it contains no privileged logic. It just wraps `postMessage` calls with a nice API surface. When the mini-app calls `app.pay(args)`, the SDK posts `{method: 'pay', args, id}` to `window.parent`. The host listens, validates origin, authorizes, runs the real payment flow, and posts the result back; the SDK resolves its promise. Two halves connected by a message bus.

```js
// iframe (sdk.js) — runs in mini-app's context
window.app = {
  pay: (args) => new Promise((resolve) => {
    const id = crypto.randomUUID();
    window.parent.postMessage({ id, method: 'pay', args }, HOST_ORIGIN);
    const handler = (e) => {
      if (e.origin !== HOST_ORIGIN || e.data.id !== id) return;
      window.removeEventListener('message', handler);
      resolve(e.data.result);
    };
    window.addEventListener('message', handler);
  })
};

// host
window.addEventListener('message', async (e) => {
  if (e.origin !== MINIAPP_ORIGIN) return;
  const result = await dispatch(e.data.method, e.data.args, /* auth ctx */);
  e.source.postMessage({ id: e.data.id, result }, e.origin);
});
```

A few things for the security model. The SDK runs in the mini-app's context, so the mini-app author can inspect or tamper with it — never put authorization checks in the SDK; all of that lives on the host side. Always validate `event.origin` on incoming messages. Treat each SDK method as a capability and only expose what that particular mini-app needs. And use the iframe's `sandbox` attribute aggressively: `sandbox="allow-scripts"` (deliberately omitting `allow-same-origin` where you can) gives you a null origin and very strong isolation.

For plumbing, three libraries worth knowing. Comlink (from the Chrome team) turns `postMessage` into Proxy-based RPC so you call it like a local object — probably the nicest DX for a Nomad OS-style platform. Penpal is promise-based parent/child iframe communication. Postmate is older and simpler but still widely used. Comlink's `expose()` also maps naturally onto a per-app capability model.

One caveat: if the iframe is same-origin, you actually *can* do `iframe.contentWindow.SDK = sdkObject` and the child reads it directly. That's fine for trusted sub-surfaces you authored yourself, but for third-party mini-app code, same-origin is a mistake — they'd get full access to your host's DOM, cookies, and auth state.

---
**HUMAN** (2026-04-19T14:10):

i want to design a sdk that allow access of data and interface, in my spirit sense, to be able to allow miniapp to use my spirit token sdk

---
**ASSISTANT** (2026-04-19T14:12):

  Ren is asking about designing an SDK that lets miniapps interact with their SST (Spirit-Space-Token) architecture through a capability-based system — similar to how UCAN and Zanzibar handle access control through tokens rather than traditional permissions.

The core challenge is that the SDK needs to let miniapps present tokens to request operations, have the host verify and authorize those requests, and then expose both data and UI surfaces (modals, toasts, navigation) scoped to what each token permits. The tricky part is that the SDK running inside the iframe shouldn't hold the token's authority itself — it's just carrying the bearer's identity while the host validates what they're actually allowed to do.

I'm sketching out the capability surface: data operations like read, write, and subscribe on sprites, spatial queries, UI affordances that the host renders rather than the miniapp, and agent-to-agent invocation with token delegation. The flow would be that the host launches the miniapp with an initial token, the miniapp can narrow it down before passing it along, and every operation carries the token so the host can re-verify. When calling other sprites, the miniapp delegates a more restricted token to maintain the chain of trust.

Now I need to figure out what the actual SDK shape should look like and how to present this without over-explaining the SST primitives. they already built)
2. Show a concrete SDK shape
3. Cover the token-verification model (authority lives on host)
4. Address data vs interface surface split
5. Note the delegation/attenuation story since that's SST-distinctive vs a plain postMessage bridge

Format: This is a design discussion. Code snippets where they clarify, prose for the reasoning. No heavy headers. Keep it focused. Ren is a sophisticated builder who wrote the SST spec — don't over-explain basics, go straight to the design choices.

Let me draft this. It should feel like continuing a design conversation with someone who knows the primitives.

I need to check the terminology first — they're using "Sprite" in the SST architecture, so "spirit" is likely autocorrect. I'll align with their language and center everything on SST.

I have enough context to sketch the design. The core idea is straightforward: tokens travel with every call, the host owns verification, and the iframe SDK is just a typed RPC layer with capability checks. When the host launches the miniapp, it mints a root token scoped to a Space with a Sprite identifier, and that becomes the foundation for everything downstream.

The token delivery is critical — it should never touch server logs, so it goes via URL fragment or the first postMessage, never query string. Once the SDK receives it, it attaches it to every subsequent call.

Now I'm sketching out the SDK shape itself...

Writing SDK interface... Finishing the API surface with token attenuation, then I'm noting two key design principles: the SDK itself holds no authority—the token does all the work, and the host verifies every call regardless of what the SDK claims. Data access is purely token-gated, while interface operations like modals and navigation use a different grant model where the user mediates the permission.

When a miniapp invokes a delegated call like `sprite.invoke('payments.charge', ...)`, the host validates the caller's token can delegate to that capability, then mints a fresh narrower token scoped just to that operation.

**Subscriptions.** Push notifications from host to miniapp need their own channel separate from the request/response bus to avoid mixing concerns, and all subscriptions get cleaned up when a miniapp's token expires or is revoked.

**What the SDK shouldn't do.** Don't put valid authorization, rate-limiting, or access logic in the iframe-side SDK since miniapp authors can rewrite it anyway — keep the SDK minimal and let it just serialize calls, attach tokens, and wait for responses. All the actual enforcement happens on the host side.

One key design question: are tokens bearer tokens where just holding them grants capability, or are they bound to a sprite's keypair so you need both the token and the ability to sign with the matching key? That choice shapes whether the handshake is just "receive and store" or if the SDK also needs access to signing functionality. I'm deciding whether a diagram of the token delegation chain would actually help here or if it's unnecessary overhead—code and prose should be enough for someone thinking in systems terms. I'll keep the response focused and tight, using bold for key points to make it scannable without overloading it.The shape that fits SST cleanly: the token travels with every call, the host is the authority that interprets it, and the SDK inside the iframe is just a typed facade over a capability-checked RPC bus. Inside the iframe there's no real "access" — only requests that carry a token, which the host re-verifies.

**Handshake.** Host mints a root token when it launches the miniapp, scoped to a Space, bearing a Sprite identity, pre-attenuated to whatever the miniapp needs. Delivered via first `postMessage` (not URL query — don't leak it to server logs). The SDK stashes it and attaches it to every subsequent call.

```js
// sprite-sdk.js — loaded inside the miniapp iframe
const token = await handshake(); // receives root token via first postMessage

export const sprite = {
  // data surface — token-scoped reads/writes
  read:      (ref)              => rpc('data.read',    { ref }, token),
  write:     (ref, value)       => rpc('data.write',   { ref, value }, token),
  subscribe: (ref, cb)          => sub('data.sub',     { ref }, token, cb),
  query:     (spaceRef, filter) => rpc('space.query',  { spaceRef, filter }, token),

  // interface surface — host renders, miniapp requests
  ui: {
    modal:    (opts)            => rpc('ui.modal',     opts, token),
    toast:    (msg, kind)       => rpc('ui.toast',     { msg, kind }, token),
    navigate: (spaceRef)        => rpc('ui.navigate',  { spaceRef }, token),
    pick:     (kind)            => rpc('ui.pick',      { kind }, token), // returns a NEW narrower token
  },

  // agent surface
  invoke:    (spriteRef, args)  => rpc('sprite.invoke', { spriteRef, args }, token),

  // attenuation — narrow your own token before handing it downstream
  attenuate: (caveats)          => rpc('token.attenuate', { caveats }, token),
};
```

A few design choices worth pulling out for SST specifically:

**The SDK holds no authority; the token does.** A miniapp author can inspect, rewrite, or strip the SDK — fine, because nothing is enforced by the SDK's structure. All enforcement lives in the host-side verifier that runs on every incoming RPC. Keep the iframe SDK boring: serialize, attach token, await response. No validation, no rate-limiting, no access logic client-side.

**Data and interface need different grant models.** Data ops are pure token checks — if caveats permit `read(space/X/*)`, it goes through silently. Interface ops split: passive ones (toast, inline mount, modal with miniapp-owned content) are token-gated, but *active* ones that touch resources outside the miniapp's caveats — pick a contact, choose a file, confirm a payment — flow through host-rendered user consent and return a **fresh, narrower token** for the specific resource granted. This is the capability-request pattern: the miniapp never holds `contacts.read`, it holds `contact:<uuid>` for the one contact the user picked. This matters a lot for SST's territorial story — miniapps never widen scope, they only receive attenuated grants from the user's active consent.

**Delegation is a host operation.** When a miniapp calls `sprite.invoke('payments.charge', ...)`, the host doesn't forward — it checks whether the caller's token permits delegation to that target, mints a fresh attenuated token carrying the caller in the invocation chain, and executes. The miniapp can also explicitly `attenuate()` before spawning a sub-iframe or sub-sprite. The host enforces the monotonic narrowing invariant (can only shrink caveats, never grow) by refusing to sign a broader child than its parent. That's where your UCAN-style delegation graph lives in the SDK flow.

**Subscriptions need their own channel.** Open a `MessageChannel` port during handshake dedicated to host→miniapp push, separate from the request/response bus. Tear down all subscriptions when the miniapp's token is revoked or expires — don't rely on the miniapp to unsubscribe cleanly.

One question that'll shape the SDK surface significantly: in your v0.1 spec, are tokens **bearer** (capability = holding the blob) or **key-bound** (capability = holding the blob *and* signing with a matching sprite keypair)? Bearer tokens mean the handshake is receive-and-store, and the SDK is essentially what I sketched. Key-bound tokens mean the SDK also needs access to a sprite's signing key inside the iframe — which changes the sandbox story substantially, because now you're either (a) exposing key material to potentially-tampered miniapp code, or (b) routing every signature request back to the host, at which point the key-binding isn't really buying you anything over bearer-plus-origin-check. If you haven't pinned this yet, worth deciding before the SDK surface hardens around either assumption.
