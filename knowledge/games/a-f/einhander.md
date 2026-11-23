---
game_id: GAME-0650
slug: einhander
game_title: Einhänder
analysis_status: reviewed
reviewed: 2026-11-22
combination_ids: []
gene_ids:
  action:
    - ACT-161
    - ACT-562
    - ACT-862
    - ACT-863
  system:
    - SYS-215
    - SYS-1410
    - SYS-1877
    - SYS-1878
    - SYS-1879
    - SYS-1880
  constraint:
    - CON-871
  information:
    - INF-602
  objective:
    - OBJ-002
    - OBJ-288
  time:
    - TIM-003
---

# Game: Einhänder

This analysis uses the [canonical vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary).

## Analysis scope

- Version / ruleset: original English North American commercial PlayStation
  disc SCUS-94243, released in 1998. The primary recording is attributed to
  that regional release. Its disc image and executable revision are unknown.
- Entry: select Astraea FGA Mk. I on Normal with the initial machine gun and
  manipulator, then gain control at the start of Stage 1 in the capital.
- Primary decision loop: steer inside the moving arena, disable carriers
  while leaving their weapons intact, close in to fit a recovered gunpod,
  then decide which mounted fire to use against the next wave or boss.
- Exit: defeat SPKB-03, see the Stage 1 receipt add 202,500 points to 279,420,
  and resume live flight and fire at the start of Stage 2.
- Included: authored scrolling, core-versus-armament targeting, live salvage,
  two fitted gunpod channels, reserve and condition, the hit gauge, the final
  boss and the additive stage result.
- Excluded: other fighters' slot and input rules, unlocked starting gunpods,
  secret-bonus triggers and detours, later stages, checkpoint reproduction,
  exact damage or attack timing, the Japanese edition and later downloads.
- Suggested later scope: replay an identical carrier with both mounts filled
  and isolate replacement selection, the precise refill cap and ammunition
  display order around firing and swapping.

## Direct-play status

No direct play was performed. The original North American manual and printed
product record establish the release and the action rules. The LongplayArchive
recording credits nikodem123asdf and identifies the US PlayStation game. Its
menu shows Astraea and its Stage 1 sequence contains the exact observed result.
A second US-attributed recording uses Endymion Mk. II, corroborating only the
shared flight and weapon-acquisition loop. The capture frames and visible
text were inspected in the background without audio. Physical button presses,
the recording environment and disc-image parity remain unverified.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
| --- | --- | --- | --- | --- | --- |
| EIN-001 | The scoped release is the English commercial North American PlayStation disc SCUS-94243. The recording shows the Normal difficulty menu and selection of Astraea FGA Mk. I with an initial machine gun and manipulator. | Observation | Corroborated | High | P1 pp. 6–9, 20; P2 printed product identifier; W1 02:50–03:25. The footage does not supply a disc checksum. |
| EIN-002 | The authored city route advances independently of screen-space steering. The fighter changes height and lateral position to line up manual fire or avoid hostile movement and incoming shots. | Observation | Corroborated | High | P1 controls and display, W1 03:30–04:20 and 07:08–08:39; W2 03:12–03:54. |
| EIN-003 | Destroy a carrier's core and preserve the gunpod to make it recoverable. A sparking named module can be reached by contact or the manipulator. In the record the first Vulcan appears on the ship and is fired into the next wave with ammunition expenditure. | Observation | Corroborated | High | P1 pp. 10, 13; W1 03:50–03:58 shows the label, mounted fire and falling Vulcan count. W2 03:18–03:42 supplies the shared salvage action under another fighter. The video does not isolate the precise physical input. |
| EIN-004 | Astraea can mount two gunpods with separate and concurrent use. Its switch command exchanges firing positions. Vulcan and Spreader occupy both channels in the same flight, and the shown order reverses. Position can change the role of a weapon. | Observation | Corroborated | High | P1 pp. 8–9, 11; W1 03:10–03:25 and 04:04–04:20. The front/rear Spreader effect is documented in P1. |
| EIN-005 | A fitted gunpod carries its own ammunition and condition. A matching pickup feeds and repairs that unit; spent or sufficiently damaged modules can be lost independently of the fighter. | Observation | Corroborated | High | P1 pp. 9–10 and W1 03:53–03:58, 07:36–07:46 and 08:35–09:29. The record shows separate reserves, the Wasp slot clearing and Vulcan changing condition. The independent ejection and matching repair rules are manual-based; the exact cause of each loss is unverified. |
| EIN-006 | The hit gauge credits different enemy components at different rates, increases its contribution when a gunpod causes qualifying destruction and declines without further credit. Destruction score uses the live multiplier. | Observation | Corroborated | High | P1 p. 14 gives the component and firing-source rules. W1 03:53–04:10 and 07:08–08:39 show live multiplier changes. No exact undisclosed decay timer is inferred. |
| EIN-007 | The walking SPKB-03 guarding the exit has distinguishable attack components and poses. Continue combat until its defeat, then proceed through the results to the next stage. | Observation | Corroborated | High | P1 pp. 13, 19; R1 gallery and Stage 1 descriptions; W1 07:08–09:29. The walking-to-low pose and visible beam are distinct observed states. |
| EIN-008 | The receipt credits 90 shot down, 9 gunpods gained, 1:29 boss time and 3 fighters remaining with 45,000, 4,500, 123,000 and 30,000 points respectively. The 202,500-point total moves the score from 279,420 to 481,920, which is visible again in live Stage 2. | Observation | Corroborated | High | P1 pp. 14–15 documents the four terms. W1 09:09, 09:14 and 09:29 establishes the scoped numbers and carry. |

## Basic data

- Analysis target: `PLAT-PLAYSTATION`, original English North American
  commercial disc SCUS-94243.
- Developer: Square. North American publisher: Sony Computer Entertainment
  America.
- Mechanical family: `FAM-010`, real-time system pressure.
- Checked: 2026-11-22.
- P1: [Original North American PlayStation instruction manual](https://www.videogamemanual.com/ps1/Einhaender%20%28USA%29.pdf).
  Controller, fighter and mount layout on pp. 6–9, salvage and parts on
  pp. 10–13, rules for score and continuation on pp. 14–15, final Stage 1
  machine in the briefing on p. 19.
- P2: [North American disc, packaging and serial](https://www.psxdatacenter.com/games/U/E/SCUS-94243.html).
  The product scans establish SCUS-94243. The site transcription does not
  establish a particular pressing or exact US street date.
- W1: [LongplayArchive, US PlayStation recording by nikodem123asdf](https://www.youtube.com/watch?v=XDmqKobR69U&t=183s).
  Fighter selection, first capture and expenditure, SPKB-03 defeat, receipt
  and return to live control at approximately 09:29.
- W2: [Wounded Turtle, US PlayStation Endymion Mk. II recording](https://www.youtube.com/watch?v=HAHMBaHaOak).
  Opening flight and salvage with a different fighter. Its spare channel
  behaviour is outside this packet.
- R1: [Zach Keene's firsthand mechanics and gallery guide](https://gamefaqs.gamespot.com/ps/197217-einhander/faqs/3840).
  Corroborates the ship distinction and identifies SPKB-03 as Drache.
  The US instruction manual names the same designation The Brute.

## Mechanical decomposition

### Action Genes

- ACT-161: line up directed fire on the carrier's reachable core and on
  hostile boss parts using the current weapons.
- ACT-562: steer continuously in both screen axes while the route advances.
- ACT-862: approach or reach an exposed hostile weapon to fit it in flight.
- ACT-863: switch the fitted guns between live firing positions while
  carrying their individual reserves forward.

### System Behaviour Genes

- SYS-215: resolve directly commanded attack effects and hostile attacks in
  real time.
- SYS-1410: advance the authored route independently of fighter placement.
- SYS-1877: separate carrier incapacitation from the preserved weapon's
  recovery eligibility.
- SYS-1878: accumulate and decay the destruction-weighted hit gauge and
  use it to multiply eligible points.
- SYS-1879: spend a fitted gunpod's finite reserve, restore it through a
  same-type recovery and remove it on depletion or sufficient damage.
- SYS-1880: add the separate stage-result bonus components to live score.

### Constraint Genes

- CON-871: admit two live gunpod positions and apply matching salvage to the
  existing weapon instead of adding another unit of that type.

### Information Genes

- INF-602: expose weapon names and salvage opportunities, individual reserves
  and condition, the live multiplier and points.

### Objective Genes

- OBJ-002: increase the accumulated score through live action and settlement.
- OBJ-288: finish the authored flight and terminal boss, see the credited
  result and regain control in the successor stage.

### Time Genes

- TIM-003: accept movement, fire and salvage inputs while waves and score
  opportunities continue in real time.

## Reproducible transitions

| State | Action or event | Result | Evidence |
| --- | --- | --- | --- |
| Normal settings and fighter menu | Choose Astraea and the initial equipment | Both gunpod indicators start empty as live city flight begins | EIN-001, EIN-002 |
| Vulcan carrier approaches | Hit the core and move into acquisition range while the module remains intact | The sparking carrier displays Vulcan around 03:51. The module is fitted by 03:53 | EIN-003 |
| Vulcan is fitted | Fire at the next formation | Mounted fire accompanies a falling reserve and live score rises. The HUD shows 746 at 03:53 | EIN-003, EIN-006 |
| Vulcan remains fitted | Acquire Spreader and switch the two positions | Both indicators are filled and change displayed order by 04:14. Each keeps its own reserve | EIN-004, EIN-005 |
| SPKB-03 moves and attacks after the city route | Steer across its separate attack zones, continue manual fire and clear the encounter | The boss collapses and the live score holds at 279,420 before adding the receipt | EIN-007, EIN-008 |
| The four Stage 1 bonus terms appear | Allow the result to settle and fly into Stage 2 | The score reaches 481,920 and is retained when ordinary steering and fire resume | EIN-008 |

## Strategic and experiential structure

The shot that disarms an enemy can remove the very equipment needed for the
next wave. Aim first at the component that leaves salvage available, then
judge whether moving close is worthwhile before the corridor carries the
opportunity away. Once both mounts are occupied, changing which direction a
gunpod covers can be more useful than emptying both reserves at once. The
boss-time term and the fading hit gauge place different values on quick
clearance and sustained scoring during combat.

## Replay and variation

The second recording supports the disable-to-acquire transition and the
shared scrolling route, then uses an Endymion craft that can keep spares.
It does not establish a repeat of Astraea's weapon assignments or the
481,920-point result. The original manual's two gunpod channels and the
observed order reversal supply the Astraea-specific boundary.

## Adjacent systems and history

The original release supports other fighters, alternate gunpods at launch
after qualifying saves and secret bonuses. The route beyond first control
in Stage 2, later equipment and other ships' internal inventory are outside
the admitted signature.

## Normalised genome

| Type | Stable genes | Role |
| --- | --- | --- |
| Action | ACT-161, ACT-562, ACT-862, ACT-863 | Aim, steer, acquire and exchange mounted weapons |
| System Behaviour | SYS-215, SYS-1410, SYS-1877, SYS-1878, SYS-1879, SYS-1880 | Resolve combat, run the course, enable salvage, operate the hit gauge and settle the stage |
| Constraint | CON-871 | Two independent active channels without duplicate weapons |
| Information | INF-602 | Read the salvage opportunity, reserves, damage and scoring conditions |
| Objective | OBJ-002, OBJ-288 | Build score and reach the next stage through its required terminal encounter |
| Time | TIM-003 | Accept commands during live progression |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `649` (`GAME-0001`–`GAME-0649`).
- Exact genome matches: none.
- Tied near matches: `GAME-0587` — Panzer Dragoon II Zwei (`7 / 25 = 0.280000`).
- Supported combination subsets: none.
- Scan date: 2026-11-22.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
| --- | --- | --- | --- |
| [Panzer Dragoon II Zwei (GAME-0587)](../m-r/panzer-dragoon-ii-zwei.md) | ACT-161, ACT-562, OBJ-002, OBJ-288, SYS-1410, SYS-215, TIM-003 | Both put directed fire and bounded steering inside an automatic flight route through a boss and credited handoff. Zwei changes attack sectors and releases dedicated volleys. Einhänder lets the player disable a carrier, recover an intact gunpod and exchange its firing position with another live mount. | Near, `0.280000` |

## Taxonomy impact

ACT-771 transfers an actively held hostile hand weapon. ACT-862 takes
salvage after incapacitation and equips it in flight. ACT-550 selects one
active vehicle weapon from a spare arsenal. ACT-863 and CON-871 instead
preserve two concurrently usable channels and reject a duplicate type.
SYS-1680 grants a fixed weapon card after defeat. SYS-1877 preserves or
eliminates salvage according to part damage. SYS-1844 refreshes a short
chain through defeats or tokens. SYS-1878 weights the damaged component
and firing source. SYS-1879 handles a mounted item's finite reserve and
repair, while SYS-1880 accounts for all four independent receipt terms.
The original Panzer Dragoon boss-to-successor objective applies here with
a different settlement calculation.

## Negative results

- The number of gunpods gained on the receipt is a cumulative count. The
  fighter does not carry nine gunpods at once.
- Matching gunpod salvage restores the existing instance rather than
  making a duplicate firing channel.
- The footage supports the order of the observed game states. Physical
  buttons, exact attack timing, replacement precedence and the refill cap
  are not inferred from the video.
- The walking boss's explosion alone is not the terminal verification.
  The receipt and renewed control follow it.

## Delta summary

Fifteen scoped genes, with eight additions and seven reuses. The study
reaches playable Stage 2 after one completed opening stage.

## New facts

- Destroying a core with armament intact creates a recoverable state that
  differs from destroying the armament itself.
- A change of firing position preserves a gunpod's own reserve, but can
  change where its fire reaches.
- The stage receipt adds points to the live score through four individually
  visible components.

## Principles and design implications

Give players a tangible reason to choose a target part instead of always
firing at the largest surface. Expose the newly available item promptly
inside a moving level, then preserve its own reserve across reassignment.
An item can matter for survival now and still add credit during settlement.

## Puzzle or game generation potential

Build a short scrolling route with two incoming carrier formations. Give one
optional armament that survives only one destruction ordering. Let the two
fitted positions cover different approaches and expose both reserves. End
with a multi-part guardian and a separately itemised receipt.

## New genes

- ACT-862
- ACT-863
- SYS-1877
- SYS-1878
- SYS-1879
- SYS-1880
- CON-871
- INF-602

## New combinations

None. All 274 verified combination signatures were checked.

## Taxonomy changes

[TAXONOMY_CHANGE_396](../../../research/taxonomy-changes/TAXONOMY_CHANGE_396.md).

## New questions

With both mounts filled and a third type available, which input or mount
state determines replacement? Repeat the same capture at both positions to
separate automatic placement from the swap command.

## Next recommended game

The Plucky Squire, native commercial PlayStation 5 base game. Follow an early
transition between the page and the exterior through a changed reachable
objective and its playable successor.

## Why this game

Live recovery makes the same enemy part a threat, a potential resource and a
contributor to score. The exact first-stage receipt closes the experiment.
