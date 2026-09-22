---
game_id: GAME-0346
slug: chrono-trigger
game_title: Chrono Trigger
analysis_status: reviewed
reviewed: 2026-09-21
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-019
    - ACT-130
    - ACT-341
  system:
    - SYS-355
    - SYS-362
    - SYS-854
    - SYS-970
    - SYS-971
  constraint:
    - CON-136
    - CON-269
    - CON-282
    - CON-323
  information:
    - INF-119
    - INF-179
  objective:
    - OBJ-203
  time:
    - TIM-026
---

# Game: Chrono Trigger

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Crono, Marle,
Lucca, Taban, Gato, Leene Square, Silver Points, G, Telepod, Pendant, Gate,
1000 A.D., 600 A.D. and Truce Canyon are carrier parameters, not gene names.

## Analysis scope

- Version / ruleset: the original North American English Super Nintendo
  Entertainment System Game Pak released by Square Soft in 1995. It is not the
  Japanese Super Famicom build, PlayStation/Final Fantasy Chronicles, Nintendo
  DS, mobile, Steam, Wii Virtual Console wrapper, translation patch,
  randomiser, ROM hack, New Game + or emulator-enhanced ruleset.
- Structured analysis target: the original English manual's New Game, field,
  map, Active/Wait battle, command, gauge, item and Game Over rules, joined to
  a written original-SNES route for the Millennial Fair, Gato, Silver Points,
  Telepod incident and first arrival in 600 A.D.; see `GAME-0346` in
  [`knowledge/platforms/games.json`](../../platforms/games.json).
- Scenario: one fresh New Game in `Wait` battle mode, from the first ordinary
  control of Crono in his bedroom through one fair challenge, one Silver Point
  exchange and the first authored time-gate transition.
- Entry: the opening presentation has finished and Crono first accepts ordinary
  directional input beside his bed in 1000 A.D. No prior save, New Game +
  state, equipment, money, experience or configuration is imported.
- Fixed reproducible route: walk downstairs, complete the required exchange
  with Crono's mother and collect the offered 200 G; enter Leene Square; collide
  with Marle, speak to her before retrieving and returning her Pendant, and
  accept her into the party; walk to the visible Gato challenge and accept it;
  use ready party commands to defeat Gato; receive 15 Silver Points, 10 EXP and
  1 TP; exchange exactly 10 Silver Points for 50 G at the money tent; learn that
  Lucca's demonstration is ready; wait while Marle chooses candy; reach the
  Telepods; let Crono complete the ordinary demonstration; let Marle's Pendant
  create the Gate and remove her from the scene; collect the dropped Pendant,
  accept Crono's second Telepod transit and stop when ordinary Crono control
  first resumes beside the Gate in Truce Canyon, 600 A.D., before movement
  releases the first Blue Imp encounter.
- Primary decision loop: navigate one visible field or landscape screen toward
  the next actor, challenge, booth or mechanism; commit its currently legal
  interaction; during Gato's challenge, wait for each party member's personal
  Battle Gauge, choose an available command and legal target, let party and
  enemy readiness resolve until the encounter settles, then spend the awarded
  fair currency and continue the ordered interaction route.
- Positive terminal: Gato has been defeated, 10 of the awarded 15 Silver
  Points have become 50 G, the Telepod/Pendant dependency has transferred Crono
  from 1000 A.D. to 600 A.D., and ordinary control resumes beside the Truce
  Canyon Gate. Moving far enough to release Blue Imps is outside the packet.
- Failure and recovery: exhausting both active party members' HP against Gato
  does not produce route-terminal Game Over; the optional fair challenge ends,
  the party is restored to one HP and may challenge again. A loss awards no
  Silver Points, so the fixed route retries Gato before the exchange. The
  packet has no irreversible negative terminal under ordinary admitted play.
- Included: four-direction field and landscape navigation; running; contextual
  talk, pickup, booth and Telepod interaction; Marle's authored party join and
  later removal; Gato's visible challenge; personal Battle Gauges; Attack,
  available Tech/Combo and Item commands with legal targets; HP, MP, learned
  Tech state and battle readiness; Gato damage, defeat, non-terminal party
  defeat, 10 EXP, 1 TP and 15 Silver Points; the fixed `10 SP -> 50 G`
  exchange; ordered fair-readiness, candy, demonstration, Pendant and Gate
  flags; and the authored 1000-to-600 A.D. relocation.
- Reproducible parameterisation: retain default character names, choose `Wait`
  before the opening, do not visit Guardia Forest or another optional battle,
  and use the route above. Gato command order, damage rolls, remaining HP/MP
  and exact walking time may vary. His presence, reward, exchange rate,
  required fair flags, Pendant reaction, Gate destination and first 600 A.D.
  control state do not.
- Excluded: Mayor's Manor, Porre, Guardia Forest, shopping for equipment or
  items, bell/race/soda games, repeated Gato farming, Norstein Bekkler, cat and
  lunch trial flags, later trial consequences, New Game + sparkle, saving,
  first Truce Canyon movement and every 600 A.D. encounter, chest, exit, castle
  and story event; later party members, Dual/Triple Tech progression, magic,
  Epoch, End of Time, endings, ports, emulator states, cheats and glitches.
- Direct-play status: not conducted. No Game Pak, console, ROM, emulator, save,
  controller trace, screenshot, video or audio was used. This is a
  source-bounded reconstruction, not a claimed playthrough or inspection of
  copyrighted game data.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `CT-001` | The packet targets the original North American English 1995 SNES ruleset, not a later port or New Game + | Confirmed | Corroborated | High | P1, P2 |
| `CT-002` | Directional input moves the party on field and landscape screens, while A talks, opens, picks up and enters nearby authored entities | Confirmed | Direct | High | P1 |
| `CT-003` | Active and Wait are selectable New Game battle modes; a ready personal Battle Gauge exposes Attack, Tech/Combo or Item command resolution | Confirmed | Direct | High | P1 |
| `CT-004` | Contacting the visible Gato challenge starts a bounded party battle whose victory awards 15 Silver Points, 10 EXP and 1 TP | Observation | Corroborated | High | P1, S1, S2 |
| `CT-005` | Losing the Gato challenge revives the party at one HP instead of producing route-terminal Game Over | Observation | Corroborated | High | S1 |
| `CT-006` | The fair booth exchanges 10 Silver Points for 50 G, leaving five after one successful Gato victory and one exchange | Observation | Corroborated | High | S1, S2 |
| `CT-007` | Marle joins after the returned Pendant and remains commandable for the Gato battle, then the Telepod incident removes her from the party | Observation | Corroborated | High | S2, S3 |
| `CT-008` | Fair readiness, candy, Crono's demonstration, Marle's Pendant reaction and retrieval of the dropped Pendant form an ordered mechanism dependency | Observation | Corroborated | High | S2, S3 |
| `CT-009` | The second Telepod activation carries Crono through the same Gate and restores ordinary control in Truce Canyon, 600 A.D. | Observation | Corroborated | High | P2, S2, S3 |
| `CT-010` | The complete signature admits only systems causally available between first bedroom control and first 600 A.D. canyon control | Observation | Corroborated | High | P1–P2, S1–S3, V1 |

## Basic data

- Release / origin: Square / Square Soft; original North American Super
  Nintendo Entertainment System release, 1995.
- Platform or physical form: licensed North American SNES Game Pak on a Super
  Nintendo Entertainment System.
- Puzzle family: tactical forecast and counterplay; inventory and fixture
  dependencies; ordered dependency sequencing.
- Primary sources, accessed 2026-09-21:
  - **[P1]** [Square Soft's original English SNES instruction
    booklet](https://archive.org/download/SNESManuals/Chrono%20Trigger%20%28USA%29.pdf),
    pp. 12–17 and 23–31, for New Game, Active/Wait, field and landscape input,
    party, Battle Gauge, commands, targeting, Tech/Combo and Game Over rules.
  - **[P2]** [Nintendo's preserved Chrono Trigger Virtual Console product
    page](https://www.nintendo.com/en-gb/Games/Virtual-Console-Wii-/CHRONO-TRIGGER--276676.html),
    identifying the represented Super Nintendo title and publisher-provided
    portal-to-the-past premise. It establishes product identity, not wrapper
    parity or the scoped route.
- Corroborating sources:
  - **[S1]** [StrategyWiki's SNES-selected Millennial Fair games
    reference](https://strategywiki.org/wiki/Chrono_Trigger/Millennial_Fair_games),
    for Gato's 15 Silver Point, 10 EXP and 1 TP victory settlement, one-HP loss
    recovery and the `10 SP -> 50 G` exchange.
  - **[S2]** [GameFAQs original-SNES route by
    Dev](https://gamefaqs.gamespot.com/snes/563538-chrono-trigger/faqs/13618),
    for first control, Marle's party join, fair readiness, candy, both Telepod
    demonstrations, Pendant reaction and 600 A.D. arrival.
  - **[S3]** [Thonky's Millennial Fair written
    route](https://www.thonky.com/chrono-trigger/millennial-fair), independently
    corroborating the fresh opening, Marle/Pendant order, demonstration and
    first Gate transition.
- Validation source:
  - **[V1]** repository-side executable transition reconstruction derived from
    P1–P2 and S1–S3; it validates stated state predicates only and does not
    execute or inspect the commercial program.
- Claim IDs: `CT-001`–`CT-010`.

## Mechanical decomposition

### Action Genes

- `ACT-008`: directly walk or run Crono and the current party across each
  field or landscape screen to actors, Gato, the money tent and Telepods.
- `ACT-019`: after a party member's Battle Gauge fills, choose one currently
  available Attack, Tech/Combo or item ability and its legal Gato or ally
  target.
- Generalised `ACT-130`: spend 10 Silver Points at the money tent to acquire
  the fixed offered 50 G currency asset; the exchange does not require a new
  verb merely because both sides are currencies.
- `ACT-341`: talk to or collect the addressed actor/object and activate the
  currently legal booth or Telepod state.
- Claims: `CT-002`–`CT-004`, `CT-006`, `CT-008`.

### System Behaviour Genes

- Generalised `SYS-355`: accepting contact with visible Gato transfers the
  current recruited party into his bounded challenge with no random encounter
  sampling or hidden world actor.
- Generalised `SYS-362`: Gato victory grants the declared 15 Silver Points,
  10 EXP and 1 TP before ordinary fair traversal resumes.
- Generalised `SYS-854`: a ready legal physical or Tech command applies its
  type and target modifiers, reduces HP and settles Gato or party-member defeat.
- New `SYS-970`: total party defeat in the optional Gato challenge closes that
  challenge without Game Over and restores the party at one HP for continued
  fair traversal or retry.
- New `SYS-971`: when the ordered Telepod/Pendant prerequisites hold, the
  mechanism creates a Gate, removes the first traveller and then relocates the
  second traveller to the authored corresponding place in another era.
- Resolution order: current field interaction starts Gato; actor-local gauges
  schedule commands; damage settles the challenge; victory grants fair and
  progression currency; a priced booth interaction converts part of that fair
  currency; the remaining fair gates enable the demonstration; Pendant
  reaction creates the Gate; the retained Pendant and second activation move
  Crono to 600 A.D.
- Claims: `CT-003`–`CT-009`.

### Constraint Genes

- `CON-136`: the money exchange requires sufficient Silver Points, and the
  second Gate transit requires every earlier fair, demonstration, Pendant and
  local mechanism state.
- `CON-269`: Tech, Combo and item commands require ready actors, sufficient MP
  or stock, an available learned command and legal target.
- `CON-282`: Marle meeting, returned Pendant, party join, fair readiness,
  candy, Crono demonstration, Marle demonstration, dropped-Pendant retrieval
  and Crono transit are ordered authored gates.
- Generalised `CON-323`: Gato's active party is bounded by the currently
  recruited and story-available roster; on this route that is Crono plus Marle,
  while her departure removes her before Crono's transit.
- Scarce route state: party HP/MP, actor readiness, item stock, Silver Points,
  G, EXP/TP credit, Marle party state, fair-ready flag, demonstration state,
  Pendant ownership and Gate phase.
- Claims: `CT-003`, `CT-006`–`CT-009`.

### Information Genes

- Generalised `INF-119`: the battle and menu surfaces expose party HP, MP,
  Battle Gauge readiness, learned Techs, item stock, EXP/TP context and current
  currency balances needed by the admitted decisions.
- Generalised `INF-179`: each current field exposes Crono, Marle, Gato, booths,
  people, pickup, Telepods and exits required to choose the next movement,
  interaction or battle action.
- Claims: `CT-002`–`CT-006`, `CT-008`.

### Objective Genes

- New `OBJ-203`: complete one authored festival opening by forming the initial
  party, settling its declared challenge and currency exchange, then resolving
  a key-item mechanism incident so ordinary control resumes in the declared
  corresponding location of another era.
- Success is not Gato victory, the exchange, Marle's disappearance or Gate
  creation alone. The second transit must settle and restore ordinary 600 A.D.
  control; Gato defeat is recoverable and therefore not a route terminal.
- Claims: `CT-004`–`CT-009`.

### Time Genes

- Generalised `TIM-026`: Gato and each current party member advance a personal
  Battle Gauge; one ready party actor accepts a command while other readiness
  and queued effects follow the selected `Wait` pause policy.
- Claims: `CT-003`, `CT-004`.

## Reproducible transitions

| Before | Action | Deterministic or bounded resolution | Establishes | Claim |
|---|---|---|---|---|
| Fresh opening has restored bedroom control | walk downstairs, answer the required naming exchange, speak again and leave | the mother interaction records Lucca's default name, offers 200 G and opens ordinary 1000 A.D. landscape traversal | reproducible entry and field/map interaction | `CT-002` |
| Marle has collided with Crono and her Pendant lies nearby | speak to Marle first, collect the Pendant, return it and accept her request | Marle enters the recruited and active party, making her personal battle commands available | authored roster change | `CT-007` |
| Crono and Marle stand beside visible Gato | accept Gato's challenge | the recruited party enters one bounded command battle and personal Battle Gauges begin filling | visible authored encounter | `CT-003`, `CT-004` |
| One party actor's gauge is full and Gato remains active | choose a legal Attack or available Tech and target Gato | the command resolves bounded damage; Gato and the other actor continue on their own readiness schedules | actor-local party command | `CT-003`, `CT-004` |
| Gato's HP reaches defeat | accept encounter settlement | ordinary fair control resumes and the party receives 15 Silver Points, 10 EXP and 1 TP | challenge reward and fair currency | `CT-004` |
| Both active party members instead reach zero HP | accept challenge loss | no route Game Over occurs; the party returns to fair traversal at one HP and may retry | non-terminal sparring defeat | `CT-005` |
| At least 10 Silver Points are carried at the money tent | confirm one exchange | exactly 10 Silver Points are spent and 50 G is added; five Silver Points remain after one Gato victory | fixed fair-to-general currency conversion | `CT-006` |
| Fair readiness is announced and Marle is present | wait for candy, reach the Telepods and let Crono test the machine | the ordinary demonstration transfers Crono between the two pads and preserves the later Marle interaction | ordered demonstration gate | `CT-008` |
| Marle enters the Telepod with her Pendant | accept the authored activation | the Pendant reacts, a Gate appears, Marle is removed through it and the Pendant remains as a reachable world object | key-item mechanism incident | `CT-007`, `CT-008` |
| The dropped Pendant is reachable and the Gate incident persists | collect it and accept Crono's Telepod activation | Crono traverses the Gate; ordinary control resumes beside its Truce Canyon endpoint in 600 A.D. before the first enemy trigger | scoped positive terminal | `CT-009` |

## Strategic and experiential structure

- Local decision: choose the next visible actor or mechanism, and in Gato's
  battle choose which ready party member acts, which available command is worth
  its MP/item cost and which legal target receives it.
- Medium-term planning: obtain a sufficient fair balance from a visible,
  recoverable challenge, convert only the required amount and preserve the
  ordered social/mechanism flags that make the demonstration and Pendant
  reaction available.
- Long-term structure: the packet starts as ordinary town/fair navigation,
  proves a two-person ATB command loop, changes encounter rewards into a second
  currency, then turns the same interaction vocabulary into a key-item-driven
  relocation across authored eras.
- Common heuristics: return the Pendant after speaking to Marle; use ordinary
  attacks rather than spending scarce items against Gato; retry after the
  non-terminal one-HP loss; exchange exactly once; wait for candy; collect the
  dropped Pendant before activating the second transit.
- Failure attribution: battle gauges, HP/MP, command availability, reward text,
  booth balances, Marle party state, Pendant position and Gate presentation
  distinguish readiness, survival, reward, transaction and prerequisite
  failures. No hidden random encounter controls this route.
- Claims: `CT-002`–`CT-010`.

## Replay and variation

- What changes between attempts: command order, damage, remaining HP/MP,
  challenge retries, exact movement time and optional unused inventory.
- Randomness or procedural generation: the world, fair, Gato, exchange rate,
  Telepod sequence and era destination are authored; combat damage contains
  bounded variance.
- Multiple viable strategies: basic attacks, available Techs and restorative
  items can all change the Gato resource profile. The accepted route requires
  one victory and one exchange, not a particular command string.
- Typical replay motive: different fair conduct, more Silver Points, other
  prizes, faster opening time or later trial consequences. Those goals are
  excluded rather than treated as part of this terminal.
- Claims: `CT-003`–`CT-010`.

## Adjacent systems and history

- Final Fantasy VII also schedules independent party and enemy readiness before
  commands. Chrono Trigger's admitted packet instead joins a recoverable
  optional fair challenge, event currency and a key-item time transition; it
  has no sampled field encounters, Materia build or timed evacuation.
- Pokémon Red Version shares direct overworld navigation, a recruited battle
  roster, command targeting and encounter rewards. Its scoped battles use
  alternating paired commands and Speed priority, not concurrently filling
  personal gauges, and its route has no authored era relocation.
- The Secret of Monkey Island also advances through ordered world interactions
  and inventory state, but its scoped trial is self-paced verb-object puzzle
  dependency with no health, party command battle or live readiness.
- Later Chrono Trigger releases, translations and audiovisual additions may
  preserve much of the route, but no parity is inferred for their executable,
  input, timing, content or presentation.
- Claims: `CT-001`, `CT-003`–`CT-010`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-019`, `ACT-130`, `ACT-341` | names, Gato, booth and Telepod identities are parameters |
| System Behaviour | `SYS-355`, `SYS-362`, `SYS-854`, `SYS-970`, `SYS-971` | HP, damage, 15 SP, 10 EXP, 1 TP, 10 SP and 50 G are parameters |
| Constraint | `CON-136`, `CON-269`, `CON-282`, `CON-323` | roster, fair flags, item stock, MP and Pendant are parameters |
| Information | `INF-119`, `INF-179` | HUD, menu, scene art and literal labels are presentation/parameters |
| Objective | `OBJ-203` | fair, challenge, transaction, era and destination are parameters |
| Time | `TIM-026` | Wait mode and Battle Gauge speed are parameters |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `345` (`GAME-0001`–`GAME-0345`).
- Exact genome matches: none.
- Tied near matches: `GAME-0338` — Final Fantasy VII (`10 / 25 = 0.400000`).
- Supported combination subsets: none.
- Scan date: 2026-09-21.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0338` — Final Fantasy VII | `ACT-008`, `ACT-019`, `ACT-341`, `SYS-362`, `SYS-854`, `CON-269`, `CON-282`, `CON-323`, `INF-119`, `TIM-026` | Both packets traverse authored fields, command a recruited party through concurrent actor-local readiness and resolve a bounded encounter with rewards and ordered gates. Final Fantasy VII derives commands from Materia, carries damage across encounters and closes a bomb-triggered reverse evacuation. Chrono Trigger instead contains a retryable fair challenge, a fixed Silver Point exchange and a Pendant-created Gate that removes one companion before relocating Crono to 600 A.D. | Near, `10 / 25 = 0.400000` |

### Preserved research notes

- New genes: `SYS-970`, `SYS-971` and `OBJ-203`.
- Classification result: `New genes`.
- Evidence and reasoning: field navigation, party commands, encounter rewards,
  contextual interactions, priced acquisition, ordered gates, party bounds,
  field/HUD disclosure and actor-local readiness all transfer from lower-ID
  records. Recoverable one-HP challenge defeat, a prerequisite-driven
  cross-era mechanism transition and the complete festival-to-era objective do
  not match a lower-ID boundary.

## Taxonomy impact

- Registry changes: append three independently evidenced Active boundaries;
  add Chrono Trigger as supporting evidence to the reused genes where wording
  remains unchanged; generalise four evidence lists without changing their
  operational definitions.
- Taxonomy-change record:
  [`TAXONOMY_CHANGE_088`](../../../research/taxonomy-changes/TAXONOMY_CHANGE_088.md).
- Candidate terms affected: Crono, Marle, Gato, Silver Points, G, Telepod,
  Pendant, Gate, Leene Square, Truce Canyon and era labels remain parameters.

## Negative results

- No direct play, ROM execution, disassembly verification, frame capture,
  controller trace, installed-build hash, screenshot, video or audio evidence.
- The written sources establish the route and fixed values but do not justify
  undocumented damage formulae, frame timings, exact collision rectangles or
  RNG internals; none are claimed.
- No random encounter, Truce Canyon battle, saved state, later party member,
  Dual/Triple Tech progression, magic, world-map epoch selection or campaign
  ending enters the signature.
- Silver Points and G are not separate genes, nor are Gato, the candy wait,
  Telepod pads, Pendant or the years 1000/600. Their causal roles are captured
  by transaction, dependency, party, transition and objective boundaries.

## Delta summary

## New facts

- [Observation | Corroborated | High] A visible optional fair battle pays 15
  Silver Points, 10 EXP and 1 TP on victory but returns a defeated party at one
  HP instead of ending the route (`CT-004`, `CT-005`).
- [Observation | Corroborated | High] One fixed 10-SP exchange leaves five and
  adds 50 G before the Pendant-gated Telepod incident restores control in 600
  A.D. (`CT-006`, `CT-008`, `CT-009`).

## New genes

- [Observation | Corroborated | High] Three boundaries isolate non-terminal
  challenge defeat, an authored cross-era mechanism transition and the complete
  festival-to-era retained-control objective.

## New combinations

- [Observation | Corroborated | High] No verified combination is expected;
  deterministic subset validation remains required.

## Taxonomy changes

- [Observation | Direct/Corroborated | High] Three Active boundaries are
  appended and reused evidence is added without changing earlier signatures or
  lifecycle states.

### Added

- `GAME-0346` as one original-SNES Millennial Fair, Gato, exchange and first
  Gate-transition packet.
- `SYS-970`, `SYS-971` and `OBJ-203`.

### Reused

- `ACT-008`, `ACT-019`, `ACT-130`, `ACT-341`, `SYS-355`, `SYS-362`,
  `SYS-854`, `CON-136`, `CON-269`, `CON-282`, `CON-323`, `INF-119`,
  `INF-179` and `TIM-026`.

### Generalised

- Evidence lists for `ACT-130`, `SYS-355`, `CON-323`, `INF-119` and `INF-179`
  admit the exact supported carrier without altering their definitions.

### Rejected

- Separate genes for each fair minigame, the 15/10/50 values, names, robot,
  candy pause, companion follow animation, Telepod pad, Pendant, Gate colour,
  era label, arrival cutscene and first canyon encounter.

### Preserved

- Every lower-ID signature, lifecycle state, verified combination and family
  definition.
