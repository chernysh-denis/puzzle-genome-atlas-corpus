---
game_id: GAME-0708
slug: rampart
game_title: "Rampart"
analysis_status: reviewed
reviewed: 2026-11-24
combination_ids: []
gene_ids:
  action:
    - ACT-026
    - ACT-161
    - ACT-924
  system:
    - SYS-1988
    - SYS-1989
  constraint:
    - CON-001
    - CON-068
  information:
    - INF-645
  objective:
    - OBJ-371
  time:
    - TIM-003
---

# Game: Rampart

This record uses the [canonical vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
Place cannons inside a starting fort, fire at the ships, then close a
wall around a castle before the repair clock runs out.

## Analysis scope

- Version / ruleset: Atari Games' English commercial dedicated
  three-player trackball arcade release, in solo mode. The cabinet
  is catalogued as 1990, and Atari advertised the three-player and
  one-player modes by February 1991. The exact first distribution
  date and installed ROM revisions in the recordings are unverified.
- Structured analysis target: PLAT-ARCADE-CABINET in
  [platform coverage](../../platforms/games.json).
- Entry: the first solo home-castle selection in the uninterrupted W2
  peninsula route. The selected castle receives an initial enclosure.
  Observe one cannon placement, bombardment and rebuild sequence.
- Primary decision loop: site the allotted cannons inside the fort.
  Fire at the incoming ships, then use the current supplied shapes to
  close a perimeter around at least one castle on the breached board.
- Positive terminal: at least one castle is enclosed at repair expiry.
  Allow the score tallies to finish and stop at the next opportunity
  to place a cannon. W2 shows this entire passage without a cut.
- Negative witness: a separate W1 cycle expires with no enclosed
  castle and reports defeat. A later paid continuation, if offered,
  is a separate boundary from continuing the present successful cycle.
- Included: positioning fixed cannons in credited territory, directed
  fire at ships, carry-over of the breached board into rebuild,
  placing the supplied wall shapes and evaluating castle enclosure.
  Joystick kit, home ports, multiplayer, later infantry and rubble
  rules, paid continuation, later maps and full-run score strategy
  are outside this scope.
- Potential scoped module: compare a later landing wave with burning
  rubble against the clean first-cycle wall-repair board.
- Direct-play status: no personal cabinet or emulator session, ROM
  execution or input telemetry. Two attributed trackball-ruleset
  recordings were examined as silent frames. W2 reports using a
  mouse. W1 tentatively recalls using a mouse. Original hardware
  feel remains unmeasured.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
| --- | --- | --- | --- | --- | --- |
| RAM-001 | Atari documents the dedicated three-player trackball cabinet and a one-player mode against invading ships. The two-player joystick kit is a separate ruleset target. | Confirmed | Direct | High | P1 pp. 1-2–1-3, 2-2–2-3; P2; P3 input maps; R1 |
| RAM-002 | Choosing a starting castle gives an enclosed region. In the separately labelled placement phase, available cannons are placed on distinct locations inside the fort walls and remain visible there for battle. | Observation | Corroborated | High | P1 p. 1-3; W2 0:39–0:51; W1 0:52–1:06 |
| RAM-003 | During battle the player uses the placed cannons to fire toward the ships. Impacts are visible, and surviving cannon sites and a broken perimeter carry into the next board rather than reverting to their initial arrangement. | Observation | Corroborated | High | P1 p. 1-3; W2 0:51–1:09; W1 1:06–1:26 |
| RAM-004 | During the live rebuild phase the player moves and orients the current supplied wall shape on the finite map, then commits it to a legal position. Occupied cells and surviving wall runs remain in the layout. | Observation | Corroborated | High | P1 pp. 1-3, 2-2–2-3; W2 1:09–1:26; W1 1:23–1:44 |
| RAM-005 | The land stays green while the main castle has an open wall. Finishing a closed wall around a castle visibly marks the accepted interior blue before the clock expires. | Observation | Corroborated | High | P1 p. 1-3; W2 1:24–1:27; W1 1:38–1:44 |
| RAM-006 | With a castle enclosed at expiry, W2 settles destruction points and the castle bonus, then offers another cannon allotment on the surviving enclosure. Its repair display starts at 25 and reaches 00. Those readings belong to this observed setup. | Observation | Corroborated | High | P1 p. 1-3; W2 1:09, 1:26–1:44 |
| RAM-007 | With no castle enclosed at expiry in a distinct W1 cycle, the attempted walls remain uncredited and the blue army is defeated after the tally. | Observation | Corroborated | High | P1 p. 1-3; W1 2:46–3:06 |

## Basic data

- Release / origin: Atari Games, dedicated three-player trackball
  arcade machine, catalogued 1990 and advertised by February 1991.
  W1 and W2 are emulated solo witnesses of the trackball ruleset.
- Families: FAM-006 for fitting wall pieces together as a spatial
  assembly, and FAM-010 for deciding under a running rebuild clock.
- P1: [Atari Games, Rampart 3-Player Game operator's manual, TM-366, first printing](https://crazykong.com/manuals/Rampart.man.pdf).
  See §Game Play, p. 1-3, for the deployment, battle and rebuilding
  order and the required enclosure. §Self-Test identifies the trackball,
  PLACE and ROTATE controls and operator options.
- P2: [Atari Games Rampart advertisement, Play Meter, February 1991](https://elibrary.arcade-museum.com/magazines/pm/PlayMeter-1991-02/PlayMeter-1991-02-148.pdf).
  Contemporary evidence for the three-player cabinet and the solo mode.
- P3: [MAME 0.268 Rampart board driver](https://github.com/mamedev/mame/blob/mame0268/src/mame/atari/rampart.cpp).
  Separately declares trackball inputs for rampart and joystick inputs
  for rampart2p. This identifies the target and input mapping.
- R1: [Museum of the Game, Rampart cabinet record](https://www.arcade-museum.com/Videogame/rampart).
  Distinguishes the dedicated 1990 trackball cabinet from the 1991 kit.
- W1: [Anthro Arcade, trackball-mapped MAME 0.268 capture](https://www.youtube.com/watch?v=n-UL96zKId4&t=46s).
  Corroborates deployment, fire and repair. The recording changes map
  after the first repair segment, around 1:45. Only the later negative
  cycle, through the defeat notice, is used for the failed gate.
- W2: [John Harris, trackball-ROM MAME 0.123 capture with Easy operator setting](https://www.youtube.com/watch?v=K6q68SM1_ak&t=34s).
  Shows castle selection, cannon placement, battle, repair and renewed
  placement on the same board. The upload's title is not release-date
  evidence. The operator setting is the uploader's attribution.
- Claim IDs: RAM-001–RAM-007.

### Reproducible fixture evidence

1. In W2 at 0:39–0:44, locate the lower-left home castle, accept
   the starting enclosure and note where the first placement phase
   begins.
2. At 0:46–0:49 compare the cannon sites before and after the
   placements. Watch 0:51–1:09 for the fire toward offshore ships,
   battle flashes and the change into the rebuild view showing the
   still-present cannon sites and the breached wall.
3. At 1:09–1:24 look for the shape following the cursor, the placed
   sections and the green castle interior. At 1:24–1:27 compare that
   region just before and after its outline closes. The interior
   becomes blue while the clock is still at 08.
4. At 1:34 the fort is enclosed when the clock reaches 00. The
   destruction and castle tallies follow, then a new cannon phase
   starts with the surviving layout at 1:44. The northern castle
   receives separate work in the witness. The published threshold is
   at least one accepted castle.
5. Compare W1's later negative cycle at 2:46–3:06. A perimeter
   remains open and the interior green at 00. The defeat notice
   follows the tallies. This is a separate cycle on a different map.

## Mechanical decomposition

### Action Genes

- ACT-026: move, rotate and place the active supplied wall section
  onto eligible empty cells. The player chooses the location and
  orientation of the current piece.
- ACT-161: aim the available in-game cannon fire toward an eligible
  ship and commit the shot. The cursor addresses the target area
  directly rather than assigning a separate autonomous unit.
- ACT-924: commit an available fixed cannon to a chosen footprint
  inside the current enclosed territory during deployment.

### System Behaviour Genes

- SYS-1988: deployment, battle and repair use the same map. Surviving
  placed cannon sites and breaches carry out of battle into rebuild.
- SYS-1989: a completed wall enclosure around an eligible castle
  marks its interior as held territory. At expiry, accepted enclosure
  permits the next placement phase after settlement.

### Constraint Genes

- CON-001: rebuild uses the fixed cells of the local repair board.
  Committing a new wall section changes occupancy on that board.
- CON-068: the rebuild deadline ends the attempt if its enclosure
  objective has not been met.

### Information Genes

- INF-645: visible wall gaps, interior colour and remaining repair
  time distinguish an unfinished perimeter from a credited one
  while the player can still respond.

### Objective Genes

- OBJ-371: enclose one or more eligible castles by the repair
  deadline and keep at least one accepted enclosure at settlement.

### Time Genes

- TIM-003: placement, battle and repair accept player input as
  their live phases progress; the repair timer keeps falling
  while the next wall shape is being moved.

### Parameters

Chosen starting castle, current territory, cannon allotment and
placement position, surviving walls and occupied cells, current
wall piece and orientation, visible repair clock, and number of
accepted castles at expiry. Exact tile-generation order, corner
connectivity, shore or map-edge treatment, damage coefficients,
clock lengths on other settings and all scoring values are unmeasured.

## Reproducible transitions

| Entry state | Input or event | Expected next state | Evidence |
| --- | --- | --- | --- |
| Home castle with a starting enclosure | Position a supplied cannon inside the walls | Cannon stays at the chosen eligible point during battle | RAM-002 |
| Cannon sites and closed starting walls | Fire toward ships and let the battle interval resolve | Surviving cannon sites and wall gaps remain on the rebuild grid | RAM-003 |
| Visible breach and green castle interior | Move, rotate and place the current wall pieces to close the perimeter | The enclosed castle's interior turns blue during repair | RAM-004–RAM-005 |
| At least one accepted castle | Repair clock reaches 00 | There is a tally and another cannon placement phase on the surviving geometry | RAM-006 |
| No accepted castle in a separate W1 cycle | Repair clock reaches 00 | Defeat follows the tally | RAM-007 |

## Strategic and experiential structure

During deployment, cannon sites use space that will still be occupied
when the surrounding wall needs rebuilding. During repair, extend intact
runs or close an alternative perimeter around the castle. A partial
wall can look substantial but still leave the region green. When time
is short the survival condition is satisfied by one accepted castle.

## Replay and variation

The captures use different coastlines, existing wall runs and timing
contexts. They illustrate how the player can fit pieces around what
remains. They do not establish whether the shape order is random,
which complete borders are smallest, or how much repair time other
operator settings provide.

## Adjacent systems and history

The manufacturer describes later ships landing and rubble interfering
with repair. Neither changes the eligibility of a placed shape within
the witnessed first W2 cycle. Multiplayer can target opposing forts,
and the separate joystick kit changes the input target for comparison.

## Normalised genome

- Action: ACT-026, ACT-161, ACT-924.
- System Behaviour: SYS-1988, SYS-1989.
- Constraint: CON-001, CON-068.
- Information: INF-645.
- Objective: OBJ-371.
- Time: TIM-003.

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `707` (`GAME-0001`–`GAME-0707`).
- Exact genome matches: none.
- Tied near matches: `GAME-0670` — Phantom Dust (`3 / 21 = 0.142857`).
- Supported combination subsets: none.
- Scan date: 2026-11-24.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
| --- | --- | --- | --- |
| [Phantom Dust (GAME-0670)](phantom-dust.md) | ACT-161, CON-068, TIM-003 | Both allow directed shots under a deadline. Phantom Dust's scoped Watchful Eye requires defeating the Ommato with capsule skills before time expires. In Rampart, battle leaves the board to repair, and the timer checks an enclosed castle. | Near, `0.142857`. |

## Taxonomy impact

Reuse the existing boundaries for supplied-shape placement, aimed
fire, fixed occupancy, live input and deadline failure. Isolate fixed
weapon siting in held land, persistence between the three phases,
accreditation of the geometric enclosure, its visible feedback and
the castle-based deadline objective.

## Negative results

- A partly repaired perimeter can expire without credit.
- Destruction and castle tallies appear even in the negative witness.
  Their appearance by itself does not establish survival.
- The footage does not settle edge leakage, exact damage or the shape
  algorithm. The W1 cut disqualifies that specific map transition as
  continuous evidence for carrying the same geometry into a new phase.

## Delta summary

One finite wall grid carries damage into a timed placement puzzle.
Its credited enclosure is both a survival condition and the available
terrain for the next placement phase.

## New facts

- A closed wall changes the visible interior before the rebuild timer ends.
- Barrage damage persists into the repair grid along with surviving cannons.
- W2 shows renewed deployment on the same enclosed land after settlement.

## Principles and design implications

Make the geometric criterion legible while decisions are still live.
Let spatial choices in preparation and destruction constrain the
next repair phase, and show how those repairs change subsequent
placement rights.

## Puzzle or game generation potential

A finite grid can start with a breached shelter and occupied fixtures.
Provide one active shape at a time, require one protected landmark
at expiry, and colour any accepted interior before time runs out.
Give the next planning phase the actual repaired layout.

## New genes

- ACT-924
- SYS-1988
- SYS-1989
- INF-645
- OBJ-371

## New combinations

None. The complete scan supports no verified subset.

## Taxonomy changes

[Taxonomy Change 454](../../../research/taxonomy-changes/TAXONOMY_CHANGE_454.md).

## New questions

- Which later rubble patterns make sealing a different castle preferable?
- Which map edges, if any, participate in a valid perimeter?

## Next recommended game

Continue Selection 061 with Baby Steps on the English commercial
PlayStation 5 release. Trace the opening controlled foot placements
from a witnessed balance or recovery state to a stable arrival.

## Why this game

A single sequence makes the dependence between shooting, spatial
repair and renewed deployment visible without relying on genre
or assumptions about an entire arcade run.
