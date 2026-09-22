---
game_id: GAME-0358
slug: psychonauts
game_title: Psychonauts
analysis_status: reviewed
reviewed: 2026-09-22
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-161
    - ACT-341
  system:
    - SYS-036
    - SYS-037
    - SYS-578
    - SYS-736
    - SYS-984
    - SYS-985
    - SYS-986
  constraint:
    - CON-282
    - CON-661
  information:
    - INF-115
    - INF-119
    - INF-268
  objective:
    - OBJ-208
  time:
    - TIM-003
---

# Game: Psychonauts

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Raz, Coach
Oleander, `Basic Braining`, figments, emotional baggage, PSI Cadet Rank and
Sasha Nein's button are carrier parameters, not gene names.

## Analysis scope

- Version / ruleset: original North American English Xbox retail release,
  Majesco UPC `096427013983`, Xbox title ID `0x4D4A0012`, fresh New adventure
  with default controls. It is not a prototype, the PlayStation 2 or Windows
  edition, a later Steam build, macOS/Linux port, PlayStation 4 release, Xbox
  backward-compatibility wrapper, modification, cheat or completed save.
- Structured analysis target: first ordinary control at the Kid's Cabins after
  opening profile setup through completion of Coach Oleander's `Basic
  Braining`, return to ordinary camp control and receipt of Sasha Nein's
  advanced-training button. Stop before entering the Main Campgrounds or
  beginning the next training.
- Entry: Raz has a fresh profile, ordinary camp movement, the default PSI Punch
  and physical jump/double-jump, no later merit badge and no imported rank,
  collectible, shop item or completed-mind state.
- Fixed reproducible route: reach Coach Oleander and accept training; enter his
  mind; follow the three authored course parts; use movement, jump/double-jump
  and PSI Punch through the opening projection, walls, poles, nets, trapezes,
  rails and log course; clear the mandatory target gallery by hitting enemy
  cut-outs and avoiding baby cut-outs; cross the machine-gun section by moving
  between cover; enter the closing white corridor and curtain sequence; accept
  the course settlement and return to the Kid's Cabins; retain Sasha Nein's
  button and stop at first ordinary control.
- Bounded collectible controls: on the accepted route, contact enough visible
  figments to cross one 100-point threshold and observe one retained PSI Cadet
  Rank increase; collect the steamer-trunk tag and reunite it with the matching
  steamer trunk. Exact incidental figment path and remainder may vary. These
  controls do not require every figment, bag, vault or cobweb.
- Bounded failure controls: in duplicated course state, deplete mental health
  once while an astral layer remains and verify return to the latest crossed
  checkpoint with one fewer layer; in a separate duplicate with no layer,
  deplete mental health and verify ejection to the real world. Neither failure
  branch substitutes for the accepted completion route.
- Primary decision loop: read the current tutorial cue, local platform and
  target class; steer, jump/double-jump, climb or swing through the immediate
  geometry; punch the required projection, enemy cut-out or breakable barrier;
  collect or deliberately bypass figments; preserve mental health and astral
  layers; satisfy the current authored predicate so the next lesson appears.
- Positive terminal: `Basic Braining` has settled, ordinary real-world control
  is restored at the Kid's Cabins and Sasha Nein's button is retained for the
  successor advanced training. Clearing only the gallery, reaching the white
  corridor or viewing the closing scene without returned control is not the
  terminal.
- Negative terminals: mental-health depletion with an astral layer returns to
  the last mental checkpoint and is recoverable; depletion with no layer ejects
  Raz to the real world and leaves this completion attempt unfinished.
- Included: direct third-person movement and camera-relative navigation;
  jump/double-jump and authored acrobatic surfaces; PSI Punch against the
  required projection, cut-outs and breakables; real-time physics and hazards;
  mental health; astral-layer recovery/ejection; contact-collected figments;
  one 100-point PSI-rank threshold; one exact baggage-tag reunion; staged
  tutorial guidance; target-class gallery scoring; authored course order;
  local view/sound; HUD health, layers, figments and rank; course completion
  and successor invitation.
- Excluded: Telekinesis, Levitation, PSI Blast, Pyrokinesis, Clairvoyance,
  Confusion, Invisibility and Shield; later merit badges; the Main Lodge and
  store; Cobweb Duster and clearing mental cobwebs; vault completion; every
  other mind; scavenger hunt, PSI Cards/Cores/Challenge Markers, arrowhead
  economy, full rank progression, optional target-gallery replay, complete
  camp/campaign, speedrun routes, glitches and every later release.
- Direct-play status: not conducted. No disc, image, Xbox console, emulator,
  controller trace, profile, save, screenshot, video or audio was obtained or
  inspected. The official Xbox manual establishes controls, HUD, health,
  layers, figments, rank and baggage; two independent written original-Xbox
  routes corroborate the bounded course order. This is a source-bounded
  reconstruction, not a claimed playthrough.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `PSY-001` | The packet targets the original North American English Xbox retail product identified by UPC `096427013983` and title ID `0x4D4A0012` | Confirmed | Corroborated | High | P1, R1, R2 |
| `PSY-002` | Default Xbox control supplies direct movement, camera, jump/double-jump, contextual interaction and PSI Punch | Confirmed | Direct | High | P1 |
| `PSY-003` | The HUD exposes mental health, astral layers, figments and PSI Cadet Rank | Confirmed | Direct | High | P1 |
| `PSY-004` | Figments carry point values and each 100 points awards one PSI Cadet Rank | Confirmed | Direct | High | P1 |
| `PSY-005` | Each emotional-baggage body accepts its corresponding luggage-tag type | Confirmed | Direct | High | P1; corroborated by S1 |
| `PSY-006` | Mental-health depletion spends one available astral layer and returns Raz to the latest checkpoint; no remaining layer ejects him to the real world | Confirmed | Direct | High | P1 |
| `PSY-007` | `Basic Braining` proceeds through three authored parts from the opening projection to its closing white corridor and curtain sequence | Observation | Corroborated | High | S1, S2 |
| `PSY-008` | The mandatory gallery rewards enemy-target hits, penalises or rejects baby-target hits and gates onward progress on the required live result | Observation | Corroborated | High | S1, S2 |
| `PSY-009` | The later course requires cover against machine-gun fire and successive pole, trapeze, rail and log traversal | Observation | Corroborated | High | S1, S2 |
| `PSY-010` | Completion returns Raz to the Kid's Cabins and retains Sasha Nein's button for advanced training | Observation | Corroborated | High | S2 |
| `PSY-011` | Telekinesis, Levitation and the other later merit-badge powers are not required or granted within this bounded course | Confirmed | Corroborated | High | P1, S1, S2 |
| `PSY-012` | The local verifier reconstructs course order, figment rank, baggage matching, gallery gate and layer-dependent failure without executing Psychonauts | Observation | Direct | High | V1 |

## Basic data

- Release / origin: Double Fine Productions developed the original game;
  Majesco published the North American Xbox retail release in April 2005.
- Platform or physical form: licensed North American English Xbox disc product,
  UPC `096427013983`, title ID `0x4D4A0012`; no disc image or executable was
  obtained, executed or hashed.
- Puzzle family: physics and object manipulation; real-time system pressure;
  ordered dependency sequencing.
- Primary sources, accessed 2026-09-22:
  - **[P1]** [Double Fine's official English Xbox
    manual](https://assets.doublefine.com/manuals/Psychonauts_Manual-Xbox.pdf),
    pp. 2–7 and 12–19, for controls, HUD, real/mental worlds, mental health,
    astral layers, checkpoints, figments, PSI Cadet Rank, emotional baggage and
    later-item/power exclusions. Preserved local SHA-256:
    `0da6bb5efd8c865e6a8d78def8c451eac406457c263b3bb4436535f684c3b470`.
  - **[P2]** [Double Fine's official Psychonauts support and manual
    page](https://www.doublefine.com/games/support/psychonauts/manual?platform=all),
    for the studio-hosted original manual identity.
  - **[P3]** [official Xbox product
    page](https://www.xbox.com/en-us/games/store/Psychonauts/C5HHPG1TXDNG),
    used for licensed product, developer and publisher identity only, not as a
    claim that the current compatibility wrapper is mechanically identical.
- Reproducible identity sources:
  - **[R1]** [GameFAQs original-Xbox release-data
    record](https://gamefaqs.gamespot.com/xbox/561517-psychonauts/data), for the
    North American Majesco release and UPC `096427013983`.
  - **[R2]** [Xbox title-ID index](https://mobcat.zip/XboxIDs/), for title ID
    `0x4D4A0012`; this identifier freezes the carrier but does not imply that an
    executable was downloaded or checked.
- Corroborating written sources, accessed 2026-09-22:
  - **[S1]** [GameFAQs original-Xbox written
    walkthrough](https://gamefaqs.gamespot.com/xbox/561517-psychonauts/faqs/38117),
    sections `Kid's Cabins` and `Basic Braining`, for Coach entry, three course
    parts, figments, baggage, target gallery, machine gun, acrobatics and the
    white-corridor closeout.
  - **[S2]** [GameSpot written
    walkthrough](https://www.gamespot.com/articles/psychonauts-walkthrough/1100-6122996/),
    for the independently matching Coach entry, gallery target classes,
    cover/trapeze/rail/log sequence, course completion and Sasha invitation.
- Validation source: **[V1]**
  [`verify_psychonauts_control.py`](../../../scripts/verify_psychonauts_control.py),
  an executable state reconstruction of the cited bounded relations. It does
  not execute Psychonauts.
- Claim IDs: `PSY-001`–`PSY-012`.

## Mechanical decomposition

### Action Genes

- Existing `ACT-008`: directly steer Raz, jump/double-jump and traverse the
  course's floors, poles, nets, trapezes, rails and log route.
- Existing `ACT-161`: aim or face and commit PSI Punch against a required
  projection, enemy cut-out or eligible breakable barrier.
- Existing `ACT-341`: accept Coach's training, address course fixtures and
  reunite one credited matching tag with its emotional-baggage body.
- Exact Xbox bindings, jump arc, camera values and PSI Punch reach are
  parameters. Claims: `PSY-002`, `PSY-005`, `PSY-007`–`PSY-009`.

### System Behaviour Genes

- Existing `SYS-036`: gravity, velocity, support, moving surfaces and collision
  continuously resolve Raz against the authored course geometry.
- Existing `SYS-037`: contact consumes or credits figments and luggage tags
  without ending the course attempt.
- Existing `SYS-578`: hazards reduce one continuous mental-health pool; health
  pickups may restore missing value, while zero hands resolution to the astral
  recovery rule instead of directly granting success.
- Existing `SYS-736`: each lesson remains current until its taught action or
  state predicate settles, then exposes the next instruction/gate.
- New `SYS-984`: figment point values accumulate; every completed hundred
  becomes one retained PSI Cadet Rank and leaves the documented remainder.
- New `SYS-985`: zero mental health spends one remaining astral layer and
  returns to the latest checkpoint, but with no layer ejects Raz from the mind.
- New `SYS-986`: the gallery classifies struck enemy and baby cut-outs, updates
  the live result and opens the successor only after the required pass quota.
- Claims: `PSY-003`, `PSY-004`, `PSY-006`–`PSY-009`.

### Constraint Genes

- Existing `CON-282`: Coach entry, course parts, gallery pass, machine-gun
  cover, later acrobatics and the closing corridor must settle in authored
  order; optional pickups cannot skip a required gate.
- New `CON-661`: the steamer-trunk tag resolves only with the steamer trunk;
  another tag/bag identity remains unmatched.
- The exact gallery quota, target cadence, checkpoint positions, figment
  values and tag locations are carrier parameters rather than new boundaries.
- Claims: `PSY-005`, `PSY-007`–`PSY-010`.

### Information Genes

- Existing `INF-115`: the local third-person view, animation and sound expose
  nearby platforms, hazards, moving course elements and currently presented
  targets without revealing the entire future course.
- Existing `INF-119`: the HUD exposes mental health, astral layers, current
  figment progress and PSI Cadet Rank before the next risk or threshold.
- Existing `INF-268`: Coach's staged instruction identifies the current taught
  action, target class or route gate and acknowledges completion before the
  next lesson.
- Claims: `PSY-003`, `PSY-007`–`PSY-009`.

### Objective Genes

- New `OBJ-208`: enter and complete the named mental course, satisfy its
  physical/combat/qualification gates, return to real-world control and retain
  Sasha Nein's successor invitation.
- A rank increase and baggage reunion are bounded controls, not terminal
  requirements. Every figment, bag, vault or cobweb is explicitly unnecessary.
- Claims: `PSY-007`–`PSY-011`.

### Time Genes

- Existing `TIM-003`: Raz, moving surfaces, target cadence, machine-gun fire,
  hazards, health and player input resolve on one live clock outside pause and
  authored transitions. Claims: `PSY-006`, `PSY-008`, `PSY-009`.

## Reproducible transitions

| Before | Action | Deterministic or bounded resolution | Establishes | Claim |
|---|---|---|---|---|
| Fresh Kid's Cabins control | reach Coach and accept `Basic Braining` | Raz enters Coach's mind and the first lesson becomes current | exact packet entry into the course | `PSY-007` |
| One figment is on the movement line | contact it | the figment is credited and its value is added without stopping live traversal | contact collection | `PSY-004` |
| The retained figment counter is below 100 by the contacted value | collect that figment | one hundred points are converted into one PSI Cadet Rank and the remainder persists | collectible-threshold progression | `PSY-004` |
| The steamer-trunk tag is credited | interact with the steamer trunk | the exact typed pair settles; a different baggage body would reject the tag | one-to-one baggage identity | `PSY-005` |
| The gallery lesson is active | punch an enemy cut-out, then avoid a baby cut-out | the approved hit advances the live result while the protected class is not valid progress | target-class scoring | `PSY-008` |
| The required gallery result is reached before its live interval closes | finish the current target sequence | Coach opens the next course continuation | score is an authored route gate | `PSY-008` |
| Machine-gun fire crosses an exposed lane | move between authored cover positions | safe timing preserves mental health; exposed contact applies damage | real-time hazard routing | `PSY-009` |
| Mental health reaches zero with one astral layer | accept failure resolution | one layer is consumed and Raz returns to the latest mental checkpoint | finite within-mind recovery | `PSY-006` |
| Mental health reaches zero with no astral layer | accept failure resolution | the course attempt closes and Raz returns to the real world | distinct ejection fallback | `PSY-006` |
| The final log/rail route reaches the white corridor and curtain | cross the closing sequence | `Basic Braining` settles; ordinary Kid's Cabins control returns with Sasha's button | exact positive terminal | `PSY-010` |

## Edge-case audit

- Double-jump is an input parameter of direct navigation, not a retained
  Levitation power. The manual explicitly separates later PSI Float from the
  starting jump/double-jump controls.
- The course visually contains mental cobwebs, but the fresh profile lacks the
  later Cobweb Duster. They are excluded obstacles/collectibles rather than
  falsely credited progress.
- Optional Dogen assistance and arrowhead collection do not gate the named
  terminal and therefore do not enter the signature.
- The gallery is not Duck Hunt's fixed ten-opportunity light-gun round. It is a
  live course gate with friendly/hostile class distinction, so `SYS-968`,
  `SYS-969`, `CON-658`, `INF-366` and `OBJ-202` are rejected.
- An astral layer is not a generic platform-game life: its debit returns within
  the current mind, while exhaustion redirects to a different real-world
  state. `SYS-911` and `SYS-933` therefore do not replace `SYS-985`.
- The 100-point conversion is persistent cadet rank, not an extra life or
  ordinary combat-experience level. `SYS-935`, `SYS-965` and `SYS-299` remain
  separate.

## Strategic and experiential structure

- Local decision: read the immediate cue and geometry, then choose jump line,
  punch target, cover timing or collectible detour.
- Medium horizon: preserve health/layers while satisfying successive lessons,
  and decide whether a visible figment or matching baggage detour is safe
  before the next gate.
- Long horizon: complete a curriculum that alternates embodied traversal,
  target classification and authored spectacle, then return to camp with the
  next instructor's invitation rather than merely reaching a level exit.
- Failure attribution: the HUD distinguishes ordinary damage, zero health,
  remaining checkpoint recovery and forced ejection; tutorial feedback
  distinguishes wrong target class from insufficient gallery result.
- Player trust: equivalent figment values, baggage identities, checkpoint
  crossings, layer debits and lesson predicates must always settle the same.

## Replay and variation

- Course geometry, lesson order, checkpoint sequence, baggage identities,
  closing corridor and Sasha invitation are authored and fixed.
- Exact movement line, missed jumps, damage, figment subset, remainder, gallery
  timing and optional baggage detour may vary.
- No procedural room generation, random loot or later psychic-power selection
  is admitted. Typical replay motives are cleaner traversal, more collectibles
  or higher optional gallery performance.

## Adjacent systems and history

- `GAME-0344` Prince of Persia: The Sands of Time is the selected near
  neighbour because both packets combine direct 3D traversal, contextual
  interaction/attack, one health pool, ordered authored gates, local danger,
  personal HUD state, staged teaching and shared real time. Prince retains a
  unique rewind artefact; Psychonauts instead combines contact collectibles,
  persistent figment rank, exact baggage matching, class-sensitive training
  score and finite astral-projection recovery.
- `GAME-0327` Fable also exposes tutorial instructions, health and a growing
  character while moving through authored early training, but its packet
  centres melee/ranged/magic hero development and choice rather than entering a
  mental course with layer-dependent ejection.
- Later Psychonauts minds and powers are potential modules, not evidence that
  the fresh `Basic Braining` packet already contains them.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-161`, `ACT-341` | Raz, bindings, jump arc, PSI Punch and Coach interaction are parameters |
| System Behaviour | `SYS-036`, `SYS-037`, `SYS-578`, `SYS-736`, `SYS-984`, `SYS-985`, `SYS-986` | platform motion, figment values, health, lesson predicates, rank threshold, layers and gallery quota are parameters |
| Constraint | `CON-282`, `CON-661` | course order and tag/bag types are parameters |
| Information | `INF-115`, `INF-119`, `INF-268` | camera, HUD art, exact prompts and sound are presentation parameters |
| Objective | `OBJ-208` | Coach's mind, Kid's Cabins and Sasha's button are parameters |
| Time | `TIM-003` | hazard and target cadence are parameters |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `357` (`GAME-0001`–`GAME-0357`).
- Exact genome matches: none.
- Tied near matches: `GAME-0344` — Prince of Persia: The Sands of Time (`9 / 25 = 0.360000`).
- Supported combination subsets: none.
- Scan date: 2026-09-22.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0344` — Prince of Persia: The Sands of Time | `ACT-008`, `ACT-161`, `ACT-341`, `SYS-578`, `CON-282`, `INF-115`, `INF-119`, `INF-268`, `TIM-003` | Both use direct 3D traversal/strikes, contextual fixtures, continuous health, local danger, ordered authored gates and staged teaching. Prince adds held guard, breakables, water recovery and a finite retained rewind artefact; Psychonauts adds continuous platform physics, contact collectibles, figment-rank conversion, classed target scoring, exact baggage pairing and astral-layer checkpoint/ejection logic. | Near, `9 / 25 = 0.360000` |

### Preserved research notes

- New genes: `SYS-984`, `SYS-985`, `SYS-986`, `CON-661`, `OBJ-208`.
- Classification result: five new boundaries plus reused movement, interaction,
  physics, collection, health, tutorial, course-order, information and time
  boundaries.
- Evidence and reasoning: complete lower-ID transfer tests reject life,
  experience, Duck Hunt round, generic checkpoint and route-endpoint matches
  where their causal terminal or fallback differs.

## Taxonomy impact

- Registry changes: add `SYS-984`, `SYS-985`, `SYS-986`, `CON-661` and
  `OBJ-208` under
  [`TAXONOMY_CHANGE_097`](../../../research/taxonomy-changes/TAXONOMY_CHANGE_097.md).
- Lifecycle changes: none. Earlier signatures remain unchanged.

## Delta summary

## New facts

- [Confirmed | Direct | High] The official Xbox manual separates figment
  values, 100-point PSI Cadet Rank conversion, typed emotional baggage and
  astral-layer checkpoint recovery from ordinary movement and health
  (`PSY-002`–`PSY-006`).
- [Observation | Corroborated | High] The three-part Basic Braining route joins
  class-sensitive target qualification, live cover and acrobatics to a
  returned-control terminal with Sasha Nein's invitation retained
  (`PSY-007`–`PSY-010`).

## New genes

- [Observation | Corroborated | High] Add `SYS-984`, `SYS-985`, `SYS-986`,
  `CON-661` and `OBJ-208` under `TAXONOMY_CHANGE_097`.

## New combinations

- [Observation | Direct | High] No verified combination is registered from one
  new carrier.

## Taxonomy changes

- [Observation | Corroborated | High] `TAXONOMY_CHANGE_097` adds five separate
  boundaries and preserves every earlier signature and lifecycle state.

## Negative results

- `SYS-299`, `SYS-935` and `SYS-965` are rejected for figments: their outputs
  are experience levels or lives, while this threshold creates PSI Cadet Rank.
- `SYS-369`, `SYS-610`, `SYS-911` and `SYS-933` are rejected as complete
  failure models: none couples a finite mental projection layer to checkpoint
  return and a distinct no-layer real-world ejection.
- `SYS-968`, `SYS-969`, `CON-658`, `INF-366` and `OBJ-202` are rejected for the
  gallery because their original boundary is a fixed hunting round with
  per-target shots and pass-line settlement, not an in-course enemy/friendly
  classification gate.
- `CON-028` is rejected for baggage: it validates paired path endpoints, not a
  separately collected typed tag reunited with one world body.
- Telekinesis, Levitation and all later merit-badge powers are rejected because
  the scoped fresh course neither grants nor requires them.

## Open questions

- Exact internal gallery target schedule, score values, pass threshold, timing,
  checkpoint coordinates, damage amounts, figment remainder and movement
  constants remain parameters because no executable or direct trace was
  inspected.
- A later bounded module could analyse Sasha's advanced training, the camp
  economy or one subsequent mind, but no later mechanic is inferred here.

## Reproducibility notes

- Start from the original English North American Xbox retail ruleset and a
  fresh New adventure; record UPC/title ID before applying route claims.
- Keep the accepted completion, astral-layer return and zero-layer ejection as
  separate attempts so a failure branch cannot masquerade as course success.
- Cross exactly one 100-point figment boundary and one matching baggage pair;
  record the point remainder and pair type rather than assuming full
  collectible completion.
- Stop at the first returned Kid's Cabins control with Sasha's button. Do not
  enter Main Campgrounds or begin advanced training.
- Treat the verifier as a transition proof over cited rules, not an emulator,
  timing measurement or proof of original binary execution.

## Localisation review

- Ukrainian profile, scope, direct-play statement, presentation, five new gene
  definitions and all plain-language cards are reviewed in this unit under
  [`UKRAINIAN_LOCALISATION_POLICY`](../../../docs/UKRAINIAN_LOCALISATION_POLICY.md).
- `verified`: Psychonauts, Xbox, Majesco, Double Fine Productions, Raz, Coach
  Oleander, `Basic Braining`, PSI Punch, PSI Cadet Rank, Kid's Cabins, Sasha
  Nein, Main Campgrounds, Telekinesis, Levitation and the stable IDs remain
  official names, literal labels or evidence-critical identifiers.
- `corrected`: all explanatory Ukrainian prose is authored naturally and keeps
  actions, prerequisites, results, failure branches and exclusions intact.
- `retained-with-reason`: remaining Latin-script terms are only the official
  product, course, character, power, place, platform and identifier labels
  above; no generic English prose is deferred to a later batch.
