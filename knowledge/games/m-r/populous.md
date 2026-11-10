---
game_id: GAME-0480
slug: populous
game_title: Populous
analysis_status: reviewed
reviewed: 2026-10-02
combination_ids: []
gene_ids:
  action:
    - ACT-599
    - ACT-634
    - ACT-635
    - ACT-636
  system:
    - SYS-002
    - SYS-045
    - SYS-046
    - SYS-051
    - SYS-1248
    - SYS-1249
    - SYS-1250
    - SYS-1251
    - SYS-1252
    - SYS-1253
    - SYS-1254
    - SYS-1255
  constraint:
    - CON-744
  information:
    - INF-454
    - INF-455
  objective:
    - OBJ-103
  time:
    - TIM-003
---

# Game: Populous — original Amiga declared Custom match

Use the [canonical genome vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Named miracles, field counts and power thresholds are parameters, not separate genes for every icon.

## Analysis scope

- Version / ruleset: original 1989 Bullfrog / Electronic Arts *Populous* for Amiga, documented by the original manual's explicit Amiga loading instructions and common rules. Exact executable revision, map seed, numeric rates and AI algorithm were not inspected. Later ports, expansions, *Populous II* and *The Beginning* are excluded.
- Structured analysis target: original Amiga (`PLAT-AMIGA`); see [`knowledge/platforms/games.json`](../../platforms/games.json).
- Primary decision loop: enlarge contiguous flat usable fields near friendly people to grow settlements and population; use the resulting manna to edit terrain or invoke permitted divine interventions; direct autonomous people through settlement, gathering, fighting or a leader-dependent magnet; query the resulting growth, strength and enemy position, then decide whether to expand, attack or irrevocably call Armageddon.
- Entry: one single-player Custom world, human Good versus computer Evil, with declared grass terrain, fatal water, bottomless swamps, building enabled, land raising and lowering near people, and both sides' terrain, attack and miracle permissions enabled in Game Balance. Population rate and computer aggression remain recorded preset parameters, not invented numeric defaults. Enter from the title's Custom setup and retain that world and preset for the match. This is not an assertion that Genesis, the first Conquest world, enables every power.
- Exit: one side loses every walker and settlement, or the player surrenders. Armageddon forces a final population battle inside this same match; it is not a separate campaign stage.
- Included: local terrain-height commands, usable farmland and settlement capacity, growth and walker emission, population-derived manna and spending, population behaviour modes, leader and magnet, autonomous travel/merging/combat/exhaustion, knight conversion, terrain disasters, final rally, command legality, live world and subject information, population elimination and real time with pause.
- Excluded: campaign progression and world passwords, tutorial instruction sequence, serial two-player communication, map painting and mid-match preset changes, harmful-water and shallow-swamp variants, only-raise or town-only building variants, external disk save/restore, exact map generation, rates, combat equations, power costs and height limits. Custom rules are declared analytically, not presented as original defaults; the manual allows these options but no executable run was performed.
- Reproducible parameterisation: pin an original Amiga executable and record the setup, map and rate/aggression values; follow a walker settling, expand its flat field footprint, wait for a full settlement to emit a walker, deliberately shrink a footprint, merge compatible walkers, move a magnet with/without a leader, exhaust an isolated walker, test flat/slope swamp targets, invoke a paid disaster, create a knight and call Armageddon. Record each transition and final elimination. Until that trace exists, the transitions below are source-based conditionals rather than fabricated measurements.
- Direct-play status: no executable, emulator, save, input trace, gameplay video or audio was inspected; no direct play was conducted. The original manual text and eight scanned pages were visually checked, including Amiga instructions, field geometry, command icons, disaster rules and custom options. Artwork is original interpretive art, not an exact map screenshot.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `POP-001` | Amiga input raises or lowers one addressed terrain point; usable flat fields determine settlement size and advancement, with a castle requiring at least a 5 × 5 field footprint. | Confirmed | Direct | High | P1 pp. 1, 7–8, 11 |
| `POP-002` | Settlement population grows toward capacity and releases a walker when full; reducing its usable land can force a walker out. Larger settlements can take fields from smaller neighbours. | Confirmed | Direct | High | P1 pp. 7–8, 24 |
| `POP-003` | Population and achievements produce manna; accepted divine interventions consume it and the bar's marker indicates available powers. Exact costs and accumulation equations remain unmeasured. | Confirmed | Direct | High | P1 pp. 4, 11–13 |
| `POP-004` | Global behaviour influences autonomous people: settle, gather then settle, fight then settle, or follow the papal magnet; magnet followers do not settle. Compatible walkers can merge into one stronger walker. | Confirmed | Direct | High | P1 pp. 8, 13–14 |
| `POP-005` | The first walker reaching the magnet becomes leader; moving it requires a leader. Leader death or knight conversion resets it to that last position until a replacement is formed. | Confirmed | Direct | High | P1 pp. 11–13 |
| `POP-006` | Walkers lose strength while travelling; terrain affects their survival. Knights autonomously seek enemy settlements, burn them and nearby fields, and can weaken and die. | Confirmed | Direct | High | P1 pp. 8–9, 12 |
| `POP-007` | Earthquake, swamp, volcano and flood alter terrain or occupancy; swamp targets must be flat, and flood raises the global sea one increment, affecting both sides. Fatal-water and bottomless-swamp settings are explicit options, not unconditional rules of every match. | Confirmed | Direct | High | P1 pp. 11–13, 17–19 |
| `POP-008` | Armageddon moves both magnets centrally, releases settlement populations into a forced final rally and battle, and prevents further player intervention from changing events. | Confirmed | Direct | High | P1 pp. 13, 24 |
| `POP-009` | The world book, local view, population gauges and manna bar expose current state; query tags expose a subject's faction, advancement, type and strength/growth, follow transfers, and support temporary zoom. The enemy cursor and exact future choices are not exposed. | Observation | Direct | High | P1 pp. 2–5, 14–15 |
| `POP-010` | Winning requires removing all opposing walkers and settlements; play is real-time and can be paused. Custom setup exposes the declared rules and per-side permissions; Conquest may lock options. | Confirmed | Direct | High | P1 pp. 3, 9–10, 15–19 |

## Basic data

- Release / origin: original 1989 Bullfrog god simulation published by Electronic Arts, with Amiga instructions in the inspected booklet. Precise release day and later DOS distribution do not define this analysis.
- Platform or physical form: Amiga computer with pointer and two mouse buttons; one indirect population match rather than a controlled combat avatar.
- Mechanical families: real-time system pressure (`FAM-010`), world topology and perspective (`FAM-014`) and agent routing and coordination (`FAM-015`). Height editing changes usable space, and global policies/magnet coordinate autonomous agents; theme alone is not the membership criterion.
- **P1:** [original Electronic Arts / Bullfrog manual scan](https://archive.org/details/populousmanual), copyright 1989, document 345205, accessed 2026-10-02. [Direct PDF](https://archive.org/download/populousmanual/Populous-Manual.pdf) and [OCR transcription](https://archive.org/stream/populousmanual/Populous-Manual_djvu.txt) are the same source, not independent corroboration. Printed pp. 1–19 and 24–26 support the rules; PDF leaves 5, 6, 12, 15–18 and 21 were visually inspected. The explicit Amiga instructions establish the target; the separately bundled PC reference card was not used.
- Claim IDs: `POP-001`–`POP-010`. Direct documentary evidence is not direct play or a binary-verified formula.

## Mechanical decomposition

### Action Genes

- Reuse `ACT-599`: select a currently available civilisation-level power and commit its legal local target or global activation. Earthquake, swamp, knight, volcano, flood and Armageddon have different effect parameters, not six copies of the same selection action (`POP-003`, `POP-007`, `POP-008`).
- New `ACT-634`: raise or lower one terrain point by a permitted increment. This changes settlement support rather than excavating an inventory material or firing into destructible cover (`POP-001`).
- New `ACT-635`: select one population-wide behaviour policy. It is not `ACT-036`'s addressed single-agent assignment; magnet following suspends settling while the other modes have settle fallbacks (`POP-004`).
- New `ACT-636`: relocate the population's attractor while a leader exists. Changing a destination for the global following policy is distinct from directly moving that leader (`POP-005`).

### System Behaviour Genes

- Reuse `SYS-002` for automatic same-faith walker merging; strengths and advancement are carrier parameters, not asserted tile-value doubling (`POP-004`).
- Reuse `SYS-045`, `SYS-046` and `SYS-051`: people travel autonomously, execute the currently imposed role and resolve eligible combat without per-step steering or per-strike commands (`POP-004`, `POP-006`).
- New `SYS-1248`: contiguous usable flat fields determine settlement footprint, capacity and advancement; larger neighbours can claim fields from smaller ones. Rocks, slopes and water can therefore prevent growth (`POP-001`, `POP-002`).
- New `SYS-1249`: automatic resident growth reaches capacity before emitting a walker; a reduced footprint can force that emission sooner. This is not a recruited production queue (`POP-002`).
- New `SYS-1250`: population and achievements feed a shared divine resource; accepted interventions consume it. There is no assigned praying workforce or proven cost equation (`POP-003`).
- New `SYS-1251`: autonomous travel drains walker strength according to terrain and can kill an unresettled walker. This is neither player-avatar hunger nor combat-only damage (`POP-006`).
- New `SYS-1252`: first eligible arrival supplies the unique leader, and leader removal rebinds the magnet to its last location pending replacement (`POP-005`).
- New `SYS-1253`: an accepted knight power converts the current leader and, if occupied, its settlement into an autonomous stronger attacker whose settlement burning also damages usable farmland. Ordinary autonomous target selection still belongs to `SYS-051` (`POP-006`).
- New `SYS-1254`: a paid terrain catastrophe resolves its declared local or global geometry/occupancy effect against both factions. Earthquake disturbs height, swamp replaces eligible flat land with a persistent drowning hazard, volcano raises obstructed terrain, and flood raises sea level one increment. These are a bounded terrain-calamity effect family; parameters preserve their target and outcome differences without asserting one identical algorithm (`POP-007`).
- New `SYS-1255`: Armageddon commits an irreversible terminal rally, empties settlements, shifts both attractors centrally, supplies crossings where necessary and removes further ordinary intervention. The final battle is not an ordinary freely redirected attack (`POP-008`).

### Constraint Genes

- New `CON-744`: each deity command requires its resource, permission and target predicate; terrain edits need a friendly person or town visible locally under the declared near-people rule, swamp needs flat land, and magnet relocation needs a leader. The setup's permission switches and manna marker are eligibility, not universal cooldowns (`POP-001`, `POP-003`, `POP-005`, `POP-007`, `POP-010`).

### Information Genes

- New `INF-454`: live global terrain/faction book and local close-up combine with population and power-availability gauges. Seeing the current map does not expose an enemy cursor, every internal numeric state or future AI actions (`POP-009`).
- New `INF-455`: a query tag exposes one subject's faction, advancement, class and strength/growth; it follows entry/exit, transfers to a surviving opponent after combat death and disappears without a successor. A zoom command briefly shows its subject's information on the shield before restoring the tagged subject's information or a blank shield; this does not establish automatic camera return (`POP-009`).

### Objective Genes

- Reuse `OBJ-103`: remove the opposing civilisation's surviving population and productive settlements before one's own elimination. Leader death or a larger headcount alone is not victory; there is no campaign score objective inside this match (`POP-010`).

### Time Genes

- Reuse `TIM-003`: people, growth and combat continue during player deliberation unless explicitly paused. No fixed phase schedule or exact simulation rate is asserted (`POP-010`).

## Reproducible transitions

| Before | Action or event | Bounded resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Friendly walker, usable flat land, settle policy | Wait | Walker creates a settlement with fields; size depends on usable footprint | Indirect settlement creation | `POP-001`, `POP-004` |
| Settlement beside a slope, eligible manna and local friendly presence | Flatten by addressed height edits | Usable fields can expand and settlement capacity/advancement respond | Geometry affects population opportunities | `POP-001`, `POP-002` |
| Growing settlement below capacity | Allow growth to fill it | Emits a new walker at capacity; shrinking usable land can force emission | Growth/capacity transition, not queued recruitment | `POP-002` |
| Two compatible same-faith walkers | Their autonomous paths meet | Merge into one stronger walker according to existing strength/advancement | Compatible actor replacement | `POP-004` |
| No current leader | Try moving magnet, then let a walker reach it | Relocation needs leader presence; arrival supplies the leader | Attractor command legality | `POP-005` |
| Current leader at a town and knight power available | Invoke knight | Leader and occupied settlement convert; magnet resets to that location | Promotion and replacement dependency | `POP-005`, `POP-006` |
| Available swamp power, a sloped target | Submit target | Flatness requirement prevents that target; a legal flat bottomless swamp persists after a victim | Predicate versus aftermath | `POP-007` |
| Both populations occupy low land and flood is available | Invoke flood | Sea rises one increment; fatal water can kill exposed people on either side | Global friendly-fire risk | `POP-007` |
| Tag follows a walker into a settlement | Enter, later leave, or die in combat | Subject and displayed information transfer as documented | Query state is not a frozen inspector | `POP-009` |
| Match active, Armageddon available | Invoke it | Both magnets centralise, populations leave homes, final battle proceeds without further altering intervention | Irreversible terminal policy | `POP-008` |
| Enemy leader dead but another settlement survives | Continue simulation | Enemy civilisation is not yet eliminated | Full population/settlement objective | `POP-010` |

## Strategic and experiential structure

Flattening more land creates room for a larger settlement, but a full large settlement takes longer to emit a walker. Shrinking its footprint can deliberately produce a follower earlier. That follower may claim new land, strengthen another walker, become leader or exhaust itself. Population supplies the manna used to expand or attack, so a catastrophe can damage one's own future source of power as well as the enemy. Magnet following trades settlement for rallying; knight promotion spends the leader relationship; Armageddon replaces further shaping with a committed final confrontation. These coupled choices distinguish indirect population control from ordinary selected-unit real-time strategy.

## Replay and variation

Custom maps and declared rate/aggression parameters may vary between new matches. They do not justify claiming a particular seed, starting population, numerical efficiency or universally unlocked Conquest powers. The current analysis retains one setup for the whole match; editing the rules or loading an external saved state is a potential separate module, not a hidden assumption.

## Adjacent systems and history

The original manual uses a global deity vocabulary but describes concrete terrain and population transitions. Later franchise powers and rendered avatars cannot be projected back into this original Amiga packet. The Black & White prayer-worker boundary was tested and rejected: Populous manna is population/achievement-derived, not a selected workforce diverted to a worship site.

## Normalised genome

| Type | Active gene IDs | Carrier parameters |
|---|---|---|
| Action | `ACT-599`, `ACT-634`, `ACT-635`, `ACT-636` | power, point height, global policy and magnet destination |
| System Behaviour | `SYS-002`, `SYS-045`, `SYS-046`, `SYS-051`, `SYS-1248`–`SYS-1255` | merging, autonomous people, fields, growth, manna, exhaustion, leader, knight, catastrophe and final rally |
| Constraint | `CON-744` | resource, local presence, leader, flat target and permissions |
| Information | `INF-454`, `INF-455` | global/local current state and queried subject |
| Objective | `OBJ-103` | opposing population and settlements eliminated |
| Time | `TIM-003` | live match with explicit pause |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `479` (`GAME-0001`–`GAME-0479`).
- Exact genome matches: none.
- Tied near matches: `GAME-0025` — Lemmings (`3 / 29 = 0.103448`).
- Supported combination subsets: none.
- Scan date: 2026-10-02.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0025` *Lemmings* | `SYS-045`, `SYS-046`, `TIM-003`: autonomous movement, assigned-role execution and a live simulation. | Populous indirectly shapes field capacity, population manna and a leader-dependent rally, permits civilisation-level disasters and commits an irreversible final battle. Lemmings instead assigns addressed walkers traversal roles to meet an exit quota under its level limits; that command and objective boundary does not transfer. | `3 / 29 = 0.103448`; nearest non-exact prior signature, not the same population-control loop. |

## Taxonomy impact

`TAXONOMY_CHANGE_217` admits fourteen bounded genes and reuses seven unchanged boundaries. No earlier genome, definition or verified combination changes. The named salience review partitions all twenty-one uses after reading this complete scope; it is presentation, not numerical weighting.

## Negative results

- Reject `ACT-036` and `ACT-317`: a population-wide behavioural directive is not a selected agent's assignment or a formation/stance command.
- Reject `SYS-1188`: manna does not require a separately assigned praying workforce with a labour trade-off.
- Reject `SYS-327`: travelling walkers are autonomous population actors, not the embodied player's needs simulation.
- Reject `INF-001`: map visibility is not complete exposure of every decision-relevant internal state.
- Reject `OBJ-029`: this civilisation continually grows/rebuilds, unlike a fixed encounter population.
- Reject one gene per named power and Conquest-default all-power availability. Preserve catastrophe outcome parameters and the explicit Custom preset instead.

## Delta summary

## New facts

- [Confirmed | Direct | High] Flat field footprint connects settlement advancement, growth, walker release and manna production (`POP-001`–`POP-003`).
- [Confirmed | Direct | High] Population policies, leader-dependent magnet and irreversible final rally are different control boundaries (`POP-004`, `POP-005`, `POP-008`).

## New genes

- [Observation | Direct | High] Fourteen boundaries cover terrain commands, global directives, magnet, field/growth/resource transitions, autonomous exhaustion, leader/knight conversion, disasters, final rally, legality and information.

## New combinations

- [Observation | Limited | Medium] No new verified combination proposed; existing proper subsets are recomputed against the complete signature.

## Taxonomy changes

- [Observation | Direct | High] `TAXONOMY_CHANGE_217`; earlier signatures remain unchanged.

## New questions

- A version-pinned Amiga trace should establish exact rate/aggression values, current-world geometry, power thresholds, exhaustion and combat equations, and final rally timing. No later-port values fill those gaps.

## Next recommended game

- [Hypothesis | Limited | Medium] `GAME-0481` *Out Run*, original Sega arcade, follows full acceptance and the Goal stop window.
- Optimisation criterion: move from indirect population/terrain control to a continuously driven branching arcade route on another platform.
