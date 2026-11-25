---
game_id: GAME-0670
slug: phantom-dust
game_title: "Phantom Dust"
analysis_status: reviewed
reviewed: 2026-11-23
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-161
    - ACT-438
    - ACT-893
  system:
    - SYS-215
    - SYS-1920
    - SYS-1921
  constraint:
    - CON-068
    - CON-351
  information:
    - INF-119
    - INF-616
    - INF-617
  objective:
    - OBJ-029
  time:
    - TIM-003
---

# Game: Phantom Dust

This record uses the [canonical vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
Capsule counts, skill names, button labels, scenario values and battlefield
geometry are parameters.

## Analysis scope

- Version / ruleset: English original North American retail Xbox
  release, March 15, 2005 (Majesco, UPC 096427014126). Ordinary
  single-player Scenario Mode, Chapter 1, Watchful Eye at Highway.
  This scenario supplies its own initial Level 5. The exact executable
  revision and controller settings in the recordings are unverified.
- Structured analysis target: PLAT-XBOX in `knowledge/platforms/games.json`.
  W1 describes original-Xbox component capture. W2 is a 2014 recording
  of the original Xbox game under Xbox 360 backward compatibility.
- Entry: confirm Watchful Eye after the first Palace mission.
  Start at Highway briefing and first control with the preset Aura
  level, Meister as partner and a single Ommato opposition.
- Primary decision loop: approach a capsule and read its skill card.
  Capture it into a chosen face-button binding. Lock on to Ommato,
  adjust distance for the attack and use the assigned button when
  the Aura cost is affordable. Preserve range and defensive options
  while Aura refills. Close the distance for Vacuum Slash when
  Ommato has been weakened.
- Exit: Ommato is defeated before the surface limit. Confirm the
  `MISSION CLEARED` panel, the 500-credit receipt and memory box
  before starting a later mission.
- Included: movement, skill capsule preview and binding, targeted
  attacks, distance-band cues, renewable Aura, limited skill
  validity, the live clock and one settled scenario result.
  Flash Barrier is an available defence distinct from a paid attack.
- Excluded: Japanese or demo rules, 2017 Xbox One and Windows
  release features, multiplayer, assembling a later arsenal,
  collecting Aura Particles to raise Level, later mission rewards,
  refund or save checks, partner recovery and exhaustive
  environment-destruction or enemy AI modelling.
- Potential scoped modules: the first custom-arsenal mission with
  Aura Particles or a scenario requiring partner capture and recovery.

## Direct-play status

No personal installation, disc authentication or direct play.
The English retail manual documents controls and the combat rules.
A capture attributed to original Xbox hardware shows the binding,
cost, target range and complete mission settlement. A pre-remaster
recording of the original game under backward compatibility corroborates
the encounter. Static frames were inspected in the background without
audio. The evidence cannot recover physical controller inputs, exact
distance thresholds, recovery tick rate or hidden spawn-order rules.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
| --- | --- | --- | --- | --- | --- |
| PHD-001 | Majesco released the original Xbox game in North America in March 2005. Watchful Eye is a first-chapter Highway mission with Meister and one Ommato. | Observation | Corroborated | High | P1, R1, R2, W1 19:55–20:28 |
| PHD-002 | A nearby skill capsule displays its name, class, price, effect and range. Press an eligible face button to capture directly into that binding, replacing its old skill if occupied. | Observation | Corroborated | High | P1 pp. 10, 16–18, W1 20:54–21:19 |
| PHD-003 | The scenario begins with 5 current Aura and Level 5. Laser is a 1-Aura unlimited-use long-range attack, Flash Barrier is a zero-cost defence with strength 2, and the short-range Vacuum Slash is listed with cost 3, strength 7 and one use. | Observation | Corroborated | High | W1 20:55–21:19, P1 pp. 16–18, R2 |
| PHD-004 | A lock binds targeting to Ommato and indicates current range. The green distant band is suitable for Laser. The orange close band matches Vacuum Slash; an attack can be affordable but ill-positioned. | Observation | Corroborated | High | P1 pp. 10–11, 16–17, W1 20:55, 21:13, 21:21–22:17, W2 22:25–22:53 |
| PHD-005 | Paid activations debit current Aura without lowering Level, and the reserve refills. In W1 the last Vacuum Slash leaves 2 of 5 Aura and empties its binding, while the other two bindings stay. W2 shows a rejected activation at 0 Aura and subsequent recovery. | Observation | Corroborated | High | P1 pp. 16–18, W1 21:18–22:18, W2 23:04–23:06 |
| PHD-006 | In regular surface play the countdown advances while combat continues. The reference defeat occurs with time left and the result credits the mission, 500 credits and a memory box. | Observation | Corroborated | High | P1 pp. 16–18, R2, W1 21:19–22:34, W2 23:05–23:18 |

## Basic data

- Release / origin: Microsoft Game Studios Japan, published in North
  America by Majesco, 2005. This analysis uses one solo scenario.
- Families: FAM-009 for choosing responses by range, current skills
  and enemy movement; FAM-010 for live battle and recovering Aura.
- P1: [English original Xbox instruction booklet](https://phantomdust.online/img/PDManual.pdf).
  Pages 10–11 cover the controller and lock choices. Pages 14–18 cover
  mission entry, surface feedback, capture, usage, Aura and settlement.
  The host supplies the scan of the original Microsoft/Majesco booklet.
- R1: [North American Xbox retail release listing](https://gamefaqs.gamespot.com/xbox/918888-phantom-dust/data).
  It records March 15, 2005 and the North American barcode.
- R2: [2005 original Xbox walkthrough](https://gamefaqs.gamespot.com/xbox/918888-phantom-dust/faqs/38277).
  The Chapter 1 section describes the starting Aura, partner, one
  Ommato and result. Its heading misspells the name; the mission
  screen is the basis for Watchful Eye here.
- W1: [Game Footage Archive, 480p original-hardware capture](https://www.youtube.com/watch?v=BMNIu1m9Yx4&t=1195s).
  The creator describes component capture from the original Xbox with
  signal conversion. The reference sequence runs from 19:55 through
  the memory-box receipt at 22:34.
- W2: [John GodGames, original Xbox run under Xbox 360 compatibility](https://www.youtube.com/watch?v=i-1_DFav1Cw&t=1236s).
  Published in 2014, before the later re-release. Used as
  the independent clear, including the zero-Aura warning at 23:04
  and the reward screens at 23:17–23:18.
- P2: [Xbox Wire announcement of the separate 2017 release](https://news.xbox.com/en-us/2017/05/16/phantom-dust-free-xbox-play-anywhere/).
  The later edition has distinct platform and service features.
- Claim IDs: PHD-001–PHD-006.

### Reproducible route evidence

1. At the Battle Terminal, select Watchful Eye for the Highway
   after To the Surface. W1 shows mission selection near 19:55,
   confirmation around 20:03 and the Highway briefing near 20:15.
   The mission starts with the allied Meister and a 10-health Ommato.
2. Approach the orange attack capsule to read Laser around 20:55.
   Capture it to a chosen button. Around 21:09 the blue Flash Barrier
   card is visible with the Laser already bound. Vacuum Slash is
   previewed around 21:13 with a one-use counter and is bound shortly
   afterward. The manual separates capture input and subsequent skill
   use on the same button.
3. Lock onto Ommato. Read the distant green and closer yellow or
   orange states as the player crosses changes in elevation. Laser
   has the long-range recommendation. A blue capsule provides a
   zero-cost defence option. Watch
   health, current Aura and the clock during the exchange.
4. In W1 near 22:16 the panel shows Ommato at 7 health and Aura at
   5 of 5. Close into the orange band and use Vacuum Slash around
   22:17. The field shows the attack, 2 of 5 Aura and an emptied
   right binding. Laser and Flash Barrier remain assigned.
5. Observe Meister's message and the accepted result. W1 shows
   `MISSION CLEARED` by 22:26, the 500-credit reward around
   22:30 and a memory box around 22:34. W2 shows the same
   receipt, followed by control at Battle Terminal around 23:23.
   Stop at the receipt.

## Mechanical decomposition

### Action Genes

- ACT-008: steer the controlled Esper along the broken Highway to
  reach capsules and attack distances. PHD-002, PHD-004.
- ACT-161: fire Laser or commit a close Vacuum Slash against the
  locked, reachable opponent. PHD-004, PHD-005.
- ACT-438: bind the view and aiming reference to Ommato with
  lock-on and reposition relative to it. PHD-004.
- ACT-893: take a nearby skill directly into a chosen combat
  button. The previous binding can be replaced. PHD-002.

### System Behaviour Genes

- SYS-215: resolve attacks, pursuit, defence, damage and defeat
  while the surface encounter continues. PHD-004–PHD-006.
- SYS-1920: refill current Aura automatically up to Level after
  ordinary spend. PHD-003, PHD-005.
- SYS-1921: consume the last use of Vacuum Slash and empty that
  binding independently of current Aura recovery. PHD-003, PHD-005.

### Constraint Genes

- CON-068: complete the prescribed encounter before expiry of
  the surface countdown. PHD-006.
- CON-351: paid skill use requires its price in current Aura and
  debits that price when accepted. PHD-003, PHD-005.

### Information Genes

- INF-119: show player health, Aura, Level and current bindings
  while fighting. PHD-003, PHD-005.
- INF-616: show the locked opponent's moving distance band so
  the player can choose the suitable skill. PHD-004.
- INF-617: show the reachable capsule's card before slot choice.
  PHD-002, PHD-003.

### Objective Genes

- OBJ-029: defeat the only required Ommato to obtain the ordinary
  Watchful Eye scenario clear. PHD-004–PHD-006.

### Time Genes

- TIM-003: make movement, attack and capture decisions while the
  enemy and surface clock advance. PHD-004–PHD-006.

## Reproducible transitions

| From | Input or event | To | Evidence |
| --- | --- | --- | --- |
| Reachable coloured capsule, destination slot selected | Press its destination face button | Capsule captured into that combat binding | PHD-002 |
| Locked Ommato at long distance | Check green band and use bound Laser | Pay 1 Aura, advance the attack, maintain the cap | PHD-003, PHD-004 |
| Current Aura 0, Laser still bound at cost 1 | Try another paid attack | Insufficient Aura feedback; binding remains and current Aura recovers | PHD-005 |
| Ommato at close range and 7 health, one Vacuum Slash remaining | Use Vacuum Slash at 5 Aura | 2 Aura, last use gone, Ommato defeated in the observed route | PHD-004–PHD-006 |
| Required opponent defeated with time remaining | Confirm the mission result panels | Clear, 500 credits and memory box | PHD-006 |

## Strategic and experiential structure

The field supply decides what can be bound, while the player chooses
which input will own each skill. The lock marker and capsule card tell
different things. One tracks the opponent's distance, the other
explains whether the offered skill works at that distance and can
be afforded. Waiting for Aura can finance another Laser; it cannot
restore the consumed Vacuum Slash. Its one use is valuable when
distance and enemy health make the finishing attack effective.

## Replay and variation

W2 uses repeated Laser fire. It shows Ommato at 1 health and
0 current Aura around 23:04, then Ommato at 0 and Aura recovering
toward the unchanged cap. The same result does not require using
Vacuum Slash. Raw numerical distances, hit processing and
clock behaviour on failure were not tested. Timer expiry and
occupied-button replacement rules are documented by the retail
manual, with successful live transitions directly visible.

## Adjacent systems and history

The disc introduces skill decks as a later scenario progression.
This encounter uses mission-supplied capsules and a preset level.
The exact order in which unbound capsules become available on
replay was not established.

## Normalised genome

| Type | Stable genes | Role |
| --- | --- | --- |
| Action | ACT-008, ACT-161, ACT-438, ACT-893 | Move, attack, lock and bind capsule |
| System Behaviour | SYS-215, SYS-1920, SYS-1921 | Live exchange, capped refill and limited use |
| Constraint | CON-068, CON-351 | Surface deadline and cost gate |
| Information | INF-119, INF-616, INF-617 | Current resources, distance band and capsule card |
| Objective | OBJ-029 | Eliminate the required opponent |
| Time | TIM-003 | Decide while the scenario advances |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `669` (`GAME-0001`–`GAME-0669`).
- Exact genome matches: none.
- Tied near matches: `GAME-0550` — Ghost of Yōtei (`6 / 17 = 0.352941`).
- Supported combination subsets: none.
- Scan date: 2026-11-23.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
| --- | --- | --- | --- |
| [Ghost of Yōtei (GAME-0550)](../g-l/ghost-of-yotei.md) | ACT-008, ACT-161, INF-119, OBJ-029, SYS-215, TIM-003 | Both steer an avatar in real time and aim a reachable attack to finish a bounded encounter. Ghost of Yōtei teaches holding the katana guard through the Snake’s sequence and cutting into the authored gap. Phantom Dust equips available capsule skills in battle, chooses them by target distance and requires enough rechargeable Aura and remaining uses. | Near, `0.352941` |

## Taxonomy impact

Five new definitions isolate local-to-button capture, distance-band
target feedback, pre-capture skill disclosure, capped automatic
resource recovery and exhaustion of an assigned skill independent
from that recovery. Nine existing boundaries remain unchanged.

## Negative results

- Simply approaching an available capsule exposes its card but
  does not select the destination binding.
- The 5-to-2 change is a reserve debit; Level remains at 5.
  A cheap attack is not equivalent to a single-use attack.
- The active reticle's colour changes with distance. It does not
  by itself guarantee contact, hit strength or player survival.
- No Aura Particle activation is necessary in the observed
  authored mission. Later arsenal draw probabilities and inventory
  persistence are not inferred from this fight.

## Delta summary

Fourteen admitted genes, including nine reused and five new.

## New facts

- Pickup and activation are separate decisions addressed through
  the same bound input.
- A valid recharge can restore Aura without returning a consumed
  skill to its slot.
- The accepted receipt is visible after the original Highway clear.

## Principles and design implications

Use a shared resource to give differently priced actions an
opportunity cost. Combine it with a separate use count when access
to a strong move should remain scarce after recharge.

## Puzzle or game generation potential

Give an arena a limited initial skill supply and use multiple distance
bands. Reward committing the costly single-use skill within its bands
at a moment when it can change the encounter. Keep cost and durability
separate.

## New genes

- ACT-893
- INF-616
- INF-617
- SYS-1920
- SYS-1921

## New combinations

None. All 274 verified combinations were checked as proper subsets.

## Taxonomy changes

[TAXONOMY_CHANGE_416](../../../research/taxonomy-changes/TAXONOMY_CHANGE_416.md).

## New questions

Does capture versus use priority change with configured input settings?
What are the exact range-band thresholds and Aura refill interval?
How does a later arsenal's skill distribution alter the same loop?

## Next recommended game

Yoshi and the Mysterious Book on Nintendo Switch 2. Follow one
creature investigation through an accepted discovery.

## Why this game

Its original Highway mission visibly separates four stages of the
same input system: revealing a capsule, assigning a skill, paying
its activation cost and consuming a limited use.
