---
game_id: GAME-0445
slug: nights-into-dreams
game_title: "NiGHTS into Dreams"
analysis_status: reviewed
reviewed: 2026-09-28
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-580
    - ACT-581
  system:
    - SYS-037
    - SYS-045
    - SYS-1029
    - SYS-1166
    - SYS-1167
    - SYS-1168
    - SYS-1169
  constraint:
    - CON-720
  information:
    - INF-429
  objective:
    - OBJ-002
    - OBJ-254
  time:
    - TIM-003
---

# Game: NiGHTS into Dreams — first Spring Valley Mare

Use the [canonical vocabulary and genome rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Blue Chips, Ideya, a flying jester and dream scenery are carriers; the quota and ordered return, not the branded nouns, define the boundary.

## Analysis scope

- Version / ruleset: the original 1996 North American English Sega Saturn release, Claris' Spring Valley dream, first Nightopia Mare only. No remaster, *Christmas NiGHTS*, two-player versus mode, later port or emulator convenience is treated as the analysed edition. The exact Saturn disc revision was not inspected.
- Primary decision loop: enter the Ideya Palace to fly as NiGHTS; steer through a live route, touching or looping around Blue Chips, optionally use a gauge-limited Drill Attack and refill it at rings; deliver at least twenty Blue Chips to the Ideya Capture; after it releases one Ideya, choose between score-bearing remaining flight and returning to the Palace before the countdown expires. Minion contact can remove five seconds. Link bonuses reward connected item-and-ring passes without replacing the required chip handoff.
- Entry: Claris has entered the first Spring Valley dream and walks into its first Ideya Palace, becoming NiGHTS for the first Mare. The packet begins at the first steerable flight frame; the introductory scene and character choice are not scored.
- Positive terminal: the first Ideya Capture has been overloaded and the released Ideya has been returned to the Palace, starting the second Mare. The next Mare's first player decision is outside this packet. The score earned on this route may vary; merely passing the twenty-chip threshold is not completion.
- Negative terminal: if the Mare timer reaches zero before the return, NiGHTS falls and Claris resumes vulnerable ground control. An Alarm Egg catching her causes `Night Over`. A timed-out flyer is therefore not automatically identical to a terminated dream; the ground escape remains a bounded failure branch.
- Included: direct aerial steering, Paraloop enclosure collection, ring passage, held Drill Attack and its gauge, contact acquisition of chips, the twenty-chip capture threshold and release, a Time Bonus at capture, post-capture Gold Chip scoring opportunities, connected `Link` scoring, Minion movement and five-second contact penalty, remaining time and other live HUD state, clock expiry, ground-form Alarm Egg pursuit, Palace return and the handoff to Mare two.
- Excluded: the other three Spring Valley Mares, any Nightmare henchman, Elliot's dreams, all-dream rank gates, two-player Reala battle, dream-diary saving, Nightopian breeding and later edition features. Exact fixed flight-path geometry, initial timer seconds, a complete score formula, one disc's exact chip placements and the Alarm Egg's pursuit speed are not claimed.
- Reproducible parameterisation: use the original English Saturn game, choose Claris and Spring Valley, enter its first Palace, collect twenty Blue Chips by contact or Paraloop, visit the Ideya Capture until it overloads, then return to the Palace before time expires. Separately, test a held drill followed by a ring, a Minion hit, extra item/ring links, and an expired timer before Palace return. These are source-derived steps, not executed play observations.
- Potential scoped modules: later Mares, Nightmare boss combat, scoring-maximisation routes, A-life ecology, two-player versus and the remaster's original-mode wrapper each need separate evidence and terminals.
- Direct-play status: no Saturn console, original disc, controller, ROM, executable, video, audio or state capture was inspected or played. The digitised original printed manual is primary rule evidence; a contemporary Saturn player guide corroborates the first-Mare loop. Actual timings, route geometry and score arithmetic remain unmeasured.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `NIG-001` | Original Saturn Claris' Spring Valley is a four-Mare dream; this packet ends at the first Palace return. | Confirmed | Direct | High | P1, P2 |
| `NIG-002` | Entering a Palace changes walking Claris into flying NiGHTS, controlled by directional input. | Observation | Direct | High | P1 |
| `NIG-003` | Twenty Blue Chips delivered to the Ideya Capture overload it and release dream energy; the Palace return advances the Mare. | Observation | Direct | High | P1 |
| `NIG-004` | A closed Paraloop encloses and collects eligible items without touching each separately. | Observation | Direct | High | P1 |
| `NIG-005` | Held Drill Attack has a finite gauge; rings refill it. | Observation | Direct | High | P1 |
| `NIG-006` | The Mare screen displays remaining time, held chips, capture strength, score and drill gauge. | Observation | Direct | High | P1 |
| `NIG-007` | A Minion hit removes five seconds; connected item/ring passes raise Link score, while overloading the Capture lists a Time Bonus. | Observation | Direct | High | P1 |
| `NIG-008` | After capture, Gold Chips are score opportunities rather than a second twenty-chip gate. | Observation | Direct | High | P1 |
| `NIG-009` | At zero time NiGHTS falls, Claris returns to ground and an Alarm Egg can catch her for Night Over. | Observation | Direct | High | P1 |
| `NIG-010` | No direct original-disc gameplay was performed; exact route and timing arithmetic are not measured. | Confirmed | Direct | High | R1 |

## Basic data

- Release / origin: Sonic Team / SEGA, original North American Sega Saturn publication in August 1996. The [official SEGA anniversary post](https://social.sega.com/articles/rt-sega-nights-into-dreams-was-released-on-the-sega/) establishes the US Saturn identity; the manual supplies the rules.
- Platform or physical form: original one-player English Sega Saturn disc, standard or 3D control pad. The specific controller is an input parameter, not a second genome.
- Mechanical families: real-time system pressure (`FAM-010`) for the live Mare deadline and penalty; ordered dependency sequencing (`FAM-017`) for chips, capture and Palace return.
- **P1:** [Original North American Sega Saturn printed instruction manual, preserved scan](https://segaretro.org/images/e/e9/Nightsintodreams_sat_us_manual.pdf), printed pp. 3–4, 19–23 and 26, inspected 2026-09-28. The Game Goal, Nightopia, Items, Paraloop, HUD and Claris' Dreams sections establish the player-facing rules. The archive hosts a scan of SEGA's original artefact; it is not a play capture or art source.
- **P2:** [Official SEGA anniversary post](https://social.sega.com/articles/rt-sega-nights-into-dreams-was-released-on-the-sega/), inspected 2026-09-28, for the original US Saturn release identity only.
- **S1:** [Kumubou's original-Saturn guide](https://gamefaqs.gamespot.com/saturn/198201-nights-into-dreams/faqs/5183), inspected 2026-09-28, contemporary first-hand written corroboration of course and return order, not a substitute for direct verification here.
- **R1:** local preflight found no original disc, executable or direct-play trace in this unit.
- Claim IDs: `NIG-001`–`NIG-010`.

## Mechanical decomposition

### Action Genes

- Reuse `ACT-008` for direct steering of one controlled flyer, followed by vulnerable ground navigation if the timer expires. Add `ACT-580` for an intentionally closed Paraloop around several chips. Add `ACT-581` for holding the Drill Attack and spending its gauge; a ring restores capacity through a separate system response.

### System Behaviour Genes

- Reuse `SYS-037` for contact collection of loose Blue, Gold and Star Chips, `SYS-045` for moving Minions and the post-timeout Alarm Egg, and `SYS-1029` for the Time Bonus listed when the Capture is overloaded quickly. Add `SYS-1166` for the Capture's chip delivery, overload, release and subsequent Gold Chip opportunity. Add `SYS-1167` for timer-driven fall to Claris plus ground pursuit, not an immediate automatic restart. Add `SYS-1168` for ring-replenished Drill Attack gauge. Add `SYS-1169` for the connected item/ring `Link` bonus. A Minion contact's five-second cost is a parameter of the live encounter, not a second timer system gene.
- Resolution order: player flight and pickup → chip delivery at Capture → quota release → optional post-release scoring → Palace return before timer expiry. If time expires earlier, flight ends and the ground pursuit branch becomes active.

### Constraint Genes

- Add `CON-720` for the two ordered gates: at least twenty delivered Blue Chips before capture release, and a subsequent return to the Palace for progression. Individual chip placement and exact course length are parameters, not new constraints.

### Information Genes

- Add `INF-429` for remaining Mare time, held chips, capture strength, score and drill gauge. This is current state, not a future course solution.

### Objective Genes

- Add `OBJ-254` for release of one Ideya and return to the Palace. Reuse `OBJ-002` for optional score maximisation through Gold Chips, Paraloops, rings and Links; high score is not required to pass this Mare.

### Time Genes

- Reuse `TIM-003`: flight, enemies and countdown continue while directional, drill and loop inputs are accepted. The timer turning to zero triggers `SYS-1167`; it does not cause the same failure state as Alarm Egg contact.

## Reproducible transitions

| Before | Action or event | Bounded resolution | Why it matters | Claim ID |
|---|---|---|---|---|
| Claris at first Spring Valley Palace | Enter Palace | Flight control transfers to NiGHTS and the Mare begins | Ground and air are different control states | `NIG-002` |
| Several free Blue Chips near a flight line | Touch individual chips or close a Paraloop around them | Contacted or enclosed chips are credited to the held total | One loop can replace several contacts | `NIG-003`, `NIG-004` |
| Positive drill gauge while flying | Hold Drill Attack, then pass through a ring | Burst spends gauge; a ring restores usable gauge | The route can sustain further acceleration | `NIG-005` |
| Fewer than twenty chips delivered | Visit the Ideya Capture | Strength falls but it remains active | Partial progress is not release | `NIG-003` |
| Twenty eligible Blue Chips delivered | Visit the Ideya Capture | It overloads and releases one Ideya; Gold Chip scoring opens | The return gate is now relevant | `NIG-003`, `NIG-008` |
| Capture released, timer positive | Collect optional Gold Chips, then reach Palace | Score may rise; arrival starts the second Mare | Optional score does not replace return | `NIG-003`, `NIG-008` |
| Flight timer positive near a Minion | Suffer hostile contact | Five seconds are removed | Threats compress the route budget | `NIG-007` |
| Flyer has not returned | Timer reaches zero | NiGHTS falls; Claris is exposed to Alarm Egg pursuit | Expiry is a state change, not yet Night Over | `NIG-009` |
| Claris still on ground after expiry | Alarm Egg catches her | Dream ends as `Night Over` | Terminal failure follows pursuit | `NIG-009` |

## Strategic and experiential structure

- Route choice trades fast twenty-chip delivery against loop-based collection and connected score. Flight lines that pass through rings sustain drill bursts, but the same detour consumes Mare time.
- The Capture is a mid-route threshold. Once released, further Gold Chips and Links improve score, whereas Palace return completes this scoped progression. The player can abandon optional points as the countdown shrinks.
- Failure can be attributed to insufficient chips, failing to revisit the Capture, delaying the Palace return, Minion time loss or being caught after a timed-out fall. This source packet does not assert a unique optimal Spring Valley path.

## Replay and variation

Different flight paths, chip loops, drill usage, ring passes, Minion contacts and post-release scoring detours produce different scores and remaining time while preserving the same ordered objective. The manual identifies four Mares, but only the first is admitted here.

## Adjacent systems and history

`GAME-0333` *Sonic the Hedgehog* likewise combines traversal and live time, but its first act clears at a signpost after ring survival, not chip delivery and a Palace return. `GAME-0378` *Super Monkey Ball 2* rewards quick course completion and optional pickups but does not switch the controlled body to vulnerable ground pursuit at timeout. Neither later *NiGHTS* port mechanics nor a boss fight is imported into this original-Saturn packet.

## Normalised genome

| Type | Active gene IDs | Key parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-580`, `ACT-581` | direct flight, Paraloop, gauge-spending drill |
| System Behaviour | `SYS-037`, `SYS-045`, `SYS-1029`, `SYS-1166`, `SYS-1167`, `SYS-1168`, `SYS-1169` | pickup, pursuit, time bonus, capture, timeout, recharge, Link |
| Constraint | `CON-720` | twenty delivered chips then Palace return |
| Information | `INF-429` | clock, chips, capture, score and gauge |
| Objective | `OBJ-002`, `OBJ-254` | optional points and required one-Ideya return |
| Time | `TIM-003` | live course countdown and input |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `444` (`GAME-0001`–`GAME-0444`).
- Exact genome matches: none.
- Tied near matches: `GAME-0342` — PAC-MAN (`5 / 26 = 0.192308`).
- Supported combination subsets: none.
- Scan date: 2026-09-28.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0342` — PAC-MAN | `ACT-008`, `SYS-037`, `SYS-045`, `OBJ-002`, `TIM-003` | Both directly steer through a live collecting route with moving threats and optional score, but PAC-MAN clears a fixed dot maze while managing four ghost modes, pellets and lives. This Mare instead encloses chips in aerial loops, delivers a quota to the Capture, then returns to the Palace before a timeout changes the controlled body. | Tied nearest by genome Jaccard at `0.192308`; not an equivalent collection terminal. |

## Taxonomy impact

`TAXONOMY_CHANGE_182` admits nine new Active boundaries for closed flight collection, drill expenditure, chip-capture release, timeout transformation, ring recharge, Link scoring, ordered return, live flight HUD and one-Ideya objective. Existing signatures and verified combinations are unchanged.

## Negative results

- Do not model twenty loose chips as instant Mare completion: they must reach the Capture, and released energy must return to the Palace.
- Do not treat timer expiry as an immediate life-stock decrement or automatic reset; the printed manual explicitly inserts Claris' vulnerable ground phase and Alarm Egg pursuit.
- Do not import *Christmas NiGHTS*, remaster additions or the four-Mare boss into this first-Mare scope.
- Exact route geometry, initial seconds, score formula and direct-play observations remain unmeasured.

## Delta summary

## New facts

- [Observation | Direct | High] The first Mare has distinct chip, capture and Palace-return boundaries (`NIG-003`).
- [Observation | Direct | High] A timed-out flight changes actor and threat before terminal failure (`NIG-009`).

## New genes

- [Observation | Direct | High] Nine typed boundaries in `TAXONOMY_CHANGE_182` distinguish this live flight and return loop from generic collection.

## New combinations

- [Observation | Limited | Medium] None proposed; existing proper-subset support is recomputed by the comparison check.

## Taxonomy changes

- [Observation | Direct | High] `TAXONOMY_CHANGE_182`; no earlier signature is changed.

## New questions

- Would a controlled original-disc trace settle first-Mare chip placement, initial timer and Link arithmetic without changing the documented capture/return gates?

## Next game

`GAME-0446` *Railroad Tycoon II* is the next selected unit only after this unit's acceptance and Goal stop window. No push, public publication or deployment is authorised.
