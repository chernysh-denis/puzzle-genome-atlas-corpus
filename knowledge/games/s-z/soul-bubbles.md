---
game_id: GAME-0726
slug: soul-bubbles
game_title: "Soul Bubbles"
analysis_status: reviewed
reviewed: 2026-11-25
combination_ids: []
gene_ids:
  action:
    - ACT-941
    - ACT-942
    - ACT-943
    - ACT-944
  system:
    - SYS-036
    - SYS-037
    - SYS-2030
  constraint: []
  information:
    - INF-657
  objective:
    - OBJ-014
  time:
    - TIM-003
---

# Game: Soul Bubbles — first spirit delivery in Tir Tairngire

Use the [canonical vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
Spirit, bubble, Celestial Stone and Gateway Cube are scoped instances.

## Analysis scope

- Version / ruleset: commercial English European Nintendo DS Game Card,
  released 13 June 2008. Use the standard solo story route after the
  three Initiation levels. The complete English recording W1 does not
  establish cartridge region, hardware or revision. The official English
  North American booklet is a rules witness, with no assumed parity
  beyond the cited controls and observed route.
- Structured target: `PLAT-NINTENDO-DS`. Start at the first grouped
  spirits in Tir Tairngire level 1 and stop at the first accepted
  Gateway Cube delivery and result. Initiation explains basic controls
  but is outside the spirit delivery. The witness takes all seven spirits
  to the cube. Cut, join and deflate are available alternatives or
  adjustments within this route.
- Primary decision loop: make a protective bubble around the spirits, aim
  airflow at the moving carrier, use size and shape to negotiate gaps
  and position it at the fixed receiver.
- Included: draw and blow input, deformation and live contact, cut and
  join, deflate, map and viewport, contact collection of stardust and
  terminal delivery. Excluded: startup microphone prompts, later stages,
  Calabash and world unlock quotas, time trials, rank optimisation,
  water and gas transport, alternate regional builds and exact physics
  coefficients. The minimum viable delivered count and breath timing are
  documentary qualifications.
- Direct-play status: no personal console or emulator session. Nintendo
  and the booklet establish edition and inputs. The English stage and
  a separate period demonstration show the carrier, clearances and
  destination. Visual frames were inspected silently in the background.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
| --- | --- | --- | --- | --- | --- |
| SB-001 | Nintendo documents the commercial European Nintendo DS Game Card for 13 June 2008. The English witness finishes three Initiation exercises before Tir Tairngire 1. | Observation | Corroborated | High | P1, P2 pp. 10–11, W1 03:15–17:42 and 18:30–18:55, S1 §§8.1–8.2 |
| SB-002 | The first Tir Tairngire stage begins with seven spirits at a Celestial Stone. The displayed Draw instruction and the closed-contour control produce a carrier around the group. | Observation | Corroborated | High | P1, P2 pp. 4–7, W1 18:35–19:02 and 19:20–19:45, S1 §§4.3–4.5 |
| SB-003 | An ordinary stylus stroke through the bubble directs the simulated gust. The booklet distinguishes short gentle strokes from longer stronger strokes and describes recovery after a long continuous stroke. Unmeasured: force curve and breath timing. | Observation | Corroborated | High | P2 pp. 4–7, W1 19:40–19:58 and 21:18–22:08, W2 00:06–00:10 |
| SB-004 | Holding the deflate modifier and touching the carrier shrinks it. Tir Tairngire teaches the smaller footprint before a tight opening. Continued touch until popping is booklet evidence, without a native timing measurement. | Observation | Corroborated | High | P1, P2 pp. 6–7, W1 18:45–18:50 and 20:09–20:36 |
| SB-005 | The same edit mode permits splitting one membrane with a stroke across it or joining two touching membranes centre to centre. The recorded stage shows separate bodies and the displayed join rule. It does not establish that splitting is globally mandatory. | Observation | Corroborated | High | P1, P2 pp. 4–7, W1 19:48–19:58 and 23:03–23:23, S1 §4.3 |
| SB-006 | The occupied bubble changes outline against the narrow wind passage and rounds out on clearance. A bubble passing over stardust collects it while the route continues. | Observation | Corroborated | High | P2 pp. 8–10, W1 22:44–23:04 and 23:36–23:50, W2 00:26–00:33, S1 §§4.5 and 8.2a |
| SB-007 | The second display shows position and explored passages. The held Map command opens the map on the touch surface for selecting the current viewport independently of payload movement. Initiation demonstrates the view relocation. | Observation | Corroborated | High | P2 pp. 5 and 9–10, W1 03:50–04:39 and 21:18–22:45 |
| SB-008 | Move the payload into the Gateway Cube. The stage transitions to the Tir Tairngire 1 result and credits seven saved. The booklet specifies delivering all survivors. Two attributable player accounts document that at least one must survive to be accepted. Partial delivery and loss were not reproduced in the scoped recording. | Observation | Corroborated | High | P2 pp. 10 and 12, W1 23:53–24:20, W2 00:43–00:56, S1 §§4.4–4.5, S2 |

## Basic data

- Release / origin: Mekensleep's original Nintendo DS release, published
  by Eidos Interactive. Nintendo lists the European release on 13 June
  2008 and an English recording shows the scoped language.
- Platform or physical form: Nintendo DS retail Game Card, with a touch
  action view and a second display. The motion uses a stylus, while buttons
  switch the function of the same touch surface.
- Mechanical family: `FAM-007`. Airflow, wall geometry, collision,
  deformation and changed clearance determine whether the payload can
  follow the intended path.
- Sources accessed 2026-11-25:
  - **P1:** [Nintendo UK product page](https://www.nintendo.com/en-gb/Games/Nintendo-DS/Soul-Bubbles-272981.html).
    Edition, date, stylus, bubble creation, variation and protected transport.
  - **P2:** [Eidos English Nintendo DS booklet](https://support.na.square-enix.com/document/manual/1012/sb_nds.pdf).
    North American edition. Printed pp. 4–13 document input modes,
    map, Initiation, successful delivery and summary. Cited common rules
    are bounded by the independent English recording.
  - **P3:** [Eidos release announcement reproduced by Nintendo World Report](https://nintendoworldreport.com/news/16145/soul-bubbles-releasing-in-europe-this-friday).
    Developer, publisher, physical European launch and custom physics.
  - **W1:** [MrClockworkApple, first English playthrough episode](https://www.youtube.com/watch?v=7_Em5UkdXFc).
    Three Initiation routes followed by Tir Tairngire Level 1.
    The observed route runs from the Level 1 title at 18:35 through
    the seven spirits accepted by the cube around 24:02 and the result.
    The recording does not identify physical buttons, cartridge region
    or exact delivery outcome with losses.
  - **W2:** [Planet Nintendo, Cube Gameplay](https://www.youtube.com/watch?v=ZjUZsvpg4Xw).
    Period clip shows a carrier entering passages and a fixed cube
    receiving its contents. The excerpt omits stage identification and
    is used only for shared mechanical corroboration.
  - **S1:** [Deejai1220, June 2008 first-hand route guide](https://gamefaqs.gamespot.com/ds/945501-soul-bubbles/faqs/53244).
    §§4, 7 and 8 explain the control, payload threshold, the three
    empty Initiation runs and first Tir Tairngire route.
  - **S2:** [Contemporary Nintendo World Report contributor's play report](https://www.nintendoworldreport.com/forums/index.php?topic=25852.0).
    Independent account of starting with seven spirits and needing
    at least one to finish a normal stage.
- Claim IDs: SB-001–SB-008. For reproduction, complete Initiation and
  begin Tir Tairngire Level 1. Test gesture, shape, source, route and
  receiver separately and stop on the result screen.

## Mechanical decomposition

### Action Genes

- New `ACT-941`: use Draw and close a loop around the starting
  group to make the protective carrier (SB-002).
- New `ACT-942`: use an ordinary directional stroke to apply
  airflow and steer the released carrier (SB-003, SB-008).
- New `ACT-943`: the edit mode splits one membrane or joins
  two touching carriers depending on the start and end of the stroke
  (SB-005).
- New `ACT-944`: use Deflate and interior contact to decrease
  the carrier's footprint before the clearance (SB-004).

### System Behaviour Genes

- Reuse `SYS-036`: the carrier moves under sustained force and
  collision within the live route (SB-003, SB-006).
- Reuse `SYS-037`: live overlap with stardust credits the
  collectible and the route continues (SB-006).
- New `SYS-2030`: the moving carrier deforms at constrictions
  while retaining the enclosed contents, then rounds out (SB-006).

### Constraint Genes

No separate constraint gene. Receiver eligibility belongs to the delivery
and local shape limits to the deformation. Breath recovery is documented
without isolating it in the observed route.

### Information Genes

- New `INF-657`: the persistent second-screen map can move to
  the touch surface and recenter the viewport. This leaves
  the carrier outside the map input loop (SB-007).

### Objective Genes

- Reuse `OBJ-014`: direct the designated spirit payload into
  the Gateway Cube. The accepted result records spirits saved (SB-008).

### Time Genes

- Reuse `TIM-003`: adjust airflow and negotiate moving constraints
  while the carrier and hazards continue to move (SB-003, SB-006).

## Formal state and transitions

Separate the current gesture mode, camera location, elapsed simulation,
carrier geometry and velocity, exposed and enclosed spirits, remaining
stardust, and fixed receiver. Creating, translating and reshaping the
carrier are distinct transitions. Moving the camera does not transport
the carrier. Arrival credits delivery and changes the stage view.

## Reproducible transitions

| Before | Action or event | Bounded resolution | Claim ID |
| --- | --- | --- | --- |
| Seven spirits share the Celestial Stone | Close an outline with Draw active | A carrier encloses the group and can move away | SB-002 |
| A live carrier lies by a tight gap | Hold Deflate and contact its interior | The membrane becomes smaller | SB-004 |
| One carrier reaches the winding channel | Maintain the route under airflow and collision | Its shape stretches and rounds out again with the same occupants | SB-006 |
| An occupied membrane reaches the fixed receiver | Let the spirits enter the cube | Stage resolves and the result records seven saved | SB-008 |

## Strategic and experiential structure

Aim repeated bursts from safe angles to let the membrane ride the
route. Reduce its footprint before an especially narrow opening.
A short interruption to inspect the map can expose the next turn.
Collect stardust while aligning to the receiver, or head straight for
delivery if a diversion risks losing the carrier.

## Replay and variation

The route supports smaller or split carriers while the same designated
payload is bound for the same receiver. The recorded route completes
with all seven. Alternative ranks, loss and completion times remain
outside the witnessed baseline.

## Adjacent systems and history

Other worlds use further contents and environment rules. The source
manual describes water, gas, world thresholds and extra rewards.
These are not treated as effects of the first delivery.

## Normalised genome

- Action: ACT-941, ACT-942, ACT-943, ACT-944.
- System Behaviour: SYS-036, SYS-037, SYS-2030.
- Constraint: none.
- Information: INF-657.
- Objective: OBJ-014.
- Time: TIM-003.

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `725` (`GAME-0001`–`GAME-0725`).
- Exact genome matches: none.
- Tied near matches: `GAME-0021` — Cut the Rope (`4 / 15 = 0.266667`).
- Supported combination subsets: none.
- Scan date: 2026-11-25.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
| --- | --- | --- | --- |
| [Cut the Rope (GAME-0021)](../a-f/cut-the-rope.md) | OBJ-014, SYS-036, SYS-037, TIM-003 | Both route a moving payload to a receiver under live physics and can collect objects along the way. Cut the Rope intervenes by removing supports from a swinging candy. Soul Bubbles creates the carrier and aims airflow, then can reduce or divide the membrane to negotiate a constriction. | Near, `0.266667`. |

## Taxonomy impact

The four touch actions have different inputs or mode-dependent
outcomes. Local elastic clearance can preserve a payload without
the agent shrinking it. The fixed receiver reuses the usual payload
goal without representing it as player-avatar arrival. No sound-based
input or load-bearing stationary ropes enter the signature.

## Negative results

- The recorded game frames and booklet do not measure a
  native force curve or prove the exact physical button presses.
- Passage contact can change silhouette with the same spirits.
  No assumption about deformation through arbitrary walls is needed.
- The map input selects the view and does not issue a movement
  waypoint to the group.
- The demonstrated full group does not require that all seven
  are alive in every successful trial.
- The recorded first Initiation stage is an empty carrier exercise.
  Its result is separate from the first spirit delivery.

## Delta summary

Record touch-driven airflow, four carrier interactions, elastic clearance
and view control in the first complete spirit delivery. Keep the scope
separate from general systems described only for later worlds.

## New facts

- A drawn closed loop creates a carrier that can be blown.
- A constrained live carrier can keep its payload as its shape changes.
- The cube takes the spirits before the normal stage result appears.

## Principles and design implications

A deformable carrier makes passage fit part of steering. Separate
normal propulsion from shape editing on a shared input surface.
Let a temporary overview inform routing without moving the cargo.

## Puzzle or game generation potential

Set up a grouped payload at an initial source, one drawable membrane,
an open corridor, one constriction, stardust and one fixed receiver.
Trace a valid airflow route and verify that view movement, geometry
editing and delivery resolve independently.

## New genes

- ACT-941
- ACT-942
- ACT-943
- ACT-944
- SYS-2030
- INF-657

## New combinations

None matched the ten-gene signature after checking all 274 verified combinations.

## Taxonomy changes

[Taxonomy Change 472](../../../research/taxonomy-changes/TAXONOMY_CHANGE_472.md).

## Next recommended game

Miniatures on macOS is the next Selection 063 unit.

## Why this game

The DS touch input changes a deformable carrier’s movement and
clearance during a complete delivery with a fixed receiver.

## Review status

Reviewed 2026-11-25 for the English Nintendo DS commercial release.
The record ends at the first spirit-delivery result in Tir Tairngire.
