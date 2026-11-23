---
game_id: GAME-0600
slug: nba-street-vol-2
game_title: "NBA Street Vol. 2"
analysis_status: reviewed
reviewed: 2026-11-21
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-052
    - ACT-411
    - ACT-412
    - ACT-414
    - ACT-798
    - ACT-799
    - ACT-800
  system:
    - SYS-459
    - SYS-757
    - SYS-760
    - SYS-762
    - SYS-1764
    - SYS-1765
    - SYS-1766
    - SYS-1767
    - SYS-1768
  constraint:
    - CON-398
    - CON-845
  information:
    - INF-178
    - INF-291
    - INF-562
  objective:
    - OBJ-325
  time:
    - TIM-003
---

# Game: NBA Street Vol. 2

Comparison uses the [canonical vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
The controller layout, team members, target and clock duration are
instance parameters.

## Analysis scope

- Version / ruleset: original North American English PlayStation 2
  retail base game, SLUS-20651, April 2003. The preserved original
  disc is identified as v1.00. The capture labels and prompts do
  not independently identify their disc revisions. Release listings
  differ on the exact April date, so only the month is asserted.
- Structured analysis target: PLAT-PLAYSTATION-2 in
  `knowledge/platforms/games.json`. Use standard PS2 controls and
  regular Pick Up Game scoring with target 21, no starting points,
  and a 24-second possession clock. Any eligible sides, triples and
  half court are parameters. The ordinary format supports a local
  match against the computer or one opposing controller.
- Primary decision loop: control one of three players, move or
  pass, vary tricks and choose which basket attempt to take.
  On defense, switch, steal, block or rebound for the next attack.
  Build the team Gamebreaker opportunity and choose to shoot,
  pocket the first charge or remove a rival's pocketed charge when
  eligible. Finish at a lead that satisfies the configured target.
- Entry and exit: begin at Play It → Pick Up Game. Choose sides,
  players, court and ordinary match parameters, then contest the
  opening tip. Stop at the postmatch result of this match, before
  any rematch, reward use or other career progression.
- Included: live three-on-three, ordinary scoring, the possession
  clock, personal Turbo expenditure, style and combo credit, both
  Gamebreaker levels, expiry and pocket/cancel decisions, and
  the result. The normal arc separates one- and two-point attempts.
- Excluded: multiplayer arrangements above two controllers, cheats,
  custom players, unlocks and reward spending, Street School,
  Be a Legend, NBA Challenge, alternate My Rules modes, later
  ports, exact meter coefficients and edge-of-rim clock rules.
- Potential scoped modules: one Trick Point Challenge settlement,
  Street School progression or a bounded Be a Legend challenge.
- Direct-play status: no direct play. The original printed PS2 rules
  describe setup, controls and scoring. Static samples from three
  independently attributed PS2 recordings show setup, live play,
  a clock violation, special-shot presentation and terminal
  results. The margin rule is documented by contemporary
  hands-on evidence. No video or audio was played. Native inputs,
  sub-second reset rules and the score floor were not tested.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
| --- | --- | --- | --- | --- | --- |
| NS-001 | The original English PlayStation 2 retail target is SLUS-20651; Pick Up Game chooses sides, three starters, court and rules. | Confirmed | Corroborated | High | P1 printed pp. 11–13, P2, P3, W1 2:30–4:50 and 11:30–13:20. |
| NS-002 | The tip is a timed Circle press; move, pass, contextual shot, trick, defensive switch, steal and block or rebound use the stated PS2 controls. | Confirmed | Corroborated | High | P1 pp. 6, 8–9, 14–15; W1 4:40–7:10; H1. |
| NS-003 | Street scoring uses one inside the arc and two outside. The selected 24-second limit can end a possession in a clock violation. | Observation | Corroborated | High | P1 pp. 12–13, 16; H1, H2; W3 24:20–24:40. |
| NS-004 | Personal Turbo and match score differ from Trick Points and the team special gauge. Links, fakeout credit, defensive exceptions and repetition affect style settlement. | Confirmed | Corroborated | High | P1 pp. 14–16, H1, H2, W1 5:20–6:50. |
| NS-005 | Style actions feed the team meter. It may decay or lose progress to blocks and steals. A full meter only permits a timed opportunity; shooting or expiry empties the live charge. | Confirmed | Corroborated | High | P1 pp. 14, 16–17; P2, H1, H2, W1 16:50–18:10. |
| NS-006 | A side with possession can bank its first live chance, refill toward Level 2 or cancel the opponent's stored chance using the indicated controls and prerequisites. | Confirmed | Corroborated | High | P1 pp. 9, 17; P2, H2; cancellation itself was not isolated in footage. |
| NS-007 | A made Gamebreaker credits the shooter and debits the opposition. The authorial table distinguishes four level-and-range branches. | Confirmed | Corroborated | High | P1 pp. 16–17; H1, H2; W1 17:20–18:10 corroborates the presentation family and changing scores. |
| NS-008 | Standard play to 21 requires a lead of two. A Foster Beach capture shows a late 17–20 state and a reported 17–21 final. | Observation | Corroborated | High | P2, H2, W2 15:20–16:30; W1 21:10–21:30 shows a separate end. |
| NS-009 | Clock reset at the rim, exact buildup and decay rates, cancel reset amount and deductions at the zero floor are unresolved. | Observation | Limited | Medium | P1 pp. 13–17 and static-frame granularity; no controlled trial. |

## Basic data

- Release / origin: NuFX and EA Canada, published by Electronic Arts
  under EA Sports BIG, original spring 2003 North American release.
- Platform or physical form: retail PlayStation 2, single-controller
  solo or each side with one local controller in this scope.
- Puzzle family: real-time system pressure (FAM-010), because possession
  and the short Gamebreaker opportunity end on separate clocks; agent
  routing and coordination (FAM-015), because direct control and the
  ball travel among coordinated attacking and defending teammates.
- P1: [EA North American PS2 instruction booklet](https://www.videogamemanual.com/PS2/NBA%20Street%20Vol.%202%20%28USA%29.pdf),
  printed controls, Pick Up settings and Gamebreaker point chart.
- P2: [EA announcement reproduced by Nintendo World Report](https://www.nintendoworldreport.com/pr/8180/nba-street-part-deux),
  pre-release announcement of PS2, standard target and Level 2.
- P3: [North American retail copy and disc identifier](https://www.vgcollect.com/item/1942)
  with [original disc preservation metadata](https://redump.info/discs?dumper=robbot&order=desc).
  The preservation catalogue applies v1.00 to the original disc.
  April dates from release catalogues are recorded only to month.
- H1: [Digital Press hands-on PS2 review](https://www.digitpress.com/reviews/nbastreet2.htm),
  match flow, the 24-second clock, Turbo and the two-sided score swing.
- H2: [Gaming Target hands-on PS2 review](https://www.gamingtarget.com/article.php?artid=3303),
  firsthand ordinary scoring, required lead and deeper charge option.
  Its general Level 2 example is not the complete scoring chart.
- W1: [GamePlayStation console-attributed PS2 recording](https://www.youtube.com/watch?v=WhRID8E9t7Q),
  beginning, match sequence and terminal statistics. Only static
  samples were inspected.
- W2: [Cage Vs Cage PS2-labelled local match](https://www.youtube.com/watch?v=thcMp4swdHw),
  independently labelled match to 21 and displayed result. The
  player footage is edited. Only game images and the end score were
  used, not the surrounding show.
- W3: [Retro Jay PS2-labelled match](https://www.youtube.com/watch?v=F05NZtfwzj8),
  visible possession-clock warning and violation. The clock run is
  independent evidence; it is not an extension of W1 or W2.
- Claim IDs: NS-001–NS-009.

### Reproducible route evidence

1. Enter Play It, then Pick Up Game. Assign the two sides and choose
   each side's starting trio, then choose a court. W1 11:30–12:30
   shows these labelled screens on the second entry. For the scoped
   replay select the regular format, Play To 21, no spot points and
   24 Seconds under My Rules if needed. The menu sequence is visible;
   these target parameters are prescribed here, not inferred for every
   capture. Begin with Play Game. At the opening toss, use Circle at
   the apex as printed in the PS2 controls. W1 13:10–13:40 shows NYC
   Rec Center, 0–0 live setup and the first action.
2. Move the current player with the left stick or directional pad.
   With the ball, Cross passes and Circle starts a shot or finish
   suited to the approach. Use Square for a trick, optionally with
   Turbo inputs. W1 5:20–6:50 shows visible trick/combo notices,
   baskets and play after the changes in ball control. On defense
   use Cross to switch, Square to steal and Triangle for a block
   or rebound. If a shot misses, the ball can stay in contest.
3. Score inside the arc or from outside for one or two points. Do
   not hold the same possession indefinitely. In W3 at 24:20–24:40,
   one possession runs into a visible Shot clock violation notice
   before play continues. The timed violation is reproduced by
   letting the enabled clock run down with no attempt; an exact rim
   reset is outside the verified rule.
4. Mix eligible tricks and finish the attack. A fakeout can earn
   extra Trick Points, while repeated tricks earn less. Normally
   link the combo to a made basket; some defensive block combos
   settle without one. Check the separate Turbo reserve and team
   gauge. W1 16:50–18:10 samples the changing team meter, the special
   sequence near 17:40 and the return to live play. It does not
   isolate all four scoring branches or the input that caused each.
5. With full live gauge and possession, press Circle with two Turbo
   buttons to attempt the Gamebreaker. An eligible first opportunity
   can instead be pocketed with Select. Refill the live meter with
   that first charge still stored to qualify for Level 2. If the
   opponent has a stored charge, the side controlling the ball can
   use a ready charge and the Turbo plus Select input to cancel it.
   This is the manual-derived branch; a separate cancellation is
   not asserted from the sampled footage.
6. Continue until one side has at least 21 and leads by at least
   two. W2's late Foster Beach scoreboard shows 17–20 at 15:20–15:30,
   with the final play around 15:40. The displayed Rundown at 16:20
   records 17–21. W1 shows terminal statistics after its first match
   at 11:00 and a separate postmatch exit prompt after the second.
   The specific missing deuce branch is documented by H2, not
   presented as a controlled measurement.

Claim IDs: NS-001–NS-009. Timestamp pairs locate stills; no unobserved
intermediate frame is used to assign an exact score delta.

## Mechanical decomposition

### Action Genes

- ACT-008: directly run the controlled player to a lane, opponent,
  ball or shooting position.
- ACT-052: Cross transfers the defensive control locus while
  the other players stay active in the same possession.
- ACT-411: choose the contest sides, starters, court and Pick Up
  parameters before committing the match.
- ACT-412: pass the held ball toward a teammate with Cross,
  including a timed delivery to an eligible airborne recipient.
- ACT-414: attempt an interception with Square or a shot block
  with Triangle. Position and the opponent's live action matter.
- ACT-798: Circle commits a contextual shot, dunk or layup from
  the current approach. A Turbo modifier can change finish tier.
- ACT-799: use Square and optional Turbo inputs for contextual
  dribble tricks that may unbalance the defender.
- ACT-800: choose between a special attempt, pocketing and an
  available cancellation while holding the ball and charge.
- Claim IDs: NS-001, NS-002, NS-004–NS-006.

### System Behaviour Genes

- SYS-459: non-controlled teammates fill live positions and
  can run to the hoop for a pass; defenders respond to the ball.
- SYS-757: resolve one ball through possession, dribble, passes,
  attempted baskets, deflections and the loose-ball contest.
- SYS-760: resolve the miss through the rebound or loose
  ball so either side can begin the next possession.
- SYS-762: a legal ordinary basket updates the team's score,
  for one inside the arc or two outside.
- SYS-1764: linked eligible style events can raise the payout;
  usually a made basket settles the combination. Repeat credit,
  non-fakeout cases and defensive block combos have separate rules.
- SYS-1765: style play fills the live team meter, inactive play
  and defensive interventions can drain it, and its ready window
  can expire without generating a shot.
- SYS-1766: retain the first pocketed opportunity apart from
  the next fill. The other team can counter it with possession
  and a live opportunity before the upgrade is realised.
- SYS-1767: the made special attempt credits one side and
  deducts from the other, with different values by level and range.
- SYS-1768: the personal reserve pays more Turbo for higher
  tier moves; this is independent of the team gauge.
- Claim IDs: NS-002–NS-007.

### Constraint Genes

- CON-398: each live side has three players, with at most one
  directly controlled body for the local authority on that side.
- CON-845: the configured shot clock terminates an attack out
  of time if it has no accepted attempt. Exact rim
  contact and reset edges were not determined.
- Claim IDs: NS-001–NS-003, NS-009.

### Information Genes

- INF-178: read the ball, current control marker, nearby
  teammate routes, defense, arc and rim from the live court view.
- INF-291: after the deciding score, the result and statistics
  identify what settled and who won.
- INF-562: the HUD distinguishes match score, Trick Points,
  personal Turbo, ready team gauge and pocketed indication.
- Claim IDs: NS-002, NS-004–NS-008.

### Objective Genes

- OBJ-325: meet or exceed the configured target with the required
  lead in match points. Reaching 21 without the lead is not enough.
- Claim IDs: NS-001, NS-008.

### Time Genes

- TIM-003: player movement, ball motion and opponent reactions
  continue before the action or possession becomes fixed.
- Claim IDs: NS-002, NS-003, NS-005.

## Reproducible transitions

| Before | Action | Resolution | What it establishes | Claim ID |
| --- | --- | --- | --- | --- |
| Rules are still editable | Choose sides and trios, court and regular 21-point match | Configured match begins at 0–0 before the tip | Setup precedes mutable possessions | NS-001 |
| Ball is at the opening toss | Press Circle at the apex | Tip can direct the live ball into play | The player can take part in the opening contest | NS-002 |
| Current possession, defender in reach | Vary a trick, pass or finish | A successful fakeout can free the carrier, or the defender can win the ball | Style has a ball-control consequence apart from scoring | NS-002, NS-004 |
| Configured clock nearly exhausted | Allow expiry without a qualifying attempt | Violation ends the possession | Waiting has a bounded cost | NS-003 |
| Eligible style chain with no defensive exception | Complete a basket | The combo settles with linked credit | Ordinary match points and style points differ | NS-003, NS-004 |
| Lit team meter and own possession | Shoot with Circle and two Turbo buttons | Attempt consumes the opportunity; a make can swing both scores | Firing alone does not debit the opponent | NS-005, NS-007 |
| Full Level 1 opportunity, own possession | Press Select | First opportunity is stored; refill is needed | The first charge and live meter are distinct | NS-006 |
| Opponent has pocketed a charge, own charge and ball ready | Press a Turbo button with Select | The opponent's pocketed charge is removed | Cancellation targets storage before the shot | NS-006 |
| Stored first charge and another full meter | Commit the special attempt | Level 2 is eligible | The stronger swing needs two builds and a stored state | NS-006, NS-007 |
| A live opportunity is unused | Let its window expire | Live gauge empties | A charge opportunity need not settle with a shot | NS-005 |
| A side reaches the target with the required lead | Resolve the deciding basket | The match exits to results | Victory compares ordinary match scores | NS-008 |

### Special-shot settlement

| Made shot | Score added to shooting side | Score deducted from rival |
| --- | --- | --- |
| Level 1 short, including dunk range | 1 | 1 |
| Level 1 long | 2 | 1 |
| Level 2 short, including dunk range | 2 | 3 |
| Level 2 long | 2 | 4 |

P1's printed chart distinguishes short and long. The deduction
column is the nominal rule when enough rival points are present;
low-score floor handling was not verified. Claim IDs: NS-005–NS-009.

## Strategic and experiential structure

The attack has two linked incentives. An immediate open basket improves
the match score; a varied attack builds the opportunity to remove points
from the opposing side. Waiting can help a defender run out a rival
opportunity but is constrained when holding the ball. Banking Level 1
for a stronger shot gives up current use and exposes stored progress
to an opponent with a ready meter and possession. Personal Turbo
makes elaborate moves cost more even when the team gauge is growing.
Claim IDs: NS-002–NS-009.

## Replay and variation

Eligible teams, starter choices and courts change local approach and
coverage. Pick Up rule settings allow other targets, spot points
and clock options, and the booklet names rule presets outside this
match. No exact cross-platform equivalence or identical player
attribute effect was tested. Claim IDs: NS-001–NS-003, NS-009.

## Adjacent systems and history

The sequel's distinguishable option is to retain a first Gamebreaker
for a second-level shot. The EA announcement identifies this as a
new sequel feature. Roster unlocking, career points and alternate
settlement modes do not determine a normal Pick Up result. Claim IDs:
NS-001, NS-006, NS-008.

## Normalised genome

| Type | Stable genes | Role |
| --- | --- | --- |
| Action | ACT-008, ACT-052, ACT-411, ACT-412, ACT-414, ACT-798, ACT-799, ACT-800 | Navigate, switch, configure, pass, defend, shoot, trick and use charge |
| System Behaviour | SYS-459, SYS-757, SYS-760, SYS-762, SYS-1764, SYS-1765, SYS-1766, SYS-1767, SYS-1768 | Team, ball, rebounds, scoring, style, readiness, bank, score swing and Turbo |
| Constraint | CON-398, CON-845 | One control locus per human side and a configured shot clock |
| Information | INF-178, INF-291, INF-562 | Court, terminal result and distinct live gauge states |
| Objective | OBJ-325 | Meet goal score with the minimum lead |
| Time | TIM-003 | Real-time response to live play |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `599` (`GAME-0001`–`GAME-0599`).
- Exact genome matches: none.
- Tied near matches: `GAME-0241` — NBA 2K26 (`13 / 37 = 0.351351`).
- Supported combination subsets: none.
- Scan date: 2026-11-21.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
| --- | --- | --- | --- |
| [NBA 2K26](nba-2k26.md) (`GAME-0241`) | `ACT-008`, `ACT-052`, `ACT-411`, `ACT-412`, `ACT-414`, `CON-398`, `INF-178`, `INF-291`, `SYS-459`, `SYS-757`, `SYS-760`, `SYS-762`, `TIM-003` | Both run one live basketball match with control transfer, team AI, possession, defense, weighted baskets and a verified result. NBA 2K26 uses release timing and a regulated period structure. Street uses a score target with a lead, and varied tricks create a bankable special opportunity with a two-sided score change. | 13 shared of 37, Jaccard 0.351351 |

### Preserved research notes

- Classification result: New gene.

## Taxonomy impact

- [TAXONOMY_CHANGE_346](../../../research/taxonomy-changes/TAXONOMY_CHANGE_346.md)
  records eleven active definitions and the basketball boundaries reused.

## Negative results

- Separate release timing under ACT-413 is not established for the
  contextual Circle attempt in this manual and route.
- A clock violation establishes CON-845. It does not prove the specific
  timely release and rim contact rule in CON-585.
- Ordinary baskets credit the shooter side. Gamebreakers cannot be
  collapsed into ordinary weighted baskets because they deduct rival
  points and use an earned opportunity.
- Trick Points are not match points. A full style gauge does not by
  itself score, discharge a shot or stop the match.
- The score target and minimum lead do not require finishing
  regulation periods or spending a finite allowance of shots.

## Delta summary

## New facts

- [Confirmed | Corroborated | High] The original PS2 control layout and
  format distinguish the tip, attacking and defensive use of the
  same buttons, ordinary score and possession time. NS-001–NS-003.
- [Confirmed | Corroborated | High] Style can earn a limited special
  opportunity. A retained first opportunity and refill qualify for
  a stronger attempt, but the opponent can remove the banked state. NS-004–NS-006.
- [Confirmed | Corroborated | High] The successful special attempt
  changes both scores by level and range. NS-007.
- [Observation | Corroborated | High] The 17–21 result settles the game;
  the margin requirement has independent firsthand documentation. NS-008.

## New genes

- [Observation | Corroborated | Medium] ACT-798, ACT-799, ACT-800,
  SYS-1764, SYS-1765, SYS-1766, SYS-1767, SYS-1768, CON-845, INF-562 and OBJ-325.

## New combinations

- [Observation | Direct | High] No new combinations.

## Taxonomy changes

- [Observation | Corroborated | High] TAXONOMY_CHANGE_346.

## New questions

- Which exact rim and timing events reset or preserve the clock?
- How does a cancellation reset the spending team's live gauge?
- How is a rival deduction settled when the rival has too few points?

## Next recommended game

- [Hypothesis | Limited | Medium] Cassette Beasts on the full
  Android release under Selection 049. Scope one opening recording
  and battle to a visible result.

## Why this game

- [Hypothesis | Limited | Medium] One two-sided contest ties a style
  economy to the ordinary score without equating the two. Banking
  creates both a stronger later possibility and an opening for counterplay.
