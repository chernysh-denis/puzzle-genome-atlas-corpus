---
game_id: GAME-0176
slug: xcom-2
game_title: XCOM 2
analysis_status: reviewed
reviewed: 2026-08-28
combination_ids:
  - COMB-0174
gene_ids:
  action:
    - ACT-014
    - ACT-019
    - ACT-126
    - ACT-183
    - ACT-306
    - ACT-307
  system:
    - SYS-004
    - SYS-208
    - SYS-386
    - SYS-534
    - SYS-535
    - SYS-536
    - SYS-537
    - SYS-538
  constraint:
    - CON-001
    - CON-011
    - CON-262
    - CON-269
    - CON-273
    - CON-455
  information:
    - INF-220
    - INF-221
  objective:
    - OBJ-029
    - OBJ-100
  time:
    - TIM-005
---

# Game: XCOM 2

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Parameters describe
gene instances but do not enter the signature.

## Analysis scope

- Version / ruleset: vanilla XCOM 2 for PC, Steam public build `8270065`,
  observed `2026-08-28`; Rookie difficulty, tutorial disabled, no DLC, mods or
  War of the Chosen systems.
- Primary decision loop: inspect concealment, detection risk, cover, movement
  bands and attack odds; interleave commands among four rookies; spend each
  soldier's two Action Points on movement, attacks, grenades, reload, Overwatch
  or the mission interaction; commit the squad phase; observe enemy decisions
  and prepared reaction fire; repeat until X4 is planted and all hostiles are
  eliminated or the squad is lost.
- Entry and exit: begins with four concealed rookies at the generated
  Operation Gatecrasher monument map; ends when the planted-charge and hostile
  clearance requirements settle the mission result. On Rookie without the
  tutorial the scope contains six hostiles.
- Included: generated tactical map; fixed occupancy grid; line of sight;
  half/full cover and flanking; concealment and pod activation; two Action
  Points per soldier; free squad switching; ranged probability; finite
  ammunition and reload; grenades and destructible cover; Overwatch; player
  and enemy phases; X4 interaction; health, wounds, death and result.
- Excluded: tutorial scripting; later missions; Avenger strategy layer;
  research, construction, recruitment and promotions; DLC, War of the Chosen,
  multiplayer, Ironman and save reloading; exact hidden AI or hit-roll formula.
- Potential scoped modules: one timed extraction mission; class abilities after
  promotion; a strategy-layer month; War of the Chosen faction systems.
- Direct-play status: not conducted. Official manuals and publisher material
  establish the tactical controls and rules; the secondary Gatecrasher record
  fixes the tutorial-off encounter boundary.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `XCOM2-001` | Steam public build `8270065` is the current observed vanilla PC build boundary | Observation | Corroborated | High | S2, S3 |
| `XCOM2-002` | Tutorial-off Gatecrasher starts four concealed rookies against six hostiles on Rookie and requires monument sabotage | Observation | Corroborated | High | S1 |
| `XCOM2-003` | Most tactical maps are procedurally generated while cells, obstacles and exclusive occupancy bound movement | Confirmed | Direct | High | P1, P3 |
| `XCOM2-004` | Soldiers normally receive two Action Points and blue/yellow movement bands disclose first and final movement authority | Confirmed | Direct | High | P1, P2 |
| `XCOM2-005` | Cover, flanking, range and sight shape ranged attacks whose hit, damage and critical information is shown before fire | Confirmed | Direct | High | P1, P2 |
| `XCOM2-006` | Detection or declared actions break concealment and revealed pods enter active tactical behaviour | Confirmed | Direct | High | P1, P2, P3 |
| `XCOM2-007` | Overwatch spends remaining authority to prepare a modified shot against eligible enemy movement | Confirmed | Direct | High | P1, P2 |
| `XCOM2-008` | Firearms use finite magazines, reload restores ammunition, and grenades can damage units and eligible geometry | Confirmed | Direct | High | P1, P2 |
| `XCOM2-009` | Committing the squad phase yields an autonomous hostile phase before soldier authority refreshes | Observation | Corroborated | High | P1, P2 |
| `XCOM2-010` | Gatecrasher settlement requires both planting X4 and eliminating the finite hostile set | Observation | Corroborated | High | S1 |
| `XCOM2-011` | Tactical damage can create recovery wounds while lethal loss permanently removes a soldier from the campaign | Confirmed | Direct | High | P1, P2 |

## Basic data

- Release / origin: `2016`, Firaxis Games / 2K; Steam public build `8270065`
  observed `2026-08-28`.
- Platform or physical form: Windows PC, mouse-and-keyboard single-player
  turn-based tactical mission.
- Puzzle family: tactical forecast and counterplay, agent routing and
  coordination, ordered dependency sequencing.
- Primary sources:
  - `P1` — [official Steam-hosted XCOM 2 manual](https://cdn.akamai.steamstatic.com/steam/apps/268500/manuals/XCOM2_Manual_English.pdf),
    especially pages 4–8 for HUD, procedural maps, permanent death, Action
    Points, cover, concealment, attacks, reload, Overwatch and interactions.
  - `P2` — [current official Feral XCOM 2 manual](https://www.feralinteractive.com/en/manuals/xcom2/latest/steam/),
    for the maintained PC control and tactical-rule description.
  - `P3` — [official 2K XCOM 2 product page](https://store.2k.com/game/buy-xcom-2-pc),
    for concealment, ambush, fallen soldiers and generated mission variety.
  - `P4` — [official 2K XCOM 2 FAQ](https://support.2k.com/hc/en-us/articles/216650707-XCOM-2-FAQ),
    for current support boundary, concealment and mission collection behaviour.
- Secondary sources:
  - `S1` — [Operation Gatecrasher mission record](https://xcom.fandom.com/wiki/Operation_Gatecrasher_%28Sabotage_ADVENT_Monument%2C_XCOM_2%29),
    for the tutorial-off four-rookie, six-hostile, X4 and untimed scope.
  - `S2` — [official Steam XCOM 2 product page](https://store.steampowered.com/app/268500/XCOM_2/),
    for platform, release and publisher metadata.
  - `S3` — [SteamDB depot history](https://steamdb.info/app/268500/depots/),
    for observed public build `8270065`.
- Reproducibility: URLs, build and access date are recorded in the research
  log; no hidden hit-roll or AI constant is asserted.
- Claim IDs: `XCOM2-001`–`XCOM2-011`.

## Mechanical decomposition

### Action Genes

- Existing genes: `ACT-014`, relocate a selected soldier to a legal cell;
  `ACT-019`, choose a soldier ability and target; `ACT-126`, end the squad
  combat phase; `ACT-183`, reload the active firearm.
- New genes: `ACT-306`, arm movement-triggered reaction fire; `ACT-307`, commit
  an adjacent mission interaction.
- Parameters: soldier, destination, movement band, weapon, target, grenade,
  reload, Overwatch trigger, X4 fixture and confirmation.
- Claim IDs: `XCOM2-004`, `XCOM2-005`, `XCOM2-007`–`XCOM2-010`.

### System Behaviour Genes

- Existing genes: `SYS-004`, generated-map and combat randomness; `SYS-208`,
  cover-dependent ranged resolution; `SYS-386`, destructible geometry.
- New genes: `SYS-534`, per-soldier Action Point refresh and spend; `SYS-535`,
  concealment break and pod activation; `SYS-536`, Overwatch resolution;
  `SYS-537`, hostile squad-phase decisions; `SYS-538`, persistent wound or
  death settlement.
- Resolution order: refresh surviving soldiers; accept interleaved legal
  commands; activate revealed pods; commit the squad phase; resolve prepared
  reactions and hostile commands; update health and objectives; test mission
  terminal; otherwise refresh the next squad phase.
- Claim IDs: `XCOM2-003`–`XCOM2-011`.

### Constraint Genes

- Existing genes: `CON-001`, fixed occupancy capacity; `CON-011`, exclusive
  occupancy and barriers; `CON-262`, magazine and grenade capacity; `CON-269`,
  legal target, range, resource and readiness; `CON-273`, fog and detection.
- New gene: `CON-455`, Action Point and terminal-action legality.
- Scarce strategic resources: soldier health, personal Action Points, cover,
  sight, concealment, ammunition, grenade charges and remaining squad bodies.
- Claim IDs: `XCOM2-003`–`XCOM2-009`, `XCOM2-011`.

### Information Genes

- New genes: `INF-220`, soldier authority, cover and attack forecast;
  `INF-221`, concealment, detection risk and mission-objective state.
- Claim IDs: `XCOM2-004`–`XCOM2-010`.

### Objective Genes

- Existing gene: `OBJ-029`, eliminate the finite hostile encounter set.
- New gene: `OBJ-100`, plant the declared sabotage charge at its fixture.
- Claim IDs: `XCOM2-002`, `XCOM2-010`.

### Time Genes

- Existing gene: `TIM-005`, flexible player planning commands followed by a
  committed hostile-resolution phase.
- Claim IDs: `XCOM2-004`, `XCOM2-007`, `XCOM2-009`.

## Reproducible transitions

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| A concealed soldier is selected | Preview a blue or yellow destination | Reachable cells and cover outcomes are shown before movement | personal AP and spatial legality | `XCOM2-004`, `XCOM2-005` |
| The first move remains outside every shown detector | Commit the move | The soldier relocates, spends one point and squad concealment remains | concealed approach | `XCOM2-004`, `XCOM2-006` |
| A move crosses detection or the squad fires | Resolve reveal | Concealment ends and the encountered pod activates | information-to-behaviour transition | `XCOM2-006` |
| A hostile is visible | Select Fire | The HUD exposes odds, then the shot consumes authority and ammunition and resolves randomly | forecasted uncertainty | `XCOM2-005`, `XCOM2-008` |
| A grenade and legal area remain | Commit the grenade | The charge is consumed and compatible units and cover receive the declared blast | finite deterministic area tool | `XCOM2-008` |
| A soldier retains final authority | Select Overwatch | Remaining ordinary authority becomes one movement-triggered prepared attack | cross-phase commitment | `XCOM2-007` |
| No further player commands are desired | End the phase | Hostile movement may trigger Overwatch, then alerted enemies choose and resolve commands | faction phase alternation | `XCOM2-007`, `XCOM2-009` |
| A soldier stands by the monument | Plant X4 | The adjacent interaction records the sabotage requirement | objective dependency | `XCOM2-010` |
| X4 is planted and no hostile survives | Settle mission | The result closes and surviving health becomes ready or wounded roster state | conjunctive terminal and persistence | `XCOM2-010`, `XCOM2-011` |

## Strategic and experiential structure

- Local decision: compare cover, detection, target odds and remaining personal
  authority before each move, shot, grenade, reload or Overwatch commitment.
- Medium-term planning: interleave soldiers so the first move creates sight and
  flanks without stranding later actors; preserve ammunition and safe cover for
  the enemy phase; sequence X4 access with hostile clearance.
- Long-term structure: this unit retains only wound or permanent-loss effects
  needed to make tactical risk meaningful; broader campaign optimisation is
  outside scope.
- Common heuristics: stay concealed until several soldiers can exploit the
  reveal; avoid yellow moves into unknown detection; use grenades to remove
  cover; reload before the phase where a shot or Overwatch is required; do not
  cluster where one attack can punish the squad.
- Failure attribution: outcomes are probabilistic, but displayed hit chances,
  cover state, movement bands, detection risk and action history expose the
  distinction between a risky plan and an unlucky roll.
- Player-trust factors: forecast values must correspond to the committed state;
  concealment boundaries and terminal actions must not change after selection.
- Claim IDs: `XCOM2-003`–`XCOM2-011`.

## Replay and variation

- What changes between attempts: generated geometry, cover, pod positions,
  soldier appearance, hit and critical results, injuries and enemy choices.
- Randomness or procedural generation: the mission type, roster size and
  objectives remain bounded while the map and attack outcomes vary.
- Multiple viable strategies: cautious Overwatch approach, coordinated close
  flank, grenade-led cover removal and several safe X4 routes may succeed.
- Typical replay motive: recover from soldier loss, test a lower-risk opening
  or compare tactical use of the same four rookies on new geometry.
- Claim IDs: `XCOM2-002`–`XCOM2-011`.

## Adjacent systems and history

- Direct predecessors: X-COM and XCOM: Enemy Unknown establish the lineage but
  are not evidence for XCOM 2's concealment and procedural mission boundary.
- Variants: tutorial Gatecrasher, higher difficulty, Ironman, DLC, War of the
  Chosen, later class abilities and multiplayer change the scope.
- Similar games: Tactical Breach Wizards shares selected-unit movement,
  abilities, grid constraints and finite hostile clearance.
- Important differences: XCOM 2 adds probabilistic ranged combat, squad
  concealment and pod activation, per-soldier Action Points, hostile phases,
  ammunition, destructible cover and persistent wounds or death.
- Claim IDs: `XCOM2-002`–`XCOM2-011`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-014`, `ACT-019`, `ACT-126`, `ACT-183`, `ACT-306`, `ACT-307` | exact weapon and grenade selections are parameters |
| System Behaviour | `SYS-004`, `SYS-208`, `SYS-386`, `SYS-534`–`SYS-538` | hidden rolls and AI weights are parameters |
| Constraint | `CON-001`, `CON-011`, `CON-262`, `CON-269`, `CON-273`, `CON-455` | difficulty modifiers are parameters |
| Information | `INF-220`, `INF-221` | HUD layout is presentation |
| Objective | `OBJ-029`, `OBJ-100` | kill and sabotage order may vary |
| Time | `TIM-005` | animation speed is a parameter |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `175` (`GAME-0001`–`GAME-0175`).
- Exact genome matches: none.
- Tied near matches: `GAME-0048` — Tactical Breach Wizards (`5 / 34 = 0.147059`).
- Supported combination subsets: `COMB-0174`.
- Scan date: 2026-08-28.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| Tactical Breach Wizards (`GAME-0048`) | selected-unit relocation, targeted abilities, grid capacity, barriers and finite hostile clearance | XCOM 2 adds personal Action Points, probabilistic cover fire, concealment and pod activation, ammunition, cross-phase Overwatch, autonomous enemy phases, sabotage and persistent casualties | Near, `0.147059` |

### Preserved research notes

- New genes: `ACT-306`, `ACT-307`, `SYS-534`–`SYS-538`, `CON-455`,
  `INF-220`, `INF-221`, `OBJ-100`.
- Classification result: `New gene`, supported reuse and a new combination of
  existing and new genes.
- Evidence and reasoning: exact weapons, map seed, difficulty modifiers, hidden
  rolls and AI weights remain parameters; admitted boundaries change command
  authority, phase interaction or persistent state.

## Taxonomy impact

- Registry changes after normalisation: eleven bounded active genes plus XCOM
  2 support for fourteen existing records.
- Taxonomy-change record: none. Existing movement, combat, resource and phase
  definitions retain their operational boundary.
- Candidate terms affected: pod, yellow move, full cover, Rookie and X4 are
  game-specific entities or parameters inside the genes.

## Negative results

- Direct-play evidence was unavailable, so hidden hit-roll formulae, AI weights,
  precise pod placement and unobserved difficulty modifiers were not admitted.
- Strategy-layer research, construction, recruitment and promotions were
  rejected because they do not resolve inside the Gatecrasher terminal.
- `SYS-357`, `ACT-281` and `TIM-018` were rejected because they encode a
  different AP source or civilisation-scale turn boundary.

## Delta summary

## Нові факти

- [Confirmed/Observation | Direct/Corroborated | High] Зафіксовано базову PC
  build `8270065`, tutorial-off Gatecrasher, чотирьох прихованих новобранців,
  дві дії, Overwatch, X4 та очищення (`XCOM2-001`–`XCOM2-011`).

## Нові гени

- [Confirmed/Observation | Direct/Corroborated | High] Одинадцять нових генів
  ізолюють AP загону, активацію після викриття, реактивний вогонь, ворожу фазу,
  постійні втрати, X4 і тактичні інформаційні поверхні (`XCOM2-004`–`XCOM2-011`).

## Нові комбінації

- [Observation | Corroborated | High] `COMB-0174` поєднує приховане планування
  загону, майбутню реакцію на рух, диверсію та очищення (`XCOM2-004`–`XCOM2-011`).

## Нові зв'язки

- [Observation | Corroborated | High] Найближча Tactical Breach Wizards ділить
  п’ять grid-tactics генів, але не має XCOM-структури ризику й фаз
  (`XCOM2-004`–`XCOM2-011`).

## Зміни таксономії

- [Observation | Corroborated | High] Наявні гени отримали новий доказовий
  приклад без зміни життєвого циклу; taxonomy-change record не потрібен.

## Джерела

- [Confirmed | Direct | High] Офіційні manual, Feral і 2K задають тактичні
  правила; Gatecrasher record лише уточнює tutorial-off encounter boundary.

## Що перевірено востаннє

- [Observation | Corroborated | High] На `2026-08-28` публічна Steam build
  `8270065` лишалася поточною; майбутні патчі не узагальнено.

## Ризики

- [Inference | Corroborated | Medium] Secondary mission record може змінитися;
  твердження про шість ворогів прив’язано до Rookie tutorial-off scope.

Next recorded unit: `GAME-0177` — Rocket League.
