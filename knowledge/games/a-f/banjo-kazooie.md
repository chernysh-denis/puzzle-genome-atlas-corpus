---
game_id: GAME-0386
slug: banjo-kazooie
game_title: Banjo-Kazooie
analysis_status: reviewed
reviewed: 2026-09-24
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-161
    - ACT-341
  system:
    - SYS-036
    - SYS-037
    - SYS-398
    - SYS-578
    - SYS-1042
    - SYS-1043
    - SYS-1044
  constraint:
    - CON-349
    - CON-440
    - CON-691
  information:
    - INF-207
    - INF-268
  objective:
    - OBJ-228
  time:
    - TIM-003
---

# Game: Banjo-Kazooie

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Banjo, Kazooie,
Bottles, Mumbo, Jinjos, Jiggies, Notes and named moves are carrier parameters,
not separate genes.

## Analysis scope

- Version / ruleset: original North American English Nintendo 64 rules of
  1998, represented in the licensed Nintendo 64 – Nintendo Switch Online
  library on Switch, ordinary unmodified new save. The original N64
  pickup-persistence rule is reconstructed from N64 sources, not directly
  confirmed in an installed Switch wrapper; Xbox and native-port behaviour
  is not transferred.
- Structured analysis target: the licensed original-N64 presentation carried
  by Switch Online in
  [`knowledge/platforms/games.json`](../../platforms/games.json).
- Setup: complete Spiral Mountain's necessary basic training, collect the first
  lair Jiggy, place it in Mumbo's Mountain's one-piece picture, and enter that
  world for the first time. This setup is specified, not counted as the
  packet's collection objective.
- Primary decision loop: inspect the reachable terrain, molehill instruction,
  visible pickup or reward condition; steer and jump the bear-and-bird body,
  learn and apply the current move, collect a Jiggy, Note, Jinjo or Mumbo token,
  or resolve an authored fixture; then revisit the now-legal branch while
  preserving health and the first-visit Note tally.
- Entry: first ordinary control inside Mumbo's Mountain after its one-Jiggy
  picture has opened, with no pre-collected world Jiggies, Notes or Jinjos and
  no imported Mumbo tokens or learned world-specific moves.
- Fixed accepted route: learn Egg Firing, Talon Trot and Beak Buster at the
  world's Bottles molehills; use eggs on Conga/JuJu, Talon Trot on steep
  slopes and Beak Buster on huts and Witch Switch; resolve the authored
  Conga, Chimpy, JuJu, huts and five-Jinjo rewards; collect five Mumbo tokens,
  including the fifth reachable inside the termite mound before transforming;
  pay Mumbo, become a termite, collect the mound-top Jiggy and remaining Notes.
  Leave through the physical exit pad after reaching ten world Jiggies and a
  100-Note first-visit best; collect the Witch-Switch-revealed lair Jiggy,
  pass the first 50-Note door, place two available Jiggies into the Treasure
  Trove Cove picture and reach the newly opened world entrance. Stop before
  entering Treasure Trove Cove.
- Positive terminal: the next world's entrance is physically open and
  reachable in the lair after both the Note Door and two-piece picture gates;
  the bounded first-world collection controls have also been met. The game
  requires only the relevant 50-Note threshold and two Jiggies to unlock that
  successor; ten world Jiggies and 100 Notes are this study packet's stricter
  route checkpoints, not an invented admission rule.
- Negative / recovery branches: health segments can be lost to enemies, unsafe
  terrain or falls and restored by honeycombs. Death or leaving an original
  N64 world respawns individual Notes, while the best world Note score remains
  recorded; such an interruption fails this single-visit 100-Note route and
  requires a fresh collection pass. Fewer than five Mumbo tokens cannot buy
  the termite form; fewer than 50 recorded Notes cannot pass the first Note
  Door; an unfilled two-piece picture cannot open the successor.
- Included: third-person movement and gravity/collision; three world-taught
  moves and their local uses; contact pickups and Jinjo-set reward; token-paid
  temporary termite form and its steep-slope access; live honeycomb health;
  original N64 best-Note versus respawned individual-Note state; distinct Note
  threshold and Jiggy-placement gates; world and lair totals UI.
- Excluded: later worlds, flight and Shock Spring training, later Mumbo forms,
  complete campaign, hidden Stop 'n' Swop collection, cheats, speedrun skips,
  exact enemy-hit timing, optional hollow-honeycomb maximum-health extension,
  and any assertion of Xbox remaster persistence rules.
- Reproducible parameterisation: identify original N64 carrier and fresh save;
  record molehill lessons, move legality, each world Jiggy/Jinjo/Note count,
  five-token threshold, form before/after Mumbo, exit-pad transition, recorded
  best Note score, lair Jiggy stock, picture fill and reachable successor.
  This is a cited state reconstruction, not a local controller trace.
- Potential scoped modules: Treasure Trove Cove's flight and spring-pad
  lessons, the later multiworld Note-door economy and the full witch finale.
- Direct-play status: none. The original manual transcription and two
  original-N64 written routes were read as text. No cartridge, console,
  emulator, ROM, save, input trace, screenshot, video or audio was inspected.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `BK-001` | The original manual separates lair jigsaw-picture doors from Note Doors and states that pictures consume placed Jiggies while Note Doors test collected totals | Confirmed | Direct | High | P1 |
| `BK-002` | Bottles teaches named moves at molehills; Talon Trot climbs steeper slopes, Beak Buster strikes down, and Egg Firing spends collected blue eggs | Confirmed | Direct | High | P1 |
| `BK-003` | Mumbo's first-world termite form requires five tokens and gives an altered traversable body; the fifth token is reachable inside the mound before paying | Observation | Corroborated | High | P1, S1 |
| `BK-004` | Ten Jiggies and 100 Notes exist in Mumbo's Mountain; all ten Jiggies and 100 Notes can be collected on the first continuous visit via the cited route | Observation | Corroborated | High | P1, S1 |
| `BK-005` | Releasing all five world Jinjos awards one world Jiggy | Confirmed | Direct | High | P1 |
| `BK-006` | Conga orange pads, Chimpy's orange, egg hits, JuJu mouths, breakable huts and steep slopes yield distinct first-world rewards after their authored conditions | Observation | Corroborated | High | S1, S2 |
| `BK-007` | The first Note Door asks for 50 Notes and the Treasure Trove Cove picture takes two Jiggies; the latter world can be opened without a ten-Jiggy or 100-Note requirement | Confirmed | Corroborated | High | P1, S1, S2 |
| `BK-008` | In original N64 play, exiting or dying respawns individual Notes but retains the best recorded world Note score for later door checks | Observation | Corroborated | High | S2, S3 |
| `BK-009` | Honeycomb health is damaged by hostile contact, unsafe ground and falls and is restored by honeycomb pickups | Confirmed | Direct | High | P1 |
| `BK-010` | No original N64 executable or audiovisual play trace was locally inspected | Observation | Direct | High | R1 |

## Basic data

- Release / origin: Rare developed and Nintendo published the original N64
  release in 1998; the selected packet is the North American English retail
  ruleset, not the current Xbox distribution linked below.
- Platform or physical form: licensed Nintendo 64 – Nintendo Switch Online
  application presenting the N64 game; the structured `analysisTarget`
  records that carrier without claiming a wrapper version or direct play.
- Puzzle family: traversal and spatial gating; ordered dependency sequencing;
  collection and resource gates.
- Primary source, checked 2026-09-24:
  - **[P1]** [original North American Nintendo 64 instruction booklet,
    transcribed](https://world-of-nintendo.com/manuals/nintendo_64/banjo-kazooie.shtml),
    pp. 8–20 and 26–27, for controls, lessons, Notes/Jiggies/Jinjos,
    Mumbo tokens, picture placement, Note Doors and health. Its transcription
    explicitly identifies a printed pause-menu exit option as removed from
    the final game; this route uses the physical exit pad, not that option.
- Reproducible original-N64 written routes, checked 2026-09-24:
  - **[S1]** [me_frog's N64 route](https://gamefaqs.gamespot.com/n64/196694-banjo-kazooie/faqs/29761),
    sections `GL01`, `MM01`, `GL02`, for the first-world move/reward order,
    fifth token before transformation, ten Jiggies, 100 Notes, exit pad and
    successor picture.
  - **[S2]** [JMendes's N64 guide](https://gamefaqs.gamespot.com/n64/196694-banjo-kazooie/faqs/3143),
    for the first 50-Note Door and independent world-collectible accounting.
  - **[S3]** [DonkeyKongSong's original-N64 route](https://gamefaqs.gamespot.com/n64/196694-banjo-kazooie/faqs/11906),
    for best-world-Note score versus reappearing individual Notes.
- Official licensed destination: [Xbox Banjo-Kazooie product
  listing](https://www.xbox.com/en-us/games/store/BanjoKazooie/BT3L7MVTD4QF),
  offered as a legal product link only; its build is not the analysed carrier.
- Nintendo's [licensed Switch Online release
  announcement](https://www.nintendo.com/en-ca/whatsnew/banjo-kazooie-arrives-on-nintendo-switch-online-expansion-pack-today-with-the-legend-of-zelda-majoras-mask-up-next/)
  establishes the selected distribution, not mechanical parity of every
  emulation convenience.
- **[R1]** Local evidence boundary: no measured frame timing, cartridge bytes
  or direct play is claimed.
- Claim IDs: `BK-001`–`BK-010`.

## Mechanical decomposition

### Action Genes

- `ACT-008`: steer, jump, climb, swim and traverse reachable world/lair paths.
- `ACT-161`: fire aimed eggs at Conga/JuJu or strike eligible hostile and
  breakable structures with the current taught move.
- `ACT-341`: address Bottles's molehill, Chimpy, Mumbo's pad, Witch Switch,
  picture pad and exit pad when their authored prerequisites hold.
- Parameters: selected move, reach, aim, egg stock, terrain and fixture.
- Claim IDs: `BK-002`, `BK-003`, `BK-006`, `BK-007`.

### System Behaviour Genes

- `SYS-036`: movement follows live jump/fall and collision geometry.
- `SYS-037`: touching Notes, Jiggies, tokens and Jinjos credits eligible
  pickups while movement continues.
- `SYS-398`: each Bottles lesson retains a named usable move on the save.
- `SYS-578`: hostile contact and falls deplete honeycomb health; energy pickups
  refill it before a terminal depletion.
- `SYS-1042`: paying an authored token cost at Mumbo's pad changes the player
  into a spatially bounded alternate form, then restores the bear-and-bird
  body on expiry or return.
- `SYS-1043`: preserve the best original-N64 world Note tally while
  respawning individual Notes on a later visit/death.
- `SYS-1044`: releasing every distinct member of a world Jinjo group emits
  its one Jiggy reward, independent of raw Note count.
- Resolution order: reach taught move → use it to reach token/reward state →
  five-token payment → termite-accessible mound reward → exit-record best
  Notes → Note Door threshold → two-piece picture completion.
- Claim IDs: `BK-002`–`BK-009`.

### Constraint Genes

- `CON-349`: steep edges and breakable-hut/Witch-Switch operations require
  their learned compatible move and proper local input.
- `CON-440`: the first Note Door remains closed until the recorded Note total
  reaches its 50-Note threshold. Notes are a retained qualifying measure here,
  not currency paid into the door.
- `CON-691`: each world picture requires enough unallocated Jiggies to fill
  its addressed slots; the two pieces allocated to Treasure Trove Cove's
  picture are not the Note Door's 50-Note check.
- Scarce strategic resources: blue-egg ammunition and five tokens spent on
  Mumbo; neither is a time limit. The route's ten Jiggies/100 Notes are
  research checkpoints, not game-required successor prices.
- Claim IDs: `BK-001`–`BK-004`, `BK-007`, `BK-008`.

### Information Genes

- `INF-207`: the totals and marked first Note Door disclose current Note
  progress and the next threshold-gated lair region.
- `INF-268`: Bottles's molehill supplies the current move input and its
  immediately relevant world affordance.
- The manual's `View Totals` reports Jiggies and Notes; Mumbo's sign displays
  the current token price. These are visible parameters, not an external
  walkthrough or a universal future-gate map.
- Claim IDs: `BK-001`, `BK-002`, `BK-003`, `BK-007`.

### Objective Genes

- `OBJ-228`: finish the declared first-world collection packet and open the
  physically reachable next world by satisfying its distinct Note Door and
  Jiggy-picture gates. The first-world full-collection packet is stricter than
  the minimum successor admission condition.
- Success, evaluation and failure: world totals, retained best Note score and
  picture fill are observable. A first-visit death breaks the 100-Note
  collection control but need not permanently prevent unlocking the successor.
- Claim IDs: `BK-004`, `BK-007`, `BK-008`.

### Time Genes

- `TIM-003`: movement, hostiles, falling and hit risks advance during live
  control. Paused menu reading does not impose an independent puzzle deadline.
- Claim IDs: `BK-002`, `BK-009`.

## Reproducible transitions

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| First entry, no world moves | Address each relevant Bottles molehill | Egg Firing, Talon Trot and Beak Buster become retained legal commands | Learning precedes corresponding route edges | `BK-002` |
| Conga's orange pad active | Stand on pad, then dodge the thrown orange | The orange strikes its switch; completing the authored pad group emits one Jiggy | Luring an enemy projectile differs from shooting it | `BK-006` |
| Egg Firing learned, blue eggs stocked | Aim eggs at Conga or JuJu's exposed mouth | Authored hit count or group condition yields a Jiggy | Ammo-backed aimed attack resolves separate fixture gates | `BK-002`, `BK-006` |
| Beak Buster learned | Ground-strike a village hut and Witch Switch | Hut contents become accessible; the switch reveals a lair Jiggy | One learned move serves object and remote-reward affordances | `BK-002`, `BK-006` |
| Four Jinjos credited | Touch the fifth distinct world Jinjo | The completed five-member group awards its one Jiggy | Set completion is not a generic note threshold | `BK-005` |
| Four Mumbo tokens and normal form | Enter the termite mound as Banjo/Kazooie and Talon Trot to token five | Payment becomes possible before transformation | The fifth token is not behind its own cost gate | `BK-003` |
| Five tokens, Mumbo pad reached | Pay Mumbo and activate pad | The temporary termite body can climb mound slopes; it reaches the final Note/Jiggy | A priced form changes reachable geometry | `BK-003`, `BK-004` |
| First-visit 100 Notes credited | Leave through the world's physical exit pad | Best Note tally is recorded; a later entry can respawn individual Notes without erasing the best | Original N64 best score differs from permanent pickup flags | `BK-008` |
| Best Notes below 50, then at least 50 | Approach first lair Note Door | Initially blocked; after threshold it opens without consuming Notes | The Note gate is a check, not a purchase | `BK-001`, `BK-007` |
| Treasure Trove Cove picture has zero of two slots | Place two available Jiggies at its pad | The picture fills and opens the next entrance; reaching it closes the packet | This is a separate allocative gate | `BK-001`, `BK-007` |

## Strategic and experiential structure

- Local decision: identify whether a visible reward needs traversal, a learned
  attack, a five-member rescue set or a paid alternate form.
- Medium-term planning: collect five tokens before Mumbo; finish Notes in one
  N64 visit if pursuing the packet's 100-Note checkpoint.
- Long-term structure: collection earns enough stock for separate lair gates;
  world completion and successor eligibility are not the same predicate.
- Common heuristic: take Bottles lessons when encountered, test their nearby
  authored affordance, and record which Jiggies/Notes remain before exiting.
- Failure attribution: an interrupted N64 Note sweep requires re-collection
  for a better score; it does not erase already earned world Jiggies.
- Player-trust factors: the 50 on the Note Door, Mumbo's token-price sign,
  picture holes and totals make the relevant gates inspectable.
- Claim IDs: `BK-001`–`BK-009`.

## Replay and variation

- What changes between attempts: pickup order, incidental damage, egg use,
  current Note tally, last best Note score and collected Jiggy stock.
- Randomness or procedural generation: this fixed first world and its authored
  reward locations are not a randomised level; enemy timing is a live-state
  parameter, not a procedurally new puzzle.
- Multiple viable strategies: alternate reward order and more-than-minimum
  Note/Jiggy stock can reach the successor; the cited route fixes one
  reproducible full-world sample without claiming it is the sole solution.
- Typical replay motive: improve the original N64 best Note score or gather
  remaining world collectibles after an interrupted visit.
- Claim IDs: `BK-004`, `BK-007`, `BK-008`.

## Adjacent systems and history

- Direct predecessors: authored 3D platform stages and permanent move unlocks
  provide context, but no predecessor identity is needed for a gene claim.
- Variants: Xbox and later rereleases should be separately checked for Note
  persistence before copying this original-N64 genome.
- Similar games: Psychonauts shares direct movement, live physics, health,
  contact pickups and training; Super Metroid shares retained ability gates.
- Important differences: the two lair gates use different collection
  semantics, and the termite's paid temporary body is neither a permanently
  learned move nor a picked-up Mario power state.
- Claim IDs: `BK-001`–`BK-009`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-161`, `ACT-341` | Named moves, world fixtures |
| System Behaviour | `SYS-036`, `SYS-037`, `SYS-398`, `SYS-578`, `SYS-1042`, `SYS-1043`, `SYS-1044` | Token cost, Note best, Jinjo set |
| Constraint | `CON-349`, `CON-440`, `CON-691` | Five tokens, 50 Notes, two picture slots |
| Information | `INF-207`, `INF-268` | Totals, price sign, molehill hint |
| Objective | `OBJ-228` | Full first-world packet, open next entrance |
| Time | `TIM-003` | Live movement and hazards |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `385` (`GAME-0001`–`GAME-0385`).
- Exact genome matches: none.
- Tied near matches: `GAME-0358` — Psychonauts (`8 / 26 = 0.307692`).
- Supported combination subsets: none.
- Scan date: 2026-09-24.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0358` Psychonauts | `ACT-008`, `ACT-161`, `ACT-341`, `SYS-036`, `SYS-037`, `SYS-578`, `INF-268` and `TIM-003` cover direct traversal, aimed strikes, authored interactions, contact pickups, health, instruction and live movement. | Psychonauts uses figment rank, matched baggage and finite astral layers in a linear training course. Banjo-Kazooie uses a purchased termite form, a best-Note record that outlives respawned objects, a five-Jinjo reward and distinct Note/picture gates; neither game's collectible terminal transfers. | `8 / 26 = 0.307692`; tied near maximum, not an equivalent first-world training loop |

### Preserved research notes

- New genes: `SYS-1042`, `SYS-1043`, `SYS-1044`, `CON-691`, `OBJ-228`.
- Reused genes: `ACT-008`, `ACT-161`, `ACT-341`, `SYS-036`, `SYS-037`,
  `SYS-398`, `SYS-578`, `CON-349`, `CON-440`, `INF-207`, `INF-268`, `TIM-003`.
- Classification result: five source-bounded first-world distinctions.

## Taxonomy impact

- `TAXONOMY_CHANGE_125` accepts five additive first-world distinctions.
- No earlier game signature, gene lifecycle, family definition or verified
  combination changes in this unit.

## Negative results

- Do not classify this first-world packet as complete campaign rescue of Tooty.
- Do not treat the study's 100-Note/ten-Jiggy checkpoints as necessary to
  enter Treasure Trove Cove; the successor's gate is 50 Notes and two placed
  Jiggies.
- Do not infer the printed but removed pause-menu exit option exists in the
  final cartridge; use the exit pad.
- Do not infer the fifth token is unreachable before the termite form; the
  original-N64 route gets it inside the mound as Banjo/Kazooie.
- Do not treat original-N64 best-Note persistence as permanently removed
  individual Note objects or as Xbox remaster save behaviour.

## Delta summary

## New facts

- [Confirmed | Corroborated | High] The original manual and N64 route support
  distinct Note-total and filled-picture access gates, a five-token termite
  transformation and a first-visit full-world sweep (`BK-001`–`BK-008`).

## New genes

- [Observation | Corroborated | High] `SYS-1042`, `SYS-1043`, `SYS-1044`,
  `CON-691` and `OBJ-228` isolate the paid form, N64 best-Note persistence,
  all-Jinjo reward, allocative picture and bounded successor terminal.

## New combinations

- [Observation | Corroborated | High] No verified combination is registered.

## Taxonomy changes

- [Observation | Corroborated | High] `TAXONOMY_CHANGE_125` adds five
  source-bounded genes without changing older signatures.

## New questions

- Would direct original-N64 cartridge tracing show any region/build-specific
  differences in Note best recording or the termite-form expiry boundary?
- Which optional ordering of first-world rewards minimises revisits while
  preserving the single-visit 100-Note control?

## Next recommended game

- [Hypothesis | Limited | Medium] GAME-0387 Super Bomberman.
- Optimisation criterion: alternate a three-dimensional collect-and-transform
  platform route with a compact tile-grid explosive contest.
- Expected information gain: timed blast propagation, destructible terrain
  and local opponent elimination.
- Backlog impact: preserves the selected nine-game order; no next unit starts
  in this commit.

## Why this game

- [Hypothesis | Limited | Medium] The first world exposes the otherwise easy
  to conflate difference between repeated note-score thresholds, paid
  alternate-form access and an addressed Jiggy picture.
