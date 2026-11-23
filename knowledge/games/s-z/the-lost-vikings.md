---
game_id: GAME-0553
slug: the-lost-vikings
game_title: The Lost Vikings
analysis_status: reviewed
reviewed: 2026-11-19
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-052
    - ACT-087
    - ACT-131
    - ACT-161
    - ACT-164
    - ACT-190
    - ACT-199
    - ACT-341
    - ACT-648
  system:
    - SYS-036
    - SYS-112
    - SYS-215
    - SYS-222
    - SYS-369
    - SYS-755
    - SYS-932
    - SYS-1600
    - SYS-1601
    - SYS-1602
  constraint:
    - CON-175
    - CON-210
    - CON-820
  information:
    - INF-073
    - INF-124
    - INF-179
    - INF-317
  objective:
    - OBJ-022
  time:
    - TIM-003
---

# Game: The Lost Vikings

Use the canonical [vocabulary and signature rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
Three named Vikings, four slots, three health dots, key colours and stage code
are parameters rather than separate genes.

## Analysis scope

- Version / ruleset: original English North American Super Nintendo retail
  rules, catalogue identity SNS-LV-USA, one player and ordinary controller,
  complete spaceship level 3, password `TLPT`. The US catalogue dates it to
  April 1993; Blizzard retrospectives disagree between 1992 and 1993, so this
  record does not certify an exact first-release day or resolve that history
  by treating a copyright date as a release date. The selection's 1992 label
  was an initial expectation, not authenticated binary provenance.
- Primary decision loop: inspect the current corridor, threats, switches,
  keys and each Viking's health/inventory; choose the persistent body with the
  required innate verb, directly move it, operate a fixture, trade/use an item
  or change Olaf's shield mode; preserve useful positions and shield support
  while switching to another body; reunite all three living Vikings at EXIT.
- Entry and exit: enter the normal `TLPT` password, or reach that same level
  through ordinary campaign order. Begin with the three Vikings at the first
  elevator, the manual's three health points each and empty inventories.
  Complete both breakable walls and arrow-button barriers, the teleporter
  and red-key descent, second elevator, shield-assisted yellow-key platforms,
  yellow gate and final combat corridor. Include the optional reachable
  wipeout bomb as a carried alternative, not a mandatory kill-all objective.
  Positive terminal is all three alive at EXIT and acceptance of the next
  level/password `GRND`; stop before its live route. One survivor arriving
  alone, one opened gate or an optional enemy defeat is not completion.
- Failure and retry: damage persists within the level; zero health for any
  required Viking makes the whole exit condition unattainable. The world may
  still be explored with survivors; death does not imply an instantaneous
  party reload. START, GIVE UP?, YES restarts the same level and revives the
  trio; a stuck position may also justify that chosen retry. Password entry
  restarts a level, not a saved mid-stage snapshot. Exact native damage,
  off-screen update rules, fall thresholds and controller frame windows were
  not measured. No owned cartridge, native save or replay was tested.
- Included: direct movement, Erik's jump and running wall ram, Baleog's sword
  and bow, Olaf's retained forward/overhead shield modes, frontal eligible
  projectile rejection, overhead ally support and slower directed descent;
  one active body with two retained non-following bodies; ladders and
  direction-controlled authored elevators; arrow-triggered mechanisms;
  co-located fixed-pad transport; red/yellow carried keys and matching locks;
  four item slots per Viking, contact pickup, selected-item use, nearby
  inventory transfer and the optional screen-wide bomb; local combat, three
  separate health pools, chosen level retry and password successor; HUD,
  local field and fixed '?' instructions. No jump is granted to Olaf or
  Baleog merely by placing them on a shield.
- Excluded: two-player master-camera handoff, Genesis bonus stages or
  three-player co-op, PC/GBA controls, Blizzard Arcade Collection Definitive
  Edition, wrapper rewind/save-anywhere, later eras, gravity boots, flaming
  arrows, extra armour, food not supplied in this declared level, campaign
  ending, speedrun camera/door/teleport glitches and exact projectile or AI
  equations. Shared-input clones and autonomous squad destination orders are
  not the single-player control model. A rear or unsupported attack is not
  granted universal shield immunity.
- Reproducible parameterisation: select one player and the original SNES
  `TLPT` route without imported inventory or cheat modifiers. Record each
  body's position, health, shield posture, active-control locus, four item
  slots, target button, wall/gate state, occupied pad, key ownership and
  three-actor EXIT condition. Use either ordinary Baleog combat or the
  available bomb where its screen predicate is satisfied; do not equate
  optional upper-platform clearance with compulsory progression.
- Potential scoped modules: one later gravity-boot level, the original
  two-player camera protocol, Genesis extra content and the 2021 Definitive
  Edition require separate evidence and entry/terminal contracts.
- Direct-play status: documentary reconstruction only. Read the US booklet
  transcription, visually inspect the original English UK booklet's relevant
  controls/items/role spreads, and cross-check the separate Nintendo Gateway
  executive summary rather than mislabelling it as the complete booklet.
  The publisher's retrospective describes roles and the abandoned auto-follow
  design. The SNES-labelled stage guide is available as indexed text; its
  challenged direct page and blocked GameFAQs body were not bypassed. Four
  public static storyboard sheets at ten-second sampling cover TLPT and its
  GRND handoff. No video/audio stream, native input, foreground window or
  focus change was used; the recording's ROM/region/patch is unauthenticated.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
| --- | --- | --- | --- | --- | --- |
| `LV-001` | Original SNES and the later multi-version Definitive Edition are distinct targets; this record prescribes one-player English SNES rules. | Observation | Corroborated | High | P1–P4, S3 |
| `LV-002` | L/R changes the direct-control body while the other two remain present; the released design has no automatic following. | Observation | Corroborated | High | P1–P3, V1 |
| `LV-003` | Erik jumps/rams, Baleog uses sword/bow and Olaf changes shield modes; overhead shield permits ally support and slower descent, not a new jump for every member. | Observation | Corroborated | High | P1, P2, S1, V1 |
| `LV-004` | Each Viking starts a level at three health with no items; all three must reach EXIT alive, and chosen Give Up revives/restarts the level. | Observation | Corroborated | High | P1–P3, V1 |
| `LV-005` | Each inventory has four slots; contact picks up into available capacity, nearby members may trade and X uses the selected item, including a same-colour key or screen-wide smart bomb. | Observation | Corroborated | High | P1, P2, P4, V1 |
| `LV-006` | TLPT combines elevator/ram/arrow buttons, co-located pad transport, Olaf's red-key descent, Erik's shield boost to the yellow key and all-three exit. | Observation | Corroborated | High | S1, S2, V1 |
| `LV-007` | Fixed '?' controls disclose local rules; the HUD shows each member's health and carried items, and ordinary live play pauses for START/SELECT. | Observation | Corroborated | High | P1, P2, V1 |
| `LV-008` | New-level passwords restore entry progress rather than a mid-level item/position snapshot; GRND follows TLPT. | Observation | Corroborated | High | P1, P2, S1, V1 |
| `LV-009` | Retrospectives report 1992 and 1993 differently; the US catalogue lists April 1993. Exact first-release dating remains unresolved here. | Observation | Conflicting | Medium | P3, P5, S3 |
| `LV-010` | A booklet, typed transcription and sparse frames cannot certify native executable, ownership, exact timings, damage values or region parity. | Observation | Direct | High | R1 |

## Basic data

- Release / origin: Silicon & Synapse / Interplay. Original SNES history is
  reported as 1992/1993; selected North American catalogue entry is April
  1993, without a certified day. See LV-009 rather than silently merging dates.
- Platform or physical form: `PLAT-SUPER-NINTENDO`, one-player original retail
  rules; the structured analysis target owns the chosen platform/edition.
- Mechanical families: physics and object manipulation; real-time system
  pressure; inventory/fixture dependencies; world topology and perspective.
- Primary artefacts and creator material, checked 2026-11-19:
  - **P1:** [SNS-LV-USA booklet transcription](https://www.world-of-nintendo.com/manuals/super_nes/lost_vikings.shtml),
    printed pp. 6–15 and 17–22. This is Michael Steele's typed presentation
    of Interplay's text, not a newly authenticated cartridge or physical book.
  - **P2:** [Original English UK booklet scan](https://snolli.fr/dwl/gamelist/docs/The%20lost%20vikings.pdf),
    visually read printed pp. 5–14 and 17–24. The shared documented rules are
    corroboration, not a claim of NTSC/PAL binary or timing equivalence.
  - **P3:** [Blizzard's role/design retrospective](https://news.blizzard.com/en-us/article/23609765/the-lost-vikings-and-how-we-learned-to-love-multiplayer-puzzles),
    for role interaction, all-three escape, abandoned auto-follow and the
    original/Definitive distinction. Its broad "any attack" shield language
    is bounded by the original manual's eligible-facing/contact exceptions.
  - **P4:** [Nintendo Gateway executive game summary](https://snescentral.com/1/0/1/1019/pdf/lostvikings.pdf),
    dated 1999-08-26, controls and trade/password corroboration only. This
    short document is not the original full instruction booklet.
  - **P5:** [Blizzard Arcade Collection announcement by Blizzard](https://blog.playstation.com/?p=346453),
    retrospective 1993 dating and modern collection context, not original
    cartridge proof or a guarantee of current store availability.
- Route/catalogue material:
  - **S1:** [StarBoy91's SNES Stage 3 record](https://starboy91.blogspot.com/2013/01/starboys-walkthrough-lost-vikings-snes_27.html),
    2013-01-27; inspected indexed text, direct page challenge not bypassed.
    It identifies both keys, optional wipeout bomb and the shield boost.
  - **S2:** [Archived Level 3 route](https://www.cheatbook.de/wfiles/thelostvikings.htm),
    an explicitly PC-labelled archive. Only its corroborating route order is
    used; its platform label does not certify SNES controls or parity.
  - **S3:** [SNES Central cartridge catalogue](https://snescentral.com/article.php?id=0446)
    for SNS-LV-USA and its separately listed revision, and
    [MobyGames release catalogue](https://www.mobygames.com/game/1547/the-lost-vikings/releases/)
    for the North American April 1993 entry, not a privately checked ROM hash.
  - **V1:** [Taramoor's SNES-labelled playthrough](https://www.youtube.com/watch?v=D1qR_lYi-38),
    four 320×180-cell storyboard sheets covering 13:30–19:20 in ten-second
    steps: TLPT begins near 14:00; first elevator, ram, arrow button and pad;
    red key/return around 15:00–16:10; second corridor and elevator; shield
    boost/yellow key around 16:50–17:30; final corridor and reunion; GRND
    appears near 18:40. Border/face-camera overlays are not game mechanics.
    The displayed inventory and optional route are not proof of a ROM build.
  - **R1:** limitations above; no game binary, emulator, save-state, audio or
    native video stream was opened. Genesis TAS/modded Ragnarok/Definitive
    videos were not substituted for the selected original rules.
- Claim IDs: LV-001–LV-010.

## Mechanical decomposition

### Action Genes

- Reuse `ACT-008` for walking, ladders and Erik's legal jump; `ACT-052` for
  control transfer without removing other bodies; `ACT-190` for the selected
  body's innate ram or shield toggle, not a newly assigned Lemming role.
- Reuse `ACT-161` for Baleog's ordinary sword/bow strikes; `ACT-190`
  covers Erik's running wall ram and Olaf's shield toggle. Ordinary tool
  attacks remain outside ACT-190's boundary rather than being counted twice.
- Reuse `ACT-341` for local button/hint and pad operations, `ACT-087`
  for selected keys at matching fixtures, `ACT-164` for selected carried item,
  `ACT-199` for reachable compatible inventory transfer and `ACT-131` for
  optional smart-bomb expenditure. Ordinary sword/bow attacks are the
  role-specific command parameters; no cooldown or ammunition pool is invented.
- `ACT-648` covers held Up/Down lift travel with the controlled body aboard.
  The non-damaging arrow-target fixture activation is recorded by ACT-341
  with ranged reach; ACT-161 remains the ordinary damage-directed weapon
  boundary, not a claim that every prop is damageable.
- Claim IDs: LV-002, LV-003, LV-005–LV-007.

### System Behaviour Genes

- Reuse `SYS-036` for gravity/contact, `SYS-112` for accepted
  key/button barrier changes, `SYS-215` for live enemy/projectile damage and
  defeat, `SYS-222` for inventory contact pickup, `SYS-369` for chosen
  authored level-origin retry, `SYS-755` for eligible rammed-wall destruction
  and `SYS-932` for passive eligible frontal projectile rejection while the
  shield is forward. The lift is controlled by occupied-platform ACT-648,
  not the autonomous switch-directed platform SYS-065.
- Add `SYS-1600` for the overhead shield's retained walkable ally support,
  `SYS-1601` for its slower controllable falling mode and `SYS-1602` for
  activation transporting only eligible bodies currently occupying a pad.
- Bomb range is the current rendered screen, a declared target-set parameter
  of `SYS-215`, not a claim of killing every enemy in the whole level.
- Resolution order: check active body's verb and local context; process
  input/movement; resolve contact, attack/trigger or item operation; preserve
  other bodies and state; continue live world resolution except explicit
  pause/inventory mode; settle all-three EXIT or choose a failed/stuck-level
  restart. Native same-frame and off-screen update order remain unverified.
- Claim IDs: LV-002–LV-008, LV-010.

### Constraint Genes

- Reuse `CON-210` for four actor-local inventory slots and compatible capacity.
  Nearby transfer additionally uses the reach parameter of `ACT-199`;
  inventories are not one global pool. `CON-175` represents persistent health
  and the declared critical-actor threshold: any dead Viking prevents whole
  level success, although survivors need not disappear immediately.
- Add `CON-820` for innate identity-bound movement/tool verbs. Neither
  inventory transfer nor changing control grants Baleog or Olaf Erik's jump.
- Claim IDs: LV-002–LV-005.

### Information Genes

- Reuse `INF-073` for slots/selected items, `INF-124` for the three bodies'
  health/status, `INF-179` for the current field and `INF-317` for fixed
  authored '?' instructions. No complete off-screen enemy roster or future
  solved route is exposed.
- Claim IDs: LV-005–LV-007.

### Objective Genes

- Reuse `OBJ-022`: every one of the three required living controlled bodies
  must reach the fixed exit. This is not a minimum rescue quota, one leader
  leaving alone, all-enemy extermination or the whole homecoming campaign.
- Claim IDs: LV-004, LV-006, LV-008.

### Time Genes

- Reuse `TIM-003`: ordinary body, projectile, combat and movement choices
  resolve in real time, with explicit START/SELECT pause exceptions.
  Switching bodies does not synchronise their input, create a turn queue or
  supply player-controlled rewind. No global stage deadline is inferred.
- Claim IDs: LV-002, LV-006, LV-007.

## Reproducible transitions

| Before | Action | Resolution | Distinction | Claim ID |
| --- | --- | --- | --- | --- |
| Erik is selected; Olaf waits with shield overhead | Switch to Erik after positioning Olaf | Olaf's body/posture remains a raised surface for Erik | Control transfer is not morphing or auto-follow | LV-002, LV-003 |
| Erik faces an eligible wall without adequate run-up | Retry the running ram with a longer approach | Accepted ram breaks the wall and opens the corridor | A wall is not removed merely by switching to Erik | LV-003, LV-006 |
| Barrier blocks a reachable passage; target lies beyond it | Use Baleog's arrow on the button | Linked barrier changes and the trio may pass | A remote shot differs from touching a local switch | LV-003, LV-006 |
| All three occupy a transport pad | Activate it | Present eligible bodies arrive at its authored destination | Not global regrouping of absent actors | LV-006 |
| Olaf leaves a ledge with shield overhead | Steer the descent toward the red key | Slower fall permits that landing | No new upward jump or aircraft parachute | LV-003, LV-006 |
| Olaf stands below the yellow-key platforms | Raise shield; switch to Erik and jump from it | Erik gains a higher supported launch point | Other bodies do not acquire his jump | LV-003, LV-006 |
| Selected red key is at the red lock | Use the carried key | Matching route gate opens | Colour/fixture compatibility matters | LV-005, LV-006 |
| Holder is near another Viking with available capacity | Transfer the selected item | Ownership moves to that actor's slots | No remote shared inventory or transferred innate ability | LV-005 |
| Smart bomb carried; some enemies are currently on screen | Use that one item | Current-screen enemies are destroyed; the item is spent | Not universal level clearance or a mandatory exit quota | LV-005 |
| One required Viking has died | Reach EXIT with the other two | Whole-level success remains impossible | No permitted partial rescue | LV-004 |
| A required death or irrecoverable position prevents completion | Choose START, GIVE UP?, YES | Same level restarts with the trio revived | Not an automatic in-place resurrection or mid-level save | LV-004, LV-008 |
| Two living Vikings wait at EXIT | Bring the third and accept the handoff | GRND becomes the next level | Whole-party conjunction settles progression | LV-004, LV-008 |

## Strategic and experiential structure

- Local decision: leave a defender safely oriented before controlling the
  shooter or runner; do not move the supporting body out from under a climb.
- Medium-term planning: keep keys with an actor who can reach the matching
  lock, regroup for lifts/pads, and choose between shield-backed combat and
  spending the optional screen-wide bomb.
- Long-term structure: preserve all three lives through this level; password
  progression is not a carried cross-level inventory economy.
- Failure attribution: local health, shield direction and geometry explain
  many failures, but exact collision and off-screen schedules are unmeasured.
- Player-trust factors: chosen level retry permits recovery from a dead member
  or a stuck arrangement without claiming rewind or arbitrary save states.
- Claim IDs: LV-002–LV-008, LV-010.

## Replay and variation

- The authored level is fixed; routes, staging positions, item ownership,
  optional bomb use and combat timing may vary. No procedural layout is claimed.
- The named route demonstrates all three roles rather than proving one unique
  solution or a globally optimal time. Claim IDs: LV-003–LV-008.

## Adjacent systems and history

- The original creators describe a Lemmings-inspired many-agent concept that
  became three directly controlled specialists; planned auto-follow was not
  shipped. This is historical evidence, not an assignment-based genome.
- Direct-control persistence differs from The Swapper's synchronized clone
  inputs; a protective teammate is not an Ico-style dependent follower.
- Claim IDs: LV-002; P3 and unchanged cited gene boundaries.

## Normalised genome

| Type | Active gene IDs | Parameters |
| --- | --- | --- |
| Action | ACT-008, ACT-052, ACT-087, ACT-131, ACT-161, ACT-164, ACT-190, ACT-199, ACT-341, ACT-648 | Body, role channel, selected item, target and transfer reach |
| System Behaviour | SYS-036, SYS-112, SYS-215, SYS-222, SYS-369, SYS-755, SYS-932, SYS-1600, SYS-1601, SYS-1602 | Gravity, lifts, gates, combat, pickup, retry, shield and pads |
| Constraint | CON-175, CON-210, CON-820 | Critical survival, four slots and innate actor verbs |
| Information | INF-073, INF-124, INF-179, INF-317 | Inventory, health, field and placed instructions |
| Objective | OBJ-022 | All three alive at EXIT and next-level handoff |
| Time | TIM-003 | Ordinary live play, explicit pause/inventory exceptions |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `552` (`GAME-0001`–`GAME-0552`).
- Exact genome matches: none.
- Tied near matches: `GAME-0259` — Dead Space (2023 remake) (`14 / 50 = 0.280000`).
- Supported combination subsets: none.
- Scan date: 2026-11-19.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0259` — Dead Space (2023 remake) | `ACT-008`, `ACT-131`, `ACT-161`, `ACT-164`, `ACT-190`, `ACT-199`, `ACT-341`, `CON-210`, `INF-073`, `SYS-112`, `SYS-215`, `SYS-369`, `SYS-755`, `TIM-003` | Both directly traverse authored corridors, use carried items, change stateful fixtures, fight live hostiles, destroy eligible obstacles and retry failed routes under inventory limits. The selected Dead Space New Arrivals packet has one Isaac, finite Plasma Energy, regional dismemberment, Stasis, power allocation and a retained Medical handoff. TLPT instead keeps three indispensable bodies with fixed verbs, shields as support/descent tools, local pad transport, two coloured keys and an all-three exit. Instant restorative versus smart-bomb effects and intra-inventory versus nearby-member transfers remain parameters; genre or setting is not the score. | Near, `0.280000` |

### Preserved research notes

- New genes: SYS-1600, SYS-1601, SYS-1602 and CON-820.
- Classification result: New gene.
- Evidence and reasoning: role identity, overhead support/descent and fixed
  pad occupancy extend existing body-switch, inventory and live-route rules.

## Taxonomy impact

- Registry changes: four new Active definitions, no earlier mutation.
- Taxonomy-change record: [TAXONOMY_CHANGE_299](../../../research/taxonomy-changes/TAXONOMY_CHANGE_299.md).
- Candidate terms affected: none left unresolved.

## Negative results

- None. Rejected alternate-version and control assumptions are scoped
  counterexamples, not claims of global absence.

## Delta summary

Twenty-nine genes cover the complete original-SNES TLPT exit task, with
four bounded additions and unchanged previous signatures.

## New facts

- [Observation | Corroborated | High] LV-002–LV-006 distinguish persistent
  bodies, actor-local inventory, shield support and all-three exit.
- [Observation | Conflicting | Medium] LV-009 retains the 1992/1993 dating
  disagreement instead of manufacturing an exact first-release day.

## New genes

- [Observation | Corroborated | High] SYS-1600–SYS-1602 and CON-820 separate
  overhead support, shield descent, pad occupancy and innate verb access.

## New combinations

- [Observation | Direct | High] None; all 274 verified subsets are scanned.

## Taxonomy changes

- [Observation | Corroborated | High] TAXONOMY_CHANGE_299 adds the four
  definitions without rewriting any earlier definition or signature.

## New questions

- Which licensed original revision can supply an exact native replay, and
  which contemporary release evidence resolves the reported year discrepancy?
- How do later gravity fields or the original two-player camera change the loop?

## Next recommended game

- [Hypothesis | Limited | High] GAME-0554 Strange Horticulture, Windows.
- Optimisation criterion: maintain Selection 044's alternate-era/platform order.
- Expected information gain: plant identification from documentary evidence
  instead of three-body spatial/action coordination.
- Backlog impact: retain the remaining five approved subjects.

## Why this game

- [Hypothesis | Corroborated | High] The original SNES level tests direct
  multi-body persistence against assigned-agent and shared-input models,
  while reusing known inventory, fixture, combat and all-required exit rules.
