---
game_id: GAME-0347
slug: castlevania-symphony-of-the-night
game_title: "Castlevania: Symphony of the Night"
analysis_status: reviewed
reviewed: 2026-09-21
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-161
    - ACT-199
    - ACT-341
    - ACT-437
  system:
    - SYS-215
    - SYS-299
    - SYS-369
    - SYS-398
    - SYS-412
    - SYS-417
    - SYS-972
    - SYS-973
  constraint:
    - CON-269
    - CON-621
  information:
    - INF-119
    - INF-125
    - INF-179
  objective:
    - OBJ-080
  time: []
---

# Game: Castlevania: Symphony of the Night

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Alucard, Richter,
Dracula, Death, Cube of Zoe, Entrance, Alchemy Laboratory, Slogra, Gaibon,
Life Max Up, Marble Gallery, PlayStation and `SLUS-00067` are carrier
parameters, not gene names.

## Analysis scope

- Version / ruleset: the original North American English PlayStation
  black-label disc published by Konami in 1997, product ID `SLUS-00067`. It is
  not the Japanese or European build, Greatest Hits revision, Sega Saturn
  version, downloadable wrapper, later port, randomiser, translation patch,
  cheat, emulator enhancement or alternate-character mode.
- Structured analysis target: the original English booklet's Alucard controls,
  HUD, map, equipment, relic, special-weapon, level, room and save rules joined
  to the written original-PlayStation route through the Entrance and Alchemy
  Laboratory; see `GAME-0347` in
  [`knowledge/platforms/games.json`](../../platforms/games.json).
- Scenario: one fresh ordinary Alucard opening, after the required Richter
  prologue, from first ordinary Alucard control outside Dracula's castle through
  the first mandatory boss pair and the opened passage into Marble Gallery.
- Entry: the Richter fight and intervening presentation are over; Alucard first
  accepts directional input at the castle approach. The fresh file has no
  imported map, save, inventory, level or alternate-name modifier.
- Fixed reproducible route: enter the castle; proceed until Death removes the
  starting equipment; continue through the Entrance; collect and leave enabled
  the Cube of Zoe; use the first save room; enter the Alchemy Laboratory; take
  the direct authored route and reachable equipment; use the laboratory save
  room; collect the Axe special weapon; defeat Slogra and Gaibon; collect their
  Life Max Up; cross the right-hand threshold into Marble Gallery.
- Primary decision loop: read the current room and retained map, move or jump
  toward one reachable exit, item, save fixture or hostile, choose equipment
  whose attack/defence suits the route, then attack, guard or spend hearts on
  the current special weapon while real-time enemy movement continues.
- Positive terminal: Slogra and Gaibon are defeated, their Life Max Up has
  raised and restored Alucard's health capacity, and ordinary control first
  resumes across the boss-opened threshold in Marble Gallery. No action there
  is admitted.
- Failure and recovery: zero HP returns to the Start screen. Continue loads the
  most recently written save-room state, so post-save route position, transient
  enemy state and progress are not kept; the fixed route may then be retried.
- Included: two-dimensional movement, crouch, jump and back dash; direct hand
  and special-weapon attacks; held shield guard when equipped; one special
  weapon and its heart cost; pickup and equipment transfer; hand, armour and
  accessory statistics; HP, MP, hearts, level, EXP and attributes; real-time
  damage; experience levelling if reached; Death's equipment removal; Cube of
  Zoe and candle-item capability; explored-room map; save-room HP/MP restoration
  and memory-card save; death/Continue; Slogra/Gaibon; Life Max Up; and the
  Marble Gallery threshold.
- Reproducible parameterisation: use a new empty file with an ordinary name,
  default controls and the required Richter prologue; do not import a save or
  use a luck-code name or sequence break. Incidental drops, remaining resources,
  level, equipment and boss attack order may vary. Death's removal, Cube,
  save-room function, boss pair, Life Max Up and next threshold do not.
- Excluded: optional prologue bonuses as an optimisation target; Death skip;
  Entrance return Easter egg; hidden rooms and out-of-route loot; spells,
  familiars, shops, warp rooms, transformations, blue doors, Jewel of Open,
  later relics, bosses, endings, inverted castle, trophies, farming,
  speedrunning and audiovisual analysis.
- Direct-play status: not conducted. No disc, console, memory card, emulator,
  ROM, save, controller trace, screenshot, video or audio was used. This is a
  source-bounded reconstruction, not a claimed playthrough.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `CS-001` | The packet targets the North American English PlayStation `SLUS-00067` ruleset | Confirmed | Corroborated | High | P1, P2, S1 |
| `CS-002` | Alucard has direct movement, jumping, back dash, separate hand inputs, status and map screens | Confirmed | Direct | High | P1 |
| `CS-003` | HUD/status expose HP, MP, hearts, equipment statistics, level, EXP, attributes and status | Confirmed | Direct | High | P1 |
| `CS-004` | Compatible equipment changes attack/defence; Death removes the initial equipped set | Observation | Corroborated | High | P1, S2 |
| `CS-005` | The enabled Cube of Zoe lets destroyed candles expose items | Confirmed | Direct | High | P1 |
| `CS-006` | The map retains visited rooms and current location without ordinary undiscovered rooms | Confirmed | Direct | High | P1 |
| `CS-007` | Save rooms restore resources and save; death plus Continue resumes the last save | Confirmed | Direct | High | P1 |
| `CS-008` | Entrance and Alchemy Laboratory lead to first bosses Slogra and Gaibon | Observation | Corroborated | High | S2, S3, S4 |
| `CS-009` | Their defeat exposes a Life Max Up and continuing passage into Marble Gallery | Observation | Corroborated | High | S2, S3 |
| `CS-010` | The signature admits only capabilities available before first Marble Gallery control | Observation | Corroborated | High | P1–P2, S1–S4, V1 |

## Basic data

- Release / origin: Konami; original North American English PlayStation
  release, 1997.
- Platform or physical form: licensed North American PlayStation CD-ROM,
  `SLUS-00067`, with memory-card saving.
- Puzzle family: tactical forecast and counterplay; inventory and fixture
  dependencies; exploration-gated capability progression.
- Primary sources, accessed 2026-09-21:
  - **[P1]** [Konami's original English PlayStation instruction booklet
    scan](https://archive.org/details/castlevania-symphony-of-the-night_202203),
    especially pp. 5–6 and 12–24, for input, files, HUD, map, status,
    equipment, relics, Cube of Zoe, hearts, rooms and saving.
  - **[P2]** [Konami's official series history
    entry](https://www.konami.com/games/castlevania/us/en-us/page/history_1997_ps),
    identifying the 1997 PlayStation product and Alucard premise.
- Corroborating sources:
  - **[S1]** [Redump's verified-disc
    catalogue](https://redump.info/discs?dumper=Read+Only), for the North
    American English original serial `SLUS-00067`.
  - **[S2]** [Versus Books' 1997 written PlayStation route preserved by the
    Internet Archive](https://archive.org/details/castlevania-symphony-of-the-night-official-guide-1997),
    for Death, Cube/save sequence, laboratory, boss pair and Life Max Up.
  - **[S3]** [GameFAQs original-PlayStation walkthrough by
    Wingchild](https://gamefaqs.gamespot.com/ps/196885-castlevania-symphony-of-the-night/faqs/3787),
    for the boss pair, reward and next passage.
  - **[S4]** [Gamer Corner's critical-path written
    route](https://guides.gamercorner.net/sotn/walkthrough/), for the Entrance,
    Cube, laboratory and first-boss order.
- Validation source: **[V1]** repository-side executable transition
  reconstruction derived from P1–P2 and S1–S4; it does not execute or inspect
  the commercial program.
- Claim IDs: `CS-001`–`CS-010`.

## Mechanical decomposition

### Action Genes

- `ACT-008`: move, crouch, jump and back-dash Alucard through visible rooms.
- `ACT-161`: commit the equipped hand or special weapon against enemies,
  breakable candles and the boss pair.
- `ACT-199`: collect and assign route items to compatible hand, armour or
  accessory positions, optionally replacing an equipped item.
- `ACT-341`: collect the Cube, activate save fixtures and accept legal exits.
- `ACT-437`: hold and release an equipped facing-relative shield guard.

### System Behaviour Genes

- `SYS-215`: resolve direct attacks, guards, hostile motion, damage and defeat.
- `SYS-299`: convert eligible experience thresholds into levels and statistics.
- `SYS-369`: lethal failure plus Continue restores the last save-room state.
- `SYS-398`: the unique Cube retains a named candle-item capability while on.
- `SYS-412`: equipment and attributes determine attack, defence and hand use.
- `SYS-417`: Life Max Up permanently raises maximum health and restores it.
- New `SYS-972`: Death's authored event removes the equipped starting set while
  Alucard, control and the equipment model continue.
- New `SYS-973`: an eligible save-room fixture restores current HP and MP.

### Constraint Genes

- `CON-269`: the special weapon needs its input, sufficient hearts and a legal
  target; only one special weapon may be carried at once.
- `CON-621`: a save write needs the designated transformed save-room cube and
  an eligible memory-card block.

### Information Genes

- `INF-119`: HUD/status expose personal resources, level, attributes,
  equipment and resulting attack/defence.
- `INF-125`: the map exposes visited geometry, current position and disclosed
  save markers without ordinary hidden contents.
- `INF-179`: each room exposes actors, threats, pickups, candles and exits.

### Objective Genes

- `OBJ-080`: satisfy the equipment-reset route, defeat Slogra/Gaibon, collect
  the retained capacity reward and cross into Marble Gallery.

### Time Genes

- No separate Time gene: simultaneous hostile action and hit cadence are
  parameters of `SYS-215`, not an independent resource or objective.

## Reproducible transitions

| Before | Action | Resolution | Establishes | Claim |
|---|---|---|---|---|
| Fresh Alucard control | enter and follow Entrance | Death removes the equipped starting set; control continues | equipment reset | `CS-004` |
| Cube is reachable | collect it and leave it enabled | candle destruction can expose items | retained capability | `CS-005` |
| Save cube is overhead | stand beneath it and press up | HP/MP refill; transformed fixture can write the current state | restorative save | `CS-007` |
| Route item is carried | select compatible area and item | equipment and attack/defence update | loadout choice | `CS-003`, `CS-004` |
| Axe is current and hearts remain | use it against a reachable boss | heart cost is spent and live damage resolves | finite special attack | `CS-003`, `CS-008` |
| Boss pair is active | move, attack and optionally guard | damage resolves until both reach defeat | guardian clearance | `CS-008` |
| Boss pair is defeated | collect Life Max Up | maximum and current health rise | retained reward | `CS-009` |
| Right passage is open | cross the threshold | Marble Gallery control resumes; packet stops | positive terminal | `CS-009` |
| Alucard reaches zero after saving | choose Continue | last save-room state returns; later transient state is discarded | retry | `CS-007` |

## Evidence limits

- The booklet establishes rules, not room order; written PlayStation guides
  provide the route and reward placement. Tactical advice is not mandatory.
- Exact drops, damage rolls, enemy HP and collision frames are not inferred
  from executable data, video or a ROM. `SLUS-00067` identifies the selected
  release; later wrappers and revisions remain excluded.

## Strategic and experiential structure

- Local decisions alternate room traversal, equipment comparison, special-
  weapon economy, facing-relative defence and real-time attack timing.
- Medium-term planning rebuilds a workable loadout after Death, retains enough
  hearts for the Axe and uses save rooms before committing to the boss pair.
- Long-term structure turns an imposed equipment reset into exploration-led
  recovery, adds one persistent candle interaction, then tests the rebuilt
  character in a mandatory two-target encounter.
- Failure attribution remains legible through HP/MP/hearts, equipment values,
  current room, explored map, boss state and the latest save-room write.

## Replay and variation

- Equipment finds, incidental drops, level, remaining resources and exact
  attack order may differ while the authored route and terminal remain fixed.
- The route admits different weapons, shield use and boss focus order; the Axe
  is fixed only for this reproducible reconstruction.
- The packet has no procedural room generation. Enemy motion and combat values
  create bounded attempt variation without changing room topology.

## Adjacent systems and history

- Super Metroid also joins explored-room mapping, direct platform movement,
  live combat and a retained early capability, but its scoped route does not
  remove a starting loadout or join restoration to manual save rooms.
- Hollow Knight shares authored-room exploration, held resources, live combat
  and checkpoint recovery; its Bench resets ordinary enemies and does not
  expose a body-slot equipment rebuild after confiscation.
- Later Symphony of the Night releases are excluded because executable,
  interface, text and feature parity were not established for this packet.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-161`, `ACT-199`, `ACT-341`, `ACT-437` | named items, inputs and rooms are parameters |
| System Behaviour | `SYS-215`, `SYS-299`, `SYS-369`, `SYS-398`, `SYS-412`, `SYS-417`, `SYS-972`, `SYS-973` | damage, values, Death, Cube and reward amount are parameters |
| Constraint | `CON-269`, `CON-621` | heart cost, target and memory-card block are parameters |
| Information | `INF-119`, `INF-125`, `INF-179` | literal HUD, map colours and room art are presentation |
| Objective | `OBJ-080` | guardians, reward and next region are parameters |
| Time | none | real-time cadence belongs to `SYS-215` |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `346` (`GAME-0001`–`GAME-0346`).
- Exact genome matches: none.
- Tied near matches: `GAME-0230` — STAR WARS Battlefront II (2017) (`9 / 34 = 0.264706`).
- Supported combination subsets: none.
- Scan date: 2026-09-21.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0230` — STAR WARS Battlefront II (2017) | `ACT-008`, `ACT-161`, `ACT-199`, `ACT-341`, `SYS-215`, `SYS-369`, `CON-269`, `INF-119`, `INF-125` | Both packets traverse authored spaces, collect/equip items, fight in real time, use constrained abilities, read personal/map state and retry from saved progress. Battlefront II centres firearm heat, temporary ability readiness and a mission evacuation. Symphony of the Night instead starts with confiscation, rebuilds body-slot equipment, retains a candle interaction, restores at manual save rooms and ends by taking a permanent health-capacity reward across a first-boss threshold. | Near, `9 / 34 = 0.264706` |

### Preserved research notes

- New genes: `SYS-972` and `SYS-973`.
- Classification result: `New genes`.

## Taxonomy impact

- Registry changes: append two Active System boundaries and add carrier
  evidence for reused exploration, equipment, persistence and combat genes.
- Taxonomy-change record:
  [`TAXONOMY_CHANGE_089`](../../../research/taxonomy-changes/TAXONOMY_CHANGE_089.md).
- Names, items, rooms, bosses, values, platform and serial remain parameters.

## Negative results

- No direct play, executable inspection, ROM, disc hash, memory-card test,
  frame capture, controller trace, screenshot, video or audio evidence.
- No verified combination, exact lower-ID genome match or later-port parity.
- No separate genes for each item slot, candle, named enemy, room, map colour,
  resource number, reward value or tactical recommendation.

## Delta summary

## New facts

- [Observation | Corroborated | High] Death removes the equipped starting set
  while the living character and equipment framework continue (`CS-004`).
- [Confirmed | Direct | High] Save rooms restore HP/MP and permit a retained
  write from which Continue can resume (`CS-007`).

## New genes

- [Observation/Confirmed | Direct/Corroborated | High] `SYS-972` and `SYS-973`
  isolate the equipment reset and restorative save-fixture transitions.

## New combinations

- [Observation | Corroborated | High] No verified combination is expected;
  deterministic subset validation remains required.

## Taxonomy changes

- [Observation | Direct/Corroborated | High] Two Active boundaries append;
  reused evidence changes no earlier signature or lifecycle.

### Added

- `GAME-0347` as one original-PlayStation equipment-reset, first-relic,
  restorative-save and first-boss threshold packet.
- `SYS-972` and `SYS-973`.

### Reused

- `ACT-008`, `ACT-161`, `ACT-199`, `ACT-341`, `ACT-437`, `SYS-215`,
  `SYS-299`, `SYS-369`, `SYS-398`, `SYS-412`, `SYS-417`, `CON-269`,
  `CON-621`, `INF-119`, `INF-125`, `INF-179` and `OBJ-080`.

### Generalised

- Evidence lists admit this exact carrier without changing operational
  definitions.

### Rejected

- Product-specific genes for Death, Cube of Zoe, Axe, Slogra, Gaibon, Life
  Max Up, each equipment slot, each room, map colour and memory-card block.

### Preserved

- Every lower-ID signature, lifecycle state, verified combination and family
  definition.
