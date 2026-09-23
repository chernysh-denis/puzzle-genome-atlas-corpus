---
game_id: GAME-0370
slug: theme-hospital
game_title: Theme Hospital
analysis_status: reviewed
reviewed: 2026-09-23
combination_ids: []
gene_ids:
  action:
    - ACT-006
    - ACT-139
    - ACT-487
    - ACT-488
    - ACT-504
    - ACT-505
  system:
    - SYS-045
    - SYS-154
    - SYS-198
    - SYS-1005
    - SYS-1006
    - SYS-1007
  constraint:
    - CON-171
    - CON-672
  information:
    - INF-058
    - INF-072
    - INF-377
  objective:
    - OBJ-213
  time:
    - TIM-003
---

# Game: Theme Hospital

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Diseases, room
names, furniture, money amounts and the five scenario thresholds are carrier
parameters, not gene names.

## Analysis scope

- Version / ruleset: Bullfrog's original English PC Theme Hospital rules as
  documented in the original DOS/Windows 95 manual. The current licensed GOG
  listing establishes an accessible distribution target, but no GOG binary or
  patch was inspected. This packet covers **First Game** tutorial-enabled
  level one, not every hospital in the campaign.
- Structured analysis target: licensed Windows PC distribution, original
  English first-level rules; see `GAME-0370` in
  [`knowledge/platforms/games.json`](../../platforms/games.json).
- Entry: begin a new Easy First Game, receive the initial empty hospital shell
  and its Mission Briefing, with the Build Timer still allowing construction
  before patients arrive. The briefing supplies this level's own winning and
  losing thresholds; this record does not invent their numerical values.
- Primary decision loop: inspect briefing, budget, staff candidates and room
  demand; place reception and blueprint a furnished GP's Office; hire the
  required receptionist and doctor; open the hospital; add diagnosis,
  treatment and support rooms with qualified staff; inspect patient routes,
  queues, diagnostic uncertainty, cures, deaths, finances, happiness and
  reputation; revise capacity, staff or policy before a quarterly appraisal.
- Positive terminal: at one end-of-quarter appraisal, all five displayed
  Reputation, Money, Cures, Happiness and Hospital Value win criteria reach
  their briefing targets and no losing criterion is met. The player is offered
  the next hospital, whether or not they choose to leave. An earlier
  unsuccessful quarter is not automatically the terminal.
- Negative terminal: a declared losing criterion reaches its threshold and
  the level is forfeited. Falling short of a win criterion in one quarter
  without meeting a loss condition leaves continued management possible.
- Included: first-level reception desk, GP's Office, General Diagnosis,
  Pharmacy, Psychiatry with qualified doctor, Inflation Clinic, patient
  facilities and staff room as available in the original manual; room
  blueprints, doors and required furnishings; receptionist, doctor, nurse and
  handyman hiring; autonomous staff/patient movement; queues, diagnostic
  referral, condition-compatible cures, prices/income, wages and expenditure,
  staff fatigue, patient needs and happiness, reputation, progress and time.
- Excluded: later hospitals, operating theatre and surgery, research and
  training rooms unavailable on level one, epidemics, disasters, emergencies,
  marketing campaigns, exact hidden probability or reputation formula,
  multiplayer hospital comparison, cheats, ports, community reimplementations
  and all GOG-specific compatibility behaviour. First Game prompts are
  guidance, not autonomous construction or proof of a particular play trace.
- Reproducible parameterisation: record selected difficulty, briefing target
  bars, room footprint/door/furniture, worker role and qualification, opening
  time, each patient's reception–diagnosis–treatment route, queue or policy
  decision, cash and outcome changes, and the quarter's criterion values.
  Specific floor plans, patient identities, exact room prices and unknown
  random arrivals are not prescribed.
- Direct-play status: not conducted. No entitlement, installation, save,
  executable hash, screenshot, video, audio or input trace was inspected. The
  original publisher manual supports a source-bounded reconstruction, not a
  claimed successful playthrough.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `TH-001` | Original PC First Game enables tutorial and starts from an empty shell with a mission briefing | Confirmed | Direct | High | P1 |
| `TH-002` | Reception, a furnished GP office and role-compatible hires precede ordinary patient service | Confirmed | Direct | High | P1 |
| `TH-003` | A room is built by blueprint, valid door and required furniture, with invalid placements rejected | Confirmed | Direct | High | P1 |
| `TH-004` | GP assessment may send a patient to further diagnosis or to a compatible cure | Confirmed | Direct | High | P1 |
| `TH-005` | Psychiatry requires a psychiatric doctor, Pharmacy a nurse; research and surgery are not first-level facilities | Confirmed | Direct | High | P1 |
| `TH-006` | Queues, personal needs, staff fatigue and hospital finances change during live time | Confirmed | Direct | High | P1 |
| `TH-007` | Cure, death, diagnosis quality and price contribute to reputation; the exact formula is not published in the cited manual | Confirmed | Direct | High | P1 |
| `TH-008` | The five briefing win bars are checked together by quarterly cycle; any fully met loss bar forfeits the level | Confirmed | Direct | High | P1 |
| `TH-009` | The current GOG listing is a licensed distribution target, not evidence that its binary was played or matches an inspected patch | Observation | Direct | High | P2, V1 |

## Basic data

- Release / origin: Bullfrog Productions, published by Electronic Arts in
  1997. The manual describes both MS-DOS and Windows 95 PC releases.
- Platform or physical form: licensed Windows PC listing; original PC rules
  analysed from the publisher's manual rather than a running application.
- Puzzle families: real-time system pressure; agent routing and coordination;
  ordered dependency sequencing.
- Primary sources, checked 2026-09-23:
  - **[P1]** [original Bullfrog/Electronic Arts PC manual, mirrored PDF](https://www.bestoldgames.net/download/games/theme-hospital/theme-hospital-manual.pdf),
    pp. 7–8, 12–24, 35–44 and 45–48 for entry, room and worker rules,
    patient/queue behaviour, business reports, five criteria and tutorial.
  - **[P2]** [licensed GOG Theme Hospital listing](https://www.gog.com/en/game/theme_hospital),
    for present-day product identity and Windows distribution only.
- Validation source: **[V1]** repository-side rule-transition reconstruction
  from P1; neither a direct game session nor binary parity test.
- Claim IDs: `TH-001`–`TH-009`.

## Mechanical decomposition

### Action Genes

- `ACT-006`: pause or change simulation speed to inspect and intervene before
  arrivals, fatigue or the quarterly clock advance.
- `ACT-139`: place legal corridor fixtures such as reception, seating and
  drinks machines, then move or remove ordinary placed property.
- `ACT-487`: use the Build Timer's GO control to open the managed hospital to
  incoming patients; an entry fee is not asserted for this carrier.
- `ACT-488`: hire and place a receptionist, doctor, nurse or handyman as an
  autonomous worker, subject to role/skill suitability.
- New `ACT-504`: make a sized room blueprint, place a valid door and required
  furniture, then commit the room for service.
- New `ACT-505`: adjust patient queues and hospital diagnosis/rest policy,
  including whether uncertain cases are treated, referred or sent away.

### System Behaviour Genes

- `SYS-045`: staff and patients move autonomously between reception, rooms,
  queues and exits rather than requiring every step from the player.
- `SYS-154`: treatment receipts and other income meet construction costs,
  wages and recurring expenditure in one managed treasury.
- `SYS-198`: patient comfort and staff fatigue change happiness, departure,
  errors or willingness to work over time.
- New `SYS-1005`: reception and diagnosis determine a patient-specific next
  service; incomplete diagnosis can send the patient through another room or
  require a policy decision instead of directly exposing a guaranteed cure.
- New `SYS-1006`: a compatible staffed treatment resolves the diagnosed
  condition into a bounded cure or failure outcome and updates cure/death
  counts and income.
- New `SYS-1007`: patient outcomes, diagnosis quality and prices update
  hospital reputation, which affects later patient demand without exposing
  the hidden exact formula.

### Constraint Genes

- `CON-171`: room construction and retained staffing draw on a finite budget;
  a planned service cannot be built or sustainably run without funds.
- New `CON-672`: a room needs a legal footprint, door and required furnishings;
  its service also requires an appropriate worker/qualification (for example
  nurse in Pharmacy or psychiatrist in Psychiatry).

### Information Genes

- `INF-058`: business screens itemise cash, income, expenditure, wages and
  other financial state before another build or hire.
- `INF-072`: selecting a staff member or patient exposes the person's
  activity, ability, needs or mood for failure attribution.
- New `INF-377`: briefing, queue, casebook and status views expose room
  pressure, diagnosis or treatment state and each of the five quarterly
  progress bars, not exact unseen future arrivals or formula weights.

### Objective and Time Genes

- New `OBJ-213`: meet all five briefing-defined win thresholds together at a
  quarterly appraisal while avoiding every declared loss threshold.
- `TIM-003`: construction and management decisions occur against ongoing
  patient arrivals, movement, fatigue, finances and quarterly time.

## Reproducible transitions

| Before | Action | Bounded resolution | Establishes | Claim |
|---|---|---|---|---|
| Empty first hospital and Build Timer | inspect Mission Briefing | five win categories and level-specific loss criteria are shown before opening | scoped entry and observable target | `TH-001`, `TH-008` |
| Legal floor and enough cash | draw a GP blueprint, choose legal door and place default furniture | invalid size/placement cannot be committed; completed furnished room opens for business | spatial room construction | `TH-003` |
| Reception desk lacks receptionist | hire and place an eligible receptionist | worker walks to the desk; ordinary reception can route incoming patients | staffed entry dependency | `TH-002` |
| Furnished GP's Office and hired doctor | press GO, allow an arrival and assessment | patient enters through reception; doctor either identifies treatment or refers for more diagnosis | live routed service | `TH-002`, `TH-004` |
| A patient remains incompletely diagnosed | build General Diagnosis and adjust diagnosis policy if needed | compatible assessment increases knowledge or yields a decision instead of guaranteed cure | uncertainty and referral | `TH-004` |
| Diagnosed condition has a compatible room | staff Pharmacy with a nurse or Psychiatry with a qualified doctor, then advance time | patient queues, treatment resolves, and cure/failure, income and reputation-relevant outcomes update | typed service and feedback | `TH-005`, `TH-007` |
| One room queue is overloaded | change queue limit or move a patient to another same-type room | patient joins the selected queue; all-alternatives-full can exceed a nominal limit | editable but bounded queue | `TH-006` |
| Financial quarter ends | allow appraisal | all five briefing win bars completed and no loss bar full offers progression; a full loss bar forfeits | conjunctive terminal | `TH-008` |

## Strategic and experiential structure

- The first dependency is operational, not decorative: reception is useless
  without its worker, and a room cannot process a patient before its legal
  blueprint, furnishings and compatible staff are in place.
- The hospital is a service network under feedback. More diagnosis can reduce
  treatment uncertainty but raises queues, cost and patient waiting; more
  staff or rooms increases capacity while draining the same budget measured
  by the Money objective.
- Failure can be traced to missing service capacity, worker qualification,
  referral loops, tired staff, unhappy patients, bad treatment outcomes or
  financial pressure. Exact hidden probabilities are not claimed.

## Replay and variation

- Room plan, queue policy, hires, prices, arrival timing, diseases and
  patient outcomes vary. The fixed five criterion *categories* remain, but
  this record deliberately does not substitute guessed first-level numbers
  for the displayed briefing.
- A losing criterion can end the level before any winning quarter. A quarter
  that fails to win but does not trigger loss is an intermediate state.

## Adjacent systems and history

- RollerCoaster Tycoon Deluxe shares opening a managed venue, placing
  facilities, autonomous visitors/workers, needs, income, queues and a
  deadline. Its ride boarding/dispatch and Park Rating are distinct from
  diagnosis-to-treatment referral and quarterly five-bar appraisal.
- Two Point Hospital is a later related hospital-management design; no later
  game's exact rules are imported into the 1997 Theme Hospital packet.

## Normalised genome

The front matter is canonical. The complete scoped signature has 19 Active
genes: six Action, six System Behaviour, two Constraint, three Information,
one Objective and one Time. The eight new boundaries are additive and do not
retrofit any lower-ID signature.

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `369` (`GAME-0001`–`GAME-0369`).
- Exact genome matches: none.
- Tied near matches: `GAME-0335` — RollerCoaster Tycoon Deluxe (`11 / 30 = 0.366667`).
- Supported combination subsets: none.
- Scan date: 2026-09-23.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0335` — RollerCoaster Tycoon Deluxe | `ACT-006`, `ACT-139`, `ACT-487`, `ACT-488`, `SYS-045`, `SYS-154`, `SYS-198`, `CON-171`, `INF-058`, `INF-072`, `TIM-003` | Both open a managed public venue and balance spatial facilities, autonomous people, needs, staff, finance and time. Theme Hospital instead makes a patient pass reception, staged diagnosis and qualified medical treatment, then tests five hospital criteria together at a quarterly appraisal. RollerCoaster Tycoon routes discretionary visitors through rides, queue boarding and dispatch toward a two-bar park objective. | Near, `11 / 30 = 0.366667` |

## Taxonomy impact

`ACT-504`–`ACT-505`, `SYS-1005`–`SYS-1007`, `CON-672`, `INF-377` and
`OBJ-213` are additive boundaries under `TAXONOMY_CHANGE_109`. Existing
managed-domain and personal-state genes transfer without changing their
definition or any earlier game signature. No combination is registered from
one new hospital carrier.

## Negative results

- No direct game execution, exact installed-build parity, patient RNG,
  optimal hospital design, exact first-level threshold values or exact
  reputation formula is claimed.
- Later-level research, surgery, training, disasters and epidemic controls
  are excluded despite appearing elsewhere in the full manual.
- A patient visibly having Bloaty Head is not treated as a completed
  diagnosis; the manual still requires diagnosis before the Inflation Clinic.

## Delta summary

The original PC manual closes a first-hospital packet from empty entry to
quarterly appraisal. Reused management genes capture shared finance and
autonomous people; eight new boundaries separate room commissioning,
patient-flow policy, referral, treatment, reputation feedback, service
eligibility, status information and the five-way quarter objective. No
earlier game signature or verified combination changes.

## New facts

- The manual distinguishes a failed-to-win quarter from a separate
  level-forfeiting loss threshold. Even visibly symptomatic patients require
  diagnosis before the matching clinic can treat them.

## New genes

- `ACT-504` and `ACT-505` isolate room commissioning and queue/policy edits.
- `SYS-1005`–`SYS-1007` isolate referral, typed treatment and reputation
  feedback.
- `CON-672`, `INF-377` and `OBJ-213` capture service eligibility, status
  information and the five-target quarterly appraisal.

## New combinations

- None; one new carrier does not prove recurrence.

## Taxonomy changes

- `TAXONOMY_CHANGE_109` records eight additive boundaries and no earlier
  signature change.

## New questions

- Direct observation of a licensed build could pin the first level's exact
  thresholds and distinguish its current patches from the original manual.

## Next recommended game

`GAME-0371` Pokémon Snap, as reserved in
[`SEARCH_DEMAND_GAME_SELECTION_027`](../../../research/selection/SEARCH_DEMAND_GAME_SELECTION_027.md).

## Why this game

Theme Hospital gives the next horizon a recognisable management-simulation
anchor whose visible room–staff–patient chain differs strongly from the
preceding nine games' maps, sports scenes and board pieces.

## Completion checklist

- [x] Original PC first-level rules, entry, exit, causal systems and exclusions bounded.
- [x] Publisher manual and licensed distribution identity separated from direct play.
- [x] Deterministic comparison, bilingual presentation, artwork and gates complete.

## Search-demand continuation

This is the first reserved unit in
[`SEARCH_DEMAND_GAME_SELECTION_027`](../../../research/selection/SEARCH_DEMAND_GAME_SELECTION_027.md).
