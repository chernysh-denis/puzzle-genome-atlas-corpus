---
game_id: GAME-0303
slug: sifu
game_title: Sifu
analysis_status: reviewed
reviewed: 2026-09-18
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-161
    - ACT-223
    - ACT-383
    - ACT-419
    - ACT-462
    - ACT-463
  system:
    - SYS-035
    - SYS-215
    - SYS-409
    - SYS-578
    - SYS-877
    - SYS-878
    - SYS-879
  constraint:
    - CON-282
    - CON-324
    - CON-589
    - CON-639
  information:
    - INF-119
    - INF-142
    - INF-295
    - INF-334
  objective:
    - OBJ-080
  time:
    - TIM-003
---

# Game: Sifu

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Product names,
amounts and moves are parameters, not new gene labels.

## Analysis scope

- Version / ruleset: the English PS5 build delivered by the PlayStation Store
  **Standard Edition PS4 & PS5** entitlement, unmodified, solo and offline, on
  **Disciple** difficulty. Disciple is the original ordinary ruleset according
  to Sloclap's `1.08` patch note. The last official patch note located for
  this review is `1.26` (2023-10-19), but no installed PS5 build was observed;
  this is a documentation horizon, not a claim that a console runs `1.26`.
  The storefront's default Deluxe selection is not this packet's SKU. The
  earlier search-selection packet's Windows/Steam provenance is not reused.
- Entry: fresh Standard Edition story save, required prologue completed, then
  ordinary first Hideout **The Squats** from the Wuguan on Disciple. The
  character starts at age 20. No earlier unlocked shortcut, permanently
  unlocked skill or other completed Hideout is admitted.
- Primary decision loop: traverse the authored first Hideout and choose a
  position among simultaneous enemies; read incoming motion and personal and
  opponent Structure; attack or use the arena's reachable improvised objects;
  hold guard or time a deflection, spatial dodge or high/low avoid; exploit a
  Structure break for a prompted takedown; build Focus through combat, then
  spend an available Focus charge on a targeted weak-point technique; after
  lethal defeat decide whether to rise with the pendant, trading a higher age
  and escalating death counter for same-encounter continuation. Defeat Fajar
  at the first Hideout's end and return to Wuguan. Exact attack order, damage,
  score, age at victory, optional pickups and number of deaths vary.
- Positive terminal: defeat the required first boss Fajar in both encounter
  phases, finish The Squats, and regain Wuguan control with The Club available.
  Official rules say chapter completion records the finishing age and resets
  the death counter; the Wuguan successor is supported by a written boss
  route. This project did **not** execute the route or verify a reload.
- Negative terminal: if the pendant cannot or is not used after lethal defeat,
  the current attempt ends. Ordinary game-over loses temporary skills and
  Shrine upgrades; previously earned permanent skill unlocks and Detective
  Board information survive. The age eligibility threshold, precise restart
  UI and retained post-patch save data require direct PS5 verification.
- Included: ordinary fresh-story traversal and combat; personal health and
  both sides' breakable Structure; guard, timed deflection, dodge and high/low
  avoid; responsive target changes; a prompted takedown; combat-earned Focus
  and one charged weak-point technique; age/death-counter escalation and
  same-place pendant revival; first Hideout access sequence, Fajar's two
  phases, chapter age save and death-counter reset. The existence of Shrines,
  skill buying and Detective Board retention is recorded as context, but no
  optional perk/skill purchase or board-completion route is performed.
- Excluded: Student or Master difficulty, Arenas, Goals, Cheats/Modifiers,
  Deluxe content, costumes, training replays, later Hideouts and bosses,
  spare/alternative-ending route, full Detective Board, optional shrine-perk
  optimisation, permanent skill grind, shortcut replay, leaderboards, scores,
  trophies, non-PS5 versions, mods and audiovisual evidence. The exclusion
  limits this *packet*, not what Sifu contains.
- Reproducible parameterisation: use the English PS5 Standard build; record
  the installed version in a future console run; choose Disciple and a clean
  save; finish the mandatory prologue and enter The Squats without a shortcut.
  Follow the ordinary apartment, corridor, hangar and botanist approach in
  the two written routes. Demonstrate at least one held block, one timed
  deflection, one high/low avoid, one Structure-break takedown, one Focus
  attack and (if feasible without ending the run) one pendant revival. Defeat
  both Fajar phases, record age and death counter on chapter settlement, then
  inspect Wuguan and reload once. This is a **future test protocol**, not a
  claim those interactions were directly observed for this record.
- Potential later modules: shrine-perk choices, skill permanence after patch
  `1.12`, shortcut reuse and route score, later Hideouts, spare ending and
  Arenas each require a separate entry, loop, terminal and evidence boundary.
- Direct-play status: not conducted. No PS5 hardware, entitlement, install,
  displayed patch or save was available to this unit. Primary Sloclap/Sony
  text establishes product and rules; two independent written routes support
  the level and boss sequence. This is a sourced reconstruction, not a claimed
  played or reload-verified result. No video or audio was opened, played,
  heard or analysed.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `SIF-001` | PlayStation offers a PS4/PS5 Standard Edition separately from Deluxe; the packet selects PS5 Standard | Confirmed | Direct | High | P1 |
| `SIF-002` | Disciple is the original normal ruleset, unlike the later Student and Master settings | Confirmed | Direct | High | P4 |
| `SIF-003` | Both combatants have Structure; enemy break opens a takedown while own break creates vulnerability | Confirmed | Direct | High | P2 |
| `SIF-004` | Guard, timed parry, dodge and high/low avoid are distinct defensive commitments | Confirmed | Direct | High | P2 |
| `SIF-005` | Focus accrues in combat and a spent charge slows time for a selected weak-point technique | Confirmed | Direct | High | P2 |
| `SIF-006` | Pendant revival keeps the encounter going, increases age by the death counter and eventually becomes unavailable | Confirmed | Direct | High | P3 |
| `SIF-007` | Chapter completion resets the death counter, not age, and makes a save point at the finishing age | Confirmed | Direct | High | P3 |
| `SIF-008` | The first ordinary Hideout is The Squats, with Fajar as its two-phase final boss, then Wuguan and The Club | Observation | Corroborated | Medium | S1, S2 |
| `SIF-009` | Shrines offer perks; ordinary game over discards temporary improvements, while permanent skills and Detective Board clues persist | Confirmed | Direct | High | P3, P5 |
| `SIF-010` | Arenas and optional Cheats/Modifiers were added later and are not intrinsic to the fresh first-story route | Confirmed | Direct | High | P5, P6 |
| `SIF-011` | No direct PS5 route, installed-build or reload check was possible | Confirmed | Direct | High | R1 |

## Basic data

- Origin: Sloclap, 2022; Standard Edition digital entitlement for PS4 and PS5.
- Platform/form: PS5 Standard Edition, offline solo, Disciple, fresh story.
- Mechanical families: tactical forecast and counterplay; real-time system
  pressure; ordered dependency sequencing.
- Primary and official sources, checked 2026-09-18:
  - **P1** — [PlayStation Store Sifu editions](https://store.playstation.com/en-us/product/UP2703-PPSA05132_00-7522931300249907/),
    including the Standard-versus-Deluxe boundary and offline PS5 entitlement.
  - **P2** — [Sloclap combat-system article on PlayStation Blog](https://blog.playstation.com/2021/11/18/how-sifus-kung-fu-combat-works/),
    for Structure, guard, parry, dodge/avoid, target switching, environment and Focus.
  - **P3** — [Sloclap death-and-aging article on PlayStation Blog](https://blog.playstation.com/?p=356878),
    for age, death counter, pendant, Shrines, chapter save, skill and board persistence.
  - **P4** — [Sloclap patch `1.08`](https://www.sifugame.com/news/patch-1-08-spring-2022-content-update),
    for the new difficulty settings and Disciple as the original ruleset.
  - **P5** — [Sloclap patch `1.12`](https://www.sifugame.com/news/patch-1-12-summer-content-update),
    for score, Cheats/Modifiers and changed permanent-skill counters.
  - **P6** — [Sloclap final Arenas update `1.24`](https://www.sifugame.com/news/patch-1-24-the-final-content-update-is-out)
    and [hotfix `1.26`](https://www.sifugame.com/news/patch-1-26-hotfix),
    for optional mode and patch-documentation boundary, not installed PS5 version.
- Corroborating written routes, checked 2026-09-18:
  - **S1** — [Outsider Gaming first-Hideout route](https://outsidergaming.com/sifu-walkthrough-of-level-one-the-squats/),
    for apartment, long corridor, warehouse, Fajar and ordinary level clear.
  - **S2** — [EIP Gaming Fajar boss route](https://eip.gg/sifu/guides/how-to-beat-the-fajar-botanist-squats-boss/)
    and [The Squats route](https://eip.gg/sifu/guides/the-squats-walkthrough/),
    for the independent boss-to-Wuguan successor and chapter structure.
- **R1** — Local preflight found no PS5, entitlement, installation, version
  screen or saved first-Hideout run; no audiovisual evidence was used.

## Mechanical decomposition

### Actions

- Reuse `ACT-008` for route movement, `ACT-161` for ordinary close strikes,
  `ACT-223` for timed parry/dodge/avoid, `ACT-383` for held guard and
  `ACT-419` for a prompted close takedown after an opening. `ACT-462` commits
  a Focus-charged targeted technique; `ACT-463` confirms pendant revival from
  the defeat interval. Neither is a weapon-specific God of War Focus Strike
  or Sekiro's charge-paid Resurrection.

### System behaviours and constraints

- `SYS-215` owns simultaneous hostile combat, `SYS-409` the Structure-break
  opening, `SYS-578` continuous health and `SYS-035` combat-earned Focus
  supply. `SYS-877` slows selection and settles the charged Focus technique;
  `SYS-878` restores the downed fighter in place while increasing age by the
  current death counter; `SYS-879` retains chapter finishing age and resets
  the death counter without claiming a performed reload. `CON-324` requires
  the right defence window, `CON-589` a live takedown opening, `CON-639` enough
  remaining pendant life to rise, and `CON-282` the required first-Hideout
  route and guardian threshold.

### Information, objective and time

- `INF-119` presents health, Structure, Focus, age and death-counter state;
  `INF-142` incoming motion, `INF-295` the exposed takedown window and
  `INF-334` enemy Structure. `OBJ-080` requires Fajar and the Wuguan
  successor; `TIM-003` owns real-time commitments under continuing attacks.

## Reproducible transitions

| Before | Player action | Bounded resolution | Claim |
|---|---|---|---|
| Enemy pressure and intact personal Structure | Hold guard or time a parry/avoid | Ordinary guard adds Structure pressure; precise defence avoids or redirects the hit | `SIF-003`, `SIF-004` |
| Enemy Structure reaches its threshold | Commit prompted close takedown | A short execution opening converts accumulated stance pressure into defeat or major damage | `SIF-003` |
| Focus charge is available | Select and commit one weak-point technique | Time slows during selection and a charged targeted effect resolves | `SIF-005` |
| Health reaches zero while revival is eligible | Confirm pendant revival | Control resumes in place; age rises by the death counter, making repeated errors costlier | `SIF-006` |
| Fajar's final phase settles | Accept chapter completion | The Squats clears; finishing age is saved, counter resets and Wuguan gives access to The Club | `SIF-007`, `SIF-008` |

## Strategic and experiential structure

Every defence is a trade: a held block is reliable but fills personal
Structure; a timed parry or vertical avoid can turn the same incoming attack
into an opening. Focus converts sustained performance into a deliberately
targeted interruption. Death is recoverable in place but not free: as the
counter rises, each next mistake consumes more of a finite age budget.
Clearing the first Hideout locks in the age that a later route inherits.

## Replay and variation

Route, enemy arrangement, improvised weapon, Focus timing, shrine choice,
death count and finishing age vary within this boundary. Optional shortcuts
and permanent skill planning can change a later replay, but neither is used
to define this clean first entry.

## Adjacent systems and history

Sekiro also fills a separate combat-stability state and converts its break
into a close execution. Sifu's own Structure makes held guard risky, while
its revival is paid by escalating age rather than a ready combat charge.
Nioh 2 instead prices both offence and evasion in one recovering Ki reserve
and refunds part through Ki Pulse. No older definition changes simply to
increase this game's apparent similarity.

## Normalised genome

| Type | Active gene IDs | Parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-161`, `ACT-223`, `ACT-383`, `ACT-419`, `ACT-462`, `ACT-463` | route, attack, response, Focus and revival |
| System Behaviour | `SYS-035`, `SYS-215`, `SYS-409`, `SYS-578`, `SYS-877`, `SYS-878`, `SYS-879` | Focus, Structure, health, age and chapter save |
| Constraint | `CON-282`, `CON-324`, `CON-589`, `CON-639` | route, window, opening and life limit |
| Information | `INF-119`, `INF-142`, `INF-295`, `INF-334` | personal and enemy gauges, cues |
| Objective | `OBJ-080` | Fajar and Wuguan successor |
| Time | `TIM-003` | live combat |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `302` (`GAME-0001`–`GAME-0302`).
- Exact genome matches: none.
- Tied near matches: `GAME-0288` — Sekiro™: Shadows Die Twice - GOTY Edition (`18 / 44 = 0.409091`).
- Supported combination subsets: none.
- Scan date: 2026-09-18.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0288` — Sekiro™: Shadows Die Twice - GOTY Edition | `ACT-008`, `ACT-161`, `ACT-223`, `ACT-383`, `ACT-419`, `SYS-035`, `SYS-215`, `SYS-409`, `SYS-578`, `CON-282`, `CON-324`, `CON-589`, `INF-119`, `INF-142`, `INF-295`, `INF-334`, `OBJ-080`, `TIM-003` | Both reward timed defence and Structure/Posture breaks. Sifu builds Focus and ages with an escalating death counter; Sekiro builds a Resurrection charge and pays a true-death checkpoint penalty. | Near, `18 / 44 = 0.409091` |

## Taxonomy impact

- New: `ACT-462`–`ACT-463`, `SYS-877`–`SYS-879`, `CON-639`. These isolate
  Sifu's charged target choice, pendant decision, revival-age escalation,
  chapter age settlement and age-based revival legality. Earlier signatures
  remain unchanged; no verified combination is proposed.

## Negative results

- Reject `ACT-452`, `SYS-848` and `CON-628`: Sifu's pendant is not Sekiro's
  combat-earned ready-charge Resurrection with a post-use lock.
- Reject `SYS-798`: Structure is a breakable defensive state, not Nioh's
  shared expenditure reserve for attacks and evasions.
- Do not infer an installed PS5 patch, personally witnessed Wuguan reload,
  optional shrine path or exact current Fajar attack frame from these sources.

## Delta summary

## New facts

- [Observation | Corroborated | Medium] `SIF-001`–`SIF-011` bound the PS5
  Standard first-Hideout Disciple route and explicitly separate official
  rules from the source-based Fajar/Wuguan reconstruction.

## New genes

- [Pattern | Corroborated | Medium] Six portable candidates distinguish
  Focus targeting and settlement, pendant revival and its age budget, chapter
  checkpoint retention and eligibility from earlier combat signatures.

## New combinations

- None proposed without a reviewed recurring proper-subset interaction.

## Taxonomy changes

- None to existing definitions or historical signatures.

## Inferences

- [Strong Pattern | Corroborated | Medium] The cheapest safe action changes
  as Structure and remaining revival age change: a conservative block can
  protect immediate health yet worsen the next exposed-break risk.

## Open questions

- Which exact PS5 patch is installed, and does the current offline chapter
  settlement/reload retain every documented field exactly as the written
  sources describe? This requires a lawful console run.

## Contradictions

- None established within the admitted Disciple first-Hideout packet.

## New questions

- Does a separate shortcut/skill-permanence packet introduce a portable
  retained-investigation route beyond the age checkpoint?

## Next recommended game

- [Hypothesis | Limited | Medium] `GAME-0304` Azul, original physical base
  game under current official English rules, is the next selected unit.
- Optimisation criterion: replace live combat and age pressure with complete
  open tabletop drafting and spatial score adjudication.
- Expected information gain: shared display depletion and round scoring.

## Why this game

- [Hypothesis | Corroborated | Medium] Sifu tests whether a familiar
  Structure-break and close-finisher signature remains distinct when each
  in-place revival irreversibly spends age and chapter settlement locks the
  next route's starting state.

## Confidence and unresolved questions

- High for officially documented core rules and Standard/Disciple identity;
  Medium for the two-source first-Hideout route and Wuguan terminal; no direct
  PS5 execution, installed-build observation or reload claim.
