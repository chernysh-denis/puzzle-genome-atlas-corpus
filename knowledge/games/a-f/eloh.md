---
game_id: GAME-0711
slug: eloh
game_title: "ELOH"
analysis_status: reviewed
reviewed: 2026-11-25
combination_ids: []
gene_ids:
  action:
    - ACT-014
    - ACT-072
  system:
    - SYS-1995
    - SYS-1996
  constraint:
    - CON-896
  information:
    - INF-001
    - INF-646
  objective:
    - OBJ-014
  time: []
---

# Game: ELOH

This record uses the [canonical vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
Move percussion blocks between marked positions to redirect a live
stream of balls into a receiver. An arrow opens the next board after
delivery is acknowledged.

## Analysis scope

- Version / ruleset: the early English-interface commercial Android
  Google Play edition, package `es.brokenrul.eloh`. Broken Rules dates
  release to October 2018. The launch-era witness links the Android
  package and tags its gameplay as Android. Its binary and device
  model are unverified. The present listing reports an October 2025
  update. Its installation and exact build are outside this fixture.
- Structured analysis target: PLAT-ANDROID in
  [platform coverage](../../platforms/games.json).
- Entry: Level 1, with the lower-left emitter stopped and the only
  percussion block at the upper of two marked diagonal berths. The
  circular receiver is fixed to the emitter's right.
- Primary decision loop: start repeated emission, inspect where the
  current bounce goes, and move the block to the lower berth while
  the board stays active. Follow the corrected rebounds into the
  receiver and use the newly exposed progression arrow.
- Positive terminal: the Level 2 title appears after the arrow is
  used. A Level 2 example checks the same routing rules with two
  separate moves and consecutive rebounds. Stop its trace at the
  next level title.
- Included: direct block repositioning, marked berths, repeat
  emission, square-block diagonal bounce, local hit feedback and
  explicit continuation. Sound associations are documented by the
  developer and the walkthrough. The spatial fixture is observable
  with the sound off.
- Excluded: later bar, triangle, portal and colour-changing rules,
  exact release build, audio timing or mix, independently measured
  shot period, hit quota, progress persistence and iOS differences.
- Potential scoped module: separate the effect of colour-matched
  bars on projectile reflection and transmission on a later board.
- Direct-play status: no personal Android session, installed build
  inspection or input telemetry. The store and presskit establish
  the edition. The developer's Google Play trailer and the
  Android-attributed recording show the same one-block correction.
  The iOS-linked independent guide corroborates geometry and control
  behaviour. Frame inspection was in the background with no audio.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
| --- | --- | --- | --- | --- | --- |
| ELH-001 | Broken Rules released ELOH for Google Play and iOS in October 2018. The Android distribution is `es.brokenrul.eloh`. The store currently describes a paid touch-controlled game without a countdown. | Confirmed | Direct | High | P1, P2 |
| ELH-002 | Level 1 exposes a fixed lower-left emitter, a round receiver at the same height to its right and two marked diagonal berths for one movable percussion block. The upper berth is initially occupied. The lower berth becomes occupied after one block move and the upper one becomes vacant. | Observation | Corroborated | High | P3 0:03–0:05, W1 0:22–0:34, W2 0:39–0:45, W3 |
| ELH-003 | A tap on the emitter enables recurring shots along its visible diagonal. Moving the block changes the route of following shots without a restart or a further start command. W1 Level 2 shows the emitter stopped and started again separately from placement. | Observation | Corroborated | High | W1 0:25–0:32 and 0:44–0:51, W2 0:43–0:49, W3 |
| ELH-004 | A square percussion block redirects the incoming diagonal into a perpendicular diagonal. With the Level 1 block in its upper berth, the red ball continues down-right past the receiver's column at a different height. In the lower berth the rebound goes down-right into the receiver. Level 2 chains two such redirections. | Observation | Corroborated | High | P3 0:03–0:05, W1 0:26–0:34 and 0:45–0:54, W3 |
| ELH-005 | The contacted block visibly animates and the live balls and their short traces show the failed or successful route. The receiver pulses after hits. The publisher associates specific sounds with spirits and the independent guide attributes a sound to the bounce. Audio was unexamined. | Observation | Corroborated | High | P2, P3 0:04–0:05, W1 0:26–0:36, W3 |
| ELH-006 | Repeated valid delivery in the corrected position is followed by a bottom continuation arrow. The board remains visible with the arrow usable; transition is separate. Activating it slides away Level 1 and shows the Level 2 title. The samples do not establish a universal hit count. | Observation | Corroborated | High | W1 0:31–0:38, W2 0:45–0:52, W3 |
| ELH-007 | In Level 2 the right block is moved to its upper berth, then the left block to its lower berth. The ball travels down-right from the emitter to the right block, down-left to the left block and down-right into the fixed receiver. The result again offers the arrow. | Observation | Corroborated | High | W1 0:39–0:59, W3 Level 2 |

## Basic data

- Release / origin: 2018. The presskit credits jcstranger, Salon
  Alpin and Broken Rules as developers, with Broken Rules publishing.
- Families: FAM-005 for constructing a connected projectile route
  by placing its deflectors and FAM-007 for contact-driven routing.
- P1: [Broken Rules release facts and credits](https://brokenrul.es/presskit/ELOH/).
- P2: [ELOH on Google Play](https://play.google.com/store/apps/details?id=es.brokenrul.eloh),
  the official Android listing. The library now contains 98 puzzles.
  The launch trailer gives 85. The extra boards and current build
  are outside the early level scope.
- P3: [Broken Rules Google Play video](https://www.youtube.com/watch?v=Ck0oVOCN9yI&t=3s).
  The 3–5s edit depicts the same failed and corrected Level 1 route.
  Its next cut is promotional and cannot establish the actual advance.
- W1: [andro-games, early mobile playback attributed to Android](https://www.youtube.com/watch?v=WkZX249YIHA&t=22s).
  The author tags it Android gameplay and links Google Play, alongside
  a general iOS store link. The capture itself does not identify the
  operating system or binary.
- W2: [App Unwrapper, Levels 1–20](https://www.youtube.com/watch?v=jnERKkv5T1Q&t=43s).
  The linked App Store product makes this corroboration for visible
  route behaviour. It is not Android build evidence.
- W3: [App Unwrapper's launch-era walkthrough and solutions](https://www.appunwrapper.com/2018/10/11/eloh-walkthrough-guide-and-solutions/).
  The guide identifies the speaker toggle, drag-placement, impact
  sounds and the exit gesture.
- Claim IDs: ELH-001–ELH-007.

### Reproducible fixture evidence

1. On W1 0:22–0:25, leave the block in the upper-right marked
   berth. The lower berth lies down-left of it, on the same rising
   diagonal from the emitter. The round target is lower and left of
   the projected intersection of the upper rebound with receiver height.
2. At about 0:25, tap the emitter. Follow multiple up-right shots to
   the upper berth. Their down-right leg misses the receiver. The
   block responds each time, so block contact alone is insufficient.
3. Around 0:30, drag the single block to the lower-left berth while
   emission continues. An earlier ball still shows the old path.
   Subsequent rebounds travel into the receiver at about 0:31–0:32.
   The ring brightens and the bottom arrow rises by about 0:33.
4. Use that arrow. W1 shows the Level 2 title at about 0:37. W2
   independently shows the lower-berth success at 0:44–0:50 and
   the next title around 0:51.
5. For a two-block comparison, W1 0:39–0:44 moves the right block up
   and the left block down. After starting the emitter, follow the
   first and second rebounds between 0:45 and 0:48. Around 0:49 the
   board still shows the arrow when the stream stops. The source
   is started again around 0:50, with the placements retained. Level
   3 follows the arrow by about 0:59.

## Mechanical decomposition

### Action Genes

- ACT-014: drag one selected controlled block to its permitted berth.
  The single block can change position while the stream runs.
- ACT-072: address the visible emitter itself to start its
  automatic recurring output.

### System Behaviour Genes

- SYS-1995: an enabled emitter produces successive independent
  projectiles with an authored heading. It remains usable across
  different placements and can cease emission independently.
- SYS-1996: one square block resolves each eligible diagonal
  collision into a perpendicular outgoing leg. The leg can lead to
  empty space, another block or the target, depending on placement.

### Constraint Genes

- CON-896: eligible berths are authored and marked on the board.
  Moving a percussion block is limited to its permitted positions.

### Information Genes

- INF-001: the early board displays the authored devices, marked
  berths and current blocks together.
- INF-646: visible traces and distinct block and receiver responses
  expose the live route. The separate arrow signals progression.

### Objective Genes

- OBJ-014: cause the required projectile delivery into the fixed
  receiver to solve the active board.

### Time Genes

- No separate time gene. Recurring shots belong to the emitter rule.
  Live repositioning remains available without an attempt deadline.

### Parameters

Emitter heading and state, berth coordinates and eligibility,
incoming and outgoing diagonals, receiver location, feedback state
and continuation input. Exact rate and delivery threshold remain
unmeasured.

## Reproducible transitions

| Entry state | Input or event | Expected next state | Evidence |
| --- | --- | --- | --- |
| Level 1 with a stopped emitter and upper block | Tap the emitter | Recurring diagonal shots test the occupied berth | ELH-002–ELH-003 |
| Upper berth is occupied and emission is active | A ball reaches the block | The block responds and sends it past the target | ELH-004–ELH-005 |
| Upper route has missed | Move the block into the lower berth | Following balls take a lower parallel rebound into the receiver | ELH-002–ELH-005 |
| Corrected route repeatedly reaches the receiver | Observe the feedback | Receiver pulses and a separate continuation arrow appears | ELH-005–ELH-006 |
| Solved board with visible arrow | Use the arrow | The board gives way to the Level 2 title | ELH-006 |
| Level 2 starting arrangement | Raise the right block, lower the left and start emission | Two rebounds reach the receiver and expose the next arrow | ELH-007 |

## Strategic and experiential structure

The entry direction and receiver are fixed. Moving a block shifts
the interception point, which shifts the reflected line without
changing the emitter. Testing can continue while making the change.
The failed route leaves a visible comparison against the successful
one.

## Replay and variation

The first board contrasts two placements under one emitter state.
The second board holds the same two block types and requires a chain
of two bounces. It also allows emission to be restarted with positions
retained in the observed solved state. The exact point at which
stopping after a hit would withhold clearance is untested.

## Adjacent systems and history

The developer's original advertisement describes 85 levels. The
current store describes 98. Later board components and any physics
changes between Android versions are separate research subjects.

## Normalised genome

- Action: ACT-014, ACT-072.
- System Behaviour: SYS-1995, SYS-1996.
- Constraint: CON-896.
- Information: INF-001, INF-646.
- Objective: OBJ-014.
- Time: none.

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `710` (`GAME-0001`–`GAME-0710`).
- Exact genome matches: none.
- Tied near matches: `GAME-0421` — The Incredible Machine (`2 / 12 = 0.166667`).
- Supported combination subsets: none.
- Scan date: 2026-11-25.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
| --- | --- | --- | --- |
| [The Incredible Machine (GAME-0421)](../s-z/the-incredible-machine.md) | INF-001, OBJ-014 | ELOH moves one percussion block between authored berths during emission to steer repeated diagonal balls. The Incredible Machine positions inventory parts, runs the assembled mechanism and tests whether its routed ball completes the trial. | Near, `0.166667`. |

## Taxonomy impact

Reuse individually moving a piece, activating a visible mechanism,
reading a visible board and routing a payload into a fixed receiver.
Admit recurring fixed-heading emission, diagonal redirection at a
square block, authored berth restrictions and readable impact and
progression feedback.

## Negative results

- A block hit can produce a clear reaction while missing the receiver.
- Moving one block does not require launching a new attempt.
- An acknowledged delivery leaves a separate action before the board
  transition.
- The witnesses do not establish an audio input, rhythm score, numerical
  shot cadence, universal hit quota or behaviour of a later coloured bar.

## Delta summary

The same running source provides both the unsuccessful and successful
tests. Moving one block brings the reflected path onto the receiver;
the ready arrow separates arrival feedback from progression.

## New facts

- The emitter can be active while a repositionable block changes berths.
- Two consecutive legal impacts can form the required route.
- Receiver feedback and a separate advance control distinguish a hit
  from leaving the board.

## Principles and design implications

Keep a failed route readable so a single placement change can be tested
in context. Distinguish reacting to a collision, delivering a payload and
choosing the next board through separate cues.

## Puzzle or game generation potential

Use a fixed emitter, a fixed receiver and two legal positions on the
incoming diagonal. Generate an initial miss and a reachable reflected
line. A second fixture can require two successive deflectors. Confirm
that the wrong block arrangement continues the visible test and that the
correct one exposes a deliberate advance action.

## New genes

- CON-896
- INF-646
- SYS-1995
- SYS-1996

## New combinations

None.

## Taxonomy changes

[Taxonomy Change 457](../../../research/taxonomy-changes/TAXONOMY_CHANGE_457.md).

## New questions

- What exact arrival condition enables the advance arrow on each early board?
- Which additional berth classes and colour rules can be demonstrated in a
  fully delimited later Android fixture?

## Next recommended game

Close Selection 061 at the verified 711-game boundary. Record the
next nine released targets in a new selection before admitting a
further game.

## Why this game

The two early boards isolate an editable live route whose individual
collisions, successful delivery and explicit advance can be examined
separately.
