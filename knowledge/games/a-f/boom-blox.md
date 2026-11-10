---
game_id: GAME-0465
slug: boom-blox
game_title: Boom Blox
analysis_status: reviewed
reviewed: 2026-10-01
combination_ids: []
gene_ids:
  action:
    - ACT-615
    - ACT-616
  system:
    - SYS-036
    - SYS-822
  constraint: []
  information:
    - INF-001
  objective:
    - OBJ-007
  time:
    - TIM-003
---

# Game: Boom Blox

Use the canonical [vocabulary and comparison rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). The Warrior, its baseball and one/two/three-throw medal thresholds are parameters of this scoped level, not separate gene names.

## Analysis scope

- Version / ruleset: original 2008 Boom Blox retail Wii game, single-player Explore → Gem Blox → Warrior puzzle. The publisher-supplied Nintendo Wii page establishes aimed motion throws and physical block effects; a contemporary original-Wii walkthrough supplies the named puzzle, controls and medal thresholds. The exact regional disc revision and executable were not obtained or hashed.
- Structured analysis target: `PLAT-NINTENDO-WII` in [platform coverage](../../platforms/games.json), not the 2009 Boom Blox Bash Party sequel, a mobile adaptation, a later emulation wrapper or a modified level.
- Entry: training is already completed so Explore is available; enter the untouched Warrior arrangement before the first throw. Training is an entry precondition, not an analysed action.
- Primary decision loop: inspect and orbit the block-built warrior, choose a line to a vulnerable support (the waist between its legs is the walkthrough's suggested target), aim with the Wii Remote, hold A, swing and release a baseball, then watch collisions and support loss move gem blocks toward the floor. Reassess the changed structure before another throw if targets remain.
- Positive terminal: the puzzle credits every required gem block as fallen and awards the level's medal according to the number of throws used. The contemporary guide lists Warrior's Gold at one, Silver at two and Bronze at three throws; one throw is an efficiency goal, not a requirement to experience the physical puzzle.
- Negative or non-medal boundary: a weak, missed or badly angled throw can leave gem blocks in place and consume another throw. The written sources do not establish the exact failure-screen timing, retry control or whether an over-bronze attempt can continue without a medal, so no finite-exhaustion terminal is inferred.
- Included: free camera orbit around the fixed construction to choose an unobstructed firing line, pointing, held-and-released motion throw, ball impact, continuously resolved rigid-body collision/gravity, gem blocks knocked off their supports, visual inspection of remaining targets, and completed-puzzle medal grading by throw count.
- Excluded: the played Training stages, later Explore Gem Blox puzzles, point/bomb/vanish/chemical blocks, blast chains, Grab and Create tools, characters, Adventure, multiplayer, online sharing, score optimisation beyond the recorded one/two/three-throw medals, exact physics coefficients, frame timing and all sequel/port rules. These exclusions do not claim those features are absent from the full product.
- Reproducible parameterisation: finish Training, select Explore → Gem Blox → Warrior, leave the arrangement untouched, rotate the camera to expose the central lower support, point at its waist, hold A, swing forward and release. Let the contacted blocks settle, inspect any gem blocks still standing, and use another aimed throw if needed. The guide offers this as a strategy, not a guaranteed one-throw input trace; physics outcomes are not asserted byte-deterministic.
- Potential scoped modules: later Gem Blox structures, bomb/chemical chain puzzles, grab-tool extraction, local multiplayer, exact medal/failure UI and direct executable capture require separate evidence packets.
- Direct-play status: not conducted. No original disc, console, executable, save, gameplay screenshot, video, audio or input trace was inspected. This is a source-led rule reconstruction, not a claim of first-hand completion.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `BBX-001` | The scoped product is original Wii Boom Blox, and swing strength plus thrown-object weight affect physical impact | Confirmed | Direct | High | P1 |
| `BBX-002` | Pointing, holding A, swinging and releasing throws; B plus pointer motion can rotate the puzzle camera | Observation | Corroborated | High | P1, S1 |
| `BBX-003` | Explore follows Training; Warrior is the first listed Gem Blox puzzle and its medal thresholds are one, two and three throws | Observation | Direct | High | S1 |
| `BBX-004` | A low strike can destabilise the warrior; waiting for the physical fall matters, and remaining gem blocks may require another angle or throw | Observation | Corroborated | High | P1, S1 |
| `BBX-005` | Gem blocks in this puzzle are cleared by falling from the construction, not by matching colours or triggering an explosive | Observation | Corroborated | High | P1, S1 |
| `BBX-006` | Seven admitted genes describe this one bounded puzzle; no unsupported finite-exhaustion failure or destroyed-support rule is imported | Observation | Direct | High | P1, S1, V1 |

## Basic data

- Release / origin: Electronic Arts, original Wii release in 2008. Nintendo UK's game record dates the European release to 8 May 2008; that date is not used as a North American disc-revision claim.
- Puzzle family: physics and object manipulation (`FAM-007`).
- **[P1]** [Nintendo UK's publisher-supplied Boom Blox description](https://www.nintendo.com/en-gb/Games/Wii/Boom-Blox-280682.html), especially aimed Wii Remote throws, impact strength, projectile weight and movable blocks; accessed 2026-10-01.
- **[S1]** [vidicator's original-Wii Boom Blox guide, updated 2008](https://gamefaqs.gamespot.com/wii/941974-boom-blox/faqs/53107), Controls / Training / Explore → Gem Blox → Warrior; accessed 2026-10-01. It is a contemporary player's written strategy, not a publisher specification or direct observation by this reviewer.
- **[V1]** Source-model transitions below; no executable or first-hand play is claimed.

## Mechanical decomposition

### Action Genes

- New `ACT-615` commits one pointer-aimed, physically swung baseball throw on release of A. This is not fixed-launcher `ACT-113` or lane-bound bowling delivery `ACT-499`.
- New `ACT-616` changes the viewing and firing line around a fixed three-dimensional construction before a throw. It does not turn perspective into traversable geometry (`ACT-095`) or change world gravity.

### System Behaviour Genes

- `SYS-036` continuously resolves the launched ball and contacted rigid blocks through gravity, collisions and lost support. It covers ordinary displacement without importing `SYS-147`'s damage-broken structural members.
- `SYS-822` grades the completed bounded puzzle by throws used: the guide lists Warrior's Gold, Silver and Bronze thresholds as one, two and three. This is a graded result, not a fixed elapsed-time medal (`SYS-711`).

### Constraint Genes

- None admitted. The three-throw Bronze threshold is evidence for a medal class, not proof that attempt exhaustion must immediately terminate play as required by `CON-020`.

### Information Genes

- `INF-001` covers the currently inspectable block arrangement and remaining gem targets; camera orbit can reveal the other side. The current shot outcome is not previewed as a guaranteed future trajectory.

### Objective Genes

- `OBJ-007` clears the declared gem-block targets by making them fall from the construction. Wooden supports need not themselves all be removed; the medal is a grading result, not the target-clearance predicate.

### Time Genes

- `TIM-003` allows aiming and further input while physical block motion runs. The guide's advice to wait rather than strike blocks that are still moving distinguishes live resolution from an automatically sealed discrete turn.

## Reproducible transitions

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Warrior is untouched and its central support is visible | Hold B and move the pointer to orbit | The construction is inspected from another line without moving its blocks | View choice affects target access, not the physical board | `BBX-002`, `BBX-004` |
| A chosen support is aligned with the pointer | Hold A, swing the Wii Remote and release A | One ball is committed; swing strength affects its impact, but exact impulse is unmeasured | Motion-sampled throw differs from a click-only launcher | `BBX-001`, `BBX-002` |
| The ball reaches a supporting block | Let live physics proceed | Contacts may displace it, remove support and topple gem blocks toward the floor | Physical cascade needs neither matching nor explosives | `BBX-004`, `BBX-005` |
| One gem block remains supported after a weak hit | Inspect the new layout and throw again | The remaining target can still prevent the all-gems clear and use another throw | A single attempted strategy is not guaranteed | `BBX-004` |
| All required gem blocks have fallen on the first, second or third throw | Allow the level result to settle | A completed Warrior receives Gold, Silver or Bronze by the recorded thresholds | Completion and efficiency grade are separate | `BBX-003`, `BBX-005` |
| Three throws are spent without the required clear | Do not infer a further input | The sources do not establish the exact UI or continuation rule | Avoids a false `CON-020` signature | `BBX-006` |

## Strategic and experiential structure

- Local decision: which support and angle will convert one ball impact into enough movement of gem blocks.
- Medium-term planning: preserve useful support displacement from the first shot and decide whether a second line is needed after blocks move.
- Long-term structure: complete Warrior and optionally seek a better throw-count medal; later Explore puzzles are outside this packet.
- Common heuristic: use a strong throw low at the waist, possibly from behind, then let moving blocks finish falling before another shot. This is advice from S1, not a universal solver.
- Failure attribution: remaining supported gems explain a non-completion; the guide does not establish an exact failure-screen transition after three misses.
- Player trust: gem-clear evaluation must follow the actual settled positions, and the medal must depend on the accepted throw count rather than the apparent size of a collapse.

## Replay and variation

- Aimed point, camera line, swing strength and physical collision outcome can vary. The authored Warrior block arrangement is not described as procedurally regenerated.
- The gold strategy is not guaranteed: the guide expressly recommends another angle if the waist strike fails.
- A replay can seek a lower throw-count medal. No score multiplier or separate collectible is inferred.

## Adjacent systems and history

- *Angry Birds Classic* and *Peggle Deluxe* share a projectile/physics/target-clear family resemblance, but their `ACT-113` fixed launcher and `SYS-146` after-launcher boundary do not describe Wii Remote motion sampling or an orbitable aiming viewpoint.
- *Wii Sports Bowling* samples a physical release, but its `ACT-499` travels down a constrained lane and its `ACT-498` selects a stance and lane line; Warrior is a freely aimed throw at a three-dimensional block support.
- `SYS-147` needs damage-broken supports. The scoped normal blocks can be displaced and topple without that breakage; later explosive/fragile blocks are explicitly excluded.
- The 2009 sequel and non-Wii versions cannot supply original-disc rules without separate evidence.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-615`, `ACT-616` | A-release, ball, camera orbit and waist line are parameters |
| System Behaviour | `SYS-036`, `SYS-822` | rigid-body contacts and 1/2/3-throw medal tiers are parameters |
| Constraint | none | no inferred attempt-exhaustion failure |
| Information | `INF-001` | inspectable gem arrangement |
| Objective | `OBJ-007` | required gem blocks falling from the structure |
| Time | `TIM-003` | live collision settlement |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `464` (`GAME-0001`–`GAME-0464`).
- Exact genome matches: none.
- Tied near matches: `GAME-0114` — Peggle Deluxe (`3 / 11 = 0.272727`).
- Supported combination subsets: none.
- Scan date: 2026-10-01.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0114` — Peggle Deluxe | `INF-001`, `OBJ-007`, `TIM-003` | Both puzzles show inspectable targets that must all be cleared while moving bodies can still be acted around. Peggle fires from a fixed top launcher into orange pegs and a bucket; Warrior samples a physical Wii throw after orbiting a three-dimensional support, then grades a completed gem-block collapse by throws. The shared target/time surface does not transfer Peggle's launcher, pegs or ball-stock rule. | Tied near, `3 / 11 = 0.272727` |

### Preserved research notes

- New genes: `ACT-615`, `ACT-616`.
- Reused genes: `SYS-036`, `SYS-822`, `INF-001`, `OBJ-007`, `TIM-003`.
- Classification result: `New genes`.
- Evidence and reasoning: an embodied release and orbit-chosen firing line require new boundaries; existing physics, graded settlement, visible current board, target clearance and live time transfer without a false finite-failure or broken-support assertion.

## Taxonomy impact

- Registry changes: add two Active Action boundaries without changing earlier signatures or verified combinations.
- Taxonomy-change record: [`TAXONOMY_CHANGE_202`](../../../research/taxonomy-changes/TAXONOMY_CHANGE_202.md).

## Negative results

- No original disc, executable, direct play, audiovisual capture or measured physics impulse.
- No evidence for exact failure-screen timing or whether a non-medal over-bronze attempt may continue; `CON-020` is not admitted.
- No evidence that the normal Warrior support is damaged into pieces; `SYS-147` is not admitted.
- No bomb, chemical, vanish, grab or Create rules are transferred from other levels into Warrior.

## Delta summary

## New facts

- [Confirmed | Direct | High] Publisher-supplied original-Wii description ties aimed Wii Remote throw strength and object weight to physical block effects (`BBX-001`).
- [Observation | Direct | High] A contemporary Wii guide records Warrior's three medal thresholds and low-support strategy (`BBX-003`, `BBX-004`).

## New genes

- [Observation | Corroborated | High] `ACT-615` and `ACT-616` isolate motion-sampled release and orbit-chosen aiming line.

## New combinations

- [Observation | Direct | High] None; verified-subset scan is recorded in Corpus comparison.

## Taxonomy changes

- [Observation | Direct | High] Two new actions, no prior signature mutation or inferred finite-exhaustion constraint.

## Open questions

- Original-disc capture could establish exact post-third-throw failure UI, retry control, active throw-while-falling permissions and numerical impact law.
