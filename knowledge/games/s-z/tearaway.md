---
game_id: GAME-0426
slug: tearaway
game_title: Tearaway
analysis_status: reviewed
reviewed: 2026-09-27
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-564
    - ACT-565
  system:
    - SYS-1124
    - SYS-1125
  constraint: []
  information:
    - INF-418
  objective:
    - OBJ-026
  time:
    - TIM-003
---

# Game: Tearaway — uncover and use a paper drum route

Use the canonical [vocabulary and genome rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). The paper flap, drum position, messenger and upper landing are parameters, not additional genes.

## Analysis scope

- Version / ruleset: original 2013 PS Vita *Tearaway*, early traversal before the messenger independently acquires a jump. No cartridge or exact software revision was inspected. This is a source-bounded **analytical example**, not a claim that one named chapter contains a fixed peel-then-drum script.
- Structured analysis target: `PLAT-PLAYSTATION-VITA` in [`knowledge/platforms/games.json`](../../platforms/games.json).
- Primary decision loop: read a manipulable paper edge and a marked rear-touch drum; peel the covering paper with the front touchscreen to expose a bouncy surface; steer Iota or Atoi onto it; tap the corresponding rear touchpad area while the messenger stands there; use the launch to reach the upper path.
- Entry and exit: start at a paper-covered bouncy platform with the controlled messenger on the nearby lower route and both Vita touch surfaces available. End the bounded packet when the covering has been removed, the drum has launched the messenger and the messenger reaches an upper traversable paper surface. This is an analytical endpoint, not a game-authored completion screen or specified level coordinate.
- Included: direct messenger locomotion, front-touch peeling of a manipulable paper layer, newly exposed bouncy surface, rear-touch drum actuation conditional on messenger position, marked touch affordances, live trajectory and reaching the next surface.
- Excluded: exact chapter name or geometry, later unlocked ordinary jumping, enemies, camera/self-portrait, papercraft printing, decoration, confetti spending, tilt, microphones, full story delivery and PS4 *Tearaway Unfolded* controls.
- Potential scoped modules: timed folding bridges, rear-touch obstacle clearing or enemy protection, front-camera tasks, later jump ability and other authored routes.
- Direct-play status: no PS Vita, cartridge, executable, input trace or audiovisual play was inspected. Sony's contemporary hands-on and independent first-hand 2013 reviews support the component mechanics. Their combination into this one analytical packet is explicitly an inference; exact level placement, launch impulse, timing and failure reset are unmeasured.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `TEA-001` | The original game was designed for PS Vita and exposes rear-touch interactions through marked thin or transparent paper surfaces. | Confirmed | Direct | High | P1, P2 |
| `TEA-002` | A rear touchpad tap can beat a drum and launch Iota or Atoi upward; the messenger must occupy the drum surface for the useful launch. | Observation | Corroborated | High | P1, S1, S2 |
| `TEA-003` | A paper coating can be peeled back to reveal a bouncy area for the messenger. | Observation | Corroborated | Medium | S1, S3 |
| `TEA-004` | Early Iota does not yet have an independent jump; later jump ability is a different route capability. | Observation | Corroborated | High | S1, S2 |
| `TEA-005` | This particular peel → occupy → rear-tap → upper-surface sequence is a bounded analytical reconstruction, not a verified named in-game stage script. | Hypothesis | Limited | Medium | P1, S1, S3 |
| `TEA-006` | Manipulable paper tabs and rear-touch markings disclose different interaction surfaces rather than exact future landing coordinates. | Observation | Corroborated | Medium | P1, S4 |

## Basic data

- Release / origin: Media Molecule's original *Tearaway*, published by Sony Computer Entertainment for PS Vita in 2013.
- Platform or physical form: PS Vita handheld with front touchscreen, rear touchpad and direct control of Iota or Atoi; no PS4 controller substitution.
- Mechanical family: world topology and perspective (`FAM-014`): peeling a world layer exposes a usable route surface, then a located physical input changes traversability.
- Primary sources, accessed 2026-09-27: **P1** — [Sony PlayStation Blog, contemporary hands-on with *Tearaway*](https://blog.playstation.com/archive/2013/05/29/hands-on-with-tearaway-media-molecules-new-ps-vita-adventure), 29 May 2013; PS Vita rear-touch markings, drum launch and paper environment. **P2** — [Sony PlayStation Blog, original PS Vita launch notice](https://blog.playstation.com/2013/11/22/tearaway-out-today-on-ps-vita/), 22 November 2013; edition and release.
- Independent first-hand sources, accessed 2026-09-27: **S1** — [Josiah Renaudin, *Tearaway* review](https://gameranx.com/features/id/18851/article/tearaway-review-the-vita-s-greatest-adventure/), Gameranx, 20 November 2013; author states a publisher-provided review copy and describes early no-jump play, paper peel revealing bounce and drum launch. **S2** — [Blair Inglis, *Tearaway* preview](https://www.thesixthaxis.com/2013/10/25/tearaway-preview/), TheSixthAxis, 25 October 2013; first-hand early Iota cannot jump and rear touch bounce advances between platforms. **S3** — [Destructoid, hands-on *Tearaway* preview](https://www.destructoid.com/hands-on-ripping-into-vita-platformer-tearaway/), 2013; front-screen paper-layer peeling and rear touch. **S4** — [Matthew Diener, lead-designer walkthrough of early levels](https://www.pocketgamer.com/tearaway/e3-2013-media-molecules-rex-crowle-walks-us-through-the-first-levels-of-tearaway/), Pocket Gamer, 12 June 2013; rear drumming and visible movable paper tabs.

## Mechanical decomposition

### Action Genes

- Reused `ACT-008`: directly steer the one persistent messenger across the currently reachable paper surfaces; the early packet does not grant an ordinary player-initiated jump. `TEA-002`, `TEA-004`.
- New `ACT-564`: drag a visible paper-layer edge on the front touchscreen to peel it from its support and uncover what was beneath. The finger changes world material, not merely a menu selection. `TEA-003`, `TEA-006`.
- New `ACT-565`: tap the rear touchpad at a marked drum while the messenger is on that surface; this is a player-timed upward impulse, not automatic contact bounce. `TEA-001`, `TEA-002`.

### System Behaviour Genes

- New `SYS-1124`: peeling the covering paper changes the platform from covered to exposed, making its bouncy surface usable. The source supports reveal, not arbitrary terrain creation elsewhere. `TEA-003`.
- New `SYS-1125`: a valid rear touch at the occupied drum delivers its launch impulse to the messenger toward an upper surface. An unoccupied or unrelated touch does not establish this same messenger launch; independent airborne steering is not asserted from these sources. `TEA-002`.
- Resolution order: exposed paper edge → front-touch peel → bouncy drum becomes available → messenger is steered onto it → corresponding rear tap → upward trajectory and landing. This ordering is the bounded analytical construction (`TEA-005`), not a measured frame-by-frame trace.

### Constraint Genes

- No independent constraint added. The drum-contact and marked touch-location prerequisites belong to `SYS-1125`'s input predicate. No resource, cooldown, time limit or irreversible failed tap is evidenced for this packet.

### Information Genes

- New `INF-418`: a graspable paper tab/edge and symbol-marked thin surface distinguish the front-touch manipulation from the rear-touch drum site. They disclose an available interaction, not a guaranteed landing point. `TEA-001`, `TEA-006`.

### Objective and Time Genes

- Reused `OBJ-026`: the bounded spatial task ends at a reachable upper paper surface after making that route usable. This is an analysis endpoint, not an authored stage victory. `TEA-002`, `TEA-005`.
- Reused `TIM-003`: the messenger moves through a live platforming world while movement and touch inputs are accepted; no fixed countdown, airborne steering rule or timing-perfect drum window is claimed. `TEA-002`.

## Reproducible transitions

| Before | Action | Bounded resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Covering paper still hides the bouncy area | Drag a manipulable paper edge on the front screen | The layer peels back and the bouncy area is exposed | world material is an editable route precondition | `TEA-003`, `TEA-006` |
| Exposed drum is reachable but the messenger stands beside it | Steer Iota or Atoi onto the drum | The messenger now occupies the eligible launch surface | avatar position matters before rear touch | `TEA-002`, `TEA-004` |
| Messenger stands on the marked drum | Tap the corresponding rear touchpad region | The drum launches the messenger upward | manual rear input differs from automatic contact bounce | `TEA-001`, `TEA-002` |
| Messenger rises beside an upper paper surface | Complete the launched passage | The messenger can reach the chosen bounded landing area | the launch completes the route after world manipulation | `TEA-002`, `TEA-005` |
| Messenger has not reached the drum | Tap an unrelated rear region | No useful occupied-drum launch is established by the sources | do not infer a universal jump or whole-floor trigger | `TEA-002`, `TEA-005` |

## Strategic and experiential structure

- Local decision: distinguish the peelable edge from the rear-touch drum cue; open the surface before trying to use it and position the messenger on it.
- Medium-term planning: align the exposed launch surface with an upper traversable continuation. The exact layout and any further obstacles are outside this packet.
- Long-term structure: later ability unlocks and creative tasks change the broader story but are deliberately excluded.
- Common heuristic: read paper tabs and rear-touch symbols as affordances, then test the edited surface with the messenger before tapping the back.
- Failure attribution: a covered surface, off-drum messenger or wrong rear-touch region cannot be treated as evidence that the launch rule is absent. Exact recovery or checkpoint behaviour remains unmeasured.
- Player-trust factors: the visible paper edge and marked thin surface make the two modes legible; the successful peel and launch provide immediate local feedback, not exact future-trajectory information.

## Replay and variation

Different messenger choice, paper layout and landing geometry may vary across the full game. No procedural generation, exact jump arc, repeat-reset rule or fixed time limit is asserted for this analytical example. Other areas may combine touch interactions differently.

## Adjacent systems and history

*LittleBigPlanet 2* has automatic contact bounce pads (`SYS-1056`), whereas this packet requires an occupied PS Vita drum and a separate rear touch. *Carto* edits map-fragment adjacency, whereas *Tearaway* peels a physical world layer. *The Room* manipulates an object to reveal inner mechanisms; *Tearaway* turns a revealed paper surface into embodied traversal.

## Normalised genome

| Type | Active gene IDs | Key parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-564`, `ACT-565` | messenger, peel edge, rear-touch drum |
| System Behaviour | `SYS-1124`, `SYS-1125` | exposed surface, occupied launch, trajectory |
| Constraint | none | contact predicate incorporated in `SYS-1125` |
| Information | `INF-418` | paper tab and rear-touch marking |
| Objective | `OBJ-026` | bounded upper landing |
| Time | `TIM-003` | live avatar motion |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `425` (`GAME-0001`–`GAME-0425`).
- Exact genome matches: none.
- Tied near matches: `GAME-0098` — Hyperbolica (`3 / 12 = 0.250000`).
- Supported combination subsets: none.
- Scan date: 2026-09-27.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0098` *Hyperbolica* | `ACT-008` direct navigation, `OBJ-026` bounded location and `TIM-003` live traversal | *Hyperbolica* changes route intuition through non-Euclidean geometry and a fixed maze sequence; this Vita packet changes a paper layer and needs a separately rear-touched occupied drum before the upper surface is reachable. | Tied-near maximum, `0.250000`; not an exact or combination match. |

## Taxonomy impact

[`TAXONOMY_CHANGE_164`](../../../research/taxonomy-changes/TAXONOMY_CHANGE_164.md) admits two touch actions, paper reveal, conditional rear-touch launch and interaction markings. No earlier genome or verified combination is revised.

## Negative results

- `SYS-1056` rejected: *LittleBigPlanet 2* bounce pads launch by contact alone; the Vita drum needs a distinct rear touch while occupied.
- A later self-jump is excluded. The early review says Iota cannot jump independently at first.
- No level name, exact map, mandatory peel/drum ordering in an authored stage, exact impulse or time limit is verified.

## Delta summary

Front-touch paper peeling can reveal a bounce surface, while an occupied rear-touch drum can launch the messenger. The two mechanics are source-supported separately; their union here is a deliberately bounded route example, not a claimed literal chapter script.

## New facts

- [Observation | Corroborated | High] Original PS Vita rear-touch drumming launches Iota/Atoi, and early independent jumping is unavailable (`TEA-002`, `TEA-004`).
- [Observation | Corroborated | Medium] Peeling a paper coating can expose a usable bouncy area (`TEA-003`).

## New genes

- [Observation | Corroborated | Medium] `ACT-564`, `ACT-565`, `SYS-1124`, `SYS-1125` and `INF-418` isolate the two touch channels, reveal and launch boundaries.

## New combinations

- [Observation | Direct | High] None created; verified prior combinations are scanned against the complete signature.

## Taxonomy changes

- [Observation | Corroborated | Medium] `TAXONOMY_CHANGE_164` admits five new typed boundaries without revising prior signatures.

## New questions

- Which exact original-PS-Vita chapter first requires the peel-and-drum interaction together, and how does its geometry route the messenger?
- What are the measured rear-touch hit region, launch velocity and landing recovery in one inspected cartridge revision?

## Next recommended game

- [Hypothesis | Limited | Medium] `GAME-0427` *Alan Wake* only after this unit's full validation, one local commit and Goal stop window; retain the recorded selection order.
- Optimisation criterion: contrast tactile platform editing with a light-and-ammunition survival route.
- Expected information gain: different perception, resource and hostile-pressure boundaries.
- Backlog impact: no successor is started in this unit.

## Why this game

- [Observation | Corroborated | Medium] The original Vita input surface can turn paper manipulation into an available launch route, giving a distinct world-editing and movement packet while source limits remain explicit.
