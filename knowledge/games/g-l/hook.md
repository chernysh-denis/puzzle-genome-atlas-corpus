---
game_id: GAME-0060
slug: hook
game_title: HOOK
analysis_status: reviewed
reviewed: 2026-08-13
combination_ids:
  - COMB-0060
gene_ids:
  action:
    - ACT-072
  system:
    - SYS-103
  constraint:
    - CON-054
    - CON-106
  information:
    - INF-001
  objective:
    - OBJ-007
  time:
    - TIM-001
---

# Game: HOOK

## Analysis scope

- Version / ruleset: Maciej Targoni's original released HOOK, restricted to
  levels 1–7, the complete introductory mechanism set before junction boxes,
  rotatable line switching, wireless receivers and time-sensitive switching.
- Included: one fixed abstract board; visible circular triggers; one or several
  visible lines and hook-ended mechanisms linked to each trigger; pressing one
  trigger; automatic withdrawal toward that trigger; permanent disappearance
  after an unobstructed withdrawal; collision when a retracting line or hook
  meets a still-active mechanism; immediate attempt reset after collision;
  complete board clearance; self-paced deterministic retries.
- Excluded: level 8 onward; junction boxes and rotatable routing; wireless
  transmitter / receiver links; timing a rotation during active retraction;
  later compound networks; HOOK 2 and Complete Edition additions; achievements,
  soundtrack, platform features, level numbering beyond the selected boundary
  and presentation.
- Direct-play status: not conducted. The creator's product pages establish the
  remove-all-hooks objective, untimed play and original title. A contemporary
  design analysis documents the exact level 1–7 progression, one-to-many trigger
  linkage, obstruction collision and dependency order. Two contemporary hands-
  on reviews independently corroborate retraction, disappearance, reset and the
  later-mechanism exclusion boundary.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `HOK-001` | The scoped first seven levels teach the original trigger, retraction, obstruction and one-to-many linkage before later routing devices | Confirmed | Corroborated | High | P1, S1-S3 |
| `HOK-002` | Every scoped board visibly exposes its current triggers, lines, hooks, crossings and linkages | Observation | Corroborated | High | S1-S3 |
| `HOK-003` | One action presses one circular trigger rather than dragging a line or hook | Confirmed | Corroborated | High | S1-S3 |
| `HOK-004` | A pressed trigger automatically retracts every mechanism currently attached to it toward the trigger | Confirmed | Corroborated | High | S1, S2 |
| `HOK-005` | A mechanism disappears after an unobstructed retraction and cannot return during ordinary forward play | Confirmed | Corroborated | High | S1-S3 |
| `HOK-006` | A retracting line or hook colliding with a still-present mechanism rejects the chosen order | Confirmed | Corroborated | High | S1-S3 |
| `HOK-007` | Collision resets the current authored level, restoring removed mechanisms | Confirmed | Corroborated | High | S2, S3 |
| `HOK-008` | Completion requires every hook-and-line mechanism to be removed from the board | Confirmed | Direct | High | P1, P2, S2 |
| `HOK-009` | Levels are self-paced, deterministic and have no score or time restriction | Confirmed | Direct | High | P1, P2, S2 |
| `HOK-010` | Level 7 introduces one trigger controlling multiple wires in the same automatic action | Confirmed | Direct | High | S1 |

## Basic data

- Release / origin: Polish solo developer Maciej Targoni first published the
  small browser version in October 2014 and released the commercial original on
  25 January 2015.
- Platform or physical form: deterministic single-player digital mechanism-
  ordering puzzle controlled by one-click triggers.
- Puzzle family: dependency-ordered line-and-hook retraction.
- Primary sources:
  - **[P1]** [Rainbow Train — Hook](https://www.rainbowtrain.eu/hook), the
    creator's current product page, for the original game's identity, remove-
    all-hooks goal, untimed / unscored design and separation from HOOK 2.
  - **[P2]** [HOOK on Steam](https://store.steampowered.com/app/367580/), for
    developer, release, single-player boundary and the same remove-all-hooks,
    no-time-restriction objective.
- Contemporary and reproducible corroboration:
  - **[S1]** Brendan Caldwell,
    [Learning the Ropes with Hook](https://haywiremag.com/columns/due-diligence-learning-the-ropes-with-hook/),
    for the exact level 1–7 tutorial sequence, trigger press, retraction,
    disappearance, collision, one-to-many linkage and partial-order example.
  - **[S2]** Lory Gil,
    [Hook review](https://www.idownloadblog.com/2015/01/29/hook-review/), for
    trigger buttons, automatic reeling, obstruction, restart, clear-board
    completion, no scoring and later rotatable switchers.
  - **[S3]** Jason Bouwmeester,
    [HOOK review](https://techaeris.com/2015/09/25/hook-review-refreshing-change-pace/),
    for hook-on-line collision, level reset, later switches, wireless links and
    crossing-depth order.
- Claim IDs: `HOK-001`–`HOK-010`.

## Mechanical decomposition

### Action Genes

- `ACT-072` — activate addressed mechanism trigger. The player taps one visible
  circular trigger; the trigger identity supplies the complete linked mechanism
  set, so the player does not separately choose a line, motion path or target.
- Parameters: input gesture, trigger position, one-to-many linkage and whether
  the trigger remains after an unsuccessful withdrawal.
- Claim IDs: `HOK-003`, `HOK-004`, `HOK-010`.

### System Behaviour Genes

- `SYS-103` — linked hook retraction with swept obstruction adjudication. The
  system begins every line attached to the selected trigger, retracts each one
  toward that trigger, removes the completed set if all sweeps remain clear, or
  produces collision feedback and resets the authored board if any moving hook
  meets a still-present mechanism.
- Resolution order: resolve selected trigger's linked set; begin declared
  withdrawals; test complete moving footprints against active geometry; remove
  the successful linked set or restore the original level after collision;
  evaluate whether any target remains; accept the next input only after the
  transition ends.
- Parameters: retraction distance, speed, linked-set concurrency, hook shape,
  crossing depth, collision classes and reset delay.
- Claim IDs: `HOK-004`–`HOK-007`, `HOK-010`.

### Constraint Genes

- `CON-054` — forward-only monotonic active-set reduction. Each successful
  trigger removes its non-empty linked set; no ordinary accepted action adds a
  mechanism or restores one. The registry wording is generalised from an exact
  one-peg decrement to a non-empty bounded removal, preserving Peg Solitaire's
  instance while admitting HOOK's one-to-many level 7 trigger.
- `CON-106` — unobstructed swept withdrawal path. A trigger is useful now only
  if the full moving footprint of each linked line can reach its trigger without
  colliding with any still-active line, hook or mechanism.
- `CON-011` is absent: the constraint concerns an entire swept trajectory, not
  occupancy of one addressed destination cell.
- Scarce strategic resource: safe currently available sinks in the visible
  dependency graph; there is no finite move allowance.
- Claim IDs: `HOK-004`–`HOK-007`, `HOK-010`.

### Information Genes

- `INF-001` — fully visible current state. Every current trigger, linkage, line,
  hook, crossing and remaining blocker in the scoped levels is visible before a
  press. No concealed future event changes the dependency graph.
- Claim IDs: `HOK-002`, `HOK-006`, `HOK-009`.

### Objective Genes

- `OBJ-007` — clear declared board-element targets. The creator declares every
  hook as the target set; a level completes only after the final visible linked
  mechanism disappears. The existing gene already covers every visible member
  of a declared class and therefore needs only another included example.
- There is no score, authored move target or time objective in scope.
- Claim IDs: `HOK-008`, `HOK-009`.

### Time Genes

- `TIM-001` — discrete turn with automatic resolution. One trigger press fully
  resolves retraction, removal or collision-and-reset before the next trigger
  can be meaningfully selected.
- Although the animation occupies real time, the first seven levels do not ask
  the player to intervene during it; later timing puzzles are excluded.
- Claim IDs: `HOK-003`–`HOK-010`.

## Reproducible transitions

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| One line joins one circular trigger and its hook path is empty | Press that trigger | The line retracts to the circle, fades and disappears | A press commands automatic removal rather than direct dragging | `HOK-003`–`HOK-005` |
| Hook A curves around still-present line B | Press A's trigger | A starts withdrawing, strikes B and the authored level is restored | Useful action legality depends on the complete current sweep | `HOK-006`, `HOK-007` |
| Hook A curves around line B, but B's trigger is pressed first | Press B, then A after B disappears | B withdraws safely; A's formerly blocked sweep is clear and also disappears | Removal changes the dependency graph and creates a new available action | `HOK-005`, `HOK-006` |
| Level 7 trigger X controls two unblocked wires | Press X | Both linked wires retract and disappear in one resolved action | Trigger identity can fan out to several mechanisms | `HOK-004`, `HOK-010` |
| Two independent outer lines block a central hook | Remove both outer lines in either order | The central trigger becomes safe only after both predecessors disappear | Solutions are partial orders, not necessarily one total order | `HOK-006`, `HOK-010` |
| One final mechanism remains and its sweep is clear | Press its trigger | It disappears and the next level is presented | Completion is exhaustive board-element removal | `HOK-008` |

## Strategic and experiential structure

- Local decision: identify which visible trigger's complete linked withdrawal
  is unobstructed in the current board.
- Medium-term planning: remove independent blockers without destroying the
  mental model of which deeper line each one releases.
- Long-term structure: repeatedly choose a sink of the current obstruction
  graph until its active node set is empty.
- Common heuristics: trace each line from circle to hook; check every part of
  the swept path rather than only the endpoint; remove visually upper or outer
  blockers first; treat one-to-many triggers as a shared atomic action.
- Failure attribution: collision follows directly from visible current
  geometry and the selected trigger; no random event changes the result.
- Player-trust factors: linkage, crossing depth, moving hook footprint,
  successful disappearance and reset feedback must remain distinguishable.
- Claim IDs: `HOK-002`–`HOK-010`.

## Replay and variation

- What changes between scoped levels: number and geometry of lines, hook
  orientation, crossings, trigger link multiplicity and dependency depth.
- Randomness or procedural generation: none in the seven authored levels.
- Multiple viable strategies: independent unblocked mechanisms can be removed
  in either order; genuine blocker chains still impose precedence.
- Typical replay motive: recover immediately after a collision or revisit a
  solved level for its mechanism sequence; no score or move rating demands
  optimisation.
- Claim IDs: `HOK-001`, `HOK-006`–`HOK-010`.

## Adjacent systems and history

- Direct successor: HOOK 2 moves the core into a spatial perspective and is a
  separate ruleset.
- Later original-game systems: rotatable junction boxes, wireless receivers and
  timing-sensitive changes expand the trigger-to-mechanism mapping beyond this
  introductory boundary.
- Similar systems: prerequisite graphs and topological elimination, expressed
  here through physical-looking line sweeps rather than explicit arrows.
- Important difference from Railbound: the player does not construct a network
  and then run several vehicles; each press immediately removes fixed mechanism
  material. Difference from Shogun Showdown: there is no editable execution
  queue. Difference from Peg Solitaire: the selected element removes its linked
  mechanism set through a swept clearance predicate rather than a local jump.
- Claim IDs: `HOK-001`–`HOK-010`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-072` | addressed circular trigger and linked-set identity |
| System Behaviour | `SYS-103` | automatic withdrawal, disappearance or reset |
| Constraint | `CON-054`, `CON-106` | monotonic active-set reduction and swept clearance |
| Information | `INF-001` | complete visible mechanism graph |
| Objective | `OBJ-007` | remove every hook-and-line target |
| Time | `TIM-001` | one press fully resolves before another decision |

Canonical signature:

`ACT-072; SYS-103; CON-054,CON-106; INF-001; OBJ-007; TIM-001`

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `59` (`GAME-0001`–`GAME-0059`).
- Exact genome matches: none.
- Tied near matches: `GAME-0019` — Peg Solitaire (`3 / 14 = 0.214286`).
- Supported combination subsets: `COMB-0060`.
- Scan date: 2026-08-13.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0019` — Peg Solitaire | `CON-054`, `INF-001`, `TIM-001` | Peg removes exactly one bounded material instance per jump while preserving a peg-movement topology; HOOK removes a trigger-linked non-empty mechanism set only after its swept path is clear | Near, `0.214286` |

### Preserved research notes

- New genes: `ACT-072`, `SYS-103`, `CON-106`.
- Generalised gene: `CON-054` from exact one-element material decrement to a
  non-empty bounded active-set removal per successful action.
- Classification result: new combination with three new genes and four reused
  genes.
- Evidence and reasoning: no prior action commands one addressed trigger's
  linked mechanism set; no system gene combines withdrawal, swept collision,
  disappearance and attempt reset; and no constraint captures obstruction over
  the complete moving withdrawal footprint.

## Taxonomy impact

- Registry changes: add `ACT-072`, `SYS-103`, `CON-106`; generalise `CON-054`
  representation-neutrally without changing Peg Solitaire's signature.
- Taxonomy-change record: none. The old instance remains a strict one-element
  case of the clarified non-empty bounded removal.
- Candidate terms affected: promote addressed mechanism triggering, linked hook
  retraction and unobstructed swept withdrawal; map monotonic mechanism removal
  to `CON-054`.

## Negative results

- `ACT-049` rejected: no locally navigated avatar operates a world switch.
- `ACT-065` and `ACT-066` rejected: the player neither edits nor releases a
  prepared command queue.
- `TIM-006` and `TIM-009` rejected: there is no separately committed machine
  design followed by a locked multi-cycle run.
- `CON-102` rejected: collision is between one triggered moving footprint and
  still-active fixed mechanism geometry, not synchronous vehicle occupancy.
- `none` as a separate negative-result record; these are local boundary tests.
