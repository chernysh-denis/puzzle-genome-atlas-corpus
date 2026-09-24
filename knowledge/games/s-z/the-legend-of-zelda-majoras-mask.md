---
game_id: GAME-0395
slug: the-legend-of-zelda-majoras-mask
game_title: "The Legend of Zelda: Majora’s Mask"
analysis_status: reviewed
reviewed: 2026-09-24
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-091
    - ACT-107
    - ACT-161
    - ACT-341
    - ACT-532
  system:
    - SYS-037
    - SYS-398
    - SYS-1057
  constraint:
    - CON-068
    - CON-282
    - CON-351
  information:
    - INF-179
    - INF-395
  objective:
    - OBJ-201
  time:
    - TIM-003
---

# Game: The Legend of Zelda: Majora's Mask

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). The password's
digits, Ocarina notes, three named days, moon appearance and Town geometry
are parameters rather than separate genes.

## Analysis scope

- Version / ruleset: original English European Nintendo 64 *Majora's Mask*,
  using Nintendo's `[0900/Z1/UKV/N64]` booklet and two original-N64 written
  routes. The N64 Expansion Pak is required. The exact cartridge revision,
  regional text variation and later licensed wrapper were not inspected.
- Primary decision loop: read the current Clock Town location, day and clock;
  navigate to an eligible person, item or gate; learn and submit the ordered
  Bomber password, trade the Moon's Tear for access to the launch flower,
  then wait for the final-night clock-tower opening, recover the Ocarina and
  deliberately play the Song of Time to settle a selective world reset.
- Entry: the first cycle's ordinary control as cursed Deku Link after leaving
  the Clock Tower basement for Clock Town on the First Day, before the Stray
  Fairy is returned. The curse's introductory chase is excluded.
- Positive terminal: after recovering the Ocarina at the clock-tower encounter,
  play the recalled Song of Time and regain ordinary control at Dawn of the
  First Day with the Ocarina/song retained. Merely entering the tower or
  seeing Skull Kid does not finish the packet.
- Negative terminal: allowing the 72 in-game hours to expire causes moonfall
  and Game Over. A prior Song-of-Time save, if any, may be loaded, but a new
  first cycle is not automatically reset with an Ocarina. The precise loss
  state after other local damage is not measured here.
- Included: the day/night-dependent Stray Fairy location and Great Fairy
  magic/bubble grant; the Bomber balloon, children's search and remembered
  numeric passcode; observatory telescope and Moon's Tear; Business Scrub
  trade for the Land Title Deed and flower access; final-night tower door;
  Deku flower launch, bubble strike, Ocarina pickup, recalled melody and
  selective Song-of-Time reset. The continuously advancing clock is included.
- Excluded: Song of Healing and return to human form after this terminal;
  Southern Swamp and all later regions/temples; optional bank deposit, mask
  collection, heart pieces, minigames, Bomber Notebook, Scarecrow time skip,
  Inverted/Double Time variations, 3DS remake changes, Switch emulator
  conveniences, exact damage/magic costs and full-campaign completion.
- Reproducible parameterisation: start the original N64 first cycle at the
  stated exit, record the displayed day/time, fairy location and grant,
  learned Bomber digits, observatory exchange, deed, flower access, tower
  opening, Ocarina pickup and reset settlement. The children's hiding places
  and exact elapsed times may vary; no route is claimed to be frame-optimal.
- Potential scoped modules: post-reset Song of Healing, one named temple and
  its three-day schedule, item banking and late-cycle song variants each need
  separate entry, terminal and evidence packets.
- Direct-play status: none. No cartridge, ROM, emulator, save, input trace,
  screenshot, video or audio was opened or analysed. The official original
  booklet supplies core time and reset rules; two written N64 routes
  reconstruct the opening gate order. This is not a claim of personal play.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `MM-001` | The original Nintendo 64 game requires an Expansion Pak; the selected booklet is the English UKV/N64 release. | Confirmed | Direct | High | P1, P2 |
| `MM-002` | Three in-game days give a 72-hour deadline; moonfall is Game Over, not an automatic retained-inventory loop. | Confirmed | Direct | High | P1 |
| `MM-003` | The clock advances during ordinary play but pauses during conversations or the pause screen. | Confirmed | Direct | High | P1 |
| `MM-004` | Playing Song of Time with the recovered Ocarina returns to Dawn of the First Day and saves designated durable progress while day-local events and event items reset. | Confirmed | Direct | High | P1 |
| `MM-005` | The first-cycle route restores the Great Fairy for magic, pops the Bomber balloon, learns a numeric passcode and enters the observatory. | Observation | Corroborated | High | S1, S2 |
| `MM-006` | Telescope observation leads to Moon's Tear; trading it to the Business Scrub permits use of the flower near the tower. | Observation | Corroborated | High | S1, S2 |
| `MM-007` | The tower access opens at midnight on the Final Day; Deku flower flight and a bubble hit permit recovery of the Ocarina and the first Song of Time reset. | Observation | Corroborated | High | S1, S2 |
| `MM-008` | This packet stops before Song of Healing, later masks/temples and any remade or emulator-specific convenience. | Observation | Direct | High | R1 |

## Basic data

- Release / origin: Nintendo 64 game from Nintendo/EAD, originally released
  in 2000; English European booklet `[0900/Z1/UKV/N64]` is the bounded
  rules source. This record does not assume the exact UK cartridge revision.
- Platform or physical form: `PLAT-NINTENDO-64` original cartridge rules,
  reconstructed from official documentation; no local executable tested.
- Mechanical families: time-loop and retained knowledge; world topology and
  perspective; real-time system pressure.
- Primary sources:
  - **[P1]** [Nintendo original English N64 instruction booklet](https://www.nintendo.com/eu/media/downloads/games_8/emanuals/nintendo_8/Manual_Nintendo64_TheLegendOfZeldaMajorasMask_EN.pdf),
    pp. 10–11 and its Deku/clock/song sections, for the deadline, save/reset,
    retained and discarded state, time controls and form abilities.
  - **[P2]** [Nintendo's Nintendo 64 history](https://www.nintendo.com/en-gb/Hardware/Nintendo-History/Nintendo-64/Nintendo-64-625959.html),
    for the original platform and Expansion Pak requirement.
- Independent original-N64 written routes:
  - **[S1]** [Zelda Dungeon first three days](https://www.zeldadungeon.net/majoras-mask-walkthrough/first-three-days/),
    distinguishing the N64 route from its 3DS notes.
  - **[S2]** [GameFAQs Nintendo 64 walkthrough](https://gamefaqs.gamespot.com/n64/197770-the-legend-of-zelda-majoras-mask/faqs/56570),
    first-three-days section for the passcode, observatory, deed, tower and song.
- **[R1]** Local no-direct-play and ADR-007 scope audit in this record.
- Claim IDs: `MM-001`–`MM-008`.

## Mechanical decomposition

### Action Genes

- `ACT-008`: navigate Clock Town and launch/glide from the Deku flower to the
  opened tower ledge. Flower position and flight distance are route parameters.
- `ACT-107`: learn the operational Bomber code from the children's authored
  interaction; the player must carry this information to the next gate.
- `ACT-532`: enter the ordered numeric code at the observatory passage and
  later the remembered note sequence on the recovered Ocarina. The two
  receiving interfaces differ but both require finite ordered submission.
- `ACT-341`: restore/interact with the Great Fairy, inspect the telescope,
  collect the falling Tear and address the tower/Ocarina world objects.
- `ACT-091`: offer the carried Moon's Tear to the Business Scrub for the
  addressed deed/flower exchange; it is not a generic pickup.
- `ACT-161`: aim and release Deku bubbles at the Bomber balloon and Skull Kid.
  The exact projectile speed is not asserted.
- Claim IDs: `MM-005`–`MM-007`.

### System Behaviour Genes

- `SYS-037`: contact with the fallen Moon's Tear and later Ocarina acquires
  the respective world object; the trade and durable artefact grant are
  distinguished from mere contact.
- `SYS-398`: Great Fairy magic supplies the bubble capability required for
  the opening gate; the recovered unique Ocarina supports the first retained
  Song of Time capability.
- `SYS-1057`: submitted Song of Time starts the initial dawn again while
  retaining the Ocarina/song and discarding specified event items and
  day-local changes. Deadline failure never invokes this rule automatically.
- Resolution order: inspect clock/location → obtain magic and code → pass
  observatory gate → acquire and trade Tear → wait for final-night access →
  launch and strike → pick up Ocarina → submit Song → selectively reset.
- Claim IDs: `MM-002`, `MM-004`–`MM-007`.

### Constraint Genes

- `CON-068`: the 72-hour moonfall deadline ends the attempt unsuccessfully;
  the player must perform the song before expiry.
- `CON-282`: authored dependencies gate the observatory, flower and opened
  tower; ordinary movement cannot bypass the stated route prerequisites.
- `CON-351`: Deku bubble attacks require magic after the Great Fairy grant.
  Exact reserve amount and shot cost remain unmeasured.
- Claim IDs: `MM-002`, `MM-005`–`MM-007`.

### Information Genes

- `INF-179`: the current view identifies nearby actors, traversable Town
  geometry, flower and accessible entrances, but not every future schedule.
- `INF-395`: displayed day and time position the player relative to the
  final-night tower gate and the known 72-hour moonfall.
- Claim IDs: `MM-002`, `MM-003`, `MM-006`, `MM-007`.

### Objective Genes

- `OBJ-201`: obtain the unique Ocarina, demonstrate its first Song of Time
  capability and regain first-dawn control retaining that capability. This
  does not require post-reset restoration of Link's human form.
- Claim IDs: `MM-004`, `MM-007`, `MM-008`.

### Time Genes

- `TIM-003`: Town movement, NPC schedule and the deadline advance in live
  time, with the booklet's conversation/pause exceptions. The submitted
  Song of Time reset is `SYS-1057`, not `TIM-016`'s automatic expiry loop.
- Claim IDs: `MM-002`–`MM-004`.

## Reproducible transitions

| Before | Action | Rule-bounded resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| First Day Deku form; Great Fairy is dispersed | Find and return the Stray Fairy | Magic/bubble capability becomes available | prerequisite for the balloon and later strike | `MM-005` |
| Bomber balloon is intact | Spend magic to shoot a Deku bubble; complete children's search | Children disclose an ordered numeric password | learned information gates the observatory | `MM-005` |
| Observatory passage awaits its password | Enter the remembered digits in order | Correct code admits the passage and telescope route | symbolic input is not walking a direction path | `MM-005` |
| Telescope frames Skull Kid and the falling object | Observe, then collect Moon's Tear | The Tear becomes a carried exchange item | information changes available world action | `MM-006` |
| Business Scrub occupies the flower plot | Offer the Moon's Tear | Trade grants Land Title Deed and access to the flower | item delivery opens a traversal edge | `MM-006` |
| Final Day clock reaches midnight | Enter opened tower approach via flower flight | Deku form reaches Skull Kid's ledge | access is both scheduled and topology-bound | `MM-007` |
| Skull Kid has the Ocarina | Hit with a Deku bubble and collect the dropped Ocarina | Unique artefact and recalled song become available | acquisition precedes the reset command | `MM-007` |
| Ocarina is held before moonfall | Play Song of Time's ordered notes | Dawn of First Day returns, durable Ocarina/song remain, local events reset | chosen selective reset is the positive terminal | `MM-004`, `MM-007` |
| Clock reaches 72 hours without the song | Take no successful reset action | Moonfall causes Game Over | deadline is not an automatic usable loop | `MM-002` |

## Strategic and experiential structure

- Local decision: read the current Town day, time and visible gate, then
  choose a reachable actor or object rather than guessing a global solution.
- Medium-term planning: acquire magic before bubble-dependent gates, preserve
  the Bomber code, trade the Tear and retain flower access until final night.
- Long-term structure: schedule the tower encounter before moonfall and
  actively spend the obtained Ocarina/song to restart the cycle.
- Failure attribution: the clock and authored midnight gate explain deadline
  pressure; exact hitboxes and route durations were not directly measured.
- Player-trust factors: unlike a hidden automatic loop, the official booklet
  explicitly describes which reset is player-commanded and which expiry is
  Game Over, and which inventory is durable versus day-local.

## Replay and variation

- Bomber placements, Stray Fairy day/night location, waiting time, optional
  errands and the precise approach may differ. The first-cycle gate order,
  terminal moonfall and deliberate song reset remain the scoped rules.
- Banking rupees can preserve them through a later reset but is optional and
  excluded from this core route; no bank mechanic is inferred into the genome.

## Adjacent systems and history

- *Outer Wilds* automatically begins another world cycle at a fixed terminal
  and keeps knowledge rather than a carried Ocarina; its `TIM-016` and
  `SYS-140` therefore do not fit the selected Majora reset.
- *Prince of Persia: The Sands of Time* also grants a unique retained artefact
  (`OBJ-201`), but the Dagger rewinds a local death rather than resetting a
  three-day schedule with selective item loss.
- *TUNIC* submits cardinal directional commands (`ACT-106`). The Bomber code
  and Ocarina song here use digits or notes at addressed interfaces.

## Normalised genome

| Type | Active genes | Parameters outside signature |
|---|---|---|
| Action | `ACT-008`, `ACT-091`, `ACT-107`, `ACT-161`, `ACT-341`, `ACT-532` | Deku flight, digits, notes, bubble targets |
| System | `SYS-037`, `SYS-398`, `SYS-1057` | acquired item, magic, retained/discarded fields |
| Constraint | `CON-068`, `CON-282`, `CON-351` | 72 hours, gate order, magic cost |
| Information | `INF-179`, `INF-395` | Town view, clock display |
| Objective | `OBJ-201` | first-dawn retained Ocarina/song |
| Time | `TIM-003` | live clock and pause exceptions |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `394` (`GAME-0001`–`GAME-0394`).
- Exact genome matches: none.
- Tied near matches: `GAME-0344` — Prince of Persia: The Sands of Time (`8 / 25 = 0.320000`).
- Supported combination subsets: none.
- Scan date: 2026-09-24.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0344` — Prince of Persia: The Sands of Time | `ACT-008`, `ACT-161`, `ACT-341`, `SYS-398`, `CON-282`, `INF-179`, `OBJ-201`, `TIM-003` share a live authored route to a retained unique artefact and its first usable power. | The Prince acquires a Dagger that locally rewinds action after an introductory demonstration; this first Clock Town cycle instead requires a learned password, an item trade and a scheduled tower before the Ocarina starts a player-commanded whole-world reset with day-local loss. | Near, `8 / 25 = 0.320000` |

### Preserved research notes

- New genes: `ACT-532`, `SYS-1057`, `INF-395`.
- Evidence and reasoning: separately distinguish ordered non-directional
  submission, chosen reset with durable inventory, and cycle-clock visibility.

## Taxonomy impact

- Registry changes: three new Active IDs; no existing signature changed.
- Taxonomy-change record: `TAXONOMY_CHANGE_133`.
- Candidate terms affected: learned password, played melody, cycle deadline,
  selective reset.

## Negative results

- `TIM-016` and `SYS-140` are explicitly rejected because they would falsely
  portray moonfall as an automatic new run and miss Ocarina retention.
- No separate negative-result record: later masks, bank and temples are
  excluded by the stated packet, not disproven as product mechanics.

## Delta summary

## New facts

- [Confirmed | Direct | High] Nintendo's booklet separates moonfall Game Over
  from the Song-of-Time reset with selected durable inventory (`MM-002`–`MM-004`).

## New genes

- [Observation | Corroborated | High] `ACT-532` and `SYS-1057` isolate player
  submission and reset; [Confirmed | Direct | High] `INF-395` isolates the
  decision-relevant three-day clock.

## New combinations

- [Observation | Limited | Medium] No new combination proposed from one
  bounded prologue; supported older subsets follow the deterministic scan.

## Taxonomy changes

- [Observation | Corroborated | High] `TAXONOMY_CHANGE_133` admits the three
  IDs without modifying earlier signatures.

## New questions

- Which exact Clock Town event-item and bank states survive a first-cycle
  Song reset on each original N64 cartridge revision?

## Next recommended game

- [Hypothesis | Limited | Medium] `GAME-0396` PaRappa the Rapper Remastered.
- Optimisation criterion: alternate the scheduled adventure with a bounded
  rhythm-performance decision loop and distinct visual composition.
- Expected information gain: test input-window and adaptive call-response
  boundaries against already registered musical mechanics.
- Backlog impact: final selected unit of the nine-game horizon.

## Why this game

- [Hypothesis | Limited | Medium] The first three-day cycle isolates a
  verifiable difference between a deadline failure and a deliberately chosen
  loop, without importing every mask, temple or later song.
