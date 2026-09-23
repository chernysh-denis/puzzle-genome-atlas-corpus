---
game_id: GAME-0367
slug: mass-effect-2-legendary-edition
game_title: Mass Effect 2 (Legendary Edition)
analysis_status: reviewed
reviewed: 2026-09-23
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-161
    - ACT-164
    - ACT-183
    - ACT-189
    - ACT-190
    - ACT-199
    - ACT-226
    - ACT-232
    - ACT-341
  system:
    - SYS-057
    - SYS-215
    - SYS-297
    - SYS-348
    - SYS-369
    - SYS-379
    - SYS-380
    - SYS-913
  constraint:
    - CON-269
    - CON-282
    - CON-285
    - CON-326
    - CON-668
  information:
    - INF-073
    - INF-115
    - INF-119
    - INF-125
    - INF-148
    - INF-375
  objective:
    - OBJ-155
  time:
    - TIM-003
    - TIM-027
---

# Game: Mass Effect 2 (Legendary Edition)

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Shepard, Soldier,
Adrenaline Rush, Jacob, Miranda, Tali, Veetor, the Collectors, Normandy SR-2,
Paragon and Renegade are carrier parameters, not gene names.

## Analysis scope

- Version / ruleset: the English Xbox One Mass Effect Legendary Edition
  application, released in 2021, running its Mass Effect 2 module at the
  documented launch-era ruleset. This packet does not claim an exact installed
  patch or executable hash. EA documents edition-specific changes to cover,
  ammunition drops and the Paragon/Renegade interface; the original official
  Xbox 360 Mass Effect 2 manual is used only for rules that survive that check.
- Entry: a fresh Mass Effect 2 New Game without an imported save or optional
  Genesis comic, selecting iconic male Commander Shepard (Soldier) and Normal
  combat difficulty. The initial Normandy SR-1 escape and Lazarus awakening
  are included because they precede the fixed Freedom's Progress assignment.
- Primary decision loop: read the current objective, nearby hostiles, typed
  target protection, Shepard and squad status; traverse the authored route;
  take cover, select a legal weapon, aim, fire and reload; pause on the power
  wheel to inspect resistance and issue one ready power per eligible squadmate;
  independently position or target the two squadmates; choose authored dialogue
  and the offered interrupt; then inspect the retained mission and custody
  outcome before receiving ship control and recruitment dossiers.
- Fixed route: escape the damaged first Normandy, follow the Lazarus station
  tutorial, meet Jacob and then Miranda, report to the Illusive Man, travel to
  Freedom's Progress, reach Tali's group, position the squad at the loading-bay
  gate, defeat the shielded and armoured heavy mech, view Veetor's footage,
  choose the Paragon interruption when offered and allow Veetor to leave with
  Tali. Return to the Illusive Man and stop at the first free Normandy SR-2
  control with the initial recruitment dossiers available. The choice is
  fixed for reproducibility, not required by the portable gene definitions.
- Positive terminal: Freedom's Progress is settled, the Collectors are
  identified from Veetor's recording, Veetor's custody choice is recorded,
  Shepard has ordinary Normandy SR-2 control and the first recruitment
  dossiers are available. Jacob and Miranda are supplied companions, not
  newly recruited optional dossiers; Tali is encountered but not recruited
  here. A dossier prompt alone, before returned ship control, is intermediate.
- Negative terminal: Shepard is defeated without a successful checkpoint
  retry, the required heavy-mech encounter or Veetor evidence cannot be
  resolved, or the player stops before the Normandy handoff. Choosing the
  alternative Veetor custody branch is a valid product outcome but fails this
  fixed trace, not the game's general success condition.
- Included: one fixed Soldier preset, ordered prologue and colony gates,
  exploration, interaction and dialogue; contextual cover, ordinary firearms,
  finite thermal clips and reload, live hostile combat, shield/armour/health
  layers and protection-sensitive powers; independent squad position/target
  orders, paused radial power selection, ready/cooldown state, Paragon dialogue
  interrupt and the Veetor custody choice; checkpoint retry, mission settlement
  and first Normandy command. Exact ammunition quantities are not asserted.
- Excluded: save import, custom class, optional Genesis, later dossiers and
  actual optional recruitment, loyalty, romance, research, scanning, probes,
  galaxy travel after first ship control, DLC missions and integrated DLC
  equipment acquisition, optional hack/bypass safes, exhaustive loot, higher
  difficulties, multiplayer, later trilogy campaigns and ending branches.
- Direct-play status: no licensed application, console input trace, save,
  screenshot, video or audio from this packet was obtained or inspected.
  Primary manuals and EA edition notes establish portable rules; two
  independent written routes corroborate the mission sequence. The local
  control model checks admitted transitions, not the game executable.
- Scope rationale: the first Normandy SR-2 handoff is the smallest stable
  terminal joining dialogue consequence, class-aware cover combat, separately
  commanded companions and a successor campaign hub without pretending that
  later recruitment has already occurred.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| ME2-001 | Legendary Edition includes the Mass Effect 2 module on Xbox One; its initial character creator supports a fresh Shepard without import | Confirmed | Corroborated | High | P1, P2, P3 |
| ME2-002 | The iconic fresh Shepard is Soldier in the original manual; Genesis is optional in Legendary Edition | Confirmed | Corroborated | High | P2, P3 |
| ME2-003 | EA changed cover reliability, ME2 ammunition drop frequency and some Paragon/Renegade behaviour in Legendary Edition | Confirmed | Direct | High | P2 |
| ME2-004 | The manual documents contextual cover, shooting, reload, independent squad orders and a command radial that pauses the fight | Confirmed | Direct | High | P3 |
| ME2-005 | Target bars distinguish shields, armour, barrier and health; some disabling or health-affecting powers require resistance removal | Confirmed | Direct | High | P3 |
| ME2-006 | The manual documents thermal clips, power readiness, selected weapons, the dialogue wheel and momentary Paragon/Renegade interrupts | Confirmed | Direct | High | P3 |
| ME2-007 | The mandatory opening moves from SR-1 escape through Lazarus, Jacob/Miranda and the Illusive Man to Freedom's Progress | Observation | Corroborated | High | S1, S2 |
| ME2-008 | At the loading bay, a heavy mech with shield, armour and health follows squad-positioning and cover preparation | Observation | Corroborated | High | S2, S3 |
| ME2-009 | Veetor's footage identifies the Collectors; the player chooses Tali or Cerberus custody and receives a corresponding Paragon/Renegade result | Observation | Corroborated | High | S2, S3 |
| ME2-010 | After the report, the first Normandy SR-2 control and recruitment dossiers become available, without an optional recruit already joining | Observation | Corroborated | High | P3, S2, S3 |
| ME2-011 | The repository control models target protection, paused command selection, the fixed custody branch and the successor-state predicate, but does not execute the game | Observation | Direct | High | V1 |

## Basic data

- Release / origin: BioWare / Electronic Arts, Mass Effect 2 first released in
  2010; Mass Effect Legendary Edition released for Xbox One in 2021.
- Platform or physical form: licensed English Xbox One Legendary Edition,
  Mass Effect 2 module, one local player with a standard controller.
- Puzzle family: tactical forecast and counterplay; real-time system pressure;
  ordered dependency sequencing. The typed protection and paused squad-order
  window distinguish this packet from a generic cover shooter.
- Primary and first-party sources, checked 2026-09-23:
  - **[P1]** [Xbox's Legendary Edition release announcement](https://news.xbox.com/en-us/2021/05/14/mass-effect-legendary-edition-now-available/amp/)
    and [EA's collection page](https://www.ea.com/games/mass-effect/mass-effect-legendary-edition),
    for product and platform identity.
  - **[P2]** [EA gameplay calibrations](https://www.ea.com/ea-play/news/gameplay-calibrations),
    for Legendary Edition cover, ammunition, optional Genesis and
    Paragon/Renegade differences.
  - **[P3]** [official original Mass Effect 2 Xbox manual](https://eaassets-a.akamaihd.net/eahelp/manuals/mass-effect-2-manuals_Microsoft%20XBOX360.pdf),
    for controls, Soldier preset, squad orders, radial pause, protective
    layers, target display, dialogue interrupt and Normandy systems. This is
    a prior-edition primary source, not proof of exact remaster values.
- Independent written route sources, checked 2026-09-23:
  - **[S1]** [GameBanshee prologue route](https://www.gamebanshee.com/masseffect2/walkthrough/prologue.php),
    for the SR-1, Lazarus and assignment order.
  - **[S2]** [GameBanshee Freedom's Progress route](https://www.gamebanshee.com/masseffect2/walkthrough/freedomsprogress.php),
    for Tali, the heavy mech, Veetor, custody and Normandy handoff.
  - **[S3]** [Gamepressure Freedom's Progress route](https://www.gamepressure.com/masseffect2/prologue-freedoms-progress/z923bb),
    for independent loading-bay and Veetor-route corroboration.
- Reproducible control: **[V1]**
  [verify_mass_effect_2_control.py](../../../scripts/verify_mass_effect_2_control.py),
  a local transition model, not an application or gameplay trace.

## Mechanical decomposition

### Action Genes

- ACT-008, ACT-341 and ACT-199 traverse the damaged ship, station and colony,
  operate required doors and collect the first compatible weapon.
- ACT-164, ACT-161 and ACT-183 select a carried gun, aim/fire at a reachable
  hostile and reload from finite thermal clips.
- ACT-226 enters and leaves reachable combat cover. ACT-189 addresses either
  squadmate with a point or enemy target; it does not give both the same order
  implicitly. ACT-190 commits one available Soldier or squad power.
- ACT-232 commits a response or the momentary Paragon interrupt during
  conversation; ACT-341 operates the required evidence and gate fixtures.

### System Behaviour Genes

- SYS-057 moves attacking mechs toward perceived targets. SYS-215 resolves
  live firearms; SYS-297 executes each addressed squad order through movement
  or attack acquisition. SYS-380 applies a selected power's typed effect.
- SYS-348 routes incoming damage through protection and health; SYS-913
  restores Shepard's ordinary shield after a quiet interval. SYS-369 handles
  the authored retry after defeat, not a second positive terminal.
- SYS-379 retains the mission progression, revealed Collector evidence and
  Veetor custody response into successor access.

### Constraint Genes

- CON-269 requires power readiness, legal target and range; CON-668 further
  rejects specified health or disabling effects while compatible enemy
  resistance remains. These are separate from damage-layer resolution.
- CON-282 orders the prologue, colony, report and ship handoff. CON-285
  requires the compatible active weapon and thermal clip; CON-326 requires
  reachable protective geometry before entering cover.

### Information Genes

- INF-073 shows current weapon selection; INF-115 gives partial local hostile
  state through sight and sound; INF-119 shows Shepard health and ability
  readiness. INF-125 shows the current mission gate and route.
- INF-148 exposes offered conversational responses and eligible interruptions;
  new INF-375 exposes typed enemy protection and contextual power suitability
  before commitment. Neither surface predicts a future hidden enemy action.

### Objective and Time Genes

- OBJ-155 completes one authored opening action segment into retained
  successor control: here the first free Normandy SR-2 command state.
- TIM-003 governs ordinary live movement and combat. New TIM-027 pauses that
  clock while the command radial is held, queues eligible choices and resumes
  live resolution when it closes.

## Reproducible transitions

| Before | Action | Bounded resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Fresh no-import entry | Confirm iconic Soldier and follow Joker | SR-1 escape leads to Lazarus awakening | fixed class and ordered opening | ME2-002, ME2-007 |
| Lazarus combat begins | Take the pistol, cover, fire and reload | Mechs fall, route opens and Jacob joins the supplied party | equipment and cover combat | ME2-004, ME2-007 |
| A target retains protection | Inspect target bar and choose a ready power | A health-only disabling effect is ineligible until matching resistance is removed | typed information and legality | ME2-005 |
| A squadmate can receive an order | Address left or right member and a point or target | That member executes the positional or attack order | independent squad command | ME2-004 |
| Combat remains live | Hold the power wheel, queue legal squad powers, release | Simulation pauses for command selection then resumes their resolution | temporal command boundary | ME2-004, ME2-006 |
| Freedom's Progress loading-bay gate is reached | Put squad in cover, survive and defeat the heavy mech | Shield, armour and health are removed in sequence; warehouse opens | layered encounter gate | ME2-005, ME2-008 |
| Veetor's recording is reachable | View it and take offered Paragon interrupt | Collector evidence and the interrupt response enter the dialogue state | authored information choice | ME2-006, ME2-009 |
| Tali requests Veetor | Let him leave with her | A distinct custody result is retained for the report | fixed branch consequence | ME2-009 |
| Mission report is complete | Accept the ship handoff | First Normandy SR-2 control and initial dossiers are available | positive successor terminal | ME2-010 |

## Strategic and experiential structure

- Local decisions: choose cover, current weapon, target resistance to strip,
  one squadmate's position or power, and an offered response.
- Medium-term plan: preserve protection and thermal clips through the colony,
  arrange the squad before the heavy mech, then keep the Veetor evidence and
  custody decision distinct from the later crew-building objective.
- Feedback and trust: target bars, power-wheel availability, squad status,
  objective and dialogue prompts distinguish illegal powers, poor cover,
  a failed encounter and a completed mission. The exact remaster drop rate is
  deliberately not inferred from the original manual.

## Replay and variation

- The fixed trace uses one no-import Soldier and one custody outcome. Other
  classes, appearance, imported continuity, Renegade interrupt or Cerberus
  custody are valid product alternatives but different packets.
- Hostile timing, individual squad positioning and ammunition drops can vary
  without altering the authored terminal. Later recruitment is a separate
  campaign module, not a hidden part of this one.

## Adjacent systems and history

- Gears of War shares contextual cover, direct firearm combat and ordered
  encounter gates but not the paused power radial or a retained conversation
  choice before ship command.
- Fallout: New Vegas shares authored dialogue, equipment, live combat and a
  retained local decision; its Goodsprings packet has character-creation
  allocation and faction settlement, not independently commanded squadmates.
- Deus Ex: Game of the Year Edition shares first-person movement, equipment,
  dialogue and mission gates but not this specific target-resistance and
  squad-command loop.

## Normalised genome

| Type | IDs | Boundary |
|---|---|---|
| Action | ACT-008, ACT-161, ACT-164, ACT-183, ACT-189, ACT-190, ACT-199, ACT-226, ACT-232, ACT-341 | traverse, shoot, equip, reload, command, power, cover and converse |
| System | SYS-057, SYS-215, SYS-297, SYS-348, SYS-369, SYS-379, SYS-380, SYS-913 | live hostiles, squad execution, layered health, recovery and quest result |
| Constraint | CON-269, CON-282, CON-285, CON-326, CON-668 | power, route, weapon, cover and protection eligibility |
| Information | INF-073, INF-115, INF-119, INF-125, INF-148, INF-375 | equipment, threats, status, objective, dialogue and target layers |
| Objective | OBJ-155 | settle the opening into free successor ship control |
| Time | TIM-003, TIM-027 | live combat and reversible command-radial pause |

The packet has 32 genes: 29 reused boundaries and three new ones. Weapon
names, squadmate identities, exact cover objects and custody recipient remain
parameters. The target does not gain a recruitment gene merely because the
first dossiers become available at the terminal.

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `366` (`GAME-0001`–`GAME-0366`).
- Exact genome matches: none.
- Tied near matches: `GAME-0361` — Fallout: New Vegas (`20 / 39 = 0.512821`).
- Supported combination subsets: none.
- Scan date: 2026-09-23.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0361` — Fallout: New Vegas | `ACT-008`, `ACT-161`, `ACT-164`, `ACT-183`, `ACT-199`, `ACT-232`, `ACT-341`, `SYS-057`, `SYS-215`, `SYS-369`, `SYS-379`, `CON-282`, `CON-285`, `INF-073`, `INF-115`, `INF-119`, `INF-125`, `INF-148`, `OBJ-155`, `TIM-003` | Both traverse an authored opening, equip and fire guns, choose dialogue and retain a mission result. New Vegas commits a numeric build, three skill tags and Goodsprings faction settlement; Mass Effect 2 independently commands two squadmates, pauses for powers, reads typed protection and settles Veetor custody before ship control. | Near, `0.512821` |

### Preserved research notes

- New genes: three Active boundaries isolate the protection-legality, target-display
  and held-radial temporal decisions; twenty-nine earlier genes transfer
  without semantic change.

## Taxonomy impact

- TAXONOMY_CHANGE_106 adds CON-668, INF-375 and TIM-027 without modifying an
  earlier signature or lifecycle.
- Earlier genes receive a carrier evidence reference only where their
  definitions fit. No combination is added from one new carrier alone.

## Negative results

- The original Xbox 360 manual is not treated as an exact Legendary Edition
  patch manifest; EA's edition-specific changes override its drop and cover
  tuning. No Xbox One executable or audiovisual trace was inspected.
- Tali is encountered but not recruited; Jacob and Miranda are supplied.
  Future dossier recruits are not credited to this completed unit.
- Optional hacking, planet scanning, research, later missions and DLC are not
  causal prerequisites of the first Normandy handoff.

## Delta summary

## New facts

- The bounded opening reaches retained Normandy command only after the
  Freedom's Progress evidence, custody choice and report.
- Protection typing governs the usefulness and eligibility of squad powers,
  and a held radial creates a real tactical pause inside live combat.

## New genes

- CON-668 — protected target layers gate disabling power effects.
- INF-375 — expose typed target protection before power selection.
- TIM-027 — pause live combat while selecting radial squad commands.

## New combinations

- None; a single new carrier does not establish a recurring proper subset.

## Taxonomy changes

- One additive taxonomy decision; no rename, merge, deprecation or earlier
  game-signature rewrite.

## New questions

- Direct play could pin a specific Xbox One patch/build and check the exact
  opening prompt sequence and post-choice state. A later separate module can
  compare recruitment and loyalty once those missions actually occur.

## Next recommended game

- GAME-0368 Dead Rising, the next reserved one-game unit.

## Why this game

- It tests whether a live shooter can temporarily pause for tactical orders
  while dialogue and an authored mission choice persist into a new campaign
  control state, without conflating future recruitment with current crew.

## Localisation review

- The canonical English scope and claim ledger were frozen before Ukrainian
  presentation. Names and literal interface labels are retained only where
  they identify the source rule or product. All new Ukrainian field groups
  and routed audit candidates are reviewed in this unit's acceptance record.
