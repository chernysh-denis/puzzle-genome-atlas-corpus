# Taxonomy Change 209: conditional homing and panel-chain traversal

## Status

- Proposal status: Accepted
- Claim status: Observation
- Evidence quality: Corroborated
- Confidence: Medium
- Date: 2026-10-02.
- Trigger: `GAME-0472`, original Dreamcast *Sonic Adventure*, Sonic's first Emerald Coast visit.
- Scope: new Active `ACT-623`, `ACT-624`, `SYS-1231`, `SYS-1232`, `INF-448`; no earlier signature or verified combination change.

## Evidence and lower-ID transfer test

The [bounded game record](../../knowledge/games/s-z/sonic-adventure.md) uses the original Dreamcast manual for the conditional airborne Homing Attack/Jump Dash, camera and ring/life display; a contemporary Dreamcast route identifies the five numbered panels and first-story Tails rescue. The later DX edition is not imported. Existing navigation, spin attack, live physics, rings, finite lives, point markers, spring launch and real-time traversal transfer without rewriting their definitions. `INF-192` is side-view-only and `SYS-947` requires Genesis-specific slope evidence. Generic `ACT-295` does not encode a second airborne command whose target/no-target resolution redirects the character, while `SYS-1056` launches on contact rather than each numbered-panel jump.

## Disposition

Accept five bounded definitions. Do not assert exact homing range, dropped-ring cap, panel-frame tolerance or disc-revision-specific collision behaviour without new evidence. Retain all earlier signatures and verified combinations.
