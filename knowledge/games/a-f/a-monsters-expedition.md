---
game_id: GAME-0054
slug: a-monsters-expedition
game_title: A Monster’s Expedition
analysis_status: reviewed
reviewed: 2026-08-13
combination_ids:
  - COMB-0044
  - COMB-0054
gene_ids:
  action:
    - ACT-008
    - ACT-009
  system:
    - SYS-096
    - SYS-097
  constraint:
    - CON-001
    - CON-011
    - CON-012
    - CON-013
  information:
    - INF-001
  objective:
    - OBJ-026
  time:
    - TIM-001
---

# Game: A Monster's Expedition

## Analysis scope

- Version / ruleset: Draknek & Friends' released base game, scoped to the
  complete introductory single-log stopper lesson: one monster, one tree that
  becomes a log, one fixed rock or stump used to stop lateral rolling, a
  one-cell water gap and the immediately connected target shore.
- Included: direct cardinal walking; pushing the tree down; end-tipping and
  side-rolling one log; maximal rolling until an obstacle or water; log
  orientation; fixed land, rock, stump and water occupancy; correct and wrong
  water settlement; persistent bridge creation; crossing to the target shore;
  visible local state; discrete undo and island reset as recovery controls.
- Excluded: every later island and multi-log composition; rafts, raft travel and
  overworld routing; snow, ice and every later traversal rule; optional museum
  exhibits, postgame, narrative interpretation, achievements, secrets,
  optimisation and presentation.
- Direct-play status: not conducted. The official product page and creator
  interview establish tree pushing, log motion and the authored introductory
  progression. Contemporary mechanical accounts independently establish end
  tipping, maximal side rolling, obstacle stops, orientation-sensitive water
  bridges, undo and reset. The scope is a reproducible introductory lesson, not
  a claim about a numbered island or a universal campaign configuration.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `AME-001` | The scoped lesson is a fixed local land-and-water puzzle with one directly moved monster and one tree-derived log | Confirmed | Corroborated | High | P1, P2, S1–S4 |
| `AME-002` | The monster walks cardinally through free land cells and pushes only from a locally reachable adjacent side | Confirmed | Corroborated | High | P2, S1–S4 |
| `AME-003` | Pushing a standing tree knocks it into an elongated log whose current axis affects later responses | Confirmed | Corroborated | High | P1, P2, S1–S3 |
| `AME-004` | An end push tips the log through one local footprint transition, while a side push rolls it along the perpendicular axis | Confirmed | Corroborated | High | P2, S1–S4 |
| `AME-005` | A side roll continues automatically until a rock, stump or water stops it | Confirmed | Corroborated | High | P2, S1–S4 |
| `AME-006` | A lengthwise log entering a compatible one-cell water gap settles as a persistent bridge the monster can cross | Confirmed | Corroborated | High | P1, P2, S1–S4 |
| `AME-007` | Water entry in an unusable orientation can consume access to the only log while leaving ordinary walking available | Observation | Corroborated | High | S1, S3, S4 |
| `AME-008` | The local terrain, log pose, stopper, water gap and target shore are visible before each command | Observation | Corroborated | High | P2, S1–S4 |
| `AME-009` | One input resolves walking or the complete tip, maximal roll, water settlement and completion check before the next input | Observation | Corroborated | High | P2, S1–S4 |
| `AME-010` | The bounded task is credited by reaching the shore made traversable by the constructed bridge, not by displaying a log pose alone | Confirmed | Corroborated | High | P1, S1–S4 |
| `AME-011` | Undo or island reset restores state but does not expose a freely editable simulation timeline | Confirmed | Corroborated | High | S2–S4 |
| `AME-012` | The log bridge changes traversable world topology directly; it does not edit a map representation or spend abstract bridge inventory | Observation | Corroborated | High | AME-003–AME-010 |

## Basic data

- Release / origin: Draknek & Friends published A Monster's Expedition on 10
  September 2020; Alan Hazelden was creative director and lead puzzle designer,
  while Benjamin Davis was lead programmer and co-designed the prototype.
- Platform or physical form: deterministic single-player digital grid puzzle
  presented as an open-world island expedition.
- Puzzle family: direction-conditioned rigid-log manipulation and traversal-
  creating bridge construction.
- Primary and creator sources:
  - **[P1]** [Official A Monster's Expedition site](https://www.monsterexpedition.com/),
    identifying the released game, team and open-world puzzle premise.
  - **[P2]** Alan Hazelden and Benjamin Davis,
    [creator interview with Game Developer](https://www.gamedeveloper.com/game-platforms/the-relaxing-open-world-puzzle-design-of-i-a-monster-s-expedition-i-),
    documenting the original tree-flipping prototype, the rule that logs roll
    until stopped, iterative introductory puzzle design and persistent island
    dependencies. Its later open-world systems remain outside this scope.
  - **[P3]** [Official Steam product page](https://store.steampowered.com/app/1052990/A_Monsters_Expedition_Through_Puzzling_Exhibitions/),
    confirming the 10 September 2020 release, developer / publisher and the
    released product's tree-pushing island-path premise.
- Contemporary mechanical corroboration:
  - **[S1]** [PC Gamer review](https://www.pcgamer.com/a-monsters-expedition-deserves-a-place-alongside-the-puzzle-game-greats/),
    describing tree knockdown, end movement, side rolling until obstacle or
    water and bridge formation across islands.
  - **[S2]** [Pocket Gamer review](https://www.pocketgamer.com/a-monsters-expedition/review/),
    corroborating the grid, stump / rock stopping geometry, water bridges,
    unlimited undo and local reset.
  - **[S3]** [Scientific Gamer mechanical analysis](https://scientificgamer.com/thoughts-a-monsters-expedition/),
    distinguishing end tipping from side rolling, recording roll-until-stop,
    orientation-sensitive one-water-gap bridges and the introductory rock-
    stopper lesson.
  - **[S4]** [Nintendo World Report review](https://www.nintendoworldreport.com/review/58185/a-monsters-expedition-switch-review),
    corroborating log manipulation, rocks / stumps, bridge traversal, visible
    island puzzles and saved progress.
- Claim IDs: `AME-001`–`AME-012`.

## Mechanical decomposition

### Action Genes

- `ACT-008` — navigate controllable agent. One cardinal input moves the monster
  through an adjacent free land or completed-bridge position so it can reach a
  chosen side of the tree or cross to the target shore.
- `ACT-009` — push adjacent movable object. Moving toward the adjacent tree or
  log commands that one object away from the monster; the system then selects
  and fully resolves the direction-conditioned log response.
- `ACT-018` is absent: the bounded lesson contains one independently movable
  log, not a chain. Undo and reset remain recovery interface controls.
- Claim IDs: `AME-001`–`AME-005`, `AME-011`.

### System Behaviour Genes

- `SYS-096` — direction-conditioned maximal log displacement. End contact tips
  the log through one footprint transition; side contact rolls it along the
  perpendicular axis until the first fixed stopper or water boundary.
- `SYS-097` — water-settled object becomes traversable bridge. A correctly
  oriented log entering the one-cell gap fixes into the water and adds the
  walkable connection used to reach the target shore.
- `SYS-078` is absent: Stephen's Sausage Roll resolves a single-cell lateral
  roll with tracked top / bottom face permutation, whereas this log rolls
  maximally, has no face-processing state and may become topology.
- Resolution order: validate monster access and contact side; knock down or
  choose end-tip versus side-roll mode; resolve the complete displacement to a
  blocker or water; if water accepts the pose, fix the log and add its traversal
  edge; test monster arrival at the newly connected shore.
- Claim IDs: `AME-003`–`AME-006`, `AME-009`, `AME-012`.

### Constraint Genes

- `CON-001` — fixed occupancy capacity. The authored lesson preserves one
  finite set of land, water, stopper and target cells.
- `CON-011` — exclusive occupancy with static barriers. The monster and log
  cannot occupy rock, stump or otherwise blocked positions, and the stopper
  terminates rather than admits a roll.
- `CON-012` — push-only access geometry. Log state changes require an adjacent
  monster on the correct contact side; pulling and remote rotation are absent.
- `CON-013` — irrecoverable objective deadlock. A legal wrong-axis water entry
  can leave walking available but make the sole bridge objective unreachable
  until undo or reset restores an earlier state.
- Scarce strategic resources: access to each log side, the single stopper, the
  only log and its final approach axis relative to the water gap.
- Claim IDs: `AME-002`, `AME-005`–`AME-007`.

### Information Genes

- `INF-001` — fully visible current state. The current island terrain, monster,
  log axis, stopper, gap and target shore are inspectable before each input.
- Clouds over later unexplored world regions do not conceal any state required
  by the bounded local lesson and therefore add no hidden-state gene.
- Claim IDs: `AME-008`, `AME-009`.

### Objective Genes

- `OBJ-026` — reach designated traversable world location. The player must
  first create the log connection and then directly walk the monster across it
  to the declared target shore.
- `OBJ-004` is absent because a correct log pose alone is not completion;
  traversal by the controlled avatar is required.
- Claim IDs: `AME-006`, `AME-010`, `AME-012`.

### Time Genes

- `TIM-001` — discrete turn with automatic resolution. A side push triggers the
  complete maximal roll, collision or water settlement before another command.
- `TIM-002` is absent under the exclusive time boundary because a decisive
  input produces automatic multi-cell system resolution. Undo and reset are
  recovery controls, not branchable temporal simulation.
- Claim IDs: `AME-005`, `AME-009`, `AME-011`.

## Reproducible transitions

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Monster faces a standing tree from a legal adjacent cell | Move toward the tree | Tree falls into an elongated log aligned away from the push | push creates oriented log state | `AME-003` |
| Monster contacts one end of a resting log | Push along the log axis | Log tips through one local footprint transition | end contact is not maximal side rolling | `AME-004` |
| Monster contacts the long side and no blocker is adjacent | Push perpendicular to the log axis | Log rolls repeatedly along that axis without another input | one command produces maximal displacement | `AME-004`, `AME-005` |
| A rock or stump lies on the rolling line | Side-push the log toward it | Roll stops at the last legal position before the blocker | stopper geometry enables reorientation | `AME-005` |
| Log reaches the gap broadside or otherwise unusably | Complete the roll | Log settles without providing the needed shore-to-shore traversal | legal water entry can deadlock the objective | `AME-007` |
| Log reaches the one-cell gap lengthwise | Complete the roll | Log fixes across water and its surface becomes traversable | object placement adds a persistent world edge | `AME-006` |
| Correct bridge is present | Walk from source land across the log | Monster reaches the connected target shore and the lesson progresses | traversal, not pose alone, completes the task | `AME-010` |

## Strategic and experiential structure

- Local decision: choose a reachable contact side and predict whether the log
  will tip once or roll through every open cell.
- Medium-term planning: use the fixed stopper to halt lateral momentum at the
  only position from which an end push can align the log with the water gap.
- Long-term structure: preserve the sole log and construct a usable topological
  connection before walking the monster to the target shore.
- Common heuristics: trace the complete roll line before pushing; reason in log
  axes rather than only cells; reserve a reachable side for the final tip.
- Failure attribution: every transition is deterministic and visible, so an
  unusable bridge traces to contact side, missing stopper or final orientation.
- Player-trust factors: end and side contact, stopping priority, water
  acceptance and bridge traversal must remain spatially consistent.
- Claim IDs: `AME-002`–`AME-010`.

## Replay and variation

- The scoped terrain, tree, stopper and water gap are authored and unchanged
  between attempts; there is no random setup or time-driven mutation.
- Walking detours may vary, but the decisive log-axis and stopper sequence is
  tightly constrained by the one-log geometry.
- Replay comes from undoing a wrong roll, resetting the island or returning
  later in the excluded open world, not from generated local rules.
- Claim IDs: `AME-001`, `AME-005`–`AME-011`.

## Adjacent systems and history

- Sokoban shares local walking, one-object pushing, access geometry and visible
  non-terminal deadlocks. Its crate always moves one cell and must end on a
  fixed goal; it does not roll maximally or become traversable terrain.
- A Good Snowman Is Hard to Build shares one-ball pushes and authored stopper
  geometry but consumes snow, changes size and builds an ordered stack.
- Stephen's Sausage Roll shares an elongated pushed body and direction-sensitive
  response. Its lateral move is one cell with face permutation and cooking;
  this log rolls to a stopper and becomes a bridge without face state.
- Carto shares the objective of reaching a location after creating connectivity.
  Carto edits an authoritative map and propagates region topology; A Monster's
  Expedition manipulates one world object directly and then walks over it.
- Claim IDs: `AME-003`–`AME-012`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-009` | cardinal walking and one adjacent log push |
| System Behaviour | `SYS-096`, `SYS-097` | axis-conditioned maximal roll and bridge settlement |
| Constraint | `CON-001`, `CON-011`, `CON-012`, `CON-013` | fixed cells, blockers, push sides and deadlock |
| Information | `INF-001` | visible local island and log pose |
| Objective | `OBJ-026` | reach shore after creating traversal |
| Time | `TIM-001` | input followed by complete roll and settlement |

Canonical signature:

`ACT-008,ACT-009; SYS-096,SYS-097; CON-001,CON-011,CON-012,CON-013; INF-001; OBJ-026; TIM-001`

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `53` (`GAME-0001`–`GAME-0053`).
- Exact genome matches: none.
- Tied near matches: `GAME-0006` — Sokoban (`7 / 13 = 0.538462`).
- Supported combination subsets: `COMB-0044`, `COMB-0054`.
- Scan date: 2026-08-13.

### Selected-neighbour interpretation

No pre-migration reviewed selected-neighbour table row exists for: `GAME-0006`.

### Preserved research notes

- New genes: `SYS-096`, `SYS-097`.
- Reused genes: `ACT-008`, `ACT-009`, `CON-001`, `CON-011`, `CON-012`,
  `CON-013`, `INF-001`, `OBJ-026`, `TIM-001`.
- Classification result: two `New gene` records and a new verified
  combination; no novelty claim.

## Combination record

- `COMB-0044` recurs because visible local navigation, one-object pushing and
  non-terminal objective deadlock are all present.
- `COMB-0054` captures direction-conditioned log motion, bridge settlement and
  target-shore traversal under complete discrete resolution.
- Exhaustive supporter scan: only `GAME-0054` contains the complete new proper
  subset; `COMB-0044` now has five reciprocal supporting games.

## Taxonomy impact

- Added `SYS-096` and `SYS-097`; added A Monster's Expedition evidence to nine
  reused genes and `COMB-0044`. No prior signature, lifecycle or type changes.
- `OBJ-026` already separated traversal after connectivity creation from
  configuration display, so Carto and this game share the objective without
  conflating map editing with physical bridge construction.

## Negative results

- `SYS-078` fails because the log has maximal roll and no tracked surface state.
  `SYS-074` fails because no authoritative map is edited. `OBJ-004` fails
  because bridge placement without avatar traversal does not complete the
  bounded task. Raft motion and open-world routing are outside the scope.

## Delta summary

## Нові факти

- [Confirmed | Corroborated | High] Contact axis selects local tipping or a
  maximal roll that continues to the first obstacle or water.
- [Confirmed | Corroborated | High] Correctly oriented water settlement turns
  the same log into persistent traversable world topology.

## Нові гени

- `SYS-096` — direction-conditioned maximal log displacement.
- `SYS-097` — water-settled object becomes traversable bridge.

## Нові комбінації

- `COMB-0054` — push-resolved log bridge construction.

## Зміни таксономії

- [Observation | Corroborated | High] Added evidence to nine reused records;
  no prior genome or boundary changed.

## Нові питання

- Which independent puzzle repeats a push-axis-selected maximal roll that
  permanently turns the moved object into traversable topology?

## Наступна рекомендована гра

- [Hypothesis | Limited | Medium] `GAME-0055` — Bonfire Peaks.

## Чому саме вона

- It closes the five-game Goal with elevation-sensitive crate burning and a
  fixed self-return boundary before the corpus-wide 55-game audit.
