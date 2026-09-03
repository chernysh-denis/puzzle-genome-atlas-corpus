---
game_id: GAME-0240
slug: kingdom-come-deliverance-ii
game_title: "Kingdom Come: Deliverance II"
analysis_status: reviewed
reviewed: 2026-09-03
combination_ids:
  - COMB-0238
gene_ids:
  action:
    - ACT-008
    - ACT-048
    - ACT-091
    - ACT-131
    - ACT-165
    - ACT-199
    - ACT-232
    - ACT-245
    - ACT-341
    - ACT-410
  system:
    - SYS-348
    - SYS-369
    - SYS-379
    - SYS-756
  constraint:
    - CON-282
    - CON-297
    - CON-336
    - CON-581
  information:
    - INF-073
    - INF-075
    - INF-125
    - INF-148
    - INF-288
  objective:
    - OBJ-148
  time:
    - TIM-003
---

# Game: Kingdom Come: Deliverance II

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Parameters describe
gene instances but do not enter the signature.

## Analysis scope

- Version / ruleset: **Kingdom Come: Deliverance II Standard Edition**, current
  unmodified English Windows Steam base product app `1771300`, public Patch
  `1.5.6`, observed public Build ID `23914554` built/published 2026-06-25,
  checked 2026-09-03; fresh `Normal` New Game, tutorials enabled, mouse and
  keyboard, and only the early base-game main quest `Fortuna`.
- Primary decision loop: read Henry's condition, inventory, journal objective,
  markers, dialogue responses and recipe page; stop opening bleeding, eat and
  wash; accept the herb task; bury the body; gather required herbs; resolve the
  bandits peacefully; execute each manual alchemy step with the correct
  ingredient treatment/order/heat timing; deliver the brew, sleep, and settle
  the next-morning dialogue.
- Entry and exit: `Easy Riders` and the opening cutscene are setup only. Entry
  is first control after Henry wakes in Bozhena's hut with `Fortuna` active and
  injury, bleeding and hunger exposed. Positive exit is first controllable
  state after `Fortuna` completes and `Laboratores` becomes active, immediately
  written to a manual save and verified by load. Zero health ends the attempt;
  loading a retained state bounds recovery but is not completion.
- Reproducible route: use four supplied bandages; eat from the pot and wash;
  ask how to recognise the herbs and accept; take the spade, carry the body to
  marked soft ground, dig and bury; collect marked chamomile and sage; return,
  equip the work axe only as contingency, then choose `Let's talk peacefully`,
  `You don't look like von Bergow's men`, and `You're looking in the wrong
  place (Lie)`; tell Bozhena the truth and volunteer to brew. At the bench use
  wine as base, add two chamomile, heat for one sandglass turn, grind and add
  one sage, then pour into a phial. Give the Strong Chamomile brew, sleep until
  morning, complete breakfast and Hans dialogue, then save/load the successor.
- Included: first-person locomotion; inventory/equipment; bandage, food and
  wash responses; body carry/burial; marked wild-herb gathering; offered
  dialogue and local reputation/quest consequences; one written recipe and its
  manual apparatus, ordered ingredients, grinding, heat interval and graded
  output; requested-item hand-in; sleep; journal update; save/load and death.
- Excluded: fighting the bandits, taking the body's sword, alternate dialogue
  or burial outcomes, repeated alchemy, free exploration, crime, commerce,
  equipment maintenance, skill grinding, perks, later quests/regions and the
  complete story; `Hardcore`, mods, console commands and exploits; Royal
  Edition, Expansion Pass, Gallant Huntsman's Kit, Shields of Seasons Passing,
  The Lion's Crest, Brushes with Death, Legacy of the Forge, Mysteria
  Ecclesiae, post-launch quest lines and every other add-on.
- Potential scoped modules: an alternate `Fortuna` branch, a later named base
  quest, one combat or smithing packet, `Hardcore`, or one named expansion each
  requires its own build, entry and terminal. None is combined here.
- Direct-play status: not conducted. Current official product, edition, patch,
  platform and manual-save material plus three independent static written
  quest traces establish the route. This is evidence-based reconstruction, not
  a captured playthrough. No video or audio was opened, played, heard, analysed
  or used.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `KCD2-001` | App `1771300` is the sold Windows base game; Royal, Expansion Pass and named add-ons are separable | Confirmed | Direct | High | P1–P3 |
| `KCD2-002` | Current public patch is 1.5.6; observed Windows public build is 23914554 | Confirmed | Corroborated | High | P3, P4, S1 |
| `KCD2-003` | `Fortuna` lies between `Easy Riders` and `Laboratores`; first hut control exposes injury, bleeding and hunger | Observation | Corroborated | High | S2–S5 |
| `KCD2-004` | Bandaging, eating and washing update the opening condition before the herb task | Observation | Corroborated | High | S2–S4 |
| `KCD2-005` | Optional burial requires spade, body carry, marked ground and digging and settles a favourable consequence | Observation | Corroborated | High | S2–S4 |
| `KCD2-006` | The fixed peaceful response sequence avoids combat and updates reputation/quest state | Observation | Corroborated | High | S2–S4 |
| `KCD2-007` | The taught brew requires wine, two chamomile, one heat interval, ground sage and phial transfer in order | Observation | Corroborated | High | S2, S3 |
| `KCD2-008` | Manual alchemy retains process state and evaluates it into the Strong Chamomile output | Observation | Corroborated | High | P2, S2, S3 |
| `KCD2-009` | Hand-in, sleep and morning/Hans dialogue complete `Fortuna` and activate `Laboratores` | Observation | Corroborated | High | S2–S5 |
| `KCD2-010` | Manual save points and load are supported; official notes confirm manual-save overwrite and save/load handling | Confirmed | Direct | High | P5, P6 |
| `KCD2-011` | Hotfix 1.1.2 changed a `Fortuna` crime-report edge but not the bounded route | Confirmed | Direct | High | P4, P7 |
| `KCD2-012` | The fixed trace joins body triage, conversation, a world-state deed and timed recipe execution before one retained successor | Observation | Corroborated | High | P1–P7, S1–S5, V1 |

## Basic data

- Release / origin: Warhorse Studios / Deep Silver, 2025-02-04.
- Form: single-player first-person action RPG; only the declared current
  Windows Steam Standard/base-game packet is admitted.
- Puzzle family: ordered dependency sequencing; state transformation; resource
  management; knowledge-based progression; authored social choice.
- Primary and official sources:
  - **[P1]** [Steam product](https://store.steampowered.com/app/1771300/Kingdom_Come_Deliverance_II/),
    for app identity, developer, publisher, release, Windows and single-player.
  - **[P2]** [Deep Silver game page](https://www.deepsilver.com/games/kingdom-come-deliverance-ii),
    for action-RPG structure, consequential actions, skills and alchemy.
  - **[P3]** [PLAION editions guide](https://support.plaion.com/en/games/kingdomcome2/article/261-Kingdom-Come-Deliverance-II-Editions/),
    for Standard/base versus Royal, Expansion Pass and add-on boundaries.
  - **[P4]** [Patch 1.5.6](https://support.plaion.com/en/games/kingdomcome2/article/407-Kingdom-Come-Deliverance-II-Patch-1-5-6/),
    for current patch authority and separately added Jester quest line.
  - **[P5]** [official PlayStation product/accessibility page](https://www.playstation.com/en-us/games/kingdom-come-deliverance-ii/),
    for the same product's manual save points and exact-state return; this is
    rules corroboration, not the scoped platform.
  - **[P6]** [Hotfix 1.3.1](https://support.plaion.com/en/games/kingdomcome2/article/346-Kingdom-Come-Deliverance-II-Hotfix-1-3-1/),
    for manual-save overwrite and save/load handling.
  - **[P7]** [Hotfix 1.1.2](https://support.plaion.com/en/games/kingdomcome2/article/311-Kingdom-Come-Deliverance-II-Hotfix-1-1-2/),
    for the bounded `Fortuna` crime-report correction.
- Secondary textual sources:
  - **[S1]** [SteamDB depots](https://steamdb.info/app/1771300/depots/),
    observed 2026-09-03, for Build ID `23914554` and timestamp.
  - **[S2]** [PowerPyx written route](https://www.powerpyx.com/kingdom-come-deliverance-2-fortuna-walkthrough/),
    for entry, bandages, burial, herbs, peaceful response, apparatus and exit.
  - **[S3]** [Gamer Guides written route](https://www.gamerguides.com/kingdom-come-deliverance-ii/guide/main-quests/trosky/fortuna-quest-walkthrough),
    for independent condition, burial, dialogue, recipe and exit corroboration.
  - **[S4]** [Gamepressure written route](https://www.gamepressure.com/kingdom-come-deliverance-2/fortuna/z411783),
    for independent route order; its translated herb-name conflict is rejected
    in favour of the two concordant detailed sources.
  - **[S5]** [wiki.gg quest record](https://kingdomcomedeliverance.wiki.gg/wiki/Fortuna),
    for predecessor, successor and quest identity.
- Reproducible control: **[V1]** repository transition trace under fixed
  product, patch, difficulty, entry, response sequence, recipe, successor and
  save/load terminal; no direct-play or audiovisual claim.
- Claim IDs: `KCD2-001`–`KCD2-012`.

## Mechanical decomposition

### Action Genes

- Existing `ACT-008`: navigate the bounded route; `ACT-048`: carry/place the
  body; `ACT-091`: give the requested brew; `ACT-131`: consume bandages into
  immediate bleed-stop effects; `ACT-165`: eat to restore nourishment;
  `ACT-199`: collect/equip tools; `ACT-232`: commit quest responses; `ACT-245`:
  gather one reachable herb yield; `ACT-341`: use pot, tub, ground and bed.
- New `ACT-410`: directly operate one compatible manual-recipe component —
  base, ingredient, heat control, timer, grinder or output vessel — thereby
  changing the retained in-progress batch.
- Exact nouns and numbers are parameters. Claims: `KCD2-004`–`KCD2-009`.

### System Behaviour Genes

- Existing `SYS-348`: bleeding drains survivable health into death;
  `SYS-369`: load replaces current state with a retained save; `SYS-379`:
  objectives, responses, deeds, relationships and successor advance through
  retained quest flags.
- New `SYS-756`: retain base, ingredients, preparations, heat intervals and
  vessel state, then evaluate the ordered process into its declared graded
  product or lesser/failed result.
- Resolution order: expose state; accept action; validate authored/recipe
  prerequisites; update body/world/relationship/batch; evaluate brew; advance
  hand-in, sleep and dialogue; settle quest; save/load successor.
- Claims: `KCD2-003`–`KCD2-012`.

### Constraint Genes

- Existing `CON-282`: authored quest gates; `CON-297`: recipe knowledge,
  ingredients and station context; `CON-336`: retained decisions gate later
  responses and quest states.
- New `CON-581`: target recipe grade requires the declared base, ingredient
  identities/quantities, preparations, addition order, heat intervals and
  compatible output vessel. Concrete values remain parameters.
- Scarce resources: bandages, health, nourishment, herb yields, tools, response
  state, ingredients, heat interval and retained save.
- Claims: `KCD2-003`–`KCD2-012`.

### Information Genes

- Existing `INF-073`: inventory/equipment; `INF-075`: condition and equipment
  wear; `INF-125`: objectives, markers and successor; `INF-148`: offered
  contextual responses without all future consequences.
- New `INF-288`: the manual-recipe surface exposes instructions, staged inputs,
  current batch/apparatus state and visible timing instrument.
- Audio is not evidence. Exact labels, art, values and positions are parameters.
- Claims: `KCD2-003`–`KCD2-012`.

### Objective Genes

- New `OBJ-148`: restore required immediate condition, complete one bounded
  recovery quest's field/dialogue/production sequence, and retain its named
  successor after a persistence check. Campaign completion is excluded.
- Claims: `KCD2-003`–`KCD2-012`.

### Time Genes

- Existing `TIM-003`: movement, condition loss, world response, sleep and heat
  timing belong to a real-time world; pausing menus do not create turns.
- Claims: `KCD2-003`–`KCD2-012`.

## Reproducible transitions

| Before | Action | Resolution | Establishes | Claim |
|---|---|---|---|---|
| Fresh Normal route after setup | Reach first hut control and save | `Fortuna` active; injured, bleeding, hungry state | entry/retry anchor | `KCD2-001`–`004` |
| Bleeding and bandage stock | Use four route bandages | Stock falls and bleeding stops before lethal loss | bounded treatment | `KCD2-004` |
| Pot/tub reachable | Eat, then wash | Nourishment/cleanliness improve | condition response | `KCD2-004` |
| Herb task offered | Ask recognition, then accept | Herb objective/marker becomes active | dialogue-to-objective | `KCD2-003`, `005` |
| Spade/body/ground eligible | Take spade, carry, dig and bury | Body/grave and favourable deed state persist | world/social state | `KCD2-005` |
| Marked herb sources retain yield | Gather chamomile and sage | Sources yield finite carried inputs | world-to-recipe input | `KCD2-007` |
| Bandit confrontation | Commit fixed peaceful responses | Lie branch avoids combat and updates quest/reputation | social branch | `KCD2-006` |
| Bozhena asks for account/brewer | Tell truth and volunteer | Recipe/workstation stage becomes current | response gate | `KCD2-006`, `007` |
| Empty batch and recipe | Add wine/chamomile; heat one sandglass turn | Inputs and heat interval persist | manual process | `KCD2-007`, `008` |
| Sage whole; batch ready | Grind/add sage; pour into phial | Valid history yields Strong Chamomile | graded output | `KCD2-007`, `008` |
| Requested brew held | Give it | Item leaves inventory; recovery/quest flags advance | hand-in | `KCD2-008`, `009` |
| Sleep objective/bed available | Sleep, breakfast, talk to Hans | `Fortuna` completes; `Laboratores` activates | named successor | `KCD2-009` |
| First successor control | Manual save, menu, load | Settled journal/inventory state returns | positive terminal | `KCD2-009`, `010` |
| Health reaches zero earlier | Load retained save | Saved state replaces failed attempt | negative recovery | `KCD2-004`, `010` |

## Strategic and experiential structure

- Local decisions prioritise treatment, optional favourable work, peaceful
  dialogue and the next recipe operation from current batch/timer evidence.
- Medium-term planning preserves condition and inputs, earns the burial
  consequence and avoids invalidating the strong brew through preparation,
  order or timing errors.
- Long-term structure moves from bodily vulnerability through a retained deed
  and social branch to manual material transformation that unlocks a named
  successor.
- Failure attribution comes from condition indicators, objectives, response
  feedback, reputation notices, visible batch contents, sandglass and output.
- The recipe/tutorial discloses each required operation; visible apparatus
  state and a loadable named successor replace walkthrough memory and an
  arbitrary sandbox stop.

## Replay and variation

- Variable: treatment timing, burial, gathering order, responses, reputation,
  recipe mistakes, save placement and duration.
- Fixed: product/build, Normal, first hut control, mandatory recovery/brew order
  and `Laboratores` successor.
- The product supports combat and other responses, but this trace fixes the
  peaceful branch to isolate one stable packet.

## Adjacent systems and history

- The first Kingdom Come: Deliverance is a separate product/quest/build; no
  rules are imported.
- The Witcher 3 shares movement, gathering, inventory, authored dialogue,
  retained quests and a taught recipe. Skyrim shares first-person condition,
  equipment and a retained successor but excludes alchemy from its reviewed
  Helgen packet. Fallout 4 shares fresh-start gates, dialogue, inventory and
  save/load but has no manual recipe procedure.
- Distinguishing feature: separately addressable apparatus operations preserve
  a process history whose preparation, order and heat interval determine a
  graded item required for quest closure.

## Normalised genome

| Type | Active gene IDs | Parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-048`, `ACT-091`, `ACT-131`, `ACT-165`, `ACT-199`, `ACT-232`, `ACT-245`, `ACT-341`, `ACT-410` | people, lines, tools, herbs, apparatus |
| System | `SYS-348`, `SYS-369`, `SYS-379`, `SYS-756` | bleed, flags, reputation, output |
| Constraint | `CON-282`, `CON-297`, `CON-336`, `CON-581` | amounts, order, interval, predicates |
| Information | `INF-073`, `INF-075`, `INF-125`, `INF-148`, `INF-288` | HUD, journal, recipe art |
| Objective | `OBJ-148` | quest/successor names |
| Time | `TIM-003` | update/timer/load duration |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `239` (`GAME-0001`–`GAME-0239`).
- Exact genome matches: none.
- Tied near matches: `GAME-0205` — The Witcher 3: Wild Hunt (`11 / 43 = 0.255814`).
- Supported combination subsets: `COMB-0238`.
- Scan date: 2026-09-03.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0205` — The Witcher 3: Wild Hunt | `ACT-008`, `ACT-131`, `ACT-199`, `ACT-232`, `ACT-245`, `SYS-379`, `CON-282`, `INF-073`, `INF-125`, `INF-148`, `TIM-003` | The Witcher 3 packet adds investigation, combat and a one-request taught craft. This packet instead adds rigid body carry, food/fixture/hand-in actions, save replacement and a player-enacted apparatus process with preparation, ordered heat timing, graded output and a recovery-quest terminal. | Near, `0.255814` |

### Preserved research notes

- New genes: `ACT-410`, `SYS-756`, `CON-581`, `INF-288`, `OBJ-148`.
- Reused genes: `ACT-008`, `ACT-048`, `ACT-091`, `ACT-131`, `ACT-165`,
  `ACT-199`, `ACT-232`, `ACT-245`, `ACT-341`, `SYS-348`, `SYS-369`,
  `SYS-379`, `CON-282`, `CON-297`, `CON-336`, `INF-073`, `INF-075`,
  `INF-125`, `INF-148`, `TIM-003`.
- Result: `New gene` and `New combination of known and new genes`. Concrete
  story, ingredient and numeric values remain parameters.

## Taxonomy impact

- Five new Active portable genes; no prior definition, lifecycle or reviewed
  signature changes. No taxonomy-change record.

## Negative results

- `ACT-123` alone is rejected: it commits a whole recipe, while this packet
  requires individual apparatus operations. `INF-059`/`INF-074` are neither
  this apparatus state nor timer. `SYS-387` is rejected because no visible d20
  or Inspiration rule is evidenced. `ACT-211` is rejected because no body-
  region wound is selected. Combat, broad skill learning, exact reputation,
  DLC and whole-campaign systems remain excluded.

## Combination subset scan

- All 237 pre-unit combinations were tested; none is a proper subset of this
  25-gene signature. `COMB-0238` reserves only the condition/dialogue/manual-recipe/
  retained-successor core. Scan date: 2026-09-03.
