---
game_id: GAME-0368
slug: dead-rising
game_title: Dead Rising
analysis_status: reviewed
reviewed: 2026-09-23
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-131
    - ACT-161
    - ACT-164
    - ACT-189
    - ACT-341
    - ACT-502
  system:
    - SYS-057
    - SYS-215
    - SYS-222
    - SYS-223
    - SYS-299
    - SYS-379
    - SYS-1001
    - SYS-1002
  constraint:
    - CON-210
    - CON-282
    - CON-285
    - CON-597
    - CON-621
  information:
    - INF-067
    - INF-073
    - INF-115
    - INF-119
    - INF-125
    - INF-376
  objective:
    - OBJ-155
  time:
    - TIM-003
    - TIM-007
---

# Game: Dead Rising

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Frank, Jeff,
Natalie, Brad, Carlito, Parkview Mall, PP and the named case are carrier
parameters, not gene names.

## Analysis scope

- Version / ruleset: Capcom's licensed English Dead Rising release for Xbox
  One dated 2016-09-13, the original game's 72 Hour Mode. Capcom identifies
  this re-release separately from the original Xbox 360 game; the latter's
  official manual supplies rules, corroborated against the 2016 Xbox product
  and Capcom's Xbox One save guidance. No exact installed patch or executable
  hash is claimed. The 2024 Deluxe Remaster and sequels are excluded.
- Entry: a fresh 72 Hour Mode start without carried-over level or status.
  Helicopter photography and the unavoidable entrance collapse precede first
  ordinary Security Room control. The fixed route begins there with the
  starting camera and available mall items.
- Primary decision loop: inspect the wristwatch, active Case and Scoop time
  bands, nearby threats, life and carried slots; decide whether an optional
  rescue and photograph can be completed before the mandatory case; move
  through the persistent mall, equip or consume scarce carried objects, frame
  and take a ready camera shot, call or point escorted civilians toward a
  reachable route, then confront the case target with chosen weapon and food
  resources before its deadline. Return to an eligible save fixture and check
  the closed case, next case and retained slot.
- Fixed route: leave the Security Room for the rooftop; speak to Jeff, bring
  him to Natalie, photograph their reunion while the opportunity is present,
  recruit both and deliver them through the vent to the Security Room. Follow
  Jessie's Case 1-1 handoff through Paradise Plaza and Leisure Park to the Food
  Court for Case 1-2, Backup for Brad. Use a picked-up improvised object on
  the mall route, then the provided handgun against Carlito, replacing an
  exhausted firearm when its current state requires it.
  Defeat the required encounter, observe Case 1-2 close and Case 1-3 become
  active, then reach the designated restroom in Al Fresca Plaza's Flexin'
  gym and write a manual save. Exact optional object, shots, PP and remaining
  clock values are parameters, not asserted constants.
- Positive terminal: Jeff and Natalie have been delivered, the documented
  photo opportunity has been used, Case 1-2 is closed after the Brad/Carlito
  encounter, Case 1-3 is available, Frank remains controllable and the
  resulting state is retained at the designated save point. The survivor and
  photo tasks are fixed trace commitments, not mandatory product rules.
- Negative terminal: Frank dies without a successful reload; the required
  Case expires before resolution, leaving the main evidence trail closed;
  either fixed-route survivor is lost; or play stops before the case and save
  boundary. A missed Scoop or lost photograph alone need not end 72 Hour Mode,
  but fails this fixed trace. Case expiry does not mean the 72-hour world clock
  itself instantly terminates.
- Included: rooftop recruitment and local escort; photograph framing,
  readiness, battery and PP scoring; finite item slots, ordinary pickups,
  breakable improvised weapons, food recovery, the handgun and compatible
  firearm state; live zombie pursuit and Food Court combat; displayed current
  time, case/scoop route and deadline bands; ordered case handoff, closure and
  successor; manual save at a specified fixture and later branchable load.
- Excluded: continuing Case 1-3 or the full 72-hour rescue; later Scoops,
  Psychopaths, survivor counts, endings, Overtime and Infinity modes; New
  Game with previously carried level, optional photo chains with Kent, weapon
  recipes, blended juice effects, vehicles, achievements, infinite firearm
  supply as a general rule, exact zombie population, DLC costumes and 2024
  Deluxe Remaster conveniences or changes.
- Direct-play status: no licensed Xbox One application, controller trace,
  save, screenshot, video or audio was obtained or inspected. The publisher's
  original manual and edition-specific product/support pages establish the
  rules; two independent written opening routes corroborate Jeff/Natalie,
  Case 1-2 and the available save point. The local source model, if present,
  tests only the claimed transition predicates and is not game execution.
- Scope rationale: the first closed combat Case followed by a manual save is
  the smallest reproducible successor boundary that joins live deadline
  pressure, optional civilian and photographic opportunities, finite carried
  tools and persistent mall state without pretending to complete 72 Hour Mode.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| DR-001 | The licensed Xbox One re-release is dated 2016-09-13 and distinct from the later Deluxe Remaster | Confirmed | Direct | High | P1, P2 |
| DR-002 | A fresh 72 Hour Mode has a running mall clock, one save slot, eligible restroom/Security Room saves and optional retained level carryover only if earlier data exists | Confirmed | Direct | High | P3, P4 |
| DR-003 | Wristwatch Scoop bands and Case panels disclose current opportunities; a missed Case becomes expired rather than closed | Confirmed | Direct | High | P3 |
| DR-004 | A ready camera shot consumes battery, waits for processing and awards PP from noteworthy framing; the view displays target and PP indicators | Confirmed | Direct | High | P3 |
| DR-005 | Inventory slots increase with level; PP awards from qualifying actions cross level thresholds | Confirmed | Direct | High | P3 |
| DR-006 | The early rooftop route can recruit and return Jeff and Natalie, and their reunion offers a photograph | Observation | Corroborated | High | S1, S2 |
| DR-007 | Case 1-2 leads from Jessie's handoff to Brad's Food Court fight with Carlito; its completion opens Case 1-3 | Observation | Corroborated | High | S1, S2 |
| DR-008 | A reachable Flexin' restroom save point exists immediately after the Case 1-2 fight route | Observation | Direct | Medium | S2 |
| DR-009 | The bounded packet's fixed terminal requires optional photo/rescue, closed Case 1-2 and a retained manual save, not the whole 72-hour ending | Strong Pattern | Corroborated | High | DR-002–DR-008 |
| DR-010 | The scoped handgun has finite shots, but no manual ammunition-transfer or reload action is evidenced; an exhausted weapon is replaced | Observation | Corroborated | Medium | P3, S1 |

## Basic data

- Release / origin: Capcom; original game first released on Xbox 360 in 2006,
  Xbox One re-release on 2016-09-13.
- Platform or physical form: licensed English Xbox One release, one local
  player on a controller; no executable or installed patch inspected.
- Puzzle family: real-time system pressure, tactical forecast and counterplay,
  ordered dependency sequencing. The camera and civilian opportunities
  compete with the authored Case while the world clock remains live.
- Primary and first-party sources, checked 2026-09-23:
  - **[P1]** [Xbox Dead Rising product page](https://www.xbox.com/en-US/games/store/dead-rising/BZV7W98B3XN4),
    for the Xbox One identity and 2016-09-13 release date.
  - **[P2]** [Capcom tenth-anniversary re-release note](https://news.capcomusa.com/lets/browse/dead-rising-10th-anniversary-edition),
    for the re-release boundary; its 1080p/60fps presentation note is not
    taken as proof of changed mechanics.
  - **[P3]** [Capcom original Xbox 360 manual](https://static.capcom.com/deadrising/manuals/X360_Manual.pdf),
    for 72 Hour Mode, camera, clock, Cases, PP, inventory and saving. It is a
    prior-platform rules source, not an Xbox One patch manifest.
  - **[P4]** [Capcom Xbox One save support](https://www.capcom.co.jp/support/faq/platform_xboxone_deadrising_0135809.html),
    for restroom and Security Room bed saving in the re-release.
- Independent written route sources, checked 2026-09-23:
  - **[S1]** [GamesRadar opening and Case 1-2 route](https://www.gamesradar.com/dead-rising-walkthrough/),
    for Jeff, Natalie, the photo, Brad/Carlito and next Case.
  - **[S2]** [PortForward Case 1 walkthrough](https://portforward.com/games/walkthroughs/Dead-Rising/Case-1.htm),
    for the Case 1-2 close and Flexin' save point; its discretionary advice is
    not treated as a mandatory rule.

## Mechanical decomposition

### Action Genes

- ACT-008 moves Frank across reachable rooftop, plaza, park and Food Court
  routes. ACT-341 operates doors, rescue conversations and a save fixture.
- ACT-131 consumes carried food into immediate recovery; ACT-164 selects the
  current carried object; ACT-161 directly strikes with an improvised melee
  object or aimed firearm. An exhausted gun is replaced, not reloaded.
- ACT-189 addresses a recruited survivor with a reachable goal point. New
  ACT-502 commits a photograph of the current camera frame while charged and
  ready; zoom and framing without a shot are not separate genes.

### System Behaviour Genes

- SYS-057 routes perceived zombies toward Frank or civilians; SYS-215 resolves
  direct attacks and damage. SYS-222 accepts eligible pickups into available
  slots, while SYS-223 wears out a used improvised tool.
- SYS-1001 scores the captured scene and credits qualifying PP. SYS-299 turns
  accrued PP thresholds into level/slot progression; it does not decide a
  photograph's content score. New SYS-1002 routes a temporarily recruited
  civilian through follow/goal movement and settles arrival or loss.
- SYS-379 advances the authored Case state from its completed encounter.

### Constraint Genes

- CON-210 bounds carried objects by available slots. CON-285 requires a
  compatible held firearm and remaining ammunition for its shot.
- CON-282 orders Jessie's handoff, the Food Court fight and next Case. CON-597
  closes an offered Case/Scoop opportunity when its live authored interval
  expires; it does not impose a global instant game-over at 72 hours.
- CON-621 limits a manual save to an eligible designated fixture.

### Information Genes

- INF-073 shows the current carried item and slots; INF-119 shows life and PP
  level; INF-115 exposes nearby visible/audible threats.
- INF-125 shows current Case and route, while INF-067 exposes current time,
  relevant deadline bands and task state. New INF-376 exposes camera battery,
  processing readiness and subject/PP framing cues before a shot.

### Objective and Time Genes

- OBJ-155 resolves the bounded first combat Case into next-Case control and a
  retained save. TIM-003 keeps mall threats and opportunities advancing during
  ordinary play; TIM-007 permits a later load from the manually retained state
  and a different continuation. Pausing a menu is not the tactical command
  radial of TIM-027.

## Reproducible transitions

| Before | Action | Bounded resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Fresh Security Room control | Enter rooftop, speak to Jeff and reach Natalie | Both join and can be led back through the vent | optional escort activation | DR-006 |
| Jeff and Natalie reunite; camera ready | Frame the reunion and take a shot | Battery is spent, the scene receives PP and processing must clear before another shot | photo action, scoring and feedback | DR-004, DR-006 |
| Both civilians follow near the vent | Cross to Security Room with both in range | Their arrival is credited; leaving one behind does not satisfy the fixed route | escort settlement | DR-006 |
| Jessie has handed off Case 1-1 | Reach Brad before Case 1-2 expires | Food Court encounter becomes the active ordered gate | deadline and case route | DR-003, DR-007 |
| Carrying one improvised tool and finite food | Strike or consume each when legal | Tool durability or life changes; slots constrain what remains carried | resources and live pressure | DR-005 |
| Carlito is reachable and Frank is armed | Aim, fire, recover and continue the fight | Encounter closes Case 1-2 and offers Case 1-3 | combat and successor | DR-007 |
| Case 1-2 closed; Frank controls the next segment | Reach Flexin' eligible restroom and save | Retained state can be loaded for a different continuation | manual save terminal | DR-002, DR-008 |
| An offered Case passes its deadline unfinished | Continue the mall clock | That evidence path expires rather than becoming completed | local expiration, not 72-hour termination | DR-003 |

## Strategic and experiential structure

- The photo is worth PP only if the subject is framed and the camera has
  battery/readiness. Stopping to frame it uses live time that could instead go
  toward Brad's Case; rescue adds a routing cost and possible civilian loss.
- Finite carried slots make food, camera-independent weapons and improvised
  objects compete. Broken objects are replaceable mall resources, not a
  permanent equipment build. PP can improve capacity but does not stop time.
- The clock and Case panel provide time bands rather than perfect future
  enemy positions. A safe manual save requires reaching its location.

## Replay and variation

- The fixed trace deliberately rescues Jeff/Natalie and photographs their
  reunion. Skipping either is valid 72 Hour Mode play but a different packet.
- Alternate weapons, different shot scores, missed Scoops, a different Case
  route, prior-level carryover and later survivor chains are not inferred from
  this trace. Reloading a retained state can branch the history, but no
  in-world rewind power exists.

## Adjacent systems and history

- Resident Evil 2 (2019 remake) shares direct combat, finite inventory and a
  fixture-gated save, but its scoped police-station route has no live Case/Scoop
  competition or PP photograph score.
- The Long Dark's Hopeless Rescue has a terminal overall timer, unlike this
  packet's separately expiring main-story and side opportunities inside a
  still-running 72-hour world.
- Half-Life (1998) has a temporary following ally, but this packet must
  deliver noncombat civilians through a safe-room boundary under a clock.

## Normalised genome

| Type | IDs | Boundary |
|---|---|---|
| Action | ACT-008, ACT-131, ACT-161, ACT-164, ACT-189, ACT-341, ACT-502 | traverse, heal, fight, equip, order, interact and photograph |
| System | SYS-057, SYS-215, SYS-222, SYS-223, SYS-299, SYS-379, SYS-1001, SYS-1002 | pursuit, damage, pickup, wear, PP, case, photo and escort |
| Constraint | CON-210, CON-282, CON-285, CON-597, CON-621 | slots, case order, ammunition, deadline and save location |
| Information | INF-067, INF-073, INF-115, INF-119, INF-125, INF-376 | task clock, carried state, threats, health, route and camera |
| Objective | OBJ-155 | close first combat Case, enter successor and retain save |
| Time | TIM-003, TIM-007 | live mall time and branchable saved history |

The packet has 29 genes: 25 reused boundaries and four new ones. The mall,
camera model, survivor names and exact case times remain parameters.

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `367` (`GAME-0001`–`GAME-0367`).
- Exact genome matches: none.
- Tied near matches: `GAME-0361` — Fallout: New Vegas (`16 / 40 = 0.400000`).
- Supported combination subsets: none.
- Scan date: 2026-09-23.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0361` — Fallout: New Vegas | `ACT-008`, `ACT-161`, `ACT-164`, `ACT-341`, `SYS-057`, `SYS-215`, `SYS-379`, `CON-282`, `CON-285`, `INF-073`, `INF-115`, `INF-119`, `INF-125`, `OBJ-155`, `TIM-003`, `TIM-007` | Both use live movement, weapons, authored tasks and retained choices. New Vegas's fixed Courier build and Goodsprings faction outcome differ from Dead Rising's timed Case/Scoop competition, photograph scoring, vulnerable civilian delivery and fixture-gated save. | Near, `0.400000` |

## Taxonomy impact

- TAXONOMY_CHANGE_107 adds ACT-502, SYS-1001, SYS-1002 and INF-376 without
  changing an earlier signature or lifecycle. No combination is inferred from
  one new carrier alone.

## Negative results

- The original Xbox 360 manual is not proof of exact Xbox One performance,
  input glyphs or later patch values. No Xbox One executable was inspected.
- A missed Case closes the main evidence trail but must not be conflated with
  an instant 72 Hour Mode world termination. An optional Scoop or photograph
  may expire without the same consequence.
- ACT-183 was rejected after checking the original controller manual and the
  opening route: neither supplies a player reload action for the scoped
  handgun. Its finite rounds remain CON-285; replacing the weapon is handled
  by ordinary selection and pickup, not an invented ammunition transfer.
- The route ends before Case 1-3 completion; later bosses, rescues, ending
  grades and game-wide photo chains are not admitted.

## Delta summary

## New facts

- The first optional rescue and camera reward compete with a mandatory Case
  on one live mall clock before a player-chosen save fixture.

## New genes

- ACT-502 — commit a photograph of the current camera frame.
- SYS-1001 — award content-sensitive photographic PP.
- SYS-1002 — route and settle a recruited civilian escort.
- INF-376 — expose camera readiness and scoring cues.

## New combinations

- None; one new carrier is not recurrence evidence.

## Taxonomy changes

- One additive decision; no rename, merge, deprecation or earlier signature
  rewrite.

## New questions

- Direct play could pin an exact installed Xbox One build and test camera
  battery/processing thresholds and the precise Case expiry screen.

## Next recommended game

- GAME-0369 Carcassonne, the final reserved unit in this horizon.

## Why this game

- It tests how optional visual scoring and civilian rescue compete against a
  case deadline and finite carried resources, without reducing the whole game
  to a single global countdown.

## Localisation review

- The canonical English scope and claim ledger were frozen before Ukrainian
  presentation. Official product and mode titles remain Latin labels where
  needed; the complete Ukrainian field review is recorded in the acceptance
  checkpoint.
