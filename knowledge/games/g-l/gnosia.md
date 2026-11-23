---
game_id: GAME-0630
slug: gnosia
game_title: "Gnosia"
analysis_status: reviewed
reviewed: 2026-11-22
combination_ids: []
gene_ids:
  action:
    - ACT-837
    - ACT-838
  system:
    - SYS-1832
  constraint: []
  information:
    - INF-268
    - INF-585
  objective:
    - OBJ-339
  time:
    - TIM-045
---

# Game: Gnosia

This analysis uses the [canonical vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary).

## Analysis scope

- Version / ruleset: Japanese PlayStation Vita commercial download,
  June 20, 2019, PCSG-01277, original Mebius release. Use a fresh
  single-player profile and its first tutorial loop. The record uses
  two launch-period Japanese Vita captures. Their patch numbers
  and hardware configuration are unverified.
- Primary decision loop: read the assigned crew role and active roster,
  respond to suspicions or wait as the discussion advances, commit a
  ballot for an eligible participant, and check who enters cold
  sleep and what the game actually records as the loop result.
- Entry: the first Day 1 meeting after the tutorial assigns the player
  to ordinary crew. The original roster is the player, Setsu, Gina,
  SQ and Raqio. The report later identifies one Gnosia.
- Exit: after SQ enters cold sleep on Day 2, the actual result shows
  victory for the crew, names every original role, and credits
  experience. Continuing leads to the next Day 1 introduction.
- Included: the guided first ballot and Raqio's cold sleep, Gina's
  disappearance at the inter-day transfer, the three remaining
  participants, the five-round Day 2 discussion, one candidate
  per ballot, the displayed vote tally, SQ's removal and the report.
- Excluded: alternate end branches, tie resolution, later loop setup,
  role skills, player removal in later loops, character stat effects,
  chance or AI weights, later-platform interface features and the
  anime adaptation.
- Suggested later scope: independently inspect a different Day 2 vote
  using the same Vita release and verify its alternative result.

## Direct-play status

No direct play was performed. Two recordings made during the Japanese
Vita launch period identify the target platform. Static samples from
both show the opening crew, discussion, cold-sleep sequence and an actual
victory report. The first uses an original player name and the second uses
a different one. The PlayStation release listing, the publisher's release
notice and a contemporaneous firsthand review establish release identity
and rule context. Audio, a native input trace, the exact patch and
unobserved branches were not verified.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
| --- | --- | --- | --- | --- | --- |
| GN-001 | Mebius released the Japanese Vita download on June 20, 2019. The contemporary product identifier is PCSG-01277. | Confirmed | Corroborated | High | P1, P2, R1. W1 and W2 identify the platform and were published before the later ports. |
| GN-002 | The opening meeting presents five participants, including the ordinary-crew player. On Day 1 Raqio is sent to cold sleep. On Day 2 LeVi reports Gina absent after spatial transfer, leaving the player, Setsu and SQ participating. | Observation | Corroborated | High | W1 7:45–8:30 and 13:15–14:50. W2 1:44–2:14 corroborates the first ballot and cold-sleep sequence. |
| GN-003 | The tutorial explains the next legal step. During Day 2, accept a contextual reply such as agreeing with suspicion or defending the addressed person, or proceed without speaking. The floor progresses through five visibly indexed rounds before voting. | Observation | Corroborated | High | W1 15:35–19:17, including 16:01 and 18:54. W2 5:00–7:10. R2. |
| GN-004 | At the second ballot the player settles on SQ. The voting screen first requests a choice, then exposes the votes and labels SQ for cold sleep. The active votes are two for SQ and one for Setsu. | Observation | Corroborated | High | W1 19:17–19:30 and W2 7:09–7:27. Departed participants remain listed without contributing a Day 2 vote. |
| GN-005 | Selection for cold sleep is separate from underlying allegiance. Raqio is removed on Day 1 but disclosed as crew at the end. The Day 2 verdict is followed by specific confirmation of SQ in cold sleep. | Observation | Corroborated | High | P2, R2, W1 8:27–8:31, 19:28–19:58 and 22:16–22:40. W2 7:27 reports the same Day 2 removal. |
| GN-006 | The result displays Day 2 victory, SQ as sole Gnosia, the other four as crew and 385 experience on the worked W1 route. The record can advance to the next Day 1. No multiplication of results, stats or votes is inferred. | Observation | Corroborated | High | W1 22:07–24:00. W2 shows the corresponding terminal reveal at 8:53–9:01. |

## Basic data

- Analysis target: `PLAT-PLAYSTATION-VITA`.
- Developer: Petit Depotto. Publisher: Mebius.
- Mechanical family: `FAM-002`, hidden-state inference.
- Checked: 2026-11-22.
- P1: [Japanese PlayStation.Blog release listing](https://blog.ja.playstation.com/2019/06/21/20190621-new-soft/).
- P2: [Mebius's June 20 release notice reproduced by 4Gamer](https://m2.4gamer.net/games/434/G043428/20190620046/),
  including the digital release, changing roles and discussion leading
  to cold sleep. The notice states that a loop result does not end the game.
- R1: [Vita product and release identifier](https://gamefaqs.gamespot.com/vita/209659-gnosia/data).
- R2: [Famitsu's July 2019 first-hand Vita account](https://www.famitsu.com/news/201907/06179080.html),
  including the vote and the distinction between roles and what a player
  can observe during debate.
- W1: [Hiken's June 21 PS Vita opening](https://www.youtube.com/watch?v=6PUJWnfmV5Y&t=465s),
  continued through Day 2 result and the next Day 1.
- W2: [TVR's July 8 Japanese PS Vita recording](https://www.youtube.com/watch?v=mkzytYeQsZE&t=300s),
  independently showing the successful Day 2 route.

## Mechanical decomposition

### Action Genes

- ACT-837: commit an available targeted stance in discussion or let
  the current opportunity pass silently.
- ACT-838: cast one structured ballot for the intended cold-sleep
  candidate before the panel publishes the collective result.

### System Behaviour Genes

- SYS-1832: tally current ballots and remove the largest unique
  vote recipient from participation by placing them in cold sleep.
  The tally does not test whether that person actually opposes the crew.

### Constraint Genes

Candidate eligibility belongs to the ballot. The target's true role
belongs to the result and is not an eligibility condition for sleep.

### Information Genes

- INF-268: tutorial prompts explain currently available commands
  and the next phase as it becomes relevant.
- INF-585: expose own role, roster and availability during the loop
  while withholding others' true roles until result. Statements and
  figures in the voting ledger are different from the final role map.

### Objective Genes

- OBJ-339: on the crew side, resolve the loop by getting its last
  hidden Gnosia into cold sleep and accepting the recorded victory.

### Time Genes

- TIM-045: run a bounded multi-round discussion phase, followed by
  a separate ballot and removal phase. Several responses can occur
  within a visible round. No elapsed real-time deadline is asserted.

## Reproducible transitions

| State | Input or event | Result | Evidence |
| --- | --- | --- | --- |
| Day 1 has the crew player and four named counterparts | Complete the guided first ballot | Raqio receives four votes and is selected for cold sleep in W1 | GN-002, GN-005 |
| Four active participants remain before transfer | Pass through the authored spatial transfer | LeVi reports Gina missing. Three participants remain for Day 2 | GN-002 |
| Day 2 debate is active and the true assignment is withheld | Select an available stance or advance without speaking | Participants respond and the counter reaches round five | GN-003 |
| The final discussion round ends | Choose SQ and confirm one ballot | The panel gives SQ two votes, Setsu one, and marks SQ for cold sleep | GN-004 |
| SQ is the largest unique vote recipient | Advance through the cold-sleep outcome | Setsu reports SQ in cold sleep and the loop stops with the crew victory | GN-005, GN-006 |
| The victory is settled | Inspect the result and continue | The actual role map identifies SQ as the sole Gnosia. The W1 player receives 385 experience and moves on to the next Day 1 | GN-006 |

## Strategic and experiential structure

Voting and dialogue provide different kinds of information. A statement
for or against a suspect is visible input, and the displayed vote result
shows collective behaviour. It does not prove which side the selected
person was really on. The first and second cold-sleep verdicts illustrate
that independence. The result maps the actual roles after the loop's
terminal condition, allowing the player to compare them with prior claims.

## Replay and variation

Two 2019 recordings agree on the normal opening victory path. Only
their observed choices and results are admitted. The packet does not
establish that a different first ballot always has the same effect,
how ties settle in other loops or that voting SQ is safe in later
assignments. Sony and Mebius describe changing roles between loops.

## Adjacent systems and history

The publisher describes experience rewards and later access to abilities
and scenario setup. Only the experience receipt is within this packet.
The sequel-like progression into a later introduction does not establish
that all temporary evidence or dialogue persists unchanged.

## Normalised genome

| Type | Stable genes | Role |
| --- | --- | --- |
| Action | ACT-837, ACT-838 | Choose a debate stance or pass, then commit one ballot |
| System Behaviour | SYS-1832 | Tally votes and remove the highest unique recipient |
| Constraint | None | Candidate eligibility is owned by the ballot |
| Information | INF-268, INF-585 | Read the current instructions and the difference between available public information and revealed roles |
| Objective | OBJ-339 | Settle the crew victory by putting the sole hidden opposing participant in cold sleep |
| Time | TIM-045 | Advance bounded rounds before a separate ballot and removal phase |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `629` (`GAME-0001`–`GAME-0629`).
- Exact genome matches: none.
- Tied near matches: `GAME-0434` — Cooking Mama (`1 / 13 = 0.076923`); `GAME-0628` — Keep Driving (`1 / 13 = 0.076923`).
- Supported combination subsets: none.
- Scan date: 2026-11-22.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
| --- | --- | --- | --- |
| [Cooking Mama (GAME-0434)](../a-f/cooking-mama.md) | INF-268 | Both expose an authored prompt for the current step. Cooking Mama prompts a stylus cooking operation and scores the completed dish. Gnosia prompts a discussion stance and settles separate ballots that change the participating roster. | Near, `0.076923` |
| [Keep Driving (GAME-0628)](keep-driving.md) | INF-268 | Both expose a prompt for the current decision. Keep Driving asks the player to align skill symbols with resource threats in a road event. Gnosia presents choices about named participants whose true roles are disclosed in the loop result. | Near, `0.076923` |

## Taxonomy impact

[TAXONOMY_CHANGE_376](../../../research/taxonomy-changes/TAXONOMY_CHANGE_376.md)
records the independent dialogue, vote, tally, information and phase boundaries.

## Negative results

- ACT-323 is a map-preference ballot. In this packet voting addresses
  one present person for loss of participation, with no random map option.
- SYS-560 can make a weighted arena choice. The observed unique highest
  tally chooses a participant directly. No tie rule or weighting is inferred.
- INF-013 is a roster identity-mapping structure. This packet shows who
  is present but conceals the true allegiances until settlement.
- The guided first run does not support arbitrary defence or accusation
  weights, physical action timing or a repeated reset on a real-time clock.

## Delta summary

Adds a full Japanese Vita introductory loop through two distinct cold
sleep outcomes, the actual crew victory report and next-day entry.

## New facts

- The tutorial begins with ordinary crew and a five-participant roster.
- A collective ballot can remove a crew member or a hidden opponent.
- The final report exposes the actual assignment behind the visible debate.

## New genes

ACT-837, ACT-838, SYS-1832, INF-585, OBJ-339 and TIM-045.

## New combinations

None. No verified combination has every required member in this signature.

## Taxonomy changes

[TAXONOMY_CHANGE_376](../../../research/taxonomy-changes/TAXONOMY_CHANGE_376.md).

## New questions

Which alternative Day 2 ballot outcomes can be independently reproduced
on the same commercial Vita version?

## Next recommended game

Close Selection 052 at this accepted unit and proceed to the first
selected release in the next mixed-platform horizon.

## Why this game

The actual report permits comparing a useful and a mistaken removal
within the same introductory session. The two decision surfaces,
discussion and ballot, remain distinct even when the vote follows the
player's suspicion.
