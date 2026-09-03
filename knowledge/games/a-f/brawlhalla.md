---
game_id: GAME-0198
slug: brawlhalla
game_title: Brawlhalla
analysis_status: reviewed
reviewed: 2026-08-30
combination_ids:
  - COMB-0196
gene_ids:
  action:
    - ACT-008
    - ACT-294
    - ACT-295
    - ACT-355
    - ACT-356
  system:
    - SYS-215
    - SYS-456
    - SYS-637
    - SYS-638
    - SYS-639
    - SYS-640
  constraint:
    - CON-442
    - CON-519
    - CON-520
    - CON-521
    - CON-522
  information:
    - INF-142
    - INF-209
    - INF-254
  objective:
    - OBJ-121
  time:
    - TIM-003
---

# Game: Brawlhalla

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Parameters describe
gene instances but do not enter the signature.

## Analysis scope

- Version / ruleset: current unmodified Windows Steam live client, official
  Patch `10.10`, public build `24744406`, checked `2026-08-30`; Offline Play >
  Couch Party; one human P1 and one Easy CPU; both fixed to permanently unlocked
  base Legend Bödvar with default stance and controls; Stock, `3` lives,
  `8:00`, `100%` damage, teams off, Variation None, normal weapon spawns,
  gadgets off, Test Features off and manually selected Small Brawlhaven.
- Primary decision loop: read both fighters' position, pose, damage colour,
  remaining stocks, weapon state, spawned pickup and clock; move, jump, fast
  fall, dash, dodge, claim or throw a weapon, or commit an unarmed/Sword/Hammer
  attack; let contact, damage-dependent force, stun, aerial recovery and arena
  bounds resolve; repeat through stock resets until one participant loses the
  third stock and the result screen appears.
- Entry and exit: begins after the fixed Couch Party settings, Bödvar mirror
  participants and Small Brawlhaven are confirmed, at first retained control
  after the match countdown. It ends only at the post-match result after one
  participant crosses a blast zone with no stock remaining. A clock expiry,
  pause-menu quit or rules mismatch invalidates the trace and requires a clean
  restart rather than substituting a time-over result.
- Included: shared side-view movement and facing; ground, air and wall movement;
  two aerial jumps, Recovery and Exhausted Recovery; dash, spot/directional
  dodge and their current cooldown/reset behaviour; unarmed and Bödvar's Sword
  and Hammer attack vocabularies only as parameters; neutral weapon spawns,
  pickup, alternation, throw, expiry and disarm; damage colour, hitstun,
  damage-sensitive force, launch trajectory, platform/wall contact, blast-zone
  KO, damage reset, stock decrement and final-stock settlement; live HUD,
  clock and result.
- Excluded: ranked or casual matchmaking; human online opposition; network
  latency, disconnect and replacement-bot rules; private online rooms;
  tournaments and multi-game sets; weekly Legend rotation; purchases, Gold,
  Mammoth Coins, account/Legend experience, missions, Battle Pass, events,
  Glory, Guilds and cosmetics; every Legend other than Bödvar; alternate
  stances; crossovers; teams, free-for-all and more than two participants;
  Timed, Strikeout, Switchcraft, Morph and every non-Stock mode; gadgets;
  Test Features; alternate maps, map striking and Training frame-data tools.
- Potential scoped modules: one ranked 1v1 match; another fixed Legend pairing;
  one 2v2 team-stock match; Training frame-data verification; one weapon-family
  matchup; one custom game-mode variation.
- Direct-play status: not conducted. Current official product, roster and patch
  pages pin the live client, local-play surface and current balance vocabulary;
  official patch `8.07` pins offline settings and separate weapon/gadget
  controls. The maintained official wiki and current unmodified Couch Party
  recordings corroborate the fixed menu packet, stock lifecycle, movement,
  pickup and blast-zone transitions without importing ranked or account state.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `BHL-001` | Official Patch `10.10` corresponds to the current Windows Steam public build `24744406` | Observation | Corroborated | High | P3, S1 |
| `BHL-002` | Brawlhalla supports local play and one configurable Offline Play / Couch Party rules surface | Confirmed | Direct | High | P1, P2, P4 |
| `BHL-003` | Offline settings separately expose mode variation, weapon spawns and gadget spawns, permitting one ordinary Stock packet with gadgets and Test Features absent | Confirmed | Direct | High | P4, S2, S3 |
| `BHL-004` | The declared Bödvar mirror, Easy CPU and Small Brawlhaven packet fixes participants, authority, weapon pair, arena and terminal while permanent ownership removes weekly-rotation dependence | Observation | Corroborated | High | P5, S4, S7, S8 |
| `BHL-005` | Direct attacks apply damage and force; accumulated damage increases launch consequence and contact can create a blast-zone KO rather than depleting a conventional health bar | Observation | Corroborated | High | P3, S6, S8 |
| `BHL-006` | Ground/wall contact, aerial jumps, Recovery, Exhausted Recovery and dodge state form a resettable off-stage survival budget | Observation | Corroborated | High | S4, S8 |
| `BHL-007` | Neutral pickups spawn into the arena and become one of the selected Legend's two compatible weapons; pickup, throw, disarm and expiry change the live command vocabulary | Observation | Corroborated | High | P4, P5, S5, S8 |
| `BHL-008` | Each blast-zone KO resets the returning fighter's damage and consumes one stock; the first participant with no remaining stock loses and opens the result state | Observation | Corroborated | High | S2, S3, S8 |
| `BHL-009` | Rank, unlock economy, missions and cosmetics are separable from this offline match and do not alter its admitted terminal | Confirmed | Direct | High | P2, P4, P5 |

## Basic data

- Release / origin: `2017`, Blue Mammoth Games / Ubisoft; current live Patch
  `10.10` observed `2026-08-30`.
- Platform or physical form: Windows PC via Steam; unmodified Offline Play /
  Couch Party with one human and one Easy CPU participant.
- Puzzle family: real-time adversarial platform fighting, damage-to-displacement
  conversion, resettable aerial recovery and finite stock elimination.
- Primary sources:
  - `P1` — [official Brawlhalla homepage](https://www.brawlhalla.com/), for the
    current free platform-fighter identity, PC support and local/online scale.
  - `P2` — [official Steam product page](https://store.steampowered.com/app/291550/Brawlhalla/),
    for developer/publisher, release, Windows, local/single-player features,
    private rooms and separation of ranked and alternate modes.
  - `P3` — [official Patch 10.10 notes](https://www.brawlhalla.com/news/new-legend-qinghua-baobao-back-to-school-2026-and-more-patch-10-10),
    for the `2026-08-18` live version, current balance state and the authored
    distinction among attack damage, force and earlier knockout potential.
  - `P4` — [official Patch 8.07 notes](https://www.brawlhalla.com/news/vivi-patch-8-07),
    for the current Custom/Offline settings surface, Variation tab and separate
    weapon and gadget spawn controls.
  - `P5` — [official Legends roster](https://www.brawlhalla.com/legends), for
    Bödvar and the current roster/weapon vocabulary without importing another
    Legend into this mirror packet.
- Secondary sources:
  - `S1` — [Steam app build record](https://steamdb.info/patchnotes/24744406/),
    observed `2026-08-30`, for Windows public build `24744406`; official Patch
    `10.10` independently pins the corresponding live rules state.
  - `S2` — [maintained official wiki mode record](https://brawlhalla.wiki.gg/wiki/Modes),
    for Offline Play, Stock and separable variations.
  - `S3` — [maintained official wiki settings record](https://brawlhalla.wiki.gg/wiki/Settings),
    for Couch Party game-rule and Stock-clock settings.
  - `S4` — [maintained official wiki movement record](https://brawlhalla.wiki.gg/wiki/Movement),
    for ground/air/wall movement, two aerial jumps, Recovery, Exhausted
    Recovery, dodge and reset conditions.
  - `S5` — [maintained official wiki weapon record](https://brawlhalla.wiki.gg/wiki/Weapons),
    for neutral pickups, Legend-compatible conversion, alternation, throw,
    expiry and disarm.
  - `S6` — [maintained official wiki attack record](https://brawlhalla.wiki.gg/wiki/Attacks),
    for non-health damage colour and accumulated-damage/force relation.
  - `S7` — [maintained official wiki Brawlhaven record](https://brawlhalla.wiki.gg/wiki/Brawlhaven),
    for Small Brawlhaven's single flat platform and intended 1v1 scale.
  - `S8` — current unmodified Windows Couch Party recordings inspected on
    `2026-08-30`, for exact settings labels, countdown entry, Bödvar mirror,
    Easy bot, stock reset and result transitions; no hidden frame values or
    online behaviour are inferred.
- Claim IDs: `BHL-001`–`BHL-009`.

## Mechanical decomposition

### Action Genes

- Existing genes: `ACT-008`, directly navigate the fighter across ground, air
  and walls; `ACT-294`, commit fixed fighters, human/CPU sides and controls;
  `ACT-295`, enter one unarmed, Sword or Hammer character-command attack.
- New genes: `ACT-355`, claim, throw or discard a spawned arena weapon;
  `ACT-356`, commit a spot or directional dodge from an eligible live state.
- Parameters: Bödvar, P1, Easy CPU, default stance/controls, direction, jump,
  fast fall, wall contact, attack input, unarmed/Sword/Hammer member, pickup,
  throw vector, dodge direction and timing.
- Claim IDs: `BHL-004`–`BHL-007`.

### System Behaviour Genes

- Existing genes: `SYS-215`, resolve directly commanded real-time hostile
  combat; `SYS-456`, resolve a committed dodge's protected opening against
  attack overlap.
- New genes: `SYS-637`, convert accumulated damage and attack force into
  hitstun and launch displacement; `SYS-638`, convert blast-zone exits into
  damage reset, stock loss, respawn or final result; `SYS-639`, schedule neutral
  pickups and transform a claim into one compatible Legend weapon; `SYS-640`,
  consume and restore the fighter's aerial jump/Recovery opportunities through
  legal ground, wall and hit transitions.
- Resolution order: sample simultaneous inputs; validate current fighter,
  weapon, pose, recovery and dodge state; advance movement, spawn and attacks;
  resolve dodge/contact, damage, force, stun and trajectory; update aerial
  opportunity state; test stage and blast-zone bounds; decrement/reset a stock
  or settle the result; otherwise continue the live clock.
- Parameters: damage, fixed/variable force, defence, attack state, stun,
  trajectory, dodge protection/cooldown, aerial jumps, Recovery, Exhausted
  Recovery, wall/ground/hit reset, spawn timing/location, weapon alternation,
  blast zone, remaining stocks and clock. Exact frame data is not asserted.
- Claim IDs: `BHL-005`–`BHL-008`.

### Constraint Genes

- Existing gene: `CON-442`, fighting commands require an actionable fighter,
  compatible weapon/pose and legal recovery state.
- New genes: `CON-519`, aerial jump, Recovery and dodge use require current
  reset/cooldown eligibility; `CON-520`, the platform, walls and surrounding
  blast zones bound legal survival space; `CON-521`, a fighter has at most one
  active weapon and a neutral pickup may become only one of the selected
  Legend's two weapon classes; `CON-522`, three stocks and the declared clock
  bound one match, with time-over excluded from this accepted trace.
- Scarce strategic resources: three stocks, current damage tolerance, two
  aerial jumps plus Recovery opportunities, current dodge readiness, stage
  position, one held weapon and remaining match time.
- Claim IDs: `BHL-003`–`BHL-008`.

### Information Genes

- Existing genes: `INF-142`, attack motion, sound and contact effects cue
  reactive timing; `INF-209`, the shared side view exposes both fighters'
  spacing, pose, facing, airborne and hit state.
- New gene: `INF-254`, the duel interface exposes paired damage colours,
  remaining stocks, active weapon state, off-screen direction and match clock.
- Claim IDs: `BHL-005`–`BHL-008`.

### Objective Genes

- New gene: `OBJ-121`, be the last participant with at least one stock in the
  fixed Bödvar mirror match.
- Success, evaluation and failure: human success is the CPU's third blast-zone
  KO before the clock expires; human failure is P1's third KO; either opens the
  accepted result terminal. Time-over, quit and settings mismatch invalidate
  the research trace and require restart.
- Claim IDs: `BHL-008`.

### Time Genes

- Existing gene: `TIM-003`, movement, attacks, items, dodge/recovery state,
  damage trajectories and the match clock advance in real time while inputs
  are accepted.
- Claim IDs: `BHL-005`–`BHL-008`.

## Reproducible transitions

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Offline Play is open | Enter Couch Party; set Stock, `3`, `8:00`, `100%`, two players, Variation None, normal Weapons, Gadgets/Test Features off; add one Easy bot | The lobby records one bounded ordinary Stock packet | ruleset isolation | `BHL-002`, `BHL-003` |
| Legend select is ready | Assign default-stance Bödvar to P1 and CPU, then select Small Brawlhaven | The same Sword/Hammer vocabulary and one flat arena load after countdown | participant and arena fixation | `BHL-004` |
| Both fighters have first control | Walk, dash, jump, fast-fall or wall-jump | Pose, facing and position advance in the shared side-view space | continuous platform movement | `BHL-004`, `BHL-006` |
| An opposing attack is about to overlap | Commit an eligible spot or directional dodge | Protected opening ignores eligible overlap and dodge readiness enters its current cooldown/reset state | active timing defence | `BHL-006` |
| A neutral pickup is available and Bödvar is unarmed | Claim it, or later throw the held weapon | The pickup becomes Bödvar's alternating Sword/Hammer kit; throwing removes armed commands until another claim | spatial loadout transition | `BHL-007` |
| An attack contacts at current damage | Complete contact resolution | Damage rises; fixed/variable force, defence and accumulated damage determine stun and launch trajectory | damage-to-displacement coupling | `BHL-005` |
| A fighter is launched beyond the platform but not a blast zone | Spend jump, dodge or Recovery and seek ground/wall contact | Current eligibility moves the fighter; legal contact or hit state restores only the declared opportunities | finite off-stage recovery | `BHL-006` |
| A fighter crosses a blast zone with stocks remaining | Complete KO resolution | One stock is removed; damage and carried weapon reset and the fighter respawns for the same match | recoverable elimination | `BHL-008` |
| One fighter has one stock remaining | Force or suffer one further blast-zone exit | The last stock is removed and the result screen settles winner and loser | bounded final-KO terminal | `BHL-008` |

## Strategic and experiential structure

- Local decision: contest space, delay or commit an attack, dodge a readable
  threat, claim/deny the weapon spawn, or spend aerial recovery now versus
  preserve it for a later trajectory.
- Medium-term planning: accumulate damage before attempting high-force edge
  conversion, preserve centre-stage control, track the opponent's weapon and
  recovery options and vary landing timing against edge pressure.
- Long-term structure: convert repeated neutral, advantage and off-stage
  exchanges into three blast-zone KOs before losing the human side's stocks.
- Common heuristics: value centre stage; take the first safe weapon; punish
  committed recovery; use light attacks to build damage and stronger force near
  red; do not spend every aerial option immediately; touch safe ground before
  re-engaging.
- Failure attribution: pose, damage colour, trajectory, spent recovery options,
  weapon state and arena bounds are visible, though CPU timing and semi-random
  later spawn positions can jointly shape the exact exchange.
- Player-trust factors: shared view, readable hit effects, damage-colour
  gradient, stock icons, off-screen indicators, clock and explicit result make
  the causal path from contact to final KO auditable.
- Claim IDs: `BHL-005`–`BHL-008`.

## Replay and variation

- What changes between sessions: attack/dodge sequence, CPU policy, pickup
  timing/position after the first spawn, alternating weapon grant, damage,
  trajectories, recovery choices and winner.
- Randomness or procedural generation: arena and rules are fixed; later weapon
  spawn positions/times and CPU decisions vary inside the declared system.
- Multiple viable strategies: unarmed pressure, Sword or Hammer control,
  weapon denial/throws, grounded damage building, early edge guards and patient
  recovery can all reach the final-stock terminal.
- Typical replay motive: improve spacing, dodge timing, pickup conversion,
  damage-to-KO efficiency and off-stage recovery, or change the fixed matchup
  in a separately reviewed scope.
- Claim IDs: `BHL-004`–`BHL-008`.

## Adjacent systems and history

- Direct predecessors: earlier platform fighters establish the broad format but
  are not imported as current rules evidence.
- Variants: other Legends, teams, ranked, Timed/party modes, variations,
  gadgets, maps and Training remain separate scopes.
- Similar games: Street Fighter 6 shares a fixed side-view opponent, fighting
  commands, live spacing and visible combat state; Rocket League shares
  resettable aerial action eligibility; arena shooters share recoverable
  elimination but not damage-driven ring-out.
- Important differences: Brawlhalla has no depleting vitality round terminal in
  this packet. Accumulated damage changes launch risk, surrounding blast zones
  consume stocks, weapon objects change a fighter-owned command set and limited
  aerial recovery can reverse an otherwise losing trajectory.
- Claim IDs: `BHL-002`–`BHL-009`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-294`, `ACT-295`, `ACT-355`, `ACT-356` | movement, fighter setup, attacks, weapon interaction and dodge |
| System Behaviour | `SYS-215`, `SYS-456`, `SYS-637`–`SYS-640` | combat, dodge, launch, stocks, pickups and aerial reset |
| Constraint | `CON-442`, `CON-519`–`CON-522` | action state, recovery, arena, weapon and match bounds |
| Information | `INF-142`, `INF-209`, `INF-254` | cues, spacing, paired damage/stock HUD and clock |
| Objective | `OBJ-121` | last participant with stock |
| Time | `TIM-003` | continuous real-time match |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `197` (`GAME-0001`–`GAME-0197`).
- Exact genome matches: none.
- Tied near matches: `GAME-0172` — Street Fighter 6 (`8 / 33 = 0.242424`).
- Supported combination subsets: `COMB-0196`.
- Scan date: 2026-08-30.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| Street Fighter 6 (`GAME-0172`) | `ACT-008`, `ACT-294`, `ACT-295`, `SYS-215`, `CON-442`, `INF-142`, `INF-209`, `TIM-003` | Both fix two side-view fighters and turn live spacing, character commands, recovery state and readable attack cues into one bounded duel. Street Fighter depletes vitality, manages Drive/Super reserves and resets first-to-two rounds inside hard stage edges; Brawlhalla accumulates launch risk, contests spawned weapons, spends resettable aerial recovery and converts surrounding blast-zone exits into three-stock elimination. | Near, `0.242424` |

### Preserved research notes

- New genes: `ACT-355`, `ACT-356`, `SYS-637`–`SYS-640`, `CON-519`–
  `CON-522`, `INF-254`, `OBJ-121`.
- Classification result: `New combination of known and new genes`.
- Evidence and reasoning: Street Fighter supplies the reusable two-fighter
  setup, command, spacing, cue and real-time combat boundaries. New records are
  limited to the causal platform-fighter differences required by the accepted
  trace: spatial weapon objects, explicit dodge commitment, accumulated
  damage-to-launch conversion, recoverable stocks, aerial reset budget, blast
  zones and last-stock settlement.

## Taxonomy impact

- Registry changes: twelve new Active definitions; new Brawlhalla support for
  `ACT-008`, `ACT-294`, `ACT-295`, `SYS-215`, `SYS-456`, `CON-442`, `INF-142`,
  `INF-209` and `TIM-003`.
- Taxonomy-change record: none; no prior game signature changes.
- Candidate terms affected: platform fighter, damage colour, launch force,
  blast zone, stock, weapon pickup, unarmed state, aerial jump, Recovery,
  Exhausted Recovery, edge guard and final knockout.

## Negative results

- `CON-183` is rejected because its stock is a sequence of whole encounters
  whose final loss resets a larger run; Brawlhalla stocks are same-arena body
  returns inside one match and have no milestone refill.
- `CON-443` is rejected because it explicitly excludes ring-out victory and
  models hard horizontal corners; Small Brawlhaven permits off-stage traversal
  and surrounds its platform with terminal blast zones.
- `CON-446` and `OBJ-099` are rejected because no vitality-zero round or
  first-to-two round-win structure exists in the scoped Stock match.
- `SYS-382` is rejected because a KO consumes a personal finite stock and
  resets the same fighter rather than waiting for a team spawn timer.
- `ACT-164` is rejected because a neutral world pickup transforms into a
  Legend-compatible weapon and there is no carried multi-slot quickbar.
- Ranked rating, account progression, weekly rotation, currency and cosmetics
  are excluded parameters, not admitted genes.
