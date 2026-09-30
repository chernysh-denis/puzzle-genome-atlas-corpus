---
game_id: GAME-0459
slug: daxter
game_title: Daxter
analysis_status: reviewed
reviewed: 2026-09-30
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-161
    - ACT-202
    - ACT-341
  system:
    - SYS-037
    - SYS-045
    - SYS-215
    - SYS-578
    - SYS-605
    - SYS-1056
    - SYS-1210
  constraint:
    - CON-175
    - CON-738
  information:
    - INF-119
    - INF-179
    - INF-441
  objective:
    - OBJ-261
  time:
    - TIM-003
---

# Game: Daxter

Use the canonical [vocabulary and signature](../../../docs/ARCHITECTURE.md#canonical-vocabulary). The ottsel, swatter, hotel, plants, Gold Gems and number 25 are parameters of reusable boundaries, not genre or carrier genes.

## Analysis scope

- Version / ruleset: Original 2006 PlayStation Portable Daxter, as documented by the original English UCES-00044/ANZ PSP booklet and two independent contemporary original-PSP routes. One first Westside Hotel extermination assignment, starting at its foyer after Osmo has supplied the basic electric swatter and the city tutorial, ending when the concierge accepts at least 25 collected Gold Gems, or when health reaches zero before that report. Include the foyer request, marked key and first elevator gate, direct running, jump/double jump and climb through the gardens and rooms, pond lily-pad crossings, crouched Ottsel Mode past hostile plants and through low passages, directly commanded swatter combat and the resulting physically collected Gems, bed-assisted height, slide traversal and obstacles, continuing health damage plus two-bar Health-Pack recovery, current-location Gem counter and required quota, return elevator and separate concierge report. The early swatter can be struck repeatedly in the documented basic combo; Dream Sequence advanced attacks are not granted at entry. Do not imply the mandatory street tutorial Gem is part of the hotel's location counter or that exactly 25 hotel enemies must die: the documented mission gate is the accepted Gold Gem count. The first slide has no reported obstacle; the later slide does. Optional Precursor Orbs, optional Combat Bug cage/cards/vials and the optional side routes do not alter this accepted mission and are outside the admitted genome. Later spray acquisition in the Construction Site, spray hover and flamethrower, vehicles, dreams, multiplayer Bug Combat, later assignments, modern PS4/PS5 enhancements, exploits and exact unmeasured hit, drop or respawn timing are excluded modules. No PSP software image or direct execution was inspected.
- Structured analysis target: `PLAT-PLAYSTATION-PORTABLE`, original booklet target in [platform coverage](../../platforms/games.json).
- Primary decision loop: inspect the next reachable room and local threats; move, jump, climb or crouch to keep access and health; strike eligible Metal Bugs with the starting swatter and touch their released Gold Gems; monitor the local proof count, then return by the elevator and report once the declared quota is met.
- Entry and exit: first hotel foyer entry after receiving the basic electric swatter. The city tutorial's pickup has happened, but its transfer into the hotel-local counter is not asserted. The ordinary health capacity starts at five bars in the manual; the exact current health at foyer entry is not measured. Positive exit is accepted concierge report with at least 25 Gems; negative exit is the first zero-health Game Over. No retry or post-report successor mission is included.
- Included: all causally necessary traversal, plant avoidance, swatter combat, physically collected proof, health, visible progress, hotel access and return-report mechanics for the bounded first assignment.
- Excluded: optional Orb completion, Bug Combat rewards, spray/hover/fire acquired later, advanced Dream attacks, unrelated city exploration, next assignments, save/reload, modern conversion and exact runtime constants. These exclusions do not claim the features are absent from the full game.
- Potential scoped modules: optional hotel collectibles and later return with hover, Construction Site spray introduction, first Dream Sequence, vehicle and Bug Combat modes, direct PSP attempt including failure recovery and edition comparison.
- Direct-play status: No UMD, PSP, emulator, ROM, input trace, save, gameplay video or game audio was opened or played. All twelve PDF leaves of the English UCES-00044/ANZ original manual were visually inspected; its controlling pages are PDF leaves 4–8. The archive names the file “Daxter (USA).pdf”, but the scanned cover and imprint identify UCES-00044/ANZ; that is the documented booklet identity, not proof of a US pressing or identical software revision. The two dated original-PSP routes were read independently. The artwork is a new interpretive illustration, not a captured frame.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| DA-001 | The inspected original English PSP booklet identifies UCES-00044/ANZ; no UMD revision or played region is established. | Observation | Direct | High | P1 cover/imprint, P2/P3 original PSP scope |
| DA-002 | The first hotel assignment requires 25 Gold Gems and a separate report to the concierge; a foyer key opens access to the garden route. | Observation | Corroborated | High | P2 first hotel, P3 first hotel |
| DA-003 | The default swatter attacks directly and repeated presses chain basic attacks; later advanced moves require Dream Sequences, and spray is obtained in the following Construction Site. | Observation | Corroborated | High | P1 PDF leaves 5–7, P3 first/second assignments |
| DA-004 | Running, jump/double jump, climbable grilles, lily pads, low-passage crawling, room beds and two slides connect the documented first route; the latter slide has obstacles. | Observation | Corroborated | High | P1 leaf 4 controls, P2/P3 first hotel |
| DA-005 | Crouched Ottsel Mode avoids the hotel plants' nearby attack, while upright proximity risks it; exact detection geometry is not measured. | Observation | Corroborated | High | P2/P3 garden routes |
| DA-006 | A defeated qualifying Metal Bug leaves a Gold Gem, and collecting it updates the current-location proof count; optional Orbs are a different collection. | Observation | Corroborated | High | P1 leaves 6–7, P2/P3 first hotel |
| DA-007 | A fresh Daxter has five Health Bars, damage removes bars, a Health Pack restores two, and zero health is Game Over; the precise foyer-entry current value is not measured. | Observation | Direct | High | P1 PDF leaves 6–7 |
| DA-008 | Manual HUD labels current-location Gem and health displays; dialogue/written routes state the quota, but an always-visible quota number in the HUD is not documented. | Observation | Corroborated | High | P1 leaf 6, P2/P3 first hotel |
| DA-009 | The mandatory route can finish without optional Combat Bug, Precursor Orb completion or later spray hover; first garden/room path returns by elevator to the concierge. | Observation | Corroborated | High | P2/P3 first hotel and next assignment, P1 leaves 7–8 |
| DA-010 | The dossier is source-only; no exact drop randomness, enemy count-to-gem identity, frame timing, checkpoint behaviour or ANZ/US software parity is measured. | Observation | Limited | High | Documentary method; P3 explicitly marks one health-drop impression uncertain |

## Basic data

- Release / origin: Ready at Dawn's original 2006 Daxter for PSP. The booklet is a Sony Computer Entertainment Europe UCES-00044/ANZ print target; it does not identify an inspected software revision.
- Platform or physical form: PlayStation Portable handheld game; archived manufacturer booklet and original-PSP first-hand route accounts, no executable observation.
- Mechanical families: FAM-010 because threats and avatar actions resolve live; FAM-013 because an addressed key, physical proof tokens and a named recipient condition access and settlement; FAM-017 because key, garden/rooms, return and report form a required authored order. Other fourteen boundaries were tested: no route construction, object packing, hidden-evidence deduction, programmable automation, tactic turn queue, world-topology editing or time reversal.
- Primary sources accessed 2026-09-30:
  - P1: [original Daxter PSP booklet scan](https://archive.org/download/SonyPSPManuals/Daxter%20%28USA%29.pdf), cover/imprint and all twelve PDF leaves visually inspected. The archive filename says USA, but the actual booklet says UCES-00044/ANZ. PDF leaves 4–8 establish default inputs, locked advanced attacks, swatter, five-bar health, two-bar packs, Gold Gems, local HUD counter, mission structure and excluded Bug Combat. Scanned screenshots and cover art were used as evidence only, never copied into the site.
  - P2: [Larry Imgrund, original PSP FAQ/Walkthrough](https://www.gamerevolution.com/guides/37168-daxter-faqwalkthrough), created 2006-03-20, updated 2006-06-22, hosted 2006-06-27; Haven City Streets and Westside Hotel sections. First-hand route observes concierge, key, garden, plants, pond, beds, slides and return.
  - P3: [_Akiro_, independent original PSP complete route](https://www.jeuxvideo.com/forums/1-10834-12808-1-0-1-0-solution-complete-de-daxter.htm), published 2008-11-05, first hotel and next Construction Site. It separately supplies the 25-Gem threshold, crouched plants, room route and later spray acquisition. Its names for an insect type are explicitly unofficial and are not adopted as canonical identities.
- Secondary sources: none needed for the admitted core. The present PS4/PS5 conversion's rewind and quick-save are edition additions outside this scope.
- Claim IDs: DA-001–DA-010.

## Mechanical decomposition

### Action Genes

`ACT-008` — Direct movement, jump/double jump and grating climb choose the next supported hotel route. Jump lily pad to lily pad rather than assume Daxter swims.

`ACT-161` — The equipped starting swatter is directly struck toward a reachable Metal Bug; repeated ordinary strikes form its basic combo. Defeat a bug before collecting its proof.

`ACT-202` — Triangle toggles Ottsel Mode, compacting the controlled body. Stay crouched near a plant or pass through a low doorway or vent.

`ACT-341` — A reachable authored person or fixture accepts a context action. Receive the concierge task, claim the marked key, use the enabled elevator, then report after the quota.

- Parameters and claim IDs: DA-002–DA-005; buttons, hotel geometry and swatter appearance are not separate genes.

### System Behaviour Genes

`SYS-037` — Touch a dropped Gold Gem to credit it; defeat alone does not perform the contact pickup.

`SYS-045` — Hotel Metal Bugs continue their local movement on the running clock while Daxter navigates or attacks.

`SYS-215` — Direct swatter contact and hostile attacks resolve by reach, cadence, damage and defeat in real time. Basic chained swats are a combat parameter, not a score multiplier.

`SYS-578` — Incoming hits lower one health pool and a Health Pack restores missing bars up to capacity. A pack adds two bars only when missing health permits.

`SYS-605` — The foyer key and authored access state admit the next hotel segment; room passage and return elevator follow the built route, not a freely chosen level jump. No unproved key-consumption rule is asserted.

`SYS-1056` — Contact with the eligible hotel bed launches Daxter higher toward an elevated platform or vent. It does not grant a permanent double-jump upgrade.

`SYS-1210` — A qualifying Metal Bug defeat creates a separate Gold Gem pickup; its proof value is credited on collection, not by merely swinging the swatter.

- Parameters and claim IDs: DA-002–DA-009; no spray, optional Orb or random Health-Pack generator is admitted.

### Constraint Genes

`CON-175` — Damage persists along the bounded route until a pack heals it; first zero health ends this attempt. A doorway is not an assumed full heal.

`CON-738` — A hotel plant can acquire an upright nearby Daxter, while maintained Ottsel Mode permits the same dangerous passage. The exact range is not inferred.

- Parameters and claim IDs: DA-005, DA-007; pond support and vent clearance are spatial parameters of movement and posture.

### Information Genes

`INF-119` — The HUD exposes current health bars before another risky fight or plant passage.

`INF-179` — The local view exposes immediate plants, Metal Bugs, platforms, grilles, beds, drops and accessible passages, not unseen later rooms.

`INF-441` — The concierge supplies the 25-Gem requirement and the HUD counts collected local Gold Gems, so return can be chosen with evidence. The quota need not appear permanently beside the HUD count.

- Parameters and claim IDs: DA-002, DA-004–DA-008.

### Objective Genes

`OBJ-261` — Collect at least 25 eligible Gold Gems and separately report them to the concierge after returning to the foyer. Crossing the numeric threshold alone does not end the assignment.

- Parameters and claim IDs: DA-002, DA-006, DA-009; 25 is a threshold, not a new gene.

### Time Genes

`TIM-003` — Direct attacks, moving bugs, plant responses and slide obstacles resolve on a live clock; menu pause or save behaviour is outside this bounded decision loop.

- Parameters and claim IDs: DA-003–DA-005; no overall hotel deadline is asserted.

## Reproducible transitions

| Before | Action | Deterministic or bounded resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Concierge contacted, hotel access key unclaimed | Take the marked key and approach the elevator gate | The first garden route becomes available | An addressed item precedes the authored segment | DA-002 |
| An upright Daxter nears the carnivorous plant | Toggle and maintain Ottsel Mode while passing | Its ordinary proximity attack is avoided in the documented passage | Posture, not merely speed, changes hostile eligibility | DA-005 |
| Daxter reaches the pond without swimming | Jump through its lily-pad supports | Reach the next bank if jumps land on support | Water is not an ordinary walkable edge | DA-004 |
| One eligible Metal Bug is alive | Repeatedly strike with the basic electric swatter | The bug can be defeated and a proof Gem appears | Default weapon, not later spray or Dream attack | DA-003, DA-006 |
| One Gold Gem is loose in the world | Touch the Gem | It is removed/credited and the local Gem counter updates | Defeat and proof collection are distinct | DA-006, DA-008 |
| Daxter has lost health but remains alive | Contact an available Health Pack | Restore at most two missing bars, capped by current capacity | Persistent attrition and bounded recovery | DA-007 |
| A bed lies below an elevated vent | Land or jump onto the bed | The elastic contact boosts Daxter toward the higher ledge | The bed is a traversal fixture, not furniture only | DA-004 |
| Local counter is below the accepted threshold | Return and speak to concierge | First assignment is not yet accepted | Defeat or partial proof cannot settle it | DA-002, DA-008 |
| At least 25 eligible Gold Gems have been collected | Return by the final elevator and report | The concierge accepts the first assignment | Threshold plus separate report is the terminal | DA-002, DA-009 |

## Strategic and experiential structure

The hotel asks for route choices under live enemy pressure: strike enough qualifying bugs to produce proof, collect what they leave, and avoid the plants with a deliberate posture change. Climbing, lily-pad jumps, bed launch and vents put this work into an authored return loop. The player can decide when enough proof has accumulated from the visible tally, but must still reach and speak to the concierge. Losing health on the way matters because only eligible packs replace lost bars. The fixed 25-Gem quota is less than the account of all available hotel Gems; clearing every optional bug or Orb is not the objective. Exact enemy AI, drop rolls, health-pack spawn chance and shortest route are not measured. DA-002–DA-010.

## Replay and variation

Keep the original PSP first-hotel scope, starter swatter and concierge threshold fixed. Safe route choices around some plants, optional fights, packs and collectibles can vary. The two contemporary routes agree on the required sequence but do not supply an exact software execution trace or prove every optional branch's persistence. No procedural hotel generation, universal Gem drop guarantee for every enemy class or independent difficulty scaling is inferred. DA-004–DA-010.

## Adjacent systems and history

The city tutorial supplies a swatter and shows a sample Gem before this bounded hotel entry, but the manual defines the Gem HUD as current-location count. The documentary sources do not establish whether the tutorial pickup is retained in the hotel's local quota, so the analysis requires the hotel display to reach its assigned 25 rather than claiming an exact starting value. The next Construction Site grants spray after the first hotel completion; hover, flame, refill and upgrades belong to later modules. Dream Sequence moves, Combat Bug cards/cages/vials, Orb unlock rewards and present-generation rewind/quick-save cannot be imported into this first attempt. DA-001–DA-010.

## Normalised genome

| Type | Active gene IDs | Parameters |
|---|---|---|
| action | `ACT-008`, `ACT-161`, `ACT-202`, `ACT-341` | direct hotel controls and fixture interactions |
| system | `SYS-037`, `SYS-045`, `SYS-215`, `SYS-578`, `SYS-605`, `SYS-1056`, `SYS-1210` | live combat, pickup, health and authored hotel state |
| constraint | `CON-175`, `CON-738` | attrition and plant posture |
| information | `INF-119`, `INF-179`, `INF-441` | health, local view and mission proof |
| objective | `OBJ-261` | 25 proof Gems and separate report |
| time | `TIM-003` | live traversal and combat |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `458` (`GAME-0001`–`GAME-0458`).
- Exact genome matches: none.
- Tied near matches: `GAME-0325` — The Legend of Zelda (`10 / 27 = 0.370370`).
- Supported combination subsets: none.
- Scan date: 2026-09-30.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0325` — The Legend of Zelda | Direct movement and attack, live hostiles, one persistent health pool, contact pickup, local view, ordered route state and live input | The NES packet uses sword/item choice, consuming keys, passive shield, map/compass and a guardian fragment; Daxter's hotel instead requires posture-sensitive plant passage, elastic-bed height, physical bug-proof drops, a local quota display and an addressed return report | Near match, `10 / 27 = 0.370370`; shared adventure traversal with different stealth, proof and completion decisions |

## Taxonomy impact

Four new boundaries in [TAXONOMY_CHANGE_196](../../../research/taxonomy-changes/TAXONOMY_CHANGE_196.md) and fourteen reviewed reuses. No earlier definition, game signature or verified combination is changed. A named salience review assigns all 18 uses without novelty weights.

## Negative results

- No `SYS-063`: the hotel key is documented as enabling access, but neither source proves that it is consumed at the gate. `ACT-341` and `SYS-605` represent the observed interaction and authored progression.
- No `SYS-574` magnetic attraction: the Gold Gem is collected by touch. No `SYS-1209` attack-method drop choice, `SYS-717` experience multiplier or special Dream attack in the first assignment.
- No `CON-077` directed vision cone or `SYS-057` pursuit: the plants have a posture-sensitive near-passage response, with no documented patrol, search or exact field angle.
- No `OBJ-242` distinct-creature capture, `OBJ-018` exhaust-every-token set or `OBJ-160` timed extraction transport: this is a proof threshold and addressed report.
- No new jump, bed, swatter, generic live combat or ordinary contact gene; existing `ACT-008`, `SYS-1056`, `ACT-161`, `SYS-215` and `SYS-037` own them.
- No unpublished ANZ/US parity, original disc play, drop probabilities, exact checkpoint reset, optional-Orb unlock branch or advanced spray in this signature.

## Delta summary

## New facts

- [Observation | Corroborated | High] The first hotel route combines key access, posture-based plant avoidance, swatter defeats, physically collected Gold Gems, bounce-and-climb traversal and a return report; DA-002–DA-009.

## New genes

- [Observation | Corroborated | High] Four generalisable boundaries: defeated-hostile proof drops, compact-posture hostile eligibility, local proof tally and threshold-plus-report terminal. No external novelty claim.

## New combinations

- [Observation | Corroborated | High] Complete proper-subset scan reviewed; no new combination proposed for a single carrier.

## Taxonomy changes

- [Observation | Corroborated | High] TAXONOMY_CHANGE_196; earlier definitions and signatures unchanged.

## New questions

- Can an observed original UCES-00044/ANZ UMD run resolve exact Gem locality at hotel entry, death/checkpoint retention, plant detection geometry and drop probabilities without importing later edition features?

## Next recommended game

- [Hypothesis | Limited | High] None is authorised after GAME-0459; the approved nine-game horizon ends here.
- Optimisation criterion: stop after acceptance and the 30-second window; new subject selection requires maintainer direction.
- Expected information gain: not assessed outside this horizon.
- Backlog impact: no next unit is reserved.

## Why this game

- [Hypothesis | Limited | Medium] The original PSP hotel adds posture-conditioned threat passage and a physical proof-and-report objective to the approved cross-platform batch without treating its later spray, dream or vehicle systems as a generic platformer genome.
