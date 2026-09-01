---
game_id: GAME-0203
slug: peak
game_title: "PEAK"
analysis_status: reviewed
reviewed: 2026-08-31
combination_ids:
  - COMB-0201
gene_ids:
  action:
    - ACT-008
    - ACT-048
    - ACT-164
    - ACT-165
    - ACT-186
    - ACT-199
    - ACT-200
    - ACT-362
    - ACT-363
    - ACT-364
  system:
    - SYS-036
    - SYS-326
    - SYS-660
    - SYS-661
    - SYS-662
    - SYS-663
    - SYS-664
    - SYS-665
    - SYS-666
    - SYS-667
    - SYS-668
    - SYS-669
  constraint:
    - CON-210
    - CON-286
    - CON-534
    - CON-535
    - CON-536
    - CON-537
  information:
    - INF-073
    - INF-075
    - INF-128
    - INF-258
    - INF-259
  objective:
    - OBJ-125
  time:
    - TIM-003
---

# Game: PEAK

## Analysis scope

- Version / ruleset: unmodified Windows Steam public build `24961053`, official
  patch `2.03.a` dated 2026-08-27, reviewed 2026-08-31; offline
  single-player, standard `Peak` difficulty, on the daily island identified by
  the interval beginning `2026-08-30 17:00 UTC`. That patch batch fixes Gloom
  and The Citadel as the fourth and fifth biomes for this dated island.
- Primary decision loop: from the Crash Site, inspect the next climb, choose
  reachable rests and grip points, spend and recover stamina, open luggage,
  trade carried weight against food, healing and climbing tools, deploy ropes
  or pitons, light each biome campfire and adapt to injury, hunger and local
  hazards until the summit flare can call rescue.
- Entry and exit: entry is the first retained Scout control at the Crash Site
  after leaving the Airport and plane-crash transition. Positive exit is the
  completed helicopter rescue, Scouting Report and expedition result after a
  Flare is lit inside the PEAK region. In solo play, unrecovered unconsciousness
  reaching death is the negative terminal; stop before credits, the Airport or
  another expedition.
- Included: Shore, the dated island's sampled Tropics-or-Roots and
  Alpine-or-Mesa choices, fixed Gloom and The Citadel, the final PEAK; standard
  Peak fog/time pressure; stamina, bonus stamina, hunger, injury and biome
  afflictions; physical falls and ragdoll; luggage and ground items; four
  personal item slots plus worn pack capacity; food, bandages and representative
  hazard remedies; ropes and pitons; biome campfires; summit Flare and rescue.
- Excluded: co-op, voice chat, Helping Hand, carrying or reviving another Scout;
  Tenderfoot, Ascents 1-8 and Custom Expeditions; Caldera, The Kiln and Nadir;
  mods, alternate daily dates, route/location guides, badges, cosmetics,
  achievements as goals, secret encounters, account progression and replay.
- Potential scoped modules: co-op bodily assistance and resurrection, every
  higher Ascent, Nadir, another dated island, Custom Expedition modifiers and
  alternate biome pairs require separate evidence and terminal contracts.
- Direct-play status: no authenticated Windows expedition was played. Official
  product, patch, announcement and achievement pages establish the current
  client, solo envelope, dated rotation batch and escape objective; referenced
  mechanics pages corroborate transitions. The repository trace is rules
  reasoning, not claimed play.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `PEAK-001` | Public Windows build `24961053` carries official patch `2.03.a` from 2026-08-27 | Confirmed | Corroborated | High | P2, S1 |
| `PEAK-002` | PEAK supports offline solo play and frames rescue as climbing the island's central mountain | Confirmed | Direct | High | P1 |
| `PEAK-003` | The scoped dated island belongs to the 2.03.a map batch with Gloom and The Citadel fixed in rotation | Confirmed | Direct | High | P2, P3 |
| `PEAK-004` | Standard Peak is the default difficulty without added Ascent modifiers | Observation | Corroborated | High | S2 |
| `PEAK-005` | Surface grip and climbing consume stamina; injury, hunger, weight and hazards reduce usable climbing capacity | Observation | Corroborated | High | P1, S3, S4 |
| `PEAK-006` | Luggage and natural food provide sampled supplies whose weight, slot use and typed effects change route options | Observation | Corroborated | High | P1, S3, S5 |
| `PEAK-007` | Ropes and pitons create persistent aids only at compatible reachable terrain | Observation | Corroborated | High | P1, S3, S6 |
| `PEAK-008` | Falls and afflictions can cause injury, ragdoll, unconsciousness and eventual death; solo has no ally revival | Observation | Corroborated | High | S3, S4, S7 |
| `PEAK-009` | Six ordered regions and biome campfires structure one ascent while standard Peak pressure keeps time live | Observation | Corroborated | High | P3, S5, S8 |
| `PEAK-010` | Reaching PEAK and lighting a Flare summons the rescue helicopter and settles the expedition | Confirmed | Corroborated | High | P1, P4, S9 |

## Basic data

- Release / origin: Team PEAK; published by Aggro Crab and Landfall Games;
  Windows release 2025, reviewed at patch `2.03.a` on 2026-08-31.
- Platform or physical form: real-time third-person Windows climbing-survival
  game through Steam, with offline single-player selected.
- Puzzle family: stamina-bounded physics climbing through a daily survival route.
- Primary and official sources:
  - **[P1]** [official Steam product page](https://store.steampowered.com/app/3527290/PEAK/),
    for Windows, offline solo, daily island, four intervening biomes, stamina,
    injury, food, survival items and the mountain-rescue framing.
  - **[P2]** [official PEAK Steam home content](https://steamcommunity.com/app/3527290/homecontent/),
    for patch `2.03.a` and its new Gloom/Citadel daily-map batch.
  - **[P3]** [official PEAK Steam announcements](https://steamcommunity.com/app/3527290/announcements/),
    for The Final Ascent, patch `2.0.a`, paired Gloom/Citadel rotation and the
    one-more-week extension covering the scoped daily date.
  - **[P4]** [official Steam achievements](https://steamcommunity.com/stats/3527290/achievements),
    for Peak Badge (`Reach the PEAK`), Lone Wolf Badge (`Escape the island in a
    solo expedition`) and other explicit escape predicates.
- Reproducible mechanics sources:
  - **[S1]** [SteamDB depot record](https://steamdb.info/app/3527290/depots/),
    observed 2026-08-31, for Windows public build `24961053`.
  - **[S2]** [Ascents](https://peak.wiki.gg/wiki/Ascents), for standard Peak as
    the default difficulty and exclusions of Tenderfoot/Ascent modifiers.
  - **[S3]** [How to play](https://peak.wiki.gg/wiki/How_to_play), for Airport
    entry, climbing, stamina, status, unconsciousness and item use.
  - **[S4]** [Stamina](https://peak.wiki.gg/wiki/Stamina), for grip consumption,
    affliction obstruction, carried weight and bonus stamina.
  - **[S5]** [Island](https://peak.wiki.gg/wiki/Island), for the 17:00 UTC daily
    identity and six-region ordered biome structure.
  - **[S6]** [Equipment](https://peak.wiki.gg/wiki/Equipment), for rope, piton,
    food, healing and Flare effects.
  - **[S7]** [Scout death states](https://peak.wiki.gg/wiki/Death), for fall,
    unconsciousness, death and resurrection boundaries.
  - **[S8]** [Gloom](https://peak.wiki.gg/wiki/Gloom) and
    [The Citadel](https://peak.wiki.gg/wiki/The_Citadel), for the fixed late
    pair, campfire gate, hazards and rising pressure.
  - **[S9]** [PEAK biome](https://peak.wiki.gg/wiki/Peak_%28biome%29), for the
    Flare, helicopter, countdown, Scouting Report and expedition closure.
- Claim IDs: `PEAK-001`–`PEAK-010`.

## Mechanical decomposition

### Action Genes

- Existing genes: `ACT-008`, walk, sprint and jump; `ACT-048`, pick up and
  release portable physics items; `ACT-164`, select a carried slot; `ACT-165`,
  consume held food; `ACT-186`, drop a held supply; `ACT-199`, transfer visible
  luggage loot into available capacity; `ACT-200`, use an interruptible remedy.
- New genes: `ACT-362`, engage, maintain or release a reachable surface grip;
  `ACT-363`, deploy a carried rope or piton onto compatible terrain; `ACT-364`,
  ignite one carried Flare in the eligible summit region.
- Parameters: movement, surface, hand reach, grip, stamina, item, slot, weight,
  anchor, tool stock, remedy, Flare and summit-region membership.
- Claim IDs: `PEAK-005`–`PEAK-010`.

### System Behaviour Genes

- Existing genes: `SYS-036`, continuous gravity, collision, momentum and
  ragdoll dynamics; `SYS-326`, generate and populate a procedural survival world.
- New genes: `SYS-660`, initialise a dated solo island expedition; `SYS-661`,
  resolve surface grip, pose and climb from stamina; `SYS-662`, convert falls
  and hazard contacts into ragdoll and injury; `SYS-663`, combine hunger,
  afflictions, weight and food into usable/bonus stamina; `SYS-664`, resolve
  typed food, healing and hazard remedies; `SYS-665`, resolve persistent rope
  and piton support; `SYS-666`, advance biome hazards and rising pressure;
  `SYS-667`, settle a lit campfire into biome passage and morale; `SYS-668`,
  advance zero usable stamina through unconsciousness to solo death; `SYS-669`,
  turn an eligible summit Flare into helicopter rescue and result.
- Resolution order: instantiate the dated island and Crash Site sample; navigate,
  grip and loot; continuously update physics, stamina and hazards; deploy aids
  and consume supplies; light biome campfires; enter PEAK; ignite the summit
  Flare; settle rescue, or terminate when unrecovered solo death occurs.
- Parameters: daily interval, map pool, biome pair, loot sample, surface pose,
  stamina, status mix, fall, injury, tool anchor, hazard phase, campfire, PEAK
  membership, Flare, countdown and result.
- Claim IDs: `PEAK-003`–`PEAK-010`.

### Constraint Genes

- Existing genes: `CON-210`, typed personal slots and stacks bound carried
  supplies; `CON-286`, a remedy requires an eligible incomplete status and an
  uninterrupted use channel.
- New genes: `CON-534`, grip requires reachable climbable surface, positive
  usable stamina and compatible pose; `CON-535`, carried weight and status
  obstruction may not exceed current climbing capacity; `CON-536`, rope or
  piton deployment requires carried stock, reach and compatible terrain;
  `CON-537`, rescue requires a live Scout, PEAK-region presence and an ignitable
  Flare after the ordered ascent.
- Scarce strategic resources: usable and bonus stamina, safe rests, daylight and
  rising-hazard time, injury/hunger/status capacity, inventory slots, carried
  weight, food, remedies, ropes, pitons and the terminal Flare.
- Claim IDs: `PEAK-005`–`PEAK-010`.

### Information Genes

- Existing genes: `INF-073`, expose active item and carried slots; `INF-075`,
  expose stamina, hunger, status and carried survival capacity; `INF-128`,
  expose visible luggage loot and compatibility.
- New genes: `INF-258`, world and body feedback expose grip, climbable surfaces,
  rests, fall risk and local hazards; `INF-259`, biome titles, campfires, PEAK
  membership, Flare response and Scouting Report expose run progress/terminal.
- Candidate genes: none.
- Claim IDs: `PEAK-005`–`PEAK-010`.

### Objective Genes

- New gene: `OBJ-125`, ascend the dated island and complete summit rescue.
- Success, evaluation and failure: PEAK-region Flare ignition followed by the
  helicopter/Scouting Report satisfies the objective. Merely reaching the
  summit, earning a badge or touching the rescue rope does not. Unrecovered solo
  death ends the attempt without success.
- Claim IDs: `PEAK-008`, `PEAK-010`.

### Time Genes

- Existing gene: `TIM-003`, physics, stamina, hunger, item channels and biome
  pressure continue while route decisions are made.
- Candidate genes: none.
- Claim IDs: `PEAK-005`–`PEAK-010`.

## Reproducible transitions

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Standard Peak solo and the `2026-08-30 17:00 UTC` island interval are selected | Board the plane and retain control after the crash | The scoped daily island instantiates one Scout at its Crash Site with sampled luggage and natural supplies | bounded entry and dated setup | `PEAK-002`–`PEAK-004` |
| A climbable face is within hand reach and usable stamina remains | Hold grip, aim the reach and move upward | Contact, pose, gravity and stamina resolve continued attachment or release into fall | core physics-climb relation | `PEAK-005` |
| One luggage item is visible but slots and weight are bounded | Open, compare, take or leave the item | Compatible capacity accepts the chosen item; added weight changes subsequent stamina cost | route-resource coupling | `PEAK-006` |
| One carried rope or piton faces compatible reachable terrain | Deploy the selected aid | Stock is consumed and a persistent climb/rest aid is anchored for later use | authored route intervention | `PEAK-007` |
| A fall or hazard removes all currently usable stamina | Fail to restore capacity before the death timer settles | The Scout passes out; without a living co-op rescuer or scoped checkpoint, death closes the solo attempt | negative terminal | `PEAK-008` |
| The current biome campfire is reachable | Light it | Morale/progress state settles and the route into the next ordered biome becomes available where gated | ascent checkpoint | `PEAK-009` |
| The living Scout is inside PEAK with an ignitable Flare | Ignite the Flare and remain through the rescue countdown | The helicopter arrives, the rescue sequence and Scouting Report run, and the expedition records escape | positive terminal | `PEAK-010` |

## Strategic and experiential structure

- Local decision: judge whether the next grip reaches a stable rest before
  stamina fails, or whether to retreat, eat, heal or place an aid first.
- Medium-term planning: keep weight low enough to climb while reserving the
  specific food, remedy and rope/piton that can cross the next biome hazard.
- Long-term structure: convert six ordered regions and their campfires into a
  continuous route that preserves enough capacity and one Flare for PEAK.
- Common heuristics: test short grips, rest on walkable ledges, drop low-value
  weight, treat stamina obstruction before hard climbs and avoid consuming the
  summit Flare as an ordinary signal.
- Failure attribution: the stamina/status bar, body pose, carried weight, local
  hazard cues, campfire state and biome title distinguish reach, resource,
  timing, fall and route failures.
- Player-trust factors: exact luggage contents and daily geometry are not
  promised in advance; visible surfaces, status loss, item effects, ordered
  progress and the rescue response must remain legible.
- Claim IDs: `PEAK-005`–`PEAK-010`.

## Replay and variation

- What changes between sessions: daily geometry, early biome alternatives,
  luggage and natural-item samples, chosen route, falls and supply consumption.
- Randomness or procedural generation: the daily interval selects one authored
  generated island batch; each expedition additionally samples item contents.
- Multiple viable strategies: low-weight direct climbing, supply-heavy safe
  routing, rope/piton infrastructure or food-driven bonus-stamina bursts.
- Typical replay motive: learn surface reads and hazard economies, then solve a
  new daily route with fewer falls and less discarded supply.
- Claim IDs: `PEAK-003`, `PEAK-005`–`PEAK-010`.

## Adjacent systems and history

- Direct predecessors: physics climbing and compact run-survival lineages; this
  record does not assign unreviewed predecessor mechanics.
- Variants: co-op adds body assistance and resurrection; higher Ascents add
  cumulative constraints; other daily dates replace geometry and biome pairs.
- Similar games: Human: Fall Flat shares real-time body physics and reachable
  grip; Getting Over It shares fall-sensitive vertical progress; Valheim shares
  stamina, food and survival capacity; Don't Starve Together shares sampled
  supplies, status pressure and world-generated routing.
- Important differences: PEAK binds freely targeted surface grip to a stamina
  bar whose usable portion is eaten by several afflictions and carried weight,
  then asks one daily route to preserve a Flare for a mechanical rescue result.
- Claim IDs: `PEAK-002`–`PEAK-010`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-048`, `ACT-164`, `ACT-165`, `ACT-186`, `ACT-199`, `ACT-200`, `ACT-362`–`ACT-364` | exact surfaces, items and controls are parameters |
| System Behaviour | `SYS-036`, `SYS-326`, `SYS-660`–`SYS-669` | daily interval, loot and numeric status effects are parameters |
| Constraint | `CON-210`, `CON-286`, `CON-534`–`CON-537` | slot count, reach, weight and time thresholds are parameters |
| Information | `INF-073`, `INF-075`, `INF-128`, `INF-258`, `INF-259` | visual styling and exact values are presentation |
| Objective | `OBJ-125` | dated island and difficulty are parameters |
| Time | `TIM-003` | grip, recovery and hazard rates are parameters |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `202` (`GAME-0001`–`GAME-0202`).
- Exact genome matches: none.
- Tied near matches: `GAME-0170` — S.T.A.L.K.E.R. 2: Heart of Chornobyl (`10 / 65 = 0.153846`).
- Supported combination subsets: `COMB-0201`.
- Scan date: 2026-08-31.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0170` — S.T.A.L.K.E.R. 2: Heart of Chornobyl | `ACT-008`, `ACT-164`, `ACT-199`, `ACT-200`, `CON-210`, `CON-286`, `INF-073`, `INF-075`, `INF-128`, `TIM-003` | Both make a limited inventory, visible survival capacity and interruptible remedies part of real-time route risk. S.T.A.L.K.E.R. 2 uses authored Zone geography, firearms, detector-led anomaly probing and a retained investigation branch; PEAK uses a dated generated island, free surface grip, body falls, climbing aids and an inventory-carried signal that immediately settles rescue | Near, `0.153846` |

### Preserved research notes

- New genes: `ACT-362`–`ACT-364`, `SYS-660`–`SYS-669`, `CON-534`–`CON-537`,
  `INF-258`, `INF-259` and `OBJ-125`.
- Reused genes: seventeen existing movement, physics, item, survival,
  inventory, information and real-time boundaries; no earlier signature changed.
- Classification result: `New gene` and `New combination of known and new genes`.
- Evidence and reasoning: physics, inventory and survival reuse remains exact;
  freely targeted stamina grip, affliction obstruction, biome pressure and
  Flare-owned rescue remain bounded additions.

## Taxonomy impact

- Registry changes: twenty bounded Active genes and `COMB-0201`; reuse and
  evidence extensions do not change any earlier reviewed signature.
- Taxonomy-change record: none.
- Candidate terms affected: grip stamina, affliction obstruction, bonus stamina,
  climbing aid, biome campfire, daily island and summit rescue.

## Negative results

- The daily date, public build and patch batch identify the island without
  pretending that one route guide or unrecorded random loot is canonical.
- Default Peak is used instead of Tenderfoot or accumulated Ascents; no modifier
  union is imported into the genome.
- Solo death is terminal because the scoped packet excludes another living
  Scout, checkpoint item and co-op resurrection. Revival remains an adjacent
  module, not a silent positive transition.
- Reaching the PEAK is insufficient for the objective: the carried/summit Flare
  must actually invoke the rescue settlement.
- No earlier verified combination was accepted from genre resemblance; the
  proper-subset scan remains validator-owned.

## Delta summary

## Нові факти

- [Confirmed | Corroborated | High] `PEAK-001`–`PEAK-010`: one current standard
  solo daily island links physics grip, stamina/status pressure, supplies,
  climbing aids and biome passage to explicit summit rescue.

## Нові гени

- [Observation | Corroborated | High] Added `ACT-362`–`ACT-364`,
  `SYS-660`–`SYS-669`, `CON-534`–`CON-537`, `INF-258`, `INF-259` and `OBJ-125`.

## Нові комбінації

- [Observation | Corroborated | High] `COMB-0201` — dated solo ascent through
  stamina grip, status obstruction, climbing aids and Flare rescue.

## Зміни таксономії

- [Observation | Corroborated | High] Змін таксономії немає; жодну раніше
  перевірену сигнатуру не змінено.

## Нові питання

- Which Crusader Kings III start and terminal expose one reproducible dynastic
  decision packet without joining incompatible campaign goals?

## Наступна рекомендована гра

- [Hypothesis | Limited | Medium] `GAME-0204` — Crusader Kings III.
- Optimisation criterion: test relationship, title, succession and scheme
  dependencies after one physical survival ascent.
- Expected information gain: move from embodied real-time route pressure to a
  pausable, actor-network grand-strategy state.
- Backlog impact: continue Selection 008 if one current start, ruleset and
  bounded terminal can be fixed.

## Чому саме вона

- [Hypothesis | Limited | Medium] Crusader Kings III should add high-distance
  social and dynastic planning while retaining transparent prerequisites and a
  bounded research trace.
