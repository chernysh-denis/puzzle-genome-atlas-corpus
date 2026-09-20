---
game_id: GAME-0324
slug: contra-force
game_title: Contra Force
analysis_status: reviewed
reviewed: 2026-09-20
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-036
    - ACT-161
    - ACT-202
    - ACT-228
    - ACT-480
  system:
    - SYS-045
    - SYS-051
    - SYS-215
    - SYS-755
    - SYS-911
    - SYS-929
    - SYS-930
  constraint:
    - CON-442
  information:
    - INF-073
    - INF-192
    - INF-235
    - INF-355
  objective:
    - OBJ-080
  time:
    - TIM-003
---

# Game: Contra Force

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Burn, Iron, Smith,
Beans, Battle Plan, Dewerdrye Warehouse and D.N.M.E. are carrier parameters,
not gene names.

## Analysis scope

- Version / ruleset: original North American English Nintendo Entertainment
  System cartridge `NES-CR-USA`, developed and published by Konami in September
  1992. The packet covers a fresh one-player game and only Mission 1,
  `The Dewerdrye Warehouse`, without two-player play, Continue, cheat code,
  emulator save state or later-wrapper conveniences.
- Structured analysis target: licensed North American NES cartridge
  `NES-CR-USA`; see `GAME-0324` in
  [`knowledge/platforms/games.json`](../../platforms/games.json).
- Primary decision loop: choose Burn, read the visible side-view warehouse
  slice, run, jump, crouch and fire in eight directions; break compatible
  crates or ledges and collect visible power-up cases; advance the current
  commando's weapon gauge and commit its highlighted capability; pause to
  switch direct control among available commandos or assign one other commando
  a temporary Battle Plan; traverse the warehouse machinery, avoid its presses,
  falling cargo, pits and fan route, then defeat the Warehouse Ringleader.
- Entry: first ordinary control of Burn at the beginning of Mission 1 after a
  fresh one-player character selection, before the first block and hostile.
- Positive terminal: the Warehouse Ringleader is defeated, Mission 1 settles
  and the game presents or begins Mission 2, `The U.S.S. Unkmy Battleship`,
  with the surviving run state eligible to continue.
- Negative terminal: loss of the selected commando's last available life opens
  the Game Over / Continue path. Choosing Continue and its mission restart are
  excluded. Earlier lethal states spend one finite life and restore a
  controlled body while the current mission remains viable.
- Included: direct side-view movement; jumping, crouching and eight-direction
  aiming; real-time firearm and explosive attacks; breakable route objects;
  visible pickups; character-specific speed, jump and weapon rows; the
  cumulative power-up gauge and one selected active upgrade; four-commandos
  roster; player-selected direct-control switching; one temporarily summoned
  autonomous partner; six Battle Plan roles; local enemies, projectiles,
  machinery, pits and boss; finite lives; Mission 1 boss and successor handoff.
- Excluded: second-player control; Mission 2 play after its first ordinary
  presentation; later missions, campaign completion, Continue, passwords,
  cheats, glitches, score farming and exact damage optimisation; Japanese
  prototype history, fan translations, hacks, ports, compilations, emulated
  browser copies, sequels and other Contra titles.
- Reproducible parameterisation: start the English `NES-CR-USA` one-player
  game, select Burn, retain default controls and do not Continue. Traverse the
  ordinary Mission 1 route, break only necessary or chosen compatible objects,
  collect any reachable cases, and use SELECT only when the visible gauge
  highlights the intended weapon or capability. At least once before the boss,
  pause and switch direct control to another available commando, then return to
  Burn; separately assign one other commando a legal Battle Plan and allow its
  short assistance interval to finish. Exact commando, plan, upgrade, enemies
  defeated, score, life loss and optional pickups may vary. Stop when Mission 2
  is first presented or when the first Game Over offer appears.
- Potential scoped modules: each other commando's complete Mission 1 weapon
  route, two-player authority, Continue, every later mission and full campaign
  completion require separate boundaries and evidence.
- Direct-play status: not conducted. No original cartridge, console, licensed
  installed wrapper, controller trace, save state, screenshot, video or audio
  was found or opened. The original manual establishes product identity,
  controls, commando roles, Battle Plans, power-ups, lives and mission names;
  two written routes corroborate the bounded first mission and boss. This is a
  source-bounded reconstruction, not a claimed playthrough or reload test.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `CF-001` | The subject is the licensed September 1992 North American NES cartridge `NES-CR-USA` | Confirmed | Corroborated | High | P1, P2, P3 |
| `CF-002` | One-player selection offers Burn, Iron, Smith and Beans with distinct movement and weapon rows | Confirmed | Direct | High | P1, P2 |
| `CF-003` | The pad supports movement and eight-direction aim, A jumps, B fires and Down plus B fires while crouched | Confirmed | Direct | High | P1, P2 |
| `CF-004` | START opens Command Select, where the player can change the directly controlled commando or assign one other commando a Battle Plan | Confirmed | Direct | High | P1, P2 |
| `CF-005` | Six Battle Plans place a partner in front, behind, around or beside the player for only a short assistance interval | Confirmed | Direct | High | P1, P2 |
| `CF-006` | Collected power-up cases advance the current commando's visible weapon gauge and SELECT activates the highlighted capability | Confirmed | Direct | High | P1, P2 |
| `CF-007` | Only one selected weapon upgrade is active at a time, and each commando has a distinct ordered upgrade row | Observation | Corroborated | High | P1, S1 |
| `CF-008` | Mission 1 is a side-scrolling warehouse route with breakable objects, presses, falling cargo, pits, platforms and a fan passage | Observation | Corroborated | High | P1, S1, S2 |
| `CF-009` | The Warehouse Ringleader shoots, rolls and jumps; defeating it closes Mission 1 and advances to the battleship mission | Observation | Corroborated | High | S1, S2 |
| `CF-010` | Each commando begins with a finite three-life stock; a Continue after exhaustion restarts the current mission and is outside this packet | Confirmed | Direct | High | P1, P2 |
| `CF-011` | No installed build, direct play, reload comparison or audiovisual evidence was used | Confirmed | Direct | High | R1 |

## Basic data

- Release / origin: Konami developed and published the North American licensed
  NES cartridge in September 1992.
- Platform or physical form: English North American Nintendo Entertainment
  System cartridge `NES-CR-USA`, fresh one-player game, original rules.
- Puzzle family: tactical forecast and counterplay; agent routing and
  coordination; real-time system pressure; ordered dependency sequencing.
- Primary and original sources, accessed 2026-09-20:
  - **[P1]** [scanned original Contra Force NES instruction
    manual](https://www.digitpress.com/library/manuals/nes/Contra%20Force.pdf),
    for licensed identity, controls, Command Select, Battle Plans, commando
    differences, power-up gauge, weapons, lives and mission names.
  - **[P2]** [searchable transcription of the original
    manual](https://www.world-of-nintendo.com/manuals/nes/contra_force.shtml),
    used to cross-check the same original-manual text and catalogue code.
  - **[P3]** [NES Directory cartridge
    record](https://nesdir.github.io/A94591B0_USA.html), for region, catalogue
    `NES-CR-USA`, licensed status, publisher, developer and September 1992
    release. No ROM was downloaded or executed.
- Corroborating textual sources, accessed 2026-09-20:
  - **[S1]** [GameFAQs written FAQ and
    walkthrough](https://gamefaqs.gamespot.com/nes/563400-contra-force/faqs/48160),
    for character rows, single-active upgrade, temporary CPU partner and the
    ordered Dewerdrye Warehouse route through its boss.
  - **[S2]** [Contra Headquarters Mission 1 written
    route](https://contra.kontek.net/games/contraforce/cfc-lev.htm), for the
    dock opening, crushers, fan passage and boss shoot/roll/jump cycle.
- Research record: **[R1]** local preflight on 2026-09-20 found no cartridge,
  console, authorised emulator session, input trace or save. No audiovisual
  evidence was used.
- Claim IDs: `CF-001`–`CF-011`.

## Mechanical decomposition

### Action Genes

- Existing `ACT-008`: directly run and jump the current commando through the
  visible side-scrolling route.
- Existing `ACT-161`: aim the current weapon at a reachable enemy or eligible
  crate, wall or ledge and commit a shot or explosive attack.
- Existing `ACT-202`: crouch without leaving the current local position so the
  body and firing line change for low attacks and hazards.
- Existing `ACT-228`: select another currently available commando on Command
  Select and transfer direct movement, attack and interaction authority.
- Existing `ACT-036`: assign one selected Front, Back, Round, Keep or Assist
  Battle Plan role to one available partner without steering its later steps.
- New `ACT-480`: press SELECT to commit the currently highlighted tier on the
  active commando's power-up gauge rather than waiting for more cases.
- Character names, pad buttons, firearm names and plan labels are parameters.
  Claims: `CF-002`–`CF-007`.

### System Behaviour Genes

- Existing `SYS-045`: ordinary hostiles move and attack without a command for
  each step. Existing `SYS-051`: a summoned partner autonomously acquires and
  fires on compatible nearby hostiles under its current plan.
- Existing `SYS-215`: player and hostile movement, shots, contact, damage and
  defeat resolve continuously. Existing `SYS-755`: compatible weapon damage
  removes a breakable crate, wall or ledge and exposes its declared route or
  contained pickup result.
- Existing `SYS-911`: lethal damage consumes one finite commando life and
  restores the controlled body while stock and mission viability remain.
- New `SYS-929`: a committed Battle Plan stages one selected partner in its
  authored relative role, lets it move and fight autonomously for the short
  plan interval, then removes that assistance without transferring direct
  control.
- New `SYS-930`: each collected case advances the current commando's ordered
  power-up gauge; SELECT converts the highlighted tier into that commando's one
  active weapon or movement capability, replacing the previous selected tier.
- Resolution order: live movement and attacks continue; accepted shots update
  hostiles or breakable objects; pickups advance the current gauge; an explicit
  selection changes active capability; Command Select may transfer authority or
  schedule a partner; partner behaviour resolves until expiry; lethal damage
  consumes a life; boss defeat opens the successor mission. Claims:
  `CF-004`–`CF-010`.

### Constraint Genes

- Existing `CON-442`: running, jumping, crouched firing, weapon use and partner
  commands begin only when the controlled commando's pose, recovery, current
  capability and Command Select state permit them.
- Gauge length, case count, exact attack reach, plan duration, life quantity,
  boss health and stage geometry remain parameters rather than genes.

### Information Genes

- Existing `INF-073`: the interface exposes the current active weapon or
  capability before a local attack.
- Existing `INF-192`: the side-scrolling camera exposes only the nearby route,
  support, machinery, pits and forward lookahead rather than the whole mission.
- Existing `INF-235`: the live view exposes visible hostiles, projectiles,
  breakable objects, power-up cases and current weapon effects.
- New `INF-355`: the joined stage HUD and Command Select surface expose the
  current commando and life stock, the ordered power-up gauge and active tier,
  plus each available roster member's direct-control or Battle Plan assignment
  before confirmation.
- Future enemy positions, hidden case contents and the boss's next exact action
  remain concealed. Claims: `CF-002`, `CF-004`–`CF-009`.

### Objective Genes

- Existing `OBJ-080`: traverse the bounded authored warehouse route, defeat
  its mandatory guardian and cross into the presented battleship mission with
  eligible run state retained. Optional pickups, score and any specific plan or
  commando are not terminal requirements. Claims: `CF-008`, `CF-009`.

### Time Genes

- Existing `TIM-003`: route hazards, hostile movement, projectiles, partner
  actions and boss attacks resolve in real time while the player chooses new
  commands. The pause-owned Command Select surface suspends rather than turns
  the action and does not make the stage turn-based.

## Reproducible transitions

| Before | Action | Deterministic or bounded resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Burn has first ordinary control | Run, jump, crouch and aim through the opening side view | body position and firing angle change while hostile movement remains live | direct side-scrolling combat vocabulary | `CF-003`, `CF-008` |
| A compatible crate blocks or contains a route result | Fire until its break threshold is met | the solid object is removed and its declared route or pickup result resolves | shots affect world objects as well as enemies | `CF-006`, `CF-008` |
| One power-up case is reached | Contact the case | the active commando's gauge advances one authored step | pickups create visible future choice | `CF-006`, `CF-007` |
| The intended gauge tier is highlighted | Press SELECT | that tier becomes the commando's one active weapon or capability and replaces the prior selection | selection, not pickup alone, commits the upgrade | `CF-006`, `CF-007` |
| Burn is assigned `1 PLAYER` on Command Select | Set another available commando to `1 PLAYER` and Burn to `NO USE` | direct control transfers to the chosen commando and its character-specific movement and weapon row become authoritative | live player-selected protagonist switching | `CF-002`, `CF-004` |
| One commando remains directly controlled | Assign another available commando a legal Battle Plan | the partner appears in the plan's relative role, fights autonomously for a short interval and then leaves | temporary planned assistance differs from direct switching | `CF-004`, `CF-005` |
| A hostile is visible while the partner is active | Continue moving or firing | the partner independently acquires compatible targets while preserving the selected plan relation | role assignment drives autonomous combat | `CF-005` |
| A commando takes lethal damage with another life available | Accept lethal resolution | one life is consumed and a controlled body returns while Mission 1 remains viable | finite-life recovery, not save reload | `CF-010` |
| The Warehouse Ringleader is active | Evade its shots, rolls and jumps while returning fire | repeated legal attacks reduce the boss toward defeat | the route ends in a live mandatory guardian | `CF-009` |
| The Warehouse Ringleader reaches defeat | Allow mission settlement | Mission 1 closes and `The U.S.S. Unkmy Battleship` is presented as the successor mission | positive terminal is a crossed progression boundary | `CF-009` |

## Edge-case audit

- Switching direct control and assigning a Battle Plan are different actions:
  the first transfers all player authority, while the second preserves the
  current commando and creates only a short autonomous assistance interval.
- A case does not itself choose the final weapon. It advances the visible gauge;
  SELECT commits the currently highlighted tier, and only one selected upgrade
  remains active for that commando.
- Character-specific jump, speed and weapon order are parameters of the roster
  and gauge systems. They do not justify four duplicate movement or weapon genes.
- Breakable boxes and ledges are world objects under `SYS-755`, not defeated
  living hostiles. Ordinary enemy defeat remains under real-time combat.
- Continue is visible only after exhausted stock and is excluded, so this
  packet does not claim its exact retained gauge, score or roster state.
- Pausing for Command Select changes authority and plan state but does not
  create tactical turns or expose future enemy actions.

## Strategic and experiential structure

- Local decision: align the current commando, choose standing or crouched fire,
  jump a hazard, break a possible pickup container or preserve space against a
  moving hostile.
- Medium horizon: decide whether to spend the current highlighted power tier or
  collect another case, and whether a direct-control switch or temporary plan
  better matches the next warehouse obstacle.
- Long horizon: conserve the finite roster's lives and reach the Ringleader
  with a useful active capability while retaining an eligible state for the
  battleship handoff.
- Feedback: local sprites and projectiles, breakage, pickup contact, gauge
  position, active weapon, roster assignment and life stock distinguish route,
  upgrade, command and failure errors.
- Skill expression: eight-direction firing, jump/crouch timing, breakable-object
  routing, commando choice, gauge commitment and temporary partner timing all
  occur under continuing hostile and machinery pressure.

## Replay and variation

- Mission geometry, major hazards and successor order are authored; no
  procedural stage generation is claimed.
- Character choice changes movement and weapon options. Case availability,
  selected tier, plan, switching, damage, life loss and exact attack sequence
  produce different legal runs without changing the terminal.
- Two-player authority, Continue and later missions introduce different state
  ownership or progression boundaries and remain separate modules.

## Adjacent systems and history

- *Battletoads* shares direct side-view movement, live hostile pressure, finite
  lives, local lookahead and a guardian-opened next stage. Its first level uses
  character-owned melee, health, enemy-to-tool conversion and encounter-gated
  scrolling; Contra Force instead centres direct firearm aim, breakable pickup
  containers, selectable commando authority and short Battle Plan partners.
- *Grand Theft Auto V* shares player-selected direct-control transfer among
  authored protagonists. Its open-world characters persist concurrently across
  broad activities; this packet switches a compact commando roster inside one
  NES mission and separately deploys a temporary autonomous partner.
- *Bad North* shares autonomous combat after a high-level role or movement
  commitment. Its persistent squads traverse an island under group commands;
  Contra Force stages one roster partner for a brief plan-relative interval.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-036`, `ACT-161`, `ACT-202`, `ACT-228`, `ACT-480` | commando, pad mapping, weapon and plan labels are parameters |
| System Behaviour | `SYS-045`, `SYS-051`, `SYS-215`, `SYS-755`, `SYS-911`, `SYS-929`, `SYS-930` | hostile roster, plan duration, gauge length and damage are parameters |
| Constraint | `CON-442` | pose, recovery, selection and availability are parameters |
| Information | `INF-073`, `INF-192`, `INF-235`, `INF-355` | HUD layout, sprites and hidden future state are parameters |
| Objective | `OBJ-080` | warehouse boss and battleship successor are parameters |
| Time | `TIM-003` | update cadence and pause behaviour are parameters |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `323` (`GAME-0001`–`GAME-0323`).
- Exact genome matches: none.
- Tied near matches: `GAME-0318` — Battletoads (`9 / 29 = 0.310345`).
- Supported combination subsets: none.
- Scan date: 2026-09-20.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0318` — Battletoads | `ACT-008`, `SYS-045`, `SYS-215`, `SYS-911`, `CON-442`, `INF-192`, `INF-235`, `OBJ-080`, `TIM-003` | Both use a live side-scrolling route, autonomous enemies, finite-life body replacement, local perception and a guardian-opened next stage. Battletoads centres character-owned melee, health, temporary defeated-enemy tools and encounter-gated scrolling. Contra Force instead uses eight-direction firearms, breakable pickup containers, player-selected commando switching, character-local weapon gauges and short plan-relative autonomous partners. | Near, `9 / 29 = 0.310345` |

### Preserved research notes

- New genes: `ACT-480`, `SYS-929`, `SYS-930` and `INF-355`.
- Classification result: `New gene`; no verified combination is expected.
- Evidence and reasoning: no lower-ID boundary owns an explicit commitment of
  a highlighted character-local weapon gauge, a time-limited plan-relative
  autonomous partner, or one interface joining gauge and roster assignment.

## Taxonomy impact

- Four Active boundaries are added for gauge commitment, temporary Battle Plan
  execution, character-local gauge conversion and joined roster/gauge state.
- Sixteen existing boundaries are reused without wording, lifecycle or earlier
  signature changes. No combination definition changes.

## Negative results

- No cartridge, console, executable, direct play, save/reload comparison,
  screenshot, video or audio evidence exists for this unit.
- No exact plan duration, damage value, enemy count, pickup distribution or
  respawn coordinate is promoted from guide language into a canonical gene.
- Crouching is admitted because it changes the firing posture; ordinary aiming
  direction remains an attack parameter rather than eight separate actions.
- The four commandos do not create four gene sets. Their identities, movement
  values and ordered weapon rows parameterise shared switching and upgrade rules.
- The optional two-player mode, Continue and later missions are excluded rather
  than averaged into the one-player opening-stage packet.

## Delta summary

## New facts

- [Confirmed | Direct | High] The original manual establishes the four-member
  roster, direct-control switch, six Battle Plans, power-up gauge, finite lives
  and the first two mission names (`CF-001`–`CF-007`, `CF-010`).
- [Observation | Corroborated | High] Independent written routes establish the
  bounded warehouse machinery, boss behaviour and successor transition
  (`CF-008`, `CF-009`).

## New genes

- [Confirmed | Direct | High] `ACT-480`, `SYS-929`, `SYS-930` and `INF-355`
  isolate highlighted gauge commitment, temporary plan-relative partner
  execution, character-local gauge conversion and the roster/gauge interface.

## New combinations

- [Observation | Corroborated | High] No new verified combination.

## Taxonomy changes

- [Confirmed | Direct | High] No earlier taxonomy boundary, signature or
  lifecycle state changes; sixteen existing genes are reused as written.

## New questions

- Which exact uncommitted gauge, active weapon and plan states survive each
  performed life loss on an original or lawfully wrapped build?
- Does the cartridge code assign any boss-specific restriction to Command
  Select, switching or Battle Plans that the manual does not state?

## Next recommended game

- [Hypothesis | Limited | Medium] No further game is reserved in the completed
  `GAME-0316`–`GAME-0324` horizon.
- Optimisation criterion: run the nine-game batch closeout and select a new
  reviewed audience-recognition horizon before assigning `GAME-0325`.
- Backlog impact: this unit completes 9/9; no next game starts implicitly.

## Why this game

- [Hypothesis | Limited | High] Contra Force is a recognisable NES-era wildcard
  whose selectable four-person commandos and temporary Battle Plans test a
  distinct squad-control boundary inside a familiar side-scrolling action form.

## Research checklist

- [x] exact original cartridge, one-player mission, entry, terminal and exclusions declared
- [x] original manual and independent written route evidence separated
- [x] direct switching separated from temporary autonomous Battle Plans
- [x] direct-play, executable, reload and audiovisual limits disclosed
- [x] complete six-type gene scan performed
- [x] deterministic lower-ID comparison output integrated
- [x] reviewed Ukrainian localisation and bilingual presentation completed
- [x] original artwork and responsive browser checks completed
