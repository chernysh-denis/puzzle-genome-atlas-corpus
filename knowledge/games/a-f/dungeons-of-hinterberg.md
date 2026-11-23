---
game_id: GAME-0592
slug: dungeons-of-hinterberg
game_title: Dungeons of Hinterberg
analysis_status: reviewed
reviewed: 2026-11-21
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-009
    - ACT-049
    - ACT-161
    - ACT-190
    - ACT-223
    - ACT-341
  system:
    - SYS-061
    - SYS-215
    - SYS-578
    - SYS-1742
    - SYS-1743
    - SYS-1744
    - SYS-1745
    - SYS-1746
    - SYS-1747
  constraint:
    - CON-402
    - CON-773
    - CON-844
  information:
    - INF-142
    - INF-179
  objective:
    - OBJ-080
  time:
    - TIM-003
---

# Game: Dungeons of Hinterberg

Use the [canonical vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
Use a summoned weight, a chain and changing tracks to reach the
Miner’s Widow, then stamp the cleared dungeon and leave by its portal.

## Analysis scope

- Version / ruleset: English Xbox Series X|S digital base game at
  18 July 2024 commercial launch. Reproduce on an ordinary fresh
  single-player path without relaxed combat, a postgame loadout or
  New Game+. The dated Xbox Series X capture uses a code supplied
  ahead of launch. The exact executable, difficulty preset of the
  capture and later patch parity remain unverified.
- Structured analysis target: PLAT-XBOX-SERIES.
  See [platform coverage](../../platforms/games.json).
- Entry: first control just inside Abandoned Mineshaft on Day 2
  after the Starting Out approach. Learn Wrecking Ball and Ball &
  Chain at the Doberkogel shrine and open the outer access before
  this entry. Use the route’s available early gear.
- Primary decision loop: read which obstacle or fixture needs
  weight, contact, a chain pull or a new rail connection. Clear
  an encountered seal and arrange the next traversable state.
  Board the yellow cart where the rails continue, select safe
  branches while rolling and dismount to realign later links.
  During combat, manage HP, refill spell MP through landed sword
  attacks, and use magic against shields without exhausting dodge
  stamina as the next attack arrives.
- Positive exit: clear the Miner’s Widow and required accompanying
  foes, interact with the stamp station and take the portal.
  The book shows Abandoned Mineshaft complete and Day 2 Evening
  begins. Stop before any town action.
- Negative exit: an unloaded plate, a mismatched rail or uncleared
  combat seal blocks progress. A striped barricade can strike the
  riding cart, consuming vitality and interrupting the ride. Zero
  health ends the current attempt. Exact retry placement, inventory
  restoration and later Waystone rules are outside this packet.
- Included: contextual traversal, one conjunction of three maintained
  loads, chain-actuated targets, temporary ball mass and detonation,
  authored cart travel and branches, ballast platform and linked rail
  alignment, mandatory combat, separate dodge and spell budgets,
  magic shields, the boss, stamp and portal.
- Excluded: Beginner’s Dungeon, exterior approach puzzles, the rest
  of the Starting Out quest, optional coin and loot as requirements,
  charm builds, weapon statistics, numerical damage and recovery
  constants, social progression, post-clear town activity, New Game+,
  other platforms and post-launch persistence changes.
- Potential scoped module: the distinct Doberkogel Minecart Workshop
  with its separate platform sequence and guardian.
- Direct-play status: no executable or native inputs used. The publisher,
  developer and platform listing establish the released product and
  regional tools. Silent stills from a release-window Xbox Series X
  route and independent launch accounts establish the in-mine sequence.
  Exact patch, internal values, replay timing and reset predicates
  remain unverified. Video and audio were not played.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
| --- | --- | --- | --- | --- | --- |
| DH-001 | The July 2024 Xbox Series X&#124;S release is a complete single-player base game. Doberkogel assigns Wrecking Ball and Ball & Chain before Abandoned Mineshaft, which is distinct from Day 1’s Beginner’s Dungeon and later Minecart Workshop. | Confirmed | Direct | High | P1–P4; W1 34:00–37:10; R1 |
| DH-002 | At the first rail-room gate, push the two small carts onto two separate gold plates after releasing the supported cart. Conjure the intact Wrecking Ball onto the last plate. Together the three supported bodies open the passage. A missing load fails the joint condition; the ball does not need to explode for this gate. | Observation | Corroborated | High | W1 37:40–38:40; W2 0:10–0:32; R1, R2 |
| DH-003 | Wrecking Ball gives Luisa a placed heavy body before detonation. It can hold a plate or weight a linked platform, and detonating at eligible rubble removes the obstruction. Ball & Chain reaches marked targets remotely, releasing tethered objects and repositioning authored crossing surfaces or rail sections. | Observation | Corroborated | High | P3, P4; W1 38:00/40:40/43:10; W2 0:18/0:28; R1, R2 |
| DH-004 | Past Travis, contextual climbing and a pulled support cross the wall route. A defended passage and reachable switch precede a shield tutorial and the climb to the first ride. The regular route uses several separate gates and does not require optional treasure. | Observation | Corroborated | High | W1 38:40–42:30; W3 1:40–5:45; R1, R2 |
| DH-005 | Riding a yellow cart advances along fixed rails. The rider chooses branches while moving; striped barricades threaten the wrong trajectory. A released Xbox capture shows a tilted cart, impact feedback, reduced vitality and another running ride. This does not specify the exact reset position. | Observation | Corroborated | High | W1 42:30/44:10/44:30/44:50/46:00; W3 6:20–7:45; R1, R2 |
| DH-006 | One weighted platform raises Luisa to a ledge for the first rail alignment. The final switch room first routes the cart to another ledge. Pull the distant marked connector there, return, toggle the earlier mechanism and move the cart back to the other starting side before choosing the new continuation. Cart location and connector alignment are independent. | Observation | Corroborated | High | W1 43:00–43:50/46:40–48:30; W2 0:31–2:20; W3 5:45–9:05; R1, R2 |
| DH-007 | Swinging the sword and casting the regional pair solve different combat needs. Spells use MP in combat; landed melee, especially heavy hits, renews it. Puzzle use is available without the combat charge. Magical shields show separate defence and are vulnerable to magic; the evidence does not establish universal immunity to all other tools. | Observation | Corroborated | High | W1 41:00–41:30/48:40–49:20; W3 4:10; R1, R3, R4 |
| DH-008 | The Miner’s Widow arena combines an approaching boss, accompanying enemies and visible attack cues. Rolls spend a limited regenerating stamina supply separate from MP and HP. The Xbox record shows an Out of Stamina warning during the active fight and surviving after low-health feedback. | Observation | Corroborated | High | W1 48:30–49:30; W3 9:45–11:05; R1–R4 |
| DH-009 | After defeat of the arena’s required foes, the stamp is registered in the Stamp Book. Crossing the nearby exit portal then advances the day to Evening. The same eligibility does not follow from an earlier cart ride or the optional dungeon coin. | Observation | Corroborated | High | W1 49:30/49:40/50:00/50:10; W3 11:35; R1, R2 |
| DH-010 | Health can decrease from attacks and rail impacts, and an exhausted health pool stops the attempt. Same-area retry is reported, but the record does not settle original console checkpoint fields or eliminate possible launch-era failure bugs. | Observation | Corroborated | Medium | W1 44:30–44:50/49:30; R5 and P5 |

## Basic data

- Microbird Games and Curve Games. FAM-017 covers prerequisite states
  for the gate and track route. FAM-010 covers live combat, rider input
  and limited evasion windows.
- P1: [Curve Games’ launch statement](https://curvegames.com/news/dungeons-of-hinterberg-launches-today/),
  dated 18 July 2024. Identifies release, platform and the combination
  of combat, exploration and puzzles.
- P2: [Xbox’s North American digital product](https://www.xbox.com/en-US/games/store/dungeons-of-hinterberg/9PGX472J0RJP/0010).
  Establishes official developer, publisher, platform and commercial
  release. Other listed platforms and current subscription availability
  are outside the analysis.
- P3: [Microbird’s press kit](https://www.dungeonsofhinterberg.com/press/).
  Confirms distinct release dates and magical traversal and combat.
- P4: [Xbox Wire’s developer-demo account](https://news.xbox.com/en-us/2023/08/23/dungeons-of-hinterberg-demo/).
  Establishes the designers’ Wrecking Ball and Ball & Chain tool
  concepts. This is precursor evidence. The released traces and
  written July rules establish their in-mine effects.
- P5: [Developer patch notes via Steam](https://steamcommunity.com/app/1983260/allnews/).
  The 12 August update documents changes to Waystones and one
  combat death issue. See the
  [dated notes mirror](https://steamdb.info/patchnotes/15344024/).
  No later revision is silently treated as the July console build.
- W1: [Section Plays, Xbox Series X launch-window route](https://www.youtube.com/watch?v=8kSQ88NQ-Yo),
  18 July 2024. Stills show Day 2 entry at 36:40, sealed fights and
  plates at 37:20–38:40, shield-room progression near 41:10, riding
  and impact at 42:30–46:00, the final switch room at 46:40–48:30,
  combat at 48:40–49:30, stamped book at 49:40 and portal and
  Evening at 50:00–50:10.
- W2: [Rascally Rasmus’s minecart guide](https://www.youtube.com/watch?v=2JUU-tgz2w8),
  26 July 2024. Frames 0:10–0:32 show both carts and the undetonated
  ball as weights. The subsequent segments support the lift and
  final reconnection. The system UI in this replay is not used to
  claim it is the same console build.
- W3: [OpenQuestline’s launch-window dungeon guide](https://www.youtube.com/watch?v=p3eJgCFNE1c),
  29 July 2024. Stills show portal-side entry, first gate at 1:40,
  Magic Shields tutorial at 4:10, rides and switch rooms, final fight
  at 9:45–11:05 and arrival at the portal at 11:35. This corroborates
  states without identifying the target executable.
- R1: [Into Indie Games’ Day 2 route](https://intoindiegames.com/walkthroughs/dungeons-of-hinterberg/).
  Distinguishes the exterior lift, three plates, accessible ledges,
  battles and the final track switches, then guardian, stamp and exit.
  The date precedes release. No precise retail parameter comes from
  the preview route alone.
- R2: [Twinfinite’s July rail and plate solutions](https://twinfinite.net/guides/all-abandoned-mineshaft-dungeon-puzzle-solutions-in-dungeons-of-hinterberg/).
  Corroborates the multiple stable cart positions, remote targets,
  intermediate destination and reconfigured last continuation.
- R3: [RPG Site's release-day play account](https://www.rpgsite.net/review/16079-dungeons-hinterberg-review).
  Documents regional capabilities, normal and heavy strikes
  replenishing MP and the separate rolling stamina supply.
- R4: [Hinterberg’s documented combat tutorials](https://dungeons-of-hinterberg.fandom.com/wiki/Combat)
  and [regional skills](https://dungeons-of-hinterberg.fandom.com/wiki/Magic_Skills).
  Useful for distinguishing exploration casts, paid combat casts,
  vitality and shields. Exact values and later modifiers are excluded.
- R5: [Twinfinite’s launch review](https://twinfinite.net/REVIEWS/DUNGEONS-OF-HINTERBERG-REVIEW/).
  Reports same-area checkpoint behavior and state restoration examples,
  without identifying an Abandoned Mineshaft console save.
- Sources accessed 2026-11-21.

## Mechanical decomposition

### Action Genes

- ACT-008 moves Luisa along the authored floor, ledges and ladder
  route. ACT-009 shifts an adjacent small cart along its limited
  spur. ACT-049 operates a reachable explicit switch (DH-002–DH-006).
- ACT-190 places or detonates Wrecking Ball and aims Ball & Chain.
  The same directed commands are reused against different legal
  targets (DH-003, DH-007).
- ACT-161 commands direct sword strikes. ACT-223 commits a timed roll
  to evade a live attack (DH-007, DH-008).
- ACT-341 boards the available cart and interacts with the stamp
  station and accepted exit (DH-005, DH-009).

### System Behaviour Genes

- SYS-061 keeps the gate state tied to occupied pressure regions. The
  three plate conjuncts require two carts and an additional placed weight
  on the demonstrated solution (DH-002).
- SYS-1742 gives one placed magical body a temporary weight function
  before deliberate detonation removes eligible material. SYS-1743
  changes authored geometry or releases a support by pulling a typed
  remote target (DH-003, DH-006).
- SYS-1744 resolves the fixed rail connector's current alignment into
  traversable continuations. SYS-1745 moves a boarded cart, accepts
  directional branch choices and treats obstruction contact separately
  from reaching its terminal (DH-005, DH-006).
- SYS-215 resolves active combat. SYS-1746 couples paid combat magic
  to replenishment from landed sword hits while equivalent traversal
  casts remain available. SYS-1747 lets magic strip a separate enemy
  barrier and open the ordinary damage cycle (DH-007, DH-008).
- SYS-578 reduces the current life pool on impact or enemy damage and
  permits compatible recovery before exhaustion (DH-008, DH-010).

### Constraint Genes

- CON-402 closes required routes during sealed combat until its hostile
  set is removed (DH-004, DH-007–DH-009).
- CON-773 requires positive vitality in the current attempt. CON-844
  gates repeated evasion by a separately recovering dodge stock
  (DH-008, DH-010).

### Information Genes

- INF-179 exposes plate engagement, rail placement, the intended
  target marks, barriers and available doors (DH-002–DH-006).
- INF-142 exposes attack motion and warnings needed for timing
  against the final foes (DH-008).

### Objective Genes

- OBJ-080 requires the opened route, the required guardian encounter,
  the stamp and exit portal into the next period (DH-009).

### Time Genes

- TIM-003 covers rolling branch decisions and live danger while
  performing attacks, spells and dodges (DH-005, DH-007, DH-008).

## Reproducible transitions

| Initial state | Intervention | Discriminating result | Evidence |
| --- | --- | --- | --- |
| Enter the mine after receiving Doberkogel magic | Descend and clear the first kobold encounter | Free access to the plate room after the temporary seal disappears. | DH-001, DH-002 |
| The first barred exit has three plate inputs and only two small carts | Free the suspended cart by pulling its target. Position the carts on separate plates and summon the ball onto the unoccupied plate. | The demonstrated route opens while all three loads remain. Detonating the ball is not part of this solution. | DH-002, DH-003 |
| Route beyond the gate passes Travis and a gap | Climb the ledges and pull the marked crossing piece with the chain | A reachable route is aligned. Following the ledges reaches another brief combat and switch. | DH-003, DH-004 |
| Magic-shielded enemy guards the route | Use an eligible spell and land sword hits as openings permit | Magic acts against the distinct shield and melee renews combat MP. The route opens after clearing the requirement. | DH-004, DH-007 |
| First cart reaches an intermediate ledge | Stand on a platform, use the ball on the linked side, then climb and pull the marked rail piece | The lift makes the high target reachable and the changed rail creates its next valid route. | DH-003, DH-005, DH-006 |
| Cart approaches a branch while rolling | Select the connected clear branch and avoid striped obstacles | A safe branch continues to the next segment. A wrong line can hit a barricade and reduce HP. | DH-005 |
| Last rail room has a toggle and a separated connector | Stage the cart on the side that reaches the ledge. Ride across, pull the remote connector, return and re-stage from the other side under the changed switch state. | The rail chain becomes continuous toward the final arena rather than stopping at the first destination. | DH-006 |
| Luisa enters the last arena | Time rolls and pair melee recovery with spells until the Widow and required adds fall | The combat boundary clears. Repeated dodges can fail briefly for lack of stamina. | DH-007, DH-008 |
| Arena clear and the stamp station are accessible | Register the book and take the portal | The completed stamp is visible. The game begins Day 2 Evening back in Hinterberg. | DH-009 |

## Strategic and experiential structure

A single conjuration acts as ballast before it acts as a blast. The
chain can replace a missing mechanical connection from an otherwise
reachable ledge. In the last room, the correct rail orientation alone
does not move the cart to the correct spur. Movement and configuration
are separate state changes. In the guardian arena, repeated spells can
drain combat MP, while excessive rolling loses a later escape option
without spending that same MP.

## Replay and variation

The documented accounts use varying optional treasure and coin
detours and different combat timing. The mandatory room order,
loads, reconnection, guardian and stamped exit agree. The launch
evidence does not establish fixed spawn timing, death inventory
retention, a deterministic combat script or cross-platform identity.

## Adjacent systems and history

Portal shows how a retained load sustains one door signal. Here two
carts and a temporary magic body must act together before a rail
puzzle can continue. Railbound uses train movement along a configured
network, but its free-car run couples numbered carriages to a
receiver. Luisa boards the active cart, chooses branches during motion
and changes later track alignment from outside it.

## Normalised genome

| Type | Active gene IDs | Carrier parameters |
| --- | --- | --- |
| Action | ACT-008, ACT-009, ACT-049, ACT-161, ACT-190, ACT-223, ACT-341 | movement, adjacent cart push, switch, sword, spells, roll and local interaction |
| System Behaviour | SYS-061, SYS-215, SYS-578, SYS-1742, SYS-1743, SYS-1744, SYS-1745, SYS-1746, SYS-1747 | plate occupancy, combat, vitality, dual-purpose weight, tether, rail alignment, driving and spell/shield transitions |
| Constraint | CON-402, CON-773, CON-844 | combat seal, viable HP and regenerating dodge supply |
| Information | INF-142, INF-179 | local route states and live threat cues |
| Objective | OBJ-080 | guardian clearance, stamp and portal |
| Time | TIM-003 | live branch timing and combat |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `591` (`GAME-0001`–`GAME-0591`).
- Exact genome matches: none.
- Tied near matches: `GAME-0532` — Hades II (`11 / 35 = 0.314286`).
- Supported combination subsets: none.
- Scan date: 2026-11-21.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
| --- | --- | --- | --- |
| GAME-0532 Hades II | ACT-008, ACT-161, ACT-190, ACT-341, CON-402, INF-142, INF-179, OBJ-080, SYS-215, SYS-578, TIM-003 | Both use movement, sword attacks, evasive movement and a live clear gate. Hades II builds a satyr-nest encounter around weapon and boon choices. The mine requires three maintained loads, a remote tether, fixed connector alignment, route-dependent cart travel and a book stamp. | 11 shared of 35; Jaccard 0.314286 |

### Preserved research notes

- New genes: SYS-1742 through SYS-1747 and CON-844.
- Classification result: New gene.

## Taxonomy impact

- [TAXONOMY_CHANGE_338](../../../research/taxonomy-changes/TAXONOMY_CHANGE_338.md)
  records the new boundaries for spell weight, authored tether, rail
  connections, inhabited track branches, MP, shield and rolling stamina.

## Negative results

- The conjured ball on the third pressure plate is useful while intact.
  A timed explosion alone does not model the recorded load setup.
- The rail-room switch, cart start position and remote rail connector
  are distinct. The recorded continuation requires their compatible state.
- No new arbitrary rail construction, latent Doberkogel spell carryover
  into other regions, universal magic immunity, required coin collection
  or exact retry inventory behaviour is inferred.
- Defeating the widow alone does not demonstrate a stamped book and
  portal return. Both are checked before ending the packet.

## Delta summary

## New facts

- [Observation | Corroborated | High] The one regional spell pair
  manipulates gates and weighted support before its combat use.

## New genes

- [Observation | Corroborated | Medium] Seven additions in
  TAXONOMY_CHANGE_338, retained alongside the reviewed reuse.

## New combinations

- [Observation | Corroborated | High] No new verified combination
  proposed. Existing subset results are recorded above.

## Taxonomy changes

- [Observation | Corroborated | Medium] Earlier definitions,
  signatures and combinations are retained.

## New questions

- A controlled launch console run could isolate the cart collision
  fallback, magic shield coefficients, spell-cost timing and precise
  checkpoint state.

## Next recommended game

- [Hypothesis | Limited | Medium] GAME-0593, The Legend of Zelda:
  The Minish Cap on North American Game Boy Advance. Bound an
  early route whose access changes with Link’s size.
- Optimisation criterion: contrast changing route fixtures with
  changing the controlled actor’s traversal scale.

## Why this game

- [Hypothesis | Limited | Medium] The mine gives multiple authored
  counterfactuals for an unchanged pair of tools across routing
  and an active guardian encounter.
