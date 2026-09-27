---
game_id: GAME-0412
slug: splatoon-3
game_title: Splatoon 3
analysis_status: reviewed
reviewed: 2026-09-26
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-161
    - ACT-190
    - ACT-202
    - ACT-446
    - ACT-552
  system:
    - SYS-215
    - SYS-380
    - SYS-382
    - SYS-1096
    - SYS-1097
    - SYS-1098
  constraint:
    - CON-269
    - CON-698
  information:
    - INF-115
    - INF-116
    - INF-119
  objective:
    - OBJ-241
  time:
    - TIM-003
---

# Game: Splatoon 3

Use the canonical [vocabulary and genome rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Stage, ink colours, weapon tuning and special-point thresholds are parameters, not genes.

## Analysis scope

- Version / ruleset: original Nintendo Switch *Splatoon 3* online-capable launch version `1.1.0` (8 September 2022), one ordinary **Regular Battle: Turf War**, two teams of four, without Splatfest rules. Nintendo's launch presentation and update history anchor this version; later Nintendo teaching pages corroborate stable mode rules but are not proof that every balance number matched launch. No console build was played.
- Structured analysis target: `PLAT-NINTENDO-SWITCH` in [`knowledge/platforms/games.json`](../../platforms/games.json).
- Primary decision loop: choose a reachable floor patch or contested route, fire ink that paints it and threatens rivals, change between firing and own-colour Swim Form to traverse and refill, use the live map and team state to retake ground, and spend a ready sub or special when it helps the team's coverage before the match clock expires.
- Entry and exit: enter an ordinary 4v4 Turf War on one available launch stage at the initial spawn, with an ordinary equipped main/sub/special kit; stop at the three-minute results screen when eligible floor coverage is compared. Stage, initial kit and opponent policy must be recorded in a reproduction, not silently assumed fixed. Winning, losing or tying settles the same packet.
- Included: continuous aim and movement; main-weapon coating and enemy splats; own-colour swimming, wall traversal and ink-tank refill; enemy-ink movement penalty; a kit's sub and charge-earned special as bounded alternatives; temporary splat/return; map-visible territorial state and match clock; optional allied Super Jump; team ground-coverage adjudication. Weapon-specific damage, range, costs and special effect are parameters; the standard Splattershot kit is an illustrative official example, not an assertion that all kits act identically.
- Excluded: walls from the *scored* floor area, although their ink can enable traversal; Anarchy modes, Tricolor Turf War, Splatfests, Salmon Run, Story Mode, Tableturf, gear collection and account progression; post-launch stages, gear changes and weapon rebalance; exact launch damage, refill, respawn and special-point numeric tables; network latency and disconnect rules not established by the source packet.
- Potential scoped modules: one precisely instrumented weapon-kit interaction, a named Anarchy mode, Tricolor's asymmetric 4v2v2 objective, or the account-level unlock economy.
- Direct-play status: none. No Switch executable, network session, input trace, video or audio was inspected. This is a source-bounded rules reconstruction from Nintendo material, not a played match or frame-level measurement.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `SP3-001` | Ordinary Turf War is a two-team 4v4 match settled after three minutes by greatest ground coverage, not splat count. | Confirmed | Direct | High | N1, N2, N3 |
| `SP3-002` | Ink can coat surfaces and opponents; Swim Form moves quickly through allied ink and refills the personal ink tank. | Confirmed | Direct | High | N2, N4 |
| `SP3-003` | Coating an opponent's turf can take its ground away as well as expand the player's turf; walls are not included in the final painted-area count. | Confirmed | Direct | High | N3, N5 |
| `SP3-004` | Splatting an opponent removes them temporarily, after which they can re-enter the match. | Confirmed | Direct | High | N2, N4 |
| `SP3-005` | A weapon kit has main, sub and special roles; painting charges the special, and sub use consumes ink. | Confirmed | Direct | High | N1, N6, N7 |
| `SP3-006` | The map reveals the two teams' spatial ink coverage during the live match; enemy movement in enemy ink is hindered. | Confirmed | Direct | High | N3, N8 |
| `SP3-007` | An allied Super Jump can rapidly reconnect a respawned or distant player with the frontline, but exposes a landing risk. | Observation | Direct | Medium | N9 |
| `SP3-008` | Exact launch-version weapon balance values and frame ordering are not established by these public explanations. | Observation | Limited | High | N1–N9 |

## Basic data

- Release / origin: Nintendo published *Splatoon 3* for Switch on 9 September 2022; update `1.1.0`, released 8 September, enabled online communication.
- Platform or physical form: Nintendo Switch, ordinary online Regular Battle; the exact console image and network session were not inspected.
- Mechanical families: tactical forecast and counterplay (`FAM-009`), real-time system pressure (`FAM-010`).
- Primary Nintendo sources, accessed 2026-09-26:
  - **N1** — [Splatoon 3 Direct launch summary](https://splatoon.nintendo.com/en/news/catch-up-on-all-the-latest-from-the-splatoon-3-direct/), 10 August 2022: four per team, three minutes, special earned by inking and new movement.
  - **N2** — [Nintendo launch overview](https://splatoon.nintendo.com/en/news/fast-fun-and-frant-ink-action-awaits-in-splatoon-3-available-now/), 9 September 2022: original release, ink weapons, temporary splat and team-colour swimming.
  - **N3** — [Nintendo's Turf War rules explanation](https://www.nintendo.com/jp/games/feature/splatoonqa/battle/nawabari/index.html): floor wins at the timer; inked walls do not count. The page is a later official explanation of the mode, not a verified launch binary trace.
  - **N4** — [Nintendo gameplay basics](https://splatoon.nintendo.com/ca/gameplay/): own-ink diving, rapid traversal, refill and temporary splat.
  - **N5** — [Nintendo Regular Battle teaching page](https://splatoon.nintendo.com/en/news/beginner-basics-for-splatoon-3-the-ins-and-outs-of-playing-online/): repainting rival territory and checking the spatial map. It postdates launch and is used only for the stable mode boundary.
  - **N6** — [Nintendo weapon-kit guide](https://splatoon.nintendo.com/en/news/beginner-basics-for-splatoon-3-choosing-the-right-weapons/): main/sub/special roles and the Splattershot example; later weapon counts and rebalances are excluded.
  - **N7** — [Nintendo gear/ink guide](https://splatoon.nintendo.com/en/news/beginner-basics-for-splatoon-3-choosing-the-right-gear/): main/sub ink consumption and special-point gain. Gear purchasing and modifiers are outside this packet.
  - **N8** — [Nintendo movement tips](https://splatoon.nintendo.com/en/news/up-your-game-in-splatoon-3-with-these-quick-tips/): enemy ink impedes movement and ink helps allies move.
  - **N9** — [Nintendo research report on Super Jump](https://splatoon.nintendo.com/en/news/squid-research-lab-dives-deep-into-the-splatlands/): jump from spawn toward an ally trades fast frontline return against landing exposure. Its later balance details are excluded.
  - **N10** — [Nintendo update history](https://www.nintendo.com/en-gb/Support/Nintendo-Switch/Game-Updates/Splatoon-3-Update-History-2358763.html): version `1.1.0` and its online-enabling date.
- Claim IDs: `SP3-001`–`SP3-008`.

## Mechanical decomposition

### Action Genes

- `ACT-008` directs the avatar around a live stage; `ACT-202` switches the same controlled body between humanoid firing and compact Swim Form.
- `ACT-446` sustains the main ink output across reachable floor or wall, whereas `ACT-161` owns aimed hostile hits. One ink burst can affect both systems; these IDs mark different decision-relevant targets, not two mandatory button presses.
- `ACT-190` commits an equipped sub or charged special. `ACT-552` selects an eligible allied or spawn landing for Super Jump; it is not free-form teleportation.
- Claim IDs: `SP3-002`, `SP3-005`, `SP3-007`.

### System Behaviour Genes

- `SYS-1096` writes and rewrites team-colour ownership on eligible ground while also coating climbable surfaces. A newly coated enemy patch removes their owned area; a coated wall changes movement access but not scored area.
- `SYS-1097` debits the personal ink tank for shooting or sub use, then restores it during eligible own-ink swimming; the tank is not a fixed finite ammunition clip.
- `SYS-1098` accrues special readiness through eligible inking and spends it on an equipped special. `SYS-380` resolves the particular sub or special effect without treating every kit as identical.
- `SYS-215` resolves shots, damage and splats under live opponents; `SYS-382` returns a splatted player to the team spawn after a delay, preserving the running match and its inked terrain.
- Resolution order for one bounded exchange: fire → consume ink → projectile/contact paints an eligible surface and can damage a rival → own/enemy coverage updates → special readiness may advance from eligible inking → splat temporarily removes a defeated player → timer and rivals continue throughout → final ground ownership is compared at expiry. Exact same-frame priority and numerical rates remain untested.
- Claim IDs: `SP3-001`–`SP3-005`, `SP3-008`.

### Constraint Genes

- `CON-698` permits fast Swim Form travel/refill through allied ink, including an allied-coated climbable wall, but not equivalent travel through opposing ink. Enemy colour also hinders ordinary movement; a wall is still excluded from scored ground.
- `CON-269` gates the sub by compatible ink and the special by earned readiness and legal use context. A shot with no ink cannot be silently resolved as if the reservoir were full.
- Claim IDs: `SP3-002`, `SP3-005`, `SP3-006`.

### Information Genes

- `INF-115` keeps unseen opponents' live positions partial rather than omniscient. `INF-116` shows allies, match time and spatial team coverage on the map; `INF-119` shows the personal ink tank and special readiness.
- The visible ink map reports present state, not guaranteed control at three minutes.
- Claim IDs: `SP3-006`, `SP3-008`.

### Objective and Time Genes

- `OBJ-241` compares only eligible ground area owned by each team when the three-minute Turf War clock ends. A splat affects opportunity to paint, not an independent victory total.
- `TIM-003` captures continuing match time, opponent actions, coating and special readiness while the player decides. The clock is a positive evaluation boundary, not `CON-068`'s failure-on-expiry deadline.
- Claim IDs: `SP3-001`, `SP3-003`.

## Reproducible transitions

| Before | Action | Bounded resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Bare eligible floor and a partly full tank | Sustain main fire across a patch | Tank falls; patch becomes team colour; special readiness can grow | coating is state and resource conversion | `SP3-002`, `SP3-005` |
| Opponent-coloured floor lies within range | Coat that floor | Its ownership changes; opponent loses that turf while the firing team gains it | contested repaint, not additive lifetime score | `SP3-003` |
| Allied-painted floor or climbable wall is reachable | Enter Swim Form and traverse | Faster own-colour route and ink refill; wall permits travel but is not counted as ground | form and surface-dependent mobility | `SP3-002`, `SP3-003` |
| Enemy-coloured patch interrupts the route | Try to swim through it | Equivalent own-ink swim/refill does not occur and ground travel is impeded | colour is a functional constraint | `SP3-006` |
| Sub has enough ink or special is charged | Commit that equipped ability | Its typed effect resolves; resource or readiness is spent | kit alternatives have gates | `SP3-005` |
| A rival receives sufficient ink damage | Continue firing | Rival is splatted temporarily, then may return while the match continues | combat is instrumental, not terminal | `SP3-004` |
| An ally is an eligible map landing | Select Super Jump | Player crosses rapidly toward ally, with a vulnerable landing opportunity | team-position repositioning | `SP3-007` |
| Three-minute timer expires | Inspect result | Eligible ground colour areas are compared; painted walls and splat count do not replace that metric | Turf War terminal | `SP3-001`, `SP3-003` |

## Strategic and experiential structure

- Local decision: fire to paint new or enemy-held ground, fight a blocking rival, or dive to refill and change angle.
- Medium-term planning: preserve paths of own ink from spawn to contested floor; use map-visible unpainted or repainted areas rather than chasing splat count.
- Long-term structure: allocate the finite three-minute window among safe base coverage, contested mid-map control and late repainting, then accept final area adjudication.
- Failure attribution: a team can splat more opponents and still lose when the other side owns more eligible ground. Current map state is observable, but opponent action and exact future area are not guaranteed.
- Player-trust factors: wall coating is useful for movement but explicitly excluded from the score; own-colour mobility and refill align the tactical route with the visible terrain state.
- Claim IDs: `SP3-001`–`SP3-008`.

## Replay and variation

- Stage layout, team compositions, kit parameters, player decisions and opponent responses vary; no specific stage rotation or matchmaking distribution is inferred.
- The same player action can change territorial ownership, create mobility and threaten a rival. This coupling is the mechanical distinction from a conventional elimination-first shooter.
- Claim IDs: `SP3-001`–`SP3-007`.

## Adjacent systems and history

- Earlier Splatoon titles also use ink and Turf War, but they are not separately analysed in this corpus; no exact signature identity is asserted. The 2022 launch introduced Squid Roll and Squid Surge, but this record does not infer their precise frame-level values.
- Battlefield 6 and Marvel Rivals share live team combat and re-entry, yet their analysed objectives settle through tickets or a pushed objective rather than continuously overwritten ground area. PowerWash Simulator shares spatial application but its treated state is persistent task progress, not a rival-reversible team contest.
- Claim IDs: `SP3-001`–`SP3-008`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-161`, `ACT-190`, `ACT-202`, `ACT-446`, `ACT-552` | kit, range, chosen jump destination |
| System Behaviour | `SYS-215`, `SYS-380`, `SYS-382`, `SYS-1096`–`SYS-1098` | ink spread, repaint, refill and special rates |
| Constraint | `CON-269`, `CON-698` | own colour, tank capacity, ability readiness |
| Information | `INF-115`, `INF-116`, `INF-119` | partial opponents, map, clock and gauges |
| Objective | `OBJ-241` | eligible floor area and three-minute expiry |
| Time | `TIM-003` | live opponents and clock |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `411` (`GAME-0001`–`GAME-0411`).
- Exact genome matches: none.
- Tied near matches: `GAME-0147` — Marvel Rivals (`11 / 33 = 0.333333`).
- Supported combination subsets: none.
- Scan date: 2026-09-26.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0147` — Marvel Rivals | `ACT-008`, `ACT-161`, `ACT-190`, `SYS-215`, `SYS-380`, `SYS-382`, `CON-269`, `INF-115`, `INF-116`, `INF-119`, `TIM-003` | Both use direct real-time team combat, typed abilities, temporary knockouts and a live team HUD. Marvel Rivals' analysed packet selects heroes and converts a captured area into an escort phase; Turf War instead continually repaints eligible ground, uses own-colour ink for mobility and refill, earns its special by painting and settles at a fixed time by current floor area. | Near, `0.333333` |

## Taxonomy impact

- Six new boundaries (`ACT-552`, `SYS-1096`–`SYS-1098`, `CON-698`, `OBJ-241`) are documented in [`TAXONOMY_CHANGE_150`](../../../research/taxonomy-changes/TAXONOMY_CHANGE_150.md).
- `SYS-630` is rejected for opponent-reversible territorial ownership; `SYS-381` is rejected because the special is earned by painting rather than combat contribution or received damage. No earlier reviewed signature changes.

## Negative results

- `CON-068` rejected: clock expiry *settles* a Turf War rather than automatically failing an unfinished task.
- `OBJ-079` rejected: opponent ticket depletion is not the Turf War score.
- `CON-516` rejected: there is no one-time treatment threshold that closes the match before the clock.
- Exact launch balance tables, wall-counting beyond Nintendo's explicit exclusion, network interruptions and future-stage rules are not inferred.

## Delta summary

Ordinary Turf War turns a single finite three-minute contest into a reversible ground-colour race. Ink is at once ammunition, traversable terrain, refill medium and the team's terminal measure; splats only change painting opportunity.

## New facts

- [Confirmed | Direct | High] Nintendo explicitly excludes painted walls from Turf War's scored area although own ink on walls aids traversal (`SP3-002`, `SP3-003`).
- [Confirmed | Direct | High] A splat is temporary, while the match winner is decided by eligible ground area at expiry (`SP3-001`, `SP3-004`).

## New genes

- [Confirmed | Direct | High] Six new typed boundaries separate map-selected team return, rival-reversible coating, own-ink refill, paint-earned special readiness, colour-dependent swim access and timed floor-area adjudication.

## New combinations

- [Observation | Direct | Medium] No new verified combination is asserted from this one game; subset matches are recomputed below.

## Taxonomy changes

- [Confirmed | Direct | High] `TAXONOMY_CHANGE_150` admits six genes without revising an earlier signature.

## New questions

- What are the exact version-1.1.0 ink-tank and special-point thresholds for a named kit, and how do they change under later balance patches?
- Does a frame-inspected launch session reveal a tie-resolution rule or disconnect branch absent from Nintendo's explanatory pages?

## Next recommended game

- [Hypothesis | Limited | Medium] `GAME-0413` *Ape Escape*.
- Optimisation criterion: alternate from team real-time territorial painting on Switch to dual-stick solo gadget capture on PlayStation.
- Expected information gain: isolate stick-directed gadget control and individual monkey-capture gates from a score-by-area contest.
- Backlog impact: no selected subject displaced.

## Why this game

- [Hypothesis | Corroborated | Medium] Splatoon 3 tests whether a surface's reversible team colour can simultaneously govern movement, resource recovery and a fixed-time objective without being collapsed into generic elimination combat or permanent cleaning progress.
