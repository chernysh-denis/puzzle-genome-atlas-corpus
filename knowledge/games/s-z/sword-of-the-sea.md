---
game_id: GAME-0599
slug: sword-of-the-sea
game_title: "Sword of the Sea"
analysis_status: reviewed
reviewed: 2026-11-21
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-341
    - ACT-797
  system:
    - SYS-1431
    - SYS-1762
    - SYS-1763
  constraint:
    - CON-788
  information:
    - INF-179
  objective:
    - OBJ-026
  time:
    - TIM-003
---

# Game: Sword of the Sea

Comparison uses the [canonical vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
Button bindings, approach geometry and water extent are instance parameters.

## Analysis scope

- Version / ruleset: the full English-language PS5 base game launched
  by Giant Squid on 19 August 2025. The US PlayStation Store identifies
  the PS5 distribution under concept 10011227. The independent PS5
  captures use English prompts. Their installed patch revisions and
  region of purchase are unverified. Day-one PlayStation Plus access is
  release context and does not identify a different ruleset.
- Structured analysis target: PLAT-PLAYSTATION-5 in
  `knowledge/platforms/games.json`. A PS5 Pro-labelled capture is
  corroboration of the PS5 rule sequence. No measured hardware parity
  or later-platform equivalence is asserted.
- Primary decision loop: choose a line on the Hoversword, carry momentum
  over traversable ground and prepare a high jump across the tutorial
  break. Resonate at the gate fixture and ride out. Find the first red
  pillar, activate its Ocean Seed locally, then travel on the exposed
  stone way and restored water toward the temple.
- Entry and exit: start a fresh adventure in the blue burial hall.
  Begin at the first steerable Hoversword movement after its scripted
  appearance. Finish at the far temple approach beyond the newly wet
  basin and causeway, before the interior vendor exchange or shop task.
- Included: board steering and supported high jump, the tutorial
  interaction and gate opening, descent into the Veiled Sea, the first
  pillar, local water restoration, changed travel medium and arrival at
  the first temple.
- Excluded: exact movement equations, the alternate stele room and
  lantern circle, vendor payment, acquired tricks, scores, collectibles
  and side challenges, further Ocean Seeds and chapter completion, and
  other releases. Upper-bound jump count, neutral-input inertia and
  skipping the first restoration by an alternate line are unverified.
- Potential scoped modules: first temple route through the vendor
  exchange, the larger Veiled Sea chain gates, and comparisons of
  later water rails and wildlife-assisted jumps.
- Direct-play status: no direct play. Developer and PlayStation
  documents distinguish the release and the movement rules. Static
  frames from two independently labelled PS5 playthroughs and a third
  PS5 first-seed route show phase boundaries. Native inputs, timing and
  the persistence of water after reload were not tested. No audio or
  motion playback.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
| --- | --- | --- | --- | --- | --- |
| SS-001 | The PS5 full commercial release is dated 19 August 2025 in both distribution and developer records. | Confirmed | Corroborated | High | P1–P3. |
| SS-002 | The opening shows board control, a hold-and-release Cross high-jump prompt and a jump route beyond the hall break. | Observation | Corroborated | High | W1 1:40–2:10, W2 1:20–1:40, R2 opening. |
| SS-003 | A nearby fixture responds to the tutorial Square Resonate action; the ahead gate opens and the stairs become usable. | Observation | Corroborated | High | W2 1:40–1:50, W1 2:10–2:30; R2 opening. |
| SS-004 | The Hoversword supports continuous steering, building speed and using the approach for launches on the way to the first basin. | Observation | Corroborated | High | P2, P3, H1, W1 2:30–4:30, W2 2:00–3:30. |
| SS-005 | At the first red pillar the Square interaction brings local water and marine life back and exposes a forward route. | Confirmed | Corroborated | High | P3, H1, W1 4:30–5:00, W2 3:20–3:50, W3 1:10–1:40, R1 and R2. |
| SS-006 | The same board can continue across restored water toward the temple. The hands-on report distinguishes higher travel speed on water. | Observation | Corroborated | High | H1, P3, W1 4:50–5:40, W2 3:50–4:20, W3 1:30–1:40, R2 first temple route. |
| SS-007 | The exact native version, speed coefficients, high-jump hold duration and alternative bypasses remain unverified. | Observation | Limited | Medium | Attribution and frame granularity of W1–W3; no controlled trials. |

## Basic data

- Release / origin: Giant Squid, original PS5 and PC launch on
  19 August 2025. The structured target is the commercial PS5 digital
  base game.
- Platform or physical form: solo PS5 game, English prompts and
  PlayStation default button names as observed.
- Puzzle family: physics and object manipulation (FAM-007), because
  the rider uses approach trajectory, launch and surface response, and
  world topology and perspective (FAM-014), because restoring the
  authored locality exposes a new traversable connection.
- P1: [PlayStation Store US](https://store.playstation.com/en-us/concept/10011227),
  release, platform, publisher and supported languages.
- P2: [Giant Squid launch overview](https://giantsquidstudios.com/Sword-of-the-Sea-Launch-Date),
  dated release, momentum and use of crests to launch.
- P3: [Matt Nava's PlayStation launch announcement](https://blog.playstation.com/?p=405589),
  first-party account of the Hoversword, restored waters and returned life.
- H1: [PlayStation hands-on with Giant Squid](https://blog.playstation.com/?p=405770),
  Ocean Seed interaction, water travel and its motion effect. The hands-on
  builds and the release captures have different evidentiary roles.
- W1: [Yellow Bolt Gaming PS5 Pro-labelled run](https://www.youtube.com/watch?v=v_87m-2C78I),
  static samples from the initial ride through the first temple approach.
- W2: [SSSB Games PS5-labelled run](https://www.youtube.com/watch?v=L-Aa15dbB64),
  static samples of the tutorial gate and initial Veiled Sea route.
- W3: [Gamer Guru PS5 first Ocean Seed](https://www.youtube.com/watch?v=BwNXvSKmhPg&t=48s),
  third capture of the first pillar and stone-and-water corridor.
- R1: [PowerPyx first Veiled Sea water point](https://www.powerpyx.com/sword-of-the-sea-all-water-point-locations-restore-water-to-all-areas/),
  identifies the circle at the pillar and Square.
- R2: [Twinfinite first-hand Veiled Sea route](https://twinfinite.net/guides/sword-of-the-sea-walkthrough/),
  follows the tutorial, red pillar, exposed path and first temple. Its later
  ability and collectible names do not expand this unit.
- Claim IDs: SS-001–SS-007.

### Reproducible route evidence

1. Begin the route as the Wraith can steer the board in the blue hall.
   Ride toward the demonstrated rise and break in floor support
   instead of relying on the opening cinematic. At W1 2:00, the
   High Jump prompt explicitly pairs Cross with holding and releasing.
   Release the prepared jump toward the stairs. W1 at 2:10 and W2
   at 1:40 show arrival by the separate blue-lit gate.
2. Follow the Square Resonate prompt near the small fixture before
   the gate. W2 shows that prompt beside the fixture at 1:40 and
   the rider outside at 1:50. W1 first passes the lit stairs at
   2:20 and is on the sand by 2:30. The written route describes
   the intervening gate opening in the same position. The prompt
   specifies a local action; its precise radius is unverified.
3. Steer through the dunes and openings. In the first wide Veiled
   Sea area, follow the line by flags and the tall red pillar.
   W1 at 4:20 approaches it from the dunes; W2 at 3:20 approaches
   on a different dry line. No stele message, trick or purchase
   was used as a required precondition in these routes.
4. Approach the blue circle at the pillar and press Square. W1 at
   4:30 shows the iridescent circle next to the rider; at 4:40 a
   flash and the green-water edge surround the pillar; at 4:50
   the view separates the basin, fish and a narrow way forward.
   Compare W2 3:30–3:50 and W3 1:20–1:40. The wet scene remains
   after the flash, with no second activation needed for the ride.
5. Resume steering on the restored surface, take the revealed
   stone band and stream toward the temple, and stop at its approach.
   W1 5:00–5:30 and W2 3:50–4:10 show steering there on the same
   board. W2 4:20 is already inside the next encounter and outside
   the scope. The higher speed on water is documented by H1 and
   the visible crossing corroborates the use of the new surface.
   No timed comparison of identical lines was performed.

Claim IDs: SS-002–SS-007. Times locate sample frames and do not
specify the required time or tempo in a new session.

## Mechanical decomposition

### Action Genes

- ACT-008: control the Wraith's board directly along the hall,
  valley and restored path. Pick motion and aim in the current
  geometry rather than selecting a destination.
- ACT-341: commit the local Resonate interaction at a reachable
  fixture. The opening gate and red-pillar Ocean Seed are separate
  targets with different results.
- ACT-797: hold and release the jump input at a supported takeoff
  for a high jump. This is distinct from pressing Cross again in
  midair to perform an aerial move.
- Claim IDs: SS-002–SS-006.

### System Behaviour Genes

- SYS-1431: opening the tutorial gate changes access to the
  same aperture and the stairs beyond it.
- SYS-1762: the Hoversword builds momentum, carries it to its
  launch and responds to the current surface. Restored water
  enables faster board movement on the continuing approach.
- SYS-1763: the first Ocean Seed restores a local traversable
  body of water and reveals the stone-and-water line ahead.
  The return of sea life is visible here; the scope does not
  require riding or landing on a creature.
- Claim IDs: SS-002–SS-007.

### Constraint Genes

- CON-788: the tutorial passage is closed at first, then
  traversable after its fixture opens it. Each board route
  still needs compatible support or a reachable landing.
  This gate is independent of both purchase currency and scores.
- Claim IDs: SS-002, SS-003, SS-007.

### Information Genes

- INF-179: see the hall step, gate, device, flags, tall red
  pillar and illuminated mark. The wet surface, moving fish and
  exposed path make the changed locality legible. The prompt
  names the available high jump and local interaction.
- Claim IDs: SS-002–SS-006.

### Objective Genes

- OBJ-026: use the authored route after restoring water and reach
  the far temple approach. A local flash alone fails the arrival
  criterion. The boundary does not require optional scoring, a
  merchant transaction or a whole-chapter clear.
- Claim IDs: SS-005–SS-007.

### Time Genes

- TIM-003: steering, support contact, launch, flight and landing
  update in real time. A poor launch may miss the intended line.
  Neither trace nor the reported rules establish a time quota on
  the first restore-and-traverse packet.
- Claim IDs: SS-002, SS-004, SS-006, SS-007.

## Reproducible transitions

| Before | Action | Resolution | What it establishes | Claim ID |
| --- | --- | --- | --- | --- |
| Controllable board on supported hall floor | Steer, hold Cross and release at the approach | Higher launch can reach the far stair | Prepare the launch before leaving support | SS-002 |
| Still short of the far stair | Re-establish a supported line before another jump | The intended route still requires reaching the far side | A launch is not a landing on the far route | SS-002, SS-007 |
| In reach of the fixture in front of the closed gate | Use Square Resonate | The gate opens and the rider can take the stairs | Local state change precedes traversing this aperture | SS-003 |
| On dry dunes | Choose the line toward flags and pillar | Momentum and visible terrain guide approach | Dry movement reaches an authored interaction locus | SS-004, SS-005 |
| At the red pillar before restoration | Use the local Square interaction | Flash spreads, basin becomes wet and the path opens | A changed area remains after its activation animation | SS-005 |
| Basin already restored | Ride along its water and exposed stone band | Same board reaches the far temple approach | Traversal applies the previous environmental change | SS-006 |
| At the temple approach | Stop before merchant progression | This packet has settled spatially | Merchant and further restorations are separate units | SS-006, SS-007 |

## Strategic and experiential structure

The first hall teaches launch placement before requiring a fixture
interaction. The larger dunes then let the player choose the approach
line while the pillar fixes the restoration locus. After the change,
the most useful local route is visible in a different surface and
direction. Several observed lines reach the same pillar without a
character loadout or a score qualification. The hands-on account
explains why the new medium matters to subsequent movement. A systematic
failure matrix and exact recoverability boundaries are unverified.
Claim IDs: SS-002–SS-007.

## Replay and variation

The checked routes approach from different headings, and W3 shows a
side visit before returning to the same restoration point. The local
restoration has the same visible result in each trace. Exact repeat
behaviour on reload, New Game Plus and alternate installed builds are
outside scope. No hidden random seed or route independence follows
from these samples. Claim IDs: SS-004–SS-007.

## Adjacent systems and history

Giant Squid names skating and snowboarding movement influences along
with its own creative heritage. This does not prove identity with
racing or trick-settlement mechanics. Journey's cloth can connect
discrete bridge sections and power scarf flight. Here one fixed
restoration point changes the rideable medium and exposes a continuous
route used by the same board. Claims SS-004–SS-007.

## Normalised genome

| Type | Stable genes | Role |
| --- | --- | --- |
| Action | ACT-008, ACT-341, ACT-797 | Steer, resonate and prepare a high jump |
| System Behaviour | SYS-1431, SYS-1762, SYS-1763 | Open a barrier, resolve board momentum and restore a wet route |
| Constraint | CON-788 | Respect the currently open aperture |
| Information | INF-179 | Read active fixtures and local routes |
| Objective | OBJ-026 | Reach the temple approach after restoration |
| Time | TIM-003 | Real-time riding and flight |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `598` (`GAME-0001`–`GAME-0598`).
- Exact genome matches: none.
- Tied near matches: `GAME-0394` — LittleBigPlanet 2 (`5 / 18 = 0.277778`).
- Supported combination subsets: none.
- Scan date: 2026-11-21.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
| --- | --- | --- | --- |
| GAME-0394 LittleBigPlanet 2 | ACT-008, ACT-341, INF-179, OBJ-026, TIM-003 | Both use live navigation, visible local fixtures and an authored activation before traversing to a destination. Grab and Swing uses a grappling tether and bounce pads past lethal floor. Veiled Sea uses a prepared board jump followed by a restored water route on the same board. | 5 shared of 18, Jaccard 0.277778 |

### Preserved research notes

- Classification result: New gene.

## Taxonomy impact

- [TAXONOMY_CHANGE_345](../../../research/taxonomy-changes/TAXONOMY_CHANGE_345.md)
  adds one action and two system boundaries.

## Negative results

- SYS-1142 requires releasing a responsive cloth span. The basin
  restores an environmental medium and uncovers a way through it.
- SYS-1133's restoration creates a rising lethal waterline. The first
  Veiled Sea restoration creates a usable surface.
- SYS-1181's downhill course settles race traversal. The restored water
  changes movement on a continuing open route without a rival finish.
- SYS-1386 covers one additional airborne impulse. This high-jump
  instruction holds and releases the supported takeoff input.

## Delta summary

## New facts

- [Observation | Corroborated | High] A high jump is prepared before
  leaving support. SS-002.
- [Confirmed | Corroborated | High] Resonating at the first red
  pillar restores the local basin and exposes a usable route. SS-005.
- [Observation | Corroborated | High] The same Hoversword continues on
  the changed surface to the temple. SS-006.

## New genes

- [Observation | Corroborated | Medium] ACT-797, SYS-1762 and SYS-1763.

## New combinations

- [Observation | Direct | High] No new combinations.

## Taxonomy changes

- [Observation | Corroborated | High] TAXONOMY_CHANGE_345.

## New questions

- What is the native charge-to-height relation in this PS5 build?
- Which first-area lines, if any, bypass the restored approach?
- How is the local water state retained on a controlled save and reload?

## Next recommended game

- [Hypothesis | Limited | Medium] NBA Street Vol. 2 on North American
  PlayStation 2 under Selection 049. Its scoring possession and
  Gamebreaker test authored progress under competitive opposition.

## Why this game

- [Hypothesis | Limited | Medium] A single terrain restoration changes
  the available connection and the movement on that connection within
  one short, visible traversal loop.
