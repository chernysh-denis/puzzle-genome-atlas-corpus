---
game_id: GAME-0277
slug: cuphead
game_title: Cuphead
analysis_status: reviewed
reviewed: 2026-09-08
combination_ids:
  - COMB-0270
gene_ids:
  action:
    - ACT-008
    - ACT-161
    - ACT-190
    - ACT-223
  system:
    - SYS-215
    - SYS-799
    - SYS-822
  constraint:
    - CON-324
    - CON-617
  information:
    - INF-115
    - INF-119
    - INF-299
  objective:
    - OBJ-029
  time:
    - TIM-003
---

# Game: Cuphead

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Parameters describe
gene instances but do not enter the signature.

## Analysis scope

- Version / ruleset: current unmodified English Windows Steam app `268910`,
  observed against public-branch build `20241530`, whose branch record was
  updated 2025-10-03; checked 2026-09-08. The publisher's latest
  version-named announcement is patch `1.3.4`, dated 2022-08-19. Because the
  named patch predates the public build, both observations are recorded and no
  semantic version is assigned to that build.
- Product boundary: base **Cuphead** on Windows. The separately listed DLC
  apps, including *The Delicious Last Course*, and the opt-in `legacy`,
  `legacy-1.1.5` and `legacy-1.2.4` branches are outside this packet.
- Platform and fixed setup: English interface, Windows, single-player,
  controller or keyboard, fresh save after the required movement tutorial,
  Cuphead, three starting hit points, Peashooter, no secondary weapon, no
  Charm and no Super Art.
- Encounter: the ordinary, non-secret `The Root Pack` fight in `Botanic
  Panic!` on `Regular` difficulty. It is one of the initially available
  Inkwell Isle One boss levels; the player keeps firing during the onion phase,
  so the optional secret phase is not triggered.
- Entry: accept control when the opening title card clears and the first Root
  Pack member becomes actionable. The health allowance is full and the Super
  Meter begins empty.
- Primary decision loop: keep the Peashooter aimed at the current phase member;
  move, jump or dash around ordinary hazards; use a second jump input on a pink
  worm or tear inside its contact window to parry it and charge the Super
  Meter; spend at least one charged card on the Peashooter EX shot; and adapt
  the firing line and escape route when the next member replaces the previous
  one with a different attack set.
- Positive terminal: defeat the third ordinary phase, pass the `KNOCKOUT!`
  transition, read the results categories and aggregate grade, return to the
  island map, and confirm in the Equip Card that `Botanic Panic!` has the
  `Regular` checkmark plus a retained highest rank and time. The corresponding
  Soul Contract is retained.
- Negative terminal: exhaust the three-hit allowance and reach the death result
  card that reports encounter progress. That failed attempt is settled. Its
  separate `Retry` choice would begin a new attempt and is not part of the
  accepted negative terminal.
- Included: direct movement, jumping and dashing; ordinary aimed shooting and
  one meter-paid EX shot; visual attack telegraphs; contact-timed parry;
  pink-class parry legality; player health and Super Meter display; three
  sequential health-gated encounter phases; the post-win results calculation;
  retained Regular completion; and uninterrupted real-time resolution.
- Excluded: `Simple` and `Expert`; the secret radish phase; cooperative play;
  Mugman and Ms. Chalice; *The Delicious Last Course* and every listed DLC app;
  legacy branches; Run & Gun levels, Mausoleums, every other boss and full
  island progression; shop purchases, alternative weapons, Charms and Super
  Arts; achievements and account optimisation; screenshots, official artwork,
  third-party visual assets, video and audio evidence.
- Reproducible parameterisation: install English Windows app `268910`, confirm
  the public build, create a fresh save, finish the movement tutorial, retain
  the default Cuphead/Peashooter configuration, choose `Botanic Panic!` on
  `Regular`, fire throughout the onion phase, parry at least one pink hazard,
  spend at least one card on an EX shot, defeat the ordinary third phase, read
  the complete results card, return to the map and verify the Equip Card entry.
- Potential scoped modules: a `Simple` or `Expert` comparison; the secret Root
  Pack branch; another boss; one Run & Gun level; a purchased loadout; local
  cooperative play; the expansion.
- Direct-play status: not conducted. Official Valve product data establishes
  lawful availability, product and platform. Publisher-authored patch notes
  establish the current result-screen HP rule, the Parry scoring category,
  phase progression and post-death Retry surface. Xbox Wire's official
  pre-release description independently identifies the move, dash, shoot and
  pink-projectile parry-to-meter loop; it is not used for exact current route
  state. Complete secondary written guides establish the named encounter,
  three-member phase order, fixed Regular route and retained Equip Card fields.
  No video or audio was opened, played, heard, analysed or used.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `CUP-001` | Steam app `268910` is the currently lawfully offered Windows base game; separately listed DLC and legacy branches are outside the packet | Confirmed | Direct | High | P1, S1 |
| `CUP-002` | Public build `20241530` was recorded on 2025-10-03, while the newest publisher announcement carrying a semantic version names patch `1.3.4` on 2022-08-19 | Observation | Corroborated | High | P2, S1 |
| `CUP-003` | `Botanic Panic!` on Regular is a fixed Inkwell Isle One boss level whose ordinary Root Pack route has three sequential members | Observation | Corroborated | High | S2, S3, S4 |
| `CUP-004` | The fixed single-player setup starts with three HP and Peashooter; its controls admit running, jumping, dashing, ordinary fire, parry and EX fire | Observation | Corroborated | High | P3, S2 |
| `CUP-005` | Ordinary phase order is a dirt-and-worm attacker, a falling-tear attacker and a homing-projectile plus beam attacker | Observation | Corroborated | High | S3, S4 |
| `CUP-006` | Pink projectiles are the declared parryable class, and a correctly timed parry neutralises the hazard and charges the Super Meter | Confirmed | Direct | High | P3, P2, S4 |
| `CUP-007` | Peashooter's EX shot spends one charged meter card and remains available without buying a weapon or unlocking a Super Art | Observation | Corroborated | High | S2 |
| `CUP-008` | Depleting the current member's health advances the same sealed encounter to the next member without settling a separate level | Observation | Corroborated | High | P2, S3, S4 |
| `CUP-009` | The successful result grades time, remaining HP, successful parries, Super Meter use and selected skill level; current HP score uses remaining HP, not damage count | Confirmed | Direct | High | P2, S2 |
| `CUP-010` | The Equip Card retains completed level, highest rank and corresponding time; a Regular boss completion is marked with a checkmark | Observation | Corroborated | High | S2 |
| `CUP-011` | Player defeat reaches a death result/progress surface, and Retry is a separate subsequent choice | Confirmed | Direct | High | P2, S2 |
| `CUP-012` | The bounded identity is a three-phase marked-parry encounter whose successful terminal evaluates how the win was achieved | Strong Pattern | Corroborated | High | `CUP-003`–`CUP-011` |

## Basic data

- Release / origin: Studio MDHR Entertainment Inc.; released 2017-09-29.
- Platform or physical form: lawfully offered English Windows Steam app
  `268910`; one solo `Regular` Root Pack encounter from a fresh save.
- Puzzle family: tactical forecast and counterplay; real-time system pressure;
  ordered dependency sequencing.
- Primary and official sources, accessed 2026-09-08:
  - **[P1]** [Valve application data](https://store.steampowered.com/api/appdetails?appids=268910&cc=ua&l=english),
    for exact product identity, developer, release date, Windows support,
    categories and separately listed DLC apps.
  - **[P2]** [Studio MDHR's official Steam announcement feed](https://steamcommunity.com/app/268910/announcements/),
    especially patches `1.3.2`–`1.3.4`, for the named version, results-screen
    HP calculation, Parry scoring, boss phase progression, the post-death
    equipment surface and the separate Retry choice.
  - **[P3]** [Xbox Wire's official Cuphead mechanics article](https://news.xbox.com/en-us/2015/06/18/xbox-cuphead-will-kill-you-with-cuteness/),
    for leaping, dashing, shooting and timed pink-projectile parries that fill
    the special meter. This pre-release source supports only those stable core
    rules, not exact current route state.
- Corroborating textual sources, accessed 2026-09-08:
  - **[S1]** [public SteamCMD info projection](https://api.steamcmd.net/v1/info/268910),
    for public build `20241530`, its branch timestamp, depots and opt-in legacy
    branches; a secondary distribution observation.
  - **[S2]** [complete Steam Community Cuphead Basics Guide](https://steamcommunity.com/sharedfiles/filedetails/?id=1310872602),
    for starting controls and equipment, boss-level completion, Regular
    progression, result categories, EX costs and retained Equip Card fields.
  - **[S3]** [complete Gameranx Root Pack guide](https://gameranx.com/features/id/122376/article/cuphead-how-to-defeat-root-pack-boss-guide/),
    for the named three-member route, direct fire, dash and the successive
    dirt, falling-hazard, homing-projectile and beam patterns.
  - **[S4]** [search-indexed Cuphead Wiki Root Pack entry](https://cuphead.wiki.gg/wiki/The_Root_Pack),
    for the `Botanic Panic!` identity, Regular phase count, pink worm and tear
    parry objects and ordinary-versus-secret phase distinction. The page itself
    returned HTTP 403, so only the indexed text is used and no claim relies on
    it alone.
- Reproducible control: **[V1]** repository-side transition trace across
  `P1`–`P3` and `S1`–`S4` under the declared product, build, setup, entry,
  exclusions and terminals; rules reasoning, not direct play.
- Claim IDs: `CUP-001`–`CUP-012`. No audiovisual evidence was used.

## Mechanical decomposition

### Action Genes

- Existing `ACT-008`: directly run, jump and dash the controlled piece across
  the arena rather than choosing an automatically followed destination.
- Existing `ACT-161`: aim and sustain Peashooter fire at the current reachable
  phase member or destructible homing hazard.
- Existing `ACT-190`: commit the available Peashooter EX shot and its direction,
  spending one charged Super Meter card. The move is an active capability, not
  an ordinary no-cost weapon shot.
- Existing `ACT-223`: commit a jump-parry at the chosen contact instant during
  one telegraphed incoming hazard.
- No new Action gene is admitted. Character, weapon, buttons, shot cadence and
  EX damage are parameters. Claims: `CUP-004`–`CUP-007`.

### System Behaviour Genes

- Existing `SYS-215`: direct shots, hazards, damage, defeat and knockback
  exchange continuously in real time.
- Existing, generalised `SYS-799`: depletion of the current phase member
  advances the same sealed encounter into a further phase with another
  occupant and attack set while prior phase completion remains. The carrier
  proves that a visible transformation of one body is not essential to this
  transition function.
- New `SYS-822`: after a successful encounter the system calculates declared
  properties of *how* it was won and records their aggregate grade with the
  completion. Current HP grading uses remaining HP.
- Resolution order: the current member's health reaches zero; the encounter
  advances without issuing a level result; the next member takes over with a
  changed attack set; only the third ordinary member's defeat triggers the
  successful result calculation. Claims: `CUP-008`, `CUP-009`.

### Constraint Genes

- Existing `CON-324`: even an eligible parry succeeds only when the second jump
  input lands inside the matching contact window.
- New `CON-617`: parry legality additionally depends on the incoming hazard's
  declared marked class. Pink worms or tears qualify; ordinary dirt or tears do
  not. This is independent of both timing and equipped-weapon state.
- The three-hit allowance and each member's health are scarce quantities, not
  separate legality genes. Claims: `CUP-004`, `CUP-006`.

### Information Genes

- Existing `INF-115`: avatar-centred sight exposes the current member, incoming
  projectile paths and beam wind-ups. This packet makes no audio claim.
- Existing `INF-119`: the HUD exposes remaining HP and charged Super Meter
  cards needed for risk and EX-spend decisions.
- Existing, generalised `INF-299`: the successful result card exposes category
  values and their aggregate grade, sufficient to explain why two wins settle
  differently.
- Claims: `CUP-005`, `CUP-006`, `CUP-009`.

### Objective Genes

- Existing `OBJ-029`: complete one bounded hostile encounter by defeating all
  three required ordinary Root Pack members before the controlled character is
  defeated.
- `OBJ-080` is rejected: this packet verifies a retained boss-level completion
  on the island map but does not cross the newly opened route threshold into a
  successor region or act.
- The grade is evaluation of the successful objective, not a required target
  grade. Claims: `CUP-003`, `CUP-010`.

### Time Genes

- Existing `TIM-003`: phase attacks, projectiles and damage progress on a
  real-time schedule while movement, fire, dash, parry and EX inputs remain
  available.
- Claims: `CUP-004`–`CUP-008`.

## Reproducible transitions

| Before | Action | Deterministic or bounded resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| First member is actionable; HP is full and meter empty | Move and sustain Peashooter fire | Shots reduce its health while the dirt/worm cadence continues in real time | direct combat substrate | `CUP-004`, `CUP-005` |
| Pink worm reaches the controlled piece | Press jump again inside contact window | Hazard is neutralised and one Super Meter increment is credited | class plus timing gates | `CUP-006` |
| Ordinary dirt reaches the same position | Use the same parry input | Dirt is not parryable; avoidance was required and contact costs HP | class gate is not timing alone | `CUP-006` |
| At least one meter card is charged | Commit Peashooter EX fire | One card is consumed and the stronger projectile resolves | resource-paid active ability | `CUP-007` |
| Current member reaches zero health | Continue | That member leaves; the next member enters with another attack set while the same level attempt continues | health-gated phase advance | `CUP-008` |
| Controlled HP reaches zero | Continue to settlement | Death result reports attempt progress; no successful completion or grade is retained | negative terminal | `CUP-011` |
| Third ordinary member reaches zero health | Continue through result and return | Results expose time, remaining HP, parries, meter use, skill level and grade; map/Equip Card retain the Regular completion | positive terminal | `CUP-009`, `CUP-010` |

## Strategic and experiential structure

- Planning horizon: three HP must survive three different attack grammars, so
  the player trades shooting uptime against safe positioning across the whole
  encounter.
- Local tactics: a pink hazard is both danger and opportunity. The same contact
  that must be timed precisely removes the hazard and supplies later EX damage.
- Medium-term structure: each defeated member preserves progress but invalidates
  the immediately learned dodge rhythm by replacing the attack set.
- Reversible versus irreversible: position can be corrected continuously;
  spent HP and passed phase opportunities cannot be recovered inside the
  attempt. EX spend converts reversible meter stock into immediate pressure.
- Failure attribution: the death progress card locates the failed phase, while
  the successful results card separates time, HP, parry and meter-use outcomes.
- Player trust: the parry class is visually marked, phase changes follow member
  depletion, and the grade is decomposed into visible categories.

## Replay and variation

- What changes: attack timing within bounded patterns, remaining HP, parry
  count, meter use, elapsed time and final grade.
- Authored structure: the ordinary route keeps the same three members and
  order; the optional secret branch is deliberately excluded.
- Multiple viable strategies: safe movement can preserve HP but extend time;
  aggressive firing and EX use shorten the fight while reducing reaction room.
- Typical replay motive: improve one or more visible result categories and the
  retained highest rank without changing the objective.

## Adjacent systems and history

- Direct predecessors: none for this product.
- Variants: `Simple`, `Expert`, the secret phase, cooperative play and the DLC
  expansion are distinct scoped modules rather than merged evidence.
- Similar games: `GAME-0274` Hollow Knight provides the nearest full genome and
  prior support for direct arena combat, timed defence, phase progression and a
  finite hostile-set objective.
- Important differences: Hollow Knight restores and develops a persistent
  campaign character around checkpoints. This packet instead marks one hazard
  class as parryable and turns a successful encounter into a category-based
  grade.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-161`, `ACT-190`, `ACT-223` | character, Peashooter and inputs are parameters |
| System Behaviour | `SYS-215`, `SYS-799`, `SYS-822` | member order, health and grade bands are parameters |
| Constraint | `CON-324`, `CON-617` | pink marking and contact window are parameters |
| Information | `INF-115`, `INF-119`, `INF-299` | HUD and results-card art are presentation |
| Objective | `OBJ-029` | encounter and member identities are parameters |
| Time | `TIM-003` | cadence and frame pacing are implementation |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `276` (`GAME-0001`–`GAME-0276`).
- Exact genome matches: none.
- Tied near matches: `GAME-0274` — Hollow Knight (`9 / 23 = 0.391304`).
- Supported combination subsets: `COMB-0270`.
- Scan date: 2026-09-08.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0274` — Hollow Knight | `ACT-008`, `ACT-161`, `ACT-190`, `ACT-223`, `SYS-215`, `SYS-799`, `INF-119`, `OBJ-029`, `TIM-003` | Both directly move, attack and use a timed response through a real-time health-gated guardian encounter. Hollow Knight surrounds that encounter with Focus healing, checkpoint rest, recoverable death, currency, map exploration and persistent capability gates. This packet instead exposes local projectile paths, restricts parry to a marked hazard class, spends parry-fed meter on EX fire and settles the win through explicit result categories and an aggregate grade. | Near, `0.391304` |

- New genes: `SYS-822`, `CON-617`.
- Reused genes: `ACT-008`, `ACT-161`, `ACT-190`, `ACT-223`, `SYS-215`,
  `SYS-799`, `CON-324`, `INF-115`, `INF-119`, `INF-299`, `OBJ-029`,
  `TIM-003`.
- Classification result: `New gene`.
- Evidence and reasoning: marked-object parry eligibility and category-based
  graded encounter settlement remain mechanically distinct from timing alone,
  close-weapon readiness and reward-tier/chest settlement. Every other admitted
  verb, transition, disclosure, objective and clock already has a transferable
  lower-ID boundary.

### Preserved research notes

- New genes: `SYS-822`, `CON-617`.
- Reused genes: `ACT-008`, `ACT-161`, `ACT-190`, `ACT-223`, `SYS-215`,
  `SYS-799`, `CON-324`, `INF-115`, `INF-119`, `INF-299`, `OBJ-029`,
  `TIM-003`.
- Classification result: `New gene`.
- Evidence and reasoning: marked-object parry eligibility and category-based
  graded encounter settlement remain mechanically distinct from timing alone,
  close-weapon readiness and reward-tier/chest settlement. Every other admitted
  verb, transition, disclosure, objective and clock already has a transferable
  lower-ID boundary.

## Closure decisions

- The candidate's two genuinely new boundaries are preserved: `SYS-822` and
  `CON-617`.
- The draft's `SYS-623`/`SYS-822` concern is resolved conservatively. The
  generic graded encounter transition stays `SYS-822`; `SYS-623` remains a
  reviewed compound whose reward-tier and chest clauses are not silently
  removed. A future approved split may reuse `SYS-822` in `GAME-0193`.
- The Root Pack is a sequential encounter set, not one opponent transforming
  twice. `SYS-799` is generalised only where the same sealed encounter, arena
  and prior phase completion continue.
- The results card receives an Information boundary through generalised
  `INF-299`; the system transition and its disclosure are not conflated.

## Taxonomy impact

- Registry changes: `SYS-799` and `INF-299` receive portable wording and this
  game as supporting evidence; the twelve reused genes gain an independent
  carrier where their existing boundaries apply.
- Taxonomy change:
  [`TAXONOMY_CHANGE_037`](../../../research/taxonomy-changes/TAXONOMY_CHANGE_037.md).
- No lifecycle, earlier reviewed signature, combination or family changes.
- Candidate terms affected: fixed route identity, phase member, colour, weapon,
  exact HP, meter-card cost and grade thresholds remain parameters.

## Negative results

- No direct play, video or audio evidence was used. The complete written
  secondary sources are explicit; the search-indexed wiki text is never the
  sole support for a claim.
- No claim treats The Root Pack as the first mandatory boss. It is one of the
  initially available bosses, and all Regular boss levels are required later
  for progression.
- `Simple`, `Expert` and the secret route are excluded because they change
  phase content or grading conditions.
- Retry is not smuggled into the negative terminal: player death settles the
  failed trace, while selecting Retry starts another attempt.
- A target grade is not required. The objective is the win; grade is a visible
  system evaluation of the completed attempt.
- `COMB-0270` is recorded after the independently reviewed DAVE THE DIVER
  service provides a second carrier for graded bounded-activity settlement and
  the report that exposes its contributing categories.

## Delta summary

## New facts

- [Observation | Corroborated | High] `CUP-001`–`CUP-012`: the fixed Regular
  Root Pack packet is three sequential members, a pink-only timed parry economy,
  an explicit death terminal and a category-based graded win.

## New genes

- [Confirmed | Direct | High] `SYS-822`, `CON-617`: graded encounter settlement
  and parry eligibility based on a declared hazard class.

## New combinations

- [Pattern | Corroborated | High] `COMB-0270`, added during the later
  `GAME-0278` closure without changing this game's signature.

## Taxonomy changes

- [Confirmed | Corroborated | High] `SYS-799` now admits a replaced phase
  occupant inside the same sealed health-gated encounter; `INF-299` now admits
  any bounded results report with category values and aggregate evaluation.

## New questions

- Should reviewed compound `SYS-623` eventually split graded settlement from
  reward-tier and chest admission, adding `SYS-822` to `GAME-0193` under a
  separately approved earlier-signature migration?

## Next recommended game

- [Hypothesis | Limited | Medium] `GAME-0278` — DAVE THE DIVER.
- Optimisation criterion: leave a single real-time encounter for a bounded
  two-activity day cycle joined by one inventory.
- Expected information gain: tests whether the candidate's excursion capacity,
  stock-to-service conversion and day terminal survive independent review.
- Backlog impact: advances the recorded closure horizon by one unit.

## Why this game

- [Hypothesis | Limited | Medium] This closure shows that a compact boss packet
  still needs four distinct layers around the same visible projectile: direct
  response, timing legality, marked-class legality and resource consequence.
  It also separates successful grading from the results interface that explains
  the grade.
