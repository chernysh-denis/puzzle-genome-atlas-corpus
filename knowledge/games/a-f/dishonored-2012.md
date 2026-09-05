---
game_id: GAME-0247
slug: dishonored-2012
game_title: Dishonored (2012)
analysis_status: reviewed
reviewed: 2026-09-04
combination_ids:
  - COMB-0245
gene_ids:
  action:
    - ACT-008
    - ACT-087
    - ACT-161
    - ACT-164
    - ACT-202
    - ACT-235
    - ACT-341
    - ACT-421
  system:
    - SYS-208
    - SYS-215
    - SYS-369
    - SYS-373
    - SYS-772
    - SYS-773
  constraint:
    - CON-262
    - CON-269
    - CON-282
    - CON-285
    - CON-335
    - CON-591
  information:
    - INF-073
    - INF-115
    - INF-119
    - INF-125
    - INF-297
    - INF-298
    - INF-299
  objective:
    - OBJ-153
  time:
    - TIM-003
---

# Game: Dishonored (2012)

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Parameters describe
gene instances but do not enter the signature.

## Analysis scope

- Version / ruleset: current unmodified English Windows regional Steam
  application `217980`, public Build ID `10256413`, built 2023-01-04 and
  checked 2026-09-04. Only base package `17209`, a fresh single-player New
  Game on `Normal`, default mouse/keyboard input and the base campaign are
  admitted. The separately offered Definitive Edition and every DLC depot are
  excluded.
- Entry: complete the required Coldridge Prison escape and Hound Pits
  onboarding on the same fresh save solely to establish the authored incoming
  state. Do not buy an upgrade, collect an optional rune or bone charm, or
  import bonus equipment. The packet begins at first retained control after
  Samuel leaves the boat in the Distillery District for `High Overseer
  Campbell`, with Blink I and the ordinary tutorial-issued equipment.
- Primary decision loop: read the current objective and journal, local sight
  and sound, incoming awareness cues, health, mana, active left-hand item or
  power, ammunition and the previewed Blink destination; walk, sprint, jump,
  crouch and lean; select Blink, sword, pistol, crossbow or sleep darts; aim a
  short-range relocation and commit only a legal endpoint; avoid, divert or
  trigger guards; choke an unaware reachable target, carry the unconscious
  body, or use a direct weapon; operate required authored objects; learn the
  non-lethal disposition, restrain Campbell, carry him to its matching fixture
  and apply the Brand; collect the required journal, return to Samuel and
  inspect the settled mission report.
- Positive terminal: Campbell is resolved non-lethally with the Heretic's
  Brand, the required journal objective is complete, and the player returns to
  Samuel. Accept the end-mission Stats surface and retain first ordinary Hound
  Pits control before the next mission briefing. Record the report's conduct
  categories and aggregate Chaos state; do not project their consequences
  into later missions.
- Negative terminal: health reaching zero or a required mission state becoming
  invalid ends the current attempt. Continue from the latest authored autosave
  so the failed transient body, awareness, combat, resource and objective state
  is replaced by the checkpoint state. Manual saves and reloads are excluded
  from the reproducible route even though the product permits them.
- Included: direct first-person traversal and posture; visible and audible
  local perception; awareness escalation into search and live combat; sword,
  pistol, crossbow and sleep-dart selection; finite ammunition, health and
  mana; one direct ranged incapacitation or one rear choke; carrying an
  unconscious body; Blink I aim, destination preview, range/resource legality
  and immediate world relocation; required journal/object interactions; the
  learned Brand procedure; Campbell's living non-lethal resolution; authored
  autosave retry; end-mission conduct categories and aggregate Chaos display;
  return to the retained Hound Pits successor.
- Excluded: killing Campbell in the accepted trace; poison-glass alternatives;
  saving or killing Curnow; Granny Rags, Slackjaw and every other side quest;
  runes, bone charms, Sokolov paintings, safes, exhaustive loot, coins and
  collectibles; purchases, upgrades and every power beyond Blink I; grenades,
  spring razors, rewired traps, Wall of Light or Arc Pylon use; exhaustive
  guard clearance; manual-save optimisation, achievements and challenge runs;
  every later mission, full-campaign Chaos propagation and endings; Dunwall
  City Trials, The Knife of Dunwall, The Brigmore Witches, Void Walker's
  Arsenal, Game of the Year, Definitive Edition, consoles, mods, cheats and the
  whole franchise.
- Reproducible parameterisation: use the English Windows public branch, base
  package only, a clean profile, `Normal`, default controls and no optional
  collection or purchase. Follow primary objectives; use one legal Blink I
  relocation, neutralise one required obstructing guard without killing, read
  the Brand instructions, render Campbell unconscious, carry him to the
  interrogation-chair fixture, apply the acquired Brand, obtain the required
  journal, return to Samuel and accept Stats. Exact route, guard, cover, sleep
  dart or choke choice, remaining ammunition, mana, health, awareness count,
  found-body count and completion time are run parameters.
- Potential scoped modules: Curnow's optional outcome, another target route,
  another mission, purchased powers, security-device rewiring, a lethal trace,
  a DLC campaign or whole-campaign Chaos consequences each require a separate
  unit.
- Direct-play status: not conducted. Current official Steam distribution and
  Bethesda support pages establish the sold Windows product, base/DLC boundary
  and mission-conduct settlement. The official PC manual establishes New Game,
  controls, Blink targeting, stealth, combat, equipment, journal and save
  rules. Static written route sources constrain the exact Brand procedure,
  Samuel return and successor transition. This is evidence-backed rules
  reconstruction, not a claimed captured playthrough or local entitlement. No
  video or audio was opened, played, heard, analysed or used.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `DISH-001` | The admitted product is the currently sold English Windows regional Steam app `217980`, base package `17209`, not Definitive Edition or a DLC bundle | Confirmed | Direct | High | P1, P2 |
| `DISH-002` | Its public Windows branch is Build `10256413`, built 2023-01-04; the identifier is distribution state rather than a claimed gameplay patch | Observation | Corroborated | High | S1 |
| `DISH-003` | Missions expose authored goals with multiple supported routes, while current weapon/power, health, mana, ammunition, journal and save state govern the next action | Confirmed | Direct | High | P2, P3 |
| `DISH-004` | Sneak, lean, sound and visibility support avoidance, unaware choking and body movement, while detection can escalate into direct melee or ranged combat | Confirmed | Direct | High | P3 |
| `DISH-005` | Blink previews an aimed short-range destination and commits direct relocation only at a legal range, endpoint and resource state | Confirmed | Direct | High | P3 |
| `DISH-006` | The selected mission permits a lethal or authored non-lethal target outcome; the accepted route requires learning and applying the Heretic's Brand to living incapacitated Campbell at its fixture | Observation | Corroborated | High | S2, S3 |
| `DISH-007` | Mission conduct, including kills, detections, found bodies and related actions, contributes to an aggregate Chaos value displayed on the end-mission Stats surface | Confirmed | Direct | High | P4, P5 |
| `DISH-008` | Returning to Samuel after resolving Campbell and the journal objective closes the mission before retained Hound Pits control | Observation | Corroborated | High | S2, S3 |
| `DISH-009` | Death or invalid required state can end the attempt and authored autosave continuation replaces transient failed state | Confirmed | Corroborated | High | P3, S2 |
| `DISH-010` | The bounded identity is a perception-sensitive infiltration whose aimed relocation and authored non-lethal target procedure settle into an explicit conduct evaluation | Strong Pattern | Corroborated | High | `DISH-003`–`DISH-009` |

## Basic data

- Release / origin: Arkane Studios and Bethesda Softworks, Dishonored, 2012.
- Platform or physical form: lawfully available English Windows Steam
  distribution, regional application `217980`; no direct entitlement is
  claimed.
- Puzzle family: tactical forecast and counterplay, real-time system pressure
  and ordered dependency sequencing.
- Primary and official sources, accessed 2026-09-04:
  - `P1` — [regional Steam application data](https://store.steampowered.com/api/appdetails?appids=217980&cc=ua&l=english),
    for the current Windows product, English support, base package `17209` and
    separately offered Definitive Edition package.
  - `P2` — [official Steam product page](https://store.steampowered.com/app/205100/Dishonored/?l=english),
    for single-player identity, flexible combat, powers, gadgets, stealth and
    mission outcomes; its worldwide app number does not replace the regional
    `217980` distribution identity.
  - `P3` — [official Windows PC manual](https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/205100/manuals/dishonored-gfw-manual-v15.pdf?t=1750785977),
    for New Game, Normal selection, HUD, journal, quick-access equipment,
    traversal, sneak/lean, sight/sound detection, choke/body movement, live
    combat, Blink aim preview and save/checkpoint rules.
  - `P4` — [Bethesda: Chaos system](https://help.bethesda.net/app/answers/detail/a_id/18227/~/how-does-the-chaos-system-work%3F-how-do-i-raise-or-lower-the-chaos-level-that-is-displayed-on-the-end-mission-stats-screen%3F),
    for end-mission Stats visibility and conduct categories that alter Chaos.
  - `P5` — [Bethesda: lowering Chaos](https://help.bethesda.net/app/answers/detail/a_id/18228/~/how-do-i-lower-chaos-in-dishonored%3F),
    for avoiding kills, using stealth and completing non-lethal objectives.
  - `P6` — [Bethesda: Game of the Year contents](https://help.bethesda.net/app/answers/detail/a_id/30680/~/what-is-included-in-the-dishonored-game-of-the-year-edition%3F),
    for the all-DLC bundle boundary excluded from the base packet.
- Corroborating textual sources, accessed 2026-09-04:
  - `S1` — [SteamDB public depots](https://steamdb.info/app/217980/depots/), for
    regional application `217980`, Windows depots, public Build `10256413` and
    timestamps. SteamDB is a secondary distribution mirror, not the publisher.
  - `S2` — [Gamer Guides High Overseer Campbell route](https://www.gamerguides.com/dishonored/guide/main-game/walkthrough/high-overseer-campbell),
    for the written non-lethal Brand prerequisites, target treatment and return
    route.
  - `S3` — [officially licensed Prima sample guide](https://ptgmedia.pearsoncmg.com/images/9780744014341/samplepages/9780744014341_sample.pdf),
    for the mission's Samuel entry/return, lethal/non-lethal target routes and
    authored handoff.
- Claim IDs: `DISH-001`–`DISH-010`.

## Mechanical decomposition

### Action Genes

- Existing `ACT-008`: directly walk, sprint and jump through the mission;
  `ACT-202`: crouch, stand or lean to change exposure; `ACT-164`: select the
  sword, pistol, crossbow, sleep darts or Blink as the current hand;
  `ACT-161`: aim and commit an eligible melee or ranged strike; `ACT-235`:
  choke an unaware reachable target, choose its non-lethal resolution and
  carry the body; `ACT-341`: read or operate one required authored object;
  `ACT-087`: apply the acquired Brand to Campbell in the compatible chair
  fixture.
- New `ACT-421`: aim and commit a short-range world relocation to the currently
  previewed destination instead of traversing every intervening position.
- Powers, targets, weapons, ammunition, mission objects and exact locations are
  parameters. Optional purchases, rewiring, traps and other powers are not
  actions in this packet. Claims: `DISH-003`–`DISH-006`.

### System Behaviour Genes

- Existing `SYS-208`: resolve a sleep dart or other admitted ranged attack
  through cover and body state; `SYS-215`: resolve directly commanded live
  hostile combat; `SYS-373`: advance sight, sound, bodies or harm through local
  suspicion, search and combat; `SYS-369`: replace the failed attempt with the
  latest authored mission checkpoint.
- New `SYS-772`: resolve one valid aimed relocation directly at its world
  endpoint, applying the power's resource debit and destination state without
  visiting the interval. New `SYS-773`: classify bounded mission conduct and
  expose the aggregate evaluation when the mission settles.
- Resolution order: accept movement, posture, equipment, interaction, choke,
  attack or relocation input; validate reach, awareness, equipment, endpoint,
  resource and authored prerequisites; move directly or relocate; update
  perception, bodies and combat; resolve target and journal state; restore a
  failed checkpoint or accept the return; classify conduct on Stats; retain
  first successor control.
- Claims: `DISH-004`–`DISH-009`.

### Constraint Genes

- Existing `CON-262`: ammunition, health/mana elixirs and admitted carried
  equipment remain finite; `CON-269`: Blink use requires a legal destination,
  range, mana and readiness; `CON-282`: incoming story, Brand instructions,
  target resolution, journal, Samuel return and successor obey authored order;
  `CON-285`: an attack requires compatible current weapon, ammunition and body
  state; `CON-335`: an unaware reachable living target is required for a rear
  choke.
- New `CON-591`: an authored non-lethal disposition requires the matching
  learned procedure, a viable restrained target and compatible world fixture.
  Campbell, the Brand, chair, exact counts and mission names are parameters.
- Scarce strategic resources: unseen routes, cover, mana, health, sleep-dart or
  other ammunition, viable target state and checkpoint-local progress. Claims:
  `DISH-003`–`DISH-006`, `DISH-009`.

### Information Genes

- Existing `INF-073`: active left/right-hand equipment, ammunition and
  inventory state are visible; `INF-115`: sight and sound expose only local
  actors and hazards; `INF-119`: health, mana and current personal state are
  visible; `INF-125`: journal, objective markers and authored route gates are
  inspectable.
- New `INF-297`: holding the relocation aim exposes the current legal endpoint
  before commitment. New `INF-298`: local awareness cues disclose incoming
  perception direction and escalation without revealing every hidden actor.
  New `INF-299`: the mission report discloses bounded conduct categories and
  aggregate evaluation after settlement.
- Exact icons, colours, text, counts and screen positions are presentation
  parameters. Claims: `DISH-003`–`DISH-007`.

### Objective Genes

- New `OBJ-153`: resolve one designated authored target through an admitted
  lethal or non-lethal route, complete its required information objective,
  return for mission settlement and retain successor control. The accepted
  trace fixes the non-lethal route; the portable objective label does not.
- A Blink, choke, found instruction, applied Brand, acquired journal or arrival
  at Samuel alone is intermediate. Death/invalid mission state is failure;
  Stats acceptance plus retained Hound Pits control is positive completion.
  Claims: `DISH-006`–`DISH-009`.

### Time Genes

- Existing `TIM-003`: movement, mana use, perception, patrols, body state,
  combat and target opportunities progress continuously while the player
  chooses actions. Menus, loading and the terminal report do not add a second
  decision clock. Claims: `DISH-004`, `DISH-005`, `DISH-009`.

## Reproducible transitions

| Before | Action | Deterministic or bounded resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Fresh `Normal` save has completed required onboarding without optional pickup or purchase | Retain first control after Samuel's Distillery District landing | `High Overseer Campbell` begins with Blink I and ordinary tutorial equipment rather than imported progression | fixed base-game entry | `DISH-001`–`DISH-003` |
| Blink I is active and a candidate point is aimed | Hold relocation aim across a ledge and adjust it | The interface distinguishes a legal endpoint from an unavailable one before commitment | relocation information and legality | `DISH-005` |
| A legal point is previewed within range and sufficient mana remains | Commit Blink | The body appears at the accepted point without occupying the intervening path and mana is debited | non-traversed spatial transition | `DISH-005` |
| One living guard is unaware and reachable from behind | Hold the choke and carry the unconscious body into cover | The actor becomes non-lethally neutralised and its body position changes without an ordinary weapon strike | constrained non-lethal local control | `DISH-004` |
| A guard sees or hears the protagonist, discovers a body or observes harm | Remain exposed, hide or attack | Awareness rises into search/combat or decays when local evidence is lost | recoverable stealth-to-combat transition | `DISH-004` |
| The Brand instructions are not yet registered | Read the matching authored record | The non-lethal target-disposition objective becomes operationally available | learned procedure prerequisite | `DISH-006` |
| Campbell is alive and unconscious at the compatible interrogation-chair fixture and the Brand is acquired | Apply the Brand | Campbell enters the authored living non-lethal resolved state and the target objective advances | irreversible target disposition | `DISH-006` |
| The target and required journal objectives are complete | Return to Samuel and accept departure | The mission closes and the Stats surface classifies this attempt's conduct and aggregate Chaos | explicit mission evaluation | `DISH-007`, `DISH-008` |
| Stats is accepted after the fixed non-lethal route | Continue to the first ordinary Hound Pits control | The settled mission and successor state remain available before the next briefing | reproducible positive terminal | `DISH-008` |
| Health reaches zero or a required mission state becomes invalid | Continue from the authored autosave | Failed transient state is replaced by checkpoint state; manual-save branching is not admitted | reproducible negative terminal | `DISH-009` |

## Strategic and experiential structure

- Planning horizon: choose a route that preserves a viable target and enough
  concealment, mana and non-lethal equipment to carry out the learned authored
  disposition, then preserve the required journal and return path.
- Local tactics: use the Blink preview before leaving cover, crouch or lean to
  manage exposure, separate one unaware guard, hide its unconscious body and
  recover from incomplete detection without converting the accepted route into
  lethal combat.
- Medium-term structure: vertical relocation and local perception lead into a
  multi-step target procedure, then the return converts the whole attempt into
  visible conduct categories rather than ending at the target interaction.
- Reversible versus irreversible: route, posture, equipment selection and
  incomplete awareness can change within the attempt; autosave retry replaces
  a failed branch; Brand application, mission settlement and retained successor
  are the bounded irreversible chain.
- Failure attribution: awareness cues, health/mana, ammunition, objective text,
  target state and Stats categories distinguish exposure, resource loss,
  target invalidation and successful low-lethality completion.
- Player trust: Blink previews destination legality; local cues disclose rising
  perception; the journal exposes required gates; Stats reports conduct after
  the return. Hidden whole-campaign consequences are not claimed in this unit.
- Claim IDs: `DISH-003`–`DISH-010`.

## Replay and variation

- What changes between attempts: chosen route and elevation, Blink endpoints,
  guard positions, posture, choke/sleep-dart use, body placement, awareness,
  direct combat, health, mana, ammunition and the resulting Stats categories.
- Randomness or procedural generation: geometry, objectives, target procedure
  and terminal are authored; live patrol timing, perception and combat outcomes
  vary within that fixed mission.
- Multiple viable strategies: lethal, non-lethal, stealthy, detected and mixed
  paths can resolve the designated target, but this reproducible trace fixes
  the Brand route to preserve a living target and bounded comparison.
- Typical replay motive: reduce kills/detections or test another target route;
  achievements and whole-campaign outcome optimisation remain excluded.
- Claim IDs: `DISH-004`–`DISH-009`.

## Adjacent systems and history

- Direct franchise corridor: later Dishonored releases alter powers, playable
  roles and campaign rules; none is merged into the 2012 base-game packet.
- Similar lower-ID games: Far Cry 3 shares direct stealth, unaware
  neutralisation, local detection and recoverable live combat; Battlefield
  Hardline adds scanning, distraction and living arrest; Crysis Remastered
  adds acquired marks and four capability modes drawing on one reserve;
  Cyberpunk 2077 shares constrained takedowns and authored mission gates.
- Important differences: Blink commits a previewed endpoint without traversing
  the interval, the required target can enter a learned authored non-lethal
  disposition, and the completed mission explicitly settles local conduct into
  an aggregate evaluation before retained successor control.
- Claim IDs: `DISH-003`–`DISH-010`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-087`, `ACT-161`, `ACT-164`, `ACT-202`, `ACT-235`, `ACT-341`, `ACT-421` | route, weapon, power, target, body and Brand names |
| System Behaviour | `SYS-208`, `SYS-215`, `SYS-369`, `SYS-373`, `SYS-772`, `SYS-773` | perception, combat, relocation, checkpoint and conduct values |
| Constraint | `CON-262`, `CON-269`, `CON-282`, `CON-285`, `CON-335`, `CON-591` | equipment, range, mana, route order and target procedure |
| Information | `INF-073`, `INF-115`, `INF-119`, `INF-125`, `INF-297`, `INF-298`, `INF-299` | HUD art, endpoint, awareness, objective and Stats fields |
| Objective | `OBJ-153` | target, journal, return, settlement and successor |
| Time | `TIM-003` | continuous unpaused simulation |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `246` (`GAME-0001`–`GAME-0246`).
- Exact genome matches: none.
- Tied near matches: `GAME-0236` — Far Cry 3 (`18 / 41 = 0.439024`).
- Supported combination subsets: `COMB-0245`.
- Scan date: 2026-09-04.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0236` — Far Cry 3 | `ACT-008`, `ACT-161`, `ACT-164`, `ACT-202`, `ACT-235`, `SYS-208`, `SYS-215`, `SYS-369`, `SYS-373`, `CON-262`, `CON-282`, `CON-285`, `CON-335`, `INF-073`, `INF-115`, `INF-119`, `INF-125`, `TIM-003` | Far Cry 3 adds deliberate optical actor marks, inert diversion, finite healing, mission-critical ally risk and persistent hostile-site conversion. Dishonored instead adds previewed non-traversed relocation, required authored-object/item use, a learned living-target disposition and explicit conduct/Chaos settlement before successor control. | Near, `0.439024` |

### Preserved research notes

- New genes: `ACT-421`, `SYS-772`, `SYS-773`, `CON-591`, `INF-297`,
  `INF-298`, `INF-299`, `OBJ-153`.
- Reused genes: `ACT-008`, `ACT-087`, `ACT-161`, `ACT-164`, `ACT-202`,
  `ACT-235`, `ACT-341`, `SYS-208`, `SYS-215`, `SYS-369`, `SYS-373`,
  `CON-262`, `CON-269`, `CON-282`, `CON-285`, `CON-335`, `INF-073`,
  `INF-115`, `INF-119`, `INF-125`, `TIM-003`.
- Classification result: `New gene` and `New combination of known and new genes`.
- Evidence and reasoning: existing direct movement, posture, equipment,
  interaction, live combat, stealth neutralisation, perception, checkpoint,
  inventory, ability and mission-gate labels fit without changing their
  boundaries. New labels isolate previewed non-traversed relocation, its
  resolution, a multi-prerequisite authored non-lethal target procedure,
  generic awareness cues, post-mission conduct settlement and the full
  target-return-successor objective. Concrete character, mission, power, item,
  fixture and statistic names remain parameters.
- Lower-ID scan: reject `ACT-055` because Blink does not transfer control to a
  targeted body; reject `ACT-014` because the player does not relocate a
  selected board piece; reject `SYS-398` because Blink I is already admitted
  at entry rather than acquired persistently; reject `INF-287` because no
  optical actor-mark acquisition is part of this packet; reject `INF-221`
  because it joins squad concealment to a conjunctive sabotage/clearance
  terminal; reject whole-campaign reputation, morality, ending and manual-save
  genes.

## Taxonomy impact

- Registry changes: eight new Active genes use portable mechanical language
  and game-scoped examples; no existing definition, lifecycle or reviewed
  signature changes.
- Taxonomy-change record: none.
- Candidate terms affected: recorded in `CANDIDATE_TERMS.md`; Dishonored,
  Campbell, Samuel, Hound Pits, Blink, Brand, journal, chair, weapon, exact
  counts, difficulty and Stats labels remain parameters.

## Negative results

- No direct-play, local entitlement, video or audio claim.
- No optional side-objective, collectible, upgrade, other power, security
  device, later-consequence, DLC, edition-union or whole-campaign gene.
- No earlier reviewed signature, definition or lifecycle state changes.

## Combination subset scan

- Every verified combination in the pre-unit registry was tested as a proper
  subset of the 29-gene signature. None fit completely. `COMB-0245` is added as
  the strict relocation/non-lethal-disposition/conduct-settlement core and
  omits general weapon, health, checkpoint and route-support information.
- Comparison and subset scan date: 2026-09-04.

## Delta summary

## New facts

- [Confirmed | Direct | High] Current regional Windows availability, base
  package and edition boundary are fixed in `DISH-001`–`DISH-002`.
- [Confirmed | Corroborated | High] Movement, equipment, stealth, perception,
  combat, Blink and checkpoint rules are bounded in `DISH-003`–`DISH-005` and
  `DISH-009`.
- [Observation | Corroborated | High] Brand disposition, Samuel return, Stats
  evaluation and retained successor form the mission terminal in
  `DISH-006`–`DISH-008`.

## New genes

- [Confirmed | Corroborated | High] `ACT-421`, `SYS-772`, `SYS-773`,
  `CON-591`, `INF-297`, `INF-298`, `INF-299` and `OBJ-153` isolate transferable
  relocation, target-procedure, awareness, evaluation and terminal boundaries.

## New combinations

- [Observation | Corroborated | High] `COMB-0245` captures an awareness-aware
  infiltration in which previewed relocation enables a multi-step non-lethal
  target disposition before explicit mission-conduct settlement.

## Taxonomy changes

- [Observation | Corroborated | High] None; no prior signature, definition or
  lifecycle state changes.

## New questions

- Does HITMAN's bounded mission preserve target-route planning and explicit
  settlement while replacing powered relocation and local Chaos accounting
  with disguise authority, trespass and challenge-grade outcomes?

## Next recommended game

- [Hypothesis | Limited | High] `GAME-0248` — HITMAN World of Assassination.
- Optimisation criterion: retain one authored target mission and a formal
  results boundary while changing the access-control and social-stealth model.
- Expected information gain: distinguish visible awareness and supernatural
  relocation from disguise-conditioned legality and opportunity execution.
- Backlog impact: advances the approved batch-013 ordered horizon.

## Why this game

- [Hypothesis | Limited | High] HITMAN keeps target planning and mission
  settlement near-constant while replacing Dishonored's movement and power
  grammar with systemic social access.
