---
game_id: GAME-0207
slug: monster-hunter-world
game_title: 'Monster Hunter: World'
analysis_status: reviewed
reviewed: 2026-09-01
combination_ids:
  - COMB-0205
gene_ids:
  action:
    - ACT-008
    - ACT-131
    - ACT-161
    - ACT-245
    - ACT-378
  system:
    - SYS-215
    - SYS-403
    - SYS-404
    - SYS-405
    - SYS-407
    - SYS-687
    - SYS-688
  constraint:
    - CON-210
    - CON-282
    - CON-354
    - CON-356
    - CON-358
  information:
    - INF-073
    - INF-075
    - INF-125
    - INF-157
    - INF-158
  objective:
    - OBJ-128
  time:
    - TIM-003
---

# Game: Monster Hunter: World

## Analysis scope

- Version / ruleset: unmodified Windows Steam public build `15539686`, English
  locale, base-game Low Rank, offline single-player. The save is one fresh
  hunter who has returned to Astera after assigned quest `00102 A Kestodon
  Kerfuffle`; the reviewed packet posts and completes assigned quest `00103
  The Great Jagras Hunt`.
- Platform: Windows Steam public branch, built 2024-08-30 and still current on
  2026-09-01. Other platforms are corroborative product evidence, not the
  executable boundary.
- Mode: solo/private assigned quest. The customised starting Palico remains the
  only autonomous ally; no SOS flare or human hunter joins.
- Entry: retained Astera control after `00102`. Equip the base `Hunter's Knife
  I` Sword & Shield and unchanged base starter armour, leave Defender weapons,
  Guardian armour and add-on item packs unused, post `00103` through the
  Handler or quest board, depart, and take only the quest-issued supplies
  needed by the route.
- Primary decision loop: follow Great Jagras traces until scoutflies expose the
  target; approach and commit short Sword & Shield attacks, guard or evade
  readable attacks, preserve health and stamina, heal from the finite supply,
  sharpen after repeated hits degrade the blade, and reacquire the same target
  when it changes zones. The Palico attacks or supports autonomously while the
  monster spends stamina and may feed. Repeat until the admitted slay terminal
  or a quest-failure condition.
- Positive terminal: slay the target before `50:00` or the third faint, use the
  post-completion window to carve the eligible body, accept the result-screen
  materials and `1,200 z` reward, and stop only after quest completion and
  rewards are retained at resumed Astera control.
- Negative terminal: time expiry or the third faint fails the quest. The first
  two faints return the hunter to camp and reduce the remaining reward/faint
  allowance; abandon, return-from-quest and client termination are not
  positive terminals.
- Excluded: Monster Hunter World: Iceborne ownership, Master Rank, Clutch Claw
  and expansion additions; online sessions, SOS, human partners and event or
  optional quests; expeditions, captures, traps and tranq items; Defender or
  Guardian equipment, add-on supplies, later smithy progression, later hunts,
  speedrun routes, mods, cosmetic DLC and platform achievements.
- Potential scoped modules: another starter weapon, a capture route, a later
  assigned hunt, multiplayer scaling, an Iceborne hunt or smithy progression
  each changes the admitted packet and requires its own version, entry and
  terminal.
- Direct-play status: no authenticated current Steam-client play was performed.
  Capcom's maintained product and web-manual evidence establishes the base
  rules. Current public-build metadata, pinned read-only client master-data
  extraction and two independent quest references corroborate the exact quest
  packet. The transitions below are rules reasoning, not a direct-play claim.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `MHWO-001` | Windows Steam public build `15539686` is the reviewed executable boundary | Confirmed | Corroborated | High | P1, S1 |
| `MHWO-002` | Assigned quest `00103` follows `00102`, is Low Rank two-star in the Ancient Forest, targets one Great Jagras and awards `1,200 z` | Observation | Corroborated | High | S2, S3 |
| `MHWO-003` | The scoped quest has a `50:00` clock and fails on time expiry or the third faint | Observation | Corroborated | High | P3, S3, S4 |
| `MHWO-004` | Traces improve scoutfly acquisition until the flies guide the hunter to the target, then withdraw during combat | Confirmed | Direct | High | P2, P4 |
| `MHWO-005` | Health reaches faint at zero; dashing and some attacks spend regenerating stamina whose maximum can decay over time | Confirmed | Direct | High | P3 |
| `MHWO-006` | Repeated close-range attacks reduce sharpness, increasing deflection risk, while a whetstone restores the gauge | Confirmed | Direct | High | P6 |
| `MHWO-007` | Great Jagras and other large monsters spend stamina, can become observably exhausted and may feed to recover; Great Jagras visibly swells after swallowing prey | Confirmed | Corroborated | High | P5, S2 |
| `MHWO-008` | The same engaged target can leave one Ancient Forest zone and remain the tracked object for reacquisition | Observation | Corroborated | High | P2, P4, S3 |
| `MHWO-009` | The starting Palico independently assists during quests by attacking and gathering | Confirmed | Direct | High | P7 |
| `MHWO-010` | A non-final faint returns the hunter to camp without deleting retained equipment; the finite quest allowance continues | Observation | Corroborated | High | P3, S3, S4 |
| `MHWO-011` | Slaying exposes a carve interaction; the results screen awards materials and zenny before retained quest completion returns control | Confirmed | Direct | High | P2, S2 |
| `MHWO-012` | The repository trace reproduces tracking, supply use, sharpness maintenance, monster feeding, pursuit, faint branches and the retained result terminal | Observation | Direct | High | V1 |

## Basic data

- Release / origin: developed and published by Capcom; Windows version released
  2018-08-09 and reviewed at the current public build on 2026-09-01.
- Platform or physical form: third-person real-time hunting action RPG on PC
  and consoles; only the declared Windows Steam base-game packet is admitted.
- Puzzle family: tactical forecast and counterplay; real-time system pressure;
  inventory and fixture dependencies; ordered dependency sequencing.
- Primary and official sources:
  - **[P1]** [official Steam product page](https://store.steampowered.com/app/582010/Monster_Hunter_World/),
    for the maintained Windows product, Capcom authorship and single-player
    capability.
  - **[P2]** [Capcom manual: Hunting and Questing](https://game.capcom.com/manual/MHW_PC/en/steam/page/3/1),
    for posting, supply items, trace collection, scoutfly withdrawal, combat,
    carving, result-screen rewards and equipment feedback.
  - **[P3]** [Capcom manual: The Game Screen](https://game.capcom.com/manual/MHW_PC/en/steam/page/2/4),
    for the quest clock, time-up failure, health, faint threshold, stamina and
    sharpness display.
  - **[P4]** [Capcom manual: Using Your Scoutflies](https://game.capcom.com/manual/MHW_PC/en/steam/page/5/3),
    for trace-based target acquisition, map selection and route updates.
  - **[P5]** [Capcom manual: Large Monsters](https://game.capcom.com/manual/MHW_PC/en/steam/page/6/1),
    for monster stamina, visible exhaustion, feeding recovery, interruption
    and body-part resistances.
  - **[P6]** [Capcom manual: Close-Range Weapons](https://game.capcom.com/manual/MHW_PC/en/steam/page/8/1),
    for close-range sharpness loss, deflection, whetstone restoration and the
    Sword & Shield boundary.
  - **[P7]** [Capcom manual: What is a Palico?](https://game.capcom.com/manual/MHW_PC/en/steam/page/12/1),
    for the customised persistent Palico's autonomous quest assistance.
- Reproducible mechanics sources:
  - **[S1]** [SteamDB public depots](https://steamdb.info/app/582010/depots/),
    for public build `15539686`, its timestamp and Windows depot boundary.
  - **[S2]** [pinned MHWorldData extraction](https://github.com/gatheringhallstudios/MHWorldData/tree/be7362213d7d1e30b794e3b58d3f87712035658d/source_data),
    for quest `103`, target, type, rank, locale, `1,200 z`, reward table,
    Great Jagras classification/description and base `Hunter's Knife I`.
  - **[S3]** [Game8 quest record](https://game8.co/games/Monster-Hunter-World/archives/311714),
    for the `00102` predecessor, two-star assignment, Ancient Forest, one Great
    Jagras, `50` minutes and `1,200 z` packet.
  - **[S4]** [GamerGuides quest walkthrough](https://www.gamerguides.com/monster-hunter-world/guide/walkthrough/astera-and-the-ancient-forest/great-jagras-the-great-jagras-hunt),
    for independent `50`-minute, three-faint failure and return-to-Astera
    corroboration.
- Reproducible control:
  - **[V1]** repository-side transition trace derived from `P1`–`P7` and
    `S1`–`S4`; it is rules reasoning, not a claim of direct play.
- Claim IDs: `MHWO-001`–`MHWO-012`.

## Mechanical decomposition

### Action Genes

- Existing `ACT-008`: directly navigate the hunter across connected Ancient
  Forest ground.
- Existing `ACT-131`: consume one finite quest supply such as a first-aid med
  or ration at a legal moment.
- Existing `ACT-161`: aim and commit one reachable Sword & Shield strike or
  shield attack against the target.
- Existing `ACT-245`: gather one eligible trace/material or carve one finite
  post-slay body yield.
- New `ACT-378`: commit the whetstone sharpening interaction on the equipped
  close-range weapon.
- Parameters: route, trace, target body part, attack, guard/evade recovery,
  supply, health/stamina effect, source, carve opportunity and sharpness.
- Claim IDs: `MHWO-004`–`MHWO-008`, `MHWO-011`, `MHWO-012`.

### System Behaviour Genes

- Existing `SYS-215`: resolve direct real-time hunter, Palico and monster
  combat through reach, body state, damage, defence and defeat.
- Existing `SYS-403`: retain and update Great Jagras identity as it moves among
  connected Ancient Forest zones and is reacquired.
- Existing `SYS-404`: convert lethal hunter damage into camp return, reward
  reduction and one consumed faint allowance.
- Existing `SYS-405`: settle the completed assigned hunt into result-screen
  materials, zenny, completion flag and resumed Astera control.
- Existing `SYS-407`: let the fixed Palico follow, attack and gather alongside
  direct hunter control.
- New `SYS-687`: spend monster stamina during combat, expose exhaustion and
  resolve feeding recovery or its interruption; Great Jagras' swallowed prey
  also changes its visible belly state.
- New `SYS-688`: degrade close-range sharpness through attacks and restore the
  gauge after a completed whetstone interaction.
- Resolution order: read the target trail; enter combat; alternate direct
  movement, attacks, defence, supplies and sharpening with live monster/Palico
  actions; update health, stamina, sharpness, monster stamina and zone; on a
  non-final faint return to camp, on failure close the attempt, or on target
  slay expose carves and settle rewards before retained hub return.
- Claim IDs: `MHWO-004`–`MHWO-012`.

### Constraint Genes

- Existing `CON-210`: supply pickup and carved-material transfer obey typed
  pouch stacks and free capacity.
- Existing `CON-282`: assigned quest `00103` requires the authored opening and
  completion of predecessor `00102`.
- Existing `CON-354`: attacks, evasion and movement require compatible stamina,
  sharpness and committed-action recovery state.
- Existing `CON-356`: the target condition must finish before `50:00` expires
  or the third faint consumes the allowance.
- Existing `CON-358`: a trace, material or body carve requires a reachable
  eligible source with an unspent yield inside its interaction window.
- Scarce strategic resources: health, stamina, sharpness, first-aid/ration
  stacks, time, two remaining recoverable faints, safe openings, target
  contact, carve opportunities and pouch capacity.
- Claim IDs: `MHWO-002`–`MHWO-012`.

### Information Genes

- Existing `INF-073`: item bar and equipment display expose the selected
  supply, stack and active weapon state.
- Existing `INF-075`: HUD gauges expose hunter health, stamina and close-range
  sharpness sufficiently to judge recovery and maintenance.
- Existing `INF-125`: quest board, objective and explored wildlife map expose
  the current authored assignment and route context.
- Existing `INF-157`: quest interface exposes target, clock, faint/failure
  state, engagement and observable monster condition without exact health.
- Existing `INF-158`: traces, scoutflies and wildlife map expose the selected
  target route, current position or last acquired evidence.
- Claim IDs: `MHWO-002`–`MHWO-012`.

### Objective Genes

- New `OBJ-128`: complete assigned quest `00103` by the admitted Great Jagras
  slay route, accept its results and regain retained Astera control.
- Success, evaluation and failure: success is not the lethal hit alone; the
  result/reward sequence and quest-complete return must settle. Time expiry or
  the third faint fails the attempt; capture is a legal wider-game hunt form
  but deliberately absent from this fixed no-capture packet.
- Claim IDs: `MHWO-002`, `MHWO-003`, `MHWO-010`–`MHWO-012`.

### Time Genes

- Existing `TIM-003`: hunter input, committed animations, Palico support,
  monster actions, stamina recovery, sharpness pressure and the quest clock
  advance in real time during admitted field control.
- Claim IDs: `MHWO-003`–`MHWO-012`.

## Reproducible transitions

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Astera control is retained after `00102`; base starter equipment is unchanged | Equip `Hunter's Knife I`, post assigned quest `00103` and depart solo | The Ancient Forest quest packet loads with one Great Jagras objective, `50:00`, three-faint failure and camp supply box | exact entry, ruleset and predecessor gate | `MHWO-002`, `MHWO-003` |
| Great Jagras is not yet acquired and one eligible trace is reachable | Examine the trace | Tracking evidence increases and scoutflies point toward another trace or the target | tracking is evidence-fed, not omniscient | `MHWO-004` |
| The target has been acquired but combat is not active | Approach and land one legal attack | Combat begins and scoutflies withdraw into their canister | route assistance yields to direct combat | `MHWO-004` |
| Hunter health is below maximum and a first-aid med remains | Use the supply while the action can complete | The stack falls and health is restored by the item's declared effect | items trade finite stock and exposure for survival | `MHWO-005` |
| Repeated close-range attacks have lowered the blade's sharpness | Continue attacking without maintenance | The lower sharpness state persists and attacks face greater deflection risk | weapon commitment includes degrading field state | `MHWO-006`, `MHWO-008` |
| The weapon is degraded and a safe recovery interval exists | Complete one whetstone interaction | Sharpness returns according to the weapon's gauge; combat and quest time were not paused | maintenance consumes time/opening rather than a finite whetstone | `MHWO-006` |
| Great Jagras has spent enough stamina | Observe the next behavior | Salivation/weaker attacks expose exhaustion and the monster may seek food | monster condition creates a temporary offensive choice | `MHWO-007` |
| An exhausted Great Jagras begins an eligible feeding attempt | Interrupt with a legal hit before recovery completes | Feeding recovery is prevented; otherwise swallowed prey restores stamina and visibly swells the belly | target state is causally changeable, not cosmetic | `MHWO-007` |
| The engaged target leaves the current zone alive | Follow updated tracks/map evidence | The same quest target persists in another connected zone and becomes reachable again | migration does not reset target identity | `MHWO-008` |
| Hunter health reaches zero with faint allowance remaining | Resolve the faint | The hunter returns to camp, reward/faint allowance decreases and the target/quest continue | faint is a bounded penalty, not save deletion | `MHWO-010` |
| Two faints have already resolved | Let health reach zero again before target completion | The third faint satisfies the declared failure condition and no positive quest result settles | exact negative terminal | `MHWO-003`, `MHWO-010` |
| Great Jagras remains alive and quest time reaches zero | Advance the clock without satisfying the target | Time-up closes the quest as failure | clock and faint predicates are independent | `MHWO-003` |
| Great Jagras reaches lethal state before failure | Resolve the slay and carve during the completion window | The target becomes an eligible finite carve source; each completed carve consumes one opportunity | combat victory exposes a separate embodied reward channel | `MHWO-011` |
| Quest-complete countdown has closed | Accept materials and zenny on the results screen | Quest `00103` completion and rewards persist, then Astera control resumes | explicit retained positive terminal | `MHWO-011`, `MHWO-012` |

## Strategic and experiential structure

- Local decision: close distance for a short Sword & Shield commitment, guard
  or evade a telegraphed attack, heal, sharpen, attack an exposed body region
  or pursue a departing target.
- Medium-term planning: preserve finite supplies and faint allowance, keep the
  blade above dangerous deflection pressure, use exhaustion/feeding openings
  and leave enough clock for reacquisition and settlement.
- Long-term structure: this packet contains exactly one authored predecessor
  gate and one retained assigned-hunt completion; materials are retained but
  later smithy conversion is outside the terminal.
- Common heuristics: collect enough traces to acquire the route; use brief
  Sword & Shield attacks rather than overcommit; sharpen before contact when
  possible; interrupt feeding; heal only behind space or a monster recovery;
  follow the same target promptly after migration.
- Failure attribution: health, stamina, sharpness, item stack, target, clock and
  quest conditions are visible. Exact target health, Palico policy, recovery
  thresholds and reward rolls remain partly hidden.
- Player-trust factors: scoutfly trails, condition animation, sharpness colour,
  item counts, faint/time messages and the distinct results screen expose the
  main causal boundaries without revealing internal health or AI values.
- Claim IDs: `MHWO-004`–`MHWO-012`.

## Replay and variation

- What changes between attempts: trace route, target zone transitions, Palico
  decisions, attack timing, damage, healing/sharpening windows, monster feeding,
  carves and reward rolls.
- Randomness or procedural generation: authored quest, locale, target identity,
  objective and failure limits remain fixed; AI choice, movement and reward
  tables provide variation without creating a new ruleset.
- Multiple viable strategies: the wider game offers fourteen weapon classes
  and capture, but this reproducible packet fixes one base Sword & Shield and a
  slay route. Within it, positioning, guard/evade timing, supply use, pursuit
  and body targeting remain variable.
- Typical replay motive: reduce faints and time, learn telegraphs, maintain
  sharpness more safely or collect another reward roll; later progression is
  outside the analysis terminal.
- Claim IDs: `MHWO-002`–`MHWO-012`.

## Adjacent systems and history

- Direct predecessors: earlier Monster Hunter games establish posted hunts,
  weapon classes, sharpness, carving and finite-faint quests; World makes
  connected-locality tracking and seamless target pursuit central.
- Variants: another starter weapon replaces the action-resource packet; a
  capture route adds traps, tranq state and a different completion form;
  Iceborne adds expansion equipment and mechanics expressly excluded here.
- Similar games: Monster Hunter Wilds, The Witcher 3: Wild Hunt, Elden Ring and
  other real-time target hunts with preparation, readable enemy state and
  retained post-combat progress.
- Important differences: Monster Hunter Wilds adds Seikret routing, two field
  weapons, localized wounds and Focus Strikes; this World packet instead fixes
  one base weapon and makes evidence-fed scoutfly acquisition, sharpness
  maintenance, visible monster exhaustion/feeding and a discrete posted-quest
  result return the central loop. The Witcher 3's royal-griffin packet solves
  authored clues and hands in a trophy; World repeatedly reacquires one live
  migrating target and settles through the quest system itself.
- Claim IDs: `MHWO-001`–`MHWO-012`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-131`, `ACT-161`, `ACT-245`, `ACT-378` | exact Sword & Shield moves and supplies are parameters |
| System Behaviour | `SYS-215`, `SYS-403`–`SYS-405`, `SYS-407`, `SYS-687`, `SYS-688` | damage, AI and recovery thresholds are parameters |
| Constraint | `CON-210`, `CON-282`, `CON-354`, `CON-356`, `CON-358` | stacks, sharpness, clock, faints and yields are parameters |
| Information | `INF-073`, `INF-075`, `INF-125`, `INF-157`, `INF-158` | audiovisual style and exact hidden health are excluded |
| Objective | `OBJ-128` | capture and later assignments are excluded |
| Time | `TIM-003` | field decisions remain live |

## Edge cases

- `Hunt` can normally be satisfied by slay or capture. This packet carries no
  traps or tranq items and authenticates only the slay branch; that does not
  redefine the wider game's objective.
- A non-final faint is not quest failure and does not reload the pre-quest save;
  the active target and quest remain while the reward/faint allowance falls.
- Whetstone use does not consume a finite whetstone stack, but it requires a
  complete exposed interaction while combat and the quest clock continue.
- Lower sharpness raises deflection risk; it does not make every attack illegal
  or delete the weapon.
- Scoutflies stop guiding during active combat and resume route value after
  disengagement/evidence; they do not move the hunter automatically.
- Great Jagras' swollen belly is visible retained monster state after feeding;
  no unsupported exact damage multiplier or guaranteed topple is claimed.
- Palico assistance is causal but not directly queued, and cannot be treated as
  a second human or deterministic attack schedule.
- The lethal hit triggers quest completion before carves. Carves are finite
  embodied interactions during the result countdown; quest rewards are a
  separate result-screen channel.
- Accepting rewards is not the terminal until the completion flag and rewards
  persist at resumed Astera control.

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `206` (`GAME-0001`–`GAME-0206`).
- Exact genome matches: none.
- Tied near matches: `GAME-0151` — Monster Hunter Wilds (`18 / 42 = 0.428571`).
- Supported combination subsets: `COMB-0205`.
- Scan date: 2026-09-01.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0151` — Monster Hunter Wilds | `ACT-008`, `ACT-131`, `ACT-161`, `ACT-245`, `SYS-215`, `SYS-403`, `SYS-404`, `SYS-405`, `SYS-407`, `CON-210`, `CON-282`, `CON-354`, `CON-356`, `CON-358`, `INF-125`, `INF-157`, `INF-158`, `TIM-003` | both track, pursue and settle a real-time material hunt under sharpness, time and faint pressure; World fixes one starter weapon and turns trace acquisition, whetstone maintenance and feeding exhaustion into one posted Great Jagras result, while Wilds adds Seikret routing, two weapons, wounds, Focus conversion, changing ecology and an ordered multi-hunt prologue | Near, `0.428571` |

### Preserved research notes

- New genes: `ACT-378`, `SYS-687`, `SYS-688` and `OBJ-128`.
- Reused genes: twenty existing records; no earlier reviewed signature changed.
- Classification result: `New gene` and `New combination of known and new genes`.
- Evidence and reasoning: World shares the established hunt/faint/settlement
  kernel with Wilds, but the bounded packet isolates field sharpening and
  monster exhaustion/feeding while removing the later game's Seikret, wound,
  Focus, second-weapon and locale-condition systems.

## Combination assessment

- `COMB-0205` is a strict 20-gene subset joining trace-led reacquisition,
  one-weapon sharpness maintenance, monster exhaustion/feeding, autonomous
  Palico pressure, finite faint/time failure, carving and retained assigned-
  quest settlement.
- No earlier verified combination is a proper subset of the 24-gene genome;
  independent recurrence of `COMB-0205` is unassessed.

## Taxonomy impact

- Registry changes: four new Active genes, evidence-preserving World examples
  on twenty reused genes, `COMB-0205` and four existing family memberships.
- Taxonomy-change record: none; no existing lifecycle, causal boundary or
  reviewed game signature changes.
- Candidate terms affected: exact health, stamina, sharpness, damage, item
  counts, monster thresholds, target route, clock, faint penalty and reward
  rolls remain parameters.

## Negative results

- No separate negative-result record. The review rejected Great Jagras belly
  size as a cosmetic-only state, sharpening as a generic consumable, a faint as
  checkpoint rollback, scoutflies as automatic movement and the result screen
  as equivalent to manual carving.

## Delta summary

## Нові факти

- [Confirmed | Direct | High] Traces feed scoutfly acquisition until combat
  disables guidance; the same target remains reacquirable after migration
  (`MHWO-004`, `MHWO-008`).
- [Confirmed | Direct | High] Close-range attacks degrade sharpness and a timed
  whetstone interaction restores it while the hunt remains live (`MHWO-006`).
- [Confirmed | Corroborated | High] Monster exhaustion and feeding create a
  causal condition loop inside the fixed timed/faint-limited assignment
  (`MHWO-003`, `MHWO-007`).

## Нові гени

- [Observation | Corroborated | High] Four bounded records isolate sharpening,
  sharpness settlement, monster stamina/feeding and the exact retained
  Great Jagras assignment terminal.

## Нові комбінації

- [Observation | Corroborated | High] `COMB-0205` joins evidence-fed pursuit,
  field maintenance, feeding state, Palico assistance and quest settlement.

## Зміни таксономії

- [Observation | Direct | High] Змін таксономії немає.

## Family classification

- `FAM-009` — Tactical forecast and counterplay: attack telegraphs, feeding,
  exhaustion and sharpness determine safe commitments and interruptions.
- `FAM-010` — Real-time system pressure: health, stamina, sharpness, monster
  action, Palico action and quest time advance together.
- `FAM-013` — Inventory and fixture dependencies: finite quest supplies, pouch
  stacks and carve opportunities constrain recovery and reward transfer.
- `FAM-017` — Ordered dependency sequencing: `00102` gates the posted `00103`
  assignment and its retained completion flag.
- No new family is created from one game.

## Plain-language interpretation

The first Great Jagras assignment is not only a fight. The hunter must first
read traces until scoutflies acquire the target, then keep contact as it moves
through the Ancient Forest. The chosen Sword & Shield has short, safe attacks,
but every commitment competes with evasion, healing and a live quest clock.
Repeated hits dull the blade, so a whetstone restores sharpness only if the
hunter finds enough time and space to finish the maintenance action.

The monster has its own changing condition. Combat spends its stamina, visible
exhaustion opens an attack interval, and feeding can restore that resource and
swell Great Jagras' belly unless interrupted. The Palico continues making
independent local choices. A faint usually sends the hunter back to camp and
spends one allowance rather than erasing the attempt; the third faint or time
expiry fails it. Slaying the target exposes finite carves, but completion
closes only when the separate result rewards persist and Astera control returns.

## New questions

- Does a later capture packet support a recurring combination with another
  weakened-target restraint game without collapsing traps, tranq state and
  hunt settlement into ordinary hostile defeat?

## Наступна рекомендована гра

- [Confirmed | Direct | High] `SEARCH_DEMAND_BATCH_008_AUDIT`.
- Optimisation criterion: independently verify all nine Selection 008 units,
  their exact scopes/evidence, Ukrainian first-pass decisions, artwork,
  generated artifacts, comparison parity and the 207-game total.
