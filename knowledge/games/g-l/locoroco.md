---
game_id: GAME-0482
slug: locoroco
game_title: LocoRoco
analysis_status: reviewed
reviewed: 2026-10-02
combination_ids: []
gene_ids:
  action:
    - ACT-519
    - ACT-637
    - ACT-638
  system:
    - SYS-036
    - SYS-037
    - SYS-1259
    - SYS-1260
    - SYS-1261
    - SYS-1262
    - SYS-1263
  constraint:
    - CON-746
    - CON-747
  information:
    - INF-192
    - INF-268
    - INF-457
  objective:
    - OBJ-181
    - OBJ-271
  time:
    - TIM-003
---

# Game: LocoRoco — original PSP first stage

Use the [canonical vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Yellow bodies, berries, shoulder buttons and individual population thresholds are carrier parameters, not genes.

## Analysis scope

- Version / ruleset: original 2006 English-language PSP UMD base game, new-game first ordinary stage, World 1-1. The preserved original English booklet supplies retail controls and ordinary stage rules; contemporary written PSP routes locate the first-stage passages and finish. The exact UMD revision, collision solver, geometry, thresholds and timings were not executed or measured. This is not the downloaded demo, LocoRoco 2, Cocoreccho!, Midnight Carnival or PS4 remaster.
- Structured analysis target: original English-language PlayStation Portable UMD base edition, first ordinary stage; existing `PLAT-PLAYSTATION-PORTABLE`. Other releases remain unaudited.
- Primary decision loop: inspect local terrain and population, tilt the world to roll its soft inhabitants, bump it to jump, divide a large body to pass a narrow opening and hold the reunion command near separated individuals. Contact berries to grow the population, investigate buds and optional routes, gather Pickories and MuiMui, and leave the group still at an eligible local singing event or the goal. Finish with at least one individual; more surviving individuals improve the optional result.
- Entry and exit: choose New in the original English PSP game and begin the first ordinary stage with the initial yellow LocoRoco after the opening/control introduction. End at the first Stage Clear settlement and returned World Map, or abandonment, before entering another stage or Time Attack. This packet includes optional exploration and its credited result, not only a prescribed shortest path. Reproduction must pin the legal UMD, new save, button trace, population, scene, contact events and first map result; the written route is not a measured input trace.
- Included: world tilt, global bounce, commanded division/nearby reunion, live gravity/contact and wind carriage, soft-body clearance, berry-born population growth, local bud activation, contact pickups, population-dependent stationary local events, first-stage control guidance and counters, ordinary clear with retained optional progress, all-twenty clear rewards/unlock eligibility, and real-time motion while unpaused. The optional reward's later use is excluded.
- Excluded: later-stage enemies, burr loss/recovery and zero-population failure rules not demonstrated as part of this first-stage packet; later launchers, machinery, bosses and colour choices; Time Attack play or deadlines; spending Pickories in mini games; Loco House building, editor, wireless sharing, photos, later campaign progression, prototype mood gauges and unimplemented rhythm-boost ideas. Pausing/restarting is ordinary interface context, not a new radial-command or rewind gene.
- Potential scoped modules: a later hazard-bearing ordinary level, Time Attack, each mini game and house/editor construction require their own evidence and packet.
- Direct-play status: no PSP, UMD executable, emulator, save, input recording, screenshot, gameplay video or audio was opened or played. The original manual's searchable text, Sony launch announcement and creator interview were read; two independent contemporary PSP guide authors support the first-stage route and stationary finish. Local PDF retrieval and screenshot inspection were unavailable, so ambiguous OCR button glyphs are not evidence for a numeric input timing. Artwork is an original possible interpretation, not captured level geometry.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| LR-001 | L/R tilt the environment; both shoulder buttons bump it for jumping. Tap Circle divides the body; holding Circle reunites nearby individuals. | Observation | Corroborated | High | P1 Controls/Rolling/Bouncing/Splitting; P2; S1 controls; S2 |
| LR-002 | Soft bodies roll and deform through live physical contact; dividing preserves population but changes geometric access. Reunion is local, not a teleport of every distant individual. | Observation | Corroborated | High | P1 Splitting; P2; P3 retail softness discussion |
| LR-003 | Eating a red berry adds one living LocoRoco; touching/approaching a bud makes a hidden berry grow, separately from consuming it. | Observation | Direct | High | P1 Secrets/Berries |
| LR-004 | First-stage routes contain narrow passages, hidden optional passages, buds, Pickories, MuiMui, wind carriage and a stationary goal event. Their exact coordinates are unmeasured. | Observation | Limited | Medium | S1 ZXC101; S2 W1L1 |
| LR-005 | Eligible local stationary reactions can reveal an optional result; a first-stage hidden MuiMui route requires a sufficiently large population. The published eighteen threshold is route evidence, not a measured universal constant. | Observation | Limited | Medium | S1 ZXC101; P3 retail discovery/waiting |
| LR-006 | A moving local view, population/Pickory feedback and contextual MuiMui instructions support the first stage without exposing every hidden passage or future level. | Observation | Corroborated | Medium | P1 Game Screen/Rolling; S1; S2 |
| LR-007 | Only one LocoRoco is necessary to clear an ordinary stage. Stage Clear records performance, sends found MuiMui to the house and returns to the map; a cleared stage is replayable. | Observation | Direct | High | P1 Finishing a Stage/World Map |
| LR-008 | An all-twenty finish awards stage-specific house parts and enables Time Attack eligibility; these are terminal rewards, not a required ordinary-clear quota or a first-attempt deadline. | Observation | Direct | High | P1 Time Attack/No Miss Clear Bonuses |
| LR-009 | The first-stage goal requires waiting; continued reunion input does not replace that inactivity event. Prototype mood and rhythm-assisted jumping were not shipped. | Observation | Corroborated | Medium | P3 retail waiting and rejected concepts; S1; S2 |

## Basic data

- Release / origin: Sony Computer Entertainment / Japan Studio, original PSP title in 2006. Sony's dated North American launch announcement is 5 September 2006; it is not used as the worldwide first-release date.
- Platform or physical form: original PSP handheld and UMD base game. The remaster-promoting interview explicitly distinguishes the original from its later PS4 edition.
- Mechanical family: `FAM-007` physics and object manipulation. Live motion alone does not establish escalating real-time pressure in this first level.
- Primary sources accessed 2026-10-02:
  - **P1:** [Original Sony English PSP instruction booklet](https://www.gamesdatabase.org/Media/SYSTEM/Sony_PSP/Manual/formated/LocoRoco_-_2006_-_Sony_Computer_Entertainment.pdf), archived searchable text: Controls, Game Screen, Rolling, Bouncing, Splitting, Berries, Finishing a Stage, Time Attack and No Miss Clear Bonuses. It warns that some printed screens can predate final completion. No screenshot-derived geometry claim is made. A search result labelled LocoRoco 2 was rejected rather than silently treated as this booklet.
  - **P2:** [Sony's 2006 North American launch announcement](https://sony.mediaroom.com/2006-09-05-LocoRoco-Rolls-Onto-the-PSP-PlayStation-Portable-System), primary evidence for original PSP, indirect tilt/bump control, growth/division and soft-body physical response. Its whole-product inventory does not place every feature in the first level.
  - **P3:** [Sony's 2017 interview with Tsutomu Kouno and Keigo Tsuchiya](https://blog.playstation.com/2017/05/09/locoroco-creators-on-the-game-that-made-the-world-smile/), retail idle/discovery responses and the distinction between shipped rules, prototype mood and unimplemented rhythmic jump enhancement. PS4 motion-control additions do not transfer to PSP.
- Secondary scope sources:
  - **S1:** [Ben Docherty's original PSP written walkthrough](https://www.supercheats.com/psp/walkthroughs/locoroco-walkthrough06.txt), version 0.40, started 2006, ZXC101 first-stage route. Its fruit numbering conflates population and consumed berries; no exact collectible-coordinate ledger is copied.
  - **S2:** [Talvon's contemporary PSP route](https://gamefaqs.gamespot.com/psp/930044-locoroco/faqs/43443), indexed W1L1 section: narrow splitting passage, wind carriage, MuiMui's wait instruction, growing goal tree and map return. Direct page retrieval was restricted; only the identifiable indexed excerpt was available, so it is corroboration with Limited confidence rather than a full independently inspected route.
- Claim IDs: `LR-001`–`LR-009`. Retail manual claims remain separate from source-limited first-stage placement and thresholds.

## Mechanical decomposition

### Action Genes

- Reuse `ACT-519`: hold L or R to change world angle, indirectly steering rolling bodies; not `ACT-008` direct avatar locomotion or `ACT-097` a discrete gravity-face choice (`LR-001`).
- New `ACT-637`: a distinct global ground-bump command launches its inhabitants, paired with current tilt; not a directly steered avatar or vehicle jump (`LR-001`).
- New `ACT-638`: request geometric division or nearby reunion of a living aggregate. Tap and hold are command variants; the player does not choose army slots, counts or separate unit destinations (`LR-001`, `LR-002`).

### System Behaviour Genes

- Reuse `SYS-036`: integrate soft bodies under gravity, momentum, surface collision, bounce and local wind forces. Exact solver and deformation coefficients remain parameters, not asserted code (`LR-002`, `LR-004`).
- Reuse `SYS-037`: contact with Pickories and found MuiMui credits optional progress while traversal continues. This is not the ordinary goal contact or later spending (`LR-004`, `LR-007`).
- New `SYS-1259`: consuming an eligible berry adds one living individual and increases the aggregate's potential size, rather than adding only score or a life retry (`LR-003`).
- New `SYS-1260`: resolve requested separation and nearby reunion into multiple small bodies or a larger aggregate while preserving represented living population. Reunion cannot recover every distant or already lost individual by declaration (`LR-002`).
- New `SYS-1261`: proximity/contact activates a local hidden bud into a ripe collectible before its separate consumption; reveal and acquisition are independent transitions (`LR-003`, `LR-004`).
- New `SYS-1262`: resolve an eligible stationary group event into its authored local response, such as optional discovery or the growing goal tree. Waiting is causally relevant; exact song duration, musical input grading and universal threshold are not claimed (`LR-005`, `LR-009`).
- New `SYS-1263`: settle a full-population ordinary clear into special parts and replay-mode eligibility, without playing that later mode (`LR-008`).

### Constraint Genes

- New `CON-746`: current physical body form must fit the passage clearance; separating changes that predicate without rewriting level geometry. Not `CON-032` a cell occupant's mutable STOP property (`LR-002`).
- New `CON-747`: a population-gated local event requires its declared living participant threshold. The optional hidden first-stage gate does not make twenty mandatory at the ordinary goal; mere body enlargement without more individuals does not satisfy it (`LR-005`, `LR-007`).

### Information Genes

- Reuse `INF-192`: the moving side-view exposes local support and approach geometry, not all hidden caves or later route geometry (`LR-004`, `LR-006`).
- Reuse `INF-268`: contextual MuiMui control/next-action teaching reveals the current lesson; the finish's instruction to wait is actionable information, not an external walkthrough (`LR-006`, `LR-009`).
- New `INF-457`: population and collected-value feedback plus stage result expose aggregate progress without claiming all secret locations or a deadline. Optional elapsed-time display is not countdown pressure (`LR-006`–`LR-008`).

### Objective Genes

- Reuse `OBJ-181`: ordinary first-stage completion settles optional credited progress and returns to a replayable map. The exact later save/write behaviour was not tested (`LR-007`).
- New `OBJ-271`: aim to finish with the largest available living population. This secondary goal differs from clearing with one, a supplied-population rescue quota and abstract score maximisation (`LR-003`, `LR-008`).

### Time Genes

- Reuse `TIM-003`: while unpaused, bodies, wind and stationary-event timers continue between commands. Waiting is an intentional option, not a turn submission, replay clock or rhythm test (`LR-002`, `LR-009`).

## Reproducible transitions

| Before | Action or event | Bounded resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Body on sloping support | Hold L/R | World angle changes; body rolls through physical resolution | Indirect field control | LR-001, LR-002 |
| Body grounded near an elevated route | Press both shoulder buttons | Ground bump supplies a jump; current tilt affects travel | Separate global impulse | LR-001 |
| Large aggregate at a narrow opening | Tap Circle | Population separates into smaller bodies that can fit | Form changes access, not unit count | LR-001, LR-002 |
| Several separated individuals near each other | Hold Circle | Nearby participants reunite; distant ones are not globally teleported | Local reunion predicate | LR-002 |
| Hidden bud, before berry acquisition | Approach/touch its activation region | Ripe berry appears; later contact consumes it | Activation precedes growth credit | LR-003 |
| Eligible living body contacts a ripe berry | Eat it | One additional individual joins population | Count growth distinct from regrouping | LR-003 |
| Local optional route with Pickories or MuiMui | Reach its pickup | Optional credit persists through ordinary clear | Pickup is not terminal | LR-004, LR-007 |
| Optional stationary population gate | Compare insufficient/sufficient group and wait | Eligible local response occurs only with its threshold met | Local quota, not full-level mandatory quota | LR-005 |
| First-stage wind carrier region | Enter while motion runs | Wind carries separated bodies through authored geometry | Physical travel not player teleport | LR-004 |
| Goal area reached | Stop input and wait instead of repeatedly reuniting | Authored stationary finish grows its tree and closes stage | Inactivity can be the required choice | LR-009 |
| Ordinary clear with a nonzero incomplete population | Accept result | Stage Clear and map return; credited optional result remains | One required versus twenty optional | LR-007 |
| Clear with all twenty | Accept result | Special house-part reward and Time Attack eligibility | Conditional settlement, not later mode play | LR-008 |

These are documentary conditional tests, not measured PSP traces. No exact jump impulse, join radius, song duration, bud radius, stage coordinate or world-save comparison is fabricated.

## Strategic and experiential structure

World tilt moves all exposed bodies; after separation, local geometry can send them along different paths. A larger combined group is easier to keep together but cannot pass every crevice. Berry growth improves the optional living-population outcome while increasing aggregate clearance demands. Hidden buds and routes reward deliberate exploration rather than only forward movement. A player pressing reunion continuously at the finish can obstruct understanding of the instruction to wait. Ordinary completion and full-population rewards remain different evaluations. The first level is not claimed to impose a hard live deadline.

## Replay and variation

The first clear returns to a replayable map with performance feedback. Optional completion can improve independently of ordinary clear; all-twenty completion enables a later time mode, whose rules are excluded. No random level generation, population mood simulation, music-driven jump boost or measured optimal route is asserted. Exact stage geometry and secret event thresholds require a lawful original execution before quantitative claims.

## Adjacent systems and history

The launch announcement describes the complete commercial product, whereas this record admits only the first ordinary level. Sony's retrospective explicitly distinguishes discarded mood/rhythm ideas from retail autonomy and describes later remaster additions. The PSP uses shoulder buttons, not the PS4 controller's added motion input. The manual's broad hazard advice cannot alone prove that a particular enemy or burr is reachable in this first-level route.

## Normalised genome

| Type | Active gene IDs | Carrier parameters |
|---|---|---|
| Action | `ACT-519`, `ACT-637`, `ACT-638` | field tilt, global bump, tap/hold grouping |
| System Behaviour | `SYS-036`, `SYS-037`, `SYS-1259`–`SYS-1263` | physics, pickups, births, regrouping, buds, stationary events, full clear rewards |
| Constraint | `CON-746`, `CON-747` | clearance and local living-population threshold |
| Information | `INF-192`, `INF-268`, `INF-457` | local view, current teaching and group/result feedback |
| Objective | `OBJ-181`, `OBJ-271` | ordinary clear/map return and largest finish population |
| Time | `TIM-003` | unpaused live motion and waiting |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `481` (`GAME-0001`–`GAME-0481`).
- Exact genome matches: none.
- Tied near matches: `GAME-0312` — ASTRO BOT (`5 / 29 = 0.172414`).
- Supported combination subsets: none.
- Scan date: 2026-10-02.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0312` ASTRO BOT | `SYS-036`, `SYS-037`, `INF-192`, `OBJ-181`, `TIM-003` | Both packets combine local physical traversal, optional contact collection and a completed-level map return. Astro directly moves and fights, uses checkpoints and a level-bound Inflate ability; LocoRoco instead tilts/bump-controls the world, changes population-conserving form and grows living individuals through berries. Its stationary local group events and optional full-population reward do not import Astro's enemies or rescue rules. | `5 / 29 = 0.172414`; nearest structural overlap, not equivalent play or inferred lineage. |

## Taxonomy impact

`TAXONOMY_CHANGE_219` admits eleven bounded genes and seven unchanged reuses. The named role review reads the full first-stage scope and partitions eighteen uses, not inferred rarity. No earlier signature, definition, combination or platform identity changes.

## Negative results

- Reject direct-avatar movement/posture, army-slot division, autonomous collision-only numerical merge and one unique gene per colour or berry.
- Reject a full-level compulsory twenty quota, current ordinary deadline, later-stage death/life economy, music rhythm grading and the discarded mood system.
- Reject using the LocoRoco 2-labelled manual result or whole-product feature list as first-stage evidence. Full PDF visual inspection was unavailable; exact geometry is not claimed.

## Delta summary

## New facts

- [Observation | Corroborated | High] PSP field input separates tilt/bump from geometric split/reunion; population growth is consumption, not regrouping.
- [Observation | Corroborated | Medium] First-stage route accounts support waiting at the goal; ordinary one-individual clear differs from the optional all-twenty result.

## New genes

- [Observation | Corroborated | Medium] Eleven bounded genes isolate global bump/group command, birth/regroup/bud/stationary/reward responses, clearance/quota, group feedback and living-population optimisation.

## New combinations

- [Observation | Limited | Medium] No new verified combination; existing proper subsets are recomputed from the complete signature.

## Taxonomy changes

- [Observation | Corroborated | Medium] `TAXONOMY_CHANGE_219`; no earlier boundaries change.

## New questions

- Verify original UMD geometry, optional singing threshold and finish timing, local join radius, exact body/contact/wind response and map/save persistence from a lawful original trace. Do not replace this evidence with remaster rules.

## Next recommended game

- [Hypothesis | Limited | Medium] `GAME-0483` *Oddworld: Stranger's Wrath*, original Xbox, follows acceptance and the Goal stop window.
- Optimisation criterion: move from world-controlled living geometry to a differently controlled bounty encounter on another platform.
