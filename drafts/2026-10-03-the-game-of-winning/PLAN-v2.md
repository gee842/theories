# The Game of Winning: plan for v2

Ren's verdict on v1: the idea and the representation are interesting, but the film is far from the conversation and not realistic. The quality, aesthetics and style are weak, the pace is too slow, and many of his points are missing. His definition: **realistic means that viewers believe it is a realistic speculative future, a demonstration of what happens if we follow the current trajectory.** This plan answers that. v1 (`SCRIPT.md`, `film.html`) stays as the archived first cut. v2 will be built in `v2/`.

## 1. What v1 got wrong

- **I replaced the conversation with my own inventions:** a score overlay, four starting points that became four factions, stick figures, and a "first frame" coda. I also anonymised the two real-world hooks Ren asked for, Trump saying "Superintelligence" and Musk's orbital data stations.
- **The core insight never appeared.** In the talk, the von Neumann machine is an *economic* logic ("要把它这种冯·诺伊曼机理解成一种经济逻辑"), and the energy bodies serve "corporate interest". v1 showed physics and no economics.
- **Every step was an icon, not a mechanism.** Squares doubled and hexagons spread. Nothing showed why each step follows from the last, so nothing felt inevitable.
- **The style read as a diagram, not a world.** It was flat, sparse and toy-like, with slow zooms and one idea per long shot.
- **Two corrections to what I said after v1:**
  - *Venting the oceans is physically coherent.* Mass thrown off the planet carries its energy away. At 10¹⁷ W the oceans would last about 29,000 years. On the growing trajectory they are spent around 2191 (§3).
  - *"星系" in the talk means star systems.* "一个个的戴森球之间，它又会开始分裂" and "从这个银河系统扫了一遍" put the war between Dyson spheres inside our galaxy. v1 had the scale right. My claim of "galaxies firing at galaxies" misread the talk.

## 2. Three rules for "realistic"

1. **The present is real.** Real clips, real places, real numbers, and real projects as they have been publicly announced. Real people appear only in real footage saying real words. No future words are put in anyone's mouth.
2. **The future is the present growth rate, continued.** Every date and number on screen comes from one stated assumption, computed by one script: data-centre power keeps its official 2024–2030 growth rate of 14.7% a year, doubling every 5.1 years, until physics stops it. Nothing is dated for drama.
3. **Every step is a known engineering idea.** Hyperscale campuses, orbital compute, laser power beaming, the disassembly of Mercury into a Dyson swarm (Armstrong and Sandberg 2013), self-replicating probes, and a Dyson swarm used as a weapon (the Nicoll-Dyson beam). A careful viewer should find nothing to dismiss as fantasy.

## 3. The spine: the logic hits a wall and consumes what lies beyond it

Ren's mechanism, compounding inside the game of winning, becomes the plot. Each physical limit becomes the next frontier, and each frontier is one of his beats. The dates are computed (`trajectory.py`). They are the film's chapter cards.

| Year (computed) | Wall | What the logic consumes | Ren's words |
|---|---|---|---|
| 2026 | none yet | today's campuses and grids | "Superintelligence" (the Trump clip) |
| 2046 | **power** (1 TW of compute) | land, gas, reactors, grids | "地球的表面，出现了各种各样的 super data center" |
| 2068 | compute alone equals all human energy use today | low orbit | "从马斯克的轨道数据站开始" |
| 2097 | **heat**: waste heat ≈ 2 W/m², half a CO₂ doubling | the climate | "随着地球需要的降温的能力越来越高" |
| 2113 | Kardashev I (10 PW), waste heat ≈ 20 W/m² | **the oceans**, vented to space as the heat sink | "把海洋变成高温蒸汽，喷射到外太空" |
| 2113–2191 | Earth uninhabitable outside enclosures | people | "人类只能生活在一些小的泡泡的温室里面……然后这就是 progress" |
| 2132 | all the sunlight Earth absorbs | **Mercury and Venus** | "首先射到了水星和金星……不断地把这两颗行星拆解" |
| ~2191 | oceans spent | (done) | "在把这些水全部都 consume 完前，造出最多的算力，从而它可以去制造它的戴森球" |
| 2291 | **the Sun**: its whole output | the Sun itself | "拆解了之后开始造戴森球" |
| 2291 | getting power back to Earth | the Moon, as a relay | "以光速地往月球传输，做一个中转站……月球在白天也有了一颗太阳般的…" |
| +10⁴ yr | **one star is not enough** | other stars | "把各种各样的 space probe，射进了银河系" |
| +10⁶ yr | the galaxy | every star | "像一个生物、像一个细胞、一个病毒一样"; "整个银河就一个个全都灭掉" |
| ~2×10⁶ yr | **nothing left outside** | each other | "当这种斗争扩张没有了之后"; "直接把恒星作为一个动力源" |
| end | | | "然后就没有然后了" |

Beyond 2291, light speed sets the pace, not the growth rate. At a tenth of light speed the galaxy takes about a million years, which matches "几百万年".

## 4. Every point from the conversation, and where it goes

v1 missed or weakened the items marked ✗.

| Point (story1 unless noted) | v1 | v2 |
|---|---|---|
| Open on Trump saying "Superintelligence"; the logic needs no explanation | ✗ anonymised | 0:00, real clip |
| Pull back from the Earth view: things appear everywhere, super data centers on the surface | weak | 0:10–0:30, real night Earth, real campus locations |
| One day it launches things outward, starting with Musk's orbital data stations | ✗ unnamed | 0:30–0:42 |
| Rising energy use, the cooling problem, oceans vented to space (生态文明) | weak | 0:42–1:10 |
| The logic must expand itself, consumes Earth, makes the most compute before the water runs out, for its Dyson sphere (生态文明) | ✗ | the 2113→2191 chapter, with the link made explicit by the dates |
| Population falls; a few live in beautiful glass domes and think giving up Earth is better; "这就是 progress"; Silo, a solarpunk *Fallout* (生态文明) | ✗ population; dome only | 1:10–1:22 |
| Mercury and Venus first; massive automated engineering; both taken apart | weak | 1:22–1:50 |
| The Dyson sphere | weak | 1:50–2:05, with visible and infrared views |
| Energy beamed at light speed to the Moon as a relay; the Moon like a sun in the daytime sky | stick figure | 2:05–2:15 |
| Probes fired into the galaxy | yes | 2:15–2:25 |
| Cosmic cancer's real form: a small ship lands, uses local resources, spreads like a cell or virus; automated facilities build more facilities; the planet comes apart; its "automated army" makes it Dyson material; the star eaten "在几千年内……就不见了" | weak | 2:25–2:50, the most detailed sequence in the film |
| Over millions of years the galaxy goes out, star by star | yes | 2:50–3:20 |
| "更高效率的能源体", yet "也没有在做什么", serving "corporate interest" | ✗ economics | 3:20–3:32, see §5d |
| The spheres split, because the logic is outward struggle | yes | 3:42–3:52 |
| Stars used directly as power sources for the beams | ✗ | 3:52–4:25, the Nicoll-Dyson beam |
| From the other side, mutually destructive beams sweep the galaxy; then nothing | yes | 4:25–4:40 |
| Title *The Game of Winning*; superintelligence is not necessarily the cause; the von Neumann machine as economic logic | title only | carried by §5c and §5d, not by words |
| Line animation, five minutes, "只要你能把意思表达明白了" | yes | lines kept, as the logic itself (§5c) |
| Greg Egan's frozen humanity (生态文明) | none | **left out**: it is borrowed, and it would dilute the film. Ren can overrule this. |

## 5. Representation, drawn from Ren's own images

**a. One outward journey.** "从地球视角向外放" becomes the film's camera. Shots get wider and years get longer, from a podium to a planet to a galaxy. A continuous outward motion is Ren's image, and it also fixes the pacing: the film never stands still.

**b. The cancer has one shape at every scale.** Ren's figure is a cell or a virus spreading over a surface. The same growth front, dense, branching and bright at its edge, appears as data-centre clusters across a continent, mining scars across Mercury, collectors around the Sun, and the colonisation front across the galaxy. Night lights seen from orbit already look like a colony on a dish, so the first instance is real. The viewer should recognise the same thing growing four times without being told.

**c. The world is realistic; the logic is drawn in lines.** Ren chose line animation. v2 gives the lines a meaning. Planets, the Sun and the galaxy are rendered as realistically as the engine allows. The logic is thin bright line: transmission lines, launch tracks, mass-driver streams, power beams, probe paths, and finally the weapons. The lines thicken until the world is mostly line. Then the lines turn on each other, and then nothing is left. This is where Ren's representation and his insight meet: the game of winning is the line, and the world is what it eats.

**d. The economic logic is shown on instruments, not stated.** A spare instrument panel, styled like telemetry, carries what words would otherwise explain:
- **YEAR**, with a single **TODAY** tick as it passes 2026. Viewers see where real data ends and projection begins, and nothing else changes at that moment. That moment is "the current trajectory" made literal. *(proposal)*
- **POWER**: the compute the logic commands, in watts, from today's real figure upward.
- **POPULATION**: real at 8.2 billion, then falling quietly while power rises. When the logic leaves Earth, the line drops off the panel, because people no longer count in the game. That is Ren's "人类的数量大幅下降" without a word spoken. *(proposal)*
- **For "corporate interest"**, one restrained device. My recommendation: at the dead, efficient galaxy, the opening's real voice returns, slowed, saying its one word. The alternative is a quarterly growth figure that keeps ticking at cosmic timescales. *(Ren chooses)*

**e. No narration and no explanation.** The only words are the real voices, the panel, the chapter years, and the title. The only invented on-screen word would be "PROGRESS" over the domes, which is Ren's own line. *(proposal)*

## 6. Look

The look is the register of evidence. The film looks like the instruments that already report on the world, so the future inherits their credibility:
- **Today:** real news footage.
- **The Earth chapters:** satellite night imagery, then thermal false-colour as the heat wall arrives.
- **The solar system:** planetary-science visualisation, with the realistic surfaces of Mercury, Venus, the Moon and the Sun.
- **The galaxy:** a visible-light survey that turns into an infrared survey as the stars are enclosed. This is how astronomers actually search for Dyson swarms.

Black space with physically motivated light. One artificial colour for the logic's lines; sodium amber, the colour of night lights, is the leading candidate. A thermal palette for heat and infrared. Telemetry typography: a precise monospace for the panel and one clean sans for the chapter years and the title. Restrained bloom, depth and grain. Density everywhere: hundreds of thousands of stars, collectors and satellites rather than v1's hundreds.

Reference points for the register, not for copying:
- the Eames *Powers of Ten*, for the outward camera;
- NASA's *Black Marble* imagery and science visualisations, for the surfaces;
- *Timelapse of the Future*, for a deep-time film people take as real.

## 7. Pace

- Five minutes, about 45 shots, averaging about 6 seconds. v1 had about 20 shots, averaging 15 seconds.
- Shot length tightens through the Earth chapters (8 s → 3 s) and opens up for two held images only: the cell, and the dead galaxy.
- The beams are a fast montage. Silence lasts four seconds.
- Time on screen accelerates with the camera's distance: two decades per ten seconds at first, a century per ten seconds at the Sun, a million years per thirty seconds at the galaxy.

**Sound: the compounding clock.** One click per doubling of POWER, every 5.1 years. In the Earth chapters the clicks accelerate as the years compress, until at the Sun they fuse into a tone: compounding made audible. In the galaxy, growth is no longer the limit, and the tone flattens into a drone ("也没有在做什么"). At the split it fractures. Then the beams, then silence. Real voices only in the opening and the reprise. If Ren's friend scores it with music, the clock is the tempo map.

## 8. Beat sheet (5:00)

| Time | Shot(s) | Panel |
|---|---|---|
| 0:00–0:10 | **Real.** Trump: "…Superintelligence." Then 3–4 real present-day shots, ≤1.5 s each: a campus under construction, GPU halls, a Starship launch, gas turbines. | none |
| 0:10–0:16 | Night Earth from orbit, real imagery. Real data-centre regions pulse. | 2026 · TODAY · 62 GW · 8.2 bn |
| 0:16–0:30 | The colony spreads along the grids; gas and reactor sites light up beside it; transmission lines thicken. 3 shots: wide, continental, wide. | → 2046 · 1 TW |
| 0:30–0:42 | Launch tracks stitch Earth to orbit; compute constellations wrap the planet, radiators glinting. 2 shots. | → 2068 · 19 TW |
| 0:42–0:55 | The view switches to thermal: the night side glows. Population starts to fall. 2 shots. | → 2097 · 1 PW |
| 0:55–1:10 | Coastal mass drivers hurl seawater off the planet; white plumes at the limb; rain belts for millennia; the seas recede. 3 shots. | → 2113 · 10 PW |
| 1:10–1:22 | A satellite zoom to a glass dome on a dry seabed, among compute fields and steam columns. "PROGRESS". 2 shots. | population in the millions |
| 1:22–1:30 | Launch tracks reach for Mercury and Venus. | 2132 · 120 PW |
| 1:30–1:50 | Mercury: a mining scar spreads like a lesion, mass drivers stream ore into orbit, the planet unravels into a ring. Venus: its clouds torn open, then the same. 3 shots. | → 2190s; population leaves the panel |
| 1:50–2:05 | Collectors fill the orbits and the Sun dims. Then the infrared view: the Sun as a dull ember. 2 shots. | 2291 · 3.8×10²⁶ W |
| 2:05–2:15 | A beam from the swarm to the Moon, which blazes. From a dome: a blinding Moon in the daytime sky, a dim red Sun. 2 shots. | |
| 2:15–2:25 | Thousands of probes launched; the camera pulls out until the solar system is a point in the Orion Arm. 2 shots. | |
| 2:25–2:50 | **The cell.** A seed brakes into another system, lands, and spreads like a cell or virus; the planet comes apart; swarms wrap the star; the star vanishes from the sky within a few thousand years. 4 shots, the most detailed sequence. | +10⁴ yr |
| 2:50–3:20 | One continuous pull-back: the front crosses the galaxy and stars go out in visible light while the galaxy glows in infrared. 1–2 shots. | → +2×10⁶ yr · 10³⁷ W |
| 3:20–3:32 | The dead, perfectly efficient galaxy. The "corporate interest" device (§5d). | power holds, unchanging |
| 3:32–3:42 | Probes reach the rim; the nearest galaxies lie millions of light years out. | |
| 3:42–3:52 | The single glow fractures into rival domains. | POWER splits into rivals |
| 3:52–4:25 | Swarms focus their stars into beams. Each volley takes millennia to cross, so the year counter jumps. Swarms die; from the other side, a sweep crosses the galaxy. 5–6 shots. | rivals fall |
| 4:25–4:33 | The last two fire at each other. Darkness. | 0 W |
| 4:33–4:40 | Black. Silence. | |
| 4:40–5:00 | THE GAME OF WINNING. | |

## 9. How it gets made

- **Engine.** Raw WebGL2 with my own shaders, deterministic in time, no libraries. It includes textured planets with day, night and thermal shading, atmospheres, instanced particles at hundreds of thousands, line geometry with glow, and bloom. Headless Chrome renders it on the M2 Max GPU (checked: ANGLE Metal, float render targets), through the existing `render.mjs` pipeline.
- **Numbers.** `trajectory.py` is the single source of every number and date on screen. Its assumptions are listed and its results checked, in the same discipline as the paper's `checks_*.py`.
- **Real imagery.** Public-domain NASA maps: Black Marble night lights, Blue Marble, MESSENGER's Mercury mosaic, Magellan's Venus, LRO's Moon, an SDO solar image. About 40–60 MB in total, downloaded only with Ren's OK. Real data-centre regions from public reporting, checked before use.
- **Real clips.** The opening clip and the present-day b-roll have to be sourced by Ren or his friend, including rights. I cannot download or verify video. I could not confirm that Trump has said the word "superintelligence" on camera, so that needs checking first.
- **Four checkpoints:**
  1. Ren approves this plan and the decisions below.
  2. Six style frames in the new engine: night Earth with the colony, the thermal Earth and the vents, Mercury unravelling, the swarm in visible and in infrared, the cell, the beams. The look is approved before anything is animated.
  3. An animatic at full speed with the clock sound.
  4. The final render, with the real clips cut in.

## 10. Decisions for Ren

1. **The opening clip.** Who sources it? If no clip of Trump saying "superintelligence" exists, what replaces it: a montage of other leaders saying it, or a different Trump line on AI?
2. **My proposals:** the TODAY tick, the POPULATION line that falls and then leaves the panel, the one word "PROGRESS". Keep or cut each.
3. **"Corporate interest":** the returning voice (my recommendation) or the quarterly figure.
4. **NASA imagery:** OK to download the public-domain maps (about 40–60 MB)?
5. **The ending:** v2 follows the talk, black and then the title, with no coda. Confirm.
