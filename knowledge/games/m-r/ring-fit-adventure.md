---
game_id: GAME-0476
slug: ring-fit-adventure
game_title: Ring Fit Adventure
analysis_status: reviewed
reviewed: 2026-10-02
combination_ids: []
gene_ids:
  action:
    - ACT-626
    - ACT-627
    - ACT-628
    - ACT-629
  system:
    - SYS-578
    - SYS-1238
    - SYS-1239
    - SYS-1240
  constraint: []
  information:
    - INF-119
    - INF-450
  objective:
    - OBJ-268
  time:
    - TIM-001
---

# Game: Ring Fit Adventure — original Switch early World 1 route and first Fit Battle

Use the [canonical genome vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary). The Ring-Con, Leg Strap, Tipp, Hoplin, World and exercise names are carriers or parameters, not gene names.

## Analysis scope

- Version / ruleset: original 2019 Nintendo Switch *Ring Fit Adventure* in Adventure Mode, default jogging movement, from the start of World 1's second course, Transient Temple, through its goal and the first ordinary Hoplin Fit Battle that follows. This is an early two-node progression packet, not all of World 1. The course/encounter order comes from secondary World 1 documentation; Nintendo's own guide establishes the mechanics but does not name this precise course. Exact software revision and exercise-intensity setting were not inspected.
- Structured analysis target: original Switch software with a Switch Joy-Con (L) in the Leg Strap and Joy-Con (R) in a calibrated Ring-Con; see [`knowledge/platforms/games.json`](../../platforms/games.json). The setup is a prerequisite, not an in-course command.
- Entry: the first World 1 course, Beginnia, and initial tutorial are already complete. The selected next course, Transient Temple, is available; the ordinary first Fit Battle and boss have not yet been cleared. A player is properly equipped and the usual jogging mode is active.
- Primary decision loop: jog in place to move forward along the authored course; orient, squeeze or pull the Ring-Con for an eligible air blast, jump or nearby pickup; reach the course goal. In the following first battle, choose an available Fit Skill, copy Tipp's demonstrated physical motion through its guided repetitions, observe the performance grade and damage, then press and hold the ring against the abdomen until the enemy finishes attacking. Repeat if needed until the ordinary enemy is defeated.
- Positive terminal: the selected course has cleared and its subsequent first ordinary Fit Battle has been won, returning to a progressed World 1 map before the Dragaux boss. Course arrival alone does not complete this two-node packet.
- Negative terminal: hearts deplete in the battle before the enemy is defeated. An abandoned course or encounter is not a positive terminal. The exact retry prompt, damage constants and initial heart count are not claimed.
- Included: physical leg-sensor jogging; authored forward course; Ring-Con orientation, compression and pull for eligible route effects; visible course goal; first ordinary Fit Battle; currently available exercise selection; body-form and repetition guidance; immediate `Great`/`Good` feedback and its damage difference; enemy reply; held Ab Guard and heart damage; bounded map progression.
- Excluded: the introductory first course, Dragaux boss, World 2 and later Worlds, full workout routines, Quick/Custom/Multitask modes, Silent Mode's squat travel, post-World-2 colour advantage, World-3 shop and smoothies, later-unlocked Fit Skills, every hidden EXP medal, equipment, long-term levelling, daily fitness goals, exact exercise count or intensity, sensor calibration formula, guaranteed health benefit and Switch 2/Joy-Con 2 compatibility.
- Reproducible parameterisation: on an original Switch with original Joy-Con, complete onboarding and Beginnia, choose World 1's Transient Temple in default movement mode, jog through its route and use the ring on an eligible obstacle or nearby pickup if present; finish the course. Select the next first ordinary Fit Battle, perform one available skill with the prompted repetitions and observe its grade, then hold Ab Guard through an enemy response; finish the encounter and stop when map progression returns, before selecting Dragaux. To replicate exact outcomes, record software revision, selected intensity, calibrated sensors, selected skills, actual course objects and final battle state. None was captured here.
- Potential scoped modules: World 1 Dragaux boss, exact first-battle enemy-colour variation, repeatable EXP grinding, later colour advantage, exercise-slot restrictions and Silent Mode mapping each need their own evidence.
- Direct-play status: no Switch hardware, cartridge or digital executable, controller trace, game screenshot, video, audio or playthrough was inspected. Nintendo's support/product pages and a Nintendo-hosted GameWith editorial guide were read directly. Secondary World 1 guides only position the second course and following encounter. The art is original conceptual illustration, not a captured game frame.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `RF-001` | Original setup places a left Joy-Con in the Leg Strap and right Joy-Con in the Ring-Con; calibration precedes play. | Confirmed | Direct | High | P1 |
| `RF-002` | Default Adventure course movement is jogging in place; squeeze/pull of the ring gives air blast/jump or pickup suction on eligible scenery. | Confirmed | Direct | High | P2, P3 |
| `RF-003` | Adventure Worlds contain courses and enemy encounters; exercise skills resolve battles and route progression. | Confirmed | Direct | High | P2, P3 |
| `RF-004` | Tipp demonstrates the current skill; `Great` form deals more damage than `Good` and gives multimodal feedback. | Confirmed | Direct | High | P2, P3 |
| `RF-005` | An enemy turn is defended by pressing Ring-Con against the abdomen and holding until the attack ends; releasing early increases damage. | Confirmed | Direct | High | P2 |
| `RF-006` | World 1's second course is Transient Temple and an ordinary first Hoplin battle follows before Dragaux Stadium. | Observation | Corroborated | Medium | S1, S2 |
| `RF-007` | Enemy-colour attack advantage unlocks only after World 2, while the store appears from World 3, so neither belongs to this packet. | Confirmed | Direct | High | P2 |
| `RF-008` | Defeating enemies and clearing courses earns EXP, but all optional medals and later character growth are not required for this bounded exit. | Confirmed | Direct | High | P2 |

## Basic data

- Release / origin: Nintendo's original 2019 Nintendo Switch *Ring Fit Adventure*; no later hardware version is substituted.
- Platform or physical form: Nintendo Switch with detachable original Joy-Con, Ring-Con and Leg Strap.
- Mechanical family: real-time system pressure (`FAM-010`) applies to the physical form and held-guard intervals within an enemy exchange. Jogging itself advances only when the player moves; this family label does not assert an auto-running course.
- **P1:** [Nintendo Support, How to Start a New Game](https://en-americas-support.nintendo.com/app/answers/detail/a_id/47820/p/1095/c/182), accessed 2026-10-02. Hardware placement and calibration, not the World 1 route. The current support page mentions later hardware, but only original Switch Joy-Con setup is imported.
- **P2:** [Nintendo-hosted GameWith editorial, Beginner Basics for Ring Fit Adventure](https://www.nintendo.com/jp/ichikara/al3pa/02_en.html), accessed 2026-10-02. Nintendo-hosted but explicitly GameWith-authored: Adventure movement, Ring-Con route effects, Fit Skills, form grades, Ab Guard, progression and later unlock boundaries.
- **P3:** [Nintendo, Full-Body Adventuring](https://www.nintendo.com/ph/switch/al3p/adv/index.html), accessed 2026-10-02. Publisher description of physical traversal, course clearing and turn-based Fit Battles.
- **S1:** [Ring Fit Adventure Wiki, In the First Place](https://ringfitadventure.fandom.com/wiki/In_the_First_Place), search-index text accessed 2026-10-02; the page itself returned an access error. It places Beginnia, Transient Temple, a first Red/Blue Hoplin Fit Battle and Dragaux in that order. This is lower-confidence route evidence, not publisher authority.
- **S2:** [Ring Fit Adventure Wiki, Transient Temple (1-2)](https://ring-fit-adventure.fandom.com/wiki/Transient_Temple_%281-2%29), search-index text accessed 2026-10-02; page body was inaccessible. It independently names Transient Temple as World 1's second course; exact encounter geometry remains unverified.
- Claim IDs: `RF-001`–`RF-008`.

## Mechanical decomposition

### Action Genes

- New `ACT-626`: repeated strapped-leg jogging requests forward avatar travel. It is not a button-controlled run or Wii Balance Board weight transfer (`RF-001`, `RF-002`).
- New `ACT-627`: orient and physically compress or pull the ring for a local course effect. An eligible air blast may clear or bypass an obstacle; a pull may draw a nearby pickup. No particular hidden item in Transient Temple is claimed (`RF-002`).
- New `ACT-628`: select a currently available Fit Skill and perform its guided physical repetitions or hold to commit an attack (`RF-003`, `RF-004`).
- New `ACT-629`: sustain Ring-Con compression against the abdomen throughout an enemy strike for Ab Guard (`RF-005`).

### System Behaviour Genes

- New `SYS-1238`: leg-sensor movement maps to forward progress on the authored route. Stopping physical motion stops this requested advance (`RF-002`).
- New `SYS-1239`: accepted form and timing produce a `Great` or weaker `Good` outcome that changes combat damage. The exact coefficients are not claimed (`RF-004`).
- New `SYS-1240`: a sustained Ab Guard reduces the enemy attack's damage; early release allows more damage (`RF-005`). Reuse `SYS-578` for the current heart pool that can be lost to enemy attack, without importing later smoothie recovery into this early packet.
- Resolution order: sensor movement → course movement and eligible ring interaction → course goal and next map node → select available exercise → perform/grade repetitions → apply enemy damage → enemy attack and physical guard → reduce hearts as appropriate → repeat or settle battle/map progress.

### Constraint Genes

- None admitted. Ring hardware attachment is a prerequisite; skill availability and intensity are parameters of the present early encounter. Later colour matching is not an early legal-action constraint (`RF-007`).

### Information Genes

- New `INF-450`: Tipp shows the current exercise, and the game signals form with `Great`/`Good`, glow, sound and vibration. Reuse `INF-119` for currently displayed character resource state, including hearts, without claiming hidden exact attack multipliers (`RF-004`).

### Objective Genes

- New `OBJ-268`: clear the selected early course and the following first ordinary battle to preserve map progression before Dragaux. Boss defeat, all EXP medals and daily exercise targets do not substitute for this bounded terminal (`RF-006`, `RF-008`).

### Time Genes

- Reuse `TIM-001` for a player-selected Fit Skill followed by automatic enemy attack resolution; the player actively performs exercise or guard during those subphases, but no simultaneous hostile decision-maker is choosing moves. Do not import `TIM-003`'s forced autonomous progression into the player-jogged course.

## Reproducible transitions

| Before | Action or event | Bounded resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Selected course is active; avatar is stationary | Jog with strapped leg | Accepted physical steps move avatar forward on authored route | leg input, not a direction key, controls travel | `RF-001`, `RF-002` |
| Eligible route feature is visible | Orient and press Ring-Con | Air blast affects obstacle or can make an eligible jump | ring squeeze is a course command | `RF-002` |
| Eligible pickup is nearby | Pull Ring-Con | Suction draws the pickup if within current effect | pulling differs from air blast | `RF-002` |
| First ordinary enemy is active | Choose an available Fit Skill and follow Tipp | Repetitions produce `Great` or `Good`; better form deals more damage | exercise performance changes combat outcome | `RF-003`, `RF-004` |
| Enemy begins its attack | Hold ring against abdomen through the strike | Guard reduces damage; early release permits more | defensive duration has a consequential boundary | `RF-005` |
| Ordinary enemy health reaches zero before hearts do | Settle battle | First Fit Battle clears and World 1 map progression returns | positive packet terminal, not boss clear | `RF-006` |

## Strategic and experiential structure

- Local decision: physical pace advances the course; route features invite an oriented press or pull. In battle, select an available exercise the player can actually perform, copy Tipp and maintain the guard through the complete enemy reply.
- Medium term: a weak `Good` form result means less damage and potentially another exercise/enemy cycle; rushing the guard can spend more hearts. The visible grade helps attribute the difference without revealing exact coefficients.
- Long term: complete the course plus first battle while retaining enough hearts; EXP is a progression reward, not evidence of all-medal completion or a health benefit.
- Variation: intensity and calibration may change physical load, and the first enemy colour is reported as variable in the secondary guide. This record fixes neither exact repetitions nor a colour weakness, which is not unlocked yet.

## Replay and variation

The authored route and early encounter order are stable at the coarse level supported by the sources. Replaying can change the chosen available exercise, physical execution quality, heart loss and optional pickup result. The exact first-encounter enemy colour and sensor-calibrated workload are not fixed in this packet; no hidden random selection formula is claimed.

## Adjacent systems and history

*Wii Fit* (`GAME-0439`) also uses sensed body movement, but its Beginner Ski Slalom continuously maps Balance Board weight distribution to left/right steering and pace, then grades missed gates as an additive time penalty. This game uses leg jogging for forward route travel and Ring-Con manipulation for course affordances, then switches to form-graded exercise attacks and held physical guard against an enemy. *Paper Mario* (`GAME-0449`) also alternates chosen attacks and enemy replies, but its action command is a controller-timed input, not a physically guided multi-repetition workout.

## Normalised genome

| Type | Active gene IDs | Carrier parameters |
|---|---|---|
| Action | `ACT-626`, `ACT-627`, `ACT-628`, `ACT-629` | leg motion, Ring-Con press/pull, exercise, Ab Guard |
| System Behaviour | `SYS-578`, `SYS-1238`, `SYS-1239`, `SYS-1240` | hearts, route mapping, graded damage, guard mitigation |
| Constraint | none | setup and later unlocks are outside the packet |
| Information | `INF-119`, `INF-450` | current hearts, exercise demonstration and grade |
| Objective | `OBJ-268` | course plus first ordinary battle clear |
| Time | `TIM-001` | selected exercise and enemy response phases |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `475` (`GAME-0001`–`GAME-0475`).
- Exact genome matches: none.
- Tied near matches: `GAME-0268` — Undertale (`3 / 26 = 0.115385`).
- Supported combination subsets: none.
- Scan date: 2026-10-02.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0268` *Undertale* | `SYS-578`, `INF-119`, `TIM-001` | Both retain a visible health pool and alternate a chosen player command with an enemy reply. Undertale's first encounter uses command-menu choices and a moving-heart dodge arena; this game advances its earlier course by sensed jogging, resolves the attack through graded physical exercise, and mitigates the enemy reply by sustained Ring-Con compression. | `3 / 26 = 0.115385`; nearest non-exact earlier signature, not the same input or combat-resolution rule. |

## Taxonomy impact

`TAXONOMY_CHANGE_213` admits nine bounded new genes: four actions, three system behaviours, one information and one objective. `SYS-578`, `INF-119` and `TIM-001` transfer unchanged. Earlier signatures and verified combinations are not changed.

## Negative results

- Reject `ACT-575`/`SYS-1152`: a Balance Board's continuous weight distribution is not the Leg Strap's repeated jog or the Ring-Con's compression.
- Reject `SYS-1180`: its one timed button press is not an Ab Guard hold sustained for an enemy attack.
- Reject `TIM-003`: the course does not force forward progress while the player is motionless, and battle action is phased.
- Reject World-2 colour advantage, World-3 store, smoothies and late skills: they are not available in the selected early packet, regardless of how prominent they are in a complete-game description.

## Delta summary

## New facts

- [Confirmed | Direct | High] Nintendo describes physical course travel, Fit Skill form grades and held Ab Guard (`RF-001`–`RF-005`).
- [Observation | Corroborated | Medium] The specific World 1 two-node boundary uses independently indexed secondary route texts; the inaccessible full pages and absent direct play limit certainty (`RF-006`).

## New genes

- [Confirmed | Direct | High] Nine typed boundaries separate body input, sensed travel, exercise-graded damage and sustained protection.

## New combinations

- [Observation | Limited | Medium] None proposed; subset support is recomputed mechanically.

## Taxonomy changes

- [Confirmed | Direct | High] `TAXONOMY_CHANGE_213` adds nine boundaries without altering an earlier signature.

## New questions

- A version-pinned original Switch capture could establish the first battle's exact roster, exercise choices, step/rep calibration and damage coefficients; none is inferred here.

## Next recommended game

- [Hypothesis | Limited | Medium] `GAME-0477` *Catherine*, original PlayStation 3, after this unit's green gates, local commit and Goal stop window.
- The following selection batch should spread platforms deliberately rather than cluster Nintendo titles.
