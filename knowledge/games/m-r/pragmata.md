---
game_id: GAME-0536
slug: pragmata
game_title: PRAGMATA
analysis_status: reviewed
reviewed: 2026-11-17
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-131
    - ACT-161
    - ACT-223
    - ACT-419
    - ACT-733
  system:
    - SYS-362
    - SYS-409
    - SYS-578
    - SYS-1549
    - SYS-1550
    - SYS-1551
    - SYS-1552
    - SYS-1553
  constraint:
    - CON-029
    - CON-269
    - CON-578
    - CON-589
  information:
    - INF-119
    - INF-142
    - INF-295
    - INF-318
    - INF-520
  objective:
    - OBJ-029
  time:
    - TIM-003
---

# Game: PRAGMATA

Use the [canonical vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
Damage, timings, encounter geometry and equipment capacity are parameters.

## Analysis scope

- Version / ruleset: US English PS5 Standard Edition, base campaign
  released April 17, 2026, solo Standard difficulty and default
  DualSense combat controls. Exact installed patch and timing frames
  were not independently observed. Select manual hacking with no
  assist that preserves a hack on damage, no New Game+ equipment and
  no optional weapon, suit or hacking upgrades. Keep the early Grip
  Gun, legal field Shockwave Gun and Stasis Net, and the Decode node
  acquired on the sector route if still stocked.
- Entry: in the Concourse of Sector 1, Solar Power Plant, ride the
  final lift after its enemy wave and interact with the control-room
  terminal. Begin at restored player control against SectorGuard.
  Prior acquisition and route fights establish the entry inventory.
- Primary decision loop: move Hugh out of charge paths and missile
  marks, aim at SectorGuard and advance Diana's cursor toward the
  green EXE node while the arena remains live. Detour through useful
  nodes or finish sooner. Exploit the exposed rear tank before the
  opening expires. Use restraint, recovery, the close Critical Shot
  or the newly taught Overdrive Protocol when eligible.
- Positive exit: incapacitate SectorGuard, collect the first Shelter
  License Key and reach the control-room terminal handoff. Stop
  before Shelter spending or travel into Sector 2. Negative exit:
  losing Hugh's health ends the current attempt.
- Included: real-time arena movement and attacks, manual hack path,
  typed nodes, interrupted route, temporary opening, finite support
  supply and health, boss health, Critical Shot, taught Overdrive and
  encounter credit. Excluded: Sketchbook Demo, prerelease show builds,
  prior exploration, Shelter economy and upgrades, later auto-hack
  and mode chips, other platforms, later sectors and post-release
  extra modes.
- Direct-play status: no PS5, executable, saved game or controller
  trace was inspected. Capcom and the US PS Store establish identity.
  Release play accounts and static screenshots establish the combat
  sequence. No audio or video was opened or played. Exact per-node
  modifiers, stagger thresholds and the restart snapshot are unverified.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
| --- | --- | --- | --- | --- | --- |
| PRA-001 | The US PS5 Standard Edition is the full April 17, 2026 release. Its single-player campaign separates the base game from Sketchbook. The Concourse terminal starts the first SectorGuard fight. | Confirmed | Corroborated | High | P1, P2, S1, S2 |
| PRA-002 | Aim at a legal target to show the grid. Face buttons move the cursor by directional steps. A connected, non-overlapping route from the current start reaches green EXE to complete the hack. Arena action continues. | Observation | Corroborated | High | P1, P3, S3, S5 |
| PRA-003 | Blue nodes along the submitted route add hack damage and prolong Open. An available Decode node adds a defense-reducing effect. The preview shows the currently planned hack and the target reports its Open state. | Observation | Corroborated | High | P3, S3, S4 |
| PRA-004 | Release aim to evade and, in the same attempt on the same target, resume from the unfinished route if it survives. Taking damage resets ordinary progress. A red failure node instead ends the attempt from within the grid. | Observation | Corroborated | High | S1, S3, S4 |
| PRA-005 | Successful execution deals hack damage and makes SectorGuard Open temporarily. Its rear canister is an exposed weak point. Moving behind and hitting it makes use of the opening. | Observation | Corroborated | High | P3, S1, S2, S3, S4 |
| PRA-006 | The boss telegraphs charges and missile impacts. Moving or evading can avoid their paths and impact areas. Stasis Net temporarily immobilizes it; that restraint is separate from the Open state. | Observation | Corroborated | High | S1, S2, S4, S6 |
| PRA-007 | The boss displays remaining health. Sufficient damage can produce a reachable Critical Shot prompt on a staggered boss. It takes a separate contextual input while the window remains. | Observation | Corroborated | High | S1, S2, S4 |
| PRA-008 | A mid-fight script teaches Overdrive Protocol. Outside its lesson the ability uses the gauge replenished by successful hacking. Its pulse damages, opens and temporarily immobilizes eligible nearby targets. | Observation | Corroborated | High | S1, S2, S3, S4 |
| PRA-009 | Hugh has one health reserve, carried recovery and finite field supplies. Defeating SectorGuard yields the first Shelter License Key before the end-of-sector handoff. | Observation | Corroborated | High | S1, S2, S4, S5 |

## Basic data

- Developer and publisher: Capcom. US PS5 Standard Edition released
  April 17, 2026. The mechanical profile is an aimed grid hack inside
  a live boss encounter with time-limited damage opportunities.
- Families: tactical forecast and counterplay, and agent routing and
  coordination.
- Sources accessed 2026-11-17:
  - **P1** — [US PlayStation Store Standard Edition](https://store.playstation.com/en-us/product/UP0102-PPSA02530_00-PRAGMATA00000000/),
    for the product, date, DualSense support and dual control.
  - **P2** — [Capcom after-launch confirmation](https://www.capcom.co.jp/ir/english/news/html/e260507.html),
    corroborating the revised launch date and PS5 release.
  - **P3** — [Capcom director and producer interview](https://blog.playstation.com/2026/03/19/pragmata-interview-combat-hacking-resource-management-and-more/),
    for the joint design of guns and hacking, the grid, Decode and
    resource tradeoffs. Release evidence below confirms the scoped
    combat behaviour independently of the interview's preview context.
  - **S1** — [PS5 release walkthrough, Solar Power Plant](https://gamefaqs.gamespot.com/ps5/292821-pragmata/faqs/82510/solar-power-plant),
    final lift through terminal, red failure, attack cues, the rear
    tank, Overdrive instruction and the first key.
  - **S2** — [Muhit Rahman's release walkthrough](https://intoindiegames.com/walkthroughs/pragmata-walkthrough-part-1-prologue-solar-power-plant/),
    for encounter phases, charge and missile, stagger, the key and
    static images of the boss and danger marks.
  - **S3** — [Will Sawyer's observed release hacking rules](https://www.gamesradar.com/games/action/pragmata-hacking/),
    for discrete inputs, route nodes, releasing aim, damage interruption,
    the Open display and Overdrive resource and pulse.
  - **S4** — [Rory Norris's release SectorGuard account](https://www.pcgamer.com/games/third-person-shooter/pragmata-sector-guard-boss/),
    for attack cues, rear position, Stasis Net, Critical Shot and the
    gauge-to-Overdrive loop.
  - **S5** — [PS5 release guide prologue](https://gamefaqs.gamespot.com/ps5/292821-pragmata/faqs/82510/prologue),
    and [PS5 hands-on release review](https://www.pushsquare.com/reviews/ps5/pragmata),
    for choice of Standard, recovery and default directional controls.
  - **S6** — [In-game weapon descriptions transcribed in a release guide](https://gmtreks.com/pragmata/weapon/9),
    for expansion of the Stasis Net on impact and temporary restraint.
- Claim IDs: PRA-001–PRA-009.

## Mechanical decomposition

### Action Genes

- Reuse `ACT-008`: move Hugh in the arena to leave impact areas
  or take an angle on the boss's rear.
- Reuse `ACT-131`: use a carried Repair Cartridge to recover health.
- Reuse `ACT-161`: aim and shoot with the currently equipped unit,
  including the shot used to land a Stasis Net.
- Reuse `ACT-223`: evade in response to a live charge or marked impact.
- Reuse `ACT-419`: close in on the stagger and take the contextual
  Critical Shot before the opportunity ends.
- New `ACT-733`: keep an eligible target aimed and add directional
  button steps to its on-screen hack, from the current head of the route.
- Claim IDs: PRA-002, PRA-005–PRA-009.

### System Behaviour Genes

- Reuse `SYS-362`: claim the key and bounded encounter credit after victory.
- Reuse `SYS-409`: sufficient qualifying damage produces a temporary
  stagger and a critical opening, separately from a normal Open state.
- Reuse `SYS-578`: attacks, recovery and attempt defeat use Hugh's one
  health pool.
- New `SYS-1549`: intermediate nodes change the eventual completed hack.
  Blue nodes increase its damage and Open duration, while a traversed
  stocked Decode node contributes its defense-reducing effect.
- New `SYS-1550`: completed EXE opens the armored target temporarily
  and reveals a vulnerable component that Hugh can attack.
- New `SYS-1551`: switching away from the grid by releasing aim
  can preserve the unfinished route. Damage without a preserving assist,
  or a failure node, cancels it. The red node is a route failure rather
  than an impassable wall.
- New `SYS-1552`: the introduced Overdrive pulse uses charge earned by
  successful hacks and imposes a distinct temporary open and immobilized
  state, with damage, on eligible targets in range.
- New `SYS-1553`: Stasis Net expands on impact and temporarily
  restricts movement of susceptible targets without itself completing
  a manual hack or establishing Open.
- Claim IDs: PRA-003–PRA-009.

### Constraint Genes

- Reuse `CON-029`: a hack is a connected single route through distinct
  cells using the directional grid topology.
- Reuse `CON-269`: hacking and Overdrive require the legal target
  or eligible range, ability readiness and available charge as applicable.
- Reuse `CON-578`: the Shockwave Gun and Stasis Net consume finite
  compatible supplies, with replacements available in the encounter.
- Reuse `CON-589`: the prompted Critical Shot requires proximity to
  the temporarily staggered living boss.
- Claim IDs: PRA-002, PRA-006–PRA-009.

### Information Genes

- Reuse `INF-119`: Hugh's health and stocked options, and Diana's
  charge, are available through the combat display.
- Reuse `INF-142`: crouch and movement cues and red ground telegraphs
  disclose pending attacks in time for a reaction.
- Reuse `INF-295`: the stagger and close follow-up have distinct
  visible cues.
- Reuse `INF-318`: continuously inspect remaining boss health.
- New `INF-520`: the target-linked grid shows the drafted route,
  node functions and predicted hack damage. The enemy's visible Open
  indicator shows that the draft has already resolved into a temporary
  state.
- Claim IDs: PRA-002, PRA-003, PRA-005–PRA-009.

### Objective Genes

- Reuse `OBJ-029`: defeat the one required guardian with Hugh alive.
- Claim ID: PRA-009.

### Time Genes

- Reuse `TIM-003`: the boss and pending arena hazards advance while
  Diana's ordinary grid accepts inputs.
- Claim IDs: PRA-002, PRA-004, PRA-006.

## Reproducible transitions

| Before | Action or event | Bounded resolution | What it establishes | Claim ID |
| --- | --- | --- | --- | --- |
| Unopened SectorGuard is targetable | Aim and enter adjacent steps while watching the arena | The route grows and the boss can still act | Manual cursor input does not pause combat | PRA-002 |
| An unfinished route is showing and a charge begins | Let go of aim, evade without damage and resume aiming at the same boss | In the absence of interruption the partial route survives | Repositioning is not automatically a puzzle restart | PRA-004 |
| There is a red cell off one possible path | Advance onto it deliberately in a comparative attempt | Current hack fails before EXE | A failure node can be entered and has a cost | PRA-004 |
| A safe path reaches EXE and another reaches it via extra blue nodes | Compare both successful paths without optional upgrades | Intermediate blue nodes add damage and lengthen the temporary opening | Valid completion and quality of completion differ | PRA-003 |
| EXE has resolved and SectorGuard is open | Move behind it and fire at the exposed canister. Use a compatible Stasis Net if available | The tank gives a damage opportunity. The net restrains movement separately | Space and timing still matter after puzzle completion | PRA-005, PRA-006 |
| Sufficient damage has staggered the boss | Reach the cue and take the Critical Shot before recovery | The contextual attack resolves by a separate input | Stagger is neither ordinary Open nor final defeat | PRA-007 |
| The boss introduces Overdrive | Follow the taught activation, then observe normal charging from hacks | Pulse creates a separate opening and damage opportunity | Scripted introduction differs from recurring gauge eligibility | PRA-008 |
| SectorGuard is defeated | Take the first Shelter License Key and proceed to the terminal handoff | Encounter credit is available before later Shelter spending | Bounded progression after the fight | PRA-009 |

## Strategic and experiential structure

A short route opens the boss earlier. A longer route through blue
nodes can buy a larger damage window, but consumes more of the live
time available before the next attack. Successful execution changes
the boss's defense in the same arena. Approaching its rear, choosing
when to spend ammunition and choosing whether to take the close
follow-up are separate spatial and timing decisions.

## Replay and variation

- Keep the same campaign, Standard difficulty, starting equipment and
  target. Compare the shortest safe finish, a blue-node detour, a red
  failure and an interrupted route after damage.
- Actual placements, carried amounts, the exact threshold to stagger,
  exposure seconds, the boss's future attack order and post-death
  recoverable state are not assigned fixed numerical values.

## Adjacent systems and history

- The early Sketchbook Demo uses other setup and encounter context.
  Its footage and layout are not evidence for the retail packet.
- Later Shelter levels enable modes and automation that can change a
  blue node's effect or spare a manual route. No such modifier is
  assumed in the first SectorGuard fight.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
| --- | --- | --- |
| Action | `ACT-008`, `ACT-131`, `ACT-161`, `ACT-223`, `ACT-419`, `ACT-733` | motion, repair, aimed shot, dodge, prompted shot and button-driven path |
| System Behaviour | `SYS-362`, `SYS-409`, `SYS-578`, `SYS-1549`, `SYS-1550`, `SYS-1551`, `SYS-1552`, `SYS-1553` | credit, stagger, health, node effects, timed exposure, interruption, pulse and restraint |
| Constraint | `CON-029`, `CON-269`, `CON-578`, `CON-589` | simple route, readiness, finite ammo and contextual reach |
| Information | `INF-119`, `INF-142`, `INF-295`, `INF-318`, `INF-520` | resources, warning, contextual cue, boss health and grid state |
| Objective | `OBJ-029` | defeat the mandatory guardian |
| Time | `TIM-003` | continued real-time combat during routing |

Canonical signature:

`ACT-008,ACT-131,ACT-161,ACT-223,ACT-419,ACT-733; SYS-362,SYS-409,SYS-578,SYS-1549,SYS-1550,SYS-1551,SYS-1552,SYS-1553; CON-029,CON-269,CON-578,CON-589; INF-119,INF-142,INF-295,INF-318,INF-520; OBJ-029; TIM-003`

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `535` (`GAME-0001`–`GAME-0535`).
- Exact genome matches: none.
- Tied near matches: `GAME-0303` — Sifu (`11 / 38 = 0.289474`).
- Supported combination subsets: none.
- Scan date: 2026-11-17.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
| --- | --- | --- | --- |
| `GAME-0303` — Sifu | `ACT-008`, `ACT-161`, `ACT-223`, `ACT-419`, `CON-589`, `INF-119`, `INF-142`, `INF-295`, `SYS-409`, `SYS-578`, `TIM-003` | Both use position and attack cues to survive live combat and exploit a reachable stagger for a separate close action. Sifu builds Structure pressure and uses age-linked revival. PRAGMATA routes a grid under live fire to expose a temporary rear target and uses a distinct charge-fed pulse. | Tied near (`0.289474`) |

### Preserved research notes

- New genes: `ACT-733`, `SYS-1549`–`SYS-1553` and `INF-520`.
- Classification result: `New gene`.
- Evidence and reasoning: adjacent button steps, route bonuses,
  executed vulnerability, partial-route continuity, restraint, pulse
  and visible state are independently testable transitions.

## Taxonomy impact

- Registry changes: seven Active additions and eighteen transfers.
- Taxonomy-change record: [TAXONOMY_CHANGE_283](../../../research/taxonomy-changes/TAXONOMY_CHANGE_283.md).

## Negative results

- Red failure cells differ from impassable grey cells. They end an
  attempted hack when entered, rather than merely preventing the step.
- Ordinary gunfire is less effective into armor. Universal immunity
  before every hack is not required or asserted.
- Neither the Overdrive lesson nor a Critical Shot establishes a
  universal numeric phase or timer. Published sources differ on how
  they describe the late attack escalation.

## Delta summary

## New facts

- [Observation | Corroborated | High] Cursor routing and boss pressure
  share time. A completed route changes the target's vulnerability
  while the player can still be threatened by arena attacks.

## New genes

- [Observation | Corroborated | High] Seven additions are documented
  in `TAXONOMY_CHANGE_283`.

## New combinations

- [Observation | Corroborated | High] No additional combination proposed.

## Taxonomy changes

- [Observation | Corroborated | High] `TAXONOMY_CHANGE_283`.

## New questions

- How do later mode chips transform the meaning of Open nodes after
  a first success, under a reproducible full-release loadout?

## Next recommended game

- [Hypothesis | Limited | Medium] Test original North American
  Game Boy Color *Kirby Tilt ’n’ Tumble* under Selection 042.
