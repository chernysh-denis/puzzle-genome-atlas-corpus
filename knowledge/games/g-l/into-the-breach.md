---
game_id: GAME-0014
slug: into-the-breach
game_title: Into the Breach
analysis_status: reviewed
reviewed: 2026-08-11
combination_ids:
  - COMB-0014
  - COMB-0047
gene_ids:
  action:
    - ACT-014
    - ACT-019
  system:
    - SYS-019
    - SYS-020
    - SYS-021
    - SYS-022
  constraint:
    - CON-001
    - CON-011
    - CON-034
    - CON-035
    - CON-036
  information:
    - INF-001
    - INF-009
  objective:
    - OBJ-011
  time:
    - TIM-005
---

# Game: Into the Breach

## Analysis scope

- Version / ruleset: the standard tactical battle loop in Subset Games' Into
  the Breach, including the current Advanced Edition where it does not alter
  the core loop.
- Included: one ordinary island battle; the mech planning phase; visible Vek
  attack intents and order; mech movement, weapons and repair; push, collision
  and terrain consequences; previewed environment events; marked emergence;
  civilian buildings, Power Grid failure and the bounded mission horizon.
- Excluded: island selection, Reactor Core upgrades, weapons inventory,
  reputation, pilots, achievements, squad unlocks, difficulty comparison,
  time-travel metaprogression and the final-island campaign ending.
- Direct-play status: not conducted for this record. Official product claims
  establish the defensive objective and telegraph premise; the mechanical
  phase detail is corroborated by specialist reference pages.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `ITB-001` | Civilian buildings power the mechs and must be defended from Vek attacks | Confirmed | Direct | High | F1, F2 |
| `ITB-002` | Every current enemy attack is telegraphed before the player commits the turn | Confirmed | Direct | High | F1, F2 |
| `ITB-003` | The player may move and use an ability with each available mech before ending the player phase | Confirmed | Corroborated | High | F3 |
| `ITB-004` | A mech normally cannot move after using its weapon, and mech order within the phase is player-selected | Confirmed | Corroborated | High | F3 |
| `ITB-005` | Surviving enemies execute their committed attacks in a visible order after the player phase | Confirmed | Corroborated | High | F3 |
| `ITB-006` | Displacement can retarget an attack, cause collision damage or expose a unit to hazardous terrain | Confirmed | Corroborated | High | F3, F4 |
| `ITB-007` | Environment events may expose affected positions before resolving in the round sequence | Confirmed | Corroborated | Medium | F3 |
| `ITB-008` | Spawn positions are marked one round ahead; occupying one blocks emergence and damages the blocker | Confirmed | Corroborated | Medium | F3, F5 |
| `ITB-009` | An ordinary battle has a finite round horizon and succeeds by surviving it with Grid power intact, not by killing every Vek | Confirmed | Corroborated | High | F3 |
| `ITB-010` | Power Grid reaching zero is terminal even if one or more mechs remain operational | Confirmed | Direct | High | F1, F4 |
| `ITB-011` | The enemy phase is automatic execution of disclosed commitments, not a second decision-maker choosing after the player | Observation | Corroborated | High | ITB-002, ITB-005 |
| `ITB-012` | The six-type model separates command, preview, resolution, action economy and mission survival without a taxonomy change | Observation | Corroborated | Medium | ITB-001–ITB-011 |

## Basic data

- Release: 27 February 2018.
- Developer / publisher: Subset Games.
- Platforms: originally Windows; later releases exist on other desktop,
  console and mobile platforms. Platform differences are outside scope.
- Puzzle family: deterministic turn-based tactical defence with previewed
  hostile intent.
- Sources:
  - **[F1]** [Subset Games — Into the Breach](https://subsetgames.com/itb.html):
    official description of powered civilian buildings, defence and
    telegraphed enemy attacks.
  - **[F2]** [Steam — Into the Breach](https://store.steampowered.com/app/590380/Into_the_Breach/):
    official store description and release metadata.
  - **[F3]** [Into the Breach Wiki — How to Play](https://game.wiki/into-the-breach/how-to-play):
    phase order, bounded battle, telegraph, push and survival details.
  - **[F4]** [Into the Breach Wiki — Vek](https://intothebreach.fandom.com/wiki/Vek):
    enemy intent, cancellation, Grid and unit-effect corroboration.
  - **[F5]** [Into the Breach Wiki — Spawn Tile](https://intothebreach.fandom.com/wiki/Spawn_Tile):
    one-round marker, blocking and blocking damage.
- Claim IDs: `ITB-001`–`ITB-012`.

## Mechanical decomposition

### Action Genes

- `ACT-014` — relocate selected controlled board piece. The player selects an
  available mech and a destination reachable under that mech's movement and
  terrain rules.
- `ACT-019` — select unit ability and target. The player chooses a mech weapon
  or repair and its target tile or footprint.
- Damage, push and collision are effects resolved from the selected ability,
  not additional player commands.
- Claim IDs: `ITB-003`, `ITB-004`, `ITB-006`.

### System Behaviour Genes

- `SYS-019` — ordered execution of committed hostile intents. When the player
  phase ends, able Vek execute the attacks whose targets and order were already
  shown; death, smoke or displacement may cancel or redirect the outcome.
- `SYS-020` — attack-induced displacement and collision resolution. Declared
  weapon effects push targets, then resolve collision and terrain consequences.
- `SYS-021` — scheduled battlefield-hazard resolution. Marked environmental
  effects resolve at their scheduled point without another command.
- `SYS-022` — marked enemy-emergence cycle. Marked tiles introduce new Vek in
  a later round unless occupied, in which case the blocker takes damage.
- Enemy intent selection before the player phase is retained as a parameter of
  the hostile cycle rather than admitted as a separate gene: the current
  sources establish the displayed commitment more strongly than the exact
  target-selection algorithm.
- Claim IDs: `ITB-005`–`ITB-008`, `ITB-011`.

### Constraint Genes

- `CON-001` — fixed occupancy capacity. The tactical map is a persistent grid
  of individually addressed positions.
- `CON-011` — exclusive occupancy with static barriers. A destination cannot
  end with two ordinary units; terrain and unit traits determine which cells a
  given mech may traverse or occupy.
- `CON-034` — per-unit move-then-ability allowance. Each mech has its own move
  and one ability opportunity; after committing the ability it normally cannot
  relocate that turn.
- `CON-035` — finite mission-round horizon. The battle completes after its
  declared final round if no terminal failure has occurred.
- `CON-036` — shared infrastructure depletion failure. Building damage reduces
  Grid integrity and zero Grid terminates the run independently of mech health.
- Claim IDs: `ITB-001`, `ITB-003`, `ITB-004`, `ITB-009`, `ITB-010`.

### Information Genes

- `INF-001` — fully visible current state. Current units, health, positions,
  terrain, buildings and active markers are inspectable; the scoped tactical
  state has no concealed board occupant.
- `INF-009` — exact committed hostile-intent preview. Attacker, affected tile,
  damage or effect and relative execution order are available before the player
  ends the phase.
- A marked spawn discloses where an emergence will occur but not enough in the
  reviewed sources to encode a separate exact reinforcement-identity preview.
  Campaign-level procedural generation is outside the battle genome.
- Claim IDs: `ITB-002`, `ITB-005`, `ITB-007`, `ITB-008`.

### Objective Genes

- `OBJ-011` — preserve protected infrastructure through horizon. The primary
  tactical objective is to keep the civilian-powered Grid above zero until the
  mission's bounded turn sequence completes.
- Killing every Vek is neither necessary nor the formal completion predicate;
  eliminating or redirecting enemies is instrumental. Mission-specific bonus
  objectives are parameters outside this baseline combination.
- Claim IDs: `ITB-001`, `ITB-009`, `ITB-010`.

### Time Genes

- `TIM-005` — planning phase before committed hostile resolution. The player
  sequences the squad's bounded commands, ends the phase, then watches scheduled
  environment, enemy and emergence events resolve before the next plan.
- This is not `TIM-004`: Vek do not observe the completed player phase and then
  choose an adversarial reply. It is not `TIM-001`: several independently
  ordered unit commands may be accumulated before one hostile-resolution phase.
- Claim IDs: `ITB-003`–`ITB-005`, `ITB-011`.

## Reproducible transitions

| Before | Player intervention | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| A Vek telegraphs damage onto a building | Push the Vek one tile sideways | Its committed attack resolves along the displaced line and misses the original building | Preview can be disrupted without killing | `ITB-002`, `ITB-006` |
| Two units are aligned with an empty destination beyond the target | Use a push weapon | Target shifts; collision is applied if the destination is occupied | Target selection differs from automatic effect | `ITB-006` |
| One mech has moved but not attacked | Select its weapon and target | Weapon resolves; that mech's later relocation is unavailable | Per-unit move-then-ability economy | `ITB-003`, `ITB-004` |
| A Vek is killed before its displayed attack step | End the player phase | Its committed attack does not execute | Intent is committed but conditionally cancelled | `ITB-005` |
| A unit ends on a marked spawn tile | End the round | Emergence is blocked and the occupying unit takes the declared damage | Previewed delayed reinforcement interaction | `ITB-008` |
| Final round completes with Grid above zero | Allow scheduled resolution to finish | Battle succeeds even if Vek remain | Survival horizon, not extermination | `ITB-009` |
| Building damage reduces Grid to zero | Resolve that damage | Attempt terminates even with surviving mechs | Shared infrastructure failure | `ITB-010` |

## Strategic and experiential structure

- Local decision: neutralise every threatening intent by killing, moving,
  blocking, disabling or sacrificing the least valuable target.
- Medium-term planning: retain mech positions and health, manage future spawn
  pressure and avoid solving one intent in a way that worsens the ordered
  resolution of another.
- Long-term structure: preserve Grid and optional mission assets across the
  finite horizon; enemy count matters only through future threat capacity.
- Dominant reasoning pattern: search for one action that changes several
  relations at once, such as moving a Vek off a building line and into another
  Vek's attack.
- Failure attribution: outcomes are legible because committed attacks and
  current board effects are previewed. Errors usually arise from an overlooked
  push, order dependency, terrain consequence or later-round position.
- Claim IDs: `ITB-002`–`ITB-011`.

## Replay and variation

- What changes between battles: map layout, buildings, terrain, enemy mix,
  mission-specific events and secondary objectives.
- What remains stable: the planning/hostile phase split, intent preview,
  per-mech action economy, displacement interactions and Grid defence.
- Randomness: campaign and mission generation vary attempts. This record does
  not infer an in-phase `SYS-004` transition because the reviewed evidence does
  not isolate when reinforcement identity is sampled.
- Typical replay motive: solve a different board-state forecast with a
  different squad toolset while managing the same defence structure.
- Claim IDs: `ITB-002`, `ITB-008`, `ITB-009`.

## Adjacent systems and history

- Chess shares selected-piece relocation and complete current-board visibility,
  but its opposing move is selected by another agent after the first move.
- Sokoban shares exclusive occupancy and displacement-sensitive spatial
  planning, but its push is directly embodied by the player agent and no
  hostile intent phase follows.
- Traditional turn-based tactics often hide or select enemy actions only after
  the player commits. Intent telegraphing is therefore a structural boundary,
  not merely a visual theme.
- Claim IDs: `ITB-002`, `ITB-006`, `ITB-011`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-014`, `ACT-019` | squad and weapon set |
| System Behaviour | `SYS-019`, `SYS-020`, `SYS-021`, `SYS-022` | enemy targeting algorithm; hazard and spawn schedules |
| Constraint | `CON-001`, `CON-011`, `CON-034`, `CON-035`, `CON-036` | terrain traits, Grid amount and mission length |
| Information | `INF-001`, `INF-009` | reinforcement-identity disclosure boundary |
| Objective | `OBJ-011` | optional secondary objectives |
| Time | `TIM-005` | phase order and undo boundary |

Canonical signature:

`ACT-014,ACT-019; SYS-019,SYS-020,SYS-021,SYS-022; CON-001,CON-011,CON-034,CON-035,CON-036; INF-001,INF-009; OBJ-011; TIM-005`

## Corpus comparison

- Indexed games scanned: `GAME-0001`–`GAME-0013`.
- Indexed combinations scanned: `COMB-0001`–`COMB-0013`.
- Exact genome matches: none.
- Existing combination subsets: none.
- Jaccard scores against complete genomes:
  - `GAME-0001`: shared `CON-001`, `INF-001`; `2 / 27 = 0.074074`.
  - `GAME-0002`: shared `CON-001`, `INF-001`; `2 / 20 = 0.100000`.
  - `GAME-0003`: shared `CON-001`; `1 / 23 = 0.043478`.
  - `GAME-0004`: shared `CON-001`, `INF-001`; `2 / 28 = 0.071429`.
  - `GAME-0005`: shared `CON-001`, `INF-001`; `2 / 20 = 0.100000`.
  - `GAME-0006`: shared `CON-001`, `CON-011`, `INF-001`; `3 / 21 = 0.142857`.
  - `GAME-0007`: shared `INF-001`; `1 / 22 = 0.045455`.
  - `GAME-0008`: shared `CON-001`, `INF-001`; `2 / 20 = 0.100000`.
  - `GAME-0009`: shared `CON-001`, `INF-001`; `2 / 29 = 0.068966`.
  - `GAME-0010`: shared `CON-001`, `INF-001`; `2 / 22 = 0.090909`.
  - `GAME-0011`: shared `ACT-014`, `CON-001`, `INF-001`; `3 / 25 = 0.120000`.
  - `GAME-0012`: shared `CON-001`, `INF-001`; `2 / 22 = 0.090909`.
  - `GAME-0013`: shared `CON-001`, `INF-001`; `2 / 26 = 0.076923`.
- Unique maximum near match: `GAME-0006` — Sokoban at `0.142857`.
- Long-form near comparison: both games make occupied cells and displacement
  geometry central. Sokoban directly pushes exactly one adjacent crate and has
  no automatic opponent; Into the Breach selects ranged abilities whose system
  effects can move either side before previewed hostile commitments resolve.
- Result: no exact signature or existing combination match. This is a corpus
  comparison only, not a novelty claim.

## Combination record

- Registered [`COMB-0014`](../../combinations/COMB-0014.md), a proper
  seven-gene subset centred on disrupting previewed hostile resolution with a
  bounded squad phase.
- It excludes general board occupancy, environment and emergence genes because
  those are not required to define the core intent-disruption structure.

## Taxonomy impact

- Four existing genes are reused and eleven bounded genes are added; the six
  existing gene types remain sufficient.
- No taxonomy-change record is required. Previewed hostile commitment belongs
  to Information, while its later execution remains System Behaviour.

## Negative results

- No taxonomy change is required. The difference from Chess is captured by
  `SYS-019`, `INF-009` and `TIM-005`, rather than by treating Vek as a second
  player.
- No `SYS-004` or `INF-002` is assigned. The sources establish generated
  battles but do not isolate reinforcement sampling as an in-phase random
  transition in the chosen scope.
- No kill objective is assigned: remaining enemies do not prevent victory when
  the mission horizon ends with Grid intact.
- No separate gene is created per weapon, environment or Vek class; their
  geometry and magnitude are parameters of bounded behaviours.
- `SYS-021` and `SYS-022` have medium confidence and should receive reuse or
  counterexample scrutiny at the 14-game checkpoint.

## Research notes

- Strongest finding: telegraphing is not merely additional visibility. It pairs
  with a later automatic execution phase, making hostile actions manipulable
  state commitments rather than predictions about a future decision-maker.
- Registry consequence: four earlier genes are reused and eleven bounded genes
  are admitted; all six existing types remain sufficient.
- Next evidence need: audit the enlarged registry before selecting
  `GAME-0015`, especially the single-game system behaviours and the boundary
  between phase scheduling and automatic resolution.

## Delta summary

## Нові факти

- Previewed hostile intents become manipulable commitments because player
  displacement occurs before a separate automatic execution phase.
- Mission success is horizon-and-Grid based; killing every remaining enemy is
  not required.

## Нові гени

- Added `ACT-019`, `SYS-019`–`SYS-022`, `CON-034`–`CON-036`, `INF-009`,
  `OBJ-011` and `TIM-005`; four earlier genes are reused.

## Нові комбінації

- Registered `COMB-0014`; no earlier combination is a subset of this genome.

## Зміни таксономії

- None. All distinctions fit the existing six-type model.
