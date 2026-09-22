---
game_id: GAME-0350
slug: jet-set-radio
game_title: "Jet Set Radio"
analysis_status: reviewed
reviewed: 2026-09-21
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-492
  system:
    - SYS-036
    - SYS-222
    - SYS-578
    - SYS-736
    - SYS-822
    - SYS-974
    - SYS-975
    - SYS-976
    - SYS-977
  constraint:
    - CON-068
    - CON-659
  information:
    - INF-268
    - INF-367
  objective:
    - OBJ-002
    - OBJ-204
  time:
    - TIM-003
---

# Game: Jet Set Radio

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Beat, Gum, Tab,
Shibuya GG, GGs, Love Shockers, Captain Onishima, spray cans, red arrows and
the `58411247` title identifier are carrier parameters, not gene names.

## Analysis scope

- Version / ruleset: licensed North American English Xbox Live Arcade release
  of Jet Set Radio for Xbox 360, title ID `58411247`, published by SEGA and
  released 2012-09-19. The current Xbox catalogue identifies the same product
  as developed by Blit and as an HD Heritage Collection release. The package,
  executable and title update were not downloaded, executed or hashed.
- Structured analysis target: one fresh New Game on
  `PLAT-XBOX-360`, from Gum's first imitation challenge through the complete
  Shibuya GG street stage and its result, stopping when Love Trap, The Monster
  of Kogane and Benten Boogie are available from the Garage.
- Primary decision loop: preserve speed through rails, walls, jumps and tricks;
  collect a finite spray reserve; choose an approach to each required red
  graffiti point; complete its size-dependent tag input while police pressure
  increases; repeat until every required point is replaced before time or
  stamina reaches zero.
- Entry: New Game has been selected on a fresh local profile and Gum's first
  demonstrated challenge is awaiting player control.
- Positive terminal: all ten required Shibuya GG graffiti points—four small,
  five large and one x-large—are complete, the stage result and rank have been
  shown, and the three named successor stages are available in the Garage.
- Negative terminal: the Shibuya GG Time Gauge or Stamina Gauge reaches zero
  before the ten required points are complete and the attempt enters Game Over.
- Included: Gum and Tab's six ordered imitation challenges; direct skate,
  steer, dash and jump; automatic rail and compatible-wall attachment; grind,
  wall ride, air and jump tricks; combo/score accumulation and collision break;
  one- and five-frame spray pickups; carrying and spending spray; small,
  large and x-large graffiti; directional command traces; ten required red
  points; time; stamina damage; police and captain escalation; current HUD,
  map support, stage result/rank and successor-stage availability.
- Excluded: the separate Tutorial menu and its lesson count; optional green
  tags; Graffiti Souls; exact Jet-rank score as a completion requirement;
  rival tagging; later districts and missions; campaign completion; test runs;
  custom graffiti editing; interviews; leaderboards; achievements; online
  services; Dreamcast save prompts; PlayStation, Windows and mobile packages;
  original Dreamcast executable behaviour not evidenced for the port; Jet Set
  Radio Future; later backward-compatibility presentation; cheats and mods.
- Reproducible parameterisation: complete Gum challenges 1–3 and Tab challenges
  1–3 in their documented order; enter the only initial Shibuya GG stage; use
  Beat; collect scattered yellow/blue cans as needed; tag all ten red points in
  any legal route while recording size, stock, directional trace, elapsed time,
  stamina, score/combo and police wave; accept the result and verify that the
  three named successors are selectable. The cited route tags the three large
  bus points first, which reproducibly triggers the first police arrival, but
  that route recommendation is not a mandatory ordering gene.
- Potential scoped modules: exact installed-title hash, direct Xbox 360 capture,
  frame/physics measurement, exact score and rank arithmetic, optional green
  tags, a later district, the separate Tutorial menu, test runs, achievements,
  Graffiti Souls, custom art and cross-platform parity each require a separate
  evidence packet.
- Direct-play status: not conducted. No Xbox 360, profile, download, executable,
  title update, save, controller trace, screenshot, video or audio was used.
  The repository control reconstructs the sourced state relations and does not
  run Blit's program or measure collision, momentum, input or scoring constants.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `JSR-001` | The selected product is SEGA's licensed 2012-09-19 Xbox Live Arcade Jet Set Radio HD release developed by Blit | Confirmed | Direct | High | P1, P2, P3 |
| `JSR-002` | Blit's final release is a hybrid port using original source code rather than evidence that every Dreamcast implementation detail is identical | Confirmed | Direct | High | P3, R1 |
| `JSR-003` | New Game opens with three Gum and three Tab imitation challenges that teach jumping, grinding, spray collection, graffiti tracing and chained rail traversal | Observation | Corroborated | High | S1, S2 |
| `JSR-004` | Street play requires the player to complete red graffiti points before either time or stamina reaches zero | Confirmed | Direct | High | P1, P4 |
| `JSR-005` | Yellow and blue pickups add one and five graffiti frames; larger points require more carried frames and large tags expose directional input commands | Confirmed | Direct | High | P4, S1 |
| `JSR-006` | Compatible rail/wall contact carries the skater through grind or wall-ride traversal, while jumps and tricks preserve or redirect route momentum | Observation | Corroborated | High | P1, P4, S1 |
| `JSR-007` | Tricks and graffiti add score, consecutive tricks form a temporary chain, and collision interrupts that chain | Observation | Corroborated | Medium | P4, S1 |
| `JSR-008` | Shibuya GG contains four small, five large and one x-large required tag; the documented x-large point costs seven cans | Observation | Corroborated | High | S1, S3 |
| `JSR-009` | Police arrive after the first three large bus tags and the captain appears during continued progress, adding movement, attack and damage pressure without changing the ten-point objective | Observation | Corroborated | High | S1, S3 |
| `JSR-010` | Completing all ten points produces a graded result and exposes Love Trap, The Monster of Kogane and Benten Boogie as successors | Observation | Corroborated | High | S1, S3 |
| `JSR-011` | The separate Tutorial menu, green tags, exact Jet threshold and later campaign are outside this packet | Confirmed | Direct | High | P4, S1, R1 |
| `JSR-012` | The repository control proves ordered introductions, attachment, trick-chain reset, spray legality, ten-point completion, pursuit escalation, failure and successor result | Observation | Direct | High | V1, JSR-003–JSR-010 |
| `JSR-013` | No package, executable, console, save or audiovisual trace was inspected | Confirmed | Direct | High | R1 |

## Basic data

- Release / origin: Xbox Wire records the Xbox Live Arcade release on
  2012-09-19. The current Xbox store identifies SEGA as publisher, Blit as
  developer and the product as an HD Heritage Collection edition of the
  Dreamcast-origin game.
- Platform or physical form: licensed North American English digital Xbox 360
  application, title ID `58411247`; current backward-compatible catalogue
  availability is product context, not a claim of Xbox One/Series rendering
  parity.
- Puzzle family: real-time system pressure; tactical forecast and counterplay;
  ordered dependency sequencing.
- Primary and creator sources, accessed 2026-09-21:
  - **[P1]** [current official Xbox product
    page](https://www.xbox.com/en-US/games/store/jet-set-radio/BVQL7V5TXBHB),
    for publisher/developer identity and the official tag, grind, trick,
    territory and police description.
  - **[P2]** [Xbox Wire release
    record](https://news.xbox.com/en-us/2012/09/19/arcade-jet-set-radio/),
    for the exact 2012-09-19 Xbox Live Arcade product and launch description.
  - **[P3]** [BlitWorks cofounder interview in Game
    Developer](https://www.gamedeveloper.com/production/what-exactly-goes-into-porting-a-video-game-blitworks-explains),
    for the original-source hybrid-port boundary.
  - **[P4]** [preserved original North American Jet Grind Radio instruction
    booklet](https://www.digitpress.com/library/manuals/dreamcast/jet_grind_radio.pdf),
    pp. 3–13, for the inherited Street rules, HUD, movement, grind/trick,
    spray-stock, graffiti-size and directional-input grammar. Local PDF
    SHA-256: `46dfae8335703ef21bac944e99b7604310ba1e81585cbccc8b2337718cfc7828`.
    It is an original-rules source used only where P3 establishes source-code
    inheritance and the Xbox route corroborates behaviour; it does not prove
    untested implementation parity by itself.
- Reproducible secondary sources, accessed 2026-09-21:
  - **[S1]** [EddeBaby's Xbox 360 Jet Set Radio guide on
    GameFAQs](https://gamefaqs.gamespot.com/xbox360/662136-jet-set-radio/faqs/10047),
    sections 9.01–9.03, for all six opening challenges, Shibuya count/size,
    stock, police/captain sequence and the three successor choices. Its stated
    Jet threshold is explicitly approximate and is excluded from completion.
  - **[S2]** [StrategyWiki's New Game tutorial
    route](https://strategywiki.org/wiki/Jet_Set_Radio/Tutorial), for an
    independently structured account of Gum and Tab's initial demonstrations.
  - **[S3]** [XboxAchievements Jet Set Radio HD achievement
    guide](https://www.xboxachievements.com/game/jet-set-radio-hd/guide/), for
    the first-story-stage identity and successor-stage availability after
    Shibuya GG.
- Reproducible control: **[V1]**
  [`verify_jet_set_radio_control.py`](../../../scripts/verify_jet_set_radio_control.py),
  an executable source-model control for the bounded state transitions.
- Research record: **[R1]** local preflight found no Xbox package, executable,
  title update, profile, save, screenshot, video, audio or controller trace.
- Claim IDs: `JSR-001`–`JSR-013`.

## Mechanical decomposition

### Action Genes

- `ACT-008` owns direct skate steering, dash, jump, air correction and approach
  to a graffiti point. Character, board, car and district are parameters.
- New `ACT-492` owns starting one eligible marked surface and completing its
  displayed directional graffiti trace. It does not absorb the system's paint
  debit, surface replacement or completion credit.
- `ACT-222` is rejected: it modifies a selected turn-based combat action,
  whereas this trace is a live world-surface action with stock and distance
  prerequisites.
- Claims: `JSR-003`, `JSR-005`, `JSR-006`.

### System Behaviour Genes

- `SYS-036` owns continuous gravity, collision and moving-body dynamics. New
  `SYS-974` separately owns attachment to a compatible rail/wall and carried
  traversal until jump, edge, loss of contact or collision.
- `SYS-222` owns contact pickup of eligible one- or five-frame spray cans.
  New `SYS-976` consumes size-dependent spray frames, evaluates any required
  command trace and progressively replaces only the addressed graffiti point.
- New `SYS-975` turns connected grind, wall, air and jump tricks into a
  temporary score chain and resets that chain on a terminating collision.
- `SYS-578` owns stamina damage and zero-state failure. New `SYS-977` turns
  required-tag progress into authored police waves whose actors pursue, shoot
  and damage the skater; it does not imply an omniscient generic patrol.
- `SYS-736` advances the six introduction predicates. `SYS-822` grades the
  completed street activity after objective settlement.
- Claims: `JSR-003`–`JSR-010`.

### Constraint Genes

- `CON-068` owns the authoritative Street deadline and terminal expiry.
- New `CON-659` requires an incomplete marked surface in range plus enough
  spray frames for its size before tagging can begin or finish. The size,
  cost and directional sequence are parameters.
- Character spray capacity is a parameter of the same stock legality, not a
  separate genome boundary in this one-character packet.
- Claims: `JSR-004`, `JSR-005`, `JSR-008`.

### Information Genes

- `INF-268` exposes one current Gum/Tab instruction and acknowledges the
  completed predicate before the next challenge.
- New `INF-367` joins live stamina, score, required-point state, time, spray
  stock, graffiti command and immediate pursuit/escape cues. A paused map can
  locate remaining untagged points without revealing future police routes.
- Claims: `JSR-003`–`JSR-005`, `JSR-008`, `JSR-009`.

### Objective Genes

- New `OBJ-204` requires every red graffiti point in the bounded street stage,
  accepts the result and ends at the declared successor-stage availability.
- `OBJ-002` separately owns voluntary score maximisation through clean tags,
  tricks, chains and time/stamina preservation. Neither Jet rank nor an exact
  score threshold is required for the positive terminal.
- Claims: `JSR-007`–`JSR-011`.

### Time Genes

- `TIM-003` owns the live interval in which the skater, moving vehicles,
  hostile pursuit, projectiles, time and stamina continue resolving.
- The result screen and Garage are settled states, not turns inside the Street
  decision loop.
- Claims: `JSR-004`, `JSR-006`, `JSR-009`.

## Reproducible transitions

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Gum challenge 1 is current | Reproduce the demonstrated jump onto the car | The predicate completes and Gum challenge 2 becomes current | staged imitation guidance | `JSR-003` |
| A compatible rail crosses the route | Jump or steer onto the rail | The skater attaches, grinds with carried motion and may jump/trick off | rail attachment is not generic free movement | `JSR-006` |
| A yellow or blue can is touched | Cross its pickup position | Spray stock rises by one or five frames, bounded by character capacity | spatial stock acquisition | `JSR-005` |
| A large red point is in range with fewer than three frames | Request graffiti | The action is rejected or cannot complete; the point remains required | size-dependent stock legality | `JSR-005`, `JSR-008` |
| A large red point is in range with sufficient stock | Start the tag and follow each displayed direction | Required frames are consumed, the surface is replaced, score rises and the point settles | authored input trace changes one objective surface | `JSR-005` |
| Two compatible tricks have remained connected | Contact a terminating obstacle | The temporary trick chain resets while accumulated stage score remains | local chain interruption | `JSR-007` |
| The third large bus point completes | Accept tag settlement | The first police wave arrives and begins pursuit pressure | objective progress escalates opposition | `JSR-009` |
| Continued required tags settle | Keep traversing and tagging | Captain Onishima joins the pressure while the same ten-point objective remains | staged pursuit does not replace territorial completion | `JSR-009` |
| Nine of ten required points are complete | Finish the last eligible red point before expiry | The street stage closes into results instead of continuing to demand score | exhaustive required-surface terminal | `JSR-008`, `JSR-010` |
| A required point remains and time reaches zero | Allow the authoritative clock to expire | Game Over replaces results and successor availability | exact negative deadline terminal | `JSR-004` |
| Results have settled | Accept the stage result | A rank is shown and Love Trap, The Monster of Kogane and Benten Boogie become available | graded completion with named successors | `JSR-010` |

## Strategic and experiential structure

- Local decision: decide whether current momentum reaches a required point,
  whether enough paint is carried and whether a command trace is safe under
  immediate pursuit.
- Medium-term planning: collect stock and clear expensive large/x-large points
  while police pressure is lower, then route between remaining points with
  rails, walls and vehicle geometry.
- Long-term structure: six teaching predicates compose into one timed district
  where movement quality, stock, objective progress, score and pursuit share
  the same continuous route.
- Common heuristics: refill before an expensive point, preserve movement
  through rail/jump transitions, do large points before stronger pressure and
  treat score rank as optional rather than a substitute for ten red tags.
- Failure attribution: HUD time and stamina distinguish two hard terminals;
  stock and prompt expose illegal tagging; required-point state exposes route
  incompleteness; collision visibly breaks a trick chain.
- Player-trust factors: one can must debit once, only the addressed surface may
  settle, a completed red point must stay complete, escalation must follow
  authored progress and all ten points—not an approximate score—must close the
  stage.
- Claims: `JSR-003`–`JSR-012`.

## Replay and variation

- What changes between attempts: route order, optional cans, attachment timing,
  trick chain, tag errors, damage, remaining time/stamina, score and rank.
- Randomness or procedural generation: district geometry, required points,
  challenge order and police milestones are authored. The packet makes no
  procedural-layout or random-tag claim.
- Multiple viable strategies: all legal routes must settle the same ten red
  points; the source route begins with buses to make escalation reproducible,
  but route order is not canonical.
- Typical replay motive: cleaner traces, longer chains, less damage, faster
  clear or a higher rank. The first ordinary completion remains sufficient.
- Claims: `JSR-005`–`JSR-010`.

## Adjacent systems and history

- Sonic the Hedgehog and Tony Hawk-derived traversal packets preserve momentum
  through authored geometry, but this route joins contact-bound rail/wall
  travel to a consumable directional surface-replacement objective.
- Graffiti-themed presentation alone is irrelevant. The admitted boundary is
  a marked, sized, stock-gated world surface whose trace completion changes
  territorial progress.
- Generic hostile pursuit does not explain why new law-enforcement roles enter
  after tag progress. `SYS-977` therefore owns the progress-to-wave relation;
  the individual actors' live motion and attacks remain carrier detail.
- Jet Set Radio Future is a different product with different graffiti and
  traversal rules and contributes no evidence to this signature.
- Claims: `JSR-001`–`JSR-013`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-492` | Beat, dash, jump and direction symbols are parameters |
| System Behaviour | `SYS-036`, `SYS-222`, `SYS-578`, `SYS-736`, `SYS-822`, `SYS-974`, `SYS-975`, `SYS-976`, `SYS-977` | rail, wall, spray, score, police roles and rank scale are parameters |
| Constraint | `CON-068`, `CON-659` | time, graffiti size, cost, range and capacity are parameters |
| Information | `INF-268`, `INF-367` | HUD layout, arrow art and map styling are presentation/parameters |
| Objective | `OBJ-002`, `OBJ-204` | ten points, stage name and successors are parameters |
| Time | `TIM-003` | live update cadence is a parameter |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `349` (`GAME-0001`–`GAME-0349`).
- Exact genome matches: none.
- Tied near matches: `GAME-0311` — Super Mario Bros. (`5 / 31 = 0.161290`).
- Supported combination subsets: none.
- Scan date: 2026-09-21.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0311` — Super Mario Bros. | `ACT-008`, `SYS-036`, `CON-068`, `OBJ-002`, `TIM-003` | Both packets make direct momentum-bearing movement and optional score live under a terminal stage deadline. Super Mario Bros. adds directional enemy contact, one-way camera progression, typed block rewards, temporary power states, finite lives and a flagpole exit. Jet Set Radio instead attaches the skater to rails/walls, collects and spends paint on directional surface traces, chains traversal tricks, retains stamina, escalates police from tag progress and requires all marked surfaces before a graded three-stage handoff. | Tied near, `5 / 31 = 0.161290` |

### Preserved research notes

- New genes: `ACT-492`, `SYS-974`, `SYS-975`, `SYS-976`, `SYS-977`,
  `CON-659`, `INF-367` and `OBJ-204`.
- Reused genes: `ACT-008`, `SYS-036`, `SYS-222`, `SYS-578`, `SYS-736`,
  `SYS-822`, `CON-068`, `INF-268`, `OBJ-002` and `TIM-003`.
- Classification result: `New genes`.
- Evidence and reasoning: lower-ID movement, pickup, health, tutorial, deadline,
  rank, score and live-time boundaries transfer clause by clause. None owns
  contact-bound rail/wall carriage, trick-chain interruption, size-dependent
  directional surface replacement, progress-triggered police waves or a
  complete required-graffiti-stage terminal.

## Taxonomy impact

- Registry changes: add eight Active boundaries and explicit Jet Set Radio
  carrier evidence to ten reused boundaries. No earlier game signature,
  verified combination or lifecycle changes.
- Taxonomy-change record:
  [`TAXONOMY_CHANGE_092`](../../../research/taxonomy-changes/TAXONOMY_CHANGE_092.md).
- Candidate terms affected: Jet Set Radio, Beat, Gum, Tab, Shibuya GG, GGs,
  Love Shockers, Captain Onishima, Xbox 360 and `58411247` remain product,
  actor, place, group, platform or identifier parameters.

## Negative results

- No direct play, package, executable, title update, console, save, screenshot,
  video, audio, controller trace or physics measurement.
- The original Dreamcast manual establishes inherited rules only where P3 and
  the Xbox 360 route corroborate them; it is not treated as byte-level parity.
- Exact Jet-rank score is rejected because the guide marks its boundaries as
  approximate and ordinary completion requires the red points, not Jet rank.
- The separate Tutorial menu is excluded; Gum and Tab's mandatory New Game
  challenges are included and must not be conflated with it.
- Green tags, Graffiti Souls, rival tagging, custom art, online services and
  later districts are not inferred from the bounded first-stage route.

## Delta summary

## New facts

- [Confirmed | Direct | High] The selected Xbox 360 release is a licensed Blit
  hybrid port that retains the original rule lineage without proving every
  implementation detail identical (`JSR-001`, `JSR-002`).
- [Observation | Corroborated | High] Six introductory challenges feed a
  ten-point Shibuya GG clear where spray stock, directional tags and police
  escalation share one live route (`JSR-003`–`JSR-010`).

## New genes

- [Observation | Corroborated | High] `ACT-492`, `SYS-974`, `SYS-976`,
  `SYS-977`, `CON-659`, `INF-367` and `OBJ-204`.
- [Observation | Corroborated | Medium] `SYS-975`.

## New combinations

- [Observation | Corroborated | High] No registered combination; recurrence
  requires an independently analysed game carrying a proper subset.

## Taxonomy changes

- [Observation | Corroborated | High] `TAXONOMY_CHANGE_092` records eight new
  boundaries and the complete lower-ID transfer test.

## New questions

- Does a separately bounded direct capture support a reusable exact
  score/rank arithmetic boundary beyond `SYS-822`?

## Next recommended game

- [Hypothesis | Corroborated | High] `GAME-0351` — Street Fighter II: The World
  Warrior.
- Optimisation criterion: test compact directional-command combat, hit states,
  round time and best-of-three settlement against the current fighting-game
  vocabulary.
- Expected information gain: separate original World Warrior command/state
  rules from later Street Fighter II revisions.
- Backlog impact: eighth of nine selected games completed; one unit remains.

## Why this game

- [Hypothesis | Corroborated | High] Street Fighter II replaces a city-scale
  route and stock-gated tagging with a symmetric two-actor arena whose entire
  product boundary can be tested inside one best-of-three match.
