---
game_id: GAME-0299
slug: nioh-2
game_title: Nioh 2
analysis_status: reviewed
reviewed: 2026-09-18
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-161
    - ACT-190
    - ACT-200
    - ACT-224
    - ACT-249
    - ACT-419
    - ACT-429
    - ACT-436
    - ACT-437
    - ACT-438
    - ACT-459
    - ACT-460
  system:
    - SYS-215
    - SYS-364
    - SYS-380
    - SYS-397
    - SYS-399
    - SYS-409
    - SYS-578
    - SYS-798
    - SYS-868
    - SYS-869
    - SYS-870
    - SYS-871
  constraint:
    - CON-282
    - CON-589
    - CON-604
    - CON-636
  information:
    - INF-119
    - INF-318
    - INF-342
  objective:
    - OBJ-080
  time:
    - TIM-003
---

# Game: Nioh 2

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Instance names and
amounts parameterise genes; they do not enter their labels.

## Analysis scope

- Version / ruleset: the unmodified English PlayStation 4 base digital product
  `UP9000-CUSA15532_00-NIOH2NA000000000`, originally released 2020-03-13.
  The last PS4-specific publisher update located during this review is
  `Ver 1.27` dated 2021-03-08. That is a public documentation reference, not
  a claim about an installed console build. The Koei Tecmo web manual bears a
  later Complete Edition heading but its explicitly labelled PS4 controls and
  common core rules are cross-checked against Sony's March 2020 base-release
  guide; no DLC or Complete Edition content enters this packet.
- Product, entry and setup: start a new solo offline base-game save on PS4,
  choose an ordinary starting melee weapon and Guardian Spirit, and enter the
  first main mission, `The Village of Cursed Blossoms`, in the Awakening
  region. The chosen weapon and Spirit form are fixed parameters of a
  reproduction, not separate games. Begin at the first playable mission
  position before using its opening Shrine.
- Primary decision loop: read life, Ki, Anima, stance, opponent Ki and red
  burst-attack cues; traverse the route while spending Ki on attacks, evasions
  and guard; change high/mid/low stance to choose attack speed, reach and
  commitment; time Ki Pulse after attacks to regain the recoverable Ki and
  purify nearby Yokai Realm patches; spend melee-earned Anima on a timed Burst
  Counter or an attuned Soul Core ability; pray at Shrines to recover while
  ordinary enemies respawn; recover the grave's Amrita after a death before a
  second death destroys it; defeat the source Enki to clear the mandatory Dark
  Realm, collect the Inner Shrine Key, unlock the boss route, break Mezuki's
  Ki where possible and defeat it.
- Positive terminal: defeat Mezuki, interact with the mission-ending golden
  glow and observe settlement back on the mission map with the successor main
  mission available. Merely lowering the boss's Ki or defeating it without
  the ending interaction is not the terminal. No reload was performed.
- Negative terminal: when life empties, the attempt returns to the last
  prayed-at Shrine. The Guardian Spirit and lost Amrita remain at one grave;
  reaching it restores them, while dying again first destroys the earlier
  Amrita and unpurified Soul Cores. The save and mission remain reattemptable.
- Included: direct traversal, ordinary melee attack, guard and Ki-priced
  evasion, selected lock-on, three combat stances, automatic Ki recovery and
  timed Ki Pulse, local Yokai Realm purification, player and enemy Ki
  exhaustion, life and Elixir recovery, melee-earned Anima, timed red-cue
  Burst Counter, first Enki Soul Core purification/attunement and one active
  ability use, Shrine recovery and ordinary-enemy respawn, grave recovery,
  mandatory Dark Realm source and its Shrine lock, Inner Shrine Key and Mezuki
  gate, mission-end interaction and successor-map state.
- Excluded: Gozuki and its optional cemetery shortcut, optional Kodama and
  Scampuss collection, side missions, later main missions, Twilight Missions,
  New Game Plus, DLC, Complete Edition extras, online graves and co-op,
  random loot optimisation, crafting, forging, levelling, skill-tree purchases,
  alternate Guardian Spirits, Yokai Shift, ranged combat, achievements and
  audiovisual evidence. Yokai Shift is visibly available when its Amrita gauge
  fills, but it is not required or demonstrated by this packet.
- Reproducible parameterisation: use the base PS4 product, English text, a
  clean solo New Game and the ordinary first-mission route. Activate the first
  Shrine; demonstrate high, mid and low stance, an attack followed by Ki
  Pulse, one guard and dodge, one red-cue Burst Counter and one purified local
  Yokai Realm patch. Take the first Enki Soul Core to a Shrine, purify and
  attune it, then spend Anima on its ability. Deliberately create and reclaim
  one grave before the boss. Cross the village, clear the larger Dark Realm's
  source Enki, take the Inner Shrine Key, pray at the newly usable Shrine,
  unlock the inner gate and defeat Mezuki. Exact weapon, Guardian Spirit,
  timings, damage, loot, Elixir count, enemy route and death location are
  parameters; the two written routes do not prove a unique path.
- Direct-play status: not conducted. No PS4, entitlement, install or save was
  available. Official Sony and Koei Tecmo pages establish the product and
  common rules. Two independent written route guides corroborate the opening
  mission, the source Enki, key and boss; current PS4 route parity and the
  mission-ending map state remain secondary-source observations. This is a
  rules reconstruction, not a claimed playthrough. No video or audio was
  opened, played, heard or analysed.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `NIO2-001` | The analysed SKU is the PS4 base product, not Complete Edition or DLC | Confirmed | Direct | High | P1 |
| `NIO2-002` | The last located PS4-specific update is `Ver 1.27`; no installed build was seen | Observation | Direct | Medium | P2, R1 |
| `NIO2-003` | Three stances change the weapon's attack form; attack, dash and evasion spend automatically recovering Ki | Confirmed | Direct | High | P3, P4 |
| `NIO2-004` | Timed post-attack Ki Pulse restores Ki and purifies a local Yokai Realm patch | Confirmed | Direct | High | P3, P4 |
| `NIO2-005` | Melee builds Anima, which pays for red-cue Burst Counter and attuned Yokai abilities | Confirmed | Direct | High | P3, P4 |
| `NIO2-006` | A Soul Core is purified and attuned at a Shrine before its ability is usable | Confirmed | Direct | High | P3, P4 |
| `NIO2-007` | Shrine prayer restores life and supplies and respawns ordinary enemies | Confirmed | Direct | High | P3, P4 |
| `NIO2-008` | Death leaves one grave holding Amrita and Guardian Spirit; a second death before recovery destroys the earlier Amrita and unpurified cores | Confirmed | Direct | High | P4 |
| `NIO2-009` | The first mission's mandatory Dark Realm disables its Shrine until the source Enki is defeated; the adjacent body holds the Inner Shrine Key | Observation | Corroborated | Medium | P3, S1, S2 |
| `NIO2-010` | Mezuki is the first mission's guardian; defeating it and interacting with the ending glow returns to a successor mission selection | Observation | Corroborated | Medium | P5, S1, S2 |
| `NIO2-011` | No direct PS4 run, terminal or reload check was possible | Confirmed | Direct | High | R1 |

## Basic data

- Origin: Team Ninja / Koei Tecmo; Sony Interactive Entertainment published
  the North American PS4 base product on 2020-03-13.
- Physical or platform form: PS4 digital base SKU, one offline fresh New Game
  through the first main-mission map settlement.
- Mechanical families: tactical forecast and counterplay; real-time system
  pressure; ordered dependency sequencing.
- Primary official sources, checked 2026-09-18:
  - **[P1]** [PlayStation base-product listing](https://store.playstation.com/en-us/product/UP9000-CUSA15532_00-NIOH2NA000000000),
    for exact PS4 product, publisher and edition boundary.
  - **[P2]** [Koei Tecmo official update index](https://www.gamecity.ne.jp/nioh2/update.html),
    for the last located PS4-specific `Ver 1.27` notice; later listed PC
    patches are not claimed for this console.
  - **[P3]** [Sony's March 2020 opening-hours guide](https://blog.playstation.com/?p=222129),
    for Ki, stances, Ki Pulse, red Burst cue, Anima, first Enki core, Dark
    Realm, Shrine and base-release context. Embedded video was not opened.
  - **[P4]** [Koei Tecmo official PS4 control page](https://www.gamecity.ne.jp/manual/t2wNiSht/ps/usa/2000.html)
    and [How to Play page](https://www.gamecity.ne.jp/manual/t2wNiSht/ps/usa/4000.html),
    for the controller action set, gauges, map progression, Soul Core
    attunement, Shrine and grave rules. The manual's Complete Edition header
    is not used as an edition claim for this base-game packet.
  - **[P5]** [Sony opening-level report](https://blog.playstation.com/2019/09/11/mythical-yokai-abound-in-new-nioh-2-gameplay-trailer/),
    for Village of Cursed Blossoms and Mezuki as its first-level boss.
- Corroborating written routes, checked 2026-09-18:
  - **[S1]** [PowerPyx first main-mission guide](https://www.powerpyx.com/nioh-2-the-village-of-cursed-blossoms-walkthrough/),
    for the first mission, Dark Realm source, Inner Shrine Key, Mezuki and
    mission-ending interaction.
  - **[S2]** [Game of Guides first mission](https://video-game-guide-walkthrough.supersoluce.com/solution/nioh-2-guide-walkthrough/nioh-2-main-missions/the-village-of-cursed-blossom/),
    an independent written route confirming the Enki, key, Shrine and Mezuki.
- **[R1]** Local preflight found no PS4 hardware, entitlement, install, save or
  captured version; no audiovisual evidence was used.

## Mechanical decomposition

### Actions

- Reuse `ACT-008` for traversal, `ACT-161` for ordinary attacks, `ACT-190`
  and `SYS-380` for an attuned Soul Core ability, `ACT-200` for Elixir use,
  `ACT-224` for Shrine prayer, `ACT-249` for grave recovery, `ACT-419` for a
  zero-Ki grapple, `ACT-429` for red-cue Burst Counter, `ACT-436` for
  Ki-priced dodge, `ACT-437` for held guard and `ACT-438` for lock-on.
- New `ACT-459` selects high/mid/low stance during live combat. New
  `ACT-460` commits the post-attack Ki Pulse within its visible interval.
  Counter type and Soul Core effect are parameters, not separate commands.

### System behaviours and constraints

- Reuse `SYS-215` for live combat, `SYS-364` for Shrine reset, `SYS-397` for
  melee-earned Anima spent on active effects, `SYS-399` for checkpoint death
  and the single recoverable grave, `SYS-409` for enemy Ki-break opening,
  `SYS-578` for life and `SYS-798` for one Ki reserve pricing offence and
  defence. `CON-282` owns the key and boss route, `CON-589` the limited
  zero-Ki grapple opening, and `CON-604` exhausted defensive legality.
- New `SYS-868` applies the selected stance's attack speed, reach and
  commitment; `SYS-869` converts a timed Ki Pulse into refund and nearby
  patch purification; `SYS-870` weakens Ki recovery, strengthens Yokai and
  locks Shrine access in a Dark Realm until its source falls; `SYS-871`
  purifies and attunes an acquired Soul Core at a Shrine. `CON-636` requires
  sufficient Anima for Burst Counter or a Soul Core ability. The Ki Pulse
  post-attack window is part of `ACT-460`, not a free anytime refill.

### Information, objective and time

- `INF-119` exposes personal life, Ki, Anima, stance and attuned skills;
  `INF-318` the Mezuki boss health; new `INF-342` exposes enemy Ki and the
  red burst cue before a counter commitment. `OBJ-080` owns Mezuki defeat
  followed by the successor-map threshold. `TIM-003` owns continuous combat
  and autonomous enemies while the player acts.

## Reproducible transitions

| Before | Player action | Bounded resolution | Claim |
|---|---|---|---|
| First mission, live Ki and selected stance | Strike, switch stance, time Ki Pulse | The attack spends Ki; stance reshapes the next move; Pulse refunds the recoverable share | `NIO2-003`, `NIO2-004` |
| Local Yokai Realm patch persists | Pulse after a nearby attack | The patch purifies along with the Ki refund | `NIO2-004` |
| Hostile flashes red, Anima is sufficient | Time Burst Counter | The incoming burst is interrupted and enemy Ki is pressured | `NIO2-005` |
| Enki core is carried but not attuned | Pray, purify and attune it; later trigger its ability | The skill becomes available and spends Anima when used | `NIO2-006` |
| Life reaches zero after a Shrine | Return and touch the grave | Amrita and Guardian Spirit return; a second death before recovery would erase the earlier stock | `NIO2-008` |
| Large Dark Realm covers inner Shrine | Defeat source Enki, take key, open gate | Realm clears, Shrine becomes usable and Mezuki route opens | `NIO2-009` |
| Mezuki encounter is live | Deplete its life, then interact with ending glow | Mission settles and successor selection appears on the map | `NIO2-010` |

## Strategic and experiential structure

The same Ki reserve pays for offence and survival; each attack creates a short
chance to recover part of that expense instead of waiting passively. Stance
selection changes the next commitment, while a red burst cue invites an
Anima-priced response that also attacks the opponent's Ki. Dark Realm pressure
slows the ordinary way back to readiness and turns its source into a local
access gate. A death does not erase the mission, but it moves unbanked Amrita
into a recoverable mark that a second death can destroy.

## Replay and variation

Weapon, Guardian Spirit counter form, exact damage, Ki values, drops, optional
shortcuts and route timing vary without changing this packet's causal owners.
The first Enki core and the larger Dark Realm source are separately located;
neither optional Gozuki nor online help is required.

## Adjacent systems and history

Dark Souls III shares Ki-like exertion, Shrine-like rest and a death mark, but
does not offer stance switching, post-attack reserve refund, a melee-earned
Anima counter or a Dark Realm source that locks a Shrine. Sekiro's Posture
break is not Nioh's Ki gauge, and its in-place Resurrection is absent here.
No older signature or definition is changed solely to force a closer match.

## Normalised genome

| Type | Active gene IDs | Parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-161`, `ACT-190`, `ACT-200`, `ACT-224`, `ACT-249`, `ACT-419`, `ACT-429`, `ACT-436`, `ACT-437`, `ACT-438`, `ACT-459`, `ACT-460` | route, weapon, stance, response and recovery |
| System Behaviour | `SYS-215`, `SYS-364`, `SYS-380`, `SYS-397`, `SYS-399`, `SYS-409`, `SYS-578`, `SYS-798`, `SYS-868`, `SYS-869`, `SYS-870`, `SYS-871` | Ki, Anima, Realm, Shrine, grave and core |
| Constraint | `CON-282`, `CON-589`, `CON-604`, `CON-636` | route, opening, reserve and ability eligibility |
| Information | `INF-119`, `INF-318`, `INF-342` | gauges, boss life, cue and enemy Ki |
| Objective | `OBJ-080` | Mezuki and successor map |
| Time | `TIM-003` | live combat |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `298` (`GAME-0001`–`GAME-0298`).
- Exact genome matches: none.
- Tied near matches: `GAME-0262` — DARK SOULS™ III (`19 / 41 = 0.463415`).
- Supported combination subsets: none.
- Scan date: 2026-09-18.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0262` — DARK SOULS III | `ACT-008`, `ACT-161`, `ACT-200`, `ACT-224`, `ACT-249`, `ACT-436`, `ACT-437`, `ACT-438`, `SYS-215`, `SYS-364`, `SYS-399`, `SYS-578`, `SYS-798`, `CON-282`, `CON-604`, `INF-119`, `INF-318`, `OBJ-080`, `TIM-003` | Both spend one recovering reserve across attack and defence, rest at a respawning checkpoint, reclaim one death-currency mark and defeat a guardian to cross a route threshold. Nioh 2 adds selectable weapon stances, a post-attack Ki refund, melee-earned Anima shared by a red-cue counter and a purified Soul Core ability, plus a source-bound Dark Realm that disables a Shrine. DARK SOULS III instead has its distinct equipment-load and sealed phase-shifting guardian rules. | Near, `0.463415` |

## Taxonomy impact

- New genes: `ACT-459`–`ACT-460`, `SYS-868`–`SYS-871`, `CON-636` and
  `INF-342`. Earlier signatures and definitions remain unchanged.
- No combination is proposed before exact strict-subset validation.

## Negative results

- Reject `SYS-848`: Nioh death returns to a Shrine and leaves a grave; it
  does not offer Sekiro's charged in-place Resurrection.
- Reject `ACT-425`: Burst Counter is a form-dependent yokai response to a red
  cue, not an equipped-weapon parry. Reuse the prompted-counter owner instead.
- Exclude Yokai Shift and levelling because neither is needed between this
  entry and terminal; their visible gauges do not by themselves add actions.

## Delta summary

## New facts

- [Observation | Corroborated | Medium] `NIO2-001`–`NIO2-011` bound the base
  PS4 first mission, its live resource loop, gate and successor state.

## New genes

- [Observation | Direct | High] Eight portable owners isolate stance choice
  and resolution, timed Ki recovery, Dark Realm pressure, Soul Core
  attunement, Anima legality and enemy cue information.

## New combinations

- [Observation | Corroborated | Medium] None proposed without a reviewed
  recurring proper-subset interaction.

## Taxonomy changes

- None; generic earlier definitions transfer without signature revisions.

## Inferences

- [Strong Pattern | Corroborated | Medium] A completed attack can fund its
  successor through Ki Pulse, but Realm pressure makes that timing and Anima
  counter choices more consequential than passive retreat alone.

## Open questions

- The precise locally installed PS4 build, current offline route parity and
  exact mission-end retention require a lawful direct console reproduction.

## Contradictions

- None established within the bounded base-game packet.

## New questions

- Does a later Yokai Shift packet require a separate transformation economy
  beyond this opening mission's Ki/Anima loop?

## Next recommended game

- [Hypothesis | Limited | Medium] `GAME-0300` Overcooked! 2 on Switch, the
  next selected exact-platform unit after this packet passes all gates.
- Optimisation criterion: test whether a short cooperative kitchen changes
  control, timing and delivery ownership relative to solo live combat.
- Expected information gain: jointly paced orders and bottlenecks rather than
  another personal combat reserve.

## Why this game

- [Hypothesis | Corroborated | Medium] Nioh 2 stresses the reusable exertion,
  checkpoint and grave owners while adding a stance and Ki Pulse layer that
  earlier Souls-like signatures cannot express.

## Confidence and unresolved questions

- High for the PS4 product and official shared mechanics; Medium for the
  two-route reconstruction and last located PS4 update; no claim of direct
  play, terminal observation or reload. A console run should record its
  displayed build, route, death and settlement before raising route confidence.
