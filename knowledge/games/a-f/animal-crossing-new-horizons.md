---
game_id: GAME-0320
slug: animal-crossing-new-horizons
game_title: "Animal Crossing: New Horizons"
analysis_status: reviewed
reviewed: 2026-09-20
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-091
    - ACT-123
    - ACT-139
    - ACT-199
    - ACT-341
    - ACT-476
    - ACT-477
  system:
    - SYS-223
    - SYS-921
    - SYS-922
    - SYS-923
  constraint:
    - CON-297
    - CON-649
  information:
    - INF-128
    - INF-132
    - INF-136
    - INF-352
  objective:
    - OBJ-187
  time:
    - TIM-013
    - TIM-025
---

# Game: Animal Crossing: New Horizons

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). The island layout,
hemisphere, season, clock time and encountered species are run parameters rather
than separate genes.

## Analysis scope

- Version / ruleset: current English original Nintendo Switch base game,
  version `3.0.3`, checked 2026-09-20. This is not Nintendo Switch 2 Edition.
  The packet uses a fresh Northern Hemisphere island, an ordinary unmodified
  system clock and no time travel.
- Structured analysis target: original Nintendo Switch digital base game; see
  `GAME-0320` in
  [`knowledge/platforms/games.json`](../../platforms/games.json).
- Primary decision loop: after the first-night prologue, take Tom Nook's DIY
  workshop, gather tree branches, craft a flimsy fishing rod and flimsy net,
  use their different timing and targeting rules to catch five distinct fish
  or bug species, hand each new species to Tom Nook, place the supplied
  Blathers Tent Marker on a valid island footprint, cross the real next-day
  boundary, then enter the occupied tent and receive the shovel and vaulting
  pole DIY recipes from Blathers.
- Entry: the first ordinary control on the first full real-time island day,
  after the avatar wakes from the introductory sleep and receives the NookPhone,
  before accepting the DIY workshop or making a catching tool.
- Positive terminal: on the following calendar day, ordinary control resumes
  after speaking with Blathers inside his tent and receiving the shovel and
  vaulting pole DIY recipes; the chosen service site remains occupied.
- Negative terminal: there is no ordinary fail state inside the peaceful
  packet. Broken flimsy tools and unavailable species are recoverable through
  more gathering, crafting, waiting or searching. Deleting or abandoning the
  island before the next-day result leaves the declared terminal unreached.
- Included: direct movement; local branch pickup; Resident Services workbench;
  recipe and ingredient visibility; crafting the flimsy rod and net; durability
  loss and breakage; fish shadows, line casting, bite cues and reeling; visible
  insects and net swings; species-specific seasonal, time and habitat
  availability; carried catches and Critterpedia identity; five distinct
  hand-ins; Blathers Tent Marker award and legal placement; real-world clock
  persistence; next-day occupancy; Blathers dialogue and two received recipes.
- Excluded: tent placement and bonfire prologue; house construction, Nook Miles
  debt and mortgage; the later fifteen donations; construction of the full
  museum; Nook's Cranny; fossils, diving and sea creatures; visitors, local or
  online multiplayer; island tours; terraforming; Happy Home Paradise; Hotel
  content from update 3.0; Nintendo Switch 2 Edition features; later facilities,
  residents and complete Critterpedia or museum collection.
- Reproducible parameterisation: create a new Northern Hemisphere island while
  the console clock is correct; finish the tent/bonfire prologue and sleep;
  stop at first control after the NookPhone handoff. Complete the DIY workshop,
  collect enough branches, craft both flimsy tools, catch and hand Tom Nook
  five species not previously handed in, place the resulting tent marker on
  any legal footprint, close or suspend normally without changing the clock,
  return after the next calendar day begins, enter Blathers' tent and accept
  both recipes. Exact island seed, weather, species, tool order and site are
  bounded run parameters.
- Potential scoped modules: the fifteen-donation museum construction, full
  first-week Resident Services progression, seasonal collection, multiplayer,
  3.0 Hotel and Switch 2 Edition each require a separate evidence boundary.
- Direct-play status: not conducted. No Switch, account session, installed
  build, island save, controller trace, screenshot, video or audio was opened
  or analysed. Nintendo's product, update, beginner and creation pages establish
  current identity and invariant gathering/crafting/calendar rules; three
  independent written routes establish the exact five-species, marker and
  next-day Blathers sequence. This is a source-bounded reconstruction.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `ACNH-001` | The current original-Switch base game is version 3.0.3 and remains distinct from Nintendo Switch 2 Edition | Confirmed | Direct | High | P1, P2 |
| `ACNH-002` | After the introductory sleep, the first full island day follows real-world time and begins with the NookPhone | Confirmed | Direct | High | P3, P5 |
| `ACNH-003` | Tom Nook's DIY workshop teaches recipe use; gathered branches can be turned into the flimsy rod and net at a workbench | Observation | Corroborated | High | P3, P4, S1 |
| `ACNH-004` | Fish require a cast near a shadow and a reel after the bite cue, while insects require a reachable timed net swing | Observation | Corroborated | High | P3, S1, S2 |
| `ACNH-005` | Available fish and insects depend on current time, season, hemisphere and local habitat | Confirmed | Direct | High | P2, P3 |
| `ACNH-006` | Tool use consumes durability and a broken flimsy tool can be replaced by gathering and crafting | Observation | Corroborated | High | P4, S1 |
| `ACNH-007` | Tom Nook counts five different donated fish or bug species, rejecting duplicate species as new progress | Observation | Corroborated | High | S1, S2, S3 |
| `ACNH-008` | The fifth accepted species causes Tom Nook to provide Blathers' tent marker for player-chosen legal placement | Observation | Corroborated | High | S1, S2, S3 |
| `ACNH-009` | Blathers occupies that site on the following calendar day and provides shovel and vaulting-pole DIY recipes | Observation | Corroborated | High | S2, S3 |
| `ACNH-010` | The bounded identity joins real-calendar ecology, tool-specific capture, distinct-species invitation and delayed service-site occupancy | Strong Pattern | Corroborated | High | `ACNH-002`–`ACNH-009` |

## Basic data

- Release / origin: Nintendo published Animal Crossing: New Horizons for
  Nintendo Switch on 2020-03-20; Nintendo's support page lists version 3.0.3
  on 2026-04-29 for both the original game and Switch 2 Edition.
- Platform or physical form: original Nintendo Switch digital base game,
  English interface, fresh solo island, current version 3.0.3.
- Puzzle family: inventory and fixture dependencies; ordered dependency
  sequencing; knowledge and evidence progression.
- Primary and official sources, accessed 2026-09-20:
  - **[P1]** [Nintendo update
    history](https://en-americas-support.nintendo.com/app/answers/detail/a_id/49112),
    for current version 3.0.3, release date and applicable editions.
  - **[P2]** [Nintendo product
    page](https://www.nintendo.com/us/store/products/animal-crossing-new-horizons-switch/),
    for original-Switch identity, release date, real-time seasons, gathering,
    fishing, bugs, Blathers and the museum premise.
  - **[P3]** [Nintendo beginner
    guide](https://www.nintendo.com/jp/ichikara/acbaa/index_en.html), for the
    first sleep/day boundary, NookPhone, real-time clock, fishing cues, bug
    catching and Tom Nook's interest in creatures.
  - **[P4]** [Nintendo creation
    guide](https://animalcrossing.nintendo.com/new-horizons/create/), for
    gathering resources, learning recipes, workbench use and crafting.
  - **[P5]** [Nintendo 3.0 update
    page](https://animalcrossing.nintendo.com/new-horizons/update-3-0/), for the
    current original-game content line and separation from Switch 2 Edition.
- Corroborating textual sources, accessed 2026-09-20:
  - **[S1]** [Thonky first-day
    route](https://www.thonky.com/animal-crossing-new-horizons/your-first-day),
    for the DIY workshop, tools, breakage, distinct creature hand-ins and the
    fifth-species tent-marker result.
  - **[S2]** [GameSpot museum
    route](https://www.gamespot.com/articles/how-to-unlock-and-upgrade-the-museum-in-animal-cro/1100-6474994/),
    for five different fish or bugs, marker placement, next-day arrival and
    the shovel/vaulting-pole recipes.
  - **[S3]** [Nintendo Life museum
    route](https://www.nintendolife.com/guides/animal-crossing-new-horizons-blathers-how-to-unlock-the-museum),
    for the same five-species, placed-tent and next-day Blathers sequence.
- Research record: **[R1]** local preflight on 2026-09-20 found no installed
  current client, console session, island save or input trace. No audiovisual
  evidence was used.
- Claim IDs: `ACNH-001`–`ACNH-010`.

## Mechanical decomposition

### Action Genes

- Existing `ACT-008`: directly walk the avatar among trees, water, insects,
  Resident Services, Tom Nook and the chosen facility site.
- Existing `ACT-199`: pick one reachable loose branch or compatible catch into
  carried inventory.
- Existing `ACT-341`: use the reachable workbench whose current state opens the
  known-recipe crafting operation.
- Existing `ACT-123`: select and craft the known flimsy fishing rod or net from
  available branches under the current recipe and station context.
- New `ACT-476`: cast the held rod toward one reachable fish shadow and reel
  only after the float's bite cue.
- New `ACT-477`: swing the held net through one reachable visible insect's
  current world position.
- Existing `ACT-091`: transfer one carried new-species specimen to Tom Nook's
  current creature request.
- Existing `ACT-139`: commit the supplied Blathers Tent Marker to one compatible
  island footprint, reserving that location for the service building.
- Claims: `ACNH-003`, `ACNH-004`, `ACNH-007`, `ACNH-008`.

### System Behaviour Genes

- New `SYS-921`: derive currently available fish and insect instances from
  species rules, hemisphere, calendar season, time and local habitat.
- New `SYS-922`: resolve a legal line reel or net contact into one carried
  species specimen and persistent caught-species record.
- Existing `SYS-223`: successful and compatible uses consume the flimsy tool's
  durability; exhaustion removes the tool and leaves the recipe route available.
- New `SYS-923`: retain the set of distinct eligible species handed to Tom Nook
  and issue one Blathers Tent Marker exactly when its size reaches five.
- Resolution order: calendar/habitat admits organisms; a tool-specific action
  tests one target; successful capture credits identity and inventory; hand-in
  removes the specimen and may extend the distinct set; the fifth addition
  creates the marker; legal placement schedules occupancy. Claims:
  `ACNH-004`–`ACNH-009`.

### Constraint Genes

- Existing `CON-297`: each tool craft requires its learned recipe, enough
  branches, the workbench context and output capacity.
- New `CON-649`: invitation progress accepts only an eligible species not
  already represented in Tom Nook's retained five-species set; duplicates do
  not satisfy another slot.
- Tool reach, water edge, insect position, inventory capacity and legal tent
  footprint are parameters. Claims: `ACNH-003`, `ACNH-007`, `ACNH-008`.

### Information Genes

- Existing `INF-128`: loose branches, carried materials, tools and compatible
  inventory state are visible before gathering or crafting.
- Existing `INF-132`: known recipes expose the ingredients, workbench context
  and resulting tool before the craft is committed.
- Existing `INF-136`: the island presentation and NookPhone expose current date,
  time, weather and season without revealing every future organism.
- New `INF-352`: the world and capture feedback expose fish shadows, bobber
  nibbles/bites, insect bodies, caught identity and prior catalogue credit while
  withholding the exact next spawn.
- Claims: `ACNH-002`–`ACNH-007`.

### Objective Genes

- New `OBJ-187`: establish the first invited island service by crafting capture
  tools, handing in five distinct fish/bug species, placing Blathers' site and
  returning after the next-day boundary to receive his two traversal recipes.
- A caught specimen, five catches without hand-in, marker possession or marker
  placement alone is not the terminal. Claim: `ACNH-003`–`ACNH-009`.

### Time Genes

- New `TIM-025`: the persistent island calendar follows the console's real-world
  date and clock across play and absence, changing season, daylight and eligible
  ecology without requiring a player-authored turn.
- Existing `TIM-013`: placing the awarded service-site marker records progress
  now but Blathers occupies it only on the following calendar day.
- Claims: `ACNH-002`, `ACNH-005`, `ACNH-008`, `ACNH-009`.

## Reproducible transitions

| Before | Action | Deterministic or bounded resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| The first-night prologue has ended | Wake and receive the NookPhone | ordinary island time begins under the console's real-world clock | persistent calendar authority | `ACNH-002` |
| The DIY workshop is available | Complete its workbench instruction | tool recipes become known and their ingredient requirements visible | authored knowledge gate before crafting | `ACNH-003` |
| Loose branches are reachable | Pick them up and select a known recipe at the bench | ingredients are consumed and one flimsy capture tool enters inventory | gather-to-craft dependency | `ACNH-003` |
| A fish shadow is in reachable water | Cast, wait through nibbles and reel after the bite cue | correct timing converts the target into a carried identified fish; early or late input does not | line-specific capture | `ACNH-004`, `ACNH-005` |
| A visible insect is within approach range | Swing the held net through its position | accepted overlap converts it into a carried identified insect; a miss leaves it free or lets it escape | net-specific capture | `ACNH-004`, `ACNH-005` |
| A compatible flimsy tool reaches exhaustion | Attempt or finish its eligible use | the tool disappears; known recipe and gatherable inputs keep the route recoverable | durability without packet failure | `ACNH-006` |
| A carried species has not been credited | Hand it to Tom Nook | specimen leaves inventory and its species joins the retained invitation set | distinct evidence accumulation | `ACNH-007` |
| A credited species is offered again | Attempt another hand-in | it cannot add a second invitation slot; another species must be found | duplicate exclusion | `ACNH-007` |
| The fifth distinct species is accepted | Finish Tom Nook's response | one Blathers Tent Marker is issued | threshold-to-site transition | `ACNH-008` |
| The marker is carried | Choose a legal island footprint and place it | the site becomes persistent and Blathers' arrival is scheduled | player-authored facility location | `ACNH-008` |
| The marker site exists before day rollover | Return after the next calendar day begins | Blathers occupies the chosen tent site | real-calendar delayed consequence | `ACNH-009` |
| Blathers is present | Speak with him | shovel and vaulting-pole DIY recipes are received and ordinary control resumes | positive terminal | `ACNH-009` |

## Strategic and experiential structure

- Local decision: search current habitat, choose rod or net, align cast/swing
  timing, replace a broken tool or spend a carried new species on hand-in.
- Medium horizon: diversify catches rather than repeat already credited species
  and choose a future service footprint before committing the marker.
- Long horizon: turn a day-one resource-and-collection loop into one persistent
  island institution whose arrival is governed by the external calendar.
- Reversibility: failed casts, net swings and broken tools are recoverable;
  marker placement persists and the elapsed calendar day cannot be rewound
  within the ordinary no-time-travel scope.
- Failure attribution: recipe/ingredient panels explain craft rejection;
  shadows, float cues and insect position explain capture timing; Tom Nook's
  response distinguishes new from duplicate species; the marker preview
  explains footprint legality.
- Player trust: the route never requires a particular random species, only five
  currently available distinct species from the disclosed fish/bug categories.

## Replay and variation

- Island layout, hemisphere, calendar date, weather, habitat, species and exact
  site change the route, but the five-distinct-species invitation invariant is
  stable.
- Tool order, capture mix and site placement are player choices. The next-day
  occupancy is not accelerated by more catches in this packet.
- Real-world date changes available species, so exact catches are parameters;
  this record does not claim complete spawn tables or probabilities.

## Adjacent systems and history

- *Stardew Valley* also schedules a service change for the next day after a
  collection predicate, but its Boiler Room uses disclosed typed bundle slots.
  Tom Nook accepts any five different eligible fish/bug species and produces a
  freely placed facility marker rather than restoring a fixed service.
- *DREDGE* also uses a fishing action and a clock-sensitive ecology, but its
  first-day decision is cargo-grid packing under a finite workday. Animal
  Crossing separates line and net capture and synchronises a persistent island
  to real-world calendar time without a packet deadline.
- *Grounded* shares gathered-material crafting and workbench dependencies, but
  its first-shelter route spends charged analysis and a survival plan. This
  packet accumulates distinct natural-history evidence into an invited service.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-091`, `ACT-123`, `ACT-139`, `ACT-199`, `ACT-341`, `ACT-476`, `ACT-477` | bindings, branches, tools, species, NPC and site are parameters |
| System Behaviour | `SYS-223`, `SYS-921`–`SYS-923` | durability, spawn table and award object are parameters |
| Constraint | `CON-297`, `CON-649` | recipe costs, duplicate policy and quota are parameters |
| Information | `INF-128`, `INF-132`, `INF-136`, `INF-352` | interface layout, cues and catalogue labels are parameters |
| Objective | `OBJ-187` | five-species quota, site and recipe reward are parameters |
| Time | `TIM-013`, `TIM-025` | hemisphere, clock and rollover are parameters |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `319` (`GAME-0001`–`GAME-0319`).
- Exact genome matches: none.
- Tied near matches: `GAME-0233` — 7 Days to Die (`7 / 42 = 0.166667`).
- Supported combination subsets: none.
- Scan date: 2026-09-20.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0233` — 7 Days to Die | `ACT-008`, `ACT-123`, `ACT-199`, `ACT-341`, `CON-297`, `INF-128`, `INF-132` | Both traverse a local world, gather compatible inventory, inspect recipe dependencies and craft at a contextual fixture. 7 Days to Die uses survival meters, destructive harvesting, structural building, live threats and retained death consequences; Animal Crossing separates rod and net capture, samples peaceful wildlife from the real calendar, counts distinct species and turns the quota into a freely placed next-day service. | Near, `0.166667` |

### Preserved research notes

- New genes: `ACT-476`, `ACT-477`, `SYS-921`–`SYS-923`, `CON-649`, `INF-352`,
  `OBJ-187` and `TIM-025`.
- Classification result: `New gene`; no verified combination is expected.
- Evidence and reasoning: no lower-ID boundary joins two tool-specific wildlife
  captures, a distinct-species invitation quota and a freely placed service
  site that becomes occupied on the real next day.

## Taxonomy impact

- Registry changes: add two Action, three System Behaviour, one Constraint,
  one Information, one Objective and one Time boundary; add Animal Crossing
  support to compatible movement, delivery, crafting, placement, pickup,
  fixture, durability, crafting-gate, inventory, dependency, calendar-state
  and next-day boundaries.
- Taxonomy-change record: none; no existing definition changes.
- Candidate terms affected: NookPhone, Resident Services, Critterpedia,
  Blathers, flimsy fishing rod, flimsy net, hemisphere, species and exact
  island/date values remain product, interface, character, item or run parameters.

## Negative results

- No Switch, installed client, island save, direct play, input trace, screenshot,
  video or audio evidence exists for this unit.
- The exact 3.0.3 installed build was not observed; the official update history
  establishes the current public version, not a local installation.
- Exact durability counts, spawn odds, bite timing, footprint dimensions and
  rollover processing time are not established and remain parameters.
- Third-party routes agree on the five-species/marker/next-day chain, but exact
  transient dialogue and controller labels are not promoted to canonical rules.

## Delta summary

## New facts

- [Confirmed | Direct | High] The first full island day and ecology follow the
  real-world clock in the current original-Switch line (`ACNH-001`–`ACNH-005`).
- [Observation | Corroborated | High] Five distinct species produce a freely
  placed service site occupied on the following day (`ACNH-006`–`ACNH-009`).

## New genes

- [Observation | Corroborated | High] `ACT-476`, `ACT-477`, `SYS-921`–`SYS-923`,
  `CON-649`, `INF-352`, `OBJ-187` and `TIM-025` isolate nine portable boundaries.

## New combinations

- [Observation | Corroborated | High] No new verified combination.

## Taxonomy changes

- [Observation | Corroborated | High] No existing gene boundary changes.

## New questions

- Does the later fifteen-donation museum route reuse the distinct-species quota
  or require a separate persistent public-collection boundary?
- Which rule differences in local/online visitors alter ownership, time and
  facility authority without changing the solo island's core clock?

## Next recommended game

- [Hypothesis | Limited | Medium] `GAME-0321` Gears of War.
- Optimisation criterion: move from peaceful asynchronous collection to a
  bounded Xbox cover-combat route with explicit squad and revival pressure.
- Expected information gain: test cover attachment, blind fire, active reload
  and co-op-shaped solo-squad authority against existing shooter genes.
- Backlog impact: `GAME-0321` remains next; no later unit starts in this commit.

## Why this game

- [Hypothesis | Limited | High] Animal Crossing: New Horizons is a recognisable
  Nintendo anchor whose smallest institution-building loop makes real-calendar
  ecology, distinct evidence and player-placed service progression inspectable.

## Research checklist

- [x] current original-Switch version, hemisphere, clock, entry and terminal declared
- [x] intro, later museum and 3.0/Switch 2 additions excluded
- [x] official invariant rules separated from corroborating exact route sources
- [x] direct-play and audiovisual limitations disclosed
- [x] complete six-type gene scan performed
- [x] deterministic lower-ID comparison and combination scan completed
- [ ] reviewed Ukrainian localisation and bilingual presentation completed
- [ ] original artwork and responsive browser checks completed
