---
game_id: GAME-0351
slug: street-fighter-ii-the-world-warrior
game_title: "Street Fighter II: The World Warrior"
analysis_status: reviewed
reviewed: 2026-09-21
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-294
    - ACT-295
    - ACT-296
    - ACT-297
  system:
    - SYS-215
    - SYS-522
  constraint:
    - CON-442
    - CON-443
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

# Game: Street Fighter II: The World Warrior

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Ryu, Ken, Chun-Li,
Hadoken, Shoryuken, Tatsumaki Senpu-kyaku and the World Warrior stage names are
carrier parameters, not gene names.

## Analysis scope

- Version / ruleset: original North American English Capcom CPS-1 arcade
  program set `sf2`, World rev G, build date `1991-05-22`; one-player mode,
  factory difficulty `Normal` (`3`) and ordinary timer; one complete first CPU
  match after selecting Ryu.
- Primary decision loop: read the two fighters' spacing, pose, vitality and
  round time; move, crouch, jump, guard, strike, throw or enter one legal
  special-move command; allow real-time contact, damage and recovery to settle;
  repeat until one side wins two rounds.
- Entry: one credit has started one-player play, Ryu is selected from the eight
  available World Warriors and the first generated CPU opponent has entered
  the arena.
- Positive terminal: Ryu records the second round win and the match result
  advances the one-player route.
- Negative terminal: the CPU opponent records the second round win and the
  continue decision appears; continuing the arcade route is outside scope.
- Included: eight-way movement; crouch and jump; six-button light, medium and
  heavy punches and kicks; character-owned normal and special attacks;
  projectile contact; opponent-relative standing/crouching guard; close throw;
  hit, guard, knockdown and recovery state; vitality, timer and round markers;
  KO, time-over, draw extension, round reset and first-to-two match settlement.
- Excluded: later CPU matches, bonus stages, the four non-playable bosses,
  complete arcade ladder and ending; two-player challenge and tournament set;
  exact frame data, damage tables, dizzy arithmetic and CPU policy; Champion
  Edition, Hyper Fighting/Turbo, Super, Super Turbo, home ports, compilations,
  emulation behaviour, hacks, speed modifications and later-series mechanics.
- Reproducible parameterisation: use the World rev G program identity, factory
  Normal difficulty and ordinary timer; start one-player play and select Ryu;
  accept whichever first CPU opponent the program assigns; use only the
  declared movement, six-button attacks, guard, throw and Ryu command attacks;
  stop immediately after either side's second awarded round. Opponent, exact
  commands, contacts, vitality, time-over and draw branches are run parameters.
- Potential scoped modules: a verified program trace, exact input windows and
  damage, dizzy state, CPU policy, bonus stage, full ladder, two-player entry,
  boss rules and every later edition require separate evidence packets.
- Direct-play status: not conducted. No cabinet, PCB, ROM, MAME execution,
  controller trace, screenshot, video or audio was used. The packet is a
  source-based reconstruction whose executable control checks only the stated
  state relations.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `SF2-001` | The selected target is Capcom's original World Warrior program family, specifically MAME set `sf2` World rev G dated 1991-05-22 | Observation | Corroborated | High | P1, P3, S1 |
| `SF2-002` | World Warrior offers eight selectable fighters and predates the playable bosses and same-character option added by Champion Edition | Confirmed | Direct | High | P1, P2 |
| `SF2-003` | The cabinet uses an eight-way direction control and six attack buttons divided into three punch and three kick strengths | Confirmed | Direct | High | P1, P3 |
| `SF2-004` | Direction, posture and button sequences select normal attacks, throws and character-specific special moves | Observation | Corroborated | High | P1, P2, S2 |
| `SF2-005` | Holding away from the opponent requests standing guard and down-away requests crouching guard against compatible attacks | Observation | Corroborated | Medium | P1, S2 |
| `SF2-006` | Movement and attacks resolve continuously through spacing, collision, hit, guard, damage, knockdown and recovery state | Observation | Corroborated | High | P2, S1, V1 |
| `SF2-007` | Factory difficulty is Normal (`3`) and the cabinet configuration exposes the ordinary one-player continue mode | Confirmed | Direct | High | P3 |
| `SF2-008` | One match is won by the first fighter to record two round wins; KO or the greater remaining vitality at time-over awards an ordinary round | Observation | Corroborated | High | P1, P4, S2 |
| `SF2-009` | A draw does not award the required round and extends the match under the original game's bounded draw policy | Observation | Limited | Medium | S2 |
| `SF2-010` | World Warrior has no ordinary throw escape input; the scoped throw uses only the offensive branch of `ACT-297` | Observation | Corroborated | Medium | S1, S2 |
| `SF2-011` | The local control covers command legality, strike/guard/throw contact, round reset, draw extension and both match terminals without executing the arcade program | Observation | Direct | High | V1 |
| `SF2-012` | No cabinet, PCB, program dump, emulator or audiovisual trace was inspected | Confirmed | Direct | High | R1 |

## Basic data

- Release / origin: Capcom, 1991; original Street Fighter II arcade release.
- Platform or physical form: North American English coin-operated CPS-1 arcade
  cabinet, World rev G program set `sf2`.
- Puzzle family: tactical forecast and counterplay; real-time system pressure.
- Primary and creator sources, accessed 2026-09-21:
  - **[P1]** [Capcom Town's official Street Fighter II
    page](https://captown.capcom.com/en/classic_games/23), for the 1991 product,
    eight fighters, directional control, six attack strengths and original
    move vocabulary. The playable web version is product context, not direct
    evidence that its implementation equals the selected PCB program.
  - **[P2]** [Capcom's Street Fighter 30th Anniversary
    retrospective](https://news.capcomusa.com/lets/browse/street-fighter-30th-anniversary-collection-retrospective-series-street-fighter-street-fighter-ii),
    for the eight-fighter World Warrior boundary, special moves and combos,
    and the later Champion Edition/Hyper Fighting changes excluded here.
  - **[P3]** [Capcom USA Street Fighter II kit instruction
    manual](https://www.arcade-museum.com/manuals-videogames/S/SFII.pdf), for
    CPS installation, six-button wiring, difficulty `3 = Normal`, factory
    settings and continue configuration. Local PDF SHA-256:
    `24265d01aeb31ffb54004b3f0f4fba3c6a035ca5d19678f92368254d2adf92d9`.
  - **[P4]** [Capcom Fighters Network's official series-rule
    explanation](https://game.capcom.com/cfn/sfv/column/130281), for the
    first-to-two round convention and draw-extension concept. It is series
    corroboration; World Warrior-specific draw limits rest on S2.
- Reproducible technical and secondary sources, accessed 2026-09-21:
  - **[S1]** [ROM Archaeology's `sf2` lineage
    inventory](https://github.com/ROMArchaeology/sf2-lineage/blob/main/README.md)
    and [engine notes](https://github.com/ROMArchaeology/sf2-lineage/blob/main/engine/ENGINE.md),
    for the exact World rev G program identity/build date and code-informed
    combat-state reconstruction. The repository identifies program CRC32
    `43fcc23e`; this unit did not obtain or execute that program.
  - **[S2]** [Tyler Oswald's World Warrior FAQ at
    GameFAQs](https://gamefaqs.gamespot.com/arcade/583626-street-fighter-ii-the-world-warrior/faqs/844),
    for original move inputs, guard, throws, round settlement and draw
    behaviour. It is a secondary written reconstruction, not direct play.
- Reproducible control: **[V1]**
  [`verify_street_fighter_ii_world_warrior_control.py`](../../../scripts/verify_street_fighter_ii_world_warrior_control.py),
  an executable source-model control for the bounded transitions.
- Research record: **[R1]** local preflight found no cabinet, PCB, ROM, MAME
  session, save, input trace, screenshot, video or audio.
- Claim IDs: `SF2-001`–`SF2-012`.

## Mechanical decomposition

### Action Genes

- `ACT-294` owns selecting Ryu for the human side before the match. World
  Warrior exposes no modern control-type choice, so the original six-button
  layout is a fixed parameter.
- `ACT-008` owns walking, crouching and jumping through the bounded fight plane.
- `ACT-295` owns one legal normal or special attack entered through direction,
  posture and punch/kick strength. It does not own resulting contact.
- `ACT-296` owns holding or releasing opponent-relative standing/crouching
  guard.
- `ACT-297` owns the close offensive throw. Its throw-escape branch is absent
  from this ruleset and is explicitly not inferred.
- Claims: `SF2-002`–`SF2-006`, `SF2-010`.

### System Behaviour Genes

- `SYS-215` resolves body, strike, projectile, throw and guard contact through
  current spacing, attack/recovery state, damage, knockdown and defeat.
- `SYS-522` awards or extends a round, resets eligible fighter state, records
  round markers and settles the match when one side reaches two wins.
- Claims: `SF2-006`, `SF2-008`, `SF2-009`.

### Constraint Genes

- `CON-442` gates movement, guard, throw and attack commands by fighter,
  facing, posture, recovery and the exact input sequence.
- `CON-443` bounds both bodies to one side-view stage whose corners, push
  contact and airborne crossover change spacing and facing without ring-out.
- `CON-446` binds every round to vitality and timer terminals and the complete
  match to two awarded rounds.
- Claims: `SF2-004`–`SF2-009`.

### Information Genes

- `INF-142` owns visible pose, animation, impact and sound cues for attacks,
  blocks, knockdowns and recovery; no exact reaction threshold is claimed.
- `INF-209` exposes the fighters' relative pose, spacing and current
  hit/guard/knockdown state in the side-view arena.
- `INF-210` exposes paired vitality, shared round timer and round-win markers.
  Its resource parameter is empty because World Warrior has no Drive, Heat or
  Super meter.
- Claims: `SF2-005`, `SF2-006`, `SF2-008`.

### Objective Genes

- `OBJ-099` requires two awarded round wins against the one fixed CPU opponent
  before that opponent reaches the same threshold.
- Claims: `SF2-008`, `SF2-009`.

### Time Genes

- `TIM-003` owns simultaneous real-time movement, attacks, projectiles,
  recovery states and the active round clock.
- Claims: `SF2-006`, `SF2-008`.

## Reproducible transitions

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| One-player character selection is open | Select Ryu | Ryu is assigned to the human side and the first CPU opponent/stage is fixed for this match | bounded fighter assignment | `SF2-002` |
| Both fighters are actionable at neutral distance | Walk, crouch or jump | Position, facing and legal body spacing update continuously inside stage bounds | direct side-view spacing | `SF2-006` |
| Ryu is actionable at suitable range | Enter a legal Hadoken direction-and-punch command | Ryu enters the command attack and its projectile resolves through contact or non-contact state | command sequence selects an attack | `SF2-004`, `SF2-006` |
| A compatible strike approaches from the front | Hold away or down-away | Legal contact resolves as standing or crouching guard instead of an ordinary hit | opponent-relative guard | `SF2-005` |
| The opponent is throwable at close range | Enter the ordinary throw input | The offensive throw resolves if range and state permit; no throw-escape response is available | original throw boundary | `SF2-010` |
| The CPU fighter's vitality reaches zero | Complete the current contact | Ryu receives one round marker and the next round resets vitality and positions | KO-to-round reset | `SF2-008` |
| Time expires with unequal vitality | Allow the timer to reach zero | The fighter with greater remaining vitality receives the round marker | time-over adjudication | `SF2-008` |
| A round resolves as a draw | Complete the tied terminal | Neither side reaches the next required win; the match continues under the bounded draw policy | draw extension | `SF2-009` |
| Ryu already has one round win | Win another awarded round | The second marker settles victory and advances the arcade route | positive match terminal | `SF2-008` |
| The CPU already has one round win | Lose another awarded round | The second CPU marker settles defeat and exposes the continue decision | negative match terminal | `SF2-008` |

## Strategic and experiential structure

- Local decision: judge range, facing and recovery, then choose movement,
  guard, throw or a strength/motion-specific attack.
- Medium-term planning: use light attacks for lower commitment, heavier attacks
  for reach/damage opportunities, preserve corner escape routes and vary guard,
  throw and projectile timing.
- Long-term structure: convert repeated neutral, pressure and knockdown states
  into two round wins while each new round restores the ordinary fight state.
- Common heuristics: anti-air a visible jump; block before challenging an
  uncertain sequence; throw a passive close defender; use a projectile only
  when its start-up and distance are credible; avoid a heavy whiff near reach.
- Failure attribution: a visible command, spacing or guard error can explain
  many losses, but CPU choice and exact frame/damage arithmetic are deliberately
  not asserted by this source-bounded packet.
- Player-trust factors: paired vitality, timer, round markers, stable facing,
  distinct poses and contact feedback make every match terminal inspectable.
- Claims: `SF2-004`–`SF2-010`.

## Replay and variation

- What changes: CPU opponent, stage, attack/defence sequence, spacing, timer,
  remaining vitality, draw branch and match winner.
- Randomness or procedural generation: no generated arena enters scope; the
  first CPU opponent/order may vary by program policy, which remains a run
  parameter rather than an inferred gene.
- Multiple viable strategies: projectile spacing, grounded normals, jump
  attacks, guard-and-punish and close throw pressure can each win rounds.
- Typical replay motive: improve command reliability, spacing, defence and
  opponent-specific timing or continue the arcade ladder.
- Claims: `SF2-004`–`SF2-009`.

## Adjacent systems and history

- Direct predecessor: the original Street Fighter established motion-command
  special attacks but is not imported as evidence for this program.
- Variants: Champion Edition adds playable bosses and same-character matches;
  Hyper Fighting changes speed and moves; Super/Super Turbo expand roster and
  systems. None modifies this World Warrior packet.
- Similar games: Street Fighter 6 shares the side-view spacing, command attack,
  guard, throw, HUD and first-to-two structure; TEKKEN 8 adds lateral stepping,
  modern resource states and first-to-three settlement; Brawlhalla replaces
  vitality depletion with damage-scaled launch and stocks.
- Important difference: this packet has no Drive, Super/Heat resource, throw
  escape, ring-out or persistent progression—only the original six-button
  fighter state, vitality, timer and round score.
- Claims: `SF2-001`, `SF2-002`, `SF2-008`, `SF2-010`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-294`–`ACT-297` | fighter selection, movement, attack, guard and offensive throw |
| System Behaviour | `SYS-215`, `SYS-522` | live contact plus round/match adjudication |
| Constraint | `CON-442`, `CON-443`, `CON-446` | command state, stage spacing, vitality, timer and round wins |
| Information | `INF-142`, `INF-209`, `INF-210` | cues, spacing/combat state and duel HUD |
| Objective | `OBJ-099` | first to two awarded rounds |
| Time | `TIM-003` | simultaneous real-time duel |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `350` (`GAME-0001`–`GAME-0350`).
- Exact genome matches: none.
- Tied near matches: `GAME-0172` — Street Fighter 6 (`15 / 20 = 0.750000`).
- Supported combination subsets: none.
- Scan date: 2026-09-21.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| Street Fighter 6 (`GAME-0172`) | `ACT-008`, `ACT-294`–`ACT-297`, `SYS-215`, `SYS-522`, `CON-442`, `CON-443`, `CON-446`, `INF-142`, `INF-209`, `INF-210`, `OBJ-099`, `TIM-003` | Both are fixed side-view, six-button, first-to-two duels. Street Fighter 6 additionally gives each fighter Drive and tiered Super resources, Drive techniques, Burnout and resource gates; World Warrior keeps only the foundational spacing, commands, guard, throw, vitality, timer and round state and offers no throw escape. | Near, `0.750000` |

## Taxonomy impact

- Registry changes: none. All fifteen boundaries are exact reuse; World
  Warrior adds support without revising their definitions.
- Taxonomy-change record: none.
- Candidate terms affected: World Warrior motion command, six attack strengths,
  offensive-only throw, draw extension and meterless duel HUD are parameters or
  negative boundaries, not new genes.

## Negative results

- No new motion-input gene is created: direction, posture, button and strength
  already parameterise `ACT-295`, while command legality remains `CON-442`.
- No throw-escape mechanic is inferred. `ACT-297` is reused only for its
  offensive throw branch; World Warrior provides no matching escape response.
- `SYS-520`, `SYS-521`, `CON-444` and `CON-445` are rejected because this
  original edition has no Drive or Super stock.
- `ACT-298` is rejected because Drive techniques belong to Street Fighter 6.
- Exact frame data, damage, dizzy, CPU policy and a maximum-draw loss rule stay
  outside the signature because admitted evidence is insufficient.

## Delta summary

## New facts

- [Confirmed | Direct | High] The original 1991 World Warrior boundary offers
  eight fighters with an eight-way direction input and six attack buttons.
- [Observation | Corroborated | High] One compact match joins motion-command
  attacks, guard, contact, vitality, time and first-to-two round settlement.

## New genes

- None. Fifteen established Active genes cover the complete scoped ruleset.

## New combinations

- None. No verified combination is a proper subset of the signature.

## Taxonomy changes

- None. This unit adds support without changing any prior definition or game
  signature.

## New questions

- Can a later original fighting game support the same round core while adding
  a causally distinct meter, tag partner, ring-out or weapon boundary?

## Next recommended game

- Not reserved by this unit. Selection 024 closes at `GAME-0351`; a new
  reviewed selection decision must allocate `GAME-0352` onward.
