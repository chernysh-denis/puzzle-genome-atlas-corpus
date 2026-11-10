---
game_id: GAME-0486
slug: final-fantasy-tactics
game_title: Final Fantasy Tactics
analysis_status: reviewed
reviewed: 2026-10-02
combination_ids: []
gene_ids:
  action:
    - ACT-014
    - ACT-019
    - ACT-651
    - ACT-652
    - ACT-653
    - ACT-654
  system:
    - SYS-004
    - SYS-299
    - SYS-362
    - SYS-1283
    - SYS-1284
    - SYS-1285
    - SYS-1286
    - SYS-1287
    - SYS-1288
    - SYS-1289
  constraint:
    - CON-001
    - CON-011
    - CON-269
    - CON-323
    - CON-752
    - CON-753
  information:
    - INF-119
    - INF-462
  objective:
    - OBJ-029
  time:
    - TIM-001
---

# Game: Final Fantasy Tactics — original PlayStation first Gariland battle

Use the [canonical vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
Job names, weapons, Zodiac signs, panel coordinates and command labels are
parameters, not new genes for every profession or attack.

## Analysis scope

- Version / ruleset: original North American English 1998 PlayStation base game, first Gariland Magic City battle after the Orbonne prologue and Formation setup. Original Square/Sony booklet text and original-PS1 written player guides support the rules; exact disc revision, executable and initial save were not inspected. This is not The War of the Lions, The Ivalice Chronicles, a mod or the whole campaign.
- Structured analysis target: existing `PLAT-PLAYSTATION`, original base edition. Other releases remain unaudited. The authorised publisher link explicitly names a later edition, not the analysed executable.
- Primary decision loop: deploy Ramza and eligible starting allies on allowed panels; when a unit's Speed-fed CT grants an individual Active Turn, choose up to one legal Move and one available Act in either order, or Wait with unused opportunities, then select facing. Coordinate reach, height, directional evasion, healing and fallen-unit recovery against automatically commanded enemies and guest Delita until the battle's required enemies are incapacitated.
- Entry and exit: enter the Gariland deployment screen after the opening narrative and Formation setup; exit when the complete battle resolves into its reward and first world-map state, or Game Over/abandonment. Keep starting Squire/Chemist jobs and equipment, Manual allied control, no additional JP purchases or optional Reaction/Support/Move abilities installed. Record the actual initial roster, levels, Speed, Brave/Faith, birthdays/Zodiac, equipment, learned starting Guts/Basic Skill/Item sets, item stock and deployment. Learned starting commands are eligible only when actually present; no universal random learned-skill list or disputed enemy count is asserted. This is a complete tactical encounter, not one player's turn or the mostly automatic Orbonne introduction.
- Included: fixed vertically addressed panels and occupied endpoints; starting-roster selection within the attack-team cap and allowed deployment region; unit-specific Move/Jump and terrain reach; ordinary weapon attacks and actually learned starting Basic Skill/Guts effects, including damage, possible displacement, stat/status changes and eligible Wish; learned stock-consuming Item recovery; own-CT Speed scheduling, one Move plus one Act in either order, deliberate partial/no-use Wait and final facing; enemy/guest individual automatic orders; zero-health recovery window and local countdown, ordinary permanent loss/remains, protected guest exceptions and Ramza failure; eligible crystal recovery/ability inheritance or chest acquisition before battle ends; action experience, level thresholds, acting-job JP and party spillover; battle rewards and surviving-party recovery; current panel height, actor/CT, legal movement/targets, facing, resources and falling-unit count. Camera changes expose the same geometry rather than altering reach.
- Excluded: later town purchases, hiring and dismissal, JP spending and job changes, newly bought Yell/Accumulate or later chapter abilities, magic cast queues, advanced jobs/equipment, monsters and breeding, special battle victory predicates, random/world-map encounters, propositions, poaching, Deep Dungeon, campaign ending, save-scumming and emulator facilities. An initially learned buff can be used; an unlearned one is not admitted merely because its job permits purchase later. No universal instant revive, automatic collection of every remaining crystal or chest at victory, enemy-team phase, shared Action/Bonus Action pool or real-time input deadline is imported.
- Exceptions and limits: the booklet describes the fallen count as initially two or three; reaching zero is followed by disappearance on the next relevant opportunity, not exactly three player rounds. Guests do not permanently crystallise under the ordinary loss rule. Indexed mechanics sections support CT gain by Speed, threshold at least 100 and end-turn subtraction of 100 for Move+Act, 80 for one, 60 for neither, preserving overshoot with a residual cap of 60; the record does not falsely reset every actor to 0/20/40. Native tie priority, initial rolls, exact hit/push probabilities, initial learned sets, stock and complete successful trace remain unmeasured. The booklet's loose heavy-weapon mobility example is not adopted as an executable weight rule. Height/reach and actual Move/Jump are retained qualitatively. No exact forecast damage or hidden future random roll is asserted.
- Potential scoped modules: Formation's JP purchases/job prerequisites, charged magic, later special objectives and campaign persistence require their own full packets and evidence. Native play could settle the initial state, target previews, tie order and exact fallen countdown without silently changing prior signatures.
- Direct-play status: no original disc, executable, emulator, save, gameplay image/video/audio or input trace was executed or inspected; no direct play or measured successful battle is claimed. Relevant complete original-booklet HTML/OCR battle/status/formation sections and Fritz Fraundorf's original-PS1 guide sections were read. AeroStar CT/evasion/EXP/JP and AstroBlue Item sections were read as indexed excerpts; their inaccessible full guides are not represented as fully read. The Japanese original-game route supports terrain/guest context, not exact North American starting counts. A retrieved seven-page marketing PDF was rejected as non-rule material. Artwork is an original possible tactical scene, not a screenshot or exact Gariland survey.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| FFT-001 | Eligible controlled allies are placed on restricted starting panels before Gariland; Ramza and automatic guest Delita are not interchangeable manual reserve units. | Observation | Corroborated | Medium | P1 deployment; S1 Gariland |
| FFT-002 | Speed-fed individual CT schedules allies and enemies; using fewer Move/Act opportunities preserves more readiness for the next turn. | Observation | Corroborated | High | P1 CT/Wait; S2 CT excerpt |
| FFT-003 | Each Active Turn permits at most one Move and one Act in either order, followed by chosen facing; no second move follows acting. | Observation | Corroborated | Medium | P1 Active Turn; S2/S4 indexed controls |
| FFT-004 | Move/Jump, terrain and vertical panel identity constrain destinations and attack reach; changing battlefield view does not change geometry. | Observation | Corroborated | High | P1 controls/topography; S1 Gariland |
| FFT-005 | Learned/equipped command sets and targets gate action; physical resolution depends on attack parameters, Zodiac compatibility and applicable directional evasion, with command-specific secondary effects. | Observation | Corroborated | Medium | P1 status/actions; S2 evasion; S3 Squire |
| FFT-006 | Eligible restorative commands consume declared item stock or own health for their typed result; Potion heals, Phoenix Down revives an eligible fallen unit, Wish transfers health and Heal removes named statuses rather than restoring HP. | Observation | Corroborated | Medium | P1 Item/death; S1 Guts; S3/S5 |
| FFT-007 | HP zero gives an expiring recovery opportunity before ordinary loss and remains. Protected guests and Ramza terminal loss are explicit exceptions; a nearby eligible unit may take a chest or choose a crystal benefit. | Observation | Corroborated | Medium | P1 death/crystals/Game Over; S2 excerpts |
| FFT-008 | Eligible actions award EXP and current-job JP; level thresholds alter stats, while party JP spillover is distinct from later JP spending. | Observation | Corroborated | Medium | P1 experience/jobs; S2 EXP/JP excerpt |
| FFT-009 | Enemies and guest Delita choose individual legal automatic orders; Gariland victory grants encounter rewards, recovers survivors and returns to the world map. | Observation | Corroborated | High | P1 enemy/guest/clear; S1 Gariland |
| FFT-010 | Current height, active-unit status/CT, legal panels/targets, facing and fallen counts are exposed without a claimed perfect forecast of hidden rolls. | Observation | Direct | High | P1 battle/status/death |

## Basic data

- Release / origin: Square's original PlayStation tactical game; the English North American base edition is the 1998 target, not a modern product's revised terminology or rules.
- Platform or physical form: original PlayStation single-player party combat; existing platform identity, no release-parity claim.
- Mechanical families: `FAM-009` tactical forecast/counterplay and `FAM-015` coordinated agents. Visible reach, orientation and readiness inform party orders; no perfect hidden-roll prediction is claimed.
- Sources accessed 2026-10-02:
  - **P1:** [Original Square/Sony English instruction booklet, complete HTML/OCR reproduction](https://manuals.plus/m/7c36efdfcdba17704ecdad21e92662edc18dda3837db9bcb534a5998d65b0a72), relevant controls, status, deployment, CT/AT, topology, fallen/crystal and Formation sections read. The mirror's webpage title calls it a strategy guide; the reproduced publisher booklet is the primary rule material. OCR is not executable proof, and the mirror is not an independent second source.
  - **S1:** [Fritz Fraundorf's original-PS1 guide, version 5.2, 25 August 1998](https://www.cheatscorner.de/database/ps1/gamefaqs/388-final_fantasy_tactics_faq_strategy_guide_version_5_2.html), initial-party route, Gariland and Squire/Guts sections read. Later upload date is not authorship date. Its first-chapter memory limitation and conflicting other guides prevent an asserted exact enemy count.
  - **S2:** [AeroStar original-PS1 Battle Mechanics Guide](https://gamefaqs.gamespot.com/ps/197339-final-fantasy-tactics/faqs/3876), indexed CT, physical-evasion, EXP/JP and remains excerpts read. Full access was restricted. Exact equations are source-reported, not independently measured; preserve CT overshoot instead of an inaccurate reset simplification.
  - **S3:** [RPGamer original Squire reference](https://archive.rpgamer.com/games/ff/fft/fftguide/jobs/squire.html), original command effects and job-learning distinction read. It does not establish a universal randomly learned initial loadout.
  - **S4:** [PsychoPenguin original-PS1 controls/route](https://gamefaqs.gamespot.com/ps/197339-final-fantasy-tactics/faqs/36930), indexed Move/Act/Wait and Gariland excerpts only. No full-access claim; its enemy count is not adopted over conflicting original accounts.
  - **S5:** [AstroBlue original-PS1 guide](https://gamefaqs.gamespot.com/ps/197339-final-fantasy-tactics/faqs/17354), indexed Chemist Item/Throw Item section only. Learned Item and inventory requirements are retained without importing later guns or Auto-Potion.
  - **S6:** [HJerng original Japanese route reference](https://www.neoseeker.com/finalfantasytactics/faqs/39362-final-fantasy-tactics-b.html), indexed Gariland route context only. Terrain and guest context do not establish the North American initial enemy count, learned abilities or executable parity; no full-guide access is claimed.
  - **P2:** [Official The Ivalice Chronicles publisher site](https://final-fantasy-tactics-the-ivalice-chronicles.square-enix-games.com/en-us), labelled later-edition product destination only, not rules evidence for the original PS1 executable.
- Claim IDs: `FFT-001`–`FFT-010`. No source-code, native timings or gameplay audiovisual is asserted.

## Mechanical decomposition

### Action Genes

- `ACT-014` and `ACT-019` transfer legal selected-piece relocation and targeted declared ability selection. `ACT-651` commits a bounded available starting roster on eligible panels, unlike real-time formation frontage. `ACT-652` relinquishes unused Move/Act opportunities, `ACT-653` chooses the end-turn defensive orientation and `ACT-654` changes view without rule-bearing projection. These are distinct inputs, not one gene per controller button. `FFT-001`–`FFT-005`.

### System Behaviour Genes

- `SYS-004` transfers eligible random outcomes, not an invented seed or deterministic hidden result. `SYS-1283` is Speed accumulation and usage-dependent CT subtraction, not a rerolled-round initiative die. `SYS-1284` resolves the available typed physical/Basic/Guts command effects; equipment, compatibility, direction and secondary-effect identity remain parameters rather than bundled job-specific genes.
- `SYS-1285` applies one declared restorative payment/result transition, separating use of learned Item from passive regeneration or automatic held-item triggers. `SYS-1286` maintains a fallen recovery window, then permanent loss and protected-guest/Ramza exceptions. `SYS-1287` settles spatially acquired remains into the eligible chosen benefit, not all end-battle loot. `SYS-1288` records current-job credit/spillover, not its later expenditure. `SYS-1289` issues each enemy/guest's automatic commands on that actor's turn, not one whole enemy-team phase. `SYS-299` and `SYS-362` transfer ordinary level thresholds and encounter settlement. `FFT-002`, `FFT-005`–`FFT-009`.

### Constraint Genes

- `CON-001` and `CON-011` transfer finite addressed positions and exclusive occupied endpoints; a bridge top and the panel below are different vertical addresses, not proof of forbidden 2D overlap. `CON-323` transfers an available bounded active party; guest deployment is an exception, not an extra controllable reserve.
- `CON-269` applies to learned Basic/Guts/Item ability eligibility, not ordinary weapon Attack. `CON-752` allows one Move and one Act in either order; reject `CON-034`'s movement lock after acting. `CON-753` restricts movement by the actor's Move/Jump and traversable height/terrain. Attack's separate weapon/command reach belongs to its declared resolution parameters. `FFT-001`, `FFT-003`–`FFT-006`.

### Information Genes

- `INF-119` transfers visible own health/resources, attributes and learned build. `INF-462` exposes tactical vertical panels, selected height, current CT/actor, facing, legal reach and fallen count. Reject quantity-bearing hex stacks, a guaranteed future initiative list and exact future random damage. `FFT-010`.

### Objective Genes

- `OBJ-029` transfers incapacitating the finite required hostile group. First-battle completion is not campaign victory, preservation of every ordinary ally or collection of every crystal. `FFT-007`, `FFT-009`.

### Time Genes

- `TIM-001` transfers discrete input and completed automatic resolution before the next accepted command; it does not imply one command for an entire Active Turn. CT and fallen countdown use simulation opportunities, not elapsed real-world seconds during deliberation. Reject a live ATB input deadline. `FFT-002`, `FFT-003`, `FFT-007`.

## Reproducible transitions

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Available roster and allowed starting panels | Commit an eligible attack team | Selected allies occupy legal initial panels; guest remains automatic | Spatial setup and active cap, not deployment anywhere | FFT-001 |
| Actor below CT threshold; no actor ready | Advance the battle scheduler | Speed increments CT until an individual turn is granted | Attribute-fed readiness rather than party rounds | FFT-002 |
| Actor's turn, both opportunities unused | Act on a legal target then Move | Each chosen opportunity is spent once; the other is still available | Either order, not move-then-act lock | FFT-003 |
| One opportunity spent | Wait and select facing | Turn ends; one-use CT subtraction preserves more readiness than both uses | Deliberate tempo tradeoff | FFT-002, FFT-003 |
| Neither opportunity spent | Wait | Smallest ordinary CT subtraction; residual is capped | Not a forced reset to zero or free extra action | FFT-002 |
| High or blocked panel outside Move/Jump legality | Request that destination | It is not admitted as an ordinary reachable endpoint | Geometry and actor mobility matter | FFT-004 |
| Physical attack has an eligible target | Confirm Attack or learned physical command | Declared chance/damage/secondary effects resolve from actor, target and orientation | Illustration is not an exact hidden roll | FFT-005 |
| Learned Potion with stock and legal living target | Confirm Item use | Stock is consumed and bounded health restored | Command healing, not passive regeneration | FFT-006 |
| Eligible Wish and living recipient | Confirm health transfer | Recipient health is restored at the actor's own health expense | Not a Potion inventory debit | FFT-006 |
| Eligible learned Heal and named removable status | Use Heal | Its declared status clears rather than restoring HP | Same word is not the same restorative effect | FFT-005, FFT-006 |
| Fallen ordinary unit before expiry; eligible learned Phoenix Down and stock | Use the item on the valid fallen target | Stock is consumed and the unit returns to positive health | Recovery must precede permanent loss | FFT-006, FFT-007 |
| Fallen ordinary unit survives unrecovered past its countdown opportunity | Scheduler advances | Unit disappears and eligible remains persist; Ramza loss may terminate play | Not BG3 death saves or guaranteed revival | FFT-007 |
| Eligible unit reaches a crystal/chest before battle ends | Select an available benefit | Crystal restores resources or grants an eligible ability; chest transfers eligible item | Spatial within-battle acquisition differs from victory reward | FFT-007 |
| Successful eligible action | Resolve it | EXP and acting-job JP are credited, with declared party spillover; crossed EXP threshold changes level/stats | JP spending is not automatically executed | FFT-008 |
| Last required foe incapacitated | Resolve victory | Encounter rewards and surviving-party recovery lead to first world-map control | Positive terminal for the complete packet | FFT-009 |

## Strategic and experiential structure

Coordinate reachable panels and attack directions without confusing the camera
with geometry. Acting first can preserve a later retreat; declining movement
can bring the same character's next opportunity sooner. A Chemist's learned
recovery and stock compete with attacking, while a falling ally's local count
can require spending a current turn before permanent loss. Delita is helpful
but not another manual action resource. These are source-supported decisions,
not a simulated optimal strategy or measured native success trace.

## Replay and variation

Deployment, chosen available initial commands, hit outcomes and within-battle
growth vary the encounter. Record initial random values rather than importing
a fixed roster seed. Changing jobs or buying additional abilities creates a
different declared packet, not permission to insert the whole campaign.

## Adjacent systems and history

The original booklet distinguishes CT, AT, JP and EXP. They are not four names
for one progress meter. Later-edition translation, convenience features and
marketing do not establish original-rule parity or historical influence from
the corpus's numerical neighbours.

## Normalised genome

| Type | Active gene IDs | Carrier parameters |
|---|---|---|
| Action | `ACT-014`, `ACT-019`, `ACT-651`–`ACT-654` | legal relocation, chosen command, roster deployment, Wait, facing, view |
| System Behaviour | `SYS-004`, `SYS-299`, `SYS-362`, `SYS-1283`–`SYS-1289` | chance, levels/rewards, CT, command effects, recovery, loss/remains, JP, AI |
| Constraint | `CON-001`, `CON-011`, `CON-269`, `CON-323`, `CON-752`, `CON-753` | vertical addresses, occupancy, ability legality, party cap, two opportunities, mobility |
| Information | `INF-119`, `INF-462` | own resources/build, tactical height/readiness/reach/count |
| Objective | `OBJ-029` | required finite foes incapacitated |
| Time | `TIM-001` | discrete commands and automatic simulation resolution |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `485` (`GAME-0001`–`GAME-0485`).
- Exact genome matches: none.
- Tied near matches: `GAME-0176` — XCOM 2 (`7 / 44 = 0.159091`).
- Supported combination subsets: none.
- Scan date: 2026-10-02.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0176` XCOM 2 | `ACT-014`, `ACT-019`, `SYS-004`, `CON-001`, `CON-011`, `CON-269`, `OBJ-029`: selected legal relocation and abilities, chance, fixed occupied panels, ability gates and required hostile defeat. | XCOM 2 coordinates a player squad phase against an enemy phase with its action-point and cover economy, mission concealment and soldier wound/loss settlement. Final Fantasy Tactics instead grants individual Speed-fed CT turns, one Move and one Act in either order, usage-dependent carried readiness, chosen final facing and local fallen countdown/remains. Shared ability legality does not transfer cover, team phases, native starting values or recovery timing. | Near; `7 / 44 = 0.159091`. Full lower-ID scan selects this neighbour, not a platform or genre assumption. |

## Taxonomy impact

`TAXONOMY_CHANGE_223` admits fourteen bounded additions and twelve unchanged
reuses. A named causal-role review covers all twenty-six uses. No earlier
canonical definition, signature, verified combination or platform changes.

## Negative results

- Reject round-rerolled initiative, ordinary weapon weight as a proven jump rule, move-then-act lock, team enemy phase and a single Action/Bonus Action pool.
- Reject exact initial enemy count, universal learned ability stock, every-command HP healing, unconditional guest crystallisation, exactly three player rounds to disappear and automatic acquisition of all remains at victory.
- Reject later-product features, complete charged magic/job/campaign systems, direct-play, exact forecast or measured native timing claims.

## Delta summary

## New facts

- [Observation | Corroborated | Medium] A complete original-PS1 Gariland battle links individual Speed readiness, ordered choices, panel height/facing and recovery opportunities. `FFT-001`–`FFT-010`.

## New genes

- [Observation | Corroborated | Medium] Fourteen additions isolate causal transitions and controls; specific jobs, skills, party size and numerical costs remain parameters.

## New combinations

- [Observation | Limited | Medium] No new verified combination; existing proper subsets are scanned from the accepted signature.

## Taxonomy changes

- [Observation | Direct | Medium] `TAXONOMY_CHANGE_223`; no prior definition or signature mutation.

## New questions

- Establish native initial-state values, tie priority, exact targeting forecast, recovery countdown and a complete success trace before strengthening limited claims.

## Next recommended game

- [Hypothesis | Limited | Medium] None selected. This is unit 9/9 and the approved batch stops after acceptance and its local commit.
- Optimisation criterion: a separately approved next selection should preserve cross-platform and decision-structure diversity.

## Why this game

- [Hypothesis | Limited | Medium] The approved original-PlayStation tactical encounter closes nine distinct platform targets without transferring live town time from Shenmue to discrete CT deliberation.
