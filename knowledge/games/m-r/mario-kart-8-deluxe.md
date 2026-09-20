---
game_id: GAME-0309
slug: mario-kart-8-deluxe
game_title: "Mario Kart 8 Deluxe"
analysis_status: reviewed
reviewed: 2026-09-19
combination_ids: []
gene_ids:
  action:
    - ACT-190
    - ACT-290
    - ACT-292
    - ACT-293
    - ACT-468
  system:
    - SYS-320
    - SYS-515
    - SYS-516
    - SYS-890
    - SYS-891
    - SYS-892
    - SYS-893
    - SYS-894
    - SYS-895
  constraint:
    - CON-438
  information:
    - INF-204
    - INF-205
    - INF-206
    - INF-208
    - INF-344
  objective:
    - OBJ-180
  time:
    - TIM-003
---

# Game: Mario Kart 8 Deluxe

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Mario, Standard
Kart, Standard Tires, Super Glider, 150 cc and Mushroom Cup are parameters or
product labels, not gene names.

## Analysis scope

- Version / ruleset: Nintendo's English Mario Kart 8 Deluxe base product,
  version `4.0.0`, on an original Nintendo Switch, offline single-player Grand
  Prix. Version `4.0.0` was the latest public update on 2026-09-19 and raises
  general race speed by the equivalent of one coin. Nintendo Switch 2 display,
  loading, controller and CameraPlay additions do not enter this target.
- Structured analysis target: original Nintendo Switch digital base product;
  see `GAME-0309` in
  [`knowledge/platforms/games.json`](../../platforms/games.json).
- Setup: choose Mario with Standard Kart, Standard Tires and Super Glider,
  select 150 cc Mushroom Cup, ordinary items and CPU rivals, and disable Smart
  Steering, Auto-Accelerate and Tilt Controls. Character and vehicle-part
  selection are fixed setup parameters rather than build-comparison genes.
- Entry: begin at the first controllable frame of Mario Kart Stadium after the
  start signal. The four-race sequence is Mario Kart Stadium, Water Park,
  Sweet Sweet Canyon and Thwomp Ruins.
- Primary decision loop: read the road, current place, lap, nearby rivals,
  coins, held-item order and warnings; steer, accelerate and brake; hold a
  drift through a useful corner and choose when to release its charged boost;
  route through coins, item boxes, shortcuts and anti-gravity contacts; decide
  whether to spend, aim or retain the active item while autonomous rivals and
  typed effects change spacing; complete each ordered three-lap course and
  revise the next line until all four results settle.
- Positive terminal: complete all four races with the highest cumulative
  driver-point total, receive the gold Mushroom Cup trophy and return to the
  Grand Prix course-selection surface where that 150 cc trophy is retained.
  A three-star rating is not required; exact points and trophy stars are
  result parameters.
- Negative terminal: a lower cumulative rank yields another trophy or no
  trophy and does not satisfy this packet. Quitting or restarting before the
  fourth result leaves no accepted positive trace; a later cup attempt is a
  separate trace.
- Included: one fixed driver/vehicle packet; 150 cc speed and CPU profile;
  four base Mushroom Cup courses; direct kart control; road, underwater,
  glider and anti-gravity movement; twelve-player autonomous field; three
  ordered laps per race; drift charge and release; capped course coins;
  ordinary and double item boxes; an ordered two-item inventory; position-
  sensitive random item acquisition; item attack, defence and acceleration
  effects; anti-gravity spin boosts; live place/lap/item/coin warnings;
  per-race points, cumulative standings, gold trophy and retained result.
- Excluded: Booster Course Pass courses and characters; Nintendo Switch 2
  hardware features; 50 cc, 100 cc, Mirror and 200 cc; every other cup; Time
  Trials, VS Race and Battle; local wireless, split-screen and online play;
  Custom Items; Smart Steering, Auto-Accelerate and Tilt Controls; vehicle
  optimisation, unlock grinding, amiibo, Mario Kart TV, highlight reels,
  statistics, records, achievements and complete-product mastery.
- Reproducible parameterisation: version `4.0.0`, original Switch, English,
  offline one-player Grand Prix, Mario, Standard Kart, Standard Tires, Super
  Glider, 150 cc, Mushroom Cup, assists off. During the cup demonstrate at
  least one charged mini-turbo release, one coin pickup, one single or double
  item-box acquisition and legal item use, and one anti-gravity spin boost.
  Complete each race's ordered three laps and stop after the first retained
  gold-trophy result. Exact item rolls, rival paths, contacts, coins, points
  and finishing order are parameters.
- Potential scoped modules: 200 cc brake drifting; Time Trial and ghosts;
  Battle; online or local multiplayer; Custom Items; Smart Steering; another
  cup; vehicle-stat optimisation; unlock progression; Booster Course Pass;
  Nintendo Switch 2 parity and a direct persistence check each need a separate
  scope.
- Direct-play status: not conducted. Nintendo's current product, support,
  update-history and beginner-technique pages directly establish the original
  Switch product, base/DLC boundary, controls, mini-turbo, item capacity and
  effects, coins, anti-gravity and assistance rules. Nintendo's preserved
  Mario Kart 8 manual establishes the inherited four-race Grand Prix points
  and trophy settlement, while a licensed written guide and static course
  records corroborate the exact Mushroom Cup sequence. No video or audio was
  opened, played, heard or analysed; no installed build, save or reload trace
  was available.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `MK8D-001` | The reviewed target is version 4.0.0 of Nintendo's base Mario Kart 8 Deluxe product on original Switch, not the Booster Course Pass or Switch 2 feature layer | Confirmed | Direct | High | P1, P2, P3 |
| `MK8D-002` | The bounded Mushroom Cup contains Mario Kart Stadium, Water Park, Sweet Sweet Canyon and Thwomp Ruins in that order | Confirmed | Corroborated | High | P1, S1, S2 |
| `MK8D-003` | Steering, throttle, brake, drift, mini-turbo release and item use remain direct player inputs when the three declared assists are off | Confirmed | Direct | High | P4, P5 |
| `MK8D-004` | Holding a drift charges visible mini-turbo tiers and releasing after a tier is reached produces its bounded acceleration burst | Confirmed | Direct | High | P4, P5 |
| `MK8D-005` | Touching item boxes can supply random race items into an ordered capacity of two, and a lower race position can expose stronger recovery items | Confirmed | Direct | High | P1, P5, P6 |
| `MK8D-006` | Held items resolve typed acceleration, attack, defence, control-loss or temporary-protection effects against the current race state | Confirmed | Direct | High | P5, P6 |
| `MK8D-007` | Collected course coins raise top speed up to a visible ten-coin race cap | Confirmed | Direct | High | P5, P6 |
| `MK8D-008` | In anti-gravity zones, eligible contact with a rival boosts both karts while contact with a marked object boosts the player kart | Confirmed | Direct | High | P5, P7 |
| `MK8D-009` | Each valid race finish awards place-dependent points, and the total after four races determines final cup rank and trophy | Confirmed | Corroborated | High | P7, S3, S4 |
| `MK8D-010` | The live and result surfaces expose place, lap, rivals, item order, coins, warnings, race points, standings and final trophy state | Observation | Corroborated | High | P5, P7, S1 |
| `MK8D-011` | No original-Switch installation, direct race, save or reload was observed for this unit | Confirmed | Direct | High | R1 |

## Basic data

- Release / origin: Nintendo developed and published Mario Kart 8 Deluxe for
  Nintendo Switch on 2017-04-28; the reviewed rules state is version `4.0.0`,
  released 2026-09-01 and checked 2026-09-19.
- Platform or physical form: original Nintendo Switch digital base product;
  one offline single-player Grand Prix cup.
- Puzzle family: physics and object manipulation; tactical forecast and
  counterplay; real-time system pressure; ordered dependency sequencing.
- Primary and official sources, accessed 2026-09-19:
  - **[P1]** [official Mario Kart 8 Deluxe site](https://mariokart8deluxe.nintendo.com/),
    for original Switch product identity, Grand Prix, Smart Steering, the 48
    base-course boundary and the separate paid Booster Course Pass.
  - **[P2]** [Nintendo update history](https://en-americas-support.nintendo.com/app/answers/detail/a_id/26098/),
    for version `4.0.0`, its date, original-Switch applicability, the one-coin
    speed-equivalent change and the separable Switch 2 additions.
  - **[P3]** [Nintendo Booster Course Pass page](https://www.nintendo.com/us/store/products/mario-kart-8-deluxe-booster-course-pass-70070000013723-switch/),
    for the paid DLC boundary excluded from the base Mushroom Cup.
  - **[P4]** [Nintendo basic-controls support](https://support-jp.nintendo.com/app/answers/detail/a_id/34439),
    for throttle, brake, steering, held drift, spark-conditioned mini-turbo
    release and item-use inputs.
  - **[P5]** [Nintendo beginner mechanics guide](https://www.nintendo.com/jp/ichikara/aabpa/index_en.html),
    for drift tiers, Smart Steering limitation, items, two-slot holding,
    coins, glider control, course boosts and anti-gravity spin boosts.
  - **[P6]** [Nintendo item catalogue](https://www.nintendo.com/jp/switch/aabpa/sp/item/index.html),
    for the two-item limit and typed Banana, shell, Mushroom, Coin, Boo,
    Lightning and related effects used as the item-system boundary.
  - **[P7]** [Nintendo's preserved Mario Kart 8 manual](https://www.nintendo.com/eu/media/downloads/games_8/emanuals/wii_u_6/mario_kart_8/ElectronicManual_WiiU_MarioKart8_EN.pdf),
    for the inherited direct controls, race HUD, anti-gravity, per-finish
    points, four-race total, final standings and trophy settlement.
- Corroborating static written sources, accessed 2026-09-19:
  - **[S1]** [official My Nintendo starter-guide listing](https://my.nintendo.com/rewards/d4b0b34ad9db8373?lang=en-US)
    and its authorised guide, for base-course grouping, controls, items and
    Mushroom Cup sequence. The guide was read as text; no art was copied.
  - **[S2]** [Prima Mushroom Cup guide](https://primagames.com/eguides/mario-kart-8-deluxe-eguide/the-tracks/mushroom-cup),
    for the four-course order and course-specific drift, underwater, glider
    and anti-gravity observations.
  - **[S3]** [Prima Grand Prix guide](https://primagames.com/eguides/mario-kart-8-eguide/the-drivethrough/grand-prix-and-time-trials/grand-prix),
    for the 150 cc Grand Prix speed class and finish-place point schedule.
  - **[S4]** [Mario Kart 8 Deluxe Grand Prix rules record](https://wikiwiki.jp/mk8d/%E3%82%B0%E3%83%A9%E3%83%B3%E3%83%97%E3%83%AA),
    for cumulative four-race ranking, trophy classes and star thresholds.
- Research record: **[R1]** 2026-09-19 local preflight found no original
  Switch installation, entitlement, save, controller trace or reload result.
- Claim IDs: `MK8D-001`–`MK8D-011`.

## Mechanical decomposition

### Action Genes

- Existing `ACT-290` covers steering, throttle and braking the dedicated kart;
  `ACT-292` fixes the 150 cc profile and turns the three assistance options
  off; and `ACT-293` commits the available Mushroom Cup as one bounded driving
  event. `ACT-190` commits the current carried race item's legal direction or
  no-target activation.
- New `ACT-468` holds a live drift while steering, then releases it at a chosen
  visible charge tier rather than storing a freely spendable boost reserve.
- Parameters: character, kart parts, speed class, assists, cup, item identity,
  item direction, drift direction, charge tier and release timing. Claims:
  `MK8D-002`–`MK8D-006`.

### System Behaviour Genes

- Existing `SYS-320` integrates road, underwater, glider and anti-gravity kart
  motion and contact; `SYS-515` continuously drives eleven CPU rivals;
  `SYS-516` accepts each three-lap ordered route and settles its finish place.
- New `SYS-890` turns eligible item-box contact into a hidden, race-state-
  weighted item result and fills the active-first two-slot queue. `SYS-891`
  resolves the committed item's typed vehicle, rival or course effect.
- New `SYS-892` advances the held drift through visible charge tiers and turns
  release into the corresponding bounded mini-turbo. `SYS-893` raises current
  top speed from collected course coins up to the ten-coin cap. `SYS-894`
  converts eligible anti-gravity rival/object contact into the declared shared
  or unilateral spin boost.
- New `SYS-895` converts every classified place into points, carries the total
  across the fixed four-race cup and settles final rank, trophy and stars.
- Resolution order: lock cup/profile/vehicle; release one race; integrate kart
  and rival motion; resolve drift, coins, item-box results, item effects and
  anti-gravity contact; validate three laps; award points; advance to the next
  course; after race four settle cumulative rank and retained trophy. Claims:
  `MK8D-004`–`MK8D-010`.

### Constraint Genes

- Existing `CON-438` requires each race to complete its ordered three laps
  before the finish place is accepted. The cup's fixed four-course order and
  the two-item capacity are owned by `SYS-895` and `SYS-890`, not independent
  player legality boundaries.
- Scarce strategic resources: course distance, carried speed, coin count,
  current place, two item slots, item timing and remaining point opportunities.
  Claims: `MK8D-002`, `MK8D-005`, `MK8D-007`, `MK8D-009`.

### Information Genes

- Existing `INF-204` exposes speed and road/course geometry; `INF-205` exposes
  current place, lap, course progress and nearby rivals; `INF-206` exposes the
  selected speed class, cup, course set and setup terms; `INF-208` exposes
  race points, cumulative standing and final trophy settlement.
- New `INF-344` exposes the current ordered item pair, coin count and incoming
  attack warnings without revealing future item rolls or rival decisions.
- Claims: `MK8D-003`–`MK8D-010`.

### Objective Genes

- New `OBJ-180` requires completing the fixed four-race cup with the highest
  cumulative point total and retaining its gold trophy. Winning every race or
  earning three stars is not required by the objective boundary.
- Success, evaluation and failure: every valid finish contributes its ranked
  points; only the post-fourth-race aggregate classifies the cup. Gold is
  positive; a lower aggregate rank, quit or restart is not. Claims:
  `MK8D-002`, `MK8D-009`, `MK8D-010`.

### Time Genes

- Existing `TIM-003` covers continuously changing kart motion, rivals, drift
  charge, item threats and course position while player inputs remain live.
  Claims: `MK8D-003`–`MK8D-010`.

## Reproducible transitions

| Before | Action | Resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Original-Switch base product exposes Mushroom Cup | Choose fixed driver/parts, 150 cc and assists off, then commit the cup | Mario Kart Stadium loads as race one of the fixed four-course sequence | exact packet contract | `MK8D-001`–`MK8D-003` |
| Kart enters a useful corner | Hold drift while steering | Sparks advance through visible charge tiers while the live line continues | coupled motion and temporary charge | `MK8D-004` |
| A charge tier is active | Release drift | The charge clears and its tier produces a bounded acceleration burst | mini-turbo is not banked nitro | `MK8D-004` |
| At least one item slot is free | Touch an ordinary or double item box | A hidden race-state-weighted roll fills one or both available ordered slots | bounded random tactical supply | `MK8D-005` |
| One item is active and another may be reserved | Use or directionally release the active item | Its typed boost, obstruction, projectile, protection or rival-control effect resolves; the reserve advances | common item queue, diverse effects | `MK8D-005`, `MK8D-006` |
| Fewer than ten coins are held | Route through a course coin | Coin count rises toward ten and the kart's current top-speed modifier increases | capped route resource | `MK8D-007` |
| Kart is inside an anti-gravity zone | Contact a rival or marked blue object | Rival contact boosts both karts; object contact boosts only the player kart | contact can be advantageous | `MK8D-008` |
| Two laps and the ordered course are complete | Cross the finish after lap three | Place is classified and converted to race points; the next Mushroom Cup course loads | per-race settlement inside cup | `MK8D-002`, `MK8D-009` |
| Thwomp Ruins finishes as the fourth valid race | Accept the cup result | Four point awards are totalled and final standing, trophy and star class appear | aggregate rather than last-race terminal | `MK8D-009`, `MK8D-010` |
| Cumulative standing is first | Return from the gold-trophy result | The 150 cc Mushroom Cup gold result remains recorded on the Grand Prix surface | positive retained terminal | `MK8D-009`, `MK8D-010` |

## Strategic and experiential structure

- Local decision: choose line, drift duration, item timing and whether a coin,
  item box, shortcut or anti-gravity contact is worth the immediate risk.
- Medium-term planning: retain defensive or acceleration items, build coin
  speed and manage rival spacing across the remaining laps rather than
  optimising one isolated corner.
- Long-term structure: maximise the four-race point total; one poor finish can
  be recovered by later standings, so the final race alone is not the cup.
- Common heuristics: release a charged drift only onto a controllable exit;
  preserve a defensive item near the lead; use stronger recovery items from
  the rear to regain positions; take coins early when route cost is acceptable.
- Failure attribution: missed lap order, overlong drift, item misuse, collision,
  low coin speed, rival item timing or insufficient aggregate points remain
  separately visible causes.
- Player trust: sparks, item slots, coin counter, attack warnings, lap/place
  HUD, race points and final standings expose every accepted boundary except
  the intentionally hidden future item roll.

## Replay and variation

- What changes: item rolls, rival spacing, contacts, coin route, drift timing,
  finishing positions, cumulative points and trophy stars.
- Randomness or procedural generation: course geometry and order are fixed;
  item results and autonomous race trajectories vary within the rules.
- Multiple viable strategies: clean front-running, defensive item retention,
  riskier item-box/coin lines and rear-field recovery can all produce gold.
- Replay motive: higher star class, another speed class, vehicle combination,
  cup, Time Trial, multiplayer or DLC lies outside this bounded first result.

## Adjacent systems and history

- Need for Speed Underground and Forza Horizon 5 share direct arcade vehicle
  control, autonomous rivals, ordered laps, live race HUD and a retained
  winning result. Mario Kart adds temporary drift charge, capped coins,
  position-sensitive two-slot items, advantageous anti-gravity contacts and a
  four-race aggregate trophy.
- Asphalt Legends shares drift-derived acceleration and a position objective,
  but its nitro becomes a freely timed stored reserve and TouchDrive owns most
  steering; Mario Kart's mini-turbo is tied to release of the current drift.
- Need for Speed: The Run also aggregates several driving events, but reduces
  an authored campaign route rank through required passing gates instead of
  converting every finish place into a cup table.

## Normalised genome

| Type | Active gene IDs | Parameters |
|---|---|---|
| Action | `ACT-190`, `ACT-290`, `ACT-292`, `ACT-293`, `ACT-468` | item use, direct kart control, 150 cc profile, cup and drift release |
| System Behaviour | `SYS-320`, `SYS-515`, `SYS-516`, `SYS-890`, `SYS-891`, `SYS-892`, `SYS-893`, `SYS-894`, `SYS-895` | motion, rivals, laps, item supply/effects, drift, coins, anti-gravity and cup score |
| Constraint | `CON-438` | ordered three-lap validity |
| Information | `INF-204`, `INF-205`, `INF-206`, `INF-208`, `INF-344` | road, place, cup terms, items, coins and result |
| Objective | `OBJ-180` | gold four-race cup |
| Time | `TIM-003` | continuous race state |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `308` (`GAME-0001`–`GAME-0308`).
- Exact genome matches: none.
- Tied near matches: `GAME-0217` — Need for Speed Underground (`12 / 24 = 0.500000`).
- Supported combination subsets: none.
- Scan date: 2026-09-19.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0217` — Need for Speed Underground | `ACT-290`, `ACT-292`, `ACT-293`, `SYS-320`, `SYS-515`, `SYS-516`, `CON-438`, `INF-204`, `INF-205`, `INF-206`, `INF-208`, `TIM-003` | Both expose direct real-time circuit driving, configured race entry, autonomous rivals, ordered laps and visible race state. Mario Kart adds live drift charging, random queued items, coins, anti-gravity contact and a four-race cumulative trophy; Underground instead resolves one two-lap event with its separate speed-resource and career reward boundaries. | Near, `0.500000` |

### Preserved research notes

- New genes: `ACT-468`, `SYS-890`–`SYS-895`, `INF-344`, `OBJ-180`.
- Classification result: new combination with nine evidenced reusable
  boundaries for kart-specific tactics and four-race settlement.
- Evidence and reasoning: character, kart, course names, speed class, item
  identities and numeric values remain parameters; the new boundaries capture
  transferable control, hidden supply, resource and aggregate-result rules.

## Taxonomy impact

- Registry changes: add nine Active genes and Mario Kart support to compatible
  existing driving boundaries; no prior signature or lifecycle changes.
- Taxonomy-change record: none; existing definitions are not broadened beyond
  their current parameter spaces.
- Candidate terms affected: Mario, Standard Kart, 150 cc, Mushroom Cup, named
  courses, individual item names, ten coins and trophy-star thresholds remain
  instance labels or values.

## Negative results

- No installed original-Switch build, direct input trace or reload exists, so
  exact default menu state, roll weights, rival paths and persistence timing
  are not asserted.
- Version `4.0.0` changes general race speed; no pre-update performance values
  are imported into this current packet.
- Exact hidden item probability tables and tie-break implementation are not
  required by the gold-cup trace and remain unclaimed.
- Wii U material is used only for inherited Grand Prix/anti-gravity rules that
  current Deluxe sources corroborate; Wii U content, controls and platform
  identity do not enter the analysis target.

## Delta summary

## New facts

- [Confirmed | Direct | High] Current Nintendo material establishes direct
  kart/drift/item controls, mini-turbo tiers, two held items, capped coins and
  anti-gravity spin boosts (`MK8D-001`, `MK8D-003`–`MK8D-008`).
- [Confirmed | Corroborated | High] Four classified races contribute points to
  the cumulative cup standing and trophy (`MK8D-002`, `MK8D-009`, `MK8D-010`).

## New genes

- [Confirmed | Direct | High] `ACT-468` isolates hold-and-release drift timing;
  `SYS-890`–`SYS-895` isolate item supply/effects, mini-turbo, coins,
  anti-gravity contact and cup scoring; `INF-344` exposes tactical race state;
  `OBJ-180` closes the four-race gold-trophy packet.

## New combinations

- [Observation | Corroborated | Medium] No verified combination is asserted;
  the deterministic subset scan is recorded above.

## Taxonomy changes

- [Confirmed | Direct | High] No earlier game signature or lifecycle changes;
  compatible existing driving records gain only a new support citation.

## New questions

- Which exact item probability tables and cup tie-break sequence does version
  `4.0.0` apply in an observed offline 150 cc run?
- Does the gold trophy reproduce identically after an observed save close and
  relaunch on original Switch hardware?

## Next recommended game

- [Hypothesis | Limited | Medium] `GAME-0310` — DEATH STRANDING DIRECTOR'S CUT,
  Windows edition.
- Optimisation criterion: contrast a compact four-race tactical aggregation
  with a source-bounded traversal-and-delivery packet.
- Backlog impact: `GAME-0310` remains next; no later unit starts in this commit.

## Why this game

- [Hypothesis | Limited | Medium] Mario Kart 8 Deluxe tests whether an iconic
  arcade racer decomposes into established vehicle/race genes plus portable
  drift, item, coin, contact and aggregate-cup boundaries without treating
  characters or tracks as mechanics.
