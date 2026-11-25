---
game_id: GAME-0684
slug: reanimal
game_title: "REANIMAL"
analysis_status: reviewed
reviewed: 2026-11-24
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-341
    - ACT-726
  system:
    - SYS-407
    - SYS-1958
    - SYS-1959
  constraint: []
  information:
    - INF-630
  objective:
    - OBJ-362
  time:
    - TIM-002
---

# Game: REANIMAL

This record uses the [canonical vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
The mill, tube, lever, hinged bridge and locker room identify the fixture.

## Analysis scope

- Version / ruleset: English Windows commercial Steam base game
  (app 2129530), launch-window solo campaign, Chapter 1, Dead in
  the Water. THQ Nordic dates release to February 13, 2026.
  W1 identifies Steam PC and W2 labels its run PC and solo.
  The exact build, OS patch and W1 input hardware are unverified.
- Structured analysis target: PLAT-WINDOWS-PC in
  [platform coverage](../../platforms/games.json).
- Entry: the earlier power switch has started the large mill tube.
  The siblings have climbed to its local control platform and the
  boy is free to move next to the stop lever. Stop before requesting
  support to reproduce this starting state.
- Primary decision loop: inspect the rotating tube and the nearby
  stop lever. At the lever, call the sister to take over the hold.
  Once it stops, land on a supported part of the tube, move along
  it and climb the far ladder. Follow the upper walkway to the
  raised crossing piece, lower it, and let the sister cross to
  the far route. Move both into the next room.
- Exit: the boy and sister have passed into the room with lockers
  and the boy can move normally. Stop before checking the lockers.
- Included: direct movement, a contextual companion command and
  input cue, conditional stop, separated positions, solid tube
  traversal, a far ladder, the lowered bridge and reunion in
  the next controllable room.
- Excluded: the earlier fan and leg-up, reactivation of power as
  a separate fixture, exact rotation and landing tolerances, fail
  recovery, two-human co-op, door or tube alternatives, optional
  masks, later chapters, post-launch additions or DLC, demo, other
  ports and any checkpoint claim.
- Potential scoped module: compare the temporary fan pause and
  alternate stop on the opposite side of the earlier fan.
- Direct-play status: no personal Windows execution or binary
  inspection. Steam and THQ Nordic identify the released product.
  W1 shows the Steam PC route, and W2 explicitly
  identifies its PC solo run and shows the crucial separation.
  The independently recorded solo segment W3 and two release
  guides corroborate the control and physical sequence.
  Only short video frames were examined in the background, with audio excluded.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
| --- | --- | --- | --- | --- | --- |
| RA-001 | The commercial Tarsier Studios game supports Windows Steam and a single-player campaign. These sources identify the February 2026 base game separately from its demo and other editions. | Confirmed | Direct | High | P1, P2, W1, W2 |
| RA-002 | Near the local lever, the boy can operate the stop and the game reveals a context-specific command to have the sister interact. W2 shows the controller call prompt. Its destination is the stop lever in this fixture. | Observation | Corroborated | High | W2 10:40–10:47, R1, R2 |
| RA-003 | The tube can spin when the stop is not held. Once the sister takes and holds the lever, the boy is free to descend. The sibling remains at the illuminated control while he walks the stopped tube and climbs the far ladder. The guided route specifically uses a supported part of the tube. | Observation | Corroborated | High | W2 10:45–10:55, W1 13:15–13:30, W3 3:27:10–3:27:30, R1, R2 |
| RA-004 | At the far walkway the boy can lower the separate raised crossing piece. This provides the subsequent route for the sister, who leaves the lever position and follows along the far-side walkway. | Observation | Corroborated | High | W2 10:57–11:12, W1 13:30–13:43, R1, R2 |
| RA-005 | Both siblings reach the next locker room. Direct movement is visible after the room transition. The observed terminal is the controllable room without testing retention after reload. | Observation | Corroborated | High | W2 11:14–11:17, W1 13:43–13:51, W3 3:27:40–3:27:50, R1 |

## Basic data

- Release / origin: Tarsier Studios and THQ Nordic, February 13, 2026.
  Windows Steam commercial base game and solo campaign.
- Mechanical families: FAM-015 for splitting and reuniting control roles,
  and FAM-017 for the order of hold, climb, connection and joint exit.
- P1: [Publisher's Steam base-game listing](https://store.steampowered.com/app/2129530/REANIMAL/).
  Establishes app identity, Windows requirements and the single-player
  offering. The product page may show Steam's age check.
- P2: [THQ Nordic release announcement](https://thqnordic.com/news/critically-acclaimed-co-op-horror-adventure-reanimal-is-out-now).
  Confirms the commercial PC release date and publisher.
- W1: [Gamer's Little Playground Steam PC capture](https://www.youtube.com/watch?v=706KU84MdX8&t=783s),
  dated February 14, 2026. Use 13:03–13:51 around the tube and door approach.
- W2: [xp-54 PC solo Chapter 1 capture](https://www.youtube.com/watch?v=BaYw2LjGgho&t=639s).
  Use 10:39–11:17 to read the cue, see the two positions and enter the room.
- W3: [NeatPick's labelled single-player segment](https://www.youtube.com/watch?v=iP3hfqsfDaM&t=12420s).
  Use 3:27:00–3:27:50. The source separates its solo and co-op segments.
  Its capture platform does not establish the Windows identity independently.
- R1: [PowerPyx's release-day Chapter 1 route](https://www.powerpyx.com/reanimal-chapter-1-walkthrough/).
  Corroborates the lever, tube surface, ladder and final bridge.
- R2: [Lauren Sayles's Chapter 1 route and control reference](https://adventuregamers.com/walkthroughs/reanimal#h-chapter-1-dead-in-the-water).
  Corroborates the motion when the boy lets go and the subsequent sibling role.
- Claim IDs: RA-001–RA-005.

### Reproducible fixture evidence

1. After turning on power earlier in Chapter 1, reach the small catwalk
   beside the rotating tube with both characters. At about 10:40 in W2,
   two separate figures stand on the control platform.
2. Operate the local stop, release it and use the context prompt by
   the lever. W2 displays its call instruction near 10:46. By about
   10:49 the boy is away from the control and the sister is holding it.
3. Follow the boy onto the curved tube surface and use the far ladder.
   Around 10:52 the lamp at the lever and the boy's separate approach
   to the ladder are visible in the same room. Avoid the missing
   section identified by R1.
4. From the upper walkway, lower the raised metal span. Around
   11:03–11:10 in W2 the route admits the sister, who leaves the
   lever station. Compare the separate light positions before and
   after this transition.
5. Go through the door and regain control in the room with the
   lockers. W2 shows both characters inside at about 11:15, moving
   farther in at 11:17. Stop before opening any locker.

## Mechanical decomposition

### Action Genes

- ACT-008: move on the catwalk, descend to supported tubing and
  climb to the far-side route. RA-003–RA-005.
- ACT-341: manipulate the local lever and the later hinged crossing
  piece within reach. RA-002, RA-004.
- ACT-726: request that the sister interact with the addressed stop
  lever while the boy remains under player control. RA-002, RA-003.

### System Behaviour Genes

- SYS-407: the sister independently occupies the delegated control
  and follows after a connected route is available alongside the
  directly controlled boy. RA-003–RA-005.
- SYS-1958: the held stop leaves an otherwise turning surface
  traversable while the holder stays at its control. RA-003.
- SYS-1959: from the far side, one character lowers a separate
  hinged piece into a usable crossing for the still-separated
  helper. RA-004.

### Constraint Genes

No separate admission. The fixture bounds its support and turn
condition through the two traversable-surface rules.

### Information Genes

- INF-630: the local prompt discloses the contextual companion
  interaction when the player is beside the lever. The command
  does not describe the later bridge route. RA-002.

### Objective Genes

- OBJ-362: move the first character across using the held stop,
  open the far-side passage for the helper and enter the next
  controllable space together. RA-003–RA-005.

### Time Genes

- TIM-002: the player can stage the call and the far bridge in
  an ordered local sequence at the player's pace. The hold keeps
  the traversal surface stopped while both roles are maintained.
  RA-002–RA-004.

## Reproducible transitions

| From | Input or event | To | Evidence |
| --- | --- | --- | --- |
| Two siblings on arrival-side lever catwalk | Operate the local stop and read the call cue | Context for delegating the lever to the sister | RA-002 |
| Stop available, boy beside the lever | Use Call so the sister takes the control | Holder stays at the control, tube stops, boy is free to traverse | RA-003 |
| Sister holding, boy at edge | Descend onto the supported face and climb the far ladder | Boy on the far walkway, sister still separated | RA-003 |
| Boy on far walkway with crossing piece raised | Lower the crossing piece | A separate usable span allows the sister to join him | RA-004 |
| Both can use the exit approach | Move through the door | Both in the next locker room with ordinary movement available | RA-005 |

## Strategic and experiential structure

Stopping the tube and crossing it require distinct positions.
A solo player assigns the first role to the sister and keeps
direct control of the boy for the second. The solution still
needs a return route for her. The separate span lets the pair
leave the temporary stop behind.

## Replay and variation

The independent recordings show matching destinations after
different amounts of time spent near the controls. No fixed
countdown or perfect stopping angle was inferred. The exact
input thresholds, blocked states and later save recovery
are outside the evidence.

## Adjacent systems and history

The Midnight Walk also uses an addressed autonomous helper.
Its helper can pass through a restriction and release a bridge
for the player. Here the directly controlled sibling reaches
the far side and restores the route for the temporary holder.

## Normalised genome

| Type | Stable genes | Role |
| --- | --- | --- |
| Action | ACT-008, ACT-341, ACT-726 | Navigate, use local fixtures and delegate the lever |
| System Behaviour | SYS-407, SYS-1958, SYS-1959 | Resolve the sister, held stop and far-side span |
| Constraint | None | Represent stop and support directly in the two crossing behaviours |
| Information | INF-630 | Expose the eligible companion command beside the stop |
| Objective | OBJ-362 | Advance both characters into the next controllable room |
| Time | TIM-002 | Stage each local action while the hold supports travel |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `683` (`GAME-0001`–`GAME-0683`).
- Exact genome matches: none.
- Tied near matches: `GAME-0683` — Last Window: The Secret of Cape West (`3 / 13 = 0.230769`).
- Supported combination subsets: none.
- Scan date: 2026-11-24.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
| --- | --- | --- | --- |
| [Last Window: The Secret of Cape West (GAME-0683)](../g-l/last-window-the-secret-of-cape-west.md) | ACT-008, ACT-341, TIM-002 | Both move between fixtures and apply distinct contextual interactions in sequence. Last Window follows a directional dial trace and inspects separate papers. REANIMAL separates two physically present characters across a stopped tube and reunites them through a different span. | Near, `0.230769` |

## Taxonomy impact

Four admissions distinguish the held stop, the far-side
bridge for its holder, the contextual companion cue and the
two-person exit. Existing control, approach, fixture use
and autonomous follow definitions are reused.

## Negative results

- Parking the boy at the stop does not put him on the tube.
- Moving the boy to the far platform leaves the sister separated
  until the return-side crossing is available.
- The deployment of a separate span changes what the sister
  can traverse. It is distinct from stopping the tube.
- Entering the room does not itself inspect the optional mask.
- No post-restart state was observed.

## Delta summary

Nine genes, four newly admitted. The observed local route
advances both siblings from one catwalk to the locker room
through two different ways of providing support.

## New facts

- A contextual call can give the sister the continuously held stop.
- A stopped tube provides a route for the other character.
- The far-side action provides a different route for the holder.
- The following room restores ordinary movement for the player
  with both siblings present.

## Principles and design implications

One actor can maintain a transient support while another reaches
a lasting connection. Make the operator's location and the
alternative crossing visible so the player can understand
each role's purpose while they are separated.

## Puzzle or game generation potential

An original industrial traversal puzzle can let a stationary
helper hold a contact-controlled stop while the player crosses
a disabled roller, then let the player deploy a separate ramp
from the far side for that helper.

## New genes

- INF-630
- OBJ-362
- SYS-1958
- SYS-1959

## New combinations

None admitted. All 274 verified combinations were checked as proper subsets.

## Taxonomy changes

[Taxonomy Change 430](../../../research/taxonomy-changes/TAXONOMY_CHANGE_430.md).

## New questions

- What happens when the call is sent before the boy uses the lever?
- What clearances determine a viable stopping orientation?
- Which state is restored if an actor falls before the span is placed?

## Next recommended game

Close Selection 058 with the nine-game acceptance checkpoint.
The next selection starts at `GAME-0685` after the continuation
window.

## Why this game

The same crossing puzzle uses a temporary support for the one
who can travel and a different route to reunite the pair.
