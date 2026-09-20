---
game_id: GAME-0312
slug: astro-bot
game_title: ASTRO BOT
analysis_status: reviewed
reviewed: 2026-09-19
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-161
    - ACT-341
    - ACT-473
  system:
    - SYS-036
    - SYS-037
    - SYS-045
    - SYS-112
    - SYS-215
    - SYS-369
    - SYS-906
    - SYS-907
  constraint:
    - CON-349
  information:
    - INF-192
  objective:
    - OBJ-181
  time:
    - TIM-003
---

# Game: ASTRO BOT

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Character names,
level names, exact counts, checkpoint positions and button identities
parameterise the genes but do not enter their labels.

## Analysis scope

- Version / ruleset: current PS5 Standard Edition base game by Team ASOBI and
  Sony Interactive Entertainment, checked 2026-09-19, offline single player on
  a fresh save. No installed build or patch number was available.
- Entry: first ordinary control after the Dual Speeder lands in Sky Garden,
  the first level of Gorilla Nebula, before any Bot or Puzzle Piece has been
  credited in that level.
- Primary decision loop: steer Astro through connected floating islands; jump,
  laser-hover and swim across authored gaps; punch ordinary enemies and
  breakable objects while using downward hover against electric enemies;
  strike stranded Bots to rescue them and contact Puzzle Pieces to credit them;
  pull exposed wires, spin fans and unzip fixtures to reveal route mechanisms;
  acquire the level's Inflate ability, hold it to rise into otherwise
  unreachable air and water-tower routes, then reach and break the final glass
  boundary.
- Positive terminal: break Sky Garden's final glass, accept the level closeout
  and return to the galaxy-map state with the level marked complete and every
  Bot or Puzzle Piece acquired on the route still credited. The declared
  reproducible route takes all seven Bots and three Puzzle Pieces, but those
  optional totals are not prerequisites for ordinary completion.
- Negative terminal: enemy or hazard contact, a fall or another lethal state
  ends the current life and restores the latest activated checkpoint. Bots and
  Puzzle Pieces already credited remain collected while post-checkpoint coins
  and transient positions do not.
- Included: direct third-person movement, jumping, laser-hovering and swimming;
  punch and charged spin; ordinary live enemies; local camera lookahead;
  automatic checkpoints; wire, fan and zipper interactions; revealed
  trampolines, slides, rooms and the Inflate pickup; one level-bound balloon
  ascent; seven optional Bot rescues; three optional Puzzle Pieces; the final
  glass exit and return to the galaxy map.
- Excluded: the broader Crash Site loop; every later Gorilla Nebula level and
  boss; other abilities; Gatcha Lab spending; puzzle-piece facility unlocks;
  campaign rescue thresholds; Deluxe cosmetics; post-launch levels and Time
  Attack rankings; trophies; Practice Mode; controller vibration, speaker and
  adaptive-trigger presentation; online features; and any persistence claim
  beyond the written checkpoint and completed-level boundaries.
- Direct-play status: not conducted. No PS5, installed application, controller
  trace, save, screenshot, video or audio was used. Official PlayStation and
  Team ASOBI material establishes the product, platforming basis, controller
  feature boundary and Sky Garden's Inflate ability. Independent written
  walkthroughs establish the exact route, collectibles, checkpoints and final
  glass. This is a source-bounded reconstruction, not a claimed playthrough.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `AB-001` | The packet is the PS5 Standard Edition's first ordinary Sky Garden level, not Astro's Playroom, a Deluxe cosmetic layer or post-launch challenge level | Confirmed | Direct | High | P1, P2 |
| `AB-002` | Astro directly runs, jumps, swims and laser-hovers through connected three-dimensional platform geometry | Confirmed | Corroborated | High | P2, P3, S1 |
| `AB-003` | Punch, charged spin and downward laser-hover defeat compatible enemies or break compatible world objects while electric enemies punish an ordinary punch | Observation | Corroborated | High | P3, S1, S2 |
| `AB-004` | Pulling wires, spinning fans and operating zippers persistently reveal trampolines, a water slide, hidden rooms, Bots or the Inflate pickup | Observation | Corroborated | High | S1, S2, S3 |
| `AB-005` | Sky Garden contains seven Bots and three Puzzle Pieces; striking a stranded Bot credits a rescue while contact credits a Puzzle Piece | Observation | Corroborated | High | S1, S2, S3 |
| `AB-006` | The revealed Inflate pickup grants a Sky Garden-bound ability whose held input expands Astro and lifts him to otherwise unreachable height | Confirmed | Corroborated | High | P3, S1, S2, S3 |
| `AB-007` | Sky Garden contains multiple automatic checkpoints; lethal failure returns to the latest one | Observation | Corroborated | Medium | P3, S1, S4 |
| `AB-008` | Bots and Puzzle Pieces credited before death remain collected, while transient post-checkpoint position and coins are restored | Observation | Corroborated | Medium | S4, S5 |
| `AB-009` | The ordinary route ends after the upper water tube and final Bot when the player breaks the final glass; the level then yields a completed map state | Observation | Corroborated | Medium | S1, S3, P3 |
| `AB-010` | Collecting all seven Bots and three Puzzle Pieces is a reproducible 100% route but is not required to reach the ordinary level exit | Confirmed | Corroborated | High | S2, S3 |
| `AB-011` | The bounded identity joins forgiving checkpoint restoration with persistent optional rescue credit and a temporary vertical-movement form inside one authored platform route | Strong Pattern | Corroborated | High | `AB-002`–`AB-010` |

## Basic data

- Release / origin: Team ASOBI; published by Sony Interactive Entertainment;
  PS5 release 2024-09-06.
- Platform or physical form: PS5 Standard Edition, offline single player,
  fresh save; current official product rules checked 2026-09-19.
- Puzzle family: world topology and perspective; physics and object
  manipulation; tactical forecast and counterplay; real-time system pressure.
- Primary and official sources, accessed 2026-09-19:
  - **[P1]** [official PlayStation product
    page](https://www.playstation.com/en-us/games/astro-bot/), for PS5 Standard
    Edition identity, release, publisher, Team ASOBI, single-player scope,
    action-platform classification, crew-rescue premise, controller feature
    options and Ukrainian screen-language support.
  - **[P2]** [Team ASOBI launch
    announcement](https://blog.playstation.com/2024/05/30/astro-bot-arrives-on-ps5-september-6/),
    for direct running, jumping, enemy contact, hidden secrets, scattered crew,
    level structure and temporary ability design.
  - **[P3]** [official PlayStation hands-on
    report](https://blog.playstation.com/2024/06/12/astro-bot-hands-on-report/),
    for jump, attack, charged spin, laser-hover, quick respawns, Sky Garden's
    connected floating islands and its collectible inflation item.
- Corroborating written sources, accessed 2026-09-19:
  - **[S1]** [The Escapist Gorilla Nebula written
    walkthrough](https://www.escapistmagazine.com/astro-bot-gorilla-nebula-walkthrough-collectibles/),
    for five route sections, punch and hover contact, checkpoints, wire/fan/zip
    operations, swimming, Inflate, the seven rescues, three pieces and final
    glass.
  - **[S2]** [Push Square Sky Garden written
    guide](https://www.pushsquare.com/guides/astro-bot-sky-garden-all-collectibles-bots-puzzle-pieces),
    for the ordered seven-Bot and three-piece route, hidden water room,
    inflatable-octopus pickup, tower ascent and final planter rescue.
  - **[S3]** [PowerPyx Sky Garden written
    guide](https://www.powerpyx.com/astro-bot-sky-garden-bots-puzzle-pieces-locations/),
    for the exact optional totals, zero secret exits, replayability and the
    wire, zipper, Inflate and water-tube sequence.
  - **[S4]** [Game8 checkpoint and death
    guide](https://game8.co/games/Astro-Bot/archives/472024), for automatic
    checkpoint activation, latest-checkpoint restoration and distinct
    persistence of credited Bots/Puzzle Pieces versus post-checkpoint coins.
  - **[S5]** [Access-Ability accessibility
    review](https://access-ability.uk/2024/09/05/astro-bot-accessibility-review/),
    for independent corroboration that death retains found Bots and Puzzle
    Pieces while restoring coin progress to the checkpoint value.
- Source-class limitation: Sky Garden's exact transitions and persistence rules
  are documented by independent written walkthrough and accessibility sources,
  not a first-party rules manual or direct local test. Accordingly the exit and
  checkpoint-detail claims remain Medium confidence even where sources agree.
- Reproducible control: repository-side transition tracing against `P1`–`P3`
  and `S1`–`S5` under the declared entry, route, terminal and exclusions;
  written-evidence reasoning, not direct play.
- Claim IDs: `AB-001`–`AB-011`. No audiovisual evidence was used.

## Mechanical decomposition

### Action Genes

- Existing `ACT-008`: directly run, jump, laser-hover and swim Astro through
  local three-dimensional platform geometry.
- Existing `ACT-161`: punch, charged-spin or direct the hover laser at a
  compatible reachable hostile or breakable object.
- Existing `ACT-341`: address and pull wires, spin fans, operate zippers and
  break the final glass as stateful route interactions.
- New `ACT-473`: while Inflate is available, hold the dedicated input to expand
  Astro and commit a controlled vertical ascent toward higher platforms or
  airborne collectibles.
- Button identity, exact jump arc, hover duration, swim speed and inflation
  rate are parameters. Claims: `AB-002`–`AB-006`, `AB-009`.

### System Behaviour Genes

- Existing `SYS-036`: gravity, velocity, support, water volume and collision
  continuously resolve the moving body against Sky Garden geometry.
- Existing `SYS-037`: contact with a Puzzle Piece marks it acquired without
  ending the level.
- Existing `SYS-045`: ordinary enemies continue their local authored movement
  and attacks without a command for each step.
- Existing `SYS-112`: an accepted wire, fan or zipper operation reveals its
  authored trampoline, slide, room, rescue subject or power-up.
- Existing `SYS-215`: direct attacks and hostile contact resolve in live time
  while route movement remains available.
- Existing `SYS-369`: lethal failure restores the latest activated authored
  checkpoint rather than the failed transient body state.
- New `SYS-906`: a successful strike on a stranded Bot removes or releases that
  world subject, registers its identity as rescued and preserves the rescue
  credit through later checkpoint failure and level settlement.
- New `SYS-907`: collecting the authored Inflate pickup equips a temporary
  traversal capability for the remainder of Sky Garden; leaving or restarting
  its level scope removes that local form rather than creating a permanent
  campaign ability.
- Resolution order: movement and autonomous enemies advance; collisions
  resolve support, water, attack, damage, collection or rescue; an accepted
  fixture interaction exposes its dependent state; checkpoint activation
  records a restoration locus; lethal failure restores transient route state
  while preserving separately credited Bots and Puzzle Pieces. Claims:
  `AB-002`–`AB-009`.

### Constraint Genes

- Existing `CON-349`: the tall post-pool route edge is not ordinarily
  traversable until the level's Inflate capability has been acquired.
- Exact platform spacing, interaction reach, enemy contact volumes, water
  boundaries and number of inflation pulses are instance parameters rather
  than separate constraints. Claims: `AB-004`, `AB-006`.

### Information Genes

- Existing `INF-192`: the third-person camera exposes Astro, nearby platforms,
  enemies, Bots, pieces, checkpoints and interactable fixtures while later
  islands and hidden compartments remain outside the current local horizon.
- Haptic feedback, speaker output and adaptive-trigger force are optional
  presentation channels, not admitted mechanical information genes because
  the official product can be played without each one. Claims: `AB-002`–`AB-006`.

### Objective Genes

- New `OBJ-181`: reach an authored level's ordinary exit, accept its closeout
  and return to the selectable map with the level-completion mark plus every
  optional collectible already credited. Neither all seven Bots nor all three
  Puzzle Pieces are required for ordinary Sky Garden completion.
- Rescue totals are optional persistent progress, not a quota imposed on this
  level terminal. Claims: `AB-005`, `AB-008`–`AB-010`.

### Time Genes

- Existing `TIM-003`: movement, enemy activity, laser-hover, inflation and
  hazard contact continue in real time while the player acts.
- Menus and checkpoint respawns do not convert the route into a turn-based
  planning phase. Claims: `AB-002`, `AB-003`, `AB-007`.

## Reproducible transitions

| Before | Action | Deterministic or bounded resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Astro is on the first island before the first Bot | Run, jump and hold jump across the gap | Ground movement, jump arc and laser-hover carry the body to the next supported island | direct embodied platform navigation | `AB-002` |
| An ordinary enemy blocks the route | Punch or hover-laser through compatible contact | the accepted hit defeats the enemy while unsafe enemy contact defeats Astro | live directed combat | `AB-003` |
| Three exposed wires sit beyond Puzzle Piece 1 | Grab and pull backward | the fixture changes state and reveals a trampoline | interaction exposes a dependent route mechanism | `AB-004` |
| A stranded Bot is reachable | Strike the Bot | the subject is freed, removed from stranded state and credited to the rescue roster | rescue is not ordinary contact collection | `AB-005` |
| A Puzzle Piece is reachable | Contact it | the piece is credited while the level continues | optional contact collection | `AB-005` |
| The inflatable-octopus fixture is open | Collect its pickup | Inflate becomes available for the remaining level route | level-bound capability grant | `AB-004`, `AB-006` |
| Inflate is available below the tower | Hold the Inflate input and steer upward | Astro expands and rises to the higher route while the input remains committed | distinct vertical traversal action | `AB-006` |
| A checkpoint has activated and Astro later dies | Accept the automatic retry | the latest checkpoint position returns; credited Bots and pieces remain while later coins and transient positions reset | split persistence at failure | `AB-007`, `AB-008` |
| The upper water tube has been crossed | Break the final glass | Sky Garden closes, returns to the galaxy map and retains completion plus acquired optional progress | ordinary level terminal | `AB-009`, `AB-010` |

## Strategic and experiential structure

- Local decision: choose jump, hover, swim, attack or fixture timing from the
  currently visible platform and enemy arrangement.
- Medium horizon: inspect side routes before crossing a checkpoint, because
  optional Bots and pieces persist once credited while uncollected branches
  may require backtracking or replay.
- Long horizon: reveal and acquire Inflate, use its vertical reach through the
  tower and water tube, then finish the level with the desired optional tally.
- Reversibility: ordinary movement can often backtrack locally; a rescue or
  piece credit persists through death; post-checkpoint coin and body state do
  not; final exit commits the level closeout.
- Failure attribution: visible hazards, enemy contact and platform boundaries
  make the cause local, while the latest checkpoint limits repetition.
- Player trust: the same fixture must reveal the same authored mechanism,
  checkpoints must restore the same boundary and credited optional progress
  must not be revoked by a later death.

## Replay and variation

- Sky Garden's platform route, fixtures, Bot positions and Puzzle Pieces are
  authored rather than procedurally generated.
- Different legal traces come from optional detours, combat avoidance versus
  defeat, and whether all collectibles are acquired before the final glass.
- Everything needed for the 100% route is replayable; no secret exit exists in
  this level.
- Replay motive is to recover missed Bots or pieces, collect more coins or
  execute the route more cleanly.

## Adjacent systems and history

- Ori and the Will of the Wisps shares direct platform movement, live combat,
  capability-gated edges and checkpoint restoration. Ori's bounded route
  permanently acquires Spirit Edge and ends at a manually used restorative
  save point; Sky Garden grants one level-local form, retains optional rescue
  credit across death and exits to a selectable map.
- Super Mario Bros. shares authored platform geometry, autonomous enemies,
  local lookahead and an exit transition. World 1-1 commits a one-way camera,
  timer and power-state damage ladder; Sky Garden allows three-dimensional
  detours, dense checkpoints and persistent optional rescue state.
- Geometry Dash shares real-time platform danger and optional collectibles,
  but automatically advances a checkpointless icon from 0% after every death.
  Astro is directly steered and resumes at authored checkpoints.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-161`, `ACT-341`, `ACT-473` | exact controls and movement values are parameters |
| System Behaviour | `SYS-036`, `SYS-037`, `SYS-045`, `SYS-112`, `SYS-215`, `SYS-369`, `SYS-906`, `SYS-907` | fixture identity and checkpoint positions are parameters |
| Constraint | `CON-349` | tower geometry and ability reach are parameters |
| Information | `INF-192` | camera angle and hidden-compartment placement are parameters |
| Objective | `OBJ-181` | optional tally and map node are parameters |
| Time | `TIM-003` | update cadence and pause behaviour are parameters |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `311` (`GAME-0001`–`GAME-0311`).
- Exact genome matches: none.
- Tied near matches: `GAME-0293` — Ori and the Will of the Wisps (`7 / 27 = 0.259259`); `GAME-0311` — Super Mario Bros. (`7 / 27 = 0.259259`).
- Supported combination subsets: none.
- Scan date: 2026-09-19.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0293` — Ori and the Will of the Wisps | `ACT-008`, `ACT-161`, `ACT-341`, `SYS-215`, `SYS-369`, `CON-349`, `TIM-003` | Both directly combine live platform movement and combat, contextual fixtures, authored checkpoint restoration and an ability-gated edge. Ori permanently earns Spirit Edge through a mandatory guardian/key chain and ends at a manually used restorative save point; Sky Garden grants one level-local inflation form, preserves optional rescued Bots through death and settles an ordinary replayable map result. | Near, `7 / 27 = 0.259259` |
| `GAME-0311` — Super Mario Bros. | `ACT-008`, `ACT-161`, `SYS-036`, `SYS-037`, `SYS-045`, `INF-192`, `TIM-003` | Both directly steer a platform body through live enemies and local camera information while crediting optional contact collectibles. World 1-1 commits a one-way camera, deadline, mutable blocks and scored successor-stage transition; Sky Garden uses three-dimensional detours, dense checkpoints, struck-subject rescue and a temporary inflation form before returning to a map. | Near, `7 / 27 = 0.259259` |

### Preserved research notes

- New genes: `ACT-473`, `SYS-906`, `SYS-907` and `OBJ-181`.
- Classification result: `New gene`; no verified combination is expected.

## Taxonomy impact

- Registry changes: add one Action, two System Behaviour and one Objective
  boundary; add ASTRO BOT support to twelve compatible existing boundaries.
- Taxonomy-change record: none; no earlier definition or signature changes.
- Candidate terms affected: Inflate, struck Bot rescue, level-bound ability and
  map-return level closeout.

## Negative results

- `SYS-398` is rejected: Inflate is not a permanently retained campaign
  traversal capability in this scope.
- `SYS-902` is rejected: inflation is a level-granted traversal form, not the
  pickup/damage power ladder defined for original Super Mario Bros.
- `OBJ-019` is rejected: Sky Garden does not require a minimum rescue quota at
  its ordinary exit.
- `OBJ-022` is rejected: the rescued Bots are optional credited subjects, not
  a controlled actor set that must all traverse the final glass.

## Delta summary

## New facts

- [Confirmed | Corroborated | High] Sky Garden contains seven optional Bot
  rescues, three optional Puzzle Pieces, a revealed Inflate ability and an
  ordinary exit beyond its upper water-tube route (`AB-004`–`AB-010`).

## New genes

- [Observation | Corroborated | High] `ACT-473`, `SYS-906`, `SYS-907` and
  `OBJ-181` isolate controlled inflation, persistent struck-subject rescue,
  level-bound traversal capability and optional-progress-retaining level
  settlement.

## New combinations

- [Observation | Corroborated | High] No new verified combination.

## Taxonomy changes

- [Observation | Corroborated | High] No earlier taxonomy boundary changes.

## New questions

- Does a directly observed fresh-save run preserve each credited collectible
  across every one of Sky Garden's five checkpoint boundaries exactly as the
  written accessibility sources report?

## Next recommended game

- [Hypothesis | Limited | Medium] `GAME-0313` — Tank 1990, the specific
  Famicom multicart variant named in the active research plan.
- Optimisation criterion: separate two-player base defence, terrain
  destruction, power-up state and stage settlement from existing tank games.
- Expected information gain: high if the exact multicart ROM identity and
  written rules can be frozen without importing Battle City variants.
- Backlog impact: `GAME-0313` remains next; no later unit starts in this commit.

## Why this game

- [Hypothesis | Limited | Medium] A current family-friendly 3D platformer tests
  whether rescue persistence, forgiving checkpoint state and a temporary
  level-only form reuse or split older platform-route boundaries.

## Research checklist

- [x] exact product, platform, entry, route and terminal declared
- [x] direct-play and audiovisual limitations disclosed
- [x] primary product and creator material inspected
- [x] exact Sky Garden route corroborated by independent written sources
- [x] complete six-type gene scan performed
- [x] optional collectibles separated from ordinary level completion
- [x] deterministic lower-ID comparison and combination scan completed
- [ ] reviewed Ukrainian localisation and bilingual presentation completed
- [ ] original artwork and responsive browser checks completed
