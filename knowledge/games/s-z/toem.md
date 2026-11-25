---
game_id: GAME-0732
slug: toem
game_title: "TOEM"
analysis_status: reviewed
reviewed: 2026-11-25
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-341
    - ACT-502
    - ACT-789
  system:
    - SYS-2039
    - SYS-2040
    - SYS-2041
  constraint: []
  information:
    - INF-661
  objective:
    - OBJ-164
  time:
    - TIM-002
---

# Game: TOEM — Nana’s portrait and the first bus ride

Use the [canonical vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
Nana, the Community Card and the Oaklaville route are instances
of the scoped request, credit and departure rules.

## Analysis scope

- Version / ruleset: English US PlayStation 5 commercial base game,
  Something We Made's 2021 release. W1 displays version 2.0.5.
  The installed package hash and version in W2 are unverified.
- Reproducible entry and exit: start at the Homelanda bus stop after
  the initial camera lesson, with the camera but before obtaining the
  Community Card. Take the first card, complete Nana's outdoor portrait
  request, claim the free ride and travel to Oaklaville. Stop on first
  arrival when movement is available again.
- Primary decision loop: talk to the requester, use the camera to frame
  the subject, decide whether to keep the exposure, choose a saved
  image to show, and claim travel after receiving the stamp.
- Included: walking, the finder and shutter, post-capture save choice,
  album submission to Nana, the card's two counters, the separate bus
  entitlement and the first regional transition. Excluded: the indoor
  tutorial, available photo alternatives, exact subject-recognition math,
  album capacity rules, optional errands, animal records and Basto.
- Direct-play status: no personal PS5 session. The official product
  and developer material establish the edition and stamp-to-pass loop.
  Two recorded PS5 routes establish the local sequence. Only silent
  background frames were inspected.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
| --- | --- | --- | --- | --- | --- |
| TE-001 | The English PS5 base game is a commercial 2021 release. The first recording's title screen reports version 2.0.5. | Observation | Corroborated | High | P1, P2, W1 00:10–00:21 |
| TE-002 | After the camera lesson, the bus attendant issues the Community Card. Its Homelanda side displays no stamps from three available and zero of the one required for a ride. | Observation | Corroborated | High | P2, W1 03:04–03:25, S1 |
| TE-003 | Nana's outdoor request registers a portrait task. The carried camera switches to a first-person finder. Framing her and triggering the shutter yields a candidate exposure with a yes-or-no album prompt. | Observation | Corroborated | High | W1 03:30–03:48, W2 03:13–03:36, S1 |
| TE-004 | The successful route saves the exposure, addresses Nana again and selects her portrait in the album. Her acceptance leads to the card-stamping screen. | Observation | Corroborated | High | W1 03:46–04:07, W2 03:35–03:58, S1 |
| TE-005 | One stamped task changes both denominators' progress, from 0/3 to 1/3 available and from 0/1 to 1/1 required for the bus. The ride is not yet granted at the stamping screen. | Observation | Corroborated | High | P2, W1 03:57–04:07 and 04:17–04:29, S1 |
| TE-006 | On return, the attendant separately grants the free ride at the local threshold. The stamp remains counted. Oaklaville is selectable after the grant, and confirming travel takes the player to the next region. | Observation | Corroborated | High | P2, W1 04:32–05:30, S1 |
| TE-007 | The scoped task and bus exchange use player-paced interactions. Waiting during framing or album selection does not automatically submit or complete the task. | Observation | Corroborated | High | W1 03:30–04:42, W2 03:13–03:58, S1 |

## Basic data

- Release / origin: Something We Made's TOEM, released September 17,
  2021. The analysis target is `PLAT-PLAYSTATION-5`, US store product
  `UP6990-PPSA04354_00-0801952478920400`.
- Mechanical families: `FAM-013` for the stored image and card
  addressed to distinct recipients, and `FAM-017` for the dependency
  from evidence acceptance to route eligibility and departure.
- Primary evidence checked 2026-11-25:
  - **P1:** [TOEM on the US PlayStation Store](https://store.playstation.com/en-us/product/UP6990-PPSA04354_00-0801952478920400).
    Base product, PS5 platform, developer listing and release date.
  - **P2:** [Something We Made's introduction on PlayStation Blog](https://blog.playstation.com/?p=352714).
    The developer describes solving problems with pictures and
    exchanging community stamps at a stop for a free bus pass.
- Recorded and independent evidence:
  - **W1:** [JayWalker Gaming's PS5 opening](https://www.youtube.com/watch?v=inBEfOHJQ1k).
    Shows the version, original one-stamp route and next-area arrival.
  - **W2:** [GamingIsFun's PS5 opening](https://www.youtube.com/watch?v=cgbyg-c2-Gk).
    Repeats the outdoor portrait sequence and its credited stamp.
    The recorder subsequently completes an extra errand before leaving.
  - **S1:** [Rahul Shirke's Homelanda walkthrough](https://intoindiegames.com/walkthroughs/toem-stamps-walkthrough-homelanda/).
    Distinguishes the initial lesson from the request, and explains
    the photo selection and the one-stamp threshold.
- Claim IDs: TE-001–TE-007. Record the album and card after each
  transition. The presence of an earlier unrelated lesson picture
  in the demonstrated album is not a prerequisite for the portrait.

## Mechanical decomposition

### Action Genes

- Reuse `ACT-008`: walk between the bus stop and Nana (TE-002, TE-006).
- Reuse `ACT-341`: address Nana or the attendant to advance the corresponding interaction (TE-002–TE-006).
- Reuse `ACT-502`: expose the current frame with the shutter (TE-003).
- Reuse `ACT-789`: raise and lower the carried camera finder (TE-003, TE-004).

### System Behaviour Genes

- New `SYS-2039`: retain the reviewed exposure in the album on explicit confirmation (TE-003, TE-004).
- New `SYS-2040`: accept one selected stored photograph for the pending request and award its stamp (TE-004, TE-005).
- New `SYS-2041`: separately grant onward travel at the regional stamp threshold without subtracting the stamps (TE-005, TE-006).

### Constraint Genes

No separate constraint is admitted. The subject requirement and
regional threshold belong to their respective settlement rules.

### Information Genes

- New `INF-661`: show one credited stamp count against both available tasks and the lower travel requirement (TE-002, TE-005, TE-006).

### Objective Genes

- Reuse `OBJ-164`: take the authorised bus out of Homelanda and regain control in the next region with the card and equipment (TE-006).

### Time Genes

- Reuse `TIM-002`: pace framing, selection, submission and bus confirmation without a task deadline (TE-007).

## Formal state and transitions

Track region, camera mode, pending exposure, saved album, active
portrait request, completion flag, credited local stamps and ride
entitlement. The shutter replaces the live view with a pending exposure.
Saving inserts that exposure into the album. Showing an eligible
saved image to Nana enables stamp settlement, which closes the
request and increments the card count. The bus attendant checks the
count against the local requirement and grants a separate entitlement.
The next region becomes reachable through a later travel choice.

## Reproducible transitions

| Before | Action or event | Bounded resolution | Claim ID |
| --- | --- | --- | --- |
| Camera acquired, no card | Address the attendant | Receive the Community Card with a one-stamp requirement | TE-002 |
| Nana's request active | Raise the finder, frame Nana and release the shutter | Preview the candidate with the album save choice | TE-003 |
| Preview is pending | Confirm saving | The portrait becomes selectable in the album | TE-003, TE-004 |
| Saved portrait and open request | Speak to Nana and show the portrait from the album, then settle the stamp screen | Complete the request and record one stamp against both card counts | TE-004, TE-005 |
| Card meets the local requirement | Return to the attendant | Receive the free ride with the credited stamp preserved | TE-006 |
| Ride granted | Choose Oaklaville and confirm travel | Arrive in the next region and resume control | TE-006 |

## Strategic and experiential structure

Keep a photograph that visibly answers the request, then show that
specific saved image. The regional card separates the number of
tasks offered from the number needed to leave. One completed
portrait is sufficient for the witnessed departure.

## Replay and variation

The second recording repeats the outdoor portrait sequence and stamp
credit. It then shows an extra stamp from an optional errand. The
first recording establishes that the extra errand is unnecessary
to travel.

## Adjacent systems and history

The camera lesson and optional errands are outside this boundary.
Basto and post-opening tools are excluded along with other
platforms and general-purpose album management.

## Normalised genome

- Action: ACT-008, ACT-341, ACT-502, ACT-789.
- System Behaviour: SYS-2039, SYS-2040, SYS-2041.
- Constraint: none.
- Information: INF-661.
- Objective: OBJ-164.
- Time: TIM-002.

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `731` (`GAME-0001`–`GAME-0731`).
- Exact genome matches: none.
- Tied near matches: `GAME-0683` — Last Window: The Secret of Cape West (`3 / 14 = 0.214286`).
- Supported combination subsets: none.
- Scan date: 2026-11-25.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
| --- | --- | --- | --- |
| [Last Window: The Secret of Cape West (GAME-0683)](../g-l/last-window-the-secret-of-cape-west.md) | ACT-008, ACT-341, TIM-002 | Both walk to a local interaction and resolve it at the player's pace. Last Window decodes written directions and works a physical dial to expose papers on the lobby floor. TOEM creates and submits its own image, then claims a bus ride from a different recipient. | Near, `0.214286`. |

## Taxonomy impact

Separate capture, explicit retention and evidence settlement.
Model route eligibility as the attendant's response to a stamp count
and the paired card counters as information for the departure decision.

## Negative results

- Taking the portrait alone does not close the request.
- Saving the portrait alone does not record a stamp.
- The card records one stamp before there is a next-area travel choice.
- Filling all three spaces on the card is unnecessary for the witnessed ride.

## Delta summary

Record a player-paced image task whose evidence passes through an
album before it changes the regional travel state.

## New facts

- The preview has an explicit choice to keep the exposure.
- The requester evaluates the selected album entry before stamping.
- The card differentiates total opportunities from the bus requirement.

## Principles and design implications

Let a single image serve as transferable evidence. Show the travel
threshold next to the completion total so a player can decide when
to leave. Let granting the ride and choosing to depart remain separate.

## Puzzle or game generation potential

Create a photographable subject, a pending request and a destination
requiring one stamp. Test empty and unsuitable album submissions,
the transition after a qualifying selection and stamp retention
after the separate pass grant.

## New genes

- SYS-2039
- SYS-2040
- SYS-2041
- INF-661

## New combinations

None. No existing verified combination is a proper subset of the signature.

## Taxonomy changes

[Taxonomy Change 478](../../../research/taxonomy-changes/TAXONOMY_CHANGE_478.md).

## Next recommended game

Solomon's Key on the North American NES cartridge is the next Selection 064 unit.

## Why this game

Photography creates a record that can be kept and submitted later.
Its acceptance advances a local count which a different recipient
uses to authorise departure.

## Review status

Reviewed 2026-11-25 for the English PS5 base-game opening from
the first card issuance to arrival in Oaklaville.
