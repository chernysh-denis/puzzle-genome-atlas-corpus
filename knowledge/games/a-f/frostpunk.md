---
game_id: GAME-0130
slug: frostpunk
game_title: Frostpunk
analysis_status: reviewed
reviewed: 2026-08-20
combination_ids:
  - COMB-0128
gene_ids:
  action:
    - ACT-006
    - ACT-036
    - ACT-068
    - ACT-120
    - ACT-139
    - ACT-140
    - ACT-149
    - ACT-157
    - ACT-166
    - ACT-167
    - ACT-168
  system:
    - SYS-004
    - SYS-045
    - SYS-046
    - SYS-123
    - SYS-156
    - SYS-161
    - SYS-194
    - SYS-224
    - SYS-225
    - SYS-226
    - SYS-227
    - SYS-228
    - SYS-229
    - SYS-230
    - SYS-231
    - SYS-232
    - SYS-233
    - SYS-234
    - SYS-235
  constraint:
    - CON-062
    - CON-136
    - CON-172
    - CON-173
    - CON-184
    - CON-185
    - CON-211
    - CON-212
    - CON-213
    - CON-214
    - CON-215
    - CON-216
  information:
    - INF-001
    - INF-002
    - INF-059
    - INF-067
    - INF-071
    - INF-077
    - INF-078
    - INF-079
    - INF-080
  objective:
    - OBJ-065
  time:
    - TIM-003
---

# Game: Frostpunk

## Analysis scope

- Version / ruleset: original PC game `1.6.2`, base-game `A New Home` on the
  standard Medium difficulty, from the eighty-person arrival at Generator 623
  through survival of the Great Storm and the scenario epilogue.
- Included: radial building and streets; workers, engineers and optional
  Automatons; workplaces, recipes, shifts and construction; finite piles and
  deposits; research; generator, Steam Hubs, heaters and Overdrive; housing,
  food, sickness and medicine; Adaptation plus one Order or Faith path; Hope,
  Discontent, promises and Londoners; Beacon, scouts and Frostland; refugees,
  storm preparation and the final storm.
- Excluded: Easy, Hard, Extreme and Survivor parameters; Endless Mode; The
  Arks, Refugees, Fall of Winterhome and DLC scenarios; settlements from On the
  Edge; achievements, mods, save-scumming, speedruns and post-victory play.
- Direct-play status: not conducted. Official product and patch materials set
  the product boundary; the maintained Frostpunk mechanics reference provides
  reproducible scenario transitions.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `FPN-001` | The player lays streets and places material-backed building plans; free citizens construct them and finite workers, engineers or Automatons staff bounded jobs | Confirmed | Corroborated | High | P1, S1, S7 |
| `FPN-002` | Staffed workplaces repeatedly extract or transform resources, while staffed Workshops progress one prerequisite-valid technology | Confirmed | Corroborated | High | P1, S8 |
| `FPN-003` | Configured generator, Steam Hubs and heaters continuously consume coal; weather, insulation and active sources determine each occupied building's heat category | Confirmed | Direct | High | P1, S2, S3 |
| `FPN-004` | Overdrive raises heat without ordinary extra coal but accumulates visible stress whose critical outcome can destroy the generator | Confirmed | Direct | High | S2 |
| `FPN-005` | Cold exposure produces staged sickness; compatible warm staffed medical beds treat it, while untreated grave illness can kill | Confirmed | Corroborated | High | S3, S4 |
| `FPN-006` | Prepared rations are consumed by population; shortage progresses through hunger and starvation | Confirmed | Corroborated | High | P1, S1 |
| `FPN-007` | Signing a law irreversibly applies its rule, unlocks declared content and may close an alternative; Order and Faith are mutually exclusive Purpose paths | Confirmed | Direct | High | P1, P2, S5 |
| `FPN-008` | Laws, conditions, deaths, promises and events update visible Hope and Discontent; an unresolved final warning ends the captaincy | Confirmed | Direct | High | P1, S5, S6 |
| `FPN-009` | A Beacon permits finite scout teams to travel among revealed Frostland nodes, resolve dilemmas, reveal successors and return cargo or survivors | Confirmed | Corroborated | High | P1, S9 |
| `FPN-010` | A New Home advances through authored event arcs from Winterhome and the Londoners to refugees, preparation and the final Great Storm | Confirmed | Corroborated | High | S1, S10 |
| `FPN-011` | Surviving the seven-day Great Storm completes the scenario and presents a retrospective of the city's laws and moral choices | Confirmed | Corroborated | High | S1, S5, S10 |
| `FPN-012` | Live time may be paused or accelerated; production, needs, travel, weather and deadlines advance only with simulation time | Confirmed | Corroborated | High | P1, S1 |

## Basic data

- Release / origin: 11 bit studios, original Windows release 2018; scoped to
  the final PC patch `1.6.2` rather than the distinct forthcoming Frostpunk 1886.
- Platform or physical form: pausable real-time radial city-builder and society
  survival strategy.
- Puzzle family: automation and spatial programming; real-time system pressure;
  agent routing and coordination; ordered dependency sequencing.
- Primary sources:
  - **[P1]** [Frostpunk on Steam](https://store.steampowered.com/app/323190/Frostpunk/), official heat, construction, resource, law and exploration overview.
  - **[P2]** [Original Frostpunk is a complete experience](https://steamcommunity.com/app/323190/allnews/), current 11 bit confirmation that original Frostpunk has no further planned mechanical development and laws are lasting choices.
  - **[P3]** [Patch 1.6.2](https://steamcommunity.com/ogg/323190/announcements/detail/3325369912538283866), official final-version announcement.
- Secondary sources:
  - **[S1]** [A New Home](https://frostpunk.fandom.com/wiki/A_New_Home), scenario sequence, default Medium boundary and storm objective.
  - **[S2]** [Generator](https://frostpunk.fandom.com/wiki/Generator), coal, power, range, Overdrive and stress.
  - **[S3]** [Heat](https://frostpunk.fandom.com/wiki/Heat), discrete temperature aggregation and illness risk.
  - **[S4]** [Sickness](https://frostpunk.fandom.com/wiki/Sickness), illness stages, beds and treatment rules.
  - **[S5]** [Book of Laws](https://frostpunk.fandom.com/wiki/Book_of_Laws), permanent branches, cooldowns and ending judgement.
  - **[S6]** [Final Warning](https://frostpunk.fandom.com/wiki/Final_Warning_%28Arc%29), Hope and Discontent terminal grace periods.
  - **[S7]** [Street](https://frostpunk.fandom.com/wiki/Street), generator-rooted facility connection.
  - **[S8]** [Workshop](https://frostpunk.fandom.com/wiki/Workshop), staffed research and tier progression.
  - **[S9]** [Scouting](https://frostpunk.fandom.com/wiki/Scouting), Frostland travel, cargo and reveal graph.
  - **[S10]** [The Great Storm](https://frostpunk.fandom.com/wiki/The_Great_Storm), final seven-day system pressure.
- Claim IDs: `FPN-001`–`FPN-012`.

## Mechanical decomposition

### Action Genes

- Reused: `ACT-006` changes speed; `ACT-036` staffs jobs; `ACT-068` lays the
  street network; `ACT-120` selects applicable workplace recipes; `ACT-139`
  places and dismantles buildings; `ACT-140` commits dilemma or promise
  responses; `ACT-149` selects research; `ACT-157` forms and routes scouts.
- New: `ACT-166` configures workplace shifts and abilities; `ACT-167` signs an
  irreversible law; `ACT-168` configures heat-source and Overdrive modes.
- Claim IDs: `FPN-001`–`FPN-004`, `FPN-007`–`FPN-010`, `FPN-012`.

### System Behaviour Genes

- Reused: `SYS-004`, `SYS-045`, `SYS-046`, `SYS-123`, `SYS-156`, `SYS-161`
  and `SYS-194` cover bounded random outcomes, citizen motion and assigned work,
  scout travel, production, finite extraction and staffed research.
- New: `SYS-224`–`SYS-235` cover coal burn, heat aggregation, sickness,
  treatment, Overdrive stress, weather, authored arcs, food, Hope/Discontent,
  laws, exploration rewards and autonomous construction.
- Resolution order: accept edits; assign construction and work; execute
  production/research and coal burn; apply weather and building heat; consume
  rations and advance illness/treatment; move scouts; resolve events, laws and
  welfare; test generator and civic failure; advance the storm objective.
- Claim IDs: `FPN-001`–`FPN-012`.

### Constraint Genes

- Reused: `CON-062` footprint compatibility; `CON-136` prerequisite chains;
  `CON-172` recipe/input/output state; `CON-173` deposit-bound extractors;
  `CON-184` owned designs and build costs; `CON-185` finite staffed slots.
- New: `CON-211` street connectivity; `CON-212` law prerequisites, cooldown and
  exclusivity; `CON-213` critical generator outcome; `CON-214` final civic
  warning; `CON-215` medical eligibility; `CON-216` scout formation and travel.
- Scarce strategic resources: live labour, engineers, healthy people, coal,
  wood, steel, Steam Cores, food, beds, warm space, research time, Hope,
  Discontent headroom, scout time and pre-storm days.
- Claim IDs: `FPN-001`–`FPN-011`.

### Information Genes

- `INF-001` exposes current city state; `INF-002` keeps bounded random outcomes
  unpreviewed; `INF-059` exposes research dependencies; `INF-067` exposes task
  deadlines and consequences; `INF-071` exposes resources, labour and survival
  reports. `INF-077`–`INF-080` expose weather/heat, welfare/promises,
  generator diagnostics and Frostland team state.
- Claim IDs: `FPN-001`–`FPN-012`.

### Objective Genes

- `OBJ-065` requires New London to survive through the Great Storm, after which
  the scenario judges the route's laws and decisions.
- Claim IDs: `FPN-010`, `FPN-011`.

### Time Genes

- `TIM-003` permits pause and speed changes while all live production, needs,
  weather, travel, deadlines and crises otherwise advance together.
- Claim IDs: `FPN-012`.

## Reproducible transitions

| Before | Action | Deterministic or bounded resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Empty compatible crater footprint; design unlocked; materials available | Place a Workshop plan and connect it by street | Materials are committed; free citizens build it; five assigned Engineers make research progress during its shift | placement, construction, connectivity, staffing and research are distinct | `FPN-001`, `FPN-002` |
| Generator on at power/range one with coal | Advance one live hour | Coal reserve falls by the displayed rate and the active zone supplies its heat modifier | heat supply is a fuel-backed continuous system | `FPN-003` |
| Tent in active zone during a temperature drop | Advance time | Weather penalty, tent insulation and source heat recompute its category; colder exposure raises sickness risk | ambient schedule and local heat jointly determine health pressure | `FPN-003`, `FPN-005` |
| Generator stress below critical | Enable Overdrive | Heat bonus applies without ordinary extra coal while stress rises; disabling it reverses stress direction | Overdrive trades future failure margin for present warmth | `FPN-004` |
| Sick citizen; warm staffed Medical Post with a free compatible bed | Advance treatment time | Citizen occupies capacity, ceases ordinary work and recovers when progress completes | healthcare is staffed, heated and capacity-bounded | `FPN-005` |
| Soup law available and signing cooldown clear | Sign Soup | Soup permanently replaces the ordinary ration option where applicable, increases output per raw food and adds Discontent | law choice rewrites rules and welfare | `FPN-006`–`FPN-008` |
| Hope near zero starts a final warning | Fail to restore Hope within two days | Captain is deposed or banished and the scenario ends | welfare is a terminal constraint, not flavour | `FPN-008` |
| Beacon active; five workers free; Lost Expedition revealed | Form scouts and select destination | Team leaves city, traverses route and on exploration can escort survivors and reveal successor nodes | exploration is a staffed route-and-reveal system | `FPN-009` |
| Winterhome arc resolved | Advance scenario | Londoners and later refugee/storm-preparation arcs activate from authored predecessor state | campaign pressure is state-triggered rather than a storyteller sample | `FPN-010` |
| Great Storm reaches New London with reserves prepared | Survive its seven live days | Food production and scouting close, temperature collapses, but a viable heated city reaches the epilogue | prior resource and law choices are tested by one terminal storm | `FPN-010`, `FPN-011` |

## Strategic and experiential structure

- Local decision: place one facility, move finite staff, change a shift or heat
  mode, sign a law, answer a promise, select research or route scouts.
- Medium-term planning: balance coal, food, warmth, medical capacity, research,
  construction labour and welfare while scripted arcs narrow the schedule.
- Long-term structure: build enough productive and social capacity to absorb
  refugees, neutralise the Londoners and stockpile for the storm without
  destroying the generator or captaincy.
- Failure attribution: visible forecasts, heat states, resource rates, Hope,
  Discontent and deadlines make most collapse chains inspectable; random scout
  outcomes and later dilemmas remain bounded unknowns.

## Replay and variation

- What changes: crater layout details, random event and scout outcomes, chosen
  technologies, Order or Faith, law branches, promises, staff plan and storm
  preparation.
- Randomness: selected exploration and event outcomes vary; the principal
  scenario arcs and weather horizon are authored.
- Multiple viable strategies: yes; coal sources, heat layout, healthcare,
  workforce, law morality and Purpose path vary under the same storm ending.

## Adjacent systems and history

- Similar games: Against the Storm, Oxygen Not Included, RimWorld, Dwarf
  Fortress and Cities: Skylines.
- Important differences: Frostpunk compresses its staffed city into a finite
  authored moral scenario where fuel-backed heat, paired civic tracks and a
  known terminal storm dominate, rather than an open-ended colony or repeated run.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-006`, `ACT-036`, `ACT-068`, `ACT-120`, `ACT-139`, `ACT-140`, `ACT-149`, `ACT-157`, `ACT-166`–`ACT-168` | staffing, plan, law, heat and scout parameters |
| System Behaviour | `SYS-004`, `SYS-045`, `SYS-046`, `SYS-123`, `SYS-156`, `SYS-161`, `SYS-194`, `SYS-224`–`SYS-235` | production, heat, survival, welfare and scenario parameters |
| Constraint | `CON-062`, `CON-136`, `CON-172`, `CON-173`, `CON-184`, `CON-185`, `CON-211`–`CON-216` | build, staff, law, generator, civic, medical and scout gates |
| Information | `INF-001`, `INF-002`, `INF-059`, `INF-067`, `INF-071`, `INF-077`–`INF-080` | city, forecast, task, welfare, generator and map disclosure |
| Objective | `OBJ-065` | Great Storm survival and epilogue |
| Time | `TIM-003` | pausable live scenario clock |

## Corpus comparison

- Genome signature `(ACT; SYS; CON; INF; OBJ; TIM)`: `ACT-006,ACT-036,ACT-068,ACT-120,ACT-139,ACT-140,ACT-149,ACT-157,ACT-166,ACT-167,ACT-168; SYS-004,SYS-045,SYS-046,SYS-123,SYS-156,SYS-161,SYS-194,SYS-224,SYS-225,SYS-226,SYS-227,SYS-228,SYS-229,SYS-230,SYS-231,SYS-232,SYS-233,SYS-234,SYS-235; CON-062,CON-136,CON-172,CON-173,CON-184,CON-185,CON-211,CON-212,CON-213,CON-214,CON-215,CON-216; INF-001,INF-002,INF-059,INF-067,INF-071,INF-077,INF-078,INF-079,INF-080; OBJ-065; TIM-003`.
- Indexed games scanned: 130, including this record.
- Indexed combinations scanned: 128.
- Exact genome matches: none.
- Near matches and similarity scores: `GAME-0124` is highest at
  `19 / 81 = 0.234568`.
- Supported combination subsets: `COMB-0128`.
- Scan date: 2026-08-20.

### Full prior-game Jaccard scan

- GAME-0001: 3 / 64 = 0.046875; GAME-0002: 1 / 59 = 0.016949; GAME-0003: 0 / 62 = 0.000000; GAME-0004: 4 / 64 = 0.062500.
- GAME-0005: 1 / 59 = 0.016949; GAME-0006: 1 / 61 = 0.016393; GAME-0007: 1 / 60 = 0.016667; GAME-0008: 1 / 59 = 0.016949.
- GAME-0009: 3 / 66 = 0.045455; GAME-0010: 1 / 61 = 0.016393; GAME-0011: 1 / 65 = 0.015385; GAME-0012: 1 / 61 = 0.016393.
- GAME-0013: 1 / 65 = 0.015385; GAME-0014: 1 / 67 = 0.014925; GAME-0015: 2 / 65 = 0.030769; GAME-0016: 4 / 64 = 0.062500.
- GAME-0017: 0 / 66 = 0.000000; GAME-0018: 5 / 67 = 0.074627; GAME-0019: 1 / 62 = 0.016129; GAME-0020: 2 / 65 = 0.030769.
- GAME-0021: 2 / 60 = 0.033333; GAME-0022: 2 / 63 = 0.031746; GAME-0023: 0 / 63 = 0.000000; GAME-0024: 1 / 64 = 0.015625.
- GAME-0025: 5 / 59 = 0.084746; GAME-0026: 2 / 63 = 0.031746; GAME-0027: 3 / 62 = 0.048387; GAME-0028: 5 / 65 = 0.076923.
- GAME-0029: 4 / 61 = 0.065574; GAME-0030: 4 / 63 = 0.063492; GAME-0031: 2 / 62 = 0.032258; GAME-0032: 1 / 63 = 0.015873.
- GAME-0033: 2 / 64 = 0.031250; GAME-0034: 3 / 64 = 0.046875; GAME-0035: 3 / 68 = 0.044118; GAME-0036: 1 / 64 = 0.015625.
- GAME-0037: 1 / 61 = 0.016393; GAME-0038: 2 / 67 = 0.029851; GAME-0039: 1 / 61 = 0.016393; GAME-0040: 1 / 60 = 0.016667.
- GAME-0041: 2 / 62 = 0.032258; GAME-0042: 2 / 60 = 0.033333; GAME-0043: 1 / 66 = 0.015152; GAME-0044: 1 / 62 = 0.016129.
- GAME-0045: 1 / 66 = 0.015152; GAME-0046: 1 / 62 = 0.016129; GAME-0047: 1 / 66 = 0.015152; GAME-0048: 1 / 66 = 0.015152.
- GAME-0049: 0 / 62 = 0.000000; GAME-0050: 1 / 67 = 0.014925; GAME-0051: 6 / 63 = 0.095238; GAME-0052: 2 / 61 = 0.032787.
- GAME-0053: 1 / 61 = 0.016393; GAME-0054: 1 / 63 = 0.015873; GAME-0055: 1 / 62 = 0.016129; GAME-0056: 1 / 60 = 0.016667.
- GAME-0057: 1 / 60 = 0.016667; GAME-0058: 1 / 61 = 0.016393; GAME-0059: 1 / 59 = 0.016949; GAME-0060: 1 / 59 = 0.016949.
- GAME-0061: 1 / 62 = 0.016129; GAME-0062: 1 / 60 = 0.016667; GAME-0063: 1 / 59 = 0.016949; GAME-0064: 1 / 57 = 0.017544.
- GAME-0065: 0 / 60 = 0.000000; GAME-0066: 0 / 63 = 0.000000; GAME-0067: 2 / 59 = 0.033898; GAME-0068: 0 / 61 = 0.000000.
- GAME-0069: 1 / 60 = 0.016667; GAME-0070: 1 / 60 = 0.016667; GAME-0071: 1 / 59 = 0.016949; GAME-0072: 1 / 60 = 0.016667.
- GAME-0073: 1 / 59 = 0.016949; GAME-0074: 1 / 61 = 0.016393; GAME-0075: 1 / 61 = 0.016393; GAME-0076: 1 / 59 = 0.016949.
- GAME-0077: 1 / 59 = 0.016949; GAME-0078: 1 / 59 = 0.016949; GAME-0079: 1 / 59 = 0.016949; GAME-0080: 1 / 59 = 0.016949.
- GAME-0081: 1 / 60 = 0.016667; GAME-0082: 1 / 60 = 0.016667; GAME-0083: 1 / 60 = 0.016667; GAME-0084: 1 / 62 = 0.016129.
- GAME-0085: 1 / 63 = 0.015873; GAME-0086: 2 / 64 = 0.031250; GAME-0087: 3 / 60 = 0.050000; GAME-0088: 2 / 60 = 0.033333.
- GAME-0089: 2 / 60 = 0.033333; GAME-0090: 2 / 66 = 0.030303; GAME-0091: 2 / 60 = 0.033333; GAME-0092: 4 / 59 = 0.067797.
- GAME-0093: 2 / 60 = 0.033333; GAME-0094: 2 / 61 = 0.032787; GAME-0095: 2 / 63 = 0.031746; GAME-0096: 2 / 61 = 0.032787.
- GAME-0097: 2 / 59 = 0.033898; GAME-0098: 2 / 58 = 0.034483; GAME-0099: 1 / 60 = 0.016667; GAME-0100: 1 / 63 = 0.015873.
- GAME-0101: 0 / 63 = 0.000000; GAME-0102: 0 / 60 = 0.000000; GAME-0103: 1 / 61 = 0.016393; GAME-0104: 1 / 61 = 0.016393.
- GAME-0105: 1 / 62 = 0.016129; GAME-0106: 0 / 60 = 0.000000; GAME-0107: 1 / 60 = 0.016667; GAME-0108: 1 / 62 = 0.016129.
- GAME-0109: 3 / 66 = 0.045455; GAME-0110: 2 / 59 = 0.033898; GAME-0111: 2 / 58 = 0.034483; GAME-0112: 2 / 59 = 0.033898.
- GAME-0113: 2 / 65 = 0.030769; GAME-0114: 2 / 58 = 0.034483; GAME-0115: 1 / 58 = 0.017241; GAME-0116: 2 / 57 = 0.035088.
- GAME-0117: 1 / 60 = 0.016667; GAME-0118: 3 / 66 = 0.045455; GAME-0119: 10 / 66 = 0.151515; GAME-0120: 2 / 80 = 0.025000.
- GAME-0121: 3 / 73 = 0.041096; GAME-0122: 4 / 64 = 0.062500; GAME-0123: 3 / 88 = 0.034091; GAME-0124: 19 / 81 = 0.234568.
- GAME-0125: 15 / 80 = 0.187500; GAME-0126: 13 / 83 = 0.156627; GAME-0127: 16 / 85 = 0.188235; GAME-0128: 8 / 61 = 0.131148.
- GAME-0129: 3 / 85 = 0.035294.

### Registry normalisation 006 score corrections

These recomputed values supersede the pre-normalisation fractions above:

- `GAME-0125`: `16 / 79 = 0.202532`
- Current prior-corpus near match after normalisation 006: `GAME-0124`.

## Evidence and unknowns

- The official store, final patch and current developer statement establish the
  stable original product. The maintained mechanics reference corroborates the
  reproducible scenario rules. Direct play would refine numeric rates and rare
  event order, not the admitted causal boundaries.

## Verification status

- Structure, evidence, localisation, web presentation, artwork and validation:
  reviewed in this unit.

## Taxonomy impact

- New genes: `ACT-166`–`ACT-168`, `SYS-224`–`SYS-235`, `CON-211`–`CON-216`,
  `INF-077`–`INF-080`, `OBJ-065`.
- Revised reuse boundaries: `SYS-123`, `CON-062`, `CON-184`.
- New family: none; existing `FAM-008`, `FAM-010`, `FAM-015`, `FAM-017` fit.

## Negative results

- `SYS-177` rejected: A New Home weather is an authored finite forecast, not a
  repeating Drizzle-Clearance-Storm cycle.
- `SYS-179` rejected: Hope and Discontent are paired city-wide civic tracks,
  not per-group Resolve that causes individual departures.
- `SYS-188` rejected: Frostpunk aggregates heat modifiers into building
  categories without conserved material-cell heat or phase transitions.
- `SYS-203` rejected: scenario arcs are authored state triggers rather than a
  pressure-scaled storyteller incident scheduler.
- `OBJ-053` rejected: A New Home has a fixed terminal storm and epilogue rather
  than an open-ended city-growth horizon.

## Delta summary

## Нові факти

- Bounded original Frostpunk to the stable 1.6.2 A New Home Medium campaign and
  decomposed the complete city-to-storm dependency route.

## Нові гени

- Added twenty-six atomic boundaries for heat, survival, laws, civic pressure,
  scouting and authored storm progression; reused twenty-seven existing genes.

## Нові комбінації

- Added `COMB-0128` for a staffed fuel-heated city under irreversible law and
  terminal storm pressure.

## Зміни таксономії

- Added Frostpunk to four existing causal families; no one-game family added.
