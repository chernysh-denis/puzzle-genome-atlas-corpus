---
game_id: GAME-0634
slug: samba-de-amigo
game_title: "Samba de Amigo"
analysis_status: reviewed
reviewed: 2026-11-22
combination_ids: []
gene_ids:
  action:
    - ACT-844
    - ACT-845
  system:
    - SYS-1835
    - SYS-1836
  constraint:
    - CON-865
  information:
    - INF-299
    - INF-588
  objective:
    - OBJ-341
  time:
    - TIM-003
---

# Game: Samba de Amigo

This analysis uses the [canonical vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary).

## Analysis scope

- Version / ruleset: Sonic Team and Sega's original 2000 North American
  retail Dreamcast release, Sega part 51092. English, Arcade, Normal,
  Maracas input. The carrier, regional repertoire and input scheme are
  corroborated separately. No physical disc checksum was available for W1.
- Primary decision loop: set the player height, choose the first chart,
  read each moving cue's destination and arrival, shake in the matching
  band or hold the indicated pose, then retain a high enough live rank
  to clear the song and select a second one.
- Entry: the first song within the observed Arcade Normal credit.
  Both players enter with maracas, confirm height and select
  The Cup of Life. Player 1 makes the music selection.
- Exit: The Cup of Life clears with C for player 1 and D for player 2.
  The stage-two list appears and Al Compas del Mambo starts.
- Included: height reference, six targets, live note, rapid-shake and
  pose cues, immediate feedback, the performance gauge and rank,
  separate results and common advancement in the recorded two-player case.
- Excluded: later chart play, alternative input mappings, Party,
  Challenge and Training, downloads, arcade hardware, PAL and Japanese
  releases, Ver.2000 and later ports. No exact shake or timing threshold,
  sensor model or complete multiplayer failure rule is asserted.
- Suggested later scope: establish how the two-player game behaves when
  neither player qualifies or only player 2 reaches the passing rank.

## Direct-play status

No direct play was performed. Sega's English retail booklet defines the
control mapping, independent height references and advancement. W1 is a
public Dreamcast capture with an inset showing the players and the
maraca-specific setup instructions. It shows The Cup of Life from
selection to result and into stage two. P2's carrier and W2's explicitly
US-labelled reference recording corroborate the edition. W2 is supporting
release evidence only. W1 does not show a disc checksum or controller
serial. Audio, exact input timestamps and sensor telemetry were not tested.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
| --- | --- | --- | --- | --- | --- |
| SAM-001 | The 2000 North American Dreamcast original is Sega part 51092. This ruleset includes Arcade Normal and native Maracas input. | Confirmed | Direct | High | P1 pp. 4–7 and 10–16, P2 US carrier scans. W1 0:13–0:50 shows the English menus and maraca-specific setup. W2 publisher-independent US-labelled capture corroborates the English roster. |
| SAM-002 | Select a height bracket before the song. The Maracas setup uses a left-hand height change to browse and a right-hand shake or button to enter. The booklet links appropriate height selection to correct detection. | Observation | Corroborated | High | P1 pp. 5 and 12. W1 0:34–0:56 shows the setup instructions and both Height Select columns. The general warning at 0:27 alone would not identify the input. |
| SAM-003 | The ordinary cue requires a shake at the destination when it arrives. Paired red, yellow and green targets distinguish upper, middle and lower bands. Separate cues request rapid shaking. The game differentiates accepted and missed input. | Observation | Corroborated | High | P1 pp. 2–3, 7 and 13. W1 0:59–1:30 and 1:51–2:28 show outward travel, target responses and rapid-shake prompts. |
| SAM-004 | Some directed cues require holding the shown two-shaker pose. Matching and missing it yield distinguishable O and X outcomes. | Observation | Corroborated | High | P1 p. 3. W1 around 1:50, 2:00 and 2:41–2:47 shows the silhouette and both outcome symbols. |
| SAM-005 | Accepted or missed cues change a segmented gauge and its current letter rank. A full gauge promotes the rank. On Normal, reaching empty at E can terminate the song early. At the end of the chart the passing rank is C or better. | Observation | Corroborated | High | P1 pp. 11, 13 and 16. W1 0:59–2:48 shows rank changes for both players. Early failure at empty E is a documented branch and was not tested in the accepted attempt. |
| SAM-006 | After The Cup of Life player 1 has 100,300 points, 56 Max Amigos, 87% and C. Player 2 has 89,475 points, 27 Max Amigos, 85% and D. The game shows Cleared and both parts are active when Al Compas del Mambo starts. | Observation | Direct | High | W1 2:52–3:01 result, 3:02 Music Select and 3:13–3:16 new stage. P1 pp. 13 and 15 define advancement and the result categories. No opposite-player qualification or both-fail case inferred. |

## Basic data

- Analysis target: `PLAT-DREAMCAST`.
- Developer: Sonic Team. Publisher: Sega.
- Mechanical family: `FAM-010`, real-time system pressure.
- Checked: 2026-11-22.
- P1: [Sega's English Dreamcast instruction booklet](https://www.digitpress.com/library/manuals/dreamcast/samba_de_amigo.pdf), pp. 2–7 and 10–16.
- P2: [Scans of the US Sega 51092 carrier and packaging](https://www.rfgeneration.com/cgi-bin/getinfo.pl?ID=U-071-S-01830-A).
- W1: [YoVideogames, Dreamcast Quick Look part 1](https://www.youtube.com/watch?v=vw-t3ca0yQk&t=13s), setup and the first complete chart through its recorded successor.
- W2: [NintendoComplete, attributed North American commercial original](https://www.youtube.com/watch?v=TaQaaM-NQQc&t=219s), Arcade Hard reference used only to corroborate roster and edition.

## Mechanical decomposition

### Action Genes

- ACT-844: position a shaker at an indicated height and shake in
  time with the arrival, repeating rapidly when the chart requests it.
- ACT-845: place and hold both shakers in the special indicated pose.

### System Behaviour Genes

- SYS-1835: judge ordinary notes by arrival alignment and position,
  and judge the distinct held pose against the displayed arrangement.
- SYS-1836: change the segmented performance gauge and promote or
  demote the live letter rank. Empty E can end the Normal chart.

### Constraint Genes

- CON-865: set a player height bracket for correct shaker-position
  detection before the chart begins.

### Information Genes

- INF-299: report score, longest accepted streak, accuracy and rank
  separately for both players after settling the first chart.
- INF-588: show the approaching objects, destination circles,
  special prompts, immediate judgement and live performance state.

### Objective Genes

- OBJ-341: finish the first chart with a qualifying rank and reach
  the following song selection.

### Time Genes

- TIM-003: read and respond while the song's chart advances in real
  time. Waiting on a cue loses the opportunity to match it.

## Reproducible transitions

| State | Input or event | Result | Evidence |
| --- | --- | --- | --- |
| Arcade entry with Maracas input | Both players join, player 1 chooses Normal, and players enter their height brackets | Player 1 can choose the first song from the listed chart options | SAM-001–SAM-002, W1 0:17–0:56 |
| The Cup of Life chart advances | Shake at an arriving target or repeat on a rapid cue | Immediate responses and gauge changes are displayed as the chart continues | SAM-003, SAM-005 |
| A Pose Mark appears during the chart | Hold the pictured arrangement | A corresponding O or X is displayed independently for each player | SAM-004 |
| The first chart reaches its end at C and D | The chart closes | The results screen reports separate totals and a common clear | SAM-006 |
| First-stage clear is settled | Music Select reopens and player 1 confirms the highlighted next song | Both sets of targets appear at the start of Al Compas del Mambo | SAM-006 |

## Strategic and experiential structure

A cue tells the player where to put the shaker and when to act.
Pose cues instead require a stable arrangement. The formula for
the letter rank is distinct from the displayed accuracy percentage.
Better held rank matters at two points: during the track at the
lowest-rank failure boundary and at the end when deciding clearance.
The first credited chart ends with separate performance reports
and one shared transition in the observed two-player run.

## Replay and variation

Normal's first qualifying stage can be replayed with different
performance histories. The manual distinguishes at least C for
ordinary progression and a larger Arcade menu after A. The recorded
C advances to a conventional stage-two selection. The expanded list
after A was not tested in this unit.

## Adjacent systems and history

Arcade is the name of the chosen mode within the Dreamcast disc.
The external cabinet, Original mode's larger song selection,
other modes, saving, and the later Japanese update have separate
scope and do not supply first-chart rules here.

## Normalised genome

| Type | Stable genes | Role |
| --- | --- | --- |
| Action | ACT-844, ACT-845 | Time shakes and hold signalled poses |
| System Behaviour | SYS-1835, SYS-1836 | Judge each response and refresh live performance rank |
| Constraint | CON-865 | Establish the height used for detecting positions |
| Information | INF-299, INF-588 | Show active cues and settled performance categories |
| Objective | OBJ-341 | Clear the first chart into the next selection |
| Time | TIM-003 | Act while the chart advances |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `633` (`GAME-0001`–`GAME-0633`).
- Exact genome matches: none.
- Tied near matches: `GAME-0406` — DanceDanceRevolution (`2 / 14 = 0.142857`).
- Supported combination subsets: none.
- Scan date: 2026-11-22.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
| --- | --- | --- | --- |
| [DanceDanceRevolution (GAME-0406)](../a-f/dancedancerevolution.md) | INF-299, TIM-003 | Both force decisions during the chart and show performance categories with the final ranking. DanceDanceRevolution judges foot-panel inputs in four lanes and the scoped chart must end with its live dance gauge above zero. Samba's shaker positions depend on player height, with separate held poses and a passing live rank that opens the next stage. | Near, `0.142857` |

## Taxonomy impact

Seven definitions cover positioned shaking, the held-pose action,
height-dependent control, outward cues, local adjudication, live rank
and rank-gated stage advancement. The established results-information
and live-timing genes apply unchanged.

## Negative results

- The general safety warning is displayed with either supported input
  method. Use the maraca-specific menu prompts and camera evidence to
  distinguish the recorded setup.
- A chart endpoint, a high hit rate and a passing letter rank are
  different observations. The shown D and its 85% do not support
  an accuracy-only qualification threshold.
- The recorded two-player clearance does not establish the complete
  rule for how both players' ranks interact on other results.

## Delta summary

Nine genes describe the first evidenced Normal chart, seven new and
two reused. Earlier gene definitions and game signatures are unchanged.

## New facts

- Each player sets a height reference before both start the first chart.
- Cue direction, arrival time and the distinction between a shake
  and a pose are visible before each judgement.
- The recorded C/D split produces individual result rows, one clear
  and an actual next-chart start.

## Principles and design implications

- Distinguish where a gesture should occur from when it is scored.
- Present pose prompts separately from momentary hits and repeats.
- Make intermediate performance rank legible during play and
  show its relationship to the eventual stage decision.

## Puzzle or game generation potential

Use fixed target heights but alternate a few short arrival patterns
with jointly held positions. Practice each response separately before
placing both in one scoreable sequence.

## New genes

ACT-844, ACT-845, CON-865, INF-588, OBJ-341, SYS-1835 and SYS-1836.

## New combinations

None. No verified combination has every required member in this signature.

## Taxonomy changes

[TAXONOMY_CHANGE_380](../../../research/taxonomy-changes/TAXONOMY_CHANGE_380.md).

## New questions

Does the shared transition still occur if only player 2 is at C or
above? What exact live condition terminates the other player's part
when only one gauge empties at E?

## Next recommended game

Analyse the first evidenced Communion interaction and following
transition in the commercial Nintendo Switch release of 1000xRESIST.

## Why this game

A single chart joins spatial targeting, gesture timing and an
explicit ranked progression gate. The recorded transition ties those
systems to a concrete result on the original home release.
