---
game_id: GAME-0269
slug: dredge
game_title: DREDGE
analysis_status: reviewed
reviewed: 2026-09-06
combination_ids:
  - COMB-0267
gene_ids:
  action:
    - ACT-008
    - ACT-219
    - ACT-245
    - ACT-261
    - ACT-341
    - ACT-424
  system:
    - SYS-597
    - SYS-816
  constraint:
    - CON-394
    - CON-612
  information:
    - INF-117
    - INF-326
  objective:
    - OBJ-163
  time:
    - TIM-002
    - TIM-003
---

# Game: DREDGE

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Parameters describe
gene instances but do not enter the signature.

## Analysis scope

- Version / ruleset: current unmodified English Windows Steam application
  `1562430`, base one-app package `824636`, on the sole `public` branch carrying
  build `20206241`, whose branch record was updated 2025-10-03; checked
  2026-09-06. A dated publisher announcement covers exactly that build — the
  2025-10-03 `Update Required` notice describing a security patch — but it
  states no version string, and the publisher's most recent *named* version,
  the 2024-09-18 hotfix `v1.5.3`, predates the build by more than a year. This
  unit therefore asserts no semantic version and identifies the ruleset by the
  sole branch and its build identifier, recording that a covering announcement
  exists but names no version.
- Product boundary: this is the base **DREDGE** application from package
  `824636`, which contains only that app. The `Digital Deluxe Edition` package
  `1114568` and the `Complete Edition` package `1093759` bundle separate DLC
  apps and are outside this packet, as are all five DLC apps `2104240`,
  `2198580`, `2198610`, `2561440` and `2561450`. The application also ships a
  macOS build; this packet uses Windows only.
- Platform, input and difficulty: English interface, Windows, keyboard and
  mouse, a fresh single-player save. The product exposes an adjustable
  difficulty category; this packet uses the default configuration as first
  offered and does not vary it.
- Setup-only predecessors: the opening wreck and the arrival at Greater Marrow,
  and the Mayor's loan of a replacement boat with the debt it carries. These
  are non-interactive or single-choice and establish a clean save only.
- Entry: accept first ordinary control of the loaned boat at the Greater Marrow
  dock on day 1, before leaving the dock and before any catch is taken.
- Primary decision loop: steer the boat out across the sea; approach a patch of
  disturbed water and commit the rod interaction; inside the catch minigame,
  commit the input while the moving indicator overlaps the disclosed zone, so
  the reel advances and a well-timed input yields a larger specimen; take the
  resulting fish into the hold and position and rotate it so its footprint fits
  cells the grid leaves free, respecting that engine, rod and light cells accept
  only their own hardware while cargo may sit on any unused cell; read the
  time-dial, the hold's free space and each fish's freshness together to decide
  whether one more spot is worth the daylight the return will need; sail back to
  Greater Marrow, sell the catch to the Fishmonger for its disclosed value, and
  address the Shipwright.
- Positive terminal: complete the opening commission — at least one fish caught
  this run, stowed in the hold, sold to the Fishmonger while still in its
  undegraded `fresh` condition, and the Shipwright addressed — with the boat
  back at the Greater Marrow dock before the world clock reaches the declared
  night boundary at 18:00 on day 1. Then reload the save and verify the retained
  money, the recorded commission and the day-1 clock position.
- Negative terminal: the world clock passing 18:00 while the boat is still at
  sea, after which darkness begins to raise the panic level; or taking a catch
  for which the hold offers no legal placement. Reaching the dock after the
  boundary, or selling a catch that has already left `fresh`, is not success.
- Included: steering the boat across the sea; the disturbed-water spot and the
  rod interaction that draws one fish from it; the catch minigame's timed input
  and its graded result; placing and rotating the fish inside the hold grid; the
  grid's typed hardware cells and permanently blank cells; the requirement that
  a footprint fit free cells; the world clock advancing only with travel and
  declared actions; the day and night hours declared on that clock; the panic
  level that darkness raises and light and daylight lower, against which the
  return deadline is defined; the freshness bands that reduce a held fish's
  value as the clock advances; selling to the Fishmonger at disclosed prices;
  addressing the Mayor, Fishmonger and Shipwright; and the reload check.
- Excluded: every DLC app and the Deluxe and Complete packages; the macOS build;
  all later regions, characters, pursuits, research and the narrative endings;
  the dredging minigame and buried relics; trawl nets and crab pots; buying or
  installing any equipment, which the commission's Shipwright step only makes
  available; boat damage and repair, which the sources reachable from this
  environment do not describe precisely enough to admit; the aberration
  mutations and their irregular footprints, which the declared route does not
  require; night encounters, obelisks and every panic consequence beyond the
  meter's own rise, since the successful route does not enter them although the
  objective is defined against them; all inputs and platforms not declared
  above; screenshots, official artwork, third-party assets, video and audio
  evidence.
- Reproducible parameterisation: install English app `1562430` from package
  `824636`, confirm the sole `public` branch, and start a fresh save. Pass the
  setup-only predecessors. From first ordinary control at the dock, take at
  least one fish from at least one disturbed-water spot, stow it in the hold by
  a placement the grid accepts, return to Greater Marrow before the clock
  reaches 18:00, sell that fish to the Fishmonger while it reads `fresh`, and
  address the Shipwright. Then perform the stated reload check. Exact species,
  spot positions, minigame form, sale values, elapsed hours and the number of
  fish taken are parameters.
- Potential scoped modules: the dredging minigame and relics; a night voyage and
  its panic consequences; equipment purchase and installation; a later region;
  or a DLC application requires its own version, entry, loop, terminal and
  evidence.
- Direct-play status: not conducted. Valve application and package data plus the
  current Steam product record establish lawful availability, exact product
  identity, Windows and macOS support, the three packages and which apps each
  contains, the `Adventure` and `RPG` genres with no Early Access marker, the
  single-player-only mode with an adjustable difficulty category, and the five
  separate DLC apps. The Valve news endpoint establishes the 2025-10-03
  announcement covering the current build and the absence of any version string
  in it, together with `v1.5.3` as the most recent publisher-named version. The
  public SteamCMD info projection supplies the sole branch and its build and
  timestamp. A design article written by a programmer and co-designer at the
  developer supplies the cargo grid's dimensions, its unusable corner cells, its
  engine, fishing-equipment and light cell regions, item rotation and the rule
  that cargo may sit on unused attachment cells. The community-maintained
  product wiki, reached directly, corroborates the disturbed-water spots, the
  catch minigame forms and their disclosed zones, the trophy result of a
  well-timed input, the freshness bands and their value fractions, what raises
  and lowers panic and what high panic produces, the actions that advance the
  clock, the declared day and night hours, and the opening commission's three
  steps. This is an evidence-backed rules reconstruction, not a claimed
  playthrough or entitlement. No video or audio was opened, played, heard,
  analysed or used.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `DRG-001` | Steam app `1562430` and its base one-app package `824636` identify the currently lawfully offered English Windows product, alongside two bundle packages and five separate DLC apps | Confirmed | Direct | High | P1, P2 |
| `DRG-002` | The sole `public` branch carries build `20206241`, whose branch record was updated 2025-10-03 | Observation | Limited | Medium | S1 |
| `DRG-003` | A dated publisher announcement of 2025-10-03 covers that build but states no version string, and the most recent publisher-named version is the 2024-09-18 hotfix `v1.5.3` | Observation | Direct | High | P3 |
| `DRG-004` | The boat's inventory is a 7 × 9 grid with unusable blank corner cells, engine cells at the bottom, fishing-equipment cells at the sides and light cells at the top | Observation | Direct | High | S2 |
| `DRG-005` | Items occupy several cells, may be rotated, and cargo may be placed anywhere including over empty attachment cells | Observation | Direct | High | S2 |
| `DRG-006` | Fishing spots are visible patches of disturbed water the boat approaches | Observation | Corroborated | High | S3 |
| `DRG-007` | The catch minigame advances a meter and offers disclosed green zones on a moving indicator; committing the input inside one advances the reel much faster | Observation | Corroborated | High | S4 |
| `DRG-008` | An occasional golden zone yields a larger, more valuable specimen when the input lands inside it | Observation | Corroborated | High | S4 |
| `DRG-009` | Time advances only when the player moves, fishes or takes a specific action that declares a waiting cost | Observation | Corroborated | High | S5 |
| `DRG-010` | The time-dial shows the weekday, the day number since the save began and the hour on a twenty-four-hour clock; the day begins at 6:00 and night at 18:00 | Observation | Corroborated | High | S5 |
| `DRG-011` | Panic rises while the boat is in darkness at night and falls in good lighting, during the day and on resting at a town | Observation | Corroborated | High | S6 |
| `DRG-012` | High panic distorts the display and makes further hostiles and mirages present | Observation | Corroborated | High | S6 |
| `DRG-013` | A fish is worth its full value while `fresh`, a reduced fraction while `stale` and a much smaller fraction once `rotting` | Observation | Corroborated | High | S3 |
| `DRG-014` | The opening commission is completed by catching fish, selling them to the Fishmonger and meeting the Shipwright, with no required quantity or sum | Observation | Corroborated | High | S7 |
| `DRG-015` | The bounded identity is one round trip in which the same clock funds the catching and the return, while the grid decides how much may be brought back and the freshness bands decide what the delay leaves it worth | Strong Pattern | Corroborated | High | `DRG-004`–`DRG-014` |

## Basic data

- Release / origin: Black Salt Games; published by Team17 and released
  2023-03-30.
- Platform or physical form: lawfully offered English Windows single-player
  Steam application `1562430`; one fresh first-day route from the Greater Marrow
  dock to a completed opening commission.
- Puzzle family: spatial assembly and packing; real-time system pressure;
  inventory and fixture dependencies.
- Primary and official sources, accessed 2026-09-06:
  - **[P1]** [Valve application data](https://store.steampowered.com/api/appdetails?appids=1562430&cc=ua&l=english),
    for the exact title, app, Windows and macOS support, developer and
    publisher, release date, the `Adventure` and `RPG` genres with no Early
    Access marker, the single-player-only mode with an adjustable difficulty
    category, the five DLC apps, the three packages and the current Ukraine
    offer.
  - **[P2]** [Valve package data](https://store.steampowered.com/api/packagedetails?packageids=824636&cc=ua&l=english),
    for base package `824636` containing only app `1562430` and its current
    Ukraine offer, against which the Deluxe and Complete packages were checked
    and excluded.
  - **[P3]** [Valve news endpoint for this application](https://api.steampowered.com/ISteamNews/GetNewsForApp/v2/?appid=1562430&count=25&feeds=steam_community_announcements),
    for the complete publisher announcement list, the 2025-10-03 `Update
    Required` notice that covers the current build without naming a version, and
    the 2024-09-18 `v1.5.3` hotfix as the most recent named version.
- Corroborating textual sources, accessed 2026-09-06:
  - **[S1]** [public SteamCMD info projection](https://api.steamcmd.net/v1/info/1562430),
    for the sole `public` branch, its build `20206241` and its update timestamp.
    This mirrors Valve's public product data and is treated as a secondary
    distribution observation, not a publisher claim.
  - **[S2]** [developer design article on this product's spatial inventory](https://www.gamedeveloper.com/design/deep-dive-the-surprising-depth-of-spatial-inventories-in-dredge),
    written by a programmer and co-designer at the developer, for the 7 × 9
    grid, the unusable blank corner cells, the engine cells at the bottom, the
    fishing-equipment cells at the sides, the light cells at the top, item
    rotation and the rule that cargo may be placed over empty attachment cells.
  - **[S3]** [community product wiki, Fish](https://dredge.wiki.gg/wiki/Fish),
    for the disturbed-water spots, the equipment that gates each species and the
    freshness bands with their value fractions.
  - **[S4]** [community product wiki, Minigames](https://dredge.wiki.gg/wiki/Minigames),
    for the catch minigame forms, their disclosed zones, the faster reel that a
    correctly timed input produces and the larger specimen a golden zone yields.
  - **[S5]** [community product wiki, Time](https://dredge.wiki.gg/wiki/Time),
    for time advancing only on movement, fishing and specific waiting actions,
    the time-dial's weekday, day number and twenty-four-hour reading, and the
    6:00 and 18:00 boundaries.
  - **[S6]** [community product wiki, Panic](https://dredge.wiki.gg/wiki/Panic),
    for panic rising in darkness at night, falling in good lighting, during the
    day and on resting at a town, and for the display distortion and additional
    hostiles and mirages that high panic produces.
  - **[S7]** [community product wiki, A Fresh Start](https://dredge.wiki.gg/wiki/A_Fresh_Start),
    for the opening commission's three steps and its completion without a
    required quantity or sum.
- Reproducible control: **[V1]** repository-side transition trace across
  `P1`–`P3` and `S1`–`S7` under the declared app, package, branch, build,
  platform, input, clean save, exclusions and terminal; rules reasoning, not
  direct play.
- Claim IDs: `DRG-001`–`DRG-015`. No audiovisual evidence was used.

## Mechanical decomposition

### Action Genes

- Existing `ACT-008`: steer the boat, one persistent controllable agent, across
  the sea's traversable geometry. `ACT-392` was rejected because its boundary
  requires throttle and three-axis attitude in open three-dimensional space,
  while this carrier has a heading on one surface; `ACT-201` was rejected
  because it requires entering and leaving a vehicle seat, and this boat is
  never left. A different carrier is a parameter, not a new action.
- Existing `ACT-245`: address one reachable disturbed-water spot and draw one
  finite yield from it into carried inventory.
- Existing `ACT-261`: commit the rod input while the moving indicator overlaps
  the disclosed zone, producing a graded result that ranges from an ordinary
  catch to a larger specimen. The Dead by Daylight boundary already covers one
  response committed against a moving pointer inside a disclosed interval for a
  graded result, so the several minigame forms this product presents are
  parameters of that boundary rather than separate actions.
- Existing `ACT-424`: position and rotate the caught fish inside the bounded
  carried grid until its footprint fits cells the grid leaves free. The Resident
  Evil 4 boundary already covers exactly this manipulation; a fish rather than a
  weapon is a parameter.
- Existing `ACT-219`: sell one owned fish through the Fishmonger's available
  sale operation for its disclosed return.
- Existing `ACT-341`: address the Mayor, the Fishmonger and the Shipwright as
  reachable authored objects and commit their currently legal interactions.
- Species, spot positions, minigame form, sale values and elapsed hours remain
  parameters. Claims: `DRG-004`–`DRG-014`.

### System Behaviour Genes

- New `SYS-816`: one shared world clock governs the day and its declared night
  boundary but advances only in proportion to the player's own travel and to the
  actions that declare a time cost, so standing still costs nothing. No existing
  time or system gene describes a clock the player alone advances: `TIM-003`
  requires forced progression, `TIM-014` runs a shift clock regardless of the
  player, `SYS-091` advances every unit one step per action irrespective of the
  action's size, and `SYS-416` and `SYS-595` describe what a running calendar
  changes rather than what moves it.
- `SYS-592` was originally reused here and is removed by
  [`TAXONOMY_CHANGE_027`](../../../research/taxonomy-changes/TAXONOMY_CHANGE_027.md).
  That gene's transition is a mental-state meter whose *low thresholds* alter
  perception and eventually make shadow entities physically hostile. This
  packet's declared scope excludes every night encounter and every panic
  consequence beyond the meter's rise, and its route never reaches those
  thresholds, so the defining half of the boundary is neither executed nor
  verified here. `BATCH_015_GENE_AUDIT_001` finding `A-04` is upheld: causal
  relevance to the terminal does not waive a gene's own transition.
- No narrower pressure gene replaces it. A lower-ID scan over every Active
  System gene mentioning sanity, stress, panic, fear, morale, a rising meter or
  exposure found `SYS-190`, `SYS-198`, `SYS-226`, `SYS-311`, `SYS-321`,
  `SYS-327`, `SYS-338`, `SYS-593` and `SYS-621`, each of which resolves the
  meter into a consequence this route excludes. What the route actually uses is
  a deadline: return before the boundary hour. That is already carried by
  `SYS-816`, which advances the clock, `CON-612` and `OBJ-163`, which define the
  terminal against it. A gene whose entire admitted content is "a number starts
  moving, with no consequence inside the packet" would not be a decision-bearing
  transition, so none is created.
- Existing `SYS-597`: a carried fish loses freshness as the clock advances and
  crosses declared states that reduce its value. The same boundary already
  covers perishable carried goods crossing freshness states that alter their
  value; that the elapsed time here is spent rather than imposed is a parameter
  supplied by `SYS-816`.
- Resolution order: an input to move or to fish advances the clock by that
  action's cost; the clock's position selects the day or night state; carried
  fish age against the same clock and
  cross their freshness states; a completed catch is offered to the grid, which
  accepts or refuses the placement; and a sale reads the fish's current
  freshness state to compute its return. Claims: `DRG-004`–`DRG-013`.

### Constraint Genes

- Existing `CON-394`: a fish enters carried state only where its footprint fits
  unoccupied grid cells.
- New `CON-612`: the same grid holds installed hardware and cargo; its cells are
  typed by hardware class and some are permanently unusable, so hardware may be
  installed only on free cells of its own type while cargo may occupy any free
  cell including unused typed cells. `CON-394` treats equipment as a separate
  matching slot and `CON-284` treats capacity as bulk plus class slots; neither
  states that capability and payload compete for one surface. `CON-062` governs
  static machine footprints against terrain and ports, not a carried grid.
- Scarce resources: the grid's free cells, the hours of daylight left on the
  clock, each fish's remaining freshness, and the money the sale returns. Exact
  values are parameters. Claims: `DRG-004`, `DRG-005`, `DRG-009`, `DRG-013`.

### Information Genes

- Existing `INF-117`: the Fishmonger's offered prices and the player's current
  money are inspectable before a sale is committed.
- New `INF-326`: the interface exposes the clock's current position, the grid's
  remaining free space and the condition of what is already carried at the same
  time, so a further catch can be priced against the daylight the return needs
  and against the value the delay removes from the rest. `INF-240` couples a
  survival meter set to a clock but carries a cooperative partner's state and no
  carried-capacity measure; `INF-128` and `INF-138` expose inventory
  compatibility and value without a clock; `INF-324` exposes a projected path.
  A split-first review for `BATCH_015_GENE_AUDIT_001` finding `A-12` compared
  each of the three values against the full lower-ID Information registry.
  `INF-136` exposes a calendar with survival infrastructure but no carried
  condition; `INF-157` exposes a hunt clock with a faint allowance and a
  monster's condition, not a capacity measure; `INF-075` exposes personal
  capacity and equipment wear without a clock; `INF-189` exposes trade capacity
  and route yields without either. `INF-116`, `INF-224`, `INF-236`, `INF-254`
  and `INF-290` are the reviewed precedent that one bounded interface surface
  exposing the small set of values a single decision loop is priced against is
  one Information gene rather than several. The three values here are that
  surface, so the gene is retained and only its novelty wording was corrected,
  from "the three values are only useful together" to a statement of what the
  surface does.
- Exact dial art, cell rendering and freshness iconography are presentation
  parameters. Claims: `DRG-010`, `DRG-013`.

### Objective Genes

- New `OBJ-163`: complete the attempt by taking material from the field, stowing
  it legally in the carried grid, returning it to the fixed buyer and selling it
  undegraded, with the whole round trip finished before the clock crosses its
  declared night boundary. `OBJ-096` settles one employer-supplied cargo
  delivery whose load is given rather than gathered, `OBJ-014` and `OBJ-023`
  credit delivery without a condition or a deadline of this kind, and `OBJ-002`
  maximises an accumulation this objective deliberately does not require.
- Reaching the dock after the boundary, or selling a catch that has already left
  `fresh`, is not success. Claims: `DRG-013`–`DRG-015`.

### Time Genes

- Existing `TIM-002`: while the boat is stationary and no timed action is
  running, the world waits; the player may pack the hold, read the dial and
  choose the next heading without any time-driven system step.
- Existing `TIM-003`: while the boat is under way and while the catch minigame
  runs, the decision state advances on a real-time schedule and input remains
  accepted throughout.
- The packet therefore carries two time structures, and which one is live is
  decided by whether the player is currently spending the clock; that spending
  rule is owned by `SYS-816` rather than by either time gene. Claims:
  `DRG-007`, `DRG-009`.

## Reproducible transitions

| Before | Action | Deterministic or bounded resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| A fresh save has completed only the setup-only predecessors | Accept ordinary control at the Greater Marrow dock | The run begins on day 1 with an empty hold and the loaned boat | fixed clean entry | `DRG-001`, `DRG-014` |
| The boat is stationary and no timed action runs | Wait without input | The time-dial does not move | player-spent clock | `DRG-009` |
| The boat is at the dock | Steer out to sea | The dial advances as the boat travels | travel spends the day | `DRG-009`, `DRG-010` |
| A patch of disturbed water is reached | Commit the rod interaction | The catch minigame opens with its meter and its disclosed zones | field source | `DRG-006`, `DRG-007` |
| The indicator is inside a disclosed zone | Commit the input | The reel advances much faster than it otherwise would | graded timing | `DRG-007` |
| An occasional golden zone is present | Commit the input inside it | The resulting specimen is larger and worth more | graded result | `DRG-008` |
| A fish has been caught and the hold has free cells | Place and rotate it | The placement is accepted where the footprint fits free cells and refused where it does not | grid legality | `DRG-004`, `DRG-005` |
| A hardware item is held and its typed cells are free | Install it on a cell of another type | The installation is refused, while a fish placed on that same unused cell is accepted | shared typed surface | `DRG-004`, `DRG-005` |
| A fish has been held while the clock advanced | Inspect it | Its condition has left `fresh` and its value has fallen to the corresponding fraction | freshness cost | `DRG-013` |
| The clock reaches 18:00 while the boat is at sea | Continue | The declared boundary hour has passed and the positive terminal is no longer available for this attempt | declared boundary | `DRG-010`, `DRG-014` |
| The boat is at the dock before 18:00 with a fresh catch | Sell to the Fishmonger | The disclosed value is paid in full and the hold empties | undegraded return | `DRG-013`, `DRG-014` |
| The commission's three steps have been completed before the boundary | Reload the save | The same money, recorded commission and day-1 clock position return | reproducible positive terminal | `DRG-014`, `DRG-015` |

## Strategic and experiential structure

- Planning horizon: the hours left before 18:00, the cells left in the hold and
  the freshness already spent decide how far out the next spot may be and
  whether the return still pays.
- Local tactics: take the near spot rather than the rich far one when the dial
  is late; place each fish against an edge so the remaining free cells stay
  contiguous; treat unused hardware cells as usable space, accepting that a
  later engine will take them back.
- Medium-term structure: the run is a single circuit whose profit is decided
  before the last catch, because every further catch is paid for twice — once in
  cells and once in the daylight that the whole hold's freshness is spent
  against.
- Reversible versus irreversible: a placement may be undone freely while the
  boat is still; a spent hour and a lost freshness band cannot be recovered, and
  a sale is final.
- Failure attribution: the dial, the free cells and the freshness states are all
  visible before each decision, so a thin return traces to a specific spot taken
  too late rather than to an unseen rule.
- Player trust: standing still is genuinely free, the grid refuses an illegal
  placement rather than silently discarding a catch, and the reloaded save shows
  the money the circuit actually earned.

## Replay and variation

- What changes: which spots are near the dock, which species they hold, which
  minigame form each catch presents, how many hours the circuit costs and how
  many fish the hold accepts.
- Randomness or procedural generation: the archipelago, its towns, its spot
  positions and its species tables are authored. The minigame form and whether a
  golden zone appears vary; no procedural-generation claim enters this packet.
- Multiple strategies: the circuit admits one distant rich spot, several near
  poor ones, or an early return with a part-full hold. The control demonstrates
  the smallest sufficient circuit rather than making a full hold the terminal.
- Typical replay motive: complete the same circuit with more cells filled, or
  with an hour still left on the dial when the sale is made.

## Adjacent systems and history

- Undertale is the selected near neighbour on the shared substrate alone: both
  advance one persistent controlled agent through authored space, address
  authored objects, commit a timed input inside a disclosed interval for a
  graded result, and run in real time during that input. Undertale's packet is
  one encounter with two alternating regimes; this packet is a round trip whose
  pressure is a clock the player themselves spends.
- Don't Starve Together shares the perishable-goods boundary exactly, and its
  own world clock runs whether the survivor acts or not. That difference is what
  makes this product's clock a new gene rather than a re-description. Its
  mental-state meter is no longer shared: `SYS-592` requires threshold
  consequences this packet's route excludes, so `TAXONOMY_CHANGE_027` removed
  that reuse.
- Resident Evil 4 (2023 remake) shares the carried-grid manipulation and the
  footprint legality, but its grid is only a container: nothing in it decays, and
  no clock is spent to reach it.
- American Truck Simulator shares returning a load to a fixed receiver under a
  clock, but its cargo is supplied rather than gathered, its load has no spatial
  form and its clock runs on its own.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-219`, `ACT-245`, `ACT-261`, `ACT-341`, `ACT-424` | species, spot positions, minigame form and sale values are parameters |
| System Behaviour | `SYS-597`, `SYS-816` | travel-to-time rate, freshness fractions and thresholds are parameters |
| Constraint | `CON-394`, `CON-612` | grid dimensions, blank cells, hardware classes and footprints are parameters |
| Information | `INF-117`, `INF-326` | dial art, cell rendering and freshness iconography are parameters |
| Objective | `OBJ-163` | buyer identity, boundary hour and the named characters are parameters |
| Time | `TIM-002`, `TIM-003` | docked pacing and minigame timing are implementation |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `268` (`GAME-0001`–`GAME-0268`).
- Exact genome matches: none.
- Tied near matches: `GAME-0224` — Once Human (`3 / 26 = 0.115385`); `GAME-0228` — A Way Out (`3 / 26 = 0.115385`).
- Supported combination subsets: `COMB-0267`.
- Scan date: 2026-09-06.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0224` — Once Human | `ACT-008`, `ACT-341`, `TIM-003` | Both advance one persistent controlled agent through authored space, address authored world objects and accept input while the state advances in real time. Once Human spends that substrate on a tutorial route through a hostile open world, where the pressure is the world's own creatures and the decisions are combat and contextual interaction. This packet spends it on a self-paced round trip whose only clock is the one the player advances by moving, whose carried goods lose value while that clock runs, and whose grid decides how much may come back. The shared core is the traversal substrate alone. | Near, `0.115385` |
| `GAME-0228` — A Way Out | `ACT-008`, `ACT-341`, `TIM-003` | The same three genes, and the same reason: both move a controlled character through authored space and address authored objects in real time. A Way Out coordinates two simultaneously controlled characters against observation windows, so its decisions are about timing an action while another player watches. This packet has one carrier, no observer, and a tempo the player sets by travelling. The tie with `GAME-0224` at the same score is itself the result: after `TAXONOMY_CHANGE_027` and `TAXONOMY_CHANGE_031` this genome has no strong neighbour left in the corpus, which is a distinctness signal rather than a thin decomposition. | Near, `0.115385` |

### Preserved research notes

- New genes: `SYS-816`, `CON-612`, `INF-326`, `OBJ-163`.
- Reused genes: `ACT-008`, `ACT-219`, `ACT-245`, `ACT-261`, `ACT-341`,
  `ACT-424`, `SYS-597`, `CON-394`, `INF-117`, `TIM-002`, `TIM-003`.
  `SYS-592` was reused at integration and removed by `TAXONOMY_CHANGE_027`.
- Classification result: `New gene`.
- Lower-ID scan: this unit's selection asked whether spatial cargo packing
  coupled to a day-cycle pressure meter is a genuine interaction or two
  already-reviewed structures sharing a product. The scan answers it directly:
  both halves are already reviewed and were reused rather than duplicated —
  `ACT-424` and `CON-394` from Resident Evil 4 for the grid and `SYS-597` from
  Don't Starve Together for the perishable cargo — and what is new is the joint,
  not either half. The mental-state half was reused as `SYS-592` at integration
  and later removed, because this route neither executes nor verifies that
  gene's threshold transition. Reject `ACT-392` and `ACT-201`
  for the boat, `ACT-312` because a fish here is drawn from a spot rather than
  reached for directly, `CON-284` and `CON-062` for the grid, `INF-240`,
  `INF-128` and `INF-138` for the disclosure, `OBJ-096`, `OBJ-014`, `OBJ-023`
  and `OBJ-002` for the objective, and `SYS-416`, `SYS-595`, `SYS-091` and
  `TIM-014` for the clock. Reject a fish-, species-, town-, character- or
  region-named gene.

## Taxonomy impact

- Registry changes: add `SYS-816`, `CON-612`, `INF-326`, `OBJ-163` and
  `COMB-0267`, plus independent evidence for eleven reused genes.
- Taxonomy-change record:
  [`TAXONOMY_CHANGE_027`](../../../research/taxonomy-changes/TAXONOMY_CHANGE_027.md)
  removed the `SYS-592` reuse from this signature, which falls from sixteen
  genes to fifteen. No gene definition or lifecycle changed and `GAME-0186`
  keeps `SYS-592` unchanged; `COMB-0267` never contained it and is unaffected.
  `INF-326` was reviewed split-first under finding `A-12` and retained, with
  only its novelty wording corrected.
- Candidate terms: recorded in `CANDIDATE_TERMS.md`; all product, character,
  species, town, region, app, package and build names remain parameters.

## Negative results

- No video or audio evidence was used; only official product data, the Valve
  news endpoint, a developer-authored design article and a community-maintained
  product wiki support this packet.
- No semantic version is asserted, and this is a fourth distinct version
  situation for the batch. A dated publisher announcement covers exactly the
  current build, but it names no version; the most recent publisher-named
  version predates the build by more than a year. This differs from
  `GAME-0265` and `GAME-0266`, where a named version existed but predated the
  branch update, from `GAME-0267`, where the name and the date agreed exactly,
  and from `GAME-0268`, where no announcement covered the build at all.
- Boat damage and its effect on the grid are excluded as a bounded evidence
  gap. The reachable sources describe repair as a Shipwright service without
  stating what damage does to individual cells, so the packet does not admit a
  rule it cannot cite.
- The aberration mutations and their irregular footprints are excluded because
  the declared route does not require one, and their appearance is not
  reproducible from the declared entry.
- The panic thresholds, every night encounter and the meter itself are excluded
  from the genome. The route's deadline is carried by `SYS-816`, `CON-612` and
  `OBJ-163`, which advance and bound the clock; the meter's onset is a signal of
  that boundary rather than an admitted transition, and `SYS-592`'s own
  threshold behaviour is neither executed nor verified here. This is a recorded
  scope limit, not a claim that the meter or its consequences do not exist.
- The dredging minigame, trawl nets and crab pots are excluded because the
  opening commission requires none of them.

## Delta summary

## New facts

- [Observation | Corroborated | High] `DRG-001`–`DRG-015`: one round trip in
  which the same clock funds both the catching and the return, the grid decides
  how much may be brought back, and the freshness bands decide what the delay
  leaves it worth.

## New genes

- [Observation | Corroborated | High] `SYS-816`, `CON-612`, `INF-326`,
  `OBJ-163` — a world clock the player alone advances, one grid whose typed
  cells make capability and payload compete for a surface, the joint disclosure
  of clock, free space and cargo condition, and a round trip that must close
  before a declared hour.

## New combinations

- [Strong Pattern | Corroborated | High] `COMB-0267` — a gathering circuit in
  which space, elapsed time and cargo value are one decision.

## Taxonomy changes

- [Observation | Direct | High] No taxonomy changes; no split, merge,
  deprecation, lifecycle change, wording generalisation or earlier signature
  change.

## New questions

- Does a second product reuse `SYS-816`, or is a clock advanced only by the
  player's own travel specific to this voyage model?

## Next recommended game

- [Hypothesis | Limited | High] `GAME-0270` — Risk of Rain 2.
- Optimisation criterion: leave the economy corridor and test whether a run
  whose difficulty rises with elapsed time, rather than with progress, is a
  distinct system boundary.
- Expected information gain: the falsifiable question the selection recorded for
  this subject.
- Backlog impact: advances the recorded 261-to-270 horizon by one unit and
  closes it.

## Why this game

- [Hypothesis | Limited | High] The selection asked whether spatial cargo
  packing coupled to a day-cycle pressure meter is a genuine interaction or two
  already-reviewed structures sharing a product. The completed decomposition
  answers it in a way neither option anticipated: both halves are already
  reviewed and were reused unchanged, but they are not merely adjacent, because
  the perishable-cargo boundary makes every hour spent packing or sailing
  subtract from the value of what is already held. The interaction is real; what
  is new is the clock the player spends, the surface that capability and payload
  share, and the circuit that must close before an hour.
