# What v3 is, honestly

Ren: good job, but still very primitive. Understand what you built and how good or bad it is; make it significantly better and elegant; make sure viewers can follow the whole narrative; 5 minutes is the upper bound.

## What works

- **The real Earth at night**, with amber industrial light spreading out of the real data-centre regions. Of everything in the film, this is the image that most reads as "this could happen".
- **A few true continuous moves:**
  - the planet turning under the night-side camera;
  - the dive to the campus;
  - the flight past Venus to Mercury;
  - the pull-back from the dead star to the galaxy.
- **Mercury's scar with its factory lights**, the swarm closing around the Sun, the infrared ember, the relay beam to the Moon, the galactic front, and the war's beams.
- **It runs in real time** at 60 fps, it scrubs, and the sound loads without blocking.

## What doesn't

1. **A viewer can't tell who is doing this, or why.** The only hint of a cause is a number labelled POWER. The *game* is invisible until the split, three and a half minutes in. Worse, the film opens on the words "super intelligence", so a viewer will conclude that AI is the cause. Ren's title says the opposite: the game is the cause.
2. **The cards state numbers, not meaning.** "10 PW" says nothing to anyone. The walls, the reason each step forces the next, are never said in plain words.
3. **The ground scenes look like a 1990s 3D demo:**
   - box buildings and lollipop trees;
   - a uniform white haze;
   - figures like pills.
   They are meant to be the human heart of the film, and they are its weakest images.
4. **The Earth's surface:**
   - The clouds are cotton balls.
   - The industrial light is a uniform carpet with noisy edges.
   - The thermal view is a garish purple and salmon.
5. **The screen is crowded and flat.** The panel, instrument label, callouts, cards and words all compete at one size. There is no hierarchy, so nothing leads the eye.
6. **The pacing drags in places:**
   - the Earth chapter runs 85 s;
   - the transit and the edge are filler;
   - the efficient galaxy holds 13 s without new information.
7. **The sound is placeholder synthesis:** beeps and bare tones, no space, no reverb, no music.
8. **The galaxy is a point cloud with a glow.** It is not yet majestic, and the dead domains read as blotches.
9. **The motif cuts to the dome land without orientation.** Nothing tells the viewer it is the same place, years later.

## What v4 changes, in order of impact

**A. The game becomes visible from the first frame.** This is the narrative spine.
- The panel shows PLAYERS from 2026, next to COMPUTE (renamed from POWER).
- On the map, rival players' territories glow in distinct quiet tints. Each player is a mosaic of sites across continents, not a country.
- As the race goes on, players are absorbed and their light takes the winner's amber. The counter falls from 12 to 1 by 2097 (card: "One player left").
- The winner keeps playing the same game, through the Sun and the galaxy.
- When nothing is left to win, the light splits again into the same tints, and the players destroy each other. 12 → 1 → 212 → 0.

Viewers no longer need narration to see that this is a race, that winning it changes nothing, and that the game ends in nothing.

**B. Ten short lines carry the story.** Cards say the wall in plain words, with the number small underneath:

| | |
|---|---|
| 2046 | Compute passes a terawatt. |
| 2068 | Compute uses as much energy as all of humanity did in 2026. |
| 2097 | One player left. The planet can no longer shed the heat. |
| 2113 | The oceans become the coolant. |
| 2132 | The Earth is not enough. |
| 2291 | The Sun is enclosed. |
| +12,000 years | One star is not enough. |
| +2 million years | Every star is taken. |
| then | Nothing is left to win. |
| end | The Game of Winning |

**C. Location stamps** orient every cut: West Texas · The dry Mediterranean · The same dome · Another star · The same dome, two million years later.

**D. Elegance:**
- **HUD:** one quiet panel with a clear hierarchy. YEAR is large; COMPUTE, PLAYERS and POPULATION sit small beneath it. The instrument label and location go bottom-left, the cards centre-low, and callouts stay rare.
- **Earth:** a real NASA cloud map instead of procedural cotton; industrial light that follows settlements, with clean edges; a restrained thermal palette.
- **Ground:** soft shadows, ambient occlusion, real foliage, ribbed halls with rooftop plant, steam lit by the sun, and figures with human proportions.
- **Galaxy:** colour variation and a fuller glow.

**E. Pacing:** about 4:20. Trim the Earth chapter, merge the edge into the efficient galaxy, shorten the transit. A time map lets the film compress or drop stretches without rewriting every scene.

**F. Sound:**
- reverb, so every sound has space;
- soft filtered ticks instead of beeps;
- a slow, darkening chord pad under the whole film;
- the events stay.

## How I will work

The dev server (`.claude/launch.json` → `film-dev`, http://localhost:5291) reloads on every save and resumes at the same second, so Ren can watch it change. `?t=` jumps anywhere; D shows a readout. For my own checks, `node render.mjs --sheet a,b,step` renders a stretch of the film as one contact sheet in seconds. MP4 export stays available but is no longer used.
