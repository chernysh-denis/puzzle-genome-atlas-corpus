---
game_id: GAME-0338
slug: final-fantasy-vii
game_title: Final Fantasy VII
analysis_status: reviewed
reviewed: 2026-09-21
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-019
    - ACT-131
    - ACT-341
  system:
    - SYS-299
    - SYS-362
    - SYS-381
    - SYS-453
    - SYS-854
    - SYS-954
  constraint:
    - CON-068
    - CON-175
    - CON-269
    - CON-282
  information:
    - INF-119
    - INF-179
  objective:
    - OBJ-199
  time:
    - TIM-026
---

# Game: Final Fantasy VII

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Cloud, Barret,
Jessie, AVALANCHE, Shinra, Midgar, Reactor No. 1, Guard Scorpion, Bolt,
Lightning Materia, Limit Break and Sector 8 are carrier parameters, not gene
names.

## Analysis scope

- Version / ruleset: the original North American English PlayStation Disc 1,
  serial `SCUS-94163`. It is not the Japanese or PAL release, PC port, mobile,
  PS4/Switch/Xbox wrapper, Final Fantasy VII Remake, a mod, translation patch,
  randomiser, speedrun exploit or emulator-enhanced ruleset.
- Structured analysis target: original licensed PlayStation field, kernel and
  battle data represented by the official manual and by extraction tooling
  pinned at commit `6bf1fbcec2c88c1856cffd4a371719b406fee654`; see
  `GAME-0338` in
  [`knowledge/platforms/games.json`](../../platforms/games.json).
- Scenario: one fresh New Game, from first ordinary control of Cloud after the
  opening train arrival through the complete Reactor No. 1 bombing mission.
- Entry: Cloud stands on the Sector 1 station platform after the authored train
  arrival, before the first required guard battle. The fresh save supplies his
  authored starting level, equipment, inventory and equipped Lightning Materia;
  no grinding, prior save or configuration exploit is imported.
- Fixed reproducible route: clear the first scripted MP encounter; take the
  authored route through doors, elevator, ladders and catwalks; join Barret;
  reach the reactor core and commit the bomb interaction; defeat Guard
  Scorpion; retrace the route under the displayed ten-minute countdown; release
  Jessie from her trapped state; use Jessie and Biggs to reopen the two return
  doors; cross the reactor exit before zero; accept the explosion sequence; and
  stop when ordinary Cloud control first resumes on the Sector 8 street before
  the flower-seller interaction.
- Primary decision loop: traverse one authored field screen toward its visible
  exit or interaction; if an encounter starts, wait for a party member's ATB
  Time gauge, choose an available Attack, Magic, Item, Defend or Limit command
  and legal target, let the queued action and enemy readiness resolve, then
  preserve party HP/MP and continue the field route. After Guard Scorpion,
  route choice is additionally constrained by the evacuation countdown.
- Positive terminal: the device is armed, Guard Scorpion is defeated, Jessie
  and both return doors are resolved, the party exits before timer expiry, the
  reactor explodes and ordinary Cloud control resumes in Sector 8. The flower-
  seller conversation and everything after it are outside the packet.
- Failure paths: all active party members becoming critically injured or
  petrified produces Game Over; failing to complete the authored evacuation
  before the countdown reaches zero also terminates the attempt. Save/reload,
  Continue and memory-card consequences are not exercised.
- Included: direct field movement and running; visible current-screen exits and
  interactables; authored doors, elevator, ladders, bomb and Jessie state;
  scripted and locally sampled encounters; ATB readiness; party command and
  target choice; basic attacks, Bolt, finite recovery items, HP, MP, Time and
  Limit gauges; equipped Lightning Materia supplying Magic/Bolt; Guard
  Scorpion's Lightning affinity and tail-counter state; battle EXP, AP, gil and
  the Assault Gun drop; the ten-minute evacuation and ordered route flags.
- Reproducible parameterisation: use a fresh original-US `SCUS-94163` New Game
  and the ordinary opening route. Field movement timing, eligible random
  encounters, damage rolls, target order, recovery-item use, Limit readiness,
  remaining HP/MP and countdown margin may vary. The scripted opening battle,
  reactor topology, bomb interaction, Guard Scorpion, Jessie gate, two doors,
  countdown, exit and Sector 8 terminal do not.
- Excluded: optional grinding or repeated encounter farming; opening-guard
  Potion searches, optional chest and Restore Materia pickup as requirements;
  changing Battle Mode or speed from their fresh configuration; manual Materia
  or equipment rearrangement; save-point use; flower purchase; train return,
  Sector 7, Reactor No. 5 and all later story, party, equipment, Materia growth,
  summons, shops, world map, minigames, optional characters, endings and discs
  2–3; later ports, boosts, encounter toggles, cheats, glitches and mods.
- Direct-play status: not conducted. No original disc, PlayStation console,
  disc image, emulator, save, controller trace, screenshot, video or audio was
  used. This is a source-bounded reconstruction, not a claimed playthrough or
  inspection of copyrighted game data.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `FF7-001` | The packet targets the North American original PlayStation Disc 1 `SCUS-94163`, not a later port or remake | Confirmed | Corroborated | High | P1, P2, R1 |
| `FF7-002` | Field controls permit direct movement, running, actor/object interaction, ladders, switches and an optional current-position/exit pointer | Confirmed | Direct | High | P1 |
| `FF7-003` | In ATB, ally and enemy Time gauges advance independently and the first ready actor receives command priority | Confirmed | Direct | High | P1 |
| `FF7-004` | Equipped Magic Materia exposes the Magic command and its spell; insufficient MP makes the spell unavailable | Confirmed | Direct | High | P1 |
| `FF7-005` | Enemy damage fills a persistent character-local Limit gauge; full readiness replaces the ordinary attack command and an unused Limit carries into the next battle | Confirmed | Direct | High | P1 |
| `FF7-006` | Cloud begins the mission with Lightning Materia supplying Bolt, and Guard Scorpion is weak to Lightning | Observation | Corroborated | High | S1, S2 |
| `FF7-007` | Winning a battle may award EXP, AP, gil and items; EXP drives character levels and AP is assigned to Materia growth | Confirmed | Direct | High | P1 |
| `FF7-008` | Eligible field movement accumulates encounter danger and samples one weighted local battle formation | Observation | Corroborated | High | R2, S3 |
| `FF7-009` | Guard Scorpion is the mandatory core security encounter; its defeat starts the visible ten-minute return deadline | Observation | Corroborated | High | S1, S2 |
| `FF7-010` | Jessie must be released and the two authored return doors reopened before the reactor exit can settle | Observation | Corroborated | High | S1, R1 |
| `FF7-011` | Exiting on time closes the bombing mission through the explosion and restores ordinary Cloud control in Sector 8 | Observation | Corroborated | High | P2, S1 |
| `FF7-012` | The complete signature admits only systems causally available between the fresh train-platform entry and the first Sector 8 control state | Observation | Corroborated | High | P1, P2, R1, R2, S1–S3, V1 |

## Basic data

- Release / origin: Square / Sony Computer Entertainment America; original
  PlayStation role-playing game released in 1997. PlayStation's official
  history identifies Final Fantasy VII as the series' 1997 PlayStation debut.
- Platform or physical form: North American original PlayStation three-disc
  release; the scoped data and opening FMV are on Disc 1 `SCUS-94163`.
- Puzzle family: tactical forecast and counterplay; real-time system pressure;
  inventory and fixture dependencies; ordered dependency sequencing.
- Primary sources, accessed 2026-09-21:
  - **[P1]** [Sony Computer Entertainment's original English PlayStation
    manual](https://secure.cdn.us.playstation.com/manuals/classic/games/final-fantasy-vii-manual-en.pdf),
    pp. 6–10 and 13–21, for field controls, exit pointers, ATB, commands,
    HP/MP/Time/Limit gauges, Materia-derived commands, items, battle rewards
    and Game Over.
  - **[P2]** [PlayStation history: Final Fantasy VII](https://www.playstation.com/en-us/playstation-history/1994-ps-one/),
    for original 1997 PlayStation identity; and the official
    [PlayStation Final Fantasy guide](https://www.playstation.com/en-us/final-fantasy/),
    which distinguishes the original from later Remake combat.
- Reproducible sources:
  - **[R1]** [`cebix/ff7tools` at commit
    `6bf1fbce`](https://github.com/cebix/ff7tools/tree/6bf1fbcec2c88c1856cffd4a371719b406fee654),
    whose README explicitly supports the US PlayStation release `SCUS-94163`
    and documents deterministic extraction of field text/scripts and
    `SCENE.BIN` battle records. No disc image was supplied to or executed by
    this review.
  - **[R2]** [Qhimm/Final Fantasy Inside field encounter structure](https://wiki.ffrtt.ru/index.php/FF7/Field/Encounter),
    for each field's enabled encounter table, rate and weighted standard or
    special formation slots.
- Corroborating sources:
  - **[S1]** [GameFAQs original-PSX guide, Reactor No. 1](https://gamefaqs.gamespot.com/ps/197341-final-fantasy-vii/faqs/71240?single=1),
    for starting Lightning/Bolt, Guard Scorpion's affinity and counter state,
    the ten-minute timer, Jessie gate, return route and reward values.
  - **[S2]** [Gamer Guides original Final Fantasy VII Reactor No. 1 route](https://www.gamerguides.com/final-fantasy-vii/guide/walkthrough-disc-1/midgar/no-1-reactor),
    independently corroborating the first encounters, Bolt, Guard Scorpion and
    timed retrace.
  - **[S3]** [Terence's original PlayStation enemy-mechanics FAQ](https://gamefaqs.gamespot.com/ps/197341-final-fantasy-vii/faqs/31903),
    for movement-driven field danger, encounter checks and local formation
    sampling, read together with R2 rather than treated as developer source.
- Validation source:
  - **[V1]** repository-side transition reconstruction from P1–P2, R1–R2 and
    S1–S3; source and rules reasoning only, with no direct play or audiovisual
    claim.
- Claim IDs: `FF7-001`–`FF7-012`.

## Mechanical decomposition

### Action Genes

- `ACT-008`: directly walk or run Cloud through one pre-rendered field's
  traversable geometry toward its next exit, ladder or fixture.
- `ACT-019`: when a party member's Time gauge is ready, choose one available
  Attack, Magic, Defend or Limit ability and its legal ally or enemy target.
- `ACT-131`: select one carried Potion or other currently available immediate-
  effect battle item, choose its legal target and spend one unit on resolution.
- Generalised `ACT-341`: operate doors, the elevator, ladders and bomb fixture,
  and interact with trapped Jessie to change actor and return-route state.
- Claims: `FF7-002`, `FF7-003`, `FF7-006`, `FF7-009`, `FF7-010`.

### System Behaviour Genes

- `SYS-299`: awarded EXP crosses character-specific thresholds and updates
  level and derived character statistics.
- `SYS-362`: victory settles eligible EXP, AP, gil and item drops before the
  party returns to field traversal.
- Generalised `SYS-381`: enemy damage fills the damaged character's Limit
  gauge; full readiness replaces the ordinary attack command until used and may
  carry across the next battle.
- Generalised `SYS-453`: equipped Lightning Materia contributes the Magic
  command and Bolt to Cloud's battle vocabulary and receives eligible AP.
- Generalised `SYS-854`: a committed physical or magical command resolves
  typed damage against target affinity, with Bolt receiving Guard Scorpion's
  Lightning modifier before HP and defeat state update.
- Generalised `SYS-954`: eligible field movement advances local encounter
  checks and samples one weighted formation from the active field table.
- Resolution order: field movement reaches an authored or sampled encounter;
  ATB schedules ready actors; committed commands resolve damage, recovery or
  defence; finite hostile clearance settles rewards and returns to the field;
  bomb state triggers Guard Scorpion; its defeat starts the countdown; return-
  route interactions and exit settle the explosion and Sector 8 transition.
- Claims: `FF7-003`–`FF7-010`.

### Constraint Genes

- `CON-068`: after Guard Scorpion, the displayed ten-minute allowance is the
  authoritative terminal deadline for the return route.
- Generalised `CON-175`: party HP remains depleted between encounters unless
  explicitly restored; total party critical injury or petrification causes
  Game Over.
- `CON-269`: Magic and item commands require a ready actor, legal target,
  equipped command source, sufficient MP or stock and an eligible state.
- `CON-282`: train-platform battle, doors, elevator, bomb, Guard Scorpion,
  Jessie release, two return doors, reactor exit and Sector 8 control are an
  ordered authored chain.
- Scarce route state: party HP/MP, item stock, actor readiness, Limit readiness,
  encounter flags, bomb/boss state, Jessie state, return-door flags and
  remaining evacuation time.
- Claims: `FF7-004`, `FF7-005`, `FF7-009`–`FF7-011`.

### Information Genes

- `INF-119`: the battle status window exposes current/max HP, MP, Time and
  Limit readiness, while available commands and disabled magic communicate the
  currently usable party build.
- Generalised `INF-179`: the current field exposes Cloud, nearby actors,
  fixtures, ladders and pickups; the optional pointer identifies his position
  and possible exits without revealing the complete future route.
- Claims: `FF7-002`–`FF7-005`.

### Objective Genes

- New `OBJ-199`: plant the Reactor No. 1 bomb, clear Guard Scorpion, resolve
  Jessie and both return doors, then exit before detonation so ordinary control
  resumes in Sector 8.
- Success, evaluation and failure: bomb placement or boss defeat alone is not
  terminal. The authored return predicates and exit must settle before zero;
  total party defeat or countdown expiry is failure.
- Claims: `FF7-009`–`FF7-011`.

### Time Genes

- New `TIM-026`: each eligible ally and enemy has independently advancing ATB
  readiness; a ready party actor accepts one command while other readiness and
  queued effects follow the active battle clock and its pause policy.
- Claims: `FF7-003`.

## Reproducible transitions

| Before | Action | Deterministic or bounded resolution | Establishes | Claim |
|---|---|---|---|---|
| Fresh `SCUS-94163` opening has returned control on the train platform | move into the two MPs and commit ready commands | the scripted formation enters battle; actor-local Time gauges produce command windows until the finite hostile set is defeated | first ATB battle and field/battle transition | `FF7-001`, `FF7-003` |
| Cloud's Time gauge is full and Lightning Materia is equipped | choose Magic, Bolt and Guard Scorpion | MP is checked and spent; Lightning affinity modifies damage before the target's HP is reduced | equipment-derived typed command | `FF7-004`, `FF7-006` |
| One party member receives eligible enemy damage | wait for the personal Limit gauge to fill | full readiness changes the ordinary attack command to Limit; use consumes it, while an unused full gauge survives battle closure | retained special readiness | `FF7-005` |
| A required encounter's hostile set reaches defeat | accept battle settlement | eligible EXP, AP, gil and item rewards are granted; threshold crossing updates level and equipped Materia receives AP before field return | bounded reward and progression | `FF7-007` |
| An encounter-enabled field is traversed | continue walking or running | movement checks advance danger; a bounded random test may choose one weighted local formation and transfer the party to battle | hidden local encounter sampling | `FF7-008` |
| Reactor core bomb fixture is reachable | confirm the contextual interaction | bomb state is armed and the authored Guard Scorpion security battle begins | sabotage midpoint, not completion | `FF7-009` |
| Guard Scorpion is active | sequence ready commands, target choices and recovery while respecting its counter state | typed damage reduces its HP to defeat, rewards settle and the visible ten-minute evacuation begins | mandatory response and deadline | `FF7-006`, `FF7-009` |
| Countdown remains and Jessie is trapped on the return path | reach and interact with Jessie | her trapped state clears, allowing the later authored door sequence to proceed | required actor gate | `FF7-010` |
| Jessie and Biggs are ready at the two closed return doors | interact in authored order | each door flag opens its edge and the exit becomes reachable while the timer continues | ordered return-route gates | `FF7-010` |
| Exit is reachable before zero and all required route flags hold | cross the reactor exit | the escape closes, the explosion sequence resolves and ordinary Cloud control first resumes in Sector 8 | scoped positive terminal | `FF7-011` |

## Strategic and experiential structure

- Local decision: choose field pace and route interaction; when ATB readiness
  arrives, choose which ready party member acts, whether to attack, cast Bolt,
  defend, heal or spend a Limit, and which legal target receives the command.
- Medium-term planning: preserve HP, MP and item stock across several field-
  separated battles; exploit known Lightning affinity; avoid Guard Scorpion's
  counter state; then trade optional encounters and menu time against the
  authoritative evacuation margin.
- Long-term structure: the packet teaches a repeated field/command-battle
  rhythm, demonstrates that equipped Materia changes command vocabulary and
  rewards, then converts the same authored route into a timed reverse traversal
  whose actor and door gates must all be restored before detonation.
- Common heuristics: inspect exit pointers on complex fields; let ready actors
  wait rather than committing a poor counter-state attack; use Bolt against the
  mechanical boss; heal before party-wide terminal risk; retrace immediately,
  release Jessie and do not treat the boss victory as mission completion.
- Failure attribution: HP/MP, Time/Limit gauges, disabled command text, damage
  numbers, boss form, countdown, trapped-actor response and door state separate
  resource failure, readiness timing, wrong affinity, counterattack, missed
  route gate and missed deadline. Encounter sampling remains bounded
  uncertainty rather than an authored route change.
- Claims: `FF7-002`–`FF7-012`.

## Replay and variation

- What changes between attempts: sampled encounters and formations, damage,
  target order, ATB timing, item use, Limit availability, EXP/AP totals,
  remaining party resources and evacuation margin.
- Randomness or procedural generation: field geometry, fixed battles, boss,
  gates and successor state are authored; encounter initiation/formations and
  combat damage contain bounded randomness.
- Multiple viable strategies: ordinary attacks, Bolt, items, Defend, Limit and
  battle escape can produce different resource/time profiles. This packet
  requires only an ordinary successful route, not speedrun optimisation.
- Typical replay motive: faster mission time, fewer encounters, lower resource
  loss, challenge constraints or broader campaign progression. Those later
  goals do not change the accepted early mission boundary.
- Claims: `FF7-003`–`FF7-012`.

## Adjacent systems and history

- Direct predecessors: earlier Final Fantasy titles established party command
  combat and ATB; Final Fantasy VII binds that readiness schedule to equipped
  Materia, individual Limit carryover and pre-rendered 3D field traversal.
- Variants: PAL/Japanese revisions, PC and modern ports, built-in boosts and
  encounter toggles, Final Fantasy VII Remake and mods require independent
  version evidence and do not inherit this exact signature.
- Similar games: Persona 5 Royal and Pokémon Red Version share party-command
  selection, typed affinity, persistent resources and encounter settlement.
- Important difference: Pokémon Red resolves strict paired turns and Persona 5
  exposes weakness-driven follow-up actions; Final Fantasy VII independently
  fills each actor's Time gauge and lets readiness order emerge continuously.

## Normalised genome

The front matter is canonical. The complete signature contains 18 Active
genes: four Action, six System Behaviour, four Constraint, two Information,
one Objective and one Time gene. Character, field, boss, item, spell, timer and
numeric reward labels remain carrier parameters.

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `337` (`GAME-0001`–`GAME-0337`).
- Exact genome matches: none.
- Tied near matches: `GAME-0291` — Persona 5 Royal (`8 / 29 = 0.275862`).
- Supported combination subsets: none.
- Scan date: 2026-09-21.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0291` — Persona 5 Royal | `ACT-008`, `ACT-019`, `ACT-341`, `SYS-362`, `SYS-854`, `CON-269`, `CON-282`, `INF-119` | Both packets move through authored fields, commit actor-targeted commands, resolve typed affinities, settle battle rewards and pass ordered interaction gates. Persona 5 Royal uses strict menu turns, weakness-driven `Down` and extra actions, calendar phases and a first Safe Room terminal. Final Fantasy VII instead races concurrent ATB gauges, derives Magic from Materia, carries Limit readiness and party HP between sampled encounters, then closes on a bomb-triggered boss and timed reverse evacuation. | Near, `8 / 29 = 0.275862` |

## Taxonomy impact

`OBJ-199` and `TIM-026` are new. `TAXONOMY_CHANGE_081` generalises
`ACT-341`, `SYS-381`, `SYS-453`, `SYS-854`, `SYS-954`, `CON-175` and
`INF-179` so authored actors/fixtures, harm-earned readiness, embedded ability
components, command-combat affinity, field-danger encounters, persistent party
health and field-level decision information reuse stable causal boundaries.
Stable support is added to `ACT-008`, `ACT-019`, `ACT-131`, `SYS-299`,
`SYS-362`, `CON-068`, `CON-269`, `CON-282` and `INF-119` without changing
their definitions. No earlier signature changes.

## Negative results

- No verified combination is registered from one new carrier.
- No direct play, disc possession or extraction, emulation, audiovisual
  observation, save, controller trace or installed-build parity test is
  claimed.
- The ff7tools repository is cited as reproducible tooling and format evidence;
  no copyrighted game data was supplied to or executed by this review.
- Conflicting secondary descriptions of countdown pause behaviour are not
  resolved into a claim; only the visible ten-minute evacuation boundary is
  admitted.
- `TIM-026` is the ATB readiness schedule, not Limit readiness, the mission
  countdown or a conventional alternating turn order.
- `OBJ-199` requires the bomb, mandatory security response, authored return
  gates and successful exit; boss defeat alone is not the terminal.
- Later Materia arrangement, equipment progression, linked effects, world-map
  systems and story outcomes are outside this opening packet.

## Delta summary

## New facts

- [Confirmed | Direct | High] Sony's manual establishes independently filling
  actor Time gauges, equipment-derived Magic, resource gates, retained Limit
  readiness, battle settlement and party-wide Game Over.
- [Observation | Corroborated | High] The bounded Reactor No. 1 route joins a
  mandatory device, Lightning-sensitive security response, visible ten-minute
  deadline, trapped-actor gate, two return doors and a Sector 8 terminal.

## New genes

- [Observation | Corroborated | High] `OBJ-199` isolates a complete mission in
  which a device is armed, its required response is cleared and every authored
  evacuation gate settles before detonation.
- [Confirmed | Direct | High] `TIM-026` isolates concurrent actor-local
  readiness before command commitment under an active battle clock.

## New combinations

- [Observation | Corroborated | High] None; recurrence remains
  evidence-driven.

## Taxonomy changes

- [Confirmed | Corroborated | High] `TAXONOMY_CHANGE_081` generalises seven
  stable carrier wordings without changing their causal tests or any earlier
  signature.

## New questions

- Which later bounded game independently combines concurrent actor-local
  readiness with an authored reverse-evacuation terminal?
- Can a lawful owner-supplied Disc 1 extraction settle the exact countdown
  pause policy without expanding this route or changing its signature?

## Next recommended game

- `GAME-0339` Metal Gear Solid, as reserved by selection 023.

## Why this game

- Final Fantasy VII is a recognisable PlayStation anchor whose first mission
  demonstrates in one bounded packet how field traversal, equipment-derived
  commands, concurrent readiness, persistent party resources and a timed
  authored evacuation depend on one another.

## Combination opportunities

- No verified combination is a proper subset of this complete signature.
- The ATB readiness clock and timed sabotage return are newly isolated genes,
  not evidence that an existing multi-gene combination should be rewritten.

## Exclusions and assumptions

- The evidence packet reconstructs the original US mission but does not execute
  the disc. No claim depends on a frame count, exact random seed, exact damage
  roll or exact timer pause behaviour not established by the cited sources.
- Optional loot, Restore Materia, save-point use, equipment swapping and random
  encounter grinding are excluded from the required route even when the
  commercial game permits them.
- Starting Lightning Materia and Guard Scorpion affinity are corroborated
  observations, not elevated to developer-source facts.
- The terminal deliberately stops before the flower-seller interaction so no
  dialogue branch, purchase, later pursuit or train state leaks into the unit.

## Open questions

- A lawful direct run or owner-supplied original Disc 1 extraction could later
  confirm exact field-script flags, timer pause policy and encounter tables.
  Until then, no stronger direct-play or exact-data claim is made.
- Later Materia configuration, linked Materia, weapon/armour growth and the
  complete Limit-learning system require a separate broader progression unit.
