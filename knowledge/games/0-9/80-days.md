---
game_id: GAME-0478
slug: 80-days
game_title: 80 Days
analysis_status: reviewed
reviewed: 2026-10-02
combination_ids: []
gene_ids:
  action:
    - ACT-232
    - ACT-632
  system:
    - SYS-1243
  constraint:
    - CON-742
  information:
    - INF-452
  objective:
    - OBJ-269
  time:
    - TIM-003
---

# Game: 80 Days — the first Paris onward connection

Use the [canonical genome vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Named cities, vehicles, cash amounts and departure times are parameters, not separate genes.

## Analysis scope

- Version / ruleset: the original English-language 31 July 2014 iOS release of inkle's *80 Days*. Later iOS content updates, the expanded 2015 desktop rebuild, Android and Switch editions are excluded. The exact launch binary and device revision were not inspected.
- Structured analysis target: original iOS software (`PLAT-IOS`); see [`knowledge/platforms/games.json`](../../platforms/games.json).
- Primary decision loop: inspect currently known onward connections and their time/cost implications at Paris, weigh the running wager clock against waiting or other city activity, commit an offered departure, and make authored responses during the journey. The chosen service moves Fogg and Passepartout to the next city while consuming its travel time and money; the resulting narrative can alter later information or opportunities. Then inspect the next city rather than assuming the full future route is already known.
- Entry: start a fresh first journey, take the opening London-to-Paris connection and arrive in Paris with at least one offered onward service. London-to-Paris is preparation, not a claim that Paris has a fixed next destination. Exact cash, day, route inventory and update-dependent alternatives are not asserted.
- Exit: arrive at the next city on one chosen, currently offered Paris departure and inspect the new position and elapsed time. This is an analytical checkpoint, **not** victory in the 80-day wager. A complete win requires circumnavigation and return to London inside the target time; a later return may still finish a journey without winning the wager.
- Included: visible current-city route choice, service schedule and cost, the continuing in-game clock, route travel, one consequential authored response if offered, partial knowledge of later connections, and the 80-day wager as the decision-driving long objective.
- Excluded: an exact first-journey timetable or balance, fixed downstream event, guaranteed route unlocked by conversation, trade profit, bank transfers, luggage capacity, Fogg's health or trust, multiplayer feed, particular alternate opening, complete world tour, precise endgame cut-off hour and any post-launch route or city. These are not claims that the complete original game lacks such features.
- Reproducible parameterisation: use a version-pinned original 2014 iOS build; begin a first journey and record its visible London connection, arrival state at Paris, offered departures, fare and time terms, selected service, any consequential story response and the next-city arrival. A future direct trace is required for exact numbers and event text. The source-based conditional procedure here does not invent such a trace.
- Direct-play status: no original iOS binary, phone, save, touch trace, screenshot, video or audio was inspected; no direct play was conducted. Contemporary developer descriptions establish the live clock and route/narrative rules; a contemporaneous first-hand account corroborates the initial Paris arrival. The illustration is original interpretive art, not a screenshot.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `DAYS-001` | The original iOS game launched on 31 July 2014; the 2015 desktop version added cities and is not identical to launch iOS. | Confirmed | Direct | High | P1 |
| `DAYS-002` | The wager asks Fogg and Passepartout to circumnavigate and return to London in 80 days; returning later can finish a journey without winning that wager. | Confirmed | Corroborated | High | P2, P3, S2 |
| `DAYS-003` | The game exposes a globe of connected journeys with different costs, risks and timings; route planning is an active player decision. | Confirmed | Direct | High | P1, P2, P3 |
| `DAYS-004` | The in-game clock continues while a player considers city activity and connections. It is not real-world GPS or physical 1:1 travel. | Confirmed | Direct | High | P1, P4, P5 |
| `DAYS-005` | Authored responses during journeys can have later consequences, and information discovered during encounters can inform a subsequent route. No fixed first-journey event is guaranteed here. | Confirmed | Direct | Medium | P1, P3, P5 |
| `DAYS-006` | An original-launch journey may begin London to Paris; Paris is then a planning stop before the player chooses another connection. Exact availability varies with edition and journey state. | Observation | Corroborated | Medium | P6, S1 |

## Basic data

- Release / origin: inkle's original 2014 iOS interactive travel narrative, not its later enlarged desktop reconstruction.
- Platform or physical form: touch-operated iPhone/iPad software with a globe and authored text choices; no exact 2014 touch target or button wording is asserted.
- Mechanical families: route and network construction (`FAM-005`) for assembling an onward connected itinerary; real-time system pressure (`FAM-010`) for a clock that continues during deliberation.
- **P1:** [inkle, *80 Days* press kit](https://www.inklestudios.com/press/80days/), accessed 2026-10-02; original iOS date, route globe, narrative decisions, continuous clock, later desktop expansion.
- **P2:** [inkle, official game overview](https://www.inklestudios.com/80days/), accessed 2026-10-02; wager, transport network, strategic route planning and interactive narrative. Its current city count is not transferred back to launch iOS.
- **P3:** [inkle, “Journey's End”](https://www.inklestudios.com/2014/07/14/approaching-journeys-end), 2014, accessed 2026-10-02; prelaunch discussion of route costs, risks and timings, market items, conditional journeys and the fixed eighty-day target.
- **P4:** [inkle, “Multiplayer Interactive Fiction”](https://www.inklestudios.com/2014/05/26/multiplayer_if), 2014, accessed 2026-10-02; the clock keeps running while the player inspects city activity or considers a connection.
- **P5:** [inkle, “So what is 80 Days?”](https://www.inklestudios.com/2014/04/15/so-what-is-eighty-days), 2014, accessed 2026-10-02; authored choices and per-journey situations. Its correction rejects an early real-world location-based premise.
- **P6:** [inkle, “An Unaccountable Delay, Passepartout!”](https://www.inklestudios.com/2014/07/22/unaccountable-delay), 2014, accessed 2026-10-02; a prelaunch first-hand playtest reached Paris and could linger there while the race advanced.
- **S1:** [John Tucker, launch-day iOS review](https://www.rpgfan.com/review/80-days-2/), 31 July 2014, accessed 2026-10-02; first-hand original iPhone account of route planning and missed trains, not an exact repeatable state trace.
- **S2:** [PocketGamer.biz, interview with Jon Ingold](https://www.pocketgamer.biz/rewriting-the-text-adventure-the-making-of-80-days/), 2014, accessed 2026-10-02; explicitly distinguishes a 62-day return from a day-152 return that still completes a journey.
- Claim IDs: `DAYS-001`–`DAYS-006`.

## Mechanical decomposition

### Action Genes

- Reuse `ACT-232` for one consequential authored response during the chosen journey. The packet does not assume a fixed response menu (`DAYS-005`).
- New `ACT-632` for choosing one *offered, scheduled* outbound service from the current city and committing its fare and departure. `ACT-127` selects a visible successor category in a run map, not a city-to-city service with a clock and price; `ACT-096` delegates local avatar pathfinding rather than choosing a transport connection (`DAYS-003`).

### System Behaviour Genes

- New `SYS-1243` for executing the selected service into a later city while charging its travel time and fare and allowing an authored en-route situation. Route commitment and automatic journey resolution are separate boundaries (`DAYS-003`–`DAYS-005`).

### Constraint Genes

- New `CON-742`: an ordinary departure is bounded by the currently offered connection, its departure schedule and its monetary cost; waiting for a service spends wager time. This does not assert that a missing fare always ends the game, or that every journey uses an ordinary purchased ticket (`DAYS-003`, `DAYS-004`).

### Information Genes

- New `INF-452` for the current-city view's known outgoing connections and their route terms alongside the current time. It does not reveal every possible later connection or a fixed narrative outcome (`DAYS-003`–`DAYS-005`).

### Objective Genes

- New `OBJ-269` for circumnavigating back to London within the 80-day wager. The current next-city arrival is merely progress toward that global comparison, and late completion is distinct from winning (`DAYS-002`).

### Time Genes

- Reuse `TIM-003` because the game clock keeps moving while decisions are available. It is not `TIM-029`'s pause-between-journey-choice calendar or real-world geolocation (`DAYS-004`).

## Reproducible transitions

| Before | Action or event | Bounded resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| First journey, London departure | Take the available opening Paris connection | The travellers arrive in Paris; its actual day and cash need a build-pinned observation | Entry into the bounded Paris packet | `DAYS-006` |
| Paris, an outgoing service is offered | Compare its route terms with another offered connection, if any | Different services can spend different time and money; a single available service is not falsely rendered as a fork | Connection choice has priced, scheduled terms | `DAYS-003` |
| Paris, no preferred service departs immediately | Spend time in the city or wait | The live clock advances; a later service may become usable while the wager budget shrinks | Waiting is consequential | `DAYS-004` |
| A presently eligible outbound service is selected | Commit the departure | Fare and journey time are applied as the trip proceeds toward the successor city | Route command differs from its resolution | `DAYS-003`, `DAYS-004` |
| A consequential authored incident is offered in transit | Select one available response | The scene and potentially later information or opportunity change; no particular event is guaranteed | Narrative response is not flavour-only | `DAYS-005` |
| The selected journey reaches its advertised next city | Inspect the new position and day | This analytical packet ends; the full London-return wager remains unsettled | Local checkpoint is not game victory | `DAYS-002`, `DAYS-003` |

## Strategic and experiential structure

- Local decision: choose among *currently available* services using visible cost and timing, rather than imagining a direct jump to any city on the globe.
- Medium-term planning: preserve enough time and money for later links; even reading, trading or waiting at a stop occurs under a running clock.
- Long-term structure: connect successive cities into a circumnavigation that returns to London within the wager. This packet tests only the first onward decision from Paris.
- Trust boundary: narrative branches and future links are not all exposed in advance. The record does not promise exact travel durations, scripted event order or success from a chosen connection.

## Replay and variation

The network contains many authored routes and consequences, so the player's selected connection, en-route response and subsequent discovery alter later plans. The launch-version first-journey option set was not captured; it cannot be collapsed into a guaranteed Paris-to-Istanbul path or imported from the larger desktop edition.

## Adjacent systems and history

*The Oregon Trail* (`GAME-0402`) also budgets days across travel choices, but its analysed A-157 menu pauses during deliberation and settles days after discrete commands. *Slay the Spire* (`GAME-0120`) also chooses successor nodes, but its map nodes disclose encounter categories and are not scheduled, fare-priced city services. These contrasts are scope-specific.

## Normalised genome

| Type | Active gene IDs | Carrier parameters |
|---|---|---|
| Action | `ACT-232`, `ACT-632` | authored response, offered transport service |
| System Behaviour | `SYS-1243` | elapsed travel, fare, successor city and scene |
| Constraint | `CON-742` | offered route, schedule and cost |
| Information | `INF-452` | known exits, journey terms and current time |
| Objective | `OBJ-269` | London return within wager |
| Time | `TIM-003` | live clock during deliberation |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `477` (`GAME-0001`–`GAME-0477`).
- Exact genome matches: none.
- Tied near matches: `GAME-0388` — L.A. Noire (`2 / 18 = 0.111111`).
- Supported combination subsets: none.
- Scan date: 2026-10-02.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0388` *L.A. Noire* | `ACT-232` and `TIM-003` permit a consequential authored response while some other game state can continue in live time. | *80 Days* commits priced and scheduled city connections toward a timed world-return wager; *L.A. Noire* investigates a case through clues and suspect challenges, with its live-time element belonging to traversal rather than a continuously running departure clock. | `2 / 18 = 0.111111`; tied nearest non-exact earlier signature, not the same travel rules. |

## Taxonomy impact

`TAXONOMY_CHANGE_215` records five new bounded genes. `ACT-232` and `TIM-003` transfer unchanged. Earlier signatures and combinations are not revised.

## Negative results

- Reject `ACT-127`: a Slay the Spire map successor exposes encounter category, not a fare-priced and scheduled transport service.
- Reject `TIM-029`: Oregon Trail day advancement occurs after a journey command while its decision menu can wait; inkle explicitly says the city clock continues while deliberating.
- Reject `CON-068`: a late return can still finish the story even when the wager is lost, rather than making the whole game terminate at the 80-day boundary.
- Reject post-launch city counts and route additions from the 2015 desktop release as evidence of the original iOS opening.

## Delta summary

## New facts

- [Confirmed | Direct | High] The original launch iOS game combines priced, timed travel connections with a continuing clock (`DAYS-001`, `DAYS-003`, `DAYS-004`).
- [Confirmed | Corroborated | High] Eighty days evaluates the wager, not whether a later world journey can continue and finish (`DAYS-002`).

## New genes

- [Observation | Corroborated | Medium] Five typed boundaries isolate scheduled-service commitment, journey settlement, departure feasibility, partial connection information and the wager result.

## New combinations

- [Observation | Limited | Medium] No new verified combination proposed; supported subsets are recomputed against this signature.

## Taxonomy changes

- [Observation | Corroborated | Medium] `TAXONOMY_CHANGE_215`; no earlier genome is changed.

## New questions

- A preserved launch-build iOS trace could pin the Paris menu, initial fare/cash, precise first onward timetable, story offer and its later effects. Those values are deliberately not inferred from post-launch walkthroughs.

## Next recommended game

- [Hypothesis | Limited | Medium] `GAME-0479` *Pitfall!* on the original Atari 2600 is the next selected unit after this one's acceptance and Goal stop window.
- Optimisation criterion: move from text-and-schedule routing to an older platform's continuous spatial hazard structure.
