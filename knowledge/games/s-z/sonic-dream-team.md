---
game_id: GAME-0682
slug: sonic-dream-team
game_title: "Sonic Dream Team"
analysis_status: reviewed
reviewed: 2026-11-24
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-904
  system:
    - SYS-036
    - SYS-037
    - SYS-974
    - SYS-1955
    - SYS-1956
  constraint: []
  information:
    - INF-441
  objective:
    - OBJ-360
  time:
    - TIM-003
---

# Game: Sonic Dream Team

This record uses the [canonical vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
The named act, three keys, one mission award and touch layout are scoped parameters.

## Analysis scope

- Version / ruleset: English commercial iOS game distributed by Apple
  Arcade, released December 2023. The fixture is the opening mission of
  Scrambled Shores Act 1, Reach the Dream Portal, after the tutorial.
  The release-window touch capture is labelled iOS; the exact installed
  build and device model are unverified. The launch-day Apple TV record
  corroborates the shared route and does not establish iOS inputs.
- Structured analysis target: PLAT-IOS in
  [platform coverage](../../platforms/games.json).
- Entry: after the tutorial award, select the first Scrambled Shores
  Act 1 mission and start with Sonic under player control. The mission
  selector initially shows a total of one Dream Orb from the tutorial.
- Primary decision loop: steer and jump through the reachable route.
  Use held boost on compatible steep surfaces and ride rails across
  gaps. Follow the local branches for three progress keys.
  Check the three-slot key display before returning to the approach.
  Cross the newly opened barrier and continue to the separate portal.
- Exit: reaching the portal registers Complete, increases the visible
  Dream Orb total from one to two in the iOS recording and makes
  Collect the Dream Orb selectable on the same act. Stop before
  controlling a character in that mission.
- Included: direct steering, air motion and rail contact, the
  boosted traversal instruction, contact pickups, the keyed barrier,
  live mission cue, portal result and return to the act selector.
- Excluded: the tutorial as a scored fixture, the second mission,
  later acts, bosses, time challenges, alternate characters' flight
  and climbing, later content updates, exact acceleration and
  input thresholds, and release coverage beyond the iOS target.
- Potential scoped module: distinguish the continuing route after
  the barrier opens from a different mission on the same geometry.
- Direct-play status: no personal iOS execution or binary inspection.
  Apple and SEGA establish the release and publisher-described movement
  affordances. W1 provides the decisive iOS work, and W2 independently
  corroborates the key gate, onward route and mission handoff. W1's
  tutorial and loading hints are used only to interpret control labels.
  Video frames were inspected in the background with audio excluded.
  The retained result is observed in the selector, with no reload tested.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
| --- | --- | --- | --- | --- | --- |
| SDT-001 | The English iOS title is distributed through Apple Arcade. SEGA dates the Arcade release to December 5, 2023. W1 has the live touch stick and action buttons and labels the game iOS. | Observation | Corroborated | High | P1, P2, W1 11:00–11:40 |
| SDT-002 | The game exposes a held boost input and presents refill pickups and compatible steep surfaces as separate parts of its use. The tutorial tells the player to hold boost on a quarter pipe to get air. The first act shows boosted motion across its steep track; a later loading hint explicitly describes held boost for wall-running. | Observation | Corroborated | High | P1, W1 4:30–5:00, 5:50–6:00, 11:40–12:00 and 16:30, W2 9:40–10:00 |
| SDT-003 | Direct movement and jumping occur on paths and over gaps. The route carries Sonic along fixed rails above the void between surfaces. Ordinary rings and the mission keys enter separate visible tallies after contact. | Observation | Corroborated | High | W1 11:30–12:10 and 13:50–14:20, W2 8:20–9:30 |
| SDT-004 | The first route includes a closed barrier and a cue to collect three keys. Route pickups mark the separate local slots. After all three are recorded, the way through the barrier becomes traversable and the portal objective returns. Acquiring the keys does not end the run. | Observation | Corroborated | High | W1 12:20–12:30 and 13:30–14:40, W2 8:50–9:40 |
| SDT-005 | The player continues beyond the barrier to the separate Dream Portal. The portal yields Complete. The iOS trace shows an Orb total of one on entry and two both in the result and in the returned mission selector. Collect the Dream Orb is now selectable. The displayed optional coin tally is incomplete at completion. | Observation | Corroborated | High | W1 11:00, 14:40, 16:00–16:20, W2 10:20–10:40 |

## Basic data

- Release / origin: SEGA, December 5, 2023, Apple Arcade. This
  fixture is the English iOS touch route.
- Mechanical families: FAM-007 for motion affected by curved support and
  fixed rails, FAM-013 for keys addressing one barrier and FAM-017
  for the ordered key, barrier and portal conditions.
- P1: [App Store product page](https://apps.apple.com/us/app/sonic-dream-team/id1609094795).
  Confirms the iPhone edition, supported English, mission structure and
  wall-running. Current later-content descriptions do not define the fixture.
- P2: [SEGA release announcement](https://www.sega.co.jp/release/231206_1.html).
  Confirms December 5, 2023 and Apple Arcade distribution.
- W1: [TapGameplay iOS launch-window capture](https://www.youtube.com/watch?v=1aVKoeOIW3s&t=660s).
  The 11:00 act selection through 16:20 controls and settlement support
  the iOS packet. The earlier tutorial and subsequent loading hint
  clarify the boost input.
- W2: [Cyberman65 Apple TV launch-day capture](https://www.youtube.com/watch?v=FeYs-zCqTuc&t=485s).
  The description identifies Apple TV and a PS5 controller and
  timestamps Act 1 first and second missions. Used for platform-independent
  route, gate and outcome corroboration.
- Claim IDs: SDT-001–SDT-005.

### Reproducible fixture evidence

1. Open Scrambled Shores Act 1 at about 11:00 in W1.
   Inspect the dimmed successor icons and the Orb total of one.
   Start Reach the Dream Portal with Sonic and wait for control.
2. Run along the ground route into the slopes and rail section at
   about 11:40–12:10. Consult the same recording's earlier boost
   prompts at 4:30–5:00 and 5:50–6:00 to distinguish a held input,
   a refill object and the curved-surface launch. Compare W2's
   steep running route near 9:40–10:00.
3. Read the explicit three-key requirement around 12:20.
   Follow the local branches and collect keys. The fixed rail and
   lateral route around 13:50–14:20 lead back toward the barrier.
   W2 gives a shorter sequence of partially filled, fully filled
   and crossed states near 9:00, 9:30 and 9:40.
4. Compare the W1 frames at about 14:30 and 14:40. Opening
   the barrier permits entry to the next piece of the same route.
   The HUD returns to the portal objective during ongoing control.
5. Reach the distinct portal at about 16:00. Look for Complete
   and the Orb total of two around 16:10. Advance to the selector
   around 16:20 and observe the total of two and a selectable
   Collect the Dream Orb. Stop before launching it.

## Mechanical decomposition

### Action Genes

- ACT-008: steer and jump Sonic directly through compatible local terrain.
  SDT-003.
- ACT-904: use a held boost input during an approach to accelerate
  into a compatible traversal surface. SDT-002.

### System Behaviour Genes

- SYS-036: resolve airborne motion and the next contact after Sonic
  leaves a supported route. SDT-002–SDT-003.
- SYS-037: award a free ring or progress key when the avatar reaches it.
  SDT-003–SDT-004.
- SYS-974: a compatible rail contact constrains the running avatar
  to that fixed path while he moves across open space. Only the rail
  branch is mapped to this gene here. SDT-003.
- SYS-1955: held boost changes access to a compatible steep surface
  and its exit into air or continuation. The supplied boost reserve
  is separate from collectible totals. SDT-002.
- SYS-1956: filling the required local set of key slots removes
  the linked barrier and restores the immediate portal goal. SDT-004.

### Constraint Genes

No separate constraint gene is admitted. The local blocker and its
release are one staged pickup condition under SYS-1956.

### Information Genes

- INF-441: the requirement and separate live key slots expose whether
  the local proof set has been collected for return to the barrier. SDT-004.

### Objective Genes

- OBJ-360: the portal settles the named mission, credits an Orb
  which is still counted in mission selection and exposes the successor
  on the same act. SDT-005.

### Time Genes

- TIM-003: decisions occur while the avatar advances on the slope
  or rail. Approaching its edge or the next gap changes the reachable
  choices. SDT-002–SDT-004.

## Reproducible transitions

| From | Input or event | To | Evidence |
| --- | --- | --- | --- |
| Act 1 selector with one Orb | Start Reach the Dream Portal | Live starting position and separate reset ring tally | SDT-001, SDT-005 |
| Steep eligible route approach | Hold boost while moving | Boosted travel on the slope or exit into airborne motion | SDT-002 |
| Reachable fixed rail | Contact along the route | Constrained traversal above the void | SDT-003 |
| Barrier closed, key display incomplete | Contact an eligible key | One more local slot is credited | SDT-003, SDT-004 |
| Required key set complete | Return on the connected route | Traverse the opened barrier with the portal still ahead | SDT-004 |
| Final route in play | Enter the portal | Complete and one mission Orb credited | SDT-005 |
| Completed mission result | Advance to act selection | Orb total remains two and a different mission is selectable | SDT-005 |

## Strategic and experiential structure

Speed and orientation help reach the key branches, but the barrier
answers a separate progress question. Its slots let the player see
whether another detour is necessary. Opening it resumes the same
motion-and-navigation task on new terrain. The checkpoint that
actually matters to the mission result is at the later portal.

## Replay and variation

W2 follows a shorter route with different optional pickups and a
different input platform. It still exhibits the three-key interlude
and the return to the portal objective. Neither capture establishes
every possible route, the exact tuning of boost or retention after
app termination.

## Adjacent systems and history

Sonic Adventure documents the original Dreamcast homing branch and its
Emerald Coast goal. That scope does not establish the touch input's
optional settings or rules in this commercial Apple Arcade game.
Later Dream Team challenges and additions are distinct subjects.

## Normalised genome

| Type | Stable genes | Role |
| --- | --- | --- |
| Action | ACT-008, ACT-904 | Steer, jump and request held boost |
| System Behaviour | SYS-036, SYS-037, SYS-974, SYS-1955, SYS-1956 | Resolve air motion, pickups, rail attachment, slope boost and barrier release |
| Constraint | None | Gate condition represented by its release rule |
| Information | INF-441 | Expose local key requirement and partial tally |
| Objective | OBJ-360 | Settle and retain the named portal mission award |
| Time | TIM-003 | Accept decisions during real-time traversal |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `681` (`GAME-0001`–`GAME-0681`).
- Exact genome matches: none.
- Tied near matches: `GAME-0391` — Uncharted 2: Among Thieves (`3 / 12 = 0.250000`).
- Supported combination subsets: none.
- Scan date: 2026-11-24.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
| --- | --- | --- | --- |
| [Uncharted 2: Among Thieves (GAME-0391)](uncharted-2-among-thieves.md) | ACT-008, SYS-036, TIM-003 | Both require steering across supports that affect real-time movement. Drake must escape a succession of failing supports to a cliff ledge. Sonic can boost along stable authored slopes, obtains three barrier keys and settles a later portal award. | Near, `0.250000` |

## Taxonomy impact

Four admissions isolate held acceleration input, the added surface
traversal rule, a cumulative local key release and the terminal
grant of a retained mission token. The pickup and displayed tally
reuse earlier definitions.

## Negative results

- Ordinary rings and optional Blue Coins are not the required keys.
- Crossing the barrier is not the terminal victory event.
- The credited Orb count is visible again in act selection. No restart
  or task-wide persistence test was observed.
- The selectable successor is a separate mission in the same act
  and its traversal is outside this fixture.
- The existence of multiple movement types in the store description
  does not admit unused flight or climbing to this signature.

## Delta summary

Ten genes, four new and six reused. The fixture distinguishes
authorised traversal, in-route proof and the terminal result.

## New facts

- The boost input and a compatible ramp jointly determine the
  path away from ordinary support.
- Keys unblock a local passage before the distinct Dream Portal.
- Portal completion shows an added Orb that remains counted when
  the selector exposes the next mission.

## Principles and design implications

Keep path permissions visible in the same view as steering. Show
which intermediate requirements are satisfied before the player
returns to a barrier. Mark the later terminal result separately.

## Puzzle or game generation potential

An original courier route could expose two valid ways to regain a
rail, then require several separate trail markers to open a gate.
Its reward can settle at a later checkpoint and survive the return
to a route selector.

## New genes

- ACT-904
- OBJ-360
- SYS-1955
- SYS-1956

## New combinations

None admitted. All 274 verified combinations were checked as proper subsets.

## Taxonomy changes

[Taxonomy Change 428](../../../research/taxonomy-changes/TAXONOMY_CHANGE_428.md).

## New questions

- Which surfaces permit a boosted path and which require another movement type?
- How long does the opened barrier remain open if the attempt is restarted?
- How do repeated completions settle distinct first-award and optional credits?

## Next recommended game

Continue Selection 058 with `GAME-0683`, the original English European
Nintendo DS release of Last Window: The Secret of Cape West.
Trace one investigation or interaction to a changed local state.

## Why this game

One authored route changes what can be traversed before it changes
the persistent mission result. The player can distinguish those
events from the visible key requirement and the later Orb receipt.
