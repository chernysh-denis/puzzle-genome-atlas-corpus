---
game_id: GAME-0413
slug: ape-escape
game_title: Ape Escape
analysis_status: reviewed
reviewed: 2026-09-26
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-164
    - ACT-477
  system:
    - SYS-1099
    - SYS-1100
  constraint: []
  information:
    - INF-406
  objective:
    - OBJ-242
  time:
    - TIM-003
---

# Game: Ape Escape

Use the canonical [vocabulary and genome rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Monkey identity, stage geometry, detection distance and controller sensitivity are parameters, not separate genes.

## Analysis scope

- Version / ruleset: original North American PlayStation *Ape Escape* (`SCUS-94423`, 1999), Normal Play's first visit to Fossil Field, from first controllable movement through the three-monkey stage-clear return to the Time Station. This is not a PlayStation 4/5 conversion or *Ape Escape: On the Loose*.
- Structured analysis target: `PLAT-PLAYSTATION` in [`knowledge/platforms/games.json`](../../platforms/games.json). The exact disc revision and emulator or console image were not inspected.
- Primary decision loop: move with the left stick toward one reachable uncaught monkey, choose the Time Net from the starting gadgets, steer a local net sweep with the right stick as the target moves or evades, and repeat until three distinct accepted captures satisfy the stage's minimum quota.
- Entry and exit: enter Fossil Field from the Time Station with the starting Stun Club and Time Net. Stop on the automatic return after the third caught monkey. The area contains four monkeys, but the fourth requires a later Sky Flyer route and is not a first-visit obligation.
- Included: independent avatar movement and directional net control, gadget selection, monkey evasion, net hit or miss, retained distinct catches, disclosed stage quota and real-time target movement. The Stun Club is available but no club strike is required in the selected three-catch route.
- Excluded: orange-enemy combat, optional chips or Specter Coin, hidden or fourth-monkey collection, Sky Flyer acquisition, other gadgets, later stages, Time Attack, minigames, full-campaign completion, PlayStation 4/5 rewind or quick save and exact numerical detection, collision or damage values. A later return for the fourth monkey would be a separate scoped module.
- Direct-play status: none. No original disc, controller input trace, gameplay video, audio or frame capture was inspected. Sony's product/history material establishes the original product and dual-stick gadget premise; multiple original-PlayStation player-authored walkthroughs corroborate first-stage counts and controls. The original manual scan could not be fetched for visual verification and is not claimed as inspected.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `APE-001` | The original 1999 PlayStation game requires dual analog control and uses a gadget net to capture monkeys. | Confirmed | Direct | High | S1, S2 |
| `APE-002` | Left stick moves the avatar, a face-button slot selects a gadget, and right-stick direction swings the chosen Time Net independently of movement. | Observation | Corroborated | High | W1, W2, S1 |
| `APE-003` | Fossil Field's first visit needs three of four monkeys; the remaining high-route monkey is reserved for a later gadget return. | Observation | Corroborated | High | W1, W3, W4 |
| `APE-004` | A successful net contact catches one monkey and advances the distinct-capture count; missed swings and approaching an evading target do not. | Observation | Corroborated | High | S2, W1, W2 |
| `APE-005` | The first-visit quota ends the stage and returns the player to the Time Station without requiring the fourth catch. | Observation | Corroborated | Medium | W1, W3, W4 |
| `APE-006` | Exact disc-revision frame timing, evasion thresholds and net collision volumes are not established by this source packet. | Observation | Limited | High | S1–S2, W1–W4 |

## Basic data

- Release / origin: Sony's PlayStation history identifies *Ape Escape* as a 1999 first-generation PlayStation title built for twin analog sticks. The North American original product identifier is `SCUS-94423` in Sony's present store listing; that listing serves as product identification, not proof of the modern conversion's original control timing.
- Platform or physical form: original PlayStation disc with required dual-analog controller, Normal Play first stage.
- Mechanical families: real-time system pressure (`FAM-010`).
- Sources accessed 2026-09-26:
  - **S1** — [Sony PlayStation history](https://www.playstation.com/uk-ua/playstation-history/1994-ps-one/), original Ape Escape and required DualShock/twin-stick gadget design.
  - **S2** — [Sony Ape Escape product listing](https://store.playstation.com/en-us/product/UP9000-PPSA06319_00-SCUS944230000000/), original PlayStation identity and Time Net in the gadget set. Its modern emulation features are expressly outside this scope.
  - **W1** — [AmericanArsenal original-PlayStation walkthrough](https://gamefaqs.gamespot.com/ps/196614-ape-escape/faqs/26743), control mapping and Fossil Field's three-needed/four-total first visit. It is a player-authored reconstruction, not Sony's rulebook.
  - **W2** — [CHyde original-PlayStation walkthrough](https://gamefaqs.gamespot.com/ps/196614-ape-escape/faqs/8940), left/right-stick operation, gadget buttons and stage progression.
  - **W3** — [CaptainCAWisma original-PlayStation walkthrough](https://gamefaqs.gamespot.com/ps/196614-ape-escape/faqs/32849), first-stage accessible three and later propeller-dependent fourth.
  - **W4** — [Gbness original-PlayStation walkthrough](https://gamefaqs.gamespot.com/ps/196614-ape-escape/faqs/25865), three-needed first-level quota, four total and hub progression.
- Claim IDs: `APE-001`–`APE-006`.

## Mechanical decomposition

### Action Genes

- `ACT-008` moves the directly controlled explorer through the open stage. The left stick's direction and degree govern approach; jump and camera controls are local traversal parameters, not independent genes in this bounded net-capture loop.
- `ACT-164` selects the assigned Time Net as the active gadget. `ACT-477` commits one directional held-net sweep through a currently reachable monkey's position; steering the right stick is an input parameter of that transient volume test, not a second catch.
- The starting Stun Club can strike enemies or briefly interrupt a monkey in other routes, but the selected three captures can be completed with the net. This record does not claim a mandatory club hit or add a redundant action gene for controller hardware.
- Claim IDs: `APE-001`, `APE-002`, `APE-004`.

### System Behaviour Genes

- `SYS-1099` changes an uncaught monkey's local position when the explorer approaches or misses, requiring a new approach and swing; exact perception and speed parameters are unmeasured.
- `SYS-1100` turns accepted Time Net contact into one retained caught flag, removes that monkey from the local chase and increments the stage count. This is not Animal Crossing's inventory specimen and catalogue state (`SYS-922`) or a consumable probability roll (`SYS-307`).
- Resolution order at the analysed boundary: move and choose a reachable target → steer net swing → resolve contact against the target's current position → on success remove and count that distinct monkey, otherwise it may keep evading → compare count to the quota. Simultaneous-frame priority is unknown.
- Claim IDs: `APE-002`–`APE-006`.

### Constraint Genes

- No new constraint is asserted. Current physical reach is a parameter of `ACT-477`. The high fourth-monkey route is excluded because Sky Flyer is unavailable on the first visit; it is not silently counted as a failed attempt to meet the three-catch quota.
- Claim IDs: `APE-003`, `APE-006`.

### Information Genes

- `INF-406` exposes the stage's three-needed and four-total distinction and accepted catch progress. A visible animal's motion gives local targeting information but not omniscient future position or an exact collision volume.
- Claim IDs: `APE-003`, `APE-004`, `APE-006`.

### Objective and Time Genes

- `OBJ-242` settles the first Fossil Field visit when three distinct monkeys have been caught and returns the player to the Time Station. The optional fourth is not required for this first clear.
- `TIM-003` captures the fact that monkey movement and net collision continue in real time while the player moves and aims. There is no ordinary first-stage deadline in this scope; a separate Time Attack mode is excluded.
- Claim IDs: `APE-003`–`APE-005`.

## Reproducible transitions

| Before | Action | Bounded resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| First visit, Time Net available, no monkey caught | Select net and approach one ground-level monkey | The chosen tool becomes active while the monkey remains a live local target | selection and approach are distinct | `APE-002` |
| One uncaught monkey moves near the explorer | Swing net through its old position | Swing misses; no caught flag or quota increment; target can keep moving | contact, not proximity or button press, counts | `APE-004` |
| One reachable monkey intersects the directed net sweep | Commit the net swing | That monkey disappears from local chase and the accepted count grows by one | persistent distinct capture | `APE-004` |
| Two distinct monkeys are already caught | Catch another reachable uncaught monkey | Count reaches three and first-visit stage clear returns to Time Station | minimum quota settles before full four | `APE-003`, `APE-005` |
| Fourth monkey remains high and Sky Flyer is not yet acquired | Try to count it as required first-visit progress | It is not needed to satisfy the three-catch exit; later route is excluded | optional inaccessible remainder is not failure | `APE-003` |

## Strategic and experiential structure

- Local decision: approach a monkey and time the independently steered net arc against its current rather than previous position.
- Medium-term planning: select the three ground-accessible catches rather than assuming all four are required before leaving the era.
- Failure attribution: a missed sweep or an evasive change in target position does not produce credit; a Stun Club hit is not a Time Net capture. The exact collision and alert thresholds remain unmeasured.
- Player-trust factor: the three-needed/four-total presentation makes the first clear intelligible even though a future-gadget target remains visible.
- Claim IDs: `APE-002`–`APE-006`.

## Replay and variation

- Approach order, local monkey positions and missed-swing count can differ; the first-visit quota remains three distinct accepted captures. No random distribution or speed value is inferred.
- The stick layout lets locomotion and the selected gadget's direction be controlled separately, but the mechanic is still one contact test followed by a separate catch resolution.

## Adjacent systems and history

- Animal Crossing: New Horizons shares `ACT-477`'s aimed net sweep but turns an insect into a carried specimen and catalogue credit. Ape Escape instead uses a monkey catch as first-stage progress and exits at a minimum quota; the target class broadens the action definition without changing the earlier Animal Crossing signature.
- Pokémon Red Version and Pokémon Legends: Z-A use a consumed capture device and a creature-capture check; those are not the reusable contact-only Time Net.
- The high fourth monkey and later Sky Flyer might support a separate capability-gated route analysis, but are not smuggled into the first-visit genome.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-164`, `ACT-477` | left/right stick mapping, gadget slot and net arc |
| System Behaviour | `SYS-1099`, `SYS-1100` | target evasion, accepted catch flag and counter |
| Constraint | none | current physical reach; future Sky Flyer route excluded |
| Information | `INF-406` | required, total and caught displays |
| Objective | `OBJ-242` | three-of-four first-clear quota |
| Time | `TIM-003` | moving target during input |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `412` (`GAME-0001`–`GAME-0412`).
- Exact genome matches: none.
- Tied near matches: `GAME-0391` — Uncharted 2: Among Thieves (`2 / 11 = 0.181818`).
- Supported combination subsets: none.
- Scan date: 2026-09-26.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0391` — Uncharted 2: Among Thieves | `ACT-008`, `TIM-003` | Both permit direct traversal while the world continues in real time. Uncharted 2's analysed train route converts climbing, cover and ranged combat into a checkpoint escape; Ape Escape independently steers a reusable net against evasive animals and ends at a three-of-four catch quota. The low overlap is structural, not a claim that the two games feel alike. | Near, `0.181818` |

## Taxonomy impact

- [`TAXONOMY_CHANGE_151`](../../../research/taxonomy-changes/TAXONOMY_CHANGE_151.md) broadens `ACT-477` from insect-only net contact to a reachable living creature and admits `SYS-1099`, `SYS-1100`, `INF-406` and `OBJ-242`. No earlier signature is changed.

## Negative results

- `SYS-922` rejected: the caught monkey does not become an inventory specimen or species-catalogue entry in this packet.
- `SYS-307` and `ACT-194` rejected: Time Net contact is not a consumed device with a probabilistic companion check.
- `OBJ-019` rejected: the player is not escorting a minimum population through a fixed exit.
- `CON-349` not admitted: the high fourth monkey's later capability gate is outside this first-clear scope.
- Original manual scan and exact disc/frame values remain unverified rather than inferred from the modern emulation listing.

## Delta summary

The first Fossil Field visit makes a separately steered reusable net a live contact test against evasive targets. Three accepted individual captures clear the stage even though four monkeys exist and the last one belongs to a later capability return.

## New facts

- [Confirmed | Direct | High] Sony identifies the original PlayStation game as a twin-analog gadget-capture design (`APE-001`).
- [Observation | Corroborated | High] Original-PlayStation walkthroughs consistently distinguish Fossil Field's three-needed first clear from its four-monkey total (`APE-003`).

## New genes

- [Observation | Corroborated | High] Evasive capture movement, net-to-retained-catch resolution, displayed quota and minimum-catch stage clear require four new typed boundaries; `ACT-477` is broadened without a new duplicate net action.

## New combinations

- [Observation | Limited | High] No new verified combination is asserted from this one game; existing subset scan is recomputed below.

## Taxonomy changes

- [Observation | Corroborated | High] `TAXONOMY_CHANGE_151` documents the net-action broadening and four new genes without revising an earlier game's signature.

## New questions

- What are the exact disc-revision alert ranges, sweep volumes and simultaneous movement/contact priority for the first Fossil Field monkeys?
- Which later Sky Flyer route reaches the fourth monkey, and how does that change a separate return-visit packet?

## Next recommended game

- [Hypothesis | Limited | Medium] `GAME-0414` *Kinect Adventures!*.
- Optimisation criterion: change platform and input surface from PlayStation dual-stick handheld gadget capture to Xbox 360 body-tracking motion interaction.
- Expected information gain: separate bodily pose recognition and sensor feedback from discrete controller-directed tool contact.
- Backlog impact: no selected subject displaced.

## Why this game

- [Hypothesis | Corroborated | Medium] Ape Escape tests whether a net swing against a moving local creature can be reused across different games while the capture outcome and stage-quota closure remain distinct system and objective genes.
