# Cross-platform miniapp sandbox architecture

created: 2026-04-22T07:03:30.648183Z  uuid: 69ab900b-5004-428a-b7c8-69e8f1fa7640  export: new
messages: 4  total_chars: 20657  human_chars: 766

summary: **Conversation Overview**

The person is building OpenClaw, an agent orchestration project with an SST (Space/Spirit/Token) architecture, and was exploring how to implement a miniapp sandbox system. Their core requirement is a full browser WebView (iframe) that can run any single-page HTML or JavaScript file—including LLM-generated "vibe coded" single-file apps—with an SDK automatically injected so that if the LLM knows the SDK surface, it can write miniapps that call SDK methods without any setup or imports. They referenced WeChat Mini Programs as a conceptual model and wanted to know whether mature cross-platform open source solutions exist.

Claude surveyed the landscape across two distinct layers: the web/iframe layer (where mature primitives exist via libraries like Penpal, Comlink, and kkrpc) and the cross-platform native container layer (where no mature OSS exists, with FinClip being the dominant commercial solution). Claude also flagged OpenAI's MCP Apps/Apps SDK as a directly relevant reference architecture—iframe plus postMessage bridge plus ambient window SDK—and recommended building toward compatibility with it for free interop with the emerging agent-UI ecosystem.

For the concrete implementation, Claude provided a complete minimal architecture: using `srcdoc` wrapping with a prelude script injected before user HTML, a ~30-line ambient Proxy-over-postMessage SDK bootstrap that makes any method path callable without pre-registration (so LLM-generated code can call `sdk.anything.you.want(args)` freely), and a parent-side dispatcher that routes calls through capability checks. Claude mapped this directly onto the person's SST primitives—Space as the iframe instance and storage namespace, Spirit as the SDK implementation, Token as the authorization object determining which SDK paths are callable. Claude noted that Penpal is slightly mismatched for this use case because it expects both sides to know the method surface up-front, whereas the Proxy pattern is better suited for LLM-generated code with an open-ended method surface. Reference implementations mentioned include Open WebUI Artifacts and Renderify. Key design decisions flagged for early resolution included sandbox flags (`allow-scripts` only vs. adding `allow-same-origin`), whether to allow external CDN scripts, SDK discoverability strategy (static `.d.ts` in context vs. dynamic `sdk.__schema()` introspection), and persistence routing through `sdk.storage` rather than direct IndexedDB access.


---
**HUMAN** (2026-04-22T07:03):

i want to implement a miniapp sandbox, within this miniapp, it get a sdk, and that is all it can use to interact with the outside. But within it is a full webView(iframe), an llm can use that sdk and generate a one page as miniapp, or it could be coded by other devs, like wechat mini program. this seems to be a useful open source project, are there mature solutions out there that we can consistantly run miniapp across platforms

---
**ASSISTANT** (2026-04-22T07:05):

  The user is asking about sandbox architectures for miniapps with SDK-only interactions, like WeChat's model. I'm thinking through the technical landscape here—WeChat Mini Programs use isolated JavaScript environments with restricted APIs, and there are similar implementations from Alipay and other platforms. I should consider what mature cross-platform solutions exist for this kind of sandboxed execution.

I'm reviewing the main options: FinClip is a commercial solution that supports multiple platforms, there are development frameworks like Taro and uni-app that help build miniapps, and open source projects like kbone from WeChat let you run web code as miniapps. For the actual runtime container specifically, FinClip seems to be the most established commercial option, though I'm less certain about some of the other runtime solutions and whether they're still actively maintained.

Given that Ren is working on agent orchestration and wants to generate miniapps for LLM agents, I should look into what's currently available in 2026 and what would actually work for their use case—both the Chinese ecosystem options and Western open source alternatives.Good question to dig into - the miniapp container space has matured a lot, especially with the Chinese ecosystem pushing it. Let me search for current state of play since this moves fast.
```
This block is not supported on your current device yet.
```

 I've found some useful information on W3C MiniApp standards and Alibaba's SuperApp approach, so now I'm narrowing my search to focus on open-source miniapp runtime containers like FinClip and comparable projects.Let me search for more specific miniapp runtime solutions - especially the ones with cross-platform aspirations.
```
This block is not supported on your current device yet.
```

 I should look into genuinely open source alternatives to FinClip, and also explore what's available in the JavaScript and web-focused space since Ren's needs seem to lean more toward web and iframe-based solutions.Let me look at the web/iframe-focused approaches more directly since that matches your stated architecture.
```
This block is not supported on your current device yet.
```

 I'm noticing that OpenAI's Apps SDK and MCP Apps standard actually implement this exact JSON-RPC over postMessage pattern between host and iframe UI, which is directly applicable to what Ren's building with OpenClaw. I should dig into the mature libraries handling this—Penpal, post-me, comlink—to see what's already available.Let me check a few more specific things - the mature iframe RPC libraries and Shopify's / Atlassian's approach, since those are closest to what Ren described.
```
This block is not supported on your current device yet.
```

 I'm pulling together what I know about Ren's situation—he's building OpenClaw for agent orchestration and needs both a runtime container and architectural primitives for an LLM-generated miniapp sandbox, he's thinking about this as an open source project, and he's based in Shenzhen with deep knowledge of the Chinese tech ecosystem.

Looking at the landscape, there's a clear split: web-only iframe-based approaches like Penpal and Comlink are simpler and browser-native, while full cross-platform miniapp containers like FinClip exist but are mostly commercial. The real gap is that there's no mature open source cross-platform container yet, though OpenAI's MCP Apps and Apps SDK are directly relevant for LLM-generated UI specifically—that's actually the most applicable reference point for what he's trying to build.

For the practical answer: iframe sandboxing with a custom SDK is well-established and mature, but there's no standardized miniapp spec at that layer. For cross-platform native consistency, FinClip dominates commercially, though Alibaba has their own proprietary solution.

Given Ren's constraints—solo developer, fast iteration on OpenClaw—I'd lean toward starting with just the web iframe layer using Penpal or Comlink for transport, then building the SDK around his SST primitives rather than attempting the full cross-platform native container that would be a massive undertaking. I'm settling on a prose-heavy approach with minimal formatting—just a focused list of library options since that's concrete and useful, and I'll make sure to cite specific claims properly while keeping quotes short and preferring paraphrasing instead.Short answer: the space is split into two very different layers, and "mature" looks different in each. Let me give you the honest landscape.

**The web/iframe layer (what you described)**

For just "iframe + SDK bridge", the primitives are extremely mature — you don't need a miniapp framework, you need an RPC library on top of `postMessage` and a well-designed SDK surface. The battle-tested options:

- **Penpal** — promise-based RPC over postMessage, handles iframes/workers/windows, solid origin checks. Closest to what you want out of the box.
- **Comlink** (Google Chrome Labs) — ~1.1KB, uses ES6 Proxies so remote calls feel like local ones. Originally for workers but works with iframes via `windowEndpoint`.
- **kkrpc** — newer, bidirectional, cross-runtime (iframe + worker + stdio + websocket). Worth looking at if you want the same protocol between browser miniapps and, say, Node-hosted ones.
- **post-me, postmate** — older but still used.

None of these give you a "miniapp spec" — they give you the transport. You'd layer your own SDK (what capabilities are exposed, the permission model, lifecycle hooks, packaging format) on top. Which honestly, given your SST architecture, is probably what you actually want: Space = iframe, Spirit = the SDK surface, Token = capability grants on specific methods.

**The cross-platform native container layer (like WeChat)**

This is where "mature OSS" basically doesn't exist. The mature option is commercial:

- **FinClip** (Finogeeks) — the dominant player. Cross-platform SDK covering iOS, Android, Mac, Linux, Windows, with a 3MB core runtime, and syntax compatibility with WeChat mini-programs so you can reuse that ecosystem's code. Not open source but has free tiers.
- **Alibaba EMAS SuperApp** — Alibaba Cloud's equivalent, commercial.
- **W3C MiniApp spec** — there's a real standardization effort with specifications defining the package structure, URI addressing, and runtime environment for miniapps across vendors, but actual cross-vendor adoption is thin outside Chinese giants.

The reason no mature OSS exists here is that it's genuinely huge scope — JS engine integration (QuickJS or V8), a custom rendering pipeline (dual-thread like WeChat's logic/view split), native API bridges per platform, package format, update mechanism, DevTools. FinClip took years with a team.

**The angle most relevant to you: MCP Apps / Apps SDK**

Given OpenClaw is agent-focused, the most interesting thing happening in this space is OpenAI's Apps SDK, which is precisely your architecture for LLM-generated miniapps: the widget renders inside an iframe sandbox and communicates with the host through the MCP Apps UI bridge using JSON-RPC over postMessage. They're also doing CSP allowlisting per app (connect/resource/frame domains), which is the right pattern for LLM-authored code where you want capability scoping by default. This is becoming a de facto spec for agent-generated UI and is worth building toward compatibility with, since it means a miniapp authored for Claude or ChatGPT could run in your OpenClaw host.

**My recommendation for OpenClaw**

Don't build a WeChat-style native runtime — that's a 50-person-year project. Build the web layer, and map it cleanly onto your SST primitives:

1. Use Penpal or Comlink as the transport. Don't reinvent postMessage plumbing.
2. Define your SDK as a capability-scoped surface — Token grants determine which SDK methods a miniapp can call. This is where your SST work pays off, because you already have the authorization semantics figured out.
3. Adopt MCP Apps' JSON-RPC-over-postMessage wire format, or at least stay close to it. That gives you free interop with the agent-UI ecosystem that's forming.
4. Package format: keep it stupid — a manifest + entry HTML + bundled JS, served from a content-addressed store. WeChat's `.wxml/.wxss` split is overkill for v0.
5. If you later need "runs on iOS/Android natively" — wrap a WebView and ship. That's 95% of FinClip's cross-platform story anyway; the remaining 5% is native API plumbing you'd add per platform.

The genuinely useful OSS gap isn't "another FinClip" — it's a clean, agent-native miniapp spec with capability-based security baked in, that's interoperable with MCP Apps. That seems directly in line with OpenClaw's positioning.

Want me to sketch what the SDK surface + Token permission model would look like concretely, mapped onto the SST primitives you've already defined?

---
**HUMAN** (2026-04-22T07:17):

what I need is a full browserView that can inject sdk, and use the sdk easily, any single page html or js can be used as the full code that can be run, penpal seems to be a pretty good pick, but i want any html - for example, anything vibe coded in a single file - if the llm knows the sdk, can write and use the sdk to create miniapps

---
**ASSISTANT** (2026-04-22T07:19):

  So Ren's clarifying that the iframe runs full HTML/JS without restrictions, meaning any single-page app works as a miniapp source. The LLM can generate complete miniapp code in one file since it understands the SDK surface, and since the SDK gets auto-injected, the miniapp just calls SDK methods directly without needing setup.

The core challenge is injecting the SDK into arbitrary user HTML — I'm weighing a few approaches: splicing a script tag into the HTML before it loads (simplest), creating a blob URL with the SDK prepended, using a service worker to intercept and inject, or injecting after the iframe loads from the parent (though that hits same-origin issues).

For same-origin iframes I can use eval or direct injection, but cross-origin sandboxed iframes require postMessage communication. The standard pattern wraps user HTML with a bootstrap script in the head that establishes a postMessage channel to the parent and exposes a global SDK object, so user code can call methods that proxy back through messaging — this is exactly what ChatGPT does with `window.openai`.

I'm now thinking through concrete implementations and checking what's already open source that follows this pattern — Observable's embedded runtime, CodePen, JSFiddle, Scrimba, and CodeSandbox all use similar injection approaches.

For a simple single-file HTML setup, the cleanest approach is wrapping the user's HTML in an iframe with srcdoc and injecting the SDK bootstrap script before their code runs.

Writing the SDK bootstrap... I'm seeing how the LLM would actually use this SDK—it just needs to know the surface API, not the internal message-passing mechanism. If I give it a clean TypeScript interface showing that `window.sdk.getUser()` returns a promise, it can write HTML that calls these methods without understanding the plumbing underneath. I'm also noticing that projects like Sandpack use this exact pattern, so there's precedent for this approach.

The real opportunity here is making the SDK self-describing—the LLM could introspect at runtime to discover what methods are available, or I could provide a schema endpoint. And looking at what's already out there, Anthropic's Artifacts already does this with `window.claude`, so the pattern is proven.

For Ren's response, I should confirm this approach is solid, walk through the actual implementation (wrapping HTML in an iframe with an injected SDK prelude), show the minimal proxy pattern code, and discuss the tradeoffs between srcdoc, blob URLs, and sandboxing flags—then point him toward existing open-source implementations like open-artifacts that he can reference or fork.That use case is simpler and cleaner than a WeChat-style miniapp — you don't need a framework, you just need an iframe runner that injects an ambient SDK before any user script runs. Let me search for what's current in this exact space since it's evolving fast with LLM-generated UI.
```
This block is not supported on your current device yet.
```

 I'm clarifying the architecture Ren needs: an iframe with injected SDK code that creates a `window.sdk` proxy, routing all method calls through postMessage to the parent, which validates permissions via Token before executing and returning results—so the LLM only needs to understand the SDK interface itself.

Looking at existing solutions, Renderify is too heavy with its JSX/transpilation overhead, and Open WebUI's artifact pattern lives in the tool rather than as a reusable library. The pattern of iframing generated code is well-established, so for single-file HTML the minimal setup is an iframe with `srcdoc` containing the SDK bootstrap script followed by the user's HTML.

I'm weighing the key architectural tradeoffs: sandbox flags like `allow-scripts` alone provide the tightest isolation, but adding `allow-same-origin` enables localStorage at the cost of breaking that isolation; there's also the choice between `srcdoc`, blob URLs, and separate-origin approaches, plus how the LLM discovers and uses the SDK interface.

Since the code is LLM-generated, full sandboxing is optional—I can trust my own output—but the security model shifts if other developers write miniapps. The SDK auto-injection means user code just calls `sdk.foo()` without any imports, so I need to show the concrete injector pattern and the postMessage proxy that routes everything back to the parent.Yes — that's the cleanest possible shape, and it's well-worn territory. The whole thing is essentially three tricks stacked:

**1. `srcdoc` wrapping with prelude injection**

Take the LLM-authored HTML and splice a bootstrap `<script>` into it before any user script runs. Render into an iframe via `srcdoc`. This is exactly how Claude/ChatGPT artifacts and the "iframe generated code" pattern popularized by Claude 3.5 Sonnet's Artifacts feature work.

```js
function wrap(userHtml) {
  const bootstrap = `<script>${SDK_BOOTSTRAP}</script>`;
  // Inject before anything the user wrote — robust even if no <head>
  return bootstrap + userHtml;
}

const iframe = document.createElement('iframe');
iframe.sandbox = 'allow-scripts'; // no allow-same-origin = full isolation
iframe.srcdoc = wrap(userHtml);
```

**2. The SDK as an ambient Proxy over postMessage**

This is ~30 lines. Any method name works — no registration — so the LLM can call `sdk.getUser()` or `sdk.db.query(...)` and it just routes.

```js
const SDK_BOOTSTRAP = `
(() => {
  const pending = new Map();
  let nextId = 0;
  addEventListener('message', e => {
    const { __id, ok, value } = e.data || {};
    const p = pending.get(__id);
    if (!p) return;
    pending.delete(__id);
    ok ? p.resolve(value) : p.reject(new Error(value));
  });
  const call = (path, args) => {
    const __id = ++nextId;
    return new Promise((resolve, reject) => {
      pending.set(__id, { resolve, reject });
      parent.postMessage({ __id, path, args }, '*');
    });
  };
  const make = (path) => new Proxy(() => {}, {
    get: (_, k) => make([...path, k]),
    apply: (_, __, args) => call(path, args),
  });
  window.sdk = make([]);
})();
`;
```

Now `sdk.anything.you.want(args)` becomes a postMessage with a method path, which the parent routes. User code looks like:

```html
<script>
  const user = await sdk.user.get();
  document.body.innerHTML = '<h1>Hi ' + user.name + '</h1>';
</script>
```

**3. Parent-side dispatcher with capability check**

```js
iframe.addEventListener('message' /* actually on window */, async (e) => {
  if (e.source !== iframe.contentWindow) return;
  const { __id, path, args } = e.data;
  try {
    if (!token.allows(path)) throw new Error('denied');
    const fn = path.reduce((o, k) => o?.[k], sdkImpl);
    const value = await fn(...args);
    iframe.contentWindow.postMessage({ __id, ok: true, value }, '*');
  } catch (err) {
    iframe.contentWindow.postMessage({ __id, ok: false, value: err.message }, '*');
  }
});
```

That's the entire runtime. ~80 lines total. This is where your SST model slots in cleanly — the Token literally decides which `path`s are callable from that Space.

**Projects doing close variants of this**

- **Open WebUI Artifacts** — open source, same pattern for Claude-style artifacts, supports full webpages with HTML/JavaScript/CSS and JS visualization libraries in the same artifact. Worth reading their Svelte component for a reference implementation.
- **Renderify** — a runtime-first rendering engine that transpiles and sandboxes LLM-generated JSX/TSX in the browser with no build step or server compilation. Heavier than you need (JSX transpilation, module loader), but the iframe/worker/ShadowRealm sandbox abstraction is instructive.
- **OpenAI Apps SDK / MCP Apps** — exact same architecture (iframe + postMessage bridge + ambient `window.openai` SDK), just with JSON-RPC as the wire format. If you match their wire format, ChatGPT-authored miniapps run in your host for free.

**Penpal vs. rolling your own**

Penpal is great but for this specific pattern it's slightly overkill — Penpal expects both sides to know the method surface up-front, whereas you want any path callable so the LLM isn't constrained. The Proxy pattern above is ~50 lines and gives you that. Penpal makes sense if you want the SDK to be structured (with TypeScript-typed method sets) and you're ok requiring the LLM to stay within the defined surface. Either works — I'd start with the Proxy pattern for pure vibes, add Penpal later if you want stricter typing.

**Design decisions worth deciding up front**

1. **Sandbox flags.** `sandbox="allow-scripts"` alone means no cookies, no localStorage, no same-origin — maximum isolation. The tradeoff: user code can't persist anything except through your SDK. Usually what you want for agent-generated code. If you add `allow-same-origin` you get a loose escape hatch but lose most of the guarantee.

2. **SDK discoverability for the LLM.** Two approaches:
   - *Static*: paste the SDK's TypeScript `.d.ts` into the LLM's context. Simple, cheap, works today.
   - *Dynamic*: expose `sdk.__schema()` that returns the JSON schema of available methods. LLM can query it at generation time. More flexible when the Space's allowed methods vary by Token.
   
   I'd do both — static for speed, dynamic for agents that explore.

3. **The "vibe-coded single file" contract.** Decide up front whether user HTML can use external CDN scripts (`<script src="https://cdn.jsdelivr.net/...">`). Allowing it is much more useful (Tailwind, React, Three.js all just work via CDN). The tradeoff is that your iframe now makes outbound requests you can't fully audit. CSP on the wrapper HTML is your lever here.

4. **Persistence.** If a miniapp needs state across sessions, expose `sdk.storage.get/set` routed to your Space's storage. Don't give it IndexedDB directly.

5. **UI affordances from parent.** Things like "open in fullscreen", "share this miniapp", theming — the parent needs to be able to push data *into* the iframe too, not just respond. Add a symmetric `iframe.contentWindow.postMessage({ event, payload })` channel and expose `sdk.on(event, handler)` inside.

**Where your SST architecture makes this clean**

The whole thing maps almost 1:1:

- **Space** = the iframe instance + its configured SDK surface + its persistent storage namespace
- **Spirit** = the SDK implementation (the set of methods the Space can call)
- **Token** = the authorization object that determines which SDK paths this particular Space instance can actually invoke

So a miniapp isn't just "HTML in an iframe" — it's "HTML in a Space, with a Spirit attached, gated by a Token." The same vibe-coded HTML file run with different Tokens has different capabilities. That's the thing FinClip/WeChat/Apps SDK don't quite have — they all have permission systems, but not a unified capability-token primitive. This is the actual differentiating shape for OpenClaw.

Want me to sketch a minimal repo structure — host runtime, SDK definition format, Token → capability mapping — so you can see how the pieces fit concretely?
