---
game_id: GAME-0460
slug: super-mario-64
game_title: Super Mario 64
analysis_status: reviewed
reviewed: 2026-09-30
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-610
    - ACT-611
  system:
    - SYS-036
    - SYS-037
    - SYS-045
    - SYS-578
    - SYS-1211
  constraint: []
  information:
    - INF-119
    - INF-179
  objective:
    - OBJ-262
  time:
    - TIM-003
---

# Game: Super Mario 64

Use the canonical [vocabulary and signature](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Mario, Bob-omb Battlefield, Lakitu, Big Bob-omb, coins and three valid throws are carrier parameters, not genre or camera-style genes.

## Analysis scope

- Version / ruleset: original Nintendo 64 *Super Mario 64*, first Bob-omb Battlefield Power Star, represented by Nintendo's original N64 booklet, a pinned decompilation of the US original-game code and a bounded original-game first-star route. The code-derived landing rule is scoped to that code revision; the European booklet corroborates generic controls without proving byte-identical regional software. Start with a fresh zero-Star file at the castle entrance, enter the first painting and walk the ordinary mountain path to Big Bob-omb. End positively only after three accepted on-summit throws, appearance and separate contact collection of the first Power Star and return to the castle; end negatively when health loss or a fatal fall closes this attempt. Include analogue movement and jumping, direct Lakitu camera reframing, visible local course geometry, continuing rolling/hostile movement, damage and coin recovery, the encounter's rear grab and throw, invalid off-summit throws that do not count, visible health and the Star pickup/return. Optional cannon, flowerbed warp, red/100-coin Stars, Wing Cap, later paintings, broader castle-door thresholds, lives/retry after this attempt, speedrun exploits, DS remake and modern port features are excluded modules. No N64 cartridge or executable was run.
- Structured analysis target: `PLAT-NINTENDO-64`, original US first-Star code path, with the original European booklet used only for shared documented controls.
- Primary decision loop: inspect the next visible ascent and reframe the following camera when terrain is obscured; steer and jump around moving hazards while preserving health; reach the summit, get behind the live guardian, lift and land him inside the summit until his finite health is exhausted; then touch the spawned Star.
- Entry and exit: fresh zero-Star castle entrance through the first painting; success is first-Star contact and castle return, not merely the boss's defeat. Zero health or a fatal course fall ends the scoped attempt; no next-life restart is represented.
- Included: only mechanisms needed for the ordinary first-Star route and encounter, including optional local coins when used to recover from damage.
- Excluded: other stars and courses, cannon/warp shortcuts, cap unlocks, save-menu management, later Bowser tail throws and regional parity beyond documented shared rules.
- Potential scoped modules: cannon access and shortcuts, red/100-coin routes, star-door progression, later boss encounters and direct cartridge/version comparison.
- Direct-play status: no cartridge, emulator, ROM image, game video or audio was opened or played. The first-party booklet and pinned human-readable decompilation were inspected as documentary/code evidence; the artwork is an original interpretation, not a frame capture.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| SM64-001 | The packet is the first original-N64 Bob-omb Battlefield Star attempt; later stars and editions are excluded. | Observation | Corroborated | High | P1, P2, R1 |
| SM64-002 | Analogue stick tilt steers movement and speed, A supports jumps, and C-button Lakitu controls change the following view without changing world geometry. | Observation | Direct | High | P1 printed pp. 8–10, 19 |
| SM64-003 | The castle's first painting enters the course; an ordinary foot ascent reaches a separately activated Big Bob-omb encounter on the summit. | Observation | Corroborated | High | P1 printed pp. 6, 15; P2, R1 |
| SM64-004 | Big Bob-omb becomes holdable after encounter activation; an on-summit landed throw reduces a three-unit boss health count, whereas an off-summit throw causes return without credit. | Observation | Corroborated | High | P2, R1 |
| SM64-005 | Exhausting that count spawns a separate Power Star, which must be touched to record progress and leave the course. | Observation | Corroborated | High | P1 printed pp. 16–18, P2, R1, R2 |
| SM64-006 | The power meter falls after damaging contact or falls; touching a coin credits a count and healing, so avoiding hazards or taking accessible coins changes survival. | Observation | Direct | High | P1 printed pp. 17–18, R2 |
| SM64-007 | The dossier is source-only: exact real-controller camera feel, frame timing, every possible shortcut and software-region parity were not measured. | Observation | Limited | High | Method and source boundary |

## Basic data

- Release / origin: Nintendo's original 1996 Nintendo 64 game; first-Star rule packet, not *Super Mario 64 DS* or a Switch wrapper.
- Platform or physical form: Nintendo 64 cartridge rules reconstructed from source, not a played cartridge. The structured registry names the exact analysis target.
- Mechanical families: `FAM-007` for collision- and gravity-dependent spatial movement and `FAM-010` for live hostile pressure; no deduction, turn queue, world-topology editing or route-construction family is asserted.
- Primary sources accessed 2026-09-30:
  - P1: [Nintendo's original N64 instruction booklet](https://www.nintendo.com/eu/media/downloads/games_8/emanuals/nintendo_8/Manual_Nintendo64_SuperMario64_EN.pdf), cover `NUS-P-NSMP-NEU6`, printed pp. 6–19. The booklet supports entry through a painting, analogue steering, movement/jumps, hold/throw, Star pickup, health and the C-button Lakitu camera. It is a European print, not proof of an inspected US cartridge.
  - P2: [The Mushroom Kingdom's original-game first-Star guide](https://themushroomkingdom.net/sm64_guide.shtml), Course 1, Star 1. It independently describes summit approach, rear pickup, three throws and no credit for an off-summit throw.
- Reproducible code record accessed 2026-09-30:
  - R1: [pinned `king_bobomb.inc.c`](https://github.com/n64decomp/sm64/blob/9921382a68bb0c865e5e45eb594d9c64db59b1af/src/game/behaviors/king_bobomb.inc.c), whose `king_bobomb_act_0`, `_4`, `_5` and `_7` initialise three health units, branch on landing height, return an off-summit boss and spawn the separate Star. [Pinned Bob-omb Battlefield script](https://github.com/n64decomp/sm64/blob/9921382a68bb0c865e5e45eb594d9c64db59b1af/levels/bob/script.c) places Big Bob-omb in the first-Star act.
  - R2: [pinned interaction code](https://github.com/n64decomp/sm64/blob/9921382a68bb0c865e5e45eb594d9c64db59b1af/src/game/interaction.c), `interact_coin` and `interact_star_or_key`, for coin count/heal and distinct Star-contact progression.
- Secondary sources: none used to assert a new rule beyond the first-hand route and code. Neither the source repository nor these links provide a licensed game image for the site.
- Claim IDs: SM64-001–SM64-007.

## Mechanical decomposition

### Action Genes

`ACT-008` — Steer Mario directly over the three-dimensional path and time jumps. Stick deflection changes speed; jumping is a movement parameter, not a new command category.

`ACT-610` — Reframe the Lakitu follow view to inspect an occluded stretch or the guardian approach. Camera movement discloses geometry but does not create a route as in Echochrome.

`ACT-611` — Approach an eligible Big Bob-omb from behind, lift him into a held phase and throw him toward the summit surface. He is a live opponent rather than an inert carried cube or an instant fighting throw.

### System Behaviour Genes

`SYS-036` — Running and jumps resolve against three-dimensional support, slopes and falls while momentum continues.

`SYS-037` — Contact credits an accessible optional coin without ending the attempt. The terminal Star contact belongs to `OBJ-262`, not this continuing-pickup boundary.

`SYS-045` — Local hostile and rolling-hazard motion continues as Mario navigates; their exact script timing is not needed for the bounded claim.

`SYS-578` — Damaging contact and falls deplete one power meter; compatible coin contact restores missing health, and zero closes the attempt.

`SYS-1211` — Only a thrown boss landing at accepted summit height reduces his three-unit count. Throwing him outside the summit returns him without credit; the third valid landing triggers the distinct Star reward.

### Constraint Genes

None separately admitted. The summit landing test is the transition branch of `SYS-1211`, not a second duplicate constraint; the zero-health terminal is already part of `SYS-578`.

### Information Genes

`INF-119` — The power meter exposes Mario's current condition before another risky segment or grab attempt.

`INF-179` — The following view exposes local path, rolling hazards, boss position, summit edge, coins and eventually the spawned Star. It does not reveal hidden later-course content.

### Objective Genes

`OBJ-262` — Defeat the first guardian under its throw rule and contact the separately spawned Power Star to record one retained progress token and leave the course.

### Time Genes

`TIM-003` — Mario's movement, hazards and guardian motion resolve on the running clock while controls continue; menu pausing is outside this live interval.

## Reproducible transitions

| Before | Action | Bounded resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Zero-Star Mario reaches the first castle painting | Jump into it | Enter Bob-omb Battlefield first-Star course | Painting is the course entry, not a free level selector | SM64-003 |
| A path segment is visually occluded | Press an eligible C button | Lakitu reframes nearby terrain while geometry remains fixed | Camera is information control, not topology mutation | SM64-002 |
| Mario is near a moving hazard with damaged power | Avoid it or contact an accessible coin | Collision may lower power; coin raises the count and heal reserve | Survival and optional recovery shape route choice | SM64-006 |
| Big Bob-omb is unactivated at the summit | Approach to trigger dialogue | The guardian becomes active and holdable | A visible boss is not yet an ordinary pickup | SM64-003, SM64-004 |
| Active guardian is approached from behind | Lift and throw onto summit | After landing, remaining boss health decreases by one | A legal attack has a separate impact resolution | SM64-004 |
| Active guardian is thrown off the summit | Wait for recovery | He returns; no counted hit is awarded | Ring-out is not victory | SM64-004 |
| Two valid summit throws have landed | Land one more valid throw | Boss reaches zero and a Star appears | Three is a parameter of a finite hit rule | SM64-004, SM64-005 |
| Spawned Star is visible but not yet collected | Touch it | First Star is credited and Mario returns to castle | Victory and reward acquisition are separate | SM64-005 |

## Strategic and experiential structure

The first mountain traversal teaches distance, steering and camera control before a close-range boss test. The final decision is not merely to throw: Mario must get behind a moving guardian and keep the landing on broad summit ground rather than launch him over its edge. Because the boss returns from an invalid throw, a failed attempt teaches a visible positional rule without consuming a credited hit. Damage on ascent or during grabs remains relevant, while accessible coins can offset it. The primary sources do not measure exact input frames, optimal camera settings or all possible shortcuts. SM64-002–SM64-007.

## Replay and variation

The authored first course, guardian health count and accepted summit are stable. The player may vary path, camera angle, optional coin pickups and exact throw positions. The packet does not assert procedural terrain, random boss health, a required cannon or a mandatory 100-coin route. SM64-003–SM64-007.

## Adjacent systems and history

The first painting sits in a larger castle with later Star doors and multiple courses, but this first-Star packet ends on its own retained token. Later Bob-omb Battlefield stars use cannon, red coins, caps and Chain Chomp interactions not required here. Bowser's later tail-throw encounter has a distinct attack target and cannot be treated as the same first guardian rule. The N64 source, European booklet and original-game route support the declared packet without asserting every port's parity. SM64-001–SM64-007.

## Normalised genome

| Type | Active gene IDs | Parameters |
|---|---|---|
| action | `ACT-008`, `ACT-610`, `ACT-611` | stick, Lakitu camera, rear grab |
| system | `SYS-036`, `SYS-037`, `SYS-045`, `SYS-578`, `SYS-1211` | live movement, nonterminal coins, power, valid landings |
| constraint | none | no duplicate of the system landing branch |
| information | `INF-119`, `INF-179` | local route and power meter |
| objective | `OBJ-262` | first spawned Power Star |
| time | `TIM-003` | live movement and encounter |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `459` (`GAME-0001`–`GAME-0459`).
- Exact genome matches: none.
- Tied near matches: `GAME-0389` — Mega Man 2 (`7 / 21 = 0.333333`).
- Supported combination subsets: none.
- Scan date: 2026-09-30.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0389` — Mega Man 2 | `ACT-008`, `SYS-036`, `SYS-037`, `SYS-045`, `SYS-578`, `INF-119`, `TIM-003` | Both have directly steered live platform movement, pickups, damage and health feedback. Mega Man 2 instead shoots through conveyor and timed-stage hazards to retain a boss weapon; this first Star requires player-reframed 3D ascent, a held guardian landed within the summit and separate contact with its reward. | Nearest by symmetric Jaccard, `7 / 21 = 0.333333`; no exact match. |

## Taxonomy impact

Four new boundaries in [TAXONOMY_CHANGE_197](../../../research/taxonomy-changes/TAXONOMY_CHANGE_197.md). No earlier definition or game signature is changed. Every earlier combination is scanned as a proper subset after index regeneration.

## Negative results

- No `ACT-095`: camera repositioning informs directly steered navigation; it does not rewrite legal geometry by screen alignment.
- No `ACT-048` or `ACT-297`: Big Bob-omb is a live, held opponent, neither an inert portable object nor an instantaneous fighting throw.
- No boss ring-out victory: an off-summit throw returns him without reducing the finite count.
- No later Bowser, cannon, Wing Cap, other-Star or DS-remake gene is imported into this first attempt.

## Delta summary

## New facts

- [Observation | Corroborated | High] The bounded original-N64 first-Star route joins player-reframed 3D navigation, finite guardian throws and a separate Star pickup; SM64-002–SM64-006.

## New genes

- [Observation | Corroborated | High] `ACT-610`, `ACT-611`, `SYS-1211` and `OBJ-262` isolate the camera command, live-opponent lift/throw, valid-arena impact and two-stage progress terminal.

## New combinations

- [Observation | Corroborated | High] No combination is admitted from one new carrier; existing proper-subset support is tested across the corpus.

## Taxonomy changes

- [Observation | Corroborated | High] `TAXONOMY_CHANGE_197` adds four bounded definitions without changing prior signatures.

## New questions

- Can a directly observed original US N64 attempt measure the precise camera and collision windows and distinguish regional variants without importing port behaviour?

## Next recommended game

- [Hypothesis | Limited | High] `GAME-0461` *The Sims* (2000), original Windows, is the next maintainer-approved unit after complete acceptance and the Goal stop window.
- Optimisation criterion: switch from authored 3D traversal to autonomous household resource allocation.
- Expected information gain: test whether first-home needs and assigned actions reuse the corpus's existing simulation genes before proposing any new boundary.
