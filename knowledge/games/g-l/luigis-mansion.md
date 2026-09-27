---
game_id: GAME-0403
slug: luigis-mansion
game_title: "Luigi's Mansion"
analysis_status: reviewed
reviewed: 2026-09-25
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-341
    - ACT-542
    - ACT-543
    - ACT-544
  system:
    - SYS-578
    - SYS-1079
    - SYS-1080
    - SYS-1081
    - SYS-1082
  constraint: []
  information:
    - INF-401
  objective:
    - OBJ-031
  time:
    - TIM-003
---

# Game: Luigi's Mansion

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Ghost count,
heart power, candle count and room identity are parameters, not genes.

## Analysis scope

- Version / ruleset: original 2001 North American English Nintendo GameCube
  retail rules, Standard control style, first Parlor room after Professor
  E. Gadd's training. The original instruction booklet and Nintendo's
  GameCube product description are primary sources. The exact disc revision
  was not inspected; this is not the 2018 Nintendo 3DS remake, Hidden
  Mansion or a later sequel.
- Structured analysis target: original GameCube retail edition in
  `knowledge/platforms/games.json`; its first post-training Parlor encounter
  is the analysed packet, not every room in the product.
- Entry: Luigi has the Poltergust 3000, flashlight and Game Boy Horror after
  training and re-enters the mansion. The bounded interval starts when he
  first steps into the upstairs Parlor before extinguishing its candles.
- Primary decision loop: move and aim in the darkening room; use suction to
  extinguish the lit candles and trigger a finite ghost appearance; keep the
  flashlight off when needed to let a ghost come close, then aim its beam to
  surprise the ghost and expose its heart; hold vacuum suction while steering
  against its escape direction to drain visible power; repeat until the
  room's ghosts are captured, then open the revealed chest and take its key.
- Positive terminal: all required Parlor ghosts are captured, the room lights
  up and Luigi has claimed the chest key for the next door. Merely surprising
  one ghost, opening an empty chest, or entering the Anteroom is not the
  success condition for this packet.
- Negative terminal: Luigi's health reaches zero before taking the key, which
  ends the attempt. A broken suction hold or one damaging grab is a recoverable
  setback while health remains positive.
- Included: direct movement and aiming, candle extinction by suction, the
  finite Parlor ghost appearance, flashlight suppression and surprise,
  distance-limited exposed-heart capture, continuous counter-steered vacuum
  struggle, ghost power, health damage/terminal, room brightening, revealed
  chest and key collection. Incidental money and furniture searches are not
  needed to clear the room and are excluded.
- Excluded: the foyer/Tutorial itself, Anteroom and later rooms, portrait-ghost
  puzzles, Boo radar and captures, elemental medals/fire/water/ice, key use at
  the next locked door, optional treasure valuation, save/Toad, gallery,
  boss areas, Hidden Mansion, other controller styles and later adaptations.
- Potential scoped modules: a portrait ghost's exposure puzzle, area/boss
  progression, the Boo search loop and the elemental-vacuum loop would each
  require their own bounded evidence before admission.
- Reproducibility: on an original North American GameCube disc with Standard
  controls after a fresh tutorial, record the Parlor's initial candles and
  health, each suction/flashlight input, ghost appearance and heart display,
  distance, sustained counter-steering, remaining power, any contact damage,
  final room-light transition, chest and collected key. Repeat with a close
  and distant flashlight reveal and with/without counter-steering. The
  booklet does not establish an exact frame window or spawn seed; do not
  infer them from this source-only reconstruction.
- Direct-play status: no disc, emulator, gameplay screenshot, video, audio or
  input trace was inspected. The original booklet specifies the capture and
  health rules; Nintendo describes the original light/vacuum struggle; two
  independent contemporary written GameCube routes corroborate the Parlor
  candle, ghost, room-light and key sequence.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `LM-001` | After training, the first upstairs Parlor's candles must be extinguished before its normal ghosts appear. | Observation | Corroborated | High | S1, S2 |
| `LM-002` | Withheld flashlight permits a closer approach; a close ghost surprised by directed light stops and exposes its heart to vacuuming. | Confirmed | Corroborated | High | P1, P2 |
| `LM-003` | Holding R draws an exposed ghost; counter-steering its escape lowers visible power and continued suction captures it at zero. | Confirmed | Direct | High | P1 |
| `LM-004` | A distant lit ghost can show its heart yet remain out of vacuum reach, and a ghost can drag Luigi and cause health loss. | Confirmed | Direct | High | P1 |
| `LM-005` | Capturing the Parlor's finite ghosts brightens the room and reveals a chest containing the key to its next door. | Observation | Corroborated | High | P1, S1, S2 |
| `LM-006` | The current health is visible and reaching zero ends the attempt. | Confirmed | Direct | High | P1 |
| `LM-007` | The original GameCube release uses a flashlight and Poltergust 3000, not the later sequels' Strobulb or Dark-Light device. | Confirmed | Direct | High | P1, P2 |

## Basic data

- Release / origin: Nintendo's original 2001 GameCube game; the selected
  North American retail rules, not a later port or remake.
- Platform or physical form: Nintendo GameCube, `PLAT-NINTENDO-GAMECUBE`.
- Puzzle family: ordered dependency sequencing (`FAM-017`), because candles,
  exposure, capture and room-clear key form a necessary progression chain.
- **[P1]** [Nintendo, original *Luigi's Mansion* instruction
  booklet](https://manualzz.com/doc/22619081/nintendo-luigi-s-mansion-video-game-instruction-booklet),
  pp. 10–13 and 22–25, accessed 2026-09-25. This is a hosted transcription
  of Nintendo's printed primary booklet; OCR artefacts were checked against
  coherent adjacent rule text, not treated as new rules.
- **[P2]** [Nintendo, original GameCube product
  page](https://www.nintendo.com/en-gb/Games/Nintendo-GameCube/Luigi-s-Mansion-268236.html),
  accessed 2026-09-25. It independently describes the original directed
  flashlight, resisting ghosts and vacuum capture. Its European release date
  is not used to date the selected North American disc.
- **[S1]** [Alxs, GameCube written
  route](https://gamefaqs.gamespot.com/gamecube/516494-luigis-mansion/faqs/19088),
  contemporary guide, accessed 2026-09-25, Parlor and Anteroom sections.
- **[S2]** [Kirby021591, GameCube written
  route](https://gamefaqs.gamespot.com/gamecube/516494-luigis-mansion/faqs/34284),
  contemporary independent guide, accessed 2026-09-25, introduction and
  Parlor sections. Its optional money detours are not in this packet.

## Mechanical decomposition

### Action Genes

- Existing `ACT-008`: directly walk Luigi into positions where the candle,
  ghost, chest and exit can be addressed.
- Existing `ACT-341`: open the revealed chest and collect the key; ordinary
  object interactions are not vacuum or light commands.
- New `ACT-542`: aim the Poltergust suction at lit Parlor candles to
  extinguish them. This is a world-fixture manipulation, not tank storage.
- New `ACT-543`: withhold then direct the handheld flashlight to a nearby
  ghost. Timing and angle control whether its heart becomes usable.
- New `ACT-544`: hold suction on an eligible ghost while steering opposite
  its escape; simply pointing at it does not complete capture.

### System Behaviour Genes

- Existing `SYS-578`: one health pool falls from ghost contact or dragging
  and zero ends this live attempt. No shield or life stock is inferred.
- New `SYS-1079`: extinguishing the authored candle set changes the Parlor
  to dark and releases its finite normal-ghost encounter.
- New `SYS-1080`: a close directed flashlight surprise stops a ghost and
  exposes its heart for a bounded capture opportunity; a distant reveal can
  fail to put the ghost within vacuum reach.
- New `SYS-1081`: sustained suction plus opposite steering counters an
  escaping ghost and lowers its visible power; zero followed by continued
  suction captures it, while a lost hold leaves it active.
- New `SYS-1082`: once the Parlor's final required ghost is captured, the
  room illuminates and the authored key chest becomes available.

### Constraint Genes

- No separate new constraint: heart exposure, suction reach and zero-health
  failure are operative gates within `SYS-1080`, `SYS-1081` and `SYS-578`.
  The next door's key requirement is outside the chosen terminal.

### Information Genes

- New `INF-401`: the view and HUD show Luigi's current health, dark/light
  room state, visible ghosts, their exposed hearts and remaining power
  during suction. Future ghost appearance timing and exact frame windows
  are not promised as previews.

### Objective Genes

- Existing `OBJ-031`: complete the Parlor's ordered authored task set:
  extinguish candles, capture all required ghosts and take the revealed key.
  Ghost capture alone is insufficient before the candle trigger or without
  claiming the key.

### Time Genes

- Existing `TIM-003`: ghosts move, attack or struggle during the same live
  interval in which Luigi aims light, holds suction and counters their pull.

## Reproducible transitions

| Before | Action | Bounded resolution | Establishes | Claim |
|---|---|---|---|---|
| First Parlor entry, candles lit | Aim suction over the candle set | Flames go out; the room darkens and finite normal ghosts appear | authored trigger before combat | `LM-001` |
| A normal ghost is approaching, flashlight withheld | move close and direct light at it | the surprised ghost stops and its heart appears | light-gated vulnerability | `LM-002` |
| A ghost is far from Luigi when lit | aim suction without closing distance | the exposed heart can be visible while suction fails to catch at that range | exposure is not unlimited capture reach | `LM-004` |
| Exposed nearby ghost retains power | hold R and steer opposite escape | resistance is overcome, power falls, then continued suction captures at zero | coupled capture contest | `LM-003` |
| Ghost drags Luigi while capture is incomplete | continue an unsuccessful hold | Luigi can lose health; zero would terminate the attempt | encounter risk | `LM-004`, `LM-006` |
| Last required ghost is captured | allow room settlement | lights come on and the key chest appears | finite room-clear result | `LM-005` |
| Cleared Parlor, chest present | open chest and collect key | key becomes carried state; this packet ends before opening the next door | positive terminal | `LM-005` |

## Edge-case audit

- A lit ghost at long range can expose a heart without being capturable yet;
  approach distance and surprise timing are distinct from simply holding R.
- Releasing or losing the vacuum hold before power reaches zero does not count
  as capture. Counter-steering affects depletion; it is not a separate
  flashlight stun.
- The portrait ghosts in the frames are not the three normal ghosts the
  first Parlor releases. Their later individual exposure puzzles are excluded.
- The optional chest's exact appearance/lighting order is not inferred
  beyond their common final-ghost clearance dependency; the two written
  routes differ on whether taking the key or the final capture coincides
  with the light cue. Either way, the terminal requires both cleared room
  and collected key.
- The booklet describes Boos in brightened rooms later in the campaign;
  there is no Boo hunt in this first Parlor packet.

## Strategic and experiential structure

- Local decision: keep the light off long enough to invite a close ghost,
  then reveal its heart and maintain opposing suction without being dragged.
- Medium-term planning: clear the finite room while protecting Luigi's one
  health pool, then claim the next-door key rather than wandering to an
  optional reward.
- Long-term structure: the key supports a later room; that later encounter
  and campaign rescue are outside this record.
- Failure attribution: visible heart power and health make a lost tug or
  damaging contact distinguishable from a missed candle/room trigger.
- Player-trust factors: the booklet states that distant exposure is not enough
  to vacuum and teaches counter-steering; exact unseen frame windows are
  deliberately not presented as established facts.

## Replay and variation

- The authored Parlor dependency is stable; approach, lighting timing,
  counter-steering and damage can differ by play. No random ghost count or
  encounter probability is inferred for this fixed first room.
- A repeat trace could measure exact exposure duration and spawn placement;
  the printed source does not establish those values.

## Adjacent systems and history

- *Slime Rancher* also has aimed suction, but its `ACT-467` transfers loose
  objects into a selected typed tank and can expel them. Luigi's ghost
  capture is a live exposure-and-resistance contest, not a reversible tank
  inventory transfer.
- *The Binding of Isaac: Rebirth* settles a cleared combat room, but
  `SYS-465` opens ordinary exits and may sample rewards. This Parlor instead
  brightens and reveals an authored key chest after a light/vacuum chain.
- The selected GameCube flashlight is not the charged Strobulb or Dark-Light
  device of later Luigi games; sequel rules must not enter this signature.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-341`, `ACT-542`–`ACT-544` | candle set, close approach, steering direction |
| System Behaviour | `SYS-578`, `SYS-1079`–`SYS-1082` | finite ghosts, heart power, light duration, health |
| Constraint | none | exposure/reach are resolution gates, not a second gene |
| Information | `INF-401` | hearts, power, health and room illumination |
| Objective | `OBJ-031` | clear first Parlor and claim its key |
| Time | `TIM-003` | uninterrupted live struggle |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `402` (`GAME-0001`–`GAME-0402`).
- Exact genome matches: none.
- Tied near matches: `GAME-0270` — Risk of Rain 2 (`4 / 22 = 0.181818`).
- Supported combination subsets: none.
- Scan date: 2026-09-25.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0270` Risk of Rain 2 | `ACT-008`, `ACT-341`, `SYS-578`, `TIM-003` | Both use live movement, contextual interaction and one health pool, but Risk of Rain 2 builds a longer combat run around item growth and a teleporter, while this bounded first-Parlor route exposes ghosts with light, contests vacuum capture and unlocks a key after a finite room clear. Shared generic rules do not imply interchangeable moment-to-moment play. | Nearest by Jaccard (`4 / 22 = 0.181818`), not a strong mechanical match. |

## Taxonomy impact

- Registry changes: eight Active genes: `ACT-542`–`ACT-544`,
  `SYS-1079`–`SYS-1082`, `INF-401`.
- Taxonomy-change record: `TAXONOMY_CHANGE_141`.
- Candidate terms affected: environmental suction, flashlight exposure,
  contested capture and room-clear illumination/key reward.

## Negative results

- None: no earlier signature or verified combination is revised.

## Delta summary

## New facts

- [Confirmed | Direct | High] The original booklet distinguishes visible
  heart exposure from reachable suction and teaches counter-steering
  (`LM-002`–`LM-004`).

## New genes

- [Observation | Corroborated | High] Eight bounded genes capture the
  first-room light-and-vacuum dependency instead of adding a generic
  "ghost" or "haunted room" tag.

## New combinations

- [Observation | Corroborated | High] No new combination proposed.

## Taxonomy changes

- [Observation | Corroborated | High] `TAXONOMY_CHANGE_141` adds eight
  boundaries without changing an earlier signature.

## New questions

- What exact original-disc frame window and counter-steering cadence govern
  capture speed for each normal ghost in the Parlor?

## Next recommended game

- [Hypothesis | Limited | Medium] `GAME-0404` *Ratchet & Clank*.
- Optimisation criterion: move from a single fixed ghost room to a bounded
  PS2 planet route combining traversal, weapon switching and a gadget gate.
- Expected information gain: test whether reusable movement and targeted
  attacks suffice or whether equipment-gated route progress adds a new
  boundary.
- Backlog impact: no selected subject displaced.

## Why this game

- [Hypothesis | Limited | Medium] The original first room isolates a familiar
  exposure-and-capture interaction while excluding later portrait, elemental
  and Boo systems that would turn the whole product into an over-broad genome.
