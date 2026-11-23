---
game_id: GAME-0666
slug: chicory-a-colorful-tale
game_title: "Chicory: A Colorful Tale"
analysis_status: reviewed
reviewed: 2026-11-23
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-887
  system:
    - SYS-1913
    - SYS-1914
  constraint:
    - CON-881
  information:
    - INF-001
  objective:
    - OBJ-026
  time: []
---

# Game: Chicory: A Colorful Tale

This record uses the [canonical vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
The forest name, chosen hue, local compass directions and the two mushroom
positions are parameters. The rules describe the first local crossing.

## Analysis scope

- Version / ruleset: English commercial Xbox Series X|S base game, Finji,
  Xbox product 9PFGQGC0XWLV, released on Xbox on May 30, 2023. The
  official store lists Series optimisation and Smart Delivery. The
  recorded installed build, controller bindings and exact Series
  console are unverified.
- Structured analysis target: PLAT-XBOX-SERIES in
  `knowledge/platforms/games.json`. The linked Xbox listing identifies
  the commercial edition. It is not a claim of ownership or runtime
  verification.
- Entry: in Chapter 1, after acquiring the basic Brush and meeting
  Blackberry south of Luncheon, follow the south path into the first
  Supper Woods clearing. Begin on the right approach, with the lower
  mushroom dormant and the left shelf across the narrow channel.
- Primary decision loop: read the current shelf, visible cap and far
  landing. Aim the Brush at the lower mushroom from the right approach
  and apply pigment. Step left into the enlarged cap. Let the automatic
  launch land, then steer the avatar down the left path into the next
  clearing.
- Exit: the avatar lands on the left shelf, walks out at the lower
  edge and regains ordinary movement in the next Supper Woods clearing
  with a row of dormant mushrooms. The successor movement is visible
  in W1. End before solving its optional gift route.
- Included: the separate brush and body positions, local dab, dormant
  and enlarged mushroom states, ordinary approach, automatic
  directional launch, shrink and paint ring, landing, exit and
  resumed control.
- Excluded: the earlier palm-tree crossing, tower acquisition sequence,
  painting for decoration, optional gifts, landing-direction changes
  and chained mushrooms in the successor, bosses, later glow and
  swim powers, co-op, persistence across reload, and other editions.
  No exact paint radius, flight trajectory, default reaction speed,
  input sampling or re-entry save state is asserted.
- Potential scoped modules: the successor's landing-direction puzzle
  and the separate light-dependent Yum Cave route.

## Direct-play status

No personal installation or direct play. The Xbox store and Finji
identify the product and the basic use of the Brush. An Xbox
Series X|S-attributed gameplay recording shows paint, growth, launch,
shrink and the next playable clearing. The Xbox walkthrough
independently documents the same route as L08 followed by M08.
An independent capture of unspecified platform repeats the crossing
with orange paint. Static frames were inspected without audio. The build, physical
controller inputs and reference console model remain unverified.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
| --- | --- | --- | --- | --- | --- |
| CHIC-001 | Finji's finished Xbox release is product 9PFGQGC0XWLV, dated May 30, 2023, and lists native Xbox Series optimisation, single-player support and Smart Delivery. | Observation | Direct | High | P1 product details, P2 release platforms |
| CHIC-002 | The world brush acts at its own visible aim point. The avatar can remain beside the target while the player dabs pigment onto it. | Observation | Corroborated | High | P2 environment description, G1 controls, W1 10:18–10:21 |
| CHIC-003 | The lower mushroom becomes a large cap after contact with paint. The avatar on the right can then approach it leftward. The upper mushroom remains small in the demonstrated setup. | Observation | Corroborated | High | G2 L08, W1 10:18–10:22, W2 12:11–12:14 |
| CHIC-004 | Entering the prepared lower cap triggers automatic leftward flight, spends its enlarged state and leaves a ring. A fresh application of paint can prepare a mushroom again. | Observation | Corroborated | High | G1 Mushrooms, G2 L08 and M08, W1 10:21–10:24, W2 12:13–12:15 |
| CHIC-005 | The first flight reaches the left shelf. The avatar then follows the left edge south, the screen changes and ordinary movement resumes in the new clearing. | Observation | Corroborated | High | G2 L08 to M08, W1 10:22–10:28, W2 12:14–12:17 |

## Basic data

- Developer: Wishes Ultd. / Greg Lobanov and team. Publisher: Finji.
  W1 concerns the 2023 Xbox release. Finji's 2021 date refers to the
  original release, which precedes that edition.
- Families: FAM-003 (state transformation). A local paint operation
  changes the dormant fixture's state and makes the destination reachable.
- P1: [Xbox commercial listing](https://www.xbox.com/en-US/games/store/p/9PFGQGC0XWLV).
- P2: [Finji release and feature overview](https://finji.co/games/chicory/).
- G1: [TrueAchievements Xbox controls and fixture guide](https://www.trueachievements.com/game/chicory-a-colorful-tale/walkthrough/2).
  Default brush actions and the grown launch-cap interaction.
- G2: [TrueAchievements Xbox Chapter 1 route](https://www.trueachievements.com/game/chicory-a-colorful-tale/walkthrough/3).
  The labels L08 and M08 are guide coordinates rather than an in-game
  clear screen. The guide describes building and spending the lower
  mushroom and walking down to the next clearing.
- W1: [Lutfi Barakat, Xbox Series X|S Chapter 1 capture](https://www.youtube.com/watch?v=_7f7Xjcf2jw&t=595s).
  Blackberry dialogue at about 10:00 follows the Luncheon path;
  the relevant contact and exit span 10:14–10:28.
- W2: [Hawky, independent Chapter 1 capture](https://www.youtube.com/watch?v=6A4BbnENYgs&t=730s).
  At 12:11–12:17 both mushrooms grow with orange pigment. Only the
  lower one is used to cross from right to left, then the player moves
  in the successor. The capture is used for mechanical parity across
  the two traces. Its platform is unverified.
- Claim IDs: CHIC-001–CHIC-005.

### Reproducible route evidence

1. With the basic Brush in Chapter 1, walk south from Blackberry
   into Supper Woods. W1 shows the area title around 10:15, then
   movement down and left along the right approach at 10:17–10:20.
   The specific cap across from the right shelf is still small.
2. Place the brush cursor on the lower mushroom and apply pigment
   from the right shelf. W1 at 10:21 shows the red cap enlarged
   while the cyan avatar still stands to its right. The upper,
   unpainted cap remains small. W2 crosses with orange paint. G2 describes painting the cap
   without naming a required hue.
3. Steer into the prepared cap from its right side. W1 at 10:22
   shows the launch and paint burst, the ring and a reduced cap in
   the ensuing frames, and the avatar separate on the left shelf
   around 10:23. The visible change separates aiming, preparation
   and spending of the fixture. The trace does not expose a measured
   trajectory or stick samples.
4. Follow the left shelf down. The boundary transition begins
   at about 10:25. At 10:26–10:28 the avatar moves in the next
   clearing above a row of small mushrooms. Entering and moving there
   is the local result. The gift shown later is a different puzzle.

## Mechanical decomposition

### Action Genes

- ACT-008: steer the same avatar along the approached shelf and out
  through the left-side continuation. CHIC-003, CHIC-005.
- ACT-887: point the Brush independently and dab the addressed
  mushroom while standing beside the channel. CHIC-002, CHIC-003.

### System Behaviour Genes

- SYS-1913: a brush mark on the dormant mushroom changes it into a
  larger launch-ready cap at the same location. CHIC-003.
- SYS-1914: entry into the enlarged cap launches the avatar in its
  ordinary approach direction, shrinks the cap and leaves pigment.
  Repainting can restore the prepared state. CHIC-004, CHIC-005.

### Constraint Genes

- CON-881: the short crossing needs a prepared cap at the reachable
  local approach and an accessible far landing. Painting at a distance
  alone does not move the avatar. CHIC-003–CHIC-005.

### Information Genes

- INF-001: the board for this local choice exposes both ledges, avatar,
  cap size and the independent brush cursor. A player can see the cap
  change before attempting the crossing. CHIC-002–CHIC-004.

### Objective Genes

- OBJ-026: make the left shelf reachable and actually move to it and
  onward to the first playable clearing. CHIC-004, CHIC-005.

### Time Genes

No separate timing gene. Preparation has no shown deadline; the
automatic flight is part of SYS-1914. The bounded puzzle verifies
neither a real-time race nor a discrete turn protocol.

## Reproducible transitions

| From | Input or event | To | Evidence |
| --- | --- | --- | --- |
| Right shelf and lower dormant cap | Put a brush mark on the lower mushroom | Large cap and same avatar foothold | CHIC-002, CHIC-003 |
| Right shelf and enlarged cap | Walk left into the cap | Automatic leftward flight, spent cap and paint ring | CHIC-004 |
| Flight | Allow the route to resolve | Supported left shelf | CHIC-004, CHIC-005 |
| Supported left shelf | Steer down through the visible route | Next clearing, with playable walking | CHIC-005 |

## Strategic and experiential structure

Treat the cap as a renewable route operation. First choose which
fixture can reach the desired landing from the starting shelf.
Painting changes the available route before contact. The walking
direction then commits the launch. The ring is a readable receipt
for the use, while the reduced cap makes its depleted state visible.

## Replay and variation

A second preparation can replenish a used cap in a compatible
approach. The first crossing needs only the lower fixture. The
successor is a separate authored opportunity to combine fixtures and
choose a different incoming direction. Exact re-entry and save
behaviour remains untested.

## Adjacent systems and history

The developer describes an adventure built around painting and
environment changes. Later abilities and other genres of choice occupy
larger portions of the game; this record covers only the completed
Chapter 1 traversal.

## Normalised genome

| Type | Stable genes | Role |
| --- | --- | --- |
| Action | ACT-008, ACT-887 | Walk or address a pigment mark independently |
| System Behaviour | SYS-1913, SYS-1914 | Prepare the fixture, then spend it through directional contact |
| Constraint | CON-881 | Gate the crossing by ready local cap and landing geometry |
| Information | INF-001 | Expose the current cap, ledges, avatar and cursor |
| Objective | OBJ-026 | Make the left landing reachable and navigate into the successor |
| Time | None | No additional timing rule admitted |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `665` (`GAME-0001`–`GAME-0665`).
- Exact genome matches: none.
- Tied near matches: `GAME-0098` — Hyperbolica (`3 / 11 = 0.272727`).
- Supported combination subsets: none.
- Scan date: 2026-11-23.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
| --- | --- | --- | --- |
| [Hyperbolica (GAME-0098)](../g-l/hyperbolica.md) | ACT-008, INF-001, OBJ-026 | Both steer a visible subject through a spatial route to a specific reachable place. Hyperbolica chooses junctions in fixed non-Euclidean geometry. Chicory changes a local launcher with pigment and spends that state on contact before ordinary walking resumes. | Near, `0.272727` |

## Taxonomy impact

ACT-887 describes an aimed marking action that is distinct from
movement of the supported body. SYS-1913 records preparation by paint.
SYS-1914 records the spent-state change on entering the launcher.
CON-881 declares the local availability and approach boundary. The
comparison reuses independent walking, state visibility and place
reaching. It preserves the distinctions between light-grown support,
painted path footprints and already-live bumpers.

## Negative results

- Painting from the right shelf does not by itself move the avatar.
- A visible pigment ring can remain after the cap has shrunk. Paint
  residue alone is insufficient evidence of launch readiness.
- The launched path requires no complete bridge across the channel.
- Entrance into M08 does not require claiming its gift.
- The trace does not establish fixed flight coefficients, a particular
  reaction-speed setting, or saved states on backtracking.

## Delta summary

Three reused genes and four newly isolated boundaries.

## New facts

- One cap changes reachability in place when a brush mark lands on it.
- Entering the cap spends its readiness and resolves a leftward flight.
- Restored walking on the far side leads directly to the next clearing.

## Principles and design implications

Separate the world-editing cursor from the moving character. Make the
preparation readable as a shape change and the spent state readable
as a separate smaller shape with a visible use trace. That supports
learning the route through one target and one crossing.

## Puzzle or game generation potential

A new spatial puzzle can use a renewable launcher in an otherwise
static room. Compare entrances, paintable caps and supported landings
while keeping the palette decorative. Do not infer a successful exit
from a prepared geometry alone.

## New genes

- ACT-887
- SYS-1913
- SYS-1914
- CON-881

## New combinations

No verified combination is a proper subset of the seven-gene scope.

## Taxonomy changes

[TAXONOMY_CHANGE_412](../../../research/taxonomy-changes/TAXONOMY_CHANGE_412.md).

## New questions

What approach directions are accepted at cap contact, and when can an
incoming flight direction be overridden? What exact fixture state is
stored on exiting and re-entering the clearing?

## Next recommended game

Selection 056 ends with this unit. Scope the next candidate through
a separate selection decision.

## Why this game

A completed brush-and-traversal test isolates paint that changes
reachability from paint that merely changes appearance.
