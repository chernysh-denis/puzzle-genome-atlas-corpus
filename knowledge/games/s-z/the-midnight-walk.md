---
game_id: GAME-0531
slug: the-midnight-walk
game_title: The Midnight Walk
analysis_status: reviewed
reviewed: 2026-11-17
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-341
    - ACT-433
    - ACT-726
    - ACT-727
  system:
    - SYS-057
    - SYS-1375
    - SYS-1528
    - SYS-1529
    - SYS-1530
    - SYS-1531
    - SYS-1532
    - SYS-1533
  constraint:
    - CON-076
    - CON-379
  information:
    - INF-115
    - INF-179
    - INF-516
  objective:
    - OBJ-026
  time:
    - TIM-003
---

# Game: The Midnight Walk

Use the [canonical vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
The fuel count, lighting target shapes and number of linked candles
parameterise the rules.

## Analysis scope

- Version / ruleset: released English PlayStation 5 base game, May 2025
  launch-era rules, standard flat-screen DualSense controls. The retail
  content identity is grounded in the platform listing. The exact
  installed patch was not observed.
- Structured analysis target: PLAT-PLAYSTATION-5, standard non-VR play.
  Native PS VR2 gaze and eyelid sensing, other platforms and later modes
  are outside the packet.
- Primary decision loop: find an eligible fixture, choose between a
  briefly carried match and Potboy's directed flame, then evaluate the
  change to the route. Close the eyes at blue-eye markers and use
  cover and patrol position to time the next crossing.
- Entry: first chapter, The Tale of the Burnt One, on reaching the
  unlit Potboy with the eyes and eye-close command already acquired.
  Use the nearby supplied match. Exit: pass the first hostile deliberately
  drawn to a candle after the cave's linked lights, reaching the right-hand
  route beyond its wardrobe. Stop before the stone bridge collapses.
- Included: local movement, matches, two coal offers at the barrel, the
  companion dispelling the dark barrier, command targeting, the small pipe
  and bridge, the paired plates, blue-eye barriers, linked candles,
  wardrobe hiding and one deliberate flame distraction.
- Excluded: sensory-body-part acquisition and earlier key search, optional
  recordings and collectibles, exact match life and damage timings, checkpoint
  persistence, exact plate release logic, Housy and the bridge-collapse
  recovery, matchlock, later chapters and replay modes.
- Direct-play status: no PS5, PS VR2, executable, recording or audio was
  run. The platform listing and developer materials establish the release
  and key interactions. Independent written first-chapter routes and static
  captures corroborate their order. Exact native frame and patch behaviour
  remain unverified.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
| --- | --- | --- | --- | --- | --- |
| MW-001 | The PS5 release supports flat-screen play. A lit match wakes the dormant Potboy. He flees into a container before offering help. | Confirmed | Corroborated | High | P1, P2, P3, S1 |
| MW-002 | Take nearby coal and feed Potboy at the container twice. He joins after that exchange. The earlier dark barrier clears when the lit companion approaches. | Observation | Corroborated | High | P2, S1, S2, S3 |
| MW-003 | Command Potboy at an eligible target. At the first pipe he carries out the route beyond the player's passage, knocking the bridge down so the player can cross. | Observation | Corroborated | High | P2, S1, S2, S3, S4 |
| MW-004 | The joint gate checks two separated floor controls. Send Potboy to occupy one and stand on the other to open it. Exact persistence after a body leaves a plate was not checked. | Observation | Corroborated | High | S1, S2, S3 |
| MW-005 | In flat-screen play holding the eye-close control suspends ordinary sight and brings up relevant sound cues. In supported cases DualSense vibration signals proximity. Looking toward a blue eye and closing the eyes alters a marked obstruction so the route is visible when they reopen. | Observation | Corroborated | High | P2, S1, S2, S3 |
| MW-006 | A placed blue-eye obstacle beyond the paired plates hides a dangerous passage. Open it with the eye-close action and use a wardrobe while the threat passes. At later linked-light stations, deliberately light the required marked candles, including a fixture Potboy must reach through a pipe. | Observation | Corroborated | High | S1, S2, S3 |
| MW-007 | At the first candle distraction after the cave, use Potboy to light the separate candle and take the wardrobe. A hostile changes course toward the flame to extinguish it. Leave after it passes and take the right-hand route. | Observation | Corroborated | High | P2, S1, S2, S4 |
| MW-008 | A matchbox provides a match, and ignition makes a short-lived carried flame. This opening match can wake Potboy. The later partner command lights candles at a distance only through his actual journey to the target. | Observation | Corroborated | High | P2, P3, S1, S2, S5 |

## Basic data

- Release / origin: MoonHood, published by Fast Travel Games, original
  PlayStation 5 release on 8 May 2025.
- Families: inventory and fixture dependencies, agent routing, and
  ordered dependency sequencing.
- Sources accessed 2026-11-17:
  - **P1** — [PlayStation Store PS5 release listing](https://store.playstation.com/en-us/concept/10009390),
    product identity, platform and May 2025 release. The scope uses
    this edition's standard DualSense control rather than VR.
  - **P2** — [PlayStation launch-period account made with MoonHood](https://blog.playstation.com/?p=404390).
    The flat-screen eye-close input and its audio and proximity feedback,
    match awakening, coal trust, helper traversal, flame-driven terrain
    change, hostile interest in flames, and hiding are described there.
    An example from a separate obstacle is not treated as proof of the
    exact opening layout.
  - **P3** — [MoonHood's original PlayStation announcement](https://blog.playstation.com/?p=396255)
    identifies the dormant lantern companion and ignition mechanic.
  - **S1** — [Vladyslav Shamshurov's May 2025 first-chapter route](https://vgtimes.com/guides/125959-the-midnight-walk-walkthrough-complete-guide-and-tips.html),
    from the unlit companion through the coal barrel, bridge, plates,
    eye-marked barriers and first exposure to the candle decoy.
  - **S2** — [Greg Wheeler's May 2025 first-chapter route](https://www.thereviewgeek.com/themidnightwalk-chapter1-walkthrough/),
    indexed sections for the dark wall, first bridge, targeted companion
    command, eye markers and the right-hand crossing after the bait.
  - **S3** — [Neoseeker's written first-chapter route](https://www.neoseeker.com/the-midnight-walk/Chapter_1%3A_The_Tale_of_the_Burnt_One),
    indexed sections for two coal offerings, the pipe, paired buttons,
    wardrobe and the marked candles in successive rooms.
  - **S4** — [Gamer Social Club's launch-day route observations](https://gamersocialclub.ca/2025/05/08/the-midnight-walk-chapter-one-collectibles-guide/),
    visual landmarks for coal pickup, bridge, wardrobe and first candle
    lure. Item collection itself is outside the packet.
  - **S5** — [Axia's written release-era play account](https://axia-asd.co.uk/the-midnight-walk-game-review/),
    finite match burn, lighting supplies and access to remote fixtures
    through Potboy. No specific burn duration is taken from it.
- Claim IDs: MW-001–MW-008.

## Mechanical decomposition

### Action Genes

- Reuse `ACT-008`: direct the Burnt One to reachable positions and
  cross an opened route when available.
- Reuse `ACT-341`: address the matchbox, a legal ignition target, the
  barrel and offered coal using their contextual interactions.
- Reuse `ACT-433`: enter and leave an authored wardrobe concealment state.
  The timed choice is whether to leave once the enemy has moved.
- New `ACT-726`: address an eligible fixture for Potboy to move to
  and operate, without taking control of his body.
- New `ACT-727`: voluntarily hold the eye-close command to suppress
  ordinary vision, including at the marked blue-eye route controls.
- Claim IDs: MW-001–MW-008.

### System Behaviour Genes

- Reuse `SYS-057`: a perceiving threat can route toward an eligible
  actor or an intentionally lit decoy. It continues moving while the
  player waits in concealment.
- Reuse `SYS-1375`: lighting a disposable match begins a finite local
  burn while carried. Replacing an exhausted match requires another
  supply activation.
- New `SYS-1528`: initial ignition wakes the dormant lantern actor.
  The actor withdraws before accepting compatible fuel offerings.
  Reaching the scripted offer threshold makes his ongoing help available.
- New `SYS-1529`: an eligible flame changes each marked local fixture
  to its lit state. The linked passage clears once the prescribed set
  is lit, including fixtures reached using Potboy.
- New `SYS-1530`: a target marked by a blue eye changes its obstruction
  state upon the correctly addressed eye-close action. That route is
  traversable after reopening the eyes. The command does not give a
  universal disarm or safe time stop.
- New `SYS-1531`: a designated enemy treats the separately lit fixture as
  a decoy and approaches it to remove its flame. This creates a window
  while the hostile is away from the player's intended route.
- New `SYS-1532`: the commanded companion takes an exclusive small
  passage and performs the remote physical action that connects the
  player's route, such as lowering the first bridge.
- New `SYS-1533`: the active flame of the following companion dispels a
  designated dark obstruction as he approaches, making the route passable.
- Claim IDs: MW-001–MW-008.

### Constraint Genes

- Reuse `CON-076`: the Burnt One crosses the large path, while Potboy
  accesses the narrow pipe and places his flame at the fixtures beyond.
  They retain different permitted routes and interactions.
- Reuse `CON-379`: the paired gate requires two distinct body inputs.
  The direct player body occupies one trigger and the addressed
  companion occupies the other. The single-occupant reset rule after
  opening is outside the established boundary.
- Claim IDs: MW-003, MW-004, MW-006.

### Information Genes

- Reuse `INF-115` and `INF-179`: the local view and current sounds
  expose visible candles, eye markers, concealment places and enemy
  positions only as they become available to this first-person view.
- New `INF-516`: eye closure removes the ordinary visual channel and
  emphasises relevant local sound with supported proximity cues through
  the controller. The rule is about current perceptual feedback, separate
  from the authored state change at a blue eye.
- Claim IDs: MW-005–MW-008.

### Objective Genes

- Reuse `OBJ-026`: connect and reach the onward path beyond the
  candle-lured hostile, with the companion's help.
- Claim IDs: MW-003, MW-004, MW-006, MW-007.

### Time Genes

- Reuse `TIM-003`: lit matches and moving enemies continue to change
  the decision state. The player decides when to activate, hide,
  wait or leave the wardrobe within the live route.
- Claim IDs: MW-006–MW-008.

## Reproducible transitions

| Before | Action or event | Bounded resolution | What it establishes | Claim ID |
| --- | --- | --- | --- | --- |
| Potboy is dormant, with a lit match available | Apply the lit match to Potboy | Potboy wakes and flees to his container | Ignition alone does not grant control of the companion | MW-001 |
| Potboy remains in the barrel after the first coal offer | Obtain and offer the second piece | Potboy trusts the player and joins. His active flame permits passage at the dark obstruction. | The second offer and the live flame support different transitions | MW-002 |
| The bridge is up and the first pipe is reachable by Potboy | Command him to go through the pipe | Potboy reaches the far side and lowers the bridge; the Burnt One can then cross | A requested helper route connects a separate player route | MW-003 |
| Two floor plates at the first joint gate | Send Potboy to one and stand on the other | The gate opens when both bodies supply their inputs | Two occupied controls differ from sequential button latches | MW-004 |
| One blue-eye obstruction is addressed | Close and then reopen the eyes | The barrier is removed. At the first post-plate barrier, seek a wardrobe while the hostile passes. | Perceptual change and route danger can coexist | MW-005, MW-006 |
| The cave passage still needs its linked candles | Send Potboy through the small pipe and light its remote candle as part of the required set | The remaining marked state can settle and clear the way | Reaching a candle can depend on the other actor's route | MW-003, MW-006 |
| The first outer decoy candle is dark and a wardrobe is nearby | Have Potboy light the candle and hide | The hostile approaches the separate flame to extinguish it. Once it has passed, the right-hand path offers a crossing. | The same flame that enables access can deliberately relocate a threat | MW-007 |

## Strategic and experiential structure

A portable match opens the first dependency by waking Potboy but expires
with time. Once trust is established, his movement and flame become
separate remote tools. The player can attend to the opposite plate or
withdraw to a wardrobe. Blue-eye barriers use a temporary loss of sight
to change traversal. The same action also changes how the player can hear
the current surroundings. A decoy light attracts the hostile instead of
making the area safe for an unlimited interval.

## Replay and variation

- The fixtures, initial companion state and route are authored. Timing
  differences can affect match expiry, when a moving threat is noticed
  and when a player tries to leave the wardrobe.
- Compare the first and second coal handoffs. Compare visual state before
  and after closing the eyes at the marked target. Compare the hostile
  route before and after the separate candle is lit.
- No exhaustive patrol schedule, tool stock count or guaranteed
  death/reload state is asserted.
- Claim IDs: MW-001–MW-008.

## Adjacent systems and history

- Later puzzles introduce other tools, including the matchlock, and
  separate blue-eye and hostile behaviours. They require their own
  boundaries. No VR input equivalence is assumed.
- A candle can satisfy a fixture requirement here or draw a live hostile.
  It does not have the scoped Animal Well candle's future-spawn suppression
  behaviour.
- Claim IDs: MW-005–MW-008.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
| --- | --- | --- |
| Action | `ACT-008`, `ACT-341`, `ACT-433`, `ACT-726`, `ACT-727` | first-person route, contextual input, wardrobe, companion destination and closed eyes |
| System Behaviour | `SYS-057`, `SYS-1375`, `SYS-1528`, `SYS-1529`, `SYS-1530`, `SYS-1531`, `SYS-1532`, `SYS-1533` | decoy route, temporary match, trust, lit station, eye gate, extinguishing, pipe bridge and dark barrier |
| Constraint | `CON-076`, `CON-379` | distinct actor access and joint occupancy |
| Information | `INF-115`, `INF-179`, `INF-516` | local sight and sound, nearby fixtures, enhanced closed-eye feedback |
| Objective | `OBJ-026` | first crossing past the candle decoy |
| Time | `TIM-003` | live patrol, ignition duration and exposure |

Canonical signature:

`ACT-008,ACT-341,ACT-433,ACT-726,ACT-727; SYS-057,SYS-1375,SYS-1528,SYS-1529,SYS-1530,SYS-1531,SYS-1532,SYS-1533; CON-076,CON-379; INF-115,INF-179,INF-516; OBJ-026; TIM-003`

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `530` (`GAME-0001`–`GAME-0530`).
- Exact genome matches: none.
- Tied near matches: `GAME-0352` — DOOM (1993) (`6 / 30 = 0.200000`).
- Supported combination subsets: none.
- Scan date: 2026-11-17.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
| --- | --- | --- | --- |
| `GAME-0352` — DOOM (1993) | `ACT-008`, `ACT-341`, `INF-115`, `OBJ-026`, `SYS-057`, `TIM-003` | Both move toward a local exit while sight, sound and live enemy reactions affect access. The scoped DOOM route uses weapons, local doors and combat to reach the exit. The Midnight Walk recruits a flame companion, changes marked barriers by closing the eyes and crosses behind a hostile drawn to an extinguishable candle. | Tied near (`0.200000`) |

### Preserved research notes

- New genes: `ACT-726`, `ACT-727`, `SYS-1528`–`SYS-1533`, `INF-516`.
- Classification result: `New gene`.
- Evidence and reasoning: ignition is used in separate trust, fixture,
  traversal and hostile-routing effects. Closing the eyes is both an
  information decision and, at marked fixtures, a world-state action.

## Taxonomy impact

- Registry changes: nine Active additions and eleven transfers.
- Taxonomy-change record: [TAXONOMY_CHANGE_278](../../../research/taxonomy-changes/TAXONOMY_CHANGE_278.md).

## Negative results

- No source establishes that weights or sequential contacts can satisfy
  the paired gate. Leave exact release timing unclaimed.
- No observation justifies treating every flame as a general-purpose
  distraction or every eye as an identical application of the local
  blue-eye rule.

## Delta summary

## New facts

- [Observation | Corroborated | High] Awakening the lantern precedes
  trust and targeted commands. A commanded flame can become an
  environmental key or a decoy depending on its receiver.

## New genes

- [Observation | Corroborated | High] Nine definitions in
  `TAXONOMY_CHANGE_278`.

## New combinations

- [Observation | Corroborated | High] No new combination proposed.

## Taxonomy changes

- [Observation | Corroborated | High] `TAXONOMY_CHANGE_278`.

## New questions

- Which legitimate interruptions can reset the two actor inputs, and
  what exact event closes the local decoy window?

## Next recommended game

- [Hypothesis | Limited | Medium] No further title is selected by
  Selection 041. The next selection remains a separate decision.
- Optimisation criterion: retain multi-platform and mixed-era coverage
  while comparing distinct flame, perception and companion mechanisms.
- Backlog impact: Selection 041 reaches its ninth scoped game.

## Why this game

- [Hypothesis | Limited | Medium] Beginning at companion activation and
  ending immediately after a live lure distinguishes four jobs performed
  by light without assuming a universal lighting rule for the full game.
