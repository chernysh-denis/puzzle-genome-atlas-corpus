---
game_id: GAME-0325
slug: the-legend-of-zelda
game_title: The Legend of Zelda
analysis_status: reviewed
reviewed: 2026-09-20
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-161
    - ACT-164
  system:
    - SYS-037
    - SYS-045
    - SYS-063
    - SYS-215
    - SYS-578
    - SYS-605
    - SYS-931
    - SYS-932
  constraint:
    - CON-175
    - CON-402
  information:
    - INF-073
    - INF-179
    - INF-180
    - INF-356
  objective:
    - OBJ-191
  time:
    - TIM-003
---

# Game: The Legend of Zelda

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Link, Level-1
Eagle, Aquamentus, Triforce, map and compass are carrier parameters, not gene
names.

## Analysis scope

- Version / ruleset: original North American English Nintendo Entertainment
  System cartridge `NES-ZL-USA`, fresh Quest 1. The packet begins before the
  wooden sword is collected, follows the ordinary overworld route to Level-1
  Eagle and ends after the first Triforce fragment is credited. Second Quest,
  later dungeons, ports, remakes and emulator conveniences are excluded.
- Structured analysis target: licensed North American NES cartridge
  `NES-ZL-USA`; see `GAME-0325` in
  [`knowledge/platforms/games.json`](../../platforms/games.json).
- Primary decision loop: move Link through one visible overworld or dungeon
  room; align the sword or selected B item with a reachable enemy; read hostile
  movement, projectiles, drops and doors; collect hearts, rupees and keys;
  spend keys on locked doors, clear rooms whose shutters depend on enemies,
  acquire the dungeon map and compass, navigate to Aquamentus, defeat it and
  claim the first Triforce fragment.
- Entry: first ordinary control of Link in the opening overworld screen of a
  fresh Quest 1 file, before entering the starting cave and taking the wooden
  sword.
- Positive terminal: Aquamentus has been defeated, the heart container may be
  taken, the first Triforce fragment is collected and the fragment-credit
  transition settles with the next overworld state eligible to continue.
- Negative terminal: Link's last half-heart is lost and the Game Over menu is
  shown. Continue, Save and Retry choices and their retained-state differences
  are outside this packet.
- Included: direct four-direction overworld and room movement; the wooden
  sword; one selected B item, with the boomerang used as the reproducible
  instance; ordinary enemies, projectiles and contact damage; passive frontal
  shield cancellation for eligible projectiles; hearts, rupees, keys and
  compatible drops; persistent health across rooms; locked doors; finite
  hostile-clearance shutters; map and compass acquisition; visible dungeon
  room graph and Triforce marker; Level-1 route, Aquamentus and the first
  fragment terminal.
- Excluded: overworld shops, bombs and bombable walls, bow and arrows, candle,
  bait, letter, potions, magical sword, recorder, raft, ladder, power bracelet,
  every later dungeon, Princess Zelda, Ganon, full-game completion, Second
  Quest, Continue/Save/Retry outcomes, deaths deliberately used for routing,
  glitches, speedrun techniques, random-drop farming, exact damage
  optimisation, Famicom Disk System behaviour, rereleases, Virtual Console,
  Switch Online, remakes, randomisers and fan modifications.
- Reproducible parameterisation: create a fresh Quest 1 file on the English
  `NES-ZL-USA` ruleset, enter the opening cave and take the wooden sword, then
  travel to Level-1 Eagle. Inside, collect and inspect the map and compass,
  carry and consume the ordinary keys needed by the chosen legal route, clear
  every room whose shutters block that route and use the obtained boomerang at
  least once. Face one compatible projectile with the ordinary shield between
  attacks so its passive cancellation is visible. Defeat Aquamentus, collect
  the first Triforce fragment and stop after the credit transition. Exact
  rupee total, ordinary drops, damage taken, heart refill, room order where
  alternatives exist and optional heart-container pickup may vary.
- Potential scoped modules: each later Quest 1 dungeon, overworld economy,
  bombable secrets, death-menu persistence, Ganon and Zelda, Second Quest and
  every later release require separate boundaries and evidence.
- Direct-play status: not conducted. No cartridge, console, licensed installed
  wrapper, controller trace, save state, screenshot, video or audio was found
  or opened. Nintendo's preserved manual establishes the controls, shield,
  inventory, health, keys, map and compass; two written routes corroborate the
  bounded first dungeon, Aquamentus and fragment terminal. This is a
  source-bounded reconstruction, not a claimed playthrough or reload test.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `LOZ-001` | The subject is the licensed North American NES cartridge `NES-ZL-USA` and fresh Quest 1 | Confirmed | Corroborated | High | P1, P2, P3 |
| `LOZ-002` | The opening cave supplies the wooden sword before the route to the first dungeon | Observation | Corroborated | High | P1, S1 |
| `LOZ-003` | Link moves in four directions, uses the sword on A and the selected inventory item on B | Confirmed | Direct | High | P1, P2 |
| `LOZ-004` | The ordinary shield passively blocks eligible projectiles when Link faces them and is not attacking | Confirmed | Direct | High | P1, P2 |
| `LOZ-005` | Hearts, rupees, keys and compatible enemy drops are visible finite state; keys open locked dungeon doors | Confirmed | Direct | High | P1, P2 |
| `LOZ-006` | Level-1 Eagle contains enemy-clearance shutters, map and compass pickups and an explored room graph | Observation | Corroborated | High | P1, S1, S2 |
| `LOZ-007` | The map adds dungeon layout while the compass identifies the Triforce location | Confirmed | Direct | High | P1, P2 |
| `LOZ-008` | Aquamentus is the mandatory first-dungeon guardian; its defeat exposes the heart container and first Triforce fragment | Observation | Corroborated | High | S1, S2, S3 |
| `LOZ-009` | Collecting the first Triforce fragment settles Level-1 and returns progression to the overworld | Observation | Corroborated | High | S1, S2 |
| `LOZ-010` | Zero remaining health opens Game Over; Continue, Save and Retry persistence are outside this packet | Confirmed | Direct | High | P1, P2 |
| `LOZ-011` | No executable, direct play, save/reload comparison or audiovisual evidence was used | Confirmed | Direct | High | R1 |

## Basic data

- Release / origin: Nintendo developed and published the North American
  licensed NES cartridge in 1987.
- Platform or physical form: English North American Nintendo Entertainment
  System cartridge `NES-ZL-USA`, fresh Quest 1, original rules.
- Puzzle family: tactical forecast and counterplay; inventory and fixture
  dependencies; real-time system pressure; ordered dependency sequencing.
- Primary and original sources, accessed 2026-09-20:
  - **[P1]** [Nintendo's preserved English NES instruction
    manual](https://www.nintendo.co.jp/clv/manuals/en/pdf/CLV-P-NAANE.pdf), for
    the original controls, sword, shield, inventory, health, rupees, keys, map,
    compass, dungeon doors, Triforce and Game Over surface.
  - **[P2]** [scan of the original `NES-ZL-USA-1`
    manual](https://old.rgm.games/wp-content/uploads/2023/06/Legend-of-Zelda-The-Manual-Clearscan_compressed.pdf),
    used to cross-check the same cartridge instructions and catalogue code.
  - **[P3]** [NES Directory cartridge
    record](https://nesdir.github.io/3FE272FB_USA.html), for licensed identity,
    region, catalogue `NES-ZL-USA`, publisher and developer. No ROM was
    downloaded or executed.
- Corroborating textual sources, accessed 2026-09-20:
  - **[S1]** [Zelda Dungeon Level 1: The Eagle written
    route](https://www.zeldadungeon.net/the-legend-of-zelda-walkthrough/level-1-the-eagle/),
    for the room sequence, key and shutter gates, map, compass, boomerang,
    Aquamentus, heart container and first fragment.
  - **[S2]** [Zelda Dungeon Level 1 reference](https://zeldadungeon.net/wiki/Level_1%3A_The_Eagle),
    for the dungeon identity, room graph, items, boss and Triforce reward.
  - **[S3]** [GameFAQs Level 1: Eagle written
    guide](https://gamefaqs.gamespot.com/nes/563433-the-legend-of-zelda/faqs/75987/level-1-eagle),
    for independent corroboration of Aquamentus and the terminal pickup.
- Research record: **[R1]** local preflight on 2026-09-20 found no cartridge,
  console, authorised emulator session, input trace or save. No audiovisual
  evidence was used.
- Claim IDs: `LOZ-001`–`LOZ-011`.

## Mechanical decomposition

### Action Genes

- Existing `ACT-008`: move Link directly through traversable overworld and
  dungeon room geometry.
- Existing `ACT-161`: align the sword or selected boomerang with a reachable
  hostile and commit the attack.
- Existing `ACT-164`: choose an owned inventory item for the B-button slot
  before using it in the current room.
- Button names, item identities, attack reach and Link's facing are parameters.
  Claims: `LOZ-002`, `LOZ-003`, `LOZ-008`.

### System Behaviour Genes

- Existing `SYS-037`: contacting a visible heart, rupee or compatible drop
  removes it and credits its health or inventory value without ending play.
- Existing `SYS-045`: dungeon enemies move and attack on the live clock without
  one player command for every step. Existing `SYS-215`: Link, enemies,
  attacks, projectiles, damage and defeat resolve in real time.
- Existing `SYS-063`: collecting a key adds carried key state and entering a
  compatible locked door consumes one key while opening that barrier.
- Existing `SYS-578`: hostile contact and attacks reduce one continuous health
  pool, compatible hearts restore missing capacity and zero health ends the
  packet. Existing `CON-175` owns the cross-room survival requirement.
- Existing `SYS-605`: keys, clearance shutters, item rooms and the mandatory
  boss form an ordered authored dungeon route whose settled flags admit the
  next segment.
- New `SYS-931`: collecting the dungeon map and compass changes the retained
  navigation disclosure: the map supplies the Level-1 layout and the compass
  marks the Triforce destination.
- New `SYS-932`: while Link faces an eligible incoming projectile and is not in
  an incompatible attack state, the ordinary shield cancels the projectile on
  contact without a separate defend input or health loss.
- Resolution order: room state advances live; accepted attacks update enemies;
  drops alter health or inventory; keys and clearance settle doors; map and
  compass update navigation disclosure; the shield resolves before compatible
  projectile damage; Aquamentus defeat exposes the terminal rewards. Claims:
  `LOZ-004`–`LOZ-010`.

### Constraint Genes

- Existing `CON-175`: health lost in one room remains lost in later rooms
  unless restored, and zero health terminates the scoped run.
- Existing `CON-402`: a declared shuttered combat-room exit remains closed
  until its finite required hostile set is defeated.
- Shield eligibility, key count, room-clear set, item reach and exact health or
  damage values are parameters rather than new constraints.

### Information Genes

- Existing `INF-073`: the HUD and inventory expose the selected B item and
  finite carried counts before a local action.
- Existing `INF-179`: the current room exposes Link, visible enemies,
  projectiles, pickups, obstacles and door states needed for the next move.
- Existing `INF-180`: the dungeon display retains explored room cells and
  connections rather than revealing all future room contents.
- New `INF-356`: the dungeon navigation display distinguishes Link's current
  room, the acquired map outline and the compass-marked Triforce destination,
  alongside visible health, rupees, keys and selected items.
- Hidden room contents, exact future drops and unobserved enemy actions remain
  concealed. Claims: `LOZ-003`–`LOZ-008`.

### Objective Genes

- New `OBJ-191`: traverse Level-1 Eagle's required key- and clearance-gated
  route, defeat Aquamentus and claim the first Triforce fragment so the
  dungeon settles and overworld progression resumes. The heart container,
  map, compass and boomerang are route or reproducibility choices, not separate
  campaign terminals. Claims: `LOZ-006`, `LOZ-008`, `LOZ-009`.

### Time Genes

- Existing `TIM-003`: enemies, projectiles and contact continue in real time
  while Link moves, attacks or chooses a new position. The inventory pause is
  a planning interruption and does not make dungeon combat turn-based.

## Reproducible transitions

| Before | Action | Deterministic or bounded resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| A fresh Quest 1 opens outside the starting cave | Enter the cave and contact the wooden sword | the sword becomes Link's A-button weapon | bounded packet includes the initial weapon handoff | `LOZ-002`, `LOZ-003` |
| One ordinary dungeon room is active | Move and strike while enemies advance | positions, attacks, contact and damage resolve on the live clock | direct room-scale action and combat | `LOZ-003`, `LOZ-006` |
| An eligible projectile approaches Link's front while he is not attacking | Keep facing the projectile | the ordinary shield cancels it before health loss | passive directional defence is not a defend command | `LOZ-004` |
| A loose key is reachable | Contact the key, then enter a compatible locked door | carried key count rises, then one key is consumed and the door opens | finite inventory state gates the route | `LOZ-005`, `LOZ-006` |
| A shuttered room still contains a required enemy | Defeat the remaining finite hostile set | the declared shutters open and the clear state persists | room clearance owns specific exits | `LOZ-006` |
| The Level-1 map is unowned | Contact the map pickup | the dungeon display gains the authored room outline | map acquisition changes retained disclosure | `LOZ-007` |
| The Level-1 compass is unowned | Contact the compass pickup | the dungeon display marks the Triforce destination | compass state narrows the terminal search | `LOZ-007` |
| The boomerang is owned but not selected | Choose it in the inventory and press B in range | the selected item becomes active and travels through its legal attack path | B-item selection precedes item use | `LOZ-003` |
| Link has missing health and reaches a compatible heart | Contact the heart | current health increases up to its allowed capacity | healing alters one continuous cross-room pool | `LOZ-005`, `LOZ-010` |
| Aquamentus is active | Evade fireballs and attack from legal reach | repeated accepted hits reduce the mandatory guardian toward defeat | first dungeon has a required live boss | `LOZ-008` |
| Aquamentus is defeated | Contact the exposed first Triforce fragment | the fragment is credited, Level-1 settles and overworld progression resumes | exact positive terminal is retained progression credit | `LOZ-008`, `LOZ-009` |

## Edge-case audit

- The shield is passive and facing-sensitive. It is not the temporary Block
  pool of `SYS-165`, an aimed parry, armour reduction or a separate defend
  action.
- Keys are carried consumables whose compatible door contact spends one key;
  the Triforce fragment is progression credit and does not belong to the same
  barrier-consumption rule.
- Enemy-clearance shutters use `CON-402`; permanently locked key doors remain
  `SYS-063`, and ordinary already-open room exits are neither.
- The map and compass alter information. They do not teleport Link, open every
  door or reveal hidden enemy/drop outcomes.
- The heart container is optional in this packet because the objective settles
  on the first Triforce fragment. If collected, its capacity increase is a
  parameter of health state rather than a second terminal.
- Continue, Save and Retry are visible after death but excluded, so no claim is
  made about exact retained rupees, keys, map, compass or fragment state after
  choosing one.

## Strategic and experiential structure

- Local decision: face or dodge a projectile, commit a sword/boomerang attack,
  take a drop, preserve health or move toward one open door.
- Medium horizon: spend keys on the chosen Level-1 route, clear shuttered rooms
  and use the map/compass disclosures to avoid unnecessary backtracking.
- Long horizon: reach Aquamentus with enough health and the required route
  state, then convert boss victory into the first retained fragment.
- Feedback: sprites, projectile motion, shield cancellation, heart meter,
  item/currency counts, door state, room map and compass mark distinguish
  combat, inventory, navigation and terminal errors.
- Skill expression: facing, spacing, attack timing, projectile reading, key
  economy and room-route memory operate together under continuous pressure.

## Replay and variation

- Level-1 geometry, item locations, locked doors and Aquamentus are authored;
  no procedural dungeon generation is claimed.
- Enemy movement and compatible drops vary within the original rules. Damage,
  rupee count, key route, healing and optional pickups can differ without
  changing the terminal.
- Second Quest changes dungeon layouts and dependencies and remains a separate
  module rather than evidence for this Quest 1 signature.

## Adjacent systems and history

- *The Binding of Isaac: Rebirth* shares room-scale live combat, visible
  projectiles, pickups, explored-room mapping and clearance-gated doors. Its
  floors are seed-generated and use layered hearts, bombs and run items; this
  packet uses one authored first dungeon, carried keys, a map/compass pair,
  passive shield cancellation and a fixed Triforce terminal.
- *TUNIC* shares direct action, item state and authored dungeon routing but
  centres knowledge-gated manual interpretation and later action-language
  discovery. This packet uses explicit NES manual rules and a first-dungeon
  item/key sequence without claiming hidden-language inference.
- *Hollow Knight* shares one continuous health pool, live combat and authored
  navigation. It restores health through a held Focus action and has different
  death recovery; Zelda uses contact hearts, carried keys, room shutters and a
  fragment-credit dungeon terminal.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-161`, `ACT-164` | Link, pad mapping, sword and B-item identity are parameters |
| System Behaviour | `SYS-037`, `SYS-045`, `SYS-063`, `SYS-215`, `SYS-578`, `SYS-605`, `SYS-931`, `SYS-932` | enemy roster, drops, health values, keys and shield eligibility are parameters |
| Constraint | `CON-175`, `CON-402` | health threshold, shutter set and key availability are parameters |
| Information | `INF-073`, `INF-179`, `INF-180`, `INF-356` | HUD layout, map cells, compass marker and concealed contents are parameters |
| Objective | `OBJ-191` | Level-1, Aquamentus and first fragment are parameters |
| Time | `TIM-003` | update cadence and inventory pause are parameters |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `324` (`GAME-0001`–`GAME-0324`).
- Exact genome matches: none.
- Tied near matches: `GAME-0272` — Serious Sam 4 (`8 / 27 = 0.296296`).
- Supported combination subsets: none.
- Scan date: 2026-09-20.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0272` — Serious Sam 4 | `ACT-008`, `ACT-161`, `ACT-164`, `SYS-215`, `SYS-578`, `CON-402`, `INF-073`, `TIM-003` | Both packets directly move and attack in live combat, expose selected equipment and preserve one health pool through finite clearance gates. Serious Sam 4 is a forward firearm route with magazine/reserve legality, triggered waves and an exit threshold. Zelda instead adds contact rewards, carried-key doors, an authored room graph, map/compass disclosure, passive facing-shield cancellation and a required Triforce-fragment pickup after its guardian. | Near, `8 / 27 = 0.296296` |

### Preserved research notes

- New genes: `SYS-931`, `SYS-932`, `INF-356` and `OBJ-191`.
- Classification result: `New gene`; no verified combination is expected.
- Evidence and reasoning: no lower-ID boundary owns the permanent map/compass
  disclosure transform, input-free facing shield, joined first-dungeon
  navigation display or first-Triforce-fragment terminal.

## Taxonomy impact

- Four Active boundaries are added for map/compass disclosure conversion,
  passive shield cancellation, the dungeon navigation display and the
  first-fragment terminal.
- Fifteen existing boundaries are reused without wording, lifecycle or earlier
  signature changes. No combination definition changes.

## Negative results

- No cartridge, console, executable, direct play, save/reload comparison,
  screenshot, video or audio evidence exists for this unit.
- No random-drop probability, exact enemy health, attack damage, room-frame
  timing or hidden behaviour is promoted from guide language into a gene.
- Bombs, bombable walls, bow/arrows and shops are excluded rather than inferred
  from general franchise knowledge or optional Level-1 possibilities.
- The ordinary shield's projectile cancellation is kept distinct from timed
  parry, armour, consumable defence and temporary Block.
- Second Quest and later dungeons are not averaged into the first Quest 1
  dungeon packet.

## Delta summary

## New facts

- [Confirmed | Direct | High] Nintendo's manual establishes the original
  controls, passive shield, health and inventory, keys, map and compass
  (`LOZ-001`–`LOZ-007`, `LOZ-010`).
- [Observation | Corroborated | High] Independent written routes establish
  Level-1's required room sequence, Aquamentus and first-fragment terminal
  (`LOZ-006`, `LOZ-008`, `LOZ-009`).

## New genes

- [Confirmed | Direct | High] `SYS-931`, `SYS-932` and `INF-356` isolate the
  map/compass disclosure transform, passive facing shield and dungeon display.
- [Observation | Corroborated | High] `OBJ-191` isolates the complete first-
  dungeon guardian-and-fragment terminal.

## New combinations

- [Observation | Corroborated | High] No new verified combination.

## Taxonomy changes

- [Confirmed | Direct | High] No earlier taxonomy boundary, signature or
  lifecycle state changes; fifteen existing genes are reused as written.

## New questions

- Which exact room, enemy and drop state survives each Continue, Save or Retry
  choice on an original cartridge?
- Which random-drop distributions and room-reset rules differ across cartridge
  revisions without altering the bounded first-fragment terminal?

## Next recommended game

- [Hypothesis | Limited | High] `GAME-0326` Crash Bandicoot, original North
  American PlayStation release, is the next reserved audience-recognition unit.
- Optimisation criterion: test a fixed forward 3D route, crate accounting and
  life/checkpoint structure against this top-down item-gated dungeon packet.
- Backlog impact: this unit completes 1/9 of the current horizon.

## Why this game

- [Hypothesis | Limited | High] The original Legend of Zelda is a culturally
  central NES title whose authored room graph, carried keys, map/compass pair,
  passive shield and first-fragment terminal expose mechanics not represented
  by genre labels alone.

## Research checklist

- [x] exact original cartridge, Quest, entry, terminal and exclusions declared
- [x] original manual and independent written route evidence separated
- [x] keys, clearance shutters, map/compass and passive shield separated
- [x] direct-play, executable, reload and audiovisual limits disclosed
- [x] complete six-type gene scan performed
- [x] deterministic lower-ID comparison output integrated
- [x] reviewed Ukrainian localisation and bilingual presentation completed
- [x] original artwork and responsive browser checks completed
