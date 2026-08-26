---
game_id: GAME-0100
slug: keep-talking-and-nobody-explodes
game_title: Keep Talking and Nobody Explodes
analysis_status: reviewed
reviewed: 2026-08-15
combination_ids:
  - COMB-0100
gene_ids:
  action:
    - ACT-099
    - ACT-100
  system:
    - SYS-132
    - SYS-133
  constraint:
    - CON-068
    - CON-151
    - CON-152
    - CON-153
  information:
    - INF-050
  objective:
    - OBJ-031
  time:
    - TIM-003
---

# Game: Keep Talking and Nobody Explodes

## Analysis scope

- Version / ruleset: released base game in configurable local-cooperative Free
  Play, using Bomb Defusal Manual version 1, verification code `241`.
- Included: one Defuser and at least one Expert; unrestricted spoken
  communication; one bomb with exactly one Wires and one Button module; casing
  inspection for serial, batteries and indicators; one wire cut; Button tap or
  hold, strip reveal and timer-conditioned release; module LEDs; countdown,
  strikes, accelerated time, explosion and all-module defusal.
- Excluded: Keypads and every later solvable module; needy modules; campaign
  unlock order; VR-specific presentation; accessibility substitutions; mods,
  community modules, achievements, leaderboards and speedrunning.
- Direct-play status: not conducted. The official game page defines the
  Defuser/Expert visibility split, required communication, procedural bombs and
  configurable Free Play. The official manual supplies the complete scoped
  module, strike, timer and completion rules. The executable control implements
  all published Wires branches, representative Button branches and success,
  strike-acceleration, third-strike and timeout transitions.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `KTN-001` | Steel Crate Games released Keep Talking and Nobody Explodes as a cooperative puzzle game built around a Defuser and manual-reading Experts | Confirmed | Direct | High | P1 |
| `KTN-002` | The Defuser can see and manipulate the bomb but Experts cannot see it; Experts possess the separate rule manual and communication is required | Confirmed | Direct | High | P1, P2 |
| `KTN-003` | A bomb succeeds only after every solvable module is disarmed before countdown expiry; an error records a strike and a standard third strike explodes the bomb | Confirmed | Direct | High | P2 |
| `KTN-004` | Recorded strikes make the countdown run faster, coupling mistake allowance with later decision time | Confirmed | Direct | High | P2 |
| `KTN-005` | Wires contains three to six ordered coloured wires and exactly one correct cut selected by the first applicable count, position and serial-parity rule | Confirmed | Direct | High | P2 |
| `KTN-006` | Button first selects tap or hold through ordered appearance/casing predicates; holding reveals a strip whose colour selects the timer digit for release | Confirmed | Direct | High | P2 |
| `KTN-007` | The bounded control reproduces twelve Wires cases, representative Button precedence, complete defusal, accelerated time, third-strike failure and timeout | Observation | Direct | High | V1 |

## Basic data

- Release / origin: developed and published by Steel Crate Games; initially
  released in 2015 after an earlier VR prototype.
- Platform or physical form: local or remote spoken-cooperative digital game
  with one running game copy and a freely viewable companion manual.
- Puzzle family: asymmetric-information cooperative procedure translation.
- Creator and primary sources:
  - **[P1]** [Official game page](https://keeptalkinggame.com/), for role
    separation, communication, procedural bombs, platforms and Free Play.
  - **[P2]** [Official Bomb Defusal Manual version 1](https://www.bombmanual.com/web/),
    verification code `241`, for bomb, module, timer, strike, Wires, Button and
    casing-reference rules.
  - **[P3]** [Official FAQ](https://keeptalkinggame.com/faq/), for configurable
    Free Play module exclusions and the base/mod boundary.
  - **[V1]** [`verify_keep_talking_control.py`](../../../scripts/verify_keep_talking_control.py),
    an executable scoped rule table and attempt-state control.

## Mechanical decomposition

### Action Genes

- `ACT-099` — communicate role-exclusive observation or instruction. The
  Defuser describes module and casing state; Experts query missing fields and
  return the accepted cut or button procedure.
- `ACT-100` — commit addressed bomb-module control. The Defuser cuts one wire,
  taps the Button, or holds and releases it at a selected timer instant.
- Bomb rotation and visual inspection are supporting access operations, not
  separate genes in this scope: they reveal parameters consumed by the role
  partition and do not themselves advance or resolve a module.

### System Behaviour Genes

- `SYS-132` — rule-conditioned bomb-module adjudication. A correct committed
  control lights the module's green LED and permanently removes that task; an
  incorrect one records a strike.
- `SYS-133` — strike-triggered countdown acceleration. A retained first or
  second strike increases the same timer's rate for the remaining modules.
- Resolution order: accept the committed module control; resolve the first
  applicable manual branch; disarm or strike; accelerate time after a retained
  strike; explode at the strike threshold or zero time; otherwise check whether
  all modules are disarmed.

### Constraint Genes

- `CON-068` — fixed attempt deadline with terminal expiry. The countdown
  decreases during communication and control; zero explodes the bomb.
- `CON-151` — role-exclusive state and control authority. Experts cannot view
  or manipulate the bomb, and the Defuser is the sole live operator.
- `CON-152` — first-applicable ordered module-rule precedence. Later matching
  Wires or Button cases cannot override the earliest true branch.
- `CON-153` — finite recoverable-strike allowance. A standard strike indicator
  permits two retained mistakes and makes the third terminal.
- Scarce strategic resources: remaining real time and unspent strike capacity.

### Information Genes

- `INF-050` — complementary role-partitioned rules and live state. The Defuser
  sees current modules, timer, strikes and casing; Experts see the authoritative
  manual procedure but not the current bomb instance.
- `INF-001` does not transfer: no one role sees every decision-relevant state
  and rule element before communication.

### Objective Genes

- `OBJ-031` — complete authored room task set. Both heterogeneous mandatory
  modules must be disarmed; completing Wires alone or Button alone is
  insufficient.
- The objective is not score maximisation and surviving until timeout is not a
  success condition.

### Time Genes

- `TIM-003` — real-time input during forced progression. The countdown keeps
  advancing while players inspect, speak and operate modules; an error changes
  its rate without creating a turn boundary.

## Reproducible transitions

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Four wires `red, blue, yellow, white`; serial ends `5` | Expert evaluates ordered four-wire rules; Defuser cuts first wire | The single-blue branch is first applicable; Wires disarms | state description, precedence and committed control | `KTN-002`, `KTN-005`, `KTN-007` |
| Same Wires state | Cut second wire | Module remains active, strike becomes one and timer rate increases | incorrect action affects two resources | `KTN-003`, `KTN-004`, `KTN-007` |
| Yellow Button labelled `Abort`, two batteries, no lit indicators | Hold Button | Yellow rule selects hold; blue strip appears | an intermediate observation is created only after commitment | `KTN-006`, `KTN-007` |
| Held Button with blue strip; timer shows `4:42` | Release | A visible `4` satisfies the blue-strip rule and Button disarms | timed release depends on live shared state | `KTN-006`, `KTN-007` |
| Wires and Button both green with positive time and fewer than three strikes | Complete second module | Bomb is defused immediately | heterogeneous task conjunction | `KTN-003`, `KTN-007` |
| Two retained strikes | Commit another incorrect control | Third strike explodes the bomb | finite recoverable error threshold | `KTN-003`, `KTN-007` |
| Any unresolved module; timer reaches `0:00` | No successful completion first | Bomb explodes | fixed live deadline | `KTN-003`, `KTN-007` |

## Strategic and experiential structure

- Local decision: translate a visible module instance into the minimal exact
  description that lets an Expert select the first applicable rule.
- Medium-term planning: split manual lookup among Experts, confirm ambiguous
  words and casing facts, and choose whether to finish a partly understood
  module or switch to the other one while time continues.
- Long-term structure: preserve both strike capacity and communication time;
  each mistake makes every remaining lookup more expensive.
- Common heuristics: announce module type first, use top-to-bottom wire order,
  state counts before positions, and avoid releasing a held Button until strip
  colour and a matching timer digit are confirmed.
- Failure attribution: the visible strike, module state and timer make an
  incorrect description, lookup or physical input traceable, though speech
  ambiguity can leave social rather than system-local causality.
- Player-trust factors: the manual is authoritative and public; identical
  described state must choose the same action, and the first-match order must
  not be silently reordered.

## Replay and variation

- Free Play can generate different module instances, colours, labels, casing
  facts and timers while retaining the same manual procedure.
- Human vocabulary, delegation and lookup speed create variation even for the
  same bomb state.
- The scoped Wires/Button packet admits different solution order and
  communication strategy but only one accepted committed control per concrete
  module state.

## Adjacent systems and history

- Mastermind and Black Box also combine hidden facts with rule-guided queries,
  but one player owns both observation and commitment; neither partitions the
  procedure across communicating human roles.
- Pikmin 4 supports cooperative work inside one visible simulation, but its
  followers are simulated agents rather than Experts holding inaccessible
  rules.
- Lemmings shares a terminal real-time deadline, while its skills and state are
  available to one operator and errors do not accelerate the clock through a
  persistent strike counter.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-099`, `ACT-100` | spoken vocabulary, wire cut, Button press/hold/release |
| System Behaviour | `SYS-132`, `SYS-133` | module branch and strike-rate multipliers |
| Constraint | `CON-068`, `CON-151`, `CON-152`, `CON-153` | timer, role authority, ordered rules, strike threshold |
| Information | `INF-050` | bomb fields, manual pages and communication channel |
| Objective | `OBJ-031` | two mandatory heterogeneous modules |
| Time | `TIM-003` | continuously advancing countdown |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `99` (`GAME-0001`–`GAME-0099`).
- Exact genome matches: none.
- Tied near matches: `GAME-0025` — Lemmings (`2 / 20 = 0.100000`).
- Supported combination subsets: `COMB-0100`.
- Scan date: 2026-08-15.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| Lemmings (`GAME-0025`) | `CON-068`, `TIM-003` | one operator assigns finite skills to visible autonomous agents; Keep Talking partitions state, procedure and control between communicating humans and couples mistakes to timer rate | Near, `0.100000` |

### Preserved research notes

- New genes: `ACT-099`, `ACT-100`, `SYS-132`, `SYS-133`, `CON-151`,
  `CON-152`, `CON-153`, `INF-050`.
- Classification result: `New gene` and `New combination of known and new
  genes`.
- Evidence and reasoning: the official role contract, manual rule tables and
  executable control reproduce each new boundary. Existing timer, task-set and
  live-time genes transfer without changing their operational definitions.

## Taxonomy impact

- Registry changes: add eight Active genes with this game as the analysed
  example.
- Taxonomy-change record: none; no prior definition is rewritten.
- Candidate terms affected: role communication is admitted only when the
  information partition is mechanically enforced, not for optional discussion.

## Negative results

- `INF-001` does not transfer because no single role sees the complete live
  state and authoritative rules.
- `SYS-089` does not transfer: module adjudication is not a concealed binary
  cell classification and may require a time-sensitive multi-stage gesture.
- `CON-020` does not transfer: correct actions do not consume strike capacity,
  and exhaustion is an error threshold rather than a general move budget.

## Delta summary

## Нові факти

- [Confirmed | Direct | High] Сапер бачить і керує бомбою без інструкції, а
  Експерти бачать інструкцію без бомби; розв’язання потребує комунікації.
- [Confirmed | Direct | High] Помилка не лише додає strike, а й прискорює
  спільний таймер для решти модулів.

## Нові гени

- [Observation | Corroborated | High] `ACT-099`, `ACT-100`, `SYS-132`,
  `SYS-133`, `CON-151`, `CON-152`, `CON-153`, `INF-050`.

## Нові комбінації

- [Confirmed | Corroborated | High] `COMB-0100` — передати розділені між
  ролями стан і правила та виконати правильну дію до спливу часу.

## Зміни таксономії

- [Observation | Direct | High] Змін таксономії немає; три перевірені старі
  гени повторно використано без розширення меж.

## Нові питання

- Чи переноситься `INF-050` на мовні ігри, де один гравець сам почергово бачить
  контекст і словник, чи там немає справжнього рольового поділу?

## Наступна рекомендована гра

- [Hypothesis | Corroborated | High] Chants of Sennaar.
- Optimisation criterion: test semantic-hypothesis maintenance and notebook
  confirmation without repeating the two-role communication boundary.
- Expected information gain: distinguish one-player contextual translation
  from role-partitioned manual lookup.
- Backlog impact: promote Chants of Sennaar for `GAME-0101`; retain The
  Password Game and Papers, Please.

## Чому саме вона

- [Hypothesis | Corroborated | High] The publisher's playable-demo boundary
  offers strong mechanical distance while directly falsifying whether
  `INF-050` is about separated interfaces or merely incomplete language
  knowledge.
