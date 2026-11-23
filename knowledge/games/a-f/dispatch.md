---
game_id: GAME-0545
slug: dispatch
game_title: Dispatch
analysis_status: reviewed
reviewed: 2026-11-19
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-106
    - ACT-191
    - ACT-232
    - ACT-743
  system:
    - SYS-139
    - SYS-299
    - SYS-773
    - SYS-1577
    - SYS-1578
    - SYS-1579
    - SYS-1580
    - SYS-1581
  constraint:
    - CON-068
    - CON-597
  information:
    - INF-123
    - INF-148
    - INF-526
  objective:
    - OBJ-302
  time:
    - TIM-003
---

# Game: Dispatch

Use the [canonical vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
Hero names, five attributes and call requirements parameterise these rules.
No universal success formula is inferred from a suitability diagram.

## Analysis scope

- Version / ruleset: full English PS5 release, original 2025 season rules,
  standard dispatch and timed hacking, with Unlimited Hacking Attempts off.
  The completed eight-episode release is the product target; this is not the
  demo, Early Access, Episode 1 interview simulation or a later Deluxe mode.
  Exact installed PS5 patch, binary and controller bindings were not inspected.
  PC play accounts corroborate shared rules, not platform timing identity.
- Entry: in Episode 2, Onboard, after Chase introduces the desk and the initial
  eight-person Z-Team, begin the first real shift before assigning its first
  ordinary call. Retain the initial profiles and no newly spent shift points.
  Preshift story choices are held fixed; no cross-choice stat equivalence is
  asserted. The roster is Flambae, Sonar, Invisigal, Prism, Punch Up, Coupé,
  Golem and Malevola, without later replacements or promoted powers.
- Primary decision loop: inspect the current call and available responders,
  compare effective attributes and relevant powers, fill the allowed slots
  and dispatch. While the live map advances, choose among other current calls
  or wait for readiness. Resolve offered contextual decisions or a hack,
  inspect outcome, injury, return and rest, then allocate earned development
  points before the next assignment.
- Positive exit: finish the first shift through the required Granny's Donuts
  intervention, including its camera and sprinkler hacks, and the performance
  review that leads to the break room. Successful ordinary calls are desired;
  perfection is an optional achievement, not the continuation condition.
- Non-perfect exit: a missed or failed ordinary call remains in the review.
  An injury or an expired call is not by itself whole-shift Game Over.
  A failed local timed hack is not silently counted as a completed hack.
- Included: current call slots and expiries; five-attribute suitability;
  conditional starter powers and their discovery; travel, return and rest;
  injury and eligible ally healing; experience, upgrades, offered call choices;
  traversable hack nodes, directional build prompts and password gates;
  local hack time limits; the closing intervention and shift evaluation.
- Excluded: Episode 1 action scenes and job assessment, preshift and postshift
  relationship conversations, later shifts and team firing, romance routes,
  later power upgrades, full-season endings, replay achievements, analytics
  percentages, unlimited-attempt accessibility rules and Deluxe challenges.
  Exact random probabilities, travel seconds, recovery durations, map-clock
  pause triggers and per-call reward coefficients remain unmeasured.
- Potential modules: later shifts with roster replacement and sabotage;
  story-choice relationships; later hostile antivirus hacking encounters.
- Direct-play status: no PS5, executable, save, controller trace or native
  shift was run. Two first-shift screenshots from a first-hand review were
  inspected as still images. Developer/product material and independent
  written play accounts reconstruct the transitions. No video or audio played.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
| --- | --- | --- | --- | --- | --- |
| DIS-001 | The released PS5 product includes map-based hero deployment and roster development. The selected boundary is the first real Episode 2 shift, not the earlier assessment. | Observation | Corroborated | High | P1, P2, S1, S3, S7 |
| DIS-002 | Calls use five attributes: Combat, Vigor, Mobility, Charisma and Intellect. Proposed teams are compared with call needs; suitability does not establish a universal guaranteed resolver. | Observation | Corroborated | High | P1, S1, S2, S4 |
| DIS-003 | Concurrent calls have expiring opportunities. Assigned actors travel, work, return and rest before ordinary reuse; the visible map labels these readiness states. | Observation | Corroborated | High | S1 text and two stills, S3 |
| DIS-004 | First injury reduces all five attributes by one for the shift; another sidelines the hero. Applicable immunity or healing changes this rule. Failure is not always injury, and heroes are not permanently killed by this shift. | Observation | Corroborated | High | S1, S5 |
| DIS-005 | Experience gives upgrade opportunities; earned points can improve attributes. Identity-specific starting powers have discovery conditions and alter eligible assignments, including solo, position, form and injury cases. | Observation | Corroborated | High | P1, S2, S3, S5 |
| DIS-006 | Some calls offer attribute-tested or character-exclusive responses and hacking alternatives. The final scripted intervention does not offer unrestricted branch control over its story result. | Observation | Corroborated | High | S2, S4 |
| DIS-007 | Hacking moves an avatar along a network. Directional build prompts reconfigure paths; some locks require a learned directional password. Selected hacks have a local timer under the admitted settings. | Observation | Corroborated | High | S2, S3, S6, S5 |
| DIS-008 | The first shift reaches Granny's Donuts and a performance review before the break-room scene. Non-perfect calls can still reach this continuation. | Observation | Corroborated | High | S1, S2, S3, S4 |
| DIS-009 | Current incidents, proposed fit, roster state and feedback are visible; future calls and the exact outcome algorithm are not fully disclosed. | Observation | Corroborated | High | P1, S1 stills, S2 |

## Basic data

- AdHoc Studio. Target: original full-season PS5 release, English.
- Families: agent routing and coordination, and real-time system pressure.
- Sources accessed 2026-11-19:
  - **P1** — [Official PlayStation product page](https://www.playstation.com/en-us/games/dispatch/),
    PS5 identity, deployment, roster improvement and offline pause availability.
    Its current accessibility inventory is not evidence for every 2025 patch.
  - **P2** — [AdHoc developer interview with Unreal Engine](https://www.unrealengine.com/developer-interviews/how-adhoc-used-unreal-engine-to-deliver-2025s-narrative-driven-hit-dispatch),
    17 April 2026, Dennis Lenart and Seth Kingsley; authored character/dispatch
    integration. It corroborates design, not exact hidden probabilities.
  - **S1** — [Alyssa Rochelle Payne's first-hand Episode 1/2 review](https://www.gamegrin.com/articles/dispatch-episode-1-and-episode-2-review-in-progress/),
    released episode review on Windows. The first-shift and call-map stills
    expose busy, returning and resting cards; its observations establish
    attributes, concurrent expiry, injuries and non-perfect completion.
  - **S2** — [Mahmud Munazil Rahman's Episode 2 walkthrough](https://intoindiegames.com/walkthroughs/dispatch-walkthrough-episode-2-onboard/),
    23 October 2025. First-shift ordering, conditional responses, route-building
    and both closing hacks. Mouse labels are not PS5 controls.
  - **S3** — [Cynic 0055's released-game achievement route](https://steamcommunity.com/sharedfiles/filedetails/?id=3622718795),
    Episode 2 and its continued section: initial roster, starter powers,
    upgrading, timed hack and distinction between finishing and a perfect shift.
    Its page-level power tally is not the initial number already known.
  - **S4** — [Damian Gacek's Episode 2 choice guide](https://www.gamepressure.com/newsroom/dispatch-episode-2-walkthrough-and-choices-guide/z78933),
    3 December 2025; call alternatives and fixed closing-story outcome.
  - **S5** — [PlayStation trophy route](https://www.playstationtrophies.org/game/dispatch/guide/),
    indexed console-oriented first-shift, starter-power and healing passages.
    The full origin request was restricted; indexed text is corroboration only.
  - **S6** — [Sweet Like Cupcake's hacking guide](https://steamcommunity.com/sharedfiles/filedetails/?id=3611723261),
    traversal, build prompts, password nodes and setting-dependent timers.
    Later antivirus systems and unlimited attempts are not imported here.
  - **S7** — [Hey Poor Player full PS5 review](https://www.heypoorplayer.com/2025/11/14/dispatch-review-ps5/),
    14 November 2025; explicitly confirms all eight episodes playable.
- Claim IDs: DIS-001–DIS-009.

## Mechanical decomposition

### Action Genes

- Reuse `ACT-008` for navigating the hack avatar along reachable routes.
- Reuse `ACT-106` for symbolic directional build and password entry.
- Reuse `ACT-191` for allocating earned attribute-development points.
- Reuse `ACT-232` for offered call and closing-intervention responses.
- Add `ACT-743` for committing available heroes to an incident's slots.
- Claim IDs: DIS-002, DIS-003, DIS-005–DIS-007.

### System Behaviour Genes

- Reuse `SYS-139` for the addressed directional password gate, `SYS-299`
  for experience thresholds and `SYS-773` for aggregate shift evaluation.
- Add `SYS-1577` for group suitability and contextual call resolution,
  `SYS-1578` for deployed/returning/resting readiness, `SYS-1579` for
  injury penalties and sidelining, `SYS-1580` for conditional hero powers,
  and `SYS-1581` for build-prompt changes to the traversable hack graph.
- Claim IDs: DIS-002–DIS-008.

### Constraint Genes

- Reuse `CON-597` for incident opportunities that close on expiry.
- Reuse `CON-068` for an admitted hack's local terminal deadline.
  This is not a whole-shift timer or automatic story failure.
- Slot limits and actor availability parameterise the dispatch/readiness
  rules; they do not justify separate one-game constraint duplicates.
- Claim IDs: DIS-003, DIS-007.

### Information Genes

- Reuse `INF-123` for inspectable hero profiles and `INF-148` for offered
  response prerequisites without every downstream consequence.
- Add `INF-526` for current incidents, proposed five-axis suitability
  and availability on the dispatch surface. Future calls remain concealed.
- Claim IDs: DIS-002, DIS-003, DIS-005, DIS-006, DIS-009.

### Objective Genes

- Add `OBJ-302` for reaching the finite shift's evaluated successor through
  the required closing intervention, without requiring a perfect record.
- Claim IDs: DIS-008.

### Time Genes

- Reuse `TIM-003` for the live map's overlapping work and expiring calls,
  plus timed local hacks while input remains possible. Paused menus do
  not advance the same live schedule. P1 supports explicit offline pause;
  exact automatic map suspension on every overlay remains unmeasured.
- Claim IDs: DIS-003, DIS-007, DIS-009.

## Starting-power boundary

The admitted initial identities have distinct conditional effects (S3, S5).
Flambae stacks Combat/Mobility after successes until failure; Sonar alternates
forms, swapping attribute pairs. Solo Invisigal shortens travel and work.
Coupé and Golem receive slot-dependent modifiers on sufficiently large calls.
Prism copies an adjacent hero into an empty slot at reduced attributes.
Punch Up is immune to injury penalties and cannot be downed; Malevola can
heal a fellow responder and gain a stacking attribute benefit. These are
conditional rules, not eight bonuses assumed active at entry. Ordinary
injury transitions below exclude Punch Up's exception. Later training powers
are excluded. The scope allows permitted assignments that reveal initial
powers; it does not require a perfect route that leaves injury powers hidden.

## Reproducible transitions

| Before | Input or event | Bounded resolution | What it establishes | Claim ID |
| --- | --- | --- | --- | --- |
| A current call has open responder slots | Inspect the needs and select available heroes | Proposed group fit changes; confirm to commit actors | Assignment differs from field control | DIS-002 |
| A hero is assigned or returning | Inspect another call | The actor is unavailable until the admitted return/rest state clears | Successful calls do not instantly refund availability | DIS-003 |
| A suitable hero is still resting | Wait on the running map past a call's interval | The opportunity can expire before the hero returns | Scheduling affects recorded results | DIS-003 |
| A call admits a contextual response | Pick a qualifying response or character-exclusive option | Apply its local resolution instead of an assumed universal roll | Identity and context can matter beyond raw totals | DIS-002, DIS-006 |
| A non-immune actor takes a first eligible injury | Inspect the hero | All five attributes have a one-point penalty | Injury changes later suitability | DIS-004 |
| An already injured non-immune actor takes another injury | Let the call resolve | The actor is sidelined for the shift | Two wounds are not cosmetic feedback | DIS-004 |
| An injured ally shares an eligible healing-power call | Meet the power's condition | Remove an eligible injury | Healing is a conditional exception | DIS-004, DIS-005 |
| Experience crosses an upgrade threshold | Open Upgrade and spend a granted point | Retain the chosen attribute improvement | XP and point allocation are separate transitions | DIS-005 |
| A solo or formation power condition is met | Form the eligible assignment | Discover and apply the identity-specific modifier | A starting power need not be known at entry | DIS-005 |
| Hack avatar reaches a build node | Enter the shown directional prompt | Change its route connections, then traverse the new branch | Solving one prompt does not finish the whole network | DIS-007 |
| A branch exposes a password | Learn it, reach the lock and enter its ordered directions | Open that gate and continue toward the terminal | Knowledge and code entry differ from route movement | DIS-007 |
| A timed hack is active with standard limits | Reach the terminal before expiry | Complete the local intervention; expiry is a local failure | Call expiry and hack timer are separate intervals | DIS-003, DIS-007 |
| The closing donut-shop incident begins | Follow the required hero intervention and both hacks | Reach its authored outcome and shift review | End-of-shift story is not an unrestricted tactical win | DIS-006, DIS-008 |
| Ordinary calls include a miss or failure | Finish the remaining shift | Review retains non-perfect outcomes and permits continuation | A perfect achievement is optional | DIS-008 |

These are documented-rule reconstructions, not a newly executed PS5 shift.

## Strategic and experiential structure

The best-looking responder may be unavailable when a call closes. Sending a
weaker available group can therefore compete with waiting for a stronger one.
A call's result changes both its record and the actors available afterward.
Injury makes that scheduling problem stateful; an upgrade or conditional power
can change the next proposed fit without replaying the previous call.

Hacking temporarily changes the kind of decision. The player navigates a
network, changes its connections and carries a learned code to a lock. This
is not automatic hero deployment or PRAGMATA's route extended during aiming.

## Replay and variation

Ordinary choices and results can differ while the closing story intervention
still reaches its authored continuation. The record does not treat a guide's
recommended hero as the only legal answer or a perfect run as the base goal.
A failed call can remain part of a completed shift. No exact RNG stream,
reload checkpoint or platform-specific save timing was independently tested.

## Adjacent systems and history

The workplace story surrounds the admitted shift, but romantic responses,
later dismissals and campaign endings are separate modules. Character powers
are admitted only where available to the initial roster; later upgrades and
antivirus stages cannot be inferred from a full-game guide's later chapters.

## Normalised genome

| Type | Genes | Scoped role |
| --- | --- | --- |
| Action | `ACT-008`, `ACT-106`, `ACT-191`, `ACT-232`, `ACT-743` | Hack traversal, directional entry, point spending, responses and dispatch |
| System Behaviour | `SYS-139`, `SYS-299`, `SYS-773`, `SYS-1577`, `SYS-1578`, `SYS-1579`, `SYS-1580`, `SYS-1581` | Codes, progression, evaluation, suitability, readiness, injury, powers and graph changes |
| Constraint | `CON-068`, `CON-597` | Local hack deadline and expiring incident opportunity |
| Information | `INF-123`, `INF-148`, `INF-526` | Profiles, offered prerequisites and live call surface |
| Objective | `OBJ-302` | Evaluated first-shift continuation |
| Time | `TIM-003` | Input while the admitted live schedule advances |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `544` (`GAME-0001`–`GAME-0544`).
- Exact genome matches: none.
- Tied near matches: `GAME-0252` — Detroit: Become Human (`5 / 32 = 0.156250`).
- Supported combination subsets: none.
- Scan date: 2026-11-19.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
| --- | --- | --- | --- |
| `GAME-0252` — Detroit: Become Human | `ACT-008`, `ACT-232`, `CON-597`, `INF-148`, `TIM-003` | Both navigate an authored intervention, choose contextual responses and face expiring opportunities. Detroit investigates one embodied hostage scene and retains its branch flowchart; Dispatch schedules multiple responders across calls, tracks return/rest, develops profiles and reconfigures separate hack networks before its shift review. | Near, `0.156250` |

### Preserved research notes

- New genes: `ACT-743`, `SYS-1577`–`SYS-1581`, `INF-526`, `OBJ-302`.
- Classification result: New gene.
- Evidence and reasoning: dispatch readiness and conditional powers differ from worker professions and field combat.

## Canonical genome

The front matter is authoritative: 20 genes, including eight new definitions.

## Taxonomy impact

- Twelve definitions are reused and eight are added.
- Registry changes: eight new Active definitions.
- Taxonomy-change record: [TAXONOMY_CHANGE_292](../../../research/taxonomy-changes/TAXONOMY_CHANGE_292.md).
- Candidate terms affected: none.

## Negative results

- none.

## Delta summary

## New facts

- [Observation | Corroborated | High] First-shift scheduling includes
  responder recovery, injuries, conditional powers and intervention choices.

## New genes

- [Observation | Corroborated | High] Eight additions separate dispatch,
  resolution, readiness, injuries, powers, graph changes, display and completion.

## New combinations

- [Observation | Corroborated | High] No new combination is proposed.

## Taxonomy changes

- [Observation | Corroborated | High] `TAXONOMY_CHANGE_292`.

## New questions

- What are the executable's exact call resolver and map suspension rules?
- Which PS5 patch first changed optional hacking limits or later challenge modes?

## Next recommended game

- [Hypothesis | Limited | Medium] Original Saturn Burning Rangers in
  [Selection 043](../../../research/selection/SEARCH_DEMAND_GAME_SELECTION_043.md).
- Optimisation criterion: change from dispatch scheduling to embodied rescue.
- Expected information gain: emergency response through route and fire handling.
- Backlog impact: advance to `GAME-0546`.

## Why this game

- [Hypothesis | Limited | Medium] A rescue stage should separate personal
  traversal and hazards from the dispatcher's abstract responder availability.
