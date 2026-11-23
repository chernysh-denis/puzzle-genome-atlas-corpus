---
game_id: GAME-0559
slug: the-last-guardian
game_title: The Last Guardian
analysis_status: reviewed
reviewed: 2026-11-19
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-048
    - ACT-202
    - ACT-341
    - ACT-535
    - ACT-706
    - ACT-759
    - ACT-761
    - ACT-762
  system:
    - SYS-036
    - SYS-369
    - SYS-407
    - SYS-755
    - SYS-1625
    - SYS-1626
  constraint:
    - CON-746
  information:
    - INF-258
    - INF-268
    - INF-372
    - INF-536
  objective:
    - OBJ-026
  time:
    - TIM-003
---

# Game: The Last Guardian

Use the canonical [vocabulary and signature rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
Barrel counts, button mapping, boy/Trico size, mirror appearance and local
animation delays are instance parameters, not separate genes.

## Analysis scope

- Version / ruleset: original fully released English European PlayStation 4
  campaign, released 7 December 2016, ordinary new-game introduction through
  the first complete cave escape. PS4 Pro footage corroborates the PS4 release
  family; no European executable, installed patch, disc hash or save was
  inspected. This is not the unreleased PS3 design, E3 demo, later VR demo,
  PS5 compatibility execution or a claim of identical regional binaries.
- Primary decision loop: explore with the boy, read the creature's local
  attention, remove accessible restraints and supply reachable food; climb
  Trico to reach otherwise inaccessible places, acquire and aim the mirror,
  use his tail response to open obstructions, then lure him into the flooded
  chamber and ride his autonomous ascent to the cave's exit.
- Entry and exit: first new-game awakening and ordinary control beside chained,
  wounded Trico; include the three opening barrels, both spear removals, collar
  release, adjoining food chamber and mirror alcove, blocked passage, narrow
  ledge, flooded cavern, chain climb, breakable barrel crate, lure, carried
  ascent and final small crawl passage. Finish on the first sunlit exterior
  when Trico rejoins the boy, before solving the first outdoor ruins. This is
  one complete dependency-and-cooperation route, not one selected interaction.
- Reproducible parameterisation: new solo campaign, normal opening equipment,
  no unlocked bonus items, ordinary DualShock controls. Include reachable
  optional cave barrels, but no all-barrel or trophy requirement. No exact
  collision tolerance, AI latency, numerical trust/hunger reserve, random seed,
  drowning deadline or per-field checkpoint rollback is asserted.
- Included: direct running, jumping and swimming; crouched/crawling clearance,
  automatic ledge catches and directed shimmy/pull-up/drop; automatically
  retained climbing on feathers and hanging chain; reachable pickup, carry,
  throw/drop, contextual spear/lever/mirror collection and heavy-crate push;
  live gravity, contact, water-supported movement and destructible barriers or
  crate contents; companion calling, autonomous food attention, wary approach,
  authored feeding readiness, resting and path/pose selection, physical
  carrying without direct mount steering; mirror marking and separate tail
  discharge; body/terrain cues, contextual prompts, narrated current hints and
  remembering the last hint; local authored failure return and cave arrival.
- Excluded: later learned R1-plus-gesture movement commands, armoured enemies,
  capture portals and escape struggles, fear-eye glass, combat petting and
  post-battle spear routines, later blue-fume gates, underwater cooperative
  dives, severed tail, later mirror loss/recovery, other creatures, final
  tower, complete-campaign ending, trophies, death/time ranks and bonus-item
  collection. Ordinary inspection and optional friendly gestures do not
  establish an unseen numerical affection system.
- Potential scoped modules: outdoor eye-obstacle coordination; first guard
  encounter; learned creature orders; cooperative underwater routing; final
  tower escape and campaign-wide optional collection.
- Direct-play status: not conducted. Inspected all sixteen public 320×180-cell
  storyboard sheets at ten-second sampling of Swimming Bird's 23:49
  PS4 Pro-labelled release recording, published 8 December 2016. The sequence
  shows both knockback interludes, barrel handling, collar, mirror, tail
  strikes, flooded cavern, chain/crate, swimming, carried climb and sunlit
  exterior around 21:00–23:00. Sparse stills are not uninterrupted playback or
  direct tests of AI timing, controller ownership, failures or PAL binary
  parity. Contemporary independent written routes corroborate the complete
  packet. No video/audio playback, foreground research window or focus change
  was used; no native console, installed build or personal completion is claimed.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `TLG-001` | The approved target is the full English PS4 release, with European launch dated separately from North America. | Observation | Direct | High | P1 |
| `TLG-002` | Both spear removals and opening food/chain dependencies precede ordinary cooperation; the second removal follows three initial barrels. | Observation | Corroborated | High | S1, S2, V1 |
| `TLG-003` | The boy automatically retains eligible climbing contact without the old held R1 grip or a grip-strength meter. | Observation | Corroborated | High | P2, S3, V1 |
| `TLG-004` | A call requests a response, while food, distance, physical reach and creature attention affect what actually happens. | Observation | Corroborated | High | S1, S2, S4, V1 |
| `TLG-005` | Posture, eyes, gaze, contextual prompts and remembered narrative hints expose local possibilities without an exact AI-state readout. | Observation | Corroborated | High | P2, S3, S4, V1 |
| `TLG-006` | The carried mirror designates a world point; a separate Trico tail discharge destroys compatible obstacles. | Observation | Corroborated | High | S1, S2, S5, V1 |
| `TLG-007` | The flooded route requires reaching the crate, releasing food, attracting Trico and using his autonomous height gain before the boy-only exit. | Observation | Corroborated | High | S1, S5, V1 |
| `TLG-008` | The admitted spatial route has live fall risk and authored checkpoint return; exact restored fields are unverified. | Observation | Corroborated | Medium | S3, S5 |
| `TLG-009` | The terminal is the exterior reunion, not the whole game's final rescue or a complete-barrel tally. | Observation | Corroborated | High | S1, S5, V1 |

## Basic data

- Release / origin: genDESIGN / SIE Japan Studio, published by Sony Interactive
  Entertainment; full PS4 release in December 2016, Europe 7 December and
  North America 6 December. Development origin is not a released PS3 edition.
- Platform or physical form: one-player PlayStation 4, DualShock controller;
  the structured platform registry owns the exact analysed target.
- Puzzle family: physical object manipulation, inventory/fixture dependencies,
  changed traversal topology and asymmetric agent coordination.
- Primary sources:
  **[P1]** [Sony's English European product record](https://store.playstation.com/en-gb/concept/204826),
  platform, released identity and European date, checked 2026-11-19;
  **[P2]** [genDESIGN's staff symposium, Part 4](https://www.gendesign.co.jp/qa_01/interview04en.html),
  final automatic grip/no strength meter, distinction from the E3 controls,
  embodied remembered-hint input and independent creature implementation.
- Secondary sources:
  **[S1]** [Gosu Noob's complete starting cave route, 6 December 2016](https://www.gosunoob.com/the-last-guardian/walkthrough-part-1-cave-starting-area/),
  food, mirror, flooded crate and exit;
  **[S2]** [Prima's release-day opening route](https://primagames.com/news/last-guardian-part-one-free-trico),
  wary feeding, spear and call dependencies;
  **[S3]** [Gamepressure's release-period control/checkpoint account](https://www.gamepressure.com/thelastguardian/controls-and-system-requirements/z79428),
  swim/posture, contextual controls, staged availability and frequent saving;
  **[S4]** [PlayStation Universe's release-period Trico guidance](https://www.psu.com/news/the-last-guardian-tips-and-tricks-how-to-master-trico/),
  attention, response and feeding; later orders are not admitted;
  **[S5]** [Gamepressure's mirror-to-exterior route](https://www.gamepressure.com/thelastguardian/find-the-mirror-and-get-out-of-the-cave/z1942b),
  obstructed passages, fall risk, water, chain/crate and exit;
  **[V1]** [Swimming Bird's PS4 Pro opening recording](https://www.youtube.com/watch?v=1oAJyCd0BFM),
  23:49, published 8 December 2016, inspected as sampled static storyboards.
  S1/S2 independently corroborate the route rather than becoming official rules;
  a contemporary capture does not identify its exact patch or region.
- Claim IDs: `TLG-001`–`TLG-009`.

## Mechanical decomposition

### Action Genes

- Existing: ACT-008, direct ground/jump/swim movement; ACT-048, one reachable
  free barrel pickup, carry and release; ACT-202, direct crouch/crawl posture;
  ACT-341, contextual spear, lever and mirror acquisition; ACT-535, addressed
  companion call without direct control; ACT-706, held heavy-crate movement;
  ACT-759, commands from an automatic authored ledge catch.
- New: ACT-761 for moving over automatically retained climbable surfaces,
  including fur and chain rather than only an edge; ACT-762 for aiming the
  acquired marker toward a world point for the separate creature's discharge.
- Parameters: DualShock triangle/circle/square/cross/R1 mapping, boy and prop
  size, crate path, eligible fur/chain, mark direction and release position.
- Claim IDs: `TLG-002`, `TLG-003`, `TLG-004`, `TLG-006`, `TLG-007`.

### System Behaviour Genes

- Existing: SYS-036, gravity/contact/support and released-object motion;
  SYS-407, persistent companion's autonomous movement and support selection;
  SYS-755, compatible world-object breakage and contained barrels;
  SYS-369, local authored failure recovery without an invented retention table.
- New: SYS-1625 for actual food acquisition/consumption changing authored
  cooperation readiness, separate from carrying or giving a generic order;
  SYS-1626 for the companion's accepted discharge to the held world mark.
- Resolution order: make the addressed action eligible; commit the boy's input;
  let physical and companion response resolve; read the changed local state.
  A call or mirror gesture is not guaranteed to complete in a fixed frame.
- No explicit survival hunger simulation, measured obedience number, hostile
  health pool or freely driven mount is inferred from these observations.
- Claim IDs: `TLG-002`, `TLG-004`, `TLG-006`, `TLG-007`, `TLG-008`.

### Constraint Genes

- Existing: CON-746, the current body must fit the local passage. The boy's
  crouched small-body path and Trico's much larger physical reach differ;
  neither is a fictional key nor permission to pass through solid walls.
- Spears, chain and blocked route are current physical/stateful dependencies
  resolved by the admitted interactions, not separate genes per obstacle.
- Scarce strategic resources: currently reachable food props and tool access;
  no exposed stamina, ammunition, timer or trust budget is claimed.
- Claim IDs: `TLG-002`, `TLG-003`, `TLG-007`.

### Information Genes

- Existing: INF-258, body/terrain feedback for climbing reach and risk;
  INF-268, current authored instruction/narrative hints and their recall;
  INF-372, context-sensitive current-action prompts.
- New: INF-536, visible companion attention/readiness without exact obedience
  values, route omniscience or a deterministic response deadline.
- The camera reveals the local scene; no perspective-law mutation or complete
  visible world state is claimed. A handholding command is not inferred from
  the reused call boundary.
- Claim IDs: `TLG-003`, `TLG-004`, `TLG-005`.

### Objective Genes

- Existing: OBJ-026, connect and reach the designated traversable exterior.
- Success: first sunlit exterior reunion; failure: a lethal fall leads to
  local authored retry. First-spear knockback is a scripted interlude rather
  than proof that healing the creature killed the boy.
- Collection of every optional food barrel or later campaign rescue does not
  become this packet's completion predicate.
- Claim IDs: `TLG-008`, `TLG-009`.

### Time Genes

- Existing: TIM-003. Gravity, water, creature attention and accepted movement
  keep resolving while the boy can move or address a tool/companion.
- Waiting can be useful but is not a discrete turn, an exact obedience timer
  or a fixed pause-until-input rule. Menu pause is not a new temporal genome.
- Claim IDs: `TLG-004`, `TLG-006`, `TLG-007`.

## Reproducible transitions

| Before | Action | Resolution / observed response | What it establishes | Claim ID |
|---|---|---|---|---|
| Wounded Trico, first spear reachable | Approach, climb and pull the spear | Spear is removed and the boy is knocked unconscious in the authored interlude | Progress event is not a failed-run terminal | TLG-002 |
| Wary Trico and a carried barrel | Throw/drop food, then move back | Trico can approach and consume it; blocking close proximity can delay feeding | Offering and actual consumption are distinct | TLG-004 |
| Only two initial barrels consumed | Seek the second spear approach | The opening readiness condition is not yet complete; supply the third initial barrel | No claim that a single barrel finishes taming | TLG-002 |
| Initial feeding and second spear complete, chain attached | Climb the neck and pull the collar lever | Tether is released and autonomous following becomes possible | Tool-like fixture interaction, not a mount control mode | TLG-002 |
| Boy attached to fur or chain | Release ordinary movement input without holding R1 | Attachment does not use the old held grip-strength model | Surface climb differs from stamina-priced gripping | TLG-003 |
| Trico below the high food ledge | Call, climb the creature and transfer to the reachable ledge | Creature pose provides height; the small opening remains boy-only | Asymmetric bodies create the route | TLG-003 |
| Mirror acquired, compatible wooden obstruction intact | Hold the mirror mark on the obstruction with Trico available | Trico discharges from his tail; compatible barrier breaks | Marker holder and attack source are different bodies | TLG-006 |
| Boy has mirror but creature response is unavailable | Keep aiming or reposition/wait | A mark alone does not itself fire from the boy or remove arbitrary geometry | Availability and acceptance remain causal | TLG-006 |
| Flooded-room crate above, food still enclosed | Climb chain and push crate off the ledge | Impact breaks crate and exposes three portable barrels | Physical movement and contained output remain distinct | TLG-007 |
| Trico hesitates above the water | Throw a reachable barrel into the lake | Food attracts him into the water; additional optional food is not a full-game quota | Local lure differs from directly steering a mount | TLG-007 |
| Boy on Trico after the lake lure | Remain attached through the creature's ascent, then transfer | Trico changes available support; boy climbs/crawls through the final aperture | Companion carrying is not mounted steering | TLG-007 |
| Final small passage traversed | Emerge into sunlight and allow exterior reunion | The scoped cave packet ends before first outdoor ruins puzzles | Spatial terminal, not campaign completion | TLG-009 |

## Strategic and experiential structure

- Local decision: determine which body can reach the next prerequisite, whether
  food is actually available and whether Trico is attending to the request.
- Medium-term planning: chain food, contact access, collar release, high ledge,
  mirror and changed barriers into the flooded-room exit route.
- Long-term structure: later tower/campaign systems are outside this genome.
- Common heuristics: read the creature before repeating commands, withdraw
  after an early food offer, use its body for height and mark compatible barriers.
- Failure attribution: missed support is visible; unclear creature readiness
  can make waiting feel like failed input. The record does not invent exact
  response thresholds to hide that ambiguity.
- Player-trust factors: distinguish current-action prompts from complete
  solutions and source-observed cooperation from an exposed obedience meter.
- Claim IDs: `TLG-002`–`TLG-009`.

## Replay and variation

- The authored opening geometry and prerequisite chain recur on a fresh start;
  creature motion, response time and barrel placement can vary locally.
- No procedural cave generator or fixed-seed guarantee is evidenced.
- Several approach/retrieval choices do not erase required feeding and access.
- Ordinary replay can refine physical coordination; full-game collectible or
  trophy cleanup remains a separate question.
- Claim IDs: `TLG-004`, `TLG-007`, `TLG-009`.

## Adjacent systems and history

- Ico supplies an authored call-and-separation counterexample; here the larger
  partner also provides moving traversable height and a remote destructive source.
- Shadow of the Colossus supplies a hostile climb surface with continuously
  held stamina-priced grip; that control contract is not inherited here.
- Moss separates Reader input from directly steered Quill; Trico instead has
  autonomous attention and local willingness rather than a tracked player hand.
- These are structural comparisons, not novelty or lineage proofs.
- Claim IDs: `TLG-003`, `TLG-004`, `TLG-006`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-048`, `ACT-202`, `ACT-341`, `ACT-535`, `ACT-706`, `ACT-759`, `ACT-761`, `ACT-762` | Instance parameters only |
| System Behaviour | `SYS-036`, `SYS-369`, `SYS-407`, `SYS-755`, `SYS-1625`, `SYS-1626` | Instance parameters only |
| Constraint | `CON-746` | Instance parameters only |
| Information | `INF-258`, `INF-268`, `INF-372`, `INF-536` | Instance parameters only |
| Objective | `OBJ-026` | Instance parameters only |
| Time | `TIM-003` | Instance parameters only |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `558` (`GAME-0001`–`GAME-0558`).
- Exact genome matches: none.
- Tied near matches: `GAME-0558` — Moss (`8 / 32 = 0.250000`).
- Supported combination subsets: none.
- Scan date: 2026-11-19.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0558` — Moss | `ACT-008`, `ACT-341`, `ACT-759`, `SYS-036`, `SYS-369`, `SYS-755`, `OBJ-026`, `TIM-003` | Both packets navigate a directly controlled body through authored ledges, physical support, fixture dependencies, breakage and local retry toward a spatial terminal. Moss separately tracks Reader hands/head and constrains stones and wheel braking; this cave uses an autonomous creature, food-mediated readiness and a marker answered by its tail. Neither score establishes identical controls or native checkpoint parity. | Tied near; `8 / 32 = 0.250000` |

### Preserved research notes

- New genes: five additions; seventeen unchanged definitions reused.
- Classification result: `New gene`.
- Evidence and reasoning: automatic surface climbing, food-mediated readiness,
  nonverbal attention and the two-sided discharge remain distinct from the
  shared traversal core.

## Taxonomy impact

- Registry changes: five Active definitions, two Actions, two System Behaviours
  and one Information gene. All previous definitions and signatures unchanged.
- Taxonomy-change record: [TAXONOMY_CHANGE_305](../../../research/taxonomy-changes/TAXONOMY_CHANGE_305.md).
- Candidate terms affected: automatic surface attachment, companion-marked
  discharge, food-mediated readiness and nonverbal attention.

## Negative results

- None as a separate record. Rejected transfer boundaries are documented in
  the taxonomy decision; no external novelty claim is made.

## Delta summary

## New facts

- [Observation | Corroborated | High] The complete cave exit depends on physical
  food, separate creature attention, acquired mirror and asymmetric reachable
  geometry rather than direct two-body control (`TLG-002`–`TLG-007`).
- [Observation | Corroborated | Medium] Local checkpoint return is documented
  but not native-tested field by field (`TLG-008`).

## New genes

- [Observation | Corroborated | High] ACT-761, ACT-762, SYS-1625, SYS-1626 and
  INF-536 isolate the five accepted boundaries, without changing older genes.

## New combinations

- [Observation | Direct | High] None unless the exhaustive canonical
  proper-subset scan proves a previously verified combination.

## Taxonomy changes

- [Observation | Direct | High] TAXONOMY_CHANGE_305 adds five definitions;
  no merge, split, reactivation or existing-game signature change.

## New questions

- Which original PS4 patch and checkpoint fields govern food restoration
  after a lethal fall, and which visible readiness cues reliably predict
  acceptance without exposing exact internal AI state?
- Can a separately bounded later learned-order packet reuse these boundaries
  without treating command repetition as guaranteed creature obedience?

## Next recommended game

- [Hypothesis | Limited | High] Gunstar Heroes, original one-player Mega Drive /
  Genesis rules, GAME-0560 under approved Selection 045.
- Optimisation criterion: alternate modern asymmetric traversal with retro
  run-and-gun weapon composition on a different platform.
- Expected information gain: distinguish combined weapon behaviour from mere
  weapon switching within a complete released stage.
- Backlog impact: eight approved units remain after this unit.

## Why this game

- [Hypothesis | Limited | High] The approved PS4 slot tests complementary
  physical reach and autonomous cooperation without repeating VR hand control.
