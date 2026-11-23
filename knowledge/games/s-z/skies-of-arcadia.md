---
game_id: GAME-0535
slug: skies-of-arcadia
game_title: Skies of Arcadia
analysis_status: reviewed
reviewed: 2026-11-17
combination_ids: []
gene_ids:
  action:
    - ACT-019
    - ACT-131
    - ACT-140
    - ACT-732
  system:
    - SYS-362
    - SYS-578
    - SYS-1307
    - SYS-1546
    - SYS-1547
    - SYS-1548
  constraint:
    - CON-269
    - CON-756
    - CON-813
  information:
    - INF-119
    - INF-518
    - INF-519
  objective:
    - OBJ-029
  time:
    - TIM-033
---

# Game: Skies of Arcadia

Use the [canonical vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
Encounter position, hull capacity, Spirit and action prices are parameters.

## Analysis scope

- Version / ruleset: original North American English two-disc Dreamcast
  retail game, November 2000, Disc 1, standard controller. This is Sega's
  original release. Exact disc mastering and hardware timings were
  not observed.
- Structured analysis target: PLAT-DREAMCAST, one ordinary first fight
  against Baltor's Blackbeard before the visit to Valua. Keep the Little
  Jack's ordinary fitted main artillery; do not buy or install a new gun
  for the packet. Start with Vyse, Aika and Drachma. Pre-existing legal
  repair items and support spells are variable entry supplies.
- Entry: accept the merchant's escort at Sailors' Island, then travel
  east along the reef toward the South Dannel Strait until Baltor
  intercepts the Little Jack. Begin at the first Ship Battle command
  grid. The escort, detours and earlier encounters establish entry.
- Primary decision loop: inspect hull state, the shared Spirit budget,
  the three time slots and previewed threats and chances. Assign a
  command and an available slot to each character. Resolve the whole
  turn, accept the encounter's maneuver decision when offered, and
  replan after damage, recovery or changed attack windows.
- Positive exit: defeat the Blackbeard while the Little Jack survives,
  receive the battle result and return to the escort route. Stop before
  arriving at the strait and receiving the merchant's passport.
  Negative exit: destruction of the Little Jack gives Game Over.
- Included: personal commands within a common scheduled batch, hull
  health, ordinary gun fire, guard, Focus and the shared ledger, repair
  items or available support magic, risk bands and chance cues, the
  tactical branch, and victory or loss. Excluded: earlier party combat,
  ship/shop preparation, specialized cannons and delayed artillery
  outside the stock loadout, Crew recruitment orders, the later Harpoon
  Cannon, Blackbeard II, Legends, VMU minigames, cheats and later routes.
- Direct-play status: no Dreamcast or executable was run. Sega's manual
  and retail confirmation establish the original rules. Two Dreamcast
  play accounts and an English first-encounter still substantiate the
  scope. No video or audio was played. The exact original drop
  calculation and live choice text of every branch were not reproduced.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
| --- | --- | --- | --- | --- | --- |
| SOA-001 | Sega's original English North American Dreamcast release predates Legends. The first airship encounter against Baltor comes during the escort from Sailors' Island before Valua and before fitting the Harpoon Cannon. | Confirmed | Corroborated | High | P1, P2, S1, S2 |
| SOA-002 | Vyse, Aika and Drachma each assign one command and choose a distinct active column of the three-round turn. Assigning a column makes it unavailable to the other two. The system resolves the completed batch, not each selection as it is made. | Observation | Corroborated | High | P1, S2, S3, S5 |
| SOA-003 | Installed ordinary artillery and legal magic draw on shared Spirit. The live gauge distinguishes availability and proposed spend. Guard, Focus and items carry no Spirit charge. A cast also uses the acting character's MP. Focus and the ordinary turn boundary restore Spirit. | Observation | Corroborated | High | P1, S2, S3 |
| SOA-004 | The grid forecasts Green, Yellow and Red danger. A Chance marker is a separate indication of a favorable attack opportunity. Visible next-turn cues are provisional and cannot receive current commands. | Observation | Corroborated | High | P1, S3, S5 |
| SOA-005 | At the encounter's maneuver prompt, taking the route behind the Blackbeard changes the following turn's opportunities. Published Dreamcast routes agree on the advantage. An exact chance count for all branches is not asserted. | Observation | Corroborated | High | P1, S1, S2, S4 |
| SOA-006 | An ordinary main gun fires and attempts its hit in the selected round. Relative ship pose can deny a firing angle and accuracy can deny a hit. Guard reduces applicable incoming damage in its scheduled window. | Observation | Corroborated | High | P1, S3, S4 |
| SOA-007 | Both vessels expose hull state. A repair item or eligible recovery action restores the Little Jack's hull. Losing all hull health ends the fight in Game Over rather than resolving individual party HP. | Observation | Corroborated | High | P1, S2, S3 |
| SOA-008 | Beating the Blackbeard gives a battle reward and control for the onward escort. The Captain's Stripe and Bomb are reported drops. The passport is awarded at a later route event. The sources report different experience figures. | Observation | Corroborated | High | P1, S1, S2 |

## Basic data

- Release / origin: Overworks, Sega; original English North American
  Dreamcast release in November 2000.
- Families: tactical forecast and counterplay, and agent routing and
  coordination.
- Sources accessed 2026-11-17:
  - **P1** — [Sega's original US Dreamcast manual](https://segaretro.org/images/d/d5/SkiesofArcadia_DC_US_Manual.pdf),
    printed pages 18–25. This establishes the shared Spirit gauge, the
    battle result, character commands, targeting columns, artillery,
    the tactical branch and Game Over from total hull loss.
  - **P2** — [Sega's American Dreamcast release anniversary](https://social.sega.com/articles/how-time-flies-skies-of-arcadia-set-sail-for-american/),
    for platform, market and November 2000 retail identity.
  - **S1** — [Arrawnt's original Dreamcast walkthrough](https://gamefaqs.gamespot.com/dreamcast/197237-skies-of-arcadia/faqs/9935),
    Sailor's Island and Blackbeard entries, for escort trigger,
    behind-ship option, reported items and later passport.
  - **S2** — [Shotgunnova's Dreamcast walkthrough](https://gamefaqs.gamespot.com/dreamcast/197237-skies-of-arcadia/faqs/66931),
    North Mid Ocean and Valua sections. It distinguishes the escort
    reward from the battle and shows the Harpoon Cannon fitted later.
  - **S3** — [MPureka's release-era Dreamcast ship battle guide](https://gamefaqs.gamespot.com/dreamcast/197237-skies-of-arcadia/faqs/9618),
    sections 2 and 3, for empty column assignment, forecast, the
    separate next-turn grid, command resolution and effects.
  - **S4** — [Jaksiel's Dreamcast boss guide](https://gamefaqs.gamespot.com/dreamcast/197237-skies-of-arcadia/faqs/9942),
    for scheduled fire, Focus, defense cues and getting behind during
    the first Blackbeard fight.
  - **S5** — [English Blackbeard planning still](https://www.galaxus.it/en/page/remember-skies-of-arcadia-33791),
    corroborating three character rows and time columns, distinct
    Chance and danger marks, hull display, Spirit and personal MP.
- Claim IDs: SOA-001–SOA-008.

## Mechanical decomposition

### Action Genes

- Reuse `ACT-019`: select the active party member's legal action and
  its applicable vessel target.
- Reuse `ACT-131`: select and expend a carried repair item when one
  is available. It must occupy the selected character's command.
- Reuse `ACT-140`: commit a finite maneuver choice between turns,
  selecting the tactical route for the following plan.
- New `ACT-732`: move the current command to one available time
  column before locking it. This chooses the sequence across
  characters independently of which character is assigned first.
- Claim IDs: SOA-002, SOA-003, SOA-005, SOA-007.

### System Behaviour Genes

- Reuse `SYS-362`: victory records battle rewards before control
  returns to the escort flight. The later passage reward is distinct.
- Reuse `SYS-578`: cannon damage and compatible recovery update the
  same ship HP, and loss of the entire hull is terminal.
- Reuse `SYS-1307`: committing Guard spends the character's timing slot
  to reduce applicable incoming damage to the ship.
- New `SYS-1546`: costly commands share one prepared Spirit budget.
  Focus takes one actor slot and adds Spirit through resolution.
  Ordinary turn settlement adds further Spirit according to the
  participating party, while unspent Spirit carries into later plans.
- New `SYS-1547`: the authored maneuver changes the ships' relationship
  and alters danger or opportunity markings in the next plan. Choosing
  the approach behind the Blackbeard yields favourable opportunities.
- New `SYS-1548`: the ordinary gun attempts its hit within the assigned
  timing slot. Relative angle can suppress the shot even after its
  plan was legal, and an actual shot can still miss.
- Claim IDs: SOA-003, SOA-005–SOA-008.

### Constraint Genes

- Reuse `CON-269`: to assign fire or support magic, the action must
  be available with the current equipment, target and resources.
  Personal MP is an additional check for magic.
- Reuse `CON-756`: a party member gets one committed command for one
  whole allocation and execution cycle, called a turn in the manual.
- New `CON-813`: each time column can hold only one newly assigned
  allied command. Another character may still act in an unused column.
  This is separate from each member's own command limit.
- Claim IDs: SOA-002, SOA-003, SOA-006.

### Information Genes

- Reuse `INF-119`: the selected character's personal MP and condition
  are shown separately from the ship and shared reserve.
- New `INF-518`: reveal categorical threat and independent attack
  opportunity for timed slots. The next-turn forecast can change
  after the current plan or the maneuver branch.
- New `INF-519`: show shared available and assigned Spirit separately
  alongside vessel hull values so the full turn's proposed cost
  can be compared with damage and recovery needs.
- Claim IDs: SOA-002–SOA-005, SOA-007.

### Objective Genes

- Reuse `OBJ-029`: defeat the required Blackbeard without losing the
  Little Jack. Settle the battle result before continuing the route.
- Claim IDs: SOA-007, SOA-008.

### Time Genes

- Reuse `TIM-033`: complete all party assignments before automatic
  interleaved action begins. Inside this turn the player-selected
  columns set the positions of allied commands, with hostile actions
  occurring during resolution.
- Claim IDs: SOA-002, SOA-005, SOA-006.

## Reproducible transitions

| Before | Action or event | Bounded resolution | What it establishes | Claim ID |
| --- | --- | --- | --- | --- |
| Three current columns and three active characters | Set Vyse's fire in an available later column, then assign Aika and Drachma to the remaining two | The used column closes to other new commands. Nothing fires until the batch is complete. | Character selection order and execution order differ | SOA-002 |
| Available Spirit leaves little room after a planned gun command | Compare the gauge before and after the assignment. Commit Focus in a remaining column. | The gauge identifies the proposed charge. On resolution Focus restores Spirit, and the ordinary boundary can restore more. | Holding a free actor slot differs from having unassigned Spirit | SOA-003 |
| An upcoming current slot has a higher danger cue | Assign Guard there while putting fire or Focus in another slot | Defense occupies this slot and reduces eligible damage rather than attacking there | Danger is actionable without identifying the exact future damage | SOA-004, SOA-006 |
| The maneuver choice appears during the encounter | Choose to go behind the Blackbeard and inspect the next grid | The battle progresses to different attack opportunities | The maneuver changes scheduling opportunities rather than steering the ship live | SOA-005 |
| A favorable slot is available and the ship can afford ordinary fire | Schedule the main gun in that slot and let it resolve | A valid gun can attempt its hit in that slot. A bad angle may cause a lost shot, and legal opportunity alone does not settle damage. | A forecast is not guaranteed damage | SOA-004, SOA-006 |
| Little Jack has lost some hull health and a repair item is available | Commit a repair in a legal slot | The item restores ship HP when it resolves. Reducing the hull to zero instead gives Game Over. | Both risk and recovery affect the same ship resource | SOA-007 |
| The Blackbeard falls and the Little Jack survives | Continue through the results | Battle rewards are available and the escort route resumes | The passport is outside this terminal | SOA-008 |

## Strategic and experiential structure

This battle assigns crew to time rather than directly controlling the
airship. A paid shot needs both Spirit and a permitted timing slot. Guard
and Focus both use slots that would otherwise support offense. Choosing
the rear approach is a tactical way to change the next forecast. During
automatic resolution the risk markings inform the earlier assignment
but never replace the physical and resource checks.

## Replay and variation

- Hold the original Dreamcast disc, three actors and stock equipment
  constant. Compare the same attack assigned in earlier and later
  columns, and compare next-turn cues before and after the rear approach.
- Use a legal repair only if needed and available. Character levels,
  ship HP at entry, learned support spells, paid-action prices and
  exact damage are treated as parameters of a repeat.
- An exact strategy script, XP amount, equal-speed tie rule or later
  crew and torpedo scheduling is not asserted.
- Claim IDs: SOA-002–SOA-008.

## Adjacent systems and history

- The later Valuan escape installs a separate special cannon. Later
  battles introduce secondary sustained fire, torpedoes and Crew
  actions. None of those moves is required by the initial packet.
- GameCube Legends has distinct releases and content. No parity with
  its bounty or later encounter rules is assumed.
- Claim IDs: SOA-001, SOA-005, SOA-008.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
| --- | --- | --- |
| Action | `ACT-019`, `ACT-131`, `ACT-140`, `ACT-732` | command, carried repair, maneuver choice and slot |
| System Behaviour | `SYS-362`, `SYS-578`, `SYS-1307`, `SYS-1546`, `SYS-1547`, `SYS-1548` | reward, hull, Guard, shared Spirit, tactical branch and angle-limited fire |
| Constraint | `CON-269`, `CON-756`, `CON-813` | action eligibility, one actor command, unique column |
| Information | `INF-119`, `INF-518`, `INF-519` | personal MP, time risks and chances, hull and planned spend |
| Objective | `OBJ-029` | defeat the Blackbeard before hull loss |
| Time | `TIM-033` | complete planning followed by interleaved resolution |

Canonical signature:

`ACT-019,ACT-131,ACT-140,ACT-732; SYS-362,SYS-578,SYS-1307,SYS-1546,SYS-1547,SYS-1548; CON-269,CON-756,CON-813; INF-119,INF-518,INF-519; OBJ-029; TIM-033`

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `534` (`GAME-0001`–`GAME-0534`).
- Exact genome matches: none.
- Tied near matches: `GAME-0489` — Golden Sun (`9 / 27 = 0.333333`).
- Supported combination subsets: none.
- Scan date: 2026-11-17.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
| --- | --- | --- | --- |
| `GAME-0489` — Golden Sun | `ACT-019`, `ACT-131`, `CON-269`, `CON-756`, `INF-119`, `OBJ-029`, `SYS-1307`, `SYS-362`, `TIM-033` | Both assign one command per actor before automatic adversarial resolution. Golden Sun orders actors by agility and uses individual casting resources and Djinn in its attic battle. The Little Jack assigns allies to exclusive time slots, pays from shared Spirit and changes the next forecast by choosing a flight maneuver. | Tied near (`0.333333`) |

### Preserved research notes

- New genes: `ACT-732`, `SYS-1546`–`SYS-1548`, `CON-813`,
  `INF-518`, `INF-519`.
- Classification result: `New gene`.
- Evidence and reasoning: actor and time column constrain the same draft
  independently. The shared budget, column forecast and later branch
  evaluate the plan without treating those steps as a guaranteed attack.

## Taxonomy impact

- Registry changes: seven Active additions and eleven transfers.
- Taxonomy-change record: [TAXONOMY_CHANGE_282](../../../research/taxonomy-changes/TAXONOMY_CHANGE_282.md).

## Negative results

- A chance marker does not establish an extra command slot, guaranteed
  damage or an installed special cannon.
- A hull defeat is not the same as one actor's resource depletion.
- Sources agree on the post-battle drops in the scope but report
  different experience figures. No fixed experience amount is used.

## Delta summary

## New facts

- [Observation | Corroborated | High] A player assigns different crew
  commands to distinct ordered slots of the same turn. The rear
  maneuver changes the following opportunities through a separate input.

## New genes

- [Observation | Corroborated | High] Seven additions in
  `TAXONOMY_CHANGE_282`.

## New combinations

- [Observation | Corroborated | High] No new combination proposed.

## Taxonomy changes

- [Observation | Corroborated | High] `TAXONOMY_CHANGE_282`.

## New questions

- Which tactical cues remain fixed if the opposite opening branch
  is chosen under exactly the same gear and entry state?

## Next recommended game

- [Hypothesis | Limited | Medium] Evaluate a bounded live hacking
  encounter in the full PS5 release of *PRAGMATA* under Selection 042.
