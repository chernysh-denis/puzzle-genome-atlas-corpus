---
game_id: GAME-0172
slug: street-fighter-6
game_title: Street Fighter 6
analysis_status: reviewed
reviewed: 2026-08-28
combination_ids:
  - COMB-0170
gene_ids:
  action:
    - ACT-008
    - ACT-294
    - ACT-295
    - ACT-296
    - ACT-297
    - ACT-298
  system:
    - SYS-215
    - SYS-520
    - SYS-521
    - SYS-522
  constraint:
    - CON-442
    - CON-443
    - CON-444
    - CON-445
    - CON-446
  information:
    - INF-142
    - INF-209
    - INF-210
  objective:
    - OBJ-099
  time:
    - TIM-003
---

# Game: Street Fighter 6

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Parameters describe
gene instances but do not enter the signature.

## Analysis scope

- Version / ruleset: Steam public build `24176760`, updated with the Year 4
  Yasmine release on `2026-08-03`; Fighting Ground > Versus > One on One;
  offline human-versus-CPU; base-roster Ryu against base-roster Luke; both use
  Classic controls; default vitality, full six-stock Drive Gauge, standard
  Super Art Gauge, `99`-second rounds, first to two round wins, no Advantage.
- Primary decision loop: read both fighters' spacing, pose, vitality, Drive and
  Super state plus the round clock; move, crouch, jump, guard, strike, throw or
  commit a legal Drive/Super technique; let real-time contact, defence, damage,
  recovery and gauge rules resolve; repeat until one round and then the match
  result settle.
- Entry and exit: begins after Ryu, Luke, Classic controls, Genbu Temple and the
  default One on One rules are confirmed; ends when either fighter records the
  second round win and the match result appears.
- Included: horizontal movement, crouching, jumping and dashing; normal and
  command attacks; Hadoken, Shoryuken and Tatsumaki Sen-pu-kyaku only as Ryu
  move parameters; blocking, throws and throw escape; hit, Counter Hit, Punish
  Counter, block, armour, knockdown, wake-up and Reversal states; projectiles;
  Drive Impact, Drive Parry, Drive Rush, Drive Reversal and Overdrive attacks;
  Drive depletion, recovery, Burnout and corner Stun; Super Arts; vitality,
  timer, round and gauge HUD; KO, time-over and first-to-two settlement.
- Excluded: Modern and Dynamic controls; Advantage; team and Gyro battles;
  Extreme Battle; Arcade, Training, Combo Trials and online matchmaking;
  World Tour, Battle Hub, avatars, commentary, ranks, Kudos, Fighting Passes,
  events, cosmetics and replay browsing; every downloadable fighter and stage;
  character-specific Ryu/Luke move-list details not causal to the ordinary
  duel; tournament set rules beyond this one in-game match.
- Potential scoped modules: Modern-control comparison; one online ranked set;
  Extreme Battle; one character-specific combo route; Battle Hub cabinets;
  World Tour progression.
- Direct-play status: not conducted. The current official web manual defines
  Fighting Ground, One on One, control types and HUD state; Capcom's Drive
  system explanation defines its six stocks, five techniques and Burnout; the
  current Steam package and official Year 4 announcement pin the reviewed
  build, while recorded default Versus play corroborates round transitions and
  the declared Ryu-versus-Luke trace.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `SF6-001` | Steam public build `24176760` carries the 3 August 2026 Yasmine/Year 4 update | Observation | Corroborated | High | P1, P7, S1 |
| `SF6-002` | Fighting Ground is the traditional fighting-game pillar and Versus One on One supports CPU or human opposition | Confirmed | Direct | High | P2, P5 |
| `SF6-003` | Classic is a six-button control type distinct from Modern and Dynamic | Confirmed | Direct | High | P4, P6 |
| `SF6-004` | The duel exposes vitality, Drive, timer, round markers, notices and a three-stock Super Art Gauge | Confirmed | Direct | High | P3 |
| `SF6-005` | Direct movement, attacks, guard and throws resolve continuously through range, contact and recovery state | Observation | Corroborated | High | P3, P6, S2 |
| `SF6-006` | The Drive System has five techniques drawing on six stocks; depletion causes Burnout until recovery | Confirmed | Direct | High | P3, P6 |
| `SF6-007` | Burnout removes Drive techniques and a corner Drive Impact can cause Stun | Confirmed | Direct | High | P6 |
| `SF6-008` | Super Art stock is earned through attacks and unused stock carries between rounds | Confirmed | Direct | High | P3 |
| `SF6-009` | Default One on One resolves each round by KO or timer comparison and ends after the second round win | Observation | Corroborated | High | P3, S2 |
| `SF6-010` | World Tour, Battle Hub, online progression and alternate Versus formats are separable from this duel | Confirmed | Direct | High | P2, P4, P5 |

## Basic data

- Release / origin: `2023`, Capcom Co., Ltd.; current Year 4 Steam build
  observed `2026-08-28`.
- Platform or physical form: Windows PC via Steam; offline Fighting Ground
  Versus match with one human and one CPU participant.
- Puzzle family: real-time adversarial fighting, spacing and timing, coupled
  offensive/defensive resource management and finite round victory.
- Primary sources:
  - `P1` — [official Steam product page](https://store.steampowered.com/app/1364780/Street_Fighter_6/),
    for Capcom authorship, release, platform and the three principal modes.
  - `P2` — [official Street Fighter 6 web manual](https://game.capcom.com/manual/SF6/en/steam/top),
    for the separation of Fighting Ground, World Tour and Battle Hub.
  - `P3` — [official Fighting Ground HUD manual](https://game.capcom.com/manual/SF6/en/steam/page/3/3),
    for vitality, Drive, timer, round markers, combat notices and Super Art
    stock/carry-over.
  - `P4` — [official Fighting Ground manual](https://game.capcom.com/manual/SF6/en/steam/page/6/1),
    for Classic, Modern and Dynamic controls and their boundaries.
  - `P5` — [official Versus manual](https://game.capcom.com/manual/SF6/en/steam/page/6/4),
    for CPU/human One on One and the separation of Team Battle.
  - `P6` — [Capcom's official battle-system introduction](https://news.capcomusa.com/2022/06/02/street-fighter-6-redefines-the-genre-in-2023/),
    for Classic/Modern input contrast, the five Drive techniques, six stocks,
    gauge recovery, Burnout and corner Stun.
  - `P7` — [official Yasmine release announcement](https://steamcommunity.com/games/1364780/announcements/detail/1839676055894097),
    for the `2026-08-03` Year 4 release and accompanying all-character battle
    adjustments.
- Secondary sources:
  - `S1` — [Steam app-info mirror](https://api.steamcmd.net/v1/info/1364780),
    observed `2026-08-28`, for public build ID `24176760`; the official Steam
    announcement independently pins its release date and content state.
  - `S2` — current unmodified PC Fighting Ground Versus recordings inspected
    on `2026-08-28`, for the default `99`-second first-to-two round flow, Ryu
    and Luke transitions and result screen; no frame-data claim is inferred.
- Claim IDs: `SF6-001`–`SF6-010`.

## Mechanical decomposition

### Action Genes

- Existing gene: `ACT-008`, directly move the active fighter through the
  side-view arena with walk, crouch, jump and dash parameters.
- New genes: `ACT-294`, commit fighter, side and control type before the duel;
  `ACT-295`, enter a character-command attack; `ACT-296`, hold or release a
  directional guard; `ACT-297`, attempt a throw or matching throw escape;
  `ACT-298`, commit one legal Drive technique.
- Parameters: Ryu, Luke, CPU level, Classic mapping, direction, button strength,
  motion sequence, attack member, spacing, facing, Drive technique and Super
  level.
- Claim IDs: `SF6-002`, `SF6-003`, `SF6-005`, `SF6-006`.

### System Behaviour Genes

- Existing gene: `SYS-215`, resolve directly commanded real-time combat through
  range, cadence, damage, defence and defeat state.
- New genes: `SYS-520`, update Drive stocks, recovery, loss, Burnout and corner
  Stun; `SYS-521`, earn, carry and spend Super Art stock; `SYS-522`, adjudicate
  KO/time-over rounds, reset round state and settle the first-to-two match.
- Resolution order: sample simultaneous input; validate command and current
  fighter state; advance movement/attack; resolve body, strike, projectile,
  throw, armour and guard contact; apply damage, gauge and recovery state;
  evaluate vitality and timer; award/reset a round or settle the match.
- Parameters: active/recovery frames, hit and push geometry, damage, block,
  armour, counter class, knockdown, Drive change, Super change, timer and round
  score. Exact frame data is intentionally not asserted.
- Claim IDs: `SF6-004`–`SF6-009`.

### Constraint Genes

- New genes: `CON-442`, command legality depends on current fighter and control
  state; `CON-443`, the shared side-view arena bounds bodies while push contact
  and airborne crossover govern spacing and facing; `CON-444`, Drive techniques
  require their stock and are unavailable during Burnout; `CON-445`, Super Arts
  require sufficient current Super stock; `CON-446`, each round and the match
  obey finite vitality, clock and win-count terminals.
- Scarce strategic resources: vitality, six Drive stocks, up to three Super Art
  stocks, remaining round time, screen position and recovery opportunity.
- Claim IDs: `SF6-004`–`SF6-009`.

### Information Genes

- Existing gene: `INF-142`, animation, contact effects, sound and notices cue
  attack, Counter Hit, throw escape and Reversal timing.
- New genes: `INF-209`, expose both fighters' relative pose, spacing and live
  hit/guard/knockdown state; `INF-210`, expose paired vitality and Drive plus
  timer, round markers and Super Art stock in one duel HUD.
- Claim IDs: `SF6-004`–`SF6-009`.

### Objective Genes

- New gene: `OBJ-099`, win the fixed One on One match by recording two round
  wins before the opponent.
- Success, evaluation and failure: KO or greater vitality at time-over awards a
  round; the second awarded round settles match victory; the opponent reaching
  that threshold first is failure for the selected human side.
- Claim IDs: `SF6-009`.

### Time Genes

- Existing gene: `TIM-003`, both fighters, projectiles, attack/recovery states,
  gauges and the round clock advance in real time while inputs are accepted.
- Claim IDs: `SF6-005`–`SF6-009`.

## Reproducible transitions

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| One on One setup is open | Assign Ryu to P1, Luke to CPU, Classic controls and confirm | The declared fighters enter Genbu Temple with default HUD resources | bounded participant and control contract | `SF6-002`, `SF6-003` |
| Fighters are at neutral range | Walk, crouch, jump or dash | Position, facing and legal collision update continuously inside stage bounds | live spacing authority | `SF6-005` |
| Ryu is actionable at Hadoken range | Enter the legal Classic Hadoken command | A projectile advances; Luke may be hit, guard, parry, evade or interrupt according to contact state | command-to-contact combat | `SF6-005` |
| Luke's strike is about to overlap Ryu | Hold back or commit Drive Parry | Ordinary guard converts legal contact to block resolution; Parry uses Drive state and changes the consequence | distinct defence commitments | `SF6-005`, `SF6-006` |
| One fighter is throwable at close range | Attempt throw while the opponent enters the escape input | Matching timing resolves Throw Escape; otherwise the throw damages and repositions the target | simultaneous throw contest | `SF6-005` |
| Ryu has enough Drive stock | Commit Drive Impact, Parry, Rush, Reversal or an Overdrive attack | The declared cost/state applies; exhausted Drive enters Burnout until recovery | shared offensive/defensive resource | `SF6-006`, `SF6-007` |
| Super Art stock is available | Enter one legal Super Art command | The level cost is consumed and the attack resolves; unused stock otherwise survives the round boundary | independently retained combat meter | `SF6-004`, `SF6-008` |
| Luke's vitality reaches zero | Complete the current resolution | Ryu receives a round marker; positions, vitality and Drive reset for the next round while eligible Super stock carries | round-to-round reset boundary | `SF6-004`, `SF6-008`, `SF6-009` |
| Ryu already has one round win | Resolve another KO or favourable time-over | The second marker settles the match and opens the result state | finite match terminal | `SF6-009` |

## Strategic and experiential structure

- Local decision: judge range, recovery and the opponent's current option, then
  choose movement, guard, throw, attack or a resource-backed response.
- Medium-term planning: preserve screen position and enough Drive to defend,
  decide whether damage or advantage justifies Drive/Super spend and vary
  timing to avoid predictable defence.
- Long-term structure: turn repeated neutral, pressure and wake-up exchanges
  into two round wins while Super stock can bridge a round boundary.
- Common heuristics: contest unsafe approach with a normal; anti-air a visible
  jump; guard before challenging delayed pressure; throw a passive defender;
  avoid emptying Drive without a credible payoff; reserve Super for a confirmed
  hit or decisive reversal.
- Failure attribution: direct input and spacing errors are visible, but hit
  trade, armour, buffered recovery and CPU timing can jointly determine the
  resulting state.
- Player-trust factors: readable poses, hit effects, notices, exact visible
  gauges, round markers and timer make contact and terminal changes auditable.
- Claim IDs: `SF6-004`–`SF6-009`.

## Replay and variation

- What changes between sessions: fighter pairing, CPU behaviour, stage,
  spacing, attack/defence sequence, resource spend and round outcome.
- Randomness or procedural generation: the arena and rules are fixed; CPU
  policy and fine timing vary, but no random generated map enters the scope.
- Multiple viable strategies: zoning, close pressure, throws, reactive defence,
  Drive conversion and Super conservation can all produce two round wins.
- Typical replay motive: learn the matchup, reduce unsafe commitments, improve
  punishes and resource conversion or change fighter/control profile.
- Claim IDs: `SF6-003`, `SF6-005`–`SF6-009`.

## Adjacent systems and history

- Direct predecessors: earlier numbered Street Fighter games establish the
  series lineage but are not imported as evidence for this build.
- Variants: Modern/Dynamic controls, Extreme Battles, teams, online ranks and
  each character matchup remain separable future scopes.
- Similar games: Marvel Rivals, Hollow Knight: Silksong and Monster Hunter Wilds
  share live movement, attack/defence timing and visible combat resources;
  Counter-Strike 2 shares finite real-time rounds and match scoring.
- Important differences: Street Fighter fixes exactly two always-opposed
  fighters in one side-view arena, carries Super stock across short rounds and
  makes Drive both an offensive and defensive reserve whose exhaustion changes
  the rules through Burnout.
- Claim IDs: `SF6-002`, `SF6-006`–`SF6-010`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-294`–`ACT-298` | fighter, controls, movement, attack, guard, throw and Drive command |
| System Behaviour | `SYS-215`, `SYS-520`–`SYS-522` | contact, recovery, gauges, Burnout, round and match settlement |
| Constraint | `CON-442`–`CON-446` | action state, stage, Drive, Super, vitality, clock and round gates |
| Information | `INF-142`, `INF-209`, `INF-210` | poses, spacing, attack cues and paired duel HUD |
| Objective | `OBJ-099` | first to two round wins |
| Time | `TIM-003` | simultaneous real-time duel and round clock |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `171` (`GAME-0001`–`GAME-0171`).
- Exact genome matches: none.
- Tied near matches: `GAME-0116` — The Stanley Parable: Ultra Deluxe (`2 / 24 = 0.083333`).
- Supported combination subsets: `COMB-0170`.
- Scan date: 2026-08-28.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| The Stanley Parable: Ultra Deluxe (`GAME-0116`) | `ACT-008`, `TIM-003` | Both accept direct movement while the represented world continues in real time. Stanley's authored office route centres navigation, narrator reaction and loop-retained endings; Street Fighter instead fixes one visible opponent and resolves attacks, guard, throws, paired meters and first-to-two rounds inside one arena. | Near, `0.083333` |

## Taxonomy impact

- Registry changes: sixteen Active definitions plus new Street Fighter support
  for `ACT-008`, `SYS-215`, `INF-142` and `TIM-003`.
- Taxonomy-change record: none; no prior boundary or signature changes.
- Candidate terms affected: fighting-game command, directional guard, throw
  escape, Drive technique, duel spacing, Burnout, Super stock and round win.

## Negative results

- `ACT-161` is rejected because Ryu's body and learned moves are not an equipped
  melee or ranged tool.
- `CON-324` is rejected because Drive Parry is a continuing player-selected
  defence state, not only the prompt-timed response gene isolated for
  turn-based telegraphed attacks.
- `SYS-409` is rejected because Drive is a general offence/defence reserve and
  Burnout state, not merely a depleted guard/stance gauge that opens one
  monster critical.
- Ranked points, character progression and paid roster access do not affect the
  chosen offline duel and are excluded from its signature.
