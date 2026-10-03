/** Fail-closed execution for the named engineering gates in a scenario.
 *
 * This does not assert that ungated actions are mechanically qualified. The
 * schematic `runScenario` remains a separate playback path; a gated run stops
 * before changing support custody when required evidence is absent or stale.
 */
import type { EventAction, ExecutionEvent, Scenario, WorldState } from '../domain/types';
import { assertWorldInvariants } from '../domain/invariants';
import type { EngineeringInputs, GateDecision, GateDefinition } from '../validation';
import { EvidenceRegistry, evaluateEventGate } from '../validation';
import { applyEvent } from './engine';

export interface GatedCommit {
  readonly event: ExecutionEvent;
  readonly gateDecision: GateDecision | null;
  readonly world: WorldState;
}

export interface GatedScenarioResult {
  readonly scenarioId: string;
  readonly status: 'complete' | 'held';
  readonly world: WorldState;
  readonly commits: readonly GatedCommit[];
  readonly hold: null | { readonly event: ExecutionEvent; readonly decision: GateDecision };
  /** The contract covers these named actions only; other mechanics remain open. */
  readonly gatedActions: readonly EventAction[];
}

export type EngineeringInputsForEvent = (worldBefore: Readonly<WorldState>, event: Readonly<ExecutionEvent>) => EngineeringInputs;

/** Run serial events, committing only after every applicable gate passes. */
export function runGatedScenario(
  scenario: Scenario,
  registry: EvidenceRegistry,
  inputsForEvent: EngineeringInputsForEvent,
  gates: Partial<Record<EventAction, GateDefinition>>,
): GatedScenarioResult {
  assertWorldInvariants(scenario.initialWorld);
  let world = structuredClone(scenario.initialWorld);
  const commits: GatedCommit[] = [];
  const gatedActions = Object.keys(gates).sort() as EventAction[];
  for (const event of scenario.events) {
    const gate = gates[event.action];
    const decision = gate
      ? evaluateEventGate(registry, world, event, inputsForEvent(world, event), gate)
      : null;
    if (decision && !decision.allowed) {
      return { scenarioId: scenario.id, status: 'held', world: structuredClone(world),
        commits, hold: { event: structuredClone(event), decision }, gatedActions };
    }
    world = applyEvent(world, event);
    commits.push({ event: structuredClone(event), gateDecision: decision,
      world: structuredClone(world) });
  }
  return { scenarioId: scenario.id, status: 'complete', world: structuredClone(world),
    commits, hold: null, gatedActions };
}
