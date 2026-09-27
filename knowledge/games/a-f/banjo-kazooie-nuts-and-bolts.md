---
game_id: GAME-0423
slug: banjo-kazooie-nuts-and-bolts
game_title: "Banjo-Kazooie: Nuts & Bolts"
analysis_status: reviewed
reviewed: 2026-09-27
combination_ids: []
gene_ids:
  action:
    - ACT-048
    - ACT-201
    - ACT-561
  system:
    - SYS-036
    - SYS-320
    - SYS-1118
  constraint:
    - CON-288
  information:
    - INF-415
  objective:
    - OBJ-014
  time:
    - TIM-003
---

# Game: Banjo-Kazooie: Nuts & Bolts — Great Balls of Fire

Use the canonical [vocabulary and genome rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Three rocks, a five-minute challenge, water location, available parts, selected vehicle and prize times are parameters, not separate genes.

## Analysis scope

- Version / ruleset: original English-language 2008 *Banjo-Kazooie: Nuts & Bolts* for Xbox 360. The packet is the `Great Balls of Fire` Jiggy challenge in Nutty Acres Act 2, not the identically named Jiggosseum achievement or the later Banjo titles. Exact retail disc revision was not inspected.
- Structured analysis target: `PLAT-XBOX-360` in [`knowledge/platforms/games.json`](../../platforms/games.json).
- Primary decision loop: optionally assemble and test a compact scoop-equipped vehicle at Mumbo's Motors from currently available parts; accept Humba Wumba's volcano challenge and choose that vehicle or the stock trolley; drive to each of three hot rocks, impart a useful push down its slope toward water or reposition it with Kazooie's wrench, observe whether it reaches water, and repeat for every remaining rock before the challenge clock expires.
- Entry and exit: a save with Nutty Acres Act 2 available and the necessary parts already acquired may build the optional vehicle before speaking to Humba Wumba near the volcano. The bounded attempt starts on selecting `Start Challenge` with a chosen player vehicle. Success is extinguishing all three designated rocks by getting each into water before the five-minute ceiling, with a Jiggy or faster Trophy grade determined by elapsed time. A rock left dry when the ceiling expires does not complete the challenge. This scope does not require the custom build: the regular trolley can complete it.
- Included: optional garage construction, the five workshop ratings, blueprint save/test/selection, occupied vehicle acceleration/steering and terrain contact, front-scoop versus rock contact, gravity/momentum down slopes, optional wrench lift/drop, the three-target water condition, challenge clock and elapsed-time reward bands.
- Excluded: Showdown Town's trolley-only traffic rule and Jiggy banking, acquiring new Mumbo Crates, shopping, all other Nutty Acres missions, multiplayer, exact parts bill, vehicle-force formula, rock coordinates or guaranteed one-hit push, obstacle placement beyond the guide's named examples, unverified physics exploits and exact disc build.
- Potential scoped modules: first-game trolley missions, a directly instrumented vehicle-build test, or later flying and watercraft challenges.
- Direct-play status: no Xbox 360 disc, executable, input trace, screenshot, video or audio was inspected. Microsoft's original manual states the vehicle-building, control and challenge-selection rules; the licensed contemporary Prima guide supplies this particular mission, its trolley alternative and timing. This is a bounded source reconstruction rather than measured vehicle physics.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `BNB-001` | Mumbo's Motors uses acquired parts to build, test and save vehicles; five ratings show speed, fuel, ammo, weight and part count. | Confirmed | Direct | High | M1 |
| `BNB-002` | A Game Host lets the player review an objective, select a player-choice vehicle or access the garage before starting; the controller distinguishes vehicle entry/exit, acceleration and steering from wrench pickup. | Confirmed | Direct | High | M1 |
| `BNB-003` | Nutty Acres Act 2's Great Balls of Fire asks Humba Wumba's visitor to cool three hot volcanic rocks by putting them in water within five minutes. | Observation | Corroborated | High | G1, S1 |
| `BNB-004` | The original trolley is sufficient, but the guide explicitly proposes a small custom bulldozer with a wide scoop; Kazooie's wrench can instead lift and drop a rock onto a useful slope. | Observation | Corroborated | High | M1, G1 |
| `BNB-005` | The three rocks begin on slopes; a useful push can let momentum carry them to water, while weak or badly directed contact can leave a rock dry and demand another attempt. | Observation | Corroborated | Medium | G1 |
| `BNB-006` | The guide prints Trophy 1:50, Jiggy 3:40 and Notes 5:00 for this challenge; these bands are not a claim about frame-precise engine behaviour or every possible release revision. | Observation | Corroborated | Medium | G1 |
| `BNB-007` | No original executable, part-by-part build recipe, numerical collision model or direct completion trace was tested. | Observation | Limited | High | M1, G1 |

## Basic data

- Release / origin: Microsoft and Rare's original Xbox 360 game, 2008. The manual's PDF-derived transcription identifies the game, garage and control rules; the licensed original Prima guide identifies the bounded Act 2 challenge.
- Platform or physical form: Xbox 360 single-player retail rules; the exact disc revision remains unknown.
- Mechanical families: physics and object manipulation (`FAM-007`) and real-time system pressure (`FAM-010`). The former covers scoop/rock collision and slope momentum; the latter covers an active deadline while repositioning finite targets.
- Sources accessed 2026-09-27:
  - **M1** — [Microsoft, original Xbox 360 *Banjo-Kazooie: Nuts & Bolts* instruction manual transcription](https://manuals.plus/microsoft/xbox-360-banjo-kazooie-video-game-manual), `Game Basics`, `Controller`, `Mumbo's Motors`, `Building Vehicles` and `Games`. Publisher text is transcribed by Manuals+; its page images and binary were not independently verified.
  - **G1** — [Catherine Browne, *Banjo-Kazooie: Nuts & Bolts Official Prima Guide* (2008), online text mirror](https://pdfcoffee.com/banjo-kazooie-nuts-and-bolts-official-prima-guide-pdf-free.html), Nutty Acres Act 2 `Great Balls of Fire`, printed pp. 46–47. A licensed contemporary guide, but the mirror is not treated as an authorised executable, measured run or official distribution channel.
  - **S1** — [GameSpot, contemporary *Banjo-Kazooie: Nuts & Bolts* walkthrough](https://www.gamespot.com/articles/banjo-kazooie-nuts-and-bolts-walkthrough/1100-6202576/), Nutty Acres Act 2 `Great Balls of Fire`, corroborating the three rocks and alternative trolley transport.

## Mechanical decomposition

### Action Genes

- New `ACT-561`: optionally place and revise available connected vehicle parts in Mumbo's Motors, testing and saving a compact wheeled design with a broad front scoop. The exact bill of materials is not asserted; the build is a player option, not the challenge's prerequisite. `BNB-001`, `BNB-004`.
- Reused `ACT-201`: enter and directly steer/accelerate the chosen world vehicle to each rock; the bear may exit to use the wrench. This is not a permanently occupied dedicated racing car. `BNB-002`–`BNB-004`.
- Reused `ACT-048`: take a small rock with Kazooie's magic wrench, carry it and drop it on a slope as an alternate to a direct vehicle push. It does not magically count as cooled before water contact. `BNB-002`, `BNB-004`.

### System Behaviour Genes

- New `SYS-1118`: the assembled connected functional parts make the chosen build operate as a vehicle and give its broad scoop a challenge-relevant contact surface; changes to the build can change what pushes a rock. The guide does not establish exact mass-to-impulse equations. `BNB-001`, `BNB-004`, `BNB-007`.
- Reused `SYS-320`: the occupied vehicle's acceleration, steering, terrain contact and collision are resolved continuously; no damage, tyre failure or measured fuel consumption is claimed for this attempt. `BNB-002`, `BNB-004`.
- Reused `SYS-036`: after scoop, trolley or wrench release, the free rock continues on its slope under collision, gravity and momentum; it can reach water or stop short. `BNB-004`, `BNB-005`.
- Resolution order: legal optional garage build and test → accept the host's challenge and select vehicle → drive or wrench-position a designated rock → contact/release imparts motion → slope and water-contact settlement → update completed-rock set and clock grade → repeat or expire. `BNB-001`–`BNB-006`.

### Constraint Genes

- Reused `CON-288`: a drivable design needs a viable driver seat, operating parts and traversable geometry; the stock trolley already meets that condition. Fuel, vehicle damage and exit injury are possible parameters of the general gene, not asserted occurrences in this mission. `BNB-001`, `BNB-002`, `BNB-007`.

### Information Genes

- New `INF-415`: the garage exposes speed, fuel, ammo, weight and part count before the player tests, saves and chooses a build. These ratings guide a choice; they do not display the exact impulse that will roll a specific rock. The named rocks, water and deadline are disclosed in the challenge briefing; this record does not invent a per-rock HUD checklist. `BNB-001`–`BNB-003`.

### Objective and Time Genes

- Reused `OBJ-014`: apply the fixed-receiver payload condition to each of three designated rocks: water contact extinguishes that rock; all three must be resolved for the bounded attempt. The number of targets and available water bodies are parameters. The guide's faster grades measure the same objective, not an extra requirement to win the campaign. `BNB-003`, `BNB-006`.
- Reused `TIM-003`: vehicle steering, rock motion and the challenge clock advance live; taking longer can lower the prize band or end the attempt at five minutes. Garage planning before the attempt is not itself under this clock. `BNB-003`, `BNB-005`, `BNB-006`.

## Reproducible transitions

| Before | Action | Bounded resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Nutty Acres Act 2 is available; eligible parts are already held | At Mumbo's Motors, assemble and test a small wheeled scoop vehicle | Five ratings reflect the current design; a saved build may be chosen for a player-choice challenge | optional functional preparation | `BNB-001`, `BNB-004` |
| Humba Wumba offers Great Balls of Fire | Start with the saved build or regular trolley | Three hot rocks and the five-minute challenge become the active task | custom build is not mandatory | `BNB-002`–`BNB-004` |
| An uncooled rock sits above water on a slope | Drive the scoop into it with a useful downhill line | Rock gains motion, rolls and may enter water; a weak or misdirected push may stop short | part-shaped contact plus physics | `BNB-004`, `BNB-005` |
| A rock is reachable but not well aligned | Exit, hold it with the wrench and drop it on a useful slope | Released rock resumes free motion; it remains pending until water contact | alternate manipulation pathway | `BNB-002`, `BNB-004` |
| One or two rocks have entered water | Push or carry another designated hot rock into water before the clock expires | Its cooled state joins the finite completed set; partial completion alone is not terminal | repeated receiver objective | `BNB-003`, `BNB-005` |
| Third rock reaches water before the ceiling | Accept the challenge result | The all-three condition settles; faster elapsed times qualify for the guide's Jiggy and Trophy bands | successful terminal and grade | `BNB-003`, `BNB-006` |
| At least one rock remains hot at five minutes | Let the challenge clock expire | No all-three completion is credited for that attempt | deadline failure | `BNB-003`, `BNB-006` |

## Strategic and experiential structure

- Local decision: choose a line that pushes the current rock toward water, or use the wrench to reset its position and exploit the slope.
- Medium-term planning: decide whether an optional broad scoop improves repeated contact enough to justify garage preparation, then visit the three rocks without wasting the live challenge clock.
- Long-term structure: the earned Jiggy contributes to later world access, but withdrawing it from the hub and opening later acts are not part of this attempt.
- Common heuristic: use slope and momentum rather than trying to carry every rock the entire distance; inspect whether a weak push stopped at the water's edge.
- Failure attribution: a dry rock after a poor line, incomplete three-rock set or expired clock explains a missed grade. Exact physical causes and UI indicators are not quantified without direct play.
- Player-trust factors: build ratings and a declared timed three-rock goal make the preparation and success condition understandable, but the guide cannot certify exact feedback frames.

## Replay and variation

The three target rocks and authored challenge are fixed by this packet, not procedurally generated. Player vehicle choice, component geometry, order of rocks, push angles, wrench use and elapsed time vary. Replaying for a faster Trophy band is plausible; no guarantee of a particular build's best time is asserted.

## Adjacent systems and history

*The Incredible Machine* lets the player edit a machine, then watches an autonomous run; this vehicle is directly driven while its front geometry engages a physical target. *Crazy Taxi* and *Project Gotham Racing 2* directly drive fixed vehicles but do not author the body that contacts the mission object. *Spore* edits and saves a living lineage's functional body, not a garage-assembled vehicle. The first Nutty Acres trolley race is deliberately not the scope: its supplied vehicle would not answer the construction question.

## Normalised genome

| Type | Active gene IDs | Key parameters |
|---|---|---|
| Action | `ACT-048`, `ACT-201`, `ACT-561` | wrench carry, direct drive, optional workshop assembly |
| System Behaviour | `SYS-036`, `SYS-320`, `SYS-1118` | free-rock motion, vehicle handling, part-shaped capability |
| Constraint | `CON-288` | viable driver/drive geometry |
| Information | `INF-415` | five garage ratings |
| Objective | `OBJ-014` | three hot rocks, water receiver, elapsed reward band |
| Time | `TIM-003` | live five-minute challenge; untimed garage preparation |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `422` (`GAME-0001`–`GAME-0422`).
- Exact genome matches: none.
- Tied near matches: `GAME-0112` — Human: Fall Flat (`3 / 15 = 0.200000`).
- Supported combination subsets: none.
- Scan date: 2026-09-27.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| Human: Fall Flat (`GAME-0112`) | `ACT-048`, `SYS-036`, `TIM-003`: a carried rigid object re-enters live gravity and collision while the player can still act | Human: Fall Flat uses direct avatar and arm control to carry a crate onto a climbing route; Nuts & Bolts lets an assembled, directly driven vehicle push any of three rocks into water under a five-minute mission clock, with wrench carry only an alternative | Near, `0.200000` |

## Taxonomy impact

[`TAXONOMY_CHANGE_161`](../../../research/taxonomy-changes/TAXONOMY_CHANGE_161.md) admits vehicle assembly, the applied physical capability of its part layout and workshop ratings. Earlier signatures and verified combinations remain unchanged.

## Negative results

- `ACT-511` and `SYS-1017` rejected: the Spore editor changes a living lineage's body, not a directly driven build selected for one physical challenge.
- `ACT-290` rejected: it covers a dedicated car continuously controlled in an event, whereas Banjo enters or exits an available world vehicle.
- `TIM-009` rejected: the player drives and corrects course under live physics; an editable transport layout is not followed by a locked automatic one-shot traversal.
- `OBJ-154` rejected: there is no required enabled extraction exit and terminal debrief after resolving the finite target set.
- First Nutty Acres Act 1 trolley challenge rejected as the primary packet because the supplied trolley does not demonstrate optional vehicle construction. Exact parts bill, physics coefficients and disc revision remain unknown.

## Delta summary

The player may design a vehicle for a fixed timed task, but the stock trolley can also win. A broad scoop changes the practical contact strategy for pushing three hot rocks downhill into water; the five garage ratings inform construction before the live challenge.

## New facts

- [Observation | Corroborated | High] The original manual and licensed guide jointly establish editable vehicles, a player-choice Great Balls of Fire mission, three water-bound rocks and a viable stock-trolley alternative (`BNB-001`–`BNB-004`).

## New genes

- [Observation | Corroborated | High] `ACT-561`, `SYS-1118` and `INF-415` distinguish part-level vehicle assembly, application of those parts to the live build and pre-challenge workshop ratings.

## New combinations

- [Observation | Corroborated | High] None created; existing verified combinations are tested against the complete ten-gene signature.

## Taxonomy changes

- [Observation | Corroborated | High] `TAXONOMY_CHANGE_161` admits three new typed boundaries without revising any earlier game.

## New questions

- Which exact part configurations, masses and contact impulses make the first rock reliably enter the lagoon on an original Xbox 360 disc?
- Do every original retail region and executable revision display identical timer thresholds and target placement?

## Next recommended game

- [Hypothesis | Limited | Medium] `GAME-0424` *Star Fox 64* after this unit's validation, local commit and Goal stop window.
- Optimisation criterion: move from authored vehicle construction and physical payload contact to guided rail flight, target choice and route branch qualification.
- Backlog impact: preserve approved `GAME-0424`–`GAME-0432` order; do not start another subject in this unit.

## Why this game

- [Hypothesis | Corroborated | Medium] The original Xbox 360 manual and licensed challenge guide together expose a repeatable, bounded vehicle-build-to-payload loop that fixed-car racing and autonomous contraption games do not capture.
