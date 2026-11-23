---
game_id: GAME-0596
slug: custom-robo
game_title: "Custom Robo"
analysis_status: reviewed
reviewed: 2026-11-21
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-161
    - ACT-341
    - ACT-792
    - ACT-793
  system:
    - SYS-036
    - SYS-215
    - SYS-369
    - SYS-453
    - SYS-1756
    - SYS-1757
  constraint: []
  information:
    - INF-179
    - INF-560
  objective:
    - OBJ-323
  time:
    - TIM-003
---

# Game: Custom Robo

Use the [canonical vocabulary and signature rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
A folded fighter's launch direction determines where it lands. Its own
countdown determines when it can act. These are separate decisions before
a live duel played around walls, attacks and knockdown states.

## Analysis scope

- Version / ruleset: original English North American Nintendo GameCube
  retail release, May 10, 2004, product DOL-GXCE-USA. Story Mode, A New
  Journey, Day 1 Employment, first fight against a Burglar in Basic
  Arena. Ordinary controls and stock newly registered parts, with
  no imported unlocks or altered rules. North American retail disc
  revision, save hash and individual frame timings are unverified.
- Structured analysis target: `PLAT-NINTENDO-GAMECUBE` in
  [platform coverage](../../platforms/games.json).
- Entry: the protagonist can move in the Research Lab after Harry's
  scripted defeat, before examining and registering the blue Ray 01
  cube. Register it and approach the first burglar. Hear Harry's
  explanation, inspect the opponent and arena in Battle Preparation,
  and start the ordinary duel. Earlier interview choices are outside
  this scope.
- Primary decision loop: aim the folded Ray 01 toward an opening
  position, accelerate its unfolding if useful, and use the closest
  walls, open lanes and jumps to shift between attacking and avoiding
  the other robo's pressure. Check both HP gauges, the knockdown state
  and time while deciding whether to close distance, fire or move to
  cover. Gunfire, the aimed bomb and the hunting pod deliver different
  trajectories with the starting hardware.
- Positive exit: win the first duel by depleting Splendor's HP before
  time-over or by leading strictly in remaining HP at expiration.
  Accept settlement, regain lab control and stop before the next
  burglar's battle. The observed pass is a KO. The ordinary first
  victory confers no new battle part.
- Negative exit: zero player HP, losing on HP at time-over, an equal
  time-over in Story Mode or retiring from the live match settles a
  loss. The instructions describe return to the scene immediately
  before the fight. A temporary knockdown at positive HP is within the
  attempt and may progress through reboot to combat.
- Included: the acquisition gate, opponent/arena data, optional
  ungraded practice in preparation, stock body and part roles, aimed
  scheduled launch, post-landing activation, embodied movement,
  weapon channels, geometry, damage, knockdown, conditions, clock,
  story win and immediate retry boundary.
- Excluded: alternative unlocked parts and dress colours, precise
  weight, impact, flight and reboot coefficients, invulnerability
  frames, exact timer-start event and measured inputs, neutral or
  simultaneous-KO adjudication, persistence beyond the first return,
  later burglar fights, more opponents, part generators, Arcade,
  VS, Grand Battle, Japanese and other franchise versions.
- Optional deeper modules: first genuinely variable loadout and a
  later fight involving tags, part awards or additional opponents.
- Direct-play status: no GameCube, disc image, emulator execution,
  savestate or inputs used. The North American booklet establishes
  rules and two independent English GameCube recordings were inspected
  via silent stills. A first-bout KO and handoff are visible. The
  time-over and defeat branches are documentary, with no direct
  first-bout sample of their local state.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
| --- | --- | --- | --- | --- | --- |
| CR-001 | The first Research Lab human-controlled fight follows the registration of Ray 01 as the protagonist's robo. Harry's earlier authored loss is neither an attempt by the player nor a reusable starting build. | Observation | Corroborated | High | M1, W1 13:40–15:20, W2 16:20–18:10, R1, R2 |
| CR-002 | One-on-one Battle Preparation discloses Splendor and Basic Arena. On a fresh route Ray 01 has Basic Gun and Standard bomb, pod and legs. The menu is present, but no alternate acquired mechanical loadout is available in the scoped fresh state. Official practice can test the same parts without the scored opponent or time limit. | Observation | Corroborated | High | M1 pp. 17–22, W1 15:20–15:30, W2 18:20–18:30, R1, R2 |
| CR-003 | The control stick aims from the cannon while the countdown runs. The shared launcher boundary fires the cubes; launch precedes landing and each own countdown. | Confirmed | Direct | High | M1 pp. 10, 23–24, W1 15:40–15:50, W2 18:40–18:50 |
| CR-004 | Nintendo documents a randomly initialized countdown from one to six after landing and four possible face-button inputs to accelerate it. Ordinary attack control begins when the same cube unfolds. The recordings corroborate the scheduled start and transition, without revealing the random draw or button timings. | Confirmed | Direct | High | M1 pp. 10, 23–24, W1 15:40–15:50, W2 18:40–18:50 |
| CR-005 | Default movement and jump permit using the barriers and firing from a different height. B fires the gun. X is the default charge. R launches a bomb and can expose a movable targeting marker, while L launches a pod with an adjustable initial direction. Both indirect devices are supplied on the first build; later verbal teaching of their controls does not grant the parts. | Observation | Corroborated | High | M1 pp. 10–11, R1–R3, W1 15:20–16:40, W2 18:20–19:40 |
| CR-006 | Splendor and Ray 01 share their starting weapon names, with different chassis. A direct shot, ranged bomb detonation and moving pod offer distinct paths through the same room. Obstacles allow cover from some paths. The captures show explosions in the arena, without identifying every explosive or numeric hit property. | Observation | Corroborated | Medium | M1 pp. 19–21, R1–R3, W1 15:50–16:40, W2 18:50–19:40 |
| CR-007 | Both robos expose HP and a separate knockdown meter. An ordinary exchange can produce HIT and DOWN; REBIRTH is the post-knockdown reboot, distinct from destruction and deployment. An exact hit-stun length or guaranteed invulnerability during reboot is outside the evidence. | Observation | Corroborated | High | M1 pp. 24–25, W2 18:50–19:30 |
| CR-008 | The bout ends on HP depletion or time-over. The side with more HP wins a time-over; Story ties and retirements are losses. Defeat brings the player to the prior scene, so play can return to preparation. | Confirmed | Direct | High | M1 pp. 23–25, R1; the first-fight time-over and loss states are documentary |
| CR-009 | The observed first KO settles the match and returns to the lab, where the next burglar is a distinct encounter. It gives no new part. A save notice is visible on one route; no exact saved fields are claimed. | Observation | Corroborated | High | W1 16:40–17:10, W2 19:40–20:20, R1, R2 |

## Basic data

- North American retail GameCube, Nintendo publisher. Nintendo's product
  history and launch notice establish the release.
- P1: [Nintendo launch dates, April–September 2004](https://www.sec.gov/Archives/edgar/vprr/0404/04046428.pdf),
  original company filing. Use the Americas GameCube line for the
  carrier date.
- P2: [Nintendo launch notice reproduced by Nintendo World Report](https://www.nintendoworldreport.com/news/9569/custom-robo-hits-stores-monday).
  Dates the GameCube edition, supplemented by the catalogued
  [North American packaging](https://www.vgcollect.com/item/2408).
- M1: [Nintendo of America instruction booklet 54093A](https://www.gamesdatabase.org/Media/SYSTEM/Nintendo_GameCube/manual/Formated/Custom_Robo_-_2004_-_Nintendo.pdf),
  original English printed booklet in a scan. Pages 10–11 cover
  controls; 17–22 explain preparation; 23–25 specify timing, gauges
  and results. Nintendo's [manual index](https://en-americas-support.nintendo.com/app/answers/detail/p/50/a_id/16961)
  lists the same title but its linked PDF returned 404 on review.
- `FAM-010` applies to acting while the launch, projectiles, opposing
  robo and round clock continue.

### Reproducible route evidence

- W1: [LongplayArchive, North American GameCube run](https://www.youtube.com/watch?v=n4Bg6ogd740&t=820s).
  Silent stills at 13:40–15:40 establish the blue cube registration,
  initial briefing, preparation and scheduled launch. Stills at
  15:50–17:10 show the first fight, victory scene, save notice and lab
  return. The next launch at about 18:10 is a distinct bout.
- W2: [Mutch Games, A New Journey capture](https://www.youtube.com/watch?v=GYSPb544Rdc&t=980s).
  Silent stills between 16:20 and 18:30 contain the loss of Harry,
  eye-scan registration, briefing and active preparation options.
  The launch near 18:40, exchanges including DOWN, and lab again near
  19:50 support the same boundaries.
- R1: [tjquick69's 2004 North American written route](https://gamefaqs.gamespot.com/gamecube/914967-custom-robo/faqs/30700).
  Day 1 Battle 1 documents both stock loadouts, Basic Arena, practice,
  fast cube activation, retry, no item award and the lab progression.
- R2: [Hyper_Omega's early written single-player route](https://gamefaqs.gamespot.com/gamecube/914967-custom-robo/faqs/38537).
  Day 1 distinguishes the first Splendor and later Metal Ape. The
  equipment list and jump-fire approach corroborate the geometry and
  each weapon family. One earlier summary heading names a different
  arena; the detailed first-bout table and R1 agree on Basic Arena.
- R3: [SpikeDragon's GameCube rules and route notes](https://gamefaqs.gamespot.com/gamecube/914967-custom-robo/faqs/50580).
  The Day 1 first-bout section covers alternate weapons during that
  fight and KO. General combat advice explains approaching with cover
  and distinguishing bomb and pod traffic.

## Mechanical decomposition

### Action Genes

- ACT-341 examines and registers the reachable Ray 01 cube. ACT-008
  covers lab positions and live robo movement and jumping.
- ACT-792 orients the cube's launch before the shared departure.
  Repeated inputs after landing affect its later stage, not aim.
- ACT-161 covers direct attacks from ready openings. ACT-793 sets the
  initial spatial input for the bomb and for the independently
  travelling pod, separate from the gun lane (CR-005, CR-006).

### System Behaviour Genes

- SYS-036 covers traversing trajectories and obstruction by arena
  geometry. SYS-1756 determines unfolding and readiness after landing
  (CR-003, CR-004, CR-006).
- SYS-453 applies the stock chassis and mounted components to movement
  and usable attacks, even with no functional first-fight substitution.
- SYS-215 resolves live movement, firing, contact, HP and enemy
  response. SYS-1757 carries distinct knockdown and reboot while HP
  remains separate (CR-005–CR-007).
- SYS-369 handles the documented return to the prior scene upon
  declared match loss (CR-008).

### Constraint Genes

- No separate gene is needed: readiness belongs to SYS-1756,
  knockdown to SYS-1757 and qualification to OBJ-323.

### Information Genes

- INF-179 exposes the current robot, opposing position, obstacles and
  nearby threats. In preparation the view permits reading the fixed
  rival and arena before entering.
- INF-560 exposes readiness transitions and both current HP and
  knockdown states alongside the live clock (CR-003, CR-004, CR-007).

### Objective Genes

- OBJ-323 requires winning the *single* timed story duel by KO or
  strict HP advantage at time-over (CR-008, CR-009).

### Time Genes

- TIM-003 applies to scheduled launch and live attacks, with a
  globally advancing match clock during the duel (CR-003, CR-008).

## Reproducible transitions

| Initial state | Intervention | Discriminating result | Evidence |
| --- | --- | --- | --- |
| Research Lab under attack; Harry defeated; player has no authorized combat robo | Approach Ray 01, examine and register it, then address the first burglar | The protagonist can enter their own encounter with the stock configuration | CR-001, CR-002 |
| Opponent revealed before entering | Check the opponent and arena data or test parts in ungraded practice; exit practice before choosing Start Battle | The regular bout uses Basic Arena with the stocks shown. Practice alone changes no story result | CR-002 |
| Cannons occupied and common start count running | Steer the launch direction toward an open side of a nearby barrier | The shared count launches both cubes in their selected directions. A landed cube is not yet a ready combatant | CR-003 |
| Own cube settled and still counting down | Use repeated eligible face-button input or let time run | Readiness arrives sooner with eligible input. The same cube unfolds where it landed | CR-004 |
| Fighter ready and other robot aligned behind cover | Move for a different gun lane or jump, aim a bomb at a point, or send a pod along another route | Direction, height and cover affect whether a shot reaches the opponent. An indirect release can remain active after movement resumes | CR-005, CR-006 |
| Hit robot still has positive HP | Observe separate knockdown and subsequent reboot | Loss of immediate attack control can be temporary. The opponent remains in the same bout | CR-007 |
| Splendor reaches zero HP or one robot leads at time-over | Observe the match settlement | KO or remaining HP decides the winner. The observed first KO returns to the lab before the Metal Ape fight, with no new part granted | CR-008, CR-009 |
| Player is defeated, ties at time-over, or retires from the match | Resolve the result | Story treats it as a loss and returns to the pre-fight scene. Exact save timing and state of a first-fight retry are unverified | CR-008 |

## Strategic and experiential structure

The opening position and first usable instant can be asymmetric even
when both fighters bring similar tools. A landing beside a wall gives immediate access to cover, while a
landing in an open lane exposes both incoming and outgoing fire. Leaving cover can make a direct
opening while putting the robo at risk of a flying bomb or pod.
Downing Splendor changes the immediate pressure without settling the
fight. A vitality advantage has strategic value as the match clock
approaches its terminal comparison.

## Replay and variation

For a reproducible run record retail identity, fresh GameCube Memory
Card state, initial hero and opponent parts, launch direction, each
landed count and button attempts, positions around walls, hit and
knockdown labels, terminal vitality and the lab return. Hold the
initial gear fixed when comparing launch directions. For a separate
negative case use the official retire path or time-over with a tie.
Only the KO and successful return were inspected in the first-fight
recordings. No strategy or order is presented as the only legal win.

## Adjacent systems and history

The original GameCube game has later part rewards and tournament
configurations. In this unit the availability of the customization
screen is evidence of preparation, without a fabricated first-fight
loadout choice. Later alternate builds, special launch coaching and
parts-generator acquisition are distinct units.

## Normalised genome

| Type | Stable genes | Role |
| --- | --- | --- |
| Action | ACT-008, ACT-161, ACT-341, ACT-792, ACT-793 | Movement, direct strikes, registration, launch aim and indirect control |
| System Behaviour | SYS-036, SYS-215, SYS-369, SYS-453, SYS-1756, SYS-1757 | Flight, live combat, retry, equipment, deployment and knockdown |
| Constraint | None | The owning rules capture readiness and victory constraints |
| Information | INF-179, INF-560 | Arena view and distinct readiness, vitality and clock |
| Objective | OBJ-323 | Win the one timed story bout |
| Time | TIM-003 | Forced progression during choices |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `595` (`GAME-0001`–`GAME-0595`).
- Exact genome matches: none.
- Tied near matches: `GAME-0312` — ASTRO BOT (`7 / 24 = 0.291667`).
- Supported combination subsets: none.
- Scan date: 2026-11-21.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
| --- | --- | --- | --- |
| GAME-0312 ASTRO BOT | ACT-008, ACT-161, ACT-341, SYS-036, SYS-215, SYS-369, TIM-003 | Both combine direct movement, context interaction, live attacks and renewed attempts. Sky Garden uses those actions to reach platforms and operate rescue fixtures on a traversal route. Basic Arena requires staging a folded fighter, reading an opponent and ending a duel by KO or the health comparison. | 7 shared of 24; Jaccard 0.291667 |

### Preserved research notes

- Classification result: New gene.

## Taxonomy impact

- [TAXONOMY_CHANGE_342](../../../research/taxonomy-changes/TAXONOMY_CHANGE_342.md)
  adds the scoped rules. No existing definition changes.

## Negative results

- Aiming the cannon does not fire it early. Mashing after landing
  advances readiness without selecting a new landing location.
- DOWN is a local loss of agency, not a KO. Time-over at equal HP is
  a loss in this Story ruleset.
- The first win does not award parts. The option to customize does
  not imply an available alternate mechanical part on a fresh route.

## Delta summary

## New facts

- [Observation | Corroborated | High] The opening splits trajectory
  selection, scheduled shared release and each cube's local startup.

## New genes

- [Observation | Corroborated | Medium] Six additions capture launch
  aim, indirect deployment, unfolding, knockdown/reboot, HUD and one
  story duel's settlement.

## New combinations

- [Observation | Corroborated | High] No new combination proposed.

## Taxonomy changes

- [Observation | Corroborated | High] New definitions supplement
  reused movement, physics, live combat and retry. Earlier signatures
  are preserved.

## New questions

- Measure a native attempt that reaches a Story tie or reboot with
  attack and protection changes recorded. Confirm the first save's
  retained fields separately from the observed lab return.

## Next recommended game

- [Hypothesis | Limited | Medium] Duck Detective: The Ghost of
  Glamping on Nintendo Switch. Check a complete inference boundary
  from an inspected clue to the accepted story deduction.

## Why this game

- [Hypothesis | Limited | Medium] Space and time interact before
  the first shot: the launch aim sets position and the arrival
  countdown sets when the fighter becomes usable.
