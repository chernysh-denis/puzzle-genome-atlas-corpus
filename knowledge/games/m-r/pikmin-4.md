---
game_id: GAME-0035
slug: pikmin-4
game_title: Pikmin 4
analysis_status: reviewed
reviewed: 2026-08-12
combination_ids:
  - COMB-0034
  - COMB-0035
  - COMB-0041
gene_ids:
  action:
    - ACT-008
    - ACT-044
    - ACT-050
    - ACT-051
    - ACT-052
  system:
    - SYS-045
    - SYS-048
    - SYS-066
    - SYS-067
    - SYS-068
  constraint:
    - CON-076
    - CON-080
    - CON-081
  information:
    - INF-001
    - INF-021
  objective:
    - OBJ-023
  time:
    - TIM-003
    - TIM-007
---

# Game: Pikmin 4

## Analysis scope

- Version / ruleset: the 2023 base game, scoped to one ordinary single-player
  surface-day task after the Rescue Officer, Oatchi and multiple Pikmin types
  are available, with one treasure or castaway requiring several carriers and
  return to the S.S. Beagle.
- Included: direct Officer / Oatchi navigation; squad following and dismissal;
  type selection and throwing followers at contextual targets; whistle recall;
  switching leaders; type-specific traversal / hazard suitability; enemy loss;
  autonomous contextual work; carrying-strength threshold and route to base;
  base intake; active follower / type caps; visible task state; real-time day,
  pause and sunset loss; checkpoint-granularity Rewind Time.
- Excluded: narrative interpretation, hub progression beyond parameters,
  night expeditions, Dandori Battles and Challenges, co-op, caves except as a
  timing contrast, postgame, unrelated catalogue completion, achievements and
  platform-specific presentation.
- Direct-play status: not conducted. Nintendo's product site, official tips and
  creator interview establish the major transitions; contemporary reviews
  corroborate autosave rewind, Oatchi work and base transport. Exact mixed-
  strength speed curves and pathfinding tie-breaks remain parameters.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `PKM-001` | The player directly navigates the active Rescue Officer or Oatchi and may switch control between them after splitting their groups | Confirmed | Direct | High | P2, P3 |
| `PKM-002` | Nearby idle Pikmin follow the active leader; dismissal separates groups and a spatial whistle recalls eligible Pikmin | Confirmed | Direct | High | P1, P2 |
| `PKM-003` | The player selects a Pikmin type and throws followers onto a world target; the target context determines whether they fight, dig, build or carry | Confirmed | Corroborated | High | P1, P2, S3 |
| `PKM-004` | Assigned Pikmin execute their task and travel without continuous steering, then wait when finished until gathered | Confirmed | Direct | High | P1, P3 |
| `PKM-005` | A carried target moves only after attached eligible workers meet its displayed strength requirement; carriers then jointly route it to base | Confirmed | Direct | High | P1, P4, S1 |
| `PKM-006` | The S.S. Beagle accepts delivered treasure or castaways, credits Sparklium or rescue progress and releases the carriers | Confirmed | Corroborated | High | P1, P2, S1 |
| `PKM-007` | Pikmin types have different task, traversal and hazard suitability, so field composition changes reachable and efficient work | Confirmed | Direct | High | P2, P3, P4 |
| `PKM-008` | The ordinary field limits active follower headcount and allows no more than three Pikmin types at once | Confirmed | Direct | High | P4, S1 |
| `PKM-009` | Pikmin can die to hazards or enemies, and surface followers not safely returned by sunset are permanently lost while the campaign continues | Confirmed | Direct | High | P2, P3 |
| `PKM-010` | Surface-day agents, tasks, combat and transport advance in real time, but map, options and selected scouting tools pause the clock | Confirmed | Direct | High | P2, P3 |
| `PKM-011` | Rewind Time lets the player choose an earlier automatically saved state from minutes ago and replay a different continuation | Confirmed | Direct | High | P2, P3, P5, S1, S2 |
| `PKM-012` | Rewind is checkpoint restoration rather than continuous scrubbing or exact future seeking; no commands are edited at timestamps | Confirmed | Corroborated | High | P2, P5, S1, S2 |
| `PKM-013` | Pikmin carrying is autonomous cooperative work, not direct avatar-held object manipulation, squad relocation or Lemmings-style abstract role assignment | Confirmed | Corroborated | High | PKM-003–PKM-006 |
| `PKM-014` | The transported castaway or treasure is the credited target; the carrier population itself is not the rescue objective | Confirmed | Corroborated | High | P1, P2, PKM-005–PKM-006 |

## Basic data

- Release / origin: Nintendo released Pikmin 4 for Nintendo Switch on 21 July
  2023.
- Platform or physical form: real-time, pauseable three-dimensional
  exploration / task-allocation puzzle with a directly navigated leader and
  autonomous typed followers.
- Puzzle family: cooperative follower-task allocation and base extraction.
- Nintendo official sources:
  - **[P1]** [Pikmin 4 official site](https://pikmin4.nintendo.com/), describing
    growing, guiding and gathering Pikmin, assigning object carrying, waiting
    after task completion, treasures / castaways, daily return and Rewind Time.
  - **[P2]** [Nintendo — Explore to the fullest tips](https://www.nintendo.com/au/news-and-articles/explore-to-the-fullest-with-these-pikmin-4-tips/),
    documenting type / enemy suitability, Oatchi rush and command, independent
    Oatchi groups, sunset loss, rewind and paused / slowed cave time.
  - **[P3]** [Nintendo — Guide for Fresh Recruits](https://www.nintendo.com/us/whatsnew/pikmin-4-guide-for-fresh-recruits/),
    documenting faster carrying, Oatchi commands, target lock, whistle safety,
    pause controls, autosave points and restart from an earlier moment.
  - **[P4]** [Nintendo product page](https://www.nintendo.com/en-ca/store/products/pikmin-4-switch/),
    confirming the maximum of three active Pikmin types; the official site's
    carrying example visibly declares a seven-Pikmin strength requirement.
  - **[P5]** [Nintendo Ask the Developer Vol. 10, Chapter 2](https://www.nintendo.com/au/news-and-articles/ask-the-developer-vol-10-pikmin-4-chapter-2/),
    explaining minutes-back rewind, alternate strategy experimentation, no
    campaign-wide day limit and player-chosen Pikmin order / approach.
- Contemporary corroboration:
  - **[S1]** [GamesRadar+ review](https://www.gamesradar.com/pikmin-4-review/),
    documenting earlier-state replay, carried treasures, movable base positions
    and Oatchi transport across water.
  - **[S2]** [GameSpot review](https://www.gamespot.com/reviews/pikmin-4-review-veggie-might/1900-6418090/),
    identifying automatic save points every few minutes, Rewind Time, Oatchi
    digging / carrying and mass Pikmin dispatch in combat.
  - **[S3]** [Axios review](https://www.axios.com/2023/07/19/pikmin-4-review),
    describing up to 100 commanded Pikmin, following, throwing, fighting and
    hauling targets as delegated work.
- Claim IDs: `PKM-001`–`PKM-014`.

## Mechanical decomposition

### Action Genes

- `ACT-008` — navigate controllable agent. Local movement directly steers the
  currently active Rescue Officer or Oatchi through the surface area.
- `ACT-044` — rewind recent simulation history. The player selects a retained
  automatic save point from minutes earlier and restores it before trying a
  different action sequence; checkpoint granularity is a parameter.
- `ACT-050` — commit selected follower to contextual target task. Throwing the
  selected Pikmin type onto a treasure, castaway, enemy or work object assigns
  that recipient to the task inferred from the target.
- `ACT-051` — recall nearby followers from autonomous tasks. The active leader
  blows a bounded whistle to gather eligible Pikmin back to its squad.
- `ACT-052` — switch direct control between field leaders. After disbanding,
  control can transfer between Oatchi and the Officer, each retaining location
  and followers.
- `ACT-036` is absent: the player does not first select an abstract role such
  as Builder and then one recipient; task identity is target-derived.
- `ACT-014` is absent: throwing dispatches followers, after which locomotion and
  work resolve rather than directly placing a squad at a legal destination.
- `ACT-048` is absent: neither leader holds the treasure at a controlled offset.
- Claim IDs: `PKM-001`–`PKM-003`, `PKM-011`–`PKM-013`.

### System Behaviour Genes

- `SYS-045` — continuous autonomous agent locomotion. Tasked Pikmin travel,
  carry and respond to terrain while the field clock runs.
- `SYS-048` — terminal-zone population accounting. Enemy / hazard death or
  unsafe sunset status removes affected followers and updates the surviving
  population; the carriers are not credited as delivered targets.
- `SYS-066` — context-derived follower task execution. Dispatched Pikmin infer
  fight, dig, build or transport from the assigned target and work without
  continuous steering.
- `SYS-067` — strength-threshold cooperative carrying. Transport waits until
  assigned carrying strength meets target weight, then the carrier group
  follows a route to the Beagle; added strength can improve delivery speed.
- `SYS-068` — base intake of transported world object. Arrival removes and
  credits treasure / castaway while freeing carriers from the task.
- `SYS-046` is absent because no separately selected role controls execution.
  `SYS-047` is absent because active Pikmin are withdrawn, grown or plucked by
  player-mediated preparation rather than released on an automatic cadence.
- Resolution order: dispatch determines target and task; eligibility and
  carrying contribution are evaluated; enough strength starts group transport;
  live pathfinding, hazards and combat update; base contact credits the target
  or lethal / sunset conditions account for followers.
- Claim IDs: `PKM-003`–`PKM-006`, `PKM-009`, `PKM-013`, `PKM-014`.

### Constraint Genes

- `CON-076` — actor-specific traversal and interaction permissions. Pikmin
  types provide different hazard resistance, reach, strength and task
  suitability; Oatchi has separately trained movement / work permissions.
- `CON-080` — finite active follower and type capacity. A field roster has an
  upgradable headcount cap and no more than three active Pikmin types, requiring
  composition choices before and during work.
- `CON-081` — day-end off-squad follower loss. Sunset ends the surface work
  interval and permanently removes vulnerable Pikmin not returned to safety,
  without failing the larger campaign.
- `CON-067` is absent: followers are reusable agents occupied by tasks, not
  consumed per-role stock. `CON-071` is absent because individual Pikmin can be
  dispatched and recalled rather than only a commander-led squad receiving one
  destination.
- Scarce strategic resources: field slots, three type slots, idle carrying
  strength, safe return time, Oatchi / Officer attention and followers exposed
  to loss.
- Claim IDs: `PKM-007`–`PKM-010`, `PKM-013`.

### Information Genes

- `INF-001` — fully visible current state. The field, active leaders, follower
  types / counts, target, current workers, day clock, routes already explored
  and transport state are inspectable; the radar pauses time.
- `INF-021` — visible cooperative-work capacity state. A carry target exposes
  its required strength and current assigned contribution before and during
  transport.
- Route choice beyond visible / mapped terrain is not guaranteed as an exact
  prospective projection, so `INF-017` is absent.
- Claim IDs: `PKM-005`, `PKM-008`–`PKM-010`.

### Objective Genes

- `OBJ-023` — extract designated world objects to operational base. Progress
  comes from delivering finite treasures for Sparklium or immobile castaways
  for rescue credit to the Beagle.
- `OBJ-014` is absent: the payload moves through assigned autonomous carriers,
  not force trajectory altered by environmental interventions, and one arrival
  need not end the expedition.
- `OBJ-019` and `OBJ-022` are absent: Pikmin are the transport workforce, not
  the rescue quota; castaways are carried objects rather than directly
  controlled actors reaching exits.
- Claim IDs: `PKM-005`, `PKM-006`, `PKM-014`.

### Time Genes

- `TIM-003` — real-time input during forced progression. Followers work,
  transport and fight while the surface day advances; opening the radar /
  options pauses this schedule as a rate-control parameter.
- `TIM-007` — branchable player-reversible simulation history. Selecting an
  earlier autosave restores the authoritative field state and a new command
  sequence replaces the discarded outcome.
- This is not continuous Braid scrubbing, but restoration granularity does not
  change the branch-replacement invariant. `TIM-008` is absent because no
  prospective future or timestamped command schedule can be edited.
- Claim IDs: `PKM-009`–`PKM-012`.

## Reproducible transitions

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Selected Red Pikmin follow the Officer near a treasure | Throw one or more at the treasure | Each attaches as a contextual carrier candidate; no direct object hold occurs | target-derived assignment differs from role selection and direct carrying | `PKM-003`, `PKM-013` |
| Assigned strength is below displayed target weight | Wait | Object remains in place while assigned carriers stay committed | carry threshold is a rule, not animation delay | `PKM-005` |
| Final required strength joins the object | Give no path command | Carrier group lifts the object and autonomously routes toward the Beagle | cooperative transport begins automatically at threshold | `PKM-004`, `PKM-005` |
| Carried treasure reaches the Beagle | Wait for intake | Treasure leaves field, Sparklium is credited and carriers become available | payload intake is distinct from carrier accounting | `PKM-006`, `PKM-014` |
| Several idle Pikmin wait after finished work | Blow whistle within range | Eligible followers rejoin the active leader's squad | recall is a bounded command, not global unit selection | `PKM-002`, `PKM-004` |
| Officer and Oatchi have been disbanded with separate groups | Choose Switch | Direct navigation / command authority transfers; both world states persist | two field leaders are alternately controlled, not remotely scheduled | `PKM-001` |
| Water route blocks a vulnerable type | Assign unsuitable type or ride trained Oatchi with the group | Type permission rejects / endangers the first route; Oatchi can provide a distinct allowed route | follower type changes reachability | `PKM-007` |
| Distant Pikmin remain outside safety near sunset | Let field clock expire | Those followers are lost and the campaign advances to another day | day deadline penalises roster without making the campaign attempt fail | `PKM-009`, `PKM-010` |
| Several Pikmin died after a poor command | Open options and choose an earlier Rewind Time state | Earlier autosave replaces current field; new dispatches can produce another result | checkpoint selection still creates branchable restored history | `PKM-011`, `PKM-012` |

## Strategic and experiential structure

- Local decision: choose leader, follower type, target and number of committed
  workers, or recall them before loss.
- Medium-term planning: split Officer and Oatchi, allocate limited types and
  headcount across parallel work, and ensure each transport path has enough
  strength and hazard compatibility.
- Long-term structure: convert a finite workday into maximum durable extraction
  while preserving enough of the reusable workforce for future days.
- Common heuristics: expose the path before assigning carriers, meet but do not
  greatly exceed low-priority weights, use extra strength where speed matters,
  keep one leader free to whistle stragglers and rewind the earliest bad split.
- Failure attribution: visible counts, task icons, weight threshold, time and
  checkpoint snapshots tie failure to composition, commitment, path, hazard or
  sunset timing rather than hidden randomness.
- Player-trust factors: target lock, automatic assignment stop, strength sums,
  carrier routing, whistle interruption, Oatchi equivalence and autosave
  restoration must be predictable.
- Claim IDs: `PKM-001`–`PKM-014`.

## Replay and variation

- What changes between days / areas: available Pikmin types and counts, Oatchi
  skills, base location, targets, weights, terrain, hazards and explored map.
- Randomness or procedural generation: none asserted for the scoped authored
  surface task.
- Multiple viable strategies: type mix, leader split, carrier allocation,
  target order, route and rewind use can differ; Nintendo explicitly frames
  Dandori as supporting multiple approaches.
- Typical replay motive: reduce losses, improve parallelism, deliver more
  within a day or retry from an earlier checkpoint with a better task split.
- Claim IDs: `PKM-003`–`PKM-012`.

## Adjacent systems and history

- Lemmings also assigns work to autonomous followers under live time, but
  spends explicit finite role stock on selected individuals. Pikmin tasks are
  contextual, followers are reusable and carrying requires cooperative strength.
- HUMANITY also combines a directly navigated leader-like avatar with a crowd,
  but writes persistent world commands for every later crosser rather than
  dispatching particular followers onto targets.
- Bad North relocates commander-led squads as indivisible command units;
  Pikmin 4 permits individual dispatch, cooperative task formation and recall.
- Portal directly holds and releases one rigid cube; Pikmin 4 leaves the target
  in world state while autonomous carriers meet a threshold and pathfind.
- Tin Hearts shares checkpoint-compatible branchable rewind, live autonomous
  motion and population loss accounting, but manipulates routing devices around
  walkers rather than assigning workers to extraction tasks.
- Claim IDs: `PKM-001`–`PKM-014`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-044`, `ACT-050`, `ACT-051`, `ACT-052` | leader navigation / switching, dispatch, recall and rewind |
| System Behaviour | `SYS-045`, `SYS-048`, `SYS-066`, `SYS-067`, `SYS-068` | autonomous work, carrying, intake and loss accounting |
| Constraint | `CON-076`, `CON-080`, `CON-081` | type permissions, roster cap and sunset safety |
| Information | `INF-001`, `INF-021` | visible field and work-capacity state |
| Objective | `OBJ-023` | finite object / castaway extraction to base |
| Time | `TIM-003`, `TIM-007` | live day and checkpoint branch restoration |

Canonical signature:

`ACT-008,ACT-044,ACT-050,ACT-051,ACT-052; SYS-045,SYS-048,SYS-066,SYS-067,SYS-068; CON-076,CON-080,CON-081; INF-001,INF-021; OBJ-023; TIM-003,TIM-007`

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `34` (`GAME-0001`–`GAME-0034`).
- Exact genome matches: none.
- Tied near matches: `GAME-0030` — Tin Hearts (`6 / 26 = 0.230769`); `GAME-0034` — Braid, Anniversary Edition (`6 / 26 = 0.230769`).
- Supported combination subsets: `COMB-0034`, `COMB-0035`, `COMB-0041`.
- Scan date: 2026-08-12.

### Selected-neighbour interpretation

No pre-migration reviewed selected-neighbour table row exists for: `GAME-0030`, `GAME-0034`.

## Combination record

- Registered `COMB-0035` — contextual cooperative follower extraction.
- Also added Pikmin 4 to recurring `COMB-0034`; checkpoint rather than
  continuous rewind remains inside the existing restoration-granularity
  parameter.

## Taxonomy impact

- Registry changes: ten stable genes added; eight existing genes reused.
- `CON-076` is generalised from two controlled characters to typed controlled
  or commanded actor classes with complementary traversal / interaction
  permissions; its reachability boundary is unchanged.
- `ACT-044` and `TIM-007` explicitly admit discrete retained checkpoint
  selection as a restoration-granularity parameter when new play replaces the
  discarded continuation.
- Taxonomy-change record: none; no prior signature or lifecycle changes.

## Negative results

- `ACT-036` / `SYS-046` are rejected because task identity is inferred from a
  world target rather than selected from an abstract role catalogue.
- `ACT-014`, `CON-071` and `ACT-048` are rejected because followers are
  individually committed and autonomously carry; neither squad nor object is
  directly relocated.
- `SYS-047` and `CON-067` are rejected because field followers are not released
  automatically or consumed as role-use stock.
- `OBJ-014`, `OBJ-019` and `OBJ-022` are rejected because the target object /
  castaway, not the carrier population or directly controlled actors, is
  credited at base.
- `CON-068` is rejected because sunset does not make the campaign attempt fail;
  it ends one work interval and loses unsafe followers.
