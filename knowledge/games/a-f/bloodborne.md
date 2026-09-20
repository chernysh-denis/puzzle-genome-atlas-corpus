---
game_id: GAME-0308
slug: bloodborne
game_title: Bloodborne™
analysis_status: reviewed
reviewed: 2026-09-19
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-161
    - ACT-200
    - ACT-224
    - ACT-249
    - ACT-419
    - ACT-436
    - ACT-438
    - ACT-459
  system:
    - SYS-215
    - SYS-364
    - SYS-399
    - SYS-578
    - SYS-778
    - SYS-798
    - SYS-799
    - SYS-832
    - SYS-852
    - SYS-868
  constraint:
    - CON-282
    - CON-286
    - CON-352
    - CON-354
    - CON-604
  information:
    - INF-119
    - INF-142
    - INF-295
    - INF-318
  objective:
    - OBJ-080
  time:
    - TIM-003
---

# Game: Bloodborne™

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Hunter, Saw
Cleaver, Hunter Pistol, Blood Vial, Quicksilver Bullet, Blood Echo, Lantern,
Father Gascoigne and Oedon Tomb Key are parameters or product labels, not gene
names.

## Analysis scope

- Version / ruleset: Sony Interactive Entertainment's original English PS4
  base product, fresh offline single-player game, checked 2026-09-19. The
  installed patch, console, entitlement and save were not available. The Old
  Hunters, online notes, spectres, summoning, invasions and PS5 compatibility
  are excluded.
- Structured analysis target: original PS4 base product, fresh offline route;
  see `GAME-0308` in
  [`knowledge/platforms/games.json`](../../platforms/games.json).
- Setup-only predecessor: create a Hunter with the fixed Lone Survivor origin.
  The unarmed clinic encounter introduces defeat and Hunter's Dream, where the
  fixed Saw Cleaver and Hunter Pistol are selected. Character appearance and
  the first unavoidable transition are setup, not separate genes.
- Entry: begin at the first ordinary Central Yharnam Lantern control with the
  Saw Cleaver and Hunter Pistol equipped, before opening the first route
  shortcut. Record health, stamina, Blood Echoes, Blood Vials and Quicksilver
  Bullets. Do not claim an exact installed-build inventory quantity.
- Primary decision loop: read local attack wind-ups and geometry; walk, run,
  lock onto one reachable enemy, spend the shared stamina bar on Saw Cleaver
  attacks and evasive movement, then create distance while stamina refills.
  Switch the same trick weapon between its compact and extended forms to trade
  speed for reach. After eligible damage, decide whether to retaliate before
  the recoverable-health window drains or spend a finite Blood Vial. Fire the
  Hunter Pistol during an eligible hostile attack to interrupt it and expose a
  short visceral opportunity, then close distance and commit the follow-up.
  Open authored gates or lifts as persistent shortcuts, use the Lantern path
  as the recovery anchor, and cross Central Yharnam to Father Gascoigne.
- Positive terminal: defeat Father Gascoigne, receive the Oedon Tomb Key,
  light the new Tomb of Oedon Lantern and use the opened rear gate and path
  into the Cathedral Ward successor. Stop at first ordinary successor control.
  No quit/reload persistence is claimed.
- Negative terminal: zero health returns the Hunter to the last available
  Lantern state while carried Blood Echoes remain at the death location or on
  an eligible enemy. Reaching that mark restores them; dying again first loses
  the earlier stock permanently. A failed boss attempt, an unlit post-boss
  Lantern or possession of the key without crossing the gate is not success.
- Included: direct third-person traversal; lock-on; light and strong close
  attacks; evasive movement; the two Saw Cleaver forms; stamina spending and
  automatic recovery; real-time damage and defeat; rally banking, retaliation
  recovery and timed expiry or replacement; finite Blood Vial healing;
  Quicksilver-Bullet firearm timing; stagger and visceral follow-up; local
  hostile cues; health, stamina, ammunition, items and Blood Echoes display;
  Lantern return; ordinary-enemy repopulation; persistent physical shortcuts;
  one recoverable death-currency mark; Father Gascoigne's later beast phase;
  mandatory-boss defeat, key award and successor access.
- Excluded: Cleric Beast because it is optional; levelling, weapon
  fortification, Blood Gems and shopping; Tiny Music Box side quest; armour
  optimisation, Molotovs and optional consumables; NPC quests; Chalice
  Dungeons; The Old Hunters; co-op, invasions, notes and spectres; all later
  bosses and areas; New Game Plus; other releases and platform parity.
- Reproducible parameterisation: use a fresh English PS4 base-game offline
  save, Lone Survivor, Saw Cleaver and Hunter Pistol. From Central Yharnam,
  open at least one return shortcut, demonstrate one stamina-limited attack or
  evasion sequence, one rally recovery, one timed pistol interruption followed
  by a visceral strike, and one deliberate death-mark recovery. Defeat Father
  Gascoigne without a summon, light the Tomb of Oedon Lantern and cross the
  keyed route to Cathedral Ward. Exact enemy order, damage, ammunition, Blood
  Echo totals, timings and boss phase duration are parameters.
- Potential scoped modules: direct PS4 capture with exact patch and reload;
  Cleric Beast; levelling and fortification; later areas; Chalice Dungeons;
  The Old Hunters; online notes, co-op and invasions.
- Direct-play status: not conducted. PlayStation's product page establishes
  the PS4 base product, release and strategic close/firearm combat. Two
  official PlayStation Blog guides directly establish the opening Hunter's
  Dream transition, starting weapon choice, weapon forms, Lanterns, shortcuts,
  stamina, firearm interruption, visceral response, rally and Blood Echo
  recovery/loss. Independent static written references establish Father
  Gascoigne as the required Central Yharnam route boss, his beast phase, key,
  post-boss Lantern and Cathedral Ward passage. This is a source-bounded rules
  reconstruction, not a claimed console playthrough or persistence test. No
  video or audio was opened, played or analysed.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `BB-001` | The target is the original Bloodborne PS4 base product, released 2015-03-24 and published by Sony Interactive Entertainment | Confirmed | Direct | High | P1 |
| `BB-002` | The opening defeat introduces Hunter's Dream, which supplies a choice of one of three close weapons and one of two firearms | Confirmed | Direct | High | P2 |
| `BB-003` | Each starting close weapon has two forms; the Saw Cleaver changes between faster compact and longer crowd-control forms | Confirmed | Direct | High | P2 |
| `BB-004` | Attacks, dodges and running spend one visible stamina bar, and exhausting it removes immediate defensive capacity until recovery | Confirmed | Direct | High | P2 |
| `BB-005` | A correctly timed firearm shot during an eligible enemy attack interrupts it and exposes a visceral follow-up | Confirmed | Direct | High | P1, P2 |
| `BB-006` | Recent eligible health loss creates a short rally window in which landed counterattacks restore part of that loss | Confirmed | Direct | High | P1, P2 |
| `BB-007` | Lanterns support voluntary Hunter's Dream return, supply recovery and later return to unlocked Lanterns; opened physical links shorten later routes | Confirmed | Direct | High | P2 |
| `BB-008` | Defeated enemies award Blood Echoes; death drops the carried stock and a second death before recovery loses it permanently | Confirmed | Direct | High | P1, P2 |
| `BB-009` | Father Gascoigne is the required Central Yharnam route boss, later becomes a beast and drops the Oedon Tomb Key | Observation | Corroborated | High | S1, S2 |
| `BB-010` | His defeat creates a new Lantern and permits the rear-gate path toward Cathedral Ward | Observation | Corroborated | High | S1, S2 |
| `BB-011` | No installed PS4 build, direct route, exact inventory state or quit/reload persistence was observed | Confirmed | Direct | High | R1 |

## Basic data

- Release / origin: FromSoftware developed Bloodborne; Sony Interactive
  Entertainment published the PS4 product on 2015-03-24.
- Platform or physical form: original English PS4 digital base product, fresh
  offline single-player route.
- Puzzle family: tactical forecast and counterplay; real-time system pressure;
  ordered dependency sequencing.
- Primary and official sources, accessed 2026-09-19:
  - **[P1]** [Bloodborne on PlayStation](https://www.playstation.com/en-us/games/bloodborne/),
    for product identity, PS4 platform, publisher, release and the official
    strategic-combat premise.
  - **[P2]** [12 tips for the first hours of Bloodborne](https://blog.playstation.com/archive/2018/03/06/12-tips-for-surviving-the-first-few-brutal-hours-of-bloodborne-this-months-ps-plus-headliner),
    for the opening Hunter's Dream transition, weapon choices and forms,
    stamina, firearm timing, visceral opportunity, rally, shortcuts, Lanterns,
    Blood Echo death recovery and the separation of online features.
  - **[P3]** [Bloodborne: 24 Tips for Survival](https://blog.playstation.com/2015/03/23/bloodborne-24-tips-for-survival/),
    for origin choice, Blood Echo currency and death loss, rally, lock-on,
    firearm timing, visceral strike, Blood Vials and Central Yharnam shortcuts.
- Corroborating written sources, accessed 2026-09-19:
  - **[S1]** [Central Yharnam reference](https://www.bloodborne-wiki.com/2015/03/central-yharnam.html),
    for the return shortcuts, required Father Gascoigne route, post-defeat
    Lantern and gate toward Oedon Chapel/Cathedral Ward.
  - **[S2]** [Father Gascoigne reference](https://www.bloodborne-wiki.com/2015/03/father-gascoigne.html),
    for required-boss classification, Oedon Tomb Key, human weapon-form phase
    and later beast phase. Datamined values are not imported into the genome.
- Research record: **[R1]** 2026-09-19 local preflight found no PS4 console,
  installed build, entitlement, save or reload trace; no direct play occurred.
- Claim IDs: `BB-001`–`BB-011`.

## Mechanical decomposition

### Action Genes

- `ACT-008` covers direct route traversal; `ACT-161` commits close or firearm
  attacks; `ACT-436` commits stamina-priced evasive movement; and `ACT-438`
  binds facing and camera to one eligible hostile.
- `ACT-459` switches the retained Saw Cleaver between its two combat forms;
  `ACT-200` consumes a finite Blood Vial through a vulnerable live animation;
  `ACT-224` uses a Lantern as the route's recovery/return anchor.
- `ACT-419` commits the exposed visceral follow-up before the temporary opening
  closes. `ACT-249` recovers the current dropped Blood Echo mark. Claims:
  `BB-002`–`BB-008`.

### System Behaviour Genes

- `SYS-215` and `SYS-578` own live combat, health loss and zero-health defeat.
  `SYS-798` depletes and regenerates the shared stamina reserve; `SYS-868`
  applies the selected trick-weapon form to later attack reach, speed and
  commitment.
- `SYS-778` turns the correctly timed shot into a temporary visceral opening.
  `SYS-832` banks eligible recent damage and restores it through landed
  attacks; `SYS-852` expires or replaces that recoverable share.
- `SYS-364` restores the route through Lantern recovery and ordinary-enemy
  repopulation. `SYS-399` returns death to the checkpoint while storing Blood
  Echoes in one recoverable mark. `SYS-799` advances Father Gascoigne into the
  later beast attack phase without ending the encounter. Claims: `BB-003`–
  `BB-010`.

### Constraint Genes

- `CON-354` requires sufficient stamina and completed prior recovery before a
  weapon action; `CON-604` withholds another dodge or run while the shared
  reserve is exhausted. `CON-286` requires missing health and a completed
  Blood Vial animation.
- `CON-352` allows only one unrecovered Blood Echo mark, so the next death
  destroys the earlier stock. `CON-282` keeps Cathedral Ward behind the
  mandatory boss, key and opened route. Claims: `BB-004`, `BB-007`–`BB-010`.

### Information Genes

- `INF-119` exposes health, stamina, Blood Echoes, equipped form and carried
  consumable/ammunition state. `INF-142` covers readable attack wind-ups;
  `INF-295` exposes the temporary visceral opportunity; `INF-318` identifies
  Father Gascoigne and his remaining health. Claims: `BB-004`–`BB-010`.

### Objective Genes

- `OBJ-080` closes the bounded route only when the mandatory guardian is
  defeated and the successor threshold is crossed. The optional Cleric Beast
  and broader campaign do not enter this objective. Claims: `BB-009`,
  `BB-010`.

### Time Genes

- `TIM-003` covers continuous hostile attacks, stamina recovery, rally expiry
  and healing vulnerability while the player chooses actions. Claims:
  `BB-004`–`BB-006`.

## Reproducible transitions

| Before | Action | Resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| First Hunter's Dream visit after the opening defeat | Select Saw Cleaver and Hunter Pistol | The fixed close weapon and firearm become the starting combat pair | source-bounded setup | `BB-002`, `BB-003` |
| Saw Cleaver is equipped in one form | Switch its live form | The same weapon changes later strike speed, reach and commitment | trick weapon rather than inventory swap | `BB-003` |
| Stamina is available and an enemy is reachable | Attack, dodge or run | The command spends the shared bar; further actions wait when it is exhausted | common offence/defence budget | `BB-004` |
| Eligible health damage has just landed | Strike the hostile before the rally window closes | A bounded part of the recent loss returns; waiting forfeits the opportunity | timed retaliation recovery | `BB-006` |
| An eligible hostile begins an attack | Fire Hunter Pistol in the accepted interval | The attack is interrupted and a short visceral opening appears | firearm as counter setup | `BB-005` |
| Visceral opening is active and reachable | Commit the close follow-up | High close damage resolves and the temporary opportunity closes | stagger conversion | `BB-005` |
| Blood Vial is carried and health is missing | Use the vial without interruption | One finite vial is consumed and health increases to its cap | consumable alternative to rally | `BB-006` |
| Hunter dies while carrying Blood Echoes | Resume from the Lantern route | Echoes remain at the death region or eligible carrier; another death threatens the old stock | recoverable failure state | `BB-007`, `BB-008` |
| Active Echo mark remains | Reach and recover it before another death | Stored Echoes return to the living Hunter | recovery task | `BB-008` |
| Father Gascoigne's encounter reaches its later threshold | Continue the fight | He becomes a beast with a changed attack set inside the same boss encounter | health-gated phase | `BB-009` |
| Father Gascoigne reaches zero health | Collect the result and light the new Lantern | Oedon Tomb Key and the Tomb of Oedon recovery anchor become available | mandatory settlement | `BB-009`, `BB-010` |
| Keyed rear route and lit Lantern are available | Open and cross toward Cathedral Ward | First successor control closes the bounded packet | positive terminal | `BB-010` |

## Strategic and experiential structure

- Local decision: spend stamina on another attack, preserve enough for an
  evasive response, or disengage to recover the shared reserve.
- Counterplay: read a wind-up, then choose distance, dodge, ordinary attack or
  the ammunition-backed timed firearm interruption.
- Health trade-off: retaliating can reclaim recent damage but risks replacing
  or losing the rally share; a Blood Vial is safer but finite and exposed.
- Route planning: opening physical shortcuts reduces the cost of repeated
  Lantern-to-boss attempts and of recovering a dropped Echo stock.
- Failure attribution: stamina exhaustion, mistimed firearm shot, missed rally
  window, interrupted healing, unrecovered Echo mark or unresolved boss gate
  each blocks a distinct causal edge.
- Player trust: visible meters, hostile wind-ups, stagger feedback, boss bar,
  item/key award and route opening expose the critical transitions.

## Replay and variation

- What changes: route, hostile engagement order, damage, rally amount,
  ammunition, vial use, Blood Echo position and boss timings.
- Randomness or procedural generation: no generated Central Yharnam layout is
  claimed; enemy drops and combat timing may vary.
- Multiple viable strategies: close-weapon form, optional shortcut order and
  use of firearm, rally or vial can vary, but the reproducible trace must
  demonstrate the selected defining transitions.
- Replay motive: different origins, weapons, builds, optional bosses, online
  play and later areas lie outside this first mandatory-route packet.

## Adjacent systems and history

- DARK SOULS III shares stamina-priced live melee, checkpoint recovery, one
  recoverable death-currency mark and a mandatory transforming boss gate.
  Bloodborne distinguishes itself with two-form trick weapons, firearm-created
  visceral openings and an expiring attack-recovered rally bank.
- Dead Cells and TEKKEN 8 share the portable recoverable-health bank, while
  Dead Cells also supports its timed expiry boundary. Their run and round
  structures are not imported here.
- Resident Evil 4 supports the firearm-to-stagger and contextual-close-action
  boundaries but does not combine them with Bloodborne's Lantern, Echo and
  rally loop.

## Normalised genome

| Type | Active gene IDs | Parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-161`, `ACT-200`, `ACT-224`, `ACT-249`, `ACT-419`, `ACT-436`, `ACT-438`, `ACT-459` | traversal, attack, recovery, lock, form and reclaim |
| System Behaviour | `SYS-215`, `SYS-364`, `SYS-399`, `SYS-578`, `SYS-778`, `SYS-798`, `SYS-799`, `SYS-832`, `SYS-852`, `SYS-868` | combat, rally, stamina, phase, Lantern and Echo mark |
| Constraint | `CON-282`, `CON-286`, `CON-352`, `CON-354`, `CON-604` | route, healing, mark and shared reserve |
| Information | `INF-119`, `INF-142`, `INF-295`, `INF-318` | personal state, cues, opening and boss health |
| Objective | `OBJ-080` | required boss and successor threshold |
| Time | `TIM-003` | continuous combat and recovery windows |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `307` (`GAME-0001`–`GAME-0307`).
- Exact genome matches: none.
- Tied near matches: `GAME-0290` — Lies of P (`27 / 39 = 0.692308`).
- Supported combination subsets: none.
- Scan date: 2026-09-19.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0290` — Lies of P | `ACT-008`, `ACT-161`, `ACT-200`, `ACT-224`, `ACT-249`, `ACT-419`, `ACT-436`, `ACT-438`, `SYS-215`, `SYS-364`, `SYS-399`, `SYS-578`, `SYS-798`, `SYS-799`, `SYS-832`, `SYS-852`, `CON-282`, `CON-286`, `CON-352`, `CON-354`, `CON-604`, `INF-119`, `INF-142`, `INF-295`, `INF-318`, `OBJ-080`, `TIM-003` | Both route shared-stamina melee, checkpoint recovery, a replaceable death-currency mark, recent-damage recovery and a phase-changing mandatory guardian toward a successor threshold. Lies of P adds a held guard whose lost health can be regained, Perfect Guard and Fury-response classification, blade-condition maintenance, hidden stagger build-up and combat-earned healing. Bloodborne instead switches one trick weapon between two live forms and uses a timed firearm hit to expose its visceral follow-up; it has no required held guard in this packet. | Tied near, `27 / 39 = 0.692308` |

### Preserved research notes

- New genes: none.
- Classification result: complete reuse of portable combat, recovery,
  checkpoint, route-gate and presentation boundaries.
- Evidence and reasoning: no product noun or numeric parameter requires a new
  gene; the bounded identity emerges from the combination of two-form weapon,
  firearm-to-visceral opening, rally bank and death-mark boss route.

## Taxonomy impact

- Registry changes: none; no earlier signature, definition or lifecycle
  changes.
- Taxonomy-change record: none.
- Candidate terms affected: Hunter, Saw Cleaver, Hunter Pistol, Blood Vial,
  Quicksilver Bullet, Blood Echo, Lantern, Father Gascoigne and Oedon Tomb Key
  remain instance labels.

## Negative results

- No PS4 build or direct input trace exists, so exact initial counts, patch,
  save timing and quit/reload retention are not asserted.
- The official guide distinguishes Father Gascoigne and Cleric Beast but the
  required-route/key relation is supported by static written references;
  datamined numeric values are not imported.
- Levelling, upgrades, optional boss routing, side quests and online features
  are excluded instead of being inferred from the broad product.

## Delta summary

## New facts

- [Confirmed | Direct | High] Official PlayStation material establishes the
  two-form starting weapons, shared stamina, firearm interruption, visceral
  opening, rally, Lanterns and Blood Echo recovery (`BB-001`–`BB-008`).
- [Observation | Corroborated | High] Static written route evidence establishes
  Father Gascoigne as the required gate with a later beast phase, key, new
  Lantern and Cathedral Ward successor (`BB-009`, `BB-010`).

## New genes

- [Confirmed | Corroborated | High] None; all admitted mechanics fit existing
  portable boundaries without definition changes.

## New combinations

- [Observation | Corroborated | Medium] No verified combination is asserted;
  the final subset scan is recorded above.

## Taxonomy changes

- [Confirmed | Direct | High] No earlier canonical gene or game signature is
  changed by this addition.

## New questions

- Which exact PS4 patch and fresh-save inventory quantities occur on a lawful
  local installation?
- Does the Tomb of Oedon Lantern and Cathedral Ward successor state reproduce
  identically after an observed quit/reload?

## Next recommended game

- [Hypothesis | Limited | Medium] `GAME-0309` — Mario Kart 8 Deluxe, original
  Switch base edition, one fixed 50 cc Mushroom Cup.
- Optimisation criterion: contrast Bloodborne's live retaliation/recovery loop
  with a four-race item-and-points aggregation packet.
- Backlog impact: `GAME-0309` remains the next recorded unit; no later game is
  started inside this commit.

## Why this game

- [Hypothesis | Limited | Medium] This unit tests whether established portable
  genes can reconstruct a recognised action-RPG opening without minting
  product-named boundaries, while preserving an explicit mandatory terminal
  and source limitation.
