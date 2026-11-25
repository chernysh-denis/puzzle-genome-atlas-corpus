---
game_id: GAME-0690
slug: sonic-advance
game_title: "Sonic Advance"
analysis_status: reviewed
reviewed: 2026-11-24
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-295
    - ACT-910
  system:
    - SYS-036
    - SYS-037
    - SYS-045
    - SYS-215
    - SYS-755
    - SYS-902
    - SYS-905
    - SYS-911
    - SYS-933
    - SYS-935
    - SYS-947
    - SYS-948
    - SYS-1056
  constraint:
    - CON-068
  information:
    - INF-192
    - INF-347
  objective:
    - OBJ-002
    - OBJ-164
  time:
    - TIM-003
---

# Game: Sonic Advance

This record uses the [canonical vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
The first act ties retained movement to the shape of the route and
keeps ordinary rings useful until the end-stage tally.

## Analysis scope

- Version / ruleset: original English European standalone Game Boy
  Advance cartridge, released March 8, 2002. The documented
  European cartridge family is AGB-ASOP. The regional witness uses
  a European cartridge on Game Boy Player. Its serial and ROM
  revision were not independently verified.
- Structured analysis target: PLAT-GAME-BOY-ADVANCE in
  [platform coverage](../../platforms/games.json).
- Entry: select Game Start, Sonic alone and Neo Green Hill Zone
  Act 1. Start from the first controllable beach position with zero
  rings. Use English, Normal controls and Time Up enabled for the
  reference trace. The captured options and prior save history are
  unverified. The elapsed limit does not fire in the successful run.
- Primary decision loop: read the path and hazards, steer and build
  speed, choose a jump or attack roll, exploit a supported slope
  or an ordinary contact spring, and collect rings along a safe
  route. Break an eligible monitor to receive its item when useful.
  Preserve rings against ordinary hits and until the exit.
- Positive terminal: pass the Act 1 signpost. Read the elapsed
  time and retained-ring bonuses converting to score. Stop at the
  initial playable position of Act 2.
- Failure and restart: the original rules describe ring scatter
  on an ordinary unshielded hit and a lost try at zero rings.
  A point marker can change where a remaining try restarts.
  The enabled Time Up option also permits a time-out loss. These
  are rule-source boundaries, not events in the successful European
  capture.
- Included: horizontal steering, jumping, character spin and
  grounded Spin Dash; directional motion, slopes, loops and
  ordinary springs; local enemies and spin contact; ring pickup,
  protection and recovery rule; one monitor and barrier; point
  marker activation, lives threshold, timer, score and signpost.
- Excluded: separate input and payoff modelling for the air dash,
  somersault and grind, exact inertia or damage formula, hit grace
  values, ring emission cap, replay or save semantics, exact
  bonus tables, Act 2 play and the boss, Special Stages,
  Tiny Chao Garden, link functions, Time Attack, co-op, the extra
  Tails code, sequels, compilations, ports and other regions as targets.
- Potential scoped module: compare tested European cartridge
  damage-and-restart branches from the same point marker, including
  the values retained across a lost try.
- Direct-play status: no personal cartridge execution, binary
  inspection or controller telemetry. W1 explicitly identifies an
  original European cartridge and Game Boy Player. W2 and W3
  are labelled supplementary traces. Short background frames were
  examined without audio.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
| --- | --- | --- | --- | --- | --- |
| SAD-001 | Nintendo dates the initial European GBA release to March 8, 2002. W1 shows Sonic alone entering Zone 1 Act 1 on a European cartridge. Prior act entries are visible in its menu. | Confirmed | Corroborated | High | P1, P2, H1, W1 1:19–1:27 |
| SAD-002 | Normal controls select horizontal movement and jumping. An attack spin can accompany moving contact. The booklet separately describes holding Down with A for an in-place Spin Dash and releasing Down to launch. W3 shows a compatible stationary spin-to-motion sequence, but there is no button telemetry. | Observation | Corroborated | High | P3 pp. 6–8, W1 1:27–1:40, W3 2:18–2:22 |
| SAD-003 | The live route integrates movement with support changes. Sonic continues along curved loop surfaces, leaves support on jumps and receives upward motion after contact with an ordinary spring. World action and ring count can change while the elapsed counter advances. | Observation | Corroborated | High | W1 1:46–1:56 and 2:18–2:24, W2 1:57–2:13 |
| SAD-004 | Ordinary ring contact increases the held count immediately. On crossing 100 in W1, the lower-left try display changes from 2 to 3 without subtracting the rings. Two local robot defeats precede score increases. | Observation | Corroborated | High | P2, W1 1:29–1:41, 2:19–2:22 and 2:28–2:30, W3 3:20–3:24 |
| SAD-005 | An eligible spin contact breaks a monitor. A green barrier appears around Sonic and persists into subsequent movement. The booklet describes single-hit removal for barrier items. The exact absorbing hit was not observed in W1. | Observation | Corroborated | High | P2, P3 p. 18, W1 2:13–2:20, W2 1:29–1:33 |
| SAD-006 | The original rules describe ordinary unshielded damage spending a positive ring reserve without consuming a try and scattering rings that can be recovered. At zero rings a compatible hit may lose a try. A checkpoint changes the restart point. The enabled Time Up option can terminate a try; the successful W1 run does not reproduce these failures. | Confirmed | Corroborated | High | P2, P3 pp. 16 and 29, W1 2:25–2:29 |
| SAD-007 | W1 freezes Act 1 at the signpost with 134 rings and displayed time 1:06.85. The tally credits 5,000 time points and 13,400 ring points. Score moves from 300 to 18,700, and the next act begins at zero rings with the accrued score and three tries displayed. | Observation | Direct | High | P2, W1 2:32–2:48 |

## Basic data

- Release / origin: Sonic Team and Dimps, original European
  English Game Boy Advance release, March 8, 2002.
- Mechanical families: FAM-007 for supported angle-dependent
  movement and physical contact, and FAM-010 for timed jumps
  through a live traversal route.
- P1: [Nintendo UK's European release listing](https://www.nintendo.com/en-gb/Games/Game-Boy-Advance/Sonic-Advance-267277.html).
  Identifies the GBA product, regional date and modes.
- P2: [SEGA's original rules](https://sonic.sega.jp/advance/rule.html)
  and [mode and option descriptions](https://sonic.sega.jp/advance/game.html).
  Identify Act 1 signpost, ring loss and recovery, try milestones,
  checkpoints, Act 2 difference and the optional time-out loss.
  These creator pages describe the original Japanese release.
  They do not establish European binary parity.
- P3: [Original North American GBA booklet scan](https://www.videogamemanual.com/gba/Sonic%20Advance%20%28USA%29.pdf).
  Printed pp. 6–8 cover normal controls and the Spin Dash,
  pp. 14–18 cover main-game progression and items, and p. 29
  documents Time Up and the button mapping. Used only as a
  supplementary regional rule source alongside P2 and observed play.
- H1: [Photographed European cartridges and board records](https://gbhwdb.gekkio.fi/cartridges/AGB-ASOP-0/).
  Establishes a reported AGB-ASOP board and AGB-ASOP-UKV/FRA
  label variants. It does not identify the witness cartridge's
  press or bytes.
- W1: [Randomised Gaming's European cartridge capture](https://www.youtube.com/watch?v=Ut1MKpGy10g&t=79s).
  The author identifies the Game Boy Player and GameCube capture
  chain. Use approximately 1:19–2:48. Its displayed choice starts
  at Act 1 with later entries present, so freshness was not inferred.
- W2: [Retro Game Spacko's GBA capture via LongplayArchive](https://www.youtube.com/watch?v=aCbbdS5t8nU&t=84s).
  The source identifies its edition as NTSC. Use 1:24–2:28 for
  corroborating movement, ordinary contact, barrier and ring pickup.
  Stop before the separate Special Stage branch.
- W3: [Dark Lord Chaos's supplementary Game Boy Advance run](https://www.youtube.com/watch?v=zGBXgSGjQeI&t=138s).
  Use 2:18–2:22 for a compatible early acceleration sequence
  and 3:20–3:24 for the 100-ring display change. Region, binary
  and inputs are unavailable. No later branch is used here.
- Claim IDs: SAD-001–SAD-007.

### Reproducible fixture evidence

1. Choose Game Start, Sonic and the first act. W1 shows its
   stage card near 1:25. At about 1:29–1:39, take nearby
   rings as they are crossed, jump over the spikes and use
   spin contact on an eligible robot. For the distinct stationary
   release use the Normal mapping from P3 p. 8.
2. At 1:46–1:56 follow the hill and loop with enough forward
   speed. Read the position relative to the curve and rising
   ring count. Observe the differing supported and airborne states.
3. Around 2:13–2:17 use spin contact on the monitor. Check the
   freed item icon and the barrier in subsequent movement.
   Around 2:20–2:22 Sonic crosses the 100-ring threshold and
   the try display rises. An ordinary spring then raises him
   around 2:22–2:24.
4. Around 2:25–2:30 pass the point marker and take contact
   pickups on the descending route. Read the checkpoint and
   restart rules in P2 and P3. Do not treat a successful pass
   as an observed restart.
5. At 2:32–2:34 pass the signpost. The captured counter reaches
   1:06.85 at 134 rings. At 2:37–2:41 read the time and ring
   amounts being transferred to score. Confirm the first
   controllable Act 2 state around 2:48 and stop.

## Mechanical decomposition

### Action Genes

- ACT-008: steer Sonic along the scrolling path and choose jumps
  across hazards or to optional ring lines. SAD-002–SAD-003.
- ACT-295: enter an ordinary character attack spin or moving roll.
  Contact resolution is separate. SAD-002, SAD-004.
- ACT-910: prepare a stationary ground spin with Down and A,
  then release Down to launch it. SAD-002.

### System Behaviour Genes

- SYS-036: maintain continuous supported and airborne movement
  through slopes, gaps and landing. SAD-003.
- SYS-037: ring contact immediately adds to the held count. SAD-004.
- SYS-045: local robots move autonomously across the current route.
  SAD-004.
- SYS-215: attack contact can defeat an eligible robot and preserve
  the live route. SAD-004.
- SYS-755: compatible contact breaks the monitor and releases its
  contained result. SAD-005.
- SYS-902: the barrier changes exposure to a compatible hit.
  Acquisition is observed, removal is rule-sourced. SAD-005.
- SYS-905: the finish marker settles time and rings into score
  before the successor act. SAD-007.
- SYS-911: a lost try returns Sonic to the allowed anchor when
  stock remains. The original documents define the branch. SAD-006.
- SYS-933: reaching a point marker sets a local restart anchor.
  SAD-006.
- SYS-935: the reached ring milestone adds a try without clearing
  the ring count. SAD-004.
- SYS-947: supported speed and route curvature determine the
  traversal state on approaches, slopes and loops. Exact original
  coefficients are unavailable. SAD-003.
- SYS-948: compatible unshielded hits can empty rings into
  recoverable pickups. The scope uses the published buffer rule,
  with exact cap and grace unavailable. SAD-006.
- SYS-1056: ordinary contact springs redirect Sonic into a higher
  path without a separate jump command. SAD-003.

### Constraint Genes

- CON-068: with Time Up enabled, reaching the declared limit can
  end a try. The capture stays short of this boundary. SAD-006.

### Information Genes

- INF-192: the scrolling viewport exposes the nearby path, spikes
  and platforms before the next movement choice. SAD-003.
- INF-347: elapsed time, held rings, score and tries remain visible
  during ordinary route play. Marker and barrier appearance
  communicate their local states. SAD-004–SAD-007.

### Objective Genes

- OBJ-002: route choices and elapsed time can raise the settled
  score through separate bonus channels. SAD-004, SAD-007.
- OBJ-164: pass the signpost and advance from the cleared act to
  the next with the settled score. SAD-007.

### Time Genes

- TIM-003: choose movement, jump and attack timing while local
  movement and the stage clock continue. SAD-002–SAD-003.

## Reproducible transitions

| From | Input or event | To | Evidence |
| --- | --- | --- | --- |
| First controllable beach frame | Apply horizontal movement or jump | Sonic moves along or leaves terrain while the act clock advances | SAD-001–SAD-003 |
| Supported standing state | Hold Down and press A, then release Down under Normal mapping | A charged ground roll launches from the stationary preparation point | SAD-002 |
| Moving over the loop and ring path | Cross eligible rings and reach the milestone | The counter increases and the try display rises without debiting rings | SAD-003–SAD-004 |
| Intact item monitor | Make eligible attack contact and receive its result | Monitor breaks and the barrier appears | SAD-005 |
| Moving into an ordinary spring | Contact its launch surface | Authored upward launch and renewed airborne steering | SAD-003 |
| Ordinary unshielded damage with rings | Receive the compatible hit | Ring reserve empties into recoverable pickups; the try remains | SAD-006 |
| Valid point marker and a later lost try | Restart with stock remaining | Anchor selected by the point marker | SAD-006 |
| Approaching Act 1 signpost with live measurements | Pass the marker and wait for the tally | Act 2 begins with settled score and the demonstrated carried stock | SAD-007 |

## Strategic and experiential structure

Speed can make curved terrain traversable, while smaller jumps
can collect rings or avoid hazards. The route does not require
holding a stated ring minimum at the signpost. Ordinary rings
still affect survival and the optional score. A result can
reward both a fast route and retained rings.

## Replay and variation

The captures take different local detours and reach different ring
totals. The documented European finish uses a shielded upper
approach through its latter section. The supplementary traces
include hidden Special Stage exploration beyond the observed
segments used here. No leaderboard or exact replay state is inferred.

## Adjacent systems and history

This original handheld game distinguishes the Act 1 signpost from
Act 2's boss and capsule. The separate Time Attack and link modes
use their own entry and result rules. Tiny Chao Garden progression
and GameCube transfer are independent of this act definition.

## Normalised genome

| Type | Stable genes | Role |
| --- | --- | --- |
| Action | ACT-008, ACT-295, ACT-910 | Direct travel, spin contact and a stationary prepared release |
| System Behaviour | SYS-036, SYS-037, SYS-045, SYS-215, SYS-755, SYS-902, SYS-905, SYS-911, SYS-933, SYS-935, SYS-947, SYS-948, SYS-1056 | Physical traversal, live contacts, protection, checkpoint and finish settlement |
| Constraint | CON-068 | If enabled, the declared time limit can end the attempt |
| Information | INF-192, INF-347 | Show imminent terrain and the held rings, score, time and tries |
| Objective | OBJ-002, OBJ-164 | Improve the tally and carry the run through the authored signpost |
| Time | TIM-003 | Intervene before an advancing live route reaches its hazards |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `689` (`GAME-0001`–`GAME-0689`).
- Exact genome matches: none.
- Tied near matches: `GAME-0333` — Sonic the Hedgehog (`20 / 22 = 0.909091`).
- Supported combination subsets: none.
- Scan date: 2026-11-24.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
| --- | --- | --- | --- |
| [Sonic the Hedgehog (GAME-0333)](sonic-the-hedgehog.md) | ACT-008, ACT-295, CON-068, INF-192, INF-347, OBJ-002, OBJ-164, SYS-036, SYS-037, SYS-045, SYS-215, SYS-755, SYS-902, SYS-905, SYS-911, SYS-933, SYS-935, SYS-947, SYS-948, TIM-003 | Both use supported speed, ring protection and a signpost tally. The handheld route adds the prepared stationary Spin Dash and separately witnessed ordinary spring launch. | Near, `0.909091` |

## Taxonomy impact

The base attack-spin gene already includes jumping into a spin
or beginning a moving roll. Retain a separate action for
preparing propulsion from a stationary supported crouch and
committing the result by releasing the direction.

## Negative results

- One hundred rings grant a try without withdrawing those rings.
- The score bonus is settled only after the signpost, even
  though collected rings affect ordinary play earlier.
- A monitor must be broken to expose its result.
- The successful recording does not measure failure thresholds,
  restart fields, options, the exact ring-loss cap or grace timing.
- No later act, special stage or character-specific unlock is
  required to close the first act as scoped.

## Delta summary

Twenty-two genes, with one new definition for the prepared
rolling launch. Sonic's direct route control, successful finish
and rule-sourced failure branches are kept distinct.

## New facts

- A stationary command can prepare a roll before any forward travel.
- Surface curvature and speed determine which supported paths remain usable.
- Retained rings can protect a try, reach a stock milestone and add score.
- The finish tallies time and rings before the next act opens.

## Principles and design implications

Separating a prepared release from a moving attack gives a
player a way to start a steep route from rest. A visible
resource can provide ordinary safety and still count at the finish.

## Puzzle or game generation potential

Design an original rolling route with a steep loop reached
from a shallow bowl. Give the player a grounded charge,
contact tokens and a marked finish. Report separate time
and retained-token bonuses.

## New genes

- ACT-910

## New combinations

None. All 274 verified combinations were checked; no proper subset fits this genome.

## Taxonomy changes

[Taxonomy Change 436](../../../research/taxonomy-changes/TAXONOMY_CHANGE_436.md).

## New questions

- What stock and time does a proven European checkpoint restore?
- How do the same-build loop and release velocities differ?
- Which exact bonus tiers apply to slower first-act finishes?

## Next recommended game

Continue Selection 059 with `GAME-0691`, REPLACED on the original
commercial Xbox Series X|S release.

## Why this game

The first small stage tests the interaction of retained speed,
physical route selection, recoverable resources and a settled finish.
