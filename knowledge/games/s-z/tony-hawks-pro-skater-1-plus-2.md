---
game_id: GAME-0365
slug: tony-hawks-pro-skater-1-plus-2
game_title: Tony Hawk’s Pro Skater 1 + 2
analysis_status: reviewed
reviewed: 2026-09-23
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-500
    - ACT-501
  system:
    - SYS-974
    - SYS-975
    - SYS-998
    - SYS-999
  constraint:
    - CON-665
    - CON-666
  information:
    - INF-374
  objective:
    - OBJ-002
    - OBJ-211
  time:
    - TIM-003
---

# Game: Tony Hawk's Pro Skater 1 + 2

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Warehouse, Tour,
Manual, Revert, S-K-A-T-E, the skateboard and exact score thresholds are
carrier or goal parameters, not extra genes.

## Analysis scope

- Version / ruleset: licensed English native PlayStation 5 application from
  the *Tony Hawk's Pro Skater 1 + 2 – Cross-Gen Deluxe Bundle* (2021), using
  default modern moveset and no gameplay assists. The separately listed
  standard PlayStation Store edition is PS4-only; the PS5 SKU is the Bundle.
  Bonus outfits and bonus skater are in the product but outside this packet.
- Structured analysis target: PS5 SKU `UP0002-PPSA02176_00-TH12RTHEGAME0001`
  on `PLAT-PLAYSTATION-5` as recorded in
  [`knowledge/platforms/games.json`](../../platforms/games.json).
- Primary decision loop: choose a route through the Warehouse; steer and
  ollie into air, a rail or a manual; select tricks, spins and stance while
  correcting balance; decide whether to land and bank a connected score or
  continue it at bail risk; cross score, collectible, object or gap goal
  conditions before the two-minute Tour clock ends; inspect retained goals
  and any unfinished goals for a possible next run.
- Entry: a fresh PS5 Tour profile and default skater select the THPS1
  Warehouse goal-based park, before its first two-minute run starts. No
  completed Warehouse goals or assists are carried into this test.
- Positive terminal: the first two-minute Warehouse Tour run settles after
  at least one credited park goal; its completed-goal set remains in Tour
  progress. This does not require all Warehouse goals, unlocking School or
  finishing either Tour.
- Negative terminal: the same run expires with no park goal credited. A bail
  loses its current unbanked trick chain but not score already landed in an
  earlier chain; it is not a game-over state.
- Reproducible route: first complete one modest score goal by linking an air
  trick to a rail grind and a grounded manual, then land while the balance
  indicator remains valid; cross a visible object or letter marker separately
  if time permits; let the clock expire and inspect the credited goal set.
  Branch: repeat the same trick enough to lower its value, then vary trick,
  spin or stance and compare score behaviour. Another branch bails before a
  landing and checks that this chain is not banked while prior score remains.
- Included: ordinary free steering and ollie; contextual flip, grab, grind,
  manual and revert; rail and wall attachment; connected tricks; active
  manual/rail balance and bail; rotation, stance, gap and repetition effects
  on score; visible current trick, balance and remaining time; Warehouse's
  score, single-combo, S-K-A-T-E, hydrant, box, gap and secret-tape goals;
  Tour credit retained across the first run; two-minute run settlement.
- Excluded: PS4-only standard SKU rules as the target; Cross-Gen Deluxe bonus
  cosmetics and Ripper; character stat-point spending, other parks and Tours,
  competitions, full park clearance, Speed Runs, Free Skate, Single Session,
  multiplayer, leaderboards, Create-a-Park, optional challenges, legacy
  movesets, assists, exact hidden score coefficients and precision physics.
- Potential scoped modules: stat-point upgrades and per-skater collection;
  multi-run Warehouse clearance and School unlocking; high-score leaderboards;
  direct PS5 executable observation of end-of-clock and active-combo ordering.
- Direct-play status: no PS5 console, licence, save, executable, controller
  trace, screenshot, video or audio was obtained or inspected. Publisher
  controls, modes and scoring guidance are direct documentary evidence;
  Warehouse-specific goal details and two-minute timer are corroborated by a
  written independent guide. No achieved in-game result is claimed.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `THPS-001` | The PS5 application is sold as the Cross-Gen Deluxe Bundle, distinct from the PS4 standard listing | Confirmed | Direct | High | P1, P2 |
| `THPS-002` | Tours supplies goal-based parks including Warehouse; Free Skate lacks goals and Speed Runs reset them | Confirmed | Direct | High | P3 |
| `THPS-003` | Default controls support steering, ollie, flip, grab, grind, manual, wall ride, spin and stance change | Confirmed | Direct | High | P4, P5 |
| `THPS-004` | Connected tricks, gaps, spins, stance and repeated-trick decay affect score | Confirmed | Direct | High | P6 |
| `THPS-005` | Balance meters and ordinary rail/manual balance are real conditions that assists can suppress | Observation | Corroborated | Medium | P5, P4 |
| `THPS-006` | Warehouse has a two-minute goal window with score, collection, object and gap tasks; incomplete tasks can be pursued in another Tour run | Observation | Corroborated | Medium | P3, S1 |
| `THPS-007` | A bail breaks an unbanked chain without erasing earlier landed score | Observation | Limited | Medium | P6, P5 |

## Basic data

- Release / origin: Vicarious Visions' remade 2020 *Tony Hawk's Pro Skater 1
  \+ 2* reached native PS5 on 2021-03-26. The PS5 Bundle contains extras,
  which are not a reason to import extra mechanics into Warehouse.
- Platform or physical form: licensed PS5 digital application and controller;
  the structured target above, not an inferred equivalence to every release.
- Puzzle family: `FAM-010` real-time system pressure; this packet joins an
  actively maintained trick chain to a fixed clock and independent goals.
- Primary sources: **[P1]** [PlayStation Store PS5 Cross-Gen Deluxe
  Bundle](https://store.playstation.com/en-us/product/UP0002-PPSA02176_00-TH12RTHEGAME0001);
  **[P2]** [PlayStation announcement of native PS5
  release](https://blog.playstation.com/2021/02/23/tony-hawks-pro-skater-1-2-coming-to-ps5-on-march-26/);
  **[P3]** [Activision Tours](https://support.activision.com/tony-hawks-pro-skater-1-2/articles/the-tony-hawks-pro-skater-1-2-tours);
  **[P4]** [Activision Controls and Tricks](https://support.activision.com/tony-hawks-pro-skater-1-2/articles/controls-and-tricks-in-tony-hawks-pro-skater-1-2);
  **[P5]** [Activision Accessibility](https://support.activision.com/tony-hawks-pro-skater-1-2/articles/tony-hawks-pro-skater-1-2-accessibility);
  **[P6]** [Activision Scoring and Combos](https://support.activision.com/tony-hawks-pro-skater-1-2/articles/tony-hawks-pro-skater-1-2-scoring-and-combos).
- Secondary source: **[S1]** [Push Square's Warehouse goals and gap
  guide](https://www.pushsquare.com/guides/tony-hawks-pro-skater-1-plus-2-warehouse-all-park-goals-gaps-and-challenges),
  used for the explicit timer and local goal examples, not to override P3.
- Claim IDs: `THPS-001`–`THPS-007`.

## Mechanical decomposition

### Action Genes

- `ACT-008` moves the skater through a continuous park; it does not itself
  classify a trick.
- `ACT-500` selects a contextual trick or transfer using the current motion
  and contact state. Flip, grab, grind, Manual and Revert are command families,
  not separate genes per named trick.
- `ACT-501` corrects live rail/manual balance to preserve the current line.
- Claim IDs: `THPS-003`, `THPS-005`.

### System Behaviour Genes

- `SYS-974` carries a compatible rail or wall contact. `SYS-975` accumulates
  a connected, breakable traversal trick chain.
- `SYS-998` changes trick value with spin, stance, gap and repeat history;
  exact coefficients are not claimed. `SYS-999` independently credits
  Warehouse score, collection, object and gap goals to retained Tour progress.
- Resolution order: command/route → contact and trick → provisional chain and
  score modifiers → balance or landing/bail → banked score and eligible goal
  credit → clock settlement → inspect retained goal set.
- Claim IDs: `THPS-002`–`THPS-007`.

### Constraint Genes

- `CON-665` restricts sustained unassisted grinds/manuals by live balance.
  A bail breaks the current line, not the entire session.
- `CON-666` ends the run at the two-minute boundary while preserving
  independently earned goals. This is not `CON-068`'s all-or-nothing failure.
- Scarce strategic resource: remaining seconds and a valid unbanked chain,
  not limited trick buttons or consumable skateboards.
- Claim IDs: `THPS-005`–`THPS-007`.

### Information Genes

- `INF-374` joins provisional trick string and score, balance indicator,
  remaining run time and Tour park goals in the default presentation.
- Claim IDs: `THPS-002`, `THPS-005`, `THPS-006`.

### Objective Genes

- `OBJ-002` encourages a larger settled score. `OBJ-211` requires at least
  one credited Warehouse goal by this run's end; it does not require full
  park or Tour completion.
- Claim IDs: `THPS-002`, `THPS-004`, `THPS-006`.

### Time Genes

- `TIM-003` covers uninterrupted movement, trick entry, balance and clock
  advance during a live run. `CON-666` owns the distinct two-minute expiry.
- Claim IDs: `THPS-003`, `THPS-005`, `THPS-006`.

## Reproducible transitions

| Before | Action | Deterministic rule-level resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Fresh Warehouse Tour run | Steer and ollie into a suitable rail with a grind command | The skater enters a rail-bound moving trick if contact is eligible | Contextual control and rail carriage | `THPS-003` |
| Connected air trick and rail grind | Enter a manual before fully settling the line | A valid ground-contact transfer continues provisional combo scoring | Chain transfer is not a new session | `THPS-003`, `THPS-004` |
| Sustained grind or manual with exposed balance | Correct within the admissible range, then leave and land | The connected score can settle; uncorrected excursion can bail and forfeit the current unbanked chain | Live balance boundary | `THPS-005`, `THPS-007` |
| One trick has already been repeated | Repeat it again, then try a different trick, spin or switch stance | Repeat lowers that trick's contribution; changed context can improve the alternative line | Score is not a fixed per-button table | `THPS-004` |
| Score and local object goals remain available | Land enough points or contact a designated Warehouse object | Each satisfied predicate receives its own park-goal credit | Multiple goal kinds settle independently | `THPS-002`, `THPS-006` |
| Countdown reaches zero with one goal credited and others incomplete | Let the first Tour run settle | The run ends, credited goals remain, and unfinished goals can be attempted later | Partial retained settlement | `THPS-006` |

## Strategic and experiential structure

- Local decision: extend the current trick line through a gap, grind or manual,
  or land early to bank a smaller but safer score.
- Medium-term planning: route between score opportunities and scattered
  goal targets while the same two-minute clock advances.
- Long-term structure: retain completed Warehouse goals for later Tour runs;
  School and full completion are outside this first-run packet.
- Common heuristic: diversify tricks and use spin or switch stance rather
  than repeat one low-value move; leave a risky balance state before bailing.
- Failure attribution: an exposed balance error or missed target can explain
  a lost line or goal, but hidden score coefficients and unseen future route
  timing are not reverse-engineered here.
- Player-trust factors: displayed trick, balance, time and goal state expose
  the main tradeoff; exact physics, arithmetic and last-frame ordering are
  not directly observed.
- Claim IDs: `THPS-002`–`THPS-007`.

## Replay and variation

- What changes between sessions: route, chosen tricks, spin, stance, balance
  correction, bails, banked score and subset of goals credited.
- Randomness or procedural generation: none is claimed for the authored
  Warehouse geometry or declared goal list in this packet.
- Multiple viable strategies: prioritise a safe score threshold, a dispersed
  collectible route or a gap/object target; no unique optimal run is asserted.
- Typical replay motive: pursue unfinished park goals after a partial first
  run rather than restart the entire Tour.
- Claim IDs: `THPS-002`–`THPS-007`.

## Adjacent systems and history

- The original 1999 and 2000 games supply the park lineage, but this record
  analyses the remake's default moveset, which includes later-series tricks.
- Jet Set Radio shares `SYS-974` and `SYS-975`: rail/wall motion and a
  breakable traversal-score line. It does not share Warehouse's balanced
  Manual/Revert transfers, repeat/stance scoring or retained multi-goal Tour.
- Free Skate, Single Session and Speed Runs are explicit separate modes; the
  publisher says Free Skate lacks Tour goals and Speed Runs reset them.
- Claim IDs: `THPS-002`–`THPS-006`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-500`, `ACT-501` | movement, contextual trick, balance correction |
| System Behaviour | `SYS-974`, `SYS-975`, `SYS-998`, `SYS-999` | rail/wall contact, connected score, modifiers, Tour goals |
| Constraint | `CON-665`, `CON-666` | live balance and timed partial settlement |
| Information | `INF-374` | trick, balance, clock and goals |
| Objective | `OBJ-002`, `OBJ-211` | maximise score and retain a local goal |
| Time | `TIM-003` | real-time input and progression |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `364` (`GAME-0001`–`GAME-0364`).
- Exact genome matches: none.
- Tied near matches: `GAME-0350` — Jet Set Radio (`5 / 26 = 0.192308`).
- Supported combination subsets: none.
- Scan date: 2026-09-23.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0350` — Jet Set Radio | `ACT-008`, `SYS-974`, `SYS-975`, `OBJ-002`, `TIM-003` | Both skate directly, attach to rails or walls, build breakable traversal-score chains and act live. Jet Set Radio makes finite spray and all required graffiti the mission bottleneck under pursuit. Warehouse instead selects contextual board tricks, maintains manual/rail balance, modifies score by spin/stance/repetition and keeps independent park goals across two-minute runs | Near, `5 / 26 = 0.192308` |

## Taxonomy impact

- Add `ACT-500`, `ACT-501`, `SYS-998`, `SYS-999`, `CON-665`, `CON-666`,
  `INF-374` and `OBJ-211` under `TAXONOMY_CHANGE_104`.
- Reuse `ACT-008`, `SYS-974`, `SYS-975`, `OBJ-002` and `TIM-003` without
  broadening any earlier signature.
- Add no combination without a verified recurring proper subset.

## Negative results

- `CON-068` is rejected: a two-minute Warehouse Tour run ends with partial
  park-goal credit instead of making all unfinished goals a terminal loss.
- `ACT-471` is rejected: active board balance is not cargo bracing on an
  uneven walking route. `SYS-717` is rejected: trick chains do not multiply
  kill experience. `OBJ-204` is rejected: no graffiti replacement terminal.
- Exact multiplier coefficients, score/clock tie ordering and controller-to-
  balance physics remain unobserved. No direct PS5 execution is claimed.

## Delta summary

## New facts

- [Confirmed | Direct | High] Native PS5 access is the Cross-Gen Deluxe
  Bundle, not the separate PS4 standard SKU (`THPS-001`).
- [Confirmed | Direct | High] Tours has goal-based Warehouse and the modern
  contextual trick/score loop (`THPS-002`–`THPS-004`).
- [Observation | Corroborated | Medium] The bounded Warehouse run uses a
  two-minute timer, active balance and independently retained goals
  (`THPS-005`, `THPS-006`).

## New genes

- [Observation | Corroborated | Medium] Eight Active boundaries preserve
  contextual trick and balance control, score context, retained multi-goals,
  balance validity, timed partial settlement and live disclosure.

## New combinations

- [Observation | Direct | High] No verified new combination.

## Taxonomy changes

- [Observation | Corroborated | High] `TAXONOMY_CHANGE_104` adds eight
  definitions and changes no earlier signature or lifecycle.

## New questions

- Does a score line still active at the instant the Tour clock reaches zero
  bank on a subsequent landing, and what are the exact repeat, spin and
  stance coefficients in this PS5 build? Licensed direct play would be
  required before adding either rule.

## Next recommended game

- [Confirmed | Direct | High] `GAME-0366` — Tekken 3, the next authorised
  unit in `SEARCH_DEMAND_GAME_SELECTION_026`.
- Optimisation criterion: continue the fixed Goal order only after this
  complete unit's validation and stop window.
- Expected information gain: four-limb 3D fighting and round progression
  versus timed stunt-route scoring.
- Backlog impact: unit 6 of the active nine-game Goal.

## Why this game

- [Confirmed | Direct | High] This is the fifth selected cult anchor and
  tests whether a continuous trick route, score risk and partial Tour goals
  can coexist without copying Jet Set Radio's mission terminal.

## Reproducibility notes

1. Launch the native PS5 Cross-Gen Deluxe Bundle SKU, default moveset, with
   Perfect Rail Balance, Perfect Manual Balance and No Bails off.
2. On a fresh Tour profile choose THPS1 Warehouse, not Single Session or
   Free Skate. Record the visible goal list and clock before the first run.
3. Build and land one air → rail → manual line; separately repeat a trick and
   vary trick/spin/stance; record the score and balance display without
   inferring exact hidden coefficients.
4. Trigger one clearly declared goal, allow the two-minute run to settle and
   inspect whether it remains credited while other goals remain available.
5. Without direct licensed play, the steps above are a falsifiable protocol,
   not a report of actions already performed.

## Localisation review

- `verified`: stable IDs and the official title, Warehouse, Tour, Manual,
  Revert, S-K-A-T-E and SKU remain source-specific literal terms.
- `corrected`: reviewed Ukrainian profile, bounded scope, direct-play caveat,
  presentation and all eight new-gene definitions preserve the source's
  goal/score and balance/clock distinctions.
- `retained-with-reason`: English park, mode and trick names remain only as
  official labels where their literal spelling identifies a mechanic.
