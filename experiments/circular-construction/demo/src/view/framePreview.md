# Schematic frame preview

`framePreview.ts` adapts the existing two-storey 2 × 2 planning fixture to a
Three.js group. It owns no renderer, camera, requestAnimationFrame loop, or clock.
The host supplies one absolute planning-time value for every update.

```ts
import { createFramePreview } from './view/framePreview';
import { runTwoByTwoFrameExample } from './planning';

const { graph, schedule } = runTwoByTwoFrameExample();
const preview = createFramePreview(graph, schedule);
site.scene.add(preview.group);
// Render both strings in the host UI while this group is visible:
// preview.label: SCHEMATIC • Planning sequence • Mechanically unverified
// preview.description: explains tokens, dashed guides, and graphical reveals.
const snapshot = preview.setTime(absolutePlanningSeconds);
// site.draw() uses the existing renderer and camera.
// preview.group.visible = false switches away without destroying state.
// preview.dispose() removes its group and disposes only its own resources.
```

The group uses Z-up coordinates, spans approximately X/Y 0..6 and Z 0..7.1,
and does not change any host scene object. Mesh names derive from part IDs;
workflow and reservation object names derive from bay and lease IDs. All objects
remain allocated across updates, and their transforms depend only on sampled
time. Negative times clamp to zero; times beyond the scheduled horizon clamp to
the last scheduled completion. Nonfinite times and mismatched graph IDs throw.

Each bay has exactly one generic member token, matching the fixture's single
`frame-member` allocation. Temporary brace and climbing rail tokens use the
corresponding task/part identities. Dashed grid outlines are schematic spatial
guides and are never shown as installed stock. Seed-kit geometry is an icon for
the proposed ground seed operation, not a specified physical kit.

Amber indicates an active operation. Completed member tokens use pale teal;
completed brace and rail tokens retain their respective materials. A coral
workflow marker identifies an active recovery. A sling-shaped line represents
the timing of the lift reservation from placement start through release end,
including recovery. This is a scheduling token, not proof of hoist support.
Graphical reveals grow along each token's axis; they do not claim a robot motion
trajectory. No material is revealed for blocked, invalid, or unscheduled tasks.

`snapshot()` and `setTime()` return the same snapshot shape, including all task
phases, active task IDs, bay states, completion count, and schedule status.
`releasedInPlan` reports completion of a release task. Completing a verification
or release task never changes `mechanicalStatus: 'unverified'`.

`createFramePreviewSampler(graph, schedule)` exposes the same sampling without
creating geometry. The adapter deliberately rejects graphs outside the named
eight-bay fixture rather than inventing geometry for unrelated task graphs.

Validation: `npm test -- src/view/framePreview.test.ts` exercises exact time
boundaries, recovery reservation timing, incomplete schedules, backwards
scrubbing with stable object IDs, disposal, and invalid input. `npx tsc --noEmit`
checks the module with the full demo.
