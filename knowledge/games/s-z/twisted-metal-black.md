---
game_id: GAME-0409
slug: twisted-metal-black
game_title: 'Twisted Metal: Black'
analysis_status: reviewed
reviewed: 2026-09-26
combination_ids: []
gene_ids:
  action:
    - ACT-161
    - ACT-290
    - ACT-309
    - ACT-550
    - ACT-551
  system:
    - SYS-045
    - SYS-215
    - SYS-222
    - SYS-320
    - SYS-578
    - SYS-691
    - SYS-738
    - SYS-911
    - SYS-1092
    - SYS-1093
  constraint:
    - CON-269
    - CON-578
  information:
    - INF-405
  objective:
    - OBJ-166
  time:
    - TIM-003
---

# Game: Twisted Metal: Black

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Junkyard Dog,
missile types and exact reserve values are parameters, not separate genes.

## Analysis scope

- Version / ruleset: original North American English 2001 PlayStation 2
  *Twisted Metal: Black*, one-player Story Mode on its first Junkyard arena,
  using Junkyard Dog at the default difficulty. Sony's original PS2 manual
  supplies the combat rules; a contemporary written PS2 guide supplies the
  first-arena route. The 2015 PS4 reissue is not the analysed executable.
- Structured analysis target: `PLAT-PLAYSTATION-2` in
  [`knowledge/platforms/games.json`](../../platforms/games.json).
- Primary decision loop: steer, throttle and boost a dedicated combat
  vehicle around the open arena; read nearby threats and radar; collect a
  compatible weapon or health pickup; cycle to a finite-ammo weapon and
  choose when to fire, use the heat-limited machine gun, the two-press
  spiked-ball Special or an energy-priced defensive attack; survive hostile
  vehicles and remove the finite roster to unlock the next Story selection.
- Entry: choose one-player Story Mode and Junkyard Dog, enter the initial
  Junkyard arena, and record displayed lives, health, opponent count, weapon
  ammunition, turbo and energy at first control. Do not assume an exact
  roster size, life stock or pickup position from an unplayed disc revision.
- Positive terminal: the arena reports no remaining opponents and offers
  the next Story stage selection/save boundary. Choosing or playing the next
  stage is outside this packet.
- Failure and recovery control: separately deplete vehicle health under
  hostile attack; one life is consumed and the arena can be retried while
  stock remains. Exhausting the stock ends this bounded attempt. Reset this
  branch before the positive route; exact respawn coordinates and retained
  pickups are not asserted.
- Included: dedicated vehicle movement and collision, turbo, autonomous
  hostile vehicles, contact weapon pickups, finite missile reserve and
  weapon cycling, heat-limited machine gun, Junkyard Dog's launchable
  spiked-ball Special with a second command, rechargeable energy used by
  shield/freeze or another manual-listed energy attack, damage and health
  pickups, a limited-use repair station, finite lives, radar/HUD and
  finite-opponent arena elimination.
- Excluded: the Junkyard's optional plane, crusher or other secrets as
  required steps; exact weapon damage, AI routes, pickup positions and
  frame timings; later Story arenas, bosses, cutscenes and endings;
  Challenge, Endurance, cooperative or versus modes; hidden vehicle unlocks,
  audiovisual claims, glitches and the PS4 wrapper.
- Potential scoped modules: a fixed later Story arena with its own hazard;
  the optional crusher/plane interactions; multiplayer item contention.
- Reproducible parameterisation: log PS2 disc revision, selected mode/car,
  difficulty, arena label, initial HUD state, every pickup, weapon selection,
  shot and ammo decrement, machine-gun heat cycle, Special launch/second
  press, energy-attack cost/recharge, repair use, each opponent defeat,
  health/life failure branch and the next-stage availability flag. Reopen
  stage-local claims if a tested revision differs from the written guide.
- Direct-play status: none. No disc, emulator, controller trace, gameplay
  video, audio or screenshot was inspected. This is a bounded reconstruction
  from Sony's original manual and one written PS2 route, not a claimed
  playthrough or byte-exact build audit.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `TMB-001` | Story Mode is separate from Challenge and Endurance; its initial Junkyard arena leads to a next-stage choice after clear. | Observation | Corroborated | Medium | P1, S1 |
| `TMB-002` | A dedicated vehicle is steered, accelerated, braked and boosted during live combat. | Confirmed | Direct | High | P1 |
| `TMB-003` | Contact pickups add compatible weapons; the player cycles an active weapon and spends its finite ammunition when fired. | Confirmed | Direct | High | P1 |
| `TMB-004` | The machine gun has unlimited ammunition but overheats and must cool before sustained fire resumes. | Confirmed | Direct | High | P1 |
| `TMB-005` | Junkyard Dog's Special launches one spiked ball; another fire command brings it down on the aiming reticle. | Confirmed | Direct | High | P1 |
| `TMB-006` | Shield, freeze and other energy attacks spend an automatically recharging shared energy meter. | Confirmed | Direct | High | P1 |
| `TMB-007` | Hostile damage lowers health; health pickups and the limited repair station can restore it, while lethal loss consumes finite lives. | Confirmed | Direct | High | P1 |
| `TMB-008` | The display includes opponent count, radar position, health/lives, active weapon/ammo, machine-gun heat, turbo and energy. | Confirmed | Direct | High | P1 |
| `TMB-009` | This first-arena packet links vehicle manoeuvre, resource-priced fire and survival to elimination of a finite hostile roster. | Strong Pattern | Corroborated | Medium | `TMB-001`–`TMB-008` |

## Basic data

- Release / origin: Incognito Entertainment and Sony Computer Entertainment,
  original PlayStation 2 release, 2001.
- Platform or physical form: North American PS2 disc, one-player Story Mode;
  no claim of exact disc revision or the later reissue's equivalence.
- Mechanical family: real-time system pressure.
- Primary rules source, accessed 2026-09-26:
  - **P1:** [Sony's original *Twisted Metal: Black* PS2 instruction manual,
    OCR-hosted scan](https://www.passeidireto.com/arquivo/120692120/twisted-metal-black-manual-ps-2),
    dated 15 May 2001 in its original layout. Controls, HUD, modes,
    pickups, heat, energy attacks, repair and Junkyard Dog's Special were
    read from the original manual text. The hosting site is not Sony.
- Official edition context, accessed 2026-09-26:
  - **P2:** [PlayStation's *Twisted Metal: Black* product
    page](https://www.playstation.com/en-us/games/twisted-metal-black/)
    identifies the PS2 original and later PS4 availability; the latter is
    not evidence for this PS2 arena's frame behaviour.
- Independent route source, accessed 2026-09-26:
  - **S1:** [Original PS2 Story walkthrough at
    GameFAQs](https://gamefaqs.gamespot.com/ps2/378092-twisted-metal-black/faqs/12610),
    2002. It places Junkyard first and describes next-stage selection and
    saving. Arena-local counts and positions are not elevated to direct-play
    observations.
- Reproducible control: source-side transition trace under the stated entry
  and terminals; no direct gameplay evidence.
- Claim IDs: `TMB-001`–`TMB-009`.

## Mechanical decomposition

### Action Genes

- Reused `ACT-290`: directly steer and accelerate the fixed combat vehicle;
  no in-arena enter/exit or fleet-selection system is claimed.
- Reused `ACT-309`: spend a finite turbo reserve for directed acceleration.
- Reused `ACT-161`: aim and fire at a reachable hostile with the selected
  weapon; weapon-specific damage values are parameters.
- New `ACT-550`: cycle the carried vehicle weapons to make one currently
  available type active before firing.
- New `ACT-551`: after launching the Junkyard Dog spiked ball, deliberately
  time a second fire command to bring that same projectile down.
- Claim IDs: `TMB-002`, `TMB-003`, `TMB-005`.

### System Behaviour Genes

- Reused `SYS-045` and `SYS-215`: hostile vehicles move and resolve
  directly commanded real-time attacks while the player manoeuvres.
- Reused `SYS-222`: contact with a compatible arena pickup transfers it to
  the controlled vehicle's carried reserve; this avatar is a vehicle body.
- Reused `SYS-320`: occupied vehicle motion and collision damage are live.
- Reused `SYS-578` and `SYS-911`: health loss can become one finite-life loss;
  health restoration and life replacement are distinct transitions.
- Reused `SYS-691`: turbo reserve converts to acceleration.
- Reused `SYS-738`: sustained machine-gun fire accumulates heat and requires
  cooling; the manual does not imply an active-cooling timing minigame.
- New `SYS-1092`: an arena repair station has a limited repair supply, so a
  damaged vehicle can receive repair but cannot farm infinite health there.
- New `SYS-1093`: a shared vehicle energy meter replenishes automatically
  while shield, freeze and related energy attacks debit it.
- Resolution order: steer/advance vehicles → contact pickup or hostile hit
  → choose weapon/attack → ammo, heat or energy cost → damage/repair →
  life check → opponent-count and Story-clear check.
- Claim IDs: `TMB-002`–`TMB-007`.

### Constraint Genes

- Reused `CON-578`: a selected finite-ammo missile cannot fire without its
  compatible reserve; the unlimited machine gun is deliberately excluded.
- Reused `CON-269`: an energy attack or Special requires its relevant
  resource, readiness and target form; no invented cooldown is asserted.
- Claim IDs: `TMB-003`, `TMB-005`, `TMB-006`.

### Information Genes

- New `INF-405`: the vehicle-combat HUD and radar expose opponent positions
  and count alongside the player's current health, lives, active weapon,
  ammunition, heat, energy and turbo. Radar does not reveal exact unseen
  vehicle intentions.
- Claim ID: `TMB-008`.

### Objective and Time Genes

- Reused `OBJ-166`: eliminate the declared finite hostile roster and retain
  the next Story stage as selectable. This does not clear the campaign.
- Reused `TIM-003`: enemy motion, incoming attacks and vehicle control
  continue in real time while weapon and resource decisions are made.
- Claim IDs: `TMB-001`, `TMB-009`.

## Reproducible transitions

| Before | Action | Bounded resolution | Establishes | Claim |
|---|---|---|---|---|
| Junkyard first control with fixed car | Steer, throttle, brake and turn | Car position and exposure change while hostiles continue to move | Direct vehicle-combat loop | `TMB-002` |
| Turbo reserve positive | Hold turbo briefly | Reserve falls and directed acceleration rises | Boost is a spendable reserve | `TMB-002` |
| Compatible missile pickup ahead | Drive through it, cycle weapon | Pickup joins carried reserve and selected weapon changes | Contact collection and active selection | `TMB-003` |
| Selected missile has ammunition | Fire at reachable opponent | One compatible shot is spent and may damage the target | Ammo gate and direct combat | `TMB-003` |
| Machine gun cool | Fire continuously, then pause | Heat reaches interruption threshold; pausing permits cooling | Heat is not finite ammo | `TMB-004` |
| Junkyard Dog Special ready | Fire, then fire again before impact | One spiked ball launches; second command brings that same ball down | Two-stage projectile control | `TMB-005` |
| Energy meter permits shield | Invoke shield during threat | Shared energy is debited and later replenishes automatically | Defence competes with other energy attacks | `TMB-006` |
| Vehicle damaged, repair supply available | Enter repair station | Health is restored within station's limited supply | Bounded arena repair | `TMB-007` |
| Health reaches zero | Observe life stock | One life is lost; retry only while stock remains | Negative branch separate from arena clear | `TMB-007` |
| One hostile remains | Defeat it | Opponent count becomes zero; next Story stage is offered | Finite-arena terminal | `TMB-001`, `TMB-009` |

## Strategic and experiential structure

- Local decision: chase a moving target, evade to a pickup, or conserve
  current health. Missile ammo, machine-gun heat and energy attacks impose
  different limits on fire.
- Medium-term planning: preserve turbo for a turn or escape; time the
  airborne Special's second press and do not consume limited repair early.
- Long-term structure: this packet ends at the first Story arena's next-stage
  selection, not a vehicle unlock or campaign ending.
- Failure attribution: vehicle health zero costs one life; failing to hit
  with a projectile is not itself terminal. Empty ammo, machine-gun
  overheating and depleted energy are distinct rejected actions.
- Player trust: radar and HUD disclose current resource and opponent state,
  but the player's route through a moving arena remains a live choice.
- Claim IDs: `TMB-001`–`TMB-009`.

## Replay and variation

- Opponents move rather than waiting in a fixed sequence; route and pickup
  choices can differ without changing the arena-clear predicate.
- The manual's different weapon pickups provide alternatives, but this
  packet requires only one compatible finite-ammo example, machine gun,
  one Special and an energy attack. Exact drop placement was not measured.

## Adjacent systems and history

- Racing-game `ACT-290`/`SYS-320` cover direct vehicle control and damage,
  but not cycling arena pickups or eliminating a hostile roster.
- `SYS-738` covers machine-gun heat; `CON-578` covers missiles, not that
  unlimited gun. `SYS-798` is exertion stamina, not a vehicle's shared
  automatically recharging energy-attack meter.
- `ACT-164` selects a general carried item slot but does not express the
  in-vehicle weapon cycle; `ACT-199` is a deliberate inventory transfer,
  not contact collection. No earlier signature changes to force reuse.

## Normalised genome

The front matter is canonical: twenty Active genes. Fifteen reuse prior
vehicle, combat, pickup, health, resource, mission-clear and real-time
boundaries; five isolate weapon cycling, second-press projectile control,
limited repair, shared regenerating energy and radar/HUD state.

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `408` (`GAME-0001`–`GAME-0408`).
- Exact genome matches: none.
- Tied near matches: `GAME-0381` — GoldenEye 007 (`6 / 29 = 0.206897`).
- Supported combination subsets: none.
- Scan date: 2026-09-26.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0381` — GoldenEye 007 | `ACT-161`, `SYS-215`, `SYS-222`, `SYS-578`, `CON-578`, `TIM-003` | Both fire at live hostiles, collect compatible ammunition and risk one health pool. GoldenEye traverses an on-foot Dam route, disables four alarms and departs by a fixed platform; Twisted Metal steers a dedicated car around a single arena, manages heat/turbo/shared energy and clears a finite vehicle roster without an exit door. | Near, `6 / 29 = 0.206897` |

## Taxonomy impact

`TAXONOMY_CHANGE_147` adds five Active genes without changing an earlier
signature or verified combination.

## Negative results

- No original PS2 disc execution verifies exact Junkyard opponent count,
  placements, damage, AI route, life stock or retry coordinate.
- Sony's modern product page documents edition history but is not treated
  as proof of PS2 encounter timing; a mistaken unrelated manual result was
  discarded during source screening.
- Junkyard Dog and the spiked-ball geometry are parameters, not a named-car
  gene; no optional arena secret becomes a mandatory objective.

## Delta summary

A combat vehicle must steer through a live arena, collect and select weapons,
manage separate ammunition, heat, turbo and energy limits, survive finite
health/lives and eliminate the roster before Story Mode advances.

## New facts

- [Confirmed | Direct | High] Sony's original PS2 manual distinguishes
  finite-ammo pickups, unlimited-but-heating machine gun, automatically
  recharging energy attacks and Junkyard Dog's two-stage Special
  (`TMB-003`–`TMB-006`).

## New genes

- [Observation | Direct | High] `ACT-550`, `ACT-551`, `SYS-1092`,
  `SYS-1093` and `INF-405` isolate five different transitions. Existing
  `OBJ-166` already covers the finite-hostile-set campaign handoff.

## New combinations

- [Observation | Direct | High] No new verified combination.

## Taxonomy changes

- [Observation | Direct | High] `TAXONOMY_CHANGE_147` admits five Active
  boundaries; older signatures remain unchanged.

## New questions

- Does a tested original PS2 disc revision present the exact first-arena
  roster and checkpoint as the written route describes?
- Which pickups, repair supply and resource amounts persist across a
  nonterminal life loss in that revision?

## Next recommended game

- [Hypothesis | Limited | Medium] `GAME-0410` *Halo Wars*.
- Optimisation criterion: switch from direct single-vehicle real-time
  combat to controller-scale RTS base production on Xbox 360.
- Expected information gain: test whether production, squad assignment and
  a bounded mission objective fit existing strategy boundaries.
- Backlog impact: no selected subject displaced.

## Why this game

- [Hypothesis | Corroborated | Medium] The first Junkyard arena couples
  vehicle steering with three different firing budgets and a finite
  elimination target. It tests transfer beyond racing or on-foot combat.

## Next test

Use an identified lawful original PS2 disc and a fresh Story file to log
first-control HUD, opponent roster, pickup and Special transitions, repair
depletion, life-loss retry and the exact next-stage/save offer. Revise only
claims contradicted by that trace.
