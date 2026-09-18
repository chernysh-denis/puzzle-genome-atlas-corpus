---
game_id: GAME-0302
slug: captain-toad-treasure-tracker
game_title: "Captain Toad: Treasure Tracker"
analysis_status: reviewed
reviewed: 2026-09-18
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-049
  system:
    - SYS-065
  constraint: []
  information:
    - INF-001
  objective:
    - OBJ-025
  time:
    - TIM-003
---

# Game: Captain Toad: Treasure Tracker

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Camera input,
the no-jump rule and the course's exact geometry parameterise the scoped
decisions; they are not newly numbered genes.

## Analysis scope

- Version / ruleset: the original European Wii U base game with Wii U GamePad,
  normal Episode 1 play and no amiibo mode. Nintendo's dated Wii U product
  record and its Wii U electronic manual establish this target. No console,
  disc, installed patch or save was available for direct inspection; the
  unit does not claim parity with every update or the later Switch/3DS ports.
- Structured analysis target: the original Wii U base product in
  `knowledge/platforms/games.json`; other releases are not inferred from it.
- Primary decision loop: inspect the first course's fixed compact terrain by
  orbiting the GamePad view, directly walk Captain Toad along the ground path,
  operate the lower Pull Switch while on its platform to reach the upper
  terrace, operate the upper switch to make the wooden approach usable, then
  follow that approach to the Power Star. The camera reveals fixed routes but
  does not itself rotate, reconnect or author the physical world.
- Entry and exit: a clean Wii U profile passes the opening story prologue and
  enters Episode 1's first ordinary course, `Plucky Pass Beginnings`. The
  bounded course ends when Captain Toad contacts its Power Star; the cleared
  page and the next course, `Walleye Tumble Temple`, are the source-reported
  successor. Nintendo documents automatic saving at course completion, but a
  retained state after reboot or reload was not observed here.
- Included: GamePad view inspection; direct walking and authored height
  access without a jump; two reachable Pull Switch interactions and their
  linked moving platform/ramp; the visible Power Star; course-clear credit,
  next-page selection and the manual's stated course-completion autosave;
  live world time while the platform moves and the avoidable side-ledge Shy
  Guy patrols. The ordinary Star path does not require the optional pickups.
- Excluded: detours for all three Super Gems, the Gold Mushroom challenge,
  turnip/POW/Super Pickaxe attacks, contact damage and life-stock recovery on
  the optional side ledge, Pixel Toad/amiibo, later courses, bonus courses,
  speed records, other episodes, Switch/3DS additions and completionist
  replay. These exclusions do not imply those mechanics are absent from the
  marketed product or the first course.
- Potential scoped modules: a later first-course completionist packet could
  examine optional pickups, combat and challenge stamps; a direct Wii U
  save/reload test could establish patch-specific persistence.
- Direct-play status: not conducted. Nintendo's official manual and Wii U
  product page establish controls, the Star completion condition, separate
  collectible/challenge status and autosaving. An original-Wii-U written
  walkthrough and a second course guide reconstruct the two-switch route and
  successor page. This is not an observed play session or measured reload.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `C-302-001` | Nintendo released the base game for Wii U with GamePad control; its later purchases through Wii U eShop closed, while Nintendo also documents packaged Wii U Game Discs. | Confirmed | Corroborated | High | P1, P2, P3 |
| `C-302-002` | Captain Toad cannot jump; the GamePad moves him, changes the view and activates reachable switches without the camera editing physical route geometry. | Observation | Direct | High | P1, P2 |
| `C-302-003` | In Episode 1's first ordinary course, the lower switch raises a platform to the upper terrace and the upper switch opens the wooden approach to the Power Star. | Observation | Corroborated | Medium | S1, S2 |
| `C-302-004` | Grabbing the course's Power Star clears it. Super Gems and the post-clear bonus challenge have separate page indicators, so collecting them all is not a prerequisite for this first clear. | Observation | Direct | High | P2 |
| `C-302-005` | The manual says progress is automatically saved at certain points, including course completion, and cleared courses have a page marker; this unit has no observed save/reload result. | Observation | Direct | High | P2 |
| `C-302-006` | The following Episode 1 course is `Walleye Tumble Temple`; the exact retained next-page state is reconstructed, not tested on a console. | Observation | Limited | Medium | S1, P2 |
| `C-302-007` | A Shy Guy moves on a side ledge during the first course, so the level runs in real time even though the selected Star route avoids that encounter and has no countdown. | Observation | Limited | Medium | S1, S2 |

## Basic data

- Release / origin: Nintendo developed and published the Wii U original;
  Nintendo's European listing dates its local release to 2015-01-02.
- Platform or physical form: original Wii U game with Wii U GamePad; Nintendo
  records both an earlier shop release and packaged Wii U Game Disc access.
  The Wii U eShop purchase channel is closed, and no lawful local disc/console
  was available during this unit.
- Puzzle family: compact spatial route activated by authored world switches,
  with direct agent navigation and a fixed progress token.
- Primary sources: [Nintendo Wii U product](https://www.nintendo.com/en-gb/Games/Wii-U-games/Captain-Toad-Treasure-Tracker-892923.html)
  (**P1**), [Nintendo Wii U electronic manual](https://www.nintendo.com/eu/media/downloads/games_8/emanuals/wii_u_6/captain_toad__treasure_tracker/ElectronicManual_WiiU_CaptainToadTreasureTracker_EN.pdf)
  (**P2**), [Nintendo packaged-disc announcement](https://www.nintendo.com/en-gb/News/2016/September/Must-have-titles-join-the-Nintendo-Selects-range--1143079.html)
  (**P3**).
- Secondary sources: [original-Wii-U GameFAQs written route](https://gamefaqs.gamespot.com/wii-u/805615-captain-toad-treasure-tracker/faqs/70755)
  (**S1**), [Neoseeker first-course written guide](https://www.neoseeker.com/captain-toad-treasure-tracker/walkthrough/1-1_Plucky_Pass_Beginnings)
  (**S2**). The latter describes a later port and only corroborates course
  geometry also described by the original-Wii-U route; it is not used to
  infer platform-specific controls or new content.
- Claim IDs: `C-302-001`–`C-302-007`.

## Mechanical decomposition

### Action Genes

- Existing gene IDs: `ACT-008` for direct movement of one controllable body
  through lower, lift and upper walkable surfaces; `ACT-049` for walking to
  each reachable Pull Switch and commanding its linked platform/ramp state.
- Candidate genes: none. The GamePad view orbit is an information-access
  parameter, not `ACT-094`'s global collision-frame rotation or `ACT-095`'s
  perspective-authoritative camera law. No direct jump command exists; that
  is the movement rule inside `ACT-008`, not a separate action.
- Parameters: route geometry, camera angle, no-jump movement, lever reach,
  lift pose and approach pose.
- Claim IDs: `C-302-002`, `C-302-003`.

### System Behaviour Genes

- Existing gene IDs: `SYS-065` for the linked platform/ramp moving along
  authored trajectories after reachable switches are pulled. The lower
  platform carries the walker upward; the upper mechanism establishes the
  final walkable approach.
- Candidate genes: none. The ordinary course-clear and later-page credit are
  the progress-token settlement already included by `OBJ-025`; neither a
  scored racing result nor a new resource-conversion system is required.
- Resolution order: approach lower switch → activate lift → arrive at upper
  terrace → activate upper switch → wait for the wooden route to settle →
  directly traverse the opened route → contact Star → record course clear.
- Parameters: mechanism endpoints, travel speed, collision and rider
  attachment, Star contact, page marker and save timing.
- Claim IDs: `C-302-003`–`C-302-006`.

### Constraint Genes

- Existing gene IDs: none. No-jump traversal and the fixed course geometry
  parameterise `ACT-008`; a lower platform position blocks the upper route as
  ordinary physical collision, not a separate credential or item predicate.
- Candidate genes: none. `CON-136` excludes a path blocked only by current
  collision, and `CON-144` concerns snap-only projected traversal decisions
  rather than a physically raised platform.
- Scarce strategic resources: no move quota or countdown for the admitted
  direct Star path. The manual's lives and side-ledge pickups are recorded as
  excluded branches, not silently treated as nonexistent.
- Claim IDs: `C-302-002`–`C-302-004`, `C-302-007`.

### Information Genes

- Existing gene IDs: `INF-001` for inspectable current route state: the
  walker, lower and upper surfaces, both reachable levers, platform pose and
  Star can be inspected by turning the GamePad view before route decisions.
- Candidate genes: none. Camera orbit changes what side of the same fixed
  diorama is visible; it does not create Fez's new projection collision slice
  or Echochrome's camera-authoritative path.
- Claim IDs: `C-302-002`, `C-302-003`.

### Objective Genes

- Existing gene IDs: `OBJ-025` for contact with the fixed Power Star after
  opening a traversable course route; that token clears the authored course
  and contributes to later course access.
- Candidate genes: none. Optional Super Gems and the Gold Mushroom bonus
  challenge have separate indicators and are not a conjunctive requirement
  for this first Star settlement.
- Success, evaluation and failure: Power Star contact clears the course;
  merely viewing it or collecting optional gems does not. A fall or hostile
  contact can lose a life under the general manual, but that optional failure
  branch is not the selected direct Star route.
- Claim IDs: `C-302-004`–`C-302-006`.

### Time Genes

- Existing gene IDs: `TIM-003` because the linked mechanism moves in world
  time after activation and the first course's Shy Guy patrol continues while
  the player navigates, despite the absence of a course countdown.
- Candidate genes: none. `TIM-002` would falsely describe the entire active
  course as having no independent state advance; `TIM-003` does not by itself
  assert a timed completion requirement.
- Claim IDs: `C-302-003`, `C-302-007`.

## Reproducible transitions

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Fresh story prologue has yielded the first Episode 1 course page | Select `Plucky Pass Beginnings` | The bounded first ordinary diorama opens with Captain Toad below its upper Star route | Reproducible course entry, not a Switch/3DS port | `C-302-001`, `C-302-003` |
| Captain Toad is at the lower path and the lift is down | Rotate the GamePad view, then walk to the lower switch | The physical terrain does not rotate; the lever and lift remain the same addressed objects | View access versus world-state manipulation | `C-302-002`, `C-302-003` |
| Captain Toad occupies the lower lift | Pull the lower switch | Its platform rises on its fixed vertical track with the walker to the upper terrace | Switch command and automatic platform transport | `C-302-003` |
| The upper wooden approach is not yet connected | Walk to and pull the upper switch | The authored approach is raised to a traversable pose | Second route-state change, not a camera-created join | `C-302-003` |
| The approach reaches the Power Star | Walk the opened route without collecting side gems | Touching the Star clears the first course | Optional collectibles do not gate first clear | `C-302-004` |
| The first course has cleared | Return to the course-book successor | The cleared marker and following `Walleye Tumble Temple` page are reported; course completion is an official autosave point, but no reload was observed | Progress and evidence boundary | `C-302-005`, `C-302-006` |

## Strategic and experiential structure

- Local decision: distinguish camera-only discovery from a physical lever
  operation and approach the switch using a no-jump walkable route.
- Medium-term planning: raise the lower platform before using the upper
  switch, then follow the resulting wooden route instead of seeking a jump
  shortcut or treating optional gems as keys.
- Long-term structure: a first credited Star leads to the next course page;
  later gems can gate other courses under the manual, but that later threshold
  is outside this immediate successor.
- Common heuristics: rotate the view before committing to a path, follow
  connected walkable surfaces, use the platform as a lift, and stop at the
  first ordinary Star rather than completing every collectible branch.
- Failure attribution: an unreachable height is a missing switch/route
  state, not an unseen jump input. Side-route contact and falls are separate
  possible failures, not evidence that gems are mandatory.
- Player-trust factors: the camera must consistently reveal the same world
  geometry; course-clear, optional-gem and bonus-stamp indicators must stay
  distinct. Persistence is documented, not presented as personally tested.
- Claim IDs: `C-302-002`–`C-302-007`.

## Replay and variation

- What changes between sessions: the player's route, camera angles and
  optional pickup choices; the fixed first-course layout is not generated.
- Randomness or procedural generation: none established for the mandatory
  Star route.
- Multiple viable strategies: the Star can be taken without the three gems
  or bonus item; optional detours can be taken before the same terminal.
- Typical replay motive: later collectible/challenge completion, excluded
  from this packet.
- Claim IDs: `C-302-003`–`C-302-005`.

## Adjacent systems and history

- Direct predecessors: Captain Toad courses in Super Mario 3D World inspired
  the standalone product, but that game's rules are not imported here.
- Variants: later Switch and 3DS releases, Wii U amiibo mode and later-course
  devices are separate scope. No input equivalence is inferred.
- Similar games: Braid combines directly driven movement and a reachable
  switch with a linked moving platform, but includes jump, time reversal and
  moving enemies as central route rules. Monument Valley changes one physical
  bridge and then automatically paths Ida under projection, whereas this
  GamePad camera observes fixed geometry and the walker moves directly.
- Important differences: the Star is a fixed room-progress token, not a
  score threshold; camera orbit does not itself alter traversal legality.
- Claim IDs: `C-302-001`–`C-302-007`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-049` | Direct no-jump walking; lower and upper Pull Switches |
| System Behaviour | `SYS-065` | Authored platform/ramp trajectories |
| Constraint | none | Fixed traversable geometry, no-jump input boundary |
| Information | `INF-001` | Inspectable fixed diorama under GamePad view orbit |
| Objective | `OBJ-025` | First-course Power Star and retained clear |
| Time | `TIM-003` | Live platform motion and avoidable side patrol |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `301` (`GAME-0001`–`GAME-0301`).
- Exact genome matches: none.
- Tied near matches: `GAME-0034` — Braid, Anniversary Edition (`5 / 15 = 0.333333`); `GAME-0116` — The Stanley Parable: Ultra Deluxe (`3 / 9 = 0.333333`).
- Supported combination subsets: none.
- Scan date: 2026-09-18.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0034` Braid, Anniversary Edition | `ACT-008`, `ACT-049`, `SYS-065`, `INF-001`, `TIM-003` | Both operate reachable switches while traversing moving platforms, but Braid's jumping, rewind and enemy interactions shape its route; Toad's first Star is a fixed progress token reached by a no-jump walk and an observational camera. | Tied near `0.333333`; shared platform loop, different terminal and time control. |
| `GAME-0116` The Stanley Parable: Ultra Deluxe | `ACT-008`, `INF-001`, `TIM-003` | Both allow direct inspection and movement during live world time. Stanley's branching narrated corridor choices have no switch-directed lift or puzzle-gated Star acquisition. | Tied near `0.333333` numerically; not a mechanical substitute. |

## Taxonomy impact

- Registry changes: none; all six selected genes are reused unchanged.
- Taxonomy-change record: none.
- Candidate terms affected: camera orbit, no-jump route, Pull Switch,
  Star clear and optional-gem exclusion are reviewed parameters or scope
  decisions, not new IDs.

## Negative results

- No structured negative-result record is warranted. Specifically,
  `ACT-094`/`ACT-095` would falsely make the camera a topology operation;
  `CON-136` would falsely make a physical route barrier a persistent
  acquisition prerequisite; `OBJ-026` excludes the progress-token contact
  that is the actual terminal. The course's optional collectibles do not
  replace the Star as its ordinary clear condition.

## Delta summary

## New facts

- [Observation | Direct | High] Nintendo's Wii U manual separates the
  Power Star clear, gem and bonus indicators and documents autosaving at
  course completion (`C-302-004`, `C-302-005`).

## New genes

- [Observation | Corroborated | Medium] No new genes; all selected boundaries
  transfer from the existing corpus.

## New combinations

- [Observation | Corroborated | Medium] No verified combination is admitted
  merely because this first-level packet uses several familiar genes.

## Taxonomy changes

- [Observation | Direct | High] No existing boundary changes.

## New questions

- Does the original Wii U disc's current installed patch reproduce the
  reported two-switch path and preserve the cleared first page and next-page
  access after a full console restart?

## Next recommended game

- [Hypothesis | Limited | Medium] `GAME-0303` Sifu, PS5 Standard Edition, as
  recorded in the platform-amended selection.
- Optimisation criterion: preserve the selected nine-game platform balance
  while moving from a compact Nintendo spatial route to authored martial
  combat on current PlayStation hardware.
- Expected information gain: test live defence, age/skill persistence and
  encounter-route boundaries against existing action-combat genomes.
- Backlog impact: no reordered later subject.

## Why this game

- [Hypothesis | Limited | Medium] This original Wii U opening tests whether
  camera inspection without topology control and a no-jump avatar can be
  represented by current spatial-route genes; Sifu provides an intentionally
  distant following decision loop.
