---
game_id: GAME-0283
slug: tekken-8
game_title: TEKKEN 8
analysis_status: reviewed
reviewed: 2026-09-10
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-202
    - ACT-294
    - ACT-295
    - ACT-296
    - ACT-297
  system:
    - SYS-215
    - SYS-522
    - SYS-832
    - SYS-836
    - SYS-837
    - SYS-838
  constraint:
    - CON-442
    - CON-446
    - CON-625
  information:
    - INF-142
    - INF-209
    - INF-210
  objective:
    - OBJ-099
  time:
    - TIM-003
---

# Game: TEKKEN 8

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Parameters describe
gene instances but do not enter the signature.

## Analysis scope

- Version / ruleset: current unmodified English Windows Steam application
  `1778820`, base package `912716` (containing only that application),
  default public branch Build ID `24827309` (published 2026-08-19 22:00 UTC
  by the secondary distribution projection, `T8-002a`), which Bandai Namco's
  own patch notes label `Ver.3.02.01`, applied 2026-08-19 15:00 PDT /
  2026-08-20 00:00 CEST (`T8-002b`); that the two describe the same build
  rests on their coincident timestamps alone (`T8-002c`); checked
  2026-09-09. Offline > Versus, one human P1 against one CPU participant,
  base-roster Jin Kazama for P1 and base-roster Kazuya Mishima for the CPU,
  Arcade Style controls for P1, the CPU at whatever level the mode offers by
  default (a parameter), the stage Arena (a base-product stage, `T8-006b`),
  and the shipped default
  match rules, under which the match is won by the first side to win three
  rounds and each round is limited to 60 seconds (`T8-007b`, an inference
  from the publisher's tournament rules that name the default settings and
  list those values; no official page or manual states the defaults
  directly).
- Product boundary: the 2024 Bandai Namco game on its base package only.
  The Advanced, Season 2 Deluxe and Season 2 Ultimate packages, the
  twenty-four downloadable-content applications (playable characters Eddy
  Gordo through Bob, the PAC-MAN and other added stages, Season and Year
  passes, cosmetic packs and the Fight Pass) are excluded. Bob, added by
  `Ver.3.02.01`, is a purchasable DLC fighter and is not a base-roster
  parameter; Jin Kazama and Kazuya Mishima are launch characters
  (`T8-004`).
- Primary decision loop: read both fighters' distance, pose, facing, health
  bars with their recoverable gauges, Heat gauges, Rage indication, round
  markers and the round clock; walk, backdash, dash, crouch, jump, sidestep
  or sidewalk to a distance and axis of your choosing; enter limb-button
  attacks, strings, while-standing or crouching commands, launchers and
  Heat Engagers, hold standing or crouching guard against the incoming hit
  level, attempt a throw or break one, and commit Heat Burst, Heat Smash,
  Heat Dash or a Rage Art when their state permits; let real-time contact
  resolve hit, counter hit, block, whiff, armour, launch, juggle, wall and
  knockdown state, permanent and recoverable damage and the Heat and Rage
  states; repeat until a round settles by KO or time and the third round
  win settles the match.
- Entry: the confirmation that launches the declared match after Jin
  (P1), Kazuya (CPU), Arcade Style for P1 and Arena are selected; the packet
  begins at first control in round 1 with both health bars full, no Heat
  used, no Rage active and the 60-second clock running.
- Positive terminal: the match-result state that appears after P1 records
  the third round win by KO or by holding more health when the clock
  reaches zero. This is a finite settlement under ADR-007; no save,
  reload, reward or progression is claimed, and the rematch or menu choices
  offered after the result are outside the packet (`T8-020`).
- Negative terminal: the same result state after the CPU records its third
  round win. There is no in-match retry; a round lost is only a marker
  against P1 until the match settles.
- Included: walking, backdash, dash, crouch, jump, sidestep and sidewalk
  with automatic facing realignment; limb-button attacks, strings,
  while-standing and crouching commands, launchers, Heat Engagers and the
  two fighters' throws; standing and crouching guard against high, mid and
  low hit levels; throw breaks; counter hit, punish, launch, airborne
  juggle, Tornado and wall splat on Arena's walls as contact-state
  parameters; the knockdown state, the tech roll, side roll, quickstand
  and back get-up commands that move or raise the downed fighter with
  their exact inputs, the get-up kicks, and staying down as the state's
  no-input branch; Power Crush armour; permanent and
  recoverable health with chip during Heat; the Heat state with Heat Burst,
  Heat Engagers, Heat Smash, Heat Dash, its timer and its once-per-round
  limit; Rage and the Rage Art; the health, recoverable-gauge, Heat, Rage,
  round-marker and clock display and the attack notices; KO, time-over
  comparison, round reset and first-to-three settlement; real-time
  simultaneous input.
- Excluded: online play, Ranked Match, Quick Match, Player Match, the
  TEKKEN Fight Lounge, Arcade Quest, Story, Character Episodes, Super
  Ghost Battle, Practice, Tekken Ball, Arcade Battle, tournaments and
  Tekken World Tour rules beyond their statement of the default settings,
  every DLC fighter and stage, the Fight Pass, cosmetics and customisation,
  replays, account progression and player ranks, the Special Style control
  layout, custom round or time settings, every stage other than Arena and
  therefore every wall break, hard wall break, floor break, floor blast,
  balcony break, wall bound and stage transition, the roster beyond the two
  chosen fighters, exact frame data and damage tables as separate claims,
  Ki Charge, the draw and double-KO rules (excluded for insufficient
  evidence, `T8-008b`), and everything after the result state.
- Reproducible parameterisation: install application `1778820` from
  package `912716` on the default public branch; open Offline > Versus,
  select Jin Kazama for P1 and Kazuya Mishima for the CPU side, leave P1 on
  Arcade Style, leave the round count and time limit at their shipped
  defaults, select Arena and confirm. Fight the match with any legal
  movement, attack, guard, throw, Heat or Rage decision until one side wins
  three rounds. Which attacks land, whether a throw is broken, whether a
  launch reaches the wall, whether Heat is activated by Burst or by an
  Engager and when, whether either fighter reaches Rage, whether a Rage Art
  is used, how much damage is banked as recoverable and regained, whether a
  round ends by KO or by the clock and which side wins are run parameters;
  no hit, whiff, wall splat, throw failure, resource spend or time-over is
  instructed. Live combat leaves the ordinary route only in its outcome
  branches, none of which is chosen deliberately.
- Potential scoped modules: one Ranked or Player Match set; Arcade Battle;
  one Super Ghost Battle; Practice frame-data verification; one match on a
  breakable stage such as Sanctum; a Special Style comparison; a DLC
  fighter matchup; Tekken Ball.
- Direct-play status: not conducted. Valve application and package data
  establish lawful availability, the base package and the DLC boundary;
  the SteamCMD projection establishes the current branch's build
  identifier, and Bandai Namco's patch notes separately establish the
  `Ver.3.02.01` label and its application time. Bandai Namco's official
  TEKKEN 8 site (battle-system, character, demo and offline-mode pages),
  its European guide and mechanics articles, its American patch notes and
  its 2026 Tekken World Tour rules establish the launch roster, the
  existence of an offline Versus mode with a CPU participant, the Heat,
  Rage, recoverable-gauge and Power Crush rules, the battle-screen
  elements, the round and time-over rule, the control styles and the
  default tournament settings. The community-maintained Wavu Wiki is one
  source family; it alone supplies the exact numeric frame, damage,
  threshold, health, stage-geometry and move-list values, and every claim
  resting on it alone is graded `Limited`. PCGamingWiki is a second
  community family for the side-view perspective alone; press guides, one
  trophy guide and dated Steam community threads supply the residual facts
  about guard, throw breaks, movement realignment, the configurable round
  settings and the CPU opponent. Bandai Namco's official manual material is
  inventoried in `T8-019`: the current site's Basic Operations and
  battle-system pages document the final product's screen, buttons,
  control styles, Heat, Rage, Power Crush and recoverable gauge; the 2023
  Closed Network Test and Closed Beta Test pages carry an image-only
  `Basic Operation/System Manual` for those test builds, read only as
  historical corroboration under a build caveat; no separate current
  downloadable manual was found (the Steam page has no `View manual`
  link, the MODE and BATTLE sections are web pages, and no Bandai Namco
  support article on Versus rules was found), and no official page states
  the Versus default settings. The Basic Operations Game Screen figure
  was inspected as one static frame (`T8-023c`); no source image was
  copied or reused as artwork. The Tekken
  Wiki on Fandom answered every request with HTTP 402 and is not used.
  This is an evidence-backed rules reconstruction, not a claimed captured
  playthrough. No video or audio was opened, played, heard, analysed or
  used.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `T8-001` | The admitted product is the Windows Steam application `1778820` TEKKEN 8, developed by Bandai Namco Studios and published by Bandai Namco Entertainment, released 2024-01-25 on Steam, sold in Ukraine, in base package `912716` that contains only that application, separate from three edition packages and twenty-four DLC applications | Confirmed | Direct | High | P1, P2 |
| `T8-002a` | The default public branch is Build `24827309`, updated 2026-08-19 22:00 UTC | Observation | Limited | Medium | S1 (a secondary projection of Valve data; one family) |
| `T8-002b` | Bandai Namco's patch notes name `Ver.3.02.01`, applied from 2026-08-19 15:00 PDT / 2026-08-20 00:00 CEST, as the current version; it added Bob as purchasable DLC, deleted pre-update replay data and changed matchmaking dialogue behaviour and Tekken Ball | Observation | Direct | High | P3 |
| `T8-002c` | Build `24827309` is the build that carries `Ver.3.02.01`; this rests on the coincident timestamps alone | Observation | Limited | Medium | S1, P3 (times only) |
| `T8-003a` | `Ver.3.02.01` implemented "system adjustments regarding health values and Quick Recovery" alongside move fixes; `Ver.3.00.00` (2026-03-17) reviewed every character with a focus on Heat and powered-up states; `Ver.3.00.02` (2026-04-16) adjusted Heat Dash combo starters and Heat-related moves | Observation | Direct | High | P3, P16, P17 |
| `T8-003b` | Under `Ver.3.02.01` maximum health is 190, Rage activates at 45 health or below and Quick Recovery recovers 5 frames slower | Observation | Limited | Medium | S2 (Version 3.02.01, Patches, Rage) |
| `T8-004` | Jin Kazama and Kazuya Mishima are launch-roster characters; Bob and nine other fighters are DLC | Confirmed | Direct | High | P4, P1 |
| `T8-005` | The full product has an offline Versus mode in which the second participant may be a CPU, and offline play supports one or two players | Observation | Corroborated | Medium | P5 (demo: "local multiplayer or versus CPU"), P6 (final product: Versus, "CPU vs. CPU not eligible for replays"), P15 (1–2 players offline), S5 (2023-12-26 thread on the CPU opponent) |
| `T8-006a` | Arena was one of the five stages of the July 2023 Closed Network Test and of the six stages of the October 2023 Closed Beta Test | Observation | Direct | High | P7, P18 (2023 test builds only; not evidence of the current build's stage list or geometry) |
| `T8-006b` | Arena is a selectable stage of the current base product: the community stage table lists it, and no DLC application in the Valve list is a stage named Arena | Observation | Limited | Medium | S2 (Stage), P1 (negative: no such DLC application); the publisher's lists in P7 and P18 name it only for the 2023 test builds |
| `T8-006c` | Arena is a 24 × 24 octagonal floor enclosed by walls with no wall break, hard wall break, floor break, floor blast, balcony break, wall bound or stage transition | Observation | Limited | Medium | S2 (Stage) alone |
| `T8-007a` | The number of rounds and the round time are configurable game option settings that apply to Versus, and shipped defaults exist | Observation | Limited | Medium | S5 (2024-01-24 thread), S6 |
| `T8-007b` | The shipped defaults are a match won by the first side to win three rounds and a 60-second round limit; Bandai Namco's 2026 Tekken World Tour rules prescribe "Tournament Settings: Default" and list "Rounds: 3 out of 5" and "Time Limit: 60 seconds", and the community wiki describes a match as "usually going until a player wins 3 rounds"; no official page or manual states the defaults directly, so this is an inference from the official rules' designation | Observation | Corroborated | Medium | P8, S2 (Jargon) |
| `T8-008a` | A round is won by depleting the opponent's Health Gauge or, when the Time Limit reaches 0, by having more health remaining; the match is won by winning the required number of rounds | Confirmed | Direct | High | P9 |
| `T8-008b` | Equal health at time-over is a draw and a double KO awards both sides a round | Observation | Limited | Low | community wiki seen only through a search snippet because the page returned HTTP 402; not admitted |
| `T8-009a` | The controls are four limb buttons (Left Punch, Right Punch, Left Kick, Right Kick); throws use 1+3 and 2+4; Arcade Style is the traditional layout and Special Style assigns recommended moves to buttons, switchable in each mode | Confirmed | Direct | High | P9, P10, P11 |
| `T8-009b` | Holding back requests standing guard against highs and mids, holding down or down-back requests crouching guard against lows, and an idle fighter guards highs and mids automatically (neutral guard); a sidestep is a tap of up or down, a sidewalk holds the direction after the tap, and a backdash creates space while still guarding highs and mids | Observation | Corroborated | Medium | S2 (Guard, Sidestep, Movement), S4 (DashFight guide, Hotspawn guide); the 2023 CBT manual's `Basic Operations` page (P18) shows the same guard, neutral-guard, step and walk inputs for that test build |
| `T8-009d` | The complete hit-level matrix: highs are blocked standing and pass over (are crushed by) a crouching fighter, mids are blocked standing and hit a crouching fighter, lows hit a standing fighter and are blocked crouching | Observation | Limited | Medium | S2 (Guard) alone; S4 states only that back blocks highs and mids and down-back blocks lows |
| `T8-009c` | A tech roll is entered by pressing an attack button as the fighter lands from a knockdown, a punch button rolling into the background and a kick button into the foreground, inside a 10-frame window, and it recovers the fighter in crouch after a sideways displacement; the get-up kicks FUFT.3 (low) and FUFT.4 (mid) attack from the face-up feet-toward ground state | Observation | Limited | Medium | S2 (Tech roll, Generic movelist) alone |
| `T8-009e` | From the ground, pressing up rises in place (quickstand), pressing back rises after moving back (back get-up), tapping 1 rolls sideways away from the screen and down+1 rolls sideways toward the screen (side roll); with no input the fighter stays down | Observation | Limited | Medium | S4 (DashFight guide) alone; S2 (Okizeme) names the same options without inputs |
| `T8-010a` | The generic throws are 1+3 and 2+4, and an ordinary throw is broken by pressing 1, 2 or 1+2 according to the hand the thrower extends | Observation | Corroborated | Medium | P9 and P11 (the throw inputs), S2 (Throw), S4 (DashFight guide) |
| `T8-010b` | The break window is 20 frames (14 on a counter-hit throw); a throw connecting on the side has a shorter window broken by that side's button; a throw connecting on the back is unbreakable; throws pass through guard | Observation | Limited | Medium | S2 (Throw) alone |
| `T8-011a` | Heat is available once per round; Heat Burst activates it while performing an attack with Power Crush properties for 10 seconds; a Heat Engager is a character attack that activates Heat on hit for 15 seconds and rushes the opponent with a significant advantage; Heat Smash consumes all remaining Heat for massive damage and ends Heat; Heat Dash follows a Heat Engager; during Heat, blocked attacks inflict recoverable gauge and move properties are enhanced; the Heat timer stops while the opponent is hit or downed | Confirmed | Direct | High | P11, P12, P9 |
| `T8-011b` | The Heat gauge is 900 frames, Heat Burst consumes 300 of them, Heat Burst deals only recoverable damage and cannot KO, Heat Engagers regain at least 30 recoverable health, Heat Dash is universally +5 on block and attacks consume gauge on hit or block | Observation | Limited | Medium | S2 (Heat) |
| `T8-012a` | Rage activates automatically when health drops below a certain amount; during Rage all attacks are more powerful and less chip damage is received; a Rage Art absorbs the opponent's attack and counterattacks, its power rising as health falls, and erases the opponent's recoverable gauge on hit | Confirmed | Direct | High | P11, P12 |
| `T8-012b` | Rage raises damage by 10%, reduces chip taken by 70%, the Rage Art input is df+1+2, its armour reduces incoming damage by 25%, and Rage ends when a Rage Art is used | Observation | Limited | Medium | S2 (Rage) |
| `T8-013a` | A recoverable gauge arises from being attacked in the air or while downed and from blocking certain special attacks or attacks during Heat; it is recovered when the fighter hits the opponent or forces a block, and a Heat Engager hit recovers a significant amount | Confirmed | Direct | High | P11, P12, P9 |
| `T8-013b` | Airborne damage splits 70% recoverable and 30% permanent, hits regain one to four points and Heat Engagers 30, each hit taken removes recoverable health equal to 30% of its damage, chip is always recoverable and cannot KO on its own, armour-absorbed damage is recoverable, and recoverable health clears at the round end | Observation | Limited | Medium | S2 (Recoverable health, Damage, Power crush) |
| `T8-014a` | A Power Crush is an attack that absorbs the opponent's high and middle attacks | Confirmed | Direct | High | P11; S2 (Power crush) agrees |
| `T8-014b` | Lows and throws beat a Power Crush | Observation | Limited | Medium | S2 (Power crush) alone |
| `T8-015a` | The battle screen shows PUNISH, CLEAN, COUNTER and TORNADO indicators and a combo count with combo damage since `Ver.2.00.01` | Observation | Direct | High | P13 |
| `T8-015b` | A counter hit is scaled to 120% damage, launchers put the opponent airborne for juggles, Tornado extends juggles and a wall splat leaves a brief wall-slump state | Observation | Limited | Medium | S2 (Counter hit, Wall) |
| `T8-015c` | An attack's start-up animation can be recognised before it lands, so slow lows, throws and slow mids are reactable; no sound cue is asserted | Observation | Limited | Medium | S2 (Reacting) |
| `T8-015d` | During a throw the extended hand shows which break button to press | Observation | Corroborated | Medium | S2 (Throw), S4 (DashFight guide) |
| `T8-016` | The battle screen exposes the Health Gauge, the Time Limit, the Rounds Won markers, the Heat Timer and the Recoverable Gauge | Confirmed | Direct | High | P9 |
| `T8-017` | Each fighter's move list carries Heat Burst 2+3, a fighter-specific Heat Smash (Jin's Hellfire Trespass Slayer, Kazuya's Omega Crash), a fighter-specific Rage Art R.df+1+2 with its own damage ceiling, fighter-specific Heat Engagers (Jin 1+2, f+3,1, df+4, f,F+2, ZEN.1,2; Kazuya df+1,2, db+1,2, b+4, b+1+2, f,F+2), Power Crushes (Jin d+1, db+1+2; Kazuya f+2, DVK.1+4), generic throws 1+3 and 2+4 broken by 1 or 2, command throws, while-standing launchers and Heat-only enhanced moves | Observation | Limited | Medium | S2 (Jin movelist, Kazuya movelist) |
| `T8-018` | Story, Arcade Quest, Character Episodes, Super Ghost Battle, Practice, Tekken Ball, the online modes and the Fight Pass are separate modes and services that do not enter an offline Versus match | Confirmed | Direct | High | P1, P6, P14, P15 |
| `T8-019` | Official manual inventory: the current official site publishes a Basic Operations page (game screen, button map, Heat Burst, Heat Smash and Rage Art availability, style switch) and a battle-system page for the final product; the 2023 Closed Network Test and Closed Beta Test pages each link an image-only `Basic Operation/System Manual` (seven pages) and a `Character Command List` for those test builds; no separate current downloadable final-product manual was found on the Steam page (no `View manual` link), in the official MODE and BATTLE sections, on the Bandai Namco product pages or in a support article, and no official page states the Versus default settings | Observation | Corroborated | Medium | P11 (current pages), P18 (test-build manuals, historical), P15 and P14 (negative search for a current manual) |
| `T8-020` | After the third round win the match result is declared; the options offered after the result and any state kept for a later match are not evidenced and lie outside the packet | Observation | Limited | Low | P9 (required rounds), negative search |
| `T8-021` | Other stages carry breakable walls, floors, balconies, wall bound and transitions | Observation | Limited | Medium | S2 (Stage, Stage break); outside this packet |
| `T8-022` | The bounded identity is one offline first-to-three duel on a walled floor plane where a lateral step can take a fighter out of a linear attack's path, hit levels meet standing or crouching guard, throws are contested by breaks, launches and Heat chip bank recoverable health that only the fighter's own attacks regain, a once-per-round timed Heat state and an automatic low-health Rage state reshape offence, and each round resets health, the recoverable gauge, Heat availability and Rage while the round markers persist until the third round win | Observation | Limited | Medium | `T8-004`–`T8-021`, `T8-023`; inherits the weakest material clause |
| `T8-023a` | The match is presented from a side view under direct real-time control | Observation | Corroborated | Medium | S7 (PCGamingWiki perspective field), P11 (the official Basic Operations Game Screen figure, `T8-023c`) |
| `T8-023b` | Movement realigns each fighter toward the opponent so that the two keep facing each other after lateral steps | Observation | Limited | Medium | S4 (Hotspawn movement guide) alone |
| `T8-023c` | Static visual observation, one frame: the official Basic Operations Game Screen figure (`img_screen_01.png`, 690 × 454, accessed 2026-09-09) views the fighters from the side; both bodies (Hwoarang left, Jin right, standing and facing each other on a water-covered stage that is not Arena) are wholly in frame with the gap between them visible, under a HUD carrying both health gauges, three round markers per side, a clock reading 60, both Heat timers, the recoverable-gauge region, a `WINS 2` marker and a Special Style prompt; no hit, guard, armour, airborne, wall, knockdown or wake-up state is shown in this frame, and the frame is not evidence of Arena, of the current build's stage list or of anything between frames | Observation | Direct | Medium | P11 (figure); the same frame is page 1 of the 2023 CBT manual (P18) and the game-screen image of the 2023 guide (P9) |

## Basic data

- Release / origin: Bandai Namco Studios and Bandai Namco Entertainment;
  Steam release 2024-01-25 (2024-01-26 in some regions); Season 3 began
  with `Ver.3.00.00` on 2026-03-17; `Ver.3.02.01` on 2026-08-19.
- Platform or physical form: lawfully available English Windows Steam
  client, base package `912716`; one offline local Versus match.
- Puzzle family: tactical forecast and counterplay; real-time system
  pressure.
- Primary and official sources, accessed 2026-09-09:
  - `P1` — [Valve application data](https://store.steampowered.com/api/appdetails?appids=1778820&cc=ua&l=english),
    for the title, Bandai Namco Studios and Bandai Namco Entertainment,
    Windows-only support, the 2024-01-25 release, packages `912716`,
    `1262248`, `1262249` and `1262250`, the twenty-four DLC applications,
    the single-player, online and shared-screen PvP categories and the
    Ukraine offer.
  - `P2` — [Valve package data](https://store.steampowered.com/api/packagedetails?packageids=912716&cc=ua&l=english),
    for package `912716` containing only application `1778820`.
  - `P3` — [Bandai Namco America patch notes `Ver.3.02.01`](https://www.bandainamcoent.com/news/tekken-8-patch-notes-v3-02-01),
    for the version label, application times, Bob as purchasable DLC, the
    replay deletion, the matchmaking dialogue change, the Tekken Ball
    change and the sentence on health-value and Quick Recovery system
    adjustments; the character tables are images and were not read.
  - `P4` — [official TEKKEN 8 character page](https://tk8.tekken-official.jp/en/character/),
    for the launch roster including Jin Kazama and Kazuya Mishima and the
    ten DLC fighters ending with Bob.
  - `P5` — [official TEKKEN 8 demo information](https://tk8.tekken-official.jp/demo/en/),
    for a Versus mode supporting two local players or a CPU opponent, Jin
    and Kazuya as demo fighters and Urban Square, Yakushima and Sanctum as
    demo stages.
  - `P6` — [Bandai Namco Europe, "What to expect from TEKKEN 8 (CBT Ver. VS Final Product Ver.)"](https://en.bandainamcoent.eu/tekken/news/what-expect-tekken-8-cbt-ver-vs-final-product-ver)
    (2023-11-30), for the final product's offline modes Arcade Quest,
    Super Ghost Battle, Versus (CPU versus CPU excluded from replays) and
    Practice, the online modes and the Fight Lounge.
  - `P7` — [Bandai Namco Europe, "TEKKEN 8 Closed Beta Test: Everything you need to know"](https://en.bandainamcoent.eu/tekken/news/tekken-8-closed-beta-test-everything-you-need-know)
    (2023-09-19), for the stage list naming Urban Square (Evening),
    Yakushima, Rebel Hangar, Sanctum, Arena and Ortiz Farm.
  - `P8` — [Bandai Namco America, Official Rules Tekken World Tour 2026](https://www.bandainamcoent.com/legal/community-events/official-rules-twt)
    (effective 2026-06-28), for "Tournament Settings: Default", "Rounds: 3
    out of 5", "Time Limit: 60 seconds", random stage selection and Special
    Style being allowed in match play.
  - `P9` — [Bandai Namco Europe, "TEKKEN 8 - The Guide to start playing"](https://en.bandainamcoent.eu/tekken/news/tekken-8-the-guide-start-playing)
    (2023-07-18), for the four limb buttons, the throw inputs, the
    Arcade/Special Style switch, the Heat Burst and Heat Engager durations,
    Heat Smash and Heat Dash, Rage and Rage Arts, the recoverable gauge,
    and the game-screen elements: Health Gauge, Time Limit ("When it
    reaches 0, time is up. The player with more health remaining wins the
    round."), Rounds Won ("Win the match by winning the required number of
    rounds."), Heat Timer and Recoverable Gauge; its game-screen image is
    the same frame as the Basic Operations figure, served from a 2023
    Closed Network Test guide folder.
  - `P10` — [Bandai Namco Europe, "TEKKEN 8: More info about the Arcade & Special Styles"](https://en.bandainamcoent.eu/tekken/news/tekken-8-more-info-about-the-arcade-special-styles)
    (2024-01-16), for Arcade Style as the traditional high-freedom style,
    Special Style's recommended moves per button that change with Heat and
    Rage state, and switching between the styles in each mode.
  - `P11` — [official TEKKEN 8 battle-system page](https://tk8.tekken-official.jp/en/battle/system.php),
    for the Heat System (once per round; Heat Burst with Power Crush
    properties, 10 seconds; Heat Engager, 15 seconds, rush and significant
    advantage; Heat Smash consuming all remaining Heat and ending it; Heat
    Dash; enhanced moves and recoverable damage on block), Power Crush
    ("absorbing an opponent's high or middle attacks"), the Recoverable
    Gauge (attacked in the air or while downed; blocking certain special
    attacks or attacks during Heat; recovered by hitting or forcing a
    block), Rage (automatic below a certain amount; more powerful attacks;
    less chip; Rage Art absorbing and counterattacking, power rising as
    health falls, erasing the opponent's recoverable gauge) and chip
    damage; the sibling
    [basic-operations page](https://tk8.tekken-official.jp/en/battle/basic_operations.php)
    for Heat Burst, Heat Smash and Rage Art availability states and the L1
    style switch, and its
    [Game Screen figure](https://tk8.tekken-official.jp/images/battle/basic_operations/img_screen_01.png),
    inspected as one static frame for `T8-023c`; no source image was
    copied or reused as artwork.
  - `P12` — [Bandai Namco Europe, "TEKKEN 8 - New info about gameplay mechanics, Rage and Heat systems, new control schemes and more!"](https://en.bandainamcoent.eu/tekken/news/tekken-8-new-info-about-gameplay-mechanics-rage-and-heat-systems-new-control-schemes)
    (2023-03-29), for "Heat can be activated once per round for 10
    seconds. Heat timer stops while an opponent is hit or down state",
    Heat Smash, Heat Dash, the enhanced Heat state, Rage and the
    recoverable gauge.
  - `P13` — [Bandai Namco America patch notes `Ver.2.00.01`](https://www.bandainamcoent.com/news/tekken-8-patch-notes-v2-00)
    (2025-03-31), for the combo count and combo damage display and the
    PUNISH, CLEAN, COUNTER and TORNADO indicators.
  - `P14` — [official TEKKEN 8 offline-mode page](https://tk8.tekken-official.jp/en/mode/offline.php),
    for Arcade Quest, Super Ghost Battle, Practice and Tekken Ball as
    separate offline modes; it does not describe Versus, so `T8-005` rests
    on `P5`, `P6` and `P15`.
  - `P15` — [Steam store page](https://store.steampowered.com/app/1778820/TEKKEN_8/),
    for the absence of a `View manual` link, the Single-player, Online PvP
    and Shared/Split Screen PvP features and the mode description; and the
    [Bandai Namco America product page](https://www.bandainamcoent.com/games/tekken-8)
    for "Offline Local Multiplayer: 1-2 Players".
  - `P16` — [Bandai Namco America patch notes `Ver.3.00.00`](https://www.bandainamcoent.com/news/tekken-8-patch-notes-v3-00)
    (2026-03-17), for the Season 3 character review focused on Heat and
    powered-up states, the Heat Smash wall-splat unification and the
    ranked changes.
  - `P17` — [Bandai Namco America patch notes `Ver.3.00.02`](https://www.bandainamcoent.com/news/tekken-8-patch-notes-v3-00-02)
    (2026-04-16), for the Heat Dash combo-starter and Heat-move
    adjustments and the note that Practice, Arcade Quest and Special Style
    command lists then contained inaccuracies.
  - `P18` — [official Closed Network Test page](https://tk8.tekken-official.jp/cnt/en/)
    (July 2023 test) and [official Closed Beta Test page](https://tk8.tekken-official.jp/cbt/en/)
    (October 2023 test), each linking an image-only `Basic Operation/System
    Manual` (`instruction.php`, seven pages) and `Character Command List`
    (`command.php`, eight pages), and [Bandai Namco Europe, \"TEKKEN 8: Here's what you're going to play in the Closed Network Test\"](https://en.bandainamcoent.eu/tekken/news/tekken-8-here-what-youre-going-play-the-closed-network-test),
    for the 2023 test builds' stage lists naming Arena and for the CBT
    manual's button map, movement, guard (including neutral guard), throw,
    Heat Burst, Heat Smash, Heat Dash and Rage Art commands and its Game
    Screen page; historical test-build material under a build-relevance
    caveat, never sole support for a current-build claim. The seven CBT
    manual pages were read as static images on 2026-09-09; the CNT manual
    and both command lists were enumerated but not read. The manual states
    no wake-up input, stage geometry, draw rule or default setting.
- Corroborating textual sources, accessed 2026-09-09:
  - `S1` — [public SteamCMD info projection](https://api.steamcmd.net/v1/info/1778820),
    for the `public` branch build `24827309` updated at Unix `1787176801`
    (2026-08-19 22:00:01 UTC); a secondary distribution mirror.
  - `S2` — [Wavu Wiki](https://wavu.wiki/t/Wavu:Tekken_8), the
    community-maintained TEKKEN frame-data wiki, read on the pages Stage,
    Stage break, Throw, Heat, Rage, Recoverable health, Guard, Sidestep,
    Movement, Generic movelist, Counter hit, Wall, Okizeme, Reacting, Power
    crush, Damage, Jargon, Notation, Patches (Tekken 8), Version 3.02.01,
    Jin movelist and Kazuya movelist; one family however many pages agree; never sole
    support for a product, build or mode claim.
  - `S4` — [DashFight, "Tekken 8 Beginner's Guide"](https://dashfight.com/news/a-beginner-s-guide-to-tekken-8-5187)
    (2024-02-07), for back-to-block, down-back low guard, throw inputs and
    hand-rule breaks, sidestep and sidewalk inputs; and
    [DashFight, "Tekken 8 Game Modes Explained"](https://dashfight.com/news/tekken-8-game-modes-explained-story-offline-online-5072)
    (2024-01-26) and [The Nerd Stash, "All Game Modes in Tekken 8, Explained"](https://thenerdstash.com/all-game-modes-in-tekken-8-explained/)
    (2024-01-26), for offline VS with customisable round counts and
    timers; and [Hotspawn, "Tekken 8 Beginner Series: Movement and How to Cancel It"](https://www.hotspawn.com/tekken/guide/tekken-8-beginner-series-movement-and-how-to-cancel-it)
    (2025-07-25), for movement realigning the fighter with a sidestepping
    or sidewalking opponent and for homing moves tracking lateral movement;
    one press family.
  - `S5` — dated Steam community threads:
    [vs CPU is too much easy!](https://steamcommunity.com/app/1778820/discussions/0/4030223677069305114)
    (2023-12-26: a CPU opponent mode exists and its highest level is
    Ultra Hard),
    [Number of rounds in the classic arcade battle](https://steamcommunity.com/app/1778820/discussions/0/4147320059824592681/)
    (2024-01-24: round count and duration "can only be modified in versus,
    tekken ball and ghost battle") and
    [Offline VS Unlimited Round Duration](https://steamcommunity.com/app/1778820/discussions/0/640179995535221181/)
    (2025-03-19: offline VS has no unlimited time option); no developer
    reply appears in any of them, and all threads count as one family.
  - `S6` — [PowerPyx TEKKEN 8 trophy guide](https://www.powerpyx.com/tekken-8-trophy-guide-roadmap/),
    for "Options > Game Option Settings > No. of Rounds" applying to all
    available match types and for offline VS being excluded from trophy
    progress.
  - `S7` — [PCGamingWiki, TEKKEN 8](https://www.pcgamingwiki.com/wiki/Tekken_8),
    read through its MediaWiki API, for the taxonomy fields `Perspectives:
    Side view`, `Controls: Direct control` and `Pacing: Real-time`; a
    second community family, used for the perspective alone.
- Negative searches, 2026-09-09: no separate current downloadable
  final-product manual was found on the Steam page, the official site, Bandai
  Namco's European or American product pages or a Bandai Namco support
  article (the current Basic Operations page and the 2023 test-build
  manuals are inventoried in `T8-019`); the official site's MODE section
  describes Arcade Quest, Super Ghost Battle, Practice and Tekken Ball but
  not Versus; no official statement of the shipped default round count or
  time limit exists apart from the tournament rules' `Default` designation
  (the official Game Screen text says only "the required number of
  rounds");
  no official statement of the draw or double-KO rule was found and the
  community wiki's page on it returned HTTP 402; the Tekken Wiki on Fandom
  (Versus Mode, Options, Health, Double K.O.) and the Esports World Cup
  rulebook could not be read; the character adjustment tables in `P3`,
  `P16` and `P17` are images and were not read.
- Evidence independence: sources are counted by family. Valve data (`P1`,
  `P2`, `S1`) is one family; Bandai Namco statements (`P3`–`P18`, on
  bandainamcoent.com, bandainamcoent.eu and tk8.tekken-official.jp) are
  one family; the Wavu Wiki (`S2`, including the two move lists) is one
  family; PCGamingWiki (`S7`) is a second community family; press guides
  (`S4`, `S6`) and Steam threads (`S5`) are separate families of lower
  reliability. `Corroborated` requires two families;
  `S2` alone is `Limited`; a single publisher statement is `Direct` for
  what it states and does not prove a neighbouring clause.
- Reproducible control: `V1` repository-side transition trace across
  `P1`–`P18` and `S1`–`S7` under the declared application, package, branch,
  mode, fighters, controls, stage, default rules and match-result terminal;
  rules reasoning, not direct play.
- Claim IDs: `T8-001`–`T8-023`; lettered sub-rows split composite claims so
  that each clause carries its own grade, and an unlettered reference means
  every sub-row of that claim. No audiovisual evidence was used.

## Mechanical decomposition

### Action Genes

- Existing `ACT-008`: walk forward and back, backdash, dash, jump, sidestep
  and sidewalk across the Arena floor (the lateral step is a movement-axis
  parameter), and from a knockdown the tech roll (an attack button as the
  body lands, `T8-009c`), the side roll (1 or d+1) and the back get-up (b)
  (`T8-009e`), whose commands displace the fighter through the floor geometry;
  existing `ACT-202`: crouch without changing local position and, from a
  knockdown, quickstand in place by pressing up (`T8-009b`, `T8-009e`), both
  direct posture changes rather than translation; staying down is no command
  and is not in either inventory;
  `ACT-294`: assign Jin to P1 and Kazuya to the CPU
  side, Arcade Style to P1 and Arena before the match; `ACT-295`: enter
  limb-button attacks, strings, while-standing and crouching commands,
  launchers, the Heat Engagers, the ground-state get-up kicks and the
  state-gated commands of the chosen fighter's move list — Heat Burst
  (2+3), the fighter's own Heat Smash (2+3 during Heat), the Heat Dash
  follow-up to a Heat Engager and the fighter's own Rage Art (df+1+2 during
  Rage) — with the universal input, the cancel source and the state
  eligibility (Heat unused this round, Heat active, Rage active) as the
  resource parameter, the eligibility itself being the entering and
  unlocking clause of `SYS-837` and `SYS-838`; `ACT-296`: hold back for standing guard or down-back for
  crouching guard and release it, with neutral auto-guard as a parameter;
  `ACT-297`: attempt a generic or command throw at close range, or press
  the matching break during the response window.
- Command audit of the Heat and Rage techniques, each tested as player
  command, ownership, legality gate and result: Heat Burst is a command
  listed in every fighter's move list with a universal input and rule,
  legal only while Heat is unused this round (a clause of `SYS-837`),
  resolving into Heat; a Heat Engager is an ordinary fighter attack whose hit
  resolves into Heat; Heat Smash is a fighter-specific attack with a
  universal input, gated by the active Heat reserve, resolving into damage
  and the end of Heat; Heat Dash is a follow-up input to a landed or
  blocked Heat Engager, gated by the active Heat reserve, consuming it; the
  Rage Art is a fighter-specific attack with a universal input, gated by
  the Rage state, resolving through armour, scaled damage and the end of
  Rage (`SYS-838`). Every one of them is therefore a character command
  under `ACT-295`, as Street Fighter 6's stock-gated Super Art is; the
  earlier assertion that they lie outside the fighter's move list is
  withdrawn. `ACT-298` is rejected: its boundary is a technique family
  funded by one shared spendable Drive stock with Burnout, while Heat and
  Rage are two independent states and no technique here spends a stock;
  the pass-01 generalisation is recorded as rejected in
  `TAXONOMY_CHANGE_044`.
- Rejected `ACT-356`: the sidestep has no protected interval and no
  cooldown; it is ordinary movement whose evasion is decided by the
  attack's tracking. Rejected `ACT-349`, `ACT-383`, `ACT-437`: guard is
  opponent-relative high or low posture, not an aimed direction, a
  depleting meter or equipment. Rejected `ACT-223`, `ACT-425`: no
  prompted or timed parry response exists; Rage Art armour is a technique
  property. Rejected `ACT-161`: the fighters' bodies and learned moves are
  not an equipped tool. Rejected `ACT-355`: no arena weapon. Rejected
  `ACT-064`: facing realigns automatically and is not commanded.
- Parameters: Jin, Kazuya, CPU authority and level, Arcade Style mapping,
  direction and button sequences, string members, hit levels, launchers,
  Heat Engager membership, throw inputs and break buttons, break window,
  Heat and Rage inputs and their state eligibility, tech roll, side roll,
  quickstand and back get-up inputs, get-up kick inputs, Ki Charge
  (available, not exercised).
  Claims: `T8-004`, `T8-005`, `T8-009`, `T8-010`, `T8-011`, `T8-012`,
  `T8-017`.

### System Behaviour Genes

- Existing `SYS-215`: real-time contact between the two fighters resolved
  by hit level against posture, range, tracking against lateral position,
  counter hit, punish, block stun, armour, launch, airborne juggle,
  Tornado, wall splat on Arena's walls, knockdown and get-up state, and
  permanent damage toward KO; `SYS-522`: a round settled by KO or by the
  health comparison at time-over, its marker recorded, health, Heat
  availability, Rage and recoverable gauge reset, and the match settled at
  the third round win.
- Reused, generalised `SYS-832`: damage from declared classes (airborne or
  downed hits and qualifying chip on block, with armour-absorbed damage as a
  recorded source parameter) is banked as recoverable health; each hit landed
  or attack blocked by the opponent restores a declared amount from that bank,
  and a Heat Engager restores a larger amount. Narrowed `SYS-836`: every later
  qualifying hit taken erodes a declared amount of the bank, while a landed
  Rage Art erases the opponent's remainder. `SYS-522`, not `SYS-836`, owns the
  round-boundary reset. `TAXONOMY_CHANGE_065` separates these rules from Dead
  Cells' timed drain and replacement under `SYS-852`. New `SYS-837`: a
  universal command (Heat Burst) or a
  Heat Engager landing enters the fighter into the Heat state once per
  round for 10 or 15 seconds; enhanced moves and recoverable chip on block
  apply, the timer pauses while the opponent is hit or downed, Heat Smash
  and Heat Dash consume the remainder, and the state ends at expiry or
  consumption. New `SYS-838`: health at or below the Rage threshold enters
  the fighter automatically into Rage for the rest of the round, raising
  damage and reducing chip taken and unlocking one Rage Art whose armour
  absorbs an attack, whose damage rises as the user's health falls and
  whose use ends Rage.
- Split-first: Heat and Rage were tested as one "powered state" and
  split, because their producers (a command or engager hit versus a
  health threshold), cadences (a pausing timer versus the rest of the
  round) and independent occurrence (Heat with full health; Rage without
  ever activating Heat) differ. Recoverable health was tested as a clause
  of Heat and split, because juggles bank it without Heat and it persists
  after Heat ends. Launch, juggle, Tornado and wall splat were kept as
  contact-state parameters of `SYS-215`, as the Street Fighter 6 carrier
  keeps Counter Hit, Punish Counter and knockdown; their only structural
  novelty, the recoverable split of airborne damage, is a source parameter
  of `SYS-832`. The knockdown state is a `SYS-215` contact-state parameter
  whose no-input branch is staying down; every rising or moving command
  from it is assigned by result: the displacing tech roll, side roll and back
  get-up are `ACT-008` inputs, the in-place quickstand is an `ACT-202` input,
  and the get-up kicks are `ACT-295` inputs.
- Evidence grades by clause: `SYS-837` is `Direct`, because activation by
  command or engager, the two durations, the once-per-round limit, the
  timer pause, the chip and enhanced moves, the consumption by Heat Smash
  and the expiry are all the publisher's statements (`T8-011a`), with the
  frame counts `Limited` (`T8-011b`). `SYS-832` is `Corroborated` across two
  independent carriers: its TEKKEN source classes and attack-driven recovery
  are the publisher's (`T8-013a`), while the Dead Cells carrier supplies the
  same portable transitions under different parameters. `SYS-836` remains
  `Limited`: Rage Art erasure is the publisher's (`T8-012a`), but the ordinary
  hit-erosion amount rests on the community wiki alone (`T8-013b`). `SYS-838`
  is `Limited`: automatic entry, the modifiers and
  the Rage Art's absorb, scaling and erasure are the publisher's
  (`T8-012a`), but the threshold and the clause that using the Rage Art
  ends Rage rest on the community wiki alone (`T8-012b`).
- Branch scope, stated for every conditional rule: a wall splat, a
  juggle, a throw break, a counter hit, Heat activation, Rage, a Rage Art,
  chip damage and a time-over are outcome branches of the two fighters'
  ordinary options; no representation of the route commands any of them.
- Retained-with-boundary `SYS-832`: Dead Cells and TEKKEN 8 share creation of
  a recoverable bank from eligible damage and restoration from the actor's
  outgoing attacks. Their timed drain or replacement (`SYS-852`) and later-hit
  erosion or erasure (`SYS-836`) remain separate rules. Rejected `SYS-750`,
  `SYS-473`, `SYS-165`, `SYS-737`: pending
  restorative recovery, core-and-outer meters, temporary Block and
  quiet-interval regeneration are not a banked portion regained by
  attacking. Rejected `SYS-520`, `SYS-521`: Heat is not a six-stock reserve
  spent per technique with Burnout, nor a tiered stock carried across
  rounds; Heat is a once-per-round timed state. Rejected `SYS-360`: Heat
  and Rage are universal states, not character-chosen resources. Rejected
  `SYS-833`, `SYS-820`, `SYS-799`, `SYS-420`: Rage is neither a lethal-hit
  downgrade, a stock-paid last chance nor an enemy's health-gated phase.
  Rejected `SYS-637`, `SYS-638`: damage subtracts from a terminal health
  pool and no blast zone or stock exists. Rejected `SYS-409`, `SYS-625`,
  `SYS-777`: no guard meter, directional block comparison or weapon parry.
  Rejected `SYS-456`: no dodge with a protected opening. Rejected
  `SYS-771`: it converts a selected personal mode into a modifier while
  continuously draining one shared reserve that replenishes after the
  drain ends; Heat is not selected among modes, is entered once per round
  by a command or a landed attack, and never replenishes before the next
  round. Rejected `SYS-707`: it refills a meter spent on abilities through
  successful attacks; recoverable health is created by damage taken, is
  never spent on an ability and is regained by hits and blocked attacks.
- Resolution order: confirm the match; each frame — sample both inputs,
  validate against fighter state and resource state, advance movement and
  realign facing, advance attacks, resolve contact by hit level, tracking,
  armour and posture, apply permanent and recoverable damage, update Heat
  and Rage state and timers, evaluate KO; on KO or time-over adjudicate the
  round, record the marker, reset the round state or settle the match at
  the third win.
  Claims: `T8-006`, `T8-008`, `T8-011`–`T8-015`.

### Constraint Genes

- Existing `CON-442`: a command begins only when
  the fighter, Arcade Style mapping, pose, recovery, airborne, grounded or
  downed state and command prerequisites permit it; `CON-446`: each round
  stops at zero health or at the 60-second limit and the match ends only at
  the third round win.
- New `CON-625`: both fighters occupy the Arena floor enclosed by walls;
  movement realigns each toward the opponent along the current axis; a
  sidestep or sidewalk is a legal displacement off that axis which can take
  the fighter out of the path of an otherwise intersecting linear attack,
  while an attack's tracking property changes how it follows the
  displacement without guaranteeing contact; a wall stops further
  displacement. Whether an attack then connects, splats the fighter or
  opens a follow-up is `SYS-215`'s resolution, not a promise of this
  geometry. Split-first against `ACT-008` (the step is the player's
  movement command; this gene is the legality of where it may go and what it
  can evade), `SYS-215` (contact, wall splat and follow-ups resolve there)
  and `CON-443` (a side-view line with corners and no lateral axis, which
  excludes three-dimensional traversal): the enclosure, the realignment and
  the legal lateral displacement are one rule about one floor, and removing
  the lateral displacement leaves `CON-443`. Grade `Limited`: the walled
  floor and the linear-versus-homing displacement rules rest on the
  community wiki (`T8-006c`, `T8-009b`) and the realignment on one press
  guide (`T8-023b`); the publisher's 2023 lists prove only that Arena
  existed in the test builds (`T8-006a`).
- Legality audit of the Heat and Rage techniques: `CON-442` excludes the
  resource costs by its own wording and continues to own pose, recovery and
  mapping legality; `CON-444` is Drive-specific, its pass-01 generalisation
  is rejected in `TAXONOMY_CHANGE_045`, and the match does not carry it;
  `CON-445` binds a tiered spendable stock that persists across rounds,
  which no TEKKEN technique has; `CON-351` binds abilities funded by one
  bounded quantity reserve that consume a declared amount, which fits Heat
  Smash and Heat Dash but not Heat Burst, whose cost is a per-round
  availability and which spends no reserve, nor the Rage Art, whose gate is
  an entered state; `CON-269` gates an ability on cast form, target, range,
  mana or charges, cooldown and disabling state, and its literal definition
  does not fit — Rage is an enabling state, not a disabling one, the Heat
  timer is an entered state rather than a charge, and no target or range
  clause is exercised — so it is rejected rather than stretched. No
  Constraint therefore owns the Heat and Rage eligibility separately: the
  once-per-round availability and the entered states are the entering and
  unlocking clauses of `SYS-837` and `SYS-838` and the resource parameter of
  the `ACT-295` commands, which is where the transition-to-gene round trip
  records them.
- Rejected `CON-443`: it excludes free three-dimensional traversal and
  binds a side-view line with corners; TEKKEN's legal lateral displacement
  and all-side walls change what an attack can be stepped out of. Rejected
  `CON-269`: its literal predicates do not fit, as recorded above. Rejected
  `CON-520`, `CON-522`: no blast zone or stock. Rejected
  `CON-519`, `CON-458`: no aerial recovery budget. Rejected `CON-604`: no
  exertion reserve. Rejected `CON-594`, `CON-617`: no parry class.
  Rejected `CON-175`, `CON-183`: health resets every round and no life
  stock exists.
- Scarce strategic resources: health and its recoverable portion, the
  once-per-round Heat activation and its remaining time, the Rage state
  and its one Rage Art, remaining round time, floor position and distance
  to the walls, and recovery frames.
  Claims: `T8-006`, `T8-007`, `T8-008`, `T8-009`, `T8-011`, `T8-012`,
  `T8-023`.

### Information Genes

- Existing `INF-142`: an attack's start-up animation lets a slow low, a
  throw or a slow mid be answered before it lands (`T8-015c`, `Limited`),
  and the throw's extended hand shows which break button to press
  (`T8-015d`, `Corroborated`); no sound cue is asserted, and the
  PUNISH, CLEAN, COUNTER and TORNADO notices are post-contact feedback,
  recorded as the hit-notice parameter of `INF-210` rather than as a cue;
  `INF-209`: the shared side view keeps both fighters' bodies, their
  distance, facing and pose in frame (`T8-023a`, corroborated by the
  official static Game Screen figure, `T8-023c`) and the current hit state
  readable through the attack's start-up (`T8-015c`) and the publisher's
  PUNISH, CLEAN, COUNTER and TORNADO indicators (`T8-015a`); the guard,
  armour, airborne, wall, knockdown and wake-up states named by the gene's
  parameters are not separately evidenced as visible and are not asserted
  for this instance, and continuity between frames is inferred from the
  fixed side-view perspective rather than observed, so the instance is
  `Limited`; `INF-210`: the battle
  screen exposes both Health Gauges with their Recoverable Gauges, both Heat
  gauges and timers, Rage indication, the Time Limit and the Rounds Won
  markers, plus the post-contact notices and combo count (generalised by
  `TAXONOMY_CHANGE_046` from the Drive-and-Super wording so that any
  shared-resource state is one boundary).
- Excluded for insufficient evidence: any preview of the CPU level's
  behaviour, any exact frame or damage readout outside Practice, and any
  audio cue. Rejected `INF-254`: no damage colour or stock. Rejected
  `INF-276`, `INF-290`: no special-meter preparation or shot clock.
- Claims: `T8-009`, `T8-015`, `T8-016`, `T8-023`.

### Objective Genes

- Existing `OBJ-099`: win the required three rounds against the fixed
  Kazuya opponent by KO or favourable time-over before the CPU does
  (generalised by `TAXONOMY_CHANGE_047` from the two-round wording so that
  the required count is a parameter).
- Rejected `OBJ-121`, `OBJ-071`, `OBJ-105`: no stock, team round score or
  control round.
- Success, evaluation and failure: success is P1's third round win and the
  result state; failure is the CPU's third round win; a draw or double KO
  is not admitted (`T8-008b`); there is no retry inside the match.
  Claims: `T8-007`, `T8-008`.

### Time Genes

- Existing `TIM-003`: both fighters, attacks, recovery states, the Heat
  timer, Rage and the round clock advance in real time while inputs are
  accepted.
- Rejected `TIM-001`, `TIM-005`: no turn or phase. Rejected `TIM-021`: no
  persistence between matches is claimed.
  Claims: `T8-008`, `T8-011`.

## Reproducible transitions

Row classes: **A** always executed on the ordinary route; **C** conditional
on an ordinary contact, resource or player option; **F** failure boundary.

| Class | Before | Action | Deterministic or bounded resolution | What it establishes | Claim ID |
|---|---|---|---|---|---|
| A | Offline > Versus is open | Assign Jin to P1 and Kazuya to the CPU, keep Arcade Style, select Arena and confirm | Round 1 begins on Arena with both health bars full, no Heat used, no Rage, the clock at 60 | the bounded participant, control, stage and rules contract | `T8-004`, `T8-005`, `T8-006`, `T8-007` |
| A | Both fighters are actionable at a distance | Walk, backdash, dash, crouch, jump, sidestep or sidewalk | Distance and axis update on the walled floor; facing realigns automatically; a lateral step can move the fighter out of the path of an otherwise intersecting linear attack, while a tracking attack follows the displacement; a wall stops further displacement | live spacing on a floor plane with a legal lateral axis | `T8-006c`, `T8-009b`, `T8-023b` |
| A | A fighter is actionable in range | Enter a limb-button attack, string, while-standing or crouching command, launcher or Heat Engager | The attack resolves by its hit level against the opponent's posture, by its tracking property against the opponent's lateral displacement and by distance and timing: hit, counter hit at 120%, block, whiff or armour; a launcher puts the opponent airborne | command-to-contact combat on the third axis | `T8-009`, `T8-015`, `T8-017` |
| C | An opposing attack's start-up is visible (`T8-015c`) | Hold back, or down-back, or release | Standing guard blocks highs and mids and is hit by lows; crouching guard blocks lows, is hit by mids and makes highs whiff; blocked attacks leave block stun and, during the attacker's Heat, recoverable chip | high, mid and low guard posture | `T8-009b`, `T8-009d`, `T8-011a` |
| C | The fighters are at throw range | Attempt 1+3, 2+4 or a command throw; the defender reads the extended hand and presses 1, 2 or 1+2 in the break window | A matching break within 20 frames (14 on counter hit) escapes; otherwise the throw damages and repositions; back throws cannot be broken | the simultaneous throw contest and its visual cue | `T8-010`, `T8-015d`, `T8-017` |
| C | A launching hit connects, or a hit lands near a wall | None | The opponent is airborne and further hits connect as a juggle with 70% of their damage banked as recoverable; Tornado extends the juggle; a wall splat leaves a brief wall-slump state; landing leaves a knockdown | launch, juggle, wall and knockdown as contact states | `T8-013`, `T8-015b`, `T8-006c` |
| C | A fighter is knocked down | Tech roll with an attack button as the body lands, side roll with 1 or d+1 or back get-up with b (`ACT-008`); quickstand in place with u (`ACT-202`); enter a get-up kick FUFT.3 or FUFT.4 (`ACT-295`); or give no input | The tech roll and side roll displace the downed body sideways before it rises, the back get-up rises after moving back and the quickstand changes the fighter from prone to standing without local displacement; the kick attacks from the ground as a low or mid; with no input the fighter stays down, the knockdown state's default branch (`SYS-215`) | every admitted wake-up command with its exact input and Action owner, and staying down as a state branch outside the command inventory | `T8-009c`, `T8-009e` |
| C | Heat is unused this round, or a Heat Engager lands | Enter Heat Burst (2+3), a state-gated move-list command, or land a Heat Engager | Heat begins for 10 seconds by Burst or 15 by Engager (the Engager rushes the opponent with advantage and regains recoverable health); enhanced moves and recoverable chip on block apply; the timer pauses while the opponent is hit or downed; Heat Smash or Heat Dash consumes the remainder; Heat ends at expiry or consumption and cannot be reactivated this round | the once-per-round timed powered state and its consumption | `T8-011`, `T8-017` |
| C | A fighter's health falls to or below the Rage threshold | None; then optionally enter the fighter's Rage Art (df+1+2), a state-gated move-list command | Rage begins automatically for the rest of the round with raised damage and reduced chip taken; the Rage Art absorbs an incoming attack, deals damage that rises as the user's health falls, erases the opponent's recoverable gauge and ends Rage | the automatic low-health state and its one finisher | `T8-012` |
| C | Damage is banked as recoverable | Land a hit, or have an attack blocked | Each landed hit or blocked attack regains a declared amount, a Heat Engager 30; every hit taken removes 30% of its damage from the banked portion; the portion never drains on its own and clears at the round end; chip and Heat Burst damage cannot KO on their own | recoverable health regained only by aggression | `T8-013` |
| C | A Power Crush move is active while a high or mid lands | None | The armour absorbs the attack and the move continues; the absorbed damage is recoverable; a low or a throw beats it | armour as an attack property | `T8-014` |
| A | Health reaches zero, or the clock reaches 0 | Complete the current resolution | The round is awarded by KO, or to the side with more health at time-over; a marker lights; health, Heat availability, Rage and recoverable gauge reset for the next round | round adjudication and reset | `T8-008a`, `T8-013b` |
| A | One side holds two markers and wins another round | Complete the current resolution | The third marker settles the match and the result state appears; what is offered after it lies outside the packet | the finite match terminal | `T8-007b`, `T8-008a`, `T8-020` |
| F | The CPU holds two markers and wins another round | None | The result state declares the CPU the winner; the packet ends for the selected side with no retry inside the match | the failure boundary | `T8-008a` |

## Strategic and experiential structure

- Planning horizon: win three rounds before Kazuya does by converting
  spacing and hit-level reads into launches while keeping enough health
  and recoverable gauge to survive his.
- Local tactics: step a linear attack and punish its recovery; duck a high
  and launch; crouch-block a low string; break the throw by the extended
  hand; activate Heat when a rush will land rather than on wake-up; spend
  Heat Smash to close a round; keep a wall behind the opponent and not
  behind yourself; keep landing hits while recoverable health is banked.
- Medium-term structure: the first round teaches which of Kazuya's attacks
  track and which whiff to a step; later rounds turn Heat timing and the
  Rage threshold into a race between damage and the clock.
- Reversible versus irreversible: three state layers must be kept apart.
  Hit stun, block stun, armour frames, airborne and knockdown state are
  transient contact values; health, the recoverable portion, the Heat
  gauge, the Heat availability and Rage are round-local and reset at the
  round boundary; the round markers persist between rounds and settle the
  match at the third win; what is retained after the result state is not
  evidenced and lies outside the packet.
- Failure attribution: the notices, contact effects, health and
  recoverable bars, Heat timer and Rage flash separate spacing, hit-level
  and timing errors; the CPU's policy is the acknowledged variance.
- Player trust: a stepped linear attack must whiff, a low must be blocked
  crouching, a matching break must escape the throw, banked recoverable
  health must return when hitting, Heat must be available exactly once per
  round and the round must end at zero health or the clock.
  Claims: `T8-008`–`T8-015`.

## Replay and variation

- What changes between matches: the exchanges, the CPU's choices, Heat and
  Rage timing, whether walls are reached, how rounds end and the winner.
- Randomness or procedural generation: the stage and rules are fixed; only
  the CPU's policy and fine timing vary.
- Multiple viable strategies: keep-out and whiff punishment, close pressure
  with strings and throws, Heat-first aggression, Heat held for the wall,
  or patient defence into Rage comebacks can all reach three round wins.
- Typical replay motive: learn the matchup, the tracking of each attack,
  break timing, Heat conversion and wall carry, or change fighter, stage or
  CPU level in a separately reviewed scope.
  Claims: `T8-005`, `T8-009`–`T8-015`.

## Adjacent systems and history

- Direct product corridor: no other TEKKEN game is in the corpus.
- Same-corpus corridors: Street Fighter 6, the mathematically selected
  neighbour, shares the fighter, side and control assignment, the
  character-command attack, the directional guard, the throw contest,
  real-time combat, round adjudication, command legality, the finite round
  bounds, the cues, the visible spacing and the paired HUD, but fights on a
  side-view line with corners, funds five universal Drive techniques from a
  six-stock reserve with Burnout, carries Super stock across rounds and
  settles at two round wins; Brawlhalla shares the fighter
  assignment, the character command, real-time combat, command legality,
  cues and the shared view but converts damage into launch risk on a
  platform with blast zones and settles by stocks.
- Important differences: this packet fights on a walled floor plane where
  a lateral step can take a fighter out of a linear attack's path, banks
  juggle and chip
  damage as recoverable health that only the fighter's own attacks regain,
  gives each
  fighter one timed Heat activation per round that its declared consuming
  commands, Heat Smash and Heat Dash, spend, enters Rage automatically at low health with one Rage Art that
  ends it, and settles at the third round win while health, the recoverable
  gauge, Heat availability and Rage reset each round and only the round
  markers persist. Claims: `T8-004`–`T8-023`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-202`, `ACT-294`, `ACT-295`, `ACT-296`, `ACT-297` | fighters, CPU level, Arcade Style, movement axes, crouch posture, tech roll, side roll, quickstand and back get-up inputs, get-up kicks, hit levels, strings, throw inputs and breaks, Heat and Rage inputs and their state eligibility |
| System Behaviour | `SYS-215`, `SYS-522`, `SYS-832`, `SYS-836`, `SYS-837`, `SYS-838` | contact states, counter hit, launch, juggle, Tornado, wall splat, knockdown with its stay-down branch, recoverable-health banking and attack recovery, later-hit erosion and finisher erasure, Heat durations, availability and pause rule, Rage threshold and Rage Art properties, 60-second clock, three required wins |
| Constraint | `CON-442`, `CON-446`, `CON-625` | pose and recovery, health and clock bounds, Arena geometry, realignment and tracking classes |
| Information | `INF-142`, `INF-209`, `INF-210` | start-up and throw-hand cues, side view with one-frame official figure, gauge layout and post-contact notices |
| Objective | `OBJ-099` | three required round wins |
| Time | `TIM-003` | frame schedule, Heat timer, round clock |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `282` (`GAME-0001`–`GAME-0282`).
- Exact genome matches: none.
- Tied near matches: `GAME-0172` — Street Fighter 6 (`14 / 26 = 0.538462`).
- Supported combination subsets: none.
- Scan date: 2026-09-10.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0172` — Street Fighter 6 | `ACT-008`, `ACT-294`, `ACT-295`, `ACT-296`, `ACT-297`, `SYS-215`, `SYS-522`, `CON-442`, `CON-446`, `INF-142`, `INF-209`, `INF-210`, `OBJ-099`, `TIM-003` | Both fix two fighters for one offline match, resolve character commands, directional guard and throw contests through real-time contact, adjudicate rounds by KO or time-over and settle at a required round-win count under one paired HUD. Street Fighter 6 confines the fighters to a side-view line with corners, funds five universal Drive techniques from a six-stock reserve whose exhaustion causes Burnout and gates them on that stock, carries Super Art stock across rounds and settles at two wins. TEKKEN 8 instead adds direct in-place posture changes through crouching and quickstand, fights on a walled floor plane where a lateral step can take a fighter out of a linear attack's path, banks eligible damage as recoverable health regained by the fighter's own hits and blocked attacks while later opposing hits and Rage Art separately erode or erase it, gives each fighter one timed Heat activation per round that Heat Smash and Heat Dash consume, enters Rage automatically at low health with one Rage Art that ends it, and settles at three wins while health, the recoverable gauge, Heat availability and Rage reset each round. | Near, `0.538462` |

### Preserved research notes

- New genes: `SYS-836`, `SYS-837`, `SYS-838` and `CON-625`.
- Reused genes: `ACT-008`, `ACT-202`, `ACT-294`, `ACT-295`, `ACT-296`, `ACT-297`,
  `SYS-215`, `SYS-522`, `SYS-832`, `CON-442`, `CON-446`, `INF-142`,
  `INF-209`, `INF-210`, `OBJ-099` and `TIM-003`.
- Classification result: `New gene plus later common-core reuse`.
- Evidence and reasoning: thirteen boundaries transfer from the reviewed
  corpus without any wording change; `INF-210` and `OBJ-099` transfer after
  the minimal generalisations recorded in `TAXONOMY_CHANGE_046` and
  `TAXONOMY_CHANGE_047`, each of which keeps the Street Fighter 6 instance
  true sentence by sentence with Drive, Super and the two-round count as
  parameter values; the pass-01 generalisations of `ACT-298` and `CON-444`
  were rejected after a technique-by-technique carrier audit
  (`TAXONOMY_CHANGE_044`, `TAXONOMY_CHANGE_045`), so the Heat and Rage
  commands are character commands under `ACT-295` whose state eligibility
  is a clause of `SYS-837` and `SYS-838`; `CON-269` was tested and rejected
  because its literal predicates do not fit. `TAXONOMY_CHANGE_065` later adds
  `SYS-832` after its common damage-bank and attack-recovery trace transfers
  from Dead Cells; the incompatible expiry rules remain `SYS-852` and
  `SYS-836`. The corpus had no later-hit erosion or finisher erasure of a
  recoverable-health bank, no once-per-round timed powered state whose
  remainder is spent through declared commands, no automatic low-health powered state with a
  one-use finisher, and no walled floor plane with legal lateral
  displacement and automatic realignment, so four genes are new; each is portable to other
  fighting rulesets and none is named after a fighter, stage, move or
  update. The grades follow the evidence model's weakest-clause rule:
  `SYS-837` is `Direct` because every clause is the publisher's statement;
  `SYS-836`, `SYS-838` and `CON-625` are `Limited` because at least one
  material clause of each rests on the community wiki or one press guide
  alone.

## Taxonomy impact

- Registry changes: four original Active genes listed above; `SYS-832` gains
  this game as a second carrier and `SYS-836` is narrowed to later-hit erosion
  or finisher erasure by
  [`TAXONOMY_CHANGE_065`](../../../research/taxonomy-changes/TAXONOMY_CHANGE_065.md);
  `INF-210` and
  `OBJ-099` generalised by
  [`TAXONOMY_CHANGE_046`](../../../research/taxonomy-changes/TAXONOMY_CHANGE_046.md)
  and
  [`TAXONOMY_CHANGE_047`](../../../research/taxonomy-changes/TAXONOMY_CHANGE_047.md)
  so that the displayed shared resources and the required round count are
  parameters; the pass-01 generalisations of `ACT-298` and `CON-444` are
  recorded as rejected in
  [`TAXONOMY_CHANGE_044`](../../../research/taxonomy-changes/TAXONOMY_CHANGE_044.md)
  and
  [`TAXONOMY_CHANGE_045`](../../../research/taxonomy-changes/TAXONOMY_CHANGE_045.md)
  and those entries keep their committed wording; twelve further Active
  genes gain this game as an additional carrier. This correction adds only
  `SYS-832` to the reviewed signature; no lifecycle or committed ID changes.
- Taxonomy-change record: `TAXONOMY_CHANGE_046`, `TAXONOMY_CHANGE_047` and
  `TAXONOMY_CHANGE_065` accepted; `TAXONOMY_CHANGE_044` and
  `TAXONOMY_CHANGE_045` rejected.
- Candidate terms affected: recorded in `CANDIDATE_TERMS.md`; `TEKKEN 8`,
  Jin Kazama, Kazuya Mishima, Arena, Heat, Heat Burst, Heat Engager, Heat
  Smash, Heat Dash, Rage, Rage Art, Power Crush, Tornado, every move name,
  `Ver.3.02.01` and every application, package, build and branch
  identifier remain parameters or literal product terms.

## Negative results

- No direct-play, entitlement, screenshot, video or audio claim.
- No Special Style, DLC fighter or stage, breakable stage element, Ki
  Charge, draw rule, rematch menu, online or progression mechanic is
  imported; the draw and double-KO rule is excluded for insufficient
  evidence rather than asserted.
- `ACT-298`, `ACT-356`, `ACT-349`, `ACT-383`, `ACT-437`, `ACT-223`,
  `ACT-425`, `ACT-161`, `ACT-355`, `ACT-064`, `SYS-750`,
  `SYS-473`, `SYS-165`, `SYS-737`, `SYS-520`, `SYS-521`, `SYS-360`,
  `SYS-833`, `SYS-820`, `SYS-799`, `SYS-420`, `SYS-637`, `SYS-638`,
  `SYS-409`, `SYS-625`, `SYS-777`, `SYS-456`, `SYS-771`, `SYS-707`,
  `CON-269`, `CON-443`, `CON-444`, `CON-445`, `CON-351`, `CON-520`,
  `CON-522`,
  `CON-519`, `CON-458`, `CON-604`, `CON-594`, `CON-617`, `CON-175`,
  `CON-183`, `INF-254`, `INF-276`, `INF-290`, `OBJ-121`, `OBJ-071`,
  `OBJ-105`, `TIM-001`, `TIM-005` and `TIM-021` are rejected with the
  smallest counterexamples recorded above.
- The pass-01 generalisations of `ACT-298` and `CON-444` are withdrawn:
  `TAXONOMY_CHANGE_044` and `TAXONOMY_CHANGE_045` are recorded as
  rejected, and no Heat or Rage technique is described as lying outside
  the fighter's move list; the pass-02 reuse of `CON-269` is withdrawn
  because its literal predicates do not fit, and no filler Constraint
  replaces it.
- No hit, whiff, wall splat, throw failure, resource spend or time-over is
  instructed to make a gene legal; Heat, Rage, recoverable health, wall
  contact and the time-over comparison are admitted only as branches that
  the two fighters' ordinary options produce.
- No shipped default is described as read from a manual; the first-to-three
  and 60-second defaults are recorded as an inference from the publisher's
  tournament rules and are reproducible by leaving the settings untouched.
- No wake-up command is admitted by option name alone: every admitted
  ground command carries an exact input and an Action owner, and staying
  down is a knockdown-state branch, not a command. No categorical claim
  that no official manual exists is made; the manual inventory in
  `T8-019` separates current final-product pages from historical
  test-build material.

## Delta summary

## New facts

- [Confirmed | Direct | High] Current base-package Windows availability,
  the launch roster containing Jin and Kazuya, the round and time-over
  rule, the battle-screen elements and the publisher's Heat, Rage,
  recoverable-gauge and Power Crush absorption statements are fixed in
  `T8-001`, `T8-004`, `T8-008a`, `T8-009a`, `T8-011a`, `T8-012a`,
  `T8-013a`, `T8-014a`, `T8-016` and `T8-018`.
- [Observation | Direct | High] The publisher's `Ver.3.02.01` label, its
  application time and its health-value and Quick Recovery adjustment, and
  the `Ver.2.00.01` post-contact battle indicators, are stated by Bandai
  Namco itself in `T8-002b`, `T8-003a` and `T8-015a`; Arena's presence in
  the 2023 test builds (`T8-006a`) and the one-frame Game Screen
  observation (`T8-023c`) are `Observation | Direct | Medium` because
  neither speaks for the current build's stage or for anything between
  frames.
- [Observation | Corroborated | Medium] The offline Versus mode with a CPU
  participant, the first-to-three and 60-second defaults, the guard and
  movement inputs with neutral guard, the hand-rule throw break, the
  throw-hand break cue, the manual inventory and the side view are bounded
  in `T8-005`, `T8-007b`, `T8-009b`, `T8-010a`, `T8-015d`, `T8-019` and
  `T8-023a`.
- [Observation | Limited | Medium] The build identifier and its link to
  the label, Arena's current availability and its geometry, the numeric
  health, Rage, Heat, recoverable, counter-hit and move-list values, the
  full hit-level matrix, the tech-roll, get-up-kick and in-place or
  backward rising inputs, the throw windows, the low-and-throw counters
  to Power Crush, the configurable settings, the start-up reactability,
  the realignment and other stages' breakable elements rest on one family
  each (`T8-002a`, `T8-002c`, `T8-003b`, `T8-006b`, `T8-006c`, `T8-007a`,
  `T8-009c`, `T8-009d`, `T8-009e`, `T8-010b`, `T8-011b`, `T8-012b`,
  `T8-013b`, `T8-014b`, `T8-015b`, `T8-015c`, `T8-017`, `T8-021`,
  `T8-022`, `T8-023b`); the draw rule and the
  post-match state are `Limited | Low` (`T8-008b`, `T8-020`).

## New genes

- [Observation | Direct | Medium] `SYS-837` isolates the once-per-round
  timed powered state whose remainder is spent through declared commands, every clause on the
  publisher's own statements with numeric values as `Limited` parameters.
- [Observation | Limited | Medium] `SYS-836` isolates later-hit erosion and
  Rage Art erasure of recoverable health, `SYS-838` the automatic low-health powered
  state with a one-use finisher that ends it, and `CON-625` the walled
  floor plane whose legal lateral displacement and automatic realignment
  bound where an attack can be stepped out of; each carries the weakest of its material clauses, which
  rest on the community wiki or one press guide alone.

## New combinations

- [Observation | Corroborated | High] `No new combinations`; none of the
  271 verified sets is a strict subset of this signature; the nearest
  misses, `COMB-0270` and `COMB-0271`, lack two genes each, and the Street
  Fighter 6 combination `COMB-0170` lacks `SYS-520`, `SYS-521` and
  `CON-445`.

## Taxonomy changes

- [Observation | Direct | High] `TAXONOMY_CHANGE_046` and
  `TAXONOMY_CHANGE_047` generalise `INF-210` and `OBJ-099` so that the
  displayed shared resources and the required round count are parameters;
  `TAXONOMY_CHANGE_044` and `TAXONOMY_CHANGE_045` are rejected after the
  carrier audit and `ACT-298` and `CON-444` keep their committed wording;
  `TAXONOMY_CHANGE_065` reuses generalised `SYS-832` for recoverable-health
  banking and attack-based recovery, narrows `SYS-836` to incoming-attack
  erosion and erasure, and leaves round reset in `SYS-522`. No lifecycle alias
  or committed ID change occurs.

## New questions

- Does Cities: Skylines II, the next ordered subject, share any real-time
  pressure boundary with a fixed duel, or is the corridor purely through
  the city-building corpus?

## Next recommended game

- [Hypothesis | Limited | High] `GAME-0284` — Cities: Skylines II, only
  under a new game-specific prompt after this unit's independent audit.
- Optimisation criterion: replace a fixed two-fighter ruleset with a
  continuous simulation whose early milestone gates a reload-verified
  save.
- Expected information gain: separate road, zoning, service and demand
  boundaries from the existing city-building carriers.
- Backlog impact: advances the recorded 280-to-288 calibration horizon.

## Why this game

- [Hypothesis | Limited | High] The third transfer test had to succeed on
  a fixed-opponent real-time ruleset whose nearest corpus neighbour is
  strong, so success depended on reuse-first discipline and honest
  isolation of the genuinely new Heat, Rage, recoverable-health and
  three-dimensional spacing boundaries rather than on a distant packet.
