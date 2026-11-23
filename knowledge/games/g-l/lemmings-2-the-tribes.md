---
game_id: GAME-0638
slug: lemmings-2-the-tribes
game_title: "Lemmings 2: The Tribes"
analysis_status: reviewed
reviewed: 2026-11-22
combination_ids:
  - COMB-0025
gene_ids:
  action:
    - ACT-006
    - ACT-036
    - ACT-850
  system:
    - SYS-045
    - SYS-046
    - SYS-047
    - SYS-048
    - SYS-1841
    - SYS-1842
  constraint:
    - CON-067
    - CON-068
  information:
    - INF-592
  objective:
    - OBJ-019
  time:
    - TIM-003
---

# Game: Lemmings 2: The Tribes

This analysis uses the [canonical vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary).

## Analysis scope

- Version / ruleset: original English 1993 Psygnosis retail
  release for Commodore Amiga on three 3.5-inch disks. The manual
  describes the Amiga boot and disk swapping sequence. The primary
  capture identifies the Amiga 500. Its disk checksum and actual
  hardware or emulator build are unverified.
- Primary decision loop: watch the emerging Beach lemmings,
  assign a finite skill to a moving individual at the right
  point, aim a Roper at separate terrain, check that the others
  can use the modified route, and verify rescue at the exit.
- Entry: Play opens the first Beach preview, Quad Quirks on the
  Quay!, with its authored skill list and 9:00 initial timer.
- Exit: the gold result for 60 rescued is settled, and the next
  Beach level, The Barley Mow...., visibly begins with 60
  available and zero rescued in its own live state.
- Included: automatic release, individual role assignment,
  observed Roper and Flame Thrower behavior, support for the
  following crowd, skill stocks, timer, fast-forward, exit
  credit, medal and the ordered population handoff.
- Excluded: Practice, the Classic tribe, optional opening skills
  outside the observed route, later solutions in The Barley Mow....,
  exact medal cutoffs, save/load, disk revision parity, other
  platform ports and the ending.
- Suggested later scope: complete an Amiga transition with a
  nonzero population loss to observe a sub-60 survivor transfer.

## Direct-play status

No direct play was performed. The original manual transcript
specifies Amiga installation and the controls, rescue goal and
successor count rule. An Amiga 500-labelled full run shows the
first Beach rescue and next live level. A separately attributed
Amiga clip uses another sequence to finish the same opening.
Both video tracks were inspected through silent static frames.
The exact disk pressing, native button telemetry, sound and a
save/reload were not tested.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
| --- | --- | --- | --- | --- | --- |
| TRIBES-001 | Psygnosis distributed the commercial Amiga edition on three disks in 1993. Play opens an authored Beach level preview distinct from Practice. | Confirmed | Direct | High | P1 Amiga loading, menu and credit sections, P2 physical edition, C1 contemporary Amiga review. W1 4:40–4:58 shows Play and the first Beach preview. |
| TRIBES-002 | Beach 1 starts with 60, a displayed 9:00 and eight separate stocks of 15. The hatches release lemmings automatically. Walkers continue across terrain and fall from unsupported edges while the player addresses individuals. An accepted skill use decrements its own stock. | Observation | Corroborated | High | P1 Play controls and timed level. W1 4:50–5:17, including separate active hatches and independent Flame Thrower and Roper counts. W2 0:00–0:26 confirms the opening and a changing Flame Thrower count. |
| TRIBES-003 | The Roper has an additional aim-and-fire input after the player addresses the shooter. A successful shot attaches a line to separate terrain. The assigned Flame Thrower also resolves a single terrain-changing action. | Observation | Corroborated | High | P1 Roper and Flame Thrower entries separate the mechanisms. W1 5:11 and 5:14–5:18 shows the visible Flame Thrower burst, Roper selection and spent use before the line forms. |
| TRIBES-004 | The anchored span persists after selection changes. A later walker crosses it without another Roper use or manual steering. | Observation | Corroborated | High | P1 describes walking on the line. W1 5:17 establishes the span. The frame near 5:46 shows a walker on it with Flame Thrower or fast-forward selected and unchanged Roper stock of 14. |
| TRIBES-005 | Entry at the exit increases the rescued count. The distinct tribe count remains 60 in this run. The selected fast-forward advances the ongoing state and timer together. A live clock and typed stock remain visible. | Observation | Corroborated | High | P1 panel, rescue and fast-forward descriptions. W1 5:19 first credited rescue and 5:45–6:29 continuing entry with the speed control selected. W2 1:16–1:38. |
| TRIBES-006 | The first run settles to 60 rescued and the gold result. Rescue success and its grade are distinct. The manual describes an at-least-one progression floor and the medal as quality feedback. | Observation | Corroborated | High | P1 Objective and post-level options. W1 6:29–6:32 and W2 1:38–1:42 show the 60 and gold outcome. Exact lower medal cutoffs were not tested. |
| TRIBES-007 | The next playable Beach state is The Barley Mow...., with a fresh level clock, an authored skill list and the previous rescue headcount as its supply. | Observation | Corroborated | High | P1 explicitly defines carryover. W1 6:33–6:48 shows the main menu, the different level preview and an emerging lemming with counters of 60 and 00. W3 lists the two Amiga levels in that order. The 60-to-60 recording alone cannot distinguish carryover from a reset to that same number. |

## Basic data

- Analysis target: `PLAT-AMIGA`.
- Developer: DMA Design. Publisher: Psygnosis.
- Mechanical families: `FAM-005`, `FAM-008`, `FAM-010` and
  `FAM-015`. The player constructs a route, delegates specialist
  behavior and directs an autonomous population on a live clock.
- Checked: 2026-11-22.
- P1: [Psygnosis Amiga manual, transcript](https://www.lemonamiga.com/doc/lemmings-2-the-tribes/995), Amiga loading, Objective, Play, panel, Roper and Flame Thrower. [Second transcription of the shared rules](https://www.freegameempire.com/games/Lemmings-2/manual).
- P2: [Centre for Computing History, Amiga retail artefact](https://www.computinghistory.org.uk/det/53284/Lemmings-2-The-Tribes/).
- C1: [Amiga Computing 59, contemporary Amiga review](https://www.amigareviews.leveluphost.com/lemming2.htm), April 1993, pp. 108–109, alongside the separately attributed March 1993 Amiga Joker review.
- W1: [RickyC, Amiga 500 longplay](https://www.youtube.com/watch?v=nYFL3c1KNHQ&t=280s), 4:40–6:48.
- W2: [Game Oldies, first Beach level on Amiga](https://www.youtube.com/watch?v=CO_yIahdX3w), 0:00–1:42.
- W3: [Original Amiga walkthrough tested on a Commodore A3000](https://www.lemonamiga.com/doc/lemmings-2-the-tribes/996), Beach Tribe.

## Mechanical decomposition

### Action Genes

- ACT-006: temporarily accelerate the live simulation after the
  useful route is in place.
- ACT-036: select a limited skill and apply it to one present
  lemming. Its movement otherwise remains autonomous.
- ACT-850: aim and fire the assigned Roper at separate terrain.

### System Behaviour Genes

- SYS-045: unsteered Walkers continue to walk or fall according
  to geometry and support.
- SYS-046: an assigned Flame Thrower advances the terrain-altering
  effect without continuous input.
- SYS-047: authored hatches introduce the supplied agents in
  successive releases.
- SYS-048: entry into the exit removes the walker from live play
  and credits that rescue.
- SYS-1841: the shot anchors a crossing that keeps supporting
  later autonomous Walkers.
- SYS-1842: the settled rescue count becomes the starting
  population of the next level in the same tribe.

### Constraint Genes

- CON-067: each accepted skill assignment spends stock from its
  own level allotment.
- CON-068: the real-time attempt has a declared deadline in the
  game clock.

### Information Genes

- INF-592: read the separate survivor and rescue counts, remaining
  time and each local skill stock in the live HUD.

### Objective Genes

- OBJ-019: get the necessary members of the released population
  to the fixed exit. The demonstrated golden result credited all
  60, with a documented lower floor for campaign progression.

### Time Genes

- TIM-003: the agents move, act and leave while the player is
  choosing a recipient and assigning the next skill.

## Reproducible transitions

| From | Input or event | Result | Evidence |
| --- | --- | --- | --- |
| The Amiga menu has the Beach campaign ready | Choose Play and accept Quad Quirks on the Quay! | Nine-minute budget and 60 assigned lemmings enter the authored opening | TRIBES-001, TRIBES-002 |
| A walker reaches the useful firing point with Roper available | Assign Roper, aim at the facing slope and fire | The stock has decreased and a taut descending line connects the ledges | TRIBES-003 |
| The player has moved on to other controls | Let later walkers approach the span | A later walker uses the existing line without requesting another shot | TRIBES-004 |
| Walkers arrive at the sandcastle exit | Leave the simulation running or use fast-forward | The separately credited rescue count climbs towards the retained tribe count | TRIBES-005 |
| All 60 rescues settle | Read the result and continue the Beach branch through the menu | The gold result precedes The Barley Mow.... and its distinct live state begins with 60 supply and zero rescued | TRIBES-006, TRIBES-007 |

## Strategic and experiential structure

A fast-moving individual is the recipient of a finite command.
The Roper gives the player a further decision about the remote
terrain anchor. The resulting line can outlast that command and
carry other walkers. Clearing a bottleneck benefits following
arrivals. The current rescue count affects the next level's
population even after the grade has been displayed.

## Replay and variation

The second Amiga trace also reports 60 rescued and gold. Its
last live panel before the result still shows the initial 15
Roper and Filler uses, whereas the main trace used both. It
therefore corroborates the goal and confirms that the observed
Roper route is optional.

## Adjacent systems and history

The original Lemmings provides the indirect assignment, autonomous
population and rescue baseline. Here the additional Roper input
and the transferred population link the opened route to the next
attempt. The figure on the observed medal does not establish
a formula for later tribes, games or ports.

## Normalised genome

| Type | Stable genes | Role |
| --- | --- | --- |
| Action | ACT-006, ACT-036, ACT-850 | Accelerate, assign and aim a separate shot |
| System Behaviour | SYS-045, SYS-046, SYS-047, SYS-048, SYS-1841, SYS-1842 | Walk, resolve roles, release, credit, sustain a rope and supply the successor |
| Constraint | CON-067, CON-068 | Bound skill assignment and the attempt clock |
| Information | INF-592 | Disclose live counts and time |
| Objective | OBJ-019 | Deliver enough autonomous agents to the fixed exit |
| Time | TIM-003 | Keep the simulation live during input |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `637` (`GAME-0001`–`GAME-0637`).
- Exact genome matches: none.
- Tied near matches: `GAME-0025` — Lemmings (`9 / 16 = 0.562500`).
- Supported combination subsets: `COMB-0025`.
- Scan date: 2026-11-22.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
| --- | --- | --- | --- |
| [Lemmings (GAME-0025)](lemmings.md) | ACT-036, CON-067, CON-068, OBJ-019, SYS-045, SYS-046, SYS-047, SYS-048, TIM-003 | Both use limited skills to redirect autonomous agents toward a fixed exit while the clock runs. The first game independently changes release cadence and shows a required rescue percentage. This Beach opening has an aimed shared rope, accelerates the whole live simulation and uses the settled rescue count to supply its successor. | Near, `0.562500` |

## Taxonomy impact

Four new definitions cover the delegated aiming input, reusable
anchored line, carried headcount and live accounting panel. Ten
existing definitions apply unchanged. The goal and accepted medal
remain separate from the transfer rule.

## Negative results

- W2 settles to the same gold count with all Roper uses intact.
- The level clock can accelerate through the fast-forward control.
  No original Lemmings-style independent release-rate control
  occurs in this scoped interface.
- The shown 60-to-60 transition, without a lower-count attempt,
  corroborates only the continuation and agreement with the
  documented carry rule. Exact medal cutoffs and the effects of
  replaying the previous level remain open.

## Delta summary

Fourteen genes capture the first Beach campaign packet. Four are
new and ten are reused. Earlier signatures and definitions remain
unchanged.

## New facts

- A separately aimed rope shot gives new support to the whole
  stream of following walkers.
- A survivor count and a rescue count give different feedback
  while the level is running.
- The next attempt's population comes from the settled rescue
  headcount, according to the edition manual.

## Principles and design implications

- Make the worker command give the following crowd a visible benefit.
- Show the headcount that will advance separately from a rank.
- Allow a verified fast-forward after the layout supports safe movement.

## Puzzle or game generation potential

Prototype an autonomous crowd released from several authored hatches.
Let one assigned worker choose a remote anchor and leave shared support
behind. Carry the rescued subset's count into a second attempted layout.

## New genes

ACT-850, INF-592, SYS-1841 and SYS-1842.

## New combinations

No new combination. The existing [COMB-0025](../../combinations/COMB-0025.md) also applies to the documented Beach rescue.

## Taxonomy changes

[TAXONOMY_CHANGE_384](../../../research/taxonomy-changes/TAXONOMY_CHANGE_384.md).

## New questions

How does the same Amiga successor initialise after a lower nonzero rescue
count? Which changes to the Roper anchor alter who can cross the line?

## Next recommended game

Analyse the commercial PS4 Rollerdrome from its first arena through
a witnessed qualifier report and next arena state.

## Why this game

An action given to one moving specialist changes the route of an
entire crowd, and that crowd's rescue count sets the resources
available in the next level.
