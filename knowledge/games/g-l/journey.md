---
game_id: GAME-0436
slug: journey
game_title: Journey
analysis_status: reviewed
reviewed: 2026-09-27
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-573
  system:
    - SYS-1142
    - SYS-1143
    - SYS-1144
  constraint:
    - CON-711
  information:
    - INF-423
  objective:
    - OBJ-026
  time:
    - TIM-003
---

# Game: Journey — crossing the broken bridge

Use the [canonical vocabulary and genome rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Robes, scarf embroidery, the mountain and named chapters are carrier parameters, not universal gene names.

## Analysis scope

- Version / ruleset: original 2012 PlayStation 3 *Journey*, ordinary first-play red-robed traveller entering the Bridge chapter after the opening gate. No PS4, PC, iOS, white-robe replay, trophy challenge or later wrapper rule is imported. Exact original binary revision is uninspected.
- Structured analysis target: `PLAT-PLAYSTATION-3` in [`knowledge/platforms/games.json`](../../platforms/games.json).
- Scenario: enter the Bridge area with the ordinary short scarf, release reachable trapped cloth to form a usable route over the broken bridge, then activate the far-end monument and pass into the next area. An anonymous second traveller may appear during an online session, but the same terminal remains possible alone.
- Primary decision loop: directly walk and position the traveller, use the call or contact to wake nearby cloth, read which bridge spans are present and how much the scarf glows, spend charged scarf power for a jump or glide when useful, and regain charge from cloth or a nearby companion before reaching the far shore.
- Entry: the opening gate has already been crossed; the traveller stands at the Bridge entrance before the local cloth segments have been released. The opening desert and first gate are prerequisites, not replayed here.
- Positive terminal: the traveller crosses the bridge area, activates the far-end monument and enters the newly revealed next passage. The bridge need not be fully rebuilt; PlayStation's original `Threshold` trophy expressly allows a crossing with incomplete reconstruction.
- Failure and recovery: an exhausted scarf removes the charged jump or glide opportunity until recharged; a missed gap can require repositioning. This packet does not assert lives, combat defeat, a fixed retry point or a mandatory co-op partner.
- Included: local movement, call and cloth contact, partial bridge restoration, charged jump/glide and recharge, visible scarf and bridge state, optional anonymous encounter and companion-based recharge, far-end monument and passage.
- Excluded: the full mountain pilgrimage, all glowing symbols or ancient glyphs, trophy hunting, fixed bridge-piece count as a win condition, forced matchmaking, private lobby, voice chat, later snow or creature hazards, white-robe self-recharge and exact scarf-unit/timing constants.
- Reproducible parameterisation: start an ordinary original-PS3 first play at the Bridge entrance. Release enough local cloth to make a viable route, optionally use charged movement over an unrepaired span, reach the far end and activate its monument. Online matching may supply zero or one anonymous companion; if present, close proximity can restore scarf charge but is not a route prerequisite. Exact cloth positions, chosen gaps and companion appearance vary.
- Potential scoped modules: exact bridge-piece geometry and shortest incomplete crossing; every symbol's scarf-length effect; later cooperative flight; whole-campaign anonymous-companion trophies.
- Direct-play status: no PS3 executable, input trace, original screenshot, video or audio was inspected. The original producer's trophy list, creator interview, publisher's first-person post-release retrospective and contemporaneous first-hand PS3 written route support the bounded reconstruction. The 2011 interview describes pre-release controls and is not relied on for final button mapping.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `JO-001` | The original PS3 chapter has a broken bridge; freeing cloth forms traversable sections, and reaching the far monument opens the next passage. | Observation | Corroborated | High | P1, S1 Bridge |
| `JO-002` | A complete bridge restoration is not required for a successful crossing. | Confirmed | Direct | High | P1 `Threshold` |
| `JO-003` | The scarf's visible charge funds jumping/gliding and can be restored by contact with local cloth. | Observation | Corroborated | High | S1 controls and Bridge; P2 borrowing-power intent |
| `JO-004` | Calling is a bounded nonverbal signal to nearby cloth or another traveller, not text or voice chat. | Observation | Corroborated | High | P2, P3 |
| `JO-005` | Online encounters are anonymous and optional; two travellers in contact can recharge each other's scarf. | Observation | Corroborated | High | P3, S1 online |
| `JO-006` | The bridge route can be completed alone; no named partner or private lobby is a precondition. | Observation | Corroborated | High | P3, S1 online, P1 |

## Basic data

- Release / origin: original PlayStation 3 *Journey*, 2012; later ports and replay-only abilities excluded.
- Platform or physical form: original PS3 downloadable game with direct movement and call / charged-movement inputs. Exact firmware or binary build is not asserted.
- Mechanical families: state transformation (`FAM-003`) for the cloth-built route; ordered dependency sequencing (`FAM-017`) for a reachable crossing before the far monument.
- **P1**: [PlayStation's original 2012 trophy list](https://blog.playstation.com/archive/2012/02/27/journey-the-trophies/), especially `Threshold` and companion trophies (accessed 2026-09-27).
- **P2**: [Jenova Chen's creator interview on PlayStation Blog](https://blog.playstation.com/2011/01/11/jenova-chen-explains-journey-social-relevance-and-artistic-inspirations/comment-page-2/), January 2011, cloth response to calls and borrowed flight power. This is pre-release design evidence only, not proof of final controller mapping.
- **P3**: [PlayStation's first-person Journey retrospective](https://blog.playstation.com/?p=224007), 2020, anonymous encounter, one call, optional solo travel and mutual scarf recharge. A publisher-hosted personal observation, not an original manual.
- **S1**: [ScrawlKnight's first-hand original-PS3 walkthrough](https://gamefaqs.gamespot.com/ps3/997885-journey/faqs/63951), controls, online explanation and Bridge route (accessed 2026-09-27). Its detailed route is corroborating player evidence, not a claim of direct Atlas play.
- Claim IDs: `JO-001`–`JO-006`.

## Mechanical decomposition

### Action Genes

- Reuse `ACT-008` for directly guiding one traveller over sand, stone and available cloth, including its charged jump trajectory. Do not treat an anonymous companion as a second locally controlled body.
- Add `ACT-573` for the player's nonverbal call directed into local reach. The same input can address cloth or signal a traveller; it is not a spoken command or a reusable item.

### System Behaviour Genes

- Add `SYS-1142` for trapped cloth becoming one traversable bridge span when activated by eligible contact or call. Do not collapse it into generic physical repair by an engineer or demand all spans.
- Add `SYS-1143` for the scarf charge being spent on powered motion and restored by compatible cloth or nearby companion contact. The short first-play capacity is a parameter.
- Add `SYS-1144` for an optional anonymous co-traveller entering the same live area without player-directed partner selection, with presence never required for this crossing.

### Constraint Genes

- Add `CON-711` for a powered jump/glide requiring positive usable scarf charge; normal walking remains legal at zero. A gap may still be crossed by another viable route or cloth span.

### Information Genes

- Add `INF-423` for the visible scarf glow and present bridge spans informing whether powered motion is available and which crossing is currently traversable; neither reveals a future companion nor a complete map.

### Objective Genes

- Reuse `OBJ-026` for reaching the far passage after making the bridge route traversable. Completing every cloth span or obtaining the `Threshold` trophy is not this objective.

### Time Genes

- Reuse `TIM-003` for continuously steered movement and online companion presence while inputs remain live, not a timed deadline or turn-resolution clock.

## Reproducible transitions

| Before | Player input | Bounded resolution | Mechanic established | Claim ID |
|---|---|---|---|---|
| Bridge approach with an unreleased cloth cluster | Move into or call near eligible cloth | The cloth rises to form a usable local bridge segment | world geometry changes from cloth activation | `JO-001`, `JO-004` |
| Scarf glows with usable charge | Jump or glide toward a reachable section | Charge is spent and motion carries the traveller; at exhaustion the same powered lift is unavailable | movement depends on a visible renewable reserve | `JO-003` |
| Traveller is near compatible cloth or a present companion | Make contact or stay nearby | Scarf charge can return; a stranger is not necessary because cloth also works | alternate recharge channels | `JO-003`, `JO-005` |
| Some bridge spans remain absent | Choose a viable path over the available spans and charged movement | The far shore can still be reached without full reconstruction | incomplete bridge is a valid crossing | `JO-002`, `JO-006` |
| Far shore reached | Activate the far monument and enter the opening | The next passage becomes available and this packet ends | separate route terminal | `JO-001` |

## Strategic and experiential structure

- Immediate choice: call or touch nearby cloth, then decide whether the current scarf charge is enough for the next move or whether to recharge first.
- Medium-term plan: bring up enough spans to reach the far end; full restoration is optional, and companionship can ease rather than gate movement.
- Long-term boundary: opening the next passage completes this local chapter packet, not the whole pilgrimage or a companion trophy.
- Failure attribution: no source supports a fixed death, score or exact charge threshold for a missed gap here; model loss of powered mobility and rerouting rather than inventing punishment.

## Replay and variation

The chosen cloth spans, optional symbols, charged jumps and online companion vary. The far-end passage is the stable terminal. An offline solo route and an online shared route preserve the same objective, with the latter adding possible mutual scarf recharge.

## Adjacent systems and history

*A Monster's Expedition* (`GAME-0054`) also creates traversable bridge geometry, but by rolling a persistent log; Journey releases responsive cloth and permits incomplete restoration. *It Takes Two* (`GAME-0215`) requires two controlled partners for its cooperative chapter, unlike Journey's optional, anonymous presence. The exact neighbour IDs and overlap are recomputed below rather than inferred from genre.

## Normalised genome

| Type | Active gene IDs | Key parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-573` | direct movement and nonverbal call |
| System Behaviour | `SYS-1142`, `SYS-1143`, `SYS-1144` | cloth spans, scarf energy and optional stranger |
| Constraint | `CON-711` | charged movement eligibility |
| Information | `INF-423` | visible charge and available spans |
| Objective | `OBJ-026` | reach far passage |
| Time | `TIM-003` | live movement and optional co-presence |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `435` (`GAME-0001`–`GAME-0435`).
- Exact genome matches: none.
- Tied near matches: `GAME-0098` — Hyperbolica (`3 / 13 = 0.230769`).
- Supported combination subsets: none.
- Scan date: 2026-09-27.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0098` *Hyperbolica* | `ACT-008`, `OBJ-026` and `TIM-003` describe directly steering an avatar to a reached world location under live movement. | Hyperbolica's scoped maze changes perceived and actual route geometry through a hyperbolic metric, with authored branch decisions and a final crystal. Journey changes an initially broken crossing through responsive cloth, spends a renewable scarf reserve and may introduce an anonymous but unnecessary companion. Shared locomotion and destination do not equate metric navigation with bridge construction or social recharge. | Sole tied-near maximum, `3 / 13 = 0.230769`; not an exact or verified-combination match. |

## Taxonomy impact

`TAXONOMY_CHANGE_173` admits an acoustic call, cloth-span activation, renewable scarf motion, optional anonymous co-presence, charged-motion legality and visible cloth/charge state. Existing direct movement, reachable-location objective and live time are reused. No earlier signature or verified combination changes.

## Negative results

- `SYS-1060` repairs a destroyed bridge through a consumed engineer entering a hut; Journey's local cloth responds to call or contact without a repair unit.
- `CON-633` is Noita's continuously held upward levitation reserve; Journey's charged jump/glide and scarf recharge do not establish that same held-lift boundary.
- A mandatory two-player objective is rejected: original-PS3 solo traversal remains possible.
- Full bridge reconstruction is rejected as an objective, since the publisher explicitly recognises an incomplete crossing.
- The 2011 prototype interview's automatic-jump remark is not treated as final 2012 PS3 button evidence.

## Delta summary

## New facts

- [Confirmed | Direct | High] The original producer's trophy list explicitly recognises a successful crossing without complete bridge reconstruction (`JO-002`).
- [Observation | Corroborated | High] An optional anonymous traveller can restore scarf charge by contact, while ordinary cloth also recharges it (`JO-003`, `JO-005`).

## New hypotheses

- [Hypothesis | Limited | Medium] Exact charge units and minimum released bridge spans for each solo route require an original-PS3 input trace; they are not inferred here.

## New genes

- [Observation | Corroborated | High] Six typed boundaries in `TAXONOMY_CHANGE_173` separate call, bridge, scarf, stranger, charge legality and visible state.

## New combinations

- [Observation | Limited | Medium] No new verified combination proposed.

## Taxonomy changes

- [Observation | Corroborated | High] `TAXONOMY_CHANGE_173`; earlier signatures unchanged.

## New questions

- Which incomplete-span routes are possible with the shortest first-play scarf in each exact original PS3 build?

## Next game

`GAME-0437` *Diner Dash*, original PC, follows after the Goal stop window. Its research question is how seating, service chains and customer patience govern one shift; no rules are presumed from selection alone.
