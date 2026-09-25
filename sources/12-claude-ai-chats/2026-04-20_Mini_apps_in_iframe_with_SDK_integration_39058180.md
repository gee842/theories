# Mini apps in iframe with SDK integration

created: 2026-04-20T09:54:36.617470Z  uuid: 39058180-9ce9-4fbc-a944-c7dd7fa0ab57  export: new
messages: 2  total_chars: 11956  human_chars: 309

summary: **Conversation Overview**

The person asked whether an iframe-based architecture with a platform SDK is a good approach for enabling third-party developers to build and distribute mini apps inside their host application, with the host acting as a server-like API provider. They also asked how this model interacts with Apple and Google app store policies. No explicit role, company, or personal details were shared beyond the technical context of the project.

Claude validated the approach as architecturally sound and well-established, citing WeChat Mini Programs, LINE Mini Apps, Telegram Mini Apps, Discord Activities, and Farcaster Frames as precedents. The response covered the core technical pattern of sandboxed iframes with a postMessage bridge SDK, the tradeoff between iframe-based execution and custom JS runtimes, the importance of a capability model and manifest schema defined early, and how the person's existing SST (Spirit/Space/Token) conceptual framework maps naturally onto mini-app permission architecture.

On store policies, Claude detailed Apple's November 2025 updates to guideline 4.7, including the new Mini Apps Partner Program offering 15% commission, restrictions on native API exposure to mini apps without approval, age-rating requirements, and the IAP exemption for physical goods and real-world services. Google Play's more permissive stance was noted alongside its digital goods billing requirements. Claude flagged that an Android-first approach suits SEA market dynamics, highlighted the web/PWA escape hatch for policy-constrained categories, and recommended early decisions on manifest schema design and Partner Program eligibility. The conversation included Claude using web search tools to retrieve current policy information before responding.


---
**HUMAN** (2026-04-20T09:54):

i want to allow people to develop mini apps in iframe, and we will be providing a sdk that allows it to talk/call the platform(which is the app)
is this a good approach? if i do this people can release their mini apps in my app, and access app(as a server api like)
how will this work with apple/google store?

---
**ASSISTANT** (2026-04-20T09:56):

  The user is asking about whether an iframe-based architecture with an SDK for host-app communication is a solid approach, and how it interacts with app store policies from Apple and Google. This is coming from Ren who's working on OpenClaw/Nomad OS infrastructure for Southeast Asia.

I'm recognizing this as the WeChat Mini Program pattern—a well-established model also used by LINE, Telegram, Farcaster, and Slack. The technical approach involves running mini-apps in sandboxed iframes with a postMessage bridge that exposes host APIs like identity, payments, storage, and notifications. The main advantages are security through sandboxing, universal web tech, easy distribution without native compilation, and no app review delays for individual mini-apps. The tradeoffs are performance compared to native code, some sandbox limitations on iOS WKWebView, and the critical question of how app store policies actually handle this pattern.

Now I'm working through the app store constraints, which is where this gets complicated. Apple's guideline 4.7 technically allows HTML5 games and bots under certain conditions, and they've been updating their stance—especially with the DMA changes in the EU and their 2024 guideline updates. The core issue is that if mini-apps involve paid content or digital goods, iOS requires using Apple's IAP system with their 30% cut, though WeChat Mini Programs and Telegram Mini Apps have found ways to operate within these rules by fitting into specific categories. Google Play is generally more permissive but has similar restrictions around circumventing Play Billing. I need to check what the latest guidance actually says since this is an area where Apple's policies have been actively evolving.

The architectural pattern itself—iframe-based with an SDK—is well-established and proven across WeChat Mini Programs, LINE Mini Apps, Telegram Mini Apps, and similar platforms. But the store policy implications are trickier and worth searching for current information, especially given that Ren's building this for SEA markets where regulatory context differs from China's WeChat ecosystem.

I need to check the current state of Apple's guideline 4.7 (updated in 2024) and Google Play's equivalent policies, since these rules around mini apps and third-party app distribution have been evolving, particularly with DMA effects in the EU.This is a well-trodden path — what you're describing is essentially the WeChat Mini Program / LINE Mini App / Telegram Mini App / Farcaster Frames pattern. Architecturally it's sound, but the app store question is the actual hard part and it's been moving recently. Let me check the current state.
```
This block is not supported on your current device yet.
```

 Apple's Mini Apps Partner Program launching in November 2025 with a 15% commission is a direct hit for what Ren's building. Now I need to look at Google Play's policies since Android dominates the SEA market he's targeting.Let me check Google Play's stance too, since SEA is heavily Android.
```
This block is not supported on your current device yet.
```

 I'm pulling together the key insights here — the iframe and SDK approach is solid and well-established, but what really matters for Ren is Apple's new Mini Apps Partner Program launching in November 2025, which opens up entirely new distribution possibilities. I need to walk through the technical constraints around native API access and age ratings, contrast that with Google Play's more flexible but still tricky landscape, and then give him concrete recommendations tailored to his situation. Message is the standard pattern (LINE, Telegram, etc.)
- WeChat Mini Programs use a custom JS runtime (not iframe) for performance and security but it's WAY more work
- For mobile, you'd embed the iframe in WKWebView (iOS) or WebView (Android)
- Capability-based SDK = good fit with his SST architecture (Spirit/Space/Token)

Key Apple constraints:
- Guideline 4.7 — must comply, mini apps treated as full apps
- 4.7.2 — CANNOT expose native APIs to mini apps without Apple permission
- 4.7.4 — manifest required
- 4.7.5 — age rating
- IAP required for digital goods
- New Mini Apps Partner Program (Nov 2025) gives 15% commission instead of 30% — but requires Advanced Commerce API, Declared Age Range API, structured manifest

Key Google constraints:
- More permissive
- Need to provide value beyond just a webview
- Standard payment policies (Play Billing for digital goods)
- WebView apps under increased scrutiny in 2026 but real platforms with mini apps are different from "wrapper" apps

For Nomad OS specifically, this approach aligns well with the vision. The payment layer gets tricky with IAP rules, but physical goods and services in SEA markets fall outside Apple's IAP requirements — that's actually a significant advantage. Crypto-to-fiat micro-payments for real-world transactions should be exempt from their policies too. I'm thinking through how to structure this response: validate the approach, walk through the technical considerations, be clear about store policy realities, and give him specific things to evaluate. He's technical and direct, so I'll aim for depth without unnecessary length.Yes, the iframe+SDK approach is sound — it's the same pattern as WeChat Mini Programs, LINE Mini Apps, Telegram Mini Apps, Discord Activities, Farcaster Frames, and now ChatGPT Apps. Architecturally well-trodden. The interesting parts are the specifics, and the store situation just shifted significantly in November 2025.

## The architecture itself

Standard pattern is sandboxed iframe + postMessage bridge to the host. Your SDK is a thin client that wraps `window.parent.postMessage` calls into a typed RPC interface (`platform.payment.request()`, `platform.identity.whoami()`, etc.) and the host implements the message handler with permission gates.

A few real choices to make:

**iframe vs. custom JS runtime.** WeChat famously doesn't use iframes — they ship their own JS engine (originally JavaScriptCore-based, now a fork) with a restricted DOM-like API surface called WXML/WXSS. This buys them better performance, tighter security, and lifecycle control, but it's enormous engineering. iframes (or WKWebView/WebView on mobile) are the 95% solution and what most platforms actually ship. Telegram and LINE went iframe-style. Start there.

**Capability model.** This maps very naturally onto your SST work — each mini app gets a Spirit (identity), runs in a Space (the iframe sandbox), and is granted Tokens (capabilities) for what it's allowed to ask the host for. The SDK becomes the user-facing surface of token redemption. Worth being deliberate about this since you'll want it composable later.

**Manifest format.** Define it early. Permissions declared, version, age rating, entry points, allowed origins. You'll need this for review processes anyway (see below) and it's how mini-app marketplaces stay legible.

## The Apple situation — this is where it got interesting

In **November 2025** Apple did two things at once: tightened guideline 4.7 *and* launched the **Mini Apps Partner Program**. Both matter for you.

The tightening: HTML5 and JavaScript mini apps are now under full App Store oversight — what was previously a gray area is now black-and-white. Your host app is responsible for every mini app's compliance. Three concrete constraints:

1. Guideline 4.7.2 prohibits exposing native platform APIs to mini apps without prior Apple approval — no camera, no push, no contacts, no location, no filesystem bridges out of the box. Mini apps get the same surface as Safari unless you negotiate exceptions.
2. Guideline 4.7.5 requires age rating mechanisms — you must identify mini apps that exceed your host's rating and gate them.
3. Digital goods sold inside mini apps must go through Apple IAP (this is the historical 30% problem).

The Partner Program is the upside. Apple now offers a 15% commission instead of 30% on qualifying IAPs inside third-party mini apps, provided you adopt the Advanced Commerce API, the Declared Age Range API, StoreKit IAP, structured mini-app manifests, and refund consumption reporting. A mini app is defined as a self-contained HTML5/JS experience built by a separate third party, downloaded after install, running inside your native host — not a feature your team built and wrapped in a webview.

**The implication for Nomad OS specifically:** if the mini-app economy is *physical-world* commerce (paying for coffee in Da Nang, splitting a bill in Chiang Mai, real-world services), Apple IAP doesn't apply at all — physical goods and real-world services are explicitly exempt and always have been. AEON Pay → local fiat for real-world transactions is fine. The IAP question only kicks in for digital goods consumed inside the app (game items, subscriptions to digital content, etc.). For your roadmap that's actually a good split.

## Google Play

Much more permissive. No equivalent to 4.7. The main risks for you:

- Google Play in 2026 has been actively filtering out low-value "wrapper" apps that just display a website — but a real platform hosting third-party mini apps with commerce, identity, and payment is categorically not a wrapper app, so this isn't aimed at you.
- Play Billing applies to digital goods the same way IAP does. Same physical-goods exemption.
- Real-money gaming, gambling-adjacent calls to action, and some financial services categories have country-specific restrictions — relevant for SEA markets where you might host fintech-adjacent mini apps.

## What I'd actually flag for you

A few things worth thinking through given where you are:

**Sandbox the SDK from day one as if Apple is watching.** Treat "no native API exposure without explicit user-mediated permission" as the default even on Android/web, because retrofitting is painful and you'll want a single capability model across platforms. Your Token primitive makes this natural.

**Manifest schema is your most important early artifact.** It's the contract between host and mini app, the input to your review process, the input to Apple's review process, and probably the thing Apple will want to see if you ever apply to the Partner Program. Spend time on it.

**Decide your stance on the Partner Program early-ish.** It's invite-style, requires the Advanced Commerce API, and is clearly aimed at the WeChat/Alipay/LINE pattern. If digital-goods commerce inside mini apps is a real part of your model, applying is probably correct. If it's all real-world payments via AEON, you don't need it. Bloomberg reported Apple and Tencent agreed to the same 15% rate for WeChat — the program is the formalization of that deal opened to other developers.

**SEA-first means Android-first dynamics.** Most of your users are on Android, where you have far more freedom. You can probably ship a much richer Android experience and a more constrained iOS one, gated behind capability flags in the SDK. WeChat does exactly this.

**The web/PWA escape hatch.** Don't forget it exists. If a mini app violates Apple rules, the same code can run in your PWA / mobile web version with no restrictions. Useful for categories Apple won't permit (certain crypto interactions, etc.).

The one architectural question I'd push you on: are you building this as "iframe with broad SDK and host-defined permissions" (Telegram model — simple, flexible) or "constrained DSL with strict capability typing" (WeChat model — more work, much better legibility and security)? Given your SST work I suspect you'll drift toward something more typed than a raw postMessage bridge, even if you start with iframes for execution.
