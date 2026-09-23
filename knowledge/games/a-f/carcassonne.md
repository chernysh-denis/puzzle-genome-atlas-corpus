---
game_id: GAME-0369
slug: carcassonne
game_title: Carcassonne
analysis_status: reviewed
reviewed: 2026-09-23
combination_ids: []
gene_ids:
  action:
    - ACT-026
    - ACT-503
  system:
    - SYS-004
    - SYS-034
    - SYS-1003
    - SYS-1004
  constraint:
    - CON-056
    - CON-058
    - CON-669
    - CON-670
    - CON-671
  information:
    - INF-001
    - INF-002
  objective:
    - OBJ-002
  time:
    - TIM-004
---

# Game: Carcassonne

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Tile shapes,
colours, seven deployable meeples and scoring values parameterise the genes;
they are not separate universal mechanisms.

## Analysis scope

- Version / ruleset: the current Z-Man Games English **Carcassonne** main
  rulesheet and the Farmers section of its companion supplemental rulesheet,
  both linked from the publisher's product page and checked 2026-09-23. This
  packet is a standard **two-player** physical game with fields/farmers
  enabled. The 12 River tiles and Abbot mini-expansion are excluded; gardeners
  and abbot withdrawal never enter the action set. Exact manufacturing print
  run is uninspected.
- Structured analysis target: `PLAT-PHYSICAL-TABLETOP`, two-player original
  landscape rules plus the published farmer module, no digital port.
- Primary decision loop: inspect the connected public landscape, placed
  followers, scores and personal reserve; draw the next random facedown land
  tile; choose a legal adjacent cell and orientation whose touching edges all
  match; optionally place one supply meeple on an unoccupied road, city,
  monastery or field feature of that new tile; then settle every newly
  completed scored feature and return its ordinary meeples. Opponents alternate
  turns. Separately claimed features can later join, changing majority; a
  farmer stays on its field until endgame.
- Entry: place the dark-backed start tile at the centre. Remove 12 River
  tiles, shuffle the remaining 71 ordinary land tiles facedown, select two
  colours, give each player seven deployable meeples and put each eighth on
  the score track at zero. Use the published youngest-player starter rule;
  example trace may fix red as starter without asserting who is younger.
- Positive terminal: after the last drawable land tile has been placed, or
  remaining drawn tiles cannot legally be placed and are discarded by rule,
  settle incomplete roads/cities/monasteries and farmers' fields, compare
  totals, and the higher score wins. A tied top score shares victory.
- Negative terminal: the other player has a higher final total. An illegal
  edge or occupied-feature claim is simply rejected, not a game-over.
- Included: 72 non-River land tiles including the starting tile; random
  undisclosed draw; square-grid frontier, rotations and strict matching;
  optional one-meeple claim from finite reserve; separate-claim joining;
  completed road/city/monastery scoring, majority/ties and meeple return;
  incomplete-feature and distinct completed-city field scoring at the end.
- Excluded: River, Abbot and its garden/withdrawal powers, inns/cathedrals,
  other expansions, 3–5-player setup variants, tournament clocks, digital
  implementations, promotional tiles and invented deterministic tile order.
- Reproducible parameterisation: record each draw, legal coordinate and
  rotation, connected feature IDs before/after placement, optional claim,
  follower counts, completed-feature points, returns and remaining supply.
  A local source model exercises selected rule predicates, not an actual
  physical playthrough or a claim about random draw likelihood.
- Direct-play status: no physical copy, complete two-person session, photos,
  video or audio was obtained. Publisher rules and diagrams are direct rules
  evidence; the local transition control is only a reconstruction.
- Scope rationale: the complete 72-tile base landscape plus farmers is the
  smallest publisher-documented competitive packet that includes both
  immediate completed-feature returns and terminal contested field scoring.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| CC-001 | The current rules list 84 land tiles, including 12 River tiles; the non-River packet therefore has 72, one of which starts the board | Confirmed | Direct | High | P1, P2 |
| CC-002 | Two players use seven deployable meeples each and one score-track meeple | Confirmed | Direct | High | P2 |
| CC-003 | Each turn places one legally edge-matching tile, optionally claims one feature on it, then scores newly completed features | Confirmed | Direct | High | P2 |
| CC-004 | A follower cannot be placed on an occupied connected feature, but previously separate claimed features can later join | Confirmed | Direct | High | P2, P3 |
| CC-005 | Completed roads score one per tile; cities two per tile and emblem; monasteries nine when surrounded; highest follower count receives full points and tied high counts each receive full points | Confirmed | Direct | High | P2 |
| CC-006 | Scored ordinary followers return; farmers remain until final scoring | Confirmed | Direct | High | P2, P3 |
| CC-007 | Final incomplete road, city and monastery values differ from completed-city values; each field scores three per distinct adjacent completed city by farmer majority | Confirmed | Direct | High | P2, P3 |
| CC-008 | An impossible drawn tile is discarded and redrawn; tile exhaustion invokes final scoring, not immediate loss | Confirmed | Direct | High | P2 |
| CC-009 | Excluding River and Abbot while including farmers is a deliberate subset of the linked main and supplemental sheets, not a claim that the publisher calls farmers mandatory | Strong Pattern | Corroborated | High | P2, P3 |

## Basic data

- Release / origin: original Carcassonne design by Klaus-Jürgen Wrede,
  published by Hans im Glück; this packet uses the linked Z-Man Games English
  rulesheet rather than an uninspected historic print run.
- Platform or physical form: `PLAT-PHYSICAL-TABLETOP`, two people around one
  shared landscape and score track.
- Puzzle family: spatial assembly and packing; route/network construction.
  The design is competitive spatial construction, not a solo solved puzzle.
- Primary first-party sources, checked 2026-09-23:
  - **[P1]** [Z-Man Carcassonne product page](https://www.zmangames.com/game/carcassonne/),
    linking the current English rulebook and supplement.
  - **[P2]** [Z-Man English main rulesheet](https://cdn.svc.asmodee.net/production-zman/uploads/2024/09/carcassonne_v3_rulesheet_en-1.pdf),
    six PDF pages; used for setup, tile/meeple turn order, scoring, majority,
    forced discard and game-end reference.
  - **[P3]** [Z-Man English supplemental rulesheet](https://cdn.svc.asmodee.net/production-zman/uploads/2024/09/carcassonne_v3_supplement_en.pdf),
    two PDF pages; only page-one Farmers module admitted. Page-two River and
    Abbot rules are explicit exclusions.

## Mechanical decomposition

### Action Genes

- `ACT-026` chooses rotation and location for the mandatory drawn tile; the
  draw itself is random selection rather than player choice.
- New `ACT-503` optionally assigns one personal follower to a feature of the
  just-placed tile. An upright knight, traveler or monk and a lying farmer are
  parameterised uses of the same claim action.

### System Behaviour Genes

- `SYS-004` selects the next hidden tile. `SYS-034` joins compatible road,
  city and field components and checks completion after placement.
- New `SYS-1003` allocates completed road/city/monastery points by follower
  majority (full points to every tied leader) and returns those followers.
- New `SYS-1004` settles incomplete roads/cities/monasteries and farmers'
  fields at tile exhaustion. One completed city is counted at most once per
  touching field; scoring multiple distinct fields may count it separately.

### Constraint Genes

- `CON-056` restricts placement to the existing square landscape frontier;
  `CON-058` makes every touched road, city and field edge compatible.
- New `CON-669` checks the whole connected feature is follower-free **when
  claimed**. Later tile joins can create multiple followers on one feature.
- New `CON-670` limits claims to the player's seven available meeples; scoring
  returns ordinary pieces, whereas a farmer remains tied up until the end.
- New `CON-671` exhausts one unreplenished tile supply, with mandatory redraw
  only when the current tile has no legal placement.

### Information Genes

- `INF-001` exposes the current landscape, followers, score track and
  remaining visible personal reserves. `INF-002` withholds the order of
  facedown future tiles. Neither makes an unseen next tile previewable.

### Objective and Time Genes

- `OBJ-002` maximises the final score against the other player, including
  final farmers and incomplete features. `TIM-004` alternates decisions
  between adversarial players; there is no per-turn timer.

## Reproducible transitions

| Before | Action | Bounded resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Start tile in centre, 71 tiles facedown | Draw a land tile | Its identity becomes current; future order remains hidden | random finite supply | CC-001, CC-008 |
| Current tile touches a city edge | Rotate and place with city-to-city, road-to-road and field-to-field contact | The tile joins the connected board and updates affected features; mismatched edge is illegal | frontier and typed matching | CC-003 |
| New tile extends a road already carrying red | Try to place blue on that now-connected road | Claim is rejected, although the tile itself may stay placed | feature-wide exclusivity at claim time | CC-004 |
| Red-claimed road and blue-claimed road are separate | Bridge them with a later legal tile and complete the road | Both meeples now coexist; each has one of the tied-high counts and receives the full road value, then both return | join, majority/tie and reuse | CC-004, CC-005, CC-006 |
| A city is enclosed after placing its final tile | Count distinct city tiles and emblems | Leading claimant gets two per tile plus two per emblem, then ordinary meeples return | completed city value | CC-005 |
| A monastery gains its eighth surrounding tile | Settle completion | Its monk's owner receives nine points and the monk returns | adjacency closure | CC-005, CC-006 |
| Drawn tile has no legal position/orientation | Discard only that tile and draw again if possible | No elective skip or points; finite supply shrinks | forced redraw exception | CC-008 |
| No tiles remain; one incomplete city and one farmer field persist | Resolve endgame | Incomplete city gets one per city tile/emblem; field gets three per **distinct completed** city it borders, by majority | terminal scoring | CC-007, CC-008 |

## Strategic and experiential structure

- The tile itself may connect two rival claims that could not have been
  co-claimed directly. This makes future geometry a contest for majority,
  not a simple first-occupant ownership lock.
- Meeple commitment trades immediate possible return from a small completion
  against longer occupation of a large feature. Farmers cannot cycle back
  before the last draw, so field control consumes long-term reserve capacity.
- Scoring a city now differs from leaving it unfinished: two versus one point
  per tile and emblem. Fields pay only for adjacent **completed** cities.

## Replay and variation

- Draw order, legal placement choices, optional claims, feature joins and
  final city-field adjacency vary between sessions. The rules do not support
  predicting a future facedown tile or choosing a later one over the current.
- The scoped two-player packet is neither the first-game no-farmer tutorial
  nor the River/Abbot-inclusive expanded setup.

## Adjacent systems and history

- Dorfromantik shares mandatory frontier placement and terrain-component
  evaluation, but its quest-replenished solo stack has no adversarial
  followers, territorial majority or field endgame.
- Carto uses strict square-edge compatibility, but reorders map fragments
  for authored route discovery instead of scoring contested connected features.
- Azul has alternating hidden supply and visible scores, but drafts colours
  into private pattern lines; it does not grow one shared spatial topology.

## Normalised genome

| Type | IDs | Boundary |
|---|---|---|
| Action | ACT-026, ACT-503 | orient/place drawn tile, optionally claim its feature |
| System | SYS-004, SYS-034, SYS-1003, SYS-1004 | random draw, component join, completion award, final field/unfinished score |
| Constraint | CON-056, CON-058, CON-669, CON-670, CON-671 | frontier, edge matching, claim eligibility, follower reserve and tile exhaustion |
| Information | INF-001, INF-002 | public present, hidden future draw |
| Objective | OBJ-002 | maximise final points against rival |
| Time | TIM-004 | alternating turns |

This packet has 15 genes: nine reused boundaries and six new ones. Counts,
tile art, colours, starting player and exact random draws are parameters.

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `368` (`GAME-0001`–`GAME-0368`).
- Exact genome matches: none.
- Tied near matches: `GAME-0020` — Dorfromantik (`7 / 22 = 0.318182`).
- Supported combination subsets: none.
- Scan date: 2026-09-23.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0020` — Dorfromantik | `ACT-026`, `SYS-004`, `SYS-034`, `CON-056`, `CON-058`, `INF-001`, `OBJ-002` | Both orient mandatory drawn tiles at a matching frontier and update connected terrain. Dorfromantik's solo hex landscape can replenish its stack through quests and has previewed successors; Carcassonne's square landscape has no replenishment or preview, adds alternating rivals, scarce territorial followers, later majority contests and terminal farmer-field score. | Near, `0.318182` |

## Taxonomy impact

- `TAXONOMY_CHANGE_108` adds `ACT-503`, `SYS-1003`, `SYS-1004`,
  `CON-669`, `CON-670` and `CON-671` without rewriting earlier signatures.
  No verified combination follows from one new carrier.

## Negative results

- `CON-039` is not used: Carcassonne requires the current drawable tile, but
  **forced discarding** of an unplaceable one is explicitly legal; that gene
  excludes any discard. `CON-671` captures the qualified finite supply.
- `CON-059` and `SYS-035` are not used: placement cannot replenish the bag.
- `CON-020` is not used: exhaustion triggers scoring, not immediate failure.
- A farmer is not returned when a neighbouring city completes. Fields score
  only at game end. River, gardens and Abbot withdrawal are out of scope.
- The illustration is an original explanatory image, not a photographed
  physical game or evidence of an exact tile distribution.

## Delta summary

## New facts

- Separately legal territorial claims can merge later, so majority is
  determined at scoring rather than permanently at claim time.

## New genes

- `ACT-503` — optional new-tile follower claim.
- `SYS-1003` — completed-feature majority score and marker return.
- `SYS-1004` — unfinished-feature and field endgame settlement.
- `CON-669` — new-tile unoccupied-feature claim rule.
- `CON-670` — finite reusable follower reserve.
- `CON-671` — unreplenished shared tile exhaustion with forced discard.

## New combinations

- None; one carrier does not establish recurrence.

## Taxonomy changes

- One additive decision, with no prior signature, merge or lifecycle change.

## New questions

- Direct physical play could test long-range majority decisions and whether
  exact tile copies in a particular print run alter the frequency of forced
  discards. Neither is asserted here.

## Next recommended game

- None recorded. `GAME-0369` closes the selected nine-game horizon; await a
  new maintainer selection before any further unit.

## Why this game

- It contrasts hidden random input with fully visible spatial consequences:
  a tile changes feature topology, ownership and future scoring opportunities.

## Localisation review

- English rules and claim boundaries were frozen before Ukrainian
  presentation. The acceptance checkpoint records the side-by-side review of
  all touched fields; title and publisher remain official Latin names.
