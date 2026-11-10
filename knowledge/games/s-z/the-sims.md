---
game_id: GAME-0461
slug: the-sims
game_title: The Sims
analysis_status: reviewed
reviewed: 2026-09-30
combination_ids: []
gene_ids:
  action:
    - ACT-130
    - ACT-257
    - ACT-524
    - ACT-612
  system:
    - SYS-205
    - SYS-431
    - SYS-432
  constraint:
    - CON-380
    - CON-739
  information:
    - INF-072
    - INF-168
    - INF-442
  objective: []
  time:
    - TIM-003
---

# Game: The Sims

The genome uses the canonical [vocabulary and signature](../../../docs/ARCHITECTURE.md#canonical-vocabulary). The Newbie household, its two adults, a particular bought chair, motive levels and the chosen observation hour are parameters, not gene names.

## Analysis scope

- Version / ruleset: the original English Windows *The Sims* (2000) base game, without expansion packs, console objectives, later-generation Wants or Scenarios. Maxis' original PC manual is the rule source; an original executable, disc, patch and save were not inspected.
- Structured analysis target: `PLAT-WINDOWS-PC`, original 2000 PC base-game Newbie household at 7 Sim Lane, as documented by the original manual. The manual does not prove one particular patched binary.
- Primary decision loop: select one of the two residents; read that resident's motives, mood and current action queue; choose an eligible object or social interaction; allow autonomy, movement and the household clock to advance; adjust the next command or switch residents. During the same sampled day, inspect shared funds, buy and legally place one affordable ordinary chair in paused Buy Mode, then use it in Live Mode to test the furnishing-to-motive connection.
- Entry and exit: reset the original tutorial to the documented Newbie starting conditions at 7 Sim Lane, complete its guided steps, retain the furnished house and two adults, and leave Free Will enabled. At the first subsequent 08:00 shown in Live Mode, pause and record both residents' visible needs and mood plus household funds. Observe until the next 08:00, when the research window closes; record whether the chosen chair was bought, placed and used, both residents' resulting conditions and the funds delta. This is an analytic 24-hour sampling boundary, not an in-game win or a claim that the game was played to that clock reading. A death before the endpoint ends the attempt adversely; no exact death threshold is asserted.
- Included: two persistent residents and selection transfer; contextual household-object use and ordinary conversation; their queued actions and Free Will; motive change, mood and possible action refusal; relationships if a conversation occurs; household funds, the Buy Mode catalogue and one priced chair purchase; legal footprint and orientation, a clear usable approach, and furniture use; the Needs, budget, profile and queue displays; Live Mode pause and speed controls.
- Excluded: household creation, moving to a different lot, architectural Build Mode, careers and newspaper job offers, recurring bill settlement, skill training, births, aging, romance, friends outside the household, visitors, disasters as a planned route, appliance repair, cheats, mods, expansion packs, console Get a Life goals, long-term financial optimisation and unbounded play. The source documents these broader systems, but they are not necessary to the chosen day.
- Potential scoped modules: first job and carpool, billed household economy, Build Mode layout changes, external social relationships, an instrumented original-disc day and version comparison with later PC releases.
- Direct-play status: source-only. No original Windows executable, disc, game screen, video, audio, save, player input trace or exact clock-to-clock outcome was inspected. The chair transaction and use are a reproducible test prescription, not an observed successful playthrough.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| SIM1-001 | The original manual's Newbie house at 7 Sim Lane is a repeatable tutorial starting point with two resident selection portraits | Observation | Direct | High | P1 pp. 4–7, 20–21, 39 |
| SIM1-002 | Live Mode advances time, needs and resident activity; pause allows panel inspection and queuing | Observation | Direct | High | P1 pp. 13–15 |
| SIM1-003 | The original game's motive panel includes hunger, comfort, hygiene, bladder, energy, fun, social and room; object interactions can replenish motives and mood affects response | Observation | Direct | High | P1 pp. 21, 31–34, 37–41 |
| SIM1-004 | Free Will can select autonomous actions, but selected-resident commands can supersede them; a blocked or occupied object can cause a queued action to disappear or time out | Observation | Direct | High | P1 pp. 19, 34, 39–41 |
| SIM1-005 | Buy Mode pauses Live Mode, displays priced objects and shared household funds, permits legal placement and resale; furnishing position affects later resident access | Observation | Direct | High | P1 pp. 15–17, 65–69 |
| SIM1-006 | Social interactions can change relationship state; the selected resident's relationship panel reveals the current result | Observation | Direct | High | P1 pp. 21–22, 42–45 |
| SIM1-007 | The game has no product-level victory condition; the 08:00-to-08:00 sample and one chair transaction are research choices, not an authored task | Observation | Direct | High | P1 pp. 65, R1 |
| SIM1-008 | Extreme neglect can produce need failure and starvation death, but the proposed day has no measured threshold or guaranteed outcome | Observation | Direct | Medium | P1 pp. 61–63, R1 |

## Basic data

- Release / origin: Maxis' original 2000 Windows household simulation, published by Electronic Arts; not its later sequels, expansions or console adaptations.
- Platform or physical form: Windows PC base-game target reconstructed from the original printed manual's English text reproduction.
- Puzzle family: live system pressure (`FAM-010`) and persistent household-agent coordination (`FAM-015`).
- Primary source, accessed 2026-09-30: **[P1]** [Maxis/Electronic Arts, *The Sims* original PC user's manual](https://manualmachine.com/gamespc/thesims/1119640-user-manual/), text reproduction of the 2000 booklet. Pages 4–7 document the resettable Newbie tutorial and 7 Sim Lane; pp. 13–21 cover modes, speed, funds, panels and autonomy; pp. 31–45 cover motives, queues and social interactions; pp. 61–69 cover failures, the absence of a win and Buy Mode.
- Corroborating collection identity: [Smithsonian National Museum of American History record](https://www.si.edu/object/sims%3Anmah_1813651) identifies a 2000 Maxis/EA Windows retail copy and its original user manual; it does not establish this packet's unplayed software revision.
- Source limitation **[R1]**: the 08:00 sampling window, choice of chair and use test are research design. We have not observed this route in the game or measured any budget, motive or relationship delta.
- Claim IDs: SIM1-001–SIM1-008.

## Mechanical decomposition

### Action Genes

- `ACT-257`: direct the selected adult to an offered household-object or social interaction. The resident executes it, not the cursor.
- `ACT-524`: change which persistent Newbie adult receives commands while the other continues to be simulated.
- `ACT-130`: spend shared Simoleons on an offered ordinary chair in Buy Mode. Price and chair model are parameters.
- New `ACT-612`: orient and place the bought chair in the home without changing its purchased identity. Its placement is an action distinct from spending funds and from the resident's later use.
- Parameters: selected resident, target, chair model, catalogue price, orientation, placement cell and ordered commands.
- Claim IDs: SIM1-001, SIM1-004, SIM1-005.

### System Behaviour Genes

- `SYS-431`: motives advance through time and activities, contribute to mood and may alter willingness or effectiveness.
- `SYS-432`: directed queue items and Free Will coexist; blocked or stale actions can fail rather than teleport through furniture.
- `SYS-205`: a permitted social exchange can change the persistent directed relationship. No guaranteed improvement is assumed.
- Resolution order: in Live Mode, time changes personal motives; the chosen context offers an interaction; the resident approaches and performs it or fails; motives and any social relationship settle. Entering Buy Mode pauses that progression, accepts the costed furnishing operation, then Live Mode resumes with its altered object access.
- Claim IDs: SIM1-002–SIM1-006.

### Constraint Genes

- `CON-380`: a resident-object or resident-resident action needs a compatible actor, usable target, current need or social context and reachable path; an occupied fixture can make a queued action lapse.
- New `CON-739`: a Buy Mode furnishing needs a legally supported, non-overlapping footprint and allowed orientation. Legal placement alone does not guarantee that a resident can approach and use it later; that second test belongs to `CON-380`.
- Scarce strategic resources: shared household funds, in-day time and residents' current needs. The sample has no invented fixed spending quota.
- Claim IDs: SIM1-004, SIM1-005.

### Information Genes

- `INF-072`: selected adult's profile, current activity and relationship state are inspectable.
- `INF-168`: current motive bars, mood and action icons distinguish urgent need, intended command and failed execution.
- New `INF-442`: the private household budget exposes a shared cash total plus current/past-day income and expense categories before another furnishing decision. This is intentionally not `INF-058`, which excludes private household accounts.
- Claim IDs: SIM1-002, SIM1-003, SIM1-005, SIM1-006.

### Objective Genes

- None admitted. The original game's manual explicitly rejects a product win condition. Buying and using a chair and stopping at 08:00 are evaluation instructions for this study, not objective predicates awarded by the game. Unlike the Sims 2 Want study, original *The Sims* has no displayed Want reward in this scope.
- Success, evaluation and failure: a useful observation records the same two residents, bought chair, actual use, visible motive change and funds at the end of the sampled day; any absent chair or interrupted action is a negative test result, not a game-over condition. Death before the endpoint ends this particular sample; the exact threshold was not measured.
- Claim IDs: SIM1-005, SIM1-007, SIM1-008.

### Time Genes

- `TIM-003`: the Live Mode clock advances needs and actions between interventions; pause and Buy Mode suspend that progression. The chosen one-day observation is a sampling parameter, not a deadline gene.
- Claim IDs: SIM1-002, SIM1-007.

## Reproducible transitions

| Before | Action | Deterministic resolution or stated branch | What it establishes | Claim ID |
|---|---|---|---|---|
| Both Newbie adults remain in one home; one is selected | Select the other portrait | The selected panel and command recipient change; the first adult persists | persistent household control | SIM1-001, SIM1-004 |
| Hunger falls while a usable refrigerator and food option exist | Queue an offered food interaction | The adult approaches and eats if the path/context remains valid; hunger can rise while other needs and time advance | directed object use and live motive pressure | SIM1-003, SIM1-004 |
| Free Will is enabled, no overriding command is active | Let Live Mode advance, then direct an eligible interaction | An autonomous action may appear; a new valid direction can supersede it | autonomy versus player order | SIM1-002, SIM1-004 |
| Household funds cover a catalogue chair | Enter Buy Mode, choose the chair and a legal orientation/footprint | Time pauses, cash is debited and the chair becomes placed; an invalid overlap is rejected | cost, pause and placement are separate boundaries | SIM1-005 |
| The chair is legally placed but blocks the route to another fixture | Direct a resident to that fixture | The queued interaction may time out rather than succeed; move the chair to clear the approach | placement legality is not use accessibility | SIM1-004, SIM1-005 |
| A resident can approach the new chair | Direct a compatible sit or rest interaction | The resident may use it and gain Comfort; observed amount is not predicted without a run | furnishing changes future affordance | SIM1-003, SIM1-005 |
| The next 08:00 appears | Pause and compare visible panels and funds | Research window closes regardless of motive or purchase outcome; no victory banner is inferred | analytic endpoint versus game terminal | SIM1-007, SIM1-008 |

## Strategic and experiential structure

- Local decision: choose whether the currently most urgent motive warrants an immediate command, or allow useful autonomous activity to continue.
- Medium-term planning: keep two residents' needs and paths serviceable while using the household's finite funds on an object that improves a relevant activity.
- Long-term structure: an open-ended household can be observed over many days; this packet deliberately stops after one and does not claim an authored daily score.
- Common heuristics: inspect motives before queuing; avoid blocking essential fixtures; buy useful furniture only when funds cover it.
- Failure attribution: the motive bars, queue icons, object placement feedback and household budget distinguish a low motive, failed path, unaffordable item and spent cash.
- Player-trust factors: the manual supports rule categories but not precise numeric simulation outcomes for our proposed day.
- Claim IDs: SIM1-002–SIM1-008.

## Replay and variation

- Tutorial reset gives a documented starting household, but later free decisions, autonomous activity, interaction timing and selected chair can produce different day states.
- No procedural room generation, guaranteed success or exact stochastic distribution is asserted.
- Different spending, command and resident-switch choices can expose different dependencies without changing the original game's absence of a win state.
- Claim IDs: SIM1-001–SIM1-008.

## Adjacent systems and history

- The Sims 2: Legacy Collection packet adds displayed Wants/Fears and an aspiration-reward goal; this 2000 base-game day has neither in its admitted rules.
- The Sims 4 packet instead follows a staged New In Town Scenario to a reward banner. Its later emotions, travel and scenario progress do not prove 2000 mechanics.
- SimCity 4 shares a visible money-management idea but its municipal ledger (`INF-058`) and recurring treasury settlement (`SYS-154`) expressly exclude a private household budget.
- Claim IDs: SIM1-003–SIM1-007.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-130`, `ACT-257`, `ACT-524`, `ACT-612` | chair model, price and placement |
| System Behaviour | `SYS-205`, `SYS-431`, `SYS-432` | motive rates, autonomy and social result |
| Constraint | `CON-380`, `CON-739` | item footprint and resident approach |
| Information | `INF-072`, `INF-168`, `INF-442` | panel values and budget categories |
| Objective | none | observational endpoint, not in-game win |
| Time | `TIM-003` | selected 08:00-to-08:00 window |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `460` (`GAME-0001`–`GAME-0460`).
- Exact genome matches: none.
- Tied near matches: `GAME-0383` — The Sims 2: Legacy Collection (`9 / 16 = 0.562500`).
- Supported combination subsets: none.
- Scan date: 2026-09-30.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0383` — The Sims 2: Legacy Collection | `ACT-257`, `ACT-524`, `SYS-205`, `SYS-431`, `SYS-432`, `CON-380`, `INF-072`, `INF-168`, `TIM-003` | Original *The Sims* spends shared funds to buy and place furniture and exposes an itemised private budget; the later game study instead follows a displayed Want to aspiration and reward points. The one-day stop in both is analytic, not a product win. | Nearest by symmetric Jaccard, `9 / 16 = 0.562500`; no exact match. |

- New genes: `ACT-612`, `CON-739`, `INF-442`.
- Classification result: `New gene`.
- Evidence and reasoning: the original manual distinguishes costed acquisition, spatial placement, a resident's later approach, and a private itemised household budget; the present registry's municipal ledger deliberately excludes that budget.

### Preserved research notes

- New genes: `ACT-612`, `CON-739`, `INF-442`.
- Classification result: `New gene`.
- Evidence and reasoning: the original manual distinguishes costed acquisition, spatial placement, a resident's later approach, and a private itemised household budget; the present registry's municipal ledger deliberately excludes that budget.

## Taxonomy impact

- Registry changes: three new Active definitions; no earlier gene boundary or game signature changed.
- Taxonomy-change record: `TAXONOMY_CHANGE_198`.
- Candidate terms affected: furniture purchase is `ACT-130`, not a second purchase gene; Buy Mode placement and private household budget are separately admitted.

## Negative results

- No new verified combination follows from one carrier.
- A one-day observation is not an objective gene or in-game victory; Sims 2 Wants and Sims 4 Scenarios are excluded from this original-game packet.

## Delta summary

## New facts

- [Observation | Direct | High] `SIM1-001`–`SIM1-007` isolate original-PC resident switching, needs, autonomy, Buy Mode placement and household funds from later-series goal systems.

## New genes

- [Observation | Direct | High] `ACT-612`, `CON-739` and `INF-442` distinguish furniture placement, its legal footprint and the private household budget.

## New combinations

- [Observation | Direct | High] No combination is admitted without separate cross-game support.

## Taxonomy changes

- [Observation | Direct | High] `TAXONOMY_CHANGE_198` adds three boundaries and preserves earlier signatures.

## New questions

- Can an instrumented original-disc day measure actual motive deltas, placement access and household cash changes across a pinned software revision?

## Next recommended game

- [Hypothesis | Limited | High] `GAME-0462` *Metal Slug 3*, original Neo Geo MVS, follows after full acceptance and the Goal stop window.
- Optimisation criterion: move from two-resident household coordination to a bounded run-and-gun mission with route choice.
- Expected information gain: test reusable combat, pickup and vehicle genes before adding arcade-specific boundaries.
