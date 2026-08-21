---
game_id: GAME-0129
slug: minecraft
game_title: Minecraft
analysis_status: reviewed
reviewed: 2026-08-20
combination_ids:
  - COMB-0127
gene_ids:
  action:
    - ACT-008
    - ACT-087
    - ACT-093
    - ACT-159
    - ACT-160
    - ACT-161
    - ACT-162
    - ACT-163
    - ACT-164
    - ACT-165
  system:
    - SYS-212
    - SYS-213
    - SYS-214
    - SYS-215
    - SYS-216
    - SYS-217
    - SYS-218
    - SYS-219
    - SYS-220
    - SYS-221
    - SYS-222
    - SYS-223
  constraint:
    - CON-136
    - CON-206
    - CON-207
    - CON-208
    - CON-209
    - CON-210
  information:
    - INF-001
    - INF-073
    - INF-074
    - INF-075
    - INF-076
  objective:
    - OBJ-064
  time:
    - TIM-003
---

# Game: Minecraft

## Analysis scope

- Version / ruleset: Minecraft Java Edition 26.2, single-player Survival on
  Normal difficulty, from a new seeded world through the first Ender Dragon
  defeat and entry into the exit portal for the End Poem and credits.
- Included: movement; hotbar selection; block breaking, drops, pickup and
  placement; 2×2/3×3 crafting; durability; hunger, food, health, ordinary death
  and respawn; combat; Nether access; Eyes of Ender, stronghold and End-portal
  completion; Dragon crystal healing and the ending.
- Excluded: Creative, Hardcore, Adventure and spectator modes; multiplayer;
  commands, datapacks, mods, Redstone automation, enchanting, breeding, trading,
  farms, villages as optimisation and post-dragon End exploration.
- Direct-play status: not conducted. Official release notes and official
  Minecraft guides establish the scoped transitions.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `MNC-001` | The player moves a persistent avatar, selects a carried quick-slot item and targets reachable blocks, fixtures or hostiles | Confirmed | Corroborated | High | P1, P2, P3 |
| `MNC-002` | Breaking and placing are distinct reachable voxel actions; a valid break may emit a collectible drop and a valid placement consumes a held block | Confirmed | Corroborated | High | P1, P3 |
| `MNC-003` | Contact pickup is bounded by slot/stack capacity, while eligible tool uses reduce durability | Confirmed | Corroborated | High | P1, P11 |
| `MNC-004` | Crafting consumes the exact supported 2×2 or 3×3 arrangement and exposes matching recipe-book state | Confirmed | Direct | High | P1, P4 |
| `MNC-005` | A seed determines terrain while local breaking and placement persistently reshape world geometry | Confirmed | Corroborated | High | P3, P5 |
| `MNC-006` | Activity, food and damage update hunger and health; ordinary death drops inventory and respawns the avatar in the same world | Confirmed | Direct | High | P2, P6, P10 |
| `MNC-007` | A valid ignited Nether frame activates a portal whose contact transfers the avatar to the Nether | Confirmed | Direct | High | P9, P11 |
| `MNC-008` | Thrown Eyes reveal stronghold bearings and may shatter; filling all twelve End-frame slots activates the portal | Confirmed | Direct | High | P8 |
| `MNC-009` | Direct combat can defeat the Dragon while intact End crystals heal it; crystal destruction removes healing but is not a formal damage prerequisite | Confirmed | Direct | High | P7 |
| `MNC-010` | Dragon defeat activates the exit portal; entering it presents the End Poem and credits while the world remains playable | Confirmed | Direct | High | P7 |

## Basic data

- Release / origin: Mojang Studios; Java Edition 26.2 is the scoped stable
  release on the review date.
- Platform or physical form: first-person voxel-world survival, construction
  and exploration game.
- Puzzle family: world topology and perspective; real-time system pressure;
  ordered dependency sequencing.
- Primary sources:
  - **[P1]** [How to Minecraft](https://www.minecraft.net/en-us/article/how-minecraft), official block, tool, crafting-table and shelter guide.
  - **[P2]** [What is Minecraft](https://www.minecraft.net/en-us/article/what-minecraft), official Survival, tool, hunger and health boundary.
  - **[P3]** [Break and Place tutorial](https://education.minecraft.net/en-us/trainings/tutorial-2-place-and-break), official breaking, hotbar and placement guide.
  - **[P4]** [How to craft](https://www.minecraft.net/en-us/article/how-craft), official grid, exact ingredient and recipe-book guide.
  - **[P5]** [Snapshot 21w41a](https://www.minecraft.net/en-us/article/minecraft-snapshot-21w41a), official seed/world-generation boundary.
  - **[P6]** [Health in Minecraft](https://www.minecraft.net/en-us/article/health-minecraft), official hunger, regeneration, damage and starvation guide.
  - **[P7]** [Ender Dragon](https://www.minecraft.net/en-us/article/ender-dragon), official Dragon, crystal healing, exit portal and credits guide.
  - **[P8]** [Stronghold](https://www.minecraft.net/en-us/article/stronghold), official Eye locating, shatter chance and End-frame completion guide.
  - **[P9]** [Visit the Nether](https://www.minecraft.net/en-us/article/visit-nether-), official obsidian-frame construction and ignition guide.
  - **[P10]** [Spawning and dying](https://www.minecraft.net/en-us/article/spawning-and-dying), official dropped inventory, item lifetime and respawn guide.
  - **[P11]** [Flint and Steel](https://www.minecraft.net/en-us/article/flint-and-steel), official portal lighting and durability guide.
  - **[P12]** [Minecraft Java Edition 26.2](https://feedback.minecraft.net/hc/en-us/articles/46690753273997-Minecraft-Java-Edition-26-2), official stable release record.
- Claim IDs: `MNC-001`–`MNC-010`.

## Mechanical decomposition

### Action Genes

- `ACT-008` navigates; `ACT-164` selects the active item; `ACT-159` breaks a
  block; `ACT-162` separately requests placement. `ACT-160` arranges crafting
  grids; `ACT-165` consumes food; `ACT-161` attacks. `ACT-087` applies flint and
  steel; `ACT-163` throws an Eye; `ACT-093` fills an End-frame slot.
- Claim IDs: `MNC-001`–`MNC-004`, `MNC-006`–`MNC-009`.

### System Behaviour Genes

- `SYS-212` resolves break/drop; `SYS-217` placement; `SYS-222` pickup;
  `SYS-223` durability. `SYS-213` generates the seed world; `SYS-214` updates
  hunger/health; `SYS-216` resolves death/drop/respawn; `SYS-215` combat.
- `SYS-218` flies an Eye then drops or shatters. `SYS-219` activates valid
  portals; `SYS-220` transfers between dimensions. `SYS-221` heals the Dragon
  from active crystals without inventing an immunity gate.
- Claim IDs: `MNC-002`–`MNC-010`.

### Constraint Genes

- `CON-206` gates breaking; `CON-208` separately gates placement; `CON-207`
  requires exact crafting-grid contents; `CON-210` bounds pickup capacity;
  `CON-209` requires complete portal frames. `CON-136` captures the persistent
  dependency chain through Nether materials, Eyes, stronghold and Dragon.
- Claim IDs: `MNC-002`–`MNC-004`, `MNC-007`–`MNC-010`.

### Information Genes

- `INF-001` exposes the local world; `INF-073` the hotbar; `INF-074` crafting;
  `INF-075` survival/durability meters; `INF-076` the Eye's temporary bearing.
- Claim IDs: `MNC-001`, `MNC-003`, `MNC-004`, `MNC-006`, `MNC-008`.

### Objective Genes

- `OBJ-064` requires reaching The End, defeating the Dragon and entering the
  exit portal; play can continue afterward.
- Claim IDs: `MNC-010`.

### Time Genes

- `TIM-003` keeps hunger, danger and combat changing during other actions.
- Claim IDs: `MNC-001`, `MNC-006`, `MNC-009`.

## Reproducible transitions

| Before | Action | Deterministic or bounded resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Reachable tree block | Hold break | Block is removed; eligible drop appears; contact picks it up if capacity exists | break, drop and pickup are separate | `MNC-002`, `MNC-003` |
| Held block; compatible reachable voxel | Use placement | One unit is consumed and the block changes geometry | placement has its own action and gate | `MNC-002` |
| Exact recipe in supported grid | Take output | Inputs are consumed and output is received | spatial arrangement is causal | `MNC-004` |
| Hungry avatar; food selected | Hold use | Food is consumed; hunger rises; high hunger permits regeneration | food action and survival update differ | `MNC-006` |
| Health reaches zero | No input required | Inventory drops; avatar respawns; persistent world continues | death is recoverable but materially lossy | `MNC-006` |
| Complete obsidian frame | Apply flint and steel | Portal activates; sustained contact transfers the avatar | activation and traversal differ | `MNC-007` |
| Eye held in Overworld | Throw it | It flies toward nearest stronghold, then drops or has a one-in-five shatter outcome | hidden route is sampled | `MNC-008` |
| Eleven End-frame slots filled | Insert last Eye | All twelve fill and portal activates | persistent typed completion gates access | `MNC-008` |
| Dragon linked to a crystal | Attack Dragon or crystal | Dragon may regain health; destroying crystal stops only that source | crystals are strategic, not a hard prerequisite | `MNC-009` |
| Dragon dead; exit portal active | Enter portal | End Poem and credits play; world remains | ending differs from world deletion | `MNC-010` |

## Strategic and experiential structure

- Local decision: select the held item, block, placement, recipe, food timing or
  combat target that improves immediate access and safety.
- Medium-term planning: maintain tools, capacity, food and shelter while
  converting resources into Nether access and Eyes.
- Long-term structure: locate the stronghold, complete the End portal and
  prepare enough equipment to out-damage or suppress crystal healing.
- Failure attribution: visible world, hotbar, grids and meters explain most
  local failures; unexplored terrain and Eye loss remain uncertain.

## Replay and variation

- What changes: seed, terrain, resource/structure locations, build path,
  equipment route, death recovery and Dragon tactics.
- Randomness: terrain is seed-determined; Eye drop/shatter is probabilistic.
- Multiple viable strategies: yes, under the same scoped ending.

## Adjacent systems and history

- Similar games: Terraria, Satisfactory, Valheim and Dragon Quest Builders.
- Important differences: direct voxel mutation and exact grid crafting rather
  than a self-running factory or authored level.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-087`, `ACT-093`, `ACT-159`–`ACT-165` | target, held item, grid, combat |
| System Behaviour | `SYS-212`–`SYS-223` | generation, survival, portals, Dragon |
| Constraint | `CON-136`, `CON-206`–`CON-210` | reach, recipe, inventory, portal |
| Information | `INF-001`, `INF-073`–`INF-076` | world, carried, crafting, meters, bearing |
| Objective | `OBJ-064` | Dragon and exit portal |
| Time | `TIM-003` | live tick |

## Corpus comparison

- Genome signature `(ACT; SYS; CON; INF; OBJ; TIM)`: `ACT-008,ACT-087,ACT-093,ACT-159,ACT-160,ACT-161,ACT-162,ACT-163,ACT-164,ACT-165; SYS-212,SYS-213,SYS-214,SYS-215,SYS-216,SYS-217,SYS-218,SYS-219,SYS-220,SYS-221,SYS-222,SYS-223; CON-136,CON-206,CON-207,CON-208,CON-209,CON-210; INF-001,INF-073,INF-074,INF-075,INF-076; OBJ-064; TIM-003`.
- Indexed games scanned: 129, including this record.
- Indexed combinations scanned: 127.
- Exact genome matches: none.
- Near matches and similarity scores: `GAME-0087` is highest at `4 / 41 = 0.097561`.
- Supported combination subsets: `COMB-0127`.
- Scan date: 2026-08-20.

### Full prior-game Jaccard scan

- GAME-0001: 1 / 48 = 0.020833; GAME-0002: 1 / 41 = 0.024390; GAME-0003: 0 / 44 = 0.000000; GAME-0004: 2 / 48 = 0.041667.
- GAME-0005: 1 / 41 = 0.024390; GAME-0006: 2 / 42 = 0.047619; GAME-0007: 1 / 42 = 0.023810; GAME-0008: 1 / 41 = 0.024390.
- GAME-0009: 1 / 50 = 0.020000; GAME-0010: 1 / 43 = 0.023256; GAME-0011: 1 / 47 = 0.021277; GAME-0012: 1 / 43 = 0.023256.
- GAME-0013: 1 / 47 = 0.021277; GAME-0014: 1 / 49 = 0.020408; GAME-0015: 1 / 48 = 0.020833; GAME-0016: 2 / 48 = 0.041667.
- GAME-0017: 0 / 48 = 0.000000; GAME-0018: 2 / 52 = 0.038462; GAME-0019: 1 / 44 = 0.022727; GAME-0020: 1 / 48 = 0.020833.
- GAME-0021: 2 / 42 = 0.047619; GAME-0022: 1 / 46 = 0.021739; GAME-0023: 0 / 45 = 0.000000; GAME-0024: 1 / 46 = 0.021739.
- GAME-0025: 2 / 44 = 0.045455; GAME-0026: 2 / 45 = 0.044444; GAME-0027: 2 / 45 = 0.044444; GAME-0028: 2 / 50 = 0.040000.
- GAME-0029: 3 / 44 = 0.068182; GAME-0030: 2 / 47 = 0.042553; GAME-0031: 1 / 45 = 0.022222; GAME-0032: 1 / 45 = 0.022222.
- GAME-0033: 3 / 45 = 0.066667; GAME-0034: 3 / 46 = 0.065217; GAME-0035: 3 / 50 = 0.060000; GAME-0036: 2 / 45 = 0.044444.
- GAME-0037: 1 / 43 = 0.023256; GAME-0038: 3 / 48 = 0.062500; GAME-0039: 1 / 43 = 0.023256; GAME-0040: 2 / 41 = 0.048780.
- GAME-0041: 3 / 43 = 0.069767; GAME-0042: 1 / 43 = 0.023256; GAME-0043: 2 / 47 = 0.042553; GAME-0044: 2 / 43 = 0.046512.
- GAME-0045: 2 / 47 = 0.042553; GAME-0046: 1 / 44 = 0.022727; GAME-0047: 1 / 48 = 0.020833; GAME-0048: 1 / 48 = 0.020833.
- GAME-0049: 0 / 44 = 0.000000; GAME-0050: 2 / 48 = 0.041667; GAME-0051: 2 / 49 = 0.040816; GAME-0052: 1 / 44 = 0.022727.
- GAME-0053: 2 / 42 = 0.047619; GAME-0054: 2 / 44 = 0.045455; GAME-0055: 2 / 43 = 0.046512; GAME-0056: 1 / 42 = 0.023810.
- GAME-0057: 1 / 42 = 0.023810; GAME-0058: 1 / 43 = 0.023256; GAME-0059: 1 / 41 = 0.024390; GAME-0060: 1 / 41 = 0.024390.
- GAME-0061: 1 / 44 = 0.022727; GAME-0062: 1 / 42 = 0.023810; GAME-0063: 1 / 41 = 0.024390; GAME-0064: 1 / 39 = 0.025641.
- GAME-0065: 0 / 42 = 0.000000; GAME-0066: 0 / 45 = 0.000000; GAME-0067: 0 / 43 = 0.000000; GAME-0068: 0 / 43 = 0.000000.
- GAME-0069: 1 / 42 = 0.023810; GAME-0070: 1 / 42 = 0.023810; GAME-0071: 1 / 41 = 0.024390; GAME-0072: 1 / 42 = 0.023810.
- GAME-0073: 1 / 41 = 0.024390; GAME-0074: 1 / 43 = 0.023256; GAME-0075: 1 / 43 = 0.023256; GAME-0076: 1 / 41 = 0.024390.
- GAME-0077: 1 / 41 = 0.024390; GAME-0078: 1 / 41 = 0.024390; GAME-0079: 1 / 41 = 0.024390; GAME-0080: 1 / 41 = 0.024390.
- GAME-0081: 1 / 42 = 0.023810; GAME-0082: 1 / 42 = 0.023810; GAME-0083: 1 / 42 = 0.023810; GAME-0084: 1 / 44 = 0.022727.
- GAME-0085: 2 / 44 = 0.045455; GAME-0086: 3 / 45 = 0.066667; GAME-0087: 4 / 41 = 0.097561; GAME-0088: 2 / 42 = 0.047619.
- GAME-0089: 3 / 41 = 0.073171; GAME-0090: 3 / 47 = 0.063830; GAME-0091: 3 / 41 = 0.073171; GAME-0092: 2 / 43 = 0.046512.
- GAME-0093: 1 / 43 = 0.023256; GAME-0094: 3 / 42 = 0.071429; GAME-0095: 3 / 44 = 0.068182; GAME-0096: 3 / 42 = 0.071429.
- GAME-0097: 3 / 40 = 0.075000; GAME-0098: 3 / 39 = 0.076923; GAME-0099: 2 / 41 = 0.048780; GAME-0100: 1 / 45 = 0.022222.
- GAME-0101: 0 / 45 = 0.000000; GAME-0102: 0 / 42 = 0.000000; GAME-0103: 1 / 43 = 0.023256; GAME-0104: 2 / 42 = 0.047619.
- GAME-0105: 2 / 43 = 0.046512; GAME-0106: 0 / 42 = 0.000000; GAME-0107: 2 / 41 = 0.048780; GAME-0108: 2 / 43 = 0.046512.
- GAME-0109: 1 / 50 = 0.020000; GAME-0110: 2 / 41 = 0.048780; GAME-0111: 3 / 39 = 0.076923; GAME-0112: 3 / 40 = 0.075000.
- GAME-0113: 3 / 46 = 0.065217; GAME-0114: 2 / 40 = 0.050000; GAME-0115: 1 / 40 = 0.025000; GAME-0116: 3 / 38 = 0.078947.
- GAME-0117: 2 / 41 = 0.048780; GAME-0118: 1 / 50 = 0.020000; GAME-0119: 2 / 56 = 0.035714; GAME-0120: 0 / 64 = 0.000000.
- GAME-0121: 1 / 57 = 0.017544; GAME-0122: 2 / 48 = 0.041667; GAME-0123: 2 / 71 = 0.028169; GAME-0124: 2 / 80 = 0.025000.
- GAME-0125: 2 / 75 = 0.026667; GAME-0126: 2 / 76 = 0.026316; GAME-0127: 2 / 81 = 0.024691; GAME-0128: 2 / 49 = 0.040816.

## Evidence and unknowns

- Official sources corroborate all admitted transitions. Direct play would
  refine timing and numeric parameters. Hostile spawning is adjacent but not
  admitted because this scope models direct combat without its full spawn model.

## Verification status

- Structure, evidence, web, localisation, artwork and validation: reviewed.

## Taxonomy impact

- Revised genes: `ACT-159`, `SYS-212`, `SYS-214`, `SYS-215`, `CON-206`, `INF-073`.
- New genes: `ACT-162`–`ACT-165`, `SYS-216`–`SYS-223`, `CON-208`–`CON-210`, `INF-074`–`INF-076`.
- Reused here: `ACT-087`, `ACT-093`, `CON-136`.
- New family: none; `FAM-010`, `FAM-014` and `FAM-017` fit.

## Negative results

- `ACT-123` rejected: grid arrangement is causal, not a selected craft queue.
- `SYS-156` rejected: no autonomous production entity.
- `SYS-116` rejected: frame completion activates a portal, not a generic reward.
- `CON-175` rejected: ordinary Survival death respawns.
- A hard "destroy every crystal first" constraint is rejected: crystals heal
  the Dragon but do not make it categorically immune to ordinary damage.

## Delta summary

## Нові факти

- Replaced a fourteen-gene compound draft with an atomic thirty-five-gene
  genome covering the complete survival-to-credits route.
- Separated break, placement, pickup, durability, survival meters, death,
  portal activation/traversal, Eye locating and crystal healing.
- Corrected the Dragon claim and grounded the 26.2 boundary officially.

## Нові гени

- Added eighteen atomic genes and narrowed six compound draft genes as listed
  in Taxonomy impact.

## Нові комбінації

- Reworked `COMB-0127` as a proper subset of the complete scoped genome.

## Зміни таксономії

- Added Minecraft to existing `FAM-010`; retained `FAM-014` and `FAM-017`.
