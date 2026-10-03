import { describe, expect, it } from 'vitest';
import { runTwoByTwoFrameExample } from '../planning/frameExample';
import { scheduleTasks } from '../planning/scheduler';
import { createFramePreview, createFramePreviewSampler, FRAME_PREVIEW_LABEL } from './framePreview';

describe('schematic frame planning preview', () => {
  const { graph, schedule } = runTwoByTwoFrameExample();
  const row = (id: string) => schedule.tasks.find(task => task.taskId === id)!;

  it('samples exact schedule boundaries and never grants mechanical validation', () => {
    const sampler = createFramePreviewSampler(graph, schedule);
    const placement = row('place-s1-x0-y0');
    const before = sampler.sample(placement.startS! - 1).bays[0];
    const start = sampler.sample(placement.startS!).bays[0];
    const middle = sampler.sample((placement.startS! + placement.endS!) / 2).bays[0];
    const end = sampler.sample(placement.endS!).bays[0];
    expect(before.member.phase).not.toBe('active');
    expect(start.member.phase).toBe('active');
    expect(start.member.progress).toBe(0);
    expect(middle.member.progress).toBe(0.5);
    expect(end.member.phase).toBe('complete');
    const final = sampler.sample(sampler.durationS);
    expect(final.completedTaskCount).toBe(graph.tasks.length);
    expect(final.bays.every(bay => bay.releasedInPlan && bay.mechanicalStatus === 'unverified')).toBe(true);
    expect(final.label).toBe(FRAME_PREVIEW_LABEL);
  });

  it('keeps a lift reservation through the injected recovery and ends at release completion', () => {
    const sampler = createFramePreviewSampler(graph, schedule);
    const recovery = row('recover-s1-x0-y0');
    const recovering = sampler.sample(recovery.startS!).bays[0];
    expect(recovering.operation.taskId).toBe(recovery.taskId);
    expect(recovering.liftReservationHeld).toBe(true);
    expect(recovering.releasedInPlan).toBe(false);
    const release = row('release-s1-x0-y0');
    expect(sampler.sample(release.endS! - 1).bays[0].liftReservationHeld).toBe(true);
    expect(sampler.sample(release.endS!).bays[0].liftReservationHeld).toBe(false);
  });

  it('does not reveal unscheduled members for impossible or partial schedules', () => {
    const impossibleGraph = { ...graph, resources: graph.resources.filter(resource => resource.kind !== 'hoist') };
    const impossible = createFramePreviewSampler(impossibleGraph, scheduleTasks(impossibleGraph));
    expect(impossible.sample(1000).completedTaskCount).toBe(0);
    const partial = createFramePreviewSampler(graph, scheduleTasks(graph, { maxTransitions: 1 }));
    const snapshot = partial.sample(partial.durationS);
    expect(snapshot.scheduleStatus).toBe('blocked');
    expect(snapshot.bays.every(bay => bay.member.phase === 'blocked' && !bay.releasedInPlan)).toBe(true);
  });

  it('keeps object identities and reproduces all transforms after backward scrubbing', () => {
    const view = createFramePreview(graph, schedule);
    const names = view.group.children.map(object => object.name);
    expect(new Set(names).size).toBe(names.length);
    const member = view.group.getObjectByName('part:part-member-s1-x0-y0')!;
    const placement = row('place-s1-x0-y0');
    const time = (placement.startS! + placement.endS!) / 2;
    const capture = () => view.group.children.map(object => ({ name: object.name,
      visible: object.visible, position: object.position.toArray(), scale: object.scale.toArray(),
      rotation: object.rotation.toArray(), userData: structuredClone(object.userData) }));
    const snapshot = view.setTime(time);
    const transforms = capture();
    view.setTime(view.durationS);
    expect(view.group.getObjectByName(member.name)).toBe(member);
    expect(view.setTime(time)).toEqual(snapshot);
    expect(capture()).toEqual(transforms);
    view.setTime(0);
    expect(member.visible).toBe(false);
    expect(view.group.userData.mechanicalStatus).toBe('unverified');
    view.dispose();
    expect(view.group.children).toHaveLength(0);
  });

  it('uses finite absolute time and rejects mismatched graph/schedule inputs', () => {
    const sampler = createFramePreviewSampler(graph, schedule);
    expect(sampler.sample(-1).timeS).toBe(0);
    expect(sampler.sample(1e6).timeS).toBe(sampler.durationS);
    expect(() => sampler.sample(NaN)).toThrow('finite');
    expect(() => createFramePreviewSampler(graph, { ...schedule, graphId: 'different' })).toThrow('IDs differ');
  });
});
