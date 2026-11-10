---
game_id: GAME-0495
slug: donkey-kong-country-returns
game_title: Donkey Kong Country Returns
analysis_status: reviewed
reviewed: 2026-10-04
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-048
    - ACT-202
    - ACT-295
    - ACT-667
    - ACT-668
  system:
    - SYS-036
    - SYS-037
    - SYS-045
    - SYS-064
    - SYS-112
    - SYS-215
    - SYS-755
    - SYS-910
    - SYS-911
    - SYS-933
    - SYS-935
    - SYS-1056
    - SYS-1332
    - SYS-1333
    - SYS-1334
    - SYS-1335
    - SYS-1336
    - SYS-1337
    - SYS-1338
  constraint:
    - CON-442
  information:
    - INF-469
  objective:
    - OBJ-283
  time:
    - TIM-003
---

# Game: Donkey Kong Country Returns

Use the canonical [vocabulary and signature](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
Character names, controller mapping, authored collectible counts and destinations
are parameters, not additional genes.

## Analysis scope

- Version / ruleset: original North American English 2010 Wii game, fresh
  Single Player save, ordinary unassisted Jungle Hijinxs 1-1; no purchased
  Cranky items. Original USA Nintendo booklet 72319A and contemporary original
  Wii written testimony define the target, not a locally executed binary.
  Use Wii Remote plus Nunchuk; the horizontal Remote is an alternative mapping,
  not another ability set. No exact disc hash, region parity, patch or HD claim.
- Structured analysis target: `PLAT-NINTENDO-WII` in the matching `analysisTarget`;
  broader release audit is explicitly not started.
- Primary decision loop: read nearby terrain, enemy motion, hearts and
  collection state; select compatible movement, jump, posture, attack, barrel
  carry/throw, blow or occupied-cannon launch; resolve contact, local reward,
  attachment/loss, fall or finite-life return; repeat through final slot
  settlement and independently banked stage-clear/collection state.
- Entry and exit: first direct control after the fresh introductory sequence
  through the ordinary Slot Machine Barrel result and returned clear map, or
  abandonment/life-stock exhaustion. Include the entire first stage and all
  optional branches, not just the shortest walk to its exit.
- Included: initial hoard cave, treetops, underground recesses, revealed
  background and return, collection bonus room, and hidden area beyond the
  final barrel; four K-O-N-G letters and nine puzzle pieces are available but
  not mandatory for ordinary clear. Solo/attached-Diddy states, variable held
  jump, crouch, roll/pound, eligible barrel pickup/throw, environmental blow,
  stomp/rebound, spring-flower bounce, fixture activation/destruction, preset
  manual/automatic launch, enemy contact/stun, healing, bananas/coins/balloons,
  checkpoint, local bonus expiry/retry, asymmetric collectible rollback,
  exit reward and map closeout all remain available. Pause/resume is a clock
  parameter; quitting is terminal for this packet's unbanked credit.
- Excluded: co-op direct Diddy/popgun or partner return, eligible cling
  geometry documented in 1-2 rather than the admitted 1-1 route, Rambi in 1-3,
  later mine carts/rockets/bosses, shops, subsequent stages, Time Attack,
  Mirror, 3DS New Mode and HD. No universal double jump or unlimited flight.
  Enough failures may offer Super Guide, but activating it leaves the
  unassisted packet; automated Super Kong, its noncollecting takeover and
  different clear colour are not ordinary unassisted victory. No invented
  eight-death threshold, thirty-second bonus timer, damage frames or formula.
- Potential scoped modules: assisted traversal and control takeover;
  co-op partner control/return; later cling or vehicle routes; Time Attack.
- Direct-play status: not conducted. Original USA manual English printed
  pp. 3–22 inspected as text and pixels. Contemporary original Wii author
  routes and written first-hand play reports corroborate availability.
  Retention granularity has Limited/Medium player testimony, not a native save
  experiment. No disc, emulator, save, video or audio was executed.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| DKR-001 | Original Wii Single Player supports the declared ordinary first-stage packet | Observation | Corroborated | High | P1 pp. 7–12; P2; P3 original Wii introduction |
| DKR-002 | Direct movement, variable jump, crouch, roll/pound, blow and barrel carry have compatible inputs | Observation | Corroborated | High | P1 pp. 3–6, 13–18; P3 controls; P4 1-1 |
| DKR-003 | Attached Diddy adds hearts, brief hover and continuous roll; buffer loss removes those abilities without manual switching | Observation | Corroborated | High | P1 pp. 13–16; P2; P5 single-player account |
| DKR-004 | Rolling off support preserves a jump; this is not a universal double jump | Observation | Corroborated | High | P1 p. 22; P3 and P4 O route |
| DKR-005 | The complete 1-1 has authored optional branches, fixture/blow rewards, local collection groups and nine pieces | Observation | Corroborated | High | P3 1-1; P4 1-1 |
| DKR-006 | Manual and automatic preset barrels connect foreground/background and return | Observation | Corroborated | High | P1 pp. 17–18; P3 and P4 background route |
| DKR-007 | Bonus collection has a local deadline and failed retry requires route reset, not immediate re-entry | Observation | Corroborated | Medium | P3 and P4 complete bonus set; P6 timed-room/retry testimony |
| DKR-008 | Finite lives, healing, banana milestone and checkpoint govern ordinary loss/return | Observation | Corroborated | High | P1 pp. 11, 17–19; P3 and P4 checkpoint |
| DKR-009 | Letters roll back by checkpoint while pieces survive ordinary death; pre-clear quit/game-over loses new collection | Observation | Limited | Medium | P7 original dated player testimony; P1 p. 19 supports clear-dependent letter credit |
| DKR-010 | Timed slot grab settles reward; DK class randomises item and permits shake-dependent quantity | Observation | Direct | High | P1 p. 17 |
| DKR-011 | Ordinary clear opens the next route with independent optional collection icons; assisted colour differs | Observation | Corroborated | High | P1 pp. 9–10, 21; P3 and P4 ordinary finish |
| DKR-012 | Play/pause disclose current hearts and separate counters without revealing every secret | Observation | Corroborated | Medium | P1 pp. 9–12; P3 and P4 local route; P6 bonus clock |
| DKR-013 | Every lower-ID signature and verified proper combination subset is scanned without changing prior genomes | Observation | Direct | High | canonical comparator |

## Basic data

- Release / origin: Retro Studios / Nintendo, original Wii 2010. The preserved
  US booklet is copyright 2010 and printed October 2010; its PDF timestamp is
  not an executable version. The official UK product page's December release
  date identifies that region, not North American disc parity.
- Platform or physical form: authorised Nintendo Wii disc, Wii Remote plus
  Nunchuk; structured authority `PLAT-NINTENDO-WII`.
- Puzzle family: existing `FAM-007` physics and objects, `FAM-009` tactical
  forecast/counterplay, `FAM-010` real-time pressure and `FAM-017` ordered
  dependencies: jumps/throws, unsafe contact, live motion and local reward
  prerequisites each alter the decision. No new one-carrier family.
- Primary sources, checked 2026-10-04: **P1**, [original USA Nintendo manual](https://csassets.nintendo.com/noaext/image/private/t_KA_PDF/Wii_DKC_Returns?_a=DATAg1AAZAA0),
  booklet 72319A, original English rules/screens/controls/items/help, printed
  pp. 3–22, text and page pixels. **P2**, [official original Wii product information](https://www.nintendo.com/en-gb/Games/Wii/Donkey-Kong-Country-Returns-280968.html),
  publisher description corroborating attached hover/roll; whole-game vehicles
  are not evidence of first-stage availability.
  **P3**, ResidentEvil4DS's original Wii guide v0.55, created November 21 and
  updated November 29, 2010: [original nominal Wii source](https://gamefaqs.gamespot.com/wii/997764-donkey-kong-country-returns/faqs/61333)
  was inaccessible, but its original authored Wii text was read in the
  [crosslisted HD wrapper](https://gamefaqs.gamespot.com/switch/470857-donkey-kong-country-returns-hd/faqs/61333).
  The wrapper does not turn this dated Wii guide into an HD play test.
  **P4**, [Mitchell Saltzman's first-stage walkthrough](https://www.gamefront.com/news/donkey-kong-country-returns-walkthrough),
  published November 19, 2010, page updated September 22, 2018; written 1-1
  route read, no embedded video played. **P5**, [Chris Atom DeAngelus's first-hand Wii review](https://worthplaying.com/article/2010/12/3/reviews/78618-wii-review-donkey-kong-country-returns/),
  December 3, 2010, independent control/companion/stomp testimony.
  **P6**, [Matt R's original Wii review](https://pixlb.it/review/284/donkey_kong_country_returns_review),
  March 5, 2011, independent bounded bonus/retry account.
  **P7**, [original player collection-retention question and answers](https://gaming.stackexchange.com/questions/13534/if-i-replay-a-level-in-donkey-kong-country-returns-do-i-have-to-collect-kong-aga),
  December 29, 2010 through January 2011: attributed, Limited/Medium,
  not a developer save contract or multiple independent native experiments.
- Secondary sources: no mixed-edition wiki or inaccessible snippet used to
  override P1. A 2013 3DS guide is rejected as original-Wii evidence.
- Claim IDs: `DKR-001`–`DKR-012`.

## Mechanical decomposition

### Action Genes

- Existing gene IDs: `ACT-008`, `ACT-048`, `ACT-202`, `ACT-295` for direct
  walk/run and short/held jump, portable rigid barrel pickup/throw, crouch and
  actionable roll/pound attacks. Attack contact is resolved separately.
- New action genes: `ACT-667` local eligible blow; `ACT-668` choosing the
  occupied arrow cannon's firing instant. Neither adds arbitrary aim/strength.
- Parameters: stick direction, A hold, B/Z held pickup/release, shake posture,
  barrel occupancy and authored destination. Stationary shake pounds;
  moving shake rolls; crouched shake blows. Grasp controls in the manual do
  not prove cling surfaces exist in 1-1; later demonstrated instances excluded.
- Claim IDs: `DKR-002`, `DKR-004`–`DKR-006`.

### System Behaviour Genes

- Existing gene IDs: `SYS-036`, `SYS-037`, `SYS-045`, `SYS-064`, `SYS-112`,
  `SYS-215`, `SYS-755`, `SYS-910`, `SYS-911`, `SYS-933`, `SYS-935`, `SYS-1056`.
  These retain live force/collision, contact collection, autonomous hostile
  motion, qualifying stomp versus unsafe side contact, accepted fixture reveal,
  combat/stun, destruction, typed healing/life pickup, finite-life return,
  checkpoint, hundred-banana life and eligible spring-flower impulse.
- New genes: `SYS-1332` acquired/lost attached ability buffer;
  `SYS-1333` roll-off airborne jump; `SYS-1334` reward for completing a local
  set; `SYS-1335` timed optional bonus and reset-gated failed retry;
  `SYS-1336` asymmetric rollback/banking; `SYS-1337` cycling exit reward;
  `SYS-1338` authored manual/automatic barrel traversal.
- Resolution order: compatible input; movement/attack or barrel trigger;
  physics/contact and eligible enemy/fixture/collectible mutation; companion
  or life consequence; checkpoint-based return with class-specific rollback
  if viable; otherwise termination. A local all-set reward must still be
  acquired. Final exit settles its symbol then stage/map/collection closeout.
  This is source-derived causality, not inspected engine same-frame code.
- Parameters: two DK and two attached-Diddy hearts, one-heart pickup healing,
  ordinary balloons, hundred bananas, checkpoint and collector groups;
  preset cannon kinds and exit symbols. No exact damage windows or random
  distribution. The manual gives five bananas, one coin or one balloon for
  those slot classes; DK quantity's internal formula is unverified.
- Claim IDs: `DKR-003`–`DKR-011`.

### Constraint Genes

- Existing gene ID: `CON-442`, compatible actionable posture, occupied
  launcher and current attachment. This does not make every input available
  while hurt, in a barrel or without Diddy.
- New constraints: none. Finite-life viability is owned by `SYS-911`, not
  duplicated as `CON-183`'s differently bounded complete encounter run.
- Scarce strategic resources: hearts, attached ability buffer, finite lives,
  local bonus time and safe jump opportunities. Coins are collected for later
  shop use; no shop transaction enters this packet.
- Claim IDs: `DKR-002`, `DKR-003`, `DKR-007`, `DKR-008`.

### Information Genes

- New gene: `INF-469`, live geometry/hearts plus pause's separate collection,
  bonus time, cycling slot symbol and independent map flags. No full secret
  map, hidden damage/physics values or future attack schedule.
- Evidence boundary: manual pixels and written play descriptions, not a
  locally observed continuous HUD/bonus-clock sequence; Medium confidence.
- Claim IDs: `DKR-010`–`DKR-012`.

### Objective Genes

- New gene: `OBJ-283`, ordinary stage result and newly available map route
  with independent optional collection credit. All four letters plus finish
  earn the K-O-N-G indicator; all nine pieces have their separate indicator.
  Neither complete set is a requirement for ordinary next-route access.
- Success, evaluation and failure: ordinary final barrel clear settles the
  stage. Incomplete optional sets reduce collection credit, not clear validity;
  life loss can return, quit or exhausted stock abandons unbanked progress.
  Super Guide's assisted colour is not ordinary unassisted completion.
- Claim IDs: `DKR-009`–`DKR-011`.

### Time Genes

- Existing gene ID: `TIM-003`, simultaneous input, enemy and physical motion
  until pause or terminal settlement. Bonus deadline and slot phase are
  instance-specific schedules, not a new gene for an unverified number.
- New time genes: none; whole-stage Time Attack is outside the fresh packet.
- Claim IDs: `DKR-002`, `DKR-007`, `DKR-010`, `DKR-012`.

## Reproducible transitions

These are source-reproducible qualitative tests, not claimed executed tests.

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| First control, initial hoard cave available | Move left before following the main path | First optional piece is reachable | Full route, not shortest traversal | DKR-005 |
| Eligible treetop ragweed nearby | Crouch and shake | Local blow exposes its item | Blow requires a compatible target | DKR-002 |
| Solo DK with a DK barrel | Break the eligible barrel | Diddy attaches and lost hearts refill | Acquired buffer/abilities, not manual character swap | DKR-003 |
| Diddy attached, airborne | Hold A after jump | Brief hover extends traversal | No unlimited flight | DKR-003 |
| Attached buffer remains | Continue shake while rolling | Kong Roll can continue | Attachment gates the ability | DKR-003 |
| Attached buffer exhausted by eligible hits | Resolve damage | Diddy leaves, hover/continued roll end, DK remains controlled | Same-body loss of affordances | DKR-003 |
| Solo or paired ground roll reaches a gap | Roll off, then request jump | Eligible airborne jump follows | Not every airborne state permits double jump | DKR-004 |
| Eligible enemy underneath | Stomp with timed jump | Enemy response and higher rebound | Top contact differs from side damage | DKR-002 |
| Frog-statue banana group partly collected | Collect the final required member | Piece is exposed, then must be picked up | Local set reward is separate from acquisition | DKR-005 |
| DK plate and background route unopened | Pound the plate, occupy the cannon | Background becomes accessible along preset launch | Fixture prerequisite and traversal differ | DKR-006 |
| Background left ragweed, Diddy retained | Hover across, blow, then return by barrels | Optional piece route and foreground continuation available | Full detour availability | DKR-003 |
| Bonus room newly entered | Collect the entire required set before expiry | Piece reward resolves; return to ordinary route | Optional bounded room | DKR-007 |
| Bonus deadline expires without completion | Continue, then attempt immediate re-entry | No reward, return; failed attempt stays unavailable until reset | Not unlimited cost-free retry | DKR-007 |
| Pig checkpoint passed, reserve life remains | Later ordinary death | Stock decreases and body returns at current anchor | Finite checkpoint return | DKR-008 |
| Letters acquired after checkpoint, piece newly acquired | Ordinary death | Those letters roll back, piece survives | Class-specific rollback, Limited testimony | DKR-009 |
| New piece acquired, stage not cleared | Quit or exhaust stock | New collection not banked across abandonment | Ordinary death differs from terminal exit | DKR-009 |
| Banana counter reaches a hundred | Resolve collection | One extra life credited | Threshold, not every banana grants a life | DKR-008 |
| Final barrel available, optional sets incomplete | Grab a displayed ordinary symbol | Reward and stage clear; next path opens without full collection | Exit is not all-secret objective | DKR-010 |
| DK symbol grabbed | Shake during its reward opportunity | Random item class and quantity response | No asserted probability or multiplier | DKR-010 |
| Enough failures offer help | Activate Super Guide | Leaves unassisted packet, distinct noncollecting assisted clear | No guessed exact threshold or ordinary-clear parity | DKR-011 |

## Strategic and experiential structure

- Local decision: align jump/contact, attack/blow posture and barrel timing
  with the current target; decide whether a safe detour needs retained Diddy.
- Medium-term planning: protect the companion and pass the pig before risk;
  a failed bonus requires a route reset, not another free visit.
- Long-term structure: ordinary clear opens the next path; complete optional
  sets are independent additional goals, not admission to the successor.
- Common heuristics: distinguish a barrel to carry from one to occupy; retain
  Diddy for hover, and finish before assuming newly found pieces are banked.
  These are source-derived suggestions, not measured optimal strategies.
- Failure attribution: unsafe contact/gap, lost companion, wrong local input,
  missed set/deadline, or premature quit; not a mysterious hidden score.
- Player-trust factors: hearts and separate pause counters support attribution;
  checkpoint retention and exact timings remain explicitly limited evidence.
- Claim IDs: `DKR-002`–`DKR-012`.

## Replay and variation

- What changes between sessions: player route, timing, optional exploration,
  health/attachment and banked collection, not a procedurally generated level.
- Randomness or procedural generation: DK exit symbol chooses reward class;
  no distribution, seed or stage-generation claim.
- Multiple viable strategies: ordinary route first or optional collection
  detours, preserving a companion versus proceeding solo where eligible.
- Typical replay motive: optional set completion or safer execution. Time
  Attack replay is a distinct module rather than a fresh-stage rule.
- Claim IDs: `DKR-003`–`DKR-011`.

## Adjacent systems and history

- Direct predecessors: original SNES Donkey Kong Country is a corpus carrier,
  not an assertion of unchanged paired control, animal or bonus rules.
- Variants: co-op, later-stage abilities, 3DS and HD are not original 1-1
  parity; the crosslisted 2010 Wii guide retains its original text identity.
- Similar games: selected canonical neighbour below, not a genre score list.
- Important differences: attached buffer versus active pair switching;
  collection-set reward versus discovery credit; checkpoint-specific rollback
  versus permanent pickup banking; optional sets versus mandatory all secrets.
- Claim IDs: `DKR-003`–`DKR-013`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-048`, `ACT-202`, `ACT-295`, `ACT-667`, `ACT-668` | Posture, hold/shake, compatible target and firing instant |
| System Behaviour | `SYS-036`, `SYS-037`, `SYS-045`, `SYS-064`, `SYS-112`, `SYS-215`, `SYS-755`, `SYS-910`, `SYS-911`, `SYS-933`, `SYS-935`, `SYS-1056`, `SYS-1332`, `SYS-1333`, `SYS-1334`, `SYS-1335`, `SYS-1336`, `SYS-1337`, `SYS-1338` | Health/buffer, target groups, checkpoint, reset, barrel and reward |
| Constraint | `CON-442` | Current compatible command state |
| Information | `INF-469` | Current play/pause/bonus/slot/map disclosure |
| Objective | `OBJ-283` | Ordinary clear and independent optional sets |
| Time | `TIM-003` | Live motion and pause |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `494` (`GAME-0001`–`GAME-0494`).
- Exact genome matches: none.
- Tied near matches: `GAME-0329` — Donkey Kong Country (`14 / 35 = 0.400000`).
- Supported combination subsets: none.
- Scan date: 2026-10-04.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0329` — Donkey Kong Country | `ACT-008`, `ACT-048`, `ACT-295`, `SYS-036`, `SYS-037`, `SYS-045`, `SYS-064`, `SYS-215`, `SYS-755`, `SYS-911`, `SYS-933`, `SYS-935`, `CON-442`, `TIM-003` | Both retain live movement, portable barrels, stomps/combat, collection, finite lives and checkpoint return. Original SNES Jungle Hijinxs permits direct paired-character switching, Rambi and mandatory all-room discovery credit. Original Wii 1-1 instead attaches Diddy to the same controlled DK with consumable hover/roll abilities, adds local blowing and all-set rewards, preset background barrels, reset-gated timed bonus and class-specific clear banking; ordinary clear does not require every secret. Shared names and route themes do not prove executable parity | Near, `0.400000` |

### Preserved research notes

- New genes: eleven additions in `TAXONOMY_CHANGE_232`.
- Classification result: `New gene`.
- Evidence and reasoning: complete local route, ability loss, reset and banking
  are retained without revising older signatures or importing later stages.

## Taxonomy impact

- Registry changes: two actions, seven systems, one information, one objective;
  eighteen unchanged transfers. No older English boundary or signature change.
- Taxonomy-change record: `TAXONOMY_CHANGE_232`.
- Candidate terms affected: no suggestion-term promotion or external novelty.
- Named complete-packet presentation review partitions all 29 uses into eight
  defining, eighteen structural and three supporting bilingual causal cards.
  Existing families suffice; presentation roles do not weight Jaccard.

## Negative results

No gene for DK's name, nine pieces, four letters, exact jump heights, guessed
bonus seconds, arbitrary cannon aim, free bonus retry, universal double jump,
manual Diddy substitution, co-op popgun, Rambi, mandatory all secrets,
immediate cross-quit permanent piece banking or assisted-clear equivalence.
No new recurring combination is inferred from a single carrier.

## Delta summary

## New facts

- [Observation | Corroborated | High] Complete first-stage optional route and
  acquired/lost attached abilities, `DKR-003`–`DKR-006`.
- [Observation | Limited | Medium] Asymmetric death/quit/clear retention,
  `DKR-009`, explicitly attributed rather than claimed locally reproduced.

## New genes

- [Observation | Corroborated | High] Eleven bounded additions; retention is
  Limited/Medium and local bonus retry/disclosure Medium as marked above.

## New combinations

- [Observation | Direct | High] No new recurring combination from one game.

## Taxonomy changes

- [Observation | Corroborated | Medium] `TAXONOMY_CHANGE_232` records transfer
  boundaries and negative counterexamples without altering earlier genomes.
