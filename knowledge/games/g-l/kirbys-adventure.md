---
game_id: GAME-0408
slug: kirbys-adventure
game_title: Kirby's Adventure
analysis_status: reviewed
reviewed: 2026-09-26
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-190
    - ACT-548
    - ACT-549
  system:
    - SYS-036
    - SYS-045
    - SYS-578
    - SYS-911
    - SYS-1090
    - SYS-1091
  constraint:
    - CON-697
  information:
    - INF-192
    - INF-404
  objective:
    - OBJ-240
  time:
    - TIM-003
---

# Game: Kirby's Adventure

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Beam, Vegetable
Valley, the initial six vitality bars and the name Waddle Doo are parameters,
not one-off gene types.

## Analysis scope

- Version / ruleset: Nintendo's original 1993 North American NES *Kirby's
  Adventure* Game Pak, as documented in Nintendo's preserved original
  instruction booklet. The selected one-player route is Level 1 Vegetable
  Valley stage `1-1`, not the later GBA *Nightmare in Dream Land* remake or
  an emulator-only save-state layer. Exact cartridge ROM revision is untested.
- Structured analysis target: `PLAT-NINTENDO-ENTERTAINMENT-SYSTEM` in
  [`knowledge/platforms/games.json`](../../platforms/games.json).
- Primary decision loop: read the live side-view route; walk and jump or
  inflate and flap over a high obstacle; while Normal, inhale one reachable
  Waddle Doo and choose swallowing over firing it as a star; use the resulting
  Beam capability against a later reachable enemy; protect the current
  vitality and ability as enemies keep moving; take the final stage door and
  settle the post-stage goal jump to expose the next map doors.
- Entry: choose an empty file, enter the first visible Level 1 map door and
  accept first control in stage `1-1` with Normal form and the manual's
  six-bar initial vitality. Record the displayed initial life stock rather
  than assuming a value from an unplayed cartridge.
- Positive terminal: enter the fixed final stage door, press A once at the
  post-clear jump prompt without requiring a particular bonus height, and
  return to Level 1's expanded map with `1-1` marked clear and more doors
  available. Obtaining Beam is a route commitment, not an independent victory.
- Failure and recovery control: a separate branch allows a hostile hit while
  Beam is active, confirms loss of the ability and optionally inhales the
  emitted star to recover it. A second branch follows depleted vitality or
  a fall to loss of one finite life and same-stage return while stock remains;
  no claim is made about the exact intra-stage respawn coordinates. These
  branches are reset before the positive route. Game Over after all lives are
  exhausted is the negative terminal for this bounded stage attempt.
- Included: direct side-view movement, gravity and collidable ground, Normal
  inflation/flapping and optional air-pellet deflation, autonomous local
  enemies, Normal-only inhalation, one mouth-held enemy, swallow versus star
  expulsion, Waddle Doo-to-Beam copying, Beam activation, damage/SELECT
  ability loss and recoverable star, vitality and finite lives, the current
  HUD, final door, goal jump and map-door reveal.
- Excluded: exact enemy damage or frame timings not established by the manual;
  alternate copied powers, multi-enemy random-copy result, optional Maximum
  Tomato detour and secret items, underwater route, bonus-game optimisation,
  boss encounters, later Vegetable Valley stages, complete Star Rod campaign,
  audiovisual interpretation, glitches, emulator rewind/save states and
  subsequent remakes or series titles.
- Potential scoped modules: a fixed later stage with a different copy ability;
  a secret-exit or boss packet; the post-stage jump as an optimised bonus-life
  challenge rather than mere closeout.
- Reproducible parameterisation: record cartridge or lawful wrapper identity,
  file slot, entry vitality/lives, chosen Waddle Doo position, each inhale,
  swallow, Beam invocation, damage/discard and recovery branch, high-wall
  flight, final door, goal-jump input, displayed clear flag and new map doors.
  If an inspected build's `1-1` route differs from the written NES guide,
  reopen stage-local claims without inventing a new ruleset.
- Direct-play status: none. No cartridge, ROM, emulator, video, audio,
  screenshot or controller trace was opened. Original Nintendo manual pages
  were read as a scanned document; a contemporary written original-NES
  walkthrough supports the particular stage route. This is a bounded
  reconstruction, not a claimed playthrough or binary audit.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `KAD-001` | An empty file opens at Level 1's first visible door; clearing one stage marks it and reveals more map doors. | Confirmed | Direct | High | P1, P2 |
| `KAD-002` | Normal Kirby can inflate with Up, flap with A and fire an air pellet with B, which deflates him. | Confirmed | Direct | High | P1, P2 |
| `KAD-003` | B inhales a nearby eligible enemy/block; B expels the held body as a star, whereas Down swallows it. | Confirmed | Direct | High | P1, P2 |
| `KAD-004` | Swallowing an ability-bearing enemy grants its typed copied ability, usable with B; an active copy prevents further inhalation. | Confirmed | Direct | High | P1, P2 |
| `KAD-005` | A hit or SELECT drops a copied ability as a star; inhaling and swallowing that star can restore it. | Confirmed | Direct | High | P1, P2 |
| `KAD-006` | The bottom HUD exposes vitality, remaining lives and Normal/copied state; depleted vitality or a fall costs a life. | Confirmed | Direct | High | P1, P2 |
| `KAD-007` | Every cleared stage presents a timed A-button goal jump; a perfect height gives a bonus life, but the route needs no perfect result. | Confirmed | Direct | High | P1 |
| `KAD-008` | Original NES Vegetable Valley `1-1` has an early Waddle Doo granting Beam, a high wall and later final door; exact placements are guide-level, not direct-play observations. | Observation | Corroborated | Medium | S1, P1 |
| `KAD-009` | The selected packet can demonstrate inhale → copy → use → optional loss/recovery while traversing one live stage and retaining its clear on the expanding map. | Strong Pattern | Corroborated | Medium | `KAD-001`–`KAD-008` |

## Basic data

- Release / origin: HAL Laboratory/Nintendo's original NES adventure, 1993;
  Nintendo's preserved original manual identifies the North American Game
  Pak as `NES-KR-USA`.
- Platform or physical form: single-player North American NES cartridge;
  any current licensed wrapper is a way to access the old game, not evidence
  for wrapper-only mechanics.
- Mechanical family: physics and object manipulation; real-time system
  pressure.
- Official rules, accessed 2026-09-26:
  - **P1:** [Nintendo's preserved original NES instruction
    booklet](https://www.nintendo.co.jp/clv/manuals/en/pdf/CLV-P-NAAPE.pdf),
    especially printed pp. 11, 14–22, 25 and 28. It directly documents the
    map, controls, inhale/swallow/copy, vitality, lives, goal jump and save
    behaviour. The scanned PDF was visually inspected and OCR used only as
    reading aid, not as a game execution trace.
  - **P2:** [Nintendo's abbreviated official controls and rules
    guide](https://www.nintendo.co.jp/clv/manuals/en/pdf/CLV-P-NAAPE_en.pdf),
    for an independently text-readable version of the input, copy, loss and
    stage-map rules. Its summary's boss-count wording is not used for this
    first-stage packet.
- Independent route account, accessed 2026-09-26:
  - **S1:** [Brian Sulpher's original-NES *Kirby's Adventure*
    walkthrough](https://gamefaqs.gamespot.com/nes/563432-kirbys-adventure/faqs/28822),
    first submitted in 2004; its Vegetable Valley `1-1` route places Waddle
    Doo/Beam early, a high wall and the subsequent doors. A guide is not a
    byte-exact map of an uninspected ROM revision.
- Reproducible control: source-side transition tracing under the stated
  entry and terminals; no direct play or audiovisual evidence.
- Claim IDs: `KAD-001`–`KAD-009`.

## Mechanical decomposition

### Action Genes

- Reused `ACT-008`: steer the same avatar horizontally and by jumping along
  local stage geometry; flight is separately controlled rather than an
  automatic destination path.
- Reused `ACT-190`: after Beam has been copied, commit its B-button active
  effect toward the current reachable threat. Beam's appearance is a
  parameter, not a new generic activation verb.
- New `ACT-548`: Normal-form inflation, repeated A flaps and optional
  air-pellet deflation make the high wall traversable without a pickup.
- New `ACT-549`: inhale one Waddle Doo into Kirby's own mouth, then choose
  Down to swallow or B to expel it as a star. The chosen route swallows.
- Claim IDs: `KAD-002`–`KAD-004`, `KAD-008`.

### System Behaviour Genes

- Reused `SYS-036`: gravity, jump arcs, support and collision keep movement
  live between input changes; exact physics constants are not claimed.
- Reused `SYS-045`: eligible stage enemies move without a command from Kirby.
- Reused `SYS-578`: enemy hits reduce one six-bar vitality pool; health zero
  ends the current life. The optional Maximum Tomato is outside this route.
- Reused `SYS-911`: a depleted bar or lethal fall consumes a finite life and
  permits same-stage return while stock remains, separate from Game Over.
- New `SYS-1090`: swallowing Waddle Doo installs Beam into the one current
  copied-ability slot; a non-bearing enemy would not supply it.
- New `SYS-1091`: hit or SELECT discards Beam into a reclaimable star;
  inhaling and swallowing the star restores the copy.
- Resolution order: movement/enemy advance → contact or inhalation → held
  swallow/expulsion → copied ability activation or damage/drop → vitality/life
  resolution → final door and goal jump → map clear/reveal.
- Claim IDs: `KAD-002`–`KAD-006`.

### Constraint Genes

- New `CON-697`: inhale requires Normal form, a reachable eligible target
  and free mouth; another enemy cannot be held before this one is resolved.
  An active Beam routes B to the copied attack instead of a new inhale.
- Claim IDs: `KAD-003`–`KAD-005`.

### Information Genes

- Reused `INF-192`: the side-view camera exposes a local slice of support,
  enemies, high wall and doors rather than the full future stage.
- New `INF-404`: the live bottom display exposes vitality, lives and Normal
  or Beam, making the inhale gate and risk of another hit observable.
- Claim IDs: `KAD-006`, `KAD-008`.

### Objective and Time Genes

- New `OBJ-240`: finish one stage through its final door and goal-jump
  closeout, then observe the flag and new doors on the Level 1 map. The
  bonus height is optional and no later stage has yet been entered.
- Reused `TIM-003`: stage enemies, movement and damage continue in real time
  while the player decides whether to copy, fight or fly.
- Claim IDs: `KAD-001`, `KAD-007`, `KAD-008`.

## Reproducible transitions

| Before | Action | Bounded resolution | Establishes | Claim |
|---|---|---|---|---|
| Empty file and first Level 1 map door | Press Up at that door | Enter `1-1` in Normal form with the initial vitality display | Reproducible route entry | `KAD-001`, `KAD-006` |
| Normal body near the first eligible Waddle Doo | Press B toward it | One enemy becomes mouth-held; B or Down now resolves it | Held body is not yet a copied ability | `KAD-003`, `KAD-008` |
| Waddle Doo held | Press Down | Enemy is consumed and Beam replaces Normal on the ability display | Typed copy acquisition | `KAD-004` |
| Beam active and a later enemy reachable | Press B | The Beam action is invoked; the exact damage timing depends on the target | Copied command changes the action set | `KAD-004` |
| Beam active in a safe control branch | Press SELECT | Beam is lost, a recoverable star appears and Kirby returns to Normal | Deliberate loss without lethal damage | `KAD-005` |
| Recoverable Beam star reachable | Inhale and swallow it | Beam returns if the star is claimed before loss | Ability recovery is an action, not automatic | `KAD-005` |
| Normal form at the high wall | Press Up, then repeated A | Inflated body gains altitude; optional B air pellet deflates it | Native flight, not a pickup power | `KAD-002`, `KAD-008` |
| Vitality reaches zero or Kirby falls | No rescue available | One life is consumed; with stock left, this stage may be retried | Health and finite lives are separate | `KAD-006` |
| Final door reached | Enter it and press A once at goal jump | Stage clear settles, map gains a flag and additional doors | Stage/map objective rather than boss defeat | `KAD-001`, `KAD-007` |

## Strategic and experiential structure

- Local decision: a normal body can turn a nearby enemy into an attack star or
  into the enemy's ability. Copying Beam helps combat but makes inhalation
  unavailable until the copy is lost or discarded.
- Medium-term planning: preserve vitality while crossing enemies and a high
  wall; deliberate SELECT may exchange Beam for immediate inhale/flight
  options, and a recoverable star can undo the loss if reached in time.
- Long-term structure: this one stage's clear flag and newly visible map
  doors persist beyond its end, though later choices and the Star Rod quest
  are outside the packet.
- Failure attribution: a lost life comes from a depleted vitality bar or
  fall; a lost Beam can occur earlier without ending the life. Neither is
  conflated with reaching the stage exit.
- Player trust: the visible ability name and vitality display tell the player
  whether inhalation is currently available and how much hostile contact can
  be tolerated; off-screen future geometry is not disclosed.
- Claim IDs: `KAD-001`–`KAD-009`.

## Replay and variation

- A Waddle Doo can be swallowed for Beam or expelled as a star; the route's
  mandatory demonstration chooses Beam. Other enemy abilities are excluded.
- The post-stage jump can award a different bonus by timing, but any legal
  result suffices for the selected map reveal.
- No claim is made that Stage `1-1` enemy placements, vitality damage amounts
  or bonus timings were measured from a specific executable revision.

## Adjacent systems and history

- *Super Mario World* also has a mouth-held body and platform exit, but
  `ACT-493`, `CON-660` and `SYS-978` belong to a mounted companion. Kirby's
  own body inhales and turns a swallowed hostile into his active ability.
- `SYS-902` converts collected pickups into platform powers; Beam comes from
  swallowing a typed enemy and can reappear as a recoverable star after a hit.
- `ACT-473` requires a temporary inflation capability; Kirby can inflate in
  his ordinary Normal form, so that narrower acquired-form boundary is not
  stretched to fit.

## Normalised genome

The front matter is canonical: fifteen Active genes. Eight transfer from
existing platform, health and real-time boundaries; seven newly isolate
native inflation, own-body inhalation, typed enemy copy, recoverable copy
loss, inhale legality, the ability/vitality HUD and stage-to-map reveal.

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `407` (`GAME-0001`–`GAME-0407`).
- Exact genome matches: none.
- Tied near matches: `GAME-0389` — Mega Man 2 (`7 / 24 = 0.291667`).
- Supported combination subsets: none.
- Scan date: 2026-09-26.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0389` — Mega Man 2 | `ACT-008`, `SYS-036`, `SYS-045`, `SYS-578`, `SYS-911`, `INF-192`, `TIM-003` | Both steer a visible platform avatar under gravity past live enemies while health and finite lives price mistakes. Mega Man 2 chooses a starting boss stage, spends selectable armament and defeats Metal Man for a permanent stage reward; Kirby inhales a stage enemy for a replaceable Beam copy, can lose and reclaim it, flies in Normal form and clears an ordinary door into a growing map. | Near, `7 / 24 = 0.291667` |

## Taxonomy impact

`TAXONOMY_CHANGE_146` adds seven Active genes without changing an older
signature or verified combination.

## Negative results

- No direct NES play or ROM inspection established exact `1-1` positions,
  frame windows, life-return coordinate or post-stage bonus score.
- The abbreviated official manual's campaign boss-count summary is not
  transferred to this first-stage scope; the original manual's map and
  controls are authoritative for the stated Game Pak.
- Waddle Doo, Beam, the number of vitality bars and one high wall are bounded
  parameters. No named-enemy or named-ability gene is created.

## Delta summary

An enemy encountered on a live platform route can be swallowed to change
Kirby's available command, and that copied power can later be lost and
reclaimed. The stage ends through a door and map expansion, not by defeating
the campaign boss.

## New facts

- [Confirmed | Direct | High] Nintendo's original booklet explicitly
  separates inhale, held-mouth swallow/expulsion, copied ability use,
  hit/SELECT drop and recoverable star (`KAD-002`–`KAD-005`).

## New genes

- [Observation | Direct | High] `ACT-548`, `ACT-549`, `SYS-1090`,
  `SYS-1091`, `CON-697`, `INF-404` and `OBJ-240` isolate the distinct
  first-stage transitions.

## New combinations

- [Observation | Direct | High] No new verified combination.

## Taxonomy changes

- [Observation | Direct | High] `TAXONOMY_CHANGE_146` adds seven Active
  boundaries; older signatures stay unchanged.

## New questions

- Does the exact original North American cartridge revision place the first
  Waddle Doo and high wall as the written guide describes?
- What exact state and position persist after a nonterminal life loss or
  post-stage goal-jump result in that revision?

## Next recommended game

- [Hypothesis | Limited | Medium] `GAME-0409` *Twisted Metal: Black*.
- Optimisation criterion: change from a side-view inhalation/copy route to
  vehicle-combat arena selection and damage pressure on PlayStation 2.
- Expected information gain: test whether weapon pickups and vehicle-specific
  special attacks transfer to existing combat and finite-life boundaries.
- Backlog impact: no selected subject displaced.

## Why this game

- [Hypothesis | Corroborated | Medium] A directly controlled mouth copies
  enemy powers and can later reclaim a lost copy. That causal sequence is not
  captured by a generic platform power-up or mounted companion's shell.

## Next test

Use an identified lawful original NES build to log the exact first Waddle
Doo, ability transition, SELECT star recovery, high-wall flight, life-loss
return and stage-to-map closeout; revise only claims contradicted by that
trace.
