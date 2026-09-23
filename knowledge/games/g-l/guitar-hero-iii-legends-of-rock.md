---
game_id: GAME-0372
slug: guitar-hero-iii-legends-of-rock
game_title: "Guitar Hero III: Legends of Rock"
analysis_status: reviewed
reviewed: 2026-09-23
combination_ids: []
gene_ids:
  action:
    - ACT-508
    - ACT-509
  system:
    - SYS-1010
    - SYS-1011
    - SYS-1012
    - SYS-1013
  constraint:
    - CON-676
  information:
    - INF-299
    - INF-379
  objective:
    - OBJ-215
  time:
    - TIM-003
---

# Game: Guitar Hero III: Legends of Rock

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). The song, guitar
model, coloured buttons and stage are parameters, not gene names.

## Analysis scope

- Version / ruleset: original English PlayStation 3 retail-disc rules from
  Activision's Guitar Hero III instruction booklet (2007). No disc image,
  console, executable version or patch was inspected.
- Structured analysis target: the original PlayStation 3 edition in
  [`knowledge/platforms/games.json`](../../platforms/games.json).
- Primary decision loop: read upcoming coloured chart events, hold the
  corresponding Easy-difficulty fret or chord, strum in time, maintain long
  holds and the Rock Meter, complete marked Star Power phrases, and choose
  when to spend the accumulated charge before the next note sequence.
- Entry: single-player Quick Play with an already available song selected on
  Easy and a compatible Guitar Hero Les Paul controller. The particular song
  and unlocked-song history are recorded parameters; the manual does not
  establish a specific title as available in every new save.
- Evaluation boundary: reach the selected song's authored end while the Rock
  Meter has not failed, then inspect the results-screen grade, score, notes-hit
  rate and streak. A five-star result is not required. This finishes one song,
  not Career or the game.
- Noncompletion: sufficiently poor chart play can take the Rock Meter to its
  flashing-red failure state and remove the performer before the song ends.
  A low score alone is not declared failure; another Quick Play attempt can
  be made.
- Included: fixed Easy chart using green/red/yellow frets, single notes,
  simultaneous chords, strumming, long holds, live judgement and score,
  streak multiplier, the four Rock Meter states, star-shaped phrase completion,
  half-full Star Power activation, temporary doubling, and the results screen.
- Excluded: Career cash and song unlocks, other difficulty charts, song list
  completeness, co-op, online and Guitar Battle, downloadable songs, guitar
  customisation, Practice and Tutorials, optional Whammy Bar tone bending or
  extra charge, exact timing windows and hidden score/meter coefficients.
- Reproducible parameterisation: record the PS3 disc identity and controller,
  selected available song, Easy chart, starting gauge state, every visible
  note/chord/sustain event and input time, hit or miss, streak, score,
  Star Power phrase and activation, Rock Meter progression, failure or song
  endpoint, and the final results. No perfect-play trace is asserted.
- Direct-play status: not conducted. No console, disc, build hash, save,
  screenshot, video, audio or input trace was inspected. This is a bounded
  reconstruction from Activision's original PS3 instruction booklet.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `GH3-001` | Original PS3 Quick Play accepts a currently earned or unlocked song, and Easy uses green, red and yellow frets | Confirmed | Direct | High | P1 |
| `GH3-002` | The player holds corresponding frets and strums as notes scroll toward the judgement area; chords contain simultaneous notes | Confirmed | Direct | High | P1 |
| `GH3-003` | Long single notes and chords require every corresponding fret held through the sustain after strumming | Confirmed | Direct | High | P1 |
| `GH3-004` | Consecutive hits raise a 2×–4× score multiplier, while a mistake removes it | Confirmed | Direct | High | P1 |
| `GH3-005` | Rock Meter exposes green, yellow, red and flashing-red performance states; continuing poor play can fail the song | Confirmed | Direct | High | P1 |
| `GH3-006` | Completing an entire glowing phrase charges Star Power; at half-full the player can activate it to double the current multiplier until charge expires | Confirmed | Direct | High | P1 |
| `GH3-007` | Song results report stars, score, longest streak and note-hit percentage | Confirmed | Direct | High | P1 |
| `GH3-008` | One selected Easy Quick Play song is a reproducible evaluation packet, not a Career completion or claimed played run | Observation | Limited | Medium | P1 |

## Basic data

- Release / origin: Neversoft-developed Guitar Hero III: Legends of Rock,
  published by Activision in 2007.
- Platform or physical form: original PlayStation 3 retail disc with compatible
  guitar controller; the research did not inspect physical media or hardware.
- Puzzle family: charted performance under real-time system pressure.
- Primary source:
  - P1: [Activision's original PS3 instruction booklet, pp. 4–10](https://www.yumpu.com/en/document/view/6266335/gh3-ps3-manual-cover-activision/7),
    checked 2026-09-23. The publisher-authored booklet is mirrored by Yumpu;
    the host's surrounding summaries are not evidence.
- Secondary sources: none used for the scoped mechanics.
- Claim IDs: `GH3-001`–`GH3-008`.

## Mechanical decomposition

### Action Genes

- New `ACT-508`: each chart event needs the correct held fret set and an
  intentional strum at the event; simultaneous notes are one chord commitment.
- New `ACT-509`: spend accumulated Star Power by controller tilt or SELECT
  only after the meter is at least half-full.
- Claim IDs: `GH3-002`, `GH3-006`.

### System Behaviour Genes

- New `SYS-1010`: the authored chart advances and judges single notes,
  chords, misses and sustains against live input.
- New `SYS-1011`: uninterrupted successful notes grow the temporary 2×–4×
  score multiplier; a mistake breaks the streak.
- New `SYS-1012`: a complete star-shaped phrase earns charge; activated
  Star Power drains while doubling the then-current multiplier.
- New `SYS-1013`: the Rock Meter changes with performance and can end a
  weak run before the chart's final note.
- Resolution order: chart event approaches → fret/strum is judged → hit or
  miss changes score, streak and Rock Meter → eligible complete phrase adds
  charge → activation temporarily doubles the score multiplier → survival
  through the final event opens the results screen.
- Claim IDs: `GH3-002`, `GH3-004`–`GH3-007`.

### Constraint Genes

- New `CON-676`: a long single note or chord requires all corresponding
  frets held after a valid initiating strum until the sustain has played;
  hitting the head alone is insufficient.
- Easy's three coloured frets are this packet's difficulty parameter, not
  a universal prohibition on blue/orange in the other charts.
- Claim IDs: `GH3-001`, `GH3-003`.

### Information Genes

- New `INF-379`: approaching chart lanes, streak multiplier, score, Rock
  Meter and Star Power show the next action and current risk.
- Reused `INF-299`: the completed song's result exposes grade, score,
  note-hit rate and streak as a bounded performance breakdown.
- Claim IDs: `GH3-002`, `GH3-004`–`GH3-007`.

### Objective and Time Genes

- New `OBJ-215`: survive one selected song to its results; maximising stars
  is optional, and ending Career is outside this packet.
- Reused `TIM-003`: the chart advances on a live schedule while fretting,
  strumming and Star Power timing remain available.
- Claim IDs: `GH3-005`, `GH3-007`, `GH3-008`.

## Reproducible transitions

| Before | Action | Bounded resolution | Establishes | Claim |
|---|---|---|---|---|
| Available song in solo Quick Play | select Easy and start | authored three-fret chart begins scrolling | bounded entry and live clock | `GH3-001`, `GH3-002` |
| Single green note approaches the line | hold green and strum in time | note is hit, score and streak can rise, Rock Meter responds | two-part timed commitment | `GH3-002`, `GH3-004`, `GH3-005` |
| Red and yellow gems align at one chart time | hold both frets and strum | chord is judged together rather than as two independent later events | simultaneous event | `GH3-002` |
| Long green note begins | strum with green held, then maintain hold | the played sustain continues until its tail; early release cannot satisfy the full hold | duration obligation | `GH3-003` |
| Long red/yellow chord begins | strum with both frets held, then maintain both | the simultaneous sustain continues until its tail; releasing either fret early cannot satisfy the full hold | multi-fret duration obligation | `GH3-003` |
| Marked star-shaped phrase approaches | hit every marked note | the completed phrase charges Star Power; an incomplete phrase does not earn that full charge | phrase-gated resource | `GH3-006` |
| Star Power is at least half-full | tilt controller or press SELECT | activated charge drains and doubles the current scoring multiplier | chosen spend timing | `GH3-006` |
| Errors accumulate near flashing red | continue missing | Rock Meter can fail and stop the song before its chart end | negative terminal | `GH3-005` |
| Final chart event passes with Rock Meter still viable | finish the song | result shows stars, score, note-hit rate and streak | positive terminal | `GH3-007` |

## Strategic and experiential structure

- The chart makes the immediate future visible, but its events continue to
  arrive. Correct fret choice is not enough without a timely strum.
- A hit streak raises the value of later notes, so losing continuity has a
  scoring cost separate from Rock Meter danger.
- Star Power is both earned by whole marked phrases and spent at a chosen
  moment. Holding charge for a later dense passage can improve score, but
  this packet does not claim an optimal activation schedule or hidden formula.
- The survival gauge and star grade answer different questions: a mediocre
  scoring run can still reach the song result, while enough misses can end it.

## Replay and variation

- The selected song's Easy chart is authored, not random. Player input
  timing, hit streak, phrase completion, activation timing and final grade
  vary between attempts.
- Another song or difficulty changes chart parameters and is not silently
  treated as the same exact event sequence.

## Adjacent systems and history

- Geometry Dash couples music and visual pulses to an authored obstacle route;
  Guitar Hero III judges the music chart's notes themselves through fret plus
  strum and exposes a live survival meter.
- Simon asks the player to reproduce a disclosed symbolic order, but it does
  not present a continuously scrolling multicolour chord-and-sustain chart.
- Batman: Arkham Asylum has a combat-chain multiplier, not song-note scoring;
  the separate rhythm-chart exclusion in that gene remains intact.

## Normalised genome

The front matter is canonical. This reviewed packet has 11 Active genes: two
Action, four System Behaviour, one Constraint, two Information, one Objective
and one Time. Nine boundaries are new; `INF-299` and `TIM-003` are reused.

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `371` (`GAME-0001`–`GAME-0371`).
- Exact genome matches: none.
- Tied near matches: `GAME-0371` — Pokémon Snap (`2 / 22 = 0.090909`).
- Supported combination subsets: none.
- Scan date: 2026-09-23.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0371` Pokémon Snap | `INF-299`, `TIM-003` | Both act under live timing and expose a bounded result breakdown; Pokémon Snap captures and curates photographs during an automatic tour, while Guitar Hero III judges fret-strum notes on an authored song chart and can fail through its Rock Meter. | Tied near, `2 / 22 = 0.090909`; not an exact match. |

## Taxonomy impact

`TAXONOMY_CHANGE_111` records nine additive boundaries. No lower-ID game
signature or verified combination changes.

## Negative results

- The booklet does not support a precise timing window, Rock Meter delta,
  initial song list or optimal Star Power activation time in this packet.
- A results-screen star grade is not a universal win threshold, and a low
  score is not independently a fail state before the song ends.
- Optional whammy expression, Career purchases and Battle attacks are not
  imported into this solo Quick Play analysis.

## Delta summary

The publisher's PS3 booklet establishes a fixed chart whose colour-and-time
events require fret plus strum, a long-note hold, a streak-sensitive score,
phrase-earned Star Power and a separate live Rock Meter survival condition.

## New facts

- [Confirmed | Direct | High] Easy uses three fret colours and a song's
  chart is judged during live play (`GH3-001`–`GH3-003`).
- [Confirmed | Direct | High] Streak, Star Power and Rock Meter resolve
  separately before the terminal results (`GH3-004`–`GH3-007`).

## New genes

- [Observation | Direct | High] Add `ACT-508`, `ACT-509`, `SYS-1010`–`SYS-1013`,
  `CON-676`, `INF-379` and `OBJ-215` for the chart, performance-resource and
  song-survival boundaries.

## New combinations

- None; one rhythm-game carrier does not establish a recurring combination.

## Taxonomy changes

- `TAXONOMY_CHANGE_111` records the nine additive gene boundaries.

## New questions

- Direct play on a pinned original PS3 disc could verify exact chart timing,
  Rock Meter behaviour and optional whammy effects without inferring them
  from the manual.

## Next recommended game

`GAME-0373` Spore, as reserved in
[`SEARCH_DEMAND_GAME_SELECTION_027`](../../../research/selection/SEARCH_DEMAND_GAME_SELECTION_027.md).

## Why this game

Spore changes the primary loop from timed song-chart execution to authored
creature construction and simulation-mediated progression.

## Completion checklist

- [x] Original PS3 rule packet, one-song entry and survival exit bounded.
- [x] Publisher manual separated from direct play and hidden coefficients.
- [x] Deterministic comparison, bilingual presentation, artwork and gates.

## Search-demand continuation

This is the third reserved unit in
[`SEARCH_DEMAND_GAME_SELECTION_027`](../../../research/selection/SEARCH_DEMAND_GAME_SELECTION_027.md).
