---
game_id: GAME-0669
slug: wilmot-works-it-out
game_title: "Wilmot Works It Out"
analysis_status: reviewed
reviewed: 2026-11-23
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-009
    - ACT-048
    - ACT-341
    - ACT-891
    - ACT-892
  system:
    - SYS-1918
    - SYS-1919
  constraint:
    - CON-884
  information:
    - INF-615
  objective:
    - OBJ-004
  time: []
---

# Game: Wilmot Works It Out

This record uses the [canonical vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
The apple art, tile count, bindings, wall coordinates and parcel order are parameters.

## Analysis scope

- Version / ruleset: English macOS commercial Steam release of October
  23, 2024, app 2060590. Ordinary solo Puzzle Club, first season, default
  joining behaviour, Braeburn after the first picture. The launch rule
  family is the target. Native macOS executable build and exact patch
  were not inspected.
- Structured analysis target: PLAT-MACOS in `knowledge/platforms/games.json`.
  P1 and P2 identify the platform and retail distribution. W1 explicitly
  shows 1.002 WindowsPlayer on the launch date. W2 is a later Steam-
  attributed trace with platform and build unverified. The shared rules
  are supported by the publisher and creator without a macOS-specific
  implementation claim.
- Entry: the first picture is hung, the floor is accessible and its
  surplus tiles remain. Sam arrives with the second parcel. Begin at
  the door before collecting and unpacking that parcel.
- Primary decision loop: accept the parcel and open it in a clear
  floor area. Inspect the square faces and separate likely apple
  pieces from unrelated ones. Push loose pieces or pick up and
  reposition tiles and connected groups. Turn the held positions
  around Wilmot as needed, then test candidate relative edges until
  the named picture is complete. Move the accepted picture into the
  wall view, choose its location and confirm.
- Exit: Braeburn is on the gallery wall beside or below the earlier
  picture. Ordinary floor control has resumed with surplus tiles
  still available. Stop before the subsequent multi-piece exercise
  and opening the next parcel.
- Included: local movement and contextual door and parcel interaction,
  direct pushing and pickup, held-position rotation, free-floor edge
  joining, incomplete versus recognised picture, guided wall
  placement and surplus-tile continuity.
- Excluded: the first picture's assembly, subsequent parcel solutions,
  deliberate group splitting, independent multi-pick tutorial after
  this result, pets, room decoration beyond the one wall mount,
  unlocks, Marathon Mode, modified joining settings and reloads.
- Potential scoped modules: one picture that requires more than one
  later parcel, or grouping and splitting under controlled options.

## Direct-play status

No personal play, commercial install or native macOS capture. Finji
identifies the shared PC and Mac release, the gallery loop and mixed
deliveries. The creators report choosing which image to complete from
a set of mixed pieces. Review-copy W1 is from launch day and identifies
a Windows build. Sponsored W2 corroborates the ordinary picture result
and different accepted placement. Only background static video frames
were inspected without audio. Physical inputs, platform-specific
behaviour, exact snapping tolerance and persistence across restart
remain unverified.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
| --- | --- | --- | --- | --- | --- |
| WWO-001 | Finji released the commercial PC and Mac game on October 23, 2024. Steam app 2060590 lists macOS and English. | Observation | Direct | High | P1, P2 |
| WWO-002 | A newly delivered parcel can be opened on the hall floor alongside retained earlier fragments. During Braeburn assembly the ordinary play view shows uniformly square faces without a finished target preview or placement board. | Observation | Corroborated | High | P2, P3, W1 1:28–1:44, W2 2:07–2:23 |
| WWO-003 | Local control permits pushing a loose tile, picking up and moving pieces and turning the attachment positions of held pieces about the avatar. During the last move the fragment's face stays readable in the same direction. | Observation | Corroborated | High | W1 1:41–1:56, 3:06–3:09, W2 2:17–2:51 |
| WWO-004 | Compatible real picture neighbours join along authored relative edges and can move together. The player assembles on the open floor and rejects false neighbours without a candidate picture preview. | Observation | Corroborated | High | P3, W1 2:20–2:43 and 3:04–3:09, W2 3:10–3:30, H1 |
| WWO-005 | The ninth required Braeburn tile triggers the named completion and the assembled picture remains carryable. The other squares remain separate. | Observation | Corroborated | High | P2, W1 3:06–3:14, W2 3:26–3:34 |
| WWO-006 | The completed picture enters a distinct gallery placement mode. Confirming a wall location fixes the displayed picture and restores floor control with unused pieces still on the floor. | Observation | Corroborated | High | P2, W1 3:13–3:37, W2 3:34–3:45 |

## Basic data

- Release / origin: Hollow Ponds, Richard Hogg and Talha Kaya, published
  by Finji. 2024. Single-player picture assembly. Scope is the launch
  commercial macOS release rules.
- Families: FAM-004 for edge compatibility and grouping, FAM-006 for
  spatial reconstruction of a finite picture.
- P1: [Finji launch notice](https://finji.co/news/2024/10/23/wwio-out-now.html).
  Announces the released Mac and PC editions and the developers'
  inspiration from assembling puzzles without a box image.
- P2: [Official Steam listing, app 2060590](https://store.steampowered.com/app/2060590/Wilmot_Works_It_Out/).
  Identifies the retail Mac release, date, floor-to-wall cycle and
  additional pieces in a delivery.
- P3: [Hollow Ponds developer interview](https://store.epicgames.com/news/hollow-ponds-talk-about-their-journey-from-stocking-shelves-to-launching-wilmot-works-it-out?lang=en-US).
  Explains grouping mixed pieces and selecting the currently finishable
  image to advance the delivery cycle.
- W1: [SUBWAY CIRCUIT, release-day Season 1 trace](https://www.youtube.com/watch?v=pGTwneJJ1j4&t=88s).
  The title at 0:00 identifies version 1.002 WindowsPlayer. The
  creator discloses a review copy. The route mounts Braeburn below
  the earlier picture.
- W2: [The Cozy Gaming Club, later Steam-attributed trace](https://www.youtube.com/watch?v=VumX5UiYXsA&t=113s).
  The creator discloses publisher sponsorship. The route places
  Braeburn to the right of the entrance. OS and exact build are
  unverified.
- H1: [XTgamer, launch-day PC play](https://www.xtgamer.net/2024/10/23/review-wilmot-works-it-out/).
  The firsthand PC review describes automatic accepted adjacency and
  independent pieces. It is used as control corroboration.
- Claim IDs: WWO-001–WWO-006.

### Reproducible route evidence

1. Start just before Sam's second delivery, after the first picture is
   mounted. Walk to the door and take the new parcel. Pick an open
   position in the hall and unpack it. W1 around 1:38–1:44 shows new
   squares next to the earlier surplus.
2. Identify likely apple fragments by their continuous red, orange
   and green shapes. Let unrelated fragments wait nearby. The
   tutorial permits pushing a loose tile and picking one up to
   carry and release it. W1 around 1:53 shows the held-position
   rotate instruction. At 3:07–3:08 the carried final fragment
   moves from north to east of Wilmot.
3. Bring compatible edges together without using a placement outline.
   W1 around 3:06 shows a three-by-three assembly with the lower
   left corner missing. The remaining compatible tile joins by
   about 3:09. A completion cue names Braeburn and several unused
   squares are still visible. W2 around 3:26–3:30 reaches the
   same result with a different order of final pieces.
4. Move the accepted picture toward the gallery wall. W1 around
   3:13 shows the separate wall operation, then a wall view used
   to choose a location. Position the frame and confirm it. The
   floor returns around 3:33–3:37 with spare pieces. W2 around
   3:34–3:45 corroborates the handoff and leaves its frame on
   the other side of the doorway. Stop when floor control returns.

## Mechanical decomposition

### Action Genes

- ACT-008: move Wilmot across the hall to the parcel, working
  fragments and wall. WWO-002, WWO-003, WWO-006.
- ACT-009: walk against a loose square and displace it away from the
  approach side. WWO-003.
- ACT-048: pick up a tile or bonded group, move it with Wilmot and
  release it back on the floor. WWO-003, WWO-004.
- ACT-341: interact at the door and then open the parcel in the
  work area. WWO-002.
- ACT-891: turn the held attachment position around Wilmot before
  approaching the final edge. The fragment artwork retains its
  reading direction. WWO-003.
- ACT-892: choose and confirm a wall position for Braeburn after
  the floor assembly is recognised. WWO-006.

### System Behaviour Genes

- SYS-1918: eligible contact bonds adjacent tiles while preserving
  their internal layout in the movable group. WWO-004.
- SYS-1919: recognise the complete picture, enable transfer to the
  wall and retain unused floor fragments after placement. WWO-005,
  WWO-006.

### Constraint Genes

- CON-884: only correct authored neighbour offsets bond. Similar
  colours and the common tile shape do not qualify a false edge.
  WWO-004.

### Information Genes

- INF-615: inspect the faces of mixed square fragments without a
  finished target image or a fixed blank board. WWO-002, WWO-004.

### Objective Genes

- OBJ-004: reconstruct the exact Braeburn layout with its full set
  of nine squares. Settlement uses the recognised picture. WWO-005,
  WWO-006.

### Time Genes

No independent time limit or timing predicate is needed for assembly
and placement in this scope.

## Reproducible transitions

| From | Input or event | To | Evidence |
| --- | --- | --- | --- |
| First artwork hung, older tiles loose | Receive second parcel and open on the hall floor | New tiles share workspace with surplus | WWO-002 |
| Loose tile beside Wilmot | Push or pick up and carry | Tile translated into a new trial position | WWO-003 |
| Final fragment held above Wilmot | Turn attachment position | Fragment is held at the right with unchanged art orientation | WWO-003 |
| Compatible fragments in matching relative positions | Bring their edges together | Bonded, movable group | WWO-004 |
| Eight correctly connected apple squares, bottom left missing | Bring ninth tile to the remaining matching edges | Named Braeburn completion, with unrelated tiles left | WWO-005 |
| Recognised picture before hanging | Switch to wall view, choose and confirm placement | Wall retains the picture and ordinary floor control resumes | WWO-006 |

## Strategic and experiential structure

The same square footprint and bright colours recur across different
pictures. Image continuity suggests a neighbour but the joined state
establishes it. A false candidate can stay near the assembly without
being consumed. Moving an attached partial picture preserves earlier
work and makes it practical to work in more than one part of the
room. The wall command settles the accepted picture while leaving
the next sorting problem intact.

## Replay and variation

W1 and W2 solve the same authored picture through different orders.
The remaining gap near the end is a consequence of the chosen
order, with no required final edge. They place the accepted picture
in different wall positions. The ordinary successful attachment and
settlement are evidenced. The tests do not measure snap distance or
assume that a colour-matched false edge has a visible rejection cue.

## Adjacent systems and history

The creators adapted direct tile handling from Wilmot's Warehouse.
Here the fragments form visually authored pictures, and retained
unused tiles make parcel boundaries differ from puzzle boundaries.
The next knock and later group tutorial sit after this exit.

## Normalised genome

| Type | Stable genes | Role |
| --- | --- | --- |
| Action | ACT-008, ACT-009, ACT-048, ACT-341, ACT-891, ACT-892 | Move, push, carry, unpack, turn attachments and place |
| System Behaviour | SYS-1918, SYS-1919 | Bond eligible edges and settle the picture selectively |
| Constraint | CON-884 | Enforce authored relative edge compatibility |
| Information | INF-615 | Show mixed tile artwork without the solution image |
| Objective | OBJ-004 | Reconstruct the exact connected picture |
| Time | None | No independent time predicate admitted |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `668` (`GAME-0001`–`GAME-0668`).
- Exact genome matches: none.
- Tied near matches: `GAME-0006` — Sokoban (`3 / 17 = 0.176471`).
- Supported combination subsets: none.
- Scan date: 2026-11-23.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
| --- | --- | --- | --- |
| [Sokoban (GAME-0006)](sokoban.md) | ACT-008, ACT-009, OBJ-004 | Both directly steer a character, push pieces and reconstruct a required configuration. Sokoban pushes crates through a bounded grid onto fixed goal cells, with corner traps and no ordinary pulling. Wilmot can pick up pieces and joined groups, compose the picture anywhere on an open floor through relative edges and hang it while surplus remains. | Near, `0.176471` |

## Taxonomy impact

Six definitions separate held-position turning, accepted wall
placement, relative picture-neighbour compatibility, visible mixed
square faces without preview, moveable groups and selective
settlement. Five existing boundaries cover the ordinary actions and
configuration objective. The joining rule is tested relative to
other tiles and requires no fixed outline.

## Negative results

- Emptying the parcel, moving all tiles or making a rectangle of
  plausible colours does not establish the complete picture.
- Turning the position of the held final square does not require
  reorienting the painted face.
- The completion cue appears before the wall command, while
  mounting leaves unrelated squares on the floor.
- The captures establish neither across-save persistence nor
  exact collision tolerances or platform-specific differences.

## Delta summary

Eleven admitted genes, including five reuses and six additions.

## New facts

- Shared square shape places more weight on visible art continuity.
- The nine connected tiles suffice without using all floor objects.
- Separate placement settles the completed work into the wall display.

## Principles and design implications

Use mixed surplus to separate the scope of a delivery from the scope
of a puzzle. Give the player enough floor space to keep more than one
hypothesis and allow correct partial assemblies to move intact.

## Puzzle or game generation potential

Offer two independent images in one tile supply. Keep faces readable
while the carrier turns to approach difficult edges. Use the exact
adjacency graph to recognise one whole image, then remove that
image by a separate placement action while the other pieces remain.

## New genes

- ACT-891
- ACT-892
- CON-884
- INF-615
- SYS-1918
- SYS-1919

## New combinations

None. All 274 verified combinations were checked as proper subsets.

## Taxonomy changes

[TAXONOMY_CHANGE_415](../../../research/taxonomy-changes/TAXONOMY_CHANGE_415.md).

## New questions

Does bond suppression change recognition timing? Which later
deliveries make more than one picture completable at the same
time? Can wall placements affect floor access in another room?

## Next recommended game

Phantom Dust on the original North American Xbox. Follow one story
battle through skill use, Aura spending and its accepted result.

## Why this game

The second picture shows that free-floor assembly, puzzle completion
and removal to a gallery can remain three separate gameplay states.
