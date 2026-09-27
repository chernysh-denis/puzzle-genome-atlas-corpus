---
game_id: GAME-0402
slug: the-oregon-trail
game_title: "The Oregon Trail"
analysis_status: reviewed
reviewed: 2026-09-25
combination_ids: []
gene_ids:
  action:
    - ACT-538
    - ACT-539
    - ACT-540
    - ACT-541
  system:
    - SYS-004
    - SYS-1075
    - SYS-1076
    - SYS-1077
    - SYS-1078
  constraint:
    - CON-695
  information:
    - INF-400
  objective:
    - OBJ-236
  time:
    - TIM-029
---

# Game: The Oregon Trail

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Named places,
profession, date, quantities and Apple II keys are parameters, not genes.

## Analysis scope

- Version / ruleset: MECC's 1985 Apple II school disk `A-157`, not the
  separately packaged home disk `H-106`, the older text game, DOS ports or
  later remakes. The original A-157 instructional booklet is the principal
  rule source. No executable revision or disk image was inspected.
- Entry: the player has chosen the farmer profession and March departure,
  named the five-person party, bought a legal outfit at Matt's store and now
  stands at Independence's first trail menu before choosing `Continue on
  trail`. The actual quantities of oxen, food, ammunition, clothing, spare
  parts and cash are recorded parameters. The school booklet gives the farmer
  $400, carpenter $800 and banker $1600 to outfit; H-106's different bank
  budget is not silently imported.
- Primary decision loop: read current date, weather, health, food, supplies
  and distance; adjust steady/strenuous/grueling pace and filling/meager/bare
  bones rations; continue for travel days that consume food and change
  progress and health under weather and possible events; optionally spend
  days resting, hunting or trading to protect health or supplies; at the
  Kansas River inspect width and depth, then ford, caulk and float, pay/wait
  for a ferry, or wait for conditions to change; resolve an attempt's risk
  and continue until the wagon and surviving party reach the far bank.
- Positive terminal: the Kansas crossing succeeds and the continuing party
  is on the far bank, ready for the next leg. Reaching the near bank or merely
  choosing a crossing method does not settle this bounded interval.
- Negative terminal: the journey ends before that crossing because the
  wagon leader and remaining party die. A crossing accident that loses goods
  or party members but leaves the journey running is a setback, not by itself
  a terminal. The exact sequence of rare simultaneous deaths is uninspected.
- Included: pre-purchased finite outfit; travel-policy changes; daily mileage,
  ration expenditure, health, weather and situation-dependent events; menu
  status/map/supply inspection; rest, on-trail trade and one-day hunting with
  100-pound carryback cap; Kansas river's displayed depth/width, legal
  ford/float/ferry/wait options, their day/cash costs and possible accidents;
  first-crossing success and whole-party failure. The optional acts are
  included because they can change resources before this crossing.
- Excluded: profession/month choice and store purchasing before entry;
  downstream Big Blue, Green and Snake crossings, forts and trail branches;
  end-of-journey Oregon scoring, Columbia rafting, top-ten list, sound,
  epitaph editing, classroom activities, historical claims about real
  emigrants, cheats and every other software edition. The exact random
  seed, event probabilities, weather trace, encounter stock and accident
  ordering are not inferred from the printed model.
- Reproducible parameterisation: start an A-157 Apple II run as a farmer in
  March, capture the chosen legal store basket and initial menu, then log
  every pace/ration setting, `Continue` day, date/weather/health/food/mileage,
  random event, rest, trade and hunt outcome; at Kansas capture depth/width,
  available methods, selected action, spent day/cash, losses and far-bank
  state. Repeat with distinct rainfall and river decisions to separate the
  fixed model from random outcomes. A no-hunt/no-trade trace is permitted but
  does not remove those eligible alternatives from this scoped ruleset.
- Direct-play status: none. Neither an A-157 disk/binary nor gameplay video,
  screenshot, input trace or audio was inspected. The edition-specific A-157
  booklet directly documents the menus, examples and underlying model; one
  later Apple II written route corroborates practical first-crossing choices.
  The H-106 home booklet was consulted only to detect edition divergence.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `OT-001` | A-157 offers banker $1600, carpenter $800, farmer $400; outfit and month precede travel. | Confirmed | Direct | High | P1 |
| `OT-002` | Travel menu permits inspecting supplies/map, changing pace/rations, resting and trading; the three pace and ration levels have different effects. | Confirmed | Direct | High | P1 |
| `OT-003` | Daily speed depends on pace, healthy oxen, party illness, terrain and snow; pace raises mileage at a welfare cost. | Confirmed | Direct | High | P1 |
| `OT-004` | Food, weather, pace, rest and illness feed the party's daily general-health state; sickness/injury can kill a member and all-party loss ends the journey. | Confirmed | Direct | High | P1 |
| `OT-005` | Hunting spends a day and at most 100 pounds of meat return to the wagon; on-trail trade also spends a day. | Confirmed | Direct | High | P1, P2 |
| `OT-006` | Kansas is the first modelled river and offers ford, caulk/float, ferry or wait; depth and width are displayed before a method is chosen. | Confirmed | Direct | High | P1 |
| `OT-007` | A Kansas ferry costs $5 and can require up to six days; floating spends a full day; ford and float risk change with water conditions and accidents remain possible. | Confirmed | Direct | High | P1 |
| `OT-008` | Rainfall-derived weather affects river levels, health, progress and events; exact encounter probabilities and seed are not established by the printed model. | Confirmed | Direct | High | P1 |
| `OT-009` | The home H-106 booklet gives the banker $2500, so its starting economy is not identical to A-157. | Confirmed | Direct | High | P1, P2 |

## Basic data

- Release / origin: Minnesota Educational Computing Corporation, 1985,
  school courseware disk A-157 for Apple II-family 64K systems.
- Platform or physical form: Apple II computer, `PLAT-APPLE-II`.
- Mechanical family: ordered dependency sequencing (`FAM-017`); provisions,
  daily condition and a viable crossing must line up before the next leg.
- **[P1]** [MECC, original A-157 instructional
  booklet](https://mirrors.apple2.org.za/ftp.apple.asimov.net/images/educational/mecc/documentation/MECC-A157%20The%20Oregon%20Trail%20manual.pdf),
  `Program Preview` pp. 6–12 and `Summary of the Underlying Model` pp. 35–36,
  accessed 2026-09-25. This is the primary school-edition rules and model
  evidence, not a claim that its 1985 historical representation is neutral.
- **[P2]** [MECC, H-106 home instruction
  booklet](https://mirrors.apple2.org.za/ftp.apple.asimov.net/images/educational/mecc/documentation/oregon_trail/The%20Oregon%20Trail.pdf),
  July 1985, pp. 3–8, accessed 2026-09-25, used only for stable cross-edition
  features and to audit budget divergence, never to override A-157.
- **[S1]** [ASchultz, Apple II game
  guide](https://gamefaqs.gamespot.com/appleii/579985-the-oregon-trail/faqs/9660),
  retrospective written route, accessed 2026-09-25, corroborating the
  first Kansas crossing and trade-offs. Its suggested grueling/bare-bones
  strategy is an opinion, not a mandated rule.

## Mechanical decomposition

### Action Genes

- New `ACT-538`: set persistent pace and daily ration policies from their
  three legal levels. The pair is independently editable but defines one
  expedition-policy control surface; exact labels and rates are parameters.
- New `ACT-539`: at a river, choose ford, caulk-and-float, eligible ferry or
  wait for a later condition. A method is a committed crossing decision, not
  merely an ordinary movement input.
- New `ACT-540`: spend ammunition and a travel day on the optional aimed
  hunting subtask to replenish carried food, subject to actual prey and the
  carryback cap.
- New `ACT-541`: offer eligible carried goods in an on-trail barter attempt;
  an accepted exchange changes the outfit and costs a day.

### System Behaviour Genes

- Existing `SYS-004`: weather/event and hunting outcomes have variable
  selection not chosen by the player; no exact probability is asserted.
- New `SYS-1075`: settle travel-day mileage from pace, oxen, health, terrain
  and obstructing weather; reached river/landmark distance advances the route.
- New `SYS-1076`: consume rationed food and update party health, illness and
  injury each day under current rest, pace and weather. A rest day can improve
  health but still spends time and provisions.
- New `SYS-1077`: resolve a selected river method against current width,
  depth, swiftness and costs, either reaching the far bank or applying a
  bounded accident/loss response. Ferry, float and ford have different risk
  and time/cash envelopes.
- New `SYS-1078`: resolve hunting aim and prey into meat credited to the
  wagon, capped at 100 pounds for that day, after ammunition/time costs.

### Constraint Genes

- New `CON-695`: the party needs remaining people and usable resources to
  continue; fatal deterioration of the full party before the far bank is
  failure. Zero food or a damaged part is not automatically an immediate
  terminal; the printed model resolves consequences over subsequent days.

### Information Genes

- New `INF-400`: status and trail map expose current date, weather, party
  health, food and next-landmark distance; the Kansas screen exposes river
  width/depth and offered methods. Future rainfall, accidents and trade or
  prey outcomes are not previewed.

### Objective Genes

- New `OBJ-236`: bring the continuing wagon party across the first named
  river to the next traversable leg, not merely to its near bank or to the
  game's final Oregon destination.

### Time Genes

- New `TIM-029`: planning menus wait for the player, while each travel,
  rest, hunt, trade or river decision advances a stated number of simulated
  days and applies daily state resolution before the next decision.

## Reproducible transitions

| Before | Action | Bounded resolution | Establishes | Claim |
|---|---|---|---|---|
| Independence menu after a legal outfit | choose `Continue` at steady/filling | calendar and mileage advance, food is consumed and health/weather are updated | day-priced travel | `OT-002`–`OT-004` |
| Same starting state | switch to grueling and bare bones before continuing | potential daily mileage rises and daily food spend falls, but health/ox risk rises; exact event draw is not fixed | policy trade-off | `OT-002`–`OT-004` |
| Low food before Kansas | hunt one day and hit game | at most 100 pounds return regardless of heavier prey; ammunition and one day are spent | limited field resupply | `OT-005` |
| Damaged health with food remaining | rest several days | travel stops, time/food are spent and health may improve; events remain possible | recovery costs | `OT-004` |
| Kansas screen shows depth and width | choose eligible ferry with cash | $5 and possibly up to six wait days are spent, then lower but nonzero accident risk settles | method-specific river cost | `OT-006`, `OT-007` |
| Kansas screen shows a deep river | attempt ford | wagon may swamp and goods/people can be lost; far bank is not guaranteed | condition-specific hazard | `OT-006`, `OT-007` |
| Kansas crossing succeeds with survivors | leave near-bank state | far-bank next leg becomes available and this scoped packet ends | positive terminal | `OT-006` |

## Edge-case audit

- A-157 and H-106 share much of the route but not the banker's starting money;
  this record selects A-157. Farmer's $400 is its starting-budget parameter.
- A river accident may cost supplies, a person or time while leaving the game
  playable. Do not equate every swamp with complete-game failure.
- Waiting can change rainfall-driven depth; it is not a free reroll because
  days and provisions pass. A ferry is only offered under suitable water
  conditions and cash availability.
- Health is party-wide and individual illness/injury is separate. A member
  already sick or injured can die under a further bad draw, but the precise
  random sequence is not promised for an uninspected disk.
- Hunting's 100-pound cap applies to meat carried back, not the visible
  animal's estimated weight. A miss may still spend the day and ammunition.
- The first river is Kansas; the later Snake guide option, Dalles raft and
  endgame score multiplier cannot be transferred into this interval.

## Strategic and experiential structure

- Local decision: compare current food/health and weather with the miles to
  Kansas, then set pace and rations or spend a day on recovery/provisioning.
- Medium-term planning: preserve oxen and enough food to arrive at the river
  with an affordable and risk-tolerable crossing choice.
- Failure attribution: shortage, illness and river loss are distinct. The
  status screen shows present constraints, not the next weather/event draw.

## Replay and variation

- Different weather, sickness and trade/hunt outcomes can change when the
  party reaches Kansas and how high the water is. The exact distributions
  are not asserted by this source-bounded reconstruction.
- A deliberate short first leg can be compared across policy choices without
  pretending that crossing Kansas completes the 2,000-mile game.

## Adjacent systems and history

- *The Long Dark* shares resource and condition pressure but resolves a
  first-person, live survival route rather than a menu-priced daily wagon
  simulation with multiple party members and river methods.
- *Mount & Blade II: Bannerlord* reuses food-over-campaign-time, but its
  combat-party recovery does not cover Oregon's coupled weather, ration,
  illness and ox-pace model.
- This is the 1985 graphical school edition A-157, not the original 1970s
  text program and not evidence for later PC remakes.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-538`–`ACT-541` | pace/ration labels, ferry choice, hunt aim, barter offer |
| System Behaviour | `SYS-004`, `SYS-1075`–`SYS-1078` | weather distribution, daily model, river risk, meat cap |
| Constraint | `CON-695` | party/outfit survival condition |
| Information | `INF-400` | present status and river measurements |
| Objective | `OBJ-236` | first Kansas far bank |
| Time | `TIM-029` | choice-paced daily advance |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `401` (`GAME-0001`–`GAME-0401`).
- Exact genome matches: none.
- Tied near matches: `GAME-0067` — Simon (`1 / 20 = 0.050000`).
- Supported combination subsets: none.
- Scan date: 2026-09-25.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0067` — Simon | `SYS-004` | Both include an outcome not chosen by the player. Simon appends an unseen random light cue to a retained sequence and tests exact recall; Oregon uses weather and encounter variability while the player manages persistent food, health, wagon pace and a measured river crossing. The lone overlap is generic randomness, not a shared journey or memory loop. | Tied near, `0.050000` |

## Taxonomy impact

- Registry changes: twelve Active genes, `ACT-538`–`ACT-541`,
  `SYS-1075`–`SYS-1078`, `CON-695`, `INF-400`, `OBJ-236`, `TIM-029`.
- Taxonomy-change record:
  [`TAXONOMY_CHANGE_140`](../../../research/taxonomy-changes/TAXONOMY_CHANGE_140.md).
- Candidate terms affected: daily travel policy, hunt/barter resupply,
  weather-and-health progression, condition-sensitive river crossing and
  first-leg arrival.

## Negative results

- None: no earlier signature or verified combination is revised.

## Delta summary

## New facts

- [Confirmed | Direct | High] A-157's first river is Kansas; its school
  starting economy differs from the H-106 home booklet (`OT-001`, `OT-009`).

## New genes

- [Confirmed | Direct | High] Twelve boundaries retain the policy and
  day-priced expedition cycle rather than turn every named river or item
  into a gene.

## New combinations

- [Observation | Corroborated | High] No new combination proposed.

## Taxonomy changes

- [Confirmed | Direct | High] `TAXONOMY_CHANGE_140` adds twelve bounded
  genes without changing an earlier signature.

## New questions

- Which exact A-157 disk revision and random-seed trace reproduce the
  printed model's simultaneous illness, weather and crossing transitions?

## Next recommended game

- [Hypothesis | Limited | Medium] `GAME-0403` *Luigi's Mansion*.
- Optimisation criterion: replace daily resource and river planning with
  light-and-vacuum room capture on GameCube.
- Expected information gain: distinguish a real-time exposure/capture chain
  from choice-paced expedition risk.
- Backlog impact: no selected subject displaced.

## Why this game

- [Hypothesis | Limited | Medium] The culturally familiar journey tests
  whether the Atlas can isolate a short, reproducible interval without
  conflating it with full Oregon arrival or importing later edition rules.
