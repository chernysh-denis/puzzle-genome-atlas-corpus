---
game_id: GAME-0148
slug: baldurs-gate-3
game_title: Baldur’s Gate 3
analysis_status: reviewed
reviewed: 2026-08-21
combination_ids:
  - COMB-0146
gene_ids:
  action:
    - ACT-008
    - ACT-019
    - ACT-040
    - ACT-107
    - ACT-130
    - ACT-131
    - ACT-161
    - ACT-190
    - ACT-191
    - ACT-199
    - ACT-232
    - ACT-238
  system:
    - SYS-299
    - SYS-379
    - SYS-387
    - SYS-388
    - SYS-389
    - SYS-390
    - SYS-391
    - SYS-392
  constraint:
    - CON-269
    - CON-270
    - CON-282
    - CON-284
    - CON-323
    - CON-336
    - CON-342
    - CON-343
    - CON-344
    - CON-345
  information:
    - INF-073
    - INF-119
    - INF-125
    - INF-128
    - INF-141
    - INF-148
    - INF-152
    - INF-153
    - INF-154
  objective:
    - OBJ-077
  time:
    - TIM-001
    - TIM-003
    - TIM-007
---

# Game: Baldur's Gate 3

## Analysis scope

- Version / ruleset: PC Patch 8 at official Hotfix #35, version
  `4.1.1.6995620`; one fresh single-player Balanced custom-character campaign
  from character creation through the first completed destroy-the-Netherbrain
  ending and epilogue.
- Included: race, class, background, abilities and skill proficiencies;
  exploration and direct four-person party control; dialogue and d20 ability
  checks; Inspiration; companions and approval; initiative, movement, Action,
  Bonus Action and Reaction; attacks, spells, slots and concentration;
  conditions, surfaces and sight; downing, death saves and revival; loot,
  inventory, equipment, trade, XP and levels through the level-12 cap; short
  and long rest; quest-state branches, save/load and the three-act main route.
- Reproducible checkpoint: create one custom Tav, recruit a four-member party,
  enter a dialogue check with an available party bonus, observe one failed
  check and Inspiration reroll, then enter combat. Record initiative; spend one
  character's movement, Action and Bonus Action; accept or decline a prompted
  Reaction; cast one concentration spell and break it by casting another;
  revive one Downed ally; take a Short Rest, then a 40-supply Long Rest. Follow
  the retained critical path through the first Netherbrain-destruction ending.
- Excluded: Origin and Dark Urge runs, romance completion, alternate endings,
  exhaustive companions, quests, areas, items or spells; Explorer, Tactician,
  Honour and Custom difficulty; multiplayer, cross-play, split-screen, mods,
  toolkit, photo mode, cosmetics, achievements and post-ending replay.
- Direct-play status: no new authenticated full campaign was played. Current
  first-party version and product material establish the boundary; maintained
  mechanics references corroborate the reproducible transitions.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `BG3-001` | Patch 8 is the final major patch and Hotfix #35 fixes the reviewed PC baseline at `4.1.1.6995620` | Confirmed | Direct | High | P1, P2 |
| `BG3-002` | A custom character binds race, class, background, abilities and proficiencies before the persistent campaign | Observation | Corroborated | High | P3, S1 |
| `BG3-003` | Dialogue and exploration checks compare d20, ability and proficiency modifiers against a DC; advantage changes the die sample and Inspiration can reroll an eligible failure | Observation | Corroborated | High | S2, S3, S4 |
| `BG3-004` | Combat orders participants by initiative and refreshes movement, Action, Bonus Action and Reaction resources by turn | Observation | Corroborated | High | S5, S6 |
| `BG3-005` | Attacks and spells require legal range, sight and resources; concentration permits one maintained spell and surfaces or elevation change resolution | Observation | Corroborated | High | S7, S8, S9 |
| `BG3-006` | Reaching zero HP Downs eligible party members into death saves; Help or healing restores them and dead companions require resurrection | Observation | Corroborated | High | S10 |
| `BG3-007` | Short Rest restores a bounded subset; a Balanced full Long Rest consumes 40 supplies, restores broad resources and advances camp or time-sensitive state | Observation | Corroborated | High | S11 |
| `BG3-008` | XP advances characters through class, subclass and optional multiclass choices to the total level-12 cap | Observation | Corroborated | High | S12, S13 |
| `BG3-009` | Dialogue and quest choices change companion approval and retained quest availability across the campaign | Observation | Corroborated | High | S14, P3 |
| `BG3-010` | Destroying the defeated Netherbrain completes the main adventure and leads to the ending and epilogue | Observation | Corroborated | High | S15, S16 |

## Basic data

- Release / origin: Larian Studios; full release 2023, reviewed at Patch 8 and
  Hotfix #35 on 2026-08-21.
- Platform or physical form: cinematic single-player party CRPG on PC and
  consoles; this unit scopes the PC single-player client.
- Puzzle family: tactical forecast and counterplay; resource transformation;
  ordered dependency sequencing; stateful conversation and quest logic.
- Primary sources:
  - **[P1]** [official Patch 8 announcement](https://baldursgate3.game/news/the-final-patch-new-subclasses-photo-mode-and-cross-play_138),
    for the final-major-patch boundary and its added subclasses.
  - **[P2]** [official Hotfix #35 notes](https://baldursgate3.game/news/hotfix-35-now-live_145),
    for PC version `4.1.1.6995620`.
  - **[P3]** [Larian general information](https://larian.com/support/faqs/general-information_46),
    for the player-driven D&D 5e-based RPG, creation and choice boundary.
  - **[P4]** [official Steam product page](https://store.steampowered.com/app/1086940/Baldurs_Gate_3/),
    for single-player party exploration, turn-based combat and authored choice.
- Secondary sources:
  - **[S1]** [character creation](https://bg3.wiki/wiki/Character_creation).
  - **[S2]** [ability checks](https://bg3.wiki/wiki/Ability_check).
  - **[S3]** [advantage](https://bg3.wiki/wiki/Advantage).
  - **[S4]** [Inspiration](https://bg3.wiki/wiki/Inspiration).
  - **[S5]** [gameplay mechanics](https://bg3.wiki/wiki/Gameplay_mechanics).
  - **[S6]** [actions and turn resources](https://bg3.wiki/wiki/Actions).
  - **[S7]** [spells](https://bg3.wiki/wiki/Spells).
  - **[S8]** [concentration](https://bg3.wiki/wiki/Concentration).
  - **[S9]** [environment and surfaces](https://bg3.wiki/wiki/Environment).
  - **[S10]** [death saving throws](https://bg3.wiki/wiki/Death_saving_throw).
  - **[S11]** [resting](https://bg3.wiki/wiki/Resting).
  - **[S12]** [experience](https://bg3.wiki/wiki/Experience).
  - **[S13]** [classes and level cap](https://bg3.wiki/wiki/Level).
  - **[S14]** [companion approval](https://bg3.wiki/wiki/Approval).
  - **[S15]** [the Netherbrain](https://bg3.wiki/wiki/Netherbrain).
  - **[S16]** [Destroy the Elder Brain](https://bg3.wiki/wiki/Destroy_the_Elder_Brain).
- Claim IDs: `BG3-001`–`BG3-010`.

## Mechanical decomposition

### Action Genes

- Existing genes: `ACT-008`, navigate the selected party member; `ACT-019`,
  choose a unit ability and target; `ACT-040`, equip loot; `ACT-107`, acquire
  an operational fact in dialogue; `ACT-130`, buy an offered item or service;
  `ACT-131`, consume a carried item; `ACT-161`, commit a weapon strike;
  `ACT-190`, cast an ability; `ACT-191`, spend a build point; `ACT-199`, transfer
  world loot; `ACT-232`, commit an authored response.
- New gene: `ACT-238`, configure a persistent custom campaign character.
- Parameters: character, party member, response, check, action, target,
  movement, equipment, spell, resource, companion and retained choice.
- Claim IDs: `BG3-002`–`BG3-009`.

### System Behaviour Genes

- Existing genes: `SYS-299`, convert XP into levels and build choices;
  `SYS-379`, advance retained authored quest state.
- New genes: `SYS-387`, resolve d20 checks; `SYS-388`, schedule initiative and
  turn resources; `SYS-389`, resolve attacks, spells, concentration and
  environmental interaction; `SYS-390`, resolve Downed, death saves and
  revival; `SYS-391`, restore resources and advance camp state through rest;
  `SYS-392`, update companion approval and participation.
- Resolution order: current world and dialogue state determines available
  checks and encounters; initiative schedules each combatant; legal movement
  and actions resolve dice, resources, damage, conditions and concentration;
  victory or conversation commits rewards and quest flags; rest restores its
  declared subset and may advance camp or quest state.
- Claim IDs: `BG3-003`–`BG3-010`.

### Constraint Genes

- Existing genes: `CON-269`, ability legality requires target, range, resource
  and readiness; `CON-270`, character choices obey levels and prerequisites;
  `CON-282`, required story encounters obey authored order; `CON-284`, capacity
  and equipment slots bound inventory; `CON-323`, the active party is roster-
  and size-bounded; `CON-336`, retained quest state gates later branches.
- New genes: `CON-342`, custom creation choices obey origin, class and point-buy
  compatibility; `CON-343`, a combat turn is bounded by movement and action
  resources; `CON-344`, spell use is bounded by preparation, slots and one
  concentration effect; `CON-345`, rest requires safe state, remaining uses or
  sufficient camp supplies.
- Scarce strategic resources: party slots, hit points, movement, action types,
  spell slots, class charges, concentration, consumables, carrying capacity,
  Inspiration, gold, camp supplies and retained companion trust.
- Claim IDs: `BG3-002`–`BG3-009`.

### Information Genes

- Existing genes: `INF-073`, hotbar and equipment; `INF-119`, character health,
  resources and build; `INF-125`, map, waypoints and quest gates; `INF-128`,
  loot and inventory compatibility; `INF-141`, initiative, resources, party
  and targets; `INF-148`, available contextual dialogue responses.
- New genes: `INF-152`, the dice interface exposes DC, modifiers, advantage and
  reroll resources; `INF-153`, party frames and sheets expose members, health,
  conditions and approval; `INF-154`, the rest interface exposes recovery and
  camp-supply commitment.
- Claim IDs: `BG3-003`–`BG3-009`.

### Objective Genes

- Existing gene: `OBJ-077`, complete the required main story through the chosen
  terminal branch; the scoped first ending destroys the Netherbrain.
- Success and failure: destroying the Netherbrain and reaching the resulting
  epilogue completes the unit; a party wipe ends the current attempt but save
  history permits restoration.
- Claim IDs: `BG3-006`, `BG3-010`.

### Time Genes

- Existing genes: `TIM-001`, combat resolves discrete selected actions before
  the next decision; `TIM-003`, exploration and environmental bodies progress
  in real time while input remains available; `TIM-007`, manual and automatic
  saves create branchable player-reversible campaign history.
- Parameters: initiative round, turn start, reaction interrupt, real-time
  exploration, save slot, autosave boundary, short rest and long-rest night.
- Claim IDs: `BG3-004`–`BG3-007`.

## Reproducible transitions

| Before | Action | Deterministic or bounded resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| New custom campaign is selected | Commit race, class, background, abilities and skills | A persistent Tav enters the shared opening with the corresponding proficiencies and actions | initial build binds later possibility | `BG3-002` |
| Dialogue presents a DC and legal bonuses | Select the checked response and roll | d20, modifiers and advantage/disadvantage determine success; an eligible failure may spend Inspiration to reroll | visible chance changes authored state | `BG3-003` |
| Hostility begins with several actors | Enter combat | Initiative orders participants and supplies the active actor's movement and action resources | continuous world becomes a turn schedule | `BG3-004` |
| Active member has movement, Action and Bonus Action | Move, attack, Jump or Shove, then end turn | Each choice spends its matching resource; a legal trigger may request a Reaction outside the actor's turn | action economy bounds tactical sequence | `BG3-004` |
| Caster has a slot and maintains one concentration spell | Cast another concentration spell | The previous concentration effect ends before the new legal effect persists | powerful duration is mutually exclusive | `BG3-005` |
| Water, grease or terrain lies inside legal attack geometry | Apply a compatible elemental effect | The surface changes, applies conditions or alters movement and sight according to its type | environment joins combat state | `BG3-005` |
| Party member reaches zero HP | Allow one death-save turn, then Help or heal | The member accumulates success/failure while Downed; Help or healing restores consciousness, while death requires resurrection | defeat has staged recovery | `BG3-006` |
| Party has spent health and resources | Take a Short Rest, then commit 40 supplies to Long Rest | Short Rest restores its subset; full rest restores broad resources and advances the camp night | recovery consumes bounded opportunities and supply | `BG3-007` |
| A quest or dialogue decision affects a companion | Commit the response | Approval and retained flags update later dialogue, party state or quest availability | narrative choice is mechanical memory | `BG3-009` |
| Final battle has defeated the Netherbrain | Command its destruction | Tadpoles and brain are destroyed, the main adventure completes and the ending leads to the epilogue | terminal branch completes campaign | `BG3-010` |

## Strategic and experiential structure

- Local decision: choose the speaking or acting party member, weigh a visible
  check, route around line of sight and surfaces, then sequence movement,
  Action, Bonus Action, Reaction and limited spell resources.
- Medium-term planning: form a complementary four-person party; prepare spells
  and equipment; preserve concentration, Inspiration and supplies; decide when
  a rest is worth possible camp or quest advancement.
- Long-term structure: XP and equipment widen character builds while retained
  choices alter companions, allies, quest access and the final route through
  Acts One, Two and Three.
- Common heuristics: let the best-skilled party member initiate a check, seek
  advantage before spending Inspiration, concentrate fire, use elevation and
  surfaces, protect concentrating casters and rest before an authored gate.
- Failure attribution: previews expose chance, resource and target legality;
  dice and concealed narrative consequences preserve uncertainty while save
  history bounds the cost of experimentation.
- Claim IDs: `BG3-003`–`BG3-010`.

## Replay and variation

- What changes: custom build, recruited party, conversation and quest choices,
  ability-check rolls, encounter approach, initiative, loot, spell preparation,
  companion approval and terminal availability.
- Randomness or procedural generation: the campaign map and quests are
  authored; d20 rolls, damage dice and selected rewards vary local resolution.
- Multiple viable strategies: martial or magical builds, persuasion or combat,
  stealth or direct approach, surface control, vertical positioning and many
  party compositions can reach the scoped ending.
- Typical replay motive: test another class and party, expose mutually
  exclusive quest state and pursue an alternate ending outside this unit.
- Claim IDs: `BG3-002`–`BG3-010`.

## Adjacent systems and history

- Dota 2 shares character resources, targeted abilities and level-gated builds,
  but Baldur's Gate 3 replaces simultaneous network combat with authored
  initiative turns, persistent party composition and dialogue-state checks.
- Clair Obscur: Expedition 33 shares a visible party turn order and persistent
  builds, but uses real-time timing prompts rather than BG3's d20 checks,
  reactions, spell concentration and environmental surfaces.
- Cyberpunk 2077 shares authored dialogue, inventory and retained quest
  branches, but BG3 makes four-character party control and tabletop-derived
  dice/action economy the primary resolution layer.
- Important difference: one retained campaign couples visible probabilistic
  conversation with party tactics, recovery logistics and a branching ending.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-019`, `ACT-040`, `ACT-107`, `ACT-130`, `ACT-131`, `ACT-161`, `ACT-190`, `ACT-191`, `ACT-199`, `ACT-232`, `ACT-238` | race, class, spell and response are parameters |
| System Behaviour | `SYS-299`, `SYS-379`, `SYS-387`–`SYS-392` | exact classes, spells, DCs and quests are parameters |
| Constraint | `CON-269`, `CON-270`, `CON-282`, `CON-284`, `CON-323`, `CON-336`, `CON-342`–`CON-345` | difficulty values and route gates are parameters |
| Information | `INF-073`, `INF-119`, `INF-125`, `INF-128`, `INF-141`, `INF-148`, `INF-152`–`INF-154` | interface layout is excluded |
| Objective | `OBJ-077` | destroy branch is scoped |
| Time | `TIM-001`, `TIM-003`, `TIM-007` | exploration, turns and save history coexist |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `147` (`GAME-0001`–`GAME-0147`).
- Exact genome matches: none.
- Tied near matches: `GAME-0146` — Cyberpunk 2077 (`21 / 74 = 0.283784`).
- Supported combination subsets: `COMB-0146`.
- Scan date: 2026-08-21.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0146` — Cyberpunk 2077 | `ACT-008`, `ACT-107`, `ACT-161`, `ACT-191`, `ACT-199`, `ACT-232`, `SYS-299`, `SYS-379`, `CON-269`, `CON-270`, `CON-282`, `CON-284`, `CON-336`, `INF-073`, `INF-119`, `INF-125`, `INF-128`, `INF-148`, `OBJ-077`, `TIM-003`, `TIM-007` | Both packets retain an authored branching campaign, persistent build and inventory choices, dialogue state and save restoration. Baldur's Gate 3 resolves those choices through a four-character initiative order, d20 checks, action economy and camp recovery, while Cyberpunk uses one real-time avatar with scanner, quickhacks and capacity-bound cyberware. | Near, `0.283784` |

## Taxonomy impact

- Registry changes: add fourteen bounded records and reuse twenty-nine active
  genes; register `COMB-0146` and extend six established family memberships.
- Taxonomy-change record: none; the d20, party-turn, rest and companion
  boundaries are additive and do not redefine the controlled vocabulary.
- Candidate terms affected: none.

## Negative results

- No prior combination is a proper subset of the complete admitted genome.
- `ACT-228` is absent because its canonical boundary excludes selecting a
  turn-based party member; BG3 party control remains a parameter of `ACT-008`
  and `ACT-019` in this unit rather than a protagonist-world switch.
- `SYS-215` is absent because hostile combat is initiative-turn resolution,
  not direct simultaneous real-time combat.
- `ACT-224` is absent because an expedition checkpoint's enemy-respawn
  consequence differs from BG3's short/long camp-rest economy.
- Romance, alchemy and exhaustive stealth systems were not promoted because
  they are outside the one-critical-path definition of done.

## Delta summary

## Нові факти

- [Observation | Corroborated | High] Visible d20 checks connect ability,
  proficiency, advantage, party bonuses and shared Inspiration to authored
  dialogue outcomes (`BG3-003`).
- [Observation | Corroborated | High] Initiative and four action-resource types
  connect party composition to spells, concentration and surfaces (`BG3-004`,
  `BG3-005`).
- [Observation | Corroborated | High] Supply-backed rest restores resources and
  may advance camp or quest state, while companion approval preserves another
  consequence track (`BG3-007`, `BG3-009`).

## Нові гени

- [Observation | Corroborated | High] Fourteen bounded genes cover custom
  creation, d20 checks, turn scheduling, combat/environment resolution,
  Downed/revival, rest, approval, creation/action/spell/rest constraints and
  dice/party/rest information.

## Нові комбінації

- [Confirmed | Corroborated | High] `COMB-0146` couples checked dialogue,
  four-person turn tactics, staged defeat, camp recovery and retained campaign
  choice into one first-ending route.

## Зміни таксономії

- [Observation | Corroborated | High] Змін таксономії немає.

## Нові питання

- Which later party RPG first recurs with the same visible Inspiration reroll,
  concentration replacement and rest-sensitive narrative state?

## Наступна рекомендована гра

- [Hypothesis | Limited | High] `GAME-0149` — Battlefield 6.
- Optimisation criterion: continue the recorded demand-led queue and contrast a
  persistent turn-based party campaign with large-scale live class combat.
- Expected information gain: squad roles, ticket attrition, capture control,
  vehicles, destruction and networked respawn structure.

## Combination Analysis

- Registered combination: `COMB-0146`, coupling visible d20 dialogue,
  four-character turn economy, concentration, staged defeat, supply-backed rest
  and retained quest memory into one first-ending campaign.
- Combination boundary: omits optional shopping and world-fact dialogue actions
  while retaining the complete checked-choice, combat, recovery and branch loop.

## Open questions

- Exact hidden DC and approval thresholds remain authored parameters unless
  exposed by the interface or current maintained data.
- A later direct-play audit could sample controller presentation separately;
  it should not change the canonical mechanical decomposition.

## Review Notes

- Patch 8 and Hotfix #35 were checked as separate major-version and current-PC
  boundaries; later maintained pages were used only for mechanics that remain
  inside that official version.
- Origin-specific and alternate-ending mechanics were deliberately excluded to
  keep one reproducible custom-character route.
