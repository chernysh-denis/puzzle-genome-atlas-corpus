---
game_id: GAME-0383
slug: the-sims-2-legacy-collection
game_title: The Sims 2: Legacy Collection
analysis_status: reviewed
reviewed: 2026-09-24
combination_ids: []
gene_ids:
  action:
    - ACT-257
    - ACT-524
  system:
    - SYS-205
    - SYS-431
    - SYS-432
    - SYS-1039
  constraint:
    - CON-380
  information:
    - INF-072
    - INF-168
    - INF-389
  objective:
    - OBJ-225
  time:
    - TIM-003
---

# Game: The Sims 2: Legacy Collection

Use the canonical [vocabulary and signature
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). The household,
residents, furnishings and displayed Want are instance parameters, not
universal gene names.

## Analysis scope

- Version / ruleset: Electronic Arts' 2025 English-language Windows 10/11
  The Sims 2: Legacy Collection. Its bundled expansions remain installed; this
  packet selects only the core occupied-residential-lot Live Mode interactions
  described by EA's original PC manual and current Legacy control guide. It
  does **not** claim that the reissue can run without its bundled expansions
  or that every original 2004 numeric parameter is unchanged.
- Entry and exit: prepare one new two-adult household with ordinary Family
  aspiration, no job, mods or cheats, on a furnished home lot with fridge,
  cooking fixture, toilet, washing fixture, table and beds. Preparation and
  furnishing are preconditions outside the packet. Enter Live Mode with both
  adults at home; at the first 08:00 clock reading, pause, note the current
  needs, relationship, Wants/Fears and aspiration panels, then resume. Stop at
  the next 08:00 with the household's current state, whether or not a Want
  was fulfilled. This 24-hour window is an analytical boundary, **not** an
  in-game victory screen or a claim that an exact controller trace was run.
- Primary decision loop: select a household member; inspect motives, mood,
  action queue, relationships and current Wants/Fears; queue eligible
  household-object or social interactions; let time, motive decay, autonomous
  decisions and social acceptance advance; switch residents or cancel a stale
  action; respond to urgent needs while trying to satisfy one displayed Want
  and preserve its aspiration gain during the bounded day.
- Included: selection between the two persistent residents; contextual
  self-care, cooking/eating and ordinary friendly social direction; visible
  action queue and autonomous activity; need decay and replenishment; mood
  pressure; accepted or rejected socials and directional relationship state;
  the displayed Wants/Fears panel and one Want event's aspiration/reward
  update; pause and speed controls; the fixed one-day observation endpoint.
- Positive local goal: complete at least one displayed eligible Want in the
  day so its icon changes and aspiration/reward points rise. Failing to do so
  before the day ends is a negative result for this bounded study, not a
  product-level loss; play may continue indefinitely.
- Failure and recovery: a contextual action may be unavailable, rejected or
  cancelled; a dire motive can interrupt planned activity. Energy, Bladder
  and Hunger at the bottom can trigger different failure responses, with
  extreme Hunger potentially fatal. The packet does not assign a guaranteed
  death, exact motive threshold or recovery timing to the prepared household.
- Excluded: Create a Family and Build/Buy authoring after the entry state;
  careers, school, travel, shopping, parties, romance, births, aging,
  aspiration-reward objects, long-term Want locks, community lots, death and
  resurrection as planned routes, expansion-exclusive aspirations, chemistry,
  seasons, businesses, pets, hobbies, apartments, supernatural states,
  time-specific scripted events, cheats, custom content, achievements and
  wider multi-day progression. Installed pack systems that may influence
  background state are not asserted absent; a direct Legacy run would need
  to record any such effect before expanding this packet.
- Potential scoped modules: one instrumented Legacy household day with
  executable/patch identity and initial save; a career departure/return day;
  Want/Fear locking and aspiration rewards; expansion-specific social or
  environmental effects; an unbounded multi-generation household.
- Direct-play status: none. No Legacy install, executable, save, screen,
  video, audio, controller or click log was inspected. The transitions below
  are source-bounded rules, not a claimed completed daily trace.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `TS2-001` | EA's Windows Legacy Collection includes The Sims 2 plus named expansion and stuff packs; it is not a bare base-game binary | Confirmed | Direct | High | P1 |
| `TS2-002` | EA's current Legacy guide identifies Live Mode, contextual interaction selection, active-household switching, pause and speed control | Confirmed | Direct | High | P2 |
| `TS2-003` | EA's PC manual states that occupied lots enter Live Mode and that selecting another household portrait transfers control while world time continues | Confirmed | Direct | High | P3 |
| `TS2-004` | Motive satisfaction decays with time, object and social interactions replenish it, and current needs affect mood and behaviour | Confirmed | Direct | High | P3 |
| `TS2-005` | Directed and autonomous interactions share a visible cancellable action queue; actor, target, mood and relationship affect social eligibility and acceptance | Confirmed | Direct | High | P3 |
| `TS2-006` | Daily and lifetime relationship measures need not be symmetric; socials can improve or degrade them and may be rejected | Confirmed | Direct | High | P3 |
| `TS2-007` | Displayed Wants and Fears change with life events; fulfilled Wants raise aspiration and award points, while realised Fears lower aspiration; one current desire may be locked | Confirmed | Corroborated | High | P3, P4 |
| `TS2-008` | Original-PC core Live Mode rules can be used as a bounded analytical slice of the Legacy reissue, but exact current numerical parameters and any installed-pack side effects remain uninspected | Hypothesis | Limited | Medium | P1–P3, R1 |
| `TS2-009` | The prepared two-adult day and one-Want target are analysis conditions, not an authored Legacy scenario, universal starting save or product victory predicate | Confirmed | Direct | High | R1 |

## Basic data

- Release / origin: Maxis' original The Sims 2 PC household simulation was
  reissued by Electronic Arts as The Sims 2: Legacy Collection on 31 January
  2025 for Windows 10/11. The reissue bundles the base game and many packs;
  this analysis does not replace their combined product with an imaginary
  pack-free executable.
- Platform or physical form: licensed Windows PC single-player household
  simulation, scoped to one occupied home lot and one 24-hour Live Mode span.
- Puzzle family: live system pressure, directed/autonomous-agent coordination
  and dependent household decisions.
- Primary sources, accessed 2026-09-24:
  - **[P1]** [EA's Legacy Collection
    announcement](https://www.ea.com/en-au/games/the-sims/amp/news/the-birthday-bundle),
    for release, Windows identity and included packs.
  - **[P2]** [EA Help's current Legacy PC control
    guide](https://help.ea.com/en/articles/the-sims/the-sims-2-legacy-collection/the-sims-2-legacy-controls/),
    for Live Mode, selection, contextual input and time controls.
  - **[P3]** [Electronic Arts' The Sims 2 Double Deluxe PC manual, reproduced
    in text](https://manualzz.com/doc/30283394/electronic-arts-double-deluxe--nightlife--celebration--st...),
    original authored booklet's base Live Mode sections pp. 21–30 and
    interactions pp. 37–38. Double Deluxe also contains Nightlife; only the
    common base sections named here are transferred.
  - **[P4]** [Maxis designer's contemporary Wants/Fears
    diary](https://www.gamespot.com/articles/the-sims-2-designer-diary-8/1100-6100496/),
    for aspiration-dependent desire generation and player locking.
- Source limitation **[R1]**: no Legacy executable or day trace was inspected;
  the prepared household and one-day stop are reproducibility instructions,
  not an observed pre-existing save.
- Claim IDs: `TS2-001`–`TS2-009`.

## Mechanical decomposition

### Action Genes

- `ACT-257` directs a selected resident to an offered self-care, object or
  social interaction. New `ACT-524` switches the selected household resident
  while the other remains simulated, unlike `ACT-228`'s transfer of direct
  movement/combat authority among authored protagonists.
- Candidate genes: Want/Fear locking is a possible separate future action,
  excluded from the one-day positive route rather than silently included.
- Parameters: resident, addressed object or person, menu choice, queue slot,
  cancellation and availability.
- Claim IDs: `TS2-002`–`TS2-005`.

### System Behaviour Genes

- `SYS-431` advances personal needs into mood pressure, `SYS-432` executes
  queued commands beside resident autonomy, and `SYS-205` updates directed
  relationship state after eligible social attempts. New `SYS-1039` resolves
  a realised Want or Fear into aspiration, reward and successor panel state.
- Resolution order: time advances motives; the interaction menu determines
  eligibility; a directed or autonomous activity executes or is interrupted;
  needs/relationships and current Wants/Fears settle; aspiration and reward
  effects apply if a displayed desire or fear is realised.
- Parameters: motive decay/activity effect, mood, autonomy, relationship
  direction and daily/lifetime measures, desire type, point award and refresh.
- Claim IDs: `TS2-004`–`TS2-007`.

### Constraint Genes

- `CON-380` requires the selected resident, other participant or object and
  current lot/relationship/need state to admit an offered interaction. A
  rejected social is not retroactively a successful relationship event.
- Scarce strategic resources: time, sufficient motive state, available social
  target and household funds for chosen meals. No required purchase is
  asserted for the positive local goal.
- Claim IDs: `TS2-004`–`TS2-006`.

### Information Genes

- `INF-072` exposes the persistent person profile and relationship panels;
  `INF-168` exposes current motives, mood and queued activity. New `INF-389`
  exposes the currently displayed Wants/Fears, aspiration status and visible
  reward effect separately from the motive bars.
- The PC manual's ordinary four Wants and three Fears describe its base panel;
  the Legacy reissue's installed packs and unlocks are not assumed to leave
  that exact count invariant. The gene boundary uses the displayed set, not
  a fixed number of icon slots.
- Claim IDs: `TS2-002`, `TS2-004`–`TS2-007`.

### Objective Genes

- New `OBJ-225` records satisfying at least one currently offered Want and
  retaining its aspiration-point transition inside the bounded day. It is a
  local in-game desired event, not a claim that midnight awards a victory.
- Success, evaluation and failure: inspect the panel before and after the
  event; a fulfilled Want changes its icon, aspiration and reward state. At
  the next 08:00, document success or failure and stop observation; the game
  remains open-ended.
- Claim IDs: `TS2-007`–`TS2-009`.

### Time Genes

- `TIM-003` advances resident needs, activity and socials in live simulation;
  pause and faster speeds alter the rate of observation, not a turn count.
- Candidate genes: none.
- Claim IDs: `TS2-002`–`TS2-005`.

## Reproducible transitions

| Before | Action | Deterministic resolution or stated branch | What it establishes | Claim ID |
|---|---|---|---|---|
| Both prepared adults are at home and one is selected | Select the other resident's portrait | Selection and visible personal panels transfer; the first resident persists rather than being replaced | multi-resident control | `TS2-002`, `TS2-003` |
| Selected resident's hunger is decreasing and stocked food/preparation affordance is available | Queue an offered meal interaction | The resident travels to and uses the fixture if the context remains valid; hunger can replenish, while elapsed time advances other motives | directed action versus autonomous world | `TS2-004`, `TS2-005` |
| Both residents are present with an eligible friendly interaction | Choose a social interaction | The target can accept or reject according to relationship and mood; accepted social can affect both Social need and relationship state | contextual non-guaranteed social result | `TS2-005`, `TS2-006` |
| A displayed Want matches a completed event | Complete the event | The desire icon refreshes, aspiration meter rises and reward points are credited | one local goal and successor desire | `TS2-007` |
| A displayed Fear's event occurs instead | Allow the event to resolve | Aspiration moves adversely and the fear icon refreshes; the day's observation continues | symmetric negative branch is not an instant game over | `TS2-007` |
| A planned action is still in the queue but becomes undesirable | Cancel its icon | Later queued actions move forward; autonomy may resume when no overriding direction remains | queue ownership and recovery | `TS2-005` |
| Next 08:00 arrives | Stop observation and compare recorded panels | The study's 24-hour boundary closes with or without local Want success; the product itself has no day-end victory | analytic stop versus product terminal | `TS2-008`, `TS2-009` |

## Strategic and experiential structure

- Local decision: choose a contextually offered command whose time and likely
  effects fit current hunger, energy, bladder, social need and mood.
- Medium-term planning: balance both residents' needs and their relationship
  while trying to trigger one visible Want, rather than queueing a long chain
  blindly.
- Long-term structure: the selected 24-hour sample demonstrates an open-ended
  household loop; it does not convert the sandbox into a one-day campaign.
- Failure attribution: need arrows/mood, offered menu, queue, daily/lifetime
  relationship meters and Wants/Fears panel distinguish an unoffered action,
  target rejection, unmet desire or insufficient time.
- Player-trust limit: source text supports qualitative transitions, not exact
  Legacy simulation coefficients or a recorded trajectory.
- Claim IDs: `TS2-003`–`TS2-009`.

## Replay and variation

- Household appearance, aspiration, personality, available Wants, motive
  starting values, spontaneous activity and social acceptance vary with a
  prepared save and subsequent events. Their exact numeric values are not
  asserted without a direct inspected run.
- The same household can continue after the day boundary; another sample can
  choose a different Want, arrangement or pack-influenced branch.
- Aspirations bias the kinds of Wants and Fears but do not fix one universal
  scripted sequence across all households.
- Claim IDs: `TS2-004`–`TS2-009`.

## Adjacent systems and history

- The Sims 4 packet in this corpus has a supplied single resident and a
  staged New In Town scenario ending. This The Sims 2 packet instead switches
  between two household members, samples an open-ended day and follows a
  live Want/Fear aspiration event without an authored scenario completion.
- Legacy Collection includes multiple expansion packs; chemistry, seasons,
  businesses, pets and later aspiration features are not silently treated as
  base-game proof or asserted impossible in an installed reissue.
- The Sims 2 relationship panel's short and long horizons are parameters of
  `SYS-205`, not a new gene; mood-linked motives reuse `SYS-431`, and action
  queues reuse `SYS-432`. New genes isolate resident selection and the
  desire/fear evaluation loop.
- Claim IDs: `TS2-001`–`TS2-009`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | ACT-257, ACT-524 | addressed target, actor switch, queue slot |
| System Behaviour | SYS-205, SYS-431, SYS-432, SYS-1039 | directed social state, motive/mood, autonomy, aspiration |
| Constraint | CON-380 | actor/target/context eligibility |
| Information | INF-072, INF-168, INF-389 | resident panels, desire icons and meter |
| Objective | OBJ-225 | one fulfilled Want inside the sampled day |
| Time | TIM-003 | continuous day with pause/speed control |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `382` (`GAME-0001`–`GAME-0382`).
- Exact genome matches: none.
- Tied near matches: `GAME-0158` — The Sims 4 (`8 / 16 = 0.500000`).
- Supported combination subsets: none.
- Scan date: 2026-09-24.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0158` The Sims 4 | Contextual resident directions, directed relationship change, motive-to-mood pressure, autonomous action queues, contextual eligibility, personal panels, active needs/queue display and live time | The Sims 2 packet selects two persistent household members and resolves current Wants/Fears into aspiration within an open day; The Sims 4 packet instead follows a supplied single resident through an authored scenario predicate and completion reward | `8 / 16 = 0.500000`; near match, not an identical objective or active-actor loop |

### Preserved research notes

- New genes: `ACT-524`, `SYS-1039`, `INF-389`, `OBJ-225`.
- Reused genes: `ACT-257`, `SYS-205`, `SYS-431`, `SYS-432`, `CON-380`,
  `INF-072`, `INF-168`, `TIM-003`.
- Classification result: New genes in a base household-loop packet.
- Evidence and reasoning: the Wants/Fears and one-day boundary are not a
  staged The Sims 4 scenario; existing mood, autonomy and relationship
  boundaries remain valid at their causal level. No earlier signature or
  verified combination changes.

## Taxonomy impact

- Registry changes: four additive Active genes, plus The Sims 2 as a new
  supporter for the reusable resident action, motive, autonomy, relationship,
  contextual interaction and personal-display genes. `INF-168` is widened
  from "dominant emotion" to "mood or emotional state" without changing its
  existing supporters' signatures.
- Taxonomy-change record: `TAXONOMY_CHANGE_122`.
- Candidate terms affected: household selection versus direct protagonist
  control; Wants/Fears resolution versus staged scenario reward.

## Negative results

- Do not treat installed expansions as absent in Legacy Collection. Their
  exclusive powers and effects require a separate inspected packet.
- Do not promote a fixed four-Want/three-Fear count, exact motivation rate or
  household outcome to a verified 2025-build claim from an older manual.
- Do not use `OBJ-052`: no branch-labelled scenario ending occurs at the next
  08:00 observation stop.

## Delta summary

## New facts

- [Confirmed | Direct | High] EA's Legacy product bundles the original game
  with expansions, so the analysis must bound features rather than assume a
  pack-free executable (`TS2-001`).
- [Confirmed | Direct | High] EA's manual and Legacy guide support household
  switching, contextual actions, motives, relationships, autonomy and
  Wants/Fears as inspectable core Live Mode mechanisms (`TS2-002`–`TS2-007`).

## New genes

- [Observation | Corroborated | High] `ACT-524`, `SYS-1039`, `INF-389` and
  `OBJ-225` distinguish the selected two-resident Want/Fear day packet from
  an authored single-resident scenario.

## New combinations

- [Observation | Direct | High] No new verified combinations. Existing subset
  support is computed in the corpus comparison above.

## Taxonomy changes

- [Observation | Corroborated | High] `TAXONOMY_CHANGE_122` adds the four
  genes and makes `INF-168`'s mood wording edition-neutral.

## New questions

- Does the current Legacy build change numerical need decay, Want slot count
  or social acceptance relative to the original PC manual?
- Which installed expansion effects occur without the player invoking an
  expansion-only action during a prepared household day?

## Next recommended game

- [Hypothesis | Limited | Medium] GAME-0384 F-Zero GX.
- Optimisation criterion: alternate a domestic autonomous life loop with an
  anti-gravity racing control, energy and position loop.
- Expected information gain: original-GameCube machine steering, energy and
  race settlement against existing vehicle-race signatures.
- Backlog impact: retains the selected 379–387 sequence; no new unit starts
  inside this game's commit.

## Why this game

- [Hypothesis | Limited | Medium] A directed two-resident household and
  Want/Fear aspiration feedback add a distinctive life-simulation comparison
  without pretending the bundled 2025 product is a bare 2004 build. Future
  direct play could reject the edition-transfer assumptions above.
