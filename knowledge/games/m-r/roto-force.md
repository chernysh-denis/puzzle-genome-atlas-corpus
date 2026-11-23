---
game_id: GAME-0549
slug: roto-force
game_title: Roto Force
analysis_status: reviewed
reviewed: 2026-11-19
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-161
    - ACT-215
    - ACT-341
    - ACT-749
  system:
    - SYS-037
    - SYS-215
    - SYS-369
    - SYS-749
    - SYS-1591
    - SYS-1592
    - SYS-1593
    - SYS-1594
  constraint:
    - CON-773
    - CON-801
    - CON-817
  information:
    - INF-119
    - INF-235
  objective:
    - OBJ-029
  time:
    - TIM-003
---

# Game: Roto Force

Use the [canonical vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
A rotating camera is not an edit to physical arena geometry. An ordinary dash
is not a universal immunity or a free charged strike.

## Analysis scope

- Version / ruleset: original English PID Games Android release,
  `com.pid.rotoforce`, launch-window 2023 rules before the September Boss Rush
  rebalance. The developer declares 18 July 2023; catalogues also list
  11 July, so no regional rollout chronology or exact installed patch is
  reconstructed from those dates. This is a released product, not the earlier
  Pixel Soldier jam build or an Early Access ruleset.
- Structured analysis target: `PLAT-ANDROID`, original touch-controlled
  Android app with the full-game unlock prescribed. No APK, native device,
  purchase entitlement, save, input trace or executable checksum was inspected.
  The now-delisted PID app is not replaced by Crunchyroll's later edition.
- Fixed setup: ordinary first-play Roto Jungle after training, standard
  Intern rules, rotating camera enabled, normal speed and damage, immortality
  off and no unlocked modifiers. Begin with Rapid Shot; Homing Shot becomes
  available in this mission. Prescribed settings are distinct from the
  unverified exact settings of a third-party capture.
- Entry: complete or accept the training prerequisite, select the initially
  available Roto Jungle and begin at its first live round. Contract signing
  and tutorial completion alone are not this unit's positive terminal.
- Primary decision loop: inspect the current boundary, enemies, hazards and
  shot direction; walk along its inner surface, then aim and release a dash
  through the interior to a different foothold. Fire the current weapon,
  use dash contact to open protected targets, acquire restorative hearts,
  and choose whether to spend banked excess health on a charged dash. At
  cleared-round checkpoints, request the support drone and select an unlocked
  weapon before the next authored wave or boss. Adapt to the later circular
  nest and fire-bird patterns instead of treating the first miniboss as a win.
- Positive exit: defeat the final Roto Jungle boss, settle Stage Clear,
  read the mission's elapsed-time and death summary and return to the map
  with that first stage marked complete. Stop before playing another stage.
  A perfect time, zero deaths, every modifier or whole-game completion is not
  required. A recorded clear with one death is evidence against perfect play
  being the ordinary gate, not a proposed optimal route.
- Negative exit and recovery: depleted ordinary health ends the current
  round attempt. Retry restores the latest authored checkpoint rather than
  requiring a full new mission. Failed transient enemies and positions are
  not kept as a live continuation. Exact health/bank restoration order,
  native retry delay and weapon reappearance timing are not measured.
- Timing qualification: touch guides disagree on aim slowdown versus full
  stop. Its native rate and onset are unmeasured; no universal stopped world
  is accepted.
- Included: boundary-constrained locomotion, automatically rotating frame,
  aimed dash/held super branch, eligible projectile immunity and bubble
  opening, limited inward shooting, Rapid/Homing shot profiles, incoming
  hazards, missing-health restoration and surplus dash supply, checkpoint
  marker/drone selection, finite kill-triggered rounds, authored arena
  replacement, first-stage bosses, local retry, live displays and clear result.
- Excluded: training as a separate objective, later biomes or weapons,
  Senior/Chief Intern, September Boss Rush and Free Aim, subsequent balance
  patches, modifiers, accessibility multipliers or immortality, achievements,
  time-star thresholds, completionist unlocks, physical controller controls,
  PC/iOS binary parity, Crunchyroll entitlement and procedural generation.
  Potential modules include a versioned Boss Rush, a modifier challenge and
  a later weapon's charge/alternate-fire rules.
- Direct-play status: no native Android app or local game was executed.
  Developer text, Play editorial rules and contemporary mobile accounts were
  read. Public static storyboard frames from a post-release mobile first-stage
  capture were inspected without audio or video playback. One muted headless
  embed inspection did not reach playable media and was closed; it supplies
  no gameplay observations. The visible trial purchase prompt does not verify
  ownership of the full unlock, and its exact OS/build/difficulty is unknown.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
| --- | --- | --- | --- | --- | --- |
| RF-001 | The released original Android app's first mission is Roto Jungle; it runs through multiple checkpointed rounds and bosses to Stage Clear and a retained map mark. The first-level trial is part of the released product, not proof of full-game entitlement. | Observation | Corroborated | High | P1, P2, P3, R1 3:35–13:10, S1 |
| RF-002 | Left/right movement follows the arena's inner boundary, with the rotating camera keeping control relative to the current foothold. Aimed dashes cross the interior and settle on another boundary; ordinary movement is not free 2D flight. | Observation | Corroborated | High | P1, P2 Q1/Q3/Q7, P3, R1 0:50–1:50, S1 |
| RF-003 | Ordinary dashing protects against eligible ordinary projectiles and opens bubbles protecting enemies or pickups. Glowing attacks and dangerous landing segments remain threats; a dash is not universal invulnerability. | Observation | Corroborated | High | P3, R1 training and protected targets, S1, S2, S3 |
| RF-004 | Missing health can be restored by eligible hearts; excess pickups become a bounded reserve for the held charged dash, whose contact can damage foes. Exact spend, recharge, bank-loss priority and passive healing are not inferred. | Observation | Corroborated | High | R1 2:45–3:25, S1, S3 |
| RF-005 | Rapid Shot and Homing Shot differ in trajectory. Acquired functions are stored by the support drone; shooting a checkpoint marker exposes weapon choices for subsequent live play and local retries. | Observation | Corroborated | High | R1 2:00, 4:40–6:00, S1, S3, S4 |
| RF-006 | Authored kill-triggered waves, minibosses, the nest handoff and the final fire-bird fight change the encounter. Death permits checkpoint retry; an ordinary clear does not require a flawless mission. | Observation | Corroborated | High | R1 3:45–12:40, S1, S3, S4 |
| RF-007 | The field, firing/dash guides, health/surplus feedback, round markers and results expose current decisions. Camera and palette changes communicate state; they do not randomise the authored mission. | Observation | Corroborated | High | P1, P2 Q5, R1, S1, S2 |
| RF-008 | Written touch guides describe an aim-associated slowdown, but disagree on slowdown versus full time stop. Its native rate and onset were not measured; no universal stopped-world interval is accepted. | Observation | Conflicting | Medium | S5, S6; sparse R1 stills cannot time the hold |

## Basic data

- Release / origin: Accidently Awesome, published by PID Games; the
  developer's full-release date is 18 July 2023. The earlier jam prototype,
  later desktop updates and later subscription port remain distinct products
  or ruleset revisions for this packet.
- Platform or physical form: original Android touch interface, two on-screen
  control regions, prescribed full-game unlock and default rotating mode.
- Puzzle family: `FAM-010`, live system pressure. Position, shot angle and
  a limited escape landing must be selected during continuing hostile action.
- Primary sources:
  - **P1** [Developer press kit](https://accidentlyawesome.com/roto-force-presskit/),
    release/platform facts, gravity-disregarding wall movement and first-stage
    trial. Official stills distinguish a bounded interior from a scrolling map.
  - **P2** [Anton Klinger's release interview](https://www.taptap.io/post/6034182),
    21 July 2023, Q1/Q3/Q5/Q7: boundary movement, rotating-camera design,
    selectable fixed-camera alternative and state-dependent palette. Mobile
    input overlays are an explicit exception to a strict four-colour claim.
  - **P3** [Google Play editorial](https://play.google.com/store/apps/editorial?id=mc_editorialevergreen_game_of_the_week_roto_force_fcp),
    touch movement, dash/ordinary-projectile protection, glowing exceptions,
    landing hazards and first-level trial versus paid continuation.
  - **P4** [Developer store and delisting reply](https://accidentlyawesome.itch.io/roto-force),
    released status, non-procedural design and the author's statement that
    the original mobile app is unavailable while Crunchyroll is the present
    mobile distribution. The page's desktop download version is not assigned
    to the historical Android target; no desktop binary was run.
  - **P5** [Developer update history](https://steamcommunity.com/app/1181610/allnews/?l=english),
    dated September 2023 and December 2025. Boss Rush, Free Aim, later damage
    changes and weapon reappearance adjustments are not back-projected into
    the selected launch-window Android packet.
- Visual evidence:
  - **R1** [Pryszard first-stage mobile capture](https://www.youtube.com/watch?v=9HZ5h0ywDA0),
    published 24 July 2023, 13:11. Inspected its public 320-by-180 storyboard
    cells at five-second sampling, not an audio/video playback. Training
    appears before 3:30, Roto Jungle starts around 3:45, Homing Shot is shown
    around 4:40, checkpoint/drone choices recur, the circular nest appears
    around 9:20 and final boss warning around 11:30. Stage Clear is visible
    at 12:40 with 8:41 and one death; map and trial purchase prompt follow.
    These coarse times locate evidence, not native-frame measurements.
- Secondary sources:
  - **S1** [NimbleThor's mobile review](https://minireview.io/action/roto-force),
    first-hand two-stick control, five starting hearts, surplus-funded super
    dash, checkpoint retry and first-mission trial. The search-rendered review
    was readable; the direct page's script shell added no gameplay evidence.
  - **S2** [App Army mobile accounts](https://www.pocketgamer.com/roto-force/app-army-assemble/),
    27 July 2023: landing into fire, first-boss danger, dash/shield interaction
    and touch controls corroborate the live loop. Device/configuration parity
    is not asserted across its different contributors.
  - **S3** [Kef's first-level account](https://www.taptap.io/post/6023314),
    18 July 2023, bubble opening, two available weapon profiles, checkpoint
    replacement and visible low-health palette. It identifies trial coverage.
  - **S4** [Contemporary mobile review](https://toucharcade.com/2023/08/01/roto-force-mobile-review-run-n-gun-shooter-bullet-hell-iphone-android-pc-steam/),
    1 August 2023, quoted first-hand checkpoint and control observations;
    readable search rendering, while direct retrieval was restricted.
    The article's iOS recommendation is not Android binary authentication.
  - **S5** [Early touch-control account](https://www.taptap.io/post/6010632),
    a pre-release demo lead describing held-aim slowdown; used only for the
    explicitly qualified timing question, never as release certification.
  - **S6** [Pre-release emulator guide](https://www.ldplayer.net/blog/roto-force-beginners-guide.html),
    23 June 2023. Its full-stop, reflected-shot, automatic banked-heart recovery
    and exact boss-order claims are not adopted as native release facts.
- Claim IDs: RF-001–RF-008.

## Mechanical decomposition

### Action Genes

- Reuse `ACT-008` for directly steered boundary travel and `ACT-161` for
  aimed live Rapid/Homing fire, not automatic Vampire Survivors attacks.
- Reuse `ACT-341` for addressing the checkpoint marker's activation and
  `ACT-215` for preparing one unlocked weapon for the next segment. Shooting
  an interactive marker is an activation request, not combat damage to it.
- Add `ACT-749` for aiming and releasing a cross-arena dash, including the
  longer held super branch when funded. It traverses collision-relevant
  intermediate space, unlike Blink's `ACT-421` relocation.
- Claim IDs: RF-002–RF-005.

### System Behaviour Genes

- Reuse `SYS-037` for contact acquisition, `SYS-215` for live weapon damage
  and hazard-sensitive combat, `SYS-749` for finite groups released by the
  authored defeat/progression predicate and `SYS-369` for local death retry.
- Add `SYS-1591` for binding movement and the following frame to the active
  inner boundary, including rebinding at the authored nest handoff.
- Add `SYS-1592` for dash contact classified by ordinary bullet, shield,
  glowing hazard and charged-body hit; a safe transit can still end in danger.
- Add `SYS-1593` for routing heart restoration at the health cap into a
  finite, deliberately spent super-dash reserve. This is not `SYS-1417`'s
  pending food recovery or `SYS-936`'s automatic invulnerability threshold.
- Add `SYS-1594` for stored weapon availability, the shot-opened checkpoint
  selector and replacement of the one active profile for subsequent rounds.
- The boss roster and encounter layout change at authored round boundaries.
  No continuous transformation threshold is inferred solely from palette
  changes, and no `SYS-799` health-gated phase is asserted from those colours.
- Claim IDs: RF-001–RF-007.

### Constraint Genes

- Add `CON-817`: ordinary locomotion is confined to the current connected
  inside boundary. Crossing open space requires the dash capability rather
  than unconstrained twin-stick flight.
- Reuse `CON-773` for positive vitality before a declared local retry,
  and `CON-801` for one replaceable active firearm without a carried backup.
  The support drone's unlocked choices are not a second live held gun.
- Shooting keeps its launch-era inward aiming limits; no later Free Aim
  modifier or unmeasured exact degree range is imported.
- Claim IDs: RF-002–RF-006.

### Information Genes

- Reuse `INF-119` for health, surplus, current weapon and readiness;
  `INF-235` for current threats, pickups and weapon effects in the playfield.
  Visible dash/firing guides, progress marks and palette feedback are scoped
  display parameters rather than a new gene per colour or HUD element.
- The summary's elapsed time and death count are not evidence for a hidden
  weighted grade. `SYS-822` is not assigned merely because numbers appear.
- Claim IDs: RF-007, RF-008.

### Objective Genes

- Reuse `OBJ-029` for the required finite combat set within each authored
  round, ending the mission only after its final boss has been incapacitated.
  The next group is defeat-triggered, not a clock-only survival assault.
- Stage Clear and the retained map mark settle the accepted packet. The first
  miniboss, a weapon unlock or a trial purchase dialog alone does not.
- Claim IDs: RF-001, RF-006.

### Time Genes

- Reuse `TIM-003`: ordinary movement, projectiles and enemies progress live.
  Pause, authored dialogue and any documented aim-rate adjustment are control
  parameters; no second universal time-stop gene is inferred from a guide.
- RF-008 retains the slowdown/full-stop conflict. Sparse stills do not measure
  native time scale, input latency, dash duration or an immunity-frame window.
- Claim IDs: RF-002, RF-003, RF-008.

## Reproducible transitions

| Before | Action or event | Bounded resolution | What it establishes | Claim ID |
| --- | --- | --- | --- | --- |
| Standing on a valid inner surface | Hold left or right | Follow the connected perimeter while the camera follows the foothold frame | Movement and automatic framing are coupled | RF-002 |
| A new surface can be reached across the interior | Aim the left control and release the dash | Traverse the chosen chord and attach to the accepted boundary | Not free flight or an arbitrary teleport | RF-002 |
| An ordinary eligible projectile crosses the dash | Commit the dash through its path | Apply the dash's ordinary projectile protection | Class-qualified protection differs from all-hazard immunity | RF-003 |
| A glowing attack or dangerous landing occupies the route | Dash into that danger | Protection against ordinary bullets does not guarantee safety | Choose both a transit and landing gap | RF-003 |
| A target or heart is enclosed by a bubble | Use ordinary fire, then eligible dash contact | Fire does not open the protection; dash contact opens access | Contact class matters before damage or acquisition | RF-003 |
| Health is missing and an eligible heart is accessible | Acquire it | Restore eligible missing health | Healing is not a shot or an earned weapon | RF-004 |
| Health is full and excess heart supply is available | Collect it | Add the declared surplus reserve for a future super dash | Cap overflow has a separate tactical use | RF-004 |
| A surplus-funded charged dash is available | Hold its preparation and commit | Spend the declared supply for a stronger contact attack | No free super on every ordinary dash | RF-004 |
| A cleared round has supplied the checkpoint marker | Address and shoot it | Expose support-drone weapon choices | A shot can operate a selector rather than harm a foe | RF-005 |
| Rapid and Homing choices have been acquired | Select an eligible weapon | Replace the active profile for the next segment | Drone storage differs from carrying two active guns | RF-005 |
| The current authored hostile set is defeated | Let its settled transition complete | Credit the round and release the next finite authored challenge | No infinite procedural survival stream | RF-006 |
| A round attempt loses all ordinary vitality | Retry | Restore the latest declared checkpoint and its encounter state | The whole mission need not restart | RF-006 |
| The authored bird handoff changes the arena | Continue with the new boundary | Bind movement and dash endpoints to the circular nest | A shape change differs from merely turning the camera | RF-002, RF-006 |
| The final Roto Jungle boss is defeated | Settle Stage Clear and return to the map | Record the first-stage clear with its time/death summary | A non-perfect clear is still a clear | RF-001, RF-006 |

These are source-based transition checks, not a native Android input session.

## Strategic and experiential structure

Walking trades position against a firing angle on the current boundary.
Dashing changes that position rapidly but must cross eligible hazards and end
on a usable segment. Opening a bubble creates a weapon or healing opportunity;
spending surplus health on contact damage competes with retaining that reserve.
Weapon choices at the drone alter the next live shooting problem without
creating a second controllable body or a carried-gun inventory.

The later nest changes available footholds and landing geometry. Its authored
boss patterns are not random generation, and a palette shift alone is not
proof of a new damage threshold. The acceptance boundary is the completed
mission, including retries, rather than an isolated successful dash.

## Replay and variation

The developer explicitly excludes procedural generation. A replay can change
weapon choice, positions, dash commitments, damage and recorded time/deaths.
Checkpoint retry reduces the cost of relearning the current round. Later
modifiers, fixed camera, accessibility multipliers and Boss Rush could form
separate packets; they are not silently enabled here.

## Adjacent systems and history

The developer names Alien Soldier as an influence on the earlier prototype's
wall/ceiling traversal, but the released camera and touch controls require
separate evidence. The original Android release, desktop build, iOS edition
and later Crunchyroll distribution are not assumed binary or input equivalents.
A June demo guide remains a qualified lead where release confirmation lacks.

## Normalised genome

| Type | Active genes | Scoped role |
| --- | --- | --- |
| Action | `ACT-008`, `ACT-161`, `ACT-215`, `ACT-341`, `ACT-749` | Walk, fire, prepare, activate and dash |
| System Behaviour | `SYS-037`, `SYS-215`, `SYS-369`, `SYS-749`, `SYS-1591`, `SYS-1592`, `SYS-1593`, `SYS-1594` | Acquire, combat, retry, waves, frame, dash classes, surplus and weapons |
| Constraint | `CON-773`, `CON-801`, `CON-817` | Vitality, one active gun and boundary-only walking |
| Information | `INF-119`, `INF-235` | Personal resources and current live field |
| Objective | `OBJ-029` | Defeat the finite required combat set |
| Time | `TIM-003` | Live progression with qualified control-rate parameters |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `548` (`GAME-0001`–`GAME-0548`).
- Exact genome matches: none.
- Tied near matches: `GAME-0293` — Ori and the Will of the Wisps (`8 / 30 = 0.266667`).
- Supported combination subsets: none.
- Scan date: 2026-11-19.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
| --- | --- | --- | --- |
| `GAME-0293` — Ori and the Will of the Wisps | `ACT-008`, `ACT-161`, `ACT-215`, `ACT-341`, `SYS-215`, `SYS-369`, `INF-119`, `TIM-003` | Both directly navigate, aim attacks, prepare capability choices, operate fixtures and retry authored checkpoints with visible personal resources. Ori follows a side-view prologue through feather, keys, Torch and Spirit Edge; Roto confines ordinary movement to an inner rim, crosses it by typed dash and spends overflow hearts through a checkpointed arena mission. | Near, `0.266667` |

### Preserved research notes

- New genes: `ACT-749`, `SYS-1591`, `SYS-1592`, `SYS-1593`, `SYS-1594`, `CON-817`.
- Classification result: New gene.
- Evidence and reasoning: live combat, checkpoints, information and finite objective transfer unchanged; boundary-relative control, dash classes, surplus spending and the drone replacement protocol require separate operational boundaries.

## Taxonomy impact

- Fourteen definitions are reused and six are added; twenty in total.
- Registry changes: six new Active definitions.
- Taxonomy-change record: [TAXONOMY_CHANGE_296](../../../research/taxonomy-changes/TAXONOMY_CHANGE_296.md).
- Candidate terms affected: none.

## Negative results

- none.

## Delta summary

## New facts

- [Observation | Corroborated | High] A bounded inner perimeter, cross-arena
  dash and surplus-funded contact attack change the same first-mission loop.

## New genes

- [Observation | Corroborated | High] Six additions separate input, frame,
  classified dash contact, surplus routing, weapon replacement and locomotion.

## New combinations

- [Observation | Corroborated | High] No new combination is proposed.

## Taxonomy changes

- [Observation | Corroborated | High] `TAXONOMY_CHANGE_296`.

## New questions

- What are the selected native build's precise aim-rate and dash immunity windows?
- How does damage settle health, surplus and the reserve cap in the original Android executable?

## Next recommended game

- [Hypothesis | Limited | Medium] No further game is selected after
  [Selection 043](../../../research/selection/SEARCH_DEMAND_GAME_SELECTION_043.md).
- Optimisation criterion: close the approved nine-game horizon before selecting another.
- Expected information gain: compare the accepted nine-game definitions and acceptance evidence.
- Backlog impact: stop expansion at `GAME-0549`; no implicit tenth game or publication.

## Why this game

- [Hypothesis | Limited | Medium] A modern Android wall-bound shooter tests
  whether a dash can be separated from a universal dodge and free movement.
