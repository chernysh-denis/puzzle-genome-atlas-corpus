---
game_id: GAME-0222
slug: call-of-juarez-gunslinger
game_title: "Call of Juarez: Gunslinger"
analysis_status: reviewed
reviewed: 2026-09-02
combination_ids:
  - COMB-0220
gene_ids:
  action:
    - ACT-008
    - ACT-161
    - ACT-164
    - ACT-183
    - ACT-191
    - ACT-199
    - ACT-229
    - ACT-390
  system:
    - SYS-215
    - SYS-299
    - SYS-348
    - SYS-368
    - SYS-369
    - SYS-717
    - SYS-718
    - SYS-719
  constraint:
    - CON-262
    - CON-270
    - CON-282
    - CON-285
  information:
    - INF-073
    - INF-115
    - INF-119
    - INF-125
    - INF-276
  objective:
    - OBJ-138
  time:
    - TIM-003
---

# Game: Call of Juarez: Gunslinger

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Parameters describe
gene instances but do not enter the signature.

## Analysis scope

- Version / ruleset: current unmodified English Windows Steam app `204450`,
  public Build ID `168269`, built 2014-01-13 and checked 2026-09-02; Story mode,
  Normal difficulty, mouse and keyboard, first episode `Once Upon a Time in
  Stinking Springs` from a fresh profile.
- Primary decision loop: read the current objective, health, weapon,
  ammunition, experience, combo and Concentration state; traverse the authored
  ranch route; aim, fire, reload, switch or collect a compatible weapon; chain
  accurate kills for experience; activate available Concentration to slow the
  pressure; spend earned skill points; survive the farmhouse and stable route;
  balance duel focus and draw-hand speed; react to Pat Garrett's draw; then
  accept the narrator's correction, repeated stable approach and true outcome.
- Entry and exit: entry is first retained control on the dirt path after
  selecting Story, New Game and Normal on a fresh profile. Positive exit is the
  episode-complete transition after the corrected objective `Get the horses...
  this time for real` and the second stable entry, where Garrett recognises
  Silas is not Billy the Kid. Death/checkpoint retry and the first apparent
  duel victory are not positive terminals.
- Included: direct first-person movement; authored objectives and route gates;
  revolver, rifle, shotgun and available dynamite use; aiming, firing, finite
  magazines/reserves, reload, weapon switching and pickups; enemy damage and
  defeat; health, death and checkpoint retry; kill score, time-bounded combo,
  experience threshold and one eligible skill allocation; charged
  Concentration; first duel hand-speed/focus preparation, draw order, shot and
  result; the narrator-triggered rewind/replacement of the stable scene; the
  corrected stable re-entry and episode completion.
- Excluded: every later Story episode; Arcade and Duel modes; True West and
  Hard difficulty; New Game Plus; all later skill-tree development, weapons,
  duels and narration transformations; Nuggets of Truth completion;
  achievements as objectives; leaderboards; speedruns, glitches, mods, saves
  imported from another profile, controllers, Steam Deck, consoles and Switch;
  whole-campaign plot interpretation and whole-series union.
- Reproducible parameterisation: begin a clean Story New Game on Normal; retain
  default mouse/keyboard bindings; record one ordinary shot, reload, pickup,
  combo increment, Concentration activation, skill spend and checkpoint retry
  if naturally reached; at Garrett, maintain both focus and draw-hand speed,
  wait for his visible draw for the ordinary honourable trace, draw and fire;
  continue through the forced correction and enter the stable again. Exact
  weapon, aim point, combo length, skill node, health, ammunition, enemy
  positions, checkpoint use and duration are run parameters.
- Potential scoped modules: one later named Story episode; one Arcade mission;
  Duel Challenge; complete Story; New Game Plus; another difficulty; or the
  separate Nintendo Switch release.
- Direct-play status: not conducted. Current official Techland and Steam pages,
  Steam distribution metadata and two maintained written walkthroughs establish
  the declared product, mode, route, duel, correction and terminal. The trace
  below is evidence-based rules reconstruction, not a claimed captured
  playthrough. No video or audio was opened, played, heard or used.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `COJG-001` | The current Steam product is the Windows single-player `Call of Juarez: Gunslinger`; its public branch is Build ID `168269` | Confirmed | Corroborated | High | P1, P2, S1 |
| `COJG-002` | Story, Arcade and Duel are separate modes, and this packet admits only Story on Normal | Confirmed | Direct | High | P2 |
| `COJG-003` | `Once Upon a Time in Stinking Springs` is the first playable episode and begins from a fixed dirt-path control state | Observation | Corroborated | High | S2, S3 |
| `COJG-004` | Silas directly traverses, aims, fires, switches, reloads and collects compatible weapons while authored enemies attack in real time | Observation | Corroborated | High | P1, P2, S2, S3 |
| `COJG-005` | Eligible rapid kills extend a visible combo and multiply experience, while thresholds expose skill points that can enter one eligible branch node | Observation | Corroborated | High | P1, P2, S2 |
| `COJG-006` | Available Concentration temporarily slows live hostile action and improves target reading while consuming its charged state | Observation | Corroborated | High | S2, S3 |
| `COJG-007` | The first duel independently tracks opponent focus and the proximity of Silas's hand to the revolver before draw input | Observation | Corroborated | High | S2, S3 |
| `COJG-008` | Draw order distinguishes an honourable response from an early draw, while speed and focus determine draw delay and post-draw aiming opportunity | Observation | Corroborated | High | S2, S3 |
| `COJG-009` | Winning the first apparent duel does not settle the episode: narration rejects that scene, restores the earlier approach and replaces the objective | Observation | Corroborated | High | S2, S3 |
| `COJG-010` | The corrected objective requires entering the stable again; Garrett's recognition transition ends the episode | Observation | Corroborated | High | S2, S3 |
| `COJG-011` | Death restores an authored checkpoint, while the narrator correction is a compulsory authored state replacement rather than player-controlled rewind | Observation | Corroborated | High | S2, S3, V1 |
| `COJG-012` | The bounded identity is ordinary score-aware FPS combat interrupted by a two-channel duel and then mechanically revised by unreliable narration | Strong Pattern | Corroborated | High | COJG-003–COJG-011 |

## Basic data

- Release / origin: developed by Techland and currently published by Techland
  Publishing; original PC release 2013-05-22, publishing rights returned to
  Techland in 2018.
- Platform or physical form: authored single-player first-person action game;
  only the current unmodified Windows Steam Story episode declared above is
  admitted.
- Puzzle family: tactical forecast and counterplay; real-time system pressure;
  spatial logic and topology; ordered dependency sequencing.
- Primary and official sources:
  - **[P1]** [official Steam product page](https://store.steampowered.com/app/204450/Call_of_Juarez_Gunslinger/),
    for current title, developer/publisher, Windows single-player delivery,
    firearms, lethal combos and selectable gunfighting skills.
  - **[P2]** [official Techland product announcement](https://techland.net/news/call-of-juarez-gunslinger-is-now-available-on-nintendo-switch),
    for developer/publisher ownership, Story/Arcade/Duel separation, personalised
    skills, weapon mastery, lethal combos and gunslinger duels. Switch-specific
    controls and enhancements are excluded.
  - **[P3]** [official Steam achievement registry](https://steamcommunity.com/stats/CallofJuarezGunslinger/achievements/),
    used only to corroborate named skill, combo, Concentration, honourable-duel
    and whole-Story concepts; achievements do not define this packet terminal.
- Secondary and reproducible sources:
  - **[S1]** [SteamDB app depots](https://steamdb.info/app/204450/depots/),
    observed 2026-09-02, for the public Windows branch Build ID `168269`, built
    2014-01-13. SteamDB is explicitly a secondary distribution mirror.
  - **[S2]** [Gamepressure episode-one walkthrough](https://www.gamepressure.com/callofjuarezgunslinger/episode-1-once-upon-a-time-in-stinking-springs/zb50ea),
    for the fixed route, weapon/skill introduction, Concentration, Sense of
    Death, stable duel, return to the path and second stable entry.
  - **[S3]** [GameFAQs written walkthrough](https://gamefaqs.gamespot.com/ps3/682514-call-of-juarez-gunslinger/faqs/67111),
    for the independent objective trace, duel focus/draw handling, explicit
    `Rewind...`, corrected objective and stable re-entry. Platform-specific
    button names are not admitted as rules.
- Reproducible control: **[V1]** repository-side transition trace across
  `P1`–`P3` and `S1`–`S3` under the declared clean-profile entry, Normal mode
  and exclusions; rules reasoning, not direct play.
- Claim IDs: `COJG-001`–`COJG-012`.

## Mechanical decomposition

### Action Genes

- Existing `ACT-008`: directly walk, sprint, crouch and jump Silas through the
  authored ranch, farmhouse and stable route.
- Existing `ACT-161`: aim and commit a revolver, rifle, shotgun, dynamite or
  contextual direct attack against a reachable hostile; `ACT-164`: switch the
  active weapon; `ACT-183`: reload a compatible finite magazine; `ACT-199`:
  collect compatible weapons and ammunition.
- Existing `ACT-191`: spend an earned skill point on an eligible node; existing
  `ACT-229`: activate the charged Concentration special.
- New `ACT-390`: simultaneously maintain the duel's focus reticle on the
  opponent and position Silas's draw hand near the holstered revolver, then
  commit the draw in response to the opponent or early by choice.
- Parameters: route, stance, aim, weapon, ammunition, target, pickup, combo,
  skill node, Concentration meter, duel focus, hand speed and draw input.
- Claim IDs: `COJG-004`–`COJG-008`, `COJG-012`.

### System Behaviour Genes

- Existing `SYS-215`: resolve directly commanded real-time firearm and
  explosive combat; `SYS-348`: apply damage through visible health into death;
  `SYS-369`: restore the current authored checkpoint after failed attempt.
- Existing `SYS-299`: convert combat experience thresholds into persistent
  level/skill-point opportunity; `SYS-368`: drain charged Concentration while
  applying its temporary combat time/target modifier, then restore it through
  eligible combat.
- New `SYS-717`: an eligible rapid-kill chain advances the combo multiplier and
  applies it to experience awards until the live continuation window expires.
- New `SYS-718`: the duel continuously derives focus and draw speed from two
  independent maintained inputs, classifies draw order, then converts them into
  draw delay, aim stability and the live shot/result window.
- New `SYS-719`: an authored narrator correction rejects the apparent stable
  outcome, restores the declared earlier route state and replaces objective and
  scene content with the corrected continuation.
- Resolution order: disclose route/combat state; accept movement, weapon and
  special inputs; resolve enemy action, shot, damage, kill, combo and
  experience; cross authored gates; in the stable read two duel inputs, draw
  order and shot; display apparent outcome; narration invalidates it; restore
  the path and corrected objective; second stable entry settles the episode.
- Claim IDs: `COJG-004`–`COJG-012`.

### Constraint Genes

- Existing `CON-262`: magazines and reserve ammunition are finite; existing
  `CON-285`: fire, switching and reload require a compatible weapon,
  ammunition and current action state.
- Existing `CON-270`: the earned point may enter only a currently eligible
  branch node; existing `CON-282`: authored objectives, gates, duel and
  correction occur in fixed episode order.
- Scarce strategic resources: health, loaded rounds, reserve ammunition,
  available weapon, combo continuation time, Concentration charge, safe cover,
  skill point, duel focus, hand speed and reaction window.
- Claim IDs: `COJG-003`–`COJG-011`.

### Information Genes

- Existing `INF-073`: active weapon and ammunition state are visible;
  `INF-115`: first-person sight exposes only local enemies and hazards;
  `INF-119`: health and survivability feedback are visible; `INF-125`: current
  objective and authored progress cue are inspectable.
- New `INF-276`: the combat/duel interface exposes combo continuation and
  multiplier, experience, Concentration readiness, opponent focus, draw-hand
  speed and the opponent's visible draw cue without guaranteeing the next hit.
- Claim IDs: `COJG-004`–`COJG-012`.

### Objective Genes

- New `OBJ-138`: complete `Once Upon a Time in Stinking Springs` by surviving
  its ordered Story route, resolving the apparent duel, accepting the forced
  correction and entering the stable again to settle the true episode outcome.
- Success, evaluation and failure: only the post-correction recognition and
  episode transition are positive. A combo, skill unlock, farmhouse clearance,
  stable arrival or apparent duel win is intermediate. Death/checkpoint restore
  and a lost duel fail only the current attempt.
- Claim IDs: `COJG-003`, `COJG-009`–`COJG-012`.

### Time Genes

- Existing `TIM-003`: traversal, enemy attacks, combo expiry, Concentration
  drain, duel preparation and shots advance under live time outside menus and
  authored transitions; Concentration changes scale but does not create a turn.
- Claim IDs: `COJG-004`–`COJG-012`.

## Reproducible transitions

| Before | Action | Deterministic or bounded resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Fresh profile, Story selected, Normal fixed | Start New Game and accept first dirt-path control | First episode route and initial equipment state become active | exact bounded entry | `COJG-001`–`COJG-003` |
| A reachable hostile is exposed and a compatible firearm is loaded | Aim and fire | Shot, hit region, damage and hostile reaction resolve while other actors continue | direct FPS kernel | `COJG-004` |
| Magazine is empty or tactically low with compatible reserve | Reload | Weapon becomes temporarily unavailable, then receives legal rounds | finite weapon cadence | `COJG-004` |
| One eligible kill has started a live combo window | Defeat another hostile before expiry | Combo count/multiplier advances and scales the experience award; expiry resets the chain | aggression changes progression rate | `COJG-005` |
| Experience crosses a threshold and a point is available | Open the tree and select an eligible node | Point is consumed and its declared combat modifier persists | bounded player-authored growth | `COJG-005` |
| Concentration is charged during active opposition | Activate it and continue aiming/firing | Surrounding action slows, targets become easier to read and meter drains until exit | temporary tempo control | `COJG-006` |
| Silas reaches the first stable scene | Keep reticle on Garrett while holding the hand near the revolver | Focus and speed rise or fall independently with maintained input | two-channel duel preparation | `COJG-007`, `COJG-008` |
| Garrett has not drawn | Draw early or keep waiting | Early draw remains possible but is classified differently; waiting preserves the ordinary honourable trace | reaction order is a player decision | `COJG-008` |
| Garrett visibly begins drawing and focus/speed are established | Draw, stabilise and fire | Speed determines access delay, focus shapes post-draw aim and the shot settles the apparent duel | preparation affects one live resolution window | `COJG-007`, `COJG-008` |
| Apparent duel victory has settled | Accept the authored narration transition | The game rejects that version, rewinds to the prior path and issues `Get the horses... this time for real` | narration causally replaces played state | `COJG-009`, `COJG-011` |
| Corrected objective is active on the restored path | Walk into the stable again | Garrett recognises Silas is not Billy; the episode ends and the next episode transition appears | reproducible positive terminal | `COJG-010` |
| Health reaches zero or the duel is lost | Choose ordinary retry | Transient damage, positions and combat return to an authored checkpoint | attempt rollback differs from narrator revision | `COJG-011` |

## Strategic and experiential structure

- Local decision: pick the suitable weapon and range, protect the combo timer,
  spend Concentration before exposure overwhelms health, and trade precision
  against speed during the duel.
- Medium-term planning: preserve ammunition and charge across successive
  ranch/farmhouse pressure points, then convert experience into a useful first
  skill without treating the chapter as an unbounded build exercise.
- Long-term structure: the episode teaches ordinary combat, progression and
  duel grammar, then makes its most important state change by declaring that
  the apparent duel was not the accepted account.
- Common heuristics: reload behind cover rather than during a live chain;
  extend a combo only while another safe target is reachable; activate
  Concentration before the sightline collapses; in the duel use small
  corrections and watch the opponent's hand while preserving both meters.
- Failure attribution: health/ammunition, hit and combo feedback, objective
  text, Concentration state, duel meters and visible draw cue explain most
  failures. The narrator correction is explicitly authored, not disguised as a
  player mistake or checkpoint rollback.
- Player-trust factors: the first duel result is intentionally revoked, but the
  new objective and restored approach disclose the replacement before the true
  terminal; no invisible alternate completion is inferred.

## Replay and variation

- What changes between attempts: aim, chosen weapons, pickup use, combo length,
  selected first skill, Concentration timing, health/ammunition, duel focus and
  speed, draw order and checkpoint use.
- Randomness or procedural generation: episode geometry, objectives, duel and
  correction are authored; local enemy positions and shot outcomes vary within
  the live simulation.
- Multiple viable strategies: revolver, rifle and shotgun emphasis, conservative
  cover play or aggressive combo chaining, different skill choice and
  honourable or early duel draw can reach the forced correction.
- Typical replay motive: cleaner combo/accuracy, another skill emphasis or a
  faster honourable duel; Arcade, Duel mode and later episodes are separate.

## Adjacent systems and history

- Direct predecessors and variants: earlier Call of Juarez games have related
  Western firearm/duel grammar but are separate products. The Switch port has
  motion control and HD rumble; neither is evidence for this Windows packet.
- Similar games: Mafia (2002) and Half-Life 2 share an authored checkpointed
  combat route; Red Dead Redemption 2 shares Western gunplay, character growth
  and slowed targeting; The Stanley Parable shares mechanically responsive
  narration.
- Important differences: Gunslinger turns rapid kills into local experience
  acceleration, suspends ordinary gunplay for a two-input draw test, and then
  compulsorily replaces already played scene state. The Stanley Parable reacts
  to the player's chosen route rather than correcting the narrator's own
  account; checkpoint reload restores failure rather than asserting a new truth.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-161`, `ACT-164`, `ACT-183`, `ACT-191`, `ACT-199`, `ACT-229`, `ACT-390` | movement, weapon handling, progression, Concentration and duel preparation |
| System Behaviour | `SYS-215`, `SYS-299`, `SYS-348`, `SYS-368`, `SYS-369`, `SYS-717`, `SYS-718`, `SYS-719` | combat, growth, health, special, retry, combo, duel and narrated replacement |
| Constraint | `CON-262`, `CON-270`, `CON-282`, `CON-285` | ammunition, skill, authored order and weapon legality |
| Information | `INF-073`, `INF-115`, `INF-119`, `INF-125`, `INF-276` | equipment, local threats, health, objective and combo/duel state |
| Objective | `OBJ-138` | settle the true first-episode outcome after correction |
| Time | `TIM-003` | live combat, combo and duel timing |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `221` (`GAME-0001`–`GAME-0221`).
- Exact genome matches: none.
- Tied near matches: `GAME-0212` — Half-Life 2 (`14 / 37 = 0.378378`).
- Supported combination subsets: `COMB-0220`.
- Scan date: 2026-09-02.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0212` — Half-Life 2 | `ACT-008`, `ACT-161`, `ACT-164`, `ACT-183`, `ACT-199`, `SYS-215`, `SYS-348`, `SYS-369`, `CON-262`, `CON-285`, `INF-073`, `INF-115`, `INF-119`, `TIM-003` | Both are authored checkpointed first-person combat chapters. Half-Life 2 centres physical prop pull/hold/launch and a pure location transition; Gunslinger instead joins combo-scaled growth, charged slowdown, a two-channel duel and compulsory narration-driven scene replacement before its episode terminal. | Near, `0.378378` |

### Preserved research notes

- New genes: `ACT-390`, `SYS-717`, `SYS-718`, `SYS-719`, `INF-276`, `OBJ-138`.
- Classification result: `New gene` and new verified interaction combination.
- Evidence and reasoning: existing movement, direct combat, equipment,
  character progression, special meter, checkpoint, authored order and
  information genes absorb the generic layer. No lower-ID record represents
  dual maintained focus/hand preparation, a duel result computed from it, or a
  non-player narrator invalidating and replacing already resolved scene state.

## Combination status

- `COMB-0220` is a strict subset coupling direct combat, Concentration, duel
  preparation/resolution, narrator replacement and the post-correction terminal.
- Every earlier verified combination is tested mechanically after registration;
  proper-subset results remain validation-controlled.

## Taxonomy impact

- Registry changes: six new Active genes, `COMB-0220`, family memberships and
  complete bilingual presentation.
- Taxonomy-change record: none; no earlier reviewed signature, lifecycle or
  stable definition changes.
- Candidate terms affected: kill-combo experience, duel focus/hand preparation,
  duel resolution, narrator-authored state replacement and true episode terminal.

## Negative results

- `ACT-044` is rejected: the player never controls or branches this rewind;
  narration compulsorily replaces the scene through `SYS-719`.
- `SYS-149` and `CON-168` are rejected: no route choice commits a narrator
  response; the same authored route is corrected after an apparent outcome.
- `SYS-479` is rejected: Concentration does not place and resolve Dead Eye
  target marks; generic charged slowdown remains `SYS-368`.
- Arcade scoring, Duel Challenge lives, Nuggets of Truth completion and later
  skill branches are real product modules but outside this single episode.

## Delta summary

## Нові факти

- [Confirmed/Observation | Direct/Corroborated | High] One current Windows
  Story episode binds ordinary score-aware shooting, Concentration, first duel,
  forced narration correction and an explicit second-stable terminal
  (`COJG-001`–`COJG-012`).

## Нові гени

- [Observation | Corroborated | High] Added `ACT-390`, `SYS-717`, `SYS-718`,
  `SYS-719`, `INF-276` and `OBJ-138` for duel preparation, combo growth, duel
  settlement, narrated state replacement, interface and exact terminal.

## Нові комбінації

- [Observation | Corroborated | High] Added `COMB-0220`, joining ordinary FPS
  pressure to a duel whose apparent result is mechanically replaced before
  true episode completion.

## Зміни таксономії

- Added one bounded Story episode and its new/reused evidence; no earlier
  reviewed signature, lifecycle or definition changed.

## Family classification

- `FAM-009` Tactical forecast and counterplay.
- `FAM-010` Real-time system pressure.
- `FAM-011` Time reversal and loop retention.
- `FAM-017` Ordered dependency sequencing.

## Plain-language interpretation

This episode first teaches a brisk Western shooter: move through the ranch,
choose a gun, protect ammunition, chain kills for more experience, spend a
skill point and slow danger with Concentration. At the stable, ordinary aiming
is replaced by two simultaneous preparations—keep attention on Garrett and the
draw hand near the revolver—before reacting to his move. Even a won duel is not
the ending. Silas's account is corrected, the game returns to the approach with
a new objective, and only the second stable entry settles what the episode
accepts as true.

## Ukrainian localisation review

- `verified`: title, exact product/mode/chapter/build identifiers, all gene and
  combination references, entry/terminal logic and source boundaries.
- `corrected`: natural Ukrainian wording for `серія швидких убивств`,
  `Концентрація`, `прицільна зосередженість`, `готовність руки до вихоплення`,
  `перемотування оповіді`, `сховище набоїв` and `повторний вхід до стайні`.
- `retained-with-reason`: official `Call of Juarez: Gunslinger`, Steam, Story,
  Normal, `Once Upon a Time in Stinking Springs`, `Get the horses... this time
  for real`, Concentration, Silas, Billy the Kid, Pat Garrett and Build ID
  `168269` remain exact product, UI, character or distribution identifiers.
- English-leak review: ordinary reader-facing prose is Ukrainian in the owner
  and presentation layers; retained Latin tokens are the exact names above,
  IDs, URLs and file/build identifiers only.

## Нові питання

- Can a later bounded game reuse narration-driven state replacement without
  also sharing direct FPS combat or a duel terminal?

## Наступна рекомендована гра

- [Confirmed | Direct | High] `GAME-0223` — Aion Classic.
- Optimisation criterion: move from a bounded narrated single-player episode to
  a current persistent MMORPG ascension packet.
- Expected information gain: faction/class progression and retained flight or
  ascension boundaries without importing a complete live service.
- Backlog impact: continue the fixed `SEARCH_DEMAND_GAME_SELECTION_010` order.

## Чому саме вона

- [Hypothesis | Limited | High] Aion Classic should reduce direct overlap with
  the current FPS corridor while testing the third deliberately separated MMO
  subject in the maintainer's horizon.
