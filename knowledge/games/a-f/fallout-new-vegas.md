---
game_id: GAME-0361
slug: fallout-new-vegas
game_title: Fallout: New Vegas
analysis_status: reviewed
reviewed: 2026-09-22
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-161
    - ACT-164
    - ACT-183
    - ACT-199
    - ACT-232
    - ACT-341
    - ACT-401
    - ACT-497
  system:
    - SYS-057
    - SYS-215
    - SYS-369
    - SYS-379
    - SYS-740
  constraint:
    - CON-282
    - CON-285
    - CON-572
  information:
    - INF-073
    - INF-115
    - INF-119
    - INF-125
    - INF-128
    - INF-148
    - INF-281
  objective:
    - OBJ-155
  time:
    - TIM-003
    - TIM-007
---

# Game: Fallout: New Vegas

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Goodsprings,
Doc Mitchell, Sunny Smiles, Ringo, Trudy, Easy Pete, Powder Gangers,
S.P.E.C.I.A.L. and `Ghost Town Gunfight` are carrier parameters, not gene names.

## Analysis scope

- Version / ruleset: current unmodified English Windows Steam base game,
  app `22380`, public Build ID `1510068`, checked 2026-09-22. The separately
  distributed DLC depots and Ultimate Edition union are excluded.
- Entry: choose `New Game` on `Normal`, keep the first presented appearance,
  name the Courier `Atlas`, set Strength 5, Perception 5, Endurance 5,
  Charisma 6, Intelligence 7, Agility 6 and Luck 6. Select Explosives,
  Medicine and Speech
  as the three tagged skills, accept the profile, and complete Doc Mitchell's
  departure sequence without optional trait selection.
- Primary decision loop: read the current objective, compass, local threats,
  inventory and dialogue gates; walk the direct route; collect and equip the
  required weapon and ammunition; choose visible skill-gated or ordinary
  responses; recruit available Goodsprings allies; aim, fire and reload in the
  live town fight; then inspect the retained quest and reputation result.
- Fixed route: complete Sunny Smiles's required shooting lesson, enter the
  saloon, choose to help Ringo, recruit Trudy through the available Speech
  check and recruit the remaining allies whose fixed requests are satisfiable
  on the direct route, then tell Ringo the town is ready. Fight Joe Cobb's
  Powder Gangers with the recruited townspeople until the encounter and quest
  settle. Optional loot and any V.A.T.S. use are rejected.
- Positive retained terminal: `Ghost Town Gunfight` is completed for
  Goodsprings, the reward, Goodsprings fame and Powder Gangers infamy are recorded, the
  surviving town returns to ordinary control, and one manual save reloads to
  the same completed quest, inventory, build and reputation state. A recruited
  ally, a dead hostile or a transient autosave alone is intermediate.
- Negative evaluation terminal: death, siding with Joe Cobb, failing to start
  the defended-town branch or reaching a progression-blocking state before
  settlement ends the attempt. Reload may bound the retry but is not positive
  completion.
- Included: fixed S.P.E.C.I.A.L. allocation; exactly three tagged skills;
  visible Speech gate; authored conversation choices; direct traversal and
  contextual interaction; inventory, weapon selection, ammunition and reload;
  hostile awareness and live firearm combat; ally recruitment; ordered quest
  stages; one retained faction outcome; manual save and reload.
- Excluded: Ultimate Edition and all DLC; Hardcore mode; mods and unofficial
  patches; traits; levelling, perks and implants; crafting, repair and gambling;
  V.A.T.S.; stealth as a required route; companions; later Mojave exploration,
  factions, reputation consequences, main quests and endings; console commands;
  other platforms.
- Direct-play status: not directly played. No entitlement, executable, save,
  input trace, screenshot, video or audio was obtained or inspected. This is a
  source-bounded transition reconstruction.
- Scope rationale: Goodsprings joins numeric character creation, a distinct
  three-skill commitment, disclosed conversational eligibility, recruitment,
  live combat and a retained local political result before the open world
  creates too many optional systems for one reproducible packet.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `FNV-001` | Steam distributes Windows app `22380` as the base game and lists DLC separately | Confirmed | Direct | High | P1, R1 |
| `FNV-002` | The scoped public branch is Build ID `1510068`; its base, English and executable depots are distinct from DLC depots | Confirmed | Corroborated | High | R1 |
| `FNV-003` | Character creation commits seven S.P.E.C.I.A.L. values from one bounded pool and then exactly three tagged skills | Confirmed | Direct | High | P2 |
| `FNV-004` | Tagged skills receive a retained starting bonus and can expose later dialogue eligibility | Confirmed | Direct | High | P2 |
| `FNV-005` | The PC manual documents movement, interaction, dialogue, inventory, weapon selection, aim, attack, reload, reputation and saving | Confirmed | Direct | High | P2 |
| `FNV-006` | Goodsprings exposes a visible Speech-gated request while preparing the town defence | Observation | Corroborated | High | S1, S2, S3 |
| `FNV-007` | Choosing Ringo's branch, recruiting allies and starting the fight advances authored quest stages | Observation | Corroborated | High | S1, S2, S3 |
| `FNV-008` | The town fight resolves in real time with equipped weapons, ammunition, reload and autonomous allies and hostiles | Observation | Corroborated | High | P2, S1, S2 |
| `FNV-009` | Settling the Goodsprings branch grants quest rewards plus Goodsprings fame and Powder Gangers infamy | Observation | Corroborated | High | S1, S2, S3 |
| `FNV-010` | A manual save/reload preserves the accepted build, inventory, completed quest and faction reputation state | Confirmed | Corroborated | High | P2, V1 |
| `FNV-011` | V.A.T.S., DLC, Hardcore, traits and later Mojave content are unnecessary to the positive terminal | Confirmed | Direct | High | P1, P2, V1 |
| `FNV-012` | The repository control reconstructs the fixed transitions without executing the game | Observation | Direct | High | V1 |

## Basic data

- Release / origin: Obsidian Entertainment / Bethesda Softworks; Windows,
  Xbox 360 and PlayStation 3 release in October 2010.
- Platform or physical form: current English Windows Steam base game, keyboard
  and mouse, one local single-player save on Normal.
- Puzzle family: tactical forecast and counterplay; real-time system pressure;
  inventory and fixture dependencies; ordered dependency sequencing.
- Primary and first-party sources, accessed 2026-09-22:
  - **[P1]** [official Steam product page](https://store.steampowered.com/app/22380/Fallout_New_Vegas/),
    for app identity, Windows availability, developer, publisher, release and
    separately listed downloadable content.
  - **[P2]** [official English PC manual](https://assets.ctfassets.net/rporu91m20dc/4VrGY6kQ6IqkYmc0GAe4Gc/c272faf09a46104654eda78d78e213f4/manual_fnv-ue_pc_en-us.pdf),
    linked by [Bethesda manual support](https://help.bethesda.net/app/answers/detail/a_id/24583/),
    for character creation, tagged skills, controls, combat, dialogue, inventory,
    reputation and saves. The booklet title reflects the later package; only
    rules shared by the separately scoped base application are imported.
- Reproducible distribution source:
  - **[R1]** [SteamDB depots](https://steamdb.info/app/22380/depots/), for
    public Build ID `1510068`, the base/English/executable depots and separate
    DLC depot boundaries.
- Independent written route sources:
  - **[S1]** [Fallout Wiki: Ghost Town Gunfight](https://fallout.fandom.com/wiki/Ghost_Town_Gunfight),
    for quest stages, ally requests, rewards and faction result.
  - **[S2]** [StrategyWiki route](https://strategywiki.org/wiki/Fallout%3A_New_Vegas/Ghost_Town_Gunfight),
    for an independent ordered Goodsprings preparation and fight account.
  - **[S3]** [GameBanshee route](https://www.gamebanshee.com/falloutnewvegas/walkthrough/ghosttowngunfight.php),
    for an independent branch and recruitment account.
- Reproducible control: **[V1]**
  [`verify_fallout_new_vegas_control.py`](../../../scripts/verify_fallout_new_vegas_control.py),
  a repository-side state reconstruction that does not execute the game.
- Claim IDs: `FNV-001`–`FNV-012`.

## Mechanical decomposition

### Action Genes

- `ACT-008`: walk the Courier through Doc Mitchell's house and Goodsprings.
- `ACT-161`, `ACT-164` and `ACT-183`: select an equipped weapon, aim and fire
  at a reachable hostile, and reload its magazine.
- `ACT-199`: transfer and equip required weapons, ammunition and quest items.
- `ACT-232`: commit the Ringo branch and ally-recruitment dialogue responses.
- `ACT-341`: activate required doors, containers and quest-world fixtures.
- `ACT-401`: distribute the fixed initial S.P.E.C.I.A.L. budget.
- New `ACT-497`: commit exactly three distinct tagged skills from the available
  skill list before leaving character creation.
- Claims: `FNV-003`–`FNV-008`.

### System Behaviour Genes

- `SYS-057` turns hostile awareness into autonomous pursuit and attack;
  `SYS-215` resolves live firearm combat for the Courier, allies and hostiles.
- `SYS-369` restores the bounded save after death or rejected branch state.
- `SYS-379` advances and retains quest and faction results from dialogue,
  recruitment and encounter settlement.
- `SYS-740` applies the committed S.P.E.C.I.A.L. values to the starting profile.
- Claims: `FNV-003`, `FNV-007`–`FNV-010`.

### Constraint Genes

- `CON-282` requires the authored Doc Mitchell, tutorial, Ringo, recruitment and
  fight gates in order.
- `CON-285` requires a compatible equipped weapon, ammunition and reload state.
- `CON-572` bounds the initial S.P.E.C.I.A.L. pool and per-attribute values.
- Claims: `FNV-003`, `FNV-007`, `FNV-008`.

### Information Genes

- `INF-073` exposes equipped weapon and quick-access state; `INF-115` exposes
  partial local hostile state through sight and sound.
- `INF-119` exposes health, action points, ammunition, skills and build;
  `INF-125` exposes the compass, local map and current quest stage.
- `INF-128` exposes loot, inventory contents and equipment compatibility.
- `INF-148` exposes authored responses and the contextual Speech gate.
- `INF-281` exposes initial attribute values and the remaining creation budget.
- Claims: `FNV-003`–`FNV-008`.

### Objective Genes

- `OBJ-155`: carry one authored opening-town action segment into retained
  successor control after the defended settlement resolves.
- Claims: `FNV-007`–`FNV-010`.

### Time Genes

- `TIM-003`: hostiles and allies keep moving and attacking during the town fight.
- `TIM-007`: manual save/reload exposes a player-reversible simulation history.
- Claims: `FNV-008`, `FNV-010`.

## Operational model

1. Allocate the fixed seven-attribute pool, select three tagged skills and
   commit the profile.
2. Complete the ordered tutorial and reach Goodsprings free control.
3. Select Ringo's defence branch; read visible dialogue gates and recruit the
   available allies through their distinct requests.
4. Confirm readiness, equip a firearm and ammunition, and settle the live
   fight without V.A.T.S.
5. Require completed quest, rewards, reputation changes and returned control.
6. Save manually, reload, and verify the same build, inventory, quest and
   reputation state.

## Reproducible transitions

| Before | Action | Deterministic or bounded resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Character creation exposes seven attributes | Commit S5/P5/E5/C6/I7/A6/L6 | The legal total becomes the retained starting profile | fixed numeric creation pool | `FNV-003` |
| Skill list requires three tags | Select Explosives, Medicine and Speech | Exactly three distinct skills receive their starting bonus | fixed-count specialisation action | `FNV-003`, `FNV-004` |
| Sunny Smiles offers the tutorial | Complete the required lesson | Goodsprings free control and later quest contacts remain available | ordered opening gate | `FNV-005`, `FNV-007` |
| Ringo's branch is available | Choose to defend him | Ghost Town Gunfight advances to preparation | authored dialogue changes quest state | `FNV-007` |
| A recruitable ally is addressed | Satisfy the disclosed request or skill check | That ally joins the coming defence | build information changes the action set | `FNV-006`, `FNV-007` |
| Ringo reports readiness | Confirm the town is ready | Powder Gangers enter and live combat begins | preparation settles into encounter | `FNV-007`, `FNV-008` |
| A hostile is alive and reachable | Aim, fire and reload with compatible equipment | Damage resolves while all actors continue | live equipped combat | `FNV-008` |
| The final required hostile is defeated | Wait for quest settlement | Reward, fame, infamy and ordinary control are retained | positive terminal | `FNV-009` |
| Positive terminal is present | Save manually and reload | Build, inventory, completed quest and reputation return | explicit retention check | `FNV-010` |

## Strategic and experiential structure

- Local decision: pick a legal creation value, choose one of exactly three skill
  tags, read a response gate, equip or reload, and select combat position.
- Medium-term planning: build enough Speech, Explosives and Medicine to recruit
  the fixed direct-route allies before committing the town to battle.
- Long-term structure: character creation becomes tutorial, political branch,
  coalition preparation, live conflict and a retained faction result.
- Common heuristics: inspect bracketed response requirements; finish recruitment
  before readiness; keep a loaded firearm; verify the journal and reputation.
- Failure attribution: creation feedback, dialogue labels, objective text,
  health, ammunition, quest state and reload retention separate error classes.
- Player trust: exact build, named branch and immediate save/reload make the
  source-bounded reconstruction falsifiable.

## Replay and variation

- What changes: attack timing, damage, allied survival, loot and micro-route.
- Randomness or procedural generation: combat timing can vary; required quest
  stages and the admitted faction result are authored.
- Multiple viable strategies: other builds and recruits can defend Goodsprings,
  but this packet fixes one reproducible profile and direct route.
- Typical replay motive: different traits, faction branch, difficulty, DLC or
  Mojave route; all remain outside this genome.

## Edge cases and failure states

- Selecting fewer or more than three tagged skills cannot complete the creation
  boundary; a later skill-point allocation is not the same action.
- A visible Speech option may be unavailable if the fixed profile misses its
  threshold; ordinary dialogue remains available but cannot prove that gate.
- Recruiting one ally does not settle the quest. The defence branch still needs
  Ringo's readiness confirmation and encounter completion.
- Joe Cobb's branch is a valid product route but fails this fixed positive
  terminal because it inverts the retained faction outcome.
- Death followed by reload restores an earlier branch state; it is recovery,
  not evidence that the quest settled.
- V.A.T.S. can alter the combat interface but is unnecessary and excluded, so
  no turn-like targeting gene enters the signature.

## Adjacent systems and history

- `GAME-0231` Fallout 4 is the closest lower-ID genome. Both commit a bounded
  S.P.E.C.I.A.L. profile, traverse an authored opening, manage equipment, fight
  in real time and verify retained state by save/reload. New Vegas additionally
  commits three tagged skills, exposes skill-gated dialogue, recruits allies and
  settles a faction reputation result in the bounded opening town.
- `GAME-0353` Deus Ex: Game of the Year Edition also joins dialogue gates,
  inventory, firearm handling, live combat, authored quest state and a retained
  terminal. It lacks the fixed S.P.E.C.I.A.L. pool and tagged-skill creation
  action of this packet.
- `GAME-0258` Prey (2017) shares first-person traversal, equipment, partial
  hostile information, live combat and save recovery but not the creation and
  defended-town political branch.

## Normalised genome

| Type | IDs | Boundary |
|---|---|---|
| Action | `ACT-008`, `ACT-161`, `ACT-164`, `ACT-183`, `ACT-199`, `ACT-232`, `ACT-341`, `ACT-401`, `ACT-497` | traverse, equip, converse, interact, allocate attributes and tag skills |
| System | `SYS-057`, `SYS-215`, `SYS-369`, `SYS-379`, `SYS-740` | hostile pursuit, live combat, recovery, quest retention and build application |
| Constraint | `CON-282`, `CON-285`, `CON-572` | ordered gates, compatible weapon state and fixed creation pool |
| Information | `INF-073`, `INF-115`, `INF-119`, `INF-125`, `INF-128`, `INF-148`, `INF-281` | equipment, threats, build, quest, inventory, dialogue gates and creation budget |
| Objective | `OBJ-155` | settle the authored town segment into retained control |
| Time | `TIM-003`, `TIM-007` | live encounter and reversible save history |

The signature contains 27 genes. `ACT-497` is new; 26 existing boundaries are
reused without changing their meaning.

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `360` (`GAME-0001`–`GAME-0360`).
- Exact genome matches: none.
- Tied near matches: `GAME-0231` — Fallout 4 (`19 / 30 = 0.633333`).
- Supported combination subsets: none.
- Scan date: 2026-09-22.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0231` — Fallout 4 | `ACT-008`, `ACT-161`, `ACT-199`, `ACT-232`, `ACT-341`, `ACT-401`, `SYS-215`, `SYS-369`, `SYS-740`, `CON-282`, `CON-285`, `CON-572`, `INF-115`, `INF-119`, `INF-125`, `INF-128`, `INF-281`, `TIM-003`, `TIM-007` | Both commit the same bounded attribute family, traverse an authored opening, handle equipment, fight in real time and preserve state. Fallout 4 exits a linear vault opening; New Vegas additionally commits three tagged skills, shows skill-gated dialogue, recruits allies and retains a local quest/faction branch. | Near, `19 / 30 = 0.633333` |

### Preserved research notes

- Classification result: one new creation action plus 26 reused traversal,
  dialogue, equipment, combat, quest, information, objective and time boundaries.

## Taxonomy impact

- Add `ACT-497` under
  [`TAXONOMY_CHANGE_100`](../../../research/taxonomy-changes/TAXONOMY_CHANGE_100.md).
- Add support references for all reused genes without changing their definitions.
- Add no combination: the conjunction is distinctive, but no recurring proper
  subset is verified by this unit.

## Delta summary

## New facts

- The exact target is current Steam base app `22380`, not the Ultimate union.
- The bounded Goodsprings route joins a fixed S.P.E.C.I.A.L. profile, three
  tagged skills, disclosed Speech eligibility and recruited town defence.
- Quest settlement retains both a local faction result and ordinary world
  control, verified through manual save/reload.

## New genes

- `ACT-497` — Commit a fixed set of distinct starting skill specialisations.

## New combinations

- None.

## Taxonomy changes

- One addition; no rename, merge, deprecation or earlier-signature rewrite.

## Negative results

- No game executable, save or audiovisual evidence was available.
- V.A.T.S. is optional and excluded rather than misclassified as necessary.
- Later reputation effects, companions, crafting and open-world breadth are not
  imported from the product into this bounded terminal.
- No repeated combination was verified.

## Open questions

- A direct-play module could later pin an executable manifest and measure the
  exact Speech threshold and recruited-party survival under the fixed build.
- A separate faction module could compare reputation consequences beyond
  Goodsprings without changing this opening signature.

## Reproducibility notes

1. Install only Steam app `22380` base depots; disable all DLC and mods.
2. Choose English, keyboard/mouse and Normal difficulty.
3. Create `Atlas` with S5/P5/E5/C6/I7/A6/L6, then tag Explosives, Medicine and
   Speech; choose no optional traits.
4. Complete the shooting lesson, help Ringo and satisfy the fixed direct-route
   ally requests, including the visible Speech-gated recruitment.
5. Confirm readiness and resolve the fight with manual aim/fire/reload only;
   do not use V.A.T.S.
6. Require completed quest, reward, Goodsprings fame, Powder Gangers infamy and
   returned control.
7. Create and reload a manual save; verify build, inventory, quest and reputation.
8. Run `python3 scripts/verify_fallout_new_vegas_control.py`, then the normal
   repository, localisation, web, browser and accessibility gates.

## Localisation review

- Touched Ukrainian game fields were newly authored and `verified`: `profile`,
  `scope`, `directPlay`, presentation title/summary/link label, platform edition
  and the new gene entry.
- `retained-with-reason`: Fallout: New Vegas, Steam, Goodsprings, S.P.E.C.I.A.L.,
  Speech, Explosives, Medicine and quest/source identifiers remain official names or
  stable interface labels where translation would damage identity.
- No generic English explanatory prose is deferred to a batch repair.
