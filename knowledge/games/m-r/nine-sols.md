---
game_id: GAME-0527
slug: nine-sols
game_title: Nine Sols
analysis_status: reviewed
reviewed: 2026-11-17
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-161
    - ACT-190
    - ACT-223
    - ACT-341
  system:
    - SYS-215
    - SYS-369
    - SYS-578
    - SYS-1512
    - SYS-1513
    - SYS-1514
  constraint:
    - CON-617
    - CON-809
  information:
    - INF-119
    - INF-310
    - INF-512
  objective:
    - OBJ-080
  time:
    - TIM-003
---

# Game: Nine Sols

Use the canonical [vocabulary and genome rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
Button binding, cue colour, charge count and enemy names parameterise the rules.

## Analysis scope

- Version / ruleset: English North American base Nintendo Switch eShop
  release of 26 November 2024, Standard Mode, ordinary first story attempt
  at Red Tiger Elite: Baichang in Apeman Facility (Elevator).
- Structured analysis target: PLAT-NINTENDO-SWITCH, original Switch
  eShop base game, launch-era rule evidence. The exact installed package
  and numeric update version are unverified.
- Primary decision loop: read Baichang's swings, face him and parry eligible
  strikes to build Qi. Dodge the crimson leap, then choose immediate slashes,
  a safe healing window or the longer commitment of attaching and detonating
  the base Qi Blast talisman. Use the opening after a completed enemy attack.
- Entry: on the direct first route, before using the green replenishment
  fixture next to the arena. The prior Root Node is activated and Yi has
  the default skills, ordinary Medicine Pipe and no equipped Jades. Do
  not buy upgrades, grind extra skill points or switch spell style.
- Exit: defeat Baichang, pick up the dropped Stasis Jade and take the
  elevator to New Kunlun Central Hall. Stop on first arrival. If Yi dies,
  recover at the activated Root Node and retry the same encounter.
- Included: side-on movement, direct sword attacks, timed parry, grounded
  Immortal Dash, Qi, recoverable and direct damage, held base talisman,
  the fixture and finite pipe heals, local failure and retry, reward
  pickup and lift access.
- Excluded: the prior prologue and earlier combat rooms, progression beyond
  Central Hall arrival, the skill tree, death-drop economics, equipping
  Stasis Jade, Tai-Chi Kick, aerial dash, Unbounded Counter, Azure Bow,
  alternate spell styles, Story Mode, rematches and cross-platform timing
  parity. Local hitbox, damage and recovery timings are unmeasured.
- Direct-play status: no console, executable, video or audio was run.
  Nintendo and Red Candle establish the shipped edition and combat design.
  Two release-day Switch play accounts establish the qualitative combat
  loop. Written routes and transcribed help text supply encounter details.
  Numeric Switch frame and damage values are outside the evidence.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
| --- | --- | --- | --- | --- | --- |
| NS-001 | The base game launched on Nintendo Switch on 26 November 2024. The product and same-day Switch play accounts support this target, without naming an executable hash. | Confirmed | Direct | High | P1, P2, S1, S2 |
| NS-002 | Yi can slash directly and dodge along the ground. Baichang has parryable chained swings and a crimson jumping slam that bypasses the basic parry. The ordinary route grants Tai-Chi Kick later. | Observation | Corroborated | High | P2, S3, S4, S5 |
| NS-003 | Facing and timing matter. An eligible precise parry prevents the hit's damage. An early but valid parry feeds recoverable damage into Yi's bar. Both valid grades add Qi while there is room. | Observation | Corroborated | High | S2, S4, S5, S6 |
| NS-004 | The base talisman dashes through a reachable target, applies a mark and starts a separate vulnerable hold. Sufficient hold detonates the mark, adding permanent damage and converting the enemy's accumulated internal damage. An interrupted hold can leave the conversion unrealised. | Observation | Corroborated | High | P2, S1, S2, S3, S6 |
| NS-005 | At least one available Qi charge is needed for base talisman use. The base detonation uses available charges up to its three-charge limit. No native drain formula or missed-dash accounting is asserted. | Observation | Corroborated | Medium | S4, S6 |
| NS-006 | Internal damage remains visible on the health bar and can recover with time. A completed talisman explosion can settle the enemy overlay as direct damage. The exact native recovery rules and rates are unmeasured. | Observation | Corroborated | Medium | S2, S6 |
| NS-007 | A nearby green fixture restores health and replenishes the pipe in the written route. The finite Medicine Pipe provides live healing. Death returns the attempt to an activated Root Node. | Observation | Corroborated | High | S2, S4, S5 |
| NS-008 | The direct first clear drops Stasis Jade and lets Yi take the lift to New Kunlun Central Hall. The local clear needs no Jade, alternate spell style or later technique. | Observation | Corroborated | High | S3, S4, S5 |
| NS-009 | The incoming swing animation and flash distinguish an eligible strike from the crimson leap. Health, internal damage, Qi and pipe stock make different parts of the next response inspectable. | Observation | Corroborated | Medium | S1, S2, S4, S6 |

## Basic data

- Release / origin: Red Candle Games, Nintendo Switch, 26 November 2024,
  single-player base eShop release.
- Mechanical family: real-time system pressure. Waiting can let a current
  strike land or a marked target recover, while a successful parry opens
  resource and timing opportunities.
- Sources accessed 2026-11-17:
  - **P1** — [Nintendo US product page](https://www.nintendo.com/us/store/products/nine-sols-switch/), release, platform and publisher.
  - **P2** — [Red Candle Games press kit](https://redcandlegames.com/presskit/sheet.php?p=nine+sols), developer description of slashing, deflection, dash and talisman detonation.
  - **S1** — [Nintendo Life's North American Switch review](https://www.nintendolife.com/reviews/switch-eshop/nine-sols), Echo Apsey, 26 November 2024, native Switch base Qi Blast sequence and vulnerability.
  - **S2** — [Nintendo World Report's Switch review](https://nintendoworldreport.com/review/69286/nine-sols-switch-review), Alex Orona, 26 November 2024, deflection supplies, imperfect defence, recovery, pipe and retries.
  - **S3** — [Into Indie Games' written opening route](https://intoindiegames.com/walkthroughs/nine-sols-walkthrough/), elevator section, Baichang and talisman punish. Used for qualitative encounter details, without inferring native Switch timings.
  - **S4** — [Written Standard-mode route](https://steamcommunity.com/sharedfiles/filedetails/?id=3457329455), Apeman Facility, first elevator, Stasis Jade and later Tai-Chi Kick. Cross-platform route corroboration, not a Switch execution record.
  - **S5** — [Neoseeker's written Apeman Facility play route](https://www.neoseeker.com/nine-sols/Apeman_Facility), first checkpoint and healing fixture, swing chains, crimson jump and successful elevator continuation. No embedded video used.
  - **S6** — [Community combat and transcribed help](https://ninesols.wiki.gg/wiki/Internal_Damage) and [base skill list](https://ninesols.wiki.gg/wiki/Skill), distinction between grades, visible provisional damage and hold resource limits. Detailed but secondary; exact numerical combat timings are unverified.

## Mechanical decomposition

### Action Genes

- Reuse `ACT-008`: run, jump and reposition along the side-on arena.
- Reuse `ACT-161`: swing the current blade at the reachable guardian.
- Reuse `ACT-190`: commit a held talisman or a finite pipe heal in its
  own safe interval.
- Reuse `ACT-223`: choose the timed parry for eligible swings and dodge
  for the crimson leap.
- Reuse `ACT-341`: interact with the replenishment fixture, claim the
  named drop and select the lift's available destination.
- Claim IDs: NS-002–NS-005, NS-007, NS-008.

### System Behaviour Genes

- Reuse `SYS-215`: resolve current geometry, connected blows, attack
  recovery and interruptions while both actors continue in real time.
- Reuse `SYS-369`: a lethal failure returns to an activated Root Node.
- Reuse `SYS-578`: lasting hits reduce the one real health pool; the pipe
  and fixture replenish it. The provisional overlay has its own rule.
- New `SYS-1512`: split valid parries by precision while both feed Qi.
  A precise response protects health; a valid early response substitutes
  internal damage, independently of the charge grant.
- New `SYS-1513`: dash into a reachable enemy and mark it, then hold
  through the vulnerable charge. Successful detonation converts the
  marked target's pending internal damage and adds an explosion hit.
- New `SYS-1514`: maintain recoverable internal damage on the health
  surface separately from permanent loss. Recovery can clear it if the
  affected actor avoids the relevant pressure; conversion can settle
  enemy damage before it fades.
- Resolution order: cue and approach → eligible response → deflection
  grade and Qi or direct hit → talisman charge and settlement, ordinary
  slashes or heal → defeat or successful drop and lift. Exact simultaneous
  event orders were not measured.
- Claim IDs: NS-002–NS-009.

### Constraint Genes

- Reuse `CON-617`: crimson leap is outside the basic parry's target class.
- New `CON-809`: basic talisman use requires a positive Qi stock. The
  completed base blast uses the available charges up to its style cap.
- Claim IDs: NS-002, NS-005.

### Information Genes

- Reuse `INF-119`: inspect current real health, Qi and finite healing supply.
- Reuse `INF-310`: a prepared swing's visible cue supports a timed response.
- New `INF-512`: distinguish current recoverable internal damage from
  settled losses on the same health state, including the enemy overlay.
- Claim IDs: NS-006, NS-009.

### Objective Genes

- Reuse `OBJ-080`: defeat the guard, collect the named drop and cross the
  opened progression threshold by taking the lift into Central Hall.
- Claim ID: NS-008.

### Time Genes

- Reuse `TIM-003`: attacks, opening windows and charge progress continue
  in live time while Yi moves or chooses a response.
- Claim IDs: NS-002–NS-007.

## Reproducible transitions

| Before | Action | Bounded resolution | What it establishes | Claim ID |
| --- | --- | --- | --- | --- |
| Yi is injured at the green fixture | Interact before entering the arena | Health and finite pipe uses refill on the corroborated route | Fixture preparation changes the retry margin | NS-007 |
| A normal swing is about to connect | Parry precisely while facing the threat | The hit is deflected without damage and Qi is gained within capacity | Dependent offensive resource is earned by defence | NS-003 |
| An eligible swing meets an early but valid parry | Let the parry resolve | The response earns Qi and shows recoverable internal damage instead of a clean defence | Grant and protection are different outcomes | NS-003, NS-006 |
| Baichang leaps with the crimson tell | Use the grounded dodge at the approach of the slam | Leave the threatened position without relying on the ordinary parry | Attack class changes the legal defence | NS-002 |
| Baichang is recovering and Qi is available | Dash through to attach and keep holding | A completed base blast uses stored Qi and converts internal damage into lasting damage | Attachment precedes detonation | NS-004–NS-006 |
| Talisman attached but the hold is interrupted | Take the hostile hit before completion | The full conversion does not settle | Marking is not a guaranteed explosion | NS-004 |
| Missing health, pipe use remains, enemy out of immediate reach | Use the pipe | Spend one finite heal and restore health during the live encounter | Healing uses a separate stock and safe window | NS-007 |
| Yi suffers lethal damage | Resume from the activated Root Node and return | Fight again against the surviving guardian | Local loss is a repeatable attempt | NS-007 |
| Baichang defeated | Collect the Stasis Jade and take the elevator | Arrive at New Kunlun Central Hall with the reward | Ends after crossing to the successor region | NS-008 |

## Strategic and experiential structure

A normal sword strike can use a short gap, while Qi Blast needs both a
successful approach and time to hold. Spending a recovery window on the
pipe preserves survival, at the cost of foregoing that opening's damage.
The early valid parry earns a charge but allows a recoverable wound; a
cleaner response protects the ordinary health margin.

## Replay and variation

- Compare a precise parry, an early valid parry and an attempted basic parry
  of the crimson move. They are distinct rule branches.
- Compare a single slash or heal during a short opening with a talisman
  held in a longer recovery. The chosen timing changes conversion risk.
- Claim IDs: NS-002–NS-007.

## Adjacent systems and history

- The developer cites Sekiro-style deflection as inspiration. This scoped
  first fight routes defensive success into a separate resource and a
  two-stage talisman strike.
- Possible later modules include Tai-Chi Kick on a different attack class,
  alternate spell settlements, Jade loadouts and corpse retrieval. None
  are prerequisites for this first clear.
- Claim IDs: NS-002–NS-008.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
| --- | --- | --- |
| Action | `ACT-008`, `ACT-161`, `ACT-190`, `ACT-223`, `ACT-341` | movement, slash, ability, defensive response and interaction |
| System Behaviour | `SYS-215`, `SYS-369`, `SYS-578`, `SYS-1512`, `SYS-1513`, `SYS-1514` | timing grades, charge, detonation, health and retry |
| Constraint | `CON-617`, `CON-809` | legal attack class and base Qi budget |
| Information | `INF-119`, `INF-310`, `INF-512` | health surfaces, stocks and attack cue |
| Objective | `OBJ-080` | named guard and lift progression |
| Time | `TIM-003` | live response windows |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `526` (`GAME-0001`–`GAME-0526`).
- Exact genome matches: none.
- Tied near matches: `GAME-0277` — Cuphead (`8 / 24 = 0.333333`); `GAME-0293` — Ori and the Will of the Wisps (`9 / 27 = 0.333333`).
- Supported combination subsets: none.
- Scan date: 2026-11-17.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0277` — Cuphead | `ACT-008`, `ACT-161`, `ACT-190`, `ACT-223`, `CON-617`, `INF-119`, `SYS-215`, `TIM-003` | Both read distinct incoming hazard classes and choose when to commit a defence or a charged attack during live combat. Cuphead parries eligible pink objects while relying on aimed fire and its own Super Meter. Nine Sols grades close deflections and applies a held mark that converts the target's recoverable damage. | Tied near (`0.333333`) |
| `GAME-0293` — Ori and the Will of the Wisps | `ACT-008`, `ACT-161`, `ACT-223`, `ACT-341`, `INF-119`, `SYS-215`, `SYS-369`, `SYS-578`, `TIM-003` | Both reposition a vulnerable character, time direct attacks and evasions, and return to an authored checkpoint after lethal harm. Ori's opening spends traversal tools and launch geometry to cross its path. Nine Sols turns successful defence into Qi and makes a second vulnerable commitment to settle a mark. | Tied near (`0.333333`) |

### Preserved research notes

- New genes: `SYS-1512`, `SYS-1513`, `SYS-1514`, `CON-809`, `INF-512`.
- Classification result: `New gene`.
- Evidence and reasoning: parry grade, charge, pending damage, and conversion
  are separate state changes at different points in the exchange.

## Taxonomy impact

- Registry changes: five Active definitions, thirteen transfers.
- Taxonomy-change record: [TAXONOMY_CHANGE_274](../../../research/taxonomy-changes/TAXONOMY_CHANGE_274.md).

## Negative results

- No earlier verified combination is a proper subset.
- No native frame timings, exact installed version or numeric damage model
  are established for the Switch target.

## Delta summary

## New facts

- [Observation | Corroborated | High] A valid early parry and a precise
  parry both feed Qi while differing in internal damage. Finishing the
  base talisman converts the enemy's outstanding internal damage.

## New genes

- [Observation | Corroborated | High] Five definitions in
  `TAXONOMY_CHANGE_274`, with medium confidence for exact-version
  inference on the budget and overlay boundaries.

## New combinations

- [Observation | Corroborated | High] No new verified combination added.

## Taxonomy changes

- [Observation | Corroborated | High] `TAXONOMY_CHANGE_274`.

## New questions

- How much of the early-parry and detonation window changes between the
  original Switch title updates?

## Next recommended game

- [Hypothesis | Limited | Medium] Original Windows *The Neverhood*.
- Optimisation criterion: contrast live timing and recoverable combat
  damage with a bounded chain of inspectable mechanical puzzles.
- Backlog impact: advance Selection 041 to its sixth candidate.

## Why this game

- [Hypothesis | Limited | Medium] The first miniboss puts timing grade,
  damage conversion and a resource-funded response in one short loop.
