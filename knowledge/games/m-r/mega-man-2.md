---
game_id: GAME-0389
slug: mega-man-2
game_title: Mega Man 2
analysis_status: reviewed
reviewed: 2026-09-24
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-131
    - ACT-161
  system:
    - SYS-036
    - SYS-037
    - SYS-045
    - SYS-215
    - SYS-578
    - SYS-911
    - SYS-1047
    - SYS-1048
  constraint: []
  information:
    - INF-119
    - INF-192
    - INF-318
  objective:
    - OBJ-230
  time:
    - TIM-003
---

# Game: Mega Man 2

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Stage geometry,
enemy counts, health values and conveyor directions are parameters, not genes.

## Analysis scope

- Version / ruleset: the original North American English 1989 NES cartridge,
  manual code `NES-XR-USA`, at **Normal** difficulty, not the Japanese
  Famicom ruleset, Game Boy *Mega Man II*, *The Wily Wars* or a Legacy
  Collection wrapper. The exact cartridge ROM revision was not inspected.
- Structured analysis target: `GAME-0389` in
  [`knowledge/platforms/games.json`](../../platforms/games.json).
- Entry: a fresh start with Metal Man selected as the first of eight Robot
  Masters, at the first controllable state of his factory stage. Mega Man has
  the unlimited basic Mega Buster; no Robot Master weapon or later support
  item has yet been earned.
- Primary decision loop: read the next side-view span, move and jump against
  gravity and conveyor displacement, avoid pits and descending presses,
  shoot or bypass stage enemies, optionally collect recovery items and an
  E-Tank, then in the closed boss chamber alternate movement, jumps and
  Buster fire against Metal Man's thrown blades and remaining health.
- Positive terminal: defeat Metal Man, receive the Metal Blade weapon and
  return to the Robot Master selection state. No use of the new weapon or
  entry into another stage is analysed.
- Negative terminal: a pit, lethal stage hazard or depleted health costs a
  life. If lives remain, Mega Man returns within the selected stage; after
  exhausting the stock the Game Over / Continue boundary is reached. A
  Continue is outside this attempt and begins the last played stage anew.
- Included: player-directed running, jumping and Buster shots; gravity and
  collision; side-view local lookahead; conveyor-supported horizontal drift;
  timed presses, pits and moving enemies as route hazards; direct real-time
  combat; player and boss health; contact-collected energy and optional
  E-Tank use; finite lives; boss victory and weapon grant.
- Excluded: exact damage values, frame windows, checkpoint coordinates and
  every branch not evidenced by the sources; using any other Robot Master
  weapon or earned support item; beating the remaining seven Robot Masters
  or Wily stages; password continuation; later-port rewind, challenges and
  achievements; any claim of direct play or observed audiovisual timing.
- Reproducible parameterisation: choose Normal and Metal Man first, then
  record stage contact with each belt, pit, press, enemy and pickup; chosen
  route, jump and shot timing; E-Tank acquisition and use if any; current
  life/health stock; boss attack and player-health changes; victory grant or
  life-loss result. An undamaged clear, a damaged clear, an E-Tank-assisted
  clear and a failed attempt are all allowed outcomes, not prescribed plays.
- Potential scoped modules: another initial Robot Master and its different
  route; the acquired Metal Blade against a later boss; Wily stages; a
  Game Over Continue; the Famicom, Game Boy or collection editions.
- Direct-play status: none. The original Nintendo manual and Nintendo's NES
  Classic manual establish controls, first-stage selection, health, lives,
  recovery and weapon reward; two written original-NES stage routes support
  Metal Man-specific conveyor, hazard and boss layout. Neither a cartridge,
  ROM, controller trace nor video was inspected.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `MM2-001` | The North American manual offers Normal or Difficult, eight selectable Robot Masters, movement, jumping and Buster fire. | Confirmed | Direct | High | P1 |
| `MM2-002` | A fresh first Metal Man selection leaves only the unlimited basic weapon; defeated bosses award their weapon. | Confirmed | Direct | High | P1, P2 |
| `MM2-003` | Metal Man's stage couples side-view jumps and shots to conveyor floors, pits, presses and enemies. | Observation | Corroborated | High | S1, S2 |
| `MM2-004` | Contact pickups can restore energy or provide a carried E-Tank; spending one restores health before another hit. | Confirmed | Direct | High | P1, P2 |
| `MM2-005` | Health depletion or fatal terrain spends a finite life; exhausted lives lead to Game Over and Continue restarts the stage. | Confirmed | Direct | High | P1, P2 |
| `MM2-006` | Metal Man's enclosed fight has a moving belt, thrown blades and a displayed boss-health gauge. | Observation | Corroborated | Medium | P1, S1, S2 |
| `MM2-007` | Defeating Metal Man ends this selected stage and grants Metal Blade before another stage choice. | Observation | Corroborated | High | P1, S1, S2 |
| `MM2-008` | Exact conveyor reversal trigger, timings, damage values and return coordinates were not measured. | Observation | Direct | High | R1 |

## Basic data

- Release / origin: Capcom's 1989 North American NES *Mega Man 2*. This
  packet uses the original US English manual's Normal choice, not a later
  collection's optional features.
- Platform or physical form: one-player NES side-view action platformer with
  selectable Robot Master stages. The packet deliberately selects only one.
- Puzzle family: `FAM-010` real-time system pressure. Enemy and hazard state
  advances while the player aims, traverses belts and times survival decisions.
- Primary sources, checked 2026-09-24:
  - **[P1]** [Nintendo-hosted original North American NES instruction
    booklet](https://www.nintendo.co.jp/clv/manuals/en/pdf/CLV-P-NABBE.pdf),
    code `NES-XR-USA`; difficulty, controls, stage selection, pickups, lives
    and Robot Master rewards. Its scanned content was also cross-checked
    against a [text transcription](https://www.world-of-nintendo.com/manuals/nes/mega_man_2.shtml),
    which is not a separate primary witness.
  - **[P2]** [Nintendo's English NES Classic manual](https://www.nintendo.co.jp/clv/manuals/en/pdf/CLV-P-NABBE_en.pdf),
    original-game rules restated in the Classic wrapper; used only where it
    describes the inherited NES rules, not wrapper features.
- Corroborating routes:
  - **[S1]** [HonestGamers' original-NES Metal Man stage
    route](https://www.honestgamers.com/guides/mega-man-2/1/read/5.html),
    conveyors, E-Tank, presses, boss belt and Metal Blade reward.
  - **[S2]** [GameFAQs' independent NES guide](https://gamefaqs.gamespot.com/nes/563442-mega-man-2/faqs/6451),
    Metal Man stage hazards, belt and boss tactics; exact AI-trigger claims
    from this guide are not adopted.
  - **[R1]** this bounded source and play-status audit.
- Claim IDs: `MM2-001`–`MM2-008`.

## Mechanical decomposition

### Action Genes

- `ACT-008` — steer Mega Man through the side-view factory, including across
  conveyor segments, toward the boss chamber.
- `ACT-161` — fire the current Mega Buster at reachable enemies and Metal Man;
  choosing this first stage excludes acquired special weapons.
- `ACT-131` — optionally consume a carried E-Tank for an immediate health
  restoration rather than treating it as an automatic pickup effect.
- Parameters: horizontal input, jump/shot timing, target, carried tank and
  consumption moment. Claim IDs: `MM2-001`–`MM2-004`, `MM2-006`.

### System Behaviour Genes

- `SYS-036` — gravity, jump momentum and solid collisions resolve continuously
  while the player moves above pits and machinery.
- `SYS-037` — contact with a placed pickup credits its recovery or tank value
  without itself ending the stage.
- `SYS-045` — stage enemies and Metal Man continue their own locomotion as
  Mega Man moves; the precise boss AI trigger is not claimed.
- `SYS-215` — real-time shot, collision and hostile-hit resolution changes
  health while both sides continue acting.
- `SYS-578` — damage and compatible recovery change Mega Man's single current
  life-health pool; zero closes that life, then `SYS-911` handles finite stock.
- `SYS-911` — a fatal state subtracts a life and returns the controlled body
  within the stage while stock remains; Continue after Game Over is excluded.
- `SYS-1047` — a contacted factory conveyor displaces the standing avatar
  laterally while movement and jumping remain player-controlled. Unlike the
  discrete assembly conveyor `SYS-077`, this is a live platforming support.
- `SYS-1048` — defeating the selected Robot Master marks that stage cleared
  and grants its named weapon; the reward is not a random pickup or chest.
- Resolution order: local view → movement/jump/shot → belt, gravity and
  collision → enemy/hazard/projectile contact → health/pickup/life update →
  boss zero-health settlement → weapon grant and stage-selection return.
- Claim IDs: `MM2-002`–`MM2-007`.

### Constraint Genes

- No separate Active constraint is warranted for this packet. The first
  Buster has unlimited ammunition; the life stock is already resolved by
  `SYS-911`, and a specific timer or exact stage-key gate was not evidenced.
- Claim IDs: `MM2-001`, `MM2-002`, `MM2-005`.

### Information Genes

- `INF-119` — player health and carried resources, including an acquired
  E-Tank, are inspectable rather than hidden.
- `INF-192` — the scrolling side view reveals the present support, hazards
  and a limited forward slice, not the whole factory route at once.
- `INF-318` — the closed boss encounter displays Metal Man's remaining
  health, separate from the player's own bar.
- Claim IDs: `MM2-001`, `MM2-003`, `MM2-004`, `MM2-006`.

### Objective Genes

- `OBJ-230` — clear one selected Robot Master stage, defeat its guardian and
  return with its named weapon. Reaching the boss door alone, defeating a
  non-selected boss and finishing the whole campaign are different goals.
- Claim IDs: `MM2-002`, `MM2-007`.

### Time Genes

- `TIM-003` — hazards, enemies, projectiles and boss actions advance in real
  time while movement and firing commands are available. No global stage
  deadline is asserted.
- Claim IDs: `MM2-003`, `MM2-006`.

## Reproducible transitions

| Before | Action | Resolution | Decision boundary | Claim ID |
|---|---|---|---|---|
| Fresh Normal stage select | Choose Metal Man first | Factory entry with basic Buster and no inherited special weapon | Order fixes the available attack set | `MM2-001`, `MM2-002` |
| Mega Man stands on a moving belt | Hold or release a direction, then jump | Belt and player movement jointly determine horizontal position until airborne | The belt is active support, not a programmed assembly route | `MM2-003` |
| Pit or descending press ahead | Time a jump and traverse, or mistime contact | Safe passage or life loss according to collision | Looking ahead and timing matter without a stage clock | `MM2-003`, `MM2-005` |
| E-Tank has been contacted | Keep it or consume it after damage | Carried stock remains or restores missing health | Acquisition and use are separate decisions | `MM2-004` |
| Boss health remains | Evade a thrown blade and shoot with Buster | Both health pools change under real-time collisions | Boss attacks and conveyor motion continue during aiming | `MM2-006` |
| Metal Man health reaches zero | Finish the encounter | Metal Blade is granted and stage selection returns | Reward belongs to this boss-clear event | `MM2-007` |

## Strategic and experiential structure

- Local decision: distinguish when a conveyor helps or opposes a jump, and
  choose a safe Buster shot without walking into a pit or press.
- Medium-term planning: preserve health and optional E-Tank stock for the
  enclosed boss encounter. The first-boss choice deliberately removes any
  acquired-weapon shortcut from this packet.
- Long-term structure: Metal Blade is retained for later selectable stages;
  those later uses are outside the bounded terminal.
- Failure attribution: lethal terrain and depleted health both cost a finite
  life, whereas the boss's remaining-health gauge makes offensive progress
  visible. Exact damage and respawn coordinates are not claimed.
- Claim IDs: `MM2-002`–`MM2-008`.

## Replay and variation

- The authored stage layout and boss identity do not change in this scope.
  Route timing, losses, pickups and whether the E-Tank is spent can vary.
- Robot Master selection order is a larger game's replay variation; fixing
  Metal Man first here makes the available weapon set reproducible.
- No random stage geometry or unseen alternative boss AI has been inferred.

## Adjacent systems and history

- Other eight-stage orders can introduce acquired weapons and different boss
  strengths; they require their own scope, rather than silently assigning
  those weapons to this first-stage run.
- *Mega Man II* on Game Boy is a separate title. The Famicom original and
  NES Classic / Legacy Collection wrappers are not the selected ruleset.
- Unlike *Super Mario Bros.* World 1-1, the selected stage has live shot
  combat, belt-driven standing displacement and a boss-clear weapon grant;
  both share direct side-view movement and bounded forward lookahead.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | ACT-008, ACT-131, ACT-161 | direct traversal, optional tank use, Buster shot |
| System Behaviour | SYS-036, SYS-037, SYS-045, SYS-215, SYS-578, SYS-911, SYS-1047, SYS-1048 | physics, pickups, enemies, health, lives, belt, reward |
| Constraint | none | no finite Buster ammo or stage timer evidenced |
| Information | INF-119, INF-192, INF-318 | resources, local view, boss health |
| Objective | OBJ-230 | clear Metal Man stage and retain weapon |
| Time | TIM-003 | live control and hazards |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `388` (`GAME-0001`–`GAME-0388`).
- Exact genome matches: none.
- Tied near matches: `GAME-0312` — ASTRO BOT (`8 / 24 = 0.333333`).
- Supported combination subsets: none.
- Scan date: 2026-09-24.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0312` ASTRO BOT | `ACT-008`, `ACT-161`, `SYS-036`, `SYS-037`, `SYS-045`, `SYS-215`, `INF-192` and `TIM-003` share directly steered platform movement, attacks, contact pickups, live enemies and local lookahead. | Sky Garden uses three-dimensional detours, laser-hover, fixture interactions, Bot rescue and a temporary Inflate ability before a glass exit returns to the galaxy map. Metal Man's first NES factory stage uses live belt displacement, limited lives, optional E-Tank recovery and a sealed Robot Master fight that grants a named retained weapon. Similar traversal does not imply equivalent objectives or support physics. | `8 / 24 = 0.333333`; tied near maximum, not an equivalent stage loop |

### Preserved research notes

- New genes: `SYS-1047`, `SYS-1048`, `OBJ-230`.
- Reused genes: `ACT-008`, `ACT-131`, `ACT-161`, `SYS-036`, `SYS-037`,
  `SYS-045`, `SYS-215`, `SYS-578`, `SYS-911`, `INF-119`, `INF-192`,
  `INF-318`, `TIM-003`.
- Classification result: stage-specific live conveyor support and a
  guardian-to-weapon reward separate movement and combat from the selected
  stage's progression terminal.

## Taxonomy impact

- Registry changes: three additive Active genes in `TAXONOMY_CHANGE_128`.
- No earlier game signature, family definition or combination changes.

## Negative results

- Do not place Metal Blade in the initial loadout simply because Metal Man
  will award it after victory.
- Do not infer exact press periods, reversal triggers, damage points or
  checkpoint coordinates from written routes.
- Do not turn unlimited basic Buster fire into a finite-ammunition
  constraint or treat collection wrappers as the original NES cartridge.

## Delta summary

## New facts

- [Confirmed | Direct | High] A Normal first choice of Metal Man starts with
  Buster controls and can award Metal Blade on victory (`MM2-001`, `MM2-002`).
- [Observation | Corroborated | High] Conveyors and factory hazards alter a
  side-view shooting route before the Metal Man fight (`MM2-003`, `MM2-006`).

## New genes

- [Observation | Corroborated | Medium] `SYS-1047`, `SYS-1048` and `OBJ-230`
  isolate live belt displacement, named boss-weapon grant and the bounded
  stage-clear terminal.

## New combinations

- [Observation | Corroborated | High] No verified combination is registered.

## Taxonomy changes

- [Observation | Corroborated | Medium] `TAXONOMY_CHANGE_128` adds three
  source-bounded genes without revising older signatures.

## New questions

- What is the exact frame sequence of Metal Man's boss-conveyor reversal?
  It needs a direct cartridge trace and is not required by this genome.
- Which exact checkpoint and life-stock values occur on each failure path?
  The manuals establish the stock rule, not an observed route trace.

## Next recommended game

- [Hypothesis | Limited | Medium] GAME-0390 SimCity 2000.
- Optimisation criterion: alternate a live side-view boss stage with a
  simulation of zoning, services and budget consequences.
- Backlog impact: follows the selected nine-game order after a Goal stop
  window; it is not started by this game commit.

## Why this game

- [Hypothesis | Limited | Medium] A recognizable NES action platformer
  tests whether the Atlas distinguishes stage route mechanics, combat and
  retained boss reward within one small, reproducible play boundary.
