# The Game of Winning: plan for v3

Ren on v2: a lot simply doesn't make sense, especially the rendered lines and the transitions between scenes. And: why MP4, why not keep it in the browser? This plan answers both. v2 stays committed as it is (`7f52c45`).

## 1. Why v2 doesn't make sense

**The lines mean nothing to a viewer.** In the screenplay "the line" was the logic. On screen it became abstract strokes:
- a web of straight segments across continents and oceans;
- arcs scratched past the Earth;
- two tracks running off-screen;
- an underline that bends into a planet.

None of it corresponds to anything physical, so it reads as a "plexus" stock effect. The viewer asks what they are and gets no answer. Only the beams make sense, because a beam is a real thing.

**The scenes are separate sets joined by cuts.** Each scene builds its own little world and its own camera: Earth at the origin here, Mercury at the origin there, a different Sun in each. Shots jump in scale, place and direction with no motion connecting them. The screenplay promised one outward journey, but the build delivered about 25 unrelated shots. With no sense of where one thing sits relative to another, the logic can't be followed.

**The viewer is never told what they are looking at.** The thermal view, the infrared Sun and the orbital shells appear without a word. A switch of sensor looks like a change of colour scheme. The register of evidence only works if it is announced, the way real imagery is captioned.

**The ground scenes look drawn.** The dome, the campus and the night sky are flat 2D shapes, with no perspective, light or air. They are the human anchor of the film, and they are the least real things in it.

**Some scenes are filler or confusing:**
- The opening spends 12 seconds on black and a gimmick.
- The edge shot is unclear.
- The alien planet is visibly Mercury recoloured.
- The swarm reads as a ball of yarn.

## 2. Why MP4, and why the browser instead

I rendered MP4 for two reasons. v2 moves about half a million points through JavaScript on every frame, which is too slow to play in real time. And a file plays anywhere: phones, uploads, festivals. Neither reason has to hold.

**v3 is a real-time film in the browser.** The page is the film. It plays at 60 fps, you can scrub to any second, and it shares as a link.

This needs one architectural change: the animation moves onto the GPU. Every star, collector, satellite and probe is uploaded once, with its own parameters: its orbit, the moment it appears, the moment it dies. A shader computes where it is at time *t*. Each frame then sends only a handful of numbers, so millions of points become cheap.

The soundtrack plays from a file rendered from the same synthesis code. The same page can still export an MP4 for platforms that need a file, but that is a by-product.

## 3. Five principles

1. **Everything visible is a physical thing.** No decorative lines. A line appears only where something really is a line: a beam, a launch plume, a stream of material, a probe's exhaust.
2. **One world, one camera.** The solar system is a single coordinate space: the Earth, the Moon, Venus, Mercury and the Sun in their places, with sizes exaggerated but positions consistent. The galaxy is a second space, and the Sun's place in it is fixed. Transitions are camera moves or motivated cuts, never arbitrary ones.
3. **The logic is shown as light and land, not strokes.** Amber means artificial light and heat, at every scale: city lights turning industrial, deserts darkening under solar glass, factory lights across Mercury's scar, waste heat glowing in infrared. This replaces "the line" as the thread, and every instance of it is physically real.
4. **Evidence grammar.** A small instrument label states the current view: NIGHT LIGHTS, VISIBLE, THERMAL INFRARED, MID-INFRARED, GROUND. Sparse callouts name each new thing once, for two seconds: "orbital data centres", "mass drivers", "collector swarm", "laser relay", "self-replicating probe". They name *what*, never *why*. The logic still needs no explanation.
5. **Real air on the ground.** The ground scenes are rebuilt in 3D (ray-marched): real perspective, a glass dome that refracts and reflects, a garden and people inside it, cracked salt flats, rows of compute halls receding into haze, steam columns with volume.

## 4. How the scenes connect

The transitions are of five kinds:
- **camera moves** within one world;
- **sensor switches**, on the same shot;
- **descents and rises** through the atmosphere, with a short haze dip;
- **following an object**: a rocket, a beam, a probe;
- **the sky motif**, a motivated cut to the same dome, bridged by sound.

| Time | Scene | What we see | Into the next |
|---|---|---|---|
| 0:00–0:07 | **The word** | Black. "super intelligence", captioned UN General Assembly, 22 September 2026, or the real clip once sourced. | The caption dissolves into the night Earth. |
| 0:07–0:30 | **Today → 2046** | One continuous orbital shot. The planet turns under the camera in time-lapse, so the Americas, Europe and Asia pass. Real data-centre regions flare (callout). Then industrial amber light spreads from them across the continents. On the day side, deserts darken under solar fields and glint. | The camera dives toward a Texas campus. |
| 0:30–0:38 | **Ground, 2050** | The campus at night (3D): halls, red aviation lights, satellite trains, a launch rising. | The camera follows the rocket up; its flame carries the dissolve to orbit. |
| 0:38–0:48 | **Orbit, → 2068** | The rocket's light joins thickening shells of orbital compute (callout). Solar glass spreads across the day side. | Same shot; the sensor switches. |
| 0:48–0:58 | **Thermal, → 2097** | Label THERMAL INFRARED. Heat islands glow and spread; the population turns. | The sensor switches back as the camera glides to the limb. |
| 0:58–1:12 | **The oceans, → 2113** | Vapour columns off the limb (callout "mass drivers venting seawater"). The seas retreat from the shallows first, following the real bathymetry, until the basins are grey. | The camera dives into a dried basin. |
| 1:12–1:24 | **The dome, 2120** | Ground (3D): the dome, its garden and people, compute halls to the horizon, steam columns, "PROGRESS". | Tilt up into the white sky, then a cut to high above looking down. |
| 1:24–1:32 | **Earth entire, 2132** | A pull-back to the whole Earth, wrapped in amber, its seas grey. | The camera turns sunward and flies inward: one continuous move. |
| 1:32–1:52 | **Mercury** | Venus passes; Mercury comes up ahead. The scar spreads, and the mass drivers stream ore into a ring. | The camera swings to Venus. |
| 1:52–1:58 | **Venus** | The scar tears through the clouds; a second ring. | The camera pulls back to the inner system. |
| 1:58–2:12 | **The swarm, → 2291** | Ring material becomes collectors: millions of them filling a shell. The Sun's disc darkens; the label switches to MID-INFRARED; an ember. | A beam leaves the swarm, and the camera follows it. |
| 2:12–2:18 | **The relay** | The beam reaches the Moon, which blazes (callout). | A motif cut to the same dome. |
| 2:18–2:24 | **Two suns** | Ground (3D): the blazing Moon, the dim red Sun, two people looking up. | A cut to the swarm. |
| 2:24–2:36 | **Launch and transit** | Probes leave (callout). The camera picks one and follows it through interstellar space as the years jump. | It brakes into another star system. |
| 2:36–2:52 | **The cell** | Landing; the spread "like a cell, a virus"; the planet comes apart; collectors wrap the star; the star goes dark. "A few thousand years." | A continuous pull-back from the dark star. |
| 2:52–3:16 | **The front** | The star joins thousands going dark. The galaxy is revealed with the front spreading from the Orion Arm; the label switches to INFRARED. | A motif cut to the dome. |
| 3:16–3:23 | **The last sky** | Ground (3D), night: the stars go out one by one. | Tilt up into the black, then rise into the galaxy. |
| 3:23–3:36 | **Efficient** | The red galaxy, still, as the word returns. | Continuous camera. |
| 3:36–4:32 | **Edge, split, beams, last light** | As in v2, on one continuous galaxy camera. The edge is shortened; probes there are moving points, not lines. | |
| 4:32–5:00 | **Black, title** | | |

## 5. Visual upgrades

- **Earth's growth is a texture, not a graph.** A growth-year map (2048×1024) is computed once from the real night lights, the real data-centre regions and land/sea. It holds the year each place becomes industrial. The planet shader uses it two ways. At night it shows amber light in fine settlement-scale grain. By day it shows solar glass that darkens deserts and catches the sun as glints.
- **The seas retreat by depth.** The Blue Marble topography-bathymetry map shades the ocean by depth. The shallows dry first, the coasts move out, and the basins whiten to salt.
- **A cloud layer** on the day side, for realism.
- **The thermal palette is redone:** cold oceans dark, heat islands bright, and labelled.
- **The swarm is a real swarm.** Millions of collectors in hundreds of orbital planes make an even, glittering shell that visibly darkens the Sun, fed by material streams from the Mercury and Venus rings.
- **The cell's planet** uses a different surface, so it is not recognisably Mercury.
- **The galaxy** gains a soft diffuse glow and dust lanes under the stars, so it reads as a galaxy rather than a point cloud.
- **The ground scenes** are one ray-marched shader with four moods: campus at night, white day, two suns, and the night the stars go out.

## 6. Sound

The design stays: the compounding clock, the rising tone, the scene events, the late impacts, the silence. It is re-timed to v3 and gets bridges across the motif cuts, so sound carries the viewer where the picture cuts. It plays from a file in the browser.

## 7. Order of work

1. **Engine:** GPU-side animation; one world per act; spline camera paths; the real-time player page (controls, chapters, fullscreen, sound); instrument labels and callouts.
2. **Earth:** the growth texture, solar glass, clouds, bathymetric retreat, the continuous time-lapse shot, the descents and the rocket follow.
3. **Ground:** the ray-marched shader with its four moods.
4. **The Sun:** the single solar-system flight, the GPU swarm, the material streams, the beam follow.
5. **The galaxy:** the probe follow, the cell, the pull-back, the diffuse glow and dust, a continuous camera through the war.
6. **Sound:** re-timed and bridged; rendered to a file.
7. **Review:** play the whole film in the browser at real speed; check frame rate, every transition, legibility and timing; fix.
8. **Publish:** the real-time page as an artifact, plus an optional MP4 export.

v2 stays as it is. v3 is built in `v3/`, reusing the engine and the assets.
