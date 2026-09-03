---
game_id: GAME-0160
slug: pokemon-legends-z-a
game_title: "Pokémon Legends: Z-A"
analysis_status: reviewed
reviewed: 2026-08-27
combination_ids:
  - COMB-0158
gene_ids:
  action:
    - ACT-008
    - ACT-019
    - ACT-131
    - ACT-164
    - ACT-194
    - ACT-195
    - ACT-196
    - ACT-215
    - ACT-258
    - ACT-259
  system:
    - SYS-004
    - SYS-215
    - SYS-299
    - SYS-307
    - SYS-373
    - SYS-438
    - SYS-439
    - SYS-440
  constraint:
    - CON-210
    - CON-269
    - CON-276
    - CON-277
    - CON-384
    - CON-385
    - CON-386
    - CON-387
  information:
    - INF-073
    - INF-115
    - INF-119
    - INF-122
    - INF-123
    - INF-125
    - INF-170
    - INF-171
  objective:
    - OBJ-088
  time:
    - TIM-003
---

# Game: Pokémon Legends: Z-A

## Analysis scope

- Version / ruleset: Nintendo Switch 2 Edition, update `2.0.2`, base game only,
  reviewed 2026-08-27; one fresh offline single-player save from choosing the
  first partner through the first completed Z-A Royale promotion match and the
  recorded change from Rank Z to Rank Y.
- Primary decision loop: prepare the bounded party by catching and training
  Pokémon in Wild Zone 1, then position the Trainer and one active partner in
  real-time battles, command ready moves or switch partners, earn the required
  nighttime Ticket Points and defeat the designated promotion opponent.
- Entry and exit: enter after character setup when Chikorita, Tepig and
  Totodile are offered as the persistent first partner; exit when Zach's three
  Pokémon are defeated, Rank Y is recorded and Main Mission 04 completes.
- Included: first-partner selection; direct Trainer traversal, crouch and roll;
  real-time Pokémon targeting, move timing, range, area and cooldown; party
  switching, health, defeat and experience levels; ordinary held-item use;
  Wild Zone 1 direct and weakened capture, Boxes and six-member party transfer;
  the five-species research gate, reusable Rock Smash TM and move assignment;
  local Trainer detection and opening advantage; the first nighttime Battle
  Zone, three required Trainer wins, 1,000 Ticket Points, Challenger's Ticket
  and Zach's Rank Y promotion match.
- Excluded: later Rank X-to-A progression, side missions, exhaustive Pokédex or
  Mable research, breeding, shiny hunting and collection optimisation; Mega
  Evolution, Rogue Mega encounters and the base-game finale; multiplayer Z-A
  Battle Club, Link Trade, Mystery Gift and Pokémon HOME; transferred Pokémon;
  all Mega Dimension DLC story, species, systems and rewards.
- Potential scoped modules: the complete base-game Rank Y-to-A and Rogue Mega
  route; the post-game Infinite Z-A Royale; one current Battle Club ruleset;
  Mega Dimension after its own versioned scope review.
- Direct-play status: no fresh Rank Y route was played directly. Nintendo and
  The Pokémon Company's current product, gameplay and update pages establish
  the ruleset; maintained release walkthroughs and mechanic references
  corroborate the exact early-route transitions.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `PLZA-001` | Update 2.0.2 leaves the released base-game route available independently of Mega Dimension | Confirmed | Direct | High | P1, P3 |
| `PLZA-002` | The Trainer and one active Pokémon move in real time while commanded moves differ by range, area, execution and cooldown | Confirmed | Corroborated | High | P2, S1 |
| `PLZA-003` | Wild Pokémon can be targeted and caught directly or after battle lowers HP, with visible capture guidance and a probabilistic result | Confirmed | Corroborated | High | P2, S2, S4 |
| `PLZA-004` | Captures enter owned storage, while a bounded active party can be revised and one eligible partner deployed or switched in battle | Confirmed | Corroborated | High | S2, S3 |
| `PLZA-005` | Battle experience raises persistent Pokémon levels and exposes learned moves that can be assigned to bounded move slots | Confirmed | Corroborated | High | S1, S2 |
| `PLZA-006` | Trainer awareness changes battle initiation: detection can catch the player's partner off guard, while a concealed approach can grant a critical opening | Confirmed | Direct | High | P2, S3 |
| `PLZA-007` | Nighttime Battle Zone victories award the 1,000 points required for the first Challenger's Ticket | Confirmed | Corroborated | High | P2, S3 |
| `PLZA-008` | Defeating Zach with that ticket records the persistent promotion from Rank Z to Rank Y and completes Main Mission 04 | Confirmed | Corroborated | High | S3, S5 |

## Basic data

- Release / origin: Game Freak / The Pokémon Company / Nintendo; released
  16 October 2025, with Nintendo update 2.0.2 dated 19 March 2026.
- Platform or physical form: third-person creature-collection action RPG on
  Nintendo Switch and Nintendo Switch 2; this scope uses Switch 2 offline play.
- Puzzle family: tactical forecast and counterplay; real-time system pressure;
  agent routing and coordination; ordered dependency sequencing.
- Primary sources:
  - **[P1]** [official Nintendo product page](https://www.nintendo.com/us/store/products/pokemon-legends-z-a-switch/),
    for release, platforms, base/DLC separation, real-time commands, switching,
    Wild Zones and the Rank Z-to-A tournament premise.
  - **[P2]** [official gameplay and battling guide](https://legends.pokemon.com/en-gb/gameplay),
    for real-time movement, move reach/timing, capture, Trainer detection,
    daytime preparation, nighttime Battle Zones, Ticket Points and promotion.
  - **[P3]** [official Nintendo update history](https://www.nintendo.com/fr-fr/Assistance/Achats-et-abonnements/Jeux/Comment-mettre-a-jour-Legendes-Pokemon-Z-A-2938482.html),
    for current update 2.0.2 and the explicit base-game/Mega Dimension boundary.
- Secondary and reproducible sources:
  - **[S1]** [Bulbapedia opening walkthrough](https://bulbapedia.bulbagarden.net/wiki/Walkthrough:Pok%C3%A9mon_Legends:_Z-A/Part_1),
    for first-partner selection, commanded move inputs, cooldown and early EXP.
  - **[S2]** [Thonky Main Mission 03 walkthrough](https://www.thonky.com/pokemon-legends-z-a/main-mission-03-a-new-life-in-lumiose-city),
    for Wild Zone 1 capture, party/Boxes, research reward, reusable TM and Rock
    Smash path gate.
  - **[S3]** [Bulbapedia Main Mission 04 walkthrough](https://bulbapedia.bulbagarden.net/wiki/Walkthrough:Pok%C3%A9mon_Legends:_Z-A/Part_4),
    for detection, switching, three Battle Zone victories, 1,000 points and the
    first promotion challenge.
  - **[S4]** [Serebii wild Pokémon mechanics](https://www.serebii.net/legendsz-a/wildpokemon.shtml),
    for spawns, direct throws, enraged lockout, capture guidance and rank/level
    influence on capture.
  - **[S5]** [Thonky Main Mission 04 walkthrough](https://www.thonky.com/pokemon-legends-z-a/main-mission-04-battling-in-the-z-a-royale),
    for the three required Trainer battles, Zach's bounded team and Rank Y exit.
- Claim IDs: `PLZA-001`–`PLZA-008`.

## Mechanical decomposition

### Action Genes

- Existing genes: `ACT-008`, navigate the Trainer; `ACT-019`, choose an active
  Pokémon move and legal target; `ACT-131`, consume or apply one carried
  immediate-effect item; `ACT-164`, select the active carried Ball or item;
  `ACT-194`, throw one capture device at an eligible wild Pokémon; `ACT-195`,
  deploy or recall the selected party partner; `ACT-196`, transfer a captured
  Pokémon between Boxes and the six-member party; `ACT-215`, revise the bounded
  learned-move loadout, including reusable Rock Smash.
- New genes: `ACT-258`, switch the active battle companion from the bounded
  party; `ACT-259`, choose one persistent starting companion from an offered
  roster.
- Parameters: partner species, party slot, learned move, move button, target,
  range, area, cooldown, Ball type, target HP, item and Rock Smash fixture.
- Claim IDs: `PLZA-002`–`PLZA-005`.

### System Behaviour Genes

- Existing genes: `SYS-004`, choose random capture outcomes; `SYS-215`, resolve
  directly commanded real-time combat; `SYS-299`, convert battle/capture EXP
  thresholds into persistent Pokémon levels; `SYS-307`, resolve probabilistic
  capture into owned storage; `SYS-373`, escalate local Trainer perception into
  detection and combat.
- New genes: `SYS-438`, alternate daytime wild preparation with nighttime
  Battle Zone competition; `SYS-439`, accumulate eligible Trainer victories
  into Ticket Points and issue the Challenger's Ticket; `SYS-440`, settle a
  designated promotion battle into the next persistent Z-A Royale rank.
- Resolution order: the selected partner and learned moves establish the active
  battle kit; positioning and target state gate a commanded ready move; damage,
  status and knockout update the party and may force a switch; capture consumes
  a Ball before its random result; EXP updates persistent levels; night exposes
  Battle Zone opponents; three scoped victories reach 1,000 points and issue
  the ticket; Zach's defeat records Rank Y and closes the route.
- Claim IDs: `PLZA-002`–`PLZA-008`.

### Constraint Genes

- Existing genes: `CON-210`, typed carried inventory and stacks; `CON-269`,
  commanded moves require a legal target, reach and readiness; `CON-276`,
  capture requires an eligible target and available Ball; `CON-277`, Boxes and
  the active party have bounded roster capacities.
- New genes: `CON-384`, only one living eligible party companion can be the
  active commanded battler; `CON-385`, relative concealment and awareness gate
  the opening advantage; `CON-386`, Battle Zone competition and Ticket Point
  awards require the eligible night phase; `CON-387`, promotion requires the
  current Challenger's Ticket and victory over its designated opponent.
- Scarce strategic resources: partner health and move readiness; six party
  slots; carried Poké Balls and restorative items; night access, Ticket Points
  and the one current Challenger's Ticket.
- Claim IDs: `PLZA-002`–`PLZA-008`.

### Information Genes

- Existing genes: `INF-073`, carried items and current selection; `INF-115`,
  local sight and sound expose Trainer/Pokémon state; `INF-119`, Pokémon health,
  level, status and readiness; `INF-122`, capture arrows and attempt feedback;
  `INF-123`, owned Pokémon profiles expose level, stats, type and moves;
  `INF-125`, the map and mission list expose authored route gates.
- New genes: `INF-170`, the battle HUD exposes the active partner, target,
  health, four assigned moves and their readiness; `INF-171`, the Z-A Royale
  interface exposes rank, Ticket Point threshold, Challenger's Ticket and
  promotion opponent.
- Claim IDs: `PLZA-002`–`PLZA-008`.

### Objective Genes

- New gene: `OBJ-088`, earn the first Z-A Royale promotion from Rank Z to Rank Y.
- Success, evaluation and failure: Zach's complete party knockout with the
  current Challenger's Ticket records Rank Y and completes Main Mission 04;
  losing a preceding battle does not satisfy the point or promotion gate and
  exhaustive capture or later Rank A is outside this objective.
- Claim IDs: `PLZA-007`, `PLZA-008`.

### Time Genes

- Existing gene: `TIM-003`, movement, detection, attacks, cooldowns and Battle
  Zone pressure advance in real time while the player may issue commands.
- Parameters: move wind-up, cooldown, day/night phase and pause/menu treatment.
- Claim IDs: `PLZA-002`, `PLZA-006`, `PLZA-007`.

## Reproducible transitions

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Three offered partners are unowned | Accept Chikorita, Tepig or Totodile | Exactly the selected Pokémon becomes the persistent first party member and supplies its early move set | starting-companion commitment | `PLZA-002`, `PLZA-005` |
| A wild Pokémon is targetable and a Poké Ball is carried | Aim and release the Ball | The Ball is spent; target state and Ball strength set the chance; success moves the Pokémon into party or Boxes | direct probabilistic capture | `PLZA-003`, `PLZA-004` |
| A difficult wild target remains active after a failed throw | Command attacks until its HP reaches zero, then throw | The target enters a short catch window with improved eligibility before recovery or despawn | combat-to-capture handoff | `PLZA-003` |
| More than six Pokémon are owned | Move one Pokémon through Boxes | The chosen creature enters an available party slot and the displaced member enters reserve storage | bounded persistent roster | `PLZA-004` |
| One partner is active and another living party member is available | Select the replacement during battle | The replacement becomes the sole commanded partner while each member retains its own health, moves and level | live party switching | `PLZA-002`, `PLZA-004` |
| A commanded move is assigned but not ready or its target is out of legal reach | Press its move input | The move remains unresolved until cooldown, target and spatial gates permit execution | positional cooldown combat | `PLZA-002` |
| The first research reward is claimable and Bunnelby is owned | Assign reusable Rock Smash, deploy Bunnelby and target the rock pile | Rock Smash occupies one legal move slot and removes the authored obstruction | capture/research-to-route dependency | `PLZA-004`, `PLZA-005` |
| A Battle Zone Trainer has not detected the player | Crouch behind cover and command the opening attack | Concealed initiation grants the scoped critical opening; being spotted instead can leave the partner off guard | awareness-dependent initiative | `PLZA-006` |
| Rank Z is active and the nighttime Battle Zone is open | Defeat the three required Trainers | Their awards accumulate to 1,000 Ticket Points and issue the current Challenger's Ticket | tournament qualification | `PLZA-007` |
| The Rank Y ticket names Zach | Defeat Slowpoke, Pidgey and Pikachu | The promotion result records Rank Y and completes Main Mission 04 | scoped terminal promotion | `PLZA-008` |

## Strategic and experiential structure

- Local decision: approach or weaken a wild target before spending a Ball;
  reposition the Trainer to keep the active Pokémon's target in reach; rotate
  among ready moves; switch before a poor type matchup or knockout; approach a
  rival unseen for the opening advantage.
- Medium-term planning: catch enough species to unlock research, keep the six
  party slots complementary, assign Rock Smash without deleting a needed move,
  preserve health and supplies across the three point-awarding fights.
- Long-term structure: convert the chosen starter and first Wild Zone captures
  into a trained party, satisfy the research/route gate, earn the Challenger's
  Ticket at night and win the designated promotion battle.
- Common heuristics: crouch or approach from behind; lower HP before a costly
  throw; command a different ready move rather than waiting idle; switch into a
  favourable type and heal before Zach.
- Failure attribution: capture guidance, health, move readiness, target reach,
  party state, Ticket Points and promotion target are visible; capture samples
  and opponent decisions remain bounded uncertainty.
- Player-trust factors: one input maps to one disclosed move slot, failed range
  and cooldown states give immediate feedback, and rank progression is tied to
  a visible ticket rather than hidden grind.
- Claim IDs: `PLZA-002`–`PLZA-008`.

## Replay and variation

- What changes between sessions: starter, early captures, party composition,
  move assignments, capture samples, battle positioning and switch order.
- Randomness or procedural generation: capture checks and ordinary local item
  finds vary; the authored Wild Zone, required point threshold and Zach team do
  not procedurally regenerate.
- Multiple viable strategies: any starter can anchor the route; different Wild
  Zone captures, move coverage and concealed or direct battle openings can
  reach the same Rank Y result.
- Typical replay motive: test another starter and early party, or solve the
  first promotion with different move timing and type coverage.
- Claim IDs: `PLZA-002`–`PLZA-008`.

## Adjacent systems and history

- Direct predecessors: Pokémon Legends: Arceus for world capture; main-series
  Pokémon for persistent parties, type matchups, levels and learned moves.
- Variants: later base-game ranks add longer preparation and Mega Evolution;
  Battle Club replaces authored rivals with networked multi-Trainer scoring;
  Mega Dimension adds a post-game hyperspace route.
- Similar games: Palworld for probabilistic creature capture and bounded party
  storage; real-time action RPGs for positional cooldown combat; rank-ladder
  games for qualification gates.
- Important differences: the Trainer remains mobile while one party Pokémon
  receives explicit real-time move commands, and a day-preparation/night-
  competition cycle converts captures and levels into a ticketed authored rank.
- Claim IDs: `PLZA-001`–`PLZA-008`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-019`, `ACT-131`, `ACT-164`, `ACT-194`–`ACT-196`, `ACT-215`, `ACT-258`, `ACT-259` | species, moves and Balls are parameters |
| System Behaviour | `SYS-004`, `SYS-215`, `SYS-299`, `SYS-307`, `SYS-373`, `SYS-438`–`SYS-440` | levels, point values and Zach's team are parameters |
| Constraint | `CON-210`, `CON-269`, `CON-276`, `CON-277`, `CON-384`–`CON-387` | capacities, cooldowns and night duration are parameters |
| Information | `INF-073`, `INF-115`, `INF-119`, `INF-122`, `INF-123`, `INF-125`, `INF-170`, `INF-171` | HUD layout and exact icons are parameters |
| Objective | `OBJ-088` | later ranks and completion goals are excluded |
| Time | `TIM-003` | live cadence and phase duration are parameters |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `159` (`GAME-0001`–`GAME-0159`).
- Exact genome matches: none.
- Tied near matches: `GAME-0139` — Palworld (`17 / 73 = 0.232877`).
- Supported combination subsets: `COMB-0158`.
- Scan date: 2026-08-27.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0139` — Palworld | `ACT-008`, `ACT-164`, `ACT-194`, `ACT-195`, `ACT-196`, `SYS-004`, `SYS-215`, `SYS-299`, `SYS-307`, `CON-210`, `CON-276`, `CON-277`, `INF-073`, `INF-122`, `INF-123`, `INF-125`, `TIM-003` | Both join live traversal and combat to probabilistic world capture, persistent companion levels, bounded party/storage transfer and visible capture state; Palworld's deployed Pal selects ordinary combat skills autonomously and extends ownership into base labour, while Z-A has one explicitly commanded and switched battler, awareness-sensitive openings and a night-gated points-to-ticket promotion | Near, `0.232877` |

### Preserved research notes

- New genes: `ACT-258`, `ACT-259`, `SYS-438`–`SYS-440`, `CON-384`–`CON-387`,
  `INF-170`, `INF-171`, `OBJ-088`.
- Classification result: `New combination of known and new genes`.
- Evidence and reasoning: existing Palworld boundaries cover throwing a
  capture device, storage/party transfer and probabilistic ownership, while
  existing combat/XP boundaries cover direct live effects and persistent
  levels. New genes are limited to the commanded active-partner switch,
  offered starter commitment and Z-A Royale's time-, ticket- and promotion-
  specific resolution and disclosure.

## Taxonomy impact

- Registry changes: twelve new stable genes and `COMB-0158`; compatible
  evidence added to existing capture, roster, loadout, direct-combat,
  experience, perception and information boundaries; memberships in existing
  families `FAM-009`, `FAM-010`, `FAM-015` and `FAM-017`.
- Taxonomy-change record: none; the reused capture and roster wording is
  generalised only to expose parameters already inside those boundaries, with
  no merge, split, lifecycle or signature migration.
- Candidate terms affected: none.

## Negative results

- No exact full-genome match is expected; the deterministic scan is recorded
  above after regeneration.
- `SYS-308` is not reused: Z-A's active Pokémon executes explicit player move
  commands rather than autonomously choosing ready combat skills.
- `ACT-188` is not reused: the starter persists across the campaign and is not
  a match-only hero commitment.
- Mega Evolution is not flattened into this first-promotion signature because
  it is unavailable before the declared Rank Y exit.
