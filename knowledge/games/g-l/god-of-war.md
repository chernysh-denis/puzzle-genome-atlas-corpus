---
game_id: GAME-0263
slug: god-of-war
game_title: God of War
analysis_status: reviewed
reviewed: 2026-09-05
combination_ids:
  - COMB-0261
gene_ids:
  action:
    - ACT-008
    - ACT-161
    - ACT-197
    - ACT-223
    - ACT-385
    - ACT-419
    - ACT-437
  system:
    - SYS-215
    - SYS-369
    - SYS-407
    - SYS-409
    - SYS-578
    - SYS-780
    - SYS-800
  constraint:
    - CON-269
    - CON-282
    - CON-324
    - CON-605
  information:
    - INF-119
    - INF-125
    - INF-142
    - INF-295
    - INF-319
  objective:
    - OBJ-155
  time:
    - TIM-003
---

# Game: God of War

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Parameters describe
gene instances but do not enter the signature.

## Analysis scope

- Version / ruleset: current unmodified English Windows Steam application
  `1593500`, sole one-app package `564166`, publisher PC `Patch v1.0.13`
  announced 2023-05-22, observed against public branch build `11168363` whose
  branch record was last updated on the same date; checked 2026-09-05. The
  semantic patch version is the publisher's own dated claim; the numeric build
  identifier is a secondary distribution observation and is never treated as a
  publisher statement.
- Product boundary: this is **God of War** (2018) on Windows, not God of War
  Ragnarök, the pre-2018 Greek-era titles, a console release or a franchise
  union. Valve's record reports no DLC app and a single package, so no
  purchased content can enter or leave this packet.
- Platform, input and difficulty: English interface and subtitles, Windows,
  keyboard and mouse, fresh single-player `New Game` on the declared default
  story difficulty. Controller input, consoles, New Game Plus, the alternative
  pre-set difficulty levels named by PlayStation's accessibility guidance and
  every accessibility-altered ruleset are separate packets.
- Setup-only predecessor: the mandatory opening sequence that precedes the
  first named objective establishes a clean story save but contributes no genes
  or transitions to this packet.
- Entry: accept first ordinary Kratos control under the first named objective
  of chapter `The Marked Trees`. Record health, the axe's in-hand state and the
  companion's current arrow availability before the first strike or throw.
- Primary decision loop: read the current objective marker and the local route;
  advance Kratos through the authored chapter geometry; strike reachable
  hostiles with the Leviathan Axe or, while it is away, with fists and the
  Guardian Shield; aim and throw the axe at a target or obstacle, leave it where
  it stopped, and recall it so its return line resolves a second time; hold the
  Guardian Shield toward the current facing to absorb eligible attacks; read
  each incoming attack's cue to decide whether a timed parry or an evasive
  response is the legal answer; command the companion to loose arrows while his
  stock permits; build a hostile's stability state until its finisher
  opportunity is exposed and commit the prompted close finish; and on death
  accept the restored authored checkpoint.
- Positive terminal: defeat the chapter's mandatory guardian `Dauði Kaupmaðr`
  and accept the objective advance to `Return to the house`. At first ordinary
  control under that successor objective, create a manual save, quit to the
  main menu, load that save and verify the same successor objective and
  retained state. Stop before the `Defeat the Stranger` objective.
- Negative terminal: health reaching zero ends the current attempt; a chosen
  retry restores the latest authored checkpoint and replaces the failed
  attempt's transient position, health, hostile and encounter state. Reaching
  the guardian, staggering it or seeing the objective text without the stated
  manual save and reload check is not success.
- Included: direct third-person traversal of the authored chapter; axe and
  bare-handed strikes; the aimed throw, the embedded rest position and the
  damaging recall; the held Guardian Shield; the timed defensive response
  chosen from the attack's cue category; the commanded companion arrow ability
  and its finite readiness; the autonomous companion's own movement and
  support; the stability state that exposes a prompted close finisher and that
  finisher itself; the continuous health pool; authored checkpoint restoration;
  the ordered objective gates; the objective marker; attack timing cues; and
  the retained successor-objective settlement.
- Excluded: the `Defeat the Stranger` objective and everything after it; every
  later chapter, realm and region; experience, skill trees and every unlocked
  shield or axe skill including the named counter skills, so only the base
  block and parry are in scope; runic attacks, enchantments, pommels, talismans
  and armour; Hacksilver, shops, crafting and upgrades; the Blades of Chaos;
  Spartan Rage, which is excluded as a recorded evidence gap rather than a
  claim of absence, because the available sources establish that the Rage Meter
  accumulates in bare-handed combat but do not establish its expenditure inside
  the declared route; collectibles, favours, chests, artefacts and exploration
  outside the objective route; New Game Plus; all difficulties, inputs and
  platforms not declared above; screenshots, official artwork, third-party
  assets, video and audio evidence.
- Reproducible parameterisation: install English app `1593500` from package
  `564166`, confirm the current PC patch, start a clean single-player `New
  Game` on the declared default story difficulty and retain default keyboard
  and mouse bindings. From first ordinary control under the first named
  objective, follow only the required objective chain; throw the axe at least
  once at a route obstacle and once at a hostile, recall it across at least one
  intervening body, fight at least one encounter while the axe is away, hold
  the shield against at least one eligible attack, commit at least one timed
  response to each cue category, command at least one companion arrow, complete
  at least one prompted close finisher, and defeat `Dauði Kaupmaðr`. Then
  perform the stated manual save and reload terminal. Exact health values,
  arrow counts, hostile positions, throw lines and encounter duration are
  parameters.
- Potential scoped modules: one later named chapter; the Blades of Chaos
  packet; the skill, runic and upgrade economy; a Spartan Rage ruleset; a
  higher difficulty; New Game Plus; or another platform requires its own
  version, entry, loop, terminal and evidence.
- Direct-play status: not conducted. Valve application and package data plus
  PlayStation's own product page establish lawful availability, exact product
  identity, Windows support, the single-player category, adjustable difficulty,
  keyboard-only support, save-anytime support and the separation of New Game
  Plus from a first playthrough. Santa Monica Studio's own dated Steam
  announcement supplies the current PC patch version. The public SteamCMD info
  projection supplies one dated secondary build observation. Independent static
  written references corroborate the chapter's ordered objectives, the starting
  availability of both the Leviathan Axe and the Guardian Shield, the aimed
  throw and recall inputs, bare-handed combat while the axe is away, the
  companion arrow command, the stability state and its prompted finish, the
  cue colours that separate parryable from unblockable attacks, and the
  guardian encounter. This is an evidence-backed rules reconstruction, not a
  claimed playthrough or entitlement. No video or audio was opened, played,
  heard, analysed or used.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `GOW-001` | Steam app `1593500` and its sole one-app package `564166` identify the currently lawfully offered English Windows product, which has no DLC app | Confirmed | Direct | High | P1, P2 |
| `GOW-002` | The publisher's current PC version is `Patch v1.0.13`, announced 2023-05-22 as a credits-only change, and the public branch record was last updated on the same date | Confirmed | Corroborated | High | P3, S1 |
| `GOW-003` | The product is single-player, offers adjustable difficulty, a keyboard-only option and save-anytime support, and unlocks New Game Plus only after the story campaign is completed | Confirmed | Corroborated | High | P1, P2 |
| `GOW-004` | `The Marked Trees` is the first of seventeen campaign chapters and is followed by `Path to the Mountain` | Observation | Corroborated | High | S2 |
| `GOW-005` | Its named objectives run in the order `Follow the river downstream`, `Hunt with Atreus`, `Defeat Dauði Kaupmaðr`, `Return to the house`, `Defeat the Stranger`, `Return to the house` | Observation | Corroborated | High | S3, S4 |
| `GOW-006` | Both the Leviathan Axe and the Guardian Shield are starting equipment available within `The Marked Trees` | Observation | Corroborated | High | S5, S6 |
| `GOW-007` | The axe is aimed and thrown with a declared input and recalled with a separate declared input | Observation | Corroborated | High | S3, S6 |
| `GOW-008` | A thrown axe damages bodies on its outbound line, remains where it stopped, and damages again along its return line when recalled | Observation | Corroborated | High | S7 |
| `GOW-009` | While the axe is away the character fights with fists, legs and shield instead, and that substituted set builds a hostile's stability state faster | Observation | Corroborated | High | S7, S8 |
| `GOW-010` | The shield is held to block and, pressed at the last moment, parries; only attacks marked by the parryable cue can be parried, while attacks marked by the unblockable cue must be evaded | Observation | Corroborated | High | S6, S8, S9 |
| `GOW-011` | The base block does not draw on any depleting guard, stamina or durability reserve; the named counter follow-ups are separate unlockable skills outside this packet | Observation | Corroborated | Medium | S6, S9 |
| `GOW-012` | The companion fires arrows on a declared player command while its availability permits, and otherwise acts autonomously beside direct control | Observation | Corroborated | High | S3, S8 |
| `GOW-013` | Accumulating a hostile's stability state exposes a prompted close finish that the player commits with a declared input | Observation | Corroborated | High | S3, S8 |
| `GOW-014` | `Dauði Kaupmaðr` is the chapter's first mandatory guardian and its defeat advances the objective to `Return to the house` | Observation | Corroborated | High | S3, S4 |
| `GOW-015` | The product's save-anytime support lets that successor-objective state be retained and restored, making it a reproducible positive terminal | Confirmed | Corroborated | High | P1, P2 |
| `GOW-016` | The bounded identity is a recallable thrown tool whose absence rewrites the close-combat vocabulary, read against cue-typed defensive responses and supported by a commandable autonomous companion | Strong Pattern | Corroborated | High | `GOW-004`–`GOW-015` |

## Basic data

- Release / origin: Santa Monica Studio and Jetpack Interactive; published on
  Windows by PlayStation Publishing LLC on 2022-01-14.
- Platform or physical form: lawfully offered English Windows single-player
  Steam application `1593500`; one fresh opening `The Marked Trees` packet.
- Puzzle family: tactical forecast and counterplay; real-time system pressure;
  ordered dependency sequencing.
- Primary and official sources, accessed 2026-09-05:
  - **[P1]** [Valve application data](https://store.steampowered.com/api/appdetails?appids=1593500&cc=ua&l=english),
    for the exact title, app, Windows support, developers, publisher, release
    date, single-player category, `Adjustable Difficulty`, `Keyboard Only
    Option`, `Save Anytime`, the absence of any DLC app, the sole package and
    the current Ukraine offer.
  - **[P2]** [PlayStation's official God of War page](https://www.playstation.com/en-us/games/god-of-war/),
    which states that "once you complete the story campaign of God of War on
    any difficulty, you unlock New Game+" and that an alternative pre-set
    difficulty level may be chosen to reduce the overall challenge, and which
    separates this title from God of War Ragnarök. Embedded media was not
    opened or used.
  - **[P3]** [Santa Monica Studio's own `Patch v01.0.13` announcement](https://store.steampowered.com/news/app/1593500),
    dated 2023-05-22, stating that "Patch v1.0.13 for God of War is now live"
    and that it updated game credits only.
- Corroborating textual sources, accessed 2026-09-05:
  - **[S1]** [public SteamCMD info projection](https://api.steamcmd.net/v1/info/1593500),
    for public branch build `11168363` and its branch timestamps. This mirrors
    Valve's public product data and is treated as a secondary distribution
    observation, not a publisher claim.
  - **[S2]** [static campaign-chapter index](https://www.shacknews.com/article/104435/guide-collectibles-and-walkthrough-god-of-war),
    for the seventeen ordered campaign chapters, `The Marked Trees` as the
    first and `Path to the Mountain` as its successor.
  - **[S3]** [static `The Marked Trees` route](https://www.powerpyx.com/god-of-war-the-marked-trees-walkthrough/),
    for the chapter's ordered named objectives, the aimed axe throw used
    against a route obstacle, the guardian's attack pattern, the accumulated
    stability state and its prompted close finish, and the companion arrow
    command.
  - **[S4]** [independent static `The Marked Trees` objective list](https://gamefaqs.gamespot.com/ps4/191627-god-of-war/faqs/75829/the-marked-trees),
    for the same ordered objectives, the absence of a time limit during the
    hunt and the guardian encounter. Images and embedded media were not opened
    or used.
  - **[S5]** [static Guardian Shield reference](https://game8.co/games/God-of-War-2018/archives/316333),
    for the shield being starting equipment available in `The Marked Trees`,
    the last-second block that produces a parry, and the named counter
    follow-ups being separately unlocked skills.
  - **[S6]** [static Leviathan Axe reference](https://game8.co/games/God-of-War-2018/archives/316372),
    for the axe being starting equipment available in `The Marked Trees`, the
    aimed throw input and the separate recall input.
  - **[S7]** [static combat-technique reference](https://game8.co/games/God-of-War-2018/archives/317558),
    for the light and heavy throw, the recall that hits the target again on its
    way back, leaving the axe embedded while fighting bare-handed, the shield's
    block and parry function, the companion arrow command and the faster
    stability accumulation of bare-handed combat.
  - **[S8]** [static combat overview](https://game8.co/games/God-of-War-2018/archives/316322),
    for the shield as starting equipment and its role in the substituted
    bare-handed set.
  - **[S9]** [static parry reference](https://gamerant.com/god-of-war-how-to-parry/),
    for the shield input used for both blocking and parrying, the requirement
    that the parry land at the last possible moment, and the cue distinction in
    which only the parryable-marked attacks can be parried while
    unblockable-marked attacks must be evaded.
- Reproducible control: **[V1]** repository-side transition trace across
  `P1`–`P3` and `S1`–`S9` under the declared app, package, patch, platform,
  input, difficulty, clean setup, exclusions and retained terminal; rules
  reasoning, not direct play.
- Claim IDs: `GOW-001`–`GOW-016`. No audiovisual evidence was used.

## Mechanical decomposition

### Action Genes

- Existing `ACT-008`: advance the controlled protagonist through the authored
  chapter geometry; `ACT-161`: aim and commit a direct strike with the axe or,
  while it is away, with fists and shield.
- Existing `ACT-385`: aim and throw the reusable hand tool at a reachable
  target, and command the deployed tool to return to hand. The boundary already
  covered a reversible throw-and-recall of one named reusable tool; only its
  wording was product-specific, so it was generalised rather than duplicated.
- Existing `ACT-437`: hold the Guardian Shield toward the current facing and
  release it. `ACT-383` is still rejected because it requires a depleting guard
  meter that can break into an exposed state, `ACT-349` because it requires a
  chosen incoming direction and `ACT-425` because it requires a
  durability-bearing close weapon. That this guard costs no reserve is a
  parameter of `ACT-437` rather than a separate Action, which
  [`TAXONOMY_CHANGE_020`](../../../research/taxonomy-changes/TAXONOMY_CHANGE_020.md)
  established.
- Existing `ACT-223`: commit the currently eligible timed defensive response
  inside a telegraphed attack; `ACT-197`: invoke the companion's declared
  arrow ability while its availability permits; `ACT-419`: commit the prompted
  close finisher while a hostile's stability opportunity remains active.
- Actor, chapter, objective, weapon, companion and exact quantity names remain
  parameters. Claims: `GOW-004`–`GOW-014`.

### System Behaviour Genes

- Existing `SYS-215`: directly controlled combatants exchange range-, cadence-,
  damage- and defeat-dependent effects in real time; `SYS-578`: strikes reduce
  one continuous health pool and zero ends the current attempt; `SYS-369`: a
  chosen retry restores the latest authored checkpoint rather than the failed
  transient state.
- Existing `SYS-407`: the persistent allied companion follows and independently
  selects legal movement, attack or support actions; `SYS-409`: qualifying
  attacks move a hostile's stability state across its threshold and expose a
  critical window; `SYS-780`: the final required interaction of the bounded
  segment closes its objective set and admits retained successor control.
- Existing `SYS-800`: the thrown tool resolves against everything on its
  outbound line, rests where it stopped and resolves a second pass along the
  return line when recalled. No existing system gene modelled a projectile that
  is resolved twice along two player-chosen lines and remains recoverable.
- Resolution order: movement changes reach and throw lines; a strike, throw or
  recall resolves against the bodies on its current line; the tool's away state
  substitutes the close action set; a held guard or a timed response is
  evaluated against the incoming attack's category and window; accumulated
  stability crosses its threshold and exposes the finisher; the companion
  resolves its commanded arrow and its own autonomous behaviour; zero health
  restores a checkpoint; and the guardian's defeat closes the objective into a
  retainable successor. Claims: `GOW-007`–`GOW-016`.

### Constraint Genes

- Existing `CON-605`: while the tool is away, its attacks and throws are
  unavailable and the substituted close set applies. This is new because
  `CON-285` governs ammunition and magazine compatibility for a retained
  weapon, not the disappearance of the weapon itself.
- Existing `CON-324`: a timed defensive response negates an incoming attack
  only inside that attack's matching real-time window; `CON-269`: the
  companion's arrow ability resolves only when its target, range and current
  availability permit; `CON-282`: each required objective advances only after
  its authored predecessor is satisfied.
- Scarce resources: health, the axe's presence in hand, the companion's current
  arrow availability, the live parry and evasion windows, the temporary
  finisher opportunity and checkpoint-local progress. Exact values are
  parameters. Claims: `GOW-007`–`GOW-015`.

### Information Genes

- Existing `INF-119`: current health and personal combat state remain visible;
  `INF-125`: the current objective and its marker expose the next authored
  gate; `INF-142`: attack motion, sound and prompt elements disclose enough of
  an executing attack's rhythm to time a response; `INF-295`: local feedback
  distinguishes a hostile's temporary finisher-eligible state from ordinary
  damage.
- Existing `INF-319`: the cue attached to an incoming attack sorts it into
  categories that differ in which defensive response can succeed. This is new
  because `INF-142` discloses timing and `INF-310` discloses which hostile is
  attacking, while neither selects the response type.
- Exact cue colours, ring geometry, prompts, bindings and interface positions
  are presentation parameters. Claims: `GOW-010`–`GOW-014`.

### Objective Genes

- Existing `OBJ-155`: survive and satisfy the ordered mandatory interactions of
  the bounded authored segment, accept its explicit completion and save
  boundary and retain ordinary control in the immediate successor objective.
- Staggering the guardian, watching the objective text change or reaching the
  house without the stated manual save and reload check is not success.
  Claims: `GOW-014`–`GOW-016`.

### Time Genes

- Existing `TIM-003`: movement, strikes, throws, recall flight, guard, parry
  windows, companion behaviour and the finisher all advance in real time while
  inputs remain accepted.
- Claims: `GOW-007`–`GOW-015`.

## Reproducible transitions

| Before | Action | Deterministic or bounded resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| A clean New Game has completed only the setup opening | Accept first ordinary control under the chapter's first named objective | The chapter begins with starting equipment and no imported New Game Plus state | fixed clean entry | `GOW-003`, `GOW-006` |
| The axe is in hand and a target or obstacle is in line | Aim and throw | The axe resolves against the bodies on its outbound line and remains where it stopped | outbound resolution and rest state | `GOW-007`, `GOW-008` |
| The axe rests away from the character with a body between them | Recall it | The axe resolves a second time along the return line before arriving in hand | player-chosen second line | `GOW-008` |
| The axe is away and a hostile is in reach | Attack | The substituted fists-and-shield set applies and accumulates the hostile's stability state faster than the axe would | tool-absence vocabulary change | `GOW-009` |
| An incoming attack carries the parryable cue | Press the guard at the last moment | The attack is parried and the hostile is opened rather than merely absorbed | cue-typed timed response | `GOW-010` |
| An incoming attack carries the unblockable cue | Hold the guard | The guard does not answer that category, so an evasive response is the legal one | response-type disclosure | `GOW-010`, `GOW-011` |
| No attack is incoming and the guard is held | Continue holding, then release | The posture persists and ends on release without consuming any reserve | reserve-free guard | `GOW-011` |
| The companion is present and its arrows are available | Commit the arrow command | The companion looses arrows at the current target while availability permits, then declines until it recovers | commanded companion ability | `GOW-012` |
| The companion is present and no command is given | Continue fighting | The companion still moves, assists and acts on its own against local state | autonomous companion behaviour | `GOW-012` |
| A hostile's stability state crosses its threshold | Approach and commit the prompted finish | The exposed contextual finisher resolves instead of an ordinary strike, and the opportunity expires if unused | stability-gated finisher | `GOW-013` |
| Health reaches zero before the guardian falls | Retry | The latest authored checkpoint replaces the failed attempt's position, health and encounter state | reproducible negative recovery | `GOW-015` |
| The guardian's health is exhausted | Complete its defeat | The objective closes and advances to the named successor objective | guardian-gated objective advance | `GOW-014` |
| First ordinary control under the successor objective is available | Create a manual save, quit and load it | The same successor objective and unadvanced route return | reproducible positive terminal | `GOW-015`, `GOW-016` |

## Strategic and experiential structure

- Planning horizon: the objective marker exposes the next authored gate, while
  health, the axe's location, the companion's arrow availability and each
  hostile's stability state determine whether to throw, recall, close, guard,
  parry or command.
- Local tactics: throw through a line of bodies rather than at one, reposition
  before recalling so the return line also connects, use the bare-handed set
  deliberately to accelerate stability rather than as a penalty for having
  thrown, read the cue category before choosing a response, and spend the
  companion's arrows on the hostile nearest its threshold.
- Medium-term structure: the chapter introduces traversal, then the throw, then
  the recall as an offensive line, then the substituted close set, then cue
  reading, and finally couples all of them against one mandatory guardian.
- Reversible versus irreversible: movement, guard, lock of attention and the
  axe's position are reversible within seconds; the companion's arrow
  availability and health are spent until they recover; the guardian's defeat
  and the objective advance persist; a checkpoint load replaces failure.
- Failure attribution: visible health, the axe's location, the arrow
  availability, the attack cue and the stability feedback make a loss traceable
  to a specific wrong response category, a throw made at the wrong moment or a
  finisher opportunity allowed to expire.
- Player trust: the cue states which response is legal before contact, the
  recalled axe follows the line the player chose by standing where they stand,
  the finisher opportunity is announced rather than guessed, and the loaded
  save reproduces the settled state exactly.

## Replay and variation

- What changes: throw and recall lines, how long the axe is left away, which
  responses answer which cues, arrow timing, which hostiles are finished and
  how many checkpoint restores occur.
- Randomness or procedural generation: chapter geometry, objectives, hostile
  placement and the guardian are authored. Minor attack selection varies; no
  procedural-generation claim enters this packet.
- Multiple strategies: encounters admit axe-ranged pressure, deliberate
  bare-handed stability building, parry-led openings or companion-assisted
  attrition. The control demonstrates one of each rather than making a
  no-damage or no-checkpoint route the terminal.
- Typical replay motive: keep the axe working on both lines, answer more cues
  correctly and reach the guardian without a checkpoint restore.

## Adjacent systems and history

- DOOM (2016) shares direct real-time combat, authored gates, a continuous
  health pool, checkpoint recovery, a visible objective and an exposed
  finisher opportunity. Its finisher is fed by health-and-resource economy and
  its weapons never leave the player's hands; this packet makes the weapon's
  absence a decision and types the defensive response by cue.
- DARK SOULS III shares real-time melee, a held guard, an authored gate and a
  mandatory guardian, but prices offence and defence from one shared reserve
  and answers attacks by roll or guard rather than by reading a response
  category off the attack itself.
- STAR WARS Jedi: Fallen Order shares a held guard and authored traversal, but
  its guard depletes a finite stability meter and its companion is not
  commanded to attack.
- Resident Evil 4 (2023 remake) shares a timed defensive response, a stagger
  state and a prompted close follow-up, but spends weapon durability on its
  parry and has no recallable thrown weapon.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-161`, `ACT-197`, `ACT-223`, `ACT-385`, `ACT-419`, `ACT-437` | chapter, objective, weapon, companion and actor names are parameters |
| System Behaviour | `SYS-215`, `SYS-369`, `SYS-407`, `SYS-409`, `SYS-578`, `SYS-780`, `SYS-800` | damage values, stability thresholds and travel speeds are parameters |
| Constraint | `CON-269`, `CON-282`, `CON-324`, `CON-605` | windows, availability counts and gate order are parameters |
| Information | `INF-119`, `INF-125`, `INF-142`, `INF-295`, `INF-319` | cue colours, prompts and interface layout are parameters |
| Objective | `OBJ-155` | objective names and retained state are parameters |
| Time | `TIM-003` | animation, flight and window timing are implementation |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `262` (`GAME-0001`–`GAME-0262`).
- Exact genome matches: none.
- Tied near matches: `GAME-0245` — DOOM (2016) (`11 / 37 = 0.297297`).
- Supported combination subsets: `COMB-0261`.
- Scan date: 2026-09-05.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0245` — DOOM (2016) | `ACT-008`, `ACT-161`, `ACT-419`, `SYS-215`, `SYS-369`, `SYS-578`, `CON-282`, `INF-119`, `INF-125`, `INF-295`, `TIM-003` | Both advance an authored route through directly commanded real-time combat, restore an authored checkpoint on death, expose the next gate and commit a prompted close finisher against a hostile that local feedback marks as eligible. DOOM keeps every weapon permanently in hand and feeds its finisher into an ammunition-and-health economy with a movement-first arena loop. This packet instead lets the primary weapon leave the character entirely, resolves that weapon twice along two player-chosen lines, substitutes a different close vocabulary while it is away, sorts incoming attacks into cue categories that select the legal defensive response, and adds a commandable autonomous companion. | Near, `0.297297` |

### Preserved research notes

- New genes: `SYS-800`, `CON-605`, `INF-319`. `ACT-439` was merged into
  `ACT-437` by
  [`TAXONOMY_CHANGE_020`](../../../research/taxonomy-changes/TAXONOMY_CHANGE_020.md),
  so the held guard is a reused Action here.
- Reused genes: the remaining 21 admitted genes in the Normalised genome.
- Classification result: `New gene`.
- Lower-ID scan: reuse the generalised `ACT-385` for the throw and recall
  rather than creating an axe-named gene; reuse `ACT-223` with `CON-324` for
  the timed response and add `INF-319` only for the category disclosure neither
  covers; reuse `SYS-409` with `INF-295` and `ACT-419` for the stability
  threshold and its prompted finish; reuse `ACT-197` with `SYS-407` and
  `CON-269` for the commanded and autonomous halves of the companion. Reject a
  companion-, chapter-, guardian-, weapon- or realm-named gene; reject a
  Spartan Rage gene because its expenditure is not evidenced inside this route;
  reject a skill-tree or upgrade gene because both lie outside the packet.

## Taxonomy impact

- Registry changes: add `SYS-800`, `CON-605`, `INF-319` and `COMB-0261`, plus
  independent evidence for 22 reused genes including the generalised
  `ACT-437`. Generalise only
  the wording of `ACT-385` from a product-specific nail label to the same
  portable reusable-hand-tool boundary; its definition semantics, lifecycle and
  all earlier signatures remain unchanged.
- Registry changes recorded by `BATCH_015_GENE_AUDIT_001` finding `A-01`:
  `ACT-197` keeps its boundary and both signatures, gains this record as
  `Additional support`, and has `active field ability` generalised to `active
  ability`. The word `field` described only where Palworld's Partner Skills are
  used, not what the transition is; the commanded companion arrow here is the
  same declared active companion ability under direct player invocation. Its
  lifecycle and the `GAME-0139` signature are unchanged, so this is a wording
  generalisation of the kind already recorded above for `ACT-385`.
- Taxonomy-change record: none; no split, merge, deprecation, lifecycle change
  or signature change. The `A-01` correction is likewise a wording and evidence
  change with no lifecycle or signature effect, so it needs no numbered record
  under the same convention.
- Candidate terms: recorded in `CANDIDATE_TERMS.md`; all product, chapter,
  objective, actor, weapon, app, package and patch names remain parameters.

## Negative results

- No video or audio evidence was used; only official static text and data plus
  static written references support this packet.
- Spartan Rage is excluded as a bounded evidence gap. The sources establish
  that the Rage Meter accumulates during bare-handed combat inside this packet
  but do not establish that it can be spent within the declared route. This is
  a recorded uncertainty, not a claim that the product lacks the mechanic, and
  it is the single open question this unit hands to the batch audit.
- The named shield counter follow-ups are separately unlocked skills, so only
  the base block and parry are admitted; no skill, runic, upgrade or shop gene
  enters the packet.
- The `Defeat the Stranger` objective, every later chapter and realm, and the
  Blades of Chaos are excluded even though the product exposes them elsewhere.
- Advancing the objective text without the manual save and reload retention
  test is not the terminal.

## Delta summary

## New facts

- [Confirmed/Observation | Direct/Corroborated | High] `GOW-001`–`GOW-016`: one
  bounded opening chapter makes the primary weapon's absence a decision,
  resolves its recall along a second player-chosen line, and types every
  defensive answer by the incoming attack's cue.

## New genes

- [Observation | Corroborated | High] `SYS-800`, `CON-605`, `INF-319` — the
  two-pass thrown-tool resolution,
  the close vocabulary that depends on the tool being in hand, and the cue that
  selects which defensive response is legal.

## New combinations

- [Strong Pattern | Corroborated | High] `COMB-0261` — a recallable thrown tool
  whose absence rewrites close combat, answered against cue-typed defensive
  responses with a commandable autonomous companion.

## Taxonomy changes

- [Observation | Direct/Corroborated | High] `ACT-385` receives a
  boundary-preserving portable label and wording generalisation; no prior
  signature or lifecycle changes.

## New questions

- Can the excluded Spartan Rage expenditure be evidenced inside this exact
  route from official or reproducible sources, and would admitting it change
  the signature?

## Next recommended game

- [Hypothesis | Limited | High] `GAME-0264` — Disco Elysium - The Final Cut.
- Optimisation criterion: leave the real-time combat corridor entirely and test
  whether a probabilistic check applied to a conversational option needs new
  objective and information boundaries.
- Expected information gain: the first corpus packet whose primary resolution
  mechanism is a dialogue attribute check rather than a physical exchange.
- Backlog impact: advances the recorded 261-to-270 horizon by one unit.

## Why this game

- [Hypothesis | Limited | High] The selection retained this reserve for the
  throw-and-recall weapon state coupled to a commanded companion, which no
  reviewed record carried as one loop. The completed scan confirms the
  distance: the nearest signature shares only an eleven-gene
  authored-combat-and-finisher backbone.
