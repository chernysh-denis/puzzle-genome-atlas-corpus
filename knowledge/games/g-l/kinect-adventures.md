---
game_id: GAME-0414
slug: kinect-adventures
game_title: Kinect Adventures!
analysis_status: reviewed
reviewed: 2026-09-26
combination_ids: []
gene_ids:
  action:
    - ACT-553
  system:
    - SYS-1101
  constraint:
    - CON-699
  information:
    - INF-407
  objective:
    - OBJ-002
  time:
    - TIM-003
---

# Game: Kinect Adventures! — 20,000 Leaks

Use the canonical [vocabulary and genome rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Leak positions, the particular player's limb, scoring amount and Kinect calibration are parameters rather than separate genes.

## Analysis scope

- Version / ruleset: original North American English Xbox 360 *Kinect Adventures!* (2010), one solo ordinary **20,000 Leaks** activity from its first active underwater-glass leak through the activity's scored result. This is not a Timed Adventure or Time Challenge. The exact disc revision and named level within the activity were not inspected; no particular numerical medal threshold is asserted.
- Structured analysis target: `PLAT-XBOX-360` with the original Kinect sensor in [`knowledge/platforms/games.json`](../../platforms/games.json). Kinect is a required input device here, not a separate release platform.
- Primary decision loop: locate the present hole or linked group in the glass, move one's tracked arms, legs, head or knees over each active leak, hold a feasible multi-limb pose until the entire connected crack seals and earns points, then respond to the next visible leak while the round continues.
- Entry and exit: begin at the first controllable leak in one selected 20,000 Leaks activity; stop at that activity's displayed result and medal evaluation. The exact leak schedule, duration, early-failure rule and score thresholds remain unmeasured; they are not silently inferred from another mode.
- Included: direct full-body contact placement, concurrently held body-part coverage of linked holes, seal-and-score resolution, currently visible leak positions, live score/time feedback and real-time response to new damage.
- Excluded: River Rush, Rallyball, Reflex Ridge, Space Pop, two-player interaction, multi-activity Adventure progression, explicit Timed Adventures and Time Challenges with their time collectibles, Xbox LIVE sharing, photos, avatar clothing, calibration menu, later activity variants and numerical Kinect recognition or scoring thresholds.
- Potential scoped modules: one identified Free Play level with measured leak schedule, or an explicitly named Timed Adventure after separate direct observation.
- Direct-play status: none. No Xbox 360 disc, Kinect sensor session, input trace, video or audio was inspected. The publisher's original English manual was downloaded from Microsoft and its relevant pages were text-extracted and visually inspected; contemporary played reviews corroborate simultaneous multi-hole poses. Hardware and exact round timing remain unverified.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `KIN-001` | The 2010 Xbox 360 pack-in is a controller-free, body-tracked collection of activities, including 20,000 Leaks. | Confirmed | Direct | High | M1, M2, E1 |
| `KIN-002` | In 20,000 Leaks, the player holds a tracked hand, foot, head or knee over a glass hole; fish cause further holes. | Confirmed | Direct | High | M1 pp. 18–19 |
| `KIN-003` | Every hole connected by one crack must be covered to seal that crack; multi-hole arrangements demand simultaneous body placement rather than a single tap. | Observation | Corroborated | High | M1 pp. 18–19, R1 |
| `KIN-004` | Sealing a crack earns points; the manual depicts a live timer and score, and ordinary activity performance can receive a medal. | Confirmed | Direct | High | M1 pp. 18–23 |
| `KIN-005` | Timed Adventures and Time Challenges have additional time-extension rules; those are not imported into the selected ordinary activity. | Confirmed | Direct | High | M1 pp. 20–23 |
| `KIN-006` | Exact sensor threshold, leak schedule, duration, medal cutoffs and early-failure ordering are not established by this source packet. | Observation | Limited | High | M1, R1 |

## Basic data

- Release / origin: Microsoft announced the Xbox 360 Kinect bundle containing *Kinect Adventures!* in July 2010. The original publisher manual has 2010 Microsoft copyright and describes the five activities and Kinect input.
- Platform or physical form: Xbox 360 disc plus Kinect full-body motion sensor, solo activity.
- Mechanical families: real-time system pressure (`FAM-010`).
- Sources accessed 2026-09-26:
  - **M1** — [Microsoft's original English Kinect Adventures! instruction manual](https://download.microsoft.com/download/F/9/9/F99AB8F0-5191-4EDD-B312-7A9B9E4784FA/KinectAdventures_MNL_EN-US.pdf), PDF pp. 9, 18–23. The exact Microsoft PDF was downloaded; its 17 PDF pages, printed pp. 18–19 art and adjacent rules were inspected. PDF SHA-256 `9b3d1242310f265387f2e551f62335a8cf8deca75a006958c978e7378cb7f205`.
  - **M2** — [Microsoft's 2010 launch announcement](https://news.microsoft.com/source/2010/07/20/new-xbox-360-kinect-sensor-and-kinect-adventures-get-all-your-controller-free-entertainment-in-one-complete-package/), original bundle and full-body, controller-free premise; marketing is not evidence for numerical leak timing.
  - **E1** — [ESRB rating summary](https://www.esrb.org/ratings/29471/kinect-adventures/), Xbox 360 identity and body movement across the included activities.
  - **R1** — [Kotaku's contemporary played review](https://kotaku.com/review-kinect-adventures-5679412), directly observed multi-leak simultaneous poses. It is a reviewer observation rather than a publisher rule specification.
- Claim IDs: `KIN-001`–`KIN-006`.

## Mechanical decomposition

### Action Genes

- `ACT-553` covers one currently visible leak by moving and holding a Kinect-tracked body part over its corresponding glass location. Hands, feet, knees and head are eligible parts in the manual; the precise collision tolerance is not known. This is a continuous body-position decision, not a face-button click or a direct avatar walk command.
- Claim IDs: `KIN-001`–`KIN-003`, `KIN-006`.

### System Behaviour Genes

- `SYS-1101` evaluates the currently held contacts for one connected crack. When every required hole in that crack is covered, the crack seals and the activity awards points; a single covered hole in a larger still-open group does not settle the crack.
- Fish striking the glass introduce subsequent damage, but the source packet does not establish a random distribution or exact spawn policy. No `SYS-004` random-outcome gene is asserted.
- Resolution order at this boundary: active leak positions are visible → the player moves eligible body parts → Kinect-mirrored contacts are evaluated together → a wholly covered connected group seals and scores → the next active damage can demand another pose. Exact sensor-frame priority is unknown.
- Claim IDs: `KIN-002`–`KIN-004`, `KIN-006`.

### Constraint Genes

- `CON-699` requires concurrently valid contacts at all holes of one connected crack. The number and positions of holes change the feasible body pose; an already released hand cannot be counted as still covering its former hole. Separate cracks are not automatically one all-or-nothing group.
- Claim IDs: `KIN-003`, `KIN-006`.

### Information Genes

- `INF-407` exposes the present holes on the glass, the tracked avatar's apparent alignment, current score and the activity clock. The publisher's pp. 18–19 image visibly includes time and score displays, but does not prove the exact values or threshold. Later hole timing is not previewed.
- Claim IDs: `KIN-002`, `KIN-004`, `KIN-006`.

### Objective and Time Genes

- `OBJ-002` makes point accumulation from sealed cracks the ordinary performance objective of this bounded activity. A medal is a result evaluation, not proof that a particular medal tier is compulsory for this one run.
- `TIM-003` reflects real-time, simultaneous body tracking and ongoing appearance of damage while contact decisions are made. Although a clock is visible, its exact duration and timeout consequence are not asserted; explicit Time Challenge extensions are excluded.
- Claim IDs: `KIN-002`–`KIN-006`.

## Reproducible transitions

| Before | Action | Bounded resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| One visible glass leak is active | Place an eligible tracked hand over its current position and hold | The matching hole becomes covered; if it is the whole connected crack, the crack seals and points accrue | direct body contact, not a button press, is the action | `KIN-002`, `KIN-004` |
| Two holes share one visible crack, only one is covered | Move a second eligible body part onto the other hole while retaining the first contact | Both contacts are concurrently valid and the group can seal; the first contact alone could not settle it | connected holes impose a multi-part pose | `KIN-003` |
| A hand leaves one hole before all connected holes are covered | Reach with the same hand toward another hole | The vacated position is no longer covered; the connected crack remains unresolved until a feasible concurrent pose exists | serial taps do not substitute for simultaneous coverage | `KIN-003` |
| A crack has sealed and scored | Respond to a later fish-caused visible leak | A new target demands another body position; prior points remain in the run score | real-time repeated scoring loop | `KIN-002`, `KIN-004` |
| The chosen activity reaches its result | Read the final performance evaluation | The bounded analysis stops at score and medal rather than continuing into another minigame | activity result, not collection-wide completion | `KIN-004`, `KIN-005` |

## Strategic and experiential structure

- Local decision: choose which reachable body part can occupy each visible leak while preserving already necessary contacts.
- Medium-term planning: keep balance and room for a second or third contact when a crack branches; the order of individual placements matters because coverage must overlap.
- Failure attribution: a misplaced limb or released earlier contact leaves the group unsealed, and sensor calibration may affect recognition. The actual recognition tolerance was not measured.
- Player-trust factor: visible leak locations, reflected body pose, clock and score distinguish a missed placement from a successfully closed crack, even without revealing future holes.
- Claim IDs: `KIN-002`–`KIN-006`.

## Replay and variation

- Leak placement and body-pose sequence can differ across named levels, but this packet does not claim a stochastic generator.
- A player can cover a compatible opening with different eligible body parts; a particular limb is a parameter as long as all linked holes remain concurrently covered.
- Faster, cleaner sealing can improve the score; no exact time-bonus conversion or medal threshold is claimed for this unspecified ordinary activity.

## Adjacent systems and history

- *DanceDanceRevolution* also treats physical movement as game input, but its four floor panels are discrete timed notes on an authored chart. 20,000 Leaks accepts spatially tracked free-limb positions held simultaneously against present cracks.
- *Wii Sports* Bowling samples one motion and releases a ball into a scored physics roll. Here the player's live body remains the coverage surface until the connected crack seals.
- *Ape Escape* aims a separate virtual net at a creature; the controller-directed transient sweep does not require several simultaneous body contacts.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-553` | tracked limb, contact position and hold duration |
| System Behaviour | `SYS-1101` | crack topology, leak contacts and point value |
| Constraint | `CON-699` | simultaneous eligible contacts across one linked group |
| Information | `INF-407` | visible leak positions, mirrored pose, score and clock |
| Objective | `OBJ-002` | maximise bounded activity points; medal is evaluation |
| Time | `TIM-003` | live pose updates and new damage; exact timeout unknown |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `413` (`GAME-0001`–`GAME-0413`).
- Exact genome matches: none.
- Tied near matches: `GAME-0114` — Peggle Deluxe (`2 / 11 = 0.181818`).
- Supported combination subsets: none.
- Scan date: 2026-09-26.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0114` — Peggle Deluxe | `OBJ-002`, `TIM-003` | Both accumulate points while a live physical state advances. Peggle commits a discrete launched ball into gravity and peg collisions under a finite stock; 20,000 Leaks keeps the player's sensor-tracked body in contact with several linked holes at once until the glass seals. The low overlap does not imply similar input or stage goals. | Near, `0.181818` |

## Taxonomy impact

- [`TAXONOMY_CHANGE_152`](../../../research/taxonomy-changes/TAXONOMY_CHANGE_152.md) admits `ACT-553`, `SYS-1101`, `CON-699` and `INF-407`. No earlier game signature or verified combination is changed.

## Negative results

- `ACT-008` rejected: the selected body-contact activity is not free avatar traversal through a world route.
- `ACT-499` and `SYS-995` rejected: no bowling-style sampled release and subsequent independent ball trajectory occurs.
- `SYS-004` rejected: fish-caused new leaks do not establish a random-outcome law.
- `TIM-016` rejected: the visible activity clock is not a world loop with reset; exact timeout rules remain unknown.
- Explicit Timed Adventure and Time Challenge clock extensions are out of scope, not silently assigned to this ordinary activity.

## Delta summary

Four new boundaries distinguish live whole-body leak placement, a sealed-and-scored connected crack, simultaneous coverage eligibility and leak/clock feedback. Existing score maximisation and real-time input genes cover the remaining objective and temporal structure.

## New facts

- [Confirmed | Direct | High] The Microsoft manual specifies body-part coverage, all holes in a connected crack and point credit (`KIN-002`–`KIN-004`).
- [Observation | Corroborated | High] A contemporary played review corroborates simultaneous multi-leak poses (`KIN-003`).

## New genes

- [Observation | Corroborated | High] `ACT-553`, `SYS-1101`, `CON-699` and `INF-407` isolate the four missing typed boundaries without inventing a per-limb or Kinect-hardware gene.

## New combinations

- [Observation | Limited | High] No verified combination is asserted from this single game; subset validation remains deterministic.

## Taxonomy changes

- [Observation | Corroborated | High] `TAXONOMY_CHANGE_152` documents the four new boundaries and rejected alternatives.

## New questions

- What are the exact original-disc recognition tolerances, damage schedule, round duration, score conversion and medal thresholds in a named 20,000 Leaks level?
- Does an early water-failure terminal occur in that level, and how is it ordered relative to clock expiration?

## Next recommended game

- [Hypothesis | Limited | Medium] No next game is selected. Complete the 397–414 horizon audit, then choose another varied nine-game batch with the maintainer.
- Optimisation criterion: verify this eighteen-game batch's accepted corpus and localisation parity before reserving a new subject.
- Expected information gain: preserve exact scope and art provenance rather than prematurely extrapolating to another Kinect activity.
- Backlog impact: no candidate is implicitly promoted to `GAME-0415`.

## Why this game

- [Hypothesis | Corroborated | Medium] A Kinect body-tracking leak task changes both platform and action geometry after a PlayStation net-capture stage, testing whether concurrent embodied coverage needs new boundaries beyond generic direct movement and live target contact.
