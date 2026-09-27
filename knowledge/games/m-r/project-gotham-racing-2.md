---
game_id: GAME-0420
slug: project-gotham-racing-2
game_title: Project Gotham Racing 2
analysis_status: reviewed
reviewed: 2026-09-27
combination_ids:
  - COMB-0215
gene_ids:
  action:
    - ACT-290
    - ACT-292
    - ACT-293
  system:
    - SYS-320
    - SYS-515
    - SYS-516
    - SYS-519
    - SYS-1114
  constraint:
    - CON-438
  information:
    - INF-204
    - INF-205
    - INF-206
    - INF-208
    - INF-413
  objective:
    - OBJ-134
  time:
    - TIM-003
---

# Game: Project Gotham Racing 2 — first Compact Sports street race

Use the canonical [vocabulary and genome rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). The Seat Leon, Florence route, Novice setting and approximate two-second Kudos window are parameters of this packet, not new universal gene names.

## Analysis scope

- Version / ruleset: original English 2003 Xbox retail *Project Gotham Racing 2*, offline Kudos World Series, Compact Sports, first Street Race on Duomo 2 in Florence, using the Seat Leon Cupra R and Novice difficulty. The printed Microsoft/Bizarre manual supplies the rules; the licensed Prima guide identifies this route, car and two-lap shape. Exact disc revision was not inspected.
- Structured analysis target: `PLAT-XBOX` in [`knowledge/platforms/games.json`](../../platforms/games.json).
- Primary decision loop: read the visible road, position, lap, speed and separate Kudos Stash/Bank; accelerate, steer, brake or handbrake the compact car to pass rivals on the two-lap circuit. A clean line, slide, draft or overtake can add Style Kudos to a short-lived stash; another eligible manoeuvre before banking yields a combo, while a cautious line can better protect position. After the valid finish, place and style contribute distinct result components.
- Entry and exit: begin with an untouched offline profile at the unlocked Compact Sports Street Race 1 pre-entry surface; choose the Seat Leon and Novice, then start. The positive packet ends after a valid first-place finish, the Novice event medal and Kudos result are retained, and control returns to the series. A lower finish or quit does not satisfy this first-place analytical target, even if some style points were earned. The first-place target is deliberately stricter than an unmeasured minimum event-completion place.
- Included: one car and one fixed Street Race route; opponent difficulty; direct car control and collision; rival placement; two ordered laps; live race position; eligible line, slide, draft and pass Style Kudos; short Stash-to-Bank timing and combo; separately calculated finish/completion bonus, medal and retained event result. No exact points or undocumented Novice rival pace is claimed.
- Excluded: the other Compact Sports events and later Car Series, car purchases or rank-token spending, Arcade Racing, Time Attack (which awards no Style Kudos), Instant Action, ghost downloads, Xbox Live, downloadable content, later PGR titles, damage repair, vehicle tuning, precise scoring formulae and all race replays beyond this first result.
- Potential scoped modules: one Cone Challenge focused on chaining, a measured higher-difficulty Street Race, a rank-to-token car unlock, or a lawful offline replay comparing best-event Kudos.
- Direct-play status: no disc, console, controller trace, screenshot, video or audio was inspected. The reconstruction is source-bounded by the contemporary publisher manual and licensed strategy guide; exact disc revision, Novice field timings and point awards remain unmeasured.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `PGR2-001` | The original Xbox manual separates offline Kudos World Series from Arcade, Time Attack and online ranks. | Confirmed | Direct | High | P1 |
| `PGR2-002` | The first Compact Sports Street Race uses Duomo 2 in Florence, a Seat Leon Cupra R route and two laps. | Confirmed | Direct | High | P2 |
| `PGR2-003` | Street Race pits the driver against rivals while still awarding Style Kudos; an overtake and clean racing line are eligible manoeuvres. | Confirmed | Direct | High | P1, P2 |
| `PGR2-004` | Eligible moves first enter Kudos Stash, transfer to Bank after about two seconds, and another move within that interval can earn a combo bonus. | Confirmed | Direct | High | P1, P2 |
| `PGR2-005` | Completing a Kudos World Series event at a selected difficulty can award a matching medal and a difficulty-dependent completion bonus; only an event's all-time best Kudos performance contributes to the running total. | Confirmed | Direct | High | P1, P2 |
| `PGR2-006` | The in-race display separates current position, lap, speed, Kudos Stash, Bank and combo feedback. | Confirmed | Direct | High | P1 |
| `PGR2-007` | Exact Novice rival pacing, point coefficients, collision penalties and retail-disc revision were not directly measured. | Observation | Limited | High | P1, P2 |

## Basic data

- Release / origin: Bizarre Creations' 2003 original Xbox *Project Gotham Racing 2*, published by Microsoft Game Studios. The packet uses the original English offline retail rules, not an Xbox 360 sequel or modern online restoration.
- Platform or physical form: original Xbox disc, offline single-player Kudos World Series.
- Mechanical family: real-time system pressure (`FAM-010`): the road and autonomous rivals continue moving while the driver trades pace, overtaking position and style opportunities.
- Sources accessed 2026-09-27:
  - **P1** — [Microsoft/Bizarre original Xbox instruction manual, text preservation](https://manualzz.com/doc/25186554/microsoft-project-gotham-racing-2-video-game-user-manual), printed pp. 2–4, 6, 10–14: mode separation, Stash/Bank/Combo, style and completion awards, screen fields, World Series difficulties and medals. This is a transcription of the publisher manual, not a later gameplay guide.
  - **P2** — [Prima's licensed official strategy guide](https://ogxbox.co.uk/media/com_eshop/attachments/Project_Gotham_Racing_2_Strategy_Guide_Book.pdf), printed pp. 6–10: first Compact Sports Street Race, Duomo 2, Seat Leon, two laps, passes, slides and the distinct completion versus in-race Kudos. It is used as a rules-and-route reference, not as an image source.
- Claim IDs: `PGR2-001`–`PGR2-007`.

## Mechanical decomposition

### Action Genes

- `ACT-290`: steer, accelerate, brake or handbrake the assigned Seat Leon during this event.
- `ACT-292`: commit Novice opponent difficulty before the race; no cross-title driving-assist claim is imported.
- `ACT-293`: enter the first available Compact Sports Street Race and its fixed Duomo 2 course.
- Claim IDs: `PGR2-002`, `PGR2-003`.

### System Behaviour Genes

- `SYS-320`: integrate occupied car motion, grip, slides and physical contact.
- `SYS-515`: advance a difficulty-scaled rival field; exact Novice pace and competitor count are not fixed by this packet.
- `SYS-516`: classify two ordered laps and the valid finishing position.
- New `SYS-1114`: award eligible driving-style events into Kudos Stash, transfer it to Bank after the short window and amplify a linked sequence with a combo bonus. A fast finish is not itself a Style Kudos action.
- `SYS-519`: settle the valid first-place result, matching difficulty medal, completion bonus and retained event progress. Only the best-event Kudos contribution is retained in the longer World Series total.
- Resolution order: commit mode/car/difficulty → run car and rivals → evaluate driving manoeuvres for Style Kudos → bank or chain the stash → validate both laps and finish → calculate distinct position/completion award → display and retain the result.
- Claim IDs: `PGR2-002`–`PGR2-007`.

### Constraint Genes

- `CON-438`: the result requires both authored laps and a valid final crossing, not merely being ahead on the first lap.
- Scarce resources: space and time before the finish, speed through each corner and the short chance to chain eligible Kudos moves. No fuel inventory or repair economy is admitted.
- Claim IDs: `PGR2-002`, `PGR2-004`.

### Information Genes

- `INF-204`: speed, gear, road and circuit map make the next braking or line choice legible.
- `INF-205`: current place, lap and nearby rivals expose the racing objective.
- `INF-206`: the event surface exposes the selected World Series race and difficulty.
- New `INF-413`: the live display distinguishes temporary Kudos Stash, banked Kudos and combo feedback from race place.
- `INF-208`: the post-race surface exposes the classified finish and credited World Series result.
- Claim IDs: `PGR2-005`–`PGR2-007`.

### Objective and Time Genes

- `OBJ-134`: win the bounded rival race in first place and retain its disclosed event result; an optional Style Kudos gain alone is not a win.
- `TIM-003`: driving, rivals and the approximately two-second Kudos transfer progress in real time while steering decisions remain live.
- Claim IDs: `PGR2-003`–`PGR2-006`.

## Reproducible transitions

| Before | Action | Bounded resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| First Compact Sports Street Race is available | Select Seat Leon, Novice and start Duomo 2 | A fixed two-lap route loads against rivals | exact event boundary | `PGR2-002` |
| Grid releases | Accelerate and steer inside the first bend | Relative position changes while grip and contact resolve | position is earned through driving | `PGR2-002`, `PGR2-003` |
| An eligible pass or slide occurs | Continue driving | Style Kudos enter Stash, separate from current place | style is not the finish predicate | `PGR2-003`, `PGR2-004` |
| Kudos remain in Stash | Perform another eligible manoeuvre before transfer, or wait | A linked move adds a Combo Bonus, or the stash moves to Bank after about two seconds | timed style chain | `PGR2-004` |
| First valid circuit completed | Cross the lap line | Lap advances; no event result is final yet | ordered two-lap requirement | `PGR2-002` |
| Second lap completed in first place | Cross the valid finish | Place and Style Kudos are shown as distinct contributors; the Novice medal and completion award settle | terminal win and retained result | `PGR2-005`, `PGR2-006` |
| Finish is below first, or player quits | End the attempt | The stricter first-place analytical objective is not met, regardless of accrued style | objective is not score-only | `PGR2-005` |

## Strategic and experiential structure

- Local decision: take a conservative fast line for position, or expose speed and grip to a controlled slide or close overtake that may add Style Kudos.
- Medium-term decision: chain eligible moves before the Stash banks without sacrificing a clean next corner or a pass opportunity.
- Long-term result: one finite race produces both a classified finishing place and a separate Kudos breakdown that can contribute to the persistent World Series rank.

## Replay and variation

The route and two laps are fixed; traffic interactions and player manoeuvres vary. A later replay may improve the event's best Kudos result, but is outside this first-entry packet. No deterministic rival line, exact Novice score or automatic gain from every slide is asserted.

## Adjacent systems and history

*Need for Speed Underground* also uses a two-lap rival race and retained reward, but its opening Circuit does not make a short-lived style stash part of the accepted ruleset. *Crazy Taxi* earns trick tips during a paid passenger trip; PGR 2's free-standing Street Race separates live place from style bank and completion bonus. The first *Project Gotham Racing* and later PGR games are not substituted for the original sequel's manual.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-290`, `ACT-292`, `ACT-293` | car control, Novice, event choice |
| System Behaviour | `SYS-320`, `SYS-515`, `SYS-516`, `SYS-519`, `SYS-1114` | car/rival movement, ordered finish, Kudos transfer and settlement |
| Constraint | `CON-438` | required two laps |
| Information | `INF-204`, `INF-205`, `INF-206`, `INF-208`, `INF-413` | road, place, event, result and separate Kudos state |
| Objective | `OBJ-134` | first-place retained race result |
| Time | `TIM-003` | live race and short Stash window |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `419` (`GAME-0001`–`GAME-0419`).
- Exact genome matches: none.
- Tied near matches: `GAME-0217` — Need for Speed Underground (`14 / 16 = 0.875000`).
- Supported combination subsets: `COMB-0215`.
- Scan date: 2026-09-27.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|
| Need for Speed Underground (`GAME-0217`) | Fourteen shared finite driving-event genes for car control, rivals, ordered laps, HUD, first-place result and real-time input | PGR 2 additionally keeps a short-lived, visibly separate Style Kudos Stash and Bank (`SYS-1114`, `INF-413`), allowing a linked-move bonus while place still decides this packet's win. The Underground opening Circuit lacks that admitted score layer | Near, `0.875000` |

## Taxonomy impact

[`TAXONOMY_CHANGE_158`](../../../research/taxonomy-changes/TAXONOMY_CHANGE_158.md) admits the distinct Stash/Bank scoring and visible temporary score information. Earlier signatures and verified combinations remain unchanged.

## Negative results

- `SYS-1103` rejected: Crazy Taxi's collision-breakable tips occur inside a paid fare; they are not a free-standing World Series style stash banked on a short timer.
- `OBJ-134` retained rather than inventing a score-only goal: the accepted packet requires first place and retained event result. A player can earn style without meeting it.
- Exact Novice rival pace, scoring coefficients and disc revision remain unknown; no Xbox Live rule or Time Attack style award is imported.

## Delta summary

The first Duomo 2 street race makes position and style simultaneous but distinct. A driver can take a fast inside line to win place while chaining a pass and slide to build Kudos; the short stash window affects style scoring, not the two-lap finish order.

## New facts

- [Confirmed | Direct | High] The publisher manual explicitly separates in-race Style Kudos from event-completion bonuses and shows a temporary Stash and Bank (`PGR2-004`–`PGR2-006`).

## New genes

- [Observation | Direct | High] `SYS-1114` and `INF-413` distinguish transient, combo-eligible Kudos from retained score and from visible race place.

## New combinations

- [Observation | Direct | High] No new combination is created. `COMB-0215` transfers as a proper subset for a bounded multi-lap rival win with retained career reward; the optional Kudos Stash and Bank stay outside that shared set.

## Taxonomy changes

- [Observation | Direct | High] `TAXONOMY_CHANGE_158` records two new typed score boundaries and rejects transferring Crazy Taxi fare tips.

## New questions

- What exact Novice opponent pace, point coefficients and collision effects reproduce the first Duomo 2 Street Race on a named disc revision?
- Under direct play, what is the minimum place accepted as event completion on Novice, distinct from this stricter first-place analytical target?

## Next recommended game

- [Hypothesis | Limited | Medium] `GAME-0421` *The Incredible Machine* on DOS PC, after this unit's validation, local commit and Goal stop window.
- Optimisation criterion: move from live position/style racing to a player-built physical contraption with a different action and timing structure.
- Backlog impact: preserve approved `GAME-0421`–`GAME-0432` order; do not start another subject in this unit.

## Why this game

- [Hypothesis | Direct | Medium] The publisher's explicit Stash/Bank/Combo distinction tests a scoring boundary absent from ordinary place-based races while retaining a familiar two-lap event for comparison.
