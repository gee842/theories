# AI-generated miniapp library naming

created: 2026-04-24T15:07:11.266385Z  uuid: 83908920-0695-4f27-b0a9-73ed6b1305e7  export: new
messages: 6  total_chars: 14024  human_chars: 473


---
**HUMAN** (2026-04-24T15:07):

i am creating a miniapp like system, or you could think it like claude artifact, it can communicate via api

and the miniapps can be ai created - 

I am just trying to come up with a good name for this library

---
**ASSISTANT** (2026-04-24T15:08):

  I'm thinking about what would fit well for Ren's system—something that captures the idea of modular, AI-generated components that communicate together. Given their mycology-inspired approach to agents, I could lean into that aesthetic while keeping the name practical and memorable for a library that handles miniapp creation and orchestration. heir existing vocabulary (Spirit/Space/Token, mycology agents) - I need something that feels native to their system and doesn't blur into Claude Artifact territory.

Given Ren's background with SST architecture and mycology metaphors, plus their fluency in both Chinese and English, I'm drawn to a few strong contenders. **Qi (器)** captures something essential - it's the concrete vessel or instrument in Chinese philosophy, which maps perfectly onto what a miniapp actually is. The Dao/Qi distinction is foundational to their thinking. **Fruitbody** works equally well from the mycology angle - it's the visible manifestation that emerges from the mycelium network, just as miniapps are the tangible expression of underlying agent capabilities. **Shard** suggests both a fragment of functionality and the composability they're after, while **Facet** implies different aspects of a larger system.

I'm also considering **Lens** as a way of viewing or interacting with capability, **Portal** for entry points, **Bloom** for that sense of emergence and biological resonance, **Cell** as both a biological and computational unit, and **Glyph** for something small and inscribed.

Looking at what Ren actually needs—a miniapp-like system that functions as an artifact, communicates via API, and is AI-generated—the strongest candidates feel like **Qi** for its philosophical depth and bilingual appeal, **Fruitbody** to stay consistent with the mycology theme, **Facet** for its clean description of UI aspects, or **Shard** for its composable, crystalline quality.

Given Ren's background with WeChat mini-programs and the Nomad OS analogy platform, **Qi** becomes even more compelling. It captures the essence of what a miniapp is—a concrete vessel through which abstract capability manifests, which mirrors the classical Chinese philosophy where Qi represents the physical manifestation of Dao. It's short, memorable, and carries real resonance for someone bilingual working in this space.

I'm also weighing whether this should be the name for the collection itself or for individual units within it. I'm deciding on the format here—this should stay conversational and concise, just offering Ren a few thoughtful options without overexplaining. Since he works across multiple traditions, I can reference the philosophical layer naturally without being heavy-handed about it.

Looking at the naming directions: Qi works as a bilingual play on the Daoist concept of concrete manifestation versus abstract principle, and it fits neatly as a tool-vessel for capabilities. Fruitbody extends the mycology metaphor from OpenClaw—the visible user-facing layer that emerges from the underlying network. Facet is simpler and more literal, describing how each miniapp surfaces one aspect of a larger capability. And Cartouche...

Actually, I'm leaning toward Qi or Fruitbody depending on the weight I want to give this layer architecturally. But I should probably trim the options and think about what feels most natural as a library name in English, especially since this is meant to be accessible to developers.A few directions that might fit the vocabulary you've already built:

**Qi (器)** — the obvious philosophical play. 形而上者谓之道，形而下者谓之器. Dao is the abstract way; Qi is the concrete vessel through which it manifests. A miniapp literally *is* a 器 — a concrete tool-vessel for a capability. Bilingual, short, and slots alongside SST as the "manifestation" layer. Library name reads clean (`qi`, `qi.js`, etc.) and individual miniapps are Qi instances.

**Fruitbody** — continues the OpenClaw mycology lineage. The fruitbody is what erupts from the mycelial network into the visible world: exactly what a miniapp is relative to your agents. Spore (first contact) → Hypha/Mycel (network) → Fruitbody (user-facing manifestation). The progression tells a coherent story.

**Facet** — clean, UI-flavored. Each miniapp is a facet of a larger capability surface. Less metaphysical weight, more shipping-a-library-to-npm energy.

**Cartouche** — the Egyptian enclosure that wraps an inscribed name. Self-contained, artifact-in-the-archaeological-sense. Probably too obscure unless you want obscure.

**Husk** / **Shell** — if you want to emphasize the sandboxed-container aspect (iframe/SDK model). Husk has a nice duality with Spore actually — the spore is the seed, the husk is what it ships inside.

My gut: **Qi** if you want it to feel load-bearing and philosophically coherent with SST. **Fruitbody** if you want the biological lineage to stay intact — and it probably should, because the mycology metaphor is already doing real work for you conceptually.

One consideration either way: since these are AI-generated and API-communicating, a name that hints at *emergence* (fruitbody) or *manifestation* (qi) beats a name that hints at *containment* (shell, husk, cartouche). The interesting property is that they come into being, not that they're sandboxed.

---
**HUMAN** (2026-04-24T15:09):

miniapp... artifact... sandbox... do we have better names for them? be creative, i am naming a library i wrote

---
**ASSISTANT** (2026-04-24T15:09):

 Let me brainstorm broadly — the target is something that names "an AI-generated, API-speaking, self-contained runnable thing."

**From the manifestation/emergence angle:**
- **Bloom** — what a mycelial network produces. Brief, lives well as both noun and verb (`bloom.create()`, "bloom a new one").
- **Efflux** — something that flows out. Technical-sounding, rare enough to own.
- **Emanate** / **Emanation** — neoplatonic vibe, the thing that radiates from a source.
- **Surface** — miniapps are where the agent-substrate surfaces into the user's world. Also a verb. Very clean.

**From the vessel/manifestation angle (Chinese philosophy):**
- **Qi (器)** — concrete vessel/tool, counterpart to Dao. Already mentioned but genuinely strong.
- **Xiang (象)** — image/manifestation/phenomenon. 大象无形 — the great image has no form. Nice for something that's configurable, protean.
- **Yong (用)** — "function" / "application" in the 体用 (substance-function) pair. Literally means "use." A miniapp is a Yong of an underlying capability.
- **体用 / Ti-Yong** — the pair itself, if the library has two halves.

**From the physics/chemistry angle:**
- **Quantum** — discrete packet. Overloaded but evocative.
- **Monad** — self-contained unit (Leibniz, not Haskell). Probably too loaded for programmers.
- **Capsule** — small, sealed, carries a payload. Clean and honest about the sandbox nature without being boring.
- **Crucible** — a vessel where transformation happens. Heavier, more dramatic.
- **Vial** — small, sealed, contains something potent. I like this one more than I expected.

**From the theatrical/performative angle:**
- **Scene** — a miniapp is a scene the AI stages for you. Ephemeral, composed, has actors and state.
- **Cast** — as in "cast a spell" or "cast of a play." Verb and noun.
- **Stage** — self-explanatory.
- **Conjure** / **Conjury** — AI summoning a UI on demand. Fits the "AI-created" property specifically.
- **Glyph** — an inscribed symbol that does something when drawn. I like this a lot for AI-generated artifacts — it captures the "summoned into being, self-contained, performs a function" trio.
- **Sigil** — same neighborhood as glyph, slightly more occult.
- **Rune** — too fantasy-novel probably, but: rune = inscribed thing that holds power until invoked.

**From the biological angle (extending mycology):**
- **Sporocarp** — technical term for fruitbody. More scientific, less poetic.
- **Gemma** (pl. Gemmae) — a small propagule that buds off a parent organism and grows into a new one independently. This is *literally* what an AI-generated miniapp is relative to the agent that made it. Short, pronounceable, has real biological precision, and nobody's using it.
- **Frond** — a single leaf-unit of something larger.
- **Spawn** — mushroom spawn is the inoculum; also a programming term. Double meaning.

**From the conceptual-unit angle:**
- **Facet** — a face of something larger.
- **Aspect** — similar.
- **Mode** — a way the system presents itself.
- **Instance** — too generic.

**From pure sound/brevity, invented or near-invented:**
- **Pod** — small, sealed, carries something living. Honest.
- **Nib** — the business-end of a pen. Small, pointed, where ink meets paper. Cute.
- **Moiety** — a part/portion, often used in chemistry. Unusual.
- **Wisp** — something small and transient.

---

**My top picks for your specific case**, in order:

1. **Glyph** — An AI-inscribed, self-contained, API-speaking thing you summon to do work. "Call a glyph," "render a glyph," "compose glyphs." Reads great as code (`glyph.mount()`, `Glyph<Props>`). Captures the *generated-on-demand* property that "miniapp" and "artifact" both miss.

2. **Gemma** — Most biologically precise if you want to extend the OpenClaw metaphor: agents (mycelium) bud off gemmae (miniapps) that can grow and run independently. Short, unclaimed, pronounceable, and it's *correct* rather than merely evocative.

3. **Qi (器)** — If you want the SST philosophical lineage to keep paying dividends. 道 is the protocol, 器 is the manifest tool. Bilingual users will feel it land.

4. **Surface** — If you want something that sounds more like infrastructure and less like a metaphor. The cleanest "library on npm" option.

5. **Capsule** — If honesty about the sandbox nature is the feature you most want to convey.

Between Glyph and Gemma, I'd probably pick **Glyph** — the "inscribed, summoned, self-contained, does something when invoked" meaning maps almost perfectly onto what you're building, and the name sounds better in English than Gemma does for a technical audience. But Gemma slots more cleanly into the mycology story you've already told.

---
**HUMAN** (2026-04-24T15:13):

"inscribed thing that holds power until invoked." interesting, how about it holds power and can be displayed?
gemma is good - but most people won't get it

---
**ASSISTANT** (2026-04-24T15:13):

 Right — so the property you want named is "holds latent capability AND is displayable/renderable." Not just dormant until invoked, but *presents itself* when summoned.

**Names that capture "inscribed + displayable + potent":**

- **Glyph** — still the top candidate. A glyph is *by definition* both inscribed (holds form/meaning) and visible (displayed). That's literally the word. The "invoked" connotation is a bonus, but the base meaning is already "a symbolic mark that is seen." This fits your requirement *exactly*.

- **Sigil** — a glyph with explicit power/intent. Slightly more occult-flavored than glyph. "Sigil" implies the inscribed thing was *made to do something*, which fits AI-generated-for-a-purpose. Reads well: `sigil.render()`, `createSigil()`.

- **Emblem** — an inscribed visual unit that stands for something and is displayed. More heraldic than magical. Less common in code.

- **Tessera** (pl. tesserae) — a tile in a mosaic. Each one is self-contained, visually present, and composes into a larger picture. Nice for a library where miniapps compose. But obscure.

- **Cartouche** — inscribed, bordered, displayed. Obscure though.

- **Totem** — an inscribed object that is both seen and carries power/identity. Carries cultural weight that might not fit.

- **Icon** — literally "image that stands for something." Extremely clean. But overloaded in software (desktop icons, React Icons, etc.).

- **Crest** — displayed, identity-bearing, inscribed. Too heraldic maybe.

- **Mandala** — displayed, structured, carries meaning. Culturally loaded.

- **Ideogram** — a symbol that represents an idea directly. Fits "an AI compressed a capability into a displayable form" quite literally. Less mystical than glyph, more semiotic.

**Invented/combined options:**

- **Lumen** — unit of visible light. "It holds potential and shines when called." Has a nice dual meaning: lumen is also "an opening/channel" in anatomy (the lumen of a vessel). Both meanings fit — a channel that shines.

- **Facet** — reconsidering: a facet of a gemstone both *holds* (structural) and *displays* (reflects light). This is actually pretty good for "holds power and is displayed."

- **Prism** — takes input, refracts it into something visible. A miniapp takes API/data and refracts it into a UI.

---

**Sharper recommendation:**

**Glyph** is still the best fit because "inscribed mark that is displayed" is its literal definition — you're not stretching the metaphor, you're using it correctly. Sigil is the runner-up and pushes harder on the "made to do something" angle, which matters more if your miniapps are *action-oriented* (buttons, forms, tools) rather than *display-oriented* (dashboards, visualizations).

Quick gut-check: **is a typical miniapp in your system more like a tool or more like a view?**

- Mostly **tools/actions** (calculators, form-fillers, API callers) → **Sigil** leans in on the "inscribed to act" meaning.
- Mostly **views/displays** (dashboards, maps, readouts) → **Glyph** is cleaner.
- **Both** → **Glyph**, because it's the more general word and doesn't carry the occult baggage.

One more to consider given your bilingual bent: **符 (fú)** — this is the Chinese word that covers both "talisman/sigil" and "symbol/mark." 符咒 is a magical charm, but 符号 just means "symbol." It's the same semantic space as glyph/sigil but with the bilingual resonance SST has. Would read as `fu` in code — short, unclaimed on npm last I knew, and carries exactly the "inscribed thing that holds power and is displayed" meaning you just described. Worth weighing against Glyph.
