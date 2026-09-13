---
game_id: GAME-0272
slug: serious-sam-4
game_title: Serious Sam 4
analysis_status: reviewed
reviewed: 2026-09-07
combination_ids:
  - COMB-0235
gene_ids:
  action:
    - ACT-008
    - ACT-161
    - ACT-164
    - ACT-183
  system:
    - SYS-215
    - SYS-222
    - SYS-578
    - SYS-749
  constraint:
    - CON-285
    - CON-402
    - CON-578
  information:
    - INF-073
    - INF-115
    - INF-119
  objective:
    - OBJ-026
  time:
    - TIM-003
---

# Game: Serious Sam 4

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Parameters describe
gene instances but do not enter the signature.

## Analysis scope

- Version / ruleset: current unmodified English Windows Steam application
  `257420`, offered through four packages, observed against public branch build
  `8705708` whose branch record was updated 2022-05-20; checked 2026-09-07.
  Croteam names update `1.08` on 2021-03-24, while the later official
  2022-05-20 maintenance announcement names no semantic version. The record
  therefore preserves both facts and does not relabel the later public build as
  `1.08`.
- Product boundary: this is **Serious Sam 4** on Windows, not Serious Sam HD:
  The First Encounter, not the standalone `Siberian Mayhem` product and not any
  other entry in the series. The application lists no DLC apps.
- Platform, input and difficulty: English interface, Windows, mouse and
  keyboard, offline single-player at `Normal` difficulty on a fresh campaign
  profile.
- Entry: accept first ordinary control after the opening convoy sequence, on
  foot in the ruined-city tunnel at the start of `Death from Above`.
- Primary decision loop: read the local geometry, the visible hostile group,
  current health and armour, the active weapon, its loaded magazine and typed
  reserve; move sideways or around hostiles to preserve distance; select an
  owned weapon with compatible ammunition; aim and fire; give up fire readiness
  long enough to reload a depleted magazine; collect compatible supplies by
  walking over them; and clear each finite group released by an authored trigger
  so the mandatory route opens.
- Positive terminal: reach the declared exit threshold of `Death from Above`
  with the route's required groups cleared and enter `Death from Below`.
- Negative terminal: health reaching zero ends the attempt.
- Included: on-foot movement and strafing; aimed firing at reachable hostiles;
  selection among owned weapons; manual reload of the starting magazine-fed
  pistol; weapon-state legality; live real-time combat; damage, zero-health
  failure and contact restoration of missing health; contact collection of
  health, armour and typed ammunition on the ordinary route; authored triggers
  that release finite hostile groups; the closed area whose exit opens only once
  its required hostiles are defeated; the finite typed ammunition economy; the
  weapon, ammunition, threat, health and armour displays; and the level's exit
  threshold.
- Excluded: cooperative play and every online category; Survival; Steam
  Workshop; the S.A.M. skill tree, gadgets and dual wielding, which this route's
  sources do not establish as available inside the first level; vehicles;
  all eight secrets and the optional EDF storage side objective; later campaign
  levels; the separate `Siberian Mayhem` product; achievements and account
  progression; screenshots, official artwork, third-party assets, video and
  audio evidence.
- Reproducible parameterisation: install English app `257420`, confirm the
  public branch build, and start a fresh single-player campaign at `Normal`.
  From first control in `Death from Above`, use and reload the starting pistol,
  take damage and collect an ordinary health pickup, clear the route's authored
  hostile releases, observe at least one area whose exit opens only after its
  group is defeated, and continue through the transition into `Death from
  Below`. Exact enemy counts, weapon models, magazine sizes, damage and pickup
  values are parameters.
- Potential scoped modules: any later level; the skill tree and gadget
  ruleset; vehicle sections; cooperative play; Survival.
- Direct-play status: not conducted. Valve application data and the current
  Steam product record establish lawful availability, exact product identity,
  Windows support, the four packages, the absence of DLC apps, the
  single-player, co-op and Workshop categories and the publisher-authored
  description of the arsenal and the hostile roster. Croteam's factsheet and
  release notes establish the product boundary and the latest named version;
  the public SteamCMD projection supplies one dated secondary build
  observation. A developer answer retained on the product's Steam forum and
  independent written references establish reloading and the first-level route.
  **No video was used at any point.** No video or audio was opened, played,
  heard, analysed or used.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `SS4-001` | Steam app `257420` identifies the currently lawfully offered English Windows product, sold through four packages, with no DLC apps and single-player, co-op and Workshop categories | Confirmed | Direct | High | P1 |
| `SS4-002` | Croteam names update `1.08` on 2021-03-24; the public branch carries build `8705708`, updated alongside a later unnumbered 2022-05-20 maintenance announcement | Observation | Corroborated | High | P3, P4, S1 |
| `SS4-003` | The publisher describes an arsenal of distinct weapons used against large numbers of returning and new hostile types, with circle-strafing and backpedalling as the intended response | Observation | Direct | High | P2, P6 |
| `SS4-004` | The first campaign level begins on foot in a ruined city after the convoy sequence and proceeds through an open pillared area, a facility and street combat to a gate area | Observation | Limited | Medium | S2, S3 |
| `SS4-005` | The route's hostiles include contact-damage charging types and headless attackers released in groups | Observation | Corroborated | Medium | S2, S3 |
| `SS4-006` | An area of the route is unlocked by defeating the hostile group in front of it before the player continues into it | Observation | Limited | Medium | S2 |
| `SS4-007` | Weapons draw on typed ammunition reserves collected from the world, and the starting magazine-fed pistol must be reloaded from its compatible reserve | Observation | Corroborated | Medium | P5, S3 |
| `SS4-008` | Hostile damage reduces a continuous health pool, compatible pickups restore missing health and zero health closes the attempt | Observation | Corroborated | Medium | S3, S4 |
| `SS4-009` | Dual wielding and gadgets require unlocked skills from the game's skill tree rather than being available by default | Observation | Limited | Medium | S3, S4 |
| `SS4-010` | The level ends at a declared threshold and the campaign continues into the next authored level | Observation | Limited | Medium | S2 |
| `SS4-011` | The bounded identity is a finite authored clearance route with typed ammunition, manual magazine reload and a continuous damage-and-healing health pool | Strong Pattern | Corroborated | Medium | `SS4-004`–`SS4-010` |

## Basic data

- Release / origin: Croteam, published by Devolver Digital; released 2020-09-24.
- Platform or physical form: lawfully offered English Windows Steam application
  `257420`; one offline single-player `Normal` campaign attempt through the
  first authored level.
- Puzzle family: tactical forecast and counterplay; real-time system pressure;
  ordered dependency sequencing.
- Primary and official sources, accessed 2026-09-07:
  - **[P1]** [Valve application data](https://store.steampowered.com/api/appdetails?appids=257420&cc=ua&l=english),
    for the exact title, app, Windows support, developer and publisher, release
    date, genres with no Early Access marker, the categories, the four packages,
    the absence of DLC apps and the current Ukraine offer.
  - **[P2]** [Croteam's official factsheet](https://www.croteam.com/press/sheet.php?p=Serious_Sam_4),
    for the exact product, creators, arsenal, circle-strafing and backpedalling,
    and cooperative and Legion System features excluded from this packet.
  - **[P3]** [Croteam's official `1.08` announcement](https://www.croteam.com/page/3/),
    dated 2021-03-24.
  - **[P4]** [the official Steam announcement feed](https://steamcommunity.com/app/257420/announcements/),
    for the unnumbered Steam Deck, stability and GPU maintenance update dated
    2022-05-20.
  - **[P5]** [a Croteam developer answer retained on the product's Steam
    forum](https://steamcommunity.com/app/257420/discussions/0/2244427453119025096/),
    for reloading being retained on weapons where it supports the rules and
    removed only from named exceptions such as the single shotgun.
  - **[P6]** the publisher-authored product description returned by `P1`, for
    the weapon roster, the named hostile types and the circle-strafing
    instruction. The storefront page itself is age-gated and returns no
    description to an anonymous request, which is why the description is cited
    from the application-data response.
- Corroborating textual sources, accessed 2026-09-07. **All are secondary:**
  - **[S1]** [public SteamCMD info projection](https://api.steamcmd.net/v1/info/257420),
    for public branch build `8705708` and its 2022-05-20 branch timestamp; a
    secondary distribution observation, not a publisher claim.
  - **[S2]** [independent first-level guide](https://www.gosunoob.com/guides/serious-sam-4-level-1-secrets-death-from-above-secret-locations/),
    for the route through the tunnel, pillared area, facility, streets and gate,
    the charging contact hostiles and the area entered after its group is
    defeated. Its secret route is evidence only for geography; every secret is
    excluded from the reproducible packet.
  - **[S3]** the community-maintained Serious Sam Wiki pages for Serious Sam 4,
    the SOP38 pistol, Health and `Death from Above`, for the pistol's magazine
    and manual reload, typed ammunition, damage, health pickups, first-level
    identity and transition to the following level.
  - **[S4]** [player discussion of the weapon wheel and skill tree on the
    product's own community forum](https://steamcommunity.com/app/257420/discussions/0/2943622078758397185/),
    for weapon and gadget selection through a wheel. This is player discussion,
    not documentation.
- Source-class limitation: Croteam publishes product facts, update notes and a
  developer answer but no complete first-level manual. Route transitions,
  exact pistol state and health behaviour therefore remain secondary and are
  graded `Limited` or `Corroborated`. Video walkthroughs dominate the available
  route material and were deliberately not used.
- Reproducible control: **[V1]** repository-side transition trace across
  `P1`–`P6` and `S1`–`S4` under the declared app, package, branch, platform,
  input, difficulty, fresh profile, exclusions and terminal; rules reasoning,
  not direct play.
- Claim IDs: `SS4-001`–`SS4-011`. No audiovisual evidence was used.

## Mechanical decomposition

### Action Genes

- Existing `ACT-008`: the player advances and strafes one persistent controlled
  protagonist through the level's traversable geometry.
- Existing `ACT-161`: the player aims the active weapon at one reachable hostile
  and fires.
- Existing `ACT-164`: the player selects one owned weapon as the active hand
  through the selection wheel.
- Existing `ACT-183`: the player commits the active magazine-fed pistol to a
  timed transfer from compatible reserve ammunition, temporarily giving up fire
  readiness to refill its magazine.
- No new Action gene is admitted. Weapon models, enemy names, magazine sizes and
  reload durations are parameters. Claims: `SS4-003`–`SS4-007`.

### System Behaviour Genes

- Existing `SYS-215`: controlled and hostile combatants exchange effects in real
  time.
- Existing `SYS-222`: walking over an eligible world item transfers it into the
  carried inventory, which is how health, armour and typed ammunition are
  acquired on the ordinary route.
- Existing `SYS-578`: hostile attacks reduce one continuous health pool,
  compatible pickups restore missing health and reaching zero closes the
  attempt.
- Existing `SYS-749`: settled authored triggers instantiate finite hostile
  groups into the live encounter.
- No new System gene is admitted. Group sizes, spawn regions, health values and
  pickup contents are parameters. Claims: `SS4-004`–`SS4-008`.

### Constraint Genes

- Existing `CON-285`: firing or reloading is legal only when the active weapon,
  its magazine, the compatible reserve and the avatar's current action state
  permit that operation.
- Existing `CON-402`: an authored combat area's route exit stays closed until
  its required hostiles are defeated.
- Existing `CON-578`: an ammunition-consuming weapon fires only while its
  compatible typed reserve can pay the shot, and pickups refill that reserve to
  a fixed cap.
- Scarce resources: loaded and reserve ammunition, the health and armour pools,
  reload-safe time, and the ground between the player and charging hostiles.
  Claims: `SS4-006`–`SS4-008`.

### Information Genes

- Existing `INF-073`: the interface exposes the carried weapons, the active one
  and its typed reserve.
- Existing `INF-115`: hostiles and their projectiles are learned through the
  avatar-centred visible field. No audio cue is required by this packet.
- Existing `INF-119`: the interface exposes the protagonist's health and armour.
- Claims: `SS4-003`, `SS4-007`, `SS4-008`.

### Objective Genes

- Existing `OBJ-026`: the packet completes by navigating the controlled
  protagonist to the level's declared exit threshold once the route is
  traversably connected.
- Reaching the threshold with required groups still alive is not possible, and
  neither the optional side objective nor any secret is required. Claims:
  `SS4-006`, `SS4-010`.

### Time Genes

- Existing `TIM-003`: hostiles advance and attack while the player's inputs stay
  accepted in real time.
- Claims: `SS4-004`, `SS4-005`.

## Reproducible transitions

| Before | Action | Deterministic or bounded resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| The level has just accepted first control on foot | Move and look | The protagonist advances through the ruined-city route with an owned weapon ready | on-foot entry | `SS4-004` |
| A hostile group is released by an authored trigger | Continue | The declared finite group is instantiated and routed into the live encounter | authored release | `SS4-005` |
| A charging contact hostile is approaching | Strafe and fire | Distance and aim decide whether contact damage lands | circle-strafe response | `SS4-003`, `SS4-005` |
| The active weapon's typed reserve is empty | Attempt to fire | The shot is refused; another owned weapon with a paid reserve remains legal | typed reserve legality | `SS4-007` |
| The pistol has reserve ammunition but its magazine is depleted | Reload | Fire readiness is surrendered for the reload interval, after which compatible rounds occupy the magazine | manual reload and compatible weapon state | `SS4-007` |
| A compatible pickup lies on the route | Walk over it | Its stack transfers into the carried inventory up to the fixed cap | contact collection | `SS4-007` |
| Health is below maximum and a compatible health pickup lies on the route | Walk over it | Missing health is restored up to the pool's cap | continuous health restoration | `SS4-008` |
| Hostile damage reduces health to zero | Continue | The current attempt closes | negative terminal | `SS4-008` |
| An area's required hostile group is alive | Attempt to continue into it | The route ahead is not open | clearance gate | `SS4-006` |
| The same group is defeated | Continue | The area opens and the route proceeds | gate release | `SS4-006` |
| The route's exit threshold is reached | Cross it | The level settles and the campaign continues into the next authored level | positive terminal | `SS4-010` |

## Strategic and experiential structure

- Planning horizon: loaded rounds, typed reserves and hostile spacing form the
  plan. A weapon is chosen not only by damage but by whether its current state
  can sustain the group and where a reload interval can be afforded.
- Local tactics: keep moving and keep distance, because the route's charging
  hostiles convert standing still into contact damage.
- Medium-term structure: authored releases and clearance gates divide one fixed
  route into finite ammunition-and-health problems.
- Reversible versus irreversible: a spent round and a collected pickup are
  gone; a bad position can be changed only while health and distance remain.
- Failure attribution: the visible reserves, health and armour make a death
  traceable to a specific weapon choice or a conceded distance.
- Player trust: the gate is honest — the exit opens exactly when the declared
  group is defeated, and every release is authored rather than endless.

## Replay and variation

- What changes: weapon choice per group, reload timing, how much distance is
  conceded and which ordinary supplies are collected before the next release.
- Randomness or procedural generation: the level, its triggers and its groups
  are authored. No procedural-generation claim enters this packet.
- Multiple viable strategies: the same route is passable with a conservative
  reserve or an aggressive one.
- Typical replay motive: safer reload windows and cheaper clearance of the same
  authored groups.

## Adjacent systems and history

- Direct predecessors: `GAME-0237` Serious Sam HD: The First Encounter, whose
  scoped packet the corpus already holds.
- Variants: the separate `Siberian Mayhem` product, out of scope here.
- Similar games: the corpus's finite authored-clearance shooters.
- Important differences: this packet adds a manual magazine reload, the
  compatibility state that makes the reload legal, and a continuous
  damage-and-healing health pool to the predecessor's shared clearance
  substrate. Larger hostile counts, the city and named arsenal remain
  parameters.
- Claims: `SS4-004`–`SS4-011`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-161`, `ACT-164`, `ACT-183` | weapon models, magazine sizes and reload duration are parameters |
| System Behaviour | `SYS-215`, `SYS-222`, `SYS-578`, `SYS-749` | group sizes, spawn regions, damage and pickup values are parameters |
| Constraint | `CON-285`, `CON-402`, `CON-578` | compatibility, reserve caps and the required group are parameters |
| Information | `INF-073`, `INF-115`, `INF-119` | HUD styling is presentation |
| Objective | `OBJ-026` | the exit threshold's identity is a parameter |
| Time | `TIM-003` | frame pacing and spawn cadence are implementation |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `271` (`GAME-0001`–`GAME-0271`).
- Exact genome matches: none.
- Tied near matches: `GAME-0237` — Serious Sam HD: The First Encounter (`13 / 16 = 0.812500`).
- Supported combination subsets: `COMB-0235`.
- Scan date: 2026-09-07.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0237` — Serious Sam HD: The First Encounter | `ACT-008`, `ACT-161`, `ACT-164`, `SYS-215`, `SYS-222`, `SYS-749`, `CON-402`, `CON-578`, `INF-073`, `INF-115`, `INF-119`, `OBJ-026`, `TIM-003` | Both packets share the authored finite-group route, typed reserves, contact pickups and clearance gate. The sequel's starting pistol, however, introduces a deliberate magazine reload and compatible live weapon state, while its evidenced damage, healing and zero-health terminal instantiate the continuous health-pool boundary. Those three portable mechanics are absent from the predecessor's reviewed packet. The exact-match claim from the candidate pass was therefore an omission, not a scale distinction. | Near, `13 / 16 = 0.812500` |

- New genes: `none`.
- Classification result: `Reuse with corrected decomposition`.
- Evidence and reasoning: the selection asked whether the first level adds
  portable encounter-scale mechanics or only reuses the earlier clearance
  genome with parameters. Independent review found three portable lower-ID
  boundaries already active in the corpus: magazine reload (`ACT-183`), legal
  weapon state (`CON-285`) and continuous health loss, recovery and failure
  (`SYS-578`). The packet remains strongly related to its predecessor without
  being identical.

### Preserved research notes

- New genes: `none`.
- Classification result: `Reuse with corrected decomposition`.
- Evidence and reasoning: the selection asked whether the first level adds
  portable encounter-scale mechanics or only reuses the earlier clearance
  genome with parameters. Independent review found three portable lower-ID
  boundaries already active in the corpus: magazine reload (`ACT-183`), legal
  weapon state (`CON-285`) and continuous health loss, recovery and failure
  (`SYS-578`). The packet remains strongly related to its predecessor without
  being identical.

## Taxonomy impact

- Registry changes: none, beyond retaining this signature as a fourth supporter
  of `COMB-0235`. Sixteen genes are reused inside their existing boundaries;
  every earlier reviewed signature is untouched.
- Taxonomy-change record: none. No split, merge, deprecation, lifecycle change,
  wording generalisation or earlier signature change.
- Candidate terms affected: all product, level, weapon and enemy names remain
  parameters rather than canonical labels.
- Resolved candidate: no representation for scale is needed here because scale
  was not the differentiator. The candidate pass had omitted three ordinary
  mechanics that already have portable lower-ID genes.

## Negative results

- No video or audio evidence was used. This is the batch's clearest case where
  video would have been the easiest source, and it was refused.
- The skill tree, dual wielding and gadgets are excluded because the sources
  place them behind unlocks rather than inside the first level. If a later unit
  evidences them inside a bounded route, they are candidates for new Action and
  Constraint boundaries, not for this record.
- Vehicles and the large-scale set pieces the product advertises are excluded on
  the same rule: a mechanic advertised for the whole product is not admitted
  unless it occurs inside the declared route.
- No armour gene is admitted separately from `INF-119`'s disclosure and
  `SYS-222`'s collection. Armour mitigation remains a parameter of `SYS-578`;
  the sources do not justify the strict shield-before-health lifecycle of
  `SYS-655`.
- `ACT-419` is rejected: the ordinary first-level melee action does not require
  an evidenced stagger window. It remains inside `ACT-161`'s aimed strike
  boundary. `SYS-369` is rejected because no checkpoint restore state is
  evidenced; only zero-health attempt closure is asserted.
- `CON-262` is rejected because the packet establishes no carrying-slot or bulk
  cap. `CON-578` owns finite typed reserves and `CON-285` owns live weapon-state
  compatibility.
- No new combination is recorded. The packet does, however, become a fourth
  supporter of the already verified `COMB-0235`, because its genome contains
  that combination's ten genes; the corpus requires declared supporters to equal
  the set of carriers, so the combination's record and this signature both name
  the relation.

## Delta summary

## New facts

- [Observation | Corroborated | Medium] `SS4-001`–`SS4-011`: the sequel's first
  bounded level extends the predecessor's shared clearance substrate with a
  magazine reload, compatible live weapon state and a continuous health pool.

## New genes

- [Observation | Corroborated | Medium] `No new genes`.

## New combinations

- [Observation | Corroborated | Medium] `No new combinations`. The packet
  becomes a fourth supporter of the existing `COMB-0235`.

## Taxonomy changes

- [Observation | Direct | High] `No taxonomy changes`; no split, merge,
  deprecation, lifecycle change, wording generalisation or earlier signature
  change.

## New questions

- Which later Serious Sam 4 level, if any, first requires a boundary the
  corpus does not already hold — the skill tree, a vehicle, or the crowd scale
  the product advertises?
- Which later level first exercises the advertised crowd scale as a portable
  decision boundary rather than as a larger parameter value?

## Next recommended game

- [Hypothesis | Limited | Medium] `GAME-0273` — Max Payne 3.
- Optimisation criterion: keep the authored-route corridor but replace clearance
  with a slow-time, cover-driven third-person chapter.
- Expected information gain: test the same predecessor question against a
  product separated from its ancestor by a decade rather than by a sequel
  number.
- Backlog impact: advances the recorded 271-to-279 horizon by one unit.

## Why this game

- [Hypothesis | Limited | Medium] The selection admitted this product to ask
  whether a 2020 sequel adds encounter-scale mechanics or only reuses its
  predecessor's genome with parameters. Independent closure found the answer in
  ordinary low-level state rather than advertised scale: reload timing, weapon
  compatibility and health-state settlement distinguish the packet.
