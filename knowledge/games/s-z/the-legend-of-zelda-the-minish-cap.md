---
game_id: GAME-0593
slug: the-legend-of-zelda-the-minish-cap
game_title: "The Legend of Zelda: The Minish Cap"
analysis_status: reviewed
reviewed: 2026-11-21
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-009
    - ACT-107
    - ACT-161
    - ACT-202
    - ACT-341
  system:
    - SYS-215
    - SYS-578
    - SYS-1363
    - SYS-1748
    - SYS-1749
    - SYS-1750
  constraint:
    - CON-746
    - CON-773
  information:
    - INF-119
    - INF-179
  objective:
    - OBJ-026
  time:
    - TIM-003
---

# Game: The Legend of Zelda: The Minish Cap

Use the [canonical vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
Change size to enter Minish Village, learn to understand its residents and
reach the first chamber of Deepwood Shrine.

## Analysis scope

- Version / ruleset: English North American Game Boy Advance retail
  Game Pak AGB-BZME-USA, released 10 January 2005. Use ordinary
  single-player progression, without cheats, randomization or save states.
  The attributed recordings show the English GBA route. Their exact
  cartridge or emulator build is unverified. The static research target
  distinguishes the original USA build from Japanese, European and demo builds.
- Structured analysis target: PLAT-GAME-BOY-ADVANCE.
  See [platform coverage](../../platforms/games.json).
- Entry: first control inside Minish Woods on the first story visit.
  Bring Smith's Sword from the castle quest and have no Flippers, Ezlo
  or Jabber Nut. Avoid farming or optional prerequisites.
- Primary decision loop: read the routes and nearby hazards, defeat the
  two Octoroks threatening Ezlo, and leave the clearing until he joins
  Link. Use the marked stump with Ezlo, then fit the small route and
  time the moving lily-pad crossing. Follow evidence from the village
  to the nut, move the obstructing crate, eat the nut, learn the
  destination from Gentari and return to Festari to make the north
  path available. Walk through the small forest passages into the shrine.
- Positive exit: first controllable chamber inside Deepwood Shrine
  at Minish size, after Festari has moved aside. Stop before operating
  its first switch or collecting a key.
- Negative exit: the wrong size cannot fit the narrow approach.
  Unsupported water at Minish size without the Flippers causes a
  recoverable drowning. Before the nut and Gentari's briefing, Festari
  does not move aside for that clearance. Zero hearts ends the current
  attempt and invokes the Game Over flow. No exact continued save state
  is assumed.
- Included: first forest route, ordinary sword combat and hearts, Ezlo,
  portal size change, size-dependent surfaces and actions, authored
  moving pads, localized hazard recovery, the village and its pushable
  crate, retained language comprehension, progression dialogue and
  first shrine entry.
- Excluded: preceding castle and field assignments, Pieces of Heart,
  rupee and Kinstone collection, later tools and portals, exact combat
  damage and reset coordinates, all play inside the shrine beyond entry,
  other versions, re-releases and full narrative progression.
- Potential scoped module: complete Deepwood Shrine separately from
  entry to Earth Element, including its barrel, Gust Jar and boss.
- Direct-play status: no executable or native inputs used. The Nintendo
  booklet and release history establish the product and controls.
  Stills from two GBA traces, first-hand route records and a pinned
  reverse-engineered implementation corroborate the transitions.
  No ROM was obtained or run. Video and audio were not played.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
| --- | --- | --- | --- | --- | --- |
| MC-001 | Nintendo's North American English Game Boy Advance retail edition uses AGB-BZME-USA and was released 10 January 2005. The scope starts after the castle briefing and excludes demo and rerelease rules. | Confirmed | Direct | High | P1 front/back and pp. 6–15; P2; P3 |
| MC-002 | Normal-sized Link can attack the two Octoroks with Smith's Sword. After the rescue, move away and advance the following dialogue until Ezlo rides on Link and offers optional advice. Defeating the enemies by itself does not put Link into the small traversal state. | Observation | Corroborated | High | W1 27:10–30:00; W2 21:20–23:40; R1, R2 |
| MC-003 | With Ezlo, climb onto the eligible stump and use the contextual R action to shrink. From beside an eligible portal, the small actor can use R to return to normal. The route demonstrates retained small form away from the stump across multiple screens. | Confirmed | Direct | High | P1 pp. 6–7, 14–15; W1 30:10–31:30; W2 24:40–26:30; D1 |
| MC-004 | At Minish size the same route exposes tiny openings and changes surface hazards. Ordinary shallow water is wadeable at normal size, while unsupported water in small form without Flippers can cause drowning. Item usability is size-dependent. Drowning restores local footing without growing Link to ordinary size. | Observation | Corroborated | High | W1 30:30–31:20; W2 25:30–26:20; D1, D2; R1 |
| MC-005 | The shore-side lily pads move along authored paths. When the small actor is supported, a pad carries him without an item propelling it. Step aboard when it arrives within reach, then off at the other shore. | Observation | Corroborated | High | W1 31:00–31:20; W2 26:10–26:30; D3; R1, R2 |
| MC-006 | At first the village residents' language is unintelligible to Link. Festari can already converse with Link and points him toward the Jabber Nut. This interaction also clears the initial guards for the barrel route when the village updates. | Observation | Corroborated | High | W1 31:30–33:30; W2 26:30–29:20; D4, D5; R1, R2 |
| MC-007 | Enter the barrel house, push aside the crate that occludes the accessible route, and address the nut. Eating it removes the world object and stores comprehension. Subsequent residents can be understood without finding another nut or spending it at a conversation. | Observation | Corroborated | High | W1 33:30–34:10; D4, D5; R1, R2 |
| MC-008 | Eating the nut does not alone grant passage. Gentari's briefing supplies the Element destinations and records the briefing. Festari checks the nut and that state, then moves aside. The forest's small openings lead into the first shrine chamber. | Observation | Corroborated | High | W1 35:50–37:40; W2 31:00–33:20; D4; R1, R2 |
| MC-009 | Ordinary hits deplete hearts, and all hearts lost ends the attempt with a save/continue choice. A water recovery uses recorded nearby valid geometry, independently of that attempt-ending threshold. Exact damage and post-save return coordinates are outside scope. | Observation | Corroborated | High | P1 pp. 20–21; W1 25:20–27:40; D1, D2 |

## Basic data

- Capcom/Flagship development and Nintendo publication. FAM-017 describes
  the dependency from the companion and scale-eligible route through
  understanding, a briefing and passage permission.
- P1: [Nintendo's original North American instruction booklet](https://www.thegameisafootarcade.com/wp-content/uploads/2017/08/The-Legend-of-Zelda-The-Minish-Cap-Game-Manual.pdf),
  preserved scan of AGB-BZME-USA. Pages 6–7, 14–15 and 20–21
  establish buttons, pushing, shrink/grow and the heart-based failure rule.
- P2: [Nintendo's North American series history](https://www.nintendo.com/en-ca/explore/characters/zelda/history/)
  lists the January 2005 GBA release. The series page is a product reference.
- P3: [Nintendo of America's dated shipment statement](https://nintendoworldreport.com/news/10212/noa-ships-first-original-zelda-for-gba),
  archived by Nintendo World Report on 10 January 2005. It establishes
  the original Nintendo retail product and size-changing premise.

### Static implementation evidence

The following is the zeldaret US-target research reconstruction at commit
`6fb6dfb4a7efbe24d0fd1dda5097af6131faacde`. It identifies distinct USA, EU,
JP and demo inputs. Its inspected routines corroborate transitions. A matching
ROM build was neither obtained nor independently reproduced.

- D1: [Portal and water actions](https://github.com/zeldaret/tmc/blob/6fb6dfb4a7efbe24d0fd1dda5097af6131faacde/src/player.c).
  Read the portal activation, shrinking and reverse paths alongside
  shallow-water routing, drown initialization and local recovery.
- D2: [Player helpers](https://github.com/zeldaret/tmc/blob/6fb6dfb4a7efbe24d0fd1dda5097af6131faacde/src/playerUtils.c).
  `CreateItem` filters use by form, and `RespawnPlayer` searches recorded
  nearby positions for a valid tile in the ordinary terrain case.
- D3: [Small lily pad](https://github.com/zeldaret/tmc/blob/6fb6dfb4a7efbe24d0fd1dda5097af6131faacde/src/object/lilypadSmall.c).
  Movement advances separately from the support eligibility check.
- D4: [Festari](https://github.com/zeldaret/tmc/blob/6fb6dfb4a7efbe24d0fd1dda5097af6131faacde/data/scripts/minishWoods/script_Festari.inc)
  checks the nut and briefed flag, distinct from the initial conversation.
  [Gentari](https://github.com/zeldaret/tmc/blob/6fb6dfb4a7efbe24d0fd1dda5097af6131faacde/data/scripts/minishWoods/script_Gentari.inc)
  checks the nut and sets the briefing flag after displaying the map.
- D5: [Nut interaction](https://github.com/zeldaret/tmc/blob/6fb6dfb4a7efbe24d0fd1dda5097af6131faacde/src/object/cutsceneMiscObject.c),
  [forest Minish dialogue](https://github.com/zeldaret/tmc/blob/6fb6dfb4a7efbe24d0fd1dda5097af6131faacde/src/npc/forestMinish.c)
  and [village initialization](https://github.com/zeldaret/tmc/blob/6fb6dfb4a7efbe24d0fd1dda5097af6131faacde/src/roomInit.c)
  distinguish the consumable, stored inventory flag and village actor sets.

### Reproducible route evidence

- W1: [zuzhi64's English GBA walkthrough](https://www.youtube.com/watch?v=SraLGHuZxeg&t=1517s).
  Silent frames at 25:20–37:40 show the first forest entry, rescue,
  stump, water, village, barrel, elder, moved gatekeeper and terminal.
  The optional heart pieces and extra conversations do not belong to
  this scoped route.
- W2: [Longplay Nexus's English GBA longplay](https://www.youtube.com/watch?v=cfvdUU1Q3vM&t=1060s).
  Independent still trace from the Minish Woods segment to Deepwood
  Shrine. The 25:30–26:30 sequence explicitly distinguishes shallow
  water at normal size from the risks of small form.
- R1: [Thonky's reproducible forest and village route](https://www.thonky.com/zelda-minish-cap/minish-woods).
  Documents the exit position, unchecked route alternatives and
  required interactions. The pad travels from shore to shore.
- R2: [Kirby021591's written GBA playthrough](https://gamefaqs.gamespot.com/gba/920670-the-legend-of-zelda-the-minish-cap/faqs/34833),
  Minish Woods and Minish Village. Independently names the abrupt
  size change, the moving leaf, the villagers, the edible capability
  and the permission sequence.

## Mechanical decomposition

### Action Genes

- ACT-008 moves Link through the forest, onto a passing pad, through
  small holes and into the shrine. ACT-009 moves the eligible crate
  in the barrel room (MC-005, MC-007, MC-008).
- ACT-107 completes conversations that register operational route
  facts: the nut lead with Festari and the map briefing with Gentari
  (MC-006, MC-008).
- ACT-161 commits the sword attack used against the Octoroks at normal
  size. ACT-202 selects the alternate body configuration through the
  portal command (MC-002, MC-003).
- ACT-341 addresses the found world object to eat the nut and returns
  to the gatekeeper to commit the now-enabled passage interaction
  (MC-007, MC-008).

### System Behaviour Genes

- SYS-215 resolves real-time combat before Ezlo joins. SYS-578 tracks
  the continuing heart pool and admits compatible local healing
  (MC-002, MC-009).
- SYS-1363 carries the small avatar on an independently moving pad
  while he remains supported (MC-005).
- SYS-1748 changes retained body scale at an enabled fixture and
  alters the allowed actions and surfaces (MC-003, MC-004).
- SYS-1749 stores the comprehension acquired from the unique eaten
  item and enables later conversations without another expenditure
  (MC-006–MC-008).
- SYS-1750 interrupts unsupported water contact and recovers the
  actor at recorded valid local geometry (MC-004, MC-009).

### Constraint Genes

- CON-746 requires the actor's current body form to fit the little
  passages. CON-773 requires positive hearts for ordinary continued
  control (MC-003, MC-004, MC-008, MC-009).

### Information Genes

- INF-119 exposes hearts and currently assigned items. INF-179 exposes
  the visible stump, local paths, enemy approach, moving support and
  nearby residents (MC-002–MC-008).

### Objective Genes

- OBJ-026 settles the reproducible approach by actually entering
  the designated shrine once all required route states permit it
  (MC-008).

### Time Genes

- TIM-003 lets enemies and riding supports advance while the player
  chooses when to attack or step on and off the pad (MC-002, MC-005).

## Reproducible transitions

| Initial state | Intervention | Discriminating result | Evidence |
| --- | --- | --- | --- |
| First Minish Woods visit with only the early sword available | Find the endangered companion, defeat the Octoroks and move away through his interruptions | Ezlo joins and his portal instruction becomes available | MC-002, MC-003 |
| Link is ordinary-sized beside the first enabled stump | Climb onto the stump and choose the contextual R action | Ezlo produces small form, which follows Link into the next screens | MC-003 |
| Link is small on dry ground near an eligible portal | Address the portal with the contextual R action instead of continuing to the village | The rule allows normal size again; small routes still require small form | MC-003, MC-004 |
| Small Link lacks Flippers and a moving pad is out of reach | Wait at the edge, step on the pad when reachable and step off at the second shore | Movement along the pad's path bridges a corridor otherwise blocked by water | MC-004, MC-005 |
| Small Link enters unsupported water | Let the drowning sequence resolve | Local recovery restores a traversable position, separately from zero-heart failure | MC-004, MC-009 |
| Village conversation is not understandable | Ask Festari, enter the barrel, push the crate and eat its nut | Village conversation is understood and the same nut is not needed again | MC-006, MC-007 |
| Nut eaten and briefing absent | Ask Festari without first completing Gentari's briefing | The blocking resident has not moved aside; the stored comprehension alone is insufficient | MC-008 |
| The briefing is recorded | Return to Festari and cross the released corridor and little openings | Reach the first controllable shrine chamber while small | MC-008 |

## Strategic and experiential structure

The player gains reach by giving up the normal body state. The new size
allows passage through small openings and travel on drifting leaves, but
also makes shallow water hazardous. The same small body's entry to the
village still leaves its residents unintelligible. One addressed object
changes the comprehension state. The later briefing and guard
interaction turn that new capability into traversable access.

## Replay and variation

A direct approach can skip optional heart pieces and extra village chats.
On the pond, wait on a bank for valid support rather than assuming line
of sight implies traversability. Regrowing at an enabled portal can undo
the clearance needed for the small approach. The account does not
claim a speed route or universal out-of-bounds handling.

## Adjacent systems and history

The re-release listings do not establish byte parity with the USA retail
Game Pak. The first dungeon later introduces a driven large lily pad.
That transport is separate from the autonomous small pads used here.

## Normalised genome

| Type | Stable genes | Role |
| --- | --- | --- |
| Action | ACT-008, ACT-009, ACT-107, ACT-161, ACT-202, ACT-341 | Current movement, pushing, route dialogue, attack, body change and interaction |
| System Behaviour | SYS-215, SYS-578, SYS-1363, SYS-1748, SYS-1749, SYS-1750 | Combat, hearts, moving support, retained size, comprehension and hazard recovery |
| Constraint | CON-746, CON-773 | Clearance and positive health |
| Information | INF-119, INF-179 | Hearts and local route |
| Objective | OBJ-026 | Shrine entry |
| Time | TIM-003 | Live attack and boarding windows |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `592` (`GAME-0001`–`GAME-0592`).
- Exact genome matches: none.
- Tied near matches: `GAME-0459` — Daxter (`9 / 27 = 0.333333`).
- Supported combination subsets: none.
- Scan date: 2026-11-21.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
| --- | --- | --- | --- |
| GAME-0459 Daxter | ACT-008, ACT-161, ACT-202, ACT-341, INF-119, INF-179, SYS-215, SYS-578, TIM-003 | Both use a compact form to pass tight geometry and live direct combat. Daxter toggles crouching while earning proof gems and reports to the concierge. Link changes scale at a fixture, uses an independently moving pad and gains comprehension before the gatekeeper moves. | 9 shared of 27; Jaccard 0.333333 |

### Preserved research notes

- Classification result: New gene.

## Taxonomy impact

- [TAXONOMY_CHANGE_339](../../../research/taxonomy-changes/TAXONOMY_CHANGE_339.md)
  records the three additions and comparisons with existing boundaries.

## Negative results

- From the wrong side of the scale change, a narrow passage remains
  inaccessible. Meeting Ezlo does not itself change Link's size.
- The small pad and shallow water have different consequences. A supported
  ride is possible; unassisted traversal into water is not its substitute.
- In the inspected route scripts, acquiring comprehension does not
  satisfy the briefing check. Festari provides an early understandable
  line and later permission under different conditions.
- No companion handover becomes a separate controlled actor. No
  universal item ban, exact damage, exact reload state or region-wide
  replay parity is inferred.

## Delta summary

## New facts

- [Observation | Corroborated | High] Physical clearance, comprehension
  and permission are independently required along this route.

## New genes

- [Observation | Corroborated | High] Three additional systems coexist
  with reused clearance, moving support and spatial objectives.

## New combinations

- [Observation | Corroborated | High] No new verified combination
  proposed. See the subset scan above.

## Taxonomy changes

- [Observation | Corroborated | High] Earlier definitions and
  signatures are retained. Only new scoped evidence adds uses.

## New questions

- A controlled cartridge test could sample the exact rejected
  portal contact or sequence around drowning recovery on a moved pad.

## Next recommended game

- [Hypothesis | Limited | Medium] GAME-0594, Bionic Bay on PlayStation 5.
  Reconstruct an authored obstacle where a position swap is indispensable.
- Optimisation criterion: contrast retained avatar size with displacement
  through a selected physical swap.

## Why this game

- [Hypothesis | Limited | Medium] This route keeps a physical state
  change and a conversational progression state distinct while both
  determine access to the same destination.
