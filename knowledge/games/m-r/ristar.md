---
game_id: GAME-0659
slug: ristar
game_title: "Ristar"
analysis_status: reviewed
reviewed: 2026-11-23
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-872
    - ACT-873
  system:
    - SYS-1899
    - SYS-1900
  constraint:
    - CON-402
    - CON-693
  information:
    - INF-075
  objective:
    - OBJ-164
  time:
    - TIM-003
---

# Game: Ristar

This analysis uses the [canonical vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary).

## Analysis scope

- Version / ruleset: original English North American commercial Sega
  Genesis cartridge, Sega 1555, released in February 1995. The manual and
  English recordings support the scoped rules. Exact ROM revision, media
  bytes, physical system and configured input in the recordings are
  unverified. The four displayed hit-capacity stars match the manual's
  Normal rules.
- Entry: start the first area of Round 1, Planet Flora, from Game Start at
  the title menu. The round title hands off to ordinary side-view control
  in the bright forest, before the first target or overhead ladder.
- Primary decision loop: steer and jump into reach, aim a grab toward a
  compatible fixture or enemy, then act on the resulting state. Traverse
  overhead rungs, grab a creature to pull the body into a hit, and catch
  the snake's exposed head in the enclosed route. Reach the ordinary exit
  Star Handle, build rotation, release and steer the resulting flight.
- Exit: the exit flight awards Height Bonus and the game displays
  Next Area: Dark Woods. The score carries into Dark Woods and normal
  movement returns. The principal run earns 8,000 height points and
  begins Dark Woods at 11,900 points.
- Included: direct ground and air movement, the aimed extending hands,
  compatible fixed anchors, hurt capacity, grab-to-impact, the confined
  snake fight, spin-and-release, height scoring and the exact handoff.
- Excluded: unrelated opening story, bonus-room treasure and clock as
  requirements, item throws in the absence of a traced instance, secret
  thresholds, exact timing windows or height formula, password and
  continue routes, Dark Woods encounters, the Flora planet-boss battle,
  Game Gear, Japanese regional rules and later ports or compilations.
- Suggested later scope: compare release angles and flight input from
  identical positions on the exit handle, and measure the score bands
  independently of clearing the later planet boss.

## Direct-play status

No direct play was performed. The original North American Genesis
booklet in Sega's archive supplies the inputs and general rules.
LongplayArchive's Retro Game Spacko run supplies the primary route;
VICIOGAME's separate English Genesis/Mega Drive recording corroborates
the transition. Still frames and on-screen text were inspected in the
background without audio. Neither clip establishes precise controller
state, exact carrier bytes, or a tested fail or reload outcome.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
| --- | --- | --- | --- | --- | --- |
| RI-001 | The English North American Sega 1555 release uses the Genesis direction pad to aim and B to grab under the default configuration; A or C jumps. The first stage starts on Planet Flora. | Observation | Corroborated | High | P1 printed pp. 3–6 and 13, R1 for the US carrier and release, W1 1:20–1:27 and W2 1:21–1:29. Button assignment is documentary. |
| RI-002 | The grab extends the avatar's hands toward an object or creature. Fixed traversal fixtures and enemies yield different outcomes. The overhead ladder supports lateral traversal; releasing it can return the body to free movement. | Observation | Corroborated | High | P1 pp. 4, 6–7; W1 1:36–1:44 and W2 around 1:43–1:49. The manual specifies Jump to let go of ladders. Hand reach and target compatibility are shown without a measured maximum. |
| RI-003 | Shooting the hands toward a compatible hostile can grip it and pull the avatar into a close impact. A missed or premature reach does not clear an enemy. | Observation | Corroborated | High | P1 pp. 6–7 distinguishes creature grabs from object throws; W1 1:36–1:38 and 3:32–3:39; R2 explains contact and head hits. No creature throw is claimed. |
| RI-004 | The live encounter opens the segmented snake's head at different holes. Clearing the required snake allows passage out of the enclosed section. The main route still needs to reach and use a separate exit handle. | Observation | Corroborated | High | R2 Flora Area 1; W1 3:31–3:43 and W2 3:25–3:37. The full hit count and exact hole sequence across retries were not inferred. |
| RI-005 | Take the fixed Star Handle, hold the grab and apply lateral input as documented to increase spin, then release and steer the resulting flight. The final ordinary handle settles this area. | Observation | Corroborated | High | P1 printed pp. 10–11, R2, W1 3:43–3:52 and W2 3:37–3:42. The captures show attachment, changing body angle and departure. No exact release frame was isolated. |
| RI-006 | The primary clear credits a separate 8,000-point Height Bonus, taking the visible score from 3,900 to 11,900. Dark Woods is named, then opens in live control with that score retained. | Observation | Corroborated | High | W1 3:44–4:07, W2 3:42–3:57 and R2 for the separate launch-height reward. The 8,000 points are an observed clear outcome, not a fixed threshold. |
| RI-007 | The HUD shows gold stars for remaining hit capacity, separately from score. A normal run can show four stars. | Observation | Corroborated | High | P1 pp. 5 and 8–9 and the four visible stars in W1 and W2. Lives and retries are documentary and were not forced in the scoped trace. |

## Basic data

- Analysis target: `PLAT-SEGA-GENESIS`, original English North
  American Sega 1555 commercial cartridge, February 1995.
- Developer: Sega's Sonic Team. North American publisher: Sega of America.
- Mechanical families: `FAM-007`, physics and object manipulation;
  `FAM-010`, real-time system pressure.
- Checked: 2026-11-23.
- P1: [Sega's original North American Genesis instruction booklet](https://www.sega.jp/genesismini2/assets/manual/pdf/US_Ristar.pdf).
  The contemporary booklet is hosted in Sega's Genesis Mini 2 archive.
  Printed pp. 4–8 and 10–13 identify input, states and handle uses.
- R1: [Genesis US cartridge release catalogue](https://gamefaqs.gamespot.com/genesis/586423-ristar/data).
  Identifies Sega 1555 and the February 1995 release.
- R2: [JRagan's Sega Genesis route](https://gamefaqs.gamespot.com/genesis/586423-ristar/faqs/2827).
  Distinguishes the Flora Area 1 required snake, optional bonus room,
  separate exit handle and the height reward.
- W1: [LongplayArchive's attributed English NTSC Genesis capture](https://www.youtube.com/watch?v=zbrh8c_NrHI&t=82s),
  credited to Retro Game Spacko, September 2020. Main trace through
  the first Dark Woods moves.
- W2: [VICIOGAME's separate Genesis/Mega Drive trace with area chapters](https://viciogameblog.com/2017/08/14/ristar_mega_drive_complete_gameplay/),
  August 2017. Its [recording](https://www.youtube.com/watch?v=V6B8b6rpzzs&t=81s)
  supplies a second route to Dark Woods. Original hardware and cartridge
  identity are unverified for both recordings.

## Mechanical decomposition

### Action Genes

- ACT-008: steer the body across forest ground, jumps and landings.
- ACT-872: aim the same extend-and-grab input toward an object or
  creature rather than steering ordinary movement into it.
- ACT-873: hold a fixed handle, command rotation and intentionally
  release into steerable flight.

### System Behaviour Genes

- SYS-1899: a successful creature grab contracts the gap by drawing
  the avatar into an impact on the held target. The action is distinct
  from throwing a held inanimate item.
- SYS-1900: at the ordinary exit, the release flight settles a
  height-based score credit. Reaching the next area is a separate
  completion boundary and does not require the maximum bonus.

### Constraint Genes

- CON-402: clear the required snake in the enclosed section before
  continuing toward the final handle. Forest enemies outside that route
  gate are not a compulsory global set.
- CON-693: an aimed extended arm can support traversal only with a
  compatible, reachable fixture. Empty air or ordinary scenery cannot
  support the planned attachment.

### Information Genes

- INF-075: read the current gold hit-capacity stars while deciding
  whether to approach or wait. The point tally is separate.

### Objective Genes

- OBJ-164: use the final Star Handle to trigger the flight settlement
  and arrive in the named successor, Dark Woods, with the score carried.

### Time Genes

- TIM-003: jumps and aimed grabs occur while falling, roaming foes
  and the snake's current opening advance. Spin and release also
  happen on the live field.

## Reproducible transitions

| State | Action or event | Result | Evidence |
| --- | --- | --- | --- |
| Planet Flora starts with the body on the left | Steer right, jump when needed and aim the hands above the body near overhead rungs | A reachable rung supports lateral travel; the body can subsequently return to free motion | RI-001, RI-002 |
| A roaming creature is in hand reach | Send the grab toward it | The grip closes the gap and the follow-through strikes the creature | RI-003 |
| Enter the confined section with multiple wall holes | Adjust position and grab toward the head when it emerges. Repeat as it moves to other holes | The required snake is defeated and the path to the terminal approach becomes usable | RI-003, RI-004 |
| The fixed ordinary Star Handle is within a jump's reach | Grab it, hold and command rotation | The body accelerates around the fixed handhold as its angle changes | RI-005 |
| Rotation established, ordinary exit handle still held | Release and steer the flight | The transition settles a visible Height Bonus. The main route's 3,900 becomes 11,900 | RI-005, RI-006 |
| Next Area: Dark Woods has been announced | Let the transition complete and resume movement | The next area is playable with 11,900 in the principal trace | RI-006 |

## Strategic and experiential structure

The hands are an aimed reach shared by terrain and enemies. Choosing a
latch changes what the next movement does: traverse a rung, close for
an impact, or build aerial momentum around a fixed handle. The final
release must be prepared by attachment and rotation. Height scoring
then evaluates the flight without replacing the need to advance.

## Replay and variation

Both routes visit a bonus chamber en route, clear a snake and leave
via the ordinary handle. The optional bonus detour is not required by
the ordinary completion rule and its treasure is outside this scope.
The two recordings retain different cumulative scores. The visible
departure route and successor match without demanding the same local
fight timings or earlier pickups.

## Adjacent systems and history

Sega's booklet distinguishes attachable ladders, climbing surfaces,
carryable objects, moving fixtures and bonus handles. Object throws,
secret-handle destinations and the separate planet-level scoring
receipt are not needed to reproduce this area transition. Dark Woods
and the later Flora boss would be separate research scopes.

## Normalised genome

| Type | Stable genes | Role |
| --- | --- | --- |
| Action | ACT-008, ACT-872, ACT-873 | Move locally, aim the hands and command a deliberate spin release |
| System Behaviour | SYS-1899, SYS-1900 | Contract a creature grab into impact and score the exit flight's height |
| Constraint | CON-402, CON-693 | Clear the enclosed route and use eligible reachable anchors |
| Information | INF-075 | Read remaining hit capacity |
| Objective | OBJ-164 | Resolve the terminal exit and resume in Dark Woods |
| Time | TIM-003 | Act while traversal and local threats remain live |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `658` (`GAME-0001`–`GAME-0658`).
- Exact genome matches: none.
- Tied near matches: `GAME-0387` — Super Bomberman (`4 / 20 = 0.200000`).
- Supported combination subsets: none.
- Scan date: 2026-11-23.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
| --- | --- | --- | --- |
| [Super Bomberman (GAME-0387)](../s-z/super-bomberman.md) | ACT-008, CON-402, OBJ-164, TIM-003 | Both require live navigation and hostile clearance before a region-specific exit. Bomberman clears the stage roster with timed, cardinal bomb blasts and visits an uncovered tile. Ristar clears a local snake encounter with an aimed grasp, then uses a separate rotation-and-release exit with a height reward. | Near, `0.200000` |

## Taxonomy impact

ACT-872 aims a grasp at both reachable hosts and world fixtures and
hands the follow-through to the selected target's rules. ACT-361
commits a grappling-line approach, and SYS-653 can stop at an anchor
without causing a committed impact. SYS-1899 specifically resolves
the approach as an impact with a susceptible held creature.
ACT-873 differs from the shape-adjusting tether of ACT-531, the
direction selection of ACT-569 and the passive moving vine release of
ACT-633. It powers rotation at one fixed pivot before release.
SYS-1900 describes height-based score settlement independently of the
player command and terminal successor. SYS-1337 evaluates a cycling
committed symbol, rather than flight height.

CON-402 applies to the snake enclosure. OBJ-164 applies to the
later handoff. No new gene is needed solely to name the snake's
head or count its openings. SYS-1858 predicts a distinct following
body or tail threat that remains unverified here.

## Negative results

- Walking toward or reaching the handle without a deliberate
  release is not the recorded clear sequence.
- Defeating the snake is a local gate, not the terminal result.
- The normal exit route does not depend on mastering a bonus room,
  throwing a creature or achieving maximum departure height.
- Exact controller state, head immunity timing, acceleration
  coefficients and retained state after reload were not verified.

## Delta summary

Ten scoped genes. Four new definitions and six existing boundaries.

## New facts

- Aimed hands can establish traversal support or pull the avatar
  into a creature, depending on what is caught.
- A fixed Star Handle creates a player-controlled rotation phase
  between reach and free flight.
- The last handle yields a height credit and a separately named,
  playable successor.

## Principles and design implications

Let one aiming input establish different commitments without a mode
selector. Put an encounter where the useful contact moves among
visible openings. After it clears, use a distinct exit pose to
reward execution quality without adding a mandatory score threshold.

## Puzzle or game generation potential

Put one reusable grabbing tool between a foe visible only through
openings and a fixed wheel axle. Time a grab for the foe, then make
the exit release itself a score-bearing movement with an immediate
successor.

## New genes

- ACT-872
- ACT-873
- SYS-1899
- SYS-1900

## New combinations

None. The scoped signature supports none of the 274 verified
combination subsets. No verified support list changes.

## Taxonomy changes

[TAXONOMY_CHANGE_405](../../../research/taxonomy-changes/TAXONOMY_CHANGE_405.md).

## New questions

How many release angles produce a useful upward arc at fixed speed?
How sensitive is the height credit to in-flight steering? Can the
player pass a given carried target or change direction before impact?

## Next recommended game

The Roottrees are Dead, the English commercial Windows Steam remake
from 2025. Trace a bounded source trail through family-tree placement
and the first verified lock of correct assignments.

## Why this game

A single directed limb extension supports traversal and attacks, while
an authored handle breaks the final motion into reach, powered rotation
and free flight. The height reward and actual exit are both observable.
