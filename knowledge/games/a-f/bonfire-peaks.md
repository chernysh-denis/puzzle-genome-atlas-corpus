---
game_id: GAME-0055
slug: bonfire-peaks
game_title: Bonfire Peaks
analysis_status: reviewed
reviewed: 2026-08-13
combination_ids:
  - COMB-0055
gene_ids:
  action:
    - ACT-008
    - ACT-048
  system:
    - SYS-098
  constraint:
    - CON-001
    - CON-011
    - CON-090
    - CON-101
  information:
    - INF-001
  objective:
    - OBJ-014
  time:
    - TIM-001
---

# Game: Bonfire Peaks

## Analysis scope

- Version / ruleset: Corey Martin and Draknek & Friends' released base game,
  scoped to the first named bonfire puzzle, `Burn Your Belongings (1.1)`.
- Included: one oriented avatar; one designated belongings crate; fixed visible
  floor, three one-step elevation bands and walls; cardinal forward / backward
  movement and quarter-turns; explicit crate grab, front-offset carrying and
  release; carried-object turn sweep; carry-conditioned ascent; the fixed
  bonfire; crate consumption and immediate puzzle completion; discrete undo and
  restart as recovery controls.
- Excluded: every later main-path and side-path puzzle; pushing free crates,
  stacking, long blocks, streams, arrows, pressure devices and other later
  rules; overworld routing and reward crates; Lost Memories DLC; optimisation,
  hint videos, achievements, narrative interpretation and presentation.
- Direct-play status: not conducted. Creator and official sources establish
  carrying, climbing and burning. A contemporary mechanical review establishes
  oriented movement and the held object's turning footprint. The specialist
  walkthrough identifies the exact puzzle as `1.1`, supplies its entry and
  one-step-before-exit states, and records one grab-carry-release manipulation.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `BFP-001` | `Burn Your Belongings` is the first named base-game bonfire puzzle, indexed as `1.1` | Confirmed | Corroborated | High | P1–P3, S2 |
| `BFP-002` | The fixed state contains one avatar, one belongings crate, three elevation bands and one bonfire | Confirmed | Direct | High | S2 |
| `BFP-003` | The avatar moves forward or backward and pivots on the spot rather than sidestepping | Confirmed | Corroborated | High | S1, S2 |
| `BFP-004` | Grab acquires the adjacent crate and holds it in the cell in front of the avatar until release | Confirmed | Corroborated | High | P2, P3, S1, S2 |
| `BFP-005` | A held crate swings around the avatar during a pivot, so the swept corner and destination must be clear | Confirmed | Corroborated | High | S1, S2 |
| `BFP-006` | Carrying changes which one-step ascents are legal; routing and facing therefore matter on the staircase | Confirmed | Corroborated | High | P2, P3, S2 |
| `BFP-007` | The puzzle requires transporting the designated belongings crate into the fixed bonfire | Confirmed | Corroborated | High | P1–P3, S1, S2 |
| `BFP-008` | Fire contact consumes the belongings and credits the puzzle instead of preserving a target arrangement | Confirmed | Corroborated | High | P1–P3, S2 |
| `BFP-009` | Terrain, avatar facing, crate pose, elevation and receiver are visible before every input | Observation | Direct | High | S2 |
| `BFP-010` | Each input and any pickup, carried-footprint move, release or completion response resolves before the next input | Observation | Corroborated | High | S1, S2 |
| `BFP-011` | Undo and restart restore the authored puzzle state without exposing a branchable timeline | Confirmed | Corroborated | High | S2, S3 |
| `BFP-012` | The scoped puzzle contains no free-crate push, stacking, return-to-start objective or automatic fall | Observation | Corroborated | High | S2 |

## Basic data

- Release / origin: Corey Martin developed Bonfire Peaks with puzzle-design
  collaboration from Alan Hazelden; Draknek & Friends published it on 30
  September 2021.
- Platform or physical form: deterministic single-player digital voxel-grid
  puzzle with discrete oriented movement and object handling.
- Puzzle family: elevation-constrained front-carried object sacrifice.
- Primary and creator sources:
  - **[P1]** [Official Bonfire Peaks site](https://bonfirepeaks.com/), identifying
    the creators and the core climb / burn-your-belongings premise.
  - **[P2]** Corey Martin,
    [Game Developer interview](https://www.gamedeveloper.com/design/bonfire-peaks-explores-complex-emotions-through-puzzle-design),
    describing boxes carried into fire and how carrying makes climbing harder.
  - **[P3]** Corey Martin,
    [PlayStation Blog release article](https://blog.playstation.com/2021/09/28/bonfire-peaks-comes-to-ps4-and-ps5-september-30/), documenting the release,
    handcrafted puzzle structure, climbing, carrying and sacrifice objective.
  - **[P4]** [Official Steam product page](https://store.steampowered.com/app/1147890/Bonfire_Peaks/), confirming developer, publisher and released base product.
- Contemporary and bounded mechanical corroboration:
  - **[S1]** [PC Gamer review](https://www.pcgamer.com/bonfire-peaks-review/),
    recording forward / backward / pivot movement, held-crate turning and early
    navigation lessons.
  - **[S2]** [Steam Community puzzle guide](https://steamcommunity.com/sharedfiles/filedetails/?id=2618480287), used only to bind `Burn Your Belongings (1.1)`, its entry / pre-exit states, controls and single crate manipulation.
  - **[S3]** [PSX Extreme review](https://psxextreme.com/reviews/ps4/bonfire-peaks-review/), corroborating grab / placement, the fire receiver, one-step undo and restart.
- Claim IDs: `BFP-001`–`BFP-012`.

## Mechanical decomposition

### Action Genes

- `ACT-008` — navigate controllable agent. Directional input advances the
  oriented avatar forward or backward through one traversable local position,
  or changes facing by a quarter turn when the movement interpretation is a
  pivot.
- `ACT-048` — pick up and release portable rigid object. Grab acquires the one
  adjacent belongings crate, preserves it one cell in front during navigation
  and lets the player release it into a legal world position or the bonfire.
- `ACT-009` is absent: the complete `1.1` route contains one grab-carry-release
  manipulation and no independent push of a free crate.
- Claim IDs: `BFP-003`–`BFP-005`, `BFP-012`.

### System Behaviour Genes

- `SYS-098` — required-object fire contact consumes and completes. When the
  designated belongings crate enters the bonfire, it is burned and the bounded
  puzzle completes; it does not remain as a placed target object.
- `SYS-084` is absent because no unsupported rigid-shape fall is required by
  the scoped solution. Climbing is a legal-transition constraint, not a
  continuously or discretely falling-body simulation.
- Resolution order: interpret directional input; validate the avatar and any
  carried-object footprint / sweep; resolve movement, pivot, grab or release;
  if the belongings contacts fire, consume it; test completion.
- Claim IDs: `BFP-005`, `BFP-008`, `BFP-010`, `BFP-012`.

### Constraint Genes

- `CON-001` — fixed occupancy capacity. The authored floor cells, elevation
  bands, walls, bonfire and one crate remain a finite unchanged puzzle.
- `CON-011` — exclusive occupancy with static barriers. Avatar and crate
  footprints cannot enter solid wall or unsupported occupied geometry.
- `CON-090` — oriented agent-plus-body sweep clearance. The held crate remains
  directly coupled in front and swings through a corner during a pivot, so a
  turn can be blocked even when the avatar's own cell stays free. Attachment
  through reversible grab rather than a permanent tool is a coupling
  parameter, not a second clearance predicate.
- `CON-101` — carry-conditioned elevation traversal. The staircase can be
  climbed only through approaches that provide valid destinations and
  clearance for both avatar and front-held crate; carrying makes climbing
  stricter than walking alone.
- `CON-100` is the merged historical alias for this Bonfire Peaks-specific
  carried form; no canonical signature uses it after normalisation 005.
- Claim IDs: `BFP-002`, `BFP-005`, `BFP-006`, `BFP-009`.

### Information Genes

- `INF-001` — fully visible current state. The complete local terrain, height
  bands, avatar facing, crate pose and bonfire are visible before each command.
- The excluded hint video and later unexplored overworld do not hide state
  required to solve `1.1`.
- Claim IDs: `BFP-002`, `BFP-009`.

### Objective Genes

- `OBJ-014` — deliver designated payload to fixed receiver. The
  specific belongings crate must be carried up the authored elevation route
  and put into the bonfire, which consumes it and ends the puzzle.
- Direct carrying and destructive consumption are parameters; the terminal
  predicate remains delivery of one designated payload to one fixed receiver.
- `OBJ-004` is absent because no persistent exact arrangement is displayed;
  the required object disappears on successful receiver contact.
- Claim IDs: `BFP-007`, `BFP-008`.

### Time Genes

- `TIM-001` — discrete turn with automatic resolution. Each input fully
  resolves the oriented avatar / crate transition and, on the terminal input,
  fire consumption and completion before the next decision.
- `TIM-002` is absent under the exclusive boundary because the decisive
  receiver input produces an automatic destructive completion response.
- Claim IDs: `BFP-008`, `BFP-010`, `BFP-011`.

## Reproducible transitions

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Avatar stands adjacent to the free belongings crate | Press Grab | Crate becomes held in the cell directly in front | portable acquisition and front offset | `BFP-004` |
| Avatar holds the crate with clear corner and destinations | Pivot ninety degrees | Avatar changes facing and crate sweeps to the new front cell | carried rotation occupies world geometry | `BFP-005` |
| The swept corner or future crate cell is blocked | Attempt the same pivot | Transition is rejected and both poses remain unchanged | legality includes more than avatar cell | `BFP-005` |
| Avatar and front-held crate approach a height change from a legal orientation | Move along the staircase route | Both footprints advance to compatible elevation-supported positions | carrying constrains climb geometry | `BFP-006` |
| Avatar reaches the upper approach with the belongings aligned to fire | Move / release the crate into the bonfire | Crate is consumed and the puzzle is credited | destructive delivery is the terminal predicate | `BFP-007`, `BFP-008` |
| Any non-terminal state follows a mistaken route | Undo or restart | Previous input or authored entry state is restored | recovery does not add a time-manipulation gene | `BFP-011` |

## Strategic and experiential structure

- Local decision: distinguish a pivot from translation and reserve the complete
  two-entity footprint needed by the next carried turn.
- Medium-term planning: orient the avatar so the crate's front cell and swept
  corner fit successive one-step elevation bands.
- Long-term structure: preserve the only required crate and deliver it intact
  to the upper bonfire, where destruction is success rather than failure.
- Common heuristics: plan the crate's cell, not only the character's; approach
  an ascent from the orientation that gives the held object clearance.
- Failure attribution: deterministic visible rejection makes blocked movement
  traceable to avatar occupancy, carried offset, swept corner or elevation.
- Claim IDs: `BFP-002`–`BFP-010`.

## Replay and variation

- The scoped entry state and transition rules are authored and deterministic;
  there is no random setup, opponent or time-driven mutation.
- Walking and pivots can contain harmless detours, but only one designated
  crate is consumed and the staircase sharply constrains its useful route.
- Replay comes from undo / restart or revisiting the excluded campaign, not
  procedural variation within `Burn Your Belongings`.
- Claim IDs: `BFP-001`, `BFP-002`, `BFP-009`–`BFP-012`.

## Adjacent systems and history

- Portal shares avatar navigation and portable-object pickup / release. Its
  cube is carried continuously in real-time physics and supports a pressure
  receiver; Bonfire Peaks discretises an occupied front offset, elevation and
  destructive delivery.
- Stephen's Sausage Roll shares an oriented two-cell actor/tool footprint and
  turn clearance. Its fork is permanent and pushes a tracked sausage; the
  Bonfire Peaks crate is detachable, held only temporarily and itself the
  required sacrificed object.
- Sokoban shares visible fixed occupancy and access planning, but only pushes a
  free crate and preserves it on a target instead of carrying and consuming it.
- A Monster's Expedition shares discrete avatar movement and height-like world
  geometry; its pushed log creates traversable topology rather than being held
  in front and burned.
- Claim IDs: `BFP-003`–`BFP-012`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-048` | oriented movement and grab / carry / release |
| System Behaviour | `SYS-098` | fire consumption and completion |
| Constraint | `CON-001`, `CON-011`, `CON-090`, `CON-101` | fixed geometry, occupied carry sweep and elevation |
| Information | `INF-001` | visible entry and current poses |
| Objective | `OBJ-014` | deliver the designated carried object to the bonfire |
| Time | `TIM-001` | discrete input and terminal resolution |

Canonical signature:

`ACT-008,ACT-048; SYS-098; CON-001,CON-011,CON-090,CON-101; INF-001; OBJ-014; TIM-001`

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `54` (`GAME-0001`–`GAME-0054`).
- Exact genome matches: none.
- Tied near matches: `GAME-0053` — Can of Wormholes (`5 / 14 = 0.357143`).
- Supported combination subsets: `COMB-0055`.
- Scan date: 2026-08-13.

### Selected-neighbour interpretation

No pre-migration reviewed selected-neighbour table row exists for: `GAME-0053`.

### Preserved research notes

- New genes originally included `SYS-098`, `CON-100`, `CON-101`, `OBJ-034`;
  normalisation 004 later merged `OBJ-034` into `OBJ-014`, and normalisation
  005 merged carried-clearance alias `CON-100` into `CON-090`.
- Reused genes: `ACT-008`, `ACT-048`, `CON-001`, `CON-011`, `INF-001`,
  `TIM-001`.
- Classification result: four `New gene` records and one verified interaction;
  no novelty claim.

## Combination record

- `COMB-0055` captures pickup, occupied front-offset turn / elevation planning,
  destructive receiver contact and completion under discrete resolution.
- Exhaustive supporter scan: only `GAME-0055` contains the complete new proper
  subset; no older combination is a proper subset of this genome.

## Taxonomy impact

- Generalised `ACT-048` from release into continuous live physics to release,
  drop or throw into the active world state, while retaining its controlled-
  offset boundary. Added four evidence-backed genes without changing any prior
  game signature.
- Initially kept detachable carried-object clearance (`CON-100`) distinct from
  permanent tool clearance (`CON-090`). Normalisation 005 later showed that
  attachment lifetime is a coupling parameter and merged the two constraints.

## Negative results

- `ACT-009`, `SYS-084`, `OBJ-004` and a return-pose objective fail the exact
  `1.1` boundary. Later free crates, stacking and
  overworld rewards cannot be imported into this introductory signature.
