---
game_id: GAME-0616
slug: silent-bomber
game_title: Silent Bomber
analysis_status: reviewed
reviewed: 2026-11-21
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-223
    - ACT-817
    - ACT-818
  system:
    - SYS-037
    - SYS-799
    - SYS-1811
    - SYS-1812
    - SYS-1813
  constraint:
    - CON-767
    - CON-842
    - CON-857
  information:
    - INF-179
    - INF-318
    - INF-575
  objective:
    - OBJ-154
  time:
    - TIM-003
---

# Game: Silent Bomber

This analysis uses the [canonical vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
Buttons, target counts, ship geometry and individual combat values are instances.

## Analysis scope

- Version / ruleset: commercial English North American PlayStation
  disc SLUS-00902, published by Bandai America in 2000. Release
  references disagree on the exact North American day. The primary
  recording identifies an NTSC release and gives a US release date.
  The second shows the same English mission, but does not establish
  its region or the exact disc image. No capture hardware or hash has
  been independently verified.
- Primary decision loop: move through the deck to address required
  batteries. Set ordinary charges locally or with Lock On, then
  command their resolution separately. Concentrate charges at one
  position or use distinct sites. Clear linked barriers, and use
  compatible pickups and the visible enemy states to choose the next
  placement. Defeat the four-legged guardian, follow the exit marker
  and cross into the scored result.
- Entry: the Mission 01 briefing to destroy the anti-aircraft
  batteries, after the opening narrative and any optional training.
- Exit: the Mission Clear report after reaching the marked exit,
  with score, life bonus, time bonus and total before the next mission.
  The last marked battery and the guardian defeat are intermediate
  results.
- Included: ordinary placement, held targeting, waiting charges,
  manual trigger, stacking, linked local barriers, basic evasion,
  the required target tally, special liquid selection and spending
  evidenced in this mission, the shield state and the evacuation
  report. E-Chip pickup is included as a collectible. Spending in
  the E-Unit menu is not required by the boundary.
- Excluded: optional tutorial and its story, later missions, VR Arena,
  other regions and reissues, detailed score ranking, reload practice,
  exact damage curves, clipping or other route optimisations. The
  presence of Gravity in the booklet does not verify its use here.
- Suggested later scope: a mission that requires deliberate changes
  to E-Unit aspects between a settled result and the next entry.

## Direct-play status

No direct play was performed. The North American Bandai booklet
supplies the default controls and the first guardian's shield rule.
The commercial disc identity is separately documented. The NTSC
longplay presents the briefing, playable action, passage to the
guardian, physical evacuation and results. A second English trace
corroborates the path without authenticating that disc region.
The author of a separate US run records ordinary and material
choices in Mission 01. Exact binaries and controller settings are
unverified. Written sources and still frames were inspected with
no video or audio playback.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
| --- | --- | --- | --- | --- | --- |
| SBOM-001 | The commercial target is the English SLUS-00902 release from Bandai America. Mission 01 begins with the anti-aircraft battery assignment. | Confirmed | Corroborated | High | P1, M1, M2, W1 12:00, W2 7:10. The Japanese developer page establishes a separate earlier edition. |
| SBOM-002 | Press Square to set an ordinary charge locally. Held Square acquires an eligible remotely addressed target and release places a charge. Triangle separately begins resolution. Eligible target visibility and range can affect acquisition. | Observation | Corroborated | High | P1 pp. 4, 16–17 and 20; W1 14:00 and 16:50; W2 9:10–9:20 and 11:10. Exact button timing and targeting bounds are not measured. |
| SBOM-003 | Ordinary deployed charges occupy an E-Unit capacity. The separate trigger resolves pending charges, including stronger co-located stacks and an ordered sequence of distinct groups. Resolving them frees occupied capacity. | Observation | Corroborated | High | P1 pp. 13, 16–17 and 20; W1 14:40–15:00; S1 Mission 1 notes. Frame sampling does not establish propagation delays. |
| SBOM-004 | Pickups include E-Chips and material liquids. Napalm and Paralysis can affect this mission through different placed effects. Material stock and the selected type are visible, and consumption of a material use is distinct from occupancy of ordinary charge capacity. | Observation | Corroborated | High | P1 pp. 18–21; W1 12:10, 13:10 and 17:00–17:20; S1 Mission 1. Gravity use is unverified here. |
| SBOM-005 | The live display marks required fixtures and counts progress against eleven. Destroying the linked emitter clears a laser barrier during incomplete target progress. Resolving the required set leads to the four-legged weapon encounter. | Observation | Corroborated | High | P1 p. 22; W1 12:20, 14:00, 15:50–16:40; W2 9:10–9:30, 10:20–11:00; S2 Mission 01. The exact credit for every visible turret and spawn is not assumed. |
| SBOM-006 | The guardian has a dedicated vitality display. After sufficient damage it gains a visible shielded attack and is temporarily immune while that shield is active. Its defeat leads to evacuation rather than settling the mission directly. | Observation | Corroborated | High | P1 pp. 22 and 26; W1 16:40–17:50, W2 11:00–14:00, S2 Mission 01. No exact health threshold or frame duration is asserted. |
| SBOM-007 | After defeating the guardian, follow the newly displayed exit direction and distance to the exit. Both recordings reach Mission Clear with the score, life and time contributions before any new briefing. | Observation | Corroborated | High | P1 pp. 22–23; W1 17:30–18:00; W2 13:40–14:10. Points and time bonuses differ between traces. |
| SBOM-008 | Movement and contact choices continue in real time during placement decisions and hostile attacks. Jump and airborne Burst Jump provide evasive movement in the default controls. | Observation | Corroborated | High | P1 pp. 13–15; W1 15:10–15:50 and 17:00–17:20; W2 11:30–13:30; S2. No frame-level invulnerability or fixed total countdown is claimed. |

## Basic data

- Origin: CyberConnect, published in North America by Bandai America.
  The developer's current site uses the CyberConnect2 name.
- Analysis target: `PLAT-PLAYSTATION`, commercial English disc
  SLUS-00902, Mission 01 briefing through Mission Clear.
- Mechanical families: `FAM-009`, for positioning and choosing
  release against a changing protective response, and `FAM-010`,
  for committing these actions while hostile movement continues.
  Cuphead independently illustrates both boundaries.
- Sources checked 21 November 2026.
- P1: [Bandai America retail instruction booklet](https://www.videogamemanual.com/ps1/Silent%20Bomber%20%28USA%29.pdf),
  scan of the English PlayStation manual, especially pp. 13–23 and 26.
- P2: [CyberConnect2 title page](https://www.cc2.co.jp/silentbomber/).
  Primary developer identity and original Japanese product context,
  separately listing the later Japanese digital offering.
- M1: [PSX DataCenter SLUS-00902 catalogue](https://psxdatacenter.com/games/SLUS-00902.html),
  commercial North American disc identifier and packaging.
- M2: [Title Screen release identification](https://titlescreen.org/release/re9nw458/silent-bomber),
  US commercial CD and independently identified disc entry.
- W1: [LongplayArchive NTSC trace, played by nikodem123asdf](https://www.youtube.com/watch?v=A6h2cyGwvr8&t=716s).
  Mission 01 at 11:56. The assignment is visible at 12:00,
  the initial counter at 12:20, the target and reticle at 14:00,
  the new arena at 16:20, the guardian and changing protection at
  16:40–17:20, the Exit cue at 17:50 and Mission Clear at 18:00.
- W2: [Alexandre Barbieri English trace](https://www.youtube.com/watch?v=tcjxKVEYuVA&t=425s).
  Mission 1 starts at 7:05. The beam barrier is visible at 9:10–9:20.
  At 9:30 the player is farther along the deck. The guardian appears
  at 10:50, its green shield is visible at 12:00 and 13:20, and
  the exit cue at 14:00 precedes Mission Clear at 14:10.
- S1: [burningsteel's US run notes](https://speeddemosarchive.com/SilentBomber.html).
  The author explicitly identifies the US version and describes the
  Mission 1 Napalm and Paralysis uses separately from tutorial skipping.
- S2: [BJange's walkthrough, section 0802](https://gamefaqs.gamespot.com/ps/198640-silent-bomber/faqs/10592).
  Corroborates targeting the linked barrier emitter and the temporary
  protective attack, without identifying the retail carrier precisely.

## Mechanical decomposition

### Action Genes

- ACT-008: guide Jutah through the current deck, into range of
  viable targets and later toward the evacuation exit.
- ACT-223: choose when to jump or Burst Jump to evade incoming
  attacks while the guardian continues its own action.
- ACT-817: use Square for local placement or hold it to acquire a
  viable target and release it to set a charge there.
- ACT-818: independently choose when to trigger pending charges.
- Claim IDs: SBOM-002, SBOM-007, SBOM-008.

### System Behaviour Genes

- SYS-037: contact with a pickup such as an E-Chip credits it
  without settling the mission.
- SYS-799: sufficient damage advances the same guardian to a
  phase with a shielded attack. Exact phase threshold is unverified.
- SYS-1811: stacks increase local effect, while distinct groups
  can resolve in placement order from the same command.
- SYS-1812: separate liquid stocks support different effects under
  the shared command. Napalm leaves fire, Paralysis affects machines.
- SYS-1813: resolving a hit on the linked fixture can remove a
  local beam barrier before the whole target set is resolved.
- Claim IDs: SBOM-003–SBOM-006.

### Constraint Genes

- CON-767: a target part must intersect the current attack
  range for ordinary Lock On. Visibility alone is insufficient.
- CON-842: pending ordinary placements consume a concurrent
  owner capacity until they resolve.
- CON-857: the guardian's active visible shield blocks its
  vitality loss, so timing the separate trigger matters.
- Claim IDs: SBOM-002, SBOM-003, SBOM-006.

### Information Genes

- INF-179: read the live local routes, pickups and hostile motion,
  then use the exit direction and distance when available.
- INF-318: a separate vitality bar tracks the live guardian's
  health. It does not identify every future attack.
- INF-575: visible required fixtures carry a label, and the
  counter exposes resolved targets against the required total.
- Claim IDs: SBOM-005–SBOM-008.

### Objective Genes

- OBJ-154: clear the declared finite set and the mandatory
  guardian, then physically evacuate and observe scored Mission Clear.
- Claim IDs: SBOM-005–SBOM-007.

### Time Genes

- TIM-003: position and commit each reactive placement, evade,
  or issue the trigger during the changing live field.
- Claim IDs: SBOM-002, SBOM-006, SBOM-008.

## Reproducible transitions

| Before | Action | Resolution | What it establishes | Claim ID |
| --- | --- | --- | --- | --- |
| The first mission is briefed | Enter the deck | The live tally starts at zero against eleven and required objects are marked as they come into view | The mission contains a finite set apart from ambient threats | SBOM-001, SBOM-005 |
| An ordinary placement slot is free | Press Square locally or acquire a valid target and release Square | A charge is pending at the selected place; occupied capacity is visible | Placement and trigger are separately controllable | SBOM-002, SBOM-003 |
| Ordinary charges are pending | Give the single Triangle command | They resolve; additional charges at a site affect the group, and different sites can resolve in order | Stack and sequence vary without a separate trigger per group | SBOM-003 |
| A source releases an eligible pickup | Move into it | The pickup is collected during live control; selected material can then be spent separately | Collectible acquisition differs from placement and resolution | SBOM-004 |
| A linked laser barrier still blocks the deck | Resolve a charge at its emitter | The barrier clears while other targets remain | A local obstacle gate is separate from total mission credit | SBOM-005 |
| Required batteries have been resolved | Enter and fight the four-legged weapon | A dedicated health bar and the protected attack distinguish progress from eligibility to damage | A visible shield interval can change the decision to trigger | SBOM-006 |
| The weapon is defeated and the exit cue is shown | Move to the evacuation exit | Mission Clear displays score, life bonus, time bonus and total | A complete result requires evacuation after the combat | SBOM-007 |

## Strategic and experiential structure

The core choice is where to set pending effects and when to release
them. Concentrating placement can strengthen one local resolution,
whereas branching across fixtures spreads the same trigger. Evasive
movement remains available while the pending effects wait. At the
guardian, when it raises the shield becomes consequential for the
trigger. The two displayed scoring outcomes follow a real exit.
SBOM-002–SBOM-008.

## Replay and variation

The NTSC trace and the independent English trace take different
times and reach different Mission Clear totals. The US run notes
provide a third approach that consumes selected liquids for speed.
None of those outcomes establishes exact timings, all route orders,
the minimum amount of required liquid, a rank threshold or a saved
state after power-off. The region is specified for the analysed
disc, with the second capture only corroborating the English route.

## Adjacent systems and history

The optional tutorial teaches equipment separately. Later missions,
all tune-up allocation branches and the distinct VR Arena mode can
change the decision loop. The commercial Japanese date is not a date
claim about the selected North American disc.

## Normalised genome

| Type | Stable genes | Role |
| --- | --- | --- |
| Action | ACT-008, ACT-223, ACT-817, ACT-818 | Move, evade, set the pending effect and choose when to trigger |
| System Behaviour | SYS-037, SYS-799, SYS-1811, SYS-1812, SYS-1813 | Collect, phase, resolve charge groups and types, and open a linked local barrier |
| Constraint | CON-767, CON-842, CON-857 | Require range, current capacity and a vulnerable shield state |
| Information | INF-179, INF-318, INF-575 | Read local state, guardian vitality and marked target progress |
| Objective | OBJ-154 | Clear the set and guardian, then physically evacuate to the scored result |
| Time | TIM-003 | Act while the live field continues |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `615` (`GAME-0001`–`GAME-0615`).
- Exact genome matches: none.
- Tied near matches: `GAME-0584` — Saturn Bomberman (`5 / 27 = 0.185185`).
- Supported combination subsets: none.
- Scan date: 2026-11-21.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
| --- | --- | --- | --- |
| [Saturn Bomberman (GAME-0584)](saturn-bomberman.md) | ACT-008, CON-842, INF-179, SYS-037, TIM-003 | Both use real-time positioning, collectible acquisition and an owner cap on outstanding placements. Saturn Bomberman resolves fused straight-line blasts on a grid during a competitive battle. Silent Bomber can place on acquired targets and separately trigger its pending charges to clear the mission and evacuate. | Near, `0.185185` |

## Taxonomy impact

- [TAXONOMY_CHANGE_362](../../../research/taxonomy-changes/TAXONOMY_CHANGE_362.md)
  separates placement, manual resolution, discharge grouping, liquid
  effects, a linked barrier, temporary damage eligibility and progress
  cues.

## Negative results

- ACT-270 and SYS-470 require a fuse. No automatic fuse is assigned
  to the ordinary charge sequence here.
- ACT-691 releases a multi-target volley from the held acquisition
  input itself. Here release places a pending effect and a different
  command starts resolution.
- SYS-1045 represents blocked cardinal blast rays. The Stack and
  Chain descriptions in this mission do not assert that geometry.
- INF-441 exposes collected physical proof. The Mission 01 display
  directly counts resolved marked targets.
- An ordinary hostile, the linked barrier and the guardian are not
  credited as the same type of mission event. Their appearance does
  not justify treating the encounter as cleared before evacuation.

## Delta summary

## New facts

- [Observation | Corroborated | High] The game separates ordinary
  placement and the shared trigger. SBOM-002, SBOM-003.
- [Observation | Corroborated | High] A temporary shield alters
  damage eligibility during the guardian encounter. SBOM-006.
- [Observation | Corroborated | High] Both paths lead beyond the
  defeated guardian to a scored Mission Clear. SBOM-007.

## New genes

- [Observation | Corroborated | Medium] ACT-817, ACT-818,
  SYS-1811, SYS-1812, SYS-1813, CON-857 and INF-575.

## New combinations

- [Observation | Direct | High] No new combination admitted.

## Taxonomy changes

- [Observation | Corroborated | High] TAXONOMY_CHANGE_362.

## New questions

- What is the exact acquisition boundary near a moving target limb?
- Which allocated E-Unit changes can be observed during one unbroken
  North American Mission 01 run?
- What conditions distinguish carried stocks from sources after Continue?

## Next recommended game

- [Hypothesis | Limited | Medium] `GAME-0617`, Strange Antiquities,
  original Nintendo Switch. Trace one complete early object request.

## Why this game

- [Hypothesis | Limited | Medium] Both scopes separate recognising an
  eligible target and committing the addressed operation. The next
  game can isolate what changes when that eligibility is inferred
  from a client's evidence rather than live spatial targeting.
