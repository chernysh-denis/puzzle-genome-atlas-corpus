---
game_id: GAME-0108
slug: cocoon
game_title: Cocoon
analysis_status: reviewed
reviewed: 2026-08-15
combination_ids:
  - COMB-0108
gene_ids:
  action:
    - ACT-008
    - ACT-048
    - ACT-112
  system:
    - SYS-144
    - SYS-145
  constraint:
    - CON-162
    - CON-163
  information:
    - INF-001
  objective:
    - OBJ-026
  time:
    - TIM-002
---

# Game: Cocoon

## Analysis scope

- Version / ruleset: Geometric Interactive's 2023 base release, bounded to a
  synthetic post-first-guardian orange-orb packet that composes only documented
  early rules rather than copying one authored room.
- Included: direct avatar navigation; picking up and carrying the persistent
  orange world orb; mounting and retrieving it at a compatible world-jump
  pedestal; entering and leaving its contained world at fixed jump points; the
  already-unlocked first orb ability; carrying that orb to manifest one hidden
  bridge; crossing to a designated route location; visible state; and
  self-paced sequencing.
- Excluded: the guardian fight and ability-acquisition event itself; green,
  purple and white orbs; carrying worlds into other worlds; recursive
  suitcasing; multi-orb machinery; towers, projectiles, eggs, boss fights,
  story interpretation, achievements and platform-specific controls.
- Direct-play status: not conducted. Official publisher and store descriptions
  establish portable world-orbs and unlockable cross-world abilities. Two
  creator interviews document fixed world-jump points and the first ability's
  invisible bridges; contemporary hands-on coverage corroborates pedestal
  projection, entry, carried-only power and orange bridge manifestation. A
  synthetic executable control tests the bounded state transitions.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `COC-001` | Cocoon is a 2023 single-player puzzle adventure by Geometric Interactive, published by Annapurna Interactive | Confirmed | Corroborated | High | P1, P2 |
| `COC-002` | Each scoped world has one persistent orb representation that the avatar can carry | Confirmed | Corroborated | High | P1, P2, P3 |
| `COC-003` | Placing a world orb into the proper mechanism exposes its contained world in a jump surface the avatar can enter | Confirmed | Corroborated | High | P3, S1, V1 |
| `COC-004` | World jumps use authored fixed points and return without replacing the orb's outer identity | Confirmed | Corroborated | High | P3, P4, V1 |
| `COC-005` | An unlocked orb is also a tool whose ability is available in other worlds while that orb is carried | Confirmed | Corroborated | High | P1, P2, P3, S1 |
| `COC-006` | The first, orange-orb ability manifests otherwise invisible bridges | Confirmed | Corroborated | High | P4, S1, V1 |
| `COC-007` | Setting down the orb removes the carried-power condition | Confirmed | Corroborated | High | P3, S1, V1 |
| `COC-008` | The bounded navigation and orb interactions are deterministic and self-paced | Observation | Corroborated | High | P3, P4, S1 |
| `COC-009` | Container-boundary, free-portal and permanent-upgrade genes do not describe the scoped orb identity and carried ability | Observation | Corroborated | High | P1–P4, S1, V1 |

## Basic data

- Release / origin: Geometric Interactive developed Cocoon; Annapurna
  Interactive published it on 29 September 2023.
- Platform or physical form: single-player digital isometric puzzle adventure,
  controlled with directional movement and one contextual interaction button.
- Puzzle family: portable world-object entry and carried world-ability routing.
- Primary / publisher sources:
  - **[P1]** [official Annapurna Interactive page](https://www.annapurna.com/interactive/cocoon),
    for 2023 release context, worlds inside portable orbs and abilities unlocked
    for use inside other worlds.
  - **[P2]** [official Steam page](https://store.steampowered.com/app/1497440/COCOON/),
    for release date, developer / publisher and the same world-orb and ability
    description.
  - **[P3]** [GameSpot developer interview](https://www.gamespot.com/articles/cocoon-developers-open-up-about-leaving-playdead-and-creating-their-most-complex-puzzle-game-yet/1100-6518762/),
    quoting the creators on worlds as orbs, pedestal-pool projection, seamless
    entry, carried powers, power loss on set-down and the one-button controls.
  - **[P4]** [Game Developer interview with Jeppe Carlsen](https://www.gamedeveloper.com/design/the-challenges-of-laying-worlds-upon-worlds-in-puzzle-game-cocoon),
    for fixed world-jump learning, the first ability manifesting invisible
    bridges and the orange world's bridge-oriented terrain.
- Contemporary corroboration:
  - **[S1]** [GameSpot review](https://www.gamespot.com/reviews/cocoon-review-a-bugs-strife/1900-6418123/),
    documenting proper orb insertion, the projected pool, seamless world entry,
    carried powers and the orange orb revealing traversable paths.
  - **[V1]** [`verify_cocoon_orb_world.py`](../../../scripts/verify_cocoon_orb_world.py),
    an original state control for compatible mounting, reversible world entry,
    stable orb identity and carried-only bridge manifestation.

## Mechanical decomposition

### Action Genes

- `ACT-008` — navigate controllable agent. The player walks the insect-like
  avatar among the loose orb, jump pedestal, contained-world core, bridge locus
  and route destination.
- `ACT-048` — pick up and release portable rigid object. The orange orb remains
  visibly carried at a controlled offset while the avatar moves and becomes a
  loose world object again when set down.
- `ACT-112` — mount or retrieve portable world orb at jump pedestal. The player
  inserts the carried orb into the proper jump mechanism to expose its world,
  then retrieves the same orb after returning outside.
- `ACT-087` is absent because the orb is not a discrete inventory item consumed
  by a fixture. `ACT-047` is absent because the player does not aim and create
  replaceable portal endpoints on surfaces.

### System Behaviour Genes

- `SYS-144` — resolve mounted world orb as reversible contained-world entry.
  Mounting exposes the orb's persistent world as a jump surface; entering moves
  the avatar to its fixed inner arrival, and exiting returns the avatar to the
  outer pedestal while the same orb remains mounted.
- `SYS-145` — manifest orb-specific traversal structure from carried ability.
  Once the first ability is already unlocked, carrying the orange orb at a
  receptive locus reveals and supports the otherwise absent bridge.
- Resolution order: carry the orb; validate pedestal compatibility; mount it;
  expose the entry; transfer the avatar to the inner arrival; later return to
  the outer pedestal; retrieve the orb; validate unlock, carried identity and
  bridge locus; manifest the bridge; traverse it.
- `SYS-069` is absent because entry is not an aligned grid-edge crossing.
  `SYS-070` is absent because the orb's containment parent is not rewritten in
  this non-recursive packet. `SYS-059` and `SYS-060` are absent because no
  freely placed aperture pair or velocity transform exists.

### Constraint Genes

- `CON-162` — mounted compatible world orb gates contained-world entry. A loose,
  carried or mismatched orb cannot be entered; the orb must occupy its proper
  pedestal and cannot simultaneously remain carried.
- `CON-163` — unlocked carried orb and compatible locus gate its ability. The
  orange bridge exists only when the ability is unlocked, that exact orb is
  currently carried and the avatar is at a receptive authored route.
- `CON-082` is absent because Cocoon uses fixed jump sites rather than a centre
  cell and aligned open edges of a movable grid container. `CON-078` is absent
  because no surface accepts a player-fired portal footprint.
- Scarce strategic resources: one persistent orb identity and one carried-object
  slot; mounting makes the world enterable but temporarily gives up the carried
  ability, while retrieval reverses those roles.

### Information Genes

- `INF-001` — fully visible current state. The scoped camera shows the orb's
  carried / mounted state, the active jump pool, the avatar's current world,
  the receptive bridge locus and the manifested route without hidden random
  variables.
- Colour and biome are presentation parameters that help world orientation;
  they do not add a second information gene in this single-orb packet.

### Objective Genes

- `OBJ-026` — reach designated traversable world location. The packet ends only
  after the player uses the carried orange ability to create a traversable
  bridge and walks the avatar across to the next route location.
- The prior guardian reward is starting state here, so neither defeating a boss
  nor acquiring every campaign orb is part of this objective.

### Time Genes

- `TIM-002` — sequential actions in self-paced time. The scoped pedestal,
  world-jump and bridge route has no countdown, turn budget or autonomous
  adversary advancing while the player pauses.

## Reproducible transitions

The executable packet combines documented rules with original labels and does
not claim to reproduce one copyrighted authored room.

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Orange orb is loose outside and the world-jump pedestal is empty | Pick up the orb | The same `orange-orb` identity becomes carried; its `orange-world` identity remains unchanged | world and portable object are two roles of one persistent identity | `COC-002` |
| Orange orb is carried beside a pedestal that accepts another orb | Attempt to mount it | The attempt is rejected and the orb remains carried | mounting is compatibility-gated | `COC-003`, `COC-009` |
| Orange orb is carried beside its compatible pedestal | Mount the orb | The orb becomes mounted, leaves the carried slot and exposes its world-jump surface | entry requires external mounting | `COC-003` |
| Orb is only loose or carried | Attempt to enter its world | No transfer occurs | object possession alone is not a portal | `COC-003`, `COC-009` |
| Orange orb is mounted and avatar is outside | Enter the jump surface | Avatar arrives at the fixed point inside `orange-world`; the same orb remains mounted outside | reversible transfer preserves orb identity | `COC-004` |
| Avatar returns through the inner jump point | Exit | Avatar returns beside the outer pedestal and can retrieve the unchanged orb | world exit restores access to the portable role | `COC-004` |
| Orange ability is unlocked, orb is carried and avatar reaches the matching locus | Approach the gap | The invisible bridge manifests and supports traversal | carried world acts as a spatial tool | `COC-005`, `COC-006` |
| Orb is set down at that locus | Re-evaluate the route | The carried-power predicate fails and the bridge becomes unavailable | power depends on current carried state | `COC-007` |

## Strategic and experiential structure

- Local decision: choose whether the single orb should currently be mounted for
  world access or carried for its bridge ability.
- Medium-term planning: leave the inner world at the correct jump point,
  retrieve the orb and transport its now-unlocked function to the next visible
  receptive route.
- Long-term structure: later puzzles place multiple worlds inside one another
  and combine several orb abilities, but those relations are deliberately
  excluded from this first transfer test.
- Common heuristics: track orb colour and identity; distinguish the world-entry
  pedestal from ordinary set-down; reason explicitly about mounted versus
  carried state; test the orange orb near visually implied gaps.
- Failure attribution: a mismatched mount is refused, an unmounted orb exposes
  no jump surface, and a missing bridge follows from visible carried / unlock /
  locus state rather than randomness.
- Player-trust factors: the same colour, orb pose, jump pool, arrival framing
  and bridge manifestation must make each identity and state transition legible.

## Replay and variation

- Orb identity, contained world, pedestal, jump points, bridge locus and target
  route are authored and fixed. The player's movement and exploratory set-downs
  may vary.
- No randomness or procedural generation affects the bounded packet.
- The successful state sequence is constrained by role exclusivity: mounted for
  entry, carried for ability. Extra walking does not change that logic.
- Replay chiefly shortens exploratory movement or tests the boundary by setting
  down and retrieving the orb at different visible positions.

## Adjacent systems and history

- Patrick's Parabox transfers actors across aligned parent / child grid edges
  and can reparent movable containers. Cocoon mounts a world representation at
  a fixed external jump site; this packet neither aligns box edges nor mutates a
  containment graph.
- Portal lets the player place two apertures on eligible surfaces and maps
  position plus velocity across them. Cocoon exposes one authored orb world at
  one pedestal and preserves ordinary local locomotion after the jump.
- The Room applies discrete inventory items to compatible fixtures and often
  consumes or transforms them. Cocoon's orb remains a continuously carried
  world object, survives mounting and later supplies a carried spatial ability.
- The Pedestrian also alternates an external topology-related state with direct
  traversal, but it creates explicit edges between sign ports rather than
  changing one object's role between world entry and carried route tool.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-048`, `ACT-112` | direct movement; held offset; pedestal gesture |
| System Behaviour | `SYS-144`, `SYS-145` | jump mapping; bridge manifestation |
| Constraint | `CON-162`, `CON-163` | pedestal class; unlock; carried identity; locus |
| Information | `INF-001` | colour coding; jump-pool and bridge feedback |
| Objective | `OBJ-026` | next route location |
| Time | `TIM-002` | pause policy; interaction animation |

## Corpus comparison

- Genome signature `(ACT; SYS; CON; INF; OBJ; TIM)`:
  `(ACT-008,ACT-048,ACT-112; SYS-144,SYS-145; CON-162,CON-163; INF-001; OBJ-026; TIM-002)`.
- Indexed games scanned: 108, including this record.
- Indexed combinations scanned: 108.
- Exact genome matches: none.
- Near matches and similarity scores: `GAME-0040` — Carto and `GAME-0107` —
  The Pedestrian tie at `4 / 14 = 0.285714`. Both share direct avatar movement,
  fully visible state, target-location access and self-paced time; Carto turns
  map layout directly into world adjacency, while The Pedestrian separately
  constructs typed panel links. Neither gives one carried object a persistent
  identity as both enterable world and conditional route tool.
- Supported combination subsets: `COMB-0108` only.
- Scan date: 2026-08-15.

### Full prior-game Jaccard scan

- `GAME-0001`: `1 / 23 = 0.043478`; `GAME-0002`: `2 / 15 = 0.133333`; `GAME-0003`: `0 / 19 = 0.000000`; `GAME-0004`: `1 / 24 = 0.041667`.
- `GAME-0005`: `2 / 15 = 0.133333`; `GAME-0006`: `3 / 16 = 0.187500`; `GAME-0007`: `2 / 16 = 0.125000`; `GAME-0008`: `2 / 15 = 0.133333`.
- `GAME-0009`: `1 / 25 = 0.040000`; `GAME-0010`: `1 / 18 = 0.055556`; `GAME-0011`: `2 / 21 = 0.095238`; `GAME-0012`: `2 / 17 = 0.117647`.
- `GAME-0013`: `1 / 22 = 0.045455`; `GAME-0014`: `1 / 24 = 0.041667`; `GAME-0015`: `1 / 23 = 0.043478`; `GAME-0016`: `1 / 24 = 0.041667`.
- `GAME-0017`: `0 / 23 = 0.000000`; `GAME-0018`: `1 / 28 = 0.035714`; `GAME-0019`: `1 / 19 = 0.052632`; `GAME-0020`: `1 / 23 = 0.043478`.
- `GAME-0021`: `1 / 18 = 0.055556`; `GAME-0022`: `1 / 21 = 0.047619`; `GAME-0023`: `1 / 19 = 0.052632`; `GAME-0024`: `1 / 21 = 0.047619`.
- `GAME-0025`: `1 / 20 = 0.050000`; `GAME-0026`: `1 / 21 = 0.047619`; `GAME-0027`: `1 / 21 = 0.047619`; `GAME-0028`: `1 / 26 = 0.038462`.
- `GAME-0029`: `2 / 20 = 0.100000`; `GAME-0030`: `1 / 23 = 0.043478`; `GAME-0031`: `1 / 20 = 0.050000`; `GAME-0032`: `1 / 20 = 0.050000`.
- `GAME-0033`: `3 / 20 = 0.150000`; `GAME-0034`: `2 / 22 = 0.090909`; `GAME-0035`: `2 / 26 = 0.076923`; `GAME-0036`: `3 / 19 = 0.157895`.
- `GAME-0037`: `1 / 18 = 0.055556`; `GAME-0038`: `2 / 24 = 0.083333`; `GAME-0039`: `2 / 17 = 0.117647`; `GAME-0040`: `4 / 14 = 0.285714`.
- `GAME-0041`: `2 / 19 = 0.105263`; `GAME-0042`: `1 / 18 = 0.055556`; `GAME-0043`: `2 / 22 = 0.090909`; `GAME-0044`: `2 / 18 = 0.111111`.
- `GAME-0045`: `2 / 22 = 0.090909`; `GAME-0046`: `2 / 18 = 0.111111`; `GAME-0047`: `1 / 23 = 0.043478`; `GAME-0048`: `1 / 23 = 0.043478`.
- `GAME-0049`: `0 / 19 = 0.000000`; `GAME-0050`: `2 / 23 = 0.086957`; `GAME-0051`: `1 / 25 = 0.040000`; `GAME-0052`: `1 / 19 = 0.052632`.
- `GAME-0053`: `2 / 17 = 0.117647`; `GAME-0054`: `3 / 18 = 0.166667`; `GAME-0055`: `3 / 17 = 0.176471`; `GAME-0056`: `1 / 17 = 0.058824`.
- `GAME-0057`: `1 / 17 = 0.058824`; `GAME-0058`: `1 / 18 = 0.055556`; `GAME-0059`: `1 / 16 = 0.062500`; `GAME-0060`: `1 / 16 = 0.062500`.
- `GAME-0061`: `2 / 18 = 0.111111`; `GAME-0062`: `2 / 16 = 0.125000`; `GAME-0063`: `2 / 15 = 0.133333`; `GAME-0064`: `2 / 13 = 0.153846`.
- `GAME-0065`: `1 / 16 = 0.062500`; `GAME-0066`: `1 / 19 = 0.052632`; `GAME-0067`: `0 / 18 = 0.000000`; `GAME-0068`: `1 / 17 = 0.058824`.
- `GAME-0069`: `2 / 16 = 0.125000`; `GAME-0070`: `1 / 17 = 0.058824`; `GAME-0071`: `2 / 15 = 0.133333`; `GAME-0072`: `2 / 16 = 0.125000`.
- `GAME-0073`: `2 / 15 = 0.133333`; `GAME-0074`: `2 / 17 = 0.117647`; `GAME-0075`: `2 / 17 = 0.117647`; `GAME-0076`: `2 / 15 = 0.133333`.
- `GAME-0077`: `2 / 15 = 0.133333`; `GAME-0078`: `2 / 15 = 0.133333`; `GAME-0079`: `2 / 15 = 0.133333`; `GAME-0080`: `2 / 15 = 0.133333`.
- `GAME-0081`: `2 / 16 = 0.125000`; `GAME-0082`: `2 / 16 = 0.125000`; `GAME-0083`: `2 / 16 = 0.125000`; `GAME-0084`: `2 / 18 = 0.111111`.
- `GAME-0085`: `1 / 20 = 0.050000`; `GAME-0086`: `2 / 21 = 0.095238`; `GAME-0087`: `1 / 19 = 0.052632`; `GAME-0088`: `2 / 17 = 0.117647`.
- `GAME-0089`: `1 / 18 = 0.055556`; `GAME-0090`: `3 / 22 = 0.136364`; `GAME-0091`: `3 / 16 = 0.187500`; `GAME-0092`: `1 / 19 = 0.052632`.
- `GAME-0093`: `3 / 16 = 0.187500`; `GAME-0094`: `3 / 17 = 0.176471`; `GAME-0095`: `3 / 19 = 0.157895`; `GAME-0096`: `3 / 17 = 0.176471`.
- `GAME-0097`: `3 / 15 = 0.200000`; `GAME-0098`: `3 / 14 = 0.214286`; `GAME-0099`: `2 / 16 = 0.125000`; `GAME-0100`: `0 / 21 = 0.000000`.
- `GAME-0101`: `2 / 18 = 0.111111`; `GAME-0102`: `1 / 16 = 0.062500`; `GAME-0103`: `1 / 18 = 0.055556`; `GAME-0104`: `3 / 16 = 0.187500`.
- `GAME-0105`: `2 / 18 = 0.111111`; `GAME-0106`: `1 / 16 = 0.062500`; `GAME-0107`: `4 / 14 = 0.285714`.

- New genes: `ACT-112`, `SYS-144`, `SYS-145`, `CON-162`, `CON-163`.
- Classification result: `New gene` and `New combination of known and new genes`.
- Evidence and reasoning: the corpus already represented avatar navigation,
  physical carrying, visible state, target-location access, self-paced play,
  recursive grid containers and placed portals. It did not represent one stable
  portable object that becomes its contained world's authored entry when
  mounted, then becomes a different world-specific spatial tool when retrieved
  and carried under an unlock-plus-locus predicate.

## Taxonomy impact

- Registry changes: five Active IDs and five transfers to a new game.
- Taxonomy-change record: none; no previous gene is merged, split or retired.
- Candidate terms affected: world-orb mounting, mounted contained-world entry,
  carried orb ability manifestation, mount-gated entry and unlock / carry /
  locus ability gating.

## Negative results

- `SYS-069` / `CON-082` rejected: Cocoon does not cross aligned centre cells of
  a movable grid container.
- `SYS-070` rejected in this packet: mounting and carrying the orange orb does
  not reparent it into another world; later recursive suitcasing is excluded.
- `ACT-047`, `SYS-059`, `SYS-060` and `CON-078` rejected: the jump point is
  authored by the mounted orb and pedestal, not a player-fired portal pair with
  surface eligibility or velocity transformation.
- `ACT-087` and `SYS-112` rejected: the orb is a persistent world object, not a
  discrete inventory item consumed by a fixture to reveal a one-shot reward.
- `SYS-113` / `OBJ-044` rejected: the ability belongs to the orb and is
  conditional on carrying it, not a permanent avatar component.

## Delta summary

## Нові факти

- [Confirmed | Corroborated | High] Одна сфера Cocoon зберігає спільну
  ідентичність як переносний об’єкт, вхід до вміщеного світу на п’єдесталі та
  носій умовної здатності після повернення (`COC-002`–`COC-007`).

## Нові гени

- [Observation | Corroborated | High] `ACT-112` — встановити або забрати
  переносну сферу-світ з п’єдесталу.
- [Observation | Corroborated | High] `SYS-144` — перетворити встановлену сферу
  на оборотний вхід до її світу; `SYS-145` — проявити просторову структуру від
  здатності сфери, яку несуть.
- [Observation | Corroborated | High] `CON-162` — вхід потребує сумісної
  встановленої сфери; `CON-163` — здатність потребує розблокованої саме цієї
  сфери в руках і сумісної ділянки.

## Нові комбінації

- [Confirmed | Corroborated | High] `COMB-0108` — увійти до переносного світу,
  повернутися й використати ту саму сферу як умовний інструмент маршруту.

## Зміни таксономії

- [Observation | Corroborated | High] Змін таксономії немає.

## Нові питання

- Чи переноситься пізнє suitcasing кількох сфер на `SYS-070`, чи потребує
  окремої межі для входу до світу, що сам міститься в іншому переносному світі?

## Наступна рекомендована гра

- [Hypothesis | Limited | Medium] Lorelei and the Laser Eyes, лише після
  дев’ятиігрового batch-аудиту.
- Optimisation criterion: перевірити, чи поєднуються розподілені коди,
  метадокументи й взаємозалежні інтерфейси без дублювання недавніх архівних та
  текстових генів.
- Expected information gain: stress-test evidence integration and revisable
  cross-room knowledge without ще одного carried-world family.
- Backlog impact: зберегти пізню рекурсію Cocoon для окремого boundary audit,
  а не розширювати цей ранній пакет.

## Чому саме вона

- [Hypothesis | Limited | Medium] Після аудиту дев’яти дуже різних ігор Lorelei
  може перевірити перенесення фактів між кількома авторськими системами без
  повторення world-orb, free-text archive або fixed-code структури.
