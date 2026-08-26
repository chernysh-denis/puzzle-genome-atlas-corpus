---
game_id: GAME-0144
slug: clair-obscur-expedition-33
game_title: Clair Obscur: Expedition 33
analysis_status: reviewed
reviewed: 2026-08-21
combination_ids:
  - COMB-0142
gene_ids:
  action:
    - ACT-008
    - ACT-019
    - ACT-040
    - ACT-131
    - ACT-161
    - ACT-191
    - ACT-222
    - ACT-223
    - ACT-224
    - ACT-225
  system:
    - SYS-299
    - SYS-355
    - SYS-356
    - SYS-357
    - SYS-358
    - SYS-359
    - SYS-360
    - SYS-361
    - SYS-362
    - SYS-363
    - SYS-364
  constraint:
    - CON-269
    - CON-270
    - CON-282
    - CON-323
    - CON-324
    - CON-325
  information:
    - INF-119
    - INF-125
    - INF-141
    - INF-142
    - INF-143
  objective:
    - OBJ-029
  time:
    - TIM-001
    - TIM-003
---

# Game: Clair Obscur: Expedition 33

## Analysis scope

- Version / ruleset: PC Standard Edition at public patch `v1.5.6`, released
  2026-06-30; a fresh single-player save on the default `Expeditioner`
  difficulty, from entry into Spring Meadows through the first successful Goblu
  defeat in Flying Waters and the next deliberate Expedition Flag or campsite
  rest.
- Included: authored third-person exploration; visible field enemies and First
  Strike; the early three-member Gustave, Lune and Maelle party; visible turn
  order; basic attack, Skill, Item and Free Aim commands; Action Points; timed
  offensive inputs; dodge, parry and available jump defence; weak points;
  character resources or stances; health, status and Break; battle defeat and
  Retry; loot, XP, levels, attributes and skills; weapons, Pictos, four-battle
  Lumina mastery; recovery-item refill and enemy respawn on rest.
- Reproducible checkpoint: enter one reachable roaming Nevron from ordinary
  contact and from an equivalent legal First Strike; in battle spend AP on one
  Free Aim shot and one Skill, deliberately succeed and miss one offensive
  prompt, dodge one attack and fully parry one multi-hit sequence, then Break
  and defeat the encounter. Equip a newly acquired Picto through four legal
  victories, activate its learned Lumina within capacity, spend the first
  available character build point and rest at the next activated flag. Trace a
  defeated-party Retry from the same checkpoint separately.
- Excluded: Story and Expert timing-window parameters; automated QTE assist;
  later acts, party members and relationship quests; Gradient Attacks and
  late-game systems not available on the bounded route; optional superbosses,
  challenge modifiers, the Verso's Drafts anniversary environment, New Game
  Plus, trophies, cosmetics, Deluxe content and exhaustive weapons, skills,
  Pictos, statuses or narrative branches.
- Direct-play status: no new paid-account play session was conducted. Current
  official patch notes and creator material establish the version boundary;
  official platform demonstrations and reproduced early-game descriptions
  establish the scoped transitions. Exact balance values remain parameters.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `COE-001` | PC patch v1.5.6 is the current reviewed public baseline and preserves the established reactive combat loop | Confirmed | Corroborated | High | P1, P2, P4 |
| `COE-002` | Visible authored field enemies enter bounded battles, and striking first grants an opening initiative advantage | Observation | Corroborated | High | P3, P5, P6 |
| `COE-003` | A visible stat-ordered queue alternates individual party and enemy turns while character AP funds Skills and Free Aim shots | Confirmed | Corroborated | High | P2, P3, P5, P6 |
| `COE-004` | Chosen attacks contain timed execution prompts, while enemy sequences demand live dodge, parry or available jump responses | Confirmed | Corroborated | High | P2, P3, P5, P6 |
| `COE-005` | Free Aim spends AP without ending the turn and can damage exposed weak points or environmental enemy components | Confirmed | Corroborated | High | P2, P3, P5, P6 |
| `COE-006` | Gustave, Lune and Maelle transform later skill effects through distinct in-battle resource or stance state | Observation | Corroborated | High | P3, P5, P7 |
| `COE-007` | Health, statuses and Break resolve after attacks; full party defeat ends the attempt and patch-era Battle Retry returns to the encounter boundary | Confirmed | Corroborated | High | P1, P5, P6 |
| `COE-008` | Battle rewards feed persistent experience, levels, attributes, skill choices, equipment and the next encounter | Observation | Corroborated | High | P2, P3, P5, P7 |
| `COE-009` | A Picto grants equipped stats and a passive; four victorious battles master that passive into reusable Lumina constrained by character points | Confirmed | Corroborated | High | P3, P6, P7 |
| `COE-010` | Resting at an Expedition Flag restores the party and replenishable Tints while respawning defeated ordinary enemies | Confirmed | Corroborated | High | P6 |

## Basic data

- Release / origin: Sandfall Interactive, published by Kepler Interactive;
  released 2025-04-24 and reviewed at PC patch v1.5.6 on 2026-08-21.
- Platform or physical form: authored single-player third-person reactive
  turn-based RPG on PC and current consoles; PC Standard Edition is scoped.
- Puzzle family: tactical forecast and counterplay; real-time system pressure;
  ordered dependency sequencing.
- Primary sources:
  - **[P1]** [official Steam patch v1.5.6](https://store.steampowered.com/news/app/1903340/view/708901647665857389),
    for the current version boundary and fixes to Burn after Break recovery,
    weapon Lumina effects, consecutive turns and attack sound cues.
  - **[P2]** [official game overview](https://www.expedition33.com/overview),
    for the reactive turn-based boundary, six-character campaign, gear, stats,
    skills, synergies, dodge, parry, counter, rhythm and Free Aim weak points.
  - **[P3]** [official gameplay breakdown](https://www.expedition33.com/post/your-first-look-at-gameplay-from-clair-obscur-expedition-33),
    for exploration, party leader, Paint Cages, Pictos, permanent Lumina,
    visible turn order, AP gain and timed attack or defensive resolution.
  - **[P4]** [official Steam product page](https://store.steampowered.com/app/1903340/Clair_Obscur_Expedition_33/),
    for release, single-player platform scope and the authored campaign loop.
- Secondary sources:
  - **[P5]** [Xbox Wire combat demonstration](https://news.xbox.com/en-us/2024/08/28/clair-obscur-expedition-33-combat-breakdown-preview/),
    for field contact, First Strike, command menu, turn order, Free Aim,
    character mechanics, dodge, parry, counter and post-battle rewards.
  - **[P6]** [Xbox Wire early-game guide](https://news.xbox.com/en-us/2025/04/23/tips-to-get-started-clair-obscur-expedition-33/),
    for difficulty timing parameters, checkpoint Retry, rest refill and enemy
    respawn, AP-priced Free Aim, weak points and four-battle Picto mastery.
  - **[P7]** [Xbox Developer Direct systems interview](https://news.xbox.com/en-us/2025/01/23/clair-obscur-expedition-33-developer-direct-2025/),
    for per-character mechanics, skill trees and Pictos evolving into Luminas.
- Claim IDs: `COE-001`–`COE-010`.

## Mechanical decomposition

### Action Genes

- Existing genes: `ACT-008`, navigate the exploration leader; `ACT-019`, choose
  a Skill and target; `ACT-040`, equip a weapon or statistical item; `ACT-131`,
  consume a combat Tint; `ACT-161`, use Free Aim against a reachable hostile or
  component; `ACT-191`, spend a character build point.
- New genes: `ACT-222`, execute an offensive timing prompt; `ACT-223`, time a
  dodge, parry or jump; `ACT-224`, deliberately rest at a checkpoint;
  `ACT-225`, configure Pictos and learned Luminas.
- Claim IDs: `COE-002`–`COE-010`.

### System Behaviour Genes

- Existing gene: `SYS-299`, convert persistent character XP into levels and
  build points.
- New genes: `SYS-355`–`SYS-364`, covering field encounter entry, visible turn
  scheduling, AP economy, offensive timing, reactive defence, character
  resources, health/Break/status/Retry, battle rewards, Picto mastery and
  checkpoint recovery with enemy respawn.
- Resolution order: enter a bounded encounter and establish initiative; advance
  one combatant's turn; accept AP-funded command and timed execution; resolve
  statuses, Break and defeat; repeat the visible queue; on victory award
  persistent rewards and mastery credit, or on party defeat return to Retry;
  later rest restores finite supplies and repopulates ordinary encounters.
- Claim IDs: `COE-002`–`COE-010`.

### Constraint Genes

- Existing genes: `CON-269`, Skill legality requires target, AP and readiness;
  `CON-270`, character build points obey level and branch gates; `CON-282`, the
  authored route orders mandatory encounters.
- New genes: `CON-323`, active formation is roster- and size-bounded;
  `CON-324`, reactive defence requires the matching live timing window;
  `CON-325`, Picto slots and Lumina points bound passive configuration.
- Scarce strategic resources: active party slots, health and recovery Tints;
  per-character AP, turn opportunities and timing attention; Break openings;
  attribute and skill points; Picto slots and Lumina capacity.
- Claim IDs: `COE-003`–`COE-010`.

### Information Genes

- Existing genes: `INF-119`, character resources, attributes and learned build;
  `INF-125`, authored route and explored-map state.
- New genes: `INF-141`, turn order, AP, party and target combat state;
  `INF-142`, motion, sound and prompts cue reactive timing; `INF-143`, Picto
  mastery and Lumina cost/capacity are visible before configuration.
- Claim IDs: `COE-002`–`COE-010`.

### Objective Genes

- Existing gene: `OBJ-029`, incapacitate the finite hostile encounter set.
- Evaluation: each bounded field or boss encounter succeeds when every required
  hostile is defeated; party defeat fails that attempt but preserves the
  checkpoint from which Retry begins.
- Claim IDs: `COE-002`, `COE-007`, `COE-008`.

### Time Genes

- Existing genes: `TIM-001`, discrete turns with automatic resolution;
  `TIM-003`, real-time input during forced attack progression.
- Parameters: initiative order, command pause, animation and cue duration,
  offensive prompt windows, per-hit defence windows and accessibility settings.
- Claim IDs: `COE-003`, `COE-004`.

## Reproducible transitions

| Before | Action | Deterministic or bounded resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Roaming Nevron is reachable but battle has not begun | Contact it normally or strike first from exploration | The authored groups enter battle; a legal First Strike changes the opening queue | World approach conditions turn initiative | `COE-002` |
| Current character has sufficient AP and a legal target | Choose Skill or fire one Free Aim shot | AP is spent; Free Aim does not itself end the turn, while the Skill proceeds to execution | AP connects several command forms inside one turn | `COE-003`, `COE-005` |
| Selected Skill animation reaches its prompt | Press inside or outside the timing window | The declared effect gains or loses its timing modifier before damage or support resolution | Execution skill changes a planned turn command | `COE-004` |
| Enemy begins a readable multi-hit sequence | Dodge one hit, then parry every hit in an equivalent sequence | Valid input negates that hit; the complete parry condition triggers its counter | Safer windows and higher-reward counters are distinct choices | `COE-004` |
| Exposed weak point or attached component is targetable | Spend AP on a precise Free Aim shot | Local hit state receives its declared damage or component effect | Spatial aim modifies an otherwise turn-based encounter | `COE-005` |
| Maelle is Stanceless or Lune has a current Stain set | Resolve a Skill that changes or consumes that state | The resource or stance persists to modify a later eligible Skill | Character identity creates multi-turn planning state | `COE-006` |
| Enemy Break gauge is below threshold | Apply enough Break damage | Threshold crossing stuns the enemy and creates a bounded offensive opening | Damage and Break are related but non-identical tracks | `COE-007` |
| Every active expeditioner reaches defeat | Accept Battle Retry | The attempt ends and restarts at its encounter or checkpoint boundary | Failure resets the battle, not the persistent build | `COE-007` |
| One Picto is equipped but not mastered | Win its fourth credited battle | Its passive becomes learned Lumina while the Picto item remains equippable | Temporary slot occupation teaches a reusable passive | `COE-009` |
| Learned Lumina exists and enough points remain | Activate it, then rest at the next flag | Build capacity updates; rest restores party/Tints and respawns ordinary enemies | Persistent build choice and renewable encounter loop intersect | `COE-009`, `COE-010` |

## Strategic and experiential structure

- Local decision: choose command, target and AP spend; decide whether Free Aim
  is worth AP before the main action; execute an attack prompt; read the next
  enemy rhythm and choose the safer dodge or tighter parry; exploit Break.
- Medium-term planning: sequence each character's resource or stance across
  visible turns; preserve recovery items; distribute party roles, weapons,
  Pictos and Lumina capacity; decide whether to rest and deliberately repopulate
  the route.
- Long-term structure: repeated victories convert XP into chosen attributes and
  skills and convert temporary Picto occupancy into a widening reusable Lumina
  library, so execution practice and build construction reinforce each other.
- Common heuristics: open with First Strike when safe, reserve AP for a decisive
  Skill rather than spending every shot, dodge unfamiliar rhythms, parry learned
  sequences, focus Break before burst damage and rotate unmastered Pictos.
- Failure attribution: the visible queue, AP, target state, timing cues and Retry
  boundary explain most immediate failures; unfamiliar animations, hidden drop
  contents and build interactions preserve learnable uncertainty.
- Claim IDs: `COE-002`–`COE-010`.

## Replay and variation

- What changes: field approach, initiative, command and target sequence, timing
  execution, damage/status outcomes, loot, levelling choices, equipped Pictos,
  learned Luminas and the decision to rest before another attempt.
- Randomness or procedural generation: the scoped levels and encounters are
  authored; reward quantities and combat variance may differ, but route
  geometry and enemy identities are not a generated run map.
- Multiple viable strategies: safer dodge-heavy play, parry-counter mastery,
  Free Aim weak-point pressure, Break-focused control and different
  character-resource or passive synergies.
- Typical replay motive: improve execution against known rhythms, master a new
  Picto and test a different AP, stance, weapon and Lumina build.
- Claim IDs: `COE-002`–`COE-010`.

## Adjacent systems and history

- Dota 2 is the mathematical near match because both expose character
  resources and builds, spend ability points through level gates and require
  real-time execution around ability use. Clair Obscur replaces continuous
  team combat, economy and respawns with a visible single-combatant turn queue,
  prompted attack execution and per-hit reactive defence.
- Shogun Showdown shares discrete finite combat clearance and avatar movement,
  but forecasts committed spatial attacks rather than embedding live timing
  windows inside a party turn queue.
- Palworld shares direct exploration, aimed attacks, authored progression gates
  and persistent character state, but its companion combat remains continuous
  and autonomous rather than command-turn plus timing-response hybrid.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-019`, `ACT-040`, `ACT-131`, `ACT-161`, `ACT-191`, `ACT-222`–`ACT-225` | bindings and individual Skills are parameters |
| System Behaviour | `SYS-299`, `SYS-355`–`SYS-364` | numeric balance and reward tables are parameters |
| Constraint | `CON-269`, `CON-270`, `CON-282`, `CON-323`–`CON-325` | party size, AP costs and windows are parameters |
| Information | `INF-119`, `INF-125`, `INF-141`–`INF-143` | HUD position and cue styling are presentation |
| Objective | `OBJ-029` | enemy identities and health are parameters |
| Time | `TIM-001`, `TIM-003` | exact timing windows depend on difficulty |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `143` (`GAME-0001`–`GAME-0143`).
- Exact genome matches: none.
- Tied near matches: `GAME-0138` — Dota 2 (`6 / 64 = 0.093750`).
- Supported combination subsets: `COMB-0142`.
- Scan date: 2026-08-21.

### Selected-neighbour interpretation

No pre-migration reviewed selected-neighbour table row exists for: `GAME-0138`.

### Preserved research notes

- New genes: `ACT-222`–`ACT-225`, `SYS-355`–`SYS-364`, `CON-323`–`CON-325`,
  `INF-141`–`INF-143`.
- Classification result: new verified combination of reused and new genes.
- Evidence and reasoning: the distinctive boundary is not turn-based command
  selection or parrying alone. It is the repeated conversion of a visible
  AP-funded turn plan into live prompted execution and enemy-response timing,
  with successful encounters permanently expanding both character builds and
  the reusable Lumina passive library.

## Taxonomy impact

- Registry changes: 20 new bounded genes and `COMB-0142`; `ACT-191`, `SYS-299`,
  `CON-270` and `INF-119` gain a second persistent-campaign example without
  changing type, lifecycle or causal boundary.
- Taxonomy-change record: none.
- Candidate terms affected: none.

## Negative results

- No separate negative-result record. The exhaustive scan found no exact
  genome and no earlier registered combination that is a proper subset.

## Delta summary

## Нові факти

- [Confirmed | Corroborated | High] A visible turn plan becomes live execution
  through offensive prompts and per-hit dodge or parry windows (`COE-003`,
  `COE-004`).
- [Confirmed | Corroborated | High] Four victories with an equipped Picto turn
  its passive into capacity-priced reusable Lumina (`COE-009`).

## Нові гени

- [Observation | Corroborated | High] 20 bounded genes cover reactive turn
  execution, AP, character resources, Break, Retry, Picto mastery and rest.

## Нові комбінації

- [Confirmed | Corroborated | High] `COMB-0142` — reactive turn execution into
  mastered passive builds.

## Зміни таксономії

- [Observation | Corroborated | High] Four existing character-build records
  gain independent campaign evidence without a boundary or type change.

## Нові питання

- Do later Gradient Attacks require a separate defence-action boundary once a
  future scope compares them against ordinary dodge, parry and jump sequences?

## Наступна рекомендована гра

- [Hypothesis | Limited | High] `GAME-0145` — Grand Theft Auto V.
- Optimisation criterion: continue the recorded second demand-led tranche while
  moving from bounded party battles to mission-gated open-world action.
- Expected information gain: character switching, wanted-state escalation,
  vehicle traversal, mission checkpoints and heist preparation.
- Backlog impact: begins the second nine-game demand-led tranche.

## Чому саме вона

- [Hypothesis | Limited | High] Its open-world multi-character mission structure
  should be distant from the turn queue while testing reuse of direct movement,
  combat, authored gates and persistent build state.
