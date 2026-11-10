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
- The portal qualification separates Nether-frame ignition and remaining
  stronghold Eye-slot completion from entry into an active surface.
  Already-filled Eye slots count; activation need not move an avatar outside
  the surface, and existing active portals need not be activated again for
  travel. Nether waiting and immediate End entry are distinguished in
  historical publisher guides; no uniform positive delay or exact Java 26.2
  timer, cooldown, arrival/linking or carried-state persistence is certified.
  The post-Dragon exit remains part of the terminal, not evidence of a
  stronghold-frame activation cause; later End gateways, Bedrock/Creative
  timing and custom commands remain excluded. No version-identified native
  trace has been executed.
- Direct-play status: Direct play was not conducted. No identified Java 26.2
  executable, seeded save, input/tick trace, actual portal-rule settings or
  reload was inspected. The publisher Nether, End-frame, stronghold,
  flint-and-steel and Dragon guide bodies read during P5 distinguish
  activation, portal-type entry, occupied Eye slots and the separate
  post-Dragon exit. Historical Java 1.20.3 notes name Nether-specific delay
  controls; they do not certify the Java 26.2 configuration. The official Java
  26.2 release identity was read through the public web reader after direct
  HTTP retrieval returned 403. These sources motivate this portal-type
  qualification; exact delay, cooldown, destination/linking and carried-state
  persistence remain unverified. No video or audio was opened or played.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `MNC-001` | The player moves a persistent avatar, selects a carried quick-slot item and targets reachable blocks, fixtures or hostiles | Confirmed | Corroborated | High | P1, P2, P3 |
| `MNC-002` | Breaking and placing are distinct reachable voxel actions; a valid break may emit a collectible drop and a valid placement consumes a held block | Confirmed | Corroborated | High | P1, P3 |
| `MNC-003` | Contact pickup is bounded by slot/stack capacity, while eligible tool uses reduce durability | Confirmed | Corroborated | High | P1, P11 |
| `MNC-004` | Crafting consumes the exact supported 2×2 or 3×3 arrangement and exposes matching recipe-book state | Confirmed | Direct | High | P1, P4 |
| `MNC-005` | A seed determines terrain while local breaking and placement persistently reshape world geometry | Confirmed | Corroborated | High | P3, P5 |
| `MNC-006` | Activity, food and damage update hunger and health; ordinary death drops inventory and respawns the avatar in the same world | Confirmed | Direct | High | P2, P6, P10 |
| `MNC-007` | A valid ignited Nether frame creates an active surface; separate entry under the portal type's contact condition transfers the avatar and carried state, without a measured Java 26.2 delay/arrival trace | Confirmed | Direct | High | P9, P11 |
| `MNC-008` | Thrown Eyes reveal stronghold bearings and may shatter; all twelve stronghold End-frame slots, including generated occupied slots, create the active entry surface without requiring twelve newly inserted Eyes | Confirmed | Direct | High | P8, P13 |
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
  - **[P13]** [End Portal Frame](https://www.minecraft.net/en-us/article/block-week--end-portal-frame), historical publisher activation versus immediate End-entry guide; no exact Java 26.2 tick claim.
  - **[P14]** [Java 1.20.3](https://www.minecraft.net/en-us/article/minecraft-java-edition-1-20-3), historical Nether-specific delay controls, not a measured Java 26.2 configuration.
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
- `SYS-218` flies an Eye then drops or shatters. `SYS-219` creates Nether
  or stronghold End-entry surfaces from each type's frame/input condition;
  `SYS-220` separately transfers the avatar and carried state through an active
  surface under that portal type's entry rule. No universal positive hold or
  measured Java 26.2 timing is asserted. `SYS-221` heals the Dragon from active
  crystals without inventing an immunity gate.
- Claim IDs: `MNC-002`–`MNC-010`.

### Constraint Genes

- `CON-206` gates breaking; `CON-208` separately gates placement; `CON-207`
  requires exact crafting-grid contents; `CON-210` bounds pickup capacity.
  `CON-209` gates each admitted entry portal's typed frame/activation state;
  already occupied stronghold Eye slots count and the Dragon exit is not
  assigned that cause. `CON-136` captures the persistent dependency chain
  through Nether materials, Eyes, stronghold and Dragon.
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
| Complete valid obsidian frame; avatar outside its interior | Apply flint and steel | Create the active Nether surface; avatar need not travel | activation writes world state | `MNC-007` |
| Already-active Nether surface | Enter and satisfy its type/rule-specific contact condition | Transfer avatar and carried state; exact Java 26.2 delay/arrival unmeasured | traversal differs from activation | `MNC-007` |
| Eye held in Overworld | Throw it | It flies toward nearest stronghold, then drops or has a one-in-five shatter outcome | hidden route is sampled | `MNC-008` |
| Eleven stronghold End-frame slots filled, including any generated Eyes | Insert one Eye in the remaining empty slot | All twelve occupied slots create the active surface, not proof of avatar entry | frame completion and activation | `MNC-008` |
| Already-active stronghold End-entry surface | Enter the surface | Historical publisher guide describes immediate End transfer; exact Java 26.2 tick/arrival trace unmeasured | type-specific entry, not a universal positive hold | `MNC-008` |
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

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `128` (`GAME-0001`–`GAME-0128`).
- Exact genome matches: none.
- Tied near matches: `GAME-0087` — The Longest Journey (`4 / 41 = 0.097561`).
- Supported combination subsets: `COMB-0127`.
- Scan date: 2026-08-20.

### Selected-neighbour interpretation

No pre-migration reviewed selected-neighbour table row exists for: `GAME-0087`.

## Evidence and unknowns

- Official guides support documentary activation/entry distinctions, including
  a Nether wait and immediate End entry. They do not certify an exact Java 26.2
  input/tick trace, current portal-rule settings, cooldowns, arrival/linking or
  carried-state persistence. No direct run or reload was inspected. Hostile
  spawning remains adjacent and is not admitted by this direct-combat scope.

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
