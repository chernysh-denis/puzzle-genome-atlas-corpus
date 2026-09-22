---
game_id: GAME-0336
slug: pokemon-red-version
game_title: "Pokémon Red Version"
analysis_status: reviewed
reviewed: 2026-09-21
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-019
    - ACT-130
    - ACT-194
    - ACT-258
    - ACT-259
  system:
    - SYS-004
    - SYS-299
    - SYS-307
    - SYS-362
    - SYS-854
    - SYS-954
    - SYS-955
    - SYS-956
    - SYS-957
  constraint:
    - CON-210
    - CON-276
    - CON-277
    - CON-282
    - CON-384
    - CON-656
  information:
    - INF-123
    - INF-363
  objective:
    - OBJ-197
  time:
    - TIM-001
---

# Game: Pokémon Red Version

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Squirtle, Bubble,
Pidgey, Rattata, Oak's Parcel, Viridian Forest, Brock and BoulderBadge are
carrier parameters, not gene names.

## Analysis scope

- Version / ruleset: the original English USA Game Boy `Pokémon Red Version`,
  reproducibly identified by the `Pokemon Red (UE) [S][!].gb` SHA-1
  `ea9bcae617fdf159b045185467ae58b2e4a48b9a`. It is not the 3DS Virtual
  Console release, a remake, a later generation or `Pokémon Blue Version`.
- Structured analysis target: original Game Boy cartridge rules reconstructed
  from Nintendo's original manual and the exact-ROM `pret/pokered` disassembly
  pinned at commit `a1a22aaf84d1675bcdbaeb194592379d586d838e`; see
  `GAME-0336` in
  [`knowledge/platforms/games.json`](../../platforms/games.json).
- Scenario: one fresh single-player New Game using the default battle style,
  from first ordinary control in the upstairs Pallet Town bedroom through the
  complete post-battle settlement after defeating Brock in Pewter Gym.
- Entry: no Pokémon, Pokédex, Bag progress, badge, visited Pokémon Center or
  retained save state exists. Character and rival names are parameters.
- Fixed reproducible route: trigger Professor Oak at Pallet Town's north grass;
  choose Squirtle; settle the mandatory lab rival battle; reach Viridian Mart,
  receive Oak's Parcel, return it and receive the Pokédex; revisit Viridian
  Mart, buy Poké Balls, weaken and capture the first eligible Route 1 Pidgey or
  Rattata, then make one voluntary party switch in a later eligible battle;
  train Squirtle to at least level 8 so Bubble is learned; heal at Viridian or
  Pewter Pokémon Center; traverse Viridian Forest; defeat the Pewter Gym
  trainer and Brock's level-12 Geodude and level-14 Onix; retain one free Bag
  slot so TM34 can be received before the BoulderBadge bit is set.
- Primary decision loop: navigate authored routes and gates; manage one active
  Pokémon from a persistent bounded party; commit FIGHT, PKMN, ITEM or RUN;
  allocate finite move PP, health and Poké Balls; use type affinity and party
  switching to survive sampled wild and fixed trainer battles; convert wins
  into money, experience, levels and moves; restore the party at a Pokémon
  Center; progress through the parcel/Pokédex and Gym gates.
- Positive terminal: Brock's two Pokémon are defeated and his automatic
  post-battle script sets `EVENT_BEAT_BROCK`, gives TM34 with the preserved Bag
  slot, sets `BIT_BOULDERBADGE` and returns ordinary control. Content after
  that return is outside the packet.
- Failure path: outside the exceptional first lab rival battle, fainting every
  party member heals the party, halves current money and returns the player to
  the last used Pokémon Center. The route may continue, but that recovery does
  not satisfy the positive terminal.
- Included: four-direction overworld navigation; one fixed starter; the first
  rival battle; ordered parcel and Pokédex gates; local grass encounter tables;
  random wild species/level selection; fixed Trainer parties; one active
  Pokémon; voluntary or forced switching; FIGHT/PKMN/ITEM/RUN; move types,
  accuracy, damage, status, PP and Speed order; health/fainting; ordinary
  Poké Ball purchase and capture; six-member party and Box destination check;
  battle money and experience; level-up and Bubble; free whole-party Center
  healing; blackout recovery; Brock and the BoulderBadge settlement.
- Reproducible parameterisation: exact step count, encounter samples, capture
  target, damage rolls, critical hits, misses, status, remaining HP/PP/money,
  optional wild battles and movement path may vary. The required gates,
  Squirtle choice, one capture, one voluntary switch, level-8 Bubble access,
  Center healing, Brock party and positive terminal do not.
- Excluded: Route 22 rival, Mt. Moon and every post-BoulderBadge area; exhaustive
  Pokédex completion, trading, link battles, evolution, breeding, Day Care,
  Safari Zone, hidden glitches and MissingNo.; other starters as played route;
  later Gyms, Elite Four and full campaign; Blue/Yellow, FireRed/LeafGreen,
  Let's Go, 3DS emulation, save states, speed-up, cheats, ROM hacks and ports.
- Direct-play status: not conducted. No cartridge, entitlement, emulator, ROM,
  save, screenshot, video, audio or input trace was used. The original manual
  and exact-ROM disassembly support a source-bounded reconstruction rather
  than a claimed playthrough.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `PKR-001` | The packet is the original English Game Boy Red ROM identity and not a remake, port or Blue ruleset | Confirmed | Direct | High | P1, P2, R1 |
| `PKR-002` | Oak gates northward movement until one starter is selected, after which the rival selects the type-counter starter and initiates the first battle | Confirmed | Direct | High | P2, R1 |
| `PKR-003` | Oak's Parcel must be collected in Viridian Mart and returned before the Pokédex event clears the Viridian route gate and ordinary Ball purchases become available | Confirmed | Direct | High | P2, R1 |
| `PKR-004` | Eligible grass steps sample an encounter check and then a local weighted species/level slot; Route 1 contains only Pidgey and Rattata in the scoped version | Confirmed | Direct | High | P2, R1 |
| `PKR-005` | Battle offers FIGHT, PKMN, ITEM and RUN; a selected move needs PP, then move priority and Speed order the two actions before residual effects and faint checks | Confirmed | Direct | High | P2, R1 |
| `PKR-006` | Move type, attacker type and defender affinity modify damage; one living party member is active and a legal switch retains each member's HP, status, level, moves and PP | Confirmed | Direct | High | P2, R1 |
| `PKR-007` | A Poké Ball cannot capture a Trainer's Pokémon; an eligible wild attempt consumes a Ball, samples health/status/catch-rate probability and sends success to party or Box according to capacity | Confirmed | Direct | High | P2, R1 |
| `PKR-008` | Participating Pokémon gain battle experience; thresholds raise levels and may teach a move, while Trainer victory also grants money | Confirmed | Direct | High | P2, R1 |
| `PKR-009` | A Pokémon Center restores party HP, status and PP and becomes the return point; an ordinary all-party faint heals, halves money and returns there | Confirmed | Direct | High | P2, R1 |
| `PKR-010` | Brock uses level-12 Geodude and level-14 Onix; defeating both and completing the post-battle script records the BoulderBadge and closes the packet | Confirmed | Direct | High | P2, R1 |
| `PKR-011` | The signature admits only transitions causally available in the fixed opening-to-BoulderBadge route | Observation | Direct | High | P1, P2, R1, V1 |

## Basic data

- Release / origin: Game Freak / Creatures / Nintendo; original late-1990s
  Game Boy software. Nintendo's current archive identifies the original Game
  Boy title, Pallet Town opening, Pokédex, Gyms, battles and trades.
- Platform or physical form: original monochrome Game Boy cartridge program;
  the exact English Red ROM is identified by its reproducible build hash.
- Puzzle family: tactical forecast and counterplay; inventory and fixture
  dependencies; ordered dependency sequencing.
- Primary sources, accessed 2026-09-21:
  - **[P1]** [official Nintendo product archive](https://www.nintendo.com/en-gb/Games/Game-Boy/Pokemon-Red-Version-266109.html),
    for original Game Boy identity, developer/publisher, Pallet Town premise,
    catching, Pokédex, Gyms, battles and trading.
  - **[P2]** [original Nintendo of America manual](https://www.videogamemanual.com/gameboy/Pokemon%20-%20Red%20Version%20%28USA%29.pdf),
    for the three starters; Route 1 and Viridian route; parcel, Poké Mart,
    Poké Ball, capture and Pokédex; Center recovery; Trainer parties; the four
    battle commands, switching, PP, experience, levels, blackout; Brock's
    Rock-type team and BoulderBadge.
- Reproducible source:
  - **[R1]** [`pret/pokered` at commit `a1a22aaf`](https://github.com/pret/pokered/tree/a1a22aaf84d1675bcdbaeb194592379d586d838e),
    whose documented Red build matches SHA-1
    `ea9bcae617fdf159b045185467ae58b2e4a48b9a`; route scripts, encounter tables,
    battle core, item effects, experience, Center healing and blackout code
    close the exact transitions and edge cases used here.
- Validation source:
  - **[V1]** repository-side transition reconstruction from P1, P2 and R1;
    source and rules reasoning only, with no direct play or audiovisual claim.
- Claim IDs: `PKR-001`–`PKR-011`.

## Mechanical decomposition

### Action Genes

- `ACT-008`: move the persistent Trainer one orthogonal overworld step through
  towns, routes, grass, buildings and forest geometry.
- `ACT-019`: with the active Pokémon awaiting a FIGHT command, select one
  learned move and its opposing combatant target.
- `ACT-130`: spend current money on one offered Poké Ball at Viridian Mart,
  adding the accepted quantity to bounded Bag inventory.
- `ACT-194`: from ITEM during an eligible wild battle, commit one carried Poké
  Ball against the current wild Pokémon and spend it after the attempt settles.
- `ACT-258`: use PKMN to replace the current active Pokémon with another living
  party member while both retain persistent personal state.
- `ACT-259`: choose Squirtle from Oak's three offered starters so it becomes the
  first persistent party member and fixes the rival's counter choice.
- Claims: `PKR-002`, `PKR-005`–`PKR-008`.

### System Behaviour Genes

- `SYS-004`: sample encounter checks, weighted encounter slots, damage ranges,
  accuracy, Speed ties, capture checks and other admitted random outcomes.
- `SYS-299`: participating battle experience crosses persistent Pokémon level
  thresholds, recalculates stats and can expose a newly learned move; Squirtle
  learns Bubble at level 8 in the scoped route.
- `SYS-307`: the current wild Pokémon's catch rate, HP, status and Ball type
  resolve a probabilistic capture; success updates Pokédex ownership and sends
  it to the free party slot or Box branch.
- `SYS-362`: defeating a wild or Trainer Pokémon distributes eligible
  experience to participants; settling a Trainer battle also awards its money.
- `SYS-854`: a damaging move applies same-type attack bonus and the type table
  before health loss, status effects and fainting; Water-type Bubble is favourable
  against Brock's Rock/Ground party.
- New `SYS-954`: an eligible overworld step tests the current terrain/map
  encounter rate, samples the local weighted slot and instantiates that
  species and level as a bounded wild battle.
- New `SYS-955`: after one player command and the opponent command are fixed,
  command class, special move priority and then Speed order their effects;
  fainting or escape may cancel the later action before the next menu cycle.
- New `SYS-956`: each party member's HP, status, level, moves and PP persist
  across ordinary battles; an accepted Pokémon Center service clears status
  and restores every member's HP and move PP while recording that Center as
  the return point.
- New `SYS-957`: when no party member remains able to battle, ordinary route
  play heals the whole party, halves current money and transfers the Trainer
  to the last used Pokémon Center; the opening lab rival exception does not.
- Resolution order: a route step may sample a wild encounter; battle entry
  loads persistent party state and one opponent; the player commits one menu
  command; the opponent command is selected; command and Speed order settle
  actions; move PP, type, damage, status and fainting update persistent state;
  victory distributes rewards or capture stores the wild Pokémon; all-party
  faint invokes blackout recovery; story events advance only through their
  authored gates; Brock settlement records the badge.
- Claims: `PKR-003`–`PKR-010`.

### Constraint Genes

- `CON-210`: Poké Ball purchase and use must fit and spend the Bag's bounded
  typed item slots and quantities; one free slot is retained for TM34.
- `CON-276`: capture requires a carried compatible Ball and the current
  capturable wild target; Trainer-owned Pokémon reject the attempt.
- `CON-277`: a captured Pokémon enters the six-member party only when a slot is
  free, otherwise the current Box must have capacity; full party plus full Box
  prevents the throw.
- `CON-282`: Oak appearance, starter, lab battle, parcel return, Pokédex,
  Viridian route access, forest traversal and Pewter Gym form ordered authored
  gates; Brock cannot settle before their route prerequisites.
- `CON-384`: exactly one living eligible party member occupies the active
  commanded battle slot; fainting forces a replacement, and no living member
  causes blackout.
- New `CON-656`: a learned move can be selected only while its current PP is
  positive and it is not disabled; each ordinary use spends one PP, and when
  no usable move remains the rules substitute Struggle.
- Scarce route state: Pokémon HP/status, move PP, party slots, Bag slots,
  Poké Balls, money, captured identity, experience/level, Center return point
  and ordered story/badge flags.
- Claims: `PKR-003`, `PKR-005`–`PKR-010`.

### Information Genes

- `INF-123`: party summaries expose each owned Pokémon's identity, level,
  status, HP, stats, type and learned moves before switching or planning.
- New `INF-363`: the battle decision surface exposes both active identities,
  levels, HP bars and status; FIGHT/PKMN/ITEM/RUN; and for the highlighted move
  its type plus current and maximum PP, without revealing the opponent's next
  selected move or random result.
- Claims: `PKR-005`–`PKR-009`.

### Objective Genes

- New `OBJ-197`: defeat Brock's complete declared party and complete his
  post-battle reward script so the BoulderBadge is retained before ordinary
  Pewter Gym control returns.
- Success, evaluation and failure: Geodude and Onix must both faint; a loss,
  escape or badge text without the final retained badge bit is not success.
  The fixed route preserves a Bag slot so TM34 and the badge settlement both
  complete.
- Claims: `PKR-010`.

### Time Genes

- `TIM-001`: overworld movement and menu navigation wait for discrete inputs;
  after a battle command is committed, its ordered attack/item/switch/run and
  opposing response settle before the next decision surface is accepted.
- Claims: `PKR-004`–`PKR-010`.

## Reproducible transitions

| Before | Action | Deterministic or bounded resolution | Establishes | Claim |
|---|---|---|---|---|
| A fresh Trainer reaches Pallet Town's north grass with no party | step north | Oak interrupts, returns the Trainer to the Lab and exposes the three starter choices | authored opening gate | `PKR-002` |
| Three starter Ball objects remain offered | accept Squirtle | Squirtle becomes the first owned party member; the rival takes the counter starter and the required lab battle follows | persistent starter commitment | `PKR-002` |
| The lab rival battle has settled and Oak lacks his parcel | enter Viridian Mart, return to Oak and complete the request dialogue | the parcel enters then leaves the Bag; the Pokédex is granted, route-blocking old-man state changes and Mart inventory becomes ordinarily available | ordered story dependency | `PKR-003` |
| Poké Balls are offered for 200 and money plus Bag capacity suffice | buy at least one Ball | money decreases and the accepted quantity enters the typed Bag stack | priced capture supply | `PKR-003`, `PKR-007` |
| The Trainer takes an eligible grass step on Route 1 | advance one tile | an encounter-rate check may fail; on success one weighted Route 1 slot supplies a level-2–5 Pidgey or Rattata and starts a wild battle | terrain-sampled encounter | `PKR-004` |
| An eligible wild Pidgey or Rattata remains alive and a Ball is carried | lower HP, choose ITEM and commit one Poké Ball | one Ball is spent; the health/status/catch-rate checks fail or record ownership and put the first capture in the free party slot | probabilistic capture | `PKR-007` |
| Starter and captured Pokémon are both living in party | choose PKMN and select the other member during a later eligible battle | the selected member becomes the sole active battler and retains its own HP, status, level, moves and PP; the exchange consumes the turn | bounded party switching | `PKR-006` |
| A highlighted learned move has positive PP | confirm the move | one PP is spent; player and opponent commands are ordered by command/move priority and Speed, then accuracy, type, damage, status and faint checks settle | finite ordered turn combat | `PKR-005`, `PKR-006` |
| A participant gains enough experience for the next threshold | settle the defeated opponent | level and stats update; at Squirtle level 8 the move-learning transition exposes Bubble | persistent battle growth | `PKR-008` |
| The party has missing HP, status or PP and a Center is reachable | accept the nurse's healing offer | every party member's HP and PP return to maximum, status clears and that Center becomes the blackout return point | whole-party service | `PKR-009` |
| Every party member faints outside the lab-rival exception | allow the loss transition to settle | party is healed, current money is halved and traversal resumes at the last used Center; badge objective remains incomplete | recoverable route failure | `PKR-009` |
| Squirtle has Bubble and Brock's Geodude then Onix are active | select legal Water attacks while preserving party viability | typed damage defeats both fixed opponents; the automatic script records victory, gives TM34 with the free Bag slot and sets BoulderBadge before control returns | scoped positive terminal | `PKR-010` |

## Strategic and experiential structure

- Local decision: choose a legal move, switch, item or escape attempt from
  visible HP/status/PP and the known or inferred type matchup; decide whether a
  weakened wild target is worth another finite Ball.
- Medium-term planning: turn the starter and first capture into a viable party,
  distribute battle participation, reach Bubble without exhausting PP, spend
  money on enough Balls and preserve a Bag slot for the final reward.
- Long-term structure: satisfy the parcel/Pokédex route gate, convert sampled
  encounters into capture and experience, restore at Centers and carry a
  trained type-appropriate party through Viridian Forest into Brock's fixed
  badge battle.
- Common heuristics: weaken before capture; do not throw at Trainer-owned
  Pokémon; switch before a faint when a useful reserve member exists; use Water
  damage against Brock; heal HP and PP before the Gym; keep one Bag slot free.
- Failure attribution: battle HUD, move PP/type, party summaries, reward text,
  Center feedback and story dialogue distinguish depleted move supply, bad type
  choice, party collapse, missing route gate and incomplete post-battle reward.
  Encounter, hit, damage and capture samples remain bounded uncertainty.
- Claims: `PKR-003`–`PKR-011`.

## Replay and variation

- What changes between attempts: encounter timing and identity, capture target
  and attempts, damage/critical/miss samples, switch order, optional battles,
  level timing, HP/PP/money and the path through the forest.
- Randomness or procedural generation: authored maps, story gates, Trainer
  parties and Brock are fixed; grass encounters sample local weighted tables,
  while combat and capture contain bounded random checks.
- Multiple viable strategies: the full product supports all three starters,
  many catches and different routes; this reproducible packet fixes Squirtle,
  one early capture and level-8 Bubble to make the evidence route comparable.
- Typical replay motive: choose another starter, capture another party, pursue
  a Pokédex or complete the campaign. Those broader motives remain outside this
  bounded opening-to-badge record.
- Claims: `PKR-002`–`PKR-011`.

## Adjacent systems and history

- Direct predecessors: earlier turn-based role-playing games supply menu
  combat, levels and typed resources; creature-collection games supply
  capture, party ownership and collection records.
- Variants: Blue changes encounter tables while sharing the story; Yellow,
  FireRed/LeafGreen, Let's Go and 3DS Virtual Console require separate version
  evidence and cannot inherit this signature automatically.
- Similar games: Pokémon Legends: Z-A shares starter commitment, capture,
  owned party, switching, levels, profile information and capacity gates, but
  its battle movement, move reach and cooldowns are live rather than Red's
  paired menu-command turns.
- Important difference: Red's wild opponent is instantiated by an eligible
  terrain-step sample and its FIGHT move consumes persistent PP; Legends: Z-A
  instead exposes a visible world creature and cooldown-based live commands.

## Normalised genome

The front matter is canonical. The complete signature contains 25 Active
genes: six Action, nine System Behaviour, six Constraint, two Information,
one Objective and one Time gene. Species, moves, route labels and reward names
remain carrier parameters.

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `335` (`GAME-0001`–`GAME-0335`).
- Exact genome matches: none.
- Tied near matches: `GAME-0160` — Pokémon Legends: Z-A (`13 / 48 = 0.270833`).
- Supported combination subsets: none.
- Scan date: 2026-09-21.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0160` Pokémon Legends: Z-A | `ACT-008`, `ACT-019`, `ACT-194`, `ACT-258`, `ACT-259`, `SYS-004`, `SYS-299`, `SYS-307`, `CON-210`, `CON-276`, `CON-277`, `CON-384`, `INF-123` | Z-A exposes visible world capture, live free movement, move reach/cooldowns and rank promotion; Red instead samples terrain encounters, orders paired menu commands by priority/Speed, spends persistent PP, restores a carried party at Centers and closes on Brock's retained badge | nearest only; `13 / 48 = 0.270833`, not equivalent |

## Taxonomy impact

`SYS-954`–`SYS-957`, `CON-656`, `INF-363` and `OBJ-197` are new.
`TAXONOMY_CHANGE_079` generalises `ACT-019`, `ACT-194`, `ACT-258`, `SYS-307`,
`CON-276`, `CON-277`, `CON-384` and `INF-123` from spatial/live first carriers
to the same transferable target, capture, party and profile operations in
turn-based Red. Stable support is added to `ACT-008`, `ACT-130`, `ACT-259`,
`SYS-004`, `SYS-299`, `SYS-362`, `SYS-854`, `CON-210`, `CON-282` and
`TIM-001` without changing their boundaries. No earlier signature changes.

## Negative results

- No verified combination is registered from one new carrier.
- No direct play, ROM possession, emulation, audiovisual observation, save or
  installed-cartridge parity test is claimed.
- The packet does not infer Blue encounter tables, later-generation type rules,
  Special split, abilities, held items, breeding or modern experience sharing.
- Optional item pickups, museum data, Route 22 rival, exhaustive collection,
  trading and link battle are not admitted merely because the cartridge
  contains them.
- The lab rival loss is not modelled as ordinary blackout: source code returns
  control inside the Lab without the Center transfer or money-halving path.
- A Pokédex goal is described by the manual but exhaustive completion lies
  outside this one-badge terminal and does not become an Objective gene.
- `INF-170` is rejected because Red exposes PP/type in discrete menus rather
  than a live four-button cooldown surface; `INF-363` preserves that boundary.

## Delta summary

## New facts

- [Confirmed | Direct | High] The original manual and exact-ROM source close
  the starter, parcel, Pokédex, capture, party, battle, Center, blackout and
  first-Gym transitions within one reproducible cartridge ruleset.
- [Confirmed | Direct | High] The disassembly fixes Route 1 and Viridian Forest
  encounter tables, Brock's exact party and the post-battle badge-setting edge.

## New genes

- [Confirmed | Direct | High] Seven new boundaries isolate terrain-sampled
  wild encounters, paired command ordering, retained/healed party state,
  blackout recovery, PP legality, the battle decision surface and the retained
  BoulderBadge terminal.

## New combinations

- [Observation | Direct | High] None; recurrence remains evidence-driven.

## Taxonomy changes

- [Confirmed | Direct | High] `TAXONOMY_CHANGE_079` broadens eight established
  capture/party boundaries without changing their causal tests or earlier
  signatures.

## New questions

- Which other early creature-collection RPG independently couples terrain
  encounter sampling, finite move PP and party-wide Center restoration?
- Does a later bounded Pokémon packet warrant a separate Pokédex collection
  objective without conflating collection progress with one-badge completion?

## Next recommended game

- `GAME-0337` Super Metroid, as reserved by selection 023.

## Why this game

- Pokémon Red Version is a recognisable handheld anchor whose opening turns a
  starter choice, sampled encounters, probabilistic capture, persistent party
  state, finite move supply and type-aware turn combat into one ordered route
  ending at a retained badge.
