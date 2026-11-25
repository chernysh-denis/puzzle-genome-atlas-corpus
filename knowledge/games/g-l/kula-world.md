---
game_id: GAME-0706
slug: kula-world
game_title: "Kula World"
analysis_status: reviewed
reviewed: 2026-11-24
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-923
  system:
    - SYS-037
    - SYS-085
    - SYS-1985
  constraint:
    - CON-068
  information:
    - INF-643
  objective:
    - OBJ-164
  time:
    - TIM-003
---

# Game: Kula World

This record uses the [canonical vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
Roll from one support face to another, collect the one required key
and return to the ground-facing exit before the clock expires.

## Analysis scope

- Version / ruleset: original 1998 European PAL PlayStation
  commercial disc SCES-01000, English, solo Arcade, Level 3.
  Game Design Sweden and Sony Computer Entertainment. The
  live witness identifies an optical-drive emulator on original
  hardware. The disc pressing and its hash were not checked directly.
- Structured analysis target: PLAT-PLAYSTATION in
  [platform coverage](../../platforms/games.json).
- Entry: the ball is controllable on a lower cube face of Level 3
  with one unfilled key indicator and a red exit marker.
- Primary decision loop: turn on the current face, advance along the
  new heading, and roll into the connected wall junction to make the
  wall the new support. Traverse the raised path to the required key.
  Return to the lower frame and roll onto the now-open exit.
- Positive terminal: the completion panel credits the level score.
  Acknowledging it opens the next numbered level with the new total.
- Included: local turn and forward movement, the wall-to-floor
  frame change, contact pickup and key eligibility, the graphical
  hourglass, red and green exit states, exit contact and settlement.
- Excluded: optional coin and fruit routes or exact score optimisation,
  optional jumps, hazards not used on the scoped route, camera
  preferences, the exact penalty after failure, bonus and hidden stages,
  multiplayer, demos and other regional versions.
- Potential scoped module: a timed route requiring a forward gap jump
  between disconnected block faces, with a witnessed failed landing.
- Direct-play status: no personal PlayStation run, physical disc
  inspection, or command and clock instrumentation. Two recordings
  were reviewed as silent frames. Retail serial and Level 3 placement
  also have museum and disc-derived support, separated below.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
| --- | --- | --- | --- | --- | --- |
| KW-001 | Sony Computer Entertainment published the 1998 PlayStation CD-ROM, product SCES-01000. The PAL manifest identifies its Europe disc. | Confirmed | Direct | High | P1, D1 |
| KW-002 | Level 3 places one required key on the inner vertical frame face and the normal exit on the top of a lower block. The PAL manifest has no override for that level record. | Confirmed | Corroborated | High | D1; W1 3:18–3:24; W2 1:29–1:36 |
| KW-003 | In-place left or right turns change the advance heading. An advance into the aligned perpendicular wall rolls the ball onto it and reorients the view and subsequent movement. | Observation | Corroborated | High | P2 §3.1, D2, R1 §3; W1 3:17–3:20; W2 1:29–1:31 |
| KW-004 | The lone key is credited on contact. Its HUD icon changes to gold, and the inactive exit changes from red to green. | Observation | Corroborated | High | D2, R1 §4; W1 3:20–3:24; W2 1:32–1:36 |
| KW-005 | Standing on the red exit does not clear the attempt. On the green exit, the same route can reach the completion panel. | Observation | Corroborated | High | D2; W2 1:28–1:29, 1:40–1:42; W1 3:28–3:30 |
| KW-006 | The running hourglass bounds the route. The parsed level carries 99 seconds, and the PAL rules initialise the clock at 50 ticks per second. Expiry ends the attempt rather than reducing only the clear award. | Confirmed | Corroborated | High | D1–D2, R1 §2; W1 hourglass in the successful Level 3 route |
| KW-007 | A completed exit settles the level score into the earlier total. W1 starts the next stage displaying that new accumulated value. | Observation | Corroborated | High | W1 3:29–3:33; W2 1:41–1:44 |

## Basic data

- Release / origin: 1998 Game Design Sweden and Sony Computer
  Entertainment, original European PlayStation retail CD-ROM.
- Families: FAM-013 and FAM-014. The typed key enables a fixed
  fixture, and the support frame changes which faces the ball
  can approach with its next roll.
- P1: [Centre for Computing History, collection record](https://www.computinghistory.org.uk/det/35999/Kula-World/).
  Records the product code, 1998 PlayStation format, author and publisher.
- P2: [Albarracín, Hernàndez-Sabaté and Gorgorió, spatial thinking through Kula World](https://ddd.uab.cat/record/298869).
  The authors' direct teaching study describes direction and the wall
  becoming the new floor in section 3.1. It does not establish PAL clocks.
- D1: [RetroAtlas disc-derived data and method](https://github.com/RetroAtlas/KulaWorldMap/tree/e05af55dea09506bc2fc05e1b23effe45bcbb5fe).
  Read the base record `/HIRO/HIRO.PAK#2` in `public/map_data.json`
  with the European overlay in `public/releases/eu.json`. The
  overlay contains no replacement for that record. The map output is
  independently extracted documentation and was not treated as a live
  observation or included as an Atlas asset.
- D2: [RetroAtlas account of movement, pickups and clock](https://github.com/RetroAtlas/KulaWorldMap/blob/e05af55dea09506bc2fc05e1b23effe45bcbb5fe/docs/motion.md).
  Links the series mechanics to executable routines and specifies
  the PAL timer convention separately from the American one.
- R1: [Marc Lalonde (Syonyx), observed control and pickup guide](https://www.supercheats.com/playstation/walkthroughs/kulaworld-walkthrough01.txt).
  Written using North American Roll Away. Used as corroboration
  for shared controls and key logic alongside both recordings,
  without adopting version-specific timing or scores from it.
- W1: [srs2236, PAL World 1 on PlayStation hardware](https://www.youtube.com/watch?v=2K9b_cUTFFE&t=195s).
  The author reports PicoStation RC3 on SCPH-1002. The Level 3
  figure becomes controllable after the options sequence.
- W2: [GameGamer, English emulator capture](https://www.youtube.com/watch?v=jBsIFDERgsE&t=86s).
  The European Sony title and Level 3 geometry match the examined
  route. Exact emulator and disc settings are unverified.
- Claim IDs: KW-001–KW-007.

### Reproducible fixture evidence

1. Enter Level 3 and locate the cube frame and the sole unfilled
   key marker. W2 rests on the red exit around 1:28, then rolls
   away at 1:29 while the key remains unfilled.
2. Follow the lower path to the perpendicular column so the ball
   faces the wall and advances normally. W2 at 1:29–1:31 and W1
   at 3:18–3:20 show the formerly upright face rotating into the
   ball's supporting plane.
3. Turn along the raised strip and roll through the key. W2 at
   1:32–1:33 shows the pickup flash and the key icon filling.
   W1 shows the same pickup around 3:21–3:22. The exit is visible
   as green on the lower frame in W1 at 3:23–3:24.
4. Use the connected faces to return and enter the green marked
   exit. W1 around 3:29 and W2 around 1:40 show the transition.
   On the completion panel, read the separately shown prior,
   level and updated totals. Acknowledge it and verify the next
   starting scene in W1 at approximately 3:32.

## Mechanical decomposition

### Action Genes

- ACT-008: advance the persistent ball along connected traversable faces.
- ACT-923: quarter-turn the local advance heading without moving to
  another cell, then choose whether to roll forward.

### System Behaviour Genes

- SYS-037: the ball's contact credits the key without ending the
  attempt. Coin and fruit are separately classified pickups.
- SYS-085: reaching the level's required key count activates the exit.
  Level 3 has a single member of this authored key set. The player
  need not apply a separately addressed key to a lock.
- SYS-1985: entering the joined perpendicular face changes the
  supporting frame and the plane of later rolling.

### Constraint Genes

- CON-068: the attempt ends unsuccessfully if the running allowance
  expires before exit contact. The PAL fixture starts at 99 seconds
  according to the extracted duration and regional clock rule.

### Information Genes

- INF-643: the key slot shows missing or acquired while the exit's
  marker changes separately from red to green. The graphical
  hourglass shows the current timed attempt.

### Objective Genes

- OBJ-164: take the eligible exit, settle current points and reach
  the next numbered level with the banked total.

### Time Genes

- TIM-003: while ordinary input remains available, time advances
  during the route and during decision pauses within live play.

### Parameters

The authored block lattice, support normal, local heading, one
required key, fixed exit face, clock, and carried total define this
fixture. The disc-derived record gives 40 cubes. It places the
start on the top of cell (17, 18, 17), the key on the +y face of
(18, 12, 14), and the normal exit on the top of (20, 18, 17).
These coordinates are read from the attributed extraction rather
than estimated from the recordings.

## Reproducible transitions

| Entry state | Input or event | Expected next state | Evidence |
| --- | --- | --- | --- |
| Ball on an ordinary lower face | Turn once left or right | Heading changes and the ball stays on that support | KW-003 |
| Ball at the currently red exit without the key | Contact the exit face | Live movement remains available and the level continues | KW-005 |
| Ball facing the contiguous wall from the base | Advance along the heading | Ball takes the perpendicular support and later forward motion follows that plane | KW-003 |
| Key icon unfilled | Touch the required key | Key icon fills and normal exit switches to green | KW-002, KW-004 |
| Ball returns to the green exit before expiry | Enter the face and acknowledge completion | Level result settles and the next level starts with the updated total | KW-005–KW-007 |

## Strategic and experiential structure

The exit can be physically reached before the loop is solved. The
question is how to reach the required key and return. At a
perpendicular join the player has to anticipate the new support
and the orientation of the next forward input. The running
clock makes spent observation and turns matter without making
the coins or fruit mandatory.

## Replay and variation

The two witnesses visit the lower frame in different orders.
One explicitly crosses the ineligible exit before going up.
The fixed required key, face changes and active exit agree.
The exact score depends on the acquired pickups and prior play.

## Adjacent systems and history

The regional release record identifies different rules for the
hourglass and later fixtures. The earlier Level 2 demonstrates
jumping between platforms. Neither justifies treating this third
level as a gap-jump or extending the study to a regional remake.

## Normalised genome

- Action: ACT-008, ACT-923.
- System Behaviour: SYS-037, SYS-085, SYS-1985.
- Constraint: CON-068.
- Information: INF-643.
- Objective: OBJ-164.
- Time: TIM-003.

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `705` (`GAME-0001`–`GAME-0705`).
- Exact genome matches: none.
- Tied near matches: `GAME-0605` — Outtrigger (`4 / 14 = 0.285714`).
- Supported combination subsets: none.
- Scan date: 2026-11-24.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
| --- | --- | --- | --- |
| [Outtrigger (GAME-0605)](../m-r/outtrigger.md) | ACT-008, CON-068, SYS-037, TIM-003 | Both directly navigate to pickups during a clock that can end the attempt. Outtrigger's last medal settles its mission on contact. The Kula World key enables another destination, reached after changing support and returning to the fixed exit. | Near, `0.285714`. |

## Taxonomy impact

Reuse contact collection, final required-set exit activation and the
scoped route objective. Admit a position-preserving pivot for later
forward motion, a face transition caused by supported advancement
and an independent key and exit status cue.

## Negative results

- The locked exit marker can be reached and crossed while live
  control continues.
- An optional coin or fruit does not fill the required key slot.
- Rolling onto the wall at the observed join does not require an
  airborne jump, an aimed gravity power or a moved block.

## Delta summary

This unit distinguishes the ball's heading, the current support
face and the key-dependent eligibility of a physically reachable
exit on the same static cube structure.

## New facts

- The first scoped key stands on a different supporting plane
  from the exit and starting face.
- Eligibility changes at the required key, while success occurs
  later at the exit.
- The new score survives the accepted transition into the next
  numbered level.

## Principles and design implications

Changing the supporting surface can expand reusable routes on a
fixed structure. A reachable locked exit can show the objective
early. Separate the indicator for the required object from the
marker that changes after acquisition.

## Puzzle or game generation potential

Build a small connected pair of orthogonal cube frames. Start the
agent near a locked exit on one plane. Put one necessary key on a
second plane reached by physical contact. Verify that the support
changes on approach, the key and finish are distinct steps, and a
reverse route to the now-eligible exit exists.

## New genes

- ACT-923
- INF-643
- SYS-1985

## New combinations

None. None of the 274 verified combinations is a proper subset.

## Taxonomy changes

[Taxonomy Change 452](../../../research/taxonomy-changes/TAXONOMY_CHANGE_452.md).

## New questions

- Which later convex edges allow an adhered wrap rather than
  blocking an ordinary advance?
- Which gap-jump positions terminate an attempt in the same
  European ruleset, and which establish a safe new support?

## Next recommended game

Continue Selection 061 with The Gunk on Xbox Series X or Series S.
Follow opening targeted suction through vegetation regrowth and a
newly traversable route.

## Why this game

The third level isolates a change of support frame within an
otherwise small and reproducible keyed exit loop.
