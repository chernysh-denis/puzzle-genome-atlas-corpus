---
game_id: GAME-0329
slug: donkey-kong-country
game_title: "Donkey Kong Country"
analysis_status: reviewed
reviewed: 2026-09-20
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-048
    - ACT-052
    - ACT-295
    - ACT-348
  system:
    - SYS-036
    - SYS-037
    - SYS-045
    - SYS-064
    - SYS-215
    - SYS-755
    - SYS-911
    - SYS-933
    - SYS-935
    - SYS-938
    - SYS-939
  constraint:
    - CON-442
  information:
    - INF-358
  objective:
    - OBJ-194
  time:
    - TIM-003
---

# Game: Donkey Kong Country

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Donkey Kong, Diddy
Kong, Rambi, Kongo Jungle, Jungle Hijinxs, Ropey Rampage, K-O-N-G letters and
named barrel classes are carrier parameters, not gene names.

## Analysis scope

- Version / ruleset: original North American English Super NES retail product
  family `SNS-8X-USA`, one-player fresh game, first stage `Jungle Hijinxs!`.
  The exact cartridge pressing and mask-ROM revision were not observed. This is
  not the Game Boy Color or Game Boy Advance port, Virtual Console, SNES
  Classic, Nintendo Switch Online wrapper, a sequel or a modification.
- Structured analysis target: licensed original Super NES cartridge product;
  see `GAME-0329` in
  [`knowledge/platforms/games.json`](../../platforms/games.json).
- Primary decision loop: steer the active Kong through the side-view route;
  jump, roll or cartwheel against immediate terrain and hostiles; carry and
  throw barrels; preserve or deliberately switch the two-Kong buffer; activate
  the Star Barrel; release and ride Rambi; break each concealed entrance,
  settle its bounded bonus room and resume the stage; then cross the exit while
  retaining both bonus discoveries.
- Entry: first ordinary control of solo Donkey Kong at the beginning of
  `Jungle Hijinxs!`, before breaking the first DK Barrel that contains Diddy.
- Positive terminal: the route has activated its Star Barrel, visited and
  settled both hidden bonus rooms, crossed the exit cave and returned to the
  Kongo Jungle map with `Jungle Hijinxs!` marked by its completion exclamation
  and `Ropey Rampage` available. The successor stage is not entered.
- Negative state: unsafe contact or a fall removes the active Kong when its
  partner is present and transfers control to the partner; the same lethal
  state while alone consumes one finite life and returns the controlled body
  to the start or activated Star Barrel while stock remains. Exhausting the
  stock reaches the first Game Over boundary; Continue behaviour is excluded.
- Included: direct run and jump; Donkey's roll and Diddy's cartwheel; carrying
  and throwing ordinary barrels; active/following Kong switching, substitution
  after damage and missing-partner restoration from a DK Barrel; side-view
  gravity and collision; visible enemies and contact resolution; bananas,
  K-O-N-G letters and balloons as route pickups; one-hundred-banana and
  complete-letter life awards; finite lives; Star Barrel return; the Rambi
  crate, mounting, direct riding and dismounting; Rambi's concealed-wall
  break; both hidden bonus rooms and their return points; the stage exit,
  successor-map unlock and full-bonus exclamation marker.
- Excluded: the optional treehouse and banana-hoard detour; off-screen treetop
  balloons and exhaustive banana collection; animal-token bonus levels; every
  later stage, world, boss and save point; Funky, Candy and Cranky services;
  two-player modes; completion percentage beyond this stage; exact scoring,
  speed or time; cartridge-revision differences; the sequel and all ports,
  wrappers, cheats, glitches, speedrun routes and modifications.
- Reproducible parameterisation: start a fresh one-player game, enter the first
  stage, free Diddy from the first DK Barrel and keep the pair when practical.
  Follow the ordinary ground route, activate the Star Barrel, break Rambi's
  crate, ride him into the first concealed wall, settle that bonus and resume.
  Reach and settle the second concealed bonus room, then enter the exit cave.
  Active Kong, incidental pickups, enemy defeats and exact input timing are
  parameters; both bonus discoveries and the exit are fixed predicates.
- Potential scoped modules: animal-token bonus stages, later animal buddies,
  mine carts, aquatic stages, world services, bosses, save persistence,
  two-player handoff and other releases require separate terminals and
  evidence.
- Direct-play status: not conducted. No cartridge, console, emulator, input
  trace, save, screenshot, video or audio was used. Nintendo's preserved manual
  establishes the product, controls, tag-team, barrels, lives, checkpoint,
  pickups, bonus rooms and animal-buddy rules; three written route references
  establish the bounded first-stage order and full-bonus marker. This is a
  source-bounded reconstruction, not a claimed playthrough or revision test.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `DKC-001` | The packet is the original North American English SNES retail product family and excludes ports and wrappers | Confirmed | Direct | High | P1, P2, S1 |
| `DKC-002` | The active Kong runs, jumps and performs its character-specific rolling attack while the partner follows | Confirmed | Direct | High | P1 |
| `DKC-003` | A hit removes the active member of a present pair and transfers control to the follower, while a DK Barrel restores a missing partner | Confirmed | Direct | High | P1 |
| `DKC-004` | Ordinary barrels can be carried and thrown, and the Star Barrel replaces the same-stage finite-life return point | Confirmed | Direct | High | P1 |
| `DKC-005` | Bananas, letters and balloons contribute to finite lives under their declared rules | Confirmed | Direct | High | P1 |
| `DKC-006` | Breaking the Rambi crate mounts the animal and Rambi can break a concealed stage wall | Confirmed | Direct | High | P1, S2, S3 |
| `DKC-007` | `Jungle Hijinxs!` contains two hidden bonus rooms whose settlement returns play to authored points in the same stage | Observation | Corroborated | High | S2, S3, S4 |
| `DKC-008` | Finding both bonus rooms changes the completed stage's map label with an exclamation mark while ordinary exit unlocks `Ropey Rampage` | Observation | Corroborated | High | S2, S4 |
| `DKC-009` | The live view and transient counters expose immediate paired, mounted, collectible, life and completion state without revealing hidden walls | Confirmed | Corroborated | High | P1, S2, S4 |

## Basic data

- Release / origin: Rare, Nintendo, Super NES, North American release
  1994-11-21.
- Platform or physical form: original licensed North American English Super NES
  cartridge product `SNS-8X-USA`; exact pressing and mask-ROM revision not
  observed.
- Puzzle family: paired-character side-view platform routing with hidden bonus
  detours and retained stage-completion credit.
- Primary sources:
  - **[P1]** [Nintendo's preserved original *Donkey Kong Country* manual](https://www.nintendo.co.jp/clvs/manuals/common/pdf/CLV-P-SAALE.pdf),
    product, controls, tag-team substitution, barrels, finite lives, checkpoint,
    pickups, bonus rooms and Rambi rules.
  - **[P2]** [Nintendo's *Donkey Kong Country* product record](https://www.nintendo.com/en-gb/Games/Super-Nintendo/Donkey-Kong-Country-276896.html),
    original platform, year, publisher and developer identity.
- Secondary sources:
  - **[S1]** [GameFAQs release data](https://gamefaqs.gamespot.com/snes/588282-donkey-kong-country/data),
    North American `SNS-8X-USA` product identifier and release date.
  - **[S2]** [GameFAQs written first-stage route](https://gamefaqs.gamespot.com/snes/588282-donkey-kong-country/faqs/7276),
    Rambi, four letters and two bonus-room entrances.
  - **[S3]** [StrategyWiki `Jungle Hijinxs` route](https://strategywiki.org/wiki/Donkey_Kong_Country/Jungle_Hijinxs),
    solo Donkey entry, Diddy restoration, Rambi crate and concealed wall.
  - **[S4]** [Source Gaming `Jungle Hijinxs` analysis](https://sourcegaming.info/2023/12/03/level-with-me-jungle-hijinxs-donkey-kong-country/),
    tag buffer, Star Barrel, both bonus returns, exit, successor and
    exclamation-marker corroboration.
- Claim IDs: `DKC-001`–`DKC-009`.

## Mechanical decomposition

### Action Genes

- Existing `ACT-008`: directly run and jump the active Kong or mounted Rambi
  through traversable side-view geometry.
- Existing `ACT-048`: pick up, carry and release or throw an ordinary barrel.
- Existing `ACT-052`: switch the unique direct-control locus between the two
  present Kongs while the former active body remains as follower.
- Existing `ACT-295`: commit Donkey's roll or Diddy's cartwheel as the current
  character-owned fighting attack.
- Existing `ACT-348`: enter Rambi's riding state from the broken crate, control
  his locomotion and jump, or dismount.
- Controller buttons, active Kong, jump arc, roll distance, carried barrel and
  Rambi pace are parameters. Claims: `DKC-002`, `DKC-004`, `DKC-006`.

### System Behaviour Genes

- Existing `SYS-036`: continuously resolve gravity, velocity, support and
  collision for the controlled body, thrown barrels and relevant actors.
- Existing `SYS-037`: collect bananas, letters, balloons and eligible reward
  objects on contact without immediately ending the stage.
- Existing `SYS-045`: advance enemies and the following partner through local
  authored locomotion while simulation time runs.
- Existing `SYS-064`: distinguish qualifying top contact from unsafe side or
  underside contact against eligible enemies.
- Existing `SYS-215`: resolve legal rolling, cartwheel, stomp, barrel and Rambi
  attacks against live hostiles in real time.
- Existing `SYS-755`: break eligible barrels, animal crates and concealed
  world fixtures while resolving their contents or linked entrance.
- Existing `SYS-911`: when the controlled pair is exhausted, spend one finite
  life and restore the body at the current stage return anchor.
- Existing `SYS-933`: activating the Star Barrel changes the finite-life return
  anchor inside the current stage.
- Existing `SYS-935`: every completed one-hundred-banana threshold becomes one
  additional finite life; K-O-N-G and balloons are separate award parameters.
- New `SYS-938`: maintain exactly one active and one following Kong when the
  pair is complete, transfer control after a hit, and restore the missing
  partner from a DK Barrel while solo.
- New `SYS-939`: enter a concealed bounded bonus room, settle its reward rule,
  return to the authored stage point and retain discovery credit toward the
  stage's full-bonus marker.
- Resolution order: input changes the active body or action; live physics,
  hostile motion and contact settle; a hit first consumes the active member of
  a complete pair; only a lethal solo state reaches the finite-life system;
  concealed entrances suspend the main route until the bonus settles; the exit
  evaluates retained bonus credit on the map. Claims: `DKC-002`–`DKC-009`.

### Constraint Genes

- Existing `CON-442`: movement, attack, carry, switch and ride commands require
  a compatible current body, pose, held-object and mounted state.
- Rambi availability, barrel reach, partner presence, attack recovery and
  current bonus-room phase are parameters. Claims: `DKC-002`, `DKC-004`,
  `DKC-006`.

### Information Genes

- New `INF-358`: the side-view stage and transient counters jointly expose the
  active/following pair, mounted state, immediate terrain, hostiles, barrels,
  pickups, bananas, letters and lives, then expose checkpoint, bonus discovery
  and exit/map completion feedback while concealed entrances and future route
  remain hidden.
- Exact HUD placement, counter duration, sprite art, viewport width and marker
  glyph are parameters. Claims: `DKC-009`.

### Objective Genes

- New `OBJ-194`: find and settle every declared hidden bonus detour in one
  authored stage, then cross its retained exit so the map records full local
  completion and exposes the successor stage.
- K-O-N-G completion, every banana, every enemy and optional off-route rewards
  are not terminal requirements. Claims: `DKC-007`, `DKC-008`.

### Time Genes

- Existing `TIM-003`: movement, gravity, enemies, partner following, attacks,
  thrown barrels and mounted traversal advance continuously while commands are
  accepted; map and bonus settlement sequences interrupt that cadence.

## Reproducible transitions

| Before | Action | Deterministic or bounded resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Solo Donkey stands near the first DK Barrel | break the barrel | Diddy appears as follower and the pair buffer becomes complete | a typed fixture restores the missing partner | `DKC-003` |
| Both Kongs are present | press the switch command | direct control transfers and the former active Kong remains as follower | persistent-body switching is distinct from replacement | `DKC-002`, `DKC-003` |
| Both Kongs are present and the active body receives an unsafe hit | allow the contact to settle | the active Kong leaves and direct control transfers to the follower without spending a life | the pair is a one-hit substitution buffer | `DKC-003` |
| A compatible barrel is reachable | pick it up, move and release toward an eligible target | the barrel becomes a carried offset body and then a thrown collision body | portable rigid objects participate in route combat | `DKC-004` |
| The Star Barrel is intact | break it | its local state settles and later solo defeat uses it as the return anchor | breakable checkpoint and finite-life return are separate transitions | `DKC-004` |
| Rambi's crate is reachable | break the crate and enter the ride state | Rambi becomes the directly ridden body and admits his movement and wall-breaking rules | an animal buddy is a mount, not a cosmetic form | `DKC-006` |
| Rambi reaches the first sensitive wall | drive into the concealed entrance | the wall breaks and play transfers to the first bounded bonus room | hidden geometry opens an optional retained detour | `DKC-006`, `DKC-007` |
| A bonus room's local rule is active | settle its reward sequence | play returns to the authored stage point and the room remains credited as found | bonus settlement preserves main-stage continuity | `DKC-007` |
| Both bonus rooms are credited | enter the exit cave | the stage settles on the map, receives the exclamation marker and exposes `Ropey Rampage` | the full-bonus terminal is retained beyond the stage | `DKC-008` |

## Edge-case audit

- Manual switching and damage substitution share the same persistent pair but
  are not the same transition: only the former is a player action.
- A DK Barrel restores a partner only while one Kong is missing; with both
  present it behaves as an ordinary barrel. This conditional output belongs to
  `SYS-938`, not a generic pickup gene.
- The Star Barrel is included only as an activated return anchor. Save files,
  world persistence and unlimited retry are not inferred.
- `SYS-935` covers the one-hundred-banana threshold. K-O-N-G and balloons award
  lives through distinct carrier rules and do not broaden that threshold
  boundary.
- Rambi is directly ridden and can break an eligible concealed wall. Other
  animal buddies, their token stages and later-level abilities are excluded.
- Both bonus rooms are optional for ordinary exit but mandatory for this
  reproducible full-bonus terminal. Their rewards do not become separate
  objectives.
- The exclamation mark records all local bonus entrances found; it does not
  claim exhaustive bananas, letters, enemies or score.
- Route sources establish ordinary progression but not exact cartridge-
  revision timing, reset tables or save persistence. Those remain unclaimed.

## Strategic and experiential structure

- Local decision: choose the active Kong for immediate movement and attack,
  preserve the partner buffer, use barrels without losing route access and
  recognise terrain that Rambi can break.
- Medium-term planning: activate the Star Barrel before later hazards, carry a
  complete pair where possible and leave each bonus room at its authored return
  point without overlooking the second entrance.
- Long-term structure: turn two concealed detours and one ordinary exit into a
  retained map marker and unlocked successor while finite lives bound failure.
- Common heuristics: keep the partner until a difficult contact; prefer the
  safer Kong attack for the present geometry; collect nearby bananas without
  treating them as the terminal; use Rambi before passing his concealed wall.
- Failure attribution: missing partner, lost life, inactive checkpoint,
  undiscovered bonus room and ordinary versus full stage completion remain
  distinguishable through bodies, counters and map feedback.
- Player trust: equivalent contacts at equivalent pair, mount and checkpoint
  state must resolve identically, and returning from a bonus room must preserve
  both its discovery credit and the declared stage re-entry.

## Replay and variation

- Stage geometry, enemies, barrels, animal crate, bonus entrances and exit are
  authored. No procedural layout or random encounter generation is claimed.
- Active Kong, incidental pickups, enemy defeats, barrel use and route timing
  can vary; the reproducible trace fixes both bonus rooms and the ordinary exit.
- Replay within this packet compares partner preservation, bonus discovery and
  clean traversal rather than speed, score or whole-game completion.
- Claims: `DKC-002`–`DKC-009`.

## Adjacent systems and history

- *Crash Bandicoot* shares direct platform movement, character-owned attacks,
  continuous body physics, route pickups, autonomous enemies, direct combat,
  breakable objects, finite lives, an activated checkpoint, collectible-to-
  life conversion and a live clock. Its first level binds counted crates,
  stacked masks and a no-death clear-gem predicate to a near-camera route;
  `Jungle Hijinxs!` instead uses a persistent two-Kong substitution buffer,
  portable barrels, direct animal riding and two retained hidden bonus rooms.
- *Super Mario Bros.* shares direct side-view jumping, enemy contact, route
  pickups, finite lives and a successor stage. Its one-way camera and flagpole
  score own the terminal; Donkey Kong Country permits local return, switches a
  paired body and records optional hidden-room completeness on the world map.
- *Battletoads* shares direct attacks, live enemies, finite lives and an
  authored first-stage exit. Its bounded canyon converts defeated enemies into
  temporary tools; Donkey Kong Country centres follower substitution, barrels,
  Rambi and hidden bonus discovery.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-048`, `ACT-052`, `ACT-295`, `ACT-348` | controller mapping, active Kong, barrel and Rambi handling |
| System Behaviour | `SYS-036`, `SYS-037`, `SYS-045`, `SYS-064`, `SYS-215`, `SYS-755`, `SYS-911`, `SYS-933`, `SYS-935`, `SYS-938`, `SYS-939` | route geometry, pair, pickups, return anchor and bonus rooms |
| Constraint | `CON-442` | body, pose, held object, partner and mounted state |
| Information | `INF-358` | viewport, transient counters and completion feedback |
| Objective | `OBJ-194` | both bonus discoveries, exit, marker and successor |
| Time | `TIM-003` | live update cadence and settlement interruptions |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `328` (`GAME-0001`–`GAME-0328`).
- Exact genome matches: none.
- Tied near matches: `GAME-0326` — Crash Bandicoot (`12 / 25 = 0.480000`).
- Supported combination subsets: none.
- Scan date: 2026-09-20.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0326` — Crash Bandicoot | `ACT-008`, `ACT-295`, `SYS-036`, `SYS-037`, `SYS-045`, `SYS-064`, `SYS-215`, `SYS-755`, `SYS-911`, `SYS-933`, `SYS-935`, `TIM-003` | Both directly steer and attack with a jumping body through live enemies, collect route objects, break fixtures and spend finite lives from an activated checkpoint. Crash uses near-camera depth, a single avatar, counted crates, a mask ladder and a no-death gem predicate; Donkey Kong Country uses side view, a persistent pair, portable barrels, direct Rambi riding and retained hidden-room credit before the map exit. | Near, `12 / 25 = 0.480000` |

### Preserved research notes

- New genes: `SYS-938`, `SYS-939`, `INF-358` and `OBJ-194`.
- Classification result: `New gene`; no verified combination is expected.
- Evidence and reasoning: established movement, switching, object, physics,
  contact, combat, breakage, life, checkpoint, collectible-threshold and time
  genes fit. No earlier boundary owns a two-character substitution buffer that
  can be restored by a conditional fixture, a hidden bounded detour whose
  discovery survives re-entry, or full local bonus discovery retained on the
  map after the ordinary stage exit.

## Taxonomy impact

- Registry changes: add four Active boundaries and add Donkey Kong Country
  support to sixteen compatible existing boundaries.
- Taxonomy-change record: none; no existing boundary or lifecycle changes.
- Candidate terms affected: named Kongs, Rambi, K-O-N-G, barrel classes,
  `Jungle Hijinxs!`, `Ropey Rampage` and the exclamation glyph remain carrier
  parameters.

## Negative results

- No cartridge, console, emulator, direct play, input trace, save, screenshot,
  video or audio evidence exists for this unit.
- No exact mask-ROM revision, frame timing, hidden random table, reset table or
  save-persistence claim is made.
- The manual's whole-game animal, barrel and bonus catalogue is not imported:
  only rules causally used by the bounded first-stage trace enter the genome.
- Treehouse and treetop detours, animal-token stages, services, later levels,
  bosses, two-player handoff and completion percentage are excluded rather
  than inferred.
- Ports and wrappers do not support this original-cartridge signature.

## Delta summary

## New facts

- [Confirmed | Direct | High] Nintendo's manual establishes the tag-team,
  barrel, life, checkpoint, pickup, bonus-room and Rambi rule families
  (`DKC-002`–`DKC-006`, `DKC-009`).
- [Observation | Corroborated | High] Three written route references establish
  the two first-stage bonus rooms and retained map-marker terminal
  (`DKC-007`, `DKC-008`).

## New genes

- [Confirmed | Direct | High] `SYS-938` isolates active/follower substitution
  and conditional DK-Barrel restoration.
- [Observation | Corroborated | High] `SYS-939`, `INF-358` and `OBJ-194`
  isolate bonus detour retention, its decision surface and full stage terminal.

## New combinations

- [Observation | Corroborated | High] No new verified combination.

## Taxonomy changes

- [Observation | Direct | High] No earlier boundary, signature or lifecycle
  state changes; sixteen existing genes are reused as written.

## New questions

- Which exact transient objects and pair fields reset after Star Barrel return
  in each North American mask-ROM revision?
- Does every retail revision apply the same map exclamation update timing when
  the second bonus room is found before ordinary exit?

## Next recommended game

- [Hypothesis | Limited | High] `GAME-0330` *Silent Hill 2*, PS5 remake, is the
  next reserved audience-recognition unit.
- Optimisation criterion: replace a bright authored platform route with
  exploration, psychological-horror combat and a bounded remake opening.
- Backlog impact: completes 5/9 of the current fixed horizon.

## Why this game

- [Hypothesis | Limited | High] Original Donkey Kong Country is a recognisable
  SNES anchor whose paired damage buffer, animal ride and retained hidden-bonus
  credit differ causally from a generic platformer label.

## Completion checklist

- [x] exact original product family, stage, entry, terminal and exclusions declared
- [x] original manual and independent written route evidence separated
- [x] paired substitution, finite lives, checkpoint and bonus credit separated
- [x] direct-play, audiovisual and cartridge-revision limits disclosed
- [x] complete six-type gene scan performed
- [x] deterministic lower-ID comparison output integrated
- [ ] reviewed Ukrainian localisation and bilingual presentation completed
- [ ] original artwork and responsive browser checks completed
- [ ] full repository and static-first gates complete
