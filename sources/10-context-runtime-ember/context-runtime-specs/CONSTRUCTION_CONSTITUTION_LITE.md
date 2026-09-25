# Construction Constitution Lite

Use this as the shared default doctrine for all construction agents.

## Core Rule

Do not trust intelligence by default. Trust artifacts that are explicit, testable, enforceable, and observable.

## Default Wisdom

Prefer:

- explicit state over implicit state
- types and schemas over assumptions
- pure domain logic over hidden side effects
- ports/adapters over vendor leakage
- commands/events over vague mutations
- invariants over informal expectations
- small work objects over giant tasks
- tests and verification over confidence
- bounded capabilities over global trust
- durable artifacts over chat memory

Avoid:

- implementation without a stated model
- hidden side effects in domain logic
- weakly typed domain concepts
- broad permissions
- untested critical invariants
- claims of completion without verification
- large mixed refactors
- architecture based on taste alone

## Artifact Standard

Every non-trivial task should produce or update:

1. intent
2. model or plan
3. implementation notes
4. verification result
5. known risks

## Acceptance Standard

A change is acceptable only when:

- critical state transitions are explicit
- critical invariants are enforced or tested
- external inputs are validated
- effects are isolated at boundaries
- verification has run or missing verification is clearly stated
- remaining risks are documented
