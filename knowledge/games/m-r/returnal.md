---
game_id: GAME-0522
slug: returnal
game_title: Returnal
analysis_status: reviewed
reviewed: 2026-11-17
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-161
    - ACT-199
    - ACT-341
    - ACT-719
  system:
    - SYS-037
    - SYS-215
    - SYS-456
    - SYS-464
    - SYS-469
    - SYS-578
    - SYS-1493
    - SYS-1494
    - SYS-1495
    - SYS-1496
    - SYS-1497
    - SYS-1498
  constraint:
    - CON-349
    - CON-801
  information:
    - INF-119
    - INF-180
  objective:
    - OBJ-026
  time:
    - TIM-003
---

# Game: Returnal

Use the [canonical vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
Controller buttons, room layouts, item names and meter levels are parameters.

## Analysis scope

- Version / ruleset: April 30, 2021 launch-era English PlayStation 5 base
  campaign, fresh save, offline solo, default DualSense mapping. The installed
  executable and exact launch patch were not inspected.
- Structured analysis target: `PLAT-PLAYSTATION-5`, original PS5 campaign.
- Primary decision loop: inspect an authored room and its exits, move and dash
  while firing the current weapon, choose whether to replace it or route to
  supplies, and manage primary recharge, the Overload window and the newly
  unlocked Alt-Fire. Follow the main path to the weapon charger and clear its
  teaching gate. On true death, return to Helios with the persistent capability
  and rebuild the temporary combat state.
- Entry and exit: start at first control after the crash. Take the initial
  sidearm, shoot the tutorial switch and take the ordinary loss branch at the
  opening Titanops. Continue in the new cycle to acquire the Atropian Weapon
  Charger, use Alt-Fire on the gate growth and cross. Sample ordinary combat
  and a weapon or pickup when available, then take the first true death after
  the charger, before installing any further permanent equipment, and stop at
  the next controllable return to Helios. Inspect the retained equipment and the reset combat state. There is no fixed itinerary
  after the guided rooms. Defeating the tutorial Titanops is possible.
- Included: aim and fire, protected eligible dash, one active gun and swaps,
  shot recharge and timed Overload, separated Alt-Fire unlock and cooldown,
  encounter resources, Adrenaline, Integrity and Resin, cycle proficiency and
  retained weapon traits, explored room and door cues, modular room layout,
  and the first post-charger death. Ether and Obolites are compared if found.
- Excluded: later permanent equipment including the Atropian Blade, the
  house, Phrike, every later biome, Reconstructor or revival items, optional
  devices, parasite and Malfunction builds, trophy routes, Suspend Cycle,
  Ascension, co-op, PC and later rule changes. Exact seeds, frame lengths,
  thresholds per weapon variant and the alternate tutorial victory route
  are outside the verified packet.
- Potential scoped modules: paid in-cycle revival, Blade traversal,
  Malfunction removal and the first biome boss as separate studies.
- Direct-play status: no direct play, video or audio. Housemarque's written
  documentation establishes mechanics. Written release-era guides and a
  later PS5 walkthrough reconstruct progress landmarks. No single reported
  room layout is treated as the launch game's only legal route.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|
| `RET-001` | PS5 launched on April 30, 2021. The studied base campaign predates Suspend Cycle and the Ascension modes. | Confirmed | Direct | High | P1, P3, P5, P6 |
| `RET-002` | The initial route supplies a pistol and a shot-operated switch. The first Titanops can kill the player and cause return. Beating it is possible. The guided charger follows either route, although the intervening rooms can vary. | Observation | Corroborated | Medium | P4, R1, R2 |
| `RET-003` | Moving, aiming and shooting resolve while enemies attack. An eligible dash avoids most projectile hits. Holding a second replacement gun is not allowed. | Observation | Corroborated | High | P2, P3, R1 |
| `RET-004` | Empty primary shots start a recharge without consuming a carried ammunition reserve. During recharge an indicated second shot-button press can complete it early. A miss does not award early readiness. | Observation | Corroborated | High | P4, R1, R4 |
| `RET-005` | Half L2 prepares focused primary aim, full L2 prepares Alt-Fire and R2 fires after the charger is acquired. Alt-Fire is tied to the weapon instance and recharges on its own timer. | Confirmed | Corroborated | High | P2, P3, P4, R5 |
| `RET-006` | The charger is permanent equipment. The tutorial uses Alt-Fire on growth blocking a door. The incoming cycle retains Alt-Fire access even if the selected gun instance is replaced. | Observation | Corroborated | High | P2, R1, R2, R5 |
| `RET-007` | Ordinary damage reduces Integrity and clears unprotected Adrenaline. Groups of three kills without damage raise Adrenaline up to five. Silphium generally heals, but at full Integrity eligible pickups count as Resin. A complete Resin threshold raises run maximum Integrity. | Observation | Corroborated | High | P3, P4, R1, R4 |
| `RET-008` | Within-cycle weapon proficiency sets potential strength of later drops. Earned weapon-trait unlocks persist for eligible future finds, separately from proficiency and the actual weapon. | Observation | Corroborated | High | P2, P3, R3, R4 |
| `RET-009` | Authored rooms assemble into varying routes, with mandatory milestones. The map shows explored links and distinct main and side route doors. | Observation | Corroborated | High | P2, P4, R1 |
| `RET-010` | True death in the first biome returns control near Helios and clears the run's weapon, temporary pickups, increased maximum Integrity, proficiency and Obolites. The Charger and any acquired Ether remain. Movement and placement in the preceding route are not restored. | Confirmed | Corroborated | High | P2, P4, R3, R5 |

## Basic data

- Release / origin: Housemarque and Sony Interactive Entertainment. Native PS5
  base game released April 30, 2021.
- Platform or physical form: PlayStation 5 with DualSense. No assumption about
  PC, newer campaign controls or regional parity beyond the English sources.
- Puzzle family: live tactical response, real-time progression and iterative
  route reset with retained state.
- Primary sources:
  - **P1** [PlayStation's Returnal product page](https://www.playstation.com/en-us/games/returnal/).
  - **P2** [Housemarque game director on combat and progress](https://blog.playstation.com/2021/01/13/returnal-combat-details-upgradable-weapons-otherworldly-tools-and-risky-buffs),
    covering adaptive trigger states, one weapon, traits, danger and reset.
    Its early launch date was superseded by the release listing and P3.
  - **P3** [Housemarque's launch-period survival guide](https://blog.playstation.com/2021/04/28/returnal-survival-guide-housemarques-gameplay-tips-for-atropos/),
    covering launch date, live evasion, gear and Adrenaline.
  - **P4** [PlayStation's written hands-on preview](https://blog.playstation.com/2021/04/01/returnal-hands-on-preview/),
    on the cycle, primary recharge, Alt-Fire, room variation and the HUD.
  - **P5** [Housemarque's dated update 2.0 announcement](https://blog.playstation.com/2021/10/26/returnal-2-0-update-brings-suspend-cycle-and-photo-mode),
    which dates the arrival of Suspend Cycle after the scoped period.
  - **P6** [Housemarque's Ascension launch announcement](https://blog.playstation.com/2022/03/22/returnal-ascension-launches-today-brings-campaign-co-op-and-endless-challenge-mode/).
- Secondary sources:
  - **R1** [GameFAQs PS5 Biome 1 walkthrough](https://gamefaqs.gamespot.com/ps5/292804-returnal/faqs/79310/biome-1)
    and [the author's mechanics appendix](https://gamefaqs.gamespot.com/ps5/292804-returnal/faqs/79310/the-basics-of-returnal),
    on both Titanops outcomes, tutorial gate, rooms, supplies and map.
  - **R2** [VULKK's May 2021 permanent equipment guide](https://vulkk.com/2021/05/04/returnal-equipment-full-list-and-usage-guide/).
  - **R3** [PowerPyx, April 2021 retention inventory](https://www.powerpyx.com/returnal-permanent-unlocks-explained/).
  - **R4** [Push Square's PS5 mechanics reference](https://www.pushsquare.com/guides/returnal-guide-tips-tricks-and-all-you-need-to-know),
    including Overload, Adrenaline, weapon proficiency and Integrity pickups.
  - **R5** [Gamepressure's launch-period Alt-Fire guide](https://www.gamepressure.com/returnal/alt-fire-how-to-unlock/z2e616)
    and [Twinfinite's launch-day control description](https://twinfinite.net/guides/returnal-weapon-alt-fire-modes-how-use/).
- Claim IDs: `RET-001` to `RET-010`.

## Mechanical decomposition

### Action Genes

- `ACT-008`: route Selene directly across the ruins.
- `ACT-161`: aim the equipped weapon and discharge at a hostile or eligible
  switch or obstruction. Room movement continues.
- `ACT-199`: accept an offered weapon as replacement for the current one.
- `ACT-341`: interact with the reachable authored charger to install it.
- `ACT-719`: choose which firing mode is readied through L2 travel. R2
  commits the current mode when it is available.
- Claim IDs: `RET-002`, `RET-003`, `RET-005`, `RET-006`.

### System Behaviour Genes

- `SYS-037`: contact acquires eligible local drops, including ordinary
  Obolites if available.
- `SYS-215`: resolve player movement and shots against live hostile actions.
- `SYS-456`: an eligible dash clears most projectile overlaps, within the
  dash's protected portion. Protection is not universal.
- `SYS-464`: a new cycle assembles available authored rooms and placements
  around route requirements. Exact seeds and layout weights are unavailable.
- `SYS-469`: true death starts a new cycle and resets temporary state. Equipment
  milestones, earned traits and Ether follow their separate retained rules.
- `SYS-578`: hits and compatible recovery change one current Integrity pool.
- `SYS-1493`: an empty primary weapon recharges. Precisely timed R2 during
  the indicated Overload window can end the recharge early. No numeric bonus
  or error-lockout duration is asserted.
- `SYS-1494`: after an eligible alternate shot, a separate cooldown must
  recover. Primary readiness and alternate readiness can differ.
- `SYS-1495`: a no-damage kill streak earns Adrenaline tiers. A damaging hit
  resets the current unprotected streak and its buffs.
- `SYS-1496`: within-cycle proficiency governs potential weapon drops, while
  earned weapon-trait unlocks follow eligible future weapon instances through
  a separate persistent ledger.
- `SYS-1497`: eligible Silphium supplies missing Integrity. At full Integrity
  it can credit Resin instead, and completing the Resin requirement raises the
  current cycle's maximum. Authored Resin pickups can also exist separately.
- `SYS-1498`: acquire the charger once as lasting equipment authority for
  a new weapon function. Its presence is independent of the current gun.
- Resolution order: resolve live shot, dash and hostile interactions, settle
  their readiness and drops, then process route and acquisition decisions.
  At true death, clear the temporary state and rebuild around retained flags.
- Claim IDs: `RET-003` to `RET-010`.

### Constraint Genes

- `CON-349`: the teaching route gate requires the acquired shooting
  capability demonstrated against its obstruction.
- `CON-801`: only one firearm instance is retained for use in the current
  loadout. Replacing it does not grant a hidden second carried gun.
- Scarce resources: current Integrity, the firing windows, nearby pickups
  and the one weapon slot. Ether and Obolites have different lifetimes.
- Claim IDs: `RET-003` to `RET-007`, `RET-010`.

### Information Genes

- `INF-119`: current Integrity, proficiency, Adrenaline and alternate
  readiness guide combat and pickup timing. The recharge reticle presents
  an opportunity, not a guarantee of accepted Overload input.
- `INF-180`: discovered rooms and connections stay available on the map in
  the cycle. Visible door classes distinguish main from side routes.
- Claim IDs: `RET-004`, `RET-005`, `RET-007`, `RET-009`.

### Objective Genes

- `OBJ-026`: the first charger demonstration opens a route and the player
  passes the newly reachable edge. Observing the later death defines the
  research endpoint and is not presented as winning the game.
- Claim IDs: `RET-006`, `RET-010`.

### Time Genes

- `TIM-003`: player inputs continue while projectiles, hostile attacks and
  weapon recharge advance.
- Claim IDs: `RET-003` to `RET-005`.

## Reproducible transitions

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| New save, training door and starter gun | Shoot the switch and proceed; follow the ordinary loss branch at the first Titanops | The switch grants passage and the lethal encounter returns control near Helios | Initial death is one tutorial outcome rather than a mandatory scripted result | `RET-002` |
| Primary ready and incoming eligible projectile overlap | Move, shoot and time a dash | The shot resolves while the world runs and protected dash can avoid the overlap | Dodging and damage are live interactions | `RET-003` |
| Primary shots exhausted | Wait, or press R2 in the displayed Overload window | Normal recharge completes on its own; a properly timed press restores readiness sooner | Output speed depends on a timing opportunity without an ammo purchase | `RET-004` |
| Charger installed and Alt-Fire ready | Prepare it with full L2 and use R2 on the obstructed teaching door | The growth clears and the new passage can be crossed | The lasting unlock supplies a gate-relevant combat verb | `RET-005`, `RET-006` |
| Primary ready but the alternate function recently discharged | Try primary during the alternate cooldown | Primary can still operate if ready; the alternate mode must recharge separately | There are two readiness states, not two held guns | `RET-005` |
| A no-hit streak or an eligible green pickup | Earn another kill without damage, take damage, or collect the pickup at the current Integrity | Completed kill groups raise tiers and damage removes the unprotected streak. Missing health heals, while full health can yield Resin credit | Per-encounter timing has run-level state consequences | `RET-007` |
| Charger and a temporary weapon or run pickup owned, no revival enabled | Take lethal damage and inspect the next controllable cycle | Helios is the start anchor. The temporary gun and spendable Obolites are gone, proficiency is reset, and the Charger remains | Losing one gun is distinct from losing the authority for its alternate function | `RET-010` |

## Strategic and experiential structure

- Local decision: choose a safe movement line and whether to accept normal
  recharge or time an early Overload while the room is active.
- Medium-term planning: choose when to change the sole gun and use an alternate
  shot for a door or target. Inspect side routes only if their supplies repay
  their exposure. Preserve a no-hit streak where useful.
- Long-term structure: the Charger increases capabilities even when a lost
  cycle resets the build. Earned traits differ from the current gun and stats.
- Failure attribution: distinguish avoidable damage or missed timing within
  a room from the deliberate research death after the unlock. No failing room
  location is guaranteed to be the same in the next cycle.
- Player-trust factors: the reticle exposes the timing attempt, the map
  exposes visited exits and the gear screen separates permanent equipment.
- Claim IDs: `RET-003` to `RET-010`.

## Replay and variation

- What changes: room sequence, encounter and supply positions, weapons and
  their assigned alternate shots. The required progression landmarks persist.
- Randomness or procedural generation: the room atlas mixes authored spaces.
  No seed distribution, layout formula or guaranteed early loot is assumed.
- Multiple viable strategies: buy time through movement and normal refill or
  use Overload; rely on a preferred gun if it drops or adapt to the offered one.
- Typical replay motive: reach the milestone with stronger retained knowledge
  and a more effective temporary kit.
- Claim IDs: `RET-003` to `RET-010`.

## Adjacent systems and history

- Direct predecessors: the record does not infer direct design lineage.
- Variants: paid revival preserves the current cycle by another rule. It is
  explicitly excluded from the terminal reset in this unit.
- Similar games: Ori and the Blind Forest shares authored traversal gates and
  live combat while using another recovery and unlock structure.
- Important differences: installed equipment changes future cycles alongside
  temporary data removal and room recomposition.
- Claim IDs: `RET-003`, `RET-006`, `RET-009`, `RET-010`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-161`, `ACT-199`, `ACT-341`, `ACT-719` | route, shot, swap, fixture and input depth |
| System Behaviour | `SYS-037`, `SYS-215`, `SYS-456`, `SYS-464`, `SYS-469`, `SYS-578`, `SYS-1493`, `SYS-1494`, `SYS-1495`, `SYS-1496`, `SYS-1497`, `SYS-1498` | combat, authored-room composition, resource lifetimes and charger |
| Constraint | `CON-349`, `CON-801` | gated edge and one weapon instance |
| Information | `INF-119`, `INF-180` | combat readouts and explored route |
| Objective | `OBJ-026` | reach the gated route beyond the growth |
| Time | `TIM-003` | live world and firing readiness |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `521` (`GAME-0001`–`GAME-0521`).
- Exact genome matches: none.
- Tied near matches: `GAME-0431` — Ori and the Blind Forest (`9 / 34 = 0.264706`).
- Supported combination subsets: none.
- Scan date: 2026-11-17.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0431` — Ori and the Blind Forest | `ACT-008`, `ACT-161`, `ACT-341`, `CON-349`, `INF-119`, `OBJ-026`, `SYS-215`, `SYS-578`, `TIM-003` share direct live traversal and combat, eligible interactions, health, local readout and capability-gated progress. | Ori's opening uses its authored route, Spirit Flame, charge-paid Soul Link, Energy, and its own return rules. Returnal instead presents a swappable gun, timed recharge, a lasting Alt-Fire switch and a true-death reset that clears its temporary kit and rebuilds the route. | Near, `0.264706` |

## Taxonomy impact

- Registry changes: `ACT-719`, `SYS-1493` through `SYS-1498` and `CON-801`.
- Taxonomy-change record: [TAXONOMY_CHANGE_269](../../../research/taxonomy-changes/TAXONOMY_CHANGE_269.md).
- Candidate terms affected: none.

## Negative results

- No verified combination is a proper subset. Exact generation seeds, specific
  Alt-Fire assignment and sensor thresholds remain unverified. A lethal hit
  under an enabled local revival is excluded and not treated as this reset.

## Delta summary

The packet adds an opening reset case with an acquired ranged capability.

## New facts

- [Observation | Corroborated | High] A retained module grants access to
  Alt-Fire on eligible guns after the current gun and combat resources reset.

## New genes

- [Observation | Corroborated | High] Eight admissions distinguish input
  depth, recharge, damage-free streaks, resource branching and equipment
  lifetimes as documented in the taxonomy change.

## New combinations

- [Observation | Corroborated | High] No new combinations.

## Taxonomy changes

- [Observation | Corroborated | High] `TAXONOMY_CHANGE_269` adds eight
  definitions and records fifteen unchanged transfers.

## New questions

- Which state does the alternate tutorial victory path preserve relative to
  the selected loss branch on a verified native launch build?

## Next recommended game

- [Hypothesis | Limited | Medium] The approved nine-game horizon ends here.
- Optimisation criterion: review the batch evidence and novelty metrics before
  selecting a new platform-balanced horizon.
- Expected information gain: distinguish repeated boundaries from sufficiently
  evidenced additions as the catalogue expands.
- Backlog impact: no successor is selected in this unit.

## Why this game

- [Hypothesis | Limited | Medium] Saving the authority to use an alternate shot
  despite losing its original gun is a clear test of persistence boundaries.
