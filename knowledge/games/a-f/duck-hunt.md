---
game_id: GAME-0345
slug: duck-hunt
game_title: "Duck Hunt"
analysis_status: reviewed
reviewed: 2026-09-21
combination_ids: []
gene_ids:
  action:
    - ACT-490
  system:
    - SYS-045
    - SYS-967
    - SYS-968
    - SYS-969
  constraint:
    - CON-658
  information:
    - INF-366
  objective:
    - OBJ-002
    - OBJ-202
  time:
    - TIM-003
---

# Game: Duck Hunt

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Ducks, hound,
Zapper, CRT, black/blue/red colour classes and PASS LINE are carrier
parameters, not gene names.

## Analysis scope

- Version / ruleset: original North American English Nintendo Entertainment
  System Duck Hunt Game Pak documented by the ©1985 Nintendo instruction
  booklet, one-player `GAME A`, default round-one rules. The program binary was
  not extracted, executed or hashed; the exact physical ruleset is frozen from
  the identified booklet and Nintendo's retrospective original-hardware page.
- Structured analysis target: one first round on
  `PLAT-NINTENDO-ENTERTAINMENT-SYSTEM`, using the NES Zapper in controller port
  2 and a compatible correctly adjusted CRT display; see `GAME-0345` in
  [`knowledge/platforms/games.json`](../../platforms/games.json).
- Primary decision loop: follow the single moving duck, physically aim the
  Zapper at its displayed position and pull the trigger before either three
  shots or the short flight opportunity ends; read hit lamps and PASS LINE,
  then repeat through ten separately settling ducks.
- Entry: `GAME A` has been selected and started; round one begins when the
  hound enters the thicket and the first duck is about to rise.
- Positive terminal: the tenth duck settles with at least six red hit lamps;
  the PASS LINE check advances the run to the round-two ready state. Stop
  before the first round-two duck rises.
- Negative terminal: the tenth duck settles with fewer than six hits and the
  game enters Game Over.
- Included: one duck at a time; varying rise locations and live flight; black,
  blue and red target classes; physical Zapper aim and trigger; display-light
  sensing on compatible original hardware; target-local three-shot allowance;
  timeout or shot-exhaustion escape; hit/miss settlement; ten target lamps;
  round-one PASS LINE of six; hit score, round score and first-round PERFECT
  bonus; round number and remaining-shot display; pause only as documented
  context, not as a strategy claim.
- Excluded: `GAME A` two-player duck control; `GAME B`; `GAME C`; rounds two
  and later; later speed, value and PASS LINE changes; arcade `VS. Duck Hunt`;
  Famicom release-specific hardware; Wii U Virtual Console pointer, reticle,
  save-state and controller substitutions; clone guns; flat-panel adapters;
  emulation, ROM modifications, light-source exploits, glitches and exact
  undocumented hitbox or scanline tolerances.
- Reproducible parameterisation: connect the original Zapper to controller
  socket 2; use a compatible CRT with brightness and contrast adjusted so
  shots register; select and start `GAME A`; for each one-at-a-time duck,
  choose zero to three trigger pulls during its visible flight; record its red
  hit lamp or miss; after the tenth settlement, record advance at six or more
  hits and Game Over below six. A ten-for-ten round additionally receives the
  documented PERFECT bonus.
- Potential scoped modules: a controlled original-hardware timing capture,
  complete ROM disassembly, `GAME A` two-player control, `GAME B`, `GAME C`,
  later-round speed/quota progression, Famicom hardware and Wii U Virtual
  Console adaptation each require separate evidence and boundaries.
- Direct-play status: not conducted. No cartridge, NES/Famicom console,
  Zapper, compatible CRT, ROM, emulator, controller trace, save, screenshot,
  video or audio was used. The repository control validates a sourced state
  model, not Nintendo program code, photodiode thresholds, screen timing or
  physical shot accuracy.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `DH-001` | The selected product is the original English NES Duck Hunt Game Pak requiring the Zapper light-gun attachment | Confirmed | Direct | High | P1, P2 |
| `DH-002` | Game A presents one duck at a time from varying rise locations and allows two-player duck control only in the excluded branch | Confirmed | Direct | High | P1, P2 |
| `DH-003` | A compatible physical setup points and fires the Zapper at the television; screen adjustment affects whether shots register | Confirmed | Direct | High | P1, P2 |
| `DH-004` | The NES Zapper exposes trigger and CRT-light state, and the documented game sequence can distinguish darkness from a target-localised light response | Observation | Corroborated | High | P2, S1 |
| `DH-005` | Each Game A duck flies for a few seconds and settles immediately on hit, after three misses or when time expires | Confirmed | Direct | High | P1, P2 |
| `DH-006` | One round contains ten separately settling ducks and exposes shots left, hit lamps, PASS LINE, round and score | Confirmed | Direct | High | P1, P2 |
| `DH-007` | Round one requires at least six hits to advance; fewer than six produces Game Over | Observation | Corroborated | High | P2, S2 |
| `DH-008` | First-band black, blue and red ducks award 500, 1000 and 1500 points; a no-miss first round adds 10,000 PERFECT points | Observation | Corroborated | High | P2, S2 |
| `DH-009` | The bounded packet stops at the advance or Game Over result and imports no later-round speed or quota | Confirmed | Direct | High | P2, R1 |
| `DH-010` | The repository control proves ten-target sequencing, sensor-position hit settlement, three-shot and timeout miss paths, six-hit qualification, failure, colour score and perfect bonus | Observation | Direct | High | V1, DH-005–DH-009 |
| `DH-011` | No original hardware, program image, emulator or audiovisual trace was inspected | Confirmed | Direct | High | R1 |

## Basic data

- Release / origin: Nintendo's original-hardware page identifies the Japanese
  Family Computer release on 1984-04-21; the selected English manual identifies
  the North American NES Game Pak and ©1985 Nintendo. The Japanese release is
  product history, not the selected physical target.
- Platform or physical form: original North American Nintendo Entertainment
  System Game Pak, English booklet, NES Zapper in controller socket 2 and a
  compatible CRT television.
- Puzzle family: real-time system pressure; tactical forecast and counterplay.
- Primary and official sources, accessed 2026-09-21:
  - **[P1]** [Nintendo's original Famicom Duck Hunt
    page](https://www.nintendo.com/jp/famicom/software/hvc-dh/index.html),
    which explicitly says its rules and gun instructions are based on the
    contemporary manual, for original product identity, Game A one-duck
    release, varying starts, short flight, three shots, timeout escape, hit
    lamps, PASS LINE, CRT range and brightness/contrast/angle conditions.
  - **[P2]** [preserved original English NES instruction booklet
    scan](https://www.nesfiles.com/NES/Duckhunt/Duckhunt.pdf), pp. 2–9, for
    the exact selected Game Pak, controller socket, Zapper operation, Game A
    rules, one duck, three shots, timeout, hit lamps, ten-duck round, PASS LINE,
    screen labels, scoring classes, PERFECT bonus and later-round exclusions.
  - **[P3]** [Nintendo UK's licensed Duck Hunt product
    page](https://www.nintendo.com/en-gb/Games/NES/Duck-Hunt-946955.html), for
    independent official NES identity, Zapper history and A/B/C distinctions;
    its Wii U distribution is outside the selected target.
- Reproducible secondary sources, accessed 2026-09-21:
  - **[S1]** [NESdev Zapper technical
    reference](https://www.nesdev.org/wiki/Zapper), for the trigger/light bits,
    CRT-frequency light sensing, display-lag limitation and reproducible
    darkness-plus-target-light sequence. It defines a hardware/programming
    interface, not a claim that this unit executed Duck Hunt code.
  - **[S2]** [NinDB Game A guide](https://nindb.net/guides/duck-hunt/game-a.html),
    for the independently tabulated round-one PASS LINE of six, first-band
    colour values and 10,000-point PERFECT bonus. NinDB is explicitly
    independent and is used only where the preserved manual's prose or
    labelled image does not expose the exact table in extracted text.
- Reproducible control: **[V1]**
  [`verify_duck_hunt_control.py`](../../../scripts/verify_duck_hunt_control.py),
  an executable source-model control for ten target opportunities, light-sample
  hit coordinates, three-shot and timeout misses, quota settlement, score and
  perfect bonus.
- Research record: **[R1]** local preflight found no cartridge image, console
  capture, Zapper trace, emulator state, screenshot, video or audio.
- Claim IDs: `DH-001`–`DH-011`.

## Mechanical decomposition

### Action Genes

- New `ACT-490` owns the physical aim-and-trigger request through an external
  display-sensing light gun. It is not ordinary `ACT-161`: the player does not
  steer a software weapon or cursor, and spatial aim is sampled from the
  display/light-gun relation.
- Duck identity, accepted range and trigger hardware are parameters. Menu
  selection occurs before the packet and is not admitted as a recurring gene.
- Claims: `DH-003`, `DH-004`.

### System Behaviour Genes

- `SYS-045` owns time-driven duck motion while input remains possible. New
  `SYS-967` owns display/light-sensor hit adjudication; it deliberately stops
  short of unsupported exact hitbox or scanline constants.
- New `SYS-968` releases and settles ten separate one-duck opportunities. New
  `SYS-969` maps credited hit class to round-one points and adds the no-miss
  PERFECT bonus.
- Dog animations, sky-colour change and laughs communicate settlement but do
  not create separate causal boundaries.
- Claims: `DH-004`–`DH-008`.

### Constraint Genes

- New `CON-658` combines the two independent target-local closures: no more
  than three shots and no input after the short live opportunity expires. A
  first hit also settles the duck, so unused shots cannot transfer.
- The round-wide PASS LINE is objective settlement, not ammunition or a
  fourth shot. Game B's shared three-shot rule is excluded.
- Claims: `DH-005`, `DH-006`.

### Information Genes

- New `INF-366` joins visible duck flight with shots left, the ten ordered hit
  lamps, PASS LINE, round and score. The original NES target has no software
  aiming cursor, so the Wii U reticle is excluded rather than imported.
- Exact hidden flight path and remaining seconds are not disclosed.
- Claims: `DH-005`, `DH-006`.

### Objective Genes

- New `OBJ-202` settles a fixed schedule by minimum hit count: six of ten is
  enough, but five is failure and perfect clearance is not required.
- `OBJ-002` separately owns voluntary score maximisation through higher-valued
  duck classes and the perfect bonus. Score cannot substitute for six hits.
- Claims: `DH-007`–`DH-009`.

### Time Genes

- `TIM-003` owns the live opportunity in which target position and remaining
  duration change while the player aims. The packet is not turn-based merely
  because targets appear sequentially.
- The documented pause command is an outer rate control; no strategy depends
  on pause, and the model makes no frame-perfect timing claim.
- Claims: `DH-005`, `DH-006`.

## Reproducible transitions

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Round one has started and no duck is active | Allow the hound/round sequence to release the next target | One duck rises from a varying location and begins live flight | separately released target opportunity | `DH-002`, `DH-005` |
| One duck is active and its displayed region is sampled by the Zapper shot | Aim at that region and pull the trigger | The light-sensor response credits a hit, turns the corresponding lamp red and ends the opportunity | hardware-mediated spatial shot resolution | `DH-003`, `DH-004` |
| One duck is active and the sampled region does not correspond to it | Pull the trigger once | One of three local shots is consumed; the duck continues if time and shots remain | a miss does not end the opportunity before its local allowance closes | `DH-005` |
| Two local shots have missed while time remains | Fire one more non-hit shot | The third miss exhausts the opportunity, the duck escapes and the current lamp remains uncredited | exact shot-exhaustion miss terminal | `DH-005`, `DH-006` |
| Fewer than three shots were used but the duck's interval expires | Do not produce a credited hit before timeout | The sky changes, the duck escapes and the current lamp remains uncredited | time is an independent opportunity terminal | `DH-005` |
| A black, blue or red round-one duck is hit | Accept the hit settlement | The corresponding 500, 1000 or 1500 points are added | target class changes optional score, not hit count | `DH-008` |
| The tenth duck settles with six hit lamps | Accept round settlement | PASS LINE is reached and the run advances to round two | exact positive terminal | `DH-007`, `DH-009` |
| The tenth duck settles with five hit lamps | Accept round settlement | PASS LINE is not reached and Game Over replaces round advance | exact negative terminal | `DH-007`, `DH-009` |
| The tenth duck settles with ten hit lamps | Accept round settlement | The round advances and adds the first-band 10,000-point PERFECT bonus | complete accuracy is rewarded but not required | `DH-008` |

## Strategic and experiential structure

- Local decision: track one visible moving target and decide when its current
  path offers a stable physical shot before either allowance expires.
- Medium-term planning: preserve the remaining local attempts after a miss
  while reading the cumulative hit lamps against the six-hit boundary.
- Long-term structure: convert ten independent short opportunities into one
  binary qualification result while score provides a stricter optional motive.
- Common heuristics: lead rather than chase erratic flight, use the full
  physical aiming posture, do not waste the third shot, and distinguish the
  six-hit pass requirement from a perfect round.
- Failure attribution: each non-hit trigger visibly reduces the local shot
  allowance; timeout and third-miss escape are distinct; the final lamp row
  makes quota failure attributable.
- Player-trust factors: every trigger must debit once, one credited hit must
  end only its current opportunity, the lamp order must match all ten targets,
  and the final PASS LINE check must not depend on score value.
- Claims: `DH-003`–`DH-010`.

## Replay and variation

- Target rise location, colour and flight vary; the ten-opportunity schedule,
  three-shot cap and round-one quota remain fixed.
- Better aim can change miss count, score and PERFECT eligibility without
  changing the target count.
- The packet admits no second-player intervention, later speed table or
  increased PASS LINE, so those sources of variation remain separate modules.
- Typical replay motives are qualification consistency, higher colour-weighted
  score and a no-miss round.
- Claims: `DH-002`, `DH-005`–`DH-009`.

## Adjacent systems and history

- Peggle Deluxe and Angry Birds Classic also spend finite launched bodies, but
  their projectile stock spans a larger attempt and each launch enters a
  physics simulation. Duck Hunt instead gives three sensor-trigger requests to
  each separately expiring moving target.
- Rhythm and timing games accept inputs in disclosed temporal zones. Duck Hunt
  requires physical spatial aim at an autonomous target; timing matters only
  because that target moves and escapes.
- PAC-MAN also rebuilds progress into later rounds and tracks score, but its
  first maze is exhaustive collection under pursuit. This packet permits four
  missed targets and settles success by a minimum hit count.
- Wii U Virtual Console uses a Wii Remote pointer and visible optional aiming
  cursor. It is a later adaptation and cannot establish parity for the
  original NES Zapper input boundary.
- Claims: `DH-001`–`DH-011`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-490` | Zapper, CRT distance and aim direction are parameters |
| System Behaviour | `SYS-045`, `SYS-967`, `SYS-968`, `SYS-969` | duck class, flight, sensor response and score values are parameters |
| Constraint | `CON-658` | three shots and flight duration are parameters |
| Information | `INF-366` | lamp art, PASS LINE position and HUD layout are presentation/parameters |
| Objective | `OBJ-002`, `OBJ-202` | score values, ten targets and six-hit threshold are parameters |
| Time | `TIM-003` | live flight cadence and pause rule are parameters |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `344` (`GAME-0001`–`GAME-0344`).
- Exact genome matches: none.
- Tied near matches: `GAME-0114` — Peggle Deluxe (`2 / 15 = 0.133333`).
- Supported combination subsets: none.
- Scan date: 2026-09-21.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0114` — Peggle Deluxe | `OBJ-002`, `TIM-003` | Both accept aim-related input while live state advances and offer score maximisation. Peggle commits a finite launched ball into continuous collision physics, clears every orange target and may recover a ball through the bucket. Duck Hunt instead samples physical display light, resets a three-shot timed opportunity for each autonomous duck and advances after a minimum six-of-ten hit count. | Near, `2 / 15 = 0.133333` |

### Preserved research notes

- New genes: `ACT-490`, `SYS-967`, `SYS-968`, `SYS-969`, `CON-658`, `INF-366`
  and `OBJ-202`.
- Classification result: `New genes`.
- Evidence and reasoning: continuous motion, score maximisation and live time
  transfer from independent lower-ID carriers. The light-sampled action and
  adjudication, expiring per-target schedule, joined hunting HUD and fixed
  minimum-hit round terminal do not match any lower-ID boundary.

## Taxonomy impact

- Registry changes: append seven independently evidenced Active boundaries;
  add Duck Hunt as supporting evidence to `SYS-045`, `OBJ-002` and `TIM-003`.
- Taxonomy-change record:
  [`TAXONOMY_CHANGE_087`](../../../research/taxonomy-changes/TAXONOMY_CHANGE_087.md).
- Candidate terms affected: Zapper, CRT, duck colour, hound, PASS LINE and
  three-shot value remain parameters of the admitted boundaries.

## Negative results

- No direct physical play, ROM execution, disassembly verification, frame
  capture, photodiode trace, exact hitbox or timing measurement.
- The official original-hardware sources establish display-sensitive shot
  registration, but exact black-frame and per-target-light implementation is
  admitted only through reproducible technical corroboration and is not given
  undocumented constants.
- No ordinary combat, enemy damage, health, ammunition reload or projectile
  trajectory enters the signature. `ACT-161`, `SYS-215`, `CON-164` and
  `CON-578` are rejected.
- Game B, Game C, two-player duck control, later rounds, Virtual Console and
  arcade variants are explicit exclusions rather than inferred parity.

## Delta summary

## New facts

- [Confirmed | Direct | High] One Game A round schedules ten one-at-a-time
  ducks; each accepts at most three shots before hit, exhaustion or timeout
  settlement (`DH-002`, `DH-005`, `DH-006`).
- [Observation | Corroborated | High] Six first-round hits qualify, colour
  classes change score, and ten hits also earn the PERFECT bonus (`DH-007`,
  `DH-008`).

## New genes

- [Observation | Direct/Corroborated | High] Seven genes isolate physical
  display-sensor input, its hit resolution, the target schedule and score,
  target-local dual limit, joined HUD and minimum-hit round terminal.

## New combinations

- [Observation | Corroborated | High] No verified combination is expected;
  deterministic subset validation remains required.

## Taxonomy changes

- [Observation | Direct/Corroborated | High] Seven Active boundaries are
  appended without changing earlier signatures or lifecycle states.

### Added

- `GAME-0345` as one original-NES Game A first-round packet.
- `ACT-490`, `SYS-967`–`SYS-969`, `CON-658`, `INF-366` and `OBJ-202`.

### Reused

- `SYS-045`, `OBJ-002` and `TIM-003`.

### Generalised

- No existing definition is broadened.

### Rejected

- Separate genes for the hound, sky colour, CRT distance, duck colours,
  controller socket, menu selection, software reticle, later-round quota,
  second-player steering and each score constant.

### Preserved

- Every lower-ID signature, lifecycle state, verified combination and family
  definition.
