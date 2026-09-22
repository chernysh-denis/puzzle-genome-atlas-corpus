---
game_id: GAME-0356
slug: shadow-of-the-colossus
game_title: Shadow of the Colossus
analysis_status: reviewed
reviewed: 2026-09-22
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-161
    - ACT-271
    - ACT-348
    - ACT-362
    - ACT-495
  system:
    - SYS-215
    - SYS-578
    - SYS-661
    - SYS-983
  constraint:
    - CON-269
    - CON-402
    - CON-534
  information:
    - INF-075
    - INF-125
    - INF-258
    - INF-318
    - INF-369
    - INF-370
  objective:
    - OBJ-206
  time:
    - TIM-003
---

# Game: Shadow of the Colossus

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Wander, Agro, the
Shrine of Worship, Dormin, Ancient Sword, the first colossus and its body
regions are carrier parameters, not gene names.

## Analysis scope

- Version / ruleset: original North American English PlayStation 2 retail
  release, serial `SCUS-97472`, on the fresh-game Normal ruleset. It is not the
  Japanese or PAL release, later Greatest Hits evidence, the PlayStation 3 HD
  collection, the 2018 PlayStation 4 remake, Time Attack, Hard mode, a cheat,
  modification or later game.
- Structured analysis target: one fresh game from first ordinary control in
  the Shrine of Worship after the opening sequence through the first ordinary
  control restored there after defeating the first colossus; see `GAME-0356`
  in [`knowledge/platforms/games.json`](../../platforms/games.json).
- Entry: Wander has the Ancient Sword and bow, Agro is available outside, the
  first colossus is the current target, health and grip are at their fresh
  values, no colossus is defeated and no Time Attack item or carried-over stat
  exists.
- Fixed reproducible route: leave the altar; call and mount Agro; reach direct
  sunlight and focus the Ancient Sword until its rays converge southward; ride
  to the cliff approach; dismount and climb the authored ledges into the first
  arena; evade the colossus; grab the fur on the rear of its own left leg;
  charge and stab the small marked wound until the colossus kneels; climb from
  the leg across its moving back, using stone ledges as rest points when grip
  needs to recover; reach the crown; equip the sword, read the major sigil,
  hold grip and charge/release stabs until the encounter health reaches zero;
  accept the black-tendril transition and automatic return to the Shrine; stop
  at the first restored ordinary control before starting the second hunt.
- Primary decision loop: read world light, sword rays, local body geometry,
  health and grip; move on foot or call, mount and steer Agro; approach the
  current guardian; alternate stable rest surfaces with stamina-priced grip;
  react to the guardian's motion and attacks; find a marked body region and
  commit a direct sword strike whose result changes topology or health.
- Positive terminal: the first colossus's required Normal-mode crown sigil has
  been depleted, the automatic return has settled and ordinary Wander control
  is available again in the Shrine. The next Dormin instruction and any step
  toward the second colossus are outside the packet.
- Failure paths: Wander's health reaching zero ends the attempt. Exhausting
  grip while attached removes continued hold and can produce a fall, but a
  fall is terminal only if resulting damage exhausts health. Restart, Continue
  and save loading are not exercised and add no genes.
- Included: direct movement and jumping; calling, mounting, steering and
  dismounting Agro; sunlight-gated sword focus and temporary bearing; local
  map/journey support; one continuous health pool; visible health and grip;
  stamina-bounded attachment, climbing and rest; live guardian attacks;
  moving-body climb topology; the leg-wound kneel; crown-sigil damage;
  guardian health and automatic shrine return.
- Reproducible parameterisation: exact movement line, Agro's approach path,
  incidental damage, grip remaining, guardian attack timing, number and charge
  of accepted stabs and number of rests may vary. The southward target,
  rear-left-leg trigger, crown major sigil, Normal-mode required target set,
  zero-health victory and automatic Shrine return do not.
- Excluded: bow use, lizards, fruit, save shrines, optional exploration,
  swimming, health or grip growth, other colossi, Hard-mode additional sigils,
  Time Attack, New Game+, complete story, score and completion-time goals,
  exploits, speedrun jumps, out-of-bounds movement, later releases and remake
  controls or additions.
- Direct-play status: not conducted. No disc, image, console, emulator,
  controller trace, save, screenshot, video or audio was obtained or inspected.
  The original manual, release record and independent written routes support a
  bounded rules reconstruction rather than a claimed playthrough.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `SOC-001` | The packet targets original North American English PS2 retail serial `SCUS-97472` on a fresh Normal game | Confirmed | Corroborated | High | P1, P2, R1 |
| `SOC-002` | Holding the sword's light command in sufficient sunlight and aiming until the rays converge exposes a bearing toward the current colossus | Confirmed | Direct | High | P1 |
| `SOC-003` | Wander can call, mount, steer and dismount Agro while retaining direct route control | Confirmed | Direct | High | P1 |
| `SOC-004` | Holding grip on compatible fur or ledges enables aimed climbing while usable grip drains, and stable rest permits recovery | Confirmed | Corroborated | High | P1, S1, S2 |
| `SOC-005` | The first colossus's movement and shaking continuously alter reachable and stable climbing relations | Observation | Corroborated | High | S1, S2 |
| `SOC-006` | Stabbing the marked rear-left-leg wound makes the first colossus kneel and opens the intended upward body route | Observation | Corroborated | High | S1, S2 |
| `SOC-007` | On Normal, the required major health-bearing sigil is on the crown; Hard-only additional targets are excluded | Observation | Corroborated | High | S1, S2 |
| `SOC-008` | Accepted charged sword stabs at that sigil reduce the visible encounter health until victory | Observation | Corroborated | High | P1, S1, S2 |
| `SOC-009` | Wander's visible health reaches a terminal state at zero while grip exhaustion interrupts attachment rather than directly declaring defeat | Confirmed | Corroborated | High | P1, S1 |
| `SOC-010` | First-colossus victory triggers a non-voluntary transition back to the Shrine and later restores ordinary control there | Observation | Corroborated | High | S1, S2 |
| `SOC-011` | Bow use, optional upgrades, saving, later guardians and post-game modes are not causally required by this route | Observation | Direct | High | P1, S1, S2 |

## Basic data

- Release / origin: Sony Computer Entertainment / Team Ico, original 2005
  PlayStation 2 action-adventure. The current official PlayStation page is a
  remake page and is used only for the publisher's stable high-level identity:
  sword, bow, world search and distinct giant challenges, not as evidence of
  original control or content parity.
- Platform or physical form: original licensed North American English
  PlayStation 2 DVD retail ruleset, serial `SCUS-97472`; no disc image or
  executable was acquired or executed.
- Puzzle family: world topology and perspective; spatial ordering and
  dependencies; real-time system pressure.
- Primary sources, accessed 2026-09-22:
  - **[P1]** [original North American English PlayStation 2 instruction
    booklet](https://www.videogamemanual.com/PS2/Shadow%20of%20the%20Colossus%20%28USA%29.pdf),
    pp. 7, 10, 13, 15–16, 19, 21–22, for health, grip and equipped-weapon
    display; crouch, grip, climb, jump, mount, steering, sword light, sword
    attack, bow and map rules. Local PDF SHA-256:
    `53bcca8f319c9b642f28340f2a24b0fcc66da0cec67dcca45d9a862d5b032fcf`.
  - **[P2]** [PlayStation's PS2 history](https://www.playstation.com/es-es/playstation-history/2000-ps2-psp/),
    for the 2005 original product and its puzzle-like colossus battles.
- Reproducible sources:
  - **[R1]** [PSX Data Center's `SCUS-97472` release
    record](https://psxdatacenter.com/psx2/games2/SCUS-97472.html), for the
    North American serial, English language, 18 October 2005 release and DVD-5
    identity; its emulator notes and cheats are not evidence for the packet.
  - **[S1]** [StrategyWiki's first-colossus
    route](https://strategywiki.org/wiki/Shadow_of_the_Colossus/Valus_-_Colossus_1),
    for the southward approach, rear-left-leg trigger, kneel, body climb and
    head weak point.
  - **[S2]** [Crazyreyn's original-PS2 written
    guide](https://gamefaqs.gamespot.com/ps2/924364-shadow-of-the-colossus/faqs/43630),
    for the Shrine departure, first route, grip-rest cadence, leg wound, crown
    sigil, health depletion and black-tendril return sequence.
- Validation source: **[V1]**
  [`verify_shadow_of_the_colossus_control.py`](../../../scripts/verify_shadow_of_the_colossus_control.py),
  an executable source-model reconstruction of the bounded state relations. It
  does not run Shadow of the Colossus.
- Claim IDs: `SOC-001`–`SOC-011`.

## Mechanical decomposition

### Action Genes

- `ACT-008`: directly move and jump across the Shrine, field, cliff route and
  guardian body; camera and animation are parameters.
- `ACT-161`: equip the sword, hold its attack preparation while gripping and
  commit a direct stab against the leg wound or crown sigil.
- `ACT-271`: call the persistent owned horse toward Wander when it is outside
  immediate mounting reach.
- `ACT-348`: mount, directly steer and dismount Agro on the field route.
- Generalised `ACT-362`: hold and aim one grip on compatible static rock,
  guardian fur or ledge, and deliberately release when changing support.
- New `ACT-495`: hold and aim the Ancient Sword in direct sunlight until its
  rays converge and request the current target bearing.
- Claims: `SOC-002`–`SOC-004`, `SOC-006`, `SOC-008`.

### System Behaviour Genes

- `SYS-215`: guardian motion, attacks, Wander movement, grip and sword strikes
  resolve concurrently in real time.
- `SYS-578`: attacks and falls reduce one continuous health pool and zero is
  terminal; optional health growth and fruit are excluded.
- Generalised `SYS-661`: reachable contact, moving or static surface geometry,
  gravity and usable grip resolve attachment, climbing, rest or fall.
- New `SYS-983`: guardian posture and movement form a changing traversal graph;
  the rear-left-leg wound produces a kneel that connects the intended route to
  the back and crown, while later shaking changes stability without becoming a
  separate terrain object.
- Claims: `SOC-004`–`SOC-009`.

### Constraint Genes

- `CON-269`: sword bearing requires the sword, sufficient sunlight and a
  focusable current target; a damaging stab requires the sword, eligible marked
  region, reach, current grip/body state and completed preparation.
- `CON-402`: first-colossus health must reach zero before the encounter settles
  and the automatic return can begin.
- Generalised `CON-534`: continued attachment requires compatible reachable
  static or moving surface, a grip-permitting pose and positive usable grip.
- Scarce route state: health, grip, current attachment, active weapon,
  guardian posture, wound/sigil state and guardian health.
- Claims: `SOC-002`, `SOC-004`, `SOC-006`–`SOC-010`.

### Information Genes

- `INF-075`: the HUD exposes Wander's health, grip, attack strength and active
  weapon before traversal or combat commitments.
- `INF-125`: the world map records past and present journeys without disclosing
  a complete automatic route to the current guardian.
- `INF-258`: fur, ledges, pose, slip and body motion reveal local climbing
  affordance and the risk of losing attachment.
- Generalised `INF-318`: the encounter surface exposes the active guardian's
  remaining health even though the original interface does not need to print a
  separate boss name.
- New `INF-369`: visible sword rays converge toward the current target bearing
  without revealing distance or turn-by-turn route.
- New `INF-370`: the equipped sword makes the rear-leg wound and crown sigil
  legible without explaining how to traverse between them.
- Claims: `SOC-002`, `SOC-004`, `SOC-006`–`SOC-009`.

### Objective Genes

- New `OBJ-206`: use the authored bearing to find the first guardian, change
  and traverse its body topology, deplete the required Normal-mode crown sigil
  and regain ordinary control after the automatic Shrine return.
- Success, evaluation and failure: finding, kneeling or reaching the crown is
  insufficient; zero guardian health plus settled hub control is required.
  Zero Wander health is failure.
- Claims: `SOC-006`–`SOC-010`.

### Time Genes

- `TIM-003`: movement, Agro, guardian attacks, body topology, grip drain and
  recovery, held preparation and damage resolve on one shared real-time clock.
- Claims: `SOC-003`–`SOC-009`.

## Reproducible transitions

| Before | Action | Deterministic or bounded resolution | Establishes | Claim |
|---|---|---|---|---|
| Wander is in sufficient direct sunlight with the sword equipped | hold Circle and aim | separated rays converge along the bearing to the first current target | optical world search | `SOC-002` |
| Agro is called and within mounting reach | press the mount command, steer and later dismount | direct route authority moves between Wander's foot and horse traversal states | persistent mount | `SOC-003` |
| Compatible fur is reachable and grip is positive | hold R1 and aim movement | attachment persists while grip drains; release or zero grip removes the hold | stamina-bounded climb | `SOC-004` |
| Wander reaches a stable stone ledge on the guardian | release grip and rest | attachment cost stops and usable grip recovers before the next ascent | rest cadence | `SOC-004`, `SOC-005` |
| The rear-left-leg wound is marked and reachable | prepare and stab it | wound progress makes the guardian kneel and exposes the intended upward connection | damage edits topology | `SOC-006` |
| Wander is attached near the crown with sword equipped | read the sigil, hold preparation and release a stab | an accepted hit lowers encounter health; guardian motion may interrupt later preparation or attachment | weak-point damage | `SOC-005`, `SOC-007`, `SOC-008` |
| Guardian health reaches zero | settle victory | the guardian collapses and the black-tendril return transition takes authority | hunt terminal precursor | `SOC-008`, `SOC-010` |
| Automatic return completes | finish the Shrine transition | ordinary Wander control resumes at the Shrine with the first colossus defeated | scoped positive terminal | `SOC-010` |

## Strategic and experiential structure

- Local decision: decide whether the current surface is grippable or safe to
  stand on, whether grip supports the next movement, when to release, and when
  the guardian's motion leaves enough stability to prepare a stab.
- Medium-term planning: use the bearing without a route line, bring Agro over
  the open field, identify the leg trigger, preserve enough grip to reach the
  next rest point and approach the crown with capacity for several attempts.
- Long-term structure: one giant converts hostile anatomy into a route whose
  graph changes after local damage. Victory removes the current guardian and
  returns the same avatar to a persistent hub for a new target; later hunts are
  outside the packet.
- Decision texture: navigation depends on an optical cue that must be actively
  focused; traversal depends on reading a moving body; offence and locomotion
  share the same attachment context, so a long charged stab competes with the
  grip needed to remain on the target.

## Replay and variation

- What changes between attempts: incidental damage, exact field line, mount
  timing, colossus attacks and shakes, remaining grip, number of rests, failed
  attachment attempts and accepted stab charge may vary.
- Randomness or procedural generation: the Shrine, field, cliff approach,
  guardian body, leg wound, crown sigil and automatic return are authored. No
  procedural layout or random objective is claimed.
- Multiple viable strategies: movement, recovery and stab timing may differ,
  but the accepted bounded route still uses the leg trigger and crown sigil on
  fresh Normal rules.
- Typical replay motive: faster victory, fewer falls or less damage. Time
  Attack, score comparison and Hard-mode target sets are excluded.

## Adjacent systems and history

- Direct series relation: none; later remasters and the remake reproduce the
  premise but are not assumed identical in controls, rendering, difficulty or
  content.
- Similar games: `GAME-0203` PEAK shares stamina-priced gripping on compatible
  surfaces; `GAME-0262` DARK SOULS III shares one visible guardian-health
  encounter; `GAME-0151` Monster Hunter Wilds shares a large moving hostile
  with localized body-state effects. None makes the same required enemy both a
  sunlight-located destination and the complete changing climb route.
- Important difference: the guardian is not merely fought on an arena. Its
  fur, ledges, posture and reactions are the traversal topology that must be
  read and edited before health-bearing damage becomes possible.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-161`, `ACT-271`, `ACT-348`, `ACT-362`, `ACT-495` | Wander, Agro, sword, exact controls and target bearing are parameters |
| System Behaviour | `SYS-215`, `SYS-578`, `SYS-661`, `SYS-983` | health values, grip values, body regions, posture and shake timing are parameters |
| Constraint | `CON-269`, `CON-402`, `CON-534` | sunlight, reach, charge, guardian health and surface tags are parameters |
| Information | `INF-075`, `INF-125`, `INF-258`, `INF-318`, `INF-369`, `INF-370` | HUD styling, ray rendering, map projection and sigil art are presentation parameters |
| Objective | `OBJ-206` | guardian, hub, required Normal sigil and return transition are parameters |
| Time | `TIM-003` | frame cadence and exact motion timing are parameters |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `355` (`GAME-0001`–`GAME-0355`).
- Exact genome matches: none.
- Tied near matches: `GAME-0355` — Metroid Prime (`8 / 33 = 0.242424`).
- Supported combination subsets: none.
- Scan date: 2026-09-22.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0355` — Metroid Prime | `ACT-008`, `ACT-161`, `SYS-215`, `SYS-578`, `CON-269`, `CON-402`, `INF-125`, `TIM-003` | Both packets use direct traversal, direct attacks, live hostile pressure, one health reserve, ability legality, finite guardian clearance, map support and shared real time. Shadow of the Colossus adds mounted field travel, stamina-priced gripping, active optical bearing, a damage-edited living climb graph, sword-revealed sigils and automatic Shrine return; Metroid Prime adds visor/form switching, target-relative lock, typed scanning, finite missiles, a deadline and forced capability loss before a new-world landing. | Near, `8 / 33 = 0.242424` |

- New genes: `ACT-495`, `SYS-983`, `INF-369`, `INF-370` and `OBJ-206`.
- Classification result: New gene and generalised gene.
- Evidence and reasoning: no lower-ID boundary owns player-focused optical
  convergence, one hostile body as a damage-edited climb graph, tool-gated
  anatomical disclosure or the complete locate–climb–automatic-return terminal.
  The existing grip and guardian-health genes broaden without changing their
  operational identity.

### Preserved research notes

- New genes: `ACT-495`, `SYS-983`, `INF-369`, `INF-370` and `OBJ-206`.
- Classification result: New gene and generalised gene.
- Evidence and reasoning: no lower-ID boundary owns player-focused optical
  convergence, one hostile body as a damage-edited climb graph, tool-gated
  anatomical disclosure or the complete locate–climb–automatic-return terminal.
  The existing grip and guardian-health genes broaden without changing their
  operational identity.
- Generalised genes: `ACT-362`, `SYS-661` and `CON-534` now accept compatible
  moving surfaces; `INF-318` accepts encounter presence as guardian identity.

## Taxonomy impact

- Registry changes: add five Active definitions, generalise four existing
  definitions and add complete reviewed Ukrainian coverage while preserving
  every earlier signature and lifecycle.
- Taxonomy-change record:
  [`TAXONOMY_CHANGE_095`](../../../research/taxonomy-changes/TAXONOMY_CHANGE_095.md).
- Candidate terms affected: retain Wander, Agro, sword, colossus anatomy,
  leg side, sigil location, exact grip and damage values as carrier parameters.

## Negative results

- No generic “boss as level”, “cinematic return”, “giant enemy” or “puzzle
  boss” gene is created. Each admitted boundary owns an observable transition.
- The leg wound is not merged into localized wound destruction: it changes the
  living body's traversable connectivity rather than yielding a material or
  ordinary stagger-only damage window.
- The crown does not create a special charged-attack gene. Direct strike and
  ability legality already own the prepared stab; charge strength and accepted
  hit count are parameters.
- Bow, fruit, lizards, save shrines, stat growth, later colossi, Hard sigils,
  Time Attack and remake features are excluded and add no genes.
- No direct play, disc, image, emulator, screenshot, video, audio or release
  parity is claimed.

## Delta summary

## New facts

- [Confirmed | Direct | High] The original manual separates visible health,
  grip and weapon state from sunlight-focused sword bearing and stamina-priced
  grip (`SOC-002`–`SOC-004`, `SOC-009`).
- [Observation | Corroborated | High] The first Normal guardian composes a leg
  wound that changes posture, a connected body climb, a crown health sigil and
  automatic Shrine return (`SOC-005`–`SOC-010`).

## New genes

- [Observation | Corroborated | High] Add `ACT-495`, `SYS-983`, `INF-369`,
  `INF-370` and `OBJ-206` under `TAXONOMY_CHANGE_095`.

## New combinations

- [Observation | Direct | High] No verified combination is registered from one
  new carrier.

## Taxonomy changes

- [Observation | Corroborated | High] `TAXONOMY_CHANGE_095` generalises
  `ACT-362`, `SYS-661`, `CON-534` and `INF-318`, adds five separate boundaries
  and preserves every earlier signature.

## Gene reuse and novelty notes

- Reused genes: `ACT-008`, `ACT-161`, `ACT-271`, `ACT-348`, `ACT-362`,
  `SYS-215`, `SYS-578`, `SYS-661`, `CON-269`, `CON-402`, `CON-534`,
  `INF-075`, `INF-125`, `INF-258`, `INF-318` and `TIM-003`.
- New genes: `ACT-495`, `SYS-983`, `INF-369`, `INF-370` and `OBJ-206`.
- Generalised definitions: `ACT-362`, `SYS-661` and `CON-534` now explicitly
  permit a moving compatible surface; `INF-318` now permits encounter presence
  rather than printed name to identify the one active guardian. No earlier
  signature changes.
- Rejected candidates: Agro identity, Ancient Sword identity, first-colossus
  anatomy, leg side, sigil location, Normal damage values, stab count and
  automatic black-tendril animation are parameters; ordinary route discovery,
  camera framing, music and rumble are not genes; bow, save, fruit, lizard and
  stat-growth rules are outside the exercised packet.
- Novelty conclusion: accept five bounded genes for active optical bearing,
  living-guardian topology, tool-revealed target regions and the hunt-to-hub
  objective. Reuse the established grip, health, mount, live-combat and HUD
  boundaries rather than naming colossus-specific duplicates.

## Open questions

- A separately bounded later-colossus unit could test whether the living-body
  topology boundary generalises across aerial, aquatic or environment-lured
  guardians. It is not inferred here.
- Direct execution of an owned `SCUS-97472` disc could replace the written
  route evidence with an exact controller/state trace and hash the disc image.
- No open question changes the admitted fresh-Normal first-colossus signature.
