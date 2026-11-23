---
game_id: GAME-0572
slug: neon-white
game_title: Neon White
analysis_status: reviewed
reviewed: 2026-11-20
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-161
    - ACT-776
  system:
    - SYS-037
    - SYS-1679
    - SYS-1680
    - SYS-369
    - SYS-711
  constraint:
    - CON-402
    - CON-835
  information:
    - INF-545
  objective:
    - OBJ-314
  time:
    - TIM-003
---

# Game: Neon White

Use the canonical [vocabulary and signature rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
The same card covers the next shot and the next high landing. Spending it
changes both the route and the tools available for that route.

## Analysis scope

- Version / ruleset: full English North American Nintendo Switch eShop release,
  launched 16 June 2022. Use the single-player campaign, ordinary controls and
  the launch-era rule evidence below. Exact installed build not verified.
- Structured analysis target: PLAT-NINTENDO-SWITCH in knowledge/platforms/games.json.
- Entry: clear Cascade in Rebirth on a fresh local campaign, then begin the
  first play of stage 1-5, Elevate, from its authored start. Use the starting
  melee option to open the first card chest and begin with no carried firearm
  cards from a previous stage.
- Primary decision loop: move and aim in real time, collect Elevate cards,
  and decide when to fire a shot and when to spend a whole copy to gain height.
  Use world pickups and dropped cards to keep both combat and traversal
  possible. Finish the whole stage.
- Positive exit: remove the five required demons, then touch the opened exit
  and read the first valid time and medal. Finishing slowly affects the award,
  while clearance and exit contact settle completion.
- Negative exit: death ends the current attempt. Retrying restores the stage
  from its start. The Switch minus input also restarts an unfinished attempt
  at the same origin and discards the transient card state and progress.
- Included: the complete first-clear route, ordinary jump and Elevate boost,
  starting chest, hostile card drop and contact acquisition, directed attacks,
  held-card capacity, live timer, demon clearance, exit, initial medal and
  restart. Exact ammunition accounting across duplicate cards, high-speed
  physics, enemy health and projectile timings remain unmeasured.
- Excluded: gift detours, ghosts, recorded hints and online scores on replays,
  cross-level rank and chapter unlocks, character stories, PS/PC editions,
  later card abilities and bonus stages. A later stage inventory also lists
  Purify. The standard Elevate route is evidenced directly; the exact
  availability and uses of that optional card on a native first visit remain
  outside the active signature. The first-clear endpoint is the whole level.
- Potential scoped modules: optional card routes and medal optimization on a
  version-verified replay, then deliberate routing around rank or gifts.
- Direct-play status: not conducted. Nintendo release metadata, director
  explanations, contemporary Switch play accounts and attributed route reports
  establish the model. No retail play or video/audio playback was performed.
  The exact demon breakdown comes from the later stage inventory. No PC medal
  threshold or exact patch version is claimed for Switch.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
| --- | --- | --- | --- | --- | --- |
| NW-001 | The native Switch single-system commercial download launched in North America on 16 June 2022 and supports US English. | Confirmed | Direct | High | P1 |
| NW-002 | The same ordinary Soul Card permits aimed ammunition-consuming fire and a separate discard. Discard spends a copy and activates its alternate effect. Elevate is a pistol whose discard adds an aerial boost. | Observation | Corroborated | High | P2, P3, R1, R3 |
| NW-003 | The starting chest and the first yellow demon at the top of the stairs provide Elevate copies. A jump and one discard reach a higher platform with a replacement pickup. Holding a second copy leaves one available after the first spend. | Observation | Corroborated | High | P3, R3 |
| NW-004 | Ordinary cards permit at most two distinct types and up to three copies per type. The reusable starting katana is separate from ordinary gun cards. | Observation | Corroborated | High | P3, R2, R4 |
| NW-005 | The stage requires clearing all demons before entering the exit. The later inventory identifies two Frogs and three Barnacles; only this inventory supplies the exact breakdown. | Observation | Corroborated | Medium | P2, R1, R5 |
| NW-006 | The documented Switch controls offer separate jump, fire, discard and quick restart inputs. An abandoned or failed attempt can return to the authored start, restoring local supplies and enemies. | Observation | Corroborated | Medium | R1, R2 |
| NW-007 | The running view displays the card and firing stock, an enemy counter and elapsed time. A valid finish independently receives a time grade. Bronze is a valid initial result. | Observation | Corroborated | High | R1, R2, R3 |
| NW-008 | Gifts are replay incentives introduced after valid completion. Later community figures distinguish Switch and PC times; an exact threshold is not established for the original native build. | Observation | Corroborated | Medium | P3, R1, R3, R5 |

## Basic data

- Angel Matrix / Annapurna Interactive. Native Nintendo Switch, North American
  commercial release, 16 June 2022.
- Families FAM-009 tactical forecast and counterplay and FAM-010 real-time
  system pressure.
- P1: [Nintendo’s US release and language listing](https://www.nintendo.com/us/store/products/neon-white-switch/).
  It names the publisher in both credit fields; director P3 supplies the
  creative team context.
- P2: [Ben Esposito’s director account of core rules](https://blog.playstation.com/?p=372564),
  1 December 2022. Common clearance and dual-use cards are corroborated on
  Switch by R1 and R2. Platform-specific DualSense functions are excluded.
- P3: [Director interview on card capacity and level design](https://www.gamedeveloper.com/business/-neon-white-and-designing-for-player-creativity),
  Joel Couture interviewing Ben Esposito, 2023. Establishes the two-by-three
  capacity and alternate use, separates gifts after completion and describes
  route optimization. Its worked Godspeed chain is a different level.
- R1: [Donald Theriault’s native Switch play account](https://nintendoworldreport.com/review/60703/neon-white-switch-review),
  15 June 2022. Supports separate ZL, ZR, R and minus inputs, enemy clearance,
  exit, and the four ordinary medal grades.
- R2: [Nintendo Life’s native Switch review and stills](https://www.nintendolife.com/reviews/switch-eshop/neon-white),
  June 2022. Supports the melee fallback, stocked ranged cards and spend
  choices. Static screenshots support the visible state, with position on the
  screen treated as presentation.
- R3: [Matt Villei’s worked Elevate route](https://gameranx.com/features/id/321112/article/neon-white-how-to-get-all-gifts-in-mission-1-rebirth/),
  9 July 2022, Level 5. Uses a replay to reach a gift. The chest, first
  yellow-demon drop and higher main landing precede the gift detour. The
  first-clear reconstruction uses only that shared part of the route.
- R4: [MeriStation’s launch-period Nintendo Switch and PC play account](https://as.com/meristation/2022/06/29/analisis/1656529807_320025.html),
  30 June 2022. Reports the default katana and the specific Elevate pistol
  versus double jump trade-off.
- R5: [Community stage inventory](https://neonwhite.fandom.com/wiki/Elevate).
  Later inventory documents the demon count, card types and platform timing
  differences. Native first-clear details are marked limited where needed.
  Sources checked 2026-11-20.

## Mechanical decomposition

### Action Genes

- ACT-008 covers running and ordinary jump. ACT-161 covers directed attacks
  with the current melee tool or firearm. ACT-776 commits the alternate
  ability by spending one active card. Shooting can preserve a future
  discard while there is a copy left. Discard sacrifices what that copy
  offers as a weapon.
- Claim IDs: NW-002–NW-004, NW-006.

### System Behaviour Genes

- SYS-037 covers contact collection of cards. SYS-1680 is the fixed drop
  that places a card in the world before collection. SYS-1679 supplies the
  extra height from a spent Elevate. Burning a copy adds reach and decreases
  future ammunition and movement options from that copy.
- SYS-369 restores the authored start on retry. SYS-711 evaluates a valid
  elapsed result by fixed level medal grades.
- Claim IDs: NW-002, NW-003, NW-005–NW-007.

### Constraint Genes

- CON-402 governs exclusion from the terminal until the finite hostile
  set is empty. CON-835 governs carried card types and copies. The scoped
  route demonstrates duplicate Elevates. It does not require reaching both
  maxima or replacing a card after pickup overflow.
- Claim IDs: NW-003–NW-005.

### Information Genes

- INF-545 exposes the held card and ammunition, the remaining demons and
  elapsed time. The player can read what is still possible before spending.
- Claim ID: NW-007.

### Objective Genes

- OBJ-314 requires a full clear followed by reaching the end. It separates the
  complete level result from opening its terminal. The medal evaluates how
  quickly the player reached the terminal.
- Claim IDs: NW-005, NW-007.

### Time Genes

- TIM-003 covers movement, air time and enemy interactions on the live clock.
  The airborne window changes reachable actions while the player decides.
  The elapsed timer is evaluated at valid completion.
- Claim IDs: NW-003, NW-006, NW-007.

## Reproducible transitions

| State / precondition | Action or event | Observable transition | Boundary | Claims |
| --- | --- | --- | --- | --- |
| First visit, at the stage start | Strike the opening chest and take its card | One Elevate enters the inventory | Chest placement supplies the initial card, while contact collects it | NW-003 |
| Elevate held with usable ammunition | Aim and fire at the first yellow demon | A firing input spends ammunition and can defeat the demon | The discard input is a separate commitment | NW-002 |
| The first yellow demon is defeated | Reach the dropped card | A second Elevate copy can be held | Defeat produces the card before collection | NW-003 |
| Airborne after a normal jump with two Elevates | Discard one active copy | Upward impulse extends reach and leaves one held copy | A second boost requires another copy | NW-002, NW-003 |
| On the higher reachable platform | Take the fixed card | Replace the used copy | The next boost can be planned against the remaining enemies | NW-003 |
| Last required demon still present | Approach the exit | Clearance condition remains unmet | Timer alone cannot settle the stage | NW-005 |
| All five demons defeated | Reach the opened exit | First completion with elapsed time and a graded medal | The last kill alone does not finish the run | NW-005, NW-007 |
| Cards and enemies altered during an unfinished attempt | Press minus for restart | Fresh attempt at the same origin | Prior in-attempt picks and defeats do not carry forward | NW-006 |

## Strategic and experiential structure

- Spend as late as useful: use the current pistol on the next reachable demon
  before consuming the card for upward reach. A drop or fixed pickup changes
  which action can follow.
- Burning the last copy too soon can strand a later jump or a ranged attack.
  A second copy can protect one option while the other is spent.
- Faster routes still have to clear the full required set. Planning around
  both the inventory and terminal tracks a different skill from saving time
  with a faster input alone.

## Replay and variation

- Return to the same opening geometry and initial supplies after restart.
  Observe the last attempted card spend and choose a different place to jump,
  fire or collect on the next attempt. Layout stays fixed while timing and
  path depend on decisions. Later replay aids are outside the first clear.
- Claim IDs: NW-002, NW-003, NW-006–NW-008.

## Adjacent systems and history

- Rebirth introduces Purify in an earlier stage and emphasizes Elevate here.
  A different main route or later mixed-card stage can be reviewed with a
  separately authenticated native source set.
- Later versions and platform leaderboards have distinct comparison pools.
  No other release's exact threshold or hardware input mapping is imported.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
| --- | --- | --- |
| Action | ACT-008, ACT-161, ACT-776 | Movement and ordinary jump, shot, alternate discard |
| System Behaviour | SYS-037, SYS-1679, SYS-1680, SYS-369, SYS-711 | Contact acquisition, stage retry, time-grade thresholds, boost, fixed enemy drop |
| Constraint | CON-402, CON-835 | Clearance gate and held-card capacity |
| Information | INF-545 | Card, firing stock, enemy count and timer |
| Objective | OBJ-314 | Complete stage after clearance and exit contact |
| Time | TIM-003 | Live air, enemy and attempt timer |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `571` (`GAME-0001`–`GAME-0571`).
- Exact genome matches: none.
- Tied near matches: `GAME-0312` — ASTRO BOT (`5 / 24 = 0.208333`).
- Supported combination subsets: none.
- Scan date: 2026-11-20.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
| --- | --- | --- | --- |
| `GAME-0312` — ASTRO BOT | ACT-008, ACT-161, SYS-037, SYS-369 and TIM-003 cover direct movement, directed attack, physical acquisition, authored recovery and live timing. | Sky Garden uses held Inflate to rise and finishes at the glass boundary. Elevate spends a weapon option per boost and requires all demons cleared before exit. | Tied near: 5 / 24 = 0.208333 |

### Preserved research notes

- New genes: ACT-776, SYS-1679, SYS-1680, CON-835, INF-545 and OBJ-314.
- Classification result: New gene.

## Taxonomy impact

- [TAXONOMY_CHANGE_318](../../../research/taxonomy-changes/TAXONOMY_CHANGE_318.md)
  records the distinction between committing a card spend, gaining reach,
  acquiring a resource and closing the stage.

## Negative results

- The published walkthrough's later gift route does not imply a gift during
  the first clear. No exact original Switch medal threshold, ammo decrement
  across duplicate cards, enemy health or frame data could be verified.
- The current stage inventory names an optional Purify pickup. Its native
  first-visit availability and action are outside this scoped Elevate route.

## Delta summary

## New facts

- [Observation | Corroborated | High] NW-002–NW-007 identify the competing
  firing and movement uses of a held copy and the independent terminal.

## New genes

- [Observation | Corroborated | Medium] Six additions in taxonomy change 318.

## New combinations

- [Observation | Corroborated | High] No new combination proposed. Existing
  supported subsets are owned by the comparison section.

## Taxonomy changes

- [Observation | Corroborated | Medium] Predecessor definitions and signatures
  stay unchanged.

## New questions

- A version-verified Switch run can resolve exact card duplication and ammo
  behavior, optional first-visit routes, transition timing and medal thresholds.

## Next recommended game

- [Hypothesis | Limited | Medium] GAME-0573, Dungeon Keeper for DOS.
- Optimisation criterion: alternate platform and era. Compare one finite
  timed level with a dungeon operating under persistent resource pressure.
- Backlog impact: sixth Selection 046 unit.

## Why this game

- [Hypothesis | Limited | Medium] The stage isolates one understandable
  trade-off across the full run: firing may preserve a card for a jump,
  while the jump spends the same card and alters the next combat choice.
