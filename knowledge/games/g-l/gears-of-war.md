---
game_id: GAME-0321
slug: gears-of-war
game_title: Gears of War
analysis_status: reviewed
reviewed: 2026-09-20
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-161
    - ACT-164
    - ACT-183
    - ACT-184
    - ACT-199
    - ACT-226
    - ACT-241
    - ACT-341
    - ACT-478
  system:
    - SYS-208
    - SYS-215
    - SYS-222
    - SYS-348
    - SYS-369
    - SYS-407
    - SYS-737
    - SYS-749
    - SYS-924
  constraint:
    - CON-262
    - CON-282
    - CON-285
    - CON-326
    - CON-402
    - CON-578
  information:
    - INF-073
    - INF-115
    - INF-119
    - INF-125
    - INF-268
    - INF-353
  objective:
    - OBJ-188
  time:
    - TIM-003
---

# Game: Gears of War

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Difficulty,
weapon, hostile, route and checkpoint labels are parameters, not gene names.

## Analysis scope

- Version / ruleset: original English North American Xbox 360 retail Gears of
  War, released in 2006. The packet reconstructs launch-disc campaign rules
  from Microsoft's release notice and original manual; no title-update number,
  disc pressing or executed binary was observed.
- Structured analysis target: original Xbox 360 base game, fresh solo Campaign
  on `Casual`, default controls, Act 1 `Ashes`, chapter `14 Years After E-Day`,
  choosing the right-hand Training route; see `GAME-0321` in
  [`knowledge/platforms/games.json`](../../platforms/games.json).
- Primary decision loop: follow Dom from Marcus's cell, choose Training, operate
  the prison controls, shoot the two door circuits, practise contextual cover,
  mantle and roadie run, then use cover, blind or aimed fire, finite ammunition,
  active reloads, grenades and Dom's autonomous support to survive the remaining
  Locust groups and reach the King Raven departure into `Trial By Fire`.
- Entry: first ordinary Marcus control after Dom opens the prison cell and
  gives him a Hammerburst, before the route choice.
- Positive terminal: the final outdoor Locust group is settled, the King Raven
  lands, the route gate falls, Marcus reaches the extraction trigger and the
  chapter-complete transition advances to `Trial By Fire`.
- Negative terminal: Marcus's lethal state ends the attempt and restores the
  latest accepted campaign checkpoint. A downed Dom may be revived at reach;
  leaving the chapter, taking the left Combat route or stopping before the
  chapter transition does not satisfy this packet.
- Included: direct third-person movement; contextual cover entry, edge movement,
  slip, SWAT turn, mantle, evade and roadie run; aimed fire and blind fire;
  active weapon switching; finite magazine and reserve ammunition; ordinary and
  timing-graded active reload; one carried Bolo Grenade throw; compatible pickup;
  Crimson Omen health and quiet-interval regeneration; autonomous Dom follow,
  cover and return fire; reachable squadmate revival if Dom is downed; authored
  controls and doors; finite encounter groups; checkpoint restoration; tutorial
  prompts; mission objective and chapter handoff.
- Excluded: the left `Straight Into the Fight` route; optional COG Tags; later
  `Trial By Fire` combat; chainsaw execution as a required mechanic; stationary
  turret use; player-issued squad orders, because Marcus is not established as
  an eligible squad leader inside this bounded prison packet; co-op, split
  screen, Xbox Live, Versus, leaderboards and achievements; Windows-exclusive
  campaign content; Ultimate Edition, Reloaded, sequels, DLC and remasters.
- Reproducible parameterisation: start a fresh original-game solo Casual
  campaign, take control in the cell, follow Dom and select Training. Use the
  console and X interaction where prompted, shoot both orange circuit boxes,
  follow the cover/mantle/roadie-run instruction path, collect only reachable
  ammunition or grenades, clear required Locust while deliberately completing
  at least one ordinary reload and one active-reload attempt, revive Dom if he
  becomes downed, continue through the final courtyard, then enter the route
  trigger after the Raven arrives and the gate falls. Weapon expenditure,
  reload grade, blind-versus-aimed shots, damage, Dom's downing and checkpoint
  recovery remain bounded attempt parameters.
- Potential scoped modules: the left combat route, performed save/reload state,
  player-issued squad orders after Marcus gains leader authority, chainsaw
  combat, emergence-hole closure, co-op revival, later chapters, multiplayer
  and each later edition require separate entry and evidence boundaries.
- Direct-play status: not conducted. No Xbox 360 console, original disc,
  installed build, storage device, save, controller trace, screenshot, video or
  audio was opened or analysed. Microsoft and Xbox establish product identity;
  the original manual directly establishes controls, cover, health, revival and
  active reload; written original-Xbox-360 routes establish the bounded path and
  terminal. This is a source-bounded reconstruction, not a claimed playthrough.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `GOW-001` | Microsoft released Epic Games' original Gears of War for Xbox 360 in North America on 2006-11-12 | Confirmed | Direct | High | P1 |
| `GOW-002` | The original controller joins movement, aim/fire, weapon switching, reload, interaction and the contextual A-button cover/movement vocabulary | Confirmed | Direct | High | P2 |
| `GOW-003` | Cover admits aimed exposure or blind fire, while mantle, cover slip, SWAT turn, evade and roadie run have distinct context and roadie run blocks firing | Confirmed | Direct | High | P2 |
| `GOW-004` | A second timed reload press has success, perfect and failure outcomes: faster reload, much faster reload plus a small damage boost, or a slower-than-ordinary reload | Confirmed | Direct | High | P2 |
| `GOW-005` | The HUD exposes ammunition, Crimson Omen life, objectives, contextual actions and the active-reload indicator | Confirmed | Direct | High | P2 |
| `GOW-006` | Damage fills the Crimson Omen toward death, quiet safety regenerates Marcus and a reachable downed squadmate may be revived | Confirmed | Direct | High | P2 |
| `GOW-007` | Dom independently defends, takes cover and returns fire without continuous player steering | Confirmed | Direct | High | P2 |
| `GOW-008` | The Training route begins after the prison-cell release, uses controls, destructible door circuits, cover traversal, timed running and several Locust fights | Observation | Corroborated | High | S1, S2, S3 |
| `GOW-009` | The final courtyard settlement admits the King Raven landing and chapter transition into `Trial By Fire` | Observation | Corroborated | High | S1, S2, S3 |
| `GOW-010` | No direct run, installed-build inspection, checkpoint reload or successor-save comparison was performed | Confirmed | Direct | High | R1 |

## Basic data

- Release / origin: Epic Games / Microsoft Game Studios; North American Xbox
  360 retail release on 2006-11-12.
- Platform or physical form: original English North American Xbox 360 base-game
  retail disc rules, fresh solo Casual campaign.
- Puzzle family: tactical forecast and counterplay; real-time system pressure;
  world topology and perspective; agent routing and coordination; ordered
  dependency sequencing.
- Primary and official sources, accessed 2026-09-20:
  - **[P1]** [Xbox Wire Emergence Day announcement](https://news.xbox.com/en-us/2006/08/03/gears-of-war-emergence-day-announced/),
    for the original Xbox 360 product and 2006-11-12 North American release.
  - **[P2]** [official original Xbox 360 manual](https://download.microsoft.com/download/F/9/9/F99AB8F0-5191-4EDD-B312-7A9B9E4784FA/GOW_MNL_EN-US.pdf),
    for the controller, HUD, health, regeneration, revival, autonomous squad
    behaviour, blind/aimed fire, contextual movement and active reload grades.
- Corroborating textual sources, accessed 2026-09-20:
  - **[S1]** [original Xbox 360 GameFAQs route by Cuzit](https://gamefaqs.gamespot.com/xbox360/928234-gears-of-war/faqs/46454),
    for the original-console-only boundary, route choice, tutorial actions,
    combat, roadie-run gate, Raven landing and chapter transition.
  - **[S2]** [original Xbox 360 GameFAQs route by Shotgunnova](https://gamefaqs.gamespot.com/xbox360/928234-gears-of-war/faqs/53814),
    for the cell opening, right-hand tutorial route and prison sequence.
  - **[S3]** [StrategyWiki Act One route](https://strategywiki.org/wiki/Gears_of_War/Act_One%3A_Ashes),
    for the Training/Combat choice, tutorial sequence and King Raven terminal.
- Research record: **[R1]** local 2026-09-20 preflight found no original Xbox
  360 console, disc, binary, save or controller trace; no audiovisual evidence
  or direct play was used.
- Claim IDs: `GOW-001`–`GOW-010`.

## Mechanical decomposition

### Action Genes

- Existing `ACT-008` owns direct traversal, evade, mantle and held roadie-run
  displacement; `ACT-161` aimed or blind firearm attacks; `ACT-164` weapon
  switching; `ACT-183` ordinary magazine reload; `ACT-184` one carried grenade
  throw; `ACT-199` compatible ammunition/weapon pickup; `ACT-226` contextual
  cover entry, edge travel, slip, SWAT turn and exit; `ACT-241` reachable Dom
  revival; and `ACT-341` the console, door and route interactions.
- New `ACT-478` owns the deliberate second reload press during the moving
  active-reload indicator. The ordinary first press remains `ACT-183`; the
  outcome grade belongs to `SYS-924`. Claims: `GOW-002`–`GOW-006`, `GOW-008`.

### System Behaviour Genes

- `SYS-208` resolves aimed or blind shots through exposure, obstruction and
  body damage; `SYS-215` advances direct real-time combat; `SYS-222` accepts
  compatible ammunition/grenade pickups; `SYS-348` owns Dom's downed and
  revival state; `SYS-737` applies Marcus damage, death and quiet-interval
  health regeneration; `SYS-407` runs Dom's autonomous follow, cover and fire;
  `SYS-749` instantiates finite authored combat groups; and `SYS-369` restores
  the latest accepted checkpoint after Marcus's lethal failure.
- New `SYS-924` grades the second reload press: success shortens the reload,
  perfect shortens it further and applies the documented small damage boost,
  while failure lengthens the reload beyond an ordinary attempt.
- Resolution order: context accepts movement or cover action; weapon state
  admits a shot or reload; the second press is measured against the current
  reload indicator; grade modifies readiness and possibly damage; live combat,
  ally AI, health/downing and encounter clearance update together; authored
  gates admit the final Raven transition. Claims: `GOW-003`–`GOW-009`.

### Constraint Genes

- `CON-262` bounds carried weapons, grenades and ammunition; `CON-285` requires
  compatible weapon/magazine/reserve state; `CON-326` requires reachable cover
  geometry and supported transition; `CON-282` keeps tutorial gates ordered;
  `CON-402` blocks declared route progress behind required finite groups; and
  `CON-578` requires usable ammunition for firearm operation. Roadie-run's
  firing prohibition, the active-reload timing band and Dom revival reach are
  parameters of their owning actions/systems rather than separate constraints.
  Claims: `GOW-002`–`GOW-009`.

### Information Genes

- `INF-073` exposes active weapon, ammunition and grenade state; `INF-119`
  exposes Crimson Omen and ally condition; `INF-115` local sight and sound;
  `INF-125` current mission gates; and `INF-268` the current contextual tutorial
  instruction/action icon.
- New `INF-353` exposes the active reload's moving marker and outcome regions
  before the second press, then reports success, perfect or failure. It does not
  reveal future enemy motion or guarantee the player's timing. Claims:
  `GOW-004`, `GOW-005`, `GOW-008`.

### Objective Genes

- New `OBJ-188` owns the complete prison-training breakout: choose Training,
  cross its control/cover/combat gates, settle the final courtyard, reach the
  King Raven trigger and retain `Trial By Fire` as the named successor. Route
  choice, practice completion or Raven arrival without the chapter transition
  is insufficient. Claims: `GOW-008`–`GOW-010`.

### Time Genes

- `TIM-003` owns continuous movement, combat, reload timing, regeneration,
  ally behaviour and encounter pressure. Checkpoint restoration replaces state
  after failure and is not a rewind input. Claims: `GOW-003`–`GOW-009`.

## Reproducible transitions

| Before | Action | Deterministic or bounded resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| A compatible cover surface is reachable | Move toward it and press A | Marcus attaches to the supported edge and receives cover-local movement/exposure options | cover is an explicit state, not merely occlusion | `GOW-003` |
| Marcus is attached to cover with a hostile beyond it | Fire without aiming | only the weapon is exposed and a less-controlled shot resolves around cover | blind fire trades precision for body exposure | `GOW-003` |
| Marcus is attached to cover with a legal adjacent edge | Aim, slip, SWAT-turn, mantle or leave as prompted | the contextual A vocabulary resolves according to geometry and direction | one input is context-gated by world topology | `GOW-002`, `GOW-003` |
| Marcus is outside cover with a traversable path | Hold A while moving | roadie run increases protected movement but blocks firearm use until it ends | speed and offence are mutually exclusive in this state | `GOW-003` |
| The active weapon has reserve ammunition | Press reload once | ordinary magazine transfer begins and fire readiness is surrendered | reload is a live commitment | `GOW-002`, `GOW-004` |
| The active-reload indicator is moving | Press reload a second time | timing is graded as success, perfect or failure | the player acts on a disclosed transient window | `GOW-004`, `GOW-005` |
| The second press lands in the perfect band | Allow reload to settle | readiness returns much faster and a small damage boost becomes active | perfect timing changes both downtime and offence | `GOW-004` |
| The second press lands outside accepted bands | Allow reload to settle | readiness returns later than after an ordinary reload | attempted optimisation has a visible downside | `GOW-004` |
| Dom is active beside Marcus | Advance into a combat region | Dom follows and independently seeks cover and returns fire | companion help does not require continuous steering | `GOW-007` |
| Dom is downed and reachable | Press X near him | Dom returns to active squad state under the revival rule | ally loss may be recoverable inside combat | `GOW-006` |
| Marcus remains alive and takes no new damage | Wait in safety | Crimson Omen recedes and health restores toward its cap | cover converts a quiet interval into recovery | `GOW-006` |
| Marcus reaches lethal state after an accepted checkpoint | Continue the campaign attempt | transient combat state is replaced by the latest eligible checkpoint | failure recovery is authored rather than persistent damage | `GOW-006`, `GOW-010` |
| The last courtyard group has settled | Approach the Raven route gate | the King Raven lands, the gate falls and the exit trigger becomes reachable | combat settlement admits extraction | `GOW-009` |
| The extraction trigger is reachable | Enter it | `14 Years After E-Day` completes and `Trial By Fire` begins | positive terminal and named successor | `GOW-009`, `GOW-010` |

## Strategic and experiential structure

- Local decision: choose between aimed exposure and blind fire, leave cover for
  a faster roadie-run crossing, attempt an active reload or accept ordinary
  downtime, and revive Dom only when the approach is safe enough.
- Medium-term planning: preserve ammunition and grenades across the prison
  sequence, move between compatible cover before Crimson Omen fills, and avoid
  letting an active-reload failure coincide with an exposed hostile push.
- Long-term structure: the tutorial alternates authored interaction lessons,
  traversal tests and finite combat, then asks the same cover/reload language to
  carry the final courtyard into one extraction transition.
- Common heuristics: enter cover before aiming; use blind fire only when target
  certainty outweighs lost accuracy; roadie-run between safe edges, not while a
  shot is needed; use the active-reload marker rather than guessing; revive Dom
  from protected reach; let health recover before the next gate.
- Failure attribution: cover prompts, reload grade, ammunition, Crimson Omen,
  ally state and mission instruction are separately visible, while checkpoint
  replacement bounds the cost of lethal error.
- Player trust: the manual-backed HUD exposes every temporary state used by the
  declared decisions; enemy positions beyond local sight remain appropriately
  partial.

## Replay and variation

- Hostile movement, Dom's paths, ammunition expenditure, grenade use, damage,
  downing, active-reload grade and checkpoint returns can vary between attempts.
- Prison geometry, Training instruction order, circuit boxes, authored combat
  regions, Raven landing and chapter successor remain fixed.
- The left Combat route offers a different opening sequence but is excluded;
  choosing it is not treated as a variant of the same tested packet.
- Casual difficulty is fixed. Hardcore/Insane tuning, co-op and collectible
  hunting are separate replay motives rather than properties of this genome.

## Adjacent systems and history

- *Halo 3* shares a 2000s Xbox campaign, finite two-weapon combat, checkpoints,
  authored groups and a named successor, but it uses a separate rechargeable
  shield and passive Motion Tracker. Gears instead attaches the body to cover,
  offers blind fire, couples health recovery to the same body pool and makes
  magazine timing an explicit risk/reward input.
- *Grand Theft Auto V* supplies the existing portable cover action and geometry
  boundary, but Gears makes that state the dominant traversal language and joins
  it to mantle, SWAT turns, roadie run and a training sequence.
- *STAR WARS Battlefront II (2017)* also exposes a timed weapon-readiness window,
  but active cooling modifies heat while Gears transfers finite reserve
  ammunition and grades success, perfect and failure with a damage bonus.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-161`, `ACT-164`, `ACT-183`, `ACT-184`, `ACT-199`, `ACT-226`, `ACT-241`, `ACT-341`, `ACT-478` | exact bindings, cover moves, weapons and revive reach are parameters |
| System Behaviour | `SYS-208`, `SYS-215`, `SYS-222`, `SYS-348`, `SYS-369`, `SYS-407`, `SYS-737`, `SYS-749`, `SYS-924` | AI, health, checkpoint and reload bands are parameters |
| Constraint | `CON-262`, `CON-282`, `CON-285`, `CON-326`, `CON-402`, `CON-578` | capacities, geometry and gate order are parameters |
| Information | `INF-073`, `INF-115`, `INF-119`, `INF-125`, `INF-268`, `INF-353` | HUD layout, prompts and reload graphics are parameters |
| Objective | `OBJ-188` | route, final group, transport and successor are parameters |
| Time | `TIM-003` | cadence, quiet interval and timing windows are parameters |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `320` (`GAME-0001`–`GAME-0320`).
- Exact genome matches: none.
- Tied near matches: `GAME-0315` — Halo 3 (`22 / 37 = 0.594595`).
- Supported combination subsets: none.
- Scan date: 2026-09-20.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0315` — Halo 3 | `ACT-008`, `ACT-161`, `ACT-164`, `ACT-183`, `ACT-184`, `ACT-199`, `ACT-341`, `SYS-215`, `SYS-222`, `SYS-348`, `SYS-369`, `SYS-749`, `CON-262`, `CON-282`, `CON-402`, `CON-578`, `INF-073`, `INF-115`, `INF-119`, `INF-125`, `INF-268`, `TIM-003` | Both are original-Xbox campaign packets with direct two-weapon combat, finite ammunition/grenades, pickups, authored groups, ordered gates, checkpoints and a named successor. Halo 3 instead places a rechargeable shield before health, reports moving contacts on a partial Motion Tracker and ends with captive release plus extraction. Gears attaches the body to cover, admits blind fire and ally revival, regenerates the health pool itself, runs Dom autonomously and turns finite-ammunition reload into a visible three-grade risk/reward input before the prison breakout. | Near, `22 / 37 = 0.594595` |

### Preserved research notes

- New genes: `ACT-478`, `SYS-924`, `INF-353` and `OBJ-188`.
- Classification result: `New gene`; no verified combination is expected.
- Evidence and reasoning: ordinary reload, contextual cover and companion AI
  already exist, but no active lower-ID boundary owns the second reload press,
  three-grade finite-ammunition outcome, its visible timing band or this exact
  prison-training terminal.

## Taxonomy impact

- Registry changes: add one Action, one System Behaviour, one Information and
  one Objective boundary; add Gears of War support to compatible traversal,
  attack, switching, reload, grenade, pickup, cover, revive, interaction,
  combat, pickup, downed, checkpoint, companion, health, finite-group,
  equipment, geometry, route, information and live-time genes.
- Taxonomy-change record: none; no earlier definition or signature changes.
- Candidate terms affected: Gears of War, Xbox 360, Marcus Fenix, Dominic
  Santiago, Hammerburst, Bolo Grenade, Crimson Omen, King Raven, `14 Years
  After E-Day`, `Trial By Fire`, Casual and all button labels remain product,
  actor, item, interface, chapter, difficulty or control parameters.

## Negative results

- No original Xbox 360 disc/build, direct control, checkpoint load, save/quit/
  relaunch or successor-save comparison was available. Source-backed checkpoint
  and chapter transitions are not measured persistence equality.
- Squad orders are not admitted: the manual limits them to the squad leader,
  while the bounded prison packet does not establish Marcus's command authority.
  Dom's documented autonomous cover/return-fire behaviour is included instead.
- Chainsaw use, turret operation, COG Tags and the left Combat route are
  available or adjacent but not required by the declared Training terminal.
- Exact timing-band widths, damage-boost value/duration, health regeneration
  delay, ammunition counts and checkpoint fields were not measured and remain
  parameters.

## Delta summary

## New facts

- [Confirmed | Direct | High] The original manual joins contextual body-to-cover
  movement, blind/aimed exposure, quiet health recovery, autonomous squad help
  and a visible three-grade active reload (`GOW-002`–`GOW-007`).
- [Observation | Corroborated | High] The right-hand prison Training route
  carries those rules through fixed lessons and Locust groups into a Raven
  transition to `Trial By Fire` (`GOW-008`–`GOW-010`).

## New genes

- [Observation | Corroborated | High] `ACT-478`, `SYS-924`, `INF-353` and
  `OBJ-188` isolate the timed second press, its graded result, its information
  surface and the complete tutorial-breakout terminal.

## New combinations

- [Observation | Corroborated | High] No new verified combination.

## Taxonomy changes

- [Confirmed | Direct | High] No earlier taxonomy boundary or signature changed.

## New questions

- Which exact checkpoint fields survive an original Xbox 360 save, quit and
  relaunch at the end of the Training route?
- At which later chapter does Marcus first gain directly verified squad-leader
  order authority, and how does that policy interact with autonomous cover AI?

## Next recommended game

- [Hypothesis | Limited | High] `GAME-0322` Diablo II: Resurrected.
- Optimisation criterion: move from continuous cover combat to a current
  remastered action-RPG packet with inventory, procedural layout and retained
  character progression.
- Expected information gain: test remaster/original-rule boundaries, item
  identity, skill allocation and waypoint/quest persistence.
- Backlog impact: `GAME-0322` remains next; no later unit starts in this commit.

## Why this game

- [Hypothesis | Limited | High] Gears of War is a recognisable original-Xbox-
  360 anchor whose smallest complete tutorial makes cover attachment, active
  reload risk and autonomous squad support separately inspectable.

## Research checklist

- [x] original Xbox 360 edition, solo difficulty, route, entry and terminal declared
- [x] original manual and three route sources separate invariant rules from path evidence
- [x] left route, later chapters, co-op, multiplayer and later editions excluded
- [x] direct-play, checkpoint, build and audiovisual limitations disclosed
- [x] complete six-type gene scan performed
- [x] deterministic lower-ID comparison and combination scan completed
- [x] reviewed Ukrainian localisation and bilingual presentation completed
- [x] original artwork and responsive browser checks completed
