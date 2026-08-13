---
game_id: GAME-0038
slug: the-swapper
game_title: The Swapper
analysis_status: reviewed
reviewed: 2026-08-12
combination_ids:
  - COMB-0038
gene_ids:
  action:
    - ACT-008
    - ACT-054
    - ACT-055
  system:
    - SYS-036
    - SYS-037
    - SYS-061
    - SYS-071
    - SYS-072
  constraint:
    - CON-031
    - CON-083
    - CON-084
    - CON-085
    - CON-086
  information:
    - INF-001
  objective:
    - OBJ-025
  time:
    - TIM-003
---

# Game: The Swapper

## Analysis scope

- Version / ruleset: the 2013 Facepalm Games base game, scoped to one ordinary
  authored puzzle room after both functions of the Swapper Device are
  available.
- Included: direct walking and jumping; aimed creation of at most four clones;
  simultaneous shared movement; local collision and gravity; line-of-sight
  control transfer; active-body device authority; red, blue and purple light
  restrictions; pressure-held mechanisms; clone removal and slot recovery;
  contact collection of the room's fixed orb; real-time aiming slowdown.
- Excluded: narrative interpretation, exploration-only corridors, reverse-
  gravity and teleport variants, whole-campaign orb completion, endings,
  hidden terminals, achievements and platform-specific presentation.
- Direct-play status: not conducted. Facepalm's official description and the
  PlayStation port announcement establish cloning and control transfer;
  contemporary GameSpot, Nintendo Life and Pocket Gamer accounts independently
  document the cap, synchronization, line of sight, coloured fields, removal,
  gravity-sensitive play, orb progression and slowdown. MobyGames' archived
  official description corroborates active-body-only device use and pressure
  plates.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `SWP-001` | The active body can walk and jump in a continuously simulated side-view room | Confirmed | Corroborated | High | S1–S3 |
| `SWP-002` | The device creates a clone at an aimed unobstructed valid position without traversing the intervening space | Confirmed | Corroborated | High | P1–P3, S1 |
| `SWP-003` | At most four created clones coexist in ordinary play | Confirmed | Direct | High | P2, S1–S3 |
| `SWP-004` | Every extant body receives the same movement and jump input, then walls, supports and gravity resolve each body locally | Confirmed | Corroborated | High | S1–S3 |
| `SWP-005` | The player can transfer the unique direct-control locus to an existing clone only through a clear targeting line | Confirmed | Corroborated | High | P1–P3, S1–S3 |
| `SWP-006` | Only the body holding that locus can originate clone creation or another swap; the former active body persists after transfer | Confirmed | Corroborated | High | P3, S2 |
| `SWP-007` | Blue light blocks clone creation, red blocks control transfer and purple blocks both while ordinary movement remains available | Confirmed | Corroborated | High | S1–S3 |
| `SWP-008` | Bodies hold linked mechanisms active by pressure occupancy, allowing clones to maintain distinct spatial requirements | Confirmed | Corroborated | High | P3, S4 |
| `SWP-009` | Clone contact, lethal loss or white cleansing light removes a clone and restores creation capacity | Confirmed | Corroborated | High | S1, S2 |
| `SWP-010` | Reaching a room orb credits puzzle progress used to open later station routes | Confirmed | Corroborated | High | S1, S4 |
| `SWP-011` | Aiming the device slows rather than freezes world time, so airborne creation and transfer remain live precision actions | Confirmed | Corroborated | High | S2, S3 |
| `SWP-012` | Geometry, bodies, lights, mechanisms, orb and current locus are visible; the scoped room has no hidden random transition | Observation | Corroborated | High | SWP-001–SWP-011 |
| `SWP-013` | Control-locus transfer is not Pikmin 4 leader switching because both bodies are mechanically identical members of one synchronized set and the old locus-holder becomes an ordinary clone | Observation | Corroborated | High | SWP-004–SWP-006 |
| `SWP-014` | Shared-input bodies are not autonomous locomotors: all displacement attempts originate in live player movement input | Observation | Corroborated | High | SWP-001, SWP-004 |

## Basic data

- Release / origin: Facepalm Games released The Swapper for PC in May 2013;
  the credited creators include Olli Harjola, Otto Hantula, Tom Jubert and
  Carlo Castellano.
- Platform or physical form: single-player, real-time 2D physics puzzle game
  controlled through avatar movement plus an aimed clone / swap device.
- Puzzle family: synchronized-body spatial coordination and control-locus
  transfer.
- Primary and official sources:
  - **[P1]** [Facepalm Games official page](https://facepalmgames.com/the-swapper),
    describing a device that clones its user and swaps control between bodies.
  - **[P2]** [PlayStation announcement by Curve Studios](https://blog.playstation.com/2014/02/26/the-swapper-coming-to-ps3-ps4-ps-vita-in-may/),
    made with original developer Olli Harjola, specifying up to four clones and
    switching between them to solve puzzles.
  - **[P3]** [GOG official product description](https://www.gog.com/en/game/the_swapper),
    preserving Facepalm's description of clone creation and control swapping;
    MobyGames' archived official description supplies the finer input, plate
    and coloured-light rules.
- Contemporary corroboration:
  - **[S1]** [GameSpot review, 28 May 2013](https://www.gamespot.com/reviews/the-swapper-review/1900-6408976/),
    documenting placement line of sight, four-clone cap, shared movement,
    absorption / death, swap line of sight, light channels, gravity and orbs.
  - **[S2]** [Nintendo Life review, 10 November 2014](https://www.nintendolife.com/reviews/wiiu-eshop/swapper),
    corroborating synchronized input, active-body-only device use, removal,
    coloured lights, slowdown and orb-gated progress.
  - **[S3]** [Pocket Gamer review, 28 July 2014](https://www.pocketgamer.com/the-swapper/review/),
    corroborating aimed visible-range creation, four clones, simultaneous
    motion, control transfer, slowdown and blue / red restrictions.
  - **[S4]** [MobyGames description](https://www.mobygames.com/game/62509/the-swapper/),
    archiving the official mechanical account of shared inputs, active-body
    device authority, pressure plates and coloured light restrictions.
- Claim IDs: `SWP-001`–`SWP-014`.

## Mechanical decomposition

### Action Genes

- `ACT-008` — navigate directly controlled avatar. Horizontal movement and
  jumping originate from live player input at the current control locus.
- `ACT-054` — instantiate body at aimed reachable position. The active body
  aims the device and creates a clone directly at a legal unobstructed point.
- `ACT-055` — transfer direct-control locus to targeted body. A valid swap
  makes the chosen clone active while leaving the former body in the shared
  synchronized set.
- `ACT-052` is absent: Pikmin 4 switches follower-command authority among
  distinct persistent field leaders. The Swapper transfers one exclusive
  device locus among otherwise identical bodies and changes the old body into
  an ordinary synchronized member.
- Claim IDs: `SWP-001`–`SWP-006`, `SWP-013`.

### System Behaviour Genes

- `SYS-036` — continuous force-constrained body dynamics. Each body falls,
  jumps, lands, collides and can suffer a lethal drop while world time runs.
- `SYS-037` — contact-triggered collectible acquisition. The active body
  touching the fixed orb removes and credits it as room progress.
- `SYS-061` — occupancy-sustained linked mechanism state. A body held on a
  pressure plate maintains its linked door or mechanism until it moves away.
- `SYS-071` — local-resolution divergence under shared body input. The same
  movement attempt reaches all bodies, but each resolves against its own wall,
  floor and gravity situation; separation is therefore authored through
  asymmetric geometry rather than separate unit commands.
- `SYS-072` — clone-body removal with capacity recovery. Absorption, lethal
  loss or white cleansing light deletes a non-active clone and returns its
  finite slot.
- `SYS-045` is absent: clones never choose or advance an autonomous route;
  their motion is a direct response to shared player input.
- Resolution order: accept live input from the active locus; broadcast movement
  / jump channels to the controlled set; resolve every body's local physics and
  collisions; update plate-held mechanisms and removal triggers; resolve valid
  device creation or locus transfer; credit active-body orb contact.
- Claim IDs: `SWP-001`, `SWP-004`, `SWP-008`–`SWP-011`, `SWP-014`.

### Constraint Genes

- `CON-031` — shared-input simultaneous controllability. Every extant body is
  in the movement-controlled set even though only one carries device authority.
  This generalises the gene beyond Baba Is You's rule-assigned classes without
  treating the bodies as autonomous followers.
- `CON-083` — finite created-body capacity. Four clone slots bound the spatial
  arrangement and become reusable only after body removal.
- `CON-084` — unobstructed targeting path for remote body operation. Walls
  block both aimed creation beyond them and swapping to a hidden clone.
- `CON-085` — region-specific action-channel suppression. Blue, red and purple
  light fields suppress cloning, swapping or both as separate channels.
- `CON-086` — active-body-exclusive device authority. Synchronized bodies all
  move, but only the current locus-holder originates creation and transfer.
- `CON-076` is absent: the bodies have no persistent actor-class traversal or
  interaction differences. Device privilege follows a transferable locus, not
  a character type.
- Scarce strategic resources: four renewable clone slots, distinct support
  positions, clear targeting lines and access to each unsuppressed device
  channel.
- Claim IDs: `SWP-003`–`SWP-009`, `SWP-013`, `SWP-014`.

### Information Genes

- `INF-001` — fully visible current state. The scoped room exposes body
  positions, solid geometry, coloured action fields, pressure mechanisms, orb
  and active-body locus; no hidden random event alters the room.
- Aim feedback is a presentation parameter, not a separate preview gene: legal
  outcomes follow from visible geometry, range, light fields and current cap.
- Claim IDs: `SWP-002`, `SWP-007`, `SWP-008`, `SWP-012`.

### Objective Genes

- `OBJ-025` — acquire fixed puzzle-gated progress token. The room is credited
  when the privileged active body reaches its authored orb after the clone /
  mechanism arrangement has made it accessible.
- `OBJ-018` is absent at scoped room level: the analysis excludes completion of
  the campaign's finite orb collection. `OBJ-022` is absent because clones need
  not all survive or reach a fixed exit and may be deliberately removed.
- Claim IDs: `SWP-009`, `SWP-010`.

### Time Genes

- `TIM-003` — real-time input during forced progression. Gravity, falling and
  collision continue while movement, creation and swapping remain available;
  aiming slows the rate but does not convert the room to discrete turns or a
  stopped planning phase.
- Slow motion is a rate parameter of `TIM-003`, not a new Time Gene. There is
  no branchable history (`TIM-007`) or design-then-locked execution phase
  (`TIM-009`).
- Claim IDs: `SWP-001`, `SWP-004`, `SWP-011`.

## Reproducible transitions

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Active body has a free clone slot and clear aimed point | Create clone | New body appears at the aimed legal point without path traversal | aimed body instantiation | `SWP-002`, `SWP-003` |
| Several bodies stand on different supports | Hold a direction or jump | Every body receives the input; each local collision / gravity state resolves separately | shared control plus local divergence | `SWP-004` |
| Visible clone is unobstructed | Fire swap beam at it | Control and camera locus transfer; old body persists and continues receiving shared movement | locus transfer, not leader switch | `SWP-005`, `SWP-006` |
| Target point lies behind solid wall | Attempt create or swap through wall | Remote operation is rejected while ordinary movement continues | targeting-path constraint | `SWP-002`, `SWP-005` |
| Target lies in blue, red or purple light | Attempt affected device action | Blue rejects creation, red rejects swapping, purple rejects both | channel-specific field permissions | `SWP-007` |
| Clone occupies a plate | Move synchronized set so it leaves | Linked mechanism returns inactive unless another eligible body remains | occupancy-held state | `SWP-008` |
| Four clone slots are occupied | Create a fifth, then remove one clone and retry | First creation fails; removal refunds capacity and retry can succeed | finite renewable body capacity | `SWP-003`, `SWP-009` |
| Active body is falling while device is aimed | Hold aim and create / swap | World slows but gravity continues; the input must resolve before unsafe contact | live time with dilation | `SWP-011` |
| Orb becomes reachable | Move the active body into it | Orb is removed and room progress is credited | fixed puzzle-token objective | `SWP-010` |

## Parameter sheet

- Clone capacity: four created clones simultaneously; whether the locus-holder
  was originally created does not alter the four-slot pool.
- Targeting: finite aimed visible range with solid-geometry occlusion; exact
  boundary tolerance and input-device sensitivity are platform parameters.
- Shared input: horizontal movement and jump offered to all bodies; local
  grounded state, collision and gravity determine each outcome.
- Device locus: unique; transfer changes origin, camera and fatal-body status
  while preserving the former body's position.
- Light mapping: blue blocks creation, red blocks swapping, purple blocks both;
  white cleansing light removes clones.
- Body removal: contact absorption, lethal fall / hazard and cleansing fields;
  exact active-body failure and checkpoint reload are implementation parameters.
- Mechanisms: plate occupancy threshold, linked door state and release order.
- Time: continuous simulation with device-aim slowdown; exact dilation factor is
  not required for the classification.
- Progress: one fixed room orb, credited on eligible active-body contact and
  contributing to later station-gate thresholds.

## Known edge cases

- A blocked body may remain still while an unblocked body moves under the same
  input; this is the core `SYS-071` divergence, not partial loss of `CON-031`.
- A swap changes which body death is terminal and which body can fire the
  device; it does not remove the former body.
- A clone can enter blue light after creation even though a new clone cannot be
  created at a blue-lit target; field evaluation is action-channel-specific.
- Removing a clone is often intentional resource recovery, but losing the
  active locus-holder triggers failure rather than an ordinary slot refund.
- Reverse-gravity fields and teleport streams exist elsewhere in the game but
  are outside this ordinary-room scope and do not enter the signature.

## Strategic and experiential structure

- Local decision: choose where to instantiate the next body or which visible
  body should receive the control locus before the shared movement changes all
  current positions.
- Medium-term planning: use asymmetric walls, ledges and plates to separate
  bodies under common input, while reserving a clear beam path and enough clone
  capacity for the next transfer.
- Long-term structure: construct a distributed body arrangement that holds the
  required mechanisms and leaves the privileged active body a route to the orb.
- Common heuristics: reason from the orb backward; treat blocked clones as
  temporary anchors; preserve one removable body when the cap is tight; test
  creation and swap light channels separately.
- Failure attribution: visible body trajectories, coloured fields and beam
  occlusion usually expose whether failure came from geometry, cap, locus or
  execution timing rather than hidden state.
- Player-trust factors: shared-input ordering, collision resolution, plate
  release, light boundaries, line-of-sight tests and slot refunds must remain
  deterministic under slowdown.
- Claim IDs: `SWP-001`–`SWP-014`.

## Replay and variation

- What changes between puzzles: room geometry, plates and linked mechanisms,
  light-field placement, orb position and later excluded gravity / teleport
  modules.
- Randomness or procedural generation: none in the scoped authored room.
- Multiple viable strategies: some rooms admit alternative clone placements or
  sacrifice orders, though their pressure and light topology often forces the
  important locus sequence.
- Typical replay motive: retry a mistimed airborne transfer, recover clone
  capacity more cleanly or solve previously skipped orb rooms.
- Claim IDs: `SWP-007`–`SWP-012`.

## Adjacent systems and history

- Baba Is You supplies the prior `CON-031` instance: several current objects
  can receive one input. Its membership is authored by mutable `IS YOU` rules;
  The Swapper's membership is the extant clone-body set plus one privileged
  device locus.
- Portal shares direct physics navigation, pressure-held mechanisms, visible
  rooms and live gravity, but its aimed shots create paired apertures on
  eligible surfaces rather than bodies that share input and control locus.
- Pikmin 4 transfers direct play between two distinct leaders with follower
  groups. Its followers walk and work autonomously; The Swapper bodies are
  mechanically identical and move only from shared direct input.
- Cut the Rope shares continuous physics and contact collection, but manipulates
  supports around one indirect payload rather than creating and coordinating a
  synchronized controlled body set.
- Claim IDs: `SWP-001`–`SWP-014`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-054`, `ACT-055` | navigation, aimed body creation and locus transfer |
| System Behaviour | `SYS-036`, `SYS-037`, `SYS-061`, `SYS-071`, `SYS-072` | physics, orb contact, plates, local divergence and clone recovery |
| Constraint | `CON-031`, `CON-083`, `CON-084`, `CON-085`, `CON-086` | shared input, cap, line of sight, fields and active-body authority |
| Information | `INF-001` | visible deterministic room state |
| Objective | `OBJ-025` | acquire the fixed room-progress orb |
| Time | `TIM-003` | live physics with aim slowdown |

Canonical signature:

`ACT-008,ACT-054,ACT-055; SYS-036,SYS-037,SYS-061,SYS-071,SYS-072; CON-031,CON-083,CON-084,CON-085,CON-086; INF-001; OBJ-025; TIM-003`

## Corpus comparison

- Indexed games scanned: `GAME-0001`–`GAME-0037`.
- Indexed combinations scanned: `COMB-0001`–`COMB-0037`.
- Exact genome matches: none.
- Existing combination subsets: none before registering `COMB-0038`.
- Full Jaccard scan (intersection / union = score):
  `GAME-0001` `1 / 29 = 0.034483`; `GAME-0002` `1 / 22 = 0.045455`;
  `GAME-0003` `0 / 25 = 0.000000`; `GAME-0004` `2 / 29 = 0.068966`;
  `GAME-0005` `1 / 22 = 0.045455`; `GAME-0006` `2 / 23 = 0.086957`;
  `GAME-0007` `1 / 23 = 0.043478`; `GAME-0008` `1 / 22 = 0.045455`;
  `GAME-0009` `1 / 31 = 0.032258`; `GAME-0010` `1 / 24 = 0.041667`;
  `GAME-0011` `1 / 28 = 0.035714`; `GAME-0012` `1 / 24 = 0.041667`;
  `GAME-0013` `2 / 27 = 0.074074`; `GAME-0014` `1 / 30 = 0.033333`;
  `GAME-0015` `1 / 29 = 0.034483`; `GAME-0016` `2 / 29 = 0.068966`;
  `GAME-0017` `0 / 29 = 0.000000`; `GAME-0018` `2 / 33 = 0.060606`;
  `GAME-0019` `1 / 25 = 0.040000`; `GAME-0020` `1 / 29 = 0.034483`;
  `GAME-0021` `4 / 21 = 0.190476`; `GAME-0022` `1 / 27 = 0.037037`;
  `GAME-0023` `0 / 26 = 0.000000`; `GAME-0024` `1 / 27 = 0.037037`;
  `GAME-0025` `2 / 25 = 0.080000`; `GAME-0026` `3 / 25 = 0.120000`;
  `GAME-0027` `2 / 26 = 0.076923`; `GAME-0028` `2 / 31 = 0.064516`;
  `GAME-0029` `3 / 25 = 0.120000`; `GAME-0030` `3 / 27 = 0.111111`;
  `GAME-0031` `1 / 26 = 0.038462`; `GAME-0032` `1 / 26 = 0.038462`;
  `GAME-0033` `5 / 24 = 0.208333`; `GAME-0034` `4 / 26 = 0.153846`;
  `GAME-0035` `3 / 31 = 0.096774`; `GAME-0036` `2 / 26 = 0.076923`;
  `GAME-0037` `1 / 24 = 0.041667`.
- Mathematical near match: `GAME-0033` — Portal at
  `5 / 24 = 0.208333`, sharing avatar navigation, continuous physics,
  occupancy-held mechanisms, visible room state and live input. Portal's
  replaceable paired apertures transform body position and velocity; The
  Swapper instead creates a bounded synchronized body set and moves the unique
  control locus between its members.

## Combination record

- Registered `COMB-0038` — synchronized clone-body locus coordination.
- Its ten-gene proper subset isolates creation, transfer, synchronized local
  divergence, renewable body capacity and device permissions without requiring
  general avatar navigation, orb collection, pressure mechanisms, visibility
  or the particular room objective.

## Taxonomy impact

- Registry changes: nine stable genes added: `ACT-054`, `ACT-055`, `SYS-071`,
  `SYS-072`, `CON-083`–`CON-086` and `OBJ-025`.
- Seven genes are reused unchanged in classification: `ACT-008`, `SYS-036`,
  `SYS-037`, `SYS-061`, `CON-031`, `INF-001` and `TIM-003`.
- `CON-031` receives a representation-neutral wording generalisation from
  rule-assigned classes to any current shared-input controlled set. Its prior
  Baba Is You instance remains inside the boundary; no earlier signature or
  lifecycle changes.

## Negative results

- `ACT-052` is rejected because this is a transferable unique locus among
  identical synchronized bodies, not switching persistent typed field leaders.
- `SYS-045` is rejected because clones do not locomote autonomously.
- `CON-076` is rejected because permissions follow the active locus and light
  regions rather than persistent actor classes.
- `OBJ-018` and `OBJ-022` are rejected because the scoped unit credits one room
  orb and neither requires the campaign's complete set nor every body at an
  exit.
- Slowdown remains a `TIM-003` parameter rather than a separate Time Gene.

## Delta summary

## Нові факти

- [Confirmed | Corroborated | High] One input drives all extant bodies, but
  local geometry and physics let their trajectories diverge (`SWP-004`).
- [Confirmed | Corroborated | High] The unique device locus can move to a
  clone while the old body persists, separating locus transfer from leader
  switching (`SWP-005`, `SWP-006`, `SWP-013`).

## Нові гени

- [Observation | Corroborated | High] Added nine bounded genes for aimed body
  creation, locus transfer, local shared-input resolution, renewable clone
  removal, clone cap, line of sight, action-channel fields, exclusive device
  authority and one-room progress-token acquisition.

## Нові комбінації

- [Observation | Corroborated | High] Registered `COMB-0038`; no existing
  game supports its synchronized clone-body core.

## Зміни таксономії

- [Observation | Corroborated | High] Generalised `CON-031` wording to shared-
  input controlled sets while preserving Baba Is You and adding The Swapper;
  no merge, split or earlier signature rewrite was required.

## Нові питання

- Can a later game recur `ACT-055` without clone creation, proving that control-
  locus transfer is independent of instantiation?
- Does The Witness now offer more information gain than another physics-heavy
  subject after Portal, Braid and The Swapper?

## Наступна рекомендована гра

- [Hypothesis | Corroborated | High] `GAME-0039` — The Witness.
- Optimisation criterion: move from a dense real-time physics cluster to a
  mechanically independent panel-line grammar while testing route constraints.
- Expected information gain: separate line drawing as action from symbol-
  constrained region partition, path coverage and panel validation.
- Backlog impact: retain Viewfinder and Carto; schedule checkpoint 040 after
  two further games unless registry density or taxonomy evidence warrants an
  earlier audit.

## Sources consulted

- Official Facepalm Games page, GOG description and Curve / PlayStation
  announcement.
- Contemporary GameSpot, Nintendo Life and Pocket Gamer reviews plus the
  archived MobyGames official description.
