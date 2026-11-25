---
game_id: GAME-0676
slug: mixtape
game_title: "Mixtape"
analysis_status: reviewed
reviewed: 2026-11-24
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-901
    - ACT-902
  system:
    - SYS-1944
    - SYS-1945
  constraint: []
  information:
    - INF-623
  objective:
    - OBJ-356
  time:
    - TIM-003
---

# Game: Mixtape

This record uses the [canonical vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
The road layout, music, individual button labels and award name are parameters.

## Analysis scope

- Version / ruleset: English Xbox Series X|S commercial base game, first
  released May 7, 2026. The observed launch-window capture identifies
  Xbox Series X. The numerical build and physical input trace are unknown.
- Structured analysis target: PLAT-XBOX-SERIES in
  `knowledge/platforms/games.json`. Xbox Store product 9NH0MSG29X6L.
- Entry: begin the first chapter. Take the opening downhill leg after the
  introductory track card, when the road view opens behind the riders.
- Primary decision loop: roll down the road, steer the rider's line and
  choose when to push or perform a trick. Read the moving traffic and
  roadside geometry so an ollie can be placed at a chosen obstacle.
  For an optional achievement, attempt a car clearance with the ollie.
  Continue rolling toward the story handoff.
- Exit: the title passes over the road and the view cuts to the first
  scripted car encounter around 02:20 in the main source. Stop at that
  handoff before the second board-controlled leg. The optional car
  award is a separate result.
- Included: forward travel on a prescribed downhill course, local
  steering, the Push and three named trick commands, staged live
  prompts, a documented eligible ollie and its optional award,
  and the first scripted change from play to the roadside scene.
- Excluded: later parts of the same chapter, the soundtrack's timing
  and licensing, cross-platform parity, exact momentum and jump
  height, collision and retry generalisation, reward persistence
  across devices, later skate chapters and other vignettes.
- Potential scoped module: compare the ordinary route with a controlled
  no-input replay or a deliberate failed clearance.
- Direct-play status: the game was not launched personally. The
  publisher and Xbox establish product and date. The main recording
  explicitly identifies Xbox Series X and shows the scoped transitions.
  A second recording with Xbox button glyphs and achievement interface
  corroborates the optional car clearance. Its interface is Spanish and
  its exact hardware and build are unverified. Only video frames were
  inspected, in the background with audio excluded.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
| --- | --- | --- | --- | --- | --- |
| MX-001 | Product 9NH0MSG29X6L is a commercial May 7, 2026 Xbox Series X or Series S release. The publisher identifies Beethoven & Dinosaur as developer and skateboarding as an included activity. | Observation | Direct | High | P1, P2 |
| MX-002 | The course visibly advances before the first displayed controls. The rider shifts relative to the road markings while the descent continues through the bends, bridge and tunnel. Xbox Wire describes player steering in the opening ride. | Observation | Corroborated | High | P3, W1 00:07–00:36 and 01:24–02:12 |
| MX-003 | The first readable Xbox button pair is Y for Push and A for Ollie. A later pair makes X for Flip Trick and B for Grab Trick visible. The tutorial text overlays the live ride rather than opening a separate menu. The rider is visibly airborne around 00:49 before rolling again around 00:51. | Observation | Direct | High | W1 00:37–00:51 |
| MX-004 | A second recording shows the rider crouching as the red car approaches, going airborne as their paths overlap in the road view, and rolling after landing. The Xbox achievement notification then appears. Its companion guide names the hold and release of A and the optional car-clearance objective. Exact hitbox and height are unverified. | Observation | Corroborated | High | W2 00:39–00:49, R1, R2 |
| MX-005 | The main trace passes the reference car approach on the board and later reaches the authored scene transition. The first title and car-scene cut are visible without the scoped trace showing an achievement notification. The guide treats the car clearance as an optional unlock. | Observation | Corroborated | High | W1 00:28–00:36 and 02:14–02:28, R1, R2 |
| MX-006 | Traveller speed and obstacle spacing offer a live placement window for a chosen trick. A matched visual cue identifies roll approach and airborne response. Recorded button events and an input-free counterfactual are unavailable. | Pattern | Corroborated | Medium | P3, W1 00:37–00:51, W2 00:39–00:49, R1 |

## Basic data

- Release / origin: Beethoven & Dinosaur, published by Annapurna
  Interactive. Xbox Store's English GB product page lists May 7, 2026.
- Puzzle family: FAM-010 for changing road position and passing vehicle
  timing while live steering and trick decisions remain available.
- P1: [Xbox Store product 9NH0MSG29X6L](https://www.xbox.com/en-GB/games/store/mixtape/9nh0msg29x6l).
- P2: [Annapurna Interactive game page](https://annapurnainteractive.com/games/mixtape).
- P3: [Xbox Wire's launch article](https://news.xbox.com/en-us/2026/05/07/mixtape-90s-narrative-music-adventure-launch/).
  The editor's first-hand account corroborates steering the skateboard
  downhill in the released game.
- W1: [That Mute Gamer's Xbox Series X opening recording](https://www.youtube.com/watch?v=1osHz4_IHyc).
  Published May 10, 2026. Use the first leg from 00:07 to approximately
  02:20 and its first roadside scene through 02:28 as exit evidence.
  Attribution identifies the device family, not the binary.
- W2: [ZhakeY's successful car-ollie recording](https://www.youtube.com/watch?v=Jxo-PQyzwtw&t=39s).
  Published May 10, 2026. Spanish interface and achievement notification
  corroborate the visible result. Use it for the optional interaction only.
- R1: [ZhakeY's companion guide](https://www.chicasgamers.com/2026/05/guia-mixtape.html).
  Documents holding and releasing the ollie on the car approach.
- R2: [Stevivor's launch-day guide](https://stevivor.com/guides/mixtape-achievement-and-trophy-guide-and-roadmap/).
  Independent play report identifies an eligible opening car and the
  award. Other suggested vehicles do not define the full eligibility set.
- Claim IDs: MX-001–MX-006.

### Reproducible route evidence

1. Start the first chapter in the English Xbox edition. After the
   track card and introductory shots, watch the rolling board and
   relative positions of the road lines. From about 00:07 to 00:36 in
   W1 the ride progresses along the same road through multiple bends.
2. At roughly 00:37–00:40, read Push on Y and Ollie on A. Keep steering
   on the road. The later live pair at approximately 00:47–00:48 shows
   Flip Trick on X and Grab Trick on B. At about 00:49 the board is off
   the ground and near 00:51 ordinary rolling is visible again. The
   recording does not establish which button was pressed for each jump.
3. For the optional clearance use the oncoming red vehicle pictured in
   W2. Set the rider's line early. Hold A as it approaches and release
   for an ollie over it, as specified by the companion guide. The rider
   crouches around 00:39–00:41, rises around 00:42, and continues rolling
   after returning to the road around 00:43. An Xbox award notification
   follows around 00:45–00:48.
4. The separate W1 trace continues through the waterfall bridge and
   tunnel, then the title at approximately 02:17–02:19. At about
   02:20–02:28 the roadside conversation begins. That transition
   is the exit for this unit. The later controlled ride is out of scope.

## Mechanical decomposition

### Action Genes

- ACT-008: directly change the rider's local line while travel continues.
  MX-002.
- ACT-901: request a push to add downhill travel during free coasting.
  It has its own button and in-ride prompt. MX-003.
- ACT-902: request a distinct board manoeuvre during a ride. The
  plain ollie, flip and grab have separate controls. MX-003, MX-004.

### System Behaviour Genes

- SYS-1944: carry the controlled skater forward on the authored course
  while accepting local steering and tricks. MX-002, MX-003.
- SYS-1945: confirm an eligible airborne clearance of traffic with a
  separate optional achievement. MX-004, MX-005.

### Constraint Genes

None admitted. Exact road bounds, collision and landing predicates
remain unverified from these traces.

### Information Genes

- INF-623: show pairs of applicable movement and trick inputs during
  the continuing ride. MX-003.

### Objective Genes

- OBJ-356: reach the authored road-leg handoff; the optional car
  clearance can be attempted along that path. MX-004, MX-005.

### Time Genes

- TIM-003: select steering or trick timing while the road and traffic
  keep moving. MX-002, MX-006.

## Reproducible transitions

| From | Input or event | To | Evidence |
| --- | --- | --- | --- |
| Opening track card and introductory view | Authored entry onto the first road leg | Riders roll down the road with local steering | MX-002 |
| Live road and first readable cue group | Choose an applicable push or trick input | The selected action takes place within the ride | MX-003 |
| Car approaching a controllable rider | Time the ollie over the car as in W2 | Rider lands and continues while Xbox shows the optional award | MX-004 |
| First downhill ride after the tunnel | Arrive at the authored handoff after the title | First scripted roadside scene | MX-005 |

## Strategic and experiential structure

The road keeps moving through each local choice. The player can use
the same descent to experiment with discrete tricks or to time one
against a car. The car interaction has a visible reward separate
from the scripted story pace.

## Replay and variation

The main trace reaches the story cut without an award notification.
The successful separate trace shows the optional notification during
rolling, rather than a course settlement screen. Previous account
unlocks, many other traffic models and collision recovery were not
established. No trick score counter appears in the scoped footage.

## Adjacent systems and history

The guide lists other skating chapters and the publisher describes
completely different interactive vignettes. Chapter-wide clearance,
a general skating career and any later control menus are separate scopes.

## Normalised genome

| Type | Stable genes | Role |
| --- | --- | --- |
| Action | ACT-008, ACT-901, ACT-902 | Steer, push or request a board manoeuvre |
| System Behaviour | SYS-1944, SYS-1945 | Roll along the prescribed course and confirm an optional clearance |
| Constraint | none | No independent constraint admitted |
| Information | INF-623 | Display successive live control pairs |
| Objective | OBJ-356 | Reach the staged scene handoff |
| Time | TIM-003 | Place local inputs against live progress |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `675` (`GAME-0001`–`GAME-0675`).
- Exact genome matches: none.
- Tied near matches: `GAME-0391` — Uncharted 2: Among Thieves (`2 / 11 = 0.181818`).
- Supported combination subsets: none.
- Scan date: 2026-11-24.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
| --- | --- | --- | --- |
| [Uncharted 2: Among Thieves (GAME-0391)](../s-z/uncharted-2-among-thieves.md) | ACT-008, TIM-003 | Both use direct local movement under live progression. Uncharted 2 uses authored grasp points and local climbing actions to survive the hanging-train escape. Mixtape carries the rider along a prescribed road with separate tricks and a car-clearance award before a story cut. | Near, `0.181818` |

## Taxonomy impact

Six narrow admissions distinguish the push and independent tricks,
automatic progress with local movement, an optional clearance award,
the staged cues and the authored exit. Two active genes already cover
direct local steering and the real-time input window.

## Negative results

- A distinct board trick does not imply a combo chain or score multiplier.
- The optional clearance and the ordinary roadside transition have
  separate receipts. No achievement requirement for the exit was found.
- Exact movement bounds, physical input timings, collision recovery
  and no-input completion were not tested.

## Delta summary

Eight genes: six new and two reused. The record covers one Xbox
board-control leg and the first roadside story handoff.

## New facts

- Live Push and Ollie cues are followed by Flip Trick and Grab Trick.
- The car interaction can earn a separate achievement during traversal.
- The authored roadside cut is an observable end to the first board leg.

## Principles and design implications

A ride can expose moment-to-moment self-expression even while
its broad direction is prescribed. A timed obstacle can have its
own feedback without controlling access to the following scene.

## Puzzle or game generation potential

Use a new short course with steerable lane offsets and passing
objects. Reveal local control affordances during travel. Track an
optional clearance independently of the route handoff.

## New genes

- ACT-901
- ACT-902
- INF-623
- OBJ-356
- SYS-1944
- SYS-1945

## New combinations

None. All 274 verified combinations were checked as proper subsets.

## Taxonomy changes

[TAXONOMY_CHANGE_422](../../../research/taxonomy-changes/TAXONOMY_CHANGE_422.md).

## New questions

- Does an input-free replay traverse this leg through the same cut?
- Which exact interactions qualify for a platform achievement?
- What feedback distinguishes a missed jump from a collision?

## Next recommended game

Continue Selection 058 with `GAME-0677`, Stunt Car Racer on Amiga.
Test an authored circuit's speed and landing demands against its
race or practice receipt.

## Why this game

The opening ride separates live steering and expressive tricks from
an authored story handoff and a separate timing-sensitive award.
