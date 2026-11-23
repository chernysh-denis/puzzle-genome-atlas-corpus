---
game_id: GAME-0615
slug: skate-story
game_title: "Skate Story"
analysis_status: reviewed
reviewed: 2026-11-21
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-341
    - ACT-797
  system:
    - SYS-398
    - SYS-1810
  constraint:
    - CON-856
  information:
    - INF-179
  objective:
    - OBJ-026
  time:
    - TIM-003
---

# Game: Skate Story

This analysis uses the [canonical vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
The Sony controller input, plaza geometry and four crests are instances.

## Analysis scope

- Version / ruleset: English, PlayStation 5 commercial base game
  distributed under UP3643-PPSA28801_00-0903988917779220, released
  8 December 2025 in the US storefront. Both dated traces are
  labelled PS5 and continue into the first chapter. The installed
  patches, licence type and input remapping are unreported.
- Primary decision loop: address the first obelisk to learn the Ollie.
  Skate toward each visible crest, put both feet on the board and hold
  then release Circle to pop a local ollie. Once the obelisk breaks
  and the forward portal lights, ride through it into the next lane.
- Entry: at the first obelisk headed The Ollie, after the initial
  contract and basic ride. Begin just before its lesson reveals
  the four crests around the open plaza.
- Exit: cross the first newly opened portal and reach controllable
  skating in the first fire-lined lane beyond it. The onscreen
  narration identifies using the Ollie over flames. Stop at this
  arrival, before solving the following fire route or crossing a
  second portal.
- Included: steering and approaching, obelisk lesson, both feet on
  the board, hold/release, spatially qualified crests, obelisk
  destruction and first portal arrival.
- Excluded: contract signatures, earlier powerslide and shatter
  onboarding, later trick trials, optional score optimization,
  currency spending, Philosopher and Moon encounters, the demo
  and other platforms. Exact holding duration, boundary radius,
  inputs with remapping, failure retry and reload were not tested.
- Suggested later scope: analyse one complete scored boss encounter
  with a visible combo-to-stomp conversion and settled outcome.

## Direct-play status

No direct play was performed. The PlayStation Store and Sam Eng's
announcement establish the commercial PS5 target and date.
Two independent launch-week recordings identify PS5 in their titles
or descriptions and show PlayStation glyphs, the live lesson, the
cleared plaza and the next route. Neither exposes its exact installed
patch or entitlement. PlayStation's hands-on account reinforces the
default Circle action. A separately written walkthrough documents
the four marks and portal. Only written sources and still frames
were inspected, with no video or audio playback.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
| --- | --- | --- | --- | --- | --- |
| SKST-001 | The target is the released English PS5 base game. Both PS5-described launch-week recordings include the first chapter's Ollie trial and subsequent story scenes. | Confirmed | Corroborated | High | P1, P2, W1, W2. Capture labels and button glyphs support console attribution without identifying the binaries. |
| SKST-002 | At the first instruction obelisk, the named Ollie lesson precedes the appearance of four spatial crests. The taught move remains available after the trial. | Observation | Corroborated | High | W1 6:40–7:10 and 9:00; W2 8:10–8:30 and 10:20; S1. W2 8:30 shows the four distinct active places. |
| SKST-003 | The default tutorial requires both feet on the board, holding and then releasing Circle. The player approaches or practises on the board before committing the supported release. | Observation | Corroborated | High | W1 7:00–7:30; W2 8:40–9:10; P3. Approach speed and exact holding or timing limits are not quantified. |
| SKST-004 | Perform the Ollie at each spatial crest to resolve its local requirement. The same move during approach or practice away from a crest does not by itself clear the visible target set. | Observation | Corroborated | High | W1 7:10–8:20 shows ordinary practice hops, remaining crests and a marked release; W2 8:50–9:50 shows practice and separate marked placements; S1 identifies four local executions. Exact interaction radius and every permitted order are unverified. |
| SKST-005 | Clearing the required crest set leads to the obelisk breaking and the Moon's Front opening. Portions of soul become visible at the remains. The recorded requirement is the spatial set, with no visible minimum combo score. | Observation | Direct | High | W1 8:20–8:50; W2 9:50–10:10. W1 displays the reward effect; W2 10:00 explicitly associates the break and opening. S1 confirms the trial and portal sequence. |
| SKST-006 | Opening the forward portal does not itself move the rider to the next lane. Both recordings show the player leave the plaza and regain controllable skating in the first fire-lined lane, with the Ollie cue still available. | Observation | Corroborated | High | W1 8:50–9:00; W2 10:10–10:20. The next portal and later enlarged jump lesson are outside this boundary. |
| SKST-007 | Board position, heading and motion are directly controllable while the live arena and the jump progress. Local movement and release approach are separate from claiming completion. | Observation | Corroborated | High | P3 and W1 7:00–8:20, W2 8:40–9:50. No fixed whole-trial countdown, delay measurement or score penalty rule is asserted. |

## Basic data

- Origin: Sam Eng, published by Devolver Digital on PlayStation 5.
- Analysis target: `PLAT-PLAYSTATION-5`, commercial English base
  game from The Ollie obelisk to the first Moon's Front lane.
- Mechanical families: `FAM-007`, applied to supported board movement
  and the committed jump. `FAM-014` covers an authored world opening
  created by a local state change. Sword of the Sea supports both
  boundaries independently.
- Sources checked 21 November 2026.
- P1: [US PlayStation Store](https://store.playstation.com/en-us/product/UP3643-PPSA28801_00-0903988917779220/).
  Commercial PS5 edition, date and publisher.
- P2: [Sam Eng's PS5 release announcement](https://blog.playstation.com/2025/10/09/skate-story-launches-december-8-on-ps5/).
  First-party release date, glass-bodied skater and basic trick context.
- P3: [PlayStation's hands-on coverage](https://blog.playstation.com/2025/11/24/skate-story-launches-into-the-playstation-plus-game-catalog-on-dec-8-hands-on-report/).
  Default Circle-based ollie, and distinction between skating trials
  and later combo-to-stomp battles. The dated hands-on description is
  supplementary to the commercial evidence.
- W1: [Orions Angel PS5 recording](https://www.youtube.com/watch?v=CB6ADTLQCSY&t=400s).
  Stream started 9 December 2025 UTC. At 6:40 the obelisk shows
  The Ollie. At 7:00 the default glyph is visible. At 8:20 a crest
  responds, then at 8:40 the remains are shown with the released soul.
  8:50–9:00 show the portal and first fire-lined lane.
- W2: [MaxiMumSavageYT PS5 recording](https://www.youtube.com/watch?v=EBjmX0PDQTk&t=490s).
  Stream started 8 December 2025 UTC. At 8:30 the four crests are
  visible in the panoramic reveal. 9:10 and 9:50 show local execution.
  10:00 shows the obelisk opening the Moon's Front; 10:20 shows
  already-controllable skating in the following lane.
- S1: [GameLine Chapter 1 route](https://gameline.jp/skate-story/chapter1/).
  The opening section distinguishes the four required ollies and the
  following portal from the separate later statue and boss trials.

## Mechanical decomposition

### Action Genes

- ACT-008: guide the skater between crests and align with the exit.
- ACT-341: address the obelisk and proceed through its lesson,
  enabling the named move and crest trial.
- ACT-797: with both feet supported, hold and release Circle
  to launch the ollie. No exact hold time is required by this claim.
- Claim IDs: SKST-002–SKST-004, SKST-006.

### System Behaviour Genes

- SYS-398: the tutorial grants the usable Ollie across the trial and
  into the next part of the route, where the same prompt remains.
- SYS-1810: each accepted crest has its own completion. The
  complete set resolves the obelisk and enables the forward route.
- Claim IDs: SKST-002, SKST-004–SKST-006.

### Constraint Genes

- CON-856: the currently active crest requires the designated
  trick within its local area. A practice ollie elsewhere or
  ordinary ground travel can occur without satisfying that crest.
- Claim IDs: SKST-003, SKST-004.

### Information Genes

- INF-179: read the current path and crest glow, the instruction
  prompt, the obelisk's visible change and the opened approach.
- Claim IDs: SKST-002–SKST-006.

### Objective Genes

- OBJ-026: ride through the newly available portal and actually
  reach the next traversable lane. Breaking the obelisk is interim.
- Claim IDs: SKST-005, SKST-006.

### Time Genes

- TIM-003: position, live board motion and jump commitment continue
  while the player adjusts approach or release.
- Claim IDs: SKST-003, SKST-004, SKST-007.

## Reproducible transitions

| Before | Action | Resolution | What it establishes | Claim ID |
| --- | --- | --- | --- | --- |
| The first obelisk stands without the active set | Address the lesson and advance through it | The named Ollie becomes usable and four crests appear around the plaza | Lesson and live spatial trial precede exit opening | SKST-002 |
| Board is supported and both feet are on it | Hold and release Circle | The skater and board pop into a short arc | Supported release is separate from the steering approach | SKST-003 |
| A crest is still lit and the board is elsewhere | Perform an ordinary practice ollie away from the marked area | The skater jumps and the remaining crest is still a target | Local placement is necessary for crest credit | SKST-004 |
| The skater reaches the active area | Execute the designated ollie there | The marked local requirement can clear | Different coordinates are credited separately | SKST-004 |
| The final required target is pending | Complete that crest | The obelisk breaks, the reward effect appears and the forward exit opens | The full set changes the structure of the route | SKST-005 |
| The arch is open and the rider is still in the plaza | Skate through the portal | The first fire-lined lane becomes controllable and the Ollie remains usable | Arrival is the actual observed successor | SKST-006 |

## Strategic and experiential structure

The tutorial separates lining up the board, setting both feet and
committing the held jump. Practice on plain ground helps judge the
approach but does not clear a distant crest. A rider who handles one
mark can continue to the next rather than hold all positions at
once. The visible reward and changed arch indicate completion.
Control on the other side proves the route through the opened space.
SKST-002–SKST-007.

## Replay and variation

The two console captures use different approaches, straights and
durations, but both settle the same authored four targets into
the first portal exit. They do not establish all valid orders,
a physical timing threshold, a build-to-build change or a recovery
rule on retry. SKST-003–SKST-007.

## Adjacent systems and history

The later statue, combo, Stomp and Moon sequences use other
qualification rules. The first obelisk is neither a boss nor a
high-score session. The visual aftermath is an opening route, not
evidence of a paid upgrade. Earlier demo footage does not establish
the commercial PS5 rules of this packet.

## Normalised genome

| Type | Stable genes | Role |
| --- | --- | --- |
| Action | ACT-008, ACT-341, ACT-797 | Navigate, enter the lesson and release a supported jump |
| System Behaviour | SYS-398, SYS-1810 | Retain the move and open the path after all crests |
| Constraint | CON-856 | Require a qualifying trick at each place |
| Information | INF-179 | Read visible marks and the approach |
| Objective | OBJ-026 | Enter the next lane |
| Time | TIM-003 | Commit the jump during live motion |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `614` (`GAME-0001`–`GAME-0614`).
- Exact genome matches: none.
- Tied near matches: `GAME-0599` — Sword of the Sea (`6 / 13 = 0.461538`).
- Supported combination subsets: none.
- Scan date: 2026-11-21.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
| --- | --- | --- | --- |
| [Sword of the Sea (GAME-0599)](sword-of-the-sea.md) | ACT-008, ACT-341, ACT-797, INF-179, OBJ-026, TIM-003 | Both teach a supported hold-and-release jump and require an actual arrival after the route opens. Sword of the Sea clears a gap and restores water through a separate local fixture, changing how the board travels. Skate Story retains the taught Ollie, checks its execution at four spatial crests, then opens a portal without restored water. | Near, `0.461538` |

## Taxonomy impact

- [TAXONOMY_CHANGE_361](../../../research/taxonomy-changes/TAXONOMY_CHANGE_361.md)
  records the trick-and-position predicate and the marked set's
  fixture and route resolution alongside the reused supported jump.

## Negative results

- SYS-1485 uses eligible contact to latch distinct switches.
  The Skate Story targets require a designated move at each location,
  and the set culminates in visibly destroying the instructor fixture.
- ACT-500 covers contextual trick selection and line transfer in a
  connected sequence. The first Ollie trial uses a single taught
  action and the existing supported release ACT-797.
- A practice jump away from the crests may be legal without meeting
  any target. Score, repeat variety and airborne Stomp mechanics
  belong to later scopes.
- Opening the first portal, traversing it, and reaching the later
  high jump and second portal are distinguishable states.

## Delta summary

## New facts

- [Observation | Corroborated | High] The named lesson enables a
  supported Ollie and exposes four spatial marks. SKST-002, SKST-003.
- [Observation | Corroborated | High] Practice away from the designated
  marks and local credited performances are separate. SKST-004.
- [Observation | Direct | High] The completed set breaks the obelisk.
  Both runs proceed through the first portal into the next lane.
  SKST-005, SKST-006.

## New genes

- [Observation | Corroborated | Medium] CON-856 and SYS-1810.

## New combinations

- [Observation | Direct | High] No new combination admitted.

## Taxonomy changes

- [Observation | Corroborated | High] TAXONOMY_CHANGE_361.

## New questions

- How does a short press differ from a prepared release at the exact
  edge of an Ollie crest in the identified PS5 build?
- Which crest states survive shattering or restarting inside this trial?
- Do the alternate input mappings affect the lesson's availability
  or only the displayed buttons and gestures?

## Next recommended game

- [Hypothesis | Limited | Medium] `GAME-0616`, Silent Bomber,
  North American PlayStation disc. Analyse one complete opening
  mission through charge placement, detonation and observed results.

## Why this game

- [Hypothesis | Limited | Medium] The current trial separates
  placement, a supported release and a world-state outcome. The
  next route can compare a separate object commitment to its
  deliberately triggered result.
