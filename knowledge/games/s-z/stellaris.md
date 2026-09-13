---
game_id: GAME-0287
slug: stellaris
game_title: Stellaris
analysis_status: reviewed
reviewed: 2026-09-10
combination_ids:
  - COMB-0273
gene_ids:
  action:
    - ACT-006
    - ACT-121
    - ACT-189
    - ACT-316
  system:
    - SYS-004
    - SYS-154
    - SYS-551
    - SYS-564
    - SYS-843
    - SYS-844
    - SYS-845
  constraint:
    - CON-225
    - CON-417
    - CON-626
    - CON-627
  information:
    - INF-081
    - INF-224
  objective:
    - OBJ-170
  time:
    - TIM-003
---

# Game: Stellaris

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Runtime names and
quantities parameterise the genes but do not enter their canonical labels.

## Analysis scope

- Version / ruleset: current unmodified English Windows Steam application
  `281990`, base package `38760`, default-public Build ID `24109497`, observed
  2026-09-09. Paradox's current stable release is Stellaris `4.4.6` `Pegasus`,
  checksum `fdde`; its publication window coincides with the observed public
  build, but Valve does not author a semantic build-to-version mapping. The
  separately selectable `4.5` beta is not admitted.
- Entry: start one fresh single-player United Nations of Earth empire in a
  Small galaxy on default `Ensign` difficulty with tutorial disabled, Ironman
  off, no mods and no separately sold DLC enabled. Select the three initial
  research targets at first control.
- Primary decision loop: read the generated hyperlane graph, known system and
  planet properties, empire stockpiles, monthly income/upkeep, ship selection,
  task progress, research channels and production state; adjust simulation
  speed or pause; command the starting science ship to explore and fully survey
  connected systems; choose a surveyed connected system containing an eligible
  habitable planet; pay the legal outpost costs and command the construction
  ship to build it; commission one colony ship from the home starbase shipyard;
  send it to the eligible owned habitat; advance the pausable simulation until
  colonisation settles into an established colony.
- Positive terminal: the first off-origin colony reaches its established
  successor state and the same empire remains available for continued control.
  Planet, system, research offers, costs, travel duration, colonisation duration
  and calendar date are run-time parameters.
- Negative terminal: none is invented. This bounded fresh single-player packet
  has no authored loss settlement or fixed deadline before the first colony.
  A bad choice may delay the terminal or require a different surveyed target,
  but delay is not itself a canonical failure state.
- Included: generated Small-galaxy topology; three selected and independently
  advancing research channels; manual science-, construction- and colony-ship
  orders; system survey as persistent knowledge; monthly empire resource
  settlement; one paid outpost and its resulting territorial ownership; one
  site-bound colony-ship production order; colonisation legality, development
  and the first established-colony successor; strategic map and command-state
  disclosure; pause and speed controls.
- Excluded: the in-game tutorial and its task chain; saving, loading and any
  reload-verification claim; multiplayer and cooperative play; custom empires;
  mods; subscription and separately sold DLC; the separately selectable beta;
  anomalies, archaeology, optional events, leaders and council optimisation;
  diplomacy, federations, espionage, war and ship combat; planetary development
  after establishment; later colonies, sectors, ascension, crises, victory and
  the wider campaign. Content incorporated into the base product by Paradox's
  2026 migration remains part of the installed base product but does not widen
  this route.
- Reproducible parameterisation: use the English Windows public branch and base
  package `38760`; disable the tutorial, Ironman, mods and separately sold DLC;
  choose the stock United Nations of Earth, Small galaxy and default `Ensign`.
  Keep manual control of the starting ships. Survey connected systems until an
  eligible habitable target is found, choose one fully surveyed connected
  target, construct its outpost, build one colony ship at the home shipyard and
  colonise that owned habitat. The generated map and offered technologies vary,
  but the transition predicates and terminal do not.
- Potential scoped modules: one current tutorial route, one anomaly chain, one
  diplomatic agreement, one war, one separately sold expansion mechanic, one
  multiplayer session or one crisis each requires its own current build,
  entry, decision loop and reproducible terminal.
- Direct-play status: not conducted. The current application was not installed
  and no local or Steam Cloud save was available. Valve metadata establishes
  lawful product delivery; Paradox material establishes the current stable
  version, stock empire, science- and construction-ship roles, base-product
  migration and the established-colony successor. Current and historical
  written references constrain the exact survey, outpost, shipyard and
  colonisation predicates. This is an evidence-backed rules reconstruction,
  not a claimed captured playthrough or reload. No video or audio was opened,
  played, heard or analysed.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `ST-001` | The admitted product is Paradox Development Studio's Windows Stellaris app `281990`, delivered alone by base package `38760` | Confirmed | Direct | High | P1, P2 |
| `ST-002` | The default public branch projects Build ID `24109497`; Paradox names the current stable release `4.4.6` `Pegasus`, checksum `fdde`, while `4.5` remains separately selectable beta material | Observation | Corroborated | High | P3, S1 |
| `ST-003` | Paradox incorporated named older expansions into the base product in 2026 without making the separately sold catalogue part of this packet | Confirmed | Direct | High | P4, P5 |
| `ST-004` | United Nations of Earth is a stock human polity with the Prosperous Unification origin | Confirmed | Direct | High | P6 |
| `ST-005` | A fresh galaxy is procedurally generated; Small and Ensign are fixed setup parameters in this packet | Observation | Corroborated | Medium | P7, S2 |
| `ST-006` | The player selects three simultaneous research targets and the channels progress independently over simulation time | Observation | Corroborated | High | P3, S3 |
| `ST-007` | A science ship can explore connected systems and survey their bodies into persistent system knowledge | Confirmed | Corroborated | High | P7, P8, S3 |
| `ST-008` | A territorial outpost order requires a surveyed unowned target, an eligible construction ship and payable resources; completion creates owned system territory | Observation | Corroborated | High | P7, S3, S4 |
| `ST-009` | Empire income and upkeep settle into visible stockpiles on the running monthly simulation clock | Observation | Corroborated | High | P3, S3 |
| `ST-010` | An eligible owned starbase shipyard accepts and advances a paid colony-ship production order | Observation | Corroborated | High | P7, S3, S5 |
| `ST-011` | Colonisation begins only at an eligible uncolonised habitat in owned territory with a compatible founding transport and population | Observation | Corroborated | High | P9, S3, S5 |
| `ST-012` | A committed colony transport is consumed into development and the colony later becomes established when its founding requirement is met | Confirmed | Corroborated | High | P9, S5 |
| `ST-013` | The strategic map and command surfaces expose discovered systems, planets, stockpiles, selected ships, orders, production and research progress before the next commitment | Observation | Corroborated | High | P7–P9, S3 |
| `ST-014` | The selected packet has no authored failure settlement or fixed pre-colony deadline | Observation | Limited | Medium | S3, S5 |
| `ST-015` | No current executable or save was available, so saving, loading and the tutorial chain cannot be claimed as executed evidence | Confirmed | Direct | High | R1 |
| `ST-016` | Amendment 002 supersedes only the tutorial-on and reload-verified clauses of the original selection | Confirmed | Direct | High | R2 |

## Basic data

- Release / origin: Paradox Development Studio / Paradox Interactive, May 2016.
- Platform or physical form: lawfully available English Windows Steam
  distribution, application `281990`, base package `38760`; no local
  entitlement or direct execution is claimed.
- Puzzle family: generated-network exploration, strategic resource scheduling,
  agent routing and ordered territorial-settlement dependencies.
- Primary and official sources, accessed 2026-09-09:
  - `P1` — [Steam product](https://store.steampowered.com/app/281990/Stellaris/),
    for title, developer, publisher, Windows availability and single-player
    delivery.
  - `P2` — [Valve package metadata](https://store.steampowered.com/api/packagedetails?packageids=38760&cc=ua&l=english),
    for base package `38760` containing application `281990`.
  - `P3` — [Official Stellaris announcements](https://store.steampowered.com/news/posts/?appgroupname=Stellaris&appids=281990&enddate=1783435441&feed=steam_community_announcements),
    for `4.4.6` `Pegasus`, checksum `fdde`, current stable fixes and the
    separation of later beta material.
  - `P4` — [Paradox, base-game update](https://www.paradoxinteractive.com/games/stellaris/news/an-update-on-stellaris-base-game),
    for the announced 2026 base-product migration.
  - `P5` — [Official 4.3.6 notes](https://store.steampowered.com/news/posts/?appgroupname=Stellaris&appids=281990&enddate=1778487355&feed=steam_community_announcements),
    for the shipped base-product migration.
  - `P6` — [Paradox, United Nations of Earth](https://www.paradoxinteractive.com/games/stellaris/stellaris-quiz/stellaris-discover-your-galactic-empire/galactic-empire-united-nations-of-earth),
    for the stock empire and origin.
  - `P7` — [Paradox, Stellaris overview](https://www.paradoxinteractive.com/games/stellaris/about),
    for procedural galaxies, science-ship surveying, construction ships and
    stations.
  - `P8` — [Paradox, Galactic Paragons available now](https://www.paradoxinteractive.com/games/stellaris/news/galactic-paragons-available-now),
    for the distinct Explore Systems and Survey Systems science-ship tasks.
  - `P9` — [Official colonisation update](https://store.steampowered.com/news/posts/?appids=281990&enddate=1741942821&feed=steam_community_announcements),
    for colonisation development and the established-colony successor.
- Corroborating textual sources, accessed 2026-09-09:
  - `S1` — [SteamCMD public-branch projection](https://api.steamcmd.net/v1/info/281990),
    for Build ID `24109497` and its branch timestamp.
  - `S2` — [Stellaris Wiki, galaxy settings](https://stellaris.fandom.com/wiki/Galaxy_settings),
    for the named Small and Ensign setup fields; exact star count and bonus
    values are not admitted as canonical facts because the accessible revision
    was not independently tied to `4.4.6`.
  - `S3` — [Stellaris Wiki, beginner's guide](https://stellaris.fandom.com/wiki/Beginner%27s_guide),
    for the present-tense research, survey, outpost, economy and early expansion
    sequence.
  - `S4` — [Steam Community, outpost discussion](https://steamcommunity.com/app/281990/discussions/0/4203492762819065496/),
    for the surveyed-system predicate and distance-sensitive construction
    observation only.
  - `S5` — [Stellaris Wiki, colonization](https://stellaris.fandom.com/wiki/Colonization),
    for owned-system eligibility, colony-ship commitment and establishment
    details not fully enumerated in current publisher prose.
- Research records:
  - `R1` — local preflight on 2026-09-09, which found no installed app, local
    save or accessible Steam Cloud save.
  - `R2` — [`SEARCH_DEMAND_GAME_SELECTION_017_AMENDMENT_002`](../../../research/selection/SEARCH_DEMAND_GAME_SELECTION_017_AMENDMENT_002.md),
    accepted by the maintainer on 2026-09-09.
- Claim IDs: `ST-001`–`ST-016`.

## Mechanical decomposition

### Action Genes

- Existing `ACT-006`: select a faster simulation rate when the next route state
  should resolve sooner; pausing and the chosen multiplier are parameters.
- Generalised `ACT-121`: choose one active technology target in each of the
  three parallel research channels. A channel assignment and a queued target
  are parameters of the same commitment.
- Existing `ACT-189`: select the science, construction or colony ship and issue
  its legal destination or task-bearing world-target order for autonomous
  pathing and resolution.
- Existing `ACT-316`: add one colony ship to the finite production channel of
  the eligible home starbase shipyard.
- Rejected `ACT-096`: it selects one reachable navigation point for the
  player's direct travel, whereas these orders address independently selected
  ships and include survey, construction and colonisation tasks. Rejected
  `ACT-149`: it assigns staffed colony research, not unstaffed polity-wide
  channels. Claims: `ST-006`–`ST-013`.

### System Behaviour Genes

- Existing `SYS-004`: generate a galaxy whose stars, connections and planet
  opportunities can vary between fresh entries.
- Generalised `SYS-154`: each recurring monthly settlement credits empire
  income, debits upkeep and updates the corresponding stockpiles.
- Existing `SYS-551`: the selected starbase shipyard advances the paid colony
  ship at the front of its production channel and releases it on completion.
- Generalised `SYS-564`: the three occupied research channels advance their
  selected technologies independently and apply completed effects.
- New `SYS-843`: the science ship's completed system survey converts unknown
  bodies into persistent inspectable system knowledge.
- New `SYS-844`: the construction ship's completed outpost project creates a
  persistent owned station and assigns the surveyed system to the empire.
- New `SYS-845`: the committed colony transport develops over time into an
  established persistent settlement.
- Resolution order: generate the fresh empire and map; accept three research
  targets; integrate the running strategic clock and monthly budget; path and
  settle survey tasks; test and pay outpost legality; complete ownership;
  accept and advance colony-ship production; test colonisation legality;
  consume the transport into development; settle the established colony.
- Rejected `SYS-236`: it requires a declared repeatable setup seed, while this
  setup exposes no seed as part of its reproducible contract. Rejected
  `SYS-159`: it consumes laboratory items into one queue, not three independent
  empire channels. Rejected `SYS-194`: no staffed research station owns these
  channels. Rejected `SYS-287`: its single shuffled research queue and mixed
  point stock differ from simultaneous fields. Rejected `SYS-297`: its compound
  RTS pathing and repeated combat acquisition exceed the non-combat packet.
  Rejected `SYS-481`: its city founding immediately claims territory, whereas
  the colony develops only after a separate outpost has already claimed the
  system. Claims: `ST-005`–`ST-012`.

### Constraint Genes

- Existing `CON-225`: outpost commitment requires enough currently available
  influence; material cost remains a separate parameter of general production
  affordability.
- Generalised `CON-417`: the home starbase shipyard must be owned, eligible and
  able to pay the colony ship's current resource, facility and capacity costs.
- New `CON-626`: outpost construction requires a fully surveyed unowned target,
  an eligible constructor and payable costs. The chosen route uses a connected
  target, but distance is a cost parameter rather than a false universal
  adjacency ban.
- New `CON-627`: colonisation requires an uncolonised eligible habitat in an
  owned system plus a compatible founding population and colony transport.
- Rejected `CON-410`: its per-turn hex movement allowance and zone-of-control
  predicates do not describe real-time ship tasks. No one-off numeric influence,
  alloy, habitability or founding threshold enters a gene label. Claims:
  `ST-008`–`ST-012`.

### Information Genes

- Existing `INF-081`: the discovered star map exposes known connections,
  systems, planet properties and survey-revealed resource observations before
  the target system is selected.
- Generalised `INF-224`: the strategic command view exposes empire stockpiles,
  selected ships, their orders, current research and shipyard production state
  before the next commitment.
- Rejected `INF-184`: it describes explored turn-grid cells and current hex
  visibility, not persistent survey knowledge on a generated stellar network.
  Rejected `INF-229`: its compound national-focus, manpower, factory and fuel
  dashboard exceeds this route. Claims: `ST-007`–`ST-013`.

### Objective Genes

- New `OBJ-170`: complete one survey → claim → transport → settlement chain
  away from the home world and reach the retained first established-colony
  state while the empire remains controllable.
- Rejected `OBJ-093`: it is an entire rival-facing civilization victory ending
  in a Mars project. Rejected `OBJ-169`: that objective crosses the first
  threshold of one still-unfinished subject; here the new colony itself crosses
  from development into an established settlement and the wider polity, not
  the settlement subject, continues. Claims: `ST-011`–`ST-016`.

### Time Genes

- Existing `TIM-003`: research, travel, survey, monthly accounting, production,
  construction and colonisation advance on the real-time simulation clock while
  the player may issue commands; pause and speed are rate controls.
- Rejected a separate monthly Time gene: monthly settlement is the interval
  parameter of `SYS-154` under the same pausable simulation clock. Claims:
  `ST-006`–`ST-014`.

## Reproducible transitions

| Before | Action | Deterministic or bounded resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Fresh United Nations of Earth entry exposes three uncommitted research fields | Select one reachable technology in each field | Each choice becomes that channel's active target and independently receives subsequent progress | parallel research commitment | `ST-006` |
| A connected system is not yet fully known | Select the science ship and issue explore or survey orders | The ship paths to required bodies; completed survey persists their system and resource knowledge | task-bearing order becomes knowledge | `ST-007` |
| A surveyed unowned connected system contains the chosen habitable planet | Select the construction ship and order an outpost | If constructor, survey and costs are legal, the project advances; completion creates the owned outpost and territorial system | knowledge and payment precede ownership | `ST-008` |
| The monthly clock advances while income and upkeep sources exist | Allow the next accounting interval to settle | Declared income is credited, upkeep debited and visible empire stockpiles change | recurring budget state | `ST-009`, `ST-013` |
| The owned home starbase has an eligible shipyard and payable colony-ship order | Queue one colony ship | The site-bound channel advances and releases the finished transport | paid production differs from colonisation | `ST-010` |
| The new transport and an uncolonised suitable planet in the owned system are available | Issue the colonise order | Eligibility is checked; the transport reaches the target and is committed into colony development | transport becomes founding state | `ST-011`, `ST-012` |
| The first off-origin colony is still developing | Advance the pausable simulation | The founding measure increases until the establishment predicate is satisfied | progress remains non-terminal below threshold | `ST-012` |
| The founding requirement is fulfilled | Allow colony settlement | Development converts into an established persistent colony and the same empire remains controllable | positive terminal | `ST-012`, `ST-016` |
| Any earlier route state is merely delayed or inefficient | Continue, redirect or wait | No authored failure report settles solely because the first colony has not yet been established | no invented failure terminal | `ST-014` |

## Strategic and experiential structure

The bounded problem is not “play a grand-strategy campaign.” It is a dependency
graph with one uncertain spatial choice. Surveying spends time to turn unknown
systems into decision-quality knowledge. The selected colony system then must
be claimed by a different mobile agent before a third, site-produced carrier
can legally convert one planet into an established settlement. Research and the
monthly economy keep advancing during those choices, so pausing or accelerating
changes decision pressure without changing the route's terminal rule.

The three ships are not interchangeable skins: the science ship produces
knowledge, the construction ship produces territorial ownership and the colony
ship is produced at a site before being consumed into settlement development.
Keeping those transitions separate prevents a quest-like “found first colony”
mega-gene and exposes the portable survey → claim → settle structure.

## Replay and variation

A fresh procedural galaxy changes the available systems, hyperlane routes,
planet properties, research offers, resource observations, costs and calendar
timing. The route remains reproducible because it fixes the product, stock
empire, size, difficulty, excluded content, action sequence and terminal
predicate rather than a particular star or planet name. No setup seed is
claimed, so `SYS-236` is not admitted.

## Adjacent systems and history

Stellaris shares real-time command-and-production grammar with Command & Conquer
and parallel strategic research with Hearts of Iron IV, but its packet places
both inside a generated knowledge-to-territory-to-settlement chain. It shares a
star map and random galaxy with Dyson Sphere Program, but not factory placement,
logistics or player-avatar spaceflight. Civilization VI also selects research
and gates production, yet its city founding and turn clock do not match a
separate outpost claim followed by time-bearing colony development.

## Normalised genome

`ACT-006 + ACT-121 + ACT-189 + ACT-316 + SYS-004 + SYS-154 + SYS-551 +
SYS-564 + SYS-843 + SYS-844 + SYS-845 + CON-225 + CON-417 + CON-626 +
CON-627 + INF-081 + INF-224 + OBJ-170 + TIM-003`

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `286` (`GAME-0001`–`GAME-0286`).
- Exact genome matches: none.
- Tied near matches: `GAME-0179` — Age of Empires II: Definitive Edition (`7 / 41 = 0.170732`).
- Supported combination subsets: `COMB-0273`.
- Scan date: 2026-09-10.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0179` — Age of Empires II: Definitive Edition | `ACT-121`, `ACT-189`, `ACT-316`, `SYS-004`, `SYS-551`, `INF-224`, `TIM-003` | Both select research, command remote units, queue units at a live site, expose strategic state and advance through a generated real-time field. Age of Empires II turns those genes into staffed resource gathering, construction, formation combat and Conquest. Stellaris instead adds persistent whole-system survey, paid neutral territorial ownership and transport-to-colony development, with no combat in the packet. | Near, `7 / 41 = 0.170732` |

The shared seven-gene spine is real but small. The score reports reusable
strategic command grammar without treating the generated land map, hostile
economy and Conquest objective as equivalents of a survey-to-colony chain.

## Preserved research notes

- The official material is strong for product identity, current release,
  procedural scope, science/construction roles, stock empire and the distinction
  between colony development and establishment.
- Current official prose does not enumerate every survey, outpost and
  colonisation UI predicate. Those clauses remain corroborated observations and
  use no exact costs or durations.
- The public Build ID is a secondary distribution observation. It is not
  represented as a publisher-authored semantic-version mapping.
- Saving and loading exist in the product, but no executed save or reload is
  claimed. The accepted amendment removes both from this packet.
- No video or audio evidence was used.

## Taxonomy impact

- `TAXONOMY_CHANGE_055` generalises five lower-ID carrier-bound labels or
  definitions without changing any earlier signature: `ACT-121`, `SYS-154`,
  `SYS-564`, `CON-417` and `INF-224`.
- Six new portable genes are required: `SYS-843`, `SYS-844`, `SYS-845`,
  `CON-626`, `CON-627` and `OBJ-170`.
- New `COMB-0273` records the strict survey → ownership → transport → first
  established-colony interaction. It omits generic time, budget, research,
  random generation and broad display support.
- No prior game signature, lifecycle, combination membership or family
  assignment changes.

## Negative results

- Lower-ID Action scan rejected `ACT-096` and `ACT-149`; `ACT-121`, `ACT-189`
  and `ACT-316` already own the transferable commitments.
- Lower-ID System scan rejected `SYS-159`, `SYS-194`, `SYS-236`, `SYS-287`,
  `SYS-297` and `SYS-481`; their resource, staff, seed, queue, combat or
  instant-founding boundaries differ materially.
- Lower-ID Constraint scan rejected `CON-410`; `CON-225` and generalised
  `CON-417` are reused, while territory and colonisation need separate new
  predicates.
- Lower-ID Information scan rejected `INF-184` and compound `INF-229`;
  `INF-081` and generalised `INF-224` cover the disclosed state.
- Lower-ID Objective scan rejected `OBJ-093` and `OBJ-169`; neither has the
  first-established-colony retained successor.
- Combination subset scan found no existing Verified combination that is a
  strict subset of this 19-gene signature. `COMB-0273` is new and itself a
  strict 12-gene subset.
- Tutorial genes `SYS-736` and `INF-268`, all save/load genes and every combat,
  diplomacy, anomaly, leader or post-establishment gene are excluded by scope.

## Delta summary

- New facts: one lawful current base-product identity; one current stable
  release boundary; one fixed fresh stock-empire packet; eight reproducible
  transitions; one retained first-colony terminal; one explicit no-failure and
  no-direct-play boundary.
- Reused genes: `13` — `ACT-006`, `ACT-121`, `ACT-189`, `ACT-316`, `SYS-004`,
  `SYS-154`, `SYS-551`, `SYS-564`, `CON-225`, `CON-417`, `INF-081`, `INF-224`
  and `TIM-003`.
- New genes: `6` — `SYS-843`, `SYS-844`, `SYS-845`, `CON-626`, `CON-627` and
  `OBJ-170`.
- New combinations: `1` — `COMB-0273`.
- Taxonomy changes: `1` — `TAXONOMY_CHANGE_055`.
- Ukrainian review: repeated genes verified; all five generalised and six new
  records corrected in the same unit; product names, identifiers, checksums and
  version strings retained with reason.

## New facts

- One generated stellar network can make knowledge acquisition an explicit
  prerequisite to territorial construction rather than merely reveal scenery.
- One mobile construction project can claim territory before a distinct
  produced transport is consumed into settlement.
- The first established settlement is a bounded positive terminal even though
  the polity and campaign continue indefinitely.

## New genes

- `SYS-843` — Resolve a ship survey into persistent system knowledge.
- `SYS-844` — Complete an outpost into territorial system ownership.
- `SYS-845` — Develop a committed colony transport into an established
  settlement.
- `CON-626` — Territorial construction requires a surveyed unowned system and
  eligible constructor.
- `CON-627` — Colonisation requires an eligible owned habitat and founding
  transport.
- `OBJ-170` — Establish one off-origin colony and regain continuing polity
  control.

## New combinations

- `COMB-0273` — Surveyed stellar expansion into first colony.

## Taxonomy changes

- [`TAXONOMY_CHANGE_055`](../../../research/taxonomy-changes/TAXONOMY_CHANGE_055.md)
  removes carrier nouns from five reusable strategic-management genes.

## New questions

1. When a later packet includes anomalies, should surveying and anomaly
   investigation remain separate System boundaries or form a reusable compound?
2. Does a scoped war route introduce a portable territorial-transfer result
   distinct from paid neutral outpost construction?
3. Can first-contact knowledge be bounded without importing the entire
   diplomacy layer?

## Next recommended game

- `GAME-0288` — Sekiro: Shadows Die Twice - GOTY Edition, using one current
  unmodified base-game opening route with a positive retained checkpoint
  terminal and no whole-game progression claim.

## Why this game

Stellaris tests whether the Atlas can separate remote command syntax from the
meaning of the projects being commanded. Its compact first-colony packet reuses
familiar research, production, budget and information grammar while adding a
new portable sequence: survey creates knowledge, outpost construction creates
territory, a site creates the founding carrier and colonisation consumes that
carrier into a continuing settlement.
