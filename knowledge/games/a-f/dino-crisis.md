---
game_id: GAME-0515
slug: dino-crisis
game_title: Dino Crisis
analysis_status: reviewed
reviewed: 2026-11-16
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-009
    - ACT-011
    - ACT-089
    - ACT-131
    - ACT-161
    - ACT-341
  system:
    - SYS-215
    - SYS-578
    - SYS-1429
    - SYS-1457
    - SYS-1458
  constraint:
    - CON-282
    - CON-285
    - CON-296
  information:
    - INF-001
    - INF-115
    - INF-500
  objective:
    - OBJ-004
    - OBJ-026
  time:
    - TIM-001
    - TIM-003
---

# Game: Dino Crisis

Use the [canonical vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
Key identifiers, switch labels, colours and room names are parameters.

## Analysis scope

- Version / ruleset: original 1999 North American English PlayStation disc,
  `SLUS-00922`, fresh `Normal` game with ordinary controller inputs. This is
  a documentary ruleset. No installed disc revision or binary was inspected.
  PlayStation Classics enhancements, the Dreamcast and Windows ports,
  unlocked modes and later difficulty behavior are outside scope.
- Structured analysis target: `PLAT-PLAYSTATION` on the original disc.
- Primary decision loop: recover the yard key and follow the opened route;
  read the four-colour reference, exchange conductor positions and activate
  surface power. On return, navigate the raptor's continued pursuit, weighing
  the cost of shots or treatment against reaching the next gate. Enter the
  facility and use the ventilation route to reach Rick.
- Entry and exit: first ordinary control of Regina in the facility backyard
  after the introductory arrival on Ibis Island. Finish when the first meeting
  with Rick in Control Room 1F resolves, before leaving for Management Office.
  Death ends the attempt. Any available Continue begins a separate attempt
  outside this boundary.
- Included: inspecting and collecting the BG Area Key, Gail's key handoff and
  gate access, optional pushed objects and obtainable supplies, ordered
  conductor arrangement and separate activation switch, the first returning
  raptor, the two yard boundaries, general equipped-shot and injury responses
  applicable during that chase, and the ventilation descent to Rick. The
  ordinary route can reach Rick with the raptor alive and ammunition unspent.
- Excluded: taking the elevator, Management Office and later routes, first
  DDK lock, underground power, special Danger inputs, emergency-box unlocks,
  point-specific save rules, mixing recipes, all later branch choices and
  exact optional supply placement or combat coefficients.
- Potential scoped modules: the later DDK and paired-panel-key route, or the
  two responses to the first voluntary Rick/Gail branch, require separate
  release evidence and complete boundaries.
- Direct-play status: no native console or game executable was used. The
  Capcom manual covers controls and injuries, while the contemporary GamePro
  guide and two independent written routes cover the opening. No video or
  audio was played. Exact collision, damage and difficulty-dependent pickup
  quantities were not measured.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| DC-001 | The scoped original PlayStation release offers a fresh Normal game. The route starts in the facility backyard and reaches Rick in Control Room 1F. | Observation | Corroborated | High | P1, P2, S1, S2 |
| DC-002 | Regina can take the BG Area Key in Material Storage. Returning to the yard with it triggers its transfer to Gail and the generator route becomes accessible. Pushing selected objects can expose optional supplies. | Observation | Corroborated | High | P1, S1, S2, S3 |
| DC-003 | The surface generator has four visible conductors, three exchange inputs and a separate activation switch. Match the referenced red, blue, green, white order. Right, Center, Right solves the evidenced starting arrangement. | Observation | Corroborated | High | S1, S2, S3, S4 |
| DC-004 | On return from power activation, a raptor follows across the lower boundary into the next yard. The following transition to the facility backyard ends this pursuit. The route does not require its defeat. | Observation | Corroborated | High | S1, S2, S3 |
| DC-005 | Direct aim and a compatible loaded weapon permit a shot. Injuries reduce condition, which is read through body animation and blood rather than a numeric meter. Hemostat stops bleeding; the amount of already lost condition calls for separate recovery. | Observation | Corroborated | High | P1, S4 |
| DC-006 | The Office Hallway vent leads through the overhead passage to the Control Room Hall. The first opening and adjacent door complete the route to Rick. | Observation | Corroborated | High | P1, S1, S2, S3 |
| DC-007 | The original and the later digital PlayStation reissue are separate targets. The digital store documents added rewind, quick save and rendering options for the reissue. | Observation | Direct | High | P2 |

## Basic data

- Release / origin: Capcom, 1999, PlayStation. Scope is the North American
  original English disc. The PlayStation listing is a legal reissue link.
- P1: [Capcom North American PlayStation manual](https://www.scribd.com/document/862305768/Dino-Crisis-1999-Capcom-Co-Ltd), text of the original manual, sections on controls, new game, moves, weapons and damage.
- P2: [PlayStation product listing](https://store.playstation.com/en-us/product/UP0102-PPSA07831_00-CLASSICDINO00001), original platform and separately named modern enhancements.
- S1: [GamePro issue 134, November 1999](https://fliphtml5.com/vfnzfk/kznr/GamePro_Issue_134_%28November_1999%29/), Dino Crisis ProStrategy opening route and Facility 1F layout, including the lower and higher pursuit boundaries.
- S2: [Kenny's PlayStation walkthrough](https://gamefaqs.gamespot.com/ps/197128-dino-crisis/faqs/5083), opening yard, BG Area Key, generator and flight through the adjoining yard.
- S3: [PlayStation walkthrough, Part 1](https://gamefaqs.gamespot.com/ps/197128-dino-crisis/faqs/76598/walkthrough), complete route and alternative ammunition-conserving decisions. Its optional supplies carry a stated placement uncertainty.
- S4: [Gunsmith's contemporary PlayStation FAQ](https://gamefaqs.gamespot.com/ps/197128-dino-crisis/faqs/5075), independent corroboration of the two-conductor exchanges and visible injury cues. Its Japanese menu description does not establish English labels or edition parity.
- Family: `FAM-017`, ordered dependency sequencing. The key, accessible
  room, matched panel, separately restored power and vent traverse are
  distinct prerequisites or transitions.

## Mechanical decomposition

| Type | Active genes | Scoped interpretation |
|---|---|---|
| Action | ACT-008, ACT-009, ACT-011, ACT-089, ACT-131, ACT-161, ACT-341 | Walk or run, push an eligible object, exchange a designated adjacent pair, collect a scene item, consume medicine, commit a compatible shot and operate addressed fixtures. |
| System Behaviour | SYS-215, SYS-578, SYS-1429, SYS-1457, SYS-1458 | Resolve real-time hostile attacks and injuries, stop a bleed separately from replacing lost health, validate and apply power, and carry one chase through an eligible boundary before cutting it off. |
| Constraint | CON-282, CON-285, CON-296 | Progress follows authored prerequisites; shots require compatible ready equipment; a locked route depends on its matching key or authorised handoff. |
| Information | INF-001, INF-115, INF-500 | Read the panel's visible current state and reference; perceive the nearby threat through local cues; infer health from motion and visible bleeding. |
| Objective | OBJ-004, OBJ-026 | Reconstruct the generator arrangement and reach the control-room meeting. |
| Time | TIM-001, TIM-003 | Each panel exchange resolves before the next selection; real-time pursuit continues during live route inputs. |

## Reproducible transitions

| Before | Command or event | Result | Claim IDs |
|---|---|---|---|
| Material Storage is reachable and yard route is secured | Collect the BG Area Key, return to the yard and trigger the gate interaction | Gail takes the key and the adjoining yard becomes reachable. Carrying a different supply does not replace the key. | DC-002 |
| Optional object blocks a supply | Face and push the eligible crate or shelf | The object leaves its contact position and the supply can be collected with a separate action. Pickup identity and quantity are not fixed here. | DC-002 |
| Surface power is off and conductors are out of order | Inspect the reference and choose Right, Center, Right at the untouched first panel | Each button exchanges its adjacent pair. The row becomes red, blue, green, white. | DC-003 |
| The conductors match the adjacent reference | Use the separate wall activation switch | Surface power is restored after confirming the configuration. Merely inspecting the board or leaving it arranged does not operate that switch. | DC-003 |
| Power is active and Regina exits to the passage | Pass the return trigger and run across the first yard boundary | The raptor continues the chase into the adjacent yard. Saving ammunition remains viable. | DC-004 |
| Regina is still pursued in the adjoining yard | Cross back into the facility backyard | The documented raptor does not cross the second barrier. The run can continue with the raptor alive. | DC-004 |
| The threat is reachable and a compatible firearm is ready | Commit an ordinary shot, or keep running without one | Fire consumes ammunition. Defeating the raptor is optional. Exact hit count, staggering and damage are outside the evidence. | DC-004, DC-005 |
| Regina has a bleeding injury | Spend an eligible Hemostat | Stops the ongoing bleed. Already lost health is a separate condition from the bleed; a basic Hemostat does not refill it. | DC-005 |
| Regina reaches the Office Hallway | Enter the vent, descend through the first opening and enter the nearby Control Room door | The meeting with Rick settles the first surface-power route. | DC-006 |

## Strategic and experiential structure

The panel is a small arrangement problem embedded in a real-time route. The
row can be read and changed without live pursuit. Once the raptor is active,
the decision is whether to spend ammunition or keep moving. The first fence
is not a universal stop: the same raptor follows across it but does not
continue across the next documented boundary. The ventilation route then
provides the inside connection to the required room.

## Replay and variation

The authored objective, key handoff, generator target and first meeting are
stable within the documentary route. A player can bypass optional supplies,
finish without shooting or choose to engage. Different health and carried
supplies are possible. The guides disagree about placement or identity of
some supplies, so neither fixed contents nor a specific random-selection
algorithm enters the signature.

## Adjacent systems and history

A graph of keys and fixtures is shared with other bounded survival-horror
openings. Here an exact conductor arrangement and separate confirmation are
central to clearing the entry route. A pursued passage boundary can admit a
hostile, so an ordinary room change cannot be treated as guaranteed cover.
No full-campaign branch or parity claim follows from this opening.

## Normalised genome

| Type | Active gene IDs | Parameters |
|---|---|---|
| Action | ACT-008, ACT-009, ACT-011, ACT-089, ACT-131, ACT-161, ACT-341 | Traversals, pushable objects, three conductor exchanges, key, supplies and fixtures |
| System Behaviour | SYS-215, SYS-578, SYS-1429, SYS-1457, SYS-1458 | Live injury, stop-bleed treatment, power confirmation and successive pursuit bounds |
| Constraint | CON-282, CON-285, CON-296 | Key authorisation, compatible ready weapon and authored prerequisites |
| Information | INF-001, INF-115, INF-500 | Visible configuration, nearby threat cues and bodily injury cues |
| Objective | OBJ-004, OBJ-026 | Four-colour goal and first meeting with Rick |
| Time | TIM-001, TIM-003 | Discrete exchanges and live pursuit |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `514` (`GAME-0001`–`GAME-0514`).
- Exact genome matches: none.
- Tied near matches: `GAME-0430` — Silent Hill (`12 / 32 = 0.375000`).
- Supported combination subsets: none.
- Scan date: 2026-11-16.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0430` Silent Hill | ACT-008, ACT-089, ACT-131, ACT-161, ACT-341, SYS-215, SYS-578, CON-282, CON-296, INF-115, OBJ-026, TIM-003 | Both openings use live movement and combat under scarce supplies along an authored access route. Silent Hill uses fog, radio and illumination while gathering three house keys. Dino Crisis requires an ordered conductor panel, a separate power commit and an escape across unequal raptor boundaries. | Near, `0.375000` |

## Taxonomy impact

- See [TAXONOMY_CHANGE_262](../../../research/taxonomy-changes/TAXONOMY_CHANGE_262.md).

## Negative results

- The raptor's crossing of the low fence does not establish a universal
  follow-through rule for all dinosaur types or all doors.
- Displayed movement and blood communicate condition without an exact
  health meter. No exact rate or amount is propagated from the manual.
- The retained configuration at the first panel does not establish the
  basement's battery installation or a DDK code submission.

## Delta summary

## New facts

- [Observation | Corroborated | High] The first panel uses adjacent pair
  exchanges followed by a separate power switch. DC-003.
- [Observation | Corroborated | High] The returning raptor persists across
  one documented boundary and stops at the following barrier. DC-004.

## New genes

- SYS-1457, SYS-1458 and INF-500.

## New combinations

- None. See the full proper-subset scan in Corpus comparison.

## Taxonomy changes

- Three additions and nineteen transfers; see TAXONOMY_CHANGE_262.

## New questions

- A controlled original-console replay could distinguish the exact trigger
  and fallback behavior when the first raptor is interrupted before the fence.

## Next recommended game

- `GAME-0516` Hi-Fi RUSH, Xbox Series X|S released base game.
