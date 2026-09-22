---
game_id: GAME-0344
slug: prince-of-persia-the-sands-of-time
game_title: "Prince of Persia: The Sands of Time"
analysis_status: reviewed
reviewed: 2026-09-21
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-044
    - ACT-161
    - ACT-341
    - ACT-437
  system:
    - SYS-215
    - SYS-398
    - SYS-578
    - SYS-755
  constraint:
    - CON-282
    - CON-351
  information:
    - INF-115
    - INF-119
    - INF-268
  objective:
    - OBJ-201
  time:
    - TIM-003
    - TIM-007
---

# Game: Prince of Persia: The Sands of Time

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). The Prince, Dagger
of Time, Sand Tanks, Power of Revival, Maharajah's Treasure Vaults and every
guard, pool, trap, ledge, column or statue are carrier parameters, not gene
names.

## Analysis scope

- Version / ruleset: the current licensed English Windows Steam application
  `13600`, publisher Ubisoft, using the base single-player rules documented by
  its linked English PC manual. No installed depot or exact executable hash was
  available, so storefront identity and sourced rules are frozen rather than
  presented as a performed current-build parity check.
- Structured analysis target: one fresh unmodified English single-player game
  on `PLAT-WINDOWS-PC`, from the first control after the opening cinematic
  through the first ordinary control after acquiring the Dagger; see
  `GAME-0344` in
  [`knowledge/platforms/games.json`](../../platforms/games.json).
- Primary decision loop: read the current tutorial cue and local geometry;
  commit runs, jumps, wall-runs, wall-jumps, ledge and column transfers;
  optionally strike or block human guards; break required obstructions, drink
  from reachable water after damage and repeat the authored route until the
  Dagger acquisition demonstrates and retains the first rewind power.
- Entry: first ordinary control of the Prince after the opening cinematic's
  letterboxing disappears, before he walks through the curtains into the
  attacked palace.
- Positive terminal: approaching the Dagger on the statue settles the authored
  acquisition cutscene, its falling-rock mishap demonstrates the Power of
  Revival, and ordinary control returns with the Dagger and its first rewind
  capability retained. Stop before committing the first escape jump.
- Negative terminal: empty Life causes Game Over before the Dagger is acquired.
  The manual's prompted saves and menu load remain recovery options, but this
  packet makes no exact checkpoint, relaunch or save-equality claim.
- Included: third-person movement, jump, wall-run, wall-jump, ledge shimmy,
  column climb and transfer; required breakable barricades; optional direct
  sword combat against pre-Sands human guards; held sword block; hard-fall,
  attack and spike-pole damage; water drinking and health restoration; staged
  tutorial text; the first prompted save opportunity as route context only;
  the complete treasure-vault approach; fixed spike-pole avoidance; Dagger
  acquisition; the automatic falling-rock rewind demonstration; retained
  Power of Revival, Sand Tank legality and visible Life/Sand/Time state.
- Excluded: the post-acquisition escape route; opening the Hourglass; every
  Sand Creature; sand retrieval, Sand Clouds, Sand Vortices and visions;
  Delay, Restraint, Haste and later Dagger upgrades; later weapons, puzzles,
  palace areas, Farah coordination and campaign completion; exact save/load
  restoration; optional secrets; other PC packages, original console builds,
  remasters, remake material, compatibility layers, cheats, glitches and mods.
- Reproducible parameterisation: start a fresh English game; take the authored
  palace route through breakable barricades, ledges, wall-runs, columns and the
  first save corridor; enter the Maharajah's Treasure Vaults; traverse the
  water pits, wall-jump shaft, hourglass chamber, moving spike poles, breaking
  ledges, columns and statue; approach the Dagger; stop at first returned
  control after its acquisition and automatic rewind demonstration. Guard
  fights may be bypassed where the written route permits; drinking is needed
  only after damage.
- Potential scoped modules: exact current-depot execution, prompted-save
  persistence, the escape from the vault, first Sand Creature combat and sand
  refill, one later Dagger power, another platform release or the complete
  campaign each require a separate entry, terminal and evidence boundary.
- Direct-play status: not conducted. No installed Steam depot, executable,
  controller or keyboard trace, profile, save, screenshot, video or audio was
  available or analysed. The local control validates a source-bounded route and
  state model, not Ubisoft program code, collision tolerances or build parity.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `POPSOT-001` | Ubisoft's licensed PC product identifies a 2003 action-adventure release, while Steam app `13600` is the selected current English Windows offer | Confirmed | Direct | High | P1, P2 |
| `POPSOT-002` | The first playable state begins when opening-cinematic letterboxing disappears and accepts movement through the curtains | Confirmed | Direct | High | P3 |
| `POPSOT-003` | The opening route teaches running, jumping, wall traversal, ledge and column transfers through staged local prompts | Observation | Corroborated | High | S1, S2 |
| `POPSOT-004` | Required barricades are removed by sword strikes; human guards can be struck, blocked or bypassed at documented route points | Observation | Corroborated | High | P3, S1, S2 |
| `POPSOT-005` | Falls, attacks and traps reduce one Life pool; reachable water restores missing Life; empty Life is Game Over | Confirmed | Corroborated | High | P3, S1, S2 |
| `POPSOT-006` | The treasure-vault approach requires authored wall-runs, wall-jumps, ledges, moving spike poles, columns and statue climbing | Observation | Corroborated | High | S1, S2 |
| `POPSOT-007` | Approaching the Dagger triggers its acquisition and a falling-rock sequence in which the first Power of Revival rewinds the mishap before control returns | Observation | Corroborated | High | P3, S3 |
| `POPSOT-008` | Holding Rewind restores up to the retained history horizon and releasing resumes from the selected earlier state | Confirmed | Direct | High | P3 |
| `POPSOT-009` | Each accepted rewind consumes one Sand Tank and requires both sand and available Time Circle history | Confirmed | Direct | High | P3 |
| `POPSOT-010` | The HUD exposes Life, Sand Tanks and the Time Circle relevant to damage and rewind legality | Confirmed | Direct | High | P3 |
| `POPSOT-011` | The bounded route stops before post-Dagger escape, Sand Creature combat or any sand replenishment | Confirmed | Corroborated | High | S1, S2, S3 |
| `POPSOT-012` | The repository control proves the ordered route gates, optional combat and healing branches, terminal capability and resource-priced rewind model | Observation | Direct | High | V1, POPSOT-002–POPSOT-011 |
| `POPSOT-013` | No current Steam executable, direct play, save or audiovisual trace was inspected | Confirmed | Direct | High | R1 |

## Basic data

- Release / origin: Ubisoft identifies the PC product as released on
  2003-12-02; the official page and Steam offer attribute the published
  product to Ubisoft and the Prince of Persia property created by Jordan
  Mechner.
- Platform or physical form: current licensed English Windows Steam app
  `13600`, fresh unmodified single-player start, keyboard-and-mouse rule
  references from the linked English PC manual.
- Puzzle family: real-time system pressure; tactical forecast and counterplay;
  ordered dependency sequencing; world topology and perspective.
- Primary and official sources, accessed 2026-09-21:
  - **[P1]** [official Ubisoft product
    page](https://www.ubisoft.com/en-us/games/prince-of-persia-the-sands-of-time),
    for product identity, PC platform, release date and the Dagger/time-control
    premise.
  - **[P2]** [Steam app
    `13600`](https://store.steampowered.com/app/13600/Prince_of_Persia_The_Sands_of_Time/),
    for the licensed current Windows offer, English interface, single-player
    category, Ubisoft publisher, release date and official manual link. The
    current store's developer label is recorded only as storefront metadata
    and is not used to rewrite historical authorship.
  - **[P3]** [official English PC
    manual](https://cdn.akamai.steamstatic.com/steam/apps/13600/manuals/manual_english.pdf),
    pp. 4–18, for first-control entry, movement and combat inputs, prompted
    saves, Dagger powers, Power of Revival input, ten-second maximum, Sand
    Tank consumption, Life/Sand/Time HUD, health damage, water healing, block
    and later-power exclusions.
- Reproducible secondary sources, accessed 2026-09-21:
  - **[S1]** [GameSpot written
    walkthrough](https://www.gamespot.com/articles/prince-of-persia-the-sands-of-time-walkthrough/1100-6085301/),
    for the training route, breakable obstructions, guard and water branches,
    first save corridor, treasure-vault wall/ledge/pole/column/statue route and
    Dagger terminal.
  - **[S2]** [independent PC written
    walkthrough](https://gamefaqs.gamespot.com/pc/589721-prince-of-persia-the-sands-of-time/faqs/30280),
    for the same bypassable guards, prompts, water, first save, exact
    treasure-vault traversal and first returned control after acquisition.
  - **[S3]** [StrategyWiki treasure-vault
    route](https://strategywiki.org/wiki/Prince_of_Persia%3A_The_Sands_of_Time/The_Maharajah%27s_Treasure_Vaults),
    for the Dagger pickup, falling rock and automatic Power of Revival
    demonstration immediately before the escape route.
- Reproducible control: **[V1]**
  [`verify_prince_of_persia_sands_of_time_control.py`](../../../scripts/verify_prince_of_persia_sands_of_time_control.py),
  an executable source-model control for route order, optional combat/healing,
  acquisition and finite rewind legality.
- Research record: **[R1]** local preflight found no installed app manifest,
  depot, executable, profile, save, input trace or audiovisual capture.
- Claim IDs: `POPSOT-001`–`POPSOT-013`.

## Mechanical decomposition

### Action Genes

- `ACT-008` owns ground, air, wall, ledge, column and statue traversal as
  parameters of one directly controlled body. `ACT-161` owns sword strikes
  against human guards and required breakable barricades. `ACT-437` owns the
  held undirected sword block. `ACT-341` owns sustained drinking at reachable
  pools or fountains. `ACT-044` owns holding rewind through recent retained
  history and releasing at a safer earlier state.
- Separate wall-run, wall-jump, shimmy, vault, water, Dagger and tutorial-input
  genes are rejected: they do not create a new action boundary beyond direct
  navigation, contextual fixture use or rewind.
- Claims: `POPSOT-002`–`POPSOT-009`.

### System Behaviour Genes

- `SYS-215` resolves directly commanded real-time sword combat and blocking;
  `SYS-578` applies fall, guard, attack and trap damage to one Life pool,
  restores missing Life from water and makes zero terminal; `SYS-755` removes
  the required barricades after eligible sword damage.
- Generalised `SYS-398` retains one authored capability in the continuing
  character state after acquisition, whether the capability is intrinsic or
  remains bound to a unique non-consumed carried artefact. Here the Dagger
  acquisition retains Power of Revival when ordinary control returns.
- The falling-rock demonstration is an authored acquisition settlement. It
  establishes the capability but is not mislabelled as a player-selected
  rewind input.
- Claims: `POPSOT-004`–`POPSOT-010`.

### Constraint Genes

- `CON-282` owns the ordered authored route from first control through required
  obstructions and traversal gates to the Dagger. `CON-351` requires a filled
  Sand Tank and usable Time Circle history for rewind and consumes one Sand
  Tank when the rewind is accepted.
- The scarce resources are current Life, the optional distance to healing
  water, and—only after the terminal acquisition—the bounded sand/history
  allowance. Guard groups are not clearance gates where the sources permit
  bypass, so `CON-402` is absent.
- Claims: `POPSOT-003`–`POPSOT-009`, `POPSOT-011`.

### Information Genes

- `INF-115` exposes nearby geometry, guards, hazards and attacks through the
  third-person frame and sound. `INF-119` exposes current Life and, after the
  acquisition, Sand Tanks and Time Circle state. `INF-268` exposes one current
  authored movement, combat or hazard instruction without revealing the full
  future route.
- The first prompted save is route context, not a separately admitted
  information or persistence boundary.
- Claims: `POPSOT-003`–`POPSOT-006`, `POPSOT-010`.

### Objective Genes

- New `OBJ-201` completes a bounded authored opening by reaching and acquiring
  its designated unique artefact, accepting the acquisition demonstration and
  regaining ordinary control with the artefact's first capability retained.
- Merely reaching the statue or showing the Dagger is not sufficient; the
  terminal requires acquisition settlement and returned control. The escape,
  Hourglass and later campaign are not required.
- Claims: `POPSOT-006`, `POPSOT-007`, `POPSOT-011`.

### Time Genes

- `TIM-003` owns live movement, guards, traps, falls and held block while the
  player decides. `TIM-007` owns branchable player-reversible retained history:
  after acquisition, rewind may restore an already lived state and release may
  replace its discarded continuation.
- The automatic falling-rock demonstration does not itself satisfy the player
  action, but the official manual establishes that the returned state accepts
  the same first power under the bounded Sand/Time legality.
- Claims: `POPSOT-003`–`POPSOT-010`.

## Reproducible transitions

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Opening cinematic letterboxing has disappeared | Press local movement toward the curtains | The Prince advances into the palace under ordinary control | reproducible entry after non-interactive cinema | `POPSOT-002` |
| A required barricade blocks the route | Draw the sword and strike it | Eligible obstruction damage removes the barrier and exposes the continuation | direct attack and world-removal are distinct rules | `POPSOT-004` |
| A human guard threatens the route | Hold block through an eligible strike or move past the documented bypass | The guard's hit is deflected, or the Prince leaves its pursuit region without a clearance flag | combat is live but not every encounter gates progress | `POPSOT-004` |
| Life is below maximum beside reachable water | Hold the contextual action at the pool | Water restores missing Life up to its cap | healing is a fixture-mediated state change | `POPSOT-005` |
| A horizontal gap has no floor path | Run into the compatible wall and commit the prompted jump if needed | Wall travel and transfer reach the authored ledge or opposite wall | wall-running is direct navigation, not teleportation | `POPSOT-003`, `POPSOT-006` |
| Moving spike poles occupy the corridor | Cross only through a currently open lane | Safe passage preserves Life; contact applies damage | live hazard phase affects route safety | `POPSOT-005`, `POPSOT-006` |
| The statue route is complete and the Dagger is approached | Enter the acquisition trigger | The Dagger becomes retained, the falling-rock mishap is automatically rewound, and ordinary control returns with Power of Revival | exact positive terminal and capability acquisition | `POPSOT-007`, `POPSOT-011` |
| Returned control has one filled Sand Tank and retained recent history | Hold Rewind, then release before the failure state | Prior states restore up to the available horizon, one Sand Tank is spent and play resumes from the selected earlier moment | finite branchable rewind rather than restart | `POPSOT-008`–`POPSOT-010` |
| Returned control has no filled Sand Tank | Request Rewind | The resource predicate fails and no accepted rewind is funded | the first power is capability-gated by current reserve | `POPSOT-009`, `POPSOT-010` |

## Strategic and experiential structure

- Local decision: read the immediate geometry or guard state and choose a jump,
  wall commitment, block, strike, bypass or recovery detour.
- Medium-term planning: preserve enough Life to cross successive authored
  gaps and moving hazards while recognising when nearby water makes risk
  recoverable.
- Long-term structure: convert a linear combat tutorial into increasingly
  vertical traversal, then end the packet where a unique acquired artefact
  changes future failure from terminal restart to consumable history repair.
- Common heuristics: follow the current prompt rather than infer the whole
  route; use the camera's local framing; block only eligible attacks; treat
  spike-pole phase and wall-run landing geometry as commitments; heal before
  the next traversal chain.
- Failure attribution: before acquisition, late jumps, unsafe falls, attacks
  and traps reduce one visible Life pool. After acquisition, a failed branch is
  recoverable only while both retained history and Sand Tank reserve remain.
- Player-trust factors: wall/ledge contacts, damage, water recovery, tutorial
  stage, Dagger ownership, rewind horizon and Sand consumption must update
  consistently around the exact moment of acquisition.
- Claims: `POPSOT-003`–`POPSOT-012`.

## Replay and variation

- Geometry, prompts, guard placements, water sources, spike poles, Dagger
  location and acquisition sequence are authored and fixed.
- Incidental combat, damage, healing, exact wall-run timing and camera movement
  may vary; cited guards can be bypassed, so their defeat is not a terminal
  predicate.
- No procedural room generation, random loot, enemy drop or later sand-refill
  loop is admitted.
- Typical replay motive is cleaner traversal, less damage, faster route
  execution or different optional guard engagement, not a new opening layout.
- Claims: `POPSOT-003`–`POPSOT-011`.

## Adjacent systems and history

- Braid, Tin Hearts and Viewfinder share branchable restoration of retained
  recent history. Their scoped rewind is ordinarily unpriced or tied to a
  different puzzle state; this packet makes the returned capability depend on
  a bounded Sand Tank and Time Circle.
- Ninja Gaiden Black shares wall-rich embodied navigation, direct sword combat,
  held guard, damage/healing, breakables, authored tutorial cues and ordered
  gates. It trades defeat Essence between recovery and charged offence and ends
  at a guardian chapter evaluation; this packet may bypass human guards and
  instead terminates at finite rewind acquisition.
- Super Metroid and Ori and the Will of the Wisps acquire retained
  capabilities through authored routes. Their packet terminals prove later
  route use or a restorative checkpoint; this one stops immediately after the
  unique artefact and its first power settle.
- Other console releases and any remake are adjacent products, not evidence of
  exact parity with the selected current Windows offer.
- Claims: `POPSOT-001`–`POPSOT-013`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-044`, `ACT-161`, `ACT-341`, `ACT-437` | wall-run, wall-jump, ledge, block and Dagger names are parameters |
| System Behaviour | `SYS-215`, `SYS-398`, `SYS-578`, `SYS-755` | guards, Life, water, barricades and Dagger identity are parameters |
| Constraint | `CON-282`, `CON-351` | authored route, Sand Tank price and Time Circle horizon are parameters |
| Information | `INF-115`, `INF-119`, `INF-268` | tutorial wording, camera and HUD layout are presentation/parameters |
| Objective | `OBJ-201` | treasure vault, Dagger and first-power identity are parameters |
| Time | `TIM-003`, `TIM-007` | live hazard cadence and rewind horizon are parameters |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `343` (`GAME-0001`–`GAME-0343`).
- Exact genome matches: none.
- Tied near matches: `GAME-0224` — Once Human (`9 / 22 = 0.409091`).
- Supported combination subsets: none.
- Scan date: 2026-09-21.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0224` — Once Human | `ACT-008`, `ACT-161`, `ACT-341`, `SYS-215`, `CON-282`, `INF-115`, `INF-119`, `INF-268`, `TIM-003` | Both directly navigate a third-person authored opening, use real-time attacks and contextual water recovery, expose health and local hazards, and advance through ordered gates under live time. Once Human adds gather/craft/base-survival onboarding, persistent online-service systems, a broad quest HUD and one checkpointed tutorial settlement. This packet instead adds held sword block, breakable route barriers, retained Dagger capability, Sand-priced history rewind and an artefact-acquisition terminal. | Near, `9 / 22 = 0.409091` |

### Preserved research notes

- New genes: `OBJ-201`.
- Classification result: `New gene`.
- Evidence and reasoning: all action, simulation, legality, information and
  time boundaries transfer from independent lower-ID carriers. The terminal is
  not generic location arrival, token collection or chapter completion: it
  accepts one unique artefact's authored acquisition demonstration and returns
  ordinary control with its first capability retained.

## Taxonomy impact

- Registry changes: add `OBJ-201`; generalise `SYS-398` to cover a retained
  capability that remains bound to a unique non-consumed carried artefact;
  add supporting-carrier evidence to reused definitions where applicable.
- Taxonomy-change record:
  [`TAXONOMY_CHANGE_086`](../../../research/taxonomy-changes/TAXONOMY_CHANGE_086.md).
- Candidate terms affected: wall-run, wall-jump, water, held block and Sand
  Tank remain parameters or reused boundaries; the retained artefact-powered
  terminal becomes `OBJ-201`.

## Negative results

- No direct current-depot execution, exact build hash, save/reload equality,
  collision-frame measurement, audiovisual observation or controller trace.
- No evidence that every opening guard must be defeated; `CON-402` and
  finite-clearance System genes are rejected.
- No player-selected rewind occurs before the terminal. The automatic rock
  demonstration proves acquisition; `ACT-044` and `TIM-007` are admitted from
  the official manual's newly available post-acquisition input, not from a
  falsely labelled cutscene action.
- Later sand retrieval and Power Tank mechanics are explicitly excluded, so no
  replenishment, enemy-finish, slow-motion or freeze genes enter the signature.

## Delta summary

## New facts

- [Observation | Corroborated | High] The source-bounded opening joins optional
  live guard handling, water recovery and a fixed acrobatic vault route before
  ordinary control returns with one retained Dagger power (`POPSOT-003`–
  `POPSOT-007`).
- [Confirmed | Direct | High] Accepted player rewind requires retained recent
  history and spends one filled Sand Tank (`POPSOT-008`–`POPSOT-010`).

## New genes

- [Observation | Corroborated | High] `OBJ-201` isolates the terminal where one
  unique artefact is acquired, its first capability is demonstrated and
  ordinary control returns with that capability retained.

## New combinations

- [Observation | Corroborated | High] No verified combination is expected;
  deterministic subset validation remains required.

## Taxonomy changes

- [Observation | Corroborated | High] `SYS-398` is generalised to permit a
  retained capability bound to one unique non-consumed carried artefact;
  `OBJ-201` is appended without altering earlier signatures.

### Added

- `GAME-0344` as one source-bounded opening route through first retained
  Dagger power.
- `OBJ-201` as the exact artefact-capability terminal.

### Reused

- Sixteen Active genes across the six canonical types.

### Generalised

- `SYS-398` now allows the retained capability to remain tied to one unique
  non-consumed carried artefact without changing its causal acquisition
  boundary or any earlier signature.

### Rejected

- Separate genes for wall-running, wall-jumping, shimmying, spike poles,
  water, Dagger identity, tutorial button prompts, optional guard clearance,
  automatic cinematic rewind and the first save prompt.

### Preserved

- Every lower-ID signature, lifecycle state, verified combination and family
  definition.
