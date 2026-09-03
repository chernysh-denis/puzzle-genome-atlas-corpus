---
game_id: GAME-0237
slug: serious-sam-hd-the-first-encounter
game_title: "Serious Sam HD: The First Encounter"
analysis_status: reviewed
reviewed: 2026-09-03
combination_ids:
  - COMB-0235
gene_ids:
  action:
    - ACT-008
    - ACT-161
    - ACT-164
  system:
    - SYS-215
    - SYS-222
    - SYS-749
  constraint:
    - CON-402
    - CON-578
  information:
    - INF-073
    - INF-115
    - INF-119
  objective:
    - OBJ-026
  time:
    - TIM-003
---

# Game: Serious Sam HD: The First Encounter

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Parameters describe
gene instances but do not enter the signature.

## Analysis scope

- Version / ruleset: current unmodified English Windows Steam application
  `41000`, public Build ID `5820849`, built and published 2020-11-12 and checked
  2026-09-03. Only the 2009 HD remake's base single-player campaign on `Normal`
  difficulty is admitted; no executable-version string is inferred from the
  distribution build.
- Entry: begin an ordinary single-player `Normal` campaign, complete the first
  Hatshepsut level without secrets or optional weapons, cross its authored exit
  and retain the resulting Sand Canyon level-start save. The packet begins at
  first direct control outside the Hatshepsut exit with the ordinary revolvers,
  pump-action shotgun and carried ammunition produced by that route.
- Primary decision loop: read the local canyon or room geometry, visible
  hostiles, projectiles, health, armour, active weapon and compatible
  ammunition; move, strafe and keep distance; select an owned weapon; aim and
  fire; cross or settle authored triggers that release finite hostile groups;
  collect compatible ammunition by contact; clear the mandatory Marsh-Hopper
  room so its exit opens; then survive the remaining route and enter the fixed
  tomb threshold.
- Positive terminal: cross the final temple threshold after the last canyon
  approach, allow the authored artefact transition to settle and reach the
  `Tomb of Ramses III` briefing/next-level state. The Sand Canyon exit, not an
  arbitrary pause after a fight, closes the packet.
- Negative terminal: health reaching zero ends the current attempt. Reload the
  retained Sand Canyon level-start save and repeat; the failed attempt's
  transient enemy, ammunition, health and position state is not admitted as a
  terminal or as persistent progression.
- Included: direct first-person movement, strafing and jump-capable traversal;
  aimed revolver and shotgun combat; weapon switching; unlimited default-
  revolver fire versus finite compatible shotgun ammunition; contact ammunition
  pickup; visible health, armour, weapon and ammunition state; local sight and
  projectile cues; the first-Kamikaze defeat releasing its authored rush;
  threshold-triggered Marsh-Hopper release; clearance-gated room exit; later
  fixed enemy groups; boulder avoidance on the mandatory right route; final
  tomb entry and next-level transition.
- Excluded: optional left fog room, boulder-ammunition detour, pickup-triggered
  flanking ambushes and all six secrets; secret Tommy Gun and every other
  optional weapon or item; alternate difficulties, manual difficulty modifiers
  and speedrun skips; Hatshepsut except as entry provenance, Tomb of Ramses III
  except as the terminal state and all other levels; co-op, deathmatch and every
  multiplayer mode; dedicated servers, leaderboards and achievements; Classic
  2001, HD: The Second Encounter, Fusion, VR, Gold Collection content, DLC,
  Workshop/mod content, consoles and the entire campaign or franchise.
- Reproducible parameterisation: use a clean English Windows install on the
  current public Steam branch, default mouse/keyboard bindings, single-player
  `Normal`, no mods and no cheats. Reach Sand Canyon through the ordinary first
  level without secrets; use its retained start as the retry origin. Collect
  the exposed entry shells, defeat the first charging Kamikaze so the authored
  rush resolves, keep distance and spend either finite shotgun shells or the
  unlimited revolvers, follow the mandatory right route, clear every released
  Marsh-Hopper until the door opens, then cross the remaining authored route and
  enter the final tomb. Exact aim, weapon timing, damage, armour, ammunition,
  enemy positions and completion time are run parameters.
- Potential scoped modules: Hatshepsut as a separate pickup-triggered tutorial;
  one later arena with several clearance gates; one named co-op level; Classic,
  Fusion or VR as independent products. None is imported here.
- Direct-play status: not conducted. Croteam's official factsheet, the current
  Steam product and official update stream establish the product, platform,
  mode separation, fifteen-level campaign and current supported branch. Three
  independent textual route sources establish the exact Sand Canyon entry,
  enemy triggers, finite groups, pickups, clearance gate and Tomb transition;
  the in-world NETRICSA transcript corroborates the Sand Canyon and successor
  briefings. The trace below is evidence-backed rules reconstruction, not a
  claimed captured playthrough. No video or audio was opened, played, heard,
  analysed or used.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `SSHD-001` | The admitted product is Croteam's 2009 HD remake for Windows, current Steam app `41000`, not the 2001 Classic game, The Second Encounter, Fusion or VR | Confirmed | Direct | High | P1, P2 |
| `SSHD-002` | The public Windows branch is Build ID `5820849`, built and published 2020-11-12, matching Croteam's latest TFE hotfix boundary | Confirmed | Corroborated | High | P3, S1 |
| `SSHD-003` | Single-player and up-to-sixteen-player co-op are distinct surfaces, and the base product exposes fifteen Egyptian levels | Confirmed | Direct | High | P1, P2 |
| `SSHD-004` | Sand Canyon is the second authored level, reached after Hatshepsut and followed by Tomb of Ramses III | Observation | Corroborated | High | S2, S3, S4 |
| `SSHD-005` | The bounded route uses direct first-person traversal, aimed fire, weapon selection and contact pickup of compatible ammunition | Observation | Corroborated | High | S2, S3, S5 |
| `SSHD-006` | Defeating the first charging Kamikaze releases an authored rush, while entering the large hall releases Marsh-Hoppers through its wall openings | Observation | Corroborated | High | S2, S3, S5 |
| `SSHD-007` | The mandatory hall's next door remains unavailable until every required Marsh-Hopper is cleared | Observation | Corroborated | High | S2, S3 |
| `SSHD-008` | Weapons differ in cadence, reach and compatible ammunition; carried ammunition is finite for consuming weapons while the default revolvers remain a lower-output fallback | Observation | Corroborated | Medium | S3, S5 |
| `SSHD-009` | Health, armour, active weapon, ammunition, visible attackers and incoming projectiles expose the immediate survival/resource state | Observation | Corroborated | High | S3, S5 |
| `SSHD-010` | Charging, rushing, leaping and ranged enemy behaviours make distance, lateral movement, target priority and ammunition choice consequential in real time | Observation | Corroborated | High | S2, S3, S5 |
| `SSHD-011` | Entering the final tomb triggers the authored artefact transition and hands control to the Tomb of Ramses III successor state | Observation | Corroborated | High | S3, S4, S5 |
| `SSHD-012` | The packet's transferable identity is a fixed route whose traversal and combat state fire finite enemy groups, including one clearance-gated swarm, under typed ammunition pressure | Strong Pattern | Corroborated | High | SSHD-004–SSHD-011 |

## Basic data

- Release / origin: Croteam; Devolver Digital; Windows release 2009-11-24;
  current Steam distribution checked 2026-09-03.
- Platform or physical form: authored single-player first-person action game;
  only one early level on the current Windows HD-remake branch.
- Puzzle family: tactical forecast and counterplay; real-time system pressure;
  world topology and perspective; ordered dependency sequencing.
- Primary and official sources:
  - **[P1]** [Croteam's official factsheet](https://www.croteam.com/press/sheet.php?p=serious_sam_HD_-_the_first_encounter),
    for developer, 2009 date, Steam platform, explicit HD-remake identity,
    single-player/16-player co-op separation, arsenal framing and fifteen
    levels.
  - **[P2]** [official Steam product page](https://store.steampowered.com/app/41000/Serious_Sam_HD_The_First_Encounter/),
    for current lawful Windows sale, app `41000`, single-player and separate
    network/local modes, release identity, engine and campaign features.
  - **[P3]** [official Steam/Croteam announcement stream](https://store.steampowered.com/oldnews/?appgroupname=Serious+Sam+HD%3A+The+First+Encounter&appids=41000&feed=steam_community_announcements&headlines=1),
    for the 2020-11-12 `SSHD TFE Hotfix` as the latest product-specific public
    update boundary and earlier distinct original-game updates.
- Secondary and reproducible textual sources:
  - **[S1]** [SteamDB depots](https://steamdb.info/app/41000/depots/), observed
    2026-09-03, for Windows support and public Build ID `5820849`, built and
    updated 2020-11-12. SteamDB identifies itself as unaffiliated with Valve.
  - **[S2]** [StrategyWiki Sand Canyon route](https://strategywiki.org/wiki/Serious_Sam:_The_First_Encounter/Sand_Canyon),
    for ordered level position, first-Kamikaze trigger, fixed hostile groups,
    mandatory Marsh-Hopper clearance, door opening and HD-specific notes.
  - **[S3]** [PortForward's text-and-image HD Sand Canyon walkthrough](https://portforward.com/games/walkthroughs/Serious-Sam-HD-The-First-Encounter/Sand-Canyon.htm),
    for exposed ammunition, charging/ranged threats, swarm release, boulder,
    clearance continuation and final tomb threshold. Only the text was read;
    its images were not used as artwork or evidence assets.
  - **[S4]** [GameFAQs NETRICSA transcript](https://gamefaqs.gamespot.com/pc/970127-serious-sam-hd-the-first-encounter/faqs/69469),
    for the in-game Sand Canyon instruction to enter the temple and the
    successor Tomb of Ramses III briefing.
  - **[S5]** [GameFAQs HD-hosted guide and walkthrough](https://gamefaqs.gamespot.com/pc/970127-serious-sam-hd-the-first-encounter/faqs/11084),
    for level order, direct controls, weapons, ammunition and the complete
    Sand Canyon-to-successor route; exact counts and higher difficulties are
    not promoted to canonical genes.
- Reproducible control: **[V1]** repository-side transition trace across
  `P1`–`P3` and `S1`–`S5` under the fixed app, build, difficulty, entry,
  mandatory-route and terminal contract; no direct-play or audiovisual claim.
- Claim IDs: `SSHD-001`–`SSHD-012`.

## Mechanical decomposition

### Action Genes

- Existing `ACT-008`: directly walk, strafe and jump through the canyon, rooms,
  hazards and final tomb threshold; `ACT-161`: aim and fire the current revolver
  or shotgun at a reachable hostile; `ACT-164`: switch the active owned weapon.
- New action genes: none. Exact movement bindings, revolver/shotgun identity,
  target priority and aim point are parameters.
- Claim IDs: `SSHD-005`, `SSHD-008`, `SSHD-010`.

### System Behaviour Genes

- Existing `SYS-215`: resolve the player's and hostile groups' simultaneous
  range-, cadence-, damage-, defence- and defeat-dependent combat in real time;
  `SYS-222`: transfer compatible exposed shells into the carried ammunition
  reserve on avatar contact.
- New `SYS-749`: a settled authored traversal, target-defeat or collection
  trigger releases its declared finite hostile group at fixed regions and
  routes it into the live encounter. The bounded trace uses the first-Kamikaze
  defeat and the mandatory Marsh-Hopper-room threshold; optional ambush pickups
  remain excluded.
- Resolution order: accept movement, weapon or attack input; validate current
  weapon and ammunition; resolve projectile, hostile movement and damage;
  settle contact pickups; when the relevant route/defeat trigger settles,
  instantiate its finite group; after every required Marsh-Hopper is defeated,
  open the next door; reaching the final tomb transfers to the successor.
- Claim IDs: `SSHD-005`–`SSHD-011`.

### Constraint Genes

- Existing `CON-402`: the mandatory Marsh-Hopper-room exit remains closed until
  every required current hostile and declared reinforcement is defeated.
- New `CON-578`: each ammunition-consuming owned weapon can fire only from its
  compatible finite reserve, while an eligible contact pickup refills that type
  only to its cap; the default unlimited revolvers remain a distinct fallback.
- Scarce strategic resources: health, armour, compatible shotgun ammunition,
  lateral space, distance from rushing enemies, safe projectile lanes and a
  clear path through the next threshold.
- Claim IDs: `SSHD-007`–`SSHD-010`.

### Information Genes

- Existing `INF-073`: the interface exposes active weapon and compatible
  ammunition; `INF-115`: avatar-centred visibility and explicit spatial effects
  expose local hostiles and projectiles rather than an omniscient level roster;
  `INF-119`: current health and armour are visible.
- Audio cues are not evidence for this unit. Exact HUD position, icon art,
  colours and numeric run values are presentation parameters.
- Claim IDs: `SSHD-008`–`SSHD-010`.

### Objective Genes

- Existing `OBJ-026`: traverse the now-connected authored route and reach the
  designated final tomb threshold that transfers to Tomb of Ramses III.
- Clearing the first rush or Marsh-Hopper room is intermediate; killing every
  optional enemy, finding secrets or completing all fifteen levels is not the
  terminal.
- Claim IDs: `SSHD-004`, `SSHD-007`, `SSHD-011`.

### Time Genes

- Existing `TIM-003`: hostile movement, charges, leaps, projectiles and damage
  advance continuously while the player moves, selects weapons and fires.
- Menus and loading do not create a second decision clock.
- Claim IDs: `SSHD-006`, `SSHD-008`–`SSHD-010`.

## Reproducible transitions

| Before | Action | Deterministic or bounded resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Ordinary `Normal` campaign has crossed the Hatshepsut exit without secrets | Load the retained Sand Canyon start and accept first control | The player begins outside the prior temple with the ordinary early arsenal and level-start state | fixed product, difficulty and entry | `SSHD-001`, `SSHD-004`, `SSHD-005` |
| Exposed compatible shells lie on the opening route below capacity | Walk through the pickup | The compatible finite reserve increases up to its cap without opening an inventory screen | spatial resupply precedes pressure | `SSHD-005`, `SSHD-008` |
| The first charging Kamikaze has entered the authored approach | Keep distance, aim and defeat it | The target leaves combat and its settled defeat releases the fixed rush from beyond the hill | target defeat is an encounter trigger | `SSHD-006`, `SSHD-010` |
| A finite-ammunition shotgun is active while the rush advances | Fire or switch to unlimited revolvers | A legal shot spends compatible shells and trades stopping power/cadence against remaining reserve; the fallback preserves a lower-output attack | ammunition type changes a live target-priority decision | `SSHD-008`, `SSHD-010` |
| The player crosses the large mandatory hall threshold | Continue into the room | Authored wall openings release a finite Marsh-Hopper group into the active space and the forward exit remains closed | traversal creates bounded swarm pressure | `SSHD-006`, `SSHD-007` |
| Required Marsh-Hoppers remain alive | Strafe, keep distance and defeat each one | Live movement, attacks, projectiles, health and ammunition resolve; partial clearance does not open the door | closed finite encounter set | `SSHD-007`, `SSHD-009`, `SSHD-010` |
| The final required Marsh-Hopper is defeated | Allow clearance to settle | The room changes to cleared and its forward door becomes traversable | clearance causally unlocks route continuation | `SSHD-007` |
| The mandatory right route exposes a rolling boulder or later hostile vector | Retreat, side-step or take a clear combat line | Collision or hostile damage is avoided or applied while the route remains live | geometry and motion remain decision-relevant | `SSHD-009`, `SSHD-010` |
| The final canyon approach is traversable | Survive the fixed group and enter the tomb | The artefact transition settles and the Tomb of Ramses III successor state loads | reproducible positive terminal | `SSHD-004`, `SSHD-011` |
| Health reaches zero before the tomb transition | Reload the retained Sand Canyon start | Transient position, health, ammunition and hostile state are replaced by the declared entry state | reproducible failed-attempt boundary | `SSHD-009`, `SSHD-011` |

## Strategic and experiential structure

- Planning horizon: preserve enough shotgun shells and lateral space for the
  next released group while recognising that an unlimited but slower fallback
  prevents finite ammunition from becoming a simple hard lock.
- Local tactics: retreat from charging threats, side-step predictable rushes,
  keep self-destructing enemies outside their damage radius, prioritise ranged
  attackers and avoid spending scarce shells where revolvers suffice.
- Medium-term structure: the route alternates open approach, narrow passage,
  threshold-triggered swarm, clearance gate and final canyon so the same
  movement-and-fire vocabulary changes meaning with geometry and group origin.
- Failure attribution: visible health, armour, ammunition, projectile paths and
  enemy approach vectors distinguish poor spacing, target priority and resource
  expenditure from a missed route gate.
- Player-trust factors: trigger outcomes are authored and repeatable under the
  same route; the closed door visibly opens after finite clearance; the named
  next-level transition gives an objective terminal.
- Claim IDs: `SSHD-005`–`SSHD-012`.

## Replay and variation

- What changes between attempts: aim, weapon choice, ammunition expenditure,
  pickup use, exact hostile positions, damage, armour and route timing.
- What remains fixed: build, `Normal`, authored geometry, trigger predicates,
  required Marsh-Hopper closure and the final tomb destination.
- Multiple viable strategies: cautious revolver conservation, earlier shotgun
  expenditure and mixed switching can all reach the same exit; secrets and
  nonmandatory detours are outside the comparison.
- Typical replay motive: improve distance control, group ordering, projectile
  avoidance and ammunition efficiency rather than change the level terminal.
- Claim IDs: `SSHD-006`–`SSHD-012`.

## Adjacent systems and history

- Direct predecessor: the 2001 Classic game's corresponding route is historical
  lineage, not an admitted executable or second ruleset.
- Variants: higher difficulties alter enemy pressure and parameters; co-op adds
  participants; Fusion, VR and The Second Encounter are distinct products.
- Similar games: Half-Life 2 shares authored first-person traversal, finite
  ammunition, local combat and a named level transition, but its reviewed
  Ravenholm packet makes physical-object repurposing central. Left 4 Dead 2
  shares a one-shot authored hostile population and bounded route, but combines
  it with adaptive Director populations, a four-Survivor party and collective
  safe-room closure. The Binding of Isaac: Rebirth shares clearance-gated
  rooms, but its room graph, random rewards and run build replace authored
  first-person trigger lines.
- Important difference: Sand Canyon repeatedly converts route or combat state
  into finite authored enemy groups, including a mandatory swarm whose complete
  clearance changes the route, while typed finite ammunition competes with an
  unlimited fallback before one fixed successor exit.
- Claim IDs: `SSHD-001`–`SSHD-012`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-161`, `ACT-164` | direct movement, aim/fire and weapon selection |
| System Behaviour | `SYS-215`, `SYS-222`, `SYS-749` | live combat, contact ammunition pickup and authored hostile release |
| Constraint | `CON-402`, `CON-578` | clearance-gated exit and typed finite ammunition |
| Information | `INF-073`, `INF-115`, `INF-119` | weapon/ammunition, local threats/projectiles and health/armour |
| Objective | `OBJ-026` | reach the Tomb of Ramses III successor threshold |
| Time | `TIM-003` | continuously advancing combat and route hazards |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `236` (`GAME-0001`–`GAME-0236`).
- Exact genome matches: none.
- Tied near matches: `GAME-0193` — Destiny 2 (`9 / 28 = 0.321429`); `GAME-0212` — Half-Life 2 (`9 / 28 = 0.321429`).
- Supported combination subsets: `COMB-0235`.
- Scan date: 2026-09-03.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0193` — Destiny 2 | `ACT-008`, `ACT-161`, `ACT-164`, `SYS-215`, `SYS-222`, `INF-073`, `INF-115`, `INF-119`, `TIM-003` | The shared first-person combat and pickup-readable state sit inside a repeatable live-service activity with ability, equipment and reward systems; it does not use Sand Canyon's one-shot authored finite releases, clearance gate, typed finite ammunition beside an unlimited fallback, or fixed next-level terminal. | Near, `0.321429` |
| `GAME-0212` — Half-Life 2 | `ACT-008`, `ACT-161`, `ACT-164`, `SYS-215`, `SYS-222`, `INF-073`, `INF-115`, `INF-119`, `TIM-003` | The shared authored first-person route and live combat are organised around physics manipulation, carried fixtures and chapter checkpoints; it does not bind finite trigger-released hostile membership to this room-clearance gate or expose the same ammunition/fallback tradeoff before one successor threshold. | Near, `0.321429` |

## Novelty assessment

- New genes: `SYS-749`, `CON-578`.
- `SYS-621` is not reused: it requires a completed declared world interaction
  to request one panic population while route transition continues. Sand
  Canyon instead admits target-defeat and traversal-volume triggers and binds
  released finite membership to a room-clearance gate.
- `SYS-572` is not reused: the groups are not indexed to a survival-stage
  clock. `SYS-619` is not reused: no adaptive intensity controller chooses the
  population. `SYS-465` is not reused because the room does not also sample a
  run reward on clearance.
- `CON-262` and `CON-331` are not reused: the packet has no round inventory,
  magazine-reload loop or weapon-wheel class replacement. Its transferable
  scarcity is compatible typed reserve for ammunition-consuming weapons beside
  an unlimited fallback.
- `OBJ-020` and `OBJ-029` are not reused: no individual hostile-clearance event
  is the packet terminal; each is an authored dependency on the route to the
  fixed successor location represented by `OBJ-026`.
- No lower-ID signature, lifecycle state or prior taxonomy decision changes.

## Taxonomy impact

- Registry changes: two new Active genes with portable names and game-scoped
  examples; no existing definition, lifecycle or reviewed signature changes.
- Taxonomy-change record: none.
- Candidate terms affected: recorded in `CANDIDATE_TERMS.md`; level, enemy,
  weapon, difficulty, ammunition amount, trigger location and route names remain
  parameters rather than canonical labels.

## Negative results

- No adaptive encounter, clock-wave or endless-spawn gene is admitted: every
  included hostile group has an authored state trigger and finite closure.
- No reload gene is admitted: the scoped early weapons spend their typed
  reserve directly and do not expose a magazine-refill decision loop.
- No entire-level hostile-clearance objective is inferred: one room requires
  clearance, but the packet succeeds only at the fixed successor threshold.
- No audiovisual evidence, secret, optional detour, multiplayer surface or
  other Serious Sam product contributes to the signature.
- No previous reviewed signature changes.

## Combination subset scan

- Every verified combination in the pre-unit registry was tested as a proper
  subset of the thirteen-gene signature. None fit completely. `COMB-0235` is
  added as the strict triggered-swarm/ammunition/clearance-route core and omits
  health plus partial local-information presentation.
- Comparison and subset scan date: 2026-09-03.
