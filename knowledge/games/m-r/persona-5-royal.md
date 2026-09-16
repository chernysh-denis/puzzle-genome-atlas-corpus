---
game_id: GAME-0291
slug: persona-5-royal
game_title: Persona 5 Royal
analysis_status: reviewed
reviewed: 2026-09-13
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-019
    - ACT-161
    - ACT-341
  system:
    - SYS-355
    - SYS-362
    - SYS-854
    - SYS-855
  constraint:
    - CON-269
    - CON-282
    - CON-629
  information:
    - INF-115
    - INF-119
    - INF-336
  objective:
    - OBJ-026
  time:
    - TIM-001
    - TIM-002
    - TIM-007
    - TIM-022
---

# Game: Persona 5 Royal

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Product labels,
dates, party members, skills and affinities parameterise the genes but do not
enter their canonical labels.

## Analysis scope

- Version / ruleset: current unmodified English Windows Steam application
  `1687950`, one-app package `601219`, default public branch Build ID
  `15515071`, built 2024-08-28 and published 2024-09-06; checked 2026-09-13.
  ATLUS exposes no separate semantic version for this build, so none is
  invented. The 2022 Windows release includes previously released downloadable
  content inside the application rather than as separate Steam DLC apps.
- Product boundary: Persona 5 Royal, not the earlier Persona 5, Persona 5
  Strikers, Persona 5 Tactica, a console edition or any soundtrack. Start with
  no prior Persona 5 save bonus and do not inspect or redeem the cardboard-box
  bonus inventory, summon included legacy Personas, equip bonus costumes or
  invoke network features. Bundled content is therefore part of the product
  offer but supplies no admitted object, action or rule effect.
- Platform, input and difficulty: English interface, Windows, keyboard and
  mouse, offline single player, fresh New Game on `Normal`. Difficulty is
  selected at New Game and remains unchanged. Player naming and the opening
  casino/interrogation framing are setup-only predecessors: they establish the
  fresh campaign but do not contribute a later comparison or decision inside
  this packet.
- Entry: first ordinary overworld control in Yongen-Jaya on 9 April after the
  prologue and name/difficulty setup, before reaching Café Leblanc. The route
  begins with no player-selected free-time activity and follows the mandatory
  opening calendar.
- Primary decision loop: read the current date and day period, authored route
  cues, party health/SP and nearby Shadows; walk the required city, school and
  Palace paths and commit the contextual interactions that advance them; accept
  the fixed calendar transition after each mandatory activity; in the first
  Kamoshida Palace visit select an available attack or Persona skill and its
  target, pay its declared HP/SP requirement, compare attack type with target
  affinity, turn a weakness hit into extra damage and `Down`, and spend the
  resulting `1 More` on another legal command; on 12 April approach the first
  roaming Shadow unseen from behind and attack to instantiate an Ambush with
  the opening advantage; settle that bounded fight, enter the immediately
  following first Safe Room, and create a new manual save there.
- Positive terminal: on 12 April Joker and Morgana have reached the first Safe
  Room of Kamoshida's Palace, with Ryuji present as a non-combat companion; the
  room's save command is available and a new slot write has been accepted. The
  date, party, learned Arsène state, surviving HP/SP, gained experience/items
  and route position are the reproducible saved-state parameters. Because no
  local application or save existed, a quit/load comparison was not performed
  and no returned values are claimed as observed.
- Negative terminal: failure to finish a mandatory battle prevents arrival at
  the Safe Room and requires recovery through the game's retained-history
  controls; this record does not assert a specific unobserved loss screen or
  checkpoint payload. Reaching the room without an accepted save-slot write is
  incomplete, and advancing into the security-level tutorial after leaving it
  crosses the packet boundary.
- Included: authored walking and contextual route interactions; visible date
  and day period; mandatory 9–12 April calendar progression; first Palace
  turn-combat commands; health and SP; physical and skill damage; target
  affinity; weakness damage, `Down` and chained `1 More`; bounded encounter
  rewards and incidental level/skill progress; a visible roaming Shadow;
  behind-and-unnoticed Ambush entry with opening advantage; the first Safe Room;
  context-gated manual saving and branchable retained campaign history.
- Excluded: the casino combat and interrogation as setup-only framing; player
  naming as a game mechanic; optional prior-save and cardboard-box bonuses;
  downloadable Personas, items and costumes; the school-question Knowledge
  reward as an optional dialogue outcome; all security-level, gun, Hold Up and
  All-Out Attack tutorials after the terminal; Persona negotiation, capture,
  switching and fusion; Baton Pass; later party members; free-time scheduling,
  Confidants, social statistics, jobs and activities; Thieves Den; Mementos;
  the rest of Kamoshida's Palace and every later Palace, boss, deadline, ending,
  New Game Plus, network feature, achievement, console rule, modification,
  screenshot, official artwork, third-party image, video and audio.
- Reproducible parameterisation: install Steam app `1687950` from package
  `601219`, verify public Build ID `15515071`, use English Windows keyboard and
  mouse, remain offline, begin fresh New Game on `Normal`, decline or leave
  untouched every inherited/bundled bonus and follow the mandatory 9–12 April
  route. On 11 April use the tutorial weakness to produce `Down` and `1 More`;
  on 12 April attack the first eligible Shadow from behind while unnoticed,
  finish the Ambush and enter the adjacent first Safe Room. Create a fresh
  manual slot without leaving the room. Dialogue wording, incidental damage,
  HP/SP totals, experience, item quantities, battle command order and elapsed
  wall-clock time are parameters unless explicitly fixed above.
- Potential scoped modules: the post-room security/gun/Hold Up/All-Out Attack
  tutorial, Persona capture and party reconfiguration, the first full Palace
  infiltration, a free-calendar week, one Confidant chain, one deadline, a
  boss, the Royal semester, Thieves Den or New Game Plus each requires its own
  version, entry, decision loop, terminal and evidence.
- Direct-play status: not conducted. No installed Persona application, app
  manifest, local save or Steam userdata for app `1687950` was found. Valve and
  ATLUS establish product identity, package, platform, release, included-content
  and New Game difficulty boundaries. Two independent written route families
  corroborate the exact dates, weakness/`Down`/`1 More`, Ambush and first Safe
  Room order; a separate written guide corroborates ordinary and Safe Room save
  contexts. This is an evidence-backed reconstruction, not a claimed
  playthrough, entitlement or reload. No audiovisual source was opened, played,
  heard, analysed or used.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `P5R-001` | Steam app `1687950` and one-app package `601219` identify the released Windows product developed by ATLUS and published by SEGA | Confirmed | Direct | High | P1, P2 |
| `P5R-002` | The default public branch projects Build ID `15515071`; no publisher semantic version is exposed for that build | Observation | Corroborated | Medium | P1, S1 |
| `P5R-003` | This release includes previously released downloadable content, while the scoped route does not redeem or use any inherited or bundled bonus | Confirmed | Direct | High | P1, S2 |
| `P5R-004` | New Game offers a difficulty choice and `Normal` can be held constant without changing story content | Confirmed | Direct | High | P3 |
| `P5R-005` | The mandatory opening advances from the 9 April arrival through school and Palace visits on 11 and 12 April before discretionary calendar scheduling begins | Observation | Corroborated | High | S2, S4, S5 |
| `P5R-006` | During the 11 April Palace tutorial, a skill that strikes weakness deals increased damage, causes `Down` and grants the acting character `1 More`, which can chain through another weakness | Observation | Corroborated | High | S2, S4 |
| `P5R-007` | HP/SP and legal skill costs constrain the opening turn-combat commands, and completed encounters grant experience and item or skill progress | Observation | Corroborated | Medium | S2, S3 |
| `P5R-008` | On 12 April, approaching the first roaming Shadow from behind while unnoticed exposes Ambush and grants the player side an opening advantage | Observation | Corroborated | High | S2, S5 |
| `P5R-009` | The first Safe Room follows that Ambush and permits consultation and manual saving; ordinary Palace corridors do not permit free saving | Observation | Corroborated | High | S2, S3, S4, S5 |
| `P5R-010` | Security level, gun use and All-Out Attack are taught only after leaving the first Safe Room, so they do not belong to this packet | Observation | Corroborated | High | S2, S5 |
| `P5R-011` | No local executable or save was available, so the Safe Room save is a reproducible evidence boundary rather than an executed save/reload observation | Confirmed | Direct | High | R1 |

## Basic data

- Release / origin: ATLUS / SEGA, Windows release 2022-10-20; public Build ID
  `15515071` checked 2026-09-13.
- Platform or physical form: lawfully offered English Windows Steam app
  `1687950`, one-app package `601219`; fresh offline `Normal` New Game.
- Puzzle family: tactical forecast and counterplay; ordered dependency
  sequencing.
- Primary and official sources, accessed 2026-09-13:
  - **[P1]** [Valve application data](https://store.steampowered.com/api/appdetails?appids=1687950&cc=ua&l=english),
    for app, developer, publisher, release, Windows support, single-player
    capability, turn-based/dungeon-crawling description, included downloadable
    content and current offer.
  - **[P2]** [Valve package data](https://store.steampowered.com/api/packagedetails?packageids=601219&cc=ua&l=english),
    for the one-app package and its current Ukraine offer.
  - **[P3]** [official Persona 5 Royal site](https://persona.atlus.com/p5r/?lang=en),
    for New Game difficulty selection, unchanged story content and the broader
    post-opening activity boundary.
- Corroborating textual sources, accessed 2026-09-13:
  - **[S1]** [SteamCMD public-branch projection](https://api.steamcmd.net/v1/info/1687950),
    for Build ID `15515071` and timestamps; secondary distribution data.
  - **[S2]** [GameFAQs Week 1 route](https://gamefaqs.gamespot.com/ps4/260936-persona-5-royal/faqs/78256/week-1-april-9th-april-17th),
    for the 9–12 April order, bonus warning, saving, weakness, `Down`, `1 More`,
    Ambush and first Safe Room tutorials.
  - **[S3]** [GameFAQs Royal walkthrough](https://gamefaqs.gamespot.com/ps4/260936-persona-5-royal/faqs/78629/walkthrough),
    for save-context restrictions, HP/SP skill costs and independent early-
    battle corroboration.
  - **[S4]** [Kamoshida Palace reference](https://megamitensei.fandom.com/wiki/Kamoshida%27s_Palace),
    for independent 11–12 April, weakness/`1 More`, Ambush and Safe Room order.
  - **[S5]** [April written route](https://www.gamerguides.com/persona-5/guide/story-walkthrough/april/continued-investigation),
    for the 12 April rear approach, pre-emptive result, first Safe Room and the
    later security-level tutorial boundary.
- Research record: **[R1]** local preflight on 2026-09-13 found no installed
  application, app manifest, local save or matching Steam userdata.
- Claim IDs: `P5R-001`–`P5R-011`.

## Mechanical decomposition

### Action Genes

- Existing `ACT-008` owns direct authored-route traversal; `ACT-019` selecting
  an available attack or Persona skill and a legal target; `ACT-161` the live
  behind-the-Shadow field strike that requests Ambush; and `ACT-341` contextual
  city, school, Palace-door and Safe Room interactions, including the terminal
  save command.
- No new Action is needed. Dialogue and setup selections are not retained:
  the admitted dialogue options do not change the route, while name and
  difficulty precede entry. Claims: `P5R-004`–`P5R-009`.

### System Behaviour Genes

- Existing `SYS-355` owns transfer from a visible roaming hostile into a
  bounded encounter with a legal pre-emptive advantage. Existing `SYS-362`
  owns bounded combat experience, item and incidental skill-progress rewards.
- New `SYS-854` owns affinity-modified turn-combat damage, `Down`, health and
  defeat. New `SYS-855` independently owns the `1 More` granted after weakness
  knockdown and its repeatable chain before base turn flow resumes.
- Resolution order: field position and hostile attention determine ordinary or
  Ambush entry; the current actor chooses a legal command and target; required
  HP/SP is tested and paid; type affinity modifies damage and status; weakness
  can produce `Down`; the qualifying result grants an immediate `1 More`;
  defeated combatants leave the encounter; completed encounters settle rewards
  and return control to the fixed route. Claims: `P5R-006`–`P5R-008`.

### Constraint Genes

- Existing `CON-269` owns legal target, resource and readiness requirements for
  the selected attack or skill. Existing `CON-282` owns the ordered city,
  school, Palace and Safe Room gates.
- New `CON-629` owns the campaign-context save restriction: the menu command is
  legal in the first Safe Room but not in ordinary Palace corridors or some
  authored scenes. It does not reuse fixture/proximity `CON-621` or live-
  interval/cooldown `CON-602`.
- Scarce resources are party health, Joker's and Morgana's SP, legal attack
  types, the first Ambush approach and the accepted manual slot. Exact values
  are parameters. Claims: `P5R-005`–`P5R-010`.

### Information Genes

- Existing `INF-115` owns partial local Shadow position, facing and attention;
  `INF-119` owns party health, SP, level, skill availability and status.
- New `INF-336` owns the exposed April date, weekday and active day period. A
  future schedule is not disclosed. Affinity feedback is a result parameter of
  `SYS-854`, not a complete pre-action weakness catalogue. Claims:
  `P5R-005`–`P5R-009`.

### Objective Genes

- Existing `OBJ-026`: reach the designated first Safe Room and retain that
  reached state in an accepted manual save. A won battle, entering the room
  without saving or leaving into the next tutorial is not the positive
  terminal. Claims: `P5R-005`, `P5R-008`–`P5R-011`.

### Time Genes

- Existing `TIM-001` owns one battle command and its completed automatic
  resolution before the next command; `TIM-002` owns self-paced traversal and
  contextual interaction outside combat; and `TIM-007` owns player-branchable
  manual save history. The reload path is documented but not performed.
- New `TIM-022` owns the mandatory 9–12 April sequence in which completion of
  the current authored activity advances the calendar before any free activity
  allocation becomes available. Claims: `P5R-005`–`P5R-011`.

## Reproducible transitions

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| 9–10 April mandatory activity remains open | Follow its marker and commit the required interaction | Current segment closes and the next authored period/date becomes active | opening calendar is fixed, not freely allocated | `P5R-005` |
| An acting character has a legal skill and SP/HP cost | Select skill and target | Cost is paid and typed affinity modifies damage and status | action legality is separate from affinity settlement | `P5R-006`, `P5R-007` |
| A standing Shadow is weak to the selected type | Resolve the hit | Damage is increased, the target becomes `Down` and the actor gains `1 More` | weakness changes both state and command schedule | `P5R-006` |
| Another standing weak target remains during `1 More` | Select another compatible skill | Another weakness knockdown can grant another `1 More` | extra-action reward can chain conditionally | `P5R-006` |
| First eligible 12 April Shadow is facing away and unaware | Approach from behind and attack | Battle begins as Ambush with opening player advantage | authored field contact configures encounter entry | `P5R-008` |
| Ambush encounter is settled | Follow Morgana into the adjacent room | First Safe Room becomes the reached route state | the terminal zone follows the taught encounter | `P5R-009` |
| Party is inside the first Safe Room | Open save and choose a new slot | A manual write is accepted in this allowed context | context-gated retained terminal | `P5R-009`, `P5R-011` |
| Party leaves the first Safe Room | Continue along the Palace route | Security-level tutorial begins | exact next mechanic lies outside the packet | `P5R-010` |

## Strategic and experiential structure

- Local decision: choose a legal target and attack type, then decide how to
  spend the immediate `1 More` before the ordinary turn sequence resumes.
- Medium-term planning: preserve HP/SP across the two opening Palace visits and
  approach the 12 April Shadow unseen to secure the taught first-round edge.
- Long-term structure: a fixed calendar unlocks mechanics in authored order and
  carries the learned combat state into the first save-enabled Palace context.
- Common heuristics: test or remember typed weaknesses; prefer an unused weak
  target during `1 More`; approach a roaming Shadow outside its view; save on
  first entering the Safe Room.
- Failure attribution: distinguish an illegal or unaffordable command, a neutral
  affinity result, an already-down target that does not extend the intended
  chain, detection before Ambush and leaving the Safe Room without saving.
- Player-trust factors: visible dates and resource panels, explicit tutorial
  messages, `Weak`/`Down` feedback, Ambush prompt and a clearly named Safe Room
  explain why each transition happened.
- Claim IDs: `P5R-005`–`P5R-010`.

## Replay and variation

- What changes between sessions: optional dialogue wording, combat command
  order, damage and SP totals, incidental rewards and save slot.
- Randomness or procedural generation: damage variance and encounter details
  may vary, but the dates, tutorial order, first Shadow and Safe Room route are
  authored.
- Multiple viable strategies: neutral attacks can finish tutorial enemies, but
  the reproducible route demonstrates at least one weakness/`1 More` chain and
  the taught rear Ambush.
- Typical replay motive: later calendar optimisation, Confidants, Personas,
  Palace routes and endings; all are outside this opening packet.
- Claim IDs: `P5R-005`–`P5R-010`.

## Adjacent systems and history

- Direct predecessors: Persona 5 supplies the broad calendar-and-Palace form;
  Royal is a distinct expanded product and only Royal's Windows release is
  scoped.
- Variants: later difficulties, free-calendar routes, bundled Personas,
  network features, Palaces and New Game Plus can change resources or choices
  and require separate scope.
- Similar games: Baldur's Gate 3 shares direct party traversal, selected
  turn-combat abilities, resource legality and branchable saves; Pokémon
  Legends: Z-A shares player navigation, selected creature abilities, typed
  targets and visible personal resources but resolves combat in live time.
- Important differences: this packet binds a fixed authored calendar to a
  visible-field Ambush and makes weakness knockdown immediately extend the
  acting character's turn before closing at a context-gated Safe Room save.
- Claim IDs: `P5R-001`–`P5R-010`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-019`, `ACT-161`, `ACT-341` | city/Palace route, skill, target, Shadow and Safe Room |
| System Behaviour | `SYS-355`, `SYS-362`, `SYS-854`, `SYS-855` | affinity, damage, `Down`, `1 More`, rewards and Ambush advantage |
| Constraint | `CON-269`, `CON-282`, `CON-629` | HP/SP, target, authored gate and save-enabled context |
| Information | `INF-115`, `INF-119`, `INF-336` | date, period, party resources and hostile attention |
| Objective | `OBJ-026` | first Safe Room and accepted manual slot |
| Time | `TIM-001`, `TIM-002`, `TIM-007`, `TIM-022` | battle resolution, self-paced route, save history and fixed calendar |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `290` (`GAME-0001`–`GAME-0290`).
- Exact genome matches: none.
- Tied near matches: `GAME-0223` — Aion Classic (`8 / 32 = 0.250000`).
- Supported combination subsets: none.
- Scan date: 2026-09-13.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0223` — Aion Classic | `ACT-008`, `ACT-161`, `ACT-341`, `SYS-362`, `CON-269`, `CON-282`, `INF-115`, `INF-119` | Both traverse one authored opening, interact with required route objects, select resource-legal combat actions, read personal and partial hostile state, settle encounters and continue through ordered gates. Aion resolves a persistent real-time class quest with equipment, flight and shared-world progression. Persona 5 Royal instead alternates self-paced authored calendar segments with discrete party turns, configures battle entry through a rear Ambush, turns typed weakness into `Down` and chained `1 More`, and ends at a context-gated manual Safe Room save. | Tied near, `8 / 32 = 0.250000` |

- New genes: `SYS-854`, `SYS-855`, `CON-629`, `INF-336`, `TIM-022`.
- Classification result: `New gene`.
- Evidence and reasoning: existing owners cover selected party abilities,
  pre-emptive field encounter entry, resources, authored gates and branchable
  saves. None owns typed affinity as the modifier of turn-combat damage, the
  consequent weakness-to-extra-action chain, save legality controlled by
  campaign context, the exposed authored day segment or mandatory calendar
  advancement before free scheduling.

### Preserved research notes

- New genes: `SYS-854`, `SYS-855`, `CON-629`, `INF-336`, `TIM-022`.
- Classification result: `New gene`.
- Evidence and reasoning: existing owners cover selected party abilities,
  pre-emptive field encounter entry, resources, authored gates and branchable
  saves. None owns typed affinity as the modifier of turn-combat damage, the
  consequent weakness-to-extra-action chain, save legality controlled by
  campaign context, the exposed authored day segment or mandatory calendar
  advancement before free scheduling.

## Taxonomy impact

- Registry changes: five new Active owners linked above; no earlier gene label,
  lifecycle or signature changes.
- Taxonomy-change record: none; no prior owner is revised.
- Candidate terms affected: Persona, Shadow, Palace, Kamoshida, Safe Room,
  Ambush, `Weak`, `Down`, `1 More`, HP, SP, Arsène, Morgana, Joker, Ryuji,
  Normal, April dates, Steam app/package/build labels and bundled-content names
  remain parameters rather than canonical IDs.

## Negative results

- No new structured negative-result record. `CON-621` and `CON-602` are
  rejected for the Safe Room because neither hostile proximity nor a live
  fixture interval/cooldown defines its menu save gate. `SYS-356` is rejected
  because no upcoming visible turn queue is evidenced. Later All-Out Attack,
  gun, security, negotiation, Persona and free-calendar mechanics fail the
  causal scope test by occurring after the terminal.

## Delta summary

## New facts

- [Observation | Corroborated | High] The 9–12 April opening teaches typed
  weakness into `Down` and chained `1 More`, then rear-entry Ambush before the
  first Safe Room (`P5R-005`–`P5R-010`).
- [Confirmed | Direct | High] App `1687950` and package `601219` define the
  released Windows product; bundled legacy content is not used (`P5R-001`–
  `P5R-004`).

## New genes

- [Observation | Corroborated | High] `SYS-854`, `SYS-855`, `CON-629`,
  `INF-336` and `TIM-022` isolate typed turn-combat affinity, conditional extra
  action, context-gated saving, visible campaign segment and mandatory authored
  calendar progression.

## New combinations

- [Observation | Direct | High] No new combination; no verified combination is
  a strict proper subset of the nineteen-gene genome.

## Taxonomy changes

- [Observation | Direct | High] No existing taxonomy boundary or signature is
  changed.

## New questions

- Does a later free-calendar week require an independent action-and-time gene
  for choosing one activity that consumes the active day period?
- Does Persona negotiation split all-enemy `Down` from Hold Up and its mutually
  exclusive money, item, recruitment and All-Out Attack outcomes?
- Can another turn RPG reuse `SYS-854` without also awarding `SYS-855`?

## Next recommended game

- [Hypothesis | Limited | High] The Forest.
- Optimisation criterion: return from a fixed calendar-and-turn packet to a
  first-person survival world and test shelter, crafting, cave and death-state
  boundaries.
- Expected information gain: determine whether carried survival resources,
  authored cave progression and recoverable or terminal death reuse the broad
  sandbox owners without copying a whole long-horizon survival genome.
- Backlog impact: retain Ori and the Will of the Wisps, V Rising, DARK SOULS™:
  REMASTERED, Noita and MONSTER HUNTER RISE in selection-018 order.

## Why this game

- [Hypothesis | Limited | High] Persona 5 Royal tests the previously uncovered
  intersection of mandatory calendar progression, typed weakness that changes
  turn authority, a visible-field pre-emptive encounter and a context-gated
  retained save terminal after two real-time action-game packets.
