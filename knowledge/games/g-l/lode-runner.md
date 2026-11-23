---
game_id: GAME-0569
slug: lode-runner
game_title: Lode Runner
analysis_status: reviewed
reviewed: 2026-11-20
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-772
  system:
    - SYS-037
    - SYS-1665
    - SYS-1666
    - SYS-1667
    - SYS-1668
    - SYS-1669
    - SYS-369
    - SYS-911
  constraint:
    - CON-183
  information: []
  objective:
    - OBJ-311
  time:
    - TIM-003
---

# Game: Lode Runner

Use the canonical [vocabulary and signature rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
Digging changes a live route for player and pursuer alike. Clearing gold and
reaching the upper boundary are separate.

## Analysis scope

- Version / ruleset: original English 1983 Brøderbund Apple II disk release.
  Fresh ordinary solo game, keyboard at the ordinary starting speed, five
  lives, stock level 001. The checked assembly reconstruction represents an
  archived copy, whose byte-for-byte parity with a retail master is unverified.
- Structured analysis target: PLAT-APPLE-II in knowledge/platforms/games.json.
- Entry: start a normal game from the demo and take control on original level
  001, with its authored geometry, six gold chests and three guards in the
  inspected archived level data. The initial stationary flashing state waits
  for keyboard input. The manual recommends starting with movement.
- Primary decision loop: inspect the live route, move along floors, ladders and
  bars, and use left/right dig to alter one eligible adjacent lower brick.
  Intercept or evade guards, collect chests and account for gold they can carry
  invisibly. Use the opened route before the brick refills. After death, revise
  the route on the restored board if lives remain.
- Positive exit: resolve the outstanding gold and reach the upper boundary
  alive, normally using the revealed ladder. Stop at level 002 entry after
  the awarded life and 1,500 points. The last pickup alone does not end
  the level. In specific blocked-drop or crushing branches in the inspected
  code, gold can be removed from the outstanding count without a player pickup.
- Negative exit: ordinary lethal guard contact or closure on the runner
  consumes one life. Ctrl+A voluntarily discards a stuck attempt at that same
  cost. If lives remain, the whole authored board is rebuilt with positions,
  gold and brick states reset and score kept. At zero lives the game ends.
- Included: direct movement under support and climb rules, one full-cell
  diagonal dig, the hole's refill cues and closure, dynamic guard pursuit,
  temporary trap footing, guarded gold transfer, live display and finite
  restart stock. The positive exit increases the life stock.
- Time boundary: after active play starts, pursuits, falls and refill progress
  without alternating turns. There is no stage completion clock. The manual
  allows pausing and speed adjustment; no precise wall-clock interval or
  alternate speed is assumed.
- Excluded: later levels and their trapdoors or solid bricks beyond the dig
  eligibility distinction, presets, editor, level skips, cheats, demo play,
  high-score entry, later Apple II products, arcade and other home ports.
- Potential scoped modules: later trapdoor routing and player-authored boards.
- Direct-play status: not conducted. The original manual and Tozai release
  history were read. A pinned assembly reconstruction and its first stage
  sector were inspected as static evidence. The checked bytes are level data
  from an archived copy, not a retail master. No binary, video or audio was
  played. Exact speed, closure duration and native platform parity are open.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
| --- | --- | --- | --- | --- | --- |
| LR-001 | Brøderbund's 1983 Apple II edition ships with 150 levels. The inspected 28 by 16 board 001 has six chests, three guards, four dormant ladder cells and no trapdoor tiles. | Observation | Corroborated | High | P1, P2, D1, D2 |
| LR-002 | The runner moves directly along floors, bars and ladders and falls when unsupported. Up needs ladder access, with no dedicated jump. Ordinary guard contact can end a life. | Observation | Corroborated | High | P1, D1 |
| LR-003 | The left and right dig controls address the adjacent lower cell. An eligible brick and workable side clearance are required, and full completion produces the opening. | Observation | Corroborated | High | P1, D1 |
| LR-004 | A fully dug cell advertises refill before restoring solidity. An occupant that remains during closure can be crushed. A trapped guard is temporarily safe footing and may escape first. | Observation | Corroborated | High | P1, D1 |
| LR-005 | Autonomous guard routes respond to the runner and current platform links. A buried guard is removed and replaced in the upper part of the board. | Observation | Corroborated | Medium | P1, D1 |
| LR-006 | A guard's carried gold is hidden and still outstanding. It can drop during motion or at a pit. Inspected branches can retire gold on a blocked release or closing cell without scoring a player pickup. | Observation | Corroborated | Medium | P1; specific exception in D1 |
| LR-007 | The gold count enables the normal hidden ladder positions. In inspected play code, a live runner at the top with the count zero or the all-ladders-enabled sentinel advances the stage. The clear credits 1,500 points and one life. | Observation | Corroborated | High | P1, D1, D2 |
| LR-008 | The game starts with five lives. Death or Ctrl+A spends a life and restores the stage while another life remains. At zero the game ends. | Observation | Corroborated | High | P1, D1 |

## Basic data

- Published by Brøderbund, designed by Douglas E. Smith; Apple II,
  platform route puzzle with continuous pursuit.
- Families: FAM-005 route and network construction, FAM-010 real-time
  system pressure. One-cell route editing is limited by refill and pursuit.
- P1: [Original Brøderbund Apple II Lode Runner disk manual, 1983](https://mirrors.apple2.org.za/ftp.apple.asimov.net/documentation/applications/misc/Broderbund_Lode_Runner_manual.pdf).
  Printed pp. 1–4 describe controls, objective, trap and gold behaviour,
  life loss, start and special keys. Editor documentation identifies tile codes.
- P2: [Tozai Games, Lode Runner history](https://global.tozaigames.com/loderunner/history).
  Licensed series history identifies the original Apple II release and
  distinguishes different products.
- D1: [Xekri Redmane's pinned Apple II assembly reconstruction](https://github.com/XekriRedmane/lode_runner_reveng/blob/113db1c16951717259c9ae5e128958b29de0634d/main.nw).
  Static review of player movement, dig/restore handlers, `MOVE_GUARDS`,
  `GUARD_DROP_GOLD`, `ENABLE_NEXT_LEVEL_LADDERS` and the ordinary game loop.
  Edition specificity is limited to the documented archive lineage.
- D2: [Track 03, sector 0, archived level 001](https://github.com/XekriRedmane/lode_runner_reveng/blob/113db1c16951717259c9ae5e128958b29de0634d/disk/track_03.asm).
  Interpret the first 224 bytes of the first listed sector as 448 four-bit
  tile values. SHA-256 of those bytes is
  `3b4f009e22f4e865d9a23119809fd1b1fc3e214845d1ddadc353a4104084e8bc`.
  Tile codes 6/7/8/9 occur 4/6/3/1 times respectively. No board art or layout
  is reproduced. Sources checked 2026-11-20.

## Mechanical decomposition

### Action Genes

- ACT-008 covers direct movement. ACT-772 addresses a single lower diagonal
  brick from the current runner cell, with separate left and right inputs.
- Claim IDs: LR-002, LR-003.

### System Behaviour Genes

- SYS-1665 restores a dug brick and resolves cell occupants. SYS-1666 owns
  temporary safe footing on a trapped guard, its escape and replacement.
  SYS-1667 governs pursuit on the current terrain. SYS-1668 separately owns
  custody, visibility and release of existing gold.
- SYS-037 is the runner's contact pickup. SYS-1669 installs the authored
  ladder route when no gold remains outstanding. SYS-911 spends a life and
  returns the controlled body, while SYS-369 is the room-wide authored reset.
- Claim IDs: LR-002–LR-008.

### Constraint Genes

- CON-183 binds continuation to a finite stock, spent on death or voluntary
  sacrifice and replenished on a level clear. Eligibility details for a dig
  belong to ACT-772.
- Claim IDs: LR-003, LR-008.

### Information Genes

- No separate active information gene. The board and bottom score/life strip
  expose much of the current state, while carried gold and the dormant exit
  remain hidden. This does not meet INF-001's full-state condition. Explicit
  refill cues and gold concealment are parameters of their system rules.
- Claim IDs: LR-001, LR-004, LR-006, LR-007.

### Objective Genes

- OBJ-311 binds the still-outstanding set to the live upper boundary. An
  isolated gold pickup or a high score is not a completion predicate.
- Claim IDs: LR-006, LR-007.

### Time Genes

- TIM-003 covers real-time movement, pursuit and pit change during active play.
- Claim IDs: LR-002–LR-005.

## Reproducible transitions

| State / precondition | Action or event | Observable transition | Boundary | Claims |
| --- | --- | --- | --- | --- |
| Fresh stock 001, default keyboard | Press a movement key to start active play | Runner leaves its initial wait; live pursuit begins | No turn exchange | LR-001, LR-002 |
| Fissured brick one row below and one column aside, permitted clearance | Press U or O for that side | After the dig completes, the cell opens | Material, reach and completion matter | LR-003 |
| A live guard above a fresh hole with a supporting tile below | Let it advance into the hole | It is trapped briefly; the runner can cross above it | This does not make untrapped contact safe | LR-004, LR-005 |
| Guard still in a hole during refill | Wait through closure | Original brick returns; guard is removed and a replacement can appear above | Escape before closure changes the branch | LR-004, LR-005 |
| Unladen guard reaches a chest | Let guard step onto the chest | Chest is hidden; outstanding count is unchanged | Carrier does not give player credit | LR-006 |
| Carrier falls into a dug cell | Resolve its release | Return the chest to the eligible cell above or settle a blocked branch | A missing chest is not proof of a collected one | LR-006 |
| Count becomes zero, no runner at the top | Finish resolving the last outstanding chest | Authored dormant ladder can appear; stage remains live | Opening and clearing differ | LR-007 |
| Runner reaches top with outstanding count resolved | Climb to the upper boundary | Level advances, one life and 1,500 points are added | Runner must reach the boundary alive | LR-007 |
| Runner trapped, at least two lives | Press Ctrl+A | Consume a life and restore the original board | No unlimited reset or snapshot of mid-attempt changes | LR-008 |

## Strategic and experiential structure

- Local choice: prepare a fall route for the runner or redirect a guard by
  choosing when and where to dig.
- Gold recovery changes with custody. An empty-looking board can still have
  outstanding gold, so a pursue-and-trap plan can matter after visible pickups.
- Route timing: crossing over a trapped guard and later traversing the same
  place depend on which pit and guard state applies when the runner arrives.
- Claim IDs: LR-002–LR-007.

## Replay and variation

- The same authored board returns after failed attempts. Live movement order
  can change guard occupancy and gold custody without shuffling the layout.
- Claim IDs: LR-001, LR-005, LR-006, LR-008.

## Adjacent systems and history

- Later boards and ports change possible route and gold situations; the 1983
  Apple II play boundary is the only one used in the signature.
- Claim IDs: LR-001, LR-003.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
| --- | --- | --- |
| Action | ACT-008, ACT-772 | Four directions and two dig sides |
| System Behaviour | SYS-037, SYS-369, SYS-911, SYS-1665, SYS-1666, SYS-1667, SYS-1668, SYS-1669 | Guard speed, chase heuristic, pit interval |
| Constraint | CON-183 | Five starting lives, clear adds one |
| Information | — | Displayed stage/lives/score; carried gold hidden |
| Objective | OBJ-311 | Six initial chests plus top boundary |
| Time | TIM-003 | Live action after the start wait |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `568` (`GAME-0001`–`GAME-0568`).
- Exact genome matches: none.
- Tied near matches: `GAME-0342` — PAC-MAN (`5 / 24 = 0.208333`).
- Supported combination subsets: none.
- Scan date: 2026-11-20.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
| --- | --- | --- | --- |
| `GAME-0342` — PAC-MAN | ACT-008, CON-183, SYS-037, SYS-911, TIM-003 | Both couple live pursuit, contact collection and finite life stock. Lode Runner changes its routes with self-restoring holes, has hidden carried gold, and requires the live upper boundary after resolving it. | Tied near: 5 / 24 = 0.208333 |

### Preserved research notes

- New genes: ACT-772, SYS-1665 through SYS-1669 and OBJ-311.
- Classification result: New gene.

## Taxonomy impact

- [TAXONOMY_CHANGE_315](../../../research/taxonomy-changes/TAXONOMY_CHANGE_315.md)
  records seven additions without predecessor changes.

## Negative results

- The first board has no trapdoor tile. Later editor affordances do not establish
  an active rule here.
- Original manual and archived code support distinct claims. The checked
  code's rare gold-retirement branches do not establish a measured level 001
  player route that deliberately forces each branch.

## Delta summary

## New facts

- [Observation | Corroborated | High] LR-003–LR-008 separate temporarily
  altered collision, gold custody, stage settlement and life-bounded recovery.

## New genes

- [Observation | Corroborated | Medium] Seven typed additions in
  TAXONOMY_CHANGE_315.

## New combinations

- [Observation | Corroborated | High] No new combination is proposed.
  Existing subsets are owned by the comparison record.

## Taxonomy changes

- [Observation | Corroborated | Medium] Seven definitions added without
  changing predecessor definitions, signatures or lifecycles.

## New questions

- Native fidelity, precise live timings and reachability of each exceptional
  gold retirement from normal stage 001 may be tested with an exact release.

## Next recommended game

- [Hypothesis | Limited | Medium] GAME-0570, PS5 Cult of the Lamb.
- Optimisation criterion: alternate era and platform. Compare live route
  choices and return to a maintained settlement with the fixed level retry.
- Backlog impact: third Selection 046 unit.

## Why this game

- [Hypothesis | Limited | Medium] Fast local edits alter both the runner's
  route and the pursuer's path, while gold can move independently of both.
