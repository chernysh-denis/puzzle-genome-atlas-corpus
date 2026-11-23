---
game_id: GAME-0635
slug: 1000xresist
game_title: "1000xRESIST"
analysis_status: reviewed
reviewed: 2026-11-22
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-107
    - ACT-846
  system:
    - SYS-1837
    - SYS-1838
  constraint:
    - CON-866
  information:
    - INF-589
  objective:
    - OBJ-342
  time:
    - TIM-002
---

# Game: 1000xRESIST

This analysis uses the [canonical vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary).

## Analysis scope

- Version / ruleset: commercial English Nintendo Switch eShop release
  of May 9, 2024, Nintendo product 70010000059157. The launch-labelled
  capture W1 does not disclose a binary version. W2 is attributed to
  docked first-generation Switch, version 1.0.7. Their observed route
  and transition agree.
- Primary decision loop: navigate the school in the first available
  remembered period, learn why the nominated gym scene is absent,
  follow the redirected rooftop conversation and verify the earlier
  playable period. Test the prompted period jump after it becomes
  available.
- Entry: the opening school scene of Chapter 1, Watcher's first
  Communion. The active period is 00, Temperature Days. The gym
  is a named destination in the recorded route.
- Exit: the rooftop conversation with Jiao's Picture transitions
  to −02, Day of the Dance, 2047 CE. Three search objectives appear.
  The marked jump controls switch to 00 and back to −02, after
  which ordinary school traversal continues.
- Included: local navigation and route-bearing dialogue, the blocked
  remembered gym, the rooftop redirect, the scripted transition,
  the two exposed periods and an observed reversible jump.
- Excluded: optional handset recordings and unrelated dialogue,
  the later three Jiao encounters and the end of the chapter, the
  prologue, chapter selection, reload persistence, other chapters,
  other platforms, exact input timings and universal coordinate
  correspondence between time periods.
- Suggested later scope: complete one Jiao encounter in −02 through
  the resulting memory fragment and return.

## Direct-play status

No direct play was performed. P1–P2 establish the released
Switch product and define Communion. Developer interviews explain
the two-period design and the time-jump mechanic. Static frames
of two attributed Switch recordings were read. W2 labels its
hardware setting and version in the description. Audio, controller
telemetry and direct binary comparison were outside this review.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
| --- | --- | --- | --- | --- | --- |
| RES-001 | The commercial Nintendo Switch game launched May 9, 2024. During Communion, Watcher explores episodes remembered by the ALLMOTHER. | Confirmed | Direct | High | P1 and P2. W1 about 14:55 and W2 about 10:48 show the playable dark school in period 00. |
| RES-002 | The gym scene is unavailable when reached in 00. Secretary explains that Communion is limited to what its experiencer experienced or dreamt, then identifies a presence on the roof. A rooftop interaction becomes the displayed objective in the observed route. | Observation | Corroborated | High | W1 33:22–34:05 and W2 15:06–15:34. The gym remains unavailable in both samples. The footage does not expose internal route flags. |
| RES-003 | Watcher takes the stairs to the rooftop scene and talks to Jiao's Picture. The picture dialogue establishes another period as relevant to finding the desired memory. | Observation | Corroborated | High | W1 36:48–38:07 and W2 16:29–17:41. Scene label and subtitles. No alternate conversation branch is asserted. |
| RES-004 | The conversation's authored transition changes the school manifestation from 00 to −02, the Day of the Dance in 2047 CE. The earlier rooftop has distinct occupants and becomes navigable. | Observation | Corroborated | High | W1 38:07–38:15 and W2 17:40–17:52. HUD labels and resumed movement. P3 corroborates two periods in this chapter. |
| RES-005 | The successor exposes three separate search locations for Jiao: the cafeteria, music room and detention. Movement and speech with other occupants are available. | Observation | Direct | High | W2 17:43–17:51 and 17:54–18:36. W1 38:10–38:39 corroborates the tasks and new occupants. The tasks are not completed inside the packet. |
| RES-006 | After the initial transition, the game exposes hold commands toward the other period. W2 returns from −02 to 00, then back to −02 at the matching stairwell, with different lighting and reachable occupants. | Observation | Corroborated | High | W2 17:52 and 18:39–18:49. W1 about 40:18–40:31 corroborates the return to 00. P3–P4. No exact position preservation across all scene pairs is inferred. |

## Basic data

- Analysis target: `PLAT-NINTENDO-SWITCH`.
- Developer: sunset visitor 斜陽過客. Publisher: Fellow Traveller.
- Mechanical families: `FAM-011`, time reversal and loop retention,
  and `FAM-012`, knowledge and evidence progression.
- Checked: 2026-11-22.
- P1: [Nintendo Switch product and release details](https://www.nintendo.com/en-gb/Games/Nintendo-Switch-download-software/1000xRESIST-2561116.html?nsuid=70010000059157).
- P2: [Fellow Traveller’s May 9, 2024 launch announcement](https://www.fellowtraveller.games/blog/your-communion-begins-1000xresist-is-out-now).
- P3: [Remy Siu on the two Chapter 1 periods and time jumps](https://www.crunchyroll.com/hi/news/interviews/2024/7/28/1000xresists-remy-siu-on-the-power-of-performance).
- P4: [Developer interview on overlaid timelines](https://www.gamedeveloper.com/design/-test-diverse-backgrounds-in-theater-music-and-dance-shaped-time-bending-thriller-1000xresist).
- W1: [justonegamr, Switch launch gameplay](https://www.youtube.com/watch?v=ZwTIb1VnoP4&t=1998s).
- W2: [Handheld Players, Switch 1 docked gameplay](https://www.youtube.com/watch?v=DhW9YseP6ik&t=902s).

## Mechanical decomposition

### Action Genes

- ACT-008: guide Watcher around the school, towards the gym and
  then up the stairs to the disclosed rooftop target.
- ACT-107: obtain the rooftop route through Secretary’s dialogue
  about the missing gym scene.
- ACT-846: use the prompted directional hold to commit a jump
  between periods after the second becomes available.

### System Behaviour Genes

- SYS-1837: settle the rooftop conversation into the first earlier
  scene and expose the successor objectives and temporal access.
- SYS-1838: switch the active local manifestation when a valid
  period jump resolves.

### Constraint Genes

- CON-866: the active remembered period does not supply the gym
  space merely because a destination is named and its door is visible.

### Information Genes

- INF-589: read the current period label and date and the presented
  past or future jump to the other available school period.

### Objective Genes

- OBJ-342: follow the redirected encounter until the earlier school
  becomes playable and its three search tasks are exposed.

### Time Genes

- TIM-002: explore and address the relevant dialogue in player-paced
  order. The selected period is a scene state, without a running
  countdown forcing the gym-to-rooftop route.

## Reproducible transitions

| State | Input or event | Result | Evidence |
| --- | --- | --- | --- |
| Watcher can move in the 00 school | Reach the gym entrance and complete the local explanation | The gym is unavailable. Secretary redirects the route to the rooftop entity | RES-002 |
| The rooftop route is identified | Ascend to the roof and follow the dialogue with Jiao's Picture | The authored conversation supplies the link to the earlier setting | RES-003 |
| The rooftop conversation reaches its ending beat | The memory transitions automatically | −02 becomes active. Day of the Dance and the three new search locations appear | RES-004–RES-005 |
| −02 is active and the future direction is displayed | Use the available jump toward 00 | Temperature Days and its dark roof and stairwell reappear | RES-006 |
| 00 is active at the stairwell | Use the available jump toward the earlier period | The matching stairwell appears in −02. Traversal proceeds in that period | RES-006 |

## Strategic and experiential structure

The stated destination and the currently traversable scene can
disagree because the active memory limits what is available.
Dialogue provides the route around that boundary. The first
switch of period is a result of the rooftop encounter. Later jumps
are deliberate inputs within the available set. Identifying the
current period helps the player distinguish the new route from
an ordinary path within one school state.

## Replay and variation

W1 spends longer on school conversations than W2, but both
reach the same earlier period. W2 demonstrates a return and a
second jump without repeating the rooftop exchange. The exact
expiration and access rules for later goals and arbitrary positions
were not tested.

## Adjacent systems and history

The prologue, Orchard, later Communion structures, chapter replay
and ending decisions are separate. The observed three search tasks
establish the successor without making their solutions part of this
opening analysis.

## Normalised genome

| Type | Stable genes | Role |
| --- | --- | --- |
| Action | ACT-008, ACT-107, ACT-846 | Move, learn the redirected route and jump to an available period |
| System Behaviour | SYS-1837, SYS-1838 | Admit the earlier scene, then change the active local manifestation |
| Constraint | CON-866 | Bound traversal by the selected memory |
| Information | INF-589 | Show the current and available remembered period |
| Objective | OBJ-342 | Reach the playable earlier encounter set |
| Time | TIM-002 | Advance through player-paced local actions |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `634` (`GAME-0001`–`GAME-0634`).
- Exact genome matches: none.
- Tied near matches: `GAME-0624` — Paradise Killer (`3 / 13 = 0.230769`).
- Supported combination subsets: none.
- Scan date: 2026-11-22.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
| --- | --- | --- | --- |
| [Paradise Killer (GAME-0624)](../m-r/paradise-killer.md) | ACT-008, ACT-107, TIM-002 | Both allow player-paced movement and dialogue that yields an actionable fact. Paradise Killer supports building an accusation and proceeding to a trial. The school packet in 1000xRESIST uses a local memory boundary, a scripted encounter and then freely commanded shifts between the two exposed periods. | Near, `0.230769` |

## Taxonomy impact

The six additions distinguish the control, access boundary, readable
period, required outcome, scripted opening and repeatable period
change. Movement, dialogue-supplied facts and self-paced progression
use existing definitions.

## Negative results

- Reaching the gym in 00 does not give access to its absent scene.
- The first visible jump to −02 is a conversation outcome. Holding
  the direction applies after the second period becomes available.
- Switching the viewed period does not establish the ability to
  rewrite remembered events. Local correspondence is observed at
  the staircase without asserting it at every point.

## Delta summary

Nine genes describe the first bounded school step. Six are new
and three are reused. Earlier signatures, definitions and family
boundaries are unchanged.

## New facts

- The current memory excludes the nominated gym scene and exposes
  a different point of entry through the rooftop.
- The first conversation with the pictured figure opens a playable
  earlier period and displays three locations for the next search.
- Both periods become directly revisitable in the sampled footage.

## Principles and design implications

- Make the reason a destination is unavailable legible within the
  active scene.
- Separate an authored first visit from a repeatable transition the
  player commands afterward.
- Mark the active period explicitly so differences in people,
  lighting and access read as authored state rather than visual noise.

## Puzzle or game generation potential

Present an initially unavailable room and a nearby authored link to
an earlier view of the same building. Give the player a small set of
period choices so each view can support a distinct next interaction.

## New genes

ACT-846, CON-866, INF-589, OBJ-342, SYS-1837 and SYS-1838.

## New combinations

None. No verified combination has every required member in this signature.

## Taxonomy changes

[TAXONOMY_CHANGE_381](../../../research/taxonomy-changes/TAXONOMY_CHANGE_381.md).

## New questions

Which sections bar a return to the other period while a local memory
fragment is active, and how do they restore the prior location?

## Next recommended game

Analyse the first exterior asteroid operation through its evidenced
transition in the original MS-DOS CD-ROM release of The Dig.

## Why this game

The opening separates linear narrative discovery from direct
temporal navigation and visibly tests both within one school.
