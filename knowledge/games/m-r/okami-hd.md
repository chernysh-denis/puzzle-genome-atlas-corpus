---
game_id: GAME-0382
slug: okami-hd
game_title: Ōkami HD
analysis_status: reviewed
reviewed: 2026-09-24
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-161
    - ACT-341
    - ACT-523
  system:
    - SYS-215
    - SYS-578
    - SYS-755
    - SYS-1036
    - SYS-1037
    - SYS-1038
  constraint:
    - CON-349
    - CON-351
  information:
    - INF-119
    - INF-372
  objective:
    - OBJ-224
  time:
    - TIM-003
---

# Game: Ōkami HD

Use the canonical [vocabulary and signature rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
Amaterasu, Issun, the River of the Heavens, Nagi's sword, the early imps and
Kamiki's suspended fruit are route parameters, not universal gene names.

## Analysis scope

- Version / ruleset: Capcom's English-language 2017 PlayStation 4 Ōkami HD
  single-player base game, modelled with the publisher's original PlayStation
  2 rules booklet and two independent PS4 HD opening-route descriptions. The
  installed PS4 binary, patch number and controller session were not inspected;
  no remaster-specific rule alteration is asserted.
- Entry and exit: start at first ordinary control at the cursed Kamiki tree,
  before entering the opening passage. Stop when the player uses learned Power
  Slash to cut the suspended fruit's stalk and the village visibly changes
  from ruined to restored. The subsequent inspection of petrified villagers,
  Sunrise, side quests and route toward Hana Valley are outside this packet.
- Primary decision loop: move Amaterasu through the authored passage; inspect
  a damaged or blocked world object; complete a celestial constellation to
  learn a needed brush mark; open the brush view, draw the mark across the
  relevant world target and let the accepted effect repair a gap or cut an
  obstruction; cross the changed route; use the reflector and learned slash
  to survive the required imp encounters; repeat until the fruit can be cut.
- Included: direct running, jumping, wall-jumping and swimming; fruit and
  route-cue inspection; the first two constellation grants (Rejuvenation and
  Power Slash); the authored river and statue-sword repairs; the initial
  Power Slash boulder and log/gate removals; mandatory return-path imp fights;
  personal health and limited, gradually refilling brush ink; the terminal
  fruit cut and village-restoration event.
- Reproducible route: inspect the fruit, enter the light, traverse the River of
  the Heavens, follow Issun's bridge demonstration, fill Yomigami's missing
  star, draw Rejuvenation over the missing river and cross. In the Cave of Nagi,
  restore the statue's sword, complete Tachigami's constellation, then use
  Power Slash on the boulder and exit obstruction. Fight the required imps on
  the return, reach the cursed tree and slash its fruit stalk. Brush misses,
  movement timing, health and ink remaining are bounded attempt variables,
  not an asserted recorded trace.
- Positive terminal: the cut fruit falls and restores the village's landscape;
  the later villagers' separate petrified state is deliberately not counted
  as resolved.
- Failure and retry boundary: normal combat can deplete health. Capcom's
  booklet gives an Origin Mirror save and game-over continuation mechanism,
  but no exact save was performed here; this packet does not assert a specific
  checkpoint or retained state after death. An invalid stroke leaves the
  addressed route object unchanged and permits another eligible attempt once
  the ink condition allows it.
- Excluded: optional mirror saving, pots, treasure chests, yen, Astral Pouch,
  praise upgrades, side encounters, post-fruit Sunrise, village errands,
  Guardian Saplings, Bloom, Cherry Bomb, later brush powers and regions,
  boss fights, the whole Orochi campaign, trophies, loading-screen play,
  4:3 versus widescreen presentation and PS2/PC/Switch control differences.
- Potential scoped modules: a directly observed PS4 save/death/retry trace;
  Sunrise and post-fruit village awakening; the first Guardian Sapling
  restoration; later brush-technique economy and combat.
- Direct-play status: none. No PS4 install, disc, executable, save, controller
  trace, screenshot, video or audio was inspected or played. The route below
  is a source-bounded reconstruction, not a claimed playthrough.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `OK-001` | The 2017 PS4 Ōkami HD is Capcom's high-resolution edition of the Amaterasu game, with one-player support | Confirmed | Direct | High | P1 |
| `OK-002` | The original publisher booklet describes a dedicated brush view, drawn marks changing the world and a finite ink-pot gauge that refills gradually | Confirmed | Direct | High | P2 |
| `OK-003` | Rejuvenation fills missing parts of world objects, while Power Slash cuts eligible objects by a drawn line | Confirmed | Direct | High | P2 |
| `OK-004` | Completing Yomigami's missing constellation mark grants Rejuvenation, which repairs the missing heavenly river to permit crossing | Observation | Corroborated | High | S1, S2 |
| `OK-005` | Repairing the Nagi statue's sword leads to Tachigami's constellation and Power Slash; that technique removes the cave return barriers | Observation | Corroborated | High | S1, S2 |
| `OK-006` | Required return-path imps are fought with direct reflector attacks and Power Slash before the fruit can be cut | Observation | Corroborated | High | S1, S2, P2 |
| `OK-007` | Cutting the suspended fruit above Kamiki changes the village landscape from cursed to restored, but a later Sunrise branch addresses still-frozen villagers | Observation | Corroborated | High | S1, S2 |
| `OK-008` | No direct PS4 build or save was inspected; exact patch, ink costs and post-death save state remain unverified | Confirmed | Direct | High | R1 |

## Basic data

- Release / origin: Clover Studio's original 2006 game, published by Capcom;
  Capcom's PS4 Ōkami HD edition released 2017-12-12 in the US listing.
- Platform or physical form: English PS4 single-player product; exact update
  version uninspected. The original PS2 manual is general-rule evidence,
  corroborated for the opening path by PS4-specific written guides.
- Puzzle family: world topology and perspective; ordered dependency
  sequencing; real-time system pressure.
- Primary sources, accessed 2026-09-24:
  - **[P1]** [Capcom's PS4 Ōkami HD PlayStation product
    listing](https://store.playstation.com/en-us/product/UP0102-CUSA08418_00-OKAMIHD000000001),
    for edition, release, publisher and visual restoration premise.
  - **[P2]** [Capcom's original Ōkami instruction
    booklet](https://static.capcom.com/okami/manuals/PS2_Okami_Manual.pdf),
    pp. 8–17 and 24–25, for controls, brush screen, ink, Rejuvenation, Power
    Slash, health and save affordances. The PDF was locally text-inspected;
    PS2 button symbols are not transferred as PS4 controls.
- Independent PS4 route descriptions, accessed 2026-09-24:
  - **[S1]** [chris-williams's PS4 Ōkami HD opening
    route](https://gamefaqs.gamespot.com/ps4/221040-okami-hd/faqs/79107/kamiki-village),
    River of the Heavens, Cave of Nagi and first fruit cut.
  - **[S2]** [SubSane's PS4 Ōkami HD written
    guide](https://gamefaqs.gamespot.com/ps4/221040-okami-hd/faqs/76318),
    §3.1, independently confirming the two powers, return combat and fruit.
- **[R1]** Local source-review boundary: no executable or audiovisual media was
  inspected; written transitions are reconstructed rather than observed.
- Claim IDs: `OK-001`–`OK-008`.

## Mechanical decomposition

### Action Genes

- `ACT-008`: directly guide the wolf through the passage, across the restored
  river, into Nagi's cave and back toward Kamiki.
- `ACT-161`: aim the reflector's immediate strike at an imp; brush slash is
  separately represented by `ACT-523` and its interpretation.
- `ACT-341`: inspect the fruit and route cues as reachable authored objects.
- New `ACT-523`: draw world-addressed marks over a missing region or eligible
  cut target in the dedicated brush view.
- Claims: `OK-002`–`OK-007`.

### System Behaviour Genes

- `SYS-215`: hostile imps and directly commanded reflector attacks resolve
  while the ordinary world runs in real time.
- `SYS-578`: hostile damage reduces Amaterasu's continuous health reserve;
  this packet asserts no exact hit values or executed death trace.
- `SYS-755`: accepted cutting damage removes eligible rock, log or gate
  obstruction, changing collision on the return route.
- New `SYS-1036`: validate a drawn mark against the current learned technique
  and world target, then apply or reject its contextual operation.
- New `SYS-1037`: accepted Rejuvenation reconstructs missing authored river
  or sword geometry, making the route or next unlock available.
- New `SYS-1038`: finishing Yomigami's or Tachigami's constellation adds its
  corresponding brush technique to the learned set.
- Resolution order: the mark is submitted on release, ink legality and learned
  pattern/target are checked, the accepted object change occurs, and any linked
  traversal or constellation successor becomes available. Live encounter
  control resumes outside the brush view.
- Claims: `OK-002`–`OK-007`.

### Constraint Genes

- `CON-349`: the missing river and cave return cannot be passed by their
  intended route until the needed Rejuvenation or Power Slash is learned and
  applied at the relevant world locus.
- `CON-351`: an accepted brush effect requires enough of the shared bounded
  ink reserve and spends its declared cost; the manual says pots replenish
  gradually. Exact technique-specific costs are not claimed.
- Scarce state: available ink, health and access to acquired powers.
- Claims: `OK-002`, `OK-004`–`OK-006`.

### Information Genes

- `INF-119`: visible personal health and ink pots disclose whether the next
  active brush attempt is currently affordable.
- `INF-372`: nearby inspection prompts identify the fruit and addressable
  world objects; damaged river/sword geometry is visible before the mark.
- Claims: `OK-002`, `OK-004`–`OK-007`.

### Objective Genes

- New `OBJ-224`: acquire both opening brush powers, cross their authored
  gates and cut the suspended fruit to restore Kamiki's landscape.
- Claims: `OK-004`–`OK-007`.

### Time Genes

- `TIM-003`: movement and obligatory imp combat are live; opening the brush
  view changes the input channel for one drawn effect, not the overall packet
  into a discrete turn or a speed-run deadline.
- Claims: `OK-002`, `OK-006`.

## Reproducible transitions

| Before | Action | Deterministic or bounded resolution | Establishes | Claim |
|---|---|---|---|---|
| Cursed tree, fruit suspended | Inspect the fruit and enter the light | The fruit cannot yet be cut; the authored opening passage is entered | terminal object seen before prerequisite powers | `OK-007` |
| Issun has demonstrated a bridge repair; Yomigami star is missing | Fill the constellation's missing star | Rejuvenation joins the learned brush set | learned technique from a sky mark | `OK-004` |
| Heavenly river has an authored missing stretch | Draw a valid Rejuvenation stroke across the gap | The missing river segment returns and can be crossed | world-geometry repair | `OK-002`–`OK-004` |
| Nagi statue's sword is broken | Draw Rejuvenation over the missing sword | The sword returns and exposes the Tachigami constellation | repaired object opens a second power | `OK-005` |
| Tachigami constellation awaits completion | Fill its missing mark | Power Slash joins the learned set | ordered capability acquisition | `OK-005` |
| Boulder or return obstruction blocks the cave route | Draw a valid Power Slash line across it | The eligible solid object is cut and the route opens | contextual cut versus repair | `OK-003`, `OK-005` |
| Return-path imps are active | Move, strike with the reflector and use an eligible slash | Imp damage and defeat settle under live combat; health can be lost | mandatory encounter | `OK-006` |
| Brush ink is insufficient | Attempt another brush effect | The effect cannot resolve until the shared reserve replenishes | finite rechargeable input | `OK-002` |
| Fruit stalk is in brush view after return | Draw Power Slash across the stalk | The fruit falls and the cursed village landscape is restored | bounded positive terminal | `OK-007` |

## Strategic and experiential structure

- Local decision: identify whether a visible gap needs Rejuvenation or an
  intact obstruction needs Power Slash, then draw over the actual target.
- Medium-term planning: the first constellation leads to river crossing;
  repairing Nagi's sword reveals the second technique needed to return.
- Long-term structure: the fruit seen at entry remains the terminal object,
  but its stalk is actionable only after the intervening power sequence.
- Failure attribution: visible geometry, learned-power state and ink gauge
  distinguish a wrong mark or insufficient resource from a missing route.
- Player-trust limit: the PS4 transitions are corroborated from text, not
  presented as a recorded controller experiment.
- Claim IDs: `OK-002`–`OK-008`.

## Replay and variation

- The authored gate and power order do not randomise in this packet. Stroke
  attempts, optional detours, ink recovery and encounter damage may differ.
- Optional saving and pickups affect an individual run, but neither is used
  to define the positive fruit-restoration terminal.
- Claim IDs: `OK-002`–`OK-008`.

## Adjacent systems and history

- Ori and the Will of the Wisps also gates an authored route behind acquired
  abilities and live combat; Ōkami's admitted route uniquely uses marks drawn
  over damaged or cuttable world targets to alter the traversable world.
- The original PS2 booklet gives the brush contract, but PS2 control labels
  and the wider thirteen-technique inventory are not silently imported into
  the PS4 opening signature.
- Claim IDs: `OK-001`–`OK-007`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | ACT-008, ACT-161, ACT-341, ACT-523 | Movement, strike, inspect and draw |
| System Behaviour | SYS-215, SYS-578, SYS-755, SYS-1036, SYS-1037, SYS-1038 | Live combat, health, cut, interpret, repair and learn |
| Constraint | CON-349, CON-351 | Acquired capability and ink reserve |
| Information | INF-119, INF-372 | Personal gauge and contextual cue |
| Objective | OBJ-224 | Restore the cursed village |
| Time | TIM-003 | Live traversal and combat |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `381` (`GAME-0001`–`GAME-0381`).
- Exact genome matches: none.
- Tied near matches: `GAME-0344` — Prince of Persia: The Sands of Time (`9 / 24 = 0.375000`).
- Supported combination subsets: none.
- Scan date: 2026-09-24.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0344` Prince of Persia: The Sands of Time | `ACT-008`, `ACT-161`, `ACT-341`, `SYS-215`, `SYS-578`, `SYS-755`, `CON-351`, `INF-119`, `TIM-003` | Both directly traverse an authored route, strike enemies, remove breakable obstructions, expose personal resources and spend a bounded ability reserve under live combat. The Prince's opening is about platform traversal, Sand-Tank revival and Dagger acquisition; Ōkami instead interprets drawn marks over world objects, reconstructs missing river and sword geometry, learns two brush techniques from constellations and restores Kamiki through a fruit cut. Neither route transfers the other's terminal. | Near, `0.375000` |

### Preserved research notes

- New genes: ACT-523, SYS-1036, SYS-1037, SYS-1038, OBJ-224.
- Classification result: five additive source-scoped distinctions and reuse
  of route, combat, resource and information genes.
- Evidence and reasoning: the publisher's brush rules and two PS4 written
  routes bound the two acquired powers and the fruit restoration.

## Taxonomy impact

- Registry changes: five additive Active IDs; earlier signatures unchanged.
- Taxonomy-change record: TAXONOMY_CHANGE_121.
- Candidate terms affected: world-addressed brush marks, authored geometry
  restoration, constellation-earned technique, contextual stroke effect.

## Negative results

- No direct-play observation, exact PS4 update or post-death state is claimed.
- The Sunrise after the fruit and later Guardian Sapling restoration are not
  part of this opening terminal.

## Delta summary

## New facts

- [Confirmed | Direct | High] `OK-001`–`OK-003` establish the HD product and
  original publisher brush, ink and technique rules.
- [Observation | Corroborated | High] `OK-004`–`OK-007` establish the PS4
  opening's ordered route and fruit restoration.

## New genes

- [Observation | Corroborated | High] Five additive IDs separate a drawn
  world-addressed input, its contextual interpretation, geometry repair,
  technique acquisition and bounded village-restoration terminal.

## New combinations

- [Observation | Corroborated | High] No verified reusable combination is
  introduced by this single game's source-bounded packet.

## Taxonomy changes

- [Confirmed | Corroborated | High] TAXONOMY_CHANGE_121 adds five boundaries
  without revising an earlier signature.

## New questions

- Does direct PS4 play reveal a distinct brush-screen timing or ink-use rule
  that the original manual and written PS4 routes do not resolve?
- What exact state returns after death without an intervening Origin Mirror
  save on this PS4 route?

## Next recommended game

- [Hypothesis | Limited | Medium] GAME-0383 The Sims 2: Legacy Collection.
- Optimisation criterion: contrast authored brush-led restoration with a
  household's recurrent autonomy, needs and social decision loop.
- Expected information gain: distinguish household simulation from direct
  avatar/world rewriting without assuming later Ōkami abilities.
- Backlog impact: preserves the selected nine-game order.

## Why this game

- [Hypothesis | Limited | Medium] Ōkami's drawn world operations contrast
  clearly with the prior unit's firearm-and-checklist infiltration.
