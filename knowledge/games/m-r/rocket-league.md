---
game_id: GAME-0177
slug: rocket-league
game_title: Rocket League
analysis_status: reviewed
reviewed: 2026-08-28
combination_ids:
  - COMB-0175
gene_ids:
  action:
    - ACT-290
    - ACT-308
    - ACT-309
    - ACT-310
  system:
    - SYS-457
    - SYS-462
    - SYS-539
    - SYS-540
    - SYS-541
    - SYS-542
  constraint:
    - CON-456
    - CON-457
    - CON-458
    - CON-459
  information:
    - INF-116
    - INF-222
  objective:
    - OBJ-101
  time:
    - TIM-003
---

# Game: Rocket League

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Parameters describe
gene instances but do not enter the signature.

## Analysis scope

- Version / ruleset: Rocket League `v2.72` on PC; one online Private Match,
  Soccar, DFH Stadium, `3v3`, no bots, default team colours, five-minute match,
  default mutators and six human-controlled cars. No match administrator.
- Primary decision loop: read the ball, car orientation, teammates, opponents,
  score, clock and boost; steer, throttle, brake, powerslide, jump, dodge or
  boost; let car and ball physics, contacts, bumps and demolitions resolve;
  rotate between challenge, support and defence; then convert a legal ball
  crossing into a goal before regulation or sudden-death settlement.
- Entry and exit: begins at the opening `0–0`, `5:00` kickoff with three blue
  and three orange cars in standard spawn positions; ends when regulation
  expires with one team ahead or, after a tie, when the first overtime goal
  settles the match.
- Included: dedicated car control; throttle, reverse, steering, braking and
  powerslide; jump, double jump, directional dodge, aerial orientation and flip
  reset; finite boost and arena pads; one freely moving ball; enclosed curved
  arena surfaces; car-ball and car-car contact; bumps, supersonic demolitions,
  brief respawn and current side-relative respawn choice; goals, score, kickoff
  resets, the running match clock, zero-second live-ball continuation and
  unlimited sudden-death overtime.
- Excluded: Casual and Competitive matchmaking, ranks, MMR, tournaments, RLCS
  series rules beyond the reproducible match settings, bots, split-screen,
  spectators and replays; training; Hoops, Snow Day, Dropshot, Rumble, Knockout
  and limited-time modes; mutator changes; Rocket Pass, challenges, XP,
  inventory, trading, cosmetics, clubs and account progression.
- Potential scoped modules: ranked `3v3`; a best-of series; `1v1` or `2v2`;
  alternate-ball and alternate-goal modes; training and replay analysis.
- Direct-play status: not conducted. Current official patch notes pin `v2.72`
  and document flip-reset, boost-pad, demolition and respawn behaviour; the
  official 2026 RLCS rulebook supplies a reproducible DFH Stadium `3v3`, no-bot,
  no-mutator, five-minute private-lobby contract. Stable default Soccar
  transitions are corroborated by official mutator and gameplay notes.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `RL-001` | `v2.72` is the current reviewed Rocket League ruleset | Confirmed | Direct | High | P1 |
| `RL-002` | The scoped private match reproducibly uses DFH Stadium, `3v3`, no bots, no mutators and a five-minute clock | Confirmed | Direct | High | P2, P3 |
| `RL-003` | Each human continuously controls one dedicated car through ground, wall and aerial movement | Observation | Corroborated | High | P4–P6 |
| `RL-004` | Jump, dodge and flip-reset eligibility create a separate aerial-action boundary | Confirmed | Direct | High | P4, P5 |
| `RL-005` | Boost is stored, spent on thrust and replenished through spatial pads whose large-pad recharge is visible | Confirmed | Corroborated | High | P4, P5 |
| `RL-006` | One shared ball remains live through car contact, arena bounce and deflection until a valid goal or match-phase terminal | Observation | Corroborated | High | P3, P6 |
| `RL-007` | Supersonic contact may demolish a car, followed by a brief same-match respawn and current side-relative spawn choice | Confirmed | Direct | High | P1, P6 |
| `RL-008` | A valid goal increments one team and resets cars and ball to a kickoff | Observation | Corroborated | High | P3, P6 |
| `RL-009` | Regulation ends when one team leads; a tie continues into sudden-death overtime and the live ball may continue at zero | Observation | Corroborated | High | P2, S1 |
| `RL-010` | The match view exposes ball/car context, boost, teams, score, clock and overtime state | Confirmed | Corroborated | High | P4, P5 |

## Basic data

- Release / origin: Psyonix; Rocket League released in 2015 and the reviewed
  live PC ruleset is `v2.72`, released 2026-08-04.
- Platform or physical form: online real-time vehicle-sport simulation on PC;
  the current official rulebook also supports console platforms.
- Puzzle family: physics and object manipulation; tactical forecast and
  counterplay; real-time system pressure; agent routing and coordination.
- Primary sources:
  - **[P1]** [Rocket League Patch Notes v2.72](https://www.rocketleague.com/news/rocket-league-patch-notes-v2-72),
    for the current version, kickoff and post-demolition spawn corrections.
  - **[P2]** [RLCS 2026 official rules](https://us-west-2-epicgames.graphassets.com/cmkr1i7c9047e07n0es5291ez/cmossrx9k14cn07oh32kssz7g),
    section 4.1.1, for DFH Stadium, `3v3`, no bots, no mutators, five minutes,
    name/password hosting and default colours.
  - **[P3]** [official competitive-rules index](https://www.rocketleague.com/competitive/rules),
    for the currency and provenance of the 2026 rulebook.
  - **[P4]** [Rocket League Patch Notes v2.66](https://www.rocketleague.com/news/rocket-league-patch-notes-v2-66),
    for flip-reset feedback and the ten-second large-boost-pad recharge.
  - **[P5]** [Rocket League Patch Notes v2.70](https://www.rocketleague.com/news/rocket-league-patch-notes-v270-season-23-live),
    for post-demolition spawn selection, car/ball speed display, hitboxes,
    airborne car state and configurable starting boost evidence.
  - **[P6]** [Rocket League v2.49 official notes](https://www.rocketleague.com/news/rocket-league-patch-notes-season-18-live),
    for private-match default jump, ball, gravity, dodge, goal, demolition and
    goal-reset boundaries distinguished from optional mutators.
- Secondary source:
  - **[S1]** [Rocket League Wiki gameplay overview](https://rocketleague.fandom.com/wiki/Gameplay),
    used only to corroborate stable zero-second continuation and sudden-death
    overtime, not current version or private-match configuration.
- Reproducible control: **[V1]** repository-side transition trace across
  `P1`–`P6` and `S1`; rules reasoning, not a claim of direct play.
- Claim IDs: `RL-001`–`RL-010`.

## Mechanical decomposition

### Action Genes

- Existing gene: `ACT-290`, directly steer and accelerate the dedicated car.
- New genes: `ACT-308`, commit jump, dodge or aerial orientation; `ACT-309`,
  spend stored boost for directed thrust; `ACT-310`, choose an eligible
  side-relative respawn after demolition.
- Parameters: car body/hitbox, steering, throttle, reverse, brake, powerslide,
  jump timing, dodge direction, orientation, boost amount and spawn side.
- Claim IDs: `RL-003`–`RL-005`, `RL-007`.

### System Behaviour Genes

- Existing genes: `SYS-457`, resolve the one live ball through contact and free
  motion; `SYS-462`, register a valid goal, update score and reset kickoff.
- New genes: `SYS-539`, integrate rocket-car motion across ground, walls and air;
  `SYS-540`, transfer arena-pad charge into the car's boost reserve and spend it
  as thrust; `SYS-541`, resolve bumps, demolition and timed respawn; `SYS-542`,
  advance regulation, zero-second continuation and sudden-death overtime.
- Resolution order: accept simultaneous car inputs; integrate car and ball
  movement; resolve pad pickup and boost thrust; resolve car-ball and car-car
  contacts; on a valid goal update score and rebuild kickoff; otherwise advance
  the clock and classify regulation or overtime settlement.
- Parameters: velocity, orientation, traction, gravity, contact impulse, pad
  state, boost reserve, demolition threshold, respawn delay, score and clock.
- Claim IDs: `RL-003`–`RL-009`.

### Constraint Genes

- New genes: `CON-456`, enclosed arena geometry keeps ordinary contact live;
  `CON-457`, capped boost and pad availability gate powered thrust; `CON-458`,
  airborne jump/dodge actions require current reset eligibility; `CON-459`,
  regulation and zero-second state gate the transition to settlement or overtime.
- Scarce strategic resources: boost reserve, ready large pads, car orientation,
  recovery time after a challenge, defensible field position and match time.
- Claim IDs: `RL-003`–`RL-009`.

### Information Genes

- Existing gene: `INF-116`, expose teams, score, clock and phase.
- New gene: `INF-222`, expose the controlled car, shared ball, field context,
  boost reserve, nearby participants and eligible flip-reset feedback.
- Claim IDs: `RL-004`, `RL-005`, `RL-010`.

### Objective Genes

- New gene: `OBJ-101`, settle one Soccar match with more valid goals than the
  opposing team, including the first overtime goal when regulation is tied.
- Success, evaluation and failure: a regulation lead at expiry or first
  overtime goal wins; trailing at expiry or conceding in overtime loses; no
  draw survives the scoped terminal.
- Claim IDs: `RL-008`, `RL-009`.

### Time Genes

- Existing gene: `TIM-003`, cars, ball, boost opportunities, opponents and the
  match clock advance in real time while inputs remain available.
- Claim IDs: `RL-003`–`RL-009`.

## Reproducible transitions

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Six cars occupy opening spawn points at `0–0`, `5:00` | Let the countdown finish and accelerate | Ball begins centred and all cars enter live simultaneous control | Explicit reproducible entry and kickoff geometry | `RL-002`, `RL-003` |
| Controlled car is grounded with a ready jump | Jump, orient and apply a directional second input | Car leaves the surface; a legal second input becomes a dodge, while air-roll and boost alter orientation and velocity | Ground and aerial authority are distinct | `RL-003`, `RL-004` |
| Car passes over a ready large boost pad | Continue through the pad, then boost | Pad becomes unavailable, reserve fills to its cap and thrust consumes reserve until released or empty | Spatially replenished finite acceleration | `RL-005` |
| Fast car approaches the ball off-centre | Steer through contact | Contact impulse changes ball velocity and spin; neither side receives abstract possession | Shared physical ball rather than turn ownership | `RL-006` |
| Supersonic car reaches an opponent from a legal collision line | Complete car contact | Opponent is demolished, loses control briefly and may choose an eligible own-side respawn before returning | Temporary removal inside continuous team play | `RL-007` |
| Whole ball crosses the orange goal plane | Complete crossing | Blue score increments; ball and cars rebuild into the next kickoff | Goal geometry changes score and phase | `RL-008` |
| Clock reaches `0:00` while the ball remains live above the floor | Keep the ball airborne | Play continues until a goal or valid grounding; only then does score comparison settle or start overtime | Zero is a conditional, not immediate, terminal | `RL-009` |
| Regulation reaches a tied grounded-ball terminal | Continue into overtime | Clock changes to overtime and the first subsequent legal goal immediately settles the winner | No accepted draw in the scoped match | `RL-009` |

## Strategic and experiential structure

- Local decision: challenge the ball, conserve or spend boost, recover the car's
  orientation, pass through contact, shoot, clear or shadow an opponent.
- Medium-term planning: rotate one car toward the challenge, one into support
  and one behind the play; route through boost pads without abandoning goal
  coverage; anticipate wall and corner bounces.
- Long-term structure: convert pressure and controlled rebounds into a goal
  advantage while preserving enough defensive depth to survive counterattacks
  through regulation or one sudden-death transition.
- Common heuristics: avoid double-committing two teammates; keep the third car
  behind the ball; use small pads along a useful route; land on wheels; prefer a
  controlled clear over a weak central touch; change risk with score and time.
- Failure attribution: visible contact, velocity, boost, score and clock make
  most consequences legible; simultaneous opponents, latency and chained
  rebounds can make ownership of a lost challenge jointly caused.
- Player-trust factors: stable hitboxes, readable pad availability, consistent
  bounces, deterministic goal plane, visible teammate labels and prompt respawn.
- Claim IDs: `RL-003`–`RL-010`.

## Replay and variation

- What changes between sessions: human decisions, kickoff roles, ball bounces,
  boost routes, challenges, demolitions, score path and overtime occurrence.
- Randomness or procedural generation: arena and starting contract are fixed;
  default gameplay is driven primarily by simultaneous physical input. A missed
  post-demolition respawn choice may retain bounded random spawn selection.
- Multiple viable strategies: ground possession, wall play, aerial pressure,
  counterattack, demolition-supported offence or conservative rotation can all
  pursue the same goal comparison.
- Typical replay motive: mechanical execution, coordination, alternative
  rotations, opponent adaptation and tighter boost economy.
- Claim IDs: `RL-003`–`RL-010`.

## Adjacent systems and history

- Direct predecessors: Supersonic Acrobatic Rocket-Powered Battle-Cars supplies
  the vehicle-Soccar lineage; no earlier rules are imported into this record.
- Variants: ranked playlists add rating; other player counts alter spacing;
  alternate modes replace ball, arena or scoring rules.
- Similar games: EA SPORTS FC 26 shares one live ball, two teams, goal scoring,
  score and real-time pressure; Forza Horizon 6 shares dedicated car control and
  live vehicle physics.
- Important differences: Rocket League gives each human one persistent car,
  replaces footballers, passing commands, offences and out-of-bounds restarts
  with enclosed free-contact physics, aerial dodge/boost control, demolitions,
  zero-second continuation and sudden-death overtime.
- Claim IDs: `RL-002`–`RL-010`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-290`, `ACT-308`–`ACT-310` | hitbox, movement input, jump, boost and respawn side |
| System Behaviour | `SYS-457`, `SYS-462`, `SYS-539`–`SYS-542` | contact, pad recharge, demolition delay and clock |
| Constraint | `CON-456`–`CON-459` | arena, boost cap, dodge window and zero-second state |
| Information | `INF-116`, `INF-222` | camera, labels, boost meter, score and clock |
| Objective | `OBJ-101` | selected team and final score |
| Time | `TIM-003` | five-minute regulation and unlimited overtime |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `176` (`GAME-0001`–`GAME-0176`).
- Exact genome matches: none.
- Tied near matches: `GAME-0163` — EA SPORTS FC 26 (`4 / 34 = 0.117647`).
- Supported combination subsets: `COMB-0175`.
- Scan date: 2026-08-28.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0163` — EA SPORTS FC 26 | `SYS-457`, `SYS-462`, `INF-116`, `TIM-003` | Both keep one shared ball, team score and clock live and turn a legal goal crossing into score. Rocket League replaces switchable eleven-player football, targeted passes, refereed offences, goalkeeper AI and an accepted regulation draw with six directly driven cars, enclosed contact, aerial dodge/boost control, demolition respawn, zero-second continuation and sudden-death overtime | Near, `0.117647` |

### Preserved research notes

- New genes: `ACT-308`–`ACT-310`, `SYS-539`–`SYS-542`, `CON-456`–`CON-459`,
  `INF-222` and `OBJ-101`.
- Classification result: `New gene` and new verified interaction combination.
- Evidence and reasoning: five existing generic boundaries fit without change;
  thirteen new records isolate vehicle-Soccar actions, resources, contact and
  terminal rules absent from the earlier football and racing packets.

## Combination status

- `COMB-0175` is a verified strict 15-gene subset coupling dedicated car
  control, aerial authority, boost routing, shared-ball contact, enclosed arena
  geometry, demolition and overtime goal settlement.
- Earlier verified combinations are tested deterministically after registration.

## Taxonomy impact

- Registry changes: thirteen new Active genes, links on five reused genes,
  `COMB-0175` and four existing family memberships.
- Taxonomy-change record: none; no prior lifecycle, definition or signature
  changes.
- Candidate terms affected: vehicle jump/dodge, finite boost thrust, respawn
  choice, rocket-car integration, boost-pad resolution, demolition respawn,
  zero-second overtime, enclosed Soccar geometry and match settlement.

## Negative results

- `ACT-268` is not reused because Rocket League has no shot command: a shot is
  emergent car-ball contact.
- `SYS-320` is not reused because its boundary requires persistent vehicle-part
  or occupant damage; Rocket League cars bump or temporarily demolish without a
  damage inventory.
- `CON-399` is not reused because it explicitly models out-of-bounds stoppage;
  the enclosed Soccar arena keeps ordinary wall and corner contact live.
- `OBJ-090` is not reused because it accepts a regulation draw, while the scoped
  Rocket League match requires sudden-death settlement.

## Delta summary

## Нові факти

- [Confirmed | Direct | High] Rocket League v2.72 supports one reproducible
  default five-minute `3v3` Soccar contract whose tied result continues to a
  sudden-death goal (`RL-001`–`RL-010`).

## Нові гени

- [Observation | Corroborated | High] Added thirteen genes for aerial car input,
  boost, demolition respawn, enclosed Soccar physics, zero-second overtime and
  decisive goal settlement.

## Нові комбінації

- [Observation | Corroborated | High] `COMB-0175` isolates boost-routed aerial
  vehicle contact into a decisive team-goal result.

## Зміни таксономії

- [Observation | Corroborated | High] No taxonomy migration; five established
  generic genes and four existing multi-game families are reused unchanged.

## Нові питання

- Which later vehicle sport first reuses finite boost routing and physical ball
  scoring while changing arena enclosure or demolition rules?

## Наступна рекомендована гра

- [Confirmed | Direct | High] `GAME-0178` — Subnautica.
- Optimisation criterion: continue the recorded demand-led Goal in exact order.
- Expected information gain: contrast this finite simultaneous sport with a
  single-player oxygen, depth, crafting and vehicle-construction survival route.
- Backlog impact: seventh of nine authorised game units.

## Чому саме вона

- [Confirmed | Direct | High] It is the next immutable subject in
  `SEARCH_DEMAND_GAME_SELECTION_005` and opens the survival-production corridor.

## Localisation status

- Ukrainian game, new-gene and combination entries are reviewed in this unit.
- The canonical brand title remains `Rocket League`; no invented translated
  brand is appended.

## Open questions

- Re-check current patch and default private-match behaviour before any later
  review-on-touch.
- Direct play could measure exact default dodge and zero-second edge timing
  without changing the present causal boundaries.

## Source notes

- Official pages were checked on 2026-08-28. Patch `v2.72` is newer than the
  Season 23 launch notes and therefore owns the version boundary.
- Tournament structure, ranking and series format are not imported from RLCS;
  only its current reproducible single-game settings are used.

## Next recommended action

- Integrate `GAME-0178` — Subnautica after the required thirty-second stop
  window.
