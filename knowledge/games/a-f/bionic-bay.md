---
game_id: GAME-0594
slug: bionic-bay
game_title: "Bionic Bay"
analysis_status: reviewed
reviewed: 2026-11-21
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-190
    - ACT-759
    - ACT-790
  system:
    - SYS-036
    - SYS-061
    - SYS-369
    - SYS-1751
    - SYS-1752
    - SYS-1753
    - SYS-1754
  constraint:
    - CON-113
  information:
    - INF-179
  objective:
    - OBJ-026
  time:
    - TIM-003
---

# Game: Bionic Bay

Use the [canonical vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
Mark a body, move to where it should go, and trade positions so the
same tool can clear a lane, carry weight and carry the scientist.

## Analysis scope

- Version / ruleset: English commercial April 2025 PlayStation 5 digital
  base game, product EP7579-PPSA23767_00-BBAY000000000PS5. Ordinary solo
  chapter play, normal world progression and no speedrun skips. The
  dated PlayStation 5 and PS5 Pro captures corroborate the released
  layout. Their exact installed update numbers are unverified.
- Structured analysis target: PLAT-PLAYSTATION-5. See
  [platform coverage](../../platforms/games.json).
- Entry: first control in chapter 2, Swap, directly after Inception.
  Walk to the new instrument sequence before the first teaching crate.
  No later learned tool is required or assumed.
- Primary decision loop: read the obstacle, reach and mark one suitable
  body, decide which position the body should take and which position the
  scientist should reach, then invoke the exchange. Follow the resulting
  weight, collision and support states in real time. Repeat through the
  pressure platform, moving prop and beam, charged obstructions, flame
  rooms, gap and two overhead structures.
- Positive exit: pass the last overhead structure and cross the right
  boundary that opens the next chapter, Beam. Stop at its first entry,
  before any Beam-only puzzles.
- Negative exit: unlinked commands do not give an arbitrary destination.
  A missed leap, live hazard or collapse can end a local attempt and
  trigger a return to a checkpoint. Moving beyond a valid connection
  can break it without ending the attempt.
- Included: ordinary movement, leap, dash and ledge pull-up, acquisition
  and link loss, reciprocal exchange, body motion, weighted support,
  occlusion, explosive obstacles, lethal contacts and checkpoints.
- Excluded: Inception, Beam puzzles after arrival, ChronoLag, Power Fist,
  Gravity Manipulation, later forms, online and score competition, trophy
  requirements, PC key mapping or demo rules, exact internal physics,
  exact patch parity and all memory-level recovery details.
- Potential scoped module: how the same exchange combines with
  beam-manipulation and later independently granted tools.
- Direct-play status: no executable or native inputs used. The developer
  and official product establish release and the tool. Visual stills
  from two released PS5 routes document the complete sequence. The
  supplemental release-window trace only corroborates layout together with these
  console observations. No video or audio playback.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
| --- | --- | --- | --- | --- | --- |
| BB-001 | The 17 April 2025 commercial PS5 game includes solo progression. The bounded chapter is the route labelled Swap, starting after Inception, before the chapter labelled Beam. | Confirmed | Direct | High | P1–P3; W1 13:30–24:50; W2 19:20–32:00; W3 11:04–20:42 |
| BB-002 | The scientist gains the tool in the first room. A close designation precedes a distinct Swap input. The demo crate becomes useful as a foothold because the exchange relocates both bodies rather than only the scientist. | Observation | Corroborated | High | P2–P3; W1 13:40–14:30; W2 19:30–20:30; R1, R2 |
| BB-003 | Eligible touched props can be marked and left physically independent. The connection can persist as the object moves; sufficiently moving away can disconnect it. The scientist remains the controlled actor after the swap. A written PS5 review reports L1 for Swap and remapping. | Observation | Corroborated | High | P2; W1 14:30–17:20; R1–R3 |
| BB-004 | Exchanging with blockers in a tight pipe and with bodies in a stack changes the accessible clearance. A crate can replace the scientist on the weighted platform to hold the linked route state. Vacating a supporting position can let an overhead body descend. | Observation | Corroborated | High | W1 14:30–16:10; W2 20:20–22:10; R1, R2 |
| BB-005 | The route includes moving ledges, a continually changing beam and a box moving on a carrier. At the latter room, mark it when near and exchange when it reaches the other side. The link follows the box's current position. | Observation | Corroborated | High | W1 16:50–18:20; W2 23:00–24:40; W3 13:20–14:40; R1 |
| BB-006 | A prop swapped into the beam line can obstruct it and create a route. This is separate from riding the beam-room carrier or from a timed gap in the beam. A straightforward attempted crossing in the console trace ends at a flash and a return to the beam's near side. | Observation | Corroborated | High | W1 16:20–17:50; W3 13:10–14:20; R1, R2 |
| BB-007 | A shifted stone can trigger charges below it and clear a blocked downward path. Subsequent climbing uses moved props as steps, and the route includes gears, a contact-triggered blast above and one across a gap. A prop may continue moving from contact or after an exchange. | Observation | Corroborated | High | W1 18:20–21:10; W2 24:40–27:50; W3 14:50–17:30; R1 |
| BB-008 | The flame rooms use two distinct responses. A crate can obstruct an active jet, while the moved object or charge at other emitters can destroy an obstruction. The route also shows hanging at a floating flame device and repositioning a broken pipe before the gap. | Observation | Corroborated | High | W1 21:20–23:00; W2 27:50–30:05; W3 17:50–19:50; R1 |
| BB-009 | The wide gap is crossed using reachable moving bodies and exchanges. In the last two structures, exchanging into position under unsupported mass can be fatal. Timely placement of support and a second exchange provide a passage. The rightward exit transitions into Beam. | Observation | Corroborated | High | W1 23:00–25:00; W2 30:00–32:00; W3 19:50–20:50; R1, R2 |
| BB-010 | Fatal contact gives a local failed state and checkpoint respawn. The source does not establish a counted life stock, exact link range, carried linear or angular velocity rule, or the exact reset state of every prop. | Observation | Corroborated | High | P1; W1 16:20–16:45 / 23:20–23:45; R2 |

## Basic data

- Psychoflow Studio and Mureena, published by Kepler Interactive.
  FAM-010 applies to shifting beams, transport and unsafe delayed exchanges.
  FAM-017 applies to choosing and using dependent route states.
- P1: [PlayStation Store base product](https://store.playstation.com/en-us/product/EP7579-PPSA23767_00-BBAY000000000PS5).
  Establishes PS5, commercial date, publisher, solo access,
  checkpoint support and controls remapping.
- P2: [Juhana Myllys on the developed PS5 rules](https://blog.playstation.com/2025/04/15/the-making-of-hand-crafted-pixel-art-platformer-bionic-bay-out-april-17-on-ps5/).
  Differentiates the foundational exchange from later time,
  gravity and force tools. The later tool rules are outside this packet.
- P3: [Official Bionic Bay site](https://www.bionicbaygame.com/).
  Describes the physical exchange, dangers and independent online mode.

### Reproducible route evidence

- W1: [RetroAnime's released PS5 Pro opening route](https://www.youtube.com/watch?v=SJxHjli4QXo&t=810s),
  22 July 2025. Stills from 13:30 to 25:00 include first control,
  the tagged crate, failed beam passage and the transition into Beam.
- W2: [ScHlAuChi's PS5 route via World of Longplays](https://www.youtube.com/watch?v=DdrxvKgA80o&t=1160s).
  Released PS5 product link and silent frames near 19:20–32:00 support
  the same physical route, including the final overhead hazards.
- W3: [NeatPick's release-window gameplay trace](https://www.youtube.com/watch?v=SaATdraDZmY&t=664s).
  Advance key disclosed; written markers name Swap and Beam.
  The 11:04–20:42 section corroborates route order and geometry,
  without establishing platform or patch parity.
- R1: [Neoseeker's first-hand chapter route](https://www.neoseeker.com/bionic-bay/Level_2).
  Describes crate contact, pressure substitution, timed beam blocking,
  explosions, flames and explicit failing placement at the last structures.
  Button labels there do not establish the PS5 mapping.
- R2: [PlayStation Universe's launch-window PS5 review](https://www.psu.com/reviews/bionic-bay-ps5-review/).
  Written from a supplied release code. Describes marking before the
  second input, crush risk, remapping and checkpoint return.
- R3: [Digital Trends' release-window first-hand review](https://www.digitaltrends.com/gaming/dont-miss-out-on-2025s-most-ingenious-platformer/).
  Corroborates choosing the object and then changing location later,
  with movement and localized physics consequences.

## Mechanical decomposition

### Action Genes

- ACT-008 advances the scientist using ordinary lateral movement,
  jumping and directional dash. ACT-759 uses reached edges for
  pull-up at the ledge above staged props (BB-002, BB-007).
- ACT-790 designates a reachable physical object. ACT-190 activates
  the separate equipped tool while that link can still be used
  (BB-002, BB-003).

### System Behaviour Genes

- SYS-1751 links a movable body's identity to a delayed action.
  SYS-1752 replaces two positions and returns both bodies to physical
  resolution (BB-002–BB-005).
- SYS-036 applies live support, motion and contact, including bodies
  that fall when support moves. SYS-061 holds the linked platform
  state through the crate's occupancy (BB-004, BB-007, BB-009).
- SYS-1753 makes an eligible solid body occlude continuous danger.
  SYS-1754 resolves a contact-induced blast that opens a different
  continuation by removing an obstruction (BB-006–BB-008).
- SYS-369 restores the local checkpoint after lethal harm
  (BB-006, BB-010).

### Constraint Genes

- CON-113 treats contact with an active visible hazard as terminal for
  the local attempt (BB-006, BB-009, BB-010).

### Information Genes

- INF-179 exposes the current bodies, usable edges, luminous beam and
  nearby machine and route states (BB-002–BB-009).

### Objective Genes

- OBJ-026 requires reaching the far chapter boundary after making the
  obstacles traversable. A successful isolated swap is intermediate
  (BB-004–BB-009).

### Time Genes

- TIM-003 applies to moving props, beam motion, gears, blasts and
  collapsing structures as the configured inputs remain available
  (BB-005–BB-009).

## Reproducible transitions

| Initial state | Intervention | Discriminating result | Evidence |
| --- | --- | --- | --- |
| First chapter-2 room before the new tool | Advance right through the pickup sequence and reach the first crate | The contact and exchange operations become usable | BB-001, BB-002 |
| A ledge is too high without a foothold | Mark a crate, stand where the step is needed, swap and use the positioned crate | Each body changes place. The relocated crate is a new foothold | BB-002 |
| Tight passage and several adjacent or stacked objects | Tag and exchange with successive bodies, avoiding a falling stack | The route shifts as the former blocker now occupies the earlier position | BB-003, BB-004 |
| A linked mechanism needs sustained weight | Tag the free object, return to the load platform and swap | The object now maintains the occupied state independently of the scientist | BB-004 |
| Crossing begins with a lethal beam and a nearby marked prop | Place the prop in the beam line by swapping from the needed location | The prop selectively interrupts the beam while it is correctly aligned | BB-006 |
| A carrier brings the movable box into reach | Tag near, wait, exchange across the hazard at the box's actual far position | Delay changes Swap's destination. Moving too far from the link can invalidate later exchange | BB-003, BB-005 |
| Charges or flames block the lower route | Trigger the charges with a displaced body, or leave the box between the jet and the intended path | A blast removes compatible obstruction. Interposing the box can instead preserve a route without destroying the emitter | BB-007, BB-008 |
| Far gap and descending upper structures obstruct the exit | Use sequential exchange on exposed bodies to span the gap and keep a prop under descending mass long enough to escape | The scientist passes the right threshold and enters Beam. An unsafe exchange under unsupported mass can end the attempt | BB-009, BB-010 |

## Strategic and experiential structure

Swap changes both the route of the actor and the next position of an
object. A box can act as a step, a loaded support or a shield depending
on where the scientist stood. The same marked box can change its own
destination while on a carrier. That makes timing and replacement
positions as important as reaching the box.

## Replay and variation

The trace includes safe reapproaches after a fatal laser. A later prop
can be repositioned into the threat rather than avoided by walking
around it. Overhead supports and blast landing geometry constrain these
choices. Optional trophy triggers are corroboration for disconnection,
not an extra objective.

## Adjacent systems and history

The developer documents later abilities and online ghost competition.
This scope includes ordinary solo traversal and stops before Beam's
mechanical additions. The PS5 and Steam releases are distinct targets.

## Normalised genome

| Type | Stable genes | Role |
| --- | --- | --- |
| Action | ACT-008, ACT-190, ACT-759, ACT-790 | Live movement, tool invocation, ledge traversal and designation |
| System Behaviour | SYS-036, SYS-061, SYS-369, SYS-1751, SYS-1752, SYS-1753, SYS-1754 | Physics, retained occupancy, retry, prop link, exchange, occlusion and contact blast |
| Constraint | CON-113 | Lethal active hazard contact |
| Information | INF-179 | Current obstacles, hazards and support |
| Objective | OBJ-026 | Cross the chapter boundary |
| Time | TIM-003 | Waiting and action while hazards and objects move |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `593` (`GAME-0001`–`GAME-0593`).
- Exact genome matches: none.
- Tied near matches: `GAME-0558` — Moss (`6 / 27 = 0.222222`).
- Supported combination subsets: none.
- Scan date: 2026-11-21.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
| --- | --- | --- | --- |
| GAME-0558 Moss | ACT-008, ACT-759, OBJ-026, SYS-036, SYS-369, TIM-003 | Both use direct movement, reached ledges, live physical context and retry. Moss separates Quill’s locomotion from the Reader’s independently moved traversal stone in its Clearing route. Swap uses the player’s previous position to place a tagged physical body and takes that body’s current position in return. | 6 shared of 27; Jaccard 0.222222 |

### Preserved research notes

- Classification result: New gene.

## Taxonomy impact

- [TAXONOMY_CHANGE_340](../../../research/taxonomy-changes/TAXONOMY_CHANGE_340.md)
  records the predecessor boundaries and five additions.

## Negative results

- An eligible contact does not by itself exchange positions.
- A usable mark does not freeze a target or promise the current
  destination will be safe. The descending mass remains dangerous.
- An occluded beam is not a permanently disabled emitter. Destruction
  and occlusion produce mechanically different access.
- No gravity reversal, time dilation, exact link radius or swapped
  velocities are imported from later abilities or desktop controls.

## Delta summary

## New facts

- [Observation | Corroborated | High] A swap places the solid prop
  where the player stood, giving the same operation a routing,
  obstruction and transport role.

## New genes

- [Observation | Corroborated | High] Five additions in
  TAXONOMY_CHANGE_340 alongside reused physics, timing and hazards.

## New combinations

- [Observation | Corroborated | High] No new combination proposed.
  The verified-set subset scan is recorded above.

## Taxonomy changes

- [Observation | Corroborated | High] Existing definitions and
  signatures are retained.

## New questions

- A controlled console attempt could measure how an eligible fast
  prop transfers or retains linear and angular motion on Swap and
  how the mark changes on reaching different checkpoint transitions.

## Next recommended game

- [Hypothesis | Limited | Medium] Complete the Selection 048 parity
  closeout and select the next mixed-era group against the reviewed
  corpus. Begin its first game from an admitted full release.
- Optimisation criterion: preserve platform and mechanism diversity
  alongside visible primary route evidence.

## Why this game

- [Hypothesis | Limited | Medium] The same concrete physical prop can
  become a destination, an occluder or a support under one reciprocal
  action, with distinct failure conditions.
