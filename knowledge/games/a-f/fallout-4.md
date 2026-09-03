---
game_id: GAME-0231
slug: fallout-4
game_title: Fallout 4
analysis_status: reviewed
reviewed: 2026-09-03
combination_ids:
  - COMB-0229
gene_ids:
  action:
    - ACT-008
    - ACT-161
    - ACT-199
    - ACT-232
    - ACT-341
    - ACT-401
  system:
    - SYS-215
    - SYS-369
    - SYS-736
    - SYS-740
  constraint:
    - CON-282
    - CON-285
    - CON-572
  information:
    - INF-115
    - INF-119
    - INF-125
    - INF-128
    - INF-268
    - INF-281
  objective:
    - OBJ-113
  time:
    - TIM-003
    - TIM-007
---

# Game: Fallout 4

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Parameters describe
gene instances but do not enter the signature.

## Analysis scope

- Version / ruleset: current legally available English Windows base game on
  Steam, app `377160`, public Build ID `24564252`, built 2026-08-05 and
  published 2026-08-18, checked 2026-09-03. The packet uses a fresh unmodded
  save on `Normal`; only base-game data are enabled.
- Entry: choose `New Game`, retain the first presented body and appearance,
  name the character `Atlas`, and allocate the fixed initial S.P.E.C.I.A.L.
  budget as 4 in each of Strength, Perception, Endurance, Charisma,
  Intelligence, Agility and Luck. Confirm the profile and continue through the
  authored pre-war home sequence.
- Primary decision loop: read the current objective or prompt; choose a required
  dialogue response or reachable authored object; navigate the evacuation and
  Vault 111 route; collect and equip required supplies; aim and attack required
  radroaches in real time; operate the terminal, doors, Pip-Boy and elevator;
  then verify the exterior quest and retained save state.
- Positive retained terminal: emerge from Vault 111 into controllable exterior
  Commonwealth state, with `War Never Changes` settled and `Out of Time`
  active. Create a manual save, quit cleanly to the main menu, reload it, and
  verify the same exterior character, S.P.E.C.I.A.L. profile, inventory and
  successor objective. The elevator, achievement notification or one transient
  autosave alone is intermediate.
- Negative evaluation terminal: death or a progression-blocking state before
  exterior control ends the attempt. A quickload, autosave or forced-save
  restoration may bound the retry, but it is not positive completion.
- Included: one fixed character packet; seven initial S.P.E.C.I.A.L.
  attributes and their fixed pool; required pre-war dialogue and evacuation;
  catastrophe and cryogenic sequence; Vault 111 traversal; required contextual
  interactions, Pip-Boy acquisition, baton or 10mm pistol pickup, ammunition
  and radroach combat; objective prompts; save types that bound this route;
  first exterior control; `Out of Time`; one manual save/reload verification.
- Reproducible parameterisation: Windows Steam app `377160`; public Build ID
  `24564252`; English; keyboard and mouse; `Normal`; first-person after control
  becomes available; default first appearance; name `Atlas`; all seven initial
  S.P.E.C.I.A.L. values set to 4; direct required route; no optional rooms,
  logs, loot detours or console commands; manual save and immediate reload
  after first exterior control.
- Excluded: Game of the Year and Anniversary bundle unions; all six DLC;
  Creation Club and Creations content; mods; Survival and other difficulties;
  alternate builds; appearance comparison; third-person play; V.A.T.S.; perks
  and levelling; crafting; settlement construction; companions; Sanctuary,
  Codsworth, Red Rocket, Dogmeat, Concord and `When Freedom Calls`; later
  quests, factions and endings; the wider Commonwealth; achievements as a
  progression requirement; other platforms.
- Direct-play status: not directly played in this unit. This is a reproducible
  source-backed transition trace. No audiovisual source was opened, played,
  heard or used.
- Scope rationale: Vault 111 supplies a deterministic fresh-save entry, an
  explicit character-budget decision, ordered interaction and combat, forced
  save boundaries and a reproducible first open-world terminal before the game
  expands into settlement, companion or faction systems.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `FO4-001` | Steam distributes Windows app `377160` separately as base, Game of the Year and Anniversary purchases | Confirmed | Direct | High | P1, P2 |
| `FO4-002` | The current public branch is Build ID `24564252`, published with Bethesda's 2026-08-18 update | Confirmed | Corroborated | High | P3, S1 |
| `FO4-003` | Difficulty is selected through Gameplay settings; this packet fixes `Normal` and excludes Survival | Confirmed | Direct | High | P4 |
| `FO4-004` | Character creation exposes seven S.P.E.C.I.A.L. attributes from 1 to 10 and a fixed initial distribution | Confirmed | Corroborated | High | P5, S2 |
| `FO4-005` | Accepted initial values persist as the character's starting statistical profile | Confirmed | Direct | High | P5 |
| `FO4-006` | The PC manual documents movement, aim, attack, activate, reload, Pip-Boy, V.A.T.S., sneak and save controls | Confirmed | Direct | High | P6 |
| `FO4-007` | Required dialogue, evacuation, Vault entry, cryogenic events and Vault 111 escape advance in authored order | Observation | Corroborated | High | S3, S4 |
| `FO4-008` | Vault 111 requires traversal, object interaction, Pip-Boy acquisition and real-time radroach combat before elevator use | Observation | Corroborated | High | P6, S3, S4 |
| `FO4-009` | Fallout 4 supports three autosaves, one quicksave, manual saves and forced saves at character-creation and Vault 111 boundaries | Confirmed | Direct | High | P7 |
| `FO4-010` | Leaving Vault 111 settles the opening boundary and exposes `Out of Time` as successor quest | Observation | Corroborated | High | S3, S4, S5 |
| `FO4-011` | Reloading a manual exterior save preserves character, inventory and current quest while permitting another future route | Confirmed | Corroborated | High | P7, V1 |
| `FO4-012` | DLC, Creations, settlements and later Commonwealth play are unnecessary to this terminal | Confirmed | Direct | High | P1, P2, V1 |

## Basic data

- Release / origin: Bethesda Game Studios / Bethesda Softworks; original
  release 2015-11-10; current Windows base game remains sold separately.
- Platform or physical form: Windows Steam client; one local single-player
  base-game save on Normal.
- Puzzle family: real-time system pressure; inventory and fixture dependencies;
  ordered dependency sequencing.
- Primary sources:
  - **[P1]** [official Steam product page](https://store.steampowered.com/app/377160/Fallout_4/),
    for current Windows availability and separate purchase options.
  - **[P2]** [official Fallout 4 product page](https://fallout.bethesda.net/en/games/fallout-4/welcome-home),
    for the Anniversary bundle's base game, expansions and Creation Club
    contents, establishing the excluded edition union.
  - **[P3]** [official August 18, 2026 update notes](https://help.bethesda.net/app/answers/detail/a_id/72995/),
    for the current dated game update.
  - **[P4]** [official difficulty support](https://help.bethesda.net/app/answers/detail/a_id/33698/),
    for Gameplay difficulty selection and distinct Survival rules.
  - **[P5]** [official character-system article](https://bethesda.net/en-US/news/fallout-4%27s-character-system),
    for seven 1–10 S.P.E.C.I.A.L. attributes and persistent effects.
  - **[P6]** [official PC manual](https://assets.ctfassets.net/rporu91m20dc/6KoDih86AwOY2MoIgQyCgK/e299f542193c671eb5dd9f7df7c2cf0f/manual_fallout4_pc_en-us.pdf),
    for keyboard/mouse traversal, combat, interaction and interface controls.
  - **[P7]** [official save-system support](https://help.bethesda.net/app/answers/detail/a_id/31908/),
    for autosave, quicksave, manual-save and forced-save behaviour.
- Secondary and reproducible sources:
  - **[S1]** [SteamDB depots](https://steamdb.info/app/377160/depots/), for
    public Build ID `24564252` and timestamps.
  - **[S2]** [Fallout 4 S.P.E.C.I.A.L. record](https://fallout-archive.fandom.com/wiki/Fallout_4_SPECIAL),
    for one base point per attribute plus twenty-one distributable points.
  - **[S3]** [War Never Changes quest record](https://fallout.fandom.com/wiki/War_Never_Changes),
    for character creation, pre-war sequence, Vault entry and authored stages.
  - **[S4]** [written Vault 111 route](https://www.neoseeker.com/fallout-4/walkthrough/Part_I%3A_Betrayal_in_Vault_111%21),
    for required equipment, terminal, radroaches, Pip-Boy and elevator.
  - **[S5]** [Out of Time quest record](https://fallout.fandom.com/wiki/Out_of_Time),
    for successor activation and the first exterior objective state.
- Reproducible control: **[V1]** repository-side transition trace across
  `P1`–`P7` and `S1`–`S5` under the fixed build, character, difficulty and
  retained-terminal parameters; no audiovisual playback or direct-play claim.
- Claim IDs: `FO4-001`–`FO4-012`.

## Mechanical decomposition

### Action Genes

- Existing `ACT-008`: navigate the home, evacuation and Vault; `ACT-161`: aim
  and commit melee or firearm attacks; `ACT-199`: collect and equip required
  items; `ACT-232`: commit required conversation responses; `ACT-341`: activate
  required terminals, doors, pod, Pip-Boy and elevator.
- New `ACT-401`: distribute a fixed initial budget across named character
  attributes and commit the resulting profile.
- Parameters: name, attribute values, response, position, item, target, weapon,
  ammunition, fixture and interaction.
- Claim IDs: `FO4-004`–`FO4-008`.

### System Behaviour Genes

- Existing `SYS-215`: resolve directly commanded real-time combat;
  `SYS-369`: restore an authored or player save after failure; `SYS-736`:
  advance opening instructions and objectives after required predicates.
- New `SYS-740`: retain committed initial attributes as the persistent starting
  profile and apply their declared character-system effects.
- Resolution order: accept input; validate budget, reach, equipment or story
  gate; commit character state or resolve combat/object changes; advance the
  objective and save state; expose exterior control and successor quest.
- Claim IDs: `FO4-004`–`FO4-011`.

### Constraint Genes

- Existing `CON-282`: pre-war, evacuation, cryogenic and Vault gates advance
  in authored order; `CON-285`: weapon use requires compatible equipped state
  and, for the pistol, ammunition.
- New `CON-572`: allocation must preserve the fixed total and keep every named
  attribute within its permitted range.
- Scarce strategic resources: initial points, health, pistol ammunition and
  safe attack timing.
- Claim IDs: `FO4-004`, `FO4-007`–`FO4-009`.

### Information Genes

- Existing `INF-115`: local sight and sound reveal radroaches; `INF-119`:
  expose health, attributes and character state; `INF-125`: expose current
  objective and marker; `INF-128`: expose loot, ammunition and equipment;
  `INF-268`: expose contextual control prompts.
- New `INF-281`: character creation exposes every attribute value and the
  remaining distributable budget before confirmation.
- Claim IDs: `FO4-004`, `FO4-006`–`FO4-010`.

### Objective Genes

- Existing `OBJ-113`: complete a mandatory character gate and authored
  captivity tutorial into retained first exterior open-world control.
- Vault entry, awakening, Pip-Boy acquisition and elevator activation are
  intermediate. Success requires exterior control, successor objective and a
  verified manual reload; death before that boundary is unsuccessful.
- Claim IDs: `FO4-007`–`FO4-011`.

### Time Genes

- Existing `TIM-003`: movement and radroach combat continue in real time;
  `TIM-007`: saves permit a prior state to be restored and continued along a
  different future route.
- Claim IDs: `FO4-006`, `FO4-008`, `FO4-009`, `FO4-011`.

## Reproducible transitions

| Before | Action | Deterministic or bounded resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Character registration exposes seven attributes and a remaining pool | Set every attribute to 4 and confirm | The 28-point total is legal and becomes the starting profile | fixed cross-attribute budget commits before campaign entry | `FO4-004`, `FO4-005` |
| Registration conversation is active | Commit the required response | The dialogue gate closes and evacuation may advance | dialogue is authored progression, not free text | `FO4-007` |
| Evacuation is active | Reach Vault 111 and enter the platform | Disaster and Vault admission advance in fixed order | movement is bounded by authored gates | `FO4-007` |
| The character awakens in Vault 111 | Traverse and operate doors or terminal | Each accepted interaction exposes the next route state | contextual objects gate escape | `FO4-008` |
| A baton or pistol is reachable | Collect and equip it | Compatible equipment becomes usable | world loot changes action authority | `FO4-008` |
| A radroach is alive and reachable | Aim and attack with equipped gear | Hits resolve until either body is defeated | required combat resolves continuously | `FO4-006`, `FO4-008` |
| The Pip-Boy is reachable | Equip it and activate the elevator | The exit accepts the character and raises the platform | equipment and fixture dependencies open the exterior | `FO4-008` |
| Final character confirmation appears | Retain the profile and exit | Commonwealth control appears and `Out of Time` is active | opening sequence settles into open-world control | `FO4-010` |
| Exterior successor state is present | Save, quit and reload | Character, build, inventory and quest state return | explicit retained terminal | `FO4-009`–`FO4-011` |
| The character dies before settlement | Load a prior save | Earlier state returns for a replacement continuation | recovery is branchable but not completion | `FO4-009`, `FO4-011` |

## Strategic and experiential structure

- Local decision: assign a creation point, choose the required response or
  fixture, take the shortest safe route, and select melee or pistol timing.
- Medium-term planning: commit a valid all-fours profile, preserve enough
  health and ammunition, and distinguish mandatory objects from detours.
- Long-term structure: domestic prologue becomes catastrophe, captivity and a
  short tutorial dungeon before the persistent character gains open-world
  control and a successor quest.
- Common heuristics: follow the marker; inspect prompts at sealed doors; equip
  necessary loot; save only after exterior control and successor state exist.
- Failure attribution: point feedback, objective text, prompts, health,
  ammunition, save timestamps and reloaded quest state separate error classes.
- Player trust: fixed build/profile remove ambiguity; named save types and an
  immediate reload make retention testable.

## Replay and variation

- What changes: micro-route, attack timing, damage, weapon and save use.
- Randomness or procedural generation: required gates are authored; incidental
  combat timing varies but no procedural generation enters the packet.
- Multiple viable strategies: baton or pistol handling varies; the all-fours
  build, required gates and exterior terminal do not.
- Typical replay motive: another build, difficulty or faction route; all are
  outside this fixed packet.

## Adjacent systems and history

- Direct predecessors: the base game remains distinct from DLC and the later
  Anniversary/Creations package. Current patching does not authorise a union.
- Similar games: Skyrim Special Edition shares character gate, captivity
  escape, combat, inventory and retained exterior control; Cyberpunk 2077
  shares attributes, dialogue and save-branching; The Witcher 3 shares authored
  quest combat but starts from an established protagonist.
- Important differences: Fallout 4 commits seven starting attributes from one
  pool, passes through pre-war catastrophe and cryogenic captivity, and verifies
  the first Commonwealth save before settlements, companions or factions.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-161`, `ACT-199`, `ACT-232`, `ACT-341`, `ACT-401` | navigate, attack, equip, respond, interact and allocate |
| System Behaviour | `SYS-215`, `SYS-369`, `SYS-736`, `SYS-740` | combat, restoration, staged progression and attributes |
| Constraint | `CON-282`, `CON-285`, `CON-572` | story order, equipment legality and allocation bounds |
| Information | `INF-115`, `INF-119`, `INF-125`, `INF-128`, `INF-268`, `INF-281` | enemies, character, objective, loot, prompts and point budget |
| Objective | `OBJ-113` | retained first exterior open-world control |
| Time | `TIM-003`, `TIM-007` | real time and branchable save restoration |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `230` (`GAME-0001`–`GAME-0230`).
- Exact genome matches: none.
- Tied near matches: `GAME-0224` — Once Human (`11 / 25 = 0.440000`).
- Supported combination subsets: `COMB-0229`.
- Scan date: 2026-09-03.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0224` — Once Human | `ACT-008`, `ACT-161`, `ACT-341`, `SYS-215`, `CON-282`, `INF-115`, `INF-119`, `INF-125`, `INF-128`, `INF-268`, `TIM-003` | Both use direct movement, live attacks, contextual fixtures and ordered tutorial gates under local hostile, character, objective, loot and prompt information. Once Human is account-gated, grants a fashion reward and ends at scenario-selection authority before any server world. Fallout 4 instead commits and retains a fixed attribute budget, includes required dialogue and equipped pickups, supports save restoration and ends after a manually reloaded captivity escape into open-world control; the shared genes cover `11 / 14 = 0.785714` of Once Human's smaller genome. | Near, `11 / 25 = 0.440000` |

### Preserved research notes

- New genes: `ACT-401`, `SYS-740`, `CON-572`, `INF-281`.
- Reused genes: `ACT-008`, `ACT-161`, `ACT-199`, `ACT-232`, `ACT-341`,
  `SYS-215`, `SYS-369`, `SYS-736`, `CON-282`, `CON-285`, `INF-115`,
  `INF-119`, `INF-125`, `INF-128`, `INF-268`, `OBJ-113`, `TIM-003`,
  `TIM-007`.
- Classification result: `New gene`, clarified reused objective and new
  verified interaction combination.
- Evidence and reasoning: fixed initial point allocation is not a lifepath,
  ancestry, class or later perk action. `OBJ-113` is clarified so an escort
  branch is optional, with no earlier signature changes.

## Taxonomy impact

- Registry changes: `ACT-401`, `SYS-740`, `CON-572`, `INF-281`; `OBJ-113`
  gains Fallout 4 support and an optional escort parameter. No lifecycle or
  earlier-signature change.
- Taxonomy-change record: none; this additive support and wording clarification
  preserve the established objective boundary.
- Candidate terms affected: initial attribute allocation, fixed creation
  budget, persistent starting statistics and remaining creation points.
- Taxonomy-health disposition: pending deterministic `BASELINE_231` metrics;
  advisory values will be recorded in the completion log.

## Negative results

- `ACT-231` and `CON-332` are rejected: this packet has no lifepath.
- `ACT-343`, `ACT-238` and `CON-342` are rejected: appearance is fixed and
  cosmetic, with no ancestry, class, background or ability package.
- V.A.T.S., perks, levels, crafting, settlements, followers, DLC and Creations
  are excluded rather than inferred from the wider product.
- Achievement appearance is corroboration, not success; exterior control,
  successor objective and reloaded save are authoritative.
