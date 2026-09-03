---
game_id: GAME-0218
slug: counter-strike
game_title: Counter-Strike
analysis_status: reviewed
reviewed: 2026-09-01
combination_ids:
  - COMB-0216
gene_ids:
  action:
    - ACT-008
    - ACT-130
    - ACT-161
    - ACT-164
    - ACT-183
    - ACT-184
    - ACT-185
    - ACT-186
    - ACT-187
  system:
    - SYS-208
    - SYS-215
    - SYS-222
    - SYS-292
    - SYS-293
    - SYS-294
    - SYS-295
  constraint:
    - CON-261
    - CON-262
    - CON-263
    - CON-264
    - CON-265
    - CON-266
  information:
    - INF-073
    - INF-115
    - INF-116
    - INF-117
  objective:
    - OBJ-135
  time:
    - TIM-003
---

# Game: Counter-Strike

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Parameters describe
gene instances but do not enter the signature.

## Analysis scope

- Version / ruleset: current unmodified English Counter-Strike for Windows,
  Steam app `10`, version `1.6`, public client build `12934623`, checked
  `2026-09-01`; official Half-Life Dedicated Server package, Steam app `90`,
  current package build `15961496`; one newly started human-only Bomb/Defuse
  session on built-in `de_dust2` using the shipped dedicated `server.cfg`.
- Primary decision loop: read local sight and sound, radar, team cues, money,
  equipment, C4 and round/map clocks; buy within the opening gate; move, aim,
  fire, reload, throw utility, transfer or collect equipment and coordinate a
  route; Terrorists deliver and plant C4 at either site while Counter-
  Terrorists deny, retake or defuse; settle the round, carry its economy and
  repeat until the shipped 20-minute map limit cycles the session.
- Entry and exit: start the official dedicated server directly on `de_dust2`
  with its unmodified shipped configuration, connect at least one human Steam
  app `10` client to each team and begin from the first ordinary round spawn.
  The packet ends when `mp_timelimit 20` performs the documented map-cycle
  boundary; the final visible Terrorist and Counter-Terrorist round scores
  classify the bounded session as a team lead or tie. A personal kill total is
  never the terminal.
- Included: direct first-person movement; firearm and knife attacks; active-
  item selection and reload; grenades; finite health, armour, ammunition and
  inventory; one life per round; buy time, `$800` starting money and cross-
  round economy; dropped weapon/C4 transfer; partial sight, spatial sound,
  radar, HUD and live team cues; two bomb sites; plant, defuse, explosion,
  elimination and unplanted timeout; team-round score; the stock 20-minute
  map-cycle settlement.
- Excluded: Counter-Strike 2, Counter-Strike: Source, Condition Zero and
  Deleted Scenes; hostage, assassination and escape maps; other maps and the
  rest of `mapcycle.txt`; bots, because Valve requires third-party bots for
  GoldSource Counter-Strike; third-party or community servers, plugins, mods,
  custom maps and custom configuration; an invented 5v5 tournament format,
  round cap, halftime side swap, MR12, overtime or win limit; matchmaking,
  VAC efficacy, cosmetics, statistics and the product's complete history.
- Reproducible parameterisation: current public Steam app `10` clients and
  official app `90` dedicated server; `-game cstrike +map de_dust2`; shipped
  `server.cfg` with `sv_aim 0`, `pausable 0`, `sv_maxspeed 320`,
  `mp_timelimit 20` and `sv_cheats 0`; no added cvar, plugin, bot or map. Human
  roster size and round outcomes may vary, but both sides must remain human-
  occupied and the same stock map/configuration and map-cycle terminal apply.
- Potential scoped modules: one hostage map, a fixed LAN roster, a declared
  community competitive configuration, another stock map or a legacy beta
  branch each needs a separate entry, evidence set and terminal.
- Direct-play status: no complete live match was played. Valve's current Steam
  metadata and official update feed pin the public client; SteamCMD retrieved
  the official dedicated package without launching it. Its text configuration,
  map briefing, English interface strings and bundled readme establish the
  executable rules trace. No video or audio was opened, played, heard or used.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `CS16-001` | The current purchasable Valve product is Counter-Strike, Steam app `10`, version `1.6`, public client build `12934623` | Confirmed | Corroborated | High | P1, P2, V1 |
| `CS16-002` | Valve's current official server package supplies Counter-Strike through app `90`; the shipped dedicated configuration sets a 20-minute map limit | Observation | Direct | High | V1 |
| `CS16-003` | Stock `de_dust2` is a two-site Bomb/Defuse map where Terrorists deliver C4 and Counter-Terrorists prevent or defuse the attack | Confirmed | Direct | High | V1 |
| `CS16-004` | A bomb round resolves through team elimination, an unplanted timeout, C4 explosion or uninterrupted defuse, with a separate fuse after planting | Confirmed | Direct | High | V1 |
| `CS16-005` | Purchases, money awards, surviving equipment and dropped-item pickup connect adjacent rounds | Observation | Direct | High | V1 |
| `CS16-006` | Lethal damage removes a player until the next round; the player then observes rather than respawning immediately | Confirmed | Direct | High | V1 |
| `CS16-007` | The HUD, radar, spatial sight/sound and team communication expose only partial live opponent state while revealing score, clocks, equipment and C4 state | Observation | Corroborated | High | P1, V1 |
| `CS16-008` | Stock `mp_timelimit 20` and zero default win/max-round limits bound the packet at a map-cycle transition with its final team-round score | Observation | Direct | High | V1 |
| `CS16-009` | Original Counter-Strike has no first-party bots; admitting bots would require a third-party modification | Confirmed | Direct | High | P3 |
| `CS16-010` | The repository transition trace reproduces purchase, transfer, plant, defuse, explosion, timeout, elimination, economy carry and map-cycle settlement | Observation | Direct | High | V2 |

## Basic data

- Release / origin: Valve; retail release `2000`, current official Steam
  product version `1.6`, public client build `12934623`.
- Platform or physical form: Windows Steam clients connected to Valve's
  official Half-Life Dedicated Server package; human-only networked session.
- Puzzle family: simultaneous team tactical counterplay under partial
  information; asymmetric bomb delivery and denial; real-time system pressure.
- Primary sources:
  - **[P1]** [official Steam product page](https://store.steampowered.com/app/10/CounterStrike/),
    for the current name, app identity, Valve authorship, availability,
    multiplayer platforms and team-mission framing.
  - **[P2]** [official Steam update feed](https://store.steampowered.com/oldnews/?appids=10&feed=steam_community_announcements),
    for the current public update boundary through Valve's `2023-12-12`
    multiplayer, dedicated-server, scoreboard and death-camera fixes.
  - **[P3]** [official Steam Support: Bots in Valve games](https://help.steampowered.com/en/faqs/view/6D65-DA3B-3B87-EE40),
    for the explicit classification of GoldSource Counter-Strike bots as
    third-party additions.
- Reproducible official package evidence:
  - **[V1]** SteamCMD app-info and official app `90` package retrieved
    `2026-09-01`. App `10` public build is `12934623`; the current installed
    dedicated package is build `15961496`; `liblist.gam` identifies
    Counter-Strike `1.6`. SHA-256: `server.cfg`
    `9cc49a925e6e8c8114b2a52070fd54e23a8b298bc796d6c6b5f5ec9b0817dbd3`,
    `readme.txt`
    `b7bfed8b90dc395693e93aa030bcd9f564913b9ed54d5529be44b6680ae87a39`,
    `maps/de_dust2.txt`
    `1812e8f86fb19ebfd5d9fc018a2b1c940d6ccafa98cfe0cd7362b319938290ea`,
    `resource/cstrike_english.txt`
    `b3cff0fd5f1ec2c8e5b0e10548410e4950107c723c693add2f035c14dfddb8ff`
    and `liblist.gam`
    `0dc83870fe4685bf409c3ba630a946da4e5fee6b782f9870242fcdaa6e2c3514`.
  - **[V2]** repository-side transition trace derived from `V1`; executable
    rules reasoning, not a claim of direct play.
- Claim IDs: `CS16-001`–`CS16-010`.

## Mechanical decomposition

### Action Genes

- Existing genes: `ACT-008`, directly traverse the first-person map;
  `ACT-130`, buy one offered round asset; `ACT-161`, aim and attack with the
  current weapon; `ACT-164`, select the active carried item; `ACT-183`, reload
  the active magazine; `ACT-184`, prime and throw a tactical grenade;
  `ACT-185`, hold a plant/defuse channel; `ACT-186`, drop equipment for
  transfer; `ACT-187`, communicate a live team cue.
- New genes: none.
- Parameters: team, position, movement, weapon, ammunition, aim, grenade,
  price, C4 site, plant/defuse duration and communication channel.
- Claim IDs: `CS16-003`–`CS16-007`.

### System Behaviour Genes

- Existing genes: `SYS-208`, resolve a ranged attack through material, armour
  and hit group; `SYS-215`, resolve direct simultaneous combat; `SYS-222`,
  pick up compatible dropped equipment; `SYS-292`, resolve tactical grenade
  flight and effect; `SYS-293`, remove a defeated player for the round and
  drop eligible equipment; `SYS-294`, adjudicate the bomb round; `SYS-295`,
  award and carry the round economy.
- New genes: none.
- Resolution order: accept live movement, weapon and communication input;
  resolve attack, utility and equipment transfer; lethal state removes control
  for the round; plant replaces the unplanted deadline with the C4 fuse;
  elimination, timeout, defuse or explosion awards the round; money and
  surviving gear carry into the next spawn; the map clock eventually invokes
  its stock cycle boundary.
- Parameters: weapon data, material, armour, grenade type, money awards,
  surviving equipment, round score, round clock, C4 fuse and map clock.
- Claim IDs: `CS16-004`–`CS16-008`.

### Constraint Genes

- Existing genes: `CON-261`, purchase requires buy time, zone and funds;
  `CON-262`, round equipment and ammunition are finite; `CON-263`, elimination
  suspends control until the next round; `CON-264`, C4 interaction requires
  the correct role, site/state and uninterrupted time; `CON-265`, the objective
  has asymmetric pre- and post-plant deadlines; `CON-266`, fixed T/CT roles
  bound objective authority and friendly interaction.
- New genes: none.
- Scarce strategic resources: living teammates, map and round time, money,
  saved weapons, armour, ammunition, grenades, defuse kit, C4 and fuse time.
- Claim IDs: `CS16-004`–`CS16-008`.

### Information Genes

- Existing genes: `INF-073`, carried inventory, active weapon and ammunition
  are visible; `INF-115`, local sight and sound expose partial opponent state;
  `INF-116`, HUD/radar expose team, score, clocks and C4 state; `INF-117`,
  personal money and purchase state are visible.
- New genes: none.
- Claim IDs: `CS16-005`–`CS16-008`.

### Objective Genes

- Existing genes: none.
- New `OBJ-135`: reach the stock 20-minute `de_dust2` map-cycle boundary with
  the team-round score that classifies the session as Terrorist lead, Counter-
  Terrorist lead or tie.
- Success, evaluation and failure: each round awards one team under Bomb/Defuse
  precedence. The bounded packet settles only at the shipped map-time cycle;
  team score, not personal kills, is evaluated. A tie remains a valid settled
  outcome, not an invented overtime trigger.
- Claim IDs: `CS16-004`, `CS16-008`, `CS16-010`.

### Time Genes

- Existing `TIM-003`: players act while movement, attacks, grenades, round and
  map clocks, plant and defuse channels progress in real time.
- New genes: none.
- Claim IDs: `CS16-004`–`CS16-008`.

## Reproducible transitions

| Before | Action | Deterministic or bounded resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| A living player is in a buy zone during buy time with enough money and capacity | Buy one offered item | Its price leaves the balance and the item enters a compatible equipment slot | gated round economy | `CS16-005` |
| A teammate needs a weapon and another player carries a droppable one | Drop the weapon; teammate contacts it with a compatible free slot | The item leaves one inventory, becomes a world object and enters the other | equipment transfer | `CS16-005` |
| The Terrorist C4 carrier reaches either `de_dust2` bomb site | Select C4 and hold the plant input for three seconds while stationary | A completed plant starts the separate C4 fuse; interruption leaves C4 unplanted | role/site/channel gate | `CS16-003`, `CS16-004` |
| C4 is planted and a living Counter-Terrorist reaches it | Hold Use without a kit for ten seconds, or with a kit for five | Uninterrupted completion immediately awards Counter-Terrorists; interruption or explosion prevents the defuse | kit-sensitive continuous objective | `CS16-004` |
| C4 remains planted until its fuse completes | Prevent a completed defuse | Explosion awards Terrorists even after the original round clock would have expired | post-plant objective precedence | `CS16-004` |
| C4 is not planted when the round timer expires | Allow the timer to reach zero | Counter-Terrorists win the round while surviving Terrorists may remain | asymmetric unplanted timeout | `CS16-004` |
| A player receives lethal damage | No same-round respawn exists | Control ends for that round, eligible equipment drops and the player observes until the next spawn | one-life round state | `CS16-006` |
| A round ends | Accept the next round transition | Team score and money awards update; surviving legal equipment and saved money persist | cross-round consequence | `CS16-005` |
| The stock map clock reaches 20 minutes after complete-round resolution | Accept the server's map-cycle transition | The session closes with the displayed team-round score as a T lead, CT lead or tie | reproducible bounded terminal | `CS16-008`, `CS16-010` |

## Strategic and experiential structure

- Local decision: choose exposure, crosshair placement, movement noise,
  recoil control, reload timing, grenade trajectory and whether the remaining
  fuse permits a complete plant or defuse.
- Medium-term planning: infer rotations from incomplete cues, coordinate an
  entry or retake, trade a teammate's elimination, deny dropped C4 and decide
  whether saving a weapon is more valuable than a low-probability objective.
- Long-term structure: convert round results and saved equipment into future
  buys while watching the finite map clock and team-round score.
- Common heuristics: isolate one sightline, avoid exposing C4 alone, preserve
  enough time for the full objective channel, communicate a dropped bomb and
  do not mistake personal kills for the bounded session result.
- Failure attribution: health, ammunition, money, equipment, round message,
  clocks and score are visible, while hidden positions and human coordination
  keep tactical causality partially uncertain.
- Player-trust factors: the shipped map, server configuration, objective text,
  clocks and scores are inspectable; public-server administration and anti-
  cheat quality are excluded.
- Claim IDs: `CS16-004`–`CS16-008`.

## Replay and variation

- What changes between sessions: human roster, team plans, purchases, weapon
  drops, routes, aim, utility, eliminations and sequence of round outcomes.
- Randomness or procedural generation: map geometry and server parameters are
  fixed; weapon spread and simultaneous human decisions vary live outcomes.
- Multiple viable strategies: site rush, split, slow information play, fake,
  bomb recovery, retake and equipment save exchange time, information and
  cross-round resources.
- Typical replay motive: tactical coordination, aim and utility mastery, and
  adaptation of buys and routes to the opposing team.
- Claim IDs: `CS16-004`–`CS16-008`.

## Adjacent systems and history

- Direct successors: Counter-Strike: Source and Counter-Strike 2 retain the
  bomb-round lineage while changing engine, content and match policies.
- Variants: hostage and other stock map objectives, legacy branches, community
  server configurations and competitive rulesets need independent bounds.
- Similar games: Counter-Strike 2, Rainbow Six Siege, Valorant and other
  one-life asymmetric tactical shooters.
- Important differences: unlike the Atlas Counter-Strike 2 packet, this unit
  contains no MR12 regulation, halftime side swap, 13-round clinch or 12–12
  draw rule. It accepts the shipped 20-minute server cycle and final team score.
- Claim IDs: `CS16-001`–`CS16-009`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-130`, `ACT-161`, `ACT-164`, `ACT-183`–`ACT-187` | aim, weapon and channel timing are parameters |
| System Behaviour | `SYS-208`, `SYS-215`, `SYS-222`, `SYS-292`–`SYS-295` | exact weapon, reward and fuse values are parameters |
| Constraint | `CON-261`–`CON-266` | inventory limits, buy window and role permissions are parameters |
| Information | `INF-073`, `INF-115`–`INF-117` | radar scale and sound range are parameters |
| Objective | `OBJ-135` | map identity, time limit and final score relation are parameters |
| Time | `TIM-003` | round, plant, defuse, fuse and map clocks are parameters |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `217` (`GAME-0001`–`GAME-0217`).
- Exact genome matches: none.
- Tied near matches: `GAME-0137` — Counter-Strike 2 (`27 / 31 = 0.870968`).
- Supported combination subsets: `COMB-0216`.
- Scan date: 2026-09-01.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0137` — Counter-Strike 2 | `ACT-008`, `ACT-130`, `ACT-161`, `ACT-164`, `ACT-183`–`ACT-187`, `SYS-208`, `SYS-215`, `SYS-222`, `SYS-292`–`SYS-295`, `CON-261`–`CON-266`, `INF-073`, `INF-115`–`INF-117`, `TIM-003` | both share purchases, one-life C4 rounds, partial team information and carried economy; Counter-Strike 2 adds a halftime side/economy reset and MR12 clinch/draw policy, while this Counter-Strike packet settles at the shipped 20-minute map cycle with a lead or tie | Near, `0.870968` |

## Taxonomy impact

- Existing boundaries retained: the 27 shared genes keep the classic tactical
  bomb-round mechanisms aligned with Counter-Strike 2 without importing its
  current regulation policy.
- New boundary: `OBJ-135` isolates a stock server's finite map-time settlement
  by team-round score; it is narrower than winning a fixed round-count match.
- Lifecycle changes: none.

## Negative results

- No exact prior genome exists; Counter-Strike 2 differs by `SYS-296`,
  `CON-267` and `OBJ-071`, while Counter-Strike uses `OBJ-135`.
- No earlier verified combination is a strict subset of this genome.
- `OBJ-071` was rejected because the shipped configuration has no round-win
  clinch, regulation maximum, halftime or draw/overtime policy.
- First-party bots were rejected because official Steam Support classifies
  original Counter-Strike bots as third-party additions.
- Kill-score, generic session survival and unbounded play were rejected as the
  terminal because the stock 20-minute map cycle supplies a reproducible end.
