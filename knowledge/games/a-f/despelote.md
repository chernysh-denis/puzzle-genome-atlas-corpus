---
game_id: GAME-0631
slug: despelote
game_title: "despelote"
analysis_status: reviewed
reviewed: 2026-11-22
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-839
  system:
    - SYS-457
    - SYS-1833
  constraint: []
  information:
    - INF-268
  objective: []
  time:
    - TIM-003
---

# Game: despelote

This analysis uses the [canonical vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary).

## Analysis scope

- Version / ruleset: Panic's native commercial PlayStation 5 download,
  released May 1, 2025. The linked US product is PPSA15428. The target
  permits English screen text. The worked video is attributed to PS5
  and uses Spanish prompts, while the PS5 review independently confirms
  the controller rule. The capture's region and patch are unverified.
- Primary decision loop: approach a loose ball in the schoolyard, use
  immediate or wound-up contact to send it into open space, follow its
  free travel and play a returned ball before the recess scene closes.
- Entry: the June 3, 2001 school sequence after the introductory
  history. Use the first announced recess and walk to the shared ball
  near the cones.
- Exit: return toward the school as recess ends. In the worked route
  the adult calls the children back and the scene cuts to the car
  ride. The independent English trace includes an intervening
  classroom moment before the car ride.
- Included: local first-person movement, on-screen kick prompts,
  immediate and wound-up kicks, free ball motion, actual peer reply
  and the separate end of the playground window.
- Excluded: title-screen soccer game rules, official match score,
  results of later football sessions, later school segments, physical
  stick telemetry, internal timing constants, haptics, subtitles as an
  audio transcription and PS4, Windows and Xbox control details.
- Suggested later scope: compare the same recess without playing the
  ball and separately analyse the television mini-game.

## Direct-play status

No direct play was performed. W1 identifies PS5 and shows PlayStation
R2 notation in the school yard. The store and developer establish the
native PS5 product. The US catalogue identifier belongs to the store
and is not inferred from the video. The labels, positions, visible
kicking animation and scene transition were read from silent extracted
frames. R1 and R2 provide independent firsthand accounts from PS5.
W2 independently illustrates the movement through the same story beat
with English text; its platform and patch are unconfirmed and it does
not substantiate PS5-only controls.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
| --- | --- | --- | --- | --- | --- |
| DSP-001 | Panic released a commercial native PS5 edition on May 1, 2025. The US store lists PPSA15428 with English screen text. | Confirmed | Direct | High | P1, P2. |
| DSP-002 | The first school recess allows local first-person movement to the loose ball near cones. Near the ball, the prompt tells the player to push the right stick to kick. | Observation | Corroborated | High | W1 8:39–9:10 and 9:54–10:20. W2 6:31–7:10 illustrates the same route, and P2 describes kicking as first-person ball interaction. |
| DSP-003 | The right stick can be pushed for an immediate kick, or pulled back to charge before a forward kick. The ball visibly departs and remains a physical object that can be approached again. | Observation | Corroborated | High | W1 10:10–10:25 and 10:29–10:47, including the prompt, foot animation and outgoing ball. R1 describes pulling and pushing on PS5. P2 identifies the physics-based ball. |
| DSP-004 | In the recess exchange, a peer plays the one shared ball toward the avatar. The avatar kicks it away again, and peers can receive and return it while the original avatar remains under control. | Observation | Corroborated | Medium | W1 11:41–11:58, including the local kick around 11:46 and the next peer kick around 11:55–11:58. W2 7:20–9:20 supplies a distinct English-text exchange. R1 and R2 corroborate informal play with other children. Exact peer eligibility and routing are unverified. |
| DSP-005 | The announced recess ends while local play could continue. The route leads away from the ball, the teacher calls the children back and the story advances to the car ride. There is no match tally or required total of passes in the observed settlement. | Observation | Corroborated | High | W1 8:35–8:44 and 13:05–14:32. W2 6:20–6:40, 9:19–10:43 shows recall, the classroom and car. R1 reports play spaces that give way to the next scene without competitive objectives. |

## Basic data

- Analysis target: `PLAT-PLAYSTATION-5`.
- Developers: Julián Cordero and Sebastián Valbuena. Publisher: Panic.
- Mechanical family: `FAM-007`, physics and object manipulation.
- Checked: 2026-11-22.
- P1: [PlayStation Store product UP3971-PPSA15428_00-0434180303206305](https://store.playstation.com/en-us/product/UP3971-PPSA15428_00-0434180303206305).
- P2: [Developer press kit](https://despelote.game/presskit/).
- R1: [Push Square firsthand PS5 Pro review, May 1, 2025](https://www.pushsquare.com/reviews/ps5/despelote).
- R2: [Couch Soup firsthand base PS5 account](https://couchsoup.com/video-games/despelote-will-hit-sports-fans-in-the-feels/).
- W1: [Project Páez PS5 recording](https://www.youtube.com/watch?v=Tf1WbRHlaMw&t=594s).
- W2: [iamhijak English-text recording](https://www.youtube.com/watch?v=_zZJDBJ9ULY&t=378s).

## Mechanical decomposition

### Action Genes

- ACT-008: move Julián between the school, cones and the patch of
  grass to reach the ball for the next touch.
- ACT-839: push the right stick for a quick kick, or pull back
  then push for a wound-up kick while in reach of the loose ball.

### System Behaviour Genes

- SYS-457: the same football moves freely under scene physics
  between contacts. A kick is an impulse rather than a handover token.
- SYS-1833: a classmate may receive and kick that free ball back
  without the player changing controlled character. No AI rule
  promising a return or an exact target is inferred.

### Constraint Genes

Ball reach is the kick's precondition. The route has no demonstrated
formal possession region, offside rule or result condition based on
goals. Reach does not warrant an additional constraint gene.

### Information Genes

- INF-268: the current movement or kick hint appears when the
  corresponding tutorial step becomes relevant. The authored hint
  can change from quick kick to winding up.

### Objective Genes

The recess offers informal play and then ends with a story transition.
No objective gene is admitted. The instruction to return to class is
evidence of the narrative boundary rather than a scored win.

### Time Genes

- TIM-003: actions continue while the limited recess progresses to an
  authored end. The school announcement belongs to the story clock
  and does not establish the conversion to real elapsed time.

## Reproducible transitions

| State | Input or event | Result | Evidence |
| --- | --- | --- | --- |
| The June 3 school scene announces recess | Walk toward the cones and approach the ball | The reachable ball and currently relevant kick prompt appear | DSP-002 |
| The ball is in range | Push the right stick forward | The football separates and can be approached at its new position | DSP-003 |
| Another touch is available | Pull the right stick back and push forward | The animated foot sends a wound-up ball out through the same yard | DSP-003 |
| Peers share the yard and a ball | Play the incoming ball back across the grass | A peer encounters the ball and a later visible return travels through reach again at 11:55–11:58 | DSP-004 |
| Recess moves toward its end | Move away from the yard as the adult recalls the children | The school sequence closes and the car ride is visible by 14:30 in W1 | DSP-005 |

## Strategic and experiential structure

The physical skill is getting within reach and deciding when to
commit the direction and force. After contact the target can move,
misjudge the ball or return it. The player then reacquires its
position. The larger scene follows the school day. A successful
exchange is local play and carries no visible competitive tally into
the following car sequence.

## Replay and variation

The two recordings move differently before the recess closes. The
worked PS5 route visibly pauses once and later resumes. These traces
do not establish elapsed real time, the shortest way to advance, or
whether any ball contact is necessary to advance. A release test
without ball contact would settle that last question.

## Adjacent systems and history

The prologue's in-world football game uses a separate overhead
playfield with teams and a score display. W1 shows it recede into
the television before the school episode. The score and any
in-world achievements belong to a separate analysis.

## Normalised genome

| Type | Stable genes | Role |
| --- | --- | --- |
| Action | ACT-008, ACT-839 | Walk to the ball and kick without or with a wind-up |
| System Behaviour | SYS-457, SYS-1833 | Keep the ball physical through contact and allow peer replies |
| Constraint | None | Kick reach is owned by ACT-839 |
| Information | INF-268 | Introduce the currently relevant control |
| Objective | None | No scored outcome is observed for recess play |
| Time | TIM-003 | Permit ongoing decisions until the recess ends |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `630` (`GAME-0001`–`GAME-0630`).
- Exact genome matches: none.
- Tied near matches: `GAME-0391` — Uncharted 2: Among Thieves (`2 / 9 = 0.222222`).
- Supported combination subsets: none.
- Scan date: 2026-11-22.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
| --- | --- | --- | --- |
| [Uncharted 2: Among Thieves (GAME-0391)](../s-z/uncharted-2-among-thieves.md) | ACT-008, TIM-003 | Both allow local avatar movement while the scene advances. Uncharted 2 requires reaching stable ground while a carriage and its handholds fail. despelote leaves the player free to exchange kicks until the school episode closes, with no scored race to an exit. | Near, `0.222222` |

## Taxonomy impact

ACT-839 separates a directionally prepared kick against a loose ball
from a pass command that chooses a teammate. SYS-1833 separates the
peer's local reply from the shared motion of the ball itself. Existing
uses of ACT-267, SYS-457 and SYS-531 retain their original boundaries.

## Negative results

- No target-selection overlay, competitive counter or pass quota was
  demonstrated in the schoolyard exchange.
- The two routes give no independent no-contact transition. They do
  not settle the effects of abstaining, requesting a pass or missing
  an unobserved contact window.
- The television mini-game uses a distinct play scale and result
  surface. No schoolyard goal or team rule is imported from it.

## Delta summary

This first-person schoolyard packet admits six genes, with two new
definitions and no additional combination or family. It adds one
commercial PS5 record without changing earlier signatures.

## New facts

- The local prompt distinguishes a forward kick from preparing one
  by pulling back before pushing the same control.
- A returned ball can remain part of the free world and be played again
  while control stays with the original avatar.
- The demonstrated recess gives way to the car ride without displaying
  a yard score or tally of successful exchanges.

## Principles and design implications

- Separate a legible kick action from the ball state it creates and
  the next person's opportunity to respond.
- Let an authored scene end after meaningful optional local activity
  without converting that activity into a score or pass quota.
- Use control prompts for the current action without suggesting that
  a charged kick automatically targets another person.

## Puzzle or game generation potential

A proposed experiment is an informal play space with one loose object
that several participants can propel. The designer can vary the
available time, reachable surfaces and response opportunities without
scoring each throw or assigning turn ownership. This is a design
hypothesis rather than a claim about despelote's underlying AI.

## New genes

ACT-839 and SYS-1833.

## New combinations

None. No verified combination has every required member in this signature.

## Taxonomy changes

[TAXONOMY_CHANGE_377](../../../research/taxonomy-changes/TAXONOMY_CHANGE_377.md).

## New questions

Does the same commercial PS5 recess advance to the car at the same
story boundary without touching the football?

## Next recommended game

Analyse the first evidenced qualifying tournament finish in the
original European PAL Nintendo 64 Star Wars Episode I: Racer release.

## Why this game

The playing space gives the player a reliable way to intervene
with one physical ball while leaving the response distributed among
the other children. The observed return and subsequent scene cut
keep those two rules separately available for comparison.
