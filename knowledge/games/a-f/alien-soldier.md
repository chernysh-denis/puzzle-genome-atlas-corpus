---
game_id: GAME-0620
slug: alien-soldier
game_title: Alien Soldier
analysis_status: reviewed
reviewed: 2026-11-21
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-161
    - ACT-822
    - ACT-823
    - ACT-824
    - ACT-825
    - ACT-826
  system:
    - SYS-1308
    - SYS-1817
    - SYS-1818
    - SYS-1819
  constraint:
    - CON-068
    - CON-860
  information:
    - INF-119
    - INF-318
    - INF-578
  objective:
    - OBJ-029
  time:
    - TIM-003
---

# Game: Alien Soldier

This analysis uses the [canonical vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
The four slots, attack labels and one boss are instances of the scoped rules.

## Analysis scope

- Version / ruleset: Japanese commercial Sega Mega Drive cartridge G-4130
  of February 24, 1995, fresh single-player Stage 01 on SUPERHARD. The
  original Japanese booklet and catalogue identify the retail release.
  One capture reports Japanese game data on a Genesis. Its exact carrier,
  game-image hash and controller inputs are not independently verified.
- Primary decision loop: enter the Jetsripper fight with the prepared
  weapon slots. Read Force Energy, life, the countdown and the boss head's
  position. Choose a firing stance and height, fire a suitable weapon or
  switch slots, and choose between a defended dash, a full-health attack
  or a forward projectile counter. Keep enough life and time to defeat
  Jetsripper and see control return in Stage 02.
- Entry: the Stage 01 boss warning and arena, with the preselected four
  slots and current life and Force stocks as initial conditions. The
  corridor before the warning and setup screens are evidence for the
  initial state, not additional play targets.
- Exit: the boss loses its remaining life. The stage transition completes
  and ordinary player movement is visible in Stage 02 before its boss.
  Merely causing a hit flash or surviving the warning is insufficient.
- Included: the preselected arsenal and live selector, fixed and moving
  fire, jump and hover height, aimed attacks on the vulnerable head,
  protected dash with its full-health outcome, the counter projectile
  and recovery option, life and weapon stocks, boss life, conditional
  weak-point cue, deadline and observed handoff.
- Excluded: later bosses including Xi-Tiger, ordinary corridor clearing,
  farming weapon spares, result-table optimisation, password and continue
  rules, SUPEREASY speed controls, European cartridge rules, Sega Channel
  and later compilations. No exact damage, recovery rate, frame input
  duration, random-pattern weights or universal lowest-time strategy.
- Suggested later scope: the distinct Antroid encounter in Stage 02, with
  its defensive posture and different valid target height.

## Direct-play status

No direct play was performed. Sega's original Japanese manual specifies
the commands and resource limits. Stage-Clear reports Japanese game
data on a North American Genesis Model 1 with a video-output modification.
Japanese introductory subtitles and SUPERHARD selection match the
reported rules. The retail cartridge itself is not authenticated by the
capture. MrCoconuts64's independent SUPERHARD trace, with Japanese opening
subtitles, corroborates the encounter and transition. Other edited
captures support the visual boss states without proving their carrier.
Only written material and sampled stills were inspected without
playing video or sound.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
| --- | --- | --- | --- | --- | --- |
| ALS-001 | The original Japanese cartridge is Sega's G-4130 release of February 24, 1995. The scoped fight is the first boss on SUPERHARD. | Confirmed | Corroborated | High | P1, P2 and S1 for the commercial product. W1 0:00–0:50 and W2 3:20–4:50 show the selected difficulty and route. W1 reports the Japanese program but has no cartridge or checksum attestation. |
| ALS-002 | Choose four weapon slots from six types before play, allowing duplicates. During the fight the selector chooses one of the prepared slots and prevents movement and attacking while open. Crouch and toggle between the white fixed and gold moving fire modes. Neither choice merges weapons. | Confirmed | Direct | High | P1 pp. 8–9 and 14–15. W2 3:40 shows Flame Force during setup. S2 gives an opening slot switch for this boss. |
| ALS-003 | Firing consumes the selected slot's Force Energy. Fixed fire costs less and anchors the body on the ground or during hover. Moving fire allows displacement and is more expensive. Unused slots recover; depletion blocks the selected weapon's normal effect. | Confirmed | Direct | High | P1 pp. 8–9 and 20–23, S2 and S4. S4 reports a weak fallback when ordinary supply is exhausted, so the handbook does not justify a claim that all possible attacks are blocked. No exact rate or per-weapon formula is admitted. |
| ALS-004 | A second jump input suspends the body in the air so it can fire; the next can raise it again. The compatible jump chord starts a fast protected Zero Teleport at the current height. Actual movement around the head is part of the route. | Confirmed | Corroborated | High | P1 pp. 6–11. W1 0:30–0:40 and W2 3:50–4:10 and 4:30 show different elevations. S2 and S3 describe choosing elevation for the boss. Static samples cannot prove a hover input on any exact frame. |
| ALS-005 | Beginning a Zero Teleport at full health upgrades it to a fiery contact attack, which itself spends life. The boss must overlap the attacking path. The same command below full health is a movement/defence action without that fiery contact upgrade. | Confirmed | Corroborated | High | P1 pp. 10–11 and 34–35. S2 describes using the upgraded dash across the low head or curled body. W3 0:20 and W4 0:20 show offensive effects in the matching boss arena but are insufficient to isolate exactly which input depleted the last health. |
| ALS-006 | Counter Force is a separate double-fire tap that creates a small shield in front of the player. An eligible projectile overlapping it is destroyed and produces a healing item, awarded on collection. Restoring full health enables the charged dash again. | Confirmed | Corroborated | High | P1 pp. 8–9, 20–21, 34–35. S2 names the first boss's bouncing projectile as a valid counter target. The positive clear does not require or prove a successful counter pickup. |
| ALS-007 | The HUD separates player life, selected Force Energy, boss life and remaining time. Eagle Eye can locate a vulnerable part after a lull in fire or during homing fire, with Sword and Lancer exceptions. Jetsripper's head is the recommended local target. No whole-body damage equivalence is established. | Confirmed | Corroborated | High | P1 pp. 8–9, 16–17 and 34–35. S2 and S3 identify the head and height trade-off. W1 0:40 and W2 4:30–4:40 show the active arena and HUD. |
| ALS-008 | Reaching zero player life or time ends the attempt. On the positive path W1 0:40 shows Jetsripper in the arena and 0:50 shows Stage 02. W2 4:40 shows the curled target being hit and 4:50 shows live movement in the successor area. | Observation | Corroborated | High | P1 pp. 16–19 and 34–35 for failure rules. W1 and W2 for the actual result. W3 0:20–0:30 moves from the first boss to the next in an edited sequence, so it corroborates identity rather than the uncut handoff. |

## Basic data

- Title: Alien Soldier
- Analysis target: `PLAT-SEGA-GENESIS`, original Japanese Mega Drive G-4130.
- Release: Treasure, published by Sega Enterprises on February 24, 1995.
- Encounter: Stage 01 Jetsripper on SUPERHARD, single player.
- Mechanical family: `FAM-010`, live hazard and countdown pressure while managing resources.
- Sources checked 21 November 2026.
- P1: [Sega's Japanese retail manual, G-4130](https://www.sega.jp/mdmini2/assets/manual/pdf/JP_Alien-Soldier.pdf).
  Printed pp. 6–11 cover the action controls, pp. 14–17 the four slots
  and HUD, pp. 20–23 the reserve and weapons, and pp. 34–35 the dash
  and counter advice. The PDF is distributed on the Mini 2 page as a
  reproduction of the Japanese retail manual.
- P2: [Sega's original Mega Drive release date](https://www.sega.jp/mdmini2/soft/alien-soldier.html),
  explicitly dated to the Mega Drive publication.
- S1: [Japanese cartridge record](https://titlescreen.org/release/rjrf2n2e/alien-soldier),
  retail serial G-004130-00. The listed hash is a catalogue identifier,
  not a measured digest of either recording.
- S2: [Japanese SUPERHARD Stage 01 account](https://shouga.nukenin.jp/ASact1.html),
  names JETSRIPPER and documents choosing flame, aiming at the low head
  and countering bouncing fire. This is the author's route, not a
  mandatory input sequence.
- S3: [Second Japanese combat account](https://zze128.blog9.fc2.com/blog-entry-508.html),
  identifies the head and Flame or Lancer choices.
- S4: [TASVideos mechanics notes](https://tasvideos.org/GameResources/Genesis/AlienSoldier)
  distinguish the exhausted-slot fallback from normal weapon fire.
  Tool-assisted tricks and exact rates are excluded.
- W1: [Stage-Clear, Japanese SUPERHARD longplay](https://www.youtube.com/watch?v=YXS89tFnFaE&t=30s).
  At 0:00 the difficulty is visible, 0:30 is the elevated approach,
  0:40 shows the first opponent and 0:50 shows Stage 02.
- W2: [MrCoconuts64 SUPERHARD longplay](https://www.youtube.com/watch?v=rq9VIZfuTd8&t=269s).
  At 3:40 the setup shows a Flame Force slot. At 4:30 the warning is
  visible, at 4:40 a hit effect overlaps the curled boss, and by
  4:50 the character is mobile on the following section's deck.
- W3: [GameMistress edited boss walkthrough](https://www.youtube.com/watch?v=jw0DoQ2H1FQ&t=14s).
  Sample at 0:20 shows the grounded projectile-to-boss geometry.
- W4: [Shadowserg SUPERHARD boss sequence](https://www.youtube.com/watch?v=LA03WAjg6ic&t=7s).
  Samples at 0:10 and 0:20 show two head elevations before the next boss.

## Mechanical decomposition

### Action Genes

- ACT-008: steer the character and use ordinary jumps to change side or height.
- ACT-161: direct the current weapon at Jetsripper's exposed head.
- ACT-822: choose a prepared weapon slot through the live selector and confirm.
- ACT-823: crouch and toggle fixed aim or firing during movement.
- ACT-824: suspend a jump at a shootable height and step higher if needed.
- ACT-825: dash laterally with a protected travel interval at the current height.
- ACT-826: double-tap fire to raise the small forward Counter Force field.

### System Behaviour Genes

- SYS-1308: the fiery dash subtracts the player's own health as its execution cost.
- SYS-1817: the selected slot spends energy on fire while unused stock recovers separately.
- SYS-1818: a dash from full health acquires the fiery contact effect, whereas the ordinary branch remains available below full health.
- SYS-1819: counterfield contact converts an eligible enemy projectile to a separated healing pickup.

### Constraint Genes

- CON-068: zero stage time before completion fails the attempt.
- CON-860: prepare exactly four weapon slots, allowing repeated weapon types.

### Information Genes

- INF-119: observe the player's health, active weapon and remaining Force Energy.
- INF-318: see the mandatory encounter's enemy life.
- INF-578: read the local Eagle Eye marker subject to idle time and weapon type.

### Objective Genes

- OBJ-029: defeat the single required guardian while the player remains viable. The observed transition to Stage 02 verifies the closeout.

### Time Genes

- TIM-003: take movement and fire decisions while the stage clock and boss continue.

## Reproducible transitions

| State | Input or trigger | Result | Evidence |
| --- | --- | --- | --- |
| Stage 01 warning, selected kit ready | Enter the local boss space and choose a position for the head's height | Jetsripper becomes active under the existing clock, with life and energy visible | ALS-001, ALS-004, ALS-007 |
| Grounded or hovering during the fight | Use fixed fire to redirect in place, or toggle to moving fire and reposition while attacking | The chosen attack spends energy at the current mode's rate | ALS-002, ALS-003 |
| Selected Force Energy running low | Open the selector, choose another prepared slot and confirm | Movement and fire are unavailable while selecting, and the abandoned slot can refill through time | ALS-002, ALS-003 |
| Boss below or level with the player | Jump or hold a hover, then choose a line for firing or a dash | The action addresses the target height, and the transit protects the body | ALS-004, ALS-007 |
| Full current life before the dash | Commit the lateral Zero Teleport toward the exposed head | The fiery branch can damage an overlapping part and reduces the player's health | ALS-005 |
| Below full current life | Request the same compatible dash | Travel still protects the body but lacks the full-health fiery attack | ALS-004, ALS-005 |
| Eligible projectile in front | Double-tap fire, then move onto the separate item if it is produced | Destruction removes the projectile, and only pickup restores life | ALS-006 |
| Guardian depleted while the avatar is viable | Finish the encounter and await the handoff | The next stage starts under ordinary control | ALS-008, W1 0:40–0:50, W2 4:40–4:50 |
| Time or player life at zero before clearance | Terminal condition | Game over rather than an ordinary stage handoff | ALS-008, P1 rules |

## Strategic and experiential structure

Time spent positioning, waiting for a cue or selecting another weapon
competes with the running clock and hostile pressure. Fixed fire trades
mobility for lower reserve expenditure. Moving fire and a protected
dash can reset the angle. Full health is both survival capacity and
the precondition of a stronger dash, creating a reason to distinguish
preventing the next hit from immediately spending the upgraded move.

## Replay and variation

The two opening traces take different paths and amounts of time while
reaching the same successor. The Japanese account reports several first
boss motion branches. The samples do not identify their exact selection
probabilities, minimum kill time or the one killing input. The documented
counter recovery and the charged dash are available decisions, not claims
that every successful route uses them.

## Adjacent systems and history

The Sega release listing preserves the original cartridge date alongside
a later compilation. The Japanese manual and Japanese-rule traces define
this analysis. Printed continue and speed differences explain why the
SUPEREASY option and later emulated product menus remain outside the packet.

## Normalised genome

| Type | Stable genes | Role |
| --- | --- | --- |
| Action | ACT-008, ACT-161, ACT-822, ACT-823, ACT-824, ACT-825, ACT-826 | Move, fire, change weapon or posture, hover, dash and counter |
| System Behaviour | SYS-1308, SYS-1817, SYS-1818, SYS-1819 | Pay life, rotate independently recovering reserves, upgrade a dash and convert hostile fire |
| Constraint | CON-068, CON-860 | Stage deadline and four prepared slots |
| Information | INF-119, INF-318, INF-578 | Personal stocks, boss life and conditional weak-point marker |
| Objective | OBJ-029 | Defeat the single mandatory boss |
| Time | TIM-003 | Choose while the encounter and clock advance |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `619` (`GAME-0001`–`GAME-0619`).
- Exact genome matches: none.
- Tied near matches: `GAME-0550` — Ghost of Yōtei (`6 / 21 = 0.285714`).
- Supported combination subsets: none.
- Scan date: 2026-11-21.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
| --- | --- | --- | --- |
| [Ghost of Yōtei (GAME-0550)](../g-l/ghost-of-yotei.md) | ACT-008, ACT-161, INF-119, INF-318, OBJ-029, TIM-003 | Both position a controlled body, attack one required opponent and read both sides’ condition during live combat. Ghost of Yōtei uses katana block and light cuts through a scripted duel. Alien Soldier rotates recovering weapon slots, chooses firing height or a full-health dash, and has a terminal stage deadline. | Near, `0.285714` |

## Taxonomy impact

[TAXONOMY_CHANGE_366](../../../research/taxonomy-changes/TAXONOMY_CHANGE_366.md)
adds the independent slot and response dependencies to the opening battle.

## Negative results

- ACT-763 combines two retained weapon components. Alien Soldier chooses
  one separate slot at a time. CON-825 models only two component positions.
- ACT-199 moves or equips an item. The live selector changes which already
  prepared offensive reserve is active without transferring it.
- SYS-1365 and SYS-237 spend one reserve rather than two or more independent
  weapon stores. SYS-1379 selects automatically after depletion.
- ACT-623 asks for a target-conditional homing dash. ACT-749 charges a
  crossing by holding an input. The Zero Teleport branch depends on current
  health and shares the same chord with ordinary protected transit.
- SYS-994 redirects a projectile. Counter Force destroys it and creates a
  collectible, so neither reflection nor immediate healing was admitted.
- INF-538 resolves a selected scan, and SYS-1236 requires an armour-state
  transition. The supplied marker and target height establish neither.
- The visible move sequence does not establish exact frame timings, a
  confirmed stage-clear record time, or the outcome of simultaneous expiry.

## Delta summary

Adds a Japanese cartridge encounter where weapon rotation, live posture and
player vitality govern different actions before the boss clear.

## New facts

- One prepared slot spends energy while inactive ones replenish independently.
- A full health bar changes the effect of the same protected dash command.
- The project's positive evidence includes access to Stage 02 after Jetsripper.

## New genes

ACT-822–ACT-826, CON-860, INF-578 and SYS-1817–SYS-1819.

## New combinations

None admitted.

## Taxonomy changes

[TAXONOMY_CHANGE_366](../../../research/taxonomy-changes/TAXONOMY_CHANGE_366.md).

## New questions

How does the choice of stance and weapon change options in Antroid's
defensive posture? A standalone trace should establish that encounter first.

## Next recommended game

`GAME-0621` Sonic Racing: CrossWorlds, Xbox Series X|S standard base game.

## Why this game

The final roster entry changes the studied decision from boss positioning
to a live route selection during a completed Grand Prix race.
