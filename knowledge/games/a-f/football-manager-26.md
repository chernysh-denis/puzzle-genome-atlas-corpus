---
game_id: GAME-0175
slug: football-manager-26
game_title: Football Manager 26
analysis_status: reviewed
reviewed: 2026-08-28
combination_ids:
  - COMB-0173
gene_ids:
  action:
    - ACT-006
    - ACT-304
    - ACT-305
  system:
    - SYS-457
    - SYS-459
    - SYS-460
    - SYS-461
    - SYS-462
    - SYS-463
    - SYS-531
    - SYS-532
    - SYS-533
  constraint:
    - CON-399
    - CON-400
    - CON-401
    - CON-452
    - CON-453
    - CON-454
  information:
    - INF-116
    - INF-216
    - INF-217
    - INF-218
    - INF-219
  objective:
    - OBJ-090
  time:
    - TIM-003
---

# Game: Football Manager 26

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Parameters describe
gene instances but do not enter the signature.

## Analysis scope

- Version / ruleset: PC update `26.3.1`, observed `2026-08-28`; one new men's
  Quick Start career as Liverpool with the default 2025/26 English Premier
  League data and real fixtures, relevant staff responsibilities delegated.
- Primary decision loop: inspect player availability, condition, attributes and
  role suitability; select a legal starting eleven and bench; configure linked
  in-possession and out-of-possession formations, roles and instructions;
  inspect the opponent; run the autonomous match; read score, clock,
  performance, analytics and staff advice; commit legal substitutions or
  tactical changes; let the match engine settle regulation and record the
  fixture result in the competition table.
- Entry and exit: begins at Liverpool's pre-match selection and tactics for the
  home Premier League fixture against AFC Bournemouth on `2025-08-15`; ends
  after the final score and resulting table state are recorded in the career.
- Included: Quick Start and manager profile only as entry gates; squad
  availability and condition; eleven starters and the named bench; positional
  and role suitability; distinct possession shapes; team instructions;
  opponent context; autonomous football, laws, goals, halves and draw policy;
  match overview, xG and staff advice; legal substitutions; live tactical
  revision; final result and table update.
- Excluded: transfers, recruitment, contracts, training, youth development,
  board confidence, finances and long-term season strategy; international or
  women's management; multiplayer, editor and other fixtures; direct control
  of any footballer or the ball; post-season classification.
- Potential scoped modules: one transfer window; training-week planning; squad
  registration; cup extra time and penalties; a multi-match form cycle.
- Direct-play status: not conducted. Official Football Manager material fixes
  the setup, squad, dual-tactics and match-management interfaces; official
  Premier League and IFAB material fixes the fixture and competition laws.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `FM26-001` | Update `26.3.1` is the latest named official FM26 update found for the reviewed PC scope | Observation | Direct | High | P1 |
| `FM26-002` | Quick Start creates a club career and the selected database and real-fixture options define its initial competition state | Confirmed | Direct | High | P2, P3 |
| `FM26-003` | Squad selection exposes availability, condition, attributes and assessed positional or role suitability before lineup commitment | Confirmed | Direct | High | P3, P4 |
| `FM26-004` | FM26 separates in-possession and out-of-possession formations, roles and instructions and previews their relationship | Confirmed | Direct | High | P4 |
| `FM26-005` | The match engine autonomously resolves player decisions and live football from attributes, roles, tactics and match state | Observation | Corroborated | High | P4, P5 |
| `FM26-006` | Match Overview, analytics and staff advice expose evidence for live managerial revisions | Confirmed | Direct | High | P3, P5 |
| `FM26-007` | The manager can commit substitutions and tactical changes but cannot directly steer a footballer or the ball | Confirmed | Direct | High | P4, P5 |
| `FM26-008` | The scoped league fixture uses regulation football laws and permits five substitutes across three opportunities plus half-time | Confirmed | Direct | High | P7, P8, P9 |
| `FM26-009` | Liverpool v AFC Bournemouth on `2025-08-15` is the opening 2025/26 Premier League fixture used by this career scope | Confirmed | Direct | High | P6 |
| `FM26-010` | Regulation settlement records the fixture result and changes persistent competition-table state | Observation | Corroborated | High | P2, P3, P5 |

## Basic data

- Release / origin: `2025`, Sports Interactive / SEGA; update `26.3.1`
  observed `2026-08-28`.
- Platform or physical form: Windows PC single-player career simulation.
- Puzzle family: manager-bounded tactical planning, autonomous agent
  coordination and live evidence-driven intervention.
- Primary sources:
  - `P1` — [official FM26 International Management Update 26.3.1](https://www.footballmanager.com/news/fm26-international-management-update-now-live),
    for the reviewed update boundary.
  - `P2` — [official Starting Your First Save guide](https://www.footballmanager.com/the-dugout/starting-your-first-save-fm26),
    for Quick Start, club selection and manager creation.
  - `P3` — [official First 10 Things to Do guide](https://www.footballmanager.com/the-dugout/first-10-things-do-fm26),
    for database setup, staff responsibilities, squad planning, dual tactics,
    match preparation and the Data Hub.
  - `P4` — [official possession and out-of-possession tactics deep dive](https://www.footballmanager.com/fm26/features/possession-out-possession-fm26s-new-tactical-evolution),
    for dual formations, roles, suitability, the visualizer and match-engine
    interpretation of the declared plan.
  - `P5` — [official match-day experience deep dive](https://www.footballmanager.com/fm26/features/where-storytelling-evolves-fm26s-match-day-experience),
    for autonomous match play, Match Overview, xG, advice and live changes.
  - `P6` — [official Premier League 2025/26 fixture announcement](https://www.premierleague.com/en/news/4324719),
    for Liverpool v Bournemouth on `2025-08-15`.
  - `P7` — [official Premier League five-substitute rule](https://www.premierleague.com/news/2555680),
    for five replacements, three opportunities and nine named substitutes.
  - `P8` — [official Premier League 2025/26 law changes](https://www.premierleague.com/en/news/4373884/whats-new-in-2025-26-season-ifab-laws-and-premier-league-football-principles),
    for the current competition-law boundary.
  - `P9` — [IFAB Laws of the Game 2025/26](https://downloads.theifab.com/downloads/laws-of-the-game-2025-26-single-pages),
    for field, offside, offences, goals and match settlement.
- Secondary source:
  - `S1` — [Steam Football Manager 26 product page](https://store.steampowered.com/app/3551340/Football_Manager_26/),
    for developer, publisher, PC form and release date.
- Reproducibility: URLs and reviewed access date are recorded in the research
  log; claims avoid unobserved hidden match-engine constants and exact player
  ratings.
- Claim IDs: `FM26-001`–`FM26-010`.

## Mechanical decomposition

### Action Genes

- Existing gene: `ACT-006`, alter the rate of the unchanged autonomous match
  presentation.
- New genes: `ACT-304`, configure the eligible lineup and dual tactical plan;
  `ACT-305`, commit a live substitution or tactical revision.
- Parameters: starter, substitute, position, role, possession phase, formation,
  instruction, match speed and confirmation point.
- Claim IDs: `FM26-003`, `FM26-004`, `FM26-006`, `FM26-007`.

### System Behaviour Genes

- Existing genes: `SYS-457`, one live football; `SYS-459`, off-ball team AI;
  `SYS-460`, offences and restarts; `SYS-461`, autonomous goalkeeper;
  `SYS-462`, valid goal; `SYS-463`, halves and regulation settlement.
- New genes: `SYS-531`, autonomous choices from attributes and tactical plan;
  `SYS-532`, evolving condition, performance and injury; `SYS-533`, persistent
  competition-result recording.
- Resolution order: apply the current legal plan; let autonomous agents and the
  football laws resolve the live state; update score, clock, condition,
  performance and analytics; accept any confirmed legal intervention at its
  match boundary; settle regulation; commit the result and table change.
- Claim IDs: `FM26-004`–`FM26-010`.

### Constraint Genes

- Existing genes: `CON-399`, field and goal geometry; `CON-400`, offside;
  `CON-401`, legal football contact.
- New genes: `CON-452`, eligible lineup and bench; `CON-453`, manager-only
  authority; `CON-454`, bench and competition substitution limits.
- Scarce strategic resources: fit eligible starters, bench alternatives,
  positional suitability, player condition, substitutions, substitution
  opportunities, match time and score margin.
- Claim IDs: `FM26-003`, `FM26-007`, `FM26-008`.

### Information Genes

- Existing gene: `INF-116`, live team, score, clock and phase state.
- New genes: `INF-216`, squad evidence; `INF-217`, dual tactical preview;
  `INF-218`, live performance, analytics and advice; `INF-219`, final result
  and competition table.
- Claim IDs: `FM26-003`, `FM26-004`, `FM26-006`, `FM26-010`.

### Objective Genes

- Existing gene: `OBJ-090`, finish regulation with more valid goals than the
  opponent while accepting a draw under the league fixture rules.
- Claim IDs: `FM26-008`, `FM26-010`.

### Time Genes

- Existing gene: `TIM-003`, the match, clock and autonomous agents continue in
  real time while managerial interventions remain available; pause and speed
  are parameters.
- Claim IDs: `FM26-005`–`FM26-008`.

## Reproducible transitions

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Pre-match selection is open | Assign eleven starters and a named bench | Only registered, available, non-duplicated players occupy legal slots | eligible autonomous roster | `FM26-003`, `FM26-008` |
| The selected squad has no confirmed plan | Configure in-possession and out-of-possession shapes, roles and instructions | The visualizer exposes both linked phases and role suitability before confirmation | dual tactical authority | `FM26-004` |
| Kick-off begins | Advance the match | Autonomous footballers act from attributes, roles, tactics and live state while football laws resolve events | manager-bounded simulation | `FM26-005`, `FM26-007` |
| Condition, rating or match pattern creates a concern | Inspect Match Overview, analytics and staff advice | Score, clock, player state and contextual evidence become available before intervention | evidence-driven management | `FM26-006` |
| An eligible substitute and quota remain | Confirm a player replacement | The named substitute replaces the outgoing player and consumes the appropriate quota and opportunity | bounded personnel change | `FM26-007`, `FM26-008` |
| The current shape is underperforming | Confirm a role, shape or instruction change | Autonomous agents apply the revised policy from the next eligible state without direct body control | live policy revision | `FM26-004`, `FM26-007` |
| Second-half regulation ends | Settle the score | Win, loss or draw is fixed, then the fixture and Premier League table record the result | persistent terminal | `FM26-008`, `FM26-010` |

## Strategic and experiential structure

- Local decision: choose the next lineup, role, instruction or replacement
  from incomplete but visible suitability, condition and match evidence.
- Medium-term planning: pair the two possession shapes, distribute duties and
  preserve bench options for predictable fatigue, injuries and score states.
- Long-term structure: this bounded unit retains only the first league result;
  season, transfer and development optimisation remain outside scope.
- Common heuristics: avoid unavailable or exhausted players; ensure the two
  formations transform coherently; compare role suitability with team balance;
  read performance and xG rather than score alone; preserve substitution
  opportunities for late incidents.
- Failure attribution: final score is partly stochastic and opponent-dependent,
  but selections, tactical revisions, match events, ratings and analytics make
  the declared intervention path auditable.
- Player-trust factors: visible eligibility and quota gates prevent impossible
  changes; autonomous resolution must consistently reflect declared roles and
  feedback without pretending to reveal every engine weight.
- Claim IDs: `FM26-003`–`FM26-010`.

## Replay and variation

- What changes between careers: player availability, roles, condition,
  instructions, opponent approach, incidents, event order and result.
- Randomness or procedural generation: the fixture and initial database are
  fixed; autonomous decisions and incident outcomes vary through engine state.
- Multiple viable strategies: possession control, direct transition, higher or
  lower defensive block, narrow or wide roles and different substitution plans
  can all pursue the same regulation objective.
- Typical replay motive: compare tactical hypotheses and adapt the same squad
  to different match states without direct execution control.
- Claim IDs: `FM26-003`–`FM26-010`.

## Adjacent systems and history

- Direct predecessors: earlier Football Manager editions establish the series
  lineage but are not evidence for FM26's dual-formation interface.
- Variants: other clubs, leagues, databases, women's and international teams,
  cup ties, multiplayer and editor-enabled careers change the scope.
- Similar games: EA SPORTS FC 26 shares the ball, laws, team AI, goal and
  regulation genes.
- Important differences: EA SPORTS FC 26 grants direct embodied control and
  ends at a temporary match result; FM26 makes lineup and policy the control
  surface and records the autonomous result in persistent competition state.
- Claim IDs: `FM26-002`–`FM26-010`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-006`, `ACT-304`, `ACT-305` | exact match speed and tactical presets are parameters |
| System Behaviour | `SYS-457`, `SYS-459`–`SYS-463`, `SYS-531`–`SYS-533` | engine weights and exact animation selection are parameters |
| Constraint | `CON-399`–`CON-401`, `CON-452`–`CON-454` | league registration and emergency exceptions are scoped parameters |
| Information | `INF-116`, `INF-216`–`INF-219` | UI layout and exact analytics panels are parameters |
| Objective | `OBJ-090` | league points are consequences, not this fixture's objective |
| Time | `TIM-003` | pause and match-speed options are parameters |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `174` (`GAME-0001`–`GAME-0174`).
- Exact genome matches: none.
- Tied near matches: `GAME-0163` — EA SPORTS FC 26 (`12 / 33 = 0.363636`).
- Supported combination subsets: `COMB-0173`.
- Scan date: 2026-08-28.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| EA SPORTS FC 26 (`GAME-0163`) | live ball, off-ball AI, football laws, goalkeeper, goals, halves, field/contact constraints, score HUD, regulation objective and real time | FM26 removes direct player/ball control, adds eligible lineup and dual-plan authoring, condition/analytics-driven intervention, substitution opportunities and persistent competition recording | Near, `0.363636` |

### Preserved research notes

- New genes: `ACT-304`–`ACT-305`, `SYS-531`–`SYS-533`, `CON-452`–`CON-454`,
  `INF-216`–`INF-219`.
- Classification result: `New gene`, supported reuse and a new combination of
  existing and new genes.
- Evidence and reasoning: individual named tactics, players, star values, exact
  match speeds and UI panels remain parameters; the admitted boundaries change
  player authority, legal intervention or persistent state.

## Taxonomy impact

- Registry changes after normalisation: twelve bounded active genes plus FM26
  support added to thirteen existing records.
- Taxonomy-change record: none. Existing football definitions retain their
  operational boundary and gain a manager-controlled parameterisation.
- Candidate terms affected: gegenpress, low block, mezzala, xG and touchline
  shout are tactics, roles, metrics or interface parameters inside the genes.

## Negative results

- Direct-play evidence was unavailable, so exact player ratings, engine
  weighting, highlight frequency and hidden outcome probabilities were not
  admitted as claims.
- Transfer, training and season-long optimisation were rejected because they
  do not resolve inside the one-fixture terminal boundary.

## Delta summary

## Нові факти

- [Confirmed/Observation | Direct/Corroborated | High] Зафіксовано FM26
  `26.3.1`, окремі формації у володінні й без м'яча, автономний матч і запис
  результату першої лігової гри (`FM26-001`–`FM26-010`).

## Нові гени

- [Confirmed/Observation | Direct/Corroborated | High] Дванадцять нових генів
  ізолюють менеджерський склад, двофазний план, живі втручання, автономні
  рішення, стан гравців, квоти й інформаційні поверхні (`FM26-003`–`FM26-010`).

## Нові комбінації

- [Observation | Corroborated | High] `COMB-0173` поєднує менеджерську
  авторизацію з автономним футбольним вирішенням і записом результату
  (`FM26-003`–`FM26-010`).

## Нові зв'язки

- [Observation | Corroborated | High] Найближча EA SPORTS FC 26 ділить
  футбольні закони, але має принципово іншу межу прямого керування (`FM26-005`,
  `FM26-007`, `FM26-010`).

## Зміни таксономії

- [Observation | Corroborated | High] Наявні футбольні гени отримали другий
  доказовий приклад без зміни меж; життєвий цикл не змінено.

## Джерела

- [Confirmed | Direct | High] Офіційні матеріали Football Manager описують
  setup, tactics і match day; Premier League та IFAB задають fixture й laws.

## Що перевірено востаннє

- [Observation | Direct | High] На `2026-08-28` останнім знайденим офіційним
  update був `26.3.1`; майбутні патчі не узагальнено.

## Ризики

- [Inference | Corroborated | Medium] Патчі можуть змінити UI, ratings і
  engine balance; запис прив'язаний до update `26.3.1` та однієї fixture scope.
