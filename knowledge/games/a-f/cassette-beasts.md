---
game_id: GAME-0601
slug: cassette-beasts
game_title: "Cassette Beasts"
analysis_status: reviewed
reviewed: 2026-11-21
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-019
    - ACT-801
    - ACT-802
  system:
    - SYS-398
    - SYS-608
    - SYS-1523
    - SYS-1769
    - SYS-1770
    - SYS-1771
  constraint:
    - CON-756
    - CON-846
  information:
    - INF-563
    - INF-564
  objective:
    - OBJ-029
  time:
    - TIM-033
---

# Game: Cassette Beasts

Comparison uses the [canonical vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
Tape names, companion, target species and observed level are instance
parameters of the first recording lesson.

## Analysis scope

- Version / ruleset: the full English Android base game as distributed
  by Raw Fury through Google Play, package `com.RawFury.CassetteBeasts`,
  commercial release in 2025. The store distinguishes its free opening
  from the full game unlocked by a one-time purchase. Raw Fury announced
  15 January for mobile. Contemporary reporting describes a temporary
  Android withdrawal, so the announced date is not treated as evidence
  of uninterrupted Android availability or a verified day of restoration.
- Structured analysis target: PLAT-ANDROID in
  `knowledge/platforms/games.json`. W1 identifies a native Android 15
  device and shows the scoped sequence. The installed build number and
  purchase status of captures are not authenticated. The scope is part
  of the full Android campaign and also lies within its shared opening.
- Primary decision loop: choose one command for each eligible party
  member, commit a blank tape against the wild Dominoth, and manage the
  partner and the exposed human recorder while the recording resolves.
  Play the acquired copy as a combat form. Continue directing both
  combatants until the wild original is defeated and the field ability
  is awarded.
- Entry and exit: in a fresh standard adventure, follow Kayleigh through
  Harbourtown Outskirts to the forced first Dominoth recording lesson
  of This Is The World We Live In. Start at the approach to the ready
  lesson after the preceding introduction, with Kayleigh and Basic
  Tapes available. Stop after the battle result and Mothwing Glide
  grant on return to the field, before further traversals or fights.
- Included: short field approach, eligible target and tape choice,
  paired turn commands, vulnerable human recording, evolving displayed
  probability, retained duplicate, in-battle playback, move cost and
  retained action points, victory and the authored glide award.
- Excluded: starter choice, preceding beach battle, optional fights,
  camp healing, editing stickers, using the awarded glide through later
  terrain, Morgante and fusion, purchases as actions, later story,
  online play, other editions, exact probability coefficients and
  exhaustive health, speed and failure-edge tests.
- Potential scoped modules: the first actual glide crossing, fusion
  in the first Archangel fight, and one unscripted recording with a
  genuinely failed attempt and retry.
- Direct-play status: no direct play. Raw Fury and the Google Play page
  establish the Android product. Developer notes describe recording
  and move costs. Still frames from an Android-labelled device run
  and two mobile-labelled captures trace recording, playback, victory
  and the grant. General mechanics pages supplement edge rules.
  No purchase state, precise build, loss recovery or probability
  edge was experimentally reproduced. No video or audio playback.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
| --- | --- | --- | --- | --- | --- |
| CB-001 | Google Play distributes the Android package with a one-time unlock of the full game. The announced 15 January launch and temporary withdrawal are distinct. | Confirmed | Corroborated | High | P1, P2, H1, W1. |
| CB-002 | Each eligible ally supplies a regular command for the round. Forms have their own sticker moves, health state and priced move options. | Observation | Corroborated | High | P3, P4, R3, W1 18:20–18:30 and 19:30–20:30, W2 15:00–15:30. |
| CB-003 | A Basic Tape and the eligible wild target are chosen for Record. The recorder returns to human form while the partner's separate action remains possible. | Confirmed | Corroborated | High | P3, W1 18:20–18:50, W2 13:10–13:40, W3 17:30–18:10. |
| CB-004 | Recording shows a linked target and live success estimate; lower starting health and damage to the target help, while damage to the recorder reduces the chance. The rules document survival of the target until the check. | Observation | Corroborated | Medium | P3, R1, W1 18:40 and 19:10–19:20. Exact floor and ordering were not forced. |
| CB-005 | Success produces a retained form tape and new species entry without removing the living opponent; the opponent is still active after success. | Confirmed | Corroborated | High | P3, W1 18:50–20:20, W2 13:40–15:10. |
| CB-006 | The acquisition is followed by a separate playback order using the new Dominoth form. The original remains available for the ensuing battle. | Observation | Corroborated | High | P1, P3, W1 19:30–20:30, W2 14:00–15:30. |
| CB-007 | The battle resolves committed allies and hostiles in an interleaved order. Move points accrue per participant between rounds and can be retained or spent by move price. | Observation | Corroborated | High | P4, R3, W1 11:40, 20:20–20:30, W2 15:10–15:30. |
| CB-008 | The defeated opponent leads to a battle result and return to the field, then the same tutorial grants Mothwing Glide to the human player. | Observation | Corroborated | High | R2, W1 20:30–21:00, W2 15:30–16:10, W3 19:00–19:20. |
| CB-009 | The recording floor is a documented boundary; neither a failed tutorial attempt, exact rollback nor a route unlocking glide without the normal lesson was reproduced. | Observation | Limited | Medium | R1, R2, sampled frames and lack of controlled Android inputs. |

## Basic data

- Release / origin: Bytten Studio, published by Raw Fury. The original
  PC release was 2023. The commercial Android release belongs to 2025.
- Platform or physical form: single-player native Android, English
  prompts and touch interface.
- Puzzle family: ordered dependency sequencing (FAM-017). A compatible
  blank medium and an eligible target precede a pending recording, the
  completed record precedes playback, and the lesson has its own
  postbattle ability settlement.
- P1: [Raw Fury's Google Play product listing](https://play.google.com/store/apps/details?hl=en-US&id=com.RawFury.CassetteBeasts),
  official package, unlock and recording-to-transformation model.
- P2: [Raw Fury's January mobile launch announcement](https://www.youtube.com/watch?v=cq2Y3JukO1I),
  dated publisher description; the announcement video was not played.
- P3: [Bytten Studio's Roll the Tape](https://steamcommunity.com/games/1321440/announcements/detail/3385038258983375397),
  first-party description of selecting Record, the blank medium,
  human recording, probability inputs and the new tape.
- P4: [Bytten Studio's Show Your Moves](https://steamcommunity.com/games/1321440/announcements/detail/5240523943475488670),
  first-party explanation of form-specific stickers and move points.
  P3 and P4 describe the original game design; mobile prompts and
  frames are the evidence of the implemented opening.
- H1: [Contemporary Android withdrawal report](https://www.pocketgamer.com/cassette-beasts/out-now-on-ios-delayed-on-android/),
  reports that the release was temporarily withdrawn while a patch
  was pending. It does not date a verified restoration.
- R1: [Recording reference](https://wiki.cassettebeasts.com/wiki/Recording),
  community documentation linked by the developer, supplies the
  active-attempt survival rule and check timing. The exact formula is
  outside this record.
- R2: [Opening quest route](https://wiki.cassettebeasts.com/wiki/This_Is_The_World_We_Live_In)
  and [ability reference](https://wiki.cassettebeasts.com/wiki/Mothwing_Glide),
  connect the forced Dominoth lesson to the specific glide grant.
- R3: [Move order](https://wiki.cassettebeasts.com/wiki/Priority),
  [action points](https://wiki.cassettebeasts.com/wiki/AP) and
  [stats](https://wiki.cassettebeasts.com/wiki/Stat), shared
  community references for priority, speed and personal resources.
- W1: [V-Alpha native Android-attributed route](https://www.youtube.com/watch?v=NjxwTaMGRlM),
  published July 2025 and attributed to a Galaxy S24 Ultra with
  Android 15. Selected rendered frames were inspected.
- W2: [ANDROOSGAMEPLAY mobile-labelled route](https://www.youtube.com/watch?v=XRxGOts61As),
  in English with touch controls. Its label includes Android and iOS
  and does not identify a particular installed build.
- W3: [Gaming Mobile mobile-labelled route](https://www.youtube.com/watch?v=fkL0A2RdnBg),
  daytime corroboration of the teaching encounter and return to field.
  The label includes both mobile platforms.
- Claim IDs: CB-001–CB-009.

### Reproducible route evidence

1. Enter the standard opening lesson in Harbourtown Outskirts with
   Kayleigh present and Basic Tapes in inventory. The start is the
   approach after the preparatory opening sequence, not New Game
   or an arbitrary later Dominoth encounter. Walk along the ledge
   trail into the authored trigger. W1 17:50–18:20 shows the declared
   encounter. W2 12:30–13:00 shows the field approach and introduction.
2. Use Record on the battle surface, pick the Basic Tape and select
   the wild Dominoth. W3 17:30 shows the Basic Tape choice; W1 18:30
   shows the target line and W1 18:40 the pending recording. Assign
   the other eligible party member's command before the mixed round
   settles. The human recorder and transformed companion coexist
   on the party side across the sampled states.
3. Read the link and percentage beside the wild Dominoth. The
   recording lesson at W1 19:10–19:20 explains that target health
   and the tape set up the chance, and relative damage can change
   it before the result. The same round gives the opponent time to
   harm the exposed recorder. Use the partner to damage the target
   or protect the recorder within available commands. No precise
   percentage is required to reproduce the tutorial. R1 documents
   keeping the target alive during the check; an overkill was not
   deliberately induced in W1.
4. Check the acquired tape and species entry. W1 18:50–19:00 and
   W2 13:40–13:50 show the acquisition and resulting identification.
   The opponent is not removed. Follow the separate transformation
   instruction, select the new Dominoth tape and re-enter the
   round in the recorded form. At W1 20:10–20:30 both the player's
   recorded form and the wild target are in the same battle. W2 15:10
   likewise shows the two opposed bodies. Sticker moves come from
   the worn form and are distinct from the recording command.
5. Continue ordinary rounds, spending only available individual
   action points on one move or other legal command per member.
   Cheap actions can leave points for a pricier move. W1 20:30
   shows a move in the closing exchange; 20:40 shows battle
   results and an awarded Zephyr sticker. W2 15:30–15:50 samples
   the last commands, settlement and return to field. The award
   table and exact finishing move are evidence of the route, not
   fixed requirements for every replay.
6. Accept the result, let the field lesson resolve and stop once
   Mothwing Glide becomes available. W1 20:50–21:00 displays the
   dialogue and wing presentation. W2 16:00 shows the named glide
   panel and W3 19:20 the postbattle field award. The new battle
   tape was already played before the separately awarded movement
   ability. The ability does not require retaining Dominoth as the
   active battle form in the world.

Claim IDs: CB-001–CB-009. Timestamps are sampled frames and do not
specify required timings.

## Mechanical decomposition

### Action Genes

- ACT-008: steer the human avatar along the outskirts approach to
  the authored recording lesson.
- ACT-019: select one affordable move for an eligible combatant
  and direct it at an available target.
- ACT-801: choose the Record command, compatible blank tape and
  wild target, suspending that actor's transformed body to record.
- ACT-802: commit playback of the newly owned form tape. The
  same player character acts as the new form on subsequent orders.
- Claim IDs: CB-002, CB-003, CB-006–CB-008.

### System Behaviour Genes

- SYS-398: the authored settlement retains Mothwing Glide as a
  human field action after the lesson.
- SYS-608: a played tape gives the persisting character a different
  body with that form's health and sticker moves. Recording returns
  the actor to human form; playback changes that state again.
- SYS-1523: ordinary allied and hostile moves execute in a mixed
  order governed by move priority and speed rather than by arbitrary
  party-list position. No exact tie-break is asserted.
- SYS-1769: the recording has a pending turn state. Damage to the
  target and to the recorder influence the later success check in
  opposite directions.
- SYS-1770: the move-point balance is personal. The round adds points;
  ordinary spending debits move cost and unused points carry forward
  up to the active capacity. The basic increment is two.
- SYS-1771: a successful copy becomes retained and playable
  alongside an independent wild original. A new species is added
  to the bestiary rather than the wild body becoming inventory.
- Claim IDs: CB-002–CB-009.

### Constraint Genes

- CON-756: the standard round schedules one command for each eligible
  member. A recording or direct playback uses that member's command.
- CON-846: the current recording target remains alive until the active
  check resolves even if it takes otherwise decisive damage. This is
  a documented edge rule, not a measured native damage floor.
- Claim IDs: CB-002–CB-004, CB-007, CB-009.

### Information Genes

- INF-563: a link and visible success estimate identify the current
  recorder and target, followed by tape-acquisition evidence.
- INF-564: read separate current health and points, then inspect a
  sticker for its cost and effect before choosing the move.
- Claim IDs: CB-002–CB-007.

### Objective Genes

- OBJ-029: settle the lesson's one finite battle by defeating the
  still-hostile target. The first success notification alone does not
  settle the battle.
- Claim IDs: CB-005, CB-006, CB-008.

### Time Genes

- TIM-033: plan commands for both eligible party members before
  interleaved resolution and return to the next planning stage if
  the opponent is still standing.
- Claim IDs: CB-002, CB-003, CB-007.

## Reproducible transitions

| Before | Action | Resolution | What it establishes | Claim ID |
| --- | --- | --- | --- | --- |
| Basic Tapes available on the authored trail | Approach the tutorial trigger | Kayleigh presents the wild Dominoth lesson | The battle has a specific route entry | CB-002, CB-008 |
| Eligible transformed allies and live wild target | Commit Record with tape and target | The recorder becomes human and the link becomes visible | A selected tape schedules copying and exposure | CB-003, CB-004 |
| Recording pending | Deal damage to target or take damage as recorder | Documented chance changes in opposite directions; the target can remain active to the check | Recording is resolved after intervening actions | CB-004, CB-009 |
| Successful check | Acknowledge the result | Receive a playable Dominoth tape; the original remains on the hostile side | Copy and original have separate identities | CB-005 |
| A newly owned form and surviving wild opponent | Commit the Dominoth tape for playback | The same person assumes recorded form in the battle | Ownership and playback are separate transitions | CB-006 |
| The target survives an ordinary command batch | Use affordable moves in later rounds | Interleaved commands settle and residual points can support a later move | The other actor and action-point balance remain relevant | CB-007 |
| The wild Dominoth still opposes the party | Defeat it and accept the battle settlement | Field control returns and the tutorial grants Mothwing Glide | The postbattle award is distinct from first tape acquisition | CB-008 |

## Strategic and experiential structure

Recording spends an action and a blank resource, and changes the
recorder's exposure within the round. Damage that would normally
work toward immediate victory also has a separate benefit while
the recording is pending. The second party member preserves a
command when the recorder cannot use its old form's moves. The
authored tutorial then makes the owned copy usable before the
original has been defeated. Claim IDs: CB-002–CB-009.

## Replay and variation

The mobile captures encounter the same lesson at different times
of day and with different preceding encounters and field lines.
The screenshots show costs and results, but do not isolate precise
AP caps or recording launch and return probabilities across Android
patches. An unsuccessful recording, nonstandard progression bypass,
later bootlegs and the precise law for subsequent glide crossings
remain separate investigations. Claim IDs: CB-001, CB-004, CB-007–CB-009.

## Adjacent systems and history

The publisher describes fusion as an additional system. It does
not explain the fact that two visually similar Dominoths can be on
opposite sides after a form has been copied and played. The normal
lesson's movement award is authored and is not evidence that recording
any roamable member of a species always grants an ability. Claim IDs:
CB-005, CB-006, CB-008, CB-009.

## Normalised genome

| Type | Stable genes | Role |
| --- | --- | --- |
| Action | ACT-008, ACT-019, ACT-801, ACT-802 | Approach, issue combat command, record, play back |
| System Behaviour | SYS-398, SYS-608, SYS-1523, SYS-1769, SYS-1770, SYS-1771 | Field grant, body change, round order, evolving chance, personal move points, retained copy |
| Constraint | CON-756, CON-846 | Member command allotment and active target protection |
| Information | INF-563, INF-564 | Pending recording and visible combat resources |
| Objective | OBJ-029 | Defeat the wild original and reach the battle result |
| Time | TIM-033 | Complete party planning before interleaved settlement |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `600` (`GAME-0001`–`GAME-0600`).
- Exact genome matches: none.
- Tied near matches: `GAME-0530` — Lost Odyssey (`5 / 33 = 0.151515`).
- Supported combination subsets: none.
- Scan date: 2026-11-21.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
| --- | --- | --- | --- |
| [Lost Odyssey](../g-l/lost-odyssey.md) (`GAME-0530`) | `ACT-019`, `CON-756`, `OBJ-029`, `SYS-1523`, `TIM-033` | Both assign a party command per member before a mixed priority and speed round, then win the bounded encounter by defeating the hostile set. Lost Odyssey’s scoped Grilgan battle uses its Ring timing, protection and spell timing. Cassette Beasts exposes the recording person during the round, preserves the wild original, and admits the new tape as a playable form before victory. | 5 shared of 33, Jaccard 0.151515 |

### Preserved research notes

- Classification result: New gene.

## Taxonomy impact

- [TAXONOMY_CHANGE_347](../../../research/taxonomy-changes/TAXONOMY_CHANGE_347.md)
  records eight active boundaries and preserves capture-specific genes.

## Negative results

- ACT-194, SYS-307 and OBJ-252 require capture semantics. The wild
  body is not removed into storage by a successful copy.
- SYS-357 grants points from attacks, active defence or passives
  within a turn. The observed move economy has a regular round
  grant and carryover.
- INF-363 prescribes move-specific PP. The menu here exposes a
  pooled balance per fighter and per-move cost instead.
- No applied or inferred fusion gene follows from the visual
  presence of two opposed instances of the same species.

## Delta summary

## New facts

- [Confirmed | Corroborated | High] A wild form can be recorded and
  played inside the same normal tutorial encounter without taking
  the original creature out of that encounter. CB-003–CB-006.
- [Observation | Corroborated | High] The verified battle result
  precedes the authored human movement ability grant. CB-008.
- [Observation | Corroborated | Medium] The current recording adds
  risk and a changing chance over the round, with a documented
  floor protection during the active window. CB-004, CB-009.

## New genes

- [Observation | Corroborated | Medium] ACT-801, ACT-802,
  SYS-1769, SYS-1770, SYS-1771, CON-846, INF-563 and INF-564.

## New combinations

- [Observation | Direct | High] No new combinations.

## Taxonomy changes

- [Observation | Corroborated | High] TAXONOMY_CHANGE_347.

## New questions

- How does a failed ordinary recording in the same Android build
  treat the expended tape, turn and eligible retry?
- Does the tutorial guarantee any step without displaying
  a guaranteed chance, and which exceptional loss states alter it?
- Which glide edges become traversable in the first independent use?

## Next recommended game

- [Hypothesis | Limited | Medium] Pilotwings 64 on North American
  Nintendo 64 under Selection 049. Reconstruct an opening scored
  flight test and its landing settlement.

## Why this game

- [Hypothesis | Limited | Medium] The first recording lesson
  makes the copy, the still-active opponent and the postbattle
  movement award independently visible in a short complete loop.
