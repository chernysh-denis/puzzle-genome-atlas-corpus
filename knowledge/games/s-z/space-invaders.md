---
game_id: GAME-0360
slug: space-invaders
game_title: "Space Invaders"
analysis_status: reviewed
reviewed: 2026-09-22
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-161
  system:
    - SYS-215
    - SYS-911
    - SYS-965
    - SYS-990
    - SYS-991
    - SYS-992
  constraint:
    - CON-183
    - CON-663
  information:
    - INF-001
  objective:
    - OBJ-002
    - OBJ-029
  time:
    - TIM-003
---

# Game: Space Invaders

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Laser base, invader,
fortress, UFO, the individual sprite shapes and exact point values are carrier
parameters, not gene names.

## Analysis scope

- Version / ruleset: Taito's original 1978 monochrome arcade family, frozen to
  MAME's complete `sisv2` program set, `Space Invaders (SV Version rev 2)`. The
  MAME preservation record identifies its six ROMs as `SV01`, `SV02`, `SV10`,
  `SV04`, `SV09` and `SV06`, and identifies the Midway `invaders` set used by
  the cited annotated disassembly as based on this set. The earlier presumed
  `SV01`–`SV06` combination has two undumped ROMs and is not claimed as an
  executable or completely preserved revision.
- Physical configuration: one player, factory three-base setting, bonus base
  at 1,500 points, upright left/right lever and fire button, monochrome Taito
  cabinet rules. The packet does not import Midway cabinet art, a colour
  overlay, cocktail alternation or a modern port's control and presentation.
- Structured target: insert one credit, start a one-player game, clear the
  initial rack of 55 invaders and wait until the successor rack is rebuilt and
  ordinary control returns. Stop before firing in the successor rack.
- Entry: score is zero; the active base and four intact fortresses are visible;
  three bases belong to the credit; a five-by-eleven rack is alive at its first
  starting height; no player shot is active.
- Fixed positive route: move only along the lower horizontal lane, fire upward
  through chosen fortress openings, let each shot settle before requesting the
  next, evade descending hostile shots, remove all 55 invaders and observe the
  next rack rebuild. The route may destroy the optional UFO if it appears, but
  UFO contact and a particular mystery value are not required by the terminal.
- Bounded failure controls: from clean duplicated source-model states, (a)
  accept three hostile hits before the bonus threshold, and (b) let the rack
  reach the base. Both must produce Game Over instead of rack clearance. These
  controls are evidence-model tests, not claims of direct cabinet play.
- Primary decision loop: read the visible rack, shots, fortresses, base stock
  and score; move the base laterally for alignment or evasion; fire only when
  the one player-shot channel is free; account for holes opened in cover; race
  the rack whose edge contacts reverse direction, drop it and reduce the time
  between effective formation steps as invaders disappear.
- Positive terminal: the fifty-fifth invader is removed, first-rack state
  settles, score and remaining base stock are retained, 55 invaders and four
  intact fortresses are rebuilt at the second-rack starting height and ordinary
  left/right/fire control returns. The last-hit explosion alone is
  insufficient; successor control must be present.
- Negative terminal: the current base is hit when no reserve base remains, or
  the formation overruns the base line; Game Over replaces continued play.
- Included: lateral base movement; upward fire; one active player projectile;
  live invader and projectile motion; five-by-eleven formation; edge reversal
  and descent; faster effective pressure with fewer invaders; three hostile
  shot channels as implementation context; bidirectional fortress erosion;
  player-projectile/hostile-projectile contact; target-class score; optional
  mystery-score UFO; factory three-base stock; one bonus base at 1,500; first
  rack clearance and successor rebuild.
- Excluded: two-player alternation; operator settings other than three bases
  and 1,500 bonus; later-rack play; exact late-rack survival strategy; named
  exploits such as the Nagoya attack; colour overlays; Part II; Midway-specific
  cabinet/audio claims; ports, compilations and mobile adaptations; emulator
  save states, speed changes, cheats, bootlegs and exact undocumented analog
  display tolerances.
- Direct-play status: not conducted. No cabinet, PCB, ROM image, executable,
  emulator, input trace, save state, screenshot, video or audio was obtained or
  inspected. The unit combines Taito's service manual, MAME's preservation
  record and a source-annotated disassembly of the explicitly related Midway
  set. The executable repository control below reconstructs cited transitions;
  it does not execute the arcade program.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `SI-001` | Taito released the original Space Invaders in 1978, and `sisv2` is the oldest complete preserved SV program set identified here | Confirmed | Corroborated | High | P1, R1 |
| `SI-002` | The selected cabinet exposes a left/right lever and fire button; a fresh one-player credit uses three factory-set bases | Confirmed | Direct | High | P2 |
| `SI-003` | A fresh rack contains 55 invaders in five rows of eleven and four fortresses | Observation | Corroborated | High | P2, T1 |
| `SI-004` | The base moves only left or right and fires an upward shot; another fire request is ignored while the player-shot channel is active | Observation | Corroborated | High | P2, T1 |
| `SI-005` | The formation moves laterally, reverses and drops after reaching an edge, and advances more quickly as its population decreases | Confirmed | Corroborated | High | P2, T1 |
| `SI-006` | Player fire, hostile fire and low formation contact can remove persistent fortress pixels and therefore rewrite future cover | Observation | Corroborated | High | P2, T1 |
| `SI-007` | Different invader rows award 30, 20 and 10 points; a UFO awards one mystery value from 50, 100, 150 or 300 | Confirmed | Direct | High | P2 |
| `SI-008` | First reaching the factory 1,500-point threshold awards one bonus base | Confirmed | Corroborated | High | P2, T1 |
| `SI-009` | A base hit consumes a finite base stock and restores the base while stock remains; exhaustion or overrun ends the game | Confirmed | Corroborated | High | P2, T1 |
| `SI-010` | Removing every invader clears the rack, retains run score and base stock, rebuilds 55 invaders and four fortresses and returns control at the next rack | Observation | Direct | High | T1 |
| `SI-011` | The local source-model control proves the accepted and two rejected terminals without executing Space Invaders | Observation | Direct | High | V1 |
| `SI-012` | No original program, cabinet play or audiovisual trace was inspected | Confirmed | Direct | High | R2 |

## Basic data

- Release / origin: Taito's corporate history records the enormously popular
  1978 release. The selected program identity is MAME's Taito `sisv2` set, not
  a claim that an incomplete earlier combination was executed.
- Platform or physical form: original upright coin-operated monochrome arcade
  cabinet with one left/right lever, fire and one-player start controls.
- Puzzle family: tactical forecast and counterplay; real-time system pressure.
- Primary and official sources, accessed 2026-09-22:
  - **[P1]** [Taito corporate
    history](https://taito.co.jp/en/corporate/about/history), for the 1978
    release and publisher identity.
  - **[P2]** [Taito *Space Invaders Service Instructions and Parts Catalog*
    `SV070019`](https://files.stardustarcade.com/PDF_Arcade_Manuals_and_Schematics/Space_Invaders_Service_Instructions_and_Parts_Catalog_(SV070019).pdf),
    pp. 1, 6, 8 and 12, for cabinet controls, three factory bases, four
    fortresses, lateral movement, fire, row scoring, mystery UFO values,
    accelerating invaders, bidirectional fortress destruction, 1,500-point
    bonus and both Game Over conditions. Preserved local SHA-256:
    `eb8b156de17cc9e3cfd053e0ff52974293ded195b10a2bd0fe3813418d1d7658`.
- Reproducible technical sources, accessed 2026-09-22:
  - **[R1]** [MAME `8080bw.cpp` preservation
    record](https://github.com/mamedev/mame/blob/master/src/mame/midw8080/8080bw.cpp),
    for the `sisv2` identity, complete six-ROM manifest, relation to Midway's
    `invaders` set and the explicit two-`NO_DUMP` limit on the presumed earlier
    set. MAME lists `sisv2` as `Space Invaders (SV Version rev 2)`.
  - **[T1]** [Computer Archaeology's annotated Space Invaders
    disassembly](https://computerarcheology.com/Arcade/SpaceInvaders/Code.html),
    for the source-model relations: initialise 55 flags, store one active
    player-shot status, move/reverse/drop the reference formation, count
    survivors, persist four shield bitmaps, consume/award bases and rebuild a
    cleared rack. It annotates the Midway set that MAME identifies as based on
    `sisv2`; byte addresses corroborate shared rule structure and are not
    asserted as a byte-identical hash of every Taito ROM.
  - **[V1]** [`verify_space_invaders_control.py`](../../../scripts/verify_space_invaders_control.py),
    an executable transition reconstruction over only the cited relations.
    It does not contain ROM bytes or emulate Intel 8080 code.
- Research record: **[R2]** local preflight found no verified program dump,
  PCB, cabinet, emulator state, input trace, screenshot, video or audio.
- Claim IDs: `SI-001`–`SI-012`.

## Mechanical decomposition

### Action Genes

- Existing `ACT-008`: directly move the persistent laser base left or right
  within the lower horizontal lane. The carrier has no vertical movement,
  jumping or remote destination selection.
- Existing `ACT-161`: align the base beneath an eligible invader, UFO or
  destructible fortress region and commit the current upward shot.
- Exact joystick travel, pixel coordinates and sprite identity are parameters.
  Claims: `SI-002`, `SI-004`.

### System Behaviour Genes

- Existing `SYS-215`: live projectile motion, collision, scoring contact,
  hostile shots and base/invader defeat resolve while movement continues.
- Existing `SYS-911`: one lethal hostile hit consumes one base and restores
  the controlled base while reserve remains; rack and fortress state persist.
- Existing `SYS-965`: first reaching the configured score threshold awards
  one extra base exactly once; this packet fixes the factory threshold at
  1,500.
- New `SYS-990`: move the surviving invaders as one reference formation,
  reverse and descend at an occupied edge, and shorten effective traversal time
  as fewer members remain.
- New `SYS-991`: accepted player shots, hostile shots and low formation contact
  erase intersected fortress pixels, retaining the resulting holes until a
  rack-clear rebuild.
- New `SYS-992`: zero surviving invaders settles the current rack, increments
  its progression state, rebuilds 55 invaders and four fortresses at the next
  start height and returns control while score and base stock persist.
- Row values and UFO mystery values are parameters of the score surface; they
  support `OBJ-002` without requiring a new generic flat-score gene. Claims:
  `SI-003`, `SI-005`–`SI-010`.

### Constraint Genes

- Existing `CON-183`: a visible finite base stock gates continued play and
  complete-run Game Over; the one score milestone may extend it.
- New `CON-663`: a fire request is legal only while no player projectile is
  active; hit, shield/bullet collision or playfield exit must settle the current
  projectile before the next can begin.
- The lower horizontal lane, occupied formation edge and projectile
  intersections are spatial carrier parameters. Claims: `SI-004`, `SI-009`.

### Information Genes

- Existing `INF-001`: the current rack, base, four fortress bitmaps,
  projectiles, UFO when present, score, high score, base stock and credit state
  are visible. Future hostile-shot timing and the next UFO mystery value are
  not disclosed, but they are not current board state.
- March audio reinforces the changing pace but no audio trace was inspected;
  the claim is therefore sourced rather than observed in this unit. Claims:
  `SI-003`–`SI-009`.

### Objective Genes

- Existing `OBJ-029`: remove every member of the finite 55-invader encounter
  set before base-stock exhaustion or overrun.
- Existing `OBJ-002`: optionally maximise accumulated score through target-row
  values and UFO opportunities. Score cannot substitute for rack clearance.
- The packet terminal additionally requires `SYS-992` successor control rather
  than stopping at the last-hit transient. Claims: `SI-007`, `SI-010`.

### Time Genes

- Existing `TIM-003`: formation motion, shots, collision and player input share
  a running real-time schedule. A smaller rack changes effective pressure while
  decisions remain live. Claims: `SI-004`–`SI-006`.

## Reproducible transitions

| Before | Action | Deterministic or bounded resolution | Establishes | Claim |
|---|---|---|---|---|
| Fresh one-player credit | move left or right | the base changes only its lower-lane horizontal coordinate within its bounds | direct lateral authority | `SI-002`, `SI-004` |
| No player shot is active | press fire | one projectile begins upward from the base and owns the player-shot channel | legal fire | `SI-004` |
| A player shot is active | press fire again | no second player projectile begins; the request remains unavailable until settlement | exact one-shot constraint | `SI-004` |
| Shot intersects a live invader | allow collision to settle | that invader flag clears, its class value is added and the remaining count falls | attack, score and formation population | `SI-005`, `SI-007` |
| Occupied formation reaches a side edge | allow the next formation move | horizontal direction reverses and the reference formation descends one carrier step | edge-coupled descent | `SI-005` |
| Fewer invaders remain | compare equal observation intervals | fewer members must be serviced per formation cycle, so effective formation advance and sourced pressure increase | population-coupled pace | `SI-005` |
| Any accepted shot intersects a fortress pixel | allow collision to settle | intersected pixels are removed and the hole remains available or dangerous for later trajectories | persistent mutable cover | `SI-006` |
| Score first reaches 1,500 | settle the scoring event | one base is added once without clearing the rack | score extends finite stock | `SI-008` |
| A hostile shot hits the base and reserve remains | accept the death sequence | one base is consumed and the base returns while rack and fortress damage persist | finite-life recovery | `SI-009` |
| A hostile shot hits with no reserve, or formation overrun occurs | accept terminal resolution | Game Over replaces continued play | two bounded failure terminals | `SI-009` |
| One invader remains | hit it and wait for settlement | survivor count reaches zero, the rack clears, score/lives persist, four intact fortresses and 55 invaders rebuild at the next start height, and control returns | positive packet terminal | `SI-010` |

## Edge-case audit

- Holding fire cannot create an overlapping stream: the active-shot flag and
  release debounce close the channel until the projectile settles.
- A player shot can expire at the top, hit a fortress, hit a hostile shot or
  hit an invader; every path must free the same channel before the next shot.
- Fortress damage is not cosmetic. A player can open a useful firing lane and
  simultaneously remove protection against later hostile fire.
- The final survivor still moves; the technical model changes one horizontal
  delta and disables one hostile-shot pattern, but the packet does not elevate
  those implementation constants into separate genes.
- The 1,500-point bonus is one-time and factory-configured. Reaching it at the
  same settlement as a base loss follows program order in the source model;
  the control tests the ordinary non-simultaneous path and makes no unsupported
  frame-order guarantee.
- UFO appearance and its mystery value affect score but not the required set;
  a route may ignore it and still clear the rack.
- Overrun has terminal precedence even if a base icon remains; it is not a
  normal hit-and-respawn path.
- The last invader's removal is not the end of the complete run. This unit uses
  returned control in the rebuilt rack only as a bounded evidence terminal and
  deliberately excludes later-rack play.

## Strategic and experiential structure

- Local: decide whether to align and fire, move under a remaining fortress
  segment, cross an exposed hole or wait for the current shot to settle.
- Medium term: carve narrow firing lanes without erasing all protection, bias
  removals toward dangerous columns and keep lateral escape room for the next
  edge descent.
- Long term: every kill advances clearance but also increases formation
  pressure; score can buy one extra base, while careless cover erosion makes
  late play less forgiving.
- Failure recovery: an ordinary hit spends a base but keeps the partially
  removed rack and damaged fortresses; exhaustion ends the credit. Overrun
  bypasses recoverable-hit logic.
- Information: the current tactical surface is readable, while hostile-shot
  timing and UFO value remain bounded uncertainty.

## Replay and variation

- The same fixed rack supports different firing lanes, fortress erosion,
  optional UFO contacts and evasive paths.
- Target order changes both near-term shot geometry and when the formation's
  effective pace accelerates.
- Score play can conflict with safe clearance because the UFO opportunity and
  exposed lane need not align with the safest remaining-invader route.
- Operator-adjustable four-to-six bases, a 1,000-point bonus and two-player
  alternation are documented but held outside the fixed packet so they do not
  masquerade as replay variation inside one canonical genome.

## Adjacent systems and history

- `GAME-0313` Tank 1990 also joins direct lateral/projectile combat, mutable
  cover, finite lives and a bounded hostile set. Tank 1990 releases reserves
  through arena spawns and protects a separate eagle; Space Invaders exposes
  one descending formation, one active player-shot channel and bidirectionally
  eroded pixel fortresses.
- `GAME-0342` PAC-MAN also carries score, finite lives, a one-time score-earned
  life and a rebuilt successor round. PAC-MAN clears collectibles while role-
  targeted pursuers and temporary predator reversal govern routing; Space
  Invaders clears a firing formation whose shrinking population increases
  pressure.
- `GAME-0345` Duck Hunt also has class-valued arcade targets and a bounded
  first-round terminal. Duck Hunt allocates three light-gun attempts per timed
  target and qualifies by six of ten; Space Invaders uses one reusable active
  projectile and requires all 55 hostiles.
- `GAME-0359` Crimson Skies shares direct real-time aimed combat, projectiles
  and bounded mission clearance but differs in three-dimensional craft motion,
  finite guided secondary ammunition and checkpoint restoration.

## Normalised genome

| Type | IDs | Boundary |
|---|---|---|
| Action | `ACT-008`, `ACT-161` | move the base laterally; align and fire |
| System | `SYS-215`, `SYS-911`, `SYS-965`, `SYS-990`, `SYS-991`, `SYS-992` | live projectile combat, finite-base recovery, score bonus, formation pressure, mutable fortresses and rack rebuild |
| Constraint | `CON-183`, `CON-663` | finite run stock and one active player projectile |
| Information | `INF-001` | current fixed arena, score, stock and threats are visible |
| Objective | `OBJ-002`, `OBJ-029` | maximise optional score; remove all 55 required hostiles |
| Time | `TIM-003` | act while formation and projectiles continue |

The signature contains 14 genes. `SYS-990`, `SYS-991`, `SYS-992` and
`CON-663` are new; ten existing boundaries are reused without changing their
meaning.

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `359` (`GAME-0001`–`GAME-0359`).
- Exact genome matches: none.
- Tied near matches: `GAME-0342` — PAC-MAN (`7 / 23 = 0.304348`).
- Supported combination subsets: none.
- Scan date: 2026-09-22.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0342` — PAC-MAN | `ACT-008`, `SYS-911`, `SYS-965`, `CON-183`, `INF-001`, `OBJ-002`, `TIM-003` | Both expose a fixed arena, lateral steering, score, finite lives, one score-earned life and live-time play whose cleared first state rebuilds a successor round. PAC-MAN clears maze collectibles while four role-targeted pursuers, tunnels and temporary predator reversal govern routing; Space Invaders clears a shrinking firing formation through one active projectile, bidirectionally eroded fortresses, edge-coupled descent and increasing pressure. | Near, `7 / 23 = 0.304348` |

### Preserved research notes

- New genes: `SYS-990`, `SYS-991`, `SYS-992` and `CON-663`.
- Classification result: four new boundaries plus ten reused movement, attack,
  live combat, recovery, bonus-stock, finite-life, visible-state, scoring,
  clearance and real-time boundaries.

## Taxonomy impact

- Add `SYS-990`, `SYS-991`, `SYS-992` and `CON-663` as active evidence-backed
  boundaries under
  [`TAXONOMY_CHANGE_099`](../../../research/taxonomy-changes/TAXONOMY_CHANGE_099.md).
- Add support references to `ACT-008`, `ACT-161`, `SYS-215`, `SYS-911`,
  `SYS-965`, `CON-183`, `INF-001`, `OBJ-002`, `OBJ-029` and `TIM-003`; their
  definitions do not need expansion.
- Add no combination. The packet's conjunction is distinctive, but the corpus
  does not yet establish a recurring structure requiring a verified
  combination record.

## Delta summary

## New facts

- Exact program scope is complete Taito `sisv2`, not the incompletely dumped
  presumed predecessor or a modern wrapper.
- The bounded first rack contains 55 invaders, four persistent fortresses and
  one directly controlled laterally moving base.
- One player projectile at a time, population-coupled pressure and
  bidirectional fortress erosion form the central decision economy.
- Three factory bases, one bonus at 1,500, stock exhaustion and overrun bound
  failure; zero invaders rebuilds the successor rack.

## New genes

- `SYS-990` — Advance a shrinking formation through edge reversal and descent.
- `SYS-991` — Erode persistent fortress pixels from either side.
- `SYS-992` — Rebuild a cleared formation while retaining run stock.
- `CON-663` — Allow only one active player projectile.

## New combinations

- None.

## Taxonomy changes

- Four additions; no rename, merge, deprecation or definition rewrite.

## Negative results

- No cabinet, PCB, program image, emulator or audiovisual trace was available.
- The presumed earlier Taito ROM combination is incomplete and was rejected as
  the exact executable target.
- No reliable reason was found to elevate individual hostile-shot patterns,
  exact UFO shot-count scoring, sprite animation or famous exploits into genes.
- No repeated combination was verified.

## Open questions

- A future controlled preservation module could hash an authorised complete
  `sisv2` set and compare its code paths byte-for-byte with the related Midway
  annotated disassembly.
- A separate later-rack packet could test starting-height progression and
  exploit boundaries without changing this first-rack genome.

## Reproducibility notes

1. Use the exact MAME `sisv2` manifest only as the preservation identity; do
   not substitute the incomplete presumed predecessor or call the Midway set
   byte-identical.
2. Configure the sourced factory policy: one player, three bases, one bonus at
   1,500 points.
3. Initialise 55 live invaders, four intact fortress masks, score zero, three
   bases and no active player projectile.
4. Verify lateral-only movement and rejection of a second fire request while
   the shot channel is occupied.
5. Verify edge reversal plus descent and a shorter effective formation cycle
   after members have been removed.
6. Verify persistent fortress-mask erosion from player and hostile fire.
7. Verify one recoverable hit with reserve, Game Over at exhaustion and Game
   Over on invasion.
8. Remove the final invader and require rebuilt second-rack state plus returned
   control before accepting the positive terminal.
9. Run `python3 scripts/verify_space_invaders_control.py`; then run the normal
   repository, localisation, web, browser and accessibility gates.

## Localisation review

- Touched Ukrainian game fields were newly authored and `verified`: `profile`,
  `scope`, `directPlay`, presentation title/summary/link label, platform edition
  and all four new gene entries.
- Functional Ukrainian vocabulary for the laser base, fortresses, formation,
  projectile, base stock, invasion and arcade cabinet is authored without
  importing generic English prose. Official title, ROM-set ID, file labels and
  source-interface tokens remain untranslated where translation would damage
  identity.
- English-leak review permits only proper names, code identifiers and cited
  source terms. No first-pass translation is deferred to a batch repair.
