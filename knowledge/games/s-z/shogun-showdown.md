---
game_id: GAME-0050
slug: shogun-showdown
game_title: Shogun Showdown
analysis_status: reviewed
reviewed: 2026-08-12
combination_ids:
  - COMB-0050
gene_ids:
  action:
    - ACT-008
    - ACT-064
    - ACT-065
    - ACT-066
    - ACT-067
  system:
    - SYS-090
    - SYS-091
  constraint:
    - CON-001
    - CON-011
    - CON-096
    - CON-097
  information:
    - INF-001
    - INF-027
  objective:
    - OBJ-029
  time:
    - TIM-001
---

# Game: Shogun Showdown

## Analysis scope

- Version / ruleset: released 1.0 base game on default Day 1 with the initially
  available Wanderer.
- Included unit: the first Camp mechanics tutorial and Bamboo Grove level 1,
  from its initial combat state through clearance of four waves and acceptance
  of the first post-level tile choice.
- Included mechanics: five-cell 1D combat field, facing, forward/backward
  movement, Wanderer swap, attack-tile queue editing and activation, attack
  geometry / damage, cooldown, exact next hostile step, automatic hostile
  response, Twin Tachi friendly fire, health, defeat, wave clearance and tile
  reward.
- Excluded: Bamboo Grove level 2 and boss; later regions, heroes, skills, tiles
  and enemies; Days 2–7 / corruption; run-wide shops and route choice;
  meta-unlocks, challenges, stamps, achievements and speedrunning.
- Direct-play status: not conducted. Product and creator sources establish the
  core loop; the official community wiki gives reproducible queue, enemy and
  level parameters, independently corroborated by two hands-on reviews. Wiki
  pages sometimes returned 403 on direct open, so cached search extracts are
  identified rather than treated as inaccessible primary documentation.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `SHO-001` | Bamboo Grove level 1 is a fixed five-position 1D field with four scheduled waves and a post-clear tile choice | Confirmed | Corroborated | High | W3, W5 |
| `SHO-002` | The player may step along the line or reverse facing; ordinary turn-costing actions are followed by hostile advancement | Confirmed | Corroborated | High | D1, S1, S2, W1 |
| `SHO-003` | The Wanderer exchanges positions with an enemy directly ahead by attempting forward movement into it | Confirmed | Corroborated | High | W2, C1 |
| `SHO-004` | A ready attack tile may be inserted into a freely editable ordered queue of at most three tiles | Confirmed | Corroborated | High | S1, W1, C2 |
| `SHO-005` | Activating the queue executes its tiles bottom-to-top as one player action before hostile response | Confirmed | Corroborated | High | S1, W1 |
| `SHO-006` | Used tiles become unavailable and regain one cooldown step at each turn boundary | Confirmed | Corroborated | High | W1 |
| `SHO-007` | Each enemy's exact next move, preparation or attack is visible before the player acts | Confirmed | Corroborated | High | S1, D1, W1 |
| `SHO-008` | After one turn-costing player input, every surviving foe automatically advances one visible behaviour step; no opposing player chooses a reply | Confirmed | Corroborated | High | D1, S1, S2, W1 |
| `SHO-009` | Twin Tachi executes its two-sided attack even when an allied enemy occupies the struck cell, enabling hostile friendly fire | Confirmed | Corroborated | High | S1, W4, C1 |
| `SHO-010` | Clearing every enemy in all four scheduled waves completes level 1 and presents a two-tile reward choice | Confirmed | Corroborated | High | S1, W1, W3, W5 |
| `SHO-011` | `INF-009` / `SYS-019` do not apply: only the next hostile step is committed at each player decision, not a complete attack retained through a bounded planning phase | Observation | Corroborated | High | SHO-007–SHO-009 |
| `SHO-012` | `TIM-001`, not `TIM-004`, `TIM-005` or `TIM-010`, captures the schedule because each player input is followed by automatic system resolution with no hostile decision-maker, multi-action phase or forecast revision | Observation | Corroborated | High | SHO-002, SHO-005, SHO-008 |
| `SHO-013` | `COMB-0014`, `COMB-0047` and `COMB-0048` are rejected, while the prepared-queue execution relation forms a distinct verified combination | Observation | Corroborated | High | SHO-004–SHO-012 |

## Basic data

- Release / origin: Roboatino developed Shogun Showdown; Goblinz Publishing and
  Gamera Games released version 1.0 on 5 September 2024.
- Platform or physical form: single-player digital turn-based combat roguelike
  on desktop and consoles.
- Puzzle family: action-alternating 1D exact-intent attack-queue tactics.
- Primary / creator sources:
  - **[P1]** [Official Steam product page](https://store.steampowered.com/app/2084000/Shogun_Showdown/),
    documenting release, positioning, attack-tile buildup / execution and
    roguelike progression.
  - **[D1]** [GOG creator interview](https://www.gog.com/en/news/gog_interview_learn_more_about_shogun_showdown_from_its_creator),
    documenting movement, turning, queueing and activation as turn actions on a
    1D grid.
- Hands-on sources:
  - **[S1]** [PC Gamer review](https://www.pcgamer.com/games/roguelike/shogun-showdown-review/),
    documenting action-for-action enemy response, visible next actions, queue
    length / execution, deterministic attack geometry, swaps and friendly fire.
  - **[S2]** [Nintendo Life review](https://www.nintendolife.com/reviews/switch-eshop/shogun-showdown),
    corroborating untimed positioning and automatic hostile response.
- Official community-wiki transition references:
  - **[W1]** [Tiles](https://shogunshowdown.wiki.gg/wiki/Tiles), for queue,
    activation, cooldown and tile-choice rules.
  - **[W2]** [Characters](https://shogunshowdown.wiki.gg/wiki/Characters), for
    the initially available Wanderer's forward swap.
  - **[W3]** [Bamboo Grove](https://shogunshowdown.wiki.gg/wiki/Bamboo_Grove),
    for the five-cell, four-wave level-1 unit and tile reward.
  - **[W4]** [Enemies](https://shogunshowdown.wiki.gg/wiki/Enemies), for
    Ashigaru / Twin Tachi parameters and allied-hit execution.
  - **[W5]** [Regions](https://shogunshowdown.wiki.gg/wiki/Regions), for wave
    progression and post-level choices.
- Narrow community controls / transition references:
  - **[C1]** [Twin Tachi mechanical page](https://shogun-showdown.fandom.com/wiki/Twin_Tachi),
    for its visible wait–queue–move–attack–retreat pattern and two-sided hit.
  - **[C2]** [Queue-order control discussion](https://steamcommunity.com/app/2084000/discussions/0/6404770645854433123/),
    used only to corroborate player reordering of queued tiles.
- Claim IDs: `SHO-001`–`SHO-013`.

## Mechanical decomposition

### Action Genes

- `ACT-008` — navigate controllable agent. The Wanderer steps one available
  position along the line when the destination is empty.
- `ACT-064` — reverse controlled-agent facing without changing position.
- `ACT-065` — edit bounded attack-execution queue by inserting a ready tile and
  optionally removing or reordering queued tiles before activation.
- `ACT-066` — activate the prepared queue as one committed input.
- `ACT-067` — swap with the faced adjacent enemy through the Wanderer's forward
  movement command.
- `ACT-019` is absent: early attack tiles carry fixed relative geometry and do
  not ask the player to select a remote target when played or activated.
- Claim IDs: `SHO-002`–`SHO-005`.

### System Behaviour Genes

- `SYS-090` — ordered prepared-attack queue execution. On activation, queued
  tiles resolve bottom-to-top from the state left by the previous tile.
- `SYS-091` — shared turn-clock state advancement. After each ordinary player
  action, every living enemy advances its displayed move / prepare / attack
  step and player cooldowns advance by one.
- `SYS-019` is absent: there is no separate end-of-planning hostile phase
  executing a complete previously committed attack set.
- `SYS-020` is absent in this scope. Wanderer swaps positions directly; Twin
  Tachi attacks but does not displace targets, and a newly selected push tile
  is not used before the scoped endpoint.
- Resolution order: accept a turn-costing movement / turn / queue insertion /
  queue activation; resolve the player transition and any complete attack
  queue; advance each surviving hostile one declared step; recharge cooldowns;
  resolve death / wave introduction / level clearance; accept the next input or
  display the tile choice.
- Claim IDs: `SHO-004`–`SHO-011`.

### Constraint Genes

- `CON-001` — fixed occupancy capacity: level 1 uses five addressed positions.
- `CON-011` — exclusive occupancy with boundaries. Units ordinarily cannot
  finish on one position; field edges limit motion, with Wanderer swap as a
  declared exchange exception.
- `CON-096` — no more than three tiles may occupy the attack queue.
- `CON-097` — a used attack tile cannot re-enter the queue until its turn-
  recharged cooldown returns to ready.
- Scarce resources: health, free line positions, facing, queue slots, ready
  attack tiles and turns before the visible hostile steps become dangerous.
- Claim IDs: `SHO-001`, `SHO-003`, `SHO-004`, `SHO-006`.

### Information Genes

- `INF-001` — current positions, facing, health, player tiles, queue, cooldown
  state and all active enemies are visible.
- `INF-027` — exact next hostile-step preview. Each enemy declares the one move,
  queue or attack step that will advance after the next turn-costing input.
- `INF-009` is absent because a complete attack does not remain committed while
  the player takes several setup actions; hostile state advances after each.
- `INF-025` is absent because the interface displays the actual next hostile
  step, not a reversible consequence simulation recomputed from a draft.
- Claim IDs: `SHO-007`, `SHO-011`.

### Objective Genes

- `OBJ-029` — incapacitate finite hostile encounter set. Level 1 ends after all
  enemies from its four scheduled waves have been defeated.
- No additional score objective is required in this scope. Run statistics and
  higher-difficulty performance stamps are excluded.
- Claim IDs: `SHO-001`, `SHO-010`.

### Time Genes

- `TIM-001` — one discrete player input is followed by queue, hostile,
  cooldown, wave and terminal resolution before the next input.
- `TIM-004` is absent: enemies are deterministic system actors, not an opposing
  decision-maker receiving an exclusive choice turn.
- `TIM-005` is absent: queue insertions themselves advance every foe, so the
  player has no bounded multi-action planning phase before hostile resolution.
- `TIM-010` is absent: no forecast / rewind / commit draft loop exists.
- Claim IDs: `SHO-002`, `SHO-005`, `SHO-008`, `SHO-012`.

## Reproducible transitions

| Before | Player action | Automatic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Adjacent forward cell empty | Move forward | Wanderer occupies it; all enemies advance one displayed step; cooldowns advance | Navigation plus shared turn clock | `SHO-002`, `SHO-008` |
| No adjacent movement needed but facing is wrong | Turn around | Position is retained; hostile / cooldown step still advances | Facing is a state-changing turn action | `SHO-002` |
| Ready attack tile outside a queue holding fewer than three | Insert tile | Tile enters chosen queue order; enemies advance one step | Queue setup is not free planning | `SHO-004`, `SHO-008` |
| Two or three attacks queued | Activate | Tiles execute bottom-to-top as one player action; then hostiles advance once | Ordered queue execution | `SHO-005` |
| Used tile has non-zero cooldown | Complete later turns | One pip recharges at each turn boundary until ready | Turn-based availability | `SHO-006` |
| Enemy stands immediately ahead of Wanderer | Move forward | Positions exchange; visible enemy step then resolves from its new geometry | Direct faced swap and intent redirection | `SHO-003`, `SHO-007` |
| Twin Tachi's visible two-sided attack is next and another enemy is adjacent | Take a safe turn-costing action | Twin Tachi attacks both adjacent cells even if one contains an ally | Hostile friendly fire without `SYS-020` | `SHO-009` |
| Final enemy of wave 4 is defeated | Finish player action and resolution | Level clears; two-tile choice appears and one may be accepted | Finite encounter objective and scoped endpoint | `SHO-010` |

## Strategic and experiential structure

- Local decision: choose a movement, facing or queue edit whose one-turn cost
  remains safe against every displayed next hostile step.
- Medium-term planning: align facing and range while charging an ordered burst;
  use an enemy body or Wanderer swap to change who occupies an imminent attack
  cell; time cooldown recovery across harmless hostile preparation steps.
- Long-term structure: clear four waves without exhausting positional escape
  space or health, preserving a queue / cooldown rhythm for later arrivals.
- Common heuristics: count setup actions, reorder multi-hit queues so early
  attacks expose later targets, and treat enemy attacks as usable geometry when
  their friendly-fire rule permits it.
- Failure attribution: exact next-step disclosure makes an avoidable hit highly
  traceable to one turn-costing input. Learned steps beyond the shown horizon
  can improve planning but are not required for immediate safety.
- Claim IDs: `SHO-004`–`SHO-010`.

## Replay and variation

- Within level 1, field size and wave count are fixed; enemy arrivals and the
  two offered reward tiles may vary under the run generator.
- Different queue orders, swap routes and cooldown stalls can clear the same
  encounter. The exact next hostile step remains visible for each decision.
- The accepted reward changes later-run capability but lies at the scoped
  endpoint; its downstream use is excluded.
- Claim IDs: `SHO-001`, `SHO-007`, `SHO-010`.

## Adjacent systems and history

- Into the Breach and Fights in Tight Spaces show complete committed hostile
  attacks before a bounded player phase. Shogun advances every foe after each
  setup action and therefore rejects their `TIM-005` core.
- Tactical Breach Wizards simulates reactive consequences from a revisable
  draft. Shogun has no forecast or current-turn rewind.
- Bad North is real-time with selection slowdown and indirect squad orders;
  Shogun's field changes only after discrete turn-costing inputs.
- A learned enemy pattern may forecast later steps, but only the exact next
  step is an Atlas information gene in this bounded unit.
- Claim IDs: `SHO-011`–`SHO-013`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-064`, `ACT-065`, `ACT-066`, `ACT-067` | input mapping, zero-time exceptions |
| System Behaviour | `SYS-090`, `SYS-091` | actor order, wave spawn timing |
| Constraint | `CON-001`, `CON-011`, `CON-096`, `CON-097` | field length, queue cap, cooldown values |
| Information | `INF-001`, `INF-027` | preview iconography, attack attributes |
| Objective | `OBJ-029` | wave closure, health failure |
| Time | `TIM-001` | turn-cost exception set |

Canonical signature:

`ACT-008,ACT-064,ACT-065,ACT-066,ACT-067; SYS-090,SYS-091; CON-001,CON-011,CON-096,CON-097; INF-001,INF-027; OBJ-029; TIM-001`

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `49` (`GAME-0001`–`GAME-0049`).
- Exact genome matches: none.
- Tied near matches: `GAME-0043` — Stephen’s Sausage Roll (`5 / 24 = 0.208333`); `GAME-0045` — Snakebird (`5 / 24 = 0.208333`).
- Supported combination subsets: `COMB-0050`.
- Scan date: 2026-08-12.

### Selected-neighbour interpretation

No pre-migration reviewed selected-neighbour table row exists for: `GAME-0043`, `GAME-0045`.

### Preserved research notes

- New combination: `COMB-0050`, the six-gene prepared attack-queue interaction.
- New genes: `ACT-064`, `ACT-065`, `ACT-066`, `ACT-067`, `SYS-090`, `SYS-091`,
  `CON-096`, `CON-097`, `INF-027`.
- Reused genes: `ACT-008`, `CON-001`, `CON-011`, `INF-001`, `OBJ-029`,
  `TIM-001`.
- Classification result: `New gene`. Each addition isolates a separately
  observable command, response, limitation or disclosure and survives the
  required intent / time counterexamples.

## Combination record

- `COMB-0050` combines queue editing, activation, ordered execution, three-slot
  capacity, turn-recharged availability and discrete resolution.
- Exhaustive supporter scan: only `GAME-0050`; no prior genome contains the
  complete proper subset. The record is verified, not novel.

## Taxonomy impact

- Nine bounded genes added and six reused; no prior signature changed.
- No taxonomy change, merge, split, lifecycle change or type move is justified.
- The player/system boundary is explicit: edit and activate are commands;
  ordered attack execution and whole-turn actor advancement are automatic.
- `TIM-001` remains representation-neutral enough to include all automatic
  Shogun state advancement after one input; `SYS-091` describes what that
  resolution specifically advances.

## Negative results

No new negative-result record is required. Search 002 already preserves the
bounded `TIM-005` rejection. This game analysis converts that lead into a full
positive genome without invalidating a canonical or novelty claim.

## Delta summary

## Нові факти

- [Confirmed | Corroborated | High] Queue construction itself costs turns and
  advances all foes; queue activation executes up to three attacks as one turn.
- [Confirmed | Corroborated | High] The interface exposes exactly one next
  hostile step, which is narrower than committed multi-action intent.
- [Observation | Corroborated | High] The schedule is discrete automatic
  resolution, not adversarial choice, bounded planning or forecast revision.

## Нові гени

- `ACT-064`–`ACT-067`, `SYS-090`–`SYS-091`, `CON-096`–`CON-097` and `INF-027`.

## Нові комбінації

- `COMB-0050` — bounded prepared attack queue with ordered activation and turn-
  recharged availability; one verified supporter, no novelty claim.

## Зміни таксономії

- [Observation | Corroborated | High] No taxonomy change and no prior genome
  rewrite.

## Нові питання

- Does another tactics game charge time for each queue insertion but execute
  the whole prepared attack list as one action?
- Which later Shogun enemy families change the one-step preview boundary through
  reactive, quick or multi-step intent?

## Наступна рекомендована гра

- [Hypothesis | Corroborated | High] `CHECKPOINT_052`, but only after two more
  separately authorised game analyses reach the regular four-game cadence.
- Immediate non-Goal next unit: `POST_GOAL_AUDIT_010` only if a maintainer wants
  a standalone audit beyond the terminal review embedded in this unit;
  otherwise return to targeted selection with Mini Motorways and Can of
  Wormholes retained.

## Чому саме вона

- [Hypothesis | Corroborated | High] The ten-unit Goal is complete at game 50,
  while the next scheduled corpus checkpoint remains game 52. No additional
  analysis should begin implicitly after the requested terminal condition.
