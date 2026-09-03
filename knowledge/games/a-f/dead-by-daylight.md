---
game_id: GAME-0161
slug: dead-by-daylight
game_title: Dead by Daylight
analysis_status: reviewed
reviewed: 2026-08-27
combination_ids:
  - COMB-0159
gene_ids:
  action:
    - ACT-008
    - ACT-260
    - ACT-261
    - ACT-262
  system:
    - SYS-004
    - SYS-215
    - SYS-441
    - SYS-442
    - SYS-443
    - SYS-444
    - SYS-445
    - SYS-446
    - SYS-447
    - SYS-448
  constraint:
    - CON-388
    - CON-389
    - CON-390
    - CON-391
    - CON-392
    - CON-393
  information:
    - INF-115
    - INF-116
    - INF-119
    - INF-172
    - INF-173
    - INF-174
  objective:
    - OBJ-089
  time:
    - TIM-003
---

# Game: Dead by Daylight

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Parameters describe
gene instances but do not enter the signature.

## Analysis scope

- Version / ruleset: PC build 10.1.0, released 25 August 2026; one standard
  public `1v4` Trial from the Survivor role with no equipped Perks, Item,
  Add-ons or Offering.
- Primary decision loop: divide live attention between finding and repairing
  five of seven Generators, evading a human Killer through sight, sound and
  chase geometry, restoring or unhooking teammates, then opening a powered
  Exit Gate or taking the last-Survivor Hatch before the controlled Survivor is
  sacrificed, killed or bled out.
- Entry and exit: begin when the blank-loadout Survivor gains control at a
  sampled Trial spawn; finish when that Survivor crosses an escape boundary or
  permanently leaves the Trial through sacrifice, death, bleed-out or Endgame
  Collapse. Team spectating and the tally screen follow the exit and are not
  part of the decision loop.
- Included: four Survivors against one human Killer; sampled map and prop
  layout; direct walking, crouching, running and crawling; seven Generators,
  five-repair quota, shared repair, saved progress, Killer regression and
  Skill Checks; sight, spatial sound, Terror Radius, Scratch Marks and Pools of
  Blood; Healthy, Injured and Dying states; altruistic healing and recovery;
  Killer attacks, pickup, carry and Hooks; Hook Stages, teammate unhooking and
  sacrifice; windows, Pallets, rushed/quiet vaults, pallet stun and destruction;
  two Exit Gates, the last-Survivor Hatch and Endgame Collapse.
- Excluded: equipped Survivor or Killer Perks, Items, Add-ons and Offerings;
  character-specific Killer Powers and exhaustive status effects; Killer-role
  input analysis; self-unhook exceptions, anti-camp resolution, Keys, Totems,
  Chests, Sabotage, Mori and map-specific interactables; 2v8, Lights Out,
  limited-time events, tutorials and Custom Game modifiers; Bloodweb,
  Bloodpoints, Prestige, Archives, Quests, Rift, account rank, cosmetics,
  storefront and post-match progression; external voice/chat coordination.
- Potential scoped modules: one named Killer's complete 10.1.0 power loop; one
  perk-bearing Survivor loadout; current 2v8 or Lights Out rules; persistent
  Bloodweb and character-progression economy.
- Direct-play status: no authenticated public Trial was played for this unit.
  Behaviour's official gameplay page establishes the current 1v4 goals;
  current official-wiki mechanic records and the 10.1.0 release record
  corroborate the reproducible transitions. Exact opponent choices remain
  bounded live uncertainty rather than asserted deterministic behaviour.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `DBD-001` | Build 10.1.0 retains the standard four-Survivor-versus-one-Killer Trial alongside separately excluded modes and character content | Confirmed | Corroborated | High | P1, P2 |
| `DBD-002` | Survivors repair five of seven Generators to power two Exit Gates; shared repair is faster but incurs per-worker efficiency loss | Confirmed | Corroborated | High | P1, S1 |
| `DBD-003` | Repair and healing can emit random timed Skill Checks whose great, good or failed result changes progress and may alert the Killer | Confirmed | Corroborated | High | P1, S1, S2 |
| `DBD-004` | Running and injury produce role-exclusive temporary evidence, while the Terror Radius communicates approximate Killer proximity without exact position | Confirmed | Corroborated | High | S3, S4, S5 |
| `DBD-005` | Killer damage advances Survivor health through Healthy, Injured and Dying states; teammates can restore eligible states before terminal removal | Confirmed | Corroborated | High | S5, S6 |
| `DBD-006` | Pallets and vaults create asymmetric chase routing: a Survivor may drop or vault a Pallet, while ordinary Killers must break a dropped Pallet and vault windows more slowly | Confirmed | Corroborated | High | S7, S8 |
| `DBD-007` | Pickup and Hook resolution advances a Survivor through timed Hook Stages; a teammate can unhook before sacrifice | Confirmed | Corroborated | High | S6, S9 |
| `DBD-008` | Opening an Exit Gate or the Killer closing the last-Survivor Hatch starts Endgame Collapse, after which remaining Survivors must escape before forced sacrifice | Confirmed | Corroborated | High | S10, S11, S12 |

## Basic data

- Release / origin: Behaviour Interactive; original release 14 June 2016;
  scoped current build 10.1.0 released 25 August 2026.
- Platform or physical form: online asymmetric third-person action game; this
  scope uses the PC public-match rules.
- Puzzle family: tactical forecast and counterplay; real-time system pressure;
  agent routing and coordination; ordered dependency sequencing.
- Primary sources:
  - **[P1]** [official Dead by Daylight game and Survivor basics](https://deadbydaylight.com/game/?category=survivor),
    for the 1v4 role split, repair, evade and escape loop, five-of-seven quota,
    Skill Check failure and cooperative repair.
  - **[P2]** [official 10.1.0 release record](https://deadbydaylight.wiki.gg/wiki/Patch_Notes_10.1.X),
    for the scoped live version and separation from the earlier PTB.
- Secondary and reproducible sources:
  - **[S1]** [official-wiki Generator rules](https://deadbydaylight.wiki.gg/wiki/Generators),
    for repair, shared efficiency, saved progress, regression and gate power.
  - **[S2]** [official-wiki Skill Check rules](https://deadbydaylight.wiki.gg/wiki/Skill_Checks),
    for random prompt placement, timing input and outcome classes.
  - **[S3]** [official-wiki Terror Radius rules](https://deadbydaylight.wiki.gg/wiki/Terror_Radius),
    for proximity-layered Survivor audio and chase music.
  - **[S4]** [official-wiki Scratch Mark rules](https://deadbydaylight.wiki.gg/wiki/Scratch_Marks),
    for run-created Killer-only transient tracks.
  - **[S5]** [official-wiki Health State rules](https://deadbydaylight.wiki.gg/wiki/Injured_State),
    for Healthy, Injured and Dying transitions, bleeding and healing.
  - **[S6]** [official in-game tutorial record](https://deadbydaylight.wiki.gg/wiki/In-Game_Tutorial),
    for healing, tracking evidence, recovery, Hook rescue and the escape loop.
  - **[S7]** [official-wiki Pallet rules](https://deadbydaylight.wiki.gg/wiki/Pallets),
    for dropping, stun, destruction and fast/slow Pallet vaults.
  - **[S8]** [official-wiki Window rules](https://deadbydaylight.wiki.gg/wiki/Windows),
    for role-dependent vault speed and rushed noise.
  - **[S9]** [official-wiki Hook rules](https://deadbydaylight.wiki.gg/wiki/Hook_Stages),
    for staged sacrifice timing and teammate rescue.
  - **[S10]** [official-wiki Exit Gate rules](https://deadbydaylight.wiki.gg/wiki/Exit_Gate_Switches),
    for two gates, powering, saved switch progress and escape boundaries.
  - **[S11]** [official-wiki Hatch rules](https://deadbydaylight.wiki.gg/wiki/Hatch),
    for the last-Survivor alternative and Killer closure.
  - **[S12]** [official-wiki Endgame Collapse rules](https://deadbydaylight.wiki.gg/wiki/Endgame_Collapse),
    for activation, timer slowdown and forced terminal sacrifice.
- Claim IDs: `DBD-001`–`DBD-008`.

## Mechanical decomposition

### Action Genes

- Existing gene: `ACT-008`, directly navigate the Survivor through live map
  geometry, including current standing, crouching, running and Dying-state
  crawling.
- New genes: `ACT-260`, commit one reachable Survivor work or rescue channel
  against a Generator, teammate or gate switch; `ACT-261`, execute the prompted
  timing input inside a live skilful interaction; `ACT-262`, drop one upright
  Pallet to change the current chase route and possibly stun the Killer.
- Parameters: movement speed, posture, interaction target, progress, prompt
  zone, Pallet state, vault type and interruption.
- Claim IDs: `DBD-002`, `DBD-003`, `DBD-005`–`DBD-008`.

### System Behaviour Genes

- Existing genes: `SYS-004`, sample eligible map, spawn and prop placements;
  `SYS-215`, resolve the human Killer's directly commanded real-time attacks
  against a reachable Survivor.
- New genes: `SYS-441`, instantiate the fixed asymmetric Trial roster and one
  sampled Trial Ground; `SYS-442`, accumulate, save and regress Generator work
  until the five-repair quota powers the gates; `SYS-443`, convert one Skill
  Check timing result into progress bonus, continuation or loss plus noise;
  `SYS-444`, advance and restore the Healthy/Injured/Dying state chain;
  `SYS-445`, emit and decay role-exclusive movement and injury tracks;
  `SYS-446`, resolve window/Pallet vaults, pallet stun, blocking and Killer
  destruction; `SYS-447`, advance pickup, carry, Hook Stages, rescue and
  sacrifice; `SYS-448`, expose the Hatch when one Survivor remains and resolve
  powered gates, Hatch closure and Endgame Collapse into escape or sacrifice.
- Resolution order: the Trial samples roles, map and props; Survivors split
  between repair and rescue; every continuing skilful channel can roll a timed
  prompt; movement and injury publish different tracking evidence; Killer hits
  change health and may lead to pickup and Hook; Pallet/window choices reshape
  a live chase; five completed Generators power both gates; opening one gate or
  closing the last-Survivor Hatch starts the terminal escape clock.
- Claim IDs: `DBD-001`–`DBD-008`.

### Constraint Genes

- New genes: `CON-388`, exactly four Survivor slots oppose one Killer slot with
  fixed role authority; `CON-389`, five of seven Generators are required before
  ordinary Exit Gate interaction is legal; `CON-390`, repair, healing, rescue
  and gate work require compatible reach, body state and a continuing channel;
  `CON-391`, current health and Hook state restrict locomotion, interaction and
  rescue eligibility; `CON-392`, Survivor and Killer roles have different
  legal Pallet and window interactions; `CON-393`, escape or terminal removal
  ends this Survivor's control, and Collapse expiry sacrifices anyone left.
- Scarce strategic resources: healthy states, remaining Hook stages, time to
  rescue, intact Pallets, unrevealed movement, completed Generator distribution
  and the Endgame Collapse interval.
- Claim IDs: `DBD-001`–`DBD-008`.

### Information Genes

- Existing genes: `INF-115`, current sight and spatial sound reveal only local
  Killer state; `INF-116`, the HUD exposes teammate health/Hook state and the
  remaining Generator objective; `INF-119`, personal health, Hook and current
  action state remain visible.
- New genes: `INF-172`, layered heartbeat and Terror Radius music communicate
  approximate Killer proximity without exact location; `INF-173`, Scratch
  Marks and Pools of Blood expose transient Survivor route evidence only to
  the Killer role; `INF-174`, the current progress bar and timed Skill Check
  dial expose immediate work state and the legal response window.
- Claim IDs: `DBD-002`–`DBD-008`.

### Objective Genes

- New gene: `OBJ-089`, escape the current standard Trial through a powered Exit
  Gate or eligible last-Survivor Hatch.
- Success, evaluation and failure: crossing either legal escape boundary ends
  the Survivor's Trial successfully; sacrifice, killing, cumulative bleed-out
  or Endgame Collapse expiry permanently removes that Survivor and fails the
  scoped objective. Other teammates may independently escape or die.
- Claim IDs: `DBD-002`, `DBD-007`, `DBD-008`.

### Time Genes

- Existing gene: `TIM-003`, repair, chase, injury, healing, Hook progression
  and Collapse advance in real time while all five players retain eligible
  inputs.
- Parameters: channel durations, prompt timing, track lifetime, Hook-stage
  duration, bleed-out and Collapse slowdown.
- Claim IDs: `DBD-002`–`DBD-008`.

## Reproducible transitions

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Seven incomplete Generators exist | Hold repair alone on one reachable Generator | Progress rises and is saved when repair stops unless the Killer begins regression | persistent shared objective work | `DBD-002` |
| Two Survivors repair one Generator | Both continue repair | Combined progress is faster than solo repair, but each worker receives the declared cooperative efficiency penalty | non-linear labour allocation | `DBD-002` |
| A repair Skill Check appears | Press inside the Good, Great or miss interval | Great adds progress, Good continues, and failure loses progress, pauses work and notifies the Killer | stochastic timing-to-information coupling | `DBD-003` |
| A Survivor runs while not hidden by an exception | Continue sprinting, then stop | Killer-visible Scratch Marks persist briefly and decay after the route has changed | movement creates asymmetric evidence | `DBD-004` |
| The Killer moves closer without exact sight | Listen while retaining cover | Heartbeat layers intensify with proximity but do not disclose a coordinate | bounded threat information | `DBD-004` |
| A Healthy Survivor is hit by an ordinary attack | Killer completes the hit | The Survivor becomes Injured, gains injury evidence and remains mobile; another eligible hit reaches Dying | layered vulnerability | `DBD-005` |
| An ally is Injured or Dying and reachable | Hold the eligible healing channel | Completed work restores one allowed health state; interruption preserves or cancels progress according to that interaction | teammate restoration | `DBD-005` |
| An upright Pallet separates Survivor and Killer | Drop it as the Killer crosses the impact zone | The Pallet becomes a route blocker and may stun; the Killer may later destroy it | consumable chase geometry | `DBD-006` |
| A Dying Survivor is reachable to the Killer | Killer picks up, carries and Hooks them | The current Hook Stage begins or advances and its timer starts | injury-to-sacrifice pipeline | `DBD-007` |
| A teammate is alive on a Hook before terminal sacrifice | Hold the unhook interaction | The teammate leaves the Hook in the eligible returned health state and keeps accumulated prior Hook Stages | survivor-mediated rescue | `DBD-007` |
| Five Generators are complete | Hold one powered Exit Gate switch | Stored switch progress reaches completion, the gate opens and Endgame Collapse starts | quota-gated escape | `DBD-008` |
| One Survivor remains alive | Reach the open Hatch before Killer closure | Crossing it escapes; Killer closure instead powers gates and starts Collapse | last-Survivor alternative | `DBD-008` |
| Endgame Collapse reaches zero with the Survivor inside | Give no escape input | The Entity sacrifices the remaining Survivor and ends their Trial | hard terminal deadline | `DBD-008` |

## Strategic and experiential structure

- Local decision: hold a repair through one more possible Skill Check or leave
  before the Killer arrives; walk/crouch to conceal the route or sprint for
  distance; spend an intact Pallet now or greed another loop; heal, unhook or
  continue objective work; open the gate or return for a teammate.
- Medium-term planning: distribute five repairs to avoid a tight final cluster,
  preserve useful Pallets, track teammate Hook states, and rotate between
  exposed and safe work without giving the Killer repeated interruptions.
- Long-term structure: convert partial repairs into five completed Generators
  while preventing sacrifice from shrinking team labour, then translate the
  powered-gate phase into one personal escape before the terminal clock.
- Common heuristics: repair away from clustered teammates when pressure is low;
  break line of sight before changing direction; avoid leaving obvious Scratch
  Marks toward a hiding place; rescue before the next Hook Stage; pre-position
  near a gate as the fifth Generator completes.
- Failure attribution: the HUD exposes health, Hook state, repair count and
  current action progress, while Killer position, teammate intent and future
  Skill Check location remain deliberately partial.
- Player-trust factors: Terror Radius, injury sounds, track rules, visible
  Pallet state, Hook bars and gate lights provide causal feedback even though
  opponent choices and map sampling remain uncertain.
- Claim IDs: `DBD-002`–`DBD-008`.

## Replay and variation

- What changes between sessions: map and spawn, Generator/Pallet/window
  distribution, Killer identity, all human decisions, chase routes, repair
  order, rescue timing and terminal escape route.
- Randomness or procedural generation: the Trial samples one map and
  compatible prop layout; Skill Check occurrence and dial zone vary. Human
  Killer and teammate decisions are adversarial uncertainty, not random rules.
- Multiple viable strategies: split or cooperative repairs, stealth or chase
  diversion, early healing or objective pressure, gate escape or the solo Hatch
  can each be correct under different live states.
- Typical replay motive: learn a new map/Killer matchup, improve chase timing
  and team allocation, or solve the same escape objective under a different
  sampled layout and opponent plan.
- Claim IDs: `DBD-001`–`DBD-008`.

## Adjacent systems and history

- Direct predecessors: asymmetric hide-and-seek, tag and slasher cinema supply
  the pursuit premise; Dead by Daylight makes it a persistent repair/rescue
  economy inside one online Trial.
- Variants: perk and Item loadouts change information, speed and exceptions;
  named Killers add independent Powers; 2v8 and Lights Out alter roster or
  information rules and require separate scopes.
- Similar games: team shooters share partial opponent information and downed
  teammate recovery; stealth games share line-of-sight evasion; cooperative
  objective games share divided live labour.
- Important differences: one human role owns the lethal pursuit while four
  individually vulnerable Survivors trade repair progress, rescue time and
  consumable chase geometry under asymmetric tracking information.
- Claim IDs: `DBD-001`–`DBD-008`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-260`–`ACT-262` | interaction duration, prompt zone and Pallet geometry are parameters |
| System Behaviour | `SYS-004`, `SYS-215`, `SYS-441`–`SYS-448` | map, Killer identity, repair rates and Hook times are parameters |
| Constraint | `CON-388`–`CON-393` | roster, quota, channel, health and deadline values are parameters |
| Information | `INF-115`, `INF-116`, `INF-119`, `INF-172`–`INF-174` | HUD layout, sound mix and track duration are parameters |
| Objective | `OBJ-089` | team outcome and post-match score are excluded |
| Time | `TIM-003` | real-time cadence and timer values are parameters |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `160` (`GAME-0001`–`GAME-0160`).
- Exact genome matches: none.
- Tied near matches: `GAME-0147` — Marvel Rivals (`6 / 47 = 0.127660`).
- Supported combination subsets: `COMB-0159`.
- Scan date: 2026-08-27.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0147` — Marvel Rivals | `ACT-008`, `SYS-215`, `INF-115`, `INF-116`, `INF-119`, `TIM-003` | Marvel Rivals restores a defeated hero into a symmetric 6v6 payload fight with ability loadouts; Dead by Daylight fixes 4v1 authority and converts timed Generator work, Killer-only tracks, health and Hook stages, consumable Pallets, Gates, Hatch and Collapse into irreversible personal escape or removal | Near, `0.127660` |

### Preserved research notes

- New genes: `ACT-260`–`ACT-262`, `SYS-441`–`SYS-448`, `CON-388`–`CON-393`,
  `INF-172`–`INF-174`, `OBJ-089`.
- Classification result: `New combination of known and new genes`.
- Evidence and reasoning: generic navigation, linked-switch operation, random
  selection, directly commanded live combat, local opponent information,
  team/objective HUD, personal state and real-time scheduling fit existing
  boundaries. New genes are limited to the role-asymmetric Trial's continuous
  Survivor interaction, chase evidence, staged Hook and escape resolution.

## Taxonomy impact

- Registry changes: twenty-one new stable genes and `COMB-0159`; compatible
  evidence added to existing navigation, random, live-combat, HUD and
  real-time boundaries; memberships in `FAM-009`, `FAM-010`, `FAM-015` and
  `FAM-017`.
- Taxonomy-change record: none; no existing boundary, lifecycle or earlier
  signature changes.
- Candidate terms affected: none.

## Negative results

- No exact full-genome match is expected; the deterministic scan is recorded
  above after regeneration.
- `SYS-057` and `SYS-373` are not reused: the Killer is a human opponent, not
  an automatically rerouted patrol or suspicion-driven NPC.
- `SYS-348` and `ACT-241` are not reused: their combat-downing boundaries do
  not cover Dead by Daylight's Healthy/Injured/Dying healing chain and Hook
  rescue sequence.
- Perks, Items and Killer Powers are not flattened into the blank-loadout core
  Trial merely because they can occur in the marketed product.
