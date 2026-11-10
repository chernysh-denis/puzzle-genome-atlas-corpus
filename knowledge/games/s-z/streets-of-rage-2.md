---
game_id: GAME-0466
slug: streets-of-rage-2
game_title: Streets of Rage 2
analysis_status: reviewed
reviewed: 2026-10-01
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-048
    - ACT-161
    - ACT-295
  system:
    - SYS-045
    - SYS-215
    - SYS-578
    - SYS-755
    - SYS-911
    - SYS-915
    - SYS-1069
    - SYS-1216
    - SYS-1217
    - SYS-1218
  constraint:
    - CON-442
  information:
    - INF-119
    - INF-192
    - INF-235
    - INF-347
  objective:
    - OBJ-080
  time:
    - TIM-003
---

# Game: Streets of Rage 2

Use the canonical [vocabulary and comparison rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Axel, Downtown, Barbon, individual weapons, food values and exact scores are carrier parameters, not separate genes.

## Analysis scope

- Version / ruleset: original North American English Sega Genesis / Mega Drive cartridge of *Streets of Rage 2* (1992), fresh one-player Normal game with Axel selected. SEGA's preserved original manual is the primary rules source. Its modern Genesis Mini hosting does not import emulator or wrapper features. The exact physical cartridge revision and executable were not obtained or hashed.
- Structured analysis target: `PLAT-SEGA-GENESIS` in [platform coverage](../../platforms/games.json), not the Master System or Game Gear versions, later collections, remakes, sequels or Duel mode.
- Entry: Axel first accepts direct control at the start of Stage 1 Downtown, with its ordinary starting health, fighter stock, score and section clock, before the first enemy is defeated.
- Primary decision loop: read the near-screen lane and enemy position; steer horizontally and in depth, jump, strike or use a temporary ground weapon; watch autonomous enemies attack and personal health fall; break eligible street receptacles for food or score items; use proximity capture and a chosen follow-up when an enemy is close; decide whether a health-priced special is worth the risk; clear each local hostile group to release scrolling and defeat Barbon behind the bar before the next stage.
- Positive terminal: Barbon is defeated, the Stage 1 clearance resolves and Stage 2 first accepts ordinary control, with eligible remaining stock and score. The manual names Downtown, its bar and back alley and the next-stage health refill; the exact final animation and precise transition frame were not inspected.
- Negative terminal: health exhaustion or a section Time Over consumes a Fighter; the run continues through a same-stage replacement while stock remains. When no Fighters remain, Game Over offers Continue; choosing it is outside this packet.
- Included: two-axis stage navigation and jumping; actionable ordinary, jumping, rear and close attacks; direct equipped-weapon hits; B pickup and B+C throw of a temporary weapon; autonomous enemies and continuous combat; damage, food healing, local breakable receptacles and their contents; finite Fighters and score-earned extras; section-specific 99-second countdown and Time Over loss; automatic close-range hold with different follow-up inputs; stationary and directional A specials with their documented health charges; local clearance gates; visible health, score, time, lives, opponents, items and nearby stage; Barbon defeat and transition.
- Excluded: other selectable fighters and their different move lists, optional second player, Duel, all later stages, full-game ending, Continue and credit accounting, difficulty changes, secret moves, exact damage/frame numbers, exact Stage 1 enemy spawn schedule, score optimisation, port and Genesis Mini convenience rules. These exclusions do not claim such features are absent from the product.
- Reproducible parameterisation: select one-player Normal and Axel, enter Downtown without Continue, move through the street and bar, defeat required local enemies whenever further scrolling is held, use legal pickups or specials as desired, defeat Barbon in the alley and stop at first Stage 2 control. A successful input trace, precise enemy counts, exact remaining score and cartridge revision are not claimed.
- Potential scoped modules: other character-specific throws and specials, co-op friendly-fire and shared resources, Duel, later bosses, Continue, regional revisions and direct cartridge capture require separate evidence packets.
- Direct-play status: not conducted. No cartridge, console, executable, controller trace, game screenshot, video or audio was opened or analysed. Pages of SEGA's scanned original manual were rendered and visually inspected; a contemporary written route corroborates the Stage 1 sequence. This is a source-bounded reconstruction, not a claimed playthrough.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `SOR2-001` | Original Genesis one-player controls use D-pad for two-axis movement, A for Special, B for attack/pickup and C for jump | Confirmed | Direct | High | P1 |
| `SOR2-002` | Each local section has a 99-second clock; clearing its enemies releases the next screen or Go arrow and restarts that clock, while Time Over loses a Fighter | Confirmed | Direct | High | P1 |
| `SOR2-003` | Hostile damage depletes personal health; food restores it, finite Fighters permit replacement, and zero stock produces Game Over before any Continue choice | Confirmed | Direct | High | P1 |
| `SOR2-004` | Approach captures a nearby enemy without a separate grab button; B, directional B or C then B select legal follow-ups from the hold | Confirmed | Direct | High | P1 |
| `SOR2-005` | A stationary special charges health only when it contacts an enemy; a directed special charges health on use, and specials are unavailable at critically low health | Confirmed | Direct | High | P1 |
| `SOR2-006` | Attacking receptacles can reveal items; B picks up weapons and B+C throws them, while food and points have distinct consequences | Confirmed | Direct | High | P1 |
| `SOR2-007` | Score milestones can award additional Fighters without consuming the accumulated score | Confirmed | Direct | High | P1 |
| `SOR2-008` | Downtown Stage 1 traverses the street, bar and back alley and ends at Barbon | Confirmed | Direct | High | P1, S1 |
| `SOR2-009` | The bounded identity is a live, section-clocked and clearance-gated brawler with automatic close hold and optional self-health-priced emergency attacks | Strong Pattern | Corroborated | High | `SOR2-002`–`SOR2-008` |

## Basic data

- Release / origin: original SEGA Genesis / Mega Drive *Streets of Rage 2*, 1992. SEGA's retrospective confirms the original US Genesis release; the analysed rules are from the original manual rather than a modern wrapper.
- Puzzle family: tactical forecast and counterplay (`FAM-009`); real-time system pressure (`FAM-010`).
- **[P1]** [SEGA-preserved original Genesis manual](https://manuals.sega.com/genesismini/pdf/STREETS_OF_RAGE_2.pdf), printed pages 6–7, 12–23 and 26–27 for controls, HUD, section clock, pickups, close attacks, specials, Stage 1 and score/life settlement; accessed 2026-10-01. It is a scanned PDF: the relevant pages were visually rendered, not inferred from empty OCR.
- **[P2]** [SEGA's original-release retrospective](https://social.sega.com/articles/streets-of-rage-2-hit-the-genesis-in-the-us/), for the original US Genesis identity and four-character roster; accessed 2026-10-01.
- **[S1]** [contemporary written Genesis Stage 1 route](https://gamefaqs.gamespot.com/genesis/563344-streets-of-rage-2/faqs/9413), for street, bar and Barbon sequence; accessed 2026-10-01. A player's guide is corroboration, not the primary rules authority.
- **[R1]** No direct game run, source code, executable or audiovisual trace was inspected.

## Mechanical decomposition

### Action Genes

- `ACT-008`: move Axel left/right and between foreground/background lanes, and jump across the current combat floor.
- `ACT-295`: command one character-owned ordinary, rear, jumping, directed-special or hold-follow-up attack when pose and input allow it.
- `ACT-048`: pick up, retain, drop or throw a reachable loose weapon.
- `ACT-161`: direct a currently held weapon strike at a reachable enemy or breakable receptacle.

### System Behaviour Genes

- `SYS-045` autonomously moves and attacks local enemies; `SYS-215` resolves both sides' live hits, range, knockback and defeat.
- `SYS-578` applies hostile or special-cost health loss and food healing to Axel's current gauge; `SYS-911` spends one finite Fighter after a lethal event and restores control while stock remains.
- `SYS-755` lets attacks break eligible street receptacles and release contained items. `SYS-1069` grants Fighters at the documented accumulating score milestones without paying score.
- `SYS-915` holds the next authored slice until the required local enemies are beaten, then releases scrolling.
- New `SYS-1216` enters a close hold when Axel approaches a compatible enemy. It persists until a legal flurry, throw, vault/slam, escape or interruption; the follow-up is a deliberate attack, not an independent grab command.
- New `SYS-1217` charges Axel's health for Specials: stationary A only when it contacts an enemy, directional A on use; the effect resolves within live combat and the critically low-health eligibility belongs to `CON-442`.
- New `SYS-1218` starts a fresh 99-second clock per local section; expiry consumes a Fighter instead of asserting immediate whole-run failure. Clearing the section resets the next clock.

### Constraint Genes

- `CON-442`: the current pose, held weapon, close-hold state, recovery and health allow or block contextual fighting commands. A Special at critically low health is not legal. The shared B button's attack/pickup meaning follows the current state.

### Information Genes

- `INF-119`: personal health and current capability are visible. `INF-347` joins current score, section time and finite Fighter stock on the live HUD.
- `INF-192` limits lookahead to the scrolling Stage 1 slice. `INF-235` exposes visible enemies, breakables, food and weapon state; it does not expose future spawn positions or guaranteed hidden contents.

### Objective Genes

- `OBJ-080`: clear the required Downtown route, beat Barbon and cross into the next playable Stage. A perfect score, all optional items and the full-game ending are not required.

### Time Genes

- `TIM-003`: enemies and the section clock continue while Axel can move and issue live attacks. Pausing and menu manipulation are outside this bounded input loop.

## Reproducible transitions

| Before | Input or event | Resolution | Boundary shown | Claim |
|---|---|---|---|---|
| Local enemies remain at a camera hold | Move in depth and strike a reachable enemy | Enemies also move and attack; the route stays held until required hostiles are cleared | Live combat plus local gate | `SOR2-001`, `SOR2-002` |
| Compatible foe enters close reach | Approach, then choose B or a directional/jump follow-up | A hold starts automatically; the chosen legal attack resolves from that state | Grab is not an extra button press | `SOR2-004` |
| Axel has usable health and a foe is in range | Press stationary A and connect, or direction+A | Stationary contact or directed use pays the documented health price while affecting the enemy | Conditional versus immediate self-cost | `SOR2-005` |
| Breakable street receptacle is intact | Hit it, inspect output, press B at a revealed item | Its body breaks and may expose food, points or a temporary weapon; eligible pickup changes health, score or weapon state | World-object destruction differs from enemy defeat | `SOR2-006` |
| Section clock reaches zero before clearance | Allow countdown to expire | One Fighter is lost; replacement occurs only if stock remains, otherwise Game Over | A local deadline is not an automatic run failure | `SOR2-002`, `SOR2-003` |
| Required local hostiles are gone | Advance toward Go arrow or newly opened view | Camera releases the next section and its clock restarts | Clearance-gated progression | `SOR2-002` |
| Accumulated score crosses an eligible milestone | Resolve points from attacks or pickups | An extra Fighter is awarded up to the game's stock limit without spending score | Score supports survival, not a mandatory Stage 1 objective | `SOR2-007` |
| Barbon is defeated in the back alley | Let Stage 1 result and transition settle | The next stage becomes playable; its health begins full | Bounded positive terminal | `SOR2-008` |

## Strategic and experiential structure

- The player reads lane alignment and attack reach rather than an abstract target list. A close approach can open a powerful hold but also exposes Axel to enemy contact.
- Weapon pickup and food compete for attention with the section clock. Breaking a receptacle may open an optional resource, but clearing the required hostile group drives progress.
- A Special exchanges health for an immediate combat effect; its two activation rules mean a missed stationary Special and a directed Special do not carry identical cost.
- Score can later replenish Fighters, but a local Time Over or lethal hit still consumes current stock. Continue is a separate post-Game-Over choice, not the same life rule.

## Replay and variation

- Enemy position, player attack choice, optional item pickup, damage, score and surviving stock can vary; the authored Stage 1 route and Barbon terminal do not imply a procedural level.
- A different fighter, difficulty or two-player mode changes the input and cost surface and requires a separately bounded analysis. No exact optimal route or enemy count is claimed.

## Adjacent systems and history

- *Battletoads* shares local hostile clearance, body-owned attacks and finite-life replacement, but its first stage culminates in the returned-rock Tall Walker view, not an automatic close hold plus health-priced Special and per-section Time Over loss.
- *Street Fighter 6* shares contextual attack legality, but its single fixed-opponent round does not transfer Stage 1's scrolling encounter gate, breakable street receptacles or score-earned Fighters.
- The Genesis Mini PDF is a preservation host for the original manual, not evidence that save states or rewind belonged to the cartridge rules.

## Normalised genome

| Type | Active gene IDs | Boundary |
|---|---|---|
| Action | `ACT-008`, `ACT-048`, `ACT-161`, `ACT-295` | movement, carried weapon and body-owned strike |
| System Behaviour | `SYS-045`, `SYS-215`, `SYS-578`, `SYS-755`, `SYS-911`, `SYS-915`, `SYS-1069`, `SYS-1216`, `SYS-1217`, `SYS-1218` | combat, resources, local gates and distinctive hold/cost/clock laws |
| Constraint | `CON-442` | compatible pose, item and health prerequisite |
| Information | `INF-119`, `INF-192`, `INF-235`, `INF-347` | visible HUD and local stage lookahead |
| Objective | `OBJ-080` | Barbon clearance and Stage 2 entry |
| Time | `TIM-003` | live input during hostile and clock progression |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `465` (`GAME-0001`–`GAME-0465`).
- Exact genome matches: none.
- Tied near matches: `GAME-0318` — Battletoads (`14 / 25 = 0.560000`).
- Supported combination subsets: none.
- Scan date: 2026-10-01.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0318` — Battletoads | `ACT-008`, `ACT-048`, `ACT-295`, `SYS-045`, `SYS-215`, `SYS-578`, `SYS-911`, `SYS-915`, `CON-442`, `INF-119`, `INF-192`, `INF-235`, `OBJ-080`, `TIM-003` | Both are local-clearance brawlers with directly controlled attacks, a finite Fighter stock and a guardian transition. Battletoads converts defeated enemies into a Walker leg or Dragon ride and reverses perspective for Tall Walker rocks; Streets of Rage 2 instead adds automatic close holds, personal-health-priced Specials, section Time Over life loss, breakable street receptacles and score-earned Fighters. | Tied near, `14 / 25 = 0.560000` |

### Preserved research notes

- New genes: `SYS-1216`, `SYS-1217`, `SYS-1218`.
- Reused genes: `ACT-008`, `ACT-048`, `ACT-161`, `ACT-295`, `SYS-045`, `SYS-215`, `SYS-578`, `SYS-755`, `SYS-911`, `SYS-915`, `SYS-1069`, `CON-442`, `INF-119`, `INF-192`, `INF-235`, `INF-347`, `OBJ-080`, `TIM-003`.
- Classification result: `New genes`.
- Evidence and reasoning: official printed rules directly distinguish automatic proximity hold, two different Special health prices and a renewable section clock with finite-stock penalty. Existing genes transfer the ordinary brawler route and resource surface without turning those three differences into mere numerical parameters.

## Taxonomy impact

- Three new Active System Behaviour genes; no previous genome, verified combination or published corpus revision is changed.
- Taxonomy-change record: [`TAXONOMY_CHANGE_203`](../../../research/taxonomy-changes/TAXONOMY_CHANGE_203.md).

## Negative results

- No cartridge execution or video inspection; exact damage numbers, hitboxes, timer reset frame and enemy spawn schedule remain unmeasured.
- The manual's four-character move list does not make all four characters simultaneous in this one-Axel packet.
- The manual's Continue instructions do not authorise a free extra life when the ordinary stock expires.
- The countdown does not imply `CON-068`'s immediate failed-attempt terminal: Time Over spends a Fighter first.

## Delta summary

## New facts

- [Confirmed | Direct | High] Official original rules document Stage 1's local 99-second clock, automatic close hold, two Special cost cases and finite Fighter settlement (`SOR2-002`–`SOR2-007`).

## New genes

- [Observation | Direct | High] `SYS-1216`–`SYS-1218` isolate proximity capture, conditional self-health-priced Special and section Time Over without mutating prior boundaries.

## New combinations

- [Observation | Direct | High] None claimed until the verified-subset scan is computed.

## Taxonomy changes

- [Observation | Direct | High] Three new system definitions, no migration of older games.

## Open questions

- Direct original-cartridge play could measure the exact item distribution, fighter cap, final transition frame and Special health values.

## Next research candidate

- `GAME-0467` — *Vib-Ribbon*, original PlayStation, the next approved unit after complete GAME-0466 acceptance and its Goal stop window.
