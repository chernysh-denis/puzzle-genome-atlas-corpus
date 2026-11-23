---
game_id: GAME-0581
slug: hardspace-shipbreaker
game_title: "Hardspace: Shipbreaker"
analysis_status: reviewed
reviewed: 2026-11-20
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-048
    - ACT-341
    - ACT-785
  system:
    - SYS-1708
    - SYS-1709
    - SYS-1710
    - SYS-1711
    - SYS-1712
    - SYS-1713
    - SYS-1714
  constraint:
    - CON-060
    - CON-556
  information:
    - INF-119
    - INF-271
    - INF-551
    - INF-552
  objective:
    - OBJ-002
  time:
    - TIM-003
---

# Game: Hardspace: Shipbreaker

Use the [canonical vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
Keep the parts intact while freeing them from the hull, send each material
to its receiver, and see how much of the ship the shift recovers.

## Analysis scope

- Version / ruleset: English Xbox Series X|S commercial console release
  of 20 September 2022, US Xbox product `9ND8C4314ZZG`. Standard
  Career with oxygen consumption and the introductory training enabled.
  No specific installed patch, exact certification payout or frame timing
  is asserted.
- Structured analysis target: PLAT-XBOX-SERIES.
  See [platform coverage](../../platforms/games.json).
- Entry: one early unpressurised Mackerel training salvage order after the
  introductory tool and receiver lessons. Start with the hull still in
  the bay and the cutting tool, grapple, scanner, thrusters and HAB access.
  The launch-day Windows corroboration identifies its sample as the
  second training shift, a Hazard 0 Station Hopper. Exact seeded layout
  parity between captures is unverified.
- Primary decision loop: brake and inspect the structure. Find a cut
  point that can be safely reached without sacrificing valuable material.
  Melt the required links, move the released object through clearance,
  and select its receiver by the current salvage designation. Watch the
  pace of oxygen use, accumulated cutter heat, and progress toward the
  ship's salvage goals. Buy supplies at the outside kiosk when needed.
- Positive exit: settle the work interval at the habitation module,
  with a shift report showing what was recovered and lost. The player's
  performance goal is to reach the highest achievable recovery milestone
  for that hull. Exact final proportions and 100% material recovery are
  unverified. A single shift need not discard the ship or exhaust all
  remaining work.
- Negative exit: processing the wrong material in a consuming receiver
  or destroying a valuable part lowers the available recovery. Depleted
  oxygen, collisions and fire can cause death. The Xbox capture shows
  replacement during the wider segment, but insurance fees, reset rules
  for consumables and exact cut-piece persistence after death are
  outside this reconstruction.
- Included: one bounded cut–move–route–settle cycle, real-time drift,
  scanner and target readout, point cuts, physical detachment, grapple,
  salvage classes, oxygen and heat, and received versus lost value.
- Excluded: quote amounts, exact thresholds for other grades, optional
  tethers and area cuts, pressurised hulls, reactor dismantling, later
  equipment, company debt as a campaign goal, Free Play, R.A.C.E.,
  Open Shift, Early Access, PS5 and Windows as targets.
- Potential scoped modules: a pressurised salvage order with explicitly
  identified atmosphere controls, or a later two-stage reactor.
- Direct-play status: not conducted. Xbox and publisher material
  establishes release scope and first-ship rules. Background storyboard
  stills of an attributed Series S capture corroborate the tool and bay
  interactions through shift reporting. Dated launch-version Windows
  storyboard stills and a written account corroborate training, receiver
  categories and settlement, with the platform difference retained.
  No installed game, audio, video playback or controlled input trace
  was used.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
| --- | --- | --- | --- | --- | --- |
| HS-001 | The commercial Xbox Series X and S release arrived on 20 September 2022; the Series product is distinct from the Windows version. The first salvage orders use the small Mackerel. | Confirmed | Direct | High | P1, P2, P3 |
| HS-002 | Translational thrust changes velocity in free space. Release leaves drift and active braking slows it. Orientation, clearance and collision still matter while the player works. | Observation | Corroborated | High | P3, W1, W2 |
| HS-003 | The scanner reveals yellow structural cut points. The Stinger melts an eligible joint under sustained aim. Cutter temperature rises during work and overheating risks ignition. | Observation | Corroborated | High | P3, W1, W2 |
| HS-004 | Parts with another structural connection remain attached. After sufficient links are removed, intact disconnected groups can move. The grapple can acquire and release compatible pieces; a heavy or attached target is harder to move than a small freed piece. | Observation | Corroborated | High | P3, W1, W2, R2 |
| HS-005 | Current part designation sets its destination: for example, nanocarbon exterior to Processor, aluminium interior to Furnace and intact reuse equipment to Barge. Delivery contributes credited value and destruction or incompatible consumption is tracked separately. | Observation | Corroborated | High | P3, W1, W2, R1, R2 |
| HS-006 | Ordered salvage goals are reached by credited ship value. Returning to the HAB settles the shift into a report; unfinished work can carry into another shift. The achieved goals and remaining pieces are separate. | Observation | Corroborated | High | P4, W1, W2, R2 |
| HS-007 | Live suit reserves constrain an excursion. Oxygen can be topped up at the HAB-side kiosk. The standard timed rules add a nominal 15-minute shift; this does not imply that every training prompt consumes the timer in the same way. | Observation | Corroborated | High | P3, W1, W2, R1 |

## Basic data

- Blackbird Interactive / Focus Entertainment at launch. FAM-007 for
  physics and structural manipulation. FAM-010 for persistent drift,
  resource depletion and the live consequences of cutter use.
- P1: [US Xbox Series product](https://www.xbox.com/en-US/games/store/hardspace-shipbreaker/9nd8c4314zzg).
  Product ID, series hardware, campaign and cutting and grappling tools.
- P2: [Publisher's console launch notice](https://www.focus-entmt.com/en/news/hardspace-shipbreaker-vient-de-debarquer-sur-consoles).
  Dated 20 September 2022, identifies Xbox Series X and S and the
  campaign, with the earlier PC release separate.
- P3: [Blackbird's first-ship guide for Xbox](https://news.xbox.com/en-us/2022/09/21/tackling-your-first-ship-in-hardspace-shipbreaker/).
  Dated 21 September 2022. Describes movement and braking, scanner and
  cut points, heat and ignition, the Mackerel and available supplies.
- P4: [Developer's version 1.0 announcement and patch notes](https://store.steampowered.com/news/posts/?appgroupname=Hardspace%3A+Shipbreaker&appids=1161580&enddate=1668679286&feed=steam_community_announcements).
  Documents the released campaign and preservation of in-progress salvage
  on returning to the HAB. Windows notes are corroboration for common
  features, not Xbox patch identification.
- W1: [AK Style Gamer's Series S-labelled capture](https://www.youtube.com/watch?v=gAQ4wQFGLYg).
  Sampled at 0:00–1:30 for bay position and tools, 8:20–12:10 for cuts
  and visible grapple feedback, 13:00–16:30 for bays and separated
  parts, and 27:00–27:40 for return and reports. The intervening
  replacement sequence does not establish a death-free recovery.
- W2: [Got Space Game's full-release second training shift](https://www.youtube.com/watch?v=RzhVIVT7hZY).
  Dated 26 May 2022. The author identifies the Hazard 0 Station Hopper.
  Stills at 0:40–1:40 show job selection, at 3:10–4:20 the scanner
  and first cuts, at 12:30–15:20 routing and return, and at
  15:30–18:20 the reports. Used for sequence and qualitative parity.
- R1: [Contemporaneous full-release written walkthrough](https://indiecator.org/2022/06/02/starting-out-in-hardspace-shipbreaker/).
  Its early Station Hopper is a separate example. Corroborates paid
  supplies, receiver classes and distinguishing fees from salvage value.
- R2: Community references on the [salvage bay](https://hardspaceshipbreaker.fandom.com/wiki/Salvage_Bay),
  [grapple](https://hardspaceshipbreaker.fandom.com/wiki/Handheld_Utility_Grapple)
  and [salvage goals](https://hardspaceshipbreaker.fandom.com/wiki/Salvage_Goals).
  Restrict to effects corroborated by the released captures and rules;
  exact numbers, tool upgrades and later structural variants are out.
- Sources accessed 2026-11-20.

## Mechanical decomposition

### Action Genes

- ACT-008: directly navigate the bay and hull through free space.
  ACT-048: acquire an eligible loose object with the grapple, guide it
  relative to the worker and release it into live space (HS-002, HS-004).
- ACT-341: address the kiosk or HAB control to buy supplies or commit
  return. ACT-785: sustain the point cutter on an eligible link for
  severance (HS-003, HS-006, HS-007).

### System Behaviour Genes

- SYS-1708: persist velocity after thrust stops, with active braking.
  SYS-1709: preserve connected hull pieces until removing the last
  supporting path, then move the detached group (HS-002–HS-004).
- SYS-1710: register parts according to receiver class. SYS-1711:
  escalate credited recovery through ship-specific thresholds without
  counting losses as salvage (HS-005, HS-006).
- SYS-1712: commit the shift report and preserve unfinished salvage.
  SYS-1713: cutter exposure builds heat with an ignition consequence.
  SYS-1714: oxygen drains during the excursion but a reachable
  supply kiosk can refill it (HS-003, HS-006, HS-007).

### Constraint Genes

- CON-060: an ordinarily melted structural link cannot reconnect
  during that job. CON-556: the grapple depends on target eligibility,
  attachment, mass and physical clearance (HS-003, HS-004).

### Information Genes

- INF-119: suit air and other personal reserves are visible.
  INF-271: tool and part response expose the grapple relation
  (HS-004, HS-007).
- INF-551: inspection exposes cut points and the hovered material
  or destination. INF-552: credited, destroyed and remaining potential
  can be distinguished against the milestone band and final report
  (HS-003, HS-005, HS-006).

### Objective Genes

- OBJ-002: maximise retained recovery value with the current ship
  and preserve access to higher milestone rewards (HS-005, HS-006).

### Time Genes

- TIM-003: inputs are accepted while the bay, drift, heat and oxygen
  advance in real time; the normal shift imposes an additional time
  budget (HS-002, HS-003, HS-007).

## Reproducible transitions

| Before | Action or event | Bounded result | Claims |
| --- | --- | --- | --- |
| Worker has velocity in clear space | Release movement input, then apply brakes | Coasting persists until the braking input changes it | HS-002 |
| A hull panel has several joints | Inspect with the scanner and melt one identified link | The chosen link disappears; remaining links can keep the panel attached | HS-003, HS-004 |
| One structural path still joins the panel | Melt the remaining joint, then acquire the freed panel | The resulting live rigid part can move independently | HS-003, HS-004 |
| Freed panel, interior section and seat have distinct classes | Route each to its indicated receiver | Appropriate delivery contributes recovery value when registered | HS-005 |
| Reusable material is destroyed or consumed incompatibly | Read the ship progress and lost value | Loss uses the separately tracked share and can eliminate an attainable goal | HS-005, HS-006 |
| Cutting several joints adds heat | Stop firing between targets | Heat exposure is interrupted before the hazardous threshold | HS-003, HS-007 |
| Suit oxygen runs low during salvage | Use the kiosk rather than the return control | The player can resume the current shift with oxygen replenished | HS-007 |
| The intended recovery is reached or the worker chooses to stop | Enter the HAB and inspect the shift report | Results are settled, with unfinished hull state distinct from the report | HS-006 |

## Strategic and experiential structure

Plan from deliverable groups, not from the number of cuts. A legal cut
can be operationally wasteful when a large outer section still has a
connection or when the worker pushes it toward the wrong intake. Free
the needed part with clearance and deliver it intact. Oxygen creates
a reason to return to the outside supplier, but a resupply is different
from ending the shift. When more work remains, settlement preserves
the distinction between stopping work and completing salvage.

## Replay and variation

The loop is reproducible on an early ordinary hazard-free Mackerel.
Optional equipment, part layout, recovery and elapsed work may vary
between spawned hulls and routes. Do not use one ship's payout or a
capture's accidental damage to define universal quotas.

## Adjacent systems and history

Later paid upgrades, pressure management and advanced reactors require
their own evidence. The 2022 commercial console edition is the target,
with Windows 1.0 supplying labelled corroboration of common training.
No PC control binding, platform achievement, later update feature or
hardware difference is inferred from those frames.

## Normalised genome

| Type | Active gene IDs | Carrier parameters |
| --- | --- | --- |
| Action | ACT-008, ACT-048, ACT-341, ACT-785 | direct free-space navigation, grapple acquire and release, reach interaction, point cut |
| System Behaviour | SYS-1708, SYS-1709, SYS-1710, SYS-1711, SYS-1712, SYS-1713, SYS-1714 | drift, detach, route by class, retained value thresholds, shift settlement, heat and oxygen |
| Constraint | CON-060, CON-556 | irreversible joints and grapple eligibility |
| Information | INF-119, INF-271, INF-551, INF-552 | reserves, grapple response, cutpoint and destination labels, recovery and loss |
| Objective | OBJ-002 | improve credited recovery |
| Time | TIM-003 | live drift, heat, oxygen and ordinary shift budget |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `580` (`GAME-0001`–`GAME-0580`).
- Exact genome matches: none.
- Tied near matches: `GAME-0212` — Half-Life 2 (`7 / 36 = 0.194444`).
- Supported combination subsets: none.
- Scan date: 2026-11-20.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
| --- | --- | --- | --- |
| `GAME-0212` — Half-Life 2 | ACT-008, ACT-048, ACT-341, CON-556, INF-119, INF-271, TIM-003 | The two loops authorise remote manipulation of eligible loose props while the world remains live. Ravenholm can turn those props into weapons against hostile groups. The Mackerel shift first disconnects structural groups and then routes freed bodies to class-specific receivers for credited recovery and a work report. | `7 / 36 = 0.194444` |

### Preserved research notes

- New genes: ACT-785, SYS-1708–SYS-1714, INF-551 and INF-552.
- Classification result: New gene.

## Taxonomy impact

- [TAXONOMY_CHANGE_327](../../../research/taxonomy-changes/TAXONOMY_CHANGE_327.md)
  separates point cutting, structural release, current material routing
  and settlement, and distinguishes the scanner from the recovery report.

## Negative results

- Reject ACT-027: the point cutter needs held aim rather than a swipe.
- Reject unqualified SYS-705: a grapple tether to a heavy object can move
  the worker, and its evidence does not establish the specific Half-Life 2
  collision-bounded held pose in all cases here.
- Reject SYS-543: oxygen comes from a designated supply rather than
  breathing freely at a reachable air surface.
- No gene for bay or laser colour on its own, exact transfer forces or
  speculative pressure, reaction or fuel-line sequences.

## Delta summary

## New facts

- [Observation | Corroborated | High] Severance makes some hull parts
  available to move; only type-appropriate delivery recovers their
  salvage value. Work can settle while the ship is still unfinished.

## New genes

- [Observation | Corroborated | Medium] Ten additions in
  TAXONOMY_CHANGE_327.

## New combinations

- [Observation | Corroborated | High] No new verified combination
  proposed. The comparison records existing subset matches.

## Taxonomy changes

- [Observation | Corroborated | Medium] Prior signatures and definitions
  are retained.

## New questions

- A controlled Xbox capture can resolve grade, recovery thresholds,
  controller behaviour and exact reporting of damaged components.

## Next recommended game

- [Hypothesis | Limited | Medium] GAME-0582, the 1998 Windows release
  of Grim Fandango. Examine a complete early puzzle loop and its
  handoff without assuming mechanics from the remaster.
- Optimisation criterion: contrast continuous physical disassembly with
  authored item and conversation dependencies.

## Why this game

- [Hypothesis | Limited | Medium] Its short training work order shows
  how disassembly choices affect material value and how those results
  survive settlement independently of the movement controls.
