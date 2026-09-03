---
game_id: GAME-0164
slug: the-binding-of-isaac-rebirth
game_title: "The Binding of Isaac: Rebirth"
analysis_status: reviewed
reviewed: 2026-08-27
combination_ids:
  - COMB-0162
gene_ids:
  action:
    - ACT-008
    - ACT-130
    - ACT-131
    - ACT-161
    - ACT-190
    - ACT-270
  system:
    - SYS-004
    - SYS-063
    - SYS-215
    - SYS-222
    - SYS-464
    - SYS-465
    - SYS-466
    - SYS-467
    - SYS-468
    - SYS-469
    - SYS-470
  constraint:
    - CON-175
    - CON-402
    - CON-403
    - CON-404
  information:
    - INF-002
    - INF-073
    - INF-119
    - INF-179
    - INF-180
  objective:
    - OBJ-091
  time:
    - TIM-003
---

# Game: The Binding of Isaac: Rebirth

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Parameters describe
gene instances but do not enter the signature.

## Analysis scope

- Version / ruleset: Steam PC base-game **The Binding of Isaac: Rebirth** as
  reviewed on 2026-08-27, installed without Afterbirth, Afterbirth+,
  Repentance or Repentance+; Normal Mode, solo Isaac, a clean save file and one
  ordinary unseeded run. The generated seed may be recorded after entry for
  reproduction, but it is not manually entered because entered seeds disable
  ordinary achievement and unlock credit.
- Primary decision loop: read the current room, health, pickups, held items and
  explored map; move and aim tears, spend a bomb, key, coin or held effect, or
  accept a pedestal item; survive the live hostile response; clear the room or
  choose an open exit; then route through the generated floor toward its boss
  and the next trapdoor.
- Entry and exit: begins when clean-save Isaac first gains control in the
  Basement I starting room of an ordinary unseeded run; succeeds when Mom is
  defeated in Depths II and the first Epilogue ending and persistent unlocks
  settle, or fails when Isaac's final available heart is depleted and the run
  returns to the menu without its room, pickup or item build.
- Included: six ordinary floors from Basement I through Depths II; generated
  room graphs and authored room layouts; room exits, Treasure Rooms, Shops,
  secret-wall discovery, locked doors and chests; direct movement and aimed
  tears; enemies, enemy shots, contact damage and finite room clearance; red,
  soul and black heart layers when encountered; coins, bombs, keys, cards,
  pills, trinkets, one active-item slot and passive collectibles; item-pool
  sampling, cumulative item effects, charges, pickups and room-clear awards;
  floor bosses, trapdoors, Mom, run-ending death and clean-save unlock credit.
- Excluded: every DLC; Hard Mode, Challenges, manually entered or special
  seeds, local co-op, mods, debug tools and console commands; Womb and later
  chapters, Boss Rush, Mega Satan and alternate routes; later characters,
  completion-mark campaigns, exhaustive item catalogue completion, Steam
  achievements beyond the scoped transition and repeated metaprogression.
- Potential scoped modules: the base-game Mom's Heart route, one shared
  manually entered seed without unlock credit, a single Challenge, Hard Mode,
  local co-op, or one separately versioned Repentance route.
- Direct-play status: not conducted. Publisher and creator material establish
  the base product, random-run, item and reset boundaries; the maintained
  version-aware wiki supplies reproducible base-Rebirth transition detail.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `ISAAC-001` | Rebirth is the standalone base game and its four named gameplay expansions are excluded modules | Confirmed | Direct | High | P1, P2 |
| `ISAAC-002` | An ordinary run is generated from a seed, while manually entering that seed suppresses normal unlock credit | Confirmed | Corroborated | High | P1, P4, S1 |
| `ISAAC-003` | Each floor composes an authored-room graph with a guaranteed boss and scoped special-room roles | Confirmed | Corroborated | High | P3, S2 |
| `ISAAC-004` | Isaac moves and fires tears in real time while hostile movement, shots and contact continue | Confirmed | Corroborated | High | P1, P3, S3 |
| `ISAAC-005` | Hostile combat rooms keep exits closed until the required enemy set is cleared, then may award a pickup | Confirmed | Corroborated | High | P5, S3, S4 |
| `ISAAC-006` | Coins, bombs and keys are distinct finite run resources for shops, blasts and locked access | Confirmed | Corroborated | High | P5, S5–S7 |
| `ISAAC-007` | Passive, active and immediate-use items alter the current run under typed slots, charges and cumulative interactions | Confirmed | Corroborated | High | P1, P3, S8–S10 |
| `ISAAC-008` | Ordered heart layers absorb damage and final health depletion terminates the run | Confirmed | Corroborated | High | S11, S12 |
| `ISAAC-009` | Defeating each floor boss opens the next descent, and first-time Mom defeat in Depths II reaches the Epilogue boundary | Confirmed | Corroborated | High | S13–S15 |
| `ISAAC-010` | Terminal run state is discarded while earned clean-save unlocks remain available to later runs | Confirmed | Corroborated | High | P3, S1, S15, S16 |

## Basic data

- Release / origin: designed by Edmund McMillen, developed and published by
  Nicalis, and released for PC on 2014-11-04.
- Platform or physical form: room-based top-down real-time action roguelike
  controlled by keyboard or gamepad.
- Puzzle family: tactical forecast and counterplay; real-time system pressure;
  inventory and fixture dependencies; ordered dependency sequencing.
- Primary and reproducible sources:
  - **[P1]** [Steam product page](https://store.steampowered.com/app/250900/The_Binding_of_Isaac_Rebirth/),
    for the base product, random action-RPG loop, seeded runs, item scale,
    controls and separate DLC catalogue.
  - **[P2]** [official Steam DLC catalogue](https://store.steampowered.com/dlc/250900/The_Binding_of_Isaac_Rebirth/),
    for the separate Afterbirth, Afterbirth+, Repentance and Repentance+ modules.
  - **[P3]** [PlayStation launch article](https://blog.playstation.com/2014/10/30/enter-insanity-the-binding-of-isaac-rebirth-hits-ps4-vita-114/),
    written by Nicalis producer Tyrone Rodriguez, for random rooms, enemies,
    levels, drops, items, bosses and all-new restarts after victory or death.
  - **[P4]** [Nicalis Rebirth announcement](https://blog.nicalis.com/blog/the-binding-of-isaac-rebirth-finds-a-new-home/),
    for the remake and base-content boundary.
  - **[P5]** [creator gameplay explanation](https://edmundmcmillen.blogspot.com/2011/09/binding-of-isaac-gameplay-explained.html),
    for generated room composition, core room roles, clearance rewards and
    risk/reward structure inherited and expanded by Rebirth.
- Secondary reproducible sources:
  - **[S1]** [Seeds](https://bindingofisaacrebirth.wiki.gg/wiki/Seeds), for
    version-bound seed reproduction and the no-trophy consequence of manual entry.
  - **[S2]** [Level Generation](https://bindingofisaacrebirth.wiki.gg/wiki/Level_Generation),
    for room-count, dead-end and special-room placement rules.
  - **[S3]** [Rooms](https://bindingofisaacrebirth.wiki.gg/wiki/Rooms), for
    room states, combat doors and exit transitions.
  - **[S4]** [Room Clear Awards](https://bindingofisaacrebirth.wiki.gg/wiki/Room_Clear_Awards),
    for eligible pickup sampling after clearance.
  - **[S5]** [Pickups](https://bindingofisaacrebirth.wiki.gg/wiki/Pickups), for
    hearts, coins, bombs, keys, batteries, pills, cards, runes and chests.
  - **[S6]** [Keys](https://bindingofisaacrebirth.wiki.gg/wiki/Keys), for
    locked rooms and chest access.
  - **[S7]** [Bombs](https://bindingofisaacrebirth.wiki.gg/wiki/Bombs), for
    timed blast, combat, rock and secret-room-wall effects.
  - **[S8]** [Items](https://bindingofisaacrebirth.wiki.gg/wiki/Items), for
    active/passive classes, run duration and cumulative effects.
  - **[S9]** [Item pools](https://bindingofisaacrebirth.wiki.gg/wiki/Item_pool),
    for room- and source-conditioned item selection.
  - **[S10]** [Cards and Runes](https://bindingofisaacrebirth.wiki.gg/wiki/Card),
    for the bounded one-use pocket effect.
  - **[S11]** [Hearts](https://bindingofisaacrebirth.wiki.gg/wiki/Hearts), for
    red, soul and black-heart acquisition and depletion order.
  - **[S12]** [Health](https://bindingofisaacrebirth.wiki.gg/wiki/Health), for
    terminal health and damage application.
  - **[S13]** [Chapters](https://bindingofisaacrebirth.wiki.gg/wiki/Chapters),
    for the ordinary Basement, Caves and Depths sequence.
  - **[S14]** [Depths](https://bindingofisaacrebirth.wiki.gg/wiki/Depths), for
    the guaranteed Depths II Mom encounter.
  - **[S15]** [Mom](https://bindingofisaacrebirth.wiki.gg/wiki/Mom), for the
    first final-boss and Epilogue/unlock boundary.
  - **[S16]** [Achievements](https://bindingofisaacrebirth.wiki.gg/wiki/Achievements),
    for persistent in-save secrets and seed restrictions.
- Reproducible control: **[V1]** repository-side transition trace across
  `P1`–`P5` and `S1`–`S16`; rules reasoning, not a direct-play claim.
- Claim IDs: `ISAAC-001`–`ISAAC-010`.

## Mechanical decomposition

### Action Genes

- Existing genes: `ACT-008`, directly navigate Isaac; `ACT-130`, spend coins
  on a current Shop offer; `ACT-131`, consume the held card, rune or pill;
  `ACT-161`, aim and fire tears at a reachable hostile; `ACT-190`, activate the
  held charged item.
- New gene: `ACT-270`, place one carried bomb with a timed fuse.
- Parameters: movement direction, tear direction and cadence, item identity,
  target, coin price, bomb position, fuse, card or pill effect and charge state.
- Claim IDs: `ISAAC-004`, `ISAAC-006`, `ISAAC-007`.

### System Behaviour Genes

- Existing genes: `SYS-004`, select random outcomes; `SYS-063`, consume a key
  at a compatible locked barrier; `SYS-215`, resolve directly commanded live
  combat; `SYS-222`, pick up eligible dropped run resources on contact.
- New genes: `SYS-464`, generate a seed-determined floor graph; `SYS-465`,
  settle hostile-room clearance and its award; `SYS-466`, apply damage and
  healing through ordered heart layers; `SYS-467`, compose collected item
  effects into the current build; `SYS-468`, advance the boss-gated floor
  sequence; `SYS-469`, clear terminal run state while retaining eligible
  unlocks; `SYS-470`, resolve one timed bomb blast.
- Resolution order: entering a new floor generates its graph and room contents;
  entering a combat room locks its exits; movement, attacks, enemies and shots
  advance continuously; hits change hearts and defeated enemies leave the set;
  the final required defeat opens exits and may roll a pickup; resource and
  item choices change later actions; boss clearance opens the next floor; Mom
  defeat or final-health loss settles the run and persistent save effects.
- Parameters: seed, floor depth, room pool, room role, enemy set, reward roll,
  heart layers, item pool, effect ordering, boss identity and unlock condition.
- Claim IDs: `ISAAC-002`–`ISAAC-010`.

### Constraint Genes

- Existing gene: `CON-175`, final persistent-health depletion terminates the run.
- New genes: `CON-402`, combat-room exits stay closed until required clearance;
  `CON-403`, typed pickups gate key, bomb and coin interactions; `CON-404`, one
  active, one trinket and one pocket slot bound the carried special-item state.
- Scarce strategic resources: health, coins, bombs, keys, active-item charges,
  the pocket slot, room-clear reward opportunities and safe floor routes.
- Claim IDs: `ISAAC-005`–`ISAAC-008`.

### Information Genes

- Existing genes: `INF-002`, future generated contents remain unpreviewed;
  `INF-073`, carried special items and their active state are visible;
  `INF-119`, current health, effects and active-item readiness are visible.
- New genes: `INF-179`, expose the current room's bodies, hazards, shots,
  pickups and exits; `INF-180`, retain an explored room graph and disclosed
  special-room roles.
- Parameters: room camera, projectile visibility, minimap cells and icons,
  heart display, pickup counts, held item, charge bar and visible transformations.
- Claim IDs: `ISAAC-002`, `ISAAC-003`, `ISAAC-006`–`ISAAC-008`.

### Objective Genes

- New gene: `OBJ-091`, defeat Mom on Depths II and reach the clean-save
  Epilogue before run-ending health loss.
- Success, evaluation and failure: first Mom defeat settles success and unlocks
  the Epilogue/next chapter; any earlier final-health depletion ends this run
  and discards its generated floor, pickups and item build.
- Claim IDs: `ISAAC-008`–`ISAAC-010`.

### Time Genes

- Existing gene: `TIM-003`, room movement, tears, hostiles, projectiles, fuse
  countdowns and contact resolution continue in real time while input remains open.
- Claim IDs: `ISAAC-004`–`ISAAC-009`.

## Reproducible transitions

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Clean-save Isaac enters Basement I without typing a seed | Start the ordinary run | The game chooses a seed and instantiates an authored-room graph with room roles and concealed contents | Explicit entry and seed-controlled generation | `ISAAC-002`, `ISAAC-003` |
| Isaac enters a living-enemy room | Cross the doorway | Combat doors close; enemies, tears and hazards continue until the finite required set is gone | Room clearance is a gate, not decorative combat | `ISAAC-004`, `ISAAC-005` |
| One required enemy remains | Fire tears and avoid its response | Valid hits reduce its health; its defeat empties the required set, opens doors and may produce an award | Live combat causally advances the route | `ISAAC-004`, `ISAAC-005` |
| A locked Treasure Room is adjacent and Isaac has one key | Enter its door | One key is consumed and the room becomes accessible for this floor | Typed key budget gates an optional build choice | `ISAAC-006` |
| A suspicious wall borders an eligible secret room and Isaac has one bomb | Place a bomb beside the wall | Fuse expiry applies the blast; a valid secret boundary opens while nearby actors and rocks may also be affected | Bomb position trades finite supply for access and combat utility | `ISAAC-006` |
| Isaac touches a passive pedestal item | Accept the item | The item leaves the pedestal and its effect composes with the current run build until terminal reset | Items are cumulative rule changes, not score tokens | `ISAAC-007` |
| Isaac holds a charged active item | Activate it | The declared effect resolves and charge is spent; later eligible room clear can refill it | Active items are reusable but readiness-bounded | `ISAAC-007` |
| Damage reaches Isaac with soul hearts outside red hearts | Receive the hit | The eligible outer layer is reduced first; later compatible heart pickups restore only legal capacity | Heart type and order shape survival decisions | `ISAAC-008` |
| A floor boss is defeated | Enter the opened trapdoor | The next floor is generated at the following depth and the current run build persists | Boss-gated floors form one continuous run | `ISAAC-003`, `ISAAC-009` |
| Mom is defeated in Depths II on the clean save | Let the result settle | The first Epilogue plays and eligible persistent unlock state is recorded while the transient run ends | Explicit success and metaprogression boundary | `ISAAC-009`, `ISAAC-010` |
| Isaac's last available half-heart is removed before Mom falls | Let damage settle | The death screen ends the run; room graph, pickups and item build do not carry into New Run, while prior unlock state remains | Explicit failure and run reset | `ISAAC-008`, `ISAAC-010` |

## Strategic and experiential structure

- Local decision: keep distance and a safe dodge lane; focus threats; decide
  whether a key, bomb, coin, charge or health trade is worth the immediate room.
- Medium-term planning: route among visible room connections, preserve access
  resources for Treasure Rooms or Shops and accept item effects whose
  interactions improve damage, survivability or room control.
- Long-term structure: carry one generated run build through six boss-gated
  floors, with no checkpoint restoration of that build after death, until Mom.
- Common heuristics: circle-strafe rather than retreat into shots; clear the
  highest-pressure enemy first; keep one key for the Treasure Room; test likely
  secret-room walls only when bomb value exceeds survival value; judge items
  as interactions, not isolated bonuses.
- Failure attribution: visible enemy bodies, projectiles, hazards, hearts,
  pickup counts, item state and explored map explain current risk; unrevealed
  rooms, drops and item identities retain deliberate uncertainty.
- Player-trust factors: stable seed reproduction within the same version,
  readable hitboxes, consistent room-clear locks, predictable typed-resource
  consumption and deterministic item-effect ordering.
- Claim IDs: `ISAAC-002`–`ISAAC-010`.

## Replay and variation

- What changes between sessions: floor graph, room layouts, enemies, bosses,
  pickups, item identities, Shop offers, secret-room location and item synergies.
- Randomness or procedural generation: a run seed determines most generated
  choices, while the current version and unlocked pools bound the result.
- Multiple viable strategies: tear positioning, aggressive or conservative
  health use, Shop versus key/bomb conservation and item-led build adaptation.
- Typical replay motive: reach the next ending, test new item interactions,
  complete character marks, share a seed or improve execution; only the first
  clean-save Mom route is admitted here.
- Claim IDs: `ISAAC-002`, `ISAAC-003`, `ISAAC-006`, `ISAAC-007`, `ISAAC-010`.

## Adjacent systems and history

- Direct predecessors: The Binding of Isaac and Wrath of the Lamb supplied the
  core generated-room action-roguelike that Rebirth remade and expanded.
- Variants: Afterbirth, Afterbirth+, Repentance and Repentance+ add modes,
  paths, items, characters, online play and balance changes outside this scope.
- Similar games: Slay the Spire shares seed-bound run structure, finite health,
  random offers and terminal reset; Path of Exile 2 shares live combat and item
  composition but retains a character build across Softcore deaths.
- Important differences: Rebirth builds a concealed room graph from authored
  layouts, locks local exits behind live clearance, makes collectible effects
  cumulative within a disposable run and uses separate keys, bombs and coins
  to price information, access and power.
- Claim IDs: `ISAAC-001`–`ISAAC-010`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-130`, `ACT-131`, `ACT-161`, `ACT-190`, `ACT-270` | character, tear cadence, offer, item and bomb values are parameters |
| System Behaviour | `SYS-004`, `SYS-063`, `SYS-215`, `SYS-222`, `SYS-464`–`SYS-470` | seed, room, reward, heart, item and unlock identities are parameters |
| Constraint | `CON-175`, `CON-402`–`CON-404` | health, price, resource count and slot count are parameters |
| Information | `INF-002`, `INF-073`, `INF-119`, `INF-179`, `INF-180` | exact HUD position, map icons and sprite style are presentation |
| Objective | `OBJ-091` | Mom identity and first-ending state are scoped parameters |
| Time | `TIM-003` | room pacing, shot cadence and bomb fuse are parameters |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `163` (`GAME-0001`–`GAME-0163`).
- Exact genome matches: none.
- Tied near matches: `GAME-0150` — Hollow Knight: Silksong (`8 / 42 = 0.190476`).
- Supported combination subsets: `COMB-0162`.
- Scan date: 2026-08-27.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0150` | `ACT-008`, `ACT-130`, `ACT-161`, `ACT-190`, `SYS-215`, `INF-073`, `INF-119`, `TIM-003` | Silksong preserves a capability-gated campaign character across checkpoint deaths; Rebirth instead composes a seed-generated room run, clears its item build at a terminal and retains only eligible unlock credit | Near, `0.190476` |

## Combination status

- `COMB-0162` is a verified strict subset coupling seed-generated room routing,
  live hostile clearance, heart survival, cumulative item effects, boss-gated
  floors and terminal run reset into the first Mom ending.
- The deterministic subset scan found no other verified combination supported
  by the complete genome.

## Reuse and novelty decision

- Reused genes: `ACT-008`, `ACT-130`, `ACT-131`, `ACT-161`, `ACT-190`,
  `SYS-004`, `SYS-063`, `SYS-215`, `SYS-222`, `CON-175`, `INF-002`, `INF-073`,
  `INF-119` and `TIM-003` retain their established parameterised boundaries.
- New genes: `ACT-270`, `SYS-464`–`SYS-470`, `CON-402`–`CON-404`, `INF-179`,
  `INF-180` and `OBJ-091` isolate the room-run rules absent from earlier carriers.
- Rejected near terms: `SYS-168` exposes a branching act-node route rather than
  a locally explored room graph; `SYS-455` resets one campaign area while
  retaining a character build; `OBJ-055` fixes a three-act card climb rather
  than the first six-floor Mom route.
- Registry changes: fourteen new stable genes and `COMB-0162`; no lifecycle or
  earlier signature change.

## Taxonomy impact

- Registry changes: fourteen new stable genes, `COMB-0162`, evidence additions
  to fourteen reused genes and memberships in `FAM-009`, `FAM-010`, `FAM-013`
  and `FAM-017`.
- Taxonomy-change record: none; no existing definition or earlier signature changes.
- Candidate terms affected: none.

## Negative results

- `SYS-168` is not reused because it generates a disclosed branching act map
  from nodes; Rebirth reveals a spatial room graph locally and instantiates
  authored room contents on entry.
- `SYS-455` is not reused because Path of Exile 2 preserves equipment, skills
  and character progression while resetting one campaign area; Rebirth clears
  the entire run build at its terminal.
- `OBJ-055` is not reused because the required act count, card-combat sequence
  and third-act boss are part of its boundary.
