---
game_id: GAME-0188
slug: final-fantasy-xiv-online
game_title: FINAL FANTASY XIV Online
analysis_status: reviewed
reviewed: 2026-08-29
combination_ids:
  - COMB-0186
gene_ids:
  action:
    - ACT-008
    - ACT-161
    - ACT-190
    - ACT-341
  system:
    - SYS-215
    - SYS-362
    - SYS-380
    - SYS-601
    - SYS-602
    - SYS-603
    - SYS-604
    - SYS-605
    - SYS-606
  constraint:
    - CON-269
    - CON-282
    - CON-503
    - CON-504
    - CON-505
  information:
    - INF-119
    - INF-125
    - INF-150
    - INF-242
  objective:
    - OBJ-112
  time:
    - TIM-003
---

# Game: FINAL FANTASY XIV Online

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Parameters describe
gene instances but do not enter the signature.

## Analysis scope

- Version / ruleset: current Windows PC live service at official game/database
  Patch `7.55`, checked 2026-08-29; one ordinary A Realm Reborn `Sastasha`
  instanced dungeon entered through Duty Support and completed with a
  level-synced Gladiator tank. Square Enix does not publish a separate stable
  launcher build number, so the official patch is the reproducible build and
  rules boundary.
- Primary decision loop: register the already-unlocked duty with the preset NPC
  light party; move through the authored cave; establish enemy groups with Iron
  Will, Shield Lob and Total Eclipse; sequence weaponskills on the shared global
  recast and abilities on their own recasts; preserve enmity, health and party
  formation while leaving telegraphed danger; read the Bloody Memo, operate the
  correct coral and switches, collect and use required keys, defeat three boss
  gates and finish by defeating Denn the Orcatoothed.
- Entry and exit: begins when a legal Gladiator of level 18 or higher selects
  Sastasha in Duty Support, accepts the preset Eager Conjurer, Eager
  Thaumaturge and Eager Lancer, selects Commence and is synced to level 18. It
  succeeds when Denn is defeated and the duty-complete result is issued. The
  attempt also closes without success if the 90-minute duty limit expires or
  the player abandons it.
- Included: one controlled Gladiator tank; the level-18-or-lower class and tank
  role kit; fixed healer and two DPS NPC allies; party roles, autonomous ally
  combat, enmity, damage, healing, statuses, target casts and ground telegraphs;
  required main-path enemies, Bloody Memo/coral/switch sequence, Captain's
  Quarters Key, Waverider Gate Key, three boss gates, main-path treasure
  coffers, boss rewards, player incapacitation, boss reset and current Willful
  retry assistance.
- Reproducible parameterisation: use a character with Sastasha unlocked, legal
  ordinary equipment and Gladiator class level at least 18, enter with level
  sync enabled and no unrestricted-party option, and accept the fixed NPC party.
  Exact equipment statistics, random reward items, optional coffer opening,
  enemy pull sizes and completion time are parameters. Use only actions
  available at synced level 18: Fast Blade, Fight or Flight, Riot Blade, Total
  Eclipse, Shield Bash, Iron Will, Shield Lob, Rampart, Low Blow, Provoke and
  Interject.
- Excluded: Sastasha (Hard), Duty Finder and other human players; unrestricted
  or undersized runs; another class/job, actions above level 18 and Paladin-only
  actions; optional side rooms and Mapping the Realm completion; quests before
  entry or after completion; open-world exploration, crafting, gathering, PvP,
  trials, raids, other dungeons, other expansions, retainers, market, glamour,
  housing, account economy, exhaustive levelling and the MMO's full history.
- Potential scoped modules: one other fixed Duty Support dungeon, one declared
  non-tank role, a four-human Duty Finder run or a later raid/trial only when its
  entry, mechanics and terminal are separately bounded.
- Direct-play status: no authenticated live duty was played. Current Square
  Enix patch notes, database, Game Manual, Party Play and Job Guide establish
  the live entry, composition, kit, HUD and retry boundaries. A maintained
  community Sastasha reference supplies the reproducible room-by-room route and
  boss trace where the official database lists outcomes but not the route.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `FFXIV-001` | The official current live/database boundary is Patch `7.55`, and the product title remains FINAL FANTASY XIV Online | Confirmed | Direct | High | P1, P2, P3 |
| `FFXIV-002` | Sastasha is available inside the Starter Edition boundary and admits level 15 characters, syncs at 18, allows 1–4 players and has a 90-minute limit | Confirmed | Direct | High | P2, P3 |
| `FFXIV-003` | Duty Support registers a supported dungeon without matchmaking and fixes A Realm Reborn NPC party members rather than allowing replacements | Confirmed | Direct | High | P4 |
| `FFXIV-004` | The scoped party is one Tank, one Healer and two DPS; a tank diverts enemy attention, a healer restores/protects and DPS concentrate damage | Confirmed | Direct | High | P3, P5 |
| `FFXIV-005` | A synced level-18 Gladiator can combine the declared weaponskills, enmity stance, ranged pull, mitigation, stun and interrupt actions | Confirmed | Direct | High | P6 |
| `FFXIV-006` | Party and target interfaces expose allied condition, enmity, statuses and target cast progress, while authored world markers communicate affected ground | Observation | Direct | High | P7, P8, P9 |
| `FFXIV-007` | Sastasha's required path uses a memo-selected coral, revealed switch, two carried keys and ordered boss/door gates before Denn | Observation | Corroborated | High | P3, S1 |
| `FFXIV-008` | The bounded route has three reward-bearing boss sections and optional treasure coffers whose actual item result can vary | Observation | Direct | High | P3 |
| `FFXIV-009` | Duty Support NPCs fill the missing roles and act autonomously during traversal and combat | Observation | Corroborated | High | P4, S1 |
| `FFXIV-010` | Since Patch 7.4, a boss incapacitation followed by a rechallenge grants Willful stacks; each can prevent one lethal event, up to five, and victory removes them | Confirmed | Direct | High | P10 |
| `FFXIV-011` | The required objective sequence terminates in Denn's defeat and the Sastasha duty-complete state | Observation | Corroborated | High | P3, S1 |
| `FFXIV-012` | The repository transition trace reproduces entry, level sync, NPC roles, enmity combat, switches, keys, bosses, retry assistance and completion | Observation | Direct | High | V1 |

## Basic data

- Release / origin: Square Enix; A Realm Reborn PC service launched in 2013 and
  the scoped live client is maintained through current Patch `7.55`.
- Platform or physical form: authenticated networked Windows PC client; one
  private instanced Duty Support dungeon with NPC allies.
- Puzzle family: real-time system pressure; agent routing and coordination;
  ordered dependency sequencing; inventory and fixture dependencies.
- Primary sources:
  - **[P1]** [official Patch 7.55 notes](https://na.finalfantasyxiv.com/lodestone/topics/detail/99b6bfb8ecac428c7d3bb37dcb84b52f1064320b?pubDate=20260728),
    for the current official live patch boundary, updated 2026-08-04.
  - **[P2]** [official Patch 7.5 product page](https://na.finalfantasyxiv.com/dawntrail/patch_7_5/),
    for the current title and Starter Edition expansion boundary.
  - **[P3]** [official Eorzea Database: Sastasha](https://na.finalfantasyxiv.com/lodestone/playguide/db/duty/b229b89b3a8/?patch=late),
    for Patch 7.55 database state, level sync, party composition, time limit and
    boss/coffer reward sections.
  - **[P4]** [official Duty Support manual](https://na.finalfantasyxiv.com/game_manual/dutysupport/),
    for entry, registration, supported duties and fixed A Realm Reborn NPCs.
  - **[P5]** [official Party Play manual](https://na.finalfantasyxiv.com/game_manual/pp/),
    for light-party size and Tank, Healer and DPS functions.
  - **[P6]** [official Paladin / Gladiator Job Guide](https://na.finalfantasyxiv.com/jobguide/paladin/),
    for the level-18-or-lower Gladiator and Tank-role action kit.
  - **[P7]** [official party-list and enmity UI guide](https://na.finalfantasyxiv.com/uiguide/know/know-hud/hud-name.html),
    for party condition, status and enmity disclosure.
  - **[P8]** [official target-cast UI guide](https://na.finalfantasyxiv.com/uiguide/battle/battle-target/ecast_setting.html),
    for target progress/cast-bar disclosure.
  - **[P9]** [official ground-target UI guide](https://na.finalfantasyxiv.com/uiguide/battle/battle-target/groundtarget_about.html),
    for affected-ground feedback and legal placement.
  - **[P10]** [official Patch 7.4 notes](https://na.finalfantasyxiv.com/lodestone/topics/detail/597d1b99656a1a0d3ba6501a48d43ec46c667068/),
    for Willful stacks, lethal prevention, recovery and boss-victory reset.
- Secondary and reproducible sources:
  - **[S1]** [maintained FFXIV Community Wiki: Sastasha](https://ffxiv.consolegameswiki.com/wiki/Sastasha),
    checked 2026-08-29, for the preset role roster, required route, keys,
    named bosses and observable boss behaviours.
  - **[V1]** repository-side transition trace derived from `P1`–`P10` and `S1`;
    executable rules reasoning, not direct play.
- Claim IDs: `FFXIV-001`–`FFXIV-012`.

## Mechanical decomposition

### Action Genes

- Existing genes: `ACT-008`, navigate the controlled Gladiator through the
  authored dungeon; `ACT-161`, aim and strike a reachable hostile with the
  current weapon action; `ACT-190`, activate one legal class or Tank-role
  ability.
- New gene: `ACT-341`, commit one contextual dungeon interaction with a memo,
  coral, switch, key, gate or treasure coffer.
- Parameters: movement, facing, target, weaponskill, ability, interaction,
  fixture, carried key, reach and resulting gate state.
- Claim IDs: `FFXIV-005`–`FFXIV-007`, `FFXIV-012`.

### System Behaviour Genes

- Existing genes: `SYS-215`, resolve directly commanded real-time hostile
  combat; `SYS-362`, award bounded encounter/coffer loot and progression credit;
  `SYS-380`, resolve selected class and role abilities into typed effects.
- New genes: `SYS-601`, apply level sync and the admitted action/stat boundary
  at duty entry; `SYS-602`, run the three preset NPC roles as an autonomous
  light party around the controlled player; `SYS-603`, accumulate enmity and
  redirect hostile targets; `SYS-604`, schedule weaponskills/spells on a shared
  global recast while independent abilities keep their own recasts; `SYS-605`,
  advance Sastasha through its memo, switch, key, door and boss gates;
  `SYS-606`, transform boss wipes into accumulating Willful protection for the
  rechallenge and clear it on victory.
- Resolution order: duty registration fixes the roster and applies level sync;
  navigation and interaction address the next authored gate; player attacks
  and abilities enter their legal recast schedules; NPC roles move and act;
  damage, healing, status and enmity update target choices; boss incapacitation
  resets the encounter and adds Willful, while a cleared boss removes it;
  required gates unlock the next segment; rewards settle; Denn's defeat closes
  the duty.
- Claim IDs: `FFXIV-002`–`FFXIV-012`.

### Constraint Genes

- Existing genes: `CON-269`, each action requires legal target, range, resource
  and readiness; `CON-282`, required authored encounters depend on prior
  switches, keys, locations and boss state.
- New genes: `CON-503`, Duty Support fixes one player plus three preset NPCs in
  a complete one-Tank/one-Healer/two-DPS light party; `CON-504`, Sastasha entry
  and the usable kit obey the minimum level and level-18 sync boundary;
  `CON-505`, the duty must reach completion before its 90-minute instance limit.
- Scarce strategic resources: health, healer attention, mitigation and
  interrupt readiness, GCD/recast windows, enmity control, safe ground, NPC
  position, required keys, remaining duty time and accumulated Willful stacks.
- Claim IDs: `FFXIV-002`–`FFXIV-007`, `FFXIV-010`–`FFXIV-011`.

### Information Genes

- Existing genes: `INF-119`, expose controlled-character health, statuses and
  action readiness; `INF-125`, expose the explored dungeon map and current
  authored objective/gate; `INF-150`, expose the fixed role roster and kits.
- New gene: `INF-242`, expose party condition, enmity, target cast progress and
  local world/ground danger cues in one live duty interface.
- Claim IDs: `FFXIV-003`–`FFXIV-007`, `FFXIV-009`–`FFXIV-012`.

### Objective Genes

- Existing genes: none.
- New gene: `OBJ-112`, complete one ordinary Sastasha Duty Support run by
  opening every required gate and defeating Denn before the instance limit.
- Success, evaluation and failure: only the issued duty-complete state is
  success; defeating a trash group, opening a coffer or clearing an intermediate
  boss is enabling progress. Timeout and abandon close the attempt without that
  success; a boss wipe is recoverable and feeds Willful rather than ending the
  whole duty.
- Claim IDs: `FFXIV-007`, `FFXIV-010`–`FFXIV-012`.

### Time Genes

- Existing gene: `TIM-003`, player, NPC allies, hostiles, recasts and the
  instance clock evolve concurrently in real time.
- New genes: none.
- Claim IDs: `FFXIV-005`–`FFXIV-012`.

## Reproducible transitions

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Sastasha unlocked; Gladiator level at least 18 | Register through Duty Support and select Commence | Instantiates the private duty, presets healer plus two DPS NPCs and syncs the player to level 18 | bounded entry, roster and build boundary | `FFXIV-002`–`FFXIV-005` |
| Unengaged enemy group; Iron Will active | Use Shield Lob, approach and follow with Total Eclipse | Damage and high-enmity effects accumulate; hostiles prefer the tank while NPCs heal and attack by role | party combat is coupled by threat rather than direct NPC commands | `FFXIV-004`–`FFXIV-006`, `FFXIV-009` |
| Fast Blade is legal and global recast is ready | Commit Fast Blade then Riot Blade after readiness returns | Each weaponskill consumes the shared readiness window and the valid sequence applies its combo effect | global cadence structures otherwise continuous combat | `FFXIV-005` |
| Chopper casts Charged Whisker | Leave the visible local danger region before resolution | The telegraphed area resolves without applying its avoidable paralysis to the moved player | world/cast information changes immediate positioning | `FFXIV-006`, `FFXIV-007` |
| Bloody Memo discloses one coral colour | Interact with the matching coral and revealed switch | Correct state summons Chopper; defeating it and pressing the switch again opens the passage | observation plus fixture interaction gates the route | `FFXIV-007` |
| Captain's Quarters remains locked | Defeat the key holder, collect the key and use it at the door | Consumes the route dependency and admits the room holding the Waverider Gate Key | carried typed key bridges two authored gates | `FFXIV-007` |
| Player becomes incapacitated by a boss | Rechallenge the reset boss encounter | Grants Willful stacks according to prior KOs, up to five; each can prevent one later lethal event and restore full HP through Will to Live | failure changes the next attempt without completing the duty | `FFXIV-010` |
| Boss falls or an admitted coffer opens | Resolve the eligible reward source | An item is selected from the declared table and transferred to the player; exact identity remains a parameter | optional local reward does not replace the route terminal | `FFXIV-008` |
| Waverider Gate opened; final route clear | Defeat Denn the Orcatoothed | Final required objective completes and the duty-complete state is issued | one reproducible Sastasha terminal | `FFXIV-011`, `FFXIV-012` |

## Strategic and experiential structure

- Local decision: choose the next legal target/action, hold enemy attention,
  preserve mitigation, interrupt or move out of a cast, gather a group without
  outrunning NPC support and interact with the next required fixture.
- Medium-term planning: pace pulls around health and recasts, preserve party
  geometry, remember the memo-selected coral, route through both required keys
  and use intermediate bosses as progress/retry boundaries.
- Long-term structure: convert one fixed cave route into five required objective
  flags, three boss clears and the final duty-complete result before the timer.
- Common heuristics: keep Iron Will active; establish enemies before allies draw
  threat; use AoE for groups and the Fast Blade/Riot Blade sequence for focused
  pressure; save mitigation for larger pulls; read target casts and ground;
  ignore optional side rooms when reproducing the main-path scope.
- Failure attribution: illegal recast/target, lost enmity, unmitigated damage,
  missed interrupt, standing in a telegraph, outranging the healer, wrong coral
  or missed key/gate can be separated from random reward identity.
- Player-trust factors: explicit party roles, party/enmity state, visible casts,
  ground cues, persistent objective prompts, opened doors, retry assistance and
  an unmistakable completion result.
- Claim IDs: `FFXIV-004`–`FFXIV-012`.

## Replay and variation

- What changes between sessions: pull sizes, positioning, action cadence, boss
  mistakes, Willful accumulation, optional coffer use and reward identities.
- Randomness or procedural generation: route, gates and bosses are authored;
  reward-table selection and the memo's correct coral colour can vary.
- Multiple viable strategies: the fixed Gladiator/NPC role topology remains,
  but tank route pace, grouping, mitigation, interrupt and target priorities vary.
- Typical replay motive: learn tank cadence, shorten the main route, reduce
  wipes and collect level-appropriate equipment; persistent progression beyond
  the resulting inventory/experience award is excluded.

## Adjacent systems and history

- Direct predecessors: Final Fantasy XI and earlier party-role MMORPGs precede
  XIV; A Realm Reborn replaced the original 1.x service. Those histories are not
  merged into the current bounded duty.
- Variants: Sastasha (Hard), human Duty Finder, unrestricted party, other jobs,
  dungeons, trials, raids and expansion content are separate modules.
- Similar games: Baldur's Gate 3, Monster Hunter Wilds, Clair Obscur:
  Expedition 33, Helldivers 2 and Palworld share selected party, combat,
  authored mission, companion or boss structures.
- Important differences: Baldur's Gate 3 resolves a directly commanded party in
  turns; Sastasha keeps only the tank under direct control and schedules preset
  allies continuously. Monster Hunter Wilds has a timed authored hunt and one
  autonomous Palico but no fixed four-role dungeon or key-gated three-boss path.
  Helldivers 2 uses human co-op, reinforcement stock and extraction; this scope
  has autonomous roles, enmity and a final-boss duty terminal.
- Claim IDs: `FFXIV-002`–`FFXIV-012`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-161`, `ACT-190`, `ACT-341` | navigation, attack, ability and authored interaction parameters |
| System Behaviour | `SYS-215`, `SYS-362`, `SYS-380`, `SYS-601`, `SYS-602`, `SYS-603`, `SYS-604`, `SYS-605`, `SYS-606` | combat, reward, sync, NPC, enmity, cadence, route and retry parameters |
| Constraint | `CON-269`, `CON-282`, `CON-503`, `CON-504`, `CON-505` | action legality, ordered gates, role roster, sync and time limit |
| Information | `INF-119`, `INF-125`, `INF-150`, `INF-242` | personal, route, roster and live party/target state |
| Objective | `OBJ-112` | complete the required Sastasha route and final boss |
| Time | `TIM-003` | concurrent real-time duty state and recasts |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `187` (`GAME-0001`–`GAME-0187`).
- Exact genome matches: none.
- Tied near matches: `GAME-0147` — Marvel Rivals (`9 / 40 = 0.225000`).
- Supported combination subsets: `COMB-0186`.
- Scan date: 2026-08-29.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0147` — Marvel Rivals | `ACT-008`, `ACT-161`, `ACT-190`, `SYS-215`, `SYS-380`, `CON-269`, `INF-119`, `INF-150`, `TIM-003` | both connect direct real-time movement and attacks, typed cooldown abilities, role disclosure and personal HUD state, but Marvel Rivals coordinates six humans through hero selection, ultimate energy, knockout return and a contested escort terminal; Sastasha instead syncs one tank, supplies three autonomous NPC roles, ranks hostile targets by enmity, shares a weaponskill recast and advances one clue/key/boss route with Willful retries | Near, `0.225000` |

### Preserved research notes

- New genes: `ACT-341`, `SYS-601`–`SYS-606`, `CON-503`–`CON-505`,
  `INF-242` and `OBJ-112`.
- Classification result: `New gene` and new verified interaction combination.
- Evidence and reasoning: direct movement, attacks, typed live abilities,
  bounded rewards, action legality, authored gates, personal HUD, roster/map
  visibility and real-time scheduling reuse safely. The precise sync, preset
  NPC, enmity, global-recast, route-gate, Willful and duty-terminal boundaries
  are not present in lower IDs.

## Combination status

- `COMB-0186` is a verified strict twenty-three-gene subset of the twenty-four-
  gene genome, coupling a synced controlled tank, autonomous preset roles,
  enmity and recast combat, authored switches/keys/bosses, wipe-conditioned
  assistance and the final duty terminal.
- Every earlier verified combination is tested deterministically after
  registration; none is a proper subset of this genome.

## Taxonomy impact

- Registry changes: twelve new Active genes, evidence links on twelve reused
  genes, `COMB-0186` and existing family memberships.
- Taxonomy-change record: none; no prior lifecycle or reviewed-game signature
  changes. `SYS-362` receives parameterised wording that keeps its bounded
  encounter-reward boundary while admitting a second evidenced ruleset.
- Candidate terms affected: contextual dungeon interaction, duty level sync,
  preset NPC light party, enmity targeting, shared global recast, authored
  dungeon gate progression, Willful retry assistance and duty completion.

## Negative results

- `CON-474` is not reused: it fixes Overwatch's human 1/2/2 Role Queue and a
  pre-match personal commitment, not a 1/1/2 NPC Duty Support fill around one
  already selected player role.
- `SYS-407` is not reused: one Monster Hunter Palico follows the hunter but does
  not instantiate a complete healer/two-DPS party or role-directed enmity loop.
- `SYS-361` is not reused: its turn-based Break and checkpoint battle retry are
  inseparable from that record; Willful instead conditions a later real-time
  boss attempt on prior player KOs.
- `CON-487` is not reused: Sastasha's 90-minute instance limit is not a fixed
  survival-to-clock-success objective, and a boss wipe does not end the duty.
- Open-world MMO progression, human matchmaking, optional side rooms and the
  rest of the live service are not admitted because the client contains them.

## Delta summary

## Нові факти

- [Confirmed | Direct | High] Current Patch 7.55 supports one Starter-bound
  Sastasha Duty Support run with level-18 sync, a preset 1/1/2 light party,
  authored gates, three bosses, 90-minute limit and current Willful retries
  (`FFXIV-001`–`FFXIV-012`).

## Нові гени

- [Observation | Corroborated | High] Added twelve genes for contextual dungeon
  interaction, level sync, autonomous preset roles, enmity, shared recasts,
  route gates, Willful retries, role composition, duty limit, live party/target
  disclosure and Sastasha completion.

## Нові комбінації

- [Observation | Corroborated | High] `COMB-0186` isolates the synced tank / NPC
  roles / enmity / recast / ordered-gate / retry interaction that produces one
  bounded duty result.

## Зміни таксономії

- [Observation | Corroborated | High] No lifecycle migration or reviewed-game
  signature change; one established encounter-reward boundary gains FFXIV
  evidence without altering its prior meaning.

## Нові питання

- Which later cooperative dungeon preserves role-complete autonomous support
  while replacing enmity or the shared global recast with another coordination
  authority?

## Наступна рекомендована гра

- [Confirmed | Direct | High] `GAME-0189` — Black Myth: Wukong.
- Optimisation criterion: continue the recorded demand-led Goal in exact order.
- Expected information gain: replace a fixed NPC-party duty with one bounded
  solo action-RPG chapter and boss terminal.
- Backlog impact: ninth of nine authorised game units.

## Чому саме вона

- [Confirmed | Direct | High] It is the next immutable subject in
  `SEARCH_DEMAND_GAME_SELECTION_006`.

## Localisation status

- Ukrainian game, new-gene and combination entries are reviewed in this unit.
- The canonical trademark title remains `FINAL FANTASY XIV Online`; Ukrainian
  explanatory prose is presentation-only.

## Open questions

- Recheck the official live patch, Sastasha database and Duty Support retry
  rules on later review-on-touch; keep other duties and job levels outside this
  signature unless separately authorised.
