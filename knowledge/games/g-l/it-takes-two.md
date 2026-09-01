---
game_id: GAME-0215
slug: it-takes-two
game_title: It Takes Two
analysis_status: reviewed
reviewed: 2026-09-01
combination_ids:
  - COMB-0213
gene_ids:
  action:
    - ACT-008
    - ACT-049
    - ACT-385
    - ACT-386
  system:
    - SYS-036
    - SYS-065
    - SYS-215
    - SYS-429
    - SYS-430
    - SYS-710
  constraint:
    - CON-047
    - CON-076
    - CON-378
    - CON-558
  information:
    - INF-001
    - INF-167
  objective:
    - OBJ-086
  time:
    - TIM-003
---

# Game: It Takes Two

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Parameters describe
gene instances but do not enter the signature.

## Analysis scope

- Version / ruleset: current unmodified English Windows Steam release, app
  `1426210`, public Build ID `18385016`, built 2025-05-08 and published to the
  public branch by 2025-05-20, checked 2026-09-01; one fresh local couch-co-op
  run with a full game copy, default controls and two controllers.
- Platform and mode: Windows local split-screen cooperative Story. One human
  controls Cody and one controls May; neither role has an AI substitute.
- Entry: first retained control in `The Depths`, after May receives the hammer
  and Cody receives his first reusable nail. The earlier vacuum, platform and
  tutorial sequence is not retained.
- Primary decision loop: each player reads both live panes and announces the
  next dependency; Cody aims, throws and recalls his bounded nail set to pin
  moving mechanisms, trigger marked switches or create swing anchors; May
  strikes marked buttons and locks with the hammer or traverses Cody's placed
  anchors. Both preserve the live segment through individual failure, evade
  hazards and combine those fixed roles to open the next route.
- Positive terminal: after `Wired Up`, both players defeat the Toolbox by
  pinning its arm, placing swing anchors, breaking both locks and hammer-
  launching Cody onto the explosive can; the complete post-boss transition
  settles `The Shed` and advances to the next chapter. Reaching one checkpoint
  or reducing one boss phase is not completion.
- Negative terminal: one failed actor returns while the partner remains active;
  overlapping failure of both actors restores the current authored checkpoint.
  Neither state is positive completion.
- Included: direct run, jump, dash, wall traversal and swinging; persistent
  split-screen; May's hammer strikes; Cody's finite reusable nails, eligible
  yellow marks, placement and instant recall; pinning platforms, switch contact
  and swing-anchor use; the mandatory `The Depths` and `Wired Up` routes;
  Toolbox hazards and staged settlement; individual return and pair-wipe reset.
- Excluded: `Wake-up Call`, vacuum tools, `The Vacuum Tower` and all earlier
  first-chapter state; `The Tree` and every later chapter/ability; optional
  minigames, achievements and collectibles; online co-op, Friend's Pass,
  Remote Play Together, EA-account/network state, chapter-select replay,
  accessibility variants, other platforms and the complete campaign/story.
- Reproducible parameterisation: use Steam app `1426210`, Local Play, a new
  Story save and two controllers. Continue only to the first hammer-and-nails
  control in `The Depths`, then retain every mandatory route and Toolbox phase
  until the chapter transition completes. Stop before either player acts in
  `The Tree`.
- Potential scoped modules: the vacuum packet, one later paired-ability
  chapter, one optional minigame, online Friend's Pass entitlement or the full
  campaign each requires a separate version, entry and terminal.
- Direct-play status: not conducted. EA and Steam establish the current
  two-human local split-screen product and changing level abilities; SteamDB
  fixes the public build; independent text walkthroughs reproduce the hammer,
  nail, route and Toolbox transitions. This is evidence-based rules
  reconstruction. No video or audio was opened, played, heard or used.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `ITT-001` | It Takes Two is built exclusively for two-player cooperation and supports local split-screen on Windows | Confirmed | Direct | High | P1, P2, P3 |
| `ITT-002` | Steam app `1426210` currently exposes public Windows Build `18385016` | Confirmed | Corroborated | High | P1, S1 |
| `ITT-003` | Levels replace the protagonists' connected abilities; this unit therefore admits only the hammer-and-nails packet | Confirmed | Direct | High | P1, P3 |
| `ITT-004` | In `The Depths`, May uses the hammer while Cody throws and instantly recalls a bounded set of nails | Observation | Corroborated | High | S2, S3 |
| `ITT-005` | Eligible yellow targets let nails pin moving platforms, operate switches and become May's swing anchors | Observation | Corroborated | High | S2, S3 |
| `ITT-006` | May's hammer activates marked fixtures and breaks route or boss locks that Cody cannot resolve | Observation | Corroborated | High | S2, S3 |
| `ITT-007` | One failed player may return while the partner lives, whereas both failing restores an authored checkpoint | Observation | Corroborated | High | S4, S5 |
| `ITT-008` | The Toolbox fight requires both tools across pin, swing, lock and launch stages | Observation | Corroborated | High | S2, S3 |
| `ITT-009` | Defeating Toolbox and completing its transition closes the bounded Shed packet | Observation | Corroborated | High | S2, S3 |
| `ITT-010` | Local couch co-op requires no network or Friend's Pass entitlement | Confirmed | Direct | High | P2 |

## Basic data

- Release / origin: Hazelight Studios; Electronic Arts released It Takes Two
  on 2021-03-25.
- Platform or physical form: real-time third-person two-human cooperative
  action-platform chapter on Windows; only the declared local Story packet is
  scoped.
- Puzzle family: physics and object manipulation; real-time system pressure;
  world topology and perspective; agent routing and coordination.
- Primary and official sources:
  - **[P1]** [official Steam product page](https://store.steampowered.com/app/1426210/It_Takes_Two/),
    for title, release, Windows, Hazelight/EA, local and online split-screen,
    two-player co-op and connected abilities that change by level.
  - **[P2]** [official Friend's Pass rules](https://www.ea.com/en/games/it-takes-two/it-takes-two/features/friends-pass),
    for local couch co-op without internet, full-copy/Friend's Pass boundaries
    and host save/chapter behaviour.
  - **[P3]** [official availability article](https://www.ea.com/ea-play/news/it-takes-two-is-available-now),
    for collaboration-only progress, split-screen and level-specific abilities.
- Reproducible mechanics sources:
  - **[S1]** [SteamDB public depots](https://steamdb.info/app/1426210/depots/),
    for public Build `18385016` and its branch timestamps.
  - **[S2]** [Gamepur text walkthrough of The Shed](https://www.gamepur.com/guides/it-takes-two-the-shed-gameplay-tips-and-walkthrough-guide),
    for hammer/nail acquisition, target marks, platform pins, swing anchors,
    locks, Toolbox phases and chapter settlement.
  - **[S3]** [Neoseeker text walkthrough of The Shed](https://www.neoseeker.com/it-takes-two/walkthrough/The_Shed),
    for the same ordered Depths, Wired Up and boss transitions.
  - **[S4]** [Neoseeker text basics](https://www.neoseeker.com/it-takes-two/walkthrough/Basics),
    for co-op-only control and checkpoint return after pair failure.
  - **[S5]** [Twinfinite text health guide](https://twinfinite.net/guides/it-takes-two-heal-health-how/),
    for individual recovery and pair-wipe checkpoint behaviour.
- Claim IDs: `ITT-001`–`ITT-010`.

## Mechanical decomposition

### Action Genes

- Existing `ACT-008`: each player directly runs, jumps, dashes, wall-traverses
  and swings one protagonist; `ACT-049`: May strikes locally reachable marked
  buttons that change a linked mechanism.
- New `ACT-385`: Cody aims, throws and recalls one role-bound reusable nail;
  new `ACT-386`: May commits one hammer strike against a compatible reachable
  button, lock or launch fixture.
- Parameters: role, controller, target, aim, throw, recall, nail identity,
  hammer reach, swing direction and traversal timing.
- Claim IDs: `ITT-004`–`ITT-008`.

### System Behaviour Genes

- Existing `SYS-036`: bodies, falls, swings and collisions continue under live
  force; `SYS-065`: accepted switch or nail contact moves a linked authored
  platform; `SYS-215`: the Toolbox hazards, direct movement and damage resolve
  in real time.
- Existing `SYS-429` returns one failed partner without stopping the survivor;
  `SYS-430` restores the segment checkpoint only when neither actor remains.
- New `SYS-710`: an accepted nail hit persists contextually as a mechanism pin,
  switch contact or swing anchor until Cody recalls it, after which the same
  nail becomes available again.
- Resolution order: accept role input; validate tool, target and nail stock;
  resolve nail or hammer contact; update mechanism/anchor state; integrate live
  bodies and hazards; resolve individual return or pair reset; retain the next
  authored gate only when both roles have crossed.
- Claim IDs: `ITT-004`–`ITT-009`.

### Constraint Genes

- Existing `CON-047`: Cody's bounded reusable nail set cannot occupy two world
  anchors at once and must be recalled before reassignment; `CON-076`: hammer
  and nails grant different traversal/interaction permissions; `CON-378`:
  exactly two independent human input owners are required.
- New `CON-558`: nail deployment requires a currently available nail and a
  compatible marked surface or mechanism; unmarked geometry and already
  deployed stock reject the request.
- Scarce strategic resources: three later-stage nail identities, both living
  bodies, each actor's route position, visible hammer/nail target eligibility
  and the current hazard window.
- Claim IDs: `ITT-001`, `ITT-004`–`ITT-008`.

### Information Genes

- Existing `INF-001` exposes the current local route, marked tool targets,
  placed nails, mechanism state and boss hazards; `INF-167` exposes both live
  viewpoints concurrently so either player can read the partner's position,
  prompt and timing.
- Hidden future chapter abilities, hazards beyond the current authored view
  and network state do not enter the packet.
- Claim IDs: `ITT-001`, `ITT-003`–`ITT-008`.

### Objective Genes

- Existing `OBJ-086` carries both separately controlled protagonists through
  the bounded hammer-and-nails chapter packet, settles Toolbox and crosses the
  declared next-chapter transition.
- One reached ledge, checkpoint, broken lock or completed boss phase is
  intermediate; both actors and the complete post-boss transition define the
  positive terminal.
- Claim IDs: `ITT-008`, `ITT-009`.

### Time Genes

- Existing `TIM-003`: movement, platform travel, swinging, falling, boss
  hazards, damage and return windows continue while both players provide live
  input.
- Claim IDs: `ITT-004`–`ITT-009`.

## Reproducible transitions

| Before | Action | Deterministic or bounded resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Both players first retain hammer-and-nails control | Cody aims at a yellow target and throws one available nail | The nail attaches and leaves his available set until recall | exact bounded entry and reusable stock | `ITT-004`, `ITT-005` |
| A moving platform crosses a yellow pin aperture | Cody hits the aperture at the needed position | The nail holds the platform on its authored path so May can cross | role-specific state enables partner route | `ITT-005` |
| A yellow wall target is reachable from Cody | Cody places a nail; May jumps and swings from it | May's live body follows the anchor arc to otherwise unreachable geometry | placed tool becomes partner traversal | `ITT-005` |
| A marked button or lock is in May's hammer reach | May strikes it | The linked mechanism changes or the lock breaks; Cody's nail cannot substitute | complementary tool authority | `ITT-006` |
| Every nail is currently deployed | Cody attempts another throw, then recalls one | The extra throw is unavailable; recalled stock can be reassigned | finite reassignable nail inventory | `ITT-004`, `ITT-005` |
| Exactly one actor fails while the partner remains active | Failed player completes the recovery input | The surviving pane continues and the actor returns into the live segment | survivor-held recovery | `ITT-007` |
| Both actors fail inside one hazard interval | Resolve overlapping pair failure | The authored checkpoint reloads and transient tool/hazard state resets | pair-wipe boundary | `ITT-007` |
| Toolbox arm is exposed over the hole | Cody pins the arm and places the remaining anchors; May swings and strikes the locks | The staged guard opens only through both tool roles | cooperative boss dependency | `ITT-008` |
| Final launch fixture and explosive can are exposed | May hammer-launches Cody; Cody reaches and nails the can | Toolbox health reaches zero and the post-boss transition begins | final role handoff | `ITT-008` |
| Post-boss transition completes | Retain the chapter result | `The Shed` closes and the next chapter becomes the new progress boundary | explicit positive terminal | `ITT-009` |

## Strategic and experiential structure

- Planning horizon: identify which marked target belongs to hammer or nail,
  reserve enough nail stock for the next platform and swing, and order the two
  routes so the acting partner does not strand the other.
- Local tactics: announce nail placement/recall, time May's swing against the
  live arc, pin moving machinery only at a crossable pose and keep one survivor
  active during hazard recovery.
- Long-term structure: repeated complementary tool states teach a stable
  grammar, then the Toolbox fight recombines pin, swing, lock and launch into
  one shared chapter settlement.
- Reversible versus irreversible: nail placement is freely recalled;
  checkpoint-local failures reset; each completed authored gate and the final
  chapter transition are retained.
- Failure attribution: the split panes, yellow target marks, visible nails,
  mechanism motion and recovery state distinguish a wrong role, unavailable
  nail, timing miss, individual fall and pair wipe.
- Player trust: neither role is decorative. Each owns visible operations that
  the other cannot impersonate, while the partner pane avoids requiring an
  external stream or hidden walkthrough.

## Replay and variation

- What changes: human-to-role assignment, communication, nail order, platform
  timing, movement execution and boss-dodge paths.
- Randomness or procedural generation: none in the scoped authored packet.
- Multiple viable strategies: local movement and recall timing vary, but the
  mandatory tool dependencies and chapter order are authored.
- Typical replay motive: swap Cody/May roles, improve coordination or replay
  the chapter; later abilities and optional minigames are separate modules.

## Adjacent systems and history

- Direct successor corridor: Split Fiction shares Hazelight's mandatory
  two-human split-screen, actor ownership and recovery boundary, but changes
  abilities and chapter mechanics.
- Similar games: Portal 2 Cooperative Campaign uses paired humans, portals and
  chamber gates; A Way Out is an external reserve, not current corpus evidence.
- Important differences: It Takes Two fixes complementary reusable hammer and
  nail tools for this packet. Its nail can be recalled among pin, switch and
  swing roles, while Split Fiction's scoped Chapter 1 centres generic paired
  gates and temporary pilot/gunner authority.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-049`, `ACT-385`, `ACT-386` | direct traversal, switch, nail and hammer input |
| System Behaviour | `SYS-036`, `SYS-065`, `SYS-215`, `SYS-429`, `SYS-430`, `SYS-710` | body/platform physics, combat, recovery and contextual nail state |
| Constraint | `CON-047`, `CON-076`, `CON-378`, `CON-558` | reusable stock, role ownership, two humans and target eligibility |
| Information | `INF-001`, `INF-167` | visible tool state and concurrent partner pane |
| Objective | `OBJ-086` | complete the bounded cooperative chapter packet |
| Time | `TIM-003` | continuous traversal, mechanisms and hazards |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `214` (`GAME-0001`–`GAME-0214`).
- Exact genome matches: none.
- Tied near matches: `GAME-0157` — Split Fiction (`12 / 22 = 0.545455`).
- Supported combination subsets: `COMB-0213`.
- Scan date: 2026-09-01.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0157` — Split Fiction | `ACT-008`, `ACT-049`, `SYS-036`, `SYS-065`, `SYS-429`, `SYS-430`, `CON-076`, `CON-378`, `INF-001`, `INF-167`, `OBJ-086`, `TIM-003` | Both require two human-controlled protagonists, concurrent partner panes, live authored traversal, role permissions and the same individual-return/pair-reset boundary. Split Fiction adds explicit paired prompts and temporary vehicle authority. It Takes Two instead fixes a finite recallable nail inventory, eligible yellow nail targets, May-only hammer fixtures and direct Toolbox hazard resolution whose ordered states create platforms, swing anchors and the chapter settlement. | Near, `0.545455` |

### Preserved research notes

- New genes: `ACT-385`, `ACT-386`, `SYS-710`, `CON-558`.
- Reused genes: `ACT-008`, `ACT-049`, `SYS-036`, `SYS-065`, `SYS-215`,
  `SYS-429`, `SYS-430`, `CON-047`, `CON-076`, `CON-378`, `INF-001`,
  `INF-167`, `OBJ-086` and `TIM-003`.
- Classification result: `New gene` and new verified interaction combination.
- Evidence and reasoning: the generic two-human, split-view, live-platform and
  recovery layer is reused without signature drift. New records isolate only
  direct nail/hammer commitments, contextual persistent nail state and its
  marked-surface/available-stock gate.

## Taxonomy impact

- Registry changes: `ACT-385`, `ACT-386`, `SYS-710`, `CON-558`; existing
  records gain It Takes Two evidence only.
- Taxonomy-change record: none; no prior signature or lifecycle changes.
- Candidate terms affected: reusable nail, hammer fixture, mechanism pin,
  swing anchor, role-bound tool and pair-wipe recovery.

## Negative results

- `ACT-256` and `CON-379` are rejected: the admitted dependencies are normally
  ordered tool states, not one simultaneous paired prompt.
- `INF-050` is rejected: both local panes are visible; rules and state are not
  split into hidden Defuser/Expert information roles.
- A general inventory or crafting gene is rejected: nails neither drop as loot
  nor enter an equipment economy; they are a bounded reusable world-tool set.
- Friend's Pass and online entitlement are excluded environment/access state,
  not causal members of the local couch-co-op decision loop.

## Delta summary

## Нові факти

- [Confirmed | Direct | High] Поточний локальний Windows-режим вимагає двох
  людей, одночасно показує обидві половини екрана й у вибраному відрізку
  надає Коді цвяхи, а Мей — молоток (`ITT-001`–`ITT-006`).
- [Observation | Corroborated | High] Послідовність «прикріпити — перейти —
  відкликати — перепризначити» зводить ролі до спільної перемоги над Toolbox і
  завершення The Shed (`ITT-007`–`ITT-009`).

## Нові гени

- [Observation | Corroborated | High] `ACT-385`, `ACT-386`, `SYS-710`,
  `CON-558`.

## Нові комбінації

- [Observation | Corroborated | High] `COMB-0213`.

## Зміни таксономії

- [Observation | Corroborated | High] Змін життєвого циклу чи сигнатур раніше
  перевірених ігор немає.

## Нові питання

- Чи повторює пізніший фіксований набір здібностей ту саму залежність ролей без
  молотка, цвяхів і імпорту всієї кампанії?

## Наступна рекомендована гра

- [Confirmed | Direct | High] `GAME-0216` — Trackmania.
- Optimisation criterion: перейти від обов'язкової двоосібної координації до
  одного детермінованого заїзду на час.
- Expected information gain: перевірити старт, контрольні точки, фініш,
  повторний старт, збережений час і медаль за одного стабільного треку.
- Backlog impact: продовжити активний Goal, не починаючи `GAME-0216` у цьому
  unit.

## Чому саме вона

- [Hypothesis | Limited | High] Це остання записана гра Batch 009 і найбільша
  жанрова та часова відстань від спільного авторського розділу.
