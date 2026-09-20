---
game_id: GAME-0331
slug: starfield
game_title: Starfield
analysis_status: reviewed
reviewed: 2026-09-21
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-122
    - ACT-161
    - ACT-199
    - ACT-210
    - ACT-232
    - ACT-341
    - ACT-392
    - ACT-393
    - ACT-481
    - ACT-482
  system:
    - SYS-045
    - SYS-215
    - SYS-578
    - SYS-723
    - SYS-724
    - SYS-736
    - SYS-940
    - SYS-941
  constraint:
    - CON-282
    - CON-284
    - CON-364
    - CON-651
  information:
    - INF-073
    - INF-081
    - INF-115
    - INF-119
    - INF-125
    - INF-128
    - INF-148
    - INF-277
    - INF-360
  objective:
    - OBJ-155
  time:
    - TIM-003
---

# Game: Starfield

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Vectera, Kreet,
Jemison, New Atlantis, Frontier, Constellation, Artifact, Vasco and named
mission objectives are carrier parameters, not gene names.

## Analysis scope

- Version / ruleset: current official English Xbox Series X|S Standard Edition
  base game, fresh New Game on default `Normal` difficulty, from the first
  ordinary control after the Vectera mine elevator through complete settlement
  of the first main mission `One Small Step`. Exact installed build, console
  firmware and account entitlement were not observed.
- Structured analysis target: licensed Xbox Series X|S Standard Edition; see
  `GAME-0331` in
  [`knowledge/platforms/games.json`](../../platforms/games.json).
- Entry: first ordinary control after emerging from the Vectera mine elevator,
  before following Supervisor Lin to the Cutter lesson.
- Primary decision loop: read the tracked objective and local prompts; move,
  interact, mine or equip the required item; aim and fight when pirates block
  the route; satisfy the current tutorial predicate; in the Frontier read
  cockpit power, target, shield and hull state, steer and fight, then select a
  legal starmap destination; on Kreet optionally record one eligible local
  survey sample, traverse the Research Base and resolve the captain by dialogue
  or combat; return to the ship, grav jump to Jemison, land at New Atlantis,
  follow the NAT route to the Lodge, place the Artifact and finish the handoff.
- Positive terminal: after the Artifact is added to Constellation's collection,
  the final conversation with Sarah settles `One Small Step`, awards its mission
  result and leaves ordinary Lodge control with `The Old Neighborhood` available.
  The successor mission itself does not begin.
- Included: Cutter extraction; mandatory character background and optional
  compatible traits; equipment and mass-bounded inventory; direct ground
  locomotion, interaction, shooting and autonomous hostiles; health; contextual
  dialogue; ordered tutorial/quest predicates; one Kreet flora, fauna or mineral
  sample; direct Frontier throttle/pitch/yaw/roll; shared ship power; cockpit
  information; non-directional ship shields before hull; starmap route command;
  Vectera–Kreet–Jemison transfer; New Atlantis landing; NAT; Lodge and Artifact.
- Reproducible parameterisation: choose any one background and either zero or a
  legal set of up to three traits; retain the fresh default ship and mission
  equipment; satisfy every tracked objective in order. On Kreet, activate the
  hand scanner and record one eligible visible sample before entering the final
  Research Base approach. Persuade or fight the Crimson Fleet captain; both
  branches must rejoin the required return-to-ship state. Exact appearance,
  name, pronouns, optional loot, combat contacts, dialogue phrasing and scanned
  target class are parameters.
- Excluded: later main missions; Constellation companion systems beyond the
  handoff; arbitrary New Atlantis or planetary exploration; complete surveys;
  outposts; research, crafting and modification; ship building, purchase or
  upgrades; skill levelling after entry; factions; romance; crimes; New Game
  Plus; Shattered Space; Creations, mods and console commands; exact damage,
  economy, performance or patch-history claims; Windows, cloud and later ports.
- Potential scoped modules: one later Constellation mission, one complete
  planetary survey, one outpost packet, one ship-design packet and New Game Plus
  each require independent version, entry, loop, evidence and terminal.
- Direct-play status: not conducted. No console, entitlement, installed build,
  controller trace, save, screenshot, video or audio was used. Xbox and Bethesda
  establish product identity, controls, character creation, scanning, travel,
  ship combat and the exact official mission objective chain; two independent
  written routes corroborate the ordered handoff. This is source-bounded rules
  reconstruction, not a claimed playthrough or patch test.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `STARF-001` | The packet is the current Xbox Series console Standard Edition base game, released 2023-09-06 by Bethesda Game Studios/Bethesda Softworks | Confirmed | Direct | High | P1 |
| `STARF-002` | `One Small Step` runs from Vectera through Kreet and Jemison to the Lodge, then placing the Artifact and speaking with Sarah completes it | Confirmed | Direct | High | P2 |
| `STARF-003` | The mission requires Cutter mining, character creation, helmet equipment, pirate combat, Frontier flight lessons and starmap travel | Confirmed | Direct | High | P2, P3 |
| `STARF-004` | A background grants starting skills and up to three compatible optional traits add benefits and costs | Confirmed | Direct | High | P8, P9 |
| `STARF-005` | The hand scanner marks eligible flora, fauna and mineral targets and accepted samples advance retained survey percentage | Confirmed | Direct | High | P10, P11 |
| `STARF-006` | Frontier flight uses direct attitude/throttle controls and a finite power budget across live engines, shields, weapons and grav drive | Confirmed | Direct | High | P3, P4, P5 |
| `STARF-007` | Ship shields receive hostile damage before hull and cockpit surfaces expose live ship/target state | Confirmed | Direct | High | P3, P4 |
| `STARF-008` | A legal selected route can enter orbit or a landing state; combat, reach, grav power and route conditions gate travel | Confirmed | Direct | High | P5, P6, P7 |
| `STARF-009` | The Kreet captain can be persuaded or fought and both routes rejoin return-to-ship progression | Confirmed | Direct | High | P2, S1, S2 |
| `STARF-010` | The repository trace reaches ordinary Lodge successor control without importing later systems | Observation | Direct | High | V1 |

## Basic data

- Release / origin: Bethesda Game Studios / Bethesda Softworks; Xbox Series X|S
  and Windows base-game release 2023-09-06.
- Platform or physical form: licensed Xbox Series X|S Standard Edition base
  game, single-player fresh New Game packet.
- Puzzle family: embodied spatial reasoning; inventory and equipment state;
  tactical forecast and counterplay; ordered dependency sequencing; knowledge
  and evidence progression; real-time system pressure.
- Primary and official sources, accessed 2026-09-21:
  - **[P1]** [official Xbox Starfield page](https://www.xbox.com/en-US/games/starfield),
    for Standard Edition identity, Xbox Series X|S platform, developer,
    publisher, release and Constellation/Artifact premise.
  - **[P2]** [Bethesda `One Small Step` mission support](https://help.bethesda.net/app/answers/detail/a_id/60739/~/one-small-step---main-mission---starfield),
    for locations, objective order, Cutter, character creation, equipment,
    pirates, ship tutorial, Kreet captain, scanner return, grav jump, NAT,
    Lodge, Artifact placement and completion.
  - **[P3]** [Bethesda Xbox controls](https://help.bethesda.net/app/answers/detail/a_id/60723/),
    for ground, scanner, ship, targeting, weapon, power and starmap controls.
  - **[P4]** [Bethesda starship combat](https://help.bethesda.net/app/answers/detail/a_id/60885/),
    for power allocation, weapons, targeting, shields and hull.
  - **[P5]** [Bethesda grav-drive guide](https://help.bethesda.net/app/answers/detail/a_id/60821/),
    for GRV power, activation time, fuel and jump range.
  - **[P6]** [Bethesda fast-travel guide](https://help.bethesda.net/app/answers/detail/a_id/60960/),
    for starmap, scanner, quest destinations and combat restrictions.
  - **[P7]** [Bethesda starmap guide](https://help.bethesda.net/app/answers/detail/a_id/61656/),
    for system, planet, orbit, resource and course surfaces.
  - **[P8]** [Bethesda character creation guide](https://help.bethesda.net/app/answers/detail/a_id/61027/),
    for background, optional traits, incompatibilities, name and pronouns.
  - **[P9]** [Bethesda background guide](https://help.bethesda.net/app/answers/detail/a_id/61069/),
    for the three starting rank-one skills supplied by each background.
  - **[P10]** [Bethesda scanning guide](https://help.bethesda.net/app/answers/detail/a_id/60950/),
    for eligible targets, sample input and retained survey percentage.
  - **[P11]** [Bethesda resource-gathering guide](https://help.bethesda.net/app/answers/detail/a_id/61082/),
    for Cutter extraction and scanner-supported local resources.
  - **[P12]** [Bethesda inventory guide](https://help.bethesda.net/app/answers/detail/a_id/61042/),
    for mass capacity, equipment, cargo and quickslots.
- Corroborating textual sources, accessed 2026-09-21:
  - **[S1]** [PowerPyx `One Small Step` route](https://www.powerpyx.com/starfield-one-small-step-walkthrough/),
    for an independent complete ordered mission route.
  - **[S2]** [Game8 `One Small Step` route](https://game8.co/games/Starfield/archives/422742),
    for independent captain-branch and Lodge-terminal corroboration.
  - **[V1]** repository-side transition trace from P1–P12 and S1–S2; rules
    reasoning, not direct play.
- Claim IDs: `STARF-001`–`STARF-010`. No audiovisual evidence was used.

## Mechanical decomposition

### Action Genes

- `ACT-008`: walk, run and jump through Vectera, Kreet, New Atlantis and Lodge.
- `ACT-122`: hold the Cutter on the required mine deposit until material enters inventory.
- Revised `ACT-210`: select one background and zero to three compatible traits.
- `ACT-199`: collect and equip the required helmet, weapons and carried items.
- `ACT-161`: aim and fire at reachable ground or ship hostiles.
- `ACT-232`: commit a currently offered response, including the captain branch.
- `ACT-341`: use doors, seats, NAT, Lodge fixture and Artifact collection.
- `ACT-392`: directly command Frontier throttle, pitch, yaw and roll.
- Revised `ACT-393`: move finite ship power among live subsystems.
- New `ACT-481`: scan one eligible Kreet target for retained survey evidence.
- New `ACT-482`: select and commit Vectera/Kreet/Jemison/orbit/landing routes.
- Claims: `STARF-002`–`STARF-009`.

### System Behaviour Genes

- `SYS-045`, `SYS-215` and `SYS-578`: hostile agents move and fight in real
  time while damage and recovery update one continuous personal health pool.
- Revised `SYS-723` and `SYS-724`: direct craft motion and collision coexist
  with subsystem performance produced by the current finite power split.
- `SYS-736`: each tutorial or mission predicate retains its stage until
  satisfied, then records it and exposes the next instruction.
- New `SYS-940`: hostile ship damage crosses undirected shields before hull.
- New `SYS-941`: a legal selected route transfers persistent ship, inventory
  and mission state into the chosen orbital or landing successor.
- Resolution order: validate current tutorial/action state; resolve movement,
  interaction or live combat; update health, inventory, survey, ship or quest
  state; expose the next predicate; transfer to a legal destination when
  committed; settle the Artifact handoff and mission terminal.
- Claims: `STARF-002`, `STARF-003`, `STARF-005`–`STARF-010`.

### Constraint Genes

- `CON-282`: authored mission predecessors gate every later encounter and handoff.
- `CON-284`: carried mass and compatible equipment slots bound item transfer.
- Revised `CON-364`: live hostile state blocks travel; discovered or explicitly
  offered mission destinations can be eligible.
- New `CON-651`: intersystem travel additionally requires a reachable target
  and compatible grav-drive power, range and fuel state.
- Claims: `STARF-002`, `STARF-003`, `STARF-008`.

### Information Genes

- `INF-073`, `INF-119` and `INF-128`: HUD and inventory expose active equipment,
  ammunition, health, build, item identity, mass and compatibility.
- `INF-115`: local sight and sound expose only currently perceivable hostiles.
- `INF-125`: tracked objectives and discovered route state expose the current gate.
- `INF-148`: conversation surfaces expose currently available responses.
- `INF-081`: starmap surfaces expose known stars, planets, routes and properties.
- Revised `INF-277`: Frontier cockpit exposes applicable power, shield, hull,
  weapon, target, objective and threat state.
- New `INF-360`: the hand scanner exposes eligible target class, accepted sample
  and retained survey progress without revealing unseen targets.
- Claims: `STARF-003`–`STARF-009`.

### Objective and Time Genes

- `OBJ-155`: survive and complete the bounded authored mission, accept its
  explicit settlement and retain ordinary control in the immediate successor.
- `TIM-003`: ground and ship combat, movement, targeting and damage continue in
  real time while local commands are accepted.
- Claims: `STARF-002`, `STARF-006`, `STARF-009`, `STARF-010`.

## Reproducible transitions

| Before | Action | Deterministic or bounded resolution | Establishes | Claim |
|---|---|---|---|---|
| Fresh default New Game reaches mine exit | follow Lin, use Cutter and touch the Artifact | mandatory extraction and vision advance to character creation | exact entry chain | `STARF-002`, `STARF-003` |
| Character creation is active | select one background and legal optional traits | starting skills/modifiers persist into ordinary control | background boundary | `STARF-004` |
| Helmet and weapon are available | transfer/equip them and repel the pirates | equipment state and live combat clear the Vectera gate | inventory/combat | `STARF-002`, `STARF-003` |
| Frontier tutorial is active | pilot, target, fire and reallocate power | motion, ship combat, shields/hull and power feedback resolve live | craft loop | `STARF-006`, `STARF-007` |
| Kreet is eligible | commit the starmap route and landing target | ship and mission state arrive at Kreet | selected ship travel | `STARF-008` |
| Eligible local target is in scanner range | record one sample | class/location survey percentage retains progress | local survey | `STARF-005` |
| Captain confrontation is reached | persuade or fight | either legal branch clears the same return-to-ship predicate | authored branch/rejoin | `STARF-009` |
| Jemison route is offered and GRV is powered | commit grav route, New Atlantis landing and NAT/Lodge route | persistent state reaches the Lodge | route legality/retention | `STARF-008` |
| Artifact collection is reachable | place the Artifact and finish Sarah's conversation | `One Small Step` settles and successor control remains | positive terminal | `STARF-002`, `STARF-010` |

## Edge-case audit

- `ACT-481` is not `ACT-313`: Starfield accepts an addressed sample and updates
  class survey progress; it does not require holding a scanner on one fragment
  until a blueprint-analysis bar completes.
- `ACT-482` is not direct craft control (`ACT-392`) or avatar travel. It commits
  one map-selected celestial/landing route whose resolution is `SYS-941`.
- `SYS-940` is not directional `SYS-725` and not personal shield/downed
  `SYS-348`: no front/rear transfer or revival layer is claimed.
- `CON-651` differs from destination eligibility in `CON-364`: one governs live
  hostile/discovery gates, the other the ship's drive/power/range feasibility.
- Character appearance, name and pronouns do not enter `ACT-210`; only the
  mechanically persistent background and compatible traits do.
- The optional single Kreet sample is made reproducible but complete survey is
  excluded and is not required for mission settlement.

## Strategic and experiential structure

- Local decision: distinguish a tracked interaction, a scan sample and a live
  threat, then commit the tool, weapon, response or movement it currently needs.
- Medium-term planning: preserve compatible equipment and carrying mass while
  moving one persistent character and ship state through Vectera and Kreet.
- Long-term structure: turn the first Artifact contact into character identity,
  ship authority, legal celestial travel and Constellation admission.
- Failure attribution: personal health, ship shield/hull, power channels,
  target state, survey feedback and current objective keep ground, flight,
  travel and mission errors distinguishable.
- Player trust: every required predicate must expose its completion before the
  next one, and either captain branch must rejoin the same return route.

## Replay and variation

- Background, legal trait set, appearance, name, pronouns, ground route, loot,
  scanned target, combat contacts, power distribution and captain resolution
  may vary. Required objective order, destinations, Artifact handoff and
  terminal remain fixed.
- Optional loot and survey progress may change carried state but do not replace
  the mission terminal. A future build that materially changes the first
  mission's route, power model or completion requires review.

## Adjacent systems and history

- *STAR WARS: Squadrons* shares direct six-degree flight, live craft power,
  cockpit targets and real-time ship combat. Its fixed X-wing has three power
  channels, directional shields and countermeasures; Starfield couples a wider
  Frontier subsystem set to selected interplanetary travel and ground play.
- *No Man's Sky* shares local survey, ship travel and staged onboarding. Its
  generated Awakenings packet centres survival recharge, production and a
  resource pulse; this authored mission centres background creation, combat,
  non-directional ship defence and one Constellation handoff.
- *Cyberpunk 2077* shares equipment mass, aimed combat, dialogue gates, mission
  tracking and character build state, but has no directly piloted spacecraft or
  selected grav-route transition in its analysed packet.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-122`, `ACT-161`, `ACT-199`, `ACT-210`, `ACT-232`, `ACT-341`, `ACT-392`, `ACT-393`, `ACT-481`, `ACT-482` | route, background, sample, craft target and destination |
| System Behaviour | `SYS-045`, `SYS-215`, `SYS-578`, `SYS-723`, `SYS-724`, `SYS-736`, `SYS-940`, `SYS-941` | hostile, health, craft motion, power, shields, tutorial and transfer |
| Constraint | `CON-282`, `CON-284`, `CON-364`, `CON-651` | order, mass, combat lock, drive power and range |
| Information | `INF-073`, `INF-081`, `INF-115`, `INF-119`, `INF-125`, `INF-128`, `INF-148`, `INF-277`, `INF-360` | equipment, map, local state, dialogue, cockpit and survey |
| Objective | `OBJ-155` | explicit first-mission completion and successor control |
| Time | `TIM-003` | live ground and ship clock |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `330` (`GAME-0001`–`GAME-0330`).
- Exact genome matches: none.
- Tied near matches: `GAME-0231` — Fallout 4 (`13 / 43 = 0.302326`).
- Supported combination subsets: none.
- Scan date: 2026-09-21.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0231` — Fallout 4 | `ACT-008`, `ACT-161`, `ACT-199`, `ACT-232`, `ACT-341`, `SYS-215`, `SYS-736`, `CON-282`, `INF-115`, `INF-119`, `INF-125`, `INF-128`, `TIM-003` | Both open Bethesda RPGs through an authored first-person character, equipment, dialogue, combat and tutorial route. Fallout 4 centres S.P.E.C.I.A.L., Vault escape, checkpoint/reload and retained manual save; Starfield adds Cutter extraction, background/traits, local survey, directly controlled ship flight, live craft power, shield/hull and selected grav travel before its Lodge handoff. | Near, `13 / 43 = 0.302326` |

### Preserved research notes

- Classification result: `New genes`; no verified combination is expected.
- Evidence and reasoning: established embodied, inventory, dialogue, mission and
  flight boundaries transfer. Local sampling, selected ship travel, undirected
  ship defence and grav-route legality remain separate causal transitions.

## Taxonomy impact

- Registry changes: add six Active boundaries and Starfield support to
  twenty-eight established boundaries.
- Taxonomy change: `TAXONOMY_CHANGE_075` generalises six first-carrier wordings
  without changing any earlier signature or lifecycle.
- Candidate terms affected: all names, mission labels, equipment and celestial
  locations remain carrier parameters.

## Negative results

- No Xbox console, entitlement, installed build, direct play, save, screenshot,
  video or audio evidence exists for this unit.
- No exact damage, fuel quantity, jump range, survey threshold, reload timing,
  patch behaviour, frame rate or platform parity is asserted.
- The optional one-sample route does not establish a complete Kreet survey.
- Later systems are excluded rather than inferred from whole-product marketing.

## Delta summary

## New facts

- [Confirmed | Direct | High] Official Xbox and Bethesda material establishes
  the product, control vocabulary, background/trait rules, survey, craft power,
  travel gates and complete mission objective chain (`STARF-001`–`STARF-008`).
- [Confirmed | Corroborated | High] Official and two independent written routes
  close the captain branch and Lodge terminal (`STARF-009`, `STARF-010`).

## New genes

- [Observation | Direct | High] `ACT-481`, `ACT-482`, `SYS-940`, `SYS-941`,
  `CON-651` and `INF-360` isolate the local sample, selected ship route,
  undirected shield/hull, retained arrival, grav eligibility and scanner display.

## New combinations

- [Observation | Corroborated | High] No new verified combination.

## Taxonomy changes

- [Observation | Corroborated | High] `TAXONOMY_CHANGE_075` generalises
  `ACT-210`, `ACT-393`, `SYS-723`, `SYS-724`, `CON-364` and `INF-277` after a
  complete lower-carrier transfer test; earlier signatures remain unchanged.

## New questions

- Which exact scanner sample counts and target regeneration rules hold across
  every current Xbox patch?
- Which ship state fields survive every optional detour between Kreet and Lodge?

## Next recommended game

- [Hypothesis | Limited | High] `GAME-0332` *Heroes of Might and Magic III:
  Complete* is the next reserved audience-recognition unit.
- Optimisation criterion: replace a first-person space onboarding route with a
  turn-based strategic army-and-map packet.
- Backlog impact: completes 7/9 of the current fixed horizon.

## Why this game

- [Hypothesis | Limited | High] Starfield is a recognisable modern space-RPG
  anchor whose first mission directly joins character, ground and ship state.

## Completion checklist

- [x] exact product, entry, terminal and exclusions declared
- [x] official mechanics separated from corroborating route evidence
- [x] local survey, ship travel and shield/hull boundaries separated
- [x] exact/near scan and selected-neighbour interpretation regenerated
- [x] Ukrainian, platform, presentation, artwork and validation accepted

## Search-demand continuation

- [Hypothesis | Limited | High] `GAME-0332` *Heroes of Might and Magic III:
  Complete* is the next reserved unit through the active Goal continuation.
