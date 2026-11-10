---
game_id: GAME-0462
slug: metal-slug-3
game_title: Metal Slug 3
analysis_status: reviewed
reviewed: 2026-10-01
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-161
    - ACT-201
    - ACT-202
    - ACT-613
    - ACT-614
  system:
    - SYS-045
    - SYS-215
    - SYS-320
    - SYS-910
    - SYS-911
    - SYS-1212
  constraint:
    - CON-578
  information:
    - INF-192
    - INF-235
    - INF-347
  objective:
    - OBJ-080
  time:
    - TIM-003
---

# Game: Metal Slug 3

The genome uses the canonical [vocabulary and signature](../../../docs/ARCHITECTURE.md#canonical-vocabulary). The boat, Metal Slug tank, Huge Hermit and particular pickup positions are carrier parameters, not gene names.

## Analysis scope

- Version / ruleset: original 2000 Neo Geo MVS arcade cartridge, one-player Mission 1. The exact cabinet BIOS, difficulty setting and software revision were not inspected. SNK's catalogue dates the Japanese MVS cartridge to 2000-03-23; the anniversary history instead says May 2000, so the precise date is not used to infer rules.
- Structured analysis target: `PLAT-NEO-GEO-MVS`, original MVS Mission 1 as documented by SNK's contemporary operations, route and item pages; see `GAME-0462` in `knowledge/platforms/games.json`.
- Primary decision loop: steer the infantry body through the visible side-scrolling slice, crouch or jump around fire and attack nearby hostiles; at the authored crossroads enter the boat rather than the ship; fight while the boat carries the body downstream; take an available special gun and manage its finite ammunition against the unlimited starting handgun; board the available Metal Slug tank before the Huge Hermit encounter, aim its mounted fire and cannon, protect its finite damage buffer or spend it in a deliberate self-destruct assault, defeat the boss and reach the Mission 2 transition.
- Entry: first ordinary player control at Mission 1 start on a fresh one-player credit, before choosing a crossroads. The packet prescribes the visible boat entrance at the documented fork. It does not claim the same item, enemy or tank timing for another route.
- Positive terminal: defeat the mandatory first-mission guardian and let the stage clear advance to the Mission 2 presentation; subsequent Mission 2 play is excluded. The guardian name and boat-route tank availability are corroborated by contemporary written routes, not by a direct MVS run.
- Negative terminal: exhausting the available life stock brings Game Over. One infantry hit or a timer reaching zero spends one life and permits a return only while lives remain. A vehicle absorbs up to the documented three hits; failure to escape its destruction can also cost a life. Continue after Game Over is excluded.
- Included: 8-way lever movement/aim, jumps, crouch, automatic close-range knife, infantry shot and finite grenade, local enemies and shots, physical branch entrance, scripted downstream boat movement, contact-collected special gun, finite compatible ammunition, tank boarding/control/fire/exit, its damage buffer and delayed explosion risk, optional A+B Metal Slug Attack, visible time/lives/ammunition, first-mission boss and next-stage handoff.
- Excluded: two-player authority, other Mission 1 branch play, hidden crossroads, later missions, whole-campaign aliens or transformations, food/Jumbo form, prisoner and score farming, exact weapon damage, boss health, boat velocity, fixed pickup coordinates, precise timer values, operator difficulty/credit configuration, Continue, AES/Neo Geo home, PlayStation, PC, mobile and ACA ports or emulation.
- Reproducible parameterisation: begin an original MVS one-player Mission 1 with ordinary controls; at the documented fork enter the boat. Treat special-gun and grenade pickup counts as conditional rather than guaranteed. On reaching the tank before Huge Hermit, board it if available; use ordinary fire and optionally the A+B assault, noting that this sacrifices the vehicle. Stop on the first Mission 2 presentation or Game Over. The route and tank sequence are source-bounded, not a claimed observed successful playthrough.
- Potential scoped modules: the ship and underwater first-mission paths; first mission with another character or a measured cabinet; two-player co-op, later branching missions and an original-MVS-to-port comparison.
- Direct-play status: not conducted. No MVS cartridge, PCB, cabinet, ROM, input trace, save, screenshot, video or audio was obtained or inspected. Original SNK text describes controls, weapons, crossroads and general stage completion; contemporary player-written routes locate the first boss and boat-path tank. Exact timings, hit values and one complete first-mission outcome remain unmeasured.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| MS3-001 | SNK's catalogue identifies Metal Slug 3 as a 2000 MVS cartridge; the exact release month conflicts with SNK's anniversary history | Observation | Conflicting | Medium | P1, P2 |
| MS3-002 | The 8-way lever moves, aims and crouches; A shoots or automatically knives nearby infantry, B jumps/boards, Down+B exits, C throws a finite grenade or fires an occupied vehicle cannon | Observation | Direct | High | P3 |
| MS3-003 | A+B deliberately drives an occupied vehicle into a damaging self-destruct assault and loses that vehicle | Observation | Direct | High | P3 |
| MS3-004 | Infantry takes one fatal hit, starts with three lives; an occupied vehicle can withstand three hits, but a delayed escape after its destruction may cost a life | Observation | Direct | High | P3 |
| MS3-005 | Reaching zero on the visible timer costs one life; the stage is cleared by defeating its final boss, not merely reaching a fork | Observation | Direct | High | P3 |
| MS3-006 | Each stage has physical route crossroads; at the documented example the player can enter a ship or dive into a boat, which then moves downstream into combat | Observation | Direct | High | P4, P2 |
| MS3-007 | The starting handgun has unlimited ammunition, while picked-up special guns and thrown items have finite ammunition; compatible supplies replenish them | Observation | Direct | High | P5, P3 |
| MS3-008 | Written Mission 1 routes identify Huge Hermit as the first guardian and a Metal Slug tank on the boat-side approach | Observation | Corroborated | Medium | S1, S2 |
| MS3-009 | An original cabinet or recorded run was not inspected; route-specific item timing and combat outcomes are not measured | Observation | Direct | High | R1 |

## Basic data

- Release / origin: SNK's Neo Geo MVS arcade release. The official catalogue lists Japanese MVS 2000-03-23 and home ROM cartridge 2000-06-01; SNK's anniversary article instead calls the MVS release May 2000. This conflict does not alter the selected ruleset.
- Platform or physical form: original Neo Geo MVS arcade cartridge in one-player mode. The analysis does not infer operator defaults or all later releases.
- Puzzle family: tactical forecast and counterplay (`FAM-009`) and real-time system pressure (`FAM-010`).
- Primary publisher sources, accessed 2026-10-01:
  - **[P1]** [SNK Neo Geo Museum title catalogue](https://neogeomuseum.snk-corp.co.jp/english/catalogue/index.php), MVS and home-release identity/dates.
  - **[P2]** [SNK Metal Slug 30th anniversary history](https://www.snk-corp.co.jp/us/anniversary/metalslug30th/history/), route choices and vehicle expansion; its MVS month conflicts with the catalogue.
  - **[P3]** [archived original SNK Japanese Metal Slug 3 operations page](https://neogeo.freeplaytech.com/metal_slug/metal_slug3/operation/operation.htm), movement, shot, vehicle commands, hit/life/timer and stage conditions. The host mirrors the historical SNK page, not a current publisher endpoint.
  - **[P4]** [archived original SNK English route page](https://neogeo.freeplaytech.com/metal_slug_en/metal_slug3/elements/elements.htm), physical crossroads, ship versus boat and downstream combat.
  - **[P5]** [archived original SNK English item page](https://neogeo.freeplaytech.com/metal_slug_en/metal_slug3/item/item.htm), unlimited handgun, finite special guns and supplies.
- Corroborating written routes, accessed 2026-10-01: **[S1]** [contemporary Metal Slug 3 boss guide](https://gamefaqs.gamespot.com/ps3/124918-metal-slug-3/faqs/9694); **[S2]** [original-game route documented in the Metal Slug Anthology vehicle guide](https://gamefaqs.gamespot.com/wii/932854-metal-slug-anthology/faqs/49614). These name the boss and boat-side tank but are not proof of original-MVS frame timing or port parity.
- **[R1]** Local source preflight found no licensed cabinet or original binary and no direct-play trace. Artwork is a new illustrative composition, not game footage.
- Claim IDs: `MS3-001`–`MS3-009`.

## Mechanical decomposition

### Action Genes

- `ACT-008`: directly move and jump the infantry body through the visible horizontal route.
- `ACT-161`: aim and fire at a reachable hostile; close-range automatic knife and the occupied tank's guns are tool-specific parameters.
- `ACT-202`: crouch to alter infantry exposure and firing line.
- New `ACT-613`: physically enter one authored crossroads opening, committing its following stage segment. This is not a menu selection of a revealed map node (`ACT-127`).
- `ACT-201`: board and directly steer the later tank, fire from it and choose when to leave; the boat is *not* counted as directly steered.
- New `ACT-614`: press A+B while aboard to send the vehicle forward as an explosive attack, knowingly losing it rather than merely ramming and continuing to drive.
- Parameters: soldier, direction, weapon, local entrance, boat route, tank position and assault timing.
- Claim IDs: `MS3-002`, `MS3-003`, `MS3-006`, `MS3-008`.

### System Behaviour Genes

- `SYS-045`: enemies and hostile shots continue their own local motion.
- `SYS-215`: directly committed attacks and hostile contact resolve live.
- `SYS-910`: a contact-collected typed stage item can change the current infantry gun or replenish a compatible reserve; unlike an inventory-selection action, this is immediate contact effect.
- New `SYS-1212`: after the player enters the boat branch, the boat carries the body downstream while combat continues; the player does not steer the transport.
- `SYS-320`: the directly operated tank resolves movement, shots, an up-to-three-hit vehicle buffer and destruction/escape exposure.
- `SYS-911`: lethal infantry contact, an expired timer or failed vehicle escape spends one finite life and permits respawn only with stock left.
- Resolution order: crossroads contact selects the route; the boat carries the player and live hostiles continue; item contact updates active weapon/reserve; entering the tank changes control authority; incoming damage first affects the tank buffer, while a destroyed tank requires timely exit or may take a life; the boss defeat closes the stage independently of score.
- Claim IDs: `MS3-002`–`MS3-008`.

### Constraint Genes

- `CON-578`: a special gun, grenade or occupied cannon requires its compatible finite ammunition for a shot; the basic handgun has no such expenditure. The sources do not prove an exact clip size or a universal replacement/fallback frame rule.
- Scarce strategic resources: finite lives, grenades, special-gun ammunition, tank damage tolerance and remaining stage time. The timer's zero is a life loss, not `CON-068`'s immediate terminal deadline while more lives remain.
- Claim IDs: `MS3-004`, `MS3-005`, `MS3-007`.

### Information Genes

- `INF-192`: the scrolling side view shows the local fork, hazards and route ahead, not the entire stage map.
- `INF-235`: nearby enemies, shots, pickups and attack effects are visible in the live slice.
- `INF-347`: the stage interface exposes time, lives, score and finite attack resources; vehicle damage feedback remains local.
- Claim IDs: `MS3-002`, `MS3-005`–`MS3-007`.

### Objective Genes

- `OBJ-080`: defeat the mandatory first-mission guardian and cross the stage-clear boundary into the next mission. Entering the boat alone is not a win and clearing the full campaign is outside the packet.
- Claim IDs: `MS3-005`, `MS3-008`.

### Time Genes

- `TIM-003`: movement, enemy fire, boat conveyance, tank combat and stage clock advance during player input.
- Claim IDs: `MS3-002`, `MS3-005`, `MS3-006`.

## Reproducible transitions

| Before | Action | Deterministic resolution or stated branch | What it establishes | Claim ID |
|---|---|---|---|---|
| Infantry reaches a visible crossroads | Enter the boat instead of the ship threshold | This physical entrance commits the downstream boat segment; the unchosen segment is not played | route commitment is not map-node selection | `MS3-006` |
| Body is aboard the moving boat | Aim and fire at a reachable enemy | The boat continues downstream without a steering command while enemies keep attacking | transport motion and combat coexist | `MS3-002`, `MS3-006` |
| Basic handgun is active | Take an available special-gun item | Active combat capability changes to a finite-ammo gun; the handgun itself is unlimited | pickup mutation versus ammunition reserve | `MS3-007` |
| Finite compatible reserve is empty | Request another corresponding shot | The shot is unavailable until a compatible supply is acquired; no exact fallback timing is asserted | ammunition gate | `MS3-007` |
| Tank is available after the boat segment | Board it with the documented input | Direct driving/fire authority moves into the vehicle, which can withstand more than one hostile hit | operated tank is not the passive boat | `MS3-002`, `MS3-004`, `MS3-008` |
| Tank has taken its allowed damage | Escape promptly or delay | A timely exit avoids the subsequent blast; remaining in the destruction interval can cost one infantry life | vehicle loss and body loss are different | `MS3-004` |
| Tank is occupied before a reachable boss phase | Press A+B | It attacks as a self-destructing vehicle and is lost; victory is not assumed unless the guardian is defeated | offensive resource sacrifice | `MS3-003` |
| Infantry body is alive, timer reaches zero | Let clock expire | One life is lost; Game Over follows only if stock is exhausted | timeout is not always whole-run terminal | `MS3-004`, `MS3-005` |
| Huge Hermit is defeated with attempt viable | Continue into stage clear | Mission 1 closes and Mission 2 is presented, ending this analysis | boss gate versus next-mission play | `MS3-005`, `MS3-008` |

## Strategic and experiential structure

- Local decision: choose a safe firing/crouching/jump moment under live hostile pressure; conserve a limited attack for a useful target.
- Medium-term planning: enter a particular physical branch, use the boat's movement without mistaking it for direct driving, and preserve the tank's protective buffer for the guardian.
- Long-term structure: the full title has multiple authored routes and later missions, but this comparison ends after one stage-clear handoff.
- Common heuristics: inspect the next visible entrance before crossing; count finite shots, leave a failing vehicle promptly and do not equate remaining lives with the vehicle's hits.
- Failure attribution: timer, life and attack displays distinguish time loss, exhausted ammunition and body death; exact boss hit values remain unmeasured.
- Player-trust factors: original SNK operations and route pages establish the major rules, but the boat-to-tank/boss placement is corroborated by player-written routes rather than independently executed in this study.
- Claim IDs: `MS3-002`–`MS3-009`.

## Replay and variation

- Selecting another physical crossroads entrance changes the authored stage segment; different item pickups, enemy positions and lives remaining may change the approach to the same first-stage closeout.
- No procedural generation, exact loot probability or random enemy schedule is asserted for this bounded original-MVS packet.
- Replays can test boat versus ship outcomes or risk a tank assault, but only the boat route is admitted here.
- Claim IDs: `MS3-006`–`MS3-009`.

## Adjacent systems and history

- Contra Force shares direct side-view aiming and finite lives but changes commandos and a power-up gauge; Metal Slug 3 instead commits a physical stage branch and uses a scripted boat followed by a directly operated tank.
- Tank 1990 shares a finite vehicle stock and contact bonuses, but its top-down defended-eagle arena does not model infantry/vehicle transfer or a passenger boat route.
- Slay the Spire's `ACT-127` selects a disclosed successor node on a map; this game's crossroads are entered in the running world.
- Claim IDs: `MS3-002`–`MS3-008`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-161`, `ACT-201`, `ACT-202`, `ACT-613`, `ACT-614` | infantry controls, physical boat entrance, tank assault |
| System Behaviour | `SYS-045`, `SYS-215`, `SYS-320`, `SYS-910`, `SYS-911`, `SYS-1212` | boat movement, item type, vehicle damage and lives |
| Constraint | `CON-578` | finite special ammunition and unlimited handgun |
| Information | `INF-192`, `INF-235`, `INF-347` | side view, local threats and stage HUD |
| Objective | `OBJ-080` | first guardian and next-mission threshold |
| Time | `TIM-003` | real-time pressure |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `461` (`GAME-0001`–`GAME-0461`).
- Exact genome matches: none.
- Tied near matches: `GAME-0324` — Contra Force (`10 / 28 = 0.357143`).
- Supported combination subsets: none.
- Scan date: 2026-10-01.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0324` — Contra Force | `ACT-008`, `ACT-161`, `ACT-202`, `SYS-045`, `SYS-215`, `SYS-911`, `INF-192`, `INF-235`, `OBJ-080`, `TIM-003` | Both demand live side-view movement, aimed fire, local hazard reading, finite lives and a first-mission guardian. Contra Force instead changes among four commandos, temporary partner plans and an ordered weapon gauge; Metal Slug 3 physically commits a boat branch, carries the soldier without boat steering, then grants a directly driven or sacrificial tank with finite special ammunition. | Nearest by symmetric Jaccard, `10 / 28 = 0.357143`; no exact match. |

- New genes: `ACT-613`, `ACT-614`, `SYS-1212`.
- Classification result: `New gene`.
- Evidence and reasoning: physically entering a live fork differs from selecting a map node; the boat supplies autonomous branch transport while the tank is driven; the combined attack deliberately consumes that vehicle.

### Preserved research notes

- New genes: `ACT-613`, `ACT-614`, `SYS-1212`.
- Classification result: `New gene`.
- Evidence and reasoning: physically entering a live fork differs from selecting a map node; the boat supplies autonomous branch transport while the tank is driven; the combined attack deliberately consumes that vehicle.

## Taxonomy impact

- Registry changes: three new Active definitions; no earlier game signature or verified combination changes.
- Taxonomy-change record: `TAXONOMY_CHANGE_199`.
- Candidate terms affected: boat passenger versus tank driver; gun pickup mutation versus finite compatible ammunition; timer life loss versus whole-attempt expiry.

## Negative results

- No new combination is admitted from a single carrier.
- The documented timer loss does not satisfy `CON-068`, whose deadline is a terminal failure; the physical boat entrance does not satisfy map-node `ACT-127`.

## Delta summary

## New facts

- [Observation | Direct | High] `MS3-002`–`MS3-007` isolate the original-MVS movement, physical crossroads, boat motion, finite arms, vehicle/life separation and timer rule.

## New genes

- [Observation | Direct | High] `ACT-613`, `ACT-614` and `SYS-1212` isolate physical branch entry, deliberate vehicle sacrifice and autonomous branch transport.

## New combinations

- [Observation | Limited | Medium] No cross-game combination is verified by this single new packet.

## Taxonomy changes

- [Observation | Direct | High] `TAXONOMY_CHANGE_199` adds three boundaries without changing earlier signatures.

## New questions

- Can an instrumented original MVS cabinet pin the boat-route tank placement, boss attack timings and exact ammunition fallback behaviour under a documented operator configuration?

## Next recommended game

- [Hypothesis | Limited | High] `GAME-0463` *Pokémon Gold Version*, original Game Boy Color, follows after full acceptance and the Goal stop window.
- Optimisation criterion: change platform and primary decision loop from live shooter routes to original handheld capture/battle progression.
- Expected information gain: test transferable roster, information and finite-resource genes against a very different turn structure.
- Backlog impact: preserve the approved nine-game cross-platform order.

## Why this game

- [Hypothesis | Limited | High] The physical route fork, transport authority distinction and vehicle-sacrifice action are likely to separate this packet from existing side-view combat signatures.
