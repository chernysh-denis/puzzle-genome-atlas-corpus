---
game_id: GAME-0609
slug: kuru-kuru-kururin
game_title: "Kuru Kuru Kururin"
analysis_status: reviewed
reviewed: 2026-11-21
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-809
  system:
    - SYS-037
    - SYS-1788
    - SYS-1789
    - SYS-1790
    - SYS-1791
  constraint:
    - CON-773
    - CON-852
  information:
    - INF-251
  objective:
    - OBJ-026
  time:
    - TIM-003
---

# Game: Kuru Kuru Kururin

This scope follows the
[canonical vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
Named zones, heart counts and penalty seconds are parameters of the
scoped commercial course.

## Analysis scope

- Version / ruleset: original English European Game Boy Advance Game
  Pak `AGB-AKRP-EUR`, commercially released 22 June 2001. Ordinary
  Normal Adventure, standard rotor span, Grasslands 3. English
  European recordings and the exact mapped European course support
  the scope. The two recordings do not identify a physical cartridge
  or binary hash.
- Primary decision loop: choose the centre’s direction and translation
  speed, anticipate clearance of the continuously turning rotor
  and cross a bend when its angle allows. Pass the recovery zone,
  manage any costly contacts and enter the goal with vitality left.
- Entry: ordinary stage launch from the blue Start Area of Grasslands
  3, with full hearts and standard rotor span after its two preceding
  stages have been cleared. The training route and earlier stages are context.
- Exit: yellow Goal Area, the Cleared Stage result and its local time
  and miss evaluation. Stop as Ocean becomes selectable and before
  operating the craft in Ocean 1.
- Included: normal translation and its held speed tiers, automatic rotor
  turning, curved and narrow corridor clearance, heart loss and time
  penalty, the pink Heart Zone, the sibling contact branch along the
  lower route, and the goal with separate clean-clear eligibility.
- Excluded: shortened-span routes except as a boundary condition, Easy
  timings, Challenge, Practice, link play, springs and later obstacles,
  optional paint or parts, full-campaign rescue totals, record
  optimisation, tool-assisted movement, exploits, native hardware
  testing and verified save/reload behaviour.
- Suggested later scope: one complete Ocean route in which a verified
  blue spring changes rotation before the next controlled crossing.

## Direct-play status

No direct play was performed. Nintendo’s European manual establishes
the control, collision, recovery and clear rules. Two English EU
captures show the course and exit. An extracted European stage map
confirms geometry, zone order and the sibling location. A firsthand
Normal route and documented EU binary observations corroborate timing
and collision; tool-assisted routes are excluded. Neither sampled
Grasslands 3 result establishes a damaged-to-healed replay. Native
input and hardware timing were not measured. No video or audio
playback was used.

## Claim ledger

| ID | Claim | Claim status | Evidence quality | Confidence | Evidence |
| --- | --- | --- | --- | --- | --- |
| KK-001 | The English European commercial Game Boy Advance edition is the target, with product AGB-AKRP-EUR and original release on 22 June 2001. | Confirmed | Corroborated | High | P1, P2, C1, W1. The 2014 eShop and subsequent distribution entries do not identify the original cartridge build. |
| KK-002 | The Control Pad translates the centre. The two-ended collision-bearing span continues to turn during movement and while waiting. | Observation | Corroborated | High | P1 pp. 6, 8, 14; H1, R1 and W1 4:20–4:30. The player steers translation, not the rotor angle. |
| KK-003 | A held A or B modifier speeds translation; holding both yields the fastest normal tier. Direction and angular state remain independently relevant. | Observation | Corroborated | High | P1 pp. 6–8 documents A and B. R1, H1 and W2's metadata describe tiers. No timing or multiplier was measured on hardware. |
| KK-004 | Grasslands 3 is a winding continuous course, with the blue start and yellow goal near each other but separated by walls. Narrow stretches and bends make rotor angle, centre path and crossing time jointly matter. | Observation | Corroborated | High | M1, H1, W1 4:20–4:30, W2 4:30–4:50. No spring appears in M1. |
| KK-005 | On Normal, three hearts are available. A harmful wall contact removes a heart, adds three seconds and counts as a miss; a depleted heart meter ends the attempt. | Confirmed | Corroborated | High | P1 p. 8, R1, C2, W1 live meter and result. The exact recovery interval after a hit is outside scope. |
| KK-006 | The Heart Zone lies mid-course. Passage through this protected zone replenishes depleted hearts while leaving the continuing attempt intact. The lower return route also has a contact-collected sibling independent of entering the yellow goal. | Observation | Corroborated | High | M1, W1 4:20 and W2 4:40 vicinity, P1 p. 9, R1. The exact collection frame and a damaged approach are not established by the ordinary stills. |
| KK-007 | Reaching the yellow zone settles one course. W1 shows Cleared Stage, 24.01 seconds, zero misses and the run at the top of the local table. W2 shows the goal and then the Ocean selection. | Observation | Direct | High | P1 pp. 9, 14; W1 4:40–4:50; W2 5:00–5:10. The sample time is not a pass threshold. |
| KK-008 | A regular clear is distinct from a clean star. The latter requires zero harmful contacts and the eligible standard rotor span. Healing does not erase a miss. | Observation | Corroborated | High | P1 pp. 10, 14, H2 and R1. Exact semantics of a later overwritten ranking or power cycle were not tested. |

## Basic data

- Release / origin: Eighting developed the original game and Nintendo
  published it. This record concerns the European 2001 cartridge.
- Platform: `PLAT-GAME-BOY-ADVANCE`, English European commercial Game Pak.
- Puzzle families: physics and object manipulation (FAM-007) for a
  dynamically changing occupied span, and real-time system pressure
  (FAM-010) for waiting or advancing while the angle keeps changing.
- P1: [Nintendo's European game instruction booklet](https://www.nintendo.com/eu/media/downloads/games_8/emanuals/game_boy_advance_8/Manual_GameBoyAdvance_KuruKuruKururin_EN_DE_FR_ES_IT.pdf),
  printed English pages 6–15. The English control, loss, refuge,
  completion and star rules precede the other language sections.
- P2: [Nintendo UK game catalogue](https://www.nintendo.com/en-gb/Games/Game-Boy-Advance/Kuru-Kuru-Kururin-946956.html).
  Nintendo and Eighting credits and the original hardware family. Its
  listed December 2014 date belongs to the Wii U Virtual Console release.
- C1: [European GBA product entry](https://gamefaqs.gamespot.com/gba/445177-kuru-kuru-kururin/data)
  and [Nintendo's hardware timeline](https://www.nintendo.com/en-gb/Hardware/Nintendo-History/Nintendo-History-625945.html).
  The game product entry and regional hardware launch date agree.
- C2: [Nintendo World Report firsthand GBA preview](https://www.nintendoworldreport.com/hands-on-preview/2544/kuru-kuru-kururin-game-boy-advance).
  Confirms that one contact can debit both a heart and time. Regional
  build details are not used to identify the target.
- H1: [Mark Turner's Normal Adventure route](https://gamefaqs.gamespot.com/gba/445177-kuru-kuru-kururin/faqs/39406),
  Section 4, Grasslands 3. Describes slowing before the recovery zone
  and waiting for a better angle before the last big bend. Its speedrun times are not thresholds in this scope.
- H2: [Titney’s firsthand control and zone account](https://gamefaqs.gamespot.com/gba/445177-kuru-kuru-kururin/faqs/11130).
  Corroborates loss, healing and the standard-span clean mark; earlier
  region wording does not replace the European release sources.
- M1: [dahrion’s European Grasslands 3 map](https://vgmaps.com/Atlas/GBA/KuruKuruKururin(E)-Grasslands-3.png),
  consulted for stage geometry and locations. The image is not included
  in this corpus or used as page artwork.
- R1: [mohoc’s reported European build observations](https://tasvideos.org/9235S).
  Reference for distinct translation tiers, the protection zone and
  contact rules. The reported tooling and strategies are outside scope.
- W1: [KAGE-008 via LongplayArchive, European game](https://www.youtube.com/watch?v=wGsYLs0Zzgg&t=250s),
  4:10–4:50. The stills show the course title, narrow route and
  24.01-second clean result. At 4:20 the rendered tips are roughly 60
  GBA screen pixels apart when scaled to a 240-pixel-wide view. This
  matches R1’s full-length sprite and distinguishes it from the short
  propeller shown as an Easy option in the earlier menus.
- W2: [RieLoveChan Gaming, European Adventure](https://www.youtube.com/watch?v=aKHdwAEzPfM&t=260s),
  4:20–5:10. Separate capture showing the level preview, passage by
  the recovery zone, arrival and next world.

### Reproducible route evidence

1. Select Grasslands 3 in Normal Adventure, keep the standard rotor and
   start in blue with three hearts. M1 shows the adjacent yellow goal
   is on the end of a different corridor; proximity gives no shortcut.
2. Control the centre along the rising corridor and its bends.
   At a wide part, wait for the rotor to line up with the next passage;
   use an appropriate translation tier to cross before the tip meets
   the wall. W1 at 4:20 samples a largely lengthwise rotor in a
   narrowing. H1 separately recommends changing departure phase.
3. Continue through the upper curved passage toward the pink square.
   W2 at 4:40 shows the approach with live time and full hearts.
   If a prior wall hit has reduced the meter, enter this zone to
   recover. The +3-second penalty and miss remain part of that attempt.
   With no hearts the attempt ends instead, as specified by P1.
4. Follow the right-side bend and return through the lower corridor.
   M1 shows the sibling at the lower-right curl. Contact can collect
   it, while stage completion is settled by the goal. W1 at 4:30 and
   W2 at 4:50 sample different angles on the route after the refuge.
5. Enter the yellow Goal Area. W2 5:00 shows arrival; W1 4:40 shows
   Cleared Stage, zero misses and a 24.01-second time in the local
   table. W1 4:50 and W2 5:10 show the Ocean world selection.
   End before the next course.

Claim IDs: KK-001–KK-008. The external playback addresses are not the
in-game attempt times.

## Mechanical decomposition

### Action Genes

- ACT-008: steer the centre through a planar course.
- ACT-809: hold one or both modifiers to alter translation as needed.
- Claim IDs: KK-002–KK-004.

### System Behaviour Genes

- SYS-037: contact acquires the sibling separately from stage exit.
- SYS-1788: the rotor changes angle over time even without translation.
- SYS-1789: harmful collision debits a heart and adds fixed time and a miss.
- SYS-1790: the Heart Zone restores vitality without resetting that attempt.
- SYS-1791: stage clear and standard-span clean marking settle separately.
- Claim IDs: KK-002, KK-004–KK-008.

### Constraint Genes

- CON-773: the ordinary attempt stays live only with positive hearts.
- CON-852: safe progress requires clearance for the full changing span.
- Claim IDs: KK-004–KK-006.

### Information Genes

- INF-251: the result exposes the completed time and local table. The
  displayed miss count helps distinguish a clean submission from
  its visible pace or available health.
- Claim IDs: KK-007, KK-008.

### Objective Genes

- OBJ-026: reach the designated yellow goal through the traversable
  corridor. Orientation is the local traversability condition.
- Claim IDs: KK-004, KK-007.

### Time Genes

- TIM-003: during live play the rotor advances regardless of the next
  translation input. A brief wait changes the crossing angle and time.
- Claim IDs: KK-002–KK-004.

## Reproducible transitions

| Before | Action | Resolution | What it establishes | Claim ID |
| --- | --- | --- | --- | --- |
| Blue start, standard span | Supply direction at a suitable phase | The centre enters the first corridor while the rotor turns | Direction and angular state are separate | KK-002, KK-003 |
| Rotor is too transverse for a narrowing | Wait in a region with enough clearance and steer as the phase aligns | The same gap now admits the full span | Waiting changes the angle even without centre movement | KK-004 |
| Rotor touches an outside wall harmfully | Continue only if a heart remains | Lose one heart, add three seconds and record a miss | Time and vitality are both costs | KK-005 |
| A damaged attempt reaches the pink restoration square | Enter the square | Health recovers while the same attempt continues | Recovery does not restore a clean run | KK-006, KK-008 |
| Surviving craft reaches the sibling on the lower route | Make the collecting contact | Sibling acquisition is separate from reaching the goal | An optional pickup has its own transition | KK-006 |
| Surviving craft reaches the yellow zone | Fly into it | Stage clears and shows time and misses | The course’s terminal is physical arrival | KK-007 |
| Clear with standard span and no misses | Read stage and course record | Clean mark is eligible separately from time rank | A slower clean clear is still eligible | KK-007, KK-008 |

## Strategic and experiential structure

A faster translation tier may get the long rotor through before the angle
becomes unsafe. The same tier can overshoot good centre alignment at a
bend. Waiting in a roomy section trades time for clearance. If harm
occurs, the Heart Zone offers survival recovery but a miss and time
penalty stay recorded. Finishing the course and earning a clean star
are separable goals. Claim IDs: KK-002–KK-008.

## Replay and variation

Both English recordings show finished routes with different pacing.
W1 supplies the exact zero-miss result and time. The manual and
independent route analysis supply the collision, recovery and clean
eligibility branches. These branches are not presented as additional
ordinary replays. Claim IDs: KK-005–KK-008.

## Adjacent systems and history

Ocean introduces springs that may reverse rotation, and later courses
have other obstacles. No spring, material customisation, Challenge
rule, link-play handicap or later reissue is modeled here.
Claim IDs: KK-001, KK-004, KK-008.

## Normalised genome

| Type | Stable genes | Role |
| --- | --- | --- |
| Action | ACT-008, ACT-809 | Steer the centre and hold a speed tier |
| System Behaviour | SYS-037, SYS-1788, SYS-1789, SYS-1790, SYS-1791 | Sibling contact, rotating span, collision costs, restoration and separate clean credit |
| Constraint | CON-773, CON-852 | Positive health and full span clearance |
| Information | INF-251 | Completed local time and place |
| Objective | OBJ-026 | Reach the designated spatial terminal |
| Time | TIM-003 | Execute while the angle advances in real time |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `608` (`GAME-0001`–`GAME-0608`).
- Exact genome matches: none.
- Tied near matches: `GAME-0394` — LittleBigPlanet 2 (`4 / 21 = 0.190476`).
- Supported combination subsets: none.
- Scan date: 2026-11-21.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
| --- | --- | --- | --- |
| [LittleBigPlanet 2 (GAME-0394)](littlebigplanet-2.md) | ACT-008, OBJ-026, SYS-037, TIM-003 | Both combine direct movement and separate pickups en route to a terminal. LittleBigPlanet 2 uses platforming and interaction with traversal fixtures. Grasslands 3 uses continuous rotor alignment and costs time and a heart for harmful contact. | Near, `0.190476` |

### Preserved research notes

- Classification result: New gene.

## Taxonomy impact

- [TAXONOMY_CHANGE_355](../../../research/taxonomy-changes/TAXONOMY_CHANGE_355.md)
  defines the new boundaries and discusses existing comparators.

## Negative results

- ACT-058 commands an orientation and its attached sweep. Here the
  player translates the centre without commanding that changing angle.
- CON-090 models a discrete multi-cell held-object sweep. This course
  continuously changes the collidable span even when movement stops.
- OBJ-251 couples a self-moving slalom to penalties for missed gates.
  This rotor is manually translated and harm is a separate physical cost.
- CON-153 counts irreversible command strikes against termination.
  Here it is recoverable vitality that can end the attempt, while the
  separate miss count affects the clean mark.
- SYS-1750 changes avatar position after a hazard. The Heart Zone can
  restore health on the live route without a teleport or retry.
- SYS-628 describes a timed finish record, without a distinct clean
  qualification tied to body span.

## Delta summary

## New facts

- [Observation | Corroborated | High] The target clearance changes with
  rotor angle while player translation can stop or change speed. KK-002–KK-004.
- [Observation | Corroborated | High] A bad contact has both resource and
  timing costs. Recovery restores the resource, not the evaluation. KK-005, KK-006.
- [Observation | Direct | High] A 24.01-second clear with no misses is
  shown on the ordinary result. Its next world and clean eligibility
  have different predicates. KK-007, KK-008.

## New genes

- [Observation | Corroborated | Medium] ACT-809, SYS-1788, SYS-1789,
  SYS-1790, SYS-1791 and CON-852.

## New combinations

- [Observation | Direct | High] No new combinations.

## Taxonomy changes

- [Observation | Corroborated | High] TAXONOMY_CHANGE_355.

## New questions

- How quickly does a damaged craft recover from a contact at the edge
  of the Heart Zone on a verified physical cartridge?
- How are score ties or a slower clean run retained alongside a previous
  faster, damaged result?
- How much ordinary timing latitude does the hardest bend allow at each
  movement tier?

## Next recommended game

- [Hypothesis | Limited | Medium] `GAME-0610`, BALL x PIT, full paid iOS
  release. Follow one base-game descent through ricochets, build choice
  and the confirmed settlement or boss result.

## Why this game

- [Hypothesis | Limited | Medium] The body’s automatic geometry turns a
  simple movement command into a timed clearance decision.
