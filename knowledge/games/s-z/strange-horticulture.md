---
game_id: GAME-0554
slug: strange-horticulture
game_title: Strange Horticulture
analysis_status: reviewed
reviewed: 2026-11-19
combination_ids: []
gene_ids:
  action:
    - ACT-070
    - ACT-087
    - ACT-089
    - ACT-107
    - ACT-751
    - ACT-752
    - ACT-753
  system:
    - SYS-1603
    - SYS-1604
    - SYS-1605
  constraint:
    - CON-821
  information:
    - INF-003
    - INF-530
    - INF-531
  objective:
    - OBJ-004
    - OBJ-305
  time:
    - TIM-002
    - TIM-003
---

# Game: Strange Horticulture

Use the canonical [vocabulary and signature rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
Fictional plant names, specimen traits, coordinates, visitor count and gauge
increments parameterise the admitted mechanics; they are not separate genes.

## Analysis scope

- Version / ruleset: full English Windows Steam release, application 1574580,
  standard mouse/keyboard shop rules, complete Day 1 Friday plus its first
  optional Rising Dread recovery. The product launched on 21 January 2022.
  Contemporary release routes and later released-PC observations support the
  bounded rules; no exact installed build, executable checksum, entitlement,
  save or native playthrough was verified. Do not claim later footage is a
  checksum-authenticated launch binary. Use manual shelf labels; automatic
  labelling and hints remain optional presentation/accessibility settings.
- Primary decision loop: read the current visitor's request and acquired
  botanical entries, inspect candidate plants, retain or revise tentative
  labels, offer the appropriate specimen, and use the result to advance the
  visitor script and reference collection. Interpret retained letters against
  the map, spend exploration readiness for a visit, then wait or water to
  replenish it. Recover from the first full dread state if it occurs.
- Entry and exit: start a new released Windows game at the first Friday shop
  with its initial shelves, book, drawer and introductory letter. Include all
  five visitors: Victoria Gray, postman David Chafer, Gilbert Ames, Faye Swift
  and Nora Butterfield. Four require plants; the postman delivers a letter.
  Positive terminal is the closed-shop state followed by the first night/card
  handoff, before Saturday's live requests. The evidenced route also visits
  C20, M21 and G5; only the necessary request sequence is the native closing
  gate, not an invented requirement to make every optional trip.
- Failure and retry: a wrong offer leaves its request unresolved and raises
  dread. The first full meter interrupts with a broken-plate reconstruction;
  completing it clears dread and resumes retained shop work. The first-recovery
  module stops at that return; deliberately repeating failure into the later
  alternating locket puzzle is outside this scope. Sources disagree about
  day restart and exact error-count wording; favour the recovery-specific
  description, corroborating independent review and observed retained progress,
  not the general guide's restart claim. No native threshold, token count,
  snap tolerance or reload experiment is certified.
- Included: partial botanical entries and close inspection; fixed but initially
  unconfirmed specimen identities; non-authoritative editable labels; current
  recipient and request matching; retained shelf stock and authored rewards;
  drawer letters and page collection; grid-map clue interpretation and visit
  outcomes; the full exploration-gauge gate, passive refill, watering and
  scripted refill; error accumulation and first restorative plate assembly;
  untimed shop decisions, independently running beneficial recharge and the
  authored night transition.
- Excluded: demo instant-loss behaviour; Switch, Xbox, macOS and mobile input
  parity; Strange Antiquities; later plant-powered gates, viewing device,
  Bryer's Disk, secret drawer cipher, elixir equipment, branching ritual and
  endings; repeated locket recovery; a complete 77-plant catalogue; campaign
  all-achievements, profit simulation, cash, finite sale stock, customer wait
  timers, plant thirst/death, hidden coordinates and exact recharge equations.
  Petting Hellebore is acknowledged presentation, not a fabricated causal gene.
- Potential scoped modules: a later multi-tool exploration packet; the elixir
  recipe/branch system; alternating recovery challenges; ending-route choice.
- Direct-play status: no native executable or personal gameplay. Primary
  creator explanations and official product material establish identification,
  inspection and map design. A release-period Steam route, independently
  written day guide and twelve static PC-labelled storyboard sheets establish
  the whole first day; nine additional static recovery sheets corroborate the
  first plate and return to a retained later-day shop. That later footage is
  recovery evidence, not proof of a first-day native experiment. No streamed
  video, audio playback, foreground window or focus change was used.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `SH-001` | The released Windows product uses partial botanical references, close inspection and map deduction; the original release is 21 January 2022. | Observation | Direct | High | P1, P2, P3 |
| `SH-002` | Friday has four plant requests interleaved with one postal visit; correct offers award specified knowledge or stock. | Observation | Corroborated | High | S1, S2, V1 |
| `SH-003` | Offering tests a retained specimen's identity rather than consuming one finite sale unit; a wrong offer leaves the visitor unresolved. | Observation | Corroborated | High | V1, P3, S3 |
| `SH-004` | Reference possession, physical specimen possession, tentative label and confirmed identity are distinct; close inspection adds descriptive traits. | Observation | Corroborated | High | P2, P3, V1, S4 |
| `SH-005` | Clues select map squares; a ready gauge funds a visit, and watering or waiting renews exploration readiness. | Observation | Corroborated | High | P2, S1, S3, V1 |
| `SH-006` | C20 supplies two entries, M21 Storian, G5 Lady of Summer; the postal letter supplies readiness. | Observation | Corroborated | High | S2, S3, V1 |
| `SH-007` | The first full dread state invokes plate assembly; successful recovery returns to retained shop work. | Observation | Corroborated | Medium | S5, S6, V2 |
| `SH-008` | General sources conflict on restart and exact error count; native build/threshold and later locket mechanics are not independently tested here. | Observation | Conflicting | Medium | S3, S5, S6, V2 |
| `SH-009` | Closure follows the required visitors, with night/card progression and no forced real-time customer deadline. | Observation | Corroborated | High | V1, S1, S7 |
| `SH-010` | First-recovery plate fitting and main-day progression are different objectives; the beneficial recharge does not create a shift deadline. | Observation | Corroborated | High | V1, V2, S5, S7 |

## Basic data

- Release / origin: Bad Viking; published by Iceberg Interactive, Windows full
  release on 21 January 2022. Later platforms are not silently treated as the
  current analysis target. The creator cites Sherlock Holmes: Consulting
  Detective as a map-clue influence, not a mechanically identical predecessor.
- Platform or physical form: Windows Steam, full release, English, one player.
  Structured target: `knowledge/platforms/games.json`, `PLAT-WINDOWS-PC`.
- Puzzle family: hidden-state inference; knowledge and evidence progression;
  spatial assembly and packing for the causally included first recovery.
- Primary sources:
  - P1: [official Steam product](https://store.steampowered.com/app/1574580/Strange_Horticulture/),
    release date, Windows target and encyclopedia/exploration premise;
    [official game site](https://www.strangehorticulture.com/).
  - P2: [Rob Donkin, creator interview, 15 March 2022](https://www.gamedeveloper.com/design/finding-right-plant-job-strange-horticulture),
    partial diagrams, distinguishing traits, close-inspection descriptions,
    authored map squares and the board-game influence.
  - P3: [Rob Donkin, creator's Xbox Wire article](https://news.xbox.com/en-us/2023/08/04/strange-horticulture-a-detective-game-about-plants/),
    plant/request deduction and relational map clues. Its Xbox publication is
    creator testimony, not a claim that Xbox input was analysed.
- Secondary sources:
  - S1: [Day by Day Walkthrough, release-period Steam guide](https://steamcommunity.com/sharedfiles/filedetails/?id=2727297761),
    Friday sequence. Direct retrieval was rate-limited; the public text view
    was read without bypass. The repeated syndicated walkthrough copies are
    not counted as independent confirmations.
  - S2: [Day 1 guide](https://strange-horticulture.fandom.com/wiki/Day_1),
    rewards and distinction between Ambleside's entries and actual plants.
  - S3: [Getting Started](https://strange-horticulture.fandom.com/wiki/Getting_Started),
    public indexed text for inspection, labels, exploration and recovery. Its
    restart assertion conflicts with the more specific recovery evidence.
  - S4: [contemporary Steam Deck account](https://www.digitaltrends.com/gaming/steam-deck-verified-op-ed/),
    manual label typing and optional auto-label. It supports the label
    distinction, not native Windows hardware reproduction.
  - S5: [Rising Dread](https://strange-horticulture.fandom.com/wiki/Rising_Dread),
    recovery-specific procedure and retained-state return; hidden token
    numerics are not treated as native measurements.
  - S6: [independent account of retrying the current customer](https://forgepress.org/strange-horticulture-review-a-plant-puzzle-game-that-channels-your-inner-sherlock/),
    first plate recovery, not a claim to have reset the whole workday.
  - S7: [day-duration discussion](https://steamcommunity.com/app/1574580/discussions/0/3734079155595776710/),
    untimed visitor work, cross-checked against the complete observed route.
  - V1: [PC-labelled first-day walkthrough](https://www.youtube.com/watch?v=6mtfSSBvtJI),
    998-second recording; 12 static sheets, 320×180 cells at ten-second steps,
    all inspected from introduction through the first night card. Later
    captions/editorial prompts are not game interface. No audio was used.
  - V2: [released-PC recovery observation](https://www.youtube.com/watch?v=Ebfj85-XX8U),
    2,157-second recording; nine static sheets, 160×90 cells at ten-second
    steps. Plate assembly appears around 27:50–31:50 and returns to the
    retained shop before the subsequent nightly transition. Facecam is not
    part of the game. Small frames cannot establish exact timing equations.
- Claim IDs: `SH-001`–`SH-010`.

## Mechanical decomposition

### Action Genes

- Existing gene IDs: `ACT-070` selects, orients and fits plate pieces in the
  first-recovery target; continuous angular/placement tolerance is a parameter,
  not an assumption of an inbento grid. `ACT-087` applies the acquired watering
  can to eligible shelf plants. `ACT-089` collects addressed notes/pages, not
  automatic character rewards. `ACT-107` receives actionable recipient facts.
- Candidate genes: accepted `ACT-751` retained-specimen offer, `ACT-752`
  editable non-authoritative label and `ACT-753` priced grid-map visit.
- Parameters: specimen, request, label text/colour, addressed paper, tool target,
  grid square and current first-recovery piece/orientation.
- Claim IDs: `SH-002`–`SH-008`.

### System Behaviour Genes

- Existing gene IDs: `none`.
- Candidate genes: accepted `SYS-1603` offer settlement and rewards;
  `SYS-1604` dread interruption/recovery; `SYS-1605` exploration-gauge cycle.
- Resolution order: offer submission → identity predicate → confirmation and
  authored reward or unresolved request plus dread → recovery if full; visit
  commitment → readiness spend → selected-square encounter; recovery assembly
  completion → dread cleared and retained shop resumed.
- Parameters: authored visitor/reward sequence, gauge cap, eligible refill,
  error threshold and geometric recovery tolerance. No exact refill constants.
- Claim IDs: `SH-002`, `SH-003`, `SH-005`–`SH-008`.

### Constraint Genes

- Existing gene IDs: `none`.
- Candidate genes: accepted `CON-821`, current recipient's specimen predicate
  and unresolved-script gate. Full-gauge visit eligibility is explicit within
  the exploration cycle; no terminal travel-supply constraint is imported.
- Scarce strategic resources: renewable exploration readiness and bounded dread
  tolerance; neither money nor depleting plant stock is invented.
- Claim IDs: `SH-003`–`SH-008`.

### Information Genes

- Existing gene IDs: `INF-003`, already fixed but not yet confirmed specimen
  identity and undiscovered location results.
- Candidate genes: accepted `INF-530`, growing reference with partial botanical
  illustrations and inspected traits; `INF-531`, named grid map with retained
  relative-location correspondence.
- Claim IDs: `SH-001`, `SH-004`–`SH-006`.

### Objective Genes

- Existing gene IDs: `OBJ-004`, reconstruct the first recovery plate.
- Candidate genes: accepted `OBJ-305`, satisfy the fixed first-day service
  sequence through closure and its nightly clue.
- Success, evaluation and failure: Victoria accepts St John's Poppy; Gilbert
  trades Phennet for Lemon Dandy; Faye accepts Forest Camphry; Nora accepts
  Wandering Bue. The postman is a fifth visitor, not a fifth plant order.
  Correctly naming a label alone is not completion. The first plate objective
  is conditional on failure, not an obligatory detour in a clean run.
- Claim IDs: `SH-002`, `SH-007`–`SH-010`.

### Time Genes

- Existing gene IDs: `TIM-002` for self-paced request reasoning and plate
  fitting, `TIM-003` only for the independently running exploration recharge
  while input remains available. These attach to distinct processes: the
  passive gauge is not a forced customer, health, plant-growth or shift clock.
- Candidate genes: `none`.
- Claim IDs: `SH-005`, `SH-009`, `SH-010`.

## Reproducible transitions

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Victoria awaits her first request | Offer the accepted red flower | Confirmation and Clavilium entry; shelf specimen retained | Request, label and finite stock are different | SH-002, SH-003 |
| A pot bears a wrong personal name | Submit it for an incompatible request | Request stays unresolved and dread grows | Text annotation is not authoritative identity | SH-003, SH-004 |
| Simone's letter is available | Visit C20 with full readiness | Gilded Dendra and Wandering Bue entries join the reference, not two granted plants | Knowledge is not specimen possession | SH-004, SH-006 |
| Amos's first letter arrives | Open it; interpret its woodland directions | Exploration becomes ready; G5 yields Lady of Summer | Receipt and relative coordinate deduction | SH-005, SH-006 |
| The drawer's hill clue is retained | Select M21 when ready | Storian joins the collection | New stock need not already have an entry | SH-005, SH-006 |
| A completed trip empties readiness | Try another trip, then wait or water | Travel remains gated until ready; shop reasoning continues | Renewable gate, not daily trip quota | SH-005 |
| First full dread interrupts work | Fit and rotate the plate pieces | Complete assembly clears dread and returns to retained work | Restorative puzzle rather than terminal loss | SH-007, SH-008 |
| Nora's final request is accepted | Leave the closed shop for night | First daily clue/card appears before Saturday | Native closure is not every optional trip | SH-009 |

## Strategic and experiential structure

- Local decision: discriminate the actual specimen by more than a matching
  colour or incomplete sketch. A personal label is memory assistance, not proof.
- Medium-term planning: acquire reference entries, retain letters and allocate
  ready map visits while watering or reasoning during refill.
- Long-term structure: the successor clue opens later investigation, excluded
  here. Owning a page before a plant is a useful knowledge/inventory separation.
- Common heuristics: inspect before guessing, keep tentative labels distinct
  from confirmed feedback and read the complete relative map clue.
- Failure attribution: errors give direct rejection and visible dread; the
  restorative first puzzle preserves progress rather than erasing the herbarium.
- Player-trust factors: no forced customer deadline; source disagreement is
  recorded rather than replaced with a fabricated native test.
- Claim IDs: `SH-002`–`SH-010`.

## Replay and variation

- What changes between sessions: chosen trip order, personal labels, shelf
  arrangement, mistakes and optional recovery. The first visitor list is fixed.
- Randomness or procedural generation: no invented random first-day plant
  identities, customer substitutions or published recovery seed.
- Multiple viable strategies: reorder eligible trips or wait/water around the
  same service sequence. Optional M21/G5 collection is not a closing quota.
- Typical replay motive: cleaner deduction and alternate later branches; no
  claim that the entire campaign was independently replayed.
- Claim IDs: `SH-002`, `SH-005`–`SH-010`.

## Adjacent systems and history

- Direct predecessors: the creator names Sherlock Holmes: Consulting Detective
  for map clues. Fictional plant properties let identification differ from an
  external botany exam.
- Variants: demo, console/mobile controls and Strange Antiquities are excluded.
- Similar games: only mathematically selected prior signatures below receive
  detailed comparison; shared shop theme is not similarity evidence.
- Important differences: no finite sale stock, delayed document-verdict audit,
  player-authored labels as ground truth or mandatory real-time waiting penalty.
- Claim IDs: `SH-001`, `SH-003`, `SH-004`, `SH-009`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-070`, `ACT-087`, `ACT-089`, `ACT-107`, `ACT-751`, `ACT-752`, `ACT-753` | specimen, label, coordinate, first plate piece |
| System Behaviour | `SYS-1603`, `SYS-1604`, `SYS-1605` | authored reward, dread, renewable readiness |
| Constraint | `CON-821` | accepted current request |
| Information | `INF-003`, `INF-530`, `INF-531` | reference entry, trait, letter, map |
| Objective | `OBJ-004`, `OBJ-305` | conditional first recovery; complete service day |
| Time | `TIM-002`, `TIM-003` | untimed decisions alongside passive beneficial refill |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `553` (`GAME-0001`–`GAME-0553`).
- Exact genome matches: none.
- Tied near matches: `GAME-0085` — The Room (`3 / 26 = 0.115385`).
- Supported combination subsets: none.
- Scan date: 2026-11-19.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0085` — The Room | `ACT-087`, `INF-003`, `TIM-002` | Both inspect authored concealed facts and apply acquired objects without a deadline. The Room reconfigures a key, lens and constrained safe mechanisms; Friday tests retained plants against recipient identities, keeps editable non-authoritative labels and spends renewable readiness on map clues. Its optional recovery does not turn the shop into the safe’s enclosure objective. | Tied near; `3 / 26 = 0.115385` |

- New genes: ten accepted additions; no old definitions or signatures change.
- Classification result: `New gene`.
- Evidence and reasoning: the complete prior-signature and combination scan
  separates identity-based reusable offers, labels, reference knowledge and
  optional restorative failure from a shop genre label.

### Preserved research notes

- New genes: ten accepted additions; no old definitions or signatures change.
- Classification result: `New gene`.
- Evidence and reasoning: the complete prior-signature and combination scan
  separates identity-based reusable offers, labels, reference knowledge and
  optional restorative failure from a shop genre label.

## Taxonomy impact

- Registry changes: `ACT-751`–`ACT-753`, `SYS-1603`–`SYS-1605`, `CON-821`,
  `INF-530`–`INF-531`, `OBJ-305`.
- Taxonomy-change record: [TAXONOMY_CHANGE_300](../../../research/taxonomy-changes/TAXONOMY_CHANGE_300.md).
- Candidate terms affected: retained-specimen offer, personal label, priced map
  visit, botanical comparison, renewable travel readiness and restorative dread.

## Negative results

- No separate record. Explicit rejected reuse boundaries are recorded in the
  taxonomy decision; no earlier signature is revised under this unit.

## Delta summary

The following compact ledger records changes rather than restating the analysis.

## New facts

- [Observation | Corroborated | High] Friday separates reference pages, physical
  plants, personal labels and accepted request identities; SH-002–SH-006.
- [Observation | Conflicting | Medium] Recovery-specific evidence supports
  retained work; broader restart wording is not silently accepted; SH-007–SH-008.

## New genes

- [Observation | Corroborated | High] Ten additions isolate the reviewed
  boundaries; the first recovery retains its Medium confidence qualification.

## New combinations

- [Observation | Corroborated | High] No new combinations; no proper verified subset.

## Taxonomy changes

- [Observation | Corroborated | High] TAXONOMY_CHANGE_300 adds definitions only.

## New questions

- [Hypothesis | Limited | Medium] A later native-build experiment could measure
  refill timing, exact dread increments and restore retention field by field;
  differing executable behaviour would reject the unmeasured assumptions.

## Next recommended game

- [Hypothesis | Limited | Medium] Chibi-Robo!, GAME-0555, European GameCube.
- Optimisation criterion: preserve the approved mixed-platform sequence.
- Expected information gain: household traversal and an actual energy budget
  after an untimed evidence-led shop.
- Backlog impact: preserve every remaining Selection 044 subject.

## Why this game

- [Hypothesis | Limited | Medium] A recent Windows detective loop extends
  knowledge/inventory separation without another consecutive retro action game.
