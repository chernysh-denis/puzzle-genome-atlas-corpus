---
game_id: GAME-0472
slug: sonic-adventure
game_title: Sonic Adventure
analysis_status: reviewed
reviewed: 2026-10-02
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-295
    - ACT-610
    - ACT-623
    - ACT-624
  system:
    - SYS-036
    - SYS-037
    - SYS-045
    - SYS-215
    - SYS-911
    - SYS-933
    - SYS-935
    - SYS-948
    - SYS-1056
    - SYS-1231
    - SYS-1232
  constraint: []
  information:
    - INF-448
  objective:
    - OBJ-164
  time:
    - TIM-003
---

# Game: Sonic Adventure — Sonic's first Emerald Coast route

Use the [canonical genome vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Sonic, Tails, rings, an orca, numbered panels and the Dreamcast controller are carrier parameters, not gene names.

## Analysis scope

- Version / ruleset: original English Dreamcast *Sonic Adventure*, Sonic's first story visit to the Emerald Coast Action Stage at level C. SEGA's official history dates the original Dreamcast title to 1998; the inspected manual is the original North American English release. Exact disc revision and cross-region parity were not measured. This is not *Sonic Adventure DX*, a trial replay or a later sequel.
- Structured analysis target: `PLAT-DREAMCAST` in [`knowledge/platforms/games.json`](../../platforms/games.json).
- Entry: immediately after the scripted Station Square approach and Tails's plane crash, at Sonic's first controllable Emerald Coast stage position with his current finite life stock. The earlier Chaos 0 fight and city navigation are not replayed in this packet.
- Primary decision loop: read the following camera's local 3D route, rings, obstacles and life/time display; steer and brake Sonic through the beach and bridge, choose a jump, spin or charged dash, and use an airborne homing command when a nearby eligible enemy is present. A missing eligible target turns that same command into a forward Jump Dash. Recover route height using authored springs, checkpoints and the later numbered jump-panel chain while preserving at least one ring against ordinary hostile hits.
- Positive terminal: reach the stage end and rescue the crash-landed Tails, completing this first Action Stage and returning to the adventure story with a cleared-stage result. The subsequent hotel conversation, Chaos Emerald handoff and next stage are outside the boundary. The original manual says Sonic normally opens an end capsule but explicitly allows another goal object; the contemporary Dreamcast route identifies this specific first-stage goal as Tails, so this record does **not** invent a required capsule hit here.
- Failure and recovery: a compatible enemy hit with no rings costs one life, whereas a hit with rings empties the reserve and permits a surviving attempt; a fall off the course can cost a life even with rings. With lives remaining, Sonic returns at the last activated point marker with its stored stage time. After the final life is lost, Game Over/Continue begins the stage anew rather than retaining the mid-stage marker. Exact recovery-ring cap, damage-grace duration and fall hitboxes were not measured.
- Included: direct analogue 3D movement, jumping and braking; jump-spin and charged Spin Dash; conditional Homing Attack/Jump Dash; optional trigger-controlled camera pan; beach, bridge, loop and waterfall route; ordinary robot enemies; rings, ring loss and recollection; 100-ring life award if reached; fixed springs; local point markers; numbered panel sequence; real-time stage display; Tails rescue. The orca bridge chase is an authored route hazard, not a controllable enemy to defeat.
- Excluded: the Station Square hub, Chaos 0, later Action Stages, alternate playable characters and their different Emerald Coast goals, A/B time or ring emblem challenges, Chao Garden, mini-games, Light Speed Shoes and Light Speed Dash, Ancient Light, later upgrades, DX, ports, modern wrappers, glitches and speedrun-only shortcuts.
- Reproducibility: a source-bounded successful route stays on the first beach/bridge path, survives the orca bridge, crosses the waterfall section, jumps through the five numbered panels and reaches Tails. Exact ring total, enemy contacts, chosen shortcuts, elapsed time and disc-revision-specific behaviour are open parameters. No direct Dreamcast play, capture or executable inspection is claimed.
- Direct-play status: no Dreamcast disc, console, executable, controller trace, screenshot, gameplay video or audio was inspected. The original manual and written routes support a bounded reconstruction, not a claimed playthrough; exact input windows, enemy geometry and ring-scatter cap remain unmeasured. The illustration is original, not game capture.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `SA-001` | Original Dreamcast Sonic story first enters Emerald Coast to reach and rescue Tails | Observation | Corroborated | High | P1, S1 |
| `SA-002` | Analogue pressure controls walking/running, reverse input brakes, and triggers pan the following camera where allowed | Confirmed | Direct | High | P1 |
| `SA-003` | Sonic may jump-spin or hold and release a steered Spin Dash before later upgrades | Confirmed | Direct | High | P1 |
| `SA-004` | A second jump command homes on a nearby eligible enemy; with no such enemy it instead produces a Jump Dash | Confirmed | Direct | High | P1 |
| `SA-005` | Rings buffer ordinary hits, a zero-ring hit is lethal, and course falls can cost a life despite rings | Confirmed | Direct | High | P1 |
| `SA-006` | Point markers retain position and stage time for a later finite-life restart, but Game Over/Continue restarts the stage | Confirmed | Direct | High | P1 |
| `SA-007` | Sonic's route crosses a beach/bridge, an orca-chased span, a waterfall section and five numbered jump panels | Observation | Corroborated | Medium | S1, S2 |
| `SA-008` | The numbered panels require a jump on each reached panel to continue the authored launch chain | Observation | Corroborated | Medium | S1, S2 |
| `SA-009` | Emerald Coast first-visit success is reaching Tails, not satisfying a later time/ring medal condition | Observation | Corroborated | High | P1, S1 |
| `SA-010` | Dropped rings may be recollected after an ordinary hit; exact emitted count is not established here | Observation | Limited | Medium | P1, S3 |

## Basic data

- Release / origin: Sonic Team / SEGA, original Japanese Dreamcast release in 1998; this bounded first-stage reconstruction uses the original English Dreamcast manual, not a claim of directly inspecting an English disc.
- Platform or physical form: one-player Dreamcast disc and analogue controller, scoped to Sonic's first Emerald Coast Action Stage.
- Mechanical families: `FAM-007` physics and object manipulation; `FAM-010` real-time system pressure. Family membership is causal, not a genre tag.
- **P1**: [original North American Dreamcast instruction manual](https://www.digitpress.com/library/manuals/dreamcast/sonic_adventure.pdf), printed pp. 2–11 and 18–19: controller, Action Stage structure, rings, point markers, finite lives, Sonic's movement and ability rules (checked 2026-10-02).
- **P2**: [SEGA's official Sonic 20th-anniversary history](https://sonic.sega.jp/20th/history/), 1998 Dreamcast release identity and 3D-action positioning, not stage-specific mechanics (checked 2026-10-02).
- **S1**: [CKohler's contemporary Dreamcast guide](https://gamefaqs.gamespot.com/dreamcast/198694-sonic-adventure/faqs/2654), Sonic story §4.1 and Emerald Coast §5.1, including the Tails goal, beach/bridge, waterfall and numbered panels (checked 2026-10-02).
- **S2**: [StrategyWiki's Sonic Emerald Coast route](https://strategywiki.org/wiki/Sonic_Adventure/Sonic/Emerald_Coast), corroborating the first-stage orca and panel sequence; the page may incorporate later-version presentation and is not used to override the Dreamcast manual (checked 2026-10-02).
- **S3**: [Sonic Adventure mechanics summary](https://www.theghz.com/sonic/adventure/adventure.html), a secondary description of recoverable ring loss, used only for that limited transition (checked 2026-10-02).
- Claim IDs: `SA-001`–`SA-010`. No direct play or audiovisual inspection.

## Mechanical decomposition

### Action Genes

- Reuse `ACT-008`: steer, brake and jump directly through a three-dimensional beach-and-bridge route. The extra depth axis is a carrier parameter, not a new navigation gene (`SA-002`).
- Reuse `ACT-295`: Sonic commits an ordinary jump-spin or a charged, steered Spin Dash as a character-owned attack pose; charge amount and release direction are parameters (`SA-003`).
- Reuse `ACT-610`: pan the following camera around Sonic where the stage permits it before choosing a partially occluded route (`SA-002`).
- Add `ACT-623`: while airborne, request Sonic's conditional homing attack or no-target Jump Dash; this is a new command boundary because the same second-jump input has target-dependent destinations (`SA-004`).
- Add `ACT-624`: jump from the currently reached numbered launch panel to request the next link; merely touching it does not perform the entire five-panel crossing (`SA-008`).

### System Behaviour Genes

- Reuse `SYS-036`: integrate live movement, gravity, collision and ring trajectories; do not claim the Genesis-specific slope coefficients (`SA-002`, `SA-005`).
- Reuse `SYS-037`: ring contact adds to the visible reserve (`SA-005`).
- Reuse `SYS-045`: ordinary enemies continue local motion without a command for each step (`SA-004`).
- Reuse `SYS-215`: resolve Sonic's spin or homing contact with eligible robot enemies while stage time continues (`SA-003`, `SA-004`).
- Reuse `SYS-911`: a lethal hit or course fall consumes one of the finite lives and restores Sonic at an eligible return point (`SA-005`, `SA-006`).
- Reuse `SYS-933`: a point marker replaces the current intra-stage return anchor and records the stage time (`SA-006`).
- Reuse `SYS-935`: reaching the manual's 100-ring milestone adds one life without ending the stage (`SA-005`).
- Reuse `SYS-948`: ordinary compatible damage empties a positive ring reserve into recoverable nearby rings; no Genesis-specific 32-ring cap is asserted for this Dreamcast route (`SA-005`, `SA-010`).
- Reuse `SYS-1056`: eligible spring contact applies a fixed launch, after which Sonic remains steerable (`SA-007`).
- Add `SYS-1231`: the airborne command selects a nearby eligible enemy for directed contact, or uses a forward dash when none is eligible; the homing outcome is not an unconditional teleport (`SA-004`).
- Add `SYS-1232`: a valid jump from a numbered panel launches Sonic to the next authored panel, making each arrival a new decision point until the chain completes (`SA-007`, `SA-008`).
- Resolution order: read camera and local target; steering/jump/spin or camera input changes the immediate state; physical movement advances; eligible spring or panel launch updates trajectory; rings/hostile contact settle; ring loss or lethal fall invokes finite-life return; only stage-end reach settles Tails's rescue.

### Constraint Genes

- No separate fixed time-limit gene: elapsed time is displayed, but this first-visit C goal is not a countdown challenge. Homing proximity and panel eligibility live within the corresponding resolution boundaries rather than an independent global restriction.

### Information Genes

- Add `INF-448`: Sonic's following 3D view and stage display expose the locally visible route, nearby target, elapsed time, rings and remaining lives, but do not reveal all later turns or guarantee a homing target (`SA-002`, `SA-004`, `SA-005`).

### Objective Genes

- Reuse `OBJ-164`: satisfy this region's exit event by reaching Tails at the end of Emerald Coast and return to the story with the cleared-stage result. A later emblem grade is not required (`SA-001`, `SA-009`).

### Time Genes

- Reuse `TIM-003`: movement, enemies, contact and elapsed stage time continue under direct real-time control; a visible stopwatch is not a fixed deadline (`SA-002`–`SA-005`).

## Reproducible transitions

| Before | Action | Bounded resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Beach route, Sonic grounded and facing a visible gap | Steer, accelerate and jump | Sonic carries motion over the gap or falls if the route is missed | directly steered 3D course and lethal boundary | `SA-002`, `SA-005` |
| Sonic is airborne near an eligible robot | Press jump again | Sonic redirects toward that target; accepted contact can defeat it | homing selection and live combat are distinct from the command | `SA-004` |
| Sonic is airborne with no eligible nearby target | Press the same button | Sonic performs a forward Jump Dash instead of a guaranteed enemy hit | conditional fallback, not an omniscient attack | `SA-004` |
| Sonic has a positive ring reserve | Suffer an ordinary compatible hit | The reserve empties, nearby dropped rings can be recovered and the attempt survives | ring-buffer recovery, not life consumption | `SA-005`, `SA-010` |
| Sonic has zero rings or falls off the course | Suffer the hit or fall | One life is spent; while lives remain he returns at the active point marker and its stored time | fall bypasses ring protection; finite-life checkpoint | `SA-005`, `SA-006` |
| Sonic reaches a numbered panel | Jump from that panel, then from each next numbered arrival | Each valid input carries Sonic to the next authored panel; stopping early leaves the chain incomplete | player-timed launch chain | `SA-007`, `SA-008` |
| Sonic reaches the end after crossing the route | Contact the first-visit goal beside Tails | Emerald Coast clears, the rescue is acknowledged and story progression becomes eligible | stage exit, not a later medal threshold | `SA-001`, `SA-009` |

## Strategic and experiential structure

- Local decision: align Sonic with the visible geometry, preserve enough momentum for a bridge or loop, choose an airborne attack only when its target is eligible, and collect at least one ring before a risky passage.
- Medium-term planning: retain a safe point marker, recover after an ordinary hit, cross the orca-chased bridge and prepare for the numbered panel sequence rather than assuming one continuous automatic ride.
- Long-term structure: complete this first story stage and meet Tails; later upgrades, alternate characters and emblem challenges do not retroactively alter the packet.
- Common heuristic: follow the camera's route cue, use springs and visible rings to maintain a safe line, and press jump again on each numbered panel.
- Failure attribution: zero-ring hostile damage and falling both spend a life, but the former can be prevented by rings while the latter cannot.
- Trust boundary: stage geometry and target semantics come from the original manual and corroborated written routes, not a claimed original-disc playthrough.

## Replay and variation

The Emerald Coast route is authored. Player steering, ring collection, enemy contacts, optional shortcuts and timing vary. The orca chase and numbered panels do not imply procedural generation. Replaying for A/B emblem conditions would change the objective and requires another scope.

## Adjacent systems and history

`GAME-0333` original Genesis *Sonic the Hedgehog* shares rings, finite lives, point markers, direct steering and live collision. The Genesis packet is a fixed side-view act with a ten-minute timeout and signpost/score closeout. This Dreamcast packet adds a following 3D camera, target-conditional airborne homing and a player-triggered numbered launch chain, and its first-visit endpoint is Tails. It does not inherit the Genesis-specific `SYS-947` slope coefficients, `CON-068` deadline or `INF-192` side-view lookahead.

## Normalised genome

| Type | Active gene IDs | Key parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-295`, `ACT-610`, `ACT-623`, `ACT-624` | 3D steering, spin, camera, homing command, panels |
| System Behaviour | `SYS-036`, `SYS-037`, `SYS-045`, `SYS-215`, `SYS-911`, `SYS-933`, `SYS-935`, `SYS-948`, `SYS-1056`, `SYS-1231`, `SYS-1232` | live motion, rings, life return, launch, target selection |
| Constraint | none | no first-visit fixed deadline |
| Information | `INF-448` | local view, rings, time, lives |
| Objective | `OBJ-164` | reach and rescue Tails |
| Time | `TIM-003` | real-time stage |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `471` (`GAME-0001`–`GAME-0471`).
- Exact genome matches: none.
- Tied near matches: `GAME-0333` — Sonic the Hedgehog (`12 / 27 = 0.444444`).
- Supported combination subsets: none.
- Scan date: 2026-10-02.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0333` *Sonic the Hedgehog* | Direct steering and spin (`ACT-008`, `ACT-295`); live body, ring collection, enemies and combat (`SYS-036`, `SYS-037`, `SYS-045`, `SYS-215`); finite-life return, point marker, ring milestone and scattered hit loss (`SYS-911`, `SYS-933`, `SYS-935`, `SYS-948`); exit handoff and live time (`OBJ-164`, `TIM-003`). | The Genesis Act 1 has side-view lookahead, source-proven slope physics, a ten-minute failure limit and signpost closeout. Emerald Coast instead has a following 3D camera, conditional airborne homing, repeated numbered-panel launches and Tails as the first-visit goal. | Sole tied-near maximum, `0.444444`; neither exact nor a verified-combination match. |

## Taxonomy impact

`TAXONOMY_CHANGE_209` isolates conditional airborne attack, numbered-panel input and launch resolution, and 3D route feedback. Earlier signatures and verified combinations are unchanged.

## Negative results

- `SYS-947` needs source-proven surface-angle coefficients and steep-surface detachment. The Dreamcast manual proves analogue speed/braking and 3D loops, not identical Genesis internals.
- `INF-192` is a side-scrolling viewport. This stage uses a following 3D camera and optional manual pan.
- `CON-068` requires a fixed failure deadline. The displayed elapsed time is not such a limit for the first C-stage rescue.
- `SYS-653` is a target-directed automatic approach but does not cover the same airborne button falling back to Jump Dash when no enemy is eligible.
- Later Light Speed Dash is upgrade-gated and unavailable for the first Emerald Coast visit.

## Delta summary

## New facts

- [Confirmed | Direct | High] The original Dreamcast manual separates ordinary Spin Dash from conditional airborne Homing Attack/Jump Dash and explains ring, life and point-marker recovery (`SA-002`–`SA-006`).
- [Observation | Corroborated | Medium] The first Sonic Emerald Coast visit crosses beach, bridge, waterfall and numbered-panel segments to rescue Tails (`SA-001`, `SA-007`–`SA-009`).

## New genes

- [Observation | Corroborated | Medium] Five new Active boundaries: `ACT-623`, `ACT-624`, `SYS-1231`, `SYS-1232`, `INF-448`.

## New combinations

- [Observation | Limited | Medium] No new verified combination proposed.

## Taxonomy changes

- [Observation | Corroborated | Medium] `TAXONOMY_CHANGE_209`; no earlier signature changed.

## New questions

- What exact target radius and precedence does a pinned original Dreamcast disc use for the first-stage homing command?
- How many dropped rings can be recovered after a hit in this original disc revision?
- What is the exact stage-end collision object for Sonic's first Emerald Coast visit, before the Tails rescue cutscene?

## Next recommended game

- [Hypothesis | Limited | Medium] `GAME-0473` *Eternal Darkness: Sanity's Requiem*, original Nintendo GameCube.
- Optimisation criterion: alternate Dreamcast 3D traversal with a different platform and psychological information-state rules while preserving the approved cross-platform order.
- Backlog impact: do not start until this unit's gates, one local commit and the Goal stop window.

## Why this game

- [Hypothesis | Limited | Medium] The first Emerald Coast route tests whether the Genesis Sonic signature transfers to a 3D following-camera, conditional-homing, panel-chain stage without mistaking shared rings for identical decision structure.
