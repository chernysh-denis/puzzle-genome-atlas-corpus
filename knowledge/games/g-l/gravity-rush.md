---
game_id: GAME-0468
slug: gravity-rush
game_title: Gravity Rush
analysis_status: reviewed
reviewed: 2026-10-01
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-295
    - ACT-618
    - ACT-619
  system:
    - SYS-036
    - SYS-037
    - SYS-215
    - SYS-1222
    - SYS-1223
    - SYS-1224
  constraint: []
  information:
    - INF-119
    - INF-125
    - INF-445
  objective:
    - OBJ-029
    - OBJ-265
  time:
    - TIM-003
---

# Game: Gravity Rush — first Nevi fight and fountain

Use the canonical [vocabulary and comparison rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). The exact geometry, enemy count, gauge capacity and gem placement are parameters, not separate genes.

## Analysis scope

- Version / ruleset: original English PS Vita *Gravity Rush* (2012), Episode 2, **Shadows Over the City**, from Kat's first required Nevi combat to the first fountain restored after collecting ten precious gems. This is not the later PS4 remaster, sequel or the whole open-world campaign. The exact Vita executable revision is uninspected.
- Structured analysis target: `PLAT-PLAYSTATION-VITA` in [platform coverage](../../platforms/games.json).
- Entry: Kat can be directly moved at the beginning of the episode's first ordinary Nevi encounter, with the early gravity-shift ability available. No later skill upgrades are assumed.
- Primary decision loop: move and kick on a surface or release Kat from ordinary gravity, aim a personal fall at a visible wall or airborne enemy and commit it; manage the finite gravity gauge and resume from normal down when the shift ends; clear the local Nevi, use the map marker to reach the first fountain, contact enough precious gems and activate the fountain.
- Positive terminal: the required Nevi encounter has been cleared and the first fountain has been activated with the local gem threshold met. The unlocked optional challenge and any subsequent chapter are outside this packet.
- Negative or interrupted state: ordinary combat can defeat Kat; an exhausted gravity gauge returns her to ordinary falling rather than making a shifted attack or wall approach last indefinitely. No exact death/restart transition or gauge duration was independently measured.
- Included: directly steered ground traversal and ordinary kicks; float/aim/commit/cancel gravity shift; avatar-local sideways fall and surface landing; gravity kick; finite gauge and visible aim/resource cues; real-time Nevi exchange; contact acquisition of precious gems; map/fountain marker; ten-gem activation threshold and explicit service restoration.
- Excluded: later gravity powers, special attacks, ability upgrades, subsequent challenge missions, every other fountain, all story chapters, DLC, PS4 remaster controls and any exact gauge drain, gem debit or damage constants. These exclusions do not assert those features are absent from the complete game.
- Reproducible parameterisation: original Vita model and retail build identifier, input/control configuration, Episode 2 start state, position and heading of Kat and each required Nevi, personal gravity vector, gauge and health at each input, traversed surface collisions, collected gem count, fountain interaction and resulting service state. No such executable trace was available.
- Potential scoped modules: the next unlocked fountain challenge, later combat skills, whole-city free exploration and edition comparison.
- Direct-play status: no Vita, cartridge/download build, controller trace, screenshot, video, audio or direct play was inspected. This is a bounded documentary reconstruction from PlayStation's contemporary descriptions and written original-Vita guides. The original illustration is interpretive, not a captured frame.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `GR-001` | The original Vita game lets Kat float, aim her own fall toward a visible side surface and cancel to ordinary down. | Observation | Corroborated | High | P1, P2, S1 |
| `GR-002` | Ground kicks and gravity-assisted airborne kicks are distinct ways to strike Nevi during live combat. | Observation | Corroborated | High | P1, P3, S1, S2 |
| `GR-003` | Gravity shifting uses a finite gauge that recovers outside an active shift; exhaustion ends sustained shifted movement. | Observation | Corroborated | Medium | S1, S3 |
| `GR-004` | Episode 2 moves from an early Nevi encounter to the first fountain; collecting ten precious gems permits fountain activation. | Observation | Corroborated | Medium | S1, S2 |
| `GR-005` | Kat can read a current gravity aim cue and personal resource state, and navigate to a marked local objective. | Observation | Corroborated | Medium | S1, S2, S3 |
| `GR-006` | The personal gravity vector changes Kat's movement and landing without globally reorienting every city body or surface. | Strong Pattern | Corroborated | High | P1, P2, `GR-001` |
| `GR-007` | Exact gauge constants, every enemy position, gem debit and save/restart behaviour cannot be pinned from the inspected evidence. | Observation | Limited | High | P1–P3, S1–S3 |

## Basic data

- Release / origin: original 2012 PS Vita *Gravity Rush* by Japan Studio / Team Gravity. The analysis concerns English original-release rules, not an asserted disc or patch hash.
- Puzzle families: `FAM-010` real-time system pressure and `FAM-014` world topology and perspective. The latter is a local traversability/orientation change for Kat, **not** a global gravity rewrite.
- **[P1]** [PlayStation's original Vita gameplay overview](https://blog.playstation.com/2011/09/16/gravity-rush-for-ps-vita-everything-you-need-to-know/), 2011: Kat, cat, personal shift, sideways surface landing, ordinary fall and gravity-assisted attacks; accessed 2026-10-01.
- **[P2]** [PlayStation's creator interview](https://blog.playstation.com/archive/2012/03/14/gravity-rushs-creators-reveal-the-games-origins), 2012: the deliberate horizontal/vertical fall concept; accessed 2026-10-01.
- **[P3]** [PlayStation's original Vita demo announcement](https://blog.playstation.com/2012/05/29/gravity-rush-demo-hits-psn-today/), 2012: motion-controlled gravity and Nevi combat; accessed 2026-10-01. Demo coverage corroborates mechanics but is not treated as the episode walkthrough.
- **[S1]** [Contemporary original-Vita chapter and control guide](https://gamefaqs.gamespot.com/vita/620274-gravity-rush/faqs/64450), June 2012: Episode 2 combat, map/fountain route, gems, gauge and controls; accessed 2026-10-01. Written player guide, not direct testing by this project.
- **[S2]** [IGN's contemporary Gravity Rush guide](https://www.bazicenter.com/features/ign_guides/gravity-rush.pdf), Episode 2: ground and air attacks, map route, ten gems and fountain; accessed 2026-10-01. Secondary walkthrough; exact build and inputs remain uninspected.
- **[S3]** [Contemporary Vita review](https://www.avforums.com/reviews/gravity-rush-ps-vita-review.728/), 2012: gravity reticle and finite/recovering shift resource; accessed 2026-10-01.

## Mechanical decomposition

### Action Genes

- Reuse `ACT-008` for directly moving Kat through connected ground and wall surfaces; the motion is not a remote waypoint command.
- Reuse `ACT-295` for Kat's ordinary player-committed ground kick. It does not itself encode the gravity-assisted approach.
- New `ACT-618` for float → aim → commit or cancel a personal directed fall. `ACT-097` is excluded because it selects an orthogonal face and changes a global gravity frame, whereas Kat's personal fall can be aimed at a visible side surface while the city retains its orientation.
- New `ACT-619` for the distinct airborne gravity-kick commitment after aiming at a hostile. The attack may miss or be interrupted; target selection does not guarantee damage.

### System Behaviour Genes

- Reuse `SYS-036` for falling, moving and colliding with available city surfaces under continuous dynamics; this generic physics gene does not define *which* gravity frame is active.
- Reuse `SYS-037` for contacting precious gems and crediting them without immediately ending the chapter.
- Reuse `SYS-215` for real-time direct attacks and Nevi damage/defeat resolution; no turn queue is imported.
- New `SYS-1222` applies a local gravity vector and orientation to Kat and restores ordinary down after cancellation. `SYS-125` is explicitly world-global and does not transfer.
- New `SYS-1223` drains and recovers Kat's shift gauge, constraining flight and aerial attack. The exact time to exhaustion is not asserted.
- New `SYS-1224` restores the first fountain only after its gem threshold and explicit activation. The ten-gem requirement is documented; the precise debit is deliberately not encoded.

### Constraint Genes

- No separate Constraint is added. The shift resource is a dynamic system (`SYS-1223`), the fountain threshold is part of the service rule (`SYS-1224`), and valid surface contact is resolved by `SYS-036` / `SYS-1222`. A Vita controller and exact numeric capacities are reproducibility parameters.

### Information Genes

- Reuse `INF-119` for Kat's visible health and gravity resource, without claiming exact numeric HUD values.
- Reuse `INF-125` for the local explored map and fountain mission marker; unseen map contents are not assumed visible.
- New `INF-445` for the aim cue and visible landing/attack direction. A reticle is not a guarantee of safety or hit.

### Objective Genes

- Reuse `OBJ-029` for clearing the bounded finite Nevi encounter as a required intermediate gate.
- New `OBJ-265` for the whole selected episode sequence: clear the threat, collect the local threshold and explicitly restore the fountain. Combat alone does not satisfy the chapter terminal.

### Time Genes

- Reuse `TIM-003`: combat, fall, collision and gauge depletion continue while inputs are selected; the chapter does not wait on discrete turns.

## Reproducible transitions

| Before | Input or event | Source-derived resolution | Boundary | Claim |
|---|---|---|---|---|
| Kat is grounded near the first Nevi | Move into ordinary kick range and attack | A legal kick exchanges damage during live combat | Ground combat, not a gravity kick | `GR-002` |
| Kat can shift and a tower wall is visible | Enter float, aim at the wall and commit | Kat falls sideways toward that surface and can land there | Personal vector, city frame unchanged | `GR-001`, `GR-006` |
| Kat is floating with a Nevi in the aimed line | Commit gravity kick | Directed fall supplies an airborne attack approach; hit still depends on contact | Attack after aim, not automatic damage | `GR-002` |
| A shift is active | Cancel it or let the finite gauge exhaust | Ordinary downward fall resumes; shifting cannot persist indefinitely | No exact duration claimed | `GR-001`, `GR-003` |
| Required Nevi remain | Defeat the last required enemy | Encounter gate clears and the local fountain route becomes the current task | Not the complete packet terminal | `GR-002`, `GR-004` |
| Kat reaches a precious gem | Contact it | Gem count grows while movement continues | Pickup alone does not restore fountain | `GR-004` |
| At least ten gems have been collected | Interact with the first fountain | Fountain service activates and the bounded chapter segment ends | Optional challenge excluded; gem debit unknown | `GR-004` |

These are documentary rule cases, not outcomes of locally executed gameplay.

## Strategic and experiential structure

- A visible wall becomes a route only when Kat's personal gravity is aimed and sustained long enough to reach it. Surface geometry, current gauge and fall direction matter together; the city does not rotate for everyone.
- Ground and aerial combat share a live hostile but have different approach commitments. The gravity kick trades a stronger directed attack opportunity against aiming, spatial contact and a draining reserve.
- Nevi defeat changes the local task from hostile survival to route-finding and gem collection; ten collected gems make the fountain available. This ordered objective cannot be compressed to “defeat enemies” or “collect currency.”

## Replay and variation

- Different trajectories, surface choices, combat positioning and gem routes can reach the same fountain terminal. The cited sources do not establish exact enemy or gem permutations for a fixed build.
- An unlocked challenge and upgrades offer further play, but are outside the selected packet.

## Adjacent systems and history

- *Manifold Garden* changes a selected orthogonal world gravity frame, including cube eligibility. Gravity Rush changes Kat's personal down direction in an otherwise stable city; treating these as the same action or system would erase the key boundary.
- *Portal* retains velocity through linked apertures under ordinary world gravity; it does not grant Kat's float/aim/personal-fall command. Ordinary combat and item pickup genes can still transfer unchanged across these games.

## Normalised genome

| Type | Active gene IDs | Boundary |
|---|---|---|
| Action | `ACT-008`, `ACT-295`, `ACT-618`, `ACT-619` | move, ground attack, personal fall and gravity kick |
| System Behaviour | `SYS-036`, `SYS-037`, `SYS-215`, `SYS-1222`, `SYS-1223`, `SYS-1224` | physics, pickup, combat, local shift, gauge, fountain |
| Constraint | none | thresholds and contacts remain within their resolving systems |
| Information | `INF-119`, `INF-125`, `INF-445` | resource, map and aim cues |
| Objective | `OBJ-029`, `OBJ-265` | encounter gate and full local restoration |
| Time | `TIM-003` | continuous decision state |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `467` (`GAME-0001`–`GAME-0467`).
- Exact genome matches: none.
- Tied near matches: `GAME-0389` — Mega Man 2 (`6 / 26 = 0.230769`).
- Supported combination subsets: none.
- Scan date: 2026-10-01.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0389` — Mega Man 2 | `ACT-008`, `SYS-036`, `SYS-037`, `SYS-215`, `INF-119`, `TIM-003` | Both directly move a combatant through force-constrained real-time geometry, collect items and expose personal resources. Mega Man 2 uses fixed platform ascent, shot/tool abilities, boss weapons and a stage guardian; Kat instead aims an avatar-local gravity fall, turns that fall into an aerial kick, manages a shifting gauge and restores a fountain after collecting gems. The moderate overlap does not imply shared gravity control. | Tied near, `6 / 26 = 0.230769` |

### Preserved research notes

- New genes: `ACT-618`, `ACT-619`, `SYS-1222`–`SYS-1224`, `INF-445`, `OBJ-265`.
- Reused genes: `ACT-008`, `ACT-295`, `SYS-036`, `SYS-037`, `SYS-215`, `INF-119`, `INF-125`, `OBJ-029`, `TIM-003`.
- Classification result: `New genes`.
- Evidence and reasoning: avatar-local gravity, directed aerial attack and a finite recharging gauge are not a world-global orthogonal frame change. No earlier signature changes.

## Taxonomy impact

- Seven new Active definitions across four types; no previous genome or verified combination changes.
- Taxonomy-change record: [`TAXONOMY_CHANGE_205`](../../../research/taxonomy-changes/TAXONOMY_CHANGE_205.md).

## Negative results

- No original Vita executable or direct audiovisual observation. Exact input windows, gauge constants, full mission enemy set and persistence behaviour remain unresolved.
- The combat/collection chapter does not establish every open-world system, later upgrades or later gravity powers.
- Collection of ten gems is a documented threshold, not evidence that exactly ten are consumed on activation.
- The source illustration represents one mechanically plausible sideways approach, not a frame from the game or a proof of the chapter's exact geometry.

## Delta summary

## New facts

- [Observation | Corroborated | High] Original Vita Kat can redirect her own fall toward a side surface and use that fall for an attack (`GR-001`, `GR-002`).

## New genes

- [Observation | Corroborated | Medium] Seven definitions isolate personal gravity aim and resolution, aerial attack, finite gauge, aim information and fountain terminal.

## New combinations

- [Observation | Direct | High] None claimed until the verified-subset scan is computed.

## Taxonomy changes

- [Observation | Corroborated | Medium] Seven new definitions, no migration of older games.

## Open questions

- Direct original-Vita execution could pin gauge rates, episode enemy/gem layout, fountain payment and restart state.

## Next research candidate

- None selected. `GAME-0468` closes the maintainer-approved nine-game horizon; a later selection needs a new request.
