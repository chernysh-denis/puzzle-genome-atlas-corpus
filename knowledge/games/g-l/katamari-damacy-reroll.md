---
game_id: GAME-0376
slug: katamari-damacy-reroll
game_title: Katamari Damacy REROLL
analysis_status: reviewed
reviewed: 2026-09-23
combination_ids: []
gene_ids:
  action:
    - ACT-008
  system:
    - SYS-1022
    - SYS-1023
  constraint:
    - CON-068
    - CON-680
  information:
    - INF-383
  objective:
    - OBJ-218
  time:
    - TIM-003
---

# Game: Katamari Damacy REROLL

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). The target
diameter, attempt allowance, individual pickup sizes and impact severity are
parameters, not genes.

## Analysis scope

- Version / ruleset: the North American English PlayStation 4 digital
  *Katamari Damacy REROLL* base release of 20 November 2020, in its ordinary
  one-player analog-stick control mode. The installed build, patch and
  executable hash are unknown. The PlayStation listing confirms this product
  and platform; publisher descriptions and observed REROLL first-stage
  reports, not a PS4 execution trace, ground the rules below.
- Structured analysis target: replay the first ordinary `Make a Star 1`
  timed stage after it is unlocked; `GAME-0376` in
  [`knowledge/platforms/games.json`](../../platforms/games.json).
- Primary decision loop: steer the katamari through a living-room route,
  attach objects small enough for its present diameter, use that growth to
  reach larger object classes, avoid impacts that can shed the collection,
  compare current size with the displayed target and countdown, and continue
  until the timed stage is evaluated.
- Entry and exit: use a profile with the ordinary first star stage already
  available, select its replay, and accept the fresh small katamari at the
  living-room start. The positive terminal is the King's successful
  end-of-attempt result after the declared size has been reached before the
  displayed deadline and the gathered ball is made into a star. A stage
  report below the requirement, or expiry before sufficient size, is not
  success. A REROLL first-hand report for another platform and a Japanese
  REROLL stage table give 10 cm and four minutes; these are replication
  parameters to verify on PS4, not an independently observed PS4 timer.
- Included: directly steered continuous rolling, contact adhesion and
  persistent ball growth, size-relative object eligibility, impact-related
  shedding, visible live diameter/goal/countdown, a terminal deadline and
  first-stage size-based star evaluation.
- Excluded: the untimed first tutorial clear, later star and constellation
  stages, reaching cars, buildings or continents, the Moon, presents, cousins,
  collection completion, shooting-star speed bonuses, cooperative or versus
  play, gyro control, Eternal mode, different ports and any exact hidden
  pickup or collision coefficient.
- Potential scoped modules: later stages with district-scale growth,
  constellation-specific collection, Eternal runs, or versus size competition
  require separate version, entry, terminal and evidence.
- Direct-play status: none. No PS4 installation, save, controller log,
  screenshot, video, audio or replay was inspected. The precise PS4 timer,
  pickup ratios, collision threshold and early-end behaviour await direct
  measurement; the supported decision boundary does not depend on inventing
  them.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `KDR-001` | Bandai Namco released the PS4 REROLL remaster, retaining ball-rolling collection and the star-making premise. | Confirmed | Direct | High | PlayStation US listing; Bandai Namco PS4 announcement and official site |
| `KDR-002` | Analog-stick input rolls a collecting katamari, and attached household objects make it grow into eligibility for larger objects. | Confirmed | Corroborated | High | Bandai Namco official site and PS4 announcement; REROLL demo observation |
| `KDR-003` | Independent REROLL first-stage reports give a 10 cm target and four-minute ordinary replay allowance, unlike older PS2 guides' three minutes. The exact PS4 display was not inspected. | Observation | Limited | Medium | Japanese REROLL stage table; first-hand Switch demo report; original PS2 guide as contrast only |
| `KDR-004` | Objects too large for the current ball are not collected; a sufficiently grown ball can acquire a larger class. | Observation | Corroborated | High | Bandai Namco small-to-large description; first-hand REROLL demo report |
| `KDR-005` | A hard obstruction impact can dislodge gathered objects and reduce size. Its exact threshold and loss amount are unknown. | Observation | Limited | Medium | First-hand REROLL demo report |
| `KDR-006` | Ordinary star play measures ball size under a deadline and converts a successful collected ball into a star. Meeting the minimum need not end a replay immediately. | Observation | Corroborated | Medium | Original Namco timed-size description; Bandai Namco REROLL star-making premise; first-hand REROLL demo report |

## Basic data

- Release / origin: original Namco *Katamari Damacy* in 2004; Bandai Namco /
  Monkeycraft *REROLL* PS4 remaster released in North America on 20 November
  2020. This packet is the PS4 REROLL ruleset, not the original PS2 timer.
- Platform or physical form: US PlayStation 4 digital base edition, ordinary
  solo analog-stick replay of the first `Make a Star` stage.
- Puzzle family: `FAM-010` real-time system pressure: rolling and collection
  continue while the stage deadline decreases.
- Primary sources: [Bandai Namco REROLL official
  site](https://www.bandainamcoent.com/games/katamari-damacy-reroll),
  [Bandai Namco PS4 release announcement](https://en.bandainamcoent.eu/katamari/news/get-back-behind-the-ball-katamari-damacy-reroll-available-now-playstationr4-and-xbox),
  [PlayStation US PS4 product listing](https://store.playstation.com/en-us/product/UP0700-CUSA24361_00-KMDMCMGMMAINGAME),
  and [Namco's contemporary timed-size game
  description](https://www.bandainamcoent.co.jp/corporate/bnours/nours/vol42/pdf/42_03-13.pdf)
  for the original loop, not for the remaster's numerical allowance.
- Secondary direct-observation reports: [Japanese REROLL first-stage
  table](https://w.atwiki.jp/katamari/pages/5.html) and [a first-hand
  REROLL Switch demo account](https://taikengame.blog.fc2.com/blog-entry-3.html).
  The latter reports a displayed four-minute limit, 10 cm target, continued
  rolling after first reaching it and collision-related detachment. Neither
  report is a substitute for direct PS4 inspection.
- Claim IDs: `KDR-001`–`KDR-006`.

## Mechanical decomposition

### Action Genes

- Existing gene ID: `ACT-008` for direct local steering of one persistent
  controlled body. Analog-stick directions and an optional faster roll are
  control parameters, not a separately priced action or remote path order.
- Claim IDs: `KDR-002`.

### System Behaviour Genes

- Candidate gene `SYS-1022` attaches eligible contacted objects to the
  rolling ball and enlarges its physical body. `SYS-037` credits a collectible
  without making it the controlled collision body, so it does not explain
  this feedback loop.
- Candidate gene `SYS-1023` sheds attached objects after a hard collision;
  only the bounded possibility, not a universal impact coefficient, is
  asserted.
- Resolution order: local steering and the clock advance; eligible contact
  removes an object from the room, attaches it and increases measured size;
  later contacts are checked against the new size; a hard obstacle impact may
  detach some mass; the final size is tested at settlement.
- Claim IDs: `KDR-002`, `KDR-004`–`KDR-006`.

### Constraint Genes

- Existing gene ID: `CON-068` for a stage deadline that makes an insufficient
  ball fail when the allotted time ends.
- Candidate gene `CON-680` for the relative size gate on pickup. A larger
  cup or furniture piece does not stick just because the small ball touches
  it.
- Scarce strategic resource: remaining stage time; collected mass can also
  be lost after a hard impact. No invented finite object capacity is added.
- Claim IDs: `KDR-003`–`KDR-006`.

### Information Genes

- Candidate gene `INF-383` for the current diameter, target and remaining
  time displayed during the attempt. An object's exact hidden pickup ratio
  is not inferred from this display.
- Claim IDs: `KDR-003`, `KDR-006`.

### Objective Genes

- Candidate gene `OBJ-218` for a sufficiently large ball accepted as a star
  at the timed first-stage result. Merely arriving at the large object does
  not satisfy it.
- Success, evaluation and failure: a successful reported size at or above
  the stage requirement produces a star; insufficient size by the authoritative
  deadline fails this attempt. Higher scores, rapid comet bonuses and all
  later stages are not required.
- Claim IDs: `KDR-001`, `KDR-003`, `KDR-006`.

### Time Genes

- Existing gene ID: `TIM-003` because the clock and the moving ball advance
  during local control; no turn or pause is imposed on ordinary rolling.
- Claim IDs: `KDR-002`, `KDR-003`, `KDR-006`.

## Reproducible transitions

| Before | Action | Rule-bounded resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Fresh small first-stage katamari faces loose tiny sweets and stationery | Steer the ball over one eligible object | The item leaves its floor position, sticks to the ball and contributes to its diameter | The objective mass is a changing controlled body, not an abstract pickup count | `KDR-002`, `KDR-004` |
| A large object is beyond the ball's present pickup size | Roll against it | It does not join the katamari; steer elsewhere to collect smaller items first | The growth loop has an ordered size gate | `KDR-004` |
| Enough smaller objects are attached that a former obstruction is now eligible | Return and roll through that object | Its successful attachment further increases size | A previous collision target can become a resource | `KDR-002`, `KDR-004` |
| A grown katamari has loose attachments and a hard obstacle lies ahead | Strike the obstacle with sufficient severity | Some attachments can scatter and measured diameter may fall; exact amount is not asserted | Local routing can reverse earlier growth without resetting the stage | `KDR-005` |
| The stage is still active after the ball reaches its displayed minimum | Continue rolling while time remains | More eligible objects can attach before result settlement | The minimum target is not an assertion of immediate forced completion | `KDR-006` |
| The authoritative stage interval ends with sufficient size | Accept the result | The King recognises success and makes the gathered katamari a star | The declared positive terminal is evaluated size, not total object collection | `KDR-001`, `KDR-006` |
| The interval ends below the required size | Accept the result | The current attempt does not create the required successful star | Expiry is the negative terminal, not a collectible-count penalty | `KDR-003`, `KDR-006` |

A direct replication should record the PS4 product/build, control preset,
stage-selection history, initial diameter, displayed target and timer, at
least one rejected and later accepted object class, impact event and
detached-item count if one occurs, diameter at result and star outcome.
The reported four-minute allowance is a lead to test, not an invented PS4
observation.

## Strategic and experiential structure

- Local decision: choose a path through currently eligible small objects
  while keeping enough clearance from large obstacles.
- Medium-term planning: revisit previously too-large objects after growth,
  weighing their likely size contribution against travel time and collision
  risk.
- Long-term structure: grow the ball past the first-stage minimum before
  the clock expires, then use any remaining time for extra size if desired.
- Common heuristics: gather dense clusters of small items before attempting
  furniture; this is a plausible route hypothesis, not a measured optimum.
- Failure attribution: visible size and time show whether the deadline or
  growth is the immediate problem; exact impact severity remains uncertain.
- Player-trust factors: a large object refusing to stick, then later sticking
  after the ball grows, makes the gating rule perceivable.
- Claim IDs: `KDR-002`–`KDR-006`.

## Replay and variation

- What changes between attempts: route, collection order, accumulated size,
  impacts and final size within the same living-room stage.
- Randomness or procedural generation: the evidence does not establish
  object-layout randomisation or a changed first-stage seed. Do not call this
  a procedural stage.
- Multiple viable strategies: direct observations show more than one possible
  small-item route; no best path is established here.
- Typical replay motive: improve final diameter or finish the target faster,
  though no speed bonus is needed for the scoped positive terminal.
- Claim IDs: `KDR-003`–`KDR-006`.

## Adjacent systems and history

- Direct predecessor: the original PS2 *Katamari Damacy* is the remaster's
  source, not an interchangeable numerical ruleset. Older three-minute
  `Make a Star 1` guides must not supply REROLL's time parameter.
- Variants: Switch gyro and multiplayer, later Xbox/PC editions and the
  separate *We Love Katamari REROLL+ Royal Reverie* product are not included.
- Similar games: the complete lower-ID scan is owned below.
- Important differences: Spore's Cell-stage growth spends food into DNA and
  editor history; Katamari's acquired objects remain on the steered rolling
  body, change pickup eligibility and may detach after impact.
- Claim IDs: `KDR-001`–`KDR-006`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-008` | Analog steering and chosen route |
| System Behaviour | `SYS-1022`, `SYS-1023` | Adhesion, growth and collision shedding |
| Constraint | `CON-068`, `CON-680` | Deadline and relative pickup size |
| Information | `INF-383` | Current size, target and countdown |
| Objective | `OBJ-218` | Timed minimum-size star result |
| Time | `TIM-003` | Live rolling and clock progression |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `375` (`GAME-0001`–`GAME-0375`).
- Exact genome matches: none.
- Tied near matches: `GAME-0116` — The Stanley Parable: Ultra Deluxe (`2 / 12 = 0.166667`); `GAME-0302` — Captain Toad: Treasure Tracker (`2 / 12 = 0.166667`).
- Supported combination subsets: none.
- Scan date: 2026-09-23.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0116` — The Stanley Parable: Ultra Deluxe | `ACT-008`, `TIM-003` | Shares direct movement and live time, not object adhesion, size gating, collision loss or a deadline-qualified star. Its authored narrative branches are not a rolling-body system. | Near, `0.166667` |
| `GAME-0302` — Captain Toad: Treasure Tracker | `ACT-008`, `TIM-003` | Shares direct movement and live time, not size-changing pickup. Its fixed spatial route and treasure terminal do not grow the controlled body. | Near, `0.166667` |

### Preserved research notes

- New genes: `SYS-1022`, `SYS-1023`, `CON-680`, `INF-383`, `OBJ-218`.
- Classification result: New gene.
- Evidence and reasoning: contact pickup physically reshapes the controlled
  rolling body and changes later eligibility, while a fixed deadline evaluates
  the resulting diameter.

## Taxonomy impact

- Registry changes: add five bounded genes; no earlier signature changes.
- Taxonomy-change record:
  [`TAXONOMY_CHANGE_115`](../../../research/taxonomy-changes/TAXONOMY_CHANGE_115.md).
- Candidate terms affected: rolling-body adhesion, size gate, impact shedding
  and target diameter are mechanics, not a genre label.

## Negative results

- No verified combination is accepted by theme or by ball geometry alone.
  The generated proper-subset scan decides support.

## Delta summary

The headings below list only new corpus changes. Reviewed Ukrainian research
views are generated from the separate locale layer.

## New facts

- [Observation | Corroborated | Medium] REROLL's first ordinary star stage
  is a bounded rolling-size task with a reported four-minute allowance, not
  the original PS2 guide's three-minute value (`KDR-003`).

## New genes

- [Observation | Corroborated | Medium] Five new genes distinguish physical
  pickup, reversible impact loss, relative size eligibility, live size/time
  information and the first star terminal.

## New combinations

- [Observation | Direct | High] No combination is added for this packet.

## Taxonomy changes

- [Observation | Corroborated | Medium] `TAXONOMY_CHANGE_115` adds the five
  boundaries without revising any earlier signature.

## New questions

- Direct PS4 play should verify the displayed allowance, exact impact loss,
  eligible item sizes and whether the ordinary replay may be ended early.

## Next recommended game

- [Hypothesis | Limited | Medium] `GAME-0377` CATAN, the next selected
  genre-contrast unit.
- Optimisation criterion: alternate continuous spatial collection with
  turn-structured trading and production.
- Expected information gain: test whether scarce settlement sites, dice
  production and player exchange create a distinct dependency economy.
- Backlog impact: no predecessor signature is revised.

## Why this game

- [Hypothesis | Limited | Medium] Its physically accumulated rolling body
  tests size-gated collection and reversible growth under a short deadline,
  unlike the previous garden-residency packet.
