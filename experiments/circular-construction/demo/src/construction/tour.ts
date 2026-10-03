import type { ConstructionPlan } from './types';

export interface TourSpan { start: number; end: number; seconds: number; carrierId?: string; partId?: string }
const durations: Record<string, number> = { empty: 3, arrival: 14, bootstrap: 9, foundations: 24, 'first-frame': 35, climbing: 25, swarm: 105, completion: 90, inspection: 10, recovery: 25, departure: 9, complete: 3 };

/** Presentation pacing only: every span advances the same chronological site history. */
export function buildTour(plan: ConstructionPlan): TourSpan[] {
  const phases: { phase: string; start: number; end: number }[] = [];
  for (const stage of plan.stages) {
    const last = phases[phases.length - 1];
    if (last?.phase === stage.phase) last.end = stage.end;
    else phases.push({ phase: stage.phase, start: stage.start, end: stage.end });
  }
  const parts = new Map(plan.parts.map(p => [p.id, p]));
  const delivery = plan.missions.find(m => parts.get(m.partId)?.kind === 'beam' && parts.get(m.partId)?.floor === 1 && m.carrierId.startsWith('carrier'));
  return phases.flatMap(phase => {
    if (phase.phase !== 'climbing' || !delivery || delivery.pickup < phase.start || delivery.returned > phase.end) return [{ start: phase.start, end: phase.end, seconds: durations[phase.phase] ?? 15 }];
    const points = [phase.start, delivery.pickup, delivery.secured, delivery.rendezvous, delivery.installed, delivery.returned, phase.end];
    const seconds = [6, 4, 18, 12, 16, 8];
    return seconds.map((duration, i): TourSpan => ({ start: points[i], end: points[i + 1], seconds: duration, ...(i > 0 && i < 5 ? { carrierId: delivery.carrierId, partId: delivery.partId } : {}) })).filter(s => s.end > s.start);
  });
}

export function tourSpanAt(spans: TourSpan[], time: number): TourSpan | undefined {
  return spans.find(s => time >= s.start && time < s.end);
}

export function advanceTour(spans: TourSpan[], time: number, elapsed: number): number {
  let remaining = Math.max(0, elapsed);
  const end = spans[spans.length - 1]?.end ?? time;
  while (remaining > 1e-9 && time < end) {
    const span = tourSpanAt(spans, time);
    if (!span) break;
    const rate = (span.end - span.start) / span.seconds;
    const untilBoundary = (span.end - time) / rate;
    const consumed = Math.min(remaining, untilBoundary);
    time = remaining >= untilBoundary ? span.end : time + consumed * rate;
    remaining -= consumed;
  }
  return time;
}
