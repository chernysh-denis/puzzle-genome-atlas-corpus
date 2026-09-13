---
game_id: GAME-0274
slug: hollow-knight
game_title: Hollow Knight
analysis_status: reviewed
reviewed: 2026-09-07
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-161
    - ACT-190
    - ACT-223
    - ACT-224
  system:
    - SYS-215
    - SYS-362
    - SYS-364
    - SYS-397
    - SYS-399
    - SYS-578
    - SYS-799
  constraint:
    - CON-351
    - CON-352
  information:
    - INF-119
    - INF-317
  objective:
    - OBJ-029
  time:
    - TIM-003
---

# Game: Hollow Knight

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Parameters describe
gene instances but do not enter the signature.

## Analysis scope

- Version / ruleset: current unmodified English Windows Steam application
  `367520`, package `66613`, observed against public branch build `22529139`
  whose branch record was updated 2026-03-27; checked 2026-09-07. Team Cherry's
  `Patch Version 1.5.12620` announcement carries the same date, so this packet
  may assert that named version while still recording the build separately.
- Product boundary: **Hollow Knight**, not `Hollow Knight: Silksong`
  (`GAME-0150`). Steam-listed DLC applications, opt-in historical or beta
  branches, console releases and the later sequel are excluded.
- Platform, input and difficulty: English interface, Windows, keyboard or
  controller, offline single-player, fresh ordinary save. No selectable
  difficulty is applied.
- Entry: first ordinary control at the beginning of King's Pass, before any
  Bench has been used.
- Primary decision loop: read health Masks and current SOUL; move and jump
  through authored rooms and respond to telegraphed attacks; strike reachable
  enemies to deal damage and fund the same SOUL reserve that Focus spends;
  choose whether a stationary, interruptible Focus window is safe; rest at an
  activated Bench to recover while ordinary enemies return; and repeat those
  decisions through one declared False Knight encounter whose later phases add
  hazards after authored health and stagger thresholds.
- Positive terminal: defeat False Knight, collect the City Crest reward into
  the retained inventory state and return to an activated Bench. The terminal
  stops there; using the Crest at the City of Tears gate is outside scope.
- Negative terminal: reaching zero Masks returns the Knight to the last Bench,
  places carried Geo in one recoverable Shade and reduces the usable SOUL
  capacity until that Shade is defeated. A second death before recovery
  replaces the Shade and loses the earlier stored Geo.
- Included: fixed placed control and Focus instructions; direct movement,
  jumping and Nail strikes; timed movement responses to telegraphed attacks;
  continuous health; strike-funded SOUL; the held Focus heal and its resource
  legality; Bench rest, recovery and ordinary-enemy reset; the Shade return,
  reversible SOUL cap and one-mark replacement rule; the False Knight's later
  attack phases; encounter clearance and its retained City Crest reward.
- Excluded: using the City Crest or entering the City of Tears; Cornifer, map
  purchase and explored-map inspection; Vengeful Spirit and every later spell;
  charms, notches, shops, later regions, bosses and endings; Steel Soul and
  challenge modes; DLC union, mods, achievements and account progression;
  screenshots, official artwork, third-party visual assets, video and audio.
- Reproducible parameterisation: install English app `367520`, confirm the
  public build and named patch separately, start a fresh ordinary save, follow
  King's Pass into Dirtmouth and Forgotten Crossroads, activate and use a
  Bench, build SOUL with direct strikes, complete at least one uninterrupted
  Focus heal, enter the False Knight arena, respond to its disclosed attack
  phases, defeat it, collect the City Crest and return to the activated Bench.
  Exact room path, Geo total, received damage and healing count are parameters.
- Potential scoped modules: map purchase and navigation; Vengeful Spirit and
  later spells; charms and loadouts; City Crest consumption and later regions;
  Steel Soul and DLC content.
- Direct-play status: not conducted. Valve establishes lawful product identity
  and availability; Team Cherry's patch feed establishes the named version;
  the Team Cherry-authored English manual directly establishes controls, HUD,
  damage, death, SOUL generation, Focus and Shade recovery. A licensed physical
  listing independently confirms that the product has an authored manual. Full
  secondary textual pages establish the bounded route, Bench reset, guardian
  phases, City Crest reward and second-death replacement. No video or audio was
  opened, played, heard, analysed or used.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `HK-001` | App `367520` is the current lawfully offered Windows product and package `66613` is the scoped purchase | Confirmed | Direct | High | P1 |
| `HK-002` | Team Cherry named `Patch Version 1.5.12620` on the same date the public branch moved | Confirmed | Corroborated | High | P2, S1 |
| `HK-003` | The authored manual defines movement, jumping, Nail strikes, downward bounce and the health, SOUL and Geo displays | Confirmed | Direct | High | P3 |
| `HK-004` | Direct strikes gain SOUL and holding Focus consumes SOUL to restore missing Masks | Confirmed | Direct | High | P3 |
| `HK-005` | Zero Masks causes death; the Shade holds the Knight's power and defeating it restores Geo and full SOUL capacity | Confirmed | Direct | High | P3 |
| `HK-006` | Fixed King's Pass instructions expose controls and Focus before the bounded route reaches Dirtmouth | Observation | Corroborated | High | S3 |
| `HK-007` | Resting at a Bench saves and restores the Knight while eligible ordinary enemies return | Observation | Corroborated | High | S2, S3 |
| `HK-008` | False Knight's health and stagger thresholds advance the continuing encounter into phases with added falling hazards | Observation | Corroborated | High | S3 |
| `HK-009` | Defeating False Knight releases the City Crest as the encounter's retained key-item reward | Observation | Corroborated | High | S2, S3 |
| `HK-010` | A later death replaces the unrecovered Shade and permanently loses the Geo held by the older one | Observation | Corroborated | High | S3 |
| `HK-011` | The City Crest is a carried key consumed at a later gate, not a retained traversal capability | Observation | Corroborated | High | S3 |
| `HK-012` | The bounded predecessor shares its strike-funded active-effect reserve and recoverable-death substrate with its sequel but not the sequel's equipment layer | Strong Pattern | Corroborated | High | `HK-003`–`HK-011` |

## Basic data

- Release / origin: Team Cherry; released 2017-02-24.
- Platform or physical form: lawfully offered English Windows Steam app
  `367520`; one ordinary offline fresh-save route through the first declared
  guardian and retained reward.
- Puzzle family: world topology and perspective; tactical forecast and
  counterplay; real-time system pressure.
- Primary and official sources, accessed 2026-09-07:
  - **[P1]** [Valve application data](https://store.steampowered.com/api/appdetails?appids=367520&cc=ua&l=english),
    for exact title, app, developer, release, Windows support, single-player
    category, package and current lawful offer.
  - **[P2]** [Team Cherry's Steam announcement feed](https://api.steampowered.com/ISteamNews/GetNewsForApp/v2/?appid=367520&count=4&feeds=steam_community_announcements),
    for `Patch Version 1.5.12620` dated 2026-03-27.
  - **[P3]** [Team Cherry-authored English game manual, preserved
    copy](https://cdn.pidgi.net/images/5/51/Manual_EN_-_Hollow_Knight.pdf),
    inspected page by page for controls, HUD, health, SOUL, Focus, death and
    Shade recovery. Its copyright page identifies Team Cherry and 2017.
  - **[P4]** [licensed Fangamer physical-edition listing](https://www.fangamer.com/products/hollow-knight-switch-ps4-pc-game),
    which confirms that every physical copy includes the game manual. It is
    provenance corroboration, not the authority for mechanical rules.
- Corroborating textual sources, accessed 2026-09-07:
  - **[S1]** [public SteamCMD info projection](https://api.steamcmd.net/v1/info/367520),
    for build `22529139`, branch date and opt-in branch list.
  - **[S2]** [independent Forgotten Crossroads walkthrough](https://gamerwalkthroughs.com/hollow-knight/forgotten-crossroads/),
    for the bounded descent, Bench route, False Knight defeat, City Crest and
    later Vengeful Spirit ordering.
  - **[S3]** full textual Hollow Knight Wiki pages for
    [Focus](https://hollowknight.wiki/w/Focus),
    [Shade](https://hollowknight.wiki/w/Shade),
    [False Knight](https://hollowknight.wiki/w/False_Knight) and
    [City Crest](https://hollowknight.wiki/w/City_Crest), for fixed tutorial
    placement, interruption and cost details, Bench/death consequences,
    second-death replacement, phase changes and reward handling.
- Source-class limitation: route and second-death claims remain secondary;
  they are not promoted to primary merely because the manual covers adjacent
  rules. The manual is a primary authored artifact in a preserved mirror, not a
  current Team Cherry-hosted file; P4 independently verifies its existence.
- Reproducible control: **[V1]** repository-side transition trace across
  `P1`–`P4` and `S1`–`S3` under the declared app, build, version, platform,
  fresh-save entry, exclusions and terminal; reasoning from written evidence,
  not a claim of direct play.
- Claim IDs: `HK-001`–`HK-012`. No audiovisual evidence was used.

## Mechanical decomposition

### Action Genes

- `ACT-008`: directly move and jump the same persistent avatar through the
  authored route.
- `ACT-161`: direct one Nail strike at a reachable hostile or compatible
  fixture.
- `ACT-190`: hold the available no-target Focus capability. The canonical
  action was generalised by `TAXONOMY_CHANGE_034`; innate versus learned and
  held versus discrete are parameters.
- `ACT-223`: time a jump or position change against a telegraphed guardian
  attack inside the live sequence.
- `ACT-224`: deliberately rest at an activated Bench and accept recovery plus
  world-reset consequences.
- Claims: `HK-003`, `HK-004`, `HK-006`–`HK-008`.

### System Behaviour Genes

- `SYS-215`: hostile and controlled attacks resolve in real time.
- `SYS-362`: guardian clearance awards the retained City Crest before normal
  traversal resumes.
- `SYS-364`: Bench rest restores the declared state and repopulates eligible
  ordinary enemies.
- `SYS-397`: eligible direct strikes fund the same bounded personal reserve
  that Focus spends. Product nouns were removed by `TAXONOMY_CHANGE_034`.
- `SYS-399`: ordinary death returns the avatar to the Bench, leaves Geo in one
  recoverable Shade and applies the reversible SOUL-cap penalty.
- `SYS-578`: hostile damage and Focus healing update one continuous Mask pool;
  zero ends the current life and hands resolution to checkpoint return.
- `SYS-799`: authored health/stagger thresholds advance False Knight into later
  phases with added hazards without resetting the encounter. A visible body
  transformation became optional under `TAXONOMY_CHANGE_035`.
- Resolution order: attack contact applies damage and eligible SOUL gain;
  accepted Focus spends its cost and heals; zero health triggers the checkpoint
  and Shade state; boss thresholds extend the current attack set; final defeat
  closes the encounter and makes the City Crest reward collectable.
- Claims: `HK-003`–`HK-010`.

### Constraint Genes

- `CON-351`: Focus is legal only when the current SOUL state covers its
  declared recovery cost; accepted resolution consumes that amount. The
  portable wording is recorded in `TAXONOMY_CHANGE_034`.
- `CON-352`: only one unrecovered Shade persists; a second death replaces it
  and destroys the earlier stored Geo.
- Scarce resources: Masks, SOUL, Geo exposed by death, safe time for Focus and
  distance from the active Bench.
- Claims: `HK-004`, `HK-005`, `HK-010`.

### Information Genes

- `INF-119`: the HUD exposes current health Masks and SOUL before the next
  attack or Focus decision.
- `INF-317`: fixed authored King's Pass instructions disclose controls and the
  Focus affordance at their world positions without becoming a tracked quest.
- The packet has no explored-map gene: map purchase is explicitly outside the
  reproducible route.
- Claims: `HK-003`, `HK-006`.

### Objective Genes

- `OBJ-029`: the bounded combat objective is to incapacitate the declared
  one-member hostile set before the controlled character is defeated.
- `SYS-362` separately records the City Crest reward after encounter clearance;
  the objective does not imply use of that item at a later gate.
- Claims: `HK-008`, `HK-009`.

### Time Genes

- `TIM-003`: movement, guardian attacks, Focus interruption and resource
  resolution continue while player input remains accepted.
- Claims: `HK-004`, `HK-008`.

## Reproducible transitions

| Before | Action | Deterministic or bounded resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Fresh control begins in King's Pass | Reach a fixed instruction position | The authored control or Focus instruction is exposed without a progress chain | placed instruction | `HK-006` |
| One eligible hostile is in Nail reach | Strike it | Damage is applied and SOUL rises | attack funds reserve | `HK-003`, `HK-004` |
| Health is missing and SOUL covers the cost | Hold Focus without interruption | SOUL is consumed and one Mask is restored | active channel and resource legality | `HK-004` |
| Focus begins but an incoming hit connects | Continue | The channel is interrupted and its recovery does not complete | timing pressure | `HK-004` |
| An activated Bench is reached | Rest | The save and resources update while eligible ordinary enemies return | rest trade | `HK-007` |
| Health reaches zero | Continue | Control returns at the Bench; Geo and part of usable SOUL remain attached to a Shade at the death region | recoverable death | `HK-005` |
| The Shade is defeated | Strike it | Stored Geo and full SOUL capacity return | reversible penalty | `HK-005` |
| A second death occurs first | Continue | A new Shade replaces the old one and the older Geo is permanently lost | single-mark rule | `HK-010` |
| False Knight crosses an authored phase threshold | Continue the encounter | The same fight continues with added falling hazards | health-gated phase | `HK-008` |
| False Knight is defeated | Collect the released item | City Crest enters the retained inventory and normal traversal resumes | encounter reward | `HK-009` |
| The reward is retained | Return to the activated Bench | The bounded positive terminal is reached without using the key | reproducible stop | `HK-009`, `HK-011` |

## Strategic and experiential structure

- Planning horizon: every room beyond the Bench increases the travel and Geo
  exposed by a failed life.
- Local tactics: attacking is both offence and resource acquisition, but Focus
  converts that resource into health only through an interruptible safe window.
- Medium-term structure: Bench rest trades restored state for repopulated
  ordinary encounters; death adds a return trip and temporary reserve cap.
- Reversible versus irreversible: the SOUL cap and Shade-held Geo are
  recoverable; Geo held by a replaced Shade is not.
- Failure attribution: visible Masks and SOUL distinguish insufficient reserve
  from poor Focus timing; the unchanged encounter across boss phases exposes
  whether old positioning stopped working after the attack set expanded.
- Player trust: the manual and HUD state the resource conversion; the secondary
  source establishes the single-mark exception explicitly rather than leaving
  it to genre inference.

## Replay and variation

- What changes: route order, damage taken, Focus timing, Bench use, Geo at risk
  and which boss windows are used for recovery.
- Randomness or procedural generation: rooms, instruction positions, ordinary
  encounters and the guardian are authored; no procedural claim enters.
- Multiple viable strategies: cautious Bench-anchored movement and a longer
  uninterrupted push can both reach the declared encounter.
- Typical replay motive: defeat the guardian with fewer lost resources or
  cleaner use of its phase-specific safe windows.

## Adjacent systems and history

- Direct predecessors: none in the corpus; this is the predecessor of a game
  the corpus reviewed first.
- Variant: `GAME-0150` Hollow Knight: Silksong.
- Similar games: `GAME-0262` DARK SOULS III and other retained-death action
  routes, but the formal lower-ID scan selects the sequel.
- Important difference: both products share the strike-funded active-effect
  reserve and recoverable death mark; only the sequel packet adds purchases,
  Tool slots, selectable Crest topology, capability-gated ascent and a later
  region threshold. This predecessor packet instead exposes placed tutorial
  instructions, one continuous health pool, a phase-changing guardian and its
  immediate retained reward.
- Claims: `HK-012`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-161`, `ACT-190`, `ACT-223`, `ACT-224` | bindings, channel duration and response timing are parameters |
| System Behaviour | `SYS-215`, `SYS-362`, `SYS-364`, `SYS-397`, `SYS-399`, `SYS-578`, `SYS-799` | damage, reserve gain, cost, cap, reward and phase thresholds are parameters |
| Constraint | `CON-351`, `CON-352` | reserve predicate and stored currency are parameters |
| Information | `INF-119`, `INF-317` | HUD and instruction styling are presentation |
| Objective | `OBJ-029` | guardian identity and incapacitation predicate are parameters |
| Time | `TIM-003` | frame pacing and animation are implementation |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `273` (`GAME-0001`–`GAME-0273`).
- Exact genome matches: none.
- Tied near matches: `GAME-0150` — Hollow Knight: Silksong (`12 / 28 = 0.428571`).
- Supported combination subsets: none.
- Scan date: 2026-09-07.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0150` — Hollow Knight: Silksong | `ACT-008`, `ACT-161`, `ACT-190`, `ACT-224`, `SYS-215`, `SYS-364`, `SYS-397`, `SYS-399`, `CON-351`, `CON-352`, `INF-119`, `TIM-003` | Both packets turn direct strikes into the bounded reserve that funds active recovery, combine real-time melee with deliberate checkpoint rest and attach lost currency plus a reversible capacity penalty to one recoverable death mark. The candidate's claimed `15 / 22` subset was false: this route never buys a map, uses a capability-gated edge or crosses the next-region threshold, and its carried City Crest is expressly excluded by `SYS-398`. Conversely, this packet has fixed placed instructions, explicit continuous health, timed defensive responses, a health-gated guardian phase and its immediate encounter reward. The sequel adds its Tool/Crest economy and retained traversal capabilities. | Near, `0.428571` |

- New genes: `none`.
- Classification result: `New combination of known genes` with two accepted
  wording generalisations.
- Evidence and reasoning: every admitted mechanism survives a complete lower-ID
  transfer test. The false subset result came from importing sequel genes that
  the predecessor route does not execute while omitting established boundaries
  that primary or full-page secondary evidence does establish.

### Preserved research notes

- New genes: `none`.
- Classification result: `New combination of known genes` with two accepted
  wording generalisations.
- Evidence and reasoning: every admitted mechanism survives a complete lower-ID
  transfer test. The false subset result came from importing sequel genes that
  the predecessor route does not execute while omitting established boundaries
  that primary or full-page secondary evidence does establish.

## Taxonomy impact

- `TAXONOMY_CHANGE_034` generalises `ACT-190`, `SYS-397` and `CON-351` from
  sequel-specific or learned-only wording to portable active-capability,
  strike-funded-reserve and resource-legality boundaries.
- `TAXONOMY_CHANGE_035` makes visible guardian transformation optional in
  `SYS-799`; the invariant is a threshold that changes the attack set while the
  same sealed encounter and accumulated progress continue.
- No gene is created, merged, split, deprecated or retired. `GAME-0150`,
  `GAME-0262`, `COMB-0148` and every other earlier signature keep the same IDs.
- Candidate terms and rejected lower-ID boundaries are recorded in
  `CANDIDATE_TERMS.md`; product, character, region, resource and item names stay
  game-scoped parameters.

## Negative results

- The candidate's statement that Team Cherry publishes no manual or rules
  documentation is false. A Team Cherry-authored manual exists, is confirmed by
  the licensed physical listing and directly covers the central control,
  health, SOUL, Focus and Shade transitions.
- `SYS-398` is rejected because its own definition excludes a carried key
  consumed by one lock. City Crest is exactly that case. `CON-349` is rejected
  because the bounded terminal stops before that later gate is used.
- `INF-125` is rejected because the route excludes map purchase, while the
  manual says the map screen shows maps already owned. No owned map exists in
  the declared packet.
- `OBJ-080` is rejected because it requires crossing the newly opened threshold
  into the next region. This packet stops after the guardian reward and
  explicitly excludes City Crest use.
- `ACT-200`, `ACT-266` and `ACT-407` are item-stock actions. Focus is an innate
  active capability, so the portable lower-ID home is generalised `ACT-190`.
- `SYS-799` is admitted only for the later attack-set phases; an ordinary
  stagger with no changed later behaviour would remain excluded.
- `INF-318` is rejected because the guardian has no exposed health bar.
  `SYS-798` is rejected because SOUL is gained through strikes and spent on
  effects rather than regenerated automatically as a shared exertion budget.
- No combination is registered: none of the 269 verified sets is a subset, and
  no new repeated strict subset is established.

## Delta summary

## New facts

- [Confirmed | Direct | High] `HK-003`–`HK-005`: the authored manual directly
  establishes the central health, SOUL, Focus and Shade rules.
- [Observation | Corroborated | High] `HK-006`–`HK-011`: full textual secondary
  pages establish tutorial placement, Bench reset, guardian phases, reward and
  second-death replacement inside the declared route.

## New genes

- [Confirmed | Direct | High] `No new genes`; eighteen lower-ID Active genes
  cover the corrected packet after transfer testing.

## New combinations

- [Observation | Corroborated | High] `No new combinations`; the full verified
  combination registry was scanned and none is supported by this genome.

## Taxonomy changes

- [Confirmed | Direct | High] `TAXONOMY_CHANGE_034`: generalise `ACT-190`,
  `SYS-397` and `CON-351` without changing lifecycle or earlier signatures.
- [Observation | Corroborated | High] `TAXONOMY_CHANGE_035`: generalise
  `SYS-799` from visible transformation to the portable attack-phase change.

## New questions

- Does a later separately scoped packet justify distinguishing Shade recovery
  by combat from non-combat recovery services, or is that interaction a
  parameter of `SYS-399`?
- Would a later City Crest-use packet reuse an existing carried-key action and
  constraint without acquiring any persistent capability gene?

## Next recommended game

- [Hypothesis | Limited | Medium] `GAME-0275` — Command & Conquer Remastered
  Collection.
- Optimisation criterion: leave the single-avatar corridor for one bounded
  authored real-time command mission.
- Expected information gain: test whether the draft omitted ordinary
  selection, command, damage, clearance and information boundaries while
  over-isolating its reinforcement schedule.
- Backlog impact: advances the recorded Batch 016 closure horizon by one unit.

## Why this game

- [Hypothesis | Limited | Medium] It is the next ordered candidate and changes
  embodiment, control scale and evidence profile sharply enough to falsify
  assumptions carried from the last three action-game packets.
