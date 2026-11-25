---
game_id: GAME-0689
slug: shadow-point
game_title: "Shadow Point"
analysis_status: reviewed
reviewed: 2026-11-24
combination_ids: []
gene_ids:
  action:
    - ACT-787
  system:
    - SYS-1964
    - SYS-1965
  constraint: []
  information:
    - INF-633
  objective:
    - OBJ-365
  time: []
---

# Game: Shadow Point

This record uses the [canonical vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
One small blue prop serves successive panels because an accepted shadow
match can remain credited after the prop moves.

## Analysis scope

- Version / ruleset: English commercial standalone Oculus Quest base
  game, released May 21, 2019, store ID 2088119334554800. The scope
  is the first outdoor shadow courtyard in The Crown, in launch-era
  recordings identified as original Oculus Quest. Exact installed
  builds were not verified.
- Structured analysis target: PLAT-META-QUEST in
  [platform coverage](../../platforms/games.json). The ID is the
  current registry family. The analysed device is the first Oculus Quest.
- Entry: after opening the entrance to The Crown, proceed to the
  nighttime courtyard with its framed screens, blue cube-like
  box and linked side passage. Start before solving its first
  required screen.
- Primary decision loop: grip the portable box with a controller-tracked hand.
  Move or turn it to compare the projected shadow with a fixed
  outline. Adjust the pose until a panel credits the match. Take
  the same box to the next required screen and use the open passage
  after the three matches.
- Positive exit: pass the courtyard side opening and cross into the
  warm-lit hall. Stop with movement available before any hall puzzle
  input. The beginning of the next screen confirms the destination.
- Included: direct tracked grip, held pose and cast silhouette,
  initially offset and accepted alignments, panel credit after the
  shadow changes, progressive target marks, three required panels
  and crossing the admitted route.
- Excluded: the cable car, observatory controls, prior entry
  mechanism, exact optics and matching tolerances, exact dwell
  times, later replay or save persistence, the separate rectangular
  compartment, collecting its item, further hall puzzles, later
  chapters and other headsets or ports.
- Potential scoped module: compare deliberately reordered courtyard
  matches and test retention after leaving and reloading the room.
- Direct-play status: no personal headset session, binary inspection
  or controller telemetry. The creator and platform pages identify
  the release. Two original Quest captures independently show the
  fixture and route. Only background visual frames were examined,
  without audio.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
| --- | --- | --- | --- | --- | --- |
| SP-001 | Coatsink's commercial puzzle game launched on May 21, 2019 with an original standalone Oculus Quest product. The Quest edition has its own listing, separate from the Rift product. | Confirmed | Corroborated | High | P1, P2, P3, P4, W1 |
| SP-002 | The tracked hand takes the blue box and moves it before a fixed panel. Translation displaces the live shadow while turning the box can alter its silhouette. A square-like shadow that is offset from the target does not immediately credit the panel. | Observation | Corroborated | High | W1 5:30–6:10, W2 11:38–12:00 |
| SP-003 | Matching the first required square produces a visible acceptance on the panel. When the box moves down, the accepted patch remains at the intended position while the dark shadow moves away. The next panel can use the same box. | Observation | Corroborated | High | W1 6:06–6:16, W2 11:59–12:05 |
| SP-004 | The next courtyard marks show fewer square edges, including three sides and then two upright lines. The box's square-like projection is accepted again at those respective marks. Distinct accepted panels accumulate without holding three shapes in place. | Observation | Corroborated | High | W1 6:14–6:35, W2 12:05–12:32 |
| SP-005 | The third required match is followed by a distinct burst and a traversable side route into a warm hall. W1 reaches it without the separate rectangular compartment seen in W2. The footage does not isolate every possible order or the exact activation delay. | Observation | Corroborated | High | W1 6:28–6:56, W2 11:16–11:32 and 12:27–13:07 |

## Basic data

- Release / origin: Coatsink Software, Oculus Studios, May 21, 2019.
  The original Oculus Quest commercial base version supplies the
  bounded fixture.
- Mechanical families: FAM-003 for iterative adjustment toward
  a bounded set of projected targets, and FAM-014 for projections
  changing access to the authored next space.
- P1: [Official standalone Quest listing](https://www.meta.com/experiences/shadow-point/2088119334554800/).
  Establishes the product ID and puzzle premise.
- P2: [Coatsink's original Quest and Rift announcement](https://coatsink.com/blog/shadow-point-oculus-quest-and-rift).
  Establishes the target platforms and authored spatial interaction.
- P3: [Coatsink's commercial availability announcement](https://www.youtube.com/watch?v=BErmBakCIrk).
  Identifies both the original Quest and Rift launch. It is used
  for its dated announcement metadata.
- P4: [Meta's parallel Rift release listing](https://www.meta.com/experiences/pcvr/shadow-point/2175239282518665/)
  and [the Quest release catalogue](https://gamefaqs.gamespot.com/meta-quest/264604-shadow-point/videos/1262316).
  Match the May 21 date. Rift's version and hardware are not used
  as evidence of the Quest binary.
- W1: [VR Edward's original Oculus Quest route](https://www.youtube.com/watch?v=UMThhPW6rHo&t=323s),
  published May 29, 2019. Inspect 5:23–6:56 to see the handheld
  box, successive panel results and first movement in the hall.
- W2: [Nathie's original Oculus Quest capture](https://www.youtube.com/watch?v=uPjJ2MyUIJ8&t=690s),
  published August 30, 2019. Its headset and controller footage
  accompanies the game view. Check 11:38–13:07 for the three
  square targets and section exit. The 11:16–11:32 rectangular
  compartment provides an optional contrast.
- Claim IDs: SP-001–SP-005.

### Reproducible fixture evidence

1. At about 5:23–5:38 in W1 enter the courtyard. Locate the blue
   box, its tracked grasp and the square target on a fixed screen.
2. At 5:41–6:10 compare angular and offset silhouettes with the
   target. An outline and a dark shadow can both be visible
   without settling a result. Move and turn the held prop until
   the projection fits.
3. Around 6:11–6:12 the frame and target change. Look at the
   accepted patch with the live shadow now lower on the same
   panel. Follow the same prop to the next required target.
   W2 independently shows the first result around 12:02.
4. Use the blue box on the three-sided target around 6:16–6:29.
   Then compare the two vertical strokes at the last screen
   around 6:30–6:35. W2 shows these two solves around 12:20 and
   12:32. Both runs use individual alignments rather than leaving
   a separate solid on every screen.
5. In W1 turn toward the side entrance around 6:36–6:49, move
   into the small intermediate room and cross the bright opening
   at about 6:55. In W2 the same threshold is visible around
   12:47–12:59. Stop before manipulating an object in the hall.

## Mechanical decomposition

### Action Genes

- ACT-787: use an independently tracked hand to grip and
  reposition the portable box, carrying it between panels.
  W1 also releases and reacquires the prop after matching. SP-002–SP-004.

### System Behaviour Genes

- SYS-1964: held pose changes the shadow on the receiving surface
  before the prop is released. SP-002.
- SYS-1965: an accepted screen stays credited after the box and
  its live shadow move. SP-003–SP-004.

### Constraint Genes

No separate admission. The demonstrated geometric requirements
belong to the projected fit. The frames do not determine a numeric
tolerance, universal accepted scale or exact timing requirement.

### Information Genes

- INF-633: compare a target outline and the moving dark silhouette
  on the same surface, then distinguish the accepted display. SP-002–SP-003.

### Objective Genes

- OBJ-365: settle all three required panel matches and walk the
  admitted route. The separate compartment is not required. SP-004–SP-005.

### Time Genes

No separate admission. The two recordings show adjustment before
settlement. A minimum stable interval or failure clock was not isolated.

## Reproducible transitions

| From | Input or event | To | Evidence |
| --- | --- | --- | --- |
| Courtyard before any required match | Grip the blue box | Tracked hand carries the box between panels | SP-002 |
| Dark shadow offset or angled against the first square | Move and turn the held prop | Current dark silhouette changes on the fixed screen | SP-002 |
| Projected figure reaches the accepted fit | Panel recognises the match | The border responds and the target is marked separately | SP-003 |
| First screen has credited the square | Lower and carry the same box away | The first result remains while a different screen can be attempted | SP-003 |
| Three-sided and two-stroke targets remain | Use the same box’s square-like projection on each | Both additional panels credit their fits | SP-004 |
| All three required results are present | Follow the side route and cross the oval opening | Movement in the warm hall | SP-005 |

## Strategic and experiential structure

The first full outline demonstrates which silhouette can fit. Later
screens show fewer edges and ask the player to carry that geometric
relationship across panels. Credited results let the player take
the only demonstrated source prop onward. Moving the shadow and
changing what is already accepted are different operations.

## Replay and variation

The two captured players use different short alignments and take
different amounts of time. W2 also explores a rectangular compartment.
Both reach the hall after three required square-compatible projections.
The observations do not establish an arbitrary solve order or
persistence through a menu load.

## Adjacent systems and history

The chapter sits after the observatory opening and before a warm
hall with its own target. Coatsink identifies later reflection,
gravity, alternate views and orientation puzzles. These have
their own authored rules and do not enter this courtyard genome.

## Normalised genome

| Type | Stable genes | Role |
| --- | --- | --- |
| Action | ACT-787 | Grip, reposition and release a tracked prop |
| System Behaviour | SYS-1964, SYS-1965 | Project the changing pose and retain credited fits |
| Constraint | None | Geometric fit is scoped in projection and goal boundaries |
| Information | INF-633 | Show target, shadow and acceptance separately |
| Objective | OBJ-365 | Complete the required panels and use the opened route |
| Time | None | No independent timed requirement established |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `688` (`GAME-0001`–`GAME-0688`).
- Exact genome matches: none.
- Tied near matches: `GAME-0680` — Ghost Town (`1 / 15 = 0.066667`).
- Supported combination subsets: none.
- Scan date: 2026-11-24.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
| --- | --- | --- | --- |
| [Ghost Town (GAME-0680)](../g-l/ghost-town.md) | ACT-787 | Both let the tracked hand carry a portable prop. Ghost Town seats a replacement bulb and uses separate readiness and light-power controls. Shadow Point moves the held prop to cast target silhouettes and carries it onward after each accepted fit. | Near, `0.066667` |

## Taxonomy impact

The hand poses a real scene object, but the tested geometry is its
projected silhouette. The live change, readout, retained validation
and completed route are separate aspects of the observed puzzle.

## Negative results

- The prop need not touch or be inserted into the receiving screen.
- A visibly offset shadow can fail to settle a match.
- Once credited, the first panel does not require continued overlap
  while the same box is used elsewhere in the courtyard.
- The separate rectangular compartment is absent from the successful
  W1 route. It is not an additional gate requirement.
- The recordings do not determine the exact predicate for omitted
  edges, sub-frame timing or retention across a reload.

## Delta summary

Five genes, four newly admitted. Success separates manipulating
one physical object, projecting its silhouette and retaining a
set of individually accepted matches.

## New facts

- Rotating or translating one carried box changes its live shadow.
- A settled result leaves a distinct patch or frame state behind.
- The next required screens expose fewer target lines.
- The linked passage leads to a room with another puzzle family.

## Principles and design implications

Put the live output and its target in the same reference frame.
Show a distinct accepted state so the player can reuse the input
object with confidence and inspect their remaining goals.

## Puzzle or game generation potential

Design an original gallery where one clay solid can cast a
compatible outline on several screens. Let early marks show a
closed shape and later ones show only the edges needed for
comparison. Retain the accepted panel states and open one route.

## New genes

- SYS-1964
- SYS-1965
- INF-633
- OBJ-365

## New combinations

None. All 274 verified combinations were checked; no combination is a proper subset of this genome.

## Taxonomy changes

[Taxonomy Change 435](../../../research/taxonomy-changes/TAXONOMY_CHANGE_435.md).

## New questions

- Which differently ordered solves still open the passage?
- What numeric alignment tolerance applies in the same Quest build?
- Which accepted states persist after exiting and reloading?

## Next recommended game

Continue Selection 059 with `GAME-0690`, Sonic Advance on
the original English European Game Boy Advance cartridge.

## Why this game

A continuous physical gesture changes a live two-dimensional test.
Independent credit makes that gesture reusable on successive panels.
