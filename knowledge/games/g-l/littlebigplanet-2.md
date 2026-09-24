---
game_id: GAME-0394
slug: littlebigplanet-2
game_title: LittleBigPlanet 2
analysis_status: reviewed
reviewed: 2026-09-24
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-341
    - ACT-531
  system:
    - SYS-037
    - SYS-369
    - SYS-398
    - SYS-1055
    - SYS-1056
  constraint:
    - CON-349
    - CON-693
  information:
    - INF-179
  objective:
    - OBJ-026
  time:
    - TIM-003
---

# Game: LittleBigPlanet 2

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Sponge shapes,
Grappling Hook button, crafted scenery, prize positions and race time are
parameters, not separate genes.

## Analysis scope

- Version / ruleset: original English North American 2011 PlayStation 3
  *LittleBigPlanet 2* Story Mode. Examine a one-player ordinary route through
  the second, post-level-link part of Da Vinci's Hideout level *Grab and Swing*.
  The exact disc revision and installed patch were not inspected; no later
  edition, demo or community level substitutes for this described packet.
- Primary decision loop: inspect the visible layer, sponge anchor, switch,
  gap, electric surface and pad; navigate or activate an eligible fixture,
  then aim the newly acquired reusable Grappling Hook, steer a suspended
  swing, reel, release or land; recover height from bounce pads and continue
  through the authored route to its final flags.
- Entry: control resumes at the toilet immediately after the level link in
  *Grab and Swing*. The preceding block-pulling and hand-grab section has
  already occurred and is not counted in this signature.
- Positive terminal: cross the final race gate/flags and proceed through the
  level's exit, before control in the next story level. Merely crossing the
  intermediate level link or collecting a prize does not finish the packet.
- Negative terminal: contact with the electric floor or another lethal hazard
  ends the present attempt and returns the avatar through an authored
  checkpoint if a usable return remains. Exact checkpoint stock, restored
  collectibles and save persistence are not established by the sources.
- Included: moving and jumping between depth layers; the back-layer button
  that opens the door; receipt and repeated use of the hook; aiming at
  grabbable sponge or an eligible switch, adjusting tether length, steering
  and releasing; bounce-pad impulses; visible electric avoidance; optional
  prize-bubble contact; checkpoint return and the final race/exit route.
- Excluded: the level's first pre-link block and sofa puzzle, the other Da
  Vinci stages, two-player prize rooms elsewhere, exhaustive prize collection,
  Ace/score-maximisation, Create/Share and online community content, player
  costumes, DLC, later PS3 patches, PS Vita/PS4 sequels and full campaign
  settlement. The race's exact score formula and time limits are not asserted.
- Reproducible parameterisation: use original PS3 Story Mode, one player,
  reach *Grab and Swing* by normal story order, then start recording at its
  post-link toilet. Log depth layer, opened door, hook possession, targeted
  sponge/switch, line attachment and length, release, hazard contact,
  checkpoint and final flags. The exact successful route and item pickups
  may vary; do not count the level's first half in the analysed genome.
- Potential scoped modules: the pre-link *Grab and Swing* object-pulling
  section, a two-player prize room, one later grappling-heavy level and the
  creation editor require distinct entry, terminal and evidence packets.
- Direct-play status: none. No PS3 disc, executable, save, input trace,
  screenshot, video or audio was opened or analysed. Publisher statements
  establish the product and hook feature; two independent written walkthroughs
  reconstruct the specific post-link route. A game-specific checkpoint
  reference supports only its ordinary return role, not a precise life count.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `LBP2-001` | The original North American PS3 game released on 2011-01-18, and Story, Create and Share are distinct product parts. | Confirmed | Direct | High | P1, P2 |
| `LBP2-002` | Grappling Hook and Bounce Pads are official LBP2 features, but the official feature list alone does not locate them in this level. | Confirmed | Direct | High | P3 |
| `LBP2-003` | In the second part of Grab and Swing, a back-layer button opens a door before Da Vinci grants the hook. | Observation | Corroborated | High | S1, S2 |
| `LBP2-004` | The hook attaches to sponge, can reel in or out and supports steered swings and releases across gaps. | Observation | Corroborated | High | S1, S2 |
| `LBP2-005` | The hook can pull an eligible toilet switch to expose an optional item; ordinary scenery is not established as universally hookable. | Observation | Corroborated | High | S1, S2 |
| `LBP2-006` | The later route places an electric floor beneath swings, uses bounce pads for height, and ends after a rotating anchor and final flags. | Observation | Corroborated | High | S1, S2 |
| `LBP2-007` | Prize bubbles occupy optional main and hidden depth-layer positions, so a normal exit need not mean exhaustive collection. | Observation | Corroborated | High | S1, S2 |
| `LBP2-008` | An authored checkpoint occurs before the late grappling/race section; ordinary death returns to a checkpoint in LBP2, but this packet does not verify exact stock or restoration fields. | Observation | Limited | Medium | S1, S3 |
| `LBP2-009` | No original executable or direct route was inspected, and the written guides do not prove exact frame timing, score conversion or installed patch behaviour. | Observation | Direct | High | R1 |

## Basic data

- Release / origin: Media Molecule and Sony Computer Entertainment; original
  North American PlayStation 3 release on 2011-01-18.
- Platform or physical form: `PLAT-PLAYSTATION-3`, single-player story route
  reconstructed from sources, not a directly tested disc or licensed port.
- Mechanical families: physics and object manipulation; world topology and
  perspective; real-time system pressure.
- Primary sources:
  - **[P1]** [PlayStation Blog release announcement](https://blog.playstation.com/2010/09/23/littlebigplanet-2-now-launching-january-18-2011-in-north-america/),
    for original platform and North American release date.
  - **[P2]** [PlayStation LittleBigFAQ](https://blog.playstation.com/2010/05/20/littlebigplanet-2-the-littlebigfaq/),
    for full Story Mode and separately evolving Create/Share modes.
  - **[P3]** [PlayStation feature list](https://blog.playstation.com/2010/12/17/littlebigplanet-2-update-music-sequencer/),
    for named Grappling Hook and Bounce Pads, not specific level placement.
- Independent written route sources:
  - **[S1]** [GameFAQs *Grab and Swing* walkthrough](https://gamefaqs.gamespot.com/ps3/954843-littlebigplanet-2/faqs/61926),
    version 1.00 updated 2011-03-06, section `[W1.2]`, especially the
    post-link hook, checkpoint, electric-floor race and final platform.
  - **[S2]** [Gamepressure *Grab and Swing* guide](https://www.gamepressure.com/littlebigplanet2/grab-and-swing/z62aab),
    sections after image 8 through image 15, corroborating the back-layer
    button, hook, pads, race and flags; last update 2016-05-11.
  - **[S3]** [Imagisphere checkpoint reference](https://wiki.imagisphere.me/Checkpoint),
    used narrowly for ordinary LBP2 respawn behaviour; not a direct play log.
- **[R1]** Local no-direct-play and scope-boundary audit in this record.
- Claim IDs: `LBP2-001`–`LBP2-009`.

## Mechanical decomposition

### Action Genes

- `ACT-008`: navigate and jump in the crafted scene, including the visible
  front/back route change. Depth layer is traversal geometry, not a separate
  rotation or world-edit command.
- `ACT-341`: activate the back-layer door button and, when chosen, pull the
  eligible toilet switch with the hook. Fixture state changes are distinct
  from swinging past the fixture.
- `ACT-531`: attach to compatible sponge, steer, reel and release a live
  traversal tether. `ACT-361` is rejected because the player is not simply
  pulled to and stopped at one chosen endpoint.
- Claim IDs: `LBP2-003`–`LBP2-005`.

### System Behaviour Genes

- `SYS-398`: the received hook becomes the available traversal capability
  for the rest of this bounded route.
- `SYS-1055`: a valid tether constrains a gravity-driven arc; reel length,
  player steering and release govern the crossing trajectory.
- `SYS-1056`: contact with a bounce pad launches the avatar into another
  controllable airborne trajectory.
- `SYS-037`: touching a prize bubble acquires that optional collectible;
  complete prize coverage is not the route objective.
- `SYS-369`: a failed attempt returns through an authored checkpoint; exact
  checkpoint stock and retained collectible state are not inferred.
- Resolution order: move/inspect → activate gate or acquire hook → attach to
  valid anchor → steer/reel/release → collide with pad, safe geometry or
  hazard → collect optional contact pickups → reach final flags or retry.
- Claim IDs: `LBP2-003`–`LBP2-008`.

### Constraint Genes

- `CON-349`: the post-link hook-dependent gaps cannot be crossed by the
  documented route until the hook is granted.
- `CON-693`: attachment needs an eligible grabbable target; a sponge anchor
  or authored hook switch qualifies, but the background does not generically.
- Electric floor position and gap width are authored hazard parameters;
  the sources do not justify a new universal damage or finite-life rule.
- Claim IDs: `LBP2-003`–`LBP2-006`.

### Information Genes

- `INF-179`: the current side-view exposes nearby layers, anchor material,
  pads, electric ground, optional bubbles and the next safe route. Hidden
  depth-layer pickups are not all visible from every position.
- Claim IDs: `LBP2-003`–`LBP2-007`.

### Objective Genes

- `OBJ-026`: make the exit gate traversable and reach it. Prize completion
  and the race's best score are separate optional evaluations.
- Claim IDs: `LBP2-006`, `LBP2-007`.

### Time Genes

- `TIM-003`: input, gravity, swing and contact continue in real time. The
  race marker does not turn traversal into a discrete turn sequence.
- Claim IDs: `LBP2-004`, `LBP2-006`.

## Reproducible transitions

| Before | Action | Rule-bounded resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Avatar has arrived from the level link and the route door is closed | Enter the back layer and activate its button | The authored door opens and the route reaches Da Vinci's hook grant | depth and fixture interaction are causally necessary | `LBP2-003` |
| Hook has been granted; a sponge is in range | Attach and steer laterally | The line supports a swinging arc over the gap while gravity continues | dynamic tether differs from an endpoint pull | `LBP2-004` |
| Avatar hangs below a sponge near an elevated route | Reel in, then release at a chosen point | Shorter line changes reachable height; release continues the current motion | length and release timing are decisions | `LBP2-004` |
| Eligible toilet switch is reachable with the hook | Attach and pull it | The switch changes the fixture and exposes an optional prize | hook can operate a fixture, not only move the avatar | `LBP2-005` |
| Avatar drops onto a bounce pad below a gap | Allow contact and steer | The pad launches the avatar upward toward the next safe surface or anchor | contact supplies an impulse without an ordinary jump | `LBP2-006` |
| A late span has electric floor underneath | Swing and release across it | Safe landing continues the route; lethal contact instead ends this attempt | hazard is an authored route pressure | `LBP2-006`, `LBP2-008` |
| Final rotating sponge and pad sequence is crossed | Pass the final flags and exit | The selected story route ends; optional uncollected bubbles do not block it | declared positive terminal | `LBP2-006`, `LBP2-007` |

## Strategic and experiential structure

- Local decision: identify a genuinely grabbable anchor, attach at a useful
  moment, then choose reel length and release point relative to the next pad
  or platform. Ordinary jumping remains available between attachments.
- Medium-term planning: preserve a traversable path over electric surfaces;
  optional bubbles encourage riskier height and layer choices but do not gate
  the exit.
- Long-term structure: complete the post-link route to its final flags,
  rather than complete all Story levels or publish a created level.
- Failure attribution: visible hazard, anchor and pad placement explain most
  route failures. Exact hitbox and checkpoint stock are not sourced, so no
  measured precision or life-loss rule is asserted.
- Player-trust factors: the tether and visible pad show why an attempted
  release reaches or misses safe geometry; checkpoint return makes failure
  local, subject to the unverified remaining-return details.

## Replay and variation

- Line length, attachment timing, layer choice, optional bubble detours and
  release velocity vary; the same authored door, hook grant, electric span
  and final flags remain the scoped packet.
- Cooperative play is possible in the marketed Story mode, but no partner
  interaction is needed or included in this one-player route.

## Adjacent systems and history

- *It Takes Two* uses a co-operative swing anchor but Cody's placed nail and
  May's hammer are role-separated. Here one avatar holds a reusable hook
  granted mid-route, adjusts line length and chooses its own release.
- *NARAKA: BLADEPOINT* and *Sekiro* use tethered approaches to a chosen
  target (`ACT-361`/`SYS-653`); this packet sustains a pendulum and retains
  variable radius rather than terminating at the anchor.
- *Super Mario Bros.* and *Sonic the Hedgehog* share live platform traversal,
  pickups and authored exit markers. Neither provides evidence that the
  present hook and pad physics are merely a score or visual parameter.

## Normalised genome

| Type | Active genes | Parameters outside signature |
|---|---|---|
| Action | `ACT-008`, `ACT-341`, `ACT-531` | depth layer, button, aim and release timing |
| System | `SYS-037`, `SYS-369`, `SYS-398`, `SYS-1055`, `SYS-1056` | hook grant, sponge geometry, pad impulse, checkpoint |
| Constraint | `CON-349`, `CON-693` | grabbable material, reach and authored gaps |
| Information | `INF-179` | scene framing, visible bubbles and electric floor |
| Objective | `OBJ-026` | final flags and exit identity |
| Time | `TIM-003` | live speed and race display |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `393` (`GAME-0001`–`GAME-0393`).
- Exact genome matches: none.
- Tied near matches: `GAME-0312` — ASTRO BOT (`6 / 23 = 0.260870`).
- Supported combination subsets: none.
- Scan date: 2026-09-24.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0312` — ASTRO BOT | `ACT-008`, `ACT-341`, `SYS-037`, `SYS-369`, `CON-349`, `TIM-003` share direct live platform traversal, contextual fixtures, contact prizes, checkpoint return and an acquired route capability. | ASTRO BOT's Sky Garden uses enemies, struck-Bot rescues, a temporary inflation form and a replayable map result. This packet instead uses one avatar's adjustable held tether, compatible sponge anchors and bounce pads to reach a post-link story exit; optional prizes are not rescue subjects. | Near, `6 / 23 = 0.260870` |

### Preserved research notes

- New genes: `ACT-531`, `SYS-1055`, `SYS-1056`, `CON-693`.
- Evidence and reasoning: distinct held-tether steering, anchor-bound motion,
  elastic contact launch and compatible-target predicate are directly
  exercised in one source-bounded route and not covered by endpoint grapple.

## Taxonomy impact

- Registry changes: four new active IDs; no earlier signature changed.
- Taxonomy-change record: `TAXONOMY_CHANGE_132`.
- Candidate terms affected: grapple swing, sponge anchor, bounce pad, layer.

## Negative results

- No separate negative-result record. Editor tools, entire-level first-half
  object dragging, score optimisation and two-player gates are excluded by
  scope, not disproven for the product.

## Delta summary

## New facts

- [Observation | Corroborated | High] The post-link route grants a hook,
  requires steering and release from grabbable anchors over electric ground,
  offers pads and prizes, and ends at authored flags (`LBP2-003`–`LBP2-007`).

## New genes

- [Observation | Corroborated | High] `ACT-531`, `SYS-1055`, `SYS-1056` and
  `CON-693` isolate four operational boundaries rather than renaming hook art.

## New combinations

- [Observation | Corroborated | High] None promoted from one story route;
  existing registered subsets require the deterministic corpus scan below.

## Taxonomy changes

- [Observation | Corroborated | High] `TAXONOMY_CHANGE_132` records admission
  and transfer tests for the four new genes without older-genome migration.

## New questions

- Which exact checkpoint stock and prize state survive a PS3 death/retry in
  this level's late electric-floor sequence?

## Next recommended game

- [Hypothesis | Limited | Medium] `GAME-0395` The Legend of Zelda: Majora's Mask.
- Optimisation criterion: alternate a crafted real-time platform route with
  an authored time-loop adventure packet.
- Expected information gain: test whether repeatable temporal scheduling
  and retained transformations need distinctions beyond the present tether.
- Backlog impact: preserves the accepted genre-alternating order.

## Why this game

- [Hypothesis | Limited | Medium] A post-link story route isolates active
  material interaction and adjustable tether motion without importing the
  unlimited rules of a creation platform.
