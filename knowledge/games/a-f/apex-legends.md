---
game_id: GAME-0154
slug: apex-legends
game_title: Apex Legends
analysis_status: reviewed
reviewed: 2026-08-26
combination_ids:
  - COMB-0152
gene_ids:
  action:
    - ACT-008
    - ACT-161
    - ACT-164
    - ACT-183
    - ACT-184
    - ACT-186
    - ACT-187
    - ACT-188
    - ACT-190
    - ACT-191
    - ACT-198
    - ACT-199
    - ACT-200
    - ACT-241
    - ACT-253
  system:
    - SYS-208
    - SYS-215
    - SYS-292
    - SYS-299
    - SYS-316
    - SYS-317
    - SYS-319
    - SYS-321
    - SYS-348
    - SYS-380
    - SYS-421
    - SYS-422
    - SYS-423
  constraint:
    - CON-262
    - CON-268
    - CON-269
    - CON-270
    - CON-272
    - CON-283
    - CON-284
    - CON-285
    - CON-286
    - CON-289
    - CON-371
    - CON-372
  information:
    - INF-073
    - INF-075
    - INF-115
    - INF-116
    - INF-119
    - INF-127
    - INF-128
    - INF-129
    - INF-150
  objective:
    - OBJ-084
  time:
    - TIM-003
---

# Game: Apex Legends

## Analysis scope

- Version / ruleset: public PC Season 30 `Marked`, reviewed 2026-08-26; one
  ordinary Core Unranked Trios Battle Royale match on World’s Edge using the
  current dropship and Jumpmaster start, from Legend selection through full
  squad elimination or last-squad victory.
- Primary decision loop: commit one non-duplicated Legend, choose and steer the
  squad’s insertion, build a match-local weapon and supply loadout, communicate
  partial hostile and route information, fight and recover squadmates, and
  rotate through the contracting Ring until only one squad remains.
- Entry and exit: enter the staggered three-player Legend selection with no
  match inventory; exit when every member of the squad is irrecoverably
  eliminated or when the squad is declared the last one alive.
- Included: one three-player squad among a 60-player field; unique Legend
  selection, five classes and the selected Legend’s passive, tactical and
  ultimate kit; Jumpmaster, dropship exit and skydive; ground, Supply Bin and
  deathbox loot; two-weapon inventory, compatible ammunition and attachments;
  Marked locked hop-ups and one corrupted attachment per weapon; health,
  Legend Armor, restorative items, knockdown shields, downing and allied
  revival; deathbox, Legend Banner, Replicator and Respawn Beacon return;
  team pings and frames; EVO levels and perk choices; the shrinking damaging
  Ring; full-squad elimination and last-squad victory.
- Excluded: Ranked Points, ladders, entry costs and Drop Zone matchmaking;
  Duos, Solo, Bot Royale Evolved, Wildcard, Mixtape, Arenas, Training, Firing
  Range, Private and limited-time modes; exhaustive Legend-specific kits,
  exact map rotation, events and balance values; Battle Pass, challenges,
  account unlocks, cosmetics, store, esports and post-match progression.
- Potential scoped modules: a later Ranked packet could model placement/RP,
  entry cost and hybrid Drop Zone rules; Wildcard would require its separate
  auto-loot, weapon-tier and revival rules rather than being folded into this
  Core signature.
- Direct-play status: no authenticated live match was played. Current official
  EA mode, season, controls, Legend, weapon, item and Battle Royale material was
  cross-checked on 2026-08-26. A current beginner page also mentions automatic
  pre-Ring-4 respawn, while the newer mode guide says Core relies on deathbox,
  Banner, Replicator and Beacon return; the conflicting automatic-return claim
  is therefore excluded from the canonical transition packet.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `APX-001` | Core Battle Royale uses 60-player matches and the terminal goal is to leave one Duo or Trio squad alive | Confirmed | Corroborated | High | P2, P7 |
| `APX-002` | The scoped start commits one unique Legend per squad slot, one volunteer or assigned Jumpmaster and one steerable dropship insertion | Observation | Corroborated | High | P1, P3, P4 |
| `APX-003` | Legends belong to one of five classes and expose a passive, tactical and ultimate kit whose legal effects alter combat, protection, movement, healing or information | Confirmed | Corroborated | High | P4 |
| `APX-004` | World and deathbox loot forms a bounded match loadout whose ammunition, attachment compatibility, locked hop-up progress and corrupted-attachment limit affect weapon use | Observation | Corroborated | High | P1, P3, P5, P6 |
| `APX-005` | Damage crosses visible armour and health, may enter a shielded downed state and permits an eligible teammate revival before full death | Observation | Corroborated | High | P3, P6 |
| `APX-006` | A dead Core teammate can return through the current deathbox or Banner-and-Respawn-source process while a squadmate remains able to complete it | Observation | Corroborated | Medium | P2, P6, P9 |
| `APX-007` | Successive Ring states contract the playable area and damage Legends outside it, forcing live rotation toward encounters | Confirmed | Corroborated | High | P2, P6, P7 |
| `APX-008` | Team pings deliberately transmit enemy, loot and route cues while team frames expose allied and match state without revealing all enemies | Confirmed | Corroborated | High | P3, P8 |
| `APX-009` | Match-local EVO thresholds raise Legend level, grow armour and expose a bounded perk choice; weapon activity separately unlocks the bound hop-up | Observation | Corroborated | High | P2, P5 |

## Basic data

- Release / origin: Respawn Entertainment / Electronic Arts; first public
  release 2019; continuously updated, scoped to Season 30 `Marked` launched
  2026-08-04 and reviewed 2026-08-26.
- Platform or physical form: networked Windows PC client; the scoped public
  Core match requires a persistent connection and EA account.
- Puzzle family: partial-information squad survival under contracting spatial
  pressure.
- Primary sources:
  - **[P1]** [official Marked patch notes](https://www.ea.com/games/apex-legends/apex-legends/news/marked-patch-notes),
    for the Season 30 boundary, current World’s Edge rotation, loot overhaul,
    corrupted attachments, weapon state and volunteer Jumpmaster.
  - **[P2]** [official current game-mode guide](https://help.ea.com/en/articles/apex-legends/game-modes/),
    for Core/Unranked scope, full loot, item-based healing and the current Core
    deathbox, Replicator and Respawn Beacon recovery distinction.
  - **[P3]** [official beginner guide](https://help.ea.com/en/articles/apex-legends/how-to-play/),
    for Core squad communication, loot, ammunition, shields, downing, revival,
    movement and Ring decisions, including the recorded respawn-source conflict.
  - **[P4]** [official Legend guide](https://help.ea.com/en/articles/apex-legends/abilities/),
    for the 28-Legend roster, five classes, three-part ability kits, fixed
    in-match identity and current class effects.
  - **[P5]** [official weapons guide](https://help.ea.com/en/articles/apex-legends/guns-and-weapons/),
    for compatible ammunition, Core locked hop-ups, weapon-bound progress,
    corrupted-attachment tradeoffs and the one-corrupted limit.
  - **[P6]** [official current terms guide](https://help.ea.com/en/articles/apex-legends/terms-guide/),
    for knocked state, deathboxes, Banners, Replicators, Beacons, Ring, loot,
    starter equipment, Shield Cores and last-squad vocabulary.
  - **[P7]** [official Battle Royale mode page](https://www.ea.com/ar/games/apex-legends/apex-legends/apex-legends-modes-hub/battle-royale),
    for 60-player matches, shrinking Ring, better equipment and last-squad
    victory across Duos and Trios.
  - **[P8]** [official controls guide](https://help.ea.com/en/articles/apex-legends/pc-and-controller-settings/),
    for direct movement, attack, reload, grenade, ability, restorative, ping,
    map and inventory inputs.
  - **[P9]** [official Overclocked patch notes](https://www.ea.com/games/apex-legends/apex-legends/news/overclocked-patch-notes),
    for direct deathbox respawn, retained unlooted gear, lockout growth and the
    continuing Respawn Beacon alternative.
- Secondary sources: none required for the accepted bounded claims; the
  unresolved automatic-respawn discrepancy is recorded instead of being
  silently harmonised.
- Claim IDs: `APX-001`–`APX-009`.

## Mechanical decomposition

### Action Genes

- Existing genes: `ACT-008`, directly navigate the Legend; `ACT-161`, aim and
  strike with the current weapon; `ACT-164`, select a carried weapon, ordnance
  or restorative; `ACT-183`, reload a magazine-fed weapon; `ACT-184`, prime and
  throw ordnance; `ACT-186`, drop eligible carried loot; `ACT-187`, transmit a
  tactical ping, voice or text cue; `ACT-188`, commit one unique match Legend;
  `ACT-190`, cast a legal tactical or ultimate; `ACT-191`, spend an unlocked
  EVO perk choice; `ACT-198`, commit dropship exit and steer descent;
  `ACT-199`, transfer and equip compatible loot; `ACT-200`, use an interruptible
  health or shield restorative; `ACT-241`, revive a reachable downed ally.
- New gene: `ACT-253`, initiate one eligible dead-squadmate return through the
  deathbox, recovered or crafted Banner and current Respawn source.
- Parameters: Legend, class, perk branch, Jumpmaster, exit time, drop vector,
  weapon, fire mode, attachment, ammo, inventory slot, restorative, ping type,
  ability, downed ally, deathbox, Banner, Replicator and Beacon.
- Claim IDs: `APX-002`–`APX-009`.

### System Behaviour Genes

- Existing genes: `SYS-208`, resolve ranged attacks through cover, hit region
  and defence; `SYS-215`, resolve live hostile combat; `SYS-292`, resolve
  ordnance trajectory and field effect; `SYS-299`, convert match activity and
  EVO thresholds into Legend levels and perk opportunities; `SYS-316`, sample
  participant, dropship and world-loot state; `SYS-317`, resolve freefall and
  landing; `SYS-319`, apply completed health or shield restoration; `SYS-321`,
  reveal and contract the Ring while applying outside damage; `SYS-348`,
  resolve armour, health, downing, allied revival and full death; `SYS-380`,
  resolve selected Legend abilities into typed live effects.
- New genes: `SYS-421`, convert weapon activity into one bound hop-up unlock;
  `SYS-422`, return an eligible dead squadmate through a deathbox or Respawn
  source; `SYS-423`, convert simultaneous full-squad defeat into elimination
  and the final remaining squad into the match winner.
- Resolution order: assign the field, map state, dropship route and loot;
  commit non-duplicated Legends and Jumpmaster; resolve insertion; accept live
  movement, looting, combat, ability, perk, ping and recovery inputs while the
  Ring advances; move lethal damage through downed and revival opportunity to
  deathbox state; return an eligible teammate only through a completed Core
  respawn path; remove a squad when no member remains active or return-eligible;
  terminate when one squad remains.
- Parameters: roster and bot fill, dropship line, loot tables, ballistics,
  shield/health values, revive and respawn durations, EVO sources and thresholds,
  hop-up points, ability kits, Ring phases, squad state and winner ordering.
- Claim IDs: `APX-001`–`APX-009`.

### Constraint Genes

- Existing genes: `CON-262`, typed weapon, ordnance and ammunition capacity;
  `CON-268`, one available Legend per fixed squad slot; `CON-269`, ability use
  requires a legal target, resource and readiness; `CON-270`, perk choice is
  bounded by current EVO level and branch; `CON-272`, death blocks direct
  control until a legal return; `CON-283`, dropship route and descent bound
  reachable insertion; `CON-284`, backpack and equipment slots bound the
  loadout; `CON-285`, weapons require compatible ammunition and action state;
  `CON-286`, restorative use requires eligible missing state and an uninterrupted
  cast; `CON-289`, successive Ring phases impose escalating live deadlines.
- New genes: `CON-371`, Core teammate return requires an eligible downed or dead
  ally, a living squad actor, the required Banner/source state and a completed
  interruptible channel; `CON-372`, a locked hop-up remains bound to its weapon
  progress and each weapon accepts at most one compatible corrupted attachment.
- Scarce strategic resources: living squad members, safe revive time, Banner
  and Respawn access, health, armour charge, restorative supply, ammunition,
  magazine readiness, compatible attachment slots, backpack space, ability
  cooldowns, EVO opportunity, concealment, high ground and Ring travel time.
- Claim IDs: `APX-002`–`APX-009`.

### Information Genes

- Existing genes: `INF-073`, carried weapons, ammunition and active item are
  visible; `INF-075`, current health and armour state are visible; `INF-115`,
  local sight, sound and effects expose partial opponent state; `INF-116`, team
  frames, allied state, pings and live match phase are visible; `INF-119`, the
  personal Legend HUD exposes health, armour, EVO, perks and ability readiness;
  `INF-127`, map and HUD expose insertion, Ring and phase timing; `INF-128`,
  world loot and inventory expose identity and compatibility; `INF-129`,
  survivor/squad count, elimination feed and terminal placement are visible;
  `INF-150`, the selection roster exposes Legends, classes and kits.
- New genes: none.
- Claim IDs: `APX-002`–`APX-009`.

### Objective Genes

- New gene: `OBJ-084`, remain the last living squad in one bounded Battle
  Royale match.
- Success, evaluation and failure: a squad wins when at least one member remains
  after every other squad has reached terminal elimination; kills, damage, EVO
  and placement below first do not independently complete the Unranked objective.
- Claim IDs: `APX-001`, `APX-007`.

### Time Genes

- Existing gene: `TIM-003`, movement, combat, casts, cooldowns, downed windows,
  respawn channels and Ring phases progress in continuous real time.
- Parameters: simulation tick, weapon cadence, reload, ability cooldown,
  restorative/revive/respawn channel, Ring warning and contraction schedule.
- Claim IDs: `APX-003`–`APX-009`.

## Reproducible transitions

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Three squad slots enter selection and Bangalore is unoccupied | Commit Bangalore | The slot receives Bangalore’s class, passive, tactical and ultimate for the match; another slot cannot duplicate her | fixed squad identity | `APX-002`, `APX-003` |
| The dropship approaches a reachable World’s Edge region | Jumpmaster exits and the squad steers or splits | Flight timing, descent control and collision map the commitment into one landing region | insertion is a shared spatial commitment | `APX-002` |
| Compatible rifle, ammunition and attachment lie within reach | Transfer and equip them | Legal slots accept the items, current capacity updates and the weapon becomes usable with its compatible state | found loot becomes a bounded match loadout | `APX-004` |
| A locked hop-up is attached to the current weapon | Deal eligible damage or use an eligible upgrade source | Weapon-bound progress crosses its threshold and activates that hop-up for whoever later carries the same weapon | weapon progression persists with the object | `APX-004`, `APX-009` |
| Bangalore has a ready Smoke Launcher and legal target space | Cast the tactical | The typed ability creates its current smoke effect and starts the declared readiness cycle | Legend identity changes available spatial counterplay | `APX-003` |
| Incoming damage exhausts armour and health without immediate finishing damage | Raise the knockdown shield while an ally approaches | Control contracts to downed movement/shield state; a completed legal ally channel restores live control | defeat has a recoverable squad stage | `APX-005` |
| A squadmate is dead and leaves a legal Core deathbox/Banner path | Initiate the current deathbox or Respawn-source interaction | A completed legal channel returns that teammate under the source’s equipment, timing and visibility rules | full death can remain squad-recoverable | `APX-006` |
| The next Ring is revealed outside the squad’s current position | Rotate late or continue looting | The boundary contracts on schedule and outside damage applies until entry, recovery or defeat | spatial uncertainty becomes a forced deadline | `APX-007` |
| Another squad is heard beyond occluding cover | Ping the observed direction and regroup | The bounded team channel adds the cue to allied live information without exposing hidden enemy state | communication changes shared partial knowledge | `APX-008` |
| Two squads remain and every member of one reaches terminal defeat | Preserve at least one living member | The defeated team is eliminated, the squad count reaches one and the remaining squad receives victory | squad survival and terminal objective share one transition | `APX-001` |

## Strategic and experiential structure

- Local decision: expose and shoot, reload, heal armour or health, cast an
  ability, revive, loot, ping, retreat or preserve a safer firing angle under
  incomplete hostile information.
- Medium-term planning: choose a landing density, distribute compatible weapons
  and supplies across the trio, select EVO perks, preserve respawn access and
  rotate before the Ring removes terrain options.
- Long-term structure: keep at least one recoverable squad line alive while
  converting found loadout, Legend-role complementarity and position into a
  sequence of favourable fights until the final Ring.
- Common heuristics: land close enough to trade without duplicating loot paths,
  communicate enemy and item locations, avoid healing in exposed channels,
  prefer an early viable rotation and disengage when a deathbox or Banner is
  more valuable than another immediate fight.
- Failure attribution: visible health, armour, cooldowns, squad frames, Ring
  timing and elimination state make many errors inspectable; random loot,
  hidden squads and simultaneous teammate choices retain material uncertainty.
- Player-trust factors: current personal, squad and Ring state is exposed,
  while future loot, Ring centres and opponent decisions remain concealed.
- Claim IDs: `APX-002`–`APX-009`.

## Replay and variation

- What changes between sessions: players or allowed bots, squad compositions,
  dropship line, landing choices, loot and attachments, Ring centres, EVO/perk
  choices, respawn opportunities and encounter order.
- Randomness or procedural generation: the authored map remains stable while
  participant fill, insertion, loot and Ring states vary within current tables.
- Multiple viable strategies: hot or remote drop, edge or early-zone rotation,
  aggressive ability composition or recovery-focused support, close- or
  long-range loadouts and contest or disengage around a dead teammate.
- Typical replay motive: mastery of movement, aim, Legend kits, team information
  and risk conversion across changing spatial and loot states.
- Claim IDs: `APX-001`–`APX-009`.

## Adjacent systems and history

- Direct predecessors: Titanfall’s movement and class-shooter lineage plus the
  established battle-royale form; this analysis does not assign unreviewed
  predecessor mechanics to the corpus.
- Variants: Ranked adds RP, entry cost, placement scoring and hybrid Drop Zone
  rules; Wildcard changes loot, weapon tiers, healing and revival; Duos changes
  squad capacity; Mixtape and Arenas replace last-squad survival.
- Similar games: PUBG: BATTLEGROUNDS shares aerial insertion, stochastic loot,
  firearm inventory and a contracting damaging area; Marvel Rivals shares
  directly controlled role-differentiated heroes, cooldown abilities, team
  information and revival-capable live combat.
- Important differences: Apex replaces PUBG Solo’s permanent first lethal
  defeat with a three-person down/revive/deathbox-return state and adds committed
  Legend kits plus EVO perks, while retaining one continuous last-survivor match
  rather than Marvel Rivals’ repeated objective respawns.
- Claim IDs: `APX-001`–`APX-009`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-161`, `ACT-164`, `ACT-183`, `ACT-184`, `ACT-186`–`ACT-191`, `ACT-198`–`ACT-200`, `ACT-241`, `ACT-253` | Legend, weapon and ping identities are parameters |
| System Behaviour | `SYS-208`, `SYS-215`, `SYS-292`, `SYS-299`, `SYS-316`, `SYS-317`, `SYS-319`, `SYS-321`, `SYS-348`, `SYS-380`, `SYS-421`–`SYS-423` | damage, loot, EVO and Ring values are parameters |
| Constraint | `CON-262`, `CON-268`–`CON-270`, `CON-272`, `CON-283`–`CON-286`, `CON-289`, `CON-371`, `CON-372` | squad size, capacities and durations are parameters |
| Information | `INF-073`, `INF-075`, `INF-115`, `INF-116`, `INF-119`, `INF-127`–`INF-129`, `INF-150` | exact HUD styling is presentation |
| Objective | `OBJ-084` | initial squad count is a parameter |
| Time | `TIM-003` | all admitted play remains live |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `153` (`GAME-0001`–`GAME-0153`).
- Exact genome matches: none.
- Tied near matches: `GAME-0140` — PUBG: BATTLEGROUNDS (`29 / 65 = 0.446154`).
- Supported combination subsets: `COMB-0152`.
- Scan date: 2026-08-26.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| PUBG: BATTLEGROUNDS (`GAME-0140`) | `ACT-008`, `ACT-161`, `ACT-164`, `ACT-183`, `ACT-184`, `ACT-186`, `ACT-198`–`ACT-200`, `SYS-208`, `SYS-215`, `SYS-292`, `SYS-316`, `SYS-317`, `SYS-319`, `SYS-321`, `CON-262`, `CON-283`–`CON-286`, `CON-289`, `INF-073`, `INF-075`, `INF-115`, `INF-127`–`INF-129`, `TIM-003` | a three-player non-duplicate Legend composition with EVO perks, layered knocked/revive/death states and conditional teammate return versus one permanently vulnerable Solo survivor with vehicles, Red Zones, destructible terrain and no squad recovery | Near, `0.446154` |

### Preserved research notes

- New genes: `ACT-253`, `SYS-421`–`SYS-423`, `CON-371`, `CON-372`, `OBJ-084`.
- Classification result: `New gene` and `New combination of known and new genes`.
- Evidence and reasoning: the current corpus already isolates most firearm,
  aerial insertion, Ring, hero ability, team information, downing and
  match-progression boundaries. The new records are restricted to Core
  squad-return interaction, weapon-bound hop-up progression, full-squad
  adjudication, the legal recovery/attachment gates and last-squad victory.

## Taxonomy impact

- Registry changes: add seven bounded active genes and `COMB-0152`; add Apex
  evidence to reusable battle-royale, hero, squad-revival and information
  records without changing an earlier game signature.
- Taxonomy-change record: none.
- Candidate terms affected: battle royale, hot drop, third party, rotation,
  ratting, Legend meta and weapon names remain genre, strategy or parameter
  vocabulary.

## Negative results

- The current official beginner page’s automatic pre-Ring-4 respawn statement
  conflicts with the current Core mode guide’s item/source-based recovery
  boundary. It is excluded pending direct reproduction rather than promoted to
  a gene or separate negative-result record.
- `OBJ-074` and `CON-290` are absent because the scoped unit is squad survival
  with recovery, not PUBG Solo’s permanent individual defeat.

## Delta summary

## Нові факти

- [Confirmed | Corroborated | High] `APX-001`–`APX-009`: Core Unranked Trios
  поєднує 60-player last-squad survival, Legend roles, dropship insertion,
  match-local loot, Ring pressure, EVO perks, down/revive і Core respawn sources.

## Нові гени

- [Observation | Corroborated | High] Додано сім genes для Core teammate
  return, weapon-bound hop-up progression, full-squad adjudication, recovery
  and corrupted-attachment gates та last-squad objective.

## Нові комбінації

- [Confirmed | Corroborated | High] `COMB-0152` — role-bound squad recovery
  through contracting Battle Royale survival.

## Зміни таксономії

- [Observation | Direct | High] Змін таксономії немає; попередні signatures не
  змінено.

## Нові питання

- Чи Slay the Spire 2 повторює достатню частину першої гри, щоб поточні
  deckbuilding boundaries залишилися стабільними після версійного Early Access
  scope test?

## Наступна рекомендована гра

- [Hypothesis | Limited | High] `GAME-0155` — Slay the Spire 2.
- Optimisation criterion: continue the authorised nine-game Goal while moving
  from live squad combat to a version-bounded solo deckbuilding run.
- Expected information gain: direct recurrence and divergence against Slay the
  Spire, Balatro and Inscryption under an unfinished Early Access endpoint.
- Backlog impact: advances the recorded order without displacing `GAME-0156`
  Strands or any later authorised subject.

## Чому саме вона

- [Hypothesis | Limited | High] The next unit provides maximum scope and reuse
  contrast after a 51-gene live-service packet while testing a publicly legible
  close-relative comparison.
