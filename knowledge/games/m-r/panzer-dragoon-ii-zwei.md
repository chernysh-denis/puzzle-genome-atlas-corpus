---
game_id: GAME-0587
slug: panzer-dragoon-ii-zwei
game_title: Panzer Dragoon II Zwei
analysis_status: reviewed
reviewed: 2026-11-20
combination_ids: []
gene_ids:
  action:
    - ACT-161
    - ACT-562
    - ACT-613
    - ACT-690
    - ACT-691
  system:
    - SYS-215
    - SYS-707
    - SYS-1410
    - SYS-1411
    - SYS-1730
    - SYS-1731
  constraint:
    - CON-773
  information:
    - INF-299
    - INF-489
  objective:
    - OBJ-002
    - OBJ-288
  time:
    - TIM-003
---

# Game: Panzer Dragoon II Zwei

Use the [canonical vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
Steer an advancing dragon through a canyon fork, fight the encounters
on that branch and defeat the transport ship that awaits either route.

## Analysis scope

- Version / ruleset: English North American commercial Sega Saturn release
  from 1996, Sega product 81022. Reproduction target is ordinary solo
  NEW GAME with default controller bindings. Choose FULL Instruments to see
  the selected-route cue, scoring and boss countdown. This is a display
  option rather than an independent difficulty selection. The recorded
  left branch has a simpler HUD. Exact revision, pre-entry performance and
  ADEC rank in the recordings are unverified.
- Structured analysis target: PLAT-SEGA-SATURN.
  See [platform coverage](../../platforms/games.json).
- Entry: begin at the ordinary Episode 2 canyon entry following Episode 1.
  Ride Lagi on the advancing path. First pass the shared ground
  encounters. Use the forward view to place Lagi at the live canyon fork.
- Primary decision loop: rotate the attack view to follow radar threats, use
  a direct rider burst or hold, sweep and release the dragon's homing
  lasers, and save or spend the separate Berserk reserve on an automatic
  barrage. Take the left passage to fly over the drop and fight airborne
  ships, or the right passage to run below and fight through the outpost.
  Each choice supplies a different encounter sequence before the common
  transport ship and changes what the game counts for the result.
- Positive exit: survive the route, destroy the transport ship, read the
  destruction and progression results, and reach ordinary Episode 3
  control. Include the resulting form if awarded. Stop before analysing
  the first distinct forest decision.
- Negative exit: exhausting the blue life bar ends the attempt. The
  documented CONTINUE restarts the episode at its beginning. SAVE END
  and END are exits at the choice screen. The exact persisted save state
  and the outcome of a boss countdown reaching zero are outside this
  reconstruction.
- Included: forward course and bounded placement, active view sectors,
  targeted bursts and released homing locks, separate health and special
  reserves, windowed route commitment, airborne ships or ground outpost,
  boss vitality, score and result settlement, successor handoff.
- Excluded: demos, other regional executables, later remakes, later-route
  decisions, Pandora's Box, exact ADEC transitions, exact score formulas,
  complete form table, native timing, unlocked special forms and full campaign.
- Potential scoped module: Episode 4 water route with an additional physical
  fork and different successor encounter sets.
- Direct-play status: not conducted. The visually inspected North American
  booklet establishes the controls and retry rules. Attributed static
  frames from two stops of one NTSC-U-labelled recording corroborate
  both Episode 2 paths through Episode 3 entry. The recorded initial save,
  exact build and inputs between frames are unknown. The source video,
  executable and audio were not played.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
| --- | --- | --- | --- | --- | --- |
| PZ-001 | The released North American Saturn edition is Sega 81022. Episode 2 has a shared moving canyon entry after the first episode. | Observation | Corroborated | High | P1 pp. 6–8, P2, W1 9:30/10:00 and 56:10/56:20 |
| PZ-002 | Direction inputs place the body within the advancing corridor and aim the reticle. Shoulder buttons select 90-degree attack sectors, and the radar distinguishes the current sector from other threatened bearings. | Confirmed | Direct | High | P1 pp. 4–5, 7–9; R1; W1 57:20/59:20 |
| PZ-003 | Tap for the rider's direct fire. Hold and sweep to acquire legal targets and release to send homing lasers. A retained target mark precedes the attack. | Confirmed | Direct | High | P1 pp. 8, 11; R1; W1 56:50/59:50/63:50 |
| PZ-004 | At the physical fork, the left path leads off a ledge and into flight against airborne ships. The right path continues on the ground through a fortified outpost. Both converge on the transport boss. A completed split does not let the player turn back. | Observation | Corroborated | High | P1 p. 8; W1 11:10–15:30 vs 58:20–62:20; R1, R2 |
| PZ-005 | The green upper Berserk reserve permits an explicit automatic homing barrage against eligible targets until that reserve is spent. Successful ordinary homing hits refill the reserve. Blue life energy is separate. | Confirmed | Direct | High | P1 pp. 8–9, 11; P2; R1 |
| PZ-006 | Both paths fight the same transport with its own yellow vitality display. Boss-phase time is visible with FULL Instruments and affects a scoring bonus. The two sampled clears finish before expiry. | Observation | Corroborated | High | W1 15:30–17:30 and 62:20–64:20; P3; R3 |
| PZ-007 | The left run shows 91 of 91 destroyed, 100.0% and five total progression points. The right run shows 134 of 134 destroyed, 100.0% and four total progression points. These are observations, not fixed enemy totals for every run. | Observation | Corroborated | High | W1 17:40 / 64:30–64:40; P1 p. 10, R2 |
| PZ-008 | The results separate the shooting score from Clear, Route and Technical contributions. The chosen route and destruction proportion can affect progress toward a persistent change of dragon form and combat capabilities. | Observation | Corroborated | High | P1 p. 10; P2; W1 17:40 / 64:30; R1, R2 |
| PZ-009 | Receiving lethal damage ends the current attempt and exposes the documented Continue choice, which returns to Episode 2 entry. Save and exit or exit to title instead close the attempt. | Confirmed | Direct | High | P1 pp. 9–10 |
| PZ-010 | The transport fight closes into results and then the Episode 3 forest. Ordinary play resumes with the resulting dragon; W1 does not establish every internal retained field or its point threshold. | Observation | Corroborated | High | W1 17:40–18:50 and 64:30–65:40; P1 p. 10; R2 |

## Basic data

- Team Andromeda and Sega, North American Saturn, 1996. FAM-009 for
  threatening sectors and choice of attack before the opportunity passes.
  FAM-010 for the moving corridor and branch choices under live pressure.
- P1: [Sega's original North American instruction booklet](https://archive.org/details/Panzer_Dragoon_II_Zwei_1996_Sega_US),
  printed pp. 4–11. The default controls, instrument settings, life and special attack
  reserves, route cue, results, form and retry text were read. Printed
  pp. 6–11 were checked on the scans to resolve OCR errors. Its general
  claim that every episode forks is not needed for Episode 2.
- P2: [North American packaging, original box scan and product record](https://www.vgcollect.com/item/8059).
  Product 81022 and the features described on the commercial box.
  [Sega's Panzer Dragoon Orta booklet retrospective](https://manualzilla.com/doc/7437732/sega-panzer-dragoon-orta-instruction-manual)
  independently identifies routes, Berserk and dragon development as
  Zwei additions. The later booklet is evidence about the original,
  not the rules carrier.
- P3: [Developer OMAKE.TXT from the Japanese disc, translated transcription](https://panzerdragoonlegacy.com/literature/437-panzer-dragoon-ii-zwei-omake).
  Corroborates score bonuses, optional instruments and ADEC.
  No Japanese build, numerical coefficients or frame counts are
  transferred to the North American target.
- W1: [K4's NTSC-U-labelled longplay](https://www.youtube.com/watch?v=gwsrTlCDdyU).
  Static samples show entry and baseline fights at 9:30, 10:00, 10:30
  and 11:10. At 11:20–14:30 the dragon is airborne above the canyon with
  hovering armoured craft, and at 15:00–17:30 it confronts the transport
  near ground level. The result is visible at 17:40, the forest title at
  18:30 and ordinary forest action at 18:50. The second pass begins at
  56:10, stays below through the fortified encounters at 59:00–61:20,
  fights the transport at 62:20–64:20, shows its result at 64:30–64:40
  and the next live controls at 65:40. Timecodes are source locators.
  The comparison uses two paths in a single attributed recording,
  so it is paired evidence rather than two independent native trials.
- R1: [Geoffrey's firsthand Zwei review](https://panzerdragoonlegacy.com/literature/392-panzer-dragoon-ii-zwei-reviewed-by-geoffrey),
  gameplay section. Distinguishes body placement, view, both routes
  and the three attack commands.
- R2: [Kimimi's authored play and scoring review](https://kimimithegameeatingshemonster.com/2020/04/27/one-of-the-best-3d-shooting-games-available-presented-for-your-pleasure/).
  Explains route-exclusive counted enemies and separates the regular
  score from the three progression contributions.
- R3: [Franz the Stampede's scoring experiments](https://panzerdragoonlegacy.com/literature/348-panzer-dragoon-zwei-scoring-guide).
  Cross-checks the transport and scoring countdown. Exact formulas,
  ranking manipulations and native stopwatch measurements are outside scope.
- Sources accessed 2026-11-20.

## Mechanical decomposition

### Action Genes

- ACT-161 aims and commits the rider's direct burst at a reachable target.
  ACT-691 holds, sweeps and releases the dragon's selected target group
  (PZ-003).
- ACT-562 adjusts lateral position and, in flight, height within the
  advancing corridor. ACT-690 rotates the active attack sector without
  selecting a new longitudinal route (PZ-002).
- ACT-613 physically steers into a branch while moving. It transfers
  from Metal Slug 3's live world entrance, including route commitment
  without a separate map (PZ-004).

### System Behaviour Genes

- SYS-1410 advances each authored corridor independently of aim or
  retrograde player control. The optional physical fork is represented
  separately. SYS-215 resolves both sides' live damage (PZ-002–PZ-006).
- SYS-1411 turns the held set into a released homing volley. SYS-707
  represents restoring the special resource through successful regular
  attacks, with the reserve's drain semantics in SYS-1730 (PZ-003, PZ-005).
- SYS-1730 starts a repeated, automatically acquired barrage and drains
  the continuous special reserve to exhaustion. SYS-1731 converts the
  three result contributions into persistent dragon development
  (PZ-005, PZ-007–PZ-010).

### Constraint Genes

- CON-773 requires positive current life energy. Zero stops the current
  attempt and places the player at the retry or exit choice (PZ-009).

### Information Genes

- INF-489 exposes the reticle, pending locks and current radar sectors.
  FULL adds danger information and confirms a committed route. Separate
  live indicators show dragon life, special power and boss life (PZ-002,
  PZ-005, PZ-006).
- INF-299 exposes the counted destruction and contribution categories at
  settlement, separate from live combat and optional score (PZ-007, PZ-008).

### Objective Genes

- OBJ-002 covers optional accumulation of shooting score. OBJ-288
  requires the complete encounter route through boss defeat, credited
  closeout and successor control. Clearing does not require 100%
  destruction, a specified route, a timer score or a particular form
  (PZ-004, PZ-006–PZ-010).

### Time Genes

- TIM-003 covers live movement and attacks during aiming, turning,
  target acquisition and fork selection. The score countdown remains
  a boss parameter rather than an inferred forced defeat (PZ-002, PZ-004, PZ-006).

## Reproducible transitions

| Initial state | Intervention | Discriminating result | Evidence |
| --- | --- | --- | --- |
| Shared ground encounters before the branch | Aim and tap fire; hold and sweep on the next targets, then release | Direct fire precedes the released homing group without waiting for the other target set. Threats and route movement continue during selection. | PZ-002, PZ-003 |
| Threat lies beside the current attack view | Press the shoulder for that sector | Aim switches one quarter turn while the course still advances. Radar and reticle now address a different approach. | PZ-002 |
| After the common ravine, approaching the fork in forward view | Steer into the left passage before passing the split | Lagi leaves the ledge, enters aerial movement and encounters the airborne sequence. The later outpost is absent. | PZ-004 |
| Same fork in a separate attempt | Stay with the right passage | The forward route continues below through the defended outpost. The air sequence is absent. Both branches reach the transport. | PZ-004, PZ-006 |
| Eligible target, depleted or partly spent special reserve | Land ordinary homing hits; activate Berserk once ready | The independent reserve refills. One activation repeatedly acquires eligible targets and spends the reserve until empty. | PZ-003, PZ-005 |
| Branch encounters completed, transport still active | Direct fire or released locks at targetable ship parts, while evading | Attack resolves against the boss and separate player vitality. With FULL, the elapsed boss time affects the remaining score opportunity. | PZ-006, PZ-009 |
| Dragon's blue life reserve becomes empty | Choose CONTINUE or exit | A failed attempt ends; CONTINUE returns to the episode opening, and a recorded boss clear is absent. | PZ-009 |
| Transport defeated on either branch | Let the results and transition settle | Results retain the route and counted destruction contributions distinct from shooting score. The dragon then enters ordinary Episode 3 play. | PZ-007, PZ-008, PZ-010 |

## Strategic and experiential structure

Turning to a threat may save the opportunity to hit it, but the live
fork is easiest to read from the front. Charging a multi-target attack
pays off only if the targets are still eligible when released. Spending
Berserk on a dense wave can preserve health, at the cost of facing the
next wave or the boss without that reserve. A left-route bonus may
improve form progression even when another route gives a greater
shooting score.

## Replay and variation

The inspected runs both show full counted destruction, but different
enemy totals, route contributions and shooting scores. The difference
in available enemies is visible in the encounter sets. Exact counts
and differences in score are not attributed only to route: enemy
appearances and scoring can also depend on play and ADEC. Weapon
order, timing, damage and retry usage can vary even on one route.

## Adjacent systems and history

The first Panzer Dragoon shares the active attack sectors, target
acquisition and authored flight handoff. Its credited settlement
rewards retries. Zwei adds a world-space branch and settles
progression into dragon form. Rez's Overdrive debits an item
charge and is distinct from the continuously drained Berserk meter.

## Normalised genome

| Type | Active gene IDs | Carrier parameters |
| --- | --- | --- |
| Action | ACT-161, ACT-562, ACT-613, ACT-690, ACT-691 | rider burst, bounded placement, live branch, quarter turn, hold and release |
| System Behaviour | SYS-215, SYS-707, SYS-1410, SYS-1411, SYS-1730, SYS-1731 | live damage, special refill and drain, authored advance, homing, form progression |
| Constraint | CON-773 | positive life required to continue |
| Information | INF-299, INF-489 | sector radar, targeting marks, separate result contributions |
| Objective | OBJ-002, OBJ-288 | optional score and transport clear through next episode |
| Time | TIM-003 | live progression while aiming and steering |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `586` (`GAME-0001`–`GAME-0586`).
- Exact genome matches: none.
- Tied near matches: `GAME-0505` — Panzer Dragoon (`11 / 25 = 0.440000`).
- Supported combination subsets: none.
- Scan date: 2026-11-20.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
| --- | --- | --- | --- |
| GAME-0505 Panzer Dragoon | ACT-161, ACT-562, ACT-690, ACT-691, INF-489, OBJ-002, OBJ-288, SYS-1410, SYS-1411, SYS-215, TIM-003 | Zwei commits one of two encounters in world space, spends its separate special reserve and carries the episode result into form. The first game has a fixed path here and awards retry credits. | `11 / 25 = 0.440000` |

### Preserved research notes

- New genes: SYS-1730 and SYS-1731.
- Classification result: New gene.

## Taxonomy impact

- [TAXONOMY_CHANGE_333](../../../research/taxonomy-changes/TAXONOMY_CHANGE_333.md)
  separates a draining special barrage from finite-charge Overdrive and
  distinguishes results that change the controlled form from score alone.

## Negative results

- CON-782 requires a fixed acquisition cap. A single fixed number across
  forms is not attributed to Zwei. SYS-1412's specific body-following
  restriction is not inferred from the first game's controls.
- SYS-1413 and SYS-1415 carry retry-stock awards in the first game.
  The sequel's result tallies and documented Continue do not establish
  those awards. A retry credit cost is not asserted.
- Exact boss countdown expiry, all ADEC thresholds, flight response,
  defence during Berserk and the full dragon form table remain untested.
- No new industry claim, source screenshot or exact reproduction of game
  assets enters the corpus.

## Delta summary

## New facts

- [Observation | Corroborated | High] A live choice of canyon passage
  changes the flight or ground encounter set and the route result before
  the same transport boss and successor episode.

## New genes

- [Observation | Corroborated | Medium] Two additions in TAXONOMY_CHANGE_333.

## New combinations

- [Observation | Corroborated | High] No new verified combination
  proposed. Existing subsets are listed in the comparison.

## Taxonomy changes

- [Observation | Corroborated | Medium] Earlier definitions and
  signatures are retained.

## New questions

- A controlled repeat could separate route, carried form and ADEC
  contributions to enemy counts. Independently test countdown expiry.

## Next recommended game

- [Hypothesis | Limited | Medium] GAME-0588, Neva on Nintendo Switch.
  Bound the companion's authored traversal and protection decisions
  to one complete release episode.
- Optimisation criterion: contrast an automatically advancing attack
  corridor with responsive traversal and companion decision timing.

## Why this game

- [Hypothesis | Limited | Medium] One paired fork followed by a shared
  boss provides a tractable route and performance counterfactual.
