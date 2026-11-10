---
game_id: GAME-0489
slug: golden-sun
game_title: Golden Sun
analysis_status: reviewed
reviewed: 2026-10-04
combination_ids: []
gene_ids:
  action:
    - ACT-019
    - ACT-131
    - ACT-661
  system:
    - SYS-299
    - SYS-362
    - SYS-854
    - SYS-1303
    - SYS-1304
    - SYS-1305
    - SYS-1306
    - SYS-1307
  constraint:
    - CON-269
    - CON-323
    - CON-756
  information:
    - INF-119
    - INF-466
  objective:
    - OBJ-029
  time:
    - TIM-033
---

# Game: Golden Sun — original GBA first Vault battle

Use the [canonical vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
Character names, Flint, Venus, Psynergy names, PP costs, element and target-row
length are parameters, not separate genes.

## Analysis scope

- Version / ruleset: original English Game Boy Advance Golden Sun, using the
  English part of Nintendo's European instruction booklet, copyright
  2001/2002. The original European English product, not The Lost Age, Dark
  Dawn, a Wii U/Switch wrapper, modification or randomiser, is the declared
  target. Exact cartridge revision and North American/European binary parity
  were not inspected. Contemporary original-GBA accounts support the bounded
  scenario, not exact cross-region timing or numerical equivalence.
- Structured analysis target: existing `PLAT-GAME-BOY-ADVANCE`, original
  cartridge booklet rules, in `knowledge/platforms/games.json`.
- Primary decision loop: inspect party HP/PP and Djinn availability; choose
  one command for each eligible member before any round action resolves;
  commit ordinary attacks, PP-paid Psynergy, an owned Djinni release or
  state change, a shared available summon, a held item or defence; let the
  complete allied/hostile batch resolve according to agility; reassess
  target survival, health, class/abilities and spirit states before the next
  round, until the three required enemies fall or the party is downed.
- Entry and exit: one fresh-story first Vault inn-attic battle, after Ivan
  joins Isaac and Garet and the tied carpenter has been released. Prepare
  all three living participants with full current HP/PP, Flint owned and Set
  on Isaac, no other Djinn, ordinary equipment and each character's acquired
  healing consumables. Record actual levels, gear and item counts at entry;
  they are explicit save-state parameters, not invented fixed defaults. A
  reproducible route leaves Vale, receives Flint, enters Vault, recruits
  Ivan, surrounds the suspected thieves, enters via the roof and moves the
  crate before releasing the carpenter. Those field actions construct the
  entry; they are not an additional traversed expedition in this signature.
  Stop after the battle's rewards and first restored field control, before
  further town service or travel. Total party Down ends this attempt; a
  refused escape or menu cancellation does not constitute success.
- Included: exactly Isaac, Garet and Ivan against one Bandit and two Thieves;
  all six battle commands Attack, Psynergy, Djinn, Summon, Item and Defend;
  round planning and cancellation/Status inspection; agility ordering;
  ordinary Attack becoming Defend if its target has already fallen or fled;
  physical/elemental damage, healing and available status effects, including
  the documented Smoke Bomb/Delusion risk; finite PP and items; centred
  multi-target effects; own-spirit versus party-shared summon availability;
  Set/Standby/Recovery transitions, passive build withdrawal/return and
  battle-local elemental power after summoning; defeat, experience/level
  thresholds, coins and the Bandit's Sword reward.
- Excluded: the opening unwinnable Saturos/Menardi encounter; field puzzles,
  Mind Read/Move route controls and ordinary random battles used to reach
  the entry; optional grinding, prior-save stock or imported extra Djinn;
  equipment or Djinn-owner changes during this fight; later revival items
  not held at entry; post-battle shops, inn/Sanctum visits, inventory
  expansion, other bosses, field recovery, world-map travel, Arena/link
  battles, save/password transfer, The Lost Age's reserve-party Switch,
  Dark Dawn and emulated convenience controls. The booklet's generic Flee
  rule is not blindly assigned to this boss: a secondary battle reference
  reports refusal in boss battles. Exact original refusal/message/turn
  precedence remains uninspected and is not admitted as a working escape
  mechanic. No exact enemy HP, damage, initiative tie, status chance,
  falloff or queued competing-summon cancellation formula is asserted.
- Potential scoped modules: the complete Vale–Vault field expedition; a
  multi-Djinn later boss; ordinary encounter escape and recovery; original
  linked Arena. They need separate evidence/admission, not an exhaustive
  product-wide union here. The selection's expedition question was provisional;
  the complete first combat packet is the accepted causal boundary.
- Direct-play status: not conducted. No cartridge, ROM, emulator, native
  save, game video/audio or controller trace was inspected. The original
  publisher booklet's relevant English sections were read, with visual
  checks of PDF leaves 7, 10, 14 and 18–23. Written original-game accounts
  are their authors' reports, not our play. PDF conversion in 2014 does not
  make its original printed rules a 2014 game revision.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `GS-001` | Every eligible party member receives a command before an agility-ordered round resolves | Confirmed | Direct | High | P1 pp. 34–35 |
| `GS-002` | An ordinary Attack whose target already fell or fled becomes Defend | Confirmed | Direct | High | P1 p. 36 |
| `GS-003` | Set Djinn contribute to attributes, elemental power/resistance and class-dependent Psynergy; withdrawal may remove abilities | Confirmed | Direct | High | P1 pp. 12–14, 18–19, 28–29, 37 |
| `GS-004` | Releasing an owned Set Djinni resolves its effect and changes it to Standby; setting Standby uses a scheduled command | Confirmed | Direct | High | P1 pp. 39–40 |
| `GS-005` | Any party member can summon from shared elemental Standby counts; spent Djinn enter Recovery and the invoker gains matching battle-local elemental power | Confirmed | Direct | High | P1 pp. 41–43 |
| `GS-006` | Used Djinn reattach after the documented recovery turn; they are not destroyed | Confirmed | Direct | High | P1 pp. 16–17, 43 |
| `GS-007` | Central targeting changes ranged effect strength and edge coverage; summons affect the enemy row with a chosen strongest target | Confirmed | Direct | High | P1 pp. 36–37, 43 |
| `GS-008` | Defend exchanges the actor's action for reduced incoming damage; item and Psynergy choices have availability/target/resource gates | Confirmed | Direct | High | P1 pp. 26–27, 36–44 |
| `GS-009` | HP depletion causes Down and disables fighting; all-party Down ends the battle attempt | Confirmed | Direct | High | P1 pp. 24–27, 34 |
| `GS-010` | Spirit states, build changes, party resources, ability costs/ranges and summon counts are inspectable | Confirmed | Direct | High | P1 pp. 16–27, 39–43 |
| `GS-011` | First Vault boss pits Isaac/Garet/Ivan with available Flint against Bandit and two Thieves; winning returns the stolen goods and awards Bandit's Sword | Observation | Corroborated | Medium | R1 Parts V–VI, R2 Vault |
| `GS-012` | Boss accounts report enemy attacks, herbs and Smoke Bomb; numerical enemy HP conflicts remain unresolved | Observation | Conflicting | Medium | R1 boss table, R2 Vault table, P1 p. 27 |
| `GS-013` | Boss escape is reported refused; exact native handling is not verified by the generic booklet escape description | Observation | Limited | Low | S1, P1 pp. 34–35 |
| `GS-014` | Battle experience can cross character-level thresholds; bounded reward settlement includes currency and a named item | Observation | Corroborated | Medium | P1 pp. 24–25, R1–R2 |
| `GS-015` | The full six-command first-boss packet preserves build withdrawal, shared summon, guarding, resources and both terminals without later systems | Observation | Corroborated | Medium | P1, R1–R2, S1 |

## Basic data

- Release / origin: Nintendo/Camelot; original GBA product with 2001/2002
  regional booklet copyright. No exact release-day or cartridge hash claim.
- Platform or physical form: original English European GBA cartridge rules;
  the existing handheld identity does not establish parity with later wrappers.
- Puzzle family: tactical forecast and counterplay; ordered dependency
  sequencing. All seventeen controlled family definitions were tested.
- Primary sources, accessed 2026-10-03:
  - **P1:** [Nintendo's original Golden Sun instruction booklet](https://www.nintendo.com/eu/media/downloads/games_8/emanuals/game_boy_advance_8/Manual_GameBoyAdvance_GoldenSun_EN_DE_FR_ES_IT.pdf),
    English pp. 12–29 and 34–44, for spirit configuration, attributes, status,
    commands, range and complete battle settlement. Read the original scans,
    not OCR alone; pagination is printed, distinct from PDF leaves.
  - **R1:** [TimeAssassin's original-GBA first-hand guide](https://gamefaqs.gamespot.com/gba/468548-golden-sun/faqs/14723),
    version 2.2, dated 2001-12-09, Parts V–VI. A contemporary player account
    supplies entry, named enemies, Flint/Venus availability and rewards;
    it is not engine inspection and describes approximate HP.
  - **R2:** [NaYa's independently authored original-GBA guide](https://gamefaqs.gamespot.com/gba/468548-golden-sun/faqs/15144),
    Vault section. Its numerical boss table differs from R1, so only their
    compatible encounter, move/item and settlement observations are retained.
- Secondary source: **S1:** [Golden Sun battle reference](https://goldensunwiki.net/wiki/Battle),
  explicitly separates original boss escape from later reserve-party Switch.
  This lower-authority report bounds an uncertainty; it does not establish
  an original-engine formula or a new escape gene.
- Claim IDs: `GS-001`–`GS-015`.

## Mechanical decomposition

### Action Genes

- Existing: `ACT-019` selects an actor's attack, Psynergy, release, summon or
  self-targeted defensive ability; `ACT-131` spends a carried immediate item.
- New: `ACT-661` requests an owned Djinni's ready/standby state, not a
  combat-time ownership transfer or an action-free equipment toggle.
- Parameters: actor, command, eligible centre/target, PP, held item and spirit.
- Claim IDs: `GS-001`, `GS-004`, `GS-008`.

### System Behaviour Genes

- Existing: `SYS-854` typed affinity, damage/status and combatant defeat;
  `SYS-362` bounded reward settlement; `SYS-299` experience thresholds.
- New: `SYS-1303` derives the current attached-spirit build; `SYS-1304`
  cycles ownership, shared Standby invocation and Recovery reattachment;
  `SYS-1305` schedules the batch and obsolete ordinary-attack fallback;
  `SYS-1306` resolves centre/row coverage and falloff; `SYS-1307` resolves
  committed defence's reduction. These preserve distinct causal effects.
- Resolution: inspect/commit the complete party batch; execute eligible
  actions with the source's agility ordering, updating health, targets,
  PP/items and Djinn/build state; settle documented recovery; return to
  planning or award the encounter result. Exact tie and competing resource
  precedence are deliberately unspecified, not reverse engineered.
- Parameters: agility, damage/affinity, row/span, power/resistance, healing,
  Delusion, command state, reward and recovery interval.
- Claim IDs: `GS-001`–`GS-009`, `GS-012`, `GS-014`.

### Constraint Genes

- Existing: `CON-269` legal ability/resource/readiness; `CON-323` currently
  available living active party. No character becomes a reserve ally here.
- New: `CON-756` one scheduled opportunity per eligible member per round.
- Scarce resources: personal HP/PP, actual carried items, one shared available
  Earth Djinni and action opportunities. Flint's Set benefits are unavailable
  while it is Standby/Recovery; one available Flint cannot pay multiple summons.
- Reject `CON-175`: this scope is one encounter, not a complete multi-node
  attrition route. Reject movement-plus-action or shared AP limits.
- Claim IDs: `GS-001`, `GS-003`–`GS-006`, `GS-008`–`GS-009`.

### Information Genes

- Existing: `INF-119` inspectable party health, PP, levels/build/status.
- New: `INF-466` distinct spirit states and before/after configuration,
  plus shared elemental summon counts. These do not preview enemy commands
  or guarantee a future turn order/hit.
- Claim IDs: `GS-010`.

### Objective Genes

- Existing: `OBJ-029`, all three required hostiles incapacitated before the
  party falls. Rewards close the packet; the carpenter and roof are entry
  preparation, not additional exit objectives.
- Failure: all active participants Down. Reviving/retrying after that terminal
  is outside this single attempt. Cancellation and a refused Flee do not win.
- Candidate genes: none; enemy identities and reward quantities are parameters.
- Claim IDs: `GS-009`, `GS-011`, `GS-014`–`GS-015`.

### Time Genes

- New: `TIM-033` paused complete-party planning before interleaved automatic
  execution. No ATB/individual CT, deadline or real-time input window.
- `TIM-001` would require one input before full resolution; `TIM-005`
  describes flexible executing player phases before committed hostile phases.
  Neither is silently broadened to describe this batch.
- Claim IDs: `GS-001`.

## Reproducible transitions

These are source-specified conditional transitions, not measured native traces.

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Three living eligible members, commands not complete | Inspect/enter one command | No combat round yet resolves | Planning differs from execution | `GS-001` |
| Ordinary Attack is queued against a thief | Earlier actor defeats that thief | Pending Attack becomes Defend, not a free retarget | Target-overcommitment cost | `GS-002` |
| Flint is Set on Isaac | Release Flint at Isaac's action | Declared release effect, then Standby and build recalculation | Passive versus paid availability | `GS-003`–`GS-004` |
| Flint is Standby, no other Djinn | Garet selects eligible Venus summon | Shared Earth count pays; Flint recovers on Isaac and Garet gains battle-local Earth power | Invoker is not necessarily owner | `GS-005` |
| Flint is in Recovery, encounter continues | Complete the documented recovery turn | Flint returns to Set and its passive contribution returns | Reusable state cycle, not consumable deletion | `GS-006` |
| Three targets in a row, three-target Psynergy | Choose an end target instead of centre | Edge clips coverage; strongest effect centres on selected target | Target choice changes coverage and strength | `GS-007` |
| A living actor can act | Commit Defend rather than Attack | Action is spent in a damage-reducing defensive state | No live guard timing | `GS-008` |
| Available PP is below a Psynergy cost | Attempt that Psynergy | Resource gate prevents eligible use | Cost is not just descriptive UI | `GS-008` |
| One ally reaches zero HP | Continue with survivors | Down ally cannot fight; all-party Down terminates the attempt | Individual loss versus party terminal | `GS-009` |
| Bandit and both Thieves are defeated | Accept settlement | Eligible EXP/coins/item reward, then restored field control | Complete bounded encounter | `GS-011`, `GS-014` |

## Strategic and experiential structure

- Local decision: avoid assigning several ordinary attacks to an enemy likely
  to fall early; choose a central area target or protect a vulnerable member.
- Medium-term planning: trade Flint's passive stats for a release and a
  party-shared Venus summon, then survive until reattachment; preserve PP
  and finite healing. The strongest elemental gain attaches to the invoker.
- Long-term structure: the scoped fight has repeated resource/state cycles,
  not a campaign calendar or a required permanent-loss countdown.
- Common heuristics: contemporary guides recommend group Psynergy and a
  Flint/Venus sequence. They are possible tactics, not optimality proofs.
- Failure attribution: committed targets, depleted PP, unavailable Djinn and
  lost action slots explain failure without a hidden genre rating.
- Player trust: own-state and build previews are visible, future enemy
  commands are not. Numerical source conflicts do not become exact rules.
- Claim IDs: `GS-001`–`GS-015`.

## Replay and variation

- Entry levels, equipment, held items, command choices, enemy action order,
  damage/status outcomes and remaining resources may vary. The declared party,
  single Flint and fixed three-enemy encounter do not.
- Exact original RNG, probabilities, agility ties and damage formulas remain
  uninspected. No new random-generation gene is admitted from that absence.
- Compare concentrated attacks, central group effects, guard/heal and the
  reusable Djinni cycle without asserting a mandatory successful tactic.
- Claim IDs: `GS-001`–`GS-015`.

## Adjacent systems and history

- The original booklet identifies the GBA product; the sequel's reserve-party
  Switch and later wrappers are explicitly not inherited.
- Field puzzles, exploration recovery and multi-Djinn configurations can be
  separate scoped modules. They do not inflate this first-battle signature.
- Detailed neighbouring-game claims follow the selected scan below only.
- Claim IDs: `GS-013`–`GS-015`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-019`, `ACT-131`, `ACT-661` | actor, ability, own spirit, item |
| System Behaviour | `SYS-299`, `SYS-362`, `SYS-854`, `SYS-1303`, `SYS-1304`, `SYS-1305`, `SYS-1306`, `SYS-1307` | elemental configuration, row, agility, thresholds |
| Constraint | `CON-269`, `CON-323`, `CON-756` | PP, readiness, party and action slots |
| Information | `INF-119`, `INF-466` | own resources, states, previews and counts |
| Objective | `OBJ-029` | fixed Bandit/Thieves set |
| Time | `TIM-033` | paused batch and automatic round |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `488` (`GAME-0001`–`GAME-0488`).
- Exact genome matches: none.
- Tied near matches: `GAME-0338` — Final Fantasy VII (`7 / 29 = 0.241379`).
- Supported combination subsets: none.
- Scan date: 2026-10-04.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0338` Final Fantasy VII | `ACT-019`, `ACT-131`, `SYS-299`, `SYS-362`, `SYS-854`, `CON-269`, `INF-119` | Both expose personal resources, typed commands, items and rewards. FFVII uses live individual ATB, equipment-derived Materia and carried Limit charge inside a timed multi-node reactor mission. Golden Sun waits for the complete party batch, interleaves by agility and cycles an owned spirit through shared invocation; it has no evacuation deadline or copied ATB/Limit. | Near; `7 / 29 = 0.241379`. |

### Preserved research notes

- New genes: nine reviewed additions in `TAXONOMY_CHANGE_226`.
- Classification result: `New gene`.
- Evidence and reasoning: the full eighteen-use packet retains fitting existing
  command, resource, party, reward and objective boundaries; state-sharing and
  execution semantics require explicit bounded additions, not thematic genes.

## Taxonomy impact

- Registry changes: `ACT-661`, `SYS-1303`–`SYS-1307`, `CON-756`, `INF-466`, `TIM-033`.
- Taxonomy-change record: [TAXONOMY_CHANGE_226](../../../research/taxonomy-changes/TAXONOMY_CHANGE_226.md).
- Candidate terms: Flint, Venus, Psynergy, PP and character names remain
  parameters. No earlier signature or verified combination is changed.

## Negative results

- No exact native cartridge, binary parity, numerical HP/damage/initiative
  formula or competing-summon cancellation is verified. R1/R2 HP conflicts
  remain unresolved; the generic manual Flee claim does not prove boss escape.
- No original direct play, video, audio, save or controller trace is claimed.
- No existing combination is manufactured from this complete signature.

## Delta summary

## New facts

- [Observation | Corroborated | Medium] The complete first Vault fight exposes
  a reusable own-spirit/passive-build/shared-invocation tradeoff; `GS-015`.

## New genes

- [Observation | Direct | Medium] Nine bounded command, configuration, state,
  scheduling, area, defence, allocation, disclosure and timing additions.

## New combinations

- [Observation | Corroborated | Medium] No new verified combination; full
  corpus subset scan is retained rather than forcing a named interaction.

## Taxonomy changes

- [Observation | Direct | Medium] `TAXONOMY_CHANGE_226` preserves prior IDs and
  nine fitting reuses while admitting the new original-battle boundaries.

## New questions

- What does a native original cartridge do with equal agility, a lost queued
  summon payment, exact boss escape refusal and simultaneous terminal effects?
- Which later independently scoped carriers transfer the shared spirit cycle?

## Next recommended game

- [Hypothesis | Limited | Medium] Comix Zone, original Mega Drive/Genesis,
  `GAME-0490`, after this complete unit and its local commit/stop window.
- Optimisation criterion: follow the approved cross-platform horizon, not an
  implicit new research selection or an unauthorised push/publication.
- Expected information gain: panel movement, bounded tools and health-paid
  traversal differ from paused party-command planning.
- Backlog impact: stop after `GAME-0495` as recorded in selection 038.

## Why this game

- [Hypothesis | Limited | Medium] Golden Sun tests shared spirit availability
  and passive build withdrawal against the existing command-combat taxonomy.
