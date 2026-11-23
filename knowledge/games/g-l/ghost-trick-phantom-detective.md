---
game_id: GAME-0533
slug: ghost-trick-phantom-detective
game_title: "Ghost Trick: Phantom Detective"
analysis_status: reviewed
reviewed: 2026-11-17
combination_ids: []
gene_ids:
  action:
    - ACT-049
    - ACT-341
    - ACT-729
    - ACT-730
  system:
    - SYS-369
    - SYS-1540
    - SYS-1541
    - SYS-1542
    - SYS-1543
  constraint:
    - CON-068
    - CON-811
  information:
    - INF-179
    - INF-517
  objective:
    - OBJ-298
  time:
    - TIM-003
    - TIM-035
---

# Game: Ghost Trick: Phantom Detective

Use the [canonical vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
The four-minute return, object positions and opening durations parameterise the
observed rules.

## Analysis scope

- Version / ruleset: original English European Nintendo DS cartridge,
  released 14 January 2011, standard single-player touch controls.
  Platform: PLAT-NINTENDO-DS. The retail identity is verified. No
  cartridge revision or binary identity was observed.
- Entry: in Chapter 1, 7:02 PM, reach Lynne's corpse via Ray's desk lamp
  after the opening tutorial death. Begin with the corpse as the selected
  host and the rewind option available. Use the authored four-minutes-before-
  death intervention. Stop when the final intervention averts Lynne's death
  and the game returns to the revised present in the scrapyard, before
  the umbrella and telephone sequence. A missed deadline is a failed
  attempt with an available retry, not completion of the packet.
- Primary decision loop: freeze the scene in Ghost World and inspect the
  current host and nearby cores. Choose a reachable core, leave Ghost
  World and apply a live trick or wait for a host's motion. Use the changed
  positions and running deadline to obtain another intervention. Recognise
  the bicycle bell as only a partial save, then finish the rescue.
- Included: corpse-anchored rewind, live timer and a frozen traversal
  mode, range-limited core transfers, host-specific commands, the rolling
  tyre and refrigerator, fan, flag and blender, bicycle and partial
  checkpoint, lever, ladder and claw, revised present and retry.
- Excluded: the earlier tutorial tricks, later investigation, phones and
  later deaths, other spirits' powers, long-term cartridge save behaviour,
  iOS variants, the HD remaster, hardware shortcuts and mods.
- Direct-play status: no cartridge or executable was run. Capcom's fact
  sheet and Nintendo's original platform announcement and regional guide
  establish the main rules. Independent DS play accounts corroborate the
  named transitions. Only written material and static source references
  were consulted. Frame timing and save-file internals remain unmeasured.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
| --- | --- | --- | --- | --- | --- |
| GT-001 | The original English European Nintendo DS release shipped on 14 January 2011, and Capcom describes the stylus-based possession and object interaction. | Confirmed | Direct | High | P1, P2 |
| GT-002 | Possessing Lynne's corpse after the tutorial unlocks a rewind to her authored pre-death state. The replay reveals the outcome to prevent, after which live control begins. The player does not select a frame to edit. | Observation | Corroborated | High | P2, P3, S1 |
| GT-003 | The stylus transfers Sissel to a sufficiently close core in Ghost World. The DS interface marks cores and describes the currently possessed object and whether it has a usable trick. Some hosts only relay movement. | Observation | Corroborated | High | P2, P3, S2, S4 |
| GT-004 | Ghost World suspends the rescue timer and world motion while accepting host transfers. Leaving it permits live tricks and resumes event progression. The top-screen hourglass and short reaction phase communicate the deadline. Missed rescue attempts can be retried. | Observation | Corroborated | High | P3, P4, S1, S2 |
| GT-005 | The tyre moves the mannequin into useful range. Opening the fridge releases the blender. Once the blender is running and the fan blows the flag line toward it, the line is drawn in and the flag rises. Sissel must occupy the flag before it ascends to ride it toward the bicycle. | Observation | Corroborated | High | P3, S1, S3 |
| GT-006 | The handlebar bell disrupts the first imminent failure and the game continues in a changed situation. Lynne cannot escape across the raised bridge. The bell supplies a partial checkpoint rather than the final success. | Observation | Corroborated | High | P3, S1, S3, S5 |
| GT-007 | Use the pedal core to move with the bicycle. At the new position operate the lever, then extend the ladder. Transfer via streetlamp and suspended ball to the claw. Releasing the positioned ball removes the immediate threat and averts the death. | Observation | Corroborated | High | P3, S1, S3 |
| GT-008 | The final intervention returns control to a revised present with Lynne alive. The following umbrella and phone puzzle is a distinct problem. Missing the earlier window cannot be counted as the same outcome. | Observation | Corroborated | High | P3, S1, S3 |

## Basic data

- Release / origin: developed and published by Capcom. Nintendo distributed
  the original European Nintendo DS release on 14 January 2011.
- Families: real-time system pressure, agent routing and coordination,
  and ordered dependency sequencing.
- Sources accessed 2026-11-17:
  - **P1** — [Nintendo's original European launch bulletin](https://www.nintendo.com/en-gb/News/2011/In-shops-now-Ghost-Trick-Phantom-Detective-for-Nintendo-DS--253025.html),
    for the product, localised release date and rescue premise.
  - **P2** — [Capcom's original DS fact sheet](https://news.capcomusa.com/lets/browse/tgs-2010-ghost-trick),
    for touch input, possession, corpse rewind and the separate phone rule.
  - **P3** — Nintendo's original regional [controls reference](https://www.guiasnintendo.com/0_NINTENDO_DS/Ghost_trick/Ghost_trick_sp/explicacion.html)
    and [Chapter 1 guide](https://www.guiasnintendo.com/0_NINTENDO_DS/Ghost_trick/Ghost_trick_sp/capitulo1.html).
    The Spanish prose and DS screen references establish the mechanics;
    English interface text was cross-checked with the original DS accounts.
  - **P4** — [Shu Takumi's release-era interview](https://www.videogamer.com/previews/ghost-trick-interview/),
    written answers on the world stop and repeatable missed opportunities.
  - **S1** — [The Lost Gamer's English DS walkthrough](https://gamefaqs.gamespot.com/ds/974785-ghost-trick-phantom-detective/faqs/65327),
    Chapter 1, for the two rescue stages, the precise rope coupling and
    the mechanically separate lever and claw.
  - **S2** — [Nintendo Life's 2011 DS play review](https://www.nintendolife.com/reviews/2011/01/ghost_trick_phantom_detective_ds)
    and [Cubed3's DS play review](https://www.cubed3.com/games/reviews/nintendo-ds/ghost-trick-phantom-detective-2),
    for stylus transfers, world switch and repeatable rewinds.
  - **S3** — [Fukuyasu's original DS walkthrough](https://gamefaqs.gamespot.com/ds/974785-ghost-trick-phantom-detective/faqs/60327),
    Chapter 1, for the sequence and save point at the bell. This documents
    the Japanese DS release; it does not establish the English labels.
  - **S4** — [Capsule Computers' 2011 DS play review](https://www.capsulecomputers.com.au/2011/01/ghost-trick-phantom-detective-ds-review/),
    for the current host's limited reach and blue cores.
  - **S5** — [2011 English DS player review](https://gamefaqs.gamespot.com/ds/974785-ghost-trick-phantom-detective/reviews/145357),
    for the distinction between the partial fate change and final rescue.
- Claim IDs: GT-001–GT-008.

## Mechanical decomposition

### Action Genes

- Reuse `ACT-049`: operate the linked lever to position the wrecking
  ball. The same reached object has a specific activation rather than
  providing unrestricted steering.
- Reuse `ACT-341`: use an available trick on the refrigerator, bike
  handlebar, pedals, ladder or reached claw.
- New `ACT-729`: drag Sissel from his current host to an eligible nearby
  core in Ghost World. This transfers possession without running the
  destination's live trick.
- New `ACT-730`: select the corpse rewind to enter an authored
  pre-death intervention with the victim-specific memory of the event.
- Claim IDs: GT-002–GT-007.

### System Behaviour Genes

- Reuse `SYS-369`: a missed window settles as failure. Retry restores
  the relevant authored entry or available partial checkpoint.
- New `SYS-1540`: the spirit follows a possessed host's movement, changing
  the coordinates used to determine the next legal transfer.
- New `SYS-1541`: one powered appliance directs a loose tether toward an
  independently powered mechanism, which catches and draws the tether.
  The otherwise passive attached carrier is lifted.
- New `SYS-1542`: interrupt one lethal event, retain a partial checkpoint,
  and let the victim's new route expose a second threat. The prior
  intervention alone does not resolve the objective.
- New `SYS-1543`: set the position of a suspended load with linked
  control. Reach its distinct release and drop it at that alignment.
- Claim IDs: GT-004–GT-008.

### Constraint Genes

- Reuse `CON-068`: live scene progression ends a missed rescue window.
  Stopping the world postpones progression, and retry restores a
  previously declared state after failure.
- New `CON-811`: legal relocation must end at an eligible core within
  range of the presently occupied host. Several local transfers and
  moving hosts can reach a destination outside the initial range.
- Claim IDs: GT-003–GT-007.

### Information Genes

- Reuse `INF-179`: the scrapyard view, hourglass and prompted dialogue
  expose current props, threat progression and the need to intervene.
- New `INF-517`: Ghost World marks possessable cores, while the upper
  screen identifies the occupied object and indicates its trick status.
  A visible core by itself does not promise a usable live trick.
- Claim IDs: GT-003–GT-007.

### Objective Genes

- New `OBJ-298`: alter the bounded replay of a victim's lethal event
  until the game returns to a present in which they survived.
- Claim IDs: GT-002, GT-006–GT-008.

### Time Genes

- Reuse `TIM-003`: the live timeline keeps moving during manipulation
  and waiting, with narrow openings before a lethal scene event.
- New `TIM-035`: voluntarily stop scene progression for host transfers
  and inspection, then return to live time for the host's actual trick
  and movement effects.
- Claim IDs: GT-003–GT-007.

## Reproducible transitions

| Before | Action or event | Bounded resolution | What it establishes | Claim ID |
| --- | --- | --- | --- | --- |
| Lynne is dead and her body is the current host | Use the rewind option | View the earlier sequence, then regain intervention control before her death | The clock returns to an authored event start | GT-002 |
| The current host and a nearby eligible core are visible | Select Ghost World and trace from host to core | The spirit changes host while the world and timer remain stopped; a sufficiently distant core still cannot be reached directly | Planning can move the spirit but cannot move objects | GT-003, GT-004 |
| The blender is inside the refrigerator | Use the tyre and mannequin route, open the fridge, then close it | The blender is available as an exposed core on the next route | Activating a reachable object can expose a distinct relay | GT-005 |
| Both appliances can be reached but the flag is low | Start the blender, start the fan, then occupy the flag before the lift | Airflow directs the loose line into the running blender, and the line draws the flag upward with Sissel aboard | Two separate device states lift a host that must already be occupied | GT-005 |
| Lynne faces the first imminent failure and Sissel reaches the handlebar | Ring the bell in the live world | Lynne evades the immediate threat but is cornered by the raised bridge; the changed situation provides a partial checkpoint | A changed fate can be retriable without counting as the rescue | GT-006 |
| The new threat is by the bridge | Move using the pedal core, activate the lever, extend the ladder and reach the claw via the lamp and ball | The first commands position the suspended load and make its release reachable. Activating the claw drops the load at the aligned position. | Positioning and releasing the load are different operations | GT-007 |
| The final intervention has resolved | Let the scene settle | Sissel returns to the revised present with Lynne alive | Final success is survival in the present, not temporary escape in the replay | GT-008 |

## Strategic and experiential structure

The player can think and relocate in suspended time. The moving world is
necessary to execute the plan: turning a prop on, allowing a host to
advance, or interrupting the victim's lethal sequence. One useful transfer
can lead to a passive core rather than an activation. The bell creates
a new problem instead of completing the rescue. The lever and claw split
the final effect into placement, access and release.

## Replay and variation

- The condition at corpse rewind is authored. The changing states
  depend on when the player returns to live time and where Sissel is
  when an object moves.
- Try remaining off the flag when it rises and compare reachable cores.
  Compare ending the active window before the bike bell with the state
  after it rings. Restart from an offered state when an intervention
  is missed.
- The original guide documents a short reaction phase but does not
  establish the exact frames, carry-over timers or all recovery choices.
- Claim IDs: GT-004–GT-008.

## Adjacent systems and history

- The following umbrella and phone sequence uses possessed objects to
  follow a witness and travel outside the scrapyard. Its goal and
  transitions fall outside this rescue.
- Later spirits and routes use additional powers; the HD remaster is
  not the analysed build.
- Claim IDs: GT-001, GT-002, GT-008.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
| --- | --- | --- |
| Action | `ACT-049`, `ACT-341`, `ACT-729`, `ACT-730` | linked control, live trick, host jump, corpse rewind |
| System Behaviour | `SYS-369`, `SYS-1540`, `SYS-1541`, `SYS-1542`, `SYS-1543` | retry, host motion, tether lift, partial rescue, aligned release |
| Constraint | `CON-068`, `CON-811` | live deadline, range from occupied core |
| Information | `INF-179`, `INF-517` | local situation and host eligibility display |
| Objective | `OBJ-298` | revised present with Lynne alive |
| Time | `TIM-003`, `TIM-035` | live progression and suspended transfer |

Canonical signature:

`ACT-049,ACT-341,ACT-729,ACT-730; SYS-369,SYS-1540,SYS-1541,SYS-1542,SYS-1543; CON-068,CON-811; INF-179,INF-517; OBJ-298; TIM-003,TIM-035`

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `532` (`GAME-0001`–`GAME-0532`).
- Exact genome matches: none.
- Tied near matches: `GAME-0394` — LittleBigPlanet 2 (`4 / 25 = 0.160000`); `GAME-0399` — Ico (`4 / 25 = 0.160000`).
- Supported combination subsets: none.
- Scan date: 2026-11-17.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
| --- | --- | --- | --- |
| `GAME-0394` — LittleBigPlanet 2 | `ACT-341`, `INF-179`, `SYS-369`, `TIM-003` | Both use local affordances under live timing with checkpoint recovery. Sackboy actively swings, reels and releases a grappling hook to cross a platform route. Sissel transfers between prop cores in suspended time and uses live prop motions to reach interventions in a victim's timeline. | Tied near (`0.160000`) |
| `GAME-0399` — Ico | `ACT-049`, `ACT-341`, `INF-179`, `TIM-003` | Both operate reachable fixtures to help someone in a live scene. Ico scales the castle, moves a cage and escorts Yorda through a two-actor gate and to a couch. Sissel uses a corpse-anchored rewind and interrupts two hazards with object tricks in the scrapyard. | Tied near (`0.160000`) |

### Preserved research notes

- New genes: `ACT-729`, `ACT-730`, `SYS-1540`–`SYS-1543`,
  `CON-811`, `INF-517`, `OBJ-298`, `TIM-035`.
- Classification result: `New gene`.
- Evidence and reasoning: corpse rewind restores one authored starting
  state, while Ghost World freezes the current state and changes Sissel's
  occupied core. The checkpoint and final survival are distinct results.

## Taxonomy impact

- Registry changes: ten Active additions and six transfers.
- Taxonomy-change record: [TAXONOMY_CHANGE_280](../../../research/taxonomy-changes/TAXONOMY_CHANGE_280.md).

## Negative results

- The four-minute rewind does not establish freely scrubbing the
  recorded simulation to an arbitrary frame.
- Neither possession nor reaching a visible core proves its live action
  is available. The scene still advances only in the live mode.
- The duration of the first window and the clock effects of every
  individual prompted line are not inferred from one route.

## Delta summary

## New facts

- [Observation | Corroborated | High] Frozen traversal can move the spirit
  while a live trick changes the positions from which it can later transfer.
  The bicycle bell creates a recovery point but does not yet save Lynne.

## New genes

- [Observation | Corroborated | High] Ten additions in
  `TAXONOMY_CHANGE_280`.

## New combinations

- [Observation | Corroborated | High] No new combination proposed.

## Taxonomy changes

- [Observation | Corroborated | High] `TAXONOMY_CHANGE_280`.

## New questions

- What exact screen and input transitions consume the live allowance
  while the DS displays a thought prompt?

## Next recommended game

- [Hypothesis | Limited | Medium] Examine a bounded job in the released
  Xbox Series X|S *PowerWash Simulator 2* under Selection 042.
