---
game_id: GAME-0264
slug: disco-elysium-the-final-cut
game_title: Disco Elysium - The Final Cut
analysis_status: reviewed
reviewed: 2026-09-05
combination_ids:
  - COMB-0262
gene_ids:
  action:
    - ACT-107
    - ACT-189
    - ACT-199
    - ACT-232
    - ACT-341
    - ACT-440
  system:
    - SYS-680
    - SYS-801
    - SYS-802
    - SYS-803
    - SYS-804
    - SYS-805
  constraint:
    - CON-282
    - CON-606
    - CON-607
  information:
    - INF-119
    - INF-320
    - INF-321
  objective:
    - OBJ-158
  time:
    - TIM-002
---

# Game: Disco Elysium - The Final Cut

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Parameters describe
gene instances but do not enter the signature.

## Analysis scope

- Version / ruleset: current unmodified English Windows Steam application
  `632470`, purchase package `172295`, observed against public branch build
  `23980936` built 2026-06-30 with its branch record updated 2026-07-01;
  checked 2026-09-05. The build identifier is a secondary distribution
  observation and is not treated as a publisher statement. `The Final Cut` is
  the only currently offered configuration of this application.
- Product boundary: this is **Disco Elysium - The Final Cut** on Windows, not
  the pre-Final-Cut release, a console version or the separately sold
  `Disco Elysium - Commercial License` package `457185`. Its two listed DLC
  apps are outside this packet.
- Platform, input and difficulty: English interface, Windows, keyboard and
  mouse, a fresh single-player `New Game`. The character is created with the
  preset `Thinker` archetype, which distributes the fixed twelve-point budget
  among the four attributes, and one signature skill bonus; that distribution
  is fixed for this packet rather than treated as a live decision.
- Setup-only predecessor: the mandatory opening interior monologue that
  precedes ordinary control establishes the clean save but contributes no
  genes or transitions to this packet.
- Entry: accept first ordinary control in the hotel room of the
  `Whirling-in-Rags` on the first day, before examining any object. Record the
  starting Health, Morale, worn items and empty inventory.
- Primary decision loop: click a reachable destination and let the character
  walk there; address a highlighted object or person and open its authored
  exchange; read the internal commentary that arrives attributed to a named
  faculty and decide how much of it to trust; select an ordinary response, or
  select an option that carries an attribute check after reading its disclosed
  odds and the individual modifiers producing them; change worn clothing to
  shift those modifiers before committing; accept that a failed reattemptable
  check waits for a qualifying change while a failed closed check is settled
  permanently; collect the items the room yields; watch the clock advance on
  each committed exchange but not while walking; and register each learned fact
  and task in the case record.
- Positive terminal: after retrieving the door key, leaving the room, recovering
  the second shoe and descending to the ground floor of the
  `Whirling-in-Rags`, reach the first ordinary conversational control with the
  partner `Kim Kitsuragi`. Create a manual save at that point, quit to the main
  menu, load the same save and verify the retained tasks, Health, Morale, worn
  items, inventory and clock. Stop before accepting any further investigation
  task from him.
- Negative terminal: either personal pool reaching zero ends the current
  attempt independently of the other, so a purely verbal exchange can end the
  attempt with no physical injury. Continuing requires restoring an earlier
  save; that restoration is outside the packet's admitted rules and is not a
  mechanic of this genome.
- Included: click-to-walk destination commands; authored object and person
  interaction; authored responses; check-bearing options with their disclosed
  odds and modifiers; the two-dice resolution with its automatic extremes; the
  reattemptable and closed retry classes; unrequested checks resolved into
  attributed internal commentary; two independent personal pools; item
  collection and worn-equipment modifiers; the clock that advances on
  interaction but not on movement; the case record that converts examined
  evidence into tracked progress; and the reload-verified partner encounter.
- Excluded: the pre-Final-Cut release, console versions and the Commercial
  License package; both DLC apps; everything after the first partner
  encounter, including every later task, day, district and ending; the Thought
  Cabinet, which is excluded as a recorded evidence gap because the sources
  establish that thoughts exist and that cabinet slots are unlocked with skill
  points but do not establish that a thought can be acquired and internalised
  inside this declared route; experience spending and level-up, excluded on the
  same evidence ground; the Novelty Dicemaker, drugs and money; combat-like
  set pieces later in the game; save-scumming as a rule; all inputs and
  platforms not declared above; screenshots, official artwork, third-party
  assets, video and audio evidence.
- Reproducible parameterisation: install English app `632470` from package
  `172295`, start a clean `New Game`, take the preset `Thinker` archetype and
  its signature skill, and retain default keyboard and mouse bindings. From
  first ordinary control, examine the mirror, the window and the ceiling
  fixture; commit at least one check-bearing option and read its disclosed odds
  and modifiers first; change at least one worn item and observe the modifier
  change; retrieve the door key from the trousers; leave the room; recover the
  second shoe; and descend to the first partner encounter. Then perform the
  stated manual save and reload terminal. Exact attribute values, odds, dice
  results, item names, clock readings and which optional objects are examined
  are parameters.
- Potential scoped modules: one later day; one named district; the Thought
  Cabinet and experience economy; a different starting archetype or custom
  attribute distribution; or a later authored set piece requires its own
  version, entry, loop, terminal and evidence.
- Direct-play status: not conducted. Valve application and package data plus
  the current Steam product record establish lawful availability, exact product
  identity, Windows support, the single-player category, the separation of the
  Commercial License package and the two DLC apps. The public SteamCMD info
  projection supplies one dated secondary build observation. Independent static
  written references corroborate the four attributes and twenty-four skills,
  the preset archetypes and the twelve-point budget, the separation of
  reattemptable from single-attempt checks, the two-dice resolution against
  declared difficulty tiers with automatic failure and success rolls, the
  modifier sources including clothing, the two personal pools damaged by
  different sources, the clock that advances on interaction but not on movement
  or item pickup, and the ordered opening route through the hotel room to the
  first partner encounter. This is an evidence-backed rules reconstruction, not
  a claimed playthrough or entitlement. No video or audio was opened, played,
  heard, analysed or used.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `DEL-001` | Steam app `632470` identifies the currently lawfully offered English Windows product, whose purchase package `172295` is distinct from the Commercial License package `457185` and from its two DLC apps | Confirmed | Direct | High | P1, P2 |
| `DEL-002` | The public branch record carries build `23980936`, built 2026-06-30 and updated 2026-07-01 | Observation | Limited | Medium | S1 |
| `DEL-003` | Four attributes each govern six skills, for twenty-four; twelve points are distributed at creation, capped per attribute, and one signature skill receives a bonus level | Observation | Corroborated | High | S2 |
| `DEL-004` | Three preset archetypes distribute the twelve points differently and a custom distribution is also offered | Observation | Corroborated | High | S2 |
| `DEL-005` | A committed check totals the tested skill's value, its modifiers and a roll of two six-sided dice, and compares that total with the option's declared difficulty number | Observation | Corroborated | High | S3 |
| `DEL-006` | The declared difficulty tiers run from Trivial at 6 through Impossible at 18 or higher | Observation | Corroborated | Medium | S3 |
| `DEL-007` | The lowest possible roll fails automatically and the highest possible roll succeeds automatically, regardless of the total | Observation | Corroborated | High | S3 |
| `DEL-008` | Modifiers reaching a check come from clothing, active thoughts, purchased dice, substances and earlier choices | Observation | Corroborated | High | S3 |
| `DEL-009` | Reattemptable checks may be tried again after a qualifying change such as a raised skill, while single-attempt checks are permanently settled by their result | Observation | Corroborated | High | S2, S3 |
| `DEL-010` | Skills also act continuously on dialogue without being selected, surfacing commentary attributed to the specific skill that produced it | Observation | Corroborated | High | S2 |
| `DEL-011` | Two separate pools exist, one damaged by physical events and one by verbal ones, and each is tied to a different attribute | Observation | Corroborated | High | S2, S3 |
| `DEL-012` | The clock progresses on interaction with objects, the character's own faculties or other people, but not while moving or picking items up | Observation | Corroborated | High | S2 |
| `DEL-013` | The opening route runs through examining the room's fixtures, passing at least one check to obtain clothing, taking the door key from the trousers, leaving the room, recovering the second shoe and descending to meet the partner | Observation | Corroborated | High | S4, S5 |
| `DEL-014` | Examined objects and completed exchanges register tasks and learned facts in the case record | Observation | Corroborated | High | S4, S5 |
| `DEL-015` | The bounded identity is an episode whose every gate is opened by a disclosed-odds attribute check, whose failures are typed as retryable or permanent, and whose information arrives attributed to the faculty that produced it | Strong Pattern | Corroborated | High | `DEL-003`–`DEL-014` |

## Basic data

- Release / origin: ZA/UM; `The Final Cut` configuration of the Windows Steam
  application published by ZA/UM, with the base application released
  2019-10-15.
- Platform or physical form: lawfully offered English Windows single-player
  Steam application `632470`; one fresh opening-episode packet ending at the
  first partner encounter.
- Puzzle family: knowledge and evidence progression; ordered dependency
  sequencing.
- Primary and official sources, accessed 2026-09-05:
  - **[P1]** [Valve application data](https://store.steampowered.com/api/appdetails?appids=632470&cc=ua&l=english),
    for the exact title, app, Windows support, developer and publisher, release
    date, single-player category, the two DLC apps, the two offered packages
    and the current Ukraine offer.
  - **[P2]** [current Steam product page](https://store.steampowered.com/app/632470/Disco_Elysium__The_Final_Cut/?l=english),
    for lawful availability, the described skill system and the separation of
    the Commercial License package from the ordinary purchase. Embedded media
    was not opened or used.
- Corroborating textual sources, accessed 2026-09-05:
  - **[S1]** [public SteamCMD info projection](https://api.steamcmd.net/v1/info/632470),
    for public branch build `23980936` and its branch timestamps. This mirrors
    Valve's public product data and is treated as a secondary distribution
    observation, not a publisher claim.
  - **[S2]** [static beginner's reference](https://steamcommunity.com/sharedfiles/filedetails/?id=3017444198),
    for the four attributes governing six skills each, the twelve-point budget
    and per-attribute cap, the three preset archetypes and the signature skill,
    the passive influence of skills on available responses, the separation of
    retryable from single-attempt checks, the two pools damaged by verbal and
    physical events, the role of thoughts as modifiers, and the statement that
    the clock progresses on interaction but not on movement or item pickup.
  - **[S3]** [static skill-check reference](https://discoelysium.fandom.com/wiki/Skills),
    together with the linked community discussions it summarises, for the
    skill-plus-modifiers-plus-two-dice total, the declared difficulty tiers,
    the automatic failure and success rolls, and the modifier sources including
    clothing, thoughts, purchased dice and earlier choices.
  - **[S4]** [static opening-route reference](https://showgamer.com/en/disco-elysium-walkthrough),
    for the ordered hotel-room route: collecting trousers, jacket, the item
    obtained by passing a check at the ceiling fixture and the shirt; examining
    the mirror, the window and the hanging item; taking the door key from the
    trouser pocket; leaving through the front door; recovering the second shoe;
    and descending to meet the partner.
  - **[S5]** [independent static task reference](https://www.gamepressure.com/disco-elysium/return-to-the-whirling-in-rags/zc11505),
    for tasks being recorded in the case record as they are encountered and for
    the partner accompanying the investigation. Images and embedded media were
    not opened or used.
- Reproducible control: **[V1]** repository-side transition trace across `P1`,
  `P2` and `S1`–`S5` under the declared app, package, build, platform, input,
  archetype, clean setup, exclusions and retained terminal; rules reasoning,
  not direct play.
- Claim IDs: `DEL-001`–`DEL-015`. No audiovisual evidence was used.

## Mechanical decomposition

### Action Genes

- Existing `ACT-189`: address the controlled character and commit a world
  destination that autonomous pathing then executes; `ACT-341`: address one
  reachable authored object and commit its legal read, collect, unlock or open
  interaction; `ACT-199`: transfer a collected item and equip it into a
  compatible worn slot.
- Existing `ACT-232`: select one currently offered authored response;
  `ACT-107`: complete an exchange that registers one exact fact as learned and
  makes it available to later rule-bearing interactions.
- New `ACT-440`: select an offered option that carries an attribute check,
  read its disclosed odds and modifiers, and commit it knowing a random
  resolution decides the outcome. `ACT-232` covers an ordinary response whose
  result is fixed, and `ACT-261` covers a timing input; neither covers accepting
  a stated probability.
- Actor, object, item, room, skill and exact value names remain parameters.
  Claims: `DEL-003`–`DEL-014`.

### System Behaviour Genes

- New `SYS-801`: total the tested value, its modifiers and two dice against the
  declared difficulty, with the extreme rolls overriding that total. No existing
  system gene exposed the contributing terms of its own randomness; `SYS-004`
  is a bare random outcome selection and was rejected as subsumed rather than
  admitted alongside it.
- New `SYS-802`: settle each failure by its declared retry class, so a
  reattemptable failure waits for a qualifying change while a closed failure
  permanently removes the outcome it would have produced.
- New `SYS-803`: continuously resolve unselected checks and surface only their
  successes as attributed commentary, leaving their failures silent and unknown.
- New `SYS-804`: advance the clock by a declared increment on each committed
  interaction and not at all while the character walks or collects items.
- New `SYS-805`: apply typed damage to two independent personal pools, either
  of which ends the attempt on its own.
- Existing `SYS-680`: convert examined evidence into recorded case progress and
  updated tracked tasks.
- Resolution order: a destination command moves the character without advancing
  the clock; addressing an object or person opens its exchange and advances the
  clock; unselected checks resolve first and may add attributed commentary; the
  worn set is read to compute each offered check's modifiers and disclosed
  odds; a committed check resolves against the difficulty with its automatic
  extremes; the result is settled by its retry class; typed damage is applied to
  the matching pool; and learned facts and tasks are registered. Claims:
  `DEL-005`–`DEL-014`.

### Constraint Genes

- New `CON-606`: a settled check may be reattempted only inside the
  reattemptable class and only after a qualifying state change; the closed class
  admits no further attempt. `CON-269` covers resource and cooldown readiness,
  which is a different legality.
- New `CON-607`: the worn set continuously modifies the attribute values used
  to resolve checks, so the same option's odds depend on current clothing.
- Existing `CON-282`: leaving the room and reaching the partner require their
  authored predecessors, including the retrieved key.
- Scarce resources: both personal pools, the single attempt available to a
  closed check, the qualifying changes that reopen a reattemptable one, the
  clock, and the attribute values themselves. Exact values are parameters.
  Claims: `DEL-005`–`DEL-013`.

### Information Genes

- New `INF-320`: an offered check exposes its difficulty, its computed odds and
  the individual terms currently raising or lowering them before commitment.
  `INF-190` forecasts an attack's result and `INF-220` shows displayed hit odds
  for a tactical action, but neither itemises the modifier terms of a
  conversational option or states what would have to change.
- New `INF-321`: each line of internal commentary is labelled with the named
  faculty that produced it, so the same sentence carries different reliability
  depending on its source. `INF-268` is a tutorial adviser and `INF-125` is a
  mission marker; neither attributes interpretation to a faculty.
- Existing `INF-119`: the current personal pools and character state remain
  visible.
- Exact wording, fonts, portrait art, odds formatting and interface positions
  are presentation parameters. Claims: `DEL-005`–`DEL-011`.

### Objective Genes

- New `OBJ-158`: complete the required interactions of the bounded authored
  episode whose gates are opened through conversation, examination and attribute
  checks rather than physical resolution, and retain its recorded progress and
  successor access across a persistence check. Every existing bounded-segment
  objective in the corpus requires a guardian, a target set, a narrative ending
  or a filled evidence account.
- Leaving the room, recovering the shoe or seeing the partner without the
  stated manual save and reload check is not success. Claims:
  `DEL-013`–`DEL-015`.

### Time Genes

- Existing `TIM-002`: the player may pause indefinitely between discrete
  actions, and each completed action changes state without a time-driven system
  step. The clock's interaction-driven advance is owned by `SYS-804` rather
  than by a real-time gene.
- Claims: `DEL-012`, `DEL-013`.

## Reproducible transitions

| Before | Action | Deterministic or bounded resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| A clean New Game has completed only the setup monologue | Accept first ordinary control in the hotel room | The episode begins with the fixed archetype's attribute values and no imported state | fixed clean entry | `DEL-003`, `DEL-004` |
| A reachable floor position is clicked | Release the input | The character walks there under automatic pathing and the clock does not advance | movement is free of time | `DEL-012` |
| A highlighted object or person is addressed | Commit the interaction | Its authored exchange opens and the clock advances by its declared increment | interaction is the clock's currency | `DEL-012` |
| An exchange is open and an unselected check succeeds | Continue reading | An additional line appears labelled with the faculty that produced it | attributed disclosure | `DEL-010` |
| An exchange is open and an unselected check fails | Continue reading | Nothing appears, and the player is not told a disclosure was withheld | silent failure | `DEL-010` |
| An offered option carries a check | Inspect it before committing | Its difficulty, computed odds and individual modifier terms are shown | pre-commitment arithmetic | `DEL-005`, `DEL-008` |
| A check's odds are unsatisfactory and a worn item affects its attribute | Change the worn item, then inspect the option again | The listed modifiers and the computed odds change accordingly | dressing as preparation | `DEL-008` |
| A check-bearing option is committed | Resolve it | The tested value plus modifiers plus two dice is compared with the declared difficulty | disclosed-odds resolution | `DEL-005`, `DEL-006` |
| A committed check rolls the lowest possible dice total | Resolve it | The attempt fails regardless of how favourable the total would have been | automatic failure | `DEL-007` |
| A committed check rolls the highest possible dice total | Resolve it | The attempt succeeds regardless of how unfavourable the total would have been | automatic success | `DEL-007` |
| A reattemptable check has failed | Produce a qualifying change, then return | The option admits another attempt | change-gated retry | `DEL-009` |
| A closed check has failed | Return to it | No further attempt is admitted and the outcome it would have produced is gone | permanent settlement | `DEL-009` |
| A verbal exchange damages the composure pool to zero | Continue | The attempt ends although the physical pool is untouched | independent verbal terminal | `DEL-011` |
| The door key has been taken from the trousers | Open the front door | The route out of the room opens, which it did not before | authored gate | `DEL-013` |
| An object has been examined or an exchange completed | Open the case record | The learned fact or task is registered there | evidence into recorded progress | `DEL-014` |
| First ordinary conversational control with the partner is available | Create a manual save, quit and load it | The same tasks, pools, worn items, inventory and clock return | reproducible positive terminal | `DEL-014`, `DEL-015` |

## Strategic and experiential structure

- Planning horizon: the case record exposes what is outstanding, while the
  attribute values, worn set and each option's disclosed odds determine whether
  to attempt a check now, prepare for it or leave it alone.
- Local tactics: read the modifier breakdown before committing, change clothing
  to move a marginal check into a comfortable band, spend reattemptable checks
  freely and closed ones only when the odds justify a permanent branch, and
  weigh a faculty's commentary against how strong that faculty actually is.
- Medium-term structure: the room teaches examination, then the first check,
  then the modifier system, then the retry classes; leaving the room converts
  those into a route gate; and the descent settles the episode into a partner
  encounter that later work depends on.
- Reversible versus irreversible: movement, clothing and examination are freely
  reversible; the clock only advances; a reattemptable failure is recoverable
  through a state change; a closed failure and either pool reaching zero are
  not.
- Failure attribution: the disclosed odds mean a lost check is traceable to an
  accepted probability rather than to a hidden rule, and the automatic extremes
  are announced in advance as part of the same system.
- Player trust: the interface states the arithmetic of its own uncertainty, the
  retry class is visible before commitment, the commentary names its own
  source, and the loaded save reproduces the settled state exactly.

## Replay and variation

- What changes: the archetype's attribute spread, which checks are attempted,
  what is worn when each is committed, which optional objects are examined, the
  dice results and how much clock is spent.
- Randomness or procedural generation: the room, its objects, the tasks, the
  difficulty numbers and the route are authored. Only the dice are random; no
  procedural-generation claim enters this packet.
- Multiple strategies: the episode admits attempting the check-bearing options
  immediately, preparing the worn set first, or bypassing optional checks
  entirely. The control demonstrates one prepared and one unprepared attempt
  rather than making a no-failure route the terminal.
- Typical replay motive: reach the partner having passed the checks that were
  closed on the previous attempt, and see the commentary a different attribute
  spread makes visible.

## Adjacent systems and history

- The Witcher 3: Wild Hunt shares authored responses, learned facts, item
  equipping, ordered gates, visible personal state and evidence converted into
  quest progress. It resolves its consequential moments through real-time
  combat and signs; this packet has no physical resolution anywhere in its
  completion condition and settles every gate through a disclosed-odds check.
- Detroit: Become Human shares branching authored dialogue whose outcomes
  persist, but its branch results are fixed by the option chosen rather than by
  a random resolution whose odds are shown and can be prepared.
- Papers, Please shares a self-paced examination loop and an interaction-driven
  clock, but its verdicts are deterministic classifications rather than
  probability commitments.
- Her Story shares the retrieval of authored information without physical
  resolution, but its progress comes from search terms rather than from
  attribute checks against a difficulty.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-107`, `ACT-189`, `ACT-199`, `ACT-232`, `ACT-341`, `ACT-440` | skill, item, object, room and character names are parameters |
| System Behaviour | `SYS-680`, `SYS-801`, `SYS-802`, `SYS-803`, `SYS-804`, `SYS-805` | dice count, difficulty numbers, increments and pool caps are parameters |
| Constraint | `CON-282`, `CON-606`, `CON-607` | retry classes, qualifying changes and per-item deltas are parameters |
| Information | `INF-119`, `INF-320`, `INF-321` | odds formatting, faculty names and interface layout are parameters |
| Objective | `OBJ-158` | episode boundary and retained successor state are parameters |
| Time | `TIM-002` | pause length and reading pace are implementation |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `263` (`GAME-0001`–`GAME-0263`).
- Exact genome matches: none.
- Tied near matches: `GAME-0205` — The Witcher 3: Wild Hunt (`6 / 43 = 0.139535`).
- Supported combination subsets: `COMB-0262`.
- Scan date: 2026-09-05.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0205` — The Witcher 3: Wild Hunt | `ACT-107`, `ACT-199`, `ACT-232`, `SYS-680`, `CON-282`, `INF-119` | Both advance an authored investigation by selecting responses, registering learned facts, equipping items, satisfying ordered gates and reading visible personal state, and both convert examined evidence into recorded progress. The Witcher resolves its consequential moments through real-time combat, signs and preparation for physical encounters. This packet contains no physical resolution at all: every gate is opened by an option whose success odds and modifier terms are disclosed before commitment, failures are typed as reattemptable or permanently closed, information arrives attributed to the named faculty that produced it, the clock is spent by interacting rather than by existing, and a purely verbal exchange can end the attempt on its own pool. This is the lowest selected-neighbour score in the batch and reflects a genuine change of mechanical domain rather than a weak decomposition. | Near, `0.139535` |

### Preserved research notes

- New genes: `ACT-440`, `SYS-801`, `SYS-802`, `SYS-803`, `SYS-804`, `SYS-805`,
  `CON-606`, `CON-607`, `INF-320`, `INF-321`, `OBJ-158`.
- Reused genes: the remaining nine admitted genes in the Normalised genome.
- Classification result: `New gene`.
- Lower-ID scan: reuse `ACT-189` for click-to-walk rather than stretching
  `ACT-008`, whose boundary explicitly excludes selecting a remote destination
  for automatic pathfinding; reuse `ACT-232` and `ACT-107` for ordinary
  responses and learned facts and add `ACT-440` only for the probability
  commitment neither covers; reuse `SYS-680` for the case record; reuse
  `TIM-002` for the self-paced structure and let `SYS-804` own the
  interaction-driven clock. Reject `SYS-004` as subsumed by `SYS-801`; reject a
  skill-, faculty-, character-, room- or item-named gene; reject a Thought
  Cabinet or experience gene because neither is evidenced inside this route.

## Taxonomy impact

- Registry changes: add `ACT-440`, `SYS-801`, `SYS-802`, `SYS-803`, `SYS-804`,
  `SYS-805`, `CON-606`, `CON-607`, `INF-320`, `INF-321`, `OBJ-158` and
  `COMB-0262`, plus independent evidence for nine reused genes.
- Taxonomy-change record: none; no split, merge, deprecation, lifecycle change,
  wording generalisation or signature change.
- Candidate terms: recorded in `CANDIDATE_TERMS.md`; all product, character,
  location, skill, item, app, package and build names remain parameters.

## Negative results

- No video or audio evidence was used; only official static text and data plus
  static written references support this packet.
- The Thought Cabinet and the experience economy are excluded as a bounded
  evidence gap. The sources establish that thoughts supply check modifiers and
  that cabinet slots are unlocked with skill points, but none establishes that
  a thought can be acquired and internalised, or a level taken, inside this
  declared route. This is a recorded uncertainty, not a claim that the product
  lacks the mechanic.
- `SYS-004` was considered and rejected: a bare random-outcome-selection gene
  adds nothing beside `SYS-801`, which already owns the dice, the modifiers and
  the automatic extremes, and admitting both would inflate the signature.
- Reloading an earlier save after a closed failure or a zero pool is a client
  facility, not an admitted rule of this genome; the packet therefore records
  the closed outcome as permanent rather than as recoverable.
- Reaching the partner without the manual save and reload retention test is not
  the terminal.

## Delta summary

## New facts

- [Observation | Corroborated | High] `DEL-001`–`DEL-015`: one bounded opening
  episode settles every gate through a check whose odds and modifiers are
  disclosed before commitment, types each failure as reattemptable or
  permanent, and attributes its information to the faculty that produced it.

## New genes

- [Observation | Corroborated | High] `ACT-440`, `SYS-801`, `SYS-802`,
  `SYS-803`, `SYS-804`, `SYS-805`, `CON-606`, `CON-607`, `INF-320`, `INF-321`,
  `OBJ-158` — the probability commitment, its disclosed resolution, the retry
  classes, attributed passive commentary, the interaction-driven clock, two
  independent personal pools, the retry legality, worn-equipment modifiers, the
  odds disclosure, faculty attribution and the dialogue-gated episode
  objective.

## New combinations

- [Strong Pattern | Corroborated | High] `COMB-0262` — a disclosed-odds
  attribute check whose failures are typed and whose information is attributed,
  settling an episode with no physical resolution.

## Taxonomy changes

- [Observation | Direct | High] No taxonomy changes; no split, merge,
  deprecation, lifecycle change, wording generalisation or earlier signature
  change.

## New questions

- Can the excluded Thought Cabinet and experience spending be evidenced inside
  this exact route, and would admitting them add genes or only parameters to
  the modifier and retry boundaries already recorded?

## Next recommended game

- [Hypothesis | Limited | High] `GAME-0265` — Bloons TD 6.
- Optimisation criterion: leave the authored-narrative corridor entirely and
  test whether pre-wave placement against a scheduled leak budget needs new
  constraint boundaries or reuses the existing placement and economy
  vocabulary.
- Expected information gain: the first tower-defence packet in the corpus.
- Backlog impact: advances the recorded 261-to-270 horizon by one unit.

## Why this game

- [Hypothesis | Limited | High] The selection called this the batch's strongest
  admission because the corpus contained no packet whose primary resolution
  mechanism is a probabilistic attribute check applied to a conversational
  option. The completed scan confirms it: at `0.139535` this is the most
  mechanically distant admission in the batch, and it shares only a six-gene
  authored-investigation backbone with its nearest neighbour.
