---
game_id: GAME-0537
slug: kirby-tilt-n-tumble
game_title: Kirby Tilt 'n' Tumble
analysis_status: reviewed
reviewed: 2026-11-17
combination_ids: []
gene_ids:
  action:
    - ACT-519
    - ACT-668
    - ACT-734
    - ACT-735
  system:
    - SYS-037
    - SYS-578
    - SYS-911
    - SYS-933
    - SYS-935
    - SYS-1028
    - SYS-1363
    - SYS-1554
    - SYS-1555
    - SYS-1556
    - SYS-1557
    - SYS-1558
  constraint:
    - CON-068
    - CON-183
    - CON-685
  information:
    - INF-317
    - INF-521
  objective:
    - OBJ-220
  time:
    - TIM-003
---

# Game: Kirby Tilt 'n' Tumble

Use the [canonical vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
Sensor angles, jump distances, item amounts and course geometry are parameters.

## Analysis scope

- Version / ruleset: original English North American cartridge
  `CGB-KTNE-USA`, April 2001, in a Game Boy Color, ordinary
  single-player adventure on a fresh file, Flat position.
  Exact ROM revision, calibration thresholds and sensor sampling are
  unverified. The licensed Switch release has different physical input
  hardware and is outside the ruleset.
- Entry: hold the console flat at Balance and confirm with A. Start
  a new ordinary adventure and begin at the first controllable
  position in Level 1, course 1. Keep the console's ordinary balance
  controls and leave the side Warp Star and optional special-star
  detours alone.
- Primary decision loop: tilt to roll through the initially enclosed
  track, using light inclination and counter-tilt at edges. Choose
  between the free flick jump and the A-button launch from an occupied
  Jump Hole. Cross directed obstacles and ride clouds, manage
  incoming contact and the running time, take useful clocks or star
  pieces, pass the gate and reach the goal pad.
- Positive exit: touch the goal pad while time remains, settle
  the position-dependent reward and ordinary course clear, and stop
  before controlling Kirby on 1-2. A fall, zero time or zero vitality
  ends a life; with stock remaining, retry from the current return
  anchor. If stock is exhausted, stop at Game Over.
- Included: calibrated roll and flick, ordinary directed holes
  and cloud carrier, bumpers, nearby item transformations, pickups
  and vitality, countdown, the mid-course gate, goal contact and
  goal reward. Excluded: the Warp Star room, the optional item
  roulette, special-star detours and later minigames, later courses,
  Extra Game, alternative hardware or patched controls.
- Direct-play status: no console, ROM, save or motion trace was run.
  The original US manual, Nintendo's released title history, a
  compiled static course map and GBC play accounts establish the
  route. No audiovisual playback. The exact clock value on a
  post-gate restart and gate credit calculation were not verified.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
| --- | --- | --- | --- | --- | --- |
| KTT-001 | The April 2001 North American Game Boy Color cartridge has its own motion sensor. Startup Balance takes a reference from a level handheld; Select can reset that balance. Position Flat differs from the alternate GB posture. | Confirmed | Corroborated | High | P1, P2, P3, S1 |
| KTT-002 | Sustained inclination rolls Kirby spatially in the tilt direction. A quick upward flick triggers the ordinary jump. The Control Pad moves the view rather than steering the ball. | Confirmed | Corroborated | High | P1, P2, S2 |
| KTT-003 | The first course has a starting corridor, bumpers, round Jump Holes and a first low barrier. Enter the ordinary hole before committing A in its indicated direction; a hole may have an advancing arrow, but no square-hole steering rule is needed here. | Confirmed | Corroborated | High | P1, S3, S4 |
| KTT-004 | Ride the cloud from one supported area to the next and dismount with A. Blue bumpers rebound Kirby on contact; red ones launch him upward. Unsupported falls cost a life, unlike ordinary bumper contact. | Confirmed | Corroborated | High | P1, S3, S4, S5 |
| KTT-005 | Flicking can change local objects before pickup. The ordinary yellow-piece and small-clock types trade places. Manual-specified stopwatch types credit distinct amounts, and a yellow-piece milestone adds a life rather than time. | Confirmed | Corroborated | High | P1, S3, S5 |
| KTT-006 | Normal 1-1 is documented at a displayed start of 200. The clock runs during traversal and reaches loss at zero. Waddle Dee contact reduces vitality, which has a separate terminal and can be recovered by appropriate items. | Observation | Corroborated | High | P1, S3, S4 |
| KTT-007 | The gate revises the return point. A life loss before the gate returns to the course origin, a later retry returns to the gate while lives remain, and a post-Game Over Continue begins the course again. Sources report extra time at a crossed gate, but its exact transition is unverified. | Confirmed | Corroborated | High | P1, S3, S4, S6 |
| KTT-008 | Contact with the fixed goal pad clears the course before expiry. Landing position determines the goal reward. Course clearance saves progression and special-star collection is not required. | Observation | Corroborated | High | P1, S3, S4, S5 |

## Basic data

- Nintendo, North American English Game Boy Color cartridge,
  April 2001. Nintendo's retrospective gives the month. The scoped
  mechanism is motion-controlled rolling, timing and authored launches.
- Families: physics and object manipulation, and real-time system pressure.
- Sources accessed 2026-11-17:
  - **P1** — [Nintendo North American instruction booklet](https://archive.org/download/NintendoGameBoyColorManuals/Kirby%20-%20Tilt%20%27n%27%20Tumble%20%28USA%29.pdf),
    printed pages 4–13 and 16–22. Inspected the tilt and Balance
    illustrations, life return diagram, HUD, bumpers, clouds, round
    holes, pickups and saved course clear.
  - **P2** — [Nintendo's Kirby development history](https://iwataasks.nintendo.com/interviews/wii/kirby-dream-land/0/3/),
    the English retrospective's reference to the April 2001 Game Boy
    Color game. [Nintendo's Switch catalogue announcement](https://www.nintendo.com/en-ca/whatsnew/june-update-see-which-game-boy-super-nes-and-nes-games-were-added-for-nintendo-switch-online-members/)
    explicitly calls its own controls a replication of the original.
  - **P3** — [US cartridge and board photographs](https://gbhwdb.gekkio.fi/cartridges/CGB-KTNE-0/),
    identifying the exact market, mapper and accelerometer component.
  - **S1** — [US packaging and booklet control transcription](https://www.rfgeneration.com/cgi-bin/getinfo.pl?ID=U-069-S-01720-A),
    for the cartridge number and balance and control reference.
  - **S2** — [Jeff Gerstmann's Game Boy Color play review](https://www.gamespot.com/reviews/kirby-tilt-n-tumble-review/1900-2701119/),
    corroborating ordinary tilt speed and jump gestures on hardware.
  - **S3** — [GBC walkthrough and controls](https://gamefaqs.gamespot.com/gbc/369876-kirby-tilt-n-tumble/faqs/22994),
    and the [contemporary 1-1 star route](https://gamefaqs.gamespot.com/gbc/369876-kirby-tilt-n-tumble/faqs/10781)
    for the checkpoint, goal platform and nearby optional locations.
  - **S4** — [Level 1-1 map and route](https://wikirby.com/wiki/Kirby_Tilt_%27n%27_Tumble_-_Lvl_1-1),
    including start allowance and the Normal / Extra differences,
    plus the [VGMaps original course composite](https://vgmaps.com/Atlas/GB-GBC/#KirbyTiltNTumble)
    inspected as static geometry before artwork.
  - **S5** — [Cloud carry and exit](https://wikirby.com/wiki/Cloud_%28object%29),
    [Stopwatch rules](https://wikirby.com/wiki/Stopwatch) and
    [Goal pad grading](https://wikirby.com/wiki/Goal_Game#Kirby_Tilt_%27n%27_Tumble).
    Distinguish ordinary clouds, standard items and optional bonus rules.
  - **S6** — [Original game mechanics overview](https://wikirby.com/wiki/Kirby%27s_Tilt_%27n%27_Tumble),
    corroborating a gate time extension without supplying the preservation
    or restart details needed to classify an additive checkpoint formula.
- Claim IDs: KTT-001–KTT-008.

## Mechanical decomposition

### Action Genes

- Reuse `ACT-519`: physically tilt the handheld to steer a supported
  rolling body, without directly commanding a position.
- Reuse `ACT-668`: press A at a selected moment while occupying a
  preset round launcher, or dismount the carrying cloud on cue.
- New `ACT-734`: a quick upward tilt commits the ordinary free jump
  without the steady inclination used for rolling.
- New `ACT-735`: explicitly calibrate the physical neutral at Balance
  or reset it with Select.
- Claim IDs: KTT-001–KTT-004.

### System Behaviour Genes

- Reuse `SYS-037`: contact with eligible on-route pickups acquires
  them without ending the course.
- Reuse `SYS-578`: contact damage and compatible recovery update one
  vitality reserve, with loss at zero.
- Reuse `SYS-911`: consuming one life can reinstantiate Kirby to retry.
- Reuse `SYS-933`: the gate changes the subsequent life return anchor.
- Reuse `SYS-935`: the yellow star-piece counter grants a life at a
  declared milestone. The manual specifies every fifty pieces.
- Reuse `SYS-1028`: tilt and ongoing motion interact, so counter-tilt
  adjusts the roll before a wall or open edge.
- Reuse `SYS-1363`: an ordinary moving cloud carries its supported
  rider along the cross-gap track. Pressing A departs; the separate
  steerable cloud types are outside the claimed behaviour.
- New `SYS-1554`: rolling into the round Jump Hole holds the ball.
  Its arrow sets the direction for the occupied hole's A-button release.
- New `SYS-1555`: the flick applies a local item conversion in addition
  to the avatar jump. Repeating the action can select a useful type
  before an eligible item is actually collected.
- New `SYS-1556`: taking a stopwatch adds its typed allowance to the
  currently remaining attempt time.
- New `SYS-1557`: contact with a blue bumper rebounds Kirby, while
  red contact adds the airborne launch.
- New `SYS-1558`: the goal pad accepts broad arrival; its landing zone
  independently determines score or an extra life before settlement.
- Claim IDs: KTT-002–KTT-008.

### Constraint Genes

- Reuse `CON-068`: the current life's countdown expires at zero,
  whether or not the player has cleared most of the route.
- Reuse `CON-183`: finite life stock limits ordinary checkpoint retries;
  Game Over ends the attempt and forfeits that anchor.
- Reuse `CON-685`: a fall beyond the course's supported route ends
  the life. A legal jump to a new support can cross a gap.
- Claim IDs: KTT-004, KTT-006, KTT-007.

### Information Genes

- Reuse `INF-317`: local boards and hint holes disclose rolling,
  launch, flick and cloud controls at the relevant place.
- New `INF-521`: the local course view and live timer, vitality,
  score and star-piece displays accompany independent map panning.
- Claim IDs: KTT-002–KTT-006.

### Objective Genes

- Reuse `OBJ-220`: guide the ball to the fixed goal pad before
  the current clock runs out. The centre is a reward target.
- Claim ID: KTT-008.

### Time Genes

- Reuse `TIM-003`: roll, cloud and hazard timing advance during
  traversal; takeoff and passive waiting share the live deadline.
- Claim IDs: KTT-003, KTT-004, KTT-006.

## Reproducible transitions

| Before | Action or event | Bounded resolution | What it establishes | Claim ID |
| --- | --- | --- | --- | --- |
| Console lies flat at Balance | Press A, select a fresh file, then tilt gently in the corridor | The chosen posture determines the neutral reading and tilt drives rolling | Neutral calibration precedes steering | KTT-001, KTT-002 |
| Kirby occupies the first round Jump Hole below a low barrier | Press A with the direction indicator pointing along the route | Kirby exits on the indicated arc over the barrier | An occupied launcher has a button and directional cue | KTT-003 |
| Kirby is on ordinary turf near an eligible yellow piece | Flick upward and compare the item before collecting it | Kirby jumps and the local piece may become a small stopwatch | Changing type and receiving its effect are distinct | KTT-002, KTT-005 |
| Stopwatch lies on accessible turf with time remaining | Roll into it | Add its amount to the live remainder | Time pickup extends a deadline rather than adding score alone | KTT-005 |
| The moving cloud approaches a ledge | Board it, wait for alignment and dismount with A | Support carries Kirby across open sky to the next approach | Timing governs boarding and dismount | KTT-004 |
| A gate has been crossed and lives remain | Fall past a later edge, or lose the life when time expires | Consume a life and retry at the gate | The checkpoint grants local recovery after life loss | KTT-006, KTT-007 |
| Goal pad is accessible with a positive countdown | Reach an outer pad zone; compare a centre landing on replay | Both can clear the course but grant different rewards | Goal validity differs from position grading | KTT-008 |

## Strategic and experiential structure

The track shifts from enclosed lanes to support separated by sky.
A small tilt preserves turning space, while a sharp flick clears a
local obstruction or changes a nearby item. An occupied round hole
supplies a separate directed leap. The player trades route safety,
clock pickups and final landing precision against the live deadline.
Crossing the gate reduces future replay distance, while retries still
cost finite stock.

## Replay and variation

- Hold the original Game Boy Color and cartridge fixed. Compare steady
  inclination, a short flick on the turf and A while in the first hole.
- Compare rolling directly into a small stopwatch with first flipping
  it into a star piece. Read timer and tally separately.
- Compare one deliberate life loss before crossing the gate and one
  after. The restart clock and simultaneous trigger ordering are
  unspecified.

## Adjacent systems and history

- The North American manual allows both Flat and GB postures. This
  unit uses Flat without making a parity claim about physical feel.
- The right-hand special-star detours and a side Warp Star room
  use the same course but are outside the bounded clear.
- Extra Game's altered obstacles and clocks, and the later exact
  adaptation of physical controls to Switch, are separate packets.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
| --- | --- | --- |
| Action | `ACT-519`, `ACT-668`, `ACT-734`, `ACT-735` | tilt, occupied launch command, flick and neutral calibration |
| System Behaviour | `SYS-037`, `SYS-578`, `SYS-911`, `SYS-933`, `SYS-935`, `SYS-1028`, `SYS-1363`, `SYS-1554`, `SYS-1555`, `SYS-1556`, `SYS-1557`, `SYS-1558` | pickup, vitality, stock, anchor, threshold, rolling, carrier, hole, flip, clock, bumper and goal grading |
| Constraint | `CON-068`, `CON-183`, `CON-685` | deadline, reserve lives and fall |
| Information | `INF-317`, `INF-521` | local instructions, panning and live HUD |
| Objective | `OBJ-220` | fixed goal pad before deadline |
| Time | `TIM-003` | continuous traversal clock |

Canonical signature:

`ACT-519,ACT-668,ACT-734,ACT-735; SYS-037,SYS-578,SYS-911,SYS-933,SYS-935,SYS-1028,SYS-1363,SYS-1554,SYS-1555,SYS-1556,SYS-1557,SYS-1558; CON-068,CON-183,CON-685; INF-317,INF-521; OBJ-220; TIM-003`

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `536` (`GAME-0001`–`GAME-0536`).
- Exact genome matches: none.
- Tied near matches: `GAME-0378` — Super Monkey Ball 2 (`7 / 25 = 0.280000`).
- Supported combination subsets: none.
- Scan date: 2026-11-17.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
| --- | --- | --- | --- |
| `GAME-0378` — Super Monkey Ball 2 | `ACT-519`, `CON-068`, `CON-685`, `OBJ-220`, `SYS-037`, `SYS-1028`, `TIM-003` | Both steer a rolling body on a tilted supported course with a live deadline. The scoped Monkey Ball stage uses a stick, unlimited Story retries and a remaining-time bonus. Kirby uses physical calibration, flicks, directed launch holes, life-limited checkpoint recovery and landing-zone rewards. | Tied near (`0.280000`) |

### Preserved research notes

- New genes: `ACT-734`, `ACT-735`, `SYS-1554`–`SYS-1558`,
  `INF-521`.
- Classification result: `New gene`.
- Evidence and reasoning: calibration is a reference input, not a
  traversal command. A local item change is separate from pickup, and
  the same goal touch can satisfy the stage with a different reward.

## Taxonomy impact

- Registry changes: eight Active additions and fifteen transfers.
- Taxonomy-change record: [TAXONOMY_CHANGE_284](../../../research/taxonomy-changes/TAXONOMY_CHANGE_284.md).

## Negative results

- The Control Pad pans the view. Button movement hacks do not
  establish original steering behaviour.
- A carried cloud is not proof that any fall is recoverable. A red
  special star is distinct from red star pieces and from goal success.
- A useful gate is confirmed as a return point. The independent
  additive-checkpoint gene is not admitted without a verified formula.

## Delta summary

## New facts

- [Observation | Corroborated | High] Tilting sets rolling response;
  flicking can both jump and transform nearby items. A directed
  A-button launch comes from a separate local fixture.

## New genes

- [Observation | Corroborated | High] Eight additions in
  `TAXONOMY_CHANGE_284`.

## New combinations

- [Observation | Corroborated | High] No new combination proposed.

## Taxonomy changes

- [Observation | Corroborated | High] `TAXONOMY_CHANGE_284`.

## New questions

- What exact remaining time and item state survive a spent life
  after this course's gate on unmodified North American hardware?

## Next recommended game

- [Hypothesis | Limited | Medium] Evaluate one bounded Windows case
  in *The Rise of the Golden Idol* under Selection 042.
