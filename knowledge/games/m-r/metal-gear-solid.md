---
game_id: GAME-0339
slug: metal-gear-solid
game_title: Metal Gear Solid
analysis_status: reviewed
reviewed: 2026-09-21
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-161
    - ACT-202
    - ACT-341
    - ACT-489
  system:
    - SYS-057
    - SYS-215
    - SYS-369
    - SYS-958
  constraint:
    - CON-077
    - CON-282
    - CON-330
  information:
    - INF-075
    - INF-115
    - INF-364
  objective:
    - OBJ-026
  time:
    - TIM-003
---

# Game: Metal Gear Solid

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Solid Snake,
Shadow Moses, Cargo Dock, Heliport, Tank Hangar, Codec, Soliton Radar, Genome
Soldiers and SOCOM are carrier parameters, not gene names.

## Analysis scope

- Version / ruleset: the original North American English PlayStation Disc 1,
  serial `SLUS-00594`, on Normal difficulty. It is not Integral, VR Missions,
  The Twin Snakes, a PC port, PSOne Classic wrapper, Master Collection
  executable, PAL or Japanese release, mod, randomiser, emulator enhancement
  or later-series ruleset.
- Structured analysis target: the original licensed PlayStation rules described
  by Konami's English manual and the current official Konami beginner
  infiltration manual, restricted to mechanics that both sources attribute to
  the preserved original opening.
- Scenario: one fresh New Game from first ordinary control of Solid Snake in
  the Cargo Dock through the opening infiltration into the Tank Hangar.
- Entry: Snake has surfaced inside the Cargo Dock and ordinary movement first
  becomes available before he reaches the first patrolling Genome Soldier. He
  has no acquired firearm, access card or later equipment.
- Fixed reproducible route: move and crawl through the Cargo Dock without
  exhausting Life; use crates, walls and water to break directed sight; avoid
  or divert the patrols; wait until the authored elevator arrives and enter it;
  accept the Heliport transition; cross the snow and moving searchlight fields;
  reach either supported ventilation entrance; change into crawling posture;
  enter its duct; and stop when ordinary control first resumes inside the Tank
  Hangar.
- Primary decision loop: read the local camera and Soliton Radar, predict each
  patrol, sight cone, camera or searchlight, then move, wait, crawl, use
  occlusion or make a local noise. If detected, break sight, survive the Alert
  response, remain concealed through Evasion and resume the route only after
  Infiltration returns.
- Positive terminal: Snake enters either supported Heliport duct and the area
  transition restores ordinary control inside the Tank Hangar. Merely reaching
  the elevator or Heliport does not complete the packet.
- Failure paths: Snake's Life reaching zero produces Game Over; Continue
  restores the nearest authored Continue Point rather than the failed local
  positions and alert state. The fixed route does not require attacking or
  defeating any guard.
- Included: direct running and walking; crouching and crawling; wall adhesion,
  contextual elevator and duct interactions; intentional wall taps; puddle,
  snow-footprint and player-made sound; authored patrols; directed sight and
  occlusion; surveillance cameras and moving searchlights; Noise, Alert,
  Evasion and Infiltration states; reinforcement/attack response; Life,
  local sight and sound; the Soliton Radar's actor dots and coloured perception
  cones; radar suppression during Alert, Evasion and narrow-space states;
  Continue Point restoration; the delayed Cargo Dock elevator; two supported
  duct routes and the Tank Hangar transition.
- Reproducible parameterisation: choose fresh New Game and Normal in the
  original-US `SLUS-00594` Disc 1 ruleset. Player timing, patrol phase, optional
  noise, detection, damage, chosen duct and remaining Life may vary. Cargo Dock,
  the delayed elevator, Heliport, supported ducts and Tank Hangar terminal do
  not.
- Excluded: item-box collection, rations, SOCOM, chaff or stun grenades,
  deliberate guard defeat, Codec saving, the DARPA Chief, Level 1 Card, cell
  defence, Armory, C4, bosses and every later story area; cardboard boxes,
  higher security cards, weapon/ammunition inventory, torture, endings, Disc 2,
  VR Training and all other releases or wrappers. These commercial mechanics
  are not inferred into this opening route merely because the manual lists
  them.
- Direct-play status: not conducted. No original disc, PlayStation console,
  disc image, emulator, save, controller trace, screenshot, video or audio was
  used. This is a source-bounded reconstruction, not a claimed playthrough.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `MGS-001` | The packet targets the original North American PlayStation Disc 1 `SLUS-00594`, not a later port, remake or wrapper | Confirmed | Corroborated | High | P1, P2, S1 |
| `MGS-002` | Direct controls support movement, crouch/crawl, wall adhesion, contextual action and intentional wall taps | Confirmed | Direct | High | P1 |
| `MGS-003` | Directed hostile or camera sight through unobstructed space causes Alert and makes the radar unavailable | Confirmed | Direct | High | P1, P2 |
| `MGS-004` | Losing sight starts an Alert countdown into Evasion; surviving a second search countdown restores Infiltration, while rediscovery returns to Alert | Confirmed | Direct | High | P1, P2 |
| `MGS-005` | In Infiltration or Evasion, eligible sound diverts a guard from patrol to investigate, and an empty search returns that guard to patrol | Confirmed | Direct | High | P1, P2 |
| `MGS-006` | The Soliton Radar exposes Snake, enemies/cameras and directed coloured perception cones but is unavailable during Alert, Evasion and declared narrow-space states | Confirmed | Direct | High | P1, P2 |
| `MGS-007` | The Cargo Dock objective requires hiding until the delayed elevator becomes accessible | Confirmed | Direct | High | P2 |
| `MGS-008` | The Heliport route tests moving searchlights, cameras, snow traces and one of two crawl-only ducts into the Tank Hangar | Confirmed | Direct | High | P2, S2 |
| `MGS-009` | Zero Life ends the attempt and Continue restores the nearest authored Continue Point | Confirmed | Direct | High | P1 |
| `MGS-010` | The complete signature admits only mechanics causally available between first Cargo Dock control and first Tank Hangar control | Observation | Corroborated | High | P1, P2, S1–S2, V1 |

## Basic data

- Release / origin: Konami; North American PlayStation release dated 1998.
  PlayStation's official history identifies Metal Gear Solid as the 1998
  PlayStation action-stealth landmark.
- Platform or physical form: original two-disc North American PlayStation
  release; this packet remains entirely on Disc 1 `SLUS-00594`.
- Puzzle family: tactical forecast and counterplay; real-time system pressure;
  ordered dependency sequencing.
- Primary sources, accessed 2026-09-21:
  - **[P1]** [Konami / Sony's original English PlayStation
    manual](https://secure.cdn.us.playstation.com/manuals/classic/games/metal-gear-solid-manual-en.pdf),
    pp. 3–10, for controls, elevator/duct operation, mission goal, radar and
    camera modes, directed perception, sound investigation, Alert/Evasion/
    Infiltration transitions, Life, Game Over and Continue Points.
  - **[P2]** [Konami's official Beginner's Infiltration
    Manual](https://metalgear.konami.net/manual/mc1/mgs1/pc/en/page19.html),
    for the preserved Cargo Dock and Heliport route: puddles, water escape,
    delayed elevator, radar cones, searchlights, cameras, snow traces and two
    duct entrances. Its modern wrapper controls and later content are not used.
  - **[P3]** [PlayStation history: Metal Gear
    Solid](https://www.playstation.com/en-us/playstation-history/1994-ps-one/),
    for original 1998 PlayStation identity and action-stealth framing.
- Corroborating sources:
  - **[S1]** [GameFAQs original PlayStation release
    data](https://gamefaqs.gamespot.com/ps/197909-metal-gear-solid/data), for
    North American `SLUS-00594` / `SLUS-00776` product identity and date.
  - **[S2]** [GameFAQs original-PlayStation opening route by
    IRojas](https://gamefaqs.gamespot.com/ps/197909-metal-gear-solid/faqs/4007),
    for Cargo Dock elevator, Heliport and duct-to-Tank-Hangar ordering.
- Validation source:
  - **[V1]** repository-side transition reconstruction from P1–P3 and S1–S2;
    source and rules reasoning only, with no direct play or audiovisual claim.
- Claim IDs: `MGS-001`–`MGS-010`.

## Mechanical decomposition

### Action Genes

- `ACT-008`: directly walk or run Snake through the current authored area.
- `ACT-161`: if detection becomes combat, commit the available unarmed strike
  against a reachable guard; the successful route does not require it.
- `ACT-202`: change between standing, crouched and crawl/Intrude posture to
  alter clearance, exposure and movement, including duct entry.
- `ACT-341`: use an eligible elevator panel or ventilation entrance to change
  the current authored route state.
- New `ACT-489`: while pressed against compatible nearby geometry, tap it to
  emit a positioned sound that can lure an eligible guard.
- Claims: `MGS-002`, `MGS-005`, `MGS-007`, `MGS-008`.

### System Behaviour Genes

- `SYS-057`: a guard replaces its normal patrol with investigation toward an
  eligible wall tap, puddle step or other local sound, then returns when it
  finds nothing.
- `SYS-215`: completed detection enables live reinforcement attack and Life
  damage while movement and survival inputs continue.
- `SYS-369`: Game Over followed by Continue restores the nearest authored
  Continue Point instead of retaining failed local state.
- New `SYS-958`: sight or camera detection enters Alert; lost sight and the
  first countdown enter Evasion; surviving the second search countdown restores
  Infiltration; rediscovery returns to Alert.
- Resolution order: movement or sound updates patrol perception; completed
  sight triggers Alert and reinforcement response; lost sight advances the two
  recovery stages; an available elevator or duct interaction transfers the
  route; zero Life restores through Continue rather than settling success.
- Claims: `MGS-003`–`MGS-005`, `MGS-009`.

### Constraint Genes

- `CON-077`: guards and cameras detect Snake only inside their current directed
  perception region without an intervening opaque barrier.
- `CON-282`: Cargo Dock control, delayed elevator, Heliport, one supported duct
  and Tank Hangar control form the authored progression order.
- `CON-330`: the active packet remains viable only while Snake retains Life and
  remains in the permitted opening areas.
- Scarce route state: Life, current alert phase/countdown, patrol phase,
  elevator availability, current posture, occlusion, chosen duct and current
  Continue Point.
- Claims: `MGS-003`, `MGS-007`–`MGS-009`.

### Information Genes

- `INF-075`: the on-screen Life gauge exposes current survival capacity when it
  changes or the rules require it.
- `INF-115`: current camera sight, footsteps, water and other spatial sound
  expose only locally perceivable patrol and response state.
- New `INF-364`: while available, the Soliton Radar plots Snake and current
  enemies/cameras with colour-coded directed perception cones; Alert, Evasion
  and narrow-space rules deliberately remove that layer.
- Claims: `MGS-003`, `MGS-005`, `MGS-006`, `MGS-009`.

### Objective Genes

- `OBJ-026`: make the delayed elevator and one supported duct traversable,
  navigate Snake through them and reach first ordinary Tank Hangar control.
- Success, evaluation and failure: the target is spatial and binary. The fixed
  route need not defeat a guard or collect an item; zero Life ends the current
  attempt and Continue restores an earlier point.
- Claims: `MGS-007`–`MGS-009`.

### Time Genes

- `TIM-003`: patrols, searchlights, perception, sound response, Alert/Evasion
  countdowns and hostile attacks progress in real time while movement, posture
  and interaction inputs remain available.
- Claims: `MGS-003`–`MGS-008`.

## Reproducible transitions

| Before | Action | Deterministic or bounded resolution | Establishes | Claim |
|---|---|---|---|---|
| Fresh Normal control begins in Cargo Dock | move while watching the patrol and current sight cone | Snake traverses continuously; occupying a directed unobstructed region triggers Alert | embodied sight-bounded infiltration | `MGS-002`, `MGS-003` |
| Snake is hidden beside compatible geometry in Infiltration | tap the wall | a nearby eligible guard leaves patrol, investigates the sound and returns after finding nothing | deliberate local diversion | `MGS-005` |
| A guard sees Snake | break line of sight and remain concealed | Alert reinforcement pressure continues, then the first zero enters Evasion and the second zero restores Infiltration; rediscovery returns to Alert | reversible staged alarm | `MGS-003`, `MGS-004` |
| Soliton Radar is available in Infiltration | observe without entering a disallowed state | actor/camera dots and directed colour-coded cones update; Alert, Evasion or narrow space suppresses the layer | conditional perception map | `MGS-006` |
| The Cargo Dock elevator is not yet available | remain concealed until its authored arrival, then use the panel/entrance | the elevator accepts Snake and transfers the route to Heliport | delayed authored gate | `MGS-007` |
| Heliport patrols, cameras and searchlights are active | cross snow under occlusion and reach either supported duct | traces and sound can alter hostile response; valid low-clearance entry requires crawl posture | alternative crawl-only gate | `MGS-005`, `MGS-008` |
| Snake is crawling inside a supported Heliport duct | advance through the duct exit | the area transition settles and ordinary control resumes inside Tank Hangar | scoped positive terminal | `MGS-008` |
| Life reaches zero before the terminal | choose Continue | failed local positions, Life and alert state are discarded and the nearest authored Continue Point is restored | bounded failure recovery | `MGS-009` |

## Strategic and experiential structure

- Local decision: choose whether to wait, move, crawl, hug cover or create a
  diversion based on current patrol facing, radar cone, sound surface and
  available concealment.
- Medium-term planning: preserve Life and low alert pressure while timing the
  delayed elevator, then cross a more open Heliport whose searchlights, cameras,
  snow traces and guards produce overlapping perception risks.
- Long-term structure: the packet teaches that observation and reversible
  concealment, rather than hostile clearance, open a linear authored route. The
  destination is reached through one of two low-clearance gates.
- Common heuristics: wait outside blue/yellow cones; use opaque crates and
  walls; avoid running through puddles; break sight before fighting; do not move
  until Evasion fully returns to Infiltration; crawl only when the duct is
  safely reachable.
- Failure attribution: radar mode/absence, coloured cones, alert label,
  countdown, spatial sound, visible patrol movement, Life and route position
  separate sight exposure, noisy movement, incomplete escape and lethal damage.
- Claims: `MGS-002`–`MGS-010`.

## Replay and variation

- What changes between attempts: patrol phase at each move, optional wall taps,
  puddle or footprint exposure, detection, chosen concealment, alert duration,
  damage, remaining Life and which duct is used.
- Randomness or procedural generation: Cargo Dock, Heliport, Tank Hangar,
  fixtures, patrol routes and supported exits are authored. This packet does
  not rely on procedural geometry or random loot.
- Multiple viable strategies: wait for clean patrol gaps, use sound to redirect
  a guard, recover from detection through staged evasion or choose either
  supported duct. The fixed route requires no firearm or hostile defeat.
- Typical replay motive: a cleaner undetected route, faster elevator/duct
  timing or fewer Life losses. Later ranks, bosses and story outcomes are not
  part of this packet.
- Claims: `MGS-003`–`MGS-010`.

## Adjacent systems and history

- Direct predecessors: Metal Gear and Metal Gear 2 established authored
  infiltration, patrol avoidance and alert pressure; this PlayStation packet
  joins those decisions to a live spatial radar and cinematic area transitions.
- Variants: Integral, The Twin Snakes, PC, PSOne Classics and Master Collection
  wrappers require independent evidence and do not inherit this exact target.
- Similar games: Far Cry 3, Dishonored and METAL GEAR SOLID V share directed
  sight, local sound, patrol diversion and recoverable detection pressure.
- Important difference: this opening exposes actual perception cones on a
  radar that disappears during danger, then requires two named countdown phases
  before ordinary patrol state returns.

## Normalised genome

The front matter is canonical. The complete signature contains 17 Active
genes: five Action, four System Behaviour, three Constraint, three Information,
one Objective and one Time gene. Character, area, interface, guard and numeric
countdown labels remain carrier parameters.

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `338` (`GAME-0001`–`GAME-0338`).
- Exact genome matches: none.
- Tied near matches: `GAME-0280` — Resident Evil 2 (2019 remake) (`11 / 33 = 0.333333`).
- Supported combination subsets: none.
- Scan date: 2026-09-21.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0280` — Resident Evil 2 (2019 remake) | `ACT-008`, `ACT-161`, `ACT-341`, `SYS-057`, `SYS-215`, `SYS-369`, `CON-282`, `INF-075`, `INF-115`, `OBJ-026`, `TIM-003` | Both packets move through authored spaces, permit contextual fixture use and live attacks, react to local perception, retain Life/health pressure, recover from failure at authored points and reach a spatial terminal in real time. Resident Evil 2 instead manages firearms, scarce inventory, a carried key, defended grabs and save-room arrival across a survival-horror chase. Metal Gear Solid centres posture, non-damaging spatial diversion, directed sight, conditional radar and two-stage alarm recovery; its successful opening requires no pickup, firearm, hostile defeat or manual save. | Near, `11 / 33 = 0.333333` |

## Taxonomy impact

`ACT-489`, `SYS-958` and `INF-364` are new under `TAXONOMY_CHANGE_082`.
Stable support is added to `ACT-008`, `ACT-161`, `ACT-202`, `ACT-341`,
`SYS-057`, `SYS-215`, `SYS-369`, `CON-077`, `CON-282`, `CON-330`, `INF-075`,
`INF-115`, `OBJ-026` and `TIM-003` without changing their definitions. No
earlier signature changes.

## Negative results

- No verified combination is registered from one new carrier.
- No direct play, disc possession/extraction, emulation, audiovisual
  observation, save or controller trace is claimed.
- The Master Collection online manual is used only where it explicitly
  preserves the original Cargo Dock/Heliport instruction; wrapper controls and
  later-package behaviour are excluded.
- The successful route does not require SOCOM, rations, combat, guard defeat,
  saving, access cards or later equipment, so those systems are not inferred.
- `SYS-958` is the reversible Alert-to-Evasion-to-Infiltration state machine,
  not a generic suspicion meter or irreversible alarm.
- `INF-364` requires both actor/perception geometry and conditional radar
  suppression; ordinary local sight alone remains `INF-115`.

## Delta summary

## New facts

- [Confirmed | Direct | High] The original manual establishes direct posture,
  wall-tap, elevator, duct, radar, alert-state, Life and Continue behaviour.
- [Confirmed | Direct | High] Konami's route manual establishes the delayed
  Cargo Dock elevator and two Heliport ducts under puddle, searchlight, camera,
  snow-trace and patrol pressure.

## New genes

- [Confirmed | Direct | High] `ACT-489` isolates an adjacent-surface action
  whose intended result is a positioned sound stimulus.
- [Confirmed | Direct | High] `SYS-958` isolates reversible detection pressure
  with two named countdown stages and reacquisition.
- [Confirmed | Direct | High] `INF-364` isolates a conditional live radar that
  exposes actor markers and directed perception regions.

## New combinations

- [Observation | Corroborated | High] None; recurrence remains
  evidence-driven.

## Taxonomy changes

- [Confirmed | Direct | High] Three new portable boundaries are added without
  modifying an earlier gene or signature.

## New questions

- Which later bounded game independently removes its threat-map information
  precisely when alert pressure increases?
- Can a later lawful direct trace establish exact countdown values without
  changing this source-bounded state-machine signature?

## Next recommended game

- `GAME-0340` Halo: Combat Evolved Anniversary, as reserved by selection 023.

## Why this game

- Metal Gear Solid is a recognisable PlayStation anchor whose opening teaches
  a complete stealth grammar before combat: observe, predict, divert, conceal,
  survive detection and enter through a route-sized posture gate.

## Combination opportunities

- No verified combination is a proper subset of this complete signature.
- The radar and alert-recovery state machine need independent recurrence before
  any reusable multi-gene combination is proposed.

## Exclusions and assumptions

- The sources directly establish opening rules and route goals but do not
  execute the original disc. No claim depends on a frame count, exact patrol
  coordinate, exact countdown number or hidden random seed.
- Normal is fixed because Konami's opening manual explicitly applies to Easy
  and Normal; this packet chooses one reproducible difficulty rather than
  merging their tuning.
- Two supported duct routes are admitted; optional item-box detours and combat
  outcomes are not terminal requirements.

## Open questions

- A lawful owner-supplied original Disc 1 trace could later confirm exact
  patrol timing, alert counters and Continue Point placement.
