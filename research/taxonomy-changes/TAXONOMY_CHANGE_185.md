# Taxonomy Change 185: Two-input endless corridor chase

## Status

- Proposal status: Accepted
- Claim status: Observation
- Evidence quality: Corroborated
- Confidence: Medium
- Date: 2026-09-28
- Trigger: `GAME-0448` *Temple Run*, one fresh unassisted run in the original 2011 iPhone game.
- Scope: admit `ACT-588`–`ACT-589`, `SYS-1175`–`SYS-1177`, `CON-723` and `INF-433` as Active. Earlier game signatures and verified combinations remain unchanged.

## Problem and accepted change

Imangi's original-game description and its founders' first-person interviews distinguish automatically continuing forward motion from discrete quarter-turn/jump/slide swipes and continuously tilted lateral placement. A 2011 firsthand account describes a changing endless course; the creator describes trips that bring pursuers close. One fixed authored level, free avatar navigation or a generic instant-death obstacle would lose those decision boundaries.

## Transfer and rejection tests

- Reuse `SYS-045` for autonomous forward movement, `SYS-037` for optional coin contact, `OBJ-002` for score seeking and `TIM-003` for live input under progression.
- `ACT-588` makes a discrete corner/posture request and `ACT-589` moves the lateral line; `CON-723` prevents either from becoming free stop/reverse navigation or substituting tilt for a corner turn.
- `SYS-1175` supplies varying future path segments without asserting a precise generator. `SYS-1176` distinguishes a survivable trip and pursuer pressure from terminal fall/collision/capture. `SYS-1177` accumulates and settles an unassisted attempt score. `INF-433` exposes only the local third-person corridor horizon.
- `SYS-496` would incorrectly make the course one fixed soundtrack-bound replay; `SYS-500` assembles a finite mission before play. `CON-113` requires terminal hazard contact and would erase the recoverable stumble. No earlier signature is silently widened.

## Decision

Admit seven reviewed boundaries with full Ukrainian copy and an original mechanically plausible left-corner-and-coin illustration. This is a source-only 2011 iPhone packet, not evidence for later Temple Run+, current challenges, exact random distribution, guaranteed coin score formula or a measured playthrough. The decision authorises only the requested local unit commit; no push, public corpus publication or deployment.
