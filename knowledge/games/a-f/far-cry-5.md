---
game_id: GAME-0271
slug: far-cry-5
game_title: Far Cry 5
analysis_status: reviewed
reviewed: 2026-09-07
combination_ids:
  - COMB-0269
gene_ids:
  action:
    - ACT-008
    - ACT-161
    - ACT-200
    - ACT-235
    - ACT-341
  system:
    - SYS-057
    - SYS-215
    - SYS-373
    - SYS-748
    - SYS-755
    - SYS-517
  constraint:
    - CON-335
    - CON-579
    - CON-440
  information:
    - INF-115
    - INF-119
    - INF-125
    - INF-207
  objective:
    - OBJ-165
  time:
    - TIM-003
---

# Game: Far Cry 5

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Parameters describe
gene instances but do not enter the signature.

## Analysis scope

- Version / ruleset: current unmodified English Windows Steam application
  `552520`, offered through four packages, observed against public branch build
  `18766066` whose branch record was updated 2025-07-20; checked 2026-09-07.
  Ubisoft publishes no version-named release announcement for this client, so
  **no semantic version is asserted**. The application also exposes an opt-in
  `local` branch, which this packet excludes.
- Product boundary: this is **Far Cry 5** on Windows, not Far Cry 3, Far Cry
  New Dawn or any other entry in the series. The five listed DLC apps
  `763820`, `761820`, `761821`, `823990` and `874610` are separate products
  outside this packet, and the storefront's `In-App Purchases` category covers
  monetised content the packet excludes entirely.
- Platform, input and difficulty: English interface, Windows, mouse and
  keyboard, offline single-player at the default difficulty. The declared
  configuration is a fresh campaign profile with no prior progression.
- Entry: accept first ordinary control during the opening arrest sequence,
  before any weapon is carried.
- Primary decision loop: read the current objective marker, the personal health
  state and the region's liberation measure together; approach one qualifying
  site on foot; decide between an unobserved approach that keeps the
  neutralisation option legal and an open exchange that alerts the site;
  neutralise the closed hostile set, free a held civilian or destroy a declared
  cult structure; watch the resistance measure absorb whatever the activity is
  worth; and price the next approach against how much of the measure still
  separates the region from its authored successor state.
- Positive terminal: the tutorial island's liberation measure reaches its
  declared threshold, the island is recorded as liberated, and the retained
  world state offers the three main regions as selectable successors.
- Negative terminal: the protagonist's health reaching zero ends the current
  attempt; this record does not assert the retry behaviour that follows,
  because no source of the required class establishes it for this packet.
- Included: on-foot movement; direct ranged and melee attack against reachable
  hostiles; close neutralisation of an unaware hostile; the medical item that
  restores the health meter from a small carried stock; contextual interaction
  with authored fixtures, including a radio installation and a supply cache's
  power and drainage controls; autonomous hostile perception, pursuit and the
  escalation from suspicion to an alerted site that calls further hostiles;
  destruction of declared cult structures and of explosive containers; the
  conversion of a cleared site into allied ownership with its retained services;
  the single regional measure that every qualifying activity credits; the
  interface that exposes that measure and its next gate; and the liberation
  terminal.
- Excluded: two-player co-op and every online category; Far Cry Arcade and its
  level editor; all five DLC apps and every in-app purchase; the three main
  regions and the remainder of the campaign; Guns for Hire and Fangs for Hire
  companions, which the packet's sources do not place inside this island;
  vehicles, hunting, fishing, wingsuit traversal and the perk economy, which are
  named as potential scoped modules rather than admitted; New Game Plus;
  achievements and account progression; screenshots, official artwork,
  third-party assets, video and audio evidence.
- Reproducible parameterisation: install English app `552520`, confirm the
  public branch build, and start a fresh single-player campaign. From first
  control, complete the opening sequence, reach the tutorial island, free at
  least one held civilian, destroy at least one declared cult structure, clear
  at least one occupied site while observing both the alerted and the unobserved
  resolution, and continue until the island's measure reaches its threshold.
  Exact site names, civilian counts, weapon models, structure types and point
  values are parameters.
- Potential scoped modules: any of the three main regions; the companion
  ruleset; the perk economy; vehicles and aircraft; Arcade; co-op. Each would
  require its own version, entry, loop, terminal and evidence.
- Direct-play status: not conducted. Valve application data and the current
  Steam product record establish lawful availability, exact product identity,
  Windows support, the four packages, the single-player and co-op categories,
  the level editor, the in-app-purchase surface and the five separate DLC apps.
  Ubisoft's own product page establishes the setting, the resistance framing,
  the companion systems and co-op. The public SteamCMD info projection supplies
  one dated secondary build observation. **Every mechanical claim below rests on
  independent secondary written references, not on publisher documentation**,
  because Ubisoft publishes no manual or support article describing this
  packet's rules; that limitation is stated per claim and in the source
  register. This is an evidence-backed rules reconstruction, not a claimed
  playthrough or entitlement. No video or audio was opened, played, heard,
  analysed or used.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `FC5-001` | Steam app `552520` identifies the currently lawfully offered English Windows product, sold through four packages, with five separate DLC apps, an in-app-purchase surface, a level editor and single-player plus co-op categories | Confirmed | Direct | High | P1, P2 |
| `FC5-002` | The public branch carries build `18766066`, whose branch record was updated 2025-07-20, and an opt-in `local` branch exists; no publisher announcement names a client version | Observation | Corroborated | Medium | S1, P3 |
| `FC5-003` | The publisher describes the product as liberating a county from a doomsday cult, with recruitable human and animal companions and two-player co-op | Observation | Direct | High | P2, P4 |
| `FC5-004` | The opening sequence starts the protagonist without weapons and equips a melee weapon and then firearms from the world before the island section | Observation | Limited | Medium | S2 |
| `FC5-005` | An unaware hostile within reach can be neutralised silently instead of being shot | Observation | Corroborated | Medium | S2, S5 |
| `FC5-006` | Occupied sites raise an alarm when the player is detected; the alarm calls further hostiles and forfeits the undetected bonus | Observation | Corroborated | Medium | S5, S4 |
| `FC5-007` | Liberating an occupied site transfers it to the resistance and opens quests, shops and a fast-travel point there | Observation | Corroborated | Medium | S4, S3 |
| `FC5-008` | Civilians held by the cult can be freed, and the island's final act is operating a radio installation; a supply cache is opened by restoring power and draining water with a valve | Observation | Limited | Medium | S3 |
| `FC5-009` | Declared cult structures are destroyed by damage, including by detonating nearby containers, and a destroyed structure counts toward the region's measure | Observation | Corroborated | Medium | S3, S4 |
| `FC5-010` | A carried medical item restores the health meter, and the carried stock is small and finite | Observation | Corroborated | Medium | S4, S2 |
| `FC5-011` | Four qualitatively different activities — freeing captives, destroying cult property, completing radio missions and liberating occupied sites — all credit one regional resistance measure | Observation | Corroborated | High | S3, S4 |
| `FC5-012` | Filling the tutorial island's measure liberates the island and opens the three main regions as selectable successors | Observation | Corroborated | Medium | S3, S4 |
| `FC5-013` | The bounded identity is a region whose authored successor is bought with one measure that several unrelated activities all pay into, so the player chooses *which kind* of resistance to perform rather than following one ordered task list | Observation | Corroborated | Medium | `FC5-004`–`FC5-012` |

## Basic data

- Release / origin: Ubisoft; developed by Ubisoft Montreal with Red Storm,
  Ubisoft Shanghai, Ubisoft Toronto and Ubisoft Kiev; released 2018-03-26.
- Platform or physical form: lawfully offered English Windows Steam application
  `552520`; one offline single-player fresh campaign through the tutorial
  island's liberation.
- Puzzle family: tactical forecast and counterplay; real-time system pressure;
  ordered dependency sequencing.
- Primary and official sources, accessed 2026-09-07:
  - **[P1]** [Valve application data](https://store.steampowered.com/api/appdetails?appids=552520&cc=ua&l=english),
    for the exact title, app, Windows support, developer and publisher, release
    date, the `Action` and `Adventure` genres with no Early Access marker, the
    single-player, co-op, level-editor and in-app-purchase categories, the four
    packages, the five DLC apps and the current Ukraine offer.
  - **[P2]** [Steam product record](https://store.steampowered.com/app/552520/),
    for the publisher-authored description and the listed feature set.
  - **[P3]** [Ubisoft's own news feed for the application](https://api.steampowered.com/ISteamNews/GetNewsForApp/v2/?appid=552520&count=4&feeds=steam_community_announcements),
    for the absence of any version-named release announcement; the most recent
    entries are a discount and a 2024-12-17 achievements post.
  - **[P4]** [Ubisoft's official product page](https://www.ubisoft.com/en-us/game/far-cry/far-cry-5),
    for the setting, the resistance framing, recruitable allies and co-op.
- Corroborating textual sources, accessed 2026-09-07. **All are secondary.**
  None is publisher documentation, and this packet has none:
  - **[S1]** [public SteamCMD info projection](https://api.steamcmd.net/v1/info/552520),
    for public branch build `18766066`, its branch update timestamp and the
    existence of the opt-in `local` branch. This mirrors Valve's public product
    data and is a secondary distribution observation.
  - **[S2]** [independent prologue walkthrough](https://www.gamepressure.com/far-cry-5/the-warrant-no-way-out/z7ac03),
    for the unarmed start, the acquisition of a melee weapon and then firearms,
    the explosive containers used against hostiles and the use of cover when
    health is low.
  - **[S3]** [independent island-liberation guide](https://www.dualshockers.com/far-cry-5-liberate-dutchs-island/),
    for the four qualifying activities, freeing held civilians, destroying cult
    structures and their gas hazard, the supply cache's power and valve steps,
    the radio installation as the final act and the three regions offered
    afterwards.
  - **[S4]** search-indexed summaries of two further independent guides on perks,
    healing and regional progression, for the finite medical stock, the transfer
    of a liberated site to the resistance with quests, shops and fast travel, and
    the statement that story missions, site liberation, side missions, property
    destruction and rescues all credit the same measure.
  - **[S5]** [player discussion of site alarms on the product's own community
    forum](https://steamcommunity.com/app/552520/discussions/0/3211505894145229870/),
    for alarms calling reinforcements and for the undetected bonus being
    forfeited once an alarm is raised. This is player discussion, not
    documentation.
- Source-class limitation, recorded in the unit that created this record:
  Ubisoft hosts no manual, in-game help reproduction or support article covering
  this packet's rules, and searches for one on the publisher's support domain
  returned none. Every mechanical claim therefore rests on secondary written
  references and is graded `Limited` or `Corroborated` accordingly; none is
  presented as official. `S4` is recorded as a search-indexed summary rather
  than as pages this unit fetched in full.
- Reproducible control: **[V1]** repository-side transition trace across
  `P1`–`P4` and `S1`–`S5` under the declared app, package, branch, platform,
  input, mode, fresh profile, exclusions and terminal; rules reasoning, not
  direct play.
- Claim IDs: `FC5-001`–`FC5-013`. No audiovisual evidence was used.

## Mechanical decomposition

### Action Genes

- Existing `ACT-008`: the player advances one persistent controllable
  protagonist through the island's traversable geometry on foot.
- Existing `ACT-161`: the player aims the equipped melee or ranged tool at one
  reachable hostile and commits a strike or shot.
- Existing `ACT-235`: from close range outside active detection, the player
  neutralises one unaware hostile instead of shooting it. `ACT-161` covers the
  ordinary attack; this boundary is specifically the unaware-target
  neutralisation, and `CON-335` carries its legality.
- Existing `ACT-200`: the player uses one carried medical item and receives its
  restoration.
- Existing `ACT-341`: the player addresses one reachable authored fixture and
  commits its legal interaction — operating the radio installation, restoring a
  cache's power, opening its drainage valve, or freeing a held civilian.
- No new Action gene is admitted. Weapon models, site names, structure types and
  civilian counts are parameters. Claims: `FC5-004`, `FC5-005`, `FC5-008`,
  `FC5-010`.

### System Behaviour Genes

- Existing `SYS-057`: an autonomous hostile abandons its route when it perceives
  the protagonist and pursues.
- Existing `SYS-215`: directly controlled combat resolves in real time.
- Existing `SYS-373`: hostile perception fills a local suspicion state, and
  completed detection alerts the site. Here the alerted state additionally
  summons further hostiles and forfeits the site's unobserved bonus, which are
  parameters of the same escalation rather than a second gene.
- Existing `SYS-748`: clearing the closed hostile set at an occupied site
  transfers local ownership to the allied faction and retains that site's
  declared services. Far Cry 3 is already a carrier; this record reuses the
  boundary unchanged, with quests, a shop and a fast-travel point as the
  retained affordances.
- Existing `SYS-755`: accepted damage removes an eligible world object once its
  break threshold is reached, including via a detonated container.
- Existing `SYS-517`: every qualifying resistance activity, whatever kind it
  is, credits one shared retained progression measure. The historical candidate
  `SYS-819` was merged into `SYS-517` by `TAXONOMY_CHANGE_033` after the older
  record's driving-event and festival wording proved to be parameters.
  Independent closure review applied the two-way transfer test:
  both products accept completed eligible activities, add configured amounts to
  one retained measure and test a later gate; activity type, region and currency
  are parameters. `TAXONOMY_CHANGE_033` therefore generalises the lower ID and
  merges the candidate duplicate before review acceptance.
- Resolution order: the player acts at one site; hostile perception resolves
  first and may alert the site and call reinforcements; the activity then
  resolves — a hostile set cleared, a captive freed, a structure destroyed; the
  regional measure absorbs the activity's declared value; and the region's
  authored successor becomes available once the measure crosses its threshold.
  Claims: `FC5-005`–`FC5-012`.

### Constraint Genes

- Existing `CON-335`: the silent neutralisation stays legal only while the
  target is reachable and has not completed detection.
- Existing `CON-579`: the medical item may be used only against a health meter
  that is actually missing and only from the small carried stock.
- Existing `CON-440`: the region's next authored stage is unavailable until its
  liberation measure reaches the declared total. The historical candidate
  `CON-614` was merged into `CON-440` by `TAXONOMY_CHANGE_033`: it stated no
  additional legality, and its regional measure name and several successors are
  parameters.
- Scarce resources: the small medical stock, the protagonist's health, the
  unobserved approach itself — spendable exactly once per site — and the
  remaining distance between the measure and its threshold. Exact values are
  parameters. Claims: `FC5-005`, `FC5-006`, `FC5-010`, `FC5-012`.

### Information Genes

- Existing `INF-115`: the player learns hostile positions and states through
  avatar-centred sight and sound.
- Existing `INF-119`: the interface exposes the protagonist's health and carried
  personal state.
- Existing `INF-125`: the discovered map exposes travel points and the current
  authored objectives, including the successor regions once they open.
- Existing `INF-207`: the region interface exposes the accumulated liberation
  measure, its threshold and the next authored gate, so the player can price an
  activity before performing it. The historical candidate `INF-328` was merged
  into `INF-207` by `TAXONOMY_CHANGE_033`: it disclosed the same three facts,
  while styling, measure name and successor identity are parameters.
- Exact meter styling, marker art, colours and interface positions are
  presentation parameters. Claims: `FC5-006`, `FC5-010`, `FC5-011`, `FC5-012`.

### Objective Genes

- New `OBJ-165`: raise one region's liberation measure to its declared threshold
  and retain the opened successor choice. `OBJ-147` completes one site and
  retains that site's services, which this packet also contains but which is not
  its terminal; `OBJ-150` and `OBJ-159` settle a single event or a fixed wave
  schedule. None ends on a regional measure whose payers are heterogeneous.
- Clearing one site, freeing one captive or destroying one structure is not
  success while the measure is short of its threshold. Claims: `FC5-011`,
  `FC5-012`, `FC5-013`.

### Time Genes

- Existing `TIM-003`: hostiles patrol, perceive and fight while the player's
  inputs stay accepted in real time.
- Claims: `FC5-004`–`FC5-009`.

## Reproducible transitions

| Before | Action | Deterministic or bounded resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| A fresh campaign has just accepted first control | Move and look | The protagonist advances on foot with no weapon carried | unarmed entry | `FC5-004` |
| A melee weapon and then a firearm are reachable in the world | Take them | The protagonist gains an equipped tool and can attack reachable hostiles | armament progression | `FC5-004` |
| One hostile has not perceived the protagonist and is within reach | Commit the close neutralisation | The hostile is removed without a shot and without alerting the site | unaware-target legality | `FC5-005`, `FC5-002` |
| The same hostile has completed detection | Attempt the close neutralisation | It is not available; the ordinary attack is | detection closes the option | `FC5-005` |
| A hostile at an occupied site perceives the protagonist | Continue | Suspicion completes into detection, the site is alerted, further hostiles are called and the unobserved bonus is forfeited | escalation and reinforcement | `FC5-006` |
| The site's closed hostile set is cleared | Let the site settle | Ownership transfers to the resistance and the site retains quests, a shop and a fast-travel point | site conversion | `FC5-007` |
| A declared cult structure is within weapon range | Damage it, directly or by detonating a nearby container | The structure is destroyed once its threshold is reached | damage-threshold destruction | `FC5-009` |
| A civilian is held by cult members | Neutralise the captors and address the civilian | The civilian is freed | captive release | `FC5-008` |
| Any of the four qualifying activities completes | Read the region interface | The regional measure has risen by that activity's declared value | one measure, several payers | `FC5-011` |
| The measure is below the region's threshold | Approach the successor stage | It is unavailable | threshold legality | `FC5-012` |
| The measure reaches the threshold | Continue | The island is recorded as liberated and the three main regions are offered as successors | positive terminal | `FC5-012`, `FC5-013` |
| The protagonist's health is critical | Use a carried medical item | The health meter is restored and the carried stock falls | finite restoration | `FC5-010` |

## Strategic and experiential structure

- Planning horizon: the measure and its threshold turn the island into a budget
  problem. The player decides how to buy the remaining distance rather than
  which mission comes next.
- Local tactics: approach unobserved while the neutralisation is legal, because
  the same site costs materially more once it is alerted and calls further
  hostiles.
- Medium-term structure: activity classes are substitutable. A player who finds
  sites expensive can pay in freed captives and destroyed structures instead,
  and the interface prices that choice before it is made.
- Reversible versus irreversible: a converted site and a destroyed structure are
  permanent for the attempt; the unobserved approach is spent the moment
  detection completes.
- Failure attribution: the visible measure and health make a loss traceable to a
  specific alerted approach or an exhausted medical stock rather than to hidden
  state.
- Player trust: the threshold is disclosed before it is paid, and every
  qualifying activity is visibly worth something.

## Replay and variation

- What changes: which activity classes the player uses, in which order, and how
  many approaches stay unobserved.
- Randomness or procedural generation: the island, its sites and its structures
  are authored. No procedural-generation claim enters this packet.
- Multiple viable strategies: the same threshold is reachable through site
  liberation alone, through rescues and destruction alone, or through any mix.
- Typical replay motive: paying the same threshold more cheaply.

## Adjacent systems and history

- Direct predecessors: `GAME-0236` Far Cry 3, whose scoped first outpost already
  carries `SYS-748` and `OBJ-147`.
- Variants: the series' later entries, none of which is in scope here.
- Similar games: the corpus's stealth-and-outpost cluster.
- Important differences: Far Cry 3's scoped packet ends at a converted site;
  this packet's terminal is a regional measure that the site merely pays into.
- Claims: `FC5-007`, `FC5-011`, `FC5-013`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-161`, `ACT-200`, `ACT-235`, `ACT-341` | weapon models, fixture identities and civilian counts are parameters |
| System Behaviour | `SYS-057`, `SYS-215`, `SYS-373`, `SYS-517`, `SYS-748`, `SYS-755` | activity class, alarm timing, reinforcement size, structure durability and point values are parameters |
| Constraint | `CON-335`, `CON-440`, `CON-579` | carried stock size, successor identity and the threshold total are parameters |
| Information | `INF-115`, `INF-119`, `INF-125`, `INF-207` | meter styling, measure name and marker art are presentation |
| Objective | `OBJ-165` | region identity and successor count are parameters |
| Time | `TIM-003` | frame pacing and patrol cadence are implementation |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `270` (`GAME-0001`–`GAME-0270`).
- Exact genome matches: none.
- Tied near matches: `GAME-0236` — Far Cry 3 (`13 / 37 = 0.351351`).
- Supported combination subsets: `COMB-0269`.
- Scan date: 2026-09-07.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0236` — Far Cry 3 | `ACT-008`, `ACT-161`, `ACT-200`, `ACT-235`, `SYS-057`, `SYS-215`, `SYS-373`, `SYS-748`, `CON-335`, `INF-115`, `INF-119`, `INF-125`, `TIM-003` | Both advance one protagonist on foot through hostile-held terrain, attack reachable hostiles in real time, neutralise unaware hostiles under the same legality, escalate perception into detection, convert a cleared occupied site into a retained allied node, restore health from a carried item and expose the same avatar-centred, personal and map information. Far Cry 3's scoped packet ends when one occupied site is cleared and its services are retained, so its objective is the site. This packet keeps the site conversion but subordinates it: the terminal is a regional measure that four unrelated activity classes all pay into, and the site is one payer among them. The shared core is the stealth-and-clearance substrate; what the two packets are *about* differs at the objective. | Near, `0.351351` |

- New genes: `OBJ-165`.
- Reused with a boundary generalisation: `SYS-517`, `CON-440`, `INF-207`.
- Classification result: `Reuse plus one new objective`.
- Evidence and reasoning: the earlier Forza-specific labels hid three portable
  boundaries already present in the corpus — credit eligible completed work to
  one retained measure, gate a successor on its threshold and disclose both.
  `OBJ-165` remains new because this packet ends at the resolved-region state
  and the opened successor choice, rather than at one contributing activity or
  at a later mandatory event.

### Preserved research notes

- New genes: `OBJ-165`.
- Classification result: `Reuse plus one new objective`.
- Evidence and reasoning: the earlier Forza-specific labels hid three portable
  boundaries already present in the corpus — credit eligible completed work to
  one retained measure, gate a successor on its threshold and disclose both.
  `OBJ-165` remains new because this packet ends at the resolved-region state
  and the opened successor choice, rather than at one contributing activity or
  at a later mandatory event.
- Evidence and reasoning: nineteen of the twenty boundaries are reused. Three
  of those reuses were exposed by closure review and are governed by
  `TAXONOMY_CHANGE_033`; thirteen remain shared with the reviewed predecessor.

## Taxonomy impact

- Registry changes: retain new `OBJ-165`; generalise lower-ID `SYS-517`,
  `CON-440` and `INF-207`; preserve the three superseded candidate IDs as
  auditable `Merged` aliases.
- Taxonomy-change record:
  [`TAXONOMY_CHANGE_033`](../../../research/taxonomy-changes/TAXONOMY_CHANGE_033.md)
  merges the historical candidates `SYS-819`, `CON-614` and `INF-328` into
  `SYS-517`, `CON-440` and `INF-207`. It changes no previously reviewed
  signature: `GAME-0171` already carries all three survivor IDs, `GAME-0236` is
  untouched, and this draft signature alone replaces the aliases before
  promotion.
- Candidate terms affected: recorded in `CANDIDATE_TERMS.md`; all product,
  region, site, structure, weapon and currency names remain parameters.
- Candidate-pass audit questions are resolved here: the product-specific nouns
  in `SYS-517`, `CON-440` and `INF-207` were parameters, not evidence of
  mechanically distinct genes.
- Combination consequence: `COMB-0269` records the three-gene interaction now
  evidenced by both Forza Horizon 6 and Far Cry 5. It is a strict proper subset
  of both genomes and does not absorb either game's distinct terminal.

## Negative results

- No video or audio evidence was used; only official product data and
  independent secondary written references support this packet.
- **This packet has no publisher documentation at all.** Ubisoft's product page
  describes setting and features but states no rule; the news feed names no
  client version; no manual or support article covering these mechanics was
  found. Every mechanical claim is therefore secondary and graded accordingly,
  and the record says so rather than presenting a guide as official.
- Companions, vehicles, hunting, fishing, the perk economy and the wingsuit are
  excluded as outside the packet: the publisher advertises them for the product,
  but this record's sources do not place them inside the tutorial island's
  route, and a mechanic advertised for the whole product is not admitted.
- No checkpoint-restore gene is admitted. The sources establish that health can
  reach zero but do not establish what the retry restores, so the failure
  behaviour is recorded as an evidence gap rather than covered by `SYS-369`.
- No perk gene is admitted, for the same reason: perk points are attested for
  the product but not evidenced as earned or spent inside this island's route.
- The lower-ID System rescan covered every Active record whose label or body
  mentions progress, threshold, milestone, unlock, region, territory or
  reputation. `SYS-171` converts an exact delivery quota; `SYS-262` accumulates
  staffed science; `SYS-503` settles extraction into mission progress; and
  `SYS-405` settles a completed hunt. They remain outside the boundary.
  `SYS-517`, however, differs only in the kinds of eligible activity and the
  product name of the measure, so the historical candidate `SYS-819` is merged
  into it under `TAXONOMY_CHANGE_033`.
- The lower-ID scan behind `OBJ-165` covered `OBJ-147`, `OBJ-150`, `OBJ-159`,
  `OBJ-081` and `OBJ-164`. Each ends on a site, an event, a wave schedule, an
  ordered hunt list or a region exit, not on a measure.
- No new combination is recorded. This batch admits a combination only where the
  interaction has at least two supporting games, and the interaction this packet
  is about currently has one carrier.

## Delta summary

## New facts

- [Observation | Corroborated | Medium] `FC5-001`–`FC5-013`: one bounded
  tutorial region is liberated by filling a single disclosed measure that four
  unrelated activity classes all credit.

## New genes

- [Observation | Corroborated | Medium] `OBJ-165` — the terminal that resolves
  one bounded region by filling its retained measure and preserving the opened
  successor choice. `SYS-517`, `CON-440` and `INF-207` are reused after the
  portable generalisation recorded in `TAXONOMY_CHANGE_033`.

## New combinations

- [Pattern | Corroborated | High] `COMB-0269` records the cross-product
  interaction exposed by normalisation: unlike completed activities fill one
  retained measure, its next threshold gate is disclosed, and the successor
  remains unavailable below that threshold. Forza Horizon 6 and Far Cry 5 are
  mechanically independent carriers.

## Taxonomy changes

- [Observation | Direct | High] `TAXONOMY_CHANGE_033` generalises `SYS-517`,
  `CON-440` and `INF-207`, then merges candidate duplicates `SYS-819`,
  `CON-614` and `INF-328`. No previously reviewed signature changes.

## New questions

- Which later product will provide a third carrier for the generalised
  progression-credit, threshold and disclosure boundaries?

## Next recommended game

- [Hypothesis | Limited | Medium] `GAME-0272` — Serious Sam 4 closure review.
- Optimisation criterion: keep the first-person corridor but replace territorial
  liberation with a finite authored clearance route.
- Expected information gain: separate the clearance substrate from the
  region-measure boundaries admitted here.
- Backlog impact: advances the recorded 271-to-279 horizon by one unit.

## Why this game

- [Hypothesis | Limited | Medium] The selection admitted this product to test
  whether an already reviewed relative, `GAME-0236`, carries its successor's
  mechanics. Nineteen reused genes and one new objective answer the question:
  the moment-to-moment substrate recurs, and the region-level objective does
  not.
