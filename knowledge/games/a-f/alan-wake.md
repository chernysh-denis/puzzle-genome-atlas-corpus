---
game_id: GAME-0427
slug: alan-wake
game_title: Alan Wake
analysis_status: reviewed
reviewed: 2026-09-27
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-161
    - ACT-223
    - ACT-453
    - ACT-566
  system:
    - SYS-215
    - SYS-791
    - SYS-1126
    - SYS-1127
    - SYS-1128
  constraint: []
  information:
    - INF-119
    - INF-419
  objective:
    - OBJ-029
  time:
    - TIM-003
---

# Game: Alan Wake — strip the darkness before firing

Use the canonical [vocabulary and genome rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). The flashlight, Taken, revolver and single passage are parameters, not additional genes.

## Analysis scope

- Version / ruleset: original 2010 Xbox 360 *Alan Wake*, Normal single-player story, Episode 1 “Nightmare”, immediately after the shooting tutorial. The original instruction manual and first-hand route accounts were inspected, not a disc or exact executable revision.
- Structured analysis target: `PLAT-XBOX-360` in [`knowledge/platforms/games.json`](../../platforms/games.json).
- Primary decision loop: while one Taken closes in near the low timber ledge, position or dodge; hold the flashlight beam on its protective darkness, optionally boost the beam at the cost of its charge, release boost to let charge recover or insert a finite carried battery; read the contracting light corona and its bright break cue; only then shoot the exposed Taken with the revolver.
- Entry and exit: start after the shooting tutorial with Alan carrying a flashlight and revolver and the first isolated Taken approaching. End the analytical encounter when that one Taken is defeated, before following the downhill route to the subsequent pair. This is an **analytical endpoint**, not a claim that killing this foe is a hard story gate.
- Included: direct movement, timed dodge, flashlight aim/boost, protected-versus-exposed target state, automatic non-boost charge recovery, optional battery refill, revolver shots, visible corona and personal HUD, live enemy attack and bounded defeat.
- Excluded: revolver-cylinder reload as unnecessary for the selected one-foe packet, tutorial weapon grant and its scripted lesson, the following two Taken, flares and flare gun, generator, manuscript pages, later episodes, strong-Taken darkness regeneration, exact attack/charge/ammunition rates, Nightmare difficulty, *American Nightmare*, the remaster and modern backwards-compatibility rules.
- Potential scoped modules: safe-haven light and health recovery, flare radius against multiple Taken, environmental generators and later hostile variants.
- Direct-play status: no Xbox 360, original disc, executable, input trace, screenshot, video or audio was inspected. The original Microsoft/Remedy manual directly establishes the combat rules; an independent first-hand walkthrough identifies the first isolated post-tutorial Taken. Exact enemy timing, health and beam depletion are unmeasured.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `AW-001` | Darkness protects a Taken from ordinary harm until directed light removes the shroud; the shrinking corona and bright flash communicate that transition. | Confirmed | Direct | High | P1 |
| `AW-002` | Boosting the flashlight strips darkness faster while spending charge; releasing boost lets the flashlight recharge even though its ordinary beam remains on. | Confirmed | Direct | High | P1 |
| `AW-003` | A carried battery can refill flashlight charge; the revolver uses finite ammunition and can be reloaded. | Confirmed | Direct | High | P1 |
| `AW-004` | The route just after the shooting tutorial presents a first lone Taken near a low wooden structure before the route descends to two more. | Observation | Corroborated | Medium | S1, S2 |
| `AW-005` | Movement and dodge can preserve space while aiming and shooting in a real-time hostile encounter. | Observation | Corroborated | High | P1, S1 |
| `AW-006` | This packet ends with defeat of the first isolated Taken, but the available route does not establish that the game itself gates continuation on that kill. | Hypothesis | Limited | Medium | S1 |

## Basic data

- Release / origin: Remedy Entertainment's original *Alan Wake*, released for Xbox 360 in 2010; original-console rules rather than the remaster.
- Platform or physical form: Xbox 360 controller, single-player third-person movement, aim/boost and firearm inputs.
- Mechanical families: tactical forecast and counterplay (`FAM-009`) and ordered dependency sequencing (`FAM-017`): dodge the approaching hostile while making it legally vulnerable before spending shots.
- Primary source, accessed 2026-09-27: **P1** — [original Xbox 360 *Alan Wake* instruction manual, Microsoft/Remedy scan](https://manuals.plus/m/3537e546dddabff38ce730c0e9cb1dcfdb522d89325690ea6ae65575ec6b36c8), 2010, pp. 4–7, 10–16; controls, HUD, Taken protection, bright vulnerability cue, beam boost, automatic recharge, battery insertion and revolver.
- Independent first-hand sources, accessed 2026-09-27: **S1** — [AlanWake.info, Episode 1 dream-sequence walkthrough](https://www.alanwake.info/2000/05/walkthrough-3-episode-01-dream-sequence.html), first isolated Taken after shooting tutorial and subsequent pair. **S2** — [GameFAQs Xbox 360 walkthrough, “Follow the Light”](https://gamefaqs.gamespot.com/xbox360/928006-alan-wake/faqs/59980), original-release route and flashlight/revolver use.

## Mechanical decomposition

### Action Genes

- Reused `ACT-008`: move Alan around the constrained forest passage instead of issuing a destination command. `AW-004`, `AW-005`.
- Reused `ACT-161`: aim and fire the currently held revolver at the reachable Taken **after** its shroud is gone. A shot into intact darkness does not substitute for the light phase. `AW-001`, `AW-003`.
- Reused `ACT-223`: choose a timed dodge against the approaching hostile rather than treating damage as a turn-based event. `AW-005`.
- Reused `ACT-453`: deliberately insert one finite carried flashlight battery to refill charge. `AW-003`.
- New `ACT-566`: aim the already-lit handheld beam at the Taken and choose whether to hold its boost; unlike Luigi's *withhold-then-surprise* input, this is continuous shroud stripping with a charge trade-off. `AW-001`, `AW-002`.

### System Behaviour Genes

- Reused `SYS-215`: both Alan and the Taken act in real time; legal revolver hits settle through the combat system. `AW-001`, `AW-005`.
- Reused `SYS-791`: an accepted battery insertion consumes finite carried stock and restores the portable light's charge. `AW-003`.
- New `SYS-1126`: directed illumination progressively removes the Taken's protective darkness; ordinary bullets cannot wound through the intact shroud, but become effective after the bright break. This is **not** the brief ghost-heart surprise window of `SYS-1080`. `AW-001`.
- New `SYS-1127`: holding boost accelerates shroud erosion and drains the flashlight's bounded internal charge; the ordinary beam is not itself a charge-draining toggle. `AW-002`.
- New `SYS-1128`: while boost is released, flashlight charge recovers automatically without consuming carried batteries **even with the normal light still shining**. This differs from inactive-device recharge (`SYS-851`). `AW-002`.
- Resolution order: approach and defensive position → beam contact and optional boost → corona contracts → shroud breaks with bright flash → eligible revolver fire defeats the lone foe. `AW-001`–`AW-005`.

### Constraint Genes

- None added. Charge, battery stock and ammunition are parameters of the corresponding action/system boundaries; the manual does not support a separate fixed countdown or required number of shots for this foe.

### Information Genes

- Reused `INF-119`: the HUD exposes Alan's health, flashlight charge/battery stock and selected weapon/ammunition. `AW-003`.
- New `INF-419`: a Taken's light corona contracts under exposure and a bright flash signals complete shroud removal, distinguishing the otherwise unsafe shot from an eligible one. `AW-001`.

### Objective and Time Genes

- Reused `OBJ-029`: defeat the one declared hostile before Alan falls. This is the chosen encounter boundary, **not** proof of a hard progression gate. `AW-004`, `AW-006`.
- Reused `TIM-003`: movement, enemy approach, light exposure, dodging and gunfire progress on a live clock. `AW-005`.

## Reproducible transitions

| Before | Action | Bounded resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| First Taken approaches with intact darkness | Aim the normal beam at it | Its corona contracts with sustained illumination | light changes protection before bullets are useful | `AW-001` |
| Darkness remains and charge is available | Hold beam boost | Shroud removal accelerates as flashlight charge drains | speed and device charge trade off | `AW-002` |
| Boost has reduced charge | Release boost without switching the ordinary beam off | Internal charge recovers without consuming a carried battery | regeneration is conditional on boost, not on a dark flashlight | `AW-002` |
| Charge is low and a spare battery exists | Insert one battery | Carried stock falls and flashlight charge rises | finite backup differs from automatic recharge | `AW-003` |
| Corona gives the bright full-removal cue | Fire an aimed revolver shot | The now-exposed Taken can take conventional damage | light phase precedes legal gun damage | `AW-001`, `AW-003` |
| Taken remains active nearby | Dodge or reposition, then continue exposure and fire | Alan preserves room during live hostile pressure | combat is not a static two-button combination | `AW-004`, `AW-005` |

## Strategic and experiential structure

- Local decision: protect space while choosing boosted versus ordinary beam and the moment to spend ammunition.
- Medium-term planning: keep spare battery and ammunition available but exploit free non-boost recharge when safe enough; exact stock at this route point was not measured. The manual documents revolver reload generally, but a reload is not required by the selected one-foe encounter and `ACT-183` is limited to magazine-fed weapons.
- Long-term structure: later multi-enemy encounters and environmental light sources alter the calculus but are excluded from this one-foe packet.
- Common heuristic: wait for the bright break cue before treating revolver fire as damage against a dark-shrouded Taken.
- Failure attribution: shooting too early is not evidence of an inaccurate weapon; retreating or dodging can create time to finish the light phase. Exact damage and recovery windows remain unmeasured.
- Player-trust factors: the corona, break flash and charge HUD expose the phase and resource state rather than hiding an arbitrary vulnerability flag.

## Replay and variation

Alan can vary movement, dodge timing, boost use, battery insertion and shot count. The manual supports those options but not a fixed optimal path, damage table, enemy HP or exact recharge cadence for this specific first foe. No random spawn or dynamic difficulty rule is asserted.

## Adjacent systems and history

*Luigi's Mansion* suppresses then flashes a light to briefly expose a ghost's heart; *Alan Wake* keeps a normal flashlight beam available and progressively burns away a damage-blocking darkness shroud. *Alien: Isolation* also uses a finite flashlight battery, but its active light drains charge, whereas Alan's ordinary light recharges when boost is released. These distinct conditions prevent false reuse of `ACT-543`, `SYS-1080`, `SYS-754` or `SYS-851`.

## Normalised genome

| Type | Active gene IDs | Key parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-161`, `ACT-223`, `ACT-453`, `ACT-566` | movement, dodge, directed beam/boost, battery, revolver |
| System Behaviour | `SYS-215`, `SYS-791`, `SYS-1126`, `SYS-1127`, `SYS-1128` | darkness gate, boosted drain, non-boost recharge, real-time combat |
| Constraint | none | no separate fixed timer or measured shot threshold |
| Information | `INF-119`, `INF-419` | player HUD, target corona and break cue |
| Objective | `OBJ-029` | bounded defeat of one Taken |
| Time | `TIM-003` | live encounter |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `426` (`GAME-0001`–`GAME-0426`).
- Exact genome matches: none.
- Tied near matches: `GAME-0277` — Cuphead (`7 / 21 = 0.333333`).
- Supported combination subsets: none.
- Scan date: 2026-09-27.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0277` *Cuphead* | `ACT-008` movement, `ACT-161` aimed attack, `ACT-223` dodge, `SYS-215` live combat, `INF-119` player HUD, `OBJ-029` bounded enemy defeat and `TIM-003` real-time decisions | *Cuphead*'s authored boss patterns, parry and shot types differ from *Alan Wake*'s light-dependent damage gate, boosted flashlight charge, spare batteries and corona cue. A revolver shot is only useful after the Taken's darkness breaks. | Tied-near maximum, `0.333333`; not exact or a verified combination match. |

## Taxonomy impact

[`TAXONOMY_CHANGE_165`](../../../research/taxonomy-changes/TAXONOMY_CHANGE_165.md) admits one directed-beam action, three light/shroud and charge-system boundaries, and one vulnerability cue. Earlier signatures and verified combinations are not revised.

## Negative results

- `ACT-543` and `SYS-1080` rejected: the first game's deliberately hidden flashlight and temporary ghost heart do not model ongoing Taken-shroud erosion.
- `SYS-754` and `SYS-851` rejected: the normal Alan Wake beam remains on while charge recovers after **boost** release.
- No claim that this first Taken's shroud regenerates: the manual says some stronger variants do, not that this foe does.
- `ACT-183` rejected: its canonical boundary is magazine-fed reload, not the revolver cylinder; no reload is needed to establish the selected light-before-shot loop.
- No claim that this kill is a mandatory progression gate, that a precise number of shots is required, or that later flare/generator rules apply.

## Delta summary

The route makes firearm damage conditional on a visible light-stripping phase, with faster exposure purchased using rechargeable flashlight charge and finite batteries as backup.

## New facts

- [Confirmed | Direct | High] A Taken's darkness blocks ordinary damage until light removes it; a shrinking corona and break flash signal the state (`AW-001`).
- [Confirmed | Direct | High] Boost drains a rechargeable charge pool while ordinary illumination remains available (`AW-002`).
- [Observation | Corroborated | Medium] The first isolated post-tutorial Taken bounds a one-foe analytical encounter (`AW-004`, `AW-006`).

## New genes

- [Confirmed | Direct | High] `ACT-566`, `SYS-1126`, `SYS-1127`, `SYS-1128` and `INF-419` preserve directed exposure, the damage gate, charge trade-off and cue separately.

## New combinations

- [Observation | Direct | High] None created; verified prior combinations are scanned against the full signature.

## Taxonomy changes

- [Confirmed | Direct | High] `TAXONOMY_CHANGE_165` admits five typed boundaries without retroactively changing prior genomes.

## New questions

- What are measured beam contact, charge drain/recovery and revolver damage values on an inspected original Xbox 360 disc revision?
- Is the first lone Taken's defeat mandatory to advance the exact Episode 1 path, or merely the prudent route taken in the walkthrough?

## Next recommended game

- [Hypothesis | Limited | Medium] `GAME-0428` *Super Mario Maker* only after this unit's full validation, one local commit and Goal stop window.
- Optimisation criterion: contrast combat vulnerability with authored-course legality and test-play.
- Expected information gain: edit/test dependencies rather than reactive hostile pressure.
- Backlog impact: no successor is started in this unit.
