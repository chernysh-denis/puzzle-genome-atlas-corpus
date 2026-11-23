---
game_id: GAME-0621
slug: sonic-racing-crossworlds
game_title: "Sonic Racing: CrossWorlds"
analysis_status: reviewed
reviewed: 2026-11-21
combination_ids: []
gene_ids:
  action:
    - ACT-131
    - ACT-290
    - ACT-468
    - ACT-827
    - ACT-828
  system:
    - SYS-891
    - SYS-892
    - SYS-1301
    - SYS-1302
    - SYS-1820
    - SYS-1821
    - SYS-1822
    - SYS-1823
  constraint:
    - CON-438
    - CON-861
  information:
    - INF-205
    - INF-344
    - INF-579
  objective:
    - OBJ-333
  time:
    - TIM-003
---

# Game: Sonic Racing: CrossWorlds

This analysis uses the [canonical vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
Character, course, point amounts and speed class are instances of the rules.

## Analysis scope

- Version / ruleset: launch-era English commercial Standard Edition
  on Xbox Series X|S, released September 25, 2025, Microsoft Store
  product 9NJZSFP2ZNVK. The main trace shows a post-launch run on
  Xbox Series X with original base-game content. It does not authenticate
  the recorder's entitlement, installed additions or exact patch number.
- Primary decision loop: drive, drift, gather rings and use held items
  to improve live position. At the boundary of lap one, the leader can
  commit the shared Travel Ring choice. All racers take the selected
  CrossWorld, adapt to its surfaces, return to a modified final lap on
  the start course and earn the points for the classified finish.
- Entry: start grid of E-Stadium, the first individual race in the
  single-player Donpa Grand Prix on High Speed. Metal Sonic, the machine,
  Rival Blaze and the preselected gadget plate are initial conditions
  in the reference Xbox attempt. The mode and speed selector identify
  those conditions without extending the scope to their unlock chains.
- Exit: the end of the third lap and the first race's settled
  standings, including Metal Sonic second for 12 points. The next
  round's ready screen carries those points forward. It is outside
  the analysed driving route, and no cup trophy is required.
- Included: direct vehicle control, optional starting boost, drift release,
  airborne tricks, speed panels, live item activation, ring count and hit
  response, shared branch authority, visual route cue, Dinosaur Jungle water
  form, changed final lap, ordered lap progress and the per-race standings.
- Excluded: subsequent cup routes and the final course medley, later cup
  trophies or Rival unlocks, Red Star Ring completion and ticket spending,
  gadget progression and detailed effects, Frenzy events, online and team
  modes, Time Trial, downloadable content, demo and network tests, other
  platforms and later patches as targets. No exact item probabilities,
  inter-gate timing or numerical speed, damage and recovery formula is claimed.
- Suggested later scope: a complete independent cup closeout, including
  a separate test of its route medley and Rival settlement.

## Direct-play status

No direct play was performed. Microsoft and Sega identify the released Xbox
base product. The retail manual and Sega's launch description establish
the general rules. Jayster's Xbox Series X recording shows the Xbox UI,
the actual High Speed opening race, the shared second-lap destination and
the result. Independent post-release captures confirm the sequence under
other observed rank outcomes. Their precise platforms and installed builds
are unverified. Sampled stills cannot establish the instant or identity
of the route chooser in the Xbox race. Only written material and static
frames were inspected, without playing video or audio.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
| --- | --- | --- | --- | --- | --- |
| SRC-001 | Microsoft product 9NJZSFP2ZNVK and Sega identify September 25, 2025 as commercial Xbox release. The trace shows base Grand Prix content on Series X. | Confirmed | Corroborated | High | P1, P2, W1 0:00–0:20. No rights, exact package or build checksum is claimed. |
| SRC-002 | The sampled local High Speed opener starts at E-Stadium. Metal Sonic uses the chosen machine and the Rival is Blaze. The player directly steers. The start gauge can grant an opening speed burst and a charged drift can grant a distinct burst on release. | Confirmed | Corroborated | High | P3 Racing Mechanics and Controls, W1 0:50–1:40, 2:10–2:50. The recordings do not establish input frames, gadget coefficients or a guaranteed boosted launch. |
| SRC-003 | At the first-lap boundary only the leading racer chooses one of the two offered Travel Rings. The others follow the selected shared route. The visible gate gives route information and can show the destination's scenery. | Confirmed | Corroborated | High | P3 CrossWorlds & Gadgets, P4, W1 at 1:30 for the on-screen rule. W1 3:20 shows the selected gate, while 7:30 illustrates two proposals in a separate round. W3 5:50–6:20 shows a leading entrant on the same E-Stadium transition. None establishes the exact chooser in W1. |
| SRC-004 | The Xbox route goes through the committed gate into the Dinosaur Jungle middle lap within the same race. The driver changes rank while lap progress carries forward. It returns to E-Stadium for lap three. | Observation | Corroborated | High | W1 3:20–4:30, W2 4:50–5:50, W3 6:10–7:20. The other captures corroborate the destination and do not substitute for the Xbox result. |
| SRC-005 | Vehicle movement reacts to the course surface. The car becomes a boat on water and can charge a jump. Air Tricks reward landing, and fixed speed pads or gates provide contact acceleration. The ordinary ring stock improves attainable speed and pickups also grant a temporary burst. | Confirmed | Corroborated | High | P3 Racing Mechanics, W1 2:10, 3:30 and 4:00, W2 5:20–5:40, W3 7:40. These assets do not certify the precise steering input or boost magnitude at any frame. |
| SRC-006 | The third lap returns to the start course with a changed route or fixture set. Spring, item, ring and route opportunities depend on lap state. A final-lap shortcut is not the collective Travel Ring choice. | Confirmed | Corroborated | High | P2 and P3 Other Elements of Racing, W1 4:30–5:10 and W3 7:20–8:10. Particular optional pickups and authored changes need not appear in every route. |
| SRC-007 | The live HUD exposes position, lap, map, ring stock and current items, with local attack cues. An activated racing item has a typed effect and consumes or advances its available uses. Hits can reduce regular rings. A hit at zero can cause loss of control. | Confirmed | Corroborated | High | P3 Racing Mechanics, Items and Controls, W1 2:50–3:10, 3:40–4:10 and 4:50–5:10. The count changes from 100 to 55 in the observed middle-lap sample. Neither an exact loss rule nor a ranked item table follows. |
| SRC-008 | The first E-Stadium race ends at its three-lap finish and classifies the field. The table places Silver first for 15, Metal Sonic second for 12 and Blaze third for 10. The next round's opening table still shows those totals. | Observation | Corroborated | High | W1 5:20–5:30 and 6:10, P3 Grand Prix. W2 6:40 and W3 8:20–8:30 independently show first-place local settlements. The difference confirms that a single race result need not be a cup win. |

## Basic data

- Title: Sonic Racing: CrossWorlds
- Analysis target: `PLAT-XBOX-SERIES`, English commercial Xbox Series X|S Standard Edition.
- Publisher and developer: Sega and Sonic Team.
- Mechanical families: `FAM-010` for racing under live pressure, and
  `FAM-014` for changing shared navigable geometry through the chosen transition.
- Sources checked 21 November 2026.
- P1: [Microsoft Store base product 9NJZSFP2ZNVK](https://www.xbox.com/en-US/games/store/p/9NJZSFP2ZNVK).
- P2: [Sega commercial launch notice and course rule](https://www.sega.co.jp/en/release/250925_1.html).
- P3: [Sega commercial-game online manual](https://manual.sega.jp/sonicracingcrossworlds/en/index.html?pid=9).
  CrossWorlds & Gadgets, Racing Mechanics, Other Elements of Racing and
  Grand Prix supply the ordinary rules. Current additions and other game
  modes are excluded. The launch trace anchors the versioned scope.
- P4: [Sega of America's rule explanation](https://blog.playstation.com/2025/02/12/sonic-racing-crossworlds-gameplay-revealed-new-mechanics-detailed/).
  The named author describes the leader's route applying to the field.
  It is design corroboration rather than Xbox attempt evidence.
- W1: [Jayster, Xbox Series X](https://www.youtube.com/watch?v=8vNp6l0CF-k&t=140s),
  published September 26, 2025. 1:00 shows High Speed, 1:10 Rival Blaze,
  1:20 the locked-in driver, 1:40 E-Stadium and 2:20 the launch. At
  3:00 the player is shown first, at 3:10 second, and at 3:20 second
  approaching the chosen gate. The middle lap appears at 3:30 and the
  stadium has returned by 4:30. The result holds at 5:20–5:30.
- W2: [Menace123, post-launch Donpa Grand Prix](https://www.youtube.com/watch?v=Atc_YpOWolA&t=290s).
  Shadow is sixth on the gate approach, enters Dinosaur Jungle, returns
  and finishes first in this separate race. Its description provides
  the course name and follows the same individual three-lap structure.
- W3: [goodgamez, post-launch E-Stadium round](https://www.youtube.com/watch?v=qGGOoE4FD_U&t=350s).
  The blue kart is first at 5:50–6:20, including when approaching the
  committed route at 6:10 and reaching the alternate lap by 6:20.
  It returns to the stadium at 7:20, then shows FINISH at 8:20
  and the ranked table at 8:30. Those static samples are not an
  input trace of the exact lane selection.

## Mechanical decomposition

### Action Genes

- ACT-131: activate the held race item while it is available.
- ACT-290: steer and regulate the current vehicle.
- ACT-468: hold a drift through a bend, then release at a chosen charge.
- ACT-827: as the current leader at the decision boundary, take one of the
  offered gates to choose the common route.
- ACT-828: perform accepted directional airborne tricks for a landing boost.

### System Behaviour Genes

- SYS-891: an activated held item resolves the corresponding vehicle or
  opponent effect with declared uses.
- SYS-892: the local drift charge resolves into a release boost.
- SYS-1301: crossing an applicable speed panel grants an immediate burst.
- SYS-1302: meeting the pre-start throttle gauge condition grants
  the bounded launch boost.
- SYS-1820: the selected gate sends the field into the same alternate
  lap without resetting progress.
- SYS-1821: the race returns to the starting course with its final-lap edits.
- SYS-1822: ordinary rings support local speed, pickup bursts and hit response.
- SYS-1823: water entry changes the same vehicle into a boat with a charge jump.

### Constraint Genes

- CON-438: ordered lap completion and crossing the finish qualify the result.
- CON-861: only the current leader chooses the shared branch at its boundary.

### Information Genes

- INF-205: live rank, lap, nearby racers and course map expose current progress.
- INF-344: item, ordinary ring and attack cues are distinct from course rank.
- INF-579: the offered and selected gates show road-visible route cues.

### Objective Genes

- OBJ-333: complete this individual Grand Prix round, classify the finish
  and credit that position's points while the Cup is still unfinished.

### Time Genes

- TIM-003: rivals, lap progression and opportunities continue while the driver
  chooses and executes controls.

## Reproducible transitions

| State | Input or trigger | Result | Evidence |
| --- | --- | --- | --- |
| First E-Stadium grid | Start, optionally time throttle within the launch gauge | Live race progresses from lap one | SRC-002 |
| While turning on the track | Steer and hold then release drift, or use an available item | Vehicle takes its directed path with the appropriate temporary effect | SRC-002, SRC-007 |
| Rank reaches the ordinary gate decision | The leading racer takes one offered gate | That CrossWorld becomes the field's shared next lap | SRC-003, SRC-004 |
| A follower approaches the committed gate | Cross that gate | The same race proceeds to 2/3 with changing rank and local geometry | SRC-003, SRC-004 |
| Water on the alternate route | Enter water and optionally charge then release | The same player uses boat form with its own jump/landing response | SRC-005 |
| Alternate lap ends | Cross the return transition | E-Stadium runs its changed third lap | SRC-006 |
| Valid final finish | Complete the declared lap order and cross the line | The table reports Metal Sonic second with 12 points, preserved at the next ready stage | SRC-008 |

## Strategic and experiential structure

An early lead grants control over the field's next environment, while
the final place still depends on the full race. Later rank changes can
reverse who benefits from the route. Drift release, course contact,
rings and held items contribute different forms of acceleration.
Red Star Ring collection is an optional reward track outside the
observed placement objective.

## Replay and variation

The route-choice opportunities and selected worlds depend on the
ordinary race state. The known Xbox attempt and two independent traces
all take Dinosaur Jungle, but finish with different places. Only the
eligible leader at the decision has authority. This analysis does not
identify the exact in-frame triggering deadline, AI selection rule,
distribution of second worlds or subsequent patch behavior.

## Adjacent systems and history

The first round of a four-race Grand Prix contributes points without
completing the cup. The later medley has different course transitions,
and patches add other item and routing options. Those changes do not
supply evidence for the September Xbox trace. The physical shortcut
rings and temporary Warp Ring item are mechanically distinct from the
shared course transition.

## Normalised genome

| Type | Stable genes | Role |
| --- | --- | --- |
| Action | ACT-131, ACT-290, ACT-468, ACT-827, ACT-828 | Item, driving, drift, gate choice and airborne trick |
| System Behaviour | SYS-891, SYS-892, SYS-1301, SYS-1302, SYS-1820–SYS-1823 | Resolve momentum, the shared detour, return, rings and water form |
| Constraint | CON-438, CON-861 | Valid lap order and the single authorised chooser |
| Information | INF-205, INF-344, INF-579 | Live progress, local stock and route cues |
| Objective | OBJ-333 | Classify and credit one race in an unfinished cup |
| Time | TIM-003 | Accept decisions while the race advances |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `620` (`GAME-0001`–`GAME-0620`).
- Exact genome matches: none.
- Tied near matches: `GAME-0309` — Mario Kart 8 Deluxe (`8 / 34 = 0.235294`).
- Supported combination subsets: none.
- Scan date: 2026-11-21.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
| --- | --- | --- | --- |
| [Mario Kart 8 Deluxe (GAME-0309)](../m-r/mario-kart-8-deluxe.md) | ACT-290, ACT-468, CON-438, INF-205, INF-344, SYS-891, SYS-892, TIM-003 | Both use steering, held items and drift-release acceleration. Mario Kart 8 Deluxe runs a fixed course order across four races. CrossWorlds lets the leader choose a shared replacement lap inside the first race; the resulting finish independently sets points within the unfinished cup. | Near, `0.235294` |

## Taxonomy impact

[TAXONOMY_CHANGE_367](../../../research/taxonomy-changes/TAXONOMY_CHANGE_367.md)
records the alternate route, temporary vehicle rules and bounded result.

## Negative results

- SYS-1565 alters associated local geometry by direct contact. It does not
  represent choosing a single shared replacement lap for the entire field.
- SYS-890's weighted ordered two-slot supply is not established for this
  release and setup. The scoped HUD and typed held effects are supported
  independently without importing the exact acquisition table.
- SYS-893 represents the distinct speed effect of collected course coins.
  It does not represent the observed rule's pickup burst and zero-stock hit.
- OBJ-226 requires first place and OBJ-257 describes a standalone race.
  SYS-895 includes settlement through a cup trophy. None can substitute
  for second place and retained points in the first unfinished cup round.
- No native frame timing, item-generation matrix, individual controller
  trace or same-frame chooser from the Xbox footage was verified.

## Delta summary

Admits one complete Xbox base-game round from live start to the field's
chosen cross-world route and settled standings.

## New facts

- The first-lap leader can determine the whole field's shared second lap.
- The starting course's return changes affordances on the final lap.
- Second place visibly settles the reference race and carries its points.

## New genes

ACT-827, ACT-828, CON-861, INF-579, OBJ-333 and SYS-1820–SYS-1823.

## New combinations

None. No verified combination is a subset of the bounded race genome.

## Taxonomy changes

[TAXONOMY_CHANGE_367](../../../research/taxonomy-changes/TAXONOMY_CHANGE_367.md).

## New questions

How do a final medley and the Rival's cup-level settlement interact with
leader-controlled branching? They warrant their own bounded packet.

## Next recommended game

Select the next commercial nine-game horizon after closeout of Selection 051.

## Why this game

The selected route adds a changing race topology and contrasts group
route authority with the one driver's independent final placement.
