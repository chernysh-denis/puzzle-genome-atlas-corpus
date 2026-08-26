---
game_id: GAME-0151
slug: monster-hunter-wilds
game_title: Monster Hunter Wilds
analysis_status: reviewed
reviewed: 2026-08-21
combination_ids:
  - COMB-0149
gene_ids:
  action:
    - ACT-008
    - ACT-123
    - ACT-131
    - ACT-161
    - ACT-221
    - ACT-243
    - ACT-244
    - ACT-245
    - ACT-246
  system:
    - SYS-215
    - SYS-251
    - SYS-401
    - SYS-402
    - SYS-403
    - SYS-404
    - SYS-405
    - SYS-406
    - SYS-407
    - SYS-408
  constraint:
    - CON-210
    - CON-282
    - CON-285
    - CON-353
    - CON-354
    - CON-355
    - CON-356
    - CON-357
    - CON-358
  information:
    - INF-119
    - INF-125
    - INF-128
    - INF-156
    - INF-157
    - INF-158
  objective:
    - OBJ-081
  time:
    - TIM-003
---

# Game: Monster Hunter Wilds

## Analysis scope

- Version / ruleset: base PC game `Ver.1.042.00.00`, offline single-player,
  from a fresh character and Palico through first completion of Chapter 1-3
  mission `To the Forest`; this matches the current Prologue Demo's bounded
  story content without treating the demo as a different ruleset.
- Included: character and Palico appearance; direct hunter movement; Seikret
  calling, riding, auto-routing and second-weapon carriage; scoutfly tracking;
  all normally available early weapon classes as parameters; direct real-time
  attacks, stamina, sharpness or ammunition; healing and field crafting;
  Focus Mode, localized wounds, Focus Strikes and part breaks; gathering and
  carving; Palico assistance; large-monster pursuit across Windward Plains
  zones; changing locale conditions; faint-and-camp return; assignment target,
  timer and faint limit; Chatacabra and Quematrice story hunts; materials,
  zenny, smithy forging or upgrades and ordered story progression to the
  Scarlet Forest boundary.
- Excluded: online play, SOS participants and Support Hunters; `Forest
  Findings` and every later chapter; High Rank, endgame, Title Update monsters,
  events, arena and challenge quests; capture-only analysis, exhaustive weapon
  moves or build optimisation; cosmetic DLC, photo mode, mods, Ascendance and
  platform achievements.
- Direct-play status: no new paid-account play session was conducted. Current
  Capcom patch and demo announcements, official platform mechanics guides and
  public chapter walkthrough traces were reconciled into deterministic
  repository-side transitions; exact balance and drop rates remain parameters.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `MHW-001` | Ver.1.042.00.00 is the current retail PC boundary and the current offline Prologue Demo ends after `To the Forest` | Confirmed | Direct | High | P1, P2 |
| `MHW-002` | A called Seikret can auto-route to a tracked target while permitting manual deviation, mounted item use and one carried secondary-weapon swap | Confirmed | Corroborated | High | P3, P4 |
| `MHW-003` | Repeated localized attacks create visible wounds; Focus Mode exposes them and a legal Focus Strike destroys one for large damage, control and bonus material | Confirmed | Corroborated | High | P3, P4, P5 |
| `MHW-004` | Weapon attacks resolve against monster body parts while stamina, sharpness, ammunition and committed animations bound legal follow-up actions | Observation | Corroborated | High | P3, P4, S1 |
| `MHW-005` | Reachable field sources and defeated monsters yield finite materials used by inventory recipes and smithy equipment creation or upgrades | Observation | Corroborated | High | P3, P6, S1 |
| `MHW-006` | A hunter faint returns the attempt to camp and consumes one quest allowance; target completion before timer or allowance failure settles rewards and story progress | Observation | Corroborated | High | P6, S1, S2 |
| `MHW-007` | Palico support, large-monster migration and changing Windward Plains conditions continue autonomously while the hunter acts | Confirmed | Corroborated | High | P4, P5 |
| `MHW-008` | The scoped assignments order Chatacabra and Quematrice hunts before `To the Forest` reaches the Scarlet Forest boundary | Observation | Corroborated | High | P2, S2, S3 |
| `MHW-009` | The repository trace reproduces Seikret routing, wound destruction, legal weapon swap, gathering, faint branches, hunt settlement and the chapter gate | Observation | Direct | High | V1 |

## Basic data

- Release / origin: Capcom; released 2025-02-28 and reviewed at PC
  `Ver.1.042.00.00` on 2026-08-21.
- Platform or physical form: third-person real-time hunting action RPG for PC
  and current consoles; the current offline PC opening is scoped.
- Puzzle family: adversarial survival and combat; resource allocation and
  transformation; ordered dependency sequencing.
- Primary sources:
  - **[P1]** [official Steam announcements](https://steamcommunity.com/app/2246340/announcements/),
    for Ver.1.042, offline availability and the August 2026 update boundary.
  - **[P2]** [official PlayStation Prologue Demo page](https://store.playstation.com/en-us/product/UP0102-PPSA35672_00-000000000000DEMO),
    for the fresh opening through completion of `To the Forest`.
  - **[P3]** [official PlayStation new-hunter handbook](https://www.playstation.com/en-us/games/monster-hunter-wilds/monster-hunter-wilds-starters-guide/),
    for camps, Slinger gathering, Seikret items and weapon swap, wounds, Focus
    Strikes, material crafting and smithing preparation.
  - **[P4]** [official Xbox developer tips](https://news.xbox.com/en-us/2025/02/28/monster-hunter-wilds-tips-from-developers/),
    for seamless field hunts, Seikret combat utility, dual weapons, wounds,
    Focus Mode, breakable parts and equipment skills.
  - **[P5]** [official PlayStation hands-on report](https://blog.playstation.com/2024/08/28/monster-hunter-wilds-hands-on-report/),
    for target auto-routing, pack response, autonomous Palico/support activity,
    Focus Strike resolution, pursuit and drastic weather change.
  - **[P6]** [Capcom Wilds online-manual entry](https://www.capcom-support.com/hc/en-us/articles/20394941803292-Monster-Hunter-Wilds-Online-Manual),
    for the maintained official manual boundary.
- Secondary sources:
  - **[S1]** [IGN `Desert Trotters` gameplay trace](https://www.youtube.com/watch?v=hQ4-hiKkoCk),
    for character creation, Seikret pursuit and the mandatory Chatacabra hunt.
  - **[S2]** [Chapter 1 walkthrough](https://game8.co/games/Monster-Hunter-Wilds/archives/498519),
    for ordered Quematrice rescue, preparation and `To the Forest` transition.
  - **[S3]** [main-story mission ledger](https://www.rpgsite.net/guide/16901-monster-hunter-wilds-main-story-quest-list-guide-all-missions-step-by-step-walkthrough),
    for the separation between `To the Forest` and later `Forest Findings`.
- Reproducible control:
  - **[V1]** repository-side transition trace derived from `P1`–`P6` and
    `S1`–`S3`; it is rules reasoning, not a claim of direct play.
- Claim IDs: `MHW-001`–`MHW-009`.

## Mechanical decomposition

### Action Genes

- Existing genes: `ACT-008`, directly navigate the hunter; `ACT-123`, craft a
  declared carried-item recipe; `ACT-131`, consume a potion, ration or other
  immediate item; `ACT-161`, aim and strike a reachable monster; `ACT-221`,
  advance a retained weapon at the smithy.
- New genes: `ACT-243`, call, mount or dismount the Seikret and choose a tracked
  destination; `ACT-244`, exchange the active weapon with the Seikret-carried
  secondary; `ACT-245`, gather or carve one reachable material source;
  `ACT-246`, aim and commit a weapon-specific Focus Strike.
- Parameters: weapon class and move, mount target, item, recipe, material
  source, body part, wound, reach, animation and upgrade tier.
- Claim IDs: `MHW-002`–`MHW-006`.

### System Behaviour Genes

- Existing genes: `SYS-215`, resolve direct real-time hostile combat;
  `SYS-251`, advance an authored cross-region quest sequence.
- New genes: `SYS-401`, route the called Seikret toward a tracked target while
  retaining manual deviation; `SYS-402`, accumulate localized wound and part
  state and resolve Focus destruction; `SYS-403`, migrate and reacquire large
  monsters across connected field zones; `SYS-404`, convert lethal hunter
  damage into camp return and one consumed faint allowance; `SYS-405`, settle
  a completed hunt into materials, zenny and unlocked follow-up state;
  `SYS-406`, forge or upgrade equipment from retained material recipes;
  `SYS-407`, run Palico support alongside direct hunter control; `SYS-408`,
  change locale weather, hazards, creatures and available resources live.
- Resolution order: route to or manually intercept the target; resolve attacks
  against localized body state; update wounds, breaks, health and monster
  movement; on hunter defeat consume a faint allowance and return to camp, or
  on target defeat expose carves and settle quest rewards; retained materials
  may then create stronger equipment before the next authored gate.
- Parameters: target, route, monster zone, wound threshold, body part, damage,
  faint count, timer, reward table, recipe, weather and Palico behaviour.
- Claim IDs: `MHW-002`–`MHW-009`.

### Constraint Genes

- Existing genes: `CON-210`, inventory transfer obeys typed stack and slot
  capacity; `CON-282`, mandatory encounters obey authored predecessor gates;
  `CON-285`, attacks require compatible weapon and ammunition state.
- New genes: `CON-353`, one active and one Seikret-carried weapon bound the
  field loadout; `CON-354`, weapon actions require their stamina, sharpness,
  ammunition and recovery state; `CON-355`, Focus Strike requires a reachable
  highlighted wound or compatible breakable part; `CON-356`, a quest succeeds
  only before its timer or faint allowance fails; `CON-357`, crafting and
  smithing require a known recipe, sufficient compatible materials and any
  declared zenny; `CON-358`, gathering and carving require a reachable eligible
  source with remaining yields.
- Scarce strategic resources: health, stamina, sharpness or ammunition, item
  stacks, two weapon positions, wound openings, quest time, faint allowance,
  material yields and zenny.
- Claim IDs: `MHW-002`–`MHW-008`.

### Information Genes

- Existing genes: `INF-119`, expose hunter health, stamina, status and active
  build; `INF-125`, expose mapped terrain and the current authored objective;
  `INF-128`, expose reachable resource and inventory compatibility state.
- New genes: `INF-156`, Focus Mode highlights wounds and compatible body parts;
  `INF-157`, the hunt HUD exposes target, timer, faint allowance and observed
  monster condition; `INF-158`, scoutflies and the map expose a selected
  target's current route or last tracked position.
- Claim IDs: `MHW-002`–`MHW-008`.

### Objective Genes

- New gene: `OBJ-081`, complete the ordered prologue hunts and reach the
  Scarlet Forest boundary through `To the Forest`.
- Success, evaluation and failure: the first recorded completion of `To the
  Forest` is success; a quest timer or exhausted faint allowance fails that
  attempt without erasing the persistent save.
- Claim IDs: `MHW-006`, `MHW-008`, `MHW-009`.

### Time Genes

- Existing gene: `TIM-003`, hunter input, monster action, Palico support,
  weather and quest time all advance while the field simulation is running.
- Parameters: animation commitment, stamina recovery, monster transition,
  wound duration, item use, weather phase and quest clock.
- Claim IDs: `MHW-002`–`MHW-009`.

## Reproducible transitions

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| A tracked assignment target is selected and the Seikret is nearby | Call, mount and accept automatic travel | The Seikret follows the target route while manual steering can temporarily deviate | target routing is autonomous but not a loss of local control | `MHW-002` |
| Two compatible weapons were assigned at camp | Mount and swap to the secondary | The secondary becomes active and the previous weapon returns to the Seikret slot | the field loadout contains one reversible two-position weapon exchange | `MHW-002` |
| Repeated attacks land on one eligible monster region | Continue damaging that region | A visible wound opens and receives increased wound pressure | wounds are localized combat state, not generic health loss | `MHW-003` |
| Focus Mode highlights an open reachable wound | Commit the weapon's Focus Strike | The wound is destroyed, large damage/control resolves and bonus material may drop | wound creation is converted by a distinct aimed finisher | `MHW-003` |
| No compatible wound or breakable focus point is in reach | Attempt the same Focus Strike | The wound-destruction transition does not resolve | Focus legality depends on body state and alignment | `MHW-003` |
| A melee weapon has degraded sharpness | Continue attacking without sharpening | Legal hits use the degraded sharpness state until maintenance restores it | weapon pressure includes a field-maintenance resource | `MHW-004` |
| A reachable gathering point retains yields | Gather once | One material transfers if inventory capacity permits and the source yield falls | world extraction is finite and capacity bounded | `MHW-005` |
| A slain large monster remains in its carve window | Carve an eligible body point | One table result enters inventory and one carve is consumed | body rewards require a post-defeat timed interaction | `MHW-005` |
| Required materials and zenny satisfy an unlocked smithy recipe | Forge or upgrade the selected weapon | Inputs are consumed and retained equipment state advances | hunt rewards feed persistent preparation | `MHW-005` |
| Hunter health reaches zero with faint allowance remaining | Accept the faint transition | The hunter returns to camp and the shared quest allowance decreases | death is a bounded attempt penalty rather than save deletion | `MHW-006` |
| The final allowed faint is consumed before target completion | Resolve camp return | The assignment fails and must be attempted again | failure is governed by a shared quest allowance | `MHW-006` |
| Chatacabra or Quematrice is the active assignment target | Slay the target before failure | Carves and quest rewards settle and the authored successor becomes available | hunt victory couples combat to campaign progression | `MHW-006` |
| Earlier prologue assignments are complete | Travel to the marked Scarlet Forest approach | `To the Forest` completes at the boundary and later `Forest Findings` remains outside scope | the endpoint is an authored region gate | `MHW-008` |

## Strategic and experiential structure

- Local decision: choose body position, attack or evade, preserve weapon state,
  create or cash a wound, mount to heal or pursue and collect a reachable drop.
- Medium-term planning: pair two weapons, stock consumables, turn hunt rewards
  into a useful upgrade and keep faint/time exposure low across assignments.
- Long-term structure: complete the ordered Windward Plains hunts and follow
  the expedition to the Scarlet Forest boundary.
- Common heuristics: let the Seikret close long pursuit gaps, attack one body
  region until a wound appears, spend the Focus Strike during a safe opening,
  sharpen or heal while mounted and forge only upgrades that help the next gate.
- Failure attribution: body telegraphs, health, stamina and quest limits are
  visible; exact hidden monster health and probabilistic material drops make
  long-term reward planning less exact.
- Player-trust factors: Focus highlights, scoutflies and explicit assignment
  state expose actionable causes without revealing every internal threshold.
- Claim IDs: `MHW-002`–`MHW-009`.

## Replay and variation

- What changes between sessions: chosen weapon pair, attack route, material
  drops, optional gathering, monster movement, locale condition and upgrade.
- Randomness or procedural generation: authored terrain and mission order stay
  fixed; monster positions, behaviours, weather timing and reward rolls vary.
- Multiple viable strategies: fourteen weapon classes, body-part priorities,
  mounted recovery, crafting and equipment choices reach the same story gates.
- Typical replay motive: learn another weapon, improve hunt time, target
  different parts or gather materials for another equipment line.
- Claim IDs: `MHW-002`–`MHW-008`.

## Adjacent systems and history

- Direct predecessors: Monster Hunter: World and earlier Monster Hunter games
  establish quests, carving and equipment-from-hunts; Wilds adds seamless
  target pursuit, the Seikret weapon pair and wound/Focus coupling.
- Variants: online hunts add human participants; later retail chapters add
  regions, ranks and systems outside this prologue; Ascendance is unreleased.
- Similar games: Palworld, Elden Ring and other real-time creature or boss
  hunting games with persistent equipment preparation.
- Important differences: the scoped loop binds a manually overridable
  auto-routing mount, exactly two field weapons and localized wound conversion
  to finite quest attempts and a material-forging progression chain.
- Claim IDs: `MHW-001`–`MHW-008`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-123`, `ACT-131`, `ACT-161`, `ACT-221`, `ACT-243`–`ACT-246` | weapon moves and item identities are parameters |
| System Behaviour | `SYS-215`, `SYS-251`, `SYS-401`–`SYS-408` | exact damage, drops and weather timings are parameters |
| Constraint | `CON-210`, `CON-282`, `CON-285`, `CON-353`–`CON-358` | capacities and timers are parameters |
| Information | `INF-119`, `INF-125`, `INF-128`, `INF-156`–`INF-158` | HUD layout and audiovisual style are excluded |
| Objective | `OBJ-081` | optional hunt order is excluded |
| Time | `TIM-003` | admitted field play remains live |

## Edge cases

- Manual Seikret steering pauses the chosen auto-route rather than clearing the
  tracked destination; normal routing resumes when control is released.
- The secondary weapon is not a third inventory slot: switching exchanges two
  assigned positions and requires the Seikret interaction.
- Ordinary body damage can break a part without an open Focus wound; a Focus
  Strike still requires its own highlighted compatible state.
- A missed Focus Strike consumes its committed animation but does not destroy a
  wound it never reaches.
- Mounting creates mobility and safer item-use opportunities but does not stop
  monster, weather or quest time.
- Inventory overflow does not create extra material; excess remains rejected or
  outside the carried stack boundary.
- A faint with allowance remaining is not quest failure; exhausting the
  allowance or timer is.
- Quest settlement rewards and manually carved materials are separate award
  channels even when they contain the same material identity.
- Completing `To the Forest` does not admit the Lala Barina and Congalala hunts
  in later `Forest Findings`.

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `150` (`GAME-0001`–`GAME-0150`).
- Exact genome matches: none.
- Tied near matches: `GAME-0143` — ARC Raiders (`9 / 76 = 0.118421`).
- Supported combination subsets: `COMB-0149`.
- Scan date: 2026-08-21.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| ARC Raiders (`GAME-0143`) | `ACT-008`, `ACT-123`, `ACT-161`, `ACT-221`, `SYS-215`, `CON-210`, `CON-285`, `INF-128`, `TIM-003` | extraction raids risk retained equipment for hub upgrades; Wilds keeps equipment through finite faints and converts localized hunt outcomes into materials and authored progression | Near, `0.118421` |

### Preserved research notes

- New genes: `ACT-243`–`ACT-246`, `SYS-401`–`SYS-408`, `CON-353`–`CON-358`,
  `INF-156`–`INF-158`, `OBJ-081`.
- Classification result: `New gene` and new combination of known and new genes.
- Evidence and reasoning: the distinctive boundary is the coupling of Seikret
  routing and two-weapon exchange to localized wound conversion, finite quest
  failure and material-fed equipment preparation.

## Combination assessment

- `COMB-0149` is admitted as a verified interaction pattern joining tracked
  mounted pursuit, two field weapons, localized wound conversion, finite hunt
  attempts and material-fed story progression.
- It is a strict subset of the 36-gene genome; independent recurrence is
  unassessed and no exact prior set duplicate is admitted.

## Taxonomy impact

- Registry changes: add 22 bounded genes and `COMB-0149`; extend evidence for
  14 reused records without changing their causal boundaries.
- Taxonomy-change record: none.
- Candidate terms affected: weapon identities, exact stamina, sharpness,
  damage, timer, faint count, material odds and weather intervals are parameters.

## Negative results

- No separate negative-result record. The review rejected Seikret routing as
  direct navigation, wounds as ordinary health, the second weapon as generic
  inventory and a faint as complete mission-checkpoint rollback.

## Delta summary

## Нові факти

- [Confirmed | Corroborated | High] Seikret combines tracked automatic travel,
  manual deviation, mobile item use and a reversible second-weapon slot
  (`MHW-002`).
- [Confirmed | Corroborated | High] Local attacks create wounds that Focus
  Mode exposes and a legal Focus Strike converts into damage, control and
  material (`MHW-003`).
- [Observation | Corroborated | High] Finite quest failure and material-fed
  smithing connect each hunt to the next authored gate (`MHW-005`, `MHW-006`).

## Нові гени

- [Observation | Corroborated | High] 22 bounded genes cover Seikret routing,
  two-weapon exchange, gathering/carving, wounds, monster pursuit, faint and
  reward settlement, equipment production, locale simulation and hunt gates.

## Нові комбінації

- [Confirmed | Corroborated | High] `COMB-0149` — tracked mounted pursuit
  couples wounds, finite hunt attempts and material preparation.

## Зміни таксономії

- [Observation | Direct | High] Змін таксономії немає.

## Family classification

- `FAM-009` — Tactical forecast and counterplay: monster telegraphs, body
  position and wound openings shape attack, evade and Focus timing.
- `FAM-010` — Real-time system pressure: live monster attacks, weapon
  state, hunter health and faint allowance drive execution.
- `FAM-013` — Inventory and fixture dependencies: finite materials and recipes
  gate carried items and smithy equipment.
- `FAM-017` — Ordered dependency sequencing: assignment victories unlock the
  prologue route to the Scarlet Forest boundary.
- No new family is created from a single game.

## Plain-language interpretation

Wilds turns finding a monster into part of the hunt. Choose a target and the
Seikret can carry the hunter along its tracked route, but the player can steer
away to gather, avoid danger or approach from another angle. The mount also
carries exactly one second weapon, so switching tactics is a reversible field
choice rather than a complete return to camp.

Combat is localized. Repeated hits open wounds on specific body regions;
Focus Mode reveals them and a weapon-specific Focus Strike can destroy one for
a strong opening and extra material. A hunt remains bounded by health, weapon
maintenance, a timer and a limited number of faints. Victory then turns body
carves and quest rewards into materials that can be crafted or forged into the
preparation for the next assignment.

## New questions

- Does a later full-campaign scope support a recurring subset with another
  equipment-from-boss-reward game without collapsing wound and part state?

## Наступна рекомендована гра

- [Confirmed | Direct | High] `GAME-0152` — Elden Ring.
- Optimisation criterion: preserve the maintainer-approved sequence and test a
  close real-time boss-combat neighbour with different death, checkpoint and
  build economies.
- Expected information gain: distinguish Monster Hunter's finite quest and
  material-forging loop from one persistent open-world life-and-rune loop.
- Backlog impact: advances the active Goal without starting GAME-0152 here.

## Чому саме вона

- [Hypothesis | Limited | High] Elden Ring should reuse live combat and
  equipment preparation while challenging every Seikret, wound, quest-limit
  and hunt-settlement boundary.
