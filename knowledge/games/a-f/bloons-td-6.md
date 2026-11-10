---
game_id: GAME-0265
slug: bloons-td-6
game_title: Bloons TD 6
analysis_status: reviewed
reviewed: 2026-09-06
combination_ids:
  - COMB-0263
gene_ids:
  action:
    - ACT-130
    - ACT-441
    - ACT-442
  system:
    - SYS-051
    - SYS-806
    - SYS-807
    - SYS-808
    - SYS-809
  constraint:
    - CON-062
    - CON-608
  information:
    - INF-131
    - INF-322
    - INF-323
  objective:
    - OBJ-159
  time:
    - TIM-003
---

# Game: Bloons TD 6

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Parameters describe
gene instances but do not enter the signature.

## Analysis scope

- Version / ruleset: historically recorded unmodified English Windows Steam
  application 960090, sole one-app package 313914, observed against public
  branch build 24829026 built and published 2026-08-20; checked 2026-09-06.
  Ninja Kiwi's most recent named release announcement at that observation was
  Update 56.0, dated 2026-08-06. The branch was updated fourteen days after
  that announcement, so the installed build may carry an unannounced patch
  inside the 56 line; this unit records both dates rather than asserting a
  single semantic version, and treats the numeric build identifier as a
  secondary distribution observation.
- Product boundary: this is **Bloons TD 6** on Windows, not an earlier Bloons
  Tower Defense title, a mobile release or a franchise union. The three listed
  DLC apps `2117950`, `3377850` and `4096360` are separate products outside
  this packet, and the storefront's `In-App Purchases` category covers
  monetised content that this packet excludes entirely.
- Platform, input and difficulty: English interface, Windows, mouse, offline
  single-player. The declared configuration is the `Easy` difficulty of the
  standard game mode on the beginner map `Monkey Meadow`, which starts the
  attempt with 200 lives and $650, prices towers and upgrades at 85% of their
  normal cost, moves bloons about 9% slower than `Medium`, and runs the
  authored round schedule from round 1 to round 40.
- Setup-only predecessor: a profile carrying no purchased Monkey Knowledge and
  no equipped hero. Both are separate meta-progression systems whose effects
  would change every value in this packet, so the declared attempt is made
  without them and they contribute no genes or transitions.
- Entry: accept first ordinary control on the empty `Monkey Meadow` track with
  the declared starting budget and stock, before the first placement and before
  round 1 is released.
- Primary decision loop: read the current budget, the remaining defence stock
  and the current round index together; select a type from the priced
  catalogue and position it so its drawn reach covers the stretch of the fixed
  track where it will do the most work, rejecting positions the preview marks
  illegal; buy tier upgrades along one of that defender's three parallel
  paths, accepting that raising one path past its middle tier forecloses the
  others; set each defender's target-selection rule among the declared
  options; let the placed defenders acquire and engage eligible bloons
  automatically; observe intrinsic type-specific layer/descendant resolution
  and pop credits; collect the flat credit the schedule settles when the round
  closes; accept that a bloon reaching the exit debits the stock by the layers
  it still carried; and price the next commitment against the rounds still
  remaining in the schedule.
- Positive terminal: clear the declared final round 40 of the `Easy` standard
  schedule with the defence stock still above zero, and accept the resulting
  victory state. Verify that the attempt records completion of the declared
  final round rather than stopping at an intermediate round.
- Negative terminal: the defence stock reaching zero before the final round
  ends the attempt. Individual bloons reaching the exit debit the stock;
  the attempt and current round continue only if stock remains above zero.
  A conceded leak is a legitimate cost only while that debit does not exhaust
  the stock.
- Included: priced placement of persistent defenders on legal ground; tier
  upgrades bought along parallel capped paths; per-defender target-selection
  rules; automatic target acquisition and attack by placed defenders;
  intrinsic damage-driven layer and declared zero-or-more descendant
  resolution; the stock debit equal to a leaked bloon's remaining layers; the
  budget credited per destroyed layer and the flat credit settled when each
  round closes; the round-indexed schedule releasing declared compositions
  onto the fixed track; footprint and terrain placement legality; the reach
  preview; the combined budget, stock and round display; and the final-round
  survival terminal.
- Excluded: all three DLC apps and every in-app purchase; Monkey Knowledge and
  the experience that unlocks it; heroes and their levels; co-op and every
  online mode; every other difficulty, map, game mode, challenge, odyssey,
  race, boss event and contested territory; powers and consumable insta-monkeys;
  selling or relocating a placed defender, which the declared route does not
  require and which the gathered evidence does not establish for this packet;
  water placement and the towers or enablers that permit it, which the declared
  beginner map does not provide; achievements, collection and account
  progression; screenshots, official artwork, third-party assets, video and
  audio evidence.
- Reproducible parameterisation: install English app 960090 from package
  313914, verify the declared historical branch build and its recorded
  named-update boundary, and start an offline single-player attempt on Monkey
  Meadow at Easy on the standard mode with no hero equipped and no Monkey
  Knowledge purchased. From the empty track, place at least two defenders of
  different types, observe the reach preview rejecting at least one illegal
  position, buy at least one tier on a second path of one defender until its
  declared cap is reached, change at least one defender's target-selection
  rule, allow at least one bloon to leak and observe the stock debit matching
  its remaining layers, and carry the attempt to the declared final round.
  Exact defender types, positions, purchase order, cash totals, leaked bloons
  and remaining lives are parameters.
- Potential scoped modules: another difficulty or map category; a hero ruleset;
  a Monkey Knowledge configuration; co-op; or one of the event and challenge
  modes requires its own version, entry, loop, terminal and evidence.
- Audit qualification: the existing dates and build 24829026 are frozen
  observations, not a newly certified latest release. Record the ordinary Easy
  AutoStart choice and actual start control before native verification;
  completion/readiness, UI index change and next release are not presumed
  simultaneous. Distinguish pending scheduled entries and surviving
  descendants from a truly resolved round. Layer/child composition is
  intrinsic to the damaged target, not a universal two-child or
  one-shot-per-layer rule; exact offsets, inherited state, damage carryover
  and intermediate frames remain unmeasured. No native install/run/save or
  final-round result has been inspected.
- Direct-play status: No identified native build 24829026 executable, install,
  seeded attempt, AutoStart setting, start-button input, tick/child-state
  trace, save/reload or final-round result was inspected. The Windows app
  960090/package 313914, build 24829026 and named Update 56.0 remain dated
  corpus observations, not recertified current-latest facts. During P5, an
  official SteamNews API retrieval supplied the actual publisher v32 article,
  whose conditional AutoStart paragraph is historical and boss-scoped, not
  proof of ordinary Easy 56-line controls. The old player guide was read
  through the public web reader after direct retrieval returned 429 during P5;
  it remains unfinished, player-authored and displayed as
  removed/incompatible. It illustrates descendant composition but cannot
  certify present native timing, damage carryover, exact offsets or the full
  round schedule. During P5, layer and AutoStart wiki direct retrievals
  returned 403; no fresh complete body is claimed. The independent income page
  was read and still distinguishes pop cash from flat round credit. Accepted
  `TAXONOMY_CHANGE_026/029` are preserved without an affordability gate. No
  video or audio was opened or played. During P7, the archived publisher API
  response and income HTML were hash-verified; the relevant publisher
  paragraph, player-guide text and income page were reread through the web
  reader. No fresh direct HTTP failure, API download or native configuration
  result is claimed.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `BTD-001` | Steam app `960090` and its sole one-app package `313914` identify the currently lawfully offered English Windows product, which has three separate DLC apps and an in-app-purchase surface | Confirmed | Direct | High | P1, P2 |
| `BTD-002` | The public branch carries build `24829026`, built and published 2026-08-20, while the publisher's most recent named release announcement is `Update 56.0` dated 2026-08-06 | Observation | Corroborated | Medium | P3, S1 |
| `BTD-003` | `Easy` starts with 200 lives and $650, prices towers and upgrades at 85% of normal, moves bloons about 9% slower than `Medium` and runs rounds 1 to 40 | Observation | Corroborated | High | S2, S3 |
| `BTD-004` | `Monkey Meadow` is a beginner map with ample land and no space for water towers | Observation | Corroborated | High | S2 |
| `BTD-005` | Towers are placed on land; water requires specific towers or enablers, and obstacles and unplaceable terrain refuse placement | Observation | Corroborated | Medium | S4 |
| `BTD-006` | Each tower exposes three upgrade paths of five tiers, of which at most one may pass the middle tier, a second is capped at the middle tier and the third stays unbought | Observation | Corroborated | High | S3, S5 |
| `BTD-007` | The declared target-selection rules are first, last, close and strong | Observation | Corroborated | High | S5 |
| `BTD-008` | Placed towers acquire eligible bloons in reach and attack automatically, without a player command for each shot | Observation | Corroborated | High | S5, S6 |
| `BTD-009` | Damage that destroys an outer layer resolves that target type's intrinsic local descendants, not a scheduled round; exact native offsets, carryover and intermediate visibility remain unverified | Observation | Corroborated | High | S6 |
| `BTD-010` | A bloon's remaining layer total is the number of stock units its escape costs, so a fortified or higher-layer bloon costs proportionally more | Observation | Corroborated | High | S6, S3 |
| `BTD-011` | Destroyed layers credit spendable cash, which funds placements and upgrades | Observation | Corroborated | Medium | S6, S8 |
| `BTD-016` | Popping credits `$1` per layer and completing round `n` settles a further flat `$100 + n`, so destroyed layers are not the attempt's only cash credit; tower-generated income exists but requires first buying such a tower | Observation | Limited | Medium | S8 |
| `BTD-012` | The authored schedule indexes waves by round number and releases each round's declared composition onto the map's fixed track | Observation | Corroborated | High | S2, S3 |
| `BTD-013` | Monkey Knowledge is a separate experience-unlocked progression across six trees, and at most one hero may be equipped and placed per player per game | Observation | Corroborated | High | S3, S7 |
| `BTD-014` | The authored success requires clearing the declared final round with stock remaining, rather than merely reaching its index; leaks continue only while stock remains above zero, and no exact native final-round result was observed | Observation | Corroborated | High | S2, S3, S6 |
| `BTD-015` | The bounded identity is a fixed authored schedule answered by irreversibly positioned autonomous defenders whose decision-bearing income is the same layered hostiles that debit the stock | Strong Pattern | Corroborated | High | `BTD-003`–`BTD-014`, `BTD-016` |

Documentary limits: existing evidence grades remain unchanged. Target-local
layer/descendant resolution and initial authored round entries differ in cause.
The actual ordinary Easy manual/AutoStart choice, exact completion predicate,
UI-index timing, child offsets, carryover and intermediate visibility are not
certified. The complete declared attempt still clears round 40 with stock above
zero; merely reaching its index or finding a temporarily empty track is not
sufficient. Accepted flat round credit, lack of an admitted affordability gate
and route-scoped fixed placement remain intact.

## Basic data

- Release / origin: Ninja Kiwi; developed and published on Windows by Ninja
  Kiwi and released 2018-12-17.
- Platform or physical form: lawfully offered English Windows Steam
  application `960090`; one offline single-player `Easy` standard attempt on
  the beginner map `Monkey Meadow`.
- Puzzle family: spatial assembly and packing; real-time system pressure;
  agent routing and coordination.
- Primary and official sources, accessed 2026-09-06:
  - **[P1]** [Valve application data](https://store.steampowered.com/api/appdetails?appids=960090&cc=ua&l=english),
    for the exact title, app, Windows support, developer and publisher, release
    date, the `Strategy` genre with no Early Access marker, the single-player
    and online co-op categories, the `In-App Purchases` category, the three DLC
    apps, the sole package and the current Ukraine offer.
  - **[P2]** [Valve package data](https://store.steampowered.com/api/packagedetails?packageids=313914&cc=ua&l=english),
    for package `313914` containing only app `960090` and its current Ukraine
    offer.
  - **[P3]** [Ninja Kiwi's own `Update 56.0` announcement](https://store.steampowered.com/news/app/960090),
    dated 2026-08-06, for the publisher's most recent named release and its
    declared new content. Embedded media was not opened or used.
  - **[P4]** [Publisher v32 release notes](https://store.steampowered.com/news/posts/?appids=960090&enddate=1660176375&feed=steam_community_announcements),
    actual article gid4598757090448664121 retrieved during P5 through official SteamNews
    API; historical2022 boss AutoStart context, not ordinary Easy56-line proof.
- Corroborating textual sources, accessed 2026-09-06:
  - **[S1]** [public SteamCMD info projection](https://api.steamcmd.net/v1/info/960090),
    for public branch build `24829026` and its 2026-08-20 timestamps. This
    mirrors Valve's public product data and is treated as a secondary
    distribution observation, not a publisher claim.
  - **[S2]** [static difficulty and map reference](https://bloons.fandom.com/wiki/Medium_Difficulty),
    together with its linked `Hard Difficulty` and `Monkey Meadow` pages, for
    the `Easy` starting stock of 200 lives, the $650 starting budget, the 85%
    price multiplier, the roughly 9% slower bloon speed, the rounds 1 to 40
    range, and the beginner classification of the declared map together with
    its absence of water-tower space.
  - **[S3]** [independent static rules guide](https://steamcommunity.com/sharedfiles/filedetails/?id=2427802931),
    for the same difficulty price multipliers, the `Easy` round-40 endpoint,
    the three upgrade paths of five tiers, the stock debit attached to a
    leaked bloon's layer total, and Monkey Knowledge as a separately
    experience-unlocked progression across six trees.
  - **[S4]** [static placement reference](https://bloons.fandom.com/wiki/Land),
    together with its linked `Water` and `Maps` pages, for land placement being
    the default, water requiring specific towers or enablers, and obstacles and
    covered terrain refusing placement.
  - **[S5]** [static upgrade and targeting reference](https://bloons.fandom.com/wiki/Upgrade_Path),
    together with its linked `Targeting Priority` and `Upgrades` pages, for the
    three paths, the rule that two paths may reach the middle tier while one
    path reaches the highest, and the four declared target-selection rules.
  - **[S6]** [static bloon composition reference](https://bloons.fandom.com/wiki/Bloon_Layers),
    together with its linked `Bloon`, `Red Bloon` and `Lives` pages, for the
    ordered layer stack, each layer's declared children released on damage, the
    layer total as the escape cost in stock units, and cash credited for pops.
  - **[S7]** [static hero and knowledge reference](https://bloons.fandom.com/wiki/Heroes_(BTD6)),
    together with its linked `Monkey Knowledge (BTD6)` page, for at most one
    equipped hero per player per game and for Monkey Knowledge's six separate
    unlock trees.
  - **[S8]** [static income reference](https://topper64.co.uk/nk/btd6/income),
    fetched and read in full on 2026-09-06, for the two unconditional in-attempt
    cash credits — "$1 for every pop" and "$100+n for completing round n" — and
    for its statement that "secondary sources of income can be provided by farms
    and certain upgrades of other towers". It is the only reference in this
    packet retrieved as a complete page rather than through search indexing, and
    it is a different source family from `S2`, `S4`, `S5`, `S6` and `S7`.
- Source-family limitation: `S2`, `S4`, `S5`, `S6` and `S7` are five pages of
  `bloons.fandom.com` and count as one corroborating family, not five
  independent sources. That host refuses direct retrieval from this environment,
  so those pages were reached through search indexing. `S3` was retrieved in
  full and does not document the income model at all. During P5, direct retrieval did not yield complete
  wiki bodies (403). The old S3 guide was read through the public web reader
  after direct HTTP429 during P5, remains player-authored with a removed/incompatible
  notice and an unfinished Rounds section, and is not native build evidence.
- Reproducible control: **[V1]** repository-side transition trace across
  `P1`–`P3` and `S1`–`S8` under the declared app, package, build, platform,
  input, difficulty, map, mode, clean profile, exclusions and terminal; rules
  reasoning, not direct play.
- Claim IDs: `BTD-001`–`BTD-015`. No audiovisual evidence was used.

## Mechanical decomposition

### Action Genes

- Existing `ACT-130`: spend the current budget to acquire one currently offered
  upgrade tier. The tier and path structure is a constraint on which offers are
  legal, not a second purchase action.
- New `ACT-441`: select a type from the priced catalogue and commit it to a
  chosen legal position on a map whose hostile route is already fixed and
  known. `ACT-117` binds its position to municipal service coverage, `ACT-119`
  binds its position to a running production layout, and `ACT-130` involves no
  world position at all, so none covers committing a combatant's reach against
  a known route before the threat arrives.
- New `ACT-442`: select among the declared rules deciding which eligible hostile
  a placed autonomous defender engages next. `ACT-317` assigns formation and
  stance to a directly commanded unit group whose members also move; this
  edits only the selection policy of an actor the player never commands.
- Map, tower, bloon, upgrade and exact price names remain parameters. Claims:
  `BTD-003`–`BTD-008`.

### System Behaviour Genes

- Existing `SYS-051`: placed defenders automatically select and engage eligible
  hostiles inside their reach according to the current rule and their persistent
  class, without a player command for each shot. Factorio turrets are already a
  carrier of this boundary, so no new acquisition gene is required.
- New `SYS-806`: damage resolves a target type's intrinsic local descendants,
  not a scheduled initial wave. Terminal and branching types differ; a distinct
  player hit or visible child frame per layer is not required. Exact offsets,
  inherited state, carryover and native event order remain unverified.
- New `SYS-807`: a hostile reaching the route's end is removed and debits the
  shared stock by the layers it still carried; the attempt continues unless
  that debit exhausts the stock.
- New `SYS-808`: each destroyed layer credits the shared budget the defence is
  bought from.
  [`TAXONOMY_CHANGE_026`](../../../research/taxonomy-changes/TAXONOMY_CHANGE_026.md)
  removed the exclusivity this record originally asserted: `BTD-016` establishes
  a further flat credit settled when each round closes, so destroyed layers are
  the decision-bearing income rather than the only one.
  [`TAXONOMY_CHANGE_029`](../../../research/taxonomy-changes/TAXONOMY_CHANGE_029.md)
  then removed the affordability legality the same gene stated, because a rule
  about which commitments are legal is Constraint content and this packet's
  claims do not establish one.
- New `SYS-809`: an authored finite round schedule releases initial
  compositions under the recorded start control. Distinguish manual start,
  enabled AutoStart, round resolution and UI index timing; no chosen ordinary
  build 24829026 setting or immediate release on clear is certified.
- Documentary composition, not a measured native event order: configured
  release admits authored round entries; defenders acquire and attack under
  current targeting. Damage resolves intrinsic local descendants and pop
  credit; leaks debit stock. Full round resolution, flat round credit, UI
  progress and next-round release must be distinguished, including pending
  scheduled arrivals and surviving children. Manual/AutoStart configuration
  remains to verify. Stock exhaustion fails; clearing round 40 with stock above
  zero succeeds. TAXONOMY_CHANGE_026/029 remain intact; no affordability gate
  or product-wide ban on sale/relocation is introduced.

### Constraint Genes

- Existing `CON-062`: a defender may be committed only where its static
  footprint does not overlap the track or an unplaceable terrain locus,
  including obstacles and water without an enabler. Factorio and Frostpunk
  terrain rejection are already carriers of this boundary, and `BTD-005`
  supports the terrain clause directly. This packet's sources do not establish
  the further defender-on-defender overlap rule, so that clause is not claimed
  here; the terrain clause alone satisfies the reused boundary, whose definition
  is a disjunction over placed components, terrain loci and fixed ports.
- New `CON-608`: the three parallel upgrade paths are not interchangeable, so
  raising one past its middle tier caps a second at that middle tier and leaves
  the third unbought for the rest of the attempt.
- No affordability Constraint is claimed for this packet. `ACT-130` carries the
  evidenced purchase transition — the player spends the current budget to
  acquire one offered defender or upgrade tier — and no claim in this ledger
  establishes a refusal for want of balance: `BTD-011` and `BTD-016` establish
  only that cash is credited and that placements and upgrades are what it funds,
  and the two refusals this packet does evidence are the terrain rejection
  (`BTD-005`) and the path cap (`BTD-006`), which `CON-062` and `CON-608`
  already carry. The lower-ID Constraint scan behind this decision covered every
  Active Constraint below `CON-609` mentioning affordability, cost, price,
  balance, currency, funds, payment or purchase. Every near boundary adds a
  second condition this packet does not have — `CON-248` a recurring balance and
  upkeep, `CON-261` a buy window and location, `CON-409` ledger unlocks and
  shared funds, `CON-417` city unlocks and capacity, `CON-171` municipal
  solvency and recurring service budgets, `CON-174` and `CON-180` a card cost
  with target or lane compatibility — so no reviewed Constraint fits, and a bare
  "the commitment must fit the current balance" gate is not created here because
  its evidence is missing and because introducing it would silently apply to a
  large number of unaudited economy carriers. See Negative results.
- Scarce resources: the shared budget, the shared defence stock, legal ground
  adjacent to the track, the single high-tier path per defender and the rounds
  remaining in the schedule. Exact values are parameters. Claims:
  `BTD-003`–`BTD-014`.

### Information Genes

- Existing `INF-131`: the placement preview exposes whether the current
  candidate position is geometrically legal before commitment.
- New `INF-322`: the same preview draws the reach the defender would have at
  the candidate position, so the overlap with the fixed route is visible rather
  than inferred. `INF-131` reports legality only and lists no reach parameter.
- New `INF-323`: the budget, the remaining stock and the current index within
  the finite schedule are exposed together, so a purchase can be priced against
  both the damage already absorbed and the rounds still to come. `INF-119`
  describes a controlled character's personal resources, which this packet has
  none of. A split-first review for this correction compared each value against
  the full lower-ID Information registry: `INF-117` exposes a personal economy
  and buy menu but carries neither a shared defence stock nor a finite schedule
  index; `INF-286` exposes a recovery stock and a cumulative rank rather than a
  budget; `INF-116`, `INF-224`, `INF-236`, `INF-254` and `INF-290` are the
  reviewed precedent that a bounded interface surface exposing the small set of
  values one decision loop is priced against is a single Information gene. The
  three values here are that surface, not three independently useful facts, so
  the gene is retained and only its novelty wording was corrected.
- Exact reach geometry, colours, currency formatting, icons and interface
  positions are presentation parameters. Claims: `BTD-003`, `BTD-005`,
  `BTD-011`, `BTD-012`.

### Objective Genes

- New `OBJ-159`: carry the shared stock through every round of the finite
  authored schedule to its declared final round. `OBJ-020` makes neutralising a
  finite assault force the completion predicate and explicitly excludes
  preserving a shared meter through a fixed number of rounds, which is exactly
  this packet's terminal, so it cannot be reused here.
- Reaching an intermediate round, or destroying every bloon of one round
  without carrying the stock to the final round, is not success. Claims:
  `BTD-014`, `BTD-015`.

### Time Genes

- Existing `TIM-003`: bloons advance along the route, defenders attack on their
  cadence and layers resolve in real time while placement, upgrade and rule
  inputs remain accepted.
- Claims: `BTD-008`–`BTD-012`.

## Reproducible transitions

| Before | Action | Deterministic or bounded resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| A clean `Easy` attempt is open on the empty beginner map | Accept first control before round 1 | The declared starting stock and budget are present with no hero and no purchased knowledge | fixed clean entry | `BTD-003`, `BTD-013` |
| A defender is being positioned over the track or an obstacle | Attempt to commit it | The preview refuses the position, and no budget is spent | footprint and terrain legality | `BTD-005` |
| A defender is being positioned over legal ground | Inspect the preview, then commit | The drawn reach shows which stretch of the fixed route the position would cover, and commitment fixes it there | prospective coverage | `BTD-005` |
| A placed defender has an eligible bloon inside its reach | Give no command | The defender selects a target under its current rule and attacks on its cadence | autonomous engagement | `BTD-008` |
| A placed defender's rule is changed while bloons are in reach | Select another declared rule | Its subsequent target choices follow the new rule without any engagement being commanded | selection-policy edit | `BTD-007` |
| Damage destroys one outer target layer | Resolve intrinsic composition | Resolve that type's local zero-or-more descendants; exact offsets, carryover and intermediate frames unverified | child resolution is not next-round release | `BTD-009` |
| A layer is destroyed | Resolve the pop | The budget is credited by that layer's declared value, which is the only credit the player's own decisions can raise | destruction-funded budget | `BTD-011` |
| Round `n` is fully resolved, including its scheduled arrivals and descendants | Let the round close under its rules | A flat credit of `$100 + n` is settled into the same budget regardless of how the round was played | unconditional schedule credit | `BTD-016` |
| A partly destroyed bloon reaches the exit | Let it leave | The stock is debited by the layers it still carried, which is less than an untouched bloon of the same type would cost | proportional leak cost | `BTD-010` |
| A bloon's exit debit leaves stock above zero | Continue | The round is not failed and the attempt continues | conceded leak is not a loss | `BTD-014` |
| One upgrade path has been raised past its middle tier | Attempt a high tier on a second path | The purchase is refused; the second path is capped at the middle tier and the third stays unbought | asymmetric path caps | `BTD-006` |
| Current round fully resolved under its rules; stock remains | Record AutoStart and actual start control | Manual mode may wait for start; enabled AutoStart follows its rule. No ordinary build 24829026 trace certifies choice or timing here | resolution versus release | `BTD-012`, native control verification pending |
| The declared final round closes with stock remaining | Accept the result | The attempt records completion of the declared schedule | positive terminal | `BTD-014`, `BTD-015` |
| The stock reaches zero before the final round | Continue | The attempt ends | negative terminal | `BTD-014` |

## Strategic and experiential structure

- Planning horizon: the round index and the finite schedule expose how much
  threat remains, while the budget and stock decide whether to buy coverage now
  or bank toward a high tier that only one path per defender can reach.
- Local tactics: place where the drawn reach covers the longest stretch of
  track a defender can act on, set rules so early defenders take the leading
  bloons while later ones catch what leaks past, and open a second path only up
  to its cap on defenders whose first path is already committed.
- Medium-term structure: early rounds fund the defence more than they threaten
  it, so the same wave that must be survived is also the budget for the next
  one; the caps then force each defender into a specialisation before the
  composition of the later rounds is known.
- Reversible versus irreversible: the target-selection rule is freely
  changeable, but a position and every purchased tier are committed for the
  attempt, and stock lost to a leak is never recovered.
- Failure attribution: the visible budget, stock and round index make a loss
  traceable to a specific under-covered stretch of track, a path committed too
  early or a wave conceded too cheaply, rather than to hidden state.
- Player trust: the schedule is authored and ordered, the reach is drawn before
  commitment, illegal positions are refused rather than silently accepted, and
  a conceded leak costs exactly the layers that survived.

## Replay and variation

- What changes: which defender types are placed, where, in what order, which
  paths are committed, which rules are set, how many leaks are conceded and how
  much budget is banked between rounds.
- Randomness or procedural generation: the map, the track, the round schedule
  and each round's composition are authored. No procedural-generation claim
  enters this packet.
- Multiple strategies: the schedule admits dense early coverage, a banked
  high-tier commitment, or a spread of cheap defenders with differentiated
  rules. The control demonstrates two types, one capped second path and one
  conceded leak rather than making a no-leak route the terminal.
- Typical replay motive: reach the final round having conceded less stock, or
  test whether a different single high-tier path answers the same schedule more
  cheaply.

## Adjacent systems and history

- Factorio shares automatic target acquisition by placed entities and the same
  static footprint legality, and its turrets are already a carrier of that
  acquisition boundary. Its placements serve a running production layout whose
  threat is generated by the player's own pollution; this packet's placements
  answer an authored round schedule with pop credits alongside flat
  round-completion credits; no exclusive-income claim is retained.
- Bad North: Jotunn Edition shares autonomous engagement and real-time
  resolution, but its defenders are directly commanded units that move between
  positions, and its objective is neutralising a finite assault force rather
  than outlasting a numbered schedule.
- Dota 2 shares a priced purchase action and autonomous structures that acquire
  nearby hostiles, but its towers are not placed by the player and its lane
  waves are created symmetrically for both sides.
- Mini Metro shares a preserved shared meter under scheduled pressure, but its
  commitments are reconfigurable network edges rather than irreversible
  combatant positions.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-130`, `ACT-441`, `ACT-442` | tower, upgrade, map and rule names are parameters |
| System Behaviour | `SYS-051`, `SYS-806`, `SYS-807`, `SYS-808`, `SYS-809` | layer counts, children, credits, debits and round compositions are parameters |
| Constraint | `CON-062`, `CON-608` | footprints, path count, tier caps and prices are parameters |
| Information | `INF-131`, `INF-322`, `INF-323` | reach geometry, currency formatting and interface layout are parameters |
| Objective | `OBJ-159` | schedule length, starting stock and final round are parameters |
| Time | `TIM-003` | cadence, bloon speed and round pacing are implementation |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `264` (`GAME-0001`–`GAME-0264`).
- Exact genome matches: none.
- Tied near matches: `GAME-0119` — Factorio (`3 / 35 = 0.085714`).
- Supported combination subsets: `COMB-0263`.
- Scan date: 2026-09-06.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0119` — Factorio | `SYS-051`, `CON-062`, `TIM-003` | Both let the player commit persistent entities whose static footprints must clear incompatible components and terrain, then leave those entities to acquire and engage eligible hostiles automatically while the world runs in real time. Factorio's placements exist to serve a running production layout, its hostile pressure is generated by the player's own industrial output rather than by an authored schedule, and its entities can be removed and replaced freely. This packet fixes each placement for the attempt against a route the player already knows, caps each defender's three upgrade paths asymmetrically so one commitment forecloses the others, makes layered hostiles both the only threat to a shared stock and the only income the player's own decisions can raise, and completes by outlasting a numbered schedule rather than by building anything. This is the lowest selected-neighbour score in the batch and reflects the first tower-defence packet in the corpus rather than a thin decomposition. | Near, `0.085714` |

### Preserved research notes

- New genes: `ACT-441`, `ACT-442`, `SYS-806`, `SYS-807`, `SYS-808`, `SYS-809`,
  `CON-608`, `INF-322`, `INF-323`, `OBJ-159`.
- Reused genes: `ACT-130`, `SYS-051`, `CON-062`, `INF-131`, `TIM-003`.
- Classification result: `New gene`.
- Lower-ID scan: reuse `SYS-051` for automatic acquisition rather than adding a
  turret gene, because Factorio turrets already carry that boundary; reuse
  `CON-062` for footprint and terrain legality rather than adding a
  tower-placement constraint; reuse `INF-131` for placement legality and add
  `INF-322` only for the reach disclosure it does not carry; reuse `ACT-130` for
  the upgrade purchase and express the path structure as `CON-608` rather than
  as a second purchase action. Reject `OBJ-020`, whose exclusions explicitly
  name preserving a shared meter through a fixed number of rounds. Reject
  `ACT-317`, which assigns stance to directly commanded moving units. Reject a
  bloon-, monkey-, map-, round- or currency-named gene.

## Taxonomy impact

- Registry changes: add `ACT-441`, `ACT-442`, `SYS-806`, `SYS-807`, `SYS-808`,
  `SYS-809`, `CON-608`, `INF-322`, `INF-323`, `OBJ-159` and `COMB-0263`, plus
  independent evidence for five reused genes.
- Taxonomy-change records:
  [`TAXONOMY_CHANGE_026`](../../../research/taxonomy-changes/TAXONOMY_CHANGE_026.md)
  narrowed `SYS-808` by removing the income exclusivity this record originally
  asserted, and
  [`TAXONOMY_CHANGE_029`](../../../research/taxonomy-changes/TAXONOMY_CHANGE_029.md)
  narrowed it again by removing the affordability legality it also stated, which
  was Constraint content inside a System gene. No split, merge, deprecation,
  lifecycle change or earlier signature change: the `GAME-0265` signature and
  the `COMB-0263` gene set are unchanged.
  `SYS-051` and `CON-062` are reused inside their existing boundaries with their
  definitions unchanged. `INF-131` gains this record as `Additional support` and
  its complete Ukrainian record was generalised across all three carriers, which
  is a wording and evidence change with no lifecycle or signature effect.
  `INF-323`'s novelty wording was corrected so its identity is the disclosure
  surface of one pricing decision rather than three values being useful
  together; its boundary is unchanged.
- Candidate terms: recorded in `CANDIDATE_TERMS.md`; all product, map, tower,
  bloon, upgrade, currency, app, package and build names remain parameters.

## Negative results

- No video or audio evidence was used; only official static text and data plus
  static written references support this packet.
- No affordability gene is carried by this packet at all, in either type.
  `TAXONOMY_CHANGE_029` removed the legality clause that had been folded into
  `SYS-808`, because a rule about which commitments are legal is Constraint
  content and a System gene may not hold it. No replacement Constraint was
  created: the corpus already encodes affordability per product in `CON-171`,
  `CON-248`, `CON-261` and `CON-417`, each with a second condition this packet
  lacks; a bare balance gate would silently apply to a large number of unaudited
  economy carriers; and, decisively, this record's own claims do not establish
  that a commitment is ever refused for want of balance. `ACT-130` carries the
  purchase this packet does evidence. A bare affordability Constraint and the
  refusal evidence it would need remain a recorded gap and a future audit
  candidate.
- The flat `$100 + n` credit settled when round `n` closes is recorded in
  `BTD-016` and in the transition table but is not admitted as a separate gene.
  It is unconditional: every round pays it, its value depends only on the round
  index, and no player authority, eligibility, timing or failure attaches to it,
  so within this bounded packet it is a parameter of the economy rather than a
  decision-bearing transition. Tower-generated income is excluded with it,
  because it requires first buying such a tower and the declared route does not.
  Both are listed as future audit candidates if a later carrier makes either a
  decision.
- Selling and relocating a placed defender are excluded as a bounded evidence
  gap: the declared route does not require either, and the gathered sources do
  not establish their rules for this packet. This is a recorded uncertainty,
  not a claim that the product lacks the mechanic.
- The publisher's most recent named update and the public branch update differ
  by fourteen days. Rather than assert a single semantic version, the record
  states both dates and treats the build identifier as secondary.
- Monkey Knowledge, heroes, powers, insta-monkeys and every DLC app are
  excluded even though the product exposes them elsewhere, because each would
  change the declared starting state and the values this packet depends on.
- Clearing an intermediate round is not the terminal.

## Delta summary

## New facts

- [Observation | Corroborated | High] `BTD-001`–`BTD-015`: one bounded
  tower-defence attempt answers an authored numbered schedule with
  irreversibly positioned autonomous defenders whose decision-bearing income is
  the same layered hostiles that debit its shared stock, beside a flat
  unconditional credit settled at each round's close.

## New genes

- [Observation | Corroborated | High] `ACT-441`, `ACT-442`, `SYS-806`,
  `SYS-807`, `SYS-808`, `SYS-809`, `CON-608`, `INF-322`, `INF-323`, `OBJ-159` —
  route-covering priced placement, the selection-policy edit, layer shedding
  with declared children, the proportional leak debit, the destruction-funded
  shared budget alongside flat round credits, the round-indexed schedule,
  asymmetric path caps, the reach
  disclosure, the combined budget/stock/schedule display and the
  survive-the-schedule objective.

## New combinations

- [Strong Pattern | Corroborated | High] `COMB-0263` — irreversibly positioned
  autonomous defenders funded by the layered hostiles they must outlast.

## Taxonomy changes

- [Observation | Direct | High] `TAXONOMY_CHANGE_026` and `TAXONOMY_CHANGE_029`
  narrowed `SYS-808` twice after this record was accepted, first by removing its
  income exclusivity and then by removing the affordability legality it stated
  under a System type. No split, merge, deprecation, lifecycle change or earlier
  signature change followed either.

## New questions

- Does a second tower-defence packet reuse this ten-gene core, or is the
  asymmetric path cap specific to this product's upgrade model?

## Next recommended game

- [Hypothesis | Limited | High] `GAME-0266` — Deep Rock Galactic.
- Optimisation criterion: keep the co-op-capable corridor but replace static
  placement with directly controlled traversal through fully destructible
  terrain against a deposited quota.
- Expected information gain: separate terrain-destruction traversal from the
  placement and schedule boundaries admitted here.
- Backlog impact: advances the recorded 261-to-270 horizon by one unit.

## Why this game

- [Hypothesis | Limited | High] The selection admitted this product because the
  corpus contained no tower-defence packet at all. The completed scan confirms
  the gap: at `0.085714` this is the lowest selected-neighbour score in the
  batch, and the nearest signature shares only automatic acquisition, footprint
  legality and real-time resolution.
