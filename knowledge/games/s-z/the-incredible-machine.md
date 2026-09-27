---
game_id: GAME-0421
slug: the-incredible-machine
game_title: The Incredible Machine
analysis_status: reviewed
reviewed: 2026-09-27
combination_ids: []
gene_ids:
  action:
    - ACT-028
  system:
    - SYS-036
    - SYS-1115
  constraint: []
  information:
    - INF-001
  objective:
    - OBJ-014
  time:
    - TIM-006
---

# Game: The Incredible Machine — manual's basketball contraption

Use the canonical [vocabulary and genome rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). The mouse, belt, bowling balls, basketball and hoop are parameters of this bounded apparatus, not universal gene names.

## Analysis scope

- Version / ruleset: the original English DOS *The Incredible Machine* described by Sierra/Dynamix's original printed manual, not *The Even More Incredible Machine*, later sequels or the retrospective Mega Pack. The analysed packet is the manual's worked basketball-to-hoop puzzle. Exact executable revision was not inspected.
- Structured analysis target: `PLAT-DOS` in [`knowledge/platforms/games.json`](../../platforms/games.json).
- Primary decision loop: inspect the visible goal, supplied parts and immovable starting apparatus; place and orient the available mouse motors, belts and ramp so falling bowling balls start a chain of wheel-driven conveyors; run the machine, observe the basketball's motion, stop and revise if it misses, and complete the puzzle when the basketball enters the hoop.
- Entry and exit: open the original DOS puzzle described in the manual's worked example before placing movable parts. Its fixed basketball, hoop, bowling-ball releases and conveyor apparatus are present. Positive exit is the basketball entering the hoop during a run. A stalled motor, disconnected belt or missed hoop leaves the puzzle unresolved and permits a new edit-test attempt.
- Included: finite supplied parts; persistent pre-run positioning and belt-endpoint attachment; immovable preset objects; gravity and collision of balls; mouse motors activated by bowling-ball contact; attached belts powering conveyors; conveyor-carried basketball; manually started/stopped simulation and resettable edit-test cycle; visible target and current layout.
- Excluded: free-form mode, gravity/air-pressure sliders, other puzzle goals, other machine parts, later levels, sequels, exact ball velocities, belt torque, collision frames, numerical scoring, sound and cosmetic animation. The manual's worked arrangement is evidence for a valid route, not proof it is the only solution.
- Potential scoped modules: a different named puzzle with fans or cats; measured physics from an identified DOS executable; free-form construction as a separate ruleset.
- Direct-play status: no original disk, executable, input trace, screenshot, video or audio was inspected. The publisher's illustrated manual is direct rules evidence; a later Sierra Help walkthrough corroborates the chain but disagrees about its puzzle number. We therefore identify the packet by its described basketball goal, not an asserted in-game menu number.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `TIMACH-001` | Puzzle mode presents a target and an available parts bin; certain placed starting objects cannot be moved. | Confirmed | Direct | High | P1 |
| `TIMACH-002` | In the basketball example, falling bowling balls start mouse motors, whose wheels are linked by attached belts to conveyors. | Confirmed | Direct | High | P1; S1 |
| `TIMACH-003` | A driven conveyor carries the basketball toward a placed ramp and fixed hoop. | Confirmed | Direct | High | P1; S1 |
| `TIMACH-004` | Players place, orient, remove and connect parts before starting the simulation, and may stop a run to change the design. | Confirmed | Direct | High | P1 |
| `TIMACH-005` | Gravity, contact and moving-machine effects determine whether the basketball reaches the hoop during a run. | Confirmed | Direct | High | P1 |
| `TIMACH-006` | The printed manual labels its worked basketball example puzzle no. 5, while a later Sierra Help walkthrough assigns a similar sequence to its first listed puzzle. The exact in-game menu number was not independently verified. | Observation | Corroborated | High | P1; S1 |
| `TIMACH-007` | Exact velocities, power-transfer formulae, uniqueness of the demonstrated solution and reset-frame behaviour are not established by these sources. | Observation | Limited | High | P1 |

## Basic data

- Release / origin: Sierra On-Line published the original *The Incredible Machine* for DOS in the early 1990s; the scanned Sierra/Dynamix manual is the edition-specific rules source. No claim of an exact release date is needed for this packet.
- Platform or physical form: single-player DOS construction puzzle, pointer-driven editable layout followed by an automatic physical run.
- Mechanical family: automation and spatial programming (`FAM-008`) because the player configures machine geometry before execution rather than steering the basketball directly.
- Sources accessed 2026-09-27:
  - **P1** — [Sierra/Dynamix original *The Incredible Machine* DOS manual scan](https://www.retrogames.cz/manualy/DOS/The_Incredible_Machine_-_DOS_-_Manual.pdf), printed pp. 8–11 for editing, starting and stopping a puzzle; printed p. 16 for the three-motor basketball worked example. This is a preserved publisher manual scan, not an executable or an authorised download of the game.
  - **S1** — [Sierra Help walkthrough](https://sierrahelp.com/Walkthroughs/TheIncredibleMachineWalkthrough.html), the “Put the Ball in the Hoop” entry, for independent prose corroboration of the bowling-ball, mouse motor, belt, conveyor, ramp and hoop chain. Its numbering is not used as a verified original-menu index.
  - **P2** — [Disney Games and Apps Support, series overview](https://appsupport.disney.com/hc/en-us/articles/360001041463-About-The-Incredible-Machine-Mega-Pack), for later rightsholder confirmation of mouse-powered contraptions and the series identity only; its Mega Pack contents and compatibility do not define this original DOS ruleset.

## Mechanical decomposition

### Action Genes

- `ACT-028`: put the supplied motors and ramp into effective positions and attach belt components between motor wheels and conveyor drive wheels. Move or remove editable pieces before each run; preset objects remain fixed. `TIMACH-001`, `TIMACH-002`, `TIMACH-004`.

### System Behaviour Genes

- `SYS-036`: after Run, the bowling balls fall and collide, and the basketball responds to active conveyor, ramp and hoop geometry. This is continuous physical motion, not a tile step or instant teleport. `TIMACH-002`, `TIMACH-003`, `TIMACH-005`.
- New `SYS-1115`: contact from a falling bowling ball starts a mouse motor; the motor wheel transfers drive through an attached belt to a conveyor, which moves a contacting payload. A missing contact or missing belt breaks the causal chain. This is neither a logic-signal graph nor a permanently self-running factory belt. `TIMACH-002`, `TIMACH-003`.
- Resolution order: commit layout and links → start simulation → falling bowling balls contact motor triggers → running wheels drive connected conveyors → basketball travels along driven surfaces and placed ramp → hoop contact completes the puzzle or a miss prompts a stop and revised design. `TIMACH-002`–`TIMACH-005`.

### Constraint Genes

- No separate constraint is admitted. The finite parts supply and immovable preset pieces are parameters of `ACT-028`'s edit space, not evidence for a transferable one-purpose placement prohibition. An unattached belt fails to transmit `SYS-1115` power rather than becoming a general inventory constraint.

### Information Genes

- `INF-001`: the current parts, supplied inventory, target and machine geometry needed for this worked solution are visible while editing and testing. The source does not establish an intentionally hidden state for this packet. `TIMACH-001`, `TIMACH-004`.

### Objective and Time Genes

- `OBJ-014`: deliver the dynamic basketball into the fixed hoop. Moving a motor or merely starting a conveyor is not completion. `TIMACH-003`.
- `TIM-006`: layout and belt editing are self-paced; Run commits a multi-cycle automatic simulation, and stopping returns to design revision. No live in-run editing is admitted. `TIMACH-004`, `TIMACH-005`.

## Reproducible transitions

| Before | Action | Bounded resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Worked basketball puzzle open | Inspect target, fixed apparatus and parts bin | Hoop, basketball and available motors, belts and ramp are legible | visible edit problem | `TIMACH-001` |
| Machine is stopped | Place motor wheels and ramp, attach belts to conveyor drives | Persistent spatial and connection design is saved for the next test | build phase | `TIMACH-002`, `TIMACH-004` |
| Parts connected | Click Run | Bowling balls fall into mouse-motor triggers | autonomous contact stage | `TIMACH-002`, `TIMACH-005` |
| Motor triggered and belt attached | Let run continue | Mouse wheel drives connected conveyor; basketball advances toward ramp | mechanical power pathway | `TIMACH-002`, `TIMACH-003` |
| Basketball reaches final conveyor | Let it follow the positioned ramp | Basketball enters hoop if geometry is sufficient | receiver objective | `TIMACH-003` |
| Belt absent, motor untriggered or ball misses | Stop, edit and run again | No victory; revised design can be retested | failure and revision boundary | `TIMACH-004`, `TIMACH-007` |

## Strategic and experiential structure

- The immediate decision is geometric: where can the finite motors, belts and ramp connect fixed input balls to the final basketball trajectory?
- The middle decision is causal: a visible but stationary conveyor is not enough; its motor must first be struck and linked.
- The long decision is iterative: each run tests a complete layout. A failed run gives spatial feedback, but no exact frame-perfect solution is asserted.

## Replay and variation

The described goal and starting apparatus are authored rather than a random board. Multiple placements may work; the manual's example only demonstrates one. Different selected puzzles and free-form mode are outside this record.

## Adjacent systems and history

*Opus Magnum* and *Infinifactory* also configure an automatic machine before running, but their instructions and item transport do not make bowling-ball contact start a mouse motor and transfer power by an attached belt. *Railbound* lays a route for a carriage without physical motor activation. *Cut the Rope* shares a dynamic object delivered to a fixed receiver, but its player cuts a live rope rather than prebuilding a chain-driven conveyor.

## Normalised genome

| Type | Active gene IDs | Key parameters |
|---|---|---|
| Action | `ACT-028` | finite motors, belts, ramp and fixed apparatus |
| System Behaviour | `SYS-036`, `SYS-1115` | gravity, collision, mouse-motor contact and belt drive |
| Constraint | none | fixed pieces and finite parts are action parameters |
| Information | `INF-001` | visible target, bin and layout |
| Objective | `OBJ-014` | basketball enters fixed hoop |
| Time | `TIM-006` | edit, run, stop and revise |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `420` (`GAME-0001`–`GAME-0420`).
- Exact genome matches: none.
- Tied near matches: `GAME-0021` — Cut the Rope (`3 / 12 = 0.250000`); `GAME-0042` — Infinifactory (`3 / 12 = 0.250000`).
- Supported combination subsets: none.
- Scan date: 2026-09-27.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| Cut the Rope (`GAME-0021`) | `SYS-036`, `INF-001`, `OBJ-014`: visible physics guides a dynamic payload into a fixed receiver | Cut the Rope severs live ropes while the candy moves (`ACT-027`, `TIM-003`); this packet arranges a motor-and-belt machine before a resettable run (`ACT-028`, `SYS-1115`, `TIM-006`) | Near, `0.250000` |
| Infinifactory (`GAME-0042`) | `ACT-028`, `INF-001`, `TIM-006`: visible layout is edited before an automatic test | Infinifactory's discrete conveyor pieces transform recurring assemblies; the manual's machine uses falling-ball contact and a linked motor to drive a continuously moving basketball into a fixed hoop (`SYS-036`, `SYS-1115`, `OBJ-014`) | Near, `0.250000` |

## Taxonomy impact

[`TAXONOMY_CHANGE_159`](../../../research/taxonomy-changes/TAXONOMY_CHANGE_159.md) admits `SYS-1115` as a distinct physical activation and belt-drive transition. Earlier signatures and verified combinations remain unchanged.

## Negative results

- `SYS-077` rejected: Infinifactory's discrete conveyor advances assemblies in authored cycles; the scoped balls move continuously under contact and gravity.
- `SYS-157` rejected: Factorio belts transport ongoing factory items without a per-run mouse wheel activated by a falling bowling ball.
- `SYS-192` rejected: no programmable sensor or logic signal is needed to start a mouse motor; the trigger is physical contact.
- A separate belt-attachment Action rejected: the attached belt is a placed persistent component already covered by `ACT-028`.
- Puzzle number, exact physics, unique solution and executable revision remain unverified because the source set is a printed manual plus later walkthrough, not direct play.

## Delta summary

The player does not fling the basketball directly. They build a finite machine before the run, use bowling-ball contact to start mouse motors, carry power across attached belts to conveyors, and guide the basketball into a fixed hoop.

## New facts

- [Confirmed | Direct | High] The original publisher manual explicitly works through mouse motors linked by belts to conveyors in a basketball-to-hoop puzzle (`TIMACH-002`, `TIMACH-003`).

## New genes

- [Observation | Direct | High] `SYS-1115` separates contact-triggered motor/belt drive from generic dynamic-body physics or always-running transport.

## New combinations

- [Observation | Direct | High] None created; every verified combination will be checked as a proper subset of this six-gene genome.

## Taxonomy changes

- [Observation | Direct | High] `TAXONOMY_CHANGE_159` records the new powered-conveyor boundary without changing prior signatures.

## New questions

- Which exact original DOS executable and menu slot reproduce the printed basketball example, given the later guide's conflicting number?
- What belt-drive timing and ball-contact thresholds are measurable in a direct-play trace?

## Next recommended game

- [Hypothesis | Limited | Medium] `GAME-0422` *Patapon* on the original PSP after this unit's validation, local commit and Goal stop window.
- Optimisation criterion: shift from physical build-test-revise to rhythmic input and autonomous formation response.
- Backlog impact: preserve approved `GAME-0422`–`GAME-0432` order; do not start another subject in this unit.

## Why this game

- [Hypothesis | Direct | Medium] The original manual's worked machine provides a falsifiable activation-and-drive chain absent from generic placement or passive physics, while the fixed hoop makes the result objectively testable.
