---
game_id: GAME-0189
slug: black-myth-wukong
game_title: "Black Myth: Wukong"
analysis_status: reviewed
reviewed: 2026-08-29
combination_ids:
  - COMB-0187
gene_ids:
  action:
    - ACT-008
    - ACT-161
    - ACT-190
    - ACT-191
    - ACT-200
    - ACT-223
    - ACT-224
    - ACT-229
    - ACT-342
  system:
    - SYS-215
    - SYS-251
    - SYS-364
    - SYS-607
    - SYS-608
    - SYS-609
    - SYS-610
    - SYS-611
  constraint:
    - CON-269
    - CON-270
    - CON-282
    - CON-286
    - CON-324
    - CON-354
    - CON-506
    - CON-507
  information:
    - INF-119
    - INF-125
  objective:
    - OBJ-080
  time:
    - TIM-003
---

# Game: Black Myth: Wukong

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Parameters describe
gene instances but do not enter the signature.

## Analysis scope

- Version / ruleset: current unmodded Windows Steam Standard Edition, official
  version `1.0.21.23831`, Steam Build `21393610`, checked 2026-08-29; one fresh
  Journey from first retained control in Chapter 1 through the saved Chapter 2
  entry after Black Bear Guai. The mandatory opening sequence is a prerequisite
  but its separately controlled Sun Wukong state lies before the analysis boundary.
- Primary decision loop: traverse the Forest of Wolves and Black Wind Mountain;
  read hostile wind-ups; spend stamina on staff attacks, dodge or sprint; turn
  light hits, charged heavies and Perfect Dodges into Focus decisions; use the
  Gourd, Immobilize and later Cloud Step around their resources/readiness;
  deliberately defeat Guangzhi to retain Red Tides; rest and configure Sparks
  at Keeper's Shrines; defeat the required route bosses and settle Chapter 1.
- Entry and exit: begins at the first ordinary Destined One control in Chapter
  1 on a fresh save after the opening transition. It succeeds only after Black
  Bear Guai is defeated, the chapter-ending sequence settles and the save
  reaches the first controllable Chapter 2 state. Death before that boundary is
  a recoverable Shrine return rather than a terminal failure.
- Included: direct traversal; staff light, heavy and varied attacks in the
  available Smash-stance route; stamina, charge and Focus; dodge and Perfect
  Dodge; Immobilize and Cloud Step when acquired on the route; the finite
  healing Gourd; Red Tides acquired from Guangzhi; experience, levels, Sparks,
  eligible Foundation/Stamina/Martial Arts/Survival/Smash allocations and free
  Shrine reclamation; Keeper's Shrine activation, rest, recovery, enemy reset
  and return after death; Bullguard, Guangzhi, Lingxuzi, Guangmou, Whiteclad
  Noble, Black Wind King and Black Bear Guai; retained chapter transition.
- Excluded: Deluxe Edition Bronzecloud Staff, Folk Opera set, Wind Chimes and
  soundtrack; later chapters, New Cycle/NG+, Challenge and Gauntlet modes,
  future DLC and live-service history; the optional three-bell/Elder Jinchi
  branch and Fireproof Mantle, Wandering Wight, Baw-Li-Guhh-Lang, Red Loong and
  other optional encounters; exhaustive Spirits, transformations, vessels,
  curios, armour, weapons, crafting, medicines, maps, secrets, collectables and
  Journal completion; mods, trainers, glitches and speedrun skips.
- Direct-play status: no authenticated fresh route was played. Current official
  developer, storefront and platform material was reconciled with maintained
  route/mechanics references into a repository-side deterministic trace;
  secondary claims remain labelled as such.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `BMW-001` | Official version 1.0.21.23831 is the current released PC rules boundary and corresponds to Steam Build 21393610 | Confirmed | Corroborated | High | P1, S1 |
| `BMW-002` | The current Standard Edition is a single-player staff-combat game whose spells, abilities, weapons and equipment can be combined rather than one fixed attack string | Confirmed | Direct | High | P2 |
| `BMW-003` | Dodge and sprint consume stamina; a correctly timed Perfect Dodge avoids damage and generates Focus, while staff pressure builds or charges Focus for stronger heavy commitment | Observation | Corroborated | High | P3, S2 |
| `BMW-004` | Immobilize and Cloud Step enter the Chapter 1 route as active spells bounded by Mana, cooldown, target and combat state | Observation | Corroborated | High | P2, S2, S3 |
| `BMW-005` | Defeating Guangzhi grants the Chapter 1 Red Tides transformation, temporarily replacing the Destined One's combat body, health/readiness and moveset before returning to the base form | Observation | Corroborated | High | P3, S2 |
| `BMW-006` | Resting at a Keeper's Shrine restores the admitted combat resources and Gourd charges while ordinary enemies return; the Shrine remains the checkpoint and travel/service hub | Observation | Corroborated | High | P3, S4 |
| `BMW-007` | Ordinary death returns the character to the latest eligible Shrine without dropping Will, experience, Sparks, items, spells or retained boss/chapter progress | Observation | Corroborated | High | S5, S6 |
| `BMW-008` | Experience thresholds award levels and Sparks; eligible tree nodes consume Sparks, and Reignite the Sparks at a Shrine reclaims allocations without a currency fee | Observation | Corroborated | High | P3, S7 |
| `BMW-009` | The bounded Chapter 1 route can reproducibly clear Bullguard, Guangzhi, Lingxuzi, Guangmou, Whiteclad Noble, Black Wind King and Black Bear Guai before the saved Chapter 2 transition | Observation | Corroborated | High | S2, S3 |
| `BMW-010` | Health, stamina, Mana, Focus, Gourd uses, spell readiness, transformation state, boss condition and current route state are exposed sufficiently for attributable decisions | Observation | Corroborated | High | P3, S2, S4 |
| `BMW-011` | Deluxe equipment is separately claimable at a Keeper's Shrine and is therefore not silently admitted to the Standard Edition route | Confirmed | Direct | High | P2 |
| `BMW-012` | The repository trace reproduces resource combat, Perfect Dodge, spell and transformation gates, Shrine reset, retained-death recovery, reversible Sparks and the Chapter 1 terminal | Observation | Direct | High | V1 |

## Basic data

- Release / origin: Game Science; released 2024-08-20 and maintained through
  official version `1.0.21.23831` at review time.
- Platform or physical form: one single-player unmodded Windows Steam Standard
  Edition save; keyboard/controller mapping is a parameter rather than a gene.
- Puzzle family: real-time system pressure; ordered dependency sequencing;
  capability-gated exploration; resource and risk management; boss-led action
  progression.
- Primary sources:
  - **[P1]** [official developer Steam announcement for version 1.0.21.23831](https://store.steampowered.com/news/app/2358720/view/499467145192673443?l=english),
    for the current released version boundary and maintenance status.
  - **[P2]** [official Steam product page](https://store.steampowered.com/app/2358720/Black_Myth_Wukong/?l=english),
    for developer/publisher identity, single-player form, staff, spells,
    transformations, equipment and separately claimable Deluxe contents.
  - **[P3]** [official Xbox Wire beginner tips](https://news.xbox.com/en-us/2025/08/18/five-tips-to-help-you-get-started-with-black-myth-wukong-on-xbox-series-xs/?ver=3.7.1),
    for Chapter 1 duration/context, dodge/Focus decisions, Shrines, Sparks,
    Guangzhi/Red Tides and ordinary enemy return. The article describes the
    console release, so only cross-platform base-system claims are reused.
- Secondary and reproducible sources:
  - **[S1]** [SteamDB Build 21393610 record](https://steamdb.info/patchnotes/21393610/),
    for the Steam build associated with official version 1.0.21.23831.
  - **[S2]** [Game8 Chapter 1 boss route](https://game8.co/games/Black-Myth-Wukong/archives/468847),
    for the named route, Guangzhi transformation and boss ordering.
  - **[S3]** [Gamer Guides Chapter 1 boss route](https://www.gamerguides.com/black-myth-wukong/guide/walkthrough/chapter-1/all-bosses-in-chapter-1),
    for Front Hills entry, Bullguard/Immobilize and the Black Wind King–Black
    Bear Guai terminal corridor.
  - **[S4]** [maintained Keeper's Shrine mechanics reference](https://wukong.cskl.pl/gameplay/keepers-shrine/),
    for checkpoint, rest, refill, enemy reset and travel/service behaviour.
  - **[S5]** [Game8 death reference](https://game8.co/games/Black-Myth-Wukong/archives/468474),
    for Shrine return and the absence of item, Will, XP, Spark or spell loss.
  - **[S6]** [GamesRadar shipped-game death/healing analysis](https://www.gamesradar.com/games/action-rpg/black-myth-wukong-is-not-a-soulslike-but-its-take-on-healing-flasks-is-so-cool-that-i-want-other-games-to-copy-it/),
    for no corpse-currency recovery and Shrine-refilled Gourd use.
  - **[S7]** [Game8 Reignite the Sparks reference](https://game8.co/games/Black-Myth-Wukong/archives/468609),
    for cost-free whole, branch or node reclamation at a Shrine.
  - **[V1]** repository-side transition trace derived from `P1`–`P3` and
    `S1`–`S7`; executable rules reasoning, not direct play.
- Claim IDs: `BMW-001`–`BMW-012`.

## Mechanical decomposition

### Action Genes

- Existing genes: `ACT-008`, directly navigate the Destined One; `ACT-161`, aim
  and commit one staff attack; `ACT-190`, activate one learned spell;
  `ACT-191`, spend one Spark on an eligible build node; `ACT-200`, commit one
  Gourd sip; `ACT-223`, time a dodge against a telegraphed attack; `ACT-224`,
  rest at an activated Keeper's Shrine; `ACT-229`, activate the ready Red Tides
  temporary combat form.
- New gene: `ACT-342`, reclaim one or more allocated Sparks at a Keeper's Shrine
  before assigning the resulting available points again.
- Parameters: movement, target, staff chain, charged/heavy input, stance, spell,
  dodge instant, Gourd use, Shrine, Spark node, reclaimed set and transformation.
- Claim IDs: `BMW-003`–`BMW-010`, `BMW-012`.

### System Behaviour Genes

- Existing genes: `SYS-215`, resolve directly commanded real-time hostile
  combat; `SYS-251`, advance the authored opening route; `SYS-364`, restore
  checkpoint resources and return ordinary enemies after rest.
- New genes: `SYS-607`, convert light pressure, charging and Perfect Dodges into
  Focus points spent by staff heavy or varied attacks; `SYS-608`, replace the
  base combat body with the temporary Red Tides health/readiness/moveset and
  return to the base body when it ends; `SYS-609`, convert experience thresholds
  into levels/Sparks and apply or freely reclaim their tree modifiers;
  `SYS-610`, convert ordinary death into Shrine return while retaining Will,
  experience, Sparks, items and authored progress; `SYS-611`, retain the
  Chapter 1 boss gates and settle Black Bear Guai into first Chapter 2 control.
- Resolution order: an input first validates target, stamina, recovery and
  readiness; staff/dodge resolution can change Focus; damage and spell effects
  update hostile state; transformation temporarily redirects those rules to its
  own body; XP may cross a level/Spark threshold; rest restores and resets its
  declared sets; lethal damage returns to the Shrine without a recovery mark;
  boss flags open the next route segment and the final flag settles the chapter.
- Claim IDs: `BMW-003`–`BMW-012`.

### Constraint Genes

- Existing genes: `CON-269`, a spell or transformation requires its legal
  target, range, resource and readiness; `CON-270`, Spark nodes obey current
  point, branch, prerequisite and rank gates; `CON-282`, authored boss/route
  gates require their prior state; `CON-286`, a Gourd sip requires a remaining
  use and an uninterrupted legal state; `CON-324`, a Perfect Dodge requires its
  matching live attack window; `CON-354`, staff, dodge and sprint commitments
  obey stamina and animation-recovery state.
- New genes: `CON-506`, a Focus-enhanced staff commitment requires the current
  point/charge state and compatible heavy or varied input; `CON-507`, Red Tides
  requires the acquired transformation, recovered readiness and compatible
  current combat state.
- Scarce strategic resources: health, Gourd charges, stamina, Focus, Mana,
  spell cooldowns, transformation readiness/duration, safe animation windows,
  available Sparks and distance to the active Shrine.
- Claim IDs: `BMW-003`–`BMW-010`.

### Information Genes

- Existing genes: `INF-119`, expose health, stamina, Mana, Focus, experience,
  Sparks, Gourd, spell/transformation readiness and current build; `INF-125`,
  expose the explored authored route, Shrine and boss/chapter gate state.
- New genes: none.
- Claim IDs: `BMW-003`–`BMW-010`, `BMW-012`.

### Objective Genes

- Existing gene: `OBJ-080`, defeat the mandatory route guardian and cross the
  newly opened authored progression threshold; here the terminal guardian is
  Black Bear Guai and the threshold is first retained Chapter 2 control.
- Success, evaluation and failure: boss KO alone is enabling progress; success
  is the saved chapter transition. Ordinary death is a recoverable setback with
  no dropped-currency branch; abandoning or deleting the save lies outside the
  game-rule terminal.
- Claim IDs: `BMW-007`, `BMW-009`, `BMW-012`.

### Time Genes

- Existing gene: `TIM-003`, traversal, hostile attacks, stamina recovery,
  spell cooldowns, transformation and boss combat evolve continuously except
  through explicit menus, rest transitions and loading boundaries.
- New genes: none.
- Claim IDs: `BMW-003`–`BMW-012`.

## Reproducible transitions

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Fresh Chapter 1 control after the opening | Reach and activate the first Keeper's Shrine | The Shrine becomes a retained rest/service and death-return point | explicit post-prologue entry and checkpoint state | `BMW-002`, `BMW-006` |
| Stamina remains and an enemy begins a readable strike | Dodge inside the matching late window | Damage is avoided and the Perfect Dodge adds Focus | defence can fund later offence but only through timing | `BMW-003` |
| The same input lands outside the Perfect Dodge window | Dodge before the hit still reaches the new position | Stamina is spent without the Perfect Dodge Focus reward | ordinary evasion and rewarded precision are distinct | `BMW-003` |
| At least one Focus point is held and the heavy input is compatible | Commit the staff heavy/varied attack | The point is spent and the authored stronger staff effect resolves if it connects | Focus is a built-and-spent combat resource | `BMW-003` |
| Immobilize is acquired, Mana remains and its cooldown is ready | Cast it on a legal nearby hostile | Mana/readiness change and the target receives the spell's temporary control state | spells form a gated layer beside staff combat | `BMW-004` |
| Guangzhi remains alive | Defeat him and acquire Red Tides | The transformation flag persists in the save | a deliberately admitted branch changes the later combat repertoire | `BMW-005`, `BMW-009` |
| Red Tides is acquired and ready | Activate the transformation during combat | Direct control moves to its separate temporary body and moveset, then returns to the Destined One when the form ends | transformation is not a cosmetic buff or second persistent character | `BMW-005` |
| Health/Gourd/Mana are depleted and ordinary enemies were defeated | Rest at an activated Shrine | Admitted resources and Gourd uses recover while ordinary enemies return | recovery deliberately rewrites local world pressure | `BMW-006` |
| The character carries Will, XP, Sparks and items | Take lethal damage and accept return | Control resumes at the latest eligible Shrine with those retained and no corpse mark; ordinary hostiles reset | Wukong death differs from recoverable-currency Soulslike death | `BMW-007` |
| One Spark is available and an eligible node's prerequisites hold | Allocate the Spark | The node modifier enters the persistent build and the available point count falls | level rewards become authored build choice | `BMW-008` |
| Several Sparks are allocated | Choose Reignite the Sparks at a Shrine and reclaim a node or branch | The selected points return without a Will fee and may be legally reassigned | build commitment is reversible at the checkpoint | `BMW-008` |
| Required Chapter 1 route remains incomplete | Defeat the next admitted boss and persist its result | The corresponding gate/award settles and the route to the later boss remains available after death | boss flags form retained ordered progress | `BMW-004`, `BMW-009` |
| Black Bear Guai remains undefeated | Defeat the boss and survive the chapter-ending sequence | Chapter 1 settles and the save reaches first controllable Chapter 2 state | boss victory plus region crossing, not KO alone, is terminal | `BMW-009`, `BMW-012` |

## Strategic and experiential structure

- Local decision: read a wind-up, preserve stamina for exit, continue a light
  sequence, charge/spend Focus, attempt Perfect Dodge, drink, cast, transform or
  disengage toward a Shrine route.
- Medium-term planning: choose Spark nodes, decide whether a safe Shrine reset
  is worth enemy return, acquire Red Tides, pace Mana/Gourd use through the next
  boss and reclaim a poor build before the following gate.
- Long-term structure: retain Shrine, spell, transformation, boss and chapter
  flags until Black Bear Guai settles the Forest of Wolves/Black Wind Mountain
  route and first Chapter 2 control is saved.
- Common heuristics: do not empty stamina on offence; use ordinary dodge before
  demanding Perfect Dodge precision; build Focus safely, then spend it in a
  confirmed opening; use Immobilize to create one; transform as a replaceable
  combat body; rest after unlocking a useful checkpoint; respec for the next
  boss rather than treating early Sparks as irreversible.
- Failure attribution: an empty stamina or Mana pool, illegal cooldown/target,
  mistimed dodge, interrupted Gourd sip, missed heavy, expired transformation,
  weak Spark allocation or skipped boss gate can be distinguished from hidden
  drop randomness.
- Player-trust factors: readable animation cues, visible gauges/readiness,
  explicit Shrine functions, persistent unlocks, retained inventory after death
  and an unambiguous chapter transition.
- Claim IDs: `BMW-003`–`BMW-012`.

## Replay and variation

- What changes between sessions: staff timing, route detours, Spark allocation,
  Gourd/Mana expenditure, spell/transformation timing, optional deaths and boss
  learning. The admitted boss set and chapter terminal remain fixed.
- Randomness or procedural generation: the route and boss order are authored;
  incidental enemy drops may vary but are not required for the control trace.
- Multiple viable strategies: different legal Spark allocations and combat
  timings can clear the same fixed Chapter 1 gates.
- Typical replay motive: execute cleaner boss reads, reduce Shrine resets,
  compare builds or continue to later chapters; later progression is excluded.

## Adjacent systems and history

- Direct predecessors: Journey to the West adaptations and earlier action RPGs
  inform theme or genre but are not merged into this current ruleset.
- Variants: Deluxe equipment, later patches, console builds, Challenge/Gauntlet,
  NG+ and each later chapter remain distinct scope modules.
- Similar games: Elden Ring, Hollow Knight: Silksong, Monster Hunter Wilds,
  Clair Obscur: Expedition 33 and Tunic share selected checkpoint, boss,
  resource, timing or route structure.
- Important differences: Elden Ring leaves one recoverable rune mark and uses
  load/attribute requirements; Wukong retains Will on death and centres Focus,
  spells and temporary full-body transformations. Silksong creates a Cocoon and
  uses acquired movement gates; Wukong's bounded chapter instead sequences
  authored bosses and a region transition. Monster Hunter uses quest timer,
  faint allowance, equipment maintenance and a Palico; this solo chapter has no
  hunt settlement or autonomous companion.
- Claim IDs: `BMW-003`–`BMW-012`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-161`, `ACT-190`, `ACT-191`, `ACT-200`, `ACT-223`, `ACT-224`, `ACT-229`, `ACT-342` | navigate, staff attack, spell, Spark, heal, dodge, rest, transform and reclaim parameters |
| System Behaviour | `SYS-215`, `SYS-251`, `SYS-364`, `SYS-607`–`SYS-611` | live combat, opening, rest reset, Focus, form, build, death and chapter state |
| Constraint | `CON-269`, `CON-270`, `CON-282`, `CON-286`, `CON-324`, `CON-354`, `CON-506`, `CON-507` | ability, tree, route, heal, dodge, stamina, Focus and transformation legality |
| Information | `INF-119`, `INF-125` | personal resources/build and authored route state |
| Objective | `OBJ-080` | defeat Black Bear Guai and cross the Chapter 2 threshold |
| Time | `TIM-003` | continuous traversal, combat and readiness |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `188` (`GAME-0001`–`GAME-0188`).
- Exact genome matches: none.
- Tied near matches: `GAME-0150` — Hollow Knight: Silksong (`11 / 40 = 0.275000`).
- Supported combination subsets: `COMB-0187`.
- Scan date: 2026-08-29.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0150` — Hollow Knight: Silksong | `ACT-008`, `ACT-161`, `ACT-190`, `ACT-224`, `SYS-215`, `SYS-364`, `CON-269`, `INF-119`, `INF-125`, `OBJ-080`, `TIM-003` | both directly traverse and fight in real time, spend active resources, rest to refill while ordinary enemies return and cross a boss-guarded act boundary, but Silksong converts attacks into Silk, changes moves and Tool topology through Crests and creates one recoverable Rosary Cocoon; Wukong instead couples stamina and Perfect Dodge to Focus, freely reclaims Sparks, temporarily replaces the combat body and retains Will without a death mark | Near, `0.275000` |

### Preserved research notes

- New genes: `ACT-342`, `SYS-607`–`SYS-611`, `CON-506` and `CON-507`.
- Classification result: `New gene` and new verified interaction combination.
- Evidence and reasoning: direct movement/attack/spell/heal/rest, live combat,
  authored opening, resource reset, skill-tree gates, timed defence, stamina,
  personal/route information and boss-region objective reuse safely. Focus
  conversion, temporary replacement form, free Spark reclamation, lossless
  Shrine death and chapter settlement are absent as a joined lower-ID boundary.

## Combination status

- `COMB-0187` is a verified strict twenty-seven-gene subset of the twenty-nine-
  gene genome, coupling staff/stamina combat, Perfect Dodge and Focus, active
  spells, Red Tides, reversible Sparks, Shrine reset, lossless death return,
  ordered boss flags and the Chapter 2 terminal.
- Every earlier verified combination is tested deterministically after
  registration; none is a proper subset of this genome.

## Taxonomy impact

- Registry changes: eight new Active genes, evidence links on reused genes,
  `COMB-0187` and existing family memberships.
- Taxonomy-change record: none; no prior lifecycle or reviewed-game signature
  changes. Reused action/checkpoint/timing/stamina definitions receive
  parameterised Wukong evidence without removing their prior boundaries.
- Candidate terms affected: Perfect-Dodge Focus, temporary replacement form,
  cost-free Spark reclamation, no-loss Shrine death and chapter-boss settlement.

## Negative results

- `SYS-399` and `CON-352` are not reused: Wukong creates no recoverable
  currency mark or second-death loss; Will and build state remain with the save.
- `SYS-409` is not reused: the scope does not require an exposed retained
  guard/stance depletion threshold or critical follow-up.
- `SYS-404` and `CON-356` are not reused: there is no quest faint allowance or
  timer; ordinary death is a repeatable checkpoint return.
- `ACT-250`, `SYS-414` and `CON-360` are not reused: optional Spirits are not
  required by this route and do not define the admitted Red Tides transformation.
- Deluxe claims, optional secret bosses and later-chapter mechanics are not
  admitted merely because the current executable contains them.

## Delta summary

## Нові факти

- [Confirmed | Corroborated | High] Current PC version 1.0.21.23831 supports a
  bounded fresh Standard Edition Chapter 1 route through Black Bear Guai and
  first retained Chapter 2 control (`BMW-001`–`BMW-012`).

## Нові гени

- [Observation | Corroborated | High] Added eight genes for Shrine Spark
  reclamation, Focus conversion, Red Tides replacement form, reversible build
  progression, no-loss death return, chapter settlement and their legality.

## Нові комбінації

- [Observation | Corroborated | High] `COMB-0187` isolates the joined
  stamina/Focus/spell/form/Shrine/build/death/boss route to one chapter terminal.

## Зміни таксономії

- [Observation | Corroborated | High] No lifecycle migration and no reviewed
  signature change; only evidence-preserving reuse generalisations were made.

## Нові питання

- Which later action game preserves checkpoint-retained currency and free build
  reclamation while replacing a temporary full-body form with a persistent
  multi-weapon stance system?

## Наступна рекомендована гра

- [Confirmed | Direct | High] `SEARCH_DEMAND_BATCH_006_AUDIT`.
- Optimisation criterion: independently verify the complete authorised
  nine-game demand-led batch before any publication decision.
- Expected information gain: detect cross-unit scope, source, localisation,
  artwork, index, generated-output or comparison-parity drift at the 189-game boundary.
- Backlog impact: final audit unit of the active Goal.

## Чому саме вона

- [Confirmed | Direct | High] It is Unit 10 in the authorised ordered horizon
  and the only remaining unit before the Goal can close.

## Localisation status

- Ukrainian game, new-gene and combination entries are reviewed in this unit.
- The canonical trademark title remains `Black Myth: Wukong`; Ukrainian prose
  is presentation-only.

## Open questions

- Recheck the official PC version and whether current updates alter Chapter 1
  spell, transformation, Shrine, death or boss transitions on review-on-touch;
  keep later chapters and optional branches outside this signature unless
  separately authorised.
