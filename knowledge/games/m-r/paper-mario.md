---
game_id: GAME-0449
slug: paper-mario
game_title: Paper Mario
analysis_status: reviewed
reviewed: 2026-09-28
combination_ids: []
gene_ids:
  action:
    - ACT-019
    - ACT-222
    - ACT-590
    - ACT-591
    - ACT-592
  system:
    - SYS-358
    - SYS-1178
    - SYS-1179
    - SYS-1180
  constraint:
    - CON-724
    - CON-725
  information:
    - INF-142
    - INF-434
  objective:
    - OBJ-029
  time:
    - TIM-001
---

# Game: Paper Mario — the four-Fuzzy battle after Kooper joins

Use the [canonical vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Names, button mappings, FP costs and enemy counts are parameters, not standalone genes.

## Analysis scope

- Version / ruleset: original English Nintendo 64 *Paper Mario*, the authored four-Fuzzy fight behind Koopa Village immediately after recovering Kooper's shell and accepting him as a partner. The exact cartridge revision was not inspected. Nintendo's original manual governs combat rules; two original-N64 written routes bind the encounter.
- Primary decision loop: inspect the four Fuzzies and Mario's HP/FP; choose Mario's jump, hammer or a legal item and Kooper's Shell Toss or FP-paid Power Shell, optionally change the one active partner to Goombario or trade the Mario/partner action order before either acts; execute offensive timing prompts, then time an A-button defence against a Fuzzy's HP-draining hit. Repeat the paired player actions and hostile response until all four are defeated or Mario reaches zero HP.
- Entry and exit: Kooper has just joined after his shell is returned; moving away triggers the fixed four-Fuzzy battle. The packet ends with victory's Star Point settlement or Mario's defeat. It does not include the preceding shell-tracking minigame, earlier two-Fuzzy fights, the next field route or later chapter objectives.
- Included: Mario plus one active partner, possible partner substitution and pre-action order swap, actor-specific commands and attack target legality, FP gate for Power Shell, action-command timing on attacks and defence, Fuzzy HP theft/restoration, finite enemy clearance, HP/FP and combat feedback.
- Excluded: exact opening HP/FP, equipped badges and inventory, guaranteed optimal move sequence, first-strike bonus, unobserved enemy AI ordering, exact Action Command frames, fleeing, Star Spirit abilities (not yet rescued), later partner ranks, level-up choices and post-battle travel. Badge configuration may affect an actual save but is deliberately not asserted for this packet.
- Direct-play status: no original cartridge, save state, video, audio or controller trace was inspected. The official manual directly establishes combat rules, while written firsthand routes corroborate this particular scripted fight. Exact timing windows, opening resources and outcome of a specific played attempt are unmeasured.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `PM-001` | Returning Kooper's shell recruits him, and moving away triggers a battle against four Fuzzies in the original N64 route. | Observation | Corroborated | High | S1, S2 |
| `PM-002` | Mario and one active partner normally each receive one action during the player portion; all enemies defeated wins, while Mario's zero HP ends the attempt. | Observation | Corroborated | High | P1, S1 |
| `PM-003` | An available partner can be changed and Mario/partner order swapped with Z only before either has acted. | Observation | Direct | High | P1 |
| `PM-004` | Jump, hammer and partner attacks have different legal target positions; special attacks require available FP. | Observation | Direct | High | P1 |
| `PM-005` | A successful prompted offensive Action Command increases or modifies attack effect; A just before an incoming hit reduces damage. | Observation | Direct | High | P1 |
| `PM-006` | Fuzzies can drain one Mario HP and regain one HP on a successful bite; Power Shell is an optional multi-target answer. | Observation | Corroborated | Medium | S1, S2 |
| `PM-007` | Defeating the finite encounter awards Star Points; exact award varies with strength and Mario's level. | Observation | Direct | High | P1 |
| `PM-008` | Cartridge build, exact encounter replay, starting resources, enemy decision policy and exact input frames were not inspected. | Confirmed | Direct | High | R1 |

## Basic data

- Origin: Intelligent Systems / Nintendo original Nintendo 64 role-playing game; this is not *The Thousand-Year Door*, a remake or a later series rule set.
- Platform: Nintendo 64 controller; structured target in `knowledge/platforms/games.json`.
- Mechanical families: tactical forecast and counterplay (`FAM-009`) and ordered dependency sequencing (`FAM-017`) within a finite paired-action encounter.
- **P1:** [Nintendo's original English Nintendo 64 Paper Mario manual](https://www.nintendo.com/eu/media/downloads/games_8/emanuals/nintendo_8/Manual_Nintendo64_PaperMario_EN.pdf), pp. 14–22, inspected 2026-09-28. It establishes one on-screen partner, battle turn structure, attack and FP commands, position legality, Action Command timing, Z-order exchange, partner change, HUD/damage and battle settlement.
- **S1:** [GameFAQs original-N64 Koopa Village route](https://gamefaqs.gamespot.com/n64/198849-paper-mario/faqs/73987/fuzzy-crisis-in-koopa-village), inspected 2026-09-28. The author's walkthrough identifies Kooper's recruitment followed by four Fuzzies, their HP drain and the Shell Toss/Power Shell options. It is encounter evidence, not authority to generalise all enemy behaviour.
- **S2:** [TDog's original-N64 chapter-one route](https://gamefaqs.gamespot.com/n64/198849-paper-mario/faqs/14327), inspected 2026-09-28. Independently identifies the four-Fuzzy post-recruitment battle and their healing after a successful attack.
- **R1:** local preflight found no original N64 installation, cartridge, recording or direct-play trace for this unit.

## Mechanical decomposition

### Action Genes

- Reuse `ACT-019`: pick Mario's jump or hammer, or Kooper's Shell Toss/Power Shell, and a legal target or target group. The command selection is distinct from the prompted execution.
- Reuse `ACT-222`: perform a successful jump, hammer or partner-attack Action Command at its own cue. It does not select an enemy or replace the whole turn.
- `ACT-590` changes which of two recruited partners occupies the sole active helper slot during battle. Kooper and Goombario offer different commands; this is not Pokémon-style replacement of the sole battling creature while the trainer stays outside combat.
- `ACT-591` trades the order of Mario's and the active partner's actions with Z, but only before either has used their action this turn.
- `ACT-592` presses A just before a Fuzzy's contact to reduce incoming damage; it does not dodge, parry for a counter, or fully cancel the attack as assumed by `ACT-223`.

### System Behaviour Genes

- Reuse `SYS-358`: grade the prompted offensive input and modify the selected attack's effect.
- `SYS-1178` grants Mario and the current partner their separate player actions before hostile replies, then repeats if both sides remain. A swapped order does not add an action; defeating all four Fuzzies ends the exchange.
- `SYS-1179` resolves a successful Fuzzy latch as Mario HP lost and enemy HP restored. The route reports one point each; a defended or missed attack must not be counted as a guaranteed heal.
- `SYS-1180` applies the timed A defence as damage reduction on the incoming attack. The official manual does not promise zero damage or a counterattack.

### Constraint Genes

- `CON-724` keeps jump, hammer and partner techniques within their respective legal target positions. Here Fuzzies are grounded, but the rule still matters to command availability; hammer normally reaches only the front ground enemy, whereas jump can reach those behind. No spiked or airborne enemy is in this packet.
- `CON-725` permits Power Shell only with its available FP cost; ordinary attacks remain usable without FP. FP cost is a parameter, and the exact starting balance is not assumed.

### Information, Objective and Time Genes

- Reuse `INF-142`: motion and the visible Action Command prompt cue the instant for offensive/defensive input without displaying exact timing frames.
- `INF-434` exposes Mario's HP/FP, active partner and selected command/target plus damage, recovery and abnormal-condition feedback. It does not disclose a future enemy attack policy.
- Reuse `OBJ-029`: clear the four-member hostile set before Mario's HP is exhausted; Star Points are a post-win reward, not an additional win condition.
- Reuse `TIM-001`: commands are selected in discrete turns, with live timed input nested within resolution, not a continuously running fight.

## Reproducible transitions

| Before | Action or event | Bounded resolution | Why it matters | Claim ID |
|---|---|---|---|---|
| Kooper joins after receiving his shell | Move toward the area exit | Four Fuzzies initiate the scripted battle | Entry is a specific finite encounter | `PM-001` |
| Mario and Kooper have not acted this player turn | Press Z before a command | Kooper can act before Mario; neither gains an extra action | Order is an explicit choice with a timing gate | `PM-002`, `PM-003` |
| Goombario is also recruited | Choose Change Party Member | Goombario replaces Kooper as the single active helper for that turn | Partner replacement changes available commands, not Mario's presence | `PM-003` |
| A rear grounded Fuzzy is selected | Choose jump rather than ordinary hammer | The jump can legally reach that target, while the normal hammer cannot | Target topology affects command choice | `PM-004` |
| Kooper and enough FP are available | Select Power Shell, then execute its cue | FP is spent and the shell can strike multiple enemies | Group coverage consumes a limited resource | `PM-004`, `PM-005`, `PM-006` |
| A Fuzzy begins its draining bite | Press A just before contact | Successful timing reduces Mario's incoming damage; an undefended successful bite may heal the Fuzzy | Defensive timing is distinct from offensive command timing | `PM-005`, `PM-006` |
| The fourth Fuzzy is defeated | Complete battle settlement | The encounter is won and Star Points are awarded under level-dependent rules | Local objective ends without implying whole-chapter completion | `PM-002`, `PM-007` |

## Strategic and experiential structure

The fixed group makes a multi-target FP expense tempting, but the packet does not assume a particular starting FP balance or that one Power Shell wins. Mario and Kooper normally each act; choosing who acts first can matter before a target is removed. Replacing Kooper with Goombario changes the available partner technique instead of recruiting an additional simultaneous attacker. The same discrete battle also contains brief real-time timing windows. A missed defence risks both Mario HP loss and enemy self-healing, so protecting health also prevents lost progress. This is a source-grounded reconstruction, not an optimal-route claim.

## Replay and variation

This encounter's four Fuzzies are authored, not a generated roster. Prior HP, FP, equipped badges and inventory may vary from the earlier route; player command order, target selection and timing success can vary within the same battle. No random distribution, exact damage sequence or deterministic save-state reproduction was established.

## Adjacent systems and history

*Clair Obscur: Expedition 33* also embeds timing inside a discrete battle, hence `ACT-222` and `SYS-358` transfer. It uses an initiative queue, AP and dodge/parry counters; the scoped *Paper Mario* fight instead has Mario-plus-one-partner actions, FP-paid techniques and A-button damage reduction. *Pokémon Red Version* can change its sole active Pokémon, but Mario remains an acting combatant when his helper changes. Treating those party switches as the same state transition would erase the distinction.

## Normalised genome

| Type | Active gene IDs | Key parameters |
|---|---|---|
| Action | `ACT-019`, `ACT-222`, `ACT-590`, `ACT-591`, `ACT-592` | actor, target, timing, partner, order |
| System Behaviour | `SYS-358`, `SYS-1178`, `SYS-1179`, `SYS-1180` | paired actions, four enemies, drain and reduction |
| Constraint | `CON-724`, `CON-725` | target position and FP gate |
| Information | `INF-142`, `INF-434` | combat HUD and input cues |
| Objective | `OBJ-029` | clear four Fuzzies before Mario falls |
| Time | `TIM-001` | discrete commands with nested timing |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `448` (`GAME-0001`–`GAME-0448`).
- Exact genome matches: none.
- Tied near matches: `GAME-0144` — Clair Obscur: Expedition 33 (`6 / 44 = 0.136364`).
- Supported combination subsets: none.
- Scan date: 2026-09-28.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0144` Clair Obscur: Expedition 33 | `ACT-019`, `ACT-222`, `SYS-358`, `INF-142`, `OBJ-029`, `TIM-001` | Both choose targets, clear enemies and embed attack timing in turns; Paper Mario's paired Mario/partner actions and A-button reduction do not have the other game's initiative queue, AP or parry counter. | Near, `6 / 44 = 0.136364` |

## Taxonomy impact

`TAXONOMY_CHANGE_186` admits nine source-supported boundaries without rewriting earlier signatures or verified combinations.

## Negative results

- No evidence justifies a guaranteed opening FP balance, a mandatory Volt Shroom, an exact perfect-input frame, a scripted Fuzzy target order or a guaranteed zero-damage guard.
- `ACT-258` and `CON-384` concern a single active Pokémon whose own health and fainting determine party replacement; Kooper is an assist alongside Mario, not the sole acting combatant.
- `SYS-356` requires a stat-ordered visible initiative queue and `ACT-223` entails dodge/parry/jump responses; neither models this packet's paired side phase and simple damage-reducing A press.

## Delta summary

## New facts

- [Observation | Corroborated | High] The fixed four-Fuzzy fight occurs just after Kooper joins, so the two-partner choice is actually available at this boundary (`PM-001`, `PM-003`).
- [Observation | Direct | High] Discrete turns embed both offensive and defensive timing prompts, while FP and target position separately gate available attacks (`PM-004`, `PM-005`).

## New genes

- [Observation | Corroborated | Medium] Nine boundaries distinguish Mario's active helper, pre-action order, damage-reducing defence, paired turn settlement, a successful enemy drain, target topology, FP legality and combat-state display.

## New combinations

- [Observation | Limited | Medium] None proposed; proper subsets are recomputed by index generation.

## Taxonomy changes

- [Observation | Corroborated | Medium] `TAXONOMY_CHANGE_186`; earlier signatures remain unchanged.

## New questions

- Can an original N64 save reproduce the four-Fuzzy entry with recorded HP, FP, equipped badges and frame-indexed Action Commands without inferring a universal enemy policy?

## Next recommended game

- [Hypothesis | Limited | Medium] `GAME-0450` *SSX Tricky*, after this unit and the Goal stop window.
- Optimisation criterion: preserve the maintainer-approved cross-platform sequence.
- Expected information gain: contrast scored downhill routes, aerial tricks and boost economy with this discrete partner battle.
- Backlog impact: none.

## Why this game

- [Hypothesis | Limited | Medium] Paper Mario introduces an original-N64 partner-action structure absent from the previous endless runner and reveals useful transfer of timing genes without collapsing two distinct RPG battle economies.
