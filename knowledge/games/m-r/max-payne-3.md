---
game_id: GAME-0273
slug: max-payne-3
game_title: Max Payne 3
analysis_status: reviewed
reviewed: 2026-09-07
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-161
    - ACT-164
    - ACT-183
    - ACT-199
    - ACT-226
    - ACT-229
    - ACT-341
    - ACT-131
  system:
    - SYS-208
    - SYS-215
    - SYS-368
    - SYS-369
    - SYS-578
    - SYS-780
    - SYS-820
  constraint:
    - CON-262
    - CON-269
    - CON-282
    - CON-285
    - CON-326
    - CON-579
  information:
    - INF-073
    - INF-115
    - INF-119
    - INF-268
  objective:
    - OBJ-155
  time:
    - TIM-003
---

# Game: Max Payne 3

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Parameters describe
gene instances but do not enter the signature.

## Analysis scope

- Version / ruleset: current unmodified English Windows Steam application
  `204100`, offered through the single package `14903`, observed against public
  branch build `17939828` whose branch record was updated 2025-04-01; checked
  2026-09-07. Rockstar Support currently surfaces PC title update
  `v1.0.0.272`; no equivalence between that named patch and the later Steam
  Build ID is asserted.
- Product boundary: this is **Max Payne 3** on Windows, not Max Payne (2001) and
  not Max Payne 2. The current storefront record describes this as the complete
  edition, which packages the original game together with previously released
  downloadable multiplayer content in the same app; the packet analyses **only
  the single-player Story campaign**, and the packaged multiplayer material is
  excluded even though it shares the application.
- Platform, input and difficulty: English interface, Windows, mouse and
  keyboard, offline single-player Story at the default `Medium` difficulty on a
  fresh profile.
- Entry: start a fresh Story at default `Medium`, accept first ordinary control
  in Chapter I `Something Rotten in the Air` with the starting sidearm carried,
  and retain the opening tutorial prompts.
- Primary decision loop: read the local third-person view, health and painkiller
  silhouette, Bullet Time meter, reticle, active weapon and ammunition; move
  through the authored route; take and leave compatible cover; aim, fire,
  reload, collect and switch compatible weapons; activate Bullet Time or
  Shootdodge while the finite meter permits; consume one carried painkiller
  when missing health justifies immediate recovery; operate required route
  fixtures; and, when a shot would otherwise be fatal, use the automatic Last
  Man Standing window to defeat the responsible hostile before it expires.
- Positive terminal: clear the closing vehicle rescue, complete Chapter I and
  retain ordinary first control in Chapter II.
- Negative terminal: health reaching zero with no eligible painkiller or
  failing Last Man Standing ends the attempt; choosing retry restores the latest
  authored checkpoint on the declared `Medium` rules.
- Included: third-person movement and short climbs; aimed body-region firing;
  manual reload, weapon pickup and selection under finite slot/ammunition state;
  attachment to and release from contextual cover; the finite Bullet Time meter
  and Shootdodge; immediate painkiller recovery from finite carried stock; Last
  Man Standing's stock-gated counter-shot; continuous health, live combat,
  current tutorial prompts and HUD state; required switchboard and combat gates;
  one checkpoint retry; and retained Chapter II control.
- Excluded: the packaged multiplayer content and every online category; Arcade
  and score-attack modes; New York Minute; other difficulties; later chapters;
  console versions; the earlier Max Payne games; optional collectible weapon
  parts and clues, which the route does not require; achievements and account
  progression; repeated-failure assistance after multiple checkpoint deaths;
  destructible-cover edge cases not exercised by the route; screenshots,
  official artwork, third-party assets, video and audio evidence.
- Reproducible parameterisation: install English app `204100`, confirm the
  public branch build, and start a fresh single-player Story campaign at the
  default difficulty. From first control, clear the opening corridor, follow one
  contextual tutorial instruction, take and leave cover at least once, commit
  one Shootdodge, reload, collect and switch to one compatible dropped weapon,
  collect and consume one painkiller, operate the required parking gate switch,
  demonstrate one successful Last Man Standing counter-shot and one ordinary
  checkpoint retry, then clear the vehicle rescue and retain first Chapter II
  control. Exact enemy counts, weapon models, collectible locations,
  painkiller counts and checkpoint inventory values are parameters.
- Potential scoped modules: any later chapter; the packaged multiplayer; Arcade
  and New York Minute; a higher difficulty with different assistance.
- Direct-play status: not conducted. Valve application data and the current
  Steam product record establish lawful availability, exact product identity,
  Windows support, the single package, the absence of separate DLC apps, the
  single-player and multiplayer categories and the complete-edition packaging.
  Rockstar's official PC manual and current support records establish the
  Story controls, HUD, weapon, health, Bullet Time, cover, Last Man Standing,
  default difficulty and checkpoint-retry rules. The public SteamCMD projection
  supplies one dated secondary build observation; the exact Chapter I route
  remains independently corroborated secondary evidence. No video or audio was
  opened, played, heard, analysed or used.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `MP3-001` | Steam app `204100` identifies the currently lawfully offered English Windows product, sold through the single package `14903`, with no separate DLC apps and single-player plus multiplayer categories | Confirmed | Direct | High | P1 |
| `MP3-002` | The publisher describes this app as the complete edition, containing the original game and all previously released downloadable content in one product | Observation | Direct | High | P2 |
| `MP3-003` | The public branch carries build `17939828`, whose branch record was updated 2025-04-01; Rockstar separately publishes PC title update `v1.0.0.272` | Observation | Corroborated | High | S1, P3 |
| `MP3-004` | The official PC manual exposes direct movement, aim, fire, reload, weapon pickup/selection, cover, Bullet Time, Shootdodge, painkillers and interaction controls | Confirmed | Direct | High | P4 |
| `MP3-005` | The HUD exposes health/painkiller stock, Bullet Time, reticle, ammunition, active weapon and contextual prompts | Confirmed | Direct | High | P4 |
| `MP3-006` | Bullet Time is finite, slows the world relative to the protagonist and is replenished by eligible fire exchanges; Shootdodge leaves the protagonist prone but still able to aim and reload | Confirmed | Direct | High | P4 |
| `MP3-007` | Painkillers are found in the environment and immediately restore missing health when consumed | Observation | Corroborated | High | P4, S2, S3 |
| `MP3-008` | A fatal shot with a painkiller remaining opens a few-second Last Man Standing window; defeating the responsible shooter consumes a painkiller and restores enough health to continue | Confirmed | Direct | High | P4 |
| `MP3-009` | `Medium` is the default Story difficulty; a failed checkpoint retry restores at least one full magazine per eligible gun and the checkpoint's starting painkiller count | Confirmed | Direct | High | P5 |
| `MP3-010` | Chapter I requires authored combat and fixture gates, closes with the vehicle rescue and hands progression to Chapter II | Observation | Corroborated | Medium | S2, S4 |
| `MP3-011` | Optional collectible weapon parts and clues are not required for the Chapter I terminal | Observation | Limited | Medium | S2 |
| `MP3-012` | The bounded identity is a retained action chapter in which one finite stock pays either for immediate recovery by choice or for successful recovery from a lethal counter-window | Strong Pattern | Corroborated | High | `MP3-004`–`MP3-010` |

## Basic data

- Release / origin: Rockstar Games; released 2012-05-31 on this platform.
- Platform or physical form: lawfully offered English Windows Steam application
  `204100`; one offline single-player Story chapter.
- Puzzle family: tactical forecast and counterplay; real-time system pressure;
  ordered dependency sequencing.
- Primary and official sources, accessed 2026-09-07:
  - **[P1]** [Valve application data](https://store.steampowered.com/api/appdetails?appids=204100&cc=ua&l=english),
    for the exact title, app, Windows support, publisher, release date, the
    `Action` genre with no Early Access marker, the single-player and
    multiplayer categories, the single package, the absence of DLC apps and the
    current Ukraine offer.
  - **[P2]** the publisher-authored product description returned by `P1`, for
    the complete-edition packaging and its list of included downloadable
    content.
  - **[P3]** [Rockstar Support PC title update
    `v1.0.0.272` notes](https://support.rockstargames.com/articles/4YI9gnURhHS0zI6S7SJeJM/max-payne-3-pc-title-update-v1-0-0-272-notes),
    for the latest separately named PC update surfaced by the publisher's
    current support index; it is not treated as the Steam branch Build ID.
  - **[P4]** [Rockstar's official English PC
    manual](https://media.rockstargames.com/rockstargames-newsite/img/manuals/en_us/MP3_PC_Manual_M01.pdf),
    for Story controls, HUD, health and painkillers, weapon handling, cover,
    Bullet Time, Shootdodge and Last Man Standing.
  - **[P5]** [Rockstar Support on Story difficulty
    settings](https://support.rockstargames.com/articles/4zeNf5cXqAvv9r4lydo8ST/information-about-difficulty-settings-in-max-payne-3),
    for default `Medium`, its dynamic-difficulty boundary and ordinary
    checkpoint-retry inventory rules.
  - **[P6]** [the publisher's own news feed for the application](https://api.steampowered.com/ISteamNews/GetNewsForApp/v2/?appid=204100&count=4&feeds=steam_community_announcements),
    which returns no announcements for this app.
- Corroborating textual sources, accessed 2026-09-07. **All are secondary:**
  - **[S1]** [public SteamCMD info projection](https://api.steamcmd.net/v1/info/204100),
    for public branch build `17939828` and its 2025-04-01 branch timestamp; a
    secondary distribution observation, not a publisher claim.
  - **[S2]** [independent chapter walkthrough](https://portforward.com/games/walkthroughs/Max-Payne-3/Chapter-I-Something-Rotten-in-the-air.htm),
    for the opening corridor fight, the slow-motion jump, cover attachment to
    objects, the painkiller found and consumed, the short climbs, the optional
    weapon-part collectibles and the chapter's closing sequence.
  - **[S3]** [an independent mechanics
    guide](https://steamcommunity.com/sharedfiles/filedetails/?id=391726164),
    for the immediate rather than delayed health response to a painkiller.
  - **[S4]** [a second independent Chapter I
    walkthrough](https://www.supercheats.com/guides/max-payne-3/something-rotten-in-the-air),
    for the opening prompts, parking-gate fixture, vehicle rescue and handoff to
    the next chapter.
- Source-class limitation: the official PC manual directly establishes the
  portable combat rules but does not identify the current Steam Build ID, and
  its document date is not equated with the observed 2025 branch build. The
  exact Chapter I route and retained terminal remain secondary, independently
  corroborated observations. No direct play or audiovisual evidence was used.
- Reproducible control: **[V1]** repository-side transition trace across
  `P1`–`P6` and `S1`–`S4` under the declared app, package, branch, platform,
  input, difficulty, fresh profile, exclusions and terminal; rules reasoning,
  not direct play.
- Claim IDs: `MP3-001`–`MP3-012`. No audiovisual evidence was used.

## Mechanical decomposition

### Action Genes

- Existing `ACT-008`: the player advances the protagonist through the chapter's
  authored geometry, including short climbs.
- Existing `ACT-161`: the player aims the carried firearm at one reachable
  hostile and fires.
- Existing `ACT-164`: the player selects one compatible carried weapon as the
  active firearm.
- Existing `ACT-183`: the player manually reloads the active firearm from its
  compatible reserve ammunition.
- Existing `ACT-199`: the player collects a compatible weapon, ammunition or
  painkiller from the authored environment.
- Existing `ACT-226`: the player attaches the protagonist to a reachable
  protective surface and deliberately leaves it while the exchange continues.
- Existing `ACT-229`: the player commits the protagonist's finite special
  resource to enter the temporary slow-motion combat form, including its diving
  variant.
- Existing `ACT-341`: the player deliberately operates a reachable authored
  fixture, including the required parking-gate switchboard.
- Existing `ACT-131`: the player consumes one carried painkiller and receives
  its immediate health effect.
- No new Action gene is admitted. Weapon models, key bindings, painkiller counts
  and fixture identities are parameters. Claims: `MP3-004`–`MP3-007`,
  `MP3-010`.

### System Behaviour Genes

- Existing `SYS-208`: aimed shots resolve against continuous body regions,
  hostile state and intervening cover.
- Existing `SYS-215`: controlled and hostile combatants exchange effects in real
  time.
- Existing `SYS-368`: the special state continuously drains its finite meter
  and applies its temporary combat modifiers until cancellation or exhaustion.
- Existing `SYS-369`: choosing retry after a failed attempt restores the latest
  authored checkpoint and its declared inventory baseline.
- Existing `SYS-578`: damage subtracts from a continuous health pool and a
  valid painkiller restores eligible missing health immediately.
- Existing `SYS-780`: completing the authored Chapter I event chain settles the
  chapter and retains ordinary control in Chapter II.
- New `SYS-820`: a blow that would end the attempt is instead suspended into a
  bounded last-chance window while restorative stock remains. Defeating the
  responsible hostile before expiry consumes one painkiller, restores a small
  amount of health and continues the attempt; expiry settles defeat.
- Resolution order: damage resolves against health; if health would reach zero
  while restorative stock remains, the lethal blow converts into the last-chance
  window; the window resolves when the responsible hostile is defeated or on
  expiry; only successful resolution consumes one painkiller and returns a
  small amount of health. Claims: `MP3-006`–`MP3-010`.

### Constraint Genes

- Existing `CON-262`: carried weapon slots, magazines, reserve ammunition and
  painkiller capacity bound the locally available stock.
- Existing `CON-269`: Bullet Time or Shootdodge requires available special-meter
  readiness.
- Existing `CON-282`: authored combat clears, fixture interaction and the
  vehicle rescue form a mandatory ordered chapter route.
- Existing `CON-285`: weapon pickup, selection, firing and reload are legal only
  for compatible weapon and ammunition state.
- Existing `CON-326`: cover attachment and aimed exposure are legal only beside
  compatible protective geometry.
- Existing `CON-579`: a restorative may be used only against a missing health
  meter and only from the carried stock.
- Scarce resources: ammunition and weapon slots; the painkiller stock, which is
  simultaneously the healing budget and last-chance eligibility; the finite
  slow-motion meter; and the protective geometry the route provides. Claims:
  `MP3-004`–`MP3-010`.

### Information Genes

- Existing `INF-073`: the interface exposes the carried weapons and the active
  one, plus compatible ammunition state.
- Existing `INF-115`: the avatar-centred view, reticle and damage effects expose
  reachable hostiles and incoming threat direction; no audio claim is needed.
- Existing `INF-119`: the interface exposes health, carried painkillers and the
  finite Bullet Time meter.
- Existing `INF-268`: contextual tutorial prompts expose the next locally
  relevant input or rule during the fresh-start route.
- Claims: `MP3-004`–`MP3-006`.

### Objective Genes

- Existing `OBJ-155`: the packet completes an explicit authored action chapter
  by satisfying its ordered combat, fixture and rescue beats, then retaining
  control in the declared successor chapter.
- Collecting the optional weapon parts is not required. Claims: `MP3-009`,
  `MP3-010`.

### Time Genes

- Existing `TIM-003`: hostiles act and the slow-motion meter drains while the
  player's inputs stay accepted.
- Claims: `MP3-006`.

## Reproducible transitions

| Before | Action | Deterministic or bounded resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| The chapter has just accepted first control | Move and fire on the corridor hostiles | The carried firearm removes them; aim placement decides how quickly | armed entry | `MP3-004` |
| The active magazine is depleted while compatible reserve ammunition remains | Reload | The active firearm receives its declared magazine allocation | explicit reload state | `MP3-004` |
| A compatible dropped weapon is reachable and a carrying slot is available | Collect it, then select it | The item enters carried state and becomes the active weapon on selection | finite weapon state | `MP3-004` |
| A protective object is beside the protagonist | Commit the cover input | The protagonist attaches to it and may leave it deliberately | contextual cover | `MP3-005` |
| No compatible surface is within reach | Commit the same input | Attachment is not available | cover legality | `MP3-005` |
| The special meter is available | Commit the slow-motion dive | The world slows relative to the protagonist and aim is taken during the dive | finite special state | `MP3-006` |
| The special meter is exhausted | Commit it again | The state does not start until eligible play restores readiness | drain and restore | `MP3-006` |
| A painkiller lies on a surface | Address it | It transfers into the carried stock | contextual collection | `MP3-007` |
| Health is missing and stock remains | Consume one painkiller | One unit leaves stock and eligible missing health returns immediately | direct recovery | `MP3-007` |
| A hostile lands a blow that would reach zero health while stock remains | Continue | Terminal defeat is suspended into a bounded Last Man Standing window | stock-gated death suspension | `MP3-008` |
| The last-chance window is running | Defeat the responsible hostile before expiry | One painkiller is consumed, a small amount of health returns and ordinary live control continues | successful reprieve | `MP3-008` |
| The same window expires without that defeat | Continue | The attempt ends | reprieve failure | `MP3-008` |
| The attempt has ended at a checkpointed route state | Choose retry once | The latest checkpoint returns with its declared starting painkillers and at least one full magazine per eligible gun | ordinary checkpoint restore | `MP3-009` |
| The parking gate blocks the required route | Operate its switchboard | The gate opens and the authored vehicle-rescue sequence becomes reachable | fixture gate | `MP3-010` |
| The vehicle rescue has been cleared | Continue | Chapter I settles and first ordinary Chapter II control is retained | positive terminal | `MP3-010` |

## Strategic and experiential structure

- Planning horizon: ammunition, Bullet Time and painkiller stock are separate
  budgets; the last is both immediate healing and eligibility for a successful
  Last Man Standing recovery.
- Local tactics: cover and the slow-motion dive trade against each other — the
  dive buys aim at the cost of the position cover was providing.
- Medium-term structure: healing early is not free; it removes one unit that
  could instead make a later lethal hit eligible for a counter-window.
- Reversible versus irreversible: position and cover are recoverable, a spent
  painkiller is not, and the last-chance window resolves once.
- Failure attribution: visible health, stock, ammunition and Bullet Time state
  make a failure traceable to a spent painkiller, an empty weapon, exhausted
  special readiness or a missed reprieve target.
- Player trust: the reprieve is honest — it is offered exactly when stock
  exists, and it demands a specific, visible target rather than a random roll.

## Replay and variation

- What changes: how the stock is spent, how much the slow-motion meter is used,
  and how often cover is taken instead of dived out of.
- Randomness or procedural generation: the chapter, its hostiles and its
  sequence are authored. No procedural-generation claim enters this packet.
- Multiple viable strategies: a cover-heavy pass and a dive-heavy pass both
  complete the route.
- Typical replay motive: the optional collectibles and a cheaper stock cost.

## Adjacent systems and history

- Direct predecessors: `GAME-0238` Max Payne (2001), whose scoped packet already
  carries real-time aimed gunplay, manual reload, finite weapon state, the
  slow-motion resource and painkiller recovery.
- Variants: the second game, not in the corpus.
- Similar games: `GAME-0176` Grand Theft Auto V, whose reviewed packet carries
  the same contextual-cover and special-ability boundaries.
- Important differences: the predecessor's packet uses delayed recovery and a
  generic retained-location terminal. This packet uses immediate recovery,
  contextual cover, checkpoint assistance, a stock-gated suspension of death
  and an explicit retained chapter successor.
- Claims: `MP3-005`, `MP3-008`, `MP3-011`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-131`, `ACT-161`, `ACT-164`, `ACT-183`, `ACT-199`, `ACT-226`, `ACT-229`, `ACT-341` | weapon models, key bindings and fixture identities are parameters |
| System Behaviour | `SYS-208`, `SYS-215`, `SYS-368`, `SYS-369`, `SYS-578`, `SYS-780`, `SYS-820` | meter rates, health values, checkpoint inventory and window duration are parameters |
| Constraint | `CON-262`, `CON-269`, `CON-282`, `CON-285`, `CON-326`, `CON-579` | slot counts, stock sizes and route geometry are parameters |
| Information | `INF-073`, `INF-115`, `INF-119`, `INF-268` | HUD styling and prompt wording are presentation |
| Objective | `OBJ-155` | chapter and successor names are parameters |
| Time | `TIM-003` | frame pacing and slow-motion scale are implementation |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `272` (`GAME-0001`–`GAME-0272`).
- Exact genome matches: none.
- Tied near matches: `GAME-0238` — Max Payne (2001) (`19 / 34 = 0.558824`).
- Supported combination subsets: none.
- Scan date: 2026-09-07.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0238` — Max Payne (2001) | `ACT-008`, `ACT-161`, `ACT-164`, `ACT-183`, `ACT-199`, `ACT-229`, `ACT-341`, `SYS-208`, `SYS-215`, `SYS-368`, `CON-262`, `CON-269`, `CON-282`, `CON-285`, `CON-579`, `INF-073`, `INF-115`, `INF-119`, `TIM-003` | Both are authored real-time third-person gunplay packets with aimed body resolution, explicit reload and weapon state, a finite slow-motion resource, carried painkillers and a mandatory route. The predecessor resolves medicine gradually and retains a generic location terminal. This packet consumes an immediate-effect medicine through `ACT-131`, adds contextual cover and checkpoint assistance, suspends an eligible lethal hit into Last Man Standing, and retains an explicit Chapter II successor. The packaged multiplayer, other difficulties and later chapters remain outside scope. | Near, `0.558824` |

- New genes: `SYS-820`.
- Classification result: `New gene`.
- Evidence and reasoning: twenty-seven of twenty-eight genes reuse existing
  portable boundaries, nineteen shared with the reviewed predecessor. The one new
  boundary is the stock-gated death-suspension window. Independent review added
  thirteen lower-ID reuses omitted by the candidate, replaced mismatched
  delayed-restorative action `ACT-407` with immediate-effect `ACT-131`, and
  removed delayed recovery `SYS-750` plus generic route objective `OBJ-026`.

### Preserved research notes

- New genes: `SYS-820`.
- Classification result: `New gene`.
- Evidence and reasoning: twenty-seven of twenty-eight genes reuse existing
  portable boundaries, nineteen shared with the reviewed predecessor. The one new
  boundary is the stock-gated death-suspension window. Independent review added
  thirteen lower-ID reuses omitted by the candidate, replaced mismatched
  delayed-restorative action `ACT-407` with immediate-effect `ACT-131`, and
  removed delayed recovery `SYS-750` plus generic route objective `OBJ-026`.

## Taxonomy impact

- Registry changes: retain candidate addition `SYS-820`, correct its boundary
  and evidence grade from the newly located official PC manual, plus independent
  evidence for twenty-seven reused genes.
- Taxonomy-change record: none. No split, merge, deprecation, lifecycle change,
  wording generalisation or earlier reviewed-game signature change. This unit
  only closes the still-draft `GAME-0273` candidate and its new gene;
  `GAME-0238` and `GAME-0176` are untouched.
- Candidate terms affected: recorded in `CANDIDATE_TERMS.md`; all product,
  chapter, character, weapon and item names remain parameters.

## Negative results

- No video or audio evidence was used. Official product data, Rockstar's PC
  manual and current support pages establish the rules; independent written
  walkthroughs only corroborate the bounded Chapter I route and terminal.
- The candidate's statement that Rockstar published no applicable manual or
  support record was false. Locating both changed the evidence grade, admitted
  reload, finite weapon state, tutorial prompts and checkpoint restore, and
  falsified the candidate's delayed-recovery interpretation.
- Candidate reuse `ACT-407` was also rejected: its canonical boundary requires
  the predecessor's delayed recovery request. Immediate-effect `ACT-131`
  describes voluntary painkiller use here without altering the earlier gene.
- The complete edition packages multiplayer content into the same application.
  That packaging is recorded as a product fact and the multiplayer is excluded
  from the packet, so no multiplayer mechanic enters the signature.
- The support record also describes extra painkillers after repeated checkpoint
  deaths. This packet exercises one ordinary retry only, so that adaptive aid
  and its distinct `SYS-751` boundary remain outside scope.
- Passive partial-health regeneration is not admitted: the official material
  inspected here establishes painkiller restoration, not a required passive
  transition inside this route.
- Degrading cover is an official system property, but no reproducible
  cover-destruction event is required by this Chapter I packet, so `SYS-755`
  remains excluded rather than inferred from an optional edge case.
- The optional collectible weapon parts are excluded from the objective: the
  route completes without them, so they are off-route content rather than a
  gene.
- The lower-ID scan behind `SYS-820` covered every Active System gene mentioning
  death, downed state, revival, reprieve or last stand. `SYS-348` resolves
  layered shield, health and downed state and reaches knockout when recovery no
  longer prevents defeat; it describes a downed combatant awaiting revival, not
  a suspended lethal blow whose successful counter-condition consumes carried
  stock. `SYS-606` allows a special survival resource to prevent defeat without
  a bounded counter-target; `SYS-750` is delayed recovery and therefore does not
  describe this packet's immediate medicine. `SYS-368` covers only the special
  meter. None states the reprieve.
- No new combination is recorded: the interaction has one carrier here, and this
  batch requires two supporting games.

## Delta summary

## New facts

- [Strong Pattern | Corroborated | High] `MP3-001`–`MP3-012`: one authored
  action chapter in which a single carried stock pays either for immediate
  recovery by choice or, after a successful counter, recovery from a suspended
  lethal hit.

## New genes

- [Observation | Direct | High] `SYS-820` — a lethal blow suspended into a
  bounded last-chance window while restorative stock remains; successful defeat
  of the responsible threat consumes one stock unit and resumes the attempt.

## New combinations

- [Observation | Corroborated | Medium] `No new combinations`.

## Taxonomy changes

- [Observation | Direct | High] `No taxonomy changes`; no split, merge,
  deprecation, lifecycle change, wording generalisation or earlier signature
  change.

## New questions

- Does another product suspend a lethal blow against a carried stock, or is
  `SYS-820` specific to this series' painkiller economy?
- Which later chapter, if any, first requires a boundary this one does not?

## Next recommended game

- [Hypothesis | Limited | Medium] `GAME-0274` — Hollow Knight.
- Optimisation criterion: leave the authored corridor for a capability-gated
  explorable world analysed after its own sequel.
- Expected information gain: test whether a predecessor reuses boundaries the
  corpus recorded from its successor.
- Backlog impact: advances the recorded 271-to-279 horizon by one unit.

## Why this game

- [Hypothesis | Limited | Medium] The selection asked which boundaries survive a
  decade and an engine change. Nineteen genes remain shared with the predecessor;
  immediate healing, contextual cover, checkpoint assistance, explicit chapter
  settlement and the stock-gated last chance describe the scoped sequel's main
  differences. Only the last boundary requires a new gene.
