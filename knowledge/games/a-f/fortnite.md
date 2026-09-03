---
game_id: GAME-0227
slug: fortnite
game_title: Fortnite
analysis_status: reviewed
reviewed: 2026-09-02
combination_ids:
  - COMB-0225
gene_ids:
  action:
    - ACT-008
    - ACT-161
    - ACT-164
    - ACT-183
    - ACT-186
    - ACT-198
    - ACT-199
    - ACT-397
  system:
    - SYS-208
    - SYS-215
    - SYS-316
    - SYS-317
    - SYS-321
    - SYS-730
    - SYS-731
    - SYS-732
  constraint:
    - CON-262
    - CON-283
    - CON-284
    - CON-285
    - CON-289
    - CON-566
  information:
    - INF-073
    - INF-075
    - INF-127
    - INF-128
    - INF-129
    - INF-278
  objective:
    - OBJ-074
  time:
    - TIM-003
---

# Game: Fortnite

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Parameters describe
gene instances but do not enter the signature.

## Analysis scope

- Version / ruleset: Epic Games' public Windows client `v42.00`, Fortnite
  Chapter 7 Season 4: Override, observed 2026-09-02; one ordinary unranked
  `Battle Royale Zero Build` Solo match on the current Override island.
- Platform and availability: the free Windows base product distributed through
  Epic Games Store and launched with an Epic Games account. Console, mobile and
  cloud-client differences are not combined with this packet.
- Mode: select Epic's `Battle Royale Zero Build` experience in Discover, set
  team size to Solo and leave Ranked disabled. The packet does not substitute
  `Battle Royale`, `Battle Royale Ranked`, `Zero Build Ranked`, `Fortnite OG
  Zero Build`, Reload or a creator island.
- Entry: begin at the Zero Build Solo lobby commitment, allow matchmaking and
  pre-match staging to settle, then retain control through the Battle Bus exit,
  skydive and glider landing. Lobby menu navigation is an entry gate rather
  than a separate persistent progression game.
- Primary decision loop: choose the Battle Bus exit and landing, collect a
  capacity-valid weapon/item loadout, move, sprint, slide or mantle between
  cover, aim, fire, switch and reload, read current Storm and survivor state,
  rotate into safety and decide whether the exposed value of an Override
  Console is worth contesting while every surviving Solo opponent makes the
  same live spatial-information decisions.
- Evaluation terminal: if the controlled participant is eliminated with no
  legal acquired extra-life state, allow the personal placement/result to
  settle and stop before Ready Up, account XP, quests or another queue. If the
  participant becomes the final survivor, allow the current `Victory Royale`
  screen to appear and stop at that positive result.
- Included: a field of the player and up to 99 opponents; variable Battle Bus
  insertion; skydive/glider landing; chests, defeated-player drops and other
  match-local loot; fixed carried slots, ammunition, weapon switching and
  reloading; direct third-person combat; Health, Shield and the Zero Build
  recharging Overshield; sprint, slide and mantle traversal; current map and
  phased Storm pressure; survivor count and final result; `v42.00` Override
  Consoles because they appear in every match and can change the live server or
  eligible squad rule; acquired `1-Up Token` or `Extra Life` return because it
  can postpone otherwise terminal Solo elimination.
- Excluded: building; Ranked and tournaments; Battle Royale with builds;
  Duos, Trios and Squads; Reload, OG, Blitz, Ballistic, Delulu and temporary
  playlists; LEGO Fortnite, Festival, Rocket Racing, Save the World, Creative,
  UEFN and third-party islands; exhaustive Sprite, Cheat Code, Loot Hack,
  vehicle, boss and weapon catalogues; Lobby Hack discovery outside the match;
  Battle Pass, quests, XP optimisation, cosmetics, purchases, social systems,
  account progression, later patches and the complete live-service history.
- Potential scoped modules: ordinary build-enabled Solo, team revival, Ranked,
  one current Sprite/extraction route, a specific vehicle or boss interaction,
  Reload and later seasons each need their own rules, evidence and terminal.
- Direct-play status: no authenticated match was played. Epic's current store,
  experience, Battle Royale and `v42.00` pages establish the live product,
  playlist, version and terminal rules; Epic documentation and the original
  Zero Build announcement establish loot, Storm and Overshield boundaries. The
  repository transitions are rules analysis, not claimed play. No video or
  audio was opened, played, heard or used; embedded players were ignored.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `FNT-001` | The current free Windows product is Epic Games' Chapter 7 Season 4 client line, and the latest official Battle Royale notes identify it as `v42.00` | Confirmed | Direct | High | P1, P2, P3, P4 |
| `FNT-002` | Epic exposes `Battle Royale Zero Build` as a separate unranked experience with a selectable Solo playlist and no building mechanics | Confirmed | Direct | High | P1, P2, P5 |
| `FNT-003` | One Battle Royale match drops the player among up to 99 opponents and awards Victory Royale to the last surviving participant while the Storm contracts playable space | Confirmed | Direct | High | P2, P6, P7 |
| `FNT-004` | Battle Bus exit, controlled descent and a current-island landing determine the opening position before the participant assembles world loot | Observation | Corroborated | High | P2, P6, P7 |
| `FNT-005` | Chests and eliminated participants expose weapons and items whose carried slots, ammunition, selection and reload state bound the match-local loadout | Observation | Corroborated | High | P1, P4, P6, P8 |
| `FNT-006` | Every Zero Build participant receives an Overshield above Shield and Health that takes damage first and recharges after depletion | Confirmed | Direct | High | P1, P5, P9 |
| `FNT-007` | `v42.00` puts Override Consoles in every match; a claim can apply a typed modifier to the whole server or to the first eligible squad while exposing claimant information | Confirmed | Direct | High | P3, P4 |
| `FNT-008` | The current loot/modifier pool can grant one acquired return from lethal Solo defeat through a `1-Up Token` or `Extra Life`, so final elimination must test that state first | Confirmed | Direct | High | P4 |
| `FNT-009` | When no return remains, elimination settles personal placement; reaching one survivor settles the current Victory Royale result screen | Observation | Corroborated | High | P2, P4, P6, P7 |
| `FNT-010` | Ranked, team modes, build-enabled Battle Royale, other Epic experiences and account reward systems are separable from this packet | Confirmed | Direct | High | P1, P2, P4, P5 |

## Basic data

- Release / origin: developed and published by Epic Games; original public
  release 2017; continuously updated, scoped to Chapter 7 Season 4 `Override`
  and official Battle Royale client line `v42.00` on 2026-09-02.
- Platform or physical form: networked Windows PC software through Epic Games
  Store; the scoped public match requires an Epic Games account and connection.
- Puzzle family: physics and object manipulation; tactical forecast and
  counterplay; real-time system pressure; inventory and fixture dependencies;
  world topology and perspective.
- Primary sources:
  - **[P1]** [official Epic Games Store product page](https://store.epicgames.com/p/fortnite?lang=en-US),
    observed 2026-09-02, for the free Windows product, current Override season,
    Zero Build Solo discovery path, no-building boundary, Overshield, traversal
    and separation of the wider Fortnite experiences.
  - **[P2]** [official current Battle Royale page](https://www.fortnite.com/@epic/battle-royale?lang=en-US),
    observed 2026-09-02, for Chapter 7 Season 4, 99 opponents, the changing
    island, Storm pressure, last-player victory and the Zero Build distinction.
  - **[P3]** [official Override season announcement](https://www.fortnite.com/news/fortnite-override-break-the-rules-change-the-game),
    dated 2026-08-20, for Chapter 7 Season 4 and every-match Override Consoles.
  - **[P4]** [Epic staff `v42.00` Battle Royale update notes](https://communities.epicgames.com/thread/v42-00-fortnite-override-battle-royale-update-notes/L5R3),
    observed 2026-09-02, for the exact client line, loot pool, Override scopes,
    `1-Up Token`, `Extra Life`, rule effects, claimant exposure and prompt
    Victory Royale display.
  - **[P5]** [official Zero Build announcement](https://www.fortnite.com/news/fortnite-zero-build-take-the-offensive-in-this-no-build-battle-royale),
    for separate Solo/Duos/Trios/Squads playlists, no building, recharging
    Overshield, sprint and mantle.
  - **[P6]** [Epic Battle Royale definition](https://dev.epicgames.com/documentation/fortnite/battle-royale),
    for Solo last-person-standing play and weapons/items from chests and
    defeated participants.
  - **[P7]** [Epic game-design documentation](https://dev.epicgames.com/documentation/fortnite/how-to-design-a-game-in-fortnite-creative),
    for the canonical last-player objective and continuously shrinking Storm
    circle in Fortnite Battle Royale.
  - **[P8]** [official Preferred Item Slots notes](https://www.fortnite.com/news/fortnite-battle-royale-v17-20-update-bughas-late-game-and-preferred-item-slots),
    for the five carried item slots, type preference, rarity replacement and
    direct loot-to-hotbar behaviour retained in current Battle Royale.
  - **[P9]** [official Overshield mechanics note](https://www.fortnite.com/news/fortnite-creative-v20-00-update),
    for damage order above Shield/Health and automatic recharge after depletion.
- Secondary sources: none. Current first-party material is sufficient for the
  accepted packet; exact unpublished matchmaking, item and damage values remain
  parameters rather than reconstructed claims.
- Claim IDs: `FNT-001`–`FNT-010`.

## Mechanical decomposition

### Action Genes

- Existing genes: `ACT-008`, directly navigate, sprint, slide and mantle;
  `ACT-161`, aim and attack; `ACT-164`, select a carried weapon or item;
  `ACT-183`, reload a magazine-fed weapon; `ACT-186`, drop eligible carried
  state; `ACT-198`, choose the Battle Bus exit and steer descent; `ACT-199`,
  transfer and equip compatible world loot.
- New gene: `ACT-397`, activate one reachable Override Console to claim its
  currently exposed match-rule modifier.
- Parameters: playlist, Battle Bus line, exit time, descent vector, weapon,
  item, inventory slot, ammunition, movement surface, console and override.
- Claim IDs: `FNT-002`–`FNT-008`.

### System Behaviour Genes

- Existing genes: `SYS-208`, resolve ranged attack through cover and layered
  protection; `SYS-215`, resolve direct live hostile combat; `SYS-316`, sample
  participants, insertion route and world loot; `SYS-317`, resolve freefall,
  glider and landing; `SYS-321`, reveal and contract phased safe areas while
  applying Storm damage.
- New `SYS-730`: resolve damage through recharging Overshield before ordinary
  Shield and Health.
- New `SYS-731`: when an eligible Override Console is claimed, apply its typed
  modifier to the declared whole-server or claimant-squad scope and expose the
  corresponding control/location consequence.
- New `SYS-732`: route Solo lethal defeat through one acquired `1-Up Token` or
  `Extra Life` return when legal; otherwise finalise placement, survivor count
  and the last participant's Victory Royale.
- Resolution order: commit playlist; initialise participants, Battle Bus and
  current loot; resolve exit and landing; accept live traversal, loot and combat
  while Storm phases advance; allow legal Override claims to alter later live
  state; apply Overshield, Shield and Health damage order; test acquired return
  before final removal; settle placement or Victory Royale.
- Parameters: participant fill, route, loot seed, ballistics, defence layers,
  recharge delay/rate, Storm phases, override type/scope, extra-life source,
  return state, survivors, placement and result.
- Claim IDs: `FNT-003`–`FNT-009`.

### Constraint Genes

- Existing genes: `CON-262`, typed weapon, item and ammunition capacity;
  `CON-283`, insertion is bounded by Battle Bus route and descent reach;
  `CON-284`, fixed carrying and equipment slots bound the loadout; `CON-285`,
  weapon operation requires compatible ammunition and action state; `CON-289`,
  successive Storm phases impose escalating live deadlines.
- New `CON-566`: lethal Solo return requires one acquired, applicable and
  unused match-local extra-life allowance; after consumption or without one,
  the same defeat is terminal.
- Scarce strategic resources: one participant life, any acquired extra life,
  safe-region travel time, concealment, Overshield recharge opportunity,
  Shield, Health, ammunition, magazine readiness and five carried item slots.
- Claim IDs: `FNT-003`–`FNT-009`.

### Information Genes

- Existing genes: `INF-073`, carried weapons, ammunition and active item are
  visible; `INF-075`, Health, Shield and Overshield are visible; `INF-127`, map
  and HUD expose insertion, present Storm safety and phase timing; `INF-128`,
  reachable loot and inventory expose identity, rarity, quantity and capacity;
  `INF-129`, survivor count, eliminations, personal placement and victory are
  visible.
- New `INF-278`: an Override claim exposes the active modifier and, according
  to its scope, the claimant's identity at the console or Solo location on the
  map, turning rule authority into contestable public information.
- Claim IDs: `FNT-003`–`FNT-009`.

### Objective Genes

- Existing `OBJ-074`: remain the last living Solo participant after every
  opponent has exhausted any legal return state.
- Success, evaluation and failure: Victory Royale satisfies the objective;
  final elimination settles placement as the negative evaluation terminal.
  Eliminations, loot, Overrides, survival time, quests and XP do not
  independently complete the unranked match.
- Claim IDs: `FNT-003`, `FNT-008`, `FNT-009`.

### Time Genes

- Existing `TIM-003`: insertion, movement, combat, reload, Overshield recharge,
  Storm phases, Override contest and terminal adjudication advance in live time
  without a tactical pause.
- Claim IDs: `FNT-003`–`FNT-009`.

## Reproducible transitions

| Before | Action | Deterministic or bounded resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Current `v42.00` Lobby exposes Epic's Zero Build experience | Select `Battle Royale Zero Build`, Solo, Ranked off, then Play | Matchmaking admits one ordinary Solo field and stages its current Battle Bus route | exact entry contract | `FNT-001`, `FNT-002` |
| The participant rides the current Battle Bus | Exit, steer the fall and deploy or retain the glider | Route, gravity, steering and collision produce one reachable island landing | spatial opening commitment | `FNT-004` |
| A chest or defeated participant exposes a weapon and ammunition | Collect, place and select legal items | Five-slot capacity accepts or replaces eligible items and exposes a usable loaded or reloadable weapon state | bounded match loadout | `FNT-005` |
| An opponent is visible across cover | Aim, fire, reposition, switch or reload | Attack and movement resolve against geometry, Overshield, Shield and Health while ammunition/readiness update | live firearm counterplay | `FNT-005`, `FNT-006` |
| Overshield has absorbed damage and its recharge condition is legal | Preserve cover for the required interval | Overshield charge restores toward capacity before later damage again reaches Shield or Health | recoverable no-build protection | `FNT-006` |
| The next safe region excludes the participant's position | Continue looting or rotate | Storm boundary contracts on schedule and applies outside damage until safety, recovery or defeat | forced spatial deadline | `FNT-003` |
| A current Override Console is reachable and exposes an available modifier | Activate the console | The claimed typed effect applies to the whole server or eligible claimant scope; claimant information becomes exposed as declared | shared rule-state intervention | `FNT-007` |
| Lethal Solo damage occurs while an acquired extra-life source remains legal | Allow the elimination transition | The allowance is consumed and participation returns under that source's declared inventory/location state | non-terminal acquired defeat | `FNT-008` |
| Lethal Solo damage occurs with no legal return remaining | Allow result settlement | The participant is removed, survivor count and personal placement settle, or the final survivor receives Victory Royale | bounded negative or positive terminal | `FNT-003`, `FNT-009` |

## Strategic and experiential structure

- Local decision: choose cover, aim, fire, reload, switch, retreat, exploit an
  Overshield recharge window or contest an Override Console under incomplete
  opponent state.
- Medium-term planning: convert landing position into a balanced five-slot
  loadout and reach each disclosed safe region before Storm pressure eliminates
  routes or forces a poor encounter.
- Long-term structure: preserve Health/Shield and any acquired extra life while
  the field and safe space contract; a claimed Override can change movement,
  damage, sustain or loot assumptions for everyone or the exposed claimant.
- Common heuristics: observe nearby descent paths, secure a usable weapon before
  optional loot, keep physical cover available for Overshield recovery, rotate
  before the Storm removes route choice and treat an Override broadcast as
  both power and an invitation to contest.
- Failure attribution: current bars, ammunition, carried slots, Storm state,
  survivor count, active modifier and placement distinguish resource, route,
  exposure and terminal errors; future loot and opponent choices remain hidden.
- Player-trust factors: present personal, Storm and result state is explicit;
  future loot, opponent positions and which participant will claim an Override
  remain uncertain, while a claimed rule change must become legible.
- Claim IDs: `FNT-004`–`FNT-009`.

## Replay and variation

- What changes between matches: participants, Battle Bus route, landing choice,
  loot, current item build, Storm centres, encounters, Override claimant/effect,
  extra-life acquisition and terminal placement.
- Randomness or procedural generation: one authored current island receives
  bounded match-local insertion, loot, Storm and encounter samples.
- Multiple viable strategies: dense or remote landing, early or edge rotation,
  short- or long-range loadout, Override contest or avoidance and aggressive or
  concealment-led endgame.
- Typical replay motive: improve landing efficiency, traversal, aim, inventory
  decisions and live adaptation to Storm, opponents and shared modifiers.
- Claim IDs: `FNT-003`–`FNT-009`.

## Adjacent systems and history

- Direct predecessors: battle-royale and third-person shooter lineages; this
  unit does not assign unreviewed predecessor mechanics.
- Variants: ordinary build-enabled Battle Royale adds construction; team modes
  add DBNO/revival relations; Ranked changes progression and competitive state;
  other Fortnite experiences replace the terminal and much of the ruleset.
- Similar games: PUBG shares Battle Bus-like stochastic aerial insertion,
  match-local firearm loot, capacity, a contracting damaging area and Solo
  last-survivor victory. Apex Legends shares layered protection and Ring
  pressure but makes defeat squad-recoverable. NARAKA shares one possible Solo
  return before final placement but centres spawn choice and melee counters.
- Important differences: Zero Build removes construction and adds a universal
  recharging defence layer. Current `v42.00` also permits a contested fixture
  to rewrite live match rules and an acquired item/modifier to delay Solo
  terminal elimination without importing team revival.
- Claim IDs: `FNT-001`–`FNT-010`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-161`, `ACT-164`, `ACT-183`, `ACT-186`, `ACT-198`, `ACT-199`, `ACT-397` | exact bindings, weapons and console are parameters |
| System Behaviour | `SYS-208`, `SYS-215`, `SYS-316`, `SYS-317`, `SYS-321`, `SYS-730`–`SYS-732` | numeric damage, Storm and override values are parameters |
| Constraint | `CON-262`, `CON-283`–`CON-285`, `CON-289`, `CON-566` | item slots, ammunition and return source are parameters |
| Information | `INF-073`, `INF-075`, `INF-127`–`INF-129`, `INF-278` | exact HUD styling is presentation |
| Objective | `OBJ-074` | participant cap and simultaneous defeat order are parameters |
| Time | `TIM-003` | all admitted play remains live |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `226` (`GAME-0001`–`GAME-0226`).
- Exact genome matches: none.
- Tied near matches: `GAME-0140` — PUBG: BATTLEGROUNDS (`24 / 49 = 0.489796`).
- Supported combination subsets: `COMB-0225`.
- Scan date: 2026-09-02.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0140` — PUBG: BATTLEGROUNDS | `ACT-008`, `ACT-161`, `ACT-164`, `ACT-183`, `ACT-186`, `ACT-198`, `ACT-199`, `SYS-208`, `SYS-215`, `SYS-316`, `SYS-317`, `SYS-321`, `CON-262`, `CON-283`, `CON-284`, `CON-285`, `CON-289`, `INF-073`, `INF-075`, `INF-127`, `INF-128`, `INF-129`, `OBJ-074`, `TIM-003` | Fortnite's admitted Zero Build packet replaces PUBG's vehicles, throwable arc, manual healing and fixed first-death settlement with a recharging first-hit layer plus current Override console claims whose public cost can alter the whole match and can supply a one-use Solo return. | Near, `24 / 49 = 0.489796` |

### Preserved research notes

- New genes: `ACT-397`, `SYS-730`–`SYS-732`, `CON-566`, `INF-278`.
- Reused genes: 24 existing navigation, firearm, aerial insertion, loot, Storm,
  protection-information, last-survivor objective and real-time boundaries; no
  earlier reviewed game signature changed.
- Classification result: `New gene` and `New combination of known and new genes`.
- Evidence and reasoning: the battle-royale corridor preserves substantial
  genuine reuse. Universal recharging Overshield, player-claimed shared rule
  intervention and an acquired Solo extra-life settlement remain operationally
  distinct from PUBG, Apex and NARAKA.

## Taxonomy impact

- Registry changes: add six bounded Active genes and `COMB-0225`; add Fortnite
  support to reusable battle-royale records without changing an earlier game
  signature.
- Taxonomy-change record: none.
- Candidate terms affected: Battle Bus, Victory Royale, Overshield, Override
  Console, Match Override, 1-Up Token, Extra Life and Zero Build remain official
  labels, rule parameters or presentation vocabulary rather than gene names.

## Negative results

- Zero Build was chosen exactly as recorded by selection. Build-enabled Battle
  Royale is not silently imported merely because construction is iconic to the
  wider product.
- `v42.00` is a dated live boundary. Earlier chapters, later hotfixes and the
  full weapon, boss, Sprite and collaboration history do not accumulate into
  one genome.
- Match Overrides remain because official notes say their consoles appear in
  every match. Optional Cheat Codes, Loot Hack configuration and Sprite
  collection are not causally required for the entry-to-result packet; their
  item identities and effects are parameters unless a later scoped unit proves
  a distinct decision boundary.
- `SYS-325` and `CON-290` are not reused: current `v42.00` can provide an
  acquired return, so the first lethal event is not unconditionally permanent.
- `SYS-659` and `CON-532` are not reused: NARAKA grants one mode-owned Rebirth
  with a phase cutoff, while Fortnite requires an acquired current item or
  modifier and has source-specific return state.
- No video or audio evidence entered any claim. The official text pages were
  sufficient, so no audiovisual trace or timestamps exist for this unit.

## Delta summary

## Нові факти

- [Confirmed | Direct | High] `FNT-001`–`FNT-010`: public Windows `v42.00`
  unranked Zero Build Solo joins aerial deployment, found firearms, recharging
  Overshield, Storm contraction, shared Overrides and conditional extra life to
  one final placement or Victory Royale result.

## Нові гени

- [Observation | Corroborated | High] Added `ACT-397`, `SYS-730`–`SYS-732`,
  `CON-566` and `INF-278` for match-rule console authority, recharging
  Overshield, acquired Solo return and public Override state.

## Нові комбінації

- [Observation | Corroborated | High] `COMB-0225` — Zero Build Solo survival
  through recharging defence, contracting Storm and contestable rule changes.

## Зміни таксономії

- [Observation | Direct | High] Змін таксономії немає; попередні signatures не
  змінено.

## Нові питання

- Which named two-role segment in A Way Out has a reproducible local entry,
  causally necessary asymmetric actions and a retained story checkpoint?

## Наступна рекомендована гра

- [Hypothesis | Limited | High] `GAME-0228` — A Way Out.
- Optimisation criterion: continue the authorised horizon while moving from
  competitive live-service Solo play to bounded two-role story cooperation.
- Expected information gain: compare role-asymmetric local coordination with
  Split Fiction and It Takes Two without unioning the full campaign.
- Backlog impact: advances the recorded order without displacing No Man's Sky
  or any later authorised subject.

## Чому саме вона

- [Hypothesis | Limited | High] It is the next fixed Unit 3 subject in
  `SEARCH_DEMAND_GAME_SELECTION_011`; no reserve or substitution condition has
  triggered.
