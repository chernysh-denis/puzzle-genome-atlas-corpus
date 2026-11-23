---
game_id: GAME-0590
slug: tokyo-xtreme-racer
game_title: Tokyo Xtreme Racer
analysis_status: reviewed
reviewed: 2026-11-21
combination_ids: []
gene_ids:
  action:
    - ACT-290
    - ACT-341
  system:
    - SYS-045
    - SYS-1738
    - SYS-1739
  constraint:
    - CON-843
  information:
    - INF-179
    - INF-204
    - INF-556
  objective:
    - OBJ-322
  time:
    - TIM-003
---

# Game: Tokyo Xtreme Racer

Use the [canonical vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
Catch the first rival, flash the headlights and build a lead on the
expressway. Settle the duel by exhausting the other driver's Spirit Points.

## Analysis scope

- Version / ruleset: Genki's September 2025 full Windows Steam release,
  Ver.1.0.0, Steam app 2634950. Genki dates the update 25 September 2025.
  Steam's English store view shows 24 September. Choose a fresh English
  single-player game, choose Challenge for reproduction and use the
  stock Toyota Sprinter Trueno GT-APEX (AE86) without battle perks.
  The source run shows the restrictions selector, starter car and first
  road entry. The selection of Challenge is a reproducible setup choice,
  not an assertion that perk mode changes this first unmodified duel.
- Structured analysis target: PLAT-WINDOWS-PC.
  See [platform coverage](../../platforms/games.json).
- Entry: the first tutorial free drive from Kandabashi C1 Inner Loop,
  with Timid Challenger moving on the same road. Buying the starter and
  choosing this ramp prepare the initial state outside the active packet.
- Primary decision loop: approach the marked rival from behind in the
  required window, initiate the headlight challenge, and resume direct
  driving when the rolling start releases control. Read the signed
  relation to the rival, the two Spirit Point (SP) bars and traffic.
  Take the lead and hold sufficient separation while following bends
  and avoiding costly contact.
- Positive exit: the rival's SP reaches zero first and the game displays
  WIN. The same road returns to ordinary driving after settlement and
  the tutorial explanation. Stop before initiating a second race or
  returning to the garage.
- Negative exit: when the player's own SP is exhausted first without
  recovery perks, the duel is lost. A position reversal can redirect
  distance pressure toward the player. Failed offer eligibility leaves
  the car in free drive. Loss is documented as an ordinary SP terminal
  but no losing Timid Challenger trial is isolated in the release clip.
- Included: road approach, range and target gate, rolling start, direct
  steering, autonomous rival and traffic, alternate SP loss through
  separation and eligible collisions, HUD feedback, two-sided
  settlement and handoff back to driving.
- Excluded: issuing a second challenge after return, garage progression,
  tutorials after the result, tyre-wear coefficients, saving, special
  rival requirements, recovery/launch perks and later story, January
  Early Access, later Steam patches, console ports and earlier games
  with the same title.
- Potential scoped module: one declared Wanderer with verified eligibility
  rules and a qualifying race, using a separately identified release.
- Direct-play status: no native inputs or game execution. Genki identifies
  the full release, start and competitive SP and collision rules. The
  dated Ver.1.0.0 stills establish the first approach, rolling start,
  increasing lead, WIN and highway return. A later match in the same
  capture and other full-release accounts corroborate contact pressure.
  Exact binary hash, controller assignments, SP/gap coefficients,
  simultaneous exhaustion and abort priority remain unverified.
  Video and audio were not played.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
| --- | --- | --- | --- | --- | --- |
| TXR-001 | This packet uses Genki's complete Windows Steam 1.0.0 release dated 25 September 2025 by Genki. Early Access had an incomplete story and the 1.0 release changed both SP and collision damage. | Confirmed | Direct | High | P1, P2 |
| TXR-002 | The recorded new game reaches the tutorial ramp from the garage in a stock Sprinter Trueno. Its live car can steer, accelerate and brake on the same expressway used for the challenge. | Observation | Corroborated | High | W1 2:20/2:30/4:00/4:10; P3 |
| TXR-003 | Approaching an eligible marked rival from behind exposes the challenge. The headlight signal accepts that local target and creates an SP Battle on the road, with a rolling start and two opposing gauges. It is distinct from merely driving alongside another vehicle. | Observation | Corroborated | High | P3; W1 4:00/4:10/4:20; R1 |
| TXR-004 | A sufficient lead applies repeated SP loss to the trailing driver while both keep driving. Which side trails matters. Close running alone does not establish gap damage, and a lead does not win until settlement. Exact threshold and drain function for the chosen unmodified 1.0.0 rules were not measured. | Observation | Corroborated | High | P1, P2; W1 4:20/4:30/4:40/4:50; R1, R2 |
| TXR-005 | Qualifying contact with road obstacles or traffic can incur collision SP damage independently of being the trailing driver. Genki distinguishes this calculation from ordinary SP pressure and changed the speed response for 1.0.0. One later sample shows a traffic overlap and damage feedback while the player leads. The stills do not isolate angle, impulse or exact damage. | Observation | Corroborated | Medium | P2; W1 5:50/6:00/6:10; R1, R3 |
| TXR-006 | The driving display retains speed, gear, minimap and road cues. The challenge adds rival identification, elapsed battle time, a relative separation cue and both remaining Spirit Point bars. Ordinary traffic can still occupy the road. | Observation | Corroborated | High | W1 4:10/4:20/4:30/4:40/5:20/6:00 |
| TXR-007 | The battle ends in WIN when the rival runs out of SP first. Without a recovery perk, exhausting the player's own SP first instead loses. Settlement does not depend on a lap count or finish line. The recorded road resumes after the result. | Observation | Corroborated | High | P1, P3, P4; W1 4:40/4:50/5:00/5:20; R1, R2 |

## Basic data

- Genki Co., Ltd. FAM-010 covers continuous tactical decisions while the
  trailing reserve depletes and traffic and geometry change.
- P1: [Genki's Windows Steam app](https://store.steampowered.com/app/2634950/Tokyo_Xtreme_Racer/).
  The official product listing identifies the single-player game, English
  support, Genki and depletion of the rivals' Spirit Points.
- P2: [Genki's dated 1.0.0 release notes](https://tokyoxtremeracer-us.genki.co.jp/news/release-notes_1_0_0.html).
  Distinguishes the full story, the optional perk-tree restriction and
  separate adjustments to SP and collision damage. The exact equations
  are absent.
- P3: [Genki's product mechanics](https://tokyoxtremeracer-us.genki.co.jp/).
  Identifies the moving headlight challenge and Spirit Point competition.
  It now also references the PS5 edition; that platform is not analysed.
- P4: [Genki's 1.0.2 release notes](https://tokyoxtremeracer-us.genki.co.jp/news/release-notes_1_0_2.html).
  Documents an exception in earlier builds to the usual zero-SP loss
  when a recovery skill could intervene. Used to qualify, not expand,
  the stock-car no-perk terminal.
- W1: [Full Release Ver.1.0.0 opening capture](https://www.youtube.com/watch?v=txBCjMyJRXw)
  published 25 September 2025. Static frames show preset selection near
  1:10, garage and ramp at 2:20–2:40, challenge tutorial at 4:00, road
  approach at 4:10, rolling GO at 4:20, lead and depletion at 4:30–4:40,
  WIN at 4:50 and renewed free driving at 5:20. A second race on the
  same recording supplies a contact comparison at 5:50–6:10. The
  second win at 6:20 is corroboration, outside the packet's exit.
- R1: [PC Gamer's own-play account](https://www.pcgamer.com/games/racing/tokyo-xtreme-racer-review/).
  Reproduces an eligible headlight challenge, then racing through
  traffic to empty the opponent's SP. It does not establish build
  1.0.0 parameters.
- R2: [Predy's published mechanics account](https://www.predygames.com/en/media/games/tokyo-xtreme-racer/).
  Corroborates separation-based loss and the zero-SP outcome. It also
  notes later perk variations. Its numerical gap is not used as an
  authenticated measurement for the selected release and setup.
- R3: [Soufu's September full-release play notes](https://note.com/soufu3414/n/n13539f7bfdd4?hl=en).
  Corroborates costly contact under full-release play and the difference
  between the base and raised SP/attack statistics.
- Sources accessed 2026-11-21.

## Mechanical decomposition

### Action Genes

- ACT-290 directly steers, brakes and applies power to the assigned car.
  ACT-341 addresses the reachable marked rival with the headlight prompt
  and turns that road encounter into an active duel (TXR-002, TXR-003).

### System Behaviour Genes

- SYS-045 advances Timid Challenger and nearby road actors without
  separately issued movement instructions (TXR-002, TXR-006).
- SYS-1738 continuously applies separation pressure to the trailing
  driver at a qualifying gap. Position changes determine whose
  reserve is subject to loss (TXR-004).
- SYS-1739 applies an additional collision loss to a competitor's duel
  reserve on a qualifying impact. A lead does not protect a car from
  this consequence (TXR-005).

### Constraint Genes

- CON-843 restricts the in-world challenge to the appropriate local
  approach and target state. The headlight input alone at an arbitrary
  point on the road does not admit this duel (TXR-003).

### Information Genes

- INF-179 exposes local obstacles, traffic and the marked challenge target
  in the driving view. INF-204 exposes speed, gear and route cues
  (TXR-002, TXR-006).
- INF-556 overlays current reserves for both drivers and the rival's
  relative gap, separately from speed and gear (TXR-004, TXR-006).

### Objective Genes

- OBJ-322 exhausts the opponent's race reserve before the player's,
  settling the fixed pair's road duel independently of circuit
  progress (TXR-004, TXR-007).

### Time Genes

- TIM-003 keeps the race live while the player steers, changes speed,
  follows traffic and manages the gap. The shown battle clock is elapsed
  time, with no universal fixed deadline inferred here (TXR-003–TXR-007).

## Reproducible transitions

| Initial state | Intervention | Discriminating result | Evidence |
| --- | --- | --- | --- |
| Fresh car enters Kandabashi C1 Inner Loop | Drive through the opening section toward the named rival | Free driving and local road guidance precede the challenge HUD. | TXR-002, TXR-006 |
| Timid Challenger is visible ahead | Close to the eligible approach and flash the headlights | The same road hosts a rolling start, then two SP bars and live control at GO. | TXR-003 |
| Both drivers are still close after the rolling start | Follow the bend and maintain enough speed to take the lead | The trailing marker passes behind the player's car. Being marginally ahead does not itself settle the result. | TXR-004, TXR-006 |
| The player has opened a sufficient gap | Maintain the lead while reading the road | The rival's bar contracts while the player's remains positive. The car still travels after the rival drops out of forward view. | TXR-004, TXR-006 |
| A competitor passes near nonparticipating traffic | Compare a clear lead pass with a qualifying side or barrier contact | The contact can damage the competitor even with the rival behind. This is a separate reason to leave room when passing. | TXR-005 |
| A driver runs out of SP while the other has some left | Continue to the first fully settled result | Rival zero yields WIN. Player zero under the same stock setup is the loss branch. | TXR-007 |
| The victory result is visible on the road | Allow the result and additional tutorial to clear | The car is again in free driving. The next challenge is outside the packet. | TXR-007 |

## Strategic and experiential structure

Before the start, closing a gap earns the opportunity to battle. Once
the opponent accepts, extending a gap while ahead is useful. The front
car still has to manage curves, barriers and traffic. Taking a straight
line at high speed can temporarily grow a lead but may cost SP through
contact or slow the car enough for the rival to regain pressure.

## Replay and variation

The second challenge on the same recording illustrates that Timid
Challenger can be challenged again after the first outcome. It begins
at a different road position and contains a traffic contact. Only the
first tutorial duel is part of the signature. No claim is made about
the traffic seed or availability of every rival after replay.

## Adjacent systems and history

OutRun 2 shares direct steering, traffic, road cues and live movement,
but its timed sections and route gates do not settle a reserve duel.
Need for Speed Underground similarly demands surviving the driving line
around traffic and barriers where applicable, but wins its selected race
through a classified finish. Here a nearby rival enters the bout from
ordinary road movement, and exhaustion determines the result on course.

## Normalised genome

| Type | Active gene IDs | Carrier parameters |
| --- | --- | --- |
| Action | ACT-290, ACT-341 | direct driving and nearby headlight challenge |
| System Behaviour | SYS-045, SYS-1738, SYS-1739 | autonomous actors, gap drain and impact damage |
| Constraint | CON-843 | qualifying trailing approach and eligible rival |
| Information | INF-179, INF-204, INF-556 | road and speed HUD, two reserves and relative gap |
| Objective | OBJ-322 | empty the other driver’s SP first |
| Time | TIM-003 | real-time road duel |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `589` (`GAME-0001`–`GAME-0589`).
- Exact genome matches: none.
- Tied near matches: `GAME-0578` — OutRun 2 (`4 / 19 = 0.210526`).
- Supported combination subsets: none.
- Scan date: 2026-11-21.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
| --- | --- | --- | --- |
| OutRun 2 (GAME-0578) | ACT-290, INF-204, SYS-045, TIM-003 | Both require live control and road reading around moving traffic. OutRun 2 resolves timed sections and their continuations; the C1 duel uses relative position and contact to exhaust a rival’s separate reserve. | 4 shared of 19 in union, 0.210526 (21.05%) |

### Preserved research notes

- New genes: SYS-1738, SYS-1739, CON-843, INF-556 and OBJ-322.
- Classification result: New gene.

## Taxonomy impact

- [TAXONOMY_CHANGE_336](../../../research/taxonomy-changes/TAXONOMY_CHANGE_336.md)
  isolates the relative gap and contact rules, race challenge gate,
  two-reserve display and no-finish-line duel settlement.

## Negative results

- Crossing a certain location or finishing a lap is not the win
  condition. A sufficient lead applies pressure but is not the terminal.
- Neither an exact gap threshold nor an SP equation is established for
  the 1.0.0 stock car. Later perk, launch and recovery behavior is outside
  this bounded duel.
- A road contact is not a takedown, a mechanical wreck requirement or an
  ordinary reversible approach. The separate rule reduces Spirit Points.
- CP, BP, garage spending, tyre durability coefficients and route
  unlocking are not inferred from the mandatory tutorial explanation
  after the selected race.

## Delta summary

## New facts

- [Observation | Corroborated | High] The eligible road encounter starts
  a two-reserve race and settles visibly before an authored finish line.

## New genes

- [Observation | Corroborated | Medium] Five additive boundaries in
  TAXONOMY_CHANGE_336, including distinct gap and impact effects.

## New combinations

- [Observation | Corroborated | High] No new verified combination
  proposed. See the complete existing-subset analysis above.

## Taxonomy changes

- [Observation | Corroborated | Medium] Earlier definitions,
  combinations and signatures are retained.

## New questions

- Controlled 1.0.0 driving could measure the lead threshold, damage
  response and ties for an unmodified battle. More counterfactuals
  are needed before adding other settlement paths.

## Next recommended game

- [Hypothesis | Limited | Medium] GAME-0591, Fatal Frame on the 2002
  North American PlayStation 2 retail release. Compare an opening
  investigation and completed Camera Obscura confrontation.
- Optimisation criterion: contrast reading a live road duel with
  sightline and exposure decisions under pressure.

## Why this game

- [Hypothesis | Limited | Medium] The opening duel cleanly contrasts a
  continuously depleting positional resource with finish-order racing.
