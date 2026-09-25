# Scalable MMORPG character panel design

created: 2026-04-21T09:35:19.737404Z  uuid: 7df782d5-c3cd-40ac-ac3b-8deb5d5f29da  export: new
messages: 4  total_chars: 31771  human_chars: 264


---
**HUMAN** (2026-04-21T09:35):

how are mmorpg character panels are designed? to be able to equipt items,  and can extend the system over time, add more types and things that can be used differently, with status change automatically

---
**ASSISTANT** (2026-04-21T09:40):

  The user is asking about MMORPG character panel architecture—how to design a system that supports equipping items, scales with new item types over time, and automatically reflects status changes. Given their background in extensible systems design, they're really looking for the underlying architectural patterns that would make this flexible and maintainable.

This is established game dev territory, so I'm thinking through the core patterns: defining equipment slots as data rather than hardcoding them, treating items as compositions of modifiers that can be applied to stats, using an event-driven system to propagate changes when equipment changes, and keeping everything data-driven so new item types don't require code changes. The key insight is separating the slot system, item properties, stat aggregation, and change notifications into distinct layers that can evolve independently.

Given Ren's background in systems thinking, I should frame this architecturally—referencing ECS patterns and composition over inheritance—and probably include a diagram to show how these components interact, since the visual flow of data and events is central to understanding the design. I'm deciding between a flow diagram showing the equip sequence or a structural diagram of the architecture itself—the flow diagram would be more concrete and show the reactive chain, so I'll go with that approach and keep the prose explanation focused on the key patterns without padding. Continuing with the data structure...

The key insight is that items are just containers holding a list of modifiers—each modifier specifies which stat it affects, what operation to apply, and the value. This means I can compose complex effects by stacking modifiers, and the stat pipeline automatically recalculates whenever equipment changes. A flaming sword might add strength, fire damage, and apply a burning effect all through the same modifier system, so adding new stat types or effects later doesn't require rewriting the item definitions. The current rewritten thinking already describes the modifier and trigger system with code examples. The next thinking continues with the stat pipeline architecture and event-driven updates, then mentions registries and extensibility.

Since the current output ends with code-like content (the modifier/trigger structure), I should switch to prose and compress the next thinking into 1-3 sentences without repeating the modifier/trigger pattern already described.

Here's the rewrite:

Stats flow through layers—base stats, equipment modifiers, buffs, and derived stats—each as a pure function you can cache and invalidate on change. Rather than polling, the system uses events: when equipment changes or damage occurs, listeners automatically update the stat pipeline and UI, so adding new behaviors is just registering new event handlers. Three registries handle most extensions: one for custom stats, one for modifier operations, and one for effect handlers, letting you ship patches with new items and mechanics without touching existing code.

The key pitfalls are computing stats every frame instead of caching with dirty flags, getting modifier order wrong (flat adds before percentage adds before multiplicative), conflating item instances with templates, and letting UI logic leak into the model. This is really ECS at its core—the character is an entity, equipment and stats are components, and the stat pipeline is a system.

Now I'm thinking a visual diagram would really help here. The response is solid, but showing the layered architecture and data flow would make it click for people. Let me create that diagram.The durable architecture behind extensible character panels comes down to one principle: **separate the data (what things are) from the pipeline (how they interact)**. If you hardcode "swords give +5 strength," you're stuck; if items are composed of declarative modifiers that plug into a stat calculation pipeline, you can add new mechanics for years without touching the core.

Here's how the pieces fit:

**Slot system as data.** Slots aren't enum constants — they're definitions like `{id, name, acceptedTags, exclusiveWith}`. A "head" slot accepts items tagged `helmet`. A "two-handed weapon" occupies both mainhand and offhand (exclusivity rules). You can ship a "jetpack" slot in a patch without changing engine code.

**Items = container + list of modifiers + list of triggers.** An item isn't `Sword { str: +5 }`. It's closer to:

```json
{
  "id": "flaming_sword",
  "slot_tags": ["weapon"],
  "modifiers": [
    { "stat": "str", "op": "add", "value": 5 },
    { "stat": "fire_damage", "op": "add", "value": 10 }
  ],
  "triggers": [
    { "event": "on_hit", "handler": "apply_burn", "params": { "dps": 3, "duration": 5 } }
  ]
}
```

Modifiers are declarative data. Triggers point to effect handlers registered in a plugin registry. Adding lifesteal = register a new handler; no existing code changes.

**Stat pipeline.** Stats flow through ordered layers — base (class/level) → equipment modifiers → buffs/debuffs → derived stats (crit% from dex, etc.). Each layer is a pure function of its inputs. Cache the output, invalidate on change. Modifier ordering matters — spell it out explicitly: `base → flat adds → percentage adds → final multiplicative`. Games that get this wrong spawn endless balance bugs.

**Event-driven updates.** Don't poll. `equip(slot, item)` fires an `equipment_changed` event. The stat pipeline marks its cache dirty. The UI listens and re-queries on redraw. Buffs listen to `on_hit`, `on_damage_taken`, `on_tick`. This is where "automatic status change" comes from — a new buff type is just a new subscriber to existing events.
```
This block is not supported on your current device yet.
```

 Now I'm deciding between a structural diagram showing the architecture layers versus a flowchart that traces how equipment changes propagate through the system. The flowchart approach seems clearer for showing the user interaction flow, though I'm still working through the exact sequence of steps. I'm leaning toward a structural layered diagram since it better illustrates the architecture they're asking about—showing how data definitions feed into state management, which flows through the computation pipeline and out to consumers like the UI and combat system, with the event bus threading through as a cross-cutting concern. I'm reconsidering the layout—instead of three vertical columns, I'll use a flow diagram where the registries sit at the top as data sources feeding into the core runtime components, then those emit events down to the consumers at the bottom.

Building the diagram... I'm realizing this is getting too cluttered, so let me simplify the whole diagram down to four core layers: registries at the top for extensible data, then runtime state with character and equipment, followed by the stat pipeline computation, and finally the consumers like UI and combat system reading from it. I'll position the event bus off to the side to show how events flow through the system.

Actually, a flowchart showing the equipment flow would be clearer—walking through what happens when you equip an item, from validation through the event bus triggering the pipeline recompute and finally the UI update. This makes the architecture's purpose more obvious.

Let me simplify and use a structural diagram instead with three columns: data layer on the left with registries, runtime in the middle with slots and the pipeline, and consumers on the right. I'll use arrows to show how data flows through the system.

Actually, I'm realizing I'm overcomplicating this—I have too many boxes for the complexity budget. Let me collapse it down to three vertical layers instead: data registries at the top, runtime state and pipeline in the middle, and UI/Combat consumers at the bottom.

I'll color-code by layer—purple for the extensible data side, teal for the stateful runtime, and gray for the neutral consumers—and make sure to label the event bus somewhere. Now I'm ready to start building the SVG with a 680-pixel width and roughly 400 pixels tall to fit everything comfortably.

Writing SVG diagram... I'm going back and forth on how to represent the event bus—whether it should be its own visual element or just labeled on the arrows. Let me simplify this and focus on the core flow: Slot → Item Instance → Modifiers → Pipeline → Stats, with a subtitle explaining the event bus connections.

Actually, I think a structural diagram showing Registries feeding into Runtime State, which then flows through the pipeline to the Event Bus and out to consumers like UI and Combat, captures the architecture better than a purely linear view.

Now I'm laying out the SVG diagram with specific positioning—setting up container boxes for the Registries, Consumers, and Runtime State sections, then placing the individual components like Item Templates, Effect Handlers, UI Panel, and the pipeline flow within those containers. I'm finishing the layout with Row 4 containing the UI Panel and Combat System as consumers, then mapping out the data flow with arrows showing how the data layer feeds into runtime, which emits events to the event bus, which cycles back to trigger recomputation and notifies the consumers. Now I'm calculating the exact positioning for each component box. I need to reconsider the arrow connections based on the actual data flow. Item Templates should feed into Equipment Slots since slots hold instances of those templates, while Effect Handlers connect to the Event Bus as listeners rather than directly to the slots. Then Equipment Slots and Active Buffs both feed their modifiers into the Stat Pipeline, and the Event Bus ties into the overall event flow.

Rather than drawing every connection, I could simplify this by organizing the diagram into conceptual layers—Data, Runtime, and Consumers—with arrows flowing between them to show the relationships more clearly.

Writing SVG code... Building the diagram... Writing SVG layout... I'm going back and forth on whether to include the extensibility layer, but it's really central to the design—I need to show it. Let me commit to a structure: Row 1 for the plugin definitions (Item Templates and Effect Handlers), Row 2 for the runtime state (Slots, Pipeline, Buffs), and Row 3 for the consumers (Event Bus, UI Panel, Combat System).

Now I'm mapping out the connections: definitions feed down into state with dashed arrows, the state components flow horizontally into the Pipeline, everything emits events downward, and those events notify the consumers. I'm using a color scheme to distinguish each layer—purple for plugins, teal for runtime, amber for events, gray for consumers—and I'm ready to start building the SVG with the viewBox and arrow markers.

Writing SVG diagram... I'm working through the arrow connections between rows and realizing the diagonal paths are getting messy. Let me reconsider the layout so the boxes in row 1 align directly with row 2, which would make the connections cleaner and more straightforward. I'm reorganizing this into a single Registry row with three aligned columns—Item templates, Stat definitions, and Effect handlers—so the connections flow cleanly downward to Slots, Pipeline, and Buffs respectively, even though Effect handlers technically feed the Event Bus rather than Buffs directly. I'm accepting this visual compromise for the sake of alignment clarity.

Actually, Effect handlers do connect to Buffs since Buffs have their own modifiers and triggers that need implementations, so the semantic mapping works after all. But I'm realizing Effect handlers are really a cross-cutting registry that serves multiple layers—they're referenced by Item templates, Triggers, and Buffs—so they don't neatly align with just one Row 2 component. Let me restructure this more cleanly by separating Data definitions in Row 1 (Item templates and Effect handler registry) from Runtime state in Row 2.

Now I'm settling on a four-row layout: definitions at the top with Item templates and Effect handlers, then runtime state with Equipment slots, Active buffs, and Base stats feeding into the Stat pipeline, followed by the Event bus, and finally the consumer systems like the UI and Combat. Actually, let me just do it and commit. Final plan:

viewBox 0 0 680 480

Row 1 (Data definitions) y=40, h=56:
- Item templates: x=80, w=220 (title "Item templates", subtitle "Data-driven registry")
- Effect handlers: x=380, w=220 (title "Effect handlers", subtitle "Plugin registry")

Row 2 (Runtime state) y=160, h=56:
- Equipment slots: x=40, w=180 (title "Equipment slots", subtitle "What's worn")
- Active buffs: x=250, w=180 (title "Active buffs", subtitle "Temp modifiers")
- Base stats: x=460, w=180 (title "Base stats", subtitle "From class/level")

Row 3 (Pipeline + Events) y=260:
- Stat pipeline: x=40, y=260, w=400, h=56 (title "Stat pipeline", subtitle "Base → equip → buffs → derived")
- Event bus: x=460, y=260, w=180, h=56 (title "Event bus", subtitle "Pub/sub for changes")

Row 4 (Consumers) y=380, h=56:
- UI panel: x=100, w=200 (title "UI panel", subtitle "Reads derived stats")
- Combat system: x=380, w=200 (title "Combat system", subtitle "Listens to on-hit etc.")

Height: 380+56+30 = 466

Now I'm laying out the arrows to show data flow between these components. I'm going to simplify this and just use dashed layer backgrounds labeled "Plugins (data-driven)", "Runtime state", "Computation", and "Consumers" with clear arrows showing how data flows between them—Equipment slots and Active buffs emit events to the Event bus, which feeds into the Stat pipeline and then out to the consumers.

Actually, let me step back and think about this differently. I'll show a horizontal pipeline flow: Base stats flowing through Equipment mods, then Buff mods, then producing Derived stats, with annotations above showing how Item Templates and Effect Handlers feed into the Equipment layer as the extensible plugin system, and below showing the Event Bus triggering recomputation.

Now I'm setting up the SVG structure with specific positioning for each component layer. Writing SVG diagram... Building the diagram layout... Writing SVG layout... Writing SVG diagram... Writing SVG diagram... I'm checking the character widths for the remaining labels and verifying the arrow paths don't cross any boxes—the diagonal from the Effect handlers down to Equipment passes cleanly through the gap between rows. I'm reconsidering the "Data layer" label—it clutters the diagram without adding much since the color already signals its purpose. I'll remove it and keep the design clean. Now I need to refine the arrow routing, particularly the curved paths from Item templates and Effect handlers down to Equipment, since they're currently converging at the same point (265, 170) which creates visual crowding. Let me spread them to different entry points on the Equipment box to improve clarity. Writing SVG paths... I've settled on the simplest approach: two direct arrows connecting each row 1 item to its corresponding row 2 box below it, with slight diagonals to show the relationship. Now I'm building out the SVG structure for the diagram. Writing the diagram structure... Writing SVG diagram... Writing SVG diagram... Building the diagram layout... Adjusting the vertical positioning for the two-line text block — I'll shift the title up to y=68 and subtitle down to y=88 to better center them within the row, though y=72 and y=90 are close enough. Adjusting the vertical positioning for consistency—I'll use title at center-10 and subtitle at center+8 for row 1, which gives me title y=68 and subtitle y=86. Actually, let me recalculate this properly: with a box height of 56 pixels containing a 14px title and 12px subtitle (roughly 26px total text), I need about 15 pixels of top padding, placing the title center at box_y + 22 and subtitle center at box_y + 40.

For row 1 at y=50, that works out to title y=72 and subtitle y=90—my original values were correct. The box center is at 78, so the title sits 6 pixels above center and subtitle 12 pixels below, which is slightly bottom-weighted but looks fine aesthetically.

For the event bus row with just a title and subtitle (no separate subtitle line), I'm using a smaller box at y=280 with height 44, centering it at 302, and placing the title at y=296 and subtitle at y=314—maintaining the same 6-above, 12-below offset pattern.

Now I'm verifying that the arrow paths don't overlap any labels: the curved paths from the top boxes down to y=170 have clear space, the vertical arrows running through the middle sections are unobstructed, and the lower vertical arrows also have room. The viewBox height of 460 accommodates the consumer boxes ending at y=436 plus padding, so everything fits.

For the response, I'll present the prose first since it's already written, then add the diagram with a couple of loading messages to keep things light—something like "Sketching the architecture" and "Labeling the layers"—and wrap up by connecting this back to Ren's SST work.

I'm thinking about the flow: intro prose, then the key architectural components, the diagram showing the layered structure, and finally the extensibility patterns with that SST connection. The diagram placement works where it is now.

For the closing bit about ECS and SST, I need to keep it straightforward—not overcomplicating the analogy between items as tokens, slots as typed references, and effects as the capability system. Let me finalize this and get it submitted.
```
This block is not supported on your current device yet.
```

**Extensibility pattern — the registry.** Three registries cover most future extension needs:

- Stat registry (add new stats like "corruption" or "lightning_resist" — just declare them, pipeline picks them up)
- Modifier operation registry (add/mul/set, or a custom one like "cap_at")
- Effect handler registry (for on-hit, on-tick, on-killed triggers)

A patch ships new item JSON plus new handler code; the engine core stays untouched. This is the thing that lets games run for a decade and keep shipping new mechanics.

**Pitfalls worth knowing:**

- Don't recompute stats eagerly every frame — cache with dirty flags, invalidate on equipment/buff change.
- Modifier ordering matters a lot. Spell it out: `base → flat adds → percentage adds → final multiplicative`. Games that leave this ambiguous get endless balance bugs.
- Don't conflate item *instance* (the sword Ren owns, enchanted, with durability 47) with item *template* (all flaming swords). Instance has a reference to template plus its own state.
- Resist putting UI logic in the item/stat model. The panel reads from the model; nothing flows the other way.

This is essentially ECS applied to gear: Character is an entity, Equipment/Stats/Buffs are components, the Stat Pipeline is a system. If you squint, it's the same shape as your SST model — `item_instance` is a token carrying capabilities (modifiers + triggers), `slot` is a pointer with a schema constraint (tag filter), `effect handlers` are hooks in the handler registry. Same primitives, different domain.

---
**HUMAN** (2026-04-21T16:36):

give me a full design of the item json, not just a demonstration

[attachment excerpt_from_previous_claude_message.txt]
{
  "id": "flaming_sword",
  "slot_tags": ["weapon"],
  "modifiers": [
    { "stat": "str", "op": "add", "value": 5 },
    { "stat": "fire_damage", "op": "add", "value": 10 }
  ],
  "triggers": [
    { "event": "on_hit", "handler": "apply_burn", "params": { "dps": 3, "duration": 5 } }
  ]
}


---
**ASSISTANT** (2026-04-21T16:38):

  I'm scoping out what a production-grade item schema needs for their MMORPG system—given their background with capability-based architecture, they'll expect something that handles identity, metadata, and the structural foundations that scale across a real game backend. Starting with the core: stable unique identifiers, localization-aware naming, visual assets, rarity tiers, classification, and level requirements as the baseline.

The key architectural decision is separating item templates (the blueprint of what an item is) from instances (the actual equipped copy with mutable state like durability, enchantments, and affixes). Then I'm mapping out the slot system—what slots accept this item, whether it occupies multiple slots like a two-handed weapon, and what items it conflicts with. For stat modifications, I'm thinking in terms of a layered pipeline: each modifier targets a stat, applies an operation (add, multiply, set, or cap), and can scale based on level or other attributes. And for dynamic behavior, I'm designing an event-driven trigger system that fires on equip, damage taken, kills, ability casts, and other gameplay moments—each with conditions like cooldowns, proc chances, and execution priority to control the order effects resolve.

Now I'm fleshing out the remaining item properties: sockets for gems with their types and what's socketed in them, affixes that roll randomly within value ranges, set bonuses tied to equipping multiple pieces, durability tracking with repair costs, and economic metadata like vendor value and bind types. I also need to capture requirements (level, class, attributes), whether the item grants active skills, transmog appearance data, and a schema version for migrations. The real challenge is making this composable and registry-driven so Ren can plug in custom handlers and behaviors without hardcoding everything.

I'm thinking through the architecture now—separating behavioral references from declarative data, treating conditions and scaling as first-class concepts, and keeping a clean split between item templates and runtime instances. I'll present the full template schema, the instance schema for mutable state, and a worked example so he can see how it all fits together. Since he appreciates technical depth, I'll go inline with prose explanations rather than a separate file, walking through each section as I build it out. I'm going back and forth on whether this deserves its own file or should stay inline — it's substantial reference material, but the user asked for it directly in the response, so I'll keep it as a well-organized code block with prose around it. Now I'm laying out the core design principles: separating template definitions from runtime state, using registry references for all behavior, treating conditions as first-class constructs, declaring scaling through formulas, enabling composition through nested sockets and set bonuses, and building in schema versioning for future migrations.

Writing the item schema... Defining the item modifiers and special effects... Defining the durability system with decay rates and repair costs, then setting up the economy parameters like vendor value and trade restrictions, and finally capturing the granted abilities and instance data for this specific weapon. Finishing up the enchantment structure, then I need to explain the design rationale behind these schemas — why I'm separating template definitions from instances, and what patterns this enables for item management and rollback scenarios.A real item spec splits into two documents: the **template** (immutable definition, lives in content database, shared across all instances) and the **instance** (mutable per-item state, lives in player inventory). The template is what designers write; the instance is what the game server persists.

## Template schema

```json
{
  "schema_version": "1.0",
  "id": "flaming_sword_of_the_phoenix",
  "kind": "equipment",

  "display": {
    "name_key": "item.flaming_sword_phoenix.name",
    "description_key": "item.flaming_sword_phoenix.desc",
    "flavor_key": "item.flaming_sword_phoenix.flavor",
    "icon": "icons/weapons/sword_phoenix.png",
    "model": "models/weapons/sword_phoenix.glb",
    "rarity": "epic",
    "quality_color": "#a335ee"
  },

  "tags": ["weapon", "sword", "two-handed", "fire", "elemental"],

  "equipment": {
    "slot_tags": ["mainhand"],
    "occupies": ["mainhand", "offhand"],
    "exclusive_with": [],
    "set_bonus_tag": "weapon"
  },

  "requirements": [
    { "type": "level",     "min": 60 },
    { "type": "class",     "allowed": ["warrior", "paladin"] },
    { "type": "attribute", "stat": "str", "min": 120 },
    { "type": "faction",   "faction": "order_of_ember", "min_standing": "honored" },
    { "type": "quest",     "completed": "trial_of_ash" }
  ],

  "modifiers": [
    { "stat": "str",          "op": "add", "layer": "flat",    "value": 25 },
    { "stat": "fire_damage",  "op": "add", "layer": "flat",    "value": 40 },
    { "stat": "crit_chance",  "op": "add", "layer": "percent", "value": 0.05 },
    {
      "stat": "fire_damage",
      "op": "mul",
      "layer": "final",
      "value": 1.15,
      "condition": { "type": "target_has_status", "status": "burning" }
    },
    {
      "stat": "spell_power",
      "op": "add",
      "layer": "flat",
      "scaling": { "formula": "owner.level * 1.5" }
    }
  ],

  "triggers": [
    {
      "event": "on_hit",
      "handler": "apply_status",
      "params": {
        "status": "burning",
        "duration_ms": 5000,
        "tick_damage_formula": "3 + 0.2 * owner.spell_power"
      },
      "chance": 0.30,
      "cooldown_ms": 0,
      "internal_cooldown_ms": 1500,
      "priority": 100
    },
    {
      "event": "on_crit",
      "handler": "spawn_projectile",
      "params": { "projectile": "phoenix_feather", "count": 3, "homing": true },
      "cooldown_ms": 6000
    },
    {
      "event": "on_equip",
      "handler": "grant_ability",
      "params": { "ability": "phoenix_dive" }
    },
    {
      "event": "on_unequip",
      "handler": "revoke_ability",
      "params": { "ability": "phoenix_dive" }
    }
  ],

  "sockets": [
    { "index": 0, "type": "prismatic", "accepts_tags": ["gem", "rune"] },
    { "index": 1, "type": "red",       "accepts_tags": ["gem"], "socket_bonus": {
        "modifier": { "stat": "str", "op": "add", "layer": "flat", "value": 10 },
        "condition": { "type": "socketed_has_tag", "tag": "red" }
      }
    }
  ],

  "affix_pool": {
    "prefix":  { "pool_id": "weapon_prefix_tier5",  "roll_count": 1 },
    "suffix":  { "pool_id": "weapon_suffix_tier5",  "roll_count": 1 },
    "implicit": []
  },

  "set_membership": {
    "set_id": "phoenix_regalia"
  },

  "durability": {
    "max": 100,
    "decay_on_hit": 0.05,
    "decay_on_block": 0.2,
    "broken_penalty": "disable_modifiers",
    "repair_cost_formula": "max * 10 * rarity_multiplier"
  },

  "economy": {
    "vendor_value": 15000,
    "tradeable": true,
    "sellable": true,
    "bind_type": "bind_on_equip",
    "stackable": false,
    "max_stack": 1
  },

  "granted_abilities": [
    { "ability": "phoenix_dive", "source": "equip" }
  ],

  "appearance": {
    "transmog_id": "sword_phoenix_epic",
    "particle_effects": ["ember_trail", "heat_shimmer"],
    "weapon_trail_color": "#ff6b2e"
  },

  "metadata": {
    "added_in_patch": "3.2.0",
    "designer_notes": "BiS for fire warriors S4",
    "telemetry_tag": "loot.raid.s4.phoenix"
  }
}
```

## Instance schema

```json
{
  "schema_version": "1.0",
  "instance_id": "itm_01HX9Z...",
  "template_id": "flaming_sword_of_the_phoenix",
  "owner_id": "plr_abc123",
  "container": { "type": "equipped", "slot": "mainhand" },

  "state": {
    "durability_current": 87.5,
    "bound_to": "plr_abc123",
    "bound_at": "2026-04-18T14:02:00Z",
    "acquired_at": "2026-04-18T14:00:00Z",
    "acquired_from": { "source": "loot", "encounter": "ashmaw_heroic" }
  },

  "rolled_affixes": [
    {
      "affix_id": "of_the_inferno",
      "position": "suffix",
      "roll_seed": 0.732,
      "modifiers": [
        { "stat": "fire_damage", "op": "add", "layer": "flat", "value": 12 }
      ]
    }
  ],

  "sockets": [
    { "index": 0, "socketed_instance_id": "itm_01HX9A..." },
    { "index": 1, "socketed_instance_id": null }
  ],

  "enchants": [
    {
      "enchant_id": "lifesteal_minor",
      "applied_at": "2026-04-20T18:22:00Z",
      "expires_at": null,
      "applied_by": "plr_xyz789"
    }
  ],

  "upgrades": {
    "upgrade_level": 2,
    "upgrade_path": "infusion"
  },

  "custom_name": "Ashbringer",
  "inspector_comment": ""
}
```

## Design notes on non-obvious fields

**`op` + `layer` together.** `op` is *how* the modifier combines (`add`, `mul`, `set`, `cap_min`, `cap_max`, `override`); `layer` is *where* in the pipeline it applies (`base`, `flat`, `percent`, `final`). Keeping them orthogonal means you can have a flat add AND a final multiplier on the same stat from the same item. Games that conflate these (e.g., just `type: "flat_add"`) end up with combinatorial enum explosion as designers want new combinations.

**`condition` on modifiers.** This is what enables conditional stats ("+15% fire damage vs burning targets") without special-casing. Conditions are themselves a plugin registry — `target_has_status`, `owner_hp_below`, `time_of_day`, `in_combat`, etc. A condition that returns true means the modifier is active; the stat pipeline just filters modifiers by condition evaluation each recompute.

**`scaling.formula`.** Declarative formulas that reference named inputs (`owner.level`, `owner.str`, `item.upgrade_level`). Parse once, evaluate often. Don't embed code — use a tiny expression language. This lets designers author items without engineer involvement.

**`chance`, `cooldown_ms`, `internal_cooldown_ms` on triggers.** `cooldown_ms` is the player-visible cooldown (triggers can't fire more often than this globally). `internal_cooldown_ms` (ICD) is the per-target throttle that prevents procs from going nuclear with fast weapons or AoE. Every MMO eventually invents ICD; bake it in from day one.

**`priority` on triggers.** When multiple handlers hook the same event, priority determines order. Matters for effects that can suppress each other (a "prevent fatal damage" handler needs to fire before a "lose all durability on death" handler).

**`occupies` vs `slot_tags`.** `slot_tags` is where the item *can* go; `occupies` is what slots it *fills*. A two-handed sword has `slot_tags: ["mainhand"]` and `occupies: ["mainhand", "offhand"]` — it's equipped to the mainhand but blocks the offhand. This separates the filter from the consequence.

**`affix_pool` on template, `rolled_affixes` on instance.** The template describes the *distribution*; the instance stores the *draw*. `roll_seed` lets you reproduce rolls deterministically for audit/anti-cheat.

**`set_bonus_tag`.** Set bonuses aren't stored on the item — they're a separate document keyed by `set_id` that reads the player's equipped items and applies modifiers when enough pieces are worn. The item just declares membership.

**`bind_type`.** `bind_on_pickup`, `bind_on_equip`, `bind_on_use`, `bind_to_account`, `unbound`. Separate from `tradeable` because some items are bound but tradeable within a guild bank.

**`schema_version` on both.** Non-negotiable. You will migrate, and instances in databases will outlive template schemas by years. Version every persistent document.

**What's deliberately *not* here.** No stats computed on the template ("total DPS = ..."). No UI hints ("show tooltip in red"). No class-specific variants ("if warrior then..."). All of those are derived by the stat pipeline, UI layer, and class system respectively — keeping them out of the item doc is what lets you add a new class in patch 7.0 without touching items.

The pattern that makes this extensible: **every string that names a behavior is a registry key**. `handler: "apply_status"`, `condition.type: "target_has_status"`, `stat: "fire_damage"`, `op: "add"`, `layer: "flat"`, `bind_type: "bind_on_equip"` — all lookups into registries that plugins populate. Add a new mechanic = add a new registry entry + author items that reference it. Core engine never changes.
