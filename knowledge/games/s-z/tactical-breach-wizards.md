---
game_id: GAME-0048
slug: tactical-breach-wizards
game_title: Tactical Breach Wizards
analysis_status: reviewed
reviewed: 2026-08-12
combination_ids:
  - COMB-0048
gene_ids:
  action:
    - ACT-014
    - ACT-019
    - ACT-062
  system:
    - SYS-020
    - SYS-047
    - SYS-088
  constraint:
    - CON-001
    - CON-011
    - CON-095
  information:
    - INF-001
    - INF-025
  objective:
    - OBJ-029
    - OBJ-031
  time:
    - TIM-010
---

# Game: Tactical Breach Wizards

## Analysis scope

- Version / ruleset: released 2024 base game on ordinary difficulty, scoped to
  the first non-Ship mission, *Rushwater Reunion*, from the initial breach of
  zone 1 through accepted completion of zone 6.
- Included: Zan and Jen; room deployment / redeployment; movement and current
  abilities; action and mana costs; targeted attacks; knockback, collision and
  defenestration; current hostile targeting; Foresee simulation; rewinding
  tentative actions; commit; hostile movement; reinforcement doors; laptops;
  mandatory room objectives, failure and room transition.
- Excluded: the preceding Ship tutorial, later missions, characters and perks;
  anxiety dreams; optional confidence optimisation beyond goals displayed in
  the scoped mission; narrative interpretation, conversation choices, DLC,
  developer commentary, Workshop levels, achievements and speedrunning.
- Direct-play status: not conducted. The released product and rewind premise
  are primary-source facts; phase, allowance, targeting and zone transitions
  are corroborated by two hands-on reviews and two independently reproducible
  Act I guides. Community references are used only for exact enemy and ability
  boundaries not stated by the product page.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `TBW-001` | Each scoped room is a fixed finite grid with visible occupants, cover, windows, doors, laptops and objective state | Confirmed | Corroborated | High | P1, D1, S1, G1, G2 |
| `TBW-002` | The player flexibly orders Zan and Jen commands; each ordinarily receives one movement use and one action, with abilities and upgrades providing declared exceptions | Confirmed | Corroborated | High | S1, S2, C1, G1 |
| `TBW-003` | Targeted abilities deterministically apply damage, knockback, collision and window removal from current geometry | Confirmed | Corroborated | High | P1, S2, C1, G1, G2 |
| `TBW-004` | Hostile targets and consequences update from the current tentative player state rather than remaining fixed commitments established before planning | Confirmed | Corroborated | High | S1, S2, C2 |
| `TBW-005` | Foresee simulates the exact hostile consequences of the current draft before the player decides whether to commit it | Confirmed | Corroborated | High | S1, S2, G1, G2 |
| `TBW-006` | Rewind may restore any earlier step of the uncommitted current turn without cost, after which a different draft and forecast can be tested | Confirmed | Direct | High | P1, S1, S2, G1 |
| `TBW-007` | Committing ends revision of that turn; hostile movement then establishes a new circumstance for the next editable player turn | Confirmed | Corroborated | High | S1, S2, G1 |
| `TBW-008` | *Rushwater Reunion* uses authored zone-specific mandatory tasks including defenestration, rescue, hostile clearance, laptop use, reinforcement-door sealing and redeployment | Confirmed | Corroborated | High | D1, G1, G2 |
| `TBW-009` | Unsealed reinforcement doors introduce additional hostiles after a turn boundary and can be sealed to prevent later arrivals | Confirmed | Corroborated | Medium | G1, G2, C3 |
| `TBW-010` | The game does not instantiate `INF-009` or `SYS-019`: ordinary hostile targeting can change during the player turn and Foresee is a reversible simulation, not execution of a previously committed attack | Observation | Corroborated | High | TBW-004–TBW-007, C2 |
| `TBW-011` | The game does not instantiate `TIM-007`: rewind is bounded to discrete states of the uncommitted turn and cannot restore a completed earlier turn | Observation | Corroborated | High | P1, S1, C1 |
| `TBW-012` | The game does not instantiate `CON-034`: movement may occur after an ability and is independent of the character's action point | Observation | Corroborated | High | C1, G1 |
| `TBW-013` | The scoped loop rejects both `COMB-0014` and `COMB-0047` while establishing a distinct forecast-rewind-commit interaction | Observation | Corroborated | High | TBW-002–TBW-012 |

## Basic data

- Release / origin: Suspicious Developments developed and published Tactical
  Breach Wizards for Windows on 22 August 2024.
- Platform or physical form: single-player digital turn-based tactics game
  with handcrafted multi-room missions.
- Puzzle family: rewindable deterministic room tactics with reactive hostile
  consequence forecasting.
- Primary and creator sources:
  - **[P1]** [Official Steam product page](https://store.steampowered.com/app/1043810/Tactical_Breach_Wizards/),
    documenting the release, unique unit abilities, free rewind, handcrafted
    levels and the developer's explicit distinction from Into the Breach.
  - **[D1]** [Steve Lee, *The Unusual Level Design of Tactical Breach Wizards*](https://media.gdcvault.com/gdc2025/Slides/Lee_Steve_TheUnusualLevel.pdf),
    creator-side evidence for authored tactical spaces and encounter design.
- Contemporary mechanical sources:
  - **[S1]** [PC Gamer review](https://www.pcgamer.com/games/strategy/tactical-breach-wizards-review/),
    documenting action, Foresee and enemy phases plus rewind before end turn.
  - **[S2]** [Game8 review](https://game8.co/articles/reviews/tactical-breach-wizards-review),
    documenting real-time target updates from tentative actions, exact
    consequence preview and unlimited current-turn revision.
- Reproducible transition documentation:
  - **[G1]** [Neoseeker Act I walkthrough](https://www.neoseeker.com/tactical-breach-wizards/Act_I),
    documenting all *Rushwater Reunion* rooms, abilities, laptops, Foresee and
    reinforcement interactions.
  - **[G2]** [Bonus Action complete walkthrough](https://bonus-action.com/guides/tactical-breach-wizards-complete-walkthrough-all-missions-and-objectives/),
    independently listing the six zones and their exact required objectives.
- Narrow community references:
  - **[C1]** [Gameplay and turn controls](https://tactical-breach-wizards.fandom.com/wiki/Tactical_Breach_Wizards),
    used for one movement, one action, post-action movement and current-turn-
    only rewind.
  - **[C2]** [RPD Tracker — official wiki](https://tacticalbreachwizards.wiki.gg/wiki/RPD_Tracker),
    documenting target changes during the player turn and target lock only at
    the Foresee boundary.
  - **[C3]** [Phase-order clarification](https://steamcommunity.com/app/1043810/discussions/0/4847653027872806910/),
    used narrowly to place reinforcement-door release after Foresee and end
    turn.
- Claim IDs: `TBW-001`–`TBW-013`.

## Mechanical decomposition

### Action Genes

- `ACT-014` — relocate selected controlled board piece. The player selects Zan
  or Jen and one currently reachable grid position; one ordinary movement use
  is consumed independently of the character's action point.
- `ACT-019` — select unit ability and target. The player selects one available
  character ability and an eligible unit, position, direction or interactive
  object. Static Blast, 3 Bolt Burst, Chain Bolt, Predictive Bolt and Use
  Laptop differ by target geometry and cost but share this command boundary.
- `ACT-062` — rewind uncommitted tactical draft. The player selects an earlier
  step of the current turn, restoring draft positions, resource use and
  consequences while leaving every completed prior turn unavailable.
- `ACT-044` is absent. No continuous simulation history or already lived
  committed world interval is restored; rewind edits only the current discrete
  turn draft.
- Claim IDs: `TBW-002`, `TBW-003`, `TBW-006`, `TBW-011`, `TBW-012`.

### System Behaviour Genes

- `SYS-020` — attack-induced displacement and collision resolution. Ability
  knockback shifts an affected target and resolves contact with walls, units,
  windows or level boundaries; defenestration removes the target.
- `SYS-047` — time-scheduled population release. An unsealed reinforcement
  door introduces its scripted hostile arrivals after a later turn boundary;
  sealing the door stops the remaining stream.
- `SYS-088` — exact draft-state consequence simulation. Foresee resolves the
  current draft's target-dependent attacks, damage, displacement and failure
  consequences as a reversible simulation. Revising an earlier action causes
  the forecast to be recomputed from the restored draft state.
- `SYS-019` is absent. RPD Trackers may change their target during the player
  turn, and the displayed Foresee outcome is reversible rather than a hostile
  attack committed before planning and then irreversibly executed afterward.
- `SYS-021` and `SYS-022` are absent. Reinforcements use persistent authored
  doors, not marked one-round spawn tiles with blocking damage; no separate
  scheduled terrain hazard is necessary in the scoped mission.
- Resolution order: enter authored room and apply deployment; issue any legal
  interleaving of character movements / abilities; update hostile target state;
  enter Foresee and simulate consequences; rewind and revise or commit; advance
  hostile movement and unsealed reinforcement doors; evaluate mandatory tasks,
  failure and room transition; refresh the next player turn.
- Claim IDs: `TBW-003`–`TBW-010`.

### Constraint Genes

- `CON-001` — fixed occupancy capacity. Each authored zone is a finite grid of
  individually addressable positions fixed before the room's tactical choices.
- `CON-011` — exclusive occupancy with static barriers. Ordinary units cannot
  finish on the same position; walls, cover, doors and room boundaries govern
  legal movement and collision.
- `CON-095` — per-character independent movement-and-action allowance. Each
  controlled character ordinarily has one movement use and one action point;
  either may be spent first, and movement remains legal after an action unless
  another rule removes it. Abilities, mana and perks create declared exceptions.
- `CON-034` is absent because that record makes movement unavailable after the
  unit's ability. This mission permits movement before, between or after
  abilities and treats movement separately from the action point.
- Scarce strategic resources: each character's remaining movement and action,
  current mana, safe line-of-sight positions, remaining reinforcement doors,
  usable collision geometry and required laptop access.
- Claim IDs: `TBW-001`, `TBW-002`, `TBW-008`, `TBW-009`, `TBW-012`.

### Information Genes

- `INF-001` — fully visible current state. Current room geometry, actors,
  health, armour, stability, remaining actions, hostile targeting and mandatory
  tasks are inspectable.
- `INF-025` — exact reactive hostile-consequence preview. Foresee discloses the
  exact hostile attacks and resulting state for the current tentative player
  draft, and the disclosure changes when the draft changes.
- `INF-009` is absent. Hostile action/target state is not already fixed before
  planning: a Tracker can change target as the player moves and locks only at
  the Foresee boundary.
- `INF-018` is absent. The player previews one tactical resolution from a
  discrete turn draft rather than scrubbing a random-access multi-time world
  trajectory.
- Claim IDs: `TBW-001`, `TBW-004`, `TBW-005`, `TBW-010`.

### Objective Genes

- `OBJ-029` — incapacitate finite hostile encounter set. Several zones require
  every current and scripted required hostile to be knocked out before the
  room can complete.
- `OBJ-031` — complete authored room task set. Each zone exposes one finite
  conjunction of mandatory predicates, such as defenestrating the Pyromancer,
  saving Zan, using a laptop, redeploying, sealing doors and clearing hostiles;
  only the required set advances the mission.
- `OBJ-011` is absent. There is no shared infrastructure integrity resource or
  survival horizon. Protected-character conditions are room tasks, not one
  persistent Grid-like resource.
- Success, evaluation and failure: each room advances after all mandatory
  tasks are accepted; defeat of a required wizard or an unsatisfied terminal
  rescue condition fails the attempt; optional Confidence goals change rewards
  but are not part of the invariant completion signature.
- Claim IDs: `TBW-008`, `TBW-009`.

### Time Genes

- `TIM-010` — editable tactical draft with forecast before commit. The player
  flexibly sequences bounded character commands, invokes exact Foresee,
  restores any earlier draft step if needed and commits one accepted outcome;
  completed turns are outside the rewind horizon.
- `TIM-005` is absent. The hostile result is computed from the player's current
  draft and previewed reversibly, not a set of attacks committed before the
  planning phase.
- `TIM-004` is absent. Enemy behaviour is automatic; no opposing decision-maker
  receives an exclusive turn and chooses a reply.
- `TIM-007` is absent. Revision cannot cross the commit boundary or branch from
  a previously completed earlier turn.
- Claim IDs: `TBW-004`–`TBW-007`, `TBW-010`, `TBW-011`.

## Reproducible transitions

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Jen has movement and action; a Pyromancer stands aligned with a window | Move beside the sofa and target the Pyromancer with Static Blast | The target is displaced through the window and removed; zone 1's required predicate is credited | selected ability, geometry and objective evaluation are distinct | `TBW-002`, `TBW-003`, `TBW-008` |
| A Tracker currently targets Zan | Move Jen into a more eligible line or move Zan out of sight | The displayed target changes during the draft before Foresee | target is reactive, not precommitted `INF-009` | `TBW-004`, `TBW-010` |
| Current draft leaves a wizard exposed | Invoke Foresee | The interface simulates the exact hostile damage and resulting positions without committing the turn | exact draft-state consequence preview | `TBW-005` |
| Foresee shows unacceptable damage | Rewind to before the responsible move and choose another position | Draft state and spent allowances restore; a new Foresee produces the replacement consequence | revision is bounded and branchable only inside the turn | `TBW-006`, `TBW-011` |
| A character has spent its action but retains movement | Select Move and a legal destination | The character relocates after the ability | `CON-034` fails; independent allowance passes | `TBW-002`, `TBW-012` |
| One hostile can be pushed into another or a wall | Select a knockback ability and target | Target moves; collision damage applies to the affected bodies or obstacle | deterministic displacement and collision | `TBW-003` |
| An Enforcer's route crosses Zan's Predictive Bolt line | Commit the accepted draft | The reaction shot triggers at the declared crossing and the forecasted hostile sequence is accepted | player-authored reaction and hostile forecast interact | `TBW-005`, `TBW-007` |
| A reinforcement door remains unsealed at the phase boundary | Commit and allow the next hostile step | The door releases its authored reinforcement and remains a future source until sealed | recurring door release differs from marked emergence | `TBW-009` |
| All enemies are down but a mandatory laptop remains unused | End the current actions without using it | The zone does not complete | clearance is only one member of the task conjunction | `TBW-008` |
| Every mandatory task in zone 6 is satisfied | Resolve the final required interaction | The room and scoped mission complete regardless of unattempted optional Confidence optimisation | authored required task set defines success | `TBW-008` |

## Strategic and experiential structure

- Local decision: choose one interleaving of moves, attacks and knockback that
  satisfies immediate room tasks while Foresee reports no unacceptable loss.
- Medium-term planning: preserve mana, movement and collision angles across a
  room; seal reinforcement doors before their future releases make clearance
  harder; finish near required laptops rather than solving combat in isolation.
- Long-term structure: complete six authored zones whose mandatory task sets
  introduce and recombine deployment, rescue, reactions, reinforcement control
  and contextual interaction.
- Common heuristics: test high-leverage knockback first; inspect target updates
  after every move; use Foresee before commit; rewind the earliest causal
  mistake; distinguish mandatory laptop/door tasks from optional style goals.
- Failure attribution: deterministic Foresee localises immediate damage to the
  current draft, while a failed room plan remains attributable to resource use,
  reinforcement timing or an omitted mandatory task rather than hidden RNG.
- Player-trust factors: target indicators update with tentative state, Foresee
  shows the exact current consequence and free rewind preserves experimentation;
  the commit boundary clearly ends that protection.
- Claim IDs: `TBW-001`–`TBW-013`.

## Replay and variation

- What changes between sessions: the base mission geometry and enemy placement
  are authored; player command order, optional Confidence pursuit and later
  perk loadout create solution variation.
- Randomness or procedural generation: none is necessary to the scoped room
  transitions. The developer explicitly describes every level as handcrafted.
- Multiple viable strategies: deterministic outcomes permit alternative
  sequences and collision chains, while required tasks constrain the final
  accepted state rather than prescribing every command.
- Typical replay motive: complete optional Confidence goals, test another
  action order or later perk set, or improve turn/resource efficiency.
- Claim IDs: `TBW-002`–`TBW-009`.

## Adjacent systems and history

- Into the Breach shares selected-unit movement/abilities, fixed grid,
  displacement, visible state and a bounded squad phase. Its Vek attacks are
  committed before planning and execute afterward; Tactical Breach Wizards
  instead recomputes a reversible forecast from the player's tentative state.
- Fights in Tight Spaces shares displacement, visible state, exact preview and
  phase commit, but its primed attacks are commitments and its one agent acts
  through a random hand / momentum economy.
- Shogun Showdown is the external timing control: enemy actions are visible and
  may be repurposed through position, but every player action immediately
  advances foes instead of building an editable multi-command draft.
- Braid shares player-controlled revision but retains and restores already
  lived continuous world history across more than one discrete action. Tactical
  Breach Wizards only edits the current uncommitted tactical turn.
- Timelie shares exact deterministic future inspection and command revision,
  but its one cursor can scrub multiple world times and edit timestamped paths;
  Foresee simulates one bounded tactical resolution from a discrete draft.
- Claim IDs: `TBW-002`–`TBW-013`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-014`, `ACT-019`, `ACT-062` | unit set, target geometry and current-turn rewind depth |
| System Behaviour | `SYS-020`, `SYS-047`, `SYS-088` | collision, door release and forecast resolution order |
| Constraint | `CON-001`, `CON-011`, `CON-095` | room topology, occupancy and allowance exceptions |
| Information | `INF-001`, `INF-025` | current visibility and reactive forecast detail |
| Objective | `OBJ-029`, `OBJ-031` | required hostiles and authored zone task set |
| Time | `TIM-010` | draft, Foresee, rewind and commit boundaries |

Canonical signature:

`ACT-014,ACT-019,ACT-062; SYS-020,SYS-047,SYS-088;
CON-001,CON-011,CON-095; INF-001,INF-025; OBJ-029,OBJ-031; TIM-010`

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `47` (`GAME-0001`–`GAME-0047`).
- Exact genome matches: none.
- Tied near matches: `GAME-0014` — Into the Breach (`6 / 23 = 0.260870`).
- Supported combination subsets: `COMB-0048`.
- Scan date: 2026-08-12.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0014` — Into the Breach | `ACT-014`, `ACT-019`, `SYS-020`, `CON-001`, `CON-011`, `INF-001` | committed attacks, move-before-ability lock and Grid horizon versus reactive forecast, post-ability movement, draft rewind and authored room tasks | Near, `0.260870` |

### Preserved research notes

- New genes: `ACT-062`, `SYS-088`, `CON-095`, `INF-025`, `OBJ-031`, `TIM-010`.
- Classification result: `New combination of known and new genes`.
- Evidence and reasoning: existing exact-intent and history-rewind boundaries
  explicitly reject the scoped forecast loop. Six narrow additions preserve
  those exclusions while reusing eight genes whose operational transitions fit.

## Combination record

- Registered `COMB-0048` — exact reactive forecast and current-turn revision
  before tactical commit.
- Exhaustive `COMB-0014` test: Tactical Breach Wizards has `ACT-019` and
  `SYS-020` of seven genes; it lacks `SYS-019`, `CON-034`, `INF-009`,
  `OBJ-011` and `TIM-005`.
- Exhaustive `COMB-0047` test: it has `SYS-020` of four genes and lacks
  `SYS-019`, `INF-009` and `TIM-005`.
- No existing combination gene set is a proper subset of the complete genome.

## Taxonomy impact

- Registry changes: added `ACT-062`, `SYS-088`, `CON-095`, `INF-025`,
  `OBJ-031` and `TIM-010`; added Tactical Breach Wizards evidence to
  `ACT-014`, `ACT-019`, `SYS-020`, `SYS-047`, `CON-001`, `CON-011`, `INF-001`
  and `OBJ-029`.
- Taxonomy-change record: none. Existing exact-intent, committed-resolution,
  move-then-ability and branchable-history definitions remain unchanged.
- Candidate terms affected: promoted current-turn tactical rewind, reactive
  consequence simulation/preview, independent movement/action allowance,
  authored room task set and editable forecast-before-commit time.

## Negative results

- Rejected `SYS-019`, `CON-034`, `INF-009`, `OBJ-011`, `TIM-004`, `TIM-005`,
  `ACT-044`, `INF-018` and `TIM-007` through explicit transition tests.
- `COMB-0014` and `COMB-0047` retain their existing supporters and boundaries;
  forecast terminology does not make Tactical Breach Wizards an exact-intent
  supporter.
- No separate structured negative-result file is required: the selected game
  was a boundary test, not a prior positive supporter or novelty claim.

## Delta summary

## Нові факти

- [Confirmed | Corroborated | High] Foresee exactly simulates hostile
  consequences from the current editable draft, while hostile targets may
  change before that boundary (`TBW-004`–`TBW-007`).

## Нові гени

- [Observation | Corroborated | High] Added `ACT-062`, `SYS-088`, `CON-095`,
  `INF-025`, `OBJ-031` and `TIM-010`; reused eight prior genes.

## Нові комбінації

- [Observation | Corroborated | High] Added verified `COMB-0048` for exact
  reactive forecast plus bounded current-turn revision before commit.

## Зміни таксономії

- [Observation | Corroborated | High] Змін таксономії немає; exact committed
  intent, move-then-ability and branchable history remain narrower records.

## Нові питання

- Does a later authored encounter ever freeze every hostile action before the
  player draft, or do all ordinary enemy families remain state-reactive?
- Should discrete undo remain uncatalogued when it is only recovery UI, while
  `ACT-062` remains limited to explicit forecast-driven tactical drafting?

## Наступна рекомендована гра

- [Hypothesis | Corroborated | High] Checkpoint 048.
- Optimisation criterion: audit the four-game post-checkpoint-044 expansion,
  the six new forecast genes, singleton density and all recurring-combination
  invariants before selecting another game.
- Expected information gain: high for whether forecast/intent/time additions
  are bounded cleanly or signal premature tactical over-fragmentation.
- Backlog impact: retain Hexcells Infinite, Shogun Showdown, Mini Motorways and
  Can of Wormholes until the checkpoint decides the next search direction.

## Чому саме вона

- [Hypothesis | Corroborated | High] The corpus has reached its regular
  four-game checkpoint cadence and the newest tactical cluster introduced six
  adjacent boundary records that require cross-corpus audit before expansion.
