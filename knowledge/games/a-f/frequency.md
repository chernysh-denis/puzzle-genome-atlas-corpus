---
game_id: GAME-0724
slug: frequency
game_title: "Frequency"
analysis_status: reviewed
reviewed: 2026-11-25
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-940
  system:
    - SYS-1655
    - SYS-2025
    - SYS-2026
    - SYS-2027
  constraint: []
  information:
    - INF-655
  objective:
    - OBJ-376
  time:
    - TIM-003
---

# Game: Frequency — The Winner on Expert

Use the [canonical vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
Song names, note patterns, skill settings and displayed results are
scoped parameters. No music, lyrics or full chart are reproduced.

## Analysis scope

- Version / ruleset: the English North American commercial PlayStation 2
  CD-ROM, SCUS-97125, published by Sony Computer Entertainment America in
  November 2001. Use Solo Game Mode, Expert and the booklet's standard
  control mappings. The witnessed run uses the Blue Pylon arena.
- Structured analysis target: `PLAT-PLAYSTATION-2`. Select Stage 1 and
  The Winner by The Crystal Method on Expert. Begin at the first playable
  chart, survive to the finish and read the Player Stats report. Stop when
  Continue returns to the song selection, before starting another song.
- Primary decision loop: choose an instrument track and press the input
  for each approaching note at the activator. Capture a two-bar phrase,
  let that part continue on its own and move to another track. Recover
  by choosing a later eligible phrase when a miss closes the current one.
  Watch energy and decide when to spend a stored item.
- Included: adjacent track changes, note identity and timing, whole-phrase
  capture and miss invalidation, automatic part playback and section
  boundaries, time pressure, capture streak, both Solo items, endpoint and
  the distinct terminal metrics.
- Excluded: a full chart transcription, exact timing tolerances, exact
  energy and scoring formulae, deliberate depletion or reload experiments,
  freestyle scoring, aggregate Stage 1 unlock conditions, later songs,
  Remix Mode, multiplayer and online features.
- Direct-play status: no personal PlayStation 2 or emulator session.
  The North American booklet documents the edition and rules. The main
  Expert recording names the song, difficulty and result, though the exact
  disc region, build, hardware and inputs used are unavailable. A second
  English PS2 recording corroborates the shared display and clearance
  structure. Frames were inspected in the background without sound.
  Playback behaviour is documented in the written sources.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
| --- | --- | --- | --- | --- | --- |
| FQ-001 | The scoped commercial issue is the English North American PS2 release SCUS-97125. W1 chooses Expert, Stage 1, The Winner and Blue Pylon. | Observation | Corroborated | High | P1 cover and pp. 15–16, P2 p. 40, D1, S1 Stage 1, W1 01:58–02:23 |
| FQ-002 | Left and right move the activator around the tunnel to choose an instrument track. On that track the mapped left, centre or right button must be pressed as the corresponding note reaches the activator. | Observation | Corroborated | High | P1 pp. 6, 10–12, 14, W1 02:33–02:48, W2 02:03–02:51 |
| FQ-003 | An eligible two-bar phrase captures the track only when all of its required notes are hit. A miss makes that pair inactive. A later eligible pair is visibly marked, and moving to another track is also possible while the chart runs. | Observation | Corroborated | High | P1 pp. 10–11, 14, W1 02:35–02:48, W2 02:26–03:04 |
| FQ-004 | Captured parts play automatically in their current section while the player works on another track. A section boundary can reintroduce unactivated tracks. Successful capture charges the separate Energy Meter. The song proceeds as the player changes tracks. | Observation | Corroborated | High | P1 pp. 10–12, P3, S2, W1 02:42–03:20, W2 03:41–04:05 |
| FQ-005 | Consecutive successful track activations without error award a bonus multiplier. The streak unit is a track capture. This streak rule is independent of the stored Multiplier item's temporary effect. | Observation | Corroborated | High | P1 pp. 16–17, W1 02:41–02:49 and 03:38–03:46 |
| FQ-006 | Marked notes in a bar earn one storable item. Cross deploys it separately. Auto-catcher handles the eligible free notes on its panel. Multiplier doubles earned points over the next eight bars according to the booklet. | Observation | Corroborated | High | P1 pp. 6, 10–11, 17, W1 02:36–02:44, 03:38–03:43 and 04:36–04:44 |
| FQ-007 | Live song time drains energy and activating tracks restores charge. The booklet declares failure on depletion. The successful run crosses the finish with charge remaining. No per-miss subtraction or decay rate was measured. | Observation | Corroborated | High | P1 pp. 10, 14, 16, W1 02:33–02:50 and 05:35–05:44, S2 |
| FQ-008 | W1 passes The Winner on Expert with 1,217 points, 100% song completion, 96% phrase capture accuracy and a hottest streak of 8. Continue returns to the song selection with Exterminator selected. Those numbers describe one run. | Observation | Corroborated | High | P1 pp. 16–17, W1 05:37–06:12, W2 11:57–12:35 for the shared result layout |

## Basic data

- Release / origin: Harmonix Music Systems developed Frequency
  for Sony Computer Entertainment America. The developer
  postmortem says November 2001. Listed days differ across
  catalogues, so this record scopes the month and disc serial.
- Platform or physical form: North American PlayStation 2
  disc, single-player with a standard controller. Later regional
  layouts and multiplayer formats are outside the fixture.
- Mechanical family: `FAM-010`. Notes, capture windows and
  the survival reserve continue under a live song clock.
- Primary sources accessed 2026-11-25:
  - **P1:** [Sony's North American printed instruction booklet, scan](https://download.ps2chd.com/chdps2emu/manuals/frequency.pdf),
    pp. 6, 10–12 and 14–17. Controller mapping, track activation,
    active-bar alert, energy, report and stored Solo items.
  - **P2:** [Harmonix developer postmortem](https://media.gdcvault.com/GD_Mag_Archives/GDM_August_2003.pdf),
    Game Developer, August 2003, p. 40. Developer, SCEA PS2
    collaboration and November 2001 release.
  - **P3:** [NIME 2005 proceedings](https://www.jamodrum.net/Articles/Nime05.pdf),
    the Harmonix games discussion on track capture and automatic
    playback. Its Amplitude-specific mechanics are out of scope.
- Independent sources and recorded play:
  - **D1:** [North American release and label scans](https://www.rfgeneration.com/cgi-bin/getinfo.pl?ID=U-072-S-00700-A),
    platform, media, region and product code.
  - **S1:** [Austin Garbers's PS2 song guide](https://gamefaqs.gamespot.com/ps2/516506-frequency/faqs/19277),
    Stage 1 ordering and a separate instrument breakdown. Chart
    tables are not reproduced.
  - **S2:** [Hardcore Gaming 101 play account](https://hardcoregaming101.net/freq/freq.htm),
    part playback and new sections, switching and energy.
    The publisher's booklet is authoritative for the names
    and the eight-bar duration of the stored Multiplier.
  - **W1:** [GXZ95, Stage 1 Expert run](https://www.youtube.com/watch?v=lNgf2Ut7INQ).
    Observe the song menu from 02:09, the first live chart
    around 02:35, Auto-catcher employment around 02:42,
    an explicit Multiplier deployment around 03:40, and
    the settled The Winner report at 05:56.
  - **W2:** [Let's Play 1001 Games, English PS2](https://www.youtube.com/watch?v=iy-MSVJB2Lw).
    The training sequence shows the track changes and a bass
    activation around 04:00. An independent scored song shows
    comparable play and result fields around 12:30. Only the
    common controls and interface are used from this trace.
- Reproduction labels: FQ-001–FQ-008. Compare the current
  section, the selected instrument, the pending two-bar
  window, the activation alert, the reserve and the terminal
  report independently.

## Mechanical decomposition

### Action Genes

- Reuse `ACT-008`: left and right directly move the activator
  between neighbouring tracks within the tunnel (`FQ-002`).
- New `ACT-940`: press the input corresponding to the arriving
  note's local position on the selected track at the crossing
  (`FQ-002`).

### System Behaviour Genes

- Reuse `SYS-1655`: song time drains the current reserve
  across the live chart. Capture replenishes it. The specific
  cost of a miss in this song was not measured (`FQ-007`).
- New `SYS-2025`: a clean eligible phrase activates the part
  for the current section. A miss invalidates that two-bar
  opportunity without waiting or rewinding (`FQ-003`, `FQ-004`).
- New `SYS-2026`: error-free consecutive track activations
  increase capture scoring and determine the best streak
  (`FQ-005`, `FQ-008`).
- New `SYS-2027`: collect a typed item, store at most one,
  then issue a separate command for its panel or scoring
  effect (`FQ-006`).

### Constraint Genes

No independent new constraint is required. Phrase eligibility,
bounded inventory and reserve exhaustion are part of the
systems and terminal objective specified here.

### Information Genes

- New `INF-655`: distinguish the selected part and the next
  eligible capture pair from the independent song position,
  remaining energy, score and stored-item cues
  (`FQ-003`, `FQ-004`, `FQ-006`).

### Objective Genes

- New `OBJ-376`: reach the end of one selected song with
  energy and settle the distinct song completion, phrase
  accuracy, streak and score values (`FQ-007`, `FQ-008`).

### Time Genes

- Reuse `TIM-003`: choose tracks and answer their notes before
  allotted positions pass on the running chart (`FQ-002`–`FQ-004`).

## Formal state and transitions

The state is a shared song position with one player-selected
instrument track, authored note positions, capture eligibility
and activated parts for the current section. It includes the
live energy reserve, score, uninterrupted track-capture streak,
its maximum and one stored item. Pressing a note input is judged
only against the selected part's current window. Capture changes
the playback and energy state. A later section exposes a new
set of capture opportunities on the same running clock.

## Reproducible transitions

| Before | Action or event | Bounded resolution | Claim ID |
| --- | --- | --- | --- |
| The Winner, Expert, starts with chart and energy visible | Move left or right and respond to the mapped note positions | The selected track changes; the song does not restart or wait | FQ-001, FQ-002 |
| The currently eligible pair is incomplete | Miss a required note or complete the pair | Miss invalidates this pair; a clean capture activates its part | FQ-003 |
| One part is playing automatically | Move to the next track and capture cleanly | The earlier part continues and the new capture can extend the bonus streak | FQ-004, FQ-005 |
| A marked bar and a later free-note panel are available | Capture the marked notes, then deploy the stored Auto-catcher | Typed inventory is granted and separately applied to the selected panel | FQ-006 |
| Multiplier is stored | Deploy before a scoring opportunity | Eligible points are doubled for the documented eight-bar interval | FQ-006 |
| The Expert chart reaches its end with energy | Read Player Stats and choose Continue | The clear and independent metrics settle; the song menu returns | FQ-007, FQ-008 |

## Strategic and experiential structure

Choosing what to attempt matters as much as hitting notes.
A missed pair leaves the option to wait for the next one or
switch to a more promising part. Clean captures enable both
reserve recovery and a scoring streak. An item that completes
a panel serves a different aim from a temporary point multiplier.

## Replay and variation

The song and difficulty fix the selected chart. Decisions
about track order, spent items and missed opportunities change
which parts are captured and the final scoring history.
W1 is one successful attempt, with no need to perfect every
eligible phrase.

## Adjacent systems and history

The instruction booklet also describes freestyle instruments,
arenas, bonus songs and a distinct Remix Mode. The observed
post-song arena message establishes one unlock announcement,
rather than a formula for campaign advancement.

## Normalised genome

- Action: ACT-008, ACT-940.
- System Behaviour: SYS-1655, SYS-2025, SYS-2026, SYS-2027.
- Constraint: none.
- Information: INF-655.
- Objective: OBJ-376.
- Time: TIM-003.

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `723` (`GAME-0001`–`GAME-0723`).
- Exact genome matches: none.
- Tied near matches: `GAME-0391` — Uncharted 2: Among Thieves (`2 / 12 = 0.166667`).
- Supported combination subsets: none.
- Scan date: 2026-11-25.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
| --- | --- | --- | --- |
| [Uncharted 2: Among Thieves (GAME-0391)](../s-z/uncharted-2-among-thieves.md) | ACT-008, TIM-003 | Both require moving an active body under continuing time pressure. Uncharted 2 uses surfaces and contextual transitions to climb a failing train. Frequency moves an activator between instrument tracks and resolves two-bar phrases into continued playback and energy. | Near, `0.166667`. |

## Taxonomy impact

Separate navigation between instrument tracks from timed
presses within a track. Capturing a phrase changes ongoing
playback, raises energy and forms a unit of the streak. The
item slot, separate deployment and independent terminal metrics
are observable state boundaries.

## Negative results

- One timely note does not by itself complete a two-bar phrase.
- A miss in one pair neither rewinds the song nor ends it immediately.
- A successful finish need not record perfect phrase capture.
- The documented rules do not supply exact timing or energy coefficients.
- A saving notice was observed, but save reload and persistence were not tested.

## Delta summary

Represent a first scored song as simultaneous instrument
opportunities sharing one clock. Local note judgments feed
section-bound part activation. That activation feeds survival
and scoring while new tracks remain actionable.

## New facts

- One track plays automatically after capture even when the activator moves.
- The scoring streak counts captures, not individual notes.
- The settled percentage of song completed differs from phrase capture accuracy.

## Principles and design implications

Let successful local performance make one part temporarily
autonomous. Keep the next target, remaining energy and
temporary score effects visibly distinguishable. Give the
player a useful choice after a missed window passes.

## Puzzle or game generation potential

Build a short multi-track timing fixture with a shared clock,
three local note positions, a clean phrase requirement and
separate automatic playback per part. Test misses against a
later pair on the same part and against a switch to another
part, then show both reach and accuracy at the result.

## New genes

- ACT-940
- SYS-2025
- SYS-2026
- SYS-2027
- INF-655
- OBJ-376

## New combinations

None. No verified combination matched the scoped song.

## Taxonomy changes

[Taxonomy Change 470](../../../research/taxonomy-changes/TAXONOMY_CHANGE_470.md).

## Next recommended game

Crypt Custodian on Xbox Series X|S is the next Selection 063 unit.

## Why this game

The tunnel gives one shared timing surface several competing
local opportunities. Clearing one pair changes which parts
continue playing as the other decisions remain live.

## Review status

Reviewed 2026-11-25 for the North American PlayStation 2 edition,
Stage 1 The Winner on Expert through its clear and return to selection.
