---
game_id: GAME-0248
slug: hitman-world-of-assassination
game_title: HITMAN World of Assassination
analysis_status: reviewed
reviewed: 2026-09-04
combination_ids:
  - COMB-0246
gene_ids:
  action:
    - ACT-008
    - ACT-161
    - ACT-164
    - ACT-183
    - ACT-202
    - ACT-235
    - ACT-341
    - ACT-406
    - ACT-422
    - ACT-423
  system:
    - SYS-057
    - SYS-208
    - SYS-215
    - SYS-369
    - SYS-373
    - SYS-773
    - SYS-774
    - SYS-775
  constraint:
    - CON-262
    - CON-282
    - CON-285
    - CON-335
    - CON-592
    - CON-593
  information:
    - INF-073
    - INF-115
    - INF-119
    - INF-125
    - INF-298
    - INF-299
    - INF-300
    - INF-301
  objective:
    - OBJ-154
  time:
    - TIM-003
---

# Game: HITMAN World of Assassination

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Parameters describe
gene instances but do not enter the signature.

## Analysis scope

- Version / ruleset: current unmodified English Windows Steam application
  `1659040`, full-game package `672746`, IO Interactive game version `3.280`
  and public Build ID `24833614`, checked 2026-09-04. The build identifier is a
  secondary distribution observation. Only non-VR, online, single-player
  Campaign → HITMAN 1 → Paris → `The Showstopper` on `Professional` is
  admitted; Part One package `963307` and Deluxe package `963308` are not
  silently substituted for the selected full-game entitlement.
- Entry: use a clean profile and the ordinary mission-planning surface. Select
  Main Entrance, the mission's standard suit, ICA19, Fiber Wire and Coin, with
  no smuggled item or Agency pickup, then begin at first retained control
  outside the Palais de Walewska. The selected online state is a reproducible
  service parameter required for the complete scored debrief; offline save and
  leaderboard semantics are excluded rather than inferred.
- Primary decision loop: read the two current target objectives, map, local
  sight and sound, Instinct overlay, awareness, presented disguise, trespass
  and illegal-action or illegal-item state, health, weapon and carried items;
  walk, run or crouch; hold Instinct to inspect nearby actors, targets and
  interactables; throw a Coin to redirect an eligible observer; subdue one
  unaware reachable actor, move or conceal the body and wear its eligible
  outfit; test role-conditioned thresholds while avoiding actors who recognise
  the disguise; operate authored objects or use an admitted close or ranged
  attack; resolve both designated targets, reach an enabled exit and inspect
  the complete online debrief.
- Positive terminal: Viktor Novikov and Dalia Margolis are both resolved by
  legal mission methods, an ordinary marked mission exit is used, and the
  online Debriefing surface exposes objective completion, conduct categories,
  total score and rating. Accept the settled result and retain control at the
  destination/mission surface; stop before replay, another destination or
  spending any mastery-derived unlock.
- Negative terminal: health reaching zero or an authored mission-failure state
  ends the current attempt. Continue only from the latest authored autosave or
  restart the mission so the failed transient body, disguise, awareness,
  target and resource state is replaced. Manual-save optimisation is excluded.
- Included: one fixed Paris story mission; mission planning and declared legal
  loadout; direct third-person traversal and crouch; local sight and sound;
  held Instinct inspection; role-bearing disguise acquisition; role-dependent
  area, action and visible-item legality; disguise-aware exceptional observers;
  trespass, suspicious activity, witnesses, discovered bodies, search and live
  combat; Coin diversion; unaware subdual and body movement; ordinary firearms,
  Fiber Wire and contextual world interactions; two required targets; authored
  autosave retry; enabled exit; post-mission objectives, conduct categories,
  total score and rating.
- Excluded: offline scoring as an alternate ruleset; Elusive Targets, Featured
  Contracts, Contracts, Escalations, Arcade, Freelancer, Sniper Assassin,
  player-created contracts, seasonal or time-limited content and every other
  mode; every other Paris mission, destination and story campaign; challenge
  completion, mastery optimisation, XP/player-level grind, leaderboards,
  achievements, unlock routing and replay; alternate difficulties, starts,
  stashes and loadouts; VR, co-op, mods, trainers, cheats, consoles, Part One,
  Deluxe-only content and the whole trilogy or live-service history.
- Reproducible parameterisation: preserve application, package, version, build,
  online state, `Professional`, Main Entrance and the declared no-stash
  loadout. During the mission use Instinct at least once, throw one Coin to
  redirect an eligible observer, subdue one unaware non-target without killing,
  conceal that body, wear its compatible disguise, cross one threshold that
  the role permits and route around one observer who can recognise it. Resolve
  both targets by currently legal mission methods, use the first safely
  reachable ordinary exit and accept Debriefing. Exact route, disguise, target
  order, elimination methods, witnesses, body location, ammunition, health,
  detection state, completion time, score and rating are run parameters.
- Potential scoped modules: one offline trace, another difficulty, another
  Paris start or elimination route, one Escalation, one Contracts packet, one
  Freelancer contract or another destination each requires a separate scope.
- Direct-play status: not conducted. Valve and IO Interactive current product,
  package, support and patch pages establish lawful availability, product and
  service boundaries. The authorised Feral manual and first-party PlayStation
  product material establish planning, disguise, trespass, Instinct, stealth,
  combat, exit and debrief rules; current IOI patch notes corroborate their
  continuing operation. Static written mission sources constrain the two
  targets and exit gate. This is evidence-backed rules reconstruction, not a
  claimed captured playthrough or entitlement. No video or audio was opened,
  played, heard, analysed or used.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `HIT-001` | The admitted product is current Windows Steam app `1659040`, full-game package `672746`, not Part One, Deluxe or a union of modes | Confirmed | Direct | High | P1, P2 |
| `HIT-002` | IOI version `3.280` is the current official game version and Steam public Build `24833614` is the corresponding observed Windows distribution state | Confirmed | Corroborated | High | P3, S1 |
| `HIT-003` | Planning fixes start, suit, concealed weapon, gear and optional stash before one mission begins | Confirmed | Direct | High | P4, P5 |
| `HIT-004` | Worn disguises change area, action and visible-item legality, while exceptional observers and witnessed crimes can expose or compromise the presented role | Confirmed | Corroborated | High | P3, P4 |
| `HIT-005` | Instinct exposes nearby targets, actors and interactable state through a held situational view without making all future patrol state known | Confirmed | Direct | High | P4 |
| `HIT-006` | Local sight, sound, bodies and suspicious or harmful actions can advance awareness through search, target lockdown and combat | Confirmed | Corroborated | High | P3, P4, P6 |
| `HIT-007` | `The Showstopper` is the Paris story mission with Viktor Novikov and Dalia Margolis as its required target set | Observation | Corroborated | High | P5, P7, S2 |
| `HIT-008` | Ordinary exits activate only after both required targets are resolved | Observation | Corroborated | High | P4, S2, S3 |
| `HIT-009` | Debriefing evaluates objectives and recorded conduct into a displayed total score and rating; online state supplies the complete retained settlement used here | Confirmed | Corroborated | High | P4, P5, P6, P8 |
| `HIT-010` | Death or authored failure permits replacement from an authored mission autosave or complete restart | Confirmed | Corroborated | High | P4, S2 |
| `HIT-011` | The bounded identity is a two-target social infiltration whose presented-role permissions and observer exceptions lead to an explicit scored mission settlement | Strong Pattern | Corroborated | High | `HIT-003`–`HIT-010` |

## Basic data

- Release / origin: IO Interactive; HITMAN World of Assassination, current
  unified product name introduced for the HITMAN 3 client; selected Paris
  content originated in HITMAN (2016).
- Platform or physical form: lawfully available English Windows Steam client,
  full-game package `672746`; one online non-VR single-player story mission.
- Puzzle family: tactical forecast and counterplay; real-time system pressure;
  ordered dependency sequencing.
- Primary and official sources, accessed 2026-09-04:
  - `P1` — [Valve application data](https://store.steampowered.com/api/appdetails?appids=1659040&cc=ua&l=english),
    for the current Windows product and Part One, full-game and Deluxe package
    offers.
  - `P2` — [Valve full-package data](https://store.steampowered.com/api/packagedetails?packageids=672746&cc=ua&l=english),
    for the selected package identity and included application.
  - `P3` — [IOI Game Update 3.280](https://ioi.dk/hitman/patch-notes/2026/game-update-3-280),
    dated 2026-08-26 for 2026-08-27 deployment on PC and all supported
    platforms, for the current version and maintained disguise, trespass,
    target-lockdown and Silent Assassin state.
  - `P4` — [authorised Feral HITMAN manual](https://www.feralinteractive.com/en/manuals/hitman/latest/linux/),
    for story-mode separation, planning, controls, Instinct, items, distraction,
    disguises, trespass, suspicion/search/combat, target lockdown, exits and
    Debriefing rating/score rules. This port manual documents the original
    Paris-era rules; current IOI sources corroborate the admitted continuing
    systems rather than treating the manual as a current build declaration.
  - `P5` — [official IOI HITMAN page](https://ioi.dk/hitman), for the current
    World of Assassination framing, Paris destination, free approach and tool
    planning.
  - `P6` — [IOI February 2021 patch notes](https://ioi.dk/hitman/patch-notes/2021/february-patch-notes),
    for the Silent Assassin tracker, camera-recording recovery and maintained
    trespass feedback.
  - `P7` — [IOI June 2021 patch notes](https://ioi.dk/hitman/patch-notes/2021/june-patch-notes),
    for `The Showstopper` Paris campaign identity and the Viktor Novikov
    objective.
  - `P8` — [IOI cross-progression guide](https://ioisupport.zendesk.com/hc/en-us/articles/32645592211229-HITMAN-World-of-Assassination-Cross-Progression-Guide),
    for the online progression boundary and separation of offline/online save
    and leaderboard state.
  - `P9` — [official PlayStation product page](https://www.playstation.com/en-gb/games/hitman-3/),
    for first-party corroboration of post-mission rating, challenges, mastery,
    starting disguise, weapons, stashes and opportunity exploration; it is not
    evidence for the selected PC build.
- Corroborating textual sources, accessed 2026-09-04:
  - `S1` — [SteamDB public depots](https://steamdb.info/app/1659040/depots/),
    for Windows depot `1659041`, public Build `24833614`, built 2026-08-20 and
    published 2026-08-27. SteamDB is a secondary distribution mirror.
  - `S2` — [TrueAchievements Paris walkthrough](https://www.trueachievements.com/game/HITMAN/walkthrough/4),
    for written mission entry, both target identities and legal route states.
  - `S3` — [Gamepressure Paris exit record](https://www.gamepressure.com/hitman/leaving-the-mission-area-after-killing-both-targets-paris-the-sh/z887cf),
    for ordinary exit activation after both target objectives.
- Claim IDs: `HIT-001`–`HIT-011`.

## Mechanical decomposition

### Action Genes

- Existing `ACT-008`: directly traverse the venue; `ACT-202`: crouch or stand
  to change exposure; `ACT-164`: select a carried weapon or item; `ACT-161`:
  aim and commit an eligible close or ranged attack; `ACT-183`: reload the
  magazine-fed pistol; `ACT-235`: subdue an unaware reachable actor and move
  the body; `ACT-341`: operate a reachable authored door, container, pickup or
  exit; `ACT-406`: throw one Coin as a positioned inert diversion.
- New `ACT-422`: take and wear one eligible role-bearing outfit from a
  neutralised actor. New `ACT-423`: hold the live situational overlay to inspect
  nearby actors, targets and interactables through its bounded perception.
- Outfit, actor, tool, weapon, target and venue names are parameters. Optional
  mastery equipment and other destinations are outside the action set. Claims:
  `HIT-003`–`HIT-007`.

### System Behaviour Genes

- Existing `SYS-057`: eligible observers replace their current patrol response
  when they perceive the positioned Coin stimulus; `SYS-208`: ranged attacks
  resolve through cover and body state; `SYS-215`: directly commanded attacks
  and hostile responses resolve in live time; `SYS-373`: sight, sound, bodies
  and harm escalate local suspicion through search and combat; `SYS-369`:
  mission failure replaces transient state with an authored autosave;
  `SYS-773`: mission closure converts recorded conduct into disclosed rating
  and total evaluation.
- New `SYS-774`: the currently presented role changes permissions for areas,
  actions and visibly carried items. New `SYS-775`: each observer tests the
  presented role against its own recognition state, so an otherwise permitted
  disguise can be seen through or compromised without globally revealing all
  actors.
- Resolution order: accept movement, posture, overlay, equipment, diversion,
  subdual, disguise, object or attack input; validate reach, inventory, role,
  local observer and target state; update patrol, access and suspicion; resolve
  stealth or live combat; update both target objectives; restore failure or
  enable exits; classify conduct and score on Debriefing. Claims:
  `HIT-004`–`HIT-010`.

### Constraint Genes

- Existing `CON-262`: weapons, magazine/reserve ammunition and carried gear are
  finite; `CON-282`: planning, two targets, enabled exit and Debriefing follow
  authored dependencies; `CON-285`: an attack or reload requires compatible
  current weapon, ammunition and body state; `CON-335`: a close stealth subdual
  requires an unaware reachable eligible actor.
- New `CON-592`: a restricted area, suspicious action or visible item is
  permitted only when the presented role grants that context and no applicable
  observer exception rejects it. New `CON-593`: ordinary mission exits cannot
  settle while any member of the declared designated-target set remains
  unresolved.
- Scarce strategic resources: unseen routes, observer attention, clean role
  identities, body concealment, ammunition, carried gear and health. Exact
  roles, areas, target count and item names are parameters. Claims:
  `HIT-003`, `HIT-004`, `HIT-007`–`HIT-010`.

### Information Genes

- Existing `INF-073`: active weapon, ammunition and carried items are visible;
  `INF-115`: ordinary sight, sound and spatial effects expose local actors;
  `INF-119`: health and immediate personal state are visible; `INF-125`: map,
  target objectives and exit gate are inspectable; `INF-298`: local awareness
  cues expose incoming suspicion and alert; `INF-299`: Debriefing exposes
  conduct categories and aggregate evaluation.
- New `INF-300`: a held situational overlay distinguishes nearby designated
  targets, actors and interactable objects through bounded occlusion. New
  `INF-301`: the interface exposes the presented role plus current trespass,
  suspicious-action and visible-item legality sufficient to revise the route.
- Exact silhouettes, icons, colours, labels, score and screen positions are
  presentation parameters. Claims: `HIT-003`–`HIT-009`.

### Objective Genes

- New `OBJ-154`: resolve every member of one closed designated-target set,
  use an enabled mission exit and retain a scored settlement that exposes
  completion before another attempt begins.
- Reaching one target, completing one optional opportunity, killing one target
  or merely reaching an exit is intermediate. Death/mission failure is the
  negative terminal; both targets, exit and accepted Debriefing are the
  positive terminal. Claims: `HIT-007`–`HIT-010`.

### Time Genes

- Existing `TIM-003`: patrols, perception, diversion, target movement, combat
  and body state progress continuously during live control. Planning, pause and
  Debriefing do not add a second decision clock. Claims: `HIT-003`–`HIT-010`.

## Reproducible transitions

| Before | Action | Deterministic or bounded resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Full-game online Campaign planning is open on the fixed Paris mission | Commit Main Entrance, standard suit, ICA19, Fiber Wire, Coin and no stash on `Professional` | First control begins outside the fixed destination with exactly the declared loadout and two target objectives | reproducible entry | `HIT-001`–`HIT-003` |
| A nearby actor, target or interactable is within the overlay's bounded perception | Hold Instinct while turning through the local space | Eligible nearby state is outlined or distinguished through ordinary occlusion without revealing every future route | deliberate partial-information view | `HIT-005` |
| An eligible observer is unaware and one Coin remains carried | Aim and throw the Coin to a reachable quiet point | The observer investigates the perceived stimulus and replaces its immediate patrol response | positioned diversion | `HIT-006` |
| One eligible non-target is unaware and reachable | Subdue without killing, conceal the body and wear its outfit | The body is neutralised; the presented role changes and its role-conditioned permissions become active | acquired social identity | `HIT-004` |
| The presented role permits a threshold but one nearby actor recognises its exception | Cross only outside that actor's effective observation or reroute | Ordinary observers admit the role while the exceptional observer can build suspicion and expose it | observer-specific permission boundary | `HIT-004`, `HIT-006` |
| A suspicious or harmful action, illegal visible item or discovered body is perceived | Break sight, change to a clean eligible disguise or fight | Awareness advances through search/compromise/combat or falls only under the applicable local and identity rules | recoverable social-stealth escalation | `HIT-004`, `HIT-006` |
| One designated target remains unresolved | Reach an ordinary exit marker | The exit cannot settle the story mission; the remaining objective persists | conjunctive target gate | `HIT-007`, `HIT-008` |
| Both designated targets are resolved | Enter one enabled ordinary mission exit | The mission closes and opens online Debriefing rather than another live destination | bounded mission closure | `HIT-008`, `HIT-009` |
| Debriefing is open | Inspect objectives, conduct categories, total score and rating, then accept | The complete evaluated result is retained before control returns to the destination/mission surface | reproducible positive terminal | `HIT-009` |
| Health reaches zero or an authored failure is declared | Continue from autosave or restart | Failed transient disguise, awareness, target and resource state is replaced by authored state | reproducible negative terminal | `HIT-010` |

## Strategic and experiential structure

- Planning horizon: commit a legal baseline loadout, then choose target order,
  disguise chain and exit route that preserve clean identities, ammunition and
  recoverable awareness while satisfying both targets.
- Local tactics: inspect through Instinct, separate an eligible actor with a
  Coin, neutralise and conceal without witnesses, compare a role's ordinary
  access with nearby recognition exceptions, and avoid displaying an illegal
  item where that presentation changes observer response.
- Medium-term structure: each acquired role trades access for a different set
  of exceptional observers. Target resolution is not terminal: both objectives
  must survive the route to an enabled exit before all recorded conduct is
  converted into the visible debrief.
- Reversible versus irreversible: movement, posture, selection, incomplete
  suspicion and some disguise changes can be revised; an exposed identity,
  neutralised actor, resolved target and settled mission constrain or close the
  route; autosave retry replaces a failed branch.
- Failure attribution: target objectives, presented-role icon, trespass and
  illegal-action feedback, observer awareness, health, exit state and debrief
  categories separate access, exposure, combat, gate and evaluation outcomes.
- Player trust: permitted roles must open only their stated contexts;
  exceptional observers must remain locally readable; both targets must gate
  exit; Debriefing must report the conduct that the score evaluates. Claims:
  `HIT-003`–`HIT-011`.

## Replay and variation

- What changes between attempts: target order, route, acquired disguise,
  exceptional observer positions, Coin landing point, neutralisation and body
  placement, elimination method, awareness, ammunition, health, time, score
  and rating.
- Randomness or procedural generation: the destination, objectives and target
  set are authored. Actor timing and live perception/combat outcomes vary
  within the fixed mission.
- Multiple viable strategies: direct, disguised, accident-led, stealthy and
  detected methods can legally resolve the targets, but this packet fixes the
  entry, role-change sample, two-target exit gate and debrief terminal rather
  than cataloguing every opportunity.
- Typical replay motive: improve access efficiency or conduct rating; mastery,
  challenge, leaderboard and unlock optimisation remain outside this unit.
- Claims: `HIT-003`–`HIT-010`.

## Adjacent systems and history

- Direct product corridor: World of Assassination unifies three campaign sets
  and many modes in one client; the corpus admits only this one stable HITMAN 1
  Paris story mission and does not merge that history.
- Similar lower-ID games: Dishonored shares local awareness, unaware
  neutralisation, live recovery and conduct settlement; Far Cry 3 adds acquired
  actor marks and a site-conversion terminal; Battlefield Hardline adds optical
  analysis, distraction and living arrest; PAYDAY 2 shares civilian control,
  staged stealth-to-loud escalation and a scored contract exit.
- Important differences: HITMAN makes a recoverable outfit into a presented
  social role whose access and illegal-item rules vary by context and by
  observer, then conjunctively gates exit on two designated targets before a
  complete mission score. Claims: `HIT-004`–`HIT-011`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-161`, `ACT-164`, `ACT-183`, `ACT-202`, `ACT-235`, `ACT-341`, `ACT-406`, `ACT-422`, `ACT-423` | route, outfit, item, weapon and target names |
| System Behaviour | `SYS-057`, `SYS-208`, `SYS-215`, `SYS-369`, `SYS-373`, `SYS-773`, `SYS-774`, `SYS-775` | role permission, observer, combat, checkpoint and score values |
| Constraint | `CON-262`, `CON-282`, `CON-285`, `CON-335`, `CON-592`, `CON-593` | role, area, visible item, target set and exit |
| Information | `INF-073`, `INF-115`, `INF-119`, `INF-125`, `INF-298`, `INF-299`, `INF-300`, `INF-301` | overlay art, legality labels, objectives and Debriefing fields |
| Objective | `OBJ-154` | target set, exit, score, rating and retention |
| Time | `TIM-003` | continuous unpaused simulation |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `247` (`GAME-0001`–`GAME-0247`).
- Exact genome matches: none.
- Tied near matches: `GAME-0247` — Dishonored (2012) (`22 / 41 = 0.536585`).
- Supported combination subsets: `COMB-0246`.
- Scan date: 2026-09-04.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0247` — Dishonored (2012) | `ACT-008`, `ACT-161`, `ACT-164`, `ACT-202`, `ACT-235`, `ACT-341`, `SYS-208`, `SYS-215`, `SYS-369`, `SYS-373`, `SYS-773`, `CON-262`, `CON-282`, `CON-285`, `CON-335`, `INF-073`, `INF-115`, `INF-119`, `INF-125`, `INF-298`, `INF-299`, `TIM-003` | Dishonored adds previewed non-traversed relocation, mana and a learned fixture-dependent living-target disposition before successor control. HITMAN adds positioned diversion, acquired presented roles, role- and observer-conditioned legality, held situational outlines and a closed two-target exit gate before scored settlement. | Near, `0.536585` |

### Preserved research notes

- New genes: `ACT-422`, `ACT-423`, `SYS-774`, `SYS-775`, `CON-592`,
  `CON-593`, `INF-300`, `INF-301`, `OBJ-154`.
- Reused genes: `ACT-008`, `ACT-161`, `ACT-164`, `ACT-183`, `ACT-202`,
  `ACT-235`, `ACT-341`, `ACT-406`, `SYS-057`, `SYS-208`, `SYS-215`,
  `SYS-369`, `SYS-373`, `SYS-773`, `CON-262`, `CON-282`, `CON-285`,
  `CON-335`, `INF-073`, `INF-115`, `INF-119`, `INF-125`, `INF-298`,
  `INF-299`, `TIM-003`.
- Classification result: `New gene` and `New combination of known and new genes`.
- Evidence and reasoning: existing traversal, equipment, attack, diversion,
  authored interaction, stealth neutralisation, perception, checkpoint and
  conduct-settlement boundaries fit without revision. New labels isolate
  deliberate held Instinct inspection, an acquired presented role, its
  context- and observer-specific permissions, their explicit feedback and the
  multi-target scored terminal. Product, venue, actor, outfit, target, item,
  score and rating names remain parameters.
- Lower-ID scan: reject `ACT-237`, because a disguise is acquired in the world
  and changes social presentation rather than selecting a combat class at
  spawn; reject `SYS-313`, because the presented role changes permissions
  rather than linearly escalating a public wanted tier; reject `SYS-475` and
  `SYS-476`, because no preventable regional witness report or persistent
  bounty is admitted; reject `INF-287`, because Instinct does not require a
  retained optical actor-mark acquisition; reject `OBJ-153`, because its
  portable boundary requires one designated target and successor control,
  whereas this packet requires a closed multi-target set and scored debrief.

## Taxonomy impact

- Registry changes: nine new Active genes use portable mechanical language
  and game-scoped examples; no existing definition, lifecycle or reviewed
  signature changes.
- Taxonomy-change record: none.
- Candidate terms affected: recorded in `CANDIDATE_TERMS.md`; HITMAN, World of
  Assassination, Paris, The Showstopper, target, outfit, Instinct, Trespassing,
  Enforcer, Silent Assassin, ICA19, Fiber Wire, Coin and score labels remain
  parameters or literal interface/product terms.

## Negative results

- No direct-play, local-entitlement, screenshot, video or audio claim.
- No time-limited target, user contract, Escalation, Freelancer, challenge,
  mastery, leaderboard, replay, other destination, package or trilogy union.
- No earlier reviewed signature, definition or lifecycle state changes.

## Combination subset scan

- Every verified combination in the pre-unit registry was tested as a proper
  subset of the 34-gene signature. None fit completely. `COMB-0246` is added as
  the strict presented-role, observer-exception, multi-target and scored-
  settlement core and omits general weapons, health, checkpoint and map state.
- Comparison and subset scan date: 2026-09-04.

## Delta summary

## New facts

- [Confirmed | Direct | High] Current full-game Windows availability, version,
  build and package boundary are fixed in `HIT-001`–`HIT-003`.
- [Confirmed | Corroborated | High] Disguise, access, observer, Instinct,
  perception, combat and checkpoint rules are bounded in `HIT-004`–`HIT-006`
  and `HIT-010`.
- [Observation | Corroborated | High] Both targets, enabled exit and complete
  online scored debrief form the terminal in `HIT-007`–`HIT-009`.

## New genes

- [Confirmed | Corroborated | High] `ACT-422`, `ACT-423`, `SYS-774`, `SYS-775`,
  `CON-592`, `CON-593`, `INF-300`, `INF-301` and `OBJ-154` isolate transferable
  social-role, inspection, legality, target-gate and settlement boundaries.

## New combinations

- [Observation | Corroborated | High] `COMB-0246` captures an infiltration in
  which acquired presented roles and observer exceptions must resolve a closed
  target set before explicit scored settlement.

## Taxonomy changes

- [Observation | Corroborated | High] None; no prior signature, definition or
  lifecycle state changes.

## New questions

- Does Resident Evil 4's bounded survival-action chapter preserve authored
  route pressure and checkpoint settlement while replacing social identity and
  conduct scoring with inventory geometry, escort state and merchant economy?

## Next recommended game

- [Hypothesis | Limited | High] `GAME-0249` — Resident Evil 4 (2023 remake).
- Optimisation criterion: retain one bounded authored mission and recoverable
  combat route while changing both the information and resource grammar.
- Expected information gain: distinguish presented-role infiltration from
  spatial inventory, enemy control and protected-companion pressure.
- Backlog impact: advances the approved batch-013 ordered horizon.

## Why this game

- [Hypothesis | Limited | High] Resident Evil 4 keeps real-time authored combat
  near-constant while replacing disguise-conditioned access and scored
  debriefing with scarce inventory and survival routing.
