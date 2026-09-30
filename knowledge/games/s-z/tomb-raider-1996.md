---
game_id: GAME-0451
slug: tomb-raider-1996
game_title: Tomb Raider (1996)
analysis_status: reviewed
reviewed: 2026-09-30
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-049
    - ACT-089
    - ACT-131
    - ACT-161
    - ACT-341
    - ACT-595
    - ACT-596
    - ACT-597
  system:
    - SYS-036
    - SYS-057
    - SYS-215
    - SYS-369
    - SYS-578
    - SYS-1049
    - SYS-1185
    - SYS-1186
  constraint:
    - CON-621
    - CON-727
    - CON-728
  information:
    - INF-436
  objective:
    - OBJ-026
  time:
    - TIM-003
    - TIM-007
---

# Game: Tomb Raider (1996) — original PlayStation Caves

Use the [canonical vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Jump distances, layout, damage, crystal position and door duration are parameters, not genes.

## Analysis scope

- Version / ruleset: original English 1996 *Tomb Raider* for PlayStation, the first Caves level. The original Eidos PlayStation booklet is the primary rule artifact; a European reprint independently confirms walking. No exact disc executable or regional timing was inspected. Anniversary, the 2013 game, Remastered controls and PC save-anywhere are excluded.
- Primary decision loop: inspect the nearby cave, align Lara and choose running, guarded walking, a jump or a held ledge; holster pistols when hands are needed, or draw and fire at the automatically acquired hostile; collect and optionally consume a medi pack, operate a reachable switch, and cross its opened passage before a timed door closes. Preserve progress at the console save beacon when available, then continue to the level exit.
- Entry and exit: New Game, first controllable position after the cave-entry cinematic, with pistols and compass. Positive exit is Caves' completion/statistics screen after passing the final opened doors; death ends the current attempt with load/restart/quit choices. Optional secrets remain optional, not clearance prerequisites.
- Included: authored caves and optional local health caches; facing-relative running, walking, jumping, roll and sidesteps; manual ledge hold, shimmy and pull-up; physical falling and damage; drawn/holstered pistols with unlimited ammunition; held-target shooting; live animal pursuit/combat and dart hazards; pickup, immediate healing, inventory feedback; ordinary switches and a time-limited passage; breakaway support; the local save crystal, memory-card eligibility and load/restart; camera look and level arrival.
- Excluded: swimming, oxygen, pushable blocks, keys/receptors, other weapons and finite ammunition, later levels, the whole Scion quest, secret-count optimisation, cheats/glitches, exact damage, trap periods, jump frame windows, enemy algorithms, door seconds, save-slot allocation and every later port/remake's rule changes. Potential scoped modules are an underwater route or a keyed block puzzle in an explicitly named later level.
- Direct-play status: no original disc, executable, input trace, save file, screenshot, video or live play was inspected. This is a manual-led reconstruction of Caves corroborated by a first-hand written classic-game route. The primary scan omits printed pp. 6–9; walking is checked against a complete publisher-authored European reprint rather than claimed to be present in that scan. Its conflicting default Jump/Roll table does not determine this unit's bindings. Exact executable behaviour and a successful attempt remain unmeasured.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `TR96-001` | Caves starts with pistols/compass and includes hostile animals, dart passages, switches, a timed door, breakaway tiles and a console save crystal before the exit. | Observation | Limited | Medium | S1 |
| `TR96-002` | Local movement permits directional jumps and a manually held ledge, sideways shimmy, pull-up and release. | Observation | Corroborated | High | P1, S1 |
| `TR96-003` | Holding Walk prevents ordinary movement off a ledge; this is not invulnerability against falls, attacks or a missed jump. | Observation | Corroborated | High | P2, S1 |
| `TR96-004` | Drawn pistols acquire a target; held Action keeps that assigned target even if line of sight is lost, and releasing Action allows a new acquisition. Drawn guns prevent hand-based tasks. | Observation | Direct | High | P1 |
| `TR96-005` | A medi pack is collected into inventory; the small pack restores half health and the large restores full health, while damage can end the attempt. | Observation | Corroborated | High | P1, P2, S1 |
| `TR96-006` | The console beacon permits local saving with a memory card, and the passport supports loading or restarting after death. | Observation | Corroborated | High | P1, P2, S1 |
| `TR96-007` | One Caves switch opens a passage only temporarily; missing the passage permits another approach rather than immediately failing the whole level. | Observation | Limited | Medium | S1 |
| `TR96-008` | Look recentres the view, held directions inspect surrounding geometry, and release returns to the normal view. | Observation | Direct | High | P1 |
| `TR96-009` | No original execution or measured timings are available; pre-release design proposals cannot establish retail behaviour. | Confirmed | Direct | High | R1 |

## Basic data

- Origin: Core Design / Eidos, original *Tomb Raider*, not its later namesakes.
- Analysis target: `PLAT-PLAYSTATION`, original English 1996 Caves; no mechanical equivalence to other releases is asserted. Release audit remains not started.
- Mechanical families: `FAM-007` for support-, gap- and gravity-dependent traversal, and `FAM-010` for live threats and time-limited passage.
- **P1:** [Eidos' original English PlayStation booklet scan](https://tombraiders.net/stella/files/manuals/TR1/Tomb_Raider_PS1.pdf), inspected 2026-09-30, printed pp. 4, 10–19: default controls, ledge hold, weapons, interactions, look, healing and saves. Printed pp. 6–9 are absent in this ten-image scan. It supports neither a complete manual claim nor a measured retail trace.
- **P2:** [Eidos' European PlayStation reprint, SLES-00024](https://manuals.plus/m/7d5d2a5c21a4ba9894a5cf0b5acf55602543e707217896e5627fc9debf5ce115), inspected 2026-09-30, Walking, Attacking and Save sections. The colophon says published under licence in 2000, while the game copyright is 1996. Treated as later printed rule corroboration, not proof of the first disc revision. Jump/Roll labels conflict across its control table and body, so this analysis avoids that table's binding claims.
- **S1:** [Stella's expressly classic Caves written walkthrough](https://www.tombraiders.net/stella/walks/TR1-classic/01caves.html), inspected 2026-09-30. A first-hand original-game account, with dated revision history and separate Remastered link. Supports the bounded route, optional health caches, console save point, timed passage, breakaway floor and exit. No linked video or screenshot was inspected; detailed geometry and exact execution remain secondary evidence.
- **R1:** the [Core Design pre-release design document](https://core-design.com/goodies_tr1_gamedesigndocuments.html) was identified during source selection but was not admitted as authority for a retail transition. No original game execution was available.

## Mechanical decomposition

### Action Genes

- `ACT-008`: direct facing-relative movement, standing/running/directional jump, sidestep and reversing roll. The player aligns the body rather than selecting an automatically computed destination.
- `ACT-049`: activate a reachable lever to change its linked door state; timing is separately resolved by `SYS-1186`.
- `ACT-089`: take a reachable health pack into the discrete inventory, not collect it merely by passing through its position.
- `ACT-131`: use one retained medi pack for an immediate bounded healing effect and spend that pack.
- `ACT-161`: request pistol fire against the current reachable hostile while directly controlling Lara. Target persistence is a system response, not another manual target-selection gene.
- `ACT-341`: commit the local save-beacon interaction. `CON-621` supplies fixture/memory-card eligibility, and `TIM-007` supplies restoreable earlier state.
- `ACT-595`: deliberately draw or holster the currently selected weapon without selecting another inventory weapon. Holstering releases hands for interaction.
- `ACT-596`: hold Action to catch a reachable ledge, continue hanging, shimmy/pull up, or release to fall. No grip-stamina drain is established.
- `ACT-597`: request behind-body recentering or direct a temporary look around, then release it. This changes inspected information, not collision geometry or visibility-dependent world rules.

### System Behaviour Genes

- Reuse `SYS-036` for live jumping, falling, slope and support contact; no exact physics coefficient is inferred.
- Reuse `SYS-057` only for animals activated into pursuit by Lara's approach; their exact awareness/memory policy is not known. `SYS-215` resolves the ensuing live range/contact combat.
- Reuse `SYS-578` for damage and immediate pack recovery on one health pool. Dart and fall injury belong here, not to a second health stack.
- Reuse `SYS-369` for restarting the authored entry or restoring a retained local save after failure; no modern auto-checkpoint is inferred.
- Reuse `SYS-1049` for the authored breakaway tiles changing support and admitting the lower continuation; this is not universal terrain destruction.
- `SYS-1185`: acquire an eligible hostile when drawn guns can aim; keep the assigned identity while Action remains held even after a lost lock, fire again when alignment permits, and reconsider on release. Lock, assigned target and shot eligibility are not identical states.
- `SYS-1186`: a triggered linked passage opens, remains available for a finite live interval and recloses on expiry. The room remains playable; no level-wide deadline or exact duration is asserted.

### Constraint Genes

- `CON-621`: saving requires the eligible world beacon and a usable memory card; the beacon is not an unrestricted menu save. No health refill at the beacon is claimed.
- `CON-727`: held guarded walking stops at an unsupported edge. Releasing Walk or jumping removes that particular safeguard; it cannot certify a jump or prevent hostile damage.
- `CON-728`: a hand-requiring pickup, switch, vault or grip is unavailable while pistols remain drawn. Holstering changes this predicate without clearing the route or damaging a hostile.

### Information, Objective and Time Genes

- `INF-436`: the following/selected look view exposes nearby terrain and hostiles; weapon pose indicates acquisition, and health/compass/inventory expose local condition and supplies. The full cave, offscreen future threats, exact trap schedule and jump frame windows are not shown by this disclosure.
- `OBJ-026`: reach the traversable Caves exit after opening its final doors. Enemy extermination and all secrets are not required.
- `TIM-003`: body, hostiles, hazards and a triggered door continue in real time during ordinary decisions; an explicit pause is a control parameter, not a claim of compulsory unpaused play.
- `TIM-007`: a retained beacon state can be loaded and continued differently. A restart-only history or PC save-anywhere is not inferred.

## Reproducible transitions

| Before | Action/event | Bounded resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Lara approaches an unsupported edge | Hold Walk and move forward | Ordinary walking stops at the edge | Guarded movement differs from a guaranteed jump | `TR96-003` |
| A jump reaches a compatible ledge with empty hands | Hold Action, then move sideways or up | Lara hangs, shimmies or pulls up; releasing permits a fall | Attachment is deliberately sustained, not automatically stamina-priced | `TR96-002`, `TR96-004` |
| Guns are drawn beside a lever | Holster, face it, use Action | The hand task becomes eligible and the linked door changes | Weapon posture gates another class of action | `TR96-004` |
| A hostile is acquired by drawn pistols | Hold fire; then lose line of sight | Assigned identity persists even though shots need usable alignment; release allows another selection | A retained target is not a guaranteed hit | `TR96-004` |
| A small pack is carried and health is damaged | Use the pack | The pack is spent for its half-health restoration | Recovery is a supply decision, not passive regeneration | `TR96-005` |
| A console beacon is reachable and memory card usable | Accept its save, later load | Earlier local progress becomes the restored branch | Save point is optional; save-anywhere does not follow | `TR96-006` |
| The temporary passage is shut | Pull its switch and cross the platforms | Door opens for an interval, then closes if traversal is late | Local timed access, not a fatal global countdown | `TR96-007` |
| Lara reaches the authored breakaway floor | Step onto its tiles | Support gives way and Lara drops to a lower continuation | A changed route need not itself be fatal | `TR96-001` |
| Final switch has opened the exit | Descend and cross the final doors | Caves ends at statistics | Arrival, not secret collection or all kills, closes the packet | `TR96-001` |

These are source-derived falsifiable tests, not executed measurements. A lawful original-disc run would need to check each predicate and record regional controls and timings before upgrading limited route claims.

## Strategic and experiential structure

Align before a jump, trade the slower protected walk for reduced edge risk, and decide when a weapon should be ready rather than occupying needed hands. A timed passage makes hesitation costly, while a health cache can justify an optional detour. A save beacon changes retained failure cost, not the physical jump. These bounded tradeoffs are interpretations of `TR96-001`–`TR96-008`, not proof of an optimal sequence.

## Replay and variation

Caves is authored, not procedurally generated. Route, optional caches, health expenditure, target acquisition and save timing can vary. No random seed, deterministic enemy trace or shortest-time route was measured.

## Adjacent systems and history

The existing 2013 Tomb Raider packet is a different product/version and does not supply this game's rules. Stamina-priced arbitrary-surface grip (`ACT-362`) and projection-authoritative camera rotation (`ACT-095`) were rejected as substitutes for held ledges and ordinary local look. The original manual's missing pages and the later reprint's conflicting table are explicit evidence limits, not concealed regional equivalence.

## Normalised genome

| Type | Active gene IDs | Parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-049`, `ACT-089`, `ACT-131`, `ACT-161`, `ACT-341`, `ACT-595`–`ACT-597` | local movement, jump, reach, supply, posture, hold, look |
| System Behaviour | `SYS-036`, `SYS-057`, `SYS-215`, `SYS-369`, `SYS-578`, `SYS-1049`, `SYS-1185`, `SYS-1186` | support, pursuit, damage, restart, lock, passage interval |
| Constraint | `CON-621`, `CON-727`, `CON-728` | beacon/card, guarded edge, free hands |
| Information | `INF-436` | current camera, health, supplies |
| Objective | `OBJ-026` | opened level exit |
| Time | `TIM-003`, `TIM-007` | live play and retained save branch |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `450` (`GAME-0001`–`GAME-0450`).
- Exact genome matches: none.
- Tied near matches: `GAME-0348` — Resident Evil: Director’s Cut (`11 / 34 = 0.323529`).
- Supported combination subsets: none.
- Scan date: 2026-09-30.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0348` Resident Evil: Director’s Cut | `ACT-008`, `ACT-161`, `ACT-341`, `SYS-057`, `SYS-215`, `SYS-369`, `SYS-578`, `CON-621`, `OBJ-026`, `TIM-003`, `TIM-007` | Both couple direct movement, live hostile combat, health, a permitted save fixture and retained-state recovery to reaching a local destination. Resident Evil's retained key, compatible equipment and consumed Ink Ribbon structure authored mansion gates; Caves instead uses manually held ledges, guarded walking, free hands, automatic persistent pistol targeting and a locally expiring door. Shared save eligibility does not imply the same saving resource or fixture. | Near 0.323529; see Corpus comparison. |

## Taxonomy impact

`TAXONOMY_CHANGE_188` admits eight bounded genes without changing earlier signatures or verified combination definitions.

## Negative results

- No swimming/oxygen, key receptor, moving block, finite pistol ammunition, modern climb stamina or automatic checkpoint is inherited merely because another Tomb Raider edition has it.
- The pre-release design document is not retail proof; the reprint is not an original-disc execution. Exact local timings remain unverified.

## Delta summary

## New facts

- [Observation | Corroborated | High] Manual ledges and free-hand interaction distinguish traversal from weapon-ready combat.
- [Observation | Limited | Medium] Caves couples that movement to a locally expiring door and authored support failure.

## New genes

- [Observation | Corroborated | Medium] Eight genes isolate weapon posture, manual ledge attachment, local look, held-target identity, expiring passage, guarded walking, free-hand eligibility and bounded state disclosure.

## New combinations

- [Observation | Limited | Medium] No new combination is proposed; existing proper subsets are scanned deterministically.

## Taxonomy changes

- [Observation | Corroborated | Medium] `TAXONOMY_CHANGE_188`; no earlier signature changes.

## New questions

- Does an original-disc trace corroborate each limited Caves route predicate and distinguish the manual's target assignment from actual shot eligibility?

## Next recommended game

- [Hypothesis | Limited | Medium] `GAME-0452` *Dr. Mario* for original NES, as recorded in selection 034.
- Optimisation criterion: alternate live spatial traversal with a paired-capsule clearing loop.
- Expected information gain: test whether virus removal and detached halves fit existing falling/clearing boundaries.
- Backlog impact: eight approved subjects remain; none is implicitly published.

## Why this game

- [Hypothesis | Limited | Medium] A recognisable original PlayStation game adds evidence about deliberate attachment and posture-gated actions without flattening a whole adventure into one product union.
