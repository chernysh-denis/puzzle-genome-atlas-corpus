---
game_id: GAME-0633
slug: flock
game_title: "Flock"
analysis_status: reviewed
reviewed: 2026-11-22
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-842
    - ACT-843
  system:
    - SYS-1834
  constraint:
    - CON-864
  information:
    - INF-587
  objective:
    - OBJ-340
  time:
    - TIM-003
---

# Game: Flock

This analysis uses the [canonical vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary).

## Analysis scope

- Version / ruleset: July 16, 2024 commercial Xbox Series X|S
  release, Xbox product 9N6DGNBPNRNN. English interface, fresh
  solo opening. Two release-week recordings identify Xbox Series.
  The exact capture build and hardware of the Series X|S-labelled
  trace are unverified.
- Primary decision loop: observe a wild individual, confirm
  the description that fits it, recover the whistle for its family,
  align the two range indicators and sing, then verify that the
  individual has joined the active flock.
- Entry: after the lesson at The Water Towers, fly to the nearby
  ledges with resting Bewls and observe the one identified by the
  game as a Basking Bewl. Recover the Bewl whistle during the
  opening tutorial.
- Exit: the first evidenced Basking Bewl charm succeeds and
  the creature accompanies the rider during resumed flight.
  The later My Flock screen verifies the distinction from a
  guide entry without making later recruitment part of the unit.
- Included: local flight, field identification, the family
  whistle prerequisite, live spatial singing, visible grade and
  outcome, and one actual follower. A later failed attempt is a
  boundary check.
- Excluded: internal range or grade formulas, an exact number
  of notes, capture patch, audio, reload persistence, collecting
  other families, subsequent story and sheep management, and
  online cooperation.
- Suggested later scope: verify retention of one individual
  when the active group is full or after restoring a save.

## Direct-play status

No direct play was performed. The Xbox listing and publisher
identify the commercial edition and the collect-and-follow rule.
W1 and W2 are separate release-week captures attributed to Xbox
Series X|S and Series X respectively. W2 shows Solo Game during
setup. The Xbox button glyphs and achievement prompts corroborate
the carrier. Rules, positional changes and outcomes were read
from static frames. The exact game build, controller telemetry
and audio were not verified.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
| --- | --- | --- | --- | --- | --- |
| FLK-001 | The commercial Xbox Series edition launched July 16, 2024, supports one player and permits the scoped solo route. | Confirmed | Direct | High | P1, P2. W2 shows Solo Game at setup. |
| FLK-002 | Inspect a live Bewl and select from descriptive clues. The tutorial accepts the Basking Bewl identification and adds the entry to Creature Guide before a charm occurs. | Observation | Corroborated | High | W1 2:55–3:10 and 3:23–4:08, with confirmation about 3:56 and named acknowledgement about 3:58. W2 repeats the observation and guide sequence around 2:40–3:30. |
| FLK-003 | Recovering the whistle for Bewls makes charm available for that family. An earlier guide entry did not itself recruit a Bewl. | Observation | Corroborated | High | W1 10:16–10:28 displays the recovered whistle and the later lesson. W2 7:52–8:04 shows recovery and the advice that the whistle is usable on Bewls. P2. |
| FLK-004 | During charm, one set of wave brackets marks the target range and the other changes with the player. Move to match and press A to sing. | Observation | Corroborated | High | W1 11:05–11:14 and W2 8:07–8:12 expose the same written lesson and live marks. |
| FLK-005 | The game grades the attempted song separately from declaring the creature charmed. W1 shows Excellent and a first-charm achievement. W2 shows Great followed by Charmed on a Basking Bewl. | Observation | Corroborated | High | W1 11:12–11:23. W2 8:07–8:16. Recovered whistle and prior species acknowledgement are separately visible. |
| FLK-006 | The recruited creature accompanies the rider across continued flight. Later, My Flock lists Basking Bewls in independent member slots rather than just as species discoveries. | Observation | Corroborated | High | W1 11:14–11:18, 11:25–11:30 and 11:41–11:57. My Flock at 16:56–17:00 shows three after additional successes. W2 8:12–8:16 and P2–P3 corroborate following. |
| FLK-007 | The same early activity can end with Spooked It and a return to ordinary flight instead of that target joining. | Observation | Corroborated | High | W2 8:17–8:22 and 8:36–8:46. The written lesson distinguishes the effects of unsuitable distance. No universal numerical cutoff is inferred. |

## Basic data

- Analysis target: `PLAT-XBOX-SERIES`.
- Developers: Hollow Ponds and Richard Hogg. Publisher: Annapurna Interactive.
- Mechanical families: `FAM-002` hidden-state inference and
  `FAM-015` agent routing and coordination.
- Checked: 2026-11-22.
- P1: [Xbox Store release listing](https://www.xbox.com/en-US/games/store/flock/9n6dgnbpnrnn).
- P2: [Annapurna Interactive's published game description](https://annapurnainteractive.com/games/flock).
- P3: [Launch interview with Ricky Haggett and Mike Robinson](https://www.gamedeveloper.com/design/better-together-making-sense-of-the-frenetic-floating-fleets-in-flock),
  which describes the independently following group behind the
  controlled bird.
- W1: [Lutfi Barakat, July 20 Xbox Series X|S opening](https://www.youtube.com/watch?v=jTi81M9lTiU&t=661s).
- W2: [Skycaptin5, July 19 Xbox Series X solo opening](https://www.youtube.com/watch?v=LJCCYQSx7lU&t=482s).

## Mechanical decomposition

### Action Genes

- ACT-008: fly the bird locally around the ledges and meadow in
  the current play space.
- ACT-842: confirm one description that fits the observed natural
  subject and gain its named guide entry.
- ACT-843: position the bird relative to the target, then actively
  sing at the chosen distance.

### System Behaviour Genes

- SYS-1834: grade an eligible song from the current alignment and
  advance or settle the attempt. A bad outcome can dismiss the
  current wild target.

### Constraint Genes

- CON-864: start charm only with the whistle linked to the
  encountered family. Observation alone does not grant the tool.

### Information Genes

- INF-587: compare the fixed target brackets, moving own
  brackets and separate charm progress. See individual feedback
  before reading the final verdict.

### Objective Genes

- OBJ-340: settle one successful charm and verify the recruited
  creature accompanying the bird during continued movement.

### Time Genes

- TIM-003: move and submit the song while flight and the
  live position relationship keep changing. No beat chart or
  elapsed-time cutoff is inferred.

## Reproducible transitions

| State | Input or event | Result | Evidence |
| --- | --- | --- | --- |
| Arrival at the Bewl ledges | Observe the pink individual and confirm the fitting description | The tutorial names Basking Bewl and Creature Guide receives the entry | FLK-002 |
| The species is known and its whistle is lost | Complete the opening whistle recovery | A distinct Bewl whistle is recovered before charm becomes available | FLK-003 |
| One Basking Bewl is eligible | Start charm and adjust flight distance | Two bracket pairs and the charm indicator are visible beside the target | FLK-004 |
| The bracket pairs align | Press A to sing | The game reports the grade. W2 shows Great followed by Charmed at about 8:12 | FLK-004, FLK-005 |
| The first charm settles | Leave the ledge in ordinary flight | The creature leaves its earlier location and follows the player's bird | FLK-006 |
| A separate later charm is open | Submit an ill-positioned attempt | Spooked It ends that attempt without another follower | FLK-007 |

## Strategic and experiential structure

Identification uses visible evidence about a fairly stationary
subject. Charm uses a live spatial relationship and sends an input
from that position. A player can know the species and have the right
tool but still mistime a song against their changing distance. The
output of good performance is a following body in the world.

## Replay and variation

The two Xbox captures choose the same first named species and succeed
under different visible grades or progress sequences. The clips
establish the presence of success and failure states. They do not
establish an exact minimum grade, a fixed quantity of songs for every
target or the persistence of an individual across a saved reload.

## Adjacent systems and history

The publisher describes hover-sheep, knitting and optional
cooperation. Those systems are not needed to read or verify the first
wild follower. Later My Flock occupancy corroborates the active
membership type. Other recruitment and removing a member remain
separate material.

## Normalised genome

| Type | Stable genes | Role |
| --- | --- | --- |
| Action | ACT-008, ACT-842, ACT-843 | Approach, identify from clues, and sing from a chosen flight position |
| System Behaviour | SYS-1834 | Grade the attempt and publish the success or spook outcome |
| Constraint | CON-864 | Match the recovered whistle to the target family |
| Information | INF-587 | Read own range, target range and current charm progress |
| Objective | OBJ-340 | Gain and observe one active following creature |
| Time | TIM-003 | Make positional decisions within live flight |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `632` (`GAME-0001`–`GAME-0632`).
- Exact genome matches: none.
- Tied near matches: `GAME-0391` — Uncharted 2: Among Thieves (`2 / 11 = 0.181818`).
- Supported combination subsets: none.
- Scan date: 2026-11-22.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
| --- | --- | --- | --- |
| [Uncharted 2: Among Thieves (GAME-0391)](../s-z/uncharted-2-among-thieves.md) | ACT-008, TIM-003 | Both accept movement decisions while the current physical relationship keeps changing. Uncharted 2 requires leaving a collapsing rail carriage for stable ground. Flock uses live spacing about a creature to judge a submitted song, then confirms a follower in free flight. | Near, `0.181818` |

## Taxonomy impact

Six definitions cover descriptive field identification, the
separate spatial song input, a family tool requirement, relative
distance and progress feedback, charm adjudication, and the active
follower outcome. They do not alter the general movement and
real-time genes or earlier captures.

## Negative results

- A named guide entry neither proves charm nor places a creature
  in the active group.
- An aligned song or positive grade is an event before the
  success state. W2 documents a distinct failure state on another
  target.
- Whistle eligibility is local to a family in the shown lesson.
  No global whistle permission or one-use inventory debit is shown.

## Delta summary

The first Xbox charm packet admits eight genes with six new
definitions. It does not revise earlier signatures or require a
new combination or family.

## New facts

- The tutorial separates a matched live description and a named
  guide entry from active recruitment.
- The recovered Bewl whistle enables the subsequent family charm.
- The first settled Basking Bewl continues flying with the
  rider, providing direct membership evidence beyond a grade.

## Principles and design implications

- Expose prerequisites, positional information and success as
  different states.
- Check active following to distinguish world-state membership
  from collection-screen discovery.
- Support a soft failure boundary on the current encounter
  without making a separate existing follower disappear.

## Puzzle or game generation potential

One design experiment would reuse one portable species clue
and one typed song tool across two encounters. Vary the speed of
the moving actor and the preferred spacing so that learning the
subject identity and achieving a position become separate tests.

## New genes

ACT-842, ACT-843, CON-864, INF-587, SYS-1834 and OBJ-340.

## New combinations

None. No verified combination has every required member in this signature.

## Taxonomy changes

[TAXONOMY_CHANGE_379](../../../research/taxonomy-changes/TAXONOMY_CHANGE_379.md).

## New questions

What happens to the same recruited individual when the active
group reaches capacity or a saved solo game is restored?

## Next recommended game

Analyse one complete first song on the North American Dreamcast
commercial original Samba de Amigo in Maracas mode.

## Why this game

The opening cleanly separates target discovery from the skill that
recruits it. The successful action has an immediate world-state
result that can be seen after the tutorial display closes.
