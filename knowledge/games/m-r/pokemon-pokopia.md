---
game_id: GAME-0518
slug: pokemon-pokopia
game_title: Pokémon Pokopia
analysis_status: reviewed
reviewed: 2026-11-16
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-089
    - ACT-123
    - ACT-131
    - ACT-162
    - ACT-341
    - ACT-408
    - ACT-712
    - ACT-713
  system:
    - SYS-353
    - SYS-752
    - SYS-1472
    - SYS-1473
    - SYS-1474
    - SYS-1475
    - SYS-1476
  constraint:
    - CON-282
    - CON-297
    - CON-797
  information:
    - INF-503
  objective:
    - OBJ-293
  time:
    - TIM-022
    - TIM-025
---

# Game: Pokémon Pokopia

Use the [canonical vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
Move names, species, recipe quantities, input buttons and the opening region
are parameters.

## Analysis scope

- Version / ruleset: English Nintendo Switch 2 released base game, fresh
  ordinary single-player story. Publisher and March 2026 route evidence
  establish the public release and opening rules. Nintendo lists update
  1.0.1 before the March 5 release. The exact binary used by each guide and
  exact precision, costs and timing of move and spawn internals are unverified.
- Structured analysis target: `PLAT-NINTENDO-SWITCH-2`, base game.
- Primary decision loop: address a resident or an affected terrain feature,
  select and apply a learned move, and inspect a habitat when the site
  signals an arrival. Use the resulting resident, materials or learned move
  to resolve the next request. Build and place the first campfire, then
  bring a resident with the compatible specialty to light it.
- Entry and exit: first free movement as Ditto in Professor Tangrowth's cave
  after appearance selection, through the first campfire and overnight
  transition. Stop upon regaining control after the introductory night,
  before following the Professor to the Pokémon Center PC.
- Included: Pokédex pickup, local movement and contextual interactions,
  Squirtle's rescue, Water Gun, Leafage, recovering and growing vegetation,
  basic tall-grass habitat recognition and occupancy, inspect-to-meet,
  assigned request order, one berry gift, replenishable move points, local
  material collection and Stockpile, chair placement and sitting, workbench
  crafting, Charmander follow and ignition, and handoff to the ordinary clock.
- Excluded: initial appearance editing, Pokémon Center services,
  environment-level and comfort progression, later construction and terrain
  powers, wider habitats and spawn tables, other regions, events, DLC,
  multiplayer, clock manipulation and later patch-specific additions.
- Potential scoped modules: opening Center reconstruction, construction
  specialties, and changing regional humidity in the next chapter.
- Direct-play status: reconstructed from the Nintendo product and update
  records, the publisher's release material and independently written
  walkthroughs. No console, executable, video or audio was played.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| PP-001 | The released English base game launched for Nintendo Switch 2 on March 5, 2026. Update 1.0.1 is listed March 3. | Confirmed | Direct | High | P1, P2, P3 |
| PP-002 | Addressing dried-out Squirtle makes Water Gun available. Aimed watering revives it and restores eligible withered vegetation. Responding to restored tall grass discloses Bulbasaur. | Observation | Corroborated | High | P2, R1, R2, R3 |
| PP-003 | Restore ten dry tall-grass patches after Bulbasaur's request and report back to learn Leafage. Switch between learned moves. Leafage adds tall grass on suitable grass ground. | Observation | Corroborated | High | P2, R1, R2, R3, R4 |
| PP-004 | Four joined living tall-grass patches support the opening habitat. Assignment of Squirtle to a new site and the arrival of Charmander at another site are different outcomes. An arrival signal calls for inspection to meet the Pokémon. | Observation | Corroborated | High | P2, R1, R2, R3, R4 |
| PP-005 | A restored Leppa tree can yield berries when headbutted. Give one to a named resident for the request or use a carried berry to recover move points. Stockpile brings eligible loose items or furniture into inventory. | Observation | Corroborated | High | R1, R2, R3, R4 |
| PP-006 | Place the received chair near Tangrowth and sit. Follow Bulbasaur to the workbench, which introduces recipes. One Sturdy Stick and one Stone craft the first Campfire. Place it near Tangrowth. | Observation | Corroborated | High | R1, R2, R3, R4 |
| PP-007 | During the fire request, meet Charmander in another Tall Grass habitat, ask it to follow, and bring it to the installed campfire. Its specialty supplies fire on approach. | Observation | Corroborated | High | R1, R2, R3, R4 |
| PP-008 | The chair interaction is an authored evening transition in this opening. Following the campfire sequence, the first overnight handoff sets ordinary play to the console's time. | Observation | Corroborated | High | P2, R1, R2, R3 |
| PP-009 | The exact delay, spawn weighting, geometry beyond the confirmed four-patch opening layouts and patch-level differences are unverified. | Observation | Limited | High | P3, R1, R2, R3, R4 |

## Basic data

- Release / origin: Nintendo and The Pokémon Company, March 5, 2026.
- Platform or physical form: Nintendo Switch 2 English base game.
- Puzzle family: ordered dependency sequencing, inventory and fixture
  dependencies, and agent routing and coordination.
- Primary sources:
  - P1 [Nintendo US store product](https://www.nintendo.com/us/store/products/70010000107421/),
    platform, distribution and date.
  - P2 [The Pokémon Company launch release](https://press.pokemon.com/en-CA/Create-Your-Own-Pokemon-Paradise-with-Pokemon-Pokopia-Available-Now)
    and [product overview](https://www.pokemon.com/uk/pokemon-video-games/pokemon-pokopia),
    environmental moves, habitats, crafting and day/night.
  - P3 [Nintendo update history](https://en-americas-support.nintendo.com/app/answers/detail/a_id/71348/~/how-to-update-pok%C3%A9mon-pokopia),
    chronology only.
- Independent practical evidence:
  - R1 [Thonky opening route](https://www.thonky.com/pokemon-pokopia/beginning-the-game),
    dated March 20, with input, recipient, inventory, recipe and handoff checks.
  - R2 [PokopiaDex opening walkthrough](https://pokopiadex.com/guides/opening-walkthrough-for-pokemon-pokopia-withered-wasteland),
    first residents, four-patch recipe, furniture, fire and clock handoff.
  - R3 [GameFAQs opening walkthrough](https://gamefaqs.gamespot.com/switch-2/559184-pokemon-pokopia/faqs/82556/game-beginning-tutorial-withered-wasteland-prelude),
    detailed opening transitions including the unlit campfire and proximity
    response.
  - R4 [Bulbapedia opening request index](https://bulbapedia.bulbagarden.net/wiki/Request_(Pokopia)#Withered_Wasteland),
    cross-check of recipient, sequence and request conditions.
- Claim IDs: PP-001–PP-009.

## Mechanical decomposition

### Action Genes

- `ACT-008` moves Ditto around the cave exit, plants, residents and workbench.
  `ACT-341` applies the contextual interaction to a resident, a marked patch,
  a tree, the workbench or the placed chair. The berry transfer uses the
  recipient's interaction and chooses a carried berry.
- `ACT-712` selects a known transformation move and targets an eligible local
  subject. Water Gun restores a dried subject. Leafage grows tall grass on
  eligible ground.
- `ACT-089` picks up an eligible loose material. `ACT-713` holds the suction
  command to collect nearby eligible items and reclaim movable furniture.
  `ACT-131` consumes a berry for move points instead of transferring it.
- `ACT-123` selects a known recipe. `ACT-162` places a carried chair or campfire
  at a supported local footprint. `ACT-408` recruits Charmander into temporary
  follow so Ditto can route it to the campfire.
- Claim IDs: PP-002–PP-007.

### System Behaviour Genes

- `SYS-1472` restores the existing viable state of a dry grass patch, flower,
  tree or eligible resident when the water reaches it. `SYS-1473` creates
  new foliage according to the base surface targeted by Leafage.
- `SYS-1474` recognises eligible empty habitat geometry and queues its
  opening encounter. A moving patch announces a waiting arrival and the
  inspect interaction reveals and registers the resident. Inviting an
  already encountered Squirtle settles its request without meeting it again.
- `SYS-1475` retains the learned move after the corresponding resident
  interaction, including Bulbasaur's request prerequisite, and presents it
  for future selection. `SYS-1476` spends available move points on supported
  transformations and restores them from consumed food such as a Leppa Berry.
- `SYS-353` turns accepted material inputs into a carried Campfire at the
  workbench. `SYS-752` routes Charmander behind Ditto and applies the Burn
  specialty when the follower comes close enough to the eligible fixture.
- Claim IDs: PP-002–PP-007.

### Constraint Genes

- `CON-282` orders the open requests. A placed campfire and an actual flame
  credit different milestones.
- `CON-297` checks the known recipe, available ingredients and workbench
  context before crafting. `CON-797` checks the arrangement and vacancy of
  a small habitat. The demonstrated Tall Grass pattern uses four connected
  living clumps. A same-level two-by-two arrangement supplies a reproducible
  positive case. This record does not assume a rule for every shape.
- Claim IDs: PP-003–PP-007, PP-009.

### Information Genes

- `INF-503` shows a visible local disturbance at an eligible habitat with a
  pending encounter. Inspecting settles the reveal. The grass motion
  supplies the place to inspect before the species is revealed in-world.
- Claim IDs: PP-002, PP-004, PP-007.

### Objective Genes

- `OBJ-293` restores a settlement's needed service by installing its fixture
  and bringing a compatible resident to make it work. The first-day endpoint
  is the attained warmth and overnight handoff after the prior requests.
- Claim IDs: PP-005–PP-008.

### Time Genes

- `TIM-022` moves the prelude from daytime to the authored evening and
  overnight transition after its required interactions.
- `TIM-025` marks the reachable handoff to the ordinary civil-time clock
  at first morning control. Later clock-linked availability is outside this
  scope.
- Claim IDs: PP-006, PP-008.

## Reproducible transitions

| Before | Action | Resolution | What it establishes | Claim |
|---|---|---|---|---|
| Ditto has just left the cave and finds dried-out Squirtle | Talk, learn Water Gun and aim it at Squirtle | Squirtle is restored and registered | Teaching and application are separate | PP-002 |
| The opening grass is dry | Rehydrate four joined clumps and wait for motion, then inspect | The Tall Grass site makes the Bulbasaur encounter available | A placement recipe, arrival cue and meeting are separate | PP-002, PP-004 |
| Bulbasaur has made the request | Restore ten dry tall-grass patches and report | Leafage joins the retained move choices | Reporting closes the measured world-state task | PP-003 |
| Squirtle asks for a home | Grow four joined clumps on another site, then address Squirtle | Squirtle moves into the eligible habitat | Housing a known resident differs from first discovery | PP-004 |
| A dry Leppa tree is nearby | Water the tree, headbutt it and collect a dropped berry | An inventory berry becomes available to eat or give | An alternative use competes with the accepted gift | PP-005 |
| The berry request is accepted | Give a berry to Squirtle or Bulbasaur, then talk to Tangrowth | Ditto obtains the chair and can place it nearby | The authored gift accepts two recipient options | PP-005, PP-006 |
| The chair is placed nearby | Sit, follow Bulbasaur and open the workbench | Evening begins and the first station recipes become available | The scripted day changes through actions | PP-006, PP-008 |
| The recipe is known and inputs are carried | Craft from one Sturdy Stick and one Stone, then install near Tangrowth | The accepted fixture is present but unlit | Crafting and ignition are separate | PP-006, PP-007 |
| A new Tall Grass site is ready in the fire request | Inspect the disturbance and ask Charmander to follow to the campfire | Charmander lights the fixture by proximity | The helper acts after routing, without a new Ditto move | PP-007 |
| The campfire is lit | Complete the closing evening encounter | Next control uses the ordinary console clock | Initial time and ordinary time have different owners | PP-008 |

## Strategic and experiential structure

Choose nearby connected sites and keep them distinct so a new habitat can
remain vacant. Water restores existing terrain, then Leafage lets Ditto
produce a compatible arrangement elsewhere. A berry can meet a request or
fund another set of move uses. A reachable campfire serves only when the
correct resident arrives. Moving the fixture closer can satisfy a placement
check without changing the recipe. PP-002–PP-008.

## Replay and variation

The taught moves, required requests and final fire outcome are authored.
Terrain sites, between-request collection, gift recipient and fixture
position can vary inside the stated constraints. Guides describe waiting
briefly for a habitat disturbance. Exact latency, probabilities and the
wider roster are unverified. PP-003–PP-009.

## Adjacent systems and history

Station work and a persistent civil clock recur in other settlement games.
The opening makes the local habitat an encounter selector and associates
different residents with capabilities. Player-aimed restoration, placement
geometry and routing a specialist operate at distinct stages. The selected
neighbour interpretation owns the measured comparison.

## Normalised genome

| Type | Active gene IDs | Parameters |
|---|---|---|
| Action | ACT-008, ACT-089, ACT-123, ACT-131, ACT-162, ACT-341, ACT-408, ACT-712, ACT-713 | Movement, collection, recipe, food, placement, interaction, follow, move and suction |
| System Behaviour | SYS-353, SYS-752, SYS-1472, SYS-1473, SYS-1474, SYS-1475, SYS-1476 | Recipe settlement, helper routing, revival, foliage, habitat arrivals, learning, move stock |
| Constraint | CON-282, CON-297, CON-797 | Request order, workbench prerequisites and habitat eligibility |
| Information | INF-503 | Habitat disturbance cue |
| Objective | OBJ-293 | Craft and make the campfire work with a compatible resident |
| Time | TIM-022, TIM-025 | Authored first day followed by console time |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `517` (`GAME-0001`–`GAME-0517`).
- Exact genome matches: none.
- Tied near matches: `GAME-0320` — Animal Crossing: New Horizons (`5 / 39 = 0.128205`).
- Supported combination subsets: none.
- Scan date: 2026-11-16.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0320` Animal Crossing: New Horizons | ACT-008, ACT-123, ACT-341, CON-297, TIM-025 | Both use local movement, context interactions and known station recipes, with ordinary play tied to the system clock. Animal Crossing opens public services by contributing to island progression. Pokopia restores or grows a spatial habitat, investigates its encounter and borrows a resident specialty to ignite the first fixture. | Near, `0.128205` |

## Taxonomy impact

- [TAXONOMY_CHANGE_265](../../../research/taxonomy-changes/TAXONOMY_CHANGE_265.md)
  records ten additions and thirteen unchanged transfers.

## Negative results

- The prelude asks for a basic Tall Grass habitat during the fire request.
  The selected route needs no tree-shaded species or later specialty.
- Eligible habitat creation, a queued encounter and invitation to occupy
  a new site are distinct. The route does not establish the exact general
  encounter roll or the full housing rules for larger structures.
- The installed first campfire needs the recruited helper. The scope
  excludes later fuel, power, construction or cooking rules and makes no
  claim about subsequent requests or an exact installed patch.

## Delta summary

## New facts

- [Observation | Corroborated | High] A reachable empty habitat makes a
  local encounter available. Inspecting the rustling site reveals the
  resident. The same basic habitat class serves a separately assigned
  home for a known resident. PP-002–PP-004, PP-007.
- [Observation | Corroborated | High] The first fire requires workbench
  production, local placement and a compatible follower. PP-006–PP-008.

## New genes

- ACT-712, ACT-713, SYS-1472, SYS-1473, SYS-1474, SYS-1475, SYS-1476, CON-797,
  INF-503 and OBJ-293.

## New combinations

- No new combination. See the computed subset scan.

## Taxonomy changes

- Ten reusable boundaries distinguish the habitat and tool acquisition loop.

## New questions

- Reproduce alternate connected habitat shapes, adjacency across different
  heights and the pointed watering footprint on a known release version.

## Next recommended game

- `GAME-0519` Power Stone, original Dreamcast release.

## Why this game

- [Hypothesis | Limited | Medium] Habitat gates couple environmental editing
  to resident capabilities and shift the solution away from acquiring only
  materials or recipes.
