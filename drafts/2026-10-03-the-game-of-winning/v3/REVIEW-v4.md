# The Game of Winning, v4: where it stands

Ren rated v3.1 at 3/10 and set a goal of 9.5. This note records what changed from v3.2 to v4.22 (artifact version 34, 4:00), what I checked and how, and what still keeps it short of 9.5.

## The story, as the cards now tell it

| Year | Card |
|---|---|
| 2026 | The race for super intelligence. *Twelve players.* |
| 2046 | Compute passes a terawatt. |
| 2068 | Compute uses as much energy as all of humanity did in 2026. |
| 2097 | One player left. The planet can no longer shed its heat. |
| 2113 | The oceans become the coolant. |
| 2132 | The Earth is not enough. |
| 2291 | The Sun is enclosed. |
| then | One star is not enough. *The probes leave.* |
| +12,000 years | The star goes dark. |
| +2 million years | Every star in the galaxy is taken. |
| then | Nothing is left to win. |
| then | Light-years apart, its copies become rivals. *212 players.* |
| end | THE GAME OF WINNING |

Two cards were added for the two turns a viewer could miss:
- **2097:** the race is won, and the expansion does not stop.
- **The split:** the light-speed mechanism that turns one winner into many rivals.

The player count on the panel agrees with every card.

## What changed

- **Ground scenes, rebuilt.**
  - **West Texas at dusk:** a road into the campus, a fence, and aviation lights blinking in sync. A launch climbs east, and its plume opens into a sunlit bell.
  - **The dry Mediterranean:** a glass dome 5 km across and 900 m high, with a garden city inside, after Ren's ruling that the domes must be city sized. Around it: salt crust, the old continental slope, steam columns, and the compute halls kept back.
  - **Two suns:** a dim day lit by the blazing Moon, with the enclosed Sun small and red. Two figures in long coats; one points at the Moon.
  - **The last sky:** a photographic Milky Way whose stars redden and go out, over the warm-lit city.
- **Earth.**
  - Territories fill in over two decades instead of all at once.
  - Clouds look natural.
  - Solar fields show no grid.
  - The thermal view builds from red to white-hot, with cold cloud tops.
  - The seas retreat between 2104 and 2140 and leave salt and silt. Before, they stayed blue until the 2180s, because most of the ocean map is deep.
  - Constellations show as shells that glitter past the terminator.
  - Seawater plumes pulse.
- **The Sun.**
  - A real disc.
  - The swarm is a shell at 3.6 solar radii, closing into an ember in the infrared.
  - Mercury and Venus are flung off into rings along their orbits.
  - The camera rides the relay beam to the Moon.
  - Once the Sun is enclosed, the Earth's day goes out.
- **Between the stars.**
  - The camera picks out one probe from the ember and rides it out.
  - The transit is still, with the fleet's drive glows slowly drawing apart.
  - At the cell: the seed's visible descent, the crust flung into a ring, the same shell closing over the star.
- **The galaxy.**
  - An open, barred, two-armed spiral.
  - A continuous climb out from the dark star, with the Sun and the first star taken named on the way.
  - A slow push through the efficient galaxy into the split.
  - Territories with coastline borders, from one precomputed map.
  - Struck stars flare and cool to embers; dead regions keep a faint glow.
  - The last two strike each other at once; then the whole galaxy goes out.
- **Sound.**
  - A chord progression per act.
  - A felt-piano motif at every wall, in each act's key. It breaks off at "Nothing is left to win" and returns once under the title.
  - Detuning unisons at the split.
  - About −18 LUFS.
- **Type.**
  - Larger throughout.
  - Dark ink over the white basin.
  - Callouts placed on what they name.
- **Performance.**
  - Every scene runs at about 4–16 ms a frame: one program per ground mood, noise from textures, precomputed tables, and reduced-size rendering for the heavy scenes.
  - Earlier timings were measured at the wrong times; fixed.

## How it was checked

- Contact sheets of the whole film, every 2.5–4 s.
- Full-resolution stills of every chapter, and crops of details.
- GPU timings, both headless and in the live pane.
- Every frame rendered in the live page with no errors.
- For the soundtrack: spectrograms, loudness, and band-energy measurements, showing the motif 8–17 dB above its surroundings at every wall.

## What still keeps it short of 9.5

- **The sound has not been heard.** It is checked only as images and numbers, and it is still synthesis. A listen is the most valuable next check.
- **The heavy ground scenes render at 50–66% of full size** and are slightly soft next to the rest.
- **The figures and the city are simple geometry:** convincing as silhouettes and from a distance, not up close.
- **The war's beams are straight lines.** They read clearly but plainly.
- **Taste calls I made without Ren:**
  - the city-dome design;
  - the two new cards' wording;
  - the open-spiral galaxy;
  - keeping the Mauritanian sand seas, which are real geography.
