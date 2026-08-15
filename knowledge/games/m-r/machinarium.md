---
game_id: GAME-0086
slug: machinarium
game_title: Machinarium
analysis_status: reviewed
reviewed: 2026-08-14
combination_ids:
  - COMB-0086
gene_ids:
  action:
    - ACT-085
    - ACT-087
    - ACT-088
    - ACT-089
    - ACT-090
    - ACT-091
  system:
    - SYS-112
    - SYS-113
  constraint:
    - CON-136
  information:
    - INF-001
    - INF-036
  objective:
    - OBJ-044
  time:
    - TIM-002
---

# Game: Machinarium

## Analysis scope

- Version / ruleset: Amanita Design's released Machinarium, restricted to the
  platform-neutral state transitions of the opening scrapyard, from Josef's
  separated head under the scrap heap through recovery of his second arm and
  traversal to the next scene.
- Included: removing the tub; exposing and dropping the torso; attaching the
  head; extending and contracting Josef's articulated body; reading the small
  robot's pictorial request; collecting and giving the doll; receiving and
  attaching the missing leg; collecting the magnet and string; combining both
  into one inventory tool; walking to and bending the pole; applying the
  composite rig; recovering the missing arm; leaving the scrapyard; persistent
  authored scene state; self-paced deterministic interaction.
- Excluded: the city-gate scene and every later puzzle; the full-game rescue
  narrative; walkthrough hint minigame; exact touch-versus-pointer gestures;
  idle animation, camera framing, music, art style, achievements, saves,
  platform features and speedrunning.
- Direct-play status: not conducted. Amanita Design's product page and Steam
  listing establish the released single-player adventure and scrap-heap
  premise. Three independent walkthroughs agree on the bounded object,
  exchange, combination, pole, arm and exit sequence. The local verifier
  formalises only those corroborated state dependencies.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `MAC-001` | Machinarium is Amanita Design's full-length adventure about a robot exiled to a scrap heap who must use logic and collect important items | Confirmed | Direct | High | F1, F2 |
| `MAC-002` | Removing the tub exposes Josef's torso, which must be dropped beside and joined to the separated head | Confirmed | Corroborated | High | S1–S3 |
| `MAC-003` | The assembled partial body can change height, and its extended configuration is required to reach the high doll | Confirmed | Corroborated | High | S1–S3 |
| `MAC-004` | Interacting with the small robot reveals a pictorial request for that doll | Confirmed | Corroborated | High | S1–S3 |
| `MAC-005` | Giving the collected doll consumes it and causes the small robot to return Josef's missing leg, enabling walking | Confirmed | Corroborated | High | S1–S3 |
| `MAC-006` | Magnet and string are separately collected and deliberately combined into one composite inventory tool | Confirmed | Corroborated | High | S1–S3 |
| `MAC-007` | The pole must be prepared and the composite magnet-and-string rig applied to recover Josef's missing arm | Confirmed | Corroborated | High | S1–S3 |
| `MAC-008` | Arm recovery completes the bounded scene and permits traversal across the pool to the next area | Confirmed | Corroborated | High | S1–S3 |
| `MAC-009` | The executable control contains 14 accepted milestones and rejects ten tested prerequisite violations | Observation | Direct | High | V1, MAC-002–MAC-008 |
| `MAC-010` | The bounded packet is deterministic and self-paced; no random or time-driven transition intervenes between decisions | Observation | Corroborated | High | S1–S3 |
| `MAC-011` | Pointer location and animation expose affordances but are not promoted unless the resulting state changes future legal interaction | Observation | Corroborated | High | S1–S3 |

## Basic data

- Release / origin: developed and published by Amanita Design; released on
  16 October 2009 according to the Steam product record.
- Platform or physical form: single-player two-dimensional point-and-click
  adventure with scene-local navigation, articulated avatar configuration and
  a persistent item inventory.
- Puzzle family: authored inventory-dependency scene with avatar restoration.
- Primary sources:
  - **[F1]** [Amanita Design — Machinarium](https://amanita-design.net/games/machinarium.html),
    for the scrap-heap premise, logic, important-item collection and objective
    of returning the robot to the city.
  - **[F2]** [Machinarium on Steam](https://store.steampowered.com/app/40700/Machinarium/),
    for developer, publisher, release date, single-player form and Josef.
- Reproducible corroboration:
  - **[S1]** [Pro Game Guides — complete Machinarium walkthrough](https://progameguides.com/machinarium/machinarium-walkthrough/),
    for the illustrated scrapyard sequence from tub through arm recovery.
  - **[S2]** [StrategyWiki — Machinarium walkthrough](https://strategywiki.org/wiki/Machinarium/Walkthrough),
    independently corroborating assembly, doll exchange, magnet-string
    combination and pole use.
  - **[S3]** [Gamer Walkthroughs — Part 1](https://gamerwalkthroughs.com/machinarium/part-1-prison-escape/),
    independently corroborating height control, requested doll, missing leg,
    composite hook and exit transition.
  - **[V1]**
    [`verify_machinarium_control.py`](../../../scripts/verify_machinarium_control.py),
    an executable state machine for fourteen milestones, one two-item
    combination, two restored limbs and ten rejected prerequisite violations.

## Mechanical decomposition

### Player actions

- `ACT-085` — manipulate constrained diegetic component. The tub, exposed
  torso and fixed pole are each committed through one authored local state.
- `ACT-087` — apply held item to compatible fixture. The completed
  magnet-and-string rig is deliberately committed to the prepared pole.
- `ACT-088` — reconfigure articulated avatar reach. Josef's torso height
  changes the set of scene objects his hand can reach.
- `ACT-089` — collect addressed scene item into inventory. The doll, magnet and
  string leave their visible scene positions and persist as held identities.
- `ACT-090` — combine two held inventory items. Magnet and string are consumed
  as separate identities and replaced by one usable composite rig.
- `ACT-091` — give held item to addressed character. The selected doll is
  transferred to the small robot whose request accepts it.

### System behaviours

- `SYS-112` — compatible fixture activation exposes dependent mechanism state.
  Removing the cover reveals the torso; using the prepared rig resolves into
  arm recovery and the traversal transition.
- `SYS-113` — requested item hand-in grants capability component. Accepting the
  doll returns and attaches the missing leg, enabling locomotion.

### Constraints

- `CON-136` — persistent prerequisite-gated mechanism dependency. Body
  assembly gates height control, height gates the doll, the doll gates walking,
  walking gates tool collection, both constituents gate combination, and the
  prepared pole plus composite rig gate arm recovery and exit.

### Information

- `INF-001` — fully visible current state. Every currently exposed scene
  object, Josef configuration, inventory identity and prepared pole state is
  inspectable before the next interaction.
- `INF-036` — pictorial requested-item disclosure. The small robot's bubble
  identifies the doll as its accepted current hand-in without spoken text.

### Objective

- `OBJ-044` — restore required avatar components and leave bounded scene. The
  packet ends only after both missing limbs are restored and Josef traverses
  out of the scrapyard.

### Time

- `TIM-002` — self-paced sequential action. The scene does not advance while
  the player inspects objects, inventory or the request bubble.

## Reproducible transitions

The executable control encodes this accepted trace:

1. Remove the tub, expose the torso and drop it beside Josef's head.
2. Attach the head to the torso and extend the articulated body.
3. Collect the high doll, contract, and give the doll to the requesting robot.
4. Receive and attach the missing leg, enabling walking.
5. Collect the magnet and string as separate inventory identities.
6. Combine both constituents into the magnet-and-string rig.
7. Walk to the pole and bend it into its prepared state.
8. Apply the composite rig, recover the missing arm and leave the scrapyard.

Ten controls separately reject torso access while covered, premature assembly
or height change, doll collection without extension, exchange without the
doll, tool collection without locomotion, incomplete combination, remote pole
manipulation, rig use without both prerequisites and exit before arm recovery.

## Strategic and experiential structure

- The scene teaches a causal inventory grammar without text: visible body
  incompleteness establishes the objective, while the request bubble reveals
  one local exchange relation.
- Avatar configuration is a stateful tool. Extending Josef is not animation or
  camera access because it changes which item is legally reachable.
- The doll exchange and the magnet-string combination are different decisions:
  one transfers an item to another actor for a capability, while the other
  replaces two held identities with a fixture-compatible composite.
- Persistent progress reduces the dependency graph until the recovered arm
  turns the far side from inaccessible presentation into an available exit.

## Replay and variation

- The scoped scene uses one authored layout, item set and dependency chain.
- Restarting changes neither request identity nor constituent compatibility.
- Later scenes broaden inventory interactions but cannot support this record's
  genes because they lie outside the declared boundary.

## Adjacent systems and history

- Graphic adventures supply the general item-to-hotspot lineage, but this
  record separates collection, character hand-in, item combination and fixture
  application instead of treating every pointer click as one action.
- The Room is the nearest corpus control because both games use persistent
  item–fixture dependency chains. Machinarium lacks a reconfigurable single
  key and instrument-only visual layer; it instead adds avatar reach, explicit
  item combination and a pictorial character request.
- SET shares selection and combination only in ordinary language; its formal
  operation chooses a three-card relational subset and never creates a held
  composite tool.

## Normalised genome

| Type | IDs | Key parameters |
|---|---|---|
| Action | `ACT-085`, `ACT-087`, `ACT-088`, `ACT-089`, `ACT-090`, `ACT-091` | local components; two body heights; three pickups; one combination; one hand-in |
| System | `SYS-112`, `SYS-113` | persistent reveal; requested-item capability grant |
| Constraint | `CON-136` | authored 14-milestone dependency chain |
| Information | `INF-001`, `INF-036` | visible scene state; pictorial doll request |
| Objective | `OBJ-044` | restore missing leg and arm, then exit |
| Time | `TIM-002` | self-paced; no autonomous scene progression |

Compact signature:

`ACT-085,ACT-087,ACT-088,ACT-089,ACT-090,ACT-091; SYS-112,SYS-113; CON-136; INF-001,INF-036; OBJ-044; TIM-002`

## Corpus comparison

The comparison scanned every complete `GAME-0001`–`GAME-0085` signature with
canonical Jaccard intersection over union.

- Near match: `GAME-0085` The Room is uniquely nearest at
  `5 / 19 = 0.263158`.

| Prior game | Shared genes | Boundary | Jaccard |
|---|---|---|---:|
| `GAME-0085` — The Room | `ACT-085`, `ACT-087`, `SYS-112`, `CON-136`, `TIM-002` | reshapes one key and uses an optical layer to open a safe; no avatar restoration, character exchange or two-item combination | nearest, `5 / 19 = 0.263158` |
| `GAME-0064` — SET | `INF-001`, `TIM-002` | selects a relational three-card subset; creates no inventory composite | next, `2 / 16 = 0.125000` |
| `GAME-0002` — Rubik's Cube | `INF-001`, `TIM-002` | reversible layer turns toward one visible arrangement; no authored dependency chain | background tie, `2 / 18 = 0.111111` |
| `GAME-0063` — Rush Hour | `INF-001`, `TIM-002` | slides fixed vehicles to clear an exit; no item acquisition or capability restoration | background tie, `2 / 18 = 0.111111` |

No prior full signature is exact, no prior combination equals the candidate and
no prior combination is a supported subset of the complete genome. The Room's
moderate lead validates the intended control: both share a staged item–fixture
chain, while Machinarium removes reshaping and optical evidence and adds a
character request, item combination and avatar restoration.

- Full numeric scan (`intersection / union = Jaccard`):
  - `GAME-0001`: `1 / 26 = 0.038462`; `GAME-0002`: `2 / 18 = 0.111111`; `GAME-0003`: `0 / 22 = 0.000000`; `GAME-0004`: `1 / 27 = 0.037037`; `GAME-0005`: `2 / 18 = 0.111111`; `GAME-0006`: `2 / 20 = 0.100000`; `GAME-0007`: `2 / 19 = 0.105263`; `GAME-0008`: `2 / 18 = 0.111111`.
  - `GAME-0009`: `1 / 28 = 0.035714`; `GAME-0010`: `1 / 21 = 0.047619`; `GAME-0011`: `2 / 24 = 0.083333`; `GAME-0012`: `2 / 20 = 0.100000`; `GAME-0013`: `1 / 25 = 0.040000`; `GAME-0014`: `1 / 27 = 0.037037`; `GAME-0015`: `1 / 26 = 0.038462`; `GAME-0016`: `1 / 27 = 0.037037`.
  - `GAME-0017`: `0 / 26 = 0.000000`; `GAME-0018`: `1 / 31 = 0.032258`; `GAME-0019`: `1 / 22 = 0.045455`; `GAME-0020`: `1 / 26 = 0.038462`; `GAME-0021`: `1 / 21 = 0.047619`; `GAME-0022`: `1 / 24 = 0.041667`; `GAME-0023`: `1 / 22 = 0.045455`; `GAME-0024`: `1 / 24 = 0.041667`.
  - `GAME-0025`: `1 / 23 = 0.043478`; `GAME-0026`: `1 / 24 = 0.041667`; `GAME-0027`: `1 / 24 = 0.041667`; `GAME-0028`: `1 / 29 = 0.034483`; `GAME-0029`: `1 / 24 = 0.041667`; `GAME-0030`: `1 / 26 = 0.038462`; `GAME-0031`: `1 / 23 = 0.043478`; `GAME-0032`: `1 / 23 = 0.043478`.
  - `GAME-0033`: `1 / 25 = 0.040000`; `GAME-0034`: `1 / 26 = 0.038462`; `GAME-0035`: `1 / 30 = 0.033333`; `GAME-0036`: `2 / 23 = 0.086957`; `GAME-0037`: `1 / 21 = 0.047619`; `GAME-0038`: `1 / 28 = 0.035714`; `GAME-0039`: `2 / 20 = 0.100000`; `GAME-0040`: `2 / 19 = 0.105263`.
  - `GAME-0041`: `1 / 23 = 0.043478`; `GAME-0042`: `1 / 21 = 0.047619`; `GAME-0043`: `1 / 26 = 0.038462`; `GAME-0044`: `1 / 22 = 0.045455`; `GAME-0045`: `1 / 26 = 0.038462`; `GAME-0046`: `2 / 21 = 0.095238`; `GAME-0047`: `1 / 26 = 0.038462`; `GAME-0048`: `1 / 26 = 0.038462`.
  - `GAME-0049`: `0 / 22 = 0.000000`; `GAME-0050`: `1 / 27 = 0.037037`; `GAME-0051`: `1 / 28 = 0.035714`; `GAME-0052`: `1 / 22 = 0.045455`; `GAME-0053`: `1 / 21 = 0.047619`; `GAME-0054`: `1 / 23 = 0.043478`; `GAME-0055`: `1 / 22 = 0.045455`; `GAME-0056`: `1 / 20 = 0.050000`.
  - `GAME-0057`: `1 / 20 = 0.050000`; `GAME-0058`: `1 / 21 = 0.047619`; `GAME-0059`: `1 / 19 = 0.052632`; `GAME-0060`: `1 / 19 = 0.052632`; `GAME-0061`: `2 / 21 = 0.095238`; `GAME-0062`: `2 / 19 = 0.105263`; `GAME-0063`: `2 / 18 = 0.111111`; `GAME-0064`: `2 / 16 = 0.125000`.
  - `GAME-0065`: `1 / 19 = 0.052632`; `GAME-0066`: `1 / 22 = 0.045455`; `GAME-0067`: `0 / 21 = 0.000000`; `GAME-0068`: `1 / 20 = 0.050000`; `GAME-0069`: `2 / 19 = 0.105263`; `GAME-0070`: `1 / 20 = 0.050000`; `GAME-0071`: `2 / 18 = 0.111111`; `GAME-0072`: `2 / 19 = 0.105263`.
  - `GAME-0073`: `2 / 18 = 0.111111`; `GAME-0074`: `2 / 20 = 0.100000`; `GAME-0075`: `2 / 20 = 0.100000`; `GAME-0076`: `2 / 18 = 0.111111`; `GAME-0077`: `2 / 18 = 0.111111`; `GAME-0078`: `2 / 18 = 0.111111`; `GAME-0079`: `2 / 18 = 0.111111`; `GAME-0080`: `2 / 18 = 0.111111`.
  - `GAME-0081`: `2 / 19 = 0.105263`; `GAME-0082`: `2 / 19 = 0.105263`; `GAME-0083`: `2 / 19 = 0.105263`; `GAME-0084`: `2 / 21 = 0.095238`; `GAME-0085`: `5 / 19 = 0.263158`.

## Combination candidate

- Candidate ID: `COMB-0086`.
- Gene set: `ACT-088`, `ACT-089`, `ACT-090`, `ACT-091`, `SYS-113`, `CON-136`,
  `INF-036`, `OBJ-044`.
- Supporting game: `GAME-0086`.
- Proper-subset rationale: `ACT-085`, `ACT-087`, `SYS-112`, `INF-001` and
  `TIM-002` execute or expose the scene but do not define the requested-item
  exchange, composite tool and avatar-restoration chain.
- Novelty claim: not assessed.

## Outcome

- Reused genes: `ACT-085`, `ACT-087`, `SYS-112`, `CON-136`, `INF-001`,
  `TIM-002`.
- Added genes: `ACT-088`, `ACT-089`, `ACT-090`, `ACT-091`, `SYS-113`,
  `INF-036`, `OBJ-044`.
- Added combination: `COMB-0086`.
- Evidence gate: passed with two primary product sources, three independently
  agreeing walkthroughs and one executable dependency verifier.
- Nearest prior genome: The Room at `5 / 19 = 0.263158`.
- Next falsification target: a bounded adventure scene with inventory
  combination but no avatar restoration or character exchange.

## Taxonomy impact

- Inventory pickup, character hand-in, two-item combination and fixture
  application are now separate action families rather than generic “use item”.
- Articulated avatar reach is promoted because it changes legal affordances;
  ordinary animation and pointer motion remain excluded.
- Character request information is separated from the exchange consequence:
  the bubble changes knowledge, while the hand-in changes inventory and
  capability state.
- The Room's persistent dependency constraint survives a mechanically distinct
  adventure scene, but its articulated-key and optical-layer genes do not.

## Negative results

- Walking between reachable scene positions is access, not a gene in this
  bounded packet.
- The hand-drawn presentation and non-verbal storytelling do not become genes.
- The magnet rig is one deterministic combination, not a general crafting
  economy or recipe-discovery system.
- The walkthrough hint feature is excluded rather than classified as normal
  puzzle information.
- The verifier proves the documented dependency order, not that no alternate
  gesture ordering exists within each animation.

## Delta summary

- Added one reviewed game record and one verified combination.
- Added four Action genes, one System Behaviour gene, one Information gene and
  one Objective gene.
- Extended two Actions, one System Behaviour, one Constraint, one Information
  and one Time gene with Machinarium evidence.
- Added an executable fourteen-milestone state-machine control.

## Нові факти

- Межу звужено до стартового звалища від розділеного тіла до переходу в
  наступну сцену.
- Висота тіла Джозефа змінює доступність предметів, а не лише анімацію.
- Піктограма малого робота прямо повідомляє потрібний предмет.
- Лялька обмінюється на ногу, тоді як магніт і мотузка об'єднуються в новий
  інструмент для повернення руки.
- Перевірено 14 послідовних віх і десять порушень передумов.

## Нові гени

- `ACT-088` — змінити конфігурацію шарнірного аватара для іншої досяжності.
- `ACT-089` — зібрати адресований предмет сцени в інвентар.
- `ACT-090` — об'єднати два предмети інвентарю.
- `ACT-091` — передати предмет адресованому персонажу.
- `SYS-113` — передача запитаного предмета надає компонент здібності.
- `INF-036` — піктографічне повідомлення про запитаний предмет.
- `OBJ-044` — відновити потрібні компоненти аватара й залишити сцену.

## Нові комбінації

- `COMB-0086` — обмін запитаного предмета та композитний інструмент для виходу
  зі сцени.

## Зміни таксономії

- `ACT-085`, `ACT-087`, `SYS-112`, `CON-136`, `INF-001` і `TIM-002`
  розширено доказами Machinarium.
- Ходьбу, рух курсора, анімацію й художній стиль залишено поза геномом, коли
  вони не створюють окремого станового рішення.

## Український підсумок

Стартове звалище Machinarium навчає не одному універсальному кліку, а кільком
різним операціям. Джозеф змінює висоту, щоб дістати ляльку; передає її
персонажу й отримує ногу; окремо збирає магніт і мотузку, об'єднує їх у новий
інструмент та застосовує до підготовленої опори, щоб повернути руку й вийти зі
сцени. The Room закономірно став найближчим контролем через спільний стійкий
ланцюг предметів і пристроїв, але схожість лишається помірною:
`5 / 19 = 0.263158`.
