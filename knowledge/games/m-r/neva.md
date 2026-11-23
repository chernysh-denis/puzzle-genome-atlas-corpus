---
game_id: GAME-0588
slug: neva
game_title: Neva
analysis_status: reviewed
reviewed: 2026-11-20
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-161
    - ACT-223
    - ACT-341
    - ACT-535
  system:
    - SYS-215
    - SYS-369
    - SYS-407
    - SYS-456
    - SYS-578
    - SYS-799
    - SYS-1049
    - SYS-1064
    - SYS-1386
    - SYS-1388
    - SYS-1732
    - SYS-1733
    - SYS-1734
    - SYS-1735
  constraint:
    - CON-076
    - CON-773
  information:
    - INF-142
    - INF-536
  objective:
    - OBJ-080
  time:
    - TIM-003
---

# Game: Neva

Use the [canonical vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
Lead a wolf cub through passages she cannot cross alone, then survive
the chase and defeat its pursuer to leave Summer together.

## Analysis scope

- Version / ruleset: October 2024 full commercial Nintendo Switch base
  release, North American eShop product, English available. Reproduce
  in solo Adventure Mode from a new base-game run. The release-window
  Switch capture is displayed in Spanish, shows the three life markers
  used in adventure play, and does not identify the executable revision.
  English labels in the record are used for reference.
- Structured analysis target: PLAT-NINTENDO-SWITCH.
  See [platform coverage](../../platforms/games.json).
- Entry: first control of Alba and the sleeping cub on the Summer forest
  floor after the base game's opening scene. Include both Summer parts.
  Halfway, the first rescue reaches the shared stump and the second part
  begins by waking the cub there. The opening scene itself is context.
- Primary decision loop: judge what Alba can cross by jumping or dodging
  and what the cub can follow. Call or reassure her at authored hang-ups.
  Fight with the sword, clear remote sources of thorns and cut restraints
  before proceeding. In combat, time defence and attack sequences to keep
  enough life for later waves. Use the route's ordered gates and staircase
  switch to reach the pursuer fight after the reunion.
- Positive exit: defeat the pursuer in the Summer boss field, allow the
  chapter transition and regain ordinary control in Fall with Neva.
  Stop before using the older wolf's own directed attacks.
- Negative exit: exhausted Alba vitality fails the current encounter or
  crossing in Adventure Mode and play returns to an authored checkpoint.
  Remaining separated at the companion gates stalls progress. Precise
  save internals, restraint timeout and universal pit-reset behavior
  are not established.
- Included: the dependent cub's follow, distraction and accepted call;
  double jump, protected dash and directed sword strikes; health,
  sequence healing and local recovery; linked thorns and reassurance,
  live chase and split, descent, arena clear and two staircase positions,
  phased boss responses and next-chapter entry.
- Excluded: Story Mode, optional fruit and hidden flower achievement
  routes, their collection and save policy, ports, the 2026 paid
  Neva: Prologue expansion, demo rules, all later season decisions,
  exact frame or healing coefficients, and end-of-campaign claims.
- Potential scoped module: Fall Part 1's directed wolf charge and the
  later encounters that depend on it.
- Direct-play status: no native game or input execution. Nintendo and
  Nomada identify the released product and young companion behavior.
  Release-window Switch and independent guide stills corroborate the
  entire Summer path through the first part of Fall. Exact patch and
  inputs between stills remain unverified. Video and audio were not
  played. Accounts from other carriers corroborate qualitative rules.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
| --- | --- | --- | --- | --- | --- |
| NV-001 | The original Switch eShop base game released on 15 October 2024; its Summer opening and two-part path precede Fall. The later paid Prologue is a separate product. | Confirmed | Direct | High | P1, P2, P4; W1 3:50/16:20/16:50/38:30 |
| NV-002 | The cub ordinarily follows and sometimes investigates the scenery. At authored difficult crossings, her hesitation or fall interrupts following. Alba can reassure nearby, then call from the far ledge to encourage a viable jump. | Observation | Corroborated | High | P3; W1 4:20/5:30/5:50; W2 6:50/7:10; R1 |
| NV-003 | Alba can steer, jump a second time in the air, use a brief protected dodge on land or in air, and make forward and downward sword attacks. These verbs permit safe passage through selected thorns and leave ordinary damage possible outside the dodge window. | Observation | Corroborated | High | W1 8:20–9:00, 18:10–19:10; R1, R2, R3 |
| NV-004 | Adventure vitality is shown as three flower markers. Eligible sequences of landed attacks restore a missing marker during combat. Healing fixtures also restore vitality; zero life leads to retry from an authored checkpoint. Exact sequence threshold, timing and checkpoint fields are unverified. | Observation | Corroborated | Medium | W1 12:00/12:10/30:10/30:50; W2 13:40; R1, R3, R4 |
| NV-005 | At the first masked-source gate Alba can dash past the hazard but the cub waits. Reaching and defeating the separate masked creature removes the linked thorns so the cub can follow. Later barriers depend on additional separate sources. | Observation | Corroborated | High | W1 18:10–19:20, 26:50–28:50; R1 |
| NV-006 | Hands can hold or threaten Neva during the first part. Cutting the restraints and clearing the local attack leaves a separate prompt to comfort the cub before onward travel. The first part closes at the resting stump. | Observation | Corroborated | High | W1 15:50–16:50; R1; P3 |
| NV-007 | In the second part, a large hostile pursues Alba and Neva across foreground hazards. Alba chooses jumps and dodges while the route remains live. The authored collapse splits their paths rather than confirming a game-over state. | Observation | Corroborated | High | W1 22:10–24:10; W2 25:20–27:30; R1, R2 |
| NV-008 | The separated routes meet after a sequence of mask-controlled barriers. Remove each linked blocking set, reach the cub and pet her to resume following. A later arena can place the pursuer's attacks and lesser enemies in the same space. | Observation | Corroborated | High | W1 26:50–30:50; W2 28:50–32:20; R1, R2 |
| NV-009 | Defeating the enemies below the final staircase chamber permits its totem interaction. A strike on the gong changes the staircase alignment and gives access to the last masked source. Returning the staircase to the other alignment permits the route to the boss after the thorns are cleared. | Observation | Corroborated | Medium | R1; W1 29:30–33:30; W2 32:20–34:30 |
| NV-010 | The pursuer becomes the Summer boss. Its local swipes, surrounding thorns and low-reaching spread call for different dodges or jumps, with opportunities to counter. Its defeat settles the season and the next active scene includes both actors. | Observation | Corroborated | High | W1 34:10–38:50; W2 36:00–38:20; R1, R2 |
| NV-011 | Publisher descriptions establish that Neva's capabilities change with age. The Autumn handoff is retained, but issued attack commands and later capability growth are outside the Summer signature. | Confirmed | Direct | High | P1, P3; W1 38:00–38:50 |

## Basic data

- Nomada Studio and Devolver Digital. FAM-010 for the live chase and
  combat. FAM-017 for the ordered rescue, barrier and staircase states
  that determine when successive route segments become usable.
- P1: [Nintendo's US Switch listing](https://www.nintendo.com/us/store/products/neva-switch/).
  Base digital title, Nintendo Switch, one player and 15 October release.
  The page lists the later Prologue separately; compatibility information
  does not make Switch 2 the analysed platform.
- P2: [Devolver Digital's product page](https://www.devolverdigital.com/games/neva).
  Dates the commercial launch and describes the platforming, combat and
  developing companion. No exact release executable is supplied.
- P3: [Nomada programmer Roger Mendoza's design account](https://blog.playstation.com/2024/10/10/neva-nomada-studio-shares-a-deep-dive-into-the-design-and-dualsense-features-of-its-gorgeous-ps5-platformer/).
  Describes the cub's distractions, calls and reassurance and distinguishes
  them from the older wolf's directed attacks. Platform-specific controller
  feedback and later abilities are not transferred to the Switch packet.
- P4: [Devolver's February 2026 Prologue announcement](https://www.devolverdigital.com/propaganda/neva-prologue-is-available-now).
  Identifies the later paid release and its new locations and mechanics.
- W1: [Freidan's release-window Nintendo Switch route](https://www.youtube.com/watch?v=zSmfo0ZrBF8)
  published 19 October 2024. Static frames establish the forest entry,
  waiting-cub crossing, rest, early thorns, two actors in the chase,
  post-collapse separation, reunion, stairs, boss and first Fall movement.
  Some nighttime samples obscure single inputs. The record does not use
  them to assert frame timing or the exact order of overlapping contacts.
- W2: [CHRSuperstar's October 2024 documented route](https://chrsuperstar.com/neva/en/)
  and [recorded guide](https://www.youtube.com/watch?v=TLkJRNTs_Ko).
  Its 7:10 gap, 13:40 health prompt, 25:20 pursuit, 28:50–30:50 reunion,
  32:20–34:30 stair route and 36:00–38:20 end corroborate the principal
  states. This cut does not authenticate another Switch binary.
- R1: [Neoseeker's solver's Summer guide](https://www.neoseeker.com/neva/walkthrough/Summer).
  Explicit first and second parts, including the separate masks, changed
  stairs, Adventure health rules and cub recovery. Its DualSense labels
  are omitted from the Switch reproduction.
- R2: [Pro Game Guides' 16 October 2024 own-play route](https://progameguides.com/general-walkthroughs/neva-walkthrough-100-all-achievements/).
  Corroborates the two Summer parts, boss responses and later season.
- R3: [CGMagazine's release-window Switch play](https://www.cgmagonline.com/review/game/neva-switch-review/).
  Reports three health segments, sequences for healing and distinct
  platforming. Exact invulnerability frames are left open.
- R4: [Shacknews' release review on Steam](https://www.shacknews.com/article/141781/neva-review-parental-discretion-is-revised).
  Corroborates Adventure versus Story, role of the healing fixtures
  and health recovery through combat. Numerical thresholds in play
  reports disagree; none is treated as established Switch behavior.
- Sources accessed 2026-11-20.

## Mechanical decomposition

### Action Genes

- ACT-008 moves Alba through the side-on route; ACT-161 commits reach- and
  direction-dependent sword hits, including the descending strike
  (NV-003, NV-005, NV-009).
- ACT-223 times a dodge or jump against a currently attacking enemy.
  ACT-341 operates the reached contextual totem after its condition is met
  (NV-003, NV-009, NV-010).
- ACT-535 addresses the cub to wake, summon or reassure her. The input
  does not hand over direct control of her body (NV-002, NV-006, NV-008).

### System Behaviour Genes

- SYS-215 resolves live combat; SYS-799 changes the active boss attack
  pattern after sufficient progression within that same fight. Exact
  health thresholds and recovery frames are not established (NV-003, NV-010).
- SYS-578 applies health loss and restoration to Alba. SYS-1733 awards
  one missing unit on a qualifying sequence of landed strikes, distinct
  from route fixtures and automatic recent-loss recovery. SYS-369
  restores an authored checkpoint after failure (NV-004).
- SYS-407 supplies the cub's autonomous following and context reactions.
  SYS-1064 resolves a viable request across an authored crossing and
  leaves the cub behind if her capability is insufficient (NV-002, NV-005).
- SYS-456 resolves qualified protected dodge overlap. SYS-1386 supplies
  the one further airborne jump. SYS-1388 drives the live pursuit.
  SYS-1049 removes a support and redirects the route at the separation
  (NV-003, NV-007).
- SYS-1732 clears linked thorns by defeating their independent masked
  source. SYS-1734 gates resumed following on clearing restraints and
  reassuring the dependent. SYS-1735 alternates the revealed staircase
  layout on eligible strikes (NV-005, NV-006, NV-008, NV-009).

### Constraint Genes

- CON-076 differentiates Alba's movement and attacks from the young cub's
  reachable passages and accepted calls. CON-773 requires positive
  Adventure vitality for the ongoing local attempt (NV-002–NV-005).

### Information Genes

- INF-142 exposes hostile attack cues and recovery via silhouette changes,
  wind-up and root patches. INF-536 exposes the cub's current attention,
  refusal and readiness via her posture and actions. Neither exposes
  an exact timing, trust meter or solved future route (NV-002, NV-007, NV-010).

### Objective Genes

- OBJ-080 clears the required routes, reunions and the pursuer fight before
  reaching the next season. Boss arrival alone and optional collectibles
  do not establish this terminal (NV-006–NV-011).

### Time Genes

- TIM-003 represents the live decisions during chase and combat; the
  pursuer advances while movement and attack commands remain available.
  No global countdown is implied (NV-007, NV-010).

## Reproducible transitions

| Initial state | Intervention | Discriminating result | Evidence |
| --- | --- | --- | --- |
| Summer starts with the cub resting on the forest floor | Use the companion interaction and walk toward the first platforms | The cub wakes and usually follows on traversable ground, with local changes of attention. | NV-001, NV-002 |
| The cub falters at the practice rocks | Approach to reassure her, cross by double jump or dash, then call from a reachable far side | She elects to cross when able. Leaving without the call does not directly move her across. | NV-002, NV-003 |
| Alba has a missing flower marker and reachable enemies | Land a qualifying attack sequence while using evasion to remain alive | One missing unit can return during combat. A different route interaction restores health at a healing fixture. | NV-004 |
| Shadow hands hold the cub during the first rescue | Cut the hands, settle the local threats, then interact beside the cub | Removing the threat opens access, and comfort restores following toward the rest. | NV-006 |
| The first part ends at the stump and darkness fades | Wake the cub at the start of the second part | The same pair controls ordinary onward travel in the changed Summer scene. | NV-001, NV-006 |
| A thorn patch separates the grounded cub from reachable platforms | Jump-dodge past the thorns, then reach and strike the masked source | Alba crosses before the cub. The rooted hazard disappears only after its linked source is defeated. | NV-003, NV-005 |
| The pursuer approaches across ground-level hazards | Use platforms, jumps and protected dodges to survive until the collapsing support | The scripted collapse separates the two actors and routes Alba below without ending the attempt. | NV-007 |
| The separated cub is above the chamber | Remove the first source, take the newly available approach to the remaining sources, then comfort the cub | The cleared links permit access and the summoned cub resumes following. | NV-005, NV-008 |
| The final chamber has an unavailable staircase | Clear the lower arena, activate the revealed totem, strike the gong, destroy the reachable source and strike again | A first alignment provides access to the controller; the other gives access to the unblocked exit. | NV-009 |
| The pursuer prepares its low sweep, leap or thorns | Time the matching dodge or jump, then strike during an opening | Damage can be avoided or incurred separately from the chosen attack. The boss changes its patterns before defeat. | NV-010 |
| Alba's Adventure life is exhausted | Allow the retry to settle | The failed attempt gives way to checkpoint control rather than a living continuation from the damaging overlap. | NV-004 |
| Summer boss has fallen | Allow the transition to complete | Alba regains ordinary control in Fall with Neva. This is the packet boundary. | NV-010, NV-011 |

## Strategic and experiential structure

Alba's rapid route can strand the cub. Look back for hesitation, and
distinguish a gap the cub can cross after the call from thorns that make
her route illegal. During encounters, landing more hits may earn a life
unit, but taking a short opening to evade may be safer than attempting
another strike. The chase resolves into a separation that traversal
alone cannot fix; the separate targets and reassurance explain what
actually completes the reunion.

## Replay and variation

The same route, reunion gates and boss are evident in the two documented
runs. Combat damage, attack order, timing and optional fruit or flowers
may vary. No variable spawn algorithm or exact enemy health is inferred.
The paid expansion and Story Mode require their own tested scope.

## Adjacent systems and history

Ico transfers the call and dependent's physical traversal boundary.
Its portal-bound abduction and companion-operated doorway differ from
freeing the cub and clearing linked thorns with Alba's own sword. South
of Midnight transfers a bounded chase, one extra airborne jump and a
vitality failure gate. Its dark-magic purification and attack-spell
recovery are not the same as earning one life unit through landed
strikes or changing the terminal staircase.

## Normalised genome

| Type | Active gene IDs | Carrier parameters |
| --- | --- | --- |
| Action | ACT-008, ACT-161, ACT-223, ACT-341, ACT-535 | movement, sword, dodge or jump, totem and companion interaction |
| System Behaviour | SYS-215, SYS-369, SYS-407, SYS-456, SYS-578, SYS-799, SYS-1049, SYS-1064, SYS-1386, SYS-1388, SYS-1732, SYS-1733, SYS-1734, SYS-1735 | live combat, retry, cub behavior, chase, terrain and recovery transitions |
| Constraint | CON-076, CON-773 | different movement capabilities and positive Adventure health |
| Information | INF-142, INF-536 | attack cues and the cub’s readiness |
| Objective | OBJ-080 | Summer guardian and Fall entry |
| Time | TIM-003 | live chase and combat |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `587` (`GAME-0001`–`GAME-0587`).
- Exact genome matches: none.
- Tied near matches: `GAME-0516` — Hi-Fi RUSH (`12 / 43 = 0.279070`).
- Supported combination subsets: none.
- Scan date: 2026-11-20.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
| --- | --- | --- | --- |
| GAME-0516 Hi-Fi RUSH | ACT-008, ACT-161, ACT-223, ACT-341, INF-142, OBJ-080, SYS-1386, SYS-215, SYS-369, SYS-578, SYS-799, TIM-003 | Both alternate authored traversal and active combat before a phased guardian. Neva has a dependent cub, linked hazards, hit-sequence healing and stairs. Hi-Fi RUSH uses beat-synchronised attacks, Reverb and graded encounter settlement. | `12 / 43 = 0.279070` |

### Preserved research notes

- New genes: SYS-1732, SYS-1733, SYS-1734 and SYS-1735.
- Classification result: New gene.

## Taxonomy impact

- [TAXONOMY_CHANGE_334](../../../research/taxonomy-changes/TAXONOMY_CHANGE_334.md)
  isolates the distant hazard controller, combat-sequence healing,
  restraint plus reassurance, and a struck two-layout traversal structure.

## Negative results

- A dash through a thorn patch does not clear it. SYS-1572 destroys a
  root by direct dash overlap and does not model the masked source.
- The young wolf is not a selectable combat avatar or an aimable charge.
  No later growth command is presumed in Summer.
- Neither a fixed portal-capture deadline nor an autonomous perfect
  rescue is established. Combo thresholds disagree in written play
  accounts; the evidence supports a qualitative award, not a guaranteed
  numeric ratio or per-hit leech.
- Fruit and the hidden collectible flowers are distinct from Alba's
  current life markers. Gardening, inventory and a hunger meter are
  not inferred from the voluntary feeding scenes.
- Any scenery, attack naming and guides' fountain terminology remain
  carrier particulars. The underlying normal or story implementation
  is not reverse-engineered.

## Delta summary

## New facts

- [Observation | Corroborated | High] Alba can pass a hazard which
  blocks the cub, then alter the shared route by defeating its source.

## New genes

- [Observation | Corroborated | Medium] Four additions in TAXONOMY_CHANGE_334.

## New combinations

- [Observation | Corroborated | High] No new verified combination
  proposed. Existing subsets appear in the comparison.

## Taxonomy changes

- [Observation | Corroborated | Medium] Earlier definitions and
  signatures are retained.

## New questions

- A native Switch test could measure the healing count, missed-strike
  consequences, failure recovery fields and exact boss damage intervals.

## Next recommended game

- [Hypothesis | Limited | Medium] GAME-0589, ChuChu Rocket! on Dreamcast.
  Bound the released North American puzzle mode to one whole solve.
- Optimisation criterion: contrast caring for an autonomous companion
  with arranging paths for independently moving groups.

## Why this game

- [Hypothesis | Limited | Medium] The first complete season offers
  different causes of separation and positive counterfactuals for
  an active call, terrain opening and reassurance.
