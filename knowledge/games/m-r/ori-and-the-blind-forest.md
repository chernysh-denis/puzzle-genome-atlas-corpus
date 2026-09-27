---
game_id: GAME-0431
slug: ori-and-the-blind-forest
game_title: Ori and the Blind Forest
analysis_status: reviewed
reviewed: 2026-09-27
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-089
    - ACT-161
    - ACT-341
    - ACT-569
    - ACT-570
  system:
    - SYS-215
    - SYS-398
    - SYS-578
    - SYS-973
    - SYS-1131
    - SYS-1132
    - SYS-1133
  constraint:
    - CON-136
    - CON-349
    - CON-621
    - CON-708
  information:
    - INF-119
  objective:
    - OBJ-026
  time:
    - TIM-003
---

# Game: Ori and the Blind Forest — Ginso Tree ascent and escape

Use the canonical [vocabulary and genome rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Ori, Sein, Bash, Soul Link, Ginso Tree, four Keystones and the waterline are carrier identities or parameters, not a claim that every platform game has the same rules.

## Analysis scope

- Version / ruleset: original English *Ori and the Blind Forest* released for Xbox One in March 2015, not the 2016 Definitive Edition. The Xbox-hosted game manual identifies the original controller actions. Xbox's 2014 creator-led Ginso Tree demonstration and its March 2015 release description directly support Bash, player-placed Soul Links and the flood; two written guides support the retail route. Exact executable revision, difficulty and controller trace were not inspected.
- Structured analysis target: `PLAT-XBOX-ONE` in [`knowledge/platforms/games.json`](../../platforms/games.json).
- Primary decision loop: absorb Bash from the Ancestral Tree, then move and jump up the authored Ginso Tree route while choosing a legal enemy, projectile or lantern and aiming a launch that propels Ori while redirecting a contacted projectile in the opposite direction; collect the four later Keystones and open their Spirit Gate; place a resource-priced Soul Link at a safe location when useful; use the designated Spirit Well before cleansing the two sides of the tree's heart; after restoration triggers rising water, chain available Bash targets and platform jumps upward before the water catches Ori.
- Entry: at the Ginso Tree Ancestral Tree immediately before acquiring Bash, after the first four-Keystone gate. Earlier arrival, Water Vein acquisition and the initial gate are prerequisites but not replayed inside this packet.
- Positive terminal: both heart-side obstructions have been cleared, the Element of Water has been restored, and Ori has escaped above the rising flood through the tree's upper exit. The following owl encounter and later region are excluded.
- Negative state: contact with lethal hazards or an overtaking flood ends the current traversal and returns to the latest valid save/checkpoint rather than preserving an unsaved midair position. The written route reports that the flood escape restarts when failed; a precise automatic-save implementation was not measured.
- Included: directly controlled jumps and wall movement; Spirit Flame against breakable plants or reachable enemies; four later Keystones and their gate; retained Bash acquisition; aiming and launching from an eligible lantern, enemy or projectile; reverse-direction projectile redirection into a barrier or enemy; player-chosen Soul Link cost and safe placement; the designated pre-heart Spirit Well's save and recovery; health and energy display; two-sided heart clearance; the triggered continuous water rise; live collision and escape timing.
- Excluded: pre-entry first gate and Water Vein quest, optional collectibles, extra Energy Cells, precise damage and recharge rates, broad ability-tree purchases, other forest areas, later abilities, story ending, Definitive Edition additions, One Life mode, speedrunning and sequence breaks. The guide's suggested path is not asserted as the only valid ascent. A mid-flood Soul Link is not assumed legal merely because the general save rule allows safe placement.
- Reproducible parameterisation: select the original Xbox One release; start at the Ancestral Tree after the initial Ginso gate, absorb Bash, use eligible anchors or projectiles to ascend, collect the later four Keystones and open their gate. Redirect hostile projectiles in the needed opposite direction to clear barriers or a guarded route, save at the Spirit Well, clear both heart sides and follow the resulting rising-water escape to the upper exit. The guide supplies one route, not measured timing or a guaranteed unique solution.
- Potential scoped modules: the earlier Water Vein quest, a direct save/reload/death trace, later Forlorn Ruins gravity rules, the final escape and Definitive Edition additions require separate boundaries and evidence.
- Direct-play status: no Xbox One console, entitlement, executable, save, input recording, screenshot, video or audio was inspected. The Xbox game manual, Xbox's creator-led written demonstration and launch description are primary sources; two written routes provide the specific retail sequence. This is a source-bounded reconstruction, not a witnessed successful playthrough.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `OBF-001` | The original Xbox One manual maps movement, jump, Spirit Flame, Soul Link, Bash, glide and map to separate controls. | Confirmed | Direct | High | P1 |
| `OBF-002` | Bash chooses an aimed launch from an eligible target and sends a contacted projectile opposite Ori's travel direction. | Confirmed | Corroborated | High | P2, P3 |
| `OBF-003` | Soul Link creates a player-chosen return point in a safe location and requires energy. | Confirmed | Corroborated | High | P2, P3 |
| `OBF-004` | Ginso's later ascent uses Bash targets, later Keystones and a Spirit Gate before the guarded heart route. | Observation | Corroborated | Medium | S1, S2 |
| `OBF-005` | Clearing the tree's heart restores the Element of Water and starts an upward escape ahead of a rising waterline. | Observation | Corroborated | High | P2, S1, S2 |
| `OBF-006` | A designated Spirit Well before the heart accepts a save and restores Ori; the exact restore quantities were not measured here. | Observation | Limited | Medium | S1, S2 |
| `OBF-007` | The written retail route restarts the flood escape on death; it does not verify whether every intermediate Soul Link command is accepted during that sequence. | Observation | Limited | Medium | S2 |

## Basic data

- Release / origin: Moon Studios; Microsoft Studios; original Xbox One release on 2015-03-11, per Microsoft's contemporaneous launch coverage.
- Platform or physical form: original English Xbox One release, offline single-player Ginso Tree packet; exact binary revision and difficulty unverified.
- Mechanical families: tactical forecast and counterplay (`FAM-009`), real-time system pressure (`FAM-010`) and ordered dependency sequencing (`FAM-017`).
- Sources accessed 2026-09-27: **P1** — [Xbox-hosted original game manual](https://dlassets-ssl.xboxlive.com/public/content/0bb3a78d-ea8a-48e2-9049-eec15e61c078/GameManual/6e3e9527-b705-4c19-926f-8ef24bf1f5a5/en-SG/index.html), Controls and Story; **P2** — [Xbox Wire's creator-led Ginso Tree demonstration](https://news.xbox.com/en-us/2014/08/14/gamescom-ori-preview/), for Bash's aimed/opposed movement, Soul Link and restoration-triggered escape; **P3** — [Xbox Wire's launch description](https://news.xbox.com/en-us/2015/03/12/games-ori-and-the-blind-forest-is-a-sight-to-behold/), for safe-location energy-priced Soul Links and Bash projectile use; **P4** — [original Xbox Store product](https://www.xbox.com/en-US/games/store/ori-and-the-blind-forest/C0MCC9R22KBJ), for release identity and separation from Definitive Edition.
- Corroborating written route sources: **S1** — [Gamer Walkthroughs Ginso Tree route](https://gamerwalkthroughs.com/ori-and-the-blind-forest/ginso-tree/), for the second four-Key gate, well, two heart sides and upward escape; **S2** — [GameFAQs original Xbox One guide](https://gamefaqs.gamespot.com/xboxone/805488-ori-and-the-blind-forest/faqs/71410), for the Ancestral Tree, projectile redirection, Spirit Well and failed escape reset. These guides are secondary; exact timing and unique route are unverified.
- Claim IDs: `OBF-001`–`OBF-007`. No audiovisual evidence was used.

## Mechanical decomposition

### Action Genes

- Reuse `ACT-008` for direct running, jumping and wall movement; `ACT-089` for the later four Keystones; `ACT-161` for Spirit Flame and eligible direct attacks; `ACT-341` for tree, gate, well and heart interactions.
- Add `ACT-569` for aiming and committing a Bash from an eligible lantern, enemy or projectile, distinct from ordinary jump. Add `ACT-570` for placing a player-chosen Soul Link rather than activating a fixed fixture.
- Parameters: target identity, aim vector, health and energy amounts, Keystone count and chosen save position. Claims: `OBF-001`–`OBF-006`.

### System Behaviour Genes

- Reuse `SYS-215` for ongoing actor/hazard resolution; `SYS-398` for retained Bash capability; `SYS-578` for live health; `SYS-973` for restorative use of the designated Spirit Well.
- Add `SYS-1131` for the opposite impulses applied to Ori and a Bash-contacted projectile; `SYS-1132` for saving and restoring the most recent eligible player-placed Soul Link; `SYS-1133` for the restoration-triggered rising lethal waterline.
- Resolution order: acquire Bash → aim from eligible target → launch Ori and, if applicable, reverse projectile → collect later keys and open gate → save before heart → clear both sides → flood advances while Ori climbs. Claims: `OBF-002`–`OBF-007`.

### Constraint Genes

- Reuse `CON-136` for the second four-Key and two-sided heart dependency chain; `CON-349` for Bash-required movement edges; `CON-621` for the designated Spirit Well save context.
- Add `CON-708` for Soul Link's safe-position and positive-energy requirement. Do not transfer this cost to Bash, and do not assume a mid-flood save is legal. Claims: `OBF-003`–`OBF-006`.

### Information, Objective and Time Genes

- Reuse `INF-119` for current health, energy and retained ability state; `OBJ-026` for the upper tree exit made traversable by heart restoration; `TIM-003` for live ascent and flood pressure. A precise water-speed display or deterministic future-hazard preview is not claimed.

## Reproducible transitions

| Before | Action | Bounded resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| The Ancestral Tree is reached without Bash | Interact and absorb its light | Bash becomes available for later target-gated ascent | retained traversal ability, not a starting move | `OBF-004` |
| A hostile projectile crosses an otherwise blocked route | Hold Bash, choose a direction, release from that projectile | Ori launches along the chosen line while the projectile goes opposite, potentially breaking an eligible barrier | coupled but opposite player/projectile motion | `OBF-002` |
| Ori has energy at a safe pause in the ascent | Place Soul Link | Energy is spent and a player-chosen save/return anchor is written; unsafe or unfunded attempts are not represented as successful | resource-priced checkpoint choice | `OBF-003` |
| The later Spirit Gate is closed | Collect the four later Keystones and open it | The authored continuation to the guarded heart becomes available | dependency gate | `OBF-004` |
| A pre-heart Spirit Well is reached | Activate it | The designated fixture saves and restores resources before the heart challenge | fixed checkpoint differs from placed Soul Link | `OBF-006` |
| Both heart sides are obstructed | Redirect projectiles to clear each side | The Element of Water is restored and the water-rise escape starts | prerequisite trigger and hazard phase | `OBF-005` |
| Water rises below an available Bash target | Aim and chain Bash or platform jumps upward | Ori escapes if the upper exit is reached before contact; contact fails the run and requires retry from an eligible save | bounded timed escape | `OBF-005`, `OBF-007` |

## Strategic and experiential structure

- Local decision: choose an available Bash target and a launch angle that avoids spikes and, when relevant, sends a projectile toward a barrier or foe.
- Medium-term planning: keep enough energy for a safe Soul Link, gather the later keys and use the Spirit Well before the heart.
- Long-term structure: restore water and escape above it; no later region is part of this signature.
- Failure attribution: a poor aim or delayed ascent is legible during the flood, but exact speed and automatic retry point were not measured.
- Player-trust factor: Xbox describes Soul Link as a choice with an energy cost, not an unlimited save-anywhere guarantee.

## Replay and variation

The authored tree layout and heart trigger persist. Save placement, optional resources, encounter handling, launch angles and failed escape attempts may vary. No procedural tree generation or randomly selected water rise is asserted.

## Adjacent systems and history

*Ori and the Will of the Wisps* (`GAME-0293`) uses dense automatic checkpoints in its analysed opening, whereas this original game's scoped route uses a player-placed, energy-priced Soul Link and a later fixed well. *Hollow Knight* (`GAME-0274`) also has checkpoint decisions but its Bench/Geo/Focus loop is not the Ginso Bash-and-flood packet.

## Normalised genome

| Type | Active gene IDs | Key parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-089`, `ACT-161`, `ACT-341`, `ACT-569`, `ACT-570` | avatar, keys, Bash aim and save placement |
| System Behaviour | `SYS-215`, `SYS-398`, `SYS-578`, `SYS-973`, `SYS-1131`, `SYS-1132`, `SYS-1133` | live collision, health, well, projectile impulse, checkpoint and flood |
| Constraint | `CON-136`, `CON-349`, `CON-621`, `CON-708` | four-Key gate, Bash edge, fixed well and safe funded Soul Link |
| Information | `INF-119` | health, energy and ability state |
| Objective | `OBJ-026` | restored-heart upper exit |
| Time | `TIM-003` | live ascent and water pressure |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `430` (`GAME-0001`–`GAME-0430`).
- Exact genome matches: none.
- Tied near matches: `GAME-0293` — Ori and the Will of the Wisps (`9 / 29 = 0.310345`).
- Supported combination subsets: none.
- Scan date: 2026-09-27.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0293` *Ori and the Will of the Wisps* | `ACT-008`, `ACT-161`, `ACT-341`, `SYS-215`, `SYS-398`, `SYS-578`, `CON-349`, `INF-119`, `TIM-003` cover directly controlled traversal, contextual route steps, live health and a retained ability gate. | The original Ginso packet adds player-placed, energy-priced Soul Link saves, opposed Bash/projectile motion and a restoration-triggered flood; the sequel's analysed opening uses automatic checkpoints, a Howl confrontation and a later Spirit Well. | Tied-near maximum, `0.310345`; not exact or a verified combination match. |

## Taxonomy impact

Six new typed boundaries (`ACT-569`, `ACT-570`, `SYS-1131`, `SYS-1132`, `SYS-1133`, `CON-708`) separate aimed Bash input, its opposed projectile result, player-chosen saving and its eligibility, and the authored rising-water response. See `TAXONOMY_CHANGE_168`. No earlier genome changes.

## Negative results

- `SYS-1032` is not reused: its definition requires an expired Worms round and Sudden Death transition, absent from Ginso.
- `SYS-369` is not reused for Soul Link: it restores an authored automatic checkpoint, not a player-placed energy-priced location.
- `CON-269` is not reused for Bash: its combat-ability mana/cooldown predicate would invent a Bash cost; eligible anchor reach is recorded within `ACT-569`.
- No claim of a legal Soul Link halfway through the flood or of an exact water-rise speed is admitted.

## Delta summary

## New facts

- [Confirmed | Corroborated | High] Original Bash sends a contacted projectile opposite Ori's chosen launch (`OBF-002`).
- [Confirmed | Corroborated | High] Soul Link is a safe-location, energy-priced player checkpoint (`OBF-003`).
- [Observation | Corroborated | High] Clearing both heart sides triggers a rising-water escape (`OBF-005`).

## New genes

- [Observation | Corroborated | High] Six new boundaries in `TAXONOMY_CHANGE_168`.

## New combinations

- [Observation | Corroborated | High] No new verified combination.

## Taxonomy changes

- [Observation | Corroborated | High] `TAXONOMY_CHANGE_168`; earlier signatures unchanged.

## New questions

- Does the original retail build prohibit a Soul Link during every flood-escape position, or only where its ordinary safe-placement condition fails? A direct Xbox One input trace could settle this; no answer is assumed here.

## Next recommended game

- [Hypothesis | Limited | Medium] `GAME-0432` *Reigns*.
- Optimisation criterion: finish this cross-platform horizon with a mobile, discrete-choice resource-balancing packet after a live platform escape.
- Expected information gain: contrast binary narrative decisions and competing reserves with player-placed checkpoint and action-platform timing.
- Backlog impact: none; the selected eighteenth unit remains reserved.

## Why this game

- [Hypothesis | Limited | Medium] The original Ginso route isolates an uncommon coupling of aimed Bash motion, opposed projectile response, player-placed save economics and a triggered flood, unlike the sequel's opening automatic-checkpoint packet.
