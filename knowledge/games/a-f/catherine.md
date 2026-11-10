---
game_id: GAME-0477
slug: catherine
game_title: Catherine
analysis_status: reviewed
reviewed: 2026-10-02
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-009
    - ACT-630
    - ACT-631
  system:
    - SYS-1241
    - SYS-1242
  constraint:
    - CON-741
  information:
    - INF-451
  objective:
    - OBJ-231
  time:
    - TIM-003
---

# Game: Catherine — original PS3 Underground Cemetery on Normal

Use the [canonical genome vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Block positions, the difficulty setting and the tower's speed are parameters, not separate genes.

## Analysis scope

- Version / ruleset: original English-language 2011 PlayStation 3 *Catherine*, Golden Playhouse, Normal difficulty, first Nightmare, Underground Cemetery (Stage 1-1). The exact disc revision and later patch state were not inspected. This is not *Catherine: Full Body*, its Remix Mode, or the 2019 PC version.
- Structured analysis target: original PlayStation 3 retail game at Normal difficulty; see [`knowledge/platforms/games.json`](../../platforms/games.json). The available 2011 publisher manual is for the contemporary Xbox 360 release; a contemporary PS3 walkthrough corroborates the first-stage mechanics, but platform-specific button labels are not transferred.
- Primary decision loop: inspect the nearby tower and receding lower rows, walk or climb where supported, push a movable adjacent block or grab and pull one toward Vincent to make a one-block stair, let the resulting blocks settle under their support rule, and continue upward before the lowest traversable rows disappear. A Normal-mode undo can reverse a recent mistaken move, but does not remove the live ascent pressure.
- Entry and exit: enter Stage 1-1 with Vincent at its bottom and the exit at the top. The positive terminal is reaching the top goal and receiving the stage-clear result. The negative terminal is falling or being caught by the collapsing tower before that goal. A retry after death is outside this single-attempt packet.
- Included: direct movement and one-block ascent; pushing and pulling ordinary blocks; edge-supported suspension versus unsupported fall; time-driven removal of lower rows; local block, exit and danger feedback; the Normal-mode undo action; goal and fall terminal.
- Excluded: the Stray Sheep conversation/alignment loop, later Nightmares and bosses, later fragile/heavy/ice/trap blocks, Babel, Colosseum, multiplayer, *Full Body* linked/Remix blocks, difficulty changes mid-stage, optional coin and pillow collection, score-chain/medal optimisation, item use, post-death retry stock, and exact descent interval, block coordinates or solved input sequence. These are not claims that such features are absent from the complete product.
- Reproducible parameterisation: select the original PS3 story at Normal, enter its first Nightmare, test an ordinary block's push, grab/pull another to form a single-height step, observe whether an edge-connected block remains and an unsupported block falls, then keep climbing while lower rows disappear until the top goal. If an input is mistaken, use the difficulty-eligible undo and retest. Record the precise revision, board layout, inputs and elapsed time before claiming an exact replay; none was captured here.
- Potential scoped modules: score-chain and medal optimisation, retry/pillow economy, later block types, boss interference and narrative alignment each require a separate bounded packet.
- Direct-play status: no PS3 console, original disc, executable, controller trace, screenshot, gameplay video or audio was inspected; no direct play was conducted. The publisher's contemporary Xbox 360 manual documents shared mechanical rules and an original-PS3 player guide corroborates the first stage. Cross-platform equivalence is assumed only for these corroborated rules, not for inputs or exact timings. The illustration is original interpretive art, not a screenshot.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `CAT-001` | The original product was released for PS3 and Xbox 360 in 2011; *Full Body* is a later expanded product. | Confirmed | Direct | High | P1, P3 |
| `CAT-002` | In Nightmare, the player grabs and moves blocks forward or backward; Vincent climbs only one block of height at a time. | Confirmed | Corroborated | High | P2, S1, S2 |
| `CAT-003` | Edge contact with a block below can suspend a block; removing all valid support can make blocks fall. | Confirmed | Corroborated | High | P2, S1, S2 |
| `CAT-004` | Lower tower rows disappear with time; Vincent must climb to the top before falling. | Confirmed | Corroborated | High | P2, S1, S2 |
| `CAT-005` | Underground Cemetery is the authored introductory Nightmare for block movement and one-step climbing. Whether immovable dark blocks occur within this first level is disputed and not admitted. | Observation | Conflicting | Medium | S1, S3 |
| `CAT-006` | In the English original Normal difficulty the publisher manual and contemporary PS3 guide permit undoing recent moves. | Confirmed | Corroborated | High | P2, S1; PS3 input not independently verified |
| `CAT-007` | Reaching the goal clears the stage; falling ends the current attempt, while retries are a separately limited recovery layer. | Confirmed | Corroborated | High | P2, S1 |

## Basic data

- Release / origin: Atlus's original 2011 *Catherine*, not the *Full Body* reworking.
- Platform or physical form: PlayStation 3 gamepad, original English-language release; no PS3-specific button mapping asserted.
- Mechanical families: physics and object manipulation (`FAM-007`) for block support and repositioning; real-time system pressure (`FAM-010`) for the advancing loss of lower rows.
- **P1:** [Atlus, original *Catherine* archive](https://www.atlus.co.jp/title-archive/cathy/), accessed 2026-10-02; original PS3/Xbox 360 identity, not a precise Stage 1 rulebook.
- **P2:** [Atlus, contemporary *Catherine* Xbox 360 instruction manual](https://www.videogamemanual.com/xbox360/Catherine.pdf), printed pp. 6–13, accessed 2026-10-02; original publisher rules for grabbing, moving, edge support, one-block climb, row loss, Normal undo and goal/failure. It is an Xbox edition manual; platform-specific button names are deliberately excluded.
- **P3:** [Atlus, *Catherine: Full Body* product page](https://atlus.com/atlus-titles/catherinefullbody/?ItemID=88), accessed 2026-10-02; distinguishes the later expanded game and Remix linked blocks, which are excluded here.
- **S1:** [Christopher J. Snelgrove, original PS3/360 walkthrough](https://gamefaqs.gamespot.com/ps3/605302-catherine/faqs/62439), 2011, accessed 2026-10-02; authored after Japanese and US PS3 play, corroborates Underground Cemetery, support/fall, time pressure and explicitly the US Normal addition of undo. This is a player guide, not the game's executable.
- **S2:** [Warp Zoned, hands-on original demo preview](https://www.warpzoned.com/2011/07/catherine-hands-on-preview-move-over-freddy-theres-a-new-nightmare-in-town/), July 2011, accessed 2026-10-02; first-stage climbing, disappearing lower steps and edge suspension.
- **S3:** [Original Underground Cemetery Stage 1-1 written route](https://catherine.fandom.com/wiki/Walkthrough%3AUnderground_Cemetery_1-1), accessed 2026-10-02; difficulty-specific step descriptions. It says immovable top blocks appear in Stage 1, while S1 places their introduction in Stage 2. This conflict is unresolved, so that feature is excluded.
- Claim IDs: `CAT-001`–`CAT-007`.

## Mechanical decomposition

### Action Genes

- Reuse `ACT-008` for Vincent's directly controlled local walking and one-height climbing; a leap over several block levels is not assumed (`CAT-002`).
- Reuse `ACT-009` for pushing one adjacent movable block away from his contact side (`CAT-002`).
- New `ACT-630` for grabbing and pulling one adjacent movable block toward the controlled body to expose a step. Sokoban's `ACT-009` explicitly excludes pulling (`CAT-002`).
- New `ACT-631` for Normal-mode undo of a recent local move. It is a discrete recent-move reversal, not `ACT-044`'s free simulation-history rewind (`CAT-006`).

### System Behaviour Genes

- New `SYS-1241`: after block displacement, an edge contact to a block below can preserve suspension, whereas loss of valid support can drop the block and alter later climb geometry (`CAT-003`).
- New `SYS-1242`: elapsed live Nightmare time removes the tower's lowest rows, so a formerly usable route may cease to exist before the avatar reaches the top (`CAT-004`).
- Resolution order: read present support → move or pull/push a legal block → settle its support/fall response → test nearby climb access → advance live lower-row loss independently of the player's deliberation → test goal or fall. Undo restores a recent eligible move, not a proof of a permanently frozen tower.

### Constraint Genes

- New `CON-741`: an upward body climb can clear at most one block of height from an eligible current foothold; taller faces need a rearranged stair (`CAT-002`).
- Block-type-specific immovability is not admitted: S1 and S3 disagree on whether the dark fixed type occurs in Stage 1 (`CAT-005`).
- Scarce strategic resources: reachable support faces and remaining vertical distance above the disappearing lower rows, not coins or a turn budget.

### Information Genes

- New `INF-451`: the local tower view exposes nearby blocks, apparent support edges, current avatar position, upper goal and visible lower-row danger; it does not disclose a complete future falling schedule (`CAT-003`–`CAT-005`).

### Objective Genes

- Reuse `OBJ-231`: reach the stable authored goal before the route's lower supports disappear. This is not merely `OBJ-026`'s arrival at a permanently traversable place (`CAT-004`, `CAT-007`).

### Time Genes

- Reuse `TIM-003`: the tower continues losing lower rows while Vincent can move or rearrange blocks. This is not untimed Sokoban (`TIM-002`) or one fully settled discrete turn (`TIM-001`) (`CAT-004`).

## Reproducible transitions

| Before | Action or event | Bounded resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| An ordinary movable block faces Vincent | Grab and pull toward him | The block shifts to a reachable position and can expose a one-step ledge | Pulling differs from push-only Sokoban | `CAT-002` |
| A movable block is adjacent with legal space behind it | Push away | Its location changes and the next climb may be open | Adjacent push can build a stair | `CAT-002` |
| A moved block retains an edge touching a lower block | Let its support resolve | It can remain suspended instead of immediately falling | Edge support changes path planning | `CAT-003` |
| A block loses all valid lower support | Move its supporting neighbour away | The unsupported block falls; the former foothold is unavailable | Unsupported fall is consequential | `CAT-003` |
| Vincent faces a vertical rise higher than one block | Attempt direct ascent | He cannot climb it directly; reposition a block into an intermediate step | The height limit is a legal-action boundary | `CAT-002` |
| Vincent delays on a lower row | Let live time pass | Bottom blocks disappear and falling can terminate the attempt | Time pressure is autonomous | `CAT-004` |
| A recent local move is mistaken on Normal | Invoke undo | An eligible prior move is reversed for another attempt | Recovery is difficulty-bounded, not a route solution itself | `CAT-006` |
| The top goal becomes reachable before the tower catches Vincent | Climb onto/reach goal | Stage 1-1 ends in a clear result | Positive packet terminal | `CAT-007` |

## Strategic and experiential structure

- Local decision: choose whether a block should move away or toward Vincent, preserving a support face and one-height step for the next ascent.
- Medium-term planning: pulling out a needed step can also remove support for blocks above; the safe route must be rechecked after each change rather than treated as an isolated sliding-box move.
- Long-term structure: advance vertically faster than the timed row loss, reaching the fixed top goal. Undo reduces a local error on Normal but does not justify deliberating without regard to the live tower.
- Common heuristics: make stair-like positions, use valid edge contact and avoid pushing a necessary support into empty space. These are tactics reported by the guide, not a guaranteed exact winning sequence.
- Failure attribution and trust: a falling block or missing lower row visibly changes traversability; the exact row-removal cadence was not measured, so this record does not claim a precise escape window.

## Replay and variation

The first stage is authored, not a procedural tower. Normal and Hard route descriptions differ; this analysis fixes Normal. Within a repeat attempt, the player's push/pull order, speed and use of undo change the route and result. Coin/chain performance is a separate scoring module, not a distinct survival terminal here.

## Adjacent systems and history

*Sokoban* (`GAME-0006`) also permits adjacent block pushing but forbids pulling, has no autonomous row loss and solves crate-on-goal occupancy rather than escaping upward. *Uncharted 2* (`GAME-0391`) shares a collapsing-route exit under live pressure, but its falling train cars are not deliberately rearranged into a one-block stair. These contrasts are scope-specific, not a statement about either complete product.

## Normalised genome

| Type | Active gene IDs | Carrier parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-009`, `ACT-630`, `ACT-631` | walking/climbing, push, pull, Normal undo |
| System Behaviour | `SYS-1241`, `SYS-1242` | edge support/fall, timed lower-row loss |
| Constraint | `CON-741` | one-block ascent |
| Information | `INF-451` | local tower, support, danger and goal |
| Objective | `OBJ-231` | reach top before support disappears |
| Time | `TIM-003` | live world progression during input |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `476` (`GAME-0001`–`GAME-0476`).
- Exact genome matches: none.
- Tied near matches: `GAME-0391` — Uncharted 2: Among Thieves (`3 / 12 = 0.250000`).
- Supported combination subsets: none.
- Scan date: 2026-10-02.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0391` *Uncharted 2: Among Thieves* | `ACT-008`, `OBJ-231`, `TIM-003` | Both climb toward a safe exit while the route fails in live time. Catherine rearranges ordinary blocks by push and pull, uses edge support, one-block climb and eligible undo; Uncharted 2 traverses authored train-car failures without building a block staircase. | `3 / 12 = 0.250000`; tied nearest non-exact earlier signature, not the same manipulated-tower rules. |

## Taxonomy impact

`TAXONOMY_CHANGE_214` admits six bounded new genes. `ACT-008`, `ACT-009`, `OBJ-231` and `TIM-003` transfer unchanged. Earlier signatures and verified combinations are not revised.

## Negative results

- Reject `ACT-044`: Normal-mode recent-move undo is not a free scrub through retained continuous simulation history.
- Reject `TIM-002`: lower rows disappear while no move is submitted.
- Reject `CON-012`: Sokoban's push-only geometry forbids pulling, which this game explicitly permits.
- Reject *Full Body* Remix linked blocks and later Nightmare special block types from this first original-stage packet.

## Delta summary

## New facts

- [Confirmed | Corroborated | High] First Nightmare progression couples push/pull staircase construction and live bottom-row loss (`CAT-002`–`CAT-004`).
- [Observation | Conflicting | Medium] Written routes disagree on whether dark immovable blocks already appear in the first stage; no such gene is admitted (`CAT-005`).

## New genes

- [Observation | Corroborated | Medium] Six typed boundaries isolate pulling, local undo, edge support/fall, timed row loss, one-step ascent and local danger information.

## New combinations

- [Observation | Limited | Medium] No new combination proposed; verified subsets are recomputed against the completed signature.

## Taxonomy changes

- [Observation | Corroborated | Medium] `TAXONOMY_CHANGE_214` adds six boundaries without modifying earlier signatures.

## New questions

- A version-pinned PS3 capture could establish the exact Normal board layout, patch state, undo/time interaction and lower-row cadence; these are not inferred from a manual of the parallel release.

## Next recommended game

- [Hypothesis | Limited | Medium] No next game is selected in this nine-game Goal. A later selection should deliberately mix platform families rather than concentrate Nintendo releases.
- Optimisation criterion: independent mechanical and platform coverage with reproducible original-edition evidence.
