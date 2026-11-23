---
game_id: GAME-0519
slug: power-stone
game_title: Power Stone
analysis_status: reviewed
reviewed: 2026-11-16
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-048
    - ACT-161
    - ACT-223
    - ACT-294
    - ACT-297
    - ACT-355
    - ACT-714
  system:
    - SYS-037
    - SYS-215
    - SYS-522
    - SYS-1477
    - SYS-1478
    - SYS-1479
    - SYS-1480
    - SYS-1481
    - SYS-1482
    - SYS-1483
  constraint:
    - CON-446
    - CON-798
  information:
    - INF-210
    - INF-504
  objective:
    - OBJ-099
  time:
    - TIM-003
---

# Game: Power Stone

Use the [canonical vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
Stone colours, fighter identity, clock length and arena scenery specify the
instances.

## Analysis scope

- Version / ruleset: original 1999 North American English Dreamcast retail
  release, Capcom product T-1201N, local Versus, two human-controlled fighters,
  default three-stone rules, timer at 99, first to two round wins, standard
  controls and items. The exact disc build and frame-level timing are unverified.
- Structured analysis target: `PLAT-DREAMCAST`, original North American game.
- Primary decision loop: route around the opponent and scenery, choose a
  normal attack, contextual interaction or arena weapon, and contest the
  three stones. A suitable hit releases a held stone for either player to
  collect. The complete set changes combat form. Use smaller powered attacks
  or spend the remainder on a finisher, then contest the released stones or
  settle the round through vitality.
- Entry and exit: choose Falcon in port A, Gunrock in port B and Londo in
  local Versus. Start at the first controllable round and finish on the
  match result after the second credited win, before a rematch or selection.
- Included: 3D repositioning, jumps, ordinary attacks and throws, dodge
  input, Londo scenery attacks and character-dependent prop access, temporary
  equipment, catch, contact acquisition and forced stone drops, automatic
  transformation, powered budgeting and return to ordinary play, regional
  pickup cue, recoverable vitality, round clock and match settlement.
- Excluded: Arcade ladder and bosses, other arenas or fighters as independent
  cases, unlockable Extra Options, collectible items from the Collection
  book, VMU games, nonstandard crystals, the NAOMI original, PSP, Power Stone 2
  and the later Capcom collection. No exact item weighting, frame counts or
  equal-vitality timeout policy established.
- Potential scoped modules: Arcade boss conditions and unlock progression,
  or alternate four- and five-stone settings after unlock.
- Direct-play status: Capcom's contemporary documentation and translated
  producer interview establish product lineage and design. Contemporary
  Dreamcast reporting and authored guides corroborate the home rules.
  No console, executable, video or audio was played.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| PS-001 | Capcom released the Dreamcast port in 1999. The North American product listing identifies T-1201N. The producer describes work adapting the arcade version. | Confirmed | Corroborated | High | P1, P2, R1 |
| PS-002 | Local Versus selects two fighters and one stage with two controllers. The normal match uses a 99-second round, KO or remaining-vitality adjudication at time-over and two required wins. The exact tied-health result is unverified. | Observation | Corroborated | High | R2, R3, R4 |
| PS-003 | Movement across Londo and height changes coexist with normal punches, kicks, short attack sequences, grabs, throws, and active avoidance. The ordinary defensive set has no standing guard. | Observation | Corroborated | High | P1, R2, R3, R4, R5 |
| PS-004 | Nearby interactables supply throws or fixture-specific moves. Reach, prop and character determine the option. A timely grab can catch an eligible incoming prop. | Observation | Corroborated | High | P1, P3, R2, R3, R4 |
| PS-005 | Fighters start with one stone each. A neutral third appears after the round begins. A qualifying hit on a carrier releases a stone into shared space. Contact claims a loose stone, and all three trigger a form change. | Observation | Corroborated | High | P1, R2, R3, R4, R5, R6 |
| PS-006 | Powered attacks replace normal inputs. Time and ordinary powered attacks reduce the gauge. A Power Fusion spends its remainder, and depletion ends the form and returns the stones to the arena. | Observation | Corroborated | High | R2, R3, R4, R5 |
| PS-007 | Treasure chests provide temporary usable items. Eligible weapons have finite use gauges and can be lost on a hit. A time-fused bomb is a different instance. | Observation | Corroborated | High | P3, R2, R3, R5 |
| PS-008 | The life display separates a recoverable portion inside the active jewel segment. Surviving without another hit can recover that portion. A lost segment is removed. | Observation | Corroborated | Medium | R2, R3 |
| PS-009 | Stone slots and the powered gauge show each side's current resource. A floor locator gives approximate loose-stone positions, distinct from the visible stone itself. | Observation | Corroborated | High | R2, R3, R4 |

## Basic data

- Release / origin: Capcom, 1999, local two-player Dreamcast release.
- Platform: Sega Dreamcast, original North American T-1201N retail.
- Puzzle family: tactical forecast and counterplay, object manipulation,
  and pressure from a running clock and finite form state.
- Primary references:
  - P1 [1999 Takeshi Tezuka interview, translated by shmuplations](https://shmuplations.com/powerstone/),
    arena freedom, stage design, transformation counterplay, and port adaptation.
  - P2 [Capcom 1999 annual report](https://www.capcom.co.jp/ir/english/data/pdf/Annual1999.pdf),
    p. 7, distinguishes the arcade project and home version.
  - P3 [Capcom's contemporary Power Stone advertisement](https://www.kingpin.info/download/kingpin/media/magazine/NEXT_Generation_Issue_58_%28USA%29_1999-10.pdf),
    Dreamcast branding and portable scenery, lamppost and wall interactions.
- Independent practical references:
  - R1 [GameFAQs Dreamcast release data](https://gamefaqs.gamespot.com/dreamcast/198332-power-stone/data),
    T-1201N identifier and region. Use the year without asserting one regional
    retail day, because period sources date distribution differently.
  - R2 [Chris Murdock Dreamcast guide](https://gamefaqs.gamespot.com/dreamcast/198332-power-stone/faqs/482),
    §§ 2–7, first-hand rules and parameters from the launch period with some
    import terminology.
  - R3 [cnick's Dreamcast guide](https://gamefaqs.gamespot.com/dreamcast/198332-power-stone/faqs/7589),
    §§ II, III, V and VI, Versus resolution, pressure, moves and Londo.
  - R4 [Clement Chan's Dreamcast guide](https://gamefaqs.gamespot.com/dreamcast/198332-power-stone/faqs/9554),
    §§ 2.1–2.7 and Falcon and Gunrock, power depletion and catch.
  - R5 [GameSpot's contemporary Dreamcast review](https://www.gamespot.com/reviews/power-stone-review/1900-2540483/),
    movement, transfer to arena, replenishment and powered attack roles.
  - R6 [GameRevolution's September 1999 Dreamcast review](https://www.gamerevolution.com/review/32228-powerstone-review),
    two initial holders, a delayed third stone and arena interactions.
- Claim IDs: PS-001–PS-009.

## Mechanical decomposition

### Action Genes

- `ACT-294` assigns fighters and participant sides. `ACT-008` steers movement
  across the arena. Jump and contextual movement give height changes.
- `ACT-161` initiates normal punches and kicks or uses a held weapon.
  `ACT-223` makes an active evasion choice on an incoming threat.
  `ACT-297` covers the legal close throw branch. No particular throw break
  or invisible input priority is asserted.
- `ACT-048` handles a portable arena prop, including carrying and release.
  `ACT-355` claims a reachable spawned weapon or abandons it for ordinary
  control. `ACT-714` attempts the timed catch of a reachable thrown prop.
- Claim IDs: PS-002–PS-004, PS-007.

### System Behaviour Genes

- `SYS-215` resolves real-time contacts, normal attack chains, knockback and
  defeat. `SYS-1477` resolves compatible scenery attacks at a wall or pole.
  Falcon's swing draws a trajectory from a fixed pole. Gunrock can use a
  removable pole as a heavy prop where eligible.
- `SYS-037` claims a loose stone on contact. `SYS-1478` ejects a held stone
  on a qualifying impact. An aerial kick supplies a documented example.
  The released stone belongs to neither side until someone collects it.
- `SYS-1479` automatically substitutes the form and moves when one fighter
  holds all three. Transformation retains the duel vitality relation.
  `SYS-1480` drains one powered budget through time and Drive use. Fusion
  spends the remaining positive budget and commits the stronger move.
  `SYS-1481` restores ordinary control and re-releases the set at depletion.
  Delay can let the opponent avoid powered contact until the set returns.
- `SYS-1482` lets eligible recent health loss inside the active segment
  recover during a no-hit interval. Expending an entire segment removes it.
  `SYS-1483` uses up eligible temporary weapon capacity or disarms the
  fighter after a hit before capacity is exhausted.
- `SYS-522` adjudicates rounds, credits the result, and starts a fresh round
  with the default resource reset until the match settles.
- Claim IDs: PS-002–PS-009.

### Constraint Genes

- `CON-446` bounds rounds by vitality and clock, and the match by two wins.
- `CON-798` gates the use branch by scenery identity, reach and the current
  fighter's permission. A fixture can admit a swing for one fighter and
  lifting for another. An ordinary chair can be carried as a prop.
- Claim IDs: PS-002, PS-004, PS-008.

### Information Genes

- `INF-210` exposes vitality and recovery, timer, round progress and stone
  possession or current powered budget in the live display.
- `INF-504` exposes approximate loose-stone regions on a small locator.
  Direct scene inspection still provides the exact route and obstacles.
- Claim IDs: PS-002, PS-008, PS-009.

### Objective Genes

- `OBJ-099` is first to two wins against the fixed opponent. Empty rival
  vitality wins the round, and higher remaining vitality wins a time-over.
  Stone acquisition changes the options available during the round.
- Claim IDs: PS-002, PS-005, PS-006.

### Time Genes

- `TIM-003` permits continuous movement, attacks, object interactions and
  defensive replies as the round progresses. The transformed budget
  decreases on a different rule from the round's remaining time.
- Claim IDs: PS-002, PS-003, PS-006.

## Reproducible transitions

| Before | Action | Resolution | What it establishes | Claim |
|---|---|---|---|---|
| Two ordinary fighters each hold one stone | Keep the opening round active and move toward the yellow stone when it appears | Its first collector holds two stones | Reaching the neutral stone alone is insufficient for transformation | PS-005 |
| The opponent holds a stone and is in range | Land the ordinary aerial kick | A stone becomes a free arena object | The hit does not credit the stone to the attacker | PS-005 |
| One fighter holds two stones | Contact the last available stone | The complete set automatically activates powered moves and a gauge | Threshold selection is automatic | PS-005, PS-006 |
| The form is active with positive budget | Use a Drive attack, then choose an eligible Fusion while some budget remains | Drive reduces the budget and Fusion consumes what remains | The attacks trade remaining uptime for their effects | PS-006 |
| The form is active | Keep moving until the meter depletes | Ordinary form returns and the three stones are available again | The same round can race for another charged form | PS-006 |
| Falcon is at a reachable Londo pole | Use the fixture action | Falcon swings into his contextual attack | The environment changes the resolved action | PS-003, PS-004 |
| A reachable light prop is coming toward the fighter | Use the catch input with suitable timing | The prop becomes held | A successful catch changes ownership without adding a new prop | PS-004 |
| An eligible active jewel segment has recent partial damage | Avoid another hit while the recoverable portion remains | Some vitality can come back within the segment | Losing the whole segment removes that recovery opportunity | PS-008 |
| One fighter has already won a round | Reduce the opponent to zero vitality, or reach timeout with more vitality | Second credited win settles the match | Items and form provide leverage without being the victory rule | PS-002 |

## Strategic and experiential structure

The neutral stone gives a route target, while hitting the other carrier
creates a second contestable object. Picking up a temporary weapon gives
an alternative to a direct approach. A lead in vitality can justify
spacing away from a powered fighter until the resource returns. If a
Fusion misses, its budget is still exhausted. Use the locator to plan a
route around Londo's fountain, walls and local obstacles. PS-002–PS-009.

## Replay and variation

The fighters, rules and stage are held constant. Free-stone positions,
contested contacts, available chest items and the resulting transformations
vary in play. The sources give no verified random seed, exhaustive placement
set or precise encounter-gauge cost. PS-004–PS-009.

## Adjacent systems and history

Versus shares the normal vitality, timer and round result structure with
other two-fighter games. Londo places a recyclable resource and usable
scenery inside the same arena. Movement can be used tactically to deny
objects, avoid a powered attack or reach a released stone after a hit.
Measured neighbours are recorded below.

## Normalised genome

| Type | Active gene IDs | Parameters |
|---|---|---|
| Action | ACT-008, ACT-048, ACT-161, ACT-223, ACT-294, ACT-297, ACT-355, ACT-714 | Steer, handle a prop, attack, evade, set the match, throw, equip and catch |
| System Behaviour | SYS-037, SYS-215, SYS-522, SYS-1477, SYS-1478, SYS-1479, SYS-1480, SYS-1481, SYS-1482, SYS-1483 | Contact, combat, rounds, scenery, forced drop, form, budget, release, vitality and temporary weapon |
| Constraint | CON-446, CON-798 | Stop rules and fighter-specific scenery access |
| Information | INF-210, INF-504 | Duel HUD and loose-stone locator |
| Objective | OBJ-099 | First to two against one selected opponent |
| Time | TIM-003 | Simultaneous continuous input under timed progression |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `518` (`GAME-0001`–`GAME-0518`).
- Exact genome matches: none.
- Tied near matches: `GAME-0351` — Street Fighter II: The World Warrior (`9 / 30 = 0.300000`).
- Supported combination subsets: none.
- Scan date: 2026-11-16.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0351` Street Fighter II: The World Warrior | ACT-008, ACT-294, ACT-297, SYS-215, SYS-522, CON-446, INF-210, OBJ-099, TIM-003 | Both use ordinary strikes, throws, a round clock and win markers in a fixed duel. Street Fighter II constrains spacing on a side-view plane with ordinary guard choices. Power Stone lets the fighters route through a 3D arena, contest objects and spend a temporary form that returns its three stones to play. | Near, `0.300000` |

## Taxonomy impact

- [TAXONOMY_CHANGE_266](../../../research/taxonomy-changes/TAXONOMY_CHANGE_266.md)
  records ten additions and fourteen unchanged transfers.

## Negative results

- No passive standing block is documented in the ordinary Versus controls.
  Active movement and evasion matter before contact.
- Power Stone 2's four-player arenas, arena transitions and item mixing
  are outside this record. Extra Options can change the stone supply after
  unlock. The selected match uses three stones.
- The documents support a delay before the neutral stone appears and a
  running powered meter. No exact delay, damage or tie policy is assigned.

## Delta summary

## New facts

- [Observation | Corroborated | High] A qualifying hit releases a stone
  which either fighter can reach. The complete set automatically powers a
  fighter, and form depletion returns it to contestable space. PS-005, PS-006.
- [Observation | Corroborated | High] Power Drive and Power Fusion use the
  same active meter. The first spends a portion and the second spends its
  remainder. PS-006.

## New genes

- ACT-714, SYS-1477–SYS-1483, CON-798 and INF-504.

## New combinations

- No new combination. The subset scan records supported prior signatures.

## Taxonomy changes

- Ten boundaries distinguish object competition from permanent progress
  or once-per-round powered state.

## New questions

- Run an unmodified North American disc at a recorded revision to check
  equal-vitality timeout, the relocation list and the rate of gauge depletion.

## Next recommended game

- `GAME-0520` Animal Well, released Nintendo Switch base game.

## Why this game

- [Hypothesis | Limited | Medium] A circulating shared resource makes attack,
  evasion and geography change each other's value within the same round.
