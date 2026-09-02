---
game_id: GAME-0224
slug: once-human
game_title: Once Human
analysis_status: reviewed
reviewed: 2026-09-02
combination_ids:
  - COMB-0222
gene_ids:
  action:
    - ACT-008
    - ACT-161
    - ACT-341
  system:
    - SYS-215
    - SYS-722
  constraint:
    - CON-282
    - CON-564
  information:
    - INF-115
    - INF-119
    - INF-125
    - INF-128
    - INF-268
  objective:
    - OBJ-140
  time:
    - TIM-003
---

# Game: Once Human

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Parameters describe
gene instances but do not enter the signature.

## Analysis scope

- Version / ruleset: current official Windows PC client, Version `3.0.4`,
  checked 2026-09-02 at 09:37 UTC, before the separately announced September 2
  4:00 PM PT maintenance window. The dated version announcement and official
  live service form the reproducible build packet.
- Reproducible account and character: North America; one fresh account with no
  existing non-beginner character; one newly created Meta-Human with ordinary
  character customisation confirmed; keyboard and mouse; third-person camera;
  no inherited, mailed or transferred veteran state. If the current client no
  longer routes this account directly into the declared tutorial, the packet
  must be re-reviewed instead of silently selecting a scenario.
- Primary decision loop: read the current tutorial objective, local target and
  personal health/readiness state; move through the indicated route; address
  the required distortion or calamitous beast with the taught contextual
  interaction or direct combat action; observe completion feedback; repeat for
  the next revealed instruction until the tutorial settles.
- Entry and exit: begins after character confirmation when the new Meta-Human
  first becomes controllable in the eternal realm after the bus disaster under
  Mitsuko's guidance. It succeeds only when the revamped new-player experience
  records completion, grants the Rare fashion `Distant Memory`, and exposes
  scenario/server selection. Choosing a scenario or entering wilderness is
  outside the terminal.
- Included: current authored tutorial stages; direct third-person traversal;
  direct hostile combat; contextual interactions required by current
  instructions; local target, objective, health, readiness, completion and
  reward feedback; the first-character admission rule; completion grant and
  transition to scenario-selection authority.
- Reproducible parameterisation: use the current default Windows client, North
  America, a genuinely fresh account, one new character, keyboard/mouse and
  third-person view; do not skip, accept veteran mail, transfer state or choose
  a scenario. Appearance, name, exact route motion, target order and combat
  timing may vary where the tutorial permits them.
- Excluded: every scenario and server, including Manibus (Novice), permanent
  servers, phase state and world selection; wilderness entry; Monolith of
  Greed, Ravenous Hunter and later Great Ones; territory placement, open-world
  gathering, crafting, survival, looting, Deviant capture/securement and
  automation; first-person presentation; multiplayer, PvP, RaidZone, custom
  servers, events, passes, shop state, account transfers, veteran tutorial
  skip, the veteran mail route and the complete live-service history.
- Potential scoped modules: one current permanent Manibus (Novice) server life,
  one fixed early territory-and-crafting route, one Deviation securement loop
  or one named Monolith run each requires its own version, server, phase, entry
  and retained terminal.
- Direct-play status: no authenticated client or tutorial was played. Current
  official Once Human update, control and scenario-flow pages establish every
  admitted boundary; repository reasoning does not claim personal play. No
  video or audio was opened, played, heard or used.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `ONCE-001` | Version `3.0.4` is the current Windows service packet at the recorded pre-maintenance verification time | Confirmed | Direct | High | P1 |
| `ONCE-002` | Newly created characters directly enter the revamped new-player experience before scenario selection | Confirmed | Direct | High | P2, P3 |
| `ONCE-003` | An account with an existing non-beginner character may skip, so a fresh account makes tutorial admission reproducible | Confirmed | Direct | High | P2 |
| `ONCE-004` | The current opening moves from a transformed bus and Deviant passengers to a controllable Meta-Human in the eternal realm guided by Mitsuko | Confirmed | Direct | High | P2 |
| `ONCE-005` | The tutorial's authored purpose is to guide the new player through a mechanically demonstrated route against distortions and calamitous beasts | Confirmed | Direct | High | P2 |
| `ONCE-006` | Current PC play supports direct movement and combat in third-person, while first-person is an optional presentation excluded here | Confirmed | Direct | High | P4 |
| `ONCE-007` | Tutorial completion grants `Distant Memory` and makes scenario selection available before wilderness entry | Confirmed | Direct | High | P2, P3 |
| `ONCE-008` | Each scenario owns distinct rules/content and servers, so admitting Manibus or a Monolith would cross the declared terminal | Confirmed | Direct | High | P3, P5 |
| `ONCE-009` | The repository trace reproduces account gating, guided combat, completion grant and next-state authority without direct play | Observation | Direct | High | V1 |

## Basic data

- Release / origin: Starry Studio / NetEase Games; the current cross-platform
  live service is maintained through dated version announcements.
- Platform or physical form: authenticated networked Windows PC client; one
  persistent account and character, before entry to any scenario server.
- Puzzle family: tactical forecast and counterplay; real-time system pressure;
  ordered dependency sequencing.
- Primary sources:
  - **[P1]** [official Version 3.0.4 update announcement](https://www.oncehuman.game/news/update/20260824/40780_1312014.html),
    for the current version, Windows payload and announced next maintenance.
  - **[P2]** [official Version 2.2.4 update announcement](https://www.oncehuman.game/news/update/20251223/40780_1278121.html),
    for the revamped tutorial, story entry, fresh/veteran routing, completion
    reward and post-tutorial scenario choice.
  - **[P3]** [official current scenario/server flow](https://www.oncehuman.game/news/update/20260824/40780_1312053.html),
    for tutorial-before-selection ordering and the separation of scenario
    worlds, rules, content and servers.
  - **[P4]** [official first-person-mode development update](https://www.oncehuman.game/news/devBlog/20260703/40781_1306531.html),
    for supported direct movement, combat actions and retained third-person
    presentation in the current client.
  - **[P5]** [official permanent-server rules](https://www.oncehuman.game/news/update/20250530/40780_1237751.html),
    for why permanent scenario life is an adjacent post-selection module.
- Secondary and reproducible sources:
  - **[V1]** repository-side transition trace from `P1`–`P5`; rules reasoning,
    not direct play.
- Claim IDs: `ONCE-001`–`ONCE-009`.

## Mechanical decomposition

### Action Genes

- Existing: `ACT-008`, move the Meta-Human through the current guided route;
  `ACT-161`, directly attack a reachable hostile; `ACT-341`, commit the
  contextual interactions required by the current tutorial instruction.
- New genes: none.
- Parameters: character, route, objective, target, combat input, contextual
  prompt, completion response and scenario-selection surface.
- Claim IDs: `ONCE-004`–`ONCE-007`.

### System Behaviour Genes

- Existing `SYS-215`: direct real-time hostile combat updates the character and
  target state while the tutorial remains active.
- New `SYS-722`: completing the universal pre-scenario tutorial records its
  completion, grants `Distant Memory` and transfers the same character from
  guided play to scenario/server-selection authority.
- Resolution order: account history determines whether tutorial admission is
  mandatory; character confirmation creates the opening; each current
  instruction exposes its local action; movement, interaction and combat
  settle in real time; accepted completion writes the grant and replaces the
  tutorial with scenario selection.
- Claim IDs: `ONCE-002`–`ONCE-007`.

### Constraint Genes

- Existing `CON-282`: authored tutorial stages and completion predicates must
  be satisfied in their current revealed order.
- New `CON-564`: new-character tutorial admission is conditioned by account
  history—fresh accounts enter directly, whereas an account with an existing
  non-beginner character may skip. The scoped packet fixes the mandatory branch.
- Scarce resources: personal health, combat readiness, local reach and the
  first-character admission state; no scenario inventory is admitted.
- Claim IDs: `ONCE-002`, `ONCE-003`, `ONCE-005`–`ONCE-007`.

### Information Genes

- Existing: `INF-115`, local targets and hazards; `INF-119`, personal health
  and combat readiness; `INF-125`, current route/objective and the unlocked
  next-state surface; `INF-128`, declared completion grant; `INF-268`, staged
  tutorial instruction and completion feedback.
- New genes: none.
- Claim IDs: `ONCE-004`–`ONCE-007`.

### Objective Genes

- New `OBJ-140`: complete the current mandatory new-player experience, retain
  `Distant Memory` and regain control at scenario/server selection without
  entering a scenario.
- Partial instruction completion, reaching the final prompt without the grant,
  veteran skip or selecting a server does not satisfy this bounded objective.
- Claim IDs: `ONCE-002`, `ONCE-005`, `ONCE-007`.

### Time Genes

- Existing `TIM-003`: traversal, hostile response, direct combat and readiness
  advance in real time outside blocking interfaces.
- Parameters: movement duration, hostile cadence, action readiness and tutorial
  stage transition.
- Claim IDs: `ONCE-005`, `ONCE-006`.

## Reproducible transitions

| Before | Action | Deterministic or bounded resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Version `3.0.4`; fresh North American account; no non-beginner character | Confirm one new character | The client routes the character directly into the revamped tutorial rather than offering veteran skip | exact admission branch | `ONCE-001`–`ONCE-003` |
| Authored bus disaster has settled | Accept first controllable state in the eternal realm | Mitsuko's guidance and the current staged objective become active | exact playable entry | `ONCE-004`, `ONCE-005` |
| A current instruction exposes a reachable locus | Move to it and commit the taught contextual action | The predicate either settles and reveals the next instruction or remains incomplete | staged guidance and order | `ONCE-005` |
| A required calamitous beast is reachable | Directly attack while inspecting health/readiness | Live damage and response resolve until the declared combat predicate succeeds or the attempt remains active | taught real-time combat | `ONCE-005`, `ONCE-006` |
| Any required tutorial predicate remains incomplete | Leave it unresolved | Completion grant and scenario-selection authority remain unavailable | negative terminal boundary | `ONCE-005`, `ONCE-007` |
| Every current tutorial predicate is complete | Accept the completion transition | The completion flag and `Distant Memory` grant settle; scenario/server selection replaces guided play | positive retained terminal | `ONCE-002`, `ONCE-007` |
| Scenario-selection surface is available | Stop without selecting a scenario | The character remains at the declared terminal; no server, phase or wilderness state enters the genome | ADR-007 boundary | `ONCE-008`, `ONCE-009` |

## Strategic and experiential structure

- Local: read the one revealed instruction, distinguish its required target,
  keep the character in a legal health/readiness state and perform the taught
  interaction or direct attack rather than exploring an unrequested branch.
- Medium-term: convert a sequence of locally explained actions into tutorial
  completion without importing scenario systems that are not yet selected.
- Long-term: turn one mandatory account-history-gated onboarding route into a
  retained cosmetic grant and explicit authority to choose the next ruleset.
- Heuristics: follow current objective feedback; confirm the prompt's target;
  use visible health/readiness state; inspect completion and grant before
  treating the scenario list as the endpoint.
- Failure attribution: objective text, target feedback, personal state,
  completion response and the presence or absence of the scenario-selection
  surface separate action, combat, ordering and terminal errors.
- Player trust: the tutorial reveals one current dependency at a time and the
  final grant plus changed navigation surface make completion inspectable.
- Claim IDs: `ONCE-002`–`ONCE-009`.

## Replay and variation

- Appearance, name, local route motion, attack timing and any permitted target
  order vary; version, fresh-account history, tutorial identity, grant and
  selection terminal stay fixed.
- Combat is live and may vary with performance; admission and completion routing
  are deterministic for the declared account branch.
- Veteran skip is not a replay shortcut for this packet. A future materially
  changed tutorial or a selected scenario requires a new review boundary.

## Adjacent systems and history

- Similar games: World of Warcraft, Aion Classic, The Elder Scrolls V: Skyrim
  Special Edition, Palworld and DayZ connect embodied movement/combat to
  persistent character or world state.
- World of Warcraft retains a long quest/dungeon chain after levelling; Aion
  closes a one-use combat-and-reward instance; Skyrim exits a fixed captivity
  route into a chosen open-world branch. Once Human instead uses account
  history to route a universal pre-scenario tutorial and ends precisely where
  authority to choose a whole scenario ruleset begins.
- Manibus, scenario seasons, permanent servers, territory, survival crafting,
  Deviations and Monoliths remain adjacent modules rather than parameters.
- Claim IDs: `ONCE-002`, `ONCE-003`, `ONCE-007`, `ONCE-008`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-161`, `ACT-341` | movement, hostile attack, contextual interaction |
| System Behaviour | `SYS-215`, `SYS-722` | live combat, tutorial-to-selection settlement |
| Constraint | `CON-282`, `CON-564` | authored order, account-history admission |
| Information | `INF-115`, `INF-119`, `INF-125`, `INF-128`, `INF-268` | local, personal, route, reward and tutorial state |
| Objective | `OBJ-140` | complete, retain grant and stop at scenario choice |
| Time | `TIM-003` | concurrent live traversal and combat |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `223` (`GAME-0001`–`GAME-0223`).
- Exact genome matches: none.
- Tied near matches: `GAME-0223` — Aion Classic (`11 / 24 = 0.458333`).
- Supported combination subsets: `COMB-0222`.
- Scan date: 2026-09-02.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0223` — Aion Classic | `ACT-008`, `ACT-161`, `ACT-341`, `SYS-215`, `CON-282`, `INF-115`, `INF-119`, `INF-125`, `INF-128`, `INF-268`, `TIM-003` | both are current guided live-combat tutorials with local/personal/objective/reward feedback; Aion admits one faction character to typed kill counters, random cooldown resets and attack-upgraded cubes before an irreversible exit, while Once Human gates the opening by account history and transfers completion into authority to choose an otherwise excluded scenario ruleset; the eleven shared genes cover `11 / 14 = 0.785714` of Once Human's smaller genome | Near, `11 / 24 = 0.458333` |

## Combination status

- `COMB-0222` is a verified strict subset coupling account-history-gated
  tutorial admission, taught live combat and completion-granted scenario choice.
- Every earlier verified combination is tested after registration; supporting
  subsets are recorded rather than inferred from live-survival theme.

## Taxonomy impact

- Adds `SYS-722`, `CON-564`, `OBJ-140` and one combination; all movement,
  combat, interaction, information, authored-order and time genes are reused.
- No previously reviewed signature or lifecycle changes.
- The new boundaries isolate account-history-dependent onboarding and the
  tutorial-to-scenario-selection settlement without importing scenario play.

## Negative results

- Palworld's capture, companion, base-labour and crafting genes are absent:
  Once Human exposes related systems after this packet's terminal, not inside
  the evidenced tutorial boundary.
- DayZ and Rust survival, inventory, construction, persistence, offline and
  wipe genes are absent for the same reason.
- `SYS-720`, `SYS-721`, `CON-563` and `OBJ-139` are absent: Once Human neither
  rolls Aion's cooldown reset/cube reward nor closes tutorial access through a
  one-use exit.
- First-person mode, scenario choice, Manibus, Monolith combat, territory,
  crafting, Deviations, PvP and service history do not enter merely because the
  current client exposes them elsewhere.

## Delta summary

## Нові факти

- Поточний перший персонаж проходить оновлене навчання до вибору сценарію й
  сервера; старий задум із permanent server суперечив фактичному порядку.
- Завершення навчання дає `Distant Memory` і відкриває вибір сценарію, тому це
  точний збережений термінал без домішування Manibus або сезонної фази.

## Нові гени

- `SYS-722`, `CON-564` і `OBJ-140` відокремлюють перехід від навчання до вибору
  правил, залежність входу від історії акаунта та точну ціль завершення.

## Нові комбінації

- `COMB-0222` — обов'язкове для нового акаунта навчання перетворює керований
  живий бій на збережену нагороду й право вибрати наступний сценарій.

## Зміни таксономії

- Додано три Active-межі без зміни наявних генів або сигнатур. Сценарії,
  сервери, фази, wilderness, Manibus, Monolith, territory, survival crafting,
  Deviations, PvP, RaidZone, veteran skip, магазин і повна історія live service
  не належать цьому pre-scenario packet.

## Нові питання

- Який майбутній окремий Manibus packet найкраще ізолює territory, crafting,
  Deviant securement і один Monolith terminal без сезонного об'єднання?
- Чи дасть STAR WARS: Squadrons суттєво інший навчальний перехід, коли всі
  рішення залишаються всередині одного фіксованого story mission?

## Наступна рекомендована гра

- [Confirmed | Direct | High] `GAME-0225` STAR WARS: Squadrons.
- Optimisation criterion: compare a fixed authored flight mission with this
  account-gated tutorial while preserving Batch 010 order.
- Expected information gain: cockpit power, shields, targeting and
  countermeasure timing inside a stable mission terminal.
- Backlog impact: Unit 9 of the active nine-game Goal.

## Чому саме вона

- It is the next authorised subject in `SEARCH_DEMAND_GAME_SELECTION_010` and
  contrasts pre-scenario onboarding with one bounded vehicle mission.

## Family classification

- `FAM-009` — Tactical forecast and counterplay.
- `FAM-010` — Real-time system pressure.
- `FAM-017` — Ordered dependency sequencing.
