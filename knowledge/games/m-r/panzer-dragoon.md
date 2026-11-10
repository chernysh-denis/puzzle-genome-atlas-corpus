---
game_id: GAME-0505
slug: panzer-dragoon
game_title: Panzer Dragoon
analysis_status: reviewed
reviewed: 2026-10-06
combination_ids: []
gene_ids:
  action:
    - ACT-161
    - ACT-562
    - ACT-610
    - ACT-690
    - ACT-691
  system:
    - SYS-215
    - SYS-1410
    - SYS-1411
    - SYS-1412
    - SYS-1413
    - SYS-1414
    - SYS-1415
  constraint:
    - CON-183
    - CON-782
  information:
    - INF-489
    - INF-490
  objective:
    - OBJ-002
    - OBJ-288
  time:
    - TIM-003
---

# Game: Panzer Dragoon — original Episode 1 flight and credit settlement

Use the canonical [vocabulary and genome rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
Controller labels, eight locks, episode names, damage values and regional credit
numbers are parameters rather than separate genes.

## Analysis scope

- Version / ruleset: original 1995 English North American Sega Saturn base game,
  ordinary GAME / NORMAL, Episode 1. This is not the 2020 Remake, Windows port,
  Orta bonus port, Zwei, Saga or an invincibility, Episode 0 or Wizard attempt.
  Exact disc revision and native execution are uninspected. The Western initial
  credit value is source-qualified, not imported from the contradictory manual.
- Structured analysis target: PLAT-SEGA-SATURN; original English North American
  Saturn base edition, Normal first episode; exact disc revision unverified.
- Primary decision loop: place the dragon within the advancing route, choose a
  forward, flank or rear attack view, aim a direct rider shot or sweep a held
  targeting command over multiple enemies and release the dragon's homing volley;
  avoid incoming harm while deciding how much exposure to accept for more kills
  and a better credit award, then defeat the episode's warship boss.
- Entry and exit: a fresh ordinary GAME / NORMAL attempt enters Episode 1 before
  its first ordinary encounter. Include the complete water/ruin route, optional
  target groups, boss, shot-down-ratio and credit closeout, transition and first
  ordinary Episode 2 control. Arriving at the boss or seeing its explosion alone
  does not finish this packet. Zero energy is a failed local attempt; an eligible
  Continue YES retries the beginning of that episode, NO abandons it and no
  remaining credit leads to Game Over. No campaign completion is claimed.
- Included: imposed forward route, bounded two-axis body control, shared aiming
  input and source-qualified view-dependent body restriction, quarter-turn attack
  sectors, three optional camera distances, aimed rider fire, hold/sweep/release
  dragon targeting, finite simultaneous target capacity, homing resolution,
  current energy and incoming harm, boss health and exposed target geometry,
  kill score, missed enemies and ratio, credit award and paid retry, episode
  closeout and restored energy in successor control, pause and resume.
- Excluded: all later Episode 2 decisions, later bosses, campaign ending,
  difficulty variants, secret modes and cheats, sequel dodge/morph/berserk rules,
  later ports and remakes, external save states, native frame timings and exact
  unverified lock/damage/credit-threshold formulas. Selecting the reproduction
  preset is not a separate campaign progression mechanic.
- Potential scoped modules: original Hard terminal, later sandworm encounter
  and regional differences, Episode 0, score ranking and exact native controller
  timing. No module ID or whole-product signature is invented.
- Direct-play status: no disc, Saturn, emulator or native input trace was run.
  Original publisher manual text and visually reviewed European printed pages
  5–8 establish instructions; attributed muted paused recording frames establish
  displays and the ordinary Episode 1-to-2 transition, not executable identity or
  uninterrupted native play. Source recording R1 discloses possible save states
  and a secret-code opening outside the scoped ordinary footage. R2 is presented
  as 4K/60FPS; native timing, region and difficulty are not inferred from it.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| PD-001 | The ordinary first episode advances through water and ruins, reaches a warship boss and settles into Episode 2 rather than a freely chosen route. | Observation | Corroborated | Medium | R1 488/555/620/645/695/740/785/800/820/850/870; R2 670/730/850/883/900 |
| PD-002 | D-pad controls flight and aiming; shoulders move the attack view in 90-degree steps and X/Y/Z select three view distances. | Confirmed | Direct | High | P1 printed pp. 6–9; P2 printed pp. 5–7, visually inspected |
| PD-003 | Holding a fire button and sweeping the aim acquires up to eight enemy targets; release emits the dragon's homing volley, whereas a tap fires the rider's aimed shot. | Confirmed | Direct | High | P1 printed p. 10; P2 printed p. 8, visually inspected |
| PD-004 | Aim and body follow the same directional input at different speeds; non-forward view restricts body movement in the original game. No precise transfer function or blocked-axis table is established. | Observation | Limited | Medium | S2 gameplay discussion; P2 separates flight direction and flight view but does not quantify this relation |
| PD-005 | Hostile damage lowers the blue energy bar; zero energy interrupts the attempt and credit availability determines whether an episode-entry Continue remains available. | Confirmed | Direct | High | P1 printed p. 10; P2 printed p. 8 |
| PD-006 | Each downed enemy adds points, and episode shot-down proportion earns credits; the complete numerical threshold table and target-specific points are not established. | Confirmed | Direct | High | P1 printed p. 10; P2 printed p. 8 |
| PD-007 | R1's completed Episode 1 displays 98.7%, one missed enemy, two awarded credits and three current credits; R2 displays 93.9%, five missed, one awarded and two current credits. These are two observed outcomes, not a universal conversion table. | Observation | Corroborated | High | R1 actual paused frame 820; R2 actual paused frame 850 |
| PD-008 | The manual states three starting credits on Normal, while the regional review and later player's account state one for the US/PAL original. R1's award plus total is consistent with one but does not prove an unmodified fresh executable. | Observation | Conflicting | Medium | P1 printed p. 10; P2 printed p. 8; S1 Credits; S2; R1 820 |
| PD-009 | The boss display exposes its remaining red health separately from the dragon's blue energy, and the radar shows current threat bearings relative to the selected attack view. No exact hidden target range is inferred. | Observation | Corroborated | Medium | R1 555/645/695/740/785; R2 670/730 |
| PD-010 | R1 carries awarded credit stock into successor play and displays a refilled energy bar at ordinary Episode 2 control. The exact reset update and other carried fields are unmeasured. | Observation | Limited | Medium | R1 785/820/870 |
| PD-011 | Continue YES returns to the start of the current episode rather than an observed halfway checkpoint; NO returns to the title, and exhausted credits produce Game Over. | Confirmed | Direct | High | P1 printed p. 10; P2 printed p. 8 |
| PD-012 | The player can pause and resume; route advancement and hostile resolution otherwise continue while aiming, changing view or acquiring locks. | Confirmed | Corroborated | High | P1 printed pp. 6–7; P2 printed p. 5; R1/R2 ordinary combat |
| PD-013 | English US and European manual controls agree, but this does not establish disc parity, exact region of either recording, all later encounters or native timing. | Observation | Limited | High | P1/P2; S1 regional changes; R1/R2 source limitations |

## Basic data

- Release / origin: original Sega Saturn Panzer Dragoon, Sega, 1995; US booklet
  identifies product 81009. No later port's release or rule changes are merged.
- Platform or physical form: Sega Saturn, one player, English base-game Normal.
- Mechanical family: real-time system pressure, for an advancing route whose
  attacks and exposure do not wait for target selection. No new family is needed.
- Sources accessed 2026-10-06:
  - **P1** — [Sega's original US instruction booklet](https://www.gamesdatabase.org/Media/SYSTEM/Sega_Saturn//Manual/formated/Panzer_Dragoon_-_1995_-_Sega.pdf), printed pp. 6–10. Text was available through the archival web renderer; later direct download and page-image retrieval failed, so no visual US-page inspection is claimed.
  - **P2** — [Sega's 1995 European manual scan](https://archive.org/details/Panzer_Dragoon_1995_Sega_EU), original 28-sheet multilingual booklet. English printed pp. 5–8 were read as text and visually inspected from PDF sheets 4–6. Its regional starting-credit text remains in conflict with S1, not proof of Western runtime behavior.
  - **R1** — [World of Longplays / Deskawa, Sega Saturn Longplay Panzer Dragoon](https://www.youtube.com/watch?v=peoRBj9U-jI), published 2011-05-21, author-described Normal. Actual paused samples: 488, 555, 620, 645, 695, 740, 785, 800, 810, 820, 850 and 870 seconds. 660 and 826 are black transition samples and are rejected as mechanical evidence. Metadata names Episode 1 at 8:04 and Episode 2 at 14:21; these are source locators, not fixed game durations. Save-state disclaimer and secret-code opening prevent any claim of clean continuous native provenance.
  - **R2** — [Longplay Library, Panzer Dragoon Saturn longplay](https://www.youtube.com/watch?v=8-10Dep-yh0), published 2026-05-02, 4K/60FPS presentation. Actual paused samples: 670, 730, 850, 883 and 900 seconds. Difficulty, region, interpolation and executable provenance are unverified; it corroborates visible route and settlement only.
  - **S1** — [Lance Way, Version Differences](https://panzerdragoonlegacy.com/literature/340-version-differences), 2011-07-06, Credits section. An unofficial regional comparison with some emulator screenshots; do not silently treat it as direct native execution.
  - **S2** — [The MegaDriver, How Panzer Dragoon Defined an Era](https://www.segasaturnshiro.com/2024/07/02/how-panzer-dragoon-defined-an-era/), 2024-07-02, gameplay discussion. The firsthand qualitative movement account does not supply a native input trace or exact axis/timing specification.
- Audio was not played or analysed. All recording samples used isolated headless
  browser processes, muted and paused. User windows, tabs, focus and system sound
  were not changed. Source screenshots remain local and are not distributed.

## Mechanical decomposition

### Action Genes

- Reuse `ACT-161`: tap the equipped rider weapon at a currently reachable target.
- Reuse `ACT-562`: place the dragon along bounded lateral flight axes while the
  authored route advances; this is not free six-axis flight or a route selection.
- Reuse `ACT-610`: change only the following view's distance with X/Y/Z while
  retaining the current attack sector and controlled body. Do not use this gene
  for shoulders, whose sector change changes target access and body authority.
- New `ACT-690`: quarter-turn the active attack view to address threats
  from a flank or rear without changing the automatically advancing world route.
- New `ACT-691`: hold acquisition, sweep the aim through eligible targets
  and release the pending multi-target volley; no inventory missile is armed.
- Claim IDs: PD-001–PD-004.

### System Behaviour Genes

- Reuse `SYS-215`: player-commanded and hostile attacks resolve in real time,
  changing target health and the dragon's single energy bar.
- New `SYS-1410`: advance the authored 3D encounter route without player
  longitudinal authority or an admitted intermediate retry checkpoint.
- New `SYS-1411`: retain the bounded set acquired during a held command and
  resolve released homing attacks against it. Locking alone is not a hit.
- New `SYS-1412`: couple the shared directional aim input to slower body
  following under current-view restrictions; quantitative behavior is unmeasured.
- New `SYS-1413`: convert the settled destroyed-versus-counted enemy ratio
  into additional continue credits under the declared regional reward policy.
- New `SYS-1414`: accept an eligible credit-paid Continue and rebuild the
  failed episode from its entry, rather than automatically reviving in place.
- New `SYS-1415`: settle boss-clear closeout, retain the current credit stock
  and instantiate the next episode with restored current energy; no disk save or
  power-off continuation is claimed.
- Resolution order: route and current attack view → bounded aim/body command →
  direct shot or held acquisition → released homing and hostile effects → enemy
  defeat/points and dragon energy → failed-entry Continue or boss-clear closeout
  → ratio award → transition and ordinary successor control. No universal frame
  ordering of simultaneous lethal damage and boss defeat is established.
- Claim IDs: PD-001, PD-003–PD-012.

### Constraint Genes

- Reuse `CON-183`: finite visible continue stock permits another episode attempt
  while any remain; no stock plus local defeat ends the run. Initial stock is a
  qualified regional parameter, not an undisputed number from the manual.
- New `CON-782`: the simultaneously acquired target set has a fixed capacity
  of eight in these original instructions; acquiring one does not invent ammo.
- Current attack view also restricts body control under PD-004; this condition is
  represented by the coupling system, not duplicated as a second candidate.
- Claim IDs: PD-003–PD-005, PD-008, PD-011.

### Information Genes

- New `INF-489`: current sector radar, aiming reticle and acquired-target
  marks expose presently addressable threats and a pending volley, not the full
  authored future route or an exact undisclosed lock timing model.
- New `INF-490`: distinguish current dragon energy and boss vitality from
  the closeout's ratio, missed-enemy count, awarded and total continue credits.
- Claim IDs: PD-005–PD-010.

### Objective Genes

- Reuse `OBJ-002`: increase the optional cumulative enemy-destruction score;
  merely passing a fixed score threshold is not the required episode clear.
- New `OBJ-288`: survive the authored first flight, defeat its terminal
  warship, accept the credit settlement and reach ordinary next-episode control.
  Destroying every ordinary enemy is not mandatory for this positive terminal.
- Claim IDs: PD-001, PD-006, PD-007, PD-010.

### Time Genes

- Reuse `TIM-003`: route, threats and live attacks progress during aim, sector
  changes and lock acquisition; pause/resume is an allowed rate parameter.
- Claim IDs: PD-001, PD-012.

## Reproducible transitions

| Before | Action | Bounded resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Ordinary Episode 1, forward sector | Move directional control while the route advances | Aim moves and the dragon follows within the allowed lateral course, not back to passed space | imposed course plus bounded placement | PD-001–PD-004 |
| A flank or rear threat is outside current aim | Press a shoulder once | Active attack view changes by one quarter-turn; route progress is not reversed | target-sector change is not cosmetic zoom | PD-002, PD-004, PD-009 |
| An eligible enemy is inside the aimed firing region | Tap fire | Rider weapon makes a direct shot; target damage still depends on legal resolution | direct aim differs from pending dragon locks | PD-003 |
| Several eligible enemies pass through the reticle | Hold fire, sweep, then release | Up to eight acquire marks precede a homing volley; holding marks alone is not a declared destruction | deferred multi-target commit | PD-003 |
| Current energy remains positive | A hostile attack connects | Blue energy decreases; no immediate extra credit is consumed merely for a non-lethal hit | energy versus attempt stock | PD-005 |
| Energy reaches zero and a credit remains | Select Continue YES | Spend the declared retry credit and restart the current episode at its beginning | explicit paid restart, not free checkpoint recovery | PD-005, PD-011 |
| Failed attempt offers continuation | Select NO | Return to title instead of accepting a retry | abandonment is not an episode clear | PD-011 |
| Energy reaches zero without credits | Let terminal resolve | Game Over and opening/title flow rather than a new credited attempt | finite run failure | PD-005, PD-011 |
| Terminal boss remains alive | Hit eligible warship targets while avoiding its attacks | Boss vitality falls independently from dragon energy; boss defeat closes ordinary episode combat | separate damage recipients | PD-001, PD-009 |
| R1 boss defeated, one counted enemy missed | Accept episode closeout | Display 98.7%, add two credits and show total three; this is an observed example, not the whole threshold table | destruction proportion differs from points | PD-007 |
| R2 boss defeated, five counted enemies missed | Accept episode closeout | Display 93.9%, add one credit and show total two | incomplete kill set can still clear | PD-007 |
| First episode closeout completed | Let transition finish | Ordinary Episode 2 control begins; R1 shows restored energy and retained credited stock | complete bounded positive terminal | PD-001, PD-010 |
| Ordinary live attempt | Press Start, then Start again | Pause and resume under original instructions | live progression is pausable, not turn-based | PD-012 |

## Strategic and experiential structure

- Local decision: balance a usable current firing sector against lateral safety
  and decide whether to take an immediate shot or spend exposure time sweeping
  a larger pending target set.
- Medium-term planning: missed enemies affect the later retry award, so kills
  have both optional point value and a survival-stock consequence. A full clear
  is not required to finish the stage, as both inspected outcomes demonstrate.
- Long-term structure: additional credits support later episode attempts, but
  the later campaign decisions and final ending are outside this packet.
- Common heuristic: check the sector radar before chasing a target, avoid
  assuming sideways camera movement gives full free-flight escape authority,
  and distinguish an acquired lock from an already resolved kill.
- Failure attribution: blue energy records current survival; the continue stock
  records whether another complete episode attempt is available. Boss health,
  missed enemies and the closeout disclose different consequences.
- Player-trust factors: current reticle/radar and paired vitality displays make
  active threats inspectable; closeout shows the observed reward. Neither exact
  numerical reward thresholds nor future unseen enemy timings are established.
- Claim IDs: PD-001–PD-012; heuristic interpretation is bounded inference.

## Replay and variation

The two attributed recordings show the same qualitative water/ruin/boss route
with different missed-target and credit outcomes. Aim order, pending lock set,
exposure, energy lost, kill count and whether a Continue is used can differ.
Random enemy-generation claims, exact native route speed and credit thresholds
are not inferred from the videos. Difficulty and regional variants need their
own declared scope rather than silently changing this one.

## Adjacent systems and history

Star Fox 64 transfers bounded two-axis rail steering, direct combat and live
progression, but its admitted Corneria checkpoint, wingmate rescue and
seven-arch route gate are absent here. Panzer's active attack-sector change,
held multi-target release and ratio-paid continue policy cannot be replaced
with those branch rules. Elite's finite missile arm/acquire/cancel and Tomb
Raider's automatically retained single-target fire lock are distinct commands.
These are operational comparisons, not a claim of historical invention.

## Normalised genome

| Type | Active gene IDs | Key parameters |
|---|---|---|
| Action | ACT-161, ACT-562, ACT-610, ACT-690, ACT-691 | aimed shot, bounded placement, distance, quarter-turn sector, held multi-target commit |
| System Behaviour | SYS-215, SYS-1410, SYS-1411, SYS-1412, SYS-1413, SYS-1414, SYS-1415 | live combat, course, pending targets, coupled control, ratio credits, paid retry, successor reset |
| Constraint | CON-183, CON-782 | finite continue stock, simultaneous target capacity |
| Information | INF-489, INF-490 | sector/aim/lock state, vitality and credited closeout |
| Objective | OBJ-002, OBJ-288 | optional points, boss-to-successor terminal |
| Time | TIM-003 | pausable concurrent progression |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `504` (`GAME-0001`–`GAME-0504`).
- Exact genome matches: none.
- Tied near matches: `GAME-0360` — Space Invaders (`5 / 28 = 0.178571`).
- Supported combination subsets: none.
- Scan date: 2026-10-06.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0360` — Space Invaders | `ACT-161`, `SYS-215`, `CON-183`, `OBJ-002`, `TIM-003` | Both combine aimed live combat, finite recovery stock and optional points. Space Invaders exposes one fixed lateral arena, one active upward projectile, erodible fortresses, a shrinking formation and a one-time point-earned base. Panzer Dragoon advances a 3D route, changes attack sectors, queues and releases several homing targets, pays a credit to retry the entire episode and replenishes credits from episode destruction proportion before restored successor control. | Near, `5 / 28 = 0.178571` |

## Taxonomy impact

Twelve additions and seven unchanged English transfers form the nineteen-gene
packet under [TAXONOMY_CHANGE_242](../../../research/taxonomy-changes/TAXONOMY_CHANGE_242.md).
No earlier signature, published mapping or public corpus is changed. A named
whole-packet salience review partitions seven defining, six structural and six
supporting uses without numeric weights. FAM-010 supplies the reused real-time
pressure boundary; no other family is added merely for an automatic route.

## Negative results

- SYS-1119 does not transfer unchanged: its definition includes an advancing
  checkpoint, whereas the original manual's admitted retry starts the current
  episode and no intermediate checkpoint is established. Do not weaken the
  earlier definition to manufacture reuse.
- ACT-609 does not transfer: its cockpit/exterior driving pair is not this
  dragon's three following distances. ACT-610 transfers only distance changes,
  not shoulder attack-sector changes and their body-control consequence.
- ACT-663 does not transfer: it arms finite carried missiles and permits
  cancellation before a separate fire command, rather than requiring held
  sweep acquisition and release to fire the queued dragon volley.
- SYS-1185 does not transfer: automatic one-target identity retention while
  held fire continues differs from manually queued multi-target release.
- SYS-911 and SYS-497 do not transfer: automatic finite-life respawn or an
  immediate free fixed-origin reset differs from an explicit paid Continue.
- SYS-965 does not transfer: fixed cumulative score milestones differ from
  episode destruction proportion. OBJ-181 requires a selectable map, absent here.
- SYS-780 does not transfer: saved/restorable successor evidence is not provided
  by an observed in-run transition. Disk persistence is not inferred.
- SYS-578 is not asserted for an uninterrupted multi-episode health pool:
  successor energy restoration and finite continue stock retain separate roles.
- Universal initial credit, complete ratio thresholds, exact lock progression,
  input transfer coefficients and simultaneous lethal precedence remain open.

## Delta summary

This complete first-episode packet separates direct rider shots from queued
dragon homing attacks, attack sector from world-route authority, and current
energy from ratio-replenished paid retries.

## New facts

- [Confirmed | Direct | High] Original instructions distinguish a tapped shot,
  held acquisition of up to eight enemies and released homing volley (PD-003).
- [Observation | Corroborated | High] Two actual closeouts show different missed
  enemies and credit awards while both proceed to Episode 2 (PD-007).
- [Observation | Conflicting | Medium] Regional starting-credit disagreement
  remains visible; manual text is not silently treated as Western runtime (PD-008).

## New genes

- `ACT-690`, `ACT-691`; `SYS-1410`–`SYS-1415`; `CON-782`; `INF-489`,
  `INF-490`; `OBJ-288`: twelve bounded additions, not a whole-product signature.

## New combinations

- None: no verified proper subset was found in the complete scan.

## Taxonomy changes

- TAXONOMY_CHANGE_242 accepts twelve additions without older definition or
  signature mutations. Flat kill-point values remain parameters of OBJ-002, as
  in the retained Space Invaders decomposition, rather than a redundant gene.

## New questions

- Which exact original US disc revisions match the stated initial credit value?
- What full ratio-to-credit thresholds and overflow policy does that executable use?
- Which input axes are restricted in each non-forward sector, at what rate?
- Which targets and damage events are eligible for locks or rider-shot interception?

## Next recommended game

- [Hypothesis | Limited | Medium] GAME-0506 Avowed, only after this complete
  Panzer Dragoon unit, one local commit, clean-source checks and stop window.
- Optimisation criterion: contrast forced-route ranged targeting with released
  fantasy combat on a different platform.
- Backlog impact: no successor starts while GAME-0505 remains incomplete.

## Why this game

- [Observation | Corroborated | Medium] Original instructions plus attributed
  first-episode closeouts support a bounded multi-direction rail-combat packet
  with source-visible credit consequences rather than a generic genre label.

## Localisation review

- Ukrainian profile, complete scope, direct-play qualification, summaries,
  external labels, platform edition, twelve four-field gene pairs, nineteen
  six-field causal cards and the complete role note are authored and `verified`.
- Generic explanation prose is Ukrainian. Product names, controller labels,
  source labels, literal Continue / GAME / NORMAL and stable IDs are
  `retained-with-reason` because they identify the instructions, not a second
  translated research source. The canonical Panzer Dragoon title is retained
  without an unsupported supposed official Ukrainian title.
- The first-pass generic score candidate was rejected before admission; no
  existing canonical definition was broadened to force reuse.
