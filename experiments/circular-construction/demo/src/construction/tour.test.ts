import { expect, it } from 'vitest';
import { buildConstructionPlan } from './runtime';
import { advanceTour, buildTour } from './tour';

it('keeps the whole history contiguous and gives a real beam delivery time for close inspection', () => {
  const plan = buildConstructionPlan(), tour = buildTour(plan);
  expect(tour[0].start).toBe(0);
  expect(tour[tour.length - 1].end).toBe(plan.duration);
  for (let i = 1; i < tour.length; i++) expect(tour[i].start).toBe(tour[i - 1].end);
  const focus = tour.filter(s => s.partId);
  expect(focus.length).toBe(4);
  expect(new Set(focus.map(s => s.partId)).size).toBe(1);
  const mission = plan.missions.find(m => m.partId === focus[0].partId)!;
  expect(focus[0].start).toBe(mission.pickup);
  expect(focus[focus.length - 1].end).toBe(mission.returned);
  expect(focus.reduce((n, s) => n + s.seconds, 0)).toBeGreaterThanOrEqual(50);
});

it('does not skip a slow handoff when a render tick crosses from an accelerated span', () => {
  const spans = [{ start: 0, end: 10000, seconds: 1 }, { start: 10000, end: 10036, seconds: 12 }];
  const one = advanceTour(spans, 0, 1.5);
  const split = advanceTour(spans, advanceTour(spans, 0, .8), .7);
  expect(one).toBeCloseTo(10001.5, 7);
  expect(split).toBeCloseTo(one, 7);
});
