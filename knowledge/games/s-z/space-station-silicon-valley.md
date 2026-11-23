---
game_id: GAME-0548
slug: space-station-silicon-valley
game_title: Space Station Silicon Valley
analysis_status: reviewed
reviewed: 2026-11-19
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-052
    - ACT-161
    - ACT-190
    - ACT-610
    - ACT-680
  system:
    - SYS-037
    - SYS-085
    - SYS-755
    - SYS-788
    - SYS-1588
    - SYS-1589
    - SYS-1590
  constraint:
    - CON-426
    - CON-816
  information:
    - INF-529
  objective:
    - OBJ-026
  time:
    - TIM-003
---

# Game: Space Station Silicon Valley

Use the [canonical vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
Evo's condition follows the processor, not a newly healed host. Blue restorative
energy, purple Power Cells and A/B skill readiness are separate quantities.

## Analysis scope

- Version / ruleset: original English North American Nintendo 64 retail,
  US 1.0, ordinary first playthrough of Smashing Start in Euro Eden, 1998.
  The version is the target described by the pinned reconstruction project;
  no cartridge checksum, executable, console or controller trace was used.
  No US 1.1, PAL timing, prototype, Game Boy Color or PlayStation conversion
  is substituted. Start pauses; R changes/leaves the animal; A and B use its
  available skills; the stick moves; C buttons reframe and Z toggles view.
- Structured analysis target: `PLAT-NINTENDO-64`, original North American cart.
- Entry: choose a fresh save slot and the first available level; accept its
  briefing and start when direct control begins in Roger the dog after the
  scripted crash and first occupation. The preceding cinematic is setup,
  not a player-executed possession transition in this packet.
- Primary decision loop: inspect the current body and briefing, navigate to
  energy and an eligible sheep, use the dog's bite to deactivate the target,
  then transfer the single control locus into it. If left outside, steer
  the exposed processor toward a usable host before condition drains away.
  Use the new body's movement, skill feedback and view controls to reach the
  activated exit after the two required objective credits.
- Positive exit: collect restorative energy, occupy a sheep and enter the
  active exit teleporter; accept the completed-level transition and retained
  first-zone progress before playing Have A Nice Day! Do not stop at the
  first bite or first body swap, and do not require all fifteen Power Cells
  or the hidden souvenir to open this ordinary exit.
- Negative exit: zero remaining controlled condition before a clear starts
  the failed-level sequence. Exposed processor decay is admitted; exact native
  delay, transfer radius, damage grace and retry-menu timing are unmeasured.
  Replay Zone restarts the authored zone; no finite life-stock price or free
  health refill from changing hosts is invented.
- Included: direct movement/jumps, camera adjustment, dog bite, ordinary crate
  breakage and energy, deactivated-body eligibility, R transfer/ejection,
  body-specific mobility and commands, retained processor condition, exposed
  decay, finite recovering skill reserves, sheep float and local call response,
  local body/HUD/terminal information, the two-goal exit and clear recording.
- Excluded: the optional fifteen-cell hunt and its banked score, souvenir
  roasting, intentionally triggering Dan's exhaust, out-of-bounds tricks,
  speedrun cutscene skips, other levels/animal species, campaign-wide repair,
  regional equivalence, cheats, save-slot copying/deletion and audio playback.
  Potential modules include a later flock-pen task, collection/souvenirs and
  the final reconstructed robot ruleset.
- Direct-play status: no console, ROM, executable, emulator, save, binary build
  or input playback was used. A publisher-manual transcription, written
  routes and a read-only pinned reconstruction were inspected. N64 stills
  in the illustrated 2019 route were visually checked; its explicitly marked
  GBC and PS1 images were not treated as N64 states. No audio/video was played.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
| --- | --- | --- | --- | --- | --- |
| SSV-001 | The selected original N64 first level starts in the dog. Its ordinary completion requires energy and occupation of a sheep before using the exit; purple Power Cells and the souvenir are optional here. | Observation | Corroborated | High | P1 pp. 5–8, S1 first level, S2, S3 |
| SSV-002 | The controlled dog can move, jump and bite/bark. R leaves or changes the host; ordinary takeover requires a nearby deactivated body, not any visible living animal. | Observation | Corroborated | High | P1 p. 4, S1 basics, S2, S3, R1 input/caller |
| SSV-003 | Changing body changes species movement and A/B commands while retaining Evo's condition. A zero-condition target is not a free refill. The abandoned body remains in the world. | Observation | Corroborated | High | S2, S3, R1 completion and species loading |
| SSV-004 | The exposed processor loses condition with live time; an animal host shelters it from that exposure drain. Energy pickups restore the current condition to its cap, separately from purple Power Cells and skill reserves. Zero condition starts failure. | Observation | Corroborated | High | P1 pp. 6–7, S1, S2, R1 microchip/pickup/results |
| SSV-005 | Sheep movement includes airborne floating. Its Baa call can cause eligible nearby idle sheep to follow; it is not a damaging dog bite or purely cosmetic noise. | Observation | Corroborated | High | S1 animal roles, S3, R1 sheep/leader code |
| SSV-006 | Species skills have separate readiness/power channels, spent by eligible use and restored under the body's rules. No native recharge curve, universal cost or shared health payment is assumed. | Observation | Corroborated | Medium | P1 p. 7, S1 basics, R1 debit/ground sheep recovery |
| SSV-007 | Green condition, blue opponent energy, separate A/B fields, briefing objectives and host information help distinguish current body capabilities and progress. C controls change view without granting a new host or altering world geometry. | Observation | Corroborated | High | P1 pp. 4–8, S1, S2, S3 |
| SSV-008 | Normal world motion, attacks, call/follow and bare-chip exposure continue in real time until pause or an authored interface transition. The exit has a separate active state and proximity admission. | Observation | Corroborated | High | P1, S2, R1 update/input/teleporter |

## Basic data

- Release / origin: DMA Design, published by Take-Two Interactive for Nintendo
  64 in 1998. Only the original US retail ruleset is analysed here; the
  unexecuted target version is distinguished from the reconstruction's date.
- Platform or physical form: Nintendo 64 with the standard controller.
- Puzzle family: live exposure pressure and ordered body/task prerequisites,
  `FAM-010` and `FAM-017`.
- Primary sources:
  - **P1** [Original instruction-book transcription](https://www.world-of-nintendo.com/manuals/nintendo_64/space_station_silicon_v.shtml),
    publisher-authored text preserved by Nick Wright. Printed pp. 4–8 and 10
    cover control, condition, skill power, possession warning, energy versus
    Power Cells, exit activation, terminal information and stage saving.
    The transcription was read; a scan or exact regional booklet was not
    independently authenticated. Its generic claim that every stage has an
    entrance teleporter does not override this stage's scripted crash entry.
- Reconstruction evidence:
  - **R1** [mkst/sssv at exact source commit](https://github.com/mkst/sssv/tree/99f7f418ac01362a7389d07dad57ba590afe8b9b),
    a work-in-progress US 1.0 reconstruction, inspected read-only without
    acquiring a ROM, compiling or asserting a locally reproduced binary match.
    Read `src.us/sssv/animals/evo_microchip.c`, `animals/sheep.c`,
    `level_results.c`, `teleporters.c`, `overlay2_707310.c`,
    `overlay2_739290.c`, `overlay2_76F7D0.c` and `overlay2_78E9F0.c`.
    Active microchip update, pickup cases, transfer completion, species
    loading, sheep following and failure dispatch corroborate transitions.
    The proposed R-target selection and general refill C bodies are inside
    `#if 0` with assembly fallbacks: they are not accepted as compiled proof
    of exact eligibility distances, rates or timing. No seconds-per-tick
    formula is inferred from the visible counters.
- Secondary sources:
  - **S1** [marshmallow's original N64 FAQ](https://gamefaqs.gamespot.com/n64/198727-space-station-silicon-valley/faqs/3530),
    preserved also as the [written guide](https://www.cheatcodes.com/guide/walkthrough-and-guide-space-station-silicon-valley-n64-11748/).
    The two hosts mirror one author and are not counted as independent
    corroboration. First-level energy and sheep completion, body roles and
    independent skill power support the bounded route. Its optional trophy
    recipe is not promoted to an ordinary clear condition.
  - **S2** [Ray Hardgrit's illustrated first-hand N64 route](https://superadventuresingaming.blogspot.com/2019/03/space-station-silicon-valley-n64.html),
    6 March 2019. The first objective, energy receipt, occupied bodies,
    condition retention and sheep exit are documented. Explicit GBC/PS1
    comparison stills and their different presentation are not mixed into
    the selected N64 model. The native N64 stills were inspected.
  - **S3** [PrinceWatercress's written first-stage notes](https://princewatercress.blogspot.com/2026/06/princewatercress-plays-space-station0815733739.html),
    28 June 2026. Only the written notes were read; the embedded video was
    not played. The generic prose reverses C-up/down zoom relative to P1;
    the selected mapping follows P1, without a frame-level camera trace.
  - **S4** [Independent N64 retrospective](https://nintendobound.wordpress.com/2021/06/17/space-station-silicon-valley/),
    17 June 2021. Multi-objective exit structure and distinct animal
    capabilities corroborate the broad loop, not native coefficients.
- Claim IDs: SSV-001–SSV-008.

## Mechanical decomposition

### Action Genes

- Reuse `ACT-008` for embodied traversal, `ACT-161` for the dog's aimed
  bite and compatible crate attacks, and `ACT-610` for view adjustment.
- Reuse `ACT-052` for moving the unique direct-control locus among persistent
  bodies, including the processor and an eligible animal. Former hosts remain
  as inactive world bodies; no second controllable clone is created.
- Reuse `ACT-680` for the acquired sheep's airborne float/steering and
  `ACT-190` for its explicitly commanded local Baa capability. The latter
  has a follow response, so it is not an excluded cosmetic emote.
- Claim IDs: SSV-002, SSV-003, SSV-005, SSV-007.

### System Behaviour Genes

- Reuse `SYS-037` for contact acquisition and mission energy credit,
  `SYS-755` for crate destruction, and `SYS-788` for separate recovering
  skill channels. Exact recovery ordering and amounts are not claimed.
- Reuse `SYS-085` with a declared finite target set of two objective credits:
  energy and sheep occupation. Crediting the final required member activates
  the fixed exit. The target set is not the fifteen optional Power Cells.
- Add `SYS-1588` for body-profile adoption without a free condition reset,
  `SYS-1589` for exposed processor attrition and capped energy restoration,
  and `SYS-1590` for the sheep call's eligible idle-neighbour follow response.
- The sheep is deactivated by ordinary attacks before transfer. This is not
  the universal temporary hostile-result conversion claimed by `SYS-916`.
- Claim IDs: SSV-001–SSV-006.

### Constraint Genes

- Reuse `CON-426`: completion settlement requires both mandatory credits
  and reaching the active extraction area.
- Add `CON-816`: ordinary takeover requires a nearby deactivated eligible
  body. A living sheep does not become controlled just because R is pressed.
  Walking exposed toward a replacement has a condition cost; exact radius,
  direct-hop grace and blocked forms are not measured from inactive C code.
- Claim IDs: SSV-001–SSV-004, SSV-008.

### Information Genes

- Add `INF-529` for body identity, condition/opponent bars, separate skill
  readiness, the briefing's objective credits and host data at a terminal.
  New-animal information is presentation, not permission to possess an
  otherwise ineligible body. No perfect future route is inferred.
- Claim IDs: SSV-006, SSV-007.

### Objective Genes

- Reuse `OBJ-026`: navigate the current controlled actor into the newly
  eligible authored exit. Its mission prerequisites are represented by
  `SYS-085` and `CON-426`, rather than inventing a second goal for each flag.
- Perfect cell collection, trophy roasting and the campaign's rebuilt robot
  are outside this first ordinary-clear objective.
- Claim IDs: SSV-001, SSV-008.

### Time Genes

- Reuse `TIM-003` for live navigation, attack, neighbour movement and exposure.
  Start pauses the game. A deactivated host remains available while the
  bare processor's survival reserve continues to fall during exposed walking.
- Claim IDs: SSV-004, SSV-005, SSV-008.

## Reproducible transitions

| Before | Input or event | Bounded resolution | What it establishes | Claim ID |
| --- | --- | --- | --- | --- |
| The scripted entry has put Evo in the dog | Use the stick and A | Move and jump with that body's ordinary controls | Entry is not a second independently controlled dog | SSV-001, SSV-002 |
| A healing-energy sphere is reachable | Contact it | Acquire energy and credit the first mission target; restore missing condition up to cap | Blue energy differs from purple collection | SSV-001, SSV-004 |
| A compatible crate is in biting reach | Attack until its break threshold | Remove the crate and expose its energy output | Destruction and subsequent contact acquisition are separate | SSV-002, SSV-004 |
| An ordinary sheep is still active | Press R nearby | It is not an eligible ordinary replacement yet | Host availability requires deactivation, not visual selection | SSV-002 |
| The dog faces a reachable sheep | Use B bite until deactivated | Leave the target body available in world space | Attack creates the replacement opportunity | SSV-002, SSV-003 |
| An eligible deactivated sheep is nearby | Use R to change host | Transfer sole control, retain Evo's condition and replace the command/movement profile | A dead target is not a health refill | SSV-003 |
| The dog has no nearby replacement | Leave it with R, then walk as the processor | Leave the old shell in place; exposed condition decreases while travelling | Body separation can turn distance into survival cost | SSV-003, SSV-004 |
| The processor's condition reaches zero before a clear | Allow the failure sequence to settle | End the current level attempt | No spare-life stock or automatic free host takeover is invented | SSV-004 |
| The sheep is airborne | Use its float capability and steer | Change the continuing descent/route under the sheep profile | A host changes mobility, not just visual skin | SSV-003, SSV-005 |
| Eligible idle sheep are nearby | Use the possessed sheep's Baa | Qualifying neighbours follow the caller autonomously | A local call differs from direct control or harmless sound | SSV-005 |
| A skill channel has spent readiness | Stop that spending and meet its recovery conditions | Recover the compatible channel separately from health | Energy spheres are not a universal skill-price currency | SSV-006 |
| Only one required mission credit is complete | Approach the ordinary exit | It does not grant an ordinary completed result | Neither first energy nor first attack alone clears the stage | SSV-001, SSV-008 |
| Energy and sheep occupation are credited | Reach the activated teleporter | Complete the zone and retain the first-stage progress | Optional cells and souvenir are not extra exit keys | SSV-001, SSV-008 |
| Third-person framing obscures the route | Use C view controls | Change the camera without replacing the host or geometry | The manual's zoom map outranks a reversed prose guide | SSV-007 |

These cases reconstruct documented rules; no console session is claimed.

## Strategic and experiential structure

Possession supplies a usable replacement body but does not erase the processor's
condition. The player can deactivate a sheep while protected inside the dog,
then minimise the exposed interval before inhabiting it. The same transfer
changes movement and removes the dog's bite in favour of the sheep's float
and call, so gaining a required host also changes remaining local options.

Mission energy and optional Power Cells look collectible but serve different
state channels. Completing the first energy credit does not settle the stage;
completing the second opens a location that must still be reached. Camera
framing and host information help distinguish those tasks from completionist
collection or later species-specific puzzles.

## Replay and variation

The first stage is authored. Neither a procedural map nor a random host roster
is claimed. R can expose the processor if it leaves without a close replacement.
Replay Zone restores the zone's starting packet; no measured failure-save
rollback, score-loss formula or end-to-end campaign save equivalence is asserted.
Both ordinary task orders are documented; speedrun timing and cutscene skips
are outside the admitted route.

## Adjacent systems and history

Ghost Trick uses stopped core-to-core traversal, with no embodied exposed
processor crossing dangerous space. The Swapper transfers control among live
clones rather than deactivating an animal to adopt its species profile.
The broad control-locus definition transfers, while host eligibility and
condition/profile resolution keep their separate boundaries.

Game Boy Color and PlayStation conversions retain related product names but
are not evidence of matching N64 controls, timing, geometry or objectives.
No known-release parity inventory is inferred from this analysis target.

## Normalised genome

| Type | Active genes | Scoped role |
| --- | --- | --- |
| Action | `ACT-008`, `ACT-052`, `ACT-161`, `ACT-190`, `ACT-610`, `ACT-680` | Movement, locus, attacks, local skill, view and float |
| System Behaviour | `SYS-037`, `SYS-085`, `SYS-755`, `SYS-788`, `SYS-1588`, `SYS-1589`, `SYS-1590` | Acquisition, task set, destruction, recovery, host profile, condition and call response |
| Constraint | `CON-426`, `CON-816` | Completed-task extraction and deactivated local host |
| Information | `INF-529` | Host identity, bars, commands and mission credits |
| Objective | `OBJ-026` | Reach the active authored exit |
| Time | `TIM-003` | Continuing world and exposed condition |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `547` (`GAME-0001`–`GAME-0547`).
- Exact genome matches: none.
- Tied near matches: `GAME-0417` — Sly Cooper and the Thievius Raccoonus (`5 / 24 = 0.208333`); `GAME-0539` — Blast Corps (`5 / 24 = 0.208333`).
- Supported combination subsets: none.
- Scan date: 2026-11-19.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
| --- | --- | --- | --- |
| `GAME-0417` — Sly Cooper and the Thievius Raccoonus | `ACT-008`, `ACT-161`, `SYS-755`, `OBJ-026`, `TIM-003` | Sly uses a continuing thief body with stealth and alarm consequences; Evo must deactivate a local replacement, retain processor condition and adopt a different species profile. | Near, `0.208333` |
| `GAME-0539` — Blast Corps | `ACT-008`, `ACT-610`, `SYS-037`, `CON-426`, `TIM-003` | The selected Blast Corps mission clears a carrier route with its bulldozer and closes through an enabled vehicle; Evo inhabits deactivated bodies, has exposed attrition and must credit energy plus sheep occupation. | Near, `0.208333` |

### Preserved research notes

- New genes: `SYS-1588`, `SYS-1589`, `SYS-1590`, `CON-816`, `INF-529`.
- Classification result: New gene.
- Evidence and reasoning: reusable control transfer, float, skill and exit predicates are retained; exposed-condition survival and dead-host profile adoption require their own boundaries.

## Taxonomy impact

- Thirteen definitions are reused and five are added; eighteen in total.
- Registry changes: five new Active definitions.
- Taxonomy-change record: [TAXONOMY_CHANGE_295](../../../research/taxonomy-changes/TAXONOMY_CHANGE_295.md).
- Candidate terms affected: none.

## Negative results

- none.

## Delta summary

## New facts

- [Observation | Corroborated | High] A replacement body changes commands
  without refilling the condition carried by the exposed processor.

## New genes

- [Observation | Corroborated | High] Five additions separate profile,
  exposure, call response, dead-host eligibility and current information.

## New combinations

- [Observation | Corroborated | High] No new combination is proposed.

## Taxonomy changes

- [Observation | Corroborated | High] `TAXONOMY_CHANGE_295`.

## New questions

- What are the exact native R-eligibility boundary and transfer-time grace?
- Which first-level objective credits are latched after later host changes?

## Next recommended game

- [Hypothesis | Limited | Medium] Full Android Roto Force in
  [Selection 043](../../../research/selection/SEARCH_DEMAND_GAME_SELECTION_043.md).
- Optimisation criterion: finish the alternating platform horizon with a modern mobile arena.
- Expected information gain: wall-relative movement and live firing in a bounded encounter.
- Backlog impact: advance to `GAME-0549`.

## Why this game

- [Hypothesis | Limited | Medium] Body-specific navigation tests whether
  retained processor condition can be separated from acquired host capabilities.
