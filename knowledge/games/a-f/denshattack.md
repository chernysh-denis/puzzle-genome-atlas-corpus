---
game_id: GAME-0687
slug: denshattack
game_title: "Denshattack!"
analysis_status: reviewed
reviewed: 2026-11-24
combination_ids: []
gene_ids:
  action:
    - ACT-500
    - ACT-797
    - ACT-908
    - ACT-909
  system:
    - SYS-1961
    - SYS-1962
  constraint: []
  information:
    - INF-632
  objective:
    - OBJ-364
  time:
    - TIM-003
---

# Game: Denshattack! — Adventure awaits! on PlayStation 5

This record uses the [canonical vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
The neighboring gorge tracks, finish arch and result identify the fixture.

## Analysis scope

- Version / ruleset: commercial English PlayStation 5 base game,
  US PlayStation Store product UP2660-PPSA29952_00-SIEESIEADSHA0000,
  released July 15, 2026. Launch-window solo Chapter 1, track
  1-2-1, Adventure awaits!, Miyazaki Prefecture. The captures identify
  PS5 and PS5 Pro. Exact installed versions and recording regions
  were not independently verified.
- Structured analysis target: PLAT-PLAYSTATION-5 in
  [platform coverage](../../platforms/games.json).
- Entry: select track 1-2-1 after the opening tutorial missions
  with the standard yellow railcar shown in W1. Start the live
  run after Fernando's briefing and the opening countdown.
- Primary decision loop: read the approaching bend or gap, time
  a drift on the current rail or prepare a jump, direct an air
  transfer onto the next track where useful and choose compatible
  tricks on the way. A manual can carry the provisional score line
  through rail contact. Continue to the marked finish under the
  briefed score and time conditions.
- Exit: Track Cleared and its report show distinct score, elapsed
  time and optional checks. Stop before the next track.
- Included: the ordinary automatic forward run, supported jump,
  airborne rail transfer, bend drift, air trick and manual chain,
  pending and credited score, finish conditions and separate
  result measures. One supplementary crash comparison bounds
  which score and time can persist during recovery.
- Excluded: exact score formula, failure cutoffs and boost or
  landing tolerances, exact button remaps and controller telemetry,
  alternative finish paths, comprehensive dare and collectible
  requirements, persistence across saved runs, early demos, Deluxe
  content, bosses, later levels, leaderboards and non-PS5 ports.
- Potential scoped module: compare the optional Perfect Drift
  counter with the separate time medal across two same-build runs.
- Direct-play status: no personal PS5 execution or binary
  inspection. Sony and the publisher identify the commercial game.
  W1 and W2 name their PlayStation capture platforms and show
  separate completed runs. W3 corroborates the briefing and a
  recovery example without disclosing its platform. Only short
  visual sequences were examined in the background, with no audio.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
| --- | --- | --- | --- | --- | --- |
| DA-001 | The English PS5 commercial base game released on July 15, 2026. Solo 1-2-1 Adventure awaits! opens with a briefing that tells the player to reach the goal on time with a minimum score. No exact failure cutoff was isolated. | Confirmed | Corroborated | High | P1, P2, W1 7:38–8:10, W2 9:50–10:10, W3 12:00 |
| DA-002 | Forward rail travel continues through local steering decisions. Marked bends prompt a timed drift. The optional counter increments for Perfect Drift results, separately from current score. | Observation | Corroborated | High | W1 1:38–1:48, 8:11–8:25, W2 10:00–10:30, W3 13:00 |
| DA-003 | The earlier tutorial teaches a held and released jump and an Air Switch while airborne. On 1-2-1 a transfer chooses adjacent support over the gorge. The train then moves along the new rail, and a Transfer label can appear amid other stunts. | Observation | Corroborated | High | P1, W1 3:00–3:32 and 8:38–8:53, W2 10:55–11:15 |
| DA-004 | Pending points and the chain marker can rise without changing the already credited score. Air tricks, transfers and manual-supported contact can stay in a single pending line. In a second run shorter chains increase the credited total before the finish. The UI alone does not specify how to compute final score. | Observation | Corroborated | High | P1, W1 8:17–10:02, W2 10:10–11:55, W3 12:20–12:45 |
| DA-005 | At the finish arch W1 transitions into Track Cleared and reports 44,592, 1:45 and 7/7. W2 also clears, with 15,033, 1:53 and 6/7, and displays distinct score and time medal colours. The report is open before advancing to the next track. | Observation | Corroborated | High | W1 10:02–10:24, W2 12:00–12:20, W3 15:00 |
| DA-006 | The publisher describes in-run checkpoints. In the supplementary capture, recovery returns to an earlier section, recomputes the white total to an earlier value and clears a pending chain while elapsed time continues. The crash-free PS5 routes do not independently test that exact penalty or time span. | Observation | Limited | Medium | P3, W3 13:33–14:01, R1 |

## Basic data

- Release / origin: Undercoders and Fireshine Games, July 15,
  2026, English commercial PlayStation 5 download.
- Mechanical families: FAM-007 for retaining or regaining motion
  through compatible rail support, and FAM-010 for continuous
  travel through successive scored decisions with a time condition.
- P1: [PlayStation Store's US PS5 base-product listing](https://store.playstation.com/en-us/product/UP2660-PPSA29952_00-SIEESIEADSHA0000).
  Establishes the commercial product, standard and Deluxe
  distinction, release date, player count and English availability.
- P2: [Enad Global 7's dated launch announcement](https://www.mfn.se/a/enad-global-7/denshattack-published-by-fireshine-games-launches-today.iframe)
  and [PlayStation's release-day notice](https://www.youtube.com/watch?v=2gOL6y8iCHc).
  Confirm commercial availability and the train stunt premise.
- P3: [Undercoders' July 10 pre-launch accessibility notes](https://steamcommunity.com/app/2524850/allnews/?l=latam).
  Use Accessibility Info for Launch, the checkpoint, in-run
  dare progress and always available tutorial sections. This is
  a developer note in the Steam news feed, not a PS5 build ID.
- W1: [Admiralvic's recorded PS5 full run](https://www.youtube.com/watch?v=wPACZmQVb7Q&t=458s).
  The author identifies a supplied review copy and PS5 capture.
  Use the tutorial at 1:38–3:32 and the 1-2-1 activation through
  result at 7:38–10:24. The selected stage is named in the
  capture. Trace attribution does not establish an installed patch.
- W2: [Ben-Gun's PS5 Pro commercial playthrough](https://www.youtube.com/watch?v=1M_k2YuIBY4&t=550s),
  published July 16, 2026. Use 9:10–12:20, from region selection
  to the same track's separate result. Use recent trick, score
  and medal displays for corroboration.
- W3: [Cheat Day Gaming's opening commercial route](https://www.youtube.com/watch?v=-PGgUGOgjSU&t=690s),
  July 19, 2026. Use the 11:30 chapter lead, 12:00 briefing,
  13:33–14:01 score and recovery and the approximately 15:00
  result. Platform is unconfirmed.
- R1: [Access-Ability's hands-on release-window account](https://access-ability.uk/2026/07/24/denshattack-accessibility-review/).
  Supports the distinction among pending multipliers, checkpointed
  points and elapsed time. It does not identify the captured PS5 build.
- Claim IDs: DA-001–DA-006.

### Reproducible fixture evidence

1. Play the tutorial missions first. In W1 check the warned curves
   around 1:38–1:48 and the supported-jump and Air Switch teaching
   around 3:00–3:32. Launch 1-2-1 after the tutorials.
2. At 8:07–8:11 the commercial PS5 run changes from its
   countdown to live forward travel with zero credited points.
   Read the signs before the early bends. From about 8:18–8:23,
   a manual follows an air trick and a Perfect Drift dare
   counter ticks during the early sequence.
3. Around 8:38–8:53 cross the gorge segment between adjacent
   routes while airborne. Compare the Transfer and manual labels
   at 8:43–8:47 in W1. The pending line continues while the
   white total stays at zero. In W2 compare the advancing white
   totals at different contacts around 10:20–11:20.
4. Follow the final track toward the marked arch. Around 10:02
   the PS5 timer shows 1:45 before Track Cleared. Allow the
   result panels to settle. Read 44,592, 1:45 and 7/7 in W1
   and 15,033, 1:53 and 6/7 at about 12:10 in W2.
5. For the optional recovery comparison, W3 shows white totals
   of 5,540, 5,340, 5,790, 5,340, then 5,856 and 5,340 with
   sections repeated as elapsed time rises. The later change
   from about 13:52 to 13:58 also removes a pending marker.
   These frames bound the rollback; they are not a PS5 build test.

## Mechanical decomposition

### Action Genes

- ACT-500: choose a contextual airborne trick and use a manual
  to link a rail contact into another trick. DA-004.
- ACT-797: prepare and release the jump from a supporting
  track rather than choose a destination remotely. DA-003.
- ACT-908: select the neighboring eligible track while airborne
  during the gorge transfer. DA-003.
- ACT-909: time the drift input for the marked bend of the track
  currently being ridden. DA-002.

### System Behaviour Genes

- SYS-1961: keep the provisional chain distinct from credited
  points through manual-supported contacts and settle successful
  lines. The supplementary recovery bounds checkpointed credit.
  DA-004, DA-006.
- SYS-1962: present a cleared track's score, elapsed time and
  optional checks independently. DA-005.

### Constraint Genes

No separate admission. Rail eligibility, supported take-off and
the conditions on the cleared course are already represented in
the action and objective boundaries.

### Information Genes

- INF-632: read elapsed time, credited points, pending additions,
  multiplier marker and the recent trick labels while moving.
  The live dare response updates independently. DA-002, DA-004.

### Objective Genes

- OBJ-364: cross the authored finish with the briefed time
  and score conditions and reach the Track Cleared report.
  DA-001, DA-005.

### Time Genes

- TIM-003: respond to approaching rail geometry during continuous
  forward movement while the in-run elapsed clock advances.
  DA-002–DA-005.

## Reproducible transitions

| From | Input or event | To | Evidence |
| --- | --- | --- | --- |
| 1-2-1 briefed, opening countdown active | Countdown ends | Live forward motion and elapsed readout; no credited points | DA-001–DA-002 |
| Running on current rail before a marked bend | Time the drift input | Continue along that bend; a qualifying drift can credit its dare | DA-002 |
| Supported train before the gorge transfer | Release the jump and direct the vehicle laterally | Airborne shift toward adjacent support and rail travel on that route | DA-003 |
| An eligible air trick in a pending line | Use a compatible manual at contact, then link the next trick | Pending chain continues while credited points can remain unchanged | DA-004 |
| Pending line in ordinary earlier sections | Complete and close the line normally | The credited total rises in the corroborating capture | DA-004 |
| Approaching the marked goal with the required result | Cross the finish | Track Cleared, then independently displayed score, time and dares | DA-005 |
| Crash or loss of support in the supplementary trace | In-run recovery | Earlier route segment and score return with a later elapsed time | DA-006 |

## Strategic and experiential structure

The neighboring route provides a timing decision before it
becomes a stunt opportunity. The player must reach compatible
support while the rail vehicle keeps moving. A manual makes
contact useful for linking the next air trick. The pending
readout and the settled total let the player tell whether
additional tricks remain unbanked.

## Replay and variation

Two recorded PlayStation runs clear with different points,
times and optional counts. One reaches six of seven. This
records variation among valid finished runs. The guide does
not claim medal persistence after closing or restarting the game.

## Adjacent systems and history

The standard stunt route combines forward rail travel with
trick-game linking. The early training stages also include
a scored practice where the clock counts down; 1-2-1 shows
elapsed time and an authored finish instead.

## Normalised genome

| Type | Stable genes | Role |
| --- | --- | --- |
| Action | ACT-500, ACT-797, ACT-908, ACT-909 | Link tricks, take off, choose adjacent support and drift on a curve |
| System Behaviour | SYS-1961, SYS-1962 | Stage pending score and report three distinct finished measures |
| Constraint | None | Preserve support and finish requirements in their action and objective boundaries |
| Information | INF-632 | Present elapsed time, banked points and current line during travel |
| Objective | OBJ-364 | Reach the timed, scored course finish |
| Time | TIM-003 | Intervene while rail motion and time advance |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `686` (`GAME-0001`–`GAME-0686`).
- Exact genome matches: none.
- Tied near matches: `GAME-0615` — Skate Story (`2 / 16 = 0.125000`).
- Supported combination subsets: none.
- Scan date: 2026-11-24.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
| --- | --- | --- | --- |
| [Skate Story (GAME-0615)](../s-z/skate-story.md) | ACT-797, TIM-003 | Both use a supported, held-and-released jump during live motion. Skate Story checks Ollies at four marked positions to open a portal. Denshattack! lets the airborne railcar select another track and closes the continuous route with separate score, time and optional results. | Near, `0.125000` |

## Taxonomy impact

The route distinguishes air switching from selecting a
connected on-track junction, and the timing of a single-rail
drift from building a release-charge tier. Its score graph
keeps pending and credited totals separate, with recovery
bounded by checkpoints. Three other definitions preserve
the independent result report, live display and the finish
conditions.

## Negative results

- A pending score increase does not immediately alter the white total.
- Rail contact during a manual need not close the chain.
- A Track Cleared report can show fewer than seven optional checks.
- The visible chain marker and recent scoreboard do not establish an exact scoring formula.
- The launch-window records do not establish an exact failure cutoff or balance tolerance.

## Delta summary

Nine genes, six newly admitted. An authored rail destination
and turn must be reached at speed while optional trick choices
change which points are still pending.

## New facts

- An airborne transfer has a different destination from a normal drift.
- A manual can carry a pending trick line through rail contact.
- Score, time and dares have separate finish receipts.
- Two independently labelled PlayStation captures clear with different values.

## Principles and design implications

Use the next bend, rail or gap to make the timing decision
readable before the train reaches it. Give optional stunt
and route-clear results independent feedback so the player
can understand both.

## Puzzle or game generation potential

Design an original elevated trolley course where a jump shifts
the vehicle to a parallel way over water. Let a short balanced
contact extend a pending line, with separate score, time and
optional route-mark results at the final platform.

## New genes

- ACT-908
- ACT-909
- INF-632
- OBJ-364
- SYS-1961
- SYS-1962

## New combinations

None admitted. All 274 verified combinations were checked as proper subsets.

## Taxonomy changes

[Taxonomy Change 433](../../../research/taxonomy-changes/TAXONOMY_CHANGE_433.md).

## New questions

- What exact minimum pair of time and score passes 1-2-1 on the same installed build?
- Which neutral contacts close a pending sequence immediately?
- Can the same checkpoint retain optional progress after a repeated crash in PS5?

## Next recommended game

Continue Selection 059 with `GAME-0688`, Lunar: Silver Star
Story Complete, on the original English PlayStation retail release.

## Why this game

The rail vehicle gives each airborne stunt an authored support
choice, and the finish still evaluates the resulting route and timing.
