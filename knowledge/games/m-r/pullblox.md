---
game_id: GAME-0737
slug: pullblox
game_title: "Pullblox"
analysis_status: reviewed
reviewed: 2026-11-25
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-950
  system:
    - SYS-036
    - SYS-2048
  constraint:
    - CON-906
  information:
    - INF-179
    - INF-665
  objective:
    - OBJ-026
  time:
    - TIM-002
---

# Game: Pullblox — Basic Lessons, Lesson 3

Use the [canonical vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
The three extensible slabs, the depth slots and the child instantiate
the local manipulation, traversal and settlement rules.

## Analysis scope

- Version / ruleset: English European Nintendo 3DS commercial
  eShop release, Pullblox, December 8, 2011. Nintendo Europe
  establishes the original release and its play loop. The detailed
  Lesson 3 witnesses display the North American title Pushmo.
  The English European install and exact version were not tested.
- Reproducible entry and exit: choose Pullblox Park, Basic Lessons,
  Lesson 3. Start with the three horizontal slabs retracted and
  Mallo at the front. Advance the introductory instruction.
  End after the child is rescued and the completion choice appears,
  before starting or replaying a puzzle.
- Primary decision loop: pull the bottom reachable block outward
  repeatedly, jump onto its top, then grip and move the middle
  and upper blocks to shallower depths. Climb the exposed treads
  and reach the marked child.
- Included: move and jump, local block grip and depth changes,
  per-block travel limits, staggered footing, planar goal map
  and the first rescue in this lesson. Excluded: side-pulling
  introduced later, using the reset switch or rewind, exact jump
  physics, elapsed-time measurements, studio, QR content,
  later gadgets, sequels and subsequent lessons.
- Direct-play status: no personal Nintendo 3DS or emulator session.
  Nintendo Europe identifies the retail ruleset and platform;
  its launch-era release is independently described. Nintendo's
  North American manual and two independent original Pushmo
  records identify Lesson 3 rule execution. A 2011 Spanish
  Pullblox recording provides European same-game controls and
  rescue context at Lesson 1 only. All footage was inspected
  silently in the background.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
| --- | --- | --- | --- | --- | --- |
| PB-001 | Nintendo released Intelligent Systems' Pullblox for European Nintendo 3DS on December 8, 2011. Nintendo's listing identifies the rescue-by-extrusion loop and the end of new eShop purchases. | Observation | Direct | High | P1, S1 |
| PB-002 | The lesson shows a vertical stack of three horizontal slabs and a target on the highest one. A gripped slab can be pulled out or pushed in along depth. Its face shape and height stay fixed. The upper screen shows the changed geometry, while the lower map locates Mallo and the goal on the face layout. | Observation | Corroborated | High | P2 controls and rules, W1 04:47–05:24, W2 08:13–09:03, S1 |
| PB-003 | The original lesson names three steps as the outward limit from retraction. The lower slab advances to the third position and the tutorial calls out the limit before ordinary movement resumes. | Observation | Corroborated | High | W1 05:13–05:34, W2 08:54–09:15, S1 |
| PB-004 | Pull the bottom out three positions, then use its top to pull the middle out two, then move to the middle tread and pull the top once. The protrusions expose a sequence of local jumping surfaces. Setting the lower depth does not move either higher slab. | Observation | Corroborated | High | W1 05:18–05:39, W2 08:55–09:22, S2, S3 |
| PB-005 | Mallo must reach the top target rather than merely extend its block. He jumps onto the last block, the child is visibly rescued and the clear screen opens a replay or next-puzzle choice. | Observation | Corroborated | High | P1, P2 rules, W1 05:34–05:47, W2 09:17–09:27 |
| PB-006 | Settled depth positions wait between accepted grip actions rather than advancing on a lesson clock. Jump movement resolves normally once committed. The displayed construction instruction changes after the third lower pull. | Observation | Corroborated | High | W1 05:18–05:39, W2 08:55–09:22, S2 |

## Basic data

- Release / origin: Intelligent Systems and Nintendo, European
  Nintendo 3DS eShop release on December 8, 2011.
  Analysis target `PLAT-NINTENDO-3DS`. The legal link is the
  official archived product page.
- Mechanical families: `FAM-005` for making a climbable route
  from mutable terrain and `FAM-017` for the reach dependencies
  between block adjustments and traversals.
- Primary sources checked 2026-11-25:
  - **P1:** [Nintendo UK's Pullblox listing](https://www.nintendo.com/en-gb/Games/Nintendo-3DS-download-software/Pullblox--298087.html).
    Identifies the European release, the push/pull rescue rules,
    and the closure of new eShop purchases.
  - **P2:** [Nintendo's original Pushmo electronic manual](https://csassets.nintendo.com/noaext/image/private/t_KA_PDF/manual-3DS-pushmo-en?_a=DATAg1AAZAA0).
    The controls and park sections describe gripping, jumping,
    moving blocks in and out, the lower-screen goal map and the
    separate reset switch. It is the North American companion
    document for the same original game.
  - **W1:** [Japancommercials4U2's original Pushmo Basic Lessons recording](https://www.youtube.com/watch?v=m2iXeiJ3c1Y&t=287s).
    The selection names Lesson 3 at 04:47. The bottom pull limit
    is taught around 05:13–05:34. The climb and clear appear at
    05:34–05:44, followed by the completion choice.
  - **W2:** [CostilerAphid18's original Pushmo recording](https://www.youtube.com/watch?v=dDu868zAw8U&t=493s).
    The author marks the Lesson 3 entry at 08:13. The trace shows
    the same lower limit and exposed stair, with the rescue and
    clear visible by 09:24. Spanish captions are commentary.
  - **W3:** [ESPALTeam's December 2011 Pullblox recording](https://www.youtube.com/watch?v=ytyCQA-vUoY&t=64s).
    Shows the European title in Spanish. Lesson 1 confirms the
    basic extension, climb and rescue interaction seen in the
    paired product family. It is not evidence of the Lesson 3
    route or of the captured English European binary.
- Independent descriptions:
  - **S1:** [Nintendo Life's December 2011 European play report](https://www.nintendolife.com/reviews/2011/12/pullblox_3dsware).
    Establishes the regional names and up to three increments.
  - **S2:** [blcklblskt's original 3DS walkthrough](https://gamefaqs.gamespot.com/3ds/644719-pushmo/faqs/63996),
    Basic Lessons, Lesson 3.
  - **S3:** [StrategyWiki's Basic Lessons walkthrough](https://strategywiki.org/wiki/Pushmo/Basic_Lessons),
    Lesson 3, corroborates the three-two-one depth recipe.
- Claim IDs: PB-001–PB-006.

## Mechanical decomposition

### Action Genes

- Reuse `ACT-008`: move Mallo on the ground and jump between the resulting treads (PB-002, PB-004, PB-005).
- New `ACT-950`: grip a reachable slab and shift that same block along its depth axis (PB-002–PB-004).

### System Behaviour Genes

- Reuse `SYS-036`: a jump leaves the current support and settles on the next attainable surface (PB-004–PB-006).
- New `SYS-2048`: expose footing by extending a lower slab farther than the slab above (PB-004, PB-005).

### Constraint Genes

- New `CON-906`: each slab has a finite extension from flush, with three steps demonstrated and named in this lesson (PB-003, PB-004).

### Information Genes

- Reuse `INF-179`: the main field displays Mallo, the position and faces of nearby slabs, the treads and the goal (PB-002, PB-004).
- New `INF-665`: pair the current three-dimensional geometry with a separate static face map and live player and goal markers (PB-002, PB-004, PB-005).

### Objective Genes

- Reuse `OBJ-026`: reach the trapped child on the upper slab after opening a traversable path (PB-004, PB-005).

### Time Genes

- Reuse `TIM-002`: the player chooses when to change each settled depth or begin the next move; there is no automatic depth change between actions (PB-003, PB-006).

## Formal state and transitions

Represent the wall by three fixed-height slabs, each with an
independent depth offset from flush. Adjacent depths determine
which top treads remain exposed. Track Mallo's current support
or airborne position separately. Grip updates a slab; climbing
updates the reachable set of faces. The goal checks arrival on
the marked upper support, then shows a separate completion choice.

## Reproducible transitions

| Before | Action or event | Bounded resolution | Claim ID |
| --- | --- | --- | --- |
| Three slabs are flush and Mallo starts in front | Follow the tutorial and grip the lowest front face | Address the bottom slab without moving the upper two | PB-002, PB-003 |
| Bottom slab addressed at flush | Pull outward three positions | Reach its declared maximum and expose the lower tread | PB-003, PB-004 |
| On the extended lower tread | Grip and pull the middle block twice | Keep the bottom tread exposed and reveal a middle ledge | PB-004 |
| On the middle tread | Pull the upper block once | Expose the last landing without filling the middle tread | PB-004 |
| The marked upper block is extended | Jump up to the child | Rescue, show clear and offer the next or replay choice | PB-005 |

## Strategic and experiential structure

Spend the deepest protrusion on the bottom slab so the higher
slabs can extend without covering the next usable tread. The
depth difference matters at each of the two intermediate tiers.
The target stays at the top while the space available to land
and reach the next face changes locally.

## Replay and variation

Two original Pushmo traces reproduce the successive grip-and-climb
solution. Both use the bottom maximum and then smaller outward
positions on the higher slabs. The scoped route runs without
triggering the reset switch or using history rewind. No claims
are made about optimal execution time or unseen alternative jumps.

## Adjacent systems and history

Nintendo's manual documents a reset switch and rewind input.
Lesson 3 displays these affordances, but only ordinary
displacement and climb are admitted here. Later lessons add
side manipulation and more complex shapes, and the studio adds
editable puzzle creation outside the selected route.

## Normalised genome

- Action: ACT-008, ACT-950.
- System Behaviour: SYS-036, SYS-2048.
- Constraint: CON-906.
- Information: INF-179, INF-665.
- Objective: OBJ-026.
- Time: TIM-002.

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `736` (`GAME-0001`–`GAME-0736`).
- Exact genome matches: none.
- Tied near matches: `GAME-0624` — Paradise Killer (`3 / 13 = 0.230769`).
- Supported combination subsets: none.
- Scan date: 2026-11-25.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
| --- | --- | --- | --- |
| [Paradise Killer (GAME-0624)](paradise-killer.md) | ACT-008, INF-179, TIM-002 | Both leave the player free to inspect the visible scene and initiate the next local action without advancing an attempt clock. Paradise Killer's Courthouse briefing yields dialogue choices, evidence and a dated account for investigation. Pullblox changes three physical depths to make successive landing and grip positions and settles when the player reaches the child. | Near, `0.230769`. |

## Taxonomy impact

A grip action changes a persistent slab's depth, while the
relative geometry determines footing. The cap applies to each
slab's position rather than to the number of actions spent.
The face map tells the player where to go within the shape
without taking over reading the 3D treads.

## Negative results

- Extending the lower block leaves the two higher slabs in place.
- The lesson declares no ordinary fourth outward position.
- Extending the upper block does not alone rescue the child.
- The lower map shows the face layout, not the tread depth itself.

## Delta summary

Record one original three-slab lesson from flush configuration
to staggered climb, child rescue and the replay or next choice.

## New facts

- One block can be moved repeatedly on a bounded depth axis.
- The three-two-one offsets create sequential treads.
- The settled rescue depends on player arrival above them.

## Principles and design implications

Let each exposed surface satisfy access to the next handle.
A separate planar readout can locate the target while leaving
the depth relationship to be read from the represented terrain.

## Puzzle or game generation potential

Make one stack of fixed-height slabs, a common retracted
baseline and a per-slab maximum. Check whether each exposed
tread can reach the next front face and whether the final
jump, rather than the last block move, settles the goal.

## New genes

- ACT-950
- CON-906
- INF-665
- SYS-2048

## New combinations

None. No verified combination is a proper subset of the signature.

## Taxonomy changes

[Taxonomy Change 483](../../../research/taxonomy-changes/TAXONOMY_CHANGE_483.md).

## Next recommended game

Dandara: Trials of Fear Edition on Android is the last Selection
064 unit.

## Why this game

The same blocks serve as both edited objects and the traversed
route. A single depth choice can reveal or cover the surface needed
for the next grip.

## Review status

Reviewed 2026-11-25 for the original European Nintendo 3DS release
target, with the Lesson 3 witness boundary described above.
