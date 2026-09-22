---
game_id: GAME-0353
slug: deus-ex-game-of-the-year-edition
game_title: "Deus Ex: Game of the Year Edition"
analysis_status: reviewed
reviewed: 2026-09-22
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-161
    - ACT-164
    - ACT-183
    - ACT-191
    - ACT-199
    - ACT-202
    - ACT-232
    - ACT-341
    - ACT-424
  system:
    - SYS-057
    - SYS-208
    - SYS-215
    - SYS-369
    - SYS-373
    - SYS-379
    - SYS-780
  constraint:
    - CON-210
    - CON-282
    - CON-285
    - CON-296
    - CON-304
    - CON-322
    - CON-394
  information:
    - INF-073
    - INF-115
    - INF-119
    - INF-125
    - INF-128
    - INF-148
    - INF-302
  objective:
    - OBJ-155
  time:
    - TIM-003
    - TIM-007
---

# Game: Deus Ex: Game of the Year Edition

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). J.C. Denton,
UNATCO, NSF, Liberty Island, Paul Denton, Harley Filben, Leo Gold, NanoKey,
multitool, lockpick, `NSF001`, `smashthestate`, Steam and Build `251801` are
carrier parameters, not gene names.

## Analysis scope

- Version / ruleset: current unmodified English Windows Steam app `6910`,
  *Deus Ex: Game of the Year Edition*, public branch Build ID `251801`, built
  2014-05-01, content depot `6911`, checked 2026-09-22. The distribution
  identifiers are secondary observations; the official Steam manual and
  storefront define the licensed product. No mod, renderer replacement or
  community patch is admitted.
- Structured analysis target: the optional three-part UNATCO Training mission
  followed by one fresh Medium-difficulty campaign from character creation,
  through Mission 1's Liberty Island and UNATCO Headquarters segments, to first
  ordinary Battery Park control and one save/reload retention check; see
  `GAME-0353` in
  [`knowledge/platforms/games.json`](../../platforms/games.json).
- Entry: select Training from the main menu and begin its first general-training
  room with no imported state. Complete general, combat and covert training and
  the final test. Then start a separate New Game on Medium, keep the default
  Trained Pistols level, raise Computers to Trained for `1125` points,
  Electronics to Trained for `1800` and Lockpicking to Trained for `1800`,
  leaving `275` of the initial `5000` points, and enter first control at the
  Liberty Island south dock. Training state does not carry into the campaign.
- Primary decision loop: read the first-person view, sound, IFF, body diagram,
  ammunition, inventory grid, Goals/Notes and local codes; walk, run, crouch,
  lean, jump, climb or swim; choose and ready a compatible item or weapon;
  rearrange bounded inventory footprints; converse and commit a response;
  enter a learned code or login, use a nanokey, lockpick or multitool, or use a
  physical route; avoid suspicion or fight in real time; manage ammunition,
  tools, regional health and skill state; satisfy the current primary goal and
  continue to the next authored gate.
- Fixed reproducible route: finish every mandatory Training room, using the
  demonstrated nanokey, lockpick, code, multitool, crouched stealth and one
  legal final-test route. In Mission 1 take Paul's mini-crossbow, meet Harley
  Filben, promise not to kill the NSF commander and receive the Statue-door
  key. Read the nearby datacube, use `NSF001` / `smashthestate` at the security
  terminal, enter through the front-door route, and avoid or neutralise only
  threats that block ascent. Reach Leo Gold and select the response that makes
  him surrender. Report to Paul, enter UNATCO HQ, report to Manderley, accept
  the next briefing, return to the south dock and board the police boat. At
  first ordinary Battery Park control, create a manual save, reload it and
  confirm the retained successor state.
- Positive terminal: boarding the boat settles Mission 1 and instantiates
  Battery Park with the carried build, inventory and campaign flags; a manual
  save/reload restores that first successor state. Merely completing Training,
  entering the Statue, obtaining credentials or reaching the commander does not
  complete this packet.
- Failure and recovery: black head or torso health kills J.C.; damaged arms or
  legs impair aim, running or jumping before that terminal. Loading an admitted
  manual or automatic save replaces transient position, awareness, damage,
  inventory and objective state with the recorded snapshot and permits a
  different continuation.
- Included: direct first-person traversal, crouch and lean; interaction focus;
  fixed initial skill allocation and later skill-point visibility; thirty-cell
  inventory, multi-cell items, stacks, hotbar aliases and rearrangement;
  nanokeys, one code/login pair, lockpicks and multitools; player-selected
  conversation responses; finite ammunition and reload; aimed regional hits;
  local sight, sound, suspicion, alarms, search and combat; regional body
  health and its performance penalties; primary/secondary goal distinction;
  ordered Mission 1 goals; mission settlement, Battery Park handoff and
  save/reload retention.
- Reproducible parameters: exact movement, guard phase, optional non-blocking
  pickups, damage, ammunition and tool counts may vary. Keep the declared skill
  allocation, mini-crossbow offer, Harley promise, front-door/security-terminal
  route, Leo surrender, required HQ chain and Battery Park retention check.
  Direct combat and rear-crate entry remain evidenced alternatives but are not
  required conduct for the fixed trace.
- Excluded: the SATCOM compound, sunken boat, electrical bunker, secret
  communicator, freeing Gunther, full exploration or skill-point collection,
  every kill/loot target, installing the first augmentation, weapon upgrades,
  optional Sam/Jaime/Anna visits, later Battery Park play, Mission 2 onward,
  multiplayer, speedrun or duplication exploits, cheats, save editing, mods,
  fan patches, other PC builds, macOS, PlayStation 2, later series games and
  audiovisual criticism.
- Potential scoped modules: a nonlethal conduct comparison, a direct-assault
  route, optional security areas, augmentation installation, or a later mission
  with stronger persistent consequences. None is inherited here.
- Direct-play status: not conducted. No entitlement, depot, executable, save,
  input trace, screenshot, video or audio was obtained or inspected. The
  licensed product and manual plus independently written Training and Mission 1
  routes support a bounded reconstruction, not a claimed playthrough or
  byte-level audit.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `DX-001` | The target is the unmodified English Windows Steam GOTY app `6910`, public Build `251801`, not a mod or later series entry | Confirmed | Corroborated | High | P1, P2, S1 |
| `DX-002` | Training independently demonstrates keys, lockpicks, codes, multitools, movement, regional injury, combat, stealth and multiple final-test solutions | Observation | Corroborated | High | P2, S2 |
| `DX-003` | New Game offers four damage-only difficulty settings, eleven four-level skills, Trained Pistols and `5000` allocable starting points | Confirmed | Direct | High | P2, S3 |
| `DX-004` | Thirty inventory cells, multi-cell footprints, stacks, rearrangement and hotbar aliases make carried layout decision-relevant | Confirmed | Direct | High | P2 |
| `DX-005` | Credentials, nanokeys, lockpicks, multitools and physical bypasses provide distinct access routes without becoming distinct genes | Confirmed | Corroborated | High | P2, S2, S4 |
| `DX-006` | Crouching, distance, shadow and lower movement noise reduce ordinary acquisition, while sensors, proximity, attack and noise can still reveal J.C. | Confirmed | Direct | High | P2 |
| `DX-007` | Firearms use finite compatible ammunition and aimed hits resolve against body regions; regional injury changes capability and black head or torso health is lethal | Confirmed | Direct | High | P2 |
| `DX-008` | Mission 1 admits a key/front-door route and a rear-crate route, then a dialogue response can settle Leo Gold through surrender | Observation | Corroborated | High | S3, S4 |
| `DX-009` | Required goals continue through UNATCO HQ and the south-dock boat; Battery Park is the immediate successor and cannot be reversed into Liberty Island | Observation | Corroborated | High | S3, S4 |
| `DX-010` | Manual save/load can retain first Battery Park control and permit a different continuation from the recorded snapshot | Confirmed | Direct | High | P2, V1 |
| `DX-011` | The admitted signature is source-bounded and does not prove that Build `251801` was executed locally | Observation | Direct | High | P1, P2, S1–S4, V1 |

## Basic data

- Release / origin: Ion Storm; original Windows release 2000-06-22; publisher
  Eidos Interactive Corp.; Steam GOTY app `6910`.
- Platform or physical form: licensed English Windows Steam distribution,
  content depot `6911`, public Build ID `251801`.
- Puzzle family: tactical forecast and counterplay; real-time system pressure;
  knowledge and evidence progression; inventory and fixture dependencies;
  world topology and perspective; ordered dependency sequencing.
- Primary and official sources, accessed 2026-09-22:
  - **[P1]** [official Steam product page](https://store.steampowered.com/app/6910/Deus_Ex_Game_of_the_Year_Edition/),
    for licensed product, developer/publisher, original date, English support
    and the official multiple-solution, skill, augmentation and inventory
    description.
  - **[P2]** [official Steam-hosted manual](https://cdn.akamai.steamstatic.com/steam/apps/6910/manuals/manual.pdf?t=1700763294),
    for difficulty, character creation, skills, inventory, hotbar, body health,
    Goals/Notes, codes, movement, stealth, equipment, conversations, combat,
    ammunition, healing, lockpicks, multitools and transport.
- Secondary and reproducible textual sources:
  - **[S1]** [SteamDB app/depot record](https://steamdb.info/app/6910/depots/),
    for current public Build `251801`, its 2014-05-01 build date and depot
    `6911`; these distribution observations do not define mechanics.
  - **[S2]** [Deus Ex Wiki Training reference](https://deusex.fandom.com/wiki/Training),
    for the three map segments, exact mandatory training demonstrations,
    stealth reset and alternative final-test solutions.
  - **[S3]** [Deus Ex Wiki Liberty Island reference](https://deusex.fandom.com/wiki/Deus_Ex_1st_Mission:_Liberty_Island),
    for objective order, map segments, front/rear entry, surrender, HQ and
    Battery Park terminal.
  - **[S4]** [GameChronicles written walkthrough](https://gamechronicles.com/guides/deusex/deusex.pdf),
    for an independent Mission 1 route, credentials, stealth/combat
    alternatives, commander conversation, HQ sequence and boat handoff.
- Reproducible control: **[V1]** repository-side transition reconstruction over
  the declared skill build, Training gates, Liberty route, mission handoff and
  save/reload snapshot. It does not execute Deus Ex.
- Claim IDs: `DX-001`–`DX-011`.

## Mechanical decomposition

### Action Genes

- `ACT-008`: directly walk, run, jump, climb, swim and strafe J.C. through the
  Training, Liberty Island, HQ and successor entry geometry.
- `ACT-161`: aim and commit a current melee, projectile or firearm attack at an
  eligible target or destructible route object.
- `ACT-164`: select one carried compatible weapon or tool as the active item.
- `ACT-183`: reload the active magazine-fed weapon from compatible reserve.
- `ACT-191`: spend the fixed initial point budget to raise Computers,
  Electronics and Lockpicking to Trained before the campaign begins.
- `ACT-199`: take, drop or equip compatible world and carried items.
- `ACT-202`: change standing, crouched and lateral-lean configuration to alter
  clearance, exposure, view and emitted movement noise.
- `ACT-232`: promise Harley not to kill Leo and later select the commander
  response that produces surrender.
- `ACT-341`: read a datacube; use a door, key, keypad, terminal, multitool,
  lockpick, button, medbot or transport when its current prerequisites permit.
- `ACT-424`: reposition fixed-orientation multi-cell objects within the
  thirty-cell inventory grid so their footprints leave legal space.
- Claims: `DX-002`–`DX-010`.

### System Behaviour Genes

- `SYS-057`: an eligible guard replaces patrol with investigation or pursuit
  after local sight or sound and may return when the cue is lost.
- `SYS-208`: a legal ranged attack resolves skill, focus, distance and hit
  location into miss or damage to a specific body region.
- `SYS-215`: movement, patrol, detection, interaction and combat resolve while
  the world advances in real time.
- `SYS-369`: death or explicit load replaces the current transient world with
  a retained manual or automatic snapshot.
- `SYS-373`: partial local suspicion escalates through acquisition and shared
  alert into active search or combat.
- `SYS-379`: primary objectives and consequential conversations update retained
  mission flags and the next authored goal.
- `SYS-780`: Mission 1 settlement carries build, inventory and flags through
  the boat transition into first Battery Park control.
- Resolution order: current input changes pose, movement, item, dialogue or
  interaction intent; local simulation advances; perception may update
  suspicion and hostility; legal attack or tool use spends its resource and
  resolves; injury updates body-region performance; required goal changes
  mission state; boat settlement instantiates Battery Park; save/load restores
  the recorded successor snapshot.
- Claims: `DX-005`–`DX-010`.

### Constraint Genes

- `CON-210`: compatible stacks and available cells bound each inventory
  transfer; excess remains in the world.
- `CON-282`: Training gates, commander contact, HQ reports, briefing and boat
  boarding require their authored predecessors.
- `CON-285`: firing and reloading require a compatible readied weapon,
  ammunition class, magazine and current action state.
- `CON-296`: a protected fixture admits only its matching nanokey, code,
  credentials or legal bypass unless a destructible alternative is used.
- `CON-304`: arm, leg, head and torso damage can impair aim, running or jumping
  or end the attempt at the lethal regional threshold.
- `CON-322`: a skill rank accepts allocation only with enough unspent points
  and an eligible next level.
- `CON-394`: a carried item must fit its fixed rectangular footprint into free
  inventory cells or its compatible stack/equipment state.
- Claims: `DX-003`–`DX-007`, `DX-009`.

### Information Genes

- `INF-073`: the hotbar, held model and inventory expose active equipment,
  carried weapons and current ammunition.
- `INF-115`: first-person sight, sound, actor motion and attack feedback expose
  only locally available opponent state.
- `INF-119`: the body diagram, bioenergy and Skills screens expose regional
  health, current points, ranks and build modifiers.
- `INF-125`: Goals/Notes and map surfaces expose current primary/secondary
  requirements, learned codes and explored route information.
- `INF-128`: focus labels and inventory reveal reachable item identity,
  compatibility, stack and remaining carrying space.
- `INF-148`: important conversations expose the currently offered responses
  without revealing every future consequence.
- `INF-302`: the inventory grid exposes item footprints and free cells before
  relocation or pickup.
- Claims: `DX-003`–`DX-009`.

### Objective Genes

- `OBJ-155`: complete Training, survive Mission 1's ordered mandatory gates,
  accept the Liberty Island-to-Battery Park settlement and retain ordinary
  first successor control through one save/reload check.
- Claims: `DX-002`, `DX-008`–`DX-010`.

### Time Genes

- `TIM-003`: traversal, patrol, suspicion, combat, tools and damage advance on
  the live mission clock outside paused information screens and conversations.
- `TIM-007`: a loaded save restores an earlier recorded state and permits a
  replacement movement, dialogue or combat continuation.
- Claims: `DX-006`, `DX-007`, `DX-010`.

## Reproducible transitions

| Before | Action | Deterministic or bounded resolution | Establishes | Claim |
|---|---|---|---|---|
| Fresh Training general room | follow the key, lockpick, code and multitool exercises | each addressed barrier accepts its demonstrated authority or consumable bypass before opening | access vocabulary | `DX-002`, `DX-005` |
| Covert Training guard has no completed acquisition | crouch and move outside strong sight/noise exposure | the player can reach the exit without alarm; completed detection closes it until reset | stealth threshold | `DX-002`, `DX-006` |
| Final Training test is active | choose one documented bridge, object, bypass, avoidance or destruction route | one legal route reaches the far side and the final conversation settles Training | multiple solutions | `DX-002` |
| New Game character screen has `5000` points | buy Trained Computers, Electronics and Lockpicking | `4725` points are committed, `275` remain and Trained Pistols is retained | fixed build | `DX-003` |
| A multi-cell item blocks another pickup | drag it to fitting free cells or drop another item | only a non-overlapping fixed footprint is accepted; legal free space changes | spatial inventory | `DX-004` |
| Harley's response set is active | promise not to kill Leo | the conversation grants the Statue-door key and records the route fact | consequential dialogue | `DX-008` |
| Front route terminal is reachable and credentials are known | enter `NSF001` / `smashthestate` and commit an available security operation | authorised functions become usable without spending a multitool | credentialed access | `DX-005` |
| A guard has not fully detected J.C. | remain crouched, distant and occluded or attack | low exposure may preserve stealth; visible/noisy harm can escalate to alert and combat | stealth/loud branch | `DX-006` |
| A loaded firearm is active | hold aim, fire and later reload | skill, focus, range and body region bound the hit; compatible reserve restores the magazine | live regional combat | `DX-007` |
| Leo Gold conversation begins | select the surrender response | Leo becomes non-hostile, the primary threat goal settles and UNATCO takes the island | dialogue mission result | `DX-008` |
| Manderley's second briefing is complete | return south and use the police boat | Mission 1 closes and first Battery Park control is instantiated | positive terminal | `DX-009` |
| Battery Park is controllable | save, change local state, then load | the saved build, inventory, position and mission state replace the changed continuation | retained successor | `DX-010` |

## Strategic and experiential structure

- Local decision: compare line of sight, noise, tool cost, ammunition, body
  condition and inventory space before using violence, stealth or access.
- Medium-term planning: preserve enough cells, lockpicks, multitools and rounds
  while converting facts and conversations into cheaper routes.
- Long-term structure: a chosen build changes the efficiency or availability
  of later actions, but one mission result remains reachable through distinct
  tactical routes.
- Common heuristics: search datacubes before spending bypass tools; crouch in
  shadow and control distance; wait for firearm focus; keep inventory space for
  route-critical items; prefer a key or credential before forced entry.
- Failure attribution: body and ammunition displays separate injury/resource
  failure from perception pressure, while Goals/Notes separates route
  uncertainty from an unsatisfied predecessor.
- Player-trust factors: exact Steam target, explicit fixed build, fixed route,
  optional-module exclusions and no-direct-play disclosure prevent later-game
  systems or mod behaviour from entering the signature.
- Claims: `DX-003`–`DX-011`.

## Replay and variation

- Change the initial skill allocation, Paul's offered weapon, Statue entry,
  hostile treatment, credential/tool use and commander response while keeping
  the same required mission terminal.
- Manual saves make alternate local continuations possible; this packet checks
  only one Battery Park retention point and does not treat every branch as a
  separate genome.
- Optional exploration areas, Gunther, aug installation and HQ visits can form
  later modules if separately bounded and evidenced.

## Adjacent systems and history

- The packet joins role-playing build allocation, grid inventory, authored
  dialogue, first-person stealth and live combat without inferring a genre gene.
- Training is included because it causally demonstrates the same reusable
  access and stealth vocabulary; its transient state remains separate from New
  Game campaign state.
- The current Steam product retains the original Windows GOTY content, but a
  current distribution identifier is not a claim that every historical retail
  binary or port is mechanically identical.

## Normalised genome

`ACT-008,ACT-161,ACT-164,ACT-183,ACT-191,ACT-199,ACT-202,ACT-232,ACT-341,ACT-424; SYS-057,SYS-208,SYS-215,SYS-369,SYS-373,SYS-379,SYS-780; CON-210,CON-282,CON-285,CON-296,CON-304,CON-322,CON-394; INF-073,INF-115,INF-119,INF-125,INF-128,INF-148,INF-302; OBJ-155; TIM-003,TIM-007`

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `352` (`GAME-0001`–`GAME-0352`).
- Exact genome matches: none.
- Tied near matches: `GAME-0260` — Metro Exodus (`24 / 48 = 0.500000`).
- Supported combination subsets: none.
- Scan date: 2026-09-22.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0260` — Metro Exodus | `ACT-008`, `ACT-161`, `ACT-164`, `ACT-183`, `ACT-199`, `ACT-202`, `ACT-341`, `SYS-057`, `SYS-208`, `SYS-215`, `SYS-369`, `SYS-373`, `SYS-780`, `CON-210`, `CON-282`, `CON-285`, `INF-073`, `INF-115`, `INF-119`, `INF-125`, `INF-128`, `OBJ-155`, `TIM-003`, `TIM-007` | Both packets combine direct first-person traversal, aiming, weapon selection, reload, grid- or slot-bounded equipment, crouched exposure, perception escalation, live regional combat, ordered mission gates, visible build/resources and branchable retention. Deus Ex adds allocable skills, authored dialogue, codes/keys/bypass tools, explicit item-grid rearrangement and a conversation-settled commander, while Metro Exodus adds its own mask, filter, workbench and journey systems. | Near, `24 / 48 = 0.500000` |

## Taxonomy impact

- Reuses `34` existing Active genes; creates no definition, combination or
  family.
- `ACT-424` and `CON-394` already cover fixed-orientation multi-cell inventory
  placement; rotation permission is a parameter and is false here.
- `SYS-208` plus `CON-304` already separate regional hit resolution from the
  movement/aim consequences of current body state.

## Negative results

- No “immersive sim”, “multiple solutions”, “augmentation”, “nanotechnology”
  or “first-person RPG” genre/content gene is created.
- Lockpick and multitool use are contextual consumable bypasses, not Skyrim's
  continuous angular lock-probing `ACT-344`.
- Codes do not use `CON-159`: they are entered in the current mission and are
  not retained knowledge across a reset loop.
- Training and Mission 1 do not establish activity-earned skill experience,
  so `SYS-342` is rejected; points are awarded and deliberately allocated.
- Optional SATCOM, Gunther, aug installation and weapon modification do not
  enter the complete signature.

## Delta summary

- New game: `GAME-0353`.
- Existing-gene usages added: `34`.
- New genes, combinations and families: `0`.

## New facts

- One source-bounded Training + Mission 1 packet now demonstrates how a fixed
  technical build, finite bypass resources, codes, conversation and physical
  topology converge on one retained mission handoff.
- The fixed route proves that a nonviolent commander result can follow a
  mixed stealth/combat approach without requiring total clearance.

## New genes

- None.

## New combinations

- None.

## Taxonomy changes

- None.

## New questions

- How does a later mission change when augmentation installation and stronger
  retained dialogue consequences are admitted?
- Which current packet best isolates the difference between known credentials,
  consumable electronic bypass and Computer-skill hacking?

## Next recommended game

- `GAME-0354` — *Super Mario World*, original North American English Super NES
  ruleset, one fresh `Yoshi's Island 2` course to its Goal Tape.

## Why this game

It adds a recognisable systemic-infiltration packet where skills, inventory,
facts, dialogue and live space are alternative resources for the same authored
mission rather than independent feature lists.
