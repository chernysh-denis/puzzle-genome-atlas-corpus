---
game_id: GAME-0371
slug: pokemon-snap
game_title: Pokémon Snap
analysis_status: reviewed
reviewed: 2026-09-23
combination_ids: []
gene_ids:
  action:
    - ACT-502
    - ACT-506
    - ACT-507
  system:
    - SYS-045
    - SYS-1008
    - SYS-1009
  constraint:
    - CON-673
    - CON-674
    - CON-675
  information:
    - INF-299
    - INF-378
  objective:
    - OBJ-214
  time:
    - TIM-003
---

# Game: Pokémon Snap

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Pokémon species,
the Beach course, Pokémon Food and the 60-exposure roll are carrier parameters,
not gene names.

## Analysis scope

- Version / ruleset: the original English Nintendo 64 Pokémon Snap rules,
  documented by Nintendo's original instruction booklet, represented by the
  licensed Nintendo 64 Classics application under Nintendo Switch Online +
  Expansion Pack. No Switch executable or original cartridge was inspected.
- Structured analysis target: the licensed Nintendo Switch N64 Classics
  distribution; see `GAME-0371` in
  [`knowledge/platforms/games.json`](../../platforms/games.json).
- Primary decision loop: during one automatically advancing Beach excursion,
  look around for subjects, place unlocked Pokémon Food to elicit a useful
  response, focus and expose a limited number of photos while the ZERO-ONE
  continues moving; after the goal gate, curate at most one picture per
  species for Professor Oak's content-sensitive check and Report.
- Entry: a valid saved Laboratory state in which Pokémon Food has already
  been unlocked, with the Beach course available. Choose Beach and begin one
  fresh 60-exposure roll in the ZERO-ONE. The exact previous unlock threshold
  is outside this packet; the manual establishes that items become available
  after progress, not a value for this staged save.
- Evaluation boundary: reach Beach's goal gate, mark a captured Pikachu photo
  as the one submitted for that species, complete Professor Oak's check, and
  observe its size, pose, technique, same-species bonus and final score in
  the PKMN Report. If Pikachu already has a recorded picture, Oak compares
  the new submission and keeps the better result; acceptance means a scored
  submission, not an invented guarantee of improvement. The game continues
  afterward; this is one bounded research excursion, not a campaign win.
- Noncompletion: reaching the gate without a usable Pikachu exposure, losing
  the moment because the vehicle passes it, exhausting film before it, or
  declining to mark that picture leaves this scoped target unmet; the player
  can replay the course. No death, combat defeat or global game-over is
  inferred.
- Included: Beach route, automatic ZERO-ONE movement and collision-safety
  behaviour, live camera aim/focus/shutter, on-screen Focus Sensor with
  `NEW`/`?` indication and remaining film, Pokémon Food thrown while not
  focusing, Pikachu's documented reaction, goal gate, Camera Check,
  one-photo-per-species mark, Oak's size/pose/technique/other-Pokémon score,
  comparison with a prior best and Report persistence.
- Excluded: the other five courses, hidden passages and later campaign
  completion, Pester Balls, Poké Flute and speed upgrades, multiplayer photo
  comparison, optional Album and Gallery curation, print kiosks, Switch
  rewind/save-state or online conveniences, exact hidden scoring coefficients,
  random encounter frequencies and New Pokémon Snap's distinct rules.
- Reproducible parameterisation: record course, item availability, starting
  Report best for Pikachu, ZERO-ONE route position, camera direction and
  focus, food impact location, Pikachu reaction, exposure index out of 60,
  captured frame, goal-gate arrival, chosen species mark, each displayed
  scoring category, total and retained Report best. This packet does not
  prescribe a perfect photograph or undocumented score threshold.
- Direct-play status: not conducted. No game entitlement, installation,
  executable hash, cartridge, save, screenshot, video, audio or input trace
  was inspected. The original manual and Nintendo's current distribution
  page support a source-bounded rule reconstruction, not an observed run.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `PS-001` | Nintendo's N64 Classics catalogue includes the original Pokémon Snap on Switch Online + Expansion Pack | Confirmed | Direct | High | P1 |
| `PS-002` | Beach is initially available and ZERO-ONE advances along a course while the player looks and focuses | Confirmed | Direct | High | P2 |
| `PS-003` | One course roll permits 60 exposures and ends at the goal gate before Camera Check | Confirmed | Direct | High | P2 |
| `PS-004` | Pokémon Food is unavailable at the beginning, later usable outside camera focus and can change Pikachu's pose | Confirmed | Direct | High | P2 |
| `PS-005` | Camera Check permits at most one marked image per Pokémon species for Oak's check | Confirmed | Direct | High | P2 |
| `PS-006` | Oak judges size, pose, centring technique and same-species presence, then retains the better reported picture | Confirmed | Direct | High | P2; P1 |
| `PS-007` | The Focus Sensor reveals recognised targets, `NEW` or `?`, and the live HUD shows remaining film | Confirmed | Direct | High | P2 |
| `PS-008` | This staged food-unlocked Beach excursion can be reproduced as an evaluation packet without claiming a full-game terminal | Observation | Limited | Medium | P2 |

## Basic data

- Release / origin: original Nintendo 64 Pokémon Snap (1999), later offered
  through Nintendo Switch Online + Expansion Pack; the product called New
  Pokémon Snap is a separate successor.
- Platform or physical form: original N64 rule packet represented by the
  licensed Nintendo Switch N64 Classics application, not a directly tested
  cartridge or installed build.
- Puzzle family: live observation and timing; constrained capture; evidence
  curation and scored report.
- Primary sources:
  - P1: [Nintendo's Switch Online Pokémon Snap availability and game
    description](https://www.nintendo.com/us/whatsnew/nintendo-switch-online-expansion-pack-pokemon-snap-is-now-available/), checked 2026-09-23.
  - P2: [Nintendo's original English Pokémon Snap instruction booklet](https://www.nintendo.com/eu/media/downloads/games_8/emanuals/nintendo_8/Manual_Nintendo64_PokemonSnap_EN.pdf), pp. 6–7, 10–21, checked and visually read 2026-09-23.
- Secondary sources: none needed for the bounded rules asserted here.
- Claim IDs: `PS-001`–`PS-008`.

## Mechanical decomposition

### Action Genes

- Reused `ACT-502`: commit the current ready camera frame with one shutter
  input; this unit clarifies readiness as a capture-resource parameter rather
  than Dead Rising's specific rechargeable camera.
- New `ACT-506`: throw available Pokémon Food to a reachable scene location
  without steering the vehicle or directly commanding a Pokémon.
- New `ACT-507`: after the course, select one exposure for each pictured
  species and mark it for Oak's evaluation; selecting a second Pikachu image
  replaces the same species' marked candidate.
- Camera aim, focus toggle and fast look are parameters of live frame choice;
  menu navigation and an unused Album mark are not additional Action genes.
- Claim IDs: `PS-002`, `PS-004`, `PS-005`.

### System Behaviour Genes

- Reused `SYS-045`: ZERO-ONE proceeds automatically; its authored course
  position advances even while the photographer searches for a shot.
- New `SYS-1008`: an eligible wild subject responds to food placed near it,
  changing its live position or pose without becoming player-controlled.
- New `SYS-1009`: after a marked submission, Oak evaluates visible photo
  categories, compares with any previous best for the same species and
  persists the better Report result.
- Resolution order: food lands near Pikachu → Pikachu's response changes the
  camera opportunity → legal shutter records current frame and consumes one
  exposure → goal gate opens Camera Check → one marked photo per species goes
  to Oak → displayed categories and Report best settle.
- Claim IDs: `PS-002`–`PS-006`.

### Constraint Genes

- New `CON-673`: the photographer may look around and focus but cannot steer
  the ZERO-ONE off the authored Beach route or wait indefinitely at a missed
  subject. Looking behind can slow, not reverse, its course progression.
- New `CON-674`: one course roll has 60 shutter exposures; using one reduces
  the remaining count and an exhausted roll cannot make another photo in
  that excursion.
- New `CON-675`: Oak accepts no more than one marked photo of a given species
  from the current Camera Check; multiple captured Pikachu frames are
  alternatives for curation, not simultaneous Report entries.
- Scarce strategic resources: camera opportunities along a moving route and
  the finite exposure count; Pokémon Food is unlocked availability, not an
  invented finite stock in this packet.
- Claim IDs: `PS-002`–`PS-005`.

### Information Genes

- Reused `INF-299`: Oak's post-course check exposes each category and the
  aggregate photo score so the evaluated result is attributable.
- New `INF-378`: live viewfinder identifies recognised or unknown focal
  subjects, indicates newly unreported species and shows remaining film;
  it does not disclose a future perfect score.
- Claim IDs: `PS-006`, `PS-007`.

### Objective and Time Genes

- New `OBJ-214`: complete the declared course and get one selected subject
  photo evaluated into its persistent species Report entry or best-shot
  comparison. This is a bounded appraisal objective, not an ending for all
  Pokémon Snap.
- Reused `TIM-003`: the subject, vehicle and chance to expose change during
  real-time input; post-course curation is untimed but does not replace the
  active excursion's clock.
- Claim IDs: `PS-002`, `PS-003`, `PS-005`, `PS-006`, `PS-008`.

## Reproducible transitions

| Before | Action | Bounded resolution | Establishes | Claim |
|---|---|---|---|---|
| Laboratory save with Pokémon Food unlocked and Beach available | choose Beach | ZERO-ONE starts the Beach course with a fresh 60-photo roll | staged entry and fixed route | `PS-002`, `PS-003`, `PS-004` |
| ZERO-ONE approaches visible Pikachu | aim and focus on the live scene | vehicle continues forward; Focus Sensor can identify the target | transient capture opportunity | `PS-002`, `PS-007` |
| Pikachu is close enough to a reachable landing place and camera is not focused | throw Pokémon Food beside it | the subject reacts to the food and may turn or pose; no direct creature command occurs | item-conditioned response | `PS-004` |
| Pikachu is in the current frame and at least one exposure remains | commit shutter | the current scene is captured and film count falls by one; later movement cannot retroactively improve the frame | finite live photograph | `PS-003`, `PS-007` |
| Course vehicle reaches the goal gate | let the route finish | Camera Check exposes the roll; movement opportunity ends | route-to-review handoff | `PS-003`, `PS-005` |
| Several Pikachu photos exist in Camera Check | mark one candidate for Oak | only one Pikachu submission remains marked even if another was captured | per-species curation | `PS-005` |
| Marked Pikachu image goes to Oak | complete check | size, pose, technique and same-species categories settle; the Report records it if better than any prior best | scored persistent evaluation | `PS-006` |

## Strategic and experiential structure

- The player controls observation and intervention, not the tour route.
  Looking, food placement and shutter timing must be coordinated before the
  ZERO-ONE passes the subject.
- A larger, centred, active Pikachu and another of the same species can
  improve category scores, but no exact scoring constants or guaranteed
  reaction timing are claimed. Food changes an opportunity; it does not
  guarantee a perfect frame.
- Camera Check is a second decision layer: many exposures can be made, but
  only one image per species goes forward. Oak's visible category report
  helps attribute a weak outcome to composition rather than inventing a
  hidden quality threshold.

## Replay and variation

- The Beach route is authored, not procedurally generated. Player look
  direction, food placement, selected exposure and resulting photograph can
  vary on each run.
- Returning after unlocking more items would change the available actions;
  Pester Ball and Poké Flute behaviour are not imported into this one-food
  packet. Replaying can improve an existing Report best.

## Adjacent systems and history

- Dead Rising shares the shutter commitment but its camera readiness,
  immediate PP reward and survival route differ from Pokémon Snap's finite
  film, post-course species curation and Oak's comparative photo report.
- Viewfinder turns placed photographs into world geometry; Pokémon Snap's
  picture is evidence submitted for evaluation and never becomes traversable
  terrain.
- New Pokémon Snap has separate modern scoring and progression and is not
  treated as mechanically identical to the original.

## Normalised genome

The front matter is canonical. This reviewed packet has 13 Active genes:
three Action, three System Behaviour, three Constraint, two Information, one
Objective and one Time. Nine distinctions are new, and the earlier Dead
Rising signature remains unchanged when `ACT-502` gains a second carrier.

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `370` (`GAME-0001`–`GAME-0370`).
- Exact genome matches: none.
- Tied near matches: `GAME-0092` — Echochrome (`2 / 21 = 0.095238`); `GAME-0345` — Duck Hunt (`2 / 21 = 0.095238`).
- Supported combination subsets: none.
- Scan date: 2026-09-23.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0092` Echochrome | `SYS-045`, `TIM-003` | Both have an autonomous traveller and live input, but Echochrome edits perspective to reconnect paths; Pokémon Snap commits a finite photo and curates evidence for scoring. | Tied near, `2 / 21 = 0.095238`; not an exact match. |
| `GAME-0345` Duck Hunt | `SYS-045`, `TIM-003` | Both present moving subjects under real-time input, but Duck Hunt shoots a target for a round threshold; Pokémon Snap changes its pose with food, captures photos and submits one per species after a course. | Tied near, `2 / 21 = 0.095238`; not an exact match. |

## Taxonomy impact

`TAXONOMY_CHANGE_110` records nine additive boundaries and a narrowed
clarification of `ACT-502` readiness, without changing any earlier game
signature. No combination is inferred from one new photography carrier.

## Negative results

- The staged saved-state entry does not establish the numeric Pokémon Food
  unlock requirement or a particular earlier progression trace.
- Beach goal-gate arrival alone is not scored photographic success; an Oak
  submission is needed for this packet's evaluation boundary.
- No claim is made that a lower-scoring replacement erases the previous
  Report best, that a food throw guarantees a pose, or that one expedition
  finishes the game's multi-course Report.

## Delta summary

The original manual and licensed re-release identify a live photography
loop: an authored moving course creates fleeting opportunities, food can
change a subject response, finite film captures candidate frames, and a
post-course one-per-species selection leads to category scoring and retained
Report evidence.

## New facts

- [Confirmed | Direct | High] Beach is available initially, ZERO-ONE keeps
  moving, each roll has 60 exposures, and the course gate precedes selection
  (`PS-002`, `PS-003`).
- [Confirmed | Direct | High] Unlocked Pokémon Food can alter a subject's
  behaviour, while Oak evaluates one marked photo per species and retains
  the better Report result (`PS-004`–`PS-006`).

## New genes

- [Observation | Direct | High] Add `ACT-506`, `ACT-507`, `SYS-1008`,
  `SYS-1009`, `CON-673`, `CON-674`, `CON-675`, `INF-378` and `OBJ-214` as
  bounded food, curation, reaction, appraisal, route, film, submission,
  disclosure and evaluation rules.

## New combinations

- None; this one new carrier does not establish recurring composition.

## Taxonomy changes

- `TAXONOMY_CHANGE_110` records the nine additive boundaries and an
  `ACT-502` readiness clarification.

## New questions

- Direct observation of the licensed application could pin its exact runtime
  handling, food unlock threshold and any wrapper-only timing behaviour.

## Next recommended game

`GAME-0372` Guitar Hero III: Legends of Rock, as reserved in
[`SEARCH_DEMAND_GAME_SELECTION_027`](../../../research/selection/SEARCH_DEMAND_GAME_SELECTION_027.md).

## Why this game

Guitar Hero III changes the primary loop from mobile scene photography to
rhythm-chart execution and should visibly contrast the Beach camera card.

## Completion checklist

- [x] Original rules, staged entry, appraisal exit and exclusions bounded.
- [x] Publisher manual and licensed distribution separated from direct play.
- [x] Deterministic comparison, bilingual presentation, artwork and gates complete.

## Search-demand continuation

This is the second reserved unit in
[`SEARCH_DEMAND_GAME_SELECTION_027`](../../../research/selection/SEARCH_DEMAND_GAME_SELECTION_027.md).
