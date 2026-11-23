---
game_id: GAME-0544
slug: space-channel-5
game_title: Space Channel 5
analysis_status: reviewed
reviewed: 2026-11-19
combination_ids: []
gene_ids:
  action:
    - ACT-533
    - ACT-742
  system:
    - SYS-369
    - SYS-1058
    - SYS-1573
    - SYS-1574
    - SYS-1575
    - SYS-1576
  constraint: []
  information:
    - INF-525
  objective:
    - OBJ-301
  time:
    - TIM-003
---

# Game: Space Channel 5

Use the [canonical vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
Button mapping, report threshold and the authored call rhythm are parameters.
No complete music chart or song lyrics are reproduced.

## Analysis scope

- Version / ruleset: original English North American Dreamcast release,
  2000, default bindings and ordinary first playthrough. This is the
  first game, not Part 2, PS2 Special Edition, GBA or VR.
  Sega of America's May 2000 manual establishes the controls.
  Exact disc revision, binary and input latency were not inspected.
- Entry: select New Game on a profile before its first clear. Begin
  Report 1, Spaceport, at the displayed 15 percent target, with the
  documented initial audience rating of 10 percent.
- Primary decision loop: observe the opponent's ordered movement or
  target demonstration, wait for Ulala's response turn, and reproduce
  the direction and timing. In shooting exchanges choose A for an
  alien and B for a human. Inspect local judgement, hearts, followers
  and audience rating before the next authored exchange.
- Positive exit: finish the complete first report, including Pudding's
  rooftop encounter and Coco Tapioca's dance/shooting phases, with
  at least 15 percent audience rating and no live failure. Stop at
  report settlement and eligibility for the second report.
- Negative exits: zero audience rating, depleted boss dance hearts,
  or ending the report below its target. Continue returns to the
  report beginning, rather than to the failed final phrase.
- Included: alternating call/response, directional dance input, typed
  shooting, contextual target order, local heart allowance, numeric
  audience rating, rescued followers, report endpoint and retry.
- Excluded: later reports, Extra Mode, all-campaign completion, exact
  charts, BPM, scoring weights and hit windows, hidden bonus inputs,
  controller remapping, VMU storage management, character-profile
  collection, save-file persistence, cheats, autonomous demonstration
  play and cross-region or cross-platform timing parity.
- Potential scoped modules: Extra Mode variation, later reversed-input
  boss rules, or the character-profile unlock and persistence layer.
- Direct-play status: no console, disc image, executable, save or
  controller trace was used. The preserved original manual's control,
  action and HUD diagrams were visually inspected alongside Sega's
  original product page and first-hand written accounts. No audio
  or video was played. The transitions are source reconstructions.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
| --- | --- | --- | --- | --- | --- |
| SC-001 | Sega's first Dreamcast game was released in Japan in December 1999 and in English North America in 2000. The selected US booklet predates its retail release. | Observation | Corroborated | High | P1, P2, P3, S2 |
| SC-002 | Dance input repeats four directions and A in the demonstrated order and timing during a later player turn. A is the Morolian beam and B the human-rescue beam in shooting. | Confirmed | Corroborated | High | P1 pp. 6–9, P2, S2 |
| SC-003 | Shooting targets appear in left, upper and right positions. The response depends on appearance order, direction, timing and enemy/human identity; the buttons are not interchangeable. When several targets share a direction, start with the leftmost. | Confirmed | Direct | High | P1 pp. 8–9 |
| SC-004 | Audience percentage is a live performance value. Zero is failure, and the report endpoint separately requires its displayed minimum. Boss dance-heart exhaustion also ends the attempt. | Observation | Corroborated | High | P1 pp. 10–11, S1, S3 |
| SC-005 | Winning dance or rescue exchanges frees people who join Ulala's following group. Poor performance changes the presentation; no permanent rescue guarantee is inferred. | Observation | Corroborated | High | P2, S1, S2 |
| SC-006 | The first report starts at 10 percent, requires 15 percent, reaches the roof encounter with Pudding and ends after Coco Tapioca. Passing does not require every rescue or a perfect report. | Observation | Corroborated | High | S1, S4, P1 minimum/progression |
| SC-007 | Turn ownership, calls, target identity/order, local hearts and audience percentage are disclosed. Start pauses. Continue after failure reconstructs the beginning of the current report. | Confirmed | Direct | High | P1 pp. 8–13 |
| SC-008 | A failed dance phrase removes a local heart. Sources differ on ordinary-dance zero behaviour, but the manual explicitly establishes boss depletion as terminal. Exact allowances and numerical scoring weights remain unmeasured. | Observation | Corroborated | Medium | P1 pp. 10–11, S1, S3 |
| SC-009 | S1 reports renewed hypnosis removing followers and performance-dependent pattern variation. Its pre-US Japanese observations do not establish exact North American branching or persistence. | Observation | Limited | Medium | S1 |

## Basic data

- United Game Artists and Sega. Target: the first game's North American
  English Dreamcast rules. The 1999 Japanese origin is not the selected disc.
- Families: matching and combination, and real-time system pressure.
  Ordered reproduction is judged in scheduled intervals.
- Sources accessed 2026-11-19:
  - **P1** — [Original Sega of America Dreamcast manual](https://www.digitpress.com/library/manuals/dreamcast/space_channel_5.pdf),
    preserved publisher-authored document, production stamp 16 May 2000.
    Printed pp. 6–11 were visually inspected; pp. 12–13 establish retry.
  - **P2** — [Sega's original Space Channel 5 product page](https://ch5.sega.jp/SpaceChannel5/index.html),
    six-button reproduction, timing, freed backup dancers and progress.
    Its Japanese text supplies shared design evidence, not exact US timing.
  - **P3** — [Sega's Dreamcast software history](https://www.sega.jp/history/hard/dreamcast/software.html),
    Japanese original date, 16 December 1999, and product identity.
  - **S1** — [Tom Callahan's first-hand original Dreamcast FAQ](https://www.cheatcodes.com/guide/strategy-guide-space-channel-5-dreamcast-11531/),
    version 2.0, 12 January 2000, preserved mirror of the original guide.
    It explicitly precedes the American release. General structure is
    corroboration; exact regional coefficients and bugs do not transfer.
  - **S2** — [Jeff Gerstmann's original Dreamcast review](https://www.gamespot.com/reviews/space-channel-5-review/1900-2581551/),
    indexed released-English controls and presentation observations.
    The indexed text was readable; the full origin request was restricted.
  - **S3** — [Original Dreamcast play account](https://gigapepsiman.blogspot.com/2010/05/space-channel-5-dreamcast-review.html),
    lost dance allowance, audience response and boss-specific terminal.
  - **S4** — [mewthepokemon's Dreamcast route](https://gamefaqs.gamespot.com/dreamcast/256048-space-channel-5/faqs/9378),
    indexed Report 1 target, Pudding and Coco Tapioca route.
    Its introduction reverses the two beam buttons. P1 and S2 establish
    the correct A-attack/B-rescue mapping used here.
- Claim IDs: SC-001–SC-009.

## Mechanical decomposition

### Action Genes

- Reuse `ACT-533` for delayed rhythmic reproduction after a demonstrated
  phrase. A directional press is not free avatar movement or a dance pad.
- Add `ACT-742` for remembering target order and choosing the compatible
  attack or rescue command during the shooting response.
- Claim IDs: SC-002, SC-003.

### System Behaviour Genes

- Reuse `SYS-1058` for the authored call followed by the response interval.
  It does not require every report to repeat the same chart regardless
  of performance. Exact adaptive branching remains unmeasured.
- Add `SYS-1573` for the joint directional, temporal and typed-beam
  judgement. When several targets share a direction, start
  with the leftmost. A correct rhythm with the wrong beam does not rescue a human.
- Add `SYS-1574` for local phrase-error hearts. Boss zero ends the report;
  no exact heart count or universal ordinary-scene zero rule is asserted.
- Add `SYS-1575` for numeric audience updates, its zero floor and separate
  report minimum. `SYS-1059` instead requires an ordinal rap rating.
- Add `SYS-1576` for successful rescues adding people to the continuing
  entourage. `SYS-906` includes irreversible checkpoint-persistent rescue
  credit, which is not established here.
- Reuse `SYS-369` for the player's accepted retry at the authored report
  entry. No finite paid continue stock or mid-phrase checkpoint is assumed.
- Claim IDs: SC-002–SC-009.

### Constraint Genes

- No independent constraint gene is admitted. Response timing and beam
  compatibility belong to the operations that judge them. Heart and
  rating exhaustion belong to their respective system boundaries.
  The fifteen-percent target is a terminal predicate, not an immediate
  floor that would reject the documented ten-percent entry.
- Claim IDs: SC-003, SC-004, SC-006.

### Information Genes

- Add `INF-525` for audiovisual call/turn and target disclosure together
  with numeric percentage and local heart state. `INF-396` requires
  the ordinal rap grade and a beat-symbol presentation of another ruleset.
- Optional vibration and a VMU turn image do not create another canonical
  rule. No complete scrolling note highway or exact hit window is inferred.
- Claim IDs: SC-002–SC-004, SC-007.

### Objective Genes

- Add `OBJ-301`: finish the entire report through the boss with its
  audience minimum and without live rating/boss-heart failure.
  `OBJ-215` describes a different song result and `OBJ-258` excludes
  live-gauge survival. No perfect rescue requirement is added.
- Claim IDs: SC-004, SC-006, SC-008.

### Time Genes

- Reuse `TIM-003`: authored call and response intervals proceed on
  the musical clock while input is accepted. Waiting indefinitely
  instead of replying misses the scheduled response. Start can pause.
- Claim IDs: SC-002, SC-003, SC-007.

## Reproducible transitions

| Before | Input or event | Bounded resolution | What it establishes | Claim ID |
| --- | --- | --- | --- | --- |
| New Game enters Report 1 | Read the report target and initial rating | Begin at 10 percent with 15 required at settlement | Being below the target at entry is not immediate failure | SC-004, SC-006 |
| The opponent is demonstrating | Observe and retain the ordered directions and intervals | Wait until the interface marks Ulala's turn | Call and response are different scheduled phases | SC-002, SC-007 |
| Ulala's response turn is active | Reproduce the dance directions and A with the demonstrated rhythm | Receive local phrase feedback and an updated performance state | Correct order alone does not guarantee correct timing | SC-002, SC-004 |
| A shooting demonstration has shown people and Morolians | Reproduce directions and timing using B for humans and A for aliens | Resolve the matching rescue or attack; mismatched beam is not a successful rescue | Target identity changes the required command | SC-003 |
| A rescue exchange succeeds | Let the scene settle | The freed people join the following group | The authored rescue has a continuing actor-state consequence | SC-005 |
| Coco Tapioca's dance phase has remaining hearts | Miss one response and inspect the allowance | Lose a heart; exhausted boss allowance terminates the report | A high audience percentage does not bypass boss failure | SC-004, SC-008 |
| The first boss changes to its shooting phase | Follow the displayed target sequence | Settle typed responses and reach the report endpoint | Boss dance and shooting are different local protocols | SC-003, SC-006 |
| All first-report encounters have ended without live failure | Compare settled rating to the displayed target | At least 15 percent permits progression; a lower result fails | Reaching the endpoint alone is insufficient | SC-004, SC-006 |
| A failure has opened Continue | Accept Continue | Rebuild the current report from its beginning | Retry is not a preserved failed phrase | SC-007 |

These reconstruct the documented rules. No native timing trace or newly
executed clear is claimed.

## Strategic and experiential structure

Remembering a direction string is only part of the task. The player
must retain its spacing and notice when the answer interval begins.
Shooting adds a semantic distinction: the same directional target
position can require a different beam when the target is human.

The audience and local hearts are separate failure channels. Surviving
the boss with a positive but insufficient audience does not pass the
report. Conversely a high rating does not refund a failed boss dance.
Choosing when to pause can support study without making the unpaused
response schedule self-paced.

## Replay and variation

A first ordinary report follows the rescue, rooftop and first-boss arc.
Performance can change the surrounding presentation. S1 additionally
reports pattern and follower-loss changes in its Japanese playthrough;
exact US branching and loss/persistence behaviour remain unresolved.
No full fixed chart, exact input buffer, timing correction or numerical
rating update is inferred from the advice. Extra Mode is excluded.

## Adjacent systems and history

PaRappa also demonstrates a phrase before the player answers. Here
numeric audience percentage, local dance hearts and typed shooting
replace the ordinal rap-risk boundary. Simon extends one retained
sequence by one cue and ends at its first mismatch; neither rule is
inherited by this authored report.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
| --- | --- | --- |
| Action | `ACT-533`, `ACT-742` | Dance reproduction and typed shooting response |
| System Behaviour | `SYS-369`, `SYS-1058`, `SYS-1573`, `SYS-1574`, `SYS-1575`, `SYS-1576` | Retry, calls, target judgement, hearts, numeric rating and rescued group |
| Constraint | none | Eligibility and timing remain within operations |
| Information | `INF-525` | Turn, call, target and both live performance displays |
| Objective | `OBJ-301` | Full first-report clear with its audience minimum |
| Time | `TIM-003` | Scheduled musical response intervals |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `543` (`GAME-0001`–`GAME-0543`).
- Exact genome matches: none.
- Tied near matches: `GAME-0396` — PaRappa the Rapper Remastered (`3 / 14 = 0.214286`).
- Supported combination subsets: none.
- Scan date: 2026-11-19.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
| --- | --- | --- | --- |
| `GAME-0396` — PaRappa the Rapper Remastered | `ACT-533`, `SYS-1058`, `TIM-003` | Both demonstrate an ordered phrase before a scheduled player reply. PaRappa uses a live ordinal rap grade and a Good-rated finish. Space Channel 5 adds typed shooting, numeric audience with a separate minimum, local boss hearts and rescued followers. | Near, `0.214286` |

### Preserved research notes

- New genes: `ACT-742`, `SYS-1573`–`SYS-1576`, `INF-525`, `OBJ-301`.
- Classification result: New gene.
- Evidence and reasoning: typed temporal replies, numeric audience
  progression and a separate boss mistake allowance form this packet.

## Taxonomy impact

- Registry changes: seven new Active definitions.
- Taxonomy-change record: [TAXONOMY_CHANGE_291](../../../research/taxonomy-changes/TAXONOMY_CHANGE_291.md).
- Candidate terms affected: none.

## Negative results

- none.

## Delta summary

## New facts

- [Observation | Corroborated | High] The first report distinguishes
  a live zero floor from its separately settled fifteen-percent target.

## New genes

- [Observation | Corroborated | High] Seven additions separate typed
  replies, hearts, audience, rescue actors, display and report clear.

## New combinations

- [Observation | Corroborated | High] No new combinations.

## Taxonomy changes

- [Observation | Corroborated | High] `TAXONOMY_CHANGE_291`.

## New questions

- What exact pattern and follower-loss branches differ across original regions?
- What are the executable's precise timing windows and audience weights?

## Next recommended game

- [Hypothesis | Limited | Medium] Full PS5 Dispatch in
  [Selection 043](../../../research/selection/SEARCH_DEMAND_GAME_SELECTION_043.md).
- Optimisation criterion: change from performed rhythm to dispatch allocation.
- Expected information gain: a bounded shift with hero-task compatibility.
- Backlog impact: advance to `GAME-0545`.

## Why this game

- [Hypothesis | Limited | Medium] A dispatch shift should expose scheduling
  choices distinct from replaying an observed timed phrase.
