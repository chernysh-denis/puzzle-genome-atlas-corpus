---
game_id: GAME-0363
slug: the-legend-of-zelda-ocarina-of-time
game_title: "The Legend of Zelda: Ocarina of Time"
analysis_status: reviewed
reviewed: 2026-09-22
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-161
    - ACT-164
    - ACT-199
    - ACT-341
    - ACT-437
    - ACT-494
  system:
    - SYS-037
    - SYS-045
    - SYS-215
    - SYS-379
    - SYS-578
    - SYS-605
    - SYS-931
    - SYS-994
  constraint:
    - CON-175
    - CON-282
  information:
    - INF-073
    - INF-128
    - INF-179
    - INF-356
    - INF-372
  objective:
    - OBJ-210
  time:
    - TIM-003
---

# Game: The Legend of Zelda: Ocarina of Time

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Link, Navi,
Kokiri Forest, the Great Deku Tree, Queen Gohma, Deku Shield, Fairy Slingshot
and Kokiri's Emerald are carrier parameters, not gene names.

## Analysis scope

- Version / ruleset: original English Nintendo 64 *The Legend of Zelda:
  Ocarina of Time* (1998) rules, represented by Nintendo's N64 Classics
  offering through Nintendo Switch Online + Expansion Pack. This is not the
  separately announced Switch 2 remake, 3DS version or Master Quest.
- Structured analysis target: the N64-original rules accessed through
  Nintendo 64 – Nintendo Classics; see `GAME-0363` in
  [`knowledge/platforms/games.json`](../../platforms/games.json). Wrapper
  suspend points, rewind and controller remapping are excluded.
- Primary decision loop: inspect the contextual A icon, Navi focus, equipment
  and current room; move or Z-target an eligible actor; raise the shield or
  aim the currently assigned item; activate a nearby object, switch or door;
  read the changed dungeon map and route flag; survive live hostiles and use
  newly acquired tools to reach the boss; stun Gohma's vulnerable eye,
  strike while she is down, exit and receive the first Spiritual Stone.
- Entry: a fresh file before ordinary control in Kokiri Forest, with Link
  still lacking the Kokiri Sword, Deku Shield, Fairy Slingshot and ocarina.
- Positive terminal: Queen Gohma is defeated, the blue boss exit is used,
  the Great Deku Tree's post-dungeon exchange grants Kokiri's Emerald, its
  first-Stone mark is retained in Quest Status and ordinary forest control
  returns **before Link leaves Kokiri Forest**. Merely defeating Gohma is
  insufficient.
- Negative terminal: health reaches zero and Game Over appears. Continue and
  save semantics after that point are not analysed.
- Reproducible route: acquire and equip the Kokiri Sword, collect enough rupees
  for and buy the Deku Shield, pass Mido and enter the Great Deku Tree; take
  the Dungeon Map; reflect the first Deku Scrub's nut with a held shield and
  speak to it; collect and assign the Fairy Slingshot; shoot down the exit
  ladder and the vine-blocking Skullwalltulas; collect the Compass; use a lit
  Deku Stick to open the barred route, fall through the central web, trigger
  the lower water switch, shoot the eye switch, move a block and burn the
  final web; reflect the three Scrubs' shots in their disclosed `2-3-1` order;
  shoot Gohma's red eye with the slingshot, hit her while stunned, take the
  Heart Container, use the blue exit and accept the Emerald.
- Included: child Link's direct three-dimensional movement and automatic gap
  jump; context-dependent A interactions; Z-target focus and relative
  movement; sword, held Deku Shield, Fairy Slingshot and finite Deku Seeds;
  Navi prompt; heart health and compatible hearts; authored room, switch,
  ladder, torch, web, water and block gates; Map and Compass disclosure;
  ordinary dungeon enemies; Gohma's eye cue, stun, larvae and live attack;
  boss exit, giver dialogue, Emerald and retained Quest Status.
- Excluded: small keys and boss keys (the original manual explicitly says
  early dungeons have no small keys), Fairy Ocarina, melodies, Zelda, Hyrule
  Field, adulthood, later dungeons, optional Gold Skulltula collection,
  optional shop optimisation, save-state conveniences, glitches, randomisers,
  3DS/Master Quest and the future Switch 2 remake.
- Potential scoped modules: Saria's Fairy Ocarina and first field exit; one
  later dungeon with actual small keys and boss key; learned melody gates;
  child/adult equipment restrictions; later quest and save persistence.
- Direct-play status: no licensed session, cartridge, installed game, save,
  input trace, screenshot, video or audio was obtained or inspected. The
  official original manual supplies control and interface rules; three
  independently written routes corroborate the first-dungeon transitions.
  The local control is a source-bounded reconstruction, not direct play.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `OOT-001` | Nintendo lists the original N64 adventure in its Switch Online Expansion Pack; the separately announced Switch 2 remake is not this ruleset | Confirmed | Direct | High | P1, P2 |
| `OOT-002` | The original manual defines contextual A commands, Navi focus and Z-targeting, with relative movement and improved aim | Confirmed | Direct | High | P3 |
| `OOT-003` | The original manual defines sword, held shield, C-item assignment, Slingshot ammunition, hearts, Map and Compass disclosure | Confirmed | Direct | High | P3 |
| `OOT-004` | The manual explicitly says small keys do not appear in the earliest dungeons; no key pickup or spend is part of the first Deku Tree route | Confirmed | Direct | High | P3, S1, S2 |
| `OOT-005` | Sword and shield access precede Mido's passage; a reflected Deku Scrub projectile creates the first dialogue and opens the route to the Slingshot | Observation | Corroborated | High | S1, S2 |
| `OOT-006` | The Slingshot lowers the hanging exit ladder and resolves distant spider or eye-switch gates | Observation | Corroborated | High | P3, S1, S2, S3 |
| `OOT-007` | Dungeon Map and Compass are separate retained pickups; the Map reveals the room outline and Compass marks boss and treasure positions | Confirmed | Corroborated | High | P3, S1, S2 |
| `OOT-008` | Torch, web, lower-water, block and `2-3-1` Scrub interactions gate the Gohma route | Observation | Corroborated | High | S1, S2, S3 |
| `OOT-009` | Gohma's exposed red eye can be shot to stun her, enabling sword damage; larvae and renewed movement continue if she survives | Observation | Corroborated | High | S1, S2, S3 |
| `OOT-010` | After boss defeat, the exit returns Link to the Great Deku Tree, who gives the first Spiritual Stone, Kokiri's Emerald, before the later Fairy Ocarina | Observation | Corroborated | High | P3, S2, S3 |
| `OOT-011` | No game execution or audiovisual play trace was used; the deterministic control checks declared transitions only | Confirmed | Direct | High | R1, V1 |

## Basic data

- Release / origin: Nintendo's 1998 Nintendo 64 action-adventure, analysed
  under its original English rules rather than a later remake.
- Platform or physical form: Nintendo 64 original rules through the licensed
  Nintendo 64 Classics service; see the structured platform record.
- Puzzle family: tactical forecast and counterplay; inventory and fixture
  dependencies; world topology and perspective; ordered dependency
  sequencing.
- Primary sources, accessed 2026-09-22:
  - **[P1]** [Nintendo's original-adventure Switch Online
    listing](https://www.nintendo.com/us/whatsnew/explore-some-of-links-earlier-adventures-available-now-with-nintendo-switch-online-and-nintendo-switch-online-expansion-pack/),
    separating the available N64 adventure from other Zelda products.
  - **[P2]** [Nintendo's separately dated Switch 2 remake
    listing](https://www.nintendo.com/pt-pt/Jogos/Jogos-para-a-Nintendo-Switch-2/The-Legend-of-Zelda-Ocarina-of-Time-3115664.html),
    used solely to exclude the later remade rules and features.
  - **[P3]** [Nintendo's preserved English original-N64
    manual](https://www.nintendo.com/eu/media/downloads/games_8/emanuals/nintendo_8/Manual_Nintendo64_TheLegendOfZeldaOcarinaOfTime_EN.pdf),
    illustrated pages 5–6, 9–22 and 29–34: opening and Stone, Z-targeting,
    A icon, movement, shield, items, Map/Compass, early absence of small keys,
    Quest Status and Game Over.
- Independent written route sources, accessed 2026-09-22:
  - **[S1]** [Zelda Universe first-dungeon written
    route](https://zeldauniverse.net/guides/ocarina-of-time/walkthrough/inside-the-deku-tree/),
    for sword/shield gate, Map, Scrub reflection, Slingshot, Compass, lower
    rooms, Gohma and encounter mechanics.
  - **[S2]** [Zelda's Palace first-dungeon written
    route](https://www.zeldaspalace.com/ocarinaoftime/soluce.php?p=2), for
    independent `2-3-1`, eye switch, water switch, boss, Emerald and the later
    Fairy Ocarina boundary.
  - **[S3]** [Z64Central original-N64 first-dungeon
    route](https://z64central.com/walkthrough/deku-tree/), for the map,
    shield, Slingshot, ladders, torch and boss transitions; its future-remake
    callouts are not used as original-rule evidence.
- Research records: **[R1]** local licensed-play preflight found no runnable
  original-game evidence; **[V1]** local deterministic source-bounded control.
- Claim IDs: `OOT-001`–`OOT-011`.

## Mechanical decomposition

### Action Genes

- Existing `ACT-008`: directly walk, run, climb, swim and automatically jump
  reachable local geometry; automatic jumping is a movement parameter, not a
  separate committed jump action.
- Existing `ACT-161`: strike a hostile with the sword or shoot the Slingshot
  at a reachable hostile or eligible breakable target.
- Existing `ACT-164`: assign a carried item to a C slot before using it.
- Existing `ACT-199`: transfer the Kokiri Sword, Deku Shield, Slingshot and
  finite ammunition into compatible inventory/equipment slots.
- Existing `ACT-341`: commit the currently offered OPEN, SPEAK, CHECK, chest,
  block or admitted exit interaction.
- Existing `ACT-437`: actively hold and release the Deku Shield toward the
  incoming Scrub nut; damage prevention and return resolution are system
  effects rather than this command.
- Existing `ACT-494`: hold one Z-target focus and move relative to the locked
  world target during the scoped combat. `ACT-438` is not added separately:
  the same lock includes eligible objects and persons as well as hostiles.
- Parameters: direction, target, range, item slot, guard direction, focus,
  action icon, addressable fixture and ammunition.
- Claim IDs: `OOT-002`, `OOT-003`, `OOT-005`, `OOT-006`, `OOT-009`.

### System Behaviour Genes

- Existing `SYS-037`: compatible hearts and other pickups credit health or
  carried stock on contact.
- Existing `SYS-045` and `SYS-215`: Skulltulas, Scrubs, larvae and Gohma move
  and attack without waiting for a player turn, while directly aimed sword and
  Slingshot exchanges resolve in live time.
- Existing `SYS-379`: the boss and subsequent Great Deku Tree exchange write
  the persistent Emerald and first-Stone quest state.
- Existing `SYS-578`: hits reduce one continuous health pool; compatible
  hearts restore it; zero opens Game Over.
- Existing `SYS-605`: authored room interactions, switches, web and boss gates
  open the next dungeon segment. Small keys are not instantiated in this
  packet despite appearing in the transferable gene's broader parameter set.
- Existing `SYS-931`: the separate Map and Compass pickups expand retained
  dungeon navigation information; Compass also marks treasure locations
  without disclosing their contents.
- New `SYS-994`: the actively raised shield turns a Scrub nut back into its
  source, stunning it and creating a contextual talk opportunity. This is not
  the uncommanded passive shield `SYS-932` from the original NES game.
- Resolution order: obtain equipment; satisfy Mido; enter dungeon; acquire
  Map; reflect-talk to open a route; obtain Slingshot; open ladder and upper
  route; obtain Compass; satisfy torch, fall, water, eye, block, web and ordered
  Scrub gates; expose and defeat Gohma; leave boss room; receive Emerald.
- Parameters: equipment, ammo, health, room flags, switch state, targeted
  source, return projectile, clue prefix, boss eye phase, stun interval,
  remaining health, story token and quest flag.
- Claim IDs: `OOT-003`–`OOT-010`.

### Constraint Genes

- Existing `CON-175`: persistent hearts must remain above zero to complete
  the bounded route; Game Over ends this attempt.
- Existing `CON-282`: sword and shield precede Mido, earlier rooms and tools
  precede later gates, and Gohma defeat precedes Emerald settlement. The
  local `2-3-1` Scrub order is one authored gate parameter, not a new general
  code gene.
- Candidate genes: none. There is no small-key inventory or boss-key gate in
  this first dungeon; transferring that later-series mechanic here would be a
  false positive.
- Scarce strategic resources: heart health, Slingshot Deku Seeds, temporary
  burning-stick duration; an optional Heart Container can raise capacity
  after Gohma but is not a prerequisite for the Emerald.
- Claim IDs: `OOT-004`, `OOT-006`, `OOT-008`–`OOT-010`.

### Information Genes

- Existing `INF-073`: C-slot item, sword, shield and current equipped stock
  are shown before an action.
- Existing `INF-128`: inventory exposes carried tool identity, seed stock and
  compatible equipment.
- Existing `INF-179`: current three-dimensional room view exposes visible
  hostiles, doors, ledges, torches, webs and interactions but not unseen rooms.
- Existing `INF-356`: live room, explored floor, acquired map outline and
  compass boss marker are joined with heart and item state. Key count stays
  zero in this first dungeon.
- New `INF-372`: A-button action text and Navi's triangle/focus cursor expose
  what the same control will do at the currently addressed actor or fixture.
- Candidate genes: none beyond `INF-372`.
- Claim IDs: `OOT-002`–`OOT-008`.

### Objective Genes

- New `OBJ-210`: the first dungeon is complete only after boss-route access,
  Gohma defeat, boss exit and Emerald award by the Great Deku Tree; the next
  region remains outside scope. `OBJ-191` belongs to a fragment contacted
  inside the original NES dungeon and does not fit the separate giver.
- Success, evaluation and failure: the retained Stone indicator and returned
  forest control verify success; boss death alone, a missed post-boss exit or
  health exhaustion do not.
- Claim IDs: `OOT-009`, `OOT-010`.

### Time Genes

- Existing `TIM-003`: hostiles, projectiles, Gohma vulnerability and burning
  stick duration advance while the player moves and chooses commands.
- Candidate genes: none. Wrapper suspend/reload is not an original-game
  timer; no playable ocarina melody appears in this route.
- Claim IDs: `OOT-008`, `OOT-009`.

## Reproducible transitions

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Fresh Kokiri control; sword and shield absent | Take sword, gather rupees, buy/equip shield, approach Mido | Mido's equipment gate admits the Great Deku Tree route | Equipment is a route prerequisite, not decorative loot | `OOT-005` |
| First Scrub's room barred; nut incoming | Face Scrub and hold shield | Eligible nut returns, stuns Scrub; SPEAK becomes legal before stun expires | Active reflected projectile creates a context-dependent gate | `OOT-002`, `OOT-005` |
| Slingshot acquired; exit platform has fallen | Assign Slingshot and shoot hanging ladder | Ladder falls and makes the return route reachable | The acquired item changes authored room topology | `OOT-006` |
| Upper main room; unopened Map and Compass chests | Open each chest, inspect map | Outline and boss/treasure markers appear in retained dungeon display | Two disclosure pickups do not themselves open doors | `OOT-007` |
| Lower route blocked by web, water and eye | Light stick, cross before flame expiry, press submerged switch, shoot eye | Burning removes web; lowered water admits platform crossing; eye opens door | Multiple typed fixtures, not a universal small-key gate | `OOT-004`, `OOT-008` |
| Final Scrubs unhandled | Reflect middle, right, left (`2-3-1`) and speak to the last stunned Scrub | Correct ordered prefix opens the boss door; wrong order does not | The local code is a gate parameter | `OOT-008` |
| Gohma active; red eye exposed | Z-target and shoot eye, then strike while down | Slingshot stuns; sword damages; survival may require another cycle with larvae | Target acquisition, vulnerability and live combat are separate boundaries | `OOT-002`, `OOT-009` |
| Gohma defeated; Emerald not yet awarded | Take Heart Container if desired, enter blue exit, complete Great Deku Tree exchange | Quest Status gains Kokiri's Emerald and forest control returns | The positive terminal follows the separate giver, before the Fairy Ocarina | `OOT-010` |

## Strategic and experiential structure

- Local decision: choose whether to aim, hold guard, move around a Z-locked
  actor, use the offered context action or preserve hearts and ammunition.
- Medium-term planning: acquire the Slingshot before distant switches and
  Skullwalltulas; use Map and Compass to identify progress without mistaking
  information for a door key.
- Long-term structure: the authored first dungeon culminates in a boss,
  post-boss exit and persistent story artefact, not full-game completion.
- Common heuristics: read Navi's triangle and action icon; inspect the new
  map layer; reflect Scrub nuts from guard; act on Gohma only when the eye is
  exposed; save seeds and hearts for the next gate.
- Failure attribution: an unreflected shot, expired flame, missed ordered
  Scrub step or unexposed Gohma eye has a visible local cause; incidental
  hostile hits threaten the continuous heart pool.
- Player-trust factors: the icon names the legal contextual action, target
  focus is visible, Map and Compass disclosure is earned, the `2-3-1` clue is
  spoken, and the Emerald is recorded separately from boss death.
- Claim IDs: `OOT-002`–`OOT-010`.

## Replay and variation

- What changes between sessions: incidental combat hits, seed use, recovery
  pickups, optional Compass/Gold Skulltula detours, room revisits and fight
  duration; the authored route and Emerald result do not randomise.
- Randomness or procedural generation: no procedural first-dungeon layout or
  random story token is evidenced; ordinary enemy timing may vary.
- Multiple viable strategies: optional resources and combat timing differ;
  the selected route fixes Map, Compass, shield reflection and Slingshot to
  make each boundary inspectable. The Compass is not a mandatory door key.
- Typical replay motive: compare cleaner routing and combat or proceed to
  the excluded ocarina and later story.

## Adjacent systems and history

- Direct predecessor: original NES *The Legend of Zelda* has a first dungeon,
  Map/Compass and boss reward, but its shield is passive and its first
  Triforce fragment is contacted in-dungeon.
- Variants: 3DS, Master Quest, later Nintendo Classics wrappers and the
  announced Switch 2 remake require separate rule evidence.
- Similar games: the original Zelda, Metroid Prime, DARK SOULS III, TUNIC and
  Hollow Knight: Silksong share subsets of dungeon, focus, contextual action,
  combat or guardian-gate mechanics.
- Important differences: this packet's Z lock and context icon operate in a
  continuous 3D dungeon; actively reflected Deku nuts create a talk gate;
  the first Spiritual Stone is awarded only after a post-boss exchange. No
  small-key mechanic is imported from later Zelda dungeons.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-161`, `ACT-164`, `ACT-199`, `ACT-341`, `ACT-437`, `ACT-494` | movement, attack, item assignment, equipment, context, held guard and target lock |
| System Behaviour | `SYS-037`, `SYS-045`, `SYS-215`, `SYS-379`, `SYS-578`, `SYS-605`, `SYS-931`, `SYS-994` | pickups, live hostiles, quest, health, dungeon, map and reflection |
| Constraint | `CON-175`, `CON-282` | heart viability and authored prerequisite order; no small keys |
| Information | `INF-073`, `INF-128`, `INF-179`, `INF-356`, `INF-372` | equipment, room/map and contextual disclosure |
| Objective | `OBJ-210` | Gohma, exit and separately given Emerald |
| Time | `TIM-003` | live hostile and fire timing |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `362` (`GAME-0001`–`GAME-0362`).
- Exact genome matches: none.
- Tied near matches: `GAME-0325` — The Legend of Zelda (`14 / 29 = 0.482759`).
- Supported combination subsets: none.
- Scan date: 2026-09-22.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0325` — The Legend of Zelda | `ACT-008`, `ACT-161`, `ACT-164`, `SYS-037`, `SYS-045`, `SYS-215`, `SYS-578`, `SYS-605`, `SYS-931`, `CON-175`, `INF-073`, `INF-179`, `INF-356`, `TIM-003` | Both bounded first dungeons use direct movement, live attacks, health, selected items, authored gates and separately earned Map/Compass disclosure. The NES packet uses passive shield cancellation, carried small keys, hostile-clearance shutters and direct contact with its Triforce fragment. Ocarina of Time instead uses 3D Z-targeting, contextual A disclosure, actively reflected Scrub shots, no early small keys and an Emerald awarded by a separate giver after the boss exit | Near, `14 / 29 = 0.482759` |

## Taxonomy impact

- Add `SYS-994`, `INF-372` and `OBJ-210` under a reviewed taxonomy-change
  record; no lower-ID signature changes.
- Reused genes retain their definitions; the new packet supplies additional
  evidence without importing early small keys.
- Add no combination without a verified recurring proper subset.

## Negative results

- `SYS-063` and any carried small-key gate are rejected: Nintendo explicitly
  excludes small keys from the earliest dungeons and neither scoped route
  uses one.
- `SYS-932` is rejected: the shield must be actively raised to reflect the
  Scrub's projectile, unlike the passive original-NES shield.
- `OBJ-191` is rejected: Kokiri's Emerald comes from a separate post-boss
  giver, not direct contact with a fragment inside the boss dungeon.
- The Fairy Ocarina is acquired only when leaving Kokiri Forest after this
  terminal; musical command genes are not part of this packet.
- No direct game execution or audiovisual evidence was obtained.

## Delta summary

## New facts

- [Confirmed | Direct | High] The original N64 first dungeon has contextual
  A and Z-target interfaces, Map/Compass disclosure and no small keys
  (`OOT-001`–`OOT-004`).
- [Observation | Corroborated | High] Reflection, Slingshot gates, ordered
  Scrubs, Gohma and post-boss Emerald comprise the bounded route
  (`OOT-005`–`OOT-010`).

## New genes

- [Observation | Corroborated | High] `SYS-994` returns a guarded projectile
  to its source and creates a contextual opportunity.
- [Confirmed | Direct | High] `INF-372` discloses the current contextual A
  action and focused target.
- [Observation | Corroborated | High] `OBJ-210` settles boss, exit and
  separately awarded story token.

## New combinations

- [Observation | Direct | High] No verified new combination.

## Taxonomy changes

- [Observation | Corroborated | High] Three new Active boundaries; no
  earlier signature or lifecycle changes.

## New questions

- Does the next Zelda dungeon with actual small and boss keys require a
  different access boundary from this keyless first-dungeon route?

## Next recommended game

- [Confirmed | Direct | High] `GAME-0364` — Wii Sports, the next authorised
  unit in `SEARCH_DEMAND_GAME_SELECTION_026`.
- Optimisation criterion: continue the fixed Goal order only after this full
  unit's validation and stop window.
- Expected information gain: motion interpretation, sampled physical input,
  sport scoring and Wii controller feedback.
- Backlog impact: unit 4 of the active nine-game Goal.

## Why this game

- [Confirmed | Direct | High] Ocarina of Time is the third selected cultural
  anchor and tests target lock, contextual action and a first-dungeon story
  token against original Zelda's earlier two-dimensional dungeon signature.

## Reproducibility notes

1. Use licensed original English N64 rules through Nintendo 64 Classics; do
   not use a 3DS version, Master Quest, future remake, rewind or guide cheats.
2. Start a fresh file, acquire Kokiri Sword and Deku Shield, pass Mido and
   enter the Great Deku Tree with Navi.
3. Take Map, reflect the Scrub's shot and speak before stun expiry; acquire
   Slingshot and shoot the hanging exit ladder; obtain Compass.
4. Traverse the torch/web, water, eye, block and `2-3-1` Scrub gates. Do not
   invent a small-key pickup or spend.
5. Shoot Gohma's red eye, strike during stun, repeat until defeated; use the
   blue exit and receive Kokiri's Emerald before leaving the forest.
6. Verify the Stone on Quest Status and run the deterministic repository-side
   control, which does not execute the game.

## Localisation review

- `verified`: official title and stable ID, Link, Navi, Kokiri, Deku,
  Slingshot, Z-targeting and Nintendo product names remain named mechanics,
  proper names or evidence-relevant labels.
- `corrected`: reviewed Ukrainian profile, scope, direct-play note,
  presentation, new-gene definitions, salience note and every admitted
  plain-language card preserve the original preconditions and terminal.
- `retained-with-reason`: `2-3-1`, button letters and stable gene IDs are
  literal rule/interface identifiers; no generic English prose is deferred.
