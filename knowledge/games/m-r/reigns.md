---
game_id: GAME-0432
slug: reigns
game_title: Reigns
analysis_status: reviewed
reviewed: 2026-09-27
combination_ids: []
gene_ids:
  action:
    - ACT-232
  system:
    - SYS-004
    - SYS-1134
    - SYS-1135
    - SYS-1136
  constraint:
    - CON-709
  information:
    - INF-002
    - INF-421
  objective:
    - OBJ-248
  time:
    - TIM-001
---

# Game: Reigns — one monarch's card decisions

Use the canonical [vocabulary and genome rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Church, people, army and treasury are the four parameters of one power-vector rule, not four different genes. Card characters and swipe direction are carriers or options, not new taxonomy boundaries.

## Analysis scope

- Version / ruleset: original English *Reigns* for iOS at its August 2016 launch, reconstructed from contemporary creator and firsthand accounts. The exact app binary, phone model and difficulty configuration were not inspected. The 2026 anniversary content and later sequels are excluded.
- Structured analysis target: `PLAT-IOS` in [`knowledge/platforms/games.json`](../../platforms/games.json).
- Primary decision loop: read the current advisor card and four power bars, tilt left or right to inspect the offered response and indicated affected domains without learning the sign or magnitude, then commit one of the two responses by swiping. Its authored consequences change one or more power bars and may change hidden story conditions. If no power bar reaches either fatal extreme, the system filters the next-card pool by kingdom state and recency, draws from the remaining weighted cards and presents the next request. Repeat to extend this monarch's reign.
- Entry: one ordinary advisor card is available for a reigning monarch with all four power bars between their terminal extremes. No specific first card or exact numerical opening reserves are asserted.
- Positive terminal / evaluation: the player tries to keep that monarch on the throne as long as possible; one reign has no ordinary victory screen. The bounded packet ends at the first reign-ending extreme and the appearance of the successor's first ordinary decision state, to verify the dynasty transition, not a complete long-arc ending.
- Negative state: either the lower or upper extreme of any one power bar ends the current monarch's reign. The next heir begins with the visible power bars returned toward their ordinary middle state. Selected authored deck or narrative availability may persist across reigns; no specific permanent unlock is required in this first-death packet.
- Included: one-card binary response, tilt/preview cue, four displayed power bars, card-specific vector effects, hidden state and recency filtering, weighted random next card, both-end terminal rule, discrete card resolution, successor transition and the distinction between resetting reserves and possible cross-reign authored continuity.
- Excluded: a fixed first-card sequence, exact numerical meter deltas or probabilities, guaranteed direction of a previewed effect, long devil arc, dungeon, duels, achievements, exact year count, 2026 anniversary additions, *Her Majesty* and other sequels. The original developer mentions several subsystems, but none is necessary to establish this ordinary-card boundary.
- Reproducible parameterisation: select the original 2016 iOS ruleset; start with an ordinary advisor card and nonterminal reserves; inspect both offered sides without committing, swipe one, observe affected reserve changes and the next eligible card, and continue until one of four bars reaches either extreme. Inspect the successor's first ordinary card and reset reserves. This is a conditional procedure, not a claimed deterministic card script.
- Potential scoped modules: individual authored quest arcs, dungeon or duel subdecks, precisely measured choice previews, exact card weights, permanent deck additions, long dynasty completion and later anniversary content require separate evidence and boundaries.
- Direct-play status: no iOS installation, original binary, purchase, save, input recording, screenshot, video or audio was inspected. The 2016 creator account and original publisher listing support the core; a contemporary paid-copy firsthand analysis supports both-end failure and heir reset. This is a source-bounded reconstruction, not a witnessed playthrough.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `REG-001` | Original play presents one advisor card with a left/right binary response and aims to prolong a monarch's reign. | Confirmed | Corroborated | High | P1, P2 |
| `REG-002` | Church, people, army and treasury form four visible power reserves affected by decisions. | Confirmed | Corroborated | High | P1, P2, S1 |
| `REG-003` | Before each next card, the system excludes cards incompatible with current kingdom state or too recently shown, then samples eligible cards using unequal weights. | Confirmed | Direct | High | P1 |
| `REG-004` | Reaching either extreme of any reserve ends the current monarch and a successor returns visible reserves toward the middle. | Observation | Corroborated | High | S1, P2 |
| `REG-005` | Tilting a response before release shows wording and affected power-domain dots but not whether each reserve rises or falls. | Observation | Limited | Medium | S1 discussion |
| `REG-006` | Some authored content availability can persist across reigns, unlike the resetting visible reserves. | Confirmed | Corroborated | Medium | P1, P2, S1 |

## Basic data

- Release / origin: Nerial / François Alliot; published by Devolver Digital; original iOS release in August 2016. The current storefront is used for product identity and original rules text, not for later update mechanics.
- Platform or physical form: original English iOS mobile application, one ordinary monarchy-decision packet; exact 2016 build unverified.
- Mechanical family: time reversal and loop retention (`FAM-011`), here through a successor reign that resets reserves while authored narrative availability may continue.
- Sources accessed 2026-09-27: **P1** — [François Alliot's 2016 design deep dive](https://www.gamedeveloper.com/design/game-design-deep-dive-creating-an-adaptive-narrative-in-i-reigns-i-), for binary cards, four dimensions, state/recency filtering, weighted draw and persistent deck additions; **P2** — [Devolver's App Store description](https://apps.apple.com/us/app/reigns/id1114127463), for mobile identity, left/right swipe, four powers, dynasty and long-reign aim. The current listing also advertises a later anniversary update, which is excluded.
- Contemporary firsthand source: **S1** — [Emily Short's August 2016 paid-copy analysis and dated reader discussion](https://emshort.blog/2016/08/20/reigns/), for both-end death, average heir reserves, unpreviewed next card and the limited tilt cue. Her account discusses a Steam copy, so UI parity on the uninspected iOS binary is bounded by the publisher's mobile swipe description, not asserted as a direct iOS test.
- Claim IDs: `REG-001`–`REG-006`. No audiovisual evidence was used.

## Mechanical decomposition

### Action Genes

- Reuse `ACT-232`: choose one of two offered advisor responses. The left/right gesture is the interface carrier; a particular side need not always mean simple acceptance or refusal (`REG-001`, `REG-005`).

### System Behaviour Genes

- Reuse `SYS-004` for random outcome selection from the already eligible, weighted card pool. Add `SYS-1134` for one response applying its authored vector to several competing power bars and story conditions; `SYS-1135` for state/recency filtering and unequal card weights before the draw; `SYS-1136` for the successor replacing a dead ruler while visible reserves reset and only eligible authored availability persists. The conditional pool and the random sample are distinct (`REG-002`–`REG-004`, `REG-006`).

### Constraint Genes

- Add `CON-709`: both low and high extremes of each visible power reserve are fatal to the current reign. There is no safe strategy of simply maximising treasury or any other bar (`REG-004`).

### Information Genes

- Reuse `INF-002` for the unrevealed next card. Add `INF-421` for present four-bar visibility and a direction-neutral indicator of which bars one hovered choice will affect. Neither exact future card nor the sign/magnitude of its impact is exposed (`REG-002`, `REG-005`).

### Objective Genes

- Add `OBJ-248` for extending one monarch's tenure until an unavoidable terminal condition, evaluated by the duration of that reign rather than the completion of the larger dynasty story (`REG-001`, `REG-004`).

### Time Genes

- Reuse `TIM-001`: a swipe is a discrete commitment; power effects, fatal checks and next-card selection complete before the next response. The App Store describes a new request each reign year, but exact displayed year increments were not measured (`REG-001`–`REG-004`).

## Reproducible transitions

| Before | Action | Bounded resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| A card is face-up and four bars are nonterminal | Tilt toward one side without releasing | Response wording and affected domains can be previewed; sign and magnitude remain concealed | partial decision information, not a result guarantee | `REG-005` |
| Two responses are currently offered | Swipe one side | Authored effects update one or more power reserves and possible hidden story conditions | binary action and vector consequence | `REG-001`, `REG-002` |
| All four resulting bars remain between extremes | Finish the swipe | Cards incompatible with current kingdom conditions or recent appearances are removed; an eligible weighted card is sampled for the next request | contextual random narrative, not a uniform full-deck draw | `REG-003` |
| An effect takes treasury or another reserve to its upper bound | Commit that response | Current monarch dies despite the bar being abundant | both-end terminal, not merely depletion | `REG-004` |
| An effect takes a reserve to its lower bound | Commit that response | Current monarch dies; a successor takes over with power reserves near their middle state | failure and successor reset | `REG-004` |
| An authored prior choice unlocks eligible later content | Continue into another reign | Such deck/story availability can remain while ordinary visible reserves reset | selective loop retention, without a guaranteed named first-heir card | `REG-006` |

## Strategic and experiential structure

- Local decision: choose the less dangerous-looking of two card responses using current balances and incomplete preview; exact effects cannot be assumed.
- Medium-term planning: keep every power bar away from both extremes despite not controlling the timing of the next eligible request.
- Long-term structure: a failed monarch yields to an heir; selected content can persist into subsequent reigns, but the scoped evaluation is one reign.
- Failure attribution: the bar that reaches an extreme is visible, while the precise hidden weight or pending future card was not disclosed before its draw.
- Player-trust factor: tilt dots indicate affected domains, not whether the decision will help or harm them; do not render them as a deterministic signed forecast.

## Replay and variation

The two-response interface and four power dimensions persist, while kingdom conditions, previously seen cards and weighted selection change the offer sequence. Some small authored arcs restrict the eligible bag; the long arc and its terminal are outside this packet. There is no evidence that every new reign is a completely fresh full-deck shuffle.

## Adjacent systems and history

*Slay the Spire* (`GAME-0120`) also samples from constrained card pools, but it builds a combat deck and map, not a state/recency-filtered advisor request for four fatal-at-both-ends powers. *The Stanley Parable: Ultra Deluxe* (`GAME-0116`) is another authored branching experience, but its repeated route does not require this four-reserve balancing or weighted card bag. These are comparison hypotheses pending the deterministic selected-neighbour scan.

## Normalised genome

| Type | Active gene IDs | Key parameters |
|---|---|---|
| Action | `ACT-232` | two offered response sides |
| System Behaviour | `SYS-004`, `SYS-1134`, `SYS-1135`, `SYS-1136` | four-dimensional delta, filtered card bag, successor |
| Constraint | `CON-709` | fatal upper and lower bounds |
| Information | `INF-002`, `INF-421` | unrevealed next card, current bars and unsigned preview |
| Objective | `OBJ-248` | tenure of one monarch |
| Time | `TIM-001` | one completed card decision at a time |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `431` (`GAME-0001`–`GAME-0431`).
- Exact genome matches: none.
- Tied near matches: `GAME-0001` — 2048 (`3 / 21 = 0.142857`).
- Supported combination subsets: none.
- Scan date: 2026-09-27.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0001` *2048* | `SYS-004`, `INF-002`, `TIM-001` cover one discrete input followed by a concealed random successor. | Reigns commits one authored advisor response, shifts four political reserves, filters and weights its next card by context and can kill at either end of any reserve before the heir takes over; 2048 shifts and merges numbered tiles toward a target under spatial occupancy and a random tile spawn. | Tied-near maximum, `0.142857`; not an exact or verified combination match. |

## Taxonomy impact

Six new typed boundaries (`SYS-1134`, `SYS-1135`, `SYS-1136`, `CON-709`, `INF-421`, `OBJ-248`) isolate vector effects, contextual weighted narrative selection, successor retention, both-end fatal thresholds, unsigned power preview and tenure evaluation. See `TAXONOMY_CHANGE_169`. No earlier signature or verified combination changes.

## Negative results

- `SYS-175` and `SYS-469` describe rebuilding a failed run's route or item build with explicit unlocks. They do not state that a dynasty heir replaces one monarch with reset political power bars and conditional authored deck persistence.
- `CON-186` is a one-track maximum settlement pressure, not four reserves whose *both* bounds end a reign.
- `INF-001` would overstate visibility: hidden story conditions, next-card identity and exact choice effects are not shown.
- `ACT-232` covers the offered response without minting a duplicate swipe-action gene; left/right is a parameter, not a new mechanic.

## Delta summary

## New facts

- [Confirmed | Direct | High] The next advisor card is sampled only after state and recency filtering, with unequal card weights (`REG-003`).
- [Observation | Corroborated | High] Any of four power reserves ending at either extreme kills one monarch; an heir resets visible reserves (`REG-004`).

## New genes

- [Observation | Corroborated | High] Six new boundaries in `TAXONOMY_CHANGE_169`.

## New combinations

- [Observation | Corroborated | High] No new verified combination.

## Taxonomy changes

- [Observation | Corroborated | High] `TAXONOMY_CHANGE_169`; earlier signatures unchanged.

## New questions

- What exact original-iOS build, response preview and initial heir state would a direct 2016 binary trace establish? No answer is inferred from later updates.

## Next recommended game

- [Hypothesis | Limited | Medium] No next game is selected in the current 415–432 horizon.
- Optimisation criterion: review this completed batch and choose a fresh cross-platform, cross-genre selection before the next unit.
- Expected information gain: not yet estimated; requires new selection research.
- Backlog impact: the approved eighteenth and final unit is complete; no game is implicitly queued.

## Why this game

- [Hypothesis | Limited | Medium] An original mobile, binary-card balancing loop tests whether the taxonomy can separate chosen response, vector consequences, contextual weighted narrative selection and dynasty retention without treating every card as an independent gene.
