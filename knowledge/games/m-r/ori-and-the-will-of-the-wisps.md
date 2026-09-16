---
game_id: GAME-0293
slug: ori-and-the-will-of-the-wisps
game_title: Ori and the Will of the Wisps
analysis_status: reviewed
reviewed: 2026-09-13
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-161
    - ACT-215
    - ACT-223
    - ACT-341
  system:
    - SYS-063
    - SYS-215
    - SYS-362
    - SYS-369
    - SYS-398
    - SYS-578
    - SYS-755
  constraint:
    - CON-282
    - CON-349
    - CON-403
  information:
    - INF-119
  objective:
    - OBJ-172
  time:
    - TIM-003
---

# Game: Ori and the Will of the Wisps

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Product names,
character identities, the exact route, checkpoint positions, damage values and
save identity parameterise the genes but do not enter their labels.

## Analysis scope

- Version / ruleset: current unmodified English Windows Steam application
  `1057090`, one-app base package `353051`, default public branch Build ID
  `5845748`, updated 2020-11-18; checked 2026-09-13. Moon Studios' official
  `Patch 3.1` notice was published 2020-11-19 and aligns with the final public-
  branch window, so the named patch and build are recorded separately.
- Product boundary: Ori and the Will of the Wisps base game by Moon Studios and
  Xbox Game Studios, not Ori and the Blind Forest, soundtrack application
  `1258740`, a console version, historical branch, modification or randomizer.
- Platform, input and difficulty: English interface, Windows, Xbox-compatible
  controller, offline single player, fresh New Game on `Normal`. Easy, Hard,
  online Spirit Trial ghosts and accessibility or sequence-breaking variants
  are excluded.
- Entry: first ordinary control in the authored Swallow's Nest prologue, before
  retrieving Kuro's Feather for Ku. The prologue is not skipped.
- Primary decision loop: directly move, jump, wall-jump and traverse the
  authored side-view route; commit contextual pickups and interactions; use the
  temporary Torch and later Spirit Edge to strike reachable enemies and
  breakable barriers; collect the missing Keystone, return to Tokk for the
  second and spend both at the first Spirit Gate; flee Howl, then time short
  attack-and-retreat windows until Howl withdraws; absorb the first Spirit
  Tree, assign the retained Spirit Edge to one of the three active buttons and
  use it against enemies and weak walls; follow the direct lower/eastern branch
  from the Moki conversation to the first Spirit Well; activate it to refill
  health and energy and write an explicit save.
- Positive terminal: the first Inkwater Marsh Spirit Well has accepted its
  interaction after Spirit Edge acquisition, refilled the current health and
  energy state and written the route state. A same-save reload with the
  acquired ability, currency, health and route progress retained is the intended
  verification, but no local application or save existed, so that reload was
  not performed and no returned values are claimed as observed.
- Negative terminal: lethal damage restores the latest automatic checkpoint
  rather than preserving the failed transient position. A death before the
  Spirit Well has saved a recently collected object can require recollecting
  it; merely seeing a pickup or an automatic-save icon is not the positive
  terminal.
- Included: the mandatory prologue interaction and temporary Ku flight; direct
  movement, jumping, wall movement and chase traversal; visible health, energy
  and Spirit Light; Torch and Spirit Edge strikes; breakable route barriers;
  Tokk's required missing-key route; two carried Keystones and their first
  Spirit Gate consumption; the Howl chase and repelling encounter; telegraphed
  bite/smash response; first Spirit Tree acquisition; retained Spirit Edge and
  its three-button ability-wheel assignment; automatic checkpoint recovery;
  the direct post-tree route to the first Spirit Well; its manual save, full
  health/energy refill and future warp role.
- Excluded: the optional early Life Cell and Spirit Light detours; Magnet and
  every other Spirit Shard; Double Jump, Regenerate, Spirit Arc, purchased
  Opher abilities and every later traversal ability; map purchase from Lupo;
  Howl's Fang and other side quests; Combat Shrines and Shard Slot upgrades;
  Spirit Trials; Kwolok's Hollow, Wellspring and every later region, boss,
  Wisp and ending; Easy, Hard, speedrunning, sequence breaks, established saves,
  soundtrack DLC, achievements, screenshots, official artwork, third-party
  images, video and audio.
- Reproducible parameterisation: install Steam app `1057090` from base package
  `353051`, confirm public Build ID `5845748`, use the English Windows client,
  Xbox-compatible controller, offline mode and a fresh `Normal` New Game.
  Complete the unskipped prologue, wake in Inkwater Marsh, obtain the Torch,
  speak with Tokk, collect the missing Keystone, receive his Keystone and open
  the two-key Spirit Gate. Survive the chase, repel Howl, absorb Spirit Edge,
  assign it to an active button, break the return barrier and follow the direct
  lower/eastern route after the Moki conversation rather than the western
  Double Jump detour. Reach and use the first Spirit Well, then quit and reload
  that same save to inspect retained ability, health, energy, Spirit Light and
  route state. Exact damage, pickups, currency, autosave moments, button slot,
  elapsed time and optional incidental fights remain parameters.
- Potential scoped modules: one executed save/quit/reload and death/recovery
  trace; Double Jump and the first ability-gated traversal loop; Regenerate and
  energy spending; Magnet plus the three-slot Shard loadout; map purchase;
  Combat Shrine slot expansion; Spirit Trials; or the complete campaign each
  requires its own entry, loop, terminal and evidence review.
- Direct-play status: not conducted. No local application manifest, install,
  save directory or matching Steam userdata was found. Valve and Xbox establish
  the lawful product, package, platform, release and broad feature boundary;
  Moon Studios' official patch post establishes the named version. Two written
  route families establish the opening sequence, while written save references
  corroborate automatic checkpoints and the Spirit Well save/refill boundary.
  This is an evidence-backed reconstruction, not a claimed playthrough,
  entitlement or reload. No audiovisual source was opened, played, heard,
  analysed or used.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `ORI-001` | Steam app `1057090` and one-app base package `353051` identify the released Windows base product by Moon Studios and Xbox Game Studios | Confirmed | Direct | High | P1, P2, P3 |
| `ORI-002` | The public branch projects Build ID `5845748`; Moon Studios separately names the corresponding final update window `Patch 3.1` | Confirmed | Corroborated | High | P4, S1 |
| `ORI-003` | The unskipped prologue requires retrieving Kuro's Feather, returning to Ku and traversing the short flight before the storm separates the pair | Observation | Limited | Medium | S2 |
| `ORI-004` | Inkwater Marsh first supplies a Torch that attacks enemies and breaks barriers; the first defeated enemy can release an Energy Orb | Observation | Corroborated | High | S3, S4 |
| `ORI-005` | Tokk's Missing Key route requires one found Keystone, returns a second Keystone and opens the first Spirit Gate with the pair | Observation | Corroborated | High | S3, S4 |
| `ORI-006` | Howl first drives a chase, then uses advancing bite and smash attacks; repeated short strikes and retreat reduce the encounter until Howl withdraws | Observation | Corroborated | High | S3, S4 |
| `ORI-007` | Absorbing the first Spirit Tree in Howl's Den permanently grants Spirit Edge, a melee ability that damages enemies and weak walls | Observation | Corroborated | High | S3, S4, S5 |
| `ORI-008` | Active abilities are assigned through a wheel to three controller face buttons; Spirit Edge is the first such attack after the temporary Torch | Observation | Limited | Medium | S5, S6 |
| `ORI-009` | A direct lower/eastern branch after the first Moki conversation reaches the first Spirit Well without requiring the later Double Jump tree | Observation | Corroborated | High | S3, S4 |
| `ORI-010` | Using a Spirit Well saves and fully refills health and energy; discovered wells also support warp travel | Observation | Corroborated | High | S3, S7, S8 |
| `ORI-011` | The game also writes automatic checkpoints, and lethal failure restores a recent checkpoint rather than requiring a player-created Soul Link | Observation | Corroborated | Medium | S8, S9 |
| `ORI-012` | Magnet, Double Jump, Regenerate, map purchase and the first Shard Slot expansion can occur later or on optional detours and are not prerequisites of the selected direct first-well route | Observation | Corroborated | High | S3, S4, S10 |
| `ORI-013` | No local application or save was available, so the intended same-save reload remains an unexecuted verification boundary | Confirmed | Direct | High | R1 |

## Basic data

- Release / origin: Moon Studios GmbH; published by Xbox Game Studios; Windows
  Steam release 2020-03-10.
- Platform or physical form: lawfully offered English Windows Steam app
  `1057090`, one-app package `353051`; fresh offline single-player `Normal`.
- Puzzle family: tactical forecast and counterplay; real-time system pressure;
  world topology and perspective; ordered dependency sequencing.
- Primary and official sources, accessed 2026-09-13:
  - **[P1]** [Valve application data](https://store.steampowered.com/api/appdetails?appids=1057090&cc=ua&l=english),
    for exact title, developer, publisher, Windows support, release,
    single-player, full-controller and Steam Cloud categories, base package and
    soundtrack application.
  - **[P2]** [Valve package data](https://store.steampowered.com/api/packagedetails?packageids=353051&cc=ua&l=english),
    for the one-app base package and current lawful offer.
  - **[P3]** [official Xbox product page](https://www.xbox.com/en-US/games/store/ori-and-the-will-of-the-wisps/9N8CD0XZKLP4),
    for Moon Studios/Xbox Game Studios provenance, release, single-player and
    controller support, crafted platforming, spirit weapons, spells, skills,
    Shards, enemies, puzzles, Spirit Trials and Shrines.
  - **[P4]** [Moon Studios' official Patch 3.1 post](https://steamcommunity.com/app/1057090/discussions/0/2968397584537393710/),
    for the named final patch and its 2020-11-19 publication.
- Corroborating textual sources, accessed 2026-09-13:
  - **[S1]** [SteamCMD public-branch projection](https://api.steamcmd.net/v1/info/1057090),
    for Build ID `5845748`, its timestamps and the Windows cloud-save patterns;
    secondary distribution data.
  - **[S2]** [GameFAQs prologue route](https://gamefaqs.gamespot.com/xboxone/211254-ori-and-the-will-of-the-wisps/faqs/78217/prologue),
    for Kuro's Feather, the return to Ku, temporary flight and the storm
    transition.
  - **[S3]** [GameFAQs Inkwater Marsh route](https://gamefaqs.gamespot.com/xboxone/211254-ori-and-the-will-of-the-wisps/faqs/78217/inkwater-marsh),
    for Torch, Missing Key, two Keystones, Spirit Gate, Howl, Spirit Edge and
    the direct first-well branch before its later Double Jump sequence.
  - **[S4]** [independent Inkwater Marsh route](https://gamerwalkthroughs.com/ori-and-the-will-of-the-wisps/inkwater-marsh/),
    for the same mandatory gates, Howl withdrawal, Spirit Edge, weak barriers,
    well refill and the alternative western ordering that visits Double Jump
    first.
  - **[S5]** [Spirit Edge reference](https://oriandtheblindforest.fandom.com/wiki/Spirit_Edge)
    and [abilities reference](https://www.neoseeker.com/ori-and-the-will-of-the-wisps/Abilities),
    for the first retained melee ability, its tree acquisition, weak-wall
    effect and ability-wheel membership.
  - **[S6]** [written ability-assignment trace](https://steamcommunity.com/app/1057090/discussions/0/2990917484128920545/?l=english),
    for the controller wheel and three button assignments; an undated
    community answer without developer participation.
  - **[S7]** [Spirit Well reference](https://oriandtheblindforest.fandom.com/wiki/Spirit_Well),
    for full health/energy restoration and saving on use.
  - **[S8]** [written save guide](https://www.gamespew.com/2020/03/how-to-save-your-game-in-ori-and-the-will-of-the-wisps/),
    for automatic saves, the save indicator, backup saves and the Spirit Well
    interaction that saves and refills both meters.
  - **[S9]** [contemporary written preview](https://www.gamepressure.com/editorials/previews/ori-and-the-will-of-the-wisps-cutest-hardcore-game/z825a),
    for dense automatic checkpoints and nearby post-death restoration.
  - **[S10]** [GameFAQs ability and Shard catalogue](https://gamefaqs.gamespot.com/xboxone/211254-ori-and-the-will-of-the-wisps/faqs/78217/upgrades-spirit-shards),
    for the later Double Jump, Regenerate, Spirit Arc, Shards and Combat Shrine
    boundaries.
- Source-class limitation: the complete route, exact checkpoint restoration,
  three-button assignment and first-well rules remain secondary. The two route
  guides share the mandatory sequence but deliberately disagree in optional
  ordering after Spirit Edge; the selected reproducible route follows S3's
  direct branch and treats S4's Double Jump detour as evidence of flexibility,
  not a prerequisite. No source is promoted merely because it agrees with
  another page in the same family.
- Reproducible control: **[V1]** repository-side transition trace across
  `P1`–`P4`, `S1`–`S10` and `R1` under the declared app, build, patch,
  platform, input, difficulty, entry, direct route, exclusions and terminal;
  written-evidence reasoning, not direct play.
- Research record: **[R1]** local preflight on 2026-09-13 found no app manifest,
  install directory, matching save or Steam userdata.
- Claim IDs: `ORI-001`–`ORI-013`. No audiovisual evidence was used.

## Mechanical decomposition

### Action Genes

- Existing `ACT-008` owns Ori's direct running, jumping, wall movement, the Ku
  prologue flight and the Howl chase; `ACT-161` owns Torch and Spirit Edge
  strikes against reachable enemies or weak barriers; `ACT-223` the timed
  repositioning against Howl's bite and smash; `ACT-341` the contextual
  feather, Keystone, Spirit Gate, Spirit Tree and Spirit Well interactions;
  and `ACT-215` the three-button active-ability assignment that makes Spirit
  Edge available after acquisition. Claims: `ORI-003`–`ORI-010`.

### System Behaviour Genes

- Existing `SYS-063` owns the two carried Keystones and their barrier
  consumption; `SYS-215` direct hostile combat in live time; `SYS-362` Howl's
  bounded withdrawal and route-progress settlement; `SYS-398` retention of
  Spirit Edge as the acquired capability that enables compatible weak-wall
  interactions; `SYS-755` removal of those barriers after accepted damage;
  and `SYS-578` damage, life-orb recovery and the continuous health terminal.
- Existing `SYS-369`, generalised by `TAXONOMY_CHANGE_070`, owns restoration of
  the latest automatic checkpoint after lethal failure without claiming an
  unevidenced inventory or currency-retention policy.
- Resolution order: collecting the missing Keystone and receiving Tokk's
  second creates a count that the Spirit Gate consumes; Howl's attacks and
  Ori's strikes resolve until withdrawal; the first tree registers Spirit Edge;
  assignment makes its attack command available; accepted damage removes weak
  barriers; the first-well interaction refills health and energy and writes the
  save. Claims: `ORI-004`–`ORI-011`.

### Constraint Genes

- Existing `CON-403` owns the exact two-Keystone requirement and subtraction at
  the first Spirit Gate; `CON-282` the authored ordering from Tokk and gate to
  Howl and Spirit Tree; and `CON-349` the post-tree weak-wall edge requiring
  the acquired Spirit Edge rather than the earlier extinguished Torch.
- Scarce or gated state is the two-Keystone count, current health, active-
  ability slots, distance from the latest automatic checkpoint and whether the
  first well has accepted its write. Energy is visible and refilled at the
  terminal, but no energy-spending ability is required before it. Claims:
  `ORI-005`–`ORI-012`.

### Information Genes

- Existing `INF-119` owns visible health, energy, Spirit Light and acquired or
  assigned ability state before the next route or combat commitment.
- The packet does not add an explored-map owner: map purchase and route-marker
  dependence are excluded. Nor does it add Shard-slot information, because the
  optional Magnet pickup and Combat Shrine occur outside the direct terminal.
  Claims: `ORI-004`, `ORI-008`, `ORI-010`, `ORI-012`.

### Objective Genes

- New `OBJ-172` owns the complete fresh route from the authored prologue through
  the two-key gate, repelled guardian and retained first ability to the first
  restorative save point. An automatic checkpoint, Howl withdrawal, Spirit
  Edge acquisition or merely reaching the well remains intermediate until the
  well interaction has saved and refilled state. Claims: `ORI-003`–`ORI-013`.

### Time Genes

- Existing `TIM-003` owns uninterrupted movement, chase, enemy attacks,
  defensive timing and automatic checkpoint pressure. Menus and the save write
  do not turn the whole packet into a turn-based or deadline schedule. Claims:
  `ORI-004`, `ORI-006`, `ORI-011`.

## Reproducible transitions

| Before | Action | Deterministic or bounded resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Swallow's Nest is controllable; Ku cannot fly | Retrieve Kuro's Feather and return to Ku | The authored prologue supplies temporary paired flight and then the storm transition | included non-skipped entry | `ORI-003` |
| Torch is reachable in Inkwater Marsh | Interact, then strike a compatible target | Ori can damage the enemy or remove the weak barrier; an eligible defeated enemy can release Energy | first temporary combat tool | `ORI-004` |
| Tokk has registered Missing Key | Collect the cave Keystone and return | Tokk supplies the second, leaving a count of two | staged key acquisition | `ORI-005` |
| Two Keystones are carried at the first Spirit Gate | Commit the gate interaction | Both are consumed and the route to Howl opens | typed finite gate | `ORI-005` |
| Howl is chasing or attacking | Jump away, strike briefly and retreat | Bite or smash misses when positioning succeeds; accumulated damage makes Howl withdraw | live guardian settlement | `ORI-006` |
| First Spirit Tree is reachable | Absorb its light | Spirit Edge becomes retained and appears in the active-ability wheel | acquired capability | `ORI-007`, `ORI-008` |
| Spirit Edge is acquired but not assigned | Select it in the wheel and choose a face button | The chosen button now commits its melee attack | bounded live loadout | `ORI-008` |
| A compatible post-tree barrier blocks the return route | Strike it with Spirit Edge | Accepted damage removes the solid obstruction | capability-gated world edge | `ORI-007` |
| Moki conversation has ended after the tree | Take the direct lower/eastern branch | Ori reaches the first Spirit Well without visiting the Double Jump tree | exclusion boundary | `ORI-009`, `ORI-012` |
| First Spirit Well is reachable | Press the contextual use command | Health and energy refill, the well becomes a warp point and the game writes a save | positive terminal transition | `ORI-010` |
| Lethal failure occurs before the terminal | Allow checkpoint restoration | Failed transient position is discarded and control resumes at a recent automatic checkpoint | bounded negative state | `ORI-011` |
| Well save exists | Quit and reload the same save | Intended verification checks ability, resource and route retention; not executed locally | evidence limit | `ORI-010`, `ORI-013` |

## Strategic and experiential structure

- Local decision: alternate short attacks with movement that clears Howl's
  telegraphed reach, then use the new Spirit Edge only after assigning it.
- Medium-term planning: complete the exact two-key loop before the first gate,
  recognise when the temporary Torch is gone and route directly toward the well
  rather than importing attractive optional upgrades.
- Long-term structure: automatic checkpoints keep failure local, while the
  first deliberate Spirit Well use creates the retained handoff for later
  ability-gated exploration.
- Common heuristics: make one or two Howl strikes per safe window; verify the
  Spirit Edge assignment before attacking the exit barrier; take the lower east
  branch immediately after the Moki conversation; use the well before optional
  exploration.
- Failure attribution: distinguish missing Keystone count, unassigned Spirit
  Edge, wrong barrier/tool relation, mistimed Howl response, unsaved recent
  pickup and a well reached but not activated.
- Player-trust factors: health and energy orbs, ability wheel, contextual
  interaction prompts, barrier response and save icon disclose the important
  state changes, though exact checkpoint placement remains authored and not
  freely chosen.
- Claim IDs: `ORI-004`–`ORI-012`.

## Replay and variation

- What changes: optional prologue and marsh pickups, incidental fights, damage,
  checkpoint timing, ability-button choice, Spirit Light total and whether the
  player detours to Double Jump before the first well.
- Randomness or procedural generation: the route, key positions, Howl and
  Spirit Tree are authored; ordinary combat timing and dropped recovery orbs
  vary, but no procedural-layout claim enters.
- Multiple viable strategies: Howl accepts different safe strike counts and
  spacing; after Spirit Edge one route reaches the well directly while another
  written guide visits Double Jump first. Only the direct branch is canonical
  here.
- Typical replay motive: cleaner movement, fewer deaths, optional exploration,
  Spirit Trials and broader ability composition; all extend beyond this unit.
- Claim IDs: `ORI-003`–`ORI-012`.

## Adjacent systems and history

- Direct predecessor: Ori and the Blind Forest is excluded and not separately
  reviewed in the corpus; its player-created Soul Link saving should not be
  imported into this sequel's automatic-checkpoint and Spirit Well rules.
- Variants: console editions, Easy and Hard, online Spirit Trials, speedrun
  skips and randomizers can alter controls, damage, route or persistence.
- Similar games: `GAME-0274` Hollow Knight, `GAME-0150` Hollow Knight:
  Silksong and `GAME-0282` Dead Cells are the declared corridors.
- Important differences: Hollow Knight and Silksong bind recovery to an attack-
  funded reserve and attach rest/death consequences to Benches; Ori's selected
  opening spends no energy before the terminal, loses no currency to a recovery
  mark in the evidenced packet, restores dense automatic checkpoints and uses
  the first well as a separate explicit save/refill boundary. Dead Cells builds
  a procedural disposable run with equipment sampling and metaprogression,
  whereas Ori's key, guardian, ability and well sequence is authored and
  retained.
- Claims: `ORI-003`–`ORI-013`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-161`, `ACT-215`, `ACT-223`, `ACT-341` | path, response timing, tool, wheel slot and well interaction |
| System Behaviour | `SYS-063`, `SYS-215`, `SYS-362`, `SYS-369`, `SYS-398`, `SYS-578`, `SYS-755` | key transfer, encounter, checkpoint, ability, health and barrier state |
| Constraint | `CON-282`, `CON-349`, `CON-403` | authored order, capability edge and two-key cost |
| Information | `INF-119` | visible health, energy, currency and ability state |
| Objective | `OBJ-172` | prologue-to-first-well retained route |
| Time | `TIM-003` | live movement, chase and combat |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `292` (`GAME-0001`–`GAME-0292`).
- Exact genome matches: none.
- Tied near matches: `GAME-0254` — CONTROL Ultimate Edition (`11 / 37 = 0.297297`).
- Supported combination subsets: none.
- Scan date: 2026-09-13.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0254` — CONTROL Ultimate Edition | `ACT-008`, `ACT-161`, `ACT-341`, `SYS-215`, `SYS-369`, `SYS-398`, `SYS-578`, `SYS-755`, `CON-282`, `INF-119`, `TIM-003` | Both directly traverse an authored live route, strike enemies and breakable barriers, retain a newly acquired world-interaction capability, restore failure from authored checkpoints and expose personal health before ordered story gates. CONTROL adds telekinetic object physics, independently recharging Service Weapon and Energy channels, cleansed service nodes, credentials, alternate-space mechanisms and a full mission settlement. Ori instead consumes a two-Keystone gate, assigns Spirit Edge in a three-button wheel, repels Howl through timed movement and ends at the first explicitly used restorative save point before its later movement, energy and Shard systems. | Near, `11 / 37 = 0.297297` |

- New genes: `OBJ-172`.
- Classification result: `New gene`.
- Evidence and reasoning: every mechanism except the bounded terminal transfers
  to an earlier owner. No earlier Objective carries a fresh authored prologue
  through a finite-key gate, repelled guardian and retained first capability to
  the first explicit restorative save point.

### Preserved research notes

- New genes: `OBJ-172`.
- Classification result: `New gene`.
- Evidence and reasoning: every mechanism except the bounded terminal transfers
  to an earlier owner. No earlier Objective carries a fresh authored prologue
  through a finite-key gate, repelled guardian and retained first capability to
  the first explicit restorative save point.
- Evidence and reasoning: Spirit Edge fits the existing retained world-
  interaction capability because it opens compatible weak-wall edges; Double
  Jump and later movement abilities are not required on the chosen direct
  route. Energy has no required spend before the well, and optional Magnet does
  not activate the Shard-slot layer.

## Taxonomy impact

- Registry changes: one new Active Objective and product-neutral wording plus
  Ori support for `SYS-369`; no earlier signature or lifecycle change.
- Taxonomy-change record:
  [`TAXONOMY_CHANGE_070`](../../../research/taxonomy-changes/TAXONOMY_CHANGE_070.md).
- Candidate terms affected: Ori, Ku, Kuro's Feather, Tokk, Keystone, Spirit
  Gate, Howl, Spirit Edge, Spirit Tree, Spirit Well, Inkwater Marsh, Normal and
  Patch 3.1 remain parameters rather than canonical IDs.

## Negative results

- `ACT-091` is rejected because the prologue and Tokk transfers are contextual
  authored interactions, not inventory-item selections addressed to a visible
  requester; `ACT-224` and `SYS-364` are rejected because the Spirit Well
  interaction is not evidenced as rest that repopulates field enemies;
  `SYS-610` is rejected because the written checkpoint sources do not establish
  its complete retained currency/inventory set; `CON-621` is rejected because
  that owner explicitly excludes restorative checkpoint fixtures; `TIM-007` is
  rejected because the packet performs no branch restoration and the intended
  same-save reload is only a validation boundary.
- `CON-351`, Regenerate and every other energy-spending ability are excluded:
  the direct first-well route acquires only the free Spirit Edge before energy
  is refilled. `CON-350` and Shard-slot information are excluded because Magnet
  is optional and the first slot expansion lies after the terminal.

## Delta summary

## New facts

- [Observation | Corroborated | High] The direct opening route consumes two
  Keystones, repels Howl, retains Spirit Edge and reaches a save/refill Spirit
  Well before Double Jump, Regenerate or Shard-slot expansion (`ORI-005`–
  `ORI-012`).
- [Confirmed | Direct | High] App `1057090`, package `353051`, public Build ID
  `5845748` and separately named Patch 3.1 freeze the current Windows product;
  no local play or reload is claimed (`ORI-001`, `ORI-002`, `ORI-013`).

## New genes

- [Observation | Corroborated | High] `OBJ-172` isolates one authored opening
  whose accepted terminal is the first explicit restorative save point after a
  finite key gate, mandatory guardian and retained first capability.

## New combinations

- [Observation | Direct | High] No new combination; no verified combination is
  a strict proper subset of the eighteen-gene genome.

## Taxonomy changes

- [Observation | Corroborated | Medium] `TAXONOMY_CHANGE_070` removes the
  mission-only and chosen-retry assumptions from `SYS-369` without changing its
  checkpoint-restoration boundary or any earlier signature.

## New questions

- In a performed Patch 3.1 run, exactly which health, energy, Spirit Light and
  pickup states survive a death immediately before versus immediately after the
  first Spirit Well save?
- Does using that first well itself respawn any nearby ordinary enemy, or are
  its save/refill and the world's later respawn cadence independent?
- What is the smallest post-well route that makes Double Jump causally required
  and therefore activates `CON-349` for movement rather than weak-wall access?

## Next recommended game

- [Hypothesis | Limited | High] V Rising.
- Optimisation criterion: replace one authored solo ability route with a
  configurable persistent vampire world, blood-linked combat and placed Castle
  Heart progression.
- Expected information gain: test world rules, blood/resource survival,
  crafting-station dependencies, boss knowledge and retained base control
  without carrying Ori's finite-key opening or restorative save-point terminal.
- Backlog impact: keep DARK SOULS™: REMASTERED, Noita and MONSTER HUNTER RISE
  in selection-018 order.

## Why this game

- [Hypothesis | Limited | High] Ori and the Will of the Wisps separates dense
  automatic checkpoint restoration from an explicit restorative save point and
  tests whether a combat ability can satisfy an existing retained world-edge
  boundary before later traversal and loadout systems appear.
