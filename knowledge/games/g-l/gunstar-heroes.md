---
game_id: GAME-0560
slug: gunstar-heroes
game_title: Gunstar Heroes
analysis_status: reviewed
reviewed: 2026-11-19
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-048
    - ACT-161
    - ACT-202
    - ACT-295
    - ACT-341
    - ACT-611
    - ACT-759
    - ACT-763
    - ACT-764
  system:
    - SYS-036
    - SYS-045
    - SYS-051
    - SYS-215
    - SYS-369
    - SYS-578
    - SYS-755
    - SYS-915
    - SYS-1627
    - SYS-1628
    - SYS-1629
    - SYS-1630
  constraint:
    - CON-442
    - CON-825
  information:
    - INF-073
    - INF-119
    - INF-192
    - INF-235
    - INF-318
  objective:
    - OBJ-308
  time:
    - TIM-003
---

# Game: Gunstar Heroes

Use the canonical [vocabulary and signature rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
Weapon names, component count, button mapping, guardian bodies, vitality
amounts and the Ancient Ruins geometry are instance parameters.

## Analysis scope

- Version / ruleset: original fully released English North American Sega
  Genesis cartridge rules, 1993, one player, Normal, Free Shot, first stage
  Ancient Ruins / Pink's Stage. The US Genesis booklet is inspected through
  SEGA's official Mini manual archive; its hosting does not make the Mini
  wrapper the target. No owned cartridge, ROM, binary checksum, original
  controller, emulator execution or save is inspected. Game Gear, 3DS,
  Gunstar Super Heroes, fan hacks and compilation rewind/save states are distinct.
- Primary decision loop: directly move, jump and fight through the visible
  stage slice; choose shooting, bodily attacks, guard, opponent/prop throws or
  platform hanging as the current threat requires; obtain spatial supplies,
  retain up to two weapon components and choose a single or combined shot;
  manage Vitality while clearing required local encounters and reach the
  Pinky Roader defeat, gem and stage-selector handoff.
- Entry and exit: fresh one-player selection with Normal, Free Shot and Force
  as the sole starting component, Ancient Ruins selected first, then first
  ordinary control on its jungle ground. Include initial soldiers/drones and
  Phantom, Papaya Dance, the second approach and pyramid climb, Bravoo Man,
  collapsing summit and downhill section, forest claw/bees, last required
  soldiers, Pinky Roader, Blue Gem settlement and the remaining-stage selector.
  Stop before playing the next selected stage. Retrying a failed attempt via
  the ordinary Continue choice is included within this same stage packet.
- Reproducible parameterisation: original defaults A select, B fire/grab,
  C jump; one human; no password, cheat, extra controller, TAS, speed-run glitch
  or wrapper rewind. Start with 100 Vitality; this is not asserted to be an
  immutable maximum. Source-indexed replacement details and stage-clear
  vitality fields remain qualified rather than falsely native-reproduced.
- Included: direct horizontal/vertical traversal, live jumping/gravity,
  crouch and eligible platform hang/shimmy/pull-up/drop; Free Shot movement
  and aim with its contextual hanging behaviour; sliding/body attacks and
  wall-kick opportunity; compatible unarmed guard; grabs/directional throws
  of live opponents and inert skull bombs, including close-fire context;
  ordinary direct shots, autonomous hostile movement/attacks, breakable world
  objects and required local scrolling locks; manually claimed weapon/health
  objects, additional bird-dispenser output, two-component capacity, duplicate
  types, reversible single/pair selection and pair-specific firing behaviour;
  one Vitality pool, eligible healing, mandatory guardian health/recovery,
  stage-clear/gem/continuation settlement and unlimited chosen stage retry;
  local viewport, threats, carried/active icons, Vitality and named boss cues.
- Excluded: Fixed Shot as the initial control style, Blue-specific aerial
  techniques, two-player rejoin/half-health sharing and partner throwing,
  subsequent Mine cart, Seven Force, aircraft, Dice Palace, space flight,
  later boss rematches, complete campaign, competitive high-score optimisation,
  achievements, cheat codes, fan patches and later-edition convenience features.
  The visible score is retained as presentation; no score threshold is invented
  as a stage-clear or survival requirement.
- Potential scoped modules: initial Fixed Shot; two-player shared survival;
  Seven Force mine routing; Dice Palace; spacecraft; complete-campaign gem use.
- Direct-play status: not conducted. Inspected the official US booklet scans
  numbered printed pp. 4–13, including Genesis mapping, guarded pose, grabs,
  hanging, original setup, two-component combinations, vitality and Continue.
  Read the later official PC manual separately as corroboration, not original
  device execution. Inspected the first four public 320×180-cell storyboard
  sheets of Riptide Longplays' 56:32 Genesis-labelled recording, published
  16 December 2024, at ten-second sampling: stage start 01:27, Papaya Dance
  01:56, Bravoo Man 02:50, Pinky Roader 04:24 and next-stage start 05:26.
  These sparse stills corroborate the first-stage route/terminal, not the
  recording's unverified regional binary, difficulty option, uninterrupted
  input, failure/retry fields or exact damage. No media playback, audio,
  foreground window or focus interception was used.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `GH-001` | The original released Genesis target is one player, Normal and Free Shot; default hardware controls differ from PC mappings and some guide labels. | Observation | Corroborated | High | P1, P2, S1 |
| `GH-002` | Direct movement, crouch, eligible hanging, bodily attacks, close throws and the simultaneous fire/jump defensive pose remain available in this stage. | Observation | Corroborated | High | P1, S1, S4 |
| `GH-003` | Two retained components admit single or combined selection, including duplicates; pair selection changes behaviour without consuming the components. | Observation | Corroborated | High | P1, P2, S1, S4 |
| `GH-004` | Supplies require a separate crouch/fire acquisition; bird sources can release additional items after eligible attacks. | Observation | Corroborated | Medium | P1, P2, S1, S2, V1 |
| `GH-005` | Ancient Ruins includes both minibosses, the pyramid descent, forest hazards, local required locks and Pinky Roader. | Observation | Corroborated | High | S1, S2, V1 |
| `GH-006` | Bravoo Man's authored recovery can undo accumulated damage during the same live encounter. | Observation | Corroborated | Medium | S2, S5 |
| `GH-007` | One Vitality pool reaches a Continue decision at zero; unlimited selected retries return to the stage start rather than spending a finite life stock. | Observation | Corroborated | High | P1, S3, S5 |
| `GH-008` | Pinky Roader defeat settles Blue Gem/clear state and remaining-stage selection; independent routes document a twenty-point vitality improvement for continuation. | Observation | Corroborated | Medium | S1, S2, S6, V1 |
| `GH-009` | An indexed detailed replacement rule distinguishes single-selected replacement from combined-mode insertion; another guide's terse left/right sentence is internally inconsistent. | Observation | Conflicting | Medium | S4, S7 |
| `GH-010` | The original booklet's wording about food and later starting vitality is not a verified permanent maximum-health rule; the PC manual describes replenishment and the routes separately describe clear rewards. | Observation | Conflicting | Medium | P1, P2, S1, S2, S6 |

## Basic data

- Release / origin: developed by Treasure and published by SEGA for Mega Drive /
  Genesis in 1993; the approved packet is the original English North American
  Genesis rules, not the later PC or Mini wrapper. Exact day and binary parity
  are not inferred from a later recording.
- Platform or physical form: Sega Genesis, one ordinary three-button controller;
  structured target in the platform registry.
- Puzzle family: explicit element combination, physical body/prop manipulation
  and live system pressure. Genre alone does not establish a family.
- Primary sources:
  **[P1]** [SEGA's official original US booklet archive](https://manuals.sega.com/genesismini/manuals/gunstarheroes/index.html),
  printed pp. 4–13, inspected as static original page scans on 2026-11-19;
  **[P2]** [SEGA's later PC Classics manual](https://shared.fastly.steamstatic.com/store_item_assets/steam/apps/71117/manuals/07%20GH_PC_MG_EFIGS_US_v6.pdf),
  English play, item, HUD and weapon sections; PC wrapper/mappings are not
  substituted for Genesis, and its health wording is kept distinct.
- Secondary sources:
  **[S1]** [Shiryu's original-Genesis guide, 29 February 2000](https://gamefaqs.gamespot.com/genesis/563327-gunstar-heroes/faqs/6993),
  controls, pair behaviours, full Ancient Ruins and clear bonus;
  **[S2]** [Sebrex's independently authored route, 13 September 2015](https://www.vizzed.com/boards/thread.php?id=89765),
  Normal-and-up Papaya context, pyramid, recovery and forest/gem handoff;
  **[S3]** [Ken Horowitz's Sega-16 review, 26 July 2004](https://www.sega-16.com/2004/07/gunstar-heroes/),
  one-life stage-start unlimited Continue; its five-weapons typo and A+B
  guard mapping do not override the primary booklet's four bases and B+C;
  **[S4]** [sherv22's original-Genesis FAQ](https://gamefaqs.gamespot.com/genesis/563327-gunstar-heroes/faqs/2782),
  indexed control, replacement and retained-pair sections; full page fetch was
  restricted, so only inspected indexed extracts support these claims;
  **[S5]** [Therealpidge05's Hard-mode guide mirror](https://www.neoseeker.com/gunstar-heroes/faqs/91948-boss-hard.html),
  corroborating recovery/Continue only; harder damage, controls and patterns
  are not silently inherited into Normal;
  **[S6]** [Gameplay reference](https://strategywiki.org/wiki/Gunstar_Heroes/Gameplay),
  indexed Normal default and twenty-point clear reward; full page returned 403;
  **[S7]** [Spatvark's indexed control extracts](https://gamefaqs.gamespot.com/genesis/563327-gunstar-heroes/faqs/39389),
  full page restricted; its left/right replacement sentence remains conflicting;
  **[V1]** [Riptide Longplays' Genesis recording](https://www.youtube.com/watch?v=OSFKLw8w5nA),
  56:32, first 00:00–05:50 sampled statically, publication 16 December 2024.
- Claim IDs: `GH-001`–`GH-010`.

## Mechanical decomposition

### Action Genes

- Reused: ACT-008, direct movement/jump; ACT-048, inert bomb pickup/release;
  ACT-161, direct weapon shot; ACT-202, crouch; ACT-295, character-owned slide,
  body splash and eligible wall-kick attack; ACT-341, addressed pickup claim;
  ACT-611, eligible live opponent lift/directional release; ACT-759, automatic
  retained ledge state with directed shimmy, pull-up or release after an
  eligible up/jump or down/jump entry. No continuously held grip reserve.
- Added: ACT-763, live single/single/pair selection; ACT-764, equipment-free
  bodily guard. All ordinary shot effects remain SYS-215 parameters.
- Parameters: initial Free Shot/Force, A/B/C mapping, eight-direction context,
  ground/air/hanging state, close-target eligibility and selected component.
- Claim IDs: `GH-001`–`GH-004`.

### System Behaviour Genes

- Reused: SYS-036, physical jump/fall/support and thrown-object motion;
  SYS-045 and SYS-051, hostile locomotion/acquisition; SYS-215, live damage,
  attack/hit eligibility, defence, knockback, defeat and thrown-body contacts;
  SYS-578, one current Vitality pool and compatible restoration, without
  asserting that initial 100 equals a fixed cap; SYS-755, compatible breakage
  and post-guardian support removal; SYS-915, required local clearance releases
  forward progress without demanding all endless soldiers be exterminated;
  SYS-369, chosen stage-start retry after the zero-Vitality terminal.
- Added: SYS-1627, reversible two-component attack behaviour; SYS-1628,
  additional spatial dispenser output before its separate pickup; SYS-1629,
  clear/gem/continuation settlement; SYS-1630, live guardian recovery.
- Resolution order: read the current pose/selection; commit movement, fire,
  grab or defence; resolve physical and combat effects while enemies advance;
  apply eligible item claim; resolve local clearance or final stage settlement.
- Replacement qualification: S4 says single-selected pickup replaces that
  component; combined selection inserts the new left entry, moves the old
  left entry right and discards the old right entry. S7's sentence says
  pushing right while dropping left, which is inconsistent. Capacity and
  reversible selection are primary-confirmed; exact replacement permutations
  remain indexed, source-limited Medium, not a native state experiment.
- Vitality qualification: beginning at 100 is not a proven 100 cap; the
  original booklet's food/later-start wording is not promoted into a permanent
  maximum-stat gene. Clear reward is sourced separately, while exact future
  Continue carry fields, native caps and overflow are unverified.
- Claim IDs: `GH-003`–`GH-010`.

### Constraint Genes

- Reused: CON-442, actionable pose/recovery, mapping and target prerequisites
  gate the current command. A nearby throwable actor can change Fire's context;
  Free Shot does not imply that every hanging/guard state retains ground running.
- Added: CON-825, at most two retained components, duplicate base types allowed;
  selecting both does not create another physical inventory entry.
- Scarce strategic resources: current Vitality and two component entries.
  No finite ammunition, magazine reload, block reserve or life stock is invented.
- Claim IDs: `GH-002`, `GH-003`, `GH-007`, `GH-009`.

### Information Genes

- Reused: INF-073, current carried/selected icons including inactive flashing;
  INF-119, current personal Vitality and low-state warning; INF-192, locally
  revealed scrolling geometry; INF-235, nearby enemies, projectiles, pickups
  and effect/collision feedback; INF-318, mandatory guardian's health counter.
- Boss introductions name their attack repertoire; that is not an exact
  committed future-action preview. Green Bravoo parts show local active danger,
  not a promise that every other boss region is harmless.
- Current score remains visible presentation without an invented survival gate,
  new life threshold, complete route map or off-screen enemy count.
- Claim IDs: `GH-002`, `GH-003`, `GH-005`, `GH-006`.

### Objective Genes

- Added: OBJ-308, complete Ancient Ruins through final-guardian defeat and
  progression-gem/clear settlement at the remaining-stage selector.
- Success is not merely reaching Papaya Dance, Bravoo Man or Pinky Roader;
  the whole route and gem handoff remain inside the packet.
- Failure at zero Vitality opens unlimited chosen Continue or quit. Retry is
  stage-bound, not a finite extra-life replacement or a wrapper save-state.
- Claim IDs: `GH-007`, `GH-008`.

### Time Genes

- Reused: TIM-003, world motion and hostile attacks advance while movement,
  selection, shots, throws, pickups or guard can be committed.
- Pyramid descent, active hazards and guardian recovery put pressure on delay;
  menu pause does not become a discrete-turn combat rule or extra time gene.
- Claim IDs: `GH-002`, `GH-005`, `GH-006`.

## Reproducible transitions

| Before | Action | Resolution / source-limited prediction | What it establishes | Claim ID |
|---|---|---|---|---|
| Free Shot, Force and moving ground control | Hold Fire while moving | Body and shot action coexist where current pose permits | Initial style is not Fixed Shot | GH-001 |
| Two components retained, only one active | Cycle selection to both, fire, then cycle back | Declared combined behaviour fires; both components remain retained after selecting one | Composition is reversible, not ingredient consumption | GH-003 |
| Force plus Fire retained | Select both and fire | Exploding Fireball differs from either base attack | Pair identity changes behaviour, not only a universal damage multiplier | GH-003 |
| Two Fire components retained | Select the pair | Ultra Flamethrower remains valid despite duplicate types | Capacity is two entries, not one instance per type | GH-003 |
| Item on reachable ground | Walk over it, then use down + Fire | Mere proximity is not the complete claim; the contextual input acquires it | No automatic contact-collection inheritance | GH-004 |
| Item bird still available | Trigger contact/output and strike when eligible | Another spatial supply can be released and still needs acquisition | Output and inventory gain are different transitions | GH-004 |
| Eligible live opponent at close range | Grab and direct the throw | The carried actor is released into active combat space | Not an instantaneous abstract fighting throw | GH-002 |
| Throwable inert skull bomb nearby | Claim/catch and throw toward a target | Bomb returns to the live scene and its impact resolves | Object handling does not require switching to another controlled ally | GH-002 |
| Actionable character and compatible incoming attack | Request fire+jump defensive pose | Eligible attack is deflected or reduced; other attacks may still hurt | Bodily guard is not a shield, parry or full immunity | GH-002 |
| Eligible thin platform | Enter hanging state and direct movement/transfer | Retained attachment permits lateral travel or deliberate upward/downward exit | Local posture and clearance gate commands | GH-002 |
| Local required group still active | Try progressing, then defeat required actors | Locked route slice can release; bypassable recurring soldiers are not an all-stage quota | Reused local-clearance boundary | GH-005 |
| Bravoo Man damaged but active | Delay until its recovery move completes | Source-grounded recovery can restore accumulated lost vitality | A live recovery race differs from a fresh checkpoint | GH-006 |
| Vitality reaches zero | Choose ordinary Continue | Stage-start attempt returns without finite life debit; exact fields remain unmeasured | Unlimited chosen retry is not a life stock | GH-007 |
| Pinky Roader defeated after the complete route | Accept gem/clear settlement | Blue Gem and remaining-stage selector close this packet | Not the next stage or complete-campaign terminal | GH-008 |

## Strategic and experiential structure

- Local decision: choose the useful shot/pair, bodily attack, throw, guard or
  posture for the visible threat without sacrificing an important component.
- Medium-term planning: preserve Vitality and useful equipment across the full
  approach, both minibosses, descent and final machine encounter.
- Long-term structure: other selected stages and campaign gems are excluded
  after this first selector return; no later loadout or max-health model is inferred.
- Common heuristics: use pair behaviour deliberately, manually claim supplies,
  separate bypassable soldiers from required stops, and finish a recovering
  guardian before the opportunity closes.
- Failure attribution: local contact and health feedback are legible; indexed
  replacement details and unmeasured Continue fields remain explicit uncertainty.
- Player-trust factors: unlimited retry is not a guarantee of zero progress loss;
  no borrowed emulator conveniences or invulnerability promise is implied.
- Claim IDs: `GH-002`–`GH-010`.

## Replay and variation

- Authored route and required encounter order recur; equipment acquisitions,
  selected pairs, movement, damage and hostile timing can differ.
- Enemy/attack timings are not claimed to be a deterministic seeded simulation.
- The same optional supplies can support different pair choices and attacks.
- High-score/TAS play, Fixed Shot and two-player survival are separate modules,
  not inherited merely because this solo stage can be replayed.
- Claim IDs: `GH-002`–`GH-008`.

## Adjacent systems and history

- Contra Force uses a gauge and activation path for a current commando's
  capability. It does not imply retaining two weapon types and a reversible
  composed attack here, nor is its finite life stock inherited.
- Mega Man 2 returns to a selector with a named weapon grant. This packet
  retains a progression gem and continuation vitality instead.
- The Shadow of the Colossus style of held stamina climbing and an equipped
  shield guard are rejected transfers despite broadly similar input buttons.
- These are structural counterexamples, not an external novelty claim.
- Claim IDs: `GH-001`–`GH-010`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-048`, `ACT-161`, `ACT-202`, `ACT-295`, `ACT-341`, `ACT-611`, `ACT-759`, `ACT-763`, `ACT-764` | Instance parameters only |
| System Behaviour | `SYS-036`, `SYS-045`, `SYS-051`, `SYS-215`, `SYS-369`, `SYS-578`, `SYS-755`, `SYS-915`, `SYS-1627`, `SYS-1628`, `SYS-1629`, `SYS-1630` | Instance parameters only |
| Constraint | `CON-442`, `CON-825` | Instance parameters only |
| Information | `INF-073`, `INF-119`, `INF-192`, `INF-235`, `INF-318` | Instance parameters only |
| Objective | `OBJ-308` | Instance parameters only |
| Time | `TIM-003` | Instance parameters only |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `559` (`GAME-0001`–`GAME-0559`).
- Exact genome matches: none.
- Tied near matches: `GAME-0466` — Streets of Rage 2 (`14 / 38 = 0.368421`).
- Supported combination subsets: none.
- Scan date: 2026-11-19.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0466` — Streets of Rage 2 | `ACT-008`, `ACT-048`, `ACT-161`, `ACT-295`, `SYS-045`, `SYS-215`, `SYS-578`, `SYS-755`, `SYS-915`, `CON-442`, `INF-119`, `INF-192`, `INF-235`, `TIM-003` | Both packets combine direct embodied attacks, loose props, live health, local enemy clearance and a bounded scrolling view. Downtown uses depth lanes, automatic close holds, health-priced specials, section time and finite Fighters; Ancient Ruins instead has manually claimed two-component weapons, reversible pair fire, bodily guard, authored guardian recovery and unlimited chosen stage-start retry before gem settlement. | Tied near; `14 / 38 = 0.368421` |

### Preserved research notes

- New genes: eight additions; twenty-three unchanged definitions reused.
- Classification result: `New gene`.
- Evidence and reasoning: the shared live brawler core does not erase
  reversible composition, different survival resources or the selector terminal.

## Taxonomy impact

- Registry changes: eight Active additions; two Actions, four System Behaviours,
  one Constraint and one Objective. Earlier definitions and signatures unchanged.
- Taxonomy-change record: [TAXONOMY_CHANGE_306](../../../research/taxonomy-changes/TAXONOMY_CHANGE_306.md).
- Candidate terms affected: reversible paired weapon selection/composition,
  bodily guard, live supply output, guardian recovery and gem settlement.

## Negative results

- None as a separate record. Rejected transfers and source conflicts are
  documented here and in the taxonomy decision; no external absence is claimed.

## Delta summary

## New facts

- [Observation | Corroborated | High] Single/pair selection retains components;
  manual supplies and unlimited stage retry differ from a finite-life shooter
  model (`GH-003`, `GH-004`, `GH-007`).
- [Observation | Conflicting | Medium] Replacement permutations and the old
  booklet's later-start wording require explicit source qualification (`GH-009`, `GH-010`).

## New genes

- [Observation | Corroborated | High] ACT-763, ACT-764, SYS-1627, CON-825 and
  OBJ-308 isolate the newly admitted control, capacity and terminal boundaries.
- [Observation | Corroborated | Medium] SYS-1628–SYS-1630 isolate additional
  dispenser output, clear settlement and guardian recovery under stated limits.

## New combinations

- [Observation | Direct | High] None unless the canonical proper-subset scan
  proves support for a previously verified combination.

## Taxonomy changes

- [Observation | Direct | High] TAXONOMY_CHANGE_306 adds eight definitions;
  no merge, split, old signature rewrite or historical mutation.

## New questions

- Which exact Genesis input/state trace independently confirms the indexed
  single-versus-combined pickup replacement order and every Continue field?
- How do original regional builds and difficulty settings alter guardian
  recovery timing or continuation vitality without changing the core pair rule?

## Next recommended game

- [Hypothesis | Limited | High] Native Xbox Series X|S Psychonauts 2,
  GAME-0561 under approved Selection 045.
- Optimisation criterion: alternate retro run-and-gun with modern psychic
  traversal on another platform.
- Expected information gain: test a complete released psychic-adventure packet
  against the earlier Psychonauts record without inheriting its whole campaign.
- Backlog impact: seven approved units remain after accepted GAME-0560.

## Why this game

- [Hypothesis | Limited | High] The approved Genesis slot tests reversible
  attack composition and explicit spatial supply choices alongside live combat.
